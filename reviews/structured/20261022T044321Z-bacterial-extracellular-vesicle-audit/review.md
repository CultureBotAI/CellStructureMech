# Source-backed review of bacterial extracellular vesicle

- Review: 20261022T044321Z-bacterial-extracellular-vesicle-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:25:29Z
- Finished UTC: 2026-10-22T04:43:21Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The bacterial-vesicle identity, composite components, scoped occurrence, S. aureus example and descriptive cargo graph are supported. One minor definition-scope clarification is needed; three cited papers were checked at complete native-abstract scope only.

## Scope And Provenance

Exactly one complete target; no neighboring scientific-record verdict is imported. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch45 fixed strict path order, index 4; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097691 | data/structures/other/bacterial_extracellular_vesicle.yaml | maintained | bacterial extracellular vesicle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0097691 | Focused validator passed. |
| Focused native strict | passed | True | GO:0097691 | Focused validator passed. |
| Focused native graphs | passed | True | GO:0097691 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:0097691 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0097691 | 7 of 8 collected target identifiers returned OK. DOI:10.1016/j.semcdb.2015.02.006: UNREACHABLE; Exact DOI, MED25704309, title and author metadata were inspected in the native Europe PMC result after failed DOI resolver transport. This establishes bibliographic identity and declared abstract scope, without certifying unaccessed full text. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0097691 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097691 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097691 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097691 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0097691 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact authority and literature-expanded boundary

identity: concern. Targets: GO:0097691.

GO:0097691, SL-0489 and extracellular-vesicle parentage identify the intended bacterial vesicle class. The historical synonym exclusion is sound. The verbatim authority definition describes plasma-membrane budding whereas current components, scope notes and literature explicitly encompass other origins; F1 requests that this distinction be visible rather than silently broadening the authority definition.

### Mixed membrane and variable cargo

grounding: supported. Targets: GO:0097691.

Both OTHER component rows accurately denote composite structures/material pools; neither claims a false single chemical or protein family. The membrane role and inside-or-surface cargo distinction match the retained authorities/review abstracts. No unique exact molecular CURIE was established for either entire heterogeneous pool, so REVIEWED_LABEL_ONLY and the bounded grounding TODO remain justified.

### Constitutional boundary versus cargo necessity

scope: supported. Targets: GO:0097691.

A bounding membrane is constitutional to the membrane-vesicle class, so its collective ESSENTIAL label does not assert that each lipid or membrane protein is required. Cargo remains UNKNOWN; the inspected evidence does not establish formation necessity of any particular cargo or individual membrane constituent.

### Bacterial occurrence and canonical organism

scope: supported. Targets: GO:0097691.

Taxon2 is Bacteria at domain rank, and1280 is Staphylococcus aureus. VARIABLE explicitly leaves species/condition dependence open. Kim/Toyofuku support Gram-negative and Gram-positive vesicle scope; Lee2009 complete primary abstract reports S. aureus vesicle production and90 identified protein components, supporting the modest example. No strain-specific method or prevalence census is inferred.

### Cargo carriage and interactions

evidence: supported. Targets: GO:0097691.

The broadly worded delivery function is supported by the review abstracts and native location description. It does not require all cargo to be luminal, all vesicles to share one production pathway or every experimental system to demonstrate every interaction.

### Two-edge descriptive function graph

graph: supported. Targets: GO:0097691.

The graph is explicitly NONMECHANISTIC: vesicle carries heterogeneous cargo and composite membrane is part of vesicle. It avoids equating all cargo with lumen contents or asserting a universal molecular release mechanism. Component references and node identities match the two current components.

### Complete target and bounded evidence

completeness: supported. Targets: GO:0097691.

All maintained fields, historical entries and discussions were read. Empty optional molecular inventories, images or dimensions do not establish defects. Historical review corrections are retained as record context rather than independent scientific proof. Paper identities/complete native abstracts are verified, with actual body-access failures kept distinct.

## Findings

### F1: Distinguish the authority definition from the broader vesicle-origin scope

minor / open / confirmed; issue key: CellStructureMech-bacterial_extracellular_vesicle-authority-definition-origin-scope.

