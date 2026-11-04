# Groel groes complex scientific review

- Review: 20261022T072030Z-groel-groes-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:59:52Z
- Finished UTC: 2026-10-22T07:20:30Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

GroEL/GroES identity, exact protein families, asymmetric14+7 architecture and coarse capping/remodeling graph are supported. No actionable issue was established within the explicit native-abstract/deposition and body-access limits.

## Scope And Provenance

Exactly one whole maintained target plus frozen guidance and protein-example skill. Source-read extents are enumerated per evidence row; no maintained neighboring record supplies biological evidence.

Selection: Target 9 of batch56, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990220 | data/structures/other/groel_groes_complex.yaml | maintained | GroEL-GroES complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990220 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990220 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:1990220 | Native focused check passed; scientific claims assessed separately. |
| Native verify | passed | True | GO:1990220 | Native focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:1990220 | No expression-module inference is used. |
| Claim-level scientific review | passed | True | GO:1990220 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990220 | 10 of 12 collected target identifiers returned OK. PDB:1AON: SKIPPED; Exact RCSB entry identifier, structure title and primary citation DOI/PMID independently read. Deposition-specific composition, ligands and structural interpretation retain the separately reviewed evidence scopes; the paper title does not substitute for entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:9285585: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990220 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990220 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990220 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990220 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990220 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Asymmetric GroEL/GroES complex and correct protein examples

identity: supported. Targets: GO:1990220.

Native GO/parent/synonyms agree. Reviewed K12 proteins and current full-family groundings are appropriate. The PDB species-level source and protein strain metadata remain separate.

### Explicit14+7 asymmetric context

grounding: supported. Targets: GO:1990220.

Both component counts explicitly say asymmetric, and the21-subunit property/canonical example are tied to1AON. Native assembly/entity counts independently support this context. Other symmetric states in the protein annotations do not contradict the scoped claim.

### Cap binding and chamber remodeling

graph: supported. Targets: GO:1990220.

The complete Xu native abstract describes GroES/ADP-associated domain movements, doubled cis-cavity volume and a hydrophilic lining; native protein annotations and deposition support capping. The maintained MECHANISTIC graph captures these coarse causal steps without claiming that an uninspected full catalytic cycle was reconstructed.

### Folding activity is not an inferred formation requirement

grounding: unknown. Targets: GO:1990220.

The record does not assign blanket ESSENTIAL fields. ATP-dependent folding and observed bound architecture do not alone establish experimental formation necessity for every constituent.

### Complete maintained target and bounded evidence coverage

completeness: supported. Targets: GO:1990220.

