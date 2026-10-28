# Shopify 127-preset systematic research — Batch 20 (2026-10-26)

## Scope, reconciliation and factual boundary

**One-round exhaustive 127-record status reconciliation plus 3 newly verified direct premium demo homepages.** The user requested full completion. This turn makes the existing bank auditable and closes all **127 official Theme Store listing checks**, but the stronger **127 individually opened demo homepages plus rendered responsive/editor/functionality testing is NOT completed**. The workflow must not advance Stage 2 or pretend otherwise. Indexed HTML and third-party/testimonial descriptions are not executed interactions.

Previously the Prestige **Strass, Vogue and Couture** homepages were counted in past batches. They were re-opened for refreshed source observation, **not** re-added to the selected cohort. Newly independently retrieved selected homes are **Eurus Arise, Eurus Whiff and Vision Poochy**.

| Preset | Direct individually opened primary HTML URL | Indexed crawler age | What was observed |
|---|---|---|---|
| Eurus / Arise | https://eurus-arise.myshopify.com/ | today | Supplement/wellness marketing, personalization quiz questions, variant/selling plan bundle chooser and customer content |
| Eurus / Arise PDP | https://eurus-arise.myshopify.com/collections/subscribers-favorite/products/maca-root-energy-libido | 2 days | Maca product option choices, copy and merchant data; no checkout |
| Eurus / Whiff | https://eurus-whiff.myshopify.com/ | today | Gift/personality quiz, build-3 jewellery set, local appointment and custom/bespoke claims, market selector |
| Eurus / Whiff collection | https://eurus-whiff.myshopify.com/collections/best-sellers-1 | 2 months | Eight product rows, material/vendor/in-stock filters, unconfigured advanced groups and registered-buyer price gating copy |
| Vision / Poochy | https://vision-pets.myshopify.com/ | last month | Pet merchandising, color/product types, supplier/pet marketing, stock/promo badges |
| Vision / Poochy collection | https://vision-pets.myshopify.com/collections/all | ~1.1 years | 16 pet product cards, color/size/availability filters, Compare source control |
| Vision / Poochy PDP | https://vision-pets.myshopify.com/products/holiday-penguin-dog-toy | ~1.1 years | Dedicated product source with variants and product data; cannot assert current stock |

Additional independently opened **supplementary** sources (not double counted in one-per-kind primary document bank):

- Prestige Strass bracelets collection: https://prestige-theme-strass2.myshopify.com/collections/bracelets — € jewelry grid with 15 products, price/color facets and zero-countdown text.
- Prestige Couture Dresses: https://prestige-theme-couture.myshopify.com/collections/dresses — additional filtered collection distinct from existing /collections/shop.
- Prestige Vogue Cinnamon Sage Lip Balm: https://prestige-theme-vogue.myshopify.com/products/cinnamon-sage-lip-balm — additional PDP distinct from earlier Bali Papaya Rice Masque source.
- Eurus Whiff sustainability editorial: https://eurus-whiff.myshopify.com/pages/our-sustainability — supplementary policy/claims page, not a PDP/category/cart.

**Direct primary source delta is +7** (3 homes +2 collections +2 PDP), from 144 to **151** primary opened HTML documents. Host count **52→55**. Selected homepage coverage **48→51** / 127, or **40.2%**. All are historical/public index text with age. No real browser sessions, mobile screenshots, add/remove cart action, predictive-search click, checkout, private Theme Editor or own Lighthouse were performed.

## Research originality and merchant control mappings

Four new reusable, source-attributed VSN patterns were added to `cross-platform-patterns.json`:

1. **Eurus Quiz + Bundle/Selling Plans:** Personalized recommendation quiz questions, tiered offer text, and publicly readable selling-plan data motivate original optional merchant-configured quiz rule/metaobject models. Actual prices/discounts remain Shopify-native; no unverified medical targeting or cart-success claims.
2. **Price-gated B2B and empty facets:** Whiff collection includes registered-price placeholders and empty Advanced filter 3/4 labels; protect buyer eligibility, do not expose restricted price in quick-view/API and don't show empty filter panels.
3. **Poochy comparison and availability:** Compare checkboxes visible in HTML aren't proof of functioning comparison or Theme Store-compliant built-in app; optional VSN extras remain separate. Use real selected-variant stock and current Search & Discovery facets.
4. **Market/currency/promotion truth:** Prestiges' € pricing and US-dollar shipping thresholds, Eurus multi-currency localized content, zero-time promos, supplements and sustainability claims require market-aware values and verifiable editorial/legal copy.

