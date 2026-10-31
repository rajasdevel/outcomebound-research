---
last_checked: 2026-10-19
volatility: VOLATILE (cloud surfaces are in preview or change monthly; limits, defaults and file names move between releases)
sources:
  - https://github.com/anthropics/claude-code/releases/tag/v2.1.314 (read 2026-10-31)
  - https://github.com/anthropics/claude-code/releases/tag/v2.1.316 (read 2026-10-31)
  - https://code.claude.com/docs/en/claude-code-on-the-web
  - https://code.claude.com/docs/en/cloud-environments
  - https://learn.chatgpt.com/docs/environments/cloud-environment
  - https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment
  - https://cursor.com/docs/cloud-agent/setup
---

# Cloud agent sessions: what runs, what loads, what leaves

Four coding harnesses run a session on a vendor's machine instead of the person's: Claude Code
(cloud sessions), Codex (cloud tasks), the GitHub Copilot cloud agent and Cursor (cloud agents).
This page records, for each, how setup steps run, what network the session has, and how work
leaves. Every claim is L (the vendor's documentation) and was read on 2026-10-19 unless it
carries another date. "Silent" means the page read does not say; it does not mean the feature is
absent. Other cloud surfaces were not read.

## 1. Claude Code (cloud sessions)

Source: the [cloud-sessions page](https://code.claude.com/docs/en/claude-code-on-the-web) and the
[cloud-environments page](https://code.claude.com/docs/en/cloud-environments). The prose below is
a paraphrase of both.

- **Start and platform.** A session runs in a fresh Ubuntu 24.04 x86_64 VM with the repository
  cloned and common toolchains installed. It starts from the browser, the phone app, the desktop
  app, `claude --cloud` or a routine. `--cloud` and `--teleport` need a claude.ai sign-in; they
  are not available when Claude Code is set up for Amazon Bedrock, Google Cloud's Agent Platform
  or another third-party provider. The session counts toward the plan's usage limits, with no
  separate charge for the VM.
- **Setup script.** An environment's setup script runs once, as root, before Claude starts. When
  it finishes in roughly five minutes, the filesystem is snapshotted and later sessions start from
  the snapshot; a script that overruns is not cached. The script runs again when it or the allowed
  hosts change, and when the cache expires after roughly seven days. The snapshot keeps files, not
  running processes.
- **Repository hook.** A `SessionStart` hook in the repository's `.claude/settings.json` runs on
  every start and resume, with no cache. The variable `CLAUDE_CODE_REMOTE` is `true` in the cloud
  and never locally, which is how a hook runs only there. Repository hooks load only when the
  session has one repository.
- **Network.** Four levels: None, Trusted (the default), Full, Custom. Trusted allows a listed set
  of domains; the list includes `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org`,
  `index.crates.io`, `proxy.golang.org` and GitHub. With None, package installs fail. Even with
  None, Claude Code can reach the Anthropic API.
- **Instructions and user-level files.** The user's settings file (`~/.claude/settings.json`) and
  user-level hooks stay on the person's machine and do not reach the VM. The page says hooks from a
  user-level settings file are not expected in the cloud.
- **Commands.** `/compact` and `/context` work; `/clear` and terminal-only commands such as
  `/plugin` and `/resume` do not. Subagents in the repository's `.claude/agents/` are picked up.
  Agent teams are off unless `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is set.
- **Secrets and credentials.** Git credentials stay outside the VM; a proxy attaches them. Keys
  added as network secrets are attached to matching requests outside the sandbox. Ordinary
  environment variables are set per environment.
- **How work leaves.** Changes are pushed as a branch to GitHub; the diff view and "Create PR" are in
  the web UI. A repository with no GitHub remote, or a GitHub repository without the Claude GitHub
  App, is uploaded as a bundle: history and uncommitted changes to tracked files go up,
  untracked files do not, the bundle must be under 100 MB, and the session can push back only
  where the GitHub connection allows it. A non-GitHub repository can be sent as a bundle with
  `CCR_FORCE_BUNDLE=1` but cannot push back to that remote.
- **Lifetime.** A session stops after a period of inactivity and its VM is reclaimed. Reopening it
  restores the conversation, not background processes. A question Claude asks can be answered
  later, until the environment expires.
- **`--teleport`.** Pulls a cloud session and its pushed branch into a local checkout of the same
  repository. The local copy then diverges: new work there does not appear in the cloud session.
  Requires a clean working tree and the same account.
- **Follow-up from a script.** `claude -p "<message>" --cloud <session-id>` queues a message into
  a running cloud session and exits without waiting; `--output-format json` returns
  `{ok, session_id, url}`.
- **Release changes in 2.1.314 and 2.1.316 [as-of 2026-10-31].** These are release notes (L), not
  a runtime check.
  - *Setup script failure.* From 2.1.314, cloud sessions started from the web, desktop and mobile
    apps start even when the setup script exits with an error, instead of failing to start. The
    cloud-environments page, read 2026-10-31, still says a non-zero exit makes the session fail to
    start and advises `|| true` on non-critical commands. Page and note disagree, and the note does
    not cover `claude --cloud` or routines, so a setup step that must hold needs its own check in
    the session, such as a `SessionStart` hook (inference).
  - *Plugins in scheduled tasks.* Scheduled-task runs in Anthropic's cloud now load the plugins
    enabled on the person's claude.ai account (2.1.314). Their skills, hooks and MCP servers can
    therefore reach such a run (inference; the note names plugins only).
  - *Network secrets and auto mode (2.1.316).* Enterprise members can now add and delete network
    secrets on their own cloud environments, not only view them. Cloud sessions and cloud scheduled
    tasks are now marked as failed when auto mode stopped a turn because the server returned no
    safety verdict.

## 2. Codex (cloud tasks)

Source: the [cloud environment page](https://learn.chatgpt.com/docs/environments/cloud-environment).
The page is labelled legacy, so a newer guide may replace it.

- **Instructions.** If the repository has an `AGENTS.md`, the agent uses it to find lint and test
  commands. Skills, user-level files and hooks in a cloud task: silent.
- **Setup.** A setup script runs with internet access, in a Bash session separate from the agent;
  an `export` in it does not reach the agent, so variables go in `~/.bashrc` or the environment
  settings. An optional maintenance script runs when a cached container resumes. The default
  image is `universal`. Automatic setup covers pip, pipenv, poetry, npm, yarn and pnpm.
- **Cache.** Container state is cached for up to 12 hours. A change to the setup script, the
  maintenance script, the environment variables or the secrets invalidates it; "Reset cache"
  forces a rebuild. On Business and Enterprise the cache is shared by the environment's users.
- **Secrets.** Available to setup scripts only; removed before the agent phase starts.
- **Network.** Off in the agent phase by default; limited or unrestricted access can be set.
  Outbound traffic goes through an HTTP/HTTPS proxy.
- **How work leaves.** The agent shows its answer and a diff; the person can then open a pull
  request or ask a follow-up. Whether Codex pushes a branch itself: silent.

## 3. GitHub Copilot cloud agent

Source: the [environment customisation page](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment).

- **Setup.** The file is `.github/workflows/copilot-setup-steps.yml`. Its job must be named
  `copilot-setup-steps`, and the file must be on the default branch before the workflow is used.
  Only the job keys `steps`, `permissions`, `runs-on`, `services`, `snapshot` and
  `timeout-minutes` are honoured; others are ignored. The maximum timeout is 59 minutes.
- **Runners.** The default is a GitHub-hosted Ubuntu runner. Larger hosted runners and
  self-hosted runners (selected by an ARC scale set name) are possible; for a self-hosted runner
  the page recommends ephemeral, single-use runners and says the integrated firewall must be off.
  Ubuntu x64 and Windows 64-bit are supported; macOS is not.
- **Variables.** The page names proxy and certificate settings (`https_proxy`, `http_proxy`,
  `no_proxy`, `ssl_cert_file`, `node_extra_ca_certs`) as settable through Copilot agent variables
  or secrets, or on the runner. A general secret mechanism for the agent: silent on this page.

## 4. Cursor cloud agents

Source: the [setup page](https://cursor.com/docs/cloud-agent/setup).

- **Instructions.** Cloud agents read `AGENTS.md`; the page advises a section for cloud-only
  setup and tests.
- **Environment file.** `.cursor/environment.json` is read only when the saved environment's
  "environment.json location" points to it (new environments default to None). A single-repository
  run can fall back to the repository's file when no saved environment matches. Self-hosted
  machines never read it. Keys: `build` (`dockerfile`, `context`), `install` (from the project
  root), `start`, `terminals` (a shared tmux session) and `snapshot` (a dashboard id).
- **Builds.** Builds use the default branch's configuration. Only disk state persists between runs,
  not processes, exported variables or memory. `install` must be idempotent, since it can run on
  prepared disk state. A failed build does not replace the active one.
- **Secrets.** Set in the dashboard Secrets tab and exposed as environment variables;
  environment-scoped secrets never reach self-hosted machines.
- **Network.** The page names a "Cloud Agent network allowlist" for restricted egress and does not
  say how to configure it or what the default is.

## Limits

- Pages were read through a fetch tool that summarises. Re-read the source before relying on a
  value.
- Not read, so not recorded: Google Jules, the Codex and Copilot skills and hooks behaviour in the
  cloud, the Copilot firewall, how any cloud interface renders diagrams or links.

Sources for sections dated 2026-10-31 (L, vendor release notes and documentation; runtime behavior
not tested):

- <https://github.com/anthropics/claude-code/releases/tag/v2.1.314> (published 2026-10-30), read
  2026-10-31.
- <https://github.com/anthropics/claude-code/releases/tag/v2.1.316> (published 2026-10-31), read
  2026-10-31.
- <https://code.claude.com/docs/en/cloud-environments> (setup script exit rule), read 2026-10-31.
