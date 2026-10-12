# Stentor myoneme whole-record review: reconcile Sfi1 source versions

- Review: 20261012T035945Z-stentor-myoneme-sfi1-source-version
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T03:48:45Z
- Finished UTC: 2026-10-12T03:59:45Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review found one minor source-version reconciliation gap. The historically explicit dissertation account is not false provenance, but the newly accessible final-paper manuscript provides different depth-resolved Sfi1 localization that the maintained evidence does not yet reconcile. Other claims remain supported with the stated reading limits.

## Scope And Provenance

One entire maintained Stentor myoneme record with claim-level sources and both histories.

Selection: Exact identifier and path resolved individually; neighboring Km/perialgal records are context, not targets of this bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e69ce7f88fb89299e401801f8b21f2d91aef6521.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:stentor_myoneme_system | data/structures/cytoskeleton/stentor_myoneme_system.yaml | maintained | Stentor myoneme system |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| stentor_myoneme_system-schema | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Deterministic check does not establish scientific correctness. |
| stentor_myoneme_system-strict | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Deterministic check does not establish scientific correctness. |
| stentor_myoneme_system-snippets | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Deterministic check does not establish scientific correctness. |
| history | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Deterministic check does not establish scientific correctness. |
| labels | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Deterministic check does not establish scientific correctness. |
| curies | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Deterministic check does not establish scientific correctness. |
| traits | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Deterministic check does not establish scientific correctness. |
| reviews | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Deterministic check does not establish scientific correctness. |
| contract | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Deterministic check does not establish scientific correctness. |
| baseline-ci | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Exact unchanged-base CI inspection, not a fresh local full-QC execution. |
| baseline-ci-full | passed | True | cellstructuremech:stentor_myoneme_system | Exit0; actual command receipt retained. Exact unchanged-base CI inspection, not a fresh local full-QC execution. |

## Scientific And Domain Assessments

### Myoneme identity, hierarchy and neighboring structures

identity: supported. Targets: cellstructuremech:stentor_myoneme_system.

Minted CYTOSKELETON/OTHER denotes longitudinal myoneme architecture, not every centrin-positive compartment or a sarcomeric M band. Broad parent and parthood, species-qualified label and broad myoneme synonym remain defensible.

### Centrin/Sfi1 constituents and source-version localization

evidence: concern. Targets: cellstructuremech:stentor_myoneme_system.

Centrin membership and Sfi1-related architecture remain supported, with UNKNOWN assembly essentiality, no copy number and conservative label-only grounding. The final manuscript adds depth-resolved anterior overlap and posterior outer-layer separation not reconciled with the dissertation-only localization conclusion.

### Experimental species and native composition limits

scope: supported. Targets: cellstructuremech:stentor_myoneme_system.

Huang and Yan experimental S.coeruleus agree with ENA species5963. No genus-wide prevalence, full paralogue inventory or defined native stoichiometry is claimed.

### Perturbation versus force-generation mechanism

graph: supported. Targets: cellstructuremech:stentor_myoneme_system.

Final Results support parallel Sfi1-1/2 knockdown cable-pattern and contraction outcomes. RNAi2/3 cross-depletion prevents isoform-exclusive attribution. Existing NONMECHANISTIC graph has no cable-loss mediation edge, universal isoform requirement or invented motor cycle; kinetic values need not be added.

### TEM figure and licensing

provenance: supported. Targets: cellstructuremech:stentor_myoneme_system.

Inspected Figure16 matches caption, scale, specimen and PDF page; source identity and versioned checksums verified. Link-only CC BY-NC-SA4.0 treatment preserved; no hosted image or inferred measurement.

### Durable unknowns and version reconciliation

completeness: concern. Targets: cellstructuremech:stentor_myoneme_system.

Family grounding, complete native composition and force generation remain genuine unknowns. The specific final-methods access gap can now be closed without pretending that mechanism is resolved; preserve the earlier dissertation account as historical evidence and explain the layer distinction.

