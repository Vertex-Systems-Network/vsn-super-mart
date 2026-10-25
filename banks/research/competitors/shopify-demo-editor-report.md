# Shopify theme demo and Theme Editor audit — Phase 3

Updated 2026-10-25. **Live-demo interactive testing is not finished.** The connected graphical browser refused access. A public Theme Store preset listing cannot be used as a substitute for opening a live demo. This package sets up the next review and captures **verified Shopify platform architecture**.

## Verified official technical findings

- Theme-block files live in `/blocks` and can be reused across sections; app blocks require schema support.
- Blocks can have `settings`, `presets`, `blocks`, names and optional wrapper controls; section-defined blocks cannot be mixed with theme blocks within the same section.
- Important limits: 300 theme-block files, max nesting depth 8, max 50 blocks per section, max 25 sections per JSON template, and 1,250 blocks per template. These are important for VSN's 192-element catalog: one catalog element is **not** necessarily one Liquid block file.
- Merchant-facing descriptions/labels must meet Theme Store naming rules and use Shopify vocabulary; block settings should be grouped sensibly to avoid overwhelming the editor.
- Checkout and customer accounts are not fully theme-editable templates; do not promise editing capabilities that Shopify does not provide.
- Each template's and preset's editor options are proprietary until accessed; never invent that competitor X supports an exact option just because Shopify offers the schema field.

Sources: [Theme blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks), [Block schema](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/schema), [Theme limits](https://shopify.dev/docs/storefronts/themes/architecture/limits), [Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements).

## Research completion gates

The **127/127 official Theme Store listing pages** were verified in PR #2. **0/127 live demo complete** because public View demo targets weren't opened via an authorized browser.

To close a single *live demo* audit: visit the actual store URL; inspect home page, collection filters and product tiles, PDP gallery/variants, cart/drawer and mobile navigation; record screenshots, URLs and dates. Only use the word *tested* when actions were performed. To close *Theme Editor* research: consult vendor schema/docs or a licensed preview in the store Theme Editor—never infer private controls from marketing claims.

The scope is intentionally honest: no workaround or fake interactive links.
