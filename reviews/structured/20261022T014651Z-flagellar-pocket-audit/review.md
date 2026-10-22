# Flagellar pocket identity, source scope and boundary review

- Review: 20261022T014651Z-flagellar-pocket-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:27:33Z
- Finished UTC: 2026-10-22T01:46:51Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The pocket identity, species scope, collar and descriptive topology are supported. One major molecular-grounding mismatch remains: the LIPID component identifies the complete pocket membrane, and its component_ref propagates that mismatch into the graph.

## Scope And Provenance

Whole single target and frozen boundary neighbors; exact native IDs, source identities and claim-bearing primary/review passages audited with per-source reading limits.

Selection: Target 1 of batch twenty-nine in strict uncovered path order; initial native inspect/schema/strict passed on fresh base f97b1abe before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0020016 | data/structures/membrane_organelle/flagellar_pocket.yaml | maintained | flagellar pocket |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0020016 | Focused validator passed. |
| Focused native strict | passed | True | GO:0020016 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0020016 | No expression-module membership, regulatory network or transcriptomic claim is used. |
| Claim-level scientific review | passed | True | GO:0020016 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0020016 | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0020016 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0020016 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0020016 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0020016 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0020016 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Pocket region versus bounding membrane and neck collar

identity: supported. Targets: GO:0020016.

The exact GO identity, accepted flagellar synonym and membrane-invagination definition match. Native GO and frozen neighbors distinguish the pocket, its complete membrane and its exit-neck collar. That sound structural distinction does not make the complete membrane term a lipid molecular identity; the component-grounding finding is assessed separately.

### Constituent identity and scoped formation evidence

grounding: concern. Targets: GO:0020016.

GO0020018 identifies the entire ciliary pocket membrane, whereas the schema defines a StructuralComponent as a molecular building block and a LIPID grounding as chemical identity. The asserted LIPID-to-whole-membrane mapping therefore exceeds the field contract. Native membrane parthood and primary architecture remain correct. The protein-complex collar grounding and BILBO1-dependent new-pocket biogenesis in the defined procyclic assay remain supported; neither proves every collar subunit necessary.

### Species occurrence, experimental stages and canonical example

scope: supported. Targets: GO:0020016.

T. brucei is the correct species. The qualitative COMMON row and canonical architecture/biogenesis example are supported by tomography and BILBO1 work. The single-pocket statement describes the usual organelle arrangement, not an explicit denial of duplication before cell division. Procyclic427 tomography, EATRO1125-T7T biogenesis and bloodstream domain/uptake experiments are kept distinct.

### Traffic gateway and descriptive exit-neck organization

graph: concern. Targets: GO:0020016.

All three descriptive topology/localization/gateway edges and NONMECHANISTIC scope are supported at their declared source tiers. The membrane node itself correctly denotes GO0020018, but its component_ref binds that complete membrane to the molecular LIPID row and propagates F1. Preserve the structural node and edges while correcting that correspondence. Cold-blocked marker accumulation is not a resolved transport mechanism.

### Optional expansion of cytoskeletal inventory

completeness: supported. Targets: GO:0020016.

The acknowledged hook/MtQ/FAZ and membrane-protein TODO does not invalidate the current bounded constituent model. No required complete molecular inventory is claimed or inferred from this optional gap.

### Whole maintained target and bounded review outcome

completeness: supported. Targets: GO:0020016.

Every maintained claim, evidence item, graph edge and discussion was inspected. The single major finding concerns molecular identity in one component and its graph correspondence, not the accepted whole-pocket identity, topology or optional inventory. No measurement, image asset or quotation requires separate numerical/licence/quotation verification. Existing status/history remain unchanged.

## Findings

### F1: Separate the complete pocket membrane from its molecular lipid constituent

major / open / confirmed; issue key: flagellar-pocket-lipid-whole-membrane-grounding.

The ciliary_pocket_membrane row has component_type LIPID but grounding GO:0020018, whose native identity is the complete ciliary pocket membrane. Schema StructuralComponent requires a molecular building block and distinguishes chemical lipid grounding from GO sub-complex grounding. The graph component_ref repeats the same invalid molecular correspondence. Correct membrane topology and membrane/collar membership do not resolve this field-level identity mismatch.

## Recommended Actions And Acceptance Checks

### A1

