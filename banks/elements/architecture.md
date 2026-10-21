# VSN Element System — Elementor + Gutenberg merged, built for Shopify

Goal: one element system that beats **Elementor** (widgets, per-breakpoint styling, theme builder) and
**WordPress Gutenberg** (global styles, synced patterns, bindings, fluid design) — on Shopify theme blocks.

## 1. What each one does best (and where it falls short)

| Concept | Elementor | Gutenberg | VSN takes |
|---|---|---|---|
| Element set | Large widget set + huge third-party addon market | ~90+ lean core blocks, content-first | Elementor + addons + Gutenberg blocks + Shopify commerce + creative (`elements.json`) |
| Global design tokens | Global colors + global fonts (site kit) | `theme.json`: palette, gradients, font sizes, spacing scale, shadows, custom properties | Full token system in theme settings, output as CSS custom properties |
| Default styles per element type | Widget defaults per kit (limited) | `styles.elements` (link, button, heading) + `styles.blocks` per block | **Element defaults**: every element type has global default style editable once in theme settings |
| Named style presets | Saved widget styles via global widgets | **Block style variations** + section styles | **Style variations** per element (e.g. Button: solid / ghost / brutal / glass) + color schemes per section |
| Reusable / global elements | Global widget (synced, no per-instance content) | **Synced patterns + overrides** (layout synced, chosen fields overridable; only some blocks/attributes) | **Global components**: synced design, *every* content field can be marked overridable, any element type |
| Ready layouts | Template kits | Pattern directory, starter patterns | **Patterns** = section/block presets per niche, from the banks |
| Dynamic data | Dynamic tags (Pro) | **Block Bindings API** (post meta, pattern overrides, custom sources) | Shopify dynamic sources on every field: product, collection, metafields, metaobjects, shop, customer |
| Responsive | Per-breakpoint controls (custom breakpoints; duplicating controls slowed frontend up to 47% per Elementor) | **No breakpoint controls in core**; intrinsic/fluid design (clamp, min/max) | **Fluid by default** (Gutenberg) **+ 9 breakpoint overrides on demand** (Elementor), only overridden values output (`responsive.json`) |
| Interactions | Motion effects, entrance animations (Pro) | Interactivity API (declarative, server-rendered) | Small web components + data attributes; motion presets; reduced-motion always respected |
| Templates / site parts | Theme Builder + display conditions (Pro) | Template parts + site editor templates | Shopify section groups (header/footer/overlay) + alternate templates + **display conditions** on every element |
| Locking / safe editing | Role manager (Pro) | `contentOnly` locking | **Simple mode**: per element, hide design controls and show content only |
| Popups | Popup builder (Pro) | none in core | Popup / drawer elements with triggers + frequency |
| Performance | Heavy DOM/CSS, many wrappers | Lean markup | Lean Liquid, CSS custom properties, no layout JS, lazy media, per-element CSS only when used |

## 2. VSN layer model (how a value is decided)

```
1 Design tokens          theme settings (colors, type scale, spacing scale, radius, shadows, motion)
2 Element defaults       global style per element type (e.g. all Headings, all Buttons)
3 Style variation        named preset chosen on the instance (Button → "Brutal")
4 Global component       synced design shared by all instances (design changes propagate)
5 Instance settings      this element's own settings (content + design overrides)
6 Responsive overrides   per-breakpoint values (only if Advanced responsive is on)
7 Display conditions     show/hide by breakpoint, customer tag, market, language, date range, product data
```
Lower layers inherit from higher ones; an instance only stores what it overrides — so presets stay small and
a whole demo can change look by editing tokens + element defaults.

## 3. Shopify mapping (what is native, what we build)

| VSN concept | Shopify building block | Notes / limits to verify in Stage 7 |
|---|---|---|
| Element | Theme block (`blocks/*.liquid`), nestable | Nesting depth and blocks-per-section limits apply |
| Design tokens | `settings_schema.json` + `settings_data.json` | Output once as `:root` custom properties |
| Element defaults | Theme settings group per element type | Keep each group small; Shopify caps settings |
| Style variation | `select` setting on the block → adds a class; variation styles live in CSS | Variations are code-defined, chosen in editor |
| Global component | Metaobject entry ("VSN component") holding shared content + a block that renders it; shared design via variation/defaults | Shopify has no native synced blocks across templates; section groups cover header/footer only |
| Patterns | Block and section `presets` + niche JSON templates | Presets come from the banks |
| Dynamic data | Dynamic sources (metafields/metaobjects) | Native in the editor |
| Responsive overrides | Hidden "advanced" settings per breakpoint → CSS variables + media queries | Count settings against limits; split across nested blocks if needed |
| Display conditions | Liquid conditions on customer tags, `localization`, dates, product tags | Done server-side, no flicker |
| Simple mode | `visible_if` (conditional settings) to hide design controls | Verify current support for conditional settings |
| Popups/drawers | Section group (overlay) + blocks | Theme Store: no fake urgency |

## 4. Where VSN beats both
1. Commerce-native elements neither has (variant picker, buy buttons, selling plans, pickup, facets, drop release, wishlist/compare UI, B2B).
2. Fluid + per-breakpoint in one model, with zero CSS for breakpoints you do not override.
3. Global components where any field is overridable (Gutenberg 6.6 allows only some blocks/attributes).
4. Display conditions on every element by Shopify data (market, language, customer tag, metafield).
5. Demos are settings-only and checked by the banks (uniqueness, coverage, no minimalism, no clipping).
6. Element defaults + variations mean a merchant restyles the whole store from one place.

## Sources
- Overrides in synced patterns (WordPress Developer Blog): https://developer.wordpress.org/news/2024/06/an-introduction-to-overrides-in-synced-patterns/
- Global Settings and Styles (theme.json): https://developer.wordpress.org/block-editor/developers/themes/theme-json/
- Gutenberg and responsive controls (Pootlepress): https://www.pootlepress.com/?p=52557
- Elementor custom breakpoints and performance: https://developers.elementor.com/the-road-to-additional-custom-breakpoints/
