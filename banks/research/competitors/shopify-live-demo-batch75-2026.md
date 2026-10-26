# Shopify live-demo research — Batch 75 (Be Yours:Harmony)

Date: 2026-10-26  
Evidence class: browser_render_readonly, using the destination exposed by the official Shopify Harmony listing preview iframe.

## Pages inspected

- Official listing: https://themes.shopify.com/themes/be-yours/presets/harmony
- Listing iframe destination / Home: https://beyours-theme-tech.myshopify.com/
- Headphones collection: https://beyours-theme-tech.myshopify.com/collections/all
- Dynasty Headphone PDP: https://beyours-theme-tech.myshopify.com/products/beoplay-h95

## Observations

- Home has a Dynasty Headphone video hero, one-product-store intro copy, feature slideshow, featured product, technical specifications, guarantees/download links, comparison table, review carousel, newsletter and store-address/footer modules.
- Headphones collection contains 3 products and exposes sort, filter, grid-density and Quick View controls. None were activated.
- PDP shows €899, five color options, inventory copy, Add to Cart/Buy It Now and sticky-cart controls, followed by technical details. No product or cart control was activated.
- Visible content conflicts: homepage calls the demo a one-product store while the collection shows three products; PDP says over-ear headphones while a specification row says “True wireless In-ear”; color controls and availability copy conflict. Treat as demo content errors, not verified product facts.
- Cart drawer opened but exposed no empty-state message or dedicated cart page, so it is not counted as a cart page.

## Counts

- Unique selected homepages across source types: 85/127; 42 remain.
- Rendered pages: 202 across 51 selected presets.
- Indexed HTML totals unchanged: 51 home, 38 collection, 40 product, 11 cart.

## Limits

No filters, sort, grid, Quick View, variants, quantity, cart mutation or checkout actions; no screenshot, measured viewport/mobile, Theme Editor, keyboard or performance tests. Product, stock, specification, warranty, shipping and other seller claims remain unverified.
