# Shopify targeted interaction review — Batch 133

**Date:** 2026-10-27  
**Branch:** `research/shopify-live-demo-batch6`  
**Scope:** read-only interaction research on selected public demo storefronts. Interaction UI was used in the normal browser viewport (**1363×936 CSS px**); mobile layout remains separately documented from the 360×640 preview sweep.

## Interaction observations

| Preset | Flow | Observed response |
|---|---|---|
| [Enterprise](https://enterprise-theme-digital.myshopify.com/) | Shop our range: Smart Tech → Home Technology → Smart Cameras | Each selector enabled the next. The final finder result opened a 7-product Smart Cameras collection. |
| [Enterprise](https://enterprise-theme-digital.myshopify.com/collections/smart-cameras) | Open Filter and Sort by | Filter groups: Availability (6 in stock, 1 out of stock), Price and Brand. Sort offered Featured, relevance, best selling, A–Z/Z–A, price low/high and date old/new. No values were selected. |
| [Enterprise](https://enterprise-theme-digital.myshopify.com/collections/smart-cameras/products/smartcamera-with-voice-control) | Open Basket without adding a product | Empty drawer showed a $0 subtotal and a Hot deals on tech recommendation shelf with Choose options actions. |
| [Prestige:Couture](https://prestige-theme-couture.myshopify.com/products/edie-cascade-wrap-mini-dress-black) | Select dress size S | S became selected; stock display changed from 4 to 3 in stock. No cart action followed. |
| Ignite:Peak | Existing 360×640 Shop Now CTA test | The CTA reached a 21+ gate; the prompt remained unanswered. |

## Completion status

- Targeted interactions: **5 observations across 3 of 127 selected presets**.
- Mobile visual review remains **127/127** at 360×640 CSS px.
- No add-to-cart, purchase, checkout, Theme Editor, keyboard/accessibility, or Lighthouse test was run.
- Interaction evidence was collected at the normal browser viewport and is not counted as mobile-device interaction validation.

## Design implications

- Offer a cascading catalog finder as an optional navigation aid, with direct category/search paths retained.
- Keep filter counts, price ranges, brand values and sort choices clear; update result counts after selections.
- Couple selected variants to stock and purchasability; keep size guidance close to the options.
- Use the empty cart for relevant discovery while preserving a clear $0 state and return path.

Per-preset records are in `shopify-live-demo-evidence-2026.json` and `shopify-127-completion-matrix-2026.json`; qualitative patterns are in `banks/design/competitor-observations.json` and `cross-platform-patterns.json`.
