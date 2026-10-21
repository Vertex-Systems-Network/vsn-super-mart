# ADR 0002 — Deploy with the Shopify GitHub integration (via a `shopify-theme` branch)

- Date: 2026-10-22 · Status: accepted (to be tested when the dev store is connected)

## Context
- The team chose the Shopify GitHub integration as the way to get the theme into stores (no CLI, no ZIPs).
- The integration only connects branches whose **root** has the Shopify theme structure; a subdirectory
  cannot be selected (feature request only). Our theme lives in `theme/` next to banks, docs and scripts.
- Shopify commits theme editor / code editor / theme app changes back to the connected branch automatically.

## Decision
1. Branch **`shopify-theme`** holds only the theme at its root; this is the branch connected in Shopify
   (Online Store → Themes → Add theme → Connect from GitHub).
2. `.github/workflows/theme-to-shopify-branch.yml` publishes `theme/` from `main` with `git subtree split`,
   fast-forward only (it refuses to overwrite editor commits that are not synced back yet).
3. `.github/workflows/shopify-branch-to-theme.yml` merges Shopify bot commits from `shopify-theme` back
   into `main:theme/` with `git subtree pull` (commit tagged `[from-shopify]` so it does not loop).
4. Each preset demo store connects the same branch (or a release branch per version later).
5. Shopify CLI is optional (local live preview); if needed later use a Theme Access password.

## Setup steps for the team (one time)
1. Merge PR #1 into `main` (workflows run from `main`).
2. Run "Theme → shopify-theme branch" once (Actions → Run workflow) to create `shopify-theme`.
3. Install the Shopify GitHub app for the `Vertex-Systems-Network` org (owner/staff with Themes permission,
   org member with write access).
4. In the dev store: Online Store → Themes → Add theme → Connect from GitHub → repo `vsn-super-mart`,
   branch `shopify-theme`. Use "Preview" / "Share preview" for links.

## Risks / to test
- Simultaneous editor saves and pushes can conflict (Shopify docs); keep pushes small, sync back first.
- Code editor in admin overwrites without conflict alerts — prefer editing in the repo.
- Workflows not yet run against a real store.
