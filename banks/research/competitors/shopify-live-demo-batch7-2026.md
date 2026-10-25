# Shopify live-demo research — Batch 7 (2026-10-25)

## Evidence and coverage

**Two selected premium presets** with newly opened live storefront home documents: **Prestige Signature** and **Broadcast Airwave**. A separate **Enterprise Theme Sections** developer showcase was also inspected but is **not** any one of Enterprise/Outlet/Homestead and thus **does not count** toward 127 selected designs.

Cumulative **28 store roots, 74 public HTML documents; 24/127 selected preset live-homepage documents = 18.9%**. This measures source retrieval, **not** completed interactive/mobile/cart/editor testing, current inventory or whole project progress.

| Source | Home | Collection | Product | Cart | Cohort |
|---|---|---|---|---|---|
| [Prestige Signature](https://prestige-theme-signature.myshopify.com/) | Opened (indexed ~1 month ago) | URL cache miss | URL cache miss | URL cache miss | **Yes**, `prestige:signature` |
| [Broadcast Airwave](https://broadcast-theme-airwave.myshopify.com/) | Opened (4-day indexed) | [All 5 products](https://broadcast-theme-airwave.myshopify.com/collections/all) (old ~1-year indexed source) | [House Blend](https://broadcast-theme-airwave.myshopify.com/products/coffee-blend) (~2 months old) | URL cache miss; homepage has cart drawer markup only | **Yes**, `broadcast:airwave` |
| [Enterprise Section showcase](https://enterprise-sections.myshopify.com/) | Opened (2-week indexed) | [Test product catalog](https://enterprise-sections.myshopify.com/collections/all) (~2 months old) | URL cache miss | URL not verified | **No**, standalone developer section test |

### Grounded observations

- Signature documents shoe departments (Pumps, Mules, Flats, Boots), euro localized country selector, 2026 campaign, best-seller shelves, Shop the Look, boutique and informational editorials. A visible coming-soon countdown shows zeroed units, but a real event isn't proved. No collection, product or standalone cart URL was successfully opened.
- Airwave features a five-product coffee assortment and educational brewing posts plus product FAQ, grind choices, gift and mug upsell. Its public collection document shows availability, price and product-type facets, sort and preorder status. The House Blend page provides 250g and grind options, shipping information and a sold-out/notify state. Its home and PDP contain **$100 versus $50** free-shipping thresholds, not automatically a bug: merchant policy contexts were not checked.
- Enterprise's **theme sections test site**, not a customer-ready named preset, exposes department search, Quick Order, comparison table and flash-sale timer. Its fixed campaign ended in October 2026; current campaign status and button behavior aren't tested. Never copy its static test product UI as proof of functional Shopify compare.

The public HTML can include *both* hidden cart/variant states. Don't label it a functional issue without rendered interaction tests. Source-level caveats captured in `shopify-demo-source-claims-batch7-2026.json`.

## Mapping into VSN AI banks

Three new evidence-linked design/system patterns; three qualitative Design Bank observations; **four proposed merchant control settings** covering variant-dependent CTA, shipping threshold source of truth, honest campaign countdown and app-first product compare. These controls are not built. No user image source, competitor code, or layout cloning.

Next: Find further supported actual preset demo URLs, retrieve collection/PDP where possible, then run authorized browser-based accessibility, cart and responsive QA separately. Old Figma Stage 6 remains archived.
