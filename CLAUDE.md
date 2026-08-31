# CLAUDE.md

Operational guidance for Claude Code and other editing agents in this repository.

## Repository purpose

CellStructureMech is a LinkML knowledge base of microbial cell structures —
organelles, envelope layers, appendages, microcompartments, inclusions,
cytoskeletal systems and multi-protein complexes. One YAML record lives under
`data/structures/<category>/<slug>.yaml` per structure.

Read before changing domain content:

- [README.md](README.md) — model and generated corpus statistics.
- [docs/CURATION.md](docs/CURATION.md) — what is a record, identifiers, evidence rules.
- [docs/SCHEMA.md](docs/SCHEMA.md) — field guide.
- [curation/source_queue.tsv](curation/source_queue.tsv) — the ranked data-source queue
  (legend in [docs/SOURCE_QUEUE.md](docs/SOURCE_QUEUE.md)); checked by `just source-queue`
  inside `just qc`; triaged by the `source-queue` skill. `ADOPTED` is earned by a PR that
  adds the script, not by editing the row.
- Issue triage: the `review-open-issues` skill
  (`.claude/skills/review-open-issues/SKILL.md`) — read-only ranking of the
  whole queue; closing and merging stay the owner's calls.

Sibling repositories use the same conventions: TraitMech, ProteinTraitsMech,
HabitatMech, CultureMech, MediaIngredientMech, CommunityMech. The upstream
pattern is monarch-initiative/dismech.

## Authoritative commands

```bash
just qc                # every local and CI quality gate
just report            # corpus statistics
just test              # unit and corpus-integrity tests
just validate-all      # closed-schema validation of every record
just render            # regenerate the committed site under pages/
just docs-stats        # refresh the generated README statistics block
just new-record ...    # scaffold a record (dry-run by default; --apply to write)
just source-queue      # the ranked data-source queue and what is unverified in it
just new-history ...   # scaffold a repository-level history record
just validate-products # id<->label correspondence gate via OAK (network on first run)
just check-curies-strict # resolve every identifier at its issuing authority (network)
just vendored-check    # claw-governed files match canon at scripts/.vendored_canon_ref
```

`just qc` is authoritative: lint, README statistics, tests, closed-schema
validation, generated-site drift check, corpus report. CI runs the same script.

## Fact-based answers only

Verify counts, statuses and identifiers with a live command (`just report`,
`grep`, `Read`) before stating them. Do not quote numbers from prose.

## Granularity and identity — the rules that matter most

- **A record is a structure, not a protein and not a phenotype.** Proteins are
  `components`; phenotypes are TraitMech records linked via `associated_traits`.
  The finest-grained record is a multi-protein complex.
- **GO cellular component first.** Use the GO CURIE when it denotes exactly
  this structure; otherwise mint `cellstructuremech:` and put the broader term
  in `parent_structures`. Never adopt a broader term as identity.
- **`parent_structures` is is-a; `part_of` is parthood.** Both must resolve to
  another record or a GO term.
- **Never guess a CURIE.** An unverified InterPro / UniProt / taxon accession
  is worse than none — leave `grounding` unset and open a `CURATION_TODO`
  discussion.
- **`snippet` is verbatim only.** Paraphrase in `notes` when you have not seen
  the source text.

## Safe mutation contract

- **Write records only through `write_validated_structure`** (closed-schema
  validation before write). Every mutation appends a `CurationEvent` via
  `record_curation_event`, with `llm_assisted: true` when a model produced it.
- **Re-emitting an unchanged record must be byte-identical.**
  `tests/test_write_validated.py` enforces the emission contract; do not loosen
  it to accommodate a hand-formatted file — reformat the file instead.
- **An LLM-drafted record is `PROPOSED`, never `REVIEWED`.** Promotion is a
  human decision.
- **Edit templates, not `pages/`.** Change `src/cellstructuremech/templates/`,
  run `just render`, commit the result. `pages/` is checked byte-for-byte.
- **Do not edit claw-governed vendored files here** — `mech_shared.yaml`,
  `history.yaml`, `scripts/check_vendored_sync.*`,
  `scripts/validate_id_label_correspondence.py`, `scripts/chem_formula.py`, the
  vendored `tests/test_*` and `prompts/backlog-loop-goal.md`. They are synced from
  culturebotai-claw at the commit in `scripts/.vendored_canon_ref` and checked
  byte-for-byte in CI (`just vendored-check`). Change them in claw and re-sync.
- **Every curation change also gets a repository-level history record**:
  `just new-history --kind record --slug <slug> --target-root data/structures/<category> ...`
  (see history/README.md). One record per hand-curated target or per coherent
  bulk change; records are append-only. `just validate-history` runs in qc.
- **`just validate-products`** is the id↔label gate: every (grounding, label)
  pair must match the ontology via OAK. It found two real modelling errors on
  adoption. Curator-accepted label residuals go in `conf/id_label_targets.yaml`
  with a reason; do not relabel a record just to pass.
- **Record location is derived** from `structure_category` and `label`
  (`scripts/corpus.py`). Move or rename by changing the record and the
  filename together.
- Keep changes scoped; preserve unrelated work in a dirty tree.
- **`research/` is tracked provenance**, evidence for a curator to read —
  never automatic record input. Canary any paid research run before a batch.

## Git workflow

Branch before the first edit. Open a PR for every change, including docs-only
changes. Review the diff as a separate adversarial pass and file findings as
issues. Do not merge without explicit approval. Delete branches after merge.
