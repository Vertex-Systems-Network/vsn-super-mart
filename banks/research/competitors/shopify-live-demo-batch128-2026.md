# Shopify validation checkpoint — Batch 128

**Date:** 2026-10-27  
**Preset:** Ignite:Peak  
**Scope:** Mobile preview and one safe homepage CTA interaction attempt.

## Verified

- Opened the official Shopify Theme Store listing preview in Mobile mode.
- Measured the embedded live storefront at **360×640 CSS px**.
- Captured a screenshot in the browser session; the image was not saved as a repository artifact.
- Tapped the homepage **Shop now** CTA. The storefront displayed a **21+ age-verification** prompt.
- Left the age prompt unanswered. No age was attested, product was not added, and checkout was not entered.

## Coverage status

Home, collection, product and cart page coverage stays **127/127 each** across combined indexed HTML and browser-rendered sources. The mobile and CTA results are one sample preset, not cohort-wide validation. Rendered evidence now totals 444 pages across 127 preset records (including the mobile viewport capture).

## Still open

- Shopper controls: collection filters/sort, product variants, quick view and keyboard behavior; cohort-wide coverage remains untested.
- Theme Editor: no merchant store/editor session was available.
- Checkout: no checkout-flow inspection was made.
- Lighthouse/performance: no Lighthouse runner or result was available in the research environment.

## Files updated

Evidence JSON, completion matrix, live-demo plan, demo audit, progress state and handoff notes on branch `research/shopify-live-demo-batch6`.
