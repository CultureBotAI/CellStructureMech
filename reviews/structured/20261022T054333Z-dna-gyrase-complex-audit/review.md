# Dna gyrase complex scientific review

- Review: 20261022T054333Z-dna-gyrase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:31:27Z
- Finished UTC: 2026-10-22T05:43:33Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Gyrase identity, exact protein families, K12 examples and2:2 composition are supported. One minor corrects the canonical deposition scope:6RKU is a cleavage-domain model;6RKW is the overall model.

## Scope And Provenance

Exactly one complete maintained record and the native/primary source passages identified in each locator; no scientific record changed.

Selection: Target 8 of batch50, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0120217 | data/structures/other/dna_gyrase_complex.yaml | maintained | DNA gyrase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0120217 | Focused validator passed. |
| Focused native strict | passed | True | GO:0120217 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0120217 | Native read-only focused check passed; scientific support assessed separately. |
| Native verify | passed | True | GO:0120217 | Native read-only focused check passed; scientific support assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0120217 | No expression-module or transcriptomic claim requires this resource. |
| Claim-level scientific review | passed | True | GO:0120217 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0120217 | 10 of 12 collected target identifiers returned OK. PDB:6RKU: SKIPPED; Exact native RCSB6RKU deposition identity and primary citation inspected. Its domain-focused model scope remains a scientific finding; identifier resolution does not endorse the overbroad canonical description.; PMID:31666516: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0120217 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0120217 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0120217 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0120217 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0120217 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Gyrase complex and broader topoisomerase class

identity: supported. Targets: GO:0120217.

Native GO identity and is-a parent agree. The record describes the usual bacterial GyrA2B2 class, distinct from the broader typeIIA family; no unrelated topoisomerase synonym is imported.

### Exact families, examples and2:2 protein composition

grounding: supported. Targets: GO:0120217.

Both full-protein families, reviewed K12 examples and current single-hit notes are correct. RCSB entities and primary reconstitution support two copies of each subunit. DNA and inhibitor in a trapped experimental assembly are not missing permanent protein-component rows.

### Source strain and exact deposited model

scope: concern. Targets: GO:0120217.

K12 source taxon is verified separately from BL21(DE3) expression host. The canonical note overstates6RKU as the complete model: both native title and primary Sec17 identify it as the cleavage-domain State1 model, while6RKW is the overall architecture. Valid6RKU entity/stoichiometry links can remain.

### Coarse topology function with experimental separation

graph: supported. Targets: GO:0120217.

GO and primary supercoiling/ATPase assay descriptions support the coarse NONMECHANISTIC graph. The drug/AMP-PNP-trapped EM structure alone is not an active turnover assay; the paper separately tests activity. The record does not claim a fully resolved strand-passage cycle or uniformly equal activity across species.

### No inferred assembly-necessity values

grounding: unknown. Targets: GO:0120217.

No essentiality field is supplied in these component rows. The inspected reconstitution and structural membership are not used to invent an optional field or a universal deletion-based formation requirement.

### Entire maintained target audited

completeness: supported. Targets: GO:0120217.

All maintained fields, discussions and historical entries were read. Source identity, experimental scope, molecular class and graph roles were checked separately; no optional inventory or uninspected mechanism was invented.

## Findings

### F1: Distinguish the cleavage-domain and overall gyrase depositions

minor / open / confirmed; issue key: gyrase-deposition-scope.

The canonical example calls PDB6RKU the complete GyrA2-GyrB2 cryo-EM assembly. Its native title and primary Methods Sec17 identify6RKU as the closed DNA-binding/cleavage-domain model and6RKW as the overall model. The two correct protein entity mappings and2:2 stoichiometry are unaffected.

## Recommended Actions And Acceptance Checks

### A1

Qualify6RKU as the domain-focused State1 deposition, or use the verified6RKW entry for an explicitly overall-model canonical example; retain6RKU where its GyrA/B entity mapping is the relevant evidence.

