#!/usr/bin/env python3
"""Validate or regenerate the surviving Afterhours HTML design source.

check   : validate 24 screen IDs, 108 image slots and 22 historical briefs
rebuild : run original Python generator and validate its outputs
bundle  : create an HTML-only preview with image placeholders (not Figma)
"""
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "banks/design/specs/gen-z-store/source"
MANIFEST = ROOT / "ai/recovery/afterhours.json"
SPEC = ROOT / "banks/design/specs/gen-z-store/spec.json"
IMAGE_LOG = ROOT / "banks/design/image-log.json"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check():
    source = (SRC / "afterhours.html").read_text(encoding="utf-8")
    slots, hashes = read(SRC / "slots.json"), read(SRC / "hashes.json")
    manifest, spec, log = read(MANIFEST), read(SPEC), read(IMAGE_LOG)
    screen_ids = re.findall(r'<div class="screen [^"]*" id="([^"]+)"', source)
    errors = []
    if screen_ids != manifest["screen_ids"]:
        errors.append("screen IDs differ from recovery manifest")
    if len(screen_ids) != 24 or len(set(screen_ids)) != 24:
        errors.append("expected 24 unique screens")
    if len(slots) != 108 or any(color not in source for color in slots):
        errors.append("placeholder mapping must have 108 positions in HTML")
    if len(hashes) != 22:
        errors.append("expected 22 historical image hash references")
    active = spec.get("figma", {})
    restored = manifest.get("restored_figma", {})
    if active.get("file_key"):
        if active.get("file_key") == manifest.get("old_file_key"):
            errors.append("deleted Figma file must never be active")
        if active.get("file_key") != restored.get("file_key"):
            errors.append("active Figma file does not match recorded restoration")
        if set(active.get("frames", {})) != set(manifest["screen_ids"]):
            errors.append("restored Figma screen ID mapping incomplete")
        if len(set(active.get("frames", {}).values())) != 24:
            errors.append("restored Figma frame node IDs must be unique")
        if active.get("page_node") != restored.get("page_node"):
            errors.append("restored page ID mismatch")
    elif active.get("frames"):
        errors.append("Figma frame IDs present but no active file key")
    items = [x for x in log["images"] if x.get("niche") == "gen-z-store"]
    if len(items) != 22 or any(x.get("figma_node") or x.get("asset_status") != "lost_or_unavailable" for x in items):
        errors.append("historical AI images must be marked unavailable, not active")
    if errors:
        print("Afterhours recovery FAIL: " + "; ".join(errors))
        return 1
    print("Afterhours recovery OK: 24 source screens, 108 placeholders, 22 historic prompts; active Figma frames recorded; original Figma photos unavailable")
    return 0


def main(argv):
    action = argv[0] if argv else "check"
    if action == "rebuild":
        subprocess.run([sys.executable, str(SRC / "build.py")], check=True, cwd=SRC)
        return check()
    if action == "check":
        return check()
    if action == "bundle":
        if check() != 0:
            return 1
        out = Path(argv[1]) if len(argv) > 1 else ROOT / "dist/afterhours-recovery.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        source = (SRC / "afterhours.html").read_text(encoding="utf-8")
        notice = '<aside style="position:fixed;z-index:999;right:12px;top:12px;background:#16161d;color:#fff;border:2px solid #C6FF3D;padding:14px;max-width:310px;font:12px sans-serif">Source-only backup: 24 layout screens. Original Figma layers and images are not included; colored blocks are placeholders.</aside>'
        out.write_text(source.replace("<body>", "<body>" + notice, 1), encoding="utf-8")
        print("HTML source preview written:", out)
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