### Scientific status, history and prior findings

ownership: supported. Targets: cellstructuremech:stentor_myoneme_system.

PROPOSED and both append-only histories are intact. Existing2006/2007 fixes remain visible; legacy review is not silently replaced. Scientific edits belong only to this maintained YAML with guarded writer, new EDIT provenance and generated page refresh.

## Findings

### F1: Reconcile Sfi1 localization with the final-paper cortical-depth results

minor / open / confirmed; issue key: stentor-myoneme-sfi1-source-version.

The component evidence correctly attributes absence of anterior centrin-mesh overlap to the dissertation, but the maintained record still treats detailed final evidence as inaccessible. PMC13637444.1 is now available and describes deeper anterior Sfi1/centrin mesh overlap while distinguishing outer lateral bands. Retaining only the older conclusion leaves a consequential unresolved version difference in constituent localization. Preserve the earlier source version, add the final layer-specific result, and update current source-access wording without widening the record to all centrin assemblies.

## Recommended Actions And Acceptance Checks

### A1

Curate the final-paper layer-specific localization and controls while retaining dissertation provenance and biological uncertainties.

- Explicitly distinguish outer lateral bands from deeper anterior mesh colocalization and do not universalize absence.
- Preserve the dissertation as an older distinct version; identify PMC author manuscript, DOI and reading scope.
- Keep UNKNOWN essentialities, label-only grounding, PROPOSED status and nonmechanistic/nonmediation graph; disclose RNAi2/3 cross-depletion when using final isoform results.
- Guarded write, append-only EDIT history, strict/history/full QC, generated output and review-contract checks pass.
- Save a supported successor disposition with this exact review/finding identity after inspecting the fix.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/cytoskeleton/stentor_myoneme_system.yaml; Entire YAML, both histories and current generated HTML | supports | Whole record read. Sfi1 evidence retains the dissertation conclusion excluding anterior centrin-mesh localization; final-paper evidence is described as abstract-only and final methods as inaccessible. The positive posterior localization, PROPOSED status and nonmechanistic graph are otherwise bounded. |
| yan-final | DOI:10.1016/j.cub.2026.06.062; PMC13637444.1: Results regional centrin patterning, multiple Sfi1 genes, cortical RNAi patterning and contractile machinery; Discussion; STAR Methods model and method details | supports | Final-paper author manuscript distinguishes cortical depth: outer lateral Sfi1 bands are distinct from the anterior centrin mesh, but deeper anterior layers share Sfi1/centrin mesh localization. It also reports Sfi1-2/3 RNAi cross-depletion, and Sfi1-1/2 perturbation phenotypes. Antibody and knockdown limitations prevent an isoform-exclusive mechanism claim. |
| yan-metadata | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC13637444.1.json; Version1 metadata and checksum verification | supports | PMID42476139, DOI10.1016/j.cub.2026.06.062, NIHMS2199024; author manuscript available2026-10-05, nonretracted; XML/TXT MD5s verified. TDM license is not permission to host figure assets. |
| yan-thesis | https://escholarship.org/content/qt48v7x2m3/qt48v7x2m3_noSplash_81e16ae35ca9c5219383afd7085febfb.pdf; Chapter2 printed pages24-33, especially31-32; browser-readable primary PDF | supports | The dissertation explicitly separates the three tested Sfi1 proteins from the anterior centrin mesh. This supports the record as an account of that version, but the later depth-resolved manuscript differs. Locus mappings, nonspecific immunoblot bands and peptide/RNAi controls were also checked. |
| huang | DOI:10.1083/jcb.57.3.704; PMC2108994.1 complete main PDF text through Discussion; Figures8,16,17 pixels | supports | Ultrastructure distinguishes deeper myonemes from Km ribbons and nearby membranes. Fixed-state morphology does not directly resolve a molecular transition. Figure16 is a contracted longitudinal myoneme with transverse inset and0.1um bar; verified CC BY-NC-SA4.0 requires link-only treatment under local policy. |
| newman | DOI:10.1126/science.177.4047.447; Complete primary PubMed abstract PMID5043148; identity cross-checked in Crossref and PMC front matter | supports | M bands straighten before shortening; mechanically evoked contraction propagates while electrical stimulation initiates contraction throughout the cell. This supports the terminology and bounded cinematic function; no calcium signal identity is established. Full methods were not readable in this pass. |
| maloney | DOI:10.1111/j.1550-7408.2005.00048x; Complete primary PubMed abstract PMID16014010 | supports | Three antibody preparations label a centrin-related calcium-binding protein in myonemes separately from alpha-tubulin-positive Km fibers, as well as membranelle bases. This is localization and immunoblot evidence, not an inventory or necessity experiment. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0030863,GO:0097427,GO:0035253,GO:0031430; Live labels, definitions and obsolete flags; seven bounded name queries | supports | Intracellular anatomical structure is an is-a parent; cortical cytoskeleton is an enclosing framework. Sarcomeric M band is not an exact match. Stentor and myoneme name queries have no hits; these probes are not exhaustive ontology absence proof. |
| centrin-family | InterPro:IPR050145; Live entry name and description | supports | Centrin/CML-like includes noncentrin calcium-binding proteins; label-only mapping remains appropriately conservative. Machine-assisted authority description is not direct Stentor localization evidence. |
| sfi1-family | InterPro:IPR052270; Live entry name and description | supports | SFI1-like includes SFI1 and CCDC191-related members; it is broader than a defined myonemal scaffold class. Exact grounding is not established by this reviewed machine-assisted family description. |
| taxon | NCBITaxon:5963; ENA live taxonomy record | supports | Species-level Stentor coeruleus identity confirmed; no genus-wide structure prevalence inferred. |
| historical-review | reports/yaml_record_review/20261004T003824Z-stentor_myoneme_system.md; Entire legacy report plus direct GitHub issue2006/2007 current state and current HTML | supports | Both prior issues are CLOSED/COMPLETED; direct Newman provenance and visible nonmechanistic/nonmediation wording remain present. No canonical predecessor exists for this target in the ignored-inclusive187-bundle exact-ID/path scan; this is a new version-reconciliation finding, not a reopening of either historical issue. |
| baseline-qc | https://github.com/CultureBotAI/CellStructureMech/actions/runs/38198723985; Exact-base merge-group run metadata and full QC log | supports | Successful exact commit e69ce7f88fb89299e401801f8b21f2d91aef6521:987 tests passed,3 skipped;909 strict records,1722 valid histories; separate contract step4 passed. No scientific file changed before this observation. |