The definition, attributed solely to GO:0097691, describes plasma-membrane budding. It is faithfully copied from GO/SL, but the same record explicitly includes outer-membrane, outer-inner-membrane and Gram-positive vesicles and says several release pathways. Toyofuku2019 complete abstract expressly includes outer-membrane blebbing and lysis-derived routes. Readers need an explicit source-qualified scope note reconciling the narrow authority wording with the broader current record; this is not a claim that the copied GO definition or observed vesicle classes are fabricated.

## Recommended Actions And Acceptance Checks

### A1

Preserve the exact authority provenance, and qualify the definition or add a definition-adjacent literature-backed note explaining that the record covers multiple bacterial vesicle origins beyond plasma-membrane budding. Keep the nonmechanistic graph and cargo boundary.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/bacterial_extracellular_vesicle.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic or transport function. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| micro45-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097691,GO:0061701,GO:1903561,GO:0009279,GO:1990063,GO:0106234; results: exact id/name/isObsolete/definition/synonyms/children for GO:0097691, GO:0061701, GO:1903561 and GO:0009279; other returned terms are not used here. | supports | Active GO:0097691 and GO:0061701 match the two distinct bacterial-vesicle labels/definitions; GO:1903561 lists both as is_a children. GO:0009279 identifies the Gram-negative outer membrane. The native BEV definition specifically says plasma-membrane budding; it does not itself express the broader literature origins. |
| micro45-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro45-tax1280 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1280; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 1280 identifies Staphylococcus aureus at rank species; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro45-toyofuku2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41579-018-0112-2%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED30397270: Types and origins of bacterial membrane vesicles. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. Its complete review abstract explicitly distinguishes outer-membrane blebbing, Gram-positive/other vesicle types and endolysin-triggered lysis; this is secondary synthesis, not a new experiment. |
| micro45-SL0489 | https://rest.uniprot.org/locations/SL-0489.json; Complete native location identity/definition/synonyms/geneOntology/parents; usage statistics not interpreted as biological prevalence. | supports | SL-0489 names Bacterial extracellular vesicle, maps to GO:0097691 and supplies the bacterial membrane vesicle synonym; parent EV/vesicle entries and the plasma-membrane-budding definition were inspected. Generic membrane-vesicle/microvesicle labels are not thereby exact bacterial-only synonyms. |
| micro45-kim2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.semcdb.2015.02.006%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED25704309: Gram-negative and Gram-positive bacterial extracellular vesicles. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-lee2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1002%2Fpmic.200900338%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED19834908: Gram-positive bacteria produce membrane vesicles: proteomics-based characterization of Staphylococcus aureus-derived membrane vesicles. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro45-toyofuku2019-publisher | https://doi.org/10.1038/s41579-018-0112-2; Complete retained response; status/content inspected against receipt. | context_only | HTTP 200 returned a 3038-byte Client Challenge HTML page, not the paper body. Metadata/abstract or a separately specified genuine body is used instead. |
| micro45-toyofuku2019-nature | https://www.nature.com/articles/s41579-018-0112-2; Complete retained response; status/content inspected against receipt. | context_only | HTTP 200 returned a 3038-byte Client Challenge HTML page, not the paper body. Metadata/abstract or a separately specified genuine body is used instead. |
| micro45-kim2015-publisher | https://doi.org/10.1016/j.semcdb.2015.02.006; Complete retained response; status/content inspected against receipt. | context_only | Native request failed at TLS transport; the retained error bytes are not a paper body. Metadata/abstract or a separately specified genuine body is used instead. |
| micro45-lee2009-publisher | https://doi.org/10.1002/pmic.200900338; Complete retained response; status/content inspected against receipt. | context_only | HTTP 403 returned an access-denied HTML response, not an inspected paper body. Metadata/abstract or a separately specified genuine body is used instead. |
| schema-result | just validate data/structures/other/bacterial_extracellular_vesicle.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/bacterial_extracellular_vesicle.yaml |
| strict-result | just validate-strict data/structures/other/bacterial_extracellular_vesicle.yaml --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/bacterial_extracellular_vesicle-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/bacterial_extracellular_vesicle.yaml --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/bacterial_extracellular_vesicle-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch45-20261022-mptgrq24/bacterial_extracellular_vesicle-strict.tsv |
| native-graphs | /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/bacterial_extracellular_vesicle.yaml; Complete read-only focused native graphs log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/bacterial_extracellular_vesicle.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 7 of 8 collected target identifiers returned OK. DOI:10.1016/j.semcdb.2015.02.006: UNREACHABLE; Exact DOI, MED25704309, title and author metadata were inspected in the native Europe PMC result after failed DOI resolver transport. This establishes bibliographic identity and declared abstract scope, without certifying unaccessed full text. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Toyofuku2019 native publisher routes returned Client Challenge HTML despite HTTP200; Kim2015 failed TLS; Lee2009 publisher returned403. Only their complete native MED metadata/abstracts were read, not main bodies, figures, supplements or strain-level methods.
- No primary vesicle pixels, purified constituent stoichiometry, taxon-wide frequency census or individual membrane/cargo formation-depletion experiments were reviewed.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these complex identity, protein family, assembly, vesicle carriage and enzyme or transport claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T044321Z-bacterial-extracellular-vesicle-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of bacterial extracellular vesicle
started_at: '2026-10-22T04:25:29Z'
finished_at: '2026-10-22T04:43:21Z'
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
summary: The bacterial-vesicle identity, composite components, scoped occurrence,
  S. aureus example and descriptive cargo graph are supported. One minor definition-scope
  clarification is needed; three cited papers were checked at complete native-abstract
  scope only.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/other/bacterial_extracellular_vesicle.yaml
    sha256: 43f0f6e0dfef8fc8533bbbac4c5a1583adc6626873f52b92f2edbc32560137d2
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
- target_id: GO:0097691
  path: data/structures/other/bacterial_extracellular_vesicle.yaml
  label: bacterial extracellular vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_extracellular_vesicle.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; no neighboring scientific-record verdict
    is imported. Exact authority, all current component/function/graph/source placements,
    taxonomic scope, formation semantics, history and discussions were reviewed.
  selection: Batch45 fixed strict path order, index 4; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097691
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: just validate data/structures/other/bacterial_extracellular_vesicle.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: just validate-strict data/structures/other/bacterial_extracellular_vesicle.yaml
    --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/bacterial_extracellular_vesicle-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-graphs
  name: Focused native graphs
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/bacterial_extracellular_vesicle.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0097691
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - micro45-go
  - micro45-tax2
  - micro45-tax1280
  - micro45-toyofuku2019-meta
  - micro45-SL0489
  - micro45-kim2015-meta
  - micro45-lee2009-meta
  - micro45-toyofuku2019-publisher
  - micro45-toyofuku2019-nature
  - micro45-kim2015-publisher
  - micro45-lee2009-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0097691
  summary: '7 of 8 collected target identifiers returned OK. DOI:10.1016/j.semcdb.2015.02.006:
    UNREACHABLE; Exact DOI, MED25704309, title and author metadata were inspected
    in the native Europe PMC result after failed DOI resolver transport. This establishes
    bibliographic identity and declared abstract scope, without certifying unaccessed
    full text. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro45-kim2015-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0097691
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
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/bacterial_extracellular_vesicle.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:39:23Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:39:23Z'
  support: context_only
  summary: ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite
    class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic
    or transport function.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:39:23Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: micro45-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097691,GO:0061701,GO:1903561,GO:0009279,GO:1990063,GO:0106234
  locator: 'results: exact id/name/isObsolete/definition/synonyms/children for GO:0097691,
    GO:0061701, GO:1903561 and GO:0009279; other returned terms are not used here.'
  accessed_at: '2026-10-22T04:32:21.376534Z'
  support: supports
  summary: Active GO:0097691 and GO:0061701 match the two distinct bacterial-vesicle
    labels/definitions; GO:1903561 lists both as is_a children. GO:0009279 identifies
    the Gram-negative outer membrane. The native BEV definition specifically says
    plasma-membrane budding; it does not itself express the broader literature origins.
  snapshot_sha256: 7039eee9ee3550641584f881c521a22795fc64a1b2b73b12b977d3eb9a8329ba
