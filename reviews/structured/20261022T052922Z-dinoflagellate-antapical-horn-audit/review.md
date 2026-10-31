# Source-backed review of dinoflagellate antapical horn

- Review: 20261022T052922Z-dinoflagellate-antapical-horn-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:15:52Z
- Finished UTC: 2026-10-22T05:29:22Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: the exact thecate antapical-horn class, direct antapex parent and explicitly inherited hypocone parthood are supported. No consequential target defect was identified.

## Scope And Provenance

Exactly one entire target, with the two frozen apex/antapex/horn neighbors read for boundary context. All current definition, hierarchy/parthood, taxonomy, topology, evidence and discussion claims were assessed; no neighboring verdict is imported.

Selection: Batch49 fixed strict path order, index 9; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097687 | data/structures/other/dinoflagellate_antapical_horn.yaml | maintained | dinoflagellate antapical horn |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0097687 | Focused validator passed. |
| Focused native strict | passed | True | GO:0097687 | Focused validator passed. |
| Focused native graph check | passed | True | GO:0097687 | No GENE_OR_PROTEIN nodes are present. Structure-node identities and topology were checked against native GO separately. |
| Claim-level scientific review | passed | True | GO:0097687 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0097687 | 6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0097687 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097687 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097687 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097687 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0097687 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact narrower horn identity and inherited containment

identity: supported. Targets: GO:0097687.

GO0097687 denotes a horn-shaped antapex limited by the source to thecate species. Its direct parent is GO0097684; the record correctly keeps the specialized horn separate from the general antapex and explicitly marks hypocone containment as inherited. It does not copy the parent’s erroneous anterior wording, so that neighboring definition defect is not duplicated here.

### Three-edge nonmechanistic horn topology

graph: supported. Targets: GO:0097687.

The three structure nodes and three edges distinguish direct horn is-a antapex, parent antapex part-of hypocone, and the resulting inherited horn parthood. The graph explicitly avoids a mechanistic assembly or a supposed independent direct GO edge. These exact claims agree with current child links and history.

### Historical metadata-only Taylor scope is accurate

provenance: supported. Targets: GO:0097687.

The retained paper identifiers and complete native abstract match the record. Publisher XML contains metadata only and the retained article route failed403. The target explicitly limits Taylor to bibliographic corroboration, so an uninspected full paper is neither upgraded to primary anatomical support nor treated as a record defect.

### Restricted Dinophyceae scope with cautious occurrence

scope: supported. Targets: GO:0097687.

Native only_in_taxon2864 and ENA class identity support the dinoflagellate restriction. VARIABLE does not claim universal presence; horn thecate restriction and conditional surface features remain explicit. These authority definitions do not supply a quantitative cross-species census.

### No regional molecular inventory asserted

grounding: supported. Targets: GO:0097687.

No component rows, gene symbols or protein instances are asserted. The historical OPEN discussion requests specifically localized constituents and exact classes; generic cellulose, membrane or whole-cell protein inventories cannot be reassigned to this regional point without direct support. No automatic omission finding is made.

### Formation necessity is not established

grounding: unknown. Targets: GO:0097687.

There are no component essentiality claims to test. Morphological location and taxonomy do not establish molecular assembly necessities or physiological functions, and the review preserves that uncertainty.

### Complete target and source-placement coverage

completeness: supported. Targets: GO:0097687.

