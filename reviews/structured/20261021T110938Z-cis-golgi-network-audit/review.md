# Cis-Golgi network taxonomy, compartment scope and graph review

- Review: 20261021T110938Z-cis-golgi-network-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:51:45Z
- Finished UTC: 2026-10-21T11:09:38Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two major corrections are needed: the cited PPY1/PPY12 experimental lineage has the wrong current species, and the stack/tER study does not directly establish the distinct CGN occurrence or canonical example. One minor correction separates the whole-network graph node from its lipid-material component link. Generic GO identity and topology remain valid.

## Scope And Provenance

Entire maintained target; native GO/taxon identities; exact citation identity and primary stack/tER evidence; current PPY12 strain bridge; frozen membrane/whole-Golgi boundary fields.

Selection: Tenth selected target in batch twenty-two, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005801 | data/structures/membrane_organelle/cis_golgi_network.yaml | maintained | cis-Golgi network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005801 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005801 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0005801 | 8 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0005801 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0005801 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005801 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005801 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005801 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0005801 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Valid ontology identity and whole-versus-membrane boundary

identity: supported. Targets: GO:0005801.

The exact GO identity, synonym, Golgi-subcompartment parent, Golgi parthood and CGN-membrane part are coherent. Native GO explicitly distinguishes the CGN from the Golgi stack. The two species/example defects below do not invalidate the generic ontology identity.

### Label-only membrane material and early-Golgi factor boundary

grounding: supported. Targets: GO:0005801.

The material row is a collective lipid constituent of the CGN membrane. No exact source-neutral lipid-species identifier is warranted by the inspected evidence. Cho’s Sed5-positive fraction and Rossanese’s tER factors do not establish a source-neutral CGN structural protein inventory, so the existing boundary discussion and deferred molecular inventory remain appropriate.

### Constitution separated from molecular formation requirements

evidence: unknown. Targets: GO:0005801.

The ESSENTIAL row represents complete constituting bilayer material. The sources do not establish which individual lipid species or trafficking protein is necessary for CGN formation. Neither the presence of stacks nor the proposed tER/cisternal maturation model resolves this experimental assembly-necessity question.

### Wrong current taxon for the cited experimental lineage

scope: concern. Targets: GO:0005801.

The taxon IDs themselves resolve, but Rossanese’s PPY1/PPY12 lineage is assigned to K. pastoris4922 in the record. Current ATCC and independent ENA source qualifiers identify PPY12 as K. phaffii460519. This is a concrete strain-to-species attribution error, separate from whether that study demonstrates a CGN.

### Stack observations do not directly establish a CGN example

evidence: concern. Targets: GO:0005801.

Rossanese directly supports the notes about ordered Golgi stacks near transitional ER. Placing those observations under this record’s COMMON occurrence and canonical example asserts occurrence of the distinct CGN, which the inspected primary Results/Discussion do not identify. The tubulovesicular Sec13 region is assigned to tER in the source. A corrected taxon alone therefore leaves a material compartment-specific evidence gap.

### Supported topology with an incorrect local component link

graph: concern. Targets: GO:0005801.

The bounds/parthood/ER-adjacency relationships are appropriate nonmechanistic ontology-backed topology; Rossanese is general stack/tER context rather than direct CGN localization evidence. However, the GO0005801 whole-network node points via component_ref to its lipid-bilayer component, conflating a membrane-bounded compartment with one constituting material. This issue is separate from the legitimate collective lipid row.

### Three bounded corrections and retained scientific limits

completeness: supported. Targets: GO:0005801.

Two major findings address independently incorrect taxon attribution and unsupported CGN-specific occurrence/example support; one minor repairs a graph-to-component link. Empty functions and unresolved exact protein/lipid inventory are not defects. Prior removal of an ad hoc ER-entry function is respected; no new mechanism is required.

## Findings

### F1: The cited PPY1/PPY12 study is assigned to the wrong current species

major / open / confirmed; issue key: cis-golgi-network-ppy12-current-taxon.

Rossanese1999 used PPY1 and its isogenic PPY12 derivatives. ATCC explicitly identifies PPY12 as K. phaffii following sequence-based reidentification, independently corroborated by ENA LC815816.1 taxon460519. The maintained taxonomic_distribution and canonical_examples instead assign the experiment to K. pastoris4922. The historical Pichia pastoris name alone does not justify that current assignment.

