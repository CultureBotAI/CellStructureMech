# ATP synthase family, composition and graph-grounding review

- Review: 20261012T100441Z-atp-synthase-family-graph-scope
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T09:58:08Z
- Finished UTC: 2026-10-12T10:04:41Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Three confirmed major findings: A-type occurrence is used to assert universal archaeal F-type presence, the ATP-product edge is grounded to enables, and a lineage-dependent b2/delta stalk is presented as an unqualified essential composition. PDB and UniProt provenance checks pass. Main-review body attributions remain incomplete.

## Scope And Provenance

Entire native record, five components, three examples, six graph edges, physical count, protein example, dataset and append-only history considered; exact main-review body claims remain unchecked; no sampling.

Selection: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e74d0c3e33df7e44348afbba1695b61c23262ab0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0045259 | data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml | maintained | proton-transporting ATP synthase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0045259 | Fresh target gate. Actual run: 2026-10-12T09:58:53Z to 2026-10-12T09:58:57Z. |
| strict | passed | True | GO:0045259 | Fresh target gate. Actual run: 2026-10-12T09:58:57Z to 2026-10-12T09:59:03Z. |
| snippets | passed | True | GO:0045259 | Fresh target gate. Zero of24 citations carries a snippet. Actual run: 2026-10-12T09:59:03Z to 2026-10-12T09:59:30Z. |
| adapter-b_subtilis-atpA | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:28Z to 2026-10-12T09:58:28Z. |
| adapter-b_subtilis-atpB | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:32Z to 2026-10-12T09:58:33Z. |
| adapter-b_subtilis-atpC | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:30Z to 2026-10-12T09:58:31Z. |
| adapter-b_subtilis-atpD | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:28Z to 2026-10-12T09:58:29Z. |
| adapter-b_subtilis-atpE | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:31Z to 2026-10-12T09:58:32Z. |
| adapter-b_subtilis-atpF | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:33Z to 2026-10-12T09:58:34Z. |
| adapter-b_subtilis-atpG | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:29Z to 2026-10-12T09:58:30Z. |
| adapter-b_subtilis-atpH | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:34Z to 2026-10-12T09:58:34Z. |
| adapter-datasets | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:20Z to 2026-10-12T09:58:21Z. |
| adapter-e_coli-atpA | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:21Z to 2026-10-12T09:58:22Z. |
| adapter-e_coli-atpB | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:26Z to 2026-10-12T09:58:27Z. |
| adapter-e_coli-atpC | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:24Z to 2026-10-12T09:58:25Z. |
| adapter-e_coli-atpD | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:22Z to 2026-10-12T09:58:23Z. |
| adapter-e_coli-atpE | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:25Z to 2026-10-12T09:58:26Z. |
| adapter-e_coli-atpF | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:27Z to 2026-10-12T09:58:27Z. |
| adapter-e_coli-atpG | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:23Z to 2026-10-12T09:58:24Z. |
| adapter-e_coli-atpH | passed | False | GO:0045259 | Fresh structured-source check; no module hit informs the verdict. Actual run: 2026-10-12T09:58:27Z to 2026-10-12T09:58:28Z. |
| reused-release-qc | passed | True | GO:0045259 | Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped; labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:33:07Z to 2026-10-12T06:45:16Z. |
| reused-release-labels | passed | True | GO:0045259 | Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped; labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:45:16Z to 2026-10-12T06:47:16Z. |
| reused-release-traits | passed | True | GO:0045259 | Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped; labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:48:15Z to 2026-10-12T06:48:52Z. |
| reused-curies-live | passed | True | GO:0045259 | Verified unchanged-input reuse: live CURIE4023OK/251skips;206 valid review bundles;4 contract tests. New post-save checks follow. Actual run: 2026-10-12T07:05:41Z to 2026-10-12T07:10:58Z. |
| reused-post-save-archive | passed | True | GO:0045259 | Verified unchanged-input reuse: live CURIE4023OK/251skips;206 valid review bundles;4 contract tests. New post-save checks follow. Actual run: 2026-10-12T09:50:24Z to 2026-10-12T09:51:43Z. |
| reused-post-save-contract | passed | True | GO:0045259 | Verified unchanged-input reuse: live CURIE4023OK/251skips;206 valid review bundles;4 contract tests. New post-save checks follow. Actual run: 2026-10-12T09:51:43Z to 2026-10-12T09:53:02Z. |
| Kuehlbrandt2019 detailed claim attribution | unavailable | True | GO:0045259 | Publisher full-text and institutional-repository requests returned403. Abstract and metadata inspected; exact8-17 count, B.subtilis example, bacterial prevalence, assembly-essentiality and detailed body attributions remain unverified. No biological defect is inferred solely from access failure. |

## Scientific And Domain Assessments

### F-type structure versus related rotary ATPase families

identity: concern. Targets: GO:0045259.

GO identity and the F1Fo architecture agree with each other. The archaeal occurrence justification instead describes a related family and does not establish an instance of this structure. Retain the valid F-type ID while correcting that scope; do not relabel all A-type enzymes as F-type.

### All five constituent groups

scope: concern. Targets: GO:0045259.

Head, rotor, central stalk and a-subunit roles have bounded bacterial support. The peripheral-stalk row lacks a qualifier for its fixed b2/delta pattern. All ESSENTIAL flags use the native assembly definition; gene presence and a wild-type structure do not independently verify those deletion/assembly assertions.

### c-ring8-17 range and physical-property context

quantity: unknown. Targets: GO:0045259.

The value is explicitly a species-dependent rotor-subunit count, not whole-complex size. E.coli c10 is directly supported. Exact support for the upper17 bound in Kuehlbrandt2019 remains unread; the earlier Walker review is not used to reject a later range.

### Universal domain rows and examples

scope: concern. Targets: GO:0045259.

All taxon labels resolve. The A-type argument does not support Archaea UNIVERSAL for this F-type record. Exact bacterial prevalence and the B.subtilis attribution to the main review remain unverified. The local UNIVERSAL enum means essentially every member, so acknowledged rare losses alone are not treated as a logical contradiction.

