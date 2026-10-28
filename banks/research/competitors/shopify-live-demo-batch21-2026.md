# Shopify selected-preset live-demo research — Batch 21 (2026-10-26)

## Scope and evidence types

This batch closes the top pending selected preset's homepage destination and inspects four storefront routes on Shopify's official Savor sample store. Pages were read directly in a rendered browser's accessibility tree. These are browser-rendered page observations, not screenshots and not executed shopper tests. No add-to-cart, cart mutation, quick-add, facet action, checkout, keyboard test, mobile viewport or private Theme Editor access was attempted.

The repo's existing 127-preset indexed HTML counter remains unchanged: **51/127 selected homepage documents (40.2%)**, **76 pending**. This batch records **one additional selected homepage plus collection/PDP/cart in a separate rendered-browser evidence class**, giving **52/127 selected presets with a homepage observed across either source class (40.9%)**. The other 75 selected presets have no independently opened homepage source in either indexed HTML or this rendered-browser set.

## Savor — selected free Shopify preset

| Page | URL | Rendered browser observations |
|---|---|---|
| Home | https://savor-theme-demo.myshopify.com/ | SHOP / ABOUT / RECIPES navigation; hero link to Dipping Sauces; six-product shelf; food brand-story section and video prompt |
| Collection | https://savor-theme-demo.myshopify.com/collections/all-products | 34 items reported; Availability and Price filters plus Sort control; product cards use Choose or Add labels |
| Product | https://savor-theme-demo.myshopify.com/products/sweet-pineapple | Three gallery images; 16.5 oz (468 g) statement; 1, 2, 3 and 6 bottle pack options; quantity, Add to Cart, Buy It Now and quick-add bar |
| Cart | https://savor-theme-demo.myshopify.com/cart | Empty state, account sign-in prompt, Continue Shopping link and three product recommendations |

Product recommendation modules on the PDP showed loading placeholders in the captured page state. Their settled state was not checked. Page copy and sample product facts are merchant-written demo content, not verified product claims.

### Source-linked design hypothesis

The Savor route sequence combines a food-specific category campaign, product discovery, clear pack-size choices, and browse recovery from an empty cart. For a new VSN direction, preserve the information hierarchy—package quantity and selected-variant price together, concise facet controls, clear purchase routes, and optional empty-cart recommendations—while creating a different visual system and copy. This pass does not establish visual composition, mobile behavior or working interactions.

Pattern added: food-multipack-merchandising mapped to variant-picker-styles, faceted-filters, quick-add, empty-states and cart-upsell.

## Independent automated accessibility report (third-party; not a VSN test)

AccessifyAI says it scanned Savor 4.2.0 on September 29, 2026 across home, collection, product and cart pages; it reports 8 issue types and 65 occurrences across the 12 criteria surfaced by its index. The report says this is not certification and states that many WCAG criteria require manual checking. These figures are attributed to the external scanner and are not reproduced or independently validated by VSN. Treat this as a source for future manual QA cases only.

## Source records

- Demo: https://savor-theme-demo.myshopify.com/
- Official listing: https://themes.shopify.com/themes/savor/presets/savor
- Third-party scan: https://accessifyai.de/shopify-theme-accessibility/savor
- Machine record: banks/research/competitors/shopify-live-demo-evidence-2026.json → browser_render_observations
- Stage gate matrix: banks/research/competitors/shopify-127-completion-matrix-2026.json → Savor row

No browser interaction, accessibility certification, Lighthouse, screenshot or responsive/device claim is made.
