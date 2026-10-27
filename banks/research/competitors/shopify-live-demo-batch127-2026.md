# Shopify deep screen research — Batch 127

**Date:** 2026-10-27  
**Goal:** Complete collection, product and cart coverage after the 127-home pass.

## Final combined coverage

| Screen | Covered |
|---|---:|
| Home | 127/127 |
| Collection | 127/127 |
| Product | 127/127 |
| Cart | 127/127 |

The previous pending counters reflected indexed HTML only. The matrix now reconciles those documents with rendered browser evidence. Evidence contains 443 read-only rendered pages across 127 browser observation records ({"home":104,"collection":105,"product":107,"cart":127} by page kind).

## Newly inspected gaps

- Collections: Wonder:Petit (three-item product listing), Eurus:Arise (availability/price/form/diet facets), Release:Serenity (12-item Best Sellers with filters/sort), Spotlight:Spotlight (basic Products listing).
- Product pages: Symmetry (color/size options and sold-out state), Eurus:Whiff (discounted anklet detail with title/description mismatch), Release:Serenity (bag color variants/stock), Release:Forest (lamp color options all unavailable).
- Carts: 27 previously missing carts were inspected. Empty-cart recommendations, Continue Shopping links, locale and policy links vary; Release:Serenity's View All link points to `false`.

## Remaining validation

No filters, sorting, variant selection, quantity, add-to-cart or checkout controls were exercised. No mobile viewports, screenshots, Theme Editor or Lighthouse/performance tests were run. These checks remain open.

Updated evidence, matrix, demo audit, design observations, plan, progress and handoff on `research/shopify-live-demo-batch6`.