### E.coli species/strain and protein-example boundaries

provenance: supported. Targets: GO:0045259.

The PDB example correctly preserves the repository species-level source562; the UniProt example is independently K12 taxon83333. The dataset does not claim a wild-type active-turnover preparation. Exact-node atpB uniqueness and localized evidence are supported without turning protein annotation into assembly proof.

### Rotary coupling and ATP synthesis

evidence: supported. Targets: GO:0045259.

Inspected primary context supports proton-driven a/c-interface coupling, a rotating central stalk and nucleotide catalysis. The native descriptions do not assert a numerical step size or perfectly rigid stator. This does not complete detailed nearest-source attribution to the inaccessible main review.

### All six mechanistic edges and relation grounding

graph: concern. Targets: GO:0045259.

Five described coupling/participation relations are compatible with inspected evidence at this coarse mechanism level. The head-to-ATP edge has biologically sensible prose but an incompatible enables identifier. Correct the ontology relation or model an activity node; chemical ATP must remain a product.

### 6OQR entry, assembly, entities and map

provenance: supported. Targets: GO:0045259.

All eight deposited entity-to-UniProt mappings match. Method, source taxon, title,3.1-Angstrom resolution, DOI/PMID, dates and EMDB link agree. Global/local/pseudo symmetry annotations are not independent whole-assembly copy counts; the native notes retain their context rather than collapsing them.

### Optional fields and genuine unresolved scope

completeness: supported. Targets: GO:0045259.

No image, trait, extra dataset or new component row is required merely to populate an optional slot. The actionable issues concern existing assertions, not empty optional fields.

### Native gates, references and review completion

schema: unknown. Targets: GO:0045259.

Deterministic target gates pass and all relied-on stable identifiers resolve after correcting the RO lookup endpoint. The main review body remains inaccessible, preventing a complete claim-level review despite concrete findings elsewhere.

### Maintained inputs, status and histories

ownership: supported. Targets: GO:0045259.

Entire YAML and its one append-only history were read. Scientific fixes belong in maintained YAML through the guarded writer and curation history, not generated pages. Current PROPOSED status and all existing files remain unchanged; no predecessor disposition is invented.

## Findings

### F1: Do not use A-type occurrence to assert universal archaeal F-type distribution

major / open / confirmed; issue key: proton-atp-synthase-family-distribution.

The Archaea row justifies UNIVERSAL by saying archaea use the related A-type synthase. GO0045259 and the native F1Fo architecture denote F-type. Related function is not identity. Remove or recurate that occurrence assertion using family-specific evidence; this finding does not assert that every archaeal lineage lacks F-type enzymes.

### F2: Correct enables grounding on the ATP-product edge

major / open / confirmed; issue key: proton-atp-synthase-atp-edge-relation.

The edge head catalyses formation of ATP is grounded to RO0002327, enables. This relation concerns execution of a process/activity, whereas its target here is chemical ATP. Preserve the biological product claim with a correctly scoped relation or an explicit catalytic-activity/product representation; remove unsupported grounding rather than guess a substitute.

### F3: Scope the b2/delta stalk composition to the appropriate lineage

major / open / confirmed; issue key: proton-atp-synthase-stalk-composition.

The generic structure has an unqualified ESSENTIAL b2/delta peripheral-stalk row. The inspected review distinguishes b/b-prime variants and mitochondrial alternatives; b2 is directly verified here only for E.coli. Qualify the prototype or represent the conserved stalk separately from variable subunits.

## Recommended Actions And Acceptance Checks

### A1

Recurate the archaeal row at the actual family boundary without changing the valid F-type GO identity.

- No A-type occurrence is counted as F-type presence.
- Any retained archaeal assertion has inspected family-specific evidence and bounded prevalence.
- Preserve PROPOSED, append actual curation history, run native gates and save a lineage-linked successor.

### A2

Correct the head-to-ATP ontology predicate while preserving the supported product relationship.

- Relation identifier, label, direction and subject/object categories agree with an inspected authority.
- ATP remains a chemical product rather than the object of enables.
- Run native graph/schema/strict gates and retain this issue key in the successor.

### A3

Separate conserved stalk function from lineage-dependent composition and assembly requirement.