## Limits And Additional Notes

- Same-agent review only, not human sign-off or raw-data reanalysis. iModulonDB live28-dataset inventory is inapplicable to Stentor; absence there is not biological evidence.
- Yan final-paper author manuscript relevant Results, Discussion and STAR Methods inspected in checksum-verified XML. Oral-regeneration Results, supplementary files, movie pixels and final publisher typeset PDF were not fully inspected. No new numeric measurement is proposed.
- Dissertation Chapter2 printed24-33 inspected via readable primary web PDF; direct download returned202 with zero bytes. No claim that this local empty file is a readable PDF. Dissertation Methods not reread this pass; final-paper Methods were read independently.
- Newman1972 and Maloney2005 complete primary abstracts inspected; full Methods not readable this pass. Newman author-host PDF was located but local DNS failed and web screenshots yielded no inspectable pixels; PMC page challenge was not bypassed. Earlier legacy claims of full reading are historical, not this reviewer reading scope.
- All required deterministic checks passed. Current label checker603 no-adapter and CURIE251 skips retained; target authorities separately verified. Snippet check has0 snippets among31 citations and does not prove literature support.
- Baseline full QC is exact unchanged-commit CI evidence, not a fresh local run. Current archive187 and four local contract tests passed. No repository scientific edits preceded this saved observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T035945Z-stentor-myoneme-sfi1-source-version
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Stentor myoneme whole-record review: reconcile Sfi1 source versions'
started_at: '2026-10-12T03:48:45Z'
finished_at: '2026-10-12T03:59:45Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same coding agent; no independent reviewer or human scientific
    sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole-record review found one minor source-version reconciliation gap. The
  historically explicit dissertation account is not false provenance, but the newly
  accessible final-paper manuscript provides different depth-resolved Sfi1 localization
  that the maintained evidence does not yet reconcile. Other claims remain supported
  with the stated reading limits.
