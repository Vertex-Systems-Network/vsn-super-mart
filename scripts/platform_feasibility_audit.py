#!/usr/bin/env python3
"""Validate source-backed Shopify platform feasibility and active project instructions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def check():
    errors = []
    registry = read_json("banks/research/competitors/shopify-editor-feasibility-batch11-2026.json")
    opts = {x["id"] for x in read_json("banks/options/options.json")["options"]}
    limits = read_json("banks/research/competitors/shopify-platform-limits-2026.json")
    live = read_json("banks/research/competitors/shopify-live-demo-evidence-2026.json")
    state = read_json("ai/state/progress.json")
    decisions = registry.get("decisions", [])
    if len(decisions) < 15:
        errors.append("Batch 11 needs at least 15 traceable platform decisions")
    names = [x.get("id") for x in decisions]
    if len(set(names)) != len(names) or not all(names):
        errors.append("Duplicate/missing platform decision IDs")
    for entry in decisions:
        name = entry.get("id", "(missing)")
        if entry.get("priority") not in {"critical", "high", "medium", "low"}:
            errors.append(name + ": invalid priority")
        if not entry.get("finding") or not entry.get("vsn_design_action") or not entry.get("check"):
            errors.append(name + ": missing observation/implication/verification")
        if not entry.get("option_ids"):
            errors.append(name + ": missing VSN option mapping")
        for oid in entry.get("option_ids", []):
            if oid not in opts:
                errors.append(name + ": unknown option " + oid)
        if not entry.get("shopify_evidence") or any(not s.startswith("https://shopify.dev/") for s in entry.get("shopify_evidence", [])):
            errors.append(name + ": missing authoritative Shopify documentation URL")
        if entry.get("status") not in {"research_only", "decision_required"}:
            errors.append(name + ": incorrectly claimed implementation/test")
    if limits["hard_limits"]["theme_block_files"] != 300 or limits["hard_limits"]["theme_block_nesting_levels"] != 8:
        errors.append("Physical block/nesting limit mismatch")
    if registry.get("competitor_live_demo_new_documents") != 0 or registry.get("competitor_private_editor_tested") is not False:
        errors.append("Platform document research misrepresented as private editor or demo access")
    # Batch 11 is a fixed historical snapshot, not a permanent cap on new verified demos.
    # New selected homepages must be independently recorded in the live evidence bank
    # and reconciled with the cumulative plan; do not manufacture counts from listings.
    historical_home = registry.get("selected_preset_demo_homepages_after")
    if historical_home != registry.get("selected_preset_demo_homepages_before") or historical_home != 43:
        errors.append("Batch 11 historical home baseline was modified")
    selected_stores = [s for s in live.get("stores", []) if s.get("selected_127")]
    selected_home = [s for s in selected_stores if s.get("homepage", {}).get("verification") == "public_html_document_opened"]
    distinct_preset_ids = {s.get("catalog_preset_id") for s in selected_home}
    plan = read_json("banks/research/competitors/shopify-live-demo-plan-2026.json")
    actual = len(selected_home)
    if (actual < historical_home
        or actual != len(distinct_preset_ids)
        or live.get("selected_127_document_count") != actual
        or plan["counts"].get("live_home_demo_verified") != actual
        or any(not s["homepage"].get("url", "").startswith("https://") for s in selected_home)):
        errors.append("Cumulative selected homepage evidence differs from actual verified URLs and plan")
    if state["stage"] == 2 and state.get("figma", {}).get("status") != "no_active_design":
        errors.append("Stage 2 active design state inconsistent")
    if state["stage"] == 2:
        claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
        workflow = (ROOT / "ai/WORKFLOW.md").read_text(encoding="utf-8")
        if "no active Figma" not in claude:
            errors.append("Claude agent must not target old Figma design")
        if "Figma AI" in claude and "never Figma AI" not in claude:
            errors.append("Claude AI image policy is stale")
        if "**Figma AI**" in workflow:
            errors.append("Workflow still directs image generation to Figma AI")
        if "not current design targets" not in workflow:
            errors.append("Workflow still risks restoring superseded Stage 6 Figma")
    return errors

if __name__ == "__main__":
    problems = check()
    if problems:
        raise SystemExit("Platform feasibility audit FAILED:\n" + "\n".join("- " + p for p in problems))
    print("Platform feasibility audit OK: >=15 source-linked decisions, no false demo/editor claims or active Figma drift.")
