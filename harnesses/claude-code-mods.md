---
last_checked: 2026-10-03
volatility: VOLATILE (an early-access API that its maker says can change between releases; launched 2026-10-01 in 2.1.287, not yet on the stable channel)
sources:
  - https://claude.com/blog/claude-code-mods
  - https://claude.dev/blog/getting-started-with-claude-code-mods/
  - https://code.claude.com/docs/en/plugins/mods/overview
  - https://code.claude.com/docs/en/plugins/mods/create
  - https://code.claude.com/docs/en/plugins/mods/reference
  - https://code.claude.com/docs/en/plugins/mods/interface
  - https://code.claude.com/docs/en/plugins/mods/events
  - https://code.claude.com/docs/en/plugins/mods/api
  - https://code.claude.com/docs/en/plugins/mods/admin
  - https://code.claude.com/docs/en/plugins/mods/troubleshoot
  - https://code.claude.com/docs/en/plugins/mods/test
  - https://code.claude.com/docs/en/hooks
  - https://github.com/anthropics/claude-code/issues/91870
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  - https://github.com/anthropics/claude-code/blob/main/mods/README.md
  - https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods
  - https://registry.npmjs.org/@anthropic-ai/claude-code
  - https://github.com/agentclientprotocol/claude-agent-acp
---

# Claude Code mods (function hooks)

> **Own results.** Claims marked (O) record observations the maintainers made while this document was written, dated and scoped where they appear. The records are not published ([CONVENTIONS](../CONVENTIONS.md)). All other claims rest on the documentation cited.

Re-check at each Claude Code release that names mods in its changelog, when the stable npm tag
reaches 2.1.287 or later, before relying on an event or method name, and by 2026-11-02.

What a Claude Code mod is, which events it can observe, rewrite or answer, what it can draw and on
which surface, how fast it can redraw, how it keeps state, how it extends the engine for other
mods, how it relates to settings hooks and plugins, and who can turn it on or off. For anyone who
plans to put behaviour or interface into Claude Code through a mod. Settings hooks, the finish hook
and the rest of Claude Code's loading are in [claude-code.md](claude-code.md). The comparison of
extension layers across harnesses is in [extension-layers.md](extension-layers.md).

All pages were read on 2026-10-03. The maker's documentation was read as raw text. The API
declarations were also read as Claude Code 2.1.288 writes them for a mod; this document calls
that file "the 2.1.288 declarations". Evidence classes are as in [CONVENTIONS.md](../CONVENTIONS.md):
L is the maker's documentation, M is a count or a measured fact, A is one account, O is an own result observed while this document was written.

## 1. What a mod is, and when it shipped

- **A mod is a plugin with a hooks module.** The hooks module is a TypeScript or JavaScript ES
  module that `hooks/hooks.json` names under `modules`. It exports `register(on, options)`. The
  maker calls the product "Claude Mods" and the primitive a "function hook" (L, issue #91870 update
  of 2026-09-09; reference page).
- **Why the maker added it.** The blog post says that settings hooks cannot rewrite events, draw
  new interface or replace features, and that mods can (L, blog, 2026-10-01).
- **Timeline.** The design was published for feedback as issue #91870 on 2026-09-03. On
  2026-09-09 the issue's update said in public that testers may turn it on with
  `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1`. Version 2.1.287 (npm, 2026-10-01) added mods, on by
  default, and ignores that variable at any value. Version 2.1.288 (npm, 2026-10-02) added
  `$.ui.selection()` and fixed at least six defects in mods and plugin hooks modules (L, changelog,
  overview and admin pages; M, npm registry).
- **Channel.** On 2026-10-03 the npm tags were `stable: 2.1.285` and `latest: 2.1.288`. A person on
  the stable channel does not have mods yet (M, npm registry).
- **No plan limit is stated.** The blog says mods are available in the CLI and the desktop app. The
  sources name no plan restriction for mods. The built-in guard (§9) depends on the plan or on
  managed settings, and two built-in mods (`telemetry`, `you-should-know`) depend on analytics being
  on (L, blog, changelog, overview page).
