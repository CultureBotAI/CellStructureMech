# COPII vesicle identity and evidence review

- Review: 20261022T005258Z-copii-coated-vesicle-lumen-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T11:11:28Z
- Finished UTC: 2026-10-22T00:52:58Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact identity, yeast context, coat or lumen boundaries and descriptive transport topology are supported within the declared primary-source limits. No concrete curation issue was established.

## Scope And Provenance

Entire single maintained record and exact native-source/primary-literature claims; no scientific mutations.

Selection: Target 10 in batch24, exact sorted uncovered maintained path at frozen revision9c0446.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:copii_coated_vesicle_lumen | data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml | maintained | COPII-coated vesicle lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native verify | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Focused command passed. Neither target has explicit accession examples or GENE_OR_PROTEIN graph nodes; the whole-vesicle coat identity is assessed separately. |
| Focused native causal-graphs | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Focused command passed. Neither target has explicit accession examples or GENE_OR_PROTEIN graph nodes; the whole-vesicle coat identity is assessed separately. |
| Focused native schema | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:copii_coated_vesicle_lumen | 5 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | cellstructuremech:copii_coated_vesicle_lumen | No expression-module, transcriptomic or regulator-network inference is made by this structural review. |
| Claim-level scientific review | passed | True | cellstructuremech:copii_coated_vesicle_lumen | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact carrier or spatial-lumen identity

identity: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

The maintained target identity is supported by the exact native source. The whole carrier is a coated-vesicle subtype and includes a COPII coat; its lumen is a spatial region inside the carrier, with cytoplasmic-vesicle-lumen parent and exact UniProt location. Synonym types and is_a versus part_of are preserved. No whole coat or transport process is substituted for the target structure.

### Yeast source context and qualified occurrence

scope: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

NCBITaxon4932 is exact. Barlowe provides the founding ER-derived vesicle reconstitution context, while Matsuoka Methods explicitly identify Saccharomyces cerevisiae RSY445 microsomes and RSY1113 Sec13/31 preparations. The maintained notes concern yeast COPII machinery and ER-derived vesicles; they do not assert those experimental strains are the taxon itself. COMMON is qualitative occurrence of established secretory-pathway compartments, not a measured population prevalence or invariant presence in each mutant or physiological state.

### Bounded interior and membrane topology

graph: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

SL0322 defines the lumen and both NONMECHANISTIC edges follow its explicit partOf and bounding-membrane definitions. GO0012507 is the surrounding ER-to-Golgi transport vesicle membrane and has COPII-coated-vesicle-membrane as an exact synonym. No invariant luminal cargo inventory is required for this spatial class. Matsuoka luminal-dye retention is additional reconstituted-system context, not direct imaging of this compartment in living yeast or a claim about every native cargo.

### Formation requirements are not asserted for individual constituents

evidence: unknown. Targets: cellstructuremech:copii_coated_vesicle_lumen.

The targets contain no component essentiality labels. Purified-subunit reconstitution tests support the specifically described in-vitro assembly context; they do not establish universal in-vivo necessity of each protein, lipid, regulator or cargo for the entire carrier/lumen class. No automatic missing-component or essentiality finding follows.

### Verified citations and honest source tiers

provenance: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

Both claimed primary citation identities are correct where present. Matsuoka is a genuine author-hosted primary PDF with original URL, UTC and hash preserved and explicit body-read scope. Barlowe remains complete-abstract support after the two retained403 routes; numerical properties, Methods and figures from that paper were not independently audited. Historical unreadability notes are not treated as false because another source route later became accessible. No verbatim snippets or image-license claims are present.

### Full single-target coverage without forced optional inventories

completeness: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

All maintained fields were assessed, including history, occurrence, parts, function and each graph edge. Optional direct molecular inventories, images, quantitative properties and expanded mechanisms are not required for these whole-carrier/spatial-volume records. No consequential missing representation or concrete source contradiction was established.

### Exact-label GO candidate has unresolved definition scope

