# Source-backed review of dinoflagellate sulcal notch

- Review: 20261022T054307Z-dinoflagellate-sulcal-notch-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:31:17Z
- Finished UTC: 2026-10-22T05:43:07Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: the specialized posterior-reaching sulcus identity, direct parent, morphological topology and explicitly limited Taylor bibliography are supported. No consequential target defect was identified.

## Scope And Provenance

Exactly one entire maintained target and the other two frozen hypocone/sulcal-notch/sulcus boundary records; all definitions, hierarchy, taxonomy, source notes, graph edges, discussions and history are covered at their declared evidence tiers.

Selection: Batch50 fixed strict path order, index 6; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097618 | data/structures/other/dinoflagellate_sulcal_notch.yaml | maintained | dinoflagellate sulcal notch |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0097618 | Focused validator passed. |
| Focused native strict | passed | True | GO:0097618 | Focused validator passed. |
| Focused native graph check | passed | True | GO:0097618 | No GENE_OR_PROTEIN nodes occur; exact structure-node identities and all descriptive edges were assessed independently. |
| Claim-level scientific review | passed | True | GO:0097618 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0097618 | 6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0097618 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097618 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097618 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097618 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0097618 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact narrower sulcus morphology

identity: supported. Targets: GO:0097618.

Current GO0097618 exactly defines the notch as a sulcus reaching the posterior antapex and making the hypocone appear bilobed. Its direct parent is GO0097612; exact dinoflagellate sulcus notch and related sulcal notch synonyms are accurate. The target correctly separates morphological extension/appearance from subclass identity with antapex or hypocone.

### Three-edge nonmechanistic notch topology

graph: supported. Targets: GO:0097618.

Four structure nodes and three edges express the direct sulcus subclass, posterior endpoint and hypocone appearance. They are supported at the GO morphology tier and explicitly NONMECHANISTIC; neither the source nor this review establishes a molecular process that creates the notch.

### Accurate metadata-only Taylor corroboration

provenance: supported. Targets: GO:0097618.

Current GO0097618 definition.xrefs does cite PMID7002229; the exact DOI and native publisher metadata agree. The target already restricts Taylor to bibliographic corroboration and does not pretend its body was read. The bilobed definition is consequently authority-supported, not independently revalidated against Taylor’s full paper.

### Dinophyceae restriction with variable occurrence

scope: supported. Targets: GO:0097618.

Current only_in_taxon2864 and ENA class identity support the taxonomic restriction. VARIABLE is compatible with lineage/morphotype variation; the expert account explicitly distinguishes groove-associated dinokont from groove-free desmokont flagellation. Neither an exact prevalence estimate nor universal presence is inferred.

### Optional regional constituents remain unresolved

grounding: supported. Targets: GO:0097618.

The target contains no molecular component rows or protein examples. Its OPEN TODO explicitly describes what was unresolved in that historical pass and requests directly localized, exactly grounded constituents. Generic cell-wall, membrane or flagellar protein material does not become a region-specific constituent automatically; the empty optional inventory alone is not a finding.

### Formation necessity remains unknown

grounding: unknown. Targets: GO:0097618.

No component essentiality labels or molecular assembly claims occur. Morphological definitions and topology do not establish which molecules are necessary to form the region; this review preserves that uncertainty.

### Complete target and bounded source coverage

completeness: supported. Targets: GO:0097618.

