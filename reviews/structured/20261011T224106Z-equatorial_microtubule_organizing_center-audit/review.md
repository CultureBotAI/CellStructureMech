# Equatorial MTOC: Alp7 residual assembly evidence

- Review: 20261011T224106Z-equatorial_microtubule_organizing_center-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T22:33:54Z
- Finished UTC: 2026-10-11T22:41:06Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole native record reviewed. One minor curation gap: UNKNOWN Alp7 assembly essentiality omits the now-inspected deletion-backed residual formation evidence. Save before native edits.

## Scope And Provenance

Entire native YAML, six component classes and examples, one function, nine causal edges, all eight discussions, taxonomic and figure provenance, and both history surfaces.

Selection: One exact record in the 909-record review goal. Interphase MTOC remains separately partial.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0933988d785a383ecd3ad882c657e3893ff4902c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000923 | data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml | maintained | equatorial microtubule organizing center |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0000923 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:0000923 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:0000923 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| Exact-base native CI quality gates | passed | True | GO:0000923 | Exact main/native merge-group QC passed: 944 tests, 3 skips; 909 records and 1707 histories; generated products current. Separate exact-base identifier and label gates passed, with policy/no-adapter skips retained. |

## Scientific And Domain Assessments

### Identity, hierarchy, parthood and component grounding

grounding: supported. Targets: GO:0000923.

Resident equatorial nucleation assembly, not a single protein, entire ring, output array or SPB. GO parent and division-site parthood are correct. Label-only classes retain uncertain exact mappings; gamma-TuC and XMAP215 are correctly bounded. No exact ring geometry or native copy counts inferred.

### All components, function and nine graph edges

evidence: supported. Targets: GO:0000923.

Mto1/Mto2/gamma-TuC/Alp7/Alp14 residence and Rsp1 turnover machinery are supported. Assembly dependencies are not sufficiency or direct binding. Residual Mto2 activity is explicit; Rsp1 UNKNOWN remains appropriate for abstract-only loss-of-function evidence. Nucleation/output and genetic turnover edges retain their limits.

### Evidence-resolved Alp7 assembly classification

completeness: concern. Targets: GO:0000923.

Alp7 remains UNKNOWN for assembly essentiality despite now-inspected primary deletion evidence in DOI:10.1091/mbc.E05-08-0811. Results and Figure 5C-E show mia1 deletion retains equatorial Mto1, Alp4 and Rsp1 markers and transient nucleation, while sustained nucleation-site use and PAA maintenance fail. The local schema defines DISPENSABLE as formation, possibly defectively, without a component. Capture that bounded outcome for Alp7, matching the record's existing assembly-versus-maintenance policy; do not infer normal function, universal dispensability, interphase behavior or Rsp1 deletion evidence. This is an evidence-resolved curation gap, not a finding merely because a field is UNKNOWN.

### Taxonomy, figure, discussions and history

completeness: supported. Targets: GO:0000923.

Single-species evidence and reference accessions remain bounded. Exact licensed Figure 1 is traceable and unchanged. All eight rationales/three scopes are visible in generated text. Genuine unknown family mappings/turnover chemistry and unsupported optional fields are not defects. No matching S. pombe dataset in the adopted 28-dataset iModulonDB inventory.

## Findings

### F1: Record deletion-backed residual equatorial assembly without Alp7

minor / open / confirmed; issue key: equatorial-mtoc-alp7-residual-assembly.

Alp7 remains UNKNOWN for assembly essentiality despite now-inspected primary deletion evidence in DOI:10.1091/mbc.E05-08-0811. Results and Figure 5C-E show mia1 deletion retains equatorial Mto1, Alp4 and Rsp1 markers and transient nucleation, while sustained nucleation-site use and PAA maintenance fail. The local schema defines DISPENSABLE as formation, possibly defectively, without a component. Capture that bounded outcome for Alp7, matching the record's existing assembly-versus-maintenance policy; do not infer normal function, universal dispensability, interphase behavior or Rsp1 deletion evidence. This is an evidence-resolved curation gap, not a finding merely because a field is UNKNOWN.

## Recommended Actions And Acceptance Checks

### A1

Curate Alp7 residual assembly and source-access provenance.

