# VSN Super Mart — AI-native Design + Development Workflow

The project runs in **niche cycles**. Stage 0 happens once. Stages 1–9 repeat for every niche (preset).
The first cycle also builds the **core** (design system, all shared sections, all templates);
later cycles add a new **preset** (style + listing templates + niche sections) on top of the core.

```
 [0 Bootstrap] ─► [1 Niche intake] ─► [2 Research] ─► [3 Options] ─► [4 Design search & direction]
                        ▲                                                         │
                        │                                                         ▼
 [9 Release preset] ◄─ [8 QA] ◄─ [7 Development] ◄─ [6 Figma build] ◄─ [5 Design spec]
```

State lives in `ai/state/progress.json`. Use `python3 scripts/vsn.py status | advance | log`.
Each stage below lists **Reads → Does → Writes → Exit gate**. `advance` checks the gate automatically
where it can; human gates (🧑) need a recorded approval: `python3 scripts/vsn.py approve <stage> "<who>"`.

---

## Stage 0 — Bootstrap (once)
- **Reads:** nothing.
- **Does:** create banks, platform rules (Theme Store requirements), competitor theme list, core options.
- **Writes:** `banks/research/platform/*`, `banks/research/competitors/themes.json`, `banks/options/options.json`.
- **Exit gate:** `vsn.py validate` passes.

## Stage 0b — Element library (core, rule 15)
- **Reads:** `banks/elements/*`.
- **Does:** keep the element catalog complete (Elementor + third-party addons + Shopify + creative), write
  each element's settings spec, then build elements in Stage 7 of the first cycle before any preset work.
- **Exit gate:** `vsn.py validate` passes (element ids unique, every element has category/source/settings).

## Stage 1 — Niche intake
- **Reads:** `banks/research/niches/` (what already exists), `progress.json.completed_niches`.
- **Does:** **ASK the human which niche** (offer the list from `banks/research/niches/index.json`, mark
  ones already shipped). Ask: target market/region, catalog size, price level, brand mood, must-have ideas,
  references they like/dislike. Do not assume.
- **Writes:** `ai/niches/<niche>/brief.md` from `ai/templates/niche-brief.md`;
  `vsn.py set-niche <niche>`.
- **Exit gate:** brief exists and has no empty required fields.

## Stage 2 — Niche research (Research Bank)
- **Reads:** `banks/research/niches/<niche>.json` if present, competitor list.
- **Does:** search the web and competitor themes/presets/demo stores for the niche. Collect must-have and
  nice-to-have sections, product/collection elements, metafields, design patterns, conversion drivers,
  anti-patterns. Fill gaps only — never overwrite sourced data without a newer source.
- **Writes:** `banks/research/niches/<niche>.json` (schema: `banks/research/README.md`), index update.
- **Exit gate:** ≥10 must-have sections, ≥3 sources, ≥3 competitor references (`vsn.py validate`).

## Stage 3 — Options mapping (Options Bank)
- **Reads:** `banks/options/options.json`, niche research.
- **Does:** add any new option found in research to the options bank (with audience, area, priority,
  `store_allowed`). Resolve the option list for this niche: all `core` options + options tagged for the niche.
- **Writes:** `banks/options/options.json` (new entries), `ai/niches/<niche>/options.resolved.json`
  via `vsn.py resolve-options <niche>`.
- **Rule 12 check:** quick view, wishlist, compare and promotions options must be in every preset.
- **App-first check:** for every option decide native → Shopify free app → VSN app → third party
  (`banks/options/apps.json`). Never drop a Shopify option.
- **Exit gate:** resolved file exists; every niche must-have section maps to an option id.

## Stage 4 — Design search & direction (Design Bank) 🧑
- **Reads:** `banks/design/registry.json` (all previous VSN designs), `banks/design/competitor-fingerprints.json`,
  niche `design_patterns`, brief.
- **Does:** design search — look at what competitors and previous VSN presets already look like. Propose
  **3 distinct directions**, each as a fingerprint (header, hero, product card, PDP layout, grid, nav,
  type pairing, palette, radius, density, motion, imagery). Run `vsn.py check-design` on each; drop/rework
  any that fail. Present the passing directions to the human with a short moodboard description.
