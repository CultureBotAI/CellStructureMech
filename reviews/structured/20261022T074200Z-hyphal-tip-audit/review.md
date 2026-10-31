# Hyphal tip scientific review

- Review: 20261022T074200Z-hyphal-tip-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:12:47Z
- Finished UTC: 2026-10-22T07:42:00Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The fungal/Neurospora tip identity and localized protein observations are supported. One major concerns the unsupported expanded defining scope; one minor corrects a spatial graph labeled mechanistic.

## Scope And Provenance

Exactly one complete maintained target plus frozen guidance, protein-example skill and, for the hyphal pair, the other frozen region/complex neighbor. Actual source-reading extents appear per evidence row.

Selection: Target 7 of batch57, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0001411 | data/structures/other/hyphal_tip.yaml | maintained | hyphal tip |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0001411 | Focused validator passed. |
| Focused native strict | passed | True | GO:0001411 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0001411 | Native focused check passed; biological claims assessed separately. |
| Native verify | passed | True | GO:0001411 | Native focused check passed; biological claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0001411 | No expression-module inference is used. |
| Claim-level scientific review | passed | True | GO:0001411 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0001411 | 12 of 12 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0001411 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0001411 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0001411 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0001411 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0001411 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Fungal tip region and localized polarisome boundary

identity: supported. Targets: GO:0001411.

The exact native identities, parents and the frozen region/complex distinction agree. Source imaging supports the mature Neurospora apical architecture without equating every fungal polarisome to a single Spitzenkorper geometry.

### Three taxon-paired proteins and bounded family candidates

grounding: supported. Targets: GO:0001411.

All three examples are correctly unreviewed OR74A proteins with the stated primary genes. Primary membership/localization comes from Lichius, not accession identity alone. The inspected broader families do not resolve the exact retained classes; no forced family mapping follows.

### Mature Neurospora hyphae and broader fungal comparisons

scope: supported. Targets: GO:0001411.

COMMON retains its majority/losses-exception meaning. The qualitative species-level characterization supports the chosen Neurospora model context, without a measured prevalence census or a claim that every growth stage has a visible Spitzenkorper. OR74A reference protein identity is separate from each transformed experimental strain.

### Tip-growth defects versus formation requirements

grounding: unknown. Targets: GO:0001411.

The deletion data directly support conditional architecture/growth phenotypes. They do not establish that the encompassing tip or every partial polarisome fails to form without each named protein; polarized growth can persist without a detectable Spitzenkorper. The three CONDITIONAL fields therefore retain unresolved formation-specific scope rather than being redefined as catalytic or growth necessity.

### Unestablished extension from fungal GO identity to oomycetes

scope: concern. Targets: GO:0001411.

The maintained definition adds oomycete occurrence and a broad mechanistic description beyond its sole GO source. GO explicitly defines a fungal tip; the directly inspected paper concerns Neurospora and compares other fungi. Its complete retained JATS contains no oomycete mention. This does not prove oomycetes lack apical growth, but the broader defining taxonomic assertion is not established by the cited sources.

### Spatial membership presented as a mechanism

graph: concern. Targets: GO:0001411.

The graph contains protein/substructure parthood and a whole-region mediates-function edge. Those source-supported statements form a coarse topology/function summary without a causal transition or assembly step; its MECHANISTIC label overstates what is encoded.

### Whole maintained target and declared source coverage

completeness: supported. Targets: GO:0001411.

Every maintained field, evidence note, graph claim and discussion was inspected at the declared source extents. Empty optional slots, acknowledged unknowns and broader-family candidates do not independently create findings.

## Findings

### F1: Source and qualify the expanded hyphal-tip definition

major / open / confirmed; issue key: hyphal-tip-definition-scope.

The fungal GO identity is extended in the maintained defining text to oomycetes and generalized apparatus mechanisms while definition_source remains GO0001411. The exact GO definition and the cited Neurospora primary study do not establish that cross-lineage defining scope.

