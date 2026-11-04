# Pusule scientific review

- Review: 20261022T033001Z-pusule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:14:09Z
- Finished UTC: 2026-10-22T03:30:01Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Source-backed canal-connected pusule identity, membrane anatomy, three bounded species examples and exact licensed Figure2 provenance are supported. Unknown physiology is retained; no concrete curation finding.

## Scope And Provenance

Entire single target including every component, hierarchy, taxon/example, function/graph, source, discussion and history. Additional frozen local inputs are read at the precise scope declared in their evidence rows; literature read extents and image inspection are separately stated.

Selection: Batch39 exact path-ordered target 7; fresh f97b native inspection/schema/strict passed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:pusule | data/structures/membrane_organelle/pusule.yaml | maintained | pusule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:pusule | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:pusule | Focused validator passed. |
| Native causal-graphs | passed | True | cellstructuremech:pusule | Native check passed; exact scientific scope was assessed separately. |
| Individual protein verification applicability | not_applicable | False | cellstructuremech:pusule | No individual protein accession or gene/protein graph node occurs in the target. |
| Expression-module applicability | not_applicable | False | cellstructuremech:pusule | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | cellstructuremech:pusule | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | cellstructuremech:pusule | 8 of 9 collected target identifiers returned OK. cellstructuremech:pusule: SKIPPED; Exact local whole-structure identity occurs once in an ignored-inclusive top-level identifier search and is a frozen maintained input. The generic resolver has no external adapter for this locally minted identifier. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | cellstructuremech:pusule | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:pusule | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:pusule | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:pusule | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | cellstructuremech:pusule | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Local identity and open canal topology

identity: supported. Targets: cellstructuremech:pusule.

The source-backed local identifier is unique in the ignored-inclusive corpus and no exact term is returned by the bounded GO query. Dodge supports the apparatus synonym and two-membrane wall connected to the flagellar canal. Broad organelle typing does not assert a sealed lumen; nuclear net and contractile vacuole are separate identities.

### Structural membrane constituent

grounding: supported. Targets: cellstructuremech:pusule.

OTHER/GO0016020 is an accurate structural membrane representation, with UNKNOWN essentiality and no chemical-species assertion. The apposed membranes are directly described in Dodge summary; no speculative proteins, nuclear ribbons or rootlets are inserted.

### Physiology and individual formation requirements

evidence: unknown. Targets: cellstructuremech:pusule.

UNKNOWN essentiality remains appropriate. Tracer entry and static membrane morphology do not establish molecular assembly necessity, transmembrane transport, a contractile cycle or a particular physiological mechanism. The open discussion is accurately conservative.

### Three bounded species examples

scope: supported. Targets: cellstructuremech:pusule.

Each taxon identity is exact. P. kofoidii has directly inspected primary ultrastructure and collection context; P. micans/A. carterae examples are explicitly abstract-only tracer/TEM scope. No distribution prevalence is inferred.

### Exact Figure2 provenance and anatomical caption

provenance: supported. Targets: cellstructuremech:pusule.

The stored/source SHA, source version/filename, native package ETag/calculated MD5, authorship and exact CC BY4.0 permissions agree. Visual panels and caption preserve the collecting duct/diverticula versus adjacent nuclear anatomy distinction.

### Bounded source audit and unchanged status

provenance: supported. Targets: cellstructuremech:pusule.