The entire target, all graph edge evidence, discussion claims and historical entries were assessed. The two other frozen regional records provide boundary context only. No canonical species, image, numerical property or additional mechanism is required merely to populate an optional slot.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dinoflagellate_sulcal_notch.yaml; Entire maintained YAML including source notes, all graph edges, discussions and history | context_only | All current scientific claims and historical annotations were read. No conclusion for a neighboring record is imported into this target. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; CellStructureRecord definition, StructuralComponent, EssentialityEnum, PresenceEnum and graph scopes | context_only | Regional morphology is distinct from a molecular constituent inventory or formation requirement; VARIABLE does not assert universal or majority occurrence. |
| curation | docs/CURATION.md; Exact identity, evidence placement, optional components and formation necessity | context_only | An exact authority identifier does not independently verify biological prose; source-specific claims retain the tier actually inspected. |
| graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Descriptive structural topology and edge-level evidence | context_only | NONMECHANISTIC may describe is-a, parthood and spatial morphology without implying a physiological or assembly mechanism. |
| neighbor-dinoflagellate_hypocone | data/structures/other/dinoflagellate_hypocone.yaml; Entire frozen hypocone/sulcal-notch/sulcus boundary neighbor | context_only | The other two records of the posterior-region/furrow boundary set were read for context only; their findings are not automatically transferred to this target. |
| neighbor-dinoflagellate_sulcus | data/structures/other/dinoflagellate_sulcus.yaml; Entire frozen hypocone/sulcal-notch/sulcus boundary neighbor | context_only | The other two records of the posterior-region/furrow boundary set were read for context only; their findings are not automatically transferred to this target. |
| micro50-go-own-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097614,GO:0097618,GO:0097612,GO:0097684; Complete four-term response: ids, active status, definitions/xrefs, synonyms, comments and typed children; the antapex wording is retained explicitly as an upstream conflict. | supports | The four active exact terms retain the maintained hypocone, sulcal-notch and sulcus definitions and synonym scopes. GO0097614 lists antapex GO0097684 as a part_of child; GO0097612 lists notch GO0097618 as an is_a child. The notch explicitly reaches the posterior antapex. Current sulcus definition.xrefs names PMID20561119, whereas the notch names PMID7002229. GO0097684 itself retains a conflicting anterior definition; that source discrepancy is not copied into these target definitions. |
| micro50-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685,GO:0097686,GO:0097611,GO:0097613,GO:0097683,GO:0097614,GO:0097610,GO:0110165; Eight-term response: complete focal definitions/status/synonyms and relevant typed children of GO0110165/0097610; no biological audit of the unrelated GO0110165 child inventory. | supports | GO0110165 relevant children include hypocone GO0097614 is_a; GO0097610 lists sulcus GO0097612 is_a. Exact epicone/cingulum definitions corroborate the anterior/posterior boundary and transverse furrow. These are typed ontology relations and definitions, not a quantitative occurrence census. |
| micro50-GO0097618-history-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097618/history; Complete native history array and current term fields, including dated RELATION/DEFINITION entries. | supports | History records the direct is_a relation to GO0097612 and the posterior-reaching bilobed morphology definition. Historical Bad taxon ID display entries do not replace the current constraints response. |
| micro50-GO0097618-constraints-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097618/constraints; Exact taxonConstraints array: ancestorId, relationship, taxId, taxIdType, taxName. Any inherited protein-annotation blacklist is not used as a regional constituent inventory. | supports | The native taxonConstraints entry for this exact term explicitly states only_in_taxon NCBITaxon2864 Dinophyceae. This is a restriction on where the structure occurs, not evidence that all or most class members possess it. |
| micro50-tax2864 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864; Complete native taxId/scientificName/rank/lineage/otherNames response. | supports | ENA taxId2864 is class Dinophyceae, with dinoflagellates as common name and Dinoflagellata/Dinophyta aliases. Identity and rank are verified without inferring a numerical frequency. |
| micro50-tol-orientation | https://tolweb.org/articles/?article_id=4756; Complete main text of Orientation of a Motile Dinoflagellate Cell, overview caption and About This Page authorship; no image pixels inspected. | supports | Mona Hoppenrath’s expert orientation note defines the lower region as hyposome, hypocone in athecate cells and hypotheca in thecate cells; it places the antapex at its bottom and everything below the cingulum posterior. The side bearing the sulcus is ventral. This supports anatomical orientation while preserving related, rather than exact, synonym scopes. |
| micro50-tol-dinoflagellates | https://tolweb.org/Dinoflagellates/2445; Authorship; Introduction morphological diversity; Characteristics opening/orientation link and complete Flagella subsection including Figs1–8 captions. Later biological sections and image pixels are not used. | supports | Hoppenrath and Saldarriaga describe the longitudinal flagellum lying partly in the sulcus with its distal portion projecting freely behind the cell. Desmokont flagellation is explicitly distinguished because its flagella are not associated with grooves. This supports the target’s cautious VARIABLE occurrence rather than universality. |
| micro50-taylor1980-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A7002229%20AND%20SRC%3AMED; Complete native bibliographic identity fields and abstractText; original2026-10-21 receipt preserved. | supports | Unique MED7002229 is Taylor FJ1980, On dinoflagellate evolution, Biosystems13(1–2):65–108, DOI10.1016/0303-2647(80)90006-4. The complete abstract is broad evolutionary synthesis and does not independently establish exact sulcus/notch anatomy. This verifies the citation’s identity, not whether a particular GO term cites it. |
| micro50-taylor1980-api | https://api.elsevier.com/content/article/pii/0303264780900064?httpAccept=text/xml; Complete publisher metadata XML; no full-text scope inferred from status200. | context_only | The retained publisher HTTP200 XML consists of coredata with matching title/DOI/PII and closed-access flags; it is not an article main body. |
| micro50-taylor1980-publisher | https://www.sciencedirect.com/science/article/pii/0303264780900064; Original status403 and visible challenge/error body; no article-body evidence inferred. | context_only | The retained ScienceDirect route returned HTTP403 challenge/error content, not a scientific article body. Its original failure timestamp and bytes remain unchanged. |
| schema-result | just validate data/structures/other/dinoflagellate_sulcal_notch.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dinoflagellate_sulcal_notch.yaml |
| strict-result | just validate-strict data/structures/other/dinoflagellate_sulcal_notch.yaml --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_sulcal_notch-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dinoflagellate_sulcal_notch.yaml --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_sulcal_notch-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_sulcal_notch-strict.tsv |
| native-graphs | /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcal_notch.yaml --causal-graphs; Complete focused read-only causal graph report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/dinoflagellate_sulcal_notch.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- These are morphological regions/furrows, not asserted molecular complexes. No localized constituent inventory, formation-necessity assay or quantitative class-wide occurrence census was established. Optional component rows are not populated with generic whole-cell materials.
- No microscopy pixels, raw imaging data or supplements were inspected. The directly read Tree of Life expert terminology is distinguished from a primary experiment; current GO supplies the exact morphological definitions and relations.
- GO0097684 retains an anterior/posterior inconsistency. These targets describe the posterior endpoint correctly using GO0097618 and the directly read orientation authority, so a neighboring definition defect is not imported as a target finding.
- The initial seven sandbox DNS attempts were retained as status0 diagnostics. Separately retained network-enabled retries returned genuine200 JSON and supplied the actual ontology evidence.
- Taylor1980 was inspected at complete native abstract and publisher metadata tier only; the retained publisher route returned403. No full main body or figures were read. Historical statements that this curation pass lacked a body are not refuted merely by present source access elsewhere.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user expressly requests one review for every unreviewed record, including clean qualified reviews.
- No molecular gene/protein actors occur; iModulonDB and protein-example enrichment are not applicable to the present anatomical claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T054307Z-dinoflagellate-sulcal-notch-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of dinoflagellate sulcal notch
started_at: '2026-10-22T05:31:17Z'
finished_at: '2026-10-22T05:43:07Z'
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
summary: 'Qualified pass: the specialized posterior-reaching sulcus identity, direct
  parent, morphological topology and explicitly limited Taylor bibliography are supported.
  No consequential target defect was identified.'
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
  - path: data/structures/other/dinoflagellate_hypocone.yaml
    sha256: 0a596b02f63ce6799d10b49b4cf34a921fb2ae92e1208ee599a96ed47c5f40a1
    role: context
  - path: data/structures/other/dinoflagellate_sulcal_notch.yaml
    sha256: 0e3dace360a1a70bc43f318649972ebb63a50628897c7681bb81c9c75f18c7b1
    role: target
  - path: data/structures/other/dinoflagellate_sulcus.yaml
    sha256: b3606a5c03fbc85a602f3ea6927c22e49eedbcd00d1e9607c85ac080205bd356
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
- target_id: GO:0097618
  path: data/structures/other/dinoflagellate_sulcal_notch.yaml
  label: dinoflagellate sulcal notch
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_sulcal_notch.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire maintained target and the other two frozen hypocone/sulcal-notch/sulcus
    boundary records; all definitions, hierarchy, taxonomy, source notes, graph edges,
    discussions and history are covered at their declared evidence tiers.
  selection: Batch50 fixed strict path order, index 6; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097618
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0097618
  command: just validate data/structures/other/dinoflagellate_sulcal_notch.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0097618
  command: just validate-strict data/structures/other/dinoflagellate_sulcal_notch.yaml
    --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_sulcal_notch-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-graphs
  name: Focused native graph check
  status: passed
  required: true
  target_ids:
  - GO:0097618
  command: /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcal_notch.yaml
    --causal-graphs
  exit_code: 0
  summary: No GENE_OR_PROTEIN nodes occur; exact structure-node identities and all
    descriptive edges were assessed independently.
  evidence_ids:
  - native-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0097618
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graph-rubric
  - neighbor-dinoflagellate_hypocone
  - neighbor-dinoflagellate_sulcus
  - micro50-go-own-network
  - micro50-go
  - micro50-GO0097618-history-network
  - micro50-GO0097618-constraints-network
  - micro50-tax2864
  - micro50-tol-orientation
  - micro50-tol-dinoflagellates
  - micro50-taylor1980-meta
  - micro50-taylor1980-api
  - micro50-taylor1980-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0097618
  summary: '6 of 7 collected target identifiers returned OK. PMID:7002229: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro50-taylor1980-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097618
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
  - GO:0097618
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
  - GO:0097618
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
  - GO:0097618
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
  - GO:0097618
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
  reference: data/structures/other/dinoflagellate_sulcal_notch.yaml
  locator: Entire maintained YAML including source notes, all graph edges, discussions
    and history
  accessed_at: '2026-10-22T05:35:03Z'
  support: context_only
  summary: All current scientific claims and historical annotations were read. No
    conclusion for a neighboring record is imported into this target.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: CellStructureRecord definition, StructuralComponent, EssentialityEnum,
    PresenceEnum and graph scopes
  accessed_at: '2026-10-22T05:35:03Z'
  support: context_only
  summary: Regional morphology is distinct from a molecular constituent inventory
    or formation requirement; VARIABLE does not assert universal or majority occurrence.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, evidence placement, optional components and formation necessity
  accessed_at: '2026-10-22T05:35:03Z'
  support: context_only
  summary: An exact authority identifier does not independently verify biological
    prose; source-specific claims retain the tier actually inspected.