### F2: The cited stack study does not directly establish this CGN occurrence and example

major / open / confirmed; issue key: cis-golgi-network-stack-study-evidence-scope.

The occurrence and canonical-example slots belong to GO0005801, but their sole cited study directly resolves Golgi stacks and adjacent transitional ER. Native GO distinguishes CGN from the Golgi stack, and the source assigns its observed Sec13-positive tubulovesicular interface to tER. Neither early/late Golgi marker apposition nor ordered stacks alone demonstrates a distinct CGN. Correcting the species leaves this unsupported compartment-specific attribution intact.

### F3: The whole-network graph node links to a lipid-material component

minor / open / confirmed; issue key: cis-golgi-network-node-lipid-component-link.

The graph node grounded to GO0005801 denotes the complete membrane-bounded network, but its component_ref names cis_golgi_network_lipid_bilayer. The schema uses component_ref when the node is an own component; native GO separately identifies the complete network and its surrounding membrane. The link therefore collapses the compartment into its lipid constituent even though the graph otherwise keeps membrane and network nodes separate.

## Recommended Actions And Acceptance Checks

### A1

Correct any retained PPY1/PPY12-based example and occurrence attribution to K. phaffii460519 with a documented strain bridge; retain the historical source name in notes. Address the separate CGN-specific evidence finding before retaining this as a confirmed CGN example.

- Any retained Rossanese example uses the experimentally verified current taxon and preserves the historical name.
- The species correction is not treated as proof of a CGN distinct from Golgi stacks.
- Focused native validators pass.

### A2

Supply direct evidence identifying the CGN in the asserted organism, or remove/defer the CGN-specific occurrence/example while retaining Rossanese as explicitly broader Golgi-stack/tER context. Do not replace the CGN identity with a whole-stack term or infer absence of CGN from this evidence gap.

- Retained occurrence/example evidence distinguishes CGN from whole Golgi stacks and transitional ER.
- The canonical example does not depend solely on whole-stack morphology or early-Golgi marker localization.
- The independent current-species error is resolved for any retained experimental attribution.
- Focused native validators pass.

### A3

Remove the lipid component_ref from the whole-CGN node, or add a separate lipid-material node carrying that component_ref and an appropriate constituent relationship. Keep GO0005801 on the complete network and GO0033106 on its membrane.