- Generic component wording no longer requires the E.coli b2 pattern across all F-type lineages.
- Essentiality follows the native structure-formation meaning and an explicitly supported scope.
- Preserve verified PDB metadata and species-versus-strain distinctions.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml; Entire YAML, all five component rows, three examples, six edges, one dataset and append-only history | supports | The record denotes an F-type enzyme yet marks Archaea UNIVERSAL using related A-type ATP synthase as its justification. The peripheral-stalk row requires an unqualified b2/delta composition. A head-to-ATP product edge uses RO0002327. |
| go | GO:0045259; GO:0015986; Complete current names, definitions, aspects and synonyms | supports | GO0045259 explicitly denotes a two-sector F0/F1 rotary complex with F-type synonyms. The process grounding denotes proton-motive-force-driven ATP synthesis. Neither makes related A-type complexes instances of the F-type structure. |
| walker | https://doi.org/10.1042/BST20110773; Author-uploaded article text at https://www.researchgate.net/publication/235377761_The_ATP_synthase_the_understood_the_uncertain_and_the_unknown ; General features, Overall structure, Figure2 caption, peripheral-stalk and bioenergetic-cost sections | supports | The review distinguishes F-type enzymes from related archaeal A-type enzymes and describes lineage-dependent stalk variants. It supports general rotary organization and variable ring counts; it is not treated as direct evidence for every later structural detail. Web body text was readable despite the separate local capture returning403. |
| kuhlbrandt | https://doi.org/10.1146/annurev-biochem-013118-110903; Complete abstract and bibliographic identity; body unavailable | partial | The abstract supports conserved subunit-a channels and rotary coupling with flexible F1/stalk movement. Detailed taxonomic prevalence, B.subtilis example attribution, assembly essentiality and the exact8-17 count remain unchecked against the cited body. |
| sobti | https://doi.org/10.1038/s41467-020-16387-2; Complete abstract, Introduction, rotational-substate and Fo-interaction Results, purification/grid Methods and data availability | supports | The study uses cysteine-free, beta-His-tagged E.coli enzyme expressed in DK8 and imaged with MgADP, not a movie of ongoing synthesis. It supports bacterial subunit architecture, channels and coupling context and assigns sub-state1A to6OQR/EMD20167. |
| pdb | https://www.rcsb.org/structure/6OQR; Current entry, assembly1 and all eight polymer entities | supports | Title, experimental EM method,3.1-Angstrom resolution, species562, dates, DOI/PMID, eight exact UniProt mappings and four symmetry annotations agree with the native dataset. Eight entity types are not eight chains: this assembly contains22 protein chains. |
| emdb | https://www.ebi.ac.uk/emdb/EMD-20167; Current map metadata, primary citation and PDB cross-reference | supports | EMD20167 links6OQR and the same Sobti paper. No raw map or molecular rendering was reanalyzed; the native dataset is metadata-only. |
| uniprot | https://rest.uniprot.org/uniprotkb/P0AB98.json; Current entry identity, gene, taxon, reviewed status, subcellular-location evidence and cited Daley reference | supports | P0AB98 is reviewed atpB on taxon83333. UniProt attaches PMID15919996/ECO0000269 to inner-membrane localization, exactly as the native note says, not to assembly membership. All seven other PDB-linked accessions also resolve to the expected subunits. |
| unique | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AatpB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete reviewed atpB search in the K12 subtree | supports | Three entries returned: P0AB98 at83333, B1X9W6 at316385 and C4ZZ16 at595496. Thus the exact-node uniqueness assertion and warning about sub-strain entries are supported. |
| daley | https://pubmed.ncbi.nlm.nih.gov/15919996/; Complete abstract and citation identity; current UniProt evidence attachment separately inspected | supports | Daley2005 is the membrane-topology study named by the record. Its full experiment/supplements were not reanalyzed; the narrower claim about what UniProt cites is directly verified in that database. |
| ro | RO:0002327; Complete OLS relation entry obtained through the properties endpoint | supports | The current relation is enables: its object is something the subject executes. It does not assert formation of ATP as a chemical product. The initial terms-endpoint404 was a query-type error, not an obsolete identifier. |
| atp | CHEBI:15422; Current ChEBI label, definition and identity | supports | ATP is a chemical entity, not an activity executed by the catalytic head. The chemical node itself is correctly grounded. |
| eco | ECO:0000269; Current ECO term | supports | Experimental evidence used in manual assertion agrees with the native UniProt evidence-note scope. |
| license | https://www.rcsb.org/pages/usage-policy; PDB archive licensing paragraph | supports | RCSB states that PDB archive data are released under CC0. This does not license unrelated journal figures; no figure is ingested. |
| adapter | https://imodulondb.org/; Fresh28-dataset inventory and16 gene searches across e_coli/precise1k and b_subtilis/modulome | supports | All eight atp gene names map to expected bacterial annotations in each dataset. Every query returned zero iModulon hits; broad atpA searches also returned unrelated ATPase-name matches. These annotations do not prove assembly essentiality, prevalence or molecular mechanism. |
| validation | /private/tmp/csm-review-20261012T095717Z-atp/baseline-verification.json; Fresh target checks and checksum-verified wider-check reuse | supports | Schema/strict pass; zero of24 citations carries a snippet. Wider QC987passed/3skipped, cached label/trait limits, live CURIE4023OK/251skips and206-bundle/four-contract-test results are explicit reuse, not fresh execution. |
| search | reviews/structured/; Ignored-inclusive target, predecessor and proposed-issue-key searches | supports | One native target, no canonical predecessor among206 bundles and no existing occurrence of the three new issue keys in the searched local review/research/curation roots. No remote issue-absence claim. |
| tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete current taxonomy entry | supports | Native taxon identifier and label agree; source support for occurrence is assessed separately. |
| tax-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; Complete current taxonomy entry | supports | Native taxon identifier and label agree; source support for occurrence is assessed separately. |
| tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete current taxonomy entry | supports | Native taxon identifier and label agree; source support for occurrence is assessed separately. |
| tax-1423 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1423; Complete current taxonomy entry | supports | Native taxon identifier and label agree; source support for occurrence is assessed separately. |
| tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete current taxonomy entry | supports | Native taxon identifier and label agree; source support for occurrence is assessed separately. |

## Limits And Additional Notes

- Partial, same-agent scientific review, not an independent human sign-off or exhaustive literature/retraction search. Main-review body access is still required for completion.
- Kuehlbrandt2019 was inspected as complete abstract and metadata only. Bacterial prevalence, the B.subtilis example, exact8-17 range and all assembly-essentiality claims are not fully verified. Search snippets suggesting later-body content were not accepted as source evidence.
- Walker2013 body was read through the author-uploaded web transcription only in the sections listed in Evidence; the direct local request returned403. The readable body, not the error capture, supports the family/composition observations.
- Sobti2020 was read in the specified abstract/Introduction/Results/Methods/data-availability sections. No raw maps, figure pixels, supplements or deposited coordinates were independently reprocessed; static MgADP structures are not observed active rotation.
- Daley2005 was inspected as abstract and metadata; the native claim about UniProt evidence attachment was directly verified in the current entry. The full601-protein experiment was not repeated or audited.
- All42 local captures are retained:38 HTTP200, one RO terms-endpoint404 and three403 access failures. RO is a relation and resolves through the properties endpoint. Error captures are not scientific evidence. A bounded code search included a nonexistent guessed filename and exited2; the actual uniprot_genes.py file was then read, and live uniqueness was checked directly.
- Fresh17 adapter commands and target gates are separate from wider-check reuse. Exact gene matches are retained; broad ATPase-name matches and zero module hits do not establish presence/absence, phenotype, assembly or mechanism.
- Current PDB source assertion is species562; the primary expression host is DK8 and the linked UniProt records are K12 entries. Those sources describe different provenance layers and are not silently collapsed into a new source-strain assertion.
- No native edits, status/history changes, generated products or GitHub mutation. Existing publication approval remains unanswered; no workaround or retry. Prior bundles and legacy reports are preserved.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T100441Z-atp-synthase-family-graph-scope
kind: record
repository: CultureBotAI/CellStructureMech
title: ATP synthase family, composition and graph-grounding review
started_at: '2026-10-12T09:58:08Z'
finished_at: '2026-10-12T10:04:41Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same coding-agent context; no independent reviewer or human
    sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Three confirmed major findings: A-type occurrence is used to assert universal
  archaeal F-type presence, the ATP-product edge is grounded to enables, and a lineage-dependent
  b2/delta stalk is presented as an unqualified essential composition. PDB and UniProt
  provenance checks pass. Main-review body attributions remain incomplete.'
