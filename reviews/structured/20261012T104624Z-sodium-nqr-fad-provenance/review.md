# Na+-NQR cofactor evidence provenance review

- Review: 20261012T104624Z-sodium-nqr-fad-provenance
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T10:40:38Z
- Finished UTC: 2026-10-12T10:46:24Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review completed with one minor finding: NqrF FAD support is incorrectly attributed to a current InterPro GO annotation. Six family identities, source-strain mappings, complete-core composition, whole-enzyme function and six coarse graph edges are otherwise supported within the stated limits.

## Scope And Provenance

One complete native record and both histories; all material claims, six component families/entity mappings, six graph edges and all native stable identifiers assessed. No sampling.

Selection: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e74d0c3e33df7e44348afbba1695b61c23262ab0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0160292 | data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml | maintained | sodium-translocating NADH:quinone reductase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0160292 | Fresh target gate. Actual UTC: 2026-10-12T10:40:55Z to 2026-10-12T10:40:57Z. |
| strict | passed | True | GO:0160292 | Fresh target gate. Actual UTC: 2026-10-12T10:40:57Z to 2026-10-12T10:41:00Z. |
| snippets | passed | True | GO:0160292 | Fresh target gate; zero of34 citations has a snippet, not automated full-text proof. Actual UTC: 2026-10-12T10:41:00Z to 2026-10-12T10:41:17Z. |
| reused-release-qc | passed | True | GO:0160292 | Original result reused after input/receipt hash checks. QC987passed/3skipped, labels603no-adapter skips, cached traits after earlier network failure. Not fresh CI. Actual UTC: 2026-10-12T06:33:07Z to 2026-10-12T06:45:16Z. |
| reused-release-labels | passed | True | GO:0160292 | Original result reused after input/receipt hash checks. QC987passed/3skipped, labels603no-adapter skips, cached traits after earlier network failure. Not fresh CI. Actual UTC: 2026-10-12T06:45:16Z to 2026-10-12T06:47:16Z. |
| reused-release-traits | passed | True | GO:0160292 | Original result reused after input/receipt hash checks. QC987passed/3skipped, labels603no-adapter skips, cached traits after earlier network failure. Not fresh CI. Actual UTC: 2026-10-12T06:48:15Z to 2026-10-12T06:48:52Z. |
| reused-curies-live | passed | True | GO:0160292 | Original result reused on unchanged bytes. Live CURIE4023OK/251SKIP/0unreachable;209valid bundles and4contract tests. New post-save archive/contract checks follow separately. Actual UTC: 2026-10-12T07:05:41Z to 2026-10-12T07:10:58Z. |
| reused-post-save-archive | passed | True | GO:0160292 | Original result reused on unchanged bytes. Live CURIE4023OK/251SKIP/0unreachable;209valid bundles and4contract tests. New post-save archive/contract checks follow separately. Actual UTC: 2026-10-12T10:37:07Z to 2026-10-12T10:38:34Z. |
| reused-post-save-contract | passed | True | GO:0160292 | Original result reused on unchanged bytes. Live CURIE4023OK/251SKIP/0unreachable;209valid bundles and4contract tests. New post-save archive/contract checks follow separately. Actual UTC: 2026-10-12T10:38:34Z to 2026-10-12T10:40:04Z. |
| adapter-datasets | passed | False | GO:0160292 | Fresh full inventory; no matching V.cholerae dataset. Actual UTC: 2026-10-12T10:40:50Z to 2026-10-12T10:40:51Z. |

## Scientific And Domain Assessments

### Na+-NQR identity, definition, synonyms and inferred parentage

identity: supported. Targets: GO:0160292.

The native record denotes the six-subunit sodium-translocating NADH:quinone complex, not proton-pumping complexI. Respiratory-chain parentage follows the source definitions and primary evidence; it is not currently an explicit GO is_a edge.

### Six exact component families

grounding: supported. Targets: GO:0160292.

All six supplied InterPro accessions are current family entries for the respective Nqr subunit and are cross-referenced by the deposited source proteins. The inconsistent E wording in the NqrF description does not override its concordant family identity and member models.

### Six-subunit composition and constituent roles

quantity: supported. Targets: GO:0160292.

The GO definition, primary paper and author-defined assembly support the NqrA-F complete core. ESSENTIAL is read as membership required for that defined complete structure, not cell viability or an assertion that no incomplete subassembly can persist. No native deletion experiment or universal kinetic stoichiometry is asserted. NqrB/C FMN roles, D/E membrane roles and NqrF cofactors agree with inspected sources.

### NqrF cofactor source-field attribution

provenance: concern. Targets: GO:0160292.

NqrF really carries FAD and2Fe-2S, but the evidence note incorrectly describes FAD binding as one of the current IPR010205 GO annotations. Restrict the correction to exact source attribution; do not remove the valid FAD role or change the family grounding.

### O395 sequence source and source-protein mapping

scope: supported. Targets: GO:0160292.

All six entity-to-UniProt mappings agree at O395/taxon345073. The canonical example explicitly preserves gene-source scope. The paper uses recombinant tagged enzyme in a strain lacking genomic nqr, so this review does not equate sequence-source taxonomy with preparation host or wild-type state.

### Whole-enzyme substrate/product and sodium coupling

evidence: supported. Targets: GO:0160292.

NADH donation, ubiquinone reduction to ubiquinol, outward sodium transport and contribution to an electrochemical sodium gradient agree with GO, the primary study and UniProt reaction. The source is not used to resolve debated individual cofactor steps.

### All six NONMECHANISTIC FUNCTION edges

graph: supported. Targets: GO:0160292.

Complex enables activity; NADH donates and ubiquinone accepts electrons; activity produces ubiquinol, exports sodium and contributes to sodium motive force. All directions agree at the declared coarse scope. The motive-force edge is correctly rooted in coupled activity after the earlier native correction.

### Primary and secondary citation identity

provenance: supported. Targets: GO:0160292.

The DOI/PMID/PMCID primary study mapping, PDB linkage and Steuber/Fritz2024 review attribution match. The secondary review is cited for bibliographic context; uninspected full secondary text is not used as proof of a detailed mechanism.

### Optional fields and explicit scope

completeness: supported. Targets: GO:0160292.

There are no native images, measured property values, prevalence, trait links or hosted datasets to audit. Empty optional slots do not warrant new findings. Unknown dynamic chemistry remains outside the expressly nonmechanistic graph.