In a separately authorized curation change, retain the complete membrane as structural topology and represent only a source-supported molecular lipid material in components, using exact chemical grounding where justified or an explicitly reviewed label-only material. Correct/remove the graph component_ref so it does not equate the whole membrane with that molecular entry.

- Confirm that every LIPID grounding identifies lipid material, not GO0020018 as the whole membrane; do not invent an exact lipid mixture or assign an arbitrary CHEBI term.
- Preserve the correctly grounded membrane STRUCTURE node and descriptive edges, the pocket identity, and the GO-grounded protein-complex collar.
- Run focused schema, grounding/product and graph checks after separately authorized scientific curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/flagellar_pocket.yaml; Entire maintained YAML, including all components, taxonomy, canonical examples, functions, graph edges, discussions and history | context_only | The whole exact target was inspected without scientific edits or native status promotion. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component grounding, component_ref, essentiality, structure-kind and graph contracts | context_only | Assembly necessity differs from catalytic activity, membership and collective material identity. A membrane boundary, the enclosed volume and the whole organelle are distinct. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Source scope and mechanistic-versus-descriptive graph guidance | context_only | Descriptive topology and localization can be represented honestly as NONMECHANISTIC without inventing a molecular mechanism. |
| membrane-neighbor | data/structures/membrane_organelle/ciliary_pocket_membrane.yaml; Entire frozen neighboring record, read for boundary identity and parthood only | context_only | This is context for distinguishing pocket membrane and exit-neck collar from the entire pocket, not another review target. |
| collar-neighbor | data/structures/cytoskeleton/ciliary_pocket_collar.yaml; Entire frozen neighboring record, read for boundary identity and parthood only | context_only | This is context for distinguishing pocket membrane and exit-neck collar from the entire pocket, not another review target. |
| flagellar-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020016,GO:0020018,GO:0060170,GO:1990900; All four native exact terms: IDs, active flags, labels, definitions, synonyms and relevant children | supports | Active GO0020016 is ciliary pocket with exact synonym flagellar pocket and the same membrane-invagination definition. GO0020018 denotes its membrane, and GO1990900 its exit-site collar; both are explicitly part_of children of the pocket. GO0060170 supplies ciliary-membrane context, not whole-pocket identity. |
| flagellar-agent-tax-5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Exact taxId, scientificName, rank, lineage and alternate names | supports | ENA identifies 5691 as Trypanosoma brucei, species rank and trypanosomatid lineage. It does not alone determine strain, life stage or occurrence frequency. |
| flagellar-agent-doi-10.1038_nrmicro2221 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nrmicro2221; Exact bibliographic identity and complete abstract; detailed primary claims use the separately inspected body | supports | Native MED identifies The trypanosome flagellar pocket. by Field MC, Carrington M. (2009), DOI 10.1038/nrmicro2221, PMID 19806154. This is review-tier context, not a new primary experiment. |
| flagellar-agent-doi-10.1242_jcs.045740 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1242/jcs.045740; Exact bibliographic identity and complete abstract; detailed primary claims use the separately inspected body | supports | Native MED identifies Three-dimensional cellular architecture of the flagellar pocket and associated cytoskeleton in trypanosomes revealed by electron microscope tomography. by Lacomble S, Vaughan S, Gadelha C, Morphew MK, Shaw MK, McIntosh JR, Gull K. (2009), DOI 10.1242/jcs.045740, PMID 19299460.  |
| flagellar-agent-doi-10.1073_pnas.0909289106 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0909289106; Exact bibliographic identity and complete abstract; detailed primary claims use the separately inspected body | supports | Native MED identifies Membrane domains and flagellar pocket boundaries are influenced by the cytoskeleton in African trypanosomes. by Gadelha C, Rothery S, Morphew M, McIntosh JR, Severs NJ, Gull K. (2009), DOI 10.1073/pnas.0909289106, PMID 19805090.  |
| flagellar-agent-doi-10.1016_j.pt.2020.11.005 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.pt.2020.11.005; Exact bibliographic identity and complete abstract; detailed primary claims use the separately inspected body | supports | Native MED identifies Trypanosomatid Flagellar Pocket from Structure to Function. by Halliday C, de Castro-Neto A, Alcantara CL, Cunha-E-Silva NL, Vaughan S, Sunter JD. (2021), DOI 10.1016/j.pt.2020.11.005, PMID 33308952. This is review-tier context, not a new primary experiment. |
| flagellar-agent-bonhivers2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1371/journal.pbio.0060105; Exact bibliographic identity and complete abstract; detailed primary claims use the separately inspected body | supports | Native MED identifies Biogenesis of the trypanosome endo-exocytotic organelle is cytoskeleton mediated. by Bonhivers M, Nowacki S, Landrein N, Robinson DR. (2008), DOI 10.1371/journal.pbio.0060105, PMID 18462016.  |
| flagellar-agent-field2009-publisher | https://www.nature.com/articles/nrmicro2221; Key Points and complete abstract only; surrounding bibliographic material confirms identity. No full review body inspected. | supports | The review Key Points and complete abstract describe a plasma-membrane invagination, its specialized trafficking role and connections to polarity/division. The retrieved publisher page is a subscription preview; a full scientific body is not claimed. |
| flagellar-agent-pmc-PMC2714436 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2714436/; Complete Summary and Introduction; complete Results subsections Flagellar pocket architecture in procyclic trypanosomes and Flagellar pocket boundaries, including Fig1–4 captions; Discussion opening through its first neck-region paragraph; complete main Materials and Methods. Other Results/Discussion portions, figure pixels and supplementary movies not independently assessed. | supports | Procyclic electron tomography distinguishes the exit-neck collar from the basal entry collarette/transitional-fibre boundary and describes the pocket as an asymmetric membrane enclosure associated with MtQ/FAZ. Methods identify 427 procyclic cells at28C. This establishes architecture; cell-cycle duplication prevents treating the usual single pocket as an invariant count at every stage. |
| flagellar-agent-pmc-PMC2755463 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2755463/; Complete abstract, Introduction, Results, Discussion and main Methods; Fig1–6 captions. Separate supporting Methods, raw data and image pixels not inspected. | supports | Bloodstream-form microscopy and endocytic-marker assays identify distinct surface-membrane domains and cytoskeletal boundaries. Cold-blocked marker accumulation and normal37C uptake are distinguished; the proposed channel route and active/passive alternatives are not a resolved transport mechanism. Collar-associated membrane boundaries are not equated with every cytoskeletal structure around the pocket. |
| flagellar-agent-bonhivers2008-plos | https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0060105&amp;type=manuscript; Complete Introduction s1; Results s2a–s2c and included Fig1–4 captions; Discussion s3a and s3d; Methods s4a, s4e and s4i. Remaining Results/Discussion/Methods, supplementary data and figure pixels not independently read. | supports | BILBO1-eGFP and immunolabeling identify the collar at the flagellar exit site. Procyclic RNAi prevents new collar/pocket formation while the old collar retains BILBO1; new flagella can still form. The principal biogenesis experiment is EATRO1125-T7T procyclic cells, while42790–13 bloodstream cells establish growth lethality. This is not a claim that every collar protein is separately necessary or that exocytic flux was directly measured. |
| flagellar-agent-halliday2021-publisher | https://doi.org/10.1016/j.pt.2020.11.005; Actual response body and content check; not scientific article text | context_only | The publisher route returned HTTP200 but only a short access/challenge page, not the review body. The complete native MED abstract is the actual inspected scientific scope. |
| schema-result | just validate data/structures/membrane_organelle/flagellar_pocket.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/flagellar_pocket.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/flagellar_pocket.yaml --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/flagellar_pocket-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/flagellar_pocket.yaml --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/flagellar_pocket-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch29-20261022-_v0k34u7/flagellar_pocket-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/flagellar_pocket.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Field2009 is inspected as its publisher Key Points and complete abstract; Halliday2021 as the complete native MED abstract. Neither full review body was recovered, and an HTTP200 access stub is not treated as one.
- Primary reading scopes are enumerated per evidence row. Lacomble inspection covers the two principal architecture/boundary Results subsections, selected Discussion and complete main Methods; Bonhivers covers the specified Results/Discussion/Methods sections. No full-body claim is made for the remaining sections. Gadelha main scientific text and main Methods were read completely. No figure pixels, raw data or supplementary movies were independently analyzed.
- The usual single-pocket arrangement changes during cell-cycle duplication. Species-level COMMON is not a counted prevalence estimate, and biochemical or morphogenetic evidence from one life stage is not silently transferred to another.
- Exact lipid mixture, complete collar molecular composition and universal individual component requirements were not established. These are bounded scientific limits, not defects inferred from optional empty slots.
- This finding does not require a complete membrane proteome, a new collar inventory or a measured lipid mixture; those optional unknowns remain limitations.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requires a validated review for each uncovered target, including an honest clean review; no issue is invented to satisfy the local issue-only output rule.
- Remote evidence preserves original request URL, actual UTC access timestamp and raw SHA256; reused batch22 sources retain their original receipts. Fresh target resolver results use the completed same-base batch26 native report; broader finalization is reserved to the parent.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T014651Z-flagellar-pocket-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Flagellar pocket identity, source scope and boundary review
started_at: '2026-10-22T01:27:33Z'
finished_at: '2026-10-22T01:46:51Z'
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
summary: 'The pocket identity, species scope, collar and descriptive topology are
  supported. One major molecular-grounding mismatch remains: the LIPID component identifies
  the complete pocket membrane, and its component_ref propagates that mismatch into
  the graph.'
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
  - path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    sha256: df0530c9582d0a40d8e0c646cdaa88cc0872d1e6e034cbdcd068b2a3f426ec3a
    role: context
  - path: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
    sha256: acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0
    role: context
  - path: data/structures/membrane_organelle/flagellar_pocket.yaml
    sha256: d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8
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
- target_id: GO:0020016
  path: data/structures/membrane_organelle/flagellar_pocket.yaml
  label: flagellar pocket
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/flagellar_pocket.yaml
    role: maintained scientific record
