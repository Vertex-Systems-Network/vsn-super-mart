# Prompt — Stage 2: Niche research (Research Bank)

Goal: turn `banks/research/niches/<niche>.json` from `seed` into `verified`.

1. Read the niche file, `banks/research/competitors/themes.json`, and the brief.
2. Research (web search + fetch real pages; one sub-agent per angle is fine):
   - Theme Store pages and live demo stores of competitor themes/presets used for this niche.
   - 5+ top real Shopify stores in this niche: which sections, product page elements, filters, metafields.
   - Niche conversion drivers and anti-patterns.
3. Update the file: add/adjust `must_have_sections`, `nice_to_have_sections`, elements, metafields,
   `design_patterns`, `competitor_references` (with demo URLs), `sources` (only URLs you actually opened).
   Keep sourced data; only replace with a newer/better source. Paraphrase, no long quotes.
4. Set `"status": "verified"`, update `verification` with what you checked, update `index.json` counts.
5. `vsn.py validate`, `vsn.py log`, `vsn.py advance`.