### F2: Label the spatial graph as nonmechanistic

minor / open / confirmed; issue key: hyphal-tip-graph-scope.

All five constituent edges are parthood statements and the final edge attaches a whole-structure function. The MECHANISTIC label and mechanism title imply a causal explanation that the graph does not encode.

## Recommended Actions And Acceptance Checks

### A1

Retain the exact supported fungal-tip definition, or add directly relevant evidence and explicit taxon/architecture qualifications for the expanded scope. Preserve the supported Neurospora observations and distinguish prior fungal comparisons.

- Do not claim that the lack of an oomycete mention proves biological absence.
- Ensure every retained defining taxon/mechanistic extension is supported by an actually inspected source.
- Preserve supported source-specific claims and pass applicable native gates.

### A2

Mark the current graph NONMECHANISTIC and describe its spatial/function scope, or add only directly sourced causal steps if a separate authorized curation establishes them.

- Preserve the valid component identities, regional parthood and polarity function.
- Preserve supported source-specific claims and pass applicable native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/hyphal_tip.yaml; Entire maintained record, including all evidence, examples, graphs, history and discussions | context_only | Every maintained field was read. Historical curation statements are not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent/ProteinExample, essentiality, PresenceEnum and graph-scope contracts | context_only | Formation necessity differs from activity, viability and observed membership. COMMON means present in most members, with losses the exception; it is not redefined as merely observed occurrence. |
| curation | docs/CURATION.md; Component grounding, including REVIEWED_LABEL_ONLY at159–160 | context_only | An exact full-family mapping is distinct from a shared domain or broader paralog class; label-only does not mean merely uncurated this pass. |
| complex57-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000133,GO:0000228,GO:0001411,GO:0004176,GO:0005743,GO:0006338,GO:0030427,GO:0031011,GO:0031521,GO:0031562,GO:0031942,GO:0051286,GO:0097346,GO:0098800; Complete target-relevant definitions/synonyms and typed relationships in the combined response; unrelated entries are not attributed to this target | supports | GO0001411 defines the end of a fungal hypha where polarized growth occurs; its definition does not add oomycetes. GO0030427/0051286 identify the two broader regions, and GO0031521/0031562 distinguish Spitzenkorper and hyphal-tip polarisome. |
| complex57-agent-go-0001411-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001411/ancestors?relations=is_a; Complete is_a-only ancestor response | supports | The is_a-only ancestor response supports the maintained parent classification. It does not prove parthood, formation requirements or taxonomic prevalence. |
| complex57-agent-tax-367110 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/367110; Complete ENA taxonomy identity/names/lineage | supports | Taxon367110 is Neurospora crassa OR74A, rank strain; native names and lineage establish this exact organism. |
| complex57-agent-tax-5141 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5141; Complete ENA taxonomy identity/names/lineage | supports | Taxon5141 is Neurospora crassa, rank species; native names and lineage establish this exact organism. |
| complex57-agent-protein-Q7RVZ1 | https://rest.uniprot.org/uniprotkb/Q7RVZ1.json; Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references | supports | UniProtKB unreviewed (TrEMBL): Q7RVZ1, Actin-interacting protein; primary genes bud6, synonyms none, taxon367110. Native comments retain their own experimental/inferred evidence qualifiers; the response independently supplies its family cross-references. |
| complex57-agent-protein-Q7RWH7 | https://rest.uniprot.org/uniprotkb/Q7RWH7.json; Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references | supports | UniProtKB unreviewed (TrEMBL): Q7RWH7, Cytokinesis protein sepA; primary genes bni1, synonyms none, taxon367110. Native comments retain their own experimental/inferred evidence qualifiers; the response independently supplies its family cross-references. |
| complex57-agent-protein-V5IQM7 | https://rest.uniprot.org/uniprotkb/V5IQM7.json; Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references | supports | UniProtKB unreviewed (TrEMBL): V5IQM7, Spa2-like protein; primary genes spa2, synonyms none, taxon367110. Native comments retain their own experimental/inferred evidence qualifiers; the response independently supplies its family cross-references. |
| complex57-agent-doi-10.1371_journal.pone.0030372 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pone.0030372%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract | supports | Exact DOI/MED identity: Comparative live-cell imaging analyses of SPA-2, BUD-6 and BNI-1 in Neurospora crassa reveal novel features of the filamentous fungal polarisome. Lichius A, Yáñez-Gutiérrez ME, Read ND, Castro-Longoria E. (2012), PMID22291944. Complete native abstract read. |
| neighbor | data/structures/other/hyphal_tip_polarisome.yaml; Entire frozen neighboring region/complex record | context_only | The two-record boundary set separates the encompassing hyphal-tip region from its polarisome. The neighbor is maintained context, not independent biological evidence. |
| complex57-agent-PMC3265482-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3265482/fullTextXML; Complete Introduction s1/Table1; Results s2a,b,e,f,i,j,k,l,n,o with embedded captions/Tables; Discussion s3a,b,c,d,e,g; all Methods s4. No figure pixels, videos or supplements. | supports | Lichius2012 live imaging and deletion analyses distinguish SPA-2 partial Spitzenkorper overlap, the BUD-6 subapical cloud and BNI-1 apical cap/core. BUD-6/BNI-1 deletion disrupts Spitzenkorper development but residual polarized growth remains. N150/FGSC9013 and Table2-derived strains are distinguished; ectopic BUD-6 did not formally rescue the aconidial deletion, while BNI-1 complementation was tested. Candida/Ashbya comparisons are prior-literature context, not the Neurospora experiment. |
| complex57-agent-ipr-IPR039892 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039892/; Native entry name/type, descriptions/curation flags and signatures; example membership is independently supplied by UniProt | supports | Spa2/Sph1 is a shared full-family class spanning distinct paralogs, not an exact identifier for the retained Neurospora Spa2 cohort. |
| complex57-agent-ipr-IPR051825 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051825/; Native entry name/type, descriptions/curation flags and signatures; example membership is independently supplied by UniProt | supports | SRCIN1/Bud6-related family metadata covers a broader class. Its LLM-unchecked descriptive prose is not treated as primary biological evidence for this localized cohort. |
| complex57-agent-ipr-IPR051661 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051661/; Native entry name/type, descriptions/curation flags and signatures; example membership is independently supplied by UniProt | supports | The actin-filament-regulator family is broader than the retained BNI-1 localized class. LLM-unchecked prose and shared domains do not establish an exact source-neutral BNI-1 family mapping. |
| schema-result | just validate data/structures/other/hyphal_tip.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/hyphal_tip.yaml |
| strict-result | just validate-strict data/structures/other/hyphal_tip.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hyphal_tip-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/hyphal_tip.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hyphal_tip-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hyphal_tip-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/hyphal_tip.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/hyphal_tip.yaml  (GO:0001411)<br>  hyphal_tip_mechanism	spa2_scaffold	COVERED	-&gt;spa2_scaffold (UniProtKB:V5IQM7)<br>  hyphal_tip_mechanism	bud6_actin_associated_polarity_protein	COVERED	-&gt;bud6_actin_associated_polarity_protein (UniProtKB:Q7RVZ1)<br>  hyphal_tip_mechanism	bni1_formin	COVERED	-&gt;bni1_formin (UniProtKB:Q7RWH7)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/hyphal_tip.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/hyphal_tip.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 12 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five completed same-base batch26 global gates are integrated with exact manifest/input/log hashes verified. No fresh full-site QC is claimed from the sparse B57 checkout.
- Only the source sections and assets explicitly enumerated in evidence locators were inspected; no unlisted supplements or atomic coordinates were analyzed.
- The broader Candida/Ashbya comparisons were read as Lichius introductory/discussion context; their cited primary experiments were not independently retrieved.
- No universal three-protein formation requirement or complete fungal/oomycete prevalence survey is inferred from the Neurospora deletion/imaging experiments.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes both clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T074200Z-hyphal-tip-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Hyphal tip scientific review
started_at: '2026-10-22T07:12:47Z'
finished_at: '2026-10-22T07:42:00Z'
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
summary: The fungal/Neurospora tip identity and localized protein observations are
  supported. One major concerns the unsupported expanded defining scope; one minor
  corrects a spatial graph labeled mechanistic.
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
  - path: data/structures/other/hyphal_tip.yaml
    sha256: d33af9efa38fa45e9d44a06739b952ee6c2b009b85d597f51b8e981084c3c7d4
    role: target
  - path: data/structures/other/hyphal_tip_polarisome.yaml
    sha256: 69417314e33e5f9ef62038f48149ff6a8099a77ca45c1227b8bb6d52ac269667
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
- target_id: GO:0001411
  path: data/structures/other/hyphal_tip.yaml
  label: hyphal tip
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target plus frozen guidance, protein-example
    skill and, for the hyphal pair, the other frozen region/complex neighbor. Actual
    source-reading extents appear per evidence row.
  selection: Target 7 of batch57, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0001411
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: just validate data/structures/other/hyphal_tip.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: just validate-strict data/structures/other/hyphal_tip.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hyphal_tip-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hyphal_tip.yaml --causal-graphs
  exit_code: 0
  summary: Native focused check passed; biological claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hyphal_tip.yaml --verify
  exit_code: 0
  summary: Native focused check passed; biological claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0001411
  summary: No expression-module inference is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0001411
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex57-agent-go
  - complex57-agent-go-0001411-ancestors
  - complex57-agent-tax-367110
  - complex57-agent-tax-5141
  - complex57-agent-protein-Q7RVZ1
  - complex57-agent-protein-Q7RWH7
  - complex57-agent-protein-V5IQM7
  - complex57-agent-doi-10.1371_journal.pone.0030372
  - neighbor
  - complex57-agent-PMC3265482-xml
  - complex57-agent-ipr-IPR039892
  - complex57-agent-ipr-IPR051825
  - complex57-agent-ipr-IPR051661
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0001411
  summary: 12 of 12 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0001411
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
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/hyphal_tip.yaml
  locator: Entire maintained record, including all evidence, examples, graphs, history
    and discussions
  accessed_at: '2026-10-22T07:28:35Z'
  support: context_only
  summary: Every maintained field was read. Historical curation statements are not
    independent biological evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent/ProteinExample, essentiality, PresenceEnum and graph-scope
    contracts
  accessed_at: '2026-10-22T07:28:35Z'
  support: context_only
  summary: Formation necessity differs from activity, viability and observed membership.
    COMMON means present in most members, with losses the exception; it is not redefined
    as merely observed occurrence.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding, including REVIEWED_LABEL_ONLY at159–160
  accessed_at: '2026-10-22T07:28:35Z'
  support: context_only
  summary: An exact full-family mapping is distinct from a shared domain or broader
    paralog class; label-only does not mean merely uncurated this pass.
