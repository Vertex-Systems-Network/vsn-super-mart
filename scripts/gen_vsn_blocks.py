#!/usr/bin/env python3
"""Generates VSN element blocks (theme/blocks/vsn-*.liquid) with standard schemas.

Every element gets: content settings, a style variation (with 'inherit' = theme element default),
responsive numeric settings (desktop/tablet/mobile + hidden advanced overrides), simple mode
(hides design controls) and advanced responsive (shows per-breakpoint overrides) — team rule 15.
Run: python3 scripts/gen_vsn_blocks.py
"""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "theme")
DESIGN = "{{ block.settings.simple_mode == false }}"
ADV = "{{ block.settings.simple_mode == false and block.settings.adv == true }}"
OVR = [320, 480, 560, 1024, 1920, 2448]


def rnum(pid, label, d, t, m, unit="px"):
    """Responsive number: 3 anchors + 6 advanced overrides."""
    out = [{"type": "header", "content": label, "visible_if": DESIGN},
           {"type": "number", "id": f"{pid}_d", "label": f"{label} — desktop (1440) {unit}", "default": d, "visible_if": DESIGN},
           {"type": "number", "id": f"{pid}_t", "label": f"{label} — tablet (768) {unit}", "default": t, "visible_if": DESIGN},
           {"type": "number", "id": f"{pid}_m", "label": f"{label} — mobile (360) {unit}", "default": m, "visible_if": DESIGN}]
    for bp in OVR:
        out.append({"type": "number", "id": f"{pid}_{bp}", "label": f"{label} — {bp} override", "visible_if": ADV})
    return out


def rsel(pid, label, options, d, t, m):
    """Responsive discrete setting (steps, no interpolation)."""
    opts = [{"value": v, "label": l} for v, l in options]
    return [{"type": "select", "id": f"{pid}_{k}", "label": f"{label} — {n}", "options": opts, "default": v, "visible_if": DESIGN}
            for k, n, v in (("d", "desktop", d), ("t", "tablet", t), ("m", "mobile", m))]


def common_tail():
    return [{"type": "header", "content": "Editing"},
            {"type": "checkbox", "id": "simple_mode", "label": "Simple mode (content only)", "default": False},
            {"type": "checkbox", "id": "adv", "label": "Advanced responsive (all 9 breakpoints)", "default": False, "visible_if": DESIGN},
            {"type": "text", "id": "css_class", "label": "Custom CSS class", "visible_if": DESIGN}]


def resp_call(pid, prop, unit="px"):
    o = ", ".join(f"o{bp}: block.settings.{pid}_{bp}" for bp in OVR)
    return (f"{{% render 'vsn-responsive', scope: scope, prop: '{prop}', unit: '{unit}', adv: block.settings.adv, "
            f"d: block.settings.{pid}_d, t: block.settings.{pid}_t, m: block.settings.{pid}_m, {o} %}}")


def write(name, doc, body, schema):
    path = os.path.join(ROOT, "blocks", f"{name}.liquid")
    with open(path, "w") as f:
        f.write("{% doc %}\n" + doc.strip() + "\n{% enddoc %}\n" + body.strip() + "\n\n{% schema %}\n" + json.dumps(schema, indent=2) + "\n{% endschema %}\n")
    print("wrote", path)


VAR_HEAD = [("inherit", "Theme default"), ("display", "Display"), ("outline", "Outline"), ("gradient", "Gradient"), ("marker", "Marker highlight")]
VAR_BTN = [("inherit", "Theme default"), ("solid", "Solid"), ("ghost", "Ghost"), ("brutal", "Brutal (offset shadow)"), ("glass", "Glass")]
VAR_CARD = [("inherit", "Theme default"), ("overlay", "Overlay"), ("minimal", "Minimal"), ("detailed", "Detailed")]
ALIGN = [("start", "Left"), ("center", "Center"), ("end", "Right")]


def opts(pairs):
    return [{"value": v, "label": l} for v, l in pairs]


