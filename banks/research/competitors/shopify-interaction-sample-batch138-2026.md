# Shopify live-demo interaction sample — Batch 138 (2026-10-27)

## Status

**Tier 2 complete: 33/33 presets.** Each record below has one live, visible interaction result recorded. The check focused on product disclosures, sizing, variant selection, product gallery zoom, locale controls, store pickup and search.

- Targeted coverage: 66/127 presets across 68 observations.
- Remaining interaction presets: 61 (Tier 3: 6; Tier 4: 38; other selected families: 17).
- Mobile visual review remains complete at 127/127, 360×640 CSS px, with two limited-clarity hero previews documented.
- Theme Editor, checkout, keyboard/accessibility and Lighthouse checks remain open.

## Interaction log

| Preset | Live demo page | Interaction | Verified result |
|---|---|---|---|
| focal / focal | [open](https://focal-theme-carbon.myshopify.com/products/leather-case-for-airpods-pro) | TECH SPECS on the product page | product accordion expanded |
| focal / ivory | [open](https://focal-theme-ivory.myshopify.com/products/evaline-e54-blazer) | Size chart on the product page | size chart opened |
| focal / quartz | [open](https://focal-theme-quartz.myshopify.com/products/1969-vintage-steel-white-36-39mm) | SHIPPING & RETURNS on the product page | product accordion expanded |
| focal / sapphire | [open](https://focal-theme-sapphire.myshopify.com/products/double-meteorites-stud-earrings-ae9784ox) | WARRANTY on the product page | product accordion expanded |
| expanse / expanse | [open](https://expanse-theme-furniture.myshopify.com/collections/planters/products/trigg-wall-vessel) | Description on the product page | product accordion expanded |
| expanse / revive | [open](https://expanse-theme-beauty.myshopify.com/collections/face-mists/products/valmont-priming-with-a-hydrating-fluid) | Description on the product page | product accordion expanded |
| expanse / spritz | [open](https://expanse-theme-food-and-drink.myshopify.com/collections/everything-organic-wine/products/organic-collection-lemon-refresher) | Description on the product page | product accordion expanded |
| expanse / fetch | [open](https://fetch-theme-modern.myshopify.com/collections/walking-kits/products/pink-dog-collar-walk-kit-bag-pins) | Description on the product page | product accordion expanded |
| expanse / gem | [open](https://gem-theme-emerald.myshopify.com/collections/earrings/products/karasuba) | Shipping information on the product page | product accordion expanded |
| local / local | [open](https://local-theme-main.myshopify.com/collections/bread-buns-crisps/products/some-bread) | the Language selector | localization selector expanded |
| local / soleway | [open](https://local-theme-soleway.myshopify.com/collections/mens-best-sellers/products/timberland%C2%AE-premium-6-inch-waterproof-boot) | the pickup-location selector | pickup location modal opened |
| local / thrive | [open](https://local-theme-thrive.myshopify.com/products/gut-health-ground-coffee) | Description on the product page | product accordion expanded |
| local / caffeine | [open](https://local-theme-caffeine.myshopify.com/collections/coffee/products/nicaragua-copy) | the Country/region selector | localization selector expanded |
| local / lively | [open](https://local-theme-lively.myshopify.com/collections/red/products/crimson-reserve-2016) | the store pickup/location panel | pickup location modal opened |
| stiletto / stiletto | [open](https://stiletto-theme-stiletto.myshopify.com/) | The listed product URL returned 404 during this review, so the same preset's public homepage was used. Opened its search modal and left the query blank. | search modal opened homepage fallback |
| stiletto / luster | [open](https://stiletto-theme-luster.myshopify.com/collections/all-jewelry/products/the-rivi-ring) | Materials & Care on the product page | product accordion expanded |
| stiletto / linen | [open](https://stiletto-theme-linen.myshopify.com/collections/footwear/products/teddy-heel-ecru?variant=45491245416563) | size 36 | variant selected url updated |
| stiletto / glimmer | [open](https://stiletto-theme-glimmer.myshopify.com/collections/face/products/marula-face-oil) | Ingredients on the product page | product accordion expanded |
| stiletto / tapestry | [open](https://stiletto-theme-tapestry.myshopify.com/collections/all/products/wine-cup-anthracite) | Product Care on the product page | product accordion expanded |
| motion / motion | [open](https://motion-theme-adventure.myshopify.com/collections/half-zips/products/merino-wool-quarter-zip) | Size guide on the product page. | size guide opened |
| motion / satchel | [open](https://motion-theme-accessories.myshopify.com/products/whelma-bag) | Description on the product page | product accordion expanded |
| motion / memo | [open](https://motion-theme-home.myshopify.com/collections/homewares/products/tumbler-eggplant) | Shipping information on the product page | product accordion expanded |
| palo-alto / palo-alto | [open](https://palo-alto-theme-main.myshopify.com/collections/new-arrivals/products/sabine-skirt) | Size guide on the product page. | size guide opened |
| palo-alto / dynamo | [open](https://palo-alto-theme-dynamo.myshopify.com/products/navigator-backpack) | Materials and specs on the product page | product accordion expanded |
| palo-alto / skylight | [open](https://palo-alto-theme-skylight.myshopify.com/products/kalinda-boots) | Size chart on the product page. | size chart opened |
| palo-alto / phenomena | [open](https://palo-alto-theme-phenomena.myshopify.com/products/halo-highlighter) | Description on the product page | product accordion expanded |
| palo-alto / pluma | [open](https://palo-alto-theme-pluma.myshopify.com/products/jardin-placemat) | Product details on the product page | product accordion expanded |
| pipeline / pipeline | [open](https://pipeline-theme-fashion.myshopify.com/products/callie-looker-cardigan-beige) | Size on the product page | size selector opened |
| pipeline / petra | [open](https://pipeline-light.myshopify.com/products/sky) | Our Promise | product accordion expanded |
| pipeline / pahoa | [open](https://pipeline-theme.myshopify.com/products/fig) | product-image Zoom | product gallery zoom opened |
| pipeline / phantom | [open](https://pipeline-botanical.myshopify.com/products/nina) | product-image Zoom | product gallery zoom opened |
| concept / concept | [open](https://concept-theme-tech.myshopify.com/products/air-beats) | Gold Tone | variant selected |
| concept / inova | [open](https://concept-theme-inova.myshopify.com/collections/seating/products/embrace-lounge-chair) | gallery media 1 in a modal | product gallery modal opened |

## Notes

Stiletto:Stiletto's listed product route returned 404 in this interaction pass. The same preset's live homepage was used to open its search modal; no query was submitted. Stiletto:Linen's size selector was tested after the accidental cart state was cleared.

During control targeting on Stiletto:Linen, an unintended quantity-2 add-to-cart state occurred. Both units were removed, the storefront cart showed “Your cart is empty,” and no checkout or payment occurred. The final review state left the demo cart empty.

## Synthesis

Tier 2 confirms broad use of in-page product disclosures and size guidance. Gallery zoom modals appeared in Pipeline and Concept; the reviewed gallery dialogs exposed close and image navigation. Local presets surfaced language, currency and pickup-location controls. Variant state was reflected in the selected option and, for Stiletto:Linen, in a variant-specific URL.