Every maintained field, evidence note, graph statement and discussion was inspected at the declared source extents. Optional inventories and unmeasured formation requirements are not invented from native validation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/groel_groes_complex.yaml; Entire maintained record, including all evidence, examples, graphs, history and discussions | context_only | The entire maintained target was read. Dated curation history is not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, essentiality, PresenceEnum and graph-scope contracts | context_only | Formation necessity differs from activity or viability. COMMON means present in most members, with losses the exception; VARIABLE means patchy lineage- or strain-level presence. Neither enum is redefined as merely observed occurrence. |
| curation | docs/CURATION.md; Component grounding, including REVIEWED_LABEL_ONLY at159–160 | context_only | A verified exact full-protein family is distinct from a shared domain or a broader class. Label-only does not mean simply that an available exact mapping was not curated this pass. |
| complex56-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030700,GO:1990204,GO:0030699,GO:0042765,GO:0032991,GO:0005789,GO:0016255,GO:1990220,GO:0016465,GO:0006457,GO:1990131,GO:0038202,GO:0000329,GO:0071986,GO:1990130,GO:0061700; Complete target-relevant definitions/synonyms and typed relationships in combined response; no unrelated child or definition attributed to this target | supports | GO1990220 identifies the bacterial GroEL-GroES complex with tetradecameric GroEL and heptameric GroES, with related bacterial-chaperonin synonyms. GO0016465 and0006457 identify the maintained parent and folding process. |
| complex56-agent-GO1990220-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990220/ancestors?relations=is_a; Complete is_a-only ancestor response | supports | The is_a-only ancestor response contains the maintained parent class. It does not establish parthood or taxonomic frequency. |
| complex56-agent-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete ENA taxonomy identity, names and lineage | supports | Taxon562 is Escherichia coli, rank species; the native names and lineage identify this exact organism. |
| complex56-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete ENA taxonomy identity, names and lineage | supports | Taxon83333 is Escherichia coli K-12, rank strain; the native names and lineage identify this exact organism. |
| complex56-agent-protein-P0A6F5 | https://rest.uniprot.org/uniprotkb/P0A6F5.json; Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P0A6F5, Chaperonin GroEL; primary genes groEL, synonyms groL, mopA, taxon83333. Native annotation evidence distinguishes measured and inferred claims. This protein response independently supplies its own family cross-references. |
| complex56-agent-protein-P0A6F9 | https://rest.uniprot.org/uniprotkb/P0A6F9.json; Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P0A6F9, Co-chaperonin GroES; primary genes groES, synonyms groS, mopB, taxon83333. Native annotation evidence distinguishes measured and inferred claims. This protein response independently supplies its own family cross-references. |
| complex56-agent-pmid-9285585 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9285585+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete MED identity and available abstract | supports | MED9285585: The crystal structure of the asymmetric GroEL-GroES-(ADP)7 chaperonin complex. Xu Z, Horwich AL, Sigler PB. (1997), DOI10.1038/41944. Exact metadata and the entire available native abstract read; primary-body access is not implied. |
| complex56-agent-ipr-IPR001844 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001844/; Native family name/type, descriptions/curation flags and signatures; protein membership is supplied independently by UniProt | supports | IPR001844 identifies the full chaperonin Cpn60/GroEL family, distinguished from the broader Cpn60/GroEL/TCP-1 parent. |
| complex56-agent-ipr-IPR020818 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020818/; Native family name/type, descriptions/curation flags and signatures; protein membership is supplied independently by UniProt | supports | IPR020818 identifies the full GroES chaperonin family. |
| complex56-agent-pdb-entry-1AON | https://data.rcsb.org/rest/v1/core/entry/1AON; Primary citation, experimental method/resolution and entity metadata | supports | PDB1AON records the asymmetric GroEL-GroES-(ADP)7 structure, Xu/Horwich/Sigler1997 DOI10.1038/41944, at3.0angstrom; two protein entities are distinguished from ADP and magnesium. |
| complex56-agent-pdb-polymer_entity-1AON-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/1AON/1; Complete entity identity/source-organism/chain and sequence-mapping metadata | supports | Protein entity1 is GroEL, with14 deposited chain instances A–N, source Escherichia coli taxon562 and SIFTS mapping to P0A6F5. |
| complex56-agent-pdb-polymer_entity-1AON-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/1AON/2; Complete entity identity/source-organism/chain and sequence-mapping metadata | supports | Protein entity2 is GroES, with7 chain instances O–U, source Escherichia coli taxon562 and SIFTS mapping to P0A6F9. |
| complex56-agent-pdb-assembly-1AON-1 | https://data.rcsb.org/rest/v1/core/assembly/1AON/1; Complete biological assembly counts and generation metadata | supports | Assembly1 contains21 protein instances from two protein entities. This supports the specified asymmetric14+7 state; it is not a claim that all GroEL/GroES states have that stoichiometry. |
| schema-result | just validate data/structures/other/groel_groes_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/groel_groes_complex.yaml |
| strict-result | just validate-strict data/structures/other/groel_groes_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/groel_groes_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/groel_groes_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/groel_groes_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/groel_groes_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/groel_groes_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/groel_groes_complex.yaml  (GO:1990220)<br>  groel_groes_folding_cycle	groes_cochaperonin	COVERED	-&gt;groes_cochaperonin (UniProtKB:P0A6F9)<br>  groel_groes_folding_cycle	groel_chaperonin	COVERED	-&gt;groel_chaperonin (UniProtKB:P0A6F5)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/groel_groes_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/groel_groes_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 12 collected target identifiers returned OK. PDB:1AON: SKIPPED; Exact RCSB entry identifier, structure title and primary citation DOI/PMID independently read. Deposition-specific composition, ligands and structural interpretation retain the separately reviewed evidence scopes; the paper title does not substitute for entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:9285585: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five completed same-base batch26 global gates are integrated with exact manifest/input/log hashes verified. The sparse B56 checkout was not used to claim a new full-site QC run.
- No supplements or atomic coordinates were independently analyzed. Actual source reading is limited to the exact locators below.
- Xu1997 publisher HTML and PDF routes both returned200 ClientChallengeHTML, not the paper body. Formal paper support is its complete native abstract plus the independently inspected primary PDB deposition and native annotations.
- No coordinates, structure pixels or supplementary data were analyzed. The scoped14+7 state is retained without certifying a universal stoichiometry or every proposed step of the folding cycle.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T072030Z-groel-groes-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Groel groes complex scientific review
started_at: '2026-10-22T06:59:52Z'
finished_at: '2026-10-22T07:20:30Z'
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
summary: GroEL/GroES identity, exact protein families, asymmetric14+7 architecture
  and coarse capping/remodeling graph are supported. No actionable issue was established
  within the explicit native-abstract/deposition and body-access limits.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/other/groel_groes_complex.yaml
    sha256: 5bd7ae78b674326f62d256614b83b15d516633140537514a676383e169999ce1
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
- target_id: GO:1990220
  path: data/structures/other/groel_groes_complex.yaml
  label: GroEL-GroES complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/groel_groes_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one whole maintained target plus frozen guidance and protein-example
    skill. Source-read extents are enumerated per evidence row; no maintained neighboring
    record supplies biological evidence.
  selection: Target 9 of batch56, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990220
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990220
  command: just validate data/structures/other/groel_groes_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990220
  command: just validate-strict data/structures/other/groel_groes_complex.yaml --out
    /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/groel_groes_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990220
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/groel_groes_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:1990220
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/groel_groes_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990220
  summary: No expression-module inference is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990220
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex56-agent-go
  - complex56-agent-GO1990220-ancestors
  - complex56-agent-tax-562
  - complex56-agent-tax-83333
  - complex56-agent-protein-P0A6F5
  - complex56-agent-protein-P0A6F9
  - complex56-agent-pmid-9285585
  - complex56-agent-ipr-IPR001844
  - complex56-agent-ipr-IPR020818
  - complex56-agent-pdb-entry-1AON
  - complex56-agent-pdb-polymer_entity-1AON-1
  - complex56-agent-pdb-polymer_entity-1AON-2
  - complex56-agent-pdb-assembly-1AON-1
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990220
  summary: '10 of 12 collected target identifiers returned OK. PDB:1AON: SKIPPED;
    Exact RCSB entry identifier, structure title and primary citation DOI/PMID independently
    read. Deposition-specific composition, ligands and structural interpretation retain
    the separately reviewed evidence scopes; the paper title does not substitute for
    entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:9285585:
    UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read
    following the bulk eutils414 transport failure. Resolution is identifier identity
    only; separate primary-body/abstract evidence limits remain in force. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.'
  evidence_ids:
  - target-curies
  - complex56-agent-pdb-entry-1AON
  - complex56-agent-pmid-9285585
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990220
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990220
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990220
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990220
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990220
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
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/groel_groes_complex.yaml
  locator: Entire maintained record, including all evidence, examples, graphs, history
    and discussions
  accessed_at: '2026-10-22T07:11:15Z'
  support: context_only
  summary: The entire maintained target was read. Dated curation history is not independent
    biological evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, essentiality, PresenceEnum and graph-scope
    contracts
  accessed_at: '2026-10-22T07:11:15Z'
  support: context_only
  summary: Formation necessity differs from activity or viability. COMMON means present
    in most members, with losses the exception; VARIABLE means patchy lineage- or
    strain-level presence. Neither enum is redefined as merely observed occurrence.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding, including REVIEWED_LABEL_ONLY at159–160
  accessed_at: '2026-10-22T07:11:15Z'
  support: context_only
  summary: A verified exact full-protein family is distinct from a shared domain or
    a broader class. Label-only does not mean simply that an available exact mapping
    was not curated this pass.