source:
  git_revision: e69ce7f88fb89299e401801f8b21f2d91aef6521
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/literature-evidence/SKILL.md
    sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/cytoskeleton/stentor_km_fiber.yaml
    sha256: 66b91b45477653bcafdf1f875b9820681ea1bdeddf36f9d37f74fabe9408cae6
    role: context
  - path: data/structures/cytoskeleton/stentor_myoneme_system.yaml
    sha256: 5d79ebc4d1396dc1a3e8d7e840a2aba6ed8dc37114846e4405df82c965b10b28
    role: target
  - path: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
    sha256: 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf
    role: context
  - path: docs/CURATION.md
    sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
    role: context
  - path: docs/SCHEMA.md
    sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
    role: context
  - path: docs/record-review-profile.md
    sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/stentor_myoneme_system/2026-10-04T002336Z-codex-87a070.yaml
    sha256: 927a11172dc4285768ad84a9f93e8abc4580474c506f9e57238529a5b6ec766e
    role: context
  - path: history/records/stentor_myoneme_system/2026-10-04T003927Z-codex-0d9afb.yaml
    sha256: 9ae95f94857096c532e4a62f6aea961a5922e6ea92c69084b80005b2fa766bac
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20261004T003824Z-stentor_myoneme_system.md
    sha256: 73ac3c10c146f059ac0e8cb687097972e2362767276ea8478315567e9780f707
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: cellstructuremech:stentor_myoneme_system
  path: data/structures/cytoskeleton/stentor_myoneme_system.yaml
  label: Stentor myoneme system
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stentor_myoneme_system.yaml
    role: maintained scientific record
scope:
  description: One entire maintained Stentor myoneme record with claim-level sources
    and both histories.
  selection: Exact identifier and path resolved individually; neighboring Km/perialgal
    records are context, not targets of this bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:stentor_myoneme_system
checks:
- check_id: stentor_myoneme_system-schema
  name: stentor_myoneme_system-schema
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Deterministic check does not establish
    scientific correctness.
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/stentor_myoneme_system.yaml
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
- check_id: stentor_myoneme_system-strict
  name: stentor_myoneme_system-strict
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Deterministic check does not establish
    scientific correctness.
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/stentor_myoneme_system.yaml
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
- check_id: stentor_myoneme_system-snippets
  name: stentor_myoneme_system-snippets
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Deterministic check does not establish
    scientific correctness.
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/stentor_myoneme_system.yaml
    --report /private/tmp/csm-review-20261012T034900Z/stentor_myoneme_system-snippets.md
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
- check_id: history
  name: history
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Deterministic check does not establish
    scientific correctness.
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
- check_id: labels
  name: labels
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Deterministic check does not establish
    scientific correctness.
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
- check_id: curies
  name: curies
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Deterministic check does not establish
    scientific correctness.
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
- check_id: traits
  name: traits
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Deterministic check does not establish
    scientific correctness.
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
- check_id: reviews
  name: reviews
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Deterministic check does not establish
    scientific correctness.
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
- check_id: contract
  name: contract
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Deterministic check does not establish
    scientific correctness.
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
- check_id: baseline-ci
  name: baseline-ci
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Exact unchanged-base CI inspection,
    not a fresh local full-QC execution.
  command: gh run view 38198723985 --repo CultureBotAI/CellStructureMech --json headSha,status,conclusion,event,name,url,jobs
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
- check_id: baseline-ci-full
  name: baseline-ci-full
  status: passed
  required: true
  summary: Exit0; actual command receipt retained. Exact unchanged-base CI inspection,
    not a fresh local full-QC execution.
  command: gh run view 38198723985 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  target_ids:
  - cellstructuremech:stentor_myoneme_system
