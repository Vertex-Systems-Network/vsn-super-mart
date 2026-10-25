# Shopify live demo HTML research — Batch 13 (2026-10-25)

## Verified progress and provenance

**47 distinct Shopify demo stores**, **131 primary indexed HTML page sources**, **43/127 selected preset demo homepages (33.9%)**. Two newly opened primary pages: Horizon /products/1tuck-tapered-pants-424 and Spotlight /cart. One PDP and one **empty** cart are newly added; selected PDP coverage is **35**, selected cart coverage **9**. Count distribution: 47 home, 37 collection, 38 PDP, 9 separately fetched cart page URLs = 131. No new preset home URL was independently verified. Official Theme Store listing research stays at 127/127 but must not be included in demo count.

Two additional **supplementary** collections were retrieved and stored separately under `supplemental_documentation`, excluded from primary one-page-per-type counting. This is especially important for Glimmer: its primary `/collections` URL is a collection-directory page, not a faceted product collection, whereas `/collections/minis` contains actual product filters.

## Individually opened primary pages

| Cohort preset | Source URL | Document observations | Indexed crawl |
|---|---|---|---|
| Horizon | https://theme-horizon-demo.myshopify.com/products/1tuck-tapered-pants-424 | Six gallery images and size options XS–XXL, product description, demo disclaimer, Add to cart markup; no size-change/cart click | ~2 weeks |
| Spotlight | https://theme-spotlight-demo.myshopify.com/cart | Real separate /cart URL says empty, has $0.00 CAD subtotal, continue shopping, shipping/taxes copy; success modal string exists in shared markup but click not tested | ~7 months |

## Supplementary source (not a new primary preset document)

| Preset | Source | Evidence |
|---|---|---|
| Stiletto Glimmer | https://stiletto-theme-glimmer.myshopify.com/collections/minis | Read-only 27-result Minis + Kits category HTML; product type, skin type, price, availability and 60/80/120-ml size facets; indexed ~2 months ago |
| Pitch | https://theme-pitch-demo.myshopify.com/collections/bundles | Read-only three skincare bundle products and sale/compare-at price markup, plus sorting and availability/price filters; no bundle cart action |

For Glimmer, the indexed collection shows 27 results plus overlapping in-stock (27) and out-of-stock (3) facet label counts. Without running a filter or knowing exact underlying product scope, this is a **copy/logic test case, not an established runtime bug**. Spotlight source includes an “Item added to your cart” modal even though its separate `/cart` page is empty — **hidden alternate markup is not an executed add-to-cart test**.

## Research-bank changes

- 3 source-mapped, original systems/design patterns for native product variants, truthful empty carts, and separate collection index vs filtered product grid.
- 3 explicit document-only source claim guardrails in `shopify-source-claims-batch13-2026.json`.
- Source-linked updates to Horizon and Spotlight general audits, plus qualitative design observations; two supplementary store sources.
- Extended `shopify_editor_audit.py` historical gates for 131 primary documents, 38 PDPs and 9 opened cart URLs, with source IDs and crawl labels.
- Other newly revisited official pages (Impulse Terrain, Impact Cocoon, Enterprise Homestead and Savor) are **listing or vendor documentation**, not newly retrieved sample storefronts. In Impulse v10.0.0 release notes the vendor mentions 2,048 variants and a specific size chart behavior. These remain vendor documentation, not runtime VSN/competitor QA: https://help.archetypethemes.co/hc/en-us/articles/46027069235091-Impulse-release-notes.

## Explicit limitations / next actions

Read-only public **indexed HTML only**, not a live browser session: no real add-to-cart, filter click, variant switching, checkout, Lighthouse/device/mobile screenshots, keyboard checks or private Theme Editor. Failed URL fetches and invented guessed storefront names never count. Stay at Stage 2 Research and 43/127 selected home sources; continue 84 unvisited preset home demo sources when actually accessible, then deeper PDP/cart state verification. Superseded Figma is historical; no theme code or Figma design changes.
