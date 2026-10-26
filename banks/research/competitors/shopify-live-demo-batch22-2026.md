# Shopify selected-preset live-demo research — Batch 22 (2026-10-26)

## Scope and evidence

This batch inspected the next priority selected preset, Refresh, on its public Shopify demo at https://theme-refresh-demo.myshopify.com/. Four routes were inspected through a rendered browser accessibility tree: home, Hair collection, Shampoo product and empty cart. This is rendered page structure evidence only; no interaction, screenshot, viewport measurement, mobile, Theme Editor, checkout or performance test was performed.

Indexed-HTML coverage remains **51/127 selected homepage documents (40.2%)**, with 76 indexed HTML homes pending. Browser-rendered evidence now covers 2 additional selected homepages (Savor and Refresh), so **53/127 selected presets (41.7%) have a homepage observed across either source class**. Four pages from Refresh join the four Savor pages; browser-rendered pages do not increment the indexed-HTML count. **74 selected presets remain unseen in either source class.**

## Refresh — rendered observations

| Page | URL | Observations |
|---|---|---|
| Home | https://theme-refresh-demo.myshopify.com/ | $40 free-shipping announcement; Hair/Body/Face/Kits navigation; hero slide with a product route; featured skincare shelf with quick add; press quotes; four image-led category stories; kit shelf; trust copy; journal slider; newsletter |
| Hair collection | https://theme-refresh-demo.myshopify.com/collections/hair | Seven products; Availability and Price filters; Best selling sort; quick-add controls; sale-price card; gift-card module and shampoo article link |
| Shampoo product | https://theme-refresh-demo.myshopify.com/products/shampoo-2 | Five gallery images; $14 price; quantity control; Add to Cart and Buy It Now; Highlights, Scent, Details and Ingredients disclosure headings; product quote, trust copy and related hair-routine links |
| Cart | https://theme-refresh-demo.myshopify.com/cart | Empty state; Continue Shopping; four-item favorites shelf with sale-price and Add/Choose controls; free-shipping announcement |

The homepage identifies the carousel as one of three slides, but only the first slide's content was inspected. Ingredients and other collapsed PDP panels were not opened. Store statements about certification, vegan status, product testing, packaging, country of origin, review counts, refunds and shipping are demo merchant copy and were not verified.

### Design hypothesis

Refresh connects category discovery, quick-add product rails, image-led category content, review-style quotes, trust statements, journal articles and a product routine. A new VSN direction can offer these as settings-driven modules, with product disclosures and related products arranged around the shopper's needs. Keep claims merchant-controlled and require evidence before presenting them as verified.

Pattern added: personal-care-routine-editorial-bridge, mapped to collection-list, collapsible-tabs, related-products, blog-posts, faceted-filters and quick-add.

## Third-party accessibility scan (not a VSN test)

AccessifyAI reports scanning Refresh 16.0.0 on September 29, 2026 across home, collection, product and cart, with five issue types and nine occurrences within the criteria it evaluates. Its report states that this is not certification and that keyboard, visual and most criteria need manual review. The accessed Shopify listing shows version 16.1.0 dated October 9, 2026, so the external scan predates that listing version. These claims are attributed to AccessifyAI and are not VSN findings or a test of v16.1.0.

## Sources

- Shopify demo: https://theme-refresh-demo.myshopify.com/
- Official listing: https://themes.shopify.com/themes/refresh/presets/refresh
- Third-party scan: https://accessifyai.de/shopify-theme-accessibility/refresh
- Machine evidence: banks/research/competitors/shopify-live-demo-evidence-2026.json → browser_render_observations
- Matrix row: banks/research/competitors/shopify-127-completion-matrix-2026.json → refresh:refresh

