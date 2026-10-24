# Prompt — Stage 4: Design search & direction (Design Bank)

1. Design search: read `banks/design/registry.json` (previous VSN designs),
   `banks/design/competitor-fingerprints.json`, `banks/design/competitor-observations.json`,
   `banks/research/competitors/demo-audit.json`, the niche `design_patterns`, and the brief.
   Open live demos of the 3–5 closest competitors across home/collection/product/mobile; upgrade their fingerprints to `verified` **only after visual inspection**, with the exact demo URL and proof. Official preset product pages alone remain unverified for visual fingerprinting.
2. Propose 3 directions in `banks/design/specs/<niche>/directions.json`
   (template `ai/templates/directions.example.json`). Each must:
   - fit the niche research and brief,
   - use values from `banks/design/fingerprint-schema.json` (add a new value only for a genuinely new
     pattern, and describe it),
   - differ strongly from each other,
   - never be minimalist (team rule; `check-design` fails 3+ minimalism markers).
3. `vsn.py check-design banks/design/specs/<niche>/directions.json` → rework any FAIL (WARN = justify).
4. Present the passing directions to the human (moodboard text, key differences, risks).
   Put the chosen id in `"chosen"`, run `vsn.py approve 4 "<name>"`, then `vsn.py advance`.