- evidence_id: micro45-tax2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:32:21.376961Z'
  support: supports
  summary: ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match
    the record. Identity alone is not prevalence or experimental-condition evidence.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: micro45-tax1280
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1280
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:32:21.377169Z'
  support: supports
  summary: ENA taxId 1280 identifies Staphylococcus aureus at rank species; aliases
    and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: 6cc681494899a86cb636a9d82b04dedddb7afe38144e54d017728306a4527776
- evidence_id: micro45-toyofuku2019-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41579-018-0112-2%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:24.609739Z'
  support: supports
  summary: 'Unique MED30397270: Types and origins of bacterial membrane vesicles.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence. Its complete review abstract explicitly distinguishes
    outer-membrane blebbing, Gram-positive/other vesicle types and endolysin-triggered
    lysis; this is secondary synthesis, not a new experiment.'
  snapshot_sha256: c4b47a43c972278d37cd87a70e6ded33d5975974952f841fc79f154f49dfe1f3
- evidence_id: micro45-SL0489
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0489.json
  locator: Complete native location identity/definition/synonyms/geneOntology/parents;
    usage statistics not interpreted as biological prevalence.
  accessed_at: '2026-10-22T04:32:21.377031Z'
  support: supports
  summary: SL-0489 names Bacterial extracellular vesicle, maps to GO:0097691 and supplies
    the bacterial membrane vesicle synonym; parent EV/vesicle entries and the plasma-membrane-budding
    definition were inspected. Generic membrane-vesicle/microvesicle labels are not
    thereby exact bacterial-only synonyms.
  snapshot_sha256: df2cf06d3a65f961f93053c81b9fd2fd82b4ff7bf98ff407caed5cbe3f0b3939
