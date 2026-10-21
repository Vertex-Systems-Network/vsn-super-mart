# Prompt — Stage 3: Options mapping (Options Bank)

1. Run `vsn.py resolve-options <niche>`. It lists research must-have sections with no option id.
2. For each unmapped section either add a new option to `banks/options/options.json`
   (id, name, audience [shopper|merchant|developer], area, priority, scope, store_allowed,
   theme_store_required, source) or map it to an existing option in the research file's
   `"option_map": {"<section-id>": "<option-id>"}`.
3. Anything a Theme Store theme may not include (wishlist, countdown, Instagram feed, fake urgency)
   gets `store_allowed: false`.
4. Re-run until no unmapped sections remain, then `vsn.py advance`.
