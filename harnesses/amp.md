---
last_checked: 2026-09-25
volatility: VOLATILE (Amp changes its loading, skills and plugin API between releases; several of its pages carry no version)
sources:
  - https://ampcode.com/docs/customize/agents-md (read 2026-11-03)
  - https://ampcode.com/docs/customize/skills (read 2026-11-03)
  - https://ampcode.com/docs/customize/plugins (read 2026-11-03)
  - https://ampcode.com/docs/customize/mcp (read 2026-11-03)
  - https://ampcode.com/docs/plugin-api (read 2026-11-03)
  - https://ampcode.com/docs/tools (read 2026-11-03)
  - https://ampcode.com/docs/cli/execute-mode (read 2026-11-03)
  - https://ampcode.com/docs/cli/settings (read 2026-11-03)
  - https://ampcode.com/docs/threads (read 2026-11-03)
  - https://ampcode.com/news/neo (read 2026-11-03)
---

# Amp

This reference covers instruction and skill loading, plugins, trust, permissions, sessions and
noninteractive runs. The comparison with other harnesses is in [cross-harness.md](cross-harness.md).
Sections 1–7 were checked against vendor documentation on 2026-11-03. L means vendor guidance;
no installed version or runtime behavior was tested. The whole-document `last_checked` remains
unchanged: the cross-harness claims were not verified.

## 1. Instruction files and precedence

[as-of 2026-11-03]

- Amp loads `AGENTS.md` from the current directory or editor workspace roots and parents up to
  `$HOME`. It includes subtree files when it reads a file in that subtree. If a directory has no
  `AGENTS.md`, it includes `AGENT.md` or `CLAUDE.md`; the documentation does not settle the
  order when both fallback names exist.
- Amp also loads `~/.config/amp/AGENTS.md`, `~/.config/AGENTS.md` and platform-specific
  system-wide files when present. Hosted workspace guidance precedes personal and repository
  guidance, but does not apply to subagents, Puck or raw custom agents.
- `@` mentions include other files; frontmatter `globs` on a mentioned file limits it to matching
  files that Amp has read. `AMP_IGNORE_GUIDANCE_FILES` can exclude guidance paths; this does not
  prevent an explicit tool read of those files.

