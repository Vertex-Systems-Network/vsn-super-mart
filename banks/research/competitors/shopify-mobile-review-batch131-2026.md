# Shopify mobile review — Batch 131

**Date:** 2026-10-27  
**Branch:** `research/shopify-live-demo-batch6`  
**Scope:** all 127 selected Shopify Theme Store presets, mobile preview at 360×640 CSS px.

## Completion table

| Measure | Result |
|---|---:|
| Selected presets reviewed | 127/127 |
| Clear mobile views | 125 |
| Limited-clarity views | 2 |
| Presets not reviewed | 0 |
| Mobile viewport attempts | 127/127 |

The two limited-clarity views were **Eurus:Arise** (a cookie-consent panel covered much of the hero and the background remained soft) and **Stiletto:Luster** (the mobile hero media remained low-resolution). Their headers and overall mobile composition were visible and reviewed; each limitation is recorded in the preset matrix and evidence log.

## Findings

- Most presets use a compact hamburger/wordmark/search/cart header followed by an edge-to-edge, single-column campaign hero.
- Search-heavy catalog layouts such as Enterprise and Warehouse stack more controls above the hero, reducing the initially visible campaign area.
- Large editorial headlines commonly continue below the first viewport. This is an expected vertical scroll pattern; headline wrapping should retain clear CTA separation.
- Text or promo strips approach or clip the phone edges on Palo Alto:Dynamo and Broadcast:Motif. Empire:Empire and Empire:Circuit also showed crowded/clipped header or hero copy in the earlier pass.
- Image-led fashion, beauty, home, food and pet presets generally preserve their visual focus at phone width. Product grids can remain two-column, as seen in Refresh and Spotlight.
- Lively presents an age-verification overlay in the mobile first view. No gated action was taken.

## Method and limitations

Opened the official Theme Store preset page, selected Mobile, opened View demo, and inspected the storefront preview at 360×640 CSS px. All 127 viewport sizes were verified. Notes describe only visible layout and text. No shopping controls, Theme Editor, checkout, keyboard, accessibility, or performance/Lighthouse testing was performed. Screenshots were inspected in the browser session but were not saved as image files.