# ---------------- Heading ----------------
write("vsn-heading", """
  VSN element: Heading (rule 15). Variations, fluid size, responsive alignment, simple mode.
  Self-contained block: callers leave the body empty.
""", """
{%- liquid
  assign scope = '#vsn-' | append: block.id
  assign variation = block.settings.variation
  if variation == 'inherit'
    assign variation = settings.vsn_heading_variation
  endif
  assign tag = block.settings.tag
-%}
{% style %}
  {{ scope }}{--vsn-align-d:{{ block.settings.align_d }};--vsn-align-t:{{ block.settings.align_t }};--vsn-align-m:{{ block.settings.align_m }};--vsn-ls:{{ block.settings.letter_spacing | divided_by: 100.0 }}em}
  {% render 'vsn-responsive', scope: scope, prop: 'fs', d: block.settings.size_d, t: block.settings.size_t, m: block.settings.size_m, adv: block.settings.adv, o320: block.settings.size_320, o480: block.settings.size_480, o560: block.settings.size_560, o1024: block.settings.size_1024, o1920: block.settings.size_1920, o2448: block.settings.size_2448 %}
{% endstyle %}
<{{ tag }}
  id="vsn-{{ block.id }}"
  class="vsn-heading vsn-heading--{{ variation }} vsn-weight--{{ block.settings.weight }} vsn-case--{{ block.settings.transform }} {{ block.settings.css_class | escape }}"
  {{ block.shopify_attributes }}
>
  {{- block.settings.text -}}
</{{ tag }}>
""", {
    "name": "VSN Heading",
    "settings": [
        {"type": "inline_richtext", "id": "text", "label": "Text", "default": "Night shift"},
        {"type": "select", "id": "tag", "label": "HTML tag", "options": opts([("h1", "H1"), ("h2", "H2"), ("h3", "H3"), ("h4", "H4"), ("p", "Paragraph")]), "default": "h2"},
        {"type": "select", "id": "variation", "label": "Style variation", "options": opts(VAR_HEAD), "default": "inherit", "visible_if": DESIGN},
        {"type": "select", "id": "weight", "label": "Weight", "options": opts([("regular", "Regular"), ("bold", "Bold")]), "default": "bold", "visible_if": DESIGN},
        {"type": "select", "id": "transform", "label": "Text case", "options": opts([("none", "As typed"), ("upper", "Uppercase")]), "default": "upper", "visible_if": DESIGN},
        {"type": "range", "id": "letter_spacing", "label": "Letter spacing", "min": -10, "max": 30, "step": 1, "unit": "%", "default": -1, "visible_if": DESIGN},
        *rnum("size", "Font size", 96, 64, 44),
        *rsel("align", "Alignment", ALIGN, "start", "start", "start"),
        *common_tail(),
    ],
})