`shopify-source-claims-batch20-2026.json` contains six source-specific quality cases: medical wellness copy, quiz/selling plan claims, Whiff empty facets/registered pricing, Whiff sustainability material, Poochy old compare/inventory labels, and Strass shipping/currency/timebox copy. These are **source-copy review scenarios, not tested bugs or endorsements**.

## Universal 127-preset audit matrix

The new machine-readable artifact **`shopify-127-completion-matrix-2026.json`** has one row **for every selected preset**, linking:

- the actual already-verified official Shopify Theme Store listing URL and known date;
- verified home/category/PDP/standalone cart URL and source crawl age, or explicit `not_verified`;
- page-specific unresolved blockers and next independently checkable URL target;
- evidence class separated by `official_listing_only`, `indexed_public_document_only`, supplemental and external reports;
- per-theme-family totals and prioritized unresolved premium/free preset short list;
- zeroed nonexecuted cart clicks, mobile rendered layout, private editor, checkout and Lighthouse state.

The new `scripts/research_127_coverage.py` validation reads canonical selected preset catalog, actual individually opened demo page bank, cumulative plan, current Stage 2 status, and this generated matrix. It fails on nonexistent demo URLs, invented progress, source-date mismatch, skipped preset, duplicated preset ID, or false stage completion. The check was added to GitHub Actions research workflow.

## Progress and hard release gate

| Evidence | Verified | Pending |
|---|---:|---:|
| 127 individually opened official Shopify preset listings | 127 | 0 |
| Selected standalone demo home HTML | **51** | **76** |
| Selected collection HTML | **38** | **89** |
| Selected PDP HTML | **40** | **87** |
| Selected cart HTML | **11** | **116** |
| Actual browser/variant/filter/cart actions | 0 | all untested |
| Mobile viewport/accessibility/Lighthouse | 0 | all untested |
| Competitor private Theme Editor settings | 0 | no authenticated access |

Primary records: **55 distinct storefront hosts**, **151 opened indexed documents** = 55 home +42 collection +43 product +11 cart. More public pages in supplements are deliberately excluded from the primary metric.

A completed **status matrix** is not the same as a completed **live-demo research test**. At least **76 specific selected demo homepages** were unresolved in this turn despite official listing lookups, theme-doc searches and browser accessibility limits. The Shopify Theme Store View Demo button was not exposed as an independently retrievable destination in the static listing source for many premium presets, and exact browser/store credentials are required for later interactive/private-editor QA. Inaccessible URLs cannot be guessed and do not become verified merely through third-party summaries.

**Stage 2 remains active**, no Figma design currently approved, no theme code implemented; do not advance, merge into main, start Stage 6 or claim merchant feature verification until project exit gate passes.

## Deterministic next completion route

1. Resolve **76 missing actual preset demo home URLs** using official View Demo browser links, first-party developer demos or evidence-linked search; prioritize **Savor, Refresh, Prestige default, Enterprise group, Broadcast Relay, Impulse Dune, Vision default, Ignite, Sleek, Wonder, Palo Alto, Pipeline**.
2. For each of 127 selected presets independently retrieve collection, PDP and cart sources from real navigation, with per-document crawled age; never count the same HTML twice.
3. In a permitted browser/session, test real variant, filters, Quick View/add-to-cart, empty/nonempty cart, form and keyboard states, mobile at prescribed widths, localization and reduced motion; record screenshots and actual results separately from indexed HTML.
4. Compile source-backed Stage3 option and global-element gaps (e.g., before/after accessible image slider, merchant quiz); decide Theme Store wishlist/compare app boundary; collect sign-off.
5. Only after checks pass may `scripts/vsn.py advance` be used to move Stage 2 on. Create an entirely new Figma later and use original ChatGPT-generated imagery; no old Afterhours designs.

**Research progress bar:** 51/127 = **40.2%** confirmed selected homepage HTML; remaining 76. Official preset listing inventory is 127/127, which should never inflate the demo metric.