- Set only Alp7 essentiality to DISPENSABLE with explicit S. pombe mia1-deletion scope and defective maintenance; retain Rsp1 UNKNOWN and Mto2 DISPENSABLE.
- Update the two assertion-local 2006 evidence notes and residual-assembly rationale to the inspected Results/Figure 5 evidence; preserve DOI and all graph content.
- Update access accounting without rewriting historical reports or events; no claim that unread 2006 supplements or all Results were inspected.
- Use the guarded writer and append actual Codex curation/EDIT history, regenerate the target page, pass focused red/green tests and native gates, and retain PROPOSED status.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml | context_only | Entire original YAML inspected before assessment; unchanged historical merged bytes. |
| rules | docs/CURATION.md | context_only | Essentiality concerns structure formation, not normal maintenance or cell viability. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml | context_only | EssentialityEnum DISPENSABLE means formation, possibly defectively, without the component. |
| source-checks | /private/tmp/csm-review-20261011T222903Z/emtoc-source-checks.json | context_only | Current visual/media and generated-text checks; historical discussion/history byte identity verified. |
| legacy | reports/yaml_record_review/20261006T031137Z-equatorial_microtubule_organizing_center.md | context_only | Original report and past issue resolutions inspected; retain access history and all original artifacts. |
| predecessors | /private/tmp/csm-review-20261011T222903Z/emtoc-predecessors.json | context_only | Ignored-inclusive structured predecessor scan has no exact-target predecessor. |
| dedup | /private/tmp/csm-review-20261011T222903Z/emtoc-issue-key.log | context_only | Fresh all-state exact-key dedup plus target issue search inspected. |
| history-0 | history/records/equatorial_microtubule_organizing_center/2026-10-06T031139Z-codex-a41835.yaml | context_only | Original append-only CREATE/EDIT history preserved. |
| history-1 | history/records/equatorial_microtubule_organizing_center/2026-10-06T031339Z-codex-72702a.yaml | context_only | Original append-only CREATE/EDIT history preserved. |
| history-2 | history/records/equatorial_microtubule_organizing_center/2026-10-06T031631Z-codex-5582be.yaml | context_only | Original append-only CREATE/EDIT history preserved. |
| history-3 | history/records/equatorial_microtubule_organizing_center/2026-10-06T034239Z-codex-18f7cb.yaml | context_only | Original append-only CREATE/EDIT history preserved. |
| mia1-2006 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1446099/; DOI:10.1091/mbc.E05-08-0811; Results sec14, Figure 5C-E, Methods and Discussion | supports | Actual primary full text: mia1 deletion retains equatorial Mto1/Alp4/Rsp1 markers and transient nucleation, but fails sustained use of nucleation sites. This is stronger than the historical abstract/caption access; no claim of normal maintenance. |
| mia1-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/ef7c/1446099/bd45711eb974/zmk0050676170005.jpg; Original Figure 5, especially C/D time series and E marker images | supports | Visually inspected wild-type/deletion comparison and equatorial markers; private review source only, no image import. |
| mto2-2005 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1142446/; DOI:10.1091/mbc.E04-11-1003; full Results, Discussion, Methods and main captions | supports | Mto2 deletion permits weak/transient PAA and faint Alp4; endogenous targeting differs from overexpression and cold shock. |
| mto2-second | https://pmc.ncbi.nlm.nih.gov/articles/PMC1142447/; DOI:10.1091/mbc.E04-12-1043; full Results, Discussion, Methods and main captions | supports | Stronger nondetection in a separate assay is preserved; ring-anchoring defects are bounded to cytokinesis delay or LatA perturbation. |
| mto1-2008 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=PMC2743986&amp;retmode=xml; Full Results, Discussion, Methods and Figures 1-6 captions | supports | CM1 mutations distinguish localization from gamma-TuC association; Figure 4E/F retains weak equatorial recruitment/nucleation in mto2 deletion. |
| mto1-2010 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2989437/fullTextXML; Results/Discussion and main captions, previously read and hash-verified | supports | Myp2/F-actin recruitment and Mto1 truncations support site-specific assembly dependencies. mto1-427 is not conflated with 1-1051/1-1065 Alp4 readouts; association need not be direct. |
| alp14-2018 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=PMC7263743&amp;retmode=xml; Results/Discussion/STAR Methods and main captions, previously read and hash-verified | supports | Alp7/Alp14 equatorial residence is supported; engineered interphase recruitment and nucleation-rate results are not equatorial measurements. |
| ring-2023 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10047812/fullTextXML; Results/Discussion/Methods and Figure 1 caption, previously read and hash-verified | supports | Offset/dosage and conditional stiffness inference are preserved; no universal cytokinesis anchoring requirement. |
| activation-2014 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3989768/fullTextXML; Results/Discussion | supports | Engineered bonsai stoichiometry and activation do not supply native equatorial copy counts. |
| phospho-2015 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4918325/fullTextXML; Mto2 homolog and quantification paragraphs | supports | Highly divergent fungal homologs exist; cytoplasmic mitotic quantification excluded equatorial-center-bearing cells. |
| lattice-2025 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11698074/fullTextXML; Discussion and main captions/context | supports | Klp2/Rsp1/Ssa1 pathway addresses lattice nucleation; not demonstrated equatorial turnover chemistry. |
| rsp1-2004 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fs1534-5807%2804%2900096-6%22&amp;format=json&amp;resultType=core; Primary abstract DOI:10.1016/s1534-5807(04)00096-6 | supports | Loss-of-function persistence supports turnover dependency, not complete protein absence or a resolved molecular disassembly reaction. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000226,GO:0000776,GO:0000923,GO:0000930,GO:0005634,GO:0005737,GO:0005815,GO:0005816,GO:0005818,GO:0005819,GO:0005822,GO:0005824,GO:0005874,GO:0005876,GO:0005879,GO:0005880,GO:0005881,GO:0007020,GO:0007059,GO:0015630,GO:0030981,GO:0030989,GO:0031021,GO:0031025,GO:0032117,GO:0032118,GO:0032153,GO:0051315,GO:0051415,GO:0051418,GO:0051647,GO:0061863,GO:0070850,GO:0072686,GO:0090307,GO:0099070,GO:0110165,GO:0140535,GO:1905720,GO:1990295; Exact identities, definitions, synonyms and typed relations | supports | Exact eMTOC identity/parent/division-site whole; PAA has-part is not inverted to universal parthood; gamma-TuC and function/disassembly scope verified. |
| protein-O94488 | https://rest.uniprot.org/uniprotkb/O94488.json; Accession, reviewed status, names/aliases, source taxon | supports | Identity verified; 972h- is a reference exemplar, not every experimental stock. |
| family-O94488 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O94488/?page_size=200; Complete native matches and entry types | supports | Whole-family/domain/broad-family distinctions preserved; empty Mto2 response is not global homology absence. |
| protein-Q9USP7 | https://rest.uniprot.org/uniprotkb/Q9USP7.json; Accession, reviewed status, names/aliases, source taxon | supports | Identity verified; 972h- is a reference exemplar, not every experimental stock. |
| family-Q9USP7 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9USP7/?page_size=200; Complete native matches and entry types | supports | Whole-family/domain/broad-family distinctions preserved; empty Mto2 response is not global homology absence. |
| protein-Q9Y705 | https://rest.uniprot.org/uniprotkb/Q9Y705.json; Accession, reviewed status, names/aliases, source taxon | supports | Identity verified; 972h- is a reference exemplar, not every experimental stock. |
| family-Q9Y705 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9Y705/?page_size=200; Complete native matches and entry types | supports | Whole-family/domain/broad-family distinctions preserved; empty Mto2 response is not global homology absence. |
| protein-Q9URY2 | https://rest.uniprot.org/uniprotkb/Q9URY2.json; Accession, reviewed status, names/aliases, source taxon | supports | Identity verified; 972h- is a reference exemplar, not every experimental stock. |
| family-Q9URY2 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9URY2/?page_size=200; Complete native matches and entry types | supports | Whole-family/domain/broad-family distinctions preserved; empty Mto2 response is not global homology absence. |
| protein-O94534 | https://rest.uniprot.org/uniprotkb/O94534.json; Accession, reviewed status, names/aliases, source taxon | supports | Identity verified; 972h- is a reference exemplar, not every experimental stock. |
| family-O94534 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O94534/?page_size=200; Complete native matches and entry types | supports | Whole-family/domain/broad-family distinctions preserved; empty Mto2 response is not global homology absence. |
| protein-O13601 | https://rest.uniprot.org/uniprotkb/O13601.json; Accession, reviewed status, names/aliases, source taxon | supports | Identity verified; 972h- is a reference exemplar, not every experimental stock. |
| family-O13601 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O13601/?page_size=200; Complete native matches and entry types | supports | Whole-family/domain/broad-family distinctions preserved; empty Mto2 response is not global homology absence. |
| taxon-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; ENA taxId/name/rank | supports | Species and reference strain distinguished. |
| taxon-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; ENA taxId/name/rank | supports | Species and reference strain distinguished. |
| figure-proof | /private/tmp/csm-review-20261011T222903Z/emtoc-image-source-proof.json | context_only | Exact-version metadata/JATS/licence and media checksums agree with hosted figure; later visual result in source-checks. |

