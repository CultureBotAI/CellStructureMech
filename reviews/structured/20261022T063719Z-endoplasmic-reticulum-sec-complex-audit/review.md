# Source-grounded review of endoplasmic reticulum Sec complex

- Review: 20261022T063719Z-endoplasmic-reticulum-sec-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:16:07Z
- Finished UTC: 2026-10-22T06:37:19Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: exact Sec parent identity, two-subcomplex boundary, yeast membrane placement and descriptive import graph are supported. Reconstitution abstract access and partial Sec62 structural resolution remain explicit limitations.

## Scope And Provenance

Exactly one complete maintained target; source-native and primary reading scopes are declared individually. Scientific inputs remain unchanged.

Selection: One complete record in strict-path batch 54 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031205 | data/structures/other/endoplasmic_reticulum_sec_complex.yaml | maintained | endoplasmic reticulum Sec complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0031205 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031205 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0031205 | Focused check passed; source claims assessed separately. |
| Native focused verify | passed | True | GO:0031205 | Focused check passed; source claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0031205 | No iModulon-specific claim is made; May2009 expression assays are assessed directly where applicable. |
| Claim-level scientific review | passed | True | GO:0031205 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031205 | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031205 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031205 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031205 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031205 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031205 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Parent assembly and two distinct subcomplexes

identity: supported. Targets: GO:0031205.

Exact GO identity and declared is_a,part_of and has_part boundaries are supported. The Sec61 heterotrimer and yeast Sec62/Sec63 tetramer remain distinct subcomplexes within the seven-subunit parent.

### Subcomplex representation is intentional and sufficient

grounding: supported. Targets: GO:0031205.

The resolved hierarchy discussion correctly avoids duplicating seven lower-level component rows. No absent optional individual-protein inventory is manufactured as a completeness finding. Native composition and purified seven-component material support this modeling choice.

### Reconstitution, contact assays and structural resolution

evidence: supported. Targets: GO:0031205.

Panzner1995 complete abstract distinguishes purified seven-protein Sec complex from separately added lumenal Kar2 and ATP. Plath supports the named substrate contacts, including Sec62-specific denaturing immunoprecipitation. Wu supports overall topology while Sec62 has only weak-density docking and one TM; the general structural wording does not explicitly claim every residue or subunit was atomically resolved.

### Supported descriptive topology and import function

graph: supported. Targets: GO:0031205.

The NONMECHANISTIC graph records subcomplex membership, membrane embedding and posttranslational import. The record does not turn Kar2 or transient substrates into permanent Sec constituents, nor claim a detailed mechanistic reconstruction of all translocation stages.

### Yeast subcomplex composition and model strains

scope: supported. Targets: GO:0031205.

The canonical reconstitution and native term scope are yeast-specific. Sec71/Sec72 are not generalized to all eukaryotes. Wu uses endogenous BY4741; no S288C protein-example rows are invented. COMMON retains its defined qualitative meaning and is not a measured strain census.

### Assembly observations do not imply all absence outcomes

grounding: unknown. Targets: GO:0031205.

Co-purification and resolved contacts support architecture but do not automatically establish component-removal consequences. The target makes no categorical individual-protein essentiality claim, and no such universal assertion is added.

### Whole maintained target and bounded follow-up

completeness: supported. Targets: GO:0031205.