scope:
  description: Whole single target and frozen boundary neighbors; exact native IDs,
    source identities and claim-bearing primary/review passages audited with per-source
    reading limits.
  selection: Target 1 of batch twenty-nine in strict uncovered path order; initial
    native inspect/schema/strict passed on fresh base f97b1abe before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0020016
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0020016
  command: just validate data/structures/membrane_organelle/flagellar_pocket.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0020016
  command: just validate-strict data/structures/membrane_organelle/flagellar_pocket.yaml
    --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/flagellar_pocket-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0020016
  summary: No expression-module membership, regulatory network or transcriptomic claim
    is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0020016
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - membrane-neighbor
  - collar-neighbor
  - flagellar-agent-go
  - flagellar-agent-tax-5691
  - flagellar-agent-doi-10.1038_nrmicro2221
  - flagellar-agent-doi-10.1242_jcs.045740
  - flagellar-agent-doi-10.1073_pnas.0909289106
  - flagellar-agent-doi-10.1016_j.pt.2020.11.005
  - flagellar-agent-bonhivers2008-meta
  - flagellar-agent-field2009-publisher
  - flagellar-agent-pmc-PMC2714436
  - flagellar-agent-pmc-PMC2755463
  - flagellar-agent-bonhivers2008-plos
  - flagellar-agent-halliday2021-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0020016
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
  - GO:0020016
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0020016
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0020016
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0020016
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0020016
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
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/flagellar_pocket.yaml
  locator: Entire maintained YAML, including all components, taxonomy, canonical examples,
    functions, graph edges, discussions and history
  accessed_at: '2026-10-22T01:38:00Z'
  support: context_only
  summary: The whole exact target was inspected without scientific edits or native
    status promotion.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component grounding, component_ref, essentiality, structure-kind and graph
    contracts
  accessed_at: '2026-10-22T01:38:00Z'
  support: context_only
  summary: Assembly necessity differs from catalytic activity, membership and collective
    material identity. A membrane boundary, the enclosed volume and the whole organelle
    are distinct.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Source scope and mechanistic-versus-descriptive graph guidance
  accessed_at: '2026-10-22T01:38:00Z'
  support: context_only
  summary: Descriptive topology and localization can be represented honestly as NONMECHANISTIC
    without inventing a molecular mechanism.
