---
last_checked: 2026-09-25
volatility: VOLATILE (Pi's documentation lives on its main branch and changes without versioned releases of the pages)
sources:
  - https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/configuration.md
  - https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/settings.md
  - https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/extensions.md
  - https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/usage.md
  - https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/how-pi-works.md
  - https://earendil.com/posts/pi-1-0/
  - https://earendil.com/posts/pi-durable/
  - https://github.com/earendil-works/pi/releases/tag/v1.1.0
  - https://github.com/earendil-works/pi/releases/tag/v1.2.0 (read 2026-10-31)
  - https://github.com/earendil-works/pi/releases/tag/v1.3.0 (read 2026-10-31)
  - https://github.com/earendil-works/pi/releases/tag/v1.4.0 (read 2026-10-31)
  - https://earendil.com/posts/pi-durable-on-cloudflare/ (read 2026-10-31)
  - https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/security.md (read 2026-11-03)
  - https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/skills.md (read 2026-11-03)
  - https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/sessions.md (read 2026-11-03)
  - https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/compaction.md (read 2026-11-03)
  - https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/cli.md (read 2026-11-03)
  - https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/mcp.md (read 2026-11-03)
  - https://github.com/earendil-works/pi/releases/tag/v1.5.0 (read 2026-11-03)
  - https://raw.githubusercontent.com/earendil-works/pi/6fb2e7815167e6b19006fc526d1a5d0f5f998787/packages/durable/README.md
---

# Pi

Re-check when Pi changes which context files it reads, what project trust gates, its extension
events or its settings keys; before relying on a field name; and by 2026-12-27.

What Pi loads and what waits for project trust, its skills, its finish event (an extension event,
not a command hook), the settings that run code, and where it keeps sessions. For anyone placing
text, skills or an extension where Pi will load them, opening an untrusted checkout in Pi. The comparison with other harnesses, the key
findings (H1–H12) and the evidence classes are in [cross-harness.md](cross-harness.md).

Sections 1–6 were checked against the current vendor documentation on 2026-11-03. L means
vendor documentation; no installed version or runtime behavior was tested. The whole-document
`last_checked` remains unchanged because the cross-harness claims in section 8 were not checked.

## 1. Instruction files and precedence

[as-of 2026-11-03]

- **Context files.** Pi loads `AGENTS.override.md`, `AGENTS.md`, `AGENTS.MD`, `CLAUDE.md` or
  `CLAUDE.MD` from the agent directory (`~/.pi/agent` by default), working directory and its
  parents. An override replaces the ordinary context file only in its own directory.
- **System prompts.** `SYSTEM.md` replaces the default and `APPEND_SYSTEM.md` adds to it. A
  trusted project's `.pi/` file takes precedence over the agent-directory file of the same name;
  Pi does not combine them.
- Context loading does not require project trust, and can be disabled. Do not assume it follows
  project-resource loading: Pi may load context files before trust is resolved.

L, [configuration](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/configuration.md)
and [security](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/security.md),
read 2026-11-03.

## 2. Caps and skills

[as-of 2026-11-03]

- No enforced cap was found in the sources read; this is not proof that no cap exists.
- Pi advertises skill names, descriptions and paths, then the model reads the full instructions
  when needed. Locations include `<agent-dir>/skills/`, `.pi/skills/`, `~/.agents/skills/` and
  project `.agents/skills/` in the working directory and its ancestors up to the repository root.
  Project skills require trust. Settings and packages can add locations.

L, [skills](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/skills.md)
and [security](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/security.md),
read 2026-11-03.

## 3. Trust

[as-of 2026-11-03]

- Trust gates `.pi/settings.json`, `.pi/mcp.json`, project extensions, skills, prompts, themes,
  system-prompt files, project packages and project `.agents/skills`. Pi reads `sessionDir` before
  the decision. Context files can still load when trust is declined.
- A CLI `--approve` or `--no-approve` overrides trust for one process. Otherwise an eligible
  user or CLI extension can decide first, followed by the nearest saved decision and the global
  `defaultProjectTrust` setting, which defaults to `ask`.
- Print, JSON and RPC modes cannot show the built-in trust prompt. Without an override, extension
  decision or saved decision, `always` loads protected resources; `ask` and `never` skip them.
- Trust controls loading, not tool permissions or isolation. Pi does not ask before every tool
  call; tools, extensions, installers and child processes have the Pi process's OS permissions
  unless an external boundary restricts them.

L, [security](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/security.md)
and [CLI](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/cli.md),
read 2026-11-03.

## 4. Hooks: extensions

[as-of 2026-11-03]

L, [extensions](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/extensions.md),
read 2026-11-03. Marks are as in [cross-harness.md](cross-harness.md#1-scope-method-and-evidence).

| Finish event | Holds the finish and returns a reason | Loop guard | Time limit | Project configuration |
| --- | --- | --- | --- | --- |
| `agent_before_settle` (doc) | `continue: true` requests another model call (doc) | extension condition (doc) | none found (`UNVERIFIED`) | TypeScript under `.pi/extensions/`, after project trust (doc) |

`agent_end` marks the end of a low-level run; retries, compaction or queued messages can follow.
`agent_before_settle` is the last actionable boundary and can request one continuation;
`agent_settled` is notification-only. An unconditional continuation can loop. Extensions also
load from the user directory, packages or an explicit CLI path. User and CLI extensions can
participate in `project_trust` before project extensions load. Extensions run inside Pi with its
OS permissions. See [cross-harness.md](cross-harness.md#92-what-makes-a-hook-unsafe-or-unusable).

## 5. Settings that run code or widen permissions

[as-of 2026-11-03]

Project settings and MCP configuration require trust. `extensions` and `packages` load code;
`shellPath`, `shellCommandPrefix` and `npmCommand` affect commands Pi runs. An MCP server's
`command` starts a local server; its `url` selects a network endpoint. `httpProxy` configures a
proxy. This is not a complete list of code paths or permission controls. L,
[settings](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/settings.md),
[MCP](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/mcp.md)
and [security](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/security.md),
read 2026-11-03.

## 6. Sessions and compaction

[as-of 2026-11-03]

- Pi saves sessions unless `--no-session` is set. Entries form a tree; the active branch supplies
  context. `/tree` moves within a session, while `/fork` and `/clone` create separate sessions.
- Compaction summarizes older context and keeps recent messages for subsequent requests; the
  original entries remain in the session tree. `/compact` can accept summary instructions.
- `pi --continue` opens the most recent session for the current directory. A resumed session can
  use its original working directory, which can differ from the current directory. `/session`
  reports the session file and usage. Shared sessions can expose prompts, tool output, file
  contents or credentials.

L, [sessions](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/sessions.md),
[compaction](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/compaction.md)
and [security](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/security.md),
read 2026-11-03.

## 7. Pi 1.0 and Pi Durable (VOLATILE) [as-of 2026-10-09]

Earendil's 2026-10-01 release introduced Pi Durable as a separate experimental framework;
it does not replace the terminal coding agent. The release observed on 2026-10-09 was
[v1.1.0](https://github.com/earendil-works/pi/releases/tag/v1.1.0), published 2026-10-07.
That release reports a fix for standalone binaries loading launch-directory `.env` files (L;
release notes, read 2026-10-09; runtime behaviour UNVERIFIED).

The [Durable README](https://raw.githubusercontent.com/earendil-works/pi/6fb2e7815167e6b19006fc526d1a5d0f5f998787/packages/durable/README.md)
at commit `6fb2e7815167e6b19006fc526d1a5d0f5f998787`, read 2026-10-09 (L), documents:

- Checkpoints and persisted tool intent. An interrupted tool runs again only when declared
  `replay: "safe"`; otherwise its stored output accompanies an interruption result.
- A repeated submission's `requestId` finds the existing submission. This does not establish
  that an external write happened once (inference).
- Ordinary conversation abort stops current work but leaves background-owned work alive.
  Stopping it requires an explicit task abort or the conversation's `{ background: true }`
  abort option.

The API can change between releases. The launch guide permits only one process to own a storage
backend at a time. These are documented mechanisms, not a tested production recovery guarantee.
For the general rule about external effects, see [agent-workspace.md](../practices/agent-workspace.md).

## 8. Elsewhere

- On DeepSWE v1.1, DeepSeek-V4.1-Flash scored 66.2 in Pi, against 74.2 in mini-SWE and 69.8 in
  Claude Code ([cross-harness.md](cross-harness.md#132-the-documented-direction)).
- MiniMax Code is built on a harness "based on … OpenCode and Pi"; GLM reaches coding agents through
  Pi among others ([others.md](others.md#opencode), [others.md](others.md#zcode-zai)).
- Whether a reply's Mermaid block is drawn is unknown [as-of 2026-09-23].

## 9. Release changes in 1.2.0, 1.3.0 and 1.4.0 [as-of 2026-10-31]

These notes describe the published releases of 2026-10-12 (1.2.0), 2026-10-15 (1.3.0) and
2026-10-21 (1.4.0), not a runtime check. L, release notes read 2026-10-31.

- **Context files (1.2.0).** A symlinked `AGENTS.md` in a git worktree that is nested inside its
  main repository caused no project context file to load. The release says this is fixed.
- **Skill and extension paths (1.2.0).** Pi did not expand `~` in `!pattern`, `+path` and `-path`
  entries of the `extensions`, `skills`, `prompts` and `themes` settings, so an entry such as
  `!~/skills/pdf` matched nothing. The release says this is fixed.
- **Extension events (1.2.0, breaking).** `before_agent_start` now also fires for a run that an
  extension starts with `pi.sendMessage(..., { triggerTurn: true })` while Pi is idle. The event is now a union on
  `messageType`, so a handler that must act only on user prompts must check
  `event.messageType === "user"`. Such runs also no longer lose the system-prompt sections that
  `before_agent_start` added after their first tool call.
- **Non-interactive mode (1.2.0).** When the final response is cut off at the output token limit,
  print mode (`-p`) now prints the partial text, writes a warning to stderr and exits 1. Before,
  it exited 0 with no warning.
- **Compaction (1.2.0, 1.4.0).** Compaction and branch summaries no longer include thinking blocks
  (1.2.0). Summaries now use the model's output limit instead of a fixed cap, so long reasoning no
  longer makes them fail, and `compaction.reserveTokens` now controls only when compaction starts
  (1.4.0). `/compact <instructions>` no longer ignores the instructions when compaction splits a
  turn (1.4.0).
- **Sessions (1.3.0, 1.4.0).** A resumed session keeps its active tools, and `--tools +name` or
  `-name` applies on top of them (1.3.0). After a resume or `/tree` navigation, extension tools
  are active unless they are registered with `defaultActive: false` (1.4.0). A session no longer
  breaks after recovery from a response cut off at the output limit (1.4.0). The new
  `sessionShareDestination` setting selects `auto`, `gist` or `radius` as the target of `/share`
  (1.3.0); the warning in §6 about what a shared session can hold still applies.
- **Subagents (1.4.0).** Parallel codemode scripts and in-process subagents now wait up to 60
  seconds for a free worker instead of failing. `PI_CODEMODE_MAX_WORKERS` raises the limit of two
  workers.
- **Tool calls (1.3.0, 1.4.0).** A tool call whose final arguments are malformed JSON now fails
  validation and shows the model what it sent; before, it ran with only the fields parsed before the
  error (1.3.0). The `grep` tool now runs `rg --no-config`, so `RIPGREP_CONFIG_PATH` options no
  longer change its searches (1.4.0).
- **MCP (1.2.0, 1.4.0).** MCP OAuth sign-in now fails with an issuer mismatch when it cannot check
  an `iss` parameter, and a call cancelled during an OAuth refresh is no longer sent after the
  refresh (1.2.0). An `mcp.json` that starts with a UTF-8 BOM no longer fails to parse and skip all
  its servers (1.4.0).
- **Model catalog.** With an OpenRouter key, Pi lists only the models that key may use (1.2.0).
  When several providers offer a `--model` match, Pi now prefers the provider with credentials and
  otherwise reports the ambiguity (1.3.0). On a model switch, Pi drops thinking blocks from the
  previous model instead of sending them as plain text (1.3.0). The default Xiaomi model is now
  `mimo-v2.6-pro`, because `mimo-v2.5-pro` left the catalog, and the default GitHub Copilot model is
  now `gpt-6.1-sol` (1.4.0).

Release notes do not establish the installed version or the behavior on a given machine.

## 10. Pi Durable on Cloudflare [as-of 2026-10-31]

Earendil's post of 2026-10-16 builds an example chat agent on Pi Durable and Cloudflare Durable
Objects. L, <https://earendil.com/posts/pi-durable-on-cloudflare/>, read 2026-10-31; nothing was
tested here. What it shows about sessions and subagents:

- One Pi Durable harness serves one session, and the example maps each session to one Durable
  Object with SQLite storage. Pi Durable ships memory, JSONL and SQLite storage, accepts another
  storage backend, and has a conformance suite to test one.
- A session can hold several conversations and forks. The example stores a receipt with the request
  id in the same commit that creates a conversation, so a repeated request does not create a
  duplicate. Messages that arrive while the model or a tool runs wait in a durable inbox and are
  answered in order.
- Cloudflare alarms run at least once, so the post makes the alarm handler idempotent. It rebuilds
  the alarm from the stored tasks each time the object wakes.
- A subagent is an ordinary conversation that the tool task owns. The example marks its tool
  replay-safe, so Pi runs it again after an eviction instead of reporting it as interrupted.

This is a worked example. It does not establish that an external effect happens once (see §7).

## 11. Release 1.5.0 [as-of 2026-11-03]

The [1.5.0 release notes](https://github.com/earendil-works/pi/releases/tag/v1.5.0),
read 2026-11-03, identify it as the latest release, published 2026-11-02. L; runtime behavior is
UNVERIFIED. The release reports:

- A fix for a saved refusal of project trust being ignored when no trust-gated resource was
  present. This did not change the separate rule that context files can load without trust.
- A new tool-argument validator. Plain JSON Schema and MCP tools now receive the same coercion as
  TypeBox tools; TypeBox features outside JSON Schema no longer apply to tool arguments.
- A `pi.exec()` output buffer limit and a `truncated` result field. A fix for SDK compaction,
  branch and bug-report summaries passing stored OAuth tokens as explicit API keys.

The release notes do not establish which version is installed or how a particular run behaves.

## Sources

- Configuration
  <https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/configuration.md>
  [chk-pi] (2026-09-25, 2026-10-01); settings
  <https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/settings.md>
  (2026-09-27, 2026-10-01); extensions
  <https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/extensions.md>
  (2026-09-29); usage, how Pi works and MCP pages under the same `docs/` path (2026-10-01).

- Earendil, Pi 1.0 and Pi Durable (both published 2026-10-01),
  <https://earendil.com/posts/pi-1-0/> and <https://earendil.com/posts/pi-durable/>;
  v1.1.0 release notes (2026-10-07),
  <https://github.com/earendil-works/pi/releases/tag/v1.1.0>; pinned Durable README above.
  All read 2026-10-09 for §7.

Checks defined here (verdict PASS, read 2026-09-25):
- [chk-pi] <https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/configuration.md>, read 2026-09-25.

Evidence ids in brackets resolve in [`../_evidence/2026-09-25.jsonl`](../_evidence/2026-09-25.jsonl).

Sources for sections dated 2026-10-31 (L, vendor release notes and post; runtime behavior not tested):

- <https://github.com/earendil-works/pi/releases/tag/v1.2.0>, read 2026-10-31 (§9).
- <https://github.com/earendil-works/pi/releases/tag/v1.3.0>, read 2026-10-31 (§9).
- <https://github.com/earendil-works/pi/releases/tag/v1.4.0>, read 2026-10-31 (§9).
- <https://earendil.com/posts/pi-durable-on-cloudflare/>, read 2026-10-31 (§10).
