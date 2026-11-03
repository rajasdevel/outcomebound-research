---
last_checked: 2026-10-19
volatility: VOLATILE (flags, output fields and exit codes change between releases; Gemini CLI availability changed on 2026-06-18)
sources:
  - https://github.com/anthropics/claude-code/releases/tag/v2.1.314 (read 2026-10-31)
  - https://github.com/anthropics/claude-code/releases/tag/v2.1.316 (read 2026-10-31)
  - https://code.claude.com/docs/en/cli-reference
  - https://learn.chatgpt.com/docs/non-interactive-mode
  - https://cursor.com/docs/cli/headless
  - https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/headless.md
  - https://geminicli.com/docs/cli/plan-mode/
  - https://opencode.ai/docs/permissions
---

# Non-interactive (print and headless) modes

How five coding harnesses run once, with no person at the terminal: the command, the output, the
flags that limit what the run can do or load, and how a run ends. Every claim is L (the vendor's
documentation) and was read on 2026-10-19. "Silent" means the page read does not say. No harness
was run for this page, so no flag was tested.

## 1. At a glance

| Harness | Non-interactive command | Stdin | Output formats | Read-only or restricted option the docs name |
| --- | --- | --- | --- | --- |
| Claude Code | `claude -p "<prompt>"` | piped content is accepted | `text`, `json`, `stream-json` | `--permission-mode plan`; `--restricted`; `--tools` and `--disallowedTools` |
| Codex | `codex exec "<prompt>"` | `codex exec -` reads the whole prompt from stdin | final message on stdout; `--json` for JSON Lines | `--sandbox`; default is a read-only sandbox |
| Cursor CLI | `cursor-agent -p "<prompt>"` | silent | `text`, `json`, `stream-json` | print mode proposes changes unless `--force` is given |
| Gemini CLI | `gemini -p "<prompt>"` | a non-TTY run is headless; the page does not describe stdin | `text`, `json`, `stream-json` | `--approval-mode plan` |
| OpenCode | `opencode run` | silent | silent on this page | permission keys with `deny` |

## 2. Claude Code