- **Direction.** The maker says it will move more built-in features into mods, so that a person can
  reduce Claude Code to a small core. `/diff` is already a mod that a person can turn off or replace
  (L, blog). The built-in mods `diff`, `agents-md`, `sec-default` and `telemetry` have public source
  in the `mods/` folder of the Claude Code repository (L, mods README).

## 2. The hook model

- **Registration.** `on(event, matcher?, hook)` adds a hook. Each hook has the shape `($, e, next)`:
  `$` is the engine interface, `e` is the event input as frozen plain data, and `next(e)` runs the
  hooks beneath and then Claude Code's own behaviour (L, reference page).
- **Three things a hook can do.** It can observe an event and call `next(e)`. It can rewrite the
  event, by calling `next` with a changed copy. It can answer the event, by returning a result
  without calling `next` (L, overview page).
- **Chain order.** The built-in guard and an organisation's `prependPlugins` mods come first. Then
  come the mods that the person installed, then the organisation's `appendPlugins` mods, then the
  other built-in mods. A mod runs before the mods it lists as `dependencies`. The first mod sees an
  event first and its result last (L, events page).
- **Budgets.** A hook has 10 s of its own time for each event. A `.catch` handler has 1 s. All
  `session.end` hooks share 1.5 s. Time spent waiting on `next` or on a `$` call does not count
  against the hook, but a `$.clock.sleep` does (L, reference page; L, the plugin-authoring
  reference that ships with 2.1.288).
- **Failure.** A hook that fails is skipped and the chain continues, unless its `.catch` handler
  answers. A broken mod never blocks a prompt (L, reference page; O, the 2.1.288 declarations).
- **Runtime.** The module runs in an environment of its own, with no DOM and no Node. Every
  effect outside it goes through `$`. This is isolation of the runtime. It is not a security
  sandbox (§9) (L, tutorial; overview page).

## 3. The events

The groups below follow the reference page, with its group "Prompts and what Claude reads" split
in two. The table leaves out `ui.close` and the events that each `$` method raises (for example
`fs.read`). What each event allows is from the doc comments of the 2.1.288 declarations (O, read
2026-10-03). Each settings-hook event is also hookable as
`classic.<Event>`, for example `classic.Stop` (L, reference page).

| Group | Events | What a mod can do there |
| --- | --- | --- |
| Tools | `tool.call`, `tool.check`, `tool.describe` | Deny, rewrite or answer a tool call; give the permission verdict (`allow`, `deny` or `ask`); rewrite a tool's description or move it behind tool search |
| Prompt | `prompt.submit`, `prompt.fill`, `prompt.edit`, `prompt.suggest` | Rewrite or drop the submitted prompt; put a draft into the prompt box; react to each edit; offer the dim suggestion that Tab accepts |
| System prompt and context | `prompt.compose`, `prompt.section`, `prompt.context`, `prompt.attachment`, `skill.prompt`, `attribution.text` | Add, replace, reorder or drop system-prompt sections; change the context blocks of the first message; drop or rewrite an injected reminder; rewrite a skill's expanded text; rewrite the commit and pull-request attribution text |
| Commands and settings | `command.run`, `command.describe`, `config.set`, `config.describe` | Answer a slash command; hide or describe a command; refuse or clamp a `/config` change; relabel a row |
| Turns | `turn.start`, `turn.step`, `turn.complete` | Observe a turn's start; change the model or effort of each model request, as a stream; show a text under the answer at the end of a turn, with no change to the transcript |
| Session | `session.start`, `session.end`, `session.append`, `session.compact`, `session.measure`, `session.receive`, `session.send`, `session.attach`, `session.detach` | Start work when the session is ready; save on exit; rewrite each row before it is stored and sent; rewrite a compaction's instructions or messages, answer it, or skip it (the reference page lists only skip); receive pushed usage and rate-limit changes; filter deliveries and messages between agents; see a remote client join |
| Subagents | `agent.offer`, `agent.spawn` | Hide an agent type from the model; choose or refuse the model of a subagent |
| Interface | `ui.render`, `ui.resolve`, `ui.press`, `ui.input`, `ui.select`, `ui.message`, `ui.scroll`, `ui.focus` | Draw, wrap or replace a component; restyle the element table; handle presses, typing, picks, scrolling and focus |
| Other mods | `plugin.register`, `engine.create` | Refuse another mod at load; add nouns to `$`, or withhold them, for the mods that load after |
| Telemetry | `telemetry.log`, `telemetry.mark` | Change what a record to the person's OpenTelemetry collector carries; never where it goes |

