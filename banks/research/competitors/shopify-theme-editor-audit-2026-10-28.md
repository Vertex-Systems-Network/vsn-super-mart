# Shopify Theme Editor Audit — VSN Prototype and 127-Preset Access Boundary

Updated 2026-10-28. This is a read-only static review of the VSN prototype theme files plus an access check against the current research scope. No Shopify admin/editor session was available, so no live Theme Editor interaction is claimed.

## Status

- **VSN prototype schema review:** complete (static source review).
- **VSN live Theme Editor preview:** not verified.
- **Competitor private Theme Editors:** 0/127 reviewed; 127/127 remain pending in the canonical matrix.
- **Theme code changed:** no.
- **Stage:** 2 — Shopify live-demo research; design remains not started.

## Source review

| Surface | Static evidence | Assessment |
|---|---|---|
| Global settings — `theme/config/settings_schema.json` | Seven configuration groups; 36 value-bearing inputs for typography, layout, colors, design tokens, element defaults and three shared global-content slots. Theme metadata includes its documentation URL and exactly one support URL. | Valid JSON and structurally consistent with Shopify’s documented settings-schema shape. This confirms declared controls only; it does not confirm Shopify Admin renders or saves them. |
| VSN reusable editor blocks — `theme/blocks/vsn-*.liquid` | Five VSN blocks: button, global component, group, heading and product card. Each has a schema. Setting IDs are unique within each schema; every select default matches a declared option. | The prototype has usable declared controls for content, variants, layout, product selection and responsive styling. |
| Responsive/simple controls | Responsive block settings use desktop/tablet/mobile anchors and additional breakpoint overrides. Advanced fields are gated with `visible_if`; simple-mode controls are also conditional. | Good progressive-disclosure intent in source. The actual editor panel density and preview response still need a live merchant test. |
| Section composition — `theme/sections/vsn-section.liquid` | One VSN section; supports `@theme` and `@app` block slots. | Basic theme/app block composition is declared, but there is not yet a complete section library. |
| Prototype page — `theme/templates/page.vsn-prototype.json` | One JSON template with three VSN sections and nested group, heading, button, product-card and global-component blocks. | Demonstrates the intended editor composition model on this prototype route only. |
| Other templates and section groups | The theme directory lists 12 Liquid templates and one VSN JSON prototype template. The sections directory contains only `vsn-section.liquid`; no header/footer section-group JSON files were present. | The full home, collection, product, cart and header/footer editing experience is not yet represented by the VSN JSON/section-group architecture. This matches the accepted ADR, which schedules the remaining conversion for Stage 7. |
| Saved editor state — `theme/config/settings_data.json` | `current` is empty. | No merchant-saved Theme Editor state is recorded. Defaults in the schema can still supply initial values; an empty `current` object is not proof that controls fail. |

## Checks performed

- Parsed `settings_schema.json` and the six VSN section/block schemas from the repository.
- Checked setting IDs for duplicates within each schema.
- Checked declared defaults against select-option values.
- Cross-read the prototype JSON template, theme directory, accepted ADR, current progress state and prior editor-feasibility evidence.
- Confirmed the earlier competitor editor feasibility record explicitly says `competitor_private_editor_tested: false` and labels Shopify-doc findings as `research_only`.

These are source-level checks only. No Theme Check command or live Shopify editor was run; the repository is not mounted in the current workspace checkout.

## Shopify platform evidence

Shopify defines `settings_schema.json` as the source of Theme settings controls, with merchant selections stored in `settings_data.json`. Sections and blocks provide the page-composition controls in the editor; Shopify describes the Theme Editor as an admin tool with real-time storefront preview.