- Keep K12 source distinct from BL21(DE3) expression.
- Do not describe full sample sequences as proof of complete atomic coverage.
- Preserve supported identifiers, examples and biological scope; pass applicable native validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dna_gyrase_complex.yaml; Entire target, including all components/examples, graph, evidence, discussions and history | context_only | The full maintained record was read. Historical curation notes are not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, EssentialityEnum and NONMECHANISTIC graph scope | context_only | Family identity is separate from a taxon-specific example. Assembly necessity differs from composition, catalytic requirement and viability. |
| curation | docs/CURATION.md; Exact family mapping and REVIEWED_LABEL_ONLY contract, especially159–160 | context_only | Reviewed label-only status requires an unresolved exact mapping, rather than simply deferring a verified available family. |
| replication50-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003918,GO:0006260,GO:0009330,GO:0009360,GO:0032991,GO:0034335,GO:0043846,GO:0043847,GO:0044775,GO:0044776,GO:0120217; Relevant complete identity/definition/active-status/synonyms and typed parent child links in the11-term native response; no unrelated descendants promoted | supports | GO0120217 matches the gyrase identity and GO0009330 has it as an is-a child. GO0034335 and GO0003918 define negative supercoiling and ATP-dependent typeII topology; the former explicitly warns that supercoiling ability is not uniform across bacterial gyrases. |
| replication50-agent-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxon response | supports | ENA taxon83333 is Escherichia coli K-12, rank strain; exact names, synonyms and available lineage read. |
| replication50-agent-protein-P0AES4 | https://rest.uniprot.org/uniprotkb/P0AES4.json; Accession/status/protein name/genes/organism, function/subunit/similarity comments and InterPro xrefs | supports | Reviewed P0AES4 is the declared gyrA protein in E.coli K12 taxon83333. Native function/subunit/similarity annotations and InterPro links support the identity; underlying experiments are certified only where separately read. |
| replication50-agent-gene-gyrA-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgyrA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; All returned identities/aliases in gene_exact AND taxonomy_id:83333 AND reviewed:true, size500 | supports | The complete current reviewed exact-gene query for gyrA and taxonomy83333 returns one entry, P0AES4, with matching gene and organism. |
| replication50-agent-protein-P0AES6 | https://rest.uniprot.org/uniprotkb/P0AES6.json; Accession/status/protein name/genes/organism, function/subunit/similarity comments and InterPro xrefs | supports | Reviewed P0AES6 is the declared gyrB protein in E.coli K12 taxon83333. Native function/subunit/similarity annotations and InterPro links support the identity; underlying experiments are certified only where separately read. |
| replication50-agent-gene-gyrB-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgyrB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; All returned identities/aliases in gene_exact AND taxonomy_id:83333 AND reviewed:true, size500 | supports | The complete current reviewed exact-gene query for gyrB and taxonomy83333 returns one entry, P0AES6, with matching gene and organism. |
| replication50-agent-pmid-31666516 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A31666516+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and entire native abstract | supports | Native MED31666516: Cryo-EM structure of the complete E. coli DNA gyrase nucleoprotein complex. Authors Vanden Broeck A, Lotz C, Ortiz J, Lamour V.; DOI 10.1038/s41467-019-12914-y. Complete abstract read at primary-study abstract tier; metadata is not a claim of full-body access. |
| replication50-agent-gyrase2019-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6821735/; Genuine PMC6821735 Introduction Sec1; Results Sec3/Sec4 and Fig1–3 captions; entire Discussion Sec8; Methods Sec10–13, Sec17, Sec20–21; Data availability notes2. Text/captions only, no supplement or pixels. | supports | Primary reconstruction establishes full GyrA2B2 architecture, with independently assayed supercoiling/ATPase activity. Cryo-EM uses gepotidacin and AMP-PNP; BL21(DE3)pRARE2 is the expression host. Sec17 assigns the closed DNA-binding/cleavage-domain model to6RKU and the overall model to6RKW. |
| replication50-agent-pdb6rku-entry | https://data.rcsb.org/rest/v1/core/entry/6RKU; Native title, primary citation and experimental/model counts | supports | 6RKU is titled E.coli DNA gyrase DNA-binding and cleavage domain in State1, at4.0A. Its exact primary citation is Vanden Broeck2019/PMID31666516/DOI10.1038/s41467-019-12914-y; the deposition is not the overall full-architecture model. |
| replication50-agent-pdb6rku-assembly | https://data.rcsb.org/rest/v1/core/assembly/6RKU/1; Assembly1 composition, polymer counts, asym_id list and modeled/unmodeled monomer counts | supports | Assembly1 has four protein instances and four DNA instances: the eight-polymer count is not eight protein subunits. Two GyrA and two GyrB entity mappings remain correct, despite incomplete modeled domain coverage. |
| replication50-agent-pdb6rku-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/6RKU/1; Native entity identity, SIFTS accession, molecule count, source organism and host organism | supports | Polymer entity1 is GyrA, mapped to P0AES4, with two listed chains, source taxon83333 and distinct expression host BL21(DE3)469008. Full sample sequence mapping does not imply all residues are modeled. |
| replication50-agent-pdb6rku-entity2 | https://data.rcsb.org/rest/v1/core/polymer_entity/6RKU/2; Native entity identity, SIFTS accession, molecule count, source organism and host organism | supports | Polymer entity2 is GyrB, mapped to P0AES6, with two listed chains, source taxon83333 and distinct expression host BL21(DE3)469008. Full sample sequence mapping does not imply all residues are modeled. |
| replication50-agent-pdb6rkw-entry | https://data.rcsb.org/rest/v1/core/entry/6RKW; Native title, primary citation and experimental metadata | supports | 6RKW is the complete E.coli DNA gyrase structure, with the same primary citation; this is the overall model named in primary Methods Sec17. |
| replication50-agent-pdb6rkw-assembly | https://data.rcsb.org/rest/v1/core/assembly/6RKW/1; Native biological assembly composition and polymer-instance counts | supports | 6RKW assembly1 retains the GyrA2B2 protein/NA architecture. The distinct entry provides the overall-model candidate; no coordinate-level reanalysis is claimed. |
| replication50-agent-ipr-IPR005743 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005743/; Native name/type, complete description, hierarchy/signatures and curation flags | supports | IPR005743 is the exact DNA gyrase A full-protein family, with GyrA-specific HAMAPMF01897 and native EC5.6.2.2 cross-reference. Its broader background paragraphs are not treated as definitions of every topoisomerase. |
| replication50-agent-ipr-IPR011557 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011557/; Native name/type, complete description, hierarchy/signatures and curation flags | supports | IPR011557 is the exact DNA gyrase B full-protein family, with HAMAPMF01898/NCBIfamTIGR01059 and EC5.6.2.2. |
| schema-result | just validate data/structures/other/dna_gyrase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dna_gyrase_complex.yaml |
| strict-result | just validate-strict data/structures/other/dna_gyrase_complex.yaml --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dna_gyrase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dna_gyrase_complex.yaml --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dna_gyrase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dna_gyrase_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dna_gyrase_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/dna_gyrase_complex.yaml  (GO:0120217)<br>  dna_gyrase_negative_supercoiling	gyrase_subunit_a	COVERED	-&gt;gyrase_subunit_a (UniProtKB:P0AES4)<br>  dna_gyrase_negative_supercoiling	gyrase_subunit_b	COVERED	-&gt;gyrase_subunit_b (UniProtKB:P0AES6)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dna_gyrase_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dna_gyrase_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 12 collected target identifiers returned OK. PDB:6RKU: SKIPPED; Exact native RCSB6RKU deposition identity and primary citation inspected. Its domain-focused model scope remains a scientific finding; identifier resolution does not endorse the overbroad canonical description.; PMID:31666516: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, supplementary experimental data, sequence alignments or coordinate geometry were independently reanalyzed. Exact text and native metadata scopes are identified per evidence row.
- The full-length enzyme was imaged under trapping conditions and modeled at several resolutions. No claim is made that6RKW resolves every residue, or that6RKU itself represents active ATP hydrolysis.
- GO0034335 explicitly cautions against uniform supercoiling generalization across all bacterial gyrases; the concrete experimental example here is E.coli.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes qualified clean reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T054333Z-dna-gyrase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Dna gyrase complex scientific review
started_at: '2026-10-22T05:31:27Z'
finished_at: '2026-10-22T05:43:33Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Gyrase identity, exact protein families, K12 examples and2:2 composition
  are supported. One minor corrects the canonical deposition scope:6RKU is a cleavage-domain
  model;6RKW is the overall model.
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
  - path: data/structures/other/dna_gyrase_complex.yaml
    sha256: 5f4e9e6f29de383572bdbea4aabb06fd250a5faeedd5facf716a7d57c860a263
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
- target_id: GO:0120217
  path: data/structures/other/dna_gyrase_complex.yaml
  label: DNA gyrase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_gyrase_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained record and the native/primary source
    passages identified in each locator; no scientific record changed.
  selection: Target 8 of batch50, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0120217
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: just validate data/structures/other/dna_gyrase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: just validate-strict data/structures/other/dna_gyrase_complex.yaml --out
    /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dna_gyrase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_gyrase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native read-only focused check passed; scientific support assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_gyrase_complex.yaml
    --verify
  exit_code: 0
  summary: Native read-only focused check passed; scientific support assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0120217
  summary: No expression-module or transcriptomic claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0120217
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - replication50-agent-go
  - replication50-agent-tax83333
  - replication50-agent-protein-P0AES4
  - replication50-agent-gene-gyrA-83333
  - replication50-agent-protein-P0AES6
  - replication50-agent-gene-gyrB-83333
  - replication50-agent-pmid-31666516
  - replication50-agent-gyrase2019-legacy
  - replication50-agent-pdb6rku-entry
  - replication50-agent-pdb6rku-assembly
  - replication50-agent-pdb6rku-entity1
  - replication50-agent-pdb6rku-entity2
  - replication50-agent-pdb6rkw-entry
  - replication50-agent-pdb6rkw-assembly
  - replication50-agent-ipr-IPR005743
  - replication50-agent-ipr-IPR011557
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0120217
  summary: '10 of 12 collected target identifiers returned OK. PDB:6RKU: SKIPPED;
    Exact native RCSB6RKU deposition identity and primary citation inspected. Its
    domain-focused model scope remains a scientific finding; identifier resolution
    does not endorse the overbroad canonical description.; PMID:31666516: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - replication50-agent-pdb6rku-entry
  - replication50-agent-pmid-31666516
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch50 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch50 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch50 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch50 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0120217
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
    and current batch50 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dna_gyrase_complex.yaml
  locator: Entire target, including all components/examples, graph, evidence, discussions
    and history
  accessed_at: '2026-10-22T05:37:10Z'
  support: context_only
  summary: The full maintained record was read. Historical curation notes are not
    independent biological evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, EssentialityEnum and NONMECHANISTIC
    graph scope
  accessed_at: '2026-10-22T05:37:10Z'
  support: context_only
  summary: Family identity is separate from a taxon-specific example. Assembly necessity
    differs from composition, catalytic requirement and viability.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact family mapping and REVIEWED_LABEL_ONLY contract, especially159–160
  accessed_at: '2026-10-22T05:37:10Z'
  support: context_only
  summary: Reviewed label-only status requires an unresolved exact mapping, rather
    than simply deferring a verified available family.
