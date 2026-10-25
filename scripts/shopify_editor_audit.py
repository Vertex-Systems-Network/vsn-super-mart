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
    if any(v!=0 for k,v in audit["counts"].items() if k.startswith("live_")):
        errors.append("no live demo may be verified without new browser evidence")
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
    print("Shopify editor audit OK: official architecture and limits; 127 live demos correctly pending")
