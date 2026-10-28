# Batch 18 — Vision / Ignite / Sleek release-derived VSN regression gates

Research recorded **October 25, 2026**, Stage 2. The attempted search for 80 remaining direct premium storefront demos did **not** yield a confirmable new actual demo URL/HTML document. The Shopify Theme Store `View demo` control was exposed as a button in publicly retrieved text, not a directly retrievable full demo route. Do not fabricate an address or count a vendor homepage, third-party UX review or PSI benchmark as independently visited Shopify demo HTML.

## Official Theme Store & first-party developer evidence

| Theme and preset source | Dated vendor release notes | Source type | VSN interpretation |
|---|---|---|---|
| Vision / Poochy | **v18.0.0, 2026-09-29**: mobile shortcut dock; fixed wrong cart-line quantity/remove after apps add/remove items; tall desktop mega menu cropping fix; standardized Shopify pixel/event payload | [Official Shopify preset listing](https://themes.shopify.com/themes/vision/presets/poochy) | Four independent unexecuted test plans for cart line identity, fixed bottom control overlap, viewport clipping and analytics event integrity |
| Ignite / Tails | **v2.7.0, 2026-09-09**: Compatibility Finder (aka My Garage), custom icon uploads, extendable product page schema and SEO/GEO enhancements | [Official Shopify preset listing](https://themes.shopify.com/themes/ignite/presets/tails) | Two planned tests for catalog fitment data and reusable product blocks; do not claim vehicle matching or improved AI ranking is verified |
| Sleek / Jumped | **v2.3.0, 2026-06-16** in accessed official listing: redesigned search drawer, collection promotion blocks, global motion controls and multi-currency free-shipping goal | [Official Shopify preset listing](https://themes.shopify.com/themes/sleek/presets/jumped) + [FoxEcom product site](https://foxecom.com/products/sleek-shopify-theme) | Two test plans for predictive search/shipping goal by market and accessible reduced-motion interactions. This version is **documented from the page** and not asserted to be the latest available version today. |

Eight original merchant/shopper/developer regression cases are stored in `shopify-vendor-regression-batch18-2026.json`; all have existing VSN option/element IDs, exact sources, precondition, expected original behavior, test plan and `status: not_executed`.

## Separately attributed independent UX review

[Theme-Hub's Vision review](https://www.theme-hub.com/vision-shopify-theme-review) reports having tested a Vision variant change (blue swatch changed corresponding speaker photos), a comparison tray of up to five items, and describes the preset home layouts for Vision, Onyx, Poochy, Velocite and Solstice. The reviewer also describes Poochy's embedded featured product with gallery/size inputs and Onyx before/after image comparison.

This is **third-party reviewer-reported interaction/content research**. We did not click that variant, run the comparison bar, inspect private settings or open those five demo sites as real standalone storefronts in this session. Documented separately in `shopify-independent-review-batch18-2026.json` with `vsn_mobile_or_interactive_tests: 0`. Do **not** increment selected demo homepage count or `interactive_events_tested`.

Design implications:
- **Cart-line mutation** must use reliable Shopify line keys, not outdated array indexes, especially with subscriptions, bundling/apps and rapid concurrent changes. Shopify event signals must align with actual successful action and avoid duplicate analytics.
- **Mobile header/dock and sticky ATC** need shared safe-area/overlap/keyboard handling; tall desktop mega menus must scroll without clipping, even at zoom 200%, low-height viewport or RTL.
- **Fitment/compatibility** requires verified structured merchant variant/product/make-model-year data and correct no-match states, not automated guarantees.
- **Flexible product editor blocks** should support original, accessible metafield-driven product facts and app slots under existing 300-file/8-depth constraints.
- **Search, promo tiles and free-shipping goals** must be accessible, market-currency consistent and backed by real shipping eligibility.
- **Independent reviewer feature claims** inform original VSN option requirements only. Vision's reviewer-reported app-like comparison is **not** proof that the same built-in feature is allowed in a Shopify Theme Store submission. Follow AGENTS.md rule: optional app track with Theme Store restrictions.
- **Before/after slider** remains an explicitly identified standalone reusable-element gap, not solved by the current ordinary comparison-table element.

## Counts and next step

No new direct Shopify demo HTML pages, source hosts, clicks, mobile renders, performance runs or Editor settings inspected. The evidence bank therefore remains **47/127 selected homepage sources (37.0%)**, **80 homepages pending**, **51 demo hosts and 143 primary HTML page documents**; selected category **36**, product **38**, cart **11**. Stage 2 continues. PR #9 research only; Figma/approved design absent, no theme implementation.

Next: independently retrieve pending premium preset demo storefront home/collection/PDP/cart URL(s) using actual vendor demo links or an accessible browser. Preserve `vendor`, `third_party_review` and `direct_opened_html` evidence boundaries, add a source only on confirmed fetch.