- No whole-CGN node is locally identified as the lipid-bilayer component.
- Any added material node preserves membrane-versus-compartment scope.
- Focused native validators pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/cis_golgi_network.yaml; Entire maintained YAML including definition/source, hierarchy, synonyms, component, functions if present, taxonomy, examples, every graph node/edge, discussions and history | context_only | The entire target was read against fresh native inspection. No scientific record, mapping status or history was changed. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent essentiality; CausalNode component_ref; docs/CURATION.md and native review checklist | context_only | Essentiality asks whether the structure forms without a component; observed membership and activity do not establish experimental formation necessity. component_ref identifies an own-component node. Optional slots are not mandatory. Reviewed-label-only collective lipid material is distinct from a whole membrane-bounded compartment. |
| cis-golgi-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005794,GO:0005801,GO:0033106,GO:0098791; Complete GO0005801, GO0033106, GO0005794, GO0098791 and GO0005783 definitions, comments, synonyms and relevant relationships | supports | GO0005801 exactly identifies the tubular/cisternal network at the convex ER-facing side of the Golgi, gives the maintained exact synonym, and explicitly comments that CGN is not part of the Golgi stack. GO0033106 identifies the surrounding lipid-bilayer membrane, distinct from the whole network. The Golgi apparatus, subcompartment and ER identities are valid. |
| cis-golgi-agent-tax-4922 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4922; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | This native ENA taxonomy response identifies Komagataella pastoris, species. It verifies only this taxon identity and rank, not experimental occurrence or strain provenance. |
| cis-golgi-agent-tax-460519 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/460519; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | This native ENA taxonomy response identifies Komagataella phaffii, species. It verifies only this taxon identity and rank, not experimental occurrence or strain provenance. |
| cis-golgi-agent-doi-10.1083_jcb.145.1.69 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.145.1.69; Complete returned bibliographic identity and abstract | supports | Exact native metadata identifies Golgi structure correlates with transitional endoplasmic reticulum organization in Pichia pastoris and Saccharomyces cerevisiae. Authors: Rossanese OW, Soderholm J, Bevis BJ, Sears IB, O'Connor J, Williamson EK, Glick BS.; PMID 10189369; DOI 10.1083/jcb.145.1.69. Bibliographic identity, publication type and available abstract were read; metadata is not a full-body substitute. |
| cis-golgi-agent-jats-PMC2148216 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2148216.1/PMC2148216.1.xml; Entire Results section and all five subsections; entire Discussion; Materials and Methods / Strains and Plasmids; complete TablesI-IV; Introduction paragraphs concerning cisternal maturation and yeast comparison. Other Methods, complete Introduction, raw images and supplements were not comprehensively audited. | supports | Rossanese1999 directly compares ordered Pichia Golgi stacks with dispersed Saccharomyces Golgi cisternae, and localizes COPII/Sec13 to adjacent tubulovesicular transitional ER. Early Och1 and late Sec7 colocalization is interpreted at the level of stacks or closely apposed structures. Methods specifies PPY1 and its isogenic PPY12 his4 arg4 derivative. This supports stack/tER organization, not direct identification of a distinct CGN. Cisternal-formation mechanisms are proposed models rather than demonstrated assembly requirements. |
| cis-golgi-agent-atcc-204163 | https://www.atcc.org/products/204163; Product organism, strain designation PPY12, genotype his4 arg4, Comments reidentification, and History deposited-as/depositor fields | supports | ATCC204163 identifies strain PPY12 as Komagataella phaffii and records that it was formerly named K. pastoris, with the change based on in-house sequence analysis. The deposited-as Pichia pastoris name is historical. This directly checks the experimental strain rather than assuming a species from the old binomial alone. |
| cis-golgi-agent-ena-LC815816 | https://www.ebi.ac.uk/ena/browser/api/embl/LC815816.1?download=false; DE/OS/OC identity and source qualifiers organism, strain and db_xref taxon460519; bibliographic provenance | supports | The native ENA record LC815816.1 independently pairs strain PPY12 with K. phaffii and taxon460519. Only this source-organism/strain bridge is used; ATG14 is not inferred to be a cis-Golgi constituent. |
| cis-golgi-agent-cho2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/S0014-5793%2800%2901268-0%22; Exact DOI/title/authors/PMID10713261 and complete abstract; no full article body | supports | The exact Cho/Noda/Yoda2000 native abstract describes immunoisolation of a Sed5-positive early Golgi fraction in S. cerevisiae, with selected Golgi markers and separation from ER/late-Golgi markers. It does not specifically identify an equivalent distinct CGN. This abstract supports the existing caution about treating early trafficking factors as CGN structural constituents. |
| cis-golgi-agent-cho2000-html | https://febs.onlinelibrary.wiley.com/doi/full/10.1016/S0014-5793%2800%2901268-0; Actual response body and retrieval receipt | context_only | The full-text publisher route returnedHTTP403; no article body is claimed from this response. The exact native abstract is available separately. |
| cis-golgi-agent-cho2000-pdf | https://febs.onlinelibrary.wiley.com/doi/pdfdirect/10.1016/S0014-5793%2800%2901268-0; Actual response body and retrieval receipt | context_only | The publisher PDF route returnedHTTP403; it is not a recovered primary PDF. |
| boundary-0 | data/structures/membrane_organelle/cis_golgi_network_membrane.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | Only these boundary fields were read for context. This is not an additional full scientific review of the neighboring record. |
| boundary-1 | data/structures/membrane_organelle/golgi_apparatus.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | Only these boundary fields were read for context. This is not an additional full scientific review of the neighboring record. |
| schema-result | just validate data/structures/membrane_organelle/cis_golgi_network.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/cis_golgi_network.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/cis_golgi_network.yaml --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/cis_golgi_network-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/cis_golgi_network.yaml --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/cis_golgi_network-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch22-20261021-xfifxerh/cis_golgi_network-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/cis_golgi_network.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 8 of8 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Cho2000 was available as exact native metadata and abstract only; both attempted publisher body/PDF routes returned403. The initial unquoted DOI query returned zero hits because of query syntax; the quoted exact query resolved PMID10713261. No article absence is inferred.
- Rossanese1999 was read at complete Results/Discussion and the exact Methods/table scopes stated in evidence. No raw image reanalysis or complete audit of other Methods, all Introduction or supplements is claimed. The CGN evidence finding is bounded to this cited study and these maintained assertions, not a claim that CGN does not exist in the species.
- ATCC reidentification and ENA source qualifiers establish the PPY12 strain bridge. The ENA ATG14 sequence is not evidence of CGN membership, function or assembly necessity.
- Collective lipid material is supported; individual lipid/protein formation requirements remain unresolved. The two neighboring records were used only for frozen boundary fields and are not independently reviewed in full.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110938Z-cis-golgi-network-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cis-Golgi network taxonomy, compartment scope and graph review
started_at: '2026-10-21T10:51:45Z'
finished_at: '2026-10-21T11:09:38Z'
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
summary: 'Two major corrections are needed: the cited PPY1/PPY12 experimental lineage
  has the wrong current species, and the stack/tER study does not directly establish
  the distinct CGN occurrence or canonical example. One minor correction separates
  the whole-network graph node from its lipid-material component link. Generic GO
  identity and topology remain valid.'
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
  - path: data/structures/membrane_organelle/cis_golgi_network.yaml
    sha256: 369cae5270aeacd25a94317be3b005167773bd89a5e4c2583061fa24cd79f31d
    role: target
  - path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    sha256: c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c
    role: context
  - path: data/structures/membrane_organelle/golgi_apparatus.yaml
    sha256: b064dc1116ec2814e2ecb946d8ebd554a4b176494c2259ff7e458bac0d3e5eb1
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
- target_id: GO:0005801
  path: data/structures/membrane_organelle/cis_golgi_network.yaml
  label: cis-Golgi network
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
scope:
  description: Entire maintained target; native GO/taxon identities; exact citation
    identity and primary stack/tER evidence; current PPY12 strain bridge; frozen membrane/whole-Golgi
    boundary fields.
  selection: Tenth selected target in batch twenty-two, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005801
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005801
  command: just validate data/structures/membrane_organelle/cis_golgi_network.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005801
  command: just validate-strict data/structures/membrane_organelle/cis_golgi_network.yaml
    --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/cis_golgi_network-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0005801
  summary: 8 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005801
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - cis-golgi-agent-go
  - cis-golgi-agent-tax-4922
  - cis-golgi-agent-tax-460519
  - cis-golgi-agent-doi-10.1083_jcb.145.1.69
  - cis-golgi-agent-jats-PMC2148216
  - cis-golgi-agent-atcc-204163
  - cis-golgi-agent-ena-LC815816
  - cis-golgi-agent-cho2000-meta
  - cis-golgi-agent-cho2000-html
  - cis-golgi-agent-cho2000-pdf
  - boundary-0
  - boundary-1
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005801
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
  - GO:0005801
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
  - GO:0005801
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
  - GO:0005801
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
  - GO:0005801
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
  reference: data/structures/membrane_organelle/cis_golgi_network.yaml
  locator: Entire maintained YAML including definition/source, hierarchy, synonyms,
    component, functions if present, taxonomy, examples, every graph node/edge, discussions
    and history
  accessed_at: '2026-10-21T10:58:08Z'
  support: context_only
  summary: The entire target was read against fresh native inspection. No scientific
    record, mapping status or history was changed.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent essentiality; CausalNode component_ref; docs/CURATION.md
    and native review checklist
  accessed_at: '2026-10-21T10:58:08Z'
  support: context_only
  summary: Essentiality asks whether the structure forms without a component; observed
    membership and activity do not establish experimental formation necessity. component_ref
    identifies an own-component node. Optional slots are not mandatory. Reviewed-label-only
    collective lipid material is distinct from a whole membrane-bounded compartment.
