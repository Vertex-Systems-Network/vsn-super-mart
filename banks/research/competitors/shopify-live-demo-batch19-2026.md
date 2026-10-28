# Shopify indexed demo research — Batch 19: Release Serenity (2026-10-25)

## 1. Verified source and provenance

Found and separately indexed the Release **Serenity** theme's actual public Shopify demo homepage, identified as **“Serenity Theme - DigiFist”**. [Official Shopify Serenity preset listing](https://themes.shopify.com/themes/release/presets/serenity) establishes its identity within Release by DigiFist. The direct storefront HTML had been crawled **last month** (not browser-rendered at research time). This is the independently opened public indexed document: https://release-serenity.myshopify.com/.

Also retrieved a **supplementary FAQ page** https://release-serenity.myshopify.com/pages/faq (indexed crawl last month). It is in `supplemental_documentation`, **not a primary collection/PDP/cart**, and therefore does not increase the four-template demo document count.

| Source | Scope | Indexed crawl age | Verified HTML signals |
|---|---|---|---|
| https://release-serenity.myshopify.com/ | **Selected Release/Serenity homepage** | Last month | Editorial handbags, separate grey/orange/peach/pink/white Amanda Bag product cards, pink Pre-order badge, shop-the-look sets for Anna/Luna/Amanda, journal/blog, newsletter, before/after editorial content, customer comments |
| https://release-serenity.myshopify.com/pages/faq | **Supplementary FAQ**, excluded from primary page totals | Last month | Returns within 30 days and refund-processing within 14 business days after received return; account and tracking FAQ (unverified sample seller policy) |
| https://themes.shopify.com/themes/release/presets/serenity | Official **Theme Store listing only**, already in 127 verified listings | Crawled last month | Confirms DigiFist Release preset identity; vendor feature catalog is not live interaction testing |

The homepage has product links and card markup but this session **did not** independently retrieve its collection, PDP or standalone cart pages, so all three remain unverified.

## 2. Original VSN global element/system implications

- **Cross-product colors vs actual variants:** Amanda Bag Grey, Orange, Peach, Pink and White are shown as separate source product cards; this does not establish shared variant IDs, linked-product strategy or a working color-switch action. Global product cards should support Shopify variant values and optionally product-group sibling linking as *different* data sources.
- **Merchant-composable premium editorial:** source structure combines bestsellers, collection group, shop-the-look product trio, image/editorial storytelling, April 2024 blog entries, FAQ and testimonials. VSN can use original global sections, settings and product references without copying the store's exact visual composition, product photos or copy.
- **Trust policies and testimonial relevance:** sample store identifies handbag products while a testimonial mentions “Leo Bikini Bottoms.” It also markets eco-friendly luxury, lifetime warranty and exclusive designs. These are seller demo-content text snippets, **not verified feedback, product certification or merchant warranty rights**. VSN must never populate such claims as default theme content.
- **Before/after content:** an “Image after” label is present in the indexed homepage text; no evidence that an accessible draggable before/after slider actually works. The dedicated original slider gap from Batch 14 remains pending.

Mapped three evidence-linked original design/system patterns to known VSN option IDs, added one independent qualitative observation and **four** source-specific merchant data integrity checks in `shopify-source-claims-batch19-2026.json`. All remain Stage 2 research only.

## 3. Updated progress: only direct, independently indexed page URLs

The newly opened Serenity home yields **48/127 selected Shopify preset demo homepages = 37.8%** and **79 pending**. Distinct sample demo stores **52**, primary HTML documents **144** (52 home + 40 collection + 41 PDP + 11 separate cart). Selected cohort deeper coverage stays **36/127 collection, 38/127 PDP, 11/127 cart**, because only the homepage was added. These numbers explicitly **exclude** Serenity's FAQ and Shopify official listing.

No variant/cart/checkout/FAQ accordion clicks, mobile/device screenshots, accessibility/Lighthouse, current inventory/warranty validation, or private Theme Editor settings were inspected. Public cached HTML from last month is not real-time stock, pricing, runtime or user-review verification.

**Next:** Independently fetch 79 remaining preset home demos and deeper selected collection/PDP/cart URLs. Preserve data provenance and do not convert third-party/reviewer/vendor feature listings into clicked shopper journeys. PR #9 research only; Stage 2 active, old Figma archived and no theme implementation.