source:
  git_revision: e74d0c3e33df7e44348afbba1695b61c23262ab0
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    sha256: 82abd63f629a8fc9e4fee7fdbb0e0fc725c391bd84f9b1adc7360d2499c708ee
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
  - path: history/records/proton_transporting_atp_synthase_complex/2026-09-04T014136Z-codex-90001a.yaml
    sha256: c4f794693a72c306de67a0708e65e99ad15bf7924c4e9b220182ebfa3b96fe14
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
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0045259
  path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
  label: proton-transporting ATP synthase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    role: maintained scientific record
scope:
  description: Entire native record, five components, three examples, six graph edges,
    physical count, protein example, dataset and append-only history considered; exact
    main-review body claims remain unchecked; no sampling.
  selection: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0045259
  exclusions:
  - target: Detailed attributions to DOI:10.1146/annurev-biochem-013118-110903
    reason: Main body inaccessible, including exact8-17 bound, B.subtilis example,
      bacterial prevalence and assembly-essentiality support.
checks:
- check_id: schema
  name: schema
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate. Actual run: 2026-10-12T09:58:53Z to 2026-10-12T09:58:57Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - validation
- check_id: strict
  name: strict
  command: .venv/bin/python scripts/validate_strict.py data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate. Actual run: 2026-10-12T09:58:57Z to 2026-10-12T09:59:03Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - validation
- check_id: snippets
  name: snippets
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    --report /private/tmp/csm-review-20261012T095717Z-atp/snippets.md
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate. Zero of24 citations carries a snippet. Actual run:
    2026-10-12T09:59:03Z to 2026-10-12T09:59:30Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - validation
- check_id: adapter-b_subtilis-atpA
  name: adapter-b_subtilis-atpA
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism b_subtilis --dataset modulome --query atpA
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:28Z to 2026-10-12T09:58:28Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-b_subtilis-atpB
  name: adapter-b_subtilis-atpB
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism b_subtilis --dataset modulome --query atpB
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:32Z to 2026-10-12T09:58:33Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-b_subtilis-atpC
  name: adapter-b_subtilis-atpC
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism b_subtilis --dataset modulome --query atpC
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:30Z to 2026-10-12T09:58:31Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-b_subtilis-atpD
  name: adapter-b_subtilis-atpD
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism b_subtilis --dataset modulome --query atpD
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:28Z to 2026-10-12T09:58:29Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-b_subtilis-atpE
  name: adapter-b_subtilis-atpE
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism b_subtilis --dataset modulome --query atpE
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:31Z to 2026-10-12T09:58:32Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-b_subtilis-atpF
  name: adapter-b_subtilis-atpF
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism b_subtilis --dataset modulome --query atpF
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:33Z to 2026-10-12T09:58:34Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-b_subtilis-atpG
  name: adapter-b_subtilis-atpG
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism b_subtilis --dataset modulome --query atpG
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:29Z to 2026-10-12T09:58:30Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-b_subtilis-atpH
  name: adapter-b_subtilis-atpH
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism b_subtilis --dataset modulome --query atpH
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:34Z to 2026-10-12T09:58:34Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-datasets
  name: adapter-datasets
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:20Z to 2026-10-12T09:58:21Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-e_coli-atpA
  name: adapter-e_coli-atpA
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query atpA
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:21Z to 2026-10-12T09:58:22Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-e_coli-atpB
  name: adapter-e_coli-atpB
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query atpB
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:26Z to 2026-10-12T09:58:27Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-e_coli-atpC
  name: adapter-e_coli-atpC
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query atpC
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:24Z to 2026-10-12T09:58:25Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-e_coli-atpD
  name: adapter-e_coli-atpD
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query atpD
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:22Z to 2026-10-12T09:58:23Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-e_coli-atpE
  name: adapter-e_coli-atpE
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query atpE
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:25Z to 2026-10-12T09:58:26Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-e_coli-atpF
  name: adapter-e_coli-atpF
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query atpF
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:27Z to 2026-10-12T09:58:27Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-e_coli-atpG
  name: adapter-e_coli-atpG
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query atpG
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:23Z to 2026-10-12T09:58:24Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: adapter-e_coli-atpH
  name: adapter-e_coli-atpH
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query atpH
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh structured-source check; no module hit informs the verdict. Actual
    run: 2026-10-12T09:58:27Z to 2026-10-12T09:58:28Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - adapter
- check_id: reused-release-qc
  name: reused-release-qc
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  status: passed
  required: true
  summary: 'Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped;
    labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:33:07Z
    to 2026-10-12T06:45:16Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - validation
- check_id: reused-release-labels
  name: reused-release-labels
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped;
    labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:45:16Z
    to 2026-10-12T06:47:16Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - validation
- check_id: reused-release-traits
  name: reused-release-traits
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  status: passed
  required: true
  summary: 'Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped;
    labels603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:48:15Z
    to 2026-10-12T06:48:52Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - validation
- check_id: reused-curies-live
  name: reused-curies-live
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  status: passed
  required: true
  summary: 'Verified unchanged-input reuse: live CURIE4023OK/251skips;206 valid review
    bundles;4 contract tests. New post-save checks follow. Actual run: 2026-10-12T07:05:41Z
    to 2026-10-12T07:10:58Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - validation
