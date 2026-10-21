#!/usr/bin/env python3
"""VSN Super Mart workflow CLI (stdlib only).

  status                       stage, niche, next action, gate result
  log "<text>"                 append to ai/state/log.md
  next "<text>"                set next_action
  set-niche <id>               set current niche (Stage 1)
  approve <stage> "<who>"      record a human approval (stages 4, 6, 9)
  advance                      check the current stage gate, then move to the next stage
  validate                     validate all banks
  resolve-options <niche>      write ai/niches/<niche>/options.resolved.json
  coverage <spec.json>         every required option + Theme Store requirement covered?
  check-design <file.json>     uniqueness vs registry + competitors (spec, direction or directions list)
  register-design <spec.json>  add a design to banks/design/registry.json
  new-niche <id> "<name>"      scaffold a research file for a niche not in the bank
"""
import colorsys, datetime, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
STATE = P("ai", "state", "progress.json")
STAGES = {0: "Bootstrap", 1: "Niche intake", 2: "Niche research", 3: "Options mapping",
          4: "Design search & direction", 5: "Design spec", 6: "Figma build",
          7: "Development", 8: "QA", 9: "Release preset"}
HUMAN_GATES = {4, 6, 9}
NEXT_HINT = {
    1: "Ask the human which niche (see banks/research/niches/index.json). Create ai/niches/<niche>/brief.md from ai/templates/niche-brief.md, then `vsn.py set-niche <niche>`.",
    2: "Deepen + verify banks/research/niches/<niche>.json with real sources (prompt: ai/prompts/2-research.md). Set status to 'verified'.",
    3: "Add new options to banks/options/options.json, then `vsn.py resolve-options <niche>`.",
    4: "Design search, write banks/design/specs/<niche>/directions.json with 3 directions, `vsn.py check-design` it, present to human, `vsn.py approve 4 \"<name>\"` + set 'chosen'.",
    5: "Write banks/design/specs/<niche>/spec.json (template: ai/templates/design-spec.json) until `vsn.py coverage` and `check-design` pass.",
    6: "Build in Figma page 'VSN | Super Mart' (25:2), add node ids to spec, `vsn.py register-design <spec>`, get approval `vsn.py approve 6`.",
    7: "Build theme work units listed in ai/niches/<niche>/work-units.md (prompt: ai/prompts/7-develop.md).",
    8: "Run QA (ai/prompts/8-qa.md), write ai/niches/<niche>/qa-report.md with no open blockers.",
    9: "Finalize preset name, docs, CHANGELOG; `vsn.py approve 9`; advance to start the next niche.",
}