All target claims were reviewed at the declared source read scopes, with primary/secondary/abstract/native authority tiers separated. No scientific mutation, mapping-status promotion, review persistence or publication is implied.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/pusule.yaml; Entire maintained YAML including all fields, graphs, history and discussions | context_only | The entire target was read; scientific content, status and history remain unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent type/grounding/formation-necessity and graph/component_ref contracts | context_only | A LIPID molecular constituent is distinct from a complete GO membrane structure. Accurate OTHER structural constituents are not categorically forbidden. Constitution, localization, regulatory activity and cell viability do not establish individual formation necessity. |
| pusule-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043227,GO:0016020; Complete exact native term definitions | supports | GO0043227 supplies the broad membrane-bounded-organelle class; GO0016020 denotes the membrane as bilayer plus associated proteins. The OTHER component asserts a structural membrane constituent rather than a chemical lipid identity. Canal connection does not make the entire apparatus identical to the plasma membrane. |
| pusule-agent-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=pusule&amp;limit=100; Complete zero-hit QuickGO response | context_only | The bounded native pusule query returned zero results; it does not establish absence from every ontology or alias. |
| local-pusule-id | rg --no-ignore --hidden -n ^identifier: cellstructuremech:pusule$ data/structures; Complete anchored identifier-line search over maintained data/structures | supports | Exactly one identifier declaration matches cellstructuremech:pusule, the frozen target. Ignored and hidden files were included. |
| pusule-agent-dodge1972-crossref | https://api.crossref.org/works/10.1007/BF01279820; Complete native title/author/DOI/date metadata | supports | The exact DOI10.1007/BF01279820 identifies J.D. Dodge1972 and the correct Protoplasma article. This Crossref response has no abstract. |
| pusule-agent-dodge1972-browser | https://link.springer.com/article/10.1007/BF01279820; Actual publisher browser-displayed Summary lines31–43 plus title/author/DOI; subscription preview only, no full body or native HTTP200 assertion | supports | The publisher summary calls it the pusule apparatus, describes variable sacs/tubules/chambers connected to the flagellar canal and apposed invaginated plasma/vacuolar membranes. It treats excretion/osmoregulation as likely functions rather than direct transport mechanisms. |
| pusule-agent-klut1987-crossref | https://api.crossref.org/works/10.1139/b87-098; Complete Crossref publisher-deposited abstract and title/authors/DOI/date, not full paper | supports | The exact Klut/Bisalputra/Antia1987 DOI10.1139/b87-098 abstract reports P. micans and A. carterae, tracer entry through the flagellar canal, size responses and a sequential-TEM model. Collar/flagellum flow and broader physiology are proposed; entry into a canal-connected lumen is not proof of transmembrane uptake or nutrient assimilation. |
| pusule-agent-gavelis2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1038/s41598-018-37065-w%22; Complete unique MED identity and abstract | supports | Exact DOI10.1038/s41598-018-37065-w/PMC6351617 identifies Gavelis et al.2019 and the nuclear-net study containing direct pusule microscopy. |
| pusule-agent-gavelis2019-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6351617/fullTextXML; Genuine PMC6351617 JATS: complete Results Sec2, Collection Sec6, TEM Sec7, FIB-SEM Sec8, Figure2 caption/graphic reference and permissions; no supplementary images or other methods certified. | supports | Results explicitly identify pusules as plasma-membrane infoldings, with collecting duct/diverticula in Figure2D/E and contextual anatomy inG/H. Collection describes wild P. kofoidii pseudocolonies; TEM examines four, and FIB-SEM reconstructs one after high-pressure freezing/freeze substitution. Permissions explicitly provide CC BY4.0 and Figure2 has no different credit restriction. |
| pusule-agent-gavelis2019-fig2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6351617.1/41598_2018_37065_Fig2_HTML.jpg; Complete original Figure2 JPEG; printed panels/scales matched to JATS caption | supports | All Figure2 pixels were visually inspected. D shows collecting duct and diverticula; E is the internal surface reconstruction; G/H place the orange pusule beside blue nuclear anatomy. A–C/F are nuclear context, not pusule constituents. Fresh source bytes exactly equal the frozen maintained image and declared SHA2566c37909f2a8a422f0625da79598171847c57a39ec9aad4587239482b31eaeb6a. |
| pusule-agent-gavelis2019-package | https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&amp;prefix=PMC6351617.1/; Complete PMC6351617.1 package listing, exact Figure2 object entry | supports | The native versioned S3 listing includes the exact Fig2 filename/189186bytes and ETag df1b5c4b4cb5d738f4042d41ce50521e, matching the independently calculated image MD5. Version, filename and byte identity are joined to the licensed JATS. |
| pusule-agent-tax271679 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/271679; Complete exact native taxonomy identity | supports | ENA271679 confirms Polykrikos kofoidii at species rank; it does not establish clade-wide organelle frequency. |
| pusule-agent-tax2945 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2945; Complete exact native taxonomy identity | supports | ENA2945 confirms Prorocentrum micans at species rank; it does not establish clade-wide organelle frequency. |
| pusule-agent-tax2961 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2961; Complete exact native taxonomy identity | supports | ENA2961 confirms Amphidinium carterae at species rank; it does not establish clade-wide organelle frequency. |
| local-image | data/images/membrane_organelle/pusule/pmc6351617_fig2.jpg; Frozen complete image; byte comparison and identical source pixels inspected | context_only | The stored image equals the fresh source JPEG and target SHA; its inclusion does not make all contextual structures constituents. |
| boundary-nuclear_net | data/structures/membrane_organelle/nuclear_net.yaml; Identifier, definition, structure-kind and identity-boundary context only | context_only | The neighboring identity is distinct from the canal-connected pusule. Other components, mechanisms and sources in this context record are not independently certified. |
| boundary-contractile_vacuole | data/structures/membrane_organelle/contractile_vacuole.yaml; Identifier, definition, structure-kind and identity-boundary context only | context_only | The neighboring identity is distinct from the canal-connected pusule. Other components, mechanisms and sources in this context record are not independently certified. |
| schema-result | just validate data/structures/membrane_organelle/pusule.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/pusule.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/pusule.yaml --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/pusule-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/pusule.yaml --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/pusule-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch39-20261022-9ejlvnby/pusule-strict.tsv |
| pusule-causal-graphs | /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/pusule.yaml; Complete native read-only log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/pusule.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 9 collected target identifiers returned OK. cellstructuremech:pusule: SKIPPED; Exact local whole-structure identity occurs once in an ignored-inclusive top-level identifier search and is a frozen maintained input. The generic resolver has no external adapter for this locally minted identifier. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Dodge1972 is publisher-summary/identity scope only. Direct publisher fetch returned HTTP200 ClientChallenge, while the actual browser preview supplied the summary; its receipt deliberately records no native HTTP status. The full paper was not recovered.
- Klut1987 is complete publisher-deposited abstract via Crossref; full Methods/controls and figures were not read. Gavelis2019 was read at the declared Results/Methods/permissions/Figure2 scopes, not every cited or supplementary source.
- No function or causal graph is asserted. Unknown physiology and molecular formation requirements are retained; the bounded zero-hit ontology query does not establish universal absence. Neighbor records were read only for the specified identity/boundary context.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes honest clean reviews; no issue was invented for the local issue-only convention. Parent owns finalization, persistence and integration of the five same-base full-corpus gates.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T033001Z-pusule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Pusule scientific review
started_at: '2026-10-22T03:14:09Z'
finished_at: '2026-10-22T03:30:01Z'
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
summary: Source-backed canal-connected pusule identity, membrane anatomy, three bounded
  species examples and exact licensed Figure2 provenance are supported. Unknown physiology
  is retained; no concrete curation finding.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/images/membrane_organelle/pusule/pmc6351617_fig2.jpg
    sha256: 6c37909f2a8a422f0625da79598171847c57a39ec9aad4587239482b31eaeb6a
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole.yaml
    sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
    role: context
  - path: data/structures/membrane_organelle/nuclear_net.yaml
    sha256: 8b4a54d13a70cfb4fdce9bd18ae990793f9de9627fdca067573c033335d847ba
    role: context
  - path: data/structures/membrane_organelle/pusule.yaml
    sha256: 3bc5082b5e3b721414b9b2d57c585c1a278de5053885f34f55b40ccd4b71a6ae
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
- target_id: cellstructuremech:pusule
  path: data/structures/membrane_organelle/pusule.yaml
  label: pusule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/pusule.yaml
    role: maintained scientific record