L, [AGENTS.md](https://ampcode.com/docs/customize/agents-md), read 2026-11-03.

## 2. Caps

[as-of 2026-11-03]

No general instruction-file cap was found in the sources read; this does not prove none exists.
Hosted skill repositories have limits, as the skills documentation states. L,
[skills](https://ampcode.com/docs/customize/skills), read 2026-11-03.

## 3. Skills

[as-of 2026-11-03]

Amp uses the first skill of a given name in this order: `~/.config/agents/skills`,
`~/.agents/skills`, `~/.config/amp/skills`, `.agents/skills` and `.claude/skills` in the
project and searched parents, `~/.claude/skills`, Claude plugin cache, configured
`amp.skills.path`, personal and workspace skill repositories, and official Amp skills. Settings
can disable the Claude-compatible or global Agent Skills locations. An active plugin can register
a separately qualified skill.

Amp advertises the name and description, then loads the body when invoked. A skill can define an
MCP server: Amp connects when it discovers the skill, although tools from a server defined only
by that skill stay hidden until the skill loads. `amp skills list` inspects skills; a separate
shell listing does not reload an existing session. L,
[skills](https://ampcode.com/docs/customize/skills), read 2026-11-03.

## 4. Hooks: the plugin API

[as-of 2026-11-03]

L, [plugin API](https://ampcode.com/docs/plugin-api) and
[plugins](https://ampcode.com/docs/customize/plugins), read 2026-11-03. Marks are as in
[cross-harness.md](cross-harness.md#1-scope-method-and-evidence).

| Finish event | Holds the finish and returns a reason | Loop guard | Time limit | Project configuration |
| --- | --- | --- | --- | --- |
| `agent.end` (doc) | `action: 'continue'` and `userMessage` start a new turn (doc) | `maxContinuations`, default 5 (doc) | handler limit not found (`UNVERIFIED`) | JavaScript or TypeScript in `.amp/plugins/`, run by Bun (doc); project-plugin trust gate not established (`UNVERIFIED`) |

`agent.end` reports `done`, `error` or `cancelled` and the turn's messages. A user message resets
the continuation count. Plugins can run code and load from project, system, personal and
workspace scopes; same-name precedence is project, system, personal, then workspace. Plugin code
runs at load. The docs say to load only trusted plugins; they do not establish a project-plugin
approval prompt.

A plugin can call tools directly. The documented normal permission and confirmation policy
applies, but default tool policy asks for no approval (section 5). Direct tool calls have a
five-minute deadline, do not enter the transcript and are not automatically retried after a lost
connection; the write outcome can be unknown. A plugin agent's default ten-minute wait timeout
rejects the wait and leaves the child running until its turn ends. These are separate time limits,
not proof of an `agent.end` handler deadline. L,
[plugins](https://ampcode.com/docs/customize/plugins) and
[plugin API](https://ampcode.com/docs/plugin-api), read 2026-11-03.

## 5. Settings that run code or widen permissions

[as-of 2026-11-03]

- Amp documents no tool approval prompt by default. Its release post says existing configurations
  that opt into permissions through `amp.permissions`, `amp.dangerouslyAllowAll: false` or
  `amp.guardedFiles.allowlist` load the old permissions plugin, including in execute mode. A
  custom plugin can also control tool use. This is not a sandbox guarantee.
- `amp.mcpServers` can define a local process with `command`, `args` and `env`, or a network
  endpoint with `url` and `headers`. Servers in `.amp/settings.json` require explicit approval;
  global or CLI-supplied servers do not require that workspace-server approval. Skill-defined
  servers have the discovery behavior in section 3. The MCP approval rule does not establish a
  general project-settings or project-plugin trust gate.
- The nearest workspace `.amp/settings.json` or `.jsonc` normally overrides user settings;
  managed settings have separate precedence. `amp.mcpPermissions` allows or rejects servers by
  command, arguments or URL; the first matching rule applies and unmatched servers are allowed.
  `amp.tools.disable` disables named or matching tools. This list is not exhaustive.

L, [tools](https://ampcode.com/docs/tools), [release post](https://ampcode.com/news/neo),
[MCP](https://ampcode.com/docs/customize/mcp),
[settings](https://ampcode.com/docs/cli/settings) and [skills](https://ampcode.com/docs/customize/skills), read 2026-11-03.

## 6. Trust, compaction and sessions

[as-of 2026-11-03]

A thread holds prompts, replies, tool calls and changed files, and can be accessed across Amp
clients. The vendor's 2026-05-06 release post says the rebuilt CLI summarizes the thread and
continues in a fresh context window when context is 90% full. This is a dated vendor statement,
not a measurement of current thresholds or summary completeness. L,
[threads](https://ampcode.com/docs/threads) and [release post](https://ampcode.com/news/neo),
read 2026-11-03.

`amp -x` sends a prompt, waits for the turn, prints the final message and exits. Noninteractive
thread creation defaults to Standard mode; `--fast` selects Fast for one invocation. If lifecycle
plugins must be ready before the turn, `--plugin-ready-timeout` waits for them: the bare flag
allows 10 seconds, a numeric argument sets a limit up to 300, and zero disables the wait. Without
that wait, the turn can start before plugin loading finishes and lifecycle events can be skipped.
L, [execute mode](https://ampcode.com/docs/cli/execute-mode), read 2026-11-03.

## 7. Observing what loaded, and rendering

[as-of 2026-11-03]

`amp skills list` and `amp plugins list` show discovered skills and loaded plugins respectively.
A command to list loaded instruction files was not found in the sources read. Whether a reply's
Mermaid block is drawn remains UNVERIFIED. L,
[skills](https://ampcode.com/docs/customize/skills) and
[plugins](https://ampcode.com/docs/customize/plugins), read 2026-11-03.
