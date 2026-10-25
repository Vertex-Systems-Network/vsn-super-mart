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
    if len(stores)!=4 or len({d["id"] for d in stores})!=4:
        errors.append("expected four distinct public demo document records")
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
    print("Shopify editor audit OK: 4 Shopify demo HTML stores (2 in cohort), interaction/mobile checks still pending")