scope:
  description: Entire single target including every component, hierarchy, taxon/example,
    function/graph, source, discussion and history. Additional frozen local inputs
    are read at the precise scope declared in their evidence rows; literature read
    extents and image inspection are separately stated.
  selection: Batch39 exact path-ordered target 7; fresh f97b native inspection/schema/strict
    passed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:pusule
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: just validate data/structures/membrane_organelle/pusule.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: just validate-strict data/structures/membrane_organelle/pusule.yaml --out
    /private/tmp/cellstructure-batch39-20261022-9ejlvnby/pusule-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/pusule.yaml
  exit_code: 0
  summary: Native check passed; exact scientific scope was assessed separately.
  evidence_ids:
  - pusule-causal-graphs
- check_id: protein-applicability
  name: Individual protein verification applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:pusule
  summary: No individual protein accession or gene/protein graph node occurs in the
    target.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:pusule
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - pusule-agent-go
  - pusule-agent-go-search
  - local-pusule-id
  - pusule-agent-dodge1972-crossref
  - pusule-agent-dodge1972-browser
  - pusule-agent-klut1987-crossref
  - pusule-agent-gavelis2019-meta
  - pusule-agent-gavelis2019-xml
  - pusule-agent-gavelis2019-fig2
  - pusule-agent-gavelis2019-package
  - pusule-agent-tax271679
  - pusule-agent-tax2945
  - pusule-agent-tax2961
  - local-image
  - boundary-nuclear_net
  - boundary-contractile_vacuole
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  summary: '8 of 9 collected target identifiers returned OK. cellstructuremech:pusule:
    SKIPPED; Exact local whole-structure identity occurs once in an ignored-inclusive
    top-level identifier search and is a frozen maintained input. The generic resolver
    has no external adapter for this locally minted identifier. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
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
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/pusule.yaml
  locator: Entire maintained YAML including all fields, graphs, history and discussions
  accessed_at: '2026-10-22T03:22:31Z'
  support: context_only
  summary: The entire target was read; scientific content, status and history remain
    unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent type/grounding/formation-necessity and graph/component_ref
    contracts
  accessed_at: '2026-10-22T03:22:31Z'
  support: context_only
  summary: A LIPID molecular constituent is distinct from a complete GO membrane structure.
    Accurate OTHER structural constituents are not categorically forbidden. Constitution,
    localization, regulatory activity and cell viability do not establish individual
    formation necessity.
