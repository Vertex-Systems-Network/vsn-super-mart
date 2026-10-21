# AGENTS.md — VSN Super Mart (AI-native Shopify theme)

This file is the **single entry point for any AI agent** (Claude, Codex, Gemini, Cursor, Copilot…) or human
working on this repository. Read it fully before doing anything.

## 1. What we are building

**VSN Super Mart** — a multi-niche Shopify theme (Online Store 2.0, theme blocks) that competes with the
best themes on the market (Prestige, Impulse, Symmetry, Trademark, Broadcast, Horizon family…).

- One codebase, many **presets** (one per niche), each a visually distinct style with its own demo store.
- Every option a **Shopper**, **Merchant (user)** and **Developer** needs (see `banks/options/`).
- Built from **Shopify Skeleton theme or original code only** — never Dawn or Horizon
  (Theme Store rule, see `banks/research/platform/theme-store-requirements.json`).
- Design lives in Figma: file `BxJuIRth8k4cCUbFnPV6ek`, page **"VSN | Super Mart"** (node `25:2`).
  Brand colors: Teal `#5BC8D6`, Blue `#5F8CC4`, Purple `#615BA8`, Ink `#17251B`.

## 2. Read order (every session)

1. `AGENTS.md` (this file)
2. `ai/state/progress.json` — **where the project stopped** (current stage, niche, next action)
3. `ai/state/HANDOFF.md` — last session's notes, open questions, blockers
4. `ai/WORKFLOW.md` — the stage you are in, its inputs, outputs and exit gate
5. The banks the current stage needs (`banks/research`, `banks/options`, `banks/design`)

Then run: `python3 scripts/vsn.py status` — it prints the stage and the exact next action.

## 3. Resume protocol (pick up exactly where it stopped)

1. Run `python3 scripts/vsn.py status`.
2. Do **only** the `next_action` it prints, inside the current stage.
3. When a step finishes, record it: `python3 scripts/vsn.py log "<what you did>"`.
4. When a stage's exit gate passes, advance: `python3 scripts/vsn.py advance` (it runs the gate check).
5. Before ending a session — even mid-task — update `ai/state/HANDOFF.md`
   (done / in progress / next / blockers) and commit. A session that ends without a handoff is a bug.

Never skip stages. Never start development before the design gate passes.

## 4. Golden rules

1. **Banks first.** Research, options and design decisions are read from and written to the banks.
   Nothing is designed from memory alone. Every new finding is added to the bank with a source.
2. **Ask the niche first.** A design/development cycle always starts by asking (or reading) the target niche.
3. **No repeated design.** Every new design gets a fingerprint in `banks/design/registry.json`.
   `python3 scripts/vsn.py check-design <spec>` must pass (not too similar to any previous VSN design
   or any competitor fingerprint) before the design is accepted.
4. **Full coverage.** Every `must` option for the niche (and every Theme Store requirement) must be
   present in the design spec. `python3 scripts/vsn.py coverage <spec>` must pass.
5. **Theme Store compliance.** No fake urgency/countdowns/stock counters/viewer counts, no app-like
   features (wishlist, booking, Instagram feed) inside the Theme Store build. Such features are tagged
   `store_allowed: false` in the options bank and go only into an optional "VSN apps/extras" track.
6. **Small, verifiable steps.** One work unit per commit. Run `shopify theme check` once theme code exists.
7. **Evidence.** Claims about competitors or the market need a URL in the bank's `sources`.
8. **Language.** Code, file names and bank data in English. Chat with the team may be Urdu/Roman Urdu.

## 5. Repository map

```
AGENTS.md                 ← you are here (all AIs)
CLAUDE.md                 ← Claude-specific pointer + commands
ai/
  WORKFLOW.md             ← stages 0–9, inputs/outputs/gates
  state/progress.json     ← machine-readable project state (resume point)
  state/HANDOFF.md        ← human-readable session handoff
  state/log.md            ← append-only activity log
  prompts/                ← ready prompts for each stage (any AI)
  templates/              ← niche brief, design spec, research entry
banks/
  research/               ← RESEARCH BANK: platform rules, competitors, per-niche research
  options/                ← OPTIONS BANK: every feature/option (shopper, merchant, developer)
  design/                 ← DESIGN BANK: design registry, fingerprints, competitor patterns, specs
scripts/vsn.py            ← status / advance / log / validate / coverage / check-design / new-niche
theme/                    ← Shopify theme source (created in stage 7 from Skeleton theme)
.claude/commands/         ← slash commands for Claude Code
```