- evidence_id: cis-golgi-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005794,GO:0005801,GO:0033106,GO:0098791
  locator: Complete GO0005801, GO0033106, GO0005794, GO0098791 and GO0005783 definitions,
    comments, synonyms and relevant relationships
  accessed_at: '2026-10-21T10:51:31.284848Z'
  support: supports
  summary: GO0005801 exactly identifies the tubular/cisternal network at the convex
    ER-facing side of the Golgi, gives the maintained exact synonym, and explicitly
    comments that CGN is not part of the Golgi stack. GO0033106 identifies the surrounding
    lipid-bilayer membrane, distinct from the whole network. The Golgi apparatus,
    subcompartment and ER identities are valid.
  snapshot_sha256: 1f64f46ea3228d75112cc4a7cd62683682181d7f56a4b695efb1f8f03db842e8
- evidence_id: cis-golgi-agent-tax-4922
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4922
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:51:31.391999Z'
  support: supports
  summary: This native ENA taxonomy response identifies Komagataella pastoris, species.
    It verifies only this taxon identity and rank, not experimental occurrence or
    strain provenance.
  snapshot_sha256: 5896e5992030d82c3a2bfe36e0c5cd013b4fd03c025f4db8bef695f70456a1d1
- evidence_id: cis-golgi-agent-tax-460519
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/460519
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:52:45.143036Z'
  support: supports
  summary: This native ENA taxonomy response identifies Komagataella phaffii, species.
    It verifies only this taxon identity and rank, not experimental occurrence or
    strain provenance.
  snapshot_sha256: c8f1333ff9a50b6e22e65fa32b6a5a349d82c72b92401daadf978166d2e89376
