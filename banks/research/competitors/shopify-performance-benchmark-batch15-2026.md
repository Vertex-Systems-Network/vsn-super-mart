# Batch 15 — Third-party October 2026 PageSpeed snapshots and Fetch correction

**Updated:** 2026-10-25. **Scope:** Stage 2 research only, no active Figma design and no code development.

## What has actually been observed

Six publicly opened eDIY competitor-theme report pages published **18 preset-specific Google PageSpeed Insights homepage lab snapshots from October 2026**. Source labels and extracted figures live in `shopify-third-party-pagespeed-batch15-2026.json`. The sources are **independent third-party reports**, not own PSI runs, not raw Lighthouse JSON, not Chrome screenshots, not CrUX field data and not new opened Shopify demo storefront HTML.

- [Prestige family](https://ediy.io/directory/shopify-themes/prestige/) — Prestige, Strass, Vogue, Signature, Couture
- [Broadcast family](https://ediy.io/directory/shopify-themes/broadcast/) — Broadcast, Airwave, Relay, Motif, Stellar
- [Expanse family](https://ediy.io/directory/shopify-themes/expanse/) — Expanse, Revive, Spritz, Fetch, Gem
- [Impulse](https://ediy.io/directory/shopify-themes/impulse/), [Symmetry](https://ediy.io/directory/shopify-themes/symmetry/), [Savor](https://ediy.io/directory/shopify-themes/savor/)

The reports do not provide independently reproducible raw PSI report identifiers, precise conditions and number of runs for each snapshot; changes in content/server/CDN can change numbers. Never call this our own benchmark, a mobile screenshot or a Theme Store pass/fail.

## Recorded competitor homepage lab scores

| Preset | Mobile | Desktop | Mobile LCP | Mobile CLS | Mobile TBT |
|---|---:|---:|---:|---:|---:|
| Prestige | 67 | 94 | 6.5s | 0.00 | 0ms |
| Strass | 68 | 93 | 13.8s | 0.00 | 42ms |
| Vogue | 83 | 92 | 4.2s | 0.00 | 47ms |
| Signature | 83 | 94 | 3.5s | 0.00 | 4ms |
| Couture | 71 | 90 | 8.2s | 0.00 | 0ms |
| Broadcast | 59 | 94 | 5.0s | 0.00 | 496ms |
| Airwave | 70 | 95 | 11.8s | 0.00 | 107ms |
| Relay | 76 | 87 | 5.2s | 0.00 | 62ms |
| Motif | 70 | 93 | 7.7s | 0.00 | 8ms |
| Stellar | 69 | 96 | 14.9s | 0.00 | 0ms |
| Expanse | 70 | 87 | 8.0s | 0.00 | 76ms |
| Revive | 73 | 96 | 7.2s | 0.00 | 0ms |
| Spritz | 87 | 80 | 3.3s | 0.00 | 91ms |
| Fetch | 76 | 100 | 5.7s | 0.00 | 87ms |
| Gem | 85 | 87 | 3.5s | 0.00 | 134ms |
| Symmetry | 85 | 92 | 3.8s | 0.09 | 20ms |
| Impulse | 65 | 98 | 11.3s | 0.14 | 67ms |
| Savor | 71 | 94 | 6.4s | 0.00 | 17ms |

**Descriptive snapshot:** Reported mobile score range 59–87; median 71. All 18 third-party mobile *lab* LCP figures exceed the 2.5-second recommended good value; this is not a field Core Web Vitals assessment and the publisher's own numbers cannot be reproduced here. A single mobile home score of 59 does not prove Shopify Theme Store rejection. Do not double-count family-level repeated live-store averages on the publisher's pages as independent per-preset samples.

## Actionable, original VSN QA implications

- Mobile-first image sizing, image-source dimensions, responsive hero art direction and correct lazy/eager loading should be validated for **real LCP elements**, not inferred from marketing speed statements. Original VSN `responsive-images`, `image-banner`, `perf-lighthouse` settings are mapped in JSON.
- Complex home sections, autoplay video, collection swatches, Quick View, async Section Rendering and promotions need measured impact on mobile CSS/JS, reduced motion and interactivity after actual Stage 7 implementation.
- **Store test evidence must contain:** exact route, theme version, product/catalog fixture, raw Lighthouse/PSI JSON, device profile and network, number of runs, median and observed issue reproduction.
- **Shopify Theme Store requirements** explicitly require **minimum *average* Lighthouse performance 60 and accessibility 90**, across **home, collection and product pages** on **both desktop and mobile** using a benchmark dataset with content/media: https://shopify.dev/docs/storefronts/themes/store/requirements. Single homepage PSI scores cannot establish this.
- Shopify's testing guide calls for each route **at least three Lighthouse runs, median result and same device/network**. Its store speed weighted estimate uses **home 17%, PDP 40%, collection 43%**, but the Theme Store admission threshold uses a **plain average** over the three page types: https://shopify.dev/docs/storefronts/themes/best-practices/performance/testing-for-performance.
- Google recommends good **field** LCP <=2.5s, INP <=200ms, CLS <=0.1. Lab TBT is *not* field INP and neither should be relabeled as such: https://developers.google.com/search/docs/appearance/core-web-vitals.

## Corrected earlier research data

Batch14 Expanse recipe mistakenly listed **Fetch** as outside the selected 127 and supplemental. It **is included** (`expanse:fetch`) in `shopify-presets-2026.json`; earlier Batch5 independently opened `fetch-theme-modern.myshopify.com` home, collection, PDP, cart and recorded it as selected in `shopify-live-demo-evidence-2026.json`. Corrected recipe JSON, Batch14 markdown, audit validator, handoff and research README. This is a **classification fix, not a new storefront visit**.

## Progress and remaining research

Unchanged actual source coverage: **43/127 selected demo homes (33.9%)**, **47 demo storefronts and 131 primary HTML docs** (47 home, 37 collection, 38 product, 9 separate cart). Pending selected: 84 demo homes, 94 collections, 92 PDPs, 118 cart URLs; screenshots, variant/filter/cart actions, keyboard/a11y, Lighthouse and private Theme Editor are still unexecuted. No VSN theme development or Figma work. PR #9 remains the research branch pending merge.
