# Prompt — Stage 5: Design spec

1. Copy `ai/templates/design-spec.json` to `banks/design/specs/<niche>/spec.json`; take `fp` + palette from
   the chosen direction.
2. Fill tokens, every template's section list, every section (blocks, settings, variants, states,
   responsive, a11y).
3. Fill `option_map` for every id in `ai/niches/<niche>/options.resolved.json` → `must` (and should where
   included) and `requirement_map` for every id in `banks/research/platform/theme-store-requirements.json`.
4. Loop: `vsn.py coverage <spec>` and `vsn.py check-design <spec>` until both pass. Then `vsn.py advance`.
