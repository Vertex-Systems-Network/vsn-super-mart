# CLAUDE.md

Read and follow **`AGENTS.md`** first — it is the source of truth for every agent.

## Claude-specific

- Start every session with `/vsn-resume` (or run `python3 scripts/vsn.py status`).
- Slash commands (in `.claude/commands/`):
  - `/vsn-resume` — load state + handoff and continue the next action
  - `/vsn-status` — show stage, niche, gates and next action
  - `/vsn-niche` — start a new niche cycle (asks the niche, creates the brief)
  - `/vsn-research` — fill the research bank for the current niche
  - `/vsn-options` — map options for the niche from the options bank
  - `/vsn-design` — create a unique design spec, check it, then build it in Figma
  - `/vsn-develop` — build the approved design into the theme, work unit by work unit
  - `/vsn-handoff` — write the session handoff before stopping
- Figma: use the Figma MCP. Load the `figma-use` skill before `use_figma`, and
  `figma-design-to-code` before `get_design_context`. Target page: "VSN | Super Mart" (`25:2`)
  in file `BxJuIRth8k4cCUbFnPV6ek`.
- Use subagents for parallel niche research; keep the main thread for decisions and bank writes.
- Never mark a stage done unless `python3 scripts/vsn.py advance` passes.
