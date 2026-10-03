---
last_checked: 2026-10-03
volatility: VOLATILE (most of these layers are experimental, in preview or a new major; event names and UI APIs change between releases)
sources:
  - https://agent-plugins.org
  - https://agent-plugins.org/compatible-clients
  - https://agent-plugins.org/plugin-authors/client-extensions
  - https://agentclientprotocol.com/get-started/agents
  - https://agentclientprotocol.com/get-started/clients
  - https://agentclientprotocol.com/protocol/v1/extensibility
  - https://agentclientprotocol.com/protocol/v2/migration
  - https://agentclientprotocol.com/protocol/v2/overview
  - https://agentclientprotocol.com/rfds/proxy-chains
  - https://agentclientprotocol.com/rfds/updates
  - https://ampcode.com/docs/customize/plugins
  - https://ampcode.com/docs/plugin-api
  - https://code.claude.com/docs/en/agent-sdk/hooks
  - https://code.claude.com/docs/en/agent-sdk/overview
  - https://code.claude.com/docs/en/agent-sdk/permissions
  - https://code.claude.com/docs/en/plugins/mods/api
  - https://code.claude.com/docs/en/plugins/mods/overview
  - https://code.claude.com/docs/en/plugins/mods/reference
  - https://code.claude.com/docs/en/statusline
  - https://code.visualstudio.com/api/extension-guides/ai/ai-extensibility-overview
  - https://code.visualstudio.com/docs/copilot/customization/hooks
  - https://cursor.com/docs/agent/tools/canvas
  - https://cursor.com/docs/cli/acp
  - https://cursor.com/docs/cli/reference/configuration
  - https://cursor.com/docs/hooks
  - https://cursor.com/docs/plugins
  - https://developers.openai.com/codex/app-server
  - https://developers.openai.com/codex/config-advanced
  - https://developers.openai.com/codex/config-reference
  - https://developers.openai.com/codex/hooks
  - https://developers.openai.com/codex/plugins
  - https://developers.openai.com/codex/sdk
  - https://docs.cline.bot/customization/hooks
  - https://docs.cline.bot/customization/plugins
  - https://docs.cline.bot/llms.txt
  - https://docs.cline.bot/sdk/guides/writing-plugins
  - https://docs.cline.bot/sdk/plugins
  - https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-extensions
  - https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/hooks
  - https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference
  - https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference
  - https://docs.github.com/en/copilot/reference/hooks-configuration
  - https://docs.github.com/en/copilot/tutorials/create-an-extension
  - https://github.com/modelcontextprotocol/experimental-ext-interceptors
  - https://github.com/modelcontextprotocol/ext-apps
  - https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx
  - https://kilo.ai/docs/automate/extending/plugins
  - https://mcpui.dev/
  - https://modelcontextprotocol.io/extensions/apps/overview
  - https://modelcontextprotocol.io/extensions/client-matrix
  - https://opencode.ai/docs/plugins/
  - https://opencode.ai/docs/sdk/
  - https://opencode.ai/docs/server/
  - https://opencode.ai/v2/docs/build/plugins
  - https://opencode.ai/v2/docs/build/plugins/cli
  - https://opencode.ai/v2/docs/build/plugins/rpc
  - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/plugin/src/index.ts
  - https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/plugin/src/tui.ts
  - https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/extensions.md
  - https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/rpc-extension-ui.md
  - https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/tui.md
  - https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/extensions/index.md
  - https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/hooks/reference.md
  - https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/reference/configuration.md
---

# Harness extension layers compared: hooks, plugins, UI and protocols

Re-check when a harness in the table ships or changes an extension, plugin or hook API, when ACP v2
or an ACP proxy design leaves draft, when MCP Apps gains a terminal host, and by 2026-11-02.

What third-party code can run inside or beside each coding harness, which lifecycle events it can
observe, intercept or rewrite, what interface it can draw and on which surface, how it keeps state,
who must consent, and how stable each layer is; and the harness-neutral protocols (ACP, MCP Apps,
Agent Plugins, the embedding SDKs) that carry state or interface between an agent and a client. For
anyone who plans behaviour or interface that should work in more than one harness. Claude Code mods
are in depth in [claude-code-mods.md](claude-code-mods.md); loading, caps, trust and finish hooks
per harness are in [cross-harness.md](cross-harness.md) and each harness's own file.

All pages were read on 2026-10-03, as raw text where the site allowed it, and the generated type
files of Pi, Amp and OpenCode were read. No harness was run. Evidence classes are as in
[CONVENTIONS.md](../CONVENTIONS.md): L is a vendor's or maintainer's documentation (published type
declarations included), M is measured here (registry metadata, HTTP status, counts), A is one
account. "Inference:" marks a conclusion of this document, not a statement of a source. `?` in a
table means that the reading did not settle it; it never means "no".

## 1. Comparison table

