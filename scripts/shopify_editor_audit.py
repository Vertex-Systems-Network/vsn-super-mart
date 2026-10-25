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
    # Batch13: primary PDP/cart and separate supplementary evidence; no interactive inference.
    b13=load(BASE/"shopify-source-claims-batch13-2026.json")
    by_id={s["id"]:s for s in stores}
    verified_b13={
        ("shopify-live-horizon-free","product"):"https://theme-horizon-demo.myshopify.com/products/1tuck-tapered-pants-424",
        ("shopify-live-spotlight-free","cart"):"https://theme-spotlight-demo.myshopify.com/cart",
    }
    for (sid,kind),url in verified_b13.items():
        item=by_id.get(sid,{}).get(kind)
        if not item or item.get("url")!=url or item.get("verification")!="public_html_document_opened" or not item.get("source_crawl_recency"):
            errors.append("Batch13 missing individually opened primary document: "+sid+"/"+kind)
    extra={
        "shopify-live-stiletto-glimmer":"https://stiletto-theme-glimmer.myshopify.com/collections/minis",
        "shopify-live-pitch-free":"https://theme-pitch-demo.myshopify.com/collections/bundles",
    }
    for sid,url in extra.items():
        sources=by_id.get(sid,{}).get("supplemental_documentation",[])
        if not any(x.get("url")==url and x.get("verification")=="public_html_document_opened" for x in sources):
            errors.append("Batch13 missing separate supplemental HTML document: "+sid)
    primary_urls={x["url"] for s in stores for x in (s.get("homepage"),s.get("collection"),s.get("product"),s.get("cart")) if x}
    supplement_urls={x.get("url") for s in stores for x in s.get("supplemental_documentation",[])}
    if len(b13.get("cases",[]))!=3 or len({c.get("id") for c in b13.get("cases",[])})!=3:
        errors.append("Batch13 expected three unique integrity cases")
    for case in b13.get("cases",[]):
        if case.get("source_url") not in primary_urls|supplement_urls or not case.get("vsn_guard"):
            errors.append("Batch13 missing supporting evidence/guardrail: "+str(case.get("id")))
    page_count=sum(sum(bool(s.get(k)) for k in ("homepage","collection","product","cart")) for s in stores)
    if page_count<131 or sum(bool(s.get("product")) for s in stores)<38 or sum(bool(s.get("cart")) for s in stores)<9:
        errors.append("Batch13 history floor: 131 primary HTML pages, 38 PDP and 9 cart")
    if audit["counts"].get("live_product_verified",0)<35 or audit["counts"].get("live_cart_verified",0)<9:
        errors.append("Batch13 selected PDP/cart cohort floor")
    # Batch 14 Expanse homepage vendor document recipes / Shopify current CSS & variant risks.
    b14=load(BASE/"shopify-vendor-homepage-recipes-expanse-batch14-2026.json")
    css14=load(BASE/"shopify-dynamic-render-qa-batch14-2026.json")
    source="https://help.archetypethemes.co/hc/en-us/articles/51462622741523-Expanse-theme-homepage-breakdown"
    if b14.get("source_url")!=source or b14.get("evidence_type")!="official_vendor_documentation_only":
        errors.append("Batch14 vendor homepage source/provenance missing")
    all_recipes=b14.get("presets",[])
    if len(all_recipes)!=5 or {p.get("name") for p in all_recipes}!={"Expanse","Revive","Spritz","Fetch","Gem"}:
        errors.append("Batch14 requires five unique sourced Expanse-family recipes")
    if b14.get("selected_demo_homepage_count_added")!=0:
        errors.append("Vendor recipes must never increase live demo count")
    for recipe in all_recipes:
        arr=recipe.get("homepage_sections",[])
        if len(arr)!=recipe.get("documented_total_including_groups") or len(arr)<10:
            errors.append("Batch14 recipe section-order size mismatch "+str(recipe.get("name")))
        if any(section not in b14.get("section_to_vsn",{}) for section in arr):
            errors.append("Batch14 recipe has unmapped module "+str(recipe.get("name")))
        if recipe.get("template_sections_excluding_header_footer")!=sum(x not in ("header-group","footer","footer-promotions") for x in arr):
            errors.append("Batch14 recipe has incorrect template section count")
        if recipe.get("selected_127") and recipe.get("catalog_preset_id") not in cohort:
            errors.append("Batch14 selected preset not in 127 cohort")
        if recipe.get("name")=="Fetch" and (recipe.get("catalog_preset_id")!="expanse:fetch" or not recipe.get("selected_127")):
            errors.append("Batch15 correction: Expanse Fetch is part of selected 127 cohort")
        if recipe.get("name")=="Fetch" and not any(x.get("catalog_preset_id")=="expanse:fetch" and x.get("selected_127") for x in stores):
            errors.append("Batch15 correction: missing previously audited Fetch demo HTML")
        if recipe.get("verification")!="vendor_documented_homepage_sections_not_live_demo_html":
            errors.append("Batch14 vendor recipe falsely presented as live source")
    for kind, mapping in b14.get("section_to_vsn",{}).items():
        for oid in mapping.get("option_ids",[]):
            if oid not in opts:
                errors.append("Batch14 unknown option "+kind+"/"+oid)
        for eid in mapping.get("element_ids",[]):
            if eid not in els:
                errors.append("Batch14 unknown element "+kind+"/"+eid)
    if "requires new native" not in b14.get("section_to_vsn",{}).get("image-comparison",{}).get("mapping_status",""):
        errors.append("Batch14 before-after image comparison element gap must be explicit")
    srcs=css14.get("sources",{})
    if len(css14.get("cases",[]))!=6 or css14.get("vsn_qa_executed") is not False:
        errors.append("Batch14 needs six unexecuted source-linked QA scenarios")
    for c in css14.get("cases",[]):
        if not c.get("qa_gate") or not c.get("vsn_design_action") or not c.get("source_ids"):
            errors.append("Batch14 QA case lacks source, action or test: "+str(c.get("id")))
        for sid in c.get("source_ids",[]):
            if sid not in srcs or not srcs[sid].startswith("https://"):
                errors.append("Batch14 bad QA citation key: "+str(sid))
    # Batch15: externally reported performance is not original VSN/mobile demo verification.
    perf15=load(BASE/"shopify-third-party-pagespeed-batch15-2026.json")
    sample15=perf15.get("samples",[])
    if len(sample15)!=18 or len({p.get("catalog_preset_id") for p in sample15})!=18:
        errors.append("Batch15 requires 18 uniquely mapped preset performance reports")
    for metric in sample15:
        sid=metric.get("catalog_preset_id")
        if sid not in cohort or metric.get("evidence_level")!="third_party_reported_google_pagespeed_insights_lab_snapshot":
            errors.append("Batch15 source provenance or cohort mismatch: "+str(sid))
        if metric.get("vsn_own_lab_test") is not False or metric.get("live_demo_html_verified_in_this_batch") is not False:
            errors.append("Batch15 cannot claim own performance test or visited storefront")
        if not 0<=metric.get("mobile_lighthouse_performance",-1)<=100 or not 0<=metric.get("desktop_lighthouse_performance",-1)<=100:
            errors.append("Batch15 bad reported score")
        if metric.get("mobile_lab_lcp_seconds",0)<=0 or not metric.get("metric_source_url","").startswith("https://ediy.io/"):
            errors.append("Batch15 source URL or LCP missing")
    if perf15.get("count_changes",{}).get("new_live_html_docs")!=0 or perf15.get("count_changes",{}).get("new_mobile_browser_render_tests")!=0:
        errors.append("Batch15 reported lab snapshots cannot inflate direct HTML/mobile QA")
    limits15=perf15.get("shopify_theme_store_requirement",{})
    if limits15.get("lighthouse_performance_mean_minimum")!=60 or limits15.get("lighthouse_accessibility_mean_minimum")!=90:
        errors.append("Batch15 Theme Store requirements inconsistent")
    # Batch16 verified public indexed Shopify Impact/Expanse demo HTML.
    b16=load(BASE/"shopify-source-claims-batch16-2026.json")
    ref16={
        "shopify-live-impact-sound":{
            "catalog_preset_id":"impact:impact",
            "homepage":"https://impact-theme-sound.myshopify.com/",
            "product":"https://impact-theme-sound.myshopify.com/products/mw07-plus-leica",
            "cart":"https://impact-theme-sound.myshopify.com/cart",
        },
        "shopify-live-expanse-furniture":{
            "catalog_preset_id":"expanse:expanse",
            "homepage":"https://expanse-theme-furniture.myshopify.com/",
            "collection":"https://expanse-theme-furniture.myshopify.com/collections/furniture",
            "product":"https://expanse-theme-furniture.myshopify.com/collections/coffee-makers/products/90018-neapolitan-coffee-maker",
        }
    }
    indexed16={s["id"]:s for s in stores}
    for sid,entry in ref16.items():
        s=indexed16.get(sid,{})
        if s.get("catalog_preset_id")!=entry["catalog_preset_id"] or not s.get("selected_127"):
            errors.append("Batch16 missing exact selected theme/preset: "+sid)
        for typ,url in entry.items():
            if typ=="catalog_preset_id":continue
            page=s.get(typ)
            if not page or page.get("url")!=url or page.get("verification")!="public_html_document_opened" or not page.get("source_crawl_recency"):
                errors.append("Batch16 missing individual public indexed HTML source and crawl age: "+sid+"/"+typ)
    if len(stores)<49 or sum(sum(bool(s.get(k)) for k in ("homepage","collection","product","cart")) for s in stores)<137:
        errors.append("Batch16 historic floor of 49 stores and 137 primary HTML docs")
    if audit["counts"].get("live_home_demo_verified",0)<45 or audit["counts"].get("live_collection_verified",0)<34 or audit["counts"].get("live_product_verified",0)<37 or audit["counts"].get("live_cart_verified",0)<10:
        errors.append("Batch16 selected preset document count below historic verified floor")
    if len(b16.get("cases",[]))!=5 or len({r.get("id") for r in b16.get("cases",[])})!=5:
        errors.append("Batch16 must retain five source-linked merchant QA cases")
    allurls={p["url"] for s in stores for p in [s.get("homepage"),s.get("collection"),s.get("product"),s.get("cart")] if p}
    for c in b16.get("cases",[]):
        if c.get("source_url") not in allurls or not c.get("vsn_guard") or not c.get("source_crawl_recency"):
            errors.append("Batch16 unsourced or incomplete risk guard: "+str(c.get("id")))
    # Batch17 Release default + Forest premium demo independently opened source URLs.
    b17=load(BASE/"shopify-source-claims-batch17-2026.json")
    expected17={
        "shopify-live-release-release":{
            "catalog_preset_id":"release:release",
            "homepage":"https://release-main.myshopify.com/",
            "collection":"https://release-main.myshopify.com/collections/new-collection",
            "product":"https://release-main.myshopify.com/products/black-puffer-edge?variant=42204594929743",
            "cart":"https://release-main.myshopify.com/cart",
        },
        "shopify-live-release-forest":{
            "catalog_preset_id":"release:forest",
            "homepage":"https://release-living.myshopify.com/",
            "collection":"https://release-living.myshopify.com/collections/living-room",
        }
    }
    by_id17={s["id"]:s for s in stores}
    for sid,expect in expected17.items():
        store=by_id17.get(sid,{})
        if store.get("catalog_preset_id")!=expect["catalog_preset_id"] or not store.get("selected_127"):
            errors.append("Batch17 selected preset ID wrong: "+sid)
        for page,url in expect.items():
            if page=="catalog_preset_id":continue
            item=store.get(page)
            if not item or item.get("url")!=url or item.get("verification")!="public_html_document_opened" or not item.get("source_crawl_recency"):
                errors.append("Batch17 source/crawl age missing: "+sid+"/"+page)
        if any(store.get(f) for f in ("interactive_tested","mobile_render_tested","editor_tested")):
            errors.append("Batch17 falsely claimed functional/mobile/editor visit: "+sid)
    if by_id17.get("shopify-live-release-forest",{}).get("product") or by_id17.get("shopify-live-release-forest",{}).get("cart"):
        errors.append("Batch17 Forest PDP/cart were not retrieved; never count without evidence")
    total17=sum(sum(bool(s.get(k)) for k in ("homepage","collection","product","cart")) for s in stores)
    if len(stores)<51 or total17<143:
        errors.append("Batch17 historic minimum: 51 demo hosts, 143 primary HTML documents")
    if audit["counts"].get("live_home_demo_verified",0)<47 or audit["counts"].get("live_collection_verified",0)<36 or audit["counts"].get("live_product_verified",0)<38 or audit["counts"].get("live_cart_verified",0)<11:
        errors.append("Batch17 selected cohort count below independently opened source floor")
    all17={p["url"] for s in stores for p in (s.get("homepage"),s.get("collection"),s.get("product"),s.get("cart")) if p}
    if len(b17.get("cases",[]))!=4 or len({c.get("id") for c in b17.get("cases",[])})!=4:
        errors.append("Batch17 requires exactly four unique source claim QA cases")
    for case in b17.get("cases",[]):
        if case.get("source_url") not in all17 or not case.get("vsn_guard") or not case.get("source_age"):
            errors.append("Batch17 unsourced merchant QA case "+str(case.get("id")))
    # Batch18 vendor source and independent reviewer scope: zero new firsthand demo HTML or interactions.
    b18=load(BASE/"shopify-vendor-regression-batch18-2026.json")
    review18=load(BASE/"shopify-independent-review-batch18-2026.json")
    if b18.get("evidence_scope")!="official Shopify Theme Store vendor release notes and first-party vendor marketing; NOT competitor live storefront HTML, NOT executed VSN functional QA":
        errors.append("Batch18 vendor notes mislabeled as firsthand demo")
    if b18.get("demo_homepage_newly_opened")!=0 or b18.get("interactions_executed_by_vsn")!=0:
        errors.append("Batch18 unexecuted vendor regression tests falsely counted")
    if len(b18.get("checks",[]))!=8 or len({i.get("id") for i in b18.get("checks",[])})!=8:
        errors.append("Batch18 missing 8 distinct release-derived QA scenarios")
    source18={i.get("id"):i.get("url") for i in b18.get("sources",[])}
    for check in b18.get("checks",[]):
        if check.get("status")!="not_executed" or check.get("evidence_level")!="vendor_published_change_note_or_marketing":
            errors.append("Batch18 QA executed without actual test "+str(check.get("id")))
        if check.get("source_url")!=source18.get(check.get("source_key")) or not check.get("source_url","").startswith("https://"):
            errors.append("Batch18 missing source link for "+str(check.get("id")))
        if check.get("catalog_preset_id") not in cohort or not check.get("planned_qa") or not check.get("original_vsn_design_rule"):
            errors.append("Batch18 unknown selected theme or missing QA plan "+str(check.get("id")))
        for oid in check.get("option_ids",[]):
            if oid not in opts:errors.append("Batch18 unknown option "+oid)
        for eid in check.get("element_ids",[]):
            if eid not in els:errors.append("Batch18 unknown element "+eid)
    if review18.get("direct_storefront_url_opened_by_vsn") is not False or review18.get("vsn_mobile_or_interactive_tests")!=0:
        errors.append("Batch18 third party article is not own browser interaction QA")
    if len(review18.get("items",[]))!=5 or len(set(i.get("id") for i in review18.get("items",[])))!=5:
        errors.append("Batch18 requires 5 third-party reviewed examples")
    for item in review18.get("items",[]):
        if item.get("preset") not in cohort or not item.get("claim") or not item.get("original_implication"):
            errors.append("Batch18 reviewer claim not traceable: "+str(item.get("id")))
        for oid in item.get("mapped_option_ids",[]):
            if oid not in opts:errors.append("Batch18 unknown review option "+oid)
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
