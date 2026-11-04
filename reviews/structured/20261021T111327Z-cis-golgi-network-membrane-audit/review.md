# Cis-Golgi network membrane identity and experimental-scope review

- Review: 20261021T111327Z-cis-golgi-network-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:57:10Z
- Finished UTC: 2026-10-21T11:13:27Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two major corrections are needed: the cited PPY1/PPY12 lineage is assigned to the wrong current species, and the Golgi-stack/tER observations do not directly establish a distinct CGN-membrane occurrence or canonical example. Exact membrane identity, collective lipid material and nonmechanistic topology remain supported.

## Scope And Provenance

Entire maintained CGN-membrane target; native GO/taxon identities; exact citations, primary stack/tER study and strain reidentification; frozen whole-CGN/Golgi-membrane boundary fields.

Selection: First selected target in batch twenty-three, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033106 | data/structures/membrane_organelle/cis_golgi_network_membrane.yaml | maintained | cis-Golgi network membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0033106 | Focused validator passed. |
| Focused native strict | passed | True | GO:0033106 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0033106 | 8 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0033106 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0033106 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0033106 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0033106 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0033106 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0033106 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact membrane identity and container boundary

identity: supported. Targets: GO:0033106.

The exact GO membrane definition and synonym are valid. The broader Golgi-membrane parent fits the definitions, and parthood in the whole CGN is directly supported. The membrane is not confused with the network, Golgi stack or transitional ER in the generic definition.

### Collective lipid-bilayer constituent

grounding: supported. Targets: GO:0033106.

The reviewed-label-only row names the complete constituting lipid material without asserting a species-specific composition. No molecular lipid or protein family is established as an exact grounding for that collective material. Sed5-positive fractionation and COPII localization do not justify treating all early trafficking machinery as membrane structural constituents.

### Constitution and formation necessity

evidence: unknown. Targets: GO:0033106.

The ESSENTIAL row represents collective lipid-bilayer constitution. The sources do not determine individual lipid-species or protein requirements for formation of this membrane. Neither source-specific fraction membership nor the proposed cisternal-formation model establishes such experimental assembly necessity.

### Experimental lineage misassigned to a current species

scope: concern. Targets: GO:0033106.

Both taxon IDs are valid species entries, but the PPY1/PPY12 lineage used by the cited study is currently identified as K. phaffii460519, not the maintained K. pastoris4922. Current ATCC reidentification and independent ENA strain qualifiers establish this mismatch separately from the compartment-specific evidence question.

### Stack morphology does not establish a specific CGN membrane

evidence: concern. Targets: GO:0033106.

The occurrence and canonical-example notes accurately describe ordered Golgi stacks near tER, but these slots assert an example of this particular CGN membrane. The primary study does not identify a distinct CGN; its tubulovesicular Sec13 interface is assigned to tER. Therefore the CGN-membrane occurrence inference remains unsupported even after the taxon is corrected.

### Supported nonmechanistic membrane topology

graph: supported. Targets: GO:0033106.

The graph keeps the membrane separate from the complete CGN, Golgi apparatus and ER. Its membrane node is explicitly defined by GO0033106 as the lipid bilayer and can represent the collective material row through component_ref; it does not identify the whole membrane-bounded network with a lipid constituent. Bounds, parthood and ER-adjacency are supported as generic ontology topology. Rossanese provides broader stack/tER context, not direct CGN-membrane localization.

### Two independent source-scope corrections

completeness: supported. Targets: GO:0033106.

Two major findings concern wrong experimental-species attribution and unsupported CGN-membrane occurrence/example support. No separate material-link defect or missing required molecular inventory was established. No function field or stronger trafficking mechanism needs to be added; native status remains unchanged.

## Findings

### F1: The cited PPY1/PPY12 lineage has the wrong current species

major / open / confirmed; issue key: cis-golgi-network-membrane-ppy12-current-taxon.

