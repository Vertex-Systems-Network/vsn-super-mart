# Shopify live demo audit — Batch 24 (Enterprise)

Observed: 2026-10-26  
Selected preset: `enterprise:enterprise`  
Official listing: https://themes.shopify.com/themes/enterprise/presets/enterprise  
Demo host: https://enterprise-theme-digital.myshopify.com/

The official View demo resolved to a storefront labelled Enterprise Theme Enterprise. Read-only rendered browser accessibility trees were inspected for the homepage, Smart Tech collection, Smart Camera PDP and cart. This is browser-rendered page structure evidence; it does not establish visual hierarchy, functioning controls, merchant-claim truth or responsive behavior.

## Observations

- **Home:** Department and product-type navigation, free-shipping/service statements, flash-sale callout and a three-slide hero lead into category discovery and product shelves. Product cards show swatches, rating, markdown and stock states. Further modules include a camera comparison table, popular departments, advice/FAQ, featured products and newsletter. A dynamic Flash Sale modal appeared in the rendered state.
- **Collection:** Smart Tech reports 37 products, technical filters (including processor, display, memory and CPU speed), sorting, compare and grid/list controls. The visible count reads 18 of 37 with a Show more control. Product cards expose variants and sample price/stock/discount states.
- **Product:** Ecobee Smart Camera page has a ten-item gallery, review count, price and description, quantity and add/buy controls, credit/insurance/returns panels, technical specifications, reviews and related products.
- **Cart:** Empty state shows a $0 subtotal and Start shopping route, followed by purchase protection and a Rollbacks & More recommendation shelf. Help, gift-card, promotion and service messaging remain visible.

## Evidence limits

No shopper actions were executed: no filter, sort, compare, tab, accordion, add-to-cart or checkout interactions. No screenshot, viewport measurement, mobile render, Theme Editor, keyboard or performance test was captured. Stock, price, reviews, shipping and promotion text are merchant sample claims, not independently verified.

## Coverage update

Selected cohort coverage is 54/127 distinct homes across source classes: 51 indexed public HTML sources and 3 selected browser-rendered homes. The browser-rendered set now contains 12 pages across Savor, Refresh and Enterprise. Prestige:Prestige remains unresolved because its official View demo opened the Allure family preview; that family-only evidence is excluded from selected-preset coverage. Next priority: Broadcast:Relay.
