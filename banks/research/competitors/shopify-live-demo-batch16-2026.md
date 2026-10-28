# Shopify premium demo HTML research — Batch 16 (2026-10-25)

## Independent storefront evidence and coverage

Six **new primary indexed HTML page documents** from two additional independently opened selected paid preset storefronts: **Impact Sound** and **Expanse Furniture**.

| Theme/preset in VSN selected cohort | Actual independently opened page | Public indexed page crawl recency | Evidence |
|---|---|---|---|
| Impact / Impact | [Sound homepage](https://impact-theme-sound.myshopify.com/) | 6 days | Promotional audio hero/slideshow, bestsellers, color options, quick-add source, market selector, product comparison specifications, FAQ and social/editorial blocks |
| Impact / Impact | [MW07 Plus Leica PDP](https://impact-theme-sound.myshopify.com/products/mw07-plus-leica) | 5 months | Seven-image product gallery, limited-edition label, product technical specs, included accessories, sharing, subscription-policy generic markup and add-to-cart source |
| Impact / Impact | [Separately fetched /cart](https://impact-theme-sound.myshopify.com/cart) | ~1.2 years | Dedicated empty-cart page with continue-shopping action, services/trust content and a shipping threshold sample (no customer cart mutation) |
| Expanse / Expanse | [Furniture homepage](https://expanse-theme-furniture.myshopify.com/) | 2 days | Large multi-department menu, category rail, shop-the-look, cross-promos, newsletter, local pickup and seller sample countdown |
| Expanse / Expanse | [Furniture collection](https://expanse-theme-furniture.myshopify.com/collections/furniture) | 5 days | 13-product product grid, native-looking sorting and type/price/brand/availability facet markup |
| Expanse / Expanse | [Alessi coffee-maker PDP](https://expanse-theme-furniture.myshopify.com/collections/coffee-makers/products/90018-neapolitan-coffee-maker) | 2 months | Price/compare-at, inventory, alleged shipping and sustainability trust claims, long editorial description, collapsible information and recommended products |

**Counts updated:** 49 distinct public sample Shopify demo storefronts (formerly 47); **137 primary indexed HTML pages** (formerly 131), comprising 49 home, 38 collection, 40 product, 10 separately opened cart documents. **45/127 selected popular preset homepages**, up from 43/127 (**35.4%**, 82 pending). Selected collection sources **34/127**, selected PDP sources **37/127**, selected cart documents **10/127**. No real interaction/device/checkout/editor test added.

## Source signals and original VSN product architecture

**Impact Sound** showcases an ambitious original module mix: country/currency market controls, editorial audio heroes, true spec attributes in comparison tables, quick-add product-card affordances, audio product color cards, product photography and a collection of branded story/video/trust blocks. Dedicated MW07 Plus Leica PDP exposes seller-provided dimension, battery/material/size specs and box contents. Model these as Shopify product metafield/metaobject-supplied block data; avoid styling/specs hardcoded to a theme. VSN theme-store build must follow the app boundary for full interactive comparison, distinct from an ordinary informational comparison table.

**Expanse Furniture** demonstrates category-scale navigation and filtering in one coherent commercial home. The separate furniture collection has published 13 results and product-type/price/brand/availability filters. This is **HTML source evidence**, not proof of successful filter clicks. Promo and “12 days” Black Friday countdown graphics appear on pages with Spring branding and long-term seller anecdotes. Do not infer an actual running countdown, local pickup eligibility or current availability from HTML alone.

**Five high-priority copy/data QA cases** in `shopify-source-claims-batch16-2026.json`:

1. Expanse coffee-maker PDP displays an apparent **negative savings label “Save $-695”** with a $695 current/base price. This is an actual *indexed HTML string* in a two-month-old source, not a verified currently visible buyer-facing defect; calculate savings only when `compare_at_price > price`.
2. Impact older cart footer promotes shipping free over $99, while newer home promotional content offers free standard shipping for every order; **dates and scopes differ**, not an authenticated checkout-rule contradiction. Connect merchant policy centrally.
3. Expanse Black Friday countdown uses sample-looking 12-day/12-hour values, but neither user countdown runtime nor event date was checked. No fabricated urgency.
4. Impact comparison/Quick Add/stock source strings do not prove a functioning theme editor/product comparison or add-to-cart action.
5. Expanse product’s “low stock — 1 left”, carbon-neutral and shipping statements are merchant-demo copy from an older indexed PDP, not validated live inventory or certification.

Four new original research patterns mapped to IDs in VSN Options and Global Elements banks: structured spec and optional comparison, native collection facet scale, real campaign data for countdowns, and merchant-backed trust/shipping claims.

## Evidence discipline and next work

Read-only opened public indexed HTML pages with source crawl ages **2 days to 1.2 years**. No screenshot, browser click, actual variant change/cart mutation/checkout, Lighthouse, keyboard or private competitor Theme Editor settings inspected. Impact collection URL was not independently fetched; Expanse separate cart route was cache-missed, so neither was fabricated or counted. Static page includes hidden state variants and demo content; never assume business data currently true.

**Still pending:** selected cohort **82** homepage demos, **93** collections, **90** PDPs, **117** separately verified carts; and functional/mobile/accessibility/Editor tests. Stage 2 active, Figma historical, theme source untouched. Changes on open research-only PR #9.
