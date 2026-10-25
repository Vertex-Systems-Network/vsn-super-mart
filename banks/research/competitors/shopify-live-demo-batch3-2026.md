# Shopify live-demo evidence — Batch 3 / new design reset (2026-10-25)

**Current design state:** Per explicit user direction, previous Stage 6 Afterhours Figma designs are no longer active. The next visual design will be **new, not a restoration**. This research must not be blocked by an old Figma approval.

## Verified individual live storefront documents

| Theme / preset | Home | Collection | Product | Empty cart | Browser interaction |
|---|---|---|---|---|---|
| [Motion — Satchel](https://motion-theme-accessories.myshopify.com/) | Yes, public HTML | Not fetched | Not fetched | Only embedded empty drawer text on homepage | No |
| [Local — Local](https://local-theme-main.myshopify.com/) | Yes, public HTML | [All products, 37 items](https://local-theme-main.myshopify.com/collections/all) | [Tomato puree PDP](https://local-theme-main.myshopify.com/collections/all/products/sliced-tomato-puree) | [Cart page](https://local-theme-main.myshopify.com/cart) | No |

**Satchel:** Homepage contains Whelma bags in five named colors with Quick View affordances, handbag editorial sections, returns/gift packaging/pickup promises, and a journal. It embeds empty cart-drawer markup; this **does not** count as successfully opening a separate cart page. Attempts to fetch its collection/PDP/cart routes failed.

**Local:** A comprehensive grocery demo with deep food taxonomies, local store preference and delivery estimates, 37-product collection with diet/allergen/certification labels and Compare affordance, PDP variants, nutrition table, pickup availability by store, and empty cart with a shipping estimator form. These are observed HTML page elements, **not proof the buttons work**. Allergen claims shown in a vendor demo must never be assumed truthful for merchant SKUs without data.

## Official vendor settings mapped to VSN

- [Local cart documentation](https://shopify-support.krownthemes.com/article/796-cart): full cart vs drawer, thumbnail aspect, upsells, shipping progress, cart notes and accelerated checkout (Shopify-owned button capabilities).
- [Local popup docs](https://shopify-support.krownthemes.com/article/800-local-popups): age, cookie, newsletter and image popups, timing/frequency control; consent must be handled appropriately.
- [Local blog article docs](https://shopify-support.krownthemes.com/article/810-local-blogs-article): article recipes with linked product quick buy.
- [Local style docs](https://shopify-support.krownthemes.com/article/794-layout-borders-shadows): cards/buttons/form borders and shadows.
- [Impulse release notes (Oct 9, 2026)](https://help.archetypethemes.co/hc/en-us/articles/46027069235091-Impulse-release-notes): 2048-variant support claimed, size-chart option binding, loading and mobile drawer fixes.

Vendor documentation supplies claimed settings; no competitor private Theme Editor was opened. `shopify-vendor-settings-2026.json` records provenance, `banks/elements/specs/shopify-local-commerce-controls-2026.json` supplies **proposed VSN original control schemas**.

## Progress and honesty

Cumulative **10 real Shopify demo stores / 33 HTML documents**. **8 stores** correspond to selected 127 Shopify theme/preset names. Additional 2 are valuable demos outside cohort.

**Still outstanding:** 119 selected demo store documents, functional cart/add-to-cart, editor login, keyboard, mobile screenshots, performance measurements, new design/artwork and eventual development testing. Do not use these findings as an excuse to clone competitor code or images.