## Limits And Additional Notes

- Same-agent review, not independent human approval or raw-data reanalysis.
- 2004 Rsp1 study remains abstract-only. The 2006 study assessment reads its equatorial Results section, main Methods, Discussion, abstract and Figure 5, not all Results, supplements or movies. Two 2005 full main Results/Discussion/Methods are now accessible; historical access notes remain factual for their original dates.
- Prior-continuation source text is reused only with verified hashes and original access dates. Site-specific evidence is not generalized to all MTOCs.
- Exact-baseline native QC/liveness/labels are verified CI, not a fresh full local QC run; resolver policy, no-adapter and three test skips remain explicit.
- Image pixels/captions and generated text were inspected; no browser-layout certification. The source Figure 5 is review-only and is not imported.
- Interphase MTOC remains partial; TACC/TOG has a separate clean completion without an output record.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T224106Z-equatorial_microtubule_organizing_center-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Equatorial MTOC: Alp7 residual assembly evidence'
started_at: '2026-10-11T22:33:54Z'
finished_at: '2026-10-11T22:41:06Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source and whole-record assessment; not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Whole native record reviewed. One minor curation gap: UNKNOWN Alp7 assembly
  essentiality omits the now-inspected deletion-backed residual formation evidence.
  Save before native edits.'
source:
  git_revision: 0933988d785a383ecd3ad882c657e3893ff4902c
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: README.md
    sha256: 3acb13884094f40c840ed3452a6209ee9a38b479ae16e4c0bca390c3c290828a
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/images/cytoskeleton/equatorial_microtubule_organizing_center/pmc10047812_cells_12_00917_f001.jpg
    sha256: e2952aa3563036f2c194633375e5ae6a5c53924da7824537b75828ead16db16b
    role: context
  - path: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
    sha256: 7e26dc96147d0fefc4f28ac7f012dcc69bc1f9a1ace03e94bf488a33ec59fd48
    role: target
  - path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    sha256: 230c0195bc1178cffbad27e77f4a1a4da56f20ec28dab5a43e192ed75d27dbbc
    role: context
  - path: data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
    sha256: adbd6ee4c956bfcb1a93d1d015b351adf92d66c025e980bfcd34630f1e8e6fb5
    role: context
  - path: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
    sha256: ec1b57e0607bc93e00bc6387142d7c452dec557894eb358423b3710ae06be7a3
    role: context
  - path: data/structures/cytoskeleton/quiescent_cell_microtubule_bundle.yaml
    sha256: 3ed050a7a95e721705ce773d2ac3093e0cc82c76b7061c5d6f76dc6703a280d1
    role: context
  - path: data/structures/cytoskeleton/quiescent_nuclear_microtubule_bundle.yaml
    sha256: c0a1869b5f5a4f4d81e55121c86afcbae0601961994cd79dd32b8a05163f37d5
    role: context
  - path: data/structures/cytoskeleton/radial_microtubule_organizing_center.yaml
    sha256: e42a1fd89a69cc61b886ae054a2f27f3477c526c7a4cfca8b63254264aa6858d
    role: context
  - path: data/structures/cytoskeleton/tacc_tog_complex.yaml
    sha256: 315d74b63309947276838f52dc5c9d7a63bc747efede86d6a7138c765afd7336
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
  - path: history/records/equatorial_microtubule_organizing_center/2026-10-06T031139Z-codex-a41835.yaml
    sha256: 82ef9f5cce2cf3ec99fe20a83bcd131c13d7e427d6bd169c09c146ec24b4b6ec
    role: context
  - path: history/records/equatorial_microtubule_organizing_center/2026-10-06T031339Z-codex-72702a.yaml
    sha256: 891832e88b93d24c6209bca588d0870d900b68cc6fe24d9fa6c248390baec090
    role: context
  - path: history/records/equatorial_microtubule_organizing_center/2026-10-06T031631Z-codex-5582be.yaml
    sha256: db0c1789bb6cce0addd5decdf334bbbb6d743ac520eb0149b8e3ae30bc64d379
    role: context
  - path: history/records/equatorial_microtubule_organizing_center/2026-10-06T034239Z-codex-18f7cb.yaml
    sha256: c3a6568e957c02da61fa2fb34cd846475488ba6a581101af4b68460873ee13dd
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: pages/structures/cytoskeleton/equatorial_microtubule_organizing_center.html
    sha256: 6bcd061a1fcb2e5d0c4bfe830960e666fa12429ff1dab874b066da1c2ac2f9cb
    role: context
  - path: reports/yaml_record_review/20261006T031137Z-equatorial_microtubule_organizing_center.md
    sha256: 205ad4e583be00db97e0933ece069432d3cb0a9d0ab7a8fa87d9f417e34d6983
    role: context
  - path: scripts/render_pages.py
    sha256: b5be74a8a3a0f7190b63da47a86cd8b48cbce4bb955ea0896f29d24f214a9b22
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/cellstructuremech/templates/structure.html
    sha256: 417b020a6eda677a1e40ecd3d849bfd5063d83291d7496e1c52a1a3a321f35ed
    role: context