grounding: unknown. Targets: cellstructuremech:copii_coated_vesicle_lumen.

GO0106173 is an active exact-label candidate, but its endocytic definition does not unambiguously match this ER-to-Golgi target. The present SL0322 identity remains positively supported by its own native definition and parthood. Candidate resolution requires reconciling the GO definition and intended class scope; neither GO absence nor an immediate identifier replacement is asserted.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml; Entire maintained YAML, including identity, all evidence and graph edges, history and occurrence notes | context_only | All target fields were read after native inspection. No maintained scientific content, history or mapping status is changed. |
| policy | docs/CURATION.md; Identity versus material grounding, exact claim scope and assembly-necessity contract | context_only | A compartment, coat, particular protein and transport activity are distinct claim types. Optional inventories and unavailable evidence alone do not create findings. |
| copii-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030134,GO:0030135,GO:0030127,GO:0090114,GO:0006888,GO:0005789,GO:0005794,GO:0060205,GO:0012507; All9 returned active identifiers/names/aspects/definitions; relevant synonyms and explicit children relation objects. Coat membership and carrier route distinguished from biological-process identity. | supports | Nine active terms supply exact identities for the COPII carrier, coated-vesicle parent, coat, ER/Golgi endpoints, budding and transport processes, lumen parent and surrounding membrane. GO0030135 explicitly lists GO0030134 is_a; GO0030134 lists membraneGO0012507 part_of, and that membrane lists COPIIcoatGO0030127 part_of. These compose parthood rather than inventing an unreturned direct relation. Exact and related synonym types on GO0030134 match the maintained aliases. GO0090114 describes ER-membrane evagination; GO0006888 describes ER-to-Golgi vesicle-mediated transport. |
| copii-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and alternative names | supports | The native taxon identifies Saccharomyces cerevisiae at species rank, with returned fungal lineage and synonyms. Taxonomic identity does not establish any particular experimental genotype or a prevalence survey. |
| copii-agent-PMID-8004676 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8004676%20AND%20SRC%3AMED; Exact PMID/DOI/title/authors/year and entire returned abstract | supports | Native MED identifies COPII: a membrane coat formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum. (Barlowe C, Orci L, Yeung T, Hosobuchi M, Hamamoto S, Salama N, Rexach MF, Ravazzola M, Amherdt M, Schekman R., 1994), PMID8004676, DOI10.1016/0092-8674(94)90138-4. Exact bibliography and the complete abstract were read. The Barlowe abstract reports washed-ER membrane reconstitution with Sar1p/Sec13p/Sec23p complexes and distinguishes GTP vesicles that target/fuse with Golgi from GMP-PNP vesicles that do not; no full-body or numerical-property audit is claimed. |
| copii-agent-matsuoka1998-author | https://bednareklab.biochem.wisc.edu/wp-content/uploads/sites/1623/2022/02/1998_Matsuoka_etal_Cell.pdf; Published pp263–274: Summary, complete Introduction, Results and Discussion; Experimental Procedures including RSY445 microsomes and RSY1113 Sec13/31 preparation, lipid/binding assays, stoichiometry and EM methods. Tables1–2 and Fig1–8 captions read. Especially pp269–271 native/synthetic comparison and luminal integrity, Fig7D caption, pp273–274 Methods. Figure pixels, supplementary data and raw measurements not reanalysed. | supports | The primary study compares recruitment and vesicle formation using native yeast ER membranes and chemically defined liposomes. Sequential Sar1p/Sec23-24/Sec13-31 recruitment and the native-versus-synthetic comparison support the maintained coat/budding context. The liposome HPTS/DPX experiments support retention of enclosed contents without rupture/resealing in that reconstituted system. The paper explicitly notes different coat concentrations/stoichiometry and incomplete physiological equivalence; synthetic vesicles are not relabeled as native ER-derived carriers. |
| copii-agent-SL-0322 | https://rest.uniprot.org/locations/SL-0322.json; Exact top-level id/name/definition/synonyms, isA and partOf entries, and their nested GO cross-references | supports | The native location exactly defines the COPII-coated vesicle lumen and supplies both maintained synonyms. It has isA cytoplasmic-vesicle lumen SL0325 (mapped to GO0060205) and direct partOf COPII-coated vesicle SL0077 (mapped to GO0030134). The lumen definition explicitly supplies its membrane boundary. No direct GO cross-reference is returned for SL0322; this is not an exhaustive GO-absence claim. |
| copii-agent-barlowe1994-publisher | https://www.cell.com/article/0092867494901384/pdf; Actual public full-text access response, not paper content | context_only | This specific attempted Barlowe primary full-text route returned403 and no readable body. The complete native abstract remains the Barlowe scientific source tier. |
| copii-agent-barlowe1994-sciencedirect | https://www.sciencedirect.com/science/article/pii/0092867494901384; Actual public full-text access response, not paper content | context_only | This specific attempted Barlowe primary full-text route returned403 and no readable body. The complete native abstract remains the Barlowe scientific source tier. |
| native-verify | /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml --verify; Complete focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml --causal-graphs; Complete focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml --out /private/tmp/cellstructure-batch24-20261021-qayobm82/copii_coated_vesicle_lumen-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml --out /private/tmp/cellstructure-batch24-20261021-qayobm82/copii_coated_vesicle_lumen-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch24-20261021-qayobm82/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch24-20261021-qayobm82/copii_coated_vesicle_lumen-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 5 of7 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:8004676: UNREACHABLE; resolved by evidence copii-agent-PMID-8004676; cellstructuremech:copii_coated_vesicle_lumen: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| copii-agent-go-lumen-candidates | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106172,GO:0106173,GO:0106174; Complete active status, exact labels, definitions and definition references for GO0106172/0106173/0106174; only GO0106173 is the COPII candidate. | context_only | Native GO0106173 is active and has the exact label COPII-coated vesicle lumen, but its definition specifies the membrane of a COPII-coated endocytic vesicle, citing PMID21172817. That scope conflicts with the maintained ER-to-Golgi lumen context. The label is a candidate for future authority reconciliation; this response alone does not establish exact replacement identity. The other returned terms denote COPI-coated and phagolysosome lumina. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Barlowe1994 was read through exact native bibliography and the complete abstract only. The retained Cell PDF and ScienceDirect routes returned403; no full-body, Methods or image-pixel audit is claimed.
- Matsuoka1998 was read at the declared full scientific-body scope. Figure captions and tables were inspected, but no microscopy pixels or raw fluorescence/EM measurements were reanalysed.
- Native ER membrane and synthetic liposome assays are distinct; GMP-PNP stabilization, concentration and stoichiometry differences prevent treating all reconstructed products as physiological Golgi-fusion-competent carriers.
- COMMON is qualitative established occurrence, not a taxon-wide prevalence assay. No exact per-vesicle composition or in-vivo constituent necessity is inferred from spatial identity.
- Historical searches and independent historical authorship are not recertified. Completed same-base global15 gates are added only at root finalization.
- Active GO0106173 has the exact lumen label but an endocytic-vesicle definition that conflicts with the ER-to-Golgi context. This candidate remains unresolved; no exhaustive GO-absence claim or forced identity replacement is made.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized a review for every uncovered record, including clean observations. This is an unsaved single-record draft; no index, persistence, finalization or Git mutation was performed.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T005258Z-copii-coated-vesicle-lumen-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: COPII vesicle identity and evidence review
started_at: '2026-10-21T11:11:28Z'
finished_at: '2026-10-22T00:52:58Z'
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
summary: Exact identity, yeast context, coat or lumen boundaries and descriptive transport
  topology are supported within the declared primary-source limits. No concrete curation
  issue was established.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    sha256: d75ae8e81d2fc08979408842f74ef1ad621e87108044faf2dcc6ca216e5e7782
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
- target_id: cellstructuremech:copii_coated_vesicle_lumen
  path: data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
  label: COPII-coated vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained record and exact native-source/primary-literature
    claims; no scientific mutations.
  selection: Target 10 in batch24, exact sorted uncovered maintained path at frozen
    revision9c0446.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
