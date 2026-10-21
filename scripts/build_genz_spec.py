import json, os
R = "/home/claude/vsn-super-mart"
J = lambda p: json.load(open(os.path.join(R, p)))
d = J("banks/design/specs/gen-z-store/directions.json")
ch = [x for x in d["directions"] if x["id"] == d["chosen"]][0]
res = J("ai/niches/gen-z-store/options.resolved.json")
opts = {o["id"]: o for o in J("banks/options/options.json")["options"]}
reqs = J("banks/research/platform/theme-store-requirements.json")["requirements"]

AREA_LOC = {
 "header": "section group header > header", "home": "index template", "collection": "collection > main-collection",
 "product": "product > main-product", "cart": "cart drawer + cart > main-cart", "search": "search > main-search + predictive search",
 "page": "page templates", "footer": "section group footer > footer", "global": "layout/theme.liquid + global snippets",
 "settings": "config/settings_schema.json", "dev": "codebase", "performance": "codebase + all templates",
 "a11y": "all components", "seo": "snippets/meta-tags + structured data", "extras": "extras track"}
SPECIFIC = {
 "hero-slideshow": "index > afterhours-video-hero (video, image, split variants)",
 "drop-release-section": "index > drop-release (release date text, collection link, early access form)",
 "early-access-signup": "index > drop-release block + password > drop-gate (customer tag 'early-access')",
 "password-drop-page": "password > drop-gate (video bg, date, signup)",
 "drop-state-badges": "snippets/product-card > badges (coming soon, sold out, last sizes from inventory)",
 "product-card-variants": "snippets/product-card: overlay (default), minimal, detailed",
 "fit-info-block": "product > main-product > fit-info block (metaobject fit)",
 "size-chart": "product > main-product > size-guide drawer (cm/inch toggle)",
 "sticky-atc": "product > sticky buy panel (desktop sticky split, mobile bottom bar)",
 "featured-collection": "index > drop-rail (horizontal rail)",
 "collection-list": "index > category-tiles",
 "cart-drawer": "global > cart-drawer (upsell rail, free shipping bar)",
 "announcement-bar": "header group > announcement marquee ticker",
 "mega-menu": "header > full-screen drawer menu with image promos (drawer nav)",
 "theme-styles-presets": "config/settings_data.json presets + listings/afterhours",
}
option_map = {}
for oid in res["must"] + res["should"]:
    o = opts[oid]
    option_map[oid] = SPECIFIC.get(oid, AREA_LOC.get(o["area"], "core"))
req_map = {r["id"]: f"{r['area']}: covered by spec section/option mapping; verify in QA" for r in reqs}
req_map.update({
 "req-codebase-origin": "Stage 7 starts from Shopify Skeleton theme",
 "req-uniqueness": "fingerprint vsn-genz-afterhours passes check-design (max 0.46)",
 "req-no-fake-urgency": "release date as static text; no ticking countdown, no fake stock",
 "req-no-app-features": "no wishlist/IG feed; UGC strip uses merchant-uploaded video",
 "req-a11y": "lime #C6FF3D on #0B0B0F = high contrast; body #F4F4F0 on #0B0B0F; focus ring lime 2px",
})