targets:
- target_id: GO:0000923
  path: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
  label: equatorial microtubule organizing center
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
    role: maintained scientific record
scope:
  description: Entire native YAML, six component classes and examples, one function,
    nine causal edges, all eight discussions, taxonomic and figure provenance, and
    both history surfaces.
  selection: One exact record in the 909-record review goal. Interphase MTOC remains
    separately partial.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000923
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0000923
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T22:34:00Z to 2026-10-11T22:34:04Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0000923
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T22:34:04Z to 2026-10-11T22:34:10Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0000923
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
    --report /private/tmp/csm-review-20261011T222903Z/equatorial_microtubule_organizing_center-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T22:34:10Z to 2026-10-11T22:34:41Z; log SHA-256 6d08feea17b930a312a8587710fef382068359a9b2f40568f3de6a114e167b58
- check_id: baseline-qc
  name: Exact-base native CI quality gates
  status: passed
  required: true
  target_ids:
  - GO:0000923
  command: gh run view 38180160395 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  summary: 'Exact main/native merge-group QC passed: 944 tests, 3 skips; 909 records
    and 1707 histories; generated products current. Separate exact-base identifier
    and label gates passed, with policy/no-adapter skips retained.'
  scope_note: Live verification receipts baseline-ci, baseline-ci-full, native-liveness
    and native-labels in /private/tmp/csm-review-20261011T222903Z
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: 7e26dc96147d0fefc4f28ac7f012dcc69bc1f9a1ace03e94bf488a33ec59fd48
  support: context_only
  summary: Entire original YAML inspected before assessment; unchanged historical
    merged bytes.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Essentiality concerns structure formation, not normal maintenance or cell
    viability.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  support: context_only
  summary: EssentialityEnum DISPENSABLE means formation, possibly defectively, without
    the component.
- evidence_id: source-checks
  kind: validation
  reference: /private/tmp/csm-review-20261011T222903Z/emtoc-source-checks.json
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: 55a2504019146412a840be5644b49656e81aca3409fdef359fedc82443f529db
  support: context_only
  summary: Current visual/media and generated-text checks; historical discussion/history
    byte identity verified.
