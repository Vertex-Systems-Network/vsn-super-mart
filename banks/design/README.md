# Design Bank

Makes sure every VSN design is **informed by research, complete, and never a repeat**.

```
fingerprint-schema.json        the dimensions that make a design recognizable + allowed values + thresholds
competitor-fingerprints.json   approximate → verified fingerprints of competitor themes/presets
competitor-observations.json   source-linked qualitative demo observations without invented fingerprint dimensions
registry.json                  every accepted VSN design: fingerprint, palette, Figma node ids, spec path
image-log.json                 every Figma AI generated image: prompt, model, node id, where used
specs/<niche>/directions.json  Stage 4 — 3 candidate directions + chosen id
specs/<niche>/spec.json        Stage 5 — full design spec (template: ai/templates/design-spec.json)
```

## How uniqueness is checked
`vsn.py check-design <file>` compares a design's 12 fingerprint dimensions + accent palette hue with every
registry entry, every competitor fingerprint and the other candidates.
Similarity = equal dimensions / 13. **≥ 0.70 FAIL**, ≥ 0.55 WARN (must be justified), else PASS.
Cosmetic swaps (only colors/fonts) cannot pass, which matches the Theme Store uniqueness rule.

## How completeness is checked
`vsn.py coverage <spec>` — every `must` option for the niche and every Theme Store requirement must appear
in the spec's `option_map` / `requirement_map`.

## Cross-platform design evidence
Read `banks/research/competitors/demo-audit.json` and `banks/design/competitor-observations.json` before direction search. A vendor listing or text-only live page does not validate a full 12-dimension screenshot fingerprint. Mark fingerprints `verified` **only after** inspecting home, collection, product and mobile views of the actual demo; save evidence and the direct demo URL. Run `vsn.py check-design` against the established fingerprints to prevent cloning recognizable designs.