- evidence_id: replication50-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003918,GO:0006260,GO:0009330,GO:0009360,GO:0032991,GO:0034335,GO:0043846,GO:0043847,GO:0044775,GO:0044776,GO:0120217
  locator: Relevant complete identity/definition/active-status/synonyms and typed
    parent child links in the11-term native response; no unrelated descendants promoted
  accessed_at: '2026-10-22T05:30:55.931295Z'
  support: supports
  summary: GO0120217 matches the gyrase identity and GO0009330 has it as an is-a child.
    GO0034335 and GO0003918 define negative supercoiling and ATP-dependent typeII
    topology; the former explicitly warns that supercoiling ability is not uniform
    across bacterial gyrases.
  snapshot_sha256: 78c81c7a8592b89cd060d4a7121e6954b1fb57e2470ea40413dc05efd6f1029a
- evidence_id: replication50-agent-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxon response
  accessed_at: '2026-10-22T05:30:55.931959Z'
  support: supports
  summary: ENA taxon83333 is Escherichia coli K-12, rank strain; exact names, synonyms
    and available lineage read.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: replication50-agent-protein-P0AES4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AES4.json
  locator: Accession/status/protein name/genes/organism, function/subunit/similarity
    comments and InterPro xrefs
  accessed_at: '2026-10-22T05:30:56.724739Z'
  support: supports
  summary: Reviewed P0AES4 is the declared gyrA protein in E.coli K12 taxon83333.
    Native function/subunit/similarity annotations and InterPro links support the
    identity; underlying experiments are certified only where separately read.
  snapshot_sha256: a69da3b0cb03f1092f1dbd6b3a9fadc93e98b7be0791b11f89c235a5681ce7e0