Every maintained field, evidence row, component/example, graph edge, discussion and history entry was read. Required defects are distinguished from optional enrichment and unavailable source detail. Scientific status/history remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/endoplasmic_reticulum_sec_complex.yaml; Entire maintained record, including evidence, components, graphs, discussions, imported composition and history where present | context_only | The complete maintained target was read. Neighboring records are not automatically reviewed by this observation. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, StructuralComponent, PresenceEnum and graph scope | context_only | Formation necessity differs from activity, recruitment into a larger assembly or viability. Where used, COMMON means present in most members with exceptional losses. This category is distinct from a measured prevalence census. |
| curation | docs/CURATION.md; Exact class mapping and protein-example boundaries | context_only | A whole-protein family grounds a constituent class; a taxon-paired accession supplies a representative instance. Domain or broader superfamily mappings do not necessarily resolve exact class tasks. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Directed evidence and mechanistic scope | context_only | Descriptive membership and function graphs are distinguished from causal assembly dependencies and detailed molecular mechanisms. |
| root54-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005784,GO:0005789,GO:0006260,GO:0008622,GO:0031205,GO:0031207,GO:0042575,GO:0042910,GO:0140330,GO:0140534,GO:1990281; Eleven native terms: identity/status, complete definitions, synonyms/comments and relevant typed child relations only | supports | GO0031205 identifies the parent ER Sec complex; GO0140534 is its is_a parent and GO0005789 its membrane context. GO0005784 identifies the Sec61 subcomplex; GO0031207 identifies the yeast Sec62/Sec63 tetramer. Typed part_of children are not converted to is_a relations. |
| root54-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | ENA taxId4932 identifies Saccharomyces cerevisiae; the complete name/rank/lineage response was read. |
| root54-sources-GO0031205-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031205/ancestors?relations=is_a; Complete native ancestor response | supports | The complete is_a-only ancestry contains the declared parent. It is not a parthood or distribution census. |
| root54-sources-GO0031205-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031205/constraints; Focal taxonConstraints array only | context_only | The focal term is constrained to Eukaryota; this restriction does not establish occurrence in every eukaryotic organism. |
| root54-sources-doi-10.1016_0092-8674-95-90077-2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2F0092-8674%2895%2990077-2%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI result, exact PMID/DOI/PMCID and complete abstractText | supports | Unique DOI result is MED7758110: Posttranslational protein transport in yeast reconstituted with a purified complex of Sec proteins and Kar2p., Panzner S, Dreier L, Hartmann E, Kostka S, Rapoport TA. (1995). Its whole native abstract and bibliographic identity were read. |
| root54-sources-doi-10.1038_s41586-018-0856-x | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41586-018-0856-x%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI result, exact PMID/DOI/PMCID and complete abstractText | supports | Unique DOI result is MED30644436: Structure of the post-translational protein translocation machinery of the ER membrane., Wu X, Cabanos C, Rapoport TA. (2019). Its whole native abstract and bibliographic identity were read. |
| root54-sources-doi-10.1091_mbc.e03-06-0390 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e03-06-0390%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI result, exact PMID/DOI/PMCID and complete abstractText | supports | Unique DOI result is MED14617809: Interactions between Sec complex and prepro-alpha-factor during posttranslational protein transport into the endoplasmic reticulum., Plath K, Wilkinson BM, Stirling CJ, Rapoport TA. (2004). Its whole native abstract and bibliographic identity were read. |
| root54-sources-primary-PMC6367035 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6367035/; Wu2019 complete main paragraphs P4-P14; Methods S2 strains,S3 purification,S4 sample/data acquisition,S6 model building; Figure1, ExtendedDataFigure3/F7 captions and FN2 data availability. S5 image processing,S7 mutagenesis,other captions/supplements/pixels not read. | supports | The purified endogenous BY4741 complex contained all seven proteins in roughly stoichiometric amounts. The4.1A reconstruction supports the subcomplex architecture and Sec63-mediated lateral-gate opening. Sec62 density is weak: a DEP-like homology model was docked and one TM identified; deposited coordinates omit Sec62. This is not a fully resolved atomic model of every subunit. |
| root54-sources-primary-PMC307522 | https://pmc.ncbi.nlm.nih.gov/articles/PMC307522/; Plath2004 complete Methods sec3,sec6,sec7 and Results sec11 including Figures1/2 captions and Table1. Other sections and pixels not read. | supports | Purified yeast Sec complexes and ppalphaF crosslinking support simultaneous signal-sequence contacts. Single-band measurements combine Sec62/71, but the double-crosslinked Sec61-ppalphaF-Sec62 product is specifically immunoprecipitated under denaturing conditions with Sec61 and Sec62 antibodies. Thus the record’s bounded Sec62 contact statement has support. Kar2-dependent transport intermediates are distinct from initial binding without Kar2. |
| schema-result | just validate data/structures/other/endoplasmic_reticulum_sec_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/endoplasmic_reticulum_sec_complex.yaml |
| strict-result | just validate-strict data/structures/other/endoplasmic_reticulum_sec_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/endoplasmic_reticulum_sec_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/endoplasmic_reticulum_sec_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/endoplasmic_reticulum_sec_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch54-20261022-hapbq96w/endoplasmic_reticulum_sec_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/endoplasmic_reticulum_sec_complex.yaml; Complete focused native report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/endoplasmic_reticulum_sec_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/endoplasmic_reticulum_sec_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw datasets, atomic coordinates, sequence alignments or supplemental data files were reanalyzed. Primary reading is limited to the exact sections declared in individual evidence rows.
- Panzner1995 was read at complete native abstract tier; the verified publisher route returned403. Wu and Plath body inspection is restricted to the enumerated sections. The Sec62 weak-density/homology-model limitation remains material despite support for overall subcomplex topology.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations and issue-bearing reviews alike.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T063719Z-endoplasmic-reticulum-sec-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of endoplasmic reticulum Sec complex
started_at: '2026-10-22T06:16:07Z'
finished_at: '2026-10-22T06:37:19Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Qualified pass: exact Sec parent identity, two-subcomplex boundary, yeast
  membrane placement and descriptive import graph are supported. Reconstitution abstract
  access and partial Sec62 structural resolution remain explicit limitations.'
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
  state: working_tree
  inputs:
  - path: .claude/skills/curate-causal-graphs/SKILL.md
    sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/literature-evidence/SKILL.md
    sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/other/endoplasmic_reticulum_sec_complex.yaml
    sha256: 9c518bbd838470051ecd41f44fade19a7575e189a7ee995022f6447240cbae4f
    role: target
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
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0031205
  path: data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  label: endoplasmic reticulum Sec complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/endoplasmic_reticulum_sec_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target; source-native and primary reading
    scopes are declared individually. Scientific inputs remain unchanged.
  selection: One complete record in strict-path batch 54 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031205
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: just validate data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: just validate-strict data/structures/other/endoplasmic_reticulum_sec_complex.yaml
    --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/endoplasmic_reticulum_sec_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  exit_code: 0
  summary: Focused check passed; source claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  exit_code: 0
  summary: Focused check passed; source claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0031205
  summary: No iModulon-specific claim is made; May2009 expression assays are assessed
    directly where applicable.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0031205
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root54-sources-go
  - root54-sources-tax4932
  - root54-sources-GO0031205-ancestors
  - root54-sources-GO0031205-constraints
  - root54-sources-doi-10.1016_0092-8674-95-90077-2
  - root54-sources-doi-10.1038_s41586-018-0856-x
  - root54-sources-doi-10.1091_mbc.e03-06-0390
  - root54-sources-primary-PMC6367035
  - root54-sources-primary-PMC307522
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031205
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:34Z to
    2026-10-22T01:34:04Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  locator: Entire maintained record, including evidence, components, graphs, discussions,
    imported composition and history where present
  accessed_at: '2026-10-22T06:30:42Z'
  support: context_only
  summary: The complete maintained target was read. Neighboring records are not automatically
    reviewed by this observation.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, StructuralComponent, PresenceEnum and graph scope
  accessed_at: '2026-10-22T06:30:42Z'
  support: context_only
  summary: Formation necessity differs from activity, recruitment into a larger assembly
    or viability. Where used, COMMON means present in most members with exceptional
    losses. This category is distinct from a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class mapping and protein-example boundaries
  accessed_at: '2026-10-22T06:30:42Z'
  support: context_only
  summary: A whole-protein family grounds a constituent class; a taxon-paired accession
    supplies a representative instance. Domain or broader superfamily mappings do
    not necessarily resolve exact class tasks.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Directed evidence and mechanistic scope
  accessed_at: '2026-10-22T06:30:42Z'
  support: context_only
  summary: Descriptive membership and function graphs are distinguished from causal
    assembly dependencies and detailed molecular mechanisms.