- evidence_id: micro45-kim2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.semcdb.2015.02.006%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:24.696830Z'
  support: supports
  summary: 'Unique MED25704309: Gram-negative and Gram-positive bacterial extracellular
    vesicles. Authors/year/DOI and the complete native abstract were inspected. This
    row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 6954f646fc25ac999bcbaef4ce8f45cc887506198c07d764b80dca3ef13a1a9f
- evidence_id: micro45-lee2009-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1002%2Fpmic.200900338%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:32:25.263744Z'
  support: supports
  summary: 'Unique MED19834908: Gram-positive bacteria produce membrane vesicles:
    proteomics-based characterization of Staphylococcus aureus-derived membrane vesicles.
    Authors/year/DOI and the complete native abstract were inspected. This row establishes
    bibliographic identity and abstract-level content only; detailed experiments require
    separately specified body evidence.'
  snapshot_sha256: 91025ec6cb90bef3dec0b39fb177720d48aff998d8e6e67fd21dfd9c2b65bc40
- evidence_id: micro45-toyofuku2019-publisher
  kind: authority
  reference: https://doi.org/10.1038/s41579-018-0112-2
  locator: Complete retained response; status/content inspected against receipt.
  accessed_at: '2026-10-22T04:32:50.863934Z'
  support: context_only
  summary: HTTP 200 returned a 3038-byte Client Challenge HTML page, not the paper
    body. Metadata/abstract or a separately specified genuine body is used instead.
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: micro45-toyofuku2019-nature
  kind: authority
  reference: https://www.nature.com/articles/s41579-018-0112-2
  locator: Complete retained response; status/content inspected against receipt.
  accessed_at: '2026-10-22T04:33:37.075077Z'
  support: context_only
  summary: HTTP 200 returned a 3038-byte Client Challenge HTML page, not the paper
    body. Metadata/abstract or a separately specified genuine body is used instead.
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: micro45-kim2015-publisher
  kind: authority
  reference: https://doi.org/10.1016/j.semcdb.2015.02.006
  locator: Complete retained response; status/content inspected against receipt.
  accessed_at: '2026-10-22T04:32:50.882550Z'
  support: context_only
  summary: Native request failed at TLS transport; the retained error bytes are not
    a paper body. Metadata/abstract or a separately specified genuine body is used
    instead.
  snapshot_sha256: a8014ecefc9b9c4cc3987abe484f64b8ee37dd3e6bc0182a0f12915e702dedb3