Source: the [CLI reference](https://code.claude.com/docs/en/cli-reference).

- `-p` / `--print` prints the response and exits. `--output-format` takes `text`, `json` or
  `stream-json`; `--input-format` takes `text` or `stream-json`; `--json-schema` returns output
  validated against a schema (print mode only).
- `--bare` skips discovery of hooks, skills, custom commands, subagents, plugins, MCP servers,
  auto memory and `CLAUDE.md`; Bash, file read and file edit stay available. `--safe-mode`
  disables the same customisations but leaves authentication, model choice, built-in tools and
  permissions as normal; managed-settings policy still applies.
- `--restricted` (version 2.1.248 or later) removes the tools that run commands or code, and
  WebFetch, unless `--tools` names them; confines the file tools to the working directories;
  loads only managed settings and `--settings`; refuses `bypassPermissions`; and refuses to create
  cloud sessions. The page describes it for an evaluation harness on a shared machine. The
  confinement had a gap before 2.1.316: a `--restricted` session uploaded files from outside the
  working directories when a Read allow rule covered them (2.1.316 release notes, L)
  [as-of 2026-10-31].
- `--permission-prompts none` (version 2.1.259 or later) denies permission prompts in print mode
  where nobody can answer; the default `host` sends them to the Agent SDK host or to the tool named
  by `--permission-prompt-tool`.
- Limits: `--max-turns` exits with an error at the limit (none by default); `--max-budget-usd` stops
  the run at an estimated spend, which can pass the cap and can differ from the bill.
- `--no-session-persistence` (print mode only) writes no session to disk.
- `claude auth status` exits 0 when signed in and 1 when not.
- **Release changes in 2.1.314 and 2.1.316 [as-of 2026-10-31].** These are release notes (L), not
  a runtime check. Before 2.1.314, `claude -p` exited 0 with no output when startup failed; it now
  prints the error and exits 1, so a script that reads only the exit code missed that failure on
  earlier versions (inference). Before 2.1.314, sandbox protections did not apply to a worktree that
  `claude -p --resume` or `--continue` entered. From 2.1.316, text output says why auto mode stopped
  a turn while a background agent was still running. The CLI reference was not re-read for these
  items.

## 3. Codex

Source: the [non-interactive page](https://learn.chatgpt.com/docs/non-interactive-mode).

- `codex exec` sends progress to stderr and only the final message to stdout. A prompt argument
  with piped stdin treats the piped text as context.
- `--ephemeral` saves no session files; `--ignore-user-config` skips `$CODEX_HOME/config.toml`;
  `--ignore-rules` skips user and project execution-policy `.rules` files.
- `-o <path>` writes the final message to a file and still prints it. `--json` makes stdout a
  JSON Lines stream (event types include `thread.started`, `turn.completed` and `error`).
- The page names the default read-only sandbox and the values `workspace-write` and
  `danger-full-access`; it does not show the short form `-s`.
- Authentication in CI: set `CODEX_API_KEY` for a single invocation. The page warns against a
  job-level variable in workflows that run repository code; ChatGPT-managed authentication is
  offered for trusted runners.

## 4. Cursor CLI

Source: the [headless page](https://cursor.com/docs/cli/headless).

- `-p` / `--print` runs non-interactively. The page says print mode alone proposes changes;
  `--force` (or `--yolo`) applies them without confirmation. It does not describe shell access.
- `--output-format` takes `text` (default; final answer only), `json` and `stream-json`;
  `--stream-partial-output` adds incremental deltas. The examples read the answer from `.result`;
  they give no full schema, no failure behaviour for `json`, no exit codes and no stdin.

## 5. Gemini CLI

Sources: the [headless page](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/headless.md)
and the [plan-mode page](https://geminicli.com/docs/cli/plan-mode/).

- Headless mode starts in a non-TTY environment or when a query is given with `-p` /
  `--prompt`. `--output-format json` returns one object with `response`, `stats` (token usage and
  API latency) and an optional `error`; `stream-json` returns JSON Lines with the event types
  `init`, `message`, `tool_use`, `tool_result`, `error` and `result`.
- Exit codes: `0` success; `1` general error or API failure; `42` input error (invalid prompt or
  arguments); `53` turn limit exceeded.
- `--approval-mode plan` is the documented read-only mode. Plan mode allows file reads, search,
  web search, `web_fetch` (with confirmation), two research subagents, read-only MCP tools, and
  writes only to `.md` files in the plans folder. In scripts and CI the policy engine approves the
  `enter_plan_mode` and `exit_plan_mode` tools without a prompt, and when a plan is executed the
  CLI switches to YOLO mode, so plan mode is not a boundary for a whole headless run.
  (Prompt-denial in headless runs is in [gemini-cli.md §7.1](gemini-cli.md#71-policy-files-and-headless-planning-as-of-2026-10-09).)
- **Availability.** The plan-mode page says Gemini CLI was replaced by Antigravity CLI on
  2026-06-18 for unpaid-tier and Google One users, and that it is not optimised for the newest
  Gemini model.

## 6. OpenCode

Source: the [permissions page](https://opencode.ai/docs/permissions).

- Permission keys: `read`, `edit` (covers edit, write and patch), `glob`, `grep`, `bash`, `task`,
  `skill`, `lsp`, `question`, `webfetch`, `websearch`, `external_directory`, `doom_loop`. Each takes
  `allow`, `ask` or `deny`. When several patterns match, the last one wins, so a catch-all goes
  first.
- Most keys default to `allow`; `doom_loop` and `external_directory` default to `ask`; `.env`
  files are denied for `read`, except `*.env.example`.
- `--auto` approves what would otherwise ask; explicit denies still apply.
- Silent on this page: what `ask` does in a non-interactive run beyond `--auto`, and whether the
  keys cover MCP tools.

## Limits

- Pages were read through a fetch tool that summarises. Re-read the source before relying on a
  flag or code.
- Not read, so not recorded: how the Cursor CLI treats shell, MCP and web fetch in its `ask` and
  `plan` modes, OpenCode's flags and output format, and every harness's error text.

Sources for sections dated 2026-10-31 (L, vendor release notes; runtime behavior not tested):

- <https://github.com/anthropics/claude-code/releases/tag/v2.1.314> (published 2026-10-30), read
  2026-10-31.
- <https://github.com/anthropics/claude-code/releases/tag/v2.1.316> (published 2026-10-31), read
  2026-10-31.