- evidence_id: root54-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005784,GO:0005789,GO:0006260,GO:0008622,GO:0031205,GO:0031207,GO:0042575,GO:0042910,GO:0140330,GO:0140534,GO:1990281
  locator: 'Eleven native terms: identity/status, complete definitions, synonyms/comments
    and relevant typed child relations only'
  accessed_at: '2026-10-22T06:18:43.212342Z'
  support: supports
  summary: GO0031205 identifies the parent ER Sec complex; GO0140534 is its is_a parent
    and GO0005789 its membrane context. GO0005784 identifies the Sec61 subcomplex;
    GO0031207 identifies the yeast Sec62/Sec63 tetramer. Typed part_of children are
    not converted to is_a relations.
  snapshot_sha256: 19cd6bbb55b31ec2bbb98181c611734e9319f4dce2181b144c23335d9ab9cc1e
- evidence_id: root54-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:18:43.212607Z'
  support: supports
  summary: ENA taxId4932 identifies Saccharomyces cerevisiae; the complete name/rank/lineage
    response was read.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root54-sources-GO0031205-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031205/ancestors?relations=is_a
  locator: Complete native ancestor response
  accessed_at: '2026-10-22T06:18:48.857699Z'
  support: supports
  summary: The complete is_a-only ancestry contains the declared parent. It is not
    a parthood or distribution census.
  snapshot_sha256: 4e5d21b49907c6724767f7807f4fec33d49c7648c26f2224dc85f0754af9e3d1