All maintained fields, every graph edge/source note, current discussion and historical entry were read. No optional canonical species, protein inventory, physical measure, image or additional causal mechanism is required solely to populate a slot. Source limits and the distinct taxonomic scopes remain explicit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dinoflagellate_antapical_horn.yaml; Entire maintained YAML, including all topology edges, source notes, discussions and historical entries | context_only | The complete target was read; a cited authority is checked for biological consistency as well as verbatim identity. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; CellStructureRecord definition/definition_source; StructuralComponent; EssentialityEnum; taxonomic presence and graph scopes | context_only | A region is distinguished from an assembled molecular complex. Formation necessity is distinct from presence or function; no molecular requirement is inferred for an unspecified inventory. |
| curation | docs/CURATION.md; Exact identity and grounding, scope and evidence placement | context_only | Exact identifiers do not by themselves validate contradictory biological prose. Optional components are not filled with generic regional or whole-cell materials without specific support. |
| graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Nonmechanistic structure topology and explicit edge-level evidence | context_only | Descriptive is-a, parthood and spatial relations can remain NONMECHANISTIC; they do not demonstrate formation or physiological causation. |
| neighbor-dinoflagellate_antapex | data/structures/other/dinoflagellate_antapex.yaml; Entire frozen regional boundary neighbor | context_only | The complete apex/antapex/horn boundary record was read for context. No neighboring verdict is imported as a target defect. |
| neighbor-dinoflagellate_apex | data/structures/other/dinoflagellate_apex.yaml; Entire frozen regional boundary neighbor | context_only | The complete apex/antapex/horn boundary record was read for context. No neighboring verdict is imported as a target defect. |
| micro49-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097684,GO:0097687,GO:0097683,GO:0097614,GO:0097613,GO:0110165,GO:0097618,GO:0097612,GO:0097685,GO:0097686; Ten-term native response: exact focal definitions, active status, synonyms and relevant typed child links; GO0110165 relevant children only, not a biological audit of its complete child inventory. | supports | Active GO0097687 is the horn-shaped thecate specialization of antapex GO0097684. The latter explicitly lists the horn as an is-a child; GO0097614 lists the antapex as a part. Thus horn-to-hypocone parthood is inherited through the parent, not asserted to be a separate directly exposed edge. |
| micro49-GO0097687-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097687/history; Complete native term-history response and dated RELATION/DEFINITION entries. | supports | History explicitly records direct is-a parent GO0097684. It does not independently demonstrate a separate direct horn-to-hypocone parthood edge; the latter is an inheritance inference. Its historical constraint display is not substituted for the actual current constraints endpoint. |
| micro49-tax2864 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864; Complete native taxId/scientificName/rank/lineage/otherNames response. | supports | ENA taxId2864 is Dinophyceae at class rank, with dinoflagellates as its common name and Dinoflagellata/Dinophyta aliases; this verifies identity, not a quantitative occurrence survey. |
| micro49-go-horn-taxon | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097687/constraints; Complete native taxonConstraints array including ancestorId, relationship, taxId, taxIdType and taxName. | supports | The native constraints endpoint explicitly returns only_in_taxon NCBITaxon2864 Dinophyceae for this term. This is a permissible taxonomic restriction, not proof that every member has the feature. |
| micro49-tol-orientation | https://tolweb.org/articles/?article_id=4756; Complete main text of Orientation of a Motile Dinoflagellate Cell, embedded overview caption and About This Page authorship/copyright; image pixels were not inspected. | supports | Mona Hoppenrath’s authored2008 orientation note directly identifies the apex at the top of the episome and the antapex at the bottom of the hyposome; positions below the cingulum are posterior. It distinguishes naked/armoured terminology and treats the apical groove as a possible athecate feature. This is an expert morphological terminology authority, not a new molecular or formation experiment. |
| micro49-taylor1980-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A7002229%20AND%20SRC%3AMED; Exact native id/title/authorString/pubYear/doi/pageInfo and complete abstractText; original2026-10-21 receipt retained. | supports | Unique MED7002229 is Taylor FJ1980, On dinoflagellate evolution, Biosystems13(1–2):65–108, DOI10.1016/0303-2647(80)90006-4. The complete abstract is a broad evolutionary synthesis and does not independently establish the particular horn/apex wording. The maintained record uses this citation only to corroborate GO’s bibliography. |
| micro49-taylor1980-api | https://api.elsevier.com/content/article/pii/0303264780900064?httpAccept=text/xml; Complete retained publisher coredata/metadata XML; status200 does not establish full-text access. | context_only | The publisher API returned HTTP200 metadata with exact title/DOI/PII and closed-access flags; the retained XML has no article main body. This is bibliographic corroboration only. |
| micro49-taylor1980-publisher | https://www.sciencedirect.com/science/article/pii/0303264780900064; Original response status/body readability limit; no article-body claims drawn. | context_only | The retained ScienceDirect response is HTTP403 and provides no inspected scientific article body. It remains an original failed-access receipt; later success elsewhere would not invalidate the historical access note. |
| schema-result | just validate data/structures/other/dinoflagellate_antapical_horn.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dinoflagellate_antapical_horn.yaml |
| strict-result | just validate-strict data/structures/other/dinoflagellate_antapical_horn.yaml --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/dinoflagellate_antapical_horn-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dinoflagellate_antapical_horn.yaml --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/dinoflagellate_antapical_horn-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch49-20261022-3rpodnkz/dinoflagellate_antapical_horn-strict.tsv |
| native-graphs | /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapical_horn.yaml --causal-graphs; Complete focused read-only causal graph report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/dinoflagellate_antapical_horn.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- The reviewed objects are morphological regions. No direct localized molecular inventory, component formation-necessity assay or quantitative distribution census was established; none is fabricated from generic dinoflagellate cell materials.
- No figure pixels, underlying microscopy data, supplements or independent experiments were reanalyzed. GO, native bibliography and expert terminology have explicitly distinct evidence tiers.
- Taylor1980 was read at complete native abstract and publisher metadata-only tier. No full main body, primary experimental details or figures from that review were inspected. Original reused source URLs, UTC timestamps and hashes are unchanged.
- The neighboring antapex definition retains a source-origin orientation discrepancy; this target does not repeat that direction. It remains a boundary limitation rather than an imported target finding.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- No protein examples or molecular graph actors occur in this target; protein-accession enrichment and iModulonDB do not apply to the present morphological topology claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T052922Z-dinoflagellate-antapical-horn-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of dinoflagellate antapical horn
started_at: '2026-10-22T05:15:52Z'
finished_at: '2026-10-22T05:29:22Z'
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
summary: 'Qualified pass: the exact thecate antapical-horn class, direct antapex parent
  and explicitly inherited hypocone parthood are supported. No consequential target
  defect was identified.'
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
  - path: data/structures/other/dinoflagellate_antapex.yaml
    sha256: 1379be0377e9b86e39f36a4a2a8946b02ab5aa9004aa2576e25b8691147c7fb9
    role: context
  - path: data/structures/other/dinoflagellate_antapical_horn.yaml
    sha256: 17b0c9dcaaa5110c51d7120d3d7fb6bf6ac9a483981418b9ada4be51b700ccc7
    role: target
  - path: data/structures/other/dinoflagellate_apex.yaml
    sha256: 5c8d91554cc820c9434886f0022093eff4f766f4ad608fed12ded740860d0749
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
- target_id: GO:0097687
  path: data/structures/other/dinoflagellate_antapical_horn.yaml
  label: dinoflagellate antapical horn
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_antapical_horn.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target, with the two frozen apex/antapex/horn neighbors
    read for boundary context. All current definition, hierarchy/parthood, taxonomy,
    topology, evidence and discussion claims were assessed; no neighboring verdict
    is imported.
  selection: Batch49 fixed strict path order, index 9; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097687
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: just validate data/structures/other/dinoflagellate_antapical_horn.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: just validate-strict data/structures/other/dinoflagellate_antapical_horn.yaml
    --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/dinoflagellate_antapical_horn-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-graphs
  name: Focused native graph check
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapical_horn.yaml
    --causal-graphs
  exit_code: 0
  summary: No GENE_OR_PROTEIN nodes are present. Structure-node identities and topology
    were checked against native GO separately.
  evidence_ids:
  - native-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0097687
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graph-rubric
  - neighbor-dinoflagellate_antapex
  - neighbor-dinoflagellate_apex
  - micro49-go
  - micro49-GO0097687-history
  - micro49-tax2864
  - micro49-go-horn-taxon
  - micro49-tol-orientation
  - micro49-taylor1980-meta
  - micro49-taylor1980-api
  - micro49-taylor1980-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0097687
  summary: '6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro49-taylor1980-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0097687
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
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dinoflagellate_antapical_horn.yaml
  locator: Entire maintained YAML, including all topology edges, source notes, discussions
    and historical entries
  accessed_at: '2026-10-22T05:21:08Z'
  support: context_only
  summary: The complete target was read; a cited authority is checked for biological
    consistency as well as verbatim identity.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: CellStructureRecord definition/definition_source; StructuralComponent;
    EssentialityEnum; taxonomic presence and graph scopes
  accessed_at: '2026-10-22T05:21:08Z'
  support: context_only
  summary: A region is distinguished from an assembled molecular complex. Formation
    necessity is distinct from presence or function; no molecular requirement is inferred
    for an unspecified inventory.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity and grounding, scope and evidence placement
  accessed_at: '2026-10-22T05:21:08Z'
  support: context_only
  summary: Exact identifiers do not by themselves validate contradictory biological
    prose. Optional components are not filled with generic regional or whole-cell
    materials without specific support.