- evidence_id: complex57-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000133,GO:0000228,GO:0001411,GO:0004176,GO:0005743,GO:0006338,GO:0030427,GO:0031011,GO:0031521,GO:0031562,GO:0031942,GO:0051286,GO:0097346,GO:0098800
  locator: Complete target-relevant definitions/synonyms and typed relationships in
    the combined response; unrelated entries are not attributed to this target
  accessed_at: '2026-10-22T07:19:38.382591Z'
  support: supports
  summary: GO0001411 defines the end of a fungal hypha where polarized growth occurs;
    its definition does not add oomycetes. GO0030427/0051286 identify the two broader
    regions, and GO0031521/0031562 distinguish Spitzenkorper and hyphal-tip polarisome.
  snapshot_sha256: 6952f2a5328b5e824e0506235219b200a620006b8f5dc429ebc31e24f9c2639e
- evidence_id: complex57-agent-go-0001411-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001411/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response
  accessed_at: '2026-10-22T07:19:49.855585Z'
  support: supports
  summary: The is_a-only ancestor response supports the maintained parent classification.
    It does not prove parthood, formation requirements or taxonomic prevalence.
  snapshot_sha256: 33ac2cae2d1346a8490cee7c367c2cddcafe714f1e5291b63404b9ad3bfef268
