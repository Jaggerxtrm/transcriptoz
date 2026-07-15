# Changelog

All notable changes to this project are documented here.

## [Unreleased]

### Other changes

- **Remove hand-edited .specialists/default/ mirror files** ([b2148b7](https://github.com/Jaggerxtrm/transcriptoz/commit/b2148b7842c6a668044f59325bf9d7cc14a764c6)) — 2026-05-26 11:42

  The previous chore commit (v3.17.0-pre soak sweep) populated
  .specialists/default/ by hand. That directory is managed by the
  update-specialists skill — never by hand per CLAUDE.md. Reverting the
  mirror edits.

  Global `sp` is now `npm link`-ed to ~/dev/specialists so v3.17.0-pre
  specialists (including the new obligations-scanner) are visible from
  every repo via package-tier resolution. No mirror needed during soak.


### Project maintenance

- **Chore** ([d3c6ca8](https://github.com/Jaggerxtrm/transcriptoz/commit/d3c6ca89fe2d5ca78ece2b8cb4c43bd4eeb03168)) — 2026-04-13 14:16


- **Pull iron-review-hardening updates (v3.17.0-pre soak)** ([a505d3f](https://github.com/Jaggerxtrm/transcriptoz/commit/a505d3f6d399e28e42ff6c1a0f03089223fdb0b0)) — 2026-05-25 00:35

  Mirrored from ~/dev/specialists ahead of v3.17.0 minor release for the
  soak period:

  - .specialists/default/{reviewer,code-sanity,executor,debugger}.specialist.json
    → Iron-style behavior: SCRUTINY tiers, auto-escalation, ddiff re-review,
      obligations discipline (executor/debugger), seconder-gate (code-sanity)
  - .specialists/default/obligations-scanner.specialist.json (NEW)
    → READ_ONLY pre-review marker scan (TODO/FIXME/HACK/XXX/TEMP/WIP/NOTE)
  - .xtrm/skills/default/using-specialists-v3/SKILL.md (v3.4 → v3.5)
    → SCRUTINY taxonomy, Git State Precondition, Cherry-Pick Playbook
      canonical, sp merge / sp epic merge prohibited (rule #9 inverted)


- **Sync xtrm v0.9.0 assets** ([0bc00d5](https://github.com/Jaggerxtrm/transcriptoz/commit/0bc00d5e047946e28aa95f0894256ed6cddd9664)) — 2026-06-07 01:47


- **Apply bd auto-stage patch (xtrm-tools auto-applied)** ([182371b](https://github.com/Jaggerxtrm/transcriptoz/commit/182371bb0469b80d0e422a3c25f26b245339e011)) — 2026-07-13 06:01


- **Finalize v2 skills migration, adopt v0.10.4 hook paths** ([4304aba](https://github.com/Jaggerxtrm/transcriptoz/commit/4304abaada3dd8bf8ab956e79dc3384348e41186)) — 2026-07-13 10:38

  - Stage retirement of per-repo .xtrm/skills/default/** (skills now global
    at ~/.xtrm/skills/default/ under v2 layout).
  - Adopt v0.10.4 service-skills hook paths: $CLAUDE_PROJECT_DIR -> $HOME.
  - Untrack runtime state and gitignore going forward.


- **Preserve local skill divergences from v2 migration** ([b5ad1b5](https://github.com/Jaggerxtrm/transcriptoz/commit/b5ad1b520a235979da985e8c35bdff6153d66568)) — 2026-07-13 10:38

  The migrator wrote these files to .xtrm/skills/local-legacy/ during v2
  skills migration because they diverged from the global default source.
  Committing preserves the divergence record for future audit; discard by
  git rm -rf if the intent is to converge on global.


- **Add git-cliff config and changelog** ([74524d7](https://github.com/Jaggerxtrm/transcriptoz/commit/74524d7c2502e27b62f036048c5a54bc73683e54)) — 2026-07-14 00:56

  Generic type-based parsers; repo-specific scopes to be tuned (see P0 bead).