- evidence_id: pusule-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043227,GO:0016020
  locator: Complete exact native term definitions
  accessed_at: '2026-10-22T03:15:31.559170Z'
  support: supports
  summary: GO0043227 supplies the broad membrane-bounded-organelle class; GO0016020
    denotes the membrane as bilayer plus associated proteins. The OTHER component
    asserts a structural membrane constituent rather than a chemical lipid identity.
    Canal connection does not make the entire apparatus identical to the plasma membrane.
  snapshot_sha256: 1f9655bc19a55016646e5d2d9ac00ae67695c7d120efca5b4905fa33af04f763
- evidence_id: pusule-agent-go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=pusule&limit=100
  locator: Complete zero-hit QuickGO response
  accessed_at: '2026-10-22T03:15:31.559584Z'
  support: context_only
  summary: The bounded native pusule query returned zero results; it does not establish
    absence from every ontology or alias.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: Native QuickGO GO ontology search query pusule, limit100; complete
    zero-hit response. Scope is this exact remote service/query, not exhaustive ontology
    absence.
- evidence_id: local-pusule-id
  kind: search
  reference: 'rg --no-ignore --hidden -n ^identifier: cellstructuremech:pusule$ data/structures'
  locator: Complete anchored identifier-line search over maintained data/structures
  accessed_at: '2026-10-22T03:20:21.380619Z'
  support: supports
  summary: Exactly one identifier declaration matches cellstructuremech:pusule, the
    frozen target. Ignored and hidden files were included.
  snapshot_sha256: e22298e730362dde57745ba13e8f961057ffec42bf85b41e02e02f8794d30410
  search_scope: All data/structures recursively including ignored and hidden files;
    exact top-level identifier declaration; fresh f97b corpus, exact top-level identifier
    uniqueness only.
- evidence_id: pusule-agent-dodge1972-crossref
  kind: database
  reference: https://api.crossref.org/works/10.1007/BF01279820
  locator: Complete native title/author/DOI/date metadata
  accessed_at: '2026-10-22T03:15:32.289189Z'
  support: supports
  summary: The exact DOI10.1007/BF01279820 identifies J.D. Dodge1972 and the correct
    Protoplasma article. This Crossref response has no abstract.
  snapshot_sha256: 4f2645030cd70f46520080402c6b262016488091ead5bb2a6894a86021c38b23