- evidence_id: complex57-agent-tax-367110
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/367110
  locator: Complete ENA taxonomy identity/names/lineage
  accessed_at: '2026-10-22T07:19:44.188968Z'
  support: supports
  summary: Taxon367110 is Neurospora crassa OR74A, rank strain; native names and lineage
    establish this exact organism.
  snapshot_sha256: dd0434eb4bcbe24c5370acfef3359c9df4da5f31bbaca0f3ba6244a610189199
- evidence_id: complex57-agent-tax-5141
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5141
  locator: Complete ENA taxonomy identity/names/lineage
  accessed_at: '2026-10-22T07:19:44.774519Z'
  support: supports
  summary: Taxon5141 is Neurospora crassa, rank species; native names and lineage
    establish this exact organism.
  snapshot_sha256: 574584705a280fad9f1e98d4f83398508b511c50023ca90be837a4a72c20911c
- evidence_id: complex57-agent-protein-Q7RVZ1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q7RVZ1.json
  locator: Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references
  accessed_at: '2026-10-22T07:19:42.986422Z'
  support: supports
  summary: 'UniProtKB unreviewed (TrEMBL): Q7RVZ1, Actin-interacting protein; primary
    genes bud6, synonyms none, taxon367110. Native comments retain their own experimental/inferred
    evidence qualifiers; the response independently supplies its family cross-references.'
  snapshot_sha256: 73f599a7a5301dd84f4cc2c6e34cdd427139009880223ef6442ba39b3c6adfa2