Rossanese1999 used PPY1 and its isogenic PPY12 derivatives. ATCC identifies PPY12 as K. phaffii after sequence-based reidentification; ENA LC815816.1 independently pairs PPY12 with taxon460519. The maintained occurrence and canonical-example fields instead assign that experiment to K. pastoris4922. Historical Pichia pastoris nomenclature alone does not justify that current species assignment.

### F2: The stack study does not directly establish a CGN-membrane example

major / open / confirmed; issue key: cis-golgi-network-membrane-stack-study-evidence-scope.

The sole source attached to this membrane occurrence and canonical example resolves ordered Golgi stacks near transitional ER. Native GO distinguishes CGN from the Golgi stack; the study assigns its observed Sec13-positive tubulovesicular interface to tER. Stack membranes or early-Golgi marker apposition therefore do not directly identify the particular CGN membrane asserted by these fields. The scope gap persists after correcting the species.

## Recommended Actions And Acceptance Checks

### A1

Correct any retained PPY1/PPY12 experimental attribution to K. phaffii460519 using the explicit strain bridge and retain the historical name in notes. Independently resolve the CGN-membrane evidence gap before retaining the study as a confirmed example.

- Any retained experimental attribution uses the verified current taxon and documented strain provenance.
- Retaxonomizing the strain is not treated as proof of CGN-membrane occurrence.
- Focused native validators pass.

### A2

Supply direct evidence for the CGN membrane in the asserted organism, or remove/defer the occurrence/example and retain Rossanese as explicitly broader Golgi-stack/tER context. Do not infer absence of CGN from the evidence gap or replace the exact membrane identity with a whole-stack concept.