checks:
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    --verify
  exit_code: 0
  summary: Focused command passed. Neither target has explicit accession examples
    or GENE_OR_PROTEIN graph nodes; the whole-vesicle coat identity is assessed separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused command passed. Neither target has explicit accession examples
    or GENE_OR_PROTEIN graph nodes; the whole-vesicle coat identity is assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just validate data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just validate-strict data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    --out /private/tmp/cellstructure-batch24-20261021-qayobm82/copii_coated_vesicle_lumen-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: 5 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - copii-agent-PMID-8004676
  - record
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: No expression-module, transcriptomic or regulator-network inference is
    made by this structural review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - copii-agent-go
  - copii-agent-tax4932
  - copii-agent-PMID-8004676
  - copii-agent-matsuoka1998-author
  - copii-agent-SL-0322
  - copii-agent-barlowe1994-publisher
  - copii-agent-barlowe1994-sciencedirect
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
  locator: Entire maintained YAML, including identity, all evidence and graph edges,
    history and occurrence notes
  accessed_at: '2026-10-21T11:13:33Z'
  support: context_only
  summary: All target fields were read after native inspection. No maintained scientific
    content, history or mapping status is changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Identity versus material grounding, exact claim scope and assembly-necessity
    contract
  accessed_at: '2026-10-21T11:13:33Z'
  support: context_only
  summary: A compartment, coat, particular protein and transport activity are distinct
    claim types. Optional inventories and unavailable evidence alone do not create
    findings.