- evidence_id: membrane-neighbor
  kind: record_content
  reference: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  locator: Entire frozen neighboring record, read for boundary identity and parthood
    only
  accessed_at: '2026-10-22T01:38:00Z'
  support: context_only
  summary: This is context for distinguishing pocket membrane and exit-neck collar
    from the entire pocket, not another review target.
- evidence_id: collar-neighbor
  kind: record_content
  reference: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
  locator: Entire frozen neighboring record, read for boundary identity and parthood
    only
  accessed_at: '2026-10-22T01:38:00Z'
  support: context_only
  summary: This is context for distinguishing pocket membrane and exit-neck collar
    from the entire pocket, not another review target.
- evidence_id: flagellar-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020016,GO:0020018,GO:0060170,GO:1990900
  locator: 'All four native exact terms: IDs, active flags, labels, definitions, synonyms
    and relevant children'
  accessed_at: '2026-10-21T10:51:30.561260Z'
  support: supports
  summary: Active GO0020016 is ciliary pocket with exact synonym flagellar pocket
    and the same membrane-invagination definition. GO0020018 denotes its membrane,
    and GO1990900 its exit-site collar; both are explicitly part_of children of the
    pocket. GO0060170 supplies ciliary-membrane context, not whole-pocket identity.
  snapshot_sha256: d86d3d966784eb15a91838b089711e2c7dce354317aa7a9d036376fb18b114d5
