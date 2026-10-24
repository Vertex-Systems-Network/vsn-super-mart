# Prompt — Stage 2: Niche research (Research Bank)

Goal: turn `banks/research/niches/<niche>.json` from `seed` into `verified`.

1. Read the niche file, `banks/research/competitors/themes.json`, `demo-audit.json`, `cross-platform-patterns.json`, and the brief. Run `python3 scripts/vsn.py competitor-audit summary` and `python3 scripts/vsn.py competitor-audit next`.
2. Research (web search + fetch real pages; one sub-agent per angle is fine):
   - Open each *individual* selected official preset listing and its live demo, then relevant home, collection, PDP, cart and mobile page variants. Record URL/date/verified scope per page; separate vendor claims from independently inspected UI.
   - Cover Shopify, WooCommerce, BigCommerce and Magento where relevant; translate findings into Shopify-native, free Shopify app, VSN app, or unsupported-with-reason mappings.
   - Add newly discovered competitors to the audit backlog rather than claiming unvisited demos are verified.
   - 5+ top real Shopify stores in this niche: which sections, product page elements, filters, metafields.
   - Niche conversion drivers and anti-patterns.
3. Update the file: add/adjust `must_have_sections`, `nice_to_have_sections`, elements, metafields,
   `design_patterns`, `competitor_references` (with demo URLs), `sources` (only URLs you actually opened).
   Keep sourced data; only replace with a newer/better source. Paraphrase, no long quotes.
4. Set `"status": "verified"`, update `verification` with what you checked, update `index.json` counts.
5. Update individual entries in `demo-audit.json`, map reusable findings to `cross-platform-patterns.json`, add genuinely missing features to Options Bank with citations; qualitative design notes go to `competitor-observations.json`.
6. `python3 scripts/competitor_audit.py validate`, `vsn.py validate`, `vsn.py log`, `vsn.py advance`.
