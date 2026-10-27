# Shopify Keyboard Accessibility Smoke Sample — 2026-10-27

## Scope and result

A bounded keyboard-only smoke check was performed on the public Dawn preset demo product page:

- URL: https://theme-dawn-demo.myshopify.com/products/small-convertible-flex-bag-cappuccino
- Method: browser keyboard Tab/Shift+Tab/Enter, followed by read-only inspection of the active element, URL hash and scroll position.
- The first three forward Tab stops observed were: “Skip to content”, the Dawn home link, and the “Bags” menu button.
- Reverse navigation returned to the skip link. Enter activated it, changed the URL hash to `#MainContent`, and moved focus to the page’s `MAIN#MainContent` element.
- The accessibility tree exposes product title, price, sold-out status, color option radios, quantity controls, accordions and footer groups. All sampled color variants were labelled sold out/unavailable; the add-to-cart and accelerated checkout controls were disabled.

## Boundaries

This is one public storefront sample only. It does not establish keyboard or accessibility coverage for the 127-preset cohort, and it does not include screen-reader testing, contrast measurements, automated accessibility scans, zoom/reflow checks, or focus-visible styling verification. It is not an audit of the VSN theme.

No cart mutation, personal data entry, checkout submission or purchase occurred.

## Cohort status

The canonical completion matrix remains unchanged: mobile 127/127 and targeted interactions 127/127 (129 observations); Theme Editor 0/127, checkout 0/127 and Lighthouse 0/127. The one keyboard smoke sample is recorded separately and does not alter those counters.

## Requirements to close remaining gates

- **Theme Editor:** inspect the actual VSN development theme in an authorized Shopify store/admin preview; public competitor storefronts cannot reveal private editor settings.
- **Checkout:** run a bounded test checkout workflow on an authorized test store; stop before submitting customer/payment details or placing an order.
- **Lighthouse:** run the agreed mobile and desktop benchmark on the VSN theme’s home, collection and product pages after a preview is deployed. Third-party competitor PageSpeed snapshots do not satisfy this gate.
- **Keyboard/accessibility:** define the test matrix and perform checks on the implemented VSN theme. This single Dawn demo smoke test is comparative evidence only.

Stage 2 research remains active. No design or VSN theme-build gate is being marked complete.