- evidence_id: complex57-agent-protein-Q7RWH7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q7RWH7.json
  locator: Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references
  accessed_at: '2026-10-22T07:19:43.346255Z'
  support: supports
  summary: 'UniProtKB unreviewed (TrEMBL): Q7RWH7, Cytokinesis protein sepA; primary
    genes bni1, synonyms none, taxon367110. Native comments retain their own experimental/inferred
    evidence qualifiers; the response independently supplies its family cross-references.'
  snapshot_sha256: 368ebdd6ae660b7568fafba5f8c8dd2bf302041f2123b41d14697d8d58ecd9b5
- evidence_id: complex57-agent-protein-V5IQM7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/V5IQM7.json
  locator: Accession/status/name/all gene tokens/organism; FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references
  accessed_at: '2026-10-22T07:19:43.402796Z'
  support: supports
  summary: 'UniProtKB unreviewed (TrEMBL): V5IQM7, Spa2-like protein; primary genes
    spa2, synonyms none, taxon367110. Native comments retain their own experimental/inferred
    evidence qualifiers; the response independently supplies its family cross-references.'
  snapshot_sha256: ee0cede8d78b4605032c09e5eb113255b2af4426d1005ad625f61459fdb505d5
- evidence_id: complex57-agent-doi-10.1371_journal.pone.0030372
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pone.0030372%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-22T07:19:49.682203Z'
  support: supports
  summary: 'Exact DOI/MED identity: Comparative live-cell imaging analyses of SPA-2,
    BUD-6 and BNI-1 in Neurospora crassa reveal novel features of the filamentous
    fungal polarisome. Lichius A, Yáñez-Gutiérrez ME, Read ND, Castro-Longoria E.
    (2012), PMID22291944. Complete native abstract read.'
  snapshot_sha256: 5909bb1acc260ea2a77b463821f9be615cdfa7dd6afc2c59c4bf1198dced8b7b