- check_id: reused-post-save-archive
  name: reused-post-save-archive
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  status: passed
  required: true
  summary: 'Verified unchanged-input reuse: live CURIE4023OK/251skips;206 valid review
    bundles;4 contract tests. New post-save checks follow. Actual run: 2026-10-12T09:50:24Z
    to 2026-10-12T09:51:43Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - validation
- check_id: reused-post-save-contract
  name: reused-post-save-contract
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  status: passed
  required: true
  summary: 'Verified unchanged-input reuse: live CURIE4023OK/251skips;206 valid review
    bundles;4 contract tests. New post-save checks follow. Actual run: 2026-10-12T09:51:43Z
    to 2026-10-12T09:53:02Z.'
  target_ids:
  - GO:0045259
  evidence_ids:
  - validation
- check_id: main-review-body
  name: Kuehlbrandt2019 detailed claim attribution
  status: unavailable
  required: true
  summary: Publisher full-text and institutional-repository requests returned403.
    Abstract and metadata inspected; exact8-17 count, B.subtilis example, bacterial
    prevalence, assembly-essentiality and detailed body attributions remain unverified.
    No biological defect is inferred solely from access failure.
  target_ids:
  - GO:0045259
  evidence_ids:
  - kuhlbrandt
evidence:
- evidence_id: native
  kind: record_content
  reference: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
  locator: Entire YAML, all five component rows, three examples, six edges, one dataset
    and append-only history
  summary: The record denotes an F-type enzyme yet marks Archaea UNIVERSAL using related
    A-type ATP synthase as its justification. The peripheral-stalk row requires an
    unqualified b2/delta composition. A head-to-ATP product edge uses RO0002327.
  support: supports
  accessed_at: '2026-10-12T10:04:41Z'
  snapshot_sha256: 82abd63f629a8fc9e4fee7fdbb0e0fc725c391bd84f9b1adc7360d2499c708ee
- evidence_id: go
  kind: authority
  reference: GO:0045259; GO:0015986
  locator: Complete current names, definitions, aspects and synonyms
  summary: GO0045259 explicitly denotes a two-sector F0/F1 rotary complex with F-type
    synonyms. The process grounding denotes proton-motive-force-driven ATP synthesis.
    Neither makes related A-type complexes instances of the F-type structure.
  support: supports
  accessed_at: '2026-10-12T09:58:43Z'
  snapshot_sha256: cee9abff0eda65f67290421d292b292bc990a86e22dd53fcbe91f56cebfb2309
- evidence_id: walker
  kind: authority
  reference: https://doi.org/10.1042/BST20110773
  locator: Author-uploaded article text at https://www.researchgate.net/publication/235377761_The_ATP_synthase_the_understood_the_uncertain_and_the_unknown
    ; General features, Overall structure, Figure2 caption, peripheral-stalk and bioenergetic-cost
    sections
  summary: The review distinguishes F-type enzymes from related archaeal A-type enzymes
    and describes lineage-dependent stalk variants. It supports general rotary organization
    and variable ring counts; it is not treated as direct evidence for every later
    structural detail. Web body text was readable despite the separate local capture
    returning403.
  support: supports
  accessed_at: '2026-10-12T10:04:41Z'
- evidence_id: kuhlbrandt
  kind: authority
  reference: https://doi.org/10.1146/annurev-biochem-013118-110903
  locator: Complete abstract and bibliographic identity; body unavailable
  summary: The abstract supports conserved subunit-a channels and rotary coupling
    with flexible F1/stalk movement. Detailed taxonomic prevalence, B.subtilis example
    attribution, assembly essentiality and the exact8-17 count remain unchecked against
    the cited body.
  support: partial
  accessed_at: '2026-10-12T09:58:47Z'
  snapshot_sha256: 4fa5a6a1f83ab69430c29cf6c354bd42a1b170fd9c2fe7997fad89874cc37fcc
- evidence_id: sobti
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-020-16387-2
  locator: Complete abstract, Introduction, rotational-substate and Fo-interaction
    Results, purification/grid Methods and data availability
  summary: The study uses cysteine-free, beta-His-tagged E.coli enzyme expressed in
    DK8 and imaged with MgADP, not a movie of ongoing synthesis. It supports bacterial
    subunit architecture, channels and coupling context and assigns sub-state1A to6OQR/EMD20167.
  support: supports
  accessed_at: '2026-10-12T09:59:26Z'
  snapshot_sha256: 8cc93a3e2ac4c914da93cae1e16a01ab6a86311d5e7d1fc66887b94207724330
- evidence_id: pdb
  kind: database
  reference: https://www.rcsb.org/structure/6OQR
  locator: Current entry, assembly1 and all eight polymer entities
  summary: 'Title, experimental EM method,3.1-Angstrom resolution, species562, dates,
    DOI/PMID, eight exact UniProt mappings and four symmetry annotations agree with
    the native dataset. Eight entity types are not eight chains: this assembly contains22
    protein chains.'
  support: supports
  accessed_at: '2026-10-12T09:59:10Z'
  snapshot_sha256: b5fd677b0f23ab016916be9ebc6c0b2ac998e34a5334e8e8ea4422880d63f517
- evidence_id: emdb
  kind: database
  reference: https://www.ebi.ac.uk/emdb/EMD-20167
  locator: Current map metadata, primary citation and PDB cross-reference
  summary: EMD20167 links6OQR and the same Sobti paper. No raw map or molecular rendering
    was reanalyzed; the native dataset is metadata-only.
  support: supports
  accessed_at: '2026-10-12T10:00:48Z'
  snapshot_sha256: 82b6732623de18acd8ff984761b8ad17924c9bf8faa109d1d830de26658c5e76
- evidence_id: uniprot
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AB98.json
  locator: Current entry identity, gene, taxon, reviewed status, subcellular-location
    evidence and cited Daley reference
  summary: P0AB98 is reviewed atpB on taxon83333. UniProt attaches PMID15919996/ECO0000269
    to inner-membrane localization, exactly as the native note says, not to assembly
    membership. All seven other PDB-linked accessions also resolve to the expected
    subunits.
  support: supports
  accessed_at: '2026-10-12T09:59:17Z'
  snapshot_sha256: 7fcd1726b143dd78ceca55b877f111d02e9e6b20c5ece7ce6d9da04dbd1b9bc6