- evidence_id: root54-sources-GO0031205-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031205/constraints
  locator: Focal taxonConstraints array only
  accessed_at: '2026-10-22T06:18:48.998253Z'
  support: context_only
  summary: The focal term is constrained to Eukaryota; this restriction does not establish
    occurrence in every eukaryotic organism.
  snapshot_sha256: 1df3dfa6b80862bc6260df27bf7e85d12aa6f3bec29691b4cb77fbe2800c414e
- evidence_id: root54-sources-doi-10.1016_0092-8674-95-90077-2
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2F0092-8674%2895%2990077-2%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI result, exact PMID/DOI/PMCID and complete abstractText
  accessed_at: '2026-10-22T06:18:47.726433Z'
  support: supports
  summary: 'Unique DOI result is MED7758110: Posttranslational protein transport in
    yeast reconstituted with a purified complex of Sec proteins and Kar2p., Panzner
    S, Dreier L, Hartmann E, Kostka S, Rapoport TA. (1995). Its whole native abstract
    and bibliographic identity were read.'
  snapshot_sha256: 5d3a4c056efd6b5dce4ef5427b94e8aba2010137f7b2ef4e892351a8e760baaf
- evidence_id: root54-sources-doi-10.1038_s41586-018-0856-x
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41586-018-0856-x%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI result, exact PMID/DOI/PMCID and complete abstractText
  accessed_at: '2026-10-22T06:18:48.123406Z'
  support: supports
  summary: 'Unique DOI result is MED30644436: Structure of the post-translational
    protein translocation machinery of the ER membrane., Wu X, Cabanos C, Rapoport
    TA. (2019). Its whole native abstract and bibliographic identity were read.'
  snapshot_sha256: 0d392da777a397e1c98795af8a06210c4796d583d547ee94768078f5b6797115
- evidence_id: root54-sources-doi-10.1091_mbc.e03-06-0390
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e03-06-0390%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI result, exact PMID/DOI/PMCID and complete abstractText
  accessed_at: '2026-10-22T06:18:48.176009Z'
  support: supports
  summary: 'Unique DOI result is MED14617809: Interactions between Sec complex and
    prepro-alpha-factor during posttranslational protein transport into the endoplasmic
    reticulum., Plath K, Wilkinson BM, Stirling CJ, Rapoport TA. (2004). Its whole
    native abstract and bibliographic identity were read.'
  snapshot_sha256: ed8f40944e992d188177a7f6d811d377e876e58d156c9002ef82b841d4605045