- evidence_id: flagellar-agent-tax-5691
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-10-21T10:51:30.561607Z'
  support: supports
  summary: ENA identifies 5691 as Trypanosoma brucei, species rank and trypanosomatid
    lineage. It does not alone determine strain, life stage or occurrence frequency.
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: flagellar-agent-doi-10.1038_nrmicro2221
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrmicro2221
  locator: Exact bibliographic identity and complete abstract; detailed primary claims
    use the separately inspected body
  accessed_at: '2026-10-21T10:51:30.561895Z'
  support: supports
  summary: Native MED identifies The trypanosome flagellar pocket. by Field MC, Carrington
    M. (2009), DOI 10.1038/nrmicro2221, PMID 19806154. This is review-tier context,
    not a new primary experiment.
  snapshot_sha256: 90dfa2be054c3fe7a235ea43f9cfd9b82bca69f4cc6aaf5e8114e2364a46f55a
- evidence_id: flagellar-agent-doi-10.1242_jcs.045740
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1242/jcs.045740
  locator: Exact bibliographic identity and complete abstract; detailed primary claims
    use the separately inspected body
  accessed_at: '2026-10-21T10:51:31.278446Z'
  support: supports
  summary: 'Native MED identifies Three-dimensional cellular architecture of the flagellar
    pocket and associated cytoskeleton in trypanosomes revealed by electron microscope
    tomography. by Lacomble S, Vaughan S, Gadelha C, Morphew MK, Shaw MK, McIntosh
    JR, Gull K. (2009), DOI 10.1242/jcs.045740, PMID 19299460. '
  snapshot_sha256: ab85e1b67afa139c3840f4cd1e58a0ecd9913aa645103352341a8824a397800b
- evidence_id: flagellar-agent-doi-10.1073_pnas.0909289106
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0909289106
  locator: Exact bibliographic identity and complete abstract; detailed primary claims
    use the separately inspected body
  accessed_at: '2026-10-21T10:51:30.562007Z'
  support: supports
  summary: 'Native MED identifies Membrane domains and flagellar pocket boundaries
    are influenced by the cytoskeleton in African trypanosomes. by Gadelha C, Rothery
    S, Morphew M, McIntosh JR, Severs NJ, Gull K. (2009), DOI 10.1073/pnas.0909289106,
    PMID 19805090. '
  snapshot_sha256: 1e0d2e19103f1a6f98801b00012315427a396610d687351c10fecc37037093bb
- evidence_id: flagellar-agent-doi-10.1016_j.pt.2020.11.005
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.pt.2020.11.005
  locator: Exact bibliographic identity and complete abstract; detailed primary claims
    use the separately inspected body
  accessed_at: '2026-10-21T10:51:30.561764Z'
  support: supports
  summary: Native MED identifies Trypanosomatid Flagellar Pocket from Structure to
    Function. by Halliday C, de Castro-Neto A, Alcantara CL, Cunha-E-Silva NL, Vaughan
    S, Sunter JD. (2021), DOI 10.1016/j.pt.2020.11.005, PMID 33308952. This is review-tier
    context, not a new primary experiment.
  snapshot_sha256: 81206ea5842bd81a66c41534c2ee52ae977be1b7fa8ec29016b002c91d64d25b