- evidence_id: graph-rubric
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Nonmechanistic structure topology and explicit edge-level evidence
  accessed_at: '2026-10-22T05:21:08Z'
  support: context_only
  summary: Descriptive is-a, parthood and spatial relations can remain NONMECHANISTIC;
    they do not demonstrate formation or physiological causation.
- evidence_id: neighbor-dinoflagellate_antapex
  kind: record_content
  reference: data/structures/other/dinoflagellate_antapex.yaml
  locator: Entire frozen regional boundary neighbor
  accessed_at: '2026-10-22T05:21:08Z'
  support: context_only
  summary: The complete apex/antapex/horn boundary record was read for context. No
    neighboring verdict is imported as a target defect.
- evidence_id: neighbor-dinoflagellate_apex
  kind: record_content
  reference: data/structures/other/dinoflagellate_apex.yaml
  locator: Entire frozen regional boundary neighbor
  accessed_at: '2026-10-22T05:21:08Z'
  support: context_only
  summary: The complete apex/antapex/horn boundary record was read for context. No
    neighboring verdict is imported as a target defect.
- evidence_id: micro49-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097684,GO:0097687,GO:0097683,GO:0097614,GO:0097613,GO:0110165,GO:0097618,GO:0097612,GO:0097685,GO:0097686
  locator: 'Ten-term native response: exact focal definitions, active status, synonyms
    and relevant typed child links; GO0110165 relevant children only, not a biological
    audit of its complete child inventory.'
  accessed_at: '2026-10-22T05:16:46.025891Z'
  support: supports
  summary: Active GO0097687 is the horn-shaped thecate specialization of antapex GO0097684.
    The latter explicitly lists the horn as an is-a child; GO0097614 lists the antapex
    as a part. Thus horn-to-hypocone parthood is inherited through the parent, not
    asserted to be a separate directly exposed edge.
  snapshot_sha256: b0a7825201eb9b01e2e669c9595cd1ad05f9e322a16bf8b1a00a4a093884736e