- **A mod cannot change the permission prompt.** A mod can restyle much of the interface, but not
  the permission prompt, and it cannot change what that prompt shows (L, overview page).
- **System-prompt sections.** `prompt.section` answers `{ text }` or `{ text: null }` for one named
  section. `prompt.compose` answers the whole ordered list. An answer that changes from call to
  call spends the prompt cache on each call (L, reference page; O, the 2.1.288 declarations).

## 4. The engine interface (`$`)

The namespaces are `plugin`, `ui`, `command`, `tool`, `agent`, `model`, `prompt`, `turn`, `session`,
`config`, `settings`, `env`, `fs`, `store`, `state`, `clock`, `http`, `process`, `mcp`, `audio` and
`telemetry` (L, reference page). These are all the nouns of `$` in the 2.1.288 declarations (O). Methods that matter for a mod that reports or
steers work:

- `$.tool.register` adds a tool that the model sees as `mcp__<plugin>__<name>`. The mod answers its
  calls in a `tool.call` hook (L, api page). `$.agent.register` adds an agent type, and
  `$.agent.spawn` runs one (L, plugin-authoring reference).
- `$.command.register` adds a slash command. The mod answers it in a `command.run` hook (L, api page).
- `$.prompt.submit` queues a prompt that starts its own turn once the session is idle.
  `$.prompt.fill` puts text into the prompt box as a draft (L, plugin-authoring reference).
- `$.session.append` adds a row to the conversation: a user-role row that the model reads and the
  person does not see as typed, or a notice that the model never reads. The row carries the mod's
  name as its origin (L, plugin-authoring reference).
- `$.model.complete` runs one completion with no history. `$.model.fork` asks one question with no
  tools over the session's own transcript, so that the API can serve that prefix from its prompt
  cache. Both always resolve to a result with `usage`, and never reject over what the provider did
  (L, plugin-authoring reference).
- `$.ui.ask` asks the person a question with two to four options, drawn as `AskUserQuestion`. It
  rejects in a `claude -p` run, where no one can answer (O, the 2.1.288 declarations).
- `$.session.usage()` gives the session's usage, and `session.measure` pushes a change when a figure
  moves (O, the 2.1.288 declarations).
- `$.process.run` runs a host command by argv. `$.fs` reads, writes, lists and stats paths.
  `$.http.fetch` reaches the network (L, plugin-authoring reference).

## 5. Drawing: sites, elements, surfaces and refresh

- **Sites a mod can draw.** A `Pane` beside the transcript in a wide fullscreen terminal, and
  above the prompt otherwise; the `AbovePrompt` band; a toast (`$.ui.toast`, top right, 4 s by default);
  one line under the prompt per mod (`$.ui.status`, shown after a `⚠` mark and the mod's name); log
  lines in the transcript; and Claude Code's own sites, which a mod can wrap or replace (L,
  reference and api pages). The 2.1.288 declarations name these sites: `AskUserQuestion`,
  `UserMessage`, `AssistantMessage`, `ToolUse`, `ToolResult`, `ToolGroup`, `ToolProgress`,
  `CommandOutput`, `Spinner`, `TurnDuration`, `InfoNotice`, `SessionMode`, `PromptHint`,
  `AbovePrompt` and `Pane` (O).