- evidence_id: neighbor
  kind: record_content
  reference: data/structures/other/hyphal_tip_polarisome.yaml
  locator: Entire frozen neighboring region/complex record
  accessed_at: '2026-10-22T07:28:35Z'
  support: context_only
  summary: The two-record boundary set separates the encompassing hyphal-tip region
    from its polarisome. The neighbor is maintained context, not independent biological
    evidence.
- evidence_id: complex57-agent-PMC3265482-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3265482/fullTextXML
  locator: Complete Introduction s1/Table1; Results s2a,b,e,f,i,j,k,l,n,o with embedded
    captions/Tables; Discussion s3a,b,c,d,e,g; all Methods s4. No figure pixels, videos
    or supplements.
  accessed_at: '2026-10-22T07:20:38.549284Z'
  support: supports
  summary: Lichius2012 live imaging and deletion analyses distinguish SPA-2 partial
    Spitzenkorper overlap, the BUD-6 subapical cloud and BNI-1 apical cap/core. BUD-6/BNI-1
    deletion disrupts Spitzenkorper development but residual polarized growth remains.
    N150/FGSC9013 and Table2-derived strains are distinguished; ectopic BUD-6 did
    not formally rescue the aconidial deletion, while BNI-1 complementation was tested.
    Candida/Ashbya comparisons are prior-literature context, not the Neurospora experiment.
  snapshot_sha256: 281f73a0f66fcac1d984a991311c6b3d8764e788c99972206f5faea072f3187d
- evidence_id: complex57-agent-ipr-IPR039892
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039892/
  locator: Native entry name/type, descriptions/curation flags and signatures; example
    membership is independently supplied by UniProt
  accessed_at: '2026-10-22T07:20:40.110049Z'
  support: supports
  summary: Spa2/Sph1 is a shared full-family class spanning distinct paralogs, not
    an exact identifier for the retained Neurospora Spa2 cohort.
  snapshot_sha256: 6476f3f836012c74087ca05a1402415a40723e51e74135035b060d96fafabc01
- evidence_id: complex57-agent-ipr-IPR051825
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051825/
  locator: Native entry name/type, descriptions/curation flags and signatures; example
    membership is independently supplied by UniProt
  accessed_at: '2026-10-22T07:20:40.458304Z'
  support: supports
  summary: SRCIN1/Bud6-related family metadata covers a broader class. Its LLM-unchecked
    descriptive prose is not treated as primary biological evidence for this localized
    cohort.
  snapshot_sha256: 34dc77dcf99b4747caa75d530205831b3d9edd66f5e4df7833319637fb3bb245
- evidence_id: complex57-agent-ipr-IPR051661
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051661/
  locator: Native entry name/type, descriptions/curation flags and signatures; example
    membership is independently supplied by UniProt
  accessed_at: '2026-10-22T07:20:40.490048Z'
  support: supports
  summary: The actin-filament-regulator family is broader than the retained BNI-1
    localized class. LLM-unchecked prose and shared domains do not establish an exact
    source-neutral BNI-1 family mapping.
  snapshot_sha256: babdb17855c5f01a4a0410ef193cff0c2e95c9eaafe0dfda2a58b7bad3b33e04
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/hyphal_tip.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:12:48Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/hyphal_tip.yaml'
  snapshot_sha256: 2582921561077dcd47952fabc83223449280edaf929fe5bc99e1fa143ccbfdf2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/hyphal_tip.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hyphal_tip-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:12:49Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/hyphal_tip.yaml\
    \ --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hyphal_tip-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hyphal_tip-strict.tsv"
  snapshot_sha256: e41afc3ffef6ee9861c9b503269589ad54103d2b0f78b3bde26f1ebe51398a73
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hyphal_tip.yaml --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T07:19:55.194361Z'
  support: supports
  summary: "data/structures/other/hyphal_tip.yaml  (GO:0001411)\n  hyphal_tip_mechanism\t\
    spa2_scaffold\tCOVERED\t->spa2_scaffold (UniProtKB:V5IQM7)\n  hyphal_tip_mechanism\t\
    bud6_actin_associated_polarity_protein\tCOVERED\t->bud6_actin_associated_polarity_protein\
    \ (UniProtKB:Q7RVZ1)\n  hyphal_tip_mechanism\tbni1_formin\tCOVERED\t->bni1_formin\
    \ (UniProtKB:Q7RWH7)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 91cc237750b3f3b8f5dfa2f9942ef9989f97cd12bb602529c105cf1290bc4896
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hyphal_tip.yaml --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T07:19:56.814845Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/hyphal_tip.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 12 of 12 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
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
  topic: Fungal tip region and localized polarisome boundary
  outcome: supported
  target_ids:
  - GO:0001411
  summary: The exact native identities, parents and the frozen region/complex distinction
    agree. Source imaging supports the mature Neurospora apical architecture without
    equating every fungal polarisome to a single Spitzenkorper geometry.
  evidence_ids:
  - record
  - neighbor
  - complex57-agent-go
  - complex57-agent-go-0001411-ancestors
  - complex57-agent-PMC3265482-xml