- evidence_id: flagellar-agent-bonhivers2008-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1371/journal.pbio.0060105
  locator: Exact bibliographic identity and complete abstract; detailed primary claims
    use the separately inspected body
  accessed_at: '2026-10-22T01:33:09.453244Z'
  support: supports
  summary: 'Native MED identifies Biogenesis of the trypanosome endo-exocytotic organelle
    is cytoskeleton mediated. by Bonhivers M, Nowacki S, Landrein N, Robinson DR.
    (2008), DOI 10.1371/journal.pbio.0060105, PMID 18462016. '
  snapshot_sha256: 8aac9d85fe19ea5e2c9aa42931cafadc60f408b34fc2ba23ed126eb1665a01e8
- evidence_id: flagellar-agent-field2009-publisher
  kind: authority
  reference: https://www.nature.com/articles/nrmicro2221
  locator: Key Points and complete abstract only; surrounding bibliographic material
    confirms identity. No full review body inspected.
  accessed_at: '2026-10-21T10:52:01.215423Z'
  support: supports
  summary: The review Key Points and complete abstract describe a plasma-membrane
    invagination, its specialized trafficking role and connections to polarity/division.
    The retrieved publisher page is a subscription preview; a full scientific body
    is not claimed.
  snapshot_sha256: 7aa1da772a876400d8169216dd2ff1ced8635fb3e666afefd25f3effd4bd2144
- evidence_id: flagellar-agent-pmc-PMC2714436
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2714436/
  locator: Complete Summary and Introduction; complete Results subsections Flagellar
    pocket architecture in procyclic trypanosomes and Flagellar pocket boundaries,
    including Fig1–4 captions; Discussion opening through its first neck-region paragraph;
    complete main Materials and Methods. Other Results/Discussion portions, figure
    pixels and supplementary movies not independently assessed.
  accessed_at: '2026-10-21T10:52:00.889852Z'
  support: supports
  summary: Procyclic electron tomography distinguishes the exit-neck collar from the
    basal entry collarette/transitional-fibre boundary and describes the pocket as
    an asymmetric membrane enclosure associated with MtQ/FAZ. Methods identify 427
    procyclic cells at28C. This establishes architecture; cell-cycle duplication prevents
    treating the usual single pocket as an invariant count at every stage.
  snapshot_sha256: ca424ebc26ba0b12693d29556013e5f3d83fdbec74c99b4c23e48a459bb340b7
- evidence_id: flagellar-agent-pmc-PMC2755463
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2755463/
  locator: Complete abstract, Introduction, Results, Discussion and main Methods;
    Fig1–6 captions. Separate supporting Methods, raw data and image pixels not inspected.
  accessed_at: '2026-10-21T10:52:00.889584Z'
  support: supports
  summary: Bloodstream-form microscopy and endocytic-marker assays identify distinct
    surface-membrane domains and cytoskeletal boundaries. Cold-blocked marker accumulation
    and normal37C uptake are distinguished; the proposed channel route and active/passive
    alternatives are not a resolved transport mechanism. Collar-associated membrane
    boundaries are not equated with every cytoskeletal structure around the pocket.
  snapshot_sha256: 487f14e3deacf17be235631744cc2845674dd5cfb332d08e44262f41a49fa850
- evidence_id: flagellar-agent-bonhivers2008-plos
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0060105&type=manuscript
  locator: Complete Introduction s1; Results s2a–s2c and included Fig1–4 captions;
    Discussion s3a and s3d; Methods s4a, s4e and s4i. Remaining Results/Discussion/Methods,
    supplementary data and figure pixels not independently read.
  accessed_at: '2026-10-22T01:33:09.460299Z'
  support: supports
  summary: BILBO1-eGFP and immunolabeling identify the collar at the flagellar exit
    site. Procyclic RNAi prevents new collar/pocket formation while the old collar
    retains BILBO1; new flagella can still form. The principal biogenesis experiment
    is EATRO1125-T7T procyclic cells, while42790–13 bloodstream cells establish growth
    lethality. This is not a claim that every collar protein is separately necessary
    or that exocytic flux was directly measured.
  snapshot_sha256: 559b71fe763193b9f919a4d853e2242072ebaf0fd44bfece2c78b6ee925391aa