- evidence_id: pusule-agent-dodge1972-browser
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/BF01279820
  locator: Actual publisher browser-displayed Summary lines31–43 plus title/author/DOI;
    subscription preview only, no full body or native HTTP200 assertion
  accessed_at: '2026-10-22T03:16:22Z'
  support: supports
  summary: The publisher summary calls it the pusule apparatus, describes variable
    sacs/tubules/chambers connected to the flagellar canal and apposed invaginated
    plasma/vacuolar membranes. It treats excretion/osmoregulation as likely functions
    rather than direct transport mechanisms.
  snapshot_sha256: 9647eef89e71d70396018b1b5b38a57c38279ff0cf9bcc58f00d54cf1eda3ee2
- evidence_id: pusule-agent-klut1987-crossref
  kind: database
  reference: https://api.crossref.org/works/10.1139/b87-098
  locator: Complete Crossref publisher-deposited abstract and title/authors/DOI/date,
    not full paper
  accessed_at: '2026-10-22T03:15:32.301501Z'
  support: supports
  summary: The exact Klut/Bisalputra/Antia1987 DOI10.1139/b87-098 abstract reports
    P. micans and A. carterae, tracer entry through the flagellar canal, size responses
    and a sequential-TEM model. Collar/flagellum flow and broader physiology are proposed;
    entry into a canal-connected lumen is not proof of transmembrane uptake or nutrient
    assimilation.
  snapshot_sha256: d50606fb8d46c495b15621bbb3afc00a31f54b8572f6001efc22f0be63b0bf64
- evidence_id: pusule-agent-gavelis2019-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/s41598-018-37065-w%22
  locator: Complete unique MED identity and abstract
  accessed_at: '2026-10-22T02:38:33.607358Z'
  support: supports
  summary: Exact DOI10.1038/s41598-018-37065-w/PMC6351617 identifies Gavelis et al.2019
    and the nuclear-net study containing direct pusule microscopy.
  snapshot_sha256: fc01d9b120d94c26377a8ebefc57a9f05a708234fdbdb3d9d5bc0e018ccec705
- evidence_id: pusule-agent-gavelis2019-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6351617/fullTextXML
  locator: 'Genuine PMC6351617 JATS: complete Results Sec2, Collection Sec6, TEM Sec7,
    FIB-SEM Sec8, Figure2 caption/graphic reference and permissions; no supplementary
    images or other methods certified.'
  accessed_at: '2026-10-22T02:39:03.526125Z'
  support: supports
  summary: Results explicitly identify pusules as plasma-membrane infoldings, with
    collecting duct/diverticula in Figure2D/E and contextual anatomy inG/H. Collection
    describes wild P. kofoidii pseudocolonies; TEM examines four, and FIB-SEM reconstructs
    one after high-pressure freezing/freeze substitution. Permissions explicitly provide
    CC BY4.0 and Figure2 has no different credit restriction.
  snapshot_sha256: 876f436ca2f0d97f7ab622c1442202ec1c4b68b9a0dc68718b213af684c79cc6
- evidence_id: pusule-agent-gavelis2019-fig2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6351617.1/41598_2018_37065_Fig2_HTML.jpg
  locator: Complete original Figure2 JPEG; printed panels/scales matched to JATS caption
  accessed_at: '2026-10-22T03:15:32.332266Z'
  support: supports
  summary: All Figure2 pixels were visually inspected. D shows collecting duct and
    diverticula; E is the internal surface reconstruction; G/H place the orange pusule
    beside blue nuclear anatomy. A–C/F are nuclear context, not pusule constituents.
    Fresh source bytes exactly equal the frozen maintained image and declared SHA2566c37909f2a8a422f0625da79598171847c57a39ec9aad4587239482b31eaeb6a.
  snapshot_sha256: 6c37909f2a8a422f0625da79598171847c57a39ec9aad4587239482b31eaeb6a
- evidence_id: pusule-agent-gavelis2019-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC6351617.1/
  locator: Complete PMC6351617.1 package listing, exact Figure2 object entry
  accessed_at: '2026-10-22T03:15:32.336589Z'
  support: supports
  summary: The native versioned S3 listing includes the exact Fig2 filename/189186bytes
    and ETag df1b5c4b4cb5d738f4042d41ce50521e, matching the independently calculated
    image MD5. Version, filename and byte identity are joined to the licensed JATS.
  snapshot_sha256: acefae52870a79d01eb41f0b80662eb9806d324328710d7ed4ff8cde8055d165