- evidence_id: complex56-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030700,GO:1990204,GO:0030699,GO:0042765,GO:0032991,GO:0005789,GO:0016255,GO:1990220,GO:0016465,GO:0006457,GO:1990131,GO:0038202,GO:0000329,GO:0071986,GO:1990130,GO:0061700
  locator: Complete target-relevant definitions/synonyms and typed relationships in
    combined response; no unrelated child or definition attributed to this target
  accessed_at: '2026-10-22T06:56:23.574147Z'
  support: supports
  summary: GO1990220 identifies the bacterial GroEL-GroES complex with tetradecameric
    GroEL and heptameric GroES, with related bacterial-chaperonin synonyms. GO0016465
    and0006457 identify the maintained parent and folding process.
  snapshot_sha256: 47442ac474d759525b8a001d355e3e4db9a53b9c5c0389770a0b1f4a3bd9cd6c
- evidence_id: complex56-agent-GO1990220-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990220/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response
  accessed_at: '2026-10-22T07:04:03.646993Z'
  support: supports
  summary: The is_a-only ancestor response contains the maintained parent class. It
    does not establish parthood or taxonomic frequency.
  snapshot_sha256: df3a0948f6b7b1fe9bc2f50706c54caf4859de989f24bb21dc7ce7985c5d5fbd
