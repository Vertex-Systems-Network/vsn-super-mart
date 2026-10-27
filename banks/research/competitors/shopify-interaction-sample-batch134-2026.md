# Shopify targeted interaction review — Batch 134

**Date:** 2026-10-27  
**Branch:** `research/shopify-live-demo-batch6`  
**Scope:** one read-only interaction on the Impulse:Impulse public storefront at a normal browser viewport (1363×936 CSS px). This is not a mobile-emulated test.

## Observation

| Preset | Flow | Observed response |
|---|---|---|
| [Impulse:Impulse](https://impulse-theme-fashion.myshopify.com/collections/2026-the-linen-edit/products/the-lido-short) | On The Lido Short PDP, opened Quick View on the related-product rail | A modal opened for The Vela Shirt without leaving the original PDP. It exposed imagery, compare-at and sale price, description, size-chart access, stock state and DESCRIPTION / MATERIALS & CARE accordions. No add-to-cart action was taken. |

## Completion status

- This batch adds **1 interaction observation**.
- Overall targeted interaction sample: **6 observations across 4 of 127 selected presets**.
- Mobile visual review remains **127/127** at 360×640 CSS px.
- **123 presets** remain without targeted interaction checks.
- Checkout, Theme Editor, keyboard/accessibility and Lighthouse checks remain open.

## Design implication

A related-product Quick View can keep shoppers on their current PDP while showing useful decision details. Preserve a clear close path and do not present modal exposure as a cart action.

Per-preset interaction records and synthesis are in `shopify-live-demo-evidence-2026.json`, `shopify-127-completion-matrix-2026.json`, `banks/design/competitor-observations.json` and `cross-platform-patterns.json`.