- evidence_id: graph-rubric
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Descriptive structural topology and edge-level evidence
  accessed_at: '2026-10-22T05:35:03Z'
  support: context_only
  summary: NONMECHANISTIC may describe is-a, parthood and spatial morphology without
    implying a physiological or assembly mechanism.
- evidence_id: neighbor-dinoflagellate_hypocone
  kind: record_content
  reference: data/structures/other/dinoflagellate_hypocone.yaml
  locator: Entire frozen hypocone/sulcal-notch/sulcus boundary neighbor
  accessed_at: '2026-10-22T05:35:03Z'
  support: context_only
  summary: The other two records of the posterior-region/furrow boundary set were
    read for context only; their findings are not automatically transferred to this
    target.
- evidence_id: neighbor-dinoflagellate_sulcus
  kind: record_content
  reference: data/structures/other/dinoflagellate_sulcus.yaml
  locator: Entire frozen hypocone/sulcal-notch/sulcus boundary neighbor
  accessed_at: '2026-10-22T05:35:03Z'
  support: context_only
  summary: The other two records of the posterior-region/furrow boundary set were
    read for context only; their findings are not automatically transferred to this
    target.
- evidence_id: micro50-go-own-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097614,GO:0097618,GO:0097612,GO:0097684
  locator: 'Complete four-term response: ids, active status, definitions/xrefs, synonyms,
    comments and typed children; the antapex wording is retained explicitly as an
    upstream conflict.'
  accessed_at: '2026-10-22T05:32:40.497633Z'
  support: supports
  summary: The four active exact terms retain the maintained hypocone, sulcal-notch
    and sulcus definitions and synonym scopes. GO0097614 lists antapex GO0097684 as
    a part_of child; GO0097612 lists notch GO0097618 as an is_a child. The notch explicitly
    reaches the posterior antapex. Current sulcus definition.xrefs names PMID20561119,
    whereas the notch names PMID7002229. GO0097684 itself retains a conflicting anterior
    definition; that source discrepancy is not copied into these target definitions.
  snapshot_sha256: c89739ac2029a1a314c387a3b9c7d3e51ac1765a4438e3b1a108337443ff92a4
