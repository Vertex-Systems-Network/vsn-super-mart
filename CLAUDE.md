# CLAUDE.md

**Read and follow `AGENTS.md` first** — the authoritative project rules. Load `ai/state/progress.json`, `ai/state/HANDOFF.md` and `ai/WORKFLOW.md` before working.

## Resume instructions

- Start by running `python3 scripts/vsn.py status` (or `/vsn-resume`).
- **Current state (2026-10-25): Stage 2 Research, no active Figma file.** Old Afterhours designs, including Figma key `y5e3fEpx2eAFhLRFLisP0o` and page `25:2`, are superseded **historical references only**. Do not edit, restore or treat them as approved current designs.
- Source-backed research, options and element architecture are the immediate workstream. Record official theme listings, indexed demo HTML, browser-rendered observations and executed interactions at distinct evidence levels.
- Only after Stage 4/5 are approved should the team create a **new** Figma design. Use the Figma MCP with its required skills when a new file is approved and available.
- Generate original images using **ChatGPT image generation**, never Figma AI credits. Upload generated image assets to the newly approved design only; log prompts, dimensions, placements and actual upload outcomes in `banks/design/image-log.json`.
- Do not start theme development before design approval, or claim merchant editor, checkout, mobile or accessibility verification based solely on public HTML.

## Commands

- `/vsn-resume` — read current stage and handoff
- `/vsn-status` — inspect stage and gate status
- `/vsn-niche` — start next niche intake
- `/vsn-research` — source-backed research bank
- `/vsn-options` — map research to merchant/shopper/developer controls
- `/vsn-design` — begin *new* design search only after stages 2–3
- `/vsn-develop` — implement only approved designs
- `/vsn-handoff` — log findings, blockers and next steps

Never mark a stage complete unless `python3 scripts/vsn.py advance` passes.