- evidence_id: legacy
  kind: prior_review
  reference: reports/yaml_record_review/20261006T031137Z-equatorial_microtubule_organizing_center.md
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: 205ad4e583be00db97e0933ece069432d3cb0a9d0ab7a8fa87d9f417e34d6983
  support: context_only
  summary: Original report and past issue resolutions inspected; retain access history
    and all original artifacts.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T222903Z/emtoc-predecessors.json
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: 39a13cd491019e538e62f292a043e11646206ad95b7e478e6897c61729d5a25b
  support: context_only
  summary: Ignored-inclusive structured predecessor scan has no exact-target predecessor.
- evidence_id: dedup
  kind: validation
  reference: /private/tmp/csm-review-20261011T222903Z/emtoc-issue-key.log
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: Fresh all-state exact-key dedup plus target issue search inspected.
- evidence_id: history-0
  kind: record_content
  reference: history/records/equatorial_microtubule_organizing_center/2026-10-06T031139Z-codex-a41835.yaml
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: 82ef9f5cce2cf3ec99fe20a83bcd131c13d7e427d6bd169c09c146ec24b4b6ec
  support: context_only
  summary: Original append-only CREATE/EDIT history preserved.
- evidence_id: history-1
  kind: record_content
  reference: history/records/equatorial_microtubule_organizing_center/2026-10-06T031339Z-codex-72702a.yaml
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: 891832e88b93d24c6209bca588d0870d900b68cc6fe24d9fa6c248390baec090
  support: context_only
  summary: Original append-only CREATE/EDIT history preserved.
- evidence_id: history-2
  kind: record_content
  reference: history/records/equatorial_microtubule_organizing_center/2026-10-06T031631Z-codex-5582be.yaml
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: db0c1789bb6cce0addd5decdf334bbbb6d743ac520eb0149b8e3ae30bc64d379
  support: context_only
  summary: Original append-only CREATE/EDIT history preserved.
- evidence_id: history-3
  kind: record_content
  reference: history/records/equatorial_microtubule_organizing_center/2026-10-06T034239Z-codex-18f7cb.yaml
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: c3a6568e957c02da61fa2fb34cd846475488ba6a581101af4b68460873ee13dd
  support: context_only
  summary: Original append-only CREATE/EDIT history preserved.
- evidence_id: mia1-2006
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1446099/
  locator: DOI:10.1091/mbc.E05-08-0811; Results sec14, Figure 5C-E, Methods and Discussion
  accessed_at: '2026-10-11T22:37:37Z'
  snapshot_sha256: 3b176d49607b7e0cdbace2c179088cd322f81ebfc88e67ecf461a7d0edcda4cc
  support: supports
  summary: 'Actual primary full text: mia1 deletion retains equatorial Mto1/Alp4/Rsp1
    markers and transient nucleation, but fails sustained use of nucleation sites.
    This is stronger than the historical abstract/caption access; no claim of normal
    maintenance.'
- evidence_id: mia1-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/ef7c/1446099/bd45711eb974/zmk0050676170005.jpg
  locator: Original Figure 5, especially C/D time series and E marker images
  accessed_at: '2026-10-11T22:38:45Z'
  snapshot_sha256: 6ff2edde2cf018e79f01e49547b9ed6a0e81201a684174c3a1630585eb5de2e5
  support: supports
  summary: Visually inspected wild-type/deletion comparison and equatorial markers;
    private review source only, no image import.
- evidence_id: mto2-2005
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1142446/
  locator: DOI:10.1091/mbc.E04-11-1003; full Results, Discussion, Methods and main
    captions
  accessed_at: '2026-10-11T22:37:00Z'
  snapshot_sha256: e24899419a8fb1e5edb6799547fc0307f38ded5ea95d548353b11e0cccaed4cb
  support: supports
  summary: Mto2 deletion permits weak/transient PAA and faint Alp4; endogenous targeting
    differs from overexpression and cold shock.
- evidence_id: mto2-second
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1142447/
  locator: DOI:10.1091/mbc.E04-12-1043; full Results, Discussion, Methods and main
    captions
  accessed_at: '2026-10-11T22:37:37Z'
  snapshot_sha256: 1bd492fb8438308b0af674676862f8624cb117ea428015fab4e6dd3e1e6ccfd7
  support: supports
  summary: Stronger nondetection in a separate assay is preserved; ring-anchoring
    defects are bounded to cytokinesis delay or LatA perturbation.
- evidence_id: mto1-2008
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMC2743986&retmode=xml
  locator: Full Results, Discussion, Methods and Figures 1-6 captions
  accessed_at: '2026-10-11T20:52:27Z'
  snapshot_sha256: 0de5fdf675e8d4f305b3d3a8248b5d26f9b314da51222a8db5e36409beac5a39
  support: supports
  summary: CM1 mutations distinguish localization from gamma-TuC association; Figure
    4E/F retains weak equatorial recruitment/nucleation in mto2 deletion.
- evidence_id: mto1-2010
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2989437/fullTextXML
  locator: Results/Discussion and main captions, previously read and hash-verified
  accessed_at: '2026-10-11T20:50:43Z'
  snapshot_sha256: 844941c6aefa5a0b9b86bfa8918a7a8657637a1f5088cc8122483d67ca452616
  support: supports
  summary: Myp2/F-actin recruitment and Mto1 truncations support site-specific assembly
    dependencies. mto1-427 is not conflated with 1-1051/1-1065 Alp4 readouts; association
    need not be direct.
