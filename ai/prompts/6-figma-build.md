# Prompt — Stage 6: Figma build

Target: Figma file `BxJuIRth8k4cCUbFnPV6ek`, page "VSN | Super Mart" (`25:2`).
(Claude: load the `figma-use` skill before every `use_figma` call.)

Order: 1) Variables (color schemes, type, spacing, radius) 2) Components with variants (buttons, inputs,
badges, swatches, product card variants, price, rating, header, footer, drawer, modal) 3) Desktop 1440 +
mobile 390 frames for: home, collection, product, cart drawer, cart page, search + predictive search,
list collections, page, contact, blog, article, account (login/register/orders), 404, password, gift card.
4) Empty/sale/sold-out/loading states. Real content only.

Write the frame node ids into `spec.json → figma.frames`, run `vsn.py register-design <spec>`, ask for
approval, `vsn.py approve 6 "<name>"`, `vsn.py advance`.