- Retained occurrence and canonical-example evidence distinguishes CGN membrane from generic stack membranes and tER.
- The example does not rest solely on ordered stacks or early-Golgi marker localization.
- The independent current-taxon mismatch is resolved for retained experimental attributions.
- Focused native validators pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/cis_golgi_network_membrane.yaml; Entire maintained YAML including definition/source, hierarchy, synonyms, component, functions if present, taxonomy, examples, every graph node/edge, discussions and history | context_only | The entire target was read against fresh native inspection. No scientific record, mapping status or history was changed. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent essentiality; CausalNode component_ref; docs/CURATION.md and native review checklist | context_only | Essentiality asks whether the structure forms without a component; observed membership and activity do not establish experimental formation necessity. component_ref identifies an own-component node. Optional slots are not mandatory. Reviewed-label-only collective lipid material is distinct from a whole membrane-bounded compartment. |
| cis-membrane-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005794,GO:0005801,GO:0033106,GO:0098791; Complete GO0033106, GO0005801, GO0005794, GO0098791 and GO0005783 definitions, comments, synonyms and relevant relationships; original batch22 native snapshot retained | supports | GO0033106 exactly denotes the lipid bilayer surrounding CGN compartments and supplies the maintained exact synonym. GO0005801 supplies direct membrane parthood and defines the containing tubular/cisternal network on the ER-facing Golgi side; its comment excludes CGN from the Golgi stack. Golgi apparatus and ER identities are distinct and valid. |
| cis-membrane-agent-go-parent | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139; Complete GO0000139 identity, definition, synonyms and returned relationships | supports | Native GO0000139 defines the Golgi membrane as the lipid bilayer around any Golgi compartment. The specific CGN-membrane definition fits this broader membrane class; this is a definition-based hierarchy check, not a claim that a direct is_a edge was returned. |
| cis-membrane-agent-tax-4922 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4922; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | This native ENA taxonomy response identifies Komagataella pastoris, species. It verifies only this taxon identity and rank, not experimental occurrence or strain provenance. |
| cis-membrane-agent-tax-460519 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/460519; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | This native ENA taxonomy response identifies Komagataella phaffii, species. It verifies only this taxon identity and rank, not experimental occurrence or strain provenance. |
| cis-membrane-agent-doi-10.1083_jcb.145.1.69 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.145.1.69; Complete returned bibliographic identity and abstract | supports | Exact native metadata identifies Golgi structure correlates with transitional endoplasmic reticulum organization in Pichia pastoris and Saccharomyces cerevisiae. Authors: Rossanese OW, Soderholm J, Bevis BJ, Sears IB, O'Connor J, Williamson EK, Glick BS.; PMID 10189369; DOI 10.1083/jcb.145.1.69. Bibliographic identity, publication type and available abstract were read; metadata is not a full-body substitute. |
| cis-membrane-agent-jats-PMC2148216 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2148216.1/PMC2148216.1.xml; Entire Results and all five subsections; entire Discussion; Methods / Strains and Plasmids; complete TablesI-IV; Introduction paragraphs concerning cisternal maturation and yeast comparison. Other Methods, complete Introduction, raw images and supplements were not comprehensively audited. Original batch22 reading and immutable receipt reused. | supports | Rossanese1999 directly compares ordered Pichia Golgi stacks with dispersed Saccharomyces cisternae. The Sec13-positive tubulovesicular region is assigned to transitional ER adjacent to stacks, and early/late marker overlap can reflect closely apposed structures. Methods identifies PPY1 and its isogenic PPY12 his4 arg4 derivative. These observations establish stack/tER organization, not specific identification of a distinct CGN or its membrane. Cisternal-formation mechanisms are proposed models. |
| cis-membrane-agent-atcc-204163 | https://www.atcc.org/products/204163; Product organism, PPY12 strain designation, his4 arg4 genotype, Comments reidentification and History deposited-as/depositor fields | supports | ATCC204163 identifies PPY12 as K. phaffii and states that its former K. pastoris identification was changed after in-house sequence analysis. The historical deposited name Pichia pastoris is not treated as an exact current-species bridge. |
| cis-membrane-agent-ena-LC815816 | https://www.ebi.ac.uk/ena/browser/api/embl/LC815816.1?download=false; DE/OS/OC identity and source qualifiers organism, strain and db_xref taxon460519; bibliographic provenance | supports | Native ENA LC815816.1 independently identifies organism K. phaffii, strain PPY12 and taxon460519. Only this strain/taxon linkage is used; the deposited ATG14 gene is not interpreted as a CGN-membrane component. |
| cis-membrane-agent-cho2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/S0014-5793%2800%2901268-0%22; Exact DOI/title/authors/PMID10713261 and complete abstract; no full article body | supports | The exact Cho/Noda/Yoda2000 metadata and abstract identify a Sed5-immunoisolated early Golgi fraction in S. cerevisiae, with selected Golgi markers and separation from ER/late-Golgi markers. This does not specifically establish a distinct CGN-membrane inventory. The existing constituent-versus-trafficking caution remains appropriate. |
| cis-membrane-agent-cho2000-html | https://febs.onlinelibrary.wiley.com/doi/full/10.1016/S0014-5793%2800%2901268-0; Actual response body and retrieval receipt | context_only | The publisher full-text route returnedHTTP403. Exact native metadata and abstract were independently available. |
| cis-membrane-agent-cho2000-pdf | https://febs.onlinelibrary.wiley.com/doi/pdfdirect/10.1016/S0014-5793%2800%2901268-0; Actual response body and retrieval receipt | context_only | The publisher PDF route returnedHTTP403; this response is not an article PDF. |
| boundary-0 | data/structures/membrane_organelle/cis_golgi_network.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | Only these boundary fields were read for context. This is not an additional full scientific review of the neighboring record. |
| boundary-1 | data/structures/membrane_organelle/golgi_membrane.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | Only these boundary fields were read for context. This is not an additional full scientific review of the neighboring record. |
| schema-result | just validate data/structures/membrane_organelle/cis_golgi_network_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/cis_golgi_network_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/cis_golgi_network_membrane.yaml --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/cis_golgi_network_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/cis_golgi_network_membrane.yaml --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/cis_golgi_network_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/cis_golgi_network_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/cis_golgi_network_membrane.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 8 of8 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Public source raw files and metadata were copied unchanged from batch22, preserving original access times and hashes; only the GO0000139 parent entry was newly retrieved. Reuse does not broaden the recorded article-reading scope.
- Cho2000 was available as exact native metadata and abstract only. Both publisher body/PDF routes returned403. The initial unquoted DOI query returned zero hits; the quoted exact query resolved PMID10713261, so no source absence is inferred.
- Rossanese was read at the stated Results/Discussion, strain Methods and table scopes, without raw image reanalysis or a comprehensive remaining-Methods/supplement audit. The finding is bounded to these maintained claims and cited observations, not a claim that CGN is absent from the species.
- The ENA ATG14 deposit is used only for the PPY12 taxon bridge. Individual lipid/protein requirements for membrane formation remain unresolved; frozen neighbors were read only at the specified boundary fields.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T111327Z-cis-golgi-network-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cis-Golgi network membrane identity and experimental-scope review
started_at: '2026-10-21T10:57:10Z'
finished_at: '2026-10-21T11:13:27Z'
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
summary: 'Two major corrections are needed: the cited PPY1/PPY12 lineage is assigned
  to the wrong current species, and the Golgi-stack/tER observations do not directly
  establish a distinct CGN-membrane occurrence or canonical example. Exact membrane
  identity, collective lipid material and nonmechanistic topology remain supported.'
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
    role: context
  - path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    sha256: c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c
    role: target
  - path: data/structures/membrane_organelle/golgi_membrane.yaml
    sha256: 6e8d11079b394cdd39cf325a3b7572042995c160308d99298765b26ce593249f
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
- target_id: GO:0033106
  path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  label: cis-Golgi network membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire maintained CGN-membrane target; native GO/taxon identities;
    exact citations, primary stack/tER study and strain reidentification; frozen whole-CGN/Golgi-membrane
    boundary fields.
  selection: First selected target in batch twenty-three, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033106
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0033106
  command: just validate data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0033106
  command: just validate-strict data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/cis_golgi_network_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0033106
  summary: 8 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0033106
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - cis-membrane-agent-go
  - cis-membrane-agent-go-parent
  - cis-membrane-agent-tax-4922
  - cis-membrane-agent-tax-460519
  - cis-membrane-agent-doi-10.1083_jcb.145.1.69
  - cis-membrane-agent-jats-PMC2148216
  - cis-membrane-agent-atcc-204163
  - cis-membrane-agent-ena-LC815816
  - cis-membrane-agent-cho2000-meta
  - cis-membrane-agent-cho2000-html
  - cis-membrane-agent-cho2000-pdf
  - boundary-0
  - boundary-1
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0033106
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
  - GO:0033106
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
  - GO:0033106
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
  - GO:0033106
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
  - GO:0033106
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
  reference: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  locator: Entire maintained YAML including definition/source, hierarchy, synonyms,
    component, functions if present, taxonomy, examples, every graph node/edge, discussions
    and history
  accessed_at: '2026-10-21T10:59:55Z'
  support: context_only
  summary: The entire target was read against fresh native inspection. No scientific
    record, mapping status or history was changed.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent essentiality; CausalNode component_ref; docs/CURATION.md
    and native review checklist
  accessed_at: '2026-10-21T10:59:55Z'
  support: context_only
  summary: Essentiality asks whether the structure forms without a component; observed
    membership and activity do not establish experimental formation necessity. component_ref
    identifies an own-component node. Optional slots are not mandatory. Reviewed-label-only
    collective lipid material is distinct from a whole membrane-bounded compartment.
