# Shopify first-party demo deep PDP evidence — Batch 12 (2026-10-25)

**Cumulative HTML-only research:** 47 Shopify storefront hosts, **129 independently opened home/collection/product/cart HTML pages**, of which 37 are PDP documents. **43/127 selected preset homepage sources** (33.9%) remain unchanged; selected product-page sources increased **29 → 34**. This batch adds **five opened PDP URLs**; not new preset homepages, mobile/screenshots, cart mutations or Theme Editor access.

| Shopify free preset | Individually opened product URL | Source findings | Indexed crawl recency |
|---|---|---|---|
| Pitch | https://theme-pitch-demo.myshopify.com/products/age-serum | Serum imagery, retinol and cosmetic benefit/claims, natural ingredient marketing, pairing | 3 days |
| Sense | https://theme-sense-demo.myshopify.com/products/natural-vegan-lip-balm-lemon-lime | Flavor choices, seven images, ingredients, care, delivery and returns | Yesterday |
| Publisher | https://theme-publisher-demo.myshopify.com/products/braulio-amado-2021 | Book size/ISBN, image gallery, quantity controls, conflicting shipping copy | 3 weeks |
| Trade | https://theme-trade-demo.myshopify.com/products/classic-towels | Large towel variant matrix, per-unit price, quantity-rule prompts, sold-out rows, care | Yesterday |
| Studio | https://theme-studio-demo.myshopify.com/products/rhyme | Artist biography, original artwork and signature copy, framing, related art, shipping/returns | Last month |

## Source-backed risk findings (not confirmed UX defects)

- **Publisher:** same indexed PDP has a $15 free-shipping callout near product and $150 North America shipping banner in footer; scope/rules untested. VSN must derive each threshold from consistent market/currency policy rather than competing editorial settings.
- **Trade:** variant rows and quantity-rule text do not establish an activated Shopify Plus B2B customer account or successful bulk cart mutation. Verify actual entitlements and a fully functional variant/quantity form before release.
- **Sense:** source includes both "Sold out" and "Add to cart" strings that could represent hidden alternate states. No actual variant click performed and no runtime defect asserted.
- **Pitch:** sample retinol/skin/ingredients marketing must never become universal theme claims. Merchant provides product-specific truth and substantiation.
- **Studio:** artwork originality, signed-artist copy and shipping return claims are merchant sample prose, not independently certified provenance.

Full five source-linked risk records are in `shopify-pdp-source-claims-batch12-2026.json`. Three original mapped research patterns added: flexible product disclosures, dense accessible variant/quantity tables and consistent market-specific shipping copy. Existing five design observations were extended with PDP modules; no fake full visual fingerprint.

## Evidence / QA boundary

These are **indexed public HTML documents** retrieved individually on 2026-10-25, with different source crawl ages. An HTML cart-success modal is not proof of actually adding to cart. No clicked filters, variant switching, checkout, mobile screenshot, keyboard test, Lighthouse report or private editor tests were completed. Stiletto Linen homepage reopened but its linked collection/PDP/cart URLs failed retrieval, so none was counted. Stage 2 research only; Figma archived and theme code untouched. Continue 84 unverified preset home demos when their actual stores can be opened.
