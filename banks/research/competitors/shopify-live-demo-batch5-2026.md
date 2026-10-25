# Shopify live-demo research — Batch 5 (2026-10-25)

## Verified coverage and limits

Six additional selected Shopify Theme Store presets have **public indexed HTML storefront homepage documents**. In the 127-selected-preset cohort that is **16/127 = 12.6%** with some live-homepage HTML evidence. This is **not a progress percentage for complete functional mobile/checkout audit or for the entire VSN project**.

Cumulative **19 distinct demo store roots / 54 opened HTML page documents**. Several pages were indexed weeks/months ago; retrieval on 2026-10-25 does **not** guarantee freshness. Real mobile rendering, add-to-cart mutations, checkout, interactive filters, keyboard QA and private Theme Editor settings **were not tested**.

| Selected preset | Home | Collection | PDP | Empty cart |
|---|---|---|---|---|
| [Warehouse — Wood](https://warehouse-theme-wood.myshopify.com/) | Opened (indexed ~2 months earlier) | Fetch failed | Fetch failed | Fetch failed |
| [Focal — Ivory](https://focal-theme-ivory.myshopify.com/) | Opened (~6 days) | Fetch failed | Fetch failed | Drawer copy only |
| [Focal — Sapphire](https://focal-theme-sapphire.myshopify.com/) | Opened (~6 days) | Fetch failed | Fetch failed | [Opened](https://focal-theme-sapphire.myshopify.com/cart) (~11-month index; may be stale) |
| [Symmetry — Beatnik](https://beatnik-5.myshopify.com/) | Opened (~4 months) | Fetch failed | Fetch failed | Fetch failed |
| [Symmetry — Duke](https://duke-16.myshopify.com/) | Opened (~2 weeks) | [Decks (35)](https://duke-16.myshopify.com/collections/skateboards) | [Libellule 1](https://duke-16.myshopify.com/collections/skateboards/products/libellule-1) | Drawer copy only |
| [Expanse — Fetch](https://fetch-theme-modern.myshopify.com/) | Opened (same-day crawl) | [Walking Kits (22)](https://fetch-theme-modern.myshopify.com/collections/walking-kits) | [Lilac kit](https://fetch-theme-modern.myshopify.com/collections/walking-kits/products/lilac-dog-collar-walk-kit) | [Opened](https://fetch-theme-modern.myshopify.com/cart) |

## Grounded findings

**Warehouse Wood**: A category-constrained search form, department menus, brand/furniture hierarchy, featured SKU/variant controls, low stock, restocking and back-in-stock labels. These are only text from document source—no actual search query or stock policy checked.

**Focal Ivory and Sapphire**: One shared theme system delivers different preset content: Ivory image-forward fashion campaign and gendered clothes taxonomy; Sapphire jewelry by type/color and editorial storytelling. Both expose cart content in source, but only Sapphire's standalone empty cart document was opened.

**Symmetry Beatnik and Duke**: Beatnik eyewear hierarchy, sustainability story, translations and timed promo text. Duke skateboard apparel with 35-product Decks collection, size/price/product-type filters, sale/sold-out/pre-order card states, related products and size selection. Duke banner advertises different shipping thresholds ($35 and $100) in different locations; actual conditions were not tested. No product/page clicks were executed; linked pages were opened read-only.

**Expanse Fetch**: Actual "Expanse for Pet Stores" feature/positioning content appears on [the demo's features page](https://fetch-theme-modern.myshopify.com/pages/theme-features), and the official [Fetch preset listing](https://themes.shopify.com/themes/expanse/presets/fetch) describes a pet-oriented preset. Homepage includes color/category navigation, shoppable sets, price comparisons, social proof and visible countdown labels (no confirmed expiry). Walking Kits category lists 22 products with availability, price and XS–XL sizes; PDP shows size options and buy buttons. Standalone empty cart source was opened. Bundle-style naming does **not** prove bundle backend or add-to-cart success.

## AI mapping and QA

Four new evidence-linked research patterns, six qualitative design observations and five **proposed, unimplemented** control sets in `banks/elements/specs/shopify-home-category-pdp-controls-2026.json`. Mappings focus on real collection filters, variant-aware stock, accessible category search, actual bundle data and honest empty-cart messaging. No competitor source code, assets, or identical layouts copied.

**Link discovery:** The 2023 Japanese [public demo URL roundup](https://shopify-restaurant.com/themestore-demourl/) was used to locate candidate hosts; every stored demo homepage URL was separately opened as public HTML. Its old "Classic/Modern" preset labels are not used as current Shopify Theme Store names.