# ---------------- Button ----------------
write("vsn-button", """
  VSN element: Button (rule 15). Variations solid/ghost/brutal/glass, responsive size, full width per device.
  Self-contained block: callers leave the body empty.
""", """
{%- liquid
  assign scope = '#vsn-' | append: block.id
  assign variation = block.settings.variation
  if variation == 'inherit'
    assign variation = settings.vsn_button_variation
  endif
-%}
{% style %}
  {{ scope }}{--vsn-full-d:{% if block.settings.full_d %}100%{% else %}auto{% endif %};--vsn-full-t:{% if block.settings.full_t %}100%{% else %}auto{% endif %};--vsn-full-m:{% if block.settings.full_m %}100%{% else %}auto{% endif %}}
  {% render 'vsn-responsive', scope: scope, prop: 'bh', d: block.settings.height_d, t: block.settings.height_t, m: block.settings.height_m, adv: block.settings.adv, o320: block.settings.height_320, o480: block.settings.height_480, o560: block.settings.height_560, o1024: block.settings.height_1024, o1920: block.settings.height_1920, o2448: block.settings.height_2448 %}
{% endstyle %}
<a
  id="vsn-{{ block.id }}"
  href="{{ block.settings.link | default: routes.all_products_collection_url }}"
  class="vsn-button vsn-button--{{ variation }} {{ block.settings.css_class | escape }}"
  {{ block.shopify_attributes }}
>
  <span>{{ block.settings.label | escape }}</span>
  {%- if block.settings.icon == 'arrow' -%}
    <svg class="vsn-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
  {%- endif -%}
</a>
""", {
    "name": "VSN Button",
    "settings": [
        {"type": "text", "id": "label", "label": "Label", "default": "Shop the drop"},
        {"type": "url", "id": "link", "label": "Link"},
        {"type": "select", "id": "variation", "label": "Style variation", "options": opts(VAR_BTN), "default": "inherit", "visible_if": DESIGN},
        {"type": "select", "id": "icon", "label": "Icon", "options": opts([("none", "None"), ("arrow", "Arrow")]), "default": "arrow", "visible_if": DESIGN},
        *rnum("height", "Height", 56, 52, 48),
        {"type": "header", "content": "Full width", "visible_if": DESIGN},
        {"type": "checkbox", "id": "full_d", "label": "Full width — desktop", "default": False, "visible_if": DESIGN},
        {"type": "checkbox", "id": "full_t", "label": "Full width — tablet", "default": False, "visible_if": DESIGN},
        {"type": "checkbox", "id": "full_m", "label": "Full width — mobile", "default": True, "visible_if": DESIGN},
        *common_tail(),
    ],
})

# ---------------- Product card ----------------
write("vsn-product-card", """
  VSN element: Product card (rule 15). Variations overlay/minimal/detailed, real badges (sale %, sold out),
  sizes, wishlist/compare/quick view buttons (data from VSN app, rule 12), responsive title size.
  Self-contained block: callers leave the body empty.
""", """
{%- liquid
  assign scope = '#vsn-' | append: block.id
  assign p = block.settings.product
  assign variation = block.settings.variation
  if variation == 'inherit'
    assign variation = settings.vsn_card_variation
  endif
-%}
{% style %}
  {{ scope }}{--vsn-ratio:{{ block.settings.ratio }}}
  {% render 'vsn-responsive', scope: scope, prop: 'tfs', d: block.settings.title_d, t: block.settings.title_t, m: block.settings.title_m, adv: block.settings.adv, o320: block.settings.title_320, o480: block.settings.title_480, o560: block.settings.title_560, o1024: block.settings.title_1024, o1920: block.settings.title_1920, o2448: block.settings.title_2448 %}
{% endstyle %}
<article
  id="vsn-{{ block.id }}"
  class="vsn-card vsn-card--{{ variation }} {{ block.settings.css_class | escape }}"
  {{ block.shopify_attributes }}
>
  {%- if p != blank -%}
    <a class="vsn-card__media" href="{{ p.url }}">
      {%- if p.featured_image -%}
        {{ p.featured_image | image_url: width: 1200 | image_tag: loading: 'lazy', sizes: '(min-width: 1024px) 25vw, 50vw', widths: '360, 540, 720, 960, 1200', alt: p.featured_image.alt | default: p.title }}
      {%- else -%}
        {{ 'product-1' | placeholder_svg_tag: 'vsn-card__placeholder' }}
      {%- endif -%}
    </a>
    {%- if block.settings.show_badges -%}
      <div class="vsn-card__badges">
        {%- if p.available == false -%}
          <span class="vsn-badge vsn-badge--soldout">{{ 'products.sold_out' | t }}</span>
        {%- elsif p.compare_at_price > p.price -%}
          {%- assign off = p.compare_at_price | minus: p.price | times: 100 | divided_by: p.compare_at_price -%}
          <span class="vsn-badge vsn-badge--sale">-{{ off }}%</span>
        {%- endif -%}
      </div>
    {%- endif -%}
    {%- if block.settings.show_actions -%}
      <div class="vsn-card__actions">
        <button type="button" class="vsn-iconbtn" data-vsn-wishlist="{{ p.id }}" aria-label="{{ 'products.add_to_wishlist' | t }}"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg></button>
        <button type="button" class="vsn-iconbtn" data-vsn-compare="{{ p.id }}" aria-label="{{ 'products.compare' | t }}"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M7 4v16M17 4v16M3 8l4-4 4 4M13 16l4 4 4-4"/></svg></button>
        <button type="button" class="vsn-iconbtn" data-vsn-quick-view="{{ p.handle }}" aria-label="{{ 'products.quick_view' | t }}"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/></svg></button>
      </div>
    {%- endif -%}
    <div class="vsn-card__info">
      <a class="vsn-card__title" href="{{ p.url }}">{{ p.title | escape }}</a>
      <div class="vsn-card__price">
        {%- if p.compare_at_price > p.price -%}
          <span class="vsn-price--sale">{{ p.price | money }}</span> <s class="vsn-price--was">{{ p.compare_at_price | money }}</s>
        {%- else -%}
          {{ p.price | money }}
        {%- endif -%}
      </div>
      {%- if block.settings.show_sizes -%}
        {%- for option in p.options_with_values -%}
          {%- assign oname = option.name | downcase -%}
          {%- if oname == 'size' or oname == 'größe' or oname == 'taille' -%}
            <ul class="vsn-card__sizes">
              {%- for value in option.values -%}
                <li class="{% unless value.available %}is-out{% endunless %}">{{ value | escape }}</li>
              {%- endfor -%}
            </ul>
          {%- endif -%}
        {%- endfor -%}
      {%- endif -%}
    </div>
  {%- else -%}
    <div class="vsn-card__media">{{ 'product-1' | placeholder_svg_tag: 'vsn-card__placeholder' }}</div>
    <div class="vsn-card__info"><span class="vsn-card__title">{{ 'products.choose_product' | t }}</span></div>
  {%- endif -%}
</article>
""", {
    "name": "VSN Product card",
    "settings": [
        {"type": "product", "id": "product", "label": "Product"},
        {"type": "select", "id": "variation", "label": "Style variation", "options": opts(VAR_CARD), "default": "inherit", "visible_if": DESIGN},
        {"type": "select", "id": "ratio", "label": "Image ratio", "options": opts([("4/5", "Portrait 4:5"), ("1/1", "Square"), ("3/4", "Tall 3:4")]), "default": "4/5", "visible_if": DESIGN},
        {"type": "checkbox", "id": "show_badges", "label": "Show badges (sale %, sold out)", "default": True},
        {"type": "checkbox", "id": "show_sizes", "label": "Show sizes", "default": True},
        {"type": "checkbox", "id": "show_actions", "label": "Show wishlist, compare and quick view", "default": True},
        *rnum("title", "Title size", 20, 18, 16),
        *common_tail(),
    ],
})

