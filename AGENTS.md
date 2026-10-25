# AGENTS.md — VSN Super Mart (AI-native Shopify theme)

This file is the **single entry point for any AI agent** (Claude, Codex, Gemini, Cursor, Copilot…) or human
working on this repository. Read it fully before doing anything.

## 1. What we are building

**VSN Super Mart** — a multi-niche Shopify theme (Online Store 2.0, theme blocks) that competes with the
best themes on the market (Prestige, Impulse, Symmetry, Trademark, Broadcast, Horizon family…).

- One codebase, many **presets** (one per niche), each a visually distinct style with its own demo store.
- Every option a **Shopper**, **Merchant (user)** and **Developer** needs (see `banks/options/`).
- Built from **Shopify Skeleton theme or original code only** — never Dawn or Horizon
  (Theme Store rule, see `banks/research/platform/theme-store-requirements.json`).
- **No active Figma design.** User explicitly superseded the old Afterhours restoration (`y5e3fEpx2eAFhLRFLisP0o`) and originally deleted file. Those IDs, palettes, layouts and screenshots are historical references only. Create an entirely fresh design direction **later** after research/options are complete; no current Stage 6 or Figma approval applies.

## 2. Read order (every session)

1. `AGENTS.md` (this file)
2. `ai/state/progress.json` — **where the project stopped** (current stage, niche, next action)
3. `ai/state/HANDOFF.md` — last session's notes, open questions, blockers
4. `ai/WORKFLOW.md` — the stage you are in, its inputs, outputs and exit gate
5. The banks the current stage needs (`banks/research`, `banks/options`, `banks/design`), including demo evidence and cross-platform patterns

Then run: `python3 scripts/vsn.py status` — it prints the stage and the exact next action.

## 3. Resume protocol (pick up exactly where it stopped)

1. Run `python3 scripts/vsn.py status`.
2. Do **only** the `next_action` it prints, inside the current stage. When the user explicitly supersedes an outdated stage/design, reset active state and preserve former assets as archival references; do not force old design restoration.
3. When a step finishes, record it: `python3 scripts/vsn.py log "<what you did>"`.
4. When a stage's exit gate passes, advance: `python3 scripts/vsn.py advance` (it runs the gate check).
5. Before ending a session — even mid-task — update `ai/state/HANDOFF.md`
   (done / in progress / next / blockers) and commit. A session that ends without a handoff is a bug.

Never skip stages. Never start development before the design gate passes.

## 4. Golden rules

1. **Banks first.** Research, options and design decisions are read from and written to the banks.
   Nothing is designed from memory alone. Every new finding is added to the bank with a source.
2. **Ask the niche first.** A design/development cycle always starts by asking (or reading) the target niche.
3. **No repeated design.** Every new design gets a fingerprint in `banks/design/registry.json`.
   `python3 scripts/vsn.py check-design <spec>` must pass (not too similar to any previous VSN design
   or any competitor fingerprint) before the design is accepted.
4. **Full coverage.** Every `must` option for the niche (and every Theme Store requirement) must be
   present in the design spec. `python3 scripts/vsn.py coverage <spec>` must pass.
5. **Theme Store compliance.** No fake urgency/countdowns/stock counters/viewer counts, no app-like
   features (wishlist, booking, Instagram feed) inside the Theme Store build. Such features are tagged
   `store_allowed: false` in the options bank and go only into an optional "VSN apps/extras" track.
6. **Small, verifiable steps.** One work unit per commit. Run `shopify theme check` once theme code exists.
7. **Evidence.** Claims about competitors or the market need a URL in the bank's `sources`.
8. **Language.** Code, file names and bank data in English. Chat with the team may be Urdu/Roman Urdu.
9. **Images are created outside Figma AI, using ChatGPT image generation only, unless the team explicitly changes this policy.**
   Generate original hero, banner, product, collection, lifestyle and blog assets using ChatGPT.
   **Do not spend any Figma AI credits.** Once a NEW Figma file is approved, upload images to that active design using
   Figma's asset upload API (not Figma image generation). **There is no active Figma file yet.**
   - Write distinct prompts from the niche research and selected design tokens. Prefer unique photographs
     and do not assign the same image to unrelated placements; repeated actual SKUs must be explicitly justified.
   - Never copy third-party theme demo imagery, logos, text overlays or identifiable brands.
   - Generated output is not “placed in Figma” until upload response/asset fill is confirmed; preserve
     files in an asset pack with a deterministic slot manifest when Figma API permissions are exhausted.
   - **Full HD policy:** ≥1920 pixels on the longer edge for final editorial assets. Product assets
     need sufficient source resolution for their largest displayed width; do not invent dimensions.
     If a generated image does not meet source resolution, flag for approved upscale/new generation.
   - Log source prompt, generation origin, dimensions, target node, upload state and placement in
     `banks/design/image-log.json`. Old deleted Figma node IDs are historical only.
10. **Never remove a Shopify option — Shopify first, then VSN apps.** Every feature, setting and option that
   Shopify provides (checkout options, discounts, selling plans, markets, filters, metafields/metaobjects,
   gift cards, pickup, Shop Pay, accelerated checkout, customer accounts, etc.) must stay supported and
   usable in the theme — never removed or hidden. For any feature, pick in this order and record it in the
   spec's `app_map`:
   1. native Shopify / theme feature, 2. a free app made by Shopify, 3. a VSN app
   (`VSN | Product Types`, `VSN | Stock Down Sort`, `VSN | Metafields`), 4. a third-party app only when 1–3
   cannot do it (write the reason). The list lives in `banks/options/apps.json`; every app there with a
   `theme_integration` must be supported by the design and the theme.
