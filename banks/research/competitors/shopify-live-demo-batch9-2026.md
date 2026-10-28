# Shopify live-demo HTML audit — Batch 9 (2026-10-25)

**12 new first-party Shopify theme demos opened** in the fixed 127-design cohort. Total **43/127 (33.9%)** selected demo homepage documents, **47 independently identified Shopify demo hosts** and **124 opened indexed HTML page documents**. Batch 9: 12 homepages, 12 collections, 11 product pages, 0 new fetched cart pages. We do not count embedded cart modal markup as a cart URL or successful cart action.

| First-party demo | Home source | Collection source | PDP source |
|---|---|---|---|
| Tinker | [Home](https://theme-tinker-demo.myshopify.com/) | [Collection](https://theme-tinker-demo.myshopify.com/collections/the-gather-collection) | [PDP](https://theme-tinker-demo.myshopify.com/products/gather-magsafe-phone-stand-black-walnut) |
| Origin | [Home](https://theme-origin-demo.myshopify.com/) | [Collection](https://theme-origin-demo.myshopify.com/collections/all) | [PDP](https://theme-origin-demo.myshopify.com/products/2unfold-bag-copy) |
| Atelier | [Home](https://theme-atelier-demo.myshopify.com/) | [Collection](https://theme-atelier-demo.myshopify.com/collections/shoulder-bags) | [PDP](https://theme-atelier-demo.myshopify.com/products/mini-isla-suede-caramel?variant=50126854848810) |
| Rise | [Home](https://theme-rise-demo.myshopify.com/) | [Collection](https://theme-rise-demo.myshopify.com/collections/all) | [PDP](https://theme-rise-demo.myshopify.com/products/white-hoodie) |
| Ride | [Home](https://theme-ride-demo.myshopify.com/) | [Collection](https://theme-ride-demo.myshopify.com/collections/performance-boards) | [PDP](https://theme-ride-demo.myshopify.com/products/filipe-toledo-wildfire) |
| Crave | [Home](https://theme-crave-demo.myshopify.com/) | [Collection](https://theme-crave-demo.myshopify.com/collections/meal-starters) | [PDP](https://theme-crave-demo.myshopify.com/products/thai-larb-starter-pack) |
| Fabric | [Home](https://theme-fabric-demo.myshopify.com/) | [Collection](https://theme-fabric-demo.myshopify.com/collections/womenswear-children-only) | [PDP](https://theme-fabric-demo.myshopify.com/products/womens-essential-sweatpant-in-black?variant=44434707710005) |
| Vessel | [Home](https://theme-vessel-demo.myshopify.com/) | [Collection](https://theme-vessel-demo.myshopify.com/collections/coffee-tea) | [PDP](https://theme-vessel-demo.myshopify.com/products/us-25192?variant=44459717656633) |
| Dwell | [Home](https://theme-dwell-demo.myshopify.com/) | [Collection](https://theme-dwell-demo.myshopify.com/collections/bedding-1) | [PDP](https://theme-dwell-demo.myshopify.com/products/top-sheet-brushed-cotton) |
| Heritage | [Home](https://theme-heritage-demo.myshopify.com/) | [Collection](https://theme-heritage-demo.myshopify.com/collections/shop-mens) | [PDP](https://theme-heritage-demo.myshopify.com/products/mof-melton-wool-blanket) |
| Ritual | [Home](https://theme-ritual-demo.myshopify.com/) | [Collection](https://theme-ritual-demo.myshopify.com/collections/new) | [PDP](https://theme-ritual-demo.myshopify.com/products/rose-11-bag-1?variant=45042658443453) |
| Pitch | [Home](https://theme-pitch-demo.myshopify.com/) | [Collection](https://theme-pitch-demo.myshopify.com/collections/skincare) | Not verified |

## Source-backed findings and original VSN implications

- **Tinker, Atelier, Fabric:** availability, color and price facets; indexed collection labels show 74, 12 and 97 items, respectively. Build a scalable facets/sorting/variant-ready element system; sample counts are not live stock evidence.
- **Origin, Dwell, Heritage:** technical details, care, craft stories, image media and review narratives indicate optional original merchant-defined product-content modules, not hardcoded competitor text.
- **Rise:** Japanese storefront, yen prices and Japanese/English locale selector appear in homepage HTML. Locale switching and translations were not functionally tested.
- **Ride, Crave, Pitch:** sale and sold-out surfboard labels, food starter bundles, recipes and skincare promotions suggest different preset configurations. Shipping thresholds, cosmetics/food claims, discounts and inventory must come from valid merchant data.
- **Vessel, Ritual, Atelier:** category merchandising with rich imagery and variant-linked product URLs, but no variant switching tests.

**Research bank:** 5 additional source-linked design/system patterns and 12 additional qualitative observations. Historical Figma Stage 6 superseded. Nothing here authorizes copying another theme’s HTML, CSS, proprietary photography or distinctive composition.

## Accuracy and remaining QA

All documents are **read-only public indexed HTML** with per-page crawl recency in the evidence JSON. Sources range from today/yesterday to months old; Ride Performance Boards collection was crawled **last year**, and Rise White Hoodie PDP **9 months ago**. No functional filter, add-to-cart, checkout, quick view, nonempty cart, responsive screenshot, accessibility, Lighthouse or private Theme Editor testing was performed. Exactly **84 selected demo home sources** remain pending. The Pitch PDP URL is null because no separately verified product document was retrieved.
