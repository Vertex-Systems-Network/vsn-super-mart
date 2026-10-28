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



## Pending QA criteria and run method — 2026-10-28

A read-only check of current Shopify developer documentation establishes the official Theme Store submission benchmarks and a practical test sequence. These are acceptance criteria/methods, **not measurements of the 127 competitor demos or the VSN store**.

| Area | Official requirement / recommended method | Evidence still needed |
|---|---|---|
| Lighthouse performance | Theme Store threshold is a minimum plain average of 60 across home, product and collection pages, on both mobile and desktop. Shopify says the test pages need real content and images; its documented test workflow uses a benchmark development store. | Run the supported benchmark on VSN and record per-page desktop/mobile scores. Do not apply the threshold as proof that a competitor demo passes. |
| Lighthouse accessibility | Theme Store threshold is a minimum plain average of 90 across home, product and collection pages, on both mobile and desktop. | Run those same six benchmark contexts and record score plus actionable findings; a score alone does not replace keyboard/assistive-technology review. |
| Keyboard operation | Shopify accessibility guidance expects links, buttons, dropdown navigation and form controls to work by keyboard, with visible focus. | Keyboard-test navigation, search, collection controls, variant selection, cart and dialogs on the authorized test storefront. |
| Checkout | Shopify-hosted checkout customizations use checkout app extensions and/or supported checkout configuration; a theme storefront page audit cannot establish checkout behavior. | Inspect the authorized checkout in a test store with test payment configuration. Stop before placing an order; record the visible progression and any plan-dependent restrictions. |