evidence:
- evidence_id: native
  kind: record_content
  reference: data/structures/cytoskeleton/stentor_myoneme_system.yaml
  locator: Entire YAML, both histories and current generated HTML
  accessed_at: '2026-10-12T03:59:45Z'
  support: supports
  summary: Whole record read. Sfi1 evidence retains the dissertation conclusion excluding
    anterior centrin-mesh localization; final-paper evidence is described as abstract-only
    and final methods as inaccessible. The positive posterior localization, PROPOSED
    status and nonmechanistic graph are otherwise bounded.
- evidence_id: yan-final
  kind: primary_source
  reference: DOI:10.1016/j.cub.2026.06.062
  locator: 'PMC13637444.1: Results regional centrin patterning, multiple Sfi1 genes,
    cortical RNAi patterning and contractile machinery; Discussion; STAR Methods model
    and method details'
  accessed_at: '2026-10-12T03:50:07Z'
  support: supports
  summary: 'Final-paper author manuscript distinguishes cortical depth: outer lateral
    Sfi1 bands are distinct from the anterior centrin mesh, but deeper anterior layers
    share Sfi1/centrin mesh localization. It also reports Sfi1-2/3 RNAi cross-depletion,
    and Sfi1-1/2 perturbation phenotypes. Antibody and knockdown limitations prevent
    an isoform-exclusive mechanism claim.'
  snapshot_sha256: 4ca4d1b66b127c68c9e30d240ab5c62d7473b98e5bdb0f0c3407313182c9b643
- evidence_id: yan-metadata
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC13637444.1.json
  locator: Version1 metadata and checksum verification
  accessed_at: '2026-10-12T03:49:26Z'
  support: supports
  summary: PMID42476139, DOI10.1016/j.cub.2026.06.062, NIHMS2199024; author manuscript
    available2026-10-05, nonretracted; XML/TXT MD5s verified. TDM license is not permission
    to host figure assets.
  snapshot_sha256: 455a333dbec1ff1fea9bdecceb6a64712da678737de90ef64808ec4c52c71783
- evidence_id: yan-thesis
  kind: primary_source
  reference: https://escholarship.org/content/qt48v7x2m3/qt48v7x2m3_noSplash_81e16ae35ca9c5219383afd7085febfb.pdf
  locator: Chapter2 printed pages24-33, especially31-32; browser-readable primary
    PDF
  accessed_at: '2026-10-12T03:59:45Z'
  support: supports
  summary: The dissertation explicitly separates the three tested Sfi1 proteins from
    the anterior centrin mesh. This supports the record as an account of that version,
    but the later depth-resolved manuscript differs. Locus mappings, nonspecific immunoblot
    bands and peptide/RNAi controls were also checked.
- evidence_id: huang
  kind: primary_source
  reference: DOI:10.1083/jcb.57.3.704
  locator: PMC2108994.1 complete main PDF text through Discussion; Figures8,16,17
    pixels
  accessed_at: '2026-10-12T03:49:30Z'
  support: supports
  summary: Ultrastructure distinguishes deeper myonemes from Km ribbons and nearby
    membranes. Fixed-state morphology does not directly resolve a molecular transition.
    Figure16 is a contracted longitudinal myoneme with transverse inset and0.1um bar;
    verified CC BY-NC-SA4.0 requires link-only treatment under local policy.
  snapshot_sha256: 61e5f2ef7e22ef22f7e1d2b2e27ecf4f58195865867356261daadaf24fe17514