- evidence_id: complex56-agent-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete ENA taxonomy identity, names and lineage
  accessed_at: '2026-10-22T06:56:31.805068Z'
  support: supports
  summary: Taxon562 is Escherichia coli, rank species; the native names and lineage
    identify this exact organism.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: complex56-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete ENA taxonomy identity, names and lineage
  accessed_at: '2026-10-22T06:56:31.661890Z'
  support: supports
  summary: Taxon83333 is Escherichia coli K-12, rank strain; the native names and
    lineage identify this exact organism.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: complex56-agent-protein-P0A6F5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A6F5.json
  locator: Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references
  accessed_at: '2026-10-22T06:56:25.702111Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P0A6F5, Chaperonin GroEL; primary genes
    groEL, synonyms groL, mopA, taxon83333. Native annotation evidence distinguishes
    measured and inferred claims. This protein response independently supplies its
    own family cross-references.'
  snapshot_sha256: 527364f6a4ba7e422217e81a9d76f2882c106655ceaedfa8d9dad0e8ad56e908
- evidence_id: complex56-agent-protein-P0A6F9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A6F9.json
  locator: Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references
  accessed_at: '2026-10-22T06:56:25.852150Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P0A6F9, Co-chaperonin GroES; primary
    genes groES, synonyms groS, mopB, taxon83333. Native annotation evidence distinguishes
    measured and inferred claims. This protein response independently supplies its
    own family cross-references.'
  snapshot_sha256: 0c39f86a7fcaf57624b9d5171cc0879a35ec6ee2adb6e12b740570c411df6a8b
- evidence_id: complex56-agent-pmid-9285585
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9285585+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete MED identity and available abstract
  accessed_at: '2026-10-22T06:56:28.780600Z'
  support: supports
  summary: 'MED9285585: The crystal structure of the asymmetric GroEL-GroES-(ADP)7
    chaperonin complex. Xu Z, Horwich AL, Sigler PB. (1997), DOI10.1038/41944. Exact
    metadata and the entire available native abstract read; primary-body access is
    not implied.'
  snapshot_sha256: 838ce05fa45ca2ea0bf9113efa08b367d258295c9b3d2df482924d2a575580d9
- evidence_id: complex56-agent-ipr-IPR001844
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001844/
  locator: Native family name/type, descriptions/curation flags and signatures; protein
    membership is supplied independently by UniProt
  accessed_at: '2026-10-22T06:56:27.462565Z'
  support: supports
  summary: IPR001844 identifies the full chaperonin Cpn60/GroEL family, distinguished
    from the broader Cpn60/GroEL/TCP-1 parent.
  snapshot_sha256: 0839e982cc89bb8b2ddb26cbe4472f1d338d4a2c74cd736cebe5248ee6307727