### Native gates and their limits

schema: supported. Targets: GO:0160292.

Fresh target gates and hash-verified wider checks pass within their recorded cache/skip limits. They cannot detect the narrow source-field attribution issue and are not substituted for the source reading.

### Status, history and maintained correction owner

ownership: supported. Targets: GO:0160292.

Both repository histories and all native events were read. Earlier graph correction remains present. No historical review is overwritten or retrospectively declared invalid. Future correction belongs in maintained YAML through the guarded writer with an append-only event; agent status remains PROPOSED.

## Findings

### F1: Correct the NqrF FAD-binding GO attribution

minor / open / confirmed; issue key: sodium-nqr-fad-go-provenance.

The component evidence note states that current IPR010205 GO annotations include FAD binding. The entire live GO list contains GO0016655,GO0051537,GO0006814 andGO0016020, not FAD binding. The family has other FAD-related evidence in its representative-structure title, and both the inspected primary paper and reviewed A5F5Y4 explicitly support the FAD cofactor. This is a narrow inaccurate description of the source field, not a false cofactor role, wrong family, or claim that InterPro has no FAD evidence.

## Recommended Actions And Acceptance Checks

### A1

Revise the NqrF local evidence note to distinguish the actual 2Fe-2S GO annotation from FAD support. Attach the inspected Kishikawa2022 primary evidence directly to the cofactor role, or accurately identify a verified supporting source field. Retain the correct FAD/iron-sulfur role and exact IPR010205 family. Preserve historical wording in append-only history; append a real correction event instead of rewriting it.