- evidence_id: micro45-lee2009-publisher
  kind: authority
  reference: https://doi.org/10.1002/pmic.200900338
  locator: Complete retained response; status/content inspected against receipt.
  accessed_at: '2026-10-22T04:32:50.893503Z'
  support: context_only
  summary: HTTP 403 returned an access-denied HTML response, not an inspected paper
    body. Metadata/abstract or a separately specified genuine body is used instead.
  snapshot_sha256: 7c97b3836e56fe9f6199d4f205457bf3a0922f16c55b28edb0dc47bf762c7f40
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/bacterial_extracellular_vesicle.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:25:30Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/bacterial_extracellular_vesicle.yaml'
  snapshot_sha256: 5d0153221d5b73aeed8fcb46b4fe35337f4eb02dc3f08048c3152875d9650b07
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/bacterial_extracellular_vesicle.yaml
    --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/bacterial_extracellular_vesicle-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:25:32Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/bacterial_extracellular_vesicle.yaml\
    \ --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/bacterial_extracellular_vesicle-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch45-20261022-mptgrq24/bacterial_extracellular_vesicle-strict.tsv"
  snapshot_sha256: c7cf5700e7bc533a6bf6a550550b4fcdb5808f40150792ddf07f46c6a63a3d11
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/bacterial_extracellular_vesicle.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T04:32:56.813551Z'
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
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/bacterial_extracellular_vesicle.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '7 of 8 collected target identifiers returned OK. DOI:10.1016/j.semcdb.2015.02.006:
    UNREACHABLE; Exact DOI, MED25704309, title and author metadata were inspected
    in the native Europe PMC result after failed DOI resolver transport. This establishes
    bibliographic identity and declared abstract scope, without certifying unaccessed
    full text. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
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
  topic: Exact authority and literature-expanded boundary
  outcome: concern
  target_ids:
  - GO:0097691
  summary: GO:0097691, SL-0489 and extracellular-vesicle parentage identify the intended
    bacterial vesicle class. The historical synonym exclusion is sound. The verbatim
    authority definition describes plasma-membrane budding whereas current components,
    scope notes and literature explicitly encompass other origins; F1 requests that
    this distinction be visible rather than silently broadening the authority definition.
  evidence_ids:
  - micro45-go
  - micro45-SL0489
  - micro45-toyofuku2019-meta
  - record
- assessment_id: materials
  area: grounding
  topic: Mixed membrane and variable cargo
  outcome: supported
  target_ids:
  - GO:0097691
  summary: Both OTHER component rows accurately denote composite structures/material
    pools; neither claims a false single chemical or protein family. The membrane
    role and inside-or-surface cargo distinction match the retained authorities/review
    abstracts. No unique exact molecular CURIE was established for either entire heterogeneous
    pool, so REVIEWED_LABEL_ONLY and the bounded grounding TODO remain justified.
  evidence_ids:
  - micro45-go
  - micro45-SL0489
  - micro45-kim2015-meta
  - micro45-toyofuku2019-meta
  - schema
  - curation
  - record
- assessment_id: necessity
  area: scope
  topic: Constitutional boundary versus cargo necessity
  outcome: supported
  target_ids:
  - GO:0097691
  summary: A bounding membrane is constitutional to the membrane-vesicle class, so
    its collective ESSENTIAL label does not assert that each lipid or membrane protein
    is required. Cargo remains UNKNOWN; the inspected evidence does not establish
    formation necessity of any particular cargo or individual membrane constituent.
  evidence_ids:
  - micro45-go
  - micro45-SL0489
  - schema
  - record