- evidence_id: replication50-agent-gene-gyrA-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgyrA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: All returned identities/aliases in gene_exact AND taxonomy_id:83333 AND
    reviewed:true, size500
  accessed_at: '2026-10-22T05:30:57.840102Z'
  support: supports
  summary: The complete current reviewed exact-gene query for gyrA and taxonomy83333
    returns one entry, P0AES4, with matching gene and organism.
  snapshot_sha256: eae5fd1ed4476e99c4d1aa676438fb80d0881a91be441011e89c98a80668045f
  search_scope: UniProt gene_exact:gyrA AND taxonomy_id:83333 AND reviewed:true; size500;
    complete one-result identity read. This bounded query is not gene-absence evidence.
- evidence_id: replication50-agent-protein-P0AES6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AES6.json
  locator: Accession/status/protein name/genes/organism, function/subunit/similarity
    comments and InterPro xrefs
  accessed_at: '2026-10-22T05:30:56.874648Z'
  support: supports
  summary: Reviewed P0AES6 is the declared gyrB protein in E.coli K12 taxon83333.
    Native function/subunit/similarity annotations and InterPro links support the
    identity; underlying experiments are certified only where separately read.
  snapshot_sha256: 0173a94c0ecd654e17e8da52dd9806a2d215b177d9474473cc73f50b740a19b4
