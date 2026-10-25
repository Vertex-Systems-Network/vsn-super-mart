#!/usr/bin/env python3
"""Check Shopify theme editor/platform hard limits and honest demo QA statuses."""
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent.parent
BASE=ROOT/"banks/research/competitors"
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def check():
    errors=[]
    try:
        limits=load(BASE/"shopify-platform-limits-2026.json")
        editor=load(BASE/"shopify-editor-matrix-2026.json")
        audit=load(BASE/"shopify-live-demo-plan-2026.json")
        presets=load(BASE/"shopify-presets-2026.json")
        elements=load(ROOT/"banks/elements/elements.json")
    except (OSError, ValueError, KeyError) as e:
        return ["shopify phase 3 research missing: "+str(e)]
    if audit["counts"]["selected_design_records"]!=len(presets["records"]):
        errors.append("live demo plan mismatch with preset inventory")
    live=load(BASE/"shopify-live-demo-evidence-2026.json")
    stores=live.get("stores",[])
    if len(stores)<47 or len({d["id"] for d in stores})!=len(stores):
        errors.append("expected at least 47 distinct public demo document records")
    selected=[d for d in stores if d.get("selected_127")]
    for key,part in (("live_home_demo_verified","homepage"),("live_collection_verified","collection"),("live_product_verified","product"),("live_cart_verified","cart")):
        n=sum(bool(d.get(part) and d[part].get("verification")=="public_html_document_opened") for d in selected)
        if audit["counts"].get(key)!=n:
            errors.append("selected cohort document count mismatch: "+key)
    if audit["counts"].get("live_mobile_verified")!=0:
        errors.append("mobile UI not browser-tested")
    opts={x["id"] for x in load(ROOT/"banks/options/options.json")["options"]}
    els={x["id"] for x in elements["elements"]}
    entries={x["id"] for x in load(BASE/"demo-audit.json")["entries"]}
    cohort={x["id"] for x in presets["records"]}
    for store in stores:
        if store["id"] not in entries:
            errors.append("missing general audit record: "+store["id"])
        if store["selected_127"] and store.get("catalog_preset_id") not in cohort:
            errors.append("selected preset not in 127-name cohort")
        if any(store.get(k) for k in ("interactive_tested","mobile_render_tested","editor_tested")):
            errors.append("unsupported interactive test claim: "+store["id"])
        for page in ("homepage","collection","product","cart"):
            item=store.get(page)
            if item is None: continue
            if item.get("verification")!="public_html_document_opened" or not item.get("url","").startswith("https://"):
                errors.append("invalid page evidence "+store["id"]+"/"+page)
            for key,valid in (("option_ids",opts),("element_ids",els)):
                for oid in item.get(key,[]):
                    if oid not in valid: errors.append("unknown "+key+": "+oid)
    recipes=load(BASE/"shopify-vendor-homepage-recipes-2026.json")
    if len(recipes.get("presets",[]))!=4:
        errors.append("four Impulse vendor homepage recipes expected")
    for key, vals in recipes.get("section_to_vsn_elements",{}).items():
        for val in vals:
            if val not in els: errors.append("unmapped vendor element "+val)
    vendor=load(BASE/"shopify-vendor-settings-2026.json")
    specs=load(ROOT/"banks/elements/specs/shopify-local-commerce-controls-2026.json")
    if len(vendor.get("notes",[]))!=5 or len(specs.get("elements",[]))!=6:
        errors.append("developer setting references or proposed original control specs missing")
    known_opts={x["id"] for x in load(ROOT/"banks/options/options.json")["options"]}
    for record in vendor.get("notes",[]):
        if record.get("source_type") not in ("official_vendor_documentation","dated_official_vendor_release_notes"):
            errors.append("vendor settings mislabelled verified in private theme editor")
        for oid in record.get("mapped_options",[]):
            if oid not in known_opts: errors.append("unknown vendor setting option "+oid)
    for block in specs.get("elements",[]):
        if block.get("id") not in els: errors.append("unknown settings element id "+str(block.get("id")))
        for oid in block.get("option_ids",[]):
            if oid not in known_opts: errors.append("unknown element control option "+oid)
    issues=load(BASE/"shopify-demo-data-integrity-2026.json")
    ui=load(ROOT/"banks/elements/specs/shopify-retail-data-integrity-2026.json")
    if len(issues.get("cases",[]))!=5 or len(ui.get("elements",[]))!=5:
        errors.append("data QA and element settings specs incomplete")
    document_urls={p["url"] for store in stores for p in (store.get("homepage"),store.get("collection"),store.get("product"),store.get("cart")) if p}
    for issue in issues.get("cases",[]):
        if issue.get("source_url") not in document_urls:
            errors.append("data issue does not link an inspected page: "+str(issue.get("id")))
    for part in ui.get("elements",[]):
        if part["id"] not in els: errors.append("unknown QA element: "+part["id"])
        for oid in part.get("option_ids",[]):
            if oid not in opts: errors.append("unknown QA option: "+oid)
    count_map=(("opened_home","homepage"),("opened_collection","collection"),("opened_product","product"),("opened_empty_cart","cart"))
    for count_key,kind in count_map:
        actual=sum(bool(store.get(kind)) for store in stores)
        if live.get("counts",{}).get(count_key)!=actual:
            errors.append("document page count mismatch: "+count_key)
    deep=load(ROOT/"banks/elements/specs/shopify-home-category-pdp-controls-2026.json")
    if len(deep.get("elements",[]))!=5:
        errors.append("shopify category/search/variant proposed controls incomplete")
    seen_ids={s["id"] for s in stores}
    for linked in deep.get("sources",[]):
        if linked.get("id") not in seen_ids:
            errors.append("deep settings source not in demo bank")
    for block in deep.get("elements",[]):
        if block.get("id") not in els:
            errors.append("unknown planned Shopify element: "+str(block.get("id")))
        for opt in block.get("option_ids",[]):
            if opt not in opts: errors.append("unmapped option in deep settings: "+opt)
    for store in stores:
        for k in ("homepage","collection","product","cart"):
            p=store.get(k)
            if p and store["id"] in {x["id"] for x in deep.get("sources",[])} and not p.get("source_crawl_recency"):
                errors.append("batch5 page missing source crawl recency: "+store["id"]+"/"+k)
    batch6=load(BASE/"shopify-demo-source-claims-batch6-2026.json")
    ui=load(ROOT/"banks/elements/specs/shopify-merchandising-controls-batch6-2026.json")
    if len(batch6.get("examples",[]))!=6 or len(ui.get("controls",[]))!=6:
        errors.append("batch6 evidence issues/merchant controls incomplete")
    batch_urls={p["url"] for store in stores for p in (store.get("homepage"),store.get("collection"),store.get("product"),store.get("cart")) if p}
    for example in batch6.get("examples",[]):
        for key in ("source_url","other_source_url"):
            if key in example and example[key] not in batch_urls:
                errors.append("batch6 issue missing inspected source: "+example["id"])
    for item in ui.get("controls",[]):
        if item.get("id") not in els:
            errors.append("batch6 unknown element "+str(item.get("id")))
        for oid in item.get("option_ids",[]):
            if oid not in opts:
                errors.append("batch6 unknown option "+oid)
    for store in stores:
        if store["id"] in {s["id"] for s in ui.get("sources",[])}:
            for kind in ("homepage","collection","product","cart"):
                p=store.get(kind)
                if p and not p.get("source_crawl_recency"):
                    errors.append("batch6 missing page crawl provenance "+store["id"]+"/"+kind)
    batch7=load(BASE/"shopify-demo-source-claims-batch7-2026.json")
    ui7=load(ROOT/"banks/elements/specs/shopify-controls-batch7-2026.json")
    if len(batch7.get("examples",[]))!=6 or len(ui7.get("controls",[]))!=4:
        errors.append("batch7 risk cases/control specs incomplete")
    evidence_urls={p["url"] for s in stores for p in (s.get("homepage"),s.get("collection"),s.get("product"),s.get("cart")) if p}
    for ex in batch7.get("examples",[]):
        for k in ("source_url","related_url"):
            if ex.get(k) and ex[k] not in evidence_urls:
                errors.append("batch7 finding not linked to inspected document: "+ex["id"])
    for c in ui7.get("controls",[]):
        if c["id"] not in els: errors.append("batch7 unknown element: "+c["id"])
        for opt in c.get("option_ids",[]):
            if opt not in opts: errors.append("batch7 unknown option: "+opt)
    if live.get("selected_127_document_count",0)<24:
        errors.append("batch7 baseline fewer than 24 selected preset home documents")
    if sum(sum(bool(s.get(p)) for p in ("homepage","collection","product","cart")) for s in stores)<74:
        errors.append("batch7 baseline fewer than 74 independently opened page documents")
    if live.get("selected_127_document_count",0)<31:
        errors.append("batch8 baseline fewer than 31 selected preset home documents")
    if sum(sum(bool(s.get(k)) for k in ("homepage","collection","product","cart")) for s in stores)<89:
        errors.append("batch8 baseline fewer than 89 documents")
    if live.get("selected_127_document_count",0)<43 or sum(sum(bool(s.get(k)) for k in ("homepage","collection","product","cart")) for s in stores)<124:
        errors.append("batch9 historical minimum: fewer than 43 selected homes or 124 indexed HTML documents")
    # Batch 12: independently verified five Shopify demo PDP indexed HTML pages.
    b12=load(BASE/"shopify-pdp-source-claims-batch12-2026.json")
    expected_products={
        "shopify-live-pitch-free":"https://theme-pitch-demo.myshopify.com/products/age-serum",
        "shopify-live-sense-free":"https://theme-sense-demo.myshopify.com/products/natural-vegan-lip-balm-lemon-lime",
        "shopify-live-publisher-free":"https://theme-publisher-demo.myshopify.com/products/braulio-amado-2021",
        "shopify-live-trade-free":"https://theme-trade-demo.myshopify.com/products/classic-towels",
        "shopify-live-studio-free":"https://theme-studio-demo.myshopify.com/products/rhyme",
    }
    by_id={s["id"]:s for s in stores}
    for sid,url in expected_products.items():
        p=by_id.get(sid,{}).get("product")
        if not p or p.get("url")!=url or p.get("verification")!="public_html_document_opened" or not p.get("source_crawl_recency"):
            errors.append("Batch12 source/crawl age missing: "+sid)
    if len(b12.get("cases",[]))!=5 or len({x.get("id") for x in b12.get("cases",[])})!=5:
        errors.append("Batch12 source risk count/unique IDs inconsistent")
    seen_urls={s["product"]["url"] for s in stores if s.get("product")}
    for case in b12.get("cases",[]):
        if case.get("source_url") not in seen_urls or not case.get("vsn_guard"):
            errors.append("Batch12 unsourced/incomplete integrity guard "+str(case.get("id")))
    if sum(bool(s.get("product")) for s in stores)<37 or sum(sum(bool(s.get(k)) for k in ("homepage","collection","product","cart")) for s in stores)<129:
        errors.append("Batch12 minimum expected 37 PDP and 129 opened HTML documents")
    if audit["counts"].get("live_product_verified",0)<34:
        errors.append("Batch12 selected-PDP minimum fewer than 34")
    if editor.get("competitor_editor_tested") is not False:
        errors.append("competitor editor cannot be marked tested")
    if not editor.get("sources") or any(not u.startswith("https://shopify.dev/") and not u.startswith("https://help.shopify.com/") for u in editor["sources"]):
        errors.append("editor matrix must use only official Shopify documentation")
    caps=limits["hard_limits"]
    if caps.get("theme_block_files")!=300 or caps.get("theme_block_nesting_levels")!=8 or caps.get("sections_per_template")!=25:
        errors.append("platform block limits should match cited current Shopify docs")
    if limits.get("vsn_catalog_element_count")!=len(elements["elements"]):
        errors.append("element count should match current catalog")
    return errors
if __name__=="__main__":
    e=check()
    if e: print("Shopify editor audit FAIL: "+"; ".join(e));sys.exit(1)
    print("Shopify editor audit OK: %d Shopify demo HTML stores (%d selected home sources), interactive/mobile tests pending" % (len(load(BASE/"shopify-live-demo-evidence-2026.json")["stores"]), load(BASE/"shopify-live-demo-evidence-2026.json")["selected_127_document_count"]))