- evidence_id: flagellar-agent-halliday2021-publisher
  kind: authority
  reference: https://doi.org/10.1016/j.pt.2020.11.005
  locator: Actual response body and content check; not scientific article text
  accessed_at: '2026-10-21T10:52:01.216138Z'
  support: context_only
  summary: The publisher route returned HTTP200 but only a short access/challenge
    page, not the review body. The complete native MED abstract is the actual inspected
    scientific scope.
  snapshot_sha256: c107afaf835af1937e35c50c624dc60406a92b24e67201ef2bb80803496b308c
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/flagellar_pocket.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:27:34Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/flagellar_pocket.yaml'
  snapshot_sha256: 0fcd8b9d0125c96c7304dbdbea7f5c91e7b922ee457f76a976171858c2f14e3a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/flagellar_pocket.yaml
    --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/flagellar_pocket-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:27:35Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/flagellar_pocket.yaml\
    \ --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/flagellar_pocket-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch29-20261022-_v0k34u7/flagellar_pocket-strict.tsv"
  snapshot_sha256: 4d063142e8286af112f6f4b7ae9d65cbb124b2736c5ad957ba99fb2ee190da05
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/flagellar_pocket.yaml; native collect()
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
  topic: Pocket region versus bounding membrane and neck collar
  outcome: supported
  target_ids:
  - GO:0020016
  summary: The exact GO identity, accepted flagellar synonym and membrane-invagination
    definition match. Native GO and frozen neighbors distinguish the pocket, its complete
    membrane and its exit-neck collar. That sound structural distinction does not
    make the complete membrane term a lipid molecular identity; the component-grounding
    finding is assessed separately.
  evidence_ids:
  - record
  - membrane-neighbor
  - collar-neighbor
  - flagellar-agent-go
  - flagellar-agent-pmc-PMC2714436
- assessment_id: components
  area: grounding
  topic: Constituent identity and scoped formation evidence
  outcome: concern
  target_ids:
  - GO:0020016
  summary: GO0020018 identifies the entire ciliary pocket membrane, whereas the schema
    defines a StructuralComponent as a molecular building block and a LIPID grounding
    as chemical identity. The asserted LIPID-to-whole-membrane mapping therefore exceeds
    the field contract. Native membrane parthood and primary architecture remain correct.
    The protein-complex collar grounding and BILBO1-dependent new-pocket biogenesis
    in the defined procyclic assay remain supported; neither proves every collar subunit
    necessary.
  evidence_ids:
  - record
  - policy
  - flagellar-agent-go
  - flagellar-agent-pmc-PMC2755463
  - flagellar-agent-bonhivers2008-plos
- assessment_id: scope
  area: scope
  topic: Species occurrence, experimental stages and canonical example
  outcome: supported
  target_ids:
  - GO:0020016
  summary: T. brucei is the correct species. The qualitative COMMON row and canonical
    architecture/biogenesis example are supported by tomography and BILBO1 work. The
    single-pocket statement describes the usual organelle arrangement, not an explicit
    denial of duplication before cell division. Procyclic427 tomography, EATRO1125-T7T
    biogenesis and bloodstream domain/uptake experiments are kept distinct.
  evidence_ids:
  - record
  - flagellar-agent-tax-5691
  - flagellar-agent-pmc-PMC2714436
  - flagellar-agent-pmc-PMC2755463
  - flagellar-agent-bonhivers2008-plos
- assessment_id: function-graph
  area: graph
  topic: Traffic gateway and descriptive exit-neck organization
  outcome: concern
  target_ids:
  - GO:0020016
  summary: All three descriptive topology/localization/gateway edges and NONMECHANISTIC
    scope are supported at their declared source tiers. The membrane node itself correctly
    denotes GO0020018, but its component_ref binds that complete membrane to the molecular
    LIPID row and propagates F1. Preserve the structural node and edges while correcting
    that correspondence. Cold-blocked marker accumulation is not a resolved transport
    mechanism.
  evidence_ids:
  - record
  - graph-policy
  - flagellar-agent-go
  - flagellar-agent-field2009-publisher
  - flagellar-agent-pmc-PMC2714436
  - flagellar-agent-pmc-PMC2755463
  - flagellar-agent-bonhivers2008-plos
  - flagellar-agent-doi-10.1038_nrmicro2221
  - flagellar-agent-doi-10.1242_jcs.045740
  - flagellar-agent-doi-10.1073_pnas.0909289106
  - flagellar-agent-doi-10.1016_j.pt.2020.11.005