- evidence_id: unique
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AatpB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete reviewed atpB search in the K12 subtree
  summary: 'Three entries returned: P0AB98 at83333, B1X9W6 at316385 and C4ZZ16 at595496.
    Thus the exact-node uniqueness assertion and warning about sub-strain entries
    are supported.'
  support: supports
  accessed_at: '2026-10-12T10:02:00Z'
  snapshot_sha256: b29ce23edbc94be6bb0036baa523e7bd0addebb7a2895657663adad8956e73ba
- evidence_id: daley
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15919996/
  locator: Complete abstract and citation identity; current UniProt evidence attachment
    separately inspected
  summary: Daley2005 is the membrane-topology study named by the record. Its full
    experiment/supplements were not reanalyzed; the narrower claim about what UniProt
    cites is directly verified in that database.
  support: supports
  accessed_at: '2026-10-12T09:58:50Z'
  snapshot_sha256: 7c83fcb28f68a14cbc566904fbd32091121999b45f87b73b013e0396826b0102
- evidence_id: ro
  kind: authority
  reference: RO:0002327
  locator: Complete OLS relation entry obtained through the properties endpoint
  summary: 'The current relation is enables: its object is something the subject executes.
    It does not assert formation of ATP as a chemical product. The initial terms-endpoint404
    was a query-type error, not an obsolete identifier.'
  support: supports
  accessed_at: '2026-10-12T09:59:25Z'
  snapshot_sha256: 5bbceaccdeae417c68a2344aac455d7a7607b3f29b5295d909a16de496b49419
- evidence_id: atp
  kind: authority
  reference: CHEBI:15422
  locator: Current ChEBI label, definition and identity
  summary: ATP is a chemical entity, not an activity executed by the catalytic head.
    The chemical node itself is correctly grounded.
  support: supports
  accessed_at: '2026-10-12T09:58:51Z'
  snapshot_sha256: 8503d1fb2389a96c9e01658c575db87d7282aa97bda93caae78ba3bb90a69b49
- evidence_id: eco
  kind: authority
  reference: ECO:0000269
  locator: Current ECO term
  summary: Experimental evidence used in manual assertion agrees with the native UniProt
    evidence-note scope.
  support: supports
  accessed_at: '2026-10-12T09:59:10Z'
  snapshot_sha256: 93e3084215699f536b15652e236a64f0ff6e1a8d3dd283e744bef108924ccd12
- evidence_id: license
  kind: authority
  reference: https://www.rcsb.org/pages/usage-policy
  locator: PDB archive licensing paragraph
  summary: RCSB states that PDB archive data are released under CC0. This does not
    license unrelated journal figures; no figure is ingested.
  support: supports
  accessed_at: '2026-10-12T10:00:48Z'
  snapshot_sha256: b8ea0f57797374c41157f6f7316963819cba9f2fa8ed6162b6f4747ec3194be6
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/
  locator: Fresh28-dataset inventory and16 gene searches across e_coli/precise1k and
    b_subtilis/modulome
  summary: All eight atp gene names map to expected bacterial annotations in each
    dataset. Every query returned zero iModulon hits; broad atpA searches also returned
    unrelated ATPase-name matches. These annotations do not prove assembly essentiality,
    prevalence or molecular mechanism.
  support: supports
  accessed_at: '2026-10-12T10:04:41Z'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/csm-review-20261012T095717Z-atp/baseline-verification.json
  locator: Fresh target checks and checksum-verified wider-check reuse
  summary: Schema/strict pass; zero of24 citations carries a snippet. Wider QC987passed/3skipped,
    cached label/trait limits, live CURIE4023OK/251skips and206-bundle/four-contract-test
    results are explicit reuse, not fresh execution.
  support: supports
  accessed_at: '2026-10-12T10:04:41Z'
- evidence_id: search
  kind: search
  reference: reviews/structured/
  locator: Ignored-inclusive target, predecessor and proposed-issue-key searches
  summary: One native target, no canonical predecessor among206 bundles and no existing
    occurrence of the three new issue keys in the searched local review/research/curation
    roots. No remote issue-absence claim.
  support: supports
  accessed_at: '2026-10-12T10:04:41Z'
  search_scope: Path.rglob included hidden/ignored canonical bundles and history;
    rg -uu searched slug/identifier/issue keys across reviews, reports/yaml_record_review,
    research and curation. Research/build/reports/.claude/curation searches for the
    Kuehlbrandt DOI/title found cached metadata/readability entries, not an inspected
    full body in those roots.
- evidence_id: tax-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete current taxonomy entry
  summary: Native taxon identifier and label agree; source support for occurrence
    is assessed separately.
  support: supports
  accessed_at: '2026-10-12T09:58:44Z'
  snapshot_sha256: 7429617438ff0162ee4783c4c660f6127642e6ff686522e670c6ecf3a5b28816
- evidence_id: tax-2157
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: Complete current taxonomy entry
  summary: Native taxon identifier and label agree; source support for occurrence
    is assessed separately.
  support: supports
  accessed_at: '2026-10-12T09:58:45Z'
  snapshot_sha256: 9ddd1001f0c607eb9b7582ecd9e83d3d18a89ddf8e540ec75da7dc4c9939c6ae
- evidence_id: tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete current taxonomy entry
  summary: Native taxon identifier and label agree; source support for occurrence
    is assessed separately.
  support: supports
  accessed_at: '2026-10-12T09:58:45Z'
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: tax-1423
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1423
  locator: Complete current taxonomy entry
  summary: Native taxon identifier and label agree; source support for occurrence
    is assessed separately.
  support: supports
  accessed_at: '2026-10-12T09:58:46Z'
  snapshot_sha256: 880a1dc4b6c2c61078b5cdc583eb737f3d4b24abd842be827e0b4ffcbdaab471
