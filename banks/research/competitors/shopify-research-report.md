# Shopify popular theme families and presets — research phase closeout

Checked: **2026-10-25**. Primary evidence: official [Shopify Theme Store](https://themes.shopify.com/themes), [Koala sample leaderboard as of 2026-10-19](https://koala-apps.io/shopify-leaderboards/top-themes/), [Shopify official themes 2026 overview](https://www.shopify.com/blog/shopify-themes).

## Explicit scope and evidence

- **47 official Shopify Theme Store theme pages opened**: 24 paid multi-preset themes + 23 individual free themes.
- **104 preset names** listed in paid parent-theme **Presets** sections (all names enumerated for these selected 24 themes).
- **23 standalone free themes** — do not count as commercial presets. Ten are distinct first-party Horizon-collection storefronts: Horizon, Savor, Vessel, Heritage, Pitch, Dwell, Ritual, Fabric, Tinker, Atelier.
- **127 named design records** in `shopify-presets-2026.json`. **127 individual official preset/theme pages opened**, consisting of all 47 primary theme pages plus the 80 additional premium preset pages. Every URL was individually opened on Shopify's official Theme Store. Their interactive **View demo** storefronts were not inspected.
- **Ella, Minimog OS 2.0, and Kalles** are separately researched as externally distributed themes. Their catalogs are large and require a different individual-demo process; the original vendor pages, not Shopify's Theme Store, are the source.
- **Trademark** is a detected Shopify storefront theme name without a current official Theme Store listing; **Debut** is a legacy retired theme. Both are retained in popularity rankings but omitted as purchasable theme families.
- **The official "View demo" buttons are not static links in the retrieved listing HTML**; real shop sessions on home/collection/PDP/cart/mobile were not executed. This is complete *parent-listing/preset-name inventory for selected popular families*, **not** a full interaction QA audit or all themes worldwide.

## Multi-preset theme inventory

| Family | Presets verified on official family listing |
|---|---|
| [Impulse](https://themes.shopify.com/themes/impulse/presets/impulse) | Impulse, Dune, Terrain, Apothecary |
| [Prestige](https://themes.shopify.com/themes/prestige/presets/prestige) | Prestige, Couture, Vogue, Strass, Signature |
| [Symmetry](https://themes.shopify.com/themes/symmetry/presets/symmetry) | Symmetry, Salt Yard, Beatnik, Duke, Amara |
| [Broadcast](https://themes.shopify.com/themes/broadcast/presets/broadcast) | Broadcast, Relay, Airwave, Motif, Stellar |
| [Enterprise](https://themes.shopify.com/themes/enterprise/presets/enterprise) | Enterprise, Outlet, Homestead |
| [Impact](https://themes.shopify.com/themes/impact/presets/impact) | Impact, Cocoon, Balance |
| [Focal](https://themes.shopify.com/themes/focal/presets/focal) | Focal, Ivory, Quartz, Sapphire |
| [Warehouse](https://themes.shopify.com/themes/warehouse/presets/warehouse) | Warehouse, Wood, Mesh |
| [Expanse](https://themes.shopify.com/themes/expanse/presets/expanse) | Expanse, Revive, Spritz, Fetch, Gem |
| [Local](https://themes.shopify.com/themes/local/presets/local) | Local, Soleway, Thrive, Caffeine, Lively |
| [Empire](https://themes.shopify.com/themes/empire/presets/empire) | Empire, Circuit, Depot, Forma |
| [Be Yours](https://themes.shopify.com/themes/be-yours/presets/be-yours) | Be Yours, Sheen, Peace, Harmony |
| [Stiletto](https://themes.shopify.com/themes/stiletto/presets/stiletto) | Stiletto, Luster, Linen, Glimmer, Tapestry |
| [Motion](https://themes.shopify.com/themes/motion/presets/motion) | Motion, Satchel, Memo |
| [Palo Alto](https://themes.shopify.com/themes/palo-alto/presets/palo-alto) | Palo Alto, Dynamo, Skylight, Phenomena, Pluma |
| [Pipeline](https://themes.shopify.com/themes/pipeline/presets/pipeline) | Pipeline, Petra, Pahoa, Phantom |
| [Concept](https://themes.shopify.com/themes/concept/presets/concept) | Concept, Inova |
| [Sleek](https://themes.shopify.com/themes/sleek/presets/sleek) | Sleek, Wildpeak, Jumped, Modiva, Glint |
| [Wonder](https://themes.shopify.com/themes/wonder/presets/wonder) | Wonder, Root, Velour, Nook, Petit |
| [Eurus](https://themes.shopify.com/themes/eurus/presets/eurus) | Eurus, Arise, Placid, Mystique, Whiff |
| [Release](https://themes.shopify.com/themes/release/presets/release) | Release, Grasse, Serenity, Forest, Renaissance |
| [Ignite](https://themes.shopify.com/themes/ignite/presets/ignite) | Ignite, Playtime, Tails, Alpha, Peak |
| [Shapes](https://themes.shopify.com/themes/shapes/presets/shapes) | Shapes, Fizz, Candy, Aura, Scratch |
| [Vision](https://themes.shopify.com/themes/vision/presets/vision) | Vision, Onyx, Poochy, Velocite, Solstice |

### Source disagreement: Empire / Vast

The public [Empire Presets listing](https://themes.shopify.com/themes/empire/presets/empire) currently exposes four names (Empire, Circuit, Depot, Forma), while the vendor's [October 23, 2026 release notes](https://support.pixelunion.net/hc/en-us/articles/360022155054-Empire-release-notes) claim **Vast** was added. It is recorded as a **pending discrepancy** instead of being counted as a verified fifth preset. This is why inventory counts are exact for *visible listings checked*, not guaranteed exhaustive across unpublished/unindexed updates.

## Individual preset URL audit finished

All **127/127** named records have a verified official URL in `shopify-presets-2026.json` as of 2026-10-25: 104 paid preset listing pages and 23 standalone free theme listing pages. This closes the **official Shopify product-page audit** for the selected cohort. It does **not** close direct live-demo browsing or functional behaviour verification.

## VSN AI decisions

| Goal | Grounded theme signal | Original Shopify-native / VSN implementation |
|---|---|---|
| Reusable multi-niche presets | Symmetry, Prestige, Impulse and others show 3–5 presets sharing a family | Shared theme code, color/typography tokens, global sections and block settings; per-niche demo content |
| Store-editor flexibility | Shopify's Horizon collection promotes deeply nestable theme blocks | Original nested Shopify blocks, dynamic sources and reusable component settings, **not copied Dawn/Horizon code** |
| Large-catalog discovery | Warehouse, Enterprise, Empire, Expanse parent listings | Shopify menus + filters + collection navigation + merchant-configured sorting |
| Editorial premium shopping | Prestige, Palo Alto, Focal, Stiletto, Pipeline | Original product media, lookbooks, configurable hero, rich PDP layout, accessible galleries |
| Promotions and quick commerce | Impulse, Broadcast, Impact, Concept | Real collection promos, quick-add, native cart API, keyboard-safe quick view |
| Grocery and local delivery | Local, Savor, Expanse and Shopify food demos | True store location pickup, metafield nutrition blocks, merchant-managed shipping thresholds |
| Motion and mobile | Motion, Concept, Shapes, Horizon collection | Native responsive layout, reduced-motion handling, intentional swipe controls; performance measured later |

Mapping status: research hypotheses and vendor-listed features, **not** evidence that VSN theme already implements these. Every feature must pass separate native Shopify / app-first compliance and real dev-store QA.

## Outstanding evidence tasks

1. Individually inspect the new preset releases and future listing pages; add direct URL and visit date only after opening.
2. Inspect live store demo home, collection, PDP, cart and mobile behaviour in a real browser session; compare screenshots and perform accessibility/performance tests.
3. Review externally sold Ella, Minimog and Kalles demos in batches, retaining licensing and app-vs-theme ownership distinctions.
4. Recheck snapshots as Shopify Theme Store themes and preset lists change.
5. Finish Afterhours Figma images/visual approval separately; this research work does **not** advance Stage 6.

### Commands
```sh
python3 scripts/shopify_theme_research.py validate
python3 scripts/shopify_theme_research.py summary
python3 scripts/shopify_theme_research.py next
python3 scripts/competitor_audit.py validate
python3 scripts/vsn.py validate
```


## Mobile design synthesis addendum — 2026-10-27

The 127-preset mobile preview sweep is complete at **360×640 CSS px**. It adds a mobile visual evidence layer to the older Theme Store listing and rendered-page research; it does not mark collection/PDP/cart interactions, Theme Editor, checkout, accessibility, or Lighthouse as tested. Two storefront hero previews remained limited in clarity (Eurus:Arise and Stiletto:Luster), while their mobile headers/compositions were reviewed.

### Patterns carried into design research
- Keep announcement, search, logo, menu and cart controls within a measured 360 px header stack; search-heavy layouts need progressive disclosure.
- Preserve image-led storytelling while controlling mobile focal points, headline wrapping and CTA separation.
- Treat a two-column product grid as a useful baseline where imagery and labels remain legible; allow one-column editorial/product views.
- Check every ticker, promo strip and image-overlay headline for horizontal clipping. Palo Alto:Dynamo, Broadcast:Motif and Empire variants showed specific crowding risks.
- Review age-gate and cookie-consent states as part of the first viewport. Lively and Eurus:Arise exposed these overlays in the reviewed view.

See `shopify-mobile-synthesis-2026.md`, `shopify-mobile-review-batch131-2026.md`, `shopify-127-completion-matrix-2026.json` and `banks/design/competitor-observations.json`. All findings inform original responsive design; exact competitor layouts, imagery and type combinations should not be copied.