- evidence_id: pusule-agent-tax271679
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/271679
  locator: Complete exact native taxonomy identity
  accessed_at: '2026-10-22T03:15:31.559690Z'
  support: supports
  summary: ENA271679 confirms Polykrikos kofoidii at species rank; it does not establish
    clade-wide organelle frequency.
  snapshot_sha256: 69cb7b45b417f8736d4242226f0b0b8b82fe08c8e4a9e82c667d7a8fa0b26f98
- evidence_id: pusule-agent-tax2945
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2945
  locator: Complete exact native taxonomy identity
  accessed_at: '2026-10-22T03:15:31.559842Z'
  support: supports
  summary: ENA2945 confirms Prorocentrum micans at species rank; it does not establish
    clade-wide organelle frequency.
  snapshot_sha256: e0ac334f3b9b3bb07fa0e608b45d7fe6fa21c04fe5d188c012df3a0318fabe02
- evidence_id: pusule-agent-tax2961
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2961
  locator: Complete exact native taxonomy identity
  accessed_at: '2026-10-22T03:15:31.559946Z'
  support: supports
  summary: ENA2961 confirms Amphidinium carterae at species rank; it does not establish
    clade-wide organelle frequency.
  snapshot_sha256: 0611f7d2024997ec72dd1ddacc0a14a79f14223c2800d75040f841378a22254d
- evidence_id: local-image
  kind: record_content
  reference: data/images/membrane_organelle/pusule/pmc6351617_fig2.jpg
  locator: Frozen complete image; byte comparison and identical source pixels inspected
  accessed_at: '2026-10-22T03:22:31Z'
  support: context_only
  summary: The stored image equals the fresh source JPEG and target SHA; its inclusion
    does not make all contextual structures constituents.
- evidence_id: boundary-nuclear_net
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_net.yaml
  locator: Identifier, definition, structure-kind and identity-boundary context only
  accessed_at: '2026-10-22T03:22:31Z'
  support: context_only
  summary: The neighboring identity is distinct from the canal-connected pusule. Other
    components, mechanisms and sources in this context record are not independently
    certified.
- evidence_id: boundary-contractile_vacuole
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole.yaml
  locator: Identifier, definition, structure-kind and identity-boundary context only
  accessed_at: '2026-10-22T03:22:31Z'
  support: context_only
  summary: The neighboring identity is distinct from the canal-connected pusule. Other
    components, mechanisms and sources in this context record are not independently
    certified.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/pusule.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:14:10Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/pusule.yaml'
  snapshot_sha256: 43959c28d4e71a0b4c33c101cac88589ed74a85fe8982dbe2a0be85e19412b64
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/pusule.yaml --out
    /private/tmp/cellstructure-batch39-20261022-9ejlvnby/pusule-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:14:11Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/pusule.yaml\
    \ --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/pusule-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch39-20261022-9ejlvnby/pusule-strict.tsv"
  snapshot_sha256: 8d008d5ca05df4c21023de7be06fcb867a91d4ccda8c69f5567cac7711d0e11d
- evidence_id: pusule-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/pusule.yaml
  locator: Complete native read-only log
  accessed_at: '2026-10-22T03:20:19.223489Z'
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
  locator: data/structures/membrane_organelle/pusule.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 9 collected target identifiers returned OK. cellstructuremech:pusule:
    SKIPPED; Exact local whole-structure identity occurs once in an ignored-inclusive
    top-level identifier search and is a frozen maintained input. The generic resolver
    has no external adapter for this locally minted identifier. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
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
  topic: Local identity and open canal topology
  outcome: supported
  target_ids:
  - cellstructuremech:pusule
  summary: The source-backed local identifier is unique in the ignored-inclusive corpus
    and no exact term is returned by the bounded GO query. Dodge supports the apparatus
    synonym and two-membrane wall connected to the flagellar canal. Broad organelle
    typing does not assert a sealed lumen; nuclear net and contractile vacuole are
    separate identities.
  evidence_ids:
  - record
  - pusule-agent-go
  - pusule-agent-go-search
  - local-pusule-id
  - pusule-agent-dodge1972-crossref
  - pusule-agent-dodge1972-browser
  - pusule-agent-gavelis2019-xml
  - boundary-nuclear_net
  - boundary-contractile_vacuole