- evidence_id: micro50-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685,GO:0097686,GO:0097611,GO:0097613,GO:0097683,GO:0097614,GO:0097610,GO:0110165
  locator: 'Eight-term response: complete focal definitions/status/synonyms and relevant
    typed children of GO0110165/0097610; no biological audit of the unrelated GO0110165
    child inventory.'
  accessed_at: '2026-10-22T05:31:10.469605Z'
  support: supports
  summary: GO0110165 relevant children include hypocone GO0097614 is_a; GO0097610
    lists sulcus GO0097612 is_a. Exact epicone/cingulum definitions corroborate the
    anterior/posterior boundary and transverse furrow. These are typed ontology relations
    and definitions, not a quantitative occurrence census.
  snapshot_sha256: 728d23e8f48df235e1d286d42796040aeef04f727c1da32f3bab38c5d3285935
- evidence_id: micro50-GO0097618-history-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097618/history
  locator: Complete native history array and current term fields, including dated
    RELATION/DEFINITION entries.
  accessed_at: '2026-10-22T05:32:40.498385Z'
  support: supports
  summary: History records the direct is_a relation to GO0097612 and the posterior-reaching
    bilobed morphology definition. Historical Bad taxon ID display entries do not
    replace the current constraints response.
  snapshot_sha256: 48fd054344ee485d39a29a69d94bb1b351e8f17308d0e716cc3dfc87f9c3289b
