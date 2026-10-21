# VSN Super Mart — multi-niche Shopify theme (AI-native)

A Shopify theme built to compete with the top themes (Prestige, Impulse, Symmetry, Trademark, Horizon family),
shipping one codebase with a distinct preset per niche.

**AI agents and new developers: start with [`AGENTS.md`](AGENTS.md).**

## Quick start
```bash
python3 scripts/vsn.py status      # where the project stopped + next action
python3 scripts/vsn.py validate    # check all banks
```

## How it works
1. **Ask the niche** → 2. **Research bank** → 3. **Options bank** → 4. **Design search** (unique direction,
checked against the **design bank**) → 5. **Design spec** (100% option coverage) → 6. **Figma build** →
7. **Development** → 8. **QA** → 9. **Release preset** → next niche.

Details: [`ai/WORKFLOW.md`](ai/WORKFLOW.md).

| Folder | What |
|---|---|
| `banks/research` | Theme Store rules, competitors, per-niche research |
| `banks/options` | Every option for shoppers, merchants and developers |
| `banks/design` | Design fingerprints, competitor patterns, registry of VSN designs, specs |
| `ai/` | Workflow, state (resume point), prompts, templates |
| `theme/` | Shopify theme source (created in Stage 7 from Skeleton theme) |

Design: Figma file `BxJuIRth8k4cCUbFnPV6ek`, page "VSN | Super Mart".

## Current status (2026-10-22 — paused)
- Gen-Z preset **Afterhours**: 24 screens designed and QA'd in Figma (Stage 6), waiting for Full HD images and approval.
- **Element library** (rule 15): 192 elements catalogued in `banks/elements/` — Elementor + addons + Gutenberg + Shopify + creative, smart responsive (2448–320).
- **Theme prototype** in `theme/`: tokens, element defaults, smart responsive, 5 elements, global components (Theme Check clean).
- Next steps: `ai/state/HANDOFF.md` → "Open items".