- **`$.ui.status` is not the `statusLine` setting.** The `statusLine` setting runs a command and
  shows what it prints. `$.ui.status` is a separate line under the prompt. The docs describe no way
  for a mod to add to the `statusLine` output (inference from the api page).
- **When a pane opens.** A pane opened by the person's act (a command, a button) takes its seat at
  any width. A pane opened without a request (from `session.start` or a timer) takes its seat only
  from 144 terminal columns, or 110 after the person has opened that pane once, and waits below
  that (L, interface and reference pages).
- **Surfaces that show a drawing.** Hooks run on every surface that loads the plugin. Only the
  terminal and the Code tab of the desktop app show what a mod draws. The VS Code chat panel,
  `claude -p`, the Agent SDK and cloud sessions run the hooks but show nothing. Under Remote
  Control, from claude.ai or the mobile app, the drawing shows only in the terminal on the
  person's machine. In WSL sessions of the desktop app, mods do not run (L, overview page). The
  2.1.288 declarations already declare element tables for `vscode` and `mobile` in the `Elements`
  type that `$.ui.resolve(e)` reads (O). Inference:
  the maker plans those surfaces, and they do not draw today.
- **Through ACP (Zed and other ACP clients).** The ACP adapter for Claude,
  `agentclientprotocol/claude-agent-acp` (formerly `zed-industries/claude-code-acp`), version 0.85.1,
  is built on `@anthropic-ai/claude-agent-sdk` 0.3.287. It starts each session with the setting
  sources `user`, `project` and `local`, and it logs plugin load failures, which it says have no
  ACP surface (L, the adapter's `package.json` and `src/acp-agent.ts`) [as-of 2026-10-04].
  Inference: installed mods load in an ACP session, their hooks run, and they draw nothing, as
  under the Agent SDK; the ACP client draws only what the protocol carries. Not observed in a
  running session.
- **Elements differ by surface.** `Svg` draws on the desktop only. `Raster` and `Image` draw in the
  terminal only. A mod builds its tree from the table that `$.ui.resolve(e)` returns for the surface
  (L, reference page).
- **Redraw rate.** Redraws are throttled to 10 per second, and to 30 per second in the terminal for
  the visible pane, the expanded band and the hint line under the prompt (L, reference page). A write to `$.state` redraws exactly the drawings that read that
  value. A change of width redraws every site once the resize settles (L, plugin-authoring
  reference).
- **Frame-rate drawing.** Three elements draw faster than a render pass. A `Client` runs a surface
  module of the mod with its own local state, a frame clock (`every(ms, fn)`), pointer and key
  listeners, and a `post` channel back to the hooks module. It is on the terminal and the desktop
  only. A `Raster` is a grid of coloured cells that `$.ui.blit` repaints without a render pass. An
  `Image` shows a picture through the kitty graphics protocol where the terminal has it, and the
  pixels never pass through `$` (O, the 2.1.288 declarations; L, plugin-authoring reference).
- **Guards.** A `Client` that calls `setState` on three renders in a row, with no input or tick
  between them, is a render loop and is unmounted (O, the 2.1.288 declarations). A tree that does
  not validate is not drawn: the engine draws its own, and says why in the debug log (L,
  plugin-authoring reference).

## 6. State, timers and work that outlives one event

- **Three lifetimes.** A module variable lasts until the next reload. `$.state` lasts for the
  session, survives a reload, redraws its readers, and is declared in a `PluginState` type
  contract. `$.store` is shared by every session on the machine, up to 4 MiB of JSON (L, interface
  and reference pages).
- **Background work.** Work that must outlive one event starts in `session.start`, which is awaited
  before the first prompt. `$.clock.every` and `$.clock.after` keep it going until it is cancelled
  or the module reloads (L, plugin-authoring reference).
- **Writes.** A render hook never writes `$.state`. A handler writes it with a version check, so two
  presses before a redraw both land (L, plugin-authoring reference).

## 7. Extending the engine for other mods

- **New nouns.** A mod can add a noun to `$` in an `engine.create` step, for example `$.topo`, and
  ship its types as a contract file named in `plugin.json` under `types`. A mod that depends on it
  lists it under `dependencies`, and the engine puts that contract beside the dependent mod. A step
  may add nouns and withhold nouns, but may not replace a noun that another step added (L,
  plugin-authoring reference; O, the 2.1.288 declarations).
- **Admission.** A `plugin.register` hook can refuse another hooks module at load, by its tier and by
  the nouns it uses (O, the 2.1.288 declarations).
- **Static reading.** `claude plugin validate` lists the events a mod hooks and the `$` methods it
  calls. Claude Code refuses to load a mod whose use of `$` this reading cannot follow (L, admin and
  reference pages).

## 8. Relation to settings hooks and plugins

- **Settings hooks stay.** The docs now call the older hooks "settings hooks": a shell command, an
  HTTP request or a prompt on a lifecycle event. They are not deprecated, and they run beside mods
  (L, overview and admin pages; hooks page).
- **Order with `PreToolUse`.** `PreToolUse` hooks from managed settings run before the first mod,
  and their block is final. If a mod rewrites a call, the managed hooks run again on the new call.
  Other `PreToolUse` hooks, from settings files and plugins, run after the last mod calls `next`. A
  mod that answers `tool.call` itself stops them from running (L, events and admin pages).
- **A mod is a plugin.** The same plugin can carry skills, agents, MCP servers and settings hooks.
  It is installed and shared like any plugin: a marketplace, `/plugin install`, or the maker's
  directory. `disableAllHooks` and `allowManagedModsOnly` stop the mod and leave the plugin's
  skills, commands, agents and MCP servers loaded (L, overview, create and reference pages).

## 9. Trust, consent and organisation control

- **Not sandboxed.** A mod runs with the person's permissions. It can read and write files, start
  processes outside the Bash sandbox, reach the network, read environment variables and settings
  (API keys included), see and rewrite every prompt and tool call, approve a tool call before the
  person is asked, and spend model usage (L, overview page).
- **Consent.** No mod loads in a directory before the person answers the workspace trust prompt.
  A mod that Claude writes in a session goes in `~/.claude/dev-mods/<session-id>/`, and Claude Code
  asks once whether to turn on hot reloading for that session. Such a mod does not load under
  `claude -p` or `dontAsk`, where no one can answer. That folder is deleted after `cleanupPeriodDays`
  (L, create and admin pages).
- **Turning mods off.** A person can disable one plugin in `/plugin`, start one session with
  `--safe-mode`, or set `disableAllHooks`. None of these stops the built-in mods. The maker can turn
  installed mods off remotely, and no local setting turns them back on (L, overview and
  troubleshoot pages).
- **The built-in guard.** `sec-default@builtin` loads first on a machine with managed settings, or
  for a person signed in with a Team or Enterprise plan. Where it loads, it keeps other mods away
  from managed hooks, managed instructions, the system prompt, settings reads and managed MCP tools,
  and it makes `deny` rules final (L, admin page). Inference: where it does not load, an installed
  mod can rewrite system-prompt sections and approve a call that a `deny` rule refuses.
- **Gaps that remain with the guard.** A mod can still approve a call that an `ask` rule or a
  non-managed `PreToolUse` hook would stop. In auto mode, a call that a mod approves skips the
  classifier. Deny rules do not apply to a mod's own `$.fs` and `$.process` calls. Network policy
  covers `$.http.fetch` but not a program started with `$.process.run` (L, admin page).
- **Organisation settings.** Managed settings offer `allowManagedModsOnly`,
  `allowModsToOverrideDenyRules`, `prependPlugins`, `appendPlugins`, `allowManagedHooksOnly`,
  `disableAllHooks`, `disableSideloadFlags` and the marketplace allowlists. An organisation can also
  enforce its policy through a mod of its own (L, reference and admin pages).
- **An outside account.** A security company's account of the early-access period names four
  gaps: silent reads of credentials, capability disclosure only by a manual command, spoofed
  interface, and code fetched after review. It was read through a summarising fetch, not line by
  line (A, Pluto Security, 2026-09-22).

## 10. Building and checking a mod

- `claude plugin validate <dir>` reads the manifest and the module as the engine will, lists hooks
  and calls, and has `--strict` and `--json`. `claude plugin test` runs a mod's `*.test.ts` files
  against the engine, with no session and no network; a test can mount a component on a named
  surface and act on it by key. `claude --plugin-dir <dir>` loads a folder for one session and
  reloads it on save. `CLAUDE_CODE_PLUGIN_DIRS` names such folders where no flag can be given (L,
  reference and test pages).
- Claude Code writes the API's `.d.ts` files beside a mod at each load. The docs tell authors to
  trust those files over any page (L, create page).

## 11. Stability

- No versioning or compatibility promise was found. The docs say events and methods can change
  between releases, and tell an author to say in the README which Claude Code version they tested
  with (L, create page). The reference page describes the API as of 2.1.287 (L).
- The repository's `mods/README.md` and the 2.1.288 declarations still say early access, and that
  the surface may change between releases without notice (L; O).
- Before the launch, the maker expected fewer breaking changes than in the first week of testing
  (L, issue #91870 update of 2026-09-09).

## Limits and open questions

- One day's reading, two days after the launch. The issue's 242 comments, its architecture PDF and
  its demo videos were not read. No post on X was read (the site returned HTTP 402).
- Nothing here was run as a mod. The facts marked O are from the declarations that 2.1.288 writes,
  not from a running mod.
- Open: when `vscode` and `mobile` start to draw; whether a mod's hooks run in an ACP session as
  inferred in §5, and whether its dialogs (`$.ui.ask`) reach the ACP client; whether the stable channel takes 2.1.287 or later
  unchanged; whether a versioning promise follows; whether `$.ui.status` and the `statusLine`
  setting merge.
- Re-read this document when any of those changes, and by 2026-11-02.

## Sources

- Blog post "Customize Claude Code with mods in TypeScript", 2026-10-01
  <https://claude.com/blog/claude-code-mods>; tutorial, 2026-10-01
  <https://claude.dev/blog/getting-started-with-claude-code-mods/> (read 2026-10-03).
- Documentation, read 2026-10-03 as raw text: overview
  <https://code.claude.com/docs/en/plugins/mods/overview>, create
  <https://code.claude.com/docs/en/plugins/mods/create>, reference
  <https://code.claude.com/docs/en/plugins/mods/reference>, interface
  <https://code.claude.com/docs/en/plugins/mods/interface>, events
  <https://code.claude.com/docs/en/plugins/mods/events>, api
  <https://code.claude.com/docs/en/plugins/mods/api>, admin
  <https://code.claude.com/docs/en/plugins/mods/admin>, test
  <https://code.claude.com/docs/en/plugins/mods/test>, troubleshoot
  <https://code.claude.com/docs/en/plugins/mods/troubleshoot>; settings hooks
  <https://code.claude.com/docs/en/hooks>.
- Issue "Mods - make Claude 10x more extensible", opened 2026-09-03
  <https://github.com/anthropics/claude-code/issues/91870>; changelog
  <https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md>; built-in mods
  <https://github.com/anthropics/claude-code/blob/main/mods/README.md>; sample mods
  <https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods>; npm registry
  <https://registry.npmjs.org/@anthropic-ai/claude-code> (all read 2026-10-03).
- ACP adapter for Claude <https://github.com/agentclientprotocol/claude-agent-acp>: `package.json`
  and `src/acp-agent.ts` on `main`, read through the GitHub API on 2026-10-04.
- The declarations (`claude-code.d.ts`) and the plugin-authoring skill's reference, as Claude Code
  2.1.288 writes them on the reader's machine (read 2026-10-03).
- Pluto Security, "Claude Code function hooks security", 2026-09-22
  <https://pluto.security/blog/claude-code-function-hooks-security/> (read 2026-10-03 through a
  summarising fetch).