- No current evidence note claims an absent InterPro FAD-binding GO annotation.
- Nearest cited source explicitly supports FAD and2Fe-2S in NqrF; the accurate family identity and O395 mapping remain unchanged.
- PROPOSED status preserved; native/repository history appended only when a scientific correction is made.
- Fresh target gates and native QC pass; save a lineage-linked successor with sodium-nqr-fad-go-provenance and this exact occurrence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml; Entire YAML, six components, six graph edges, three native events and both repository histories | supports | The NqrF role states FAD and an iron-sulfur center. Its local InterPro note specifically attributes both FAD binding and 2Fe-2S binding to GO annotations. The prior ADDRESS_REVIEW event records that wording as an earlier correction, not an independently inspected review disposition. |
| rules | .claude/skills/curate-yaml-record/references/review-checklist.md; Evidence standard and components/provenance rubric | supports | The nearest evidence must support the exact assertion, source identity and source version. A narrow source-field misattribution is distinguishable from a false biological role. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160292,GO:0098803; Full active cellular-component definitions and exact synonyms | supports | GO0160292 defines six NqrABCDEF proteins coupling NADH-to-ubiquinone electron transfer to cytoplasm-to-periplasm sodium transport. Both native synonyms are exact. The definition cites PMID38955304. GO0098803 denotes a protein complex in a respiratory chain. |
| go-hierarchy | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160292/ancestors?relations=is_a; Complete current is_a ancestors response | context_only | The current GO is_a graph does not include GO0098803 among this term's ancestors. Native respiratory-chain parentage is instead a curator inference supported by the two definitions and the primary paper, not a verbatim GO edge. |
| nqrf-go | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010205/; Entire standalone payload, especially metadata.go_terms, representative_structure, name/type, description and member models | refutes | The complete four-term GO list contains 2Fe-2S binding but not FAD binding. The same entry does contain FAD-related evidence in its representative-structure title for 4u9u, so the finding is not absence of all FAD support. Name, family type and HAMAP/NCBIfam members identify NqrF, although the prose description inconsistently says E subunit. |
| paper | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9325719/fullTextXML; Main introduction, all Results and Discussion, Methods including expression/purification, figure captions and data availability | supports | Kishikawa et al.2022 directly identify FAD and a 2Fe-2S center in NqrF and support the six-subunit complex, FMN-bearing B/C and membrane D/E. Their enzyme activity and structural analysis support the coarse whole-enzyme reaction. The paper distinguishes flexible NqrF density from loss of the subunit and links state1 to 7XK3/EMD33242. It does not resolve every dynamic electron-transfer step. |
| pdb | https://data.rcsb.org/rest/v1/core/entry/7XK3; Entry title, experimental method/resolution and primary DOI/PMID citation | supports | 7XK3 is state1 of the V.cholerae Na+-NQR cryo-EM study at3.1A, matching DOI10.1038/s41467-022-31718-1 and PMID35882843. Six distinct protein entities are deposited. |
| assembly | https://data.rcsb.org/rest/v1/core/assembly/7XK3/1; Author-defined assembly1 and polymer multiplicities | supports | Assembly1 contains six protein instances with A1B1C1D1E1F1 stoichiometry. Nonpolymer entities and symmetry annotations are not counted as extra subunits. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/345073; Complete taxonomy identity | supports | Taxon345073 is the O395 source identity. Native canonical-example wording is explicitly gene-source sequences, not a claim about the expression host or an unmodified wild-type preparation. |
| citation-primary | https://api.crossref.org/works/10.1038/s41467-022-31718-1; Crossref title/authors/year/DOI, independently cross-checked with EuropePMC PMID/PMCID and article body | supports | Kishikawa et al.2022,Nature Communications,DOI10.1038/s41467-022-31718-1,PMID35882843 and PMC9325719 agree. |
| citation-review | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A38955304+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete abstract and bibliographic metadata/publication type; Crossref title/authors/year also inspected | supports | PMID38955304 is the Steuber/Fritz2024 review of Na+-NQR, DOI10.1016/j.bbabio.2024.149485. Its identity matches the native bibliographic note and GO definition cross-reference. Its abstract is not treated as direct evidence of all proposed mechanistic steps. |
| adapter | https://imodulondb.org/; Fresh complete28-dataset inventory | supports | No V.cholerae dataset is listed. V.natriegens datasets are not interchangeable with O395. Gene/module searches are not applicable; this absence is not negative biological evidence. |
| validation | /private/tmp/csm-review-20261012T104010Z-nqr/baseline-verification.json; Fresh target checks and hash-verified wider-check receipts | supports | Schema, strict and snippet gates pass. Zero of34 citations has a snippet (33 evidence items, one bare reference), so snippet validation is not full-text scientific verification. Reused QC987passed/3skipped, labels603no-adapter skips, cached trait checks, live CURIE4023OK/251SKIP/0unreachable,209valid bundles and4contract tests retain their original times and limits. |
| predecessors | reviews/structured/; Ignored-inclusive canonical and local text searches | supports | No canonical predecessor among209 bundles. Target identifier/label/slug searches in reports/research found only the CURIE report. The new issue key had no match in reviews/reports/research/curation/history; native references to earlier GitHub issues do not create an invented canonical predecessor. |
| family-1 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008703/; Current entry name/type, full description and GO annotations | supports | The entry is the exact NqrA family named by the component. Source annotations are interpreted at their stated scope; obsolete intermediate-reaction models in database prose are not imported into the native coarse graph. |
| entity-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/1; Polymer identity, source taxon, complete SIFTS mapping and EC annotation | supports | Entity1 maps toA5F5X1 at taxon345073 as stated. Its EC7.2.1.1 annotation describes complex activity, not isolated-subunit catalysis. |
| protein-a5f5x1 | https://rest.uniprot.org/uniprotkb/A5F5X1.json; Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor notes and InterPro cross-references | supports | Identity, nqrA gene name and native family mapping agree. All six are reviewed UniProt entries at taxon345073. Functional annotation is not interpreted as a deletion or assembly-essentiality experiment. |
| family-2 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010966/; Current entry name/type, full description and GO annotations | supports | The entry is the exact NqrB family named by the component. Source annotations are interpreted at their stated scope; obsolete intermediate-reaction models in database prose are not imported into the native coarse graph. |
| entity-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/2; Polymer identity, source taxon, complete SIFTS mapping and EC annotation | supports | Entity2 maps toA5F5X0 at taxon345073 as stated. Its EC7.2.1.1 annotation describes complex activity, not isolated-subunit catalysis. |
| protein-a5f5x0 | https://rest.uniprot.org/uniprotkb/A5F5X0.json; Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor notes and InterPro cross-references | supports | Identity, nqrB gene name and native family mapping agree. All six are reviewed UniProt entries at taxon345073. Functional annotation is not interpreted as a deletion or assembly-essentiality experiment. |
| family-3 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010204/; Current entry name/type, full description and GO annotations | supports | The entry is the exact NqrC family named by the component. Source annotations are interpreted at their stated scope; obsolete intermediate-reaction models in database prose are not imported into the native coarse graph. |
| entity-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/3; Polymer identity, source taxon, complete SIFTS mapping and EC annotation | supports | Entity3 maps toA5F5Y7 at taxon345073 as stated. Its EC7.2.1.1 annotation describes complex activity, not isolated-subunit catalysis. |
| protein-a5f5y7 | https://rest.uniprot.org/uniprotkb/A5F5Y7.json; Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor notes and InterPro cross-references | supports | Identity, nqrC gene name and native family mapping agree. All six are reviewed UniProt entries at taxon345073. Functional annotation is not interpreted as a deletion or assembly-essentiality experiment. |
| family-4 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011292/; Current entry name/type, full description and GO annotations | supports | The entry is the exact NqrD family named by the component. Source annotations are interpreted at their stated scope; obsolete intermediate-reaction models in database prose are not imported into the native coarse graph. |
| entity-4 | https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/4; Polymer identity, source taxon, complete SIFTS mapping and EC annotation | supports | Entity4 maps toA5F5Y6 at taxon345073 as stated. Its EC7.2.1.1 annotation describes complex activity, not isolated-subunit catalysis. |
| protein-a5f5y6 | https://rest.uniprot.org/uniprotkb/A5F5Y6.json; Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor notes and InterPro cross-references | supports | Identity, nqrD gene name and native family mapping agree. All six are reviewed UniProt entries at taxon345073. Functional annotation is not interpreted as a deletion or assembly-essentiality experiment. |
| family-5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010967/; Current entry name/type, full description and GO annotations | supports | The entry is the exact NqrE family named by the component. Source annotations are interpreted at their stated scope; obsolete intermediate-reaction models in database prose are not imported into the native coarse graph. |
| entity-5 | https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/5; Polymer identity, source taxon, complete SIFTS mapping and EC annotation | supports | Entity5 maps toA5F5Y5 at taxon345073 as stated. Its EC7.2.1.1 annotation describes complex activity, not isolated-subunit catalysis. |
| protein-a5f5y5 | https://rest.uniprot.org/uniprotkb/A5F5Y5.json; Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor notes and InterPro cross-references | supports | Identity, nqrE gene name and native family mapping agree. All six are reviewed UniProt entries at taxon345073. Functional annotation is not interpreted as a deletion or assembly-essentiality experiment. |
| family-6 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010205/; Current entry name/type, full description and GO annotations | supports | The entry is the exact NqrF family named by the component. Source annotations are interpreted at their stated scope; obsolete intermediate-reaction models in database prose are not imported into the native coarse graph. |
| entity-6 | https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/6; Polymer identity, source taxon, complete SIFTS mapping and EC annotation | supports | Entity6 maps toA5F5Y4 at taxon345073 as stated. Its EC7.2.1.1 annotation describes complex activity, not isolated-subunit catalysis. |
| protein-a5f5y4 | https://rest.uniprot.org/uniprotkb/A5F5Y4.json; Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor notes and InterPro cross-references | supports | Identity, nqrF gene name and native family mapping agree. All six are reviewed UniProt entries at taxon345073. NqrF specifically has separate FAD and2Fe-2S cofactor annotations, supporting the role despite the local InterPro GO misattribution. |

## Limits And Additional Notes