- evidence_id: cis-membrane-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005794,GO:0005801,GO:0033106,GO:0098791
  locator: Complete GO0033106, GO0005801, GO0005794, GO0098791 and GO0005783 definitions,
    comments, synonyms and relevant relationships; original batch22 native snapshot
    retained
  accessed_at: '2026-10-21T10:51:31.284848Z'
  support: supports
  summary: GO0033106 exactly denotes the lipid bilayer surrounding CGN compartments
    and supplies the maintained exact synonym. GO0005801 supplies direct membrane
    parthood and defines the containing tubular/cisternal network on the ER-facing
    Golgi side; its comment excludes CGN from the Golgi stack. Golgi apparatus and
    ER identities are distinct and valid.
  snapshot_sha256: 1f64f46ea3228d75112cc4a7cd62683682181d7f56a4b695efb1f8f03db842e8
- evidence_id: cis-membrane-agent-go-parent
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139
  locator: Complete GO0000139 identity, definition, synonyms and returned relationships
  accessed_at: '2026-10-21T10:59:03.588017Z'
  support: supports
  summary: Native GO0000139 defines the Golgi membrane as the lipid bilayer around
    any Golgi compartment. The specific CGN-membrane definition fits this broader
    membrane class; this is a definition-based hierarchy check, not a claim that a
    direct is_a edge was returned.
  snapshot_sha256: c72b414cdeea8f8b7e171c6ba56625fba7b621cbf2eb987f05aa8635300f8f6f