- evidence_id: alp14-2018
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMC7263743&retmode=xml
  locator: Results/Discussion/STAR Methods and main captions, previously read and
    hash-verified
  accessed_at: '2026-10-11T20:51:51Z'
  snapshot_sha256: d734ac81e937c81ee8901e14a79bf581a3aa0cb2df184d6387e6ad014346fa75
  support: supports
  summary: Alp7/Alp14 equatorial residence is supported; engineered interphase recruitment
    and nucleation-rate results are not equatorial measurements.
- evidence_id: ring-2023
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10047812/fullTextXML
  locator: Results/Discussion/Methods and Figure 1 caption, previously read and hash-verified
  accessed_at: '2026-10-11T20:51:23Z'
  snapshot_sha256: 02fb84ec9de76eeae0fee1c5c7750b2641de9497a1ffa9904898e17864eb910e
  support: supports
  summary: Offset/dosage and conditional stiffness inference are preserved; no universal
    cytokinesis anchoring requirement.
- evidence_id: activation-2014
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3989768/fullTextXML
  locator: Results/Discussion
  accessed_at: '2026-10-11T20:50:47Z'
  snapshot_sha256: 7fd53c538d7300534143ca9ca8c68dc322982939aad5ec87eb7c58a3fb1d40a4
  support: supports
  summary: Engineered bonsai stoichiometry and activation do not supply native equatorial
    copy counts.
- evidence_id: phospho-2015
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4918325/fullTextXML
  locator: Mto2 homolog and quantification paragraphs
  accessed_at: '2026-10-11T20:50:52Z'
  snapshot_sha256: 7db79b1ff5c9f12e41fbb77e955fe363c467bfd467950a204cfb3236b1c5c286
  support: supports
  summary: Highly divergent fungal homologs exist; cytoplasmic mitotic quantification
    excluded equatorial-center-bearing cells.
- evidence_id: lattice-2025
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11698074/fullTextXML
  locator: Discussion and main captions/context
  accessed_at: '2026-10-11T20:51:18Z'
  snapshot_sha256: b8fe2d3705650333215b17946f293e9d10a512ea21bcc26052ddb983839d0ff1
  support: supports
  summary: Klp2/Rsp1/Ssa1 pathway addresses lattice nucleation; not demonstrated equatorial
    turnover chemistry.
- evidence_id: rsp1-2004
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fs1534-5807%2804%2900096-6%22&format=json&resultType=core
  locator: Primary abstract DOI:10.1016/s1534-5807(04)00096-6
  accessed_at: '2026-10-11T20:50:49Z'
  snapshot_sha256: 5e862e9293ee598835c0c101db4948afc4b6391130e3835fe4c69a284fd189da
  support: supports
  summary: Loss-of-function persistence supports turnover dependency, not complete
    protein absence or a resolved molecular disassembly reaction.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000226,GO:0000776,GO:0000923,GO:0000930,GO:0005634,GO:0005737,GO:0005815,GO:0005816,GO:0005818,GO:0005819,GO:0005822,GO:0005824,GO:0005874,GO:0005876,GO:0005879,GO:0005880,GO:0005881,GO:0007020,GO:0007059,GO:0015630,GO:0030981,GO:0030989,GO:0031021,GO:0031025,GO:0032117,GO:0032118,GO:0032153,GO:0051315,GO:0051415,GO:0051418,GO:0051647,GO:0061863,GO:0070850,GO:0072686,GO:0090307,GO:0099070,GO:0110165,GO:0140535,GO:1905720,GO:1990295
  locator: Exact identities, definitions, synonyms and typed relations
  accessed_at: '2026-10-11T20:51:58Z'
  snapshot_sha256: b4a25cd70fae0cba6cddd4a8e5712338ace5b06060e4e6112b8a71d52a5506b1
  support: supports
  summary: Exact eMTOC identity/parent/division-site whole; PAA has-part is not inverted
    to universal parthood; gamma-TuC and function/disassembly scope verified.
- evidence_id: protein-O94488
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O94488.json
  locator: Accession, reviewed status, names/aliases, source taxon
  accessed_at: '2026-10-11T20:52:06Z'
  snapshot_sha256: 4903509b256bf5164ea7e5b80970bbb89056a71a4ea4a257e9feb8adcaf0e46b
  support: supports
  summary: Identity verified; 972h- is a reference exemplar, not every experimental
    stock.
- evidence_id: family-O94488
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O94488/?page_size=200
  locator: Complete native matches and entry types
  accessed_at: '2026-10-11T20:52:09Z'
  snapshot_sha256: 475c2fa2c23696d5933a5f8278316b1d74bb8b282f9d954daa3b084e382dd7a9
  support: supports
  summary: Whole-family/domain/broad-family distinctions preserved; empty Mto2 response
    is not global homology absence.
- evidence_id: protein-Q9USP7
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9USP7.json
  locator: Accession, reviewed status, names/aliases, source taxon
  accessed_at: '2026-10-11T20:53:07Z'
  snapshot_sha256: ae275cdd142bdffa04ce4e120465b57fbd20dbe1223de0be9a72966ec6e40698
  support: supports
  summary: Identity verified; 972h- is a reference exemplar, not every experimental
    stock.