- assessment_id: taxa
  area: scope
  topic: Bacterial occurrence and canonical organism
  outcome: supported
  target_ids:
  - GO:0097691
  summary: Taxon2 is Bacteria at domain rank, and1280 is Staphylococcus aureus. VARIABLE
    explicitly leaves species/condition dependence open. Kim/Toyofuku support Gram-negative
    and Gram-positive vesicle scope; Lee2009 complete primary abstract reports S.
    aureus vesicle production and90 identified protein components, supporting the
    modest example. No strain-specific method or prevalence census is inferred.
  evidence_ids:
  - micro45-tax2
  - micro45-tax1280
  - micro45-kim2015-meta
  - micro45-toyofuku2019-meta
  - micro45-lee2009-meta
- assessment_id: function
  area: evidence
  topic: Cargo carriage and interactions
  outcome: supported
  target_ids:
  - GO:0097691
  summary: The broadly worded delivery function is supported by the review abstracts
    and native location description. It does not require all cargo to be luminal,
    all vesicles to share one production pathway or every experimental system to demonstrate
    every interaction.
  evidence_ids:
  - micro45-go
  - micro45-SL0489
  - micro45-kim2015-meta
  - micro45-toyofuku2019-meta
  - record
- assessment_id: graph
  area: graph
  topic: Two-edge descriptive function graph
  outcome: supported
  target_ids:
  - GO:0097691
  summary: 'The graph is explicitly NONMECHANISTIC: vesicle carries heterogeneous
    cargo and composite membrane is part of vesicle. It avoids equating all cargo
    with lumen contents or asserting a universal molecular release mechanism. Component
    references and node identities match the two current components.'
  evidence_ids:
  - micro45-go
  - micro45-SL0489
  - micro45-toyofuku2019-meta
  - record
- assessment_id: coverage
  area: completeness
  topic: Complete target and bounded evidence
  outcome: supported
  target_ids:
  - GO:0097691
  summary: All maintained fields, historical entries and discussions were read. Empty
    optional molecular inventories, images or dimensions do not establish defects.
    Historical review corrections are retained as record context rather than independent
    scientific proof. Paper identities/complete native abstracts are verified, with
    actual body-access failures kept distinct.
  evidence_ids:
  - micro45-lee2009-meta
  - micro45-kim2015-meta
  - micro45-toyofuku2019-meta
  - record
findings:
- finding_id: F1
  issue_key: CellStructureMech-bacterial_extracellular_vesicle-authority-definition-origin-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish the authority definition from the broader vesicle-origin scope
  description: The definition, attributed solely to GO:0097691, describes plasma-membrane
    budding. It is faithfully copied from GO/SL, but the same record explicitly includes
    outer-membrane, outer-inner-membrane and Gram-positive vesicles and says several
    release pathways. Toyofuku2019 complete abstract expressly includes outer-membrane
    blebbing and lysis-derived routes. Readers need an explicit source-qualified scope
    note reconciling the narrow authority wording with the broader current record;
    this is not a claim that the copied GO definition or observed vesicle classes
    are fabricated.
  target_ids:
  - GO:0097691
  field_paths:
  - definition
  - definition_source
  - components[0].grounding_notes
  - causal_graphs[0].scope_notes
  evidence_ids:
  - micro45-go
  - micro45-SL0489
  - micro45-toyofuku2019-meta
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_extracellular_vesicle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: Minor because exact identity, provenance and the multiple-origin
    biology are independently supported and current prose already states the broader
    scope; the required correction makes the authority/literature distinction explicit
    rather than reversing a mechanism or identity.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0097691
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_extracellular_vesicle.yaml
    role: maintained scientific record
  description: Preserve the exact authority provenance, and qualify the definition
    or add a definition-adjacent literature-backed note explaining that the record
    covers multiple bacterial vesicle origins beyond plasma-membrane budding. Keep
    the nonmechanistic graph and cargo boundary.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
limitations:
- Toyofuku2019 native publisher routes returned Client Challenge HTML despite HTTP200;
  Kim2015 failed TLS; Lee2009 publisher returned403. Only their complete native MED
  metadata/abstracts were read, not main bodies, figures, supplements or strain-level
  methods.
- No primary vesicle pixels, purified constituent stoichiometry, taxon-wide frequency
  census or individual membrane/cargo formation-depletion experiments were reviewed.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these complex identity, protein family, assembly,
  vesicle carriage and enzyme or transport claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