- evidence_id: copii-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030134,GO:0030135,GO:0030127,GO:0090114,GO:0006888,GO:0005789,GO:0005794,GO:0060205,GO:0012507
  locator: All9 returned active identifiers/names/aspects/definitions; relevant synonyms
    and explicit children relation objects. Coat membership and carrier route distinguished
    from biological-process identity.
  accessed_at: '2026-10-21T11:12:01.946307Z'
  support: supports
  summary: Nine active terms supply exact identities for the COPII carrier, coated-vesicle
    parent, coat, ER/Golgi endpoints, budding and transport processes, lumen parent
    and surrounding membrane. GO0030135 explicitly lists GO0030134 is_a; GO0030134
    lists membraneGO0012507 part_of, and that membrane lists COPIIcoatGO0030127 part_of.
    These compose parthood rather than inventing an unreturned direct relation. Exact
    and related synonym types on GO0030134 match the maintained aliases. GO0090114
    describes ER-membrane evagination; GO0006888 describes ER-to-Golgi vesicle-mediated
    transport.
  snapshot_sha256: 3b391d054f6f355480cf0c55d0e10b4ea88dd6b250c3683c60587ddc62cb77c6
- evidence_id: copii-agent-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and alternative names
  accessed_at: '2026-10-21T11:04:40.023078Z'
  support: supports
  summary: The native taxon identifies Saccharomyces cerevisiae at species rank, with
    returned fungal lineage and synonyms. Taxonomic identity does not establish any
    particular experimental genotype or a prevalence survey.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: copii-agent-PMID-8004676
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8004676%20AND%20SRC%3AMED
  locator: Exact PMID/DOI/title/authors/year and entire returned abstract
  accessed_at: '2026-10-21T10:57:49.986369Z'
  support: supports
  summary: 'Native MED identifies COPII: a membrane coat formed by Sec proteins that
    drive vesicle budding from the endoplasmic reticulum. (Barlowe C, Orci L, Yeung
    T, Hosobuchi M, Hamamoto S, Salama N, Rexach MF, Ravazzola M, Amherdt M, Schekman
    R., 1994), PMID8004676, DOI10.1016/0092-8674(94)90138-4. Exact bibliography and
    the complete abstract were read. The Barlowe abstract reports washed-ER membrane
    reconstitution with Sar1p/Sec13p/Sec23p complexes and distinguishes GTP vesicles
    that target/fuse with Golgi from GMP-PNP vesicles that do not; no full-body or
    numerical-property audit is claimed.'
  snapshot_sha256: f3ff438cc130518602efe6aa0252c6d5634fafad949d62cf23e3a6e837819fc7
