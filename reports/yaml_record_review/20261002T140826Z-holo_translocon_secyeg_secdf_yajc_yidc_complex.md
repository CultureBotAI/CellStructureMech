# Review: Holo-translocon SecYEG-SecDF-YajC-YidC complex

- **PR:** #1915
- **Record:** `data/structures/secretion_system/holo_translocon_secyeg_secdf_yajc_yidc_complex.yaml`
- **Identifier:** `cellstructuremech:holo_translocon_secyeg_secdf_yajc_yidc_complex`
- **Review timestamp:** 2026-10-02T14:08:26Z
- **Reviewer:** codex

## Scope

Adversarial review of the newly added proposed `Holo-translocon
SecYEG-SecDF-YajC-YidC complex` record, its `ComplexPortal:CPX-1095`
source composition, generated site and embedding artifacts, and the
append-only history record.

## Authority Checks

- Hidden/ignored-inclusive duplicate checks over `data`, `history`, `pages`,
  `reports`, `scripts`, `docs`, `src`, `curation`, `research`, and `.github`
  found no pre-existing `CPX-1095` or exact holo-translocon record; the only
  pre-existing semantic hit was the SecYEG record's open TODO asking whether
  SecDF-YajC and YidC should become a separate holo-translocon subrecord.
- QuickGO searches for `holo-translocon`, `SecYEG-SecDF-YajC-YidC`, and
  `SecDF-YajC-YidC` found no exact cellular-component term, so a local
  `cellstructuremech:` identifier is appropriate.
- QuickGO resolves `GO:0031522` as the broader cell-envelope Sec protein
  transport complex parent, `GO:0043952` as protein transport by the Sec
  complex, and `GO:0032977` as membrane insertase activity.
- ComplexPortal `CPX-1095` resolves to the `Holo-translocon
  SecYEG-SecDF-YajC-YidC complex` for *Escherichia coli* K-12, asserts a
  `Heteroheptamer`, and lists one copy each of YajC, SecF, SecD, YidC, SecG,
  SecE, and SecY.
- The Complex Portal import was run through the exact accession endpoint and
  imported the seven E. coli K-12 UniProt participants into
  `complex_compositions`; those accession-level IDs were deliberately not used
  as taxon-agnostic `components` groundings.
- RCSB PDB `5MG3` is an EM-fitted bacterial holo-translocon model containing
  SecYEG, SecDF, and YidC but no YajC; the record cites it only as structural
  evidence for the modeled SecYEG-SecDF-YidC assembly, not as evidence for the
  seven-protein ComplexPortal stoichiometry.
- UniProt identity was verified for YidC, SecE, and SecY, but exact
  source-neutral InterPro/Pfam/NCBIfam/GO family terms were not verified for
  all seven proteins. The record correctly leaves all seven component rows
  `REVIEWED_LABEL_ONLY` and opens a `CURATION_TODO`.
- PubMed `27435098` / DOI `10.1042/BCJ20160545` name the bacterial
  `SecYEG-SecDF-YajC-YidC` holo-translocon; PubMed `27924919` /
  DOI `10.1038/srep38399` are the paired literature identifiers for the
  `PDB:5MG3` central-cavity structure.

## Findings

- **#1916 - Missing SecYEG-core boundary rationale.** The opened PR modeled the
  larger holo-translocon with `has_part:
  cellstructuremech:secyeg_translocon_complex`, but its only resolved boundary
  discussion excluded SecA. That left the older SecYEG-vs-holo-translocon
  question implicit in the new record. Fixed in `f1632549` by adding the
  `secyeg_core_holotranslocon_boundary` resolved `INTERPRETATION` discussion,
  attaching it to the SecYEG core `has_part` relation and the SecD, SecF,
  YajC, and YidC component rows.

## Validation Reviewed

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/secretion_system/holo_translocon_secyeg_secdf_yajc_yidc_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/secretion_system/holo_translocon_secyeg_secdf_yajc_yidc_complex.yaml`
- `just validate-strict --quiet`
- `just validate-history history/records/holo_translocon_secyeg_secdf_yajc_yidc_complex/2026-10-02T134250Z-codex-2c73b0.yaml`
- `just validate-history`
- `just text-embeddings-refresh`
- `just text-map-check`
- `just render`
- `just render-check`
- `just docs-stats`
- `just docs-check`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `just qc`
- `git diff --check`