- Same-agent review, not independent human sign-off or exhaustive literature/retraction surveillance.
- Primary main text, relevant methods/results/discussion and captions were inspected as full-text XML. Figure pixels, supplementary files, raw EM maps and coordinates were not reanalyzed. No native image or numerical measurement depends on such reanalysis.
- The2024 secondary review was checked through its complete abstract and bibliographic metadata, not its full body. It supplies only native bibliographic/GO-reference context here; primary text and structured sources support material scientific claims.
- InterPro IPR010205 has an inconsistent E-subunit description despite NqrF identity/name/member models. This upstream inconsistency is preserved as context, not propagated or treated as native wrong-family identity. Current absence of FAD in its GO list is not evidence it was absent on the historical curation date.
- Native respiratory-chain parentage is supported curator inference, not an edge present in the inspected current GO is_a hierarchy. ESSENTIAL is interpreted at complete-core structure scope, not as a viability or deletion claim.
- Fresh target gates and28successful public-source captures; wider gates reused only after unchanged-byte verification with original skips/cache limits. This is not fresh CI. No V.cholerae iModulonDB dataset matched.
- No scientific YAML, status, history, generated product or prior review changed. No GitHub mutation, push, issue, PR or merge; previous external-publication approval remains unanswered.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T104624Z-sodium-nqr-fad-provenance
kind: record
repository: CultureBotAI/CellStructureMech
title: Na+-NQR cofactor evidence provenance review
started_at: '2026-10-12T10:40:38Z'
finished_at: '2026-10-12T10:46:24Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same coding-agent context; no independent reviewer or human
    sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Whole-record review completed with one minor finding: NqrF FAD support is
  incorrectly attributed to a current InterPro GO annotation. Six family identities,
  source-strain mappings, complete-core composition, whole-enzyme function and six
  coarse graph edges are otherwise supported within the stated limits.'
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
  - path: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
    sha256: bed96d5d9cae4915ec18db7966eb64db2baf32c027ff85363cece039bb3ca21f
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
  - path: history/records/sodium_translocating_nadh_quinone_reductase_complex/2026-09-24T074303Z-codex-84d8bf.yaml
    sha256: cfd026711ecbdedbe27be25911d21a1e7467f0edd6c5318ff80d596c2d53a05c
    role: context
  - path: history/records/sodium_translocating_nadh_quinone_reductase_complex/2026-09-24T075617Z-codex-1ee4b7.yaml
    sha256: a8b6df1fe1ddd5f41cf824b445480c9d391ebad43ffc6cce8e6ec8bb1cef4d13
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
- target_id: GO:0160292
  path: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
  label: sodium-translocating NADH:quinone reductase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
    role: maintained scientific record
scope:
  description: One complete native record and both histories; all material claims,
    six component families/entity mappings, six graph edges and all native stable
    identifiers assessed. No sampling.
  selection: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0160292
checks:
- check_id: schema
  name: schema
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate. Actual UTC: 2026-10-12T10:40:55Z to 2026-10-12T10:40:57Z.'
  target_ids:
  - GO:0160292
  evidence_ids:
  - validation
- check_id: strict
  name: strict
  command: .venv/bin/python scripts/validate_strict.py data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate. Actual UTC: 2026-10-12T10:40:57Z to 2026-10-12T10:41:00Z.'
  target_ids:
  - GO:0160292
  evidence_ids:
  - validation
- check_id: snippets
  name: snippets
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
    --report /private/tmp/csm-review-20261012T104010Z-nqr/snippets.md
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate; zero of34 citations has a snippet, not automated full-text
    proof. Actual UTC: 2026-10-12T10:41:00Z to 2026-10-12T10:41:17Z.'
  target_ids:
  - GO:0160292
  evidence_ids:
  - validation
- check_id: reused-release-qc
  name: reused-release-qc
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  status: passed
  required: true
  summary: 'Original result reused after input/receipt hash checks. QC987passed/3skipped,
    labels603no-adapter skips, cached traits after earlier network failure. Not fresh
    CI. Actual UTC: 2026-10-12T06:33:07Z to 2026-10-12T06:45:16Z.'
  target_ids:
  - GO:0160292
  evidence_ids:
  - validation
- check_id: reused-release-labels
  name: reused-release-labels
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Original result reused after input/receipt hash checks. QC987passed/3skipped,
    labels603no-adapter skips, cached traits after earlier network failure. Not fresh
    CI. Actual UTC: 2026-10-12T06:45:16Z to 2026-10-12T06:47:16Z.'
  target_ids:
  - GO:0160292
  evidence_ids:
  - validation
- check_id: reused-release-traits
  name: reused-release-traits
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  status: passed
  required: true
  summary: 'Original result reused after input/receipt hash checks. QC987passed/3skipped,
    labels603no-adapter skips, cached traits after earlier network failure. Not fresh
    CI. Actual UTC: 2026-10-12T06:48:15Z to 2026-10-12T06:48:52Z.'
  target_ids:
  - GO:0160292
  evidence_ids:
  - validation
- check_id: reused-curies-live
  name: reused-curies-live
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  status: passed
  required: true
  summary: 'Original result reused on unchanged bytes. Live CURIE4023OK/251SKIP/0unreachable;209valid
    bundles and4contract tests. New post-save archive/contract checks follow separately.
    Actual UTC: 2026-10-12T07:05:41Z to 2026-10-12T07:10:58Z.'
  target_ids:
  - GO:0160292
  evidence_ids:
  - validation
- check_id: reused-post-save-archive
  name: reused-post-save-archive
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  status: passed
  required: true
  summary: 'Original result reused on unchanged bytes. Live CURIE4023OK/251SKIP/0unreachable;209valid
    bundles and4contract tests. New post-save archive/contract checks follow separately.
    Actual UTC: 2026-10-12T10:37:07Z to 2026-10-12T10:38:34Z.'
  target_ids:
  - GO:0160292
  evidence_ids:
  - validation
- check_id: reused-post-save-contract
  name: reused-post-save-contract
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  status: passed
  required: true
  summary: 'Original result reused on unchanged bytes. Live CURIE4023OK/251SKIP/0unreachable;209valid
    bundles and4contract tests. New post-save archive/contract checks follow separately.
    Actual UTC: 2026-10-12T10:38:34Z to 2026-10-12T10:40:04Z.'
  target_ids:
  - GO:0160292
  evidence_ids:
  - validation
- check_id: adapter-datasets
  name: adapter-datasets
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh full inventory; no matching V.cholerae dataset. Actual UTC: 2026-10-12T10:40:50Z
    to 2026-10-12T10:40:51Z.'
  target_ids:
  - GO:0160292
  evidence_ids:
  - adapter
evidence:
- evidence_id: native
  kind: record_content
  reference: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
  locator: Entire YAML, six components, six graph edges, three native events and both
    repository histories
  summary: The NqrF role states FAD and an iron-sulfur center. Its local InterPro
    note specifically attributes both FAD binding and 2Fe-2S binding to GO annotations.
    The prior ADDRESS_REVIEW event records that wording as an earlier correction,
    not an independently inspected review disposition.
  support: supports
  accessed_at: '2026-10-12T10:46:24Z'
  snapshot_sha256: bed96d5d9cae4915ec18db7966eb64db2baf32c027ff85363cece039bb3ca21f
