# Prototype — VSN element system (2026-10-22)

## Built (theme/)
| Piece | File | Proves |
|---|---|---|
| Design tokens (colors, fonts, radius, motion) | `snippets/vsn-tokens.liquid`, theme settings "VSN design tokens" | Layer 1 tokens → CSS custom properties |
| Element defaults | theme settings "VSN element defaults" | Layer 2: one place sets the default variation for all headings/buttons/cards |
| Smart responsive | `snippets/vsn-responsive.liquid` | 3 anchors (1440/768/360) interpolated; 6 hidden overrides only when Advanced is on |
| Heading | `blocks/vsn-heading.liquid` | Variations display/outline/gradient/marker, fluid size, responsive alignment |
| Button | `blocks/vsn-button.liquid` | Variations solid/ghost/brutal/glass, responsive height, full width per device |
| Product card | `blocks/vsn-product-card.liquid` | Variations overlay/minimal/detailed, real sale %/sold-out badges, sizes, wishlist/compare/quick view hooks |
| Group | `blocks/vsn-group.liquid` | Nestable container (any theme block), grid columns / flex direction per device |
| Global component | `blocks/vsn-global-component.liquid` + theme settings "VSN global components" | Layer 4: synced content, per-instance overrides (blank = shared) |
| Section | `sections/vsn-section.liquid` | Holds any theme block, responsive padding |
| Demo page | `templates/page.vsn-prototype.json` | A page built only from elements + settings |
| Generator | `scripts/gen_vsn_blocks.py` | Every element gets the same schema standard (variation, responsive, simple mode, advanced) |

`visible_if` hides design controls in **Simple mode** and shows per-breakpoint overrides only when
**Advanced responsive** is on.

## Tests
- Theme Check (`node tools/theme-check.js`, theme-check:recommended): **0 offenses**.
- Responsive math (snippet rendered with LiquidJS, measured in Chromium):

| Width | Advanced on (2448=140, 320=36) | Advanced off |
|---|---|---|
| 2448 | 140px | 96px |
| 1920 | 96px | 96px |
| 1440 | 96px | 96px |
| 1024 | 76.19px | 76.19px |
| 768 | 64px | 64px |
| 560 | 53.80px | 53.80px |
| 480 | 49.88px | 49.88px |
| 360 | 44px | 44px |
| 320 | 36px | 44px |

- Visual harness at 1440 / 768 / 360: no clipping, no text overflow (rule 14). Two issues found and fixed:
  global component heading overflowing its box (now container-query sized) and brutal button shadow
  leaving the screen on mobile.

## Not tested yet (needs a Shopify development store)
- Real rendering in the theme editor (`shopify theme dev`), drag and drop, `visible_if` behaviour,
  nested block limits in practice, product data in cards, font loading via `font_face`.
- Next: connect a dev store (store URL + `shopify theme dev` login by the team), then test in the editor.
