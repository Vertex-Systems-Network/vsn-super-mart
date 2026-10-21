# Options Bank

Every feature/option the theme can offer, for all three audiences: **shopper**, **merchant** (store owner /
theme editor user) and **developer**. `options.json` is the master list.

| field | values |
|---|---|
| id | kebab-case, unique, never renamed |
| audience | `shopper`, `merchant`, `developer` (one or more) |
| area | header, home, collection, product, cart, search, page, footer, global, settings, dev, performance, a11y, seo, extras |
| priority | `must` / `should` / `could` |
| scope | `"core"` (every preset) or a list of niche ids |
| store_allowed | `false` = not allowed in a Theme Store theme (wishlist, countdown, Instagram feed, fake urgency) → extras track only |
| theme_store_required | `true` = required by Theme Store rules |
| source | `theme-store-requirements`, `competitor-analysis`, or a niche id |

`vsn.py resolve-options <niche>` produces the niche's must/should/could list;
`vsn.py coverage <spec>` checks that a design covers every `must`.