- evidence_id: rules
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Evidence standard and components/provenance rubric
  summary: The nearest evidence must support the exact assertion, source identity
    and source version. A narrow source-field misattribution is distinguishable from
    a false biological role.
  support: supports
  accessed_at: '2026-10-12T10:46:24Z'
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160292,GO:0098803
  locator: Full active cellular-component definitions and exact synonyms
  summary: GO0160292 defines six NqrABCDEF proteins coupling NADH-to-ubiquinone electron
    transfer to cytoplasm-to-periplasm sodium transport. Both native synonyms are
    exact. The definition cites PMID38955304. GO0098803 denotes a protein complex
    in a respiratory chain.
  support: supports
  accessed_at: '2026-10-12T10:40:54Z'
  snapshot_sha256: 485c9e1437099dd58b0acd3b23a215f2ef265544f6a72a550263dc655080d195
- evidence_id: go-hierarchy
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160292/ancestors?relations=is_a
  locator: Complete current is_a ancestors response
  summary: The current GO is_a graph does not include GO0098803 among this term's
    ancestors. Native respiratory-chain parentage is instead a curator inference supported
    by the two definitions and the primary paper, not a verbatim GO edge.
  support: context_only
  accessed_at: '2026-10-12T10:41:25Z'
  snapshot_sha256: 07d817f391b96763079d89fd1b660503cd890b73a04c2c794a3554a9b1cafcc1
- evidence_id: nqrf-go
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010205/
  locator: Entire standalone payload, especially metadata.go_terms, representative_structure,
    name/type, description and member models
  summary: The complete four-term GO list contains 2Fe-2S binding but not FAD binding.
    The same entry does contain FAD-related evidence in its representative-structure
    title for 4u9u, so the finding is not absence of all FAD support. Name, family
    type and HAMAP/NCBIfam members identify NqrF, although the prose description inconsistently
    says E subunit.
  support: refutes
  accessed_at: '2026-10-12T10:41:01Z'
  snapshot_sha256: fdd59ad47dbb2c4097ac9b60cd0be15137111cdfc588d8dbf112105ad17e64c9
- evidence_id: paper
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9325719/fullTextXML
  locator: Main introduction, all Results and Discussion, Methods including expression/purification,
    figure captions and data availability
  summary: Kishikawa et al.2022 directly identify FAD and a 2Fe-2S center in NqrF
    and support the six-subunit complex, FMN-bearing B/C and membrane D/E. Their enzyme
    activity and structural analysis support the coarse whole-enzyme reaction. The
    paper distinguishes flexible NqrF density from loss of the subunit and links state1
    to 7XK3/EMD33242. It does not resolve every dynamic electron-transfer step.
  support: supports
  accessed_at: '2026-10-12T10:41:24Z'
  snapshot_sha256: 80a348c98b02eca50a2bf84e5c98c552a867a442ccd022c872168acf22b96d60
- evidence_id: pdb
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/7XK3
  locator: Entry title, experimental method/resolution and primary DOI/PMID citation
  summary: 7XK3 is state1 of the V.cholerae Na+-NQR cryo-EM study at3.1A, matching
    DOI10.1038/s41467-022-31718-1 and PMID35882843. Six distinct protein entities
    are deposited.
  support: supports
  accessed_at: '2026-10-12T10:40:57Z'
  snapshot_sha256: 68191918494f6b86edb5e8a6c33ed125772229f71d9cda243e896a8326190ffc
- evidence_id: assembly
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/7XK3/1
  locator: Author-defined assembly1 and polymer multiplicities
  summary: Assembly1 contains six protein instances with A1B1C1D1E1F1 stoichiometry.
    Nonpolymer entities and symmetry annotations are not counted as extra subunits.
  support: supports
  accessed_at: '2026-10-12T10:40:57Z'
  snapshot_sha256: 02d8d84d317d1ac0ac77f27630d3ca1bb72564781cf8d1de3aca880eb9eb90ca
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/345073
  locator: Complete taxonomy identity
  summary: Taxon345073 is the O395 source identity. Native canonical-example wording
    is explicitly gene-source sequences, not a claim about the expression host or
    an unmodified wild-type preparation.
  support: supports
  accessed_at: '2026-10-12T10:40:55Z'
  snapshot_sha256: b1655ff162ce020019d8fa9a116bbf7cde87ce6e563f8fd02086a7670a5f8435
- evidence_id: citation-primary
  kind: authority
  reference: https://api.crossref.org/works/10.1038/s41467-022-31718-1
  locator: Crossref title/authors/year/DOI, independently cross-checked with EuropePMC
    PMID/PMCID and article body
  summary: Kishikawa et al.2022,Nature Communications,DOI10.1038/s41467-022-31718-1,PMID35882843
    and PMC9325719 agree.
  support: supports
  accessed_at: '2026-10-12T10:40:57Z'
  snapshot_sha256: b70327ad0a001e6bf95876eef5f7de0d439a94313c7f3acde261c0a0fee5e7f9
- evidence_id: citation-review
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A38955304+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete abstract and bibliographic metadata/publication type; Crossref
    title/authors/year also inspected
  summary: PMID38955304 is the Steuber/Fritz2024 review of Na+-NQR, DOI10.1016/j.bbabio.2024.149485.
    Its identity matches the native bibliographic note and GO definition cross-reference.
    Its abstract is not treated as direct evidence of all proposed mechanistic steps.
  support: supports
  accessed_at: '2026-10-12T10:40:56Z'
  snapshot_sha256: c2647c8651dc255662a4961ce23fb205de7e7bf70a3c80daf61024bd999b6bea
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/
  locator: Fresh complete28-dataset inventory
  summary: No V.cholerae dataset is listed. V.natriegens datasets are not interchangeable
    with O395. Gene/module searches are not applicable; this absence is not negative
    biological evidence.
  support: supports
  accessed_at: '2026-10-12T10:46:24Z'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/csm-review-20261012T104010Z-nqr/baseline-verification.json
  locator: Fresh target checks and hash-verified wider-check receipts
  summary: Schema, strict and snippet gates pass. Zero of34 citations has a snippet
    (33 evidence items, one bare reference), so snippet validation is not full-text
    scientific verification. Reused QC987passed/3skipped, labels603no-adapter skips,
    cached trait checks, live CURIE4023OK/251SKIP/0unreachable,209valid bundles and4contract
    tests retain their original times and limits.
  support: supports
  accessed_at: '2026-10-12T10:46:24Z'