- evidence_id: micro50-GO0097618-constraints-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097618/constraints
  locator: 'Exact taxonConstraints array: ancestorId, relationship, taxId, taxIdType,
    taxName. Any inherited protein-annotation blacklist is not used as a regional
    constituent inventory.'
  accessed_at: '2026-10-22T05:32:40.498285Z'
  support: supports
  summary: The native taxonConstraints entry for this exact term explicitly states
    only_in_taxon NCBITaxon2864 Dinophyceae. This is a restriction on where the structure
    occurs, not evidence that all or most class members possess it.
  snapshot_sha256: 33e619b672dc492461b1ba4560aed8f3c88e15fd6dc4890bedafffe748648f50
- evidence_id: micro50-tax2864
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864
  locator: Complete native taxId/scientificName/rank/lineage/otherNames response.
  accessed_at: '2026-10-22T05:16:46.025548Z'
  support: supports
  summary: ENA taxId2864 is class Dinophyceae, with dinoflagellates as common name
    and Dinoflagellata/Dinophyta aliases. Identity and rank are verified without inferring
    a numerical frequency.
  snapshot_sha256: da7d6dfa6d6784e4eb22bc3f3e05878f3aae5a281a4996ee25a2012d580f27d4
- evidence_id: micro50-tol-orientation
  kind: authority
  reference: https://tolweb.org/articles/?article_id=4756
  locator: Complete main text of Orientation of a Motile Dinoflagellate Cell, overview
    caption and About This Page authorship; no image pixels inspected.
  accessed_at: '2026-10-22T05:18:11.990831Z'
  support: supports
  summary: Mona Hoppenrath’s expert orientation note defines the lower region as hyposome,
    hypocone in athecate cells and hypotheca in thecate cells; it places the antapex
    at its bottom and everything below the cingulum posterior. The side bearing the
    sulcus is ventral. This supports anatomical orientation while preserving related,
    rather than exact, synonym scopes.
  snapshot_sha256: 406916e9c83d51de4ec6f7dee8a7b129c6ab8e1781a65a3ec28d83734970370e