- assessment_id: proteins
  area: grounding
  topic: Three taxon-paired proteins and bounded family candidates
  outcome: supported
  target_ids:
  - GO:0001411
  summary: All three examples are correctly unreviewed OR74A proteins with the stated
    primary genes. Primary membership/localization comes from Lichius, not accession
    identity alone. The inspected broader families do not resolve the exact retained
    classes; no forced family mapping follows.
  evidence_ids:
  - record
  - curation
  - complex57-agent-PMC3265482-xml
  - complex57-agent-protein-Q7RVZ1
  - complex57-agent-protein-Q7RWH7
  - complex57-agent-protein-V5IQM7
  - complex57-agent-ipr-IPR039892
  - complex57-agent-ipr-IPR051825
  - complex57-agent-ipr-IPR051661
- assessment_id: scope
  area: scope
  topic: Mature Neurospora hyphae and broader fungal comparisons
  outcome: supported
  target_ids:
  - GO:0001411
  summary: COMMON retains its majority/losses-exception meaning. The qualitative species-level
    characterization supports the chosen Neurospora model context, without a measured
    prevalence census or a claim that every growth stage has a visible Spitzenkorper.
    OR74A reference protein identity is separate from each transformed experimental
    strain.
  evidence_ids:
  - record
  - schema
  - complex57-agent-PMC3265482-xml
  - complex57-agent-tax-367110
  - complex57-agent-tax-5141
  - complex57-agent-protein-Q7RVZ1
  - complex57-agent-protein-Q7RWH7
  - complex57-agent-protein-V5IQM7
- assessment_id: formation
  area: grounding
  topic: Tip-growth defects versus formation requirements
  outcome: unknown
  target_ids:
  - GO:0001411
  summary: The deletion data directly support conditional architecture/growth phenotypes.
    They do not establish that the encompassing tip or every partial polarisome fails
    to form without each named protein; polarized growth can persist without a detectable
    Spitzenkorper. The three CONDITIONAL fields therefore retain unresolved formation-specific
    scope rather than being redefined as catalytic or growth necessity.
  evidence_ids:
  - record
  - schema
  - complex57-agent-PMC3265482-xml
- assessment_id: definition
  area: scope
  topic: Unestablished extension from fungal GO identity to oomycetes
  outcome: concern
  target_ids:
  - GO:0001411
  summary: The maintained definition adds oomycete occurrence and a broad mechanistic
    description beyond its sole GO source. GO explicitly defines a fungal tip; the
    directly inspected paper concerns Neurospora and compares other fungi. Its complete
    retained JATS contains no oomycete mention. This does not prove oomycetes lack
    apical growth, but the broader defining taxonomic assertion is not established
    by the cited sources.
  evidence_ids:
  - record
  - complex57-agent-go
  - complex57-agent-PMC3265482-xml