- evidence_id: predecessors
  kind: search
  reference: reviews/structured/
  locator: Ignored-inclusive canonical and local text searches
  summary: No canonical predecessor among209 bundles. Target identifier/label/slug
    searches in reports/research found only the CURIE report. The new issue key had
    no match in reviews/reports/research/curation/history; native references to earlier
    GitHub issues do not create an invented canonical predecessor.
  support: supports
  accessed_at: '2026-10-12T10:46:24Z'
  search_scope: Path.rglob includes ignored/hidden canonical reviews and histories;
    rg --no-ignore --hidden searched reports/research for target identity and reviews/reports/research/curation/history
    for sodium-nqr-fad-go-provenance. Bounded local search, not GitHub-wide absence.
- evidence_id: family-1
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008703/
  locator: Current entry name/type, full description and GO annotations
  summary: The entry is the exact NqrA family named by the component. Source annotations
    are interpreted at their stated scope; obsolete intermediate-reaction models in
    database prose are not imported into the native coarse graph.
  support: supports
  accessed_at: '2026-10-12T10:40:58Z'
  snapshot_sha256: 7badf1af8ca3ad18430bda12ed084838521fa3f0cc17e2a3e4ae2e9b3fb79231
- evidence_id: entity-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/1
  locator: Polymer identity, source taxon, complete SIFTS mapping and EC annotation
  summary: Entity1 maps toA5F5X1 at taxon345073 as stated. Its EC7.2.1.1 annotation
    describes complex activity, not isolated-subunit catalysis.
  support: supports
  accessed_at: '2026-10-12T10:41:01Z'
  snapshot_sha256: afc6a66310c93c994e7166b6f8febf696f2c2349326a463d23bd549d2eb4b570
- evidence_id: protein-a5f5x1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A5F5X1.json
  locator: Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor
    notes and InterPro cross-references
  summary: Identity, nqrA gene name and native family mapping agree. All six are reviewed
    UniProt entries at taxon345073. Functional annotation is not interpreted as a
    deletion or assembly-essentiality experiment.
  support: supports
  accessed_at: '2026-10-12T10:41:03Z'
  snapshot_sha256: dbdc1bf60ae0643d0e864972215c881eadf82ba1c90c96112e0476327d92661d
- evidence_id: family-2
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010966/
  locator: Current entry name/type, full description and GO annotations
  summary: The entry is the exact NqrB family named by the component. Source annotations
    are interpreted at their stated scope; obsolete intermediate-reaction models in
    database prose are not imported into the native coarse graph.
  support: supports
  accessed_at: '2026-10-12T10:40:58Z'
  snapshot_sha256: b54455ae6234f1d5e280e37b7272dc89049c6e19a954d5c2c02cde0b815529f2
- evidence_id: entity-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/2
  locator: Polymer identity, source taxon, complete SIFTS mapping and EC annotation
  summary: Entity2 maps toA5F5X0 at taxon345073 as stated. Its EC7.2.1.1 annotation
    describes complex activity, not isolated-subunit catalysis.
  support: supports
  accessed_at: '2026-10-12T10:41:01Z'
  snapshot_sha256: b2dfe53d2e2ed99719baecb15941ec1a34d0a89685800cab0504966c5ff4f390
- evidence_id: protein-a5f5x0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A5F5X0.json
  locator: Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor
    notes and InterPro cross-references
  summary: Identity, nqrB gene name and native family mapping agree. All six are reviewed
    UniProt entries at taxon345073. Functional annotation is not interpreted as a
    deletion or assembly-essentiality experiment.
  support: supports
  accessed_at: '2026-10-12T10:41:04Z'
  snapshot_sha256: dc676e463540bb961a64666aaf3a88819b3f240d505d14dcfad5177e9475e495
- evidence_id: family-3
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010204/
  locator: Current entry name/type, full description and GO annotations
  summary: The entry is the exact NqrC family named by the component. Source annotations
    are interpreted at their stated scope; obsolete intermediate-reaction models in
    database prose are not imported into the native coarse graph.
  support: supports
  accessed_at: '2026-10-12T10:40:59Z'
  snapshot_sha256: 605d96453f1d9e41115299ec2aad186e0b48264714d134daefec408be9cc468d
- evidence_id: entity-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/3
  locator: Polymer identity, source taxon, complete SIFTS mapping and EC annotation
  summary: Entity3 maps toA5F5Y7 at taxon345073 as stated. Its EC7.2.1.1 annotation
    describes complex activity, not isolated-subunit catalysis.
  support: supports
  accessed_at: '2026-10-12T10:41:01Z'
  snapshot_sha256: 46bb069b9cf94a0490e84b79ca2428ab81a87f7a8044f3a48646fd41fb9df623
- evidence_id: protein-a5f5y7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A5F5Y7.json
  locator: Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor
    notes and InterPro cross-references
  summary: Identity, nqrC gene name and native family mapping agree. All six are reviewed
    UniProt entries at taxon345073. Functional annotation is not interpreted as a
    deletion or assembly-essentiality experiment.
  support: supports
  accessed_at: '2026-10-12T10:41:04Z'
  snapshot_sha256: dddf88658b6277ae5d36c5d2c427710aef356ee9c86dfb2b44d31d53c4a1dad7
- evidence_id: family-4
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011292/
  locator: Current entry name/type, full description and GO annotations
  summary: The entry is the exact NqrD family named by the component. Source annotations
    are interpreted at their stated scope; obsolete intermediate-reaction models in
    database prose are not imported into the native coarse graph.
  support: supports
  accessed_at: '2026-10-12T10:41:00Z'
  snapshot_sha256: a2d23ad70a46252c085829254e0c42dfe497b3b3e037250d1d2a5a5b7b28b9bc
- evidence_id: entity-4
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/4
  locator: Polymer identity, source taxon, complete SIFTS mapping and EC annotation
  summary: Entity4 maps toA5F5Y6 at taxon345073 as stated. Its EC7.2.1.1 annotation
    describes complex activity, not isolated-subunit catalysis.
  support: supports
  accessed_at: '2026-10-12T10:41:02Z'
  snapshot_sha256: eca872c6b4d9b549fe6126aa1c9eb35cc2cf5435089d6d3baaf380ac65417d45