- evidence_id: cis-golgi-agent-doi-10.1083_jcb.145.1.69
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.145.1.69
  locator: Complete returned bibliographic identity and abstract
  accessed_at: '2026-10-21T10:51:31.915928Z'
  support: supports
  summary: 'Exact native metadata identifies Golgi structure correlates with transitional
    endoplasmic reticulum organization in Pichia pastoris and Saccharomyces cerevisiae.
    Authors: Rossanese OW, Soderholm J, Bevis BJ, Sears IB, O''Connor J, Williamson
    EK, Glick BS.; PMID 10189369; DOI 10.1083/jcb.145.1.69. Bibliographic identity,
    publication type and available abstract were read; metadata is not a full-body
    substitute.'
  snapshot_sha256: f80575f934ea8397ea102f48bdec522ae4b284adc5ac8a1ca9c612ffca19b4b4
- evidence_id: cis-golgi-agent-jats-PMC2148216
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2148216.1/PMC2148216.1.xml
  locator: Entire Results section and all five subsections; entire Discussion; Materials
    and Methods / Strains and Plasmids; complete TablesI-IV; Introduction paragraphs
    concerning cisternal maturation and yeast comparison. Other Methods, complete
    Introduction, raw images and supplements were not comprehensively audited.
  accessed_at: '2026-10-21T10:52:00.890099Z'
  support: supports
  summary: Rossanese1999 directly compares ordered Pichia Golgi stacks with dispersed
    Saccharomyces Golgi cisternae, and localizes COPII/Sec13 to adjacent tubulovesicular
    transitional ER. Early Och1 and late Sec7 colocalization is interpreted at the
    level of stacks or closely apposed structures. Methods specifies PPY1 and its
    isogenic PPY12 his4 arg4 derivative. This supports stack/tER organization, not
    direct identification of a distinct CGN. Cisternal-formation mechanisms are proposed
    models rather than demonstrated assembly requirements.
  snapshot_sha256: e9eb8235003747a36696a90d27a3fd45f601b1e46dfb3bba5419d779b5fe9590
- evidence_id: cis-golgi-agent-atcc-204163
  kind: authority
  reference: https://www.atcc.org/products/204163
  locator: Product organism, strain designation PPY12, genotype his4 arg4, Comments
    reidentification, and History deposited-as/depositor fields
  accessed_at: '2026-10-21T10:52:45.142535Z'
  support: supports
  summary: ATCC204163 identifies strain PPY12 as Komagataella phaffii and records
    that it was formerly named K. pastoris, with the change based on in-house sequence
    analysis. The deposited-as Pichia pastoris name is historical. This directly checks
    the experimental strain rather than assuming a species from the old binomial alone.
  snapshot_sha256: 3c8663a19400c95a9669aeb0014e15527ed2c530e333df80501e6eb8d01d5319
- evidence_id: cis-golgi-agent-ena-LC815816
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/LC815816.1?download=false
  locator: DE/OS/OC identity and source qualifiers organism, strain and db_xref taxon460519;
    bibliographic provenance
  accessed_at: '2026-10-21T10:52:45.142930Z'
  support: supports
  summary: The native ENA record LC815816.1 independently pairs strain PPY12 with
    K. phaffii and taxon460519. Only this source-organism/strain bridge is used; ATG14
    is not inferred to be a cis-Golgi constituent.
  snapshot_sha256: f02d748dce33d5c56b830ab9e96ccb14facd65a8a7621bdaa10c7711eb8d63b4