- evidence_id: copii-agent-matsuoka1998-author
  kind: primary_source
  reference: https://bednareklab.biochem.wisc.edu/wp-content/uploads/sites/1623/2022/02/1998_Matsuoka_etal_Cell.pdf
  locator: 'Published pp263–274: Summary, complete Introduction, Results and Discussion;
    Experimental Procedures including RSY445 microsomes and RSY1113 Sec13/31 preparation,
    lipid/binding assays, stoichiometry and EM methods. Tables1–2 and Fig1–8 captions
    read. Especially pp269–271 native/synthetic comparison and luminal integrity,
    Fig7D caption, pp273–274 Methods. Figure pixels, supplementary data and raw measurements
    not reanalysed.'
  accessed_at: '2026-10-21T11:10:08.369823Z'
  support: supports
  summary: The primary study compares recruitment and vesicle formation using native
    yeast ER membranes and chemically defined liposomes. Sequential Sar1p/Sec23-24/Sec13-31
    recruitment and the native-versus-synthetic comparison support the maintained
    coat/budding context. The liposome HPTS/DPX experiments support retention of enclosed
    contents without rupture/resealing in that reconstituted system. The paper explicitly
    notes different coat concentrations/stoichiometry and incomplete physiological
    equivalence; synthetic vesicles are not relabeled as native ER-derived carriers.
  snapshot_sha256: 4c7e8eafea53f213b25b339d684115bd65a1af9e79d86b9e1222050aa52b0efa
- evidence_id: copii-agent-SL-0322
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0322.json
  locator: Exact top-level id/name/definition/synonyms, isA and partOf entries, and
    their nested GO cross-references
  accessed_at: '2026-10-21T11:12:01.946731Z'
  support: supports
  summary: The native location exactly defines the COPII-coated vesicle lumen and
    supplies both maintained synonyms. It has isA cytoplasmic-vesicle lumen SL0325
    (mapped to GO0060205) and direct partOf COPII-coated vesicle SL0077 (mapped to
    GO0030134). The lumen definition explicitly supplies its membrane boundary. No
    direct GO cross-reference is returned for SL0322; this is not an exhaustive GO-absence
    claim.
  snapshot_sha256: 1e9227774ff93659e52c60dde84a590d43591d0e4ac5d3c190b446db015b889f
- evidence_id: copii-agent-barlowe1994-publisher
  kind: authority
  reference: https://www.cell.com/article/0092867494901384/pdf
  locator: Actual public full-text access response, not paper content
  accessed_at: '2026-10-21T10:58:29.273436Z'
  support: context_only
  summary: This specific attempted Barlowe primary full-text route returned403 and
    no readable body. The complete native abstract remains the Barlowe scientific
    source tier.
  snapshot_sha256: 6d0a5634db429b0ee61d3d8d69a9a19a36394072565e9883d59cc6fd369d859c
