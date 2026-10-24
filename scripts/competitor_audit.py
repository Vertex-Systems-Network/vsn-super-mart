#!/usr/bin/env python3
"""Audit VSN's source-traceable, cross-platform theme research (stdlib only).

Usage:
    python3 scripts/competitor_audit.py validate
    python3 scripts/competitor_audit.py summary
    python3 scripts/competitor_audit.py next

Source levels intentionally distinguish a vendor's feature listing from an
independently opened live-demo page. Neither level proves interactive behavior.
Research never authorizes copying third-party code, imagery, or exact layouts.
"""
import collections
import json
import pathlib
import sys
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parent.parent
AUDIT = ROOT / "banks/research/competitors/demo-audit.json"
PATTERNS = ROOT / "banks/research/competitors/cross-platform-patterns.json"
OPTIONS = ROOT / "banks/options/options.json"
OBSERVATIONS = ROOT / "banks/design/competitor-observations.json"
ALLOWED = {"official_preset_page", "live_demo_page"}
PLATFORMS = {"shopify", "woocommerce", "bigcommerce", "magento"}


def read(path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def check_repo():
    errors = []
    for path in (AUDIT, PATTERNS, OPTIONS, OBSERVATIONS):
        if not path.is_file():
            return ["missing required audit file: " + str(path.relative_to(ROOT))]
    audit, patterns, options, observations = map(
        read, (AUDIT, PATTERNS, OPTIONS, OBSERVATIONS)
    )
    entries = audit.get("entries", [])
    known_options = {o["id"] for o in options.get("options", [])}
    ids = set()
    urls = set()
    for entry in entries:
        eid = entry.get("id")
        if not eid or eid in ids:
            errors.append("duplicate/missing entry id: " + str(eid))
        ids.add(eid)
        url = entry.get("url", "")
        parts = urlparse(url)
        if parts.scheme != "https" or not parts.netloc:
            errors.append(str(eid) + ": source URL must be HTTPS")
        if url in urls:
            errors.append(str(eid) + ": same URL recorded twice")
        urls.add(url)
        if entry.get("platform") not in PLATFORMS:
            errors.append(str(eid) + ": unexpected platform")
        if entry.get("evidence_level") not in ALLOWED:
            errors.append(str(eid) + ": bad evidence level")
        if not entry.get("opened_on") or not entry.get("design_signals"):
            errors.append(str(eid) + ": missing visit date or design signals")
        for option_id in entry.get("feature_option_ids", []):
            if option_id not in known_options:
                errors.append(str(eid) + ": unmapped option " + option_id)
    for pattern in patterns.get("patterns", []):
        if not pattern.get("design_implication"):
            errors.append("pattern missing design implication: " + pattern.get("id", "?"))
        for sid in pattern.get("source_entry_ids", []):
            if sid not in ids:
                errors.append("pattern " + pattern.get("id", "?") + ": unknown evidence " + sid)
        for oid in pattern.get("option_ids", []):
            if oid not in known_options:
                errors.append("pattern " + pattern.get("id", "?") + ": unknown option " + oid)
    observation_ids = set()
    for item in observations.get("observations", []):
        sid = item.get("id")
        if sid in observation_ids:
            errors.append("duplicate design observation: " + str(sid))
        observation_ids.add(sid)
        match = next((e for e in entries if e["id"] == sid), None)
        if not match:
            errors.append("design observation without audit entry: " + str(sid))
        elif item.get("evidence_level") != match["evidence_level"]:
            errors.append("evidence level mismatch in design observation: " + str(sid))
    if not entries:
        errors.append("empty audit")
    if len({e.get("platform") for e in entries}) < 3:
        errors.append("audit must cover at least three platforms")
    return errors


def summary():
    entries = read(AUDIT)["entries"]
    by_platform = collections.Counter(e["platform"] for e in entries)
    by_level = collections.Counter(e["evidence_level"] for e in entries)
    print("VSN competitor audit: %d individual source entries" % len(entries))
    for platform, count in sorted(by_platform.items()):
        print("  %-13s %d" % (platform, count))
    for level, count in sorted(by_level.items()):
        print("  %-22s %d" % (level, count))
    print("Patterns: %d" % len(read(PATTERNS)["patterns"]))
    print("Backlog: %d" % len(read(AUDIT).get("backlog", [])))


def main(argv):
    cmd = argv[0] if argv else "summary"
    if cmd == "validate":
        errors = check_repo()
        if errors:
            print("competitor audit: FAIL\n  " + "\n  ".join(errors))
            return 1
        print("competitor audit: OK")
        summary()
    elif cmd == "summary":
        summary()
    elif cmd == "next":
        for item in read(AUDIT).get("backlog", []):
            print("%s / %s: %s" % (
                item["platform"], item["theme"], item["reason"]
            ))
    else:
        print("Usage: competitor_audit.py [validate|summary|next]")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