- evidence_id: cis-membrane-agent-tax-4922
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4922
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:51:31.391999Z'
  support: supports
  summary: This native ENA taxonomy response identifies Komagataella pastoris, species.
    It verifies only this taxon identity and rank, not experimental occurrence or
    strain provenance.
  snapshot_sha256: 5896e5992030d82c3a2bfe36e0c5cd013b4fd03c025f4db8bef695f70456a1d1
- evidence_id: cis-membrane-agent-tax-460519
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/460519
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:52:45.143036Z'
  support: supports
  summary: This native ENA taxonomy response identifies Komagataella phaffii, species.
    It verifies only this taxon identity and rank, not experimental occurrence or
    strain provenance.
  snapshot_sha256: c8f1333ff9a50b6e22e65fa32b6a5a349d82c72b92401daadf978166d2e89376
- evidence_id: cis-membrane-agent-doi-10.1083_jcb.145.1.69
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
- evidence_id: cis-membrane-agent-jats-PMC2148216
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2148216.1/PMC2148216.1.xml
  locator: Entire Results and all five subsections; entire Discussion; Methods / Strains
    and Plasmids; complete TablesI-IV; Introduction paragraphs concerning cisternal
    maturation and yeast comparison. Other Methods, complete Introduction, raw images
    and supplements were not comprehensively audited. Original batch22 reading and
    immutable receipt reused.
  accessed_at: '2026-10-21T10:52:00.890099Z'
  support: supports
  summary: Rossanese1999 directly compares ordered Pichia Golgi stacks with dispersed
    Saccharomyces cisternae. The Sec13-positive tubulovesicular region is assigned
    to transitional ER adjacent to stacks, and early/late marker overlap can reflect
    closely apposed structures. Methods identifies PPY1 and its isogenic PPY12 his4
    arg4 derivative. These observations establish stack/tER organization, not specific
    identification of a distinct CGN or its membrane. Cisternal-formation mechanisms
    are proposed models.
  snapshot_sha256: e9eb8235003747a36696a90d27a3fd45f601b1e46dfb3bba5419d779b5fe9590
- evidence_id: cis-membrane-agent-atcc-204163
  kind: authority
  reference: https://www.atcc.org/products/204163
  locator: Product organism, PPY12 strain designation, his4 arg4 genotype, Comments
    reidentification and History deposited-as/depositor fields
  accessed_at: '2026-10-21T10:52:45.142535Z'
  support: supports
  summary: ATCC204163 identifies PPY12 as K. phaffii and states that its former K.
    pastoris identification was changed after in-house sequence analysis. The historical
    deposited name Pichia pastoris is not treated as an exact current-species bridge.
  snapshot_sha256: 3c8663a19400c95a9669aeb0014e15527ed2c530e333df80501e6eb8d01d5319