- evidence_id: root54-sources-primary-PMC6367035
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6367035/
  locator: Wu2019 complete main paragraphs P4-P14; Methods S2 strains,S3 purification,S4
    sample/data acquisition,S6 model building; Figure1, ExtendedDataFigure3/F7 captions
    and FN2 data availability. S5 image processing,S7 mutagenesis,other captions/supplements/pixels
    not read.
  accessed_at: '2026-10-22T06:20:24.976756Z'
  support: supports
  summary: 'The purified endogenous BY4741 complex contained all seven proteins in
    roughly stoichiometric amounts. The4.1A reconstruction supports the subcomplex
    architecture and Sec63-mediated lateral-gate opening. Sec62 density is weak: a
    DEP-like homology model was docked and one TM identified; deposited coordinates
    omit Sec62. This is not a fully resolved atomic model of every subunit.'
  snapshot_sha256: f185e854327ded00cdf767b7f0b4961469c389cfb880d62258b0e2538b07e653
- evidence_id: root54-sources-primary-PMC307522
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC307522/
  locator: Plath2004 complete Methods sec3,sec6,sec7 and Results sec11 including Figures1/2
    captions and Table1. Other sections and pixels not read.
  accessed_at: '2026-10-22T06:20:24.977061Z'
  support: supports
  summary: Purified yeast Sec complexes and ppalphaF crosslinking support simultaneous
    signal-sequence contacts. Single-band measurements combine Sec62/71, but the double-crosslinked
    Sec61-ppalphaF-Sec62 product is specifically immunoprecipitated under denaturing
    conditions with Sec61 and Sec62 antibodies. Thus the record’s bounded Sec62 contact
    statement has support. Kar2-dependent transport intermediates are distinct from
    initial binding without Kar2.
  snapshot_sha256: d9480bd548b046b97ba29f8838759d77ea34b235793cb9a226aed795dad11a5d
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:16:09Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/endoplasmic_reticulum_sec_complex.yaml'
  snapshot_sha256: ac95f8ab1e82a3efaef07ec7637d56c28a9498cbb46e97430a23f5bc32dcb94c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/endoplasmic_reticulum_sec_complex.yaml
    --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/endoplasmic_reticulum_sec_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:16:10Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/endoplasmic_reticulum_sec_complex.yaml\
    \ --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/endoplasmic_reticulum_sec_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch54-20261022-hapbq96w/endoplasmic_reticulum_sec_complex-strict.tsv"
  snapshot_sha256: 7457d8fce88c22bccec32416c74d60a63910a377f70a33a8e7d29d1beef5ada0
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:19:52.871604Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:19:53.301276Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/endoplasmic_reticulum_sec_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  snapshot_sha256: 173c367ec1621e2a96027e149b5cad9f4db0a86f0a3c916455ce192a9aa5f428
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:05:35Z'
  support: supports
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 8696c0d603149cee93ac200eaa3ed26c84320204285cd22cca542eb1ae7ba572
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:37Z'
  support: supports
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  snapshot_sha256: 98a7952c42add0416633f4dee73ff64331e5c6c4c4c8d707e98a152f04fc5b6d
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:59:14Z'
  support: supports
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:40Z'
  support: supports
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  snapshot_sha256: 00cc5664a9143235d28fb9885fc5c43a8a78c9a9c9f47603b1232e1eddddeac1
assessments:
- assessment_id: identity
  area: identity
  topic: Parent assembly and two distinct subcomplexes
  outcome: supported
  target_ids:
  - GO:0031205
  summary: Exact GO identity and declared is_a,part_of and has_part boundaries are
    supported. The Sec61 heterotrimer and yeast Sec62/Sec63 tetramer remain distinct
    subcomplexes within the seven-subunit parent.
  evidence_ids:
  - record
  - root54-sources-go
  - root54-sources-primary-PMC6367035
  - root54-sources-GO0031205-ancestors
  - root54-sources-GO0031205-constraints
  - root54-sources-doi-10.1016_0092-8674-95-90077-2
  - root54-sources-doi-10.1038_s41586-018-0856-x
  - root54-sources-doi-10.1091_mbc.e03-06-0390