- evidence_id: complex56-agent-ipr-IPR020818
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020818/
  locator: Native family name/type, descriptions/curation flags and signatures; protein
    membership is supplied independently by UniProt
  accessed_at: '2026-10-22T06:56:27.527932Z'
  support: supports
  summary: IPR020818 identifies the full GroES chaperonin family.
  snapshot_sha256: 42353b1fc26e570431c5612d364c25a5804960b040d2051c89a9007e2fdf564d
- evidence_id: complex56-agent-pdb-entry-1AON
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1AON
  locator: Primary citation, experimental method/resolution and entity metadata
  accessed_at: '2026-10-22T06:56:32.126261Z'
  support: supports
  summary: PDB1AON records the asymmetric GroEL-GroES-(ADP)7 structure, Xu/Horwich/Sigler1997
    DOI10.1038/41944, at3.0angstrom; two protein entities are distinguished from ADP
    and magnesium.
  snapshot_sha256: 768d1f52c7b0e46862648f588428d9a581de7cad98143389b0802c55e3aa7a1e
- evidence_id: complex56-agent-pdb-polymer_entity-1AON-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1AON/1
  locator: Complete entity identity/source-organism/chain and sequence-mapping metadata
  accessed_at: '2026-10-22T06:56:32.235783Z'
  support: supports
  summary: Protein entity1 is GroEL, with14 deposited chain instances A–N, source
    Escherichia coli taxon562 and SIFTS mapping to P0A6F5.
  snapshot_sha256: 31b1d105618736962709f4a92e0fc06ae548d27b39f433ebc9b0353d12f98965
- evidence_id: complex56-agent-pdb-polymer_entity-1AON-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1AON/2
  locator: Complete entity identity/source-organism/chain and sequence-mapping metadata
  accessed_at: '2026-10-22T06:56:32.274481Z'
  support: supports
  summary: Protein entity2 is GroES, with7 chain instances O–U, source Escherichia
    coli taxon562 and SIFTS mapping to P0A6F9.
  snapshot_sha256: 751ea41d7fdf57f39719c7f43466d9dea5a6d2e4bc0dbf603d530fc9e9586f5e
- evidence_id: complex56-agent-pdb-assembly-1AON-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/1AON/1
  locator: Complete biological assembly counts and generation metadata
  accessed_at: '2026-10-22T06:56:32.314769Z'
  support: supports
  summary: Assembly1 contains21 protein instances from two protein entities. This
    supports the specified asymmetric14+7 state; it is not a claim that all GroEL/GroES
    states have that stoichiometry.
  snapshot_sha256: d3d2166c8dca965a42ce37c0bf230253e21f9f14cf2f043f1a6649509abe88ae
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/groel_groes_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:54Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/groel_groes_complex.yaml'
  snapshot_sha256: e38a6d9e38befd5694bef21737da09e40414e6eda691240853e3cc2e906194c0
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/groel_groes_complex.yaml --out
    /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/groel_groes_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:55Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/groel_groes_complex.yaml\
    \ --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/groel_groes_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/groel_groes_complex-strict.tsv"
  snapshot_sha256: 75fe8e9d698f16cdac39056c9522311152cf8d4f2ce394319169f59a41f60013
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/groel_groes_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T07:03:40.547444Z'
  support: supports
  summary: "data/structures/other/groel_groes_complex.yaml  (GO:1990220)\n  groel_groes_folding_cycle\t\
    groes_cochaperonin\tCOVERED\t->groes_cochaperonin (UniProtKB:P0A6F9)\n  groel_groes_folding_cycle\t\
    groel_chaperonin\tCOVERED\t->groel_chaperonin (UniProtKB:P0A6F5)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 698d601827ffdc8ddac895e5d75a41d400cfe8d169add39046e065df4273bdbf
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/groel_groes_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T07:03:41.968101Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/groel_groes_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 12 collected target identifiers returned OK. PDB:1AON: SKIPPED;
    Exact RCSB entry identifier, structure title and primary citation DOI/PMID independently
    read. Deposition-specific composition, ligands and structural interpretation retain
    the separately reviewed evidence scopes; the paper title does not substitute for
    entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:9285585:
    UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read
    following the bulk eutils414 transport failure. Resolution is identifier identity
    only; separate primary-body/abstract evidence limits remain in force. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.'
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
  topic: Asymmetric GroEL/GroES complex and correct protein examples
  outcome: supported
  target_ids:
  - GO:1990220
  summary: Native GO/parent/synonyms agree. Reviewed K12 proteins and current full-family
    groundings are appropriate. The PDB species-level source and protein strain metadata
    remain separate.
  evidence_ids:
  - record
  - complex56-agent-go
  - complex56-agent-GO1990220-ancestors
  - complex56-agent-pdb-entry-1AON
  - complex56-agent-pdb-polymer_entity-1AON-1
  - complex56-agent-pdb-polymer_entity-1AON-2
  - complex56-agent-protein-P0A6F5
  - complex56-agent-protein-P0A6F9
  - complex56-agent-ipr-IPR001844
  - complex56-agent-ipr-IPR020818
  - complex56-agent-tax-562
  - complex56-agent-tax-83333
