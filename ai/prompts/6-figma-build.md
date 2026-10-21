# Prompt — Stage 6: Figma build

Target: Figma file `BxJuIRth8k4cCUbFnPV6ek`, page "VSN | Super Mart" (`25:2`).
(Claude: load the `figma-use` skill before every `use_figma` call.)

Order: 1) Variables (color schemes, type, spacing, radius) 2) Components with variants (buttons, inputs,
badges, swatches, product card variants, price, rating, header, footer, drawer, modal) 3) Desktop 1440 +
mobile 390 frames for: home, collection, product, cart drawer, cart page, search + predictive search,
list collections, page, contact, blog, article, account (login/register/orders), 404, password, gift card.
4) Empty/sale/sold-out/loading states. Real content only.

Write the frame node ids into `spec.json → figma.frames`, run `vsn.py register-design <spec>`, ask for
approval, `vsn.py approve 6 "<name>"`, `vsn.py advance`.

## Images (Figma AI only)

All imagery is generated with Figma AI — `generate_image` on the Figma MCP — straight into the Figma file.
No stock photos, no images taken from other websites. Each call spends Figma AI credits.

1. **Image brief first.** Add `image_brief` to `spec.json`: for each slot (hero, banner, collection tile,
   product shot, lifestyle, blog cover, empty state) give purpose, aspect ratio, subject, and the shared
   style line (from the chosen direction: mood, palette hex, lighting, `imagery` value such as
   `cutout-on-color` or `lifestyle`).
2. **Placeholders.** Build frames with empty image placeholders at the right sizes.
3. **Generate.** `generate_image` with `fileKey` = `BxJuIRth8k4cCUbFnPV6ek`, the placeholder's `nodeId`
   (replaces the fill without resizing), `width`/`height` for the ratio (max 2048), and a prompt =
   subject + style line + "no text, no logos, no watermark, no recognizable people".
   - Draft / bulk product shots: `gemini-3.1-flash-lite-image` (default, cheapest).
   - Final hero and key lifestyle shots: `gemini-3.1-flash-image` or `gpt-image-2.5-sunburst`.
   - **Full HD:** final images need ≥1920 px on the long edge. Check `image.width/height` in the result;
     if smaller, mark `full_hd: false` in the log and regenerate with a Full HD model or upscale.
   - Keep one style line per preset so every image in the preset looks like one shoot.
4. **Review.** Look at the returned thumbnail. Regenerate only if it is off-brief (wrong subject, baked-in
   text, artifacts, off-palette) — note the reason in the log.
5. **Log.** Append each image to `banks/design/image-log.json`.
6. **Reuse.** Before generating, search the log for an image that already fits (same niche/slot) and reuse
   it instead of paying for a new one.

## QA before showing the design (rules 11–14)
1. `scripts/figma-qa-clipping.js` via `use_figma` → must return zero cut nodes.
2. Screenshot every screen; check: content consistency (dates + weekdays, prices, sale prices, counts,
   stock states), no sold-out item recommended, no image used twice on one page, no text over busy image
   areas, hotspots on products, quick view + wishlist + compare + promotions + blog + sharing present.
