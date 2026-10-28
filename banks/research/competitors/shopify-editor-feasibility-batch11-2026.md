# Batch 11 — Shopify Theme Editor feasibility and compliance (2026-10-25)

## Scope / evidence

This research opened authoritative first-party Shopify docs for [Theme limits](https://shopify.dev/docs/storefronts/themes/architecture/limits), [Blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks), [Static blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks), [Settings and visible_if](https://shopify.dev/docs/storefronts/themes/architecture/settings), [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) and [Preset architecture](https://shopify.dev/docs/storefronts/themes/store/success/updates). Every documented constraint is mapped to existing VSN option IDs in `shopify-editor-feasibility-batch11-2026.json`. It is **not** private competitor Theme Editor access or a live HTML demo audit.

Coverage stays **43/127 (33.9%)** selected preset demo homepages, **47 storefronts / 124 indexed HTML documents**. No new storefront document was verified in this batch. Direct public storefront fetches failed in this session, and the browser connector remains denied. Failed visits do not increment the denominator.

## Findings to retain before design and development

- Shopify supports **300 physical theme block files**, and merchant Sidekick-generated files count too. The **192 conceptual VSN elements are not equal to 192 physical Liquid blocks**; allocate compiled blocks, snippets and sections consciously. [Official Blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks)
- **25 sections per JSON template, 50 dynamic blocks per section, 1,250 blocks per template and 8 theme block nesting levels** constrain VSN’s proposed deeply nested Elementor/Gutenberg-like editor. Static blocks have different limit and edit behavior; section-local and theme blocks cannot be mixed in the same section. [Official limits](https://shopify.dev/docs/storefronts/themes/architecture/limits) · [Blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks)
- **Conditional editor fields (`visible_if`) cannot inspect resolved dynamic source or storefront runtime data**; market/customer/metafield display rules need real Liquid guards, not invented Theme Editor behavior. Shopify itself owns theme/section Custom CSS settings. [Official settings](https://shopify.dev/docs/storefronts/themes/architecture/settings)
- **Theme Store compliance blocker:** mandatory wishlist and compare for each VSN demo conflicts with the prohibition on app-dependent or incomplete theme-native functionality and the rule that a demo showcases only theme-built features. Keep wishlist/compare as the separate optional VSN-app track; agree exact Theme Store demo scope before Stage 4/5. Do not silently drop the product vision or falsely market app-only features as built-in. [Official Theme Store](https://shopify.dev/docs/storefronts/themes/store/requirements)
- **No-app core baseline:** product/featured product sections still need true product blocks and `@app` support even when no apps are installed. Native product/variant/buy/cart functionality must never be hidden behind VSN app availability. [Official Theme Store](https://shopify.dev/docs/storefronts/themes/store/requirements)
- A Theme Store theme must be based on **Shopify Skeleton or fully original code**, not Dawn/Horizon. Multiple presets must demonstrate structural differentiation, not only settings/theme colors. [Official Theme Store](https://shopify.dev/docs/storefronts/themes/store/requirements)
- **Bundle size and schema size need a planned budget** because 192 elements × nine responsive breakpoints can produce unmanageable settings/schema. Stage 7 must measure actual compiled bytes and Stage 8 must run Lighthouse/keyboard/device tests; no guessed performance scores. [Official limits](https://shopify.dev/docs/storefronts/themes/architecture/limits) · [Official Theme Store](https://shopify.dev/docs/storefronts/themes/store/requirements)

## Traceable decision registry

| # | Decision ID | Priority | Original VSN direction |
|---:|---|---|---|
| 1 | compiled-block-budget | high | Explicitly map every conceptual element to block, snippet or reusable section; budget headroom for merchant/AI added blocks. |
| 2 | section-composition-ceilings | high | Budget rich home/collection/PDP designs inside template and block ceilings; distinguish static from dynamic counts. |
| 3 | nesting-limit | high | VSN Group/Container hierarchy must collapse wrappers or use snippets before hitting depth 8. |
| 4 | block-schema-incompatibility | high | Prefer theme-block architecture for globally reusable elements; choose local section blocks only when nesting/reuse is unnecessary. |
| 5 | static-component-semantics | medium | Use static only for essential fixed UI; dynamic merchant components remain reorderable; do not present static as draggable. |
| 6 | block-vs-snippet | high | Reserve theme blocks for merchant-configurable structure; share low-level rendering through snippets to avoid bloated sidebar and file budget. |
| 7 | setting-visibility-scope | high | Separate editor display logic from runtime Liquid conditions for variant, market, customer or metafield values. |
| 8 | platform-owned-css | medium | Expose original token/variation settings, not a fake custom CSS override UI that changes merchant's platform customization. |
| 9 | dynamic-source-translation | medium | Offer metafields/metaobjects where supported; ensure theme locale translations and merchant content translation paths are distinct. |
| 10 | theme-store-app-boundary | critical | Keep Wishlist/Compare requirement in optional VSN apps/extras, but block those app-dependent interactions in Theme Store submission/demo unless Shopify confirms an allowed representation. Retain standard @app integration support. |
| 11 | core-product-section-app-blocks | high | Theme product layouts must keep independent merchant editability and app-block slots without requiring any app. |
| 12 | presets-per-demo | high | Evaluate VSN theme identity across all templates; publish each preset with substantive structural/UX differentiation and a demo equivalent to installed state. |
| 13 | theme-store-code-origin | critical | Stage 7 inherits Skeleton/original; competitor and Shopify sample code are research only. |
| 14 | filesize-and-style-budget | high | Avoid 192-by-nine-breakpoint settings explosion; only expose selected anchors and advanced overrides where practical. Keep content/media outside bloated packaged theme. |
| 15 | theme-store-performance-and-accessibility | high | Defer runtime claims until benchmark QA; animate with reduced-motion and avoid oversized nested DOM. |

## Agent documentation drift corrected

`AGENTS.md` and `ai/state/progress.json` are authoritative: **Stage 2 / no active Figma**. The old `CLAUDE.md` had an obsolete active Figma target and told agents to spend Figma AI credits. Stage 6 and Stage 9 sections of `ai/WORKFLOW.md` also instructed Figma AI use despite AGENTS specifying **ChatGPT-generated images, not Figma AI**, with verified asset upload only into a newly approved Figma file. Updated those subsidiary documents without creating a new design, recovering obsolete frames or changing theme code.

## Gate and next research

`scripts/platform_feasibility_audit.py` enforces nonempty source-backed option mappings, unique decisions, matching current Stage 2/no-Figma state and absent stale Figma AI instructions. Wired into the existing research CI. Continue actual demo home/collection/PDP/mobile research for remaining 84 presets when retrievable; never increase source counts from listings or documented vendor claims.