- evidence_id: micro49-GO0097687-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097687/history
  locator: Complete native term-history response and dated RELATION/DEFINITION entries.
  accessed_at: '2026-10-22T05:16:46.702526Z'
  support: supports
  summary: History explicitly records direct is-a parent GO0097684. It does not independently
    demonstrate a separate direct horn-to-hypocone parthood edge; the latter is an
    inheritance inference. Its historical constraint display is not substituted for
    the actual current constraints endpoint.
  snapshot_sha256: 70fea0d8875ec84768ec659b43a15c8da4c02685293b1ace96939663dc52b408
- evidence_id: micro49-tax2864
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864
  locator: Complete native taxId/scientificName/rank/lineage/otherNames response.
  accessed_at: '2026-10-22T05:16:46.025548Z'
  support: supports
  summary: ENA taxId2864 is Dinophyceae at class rank, with dinoflagellates as its
    common name and Dinoflagellata/Dinophyta aliases; this verifies identity, not
    a quantitative occurrence survey.
  snapshot_sha256: da7d6dfa6d6784e4eb22bc3f3e05878f3aae5a281a4996ee25a2012d580f27d4
- evidence_id: micro49-go-horn-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097687/constraints
  locator: Complete native taxonConstraints array including ancestorId, relationship,
    taxId, taxIdType and taxName.
  accessed_at: '2026-10-22T05:18:11.991416Z'
  support: supports
  summary: The native constraints endpoint explicitly returns only_in_taxon NCBITaxon2864
    Dinophyceae for this term. This is a permissible taxonomic restriction, not proof
    that every member has the feature.
  snapshot_sha256: c1ac2d6dd676fa882d195bb473ce1a577eae8a20453c4adf06a7bc85e26d416a
- evidence_id: micro49-tol-orientation
  kind: authority
  reference: https://tolweb.org/articles/?article_id=4756
  locator: Complete main text of Orientation of a Motile Dinoflagellate Cell, embedded
    overview caption and About This Page authorship/copyright; image pixels were not
    inspected.
  accessed_at: '2026-10-22T05:18:11.990831Z'
  support: supports
  summary: Mona Hoppenrath’s authored2008 orientation note directly identifies the
    apex at the top of the episome and the antapex at the bottom of the hyposome;
    positions below the cingulum are posterior. It distinguishes naked/armoured terminology
    and treats the apical groove as a possible athecate feature. This is an expert
    morphological terminology authority, not a new molecular or formation experiment.
  snapshot_sha256: 406916e9c83d51de4ec6f7dee8a7b129c6ab8e1781a65a3ec28d83734970370e
