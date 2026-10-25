#!/usr/bin/env python3
"""Validate Shopify popular-theme families and preset evidence in VSN AI banks.
Usage: python3 scripts/shopify_theme_research.py validate|summary|next
Does not claim verification of dynamic Shopify storefront demo buttons.
"""
import collections
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent.parent
BANK=ROOT/"banks/research/competitors"
def read(p):
    with (BANK/p).open(encoding="utf-8") as h:
        return json.load(h)
def check_research():
    errors=[]
    try:
        families=read("shopify-families-2026.json")
        presets=read("shopify-presets-2026.json")
        external=read("shopify-external-themes-2026.json")
        popularity=read("shopify-popularity-top25-2026.json")
        audit=read("demo-audit.json")
        opts=json.loads((ROOT/"banks/options/options.json").read_text(encoding="utf-8"))
    except (OSError, ValueError, KeyError) as exc:
        return ["missing or invalid research bank: "+str(exc)]
    family_items=families.get("families",[])
    preset_items=presets.get("records",[])
    family_ids=set()
    paid_names=set()
    for family in family_items:
        fid=family["family_id"]
        if fid in family_ids:
            errors.append("duplicate theme family: "+fid)
        family_ids.add(fid)
        if family["official_url"]!=f"https://themes.shopify.com/themes/{fid}/presets/{fid}":
            errors.append("incorrect family official URL: "+fid)
        if family["mode"]=="paid_multi_preset":
            names=family.get("presets",[])
            if family.get("official_preset_count")!=len(names) or len(names)<2:
                errors.append("incorrect premium preset count: "+fid)
            if family["name"] not in names or len(set(names))!=len(names):
                errors.append("base name missing or duplicate presets: "+fid)
            for n in names:
                paid_names.add(fid+":"+n.lower().replace(" ","-"))
        elif family["mode"]!="standalone_free_theme" or family.get("presets") is not None:
            errors.append("standalone free classification invalid: "+fid)
    option_ids={x["id"] for x in opts["options"]}
    for family in family_items:
        for opt in family.get("feature_option_ids",[]):
            if opt not in option_ids:
                errors.append("unknown mapped option: "+family["family_id"]+" / "+opt)
        if family.get("live_demo_verified") is not False:
            errors.append("unverified live demo incorrectly marked verified: "+family["family_id"])
    preset_ids=set()
    seen_by_theme=collections.Counter()
    for item in preset_items:
        pid=item["id"]
        if pid in preset_ids:
            errors.append("duplicate design id: "+pid)
        preset_ids.add(pid)
        fid=item["theme_id"]
        seen_by_theme[fid]+=1
        if fid not in family_ids:
            errors.append("orphan design: "+pid)
        if item.get("individual_listing_page_verified") and not item.get("individual_listing_url"):
            errors.append("verified listing missing URL: "+pid)
        if item.get("individual_listing_url") and not item.get("individual_listing_page_verified"):
            errors.append("unopened listing has invented direct URL: "+pid)
        if any(item.get(x) for x in ("live_demo_home_verified","collection_verified","product_verified","cart_verified","mobile_verified")):
            errors.append("storefront interaction falsely marked verified: "+pid)
    for family in family_items:
        fid=family["family_id"]
        expected=len(family["presets"]) if family["presets"] is not None else 1
        if seen_by_theme[fid]!=expected:
            errors.append("preset index incomplete for "+fid)
    verified_count=sum(bool(x.get("individual_listing_page_verified")) for x in preset_items)
    if verified_count!=127:
        errors.append(f"all 127 selected official Shopify listing URLs must be individually verified; got {verified_count}")
    for item in preset_items:
        family_id=item["theme_id"]
        slug=item["preset_name"].lower().replace(" ","-")
        exact=f"https://themes.shopify.com/themes/{family_id}/presets/{slug}"
        if item.get("individual_listing_url")!=exact:
            errors.append("preset official listing URL mismatch: "+item["id"])
    if len(family_items)!=47 or len(preset_items)!=127:
        errors.append("catalog expected 47 family listings and 127 names")
    if sum(x["mode"]=="paid_multi_preset" for x in family_items)!=24:
        errors.append("premium family count mismatch")
    if sum(x["mode"]=="standalone_free_theme" for x in family_items)!=23:
        errors.append("standalone free count mismatch")
    if len(external.get("themes",[]))!=3:
        errors.append("external popular theme channel missing")
    if len(popularity.get("top25",[]))!=25:
        errors.append("popularity leaderboard snapshot incomplete")
    in_audit={(e.get("theme","").lower(),e.get("preset","").lower()) for e in audit.get("entries",[]) if e.get("platform")=="shopify"}
    for f in family_items:
        if (f["name"].lower(),f["name"].lower()) not in in_audit:
            errors.append("family not mapped to general research index: "+f["family_id"])
    return errors
def summary():
    f=read("shopify-families-2026.json")["families"]
    p=read("shopify-presets-2026.json")["records"]
    print(f"Shopify official parent listings: {len(f)}")
    print(f"Paid families: {sum(x['mode']=='paid_multi_preset' for x in f)}")
    print(f"Paid family preset names: {sum(len(x['presets']) for x in f if x['presets'] is not None)}")
    print(f"Standalone free themes: {sum(x['mode']=='standalone_free_theme' for x in f)}")
    print(f"Named design records: {len(p)}")
    print(f"Individually opened official pages: {sum(x['individual_listing_page_verified'] for x in p)}")
    print("Live storefront interactive demos verified: 0")
def main(argv):
    cmd=argv[0] if argv else "summary"
    if cmd=="validate":
        err=check_research()
        if err:
            print("Shopify research FAIL:\n - "+"\n - ".join(err))
            return 1
        print("Shopify research OK")
        summary()
    elif cmd=="summary":
        summary()
    elif cmd=="next":
        print("Shopify Theme Store View demo interactions and PDP/cart/mobile QA: not yet verified")
        print("Premium preset pages with unconfirmed direct URL:",sum(not x["individual_listing_page_verified"] for x in read("shopify-presets-2026.json")["records"]))
        print("External Ella/Minimog/Kalles: many demos still need individual live checks")
    else:
        print(__doc__)
        return 2
    return 0
if __name__=="__main__":
    sys.exit(main(sys.argv[1:]))