- evidence_id: tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete current taxonomy entry
  summary: Native taxon identifier and label agree; source support for occurrence
    is assessed separately.
  support: supports
  accessed_at: '2026-10-12T09:58:47Z'
  snapshot_sha256: e57741d95cb5fd100d7f96cb4e99950761be3a9075ccde3ab220f2e4810f8e78
assessments:
- assessment_id: identity
  area: identity
  topic: F-type structure versus related rotary ATPase families
  outcome: concern
  summary: GO identity and the F1Fo architecture agree with each other. The archaeal
    occurrence justification instead describes a related family and does not establish
    an instance of this structure. Retain the valid F-type ID while correcting that
    scope; do not relabel all A-type enzymes as F-type.
  target_ids:
  - GO:0045259
  evidence_ids:
  - native
  - go
  - walker
- assessment_id: components
  area: scope
  topic: All five constituent groups
  outcome: concern
  summary: Head, rotor, central stalk and a-subunit roles have bounded bacterial support.
    The peripheral-stalk row lacks a qualifier for its fixed b2/delta pattern. All
    ESSENTIAL flags use the native assembly definition; gene presence and a wild-type
    structure do not independently verify those deletion/assembly assertions.
  target_ids:
  - GO:0045259
  evidence_ids:
  - native
  - sobti
  - walker
  - uniprot
  - adapter
- assessment_id: quantity
  area: quantity
  topic: c-ring8-17 range and physical-property context
  outcome: unknown
  summary: The value is explicitly a species-dependent rotor-subunit count, not whole-complex
    size. E.coli c10 is directly supported. Exact support for the upper17 bound in
    Kuehlbrandt2019 remains unread; the earlier Walker review is not used to reject
    a later range.
  target_ids:
  - GO:0045259
  evidence_ids:
  - native
  - pdb
  - sobti
  - kuhlbrandt
- assessment_id: taxonomy
  area: scope
  topic: Universal domain rows and examples
  outcome: concern
  summary: All taxon labels resolve. The A-type argument does not support Archaea
    UNIVERSAL for this F-type record. Exact bacterial prevalence and the B.subtilis
    attribution to the main review remain unverified. The local UNIVERSAL enum means
    essentially every member, so acknowledged rare losses alone are not treated as
    a logical contradiction.
  target_ids:
  - GO:0045259
  evidence_ids:
  - native
  - go
  - walker
  - tax-2
  - tax-2157
  - kuhlbrandt
- assessment_id: examples
  area: provenance
  topic: E.coli species/strain and protein-example boundaries
  outcome: supported
  summary: The PDB example correctly preserves the repository species-level source562;
    the UniProt example is independently K12 taxon83333. The dataset does not claim
    a wild-type active-turnover preparation. Exact-node atpB uniqueness and localized
    evidence are supported without turning protein annotation into assembly proof.
  target_ids:
  - GO:0045259
  evidence_ids:
  - native
  - pdb
  - sobti
  - uniprot
  - unique
  - daley
- assessment_id: function
  area: evidence
  topic: Rotary coupling and ATP synthesis
  outcome: supported
  summary: Inspected primary context supports proton-driven a/c-interface coupling,
    a rotating central stalk and nucleotide catalysis. The native descriptions do
    not assert a numerical step size or perfectly rigid stator. This does not complete
    detailed nearest-source attribution to the inaccessible main review.
  target_ids:
  - GO:0045259
  evidence_ids:
  - native
  - go
  - sobti
  - kuhlbrandt
- assessment_id: graph
  area: graph
  topic: All six mechanistic edges and relation grounding
  outcome: concern
  summary: Five described coupling/participation relations are compatible with inspected
    evidence at this coarse mechanism level. The head-to-ATP edge has biologically
    sensible prose but an incompatible enables identifier. Correct the ontology relation
    or model an activity node; chemical ATP must remain a product.
  target_ids:
  - GO:0045259
  evidence_ids:
  - native
  - sobti
  - ro
  - atp
- assessment_id: dataset
  area: provenance
  topic: 6OQR entry, assembly, entities and map
  outcome: supported
  summary: All eight deposited entity-to-UniProt mappings match. Method, source taxon,
    title,3.1-Angstrom resolution, DOI/PMID, dates and EMDB link agree. Global/local/pseudo
    symmetry annotations are not independent whole-assembly copy counts; the native
    notes retain their context rather than collapsing them.
  target_ids:
  - GO:0045259
  evidence_ids:
  - pdb
  - emdb
  - sobti
  - license
  dimensions:
  - name: preparation
    value: Cysteine-free E.coli enzyme with beta His-tag, expressed in DK8; MgADP
      state
    definition: Primary preparation context, not a reassignment of the PDB source
      taxon or proof of observed active rotation.
    evidence_ids:
    - sobti
  - name: assembly
    value: 8 protein entity types;22 polymer instances;c10 rotor
    definition: Distinguishes entity identity, biological assembly multiplicity and
      ring count.
    evidence_ids:
    - pdb
- assessment_id: completeness
  area: completeness
  topic: Optional fields and genuine unresolved scope
  outcome: supported
  summary: No image, trait, extra dataset or new component row is required merely
    to populate an optional slot. The actionable issues concern existing assertions,
    not empty optional fields.
  target_ids:
  - GO:0045259
  evidence_ids:
  - native
  - adapter
  - pdb
- assessment_id: checks
  area: schema
  topic: Native gates, references and review completion
  outcome: unknown
  summary: Deterministic target gates pass and all relied-on stable identifiers resolve
    after correcting the RO lookup endpoint. The main review body remains inaccessible,
    preventing a complete claim-level review despite concrete findings elsewhere.
  target_ids:
  - GO:0045259
  evidence_ids:
  - validation
  - kuhlbrandt
  - ro
- assessment_id: ownership
  area: ownership
  topic: Maintained inputs, status and histories
  outcome: supported
  summary: Entire YAML and its one append-only history were read. Scientific fixes
    belong in maintained YAML through the guarded writer and curation history, not
    generated pages. Current PROPOSED status and all existing files remain unchanged;
    no predecessor disposition is invented.
  target_ids:
  - GO:0045259
  evidence_ids:
  - native
  - search
