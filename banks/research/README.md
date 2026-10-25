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
