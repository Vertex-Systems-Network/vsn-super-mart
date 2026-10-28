# Shopify live demo indexed HTML — Batch 17 Release/Forest (2026-10-25)

## Opened pages and source provenance

Added **two selected popular Shopify Release theme preset homepages** as separate publicly retrieved Shopify demo storefronts: the default **Release** fashion sample and **Forest** furniture sample. The [official Release preset listing](https://themes.shopify.com/themes/release/presets/release) and [Forest preset listing](https://themes.shopify.com/themes/release/presets/forest) confirm that Release is by DigiFist and Forest is one of its five presets. Forest sample explicitly identifies itself as “Forest Theme - DigiFist”; don't count its older Living+ vendor copy as a separate preset.

| Preset | Individually opened source | Indexed crawl recency | Document signals |
|---|---|---|---|
| Release / Release | https://release-main.myshopify.com/ | 2 days | Fashion assortment, editorial rails, country selection, size/colour choices, preorder/soldout badges, embedded featured product with size chart, journal |
| Release / Release | https://release-main.myshopify.com/collections/new-collection | 6 months | 21 product cards with Shopify taxonomy color IDs, price/availability filters, sorting, size/color swatches, editorial in-grid tile, sample countdown 0d state |
| Release / Release | https://release-main.myshopify.com/products/black-puffer-edge?variant=42204594929743 | last week | Individually retrieved product variant URL, product gallery/form, pre-order and size-related content; no selected variant click |
| Release / Release | https://release-main.myshopify.com/cart | 6 months | Dedicated empty cart 0 page, suggested products, continue shopping, subscription/age-verification modal strings hidden in source |
| Release / Forest | https://release-living.myshopify.com/ | 3 weeks | Furniture room/collection mega menus, eight leading arrivals, category imagery, editorial seasonal stories, blog, testimonials, seller service claims |
| Release / Forest | https://release-living.myshopify.com/collections/living-room | last month | 28 shown out of 49 products, availability/price/material attribute filters (Material CM/Material/Material VM), furniture product cards and pre-order item |

**Counts:** **51 storefront hosts**, **143 opened primary public indexed HTML page documents** (51 home, 40 collection, 41 PDP, 11 dedicated cart), versus 49 hosts/137 HTML before. Selected cohort homepages **47/127 = 37.0%**, **80 pending**; 36 selected collections, 38 selected PDPs and 11 selected cart pages. No extra count for vendor listing pages, failed links, source duplicates or UI page features visible in shared layout code.

## Source-backed original VSN patterns

Three new source-linked research patterns map to existing options/elements:

1. **Clothing variants, genuine preorder & promo composition:** Release fashion cards show sizes, colors, badges, stock and pre-order markup alongside editorial promo tiles. VSN should let merchants configure variant-aware cards with native Shopify taxonomy/metafields and actual product inventory/order eligibility, rather than hardcoded badge values.
2. **Furniture material filters:** Forest Living Room has distinct Material CM, Material and Material VM groups, plus price/availability and category navigational content. This is not proof of a duplicate-filter bug: treat underlying merchant filter definitions and metafield schemas as separate, and check real Search & Discovery behavior later.
3. **Cart hidden markup vs active visible state:** Release empty cart and shared quick cart/popups include various labels. Source presence does not establish cart mutation or popup visibility. VSN empty/nonempty cart must respond to actual buyer state; merchant-integrated popup content should not override hidden structure.

`shopify-source-claims-batch17-2026.json` includes 4 provenance/source recency guardrails for product/variant claims, expired timer, materially similar filter labels and finance/shipping policy copy.

## Testing limitations and next action

These are independently opened **indexed public HTML documents**, not Chrome screenshots, actual responsive behavior, real variant/filters/cart actions, merchant private Theme Editor, checkout, Lighthouse or accessibility verification. Source ages differ from 2 days to 6 months. Forest PDP and standalone /cart could not be retrieved and are explicitly **not counted**. The sample contains buyer-promises (“selected products in 7 days”, installments and free delivery), which are unverified seller copy, not statements of current entitlements.

Next: Continue 80 remaining selected preset demo homes and deeper collection/PDP/cart links, with exact source types and crawl age; no old Figma restoration or Shopify theme implementation. PR #9 research branch only, Stage 2 active.