- assessment_id: inventory
  area: completeness
  topic: Optional expansion of cytoskeletal inventory
  outcome: supported
  target_ids:
  - GO:0020016
  summary: The acknowledged hook/MtQ/FAZ and membrane-protein TODO does not invalidate
    the current bounded constituent model. No required complete molecular inventory
    is claimed or inferred from this optional gap.
  evidence_ids:
  - record
  - flagellar-agent-pmc-PMC2714436
  - flagellar-agent-pmc-PMC2755463
  - flagellar-agent-bonhivers2008-plos
- assessment_id: coverage
  area: completeness
  topic: Whole maintained target and bounded review outcome
  outcome: supported
  target_ids:
  - GO:0020016
  summary: Every maintained claim, evidence item, graph edge and discussion was inspected.
    The single major finding concerns molecular identity in one component and its
    graph correspondence, not the accepted whole-pocket identity, topology or optional
    inventory. No measurement, image asset or quotation requires separate numerical/licence/quotation
    verification. Existing status/history remain unchanged.
  evidence_ids:
  - record
  - policy
findings:
- finding_id: F1
  issue_key: flagellar-pocket-lipid-whole-membrane-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate the complete pocket membrane from its molecular lipid constituent
  description: The ciliary_pocket_membrane row has component_type LIPID but grounding
    GO:0020018, whose native identity is the complete ciliary pocket membrane. Schema
    StructuralComponent requires a molecular building block and distinguishes chemical
    lipid grounding from GO sub-complex grounding. The graph component_ref repeats
    the same invalid molecular correspondence. Correct membrane topology and membrane/collar
    membership do not resolve this field-level identity mismatch.
  target_ids:
  - GO:0020016
  field_paths:
  - components#ciliary_pocket_membrane.component_type
  - components#ciliary_pocket_membrane.grounding
  - causal_graphs#pocket_boundary_and_traffic.nodes#ciliary_pocket_membrane.component_ref
  evidence_ids:
  - record
  - policy
  - flagellar-agent-go
  - flagellar-agent-pmc-PMC2755463
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/flagellar_pocket.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity and source scope
  native_severity: major
  normalization_reason: Major because an asserted molecular component is grounded
    to a distinct complete structure and that correspondence propagates into the graph;
    the organelle identity and descriptive boundary are intact and are not the basis
    for a higher severity.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0020016
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/flagellar_pocket.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, retain the complete membrane
    as structural topology and represent only a source-supported molecular lipid material
    in components, using exact chemical grounding where justified or an explicitly
    reviewed label-only material. Correct/remove the graph component_ref so it does
    not equate the whole membrane with that molecular entry.
  acceptance_checks:
  - Confirm that every LIPID grounding identifies lipid material, not GO0020018 as
    the whole membrane; do not invent an exact lipid mixture or assign an arbitrary
    CHEBI term.
  - Preserve the correctly grounded membrane STRUCTURE node and descriptive edges,
    the pocket identity, and the GO-grounded protein-complex collar.
  - Run focused schema, grounding/product and graph checks after separately authorized
    scientific curation.
limitations:
- Field2009 is inspected as its publisher Key Points and complete abstract; Halliday2021
  as the complete native MED abstract. Neither full review body was recovered, and
  an HTTP200 access stub is not treated as one.
- Primary reading scopes are enumerated per evidence row. Lacomble inspection covers
  the two principal architecture/boundary Results subsections, selected Discussion
  and complete main Methods; Bonhivers covers the specified Results/Discussion/Methods
  sections. No full-body claim is made for the remaining sections. Gadelha main scientific
  text and main Methods were read completely. No figure pixels, raw data or supplementary
  movies were independently analyzed.
- The usual single-pocket arrangement changes during cell-cycle duplication. Species-level
  COMMON is not a counted prevalence estimate, and biochemical or morphogenetic evidence
  from one life stage is not silently transferred to another.
- Exact lipid mixture, complete collar molecular composition and universal individual
  component requirements were not established. These are bounded scientific limits,
  not defects inferred from optional empty slots.
- This finding does not require a complete membrane proteome, a new collar inventory
  or a measured lipid mixture; those optional unknowns remain limitations.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requires a validated review for each uncovered target, including
  an honest clean review; no issue is invented to satisfy the local issue-only output
  rule.
- Remote evidence preserves original request URL, actual UTC access timestamp and
  raw SHA256; reused batch22 sources retain their original receipts. Fresh target
  resolver results use the completed same-base batch26 native report; broader finalization
  is reserved to the parent.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
