# Batch 14 — Expanse family documented homepage recipes + Shopify dynamic-render QA

**Research date:** 2026-10-25. **Status: Stage 2, research only.**

## Source class: vendor recipe, NOT a live storefront document

Official Archetype support published the exact ordered homepage section recipes for the Expanse family (May 15, 2026):

- [Expanse preset family homepage breakdown](https://help.archetypethemes.co/hc/en-us/articles/51462622741523-Expanse-theme-homepage-breakdown)
- [Expanse version notes](https://help.archetypethemes.co/hc/en-us/articles/46027072690835-Expanse-release-notes)
- [Shopify stylesheet content subsetting](https://shopify.dev/docs/storefronts/themes/best-practices/performance/stylesheet-subsetting)
- [Shopify >250-variant product guide](https://shopify.dev/docs/storefronts/themes/product-merchandising/variants/support-high-variant-products)
- [Shopify Theme Editor lifecycle](https://shopify.dev/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks)

The vendor source is **not** permission to mark an actual demo home, mobile render, cart interaction or private Theme Editor verified. Vendor-published section ordering is recorded separately under `shopify-vendor-homepage-recipes-expanse-batch14-2026.json`. We attempted to find new selected premium preset demo host URLs, but Shopify listing “View demo” destinations were not exposed as independently fetchable storefront documents. **Zero new live HTML sources counted in this batch.**

| Vendor preset | Chosen cohort? | Ordered published modules, including groups | Approx. JSON-template modules (excluding header/footer groups) | Distinctive source-backed grouping |
|---|---:|---:|---:|---|
| Expanse | Yes | 17 | 14 | Split heroes, promotional grids, hotpots and repeated collection rails |
| Revive | Yes | 21 | 18 | Beauty hero, repeated featured collection, testimonials, before/after, newsletter |
| Spritz | Yes | 20 | 17 | Food/drink merchandising, promos, recipe navigation, trust and editorial |
| Fetch | Yes | 17 | 14 | Pet video hero, sale promo, trust/review, collection and blog |
| Gem | Yes | 13 | 11 | Gem/jewelry promotional mosaic, gallery, lookbook, storytelling and trust |

The source explicitly describes vendor demo configuration. This is different from a screenshot or interactive test. **Correction (Batch 15):** Fetch is included in the selected 127 as `expanse:fetch` and was already part of the previous live HTML research. All five recipes belong to selected preset identities; the vendor recipe does not add another demo HTML page. Compare against four earlier Impulse family recipes as cross-family merchandising evidence, not proof that nine complete stores were visited.

## Translatable original VSN element requirements

There are **23 normalized section kinds** mapped to current VSN option and element IDs. High-signal patterns:

- The same `featured-collection`, `promotional-grid`, `hero-slideshow` and `collection-list` primitives form substantially different niche narratives based on block settings and ordering; VSN should support original design differentiation without copying Archetype's exact layout or creative assets.
- Multi-block promo grids require flexible image/video/product/collection/banners, honest price/discount data and predictable responsive spans; no invented scarcity.
- Testimonials, skincare before/after media, gallery, logos, recipe/blog content and tiered collection promotions are merchant-managed optional content, not theme-injected factual endorsements.
- **Library gap:** an actual before/after **image comparison slider** element is not yet in the 192 conceptual VSN element catalog. Related image/media primitives exist but are **not a real substitute** for a compliant interactive compare. Stage 3 should add/approve an original reusable element and settings model, with keyboard/pointer/touch QA, before promising the effect to merchants.
- Source recipe lengths below 25 JSON-template sections are not proof of Shopify compiled output. Header/footer group accounting must remain separate and actual generated structure is a later development/validation task.

## Six new CSS/variants/Theme Editor quality gates

`shopify-dynamic-render-qa-batch14-2026.json` records **six unexecuted test scenarios**, grounded in Shopify's current official developer guides and Archetype's Expanse 10.0.0/10.0.1 release notes:

1. **Render-tree CSS ownership**: Shopify subsets `{% stylesheet %}` CSS by section/block/snippet rendered tree; unrelated file CSS can disappear from a Quick View/Quick Add/cart fragment. Shopify Theme Check includes `ValidScopedCSSClass`.
2. **Section Rendering API**: Partial DOM extraction must preserve necessary `<style data-section-stylesheet>` content supplied with fetched dynamic sections.
3. **High variant count**: `product.variants` Liquid returns only up to **250 variants**; VSN's PDP and quick add must use supported selected-option APIs for larger catalogs rather than looping incomplete variant sets.
4. **Accurate selected-variant data**: Vendor notes describe previously fixed stale pickup/inventory, option-availability and add-to-cart states. They are vendor historical bugs, **not** VSN bugs and not a live competitor demonstration.
5. **Theme Editor event lifecycle**: Section re-render after an editor action does not rerun page-load JS automatically; component initialization, teardown, focus and selected-slider behavior need actual editor QA.
6. **Stylesheet count vs interaction latency**: No stylesheet tags for each product card instance; measure loaded style count, field INP and dense catalog interactions later.

The vendor noted Expanse v10.0.1 (Aug 21 2026) compatibility for Shopify stylesheet subsetting and v10.0.0 (Aug 7 2026) high-variant picker modernization. These are **vendor notes**, not a performance measurement or runtime validation.

## Cumulative progress / limits

**43 / 127** selected independently opened demo homepages = **33.9%** (84 pending); **47** unique Shopify demo hosts; **131** primary opened indexed HTML pages (47 home +37 collection +38 product +9 separate cart). No change from Batch 13. Official **127/127** preset/listing pages were already separately verified; their count is not equivalent to the demo source count. All browser interactions, checkout, mobile devices/screenshots, Lighthouse and competitor private Theme Editor remain untested. Main branch unaffected; PR #9 research branch only. No theme code or Figma file changed.

**Next:** prioritize independently retrievable remaining 84 preset demo homepages; keep vendor release/configuration and live HTML distinct. Original image comparison element research must be resolved at the Options/Element mapping gate before new designs.

**Recorded Batch 15 correction:** Both `shopify-presets-2026.json` and `shopify-live-demo-evidence-2026.json` contain `expanse:fetch`. Earlier supplementary classification was incorrect; the verified-home count remains unchanged.
