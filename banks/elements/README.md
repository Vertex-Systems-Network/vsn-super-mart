# Element Bank (team rule 15)

VSN Super Mart is built from a **library of global elements** (Shopify theme blocks, nestable) with full
customization. **Every demo/preset is made only by settings** (JSON templates + settings_data presets) —
no preset-specific code.

```
elements.json            catalog of every element: Elementor status, gaps, VSN extras, Shopify source
universal-settings.json  setting groups every element gets + the global design system tokens
responsive.json          smart responsive: 9 breakpoints (2448 1920 1440 1024 768 560 480 360 320)
```

## Principles
1. **Everything Elementor has, better** — every Elementor Free/Pro widget and the useful widgets of the big
   third-party addons (Essential Addons, The Plus, UAE, Happy, ElementsKit, Premium, Crocoblock, PowerPack),
   with the options they lack (`elementor_gap` → `vsn_extras`).
2. **Plus what Elementor never had** — Shopify commerce elements (variant picker, buy buttons, selling plans,
   pickup, facets, cart drawer, metafields…) and Gen-Z creative elements.
3. **Smart responsive** — 3 visible controls (desktop 1440 / tablet 768 / mobile 360), other breakpoints
   calculated with clamp(); "Advanced responsive" unlocks per-breakpoint overrides for all 9.
4. **Design system first** — elements default to theme tokens (colors, type, spacing, radius, motion).
5. **Shopify-first + compliance** — rule 10 order applies; elements with `store_allowed: false` live in
   the extras track or come from a VSN app.

## Status flow per element
`planned` → `spec` (settings written) → `built` (Liquid + CSS + JS) → `qa` (9 widths, a11y, perf) → `done`.