- evidence_id: micro49-taylor1980-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A7002229%20AND%20SRC%3AMED
  locator: Exact native id/title/authorString/pubYear/doi/pageInfo and complete abstractText;
    original2026-10-21 receipt retained.
  accessed_at: '2026-10-21T09:08:00.385105Z'
  support: supports
  summary: Unique MED7002229 is Taylor FJ1980, On dinoflagellate evolution, Biosystems13(1–2):65–108,
    DOI10.1016/0303-2647(80)90006-4. The complete abstract is a broad evolutionary
    synthesis and does not independently establish the particular horn/apex wording.
    The maintained record uses this citation only to corroborate GO’s bibliography.
  snapshot_sha256: 03033d3a50fcdf442fafea318713584e25d28b09b50aaf93b2a7f9674b79d1c7
- evidence_id: micro49-taylor1980-api
  kind: database
  reference: https://api.elsevier.com/content/article/pii/0303264780900064?httpAccept=text/xml
  locator: Complete retained publisher coredata/metadata XML; status200 does not establish
    full-text access.
  accessed_at: '2026-10-21T09:08:56.409707Z'
  support: context_only
  summary: The publisher API returned HTTP200 metadata with exact title/DOI/PII and
    closed-access flags; the retained XML has no article main body. This is bibliographic
    corroboration only.
  snapshot_sha256: c4412fc99d85956bb46c41524b17fae0d57261ec0302293d8d856dc905528dd5
- evidence_id: micro49-taylor1980-publisher
  kind: database
  reference: https://www.sciencedirect.com/science/article/pii/0303264780900064
  locator: Original response status/body readability limit; no article-body claims
    drawn.
  accessed_at: '2026-10-21T09:08:56.074246Z'
  support: context_only
  summary: The retained ScienceDirect response is HTTP403 and provides no inspected
    scientific article body. It remains an original failed-access receipt; later success
    elsewhere would not invalidate the historical access note.
  snapshot_sha256: 14dd40deb21794994e8cbc95036a781eb7e7b41de1fbcc216c4af476bd5948f7
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dinoflagellate_antapical_horn.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:15:53Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dinoflagellate_antapical_horn.yaml'
  snapshot_sha256: 1f3e685b44ca05b53f3766c001d907198c91627903fbaf80714e9bd769e902cc
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dinoflagellate_antapical_horn.yaml
    --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/dinoflagellate_antapical_horn-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:15:54Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dinoflagellate_antapical_horn.yaml\
    \ --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/dinoflagellate_antapical_horn-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch49-20261022-3rpodnkz/dinoflagellate_antapical_horn-strict.tsv"
  snapshot_sha256: f6446e7264cec1a4ed042807fe2fdb8ce99cd17a9451897922163eb4c472d341
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapical_horn.yaml
    --causal-graphs
  locator: Complete focused read-only causal graph report
  accessed_at: '2026-10-22T05:17:00.125373Z'
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
  locator: data/structures/other/dinoflagellate_antapical_horn.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE;
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
  topic: Exact narrower horn identity and inherited containment
  outcome: supported
  target_ids:
  - GO:0097687
  summary: GO0097687 denotes a horn-shaped antapex limited by the source to thecate
    species. Its direct parent is GO0097684; the record correctly keeps the specialized
    horn separate from the general antapex and explicitly marks hypocone containment
    as inherited. It does not copy the parent’s erroneous anterior wording, so that
    neighboring definition defect is not duplicated here.
  evidence_ids:
  - record
  - schema
  - micro49-go
  - micro49-GO0097687-history
  - micro49-tax2864
  - micro49-go-horn-taxon
  - micro49-tol-orientation
  - micro49-taylor1980-meta
  - micro49-taylor1980-api
  - micro49-taylor1980-publisher
- assessment_id: topology
  area: graph
  topic: Three-edge nonmechanistic horn topology
  outcome: supported
  target_ids:
  - GO:0097687
  summary: The three structure nodes and three edges distinguish direct horn is-a
    antapex, parent antapex part-of hypocone, and the resulting inherited horn parthood.
    The graph explicitly avoids a mechanistic assembly or a supposed independent direct
    GO edge. These exact claims agree with current child links and history.
  evidence_ids:
  - record
  - schema
  - micro49-go
  - micro49-GO0097687-history
  - micro49-tax2864
  - micro49-go-horn-taxon
  - micro49-tol-orientation
  - micro49-taylor1980-meta
  - micro49-taylor1980-api
  - micro49-taylor1980-publisher
  - graph-rubric