- evidence_id: micro50-tol-dinoflagellates
  kind: authority
  reference: https://tolweb.org/Dinoflagellates/2445
  locator: Authorship; Introduction morphological diversity; Characteristics opening/orientation
    link and complete Flagella subsection including Figs1–8 captions. Later biological
    sections and image pixels are not used.
  accessed_at: '2026-10-22T05:17:27.625373Z'
  support: supports
  summary: Hoppenrath and Saldarriaga describe the longitudinal flagellum lying partly
    in the sulcus with its distal portion projecting freely behind the cell. Desmokont
    flagellation is explicitly distinguished because its flagella are not associated
    with grooves. This supports the target’s cautious VARIABLE occurrence rather than
    universality.
  snapshot_sha256: 5957a1388500247ac00f15d5ffaccc4df3ee19b07daf5986bd7a96fa5fc3df47
- evidence_id: micro50-taylor1980-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A7002229%20AND%20SRC%3AMED
  locator: Complete native bibliographic identity fields and abstractText; original2026-10-21
    receipt preserved.
  accessed_at: '2026-10-21T09:08:00.385105Z'
  support: supports
  summary: Unique MED7002229 is Taylor FJ1980, On dinoflagellate evolution, Biosystems13(1–2):65–108,
    DOI10.1016/0303-2647(80)90006-4. The complete abstract is broad evolutionary synthesis
    and does not independently establish exact sulcus/notch anatomy. This verifies
    the citation’s identity, not whether a particular GO term cites it.
  snapshot_sha256: 03033d3a50fcdf442fafea318713584e25d28b09b50aaf93b2a7f9674b79d1c7
- evidence_id: micro50-taylor1980-api
  kind: database
  reference: https://api.elsevier.com/content/article/pii/0303264780900064?httpAccept=text/xml
  locator: Complete publisher metadata XML; no full-text scope inferred from status200.
  accessed_at: '2026-10-21T09:08:56.409707Z'
  support: context_only
  summary: The retained publisher HTTP200 XML consists of coredata with matching title/DOI/PII
    and closed-access flags; it is not an article main body.
  snapshot_sha256: c4412fc99d85956bb46c41524b17fae0d57261ec0302293d8d856dc905528dd5
