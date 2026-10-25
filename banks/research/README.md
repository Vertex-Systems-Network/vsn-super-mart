# Research Bank

Stores everything learned about the platform, competitors and each niche. Agents **read before designing**
and **write every new finding here with a source**.

```
platform/theme-store-requirements.json   Shopify Theme Store rules as a checklist (req-* ids)
competitors/themes.json                  popular themes, presets, positioning, market insights
competitors/demo-audit.json               individual opened demo/preset URLs with evidence levels
competitors/cross-platform-patterns.json  source-linked patterns mapped to VSN option IDs
niches/index.json                        list of niches + status (seed | verified) + counts
niches/<niche-id>.json                   one file per niche (schema below)
```

## Niche file schema
| key | meaning |
|---|---|
| id, name, aliases | identity |
| status | `seed` (initial, partly unverified) → `verified` (Stage 2 done with real sources) |
| shopper_profile, catalog_traits | who buys, catalog size / variants / price range |
| must_have_sections / nice_to_have_sections | `{id, name, page, why}` |
| product_page_elements, collection_page_elements | element lists |
| metafields_metaobjects | custom data the niche needs |
| design_patterns | typography, color_mood, imagery, layout, motion |
| conversion_drivers, anti_patterns | what sells / what to avoid |
| competitor_references | `{theme, preset_or_style, notable}` |
| option_map (optional) | `{section-id: option-id}` when a section maps to a differently named option |
| sources | `{title, url}` — only pages actually seen |

Rules: paraphrase (no long quotes), never delete sourced data without a newer source, one agent per niche file.

## Competitive demo research
Run `python3 scripts/competitor_audit.py validate` or `python3 scripts/vsn.py competitor-audit summary` before using cross-platform findings.

- `official_preset_page`: official product/preset listing opened; vendor features are claims, **not** interactive demo verification.
- `live_demo_page`: the individual demo page was opened and its visible document inspected; mobile layout, interactions and checkout are **not** tested by this alone.
- Every entry has source URL, date, platform, theme + preset, mapped option IDs and qualitative design signals; patterns cite entry IDs.
- Transfer **ideas**, not copyrighted code, images, brands, or pixel-identical designs. WooCommerce/Magento/BigCommerce features require a separate Shopify capability and Theme Store compliance check.
- The `backlog` is explicitly unvisited research. Do not claim that the entire theme marketplace has been inspected.

## Research closeout and executable decisions (2026-10-25)

- `competitors/research-closeout.md` is the curated cohort evidence summary and limitation ledger, not a claim of exhaustively visiting every public ecommerce demo.
- `competitors/shopify-implementation-matrix.json` maps the most important evidence-backed option IDs to native Shopify, original theme components, VSN apps, or app-block slots; all entries remain `planned` until development/QA.
- `scripts/competitor_audit.py validate` now checks per-template evidence coverage and these mappings, and prevents app-only wishlist/compare from being misclassified as native theme features.

## Popular Shopify theme and preset deep index (2026-10-25)

- `competitors/shopify-families-2026.json`: 47 official parent theme listings (24 paid multi-preset / 23 distinct free designs), mapped to existing option IDs with research hypotheses explicitly labeled.
- `competitors/shopify-presets-2026.json`: 127 design records (104 official paid preset names / 23 free standalone theme pages). All 127 selected individual official theme/preset listing URLs were opened on 2026-10-25; do not infer live demo or interactive testing from this.
- `competitors/shopify-popularity-top25-2026.json`: dated Koala tracked-store top 25 with Shopify Store/external/legacy classification.
- `competitors/shopify-external-themes-2026.json`: Ella, Minimog and Kalles external vendors; do not mix their demonstrations or feature rules with Theme Store listings.
- `competitors/shopify-research-report.md`: conclusions, product feature paths and remaining demo/checkout coverage.
- `python3 scripts/shopify_theme_research.py validate|summary|next` checks source counts, no duplicate names, mapping and honest verification statuses.

## Live Shopify demo HTML batch (2026-10-25)

- `competitors/shopify-live-demo-evidence-2026.json`: 4 actual public Shopify demo stores, 14 pages opened, with individual URL, option IDs and VSN element IDs. Only 2 demos belong to selected 127 preset cohort.
- `competitors/shopify-vendor-homepage-recipes-2026.json`: Impulse/Dune/Terrain/Apothecary homepage section orders taken from official Archetype support page; NOT an interactive store visit.
- `competitors/shopify-live-demo-report-2026.md`: findings and unsupported interaction/mobile/checkout limits.

