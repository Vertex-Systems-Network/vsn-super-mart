# Prompt — Stage 7: Development

1. First cycle only: `shopify theme init theme --clone-url https://github.com/Shopify/skeleton-theme`
   (never Dawn/Horizon). Add `.theme-check.yml`.
2. Write `ai/niches/<niche>/work-units.md` as a checklist (`- [ ] WU-01 ...`), ordered:
   tokens/settings_schema → layout/theme.liquid → section groups (header/footer) → snippets (price,
   product-card, icons, image) → global JS web components (cart, drawer, predictive search, variant picker)
   → sections → templates → listings/<preset> (multi-preset) → locales.
3. Per unit: read spec + Figma frame (`get_design_context`; Claude loads `figma-design-to-code` first),
   implement, `shopify theme check`, commit `WU-xx: <title>`, tick `- [x]`, `vsn.py log`.
4. Rules: native CSS, no Sass, no jQuery, routes object, every setting labeled, sentence case copy,
   responsive images + lazy load, a11y from the start.
5. When all units are ticked: `vsn.py advance`.