- assessment_id: stoichiometry
  area: grounding
  topic: Explicit14+7 asymmetric context
  outcome: supported
  target_ids:
  - GO:1990220
  summary: Both component counts explicitly say asymmetric, and the21-subunit property/canonical
    example are tied to1AON. Native assembly/entity counts independently support this
    context. Other symmetric states in the protein annotations do not contradict the
    scoped claim.
  evidence_ids:
  - record
  - complex56-agent-pdb-entry-1AON
  - complex56-agent-pdb-polymer_entity-1AON-1
  - complex56-agent-pdb-polymer_entity-1AON-2
  - complex56-agent-pdb-assembly-1AON-1
  - complex56-agent-protein-P0A6F5
  - complex56-agent-protein-P0A6F9
- assessment_id: graph
  area: graph
  topic: Cap binding and chamber remodeling
  outcome: supported
  target_ids:
  - GO:1990220
  summary: The complete Xu native abstract describes GroES/ADP-associated domain movements,
    doubled cis-cavity volume and a hydrophilic lining; native protein annotations
    and deposition support capping. The maintained MECHANISTIC graph captures these
    coarse causal steps without claiming that an uninspected full catalytic cycle
    was reconstructed.
  evidence_ids:
  - record
  - complex56-agent-go
  - complex56-agent-pmid-9285585
  - complex56-agent-pdb-entry-1AON
  - complex56-agent-protein-P0A6F5
  - complex56-agent-protein-P0A6F9
- assessment_id: formation
  area: grounding
  topic: Folding activity is not an inferred formation requirement
  outcome: unknown
  target_ids:
  - GO:1990220
  summary: The record does not assign blanket ESSENTIAL fields. ATP-dependent folding
    and observed bound architecture do not alone establish experimental formation
    necessity for every constituent.
  evidence_ids:
  - record
  - schema
  - complex56-agent-pmid-9285585
  - complex56-agent-pdb-entry-1AON
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target and bounded evidence coverage
  outcome: supported
  target_ids:
  - GO:1990220
  summary: Every maintained field, evidence note, graph statement and discussion was
    inspected at the declared source extents. Optional inventories and unmeasured
    formation requirements are not invented from native validation.
  evidence_ids:
  - record
  - schema
  - curation
  - complex56-agent-go
findings: []
actions: []
limitations:
- All five completed same-base batch26 global gates are integrated with exact manifest/input/log
  hashes verified. The sparse B56 checkout was not used to claim a new full-site QC
  run.
- No supplements or atomic coordinates were independently analyzed. Actual source
  reading is limited to the exact locators below.
- Xu1997 publisher HTML and PDF routes both returned200 ClientChallengeHTML, not the
  paper body. Formal paper support is its complete native abstract plus the independently
  inspected primary PDB deposition and native annotations.
- No coordinates, structure pixels or supplementary data were analyzed. The scoped14+7
  state is retained without certifying a universal stoichiometry or every proposed
  step of the folding cycle.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