- evidence_id: micro50-taylor1980-publisher
  kind: database
  reference: https://www.sciencedirect.com/science/article/pii/0303264780900064
  locator: Original status403 and visible challenge/error body; no article-body evidence
    inferred.
  accessed_at: '2026-10-21T09:08:56.074246Z'
  support: context_only
  summary: The retained ScienceDirect route returned HTTP403 challenge/error content,
    not a scientific article body. Its original failure timestamp and bytes remain
    unchanged.
  snapshot_sha256: 14dd40deb21794994e8cbc95036a781eb7e7b41de1fbcc216c4af476bd5948f7
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dinoflagellate_sulcal_notch.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:31:20Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dinoflagellate_sulcal_notch.yaml'
  snapshot_sha256: 80169e9010709487159fa312857d60cba60760786ad83f7e0eb04343efd5618e
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dinoflagellate_sulcal_notch.yaml
    --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_sulcal_notch-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:31:23Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dinoflagellate_sulcal_notch.yaml\
    \ --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_sulcal_notch-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_sulcal_notch-strict.tsv"
  snapshot_sha256: 7870275024e014e0e6885a53d5ae3363beb237e368ee157df2c927a106d381f8
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcal_notch.yaml
    --causal-graphs
  locator: Complete focused read-only causal graph report
  accessed_at: '2026-10-22T05:33:14.401217Z'
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
  locator: data/structures/other/dinoflagellate_sulcal_notch.yaml; native collect()
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
  topic: Exact narrower sulcus morphology
  outcome: supported
  target_ids:
  - GO:0097618
  summary: Current GO0097618 exactly defines the notch as a sulcus reaching the posterior
    antapex and making the hypocone appear bilobed. Its direct parent is GO0097612;
    exact dinoflagellate sulcus notch and related sulcal notch synonyms are accurate.
    The target correctly separates morphological extension/appearance from subclass
    identity with antapex or hypocone.
  evidence_ids:
  - record
  - schema
  - micro50-go-own-network
  - micro50-go
  - micro50-GO0097618-history-network
  - micro50-GO0097618-constraints-network
  - micro50-tax2864
  - micro50-tol-orientation
  - micro50-tol-dinoflagellates
  - micro50-taylor1980-meta
  - micro50-taylor1980-api
  - micro50-taylor1980-publisher
- assessment_id: topology
  area: graph
  topic: Three-edge nonmechanistic notch topology
  outcome: supported
  target_ids:
  - GO:0097618
  summary: Four structure nodes and three edges express the direct sulcus subclass,
    posterior endpoint and hypocone appearance. They are supported at the GO morphology
    tier and explicitly NONMECHANISTIC; neither the source nor this review establishes
    a molecular process that creates the notch.
  evidence_ids:
  - record
  - schema
  - micro50-go-own-network
  - micro50-go
  - micro50-GO0097618-history-network
  - micro50-GO0097618-constraints-network
  - micro50-tax2864
  - micro50-tol-orientation
  - micro50-tol-dinoflagellates
  - micro50-taylor1980-meta
  - micro50-taylor1980-api
  - micro50-taylor1980-publisher
  - graph-rubric
- assessment_id: bibliography
  area: provenance
  topic: Accurate metadata-only Taylor corroboration
  outcome: supported
  target_ids:
  - GO:0097618
  summary: Current GO0097618 definition.xrefs does cite PMID7002229; the exact DOI
    and native publisher metadata agree. The target already restricts Taylor to bibliographic
    corroboration and does not pretend its body was read. The bilobed definition is
    consequently authority-supported, not independently revalidated against Taylor’s
    full paper.
  evidence_ids:
  - micro50-go-own-network
  - micro50-taylor1980-meta
  - micro50-taylor1980-api
  - micro50-taylor1980-publisher
  - record
- assessment_id: taxonomic-scope
  area: scope
  topic: Dinophyceae restriction with variable occurrence
  outcome: supported
  target_ids:
  - GO:0097618
  summary: Current only_in_taxon2864 and ENA class identity support the taxonomic
    restriction. VARIABLE is compatible with lineage/morphotype variation; the expert
    account explicitly distinguishes groove-associated dinokont from groove-free desmokont
    flagellation. Neither an exact prevalence estimate nor universal presence is inferred.
  evidence_ids:
  - record
  - schema
  - micro50-go-own-network
  - micro50-go
  - micro50-GO0097618-history-network
  - micro50-GO0097618-constraints-network
  - micro50-tax2864
  - micro50-tol-orientation
  - micro50-tol-dinoflagellates
  - micro50-taylor1980-meta
  - micro50-taylor1980-api
  - micro50-taylor1980-publisher
