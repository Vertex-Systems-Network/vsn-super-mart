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

Design: Figma file `y5e3fEpx2eAFhLRFLisP0o`, page "AFTERHOURS — Restored UI". Source-backed 24-screen editable restoration; original photos missing.

**Popular Shopify theme research, PR #2:** [47 family listings](banks/research/competitors/shopify-families-2026.json), [127 individually opened official listing design/preset records](banks/research/competitors/shopify-presets-2026.json) and [research report](banks/research/competitors/shopify-research-report.md). Real live-store interactions are not yet verified; this is source-backed catalog research.

## Current status (2026-10-25)

- **PR #1 research cohort:** 55 individually referenced theme/preset/demo entries, 14 evidence-linked patterns, 16 qualitative design observations and 20 Shopify capability route decisions. See [research closeout](banks/research/competitors/research-closeout.md) and [implementation matrix](banks/research/competitors/shopify-implementation-matrix.json).
- **Afterhours Figma:** 24 editable layout frames restored (19 desktop / 5 mobile) in [this file](https://www.figma.com/design/y5e3fEpx2eAFhLRFLisP0o/VSN-Super-Mart?node-id=0-1). Generated images still require upload and full visual QA; Stage 6 design approval is **pending**.
- **Core theme:** 192 elements catalogued, 5 core new specs ready; prototype blocks in `theme/` are not release-ready and have not been tested in a live Shopify development store.
- The research/AI workflow PR can be merged as infrastructure. It does **not** indicate Stage 7 theme development or Store release approval.
- Run `python3 scripts/competitor_audit.py validate` and `python3 scripts/vsn.py validate` before changes.