- evidence_id: cis-golgi-agent-cho2000-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/S0014-5793%2800%2901268-0%22
  locator: Exact DOI/title/authors/PMID10713261 and complete abstract; no full article
    body
  accessed_at: '2026-10-21T10:52:01.200160Z'
  support: supports
  summary: The exact Cho/Noda/Yoda2000 native abstract describes immunoisolation of
    a Sed5-positive early Golgi fraction in S. cerevisiae, with selected Golgi markers
    and separation from ER/late-Golgi markers. It does not specifically identify an
    equivalent distinct CGN. This abstract supports the existing caution about treating
    early trafficking factors as CGN structural constituents.
  snapshot_sha256: b0960521e38911bcc0523d02dcbc5d953440044fcace3d795af4bf575d3fd67f
- evidence_id: cis-golgi-agent-cho2000-html
  kind: authority
  reference: https://febs.onlinelibrary.wiley.com/doi/full/10.1016/S0014-5793%2800%2901268-0
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:52:45.143274Z'
  support: context_only
  summary: The full-text publisher route returnedHTTP403; no article body is claimed
    from this response. The exact native abstract is available separately.
  snapshot_sha256: d8a6e12757bd32866af00ef2200ea277d965f98b9279e90aa9bdf87bc571f9d0
- evidence_id: cis-golgi-agent-cho2000-pdf
  kind: authority
  reference: https://febs.onlinelibrary.wiley.com/doi/pdfdirect/10.1016/S0014-5793%2800%2901268-0
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:52:45.143129Z'
  support: context_only
  summary: The publisher PDF route returnedHTTP403; it is not a recovered primary
    PDF.
  snapshot_sha256: 1d8ca7528f70488c47614c7d8eedfd13fb5c64cbc37827517c91e018503dacaf
- evidence_id: boundary-0
  kind: record_content
  reference: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:58:08Z'
  support: context_only
  summary: Only these boundary fields were read for context. This is not an additional
    full scientific review of the neighboring record.
- evidence_id: boundary-1
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_apparatus.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:58:08Z'
  support: context_only
  summary: Only these boundary fields were read for context. This is not an additional
    full scientific review of the neighboring record.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/cis_golgi_network.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:51:47Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/cis_golgi_network.yaml'
  snapshot_sha256: fa897d8bc98035fa2094e445e6fc78f97d5481318d279ae4030b8303a9ebc72d
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/cis_golgi_network.yaml
    --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/cis_golgi_network-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:51:48Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/cis_golgi_network.yaml\
    \ --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/cis_golgi_network-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch22-20261021-xfifxerh/cis_golgi_network-strict.tsv"
  snapshot_sha256: 5158fad8acbd2474bcc42fc68f6a9384d2a09eff0605b475ae1b6d091781220a
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/cis_golgi_network.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:58:08Z'
  support: supports
  summary: '8 of8 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
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
  topic: Valid ontology identity and whole-versus-membrane boundary
  outcome: supported
  target_ids:
  - GO:0005801
  summary: The exact GO identity, synonym, Golgi-subcompartment parent, Golgi parthood
    and CGN-membrane part are coherent. Native GO explicitly distinguishes the CGN
    from the Golgi stack. The two species/example defects below do not invalidate
    the generic ontology identity.
  evidence_ids:
  - cis-golgi-agent-go
  - boundary-0
  - boundary-1
  - record
- assessment_id: composition
  area: grounding
  topic: Label-only membrane material and early-Golgi factor boundary
  outcome: supported
  target_ids:
  - GO:0005801
  summary: The material row is a collective lipid constituent of the CGN membrane.
    No exact source-neutral lipid-species identifier is warranted by the inspected
    evidence. Cho’s Sed5-positive fraction and Rossanese’s tER factors do not establish
    a source-neutral CGN structural protein inventory, so the existing boundary discussion
    and deferred molecular inventory remain appropriate.
  evidence_ids:
  - cis-golgi-agent-go
  - cis-golgi-agent-cho2000-meta
  - cis-golgi-agent-jats-PMC2148216
  - record
  - policy
- assessment_id: necessity
  area: evidence
  topic: Constitution separated from molecular formation requirements
  outcome: unknown
  target_ids:
  - GO:0005801
  summary: The ESSENTIAL row represents complete constituting bilayer material. The
    sources do not establish which individual lipid species or trafficking protein
    is necessary for CGN formation. Neither the presence of stacks nor the proposed
    tER/cisternal maturation model resolves this experimental assembly-necessity question.
  evidence_ids:
  - cis-golgi-agent-go
  - cis-golgi-agent-jats-PMC2148216
  - cis-golgi-agent-cho2000-meta
  - record
  - policy