- evidence_id: family-Q9USP7
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9USP7/?page_size=200
  locator: Complete native matches and entry types
  accessed_at: '2026-10-11T20:53:08Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  support: supports
  summary: Whole-family/domain/broad-family distinctions preserved; empty Mto2 response
    is not global homology absence.
- evidence_id: protein-Q9Y705
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9Y705.json
  locator: Accession, reviewed status, names/aliases, source taxon
  accessed_at: '2026-10-11T20:53:09Z'
  snapshot_sha256: 1735b88bbff6bce84e252460f2f8e64bb72fbe3901bd81b9f1db63cba4d23682
  support: supports
  summary: Identity verified; 972h- is a reference exemplar, not every experimental
    stock.
- evidence_id: family-Q9Y705
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9Y705/?page_size=200
  locator: Complete native matches and entry types
  accessed_at: '2026-10-11T20:53:12Z'
  snapshot_sha256: e6cb5f9d94ae430dd59a84be23c1c0b122e8cc79f7a5cffdcdeefe4c93bb89a9
  support: supports
  summary: Whole-family/domain/broad-family distinctions preserved; empty Mto2 response
    is not global homology absence.
- evidence_id: protein-Q9URY2
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9URY2.json
  locator: Accession, reviewed status, names/aliases, source taxon
  accessed_at: '2026-10-11T20:53:02Z'
  snapshot_sha256: 69a22093a5968e9a614a5170718632ab935b0628867cab263df68ad3bb240fe7
  support: supports
  summary: Identity verified; 972h- is a reference exemplar, not every experimental
    stock.
- evidence_id: family-Q9URY2
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9URY2/?page_size=200
  locator: Complete native matches and entry types
  accessed_at: '2026-10-11T20:53:04Z'
  snapshot_sha256: 03fb62580d358165f529e289536f7dbf5f6bdaf12119343b73f88db231a224f9
  support: supports
  summary: Whole-family/domain/broad-family distinctions preserved; empty Mto2 response
    is not global homology absence.
- evidence_id: protein-O94534
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O94534.json
  locator: Accession, reviewed status, names/aliases, source taxon
  accessed_at: '2026-10-11T20:52:10Z'
  snapshot_sha256: 257ba28d9d0e8203582177682405142bf2445317baad602e9f31a1171e13a722
  support: supports
  summary: Identity verified; 972h- is a reference exemplar, not every experimental
    stock.
- evidence_id: family-O94534
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O94534/?page_size=200
  locator: Complete native matches and entry types
  accessed_at: '2026-10-11T20:52:12Z'
  snapshot_sha256: f62d9723b32a2c5c0641202d2b4296c8edf971796e4d4c18b72950a047b2aef7
  support: supports
  summary: Whole-family/domain/broad-family distinctions preserved; empty Mto2 response
    is not global homology absence.
- evidence_id: protein-O13601
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O13601.json
  locator: Accession, reviewed status, names/aliases, source taxon
  accessed_at: '2026-10-11T20:52:01Z'
  snapshot_sha256: f2fe8b41baa1ba1a11a257e091c9b73b5133e8c61ce97d53456d7ddaf9430936
  support: supports
  summary: Identity verified; 972h- is a reference exemplar, not every experimental
    stock.
- evidence_id: family-O13601
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O13601/?page_size=200
  locator: Complete native matches and entry types
  accessed_at: '2026-10-11T20:52:03Z'
  snapshot_sha256: 757e197bfcbfbd3f5d70da4ffd10b5d83af022b6a572775a95431f6995a88394
  support: supports
  summary: Whole-family/domain/broad-family distinctions preserved; empty Mto2 response
    is not global homology absence.
- evidence_id: taxon-4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: ENA taxId/name/rank
  accessed_at: '2026-10-11T20:51:59Z'
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
  support: supports
  summary: Species and reference strain distinguished.
- evidence_id: taxon-284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: ENA taxId/name/rank
  accessed_at: '2026-10-11T20:51:59Z'
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
  support: supports
  summary: Species and reference strain distinguished.
- evidence_id: figure-proof
  kind: validation
  reference: /private/tmp/csm-review-20261011T222903Z/emtoc-image-source-proof.json
  accessed_at: '2026-10-11T22:41:06Z'
  snapshot_sha256: 017ad80acd9b936eb9b27f73d02460ab62b65660d546545a3ed0dc780de79837
  support: context_only
  summary: Exact-version metadata/JATS/licence and media checksums agree with hosted
    figure; later visual result in source-checks.
assessments:
- assessment_id: identity
  area: grounding
  topic: Identity, hierarchy, parthood and component grounding
  outcome: supported
  target_ids:
  - GO:0000923
  evidence_ids:
  - record
  - go
  summary: Resident equatorial nucleation assembly, not a single protein, entire ring,
    output array or SPB. GO parent and division-site parthood are correct. Label-only
    classes retain uncertain exact mappings; gamma-TuC and XMAP215 are correctly bounded.
    No exact ring geometry or native copy counts inferred.