Official sources checked on 2026-10-28:
- [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) — performance and accessibility thresholds.
- [Theme performance testing](https://shopify.dev/docs/storefronts/themes/best-practices/performance/testing-for-performance) — benchmark/testing method.
- [Theme accessibility best practices](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility) — keyboard and focus requirements.
- [Shopify Lighthouse CI](https://shopify.dev/docs/storefronts/themes/tools/lighthouse-ci) — repeatable CI option.
- [Checkout UI extensions](https://shopify.dev/docs/api/checkout-ui-extensions/latest) — checkout/app extension scope and targets.

This closes the **requirements research** portion only. No Lighthouse run, keyboard session, checkout progression or Theme Store benchmark was available in this environment; the live QA items and 0/127 private-editor count remain open.


## Live QA evidence — Impulse:Impulse (2026-10-28)

### Checkout

A reversible cart smoke test added *The Ames Trouser* ($145) and opened the cart drawer. Checkout was attempted with the required terms checkbox left unchecked; the merchant displayed a required-consent alert and did not advance. No terms were accepted, no personal/payment details were entered, and no order was placed. The test item was removed and the cart showed empty. Status: **attempted, blocked before checkout; incomplete**.

### Keyboard and accessibility smoke review

- Homepage: Tab reached the “Skip to content” link with a visible focus outline. The Clothing navigation control was keyboard reachable and expanded on focus.
- Collection: the Filter button was keyboard reachable; Enter opened the filter drawer and exposed Price, Size, Product Type and Availability controls. Escape closed the drawer.
- Product: the tab sequence reached Add to Cart. Two product-gallery buttons appeared without accessible names in the accessibility tree.
- This is a limited manual smoke review, not a WCAG conformance claim.

### PageSpeed Insights / Lighthouse runs

Lighthouse 13.5.0 results captured for five of the six Home/Product/Collection device views:

| Page | Device | Performance | Accessibility | Best practices | SEO |
|---|---:|---:|---:|---:|---:|
| Home | Mobile | 56 | 86 | 96 | 77 |
| Home | Desktop | 89 | 90 | 96 | 77 |
| Product | Mobile | 59 | 95 | 96 | 92 |
| Collection | Mobile | 91 | 100 | 96 | 92 |
| Collection | Desktop | 99 | 100 | 96 | 92 |
| Product | Desktop | Pending | Pending | Pending | Pending |

The Product Desktop PSI report loaded its field data but the Lighthouse scoring panel remained in “loading,” so it is not counted. Cart was not run. Home mobile flagged missing image alt text, unnamed links, focusable descendants under aria-hidden, and heading order. Product mobile flagged focusable descendants under aria-hidden and heading order. Collection mobile and desktop each retained manual accessibility checks. These are lab snapshots for one demo theme/preset only, not proof for the other 126 presets.

**Disposition:** QA coverage improved for one preset, but checkout, full keyboard/accessibility review, and Lighthouse coverage remain incomplete. The canonical matrix counters remain at 0/127 for completed checkout and Lighthouse runs; no cohort-wide completion is claimed.


### PSI retry limitation

A single reload retry for the stalled Product Desktop report was redirected to Google's reCAPTCHA page, which said unusual traffic was detected. The challenge was not solved. This browser cannot currently retrieve additional PSI results; missing scores remain pending.


## Scope update and Dune keyboard/accessibility review — 2026-10-28

Checkout QA has been **removed from the active task at the user's request**. The earlier Impulse:Impulse terms-gate attempt remains in this report as historical context only; it is no longer a pending deliverable. The matrix sets pending checkout to zero and records the scope change without claiming a completed checkout test.

### Dune (Impulse:Dune) manual keyboard smoke review

- Homepage: visible focus on “Skip to content”; Tab traversal reached the Shop menu, which expanded on focus, and its submenu links were reachable.
- Product page: Tab traversal reached the size radio choices and Add to Cart. The product gallery has an unnamed button; Shop the Look has two unnamed buttons in the accessibility tree.
- Collection page: the Filter drawer exposes named Color, Price, Size, Product Type and Brand controls. Escape closed the drawer and returned focus to Filter. A Search combobox appeared after Escape. The drawer was opened by pointer, so keyboard opening itself was not confirmed.
- This is a limited manual smoke review, not a WCAG conformance audit.

Lighthouse has not been run for Dune. Additional PSI retrieval is currently blocked in this browser after Google's unusual-traffic human-verification challenge; it was not solved.


### Dune keyboard verification addendum — 2026-10-28

Follow-up confirmed keyboard operation on the Dune demo:

- On the collection page, Tab reached the SIZE filter after the skip link; Enter expanded it, Tab moved through the four labeled size checkboxes, and Space selected S. The URL gained `?filter.v.option.size=S`; the test was cleared by navigating back to the base collection URL.
- On the product page, Tab reached the labeled size radio options and Add to Cart.
- The collection Filter drawer can be opened with Enter and its controls are traversable by Tab. Escape closes the drawer, but the resulting focus is at the page root and a Search combobox appears; this focus behavior should be reviewed.
- The product gallery has an unnamed button, and Shop the Look has two unnamed buttons in the accessibility tree.

This remains a manual smoke review only, not a WCAG conformance audit.


### Apothecary keyboard smoke review — 2026-10-28

- Homepage: Tab reached the SHOP button; its submenu expanded while focused.
- Collection: Tab reached Filter after Skip to content. Space showed the FilterDrawer (Availability and Price sections) in the resulting accessibility snapshot. On the next Tab, the drawer had disappeared and focus was on Sort. Keyboard activation/focus persistence is inconsistent in this observation and needs follow-up.
- Product: Tab from Skip to content reached Add to Cart. Product disclosure controls were named and exposed as expandable buttons.
- Manual smoke test only; not a WCAG conformance audit.

The matrix now shows **0/127 complete** and **4/127 with partial keyboard/accessibility observations**. Lighthouse remains **0/127 complete**; PSI is still blocked by the human-verification challenge from the prior retry.


### Prestige — Allure homepage keyboard smoke review — 2026-10-28

Tab traversal reached the primary WOMEN, MEN, ABOUT and PRESETS buttons and the site logo. The buttons were named in the accessibility tree. Menu activation, product/collection keyboard behavior and Lighthouse were not verified. This is a homepage-only partial observation, not a WCAG audit.


### Prestige — Couture keyboard smoke review — 2026-10-28

- Homepage: Tab reached Skip to content, logo, HOME, SHOP, BLOG, ABOUT and PRESETS. Shift+Tab returned to SHOP; Enter expanded the submenu.
- Collection: Tab traversal reached Availability; Enter expanded it and exposed the named “In stock only” checkbox. Space toggled it on and the URL reflected `filter.v.availability=1`. The filter was cleared by returning to the base collection URL.
- Product: the accessibility tree exposed named gallery images, Black color radio, size chart, XS/S/M/L size radios, quantity controls, Add to Cart, Buy It Now and shipping/returns disclosures. Keyboard activation of every product control was not verified.
- This is a limited manual smoke review, not a WCAG conformance audit. Lighthouse was not run for this preset because PSI access in this browser remains blocked by the previously encountered Google unusual-traffic verification challenge; no CAPTCHA was solved.

The keyboard partial-observation count is now 6/127; full keyboard/accessibility completion remains 0/127. Lighthouse remains 0/127 complete.


### Prestige — Vogue keyboard smoke review — 2026-10-28

- Homepage: Tab reached the named Navigation menu button; Enter expanded the menu and exposed FACE, BODY, COLLECTIONS, JOURNAL and PRESETS. Escape collapsed it while focus remained on the menu button.
- Kits collection: Tab reached Availability; Enter expanded it and exposed the named “In stock only” checkbox. Space toggled it on and the URL reflected `filter.v.availability=1`. The test filter was cleared by returning to the base collection URL.
- The homepage accessibility tree exposed named product variant radios, quantity controls and Add to Cart for the featured Konjac Sponge. Keyboard activation of those product controls and the standalone product page were not verified.
- Limited manual smoke review only; not a WCAG conformance audit. Lighthouse was not run because PSI access in this browser remains blocked by the previously encountered Google unusual-traffic verification challenge; no CAPTCHA was solved.

The keyboard partial-observation count is now 7/127; full keyboard/accessibility completion remains 0/127. Lighthouse remains 0/127 complete.


### Prestige — Strass keyboard smoke review — 2026-10-28

- Homepage: the Navigation menu button appeared in the accessibility tree. Tab traversal was observed across Skip to content, announcement Previous/Next and the logo; keyboard activation of the menu was not verified.
- Necklaces collection: Tab reached FILTER; Enter expanded the filter drawer and exposed Availability, Price, Color, Close and View Results. Tab entered Availability and Escape closed the drawer, returning focus to FILTER.
- Homepage featured products expose Add to Cart / Choose options in the accessibility tree; keyboard activation was not verified.
- Limited manual smoke review only; not a WCAG conformance audit. Product-page keyboard behavior and Lighthouse were not tested. PSI access remains blocked in this browser by the previously encountered Google unusual-traffic verification challenge; no CAPTCHA was solved.

The keyboard partial-observation count is now 8/127; full keyboard/accessibility completion remains 0/127. Lighthouse remains 0/127 complete.


### Prestige — Signature keyboard smoke review — 2026-10-28

- Pumps collection: Tab traversal reached FILTER; Enter opened the drawer. Tab reached Availability, Enter expanded it and exposed the named “In stock only” checkbox. Space toggled it on. Escape closed the drawer and returned focus to FILTER.
- Drawer exposed named Availability, Color, Size and Price sections plus Close and View Results controls. The filter was not applied.
- Home keyboard menu and standalone product-page behavior were not tested. This is a limited manual keyboard smoke review, not a WCAG conformance audit. Lighthouse was not run; PSI access in this browser remains blocked by Google's unusual-traffic verification challenge, which was not solved.

The keyboard partial-observation count is now 9/127; full keyboard/accessibility completion remains 0/127. Lighthouse remains 0/127 complete.


### Symmetry — Chantilly keyboard smoke review — 2026-10-28

- All Our Products collection: Tab traversal reached the Filter link; Enter expanded the filter form and exposed named availability, color and size controls in the accessibility tree.
- Focus remained on the Filter trigger after activation. The next Tab moved to Sort (Featured), rather than entering the visible filter controls. Keyboard traversal inside the filter is unconfirmed and appears to need focus-management follow-up.
- No filter value was selected or applied; the base collection URL was restored.
- Limited manual smoke review only; not a WCAG conformance audit. Homepage menu and product-page keyboard controls were not tested. Lighthouse was not run; PSI access remains blocked in this browser by Google's unusual-traffic verification challenge, which was not solved.

The keyboard partial-observation count is now 10/127; full keyboard/accessibility completion remains 0/127. Lighthouse remains 0/127 complete.


### Symmetry — Salt Yard keyboard smoke review — 2026-10-28

- New Arrivals collection: Tab reached the Filter link; Enter expanded the filter form and exposed Price, Color, Size and Product type controls in the accessibility tree.
- Focus remained on the Filter trigger; the next Tab moved to Sort (Featured), rather than entering the visible filter controls. Keyboard traversal within the form is unconfirmed and appears to need focus-management follow-up.
- No filter value was selected or applied; the base collection URL was restored.
- Limited manual smoke review only; not a WCAG conformance audit. Homepage/product keyboard behavior and Lighthouse were not tested. PSI access remains blocked in this browser by Google's unusual-traffic verification challenge, which was not solved.

The keyboard partial-observation count is now 11/127; full keyboard/accessibility completion remains 0/127. Lighthouse remains 0/127 complete.


### Symmetry — Beatnik keyboard smoke review — 2026-10-28

- Women's Sunglasses collection: Tab reached the Filter link; Enter activated it and exposed Color and Product type controls with named checkboxes in the accessibility tree.
- Focus remained on Filter; the next Tab moved to Sort (Featured), skipping the visible filter controls. Keyboard traversal within the filter is unconfirmed and appears to need focus-management follow-up.
- No filter value was selected or applied. This is limited manual smoke review only, not a WCAG conformance audit. Homepage/product controls and Lighthouse were not tested; PSI remains blocked in this browser by the earlier Google unusual-traffic verification challenge, which was not solved.

The keyboard partial-observation count is now 12/127; full keyboard/accessibility completion remains 0/127. Lighthouse remains 0/127 complete.


### Symmetry — Duke keyboard smoke review — 2026-10-28

- Decks collection: Tab reached the Filter link; Enter opened the filter form and exposed Availability, Price, Product type and Size controls in the accessibility tree.
- After activating Filter, the next Tab moved to Sort (Date, new to old), rather than entering the visible filter controls. Keyboard traversal within the filter is unconfirmed and appears to need focus-management follow-up.
- No filter value was selected or applied; the base collection URL was restored. Limited manual smoke review only; not a WCAG conformance audit. Homepage and product-page keyboard behavior and Lighthouse were not tested. PSI remains blocked in this browser by Google's unusual-traffic verification challenge, which was not solved.

The keyboard partial-observation count is now 13/127; full keyboard/accessibility completion remains 0/127. Lighthouse remains 0/127 complete.


### Symmetry — Amara keyboard smoke review — 2026-10-28

- Rings collection: Tab reached the Filter link; Enter exposed availability radios and Price, Material and Ring Size controls in the accessibility tree.
- Focus remained on Filter; the next Tab moved to Sort (Featured), rather than entering the visible filter controls. Keyboard traversal within the filter is unconfirmed and appears to need focus-management follow-up.
- No filter value was selected or applied. Limited manual smoke review only; not a WCAG conformance audit. Homepage/product keyboard behavior and Lighthouse were not tested. PSI remains blocked in this browser by Google's unusual-traffic verification challenge, which was not solved.

The keyboard partial-observation count is now 14/127; full keyboard/accessibility completion remains 0/127. Lighthouse remains 0/127 complete.