- evidence_id: replication50-agent-gene-gyrB-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgyrB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: All returned identities/aliases in gene_exact AND taxonomy_id:83333 AND
    reviewed:true, size500
  accessed_at: '2026-10-22T05:30:57.999554Z'
  support: supports
  summary: The complete current reviewed exact-gene query for gyrB and taxonomy83333
    returns one entry, P0AES6, with matching gene and organism.
  snapshot_sha256: 7f291d2a8b59d8769fc4f789d9cfbace8c08bbd60ebffae2638b28a0072bed02
  search_scope: UniProt gene_exact:gyrB AND taxonomy_id:83333 AND reviewed:true; size500;
    complete one-result identity read. This bounded query is not gene-absence evidence.
- evidence_id: replication50-agent-pmid-31666516
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A31666516+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and entire native abstract
  accessed_at: '2026-10-22T05:30:59.165208Z'
  support: supports
  summary: 'Native MED31666516: Cryo-EM structure of the complete E. coli DNA gyrase
    nucleoprotein complex. Authors Vanden Broeck A, Lotz C, Ortiz J, Lamour V.; DOI
    10.1038/s41467-019-12914-y. Complete abstract read at primary-study abstract tier;
    metadata is not a claim of full-body access.'
  snapshot_sha256: 1b13ca479b7d29ffdd60bc5e11cb7647cce7e7d90ad9ad7c53606f38a1f2367f
- evidence_id: replication50-agent-gyrase2019-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6821735/
  locator: Genuine PMC6821735 Introduction Sec1; Results Sec3/Sec4 and Fig1–3 captions;
    entire Discussion Sec8; Methods Sec10–13, Sec17, Sec20–21; Data availability notes2.
    Text/captions only, no supplement or pixels.
  accessed_at: '2026-10-22T05:32:49.580211Z'
  support: supports
  summary: Primary reconstruction establishes full GyrA2B2 architecture, with independently
    assayed supercoiling/ATPase activity. Cryo-EM uses gepotidacin and AMP-PNP; BL21(DE3)pRARE2
    is the expression host. Sec17 assigns the closed DNA-binding/cleavage-domain model
    to6RKU and the overall model to6RKW.
  snapshot_sha256: 97dec7f35627fabca7b24cdaae5b2a741fc570dc8fd5d7d3b7eead73daa4f616