- evidence_id: protein-a5f5y6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A5F5Y6.json
  locator: Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor
    notes and InterPro cross-references
  summary: Identity, nqrD gene name and native family mapping agree. All six are reviewed
    UniProt entries at taxon345073. Functional annotation is not interpreted as a
    deletion or assembly-essentiality experiment.
  support: supports
  accessed_at: '2026-10-12T10:41:05Z'
  snapshot_sha256: 6f3f9b0ec0ae6e519312baf34a9173d6eb0e9ea6b43b1314991c036d50e6763b
- evidence_id: family-5
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010967/
  locator: Current entry name/type, full description and GO annotations
  summary: The entry is the exact NqrE family named by the component. Source annotations
    are interpreted at their stated scope; obsolete intermediate-reaction models in
    database prose are not imported into the native coarse graph.
  support: supports
  accessed_at: '2026-10-12T10:41:00Z'
  snapshot_sha256: c2ef3b6b658ff0518ec09f055b216e9c3ddfaf4edd9d19b8568d227fc0b32849
- evidence_id: entity-5
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/5
  locator: Polymer identity, source taxon, complete SIFTS mapping and EC annotation
  summary: Entity5 maps toA5F5Y5 at taxon345073 as stated. Its EC7.2.1.1 annotation
    describes complex activity, not isolated-subunit catalysis.
  support: supports
  accessed_at: '2026-10-12T10:41:02Z'
  snapshot_sha256: 1553b4dbaed8cde432d438d20360ef24750dd4f1c9e544f1c9110573c6beedcd
- evidence_id: protein-a5f5y5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A5F5Y5.json
  locator: Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor
    notes and InterPro cross-references
  summary: Identity, nqrE gene name and native family mapping agree. All six are reviewed
    UniProt entries at taxon345073. Functional annotation is not interpreted as a
    deletion or assembly-essentiality experiment.
  support: supports
  accessed_at: '2026-10-12T10:41:06Z'
  snapshot_sha256: b2eb177b26cc292c89b4412e4b9aa6a491033f434b519b9e881c8ebc0f9015f8
- evidence_id: family-6
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010205/
  locator: Current entry name/type, full description and GO annotations
  summary: The entry is the exact NqrF family named by the component. Source annotations
    are interpreted at their stated scope; obsolete intermediate-reaction models in
    database prose are not imported into the native coarse graph.
  support: supports
  accessed_at: '2026-10-12T10:41:01Z'
  snapshot_sha256: fdd59ad47dbb2c4097ac9b60cd0be15137111cdfc588d8dbf112105ad17e64c9
- evidence_id: entity-6
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7XK3/6
  locator: Polymer identity, source taxon, complete SIFTS mapping and EC annotation
  summary: Entity6 maps toA5F5Y4 at taxon345073 as stated. Its EC7.2.1.1 annotation
    describes complex activity, not isolated-subunit catalysis.
  support: supports
  accessed_at: '2026-10-12T10:41:02Z'
  snapshot_sha256: 1c6dafa2d5d0b6a5575c91ba006f2f6502b44b794f2568e179bccf2b4ed27f57
- evidence_id: protein-a5f5y4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A5F5Y4.json
  locator: Reviewed identity, organism, gene/locus aliases, function/subunit/location/cofactor
    notes and InterPro cross-references
  summary: Identity, nqrF gene name and native family mapping agree. All six are reviewed
    UniProt entries at taxon345073. NqrF specifically has separate FAD and2Fe-2S cofactor
    annotations, supporting the role despite the local InterPro GO misattribution.
  support: supports
  accessed_at: '2026-10-12T10:41:06Z'
  snapshot_sha256: 84626390b25e30b0303a677c3f0a985568878fec82988cfafd8fcd5e1bb13808
assessments:
- assessment_id: identity
  area: identity
  topic: Na+-NQR identity, definition, synonyms and inferred parentage
  outcome: supported
  summary: The native record denotes the six-subunit sodium-translocating NADH:quinone
    complex, not proton-pumping complexI. Respiratory-chain parentage follows the
    source definitions and primary evidence; it is not currently an explicit GO is_a
    edge.
  target_ids:
  - GO:0160292
  evidence_ids:
  - native
  - go
  - go-hierarchy
  - paper
- assessment_id: grounding
  area: grounding
  topic: Six exact component families
  outcome: supported
  summary: All six supplied InterPro accessions are current family entries for the
    respective Nqr subunit and are cross-referenced by the deposited source proteins.
    The inconsistent E wording in the NqrF description does not override its concordant
    family identity and member models.
  target_ids:
  - GO:0160292
  evidence_ids:
  - family-1
  - family-2
  - family-3
  - family-4
  - family-5
  - family-6
  - nqrf-go
  - protein-a5f5y4
- assessment_id: composition
  area: quantity
  topic: Six-subunit composition and constituent roles
  outcome: supported
  summary: The GO definition, primary paper and author-defined assembly support the
    NqrA-F complete core. ESSENTIAL is read as membership required for that defined
    complete structure, not cell viability or an assertion that no incomplete subassembly
    can persist. No native deletion experiment or universal kinetic stoichiometry
    is asserted. NqrB/C FMN roles, D/E membrane roles and NqrF cofactors agree with
    inspected sources.
  target_ids:
  - GO:0160292
  evidence_ids:
  - go
  - paper
  - assembly
  - entity-1
  - entity-2
  - entity-3
  - entity-4
  - entity-5
  - entity-6
- assessment_id: provenance
  area: provenance
  topic: NqrF cofactor source-field attribution
  outcome: concern
  summary: NqrF really carries FAD and2Fe-2S, but the evidence note incorrectly describes
    FAD binding as one of the current IPR010205 GO annotations. Restrict the correction
    to exact source attribution; do not remove the valid FAD role or change the family
    grounding.
  target_ids:
  - GO:0160292
  evidence_ids:
  - native
  - nqrf-go
  - paper
  - protein-a5f5y4
  - rules
- assessment_id: taxon
  area: scope
  topic: O395 sequence source and source-protein mapping
  outcome: supported
  summary: All six entity-to-UniProt mappings agree at O395/taxon345073. The canonical
    example explicitly preserves gene-source scope. The paper uses recombinant tagged
    enzyme in a strain lacking genomic nqr, so this review does not equate sequence-source
    taxonomy with preparation host or wild-type state.
  target_ids:
  - GO:0160292
  evidence_ids:
  - taxon
  - paper
  - pdb
  - entity-1
  - entity-2
  - entity-3
  - entity-4
  - entity-5
  - entity-6