- evidence_id: newman
  kind: primary_source
  reference: DOI:10.1126/science.177.4047.447
  locator: Complete primary PubMed abstract PMID5043148; identity cross-checked in
    Crossref and PMC front matter
  accessed_at: '2026-10-12T03:48:32Z'
  support: supports
  summary: M bands straighten before shortening; mechanically evoked contraction propagates
    while electrical stimulation initiates contraction throughout the cell. This supports
    the terminology and bounded cinematic function; no calcium signal identity is
    established. Full methods were not readable in this pass.
  snapshot_sha256: f476b558dc53b555f123c58c1457abf3ad301835263c45ddd16d4a2228ea590c
- evidence_id: maloney
  kind: primary_source
  reference: DOI:10.1111/j.1550-7408.2005.00048x
  locator: Complete primary PubMed abstract PMID16014010
  accessed_at: '2026-10-12T03:48:32Z'
  support: supports
  summary: Three antibody preparations label a centrin-related calcium-binding protein
    in myonemes separately from alpha-tubulin-positive Km fibers, as well as membranelle
    bases. This is localization and immunoblot evidence, not an inventory or necessity
    experiment.
  snapshot_sha256: f476b558dc53b555f123c58c1457abf3ad301835263c45ddd16d4a2228ea590c
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0030863,GO:0097427,GO:0035253,GO:0031430
  locator: Live labels, definitions and obsolete flags; seven bounded name queries
  accessed_at: '2026-10-12T03:48:36Z'
  support: supports
  summary: Intracellular anatomical structure is an is-a parent; cortical cytoskeleton
    is an enclosing framework. Sarcomeric M band is not an exact match. Stentor and
    myoneme name queries have no hits; these probes are not exhaustive ontology absence
    proof.
  snapshot_sha256: b77e3630d1abf16bc4f8eb7ce7dc41b9861bcd822070b03620913dca62ffd5be
- evidence_id: centrin-family
  kind: authority
  reference: InterPro:IPR050145
  locator: Live entry name and description
  accessed_at: '2026-10-12T03:48:43Z'
  support: supports
  summary: Centrin/CML-like includes noncentrin calcium-binding proteins; label-only
    mapping remains appropriately conservative. Machine-assisted authority description
    is not direct Stentor localization evidence.
  snapshot_sha256: 386371fb67a7de41d9f9a6ded2bbb77530d9a27411b46349d2ac050d45832910
- evidence_id: sfi1-family
  kind: authority
  reference: InterPro:IPR052270
  locator: Live entry name and description
  accessed_at: '2026-10-12T03:48:43Z'
  support: supports
  summary: SFI1-like includes SFI1 and CCDC191-related members; it is broader than
    a defined myonemal scaffold class. Exact grounding is not established by this
    reviewed machine-assisted family description.
  snapshot_sha256: 1b31c05d82a1ef155a91ee9b419e70a5e28f9414358e858d34f79e55ea5b54bb
- evidence_id: taxon
  kind: authority
  reference: NCBITaxon:5963
  locator: ENA live taxonomy record
  accessed_at: '2026-10-12T03:48:44Z'
  support: supports
  summary: Species-level Stentor coeruleus identity confirmed; no genus-wide structure
    prevalence inferred.
  snapshot_sha256: e66b4bd1362354340ef4683fab0f80bead40dfcfe41f4814c3b7283f96193813
- evidence_id: historical-review
  kind: prior_review
  reference: reports/yaml_record_review/20261004T003824Z-stentor_myoneme_system.md
  locator: Entire legacy report plus direct GitHub issue2006/2007 current state and
    current HTML
  accessed_at: '2026-10-12T03:59:45Z'
  support: supports
  summary: Both prior issues are CLOSED/COMPLETED; direct Newman provenance and visible
    nonmechanistic/nonmediation wording remain present. No canonical predecessor exists
    for this target in the ignored-inclusive187-bundle exact-ID/path scan; this is
    a new version-reconciliation finding, not a reopening of either historical issue.