- evidence_id: replication50-agent-pdb6rku-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/6RKU
  locator: Native title, primary citation and experimental/model counts
  accessed_at: '2026-10-22T05:31:00.459033Z'
  support: supports
  summary: 6RKU is titled E.coli DNA gyrase DNA-binding and cleavage domain in State1,
    at4.0A. Its exact primary citation is Vanden Broeck2019/PMID31666516/DOI10.1038/s41467-019-12914-y;
    the deposition is not the overall full-architecture model.
  snapshot_sha256: a4f8c7d36049c1d57991d8474271b4a0c10b7b6cd21f94ff7fc2b8ec84d167da
- evidence_id: replication50-agent-pdb6rku-assembly
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/6RKU/1
  locator: Assembly1 composition, polymer counts, asym_id list and modeled/unmodeled
    monomer counts
  accessed_at: '2026-10-22T05:31:00.534755Z'
  support: supports
  summary: 'Assembly1 has four protein instances and four DNA instances: the eight-polymer
    count is not eight protein subunits. Two GyrA and two GyrB entity mappings remain
    correct, despite incomplete modeled domain coverage.'
  snapshot_sha256: 1186bd23f7f504961033028d9f0d7be4139ee62f811bdd3db49146dd8378729f
- evidence_id: replication50-agent-pdb6rku-entity1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6RKU/1
  locator: Native entity identity, SIFTS accession, molecule count, source organism
    and host organism
  accessed_at: '2026-10-22T05:31:00.567790Z'
  support: supports
  summary: Polymer entity1 is GyrA, mapped to P0AES4, with two listed chains, source
    taxon83333 and distinct expression host BL21(DE3)469008. Full sample sequence
    mapping does not imply all residues are modeled.
  snapshot_sha256: 358604ee562ec36f13b998480571cfda11fa158692944d86ca8078c5b6dd84d1
- evidence_id: replication50-agent-pdb6rku-entity2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6RKU/2
  locator: Native entity identity, SIFTS accession, molecule count, source organism
    and host organism
  accessed_at: '2026-10-22T05:31:00.599836Z'
  support: supports
  summary: Polymer entity2 is GyrB, mapped to P0AES6, with two listed chains, source
    taxon83333 and distinct expression host BL21(DE3)469008. Full sample sequence
    mapping does not imply all residues are modeled.
  snapshot_sha256: f71aeebec430466327f9841d2d7ef05fd7be3fec1c38c1712244b275bb9239dc
- evidence_id: replication50-agent-pdb6rkw-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/6RKW
  locator: Native title, primary citation and experimental metadata
  accessed_at: '2026-10-22T05:35:10.782428Z'
  support: supports
  summary: 6RKW is the complete E.coli DNA gyrase structure, with the same primary
    citation; this is the overall model named in primary Methods Sec17.
  snapshot_sha256: e96c06cf26895043a7d0292e9de5f1048aebfe171333e3a29b366308125b290b
- evidence_id: replication50-agent-pdb6rkw-assembly
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/6RKW/1
  locator: Native biological assembly composition and polymer-instance counts
  accessed_at: '2026-10-22T05:35:10.781978Z'
  support: supports
  summary: 6RKW assembly1 retains the GyrA2B2 protein/NA architecture. The distinct
    entry provides the overall-model candidate; no coordinate-level reanalysis is
    claimed.
  snapshot_sha256: 3ff9bdffdf1f1a2a4089621ad907d9416726c6c3e5cb3ce5ec8f843dbee74c24