- assessment_id: taxon
  area: scope
  topic: Wrong current taxon for the cited experimental lineage
  outcome: concern
  target_ids:
  - GO:0005801
  summary: The taxon IDs themselves resolve, but Rossanese’s PPY1/PPY12 lineage is
    assigned to K. pastoris4922 in the record. Current ATCC and independent ENA source
    qualifiers identify PPY12 as K. phaffii460519. This is a concrete strain-to-species
    attribution error, separate from whether that study demonstrates a CGN.
  evidence_ids:
  - cis-golgi-agent-jats-PMC2148216
  - cis-golgi-agent-atcc-204163
  - cis-golgi-agent-ena-LC815816
  - cis-golgi-agent-tax-4922
  - cis-golgi-agent-tax-460519
  - record
- assessment_id: example
  area: evidence
  topic: Stack observations do not directly establish a CGN example
  outcome: concern
  target_ids:
  - GO:0005801
  summary: Rossanese directly supports the notes about ordered Golgi stacks near transitional
    ER. Placing those observations under this record’s COMMON occurrence and canonical
    example asserts occurrence of the distinct CGN, which the inspected primary Results/Discussion
    do not identify. The tubulovesicular Sec13 region is assigned to tER in the source.
    A corrected taxon alone therefore leaves a material compartment-specific evidence
    gap.
  evidence_ids:
  - cis-golgi-agent-jats-PMC2148216
  - cis-golgi-agent-go
  - cis-golgi-agent-cho2000-meta
  - record
- assessment_id: graph
  area: graph
  topic: Supported topology with an incorrect local component link
  outcome: concern
  target_ids:
  - GO:0005801
  summary: The bounds/parthood/ER-adjacency relationships are appropriate nonmechanistic
    ontology-backed topology; Rossanese is general stack/tER context rather than direct
    CGN localization evidence. However, the GO0005801 whole-network node points via
    component_ref to its lipid-bilayer component, conflating a membrane-bounded compartment
    with one constituting material. This issue is separate from the legitimate collective
    lipid row.
  evidence_ids:
  - cis-golgi-agent-go
  - cis-golgi-agent-jats-PMC2148216
  - record
  - policy
  - boundary-0
  - boundary-1
- assessment_id: coverage
  area: completeness
  topic: Three bounded corrections and retained scientific limits
  outcome: supported
  target_ids:
  - GO:0005801
  summary: Two major findings address independently incorrect taxon attribution and
    unsupported CGN-specific occurrence/example support; one minor repairs a graph-to-component
    link. Empty functions and unresolved exact protein/lipid inventory are not defects.
    Prior removal of an ad hoc ER-entry function is respected; no new mechanism is
    required.
  evidence_ids:
  - cis-golgi-agent-go
  - cis-golgi-agent-jats-PMC2148216
  - cis-golgi-agent-atcc-204163
  - cis-golgi-agent-ena-LC815816
  - cis-golgi-agent-cho2000-meta
  - record
  - policy
findings:
- finding_id: F1
  issue_key: cis-golgi-network-ppy12-current-taxon
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: The cited PPY1/PPY12 study is assigned to the wrong current species
  description: Rossanese1999 used PPY1 and its isogenic PPY12 derivatives. ATCC explicitly
    identifies PPY12 as K. phaffii following sequence-based reidentification, independently
    corroborated by ENA LC815816.1 taxon460519. The maintained taxonomic_distribution
    and canonical_examples instead assign the experiment to K. pastoris4922. The historical
    Pichia pastoris name alone does not justify that current assignment.
  target_ids:
  - GO:0005801
  field_paths:
  - taxonomic_distribution[0].taxon_id
  - taxonomic_distribution[0].taxon_label
  - canonical_examples[0].taxon_id
  - canonical_examples[0].taxon_label
  evidence_ids:
  - cis-golgi-agent-jats-PMC2148216
  - cis-golgi-agent-atcc-204163
  - cis-golgi-agent-ena-LC815816
  - cis-golgi-agent-tax-4922
  - cis-golgi-agent-tax-460519
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Major because experimental species scope and the canonical
    example are materially misattributed, while the generic structure identity remains
    valid.