- assessment_id: composition
  area: grounding
  topic: Structural membrane constituent
  outcome: supported
  target_ids:
  - cellstructuremech:pusule
  summary: OTHER/GO0016020 is an accurate structural membrane representation, with
    UNKNOWN essentiality and no chemical-species assertion. The apposed membranes
    are directly described in Dodge summary; no speculative proteins, nuclear ribbons
    or rootlets are inserted.
  evidence_ids:
  - record
  - schema
  - pusule-agent-go
  - pusule-agent-dodge1972-browser
  - pusule-agent-gavelis2019-xml
- assessment_id: necessity
  area: evidence
  topic: Physiology and individual formation requirements
  outcome: unknown
  target_ids:
  - cellstructuremech:pusule
  summary: UNKNOWN essentiality remains appropriate. Tracer entry and static membrane
    morphology do not establish molecular assembly necessity, transmembrane transport,
    a contractile cycle or a particular physiological mechanism. The open discussion
    is accurately conservative.
  evidence_ids:
  - record
  - schema
  - pusule-agent-dodge1972-browser
  - pusule-agent-klut1987-crossref
  - pusule-agent-gavelis2019-xml
- assessment_id: examples
  area: scope
  topic: Three bounded species examples
  outcome: supported
  target_ids:
  - cellstructuremech:pusule
  summary: Each taxon identity is exact. P. kofoidii has directly inspected primary
    ultrastructure and collection context; P. micans/A. carterae examples are explicitly
    abstract-only tracer/TEM scope. No distribution prevalence is inferred.
  evidence_ids:
  - record
  - pusule-agent-klut1987-crossref
  - pusule-agent-gavelis2019-meta
  - pusule-agent-gavelis2019-xml
  - pusule-agent-tax271679
  - pusule-agent-tax2945
  - pusule-agent-tax2961
- assessment_id: image
  area: provenance
  topic: Exact Figure2 provenance and anatomical caption
  outcome: supported
  target_ids:
  - cellstructuremech:pusule
  summary: The stored/source SHA, source version/filename, native package ETag/calculated
    MD5, authorship and exact CC BY4.0 permissions agree. Visual panels and caption
    preserve the collecting duct/diverticula versus adjacent nuclear anatomy distinction.
  evidence_ids:
  - record
  - local-image
  - pusule-agent-gavelis2019-xml
  - pusule-agent-gavelis2019-fig2
  - pusule-agent-gavelis2019-package
- assessment_id: provenance
  area: provenance
  topic: Bounded source audit and unchanged status
  outcome: supported
  target_ids:
  - cellstructuremech:pusule
  summary: All target claims were reviewed at the declared source read scopes, with
    primary/secondary/abstract/native authority tiers separated. No scientific mutation,
    mapping-status promotion, review persistence or publication is implied.
  evidence_ids:
  - record
  - pusule-agent-go
  - pusule-agent-dodge1972-crossref
  - pusule-agent-dodge1972-browser
  - pusule-agent-klut1987-crossref
  - pusule-agent-gavelis2019-meta
  - pusule-agent-gavelis2019-xml
  - pusule-agent-gavelis2019-fig2
  - pusule-agent-gavelis2019-package
  - pusule-agent-tax271679
  - pusule-agent-tax2945
  - pusule-agent-tax2961
findings: []
actions: []
limitations:
- Dodge1972 is publisher-summary/identity scope only. Direct publisher fetch returned
  HTTP200 ClientChallenge, while the actual browser preview supplied the summary;
  its receipt deliberately records no native HTTP status. The full paper was not recovered.
- Klut1987 is complete publisher-deposited abstract via Crossref; full Methods/controls
  and figures were not read. Gavelis2019 was read at the declared Results/Methods/permissions/Figure2
  scopes, not every cited or supplementary source.
- No function or causal graph is asserted. Unknown physiology and molecular formation
  requirements are retained; the bounded zero-hit ontology query does not establish
  universal absence. Neighbor records were read only for the specified identity/boundary
  context.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes honest clean reviews; no issue was invented for
  the local issue-only convention. Parent owns finalization, persistence and integration
  of the five same-base full-corpus gates.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