- [Theme Editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor)
- [Theme settings schema](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-schema-json)
- [Theme settings data](https://shopify.dev/docs/storefronts/themes/architecture/config/settings-data-json)
- [Theme architecture](https://shopify.dev/docs/storefronts/themes/architecture)

## Why the cohort counter stays open

The 127 pending records are Theme Editor reviews of selected competitor presets. Public storefront demos and official listing pages do not expose a merchant’s private editor configuration. Repo policy says not to infer those settings and not to claim editor access without credentials and direct evidence. The VSN schema review above is useful platform/prototype evidence, but it is not 127 competitor editor inspections and does not change `pending.editor = 127`.

## Exact completion gate

To complete the VSN editor QA later, use the authorized VSN development store connected through the repository’s approved Shopify GitHub integration and verify, in the actual editor preview:

1. The prototype and then each JSON page template load without editor errors.
2. Global settings, block settings, theme/app blocks, preset defaults and conditional controls render with useful merchant-facing labels.
3. Changing a representative global setting and block setting visibly updates the preview and persists on save/reopen.
4. Header/footer section groups and the required page templates are present after the Stage 7 architecture work.
5. No unsupported competitor control claims are imported into the design spec.

To close competitor editor research, each record needs authorized direct access to that preset’s editor or a vendor-published schema/settings source. Until then, retain 0/127 reviewed and 127/127 pending.


## App block / app embed visibility diagnosis — 2026-10-28

The reported “embedded app option” can refer to two different Shopify features:

| Feature | Where it appears | What this repository supports | What is still required |
|---|---|---|---|
| **App embed** (floating widget, tracking, overlay) | Theme Editor → Theme settings → App embeds | `theme/layout/theme.liquid` contains `{{ content_for_header }}` and the normal layout output hook, so no missing global hook was found in the inspected file. | The actual Shopify app must provide and deploy a Theme App Extension with an embed block, and that app must be installed on the store. There is no app project or extension directory in this repository, so theme code alone cannot create its app-embed toggle. |
| **App block** (inline content such as reviews) | Apps section or an app-compatible section in a JSON template | `vsn-section.liquid` declares `@app` and renders `{% content_for 'blocks' %}`. This is present on the single `page.vsn-prototype.json` template. | The app must provide an app block. The current 12 Liquid templates are not JSON templates, so they do not provide this section-based insertion path yet. Convert them during the planned Stage 7 architecture work. |

Shopify documents these as separate extension targets: app blocks use `target: content` and require JSON templates plus a section that supports and renders `@app`; app embeds use `head`, `body`, or `compliance_head` and are enabled from Theme settings → App embeds after the app is installed. App embeds work without JSON templates. See [Shopify theme app extension configuration](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration) and [App blocks for themes](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks).

**Most likely cause:** if the missing control is in the App embeds panel, the extension is not installed/deployed in the target store (or the target app does not provide an embed block). The VSN theme does not define that app-owned control. If the missing control is an inline app block, it is only structurally available in the prototype JSON page today, not throughout the Liquid templates. The repository has no store connection or app installation state, so this is a source-based diagnosis, not direct confirmation of the store's installed-app state.

No code or matrix counters changed. Theme Editor competitor coverage remains 0/127 reviewed, 127 pending.


## Cross-repository correction — VSN Builder Theme App Extension

A follow-up read-only search across the same organization's VSN Builder app repository found the actual Theme App Extension. This corrects the earlier repo-local statement: **`vsn-super-mart` itself has no app project/extension, but the app extension exists in `Vertex-Systems-Network/vsn-builder`.**

- `extensions/vsn-page-builder-theme/shopify.extension.toml` declares the “VSN Builder Theme” extension.
- `extensions/vsn-page-builder-theme/blocks/vsn-page-renderer.liquid` declares `"target": "body"`, which is the VSN Builder app embed.
- 25 other extension blocks declare `"target": "section"`, providing inline app-blocks.
- `app/services/theme-embed-status.server.js` generates the activation deep link and checks `config/settings_data.json` for the active `vsn-page-renderer` block; `TopNav.jsx` also checks Shopify App Bridge extension activation status.
- `docs/t032-upstream-theme-fixtures.md` states **no Shopify store installed, published, or deployed** and leaves real Theme Editor/storefront acceptance pending. The roadmap lists real extension E2E as T033 WAITING. `scripts/deployment-blocked.mjs` disables direct Shopify CLI deploy/config-switch until the environment/release gates are satisfied.

**Updated likely cause:** the embed implementation exists in source, but it is not deployed/installed in the target Shopify store (or the target store is not the matching VSN Builder app installation). That would explain why the embed is absent in Theme Editor. This is strongly supported by repository release evidence, but remains **unconfirmed against the user's store**, which is not connected here. Shopify only shows an app-owned embed after its extension is installed and available to that store. See [VSN Builder extension source](https://github.com/Vertex-Systems-Network/vsn-builder/tree/development/extensions/vsn-page-builder-theme) and [T032 fixture status](https://github.com/Vertex-Systems-Network/vsn-builder/blob/development/docs/t032-upstream-theme-fixtures.md).

**Next required action:** after deployment safeguards are satisfied, install/update VSN Builder on the target development store, then use the existing activation URL/status workflow and verify Theme settings → App embeds. Do not create another theme setting or confuse this body embed with the section-target app blocks. No deployment was attempted and no app code or credentials were changed.

The competitor Theme Editor matrix remains editor 0/127 reviewed, 127 pending; this app-extension diagnosis is separate from the competitor cohort.