11. **No minimalist demos.** No preset or demo store may be minimalist (plain white/black, airy empty grids,
   thin minimal cards, no motion, neutral-only palette). Every preset must be bold and expressive with a
   strong accent color, rich sections and motion. `vsn.py check-design` fails any design that shows 3 or
   more minimalism markers (see `banks/design/fingerprint-schema.json → minimalism_markers`).
12. **Every demo has quick view, wishlist, comparison and promotions.** These are mandatory on every preset:
   - **Quick view** (modal from every product card) and **quick add**.
   - **Wishlist** (heart on cards + product page, wishlist page/drawer) and **compare** (compare toggle on
     cards, compare bar, compare page with spec rows). Theme Store forbids building these as theme logic, so
     the theme ships the UI + app block slots and the data comes from a VSN app (`vsn-wishlist-compare`,
     rule 10); outside the Theme Store build they can run as the extras track.
   - **Promotions:** announcement ticker, promo banner section, sale campaign section, promo tile inside
     product grids, sale badges with compare-at price and % off, free shipping bar, promo popup, sale
     collection styling. Only real data — no fake countdowns, stock or urgency (Theme Store rule).
13. **Blog posts and sharing in every design.** Every preset ships the blog listing + article templates and a
   "From the journal" section on the home page, plus share buttons (copy link, WhatsApp, X, Facebook,
   Pinterest, native share on mobile) on every product page, quick view and blog article.
14. **Nothing may be cut.** No icon, image, text or element may be clipped by its container or the screen
   edge (except an image's own intentional crop inside its frame). Marquees/tickers must fit or be shown
   as a static row in the mockup. Every Figma QA runs `scripts/figma-qa-clipping.js` (via `use_figma`) on
   all screens and must return zero cut nodes before a design is shown or approved.
15. **Global element library — demos by settings only.** The theme is a library of global elements
   (`banks/elements/elements.json`): every Elementor Free/Pro widget and the useful third-party Elementor
   addon widgets, upgraded with the options they lack, plus Shopify commerce and creative elements Elementor
   never had. Every element gets the universal setting groups (`universal-settings.json`) and the smart
   responsive system for breakpoints 2448, 1920, 1440, 1024, 768, 560, 480, 360, 320 (`responsive.json`:
   3 visible anchors + calculated values + advanced per-breakpoint overrides). Every demo is built only
   from elements + settings; if a design needs something new, add a new element to the library (never
   one-off code for a single preset). The system merges Elementor and WordPress Gutenberg ideas —
   tokens → element defaults → style variations → global components (synced, any field overridable) →
   instance → responsive overrides → display conditions — see `banks/elements/architecture.md`.
16. **Deploy only through the Shopify GitHub integration.** Code is edited in `theme/` and pushed to GitHub;
   the `shopify-theme` branch (theme at root, kept in sync by GitHub Actions) is connected to the stores.
   Never upload ZIPs or edit in the Shopify code editor; theme editor changes flow back automatically.
   CLI is optional for local preview only. See `docs/adr/0002-deploy-via-shopify-github-integration.md`.

17. **Cross-platform competitive intelligence must be evidence-linked.** Inspect major Shopify, WooCommerce,
    BigCommerce and Magento themes and each selected individual preset/demo. Save source URLs and visit dates
    in `banks/research/competitors/demo-audit.json`; map design/system patterns through
    `cross-platform-patterns.json` into Options and Design banks. **Vendor feature listings are not live
    interaction verification.** Run `python3 scripts/vsn.py competitor-audit validate`. Maintain an explicit
    demo backlog for unvisited sites. Original code, imagery, brand assets and recognizable layouts must
    never be copied. Apply Theme Store policy and app-first architecture to every imported idea.

19. **Shopify theme editor constraints.** Competitor preset listings don't reveal their actual editor settings. Use documented Shopify schema (`blocks/`, `sections/`, `config/`) as capability evidence and stay within hard limits (300 theme-block files, 8 nesting levels, 25 sections per JSON template, 50 blocks per section). Keep 192 conceptual elements distinct from compiled theme block file count. Never claim live competitor editor access without credentials and direct evidence.

18. **Historical Figma concepts:** Never treat superseded Afterhours Figma frame or image IDs as live. The original Python/HTML/slot sources are preserved; use `python3 scripts/afterhours_recovery.py check`. A source-only preview is not a restored editable canvas or recovered photo. Require fresh visual QA and design approval.

## 5. Repository map

```
AGENTS.md                 ← you are here (all AIs)
CLAUDE.md                 ← Claude-specific pointer + commands
ai/
  WORKFLOW.md             ← stages 0–9, inputs/outputs/gates
  state/progress.json     ← machine-readable project state (resume point)
  state/HANDOFF.md        ← human-readable session handoff
  state/log.md            ← append-only activity log
  prompts/                ← ready prompts for each stage (any AI)
  templates/              ← niche brief, design spec, research entry
banks/
  research/               ← RESEARCH BANK: platform rules, competitors, per-niche research
  options/                ← OPTIONS BANK: every feature/option (shopper, merchant, developer)
  design/                 ← DESIGN BANK: design registry, fingerprints, competitor patterns, specs
scripts/vsn.py            ← status / advance / log / validate / coverage / check-design / new-niche
theme/                    ← Shopify theme source (created in stage 7 from Skeleton theme)
.claude/commands/         ← slash commands for Claude Code
```