- assessment_id: graph
  area: graph
  topic: Spatial membership presented as a mechanism
  outcome: concern
  target_ids:
  - GO:0001411
  summary: The graph contains protein/substructure parthood and a whole-region mediates-function
    edge. Those source-supported statements form a coarse topology/function summary
    without a causal transition or assembly step; its MECHANISTIC label overstates
    what is encoded.
  evidence_ids:
  - record
  - schema
  - complex57-agent-go
  - complex57-agent-PMC3265482-xml
- assessment_id: coverage
  area: completeness
  topic: Whole maintained target and declared source coverage
  outcome: supported
  target_ids:
  - GO:0001411
  summary: Every maintained field, evidence note, graph claim and discussion was inspected
    at the declared source extents. Empty optional slots, acknowledged unknowns and
    broader-family candidates do not independently create findings.
  evidence_ids:
  - record
  - schema
  - curation
  - complex57-agent-go
findings:
- finding_id: F1
  issue_key: hyphal-tip-definition-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Source and qualify the expanded hyphal-tip definition
  description: The fungal GO identity is extended in the maintained defining text
    to oomycetes and generalized apparatus mechanisms while definition_source remains
    GO0001411. The exact GO definition and the cited Neurospora primary study do not
    establish that cross-lineage defining scope.
  target_ids:
  - GO:0001411
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - record
  - complex57-agent-go
  - complex57-agent-PMC3265482-xml
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: major
  normalization_reason: The unsupported assertion changes the biological scope of
    the defining class, not merely a citation format. Exact GO identity remains intact,
    but it does not validate the added cross-lineage definition.
- finding_id: F2
  issue_key: hyphal-tip-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Label the spatial graph as nonmechanistic
  description: All five constituent edges are parthood statements and the final edge
    attaches a whole-structure function. The MECHANISTIC label and mechanism title
    imply a causal explanation that the graph does not encode.
  target_ids:
  - GO:0001411
  field_paths:
  - causal_graphs#hyphal_tip_mechanism.scope_status
  - causal_graphs#hyphal_tip_mechanism.title
  evidence_ids:
  - record
  - schema
  - complex57-agent-PMC3265482-xml
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: minor
  normalization_reason: A bounded correction preserves the supported structure identity
    and source-specific biology.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0001411
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip.yaml
    role: maintained scientific record
  description: Retain the exact supported fungal-tip definition, or add directly relevant
    evidence and explicit taxon/architecture qualifications for the expanded scope.
    Preserve the supported Neurospora observations and distinguish prior fungal comparisons.
  acceptance_checks:
  - Do not claim that the lack of an oomycete mention proves biological absence.
  - Ensure every retained defining taxon/mechanistic extension is supported by an
    actually inspected source.
  - Preserve supported source-specific claims and pass applicable native gates.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0001411
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip.yaml
    role: maintained scientific record
  description: Mark the current graph NONMECHANISTIC and describe its spatial/function
    scope, or add only directly sourced causal steps if a separate authorized curation
    establishes them.
  acceptance_checks:
  - Preserve the valid component identities, regional parthood and polarity function.
  - Preserve supported source-specific claims and pass applicable native gates.
limitations:
- All five completed same-base batch26 global gates are integrated with exact manifest/input/log
  hashes verified. No fresh full-site QC is claimed from the sparse B57 checkout.
- Only the source sections and assets explicitly enumerated in evidence locators were
  inspected; no unlisted supplements or atomic coordinates were analyzed.
- The broader Candida/Ashbya comparisons were read as Lichius introductory/discussion
  context; their cited primary experiments were not independently retrieved.
- No universal three-protein formation requirement or complete fungal/oomycete prevalence
  survey is inferred from the Neurospora deletion/imaging experiments.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes both clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
