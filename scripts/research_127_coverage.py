#!/usr/bin/env python3
"""Validate the 127-preset research completion dashboard without falsifying demo work."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
BASE=ROOT/"banks/research/competitors"

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def check():
    errors=[]
    catalog=load(BASE/"shopify-presets-2026.json")
    source=load(BASE/"shopify-live-demo-evidence-2026.json")
    plan=load(BASE/"shopify-live-demo-plan-2026.json")
    matrix=load(BASE/"shopify-127-completion-matrix-2026.json")
    progress=load(ROOT/"ai/state/progress.json")
    selected=catalog.get("records",[])
    by_preset={s.get("catalog_preset_id"):s for s in source.get("stores",[]) if s.get("selected_127")}
    rows=matrix.get("presets",[])
    if len(selected)!=127 or len(rows)!=127:
        errors.append("127 official selected presets and 127 matrix rows required")
    ids=[r.get("selected_preset_id") for r in rows]
    if len(set(ids))!=len(ids):
        errors.append("Duplicate selected preset in matrix")
    catalog_ids={r.get("id") for r in selected}
    if set(ids)!=catalog_ids:
        errors.append("Matrix IDs not equal selected official catalog IDs")
    # Rendered browser observations are tracked separately from public indexed HTML.
    rendered=source.get("browser_render_observations",[])
    rendered_by_preset={}
    render_urls=set()
    render_home_ids=set()
    selected_ids={x.get("id") for x in selected}
    for record in rendered:
        preset_id=record.get("selected_preset_id")
        if preset_id not in selected_ids:
            errors.append("Rendered observation references an unselected preset: "+str(preset_id))
        if record.get("source_class")!="browser_render_readonly":
            errors.append("Rendered observation has unsupported source class: "+str(record.get("id")))
        pages=record.get("pages",[])
        seen_kinds=set()
        for page in pages:
            kind=page.get("kind")
            url=page.get("url","")
            if kind not in ("home","collection","product","cart"):
                errors.append("Invalid rendered page kind: "+str(kind))
            if kind in seen_kinds:
                errors.append("Duplicate rendered page kind: "+str(preset_id)+"/"+str(kind))
            seen_kinds.add(kind)
            if not url.startswith("https://") or url in render_urls:
                errors.append("Invalid or duplicate rendered page URL: "+str(url))
            render_urls.add(url)
            if page.get("evidence_class")!="browser_render_readonly" or page.get("interactions_executed") is not False:
                errors.append("Rendered page evidence scope is invalid: "+str(url))
        rendered_by_preset[preset_id]=[{"kind":p.get("kind"),"url":p.get("url"),"evidence_class":p.get("evidence_class")} for p in pages]
        if any(p.get("kind")=="home" for p in pages):
            render_home_ids.add(preset_id)
    expected_render_pages=sum(len(x.get("pages",[])) for x in rendered)
    indexed_home_ids={s.get("catalog_preset_id") for s in source.get("stores",[]) if s.get("selected_127") and s.get("homepage",{}).get("verification")=="public_html_document_opened"}
    any_home_ids=indexed_home_ids | render_home_ids
    if matrix.get("counts",{}).get("browser_rendered_pages")!=expected_render_pages:
        errors.append("Matrix rendered-page count differs from source evidence")
    if matrix.get("counts",{}).get("browser_rendered_selected_presets")!=len(rendered_by_preset):
        errors.append("Matrix rendered-preset count differs from source evidence")
    if matrix.get("counts",{}).get("distinct_selected_homepages_any_source")!=len(any_home_ids):
        errors.append("Matrix unique homepage count differs across source types")
    if matrix.get("pending",{}).get("home_any_source")!=127-len(any_home_ids):
        errors.append("Matrix any-source homepage backlog differs from source evidence")
    if plan.get("counts",{}).get("browser_rendered_pages")!=expected_render_pages:
        errors.append("Research plan rendered-page count differs from source evidence")
    if plan.get("counts",{}).get("browser_rendered_selected_presets")!=len(rendered_by_preset):
        errors.append("Research plan rendered-preset count differs from source evidence")
    if plan.get("counts",{}).get("selected_home_observed_any_source")!=len(any_home_ids):
        errors.append("Research plan unique homepage count differs across source types")
    expected={k:0 for k in ("home","collection","product","cart")}
    for row in rows:
        id_=row.get("selected_preset_id")
        matching=by_preset.get(id_,{})
        listing=next((x for x in selected if x.get("id")==id_),{})
        if row.get("official_listing",{}).get("url")!=listing.get("individual_listing_url"):
            errors.append("Official listing URL differs: "+str(id_))
        if row.get("official_listing",{}).get("status")!="official_listing_verified":
            errors.append("Unverified listing in 127 catalog: "+str(id_))
        for category,source_category in (("home","homepage"),("collection","collection"),("product","product"),("cart","cart")):
            record=matching.get(source_category)
            actual=bool(record and record.get("verification")=="public_html_document_opened")
            given=row.get("primary_demo",{}).get(source_category,{})
            if actual:expected[category]+=1
            if given.get("status")!=("public_indexed_html_opened" if actual else "not_verified"):
                errors.append("Missing/false page status: "+str(id_)+"/"+category)
            if given.get("url")!=(record.get("url") if record else None):
                errors.append("Page URL mismatch: "+str(id_)+"/"+category)
            if given.get("indexed_crawl_recency")!=(record.get("source_crawl_recency") if record else None):
                errors.append("Page crawl age mismatch: "+str(id_)+"/"+category)
        for key in ("actual_dom_interactions","mobile_viewport_render","private_theme_editor","checkout","real_lighthouse"):
            if row.get("test_scope",{}).get(key) is not False:
                errors.append("Unperformed test marked passed "+str(id_)+":"+key)
        expected_browser=rendered_by_preset.get(id_,[])
        given_browser=row.get("browser_render_observations",[])
        if given_browser!=expected_browser:
            errors.append("Rendered browser observations mismatch: "+str(id_))
        actual_extra=[d.get("url") for d in matching.get("supplemental_documentation",[])]
        if row.get("supplementary_indexed_html_urls")!=actual_extra:
            errors.append("Supplementary pages misrepresented: "+str(id_))
    counts=matrix.get("counts",{})
    if counts.get("official_listing")!=127:
        errors.append("Official listings not 127/127")
    if expected["home"]!=source.get("selected_127_document_count") or expected["home"]!=plan.get("counts",{}).get("live_home_demo_verified"):
        errors.append("Actual selected demo home and research plan mismatch")
    for key,plan_key in (("collection","live_collection_verified"),("product","live_product_verified"),("cart","live_cart_verified")):
        if expected[key]!=plan.get("counts",{}).get(plan_key):
            errors.append("Actual selected "+key+" and plan mismatch")
    for key,val in expected.items():
        if counts.get(key)!=val or matrix.get("pending",{}).get(key)!=127-val:
            errors.append("Dashboard "+key+" count not source derived")
    if matrix.get("completion_claim")!="INCOMPLETE_DIRECT_DEMO_COVERAGE_DO_NOT_ADVANCE_STAGE":
        errors.append("Cannot falsely mark unfinished live demo audit as complete")
    if expected["home"]<127 and progress.get("stage")!=2:
        errors.append("Stage advanced with incomplete selected demo HTML")
    if len(source.get("stores",[]))<55:
        errors.append("Historic 55 demo host floor must be maintained")
    primary=sum(sum(bool(s.get(x)) for x in ("homepage","collection","product","cart")) for s in source.get("stores",[]))
    if primary<151:
        errors.append("Historic 151 primary HTML documents floor must be maintained")
    return errors, expected

if __name__=="__main__":
    errors,counts=check()
    if errors:
        raise SystemExit("127-preset coverage audit FAILED:\n"+"\n".join("- "+e for e in errors))
    print("127-preset matrix OK; opened selected demo HTML home={home} collection={collection} product={product} cart={cart}; unfinished test categories remain blocked.".format(**counts))
