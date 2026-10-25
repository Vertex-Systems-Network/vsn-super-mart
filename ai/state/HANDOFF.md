# Session handoff

_Update at the end of every session (even mid-task). Newest entry on top._

## 2026-10-25 — PR research quality gates and ChatGPT image policy

Added 20 evidence-to-implementation route decisions (Shopify native / original theme component / app block / VSN app), with explicit rule protection for app-only wishlist/compare. Expanded audit validation to require the 5 template-scope states and mapped evidence. Updated AGENTS image policy to use **ChatGPT image generation and Figma asset uploads, never Figma AI credits**, per team's current requirement. Corrected stale README status and Afterhours color references. Source research is ready for infrastructure merge; Stage 6 image placement and approval still pending.


## 2026-10-25 — PR #1 research curated cohort finalized

Added 23 new source-linked pages (Shopify major presets, Porto Grocery 2/3 & Shop 35/Book/Single Product, Astra, Blocksy E-Bike/Kiddy, Kadence directory and BigCommerce Cornerstone Warm). Research cohort now **55 entries**, 14 reusable patterns, 16 qualitative observations, with evidence-level verification and per-template (home/collection/PDP/cart/mobile) gaps. Wrote `banks/research/competitors/research-closeout.md` with implementation route and explicit limitations; updated Oct 19 Koala sample popularity baseline. Source records and mapping validated; no claim of testing every worldwide theme/demo or live cart/checkout. Stage 6 Figma is still not approved.


## 2026-10-25 — RESTORED EDITABLE LAYOUTS IN NEW FIGMA FILE

**Destination:** https://www.figma.com/design/y5e3fEpx2eAFhLRFLisP0o/VSN-Super-Mart?node-id=0-1

Native editable Figma structure rebuilt directly on page `0:1`: **24/24 named screens, 19 desktop + 5 mobile**, **641 editable text layers**. Data/source based reconstruction from saved Afterhours HTML/spec/tokens; restored Figma node IDs in `spec.json → figma.frames` and `ai/recovery/afterhours.json → restored_figma`.

**Quality/evidence:** Figma Plugin API enumerated exact 24 unique screen frames with no missing names and editable frame/text layers. Mobile home screenshot visually checked. Figma Starter MCP call quota reached before complete pixel-level review; final visual QA must be rerun when access available. Source placement and content are approximate **not pixel-identical original files**.

**Still pending:** Original 22 Figma AI image assets remain unavailable; placeholders currently visible. Recreate new original Full HD images, replace placeholders, inspect all 24 layouts and secure team Stage 6 approval. Do not advance stage or claim theme/editor QA passed. The deleted file historical IDs remain historical only.


## 2026-10-25 — Stage 0b element specs prepared during source recovery

Wrote `banks/elements/specs/afterhours-core.json` with detailed behavior/settings/states/a11y for header, mega-menu, product gallery, quick view and cart drawer. Their catalog statuses move `planned` -> `spec` (NOT built). Added `ai/niches/gen-z-store/work-units.md` with explicit unchecked implementation tasks for the eventual Stage 7 after design approval.

## 2026-10-25 — Additional competitive evidence verified

**Research:** Reopened all 15 initial non-Shopify demo homepage/category URLs with public source retrieval (Flatsome, WoodMart, Porto, BigCommerce Cornerstone, Magento Hyva), and recorded document-level verification only. Opened 4 Blocksy official starter preset pages (Modern Shop, Petsy, Book Store Pro, Furniture Pro). Their live starter-domain demos were blocked by HTTP 403 in this environment; they remain official-feature-only, not interactive verified. Expanded demo-audit to 32 entries and patterns to 9, with source-quality flags and backlog.

## 2026-10-25 — Figma original deleted; source-only recovery

**Verified in GitHub:** 24 HTML screen layouts, original Python generator, 108 image placeholder mappings, 22 image prompts. Old Figma file returned edit-access error, and user reported UI permanently deleted. Original Figma images/layers are not recoverable from hashes. Historical frame/image IDs now explicitly marked unavailable; 404 HTML ID aligned with spec.

**Built:** `ai/recovery/afterhours.json` manifest and `scripts/afterhours_recovery.py` check/rebuild/bundle CLI, wired into VSN validation and PR CI with standalone HTML preview artifact. The project is at Stage 6 design recovery, not falsely recorded as Figma completed.

**Pending:** New visual assets and design review, stage 6 approval; Shopify editor preview and full development. Cross-platform competitor research may proceed in parallel.


## 2026-10-25 — RESUMED: cross-platform theme intelligence added to PR #1

