# Session handoff

_Update at the end of every session (even mid-task). Newest entry on top._

## 2026-10-21 — All Afterhours screens built + rule 12

**Done**
- Rule 12: every demo has quick view, wishlist, compare and promotions (wishlist/compare UI in theme, data
  from planned `vsn-wishlist-compare` VSN app because Theme Store forbids theme-built wishlist).
- Figma page 25:2 now has 24 screens (19 desktop, 5 mobile); ids in spec → figma.frames. Coverage
  124/124 options, 39/39 requirements, 19/19 apps.
- Reused existing Figma AI images (no new generations).

**Waiting**
- Full HD images: team decided to wait for Figma AI credit reset (2026-11-04 11:17 UTC). A scheduled
  reminder fires 2026-11-04 11:30 UTC in this session.
- Design approval (`vsn.py approve 6`).

## 2026-10-21 — Gen-Z / Afterhours designed in Figma (Stage 6, gate pending)

**Done**
- Stage 5 spec `banks/design/specs/gen-z-store/spec.json`: 114/114 options, 39/39 requirements, 18/18 apps.
- Figma page "VSN | Super Mart" (25:2): 7 screens — Home, Collection, Product, Cart drawer, Password drop
  (desktop 1440) + Home, Product (mobile 390). Frame ids in spec → figma.frames. Built from
  `banks/design/specs/gen-z-store/source/build.py` via html_to_figma (editable layers).
- 22 Figma AI images (one regenerated) placed into 44 slots; logged in `banks/design/image-log.json`.
- New team rules added: 9 (Full HD images), 10 (never remove a Shopify option; Shopify → free Shopify app →
  VSN app → third party; `banks/options/apps.json`), 11 (no minimalist demos, auto-checked).

**Blockers**
- Images are NOT Full HD (928–1376 px). Figma AI credits ran out; reset 2026-11-04T11:17Z.
  Options: wait and regenerate with a Full HD model, add Figma AI credits, or upscale (needs team approval).
- Stage 6 gate also needs human design approval (`vsn.py approve 6`).

**Next**
- Build remaining screens: search, list collections, page/contact, blog/article, account, 404, gift card,
  cart page, mobile collection/cart. Then Full HD images, approval, Stage 7.
- Confirm the feature lists of the VSN apps (Product Types, Stock Down Sort, Metafields).

## 2026-10-21 — Rule added: images via Figma AI

- All images (designs + demo stores) must be generated with Figma AI (`generate_image`) in the Figma file.
  Added to AGENTS.md (rule 9), CLAUDE.md, WORKFLOW (stages 6 and 9), prompt 6 ("Images"), spec template
  (`image_brief`), new `banks/design/image-log.json`, and `vsn.py validate` checks the log.
- Next is unchanged: Stage 1, ask the first niche.

## 2026-10-21 — Bootstrap (Stage 0) complete

**Done**
- AI workflow: `AGENTS.md`, `CLAUDE.md`, `ai/WORKFLOW.md` (stages 0–9), prompts, templates, slash commands.
- Research Bank: Theme Store requirements checklist, competitor theme list, 14 niche files (status `seed`).
- Options Bank: 156 options (shopper / merchant / developer), with Theme Store flags.
- Design Bank: fingerprint schema, 9 approximate competitor fingerprints, empty registry.
- `scripts/vsn.py`: status / advance / approve / validate / resolve-options / coverage / check-design / register-design.
- Figma checked: page "VSN | Super Mart" (25:2) is empty; brand colors taken from the "Product Types" page.

**Next**
- Stage 1: ask the team which niche goes first (it also builds the core). Suggested: `grocery-supermarket`
  (matches the "Super Mart" name and is the least crowded premium-theme space).

**Open questions**
- Theme Store submission vs. own sales channel? (Theme Store forbids wishlist/countdown/Instagram feed and
  requires exclusivity.)
- Which niches ship in v1 (suggest 3–4)?

**Known gaps**
- Niche files are `seed`: several sources are search-result links not yet opened, and paid-theme preset
  details come from general knowledge. Stage 2 must verify each niche before design.
- Competitor fingerprints are `approx`; verify against live demos in Stage 4.