- assessment_id: function
  area: evidence
  topic: Whole-enzyme substrate/product and sodium coupling
  outcome: supported
  summary: NADH donation, ubiquinone reduction to ubiquinol, outward sodium transport
    and contribution to an electrochemical sodium gradient agree with GO, the primary
    study and UniProt reaction. The source is not used to resolve debated individual
    cofactor steps.
  target_ids:
  - GO:0160292
  evidence_ids:
  - go
  - paper
  - protein-a5f5y4
- assessment_id: graph
  area: graph
  topic: All six NONMECHANISTIC FUNCTION edges
  outcome: supported
  summary: Complex enables activity; NADH donates and ubiquinone accepts electrons;
    activity produces ubiquinol, exports sodium and contributes to sodium motive force.
    All directions agree at the declared coarse scope. The motive-force edge is correctly
    rooted in coupled activity after the earlier native correction.
  target_ids:
  - GO:0160292
  evidence_ids:
  - native
  - go
  - paper
  - protein-a5f5y4
- assessment_id: citations
  area: provenance
  topic: Primary and secondary citation identity
  outcome: supported
  summary: The DOI/PMID/PMCID primary study mapping, PDB linkage and Steuber/Fritz2024
    review attribution match. The secondary review is cited for bibliographic context;
    uninspected full secondary text is not used as proof of a detailed mechanism.
  target_ids:
  - GO:0160292
  evidence_ids:
  - pdb
  - citation-primary
  - citation-review
  - go
- assessment_id: completeness
  area: completeness
  topic: Optional fields and explicit scope
  outcome: supported
  summary: There are no native images, measured property values, prevalence, trait
    links or hosted datasets to audit. Empty optional slots do not warrant new findings.
    Unknown dynamic chemistry remains outside the expressly nonmechanistic graph.
  target_ids:
  - GO:0160292
  evidence_ids:
  - native
  - paper
  - adapter
- assessment_id: checks
  area: schema
  topic: Native gates and their limits
  outcome: supported
  summary: Fresh target gates and hash-verified wider checks pass within their recorded
    cache/skip limits. They cannot detect the narrow source-field attribution issue
    and are not substituted for the source reading.
  target_ids:
  - GO:0160292
  evidence_ids:
  - validation
  - nqrf-go
- assessment_id: ownership
  area: ownership
  topic: Status, history and maintained correction owner
  outcome: supported
  summary: Both repository histories and all native events were read. Earlier graph
    correction remains present. No historical review is overwritten or retrospectively
    declared invalid. Future correction belongs in maintained YAML through the guarded
    writer with an append-only event; agent status remains PROPOSED.
  target_ids:
  - GO:0160292
  evidence_ids:
  - native
  - predecessors
  - rules
findings:
- finding_id: F1
  issue_key: sodium-nqr-fad-go-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the NqrF FAD-binding GO attribution
  description: The component evidence note states that current IPR010205 GO annotations
    include FAD binding. The entire live GO list contains GO0016655,GO0051537,GO0006814
    andGO0016020, not FAD binding. The family has other FAD-related evidence in its
    representative-structure title, and both the inspected primary paper and reviewed
    A5F5Y4 explicitly support the FAD cofactor. This is a narrow inaccurate description
    of the source field, not a false cofactor role, wrong family, or claim that InterPro
    has no FAD evidence.
  target_ids:
  - GO:0160292
  field_paths:
  - components[component_id=nqrF_subunit].evidence[reference=InterPro:IPR010205].notes
  evidence_ids:
  - native
  - nqrf-go
  - paper
  - protein-a5f5y4
  - rules
  rule_id: review-checklist:evidence-standard
  native_severity: minor
  normalization_reason: Non-blocking provenance wording is incorrect while the exact
    protein-family identity and biological cofactor role have independent inspected
    support.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Revise the NqrF local evidence note to distinguish the actual 2Fe-2S
    GO annotation from FAD support. Attach the inspected Kishikawa2022 primary evidence
    directly to the cofactor role, or accurately identify a verified supporting source
    field. Retain the correct FAD/iron-sulfur role and exact IPR010205 family. Preserve
    historical wording in append-only history; append a real correction event instead
    of rewriting it.
  finding_ids:
  - F1
  target_ids:
  - GO:0160292
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
    role: maintained scientific record
  generator: Guarded native writer and documented product workflow for a separately
    authorized correction.
  acceptance_checks:
  - No current evidence note claims an absent InterPro FAD-binding GO annotation.
  - Nearest cited source explicitly supports FAD and2Fe-2S in NqrF; the accurate family
    identity and O395 mapping remain unchanged.
  - PROPOSED status preserved; native/repository history appended only when a scientific
    correction is made.
  - Fresh target gates and native QC pass; save a lineage-linked successor with sodium-nqr-fad-go-provenance
    and this exact occurrence.
limitations:
- Same-agent review, not independent human sign-off or exhaustive literature/retraction
  surveillance.
- Primary main text, relevant methods/results/discussion and captions were inspected
  as full-text XML. Figure pixels, supplementary files, raw EM maps and coordinates
  were not reanalyzed. No native image or numerical measurement depends on such reanalysis.
- The2024 secondary review was checked through its complete abstract and bibliographic
  metadata, not its full body. It supplies only native bibliographic/GO-reference
  context here; primary text and structured sources support material scientific claims.
- InterPro IPR010205 has an inconsistent E-subunit description despite NqrF identity/name/member
  models. This upstream inconsistency is preserved as context, not propagated or treated
  as native wrong-family identity. Current absence of FAD in its GO list is not evidence
  it was absent on the historical curation date.
- Native respiratory-chain parentage is supported curator inference, not an edge present
  in the inspected current GO is_a hierarchy. ESSENTIAL is interpreted at complete-core
  structure scope, not as a viability or deletion claim.
- Fresh target gates and28successful public-source captures; wider gates reused only
  after unchanged-byte verification with original skips/cache limits. This is not
  fresh CI. No V.cholerae iModulonDB dataset matched.
- No scientific YAML, status, history, generated product or prior review changed.
  No GitHub mutation, push, issue, PR or merge; previous external-publication approval
  remains unanswered.
tags:
- scientific-review
- energy-complex
- provenance
```