# ---------------- Group (layout container) ----------------
write("vsn-group", """
  VSN element: Group / container (rule 15). Holds any theme blocks (nestable). Flex or grid,
  responsive columns, direction, gap and padding. Children come from the theme editor via content_for 'blocks'.
""", """
{%- liquid
  assign scope = '#vsn-' | append: block.id
-%}
{% style %}
  {{ scope }}{--vsn-cols-d:{{ block.settings.cols_d }};--vsn-cols-t:{{ block.settings.cols_t }};--vsn-cols-m:{{ block.settings.cols_m }};--vsn-dir-d:{{ block.settings.dir_d }};--vsn-dir-t:{{ block.settings.dir_t }};--vsn-dir-m:{{ block.settings.dir_m }}}
  {% render 'vsn-responsive', scope: scope, prop: 'gap', d: block.settings.gap_d, t: block.settings.gap_t, m: block.settings.gap_m, adv: block.settings.adv, o320: block.settings.gap_320, o480: block.settings.gap_480, o560: block.settings.gap_560, o1024: block.settings.gap_1024, o1920: block.settings.gap_1920, o2448: block.settings.gap_2448 %}
  {% render 'vsn-responsive', scope: scope, prop: 'pad', d: block.settings.pad_d, t: block.settings.pad_t, m: block.settings.pad_m, adv: block.settings.adv, o320: block.settings.pad_320, o480: block.settings.pad_480, o560: block.settings.pad_560, o1024: block.settings.pad_1024, o1920: block.settings.pad_1920, o2448: block.settings.pad_2448 %}
{% endstyle %}
<div
  id="vsn-{{ block.id }}"
  class="vsn-group vsn-group--{{ block.settings.layout }} {{ block.settings.css_class | escape }}"
  {{ block.shopify_attributes }}
>
  {% content_for 'blocks' %}
</div>
""", {
    "name": "VSN Group",
    "blocks": [{"type": "@theme"}, {"type": "@app"}],
    "settings": [
        {"type": "select", "id": "layout", "label": "Layout", "options": opts([("flex", "Flex (row or stack)"), ("grid", "Grid")]), "default": "grid"},
        *rsel("cols", "Grid columns", [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6")], "4", "2", "2"),
        *rsel("dir", "Flex direction", [("row", "Row"), ("column", "Stack")], "row", "row", "column"),
        *rnum("gap", "Gap", 16, 12, 8),
        *rnum("pad", "Padding", 0, 0, 0),
        *common_tail(),
    ],
})

# ---------------- Global component ----------------
write("vsn-global-component", """
  VSN element: Global component (rule 15, architecture.md layer 4). Content and design live in theme
  settings slot 1-3 and stay synced on every page; each field can be overridden per instance
  (blank = use the synced value). Self-contained block: callers leave the body empty.
""", """
{%- liquid
  assign slot = block.settings.slot
  case slot
    when '2'
      assign g_head = settings.vsn_gc2_heading
      assign g_text = settings.vsn_gc2_text
      assign g_label = settings.vsn_gc2_label
      assign g_link = settings.vsn_gc2_link
      assign g_var = settings.vsn_gc2_variation
    when '3'
      assign g_head = settings.vsn_gc3_heading
      assign g_text = settings.vsn_gc3_text
      assign g_label = settings.vsn_gc3_label
      assign g_link = settings.vsn_gc3_link
      assign g_var = settings.vsn_gc3_variation
    else
      assign g_head = settings.vsn_gc1_heading
      assign g_text = settings.vsn_gc1_text
      assign g_label = settings.vsn_gc1_label
      assign g_link = settings.vsn_gc1_link
      assign g_var = settings.vsn_gc1_variation
  endcase
  assign head = block.settings.o_heading | default: g_head
  assign text = block.settings.o_text | default: g_text
  assign label = block.settings.o_label | default: g_label
  assign link = block.settings.o_link | default: g_link | default: routes.all_products_collection_url
-%}
<div
  id="vsn-{{ block.id }}"
  class="vsn-gc vsn-gc--{{ g_var }} {{ block.settings.css_class | escape }}"
  data-vsn-global-slot="{{ slot }}"
  {{ block.shopify_attributes }}
>
  {%- if head != blank -%}<h2 class="vsn-gc__heading">{{ head }}</h2>{%- endif -%}
  {%- if text != blank -%}<div class="vsn-gc__text">{{ text }}</div>{%- endif -%}
  {%- if label != blank -%}<a class="vsn-button vsn-button--{{ settings.vsn_button_variation }}" href="{{ link }}"><span>{{ label | escape }}</span></a>{%- endif -%}
</div>
""", {
    "name": "VSN Global component",
    "settings": [
        {"type": "select", "id": "slot", "label": "Global component", "options": opts([("1", "Global component 1"), ("2", "Global component 2"), ("3", "Global component 3")]), "default": "1", "info": "Edit the shared content and design in Theme settings → Global components."},
        {"type": "header", "content": "Overrides for this page (leave empty to use the shared value)"},
        {"type": "inline_richtext", "id": "o_heading", "label": "Heading override"},
        {"type": "richtext", "id": "o_text", "label": "Text override"},
        {"type": "text", "id": "o_label", "label": "Button label override"},
        {"type": "url", "id": "o_link", "label": "Button link override"},
        {"type": "header", "content": "Editing"},
        {"type": "text", "id": "css_class", "label": "Custom CSS class"},
    ],
})