- assessment_id: composition
  area: grounding
  topic: Optional regional constituents remain unresolved
  outcome: supported
  target_ids:
  - GO:0097618
  summary: The target contains no molecular component rows or protein examples. Its
    OPEN TODO explicitly describes what was unresolved in that historical pass and
    requests directly localized, exactly grounded constituents. Generic cell-wall,
    membrane or flagellar protein material does not become a region-specific constituent
    automatically; the empty optional inventory alone is not a finding.
  evidence_ids:
  - record
  - schema
  - micro50-go-own-network
  - micro50-go
  - micro50-GO0097618-history-network
  - micro50-GO0097618-constraints-network
  - micro50-tax2864
  - micro50-tol-orientation
  - micro50-tol-dinoflagellates
  - micro50-taylor1980-meta
  - micro50-taylor1980-api
  - micro50-taylor1980-publisher
  - curation
- assessment_id: formation
  area: grounding
  topic: Formation necessity remains unknown
  outcome: unknown
  target_ids:
  - GO:0097618
  summary: No component essentiality labels or molecular assembly claims occur. Morphological
    definitions and topology do not establish which molecules are necessary to form
    the region; this review preserves that uncertainty.
  evidence_ids:
  - record
  - schema
  - micro50-go-own-network
  - micro50-go
  - micro50-GO0097618-history-network
  - micro50-GO0097618-constraints-network
  - micro50-tax2864
  - micro50-tol-orientation
  - micro50-tol-dinoflagellates
  - micro50-taylor1980-meta
  - micro50-taylor1980-api
  - micro50-taylor1980-publisher
- assessment_id: coverage
  area: completeness
  topic: Complete target and bounded source coverage
  outcome: supported
  target_ids:
  - GO:0097618
  summary: The entire target, all graph edge evidence, discussion claims and historical
    entries were assessed. The two other frozen regional records provide boundary
    context only. No canonical species, image, numerical property or additional mechanism
    is required merely to populate an optional slot.
  evidence_ids:
  - record
  - schema
  - micro50-go-own-network
  - micro50-go
  - micro50-GO0097618-history-network
  - micro50-GO0097618-constraints-network
  - micro50-tax2864
  - micro50-tol-orientation
  - micro50-tol-dinoflagellates
  - micro50-taylor1980-meta
  - micro50-taylor1980-api
  - micro50-taylor1980-publisher
  - curation
findings: []
actions: []
limitations:
- These are morphological regions/furrows, not asserted molecular complexes. No localized
  constituent inventory, formation-necessity assay or quantitative class-wide occurrence
  census was established. Optional component rows are not populated with generic whole-cell
  materials.
- No microscopy pixels, raw imaging data or supplements were inspected. The directly
  read Tree of Life expert terminology is distinguished from a primary experiment;
  current GO supplies the exact morphological definitions and relations.
- GO0097684 retains an anterior/posterior inconsistency. These targets describe the
  posterior endpoint correctly using GO0097618 and the directly read orientation authority,
  so a neighboring definition defect is not imported as a target finding.
- The initial seven sandbox DNS attempts were retained as status0 diagnostics. Separately
  retained network-enabled retries returned genuine200 JSON and supplied the actual
  ontology evidence.
- Taylor1980 was inspected at complete native abstract and publisher metadata tier
  only; the retained publisher route returned403. No full main body or figures were
  read. Historical statements that this curation pass lacked a body are not refuted
  merely by present source access elsewhere.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user expressly requests one review for every unreviewed record, including clean
  qualified reviews.
- No molecular gene/protein actors occur; iModulonDB and protein-example enrichment
  are not applicable to the present anatomical claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