- **Writes:** `banks/design/specs/<niche>/directions.json`.
- **Exit gate:** 🧑 human picks one direction (`vsn.py approve 4 "<name>"`), and it passes `check-design`.

## Stage 5 — Design spec
- **Reads:** chosen direction, `options.resolved.json`, `banks/design/README.md` (spec schema).
- **Does:** write the full spec: tokens (colors, type scale, spacing, radius, shadows), every template's
  section list, every section's blocks/settings/variants/states (empty, loading, error, sold out, sale),
  responsive rules, accessibility notes. Map every option id to where it appears. List the element ids
  used (`elements_used`) — designs may only use elements from `banks/elements/elements.json`.
- **Writes:** `banks/design/specs/<niche>/spec.json`.
- **Exit gate:** `vsn.py coverage banks/design/specs/<niche>/spec.json` passes (100% of `must` options and
  Theme Store requirements), every app in `banks/options/apps.json` that has a `theme_integration` is in the
  spec's `app_map`, **and** `vsn.py check-design` still passes.

## Stage 6 — Figma build 🧑
- **Reads:** spec.
- **Does:** build in Figma page "VSN | Super Mart" (`25:2`): foundations (variables/tokens), components
  with variants, then desktop + mobile frames for home, collection, product, cart drawer + page, search,
  account, blog/article, 404, password, gift card. Use real-looking content, never lorem ipsum.
- **Images:** all imagery is generated with **Figma AI** (`generate_image`) inside the Figma file, from an
  image brief built from the niche research + chosen direction, Full HD minimum (≥1920 px long edge). Placeholders first, then fill them by
  `nodeId`. Each image is logged in `banks/design/image-log.json`. No stock or copied images.
- **Writes:** register design: `vsn.py register-design <spec>` (stores fingerprint + Figma node ids in
  `banks/design/registry.json`).
- **Exit gate:** 🧑 design approval (`vsn.py approve 6 "<name>"`), and `vsn.py validate` passes
  (image log complete).

## Stage 7 — Development
- **Reads:** spec, Figma (via `get_design_context`), options resolved.
- **Does:** first cycle: create `theme/` from Shopify Skeleton theme (`shopify theme init`), build tokens →
  settings_schema → layout → section groups → snippets → sections → templates. Later cycles: add the preset
  (`theme/listings/<preset>/`) + new niche sections. Break into work units in
  `ai/niches/<niche>/work-units.md`; one unit per commit; tick it off.
- **Writes:** `theme/**`, work units file.
- **Deploy (rule 16):** push to GitHub → Action publishes `theme/` to branch `shopify-theme` → connected dev
  store updates; share the store's theme preview link for review. Theme editor edits come back to `theme/`.
- **Exit gate:** all work units done; Theme Check (`node tools/theme-check.js`) has no errors.

## Stage 8 — QA
- **Does:** Theme Store checklist (`banks/research/platform/theme-store-requirements.json`), Lighthouse
  (perf ≥ 60, a11y ≥ 90 avg on home/collection/product, desktop+mobile), keyboard + contrast, browsers,
  editor preview of every setting, real-content demo.
- **Writes:** `ai/niches/<niche>/qa-report.md`.
- **Exit gate:** no open blockers in the QA report.

## Stage 9 — Release preset 🧑
- **Does:** finalize preset name (1–2 words, unique, not an industry word), demo store content (images are the
  Figma AI images from `image-log.json`, exported from Figma and uploaded to the demo store — not bundled
  in `theme/assets`), docs/FAQ
  entries, release notes, version bump.
- **Writes:** `progress.json.completed_niches += niche`, `CHANGELOG.md`.
- **Exit gate:** 🧑 release approval. Then loop to Stage 1 for the next niche.

---

## Working with several AIs at once
- Research for different niches can run in parallel (one agent per niche) — each writes only its own
  `banks/research/niches/<niche>.json`.
- Only one agent edits `progress.json` / `options.json` / `registry.json` at a time (the lead agent).
- Development work units can run in parallel in separate git branches/worktrees; the lead merges.
