# Batch 10 — Shopify official capability cross-check (2026-10-25)

## Evidence classification

Four **individual official Shopify Theme Store preset listings** were opened anew on 2026-10-25. This is **vendor-published capabilities and marketing claims**, **not** independently opened live storefront demo HTML, visual UX testing or Theme Editor inspection. Existing baseline **43/127 independently retrieved selected demo home documents** and 47 demo hosts / 124 public HTML pages is unchanged. Do not increment demo counts using these four listings, which already appear in the 127/127 official listing research inventory.

| Theme/preset | Official listing opened | Published capabilities relevant to VSN | Evidence level |
|---|---|---|---|
| Impact / Impact | https://themes.shopify.com/themes/impact/presets/impact | Vendor promotes 35+ sections, gradients, large typography, subtle motion; quick buy, sticky cart, cross-sell, promo tiles, lookbooks, hotspots, image comparison, swatch filters and RTL. Combined listing and quantity pricing are explicitly marked Shopify Plus. | Official listing only |
| Enterprise / Enterprise | https://themes.shopify.com/themes/enterprise/presets/enterprise | Vendor promotes speed, sticky add-to-cart, targeted popups, quick buy, stock counter, infinite scroll, swatch filters, compare-like discovery affordances and B2B combined listing (Shopify Plus). Performance is **not** independently measured. | Official listing only |
| Broadcast / Relay | https://themes.shopify.com/themes/broadcast/presets/relay | Vendor markets 30+ sections, one-click add-to-cart, upsells, promotional popups, recently viewed, before/after media and RTL-compatible storefront behavior. Accessibility/performance claims require independent measurement. | Official listing only |
| Savor / Savor | https://themes.shopify.com/themes/savor/presets/savor | Shopify first-party free theme stresses colorful food and ingredient storytelling, edge-to-edge photography, nested blocks, quick buy, filters and nutrition/ingredient information. Shopify Plus combined listings are a platform-dependent feature. | Official listing only |

## Controls and data-model implications for VSN Super Mart

1. **Do not convert listings into functional test results.** Vendor feature inventory only establishes potential capability; neither nested blocks nor popups are verified working in a third-party shop or private editor.
2. **Merchant controls: native first.** App and platform routing must distinguish theme-authored layout controls, merchant-provided product/metafield data, optional VSN app state, and Plus-gated B2B/combined listing capabilities. Do not promise Plus-only entitlements on every plan.
3. **Truthful dynamic states.** Stock counters, sale urgency and shipping/discount claims must rely on actual Shopify inventory, variant and market data. A Theme Store listing's presence of a countdown/stock counter does not authorize fictitious data.
4. **Visual direction:** Impact's dramatic motion-heavy promo composition, Enterprise's dense conversion controls, Broadcast Relay's social/editorial merchandising and Savor's food-first nested blocks are *research inputs*. VSN must produce original designs, not clone these themes' visual compositions.
5. **Future validation:** Open genuine View demo URLs and separately collect homepage/collection/PDP/cart HTML; perform real mobile screenshots, filters, add-to-cart and accessibility testing when a browser session is accessible. In this session the Opera browser connector was explicitly denied, so no browser interactions are claimed.

## Research status

No new preset homepage source verified in this batch; **43/127 (33.9%)** remains the honest demo homepage coverage. No new VSN elements, theme code, Figma frames or app code were implemented. Continue Stage 2 research on real demo storefronts once accessible; meanwhile vendor documentation can refine Options/Elements specifications without conflating evidence levels.
