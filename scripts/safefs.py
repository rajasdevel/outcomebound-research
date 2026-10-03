"""Write files below a root without following a symbolic link. Standard library only.

`render.py` and `collect.py` write generated files and queue entries inside this repository. A
symbolic link at a destination, or at any folder above it, would send the write somewhere else.
These helpers refuse that in two ways:

- `refuse_links` walks the destination from the root and refuses a link at any step. It is a
  check made before work starts, so a person gets one clear message.
- `open_below` opens each folder with `O_NOFOLLOW` relative to the descriptor of the folder above
  it, and the file the same way, so a link swapped in after the check is still not followed.

A platform without `O_NOFOLLOW` or descriptor-relative opens cannot give either guarantee; the
helpers refuse to write there instead of writing unsafely. The root itself is trusted, and may be
reached through a link; only the steps below it are judged.
"""

from __future__ import annotations

import errno
import os
import stat
from pathlib import Path, PurePosixPath

SUPPORTED = hasattr(os, "O_NOFOLLOW") and hasattr(os, "O_DIRECTORY") and os.open in os.supports_dir_fd


class UnsafePath(OSError):
    """A destination that is, or sits under, a symbolic link or a non-regular file."""


def _steps(rel: str) -> tuple[str, ...]:
    path = PurePosixPath(rel)
    if path.is_absolute() or not path.parts or ".." in path.parts or "." in path.parts:
        raise UnsafePath(f"{rel}: not a path below the repository")
    return path.parts


def refuse_links(root: Path, rel: str, folder: bool = False) -> None:
    """Raise UnsafePath when a step of `rel` below `root` exists as anything but a plain folder
    (or, for the last step, a plain file, or a plain folder when `folder` is true). A step that
    does not exist yet is fine."""
    current = root
    parts = _steps(rel)
    for index, part in enumerate(parts):
        current = current / part
        try:
            mode = os.lstat(current).st_mode
        except FileNotFoundError:
            return
        except OSError as error:
            raise UnsafePath(f"{rel}: cannot inspect {part}: {error.strerror}") from error
        if stat.S_ISLNK(mode):
            raise UnsafePath(f"{rel}: {'/'.join(parts[: index + 1])} is a symbolic link")
        last = index == len(parts) - 1
        if last and not (stat.S_ISDIR(mode) if folder else stat.S_ISREG(mode)):
            raise UnsafePath(f"{rel}: not a {'folder' if folder else 'regular file'}")
        if not last and not stat.S_ISDIR(mode):
            raise UnsafePath(f"{rel}: {'/'.join(parts[: index + 1])} is not a folder")


def open_below(root: Path, rel: str, flags: int, mode: int = 0o666, make_dirs: bool = False) -> int:
    """Open `rel` below `root` for writing and return the descriptor.

    No step may be a symbolic link and the file must be regular, else UnsafePath. `flags` should
    name the access (O_WRONLY, O_CREAT, O_EXCL, O_APPEND); O_TRUNC is not used, because the file
    is judged before it is cut: use `os.ftruncate` on the result. With `make_dirs`, missing
    folders are created. FileExistsError is raised, unchanged, when O_EXCL meets a file.
    """
    if not SUPPORTED:
        raise UnsafePath("this platform cannot open files without following links, so nothing is written")
    parts = _steps(rel)
    parent = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in parts[:-1]:
            try:
                step = _open_folder(part, parent, make_dirs)
            except OSError as error:
                if isinstance(error, UnsafePath):
                    raise
                if error.errno in (errno.ELOOP, errno.ENOTDIR):
                    raise UnsafePath(f"{rel}: {part} is a symbolic link or not a folder") from error
                raise
            os.close(parent)
            parent = step
        try:
            descriptor = os.open(
                parts[-1], flags | os.O_NOFOLLOW | getattr(os, "O_NONBLOCK", 0), mode, dir_fd=parent
            )
        except FileExistsError:
            raise
        except OSError as error:
            if error.errno in (errno.ELOOP, errno.ENXIO, errno.EMLINK):
                raise UnsafePath(f"{rel}: {parts[-1]} is a symbolic link or not a regular file") from error
            raise
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            os.close(descriptor)
            raise UnsafePath(f"{rel}: not a regular file")
        return descriptor
    finally:
        os.close(parent)


def _open_folder(name: str, parent: int, make_dirs: bool) -> int:
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    try:
        return os.open(name, flags, dir_fd=parent)
    except FileNotFoundError:
        if not make_dirs:
            raise
    try:
        os.mkdir(name, 0o777, dir_fd=parent)
    except FileExistsError:
        pass  # made by someone else a moment ago; open it, still without following a link
    return os.open(name, flags, dir_fd=parent)


def write_text(root: Path, rel: str, text: str, make_dirs: bool = True) -> None:
    """Replace (or create) the file `rel` below `root` with `text`, UTF-8."""
    descriptor = open_below(root, rel, os.O_WRONLY | os.O_CREAT, make_dirs=make_dirs)
    try:
        os.ftruncate(descriptor, 0)
        _write_all(descriptor, text.encode("utf-8"))
    finally:
        os.close(descriptor)


def create_text(root: Path, rel: str, text: str) -> bool:
    """Create the file `rel` below `root` with `text`. True when written; False when a file with
    exactly that text is already there; UnsafePath when a file with other text is. Never replaces."""
    data = text.encode("utf-8")
    try:
        descriptor = open_below(root, rel, os.O_WRONLY | os.O_CREAT | os.O_EXCL, make_dirs=True)
    except FileExistsError:
        pass
    else:
        try:
            _write_all(descriptor, data)
        finally:
            os.close(descriptor)
        return True
    existing = read_bytes(root, rel, len(data) + 1)
    if existing == data:
        return False
    raise UnsafePath(f"{rel}: a file with different content is already there; it is left as it is")


def append_text(root: Path, rel: str, text: str) -> None:
    """Append `text`, UTF-8, to the file `rel` below `root`, creating it and its folders."""
    descriptor = open_below(root, rel, os.O_WRONLY | os.O_CREAT | os.O_APPEND, make_dirs=True)
    try:
        _write_all(descriptor, text.encode("utf-8"))
    finally:
        os.close(descriptor)


def read_bytes(root: Path, rel: str, limit: int) -> bytes:
    """Up to `limit` bytes of the regular file `rel` below `root`, links refused."""
    if not SUPPORTED:
        raise UnsafePath("this platform cannot open files without following links")
    parts = _steps(rel)
    parent = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in parts[:-1]:
            step = _open_folder(part, parent, make_dirs=False)
            os.close(parent)
            parent = step
        descriptor = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | getattr(os, "O_NONBLOCK", 0), dir_fd=parent)
    except OSError as error:
        if error.errno in (errno.ELOOP, errno.ENOTDIR):
            raise UnsafePath(f"{rel}: a symbolic link or not a folder on the way") from error
        raise
    finally:
        os.close(parent)
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise UnsafePath(f"{rel}: not a regular file")
        return os.read(descriptor, limit)
    finally:
        os.close(descriptor)


def _write_all(descriptor: int, data: bytes) -> None:
    view = memoryview(data)
    while view:
        view = view[os.write(descriptor, view):]
