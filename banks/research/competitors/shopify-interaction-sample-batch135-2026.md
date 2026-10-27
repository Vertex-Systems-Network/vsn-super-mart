# Shopify targeted interaction review — Batch 135

**Date:** 2026-10-27  
**Branch:** `research/shopify-live-demo-batch6`  
**Scope:** one read-only product variant interaction on Impulse:Dune at a normal browser viewport (1363×936 CSS px).

## Observation

| Preset | Flow | Observed response |
|---|---|---|
| [Impulse:Dune](https://impulse-theme-apparel.myshopify.com/products/naked-famous-crewneck-heavyweight-terry-black) | Selected size M on the Naked & Famous Crewneck PDP | M became selected, S deselected, and the URL updated with variant ID `30237988749383`. “In stock, ready to ship” remained unchanged. No add-to-cart action followed. |

## Completion status

- This batch adds **1 interaction observation**.
- Overall targeted sample: **7 observations across 5 of 127 selected presets**.
- Mobile visual review remains **127/127** at 360×640 CSS px.
- **122 presets** remain without targeted interaction checks. Completed presets are marked in the matrix and excluded from the pending count.
- Checkout, Theme Editor, keyboard/accessibility and Lighthouse checks remain open.

## Design implication

Keep the selected variant visible and reflect it in the URL. Recalculate inventory messaging when availability changes; avoid changing stable stock copy when the selected variant remains in stock.

Per-preset evidence and synthesis are in `shopify-live-demo-evidence-2026.json`, `shopify-127-completion-matrix-2026.json`, `banks/design/competitor-observations.json` and `cross-platform-patterns.json`.
