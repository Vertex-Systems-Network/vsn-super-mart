# Shopify targeted interaction review — Batch 136

**Date:** 2026-10-27  
**Branch:** `research/shopify-live-demo-batch6`  
**Scope:** one read-only product variant interaction on Impulse:Terrain at a normal browser viewport (1363×936 CSS px).

## Observation

| Preset | Flow | Observed response |
|---|---|---|
| [Impulse:Terrain](https://impulse-theme-sports.myshopify.com/products/2016-carbine-expert-build) | Selected size M on the 2016 Carbine Expert Build PDP | M became selected, S deselected, and the URL updated with variant ID `7839884836925`. “In stock, ready to ship” remained unchanged. No add-to-cart action followed. |

## Completion status

- This batch adds **1 interaction observation**.
- Overall targeted sample: **8 observations across 6 of 127 selected presets**.
- Mobile visual review remains **127/127** at 360×640 CSS px.
- **121 presets** remain without targeted interaction checks. Completed presets are excluded from the pending count.
- Checkout, Theme Editor, keyboard/accessibility and Lighthouse checks remain open.

## Design implication

Keep the selected variant visible and reflect it in the URL. Update inventory feedback only when the selected variant changes availability.

Per-preset evidence and synthesis are in `shopify-live-demo-evidence-2026.json`, `shopify-127-completion-matrix-2026.json`, `banks/design/competitor-observations.json` and `cross-platform-patterns.json`.