- finding_id: F2
  issue_key: cis-golgi-network-stack-study-evidence-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The cited stack study does not directly establish this CGN occurrence and
    example
  description: The occurrence and canonical-example slots belong to GO0005801, but
    their sole cited study directly resolves Golgi stacks and adjacent transitional
    ER. Native GO distinguishes CGN from the Golgi stack, and the source assigns its
    observed Sec13-positive tubulovesicular interface to tER. Neither early/late Golgi
    marker apposition nor ordered stacks alone demonstrates a distinct CGN. Correcting
    the species leaves this unsupported compartment-specific attribution intact.
  target_ids:
  - GO:0005801
  field_paths:
  - taxonomic_distribution[0]
  - canonical_examples[0]
  evidence_ids:
  - cis-golgi-agent-go
  - cis-golgi-agent-jats-PMC2148216
  - cis-golgi-agent-cho2000-meta
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Major because the only asserted species occurrence and canonical
    example overextend the cited observations to a different compartment scope; the
    ontology identity and generic topology remain supported.
- finding_id: F3
  issue_key: cis-golgi-network-node-lipid-component-link
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: The whole-network graph node links to a lipid-material component
  description: The graph node grounded to GO0005801 denotes the complete membrane-bounded
    network, but its component_ref names cis_golgi_network_lipid_bilayer. The schema
    uses component_ref when the node is an own component; native GO separately identifies
    the complete network and its surrounding membrane. The link therefore collapses
    the compartment into its lipid constituent even though the graph otherwise keeps
    membrane and network nodes separate.
  target_ids:
  - GO:0005801
  field_paths:
  - causal_graphs#cis_golgi_network_entry_topology.nodes#cis_golgi_network.component_ref
  evidence_ids:
  - cis-golgi-agent-go
  - record
  - policy
  - boundary-0
  - boundary-1
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: Minor because the graph identities and topology are otherwise
    valid; one local cross-link misrepresents material-versus-whole scope.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005801
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  description: Correct any retained PPY1/PPY12-based example and occurrence attribution
    to K. phaffii460519 with a documented strain bridge; retain the historical source
    name in notes. Address the separate CGN-specific evidence finding before retaining
    this as a confirmed CGN example.
  acceptance_checks:
  - Any retained Rossanese example uses the experimentally verified current taxon
    and preserves the historical name.
  - The species correction is not treated as proof of a CGN distinct from Golgi stacks.
  - Focused native validators pass.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0005801
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  description: Supply direct evidence identifying the CGN in the asserted organism,
    or remove/defer the CGN-specific occurrence/example while retaining Rossanese
    as explicitly broader Golgi-stack/tER context. Do not replace the CGN identity
    with a whole-stack term or infer absence of CGN from this evidence gap.
  acceptance_checks:
  - Retained occurrence/example evidence distinguishes CGN from whole Golgi stacks
    and transitional ER.
  - The canonical example does not depend solely on whole-stack morphology or early-Golgi
    marker localization.
  - The independent current-species error is resolved for any retained experimental
    attribution.
  - Focused native validators pass.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0005801
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  description: Remove the lipid component_ref from the whole-CGN node, or add a separate
    lipid-material node carrying that component_ref and an appropriate constituent
    relationship. Keep GO0005801 on the complete network and GO0033106 on its membrane.
  acceptance_checks:
  - No whole-CGN node is locally identified as the lipid-bilayer component.
  - Any added material node preserves membrane-versus-compartment scope.
  - Focused native validators pass.
limitations:
- Cho2000 was available as exact native metadata and abstract only; both attempted
  publisher body/PDF routes returned403. The initial unquoted DOI query returned zero
  hits because of query syntax; the quoted exact query resolved PMID10713261. No article
  absence is inferred.
- Rossanese1999 was read at complete Results/Discussion and the exact Methods/table
  scopes stated in evidence. No raw image reanalysis or complete audit of other Methods,
  all Introduction or supplements is claimed. The CGN evidence finding is bounded
  to this cited study and these maintained assertions, not a claim that CGN does not
  exist in the species.
- ATCC reidentification and ENA source qualifiers establish the PPY12 strain bridge.
  The ENA ATG14 sequence is not evidence of CGN membership, function or assembly necessity.
- Collective lipid material is supported; individual lipid/protein formation requirements
  remain unresolved. The two neighboring records were used only for frozen boundary
  fields and are not independently reviewed in full.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