findings:
- finding_id: F1
  issue_key: proton-atp-synthase-family-distribution
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Do not use A-type occurrence to assert universal archaeal F-type distribution
  description: The Archaea row justifies UNIVERSAL by saying archaea use the related
    A-type synthase. GO0045259 and the native F1Fo architecture denote F-type. Related
    function is not identity. Remove or recurate that occurrence assertion using family-specific
    evidence; this finding does not assert that every archaeal lineage lacks F-type
    enzymes.
  target_ids:
  - GO:0045259
  field_paths:
  - taxonomic_distribution[taxon_id=NCBITaxon:2157]
  evidence_ids:
  - native
  - go
  - walker
  rule_id: review-checklist:identity-and-taxonomic-scope
  native_severity: major
  normalization_reason: An occurrence assertion conflates distinct complex families
    across an entire domain, while the underlying F-type identity remains usable.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    role: maintained scientific record
- finding_id: F2
  issue_key: proton-atp-synthase-atp-edge-relation
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct enables grounding on the ATP-product edge
  description: The edge head catalyses formation of ATP is grounded to RO0002327,
    enables. This relation concerns execution of a process/activity, whereas its target
    here is chemical ATP. Preserve the biological product claim with a correctly scoped
    relation or an explicit catalytic-activity/product representation; remove unsupported
    grounding rather than guess a substitute.
  target_ids:
  - GO:0045259
  field_paths:
  - causal_graphs[rotary_catalysis].edges[subject=head,object=atp].predicate_id
  evidence_ids:
  - native
  - ro
  - atp
  rule_id: review-checklist:causal-edge-identity-and-grounding
  native_severity: major
  normalization_reason: The machine-readable relation changes the meaning and object
    category of a mechanistic assertion despite plausible display prose.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    role: maintained scientific record
- finding_id: F3
  issue_key: proton-atp-synthase-stalk-composition
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Scope the b2/delta stalk composition to the appropriate lineage
  description: The generic structure has an unqualified ESSENTIAL b2/delta peripheral-stalk
    row. The inspected review distinguishes b/b-prime variants and mitochondrial alternatives;
    b2 is directly verified here only for E.coli. Qualify the prototype or represent
    the conserved stalk separately from variable subunits.
  target_ids:
  - GO:0045259
  field_paths:
  - components[peripheral_stalk].label
  - components[peripheral_stalk].gene_symbols
  - components[peripheral_stalk].essentiality
  - components[peripheral_stalk].role
  evidence_ids:
  - native
  - walker
  - sobti
  - pdb
  rule_id: review-checklist:complex-composition-and-lineage-scope
  native_severity: major
  normalization_reason: A fixed composition is presented as required for the generic
    structure rather than as a lineage-bounded example.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Recurate the archaeal row at the actual family boundary without changing
    the valid F-type GO identity.
  finding_ids:
  - F1
  target_ids:
  - GO:0045259
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - No A-type occurrence is counted as F-type presence.
  - Any retained archaeal assertion has inspected family-specific evidence and bounded
    prevalence.
  - Preserve PROPOSED, append actual curation history, run native gates and save a
    lineage-linked successor.
- action_id: A2
  description: Correct the head-to-ATP ontology predicate while preserving the supported
    product relationship.
  finding_ids:
  - F2
  target_ids:
  - GO:0045259
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - Relation identifier, label, direction and subject/object categories agree with
    an inspected authority.
  - ATP remains a chemical product rather than the object of enables.
  - Run native graph/schema/strict gates and retain this issue key in the successor.
- action_id: A3
  description: Separate conserved stalk function from lineage-dependent composition
    and assembly requirement.
  finding_ids:
  - F3
  target_ids:
  - GO:0045259
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - Generic component wording no longer requires the E.coli b2 pattern across all
    F-type lineages.
  - Essentiality follows the native structure-formation meaning and an explicitly
    supported scope.
  - Preserve verified PDB metadata and species-versus-strain distinctions.
limitations:
- Partial, same-agent scientific review, not an independent human sign-off or exhaustive
  literature/retraction search. Main-review body access is still required for completion.
- Kuehlbrandt2019 was inspected as complete abstract and metadata only. Bacterial
  prevalence, the B.subtilis example, exact8-17 range and all assembly-essentiality
  claims are not fully verified. Search snippets suggesting later-body content were
  not accepted as source evidence.
- Walker2013 body was read through the author-uploaded web transcription only in the
  sections listed in Evidence; the direct local request returned403. The readable
  body, not the error capture, supports the family/composition observations.
- Sobti2020 was read in the specified abstract/Introduction/Results/Methods/data-availability
  sections. No raw maps, figure pixels, supplements or deposited coordinates were
  independently reprocessed; static MgADP structures are not observed active rotation.
- Daley2005 was inspected as abstract and metadata; the native claim about UniProt
  evidence attachment was directly verified in the current entry. The full601-protein
  experiment was not repeated or audited.
- All42 local captures are retained:38 HTTP200, one RO terms-endpoint404 and three403
  access failures. RO is a relation and resolves through the properties endpoint.
  Error captures are not scientific evidence. A bounded code search included a nonexistent
  guessed filename and exited2; the actual uniprot_genes.py file was then read, and
  live uniqueness was checked directly.
- Fresh17 adapter commands and target gates are separate from wider-check reuse. Exact
  gene matches are retained; broad ATPase-name matches and zero module hits do not
  establish presence/absence, phenotype, assembly or mechanism.
- Current PDB source assertion is species562; the primary expression host is DK8 and
  the linked UniProt records are K12 entries. Those sources describe different provenance
  layers and are not silently collapsed into a new source-strain assertion.
- No native edits, status/history changes, generated products or GitHub mutation.
  Existing publication approval remains unanswered; no workaround or retry. Prior
  bundles and legacy reports are preserved.
tags:
- scientific-review
- energy-complex
- scope
- graph-grounding
- partial
- major
```