- evidence_id: baseline-qc
  kind: validation
  reference: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38198723985
  locator: Exact-base merge-group run metadata and full QC log
  accessed_at: '2026-10-12T03:59:45Z'
  support: supports
  summary: Successful exact commit e69ce7f88fb89299e401801f8b21f2d91aef6521:987 tests
    passed,3 skipped;909 strict records,1722 valid histories; separate contract step4
    passed. No scientific file changed before this observation.
assessments:
- assessment_id: identity
  area: identity
  topic: Myoneme identity, hierarchy and neighboring structures
  outcome: supported
  summary: Minted CYTOSKELETON/OTHER denotes longitudinal myoneme architecture, not
    every centrin-positive compartment or a sarcomeric M band. Broad parent and parthood,
    species-qualified label and broad myoneme synonym remain defensible.
  target_ids:
  - cellstructuremech:stentor_myoneme_system
  evidence_ids:
  - native
  - huang
  - newman
  - go
- assessment_id: components
  area: evidence
  topic: Centrin/Sfi1 constituents and source-version localization
  outcome: concern
  summary: Centrin membership and Sfi1-related architecture remain supported, with
    UNKNOWN assembly essentiality, no copy number and conservative label-only grounding.
    The final manuscript adds depth-resolved anterior overlap and posterior outer-layer
    separation not reconciled with the dissertation-only localization conclusion.
  target_ids:
  - cellstructuremech:stentor_myoneme_system
  evidence_ids:
  - native
  - maloney
  - yan-thesis
  - yan-final
  - centrin-family
  - sfi1-family
- assessment_id: taxonomic
  area: scope
  topic: Experimental species and native composition limits
  outcome: supported
  summary: Huang and Yan experimental S.coeruleus agree with ENA species5963. No genus-wide
    prevalence, full paralogue inventory or defined native stoichiometry is claimed.
  target_ids:
  - cellstructuremech:stentor_myoneme_system
  evidence_ids:
  - huang
  - yan-final
  - taxon
- assessment_id: function-graph
  area: graph
  topic: Perturbation versus force-generation mechanism
  outcome: supported
  summary: Final Results support parallel Sfi1-1/2 knockdown cable-pattern and contraction
    outcomes. RNAi2/3 cross-depletion prevents isoform-exclusive attribution. Existing
    NONMECHANISTIC graph has no cable-loss mediation edge, universal isoform requirement
    or invented motor cycle; kinetic values need not be added.
  target_ids:
  - cellstructuremech:stentor_myoneme_system
  evidence_ids:
  - native
  - newman
  - yan-final
- assessment_id: images
  area: provenance
  topic: TEM figure and licensing
  outcome: supported
  summary: Inspected Figure16 matches caption, scale, specimen and PDF page; source
    identity and versioned checksums verified. Link-only CC BY-NC-SA4.0 treatment
    preserved; no hosted image or inferred measurement.
  target_ids:
  - cellstructuremech:stentor_myoneme_system
  evidence_ids:
  - huang
  - native
- assessment_id: discussions
  area: completeness
  topic: Durable unknowns and version reconciliation
  outcome: concern
  summary: Family grounding, complete native composition and force generation remain
    genuine unknowns. The specific final-methods access gap can now be closed without
    pretending that mechanism is resolved; preserve the earlier dissertation account
    as historical evidence and explain the layer distinction.
  target_ids:
  - cellstructuremech:stentor_myoneme_system
  evidence_ids:
  - native
  - yan-final
  - yan-thesis
  - yan-metadata