**Done:** Added 28 individually referenced source entries (15 live demo pages inspected at document level; 13 Shopify official preset feature pages), spanning Shopify, WooCommerce, BigCommerce and Magento. Evidence levels explicitly distinguish a live page from a vendor listing. Added 8 evidence-to-option design/system patterns, 5 non-duplicative `should/could` options and qualitative competitor observations. Updated workflow, prompts, agent rules, CLI bank validation and audit backlog. Work committed onto the existing `ai-native-workflow` PR #1 branch, not `main`.

**Not done:** No claim that every demo in the marketplaces was opened. Shopify interactive live demo buttons, full mobile/browser testing and all other unvisited demos remain in `demo-audit.json → backlog`. Research does not prove runtime feature compatibility. Do not advance Stage 6 automatically.

**Resume next:** `python3 scripts/vsn.py status` and `python3 scripts/vsn.py competitor-audit next`. Continue demo-level discovery in batches and map resulting patterns to the element library. Stage 6 still needs Full HD images (planned credit reset 2026-11-04), Afterhours human design approval, dev store connectivity and element specs/build; see the 2026-10-22 section below.


## 2026-10-22 — PAUSED by the team ("phir kabhi start karenge"). Full status + how to resume

### Where the project stands
| Track | Status | Key files |
|---|---|---|
| AI workflow + banks | Done (stages 0–9, rules 1–15, vsn.py gates) | `AGENTS.md`, `ai/WORKFLOW.md`, `scripts/vsn.py` |
| Research bank | 15 niches (gen-z-store **verified**, 14 seed) + Theme Store rules + competitors | `banks/research/` |
| Options bank | 160 options + Apps bank (20 Shopify apps, 4 VSN apps incl. planned Wishlist & Compare) | `banks/options/` |
| Design bank | Afterhours registered; fingerprints; minimalism + uniqueness checks | `banks/design/` |
| Gen-Z / Afterhours design | **Stage 6**: 24 screens in Figma page 25:2, QA done (25 fixes, clipping audit 0) | `banks/design/specs/gen-z-store/`, `ai/niches/gen-z-store/design-qa.md` |
| Element library (rule 15) | 192 elements catalogued (Elementor free/pro, 8 third-party addons, Gutenberg core, Shopify, creative); universal settings; smart responsive; Elementor + Gutenberg merged architecture | `banks/elements/` |
| Theme prototype | Skeleton base + VSN sections; tokens, element defaults, smart responsive, Heading/Button/Product card/Group/Global component; Theme Check 0; responsive verified at 9 widths | `theme/`, `docs/prototype-element-system.md`, `docs/adr/0001-*` |

### Team rules added in this period (see AGENTS.md)
9 Figma AI images, Full HD · 10 never remove a Shopify option; Shopify → free Shopify app → VSN app ·
11 no minimalist demos · 12 quick view, wishlist, compare, promotions on every demo · 13 blog posts +
sharing in every design · 14 nothing may be cut (clipping audit = 0) · 15 global element library,
demos by settings only, smart responsive 2448–320, Elementor + Gutenberg merged.

### Open items when we restart (in order)
1. **Full HD images** — Figma AI credits reset 2026-11-04 11:17 UTC (a reminder is scheduled in the original
   session for 11:30 UTC). Regenerate the 22 images in Full HD, swap hashes on the 24 screens
   (`banks/design/specs/gen-z-store/source/hashes.json`, `slots.json`), fix lookbook "D14" marking, update
   `banks/design/image-log.json` (width/height/full_hd), re-run the clipping audit.
2. **Design approval** of Afterhours by the team → `vsn.py approve 6 "<name>"` → `vsn.py advance` (Stage 7).
3. **Shopify development store via GitHub integration (team decision, rule 16)** — merge PR #1 into `main`,
   run the "Theme → shopify-theme branch" workflow once, install the Shopify GitHub app for the org, then in
   the dev store connect repo `vsn-super-mart` branch `shopify-theme` (steps in ADR 0002). Then test the
   prototype in the real theme editor (drag and drop, `visible_if`, nested blocks, real products).
4. **Element specs** — write full settings for each element (start with those used by Afterhours), then build
   them with `scripts/gen_vsn_blocks.py` (Stage 0b / Stage 7, core cycle).
5. Confirm VSN app feature lists (Product Types, Stock Down Sort, Metafields) and decide on the planned
   `VSN | Wishlist & Compare` app.
6. Open questions from the brief: liked/disliked brands, deadline, Theme Store vs own channel.

### How to resume
`python3 scripts/vsn.py status` → read this file → open the prompt for the current stage in `ai/prompts/`.
Tools: `node tools/theme-check.js` (Theme Check), `tools/liquid-render.js` (render Liquid snippets for tests),
`scripts/figma-qa-clipping.js` (Figma clipping audit), `scripts/gen_vsn_blocks.py` (element generator).

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