- evidence_id: cis-membrane-agent-ena-LC815816
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/LC815816.1?download=false
  locator: DE/OS/OC identity and source qualifiers organism, strain and db_xref taxon460519;
    bibliographic provenance
  accessed_at: '2026-10-21T10:52:45.142930Z'
  support: supports
  summary: Native ENA LC815816.1 independently identifies organism K. phaffii, strain
    PPY12 and taxon460519. Only this strain/taxon linkage is used; the deposited ATG14
    gene is not interpreted as a CGN-membrane component.
  snapshot_sha256: f02d748dce33d5c56b830ab9e96ccb14facd65a8a7621bdaa10c7711eb8d63b4
- evidence_id: cis-membrane-agent-cho2000-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/S0014-5793%2800%2901268-0%22
  locator: Exact DOI/title/authors/PMID10713261 and complete abstract; no full article
    body
  accessed_at: '2026-10-21T10:52:01.200160Z'
  support: supports
  summary: The exact Cho/Noda/Yoda2000 metadata and abstract identify a Sed5-immunoisolated
    early Golgi fraction in S. cerevisiae, with selected Golgi markers and separation
    from ER/late-Golgi markers. This does not specifically establish a distinct CGN-membrane
    inventory. The existing constituent-versus-trafficking caution remains appropriate.
  snapshot_sha256: b0960521e38911bcc0523d02dcbc5d953440044fcace3d795af4bf575d3fd67f
- evidence_id: cis-membrane-agent-cho2000-html
  kind: authority
  reference: https://febs.onlinelibrary.wiley.com/doi/full/10.1016/S0014-5793%2800%2901268-0
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:52:45.143274Z'
  support: context_only
  summary: The publisher full-text route returnedHTTP403. Exact native metadata and
    abstract were independently available.
  snapshot_sha256: d8a6e12757bd32866af00ef2200ea277d965f98b9279e90aa9bdf87bc571f9d0
- evidence_id: cis-membrane-agent-cho2000-pdf
  kind: authority
  reference: https://febs.onlinelibrary.wiley.com/doi/pdfdirect/10.1016/S0014-5793%2800%2901268-0
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:52:45.143129Z'
  support: context_only
  summary: The publisher PDF route returnedHTTP403; this response is not an article
    PDF.
  snapshot_sha256: 1d8ca7528f70488c47614c7d8eedfd13fb5c64cbc37827517c91e018503dacaf
- evidence_id: boundary-0
  kind: record_content
  reference: data/structures/membrane_organelle/cis_golgi_network.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:59:55Z'
  support: context_only
  summary: Only these boundary fields were read for context. This is not an additional
    full scientific review of the neighboring record.
- evidence_id: boundary-1
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_membrane.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:59:55Z'
  support: context_only
  summary: Only these boundary fields were read for context. This is not an additional
    full scientific review of the neighboring record.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:57:12Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/cis_golgi_network_membrane.yaml'
  snapshot_sha256: f2c0bdb8446ab5bef6fb15d7945fd27d94f52c5463899f6d54075b50a9efc090
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/cis_golgi_network_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:57:13Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/cis_golgi_network_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/cis_golgi_network_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/cis_golgi_network_membrane-strict.tsv"
  snapshot_sha256: a0be38b9c8e1fc5adae2a2b6a60886a5a1a9ebe7fd893c35c818d6e2137ccb55
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:59:55Z'
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
  topic: Exact membrane identity and container boundary
  outcome: supported
  target_ids:
  - GO:0033106
  summary: The exact GO membrane definition and synonym are valid. The broader Golgi-membrane
    parent fits the definitions, and parthood in the whole CGN is directly supported.
    The membrane is not confused with the network, Golgi stack or transitional ER
    in the generic definition.
  evidence_ids:
  - cis-membrane-agent-go
  - cis-membrane-agent-go-parent
  - boundary-0
  - boundary-1
  - record
- assessment_id: material
  area: grounding
  topic: Collective lipid-bilayer constituent
  outcome: supported
  target_ids:
  - GO:0033106
  summary: The reviewed-label-only row names the complete constituting lipid material
    without asserting a species-specific composition. No molecular lipid or protein
    family is established as an exact grounding for that collective material. Sed5-positive
    fractionation and COPII localization do not justify treating all early trafficking
    machinery as membrane structural constituents.
  evidence_ids:
  - cis-membrane-agent-go
  - cis-membrane-agent-go-parent
  - cis-membrane-agent-cho2000-meta
  - cis-membrane-agent-jats-PMC2148216
  - record
  - policy