- assessment_id: biology
  area: evidence
  topic: All components, function and nine graph edges
  outcome: supported
  target_ids:
  - GO:0000923
  evidence_ids:
  - record
  - mto1-2010
  - mto1-2008
  - mto2-2005
  - mto2-second
  - alp14-2018
  - rsp1-2004
  - ring-2023
  summary: Mto1/Mto2/gamma-TuC/Alp7/Alp14 residence and Rsp1 turnover machinery are
    supported. Assembly dependencies are not sufficiency or direct binding. Residual
    Mto2 activity is explicit; Rsp1 UNKNOWN remains appropriate for abstract-only
    loss-of-function evidence. Nucleation/output and genetic turnover edges retain
    their limits.
- assessment_id: alp7-assembly
  area: completeness
  topic: Evidence-resolved Alp7 assembly classification
  outcome: concern
  target_ids:
  - GO:0000923
  evidence_ids:
  - record
  - schema
  - rules
  - mia1-2006
  - mia1-figure
  summary: Alp7 remains UNKNOWN for assembly essentiality despite now-inspected primary
    deletion evidence in DOI:10.1091/mbc.E05-08-0811. Results and Figure 5C-E show
    mia1 deletion retains equatorial Mto1, Alp4 and Rsp1 markers and transient nucleation,
    while sustained nucleation-site use and PAA maintenance fail. The local schema
    defines DISPENSABLE as formation, possibly defectively, without a component. Capture
    that bounded outcome for Alp7, matching the record's existing assembly-versus-maintenance
    policy; do not infer normal function, universal dispensability, interphase behavior
    or Rsp1 deletion evidence. This is an evidence-resolved curation gap, not a finding
    merely because a field is UNKNOWN.
- assessment_id: provenance
  area: completeness
  topic: Taxonomy, figure, discussions and history
  outcome: supported
  target_ids:
  - GO:0000923
  evidence_ids:
  - record
  - source-checks
  - figure-proof
  - legacy
  - phospho-2015
  - lattice-2025
  - activation-2014
  summary: Single-species evidence and reference accessions remain bounded. Exact
    licensed Figure 1 is traceable and unchanged. All eight rationales/three scopes
    are visible in generated text. Genuine unknown family mappings/turnover chemistry
    and unsupported optional fields are not defects. No matching S. pombe dataset
    in the adopted 28-dataset iModulonDB inventory.
findings:
- finding_id: F1
  issue_key: equatorial-mtoc-alp7-residual-assembly
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Record deletion-backed residual equatorial assembly without Alp7
  description: Alp7 remains UNKNOWN for assembly essentiality despite now-inspected
    primary deletion evidence in DOI:10.1091/mbc.E05-08-0811. Results and Figure 5C-E
    show mia1 deletion retains equatorial Mto1, Alp4 and Rsp1 markers and transient
    nucleation, while sustained nucleation-site use and PAA maintenance fail. The
    local schema defines DISPENSABLE as formation, possibly defectively, without a
    component. Capture that bounded outcome for Alp7, matching the record's existing
    assembly-versus-maintenance policy; do not infer normal function, universal dispensability,
    interphase behavior or Rsp1 deletion evidence. This is an evidence-resolved curation
    gap, not a finding merely because a field is UNKNOWN.
  target_ids:
  - GO:0000923
  field_paths:
  - components[3].essentiality
  - components[3].evidence
  - components[3].protein_examples[0].evidence
  - discussions[3].rationale
  evidence_ids:
  - record
  - schema
  - rules
  - mia1-2006
  - mia1-figure
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#components
  native_severity: minor
  normalization_reason: Bounded evidence-resolved classification gap. Identity and
    maintenance claims remain supported; no unsupported mechanism or essential-assembly
    assertion is alleged.
actions:
- action_id: A1
  description: Curate Alp7 residual assembly and source-access provenance.
  finding_ids:
  - F1
  target_ids:
  - GO:0000923
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
    role: maintained scientific record
  acceptance_checks:
  - Set only Alp7 essentiality to DISPENSABLE with explicit S. pombe mia1-deletion
    scope and defective maintenance; retain Rsp1 UNKNOWN and Mto2 DISPENSABLE.
  - Update the two assertion-local 2006 evidence notes and residual-assembly rationale
    to the inspected Results/Figure 5 evidence; preserve DOI and all graph content.
  - Update access accounting without rewriting historical reports or events; no claim
    that unread 2006 supplements or all Results were inspected.
  - Use the guarded writer and append actual Codex curation/EDIT history, regenerate
    the target page, pass focused red/green tests and native gates, and retain PROPOSED
    status.
limitations:
- Same-agent review, not independent human approval or raw-data reanalysis.
- 2004 Rsp1 study remains abstract-only. The 2006 study assessment reads its equatorial
  Results section, main Methods, Discussion, abstract and Figure 5, not all Results,
  supplements or movies. Two 2005 full main Results/Discussion/Methods are now accessible;
  historical access notes remain factual for their original dates.
- Prior-continuation source text is reused only with verified hashes and original
  access dates. Site-specific evidence is not generalized to all MTOCs.
- Exact-baseline native QC/liveness/labels are verified CI, not a fresh full local
  QC run; resolver policy, no-adapter and three test skips remain explicit.
- Image pixels/captions and generated text were inspected; no browser-layout certification.
  The source Figure 5 is review-only and is not imported.
- Interphase MTOC remains partial; TACC/TOG has a separate clean completion without
  an output record.
```
