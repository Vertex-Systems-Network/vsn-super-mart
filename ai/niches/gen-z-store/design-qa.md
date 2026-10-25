# Design QA — Afterhours (gen-z-store) — 2026-10-21

Scope: 24 screens on Figma page "VSN | Super Mart" (frame ids in spec → figma.frames).
Method: screenshot review of every screen + automated clipping audit (`scripts/figma-qa-clipping.js`)
+ local browser clipping/wrapping check of the source HTML.

## Issues found and fixed
| # | Issue | Fix |
|---|---|---|
| 1 | Ticker said Drop 07 arrives "Fri 24 Oct" while hero said "out now" | Ticker: Drop 07 out now, Drop 08 Fri 06 Nov |
| 2 | Wrong weekdays (26 Oct is Mon, 07 Nov is Sat, 24 Oct is Sat) | Sun 25 Oct, Fri 06 Nov everywhere |
| 3 | Wishlist count 3 vs 4; cart page Bag (3) with header 2 | Counts consistent (4 / 3) |
| 4 | Runner 02 €182 in some places, €260 in others | Sale price + compare-at everywhere |
| 5 | Sold-out Boxy tee recommended in upsells | Replaced with Zip hoodie |
| 6 | "Hoodie" search showed jacket and tee | Hoodie-related results + journal result |
| 7 | Hero paragraph over the model | Copy moved under the headline, left gradient |
| 8 | Compare bar covered footer | Footer spacer |
| 9 | Empty page behind cart drawer and quick view | Product grid behind the overlay |
| 10 | Lookbook hotspot on a face | Hotspots on jacket and cargo |
| 11 | Outline marquee missing / cut off | Restored, fits the screen |
| 12 | Payment icons 9px | 11px, larger badges |
| 13 | Filled heart rendered as a blob | Proper heart path |
| 14 | Gift card QR was a blank square | QR pattern |
| 15 | Mobile header had no wishlist (rule 12) | Heart added |
| 16 | Same image twice on Home and All collections | Different images per page |
| 17 | No reviews on product page | Rating summary + reviews section |
| 18 | No notify-me for sold-out sizes | Notify link |
| 19 | Gift card page too plain (rule 11) | Textured background + offset card |
| 20 | Mobile sale banner wrong date | Fixed |
| 21 | 203 icons cut by their frames (rule 14) | Icons scaled inside frames |
| 22 | Ticker text cut at right edge | Ticker fits, centered |
| 23 | 1–4 px bottom cuts on several screens | Frames fitted to content |
| 24 | "Copy link" wrapped to two lines | No-wrap chips |
| 25 | "40%" on lime light beam, low contrast | Stronger overlay |

Added (rule 13): share buttons on product, quick view, mobile product and article; "From the journal" on home.

## Result
- Clipping audit: **0** cut icons/images/texts/elements on all 24 screens.
- Coverage: options and requirements PASS (see `vsn.py coverage`).

## Still open
- Images below Full HD — waiting for Figma AI credit reset (2026-11-04).
- Lookbook image has a small "D14" level marking on a pillar (fix when regenerating images).
- Human design approval.

## Recovery warning (2026-10-25)
This QA report describes the former 2026-10-21 Figma canvas only. That canvas is unavailable. Its previous clipping audit must NOT be used as a passing result for any reconstructed visuals; fresh visual QA is needed.

## 2026-10-25 — new Figma restoration verification (not final visual QA)

Target file `y5e3fEpx2eAFhLRFLisP0o`, page `0:1` contains 24/24 named restored frames: 19 desktop and 5 mobile, including 641 editable native text nodes. Native layout shapes/frames exist; this is not a screenshot paste. Home mobile screenshot inspected. Original Figma photos are replaced by visible neutral placeholders; the appearance is source-guided and cannot be declared pixel-identical to lost original. Figma Starter tool quota stopped further screen-by-screen visual QA. **Do not reuse the old clipping audit or approve stage 6 yet.**