- assessment_id: necessity
  area: evidence
  topic: Constitution and formation necessity
  outcome: unknown
  target_ids:
  - GO:0033106
  summary: The ESSENTIAL row represents collective lipid-bilayer constitution. The
    sources do not determine individual lipid-species or protein requirements for
    formation of this membrane. Neither source-specific fraction membership nor the
    proposed cisternal-formation model establishes such experimental assembly necessity.
  evidence_ids:
  - cis-membrane-agent-go
  - cis-membrane-agent-jats-PMC2148216
  - cis-membrane-agent-cho2000-meta
  - record
  - policy
- assessment_id: taxon
  area: scope
  topic: Experimental lineage misassigned to a current species
  outcome: concern
  target_ids:
  - GO:0033106
  summary: Both taxon IDs are valid species entries, but the PPY1/PPY12 lineage used
    by the cited study is currently identified as K. phaffii460519, not the maintained
    K. pastoris4922. Current ATCC reidentification and independent ENA strain qualifiers
    establish this mismatch separately from the compartment-specific evidence question.
  evidence_ids:
  - cis-membrane-agent-jats-PMC2148216
  - cis-membrane-agent-atcc-204163
  - cis-membrane-agent-ena-LC815816
  - cis-membrane-agent-tax-4922
  - cis-membrane-agent-tax-460519
  - record
- assessment_id: example
  area: evidence
  topic: Stack morphology does not establish a specific CGN membrane
  outcome: concern
  target_ids:
  - GO:0033106
  summary: The occurrence and canonical-example notes accurately describe ordered
    Golgi stacks near tER, but these slots assert an example of this particular CGN
    membrane. The primary study does not identify a distinct CGN; its tubulovesicular
    Sec13 interface is assigned to tER. Therefore the CGN-membrane occurrence inference
    remains unsupported even after the taxon is corrected.
  evidence_ids:
  - cis-membrane-agent-jats-PMC2148216
  - cis-membrane-agent-go
  - cis-membrane-agent-cho2000-meta
  - record
- assessment_id: graph
  area: graph
  topic: Supported nonmechanistic membrane topology
  outcome: supported
  target_ids:
  - GO:0033106
  summary: The graph keeps the membrane separate from the complete CGN, Golgi apparatus
    and ER. Its membrane node is explicitly defined by GO0033106 as the lipid bilayer
    and can represent the collective material row through component_ref; it does not
    identify the whole membrane-bounded network with a lipid constituent. Bounds,
    parthood and ER-adjacency are supported as generic ontology topology. Rossanese
    provides broader stack/tER context, not direct CGN-membrane localization.
  evidence_ids:
  - cis-membrane-agent-go
  - cis-membrane-agent-go-parent
  - cis-membrane-agent-jats-PMC2148216
  - record
  - policy
  - boundary-0
  - boundary-1
- assessment_id: coverage
  area: completeness
  topic: Two independent source-scope corrections
  outcome: supported
  target_ids:
  - GO:0033106
  summary: Two major findings concern wrong experimental-species attribution and unsupported
    CGN-membrane occurrence/example support. No separate material-link defect or missing
    required molecular inventory was established. No function field or stronger trafficking
    mechanism needs to be added; native status remains unchanged.
  evidence_ids:
  - cis-membrane-agent-go
  - cis-membrane-agent-go-parent
  - cis-membrane-agent-jats-PMC2148216
  - cis-membrane-agent-atcc-204163
  - cis-membrane-agent-ena-LC815816
  - cis-membrane-agent-cho2000-meta
  - record
  - policy
