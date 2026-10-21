# ADR 0001 — Theme base: Shopify Skeleton + sections/JSON templates + VSN element library

- Date: 2026-10-22 · Status: accepted (prototype)

## Context
- Theme Store requires Skeleton or original code (no Dawn/Horizon), **JSON templates** for the required
  templates, header/footer in **section groups**, and sections on every template.
- The current upstream Skeleton (github.com/Shopify/skeleton-theme) uses a newer "no sections, Liquid
  templates, `{% block %}` tag, `{% partial %}`" model aimed at the agentic editor; its own guide forbids
  sections and JSON templates.
- Team rule 15: every demo is built from a global element library by settings only.

## Decision
1. Start from Skeleton files (allowed base) but **do not follow its no-sections rule**: VSN adds
   `sections/` + JSON templates + section groups so merchants get full drag-and-drop editing and the theme
   meets Theme Store requirements. Upstream guide kept as `theme/SKELETON-UPSTREAM-AGENTS.md` for reference.
2. VSN elements are **theme blocks** (`blocks/vsn-*.liquid`) used inside generic VSN sections via
   `{% content_for 'blocks' %}` and nestable (max depth 8).
3. **Global components** use theme settings slots (synced across pages, Theme Store safe) instead of
   custom metaobjects (Theme Store allows only standard metaobject definitions). A metaobject-based version
   can be offered later through a VSN app.
4. Smart responsive: anchors (1440/768/360) interpolated with CSS calc/clamp; per-breakpoint overrides
   hidden behind `visible_if` "Advanced responsive"; only set overrides emit media queries.

## Consequences
- Templates other than the prototype page are still Skeleton Liquid templates; converting them to JSON is
  part of Stage 7.
- Theme Check runs with `theme-check:recommended`.
