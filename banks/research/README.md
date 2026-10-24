# Research Bank

Stores everything learned about the platform, competitors and each niche. Agents **read before designing**
and **write every new finding here with a source**.

```
platform/theme-store-requirements.json   Shopify Theme Store rules as a checklist (req-* ids)
competitors/themes.json                  popular themes, presets, positioning, market insights
competitors/demo-audit.json               individual opened demo/preset URLs with evidence levels
competitors/cross-platform-patterns.json  source-linked patterns mapped to VSN option IDs
niches/index.json                        list of niches + status (seed | verified) + counts
niches/<niche-id>.json                   one file per niche (schema below)
```

## Niche file schema
| key | meaning |
|---|---|
| id, name, aliases | identity |
| status | `seed` (initial, partly unverified) → `verified` (Stage 2 done with real sources) |
| shopper_profile, catalog_traits | who buys, catalog size / variants / price range |
| must_have_sections / nice_to_have_sections | `{id, name, page, why}` |
| product_page_elements, collection_page_elements | element lists |
| metafields_metaobjects | custom data the niche needs |
| design_patterns | typography, color_mood, imagery, layout, motion |
| conversion_drivers, anti_patterns | what sells / what to avoid |
| competitor_references | `{theme, preset_or_style, notable}` |
| option_map (optional) | `{section-id: option-id}` when a section maps to a differently named option |
| sources | `{title, url}` — only pages actually seen |

Rules: paraphrase (no long quotes), never delete sourced data without a newer source, one agent per niche file.

## Competitive demo research
Run `python3 scripts/competitor_audit.py validate` or `python3 scripts/vsn.py competitor-audit summary` before using cross-platform findings.

- `official_preset_page`: official product/preset listing opened; vendor features are claims, **not** interactive demo verification.
- `live_demo_page`: the individual demo page was opened and its visible document inspected; mobile layout, interactions and checkout are **not** tested by this alone.
- Every entry has source URL, date, platform, theme + preset, mapped option IDs and qualitative design signals; patterns cite entry IDs.
- Transfer **ideas**, not copyrighted code, images, brands, or pixel-identical designs. WooCommerce/Magento/BigCommerce features require a separate Shopify capability and Theme Store compliance check.
- The `backlog` is explicitly unvisited research. Do not claim that the entire theme marketplace has been inspected.
