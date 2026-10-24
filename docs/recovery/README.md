# Afterhours recovery

Original Figma UI was reported deleted; old file also returns access denied. The GitHub repository retains 24 source HTML screens and the Python generator, 108 image slots and 22 historical image prompts. These are NOT Figma layers or recovered photos.

Run `python3 scripts/afterhours_recovery.py check`, `python3 scripts/afterhours_recovery.py rebuild`, and `python3 scripts/afterhours_recovery.py bundle dist/afterhours-recovery.html`. The PR workflow uploads an HTML-only source-preview artifact. It shows placeholders where Figma images must be recreated. Review desktop/mobile visually before approving Stage 6; no automatic release gate bypass.