- evidence_id: replication50-agent-ipr-IPR005743
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005743/
  locator: Native name/type, complete description, hierarchy/signatures and curation
    flags
  accessed_at: '2026-10-22T05:31:00.235181Z'
  support: supports
  summary: IPR005743 is the exact DNA gyrase A full-protein family, with GyrA-specific
    HAMAPMF01897 and native EC5.6.2.2 cross-reference. Its broader background paragraphs
    are not treated as definitions of every topoisomerase.
  snapshot_sha256: 3381bdfb7148e154fda31bde2ba43fa7b703fb61ff2e064a153cdb84f6fd231b
- evidence_id: replication50-agent-ipr-IPR011557
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011557/
  locator: Native name/type, complete description, hierarchy/signatures and curation
    flags
  accessed_at: '2026-10-22T05:31:00.366347Z'
  support: supports
  summary: IPR011557 is the exact DNA gyrase B full-protein family, with HAMAPMF01898/NCBIfamTIGR01059
    and EC5.6.2.2.
  snapshot_sha256: 4d68f4e62fbab9095f45069c2ac8461c4de9942f13db1ebe84315906e2197560
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dna_gyrase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:31:30Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dna_gyrase_complex.yaml'
  snapshot_sha256: a5c796e04b0f0f82fadb54ac7b567e449f62f46f907f05e6e461cf48b9eb6251
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dna_gyrase_complex.yaml --out
    /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dna_gyrase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:31:32Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dna_gyrase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dna_gyrase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dna_gyrase_complex-strict.tsv"
  snapshot_sha256: acdbb36574d0800729bab7b58d22a62eeb2a41bc5296fc990a8986f6af989d32
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_gyrase_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:32:56.307515Z'
  support: supports
  summary: "data/structures/other/dna_gyrase_complex.yaml  (GO:0120217)\n  dna_gyrase_negative_supercoiling\t\
    gyrase_subunit_a\tCOVERED\t->gyrase_subunit_a (UniProtKB:P0AES4)\n  dna_gyrase_negative_supercoiling\t\
    gyrase_subunit_b\tCOVERED\t->gyrase_subunit_b (UniProtKB:P0AES6)\n\ncausal_graphs\
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
  snapshot_sha256: e9925e98caefb278bed69f8a980ae3af6087a314dde6560afdf7442ac66a91b6
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_gyrase_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:32:59.210856Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dna_gyrase_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 12 collected target identifiers returned OK. PDB:6RKU: SKIPPED;
    Exact native RCSB6RKU deposition identity and primary citation inspected. Its
    domain-focused model scope remains a scientific finding; identifier resolution
    does not endorse the overbroad canonical description.; PMID:31666516: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
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
  topic: Gyrase complex and broader topoisomerase class
  outcome: supported
  target_ids:
  - GO:0120217
  summary: Native GO identity and is-a parent agree. The record describes the usual
    bacterial GyrA2B2 class, distinct from the broader typeIIA family; no unrelated
    topoisomerase synonym is imported.
  evidence_ids:
  - record
  - replication50-agent-go
  - replication50-agent-gyrase2019-legacy
- assessment_id: composition
  area: grounding
  topic: Exact families, examples and2:2 protein composition
  outcome: supported
  target_ids:
  - GO:0120217
  summary: Both full-protein families, reviewed K12 examples and current single-hit
    notes are correct. RCSB entities and primary reconstitution support two copies
    of each subunit. DNA and inhibitor in a trapped experimental assembly are not
    missing permanent protein-component rows.
  evidence_ids:
  - record
  - replication50-agent-protein-P0AES4
  - replication50-agent-protein-P0AES6
  - replication50-agent-gene-gyrA-83333
  - replication50-agent-gene-gyrB-83333
  - replication50-agent-ipr-IPR005743
  - replication50-agent-ipr-IPR011557
  - replication50-agent-pdb6rku-entity1
  - replication50-agent-pdb6rku-entity2
  - replication50-agent-pdb6rku-assembly
  - replication50-agent-gyrase2019-legacy
