# Research Bank

Stores everything learned about the platform, competitors and each niche. Agents **read before designing**
and **write every new finding here with a source**.

```
platform/theme-store-requirements.json   Shopify Theme Store rules as a checklist (req-* ids)
competitors/themes.json                  popular themes, presets, positioning, market insights
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
