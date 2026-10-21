# Prompt — Stage 8: QA

Write `ai/niches/<niche>/qa-report.md`. Prefix any failing item with `BLOCKER:` (the gate fails while one
exists). Check:
- Every item in `banks/research/platform/theme-store-requirements.json` (pass/fail + evidence).
- `shopify theme check` clean.
- Lighthouse home/collection/product, desktop + mobile: performance avg ≥ 60 (target 85), a11y ≥ 90.
- Keyboard-only walkthrough, focus visible, contrast, 24px targets, screen-reader labels.
- Browsers + Instagram/Facebook/Pinterest webviews.
- Every setting visible in the editor preview; every option in `option_map` actually works.
- Demo content is real; no apps; no fake urgency.
- Figma design QA: run `scripts/figma-qa-clipping.js` with `use_figma` on every screen — zero cut icons,
  images, texts or elements (rule 14). Also check dates/weekdays, prices, counts and stock states are
  consistent across all screens, and that no sold-out product is recommended.
Then `vsn.py advance`.
