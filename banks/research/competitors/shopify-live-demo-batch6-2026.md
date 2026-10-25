# Shopify demo evidence — Batch 6 (2026-10-25)

**Six newly inspected selected official theme/preset storefronts.** Cumulative **25 unique Shopify demo store hosts, 68 page HTML documents, and 22/127 (17.3%) selected preset records with opened homepage evidence**. This is **not** complete live usability testing or overall project completion.

| Selected preset | Actual demo home | Additional observed page documents |
|---|---|---|
| Stiletto Linen | [Footwear homepage](https://stiletto-theme-linen.myshopify.com/) | Collection/PDP/cart fetch failed |
| Stiletto Glimmer | [Beauty homepage](https://stiletto-theme-glimmer.myshopify.com/) | [29-collection index](https://stiletto-theme-glimmer.myshopify.com/collections) (NOT product facets) |
| Stiletto Tapestry | [Ceramics/workshops homepage](https://stiletto-theme-tapestry.myshopify.com/) | [All Ceramics, 68 products](https://stiletto-theme-tapestry.myshopify.com/collections/all-ceramics), [Dinnerware set PDP](https://stiletto-theme-tapestry.myshopify.com/products/4-piece-dinnerware-set) |
| Prestige Strass | [Fine jewelry homepage](https://prestige-theme-strass2.myshopify.com/) | [Earrings, 18 products](https://prestige-theme-strass2.myshopify.com/collections/earrings), [Wave Silver PDP](https://prestige-theme-strass2.myshopify.com/products/wave-silver-necklace) |
| Sleek Wildpeak | [Outdoor apparel homepage](https://sleek-wildpeak.myshopify.com/) | [Adjustable-waist pants PDP](https://sleek-wildpeak.myshopify.com/products/amelia-hiking-pants-with-adjustable-waist-camel) |
| Shopify Dawn | [Free theme demo](https://theme-dawn-demo.myshopify.com/) | [Bags, 26 products](https://theme-dawn-demo.myshopify.com/collections/bags), [Sold-out convertible bag PDP](https://theme-dawn-demo.myshopify.com/products/small-convertible-flex-bag-cappuccino) |

These are public indexed source documents, with crawl recency fields in `shopify-live-demo-evidence-2026.json`; not permission to clone product images or code. No button, filter, variant, cart mutation, checkout, mobile screenshot, Lighthouse or private Theme Editor action was tested.

## Distinct design/commerce learnings

- **Same code family; distinct niches:** Stiletto's Linen (footwear), Glimmer (skincare by concern & size), and Tapestry (ceramic forms, finishes, workshops) illustrate how theme presets can vary taxonomy/content, merchandising and PDP detail without separate commerce engines.
- **Real product facets:** Tapestry's collection lists Form, Finish, Price and Availability across 68 products. Prestige Strass earrings lists Availability/Price/Color across 18 products. Glimmer `/collections` is a **collection directory** with 29 categories rather than a product filter page.
- **PDP decisions:** Tapestry's 5-piece set shows a Stone/Anthracite option and detailed care guidance; Strass has fine-jewelry color choices, 4 gallery assets, localized EUR price and warranty; Wildpeak has fit sizing guide, accordion and product inquiry; Dawn's bag source has 22 media and a currently sold-out color variant.
- **Risk/quality audits:** Tapestry shipping messages differ ($250 homepage vs $150 PDP); Strass warranty copy varies (3-year collection tile vs 2-year PDP); Wildpeak has a struck-through $0.00 compare-at and time-limited sale text whose expiry wasn't tested; Dawn's hidden “item added” message is **not** evidence of a successful cart transaction. Do not assume demo claims are valid merchant data.

AI changes: **5 evidence-linked pattern decisions**, **6 qualitative design observations**, **6 claim/quality cases** and **6 original proposed VSN merchant settings groups**. Proposed controls are research/specifications **not implemented in Shopify Liquid/JS**.

**Still open:** 105/127 selected presets without live homepage evidence. Every preset's interactive desktop/mobile/checkout/Theme Editor QA remains a separate pending task. No Figma work; prior Stage 6 remains historical.
