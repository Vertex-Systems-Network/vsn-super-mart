# theme/ — agent notes

Follow the repository root `AGENTS.md` (team rules 1–15) and `docs/adr/0001-theme-base-and-architecture.md`.
This theme starts from Shopify Skeleton but **does use sections, JSON templates and section groups**
(Theme Store requirement). The upstream Skeleton guide is kept only for reference in
`SKELETON-UPSTREAM-AGENTS.md` — where it conflicts with the ADR, the ADR wins.

Conventions kept from Skeleton: no `{% stylesheet %}`/`{% javascript %}` (assets only), `routes.*` for
URLs, translated storefront strings, whitespace between tag names and Liquid, Theme Check clean.

VSN element blocks live in `blocks/vsn-*.liquid`; tokens in `snippets/vsn-tokens.liquid`; responsive CSS
generator in `snippets/vsn-responsive.liquid`.
