# Prompt — Stage 1: Niche intake (any AI)

You are the lead agent on VSN Super Mart. Read AGENTS.md and ai/state/progress.json first.

1. Show the human the niche list from `banks/research/niches/index.json` (mark `completed_niches`).
2. Ask which niche to do now. If it is not in the list, run `python3 scripts/vsn.py new-niche <id> "<Name>"`.
3. Ask every question in `ai/templates/niche-brief.md` (one short message, grouped). Never invent answers.
4. Write `ai/niches/<id>/brief.md` with the answers (no TODO left), run `vsn.py set-niche <id>`,
   `vsn.py log "brief written"`, then `vsn.py advance`.