- `competitors/shopify-live-demo-batch2-2026.md`: four more Shopify live demo HTML stores (Empire Depot/Wonder/Be Yours/Taste). Cumulative 8 stores, 28 documented public pages, 6 belonging to selected 127 design index. Interactive QA remains pending.

## Shopify live demo Batch 3 and new design decision (2026-10-25)

- `competitors/shopify-live-demo-batch3-2026.md`: Motion Satchel and Local default public page observations and explicit interaction limits.
- `competitors/shopify-vendor-settings-2026.json`: Local developer cart, popup, article, layout controls and Impulse v10 release-note claims, separate from private Theme Editor observation.
- `banks/elements/specs/shopify-local-commerce-controls-2026.json`: original proposed VSN settings for pickup/store selector, allergen labels, shipping estimator, article quickbuy, popups and variant picker; not runtime implementation.
- **No current Figma or Stage 6**: user superseded old designs; new design to be started later. Research proceeds independently.

- `competitors/shopify-live-demo-batch4-2026.md`: Impulse/Salt Yard and historical Expanse live HTML source audit: total 13 stores, 42 pages, 10 from 127. No dynamic action or mobile QA.
- `competitors/shopify-demo-data-integrity-2026.json`: five source-backed retail data integrity QA cases, not verified runtime defects.
- `banks/elements/specs/shopify-retail-data-integrity-2026.json`: five proposed VSN element settings, not built.

- `competitors/shopify-live-demo-batch5-2026.md`: six additional selected official preset storefront HTML sources; total 19 demo hosts and 54 page documents. Selected cohort 16/127 (12.6%) with at least opened home HTML, not functional/mobile audits.
- `banks/elements/specs/shopify-home-category-pdp-controls-2026.json`: proposed original VSN search, inventory, faceting, cart and variant settings, NOT implemented.

- `competitors/shopify-live-demo-batch6-2026.md`: Six new actual Shopify live HTML stores (Stiletto Linen/Glimmer/Tapestry, Prestige Strass, Sleek Wildpeak, Dawn); 25 store hosts, 68 page documents and 22/127 selected presets with live homepage evidence.
- `competitors/shopify-demo-source-claims-batch6-2026.json`: six merchant claim/pricing/urgency/source-evidence QA cases; not executed bugs.
- `banks/elements/specs/shopify-merchandising-controls-batch6-2026.json`: six merchant control groups proposed to preserve authentic filters, variants, bundles, offer promises and carts; not implemented.

- `competitors/shopify-live-demo-batch7-2026.md`: Prestige Signature and Broadcast Airwave real Shopify demo public HTML, plus Enterprise developer section showcase (not a selected preset). Coverage 24/127, 28 store roots, 74 documents. No UI/checkout/mobile testing.
- `competitors/shopify-demo-source-claims-batch7-2026.json`: six contextual shipping/inventory/countdown/compare checks with source URLs.
- `banks/elements/specs/shopify-controls-batch7-2026.json`: four proposed original VSN merchant setting groups, no runtime implementation.

- Batch 8 Shopify first-party themes: 35 source hosts, 89 HTML pages, 31/127 selected — `competitors/shopify-live-demo-batch8-2026.md`.

## Shopify platform feasibility — Batch 11 (2026-10-25)

- `competitors/shopify-editor-feasibility-batch11-2026.json`: 15 sourced constraints/decisions mapped to existing VSN option IDs; includes serious Theme Store app-dependent wishlist/compare scope conflict. This is **first-party platform documentation only**, not competitor editor or interactive demo inspection.
- `competitors/shopify-editor-feasibility-batch11-2026.md`: rationale and suggested Stage 4/5/7/8 gates for element compilation, Theme Store rules, responsive settings and image/Figma policy consistency.
- `python3 scripts/platform_feasibility_audit.py`: checks source mappings, status evidence and that project agents follow `AGENTS.md` and `progress.json` rather than archived Figma/Figma AI instructions.
- **Cumulative actual demo count remains 43/127 selected homepages, 47 hosts and 124 indexed HTML documents** pending new independently retrieved pages. Listing/vendor docs must not inflate demo coverage.

## Shopify first-party PDP HTML — Batch 12 (2026-10-25)

- `competitors/shopify-live-demo-batch12-2026.md`: five individually opened Pitch/Sense/Publisher/Trade/Studio product pages with source crawl age.
- `competitors/shopify-pdp-source-claims-batch12-2026.json`: five merchant data/policy claim risk checks (not confirmed runtime defects).
- Cumulative 47 demo hosts / **129 opened indexed HTML documents**, **43/127 selected demo homepages** and **34 selected PDP documents**. No new interactive/browser/device/checkout verification.

## Shopify indexed demo deep-page audit — Batch 13 (2026-10-25)