- evidence_id: copii-agent-barlowe1994-sciencedirect
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/0092867494901384
  locator: Actual public full-text access response, not paper content
  accessed_at: '2026-10-21T11:00:51.278514Z'
  support: context_only
  summary: This specific attempted Barlowe primary full-text route returned403 and
    no readable body. The complete native abstract remains the Barlowe scientific
    source tier.
  snapshot_sha256: 3d1169b14e8018ba05b1f0dfc9e5f4036b4133f6bc2cd410127c5c1d388722cf
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    --verify
  locator: Complete focused native output
  accessed_at: '2026-10-21T11:12:38.586013Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    --causal-graphs
  locator: Complete focused native output
  accessed_at: '2026-10-21T11:12:39.141913Z'
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
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:11:30Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml'
  snapshot_sha256: c1416811bc80c7c50df5ec8f8bb8dde03165043cd4825e6566cd9386188ad3c2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    --out /private/tmp/cellstructure-batch24-20261021-qayobm82/copii_coated_vesicle_lumen-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:11:31Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml\
    \ --out /private/tmp/cellstructure-batch24-20261021-qayobm82/copii_coated_vesicle_lumen-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch24-20261021-qayobm82/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch24-20261021-qayobm82/copii_coated_vesicle_lumen-strict.tsv"
  snapshot_sha256: 3f170cfdca57bc8cc5d9b4e7d306b2deb103769ed47d3a70fd4fa3a9f53d0708
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T11:13:33Z'
  support: supports
  summary: '5 of7 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:8004676: UNREACHABLE; resolved by evidence copii-agent-PMID-8004676;
    cellstructuremech:copii_coated_vesicle_lumen: SKIPPED; resolved by evidence record.
    Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: copii-agent-go-lumen-candidates
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106172,GO:0106173,GO:0106174
  locator: Complete active status, exact labels, definitions and definition references
    for GO0106172/0106173/0106174; only GO0106173 is the COPII candidate.
  accessed_at: '2026-10-21T11:18:39.570972Z'
  support: context_only
  summary: Native GO0106173 is active and has the exact label COPII-coated vesicle
    lumen, but its definition specifies the membrane of a COPII-coated endocytic vesicle,
    citing PMID21172817. That scope conflicts with the maintained ER-to-Golgi lumen
    context. The label is a candidate for future authority reconciliation; this response
    alone does not establish exact replacement identity. The other returned terms
    denote COPI-coated and phagolysosome lumina.
  snapshot_sha256: dc88a9d584e1ae86bb88b94724aaa7e1052ffad58276ca960ebdbc5b51e1c782
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: identity
  area: identity
  topic: Exact carrier or spatial-lumen identity
  outcome: supported
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: The maintained target identity is supported by the exact native source.
    The whole carrier is a coated-vesicle subtype and includes a COPII coat; its lumen
    is a spatial region inside the carrier, with cytoplasmic-vesicle-lumen parent
    and exact UniProt location. Synonym types and is_a versus part_of are preserved.
    No whole coat or transport process is substituted for the target structure.
  evidence_ids:
  - record
  - policy
  - copii-agent-go
  - copii-agent-tax4932
  - copii-agent-PMID-8004676
  - copii-agent-matsuoka1998-author
  - copii-agent-SL-0322
- assessment_id: scope
  area: scope
  topic: Yeast source context and qualified occurrence
  outcome: supported
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: NCBITaxon4932 is exact. Barlowe provides the founding ER-derived vesicle
    reconstitution context, while Matsuoka Methods explicitly identify Saccharomyces
    cerevisiae RSY445 microsomes and RSY1113 Sec13/31 preparations. The maintained
    notes concern yeast COPII machinery and ER-derived vesicles; they do not assert
    those experimental strains are the taxon itself. COMMON is qualitative occurrence
    of established secretory-pathway compartments, not a measured population prevalence
    or invariant presence in each mutant or physiological state.
  evidence_ids:
  - record
  - policy
  - copii-agent-go
  - copii-agent-tax4932
  - copii-agent-PMID-8004676
  - copii-agent-matsuoka1998-author
  - copii-agent-SL-0322
- assessment_id: composition-graph
  area: graph
  topic: Bounded interior and membrane topology
  outcome: supported
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: SL0322 defines the lumen and both NONMECHANISTIC edges follow its explicit
    partOf and bounding-membrane definitions. GO0012507 is the surrounding ER-to-Golgi
    transport vesicle membrane and has COPII-coated-vesicle-membrane as an exact synonym.
    No invariant luminal cargo inventory is required for this spatial class. Matsuoka
    luminal-dye retention is additional reconstituted-system context, not direct imaging
    of this compartment in living yeast or a claim about every native cargo.
  evidence_ids:
  - record
  - policy
  - copii-agent-go
  - copii-agent-tax4932
  - copii-agent-PMID-8004676
  - copii-agent-matsuoka1998-author
  - copii-agent-SL-0322