findings:
- finding_id: F1
  issue_key: cis-golgi-network-membrane-ppy12-current-taxon
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: The cited PPY1/PPY12 lineage has the wrong current species
  description: Rossanese1999 used PPY1 and its isogenic PPY12 derivatives. ATCC identifies
    PPY12 as K. phaffii after sequence-based reidentification; ENA LC815816.1 independently
    pairs PPY12 with taxon460519. The maintained occurrence and canonical-example
    fields instead assign that experiment to K. pastoris4922. Historical Pichia pastoris
    nomenclature alone does not justify that current species assignment.
  target_ids:
  - GO:0033106
  field_paths:
  - taxonomic_distribution[0].taxon_id
  - taxonomic_distribution[0].taxon_label
  - canonical_examples[0].taxon_id
  - canonical_examples[0].taxon_label
  evidence_ids:
  - cis-membrane-agent-jats-PMC2148216
  - cis-membrane-agent-atcc-204163
  - cis-membrane-agent-ena-LC815816
  - cis-membrane-agent-tax-4922
  - cis-membrane-agent-tax-460519
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Major because the source-based occurrence and canonical example
    have a materially incorrect experimental taxon, while generic membrane identity
    is valid.
- finding_id: F2
  issue_key: cis-golgi-network-membrane-stack-study-evidence-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The stack study does not directly establish a CGN-membrane example
  description: The sole source attached to this membrane occurrence and canonical
    example resolves ordered Golgi stacks near transitional ER. Native GO distinguishes
    CGN from the Golgi stack; the study assigns its observed Sec13-positive tubulovesicular
    interface to tER. Stack membranes or early-Golgi marker apposition therefore do
    not directly identify the particular CGN membrane asserted by these fields. The
    scope gap persists after correcting the species.
  target_ids:
  - GO:0033106
  field_paths:
  - taxonomic_distribution[0]
  - canonical_examples[0]
  evidence_ids:
  - cis-membrane-agent-go
  - cis-membrane-agent-jats-PMC2148216
  - cis-membrane-agent-cho2000-meta
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Major because the only asserted occurrence and canonical example
    overextend the cited study to a distinct compartment membrane; generic GO identity
    and topology remain sound.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0033106
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    role: maintained scientific record
  description: Correct any retained PPY1/PPY12 experimental attribution to K. phaffii460519
    using the explicit strain bridge and retain the historical name in notes. Independently
    resolve the CGN-membrane evidence gap before retaining the study as a confirmed
    example.
  acceptance_checks:
  - Any retained experimental attribution uses the verified current taxon and documented
    strain provenance.
  - Retaxonomizing the strain is not treated as proof of CGN-membrane occurrence.
  - Focused native validators pass.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0033106
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    role: maintained scientific record
  description: Supply direct evidence for the CGN membrane in the asserted organism,
    or remove/defer the occurrence/example and retain Rossanese as explicitly broader
    Golgi-stack/tER context. Do not infer absence of CGN from the evidence gap or
    replace the exact membrane identity with a whole-stack concept.
  acceptance_checks:
  - Retained occurrence and canonical-example evidence distinguishes CGN membrane
    from generic stack membranes and tER.
  - The example does not rest solely on ordered stacks or early-Golgi marker localization.
  - The independent current-taxon mismatch is resolved for retained experimental attributions.
  - Focused native validators pass.
limitations:
- Public source raw files and metadata were copied unchanged from batch22, preserving
  original access times and hashes; only the GO0000139 parent entry was newly retrieved.
  Reuse does not broaden the recorded article-reading scope.
- Cho2000 was available as exact native metadata and abstract only. Both publisher
  body/PDF routes returned403. The initial unquoted DOI query returned zero hits;
  the quoted exact query resolved PMID10713261, so no source absence is inferred.
- Rossanese was read at the stated Results/Discussion, strain Methods and table scopes,
  without raw image reanalysis or a comprehensive remaining-Methods/supplement audit.
  The finding is bounded to these maintained claims and cited observations, not a
  claim that CGN is absent from the species.
- The ENA ATG14 deposit is used only for the PPY12 taxon bridge. Individual lipid/protein
  requirements for membrane formation remain unresolved; frozen neighbors were read
  only at the specified boundary fields.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