| Layer | Code runs where, language | Lifecycle it can observe / intercept / rewrite | UI it can draw, on which surfaces | State, timers | Trust / consent | Stability |
| --- | --- | --- | --- | --- | --- | --- |
| **Claude Code mods** | In process, JS/TS ES module in its own runtime (no DOM, no Node), all effects via `$` | Tool call (deny, rewrite, answer), permission verdict, prompt submit (rewrite, drop), system-prompt sections, first-message context, turn steps (model, effort), turn end, session start/end, compaction (rewrite, answer, skip), transcript rows, other mods | Pane, band above prompt, toast, line under prompt, dialogs (`$.ui.ask`), restyle or replace built-in rows and spinner; terminal and Desktop Code tab only; hooks run but draw nothing in VS Code panel, `-p`, Agent SDK, cloud | Module vars, `$.state` (session), `$.store` (machine, 4 MiB); `$.clock.every/after` | Installed as plugin; not sandboxed; `claude plugin validate` lists hooks and calls; managed allow-lists | Shipped 2.1.287 on 2026-10-01, on `latest` not `stable` tag (per claude-code-mods.md) |
| **Claude Code settings hooks + `statusLine`** | Subprocess command (also http, mcp_tool, prompt, agent handlers); any language | 33 events (per claude-code.md): PreToolUse deny/rewrite, UserPromptSubmit context, Stop continue, Session*, Pre/PostCompact | Status line: command's stdout lines, multi-line, OSC 8 links, `refreshInterval`, 300 ms debounce; hook text to transcript | Files only; status line re-run on events or timer | Workspace trust for settings files; `-p`/SDK treat folder as trusted (claude-code.md) | Stable |
| **Pi extensions** | In process, TS/JS via jiti, same OS permissions | `tool_call` (mutate, block), `tool_result` (modify), `before_agent_start` (prompt, tools, whole system prompt), `context`, `context_with_system`, `message_end` (replace), `turn_end`/`agent_before_settle` (continue), `user_bash`, session start/shutdown | `notify`, `confirm/select/input/editor`, `setStatus`, `setWidget`, `setTitle`, header/footer/editor replacement, `custom()` overlays, tool and message renderers; TUI full; RPC mode forwards dialogs, notify, status, string widgets; JSON/print none | `appendEntry`, tool-result `details`, branch-aware rebuild; timers allowed from `session_start`, not the factory | Project extensions load after project trust (pi.md); no per-extension consent | No stability label; reload invalidates state |
| **Amp plugins** | Long-lived Bun process per plugin, TS/JS, may serve many threads | `tool.call` (allow, reject, modify, synthesize), `tool.result` (replace), `agent.start` (append hidden or shown text to user message), `agent.end` (continue, cap 5), `changes.prompt`, `session.start` | `notify`, `input`, `select`, `confirm` (editable fields), command palette, transcript link patterns, agent modes; mirrored across TUI and Web; status item CLI-only and `experimental` | `amp.configuration` (observable), own process memory; `setInterval` used in docs; `onDispose` ~3 s | "only load plugins you trust"; no consent gate documented | Core API un-labelled; `amp.experimental` namespace unstable |
| **OpenCode 1.x plugins (server + TUI)** | In process (Bun), TS/JS; server plugin and separate TUI plugin module | `tool.execute.before/after`, `chat.message`, `chat.params`, `chat.headers`, `permission.ask`, `command.execute.before`, `shell.env`, `tool.definition`, `event` bus (`session.idle`, `session.compacted`, …), experimental: `chat.system.transform`, `chat.messages.transform`, `session.compacting`, `compaction.autocontinue` | Server plugin: `client.tui.showToast`, `appendPrompt` over HTTP; TUI plugin: slots (home/session prompt, `home_footer`, sidebar title/content/footer), dialogs, toast, routes, keymap | TUI `kv`; process memory | Auto-load from `.opencode/plugins/`; no trust gate documented | `experimental.*` hooks labelled |
| **OpenCode 2.x plugins + CLI plugins** | In process; plugin context is a server client; separate CLI (TUI) plugin; RPC plugins | `session.hook`: `prompt` (rewrite admitted input), `context` (system, tools, options per model call), `compaction` (supply result), `generate`, `title`, `model.request`, `http.*`, `retry`; `tool.hook execute.before/after`; `permission.hook evaluate`; `shell.hook` | Slots `app`, `home.footer(.status)`, `prompt.footer(.status/.file)`, `session.composer.top`, `sidebar.*`, `session.panel`; dialogs, toasts, routes, tabs, keymap, attention (system notification, sound) | `ctx.storage`; CLI `storage.store` (durable, synced across TUI instances), `storage.memory` | No trust gate documented | New major (first npm 2026-09-02); WebSocket hooks experimental |
| **Kilo plugins** | OpenCode 1.x plugin API (`@kilocode/plugin`), Bun | As OpenCode 1.x | As OpenCode 1.x; CLI and VS Code extension | As OpenCode 1.x | Auto-load `.kilo/plugin/` | ? |
| **Codex hooks, status line, notify** | Subprocess command or `mcp_tool`; any language | 12 events: PreToolUse (block, `updatedInput`), PermissionRequest, PostToolUse (feedback), UserPromptSubmit (block, context), Stop/SubagentStop (continue), Pre/PostCompact, Session/Subagent start, SessionEnd, Interrupt | `systemMessage` warning, `statusMessage` while hook runs; status line = ordered built-in item IDs only; `notify` runs a program on `agent-turn-complete`; TUI OSC 9/BEL notifications | Files; async hooks | Per-hook review by hash, `/hooks`; project layer needs trust | `features.hooks` on by default (codex.md); no stability label read |
| **Codex app-server / SDK** | Separate process, JSON-RPC over stdio (WebSocket experimental); client in any language | Client drives threads and turns; receives item, plan, diff, hook started/completed notifications; answers approval, user-input and MCP elicitation requests | Client draws everything (VS Code extension, desktop app use it) | Server-side threads | Client is the embedding product | Stable surface plus opt-in `experimentalApi`; Python SDK stable |
| **Gemini CLI hooks + extensions** | Subprocess command only; any language. Extensions are packages, not code hosts | BeforeTool (block, merge input), AfterTool (context), BeforeAgent (context), AfterAgent (retry), BeforeModel (override request, synthetic response), BeforeToolSelection, AfterModel (replace chunk), SessionStart/End, Notification, PreCompress | `systemMessage` text; extension themes; footer = built-in item IDs | Files | Project hooks fingerprinted (gemini-cli.md); extension install asks consent | Weekly releases; no label read |
| **Cursor hooks + plugins + canvases** | Subprocess command or `prompt` (LLM) hook | preToolUse (allow/deny, `updated_input`), postToolUse (MCP output, context), beforeShell/MCP/ReadFile, afterFileEdit, beforeSubmitPrompt (block only), sessionStart (context, fire-and-forget), stop (follow-up), preCompact (observe), Tab hooks, `workspaceOpen` | `user_message` text; canvases are agent-authored React views beside chat (not plugin code); CLI status line booleans only | Files | Trusted workspaces (cursor.md) | ? |
| **Copilot CLI hooks + extensions + `statusLine`** | Hooks: subprocess command/exec, `http`, `prompt` (sessionStart). Extensions: separate Node.js process joined via SDK | preToolUse (allow/deny/`modifiedArgs`), postToolUse (modify result), userPromptTransformed (rewrite model-facing text), agentStop/subagentStop (continue), sessionStart (context, auto-submit prompt), preCompact (observe), notification; extensions subscribe to session events | Hook progress lines (persistent or transient); `statusLine` command (Claude Code shape) with `refreshInterval`; footer item toggles; extensions add tools, slash commands, `session.log` | Extension process memory; status line timer | Extensions: experimental flag, `/extensions mode`; first-party plugins auto-update at session start; other marketplaces opt in with `autoUpdate: true` | Extensions experimental; SDK hooks GA |
| **VS Code (agent hooks, extension API, Agent Host)** | Local harness hooks: subprocess; extension API: in-process extension host | Local hooks: SessionStart, UserPromptSubmit, PreToolUse (block, approve, change input), PostToolUse, PreCompact, SubagentStart/Stop, Stop | Extension API: chat participants, LM tools, webviews; renders MCP Apps; Agent Host runs Copilot, Claude and Codex harnesses | ? | Trusted workspace, `chat.useHooks` | Hooks Preview |
| **Cline SDK plugins** | In process, TS (`AgentPlugin`) | `beforeRun/afterRun/beforeModel/afterModel/beforeTool/afterTool/onEvent` | None documented | ? | ? | SDK, CLI, Kanban only; not VS Code/JetBrains extension |
| **ACP (Agent Client Protocol)** | Agent is a subprocess of the client, JSON-RPC 2.0 | Client sends prompts, cancel; agent streams messages, tool calls, plans, state, usage; asks permission, elicitation | Client (editor) renders all; agent supplies data only | Agent sessions; list/resume | Client mediates permissions | v1 current; v2 baseline described as stable but the v2 surface "labeled draft"; proxies RFD draft |
| **MCP Apps (MCP-UI)** | MCP server supplies HTML (`ui://`); host renders in sandboxed iframe | Bound to a tool call; app can call tools, send messages, update model context | Inline, fullscreen, picture-in-picture; the listed hosts are web and desktop products | Host-managed | Sandboxed iframe, CSP, sandbox permissions the host MAY grant | Spec 2026-01-26 stable; opt-in extension |
| **Agent Plugins 1.0** | Package format, not a runtime | Portable: skills and MCP servers only; hooks only as client extensions | None portable | — | Client-controlled | Spec 1.0.0 |
| **Claude Agent SDK / Codex SDK** | Embedding library, in the host program (TS/Python) | SDK hooks as callbacks (tool, session, stop), `canUseTool`; Codex SDK starts, continues, resumes threads | Host program draws | Host | Host | Stable releases |