- assessment_id: necessity
  area: evidence
  topic: Formation requirements are not asserted for individual constituents
  outcome: unknown
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: The targets contain no component essentiality labels. Purified-subunit
    reconstitution tests support the specifically described in-vitro assembly context;
    they do not establish universal in-vivo necessity of each protein, lipid, regulator
    or cargo for the entire carrier/lumen class. No automatic missing-component or
    essentiality finding follows.
  evidence_ids:
  - record
  - policy
  - copii-agent-go
  - copii-agent-tax4932
  - copii-agent-PMID-8004676
  - copii-agent-matsuoka1998-author
  - copii-agent-SL-0322
- assessment_id: provenance
  area: provenance
  topic: Verified citations and honest source tiers
  outcome: supported
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: Both claimed primary citation identities are correct where present. Matsuoka
    is a genuine author-hosted primary PDF with original URL, UTC and hash preserved
    and explicit body-read scope. Barlowe remains complete-abstract support after
    the two retained403 routes; numerical properties, Methods and figures from that
    paper were not independently audited. Historical unreadability notes are not treated
    as false because another source route later became accessible. No verbatim snippets
    or image-license claims are present.
  evidence_ids:
  - record
  - policy
  - copii-agent-go
  - copii-agent-tax4932
  - copii-agent-PMID-8004676
  - copii-agent-matsuoka1998-author
  - copii-agent-SL-0322
- assessment_id: completeness
  area: completeness
  topic: Full single-target coverage without forced optional inventories
  outcome: supported
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: All maintained fields were assessed, including history, occurrence, parts,
    function and each graph edge. Optional direct molecular inventories, images, quantitative
    properties and expanded mechanisms are not required for these whole-carrier/spatial-volume
    records. No consequential missing representation or concrete source contradiction
    was established.
  evidence_ids:
  - record
  - policy
  - copii-agent-go
  - copii-agent-tax4932
  - copii-agent-PMID-8004676
  - copii-agent-matsuoka1998-author
  - copii-agent-SL-0322
- assessment_id: ontology-candidate
  area: grounding
  topic: Exact-label GO candidate has unresolved definition scope
  outcome: unknown
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: GO0106173 is an active exact-label candidate, but its endocytic definition
    does not unambiguously match this ER-to-Golgi target. The present SL0322 identity
    remains positively supported by its own native definition and parthood. Candidate
    resolution requires reconciling the GO definition and intended class scope; neither
    GO absence nor an immediate identifier replacement is asserted.
  evidence_ids:
  - copii-agent-go-lumen-candidates
  - copii-agent-SL-0322
  - copii-agent-go
  - record
findings: []
actions: []
limitations:
- Barlowe1994 was read through exact native bibliography and the complete abstract
  only. The retained Cell PDF and ScienceDirect routes returned403; no full-body,
  Methods or image-pixel audit is claimed.
- Matsuoka1998 was read at the declared full scientific-body scope. Figure captions
  and tables were inspected, but no microscopy pixels or raw fluorescence/EM measurements
  were reanalysed.
- Native ER membrane and synthetic liposome assays are distinct; GMP-PNP stabilization,
  concentration and stoichiometry differences prevent treating all reconstructed products
  as physiological Golgi-fusion-competent carriers.
- COMMON is qualitative established occurrence, not a taxon-wide prevalence assay.
  No exact per-vesicle composition or in-vivo constituent necessity is inferred from
  spatial identity.
- Historical searches and independent historical authorship are not recertified. Completed
  same-base global15 gates are added only at root finalization.
- Active GO0106173 has the exact lumen label but an endocytic-vesicle definition that
  conflicts with the ER-to-Golgi context. This candidate remains unresolved; no exhaustive
  GO-absence claim or forced identity replacement is made.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized a review for every uncovered record, including clean
  observations. This is an unsaved single-record draft; no index, persistence, finalization
  or Git mutation was performed.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