- assessment_id: bibliography
  area: provenance
  topic: Historical metadata-only Taylor scope is accurate
  outcome: supported
  target_ids:
  - GO:0097687
  summary: The retained paper identifiers and complete native abstract match the record.
    Publisher XML contains metadata only and the retained article route failed403.
    The target explicitly limits Taylor to bibliographic corroboration, so an uninspected
    full paper is neither upgraded to primary anatomical support nor treated as a
    record defect.
  evidence_ids:
  - micro49-taylor1980-meta
  - micro49-taylor1980-api
  - micro49-taylor1980-publisher
  - record
  - micro49-go
- assessment_id: taxonomic-scope
  area: scope
  topic: Restricted Dinophyceae scope with cautious occurrence
  outcome: supported
  target_ids:
  - GO:0097687
  summary: Native only_in_taxon2864 and ENA class identity support the dinoflagellate
    restriction. VARIABLE does not claim universal presence; horn thecate restriction
    and conditional surface features remain explicit. These authority definitions
    do not supply a quantitative cross-species census.
  evidence_ids:
  - record
  - schema
  - micro49-go
  - micro49-GO0097687-history
  - micro49-tax2864
  - micro49-go-horn-taxon
  - micro49-tol-orientation
  - micro49-taylor1980-meta
  - micro49-taylor1980-api
  - micro49-taylor1980-publisher
- assessment_id: composition
  area: grounding
  topic: No regional molecular inventory asserted
  outcome: supported
  target_ids:
  - GO:0097687
  summary: No component rows, gene symbols or protein instances are asserted. The
    historical OPEN discussion requests specifically localized constituents and exact
    classes; generic cellulose, membrane or whole-cell protein inventories cannot
    be reassigned to this regional point without direct support. No automatic omission
    finding is made.
  evidence_ids:
  - record
  - schema
  - micro49-go
  - micro49-GO0097687-history
  - micro49-tax2864
  - micro49-go-horn-taxon
  - micro49-tol-orientation
  - micro49-taylor1980-meta
  - micro49-taylor1980-api
  - micro49-taylor1980-publisher
  - curation
- assessment_id: formation
  area: grounding
  topic: Formation necessity is not established
  outcome: unknown
  target_ids:
  - GO:0097687
  summary: There are no component essentiality claims to test. Morphological location
    and taxonomy do not establish molecular assembly necessities or physiological
    functions, and the review preserves that uncertainty.
  evidence_ids:
  - record
  - schema
  - micro49-go
  - micro49-GO0097687-history
  - micro49-tax2864
  - micro49-go-horn-taxon
  - micro49-tol-orientation
  - micro49-taylor1980-meta
  - micro49-taylor1980-api
  - micro49-taylor1980-publisher
- assessment_id: coverage
  area: completeness
  topic: Complete target and source-placement coverage
  outcome: supported
  target_ids:
  - GO:0097687
  summary: All maintained fields, every graph edge/source note, current discussion
    and historical entry were read. No optional canonical species, protein inventory,
    physical measure, image or additional causal mechanism is required solely to populate
    a slot. Source limits and the distinct taxonomic scopes remain explicit.
  evidence_ids:
  - record
  - schema
  - micro49-go
  - micro49-GO0097687-history
  - micro49-tax2864
  - micro49-go-horn-taxon
  - micro49-tol-orientation
  - micro49-taylor1980-meta
  - micro49-taylor1980-api
  - micro49-taylor1980-publisher
  - curation
findings: []
actions: []
limitations:
- The reviewed objects are morphological regions. No direct localized molecular inventory,
  component formation-necessity assay or quantitative distribution census was established;
  none is fabricated from generic dinoflagellate cell materials.
- No figure pixels, underlying microscopy data, supplements or independent experiments
  were reanalyzed. GO, native bibliography and expert terminology have explicitly
  distinct evidence tiers.
- Taylor1980 was read at complete native abstract and publisher metadata-only tier.
  No full main body, primary experimental details or figures from that review were
  inspected. Original reused source URLs, UTC timestamps and hashes are unchanged.
- The neighboring antapex definition retains a source-origin orientation discrepancy;
  this target does not repeat that direction. It remains a boundary limitation rather
  than an imported target finding.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- No protein examples or molecular graph actors occur in this target; protein-accession
  enrichment and iModulonDB do not apply to the present morphological topology claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