spec = {
 "id": ch["id"], "niche": "gen-z-store", "name": "Afterhours", "direction_summary": ch["moodboard"],
 "fp": ch["fp"], "palette": ch["palette"],
 "tokens": {
  "color_schemes": [
   {"id": "night", "background": "#0B0B0F", "foreground": "#F4F4F0", "accent": "#C6FF3D", "button": "#C6FF3D", "button_label": "#0B0B0F", "border": "#2A2A33", "muted": "#9A9AA3"},
   {"id": "surface", "background": "#16161D", "foreground": "#F4F4F0", "accent": "#C6FF3D", "button": "#F4F4F0", "button_label": "#0B0B0F", "border": "#2A2A33", "muted": "#9A9AA3"},
   {"id": "acid", "background": "#C6FF3D", "foreground": "#0B0B0F", "accent": "#0B0B0F", "button": "#0B0B0F", "button_label": "#C6FF3D", "border": "#0B0B0F", "muted": "#3A4A10"},
   {"id": "paper", "background": "#F4F4F0", "foreground": "#0B0B0F", "accent": "#0B0B0F", "button": "#0B0B0F", "button_label": "#F4F4F0", "border": "#D6D6CF", "muted": "#5C5C66"}],
  "status_colors": {"sale": "#FF3D6E", "success": "#C6FF3D", "error": "#FF5A4E"},
  "typography": {"heading_font": "Oswald (uppercase, tight tracking)", "body_font": "Inter", "note": "Confirm both in Shopify font library at build time",
                 "scale": {"display": 120, "h1": 72, "h2": 48, "h3": 32, "h4": 22, "body": 16, "small": 13, "label": 12}, "mobile_scale": {"display": 56, "h1": 40, "h2": 32, "h3": 24}},
  "spacing": {"unit": 4, "section_padding": {"mobile": 48, "desktop": 96}, "page_width": 1440, "gutter": {"mobile": 16, "desktop": 32}},
  "radius": {"button": 0, "card": 0, "input": 0, "badge": 0},
  "shadows": "none; depth via borders and surface color",
  "motion": {"duration_ms": 220, "easing": "cubic-bezier(.2,.8,.2,1)", "patterns": ["marquee ticker", "image scale on hover", "reveal on scroll"], "reduced_motion": "disable marquee + reveals"}},
 "templates": {
  "index": ["announcement-marquee", "header", "afterhours-video-hero", "drop-release", "drop-rail", "category-tiles", "lookbook-split", "ugc-video-strip", "manifesto-marquee", "newsletter", "footer"],
  "collection": ["collection-banner", "main-collection (horizontal filters, dense overlay grid)"],
  "product": ["main-product (sticky split)", "fit-info", "complementary-products", "related-products", "recently-viewed"],
  "cart": ["main-cart", "cart-upsell"], "search": ["main-search"], "list-collections": ["main-list-collections"],
  "page": ["main-page"], "page.contact": ["main-page", "contact-form"], "blog": ["main-blog"], "article": ["main-article"],
  "404": ["main-404"], "password": ["drop-gate"], "gift_card": ["gift-card"]},
 "sections": [
  {"id": "announcement-marquee", "name": "Announcement ticker", "blocks": ["message"], "settings": ["speed", "scheme", "pause on hover"], "variants": ["marquee", "static rotate"], "states": ["reduced motion = static"], "responsive": "same", "a11y": "pause control, aria-live off"},
  {"id": "header", "name": "Header", "blocks": [], "settings": ["logo", "menu", "sticky", "transparent over hero"], "variants": ["logo center + drawer"], "states": ["transparent", "solid on scroll"], "responsive": "icons: menu, search, account, cart", "a11y": "focus trap in drawer"},
  {"id": "afterhours-video-hero", "name": "Video hero", "blocks": ["eyebrow", "heading", "text", "buttons"], "settings": ["video", "poster image", "overlay opacity", "height"], "variants": ["video", "image", "split"], "states": ["video loading = poster"], "responsive": "mobile 9:16 video", "a11y": "pause button, captions optional"},
  {"id": "drop-release", "name": "Drop release", "blocks": ["drop label", "heading", "release date", "collection link", "early access form"], "settings": ["date (text)", "scheme"], "variants": ["upcoming", "live", "sold out"], "states": ["form success", "form error"], "responsive": "stack", "a11y": "labelled form"},
  {"id": "drop-rail", "name": "Drop rail", "blocks": [], "settings": ["collection", "card style", "show sizes"], "variants": ["rail", "grid"], "states": ["empty collection"], "responsive": "swipe", "a11y": "arrow buttons labelled"},
  {"id": "category-tiles", "name": "Category tiles", "blocks": ["tile"], "settings": ["columns"], "variants": ["2", "3", "4"], "states": [], "responsive": "2 cols", "a11y": ""},
  {"id": "lookbook-split", "name": "Lookbook / shop the look", "blocks": ["hotspot product"], "settings": ["image"], "variants": [], "states": [], "responsive": "list under image", "a11y": "hotspots are buttons"},
  {"id": "ugc-video-strip", "name": "UGC video strip", "blocks": ["video"], "settings": [], "variants": [], "states": [], "responsive": "swipe", "a11y": "muted, controls"},
  {"id": "main-product", "name": "Main product (sticky split)", "blocks": ["vendor", "title", "price", "installments", "variant picker", "size guide", "quantity", "buy buttons", "pickup", "fit info", "collapsible tabs", "share", "@app", "custom liquid"], "settings": ["media layout", "video autoplay"], "variants": ["sticky split"], "states": ["sold out", "size sold out", "sale", "coming soon"], "responsive": "mobile: media carousel + bottom buy bar", "a11y": "fieldset radios for sizes"},
  {"id": "cart-drawer", "name": "Cart drawer", "blocks": [], "settings": ["free shipping threshold", "upsell collection"], "variants": [], "states": ["empty", "loading", "error"], "responsive": "full width mobile", "a11y": "dialog"},
  {"id": "drop-gate", "name": "Password drop gate", "blocks": ["logo", "heading", "date", "signup", "password"], "settings": ["video"], "variants": [], "states": ["signup success"], "responsive": "", "a11y": ""}],
 "image_brief": {
  "style_line": "Night-time streetwear editorial: deep black background, hard flash photography, acid lime (#C6FF3D) rim light accents, gritty film grain, high contrast, Europe/US Gen-Z street style. No text, no logos, no watermark, no recognizable real people.",
  "slots": [
   {"slot": "home-hero", "ratio": "16:9", "subject": "model in oversized black hoodie under harsh flash on an empty city street at night"},
   {"slot": "lookbook", "ratio": "4:5", "subject": "two friends in streetwear layering, cargo pants and puffer, parking garage at night"},
   {"slot": "product-hoodie", "ratio": "4:5", "subject": "oversized washed-black hoodie, flat lay on dark concrete"},
   {"slot": "product-cargo", "ratio": "4:5", "subject": "black utility cargo pants with straps on dark background"},
   {"slot": "product-tee", "ratio": "4:5", "subject": "heavyweight off-white boxy t-shirt on dark background"},
   {"slot": "product-sneaker", "ratio": "4:5", "subject": "chunky black and lime sneaker on concrete"},
   {"slot": "product-cap", "ratio": "4:5", "subject": "black six-panel cap on dark surface"},
   {"slot": "product-jacket", "ratio": "4:5", "subject": "black nylon track jacket with lime piping"},
   {"slot": "category-tops", "ratio": "1:1", "subject": "close up of stacked black hoodies and tees"},
   {"slot": "category-bottoms", "ratio": "1:1", "subject": "close up of cargo pants fabric and straps"},
   {"slot": "category-accessories", "ratio": "1:1", "subject": "caps, chains and a crossbody bag on dark concrete"},
   {"slot": "drop-gate", "ratio": "16:9", "subject": "dark warehouse with single lime light beam, smoke"}]},
 "option_map": option_map, "requirement_map": req_map,
 "figma": {"file_key": "BxJuIRth8k4cCUbFnPV6ek", "page_node": "25:2", "frames": {}}}
json.dump(spec, open(os.path.join(R, "banks/design/specs/gen-z-store/spec.json"), "w"), indent=1)
print("options mapped", len(option_map))
