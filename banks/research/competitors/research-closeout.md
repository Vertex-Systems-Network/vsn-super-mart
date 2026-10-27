# Cross-platform theme research — curated cohort closeout (2026-10-25)

## Scope & status

**Curated evidence collection: complete for the selected first cohort. Marketplace-exhaustive auditing: not claimed.** 55 unique, source-linked theme/preset/demo records covering Shopify, WooCommerce, BigCommerce and Magento. Shopify official preset pages are **vendor claims**; Woo, BigCommerce and Hyvä live demo pages are **document-level observations**, not interactive browser session tests.

The live-demo universe (Shopify Theme Store has hundreds of themes and multiple presets; Woo themes have dozens or hundreds of demos) cannot honestly be marked entirely researched in this cycle. `demo-audit.json.backlog` identifies live interactions, blocked demos and future monitoring without misreporting them as tested.

## Method

1. Prioritize popular Shopify themes using a dated, sample-based Koala leaderboard rather than unsourced 'top' rankings.
2. Open individual official preset/theme pages. Record each source URL, the source level, visit date, feature-option IDs and design signals.
3. Open public demo pages of Porto, Flatsome, WoodMart, BigCommerce Cornerstone and Magento Hyvä. Record only what can be observed in public HTML.
4. Map evidence into `cross-platform-patterns.json` and `banks/options/options.json`. Keep `competitor-observations.json` qualitative until visual screenshot audit upgrades fingerprint status.
5. Reject unverified interactions (cart completion, checkout, mobile UI, Core Web Vitals). Distinguish Woo/plugin functionality from native Shopify and Shopify app blocks.

## Priority decisions for VSN (original work, no copying)

| Priority | System | Research evidence | Implementation route | Guardrail |
|---|---|---|---|---|
| P0 | Large-catalog mega-navigation + filters | Warehouse, Empire, Porto Shop 35/Grocery 3 | Shopify native `linklists`, collections + Search & Discovery filter data | Keyboard/touch accessible menus; no 3rd-party markup clones |
| P0 | Conversion paths: quick view, quick add, cart drawer | Impact, Flatsome, Cornerstone | Shopify product/variant/cart APIs and original theme blocks | Real sold-out and cart errors; no fake urgency |
| P0 | Product gallery and variant media | Porto product layouts, Blocksy E-Bike, Prestige | Shopify `product.media` + variant picker | Native media, reduced motion, accessible alt and focus |
| P0 | Multi-niche styling | Horizon, Prestige Vogue, Warehouse Wood, Cornerstone Warm | Global editor tokens, section presets, nested theme blocks | One codebase; no fork per niche |
| P1 | Food/pickup/ingredient info | Local, Porto Grocery 2/3, WoodMart Vegetables | Native pickup + structured metafields | Merchant-verified info only; no inferred shipping totals |
| P1 | Long-form product landing | Porto Single Product, Impact | Shopify alternative PDP template + feature blocks | Standard PDP and checkout stay functional |
| P1 | Technical product compare/wishlist | Empire, Cornerstone, Blocksy Furniture | VSN app/theme-app extension slot | Do not store app-level customer data inside the theme |
| P1 | Strong editorial merchandise | Focal, Prestige, Porto lookbook demos | Image/video blocks with original media assets | Do not reuse competitor photography/layouts |

## Evidence limitations

- Shopify Theme Store often exposes “View demo” as a dynamic button, not an accessible direct demo URL. A preset listing is not a live demo.
- Blocksy's starter demo domain may return HTTP 403 while its official descriptions remain accessible.
- BigCommerce Cornerstone **Bold** demo was inaccessible; **Light** and **Warm** demos provided home-page evidence.
- Kadence's official WordPress directory listing is not a specific WooCommerce starter storefront.
- No full product/cart/checkout transaction, all-mobile screenshot sweep or real-device Lighthouse test is claimed.
- Original VSN Afterhours Figma layouts have been recreated but images/visual approval remain separate Stage 6 gates.

## Repeatable checks

```sh
python3 scripts/competitor_audit.py validate
python3 scripts/competitor_audit.py summary
python3 scripts/competitor_audit.py next
python3 scripts/vsn.py validate
```

New themes and demos are incremental future research, not blockers for signing off this **curated research cohort**. PR #1 is an AI system foundation merge, **not** the Shopify theme release or Figma Stage 6 design approval.


## Selected Shopify mobile sweep update — 2026-10-27

The curated Shopify cohort now has a 127/127 mobile preview sweep at 360×640 CSS px, documented in `shopify-mobile-review-batch131-2026.md`. This supersedes the earlier “no all-mobile screenshot sweep” limitation for the selected Shopify cohort only. It does not claim marketplace-wide coverage or a full interactive, editor, accessibility, checkout or performance audit. Two hero images had limited clarity; see the linked preset-level records.