- `competitors/shopify-live-demo-batch13-2026.md`: Horizon PDP and Spotlight separately fetched empty-cart evidence; read-only, never an executed variant/add-to-cart test.
- `competitors/shopify-source-claims-batch13-2026.json`: 3 source integrity guards, not confirmed runtime defects.
- Stiletto Glimmer Minis and Pitch Bundles faceted collection documents recorded under `supplemental_documentation` rather than double counting primary category screens.
- Cumulative **47 storefront hosts / 131 primary indexed HTML pages**, **43/127 selected preset demo homes (33.9%)**, **35 selected PDPs / 9 selected carts**; no browser interaction/mobile/editor QA.

## Shopify Expanse documented demo recipes — Batch 14 (2026-10-25)

- `competitors/shopify-vendor-homepage-recipes-expanse-batch14-2026.json`: five vendor-published ordered homepage recipes (Expanse, Revive, Spritz, Fetch and Gem all selected; corrected in Batch15); 23 normalized section kinds linked to actual option/element IDs. **Vendor documentation only — no live HTML pages credited.**
- `competitors/shopify-dynamic-render-qa-batch14-2026.json`: six *not-yet-executed* original Shopify CSS subsetting/Section Rendering/high-variant/Theme Editor QA cases with official sources and vendor release note context. No implemented code claims.
- `competitors/shopify-vendor-homepage-research-batch14-2026.md`: distinction between five vendor recipes and verified demo count; image comparison slider missing as a dedicated VSN reusable element.
- Confirmed live demo progress still **43/127 selected homepage HTML (33.9%), 47 hosts /131 primary HTML documents**, pending 84 actual preset homepages.

## Batch 15 external October PageSpeed comparison (2026-10-25)

- `competitors/shopify-third-party-pagespeed-batch15-2026.json`: 18 selected Shopify preset homepage mobile/desktop PageSpeed lab measurements **reported by independent eDIY October 2026 pages** (six URLs), reported LCP/CLS/TBT, explicit evidence-class and three unexecuted VSN performance QA hypotheses. No raw PSI runs reproduced or mobile demos rendered by VSN.
- `competitors/shopify-performance-benchmark-batch15-2026.md`: competitor performance research plus **official Shopify requirements**: Theme Store Lighthouse average >=60 performance and >=90 accessibility across home, PDP and collection, mobile + desktop. Three runs, consistent Chrome/network, report median; compare to actual Shopify benchmark later.
- Corrected **Batch14 Fetch source-classification mistake**: `expanse:fetch` is selected and its demo home/collection/PDP/cart had already been opened in earlier research. Vendor recipe adds **0** new demo documents.
- Verified preset homepage HTML stays **43/127 (33.9%), 84 pending**, **47 hosts /131 primary documents**. Do not conflate independent publisher PSI snapshot with in-house Lighthouse or individual opened storefront HTML.

## Batch16 — two additional premium Shopify demo HTML audits (2026-10-25)

- `competitors/shopify-live-demo-batch16-2026.md`: opened **Impact Sound** and **Expanse Furniture** home pages, Impact PDP/empty /cart, Expanse Furniture filtered collection and coffee-maker PDP, each with individual source URL and indexed crawl age. **Actual public HTML, not vendor marketing page and not executed interaction.**
- `competitors/shopify-source-claims-batch16-2026.json`: 5 source-backed merchant claim/variant/urgency QA cases, including negative saved-amount string in older Expanse coffee PDP and inconsistent dated shipping banner language; **not confirmed current runtime bugs**.
- Four original reusable VSN option/element patterns plus two qualitative observations mapped.
- Cumulative **45/127 selected homepage HTML sources (35.4%), 82 pending**, **49 distinct Shopify demo hosts / 137 primary HTML documents**. Selected collection 34, PDP 37, cart 10. No browser/mobile/checkout/private Theme Editor testing.

## Shopify premium storefront HTML — Batch 17 (2026-10-25)

- `competitors/shopify-live-demo-batch17-2026.md`: 2 selected paid **Release/Release** and **Release/Forest** Shopify demo homes, plus default clothing collection/PDP/cart and Forest furniture category, each with exact independently opened indexed HTML URL and crawler age.
- `competitors/shopify-source-claims-batch17-2026.json`: four merchant policy/preorder/material filter/countdown provenance risks, not executed UI defects.
- Three source-linked, original merchant-control patterns and two catalog observations mapped. Cumulative **47/127 selected demo homes (37.0%)**, **51 hosts /143 primary HTML documents**. Selected: 36 collections, 38 PDPs, 11 carts; interactive/mobile/editor remain 0.