- assessment_id: composition
  area: grounding
  topic: Subcomplex representation is intentional and sufficient
  outcome: supported
  target_ids:
  - GO:0031205
  summary: The resolved hierarchy discussion correctly avoids duplicating seven lower-level
    component rows. No absent optional individual-protein inventory is manufactured
    as a completeness finding. Native composition and purified seven-component material
    support this modeling choice.
  evidence_ids:
  - record
  - root54-sources-go
  - root54-sources-primary-PMC6367035
  - curation
- assessment_id: evidence
  area: evidence
  topic: Reconstitution, contact assays and structural resolution
  outcome: supported
  target_ids:
  - GO:0031205
  summary: Panzner1995 complete abstract distinguishes purified seven-protein Sec
    complex from separately added lumenal Kar2 and ATP. Plath supports the named substrate
    contacts, including Sec62-specific denaturing immunoprecipitation. Wu supports
    overall topology while Sec62 has only weak-density docking and one TM; the general
    structural wording does not explicitly claim every residue or subunit was atomically
    resolved.
  evidence_ids:
  - record
  - root54-sources-primary-PMC6367035
  - root54-sources-primary-PMC307522
  - root54-sources-doi-10.1016_0092-8674-95-90077-2
  - root54-sources-doi-10.1038_s41586-018-0856-x
  - root54-sources-doi-10.1091_mbc.e03-06-0390
- assessment_id: graph
  area: graph
  topic: Supported descriptive topology and import function
  outcome: supported
  target_ids:
  - GO:0031205
  summary: The NONMECHANISTIC graph records subcomplex membership, membrane embedding
    and posttranslational import. The record does not turn Kar2 or transient substrates
    into permanent Sec constituents, nor claim a detailed mechanistic reconstruction
    of all translocation stages.
  evidence_ids:
  - record
  - graphs
  - root54-sources-go
  - root54-sources-primary-PMC6367035
  - root54-sources-primary-PMC307522
  - root54-sources-doi-10.1016_0092-8674-95-90077-2
  - root54-sources-doi-10.1038_s41586-018-0856-x
  - root54-sources-doi-10.1091_mbc.e03-06-0390
- assessment_id: scope
  area: scope
  topic: Yeast subcomplex composition and model strains
  outcome: supported
  target_ids:
  - GO:0031205
  summary: The canonical reconstitution and native term scope are yeast-specific.
    Sec71/Sec72 are not generalized to all eukaryotes. Wu uses endogenous BY4741;
    no S288C protein-example rows are invented. COMMON retains its defined qualitative
    meaning and is not a measured strain census.
  evidence_ids:
  - record
  - schema
  - root54-sources-primary-PMC6367035
  - root54-sources-tax4932
  - root54-sources-GO0031205-ancestors
  - root54-sources-GO0031205-constraints
- assessment_id: formation
  area: grounding
  topic: Assembly observations do not imply all absence outcomes
  outcome: unknown
  target_ids:
  - GO:0031205
  summary: Co-purification and resolved contacts support architecture but do not automatically
    establish component-removal consequences. The target makes no categorical individual-protein
    essentiality claim, and no such universal assertion is added.
  evidence_ids:
  - record
  - schema
  - root54-sources-primary-PMC6367035
  - root54-sources-primary-PMC307522
- assessment_id: coverage
  area: completeness
  topic: Whole maintained target and bounded follow-up
  outcome: supported
  target_ids:
  - GO:0031205
  summary: Every maintained field, evidence row, component/example, graph edge, discussion
    and history entry was read. Required defects are distinguished from optional enrichment
    and unavailable source detail. Scientific status/history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root54-sources-go
  - root54-sources-doi-10.1016_0092-8674-95-90077-2
  - root54-sources-doi-10.1038_s41586-018-0856-x
  - root54-sources-doi-10.1091_mbc.e03-06-0390
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw datasets, atomic coordinates, sequence alignments or supplemental
  data files were reanalyzed. Primary reading is limited to the exact sections declared
  in individual evidence rows.
- Panzner1995 was read at complete native abstract tier; the verified publisher route
  returned403. Wu and Plath body inspection is restricted to the enumerated sections.
  The Sec62 weak-density/homology-model limitation remains material despite support
  for overall subcomplex topology.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations and issue-bearing reviews
  alike.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