- assessment_id: canonical
  area: scope
  topic: Source strain and exact deposited model
  outcome: concern
  target_ids:
  - GO:0120217
  summary: 'K12 source taxon is verified separately from BL21(DE3) expression host.
    The canonical note overstates6RKU as the complete model: both native title and
    primary Sec17 identify it as the cleavage-domain State1 model, while6RKW is the
    overall architecture. Valid6RKU entity/stoichiometry links can remain.'
  evidence_ids:
  - record
  - replication50-agent-gyrase2019-legacy
  - replication50-agent-pdb6rku-entry
  - replication50-agent-pdb6rkw-entry
  - replication50-agent-pdb6rkw-assembly
  - replication50-agent-tax83333
  - replication50-agent-pdb6rku-entity1
  - replication50-agent-pdb6rku-entity2
- assessment_id: function-graph
  area: graph
  topic: Coarse topology function with experimental separation
  outcome: supported
  target_ids:
  - GO:0120217
  summary: GO and primary supercoiling/ATPase assay descriptions support the coarse
    NONMECHANISTIC graph. The drug/AMP-PNP-trapped EM structure alone is not an active
    turnover assay; the paper separately tests activity. The record does not claim
    a fully resolved strand-passage cycle or uniformly equal activity across species.
  evidence_ids:
  - record
  - schema
  - replication50-agent-go
  - replication50-agent-gyrase2019-legacy
  - replication50-agent-pdb6rku-assembly
- assessment_id: formation
  area: grounding
  topic: No inferred assembly-necessity values
  outcome: unknown
  target_ids:
  - GO:0120217
  summary: No essentiality field is supplied in these component rows. The inspected
    reconstitution and structural membership are not used to invent an optional field
    or a universal deletion-based formation requirement.
  evidence_ids:
  - record
  - schema
  - replication50-agent-gyrase2019-legacy
- assessment_id: coverage
  area: completeness
  topic: Entire maintained target audited
  outcome: supported
  target_ids:
  - GO:0120217
  summary: All maintained fields, discussions and historical entries were read. Source
    identity, experimental scope, molecular class and graph roles were checked separately;
    no optional inventory or uninspected mechanism was invented.
  evidence_ids:
  - record
  - schema
  - curation
  - replication50-agent-go
findings:
- finding_id: F1
  issue_key: gyrase-deposition-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish the cleavage-domain and overall gyrase depositions
  description: The canonical example calls PDB6RKU the complete GyrA2-GyrB2 cryo-EM
    assembly. Its native title and primary Methods Sec17 identify6RKU as the closed
    DNA-binding/cleavage-domain model and6RKW as the overall model. The two correct
    protein entity mappings and2:2 stoichiometry are unaffected.
  target_ids:
  - GO:0120217
  field_paths:
  - canonical_examples[0].note
  - canonical_examples[0].reference
  evidence_ids:
  - record
  - replication50-agent-gyrase2019-legacy
  - replication50-agent-pdb6rku-entry
  - replication50-agent-pdb6rkw-entry
  - replication50-agent-pdb6rku-assembly
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_gyrase_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific identity, scope and exact component grounding
  native_severity: minor
  normalization_reason: The maintained complex identity, correct protein examples
    and supported coarse function remain intact; the defect is localized source precision
    or exact family grounding.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0120217
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_gyrase_complex.yaml
    role: maintained scientific record
  description: Qualify6RKU as the domain-focused State1 deposition, or use the verified6RKW
    entry for an explicitly overall-model canonical example; retain6RKU where its
    GyrA/B entity mapping is the relevant evidence.
  acceptance_checks:
  - Keep K12 source distinct from BL21(DE3) expression.
  - Do not describe full sample sequences as proof of complete atomic coverage.
  - Preserve supported identifiers, examples and biological scope; pass applicable
    native validation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, supplementary experimental data, sequence alignments or coordinate
  geometry were independently reanalyzed. Exact text and native metadata scopes are
  identified per evidence row.
- The full-length enzyme was imaged under trapping conditions and modeled at several
  resolutions. No claim is made that6RKW resolves every residue, or that6RKU itself
  represents active ATP hydrolysis.
- GO0034335 explicitly cautions against uniform supercoiling generalization across
  all bacterial gyrases; the concrete experimental example here is E.coli.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes qualified clean reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
