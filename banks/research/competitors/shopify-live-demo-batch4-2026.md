# Shopify live-demo HTML research — Batch 4 (2026-10-25)

**Three additional live stores, nine opened HTML pages**; total **13 stores / 42 pages**, with **10** distinct selected popular Shopify presets now having live-homepage HTML evidence out of 127. All observations are public document source, **not** functional browser click/checkout/mobile tests.

| Theme and actual demo | Home | Collection | Product | Cart |
|---|---|---|---|---|
| [Impulse default](https://impulse-theme-fashion.myshopify.com/) | Opened | [Linen Edit](https://impulse-theme-fashion.myshopify.com/collections/2026-the-linen-edit) (7 SKUs and product type/price/availability filters) | [Lido Short](https://impulse-theme-fashion.myshopify.com/collections/2026-the-linen-edit/products/the-lido-short) | [Empty cart](https://impulse-theme-fashion.myshopify.com/cart) |
| [Symmetry Salt Yard](https://salt-yard.myshopify.com/) | Opened | Fetch unavailable | [Knitted Polo](https://salt-yard.myshopify.com/collections/new-arrivals/products/knitted-polo-shirt) | Fetch unavailable |
| [Legacy Expanse Food & Drink](https://expanse-theme-food-and-drink.myshopify.com/) | Opened | [Organic Wine](https://expanse-theme-food-and-drink.myshopify.com/collections/everything-organic-wine) | [Lemon Refresher](https://expanse-theme-food-and-drink.myshopify.com/collections/everything-organic-wine/products/organic-collection-lemon-refresher) | Fetch unavailable |

**Critical classification:** The legacy Expanse Food & Drink demo is **not** verified as the current 2026 Expanse Spritz preset. It does not count toward selected 127 designs.

**Impulse** product pages show sale pricing, size guide, descriptions, shipping and recently viewed. **Salt Yard** PDP shows swatches, stock, pre-order, pickup at named locations and fit guide. **Legacy Expanse** category offers Large/Small/List density and filters, with age-gate and promo copy in home.

## Data-integrity findings (not proven functional bugs)

- Salt Yard homepage contains $100/$150 shipping-message differences; actual eligibility context not known.
- Salt Yard PDP includes an outdated May 2025 expected shipping statement when observed in October 2026.
- Impulse's Lido Short has a size chart despite underlying single Default Title variant; chart could legitimately be informational.
- Legacy Expanse extracted PDP contains malformed negative savings copy; browser-rendered version not independently checked.
- Legacy Expanse giveaway countdown has no verified underlying merchant end date.

Five source-linked QA cases in `shopify-demo-data-integrity-2026.json` and five **proposed, unimplemented** VSN merchant element schemas in `banks/elements/specs/shopify-retail-data-integrity-2026.json`.

**Still pending:** 117 of the selected 127 live demo storefronts, actual cart mutations/checkout, mobile/responsive screenshots, Lighthouse, competitor Theme Editor access. Previous Afterhours Figma archived and superseded; active project stage is Research 2, and a new design will be built later.
