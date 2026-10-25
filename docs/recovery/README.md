# Afterhours recovery

Original Figma UI was reported deleted; old file also returns access denied. The GitHub repository retains 24 source HTML screens and the Python generator, 108 image slots and 22 historical image prompts. These are NOT Figma layers or recovered photos.

Run `python3 scripts/afterhours_recovery.py check`, `python3 scripts/afterhours_recovery.py rebuild`, and `python3 scripts/afterhours_recovery.py bundle dist/afterhours-recovery.html`. The PR workflow uploads an HTML-only source-preview artifact. It shows placeholders where Figma images must be recreated. Review desktop/mobile visually before approving Stage 6; no automatic release gate bypass.

## Restored editable destination (2026-10-25)

New Figma file: https://www.figma.com/design/y5e3fEpx2eAFhLRFLisP0o/VSN-Super-Mart?node-id=0-1 . Contains 24 source-guided editable screens and 641 editable text layers; the scene-layer mapping is in spec.json. Original source photos are still absent. Do not confuse historical image hashes with exported photos. Visual QA and approval remain pending.

## Superseded on 2026-10-25

Per user instruction, **neither original Afterhours nor recreated Figma design is active**. This document is historical only. Current workflow is Stage 2 research and will create a brand-new design later after updated direction/options review. Do not use old Figma file or nodes as work targets.