## 2. Capability matrix (what each layer can do at each point)

Y = documented; P = partial (see note); N = documented absence or the layer has no such mechanism;
? = not established by this read.

| Layer | Pre-tool deny | Pre-tool rewrite | Post-tool rewrite | Prompt: add context | Prompt: rewrite | System prompt edit | Turn end: continue | Session start / end | Compaction | Custom status line | Toast / notify | Dialog | Panel / widget | Restyle built-ins | Timers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Code settings hooks | Y | Y | P¹ | Y | ? | N | Y | Y / Y | P (block, observe) | Y (`statusLine`) | P (text) | N | N | N | P (status `refreshInterval`) |
| Claude Code mods | Y | Y | Y | Y | Y | Y | Y | Y / Y | Y¹² | P² | Y | Y | Y | Y | Y |
| Pi | Y | Y | Y | Y | P¹¹ | Y | Y | Y / Y | P¹³ | Y | Y | Y | Y | P³ | Y |
| Amp | Y | Y | Y | Y | N | P⁴ | Y | Y / N | ? | P⁵ | Y | Y | N | N | Y |
| OpenCode 1.x | Y⁶ | Y | Y | Y | Y | Y (experimental) | ? | Y (events) | Y (experimental) | P (slot) | Y | Y | Y | ? | Y |
| OpenCode 2.x | Y¹⁴ | Y | ? | Y | Y | Y | ? | ? | Y | Y (slot) | Y | Y | Y | P (slot replace) | Y |
| Codex | Y | Y | P⁷ | Y | ? | N | Y | Y / Y | P (stop only) | N (fixed items) | P (text, `notify`, OSC 9) | N | N | N | N |
| Gemini CLI | Y | Y | P (context) | Y | ? | P⁸ | Y | Y / Y | P (observe) | N (fixed items) | P (text) | N | N | N (themes) | N |
| Cursor | Y | Y | P (MCP output) | P (session start only) | N | N | Y | Y / Y | P (observe) | N | P (text) | N | N | N | N |
| Copilot CLI | Y | Y | Y | Y (sessionStart; `userPromptTransformed`) | P⁹ | ? | Y | Y / Y | P (observe) | Y (`statusLine`) | P (progress lines) | N | N | N | P (status `refreshInterval`) |
| Cline SDK | P¹⁵ | ? | ? | ? | ? | Y¹⁰ | ? | Y (run) | ? | N | N | N | N | N | ? |

Notes. ¹ From research files: PostToolUse can block or add context; whole-result replacement not
re-read here. ² `$.ui.status` is a line under the prompt, separate from `statusLine` (per
claude-code-mods.md). ³ Header, footer and editor replacement and tool/message renderers; not every
built-in row. ⁴ Only through a custom agent mode (`createAgent` instructions); `agent.start` appends
to the user message. ⁵ `createStatusItem`, CLI only, documented under `experimental`. ⁶ By throwing
in `tool.execute.before`. ⁷ A blocking PostToolUse replaces what the model sees with the hook's
feedback (codex.md). ⁸ Inference: `BeforeModel` overrides parts of `llm_request`, whose messages
carry a `system` role; no sentence says the system instruction can be replaced. ⁹ `modifiedPrompt`
only for SDK programmatic hooks; `userPromptTransformed` rewrites the model-facing content. ¹⁰ The
guide suggests `beforeRun` or `beforeModel` to adjust the system prompt. ¹¹ Through the `context`
event, which transforms the messages of one request; no sentence read says the stored user prompt
can be rewritten. ¹² The 2.1.288 declarations let `session.compact` rewrite the instructions or
messages, answer its own `{ messages }`, or skip; the reference page lists only skip. ¹³ `turn_end`
and `agent_before_settle` handlers can propose `compaction` entries. ¹⁴ `permission.hook evaluate`
can set `deny` (§3.5). ¹⁵ A throw in `beforeTool` counts as a tool failure; the guide says hooks are
for observation, not for changing behaviour.

## 3. Per-harness findings

### 3.1 Claude Code (mods, settings hooks, `statusLine`)

Mods are covered in depth by `harnesses/claude-code-mods.md`; only facts needed for the cross-harness
comparison are listed.

- A mod is a plugin whose JS/TS handlers run inside Claude Code; settings hooks run as a shell
  command, HTTP request or prompt (L, https://code.claude.com/docs/en/plugins/mods/overview,
  2026-10-03). "A mod's handlers are functions that run inside Claude Code instead."
- A mod can draw a pane or a band, redraw Claude Code's own interface, hold or answer a tool call,
  add commands, and share data between hooks (L, same URL, 2026-10-03).
- Hooks run on every surface that loads the plugin; "only the terminal and the Desktop app show a
  mod's panes, bands, and replaced rows" (L, same URL, 2026-10-03). The VS Code chat panel, `-p`,
  the Agent SDK and cloud sessions run hooks and draw nothing (L, same URL, 2026-10-03).
- "Mods aren't sandboxed." A mod can approve a tool call before the user is asked, and cannot
  change the permission prompt (L, same URL, 2026-10-03).