def load(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


def today():
    return datetime.date.today().isoformat()


def state():
    return load(STATE)


def save_state(s):
    s["updated_at"] = today()
    save(STATE, s)


def log(text):
    path = P("ai", "state", "log.md")
    new = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as f:
        if new:
            f.write("# Activity log (append-only)\n\n")
        s = state()
        f.write(f"- {datetime.datetime.now():%Y-%m-%d %H:%M} [stage {s['stage']}"
                f"{' / ' + s['current_niche'] if s.get('current_niche') else ''}] {text}\n")


# ---------------- banks ----------------
def options():
    return load(P("banks", "options", "options.json"))["options"]


def requirements():
    return load(P("banks", "research", "platform", "theme-store-requirements.json"))["requirements"]


def niche_file(n):
    return P("banks", "research", "niches", f"{n}.json")


def required_options(niche):
    out = []
    for o in options():
        if not o["store_allowed"]:
            continue
        in_scope = o["scope"] == "core" or (isinstance(o["scope"], list) and niche in o["scope"])
        if in_scope and (o["priority"] == "must" or o["theme_store_required"]):
            out.append(o["id"])
    return out


def validate(verbose=True):
    errs = []
    opts = options()
    ids = [o["id"] for o in opts]
    if len(ids) != len(set(ids)):
        errs.append("options: duplicate ids")
    for o in opts:
        for k in ("id", "name", "audience", "area", "priority", "scope", "store_allowed"):
            if k not in o:
                errs.append(f"option {o.get('id')}: missing {k}")
        if o.get("priority") not in ("must", "should", "could"):
            errs.append(f"option {o['id']}: bad priority")
    req_keys = ["id", "name", "must_have_sections", "product_page_elements", "design_patterns",
                "competitor_references", "sources"]
    idx = load(P("banks", "research", "niches", "index.json"), {"niches": []})
    for n in idx["niches"]:
        d = load(niche_file(n["id"]))
        if d is None:
            errs.append(f"niche {n['id']}: file missing")
            continue
        for k in req_keys:
            if k not in d:
                errs.append(f"niche {n['id']}: missing {k}")
    reg = load(P("banks", "design", "registry.json"))
    schema = load(P("banks", "design", "fingerprint-schema.json"))
    comp = load(P("banks", "design", "competitor-fingerprints.json"))
    for e in reg["designs"] + comp["fingerprints"]:
        errs += [f"fingerprint {e.get('id')}: {x}" for x in fp_errors(e.get("fp", {}), schema)]
    log_ = load(P("banks", "design", "image-log.json"), {"images": []})
    for im in log_["images"]:
        for k in ("id", "niche", "slot", "prompt", "model", "figma_node", "used_in"):
            if not im.get(k):
                errs.append(f"image {im.get('id')}: missing {k}")
    if verbose:
        print("validate: OK" if not errs else "validate: FAIL\n  " + "\n  ".join(errs))
    return not errs


def niche_research_ok(n):
    d = load(niche_file(n))
    if not d:
        return False, "research file missing"
    probs = []
    if len(d.get("must_have_sections", [])) < 10:
        probs.append("<10 must-have sections")
    if len(d.get("sources", [])) < 3:
        probs.append("<3 sources")
    if len(d.get("competitor_references", [])) < 3:
        probs.append("<3 competitor references")
    if d.get("status") != "verified":
        probs.append("status is not 'verified'")
    return not probs, ", ".join(probs) or "ok"


def resolve_options(niche):
    opts = options()
    sel = [o for o in opts if o["store_allowed"] and (o["scope"] == "core" or
           (isinstance(o["scope"], list) and niche in o["scope"]))]
    extras = [o["id"] for o in opts if not o["store_allowed"] and o["scope"] != []]
    research = load(niche_file(niche), {})
    opt_ids = {o["id"] for o in opts}
    unmapped = [s["id"] for s in research.get("must_have_sections", [])
                if s["id"] not in opt_ids and s["id"] not in research.get("option_map", {})]
    out = {"niche": niche, "generated_at": today(),
           "must": [o["id"] for o in sel if o["priority"] == "must" or o["theme_store_required"]],
           "should": [o["id"] for o in sel if o["priority"] == "should" and not o["theme_store_required"]],
           "could": [o["id"] for o in sel if o["priority"] == "could"],
           "extras_track_only": extras,
           "unmapped_research_sections": unmapped}
    save(P("ai", "niches", niche, "options.resolved.json"), out)
    print(f"resolved: must={len(out['must'])} should={len(out['should'])} could={len(out['could'])}")
    if unmapped:
        print("UNMAPPED research must-have sections (add to options bank, or map them in the research "
              "file's 'option_map' {section_id: option_id}):\n  " + ", ".join(unmapped))
    return out


def coverage(spec_path, verbose=True):
    spec = load(spec_path)
    niche = spec["niche"]
    covered = set(spec.get("option_map", {}).keys())
    covered_req = set(spec.get("requirement_map", {}).keys())
    miss_o = [o for o in required_options(niche) if o not in covered]
    miss_r = [r["id"] for r in requirements() if r["id"] not in covered_req]
    ok = not miss_o and not miss_r
    if verbose:
        tot_o = len(required_options(niche))
        print(f"coverage: options {tot_o - len(miss_o)}/{tot_o}, requirements "
              f"{len(requirements()) - len(miss_r)}/{len(requirements())} -> {'PASS' if ok else 'FAIL'}")
        if miss_o:
            print("  missing options: " + ", ".join(miss_o))
        if miss_r:
            print("  missing requirements: " + ", ".join(miss_r))
    return ok


# ---------------- design uniqueness ----------------
def fp_errors(fp, schema):
    errs = []
    for dim, values in schema["dimensions"].items():
        if dim not in fp:
            errs.append(f"missing dimension {dim}")
        elif fp[dim] not in values:
            errs.append(f"{dim}='{fp[dim]}' not in schema (add it to fingerprint-schema.json if new)")
    return errs


def hue(hex_):
    h = hex_.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    return hh * 360, ss, ll


def palette_match(a, b, tol):
    if not a or not b:
        return False
    (h1, s1, l1), (h2, s2, l2) = hue(a[0]), hue(b[0])
    if s1 < 0.15 and s2 < 0.15:  # both near-neutral accents
        return abs(l1 - l2) < 0.2
    d = abs(h1 - h2) % 360
    return min(d, 360 - d) <= tol and abs(l1 - l2) < 0.3


def similarity(x, y, schema):
    dims = list(schema["dimensions"])
    same = [d for d in dims if x["fp"].get(d) == y["fp"].get(d)]
    pal = palette_match(x.get("palette"), y.get("palette"), schema["palette_hue_tolerance_deg"])
    score = (len(same) + (1 if pal else 0)) / (len(dims) + 1)
    return score, same + (["palette"] if pal else [])


def check_design(path, verbose=True):
    schema = load(P("banks", "design", "fingerprint-schema.json"))
    data = load(path)
    cands = data["directions"] if "directions" in data else [data]
    others = load(P("banks", "design", "registry.json"))["designs"] + \
        load(P("banks", "design", "competitor-fingerprints.json"))["fingerprints"]
    all_ok = True
    for i, c in enumerate(cands):
        cid = c.get("id", f"candidate-{i + 1}")
        errs = fp_errors(c.get("fp", {}), schema)
        if errs:
            print(f"[{cid}] INVALID: " + "; ".join(errs))
            all_ok = False
            continue
        pool = [o for o in others if o.get("id") != cid] + \
               [dict(o, id=o.get("id", f"candidate-{j + 1}")) for j, o in enumerate(cands) if j != i]
        worst = (0, None, [])
        for o in pool:
            s, same = similarity(c, o, schema)
            if s > worst[0]:
                worst = (s, o.get("id"), same)
        verdict = "FAIL" if worst[0] >= schema["thresholds"]["fail"] else \
            "WARN" if worst[0] >= schema["thresholds"]["warn"] else "PASS"
        if verdict == "FAIL":
            all_ok = False
        if verbose:
            print(f"[{cid}] {verdict}: max similarity {worst[0]:.2f} with '{worst[1]}'"
                  + (f" (same: {', '.join(worst[2])})" if worst[2] else ""))
    return all_ok


def register_design(path):
    spec = load(path)
    reg_path = P("banks", "design", "registry.json")
    reg = load(reg_path)
    entry = {"id": spec["id"], "niche": spec["niche"], "name": spec.get("name"),
             "fp": spec["fp"], "palette": spec.get("palette", []),
             "figma": spec.get("figma", {}), "spec": os.path.relpath(path, ROOT),
             "registered_at": today()}
    reg["designs"] = [d for d in reg["designs"] if d["id"] != entry["id"]] + [entry]
    save(reg_path, reg)
    print(f"registered {entry['id']}")


# ---------------- gates ----------------
def gate(s):
    st, n = s["stage"], s.get("current_niche")
    nd = P("ai", "niches", n or "_")
    if st == 0:
        return validate(False), "banks valid"
    if st == 1:
        b = os.path.join(nd, "brief.md")
        if not n or not os.path.exists(b):
            return False, "no niche set or brief.md missing"
        txt = open(b, encoding="utf-8").read()
        return ("TODO" not in txt), "brief has no TODO left" if "TODO" not in txt else "brief still has TODO fields"
    if st == 2:
        return niche_research_ok(n)
    if st == 3:
        r = load(os.path.join(nd, "options.resolved.json"))
        if not r:
            return False, "run resolve-options"
        return (not r["unmapped_research_sections"]), f"unmapped: {r['unmapped_research_sections']}"
    spec = P("banks", "design", "specs", n or "_", "spec.json")
    if st == 4:
        d = P("banks", "design", "specs", n or "_", "directions.json")
        if not os.path.exists(d):
            return False, "directions.json missing"
        dj = load(d)
        if not dj.get("chosen"):
            return False, "no 'chosen' direction id in directions.json"
        if "4" not in s.get("approvals", {}):
            return False, "needs human approval: vsn.py approve 4 \"<name>\""
        chosen = [x for x in dj["directions"] if x["id"] == dj["chosen"]]
        tmp = P("ai", "state", ".chosen.json")
        save(tmp, chosen[0] if chosen else {})
        ok = bool(chosen) and check_design(tmp, False)
        os.remove(tmp)
        return ok, "chosen direction unique" if ok else "chosen direction fails uniqueness"
    if st == 5:
        if not os.path.exists(spec):
            return False, "spec.json missing"
        ok = coverage(spec) and check_design(spec)
        return ok, "coverage + uniqueness"
    if st == 6:
        reg = load(P("banks", "design", "registry.json"))
        if not any(d["niche"] == n for d in reg["designs"]):
            return False, "design not registered"
        return ("6" in s.get("approvals", {})), "needs approval 6" if "6" not in s.get("approvals", {}) else "approved"
    if st == 7:
        w = os.path.join(nd, "work-units.md")
        if not os.path.exists(w):
            return False, "work-units.md missing"
        open_units = [l for l in open(w, encoding="utf-8") if l.strip().startswith("- [ ]")]
        return not open_units, f"{len(open_units)} open work units"
    if st == 8:
        q = os.path.join(nd, "qa-report.md")
        if not os.path.exists(q):
            return False, "qa-report.md missing"
        return "BLOCKER" not in open(q, encoding="utf-8").read(), "no BLOCKER lines"
    if st == 9:
        return ("9" in s.get("approvals", {})), "release approval"
    return False, "unknown stage"


def cmd_status():
    s = state()
    ok, why = gate(s)
    print(f"Stage {s['stage']}: {s['stage_name']}   cycle {s['cycle']}")
    print(f"Niche: {s.get('current_niche') or '-'}   completed: {', '.join(s['completed_niches']) or '-'}")
    print(f"Gate: {'PASS' if ok else 'not yet'} ({why})")
    print(f"Next action: {s['next_action']}")
    print("Handoff notes: ai/state/HANDOFF.md")


def cmd_advance():
    s = state()
    ok, why = gate(s)
    if not ok:
        print(f"Gate for stage {s['stage']} not passed: {why}")
        sys.exit(1)
    if s["stage"] == 9:
        s["completed_niches"].append(s["current_niche"])
        s.update(stage=1, cycle=s["cycle"] + 1, current_niche=None, approvals={})
    else:
        s["stage"] += 1
    s["stage_name"] = STAGES[s["stage"]]
    s["next_action"] = f"Stage {s['stage']}: " + NEXT_HINT[s["stage"]]
    save_state(s)
    log(f"advanced to stage {s['stage']} ({s['stage_name']})")
    cmd_status()


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    c, a = argv[0], argv[1:]
    if c == "status":
        cmd_status()
    elif c == "log":
        log(" ".join(a)); print("logged")
    elif c == "next":
        s = state(); s["next_action"] = " ".join(a); save_state(s); print("next_action set")
    elif c == "set-niche":
        n = a[0]
        if not os.path.exists(niche_file(n)):
            print(f"no research file for '{n}'. Run: vsn.py new-niche {n} \"<Name>\""); sys.exit(1)
        s = state(); s["current_niche"] = n; save_state(s); log(f"niche set to {n}"); print(f"niche = {n}")
    elif c == "approve":
        s = state(); s.setdefault("approvals", {})[a[0]] = {"by": " ".join(a[1:]) or "human", "on": today()}
        save_state(s); log(f"approval stage {a[0]} by {' '.join(a[1:])}"); print("approved")
    elif c == "advance":
        cmd_advance()
    elif c == "validate":
        sys.exit(0 if validate() else 1)
    elif c == "resolve-options":
        resolve_options(a[0])
    elif c == "coverage":
        sys.exit(0 if coverage(a[0]) else 1)
    elif c == "check-design":
        sys.exit(0 if check_design(a[0]) else 1)
    elif c == "register-design":
        register_design(a[0])
    elif c == "new-niche":
        nid, name = a[0], " ".join(a[1:]) or a[0]
        tpl = {"id": nid, "name": name, "aliases": [], "status": "seed", "shopper_profile": "",
               "catalog_traits": {}, "must_have_sections": [], "nice_to_have_sections": [],
               "product_page_elements": [], "collection_page_elements": [], "metafields_metaobjects": [],
               "design_patterns": {}, "conversion_drivers": [], "competitor_references": [],
               "anti_patterns": [], "sources": [], "updated_at": today()}
        save(niche_file(nid), tpl)
        idx_path = P("banks", "research", "niches", "index.json")
        idx = load(idx_path, {"niches": []})
        idx["niches"].append({"id": nid, "name": name, "status": "seed", "must_have_count": 0, "sources": 0})
        save(idx_path, idx); print(f"created {niche_file(nid)}")
    else:
        print(f"unknown command {c}\n{__doc__}"); sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