- assessment_id: history
  area: ownership
  topic: Scientific status, history and prior findings
  outcome: supported
  summary: PROPOSED and both append-only histories are intact. Existing2006/2007 fixes
    remain visible; legacy review is not silently replaced. Scientific edits belong
    only to this maintained YAML with guarded writer, new EDIT provenance and generated
    page refresh.
  target_ids:
  - cellstructuremech:stentor_myoneme_system
  evidence_ids:
  - native
  - historical-review
  - baseline-qc
findings:
- finding_id: F1
  issue_key: stentor-myoneme-sfi1-source-version
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Reconcile Sfi1 localization with the final-paper cortical-depth results
  description: The component evidence correctly attributes absence of anterior centrin-mesh
    overlap to the dissertation, but the maintained record still treats detailed final
    evidence as inaccessible. PMC13637444.1 is now available and describes deeper
    anterior Sfi1/centrin mesh overlap while distinguishing outer lateral bands. Retaining
    only the older conclusion leaves a consequential unresolved version difference
    in constituent localization. Preserve the earlier source version, add the final
    layer-specific result, and update current source-access wording without widening
    the record to all centrin assemblies.
  target_ids:
  - cellstructuremech:stentor_myoneme_system
  field_paths:
  - components[sfi1_family_scaffolds].evidence
  - discussions[mechanism_and_source_versions]
  - evidence
  evidence_ids:
  - native
  - yan-thesis
  - yan-final
  - yan-metadata
  rule_id: review-checklist:components-and-source-version; review-yaml-record:preserve-conflicts
  native_severity: P3
  normalization_reason: 'Minor: bounded source-version reconciliation gap; the original
    attribution is explicitly historical, and identity, posterior membership and nonmechanistic
    function are not overturned.'
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stentor_myoneme_system.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Curate the final-paper layer-specific localization and controls while
    retaining dissertation provenance and biological uncertainties.
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:stentor_myoneme_system
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stentor_myoneme_system.yaml
    role: maintained scientific record
  generator: just render
  acceptance_checks:
  - Explicitly distinguish outer lateral bands from deeper anterior mesh colocalization
    and do not universalize absence.
  - Preserve the dissertation as an older distinct version; identify PMC author manuscript,
    DOI and reading scope.
  - Keep UNKNOWN essentialities, label-only grounding, PROPOSED status and nonmechanistic/nonmediation
    graph; disclose RNAi2/3 cross-depletion when using final isoform results.
  - Guarded write, append-only EDIT history, strict/history/full QC, generated output
    and review-contract checks pass.
  - Save a supported successor disposition with this exact review/finding identity
    after inspecting the fix.
limitations:
- Same-agent review only, not human sign-off or raw-data reanalysis. iModulonDB live28-dataset
  inventory is inapplicable to Stentor; absence there is not biological evidence.
- Yan final-paper author manuscript relevant Results, Discussion and STAR Methods
  inspected in checksum-verified XML. Oral-regeneration Results, supplementary files,
  movie pixels and final publisher typeset PDF were not fully inspected. No new numeric
  measurement is proposed.
- Dissertation Chapter2 printed24-33 inspected via readable primary web PDF; direct
  download returned202 with zero bytes. No claim that this local empty file is a readable
  PDF. Dissertation Methods not reread this pass; final-paper Methods were read independently.
- Newman1972 and Maloney2005 complete primary abstracts inspected; full Methods not
  readable this pass. Newman author-host PDF was located but local DNS failed and
  web screenshots yielded no inspectable pixels; PMC page challenge was not bypassed.
  Earlier legacy claims of full reading are historical, not this reviewer reading
  scope.
- All required deterministic checks passed. Current label checker603 no-adapter and
  CURIE251 skips retained; target authorities separately verified. Snippet check has0
  snippets among31 citations and does not prove literature support.
- Baseline full QC is exact unchanged-commit CI evidence, not a fresh local run. Current
  archive187 and four local contract tests passed. No repository scientific edits
  preceded this saved observation.
tags:
- scientific-review
- source-version
- stentor
```