- Event groups: tools, prompts and system prompt (`prompt.compose`, `prompt.section`), commands and
  config, turns, session (including `session.compact` skip), subagents, interface, other mods,
  telemetry, and every settings-hook event as `classic.<Event>` (L,
  https://code.claude.com/docs/en/plugins/mods/reference, 2026-10-03).
- Limits: 10 s own time per hook per event; redraws throttled to 10 per second (30 in the terminal
  for the visible pane, the expanded band and the hint line under the prompt); `$.store` 4 MiB; toast 4 s by default (L, same URL, 2026-10-03).
- Background work runs on `$.clock.every` started from `session.start` (L,
  https://code.claude.com/docs/en/plugins/mods/api, 2026-10-03).
- The `statusLine` setting runs a command with session JSON on stdin and shows its stdout; it
  re-runs on new assistant messages, `/compact`, mode changes, and an optional `refreshInterval`
  (L, https://code.claude.com/docs/en/statusline, 2026-10-03). "Claude Code debounces updates at
  300ms."
- Each printed line is a separate row, and OSC 8 escape sequences make text clickable in
  supporting terminals (L, same URL, 2026-10-03).
- The status line "temporarily hides during certain UI interactions, including the help menu and
  permission prompts" (L, same URL, 2026-10-03).

### 3.2 Pi coding agent (extensions)

- "An extension runs inside the Pi process with the same operating-system permissions." Extensions
  are TypeScript modules loaded through jiti with no build step (L,
  https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/extensions.md,
  2026-10-03).
- `before_agent_start` exposes the prompt and structured system-prompt options; "Returning
  `systemPrompt`, or setting `forceSystemPrompt`, replaces the whole prompt for that run" (L, same
  URL, 2026-10-03).
- `tool_call` can mutate input or block execution; `tool_result` handlers compose; `message_end`
  can replace a finalized message (L, same URL, 2026-10-03).
- `context` transforms conversation messages; `context_with_system` owns the complete transcript
  for one request (L, same URL, 2026-10-03).
- `turn_end` and `agent_before_settle` can append entries (including proposed `compaction` entries)
  and return `continue: true` for one more model request (L, same URL, 2026-10-03).
- A failing `tool_call` handler blocks the tool as a fail-safe; other handler errors are reported
  and Pi continues (L, same URL, 2026-10-03).
- "Do not start processes, sockets, watchers, or timers in the factory because some invocations
  load extensions without starting a session." Start them from `session_start` (L, same URL,
  2026-10-03).
- State: tool-result `details` for branch-following state, `pi.appendEntry()` for durable data kept
  out of model context, external storage across sessions (L, same URL, 2026-10-03).
- `ctx.ui` provides dialogs, notifications, status text, widgets, titles, editor access and custom
  components; header, footer and editor can be replaced through component factories (L,
  https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/tui.md,
  2026-10-03).
- `ctx.ui.custom()` with `overlay: true` draws above existing content; fullscreen mode routes mouse
  events to components (L, same URL, 2026-10-03).
- Modes: interactive TUI has the full UI; RPC forwards supported dialogs and notifications; JSON and
  print modes have no UI; guard with `ctx.mode === "tui"` and `ctx.hasUI` (L, extensions.md URL
  above, 2026-10-03).
- In RPC mode, dialog methods (`select`, `confirm`, `input`, `editor`) become
  `extension_ui_request` messages that block for an `extension_ui_response`; `notify`, `setStatus`,
  `setWidget`, `setTitle` and `set_editor_text` are fire-and-forget (L,
  https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/rpc-extension-ui.md,
  2026-10-03).
- A dialog request may carry a `timeout`, after which the agent side resolves with a default value
  (L, same URL, 2026-10-03).
- RPC widgets: "Only string arrays are supported in RPC mode; component factories are ignored."
  `custom()`, `setFooter()` and `setHeader()` are no-ops in RPC (L, same URL, 2026-10-03).
- The GitHub repository moved: `github.com/badlogic/pi-mono` answers 301 to
  `github.com/earendil-works/pi`; npm `@earendil-works/pi-coding-agent` 1.0.1 published
  2026-10-03 (M, HTTP and npm registry, 2026-10-03).
- No stability label was found in the extension docs (L, extensions.md URL above, 2026-10-03).

### 3.3 Amp (plugins)

- Plugins "are long-lived processes that may run for multiple threads concurrently", in
  `.amp/plugins/` or `~/.config/amp/plugins/`, executed with Bun (L,
  https://ampcode.com/docs/plugin-api, 2026-10-03).
- Plugin scopes are workspace (admin-managed), personal, project and system; same-name precedence is
  project, system, personal, workspace (L, https://ampcode.com/docs/customize/plugins, 2026-10-03).
- "Plugins run code in your environment, so only load plugins you trust." No consent prompt is
  documented (L, same URL, 2026-10-03).
- Events: `session.start`, `tool.call`, `tool.result`, `agent.start`, `agent.end`,
  `changes.prompt` (L, https://ampcode.com/docs/plugin-api, 2026-10-03).
- `tool.call` returns allow, reject-and-continue, modify (change input) or synthesize (result
  without running the tool) (L, https://ampcode.com/docs/customize/plugins, 2026-10-03).
- `tool.result` can return a replacement status or output before the result reaches the model (L,
  same URL, 2026-10-03).
- `agent.start` can append a message after the user's content, hidden unless `display: true`; the
  type comment says it allows "modifying the system prompt", but the result type has only `message`
  (L, https://ampcode.com/docs/plugin-api, 2026-10-03). Inference: per-turn system-prompt edits are
  not available; a custom agent mode (`createAgent` with `instructions`, optionally `extends` a
  built-in mode) is the documented way to change instructions.
- `agent.end` can return `continue` with a follow-up user message; `maxContinuations` defaults to 5
  and any user message resets the count (L, same URL, 2026-10-03).
- UI: `notify`, `input`, `select`, `confirm` (with editable fields, image previews, link buttons),
  command palette commands with availability states, transcript link patterns (L, same URL,
  2026-10-03).
- "Plugin UI is mirrored across TUI and Web surfaces" (L, https://ampcode.com/docs/customize/plugins,
  2026-10-03).
- "Status items appear in the CLI status line. Other clients ignore them"; the worked example calls
  `amp.experimental?.createStatusItem()` and ticks it with `setInterval` every second (L, same URL,
  2026-10-03).
- `onDispose` callbacks together get about 3 seconds and do not run on crash or SIGKILL (L,
  https://ampcode.com/docs/plugin-api, 2026-10-03).
- APIs under `amp.experimental` "are not stable and may change or be removed" (L, same URL,
  2026-10-03).
- The plugins guide credits Pi's extension API as the inspiration for Amp's (L,
  https://ampcode.com/docs/customize/plugins, 2026-10-03).
- `@ampcode/plugin` is published as dated pre-release builds (`0.0.0-20261003001754-...`) (M, npm
  registry, 2026-10-03).

### 3.4 OpenCode 1.x and Kilo (plugins, server, SDK, TUI plugins)

- A plugin is a JS/TS module exporting plugin functions; files in `.opencode/plugins/` and
  `~/.config/opencode/plugins/` "are automatically loaded at startup"; npm plugins install through
  Bun (L, https://opencode.ai/docs/plugins/, 2026-10-03).
- No trust or consent step for project plugins is documented (L, same URL, 2026-10-03).
- Server-plugin hooks in the `dev`-branch source read on 2026-10-03 (the latest npm release was
  1.18.34): `event`, `config`, `tool`, `auth`, `provider`,
  `chat.message`, `chat.params`, `chat.headers`, `permission.ask`, `command.execute.before`,
  `tool.execute.before`, `shell.env`, `tool.execute.after`, `tool.definition`, and experimental
  `chat.messages.transform`, `chat.system.transform`, `provider.small_model`, `session.compacting`,
  `compaction.autocontinue`, `text.complete` (L,
  https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/plugin/src/index.ts,
  2026-10-03).
- `experimental.session.compacting` can add context to the compaction prompt or replace it with
  `output.prompt` (L, https://opencode.ai/docs/plugins/, 2026-10-03).
- The server exposes TUI control routes: append, submit and clear the prompt, open dialogs, execute
  a command, show a toast (L, https://opencode.ai/docs/server/, 2026-10-03); the SDK wraps them as
  `client.tui.appendPrompt` and `client.tui.showToast` (L, https://opencode.ai/docs/sdk/,
  2026-10-03).
- The server can be protected with HTTP basic auth via `OPENCODE_SERVER_PASSWORD` and publishes an
  OpenAPI 3.1 spec and an SSE event stream (L, https://opencode.ai/docs/server/, 2026-10-03).
- A separate TUI plugin module type (`tui`) gets OpenTUI/Solid rendering: slots `home_prompt`,
  `session_prompt`, `home_footer`, `sidebar_title`, `sidebar_content`, `sidebar_footer`; dialogs;
  `toast`; routes; keymap; a `kv` store (L,
  https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/plugin/src/tui.ts, 2026-10-03).
- Kilo plugins use the same API (`@kilocode/plugin`, `.kilo/plugin/`) and "work in both the Kilo
  CLI and the VS Code extension" (L, https://kilo.ai/docs/automate/extending/plugins, 2026-10-03).
- The repository moved: `github.com/sst/opencode` answers 301 to `github.com/anomalyco/opencode`
  (M, HTTP, 2026-10-03). `opencode-ai` 1.18.34 published 2026-09-30 (M, npm, 2026-10-03).

### 3.5 OpenCode 2.x

- OpenCode 2 is a separate install (`@opencode/cli`, first published 2026-09-02, 2.0.22 on
  2026-10-02) (M, npm registry, 2026-10-03).
- "The plugin context is essentially an OpenCode server client", with added methods for transforms,
  runtime hooks, reloads and registrations (L, https://opencode.ai/v2/docs/build/plugins,
  2026-10-03).
- Session hooks: `prompt` (mutable draft of the admitted user input, no typed rejection),
  `context` (system instructions, messages, tools, options before each agent-loop model call),
  `compaction` (can supply the result and skip the model call), `generate`, `title`,
  `model.request`, `http.request`, `http.response`, `retry`, and experimental WebSocket hooks (L,
  same URL, 2026-10-03).
- "Changes affect only the outgoing model call, not persisted history or configuration." (L, same
  URL, 2026-10-03).
- Tool hooks `execute.before` (inspect or replace input) and `execute.after`; permission hook
  `evaluate` can change `allow`/`ask` to any effect, but a configured deny is final (L, same URL,
  2026-10-03).
- CLI plugins extend the terminal with commands, routes, slots, Markdown renderers, notifications
  and local state (L, https://opencode.ai/v2/docs/build/plugins/cli, 2026-10-03).
- Slots: `app`, `home.footer`, `home.footer.status`, `prompt.footer`, `prompt.footer.status`,
  `prompt.footer.file`, `session.composer.top`, `sidebar.content`, `sidebar.footer`, placed by
  prepend, append, before, after or replace; plus `session.panel`, where "The host owns sizing,
  focus, and full-screen presentation" (L, same URL, 2026-10-03).
- "Durable storage persists JSON across restarts and synchronizes across TUI instances"; memory
  storage survives plugin reloads and ends with the TUI (L, same URL, 2026-10-03).
- Attention requests show a system notification, play a sound, or both, by terminal focus (L, same
  URL, 2026-10-03).
- RPC plugins declare methods, errors and events callable by other plugins or clients (L,
  https://opencode.ai/v2/docs/build/plugins/rpc, 2026-10-03).
- One package can serve both majors: V1 calls `server()`, V2 reads `id` and `setup()`; "sharing an
  export does not translate V1 hooks into V2 hooks" (L, https://opencode.ai/v2/docs/build/plugins,
  2026-10-03).

### 3.6 Codex (hooks, status line, notify, app-server, SDK)

- Events: PreToolUse, PermissionRequest, PostToolUse, PreCompact, PostCompact, UserPromptSubmit,
  SubagentStop, Stop, Interrupt, SessionStart, SubagentStart, SessionEnd (L,
  https://developers.openai.com/codex/hooks, 2026-10-03).
- "command and mcp_tool handlers are supported. prompt and agent handlers are parsed but skipped."
  (L, same URL, 2026-10-03).
- PreToolUse can rewrite a call: return `permissionDecision: "allow"` with `updatedInput` (L, same
  URL, 2026-10-03).
- `statusMessage` is optional per hook; `SessionEnd` and `Interrupt` default to 1 s and allow up to
  3 s; `additionalContextLimit` caps model-visible context before spilling to disk (L, same URL,
  2026-10-03).
- `systemMessage` is "Surfaced as a warning in the UI or event stream" (L, same URL, 2026-10-03).
- Installed plugins can bundle lifecycle hooks; plugin hooks need trust review before they run (L,
  same URL and https://developers.openai.com/codex/plugins, 2026-10-03).
- Plugins can contain skills, MCP servers (which "can optionally include custom UI"), browser
  extensions and hooks (L, https://developers.openai.com/codex/plugins, 2026-10-03).
- `tui.status_line`: "Ordered list of TUI footer status-line item identifiers. null disables the
  status line." `tui.terminal_title` is a parallel list (L,
  https://developers.openai.com/codex/config-reference, 2026-10-03).
- Inference: the reference documents no command field for the status line, so Codex status-line
  content is limited to built-in item identifiers (from the L reference above, 2026-10-03).
- `notify` runs an external program on supported events, "currently only agent-turn-complete";
  `tui.notifications` filters built-in TUI notifications; `tui.notification_method` is `auto`,
  `osc9` or `bel` (L, https://developers.openai.com/codex/config-advanced, 2026-10-03).
- Project-local `.codex/config.toml` ignores `notify` and other provider, notification and
  telemetry keys (L, https://developers.openai.com/codex/config-reference, 2026-10-03).
- "Codex app-server is the interface Codex uses to power rich clients (for example, the Codex VS
  Code extension)." (L, https://developers.openai.com/codex/app-server, 2026-10-03).
- Transport: JSON-RPC over stdio by default; WebSocket "experimental and unsupported"; Unix socket
  (L, same URL, 2026-10-03).
- Experimental methods and fields are gated behind `capabilities.experimentalApi`; `dynamicTools`
  on `thread/start` and `tool/requestUserInput` are experimental (L, same URL, 2026-10-03).
- Server requests a client must render: command-execution and file-change approvals, permission
  grants, `tool/requestUserInput` (1 to 3 questions), `mcpServer/elicitation/request` (forms) (L,
  same URL, 2026-10-03).
- Notifications include item started/completed, message deltas, plan and diff updates, and
  `hook/started`/`hook/completed` for synchronous hooks (L, same URL, 2026-10-03).
- The TypeScript SDK starts, continues and resumes local Codex threads; the Python SDK "controls the
  local Codex app-server over JSON-RPC" and is a stable release (L,
  https://developers.openai.com/codex/sdk, 2026-10-03).
- `@openai/codex` 0.160.0 published 2026-10-01 (M, npm registry, 2026-10-03).

### 3.7 Gemini CLI (hooks, extensions)

- Hook handler type: "Currently only `"command"` is supported." Input on stdin, JSON on stdout;
  exit 2 blocks (L,
  https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/hooks/reference.md,
  2026-10-03).
- Events: BeforeTool, AfterTool, BeforeAgent, AfterAgent, BeforeModel, BeforeToolSelection,
  AfterModel, SessionStart, SessionEnd, Notification, PreCompress (L, same URL, 2026-10-03).
- BeforeTool output `tool_input` merges with the model's arguments (L, same URL, 2026-10-03).
- BeforeModel can override parts of the outgoing request, return a synthetic response that skips
  the model, or deny the turn; AfterModel can replace each streamed chunk (L, same URL,
  2026-10-03).
- BeforeToolSelection can restrict the tool list or force tool mode; whitelists from several hooks
  are combined (L, same URL, 2026-10-03).
- `systemMessage` is "Displayed immediately to the user in the terminal" (L, same URL, 2026-10-03).
- Extensions package prompts, MCP servers, custom commands, themes, hooks, sub-agents and skills;
  hooks live in the extension's `hooks/hooks.json` (L,
  https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/extensions/index.md and
  .../docs/extensions/reference.md, 2026-10-03).
- Extension policies cannot pre-approve: "Gemini CLI ignores any `allow` decisions or `yolo` mode
  configurations in extension policies." (L, extensions/reference.md, 2026-10-03).
- `gemini extensions install` shows a confirmation prompt that `--consent` skips (L, same URL,
  2026-10-03).
- Extension themes can recolour the CLI; no extension API to draw panels or widgets was found (L,
  same URL, 2026-10-03).
- Footer: `ui.footer.items` is a list of item IDs; other footer keys hide built-in items (L,
  https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/reference/configuration.md,
  2026-10-03).
- `--acp` starts the agent in ACP mode (the page expands it as "Agent Communication Protocol") (L,
  same URL, 2026-10-03).
- `@google/gemini-cli` 0.62.0 published 2026-09-29 (M, npm registry, 2026-10-03).

### 3.8 Cursor (hooks, plugins, canvases, ACP)

- Agent hooks: sessionStart/End, preToolUse/postToolUse/postToolUseFailure, subagentStart/Stop,
  before/afterShellExecution, before/afterMCPExecution, beforeReadFile, afterFileEdit,
  beforeSubmitPrompt, preCompact, stop, afterAgentResponse, afterAgentThought; Tab hooks; app
  lifecycle `workspaceOpen` (L, https://cursor.com/docs/hooks, 2026-10-03).
- preToolUse returns `permission` and optional `updated_input`; "ask" is accepted by the schema but
  not enforced today (L, same URL, 2026-10-03).
- beforeSubmitPrompt can only allow or block submission (L, same URL, 2026-10-03).
- sessionStart "runs as fire-and-forget" and can return `env` and `additional_context` (L, same
  URL, 2026-10-03).
- `workspaceOpen` "Can return additional plugin paths to load for the current workspace" (L, same
  URL, 2026-10-03).
- Prompt hooks use an LLM to evaluate a natural-language condition and return `{ ok, reason }` (L,
  same URL, 2026-10-03).
- Responses from all sources merge: deny wins over ask, ask over allow; messages concatenate (L,
  same URL, 2026-10-03).
- "Cursor supports the Agent Plugins open standard alongside its own plugin format." Cursor Plugins
  add rules, agents, commands, hooks and variables (L, https://cursor.com/docs/plugins,
  2026-10-03).
- Canvases are agent-built interactive views next to the chat, reopenable and shareable, and can be
  packaged in skills (L, https://cursor.com/docs/agent/tools/canvas, 2026-10-03). Inference: a
  canvas is model output that Cursor renders, not a plugin runtime, so third-party code reaches it
  only through skills.
- The Cursor CLI (`agent acp`) speaks ACP over stdio; "Cursor sends ACP extension methods for
  richer client UX": blocking `cursor/ask_question`, `cursor/create_plan`; notifications
  `cursor/update_todos`, `cursor/task`, `cursor/generate_image` (L,
  https://cursor.com/docs/cli/acp, 2026-10-03).
- Cursor CLI status line settings are booleans (`display.showStatusLineRunningTime`), with no custom
  command (L, https://cursor.com/docs/cli/reference/configuration, 2026-10-03).

### 3.9 GitHub Copilot CLI and VS Code

- Copilot CLI hook events include agentStop and subagentStop (block forces another turn),
  preToolUse (allow, deny or modify), postToolUse (modify the result or add context),
  permissionRequest, preCompact (notification only), sessionStart (context), sessionEnd,
  userPromptSubmitted, userPromptTransformed (rewrites model-facing content), notification,
  errorOccurred (L, https://docs.github.com/en/copilot/reference/hooks-configuration, 2026-10-03).
- preToolUse can return `modifiedArgs` to substitute tool arguments (L, same URL, 2026-10-03).
- `modifiedPrompt` on userPromptSubmitted "is honored only by SDK programmatic hooks" (L, same URL,
  2026-10-03).
- A `prompt` hook on sessionStart auto-submits text or a slash command, in the CLI only (L, same
  URL, 2026-10-03).
- Command hooks can write `{"type": "progress", "message": "..."}` lines to the CLI timeline, with
  `"temporary": true` for a transient line; "Progress messages are display-only" (L, same URL,
  2026-10-03).
- A hook configured under the PascalCase name `PreToolUse`, as Claude Code plugins use it, gets
  Claude's matcher semantics; other PascalCase names select the VS Code-compatible snake_case
  payload (L, same URL, 2026-10-03).
- Copilot CLI `statusLine`: `type` "must be `"command"`", the script gets session JSON on stdin and
  prints status to stdout, with `padding` and `refreshInterval` (1 s minimum) (L,
  https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference,
  2026-10-03). Inference: this has the same configuration shape as Claude Code's `statusLine`.
  Copilot's `command` is a path to an executable, not a shell line, and the page does not give the
  stdin fields, so a script written for Claude Code is not shown to work unchanged.
- `footer` toggles built-in status-line items, managed by `/statusline` or `/footer` (L, same URL
  and .../cli-command-reference, 2026-10-03).
- "Each extension is a small Node.js module that runs as a separate process alongside your
  interactive session and connects back to it." Extensions add tools and slash commands (L,
  https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-extensions, 2026-10-03).
- "GitHub Copilot CLI extensions are currently an experimental feature and are subject to change."
  They need `--experimental` or `/experimental on`; `/extensions mode` offers Load & Augment, Load
  Only, Disabled (L, same URL, 2026-10-03).
- Project extensions live in `.github/extensions/NAME/`; JavaScript only (L, same URL,
  2026-10-03).
- Extensions call `joinSession` from the bundled `@github/copilot-sdk/extension`, subscribe to
  session events such as `tool.execution_start` and `assistant.usage`, and write to the transcript
  with `session.log` (L, https://docs.github.com/en/copilot/tutorials/create-an-extension,
  2026-10-03).
- Copilot CLI reads Agent Plugins 1.0 and keeps its own components (agents, commands, rules, hooks,
  LSP servers) in a `com.github.copilot/` namespace directory (L,
  https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference,
  2026-10-03).
- Copilot SDK hooks are in-process callbacks (`onPreToolUse`, `onPostToolUse`, `onSessionStart`, …)
  in TypeScript, Python, Go, .NET and Java (L,
  https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/hooks, 2026-10-03).
- "The VS Code hooks experience is in Preview." "The Agent Host is the process that hosts the
  Copilot, Claude, and Codex harnesses"; the Local harness runs in the extension host (L,
  https://code.visualstudio.com/docs/copilot/customization/hooks, 2026-10-03).
- Local harness events: SessionStart, UserPromptSubmit, PreToolUse (block, request approval,
  change input), PostToolUse, PreCompact, SubagentStart, SubagentStop, Stop (L, same URL,
  2026-10-03).
- Shared hook files do not mean shared behaviour: events, names, matchers, payloads and decisions
  can differ by harness (L, same URL, 2026-10-03).
- VS Code's extension API offers chat participants, language model tools, the Language Model API
  and MCP integration as AI extension points (L,
  https://code.visualstudio.com/api/extension-guides/ai/ai-extensibility-overview, 2026-10-03).
- `@github/copilot` 1.0.91 published 2026-10-01 (M, npm registry, 2026-10-03).

### 3.10 Cline

- The hooks page now only says "See details under SDK Plugins page." (L,
  https://docs.cline.bot/customization/hooks, 2026-10-03).
- An `AgentPlugin` registers tools, commands, rules and events; lifecycle hooks are `beforeRun`,
  `afterRun`, `beforeModel`, `afterModel`, `beforeTool`, `afterTool`, `onEvent` (L,
  https://docs.cline.bot/sdk/plugins, 2026-10-03).
- Plugins apply to the SDK, CLI and Kanban: "This feature is not applicable on VSCode and JetBrains
  Extension for now." (L, https://docs.cline.bot/customization/plugins, 2026-10-03).
- Single-file plugins can import only Node built-ins and `@cline/*` (L,
  https://docs.cline.bot/sdk/guides/writing-plugins, 2026-10-03).
- Cline also runs as an ACP agent in Zed, JetBrains, Neovim and Emacs (L,
  https://docs.cline.bot/llms.txt, 2026-10-03).
- No UI API for plugins was found (L, the three pages above, 2026-10-03).

### 3.11 Agent Client Protocol (ACP)

- Agents "typically run as subprocesses of the Client"; messages are JSON-RPC 2.0 (L,
  https://agentclientprotocol.com/protocol/v2/overview, 2026-10-03).
- v2 session updates: message chunks and whole messages, `state_update` (`running`, `idle`,
  `requires_action`), `tool_call_update`, `tool_call_content_chunk`, `terminal_update`,
  `plan_update`, `available_commands_update`, `config_option_update`, `session_info_update`,
  `usage_update` (L, https://agentclientprotocol.com/protocol/v2/migration, 2026-10-03).
- Client methods the agent can call: `session/request_permission` (baseline) and
  `elicitation/create` (optional, structured user input) (L, v2 overview URL above, 2026-10-03).
- "v2 removes the entire v1 Client-provided execution surface" (file system and terminal methods);
  clients should offer such tools as an MCP server instead (L, migration URL above, 2026-10-03).
- "The v2 protocol surface as a whole is still labeled draft"; unstable features sit in a separate
  schema behind capabilities (L, same URL, 2026-10-03).
- Extensibility: a `_meta` field on many types and method names starting with `_` (L,
  https://agentclientprotocol.com/protocol/v1/extensibility, 2026-10-03).
- Session Notices (advisory notices outside conversation history) moved to Preview on 2026-09-24,
  with v1 support in Zed and the Claude Agent and Codex adapters; Session Compaction moved to
  Preview on 2026-09-23 (L, https://agentclientprotocol.com/rfds/updates, 2026-10-03).
- The proxy-chains RFD proposes proxies between client and agent that "can intercept and transform
  messages", as a universal extension mechanism; a prototype exists as Rust crates, and the RFD is
  not accepted (L, https://agentclientprotocol.com/rfds/proxy-chains, 2026-10-03).
- The RFD's rationale: "MCP servers are fundamentally limited because they sit "behind" the agent."
  (L, same URL, 2026-10-03).
- Listed agents include Claude Agent (via Zed's adapter), Codex CLI (via ACP's adapter), Cursor,
  Gemini CLI, GitHub Copilot (public preview), OpenCode, Cline, Kiro, Junie, Qwen Code, Mistral
  Vibe and Pi (via an adapter) (L, https://agentclientprotocol.com/get-started/agents,
  2026-10-03).
- Listed clients include Zed, JetBrains, Neovim plugins, Emacs, VS Code extensions, Obsidian
  plugins, Sublime Text, Qt Creator, and desktop and web clients (L,
  https://agentclientprotocol.com/get-started/clients, 2026-10-03).
- `@agentclientprotocol/sdk` 1.7.0 published 2026-10-02 (M, npm registry, 2026-10-03).

### 3.12 MCP Apps and MCP-UI

- MCP Apps let a tool declare `_meta.ui.resourceUri` pointing to a `ui://` resource; the host
  fetches the HTML and renders it, typically in a sandboxed iframe (L,
  https://modelcontextprotocol.io/extensions/apps/overview, 2026-10-03).
- "MCP Apps run in a sandboxed iframe controlled by the host." (L, same URL, 2026-10-03).
- The app talks to the host over a JSON-RPC dialect of MCP: it can request tool calls, send
  messages, update the model's context and receive data (L, same URL, 2026-10-03).
- Spec methods include `ui/message`, `ui/update-model-context`, `ui/open-link`,
  `ui/request-display-mode`, tool-input and tool-result notifications; display modes are `inline`,
  `fullscreen`, `pip` (L,
  https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx,
  2026-10-03).
- Spec version 2026-01-26 is marked Stable; a draft folder also exists (L,
  https://github.com/modelcontextprotocol/ext-apps, 2026-10-03).
- "Extensions are always opt-in": both client and server must declare the extension (L,
  https://modelcontextprotocol.io/extensions/client-matrix, 2026-10-03).
- Hosts listed for MCP Apps: Claude (web), Claude Desktop, VS Code GitHub Copilot, Microsoft 365
  Copilot, Goose, Postman, MCPJam, ChatGPT, Cursor, Archestra.AI, PostHog Code; no terminal coding
  CLI is listed (L, same URL, 2026-10-03). The matrix is community-maintained (L, same URL).
- MCP-UI's site says MCP-UI is now standardised into MCP Apps and its packages implement that spec
  (L, https://mcpui.dev/, 2026-10-03, via a summarising fetch).
- An experimental MCP interceptors extension (SEP-2624) exists only as a reference implementation
  "for prototyping and feedback only" (L,
  https://github.com/modelcontextprotocol/experimental-ext-interceptors, 2026-10-03).
- `@modelcontextprotocol/ext-apps` 2.0.3 published 2026-09-25 (M, npm registry, 2026-10-03).

### 3.13 Agent Plugins 1.0 (packaging standard)

- Agent Plugins 1.0.0 defines a portable package of Agent Skills and MCP servers, with a
  `plugin.json` manifest (L, https://agent-plugins.org, 2026-10-03).
- Its initial Technical Steering Committee includes maintainers from Amazon, Cursor, Microsoft,
  OpenAI and Vercel (L, same URL, 2026-10-03).
- Client-specific behaviour (for example hooks) lives under a reverse-domain namespace directory;
  "Client extensions are not portable Agent Plugins components." (L,
  https://agent-plugins.org/plugin-authors/client-extensions, 2026-10-03).
- Compatible clients listed: VS Code, Cursor, GitHub Copilot, ChatGPT & Codex, Kiro, Hermes Agent,
  OpenClaw, Grok Bot, NanoClaw, OpenHands. Claude Code is not listed (L,
  https://agent-plugins.org/compatible-clients, 2026-10-03).

### 3.14 Embedding SDKs (Claude Agent SDK, Codex SDK)

- Claude Agent SDK hooks "are callback functions that run your code in response to agent events";
  they can block, modify input or inject context (L,
  https://code.claude.com/docs/en/agent-sdk/hooks, 2026-10-03).
- `SessionStart` and `SessionEnd` callback hooks exist in TypeScript, not in Python (L, same URL,
  2026-10-03).
- Approvals that no rule resolves reach the host's `canUseTool` callback (L,
  https://code.claude.com/docs/en/agent-sdk/permissions, 2026-10-03).
- Other languages drive the same loop by running the CLI as a subprocess with `-p` and
  `--output-format json` (L, https://code.claude.com/docs/en/agent-sdk/overview, 2026-10-03).
- Claude Code mods' hooks run under the Agent SDK but draw nothing there (L,
  https://code.claude.com/docs/en/plugins/mods/overview, 2026-10-03).
- Codex SDK facts are in §3.6.

## 4. Common denominators

### 4.1 Stated facts, collected across §3

- **Pre-tool interception with deny and input rewrite** is documented in every harness read except
  Cline: as a command hook in Claude Code, Codex, Gemini CLI, Cursor, Copilot CLI and VS Code's
  Local harness, and as an in-process handler in Claude Code mods, Pi, Amp, OpenCode (1.x and 2.x)
  and Kilo. Cline documents `beforeTool` for observation; a throw there counts as a tool failure.
- **Turn-end continuation** (hold the finish and send another message) is documented in Claude
  Code, Codex, Gemini CLI, Cursor, Copilot CLI, VS Code Local, Amp and Pi. OpenCode 1.x documents
  only an observed `session.idle` event.
- **Session start with added context** is documented in Claude Code, Codex, Gemini CLI, Cursor,
  Copilot CLI and VS Code Local; in-process layers have a session-start event.
- **Pre-compaction observation** is common (Claude Code, Codex, Gemini CLI, Cursor, Copilot CLI,
  VS Code Local). Editing or supplying the compaction result is documented in OpenCode
  (`session.compacting`, v2 `compaction`) and in the 2.1.288 declarations of Claude Code mods
  (`session.compact` can rewrite the instructions or messages, or answer its own `{ messages }`; the
  reference page lists only `{ skip }`); Pi handlers can propose `compaction` entries at
  `turn_end`.
- **System-prompt editing** is documented only in in-process layers: Claude Code mods, Pi, OpenCode
  (experimental in 1.x, `context` hook in 2.x), Cline (`beforeModel`, per its guide); Amp only via a
  custom agent mode. No command-hook harness documents it; Gemini's `BeforeModel` is the nearest.
- **User-visible output from a command hook** is plain text everywhere it exists: `systemMessage`
  (Claude Code, Codex, Gemini CLI), `user_message` (Cursor), progress lines (Copilot CLI),
  `statusMessage` (Codex).
- **A custom status line driven by a command** exists in Claude Code and Copilot CLI with the same
  shape (`type: "command"`, session JSON on stdin, stdout shown, `refreshInterval`). Codex, Gemini
  CLI and Cursor CLI offer only built-in items.
- **Packaging**: Agent Plugins 1.0 makes skills and MCP servers portable across VS Code, Cursor,
  Copilot and ChatGPT/Codex among others; hooks stay client-specific by design.
- **Rich UI from outside the harness**: the MCP Apps hosts in the community matrix are web and
  desktop products, none a terminal coding CLI, and the matrix does not say which surface of each
  host renders apps; ACP lets one
  agent stream structured state into many editors, but the client owns all drawing.

### 4.2 The lowest common denominator (inference)

Inference: across all harnesses read, the capability set that a harness-neutral layer can rely on
is:

1. A pre-tool gate that can deny and rewrite a call.
2. A prompt-submit or session-start point that can add model-visible context.
3. A turn-end point that can hold the finish and send one more message, with the harness's or the
   hook's own loop guard.
4. An observe-only pre-compaction point.
5. Plain-text messages to the user from a hook, and the transcript itself.
6. Skills and MCP servers, packaged once (Agent Plugins) and loaded everywhere.

A custom command status line is shared by only two harnesses (Claude Code, Copilot CLI), though they
are the two with the highest stated adoption in cross-harness.md §12; it is a strong second tier,
not a floor.

### 4.3 What only in-process UI layers have (inference)

Inference: only in-process layers (Claude Code mods, Pi, Amp, OpenCode TUI/CLI plugins) can keep
**live, interactive, stateful interface inside the harness**: panes, widgets, footers and dialogs
fed by session state that persists across events, refreshed on timers, and able to **hold a tool
call while asking the user**, then answer it. Command hooks are stateless per event, cannot draw,
and see only one event at a time; MCP Apps draw only inside a tool result, on hosts that are web and desktop products; ACP
leaves drawing to the client. In-process layers are also the only ones that can edit the system
prompt per request (§4.1).

Inference: the in-process layers converge on a small UI vocabulary: `notify`/toast, blocking
`confirm`/`select`/`input`, slash or palette commands, and a status entry (Pi `setStatus`, OpenCode
slots, Claude Code mods `$.ui.status` one line per mod, Amp only as an experimental CLI status
item). Pi and OpenCode also have a widget of lines; Amp documents none, and Claude Code mods draw
panes and a band instead. Pi's RPC subprotocol already serialises this vocabulary as JSON (blocking dialogs with timeouts and defaults;
fire-and-forget notify, status, string-array widgets) and drops component factories when no
terminal is present. That is a working precedent for a harness-neutral UI intent format with
graceful degradation: draw natively where an in-process layer exists, fall back to text messages
or a command status line elsewhere.

### 4.4 Stability caveats (stated facts)

- Experimental or preview: Claude Code mods (early, `latest` tag only, per claude-code-mods.md),
  Amp `experimental` APIs including status items, OpenCode `experimental.*` hooks and 2.x as a new
  major, Copilot CLI extensions, VS Code hooks, Codex app-server experimental surface, ACP v2
  ("labeled draft"), ACP proxies (RFD), MCP interceptors.
- Marked stable: Codex Python SDK, MCP Apps spec 2026-01-26, Agent Plugins 1.0.0, Copilot SDK hooks
  (GA per VS Code). No page read labels ACP v1 stable.

## Limits and open questions

- One day's reading, with no harness run. Several layers changed in the last month (OpenCode 2.x,
  Copilot CLI extensions, VS Code hooks, Claude Code mods), so names in this file go stale fast.
- The MCP-UI site was read through a summarising fetch only.
- Open: whether Codex, Gemini CLI or Cursor CLI add a command-driven status line; whether ACP
  proxies are accepted, which would give one interception layer for every ACP agent; whether a
  terminal harness renders MCP Apps; whether Agent Plugins grows a portable hook or UI component.
- Other files of this repository that this reading found out of date (2026-10-03):
  [cross-harness.md](cross-harness.md) H9 counts four harnesses with a command finish hook, and
  GitHub Copilot CLI (`agentStop`) and VS Code's Local harness (`Stop`, Preview) now make six; its H8
  list of committed executable files lacks `.github/hooks/*.json`, `.github/extensions/`,
  `.opencode/plugins/`, `.kilo/plugin/` and `.cline/plugins`; its §13.2 does not record MCP Apps,
  ACP or Agent Plugins 1.0. [pi.md](pi.md) cites `badlogic/pi-mono`, which now answers 301 to
  `earendil-works/pi`, and records only the finish event. [amp.md](amp.md), [codex.md](codex.md),
  [gemini-cli.md](gemini-cli.md), [cursor.md](cursor.md) and [others.md](others.md) record the
  finish event but not the tool, prompt and UI layers in §3 here; OpenCode's repository moved from
  `sst/opencode` to `anomalyco/opencode`. These files need a refresh pass.

## Sources

Every URL in the frontmatter was read on 2026-10-03; each claim above names the page it rests on.
Version and date facts come from the npm registry entries of `@anthropic-ai/claude-code`,
`@earendil-works/pi-coding-agent`, `@ampcode/plugin`, `opencode-ai`, `@opencode/cli`,
`@openai/codex`, `@google/gemini-cli`, `@github/copilot`, `@agentclientprotocol/sdk` and
`@modelcontextprotocol/ext-apps`, read the same day.
