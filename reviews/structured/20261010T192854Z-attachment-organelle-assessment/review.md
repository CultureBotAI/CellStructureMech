# Attachment organelle: scientific assessment

- Review: 20261010T192854Z-attachment-organelle-assessment
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T17:29:03Z
- Finished UTC: 2026-10-10T19:28:54Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Claim-by-claim assessment completed for this one record. Current NCBI taxon scope requires correction. P30 assembly essentiality also requires correction.

## Scope And Provenance

Entire maintained record, present material claims and both history surfaces; optional missing fields are not findings.

Selection: Exact path data/structures/appendage/attachment_organelle.yaml; not a corpus sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 478edc23b61f8ea6be66c5b86df04040be08fbdb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033099 | data/structures/appendage/attachment_organelle.yaml | maintained | attachment organelle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Fresh focused schema | passed | True | GO:0033099 | Passed before curation. |
| Fresh focused strict | passed | True | GO:0033099 | Passed before curation. |
| Exact-revision full-corpus gates | passed | True | GO:0033099 | Verified success at unchanged HEAD for Build and test (38043028532), label correspondence (38043028531), identifier/trait checks (38043028562), vendored sync (38043028526), and merge integrity (38043028544). |

## Scientific And Domain Assessments

### Structure identity, category, kind and mereology

identity: supported. Targets: GO:0033099.

Exact GO structure identity, not a protein or phenotype. Membrane is-a/parthood and whole-organelle cell-projection parent/membrane-part boundaries are sound; PROPOSED retained.

### Taxonomic distribution and canonical example

scope: concern. Targets: GO:0033099.

The M129 example and restricted bacterial occurrence are supported, but historical Mollicutes wording has been attached to current NCBITaxon:31969, outside the example lineage. Use the verified encompassing phylum with explicit literature scope, not an asserted taxon synonym or universal presence.

### All five components and essentiality

evidence: concern. Targets: GO:0033099.

P1/P40/P90 surface membership and corrected DISPENSABLE value, HMW2 parallel scaffold/length setting and ESSENTIAL value, P65 terminal button and HMW3 boundary are supported in M. pneumoniae. P30 front localization and adhesion/shape roles are supported, but ESSENTIAL conflates assembly and function. No numeric stoichiometry is asserted; parallel alignment is architectural free text.

### Three taxon-paired protein examples

evidence: supported. Targets: GO:0033099.

Reviewed accessions, protein labels, genes/loci and M129 taxon match UniProt. PMID 15466048 supports P65/HMW2 tagging and PMID 26633540 supports all three mapped examples; notes correctly attribute ECO annotations to UniProt.

### Synonym, two functions and all eight graph edges

evidence: supported. Targets: GO:0033099.

Terminal-organelle synonym, cytadherence and gliding roles are supported. Eight edges preserve HMW2/P65/HMW3 core locations, internal core within organelle, surface P1/P30 locations, P30 adhesion role and organelle gliding. No graph edge asserts core deformation as established. Existing corrected gliding and P1 findings are not reopened.

### Other fields, status and provenance

completeness: supported. Targets: GO:0033099.

All present material claims assessed. No images, physical measurements, traits, pathway links or datasets are asserted; their optional absence is not a defect. Both history surfaces remain intact. This is agent assessment, not human scientific promotion.

## Findings

### F1: Ground the distribution to a current ancestor taxon

major / open / confirmed; issue key: attachment-organelle-mollicutes-taxon-scope.

NCBITaxon:31969 is current class Mollicutes, but NCBI full lineage places the characterized M129 example in Mycoplasmoidales directly under Mycoplasmatota. A historical review usage does not establish the current structured scope. Use verified Mycoplasmatota 544448 with VARIABLE and bounded pneumoniae-cluster notes; retain the historical source terminology explicitly.

### F2: Separate P30 assembly essentiality from normal function

major / open / confirmed; issue key: attachment-organelle-p30-assembly-essentiality.

P30 is ESSENTIAL under an assembly-only field, although mutant II-3 retains core/internal substructures. Change to DISPENSABLE with M129-mutant scope and retain adhesion, morphology and surface-knob defects; P30 remains a constituent.

## Recommended Actions And Acceptance Checks

### A1

Ground the distribution to a current ancestor taxon

- NCBITaxon:31969 is current class Mollicutes, but NCBI full lineage places the characterized M129 example in Mycoplasmoidales directly under Mycoplasmatota. A historical review usage does not establish the current structured scope. Use verified Mycoplasmatota 544448 with VARIABLE and bounded pneumoniae-cluster notes; retain the historical source terminology explicitly.
- Guarded writer; append both histories; preserve PROPOSED and unrelated claims; strict, labels, traits, history, QC and review contract pass.

### A2

Separate P30 assembly essentiality from normal function

- P30 is ESSENTIAL under an assembly-only field, although mutant II-3 retains core/internal substructures. Change to DISPENSABLE with M129-mutant scope and retain adhesion, morphology and surface-knob defects; P30 remains a constituent.
- Guarded writer; append both histories; preserve PROPOSED and unrelated claims; strict, labels, traits, history, QC and review contract pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/attachment_organelle.yaml; Entire YAML and append-only record histories | context_only | Full record read; native status is PROPOSED; input hashes captured before assessment. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=272634&amp;retmode=xml; Taxon/LineageEx, every ancestor ID | refutes | M129 lineage includes Mycoplasmatota 544448, Mycoplasmoidales 2790996 and Mycoplasmoidaceae 2790998, but not Mollicutes 31969. |
| taxon-parent | https://rest.uniprot.org/taxonomy/2790996.json; parent, rank, active, full lineage | supports | The order parent is the phylum Mycoplasmatota, not class Mollicutes. |
| phylum | https://rest.uniprot.org/taxonomy/544448.json; taxonId, scientificName, rank, active | supports | Taxon 544448 is active Mycoplasmatota, phylum; verified alternative ancestor, not a synonym for Mollicutes. |
| review2025 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12395765/fullTextXML; Inspected review article: Introduction, The motility of M. pneumoniae cluster, The attachment organelles in M. pneumoniae cluster species | supports | Review uses historical Mollicutes language and describes restricted, variable distribution and characterized pneumoniae-cluster organelles; it does not make current NCBI taxon 31969 an ancestor of M129. |
| mapping2015 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4669176/fullTextXML; Results protein localization, Fig. 4, immunogold mapping, Discussion model, strain methods | supports | Primary microscopy supports M129 polar organelle architecture, surface P1/P40/P90 and P30, internal HMW2/P65/HMW3 localization and the strain example. |
| go-identity | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033099; Inspected source-native identifier, label, definition and hierarchy | supports | Verified the exact cellular-component identity and/or topology. The GO:0033111 definition also has an erroneous mycolate-outer-membrane clause; the native record does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood. |
| go-membrane | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016020; Inspected source-native identifier, label, definition and hierarchy | supports | Verified the exact cellular-component identity and/or topology. The GO:0033111 definition also has an erroneous mycolate-outer-membrane clause; the native record does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood. |
| go-plasma | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005886; Inspected source-native identifier, label, definition and hierarchy | supports | Verified the exact cellular-component identity and/or topology. The GO:0033111 definition also has an erroneous mycolate-outer-membrane clause; the native record does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood. |
| go-whole | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033099; Inspected source-native identifier, label, definition and hierarchy | supports | Verified the exact cellular-component identity and/or topology. The GO:0033111 definition also has an erroneous mycolate-outer-membrane clause; the native record does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood. |
| go-projection | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042995; Inspected source-native identifier, label, definition and hierarchy | supports | Verified the exact cellular-component identity and/or topology. The GO:0033111 definition also has an erroneous mycolate-outer-membrane clause; the native record does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood. |
| sl | https://rest.uniprot.org/locations/SL-0021.json; Inspected source-native identifier, label, definition and hierarchy | supports | Verified the exact cellular-component identity and/or topology. The GO:0033111 definition also has an erroneous mycolate-outer-membrane clause; the native record does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood. |
| ruler2021 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8191905/fullTextXML; Results, Discussion and S7 Fig. | supports | Engineered HMW2 length controls core/organelle length. The 50-Hz, 20-cell test did not detect large stepwise displacement; the native gliding model now preserves this limitation. |
| ect2016 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4959525/fullTextXML; Class IV-22 comparison, periodicity, gliding model and ECT methods | supports | P1/P40/P90 mutant retains membrane/core. Frozen ECT informs a proposed gliding model; the record now distinguishes assembly from function and static from live imaging. |
| romero1999 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9973332+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Inspected primary abstract via Europe PMC, PMID 9973332 | supports | P30 loss disrupts cytadherence and normal tip morphology; complementation restores these phenotypes. P1 still localizes to the terminal organelle. |
| kenri2004 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15466048+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Inspected primary abstract via Europe PMC, PMID 15466048 | supports | Fluorescent P65 and HMW2 localize to the attachment organelle; source supports the bounded localization claim. |
| krause2004 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1046%2Fj.1365-2958.2003.03899.x%22&amp;format=json&amp;resultType=core; Inspected review abstract via Europe PMC, DOI 10.1046/j.1365-2958.2003.03899.x | supports | Terminal organelle refers to the membrane-bound polar extension with longitudinal paired core and terminal button; supports synonym and cytadherence context. |
| seto2003 | https://doi.org/10.1128/JB.185.3.1082-1091.2003; Publisher full text: Results Electron-dense core formation; Tables 1-2; Discussion | refutes | Mutant II-3 retains a core despite defective P30; HMW1/HMW2 mutants lack it. Supports separating assembly from cytadherence. |
| ect2018 | https://doi.org/10.1111/mmi.13937; Publisher full text: Table 1, Protein knob density was reduced on some mutants, Fig. 7, strain/ECT methods | refutes | II-3 lacks P30, has reduced P65, retains all internal substructures and has fewer surface knobs. This M129 mutant supports assembly dispensability, not normal function or universal dispensability. |
| p75471 | https://rest.uniprot.org/uniprotkb/P75471.json; Reviewed UniProtKB entry: identity, gene/locus, taxon, SL-0020 localization and ECO:0000269 PubMed annotations | supports | Identity, M129 taxon and explicit localization source annotations agree with the protein example. |
| p0cj81 | https://rest.uniprot.org/uniprotkb/P0CJ81.json; Reviewed UniProtKB entry: identity, gene/locus, taxon, SL-0020 localization and ECO:0000269 PubMed annotations | supports | Identity, M129 taxon and explicit localization source annotations agree with the protein example. |
| q50360 | https://rest.uniprot.org/uniprotkb/Q50360.json; Reviewed UniProtKB entry: identity, gene/locus, taxon, SL-0020 localization and ECO:0000269 PubMed annotations | supports | Identity, M129 taxon and explicit localization source annotations agree with the protein example. |

## Limits And Additional Notes

- Baseline full-corpus checks are reused exact-revision CI; only focused schema/strict checks were rerun before curation. CI checks are deterministic, not biological evidence.
- Cached same-day authority/primary files were inspected with original retrieval timestamps and hashes retained. Europe PMC legacy XML routes returned HTTP 500; readable publisher text or primary abstracts supplied the specific claims instead.
- 1999 and 2004 papers were assessed through their inspected abstracts plus explicit UniProt source annotations, not unavailable full text. No uninspected experimental detail is certified.
- Chen 2025 and Krause/Balish 2004 are reviews, not new experiments, despite generic source-document typing in this output.
- GO:0033111 has an upstream mycolate-outer-membrane wording error; it is not adopted by either native record. Independent cell-membrane evidence supports the curated boundary.
- Complete 28-dataset iModulonDB inventory was checked earlier this day: no applicable Mycoplasma/Mycoplasmoides dataset. This is not evidence of biological absence.
- Ignored/hidden files were included in local review/history searches. GitHub all-state searches for P30 and Mollicutes returned no matching issue; resolved P1 and gliding issues are distinct.
- This covers one record, not the remaining corpus. No native record/history edit preceded this saved observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T192854Z-attachment-organelle-assessment
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Attachment organelle: scientific assessment'
started_at: '2026-10-10T17:29:03Z'
finished_at: '2026-10-10T19:28:54Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same agent performs the audit and separately authorized curation;
    no independent human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Claim-by-claim assessment completed for this one record. Current NCBI taxon
  scope requires correction. P30 assembly essentiality also requires correction.
source:
  git_revision: 478edc23b61f8ea6be66c5b86df04040be08fbdb
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
  - path: data/structures/appendage/attachment_organelle.yaml
    sha256: 8fcf94ec6556f614d985263de8d1531e5e334d47ed48d212b87a42d1cda458ef
    role: target
  - path: docs/CURATION.md
    sha256: c3e482fbf381edcf0238e579648b779c3a8803a1d888b89397ad6fc8808dd07d
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
  - path: history/README.md
    sha256: 1636df44f28547f440242afcb4a05ac293b9714b4d7b809cecc30b975e44a522
    role: context
  - path: history/records/attachment_organelle/2026-09-06T150543Z-claude-459ee1.yaml
    sha256: cd0da0beec435828bc3ff1e604c42af6bff609c6509c346f0dc280ba19550a25
    role: context
  - path: history/records/attachment_organelle/2026-09-06T152541Z-claude-c2f4d9.yaml
    sha256: e4eb2edc91e2032dbf94dab07b8846bedbd06e19349f85d234d11c4b76986a39
    role: context
  - path: history/records/attachment_organelle/2026-10-10T070837Z-Codex-5596d4.yaml
    sha256: da925b58cbea8dcb7438ba3fab90de6415acd3a50bd49611d86800d5e1973497
    role: context
  - path: history/records/attachment_organelle/2026-10-10T075421Z-Codex-d16233.yaml
    sha256: f5058f62bbefce8615f265ca6c6255b4418ca45b2e0ce17e11ab0b4286c4b40e
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T070627Z-attachment-assembly/review.yaml
    sha256: a975e4dd0b75cda1322a6e18d16c5e2dd84bdaf5528dd5ab1d50b20ff112b0b0
    role: context
  - path: reviews/structured/20261010T072543Z-attachment-finding-dispositions/review.yaml
    sha256: 7815a953362800c676e7a92bfd22d4998184cdb2c47cd08f8c48c4b5b195ccc4
    role: context
  - path: reviews/structured/20261010T075315Z-attachment-gliding-evidence/review.yaml
    sha256: d6e7949dec4799c12e5d2033f6ebe7cae50d79f7915831c8d73f53be7216f046
    role: context
  - path: reviews/structured/20261010T083322Z-attachment-gliding-disposition/review.yaml
    sha256: c1d3c148e8485cf1f0f427880e1973dec08c8110dd27065733bf008ff0b4965c
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0033099
  path: data/structures/appendage/attachment_organelle.yaml
  label: attachment organelle
  kind: maintained
  record_class: CellStructureRecord
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
scope:
  description: Entire maintained record, present material claims and both history
    surfaces; optional missing fields are not findings.
  selection: Exact path data/structures/appendage/attachment_organelle.yaml; not a
    corpus sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033099
checks:
- check_id: pre-schema
  name: Fresh focused schema
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/attachment_organelle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed before curation.
  scope_note: 2026-10-10T19:25:47Z to 2026-10-10T19:25:51Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: pre-strict
  name: Fresh focused strict
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/attachment_organelle.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed before curation.
  scope_note: 2026-10-10T19:25:51Z to 2026-10-10T19:26:00Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: baseline-ci
  name: Exact-revision full-corpus gates
  status: passed
  required: true
  target_ids:
  - GO:0033099
  command: gh api 'repos/CultureBotAI/CellStructureMech/actions/runs?head_sha=478edc23b61f8ea6be66c5b86df04040be08fbdb&event=push&per_page=10'
    --jq '.workflow_runs[] | {id,name,status,conclusion,head_sha}'
  exit_code: 0
  expected_exit_code: 0
  summary: Verified success at unchanged HEAD for Build and test (38043028532), label
    correspondence (38043028531), identifier/trait checks (38043028562), vendored
    sync (38043028526), and merge integrity (38043028544).
  scope_note: Reused exact-commit CI, queried during this assessment, not newly executed
    local full-corpus gates. The initial sandboxed GitHub query failed; the escalated
    retry succeeded.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/attachment_organelle.yaml
  locator: Entire YAML and append-only record histories
  accessed_at: '2026-10-10T19:28:54Z'
  support: context_only
  summary: Full record read; native status is PROPOSED; input hashes captured before
    assessment.
- evidence_id: taxonomy
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=272634&retmode=xml
  locator: Taxon/LineageEx, every ancestor ID
  accessed_at: '2026-10-10T19:26:05Z'
  snapshot_sha256: a18ecdeac4d3e1be78c2cff46314fd76ad82e9d3c1a5e50cb7e884954da736b1
  support: refutes
  summary: M129 lineage includes Mycoplasmatota 544448, Mycoplasmoidales 2790996 and
    Mycoplasmoidaceae 2790998, but not Mollicutes 31969.
- evidence_id: taxon-parent
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2790996.json
  locator: parent, rank, active, full lineage
  accessed_at: '2026-10-10T19:26:04Z'
  snapshot_sha256: eb371870be7555aea28686214aeee28f9434c5a204d7a76217b0330b43e4532c
  support: supports
  summary: The order parent is the phylum Mycoplasmatota, not class Mollicutes.
- evidence_id: phylum
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/544448.json
  locator: taxonId, scientificName, rank, active
  accessed_at: '2026-10-10T19:26:05Z'
  snapshot_sha256: 78446f8d85b3f65c7fb1cfa232dba437d794d383edc2ad2bb13d8bf3c870174d
  support: supports
  summary: Taxon 544448 is active Mycoplasmatota, phylum; verified alternative ancestor,
    not a synonym for Mollicutes.
- evidence_id: review2025
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12395765/fullTextXML
  locator: 'Inspected review article: Introduction, The motility of M. pneumoniae
    cluster, The attachment organelles in M. pneumoniae cluster species'
  accessed_at: '2026-10-10T07:47:51Z'
  snapshot_sha256: afea635a9be3fb46558d6eb31136fbf46aa3b1407eba1480a1e1ecfc15af351d
  support: supports
  summary: Review uses historical Mollicutes language and describes restricted, variable
    distribution and characterized pneumoniae-cluster organelles; it does not make
    current NCBI taxon 31969 an ancestor of M129.
- evidence_id: mapping2015
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4669176/fullTextXML
  locator: Results protein localization, Fig. 4, immunogold mapping, Discussion model,
    strain methods
  accessed_at: '2026-10-10T07:47:49Z'
  snapshot_sha256: eb873beb04aa5fe98c83fe843d0b7537b62ae2738115308ea9da521d1ed42557
  support: supports
  summary: Primary microscopy supports M129 polar organelle architecture, surface
    P1/P40/P90 and P30, internal HMW2/P65/HMW3 localization and the strain example.
- evidence_id: go-identity
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033099
  locator: Inspected source-native identifier, label, definition and hierarchy
  accessed_at: '2026-10-10T07:47:55Z'
  snapshot_sha256: 7386b48d2989ab4eb1369b50a8f4fb75cc4fd7f1685e63842bacf75d5de52251
  support: supports
  summary: Verified the exact cellular-component identity and/or topology. The GO:0033111
    definition also has an erroneous mycolate-outer-membrane clause; the native record
    does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood.
- evidence_id: go-membrane
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016020
  locator: Inspected source-native identifier, label, definition and hierarchy
  accessed_at: '2026-10-10T07:47:55Z'
  snapshot_sha256: 484c18f341111604e2fe5f98c2c753c8e62366f1fc27064c89697efe3eeb7808
  support: supports
  summary: Verified the exact cellular-component identity and/or topology. The GO:0033111
    definition also has an erroneous mycolate-outer-membrane clause; the native record
    does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood.
- evidence_id: go-plasma
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005886
  locator: Inspected source-native identifier, label, definition and hierarchy
  accessed_at: '2026-10-10T07:47:55Z'
  snapshot_sha256: 1e6351cf06b2f8a92e1c37875040ea589d86395bfd25e721ab9e120904ab50af
  support: supports
  summary: Verified the exact cellular-component identity and/or topology. The GO:0033111
    definition also has an erroneous mycolate-outer-membrane clause; the native record
    does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood.
- evidence_id: go-whole
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033099
  locator: Inspected source-native identifier, label, definition and hierarchy
  accessed_at: '2026-10-10T07:47:55Z'
  snapshot_sha256: 7386b48d2989ab4eb1369b50a8f4fb75cc4fd7f1685e63842bacf75d5de52251
  support: supports
  summary: Verified the exact cellular-component identity and/or topology. The GO:0033111
    definition also has an erroneous mycolate-outer-membrane clause; the native record
    does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood.
- evidence_id: go-projection
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042995
  locator: Inspected source-native identifier, label, definition and hierarchy
  accessed_at: '2026-10-10T07:47:55Z'
  snapshot_sha256: b7bc936645b14ccf7b8d96f309e7ff4b3965e82c0b305cc6e5d3c2ae03005bd5
  support: supports
  summary: Verified the exact cellular-component identity and/or topology. The GO:0033111
    definition also has an erroneous mycolate-outer-membrane clause; the native record
    does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood.
- evidence_id: sl
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0021.json
  locator: Inspected source-native identifier, label, definition and hierarchy
  accessed_at: '2026-10-10T19:11:13Z'
  snapshot_sha256: 1a59d475631ef5fa44efc1caaa8c6a9663a1ded416fa93716227525261614479
  support: supports
  summary: Verified the exact cellular-component identity and/or topology. The GO:0033111
    definition also has an erroneous mycolate-outer-membrane clause; the native record
    does not adopt it and UniProt SL-0021 independently supports cell-membrane parthood.
- evidence_id: ruler2021
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8191905/fullTextXML
  locator: Results, Discussion and S7 Fig.
  accessed_at: '2026-10-10T07:47:49Z'
  snapshot_sha256: a92f1eadb0b76bf1d95c011cfb51bbe9344f49ef56dcfd4787cacc822b971a6d
  support: supports
  summary: Engineered HMW2 length controls core/organelle length. The 50-Hz, 20-cell
    test did not detect large stepwise displacement; the native gliding model now
    preserves this limitation.
- evidence_id: ect2016
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4959525/fullTextXML
  locator: Class IV-22 comparison, periodicity, gliding model and ECT methods
  accessed_at: '2026-10-10T07:47:54Z'
  snapshot_sha256: 7d579ad7ba828670d16c6e9e9a73c4a692a56d52366b08be6e97b59e0249f793
  support: supports
  summary: P1/P40/P90 mutant retains membrane/core. Frozen ECT informs a proposed
    gliding model; the record now distinguishes assembly from function and static
    from live imaging.
- evidence_id: romero1999
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9973332+AND+SRC%3AMED&format=json&resultType=core
  locator: Inspected primary abstract via Europe PMC, PMID 9973332
  accessed_at: '2026-10-10T19:11:10Z'
  snapshot_sha256: 77cc47fcfc01583d3ca4394afd940b1fc930171bd8274a41b4e3900991db7917
  support: supports
  summary: P30 loss disrupts cytadherence and normal tip morphology; complementation
    restores these phenotypes. P1 still localizes to the terminal organelle.
- evidence_id: kenri2004
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15466048+AND+SRC%3AMED&format=json&resultType=core
  locator: Inspected primary abstract via Europe PMC, PMID 15466048
  accessed_at: '2026-10-10T19:11:11Z'
  snapshot_sha256: aa821982affb24edd5b652db72568f99a3f5a99a9ea08aee4d9d63456958158b
  support: supports
  summary: Fluorescent P65 and HMW2 localize to the attachment organelle; source supports
    the bounded localization claim.
- evidence_id: krause2004
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1046%2Fj.1365-2958.2003.03899.x%22&format=json&resultType=core
  locator: Inspected review abstract via Europe PMC, DOI 10.1046/j.1365-2958.2003.03899.x
  accessed_at: '2026-10-10T19:11:12Z'
  snapshot_sha256: 0ef43b02b559c1716d7ea35497e858940b76b646987e9d5beadd897a414c6772
  support: supports
  summary: Terminal organelle refers to the membrane-bound polar extension with longitudinal
    paired core and terminal button; supports synonym and cytadherence context.
- evidence_id: seto2003
  kind: primary_source
  reference: https://doi.org/10.1128/JB.185.3.1082-1091.2003
  locator: 'Publisher full text: Results Electron-dense core formation; Tables 1-2;
    Discussion'
  accessed_at: '2026-10-10T19:28:54Z'
  support: refutes
  summary: Mutant II-3 retains a core despite defective P30; HMW1/HMW2 mutants lack
    it. Supports separating assembly from cytadherence.
- evidence_id: ect2018
  kind: primary_source
  reference: https://doi.org/10.1111/mmi.13937
  locator: 'Publisher full text: Table 1, Protein knob density was reduced on some
    mutants, Fig. 7, strain/ECT methods'
  accessed_at: '2026-10-10T19:28:54Z'
  support: refutes
  summary: II-3 lacks P30, has reduced P65, retains all internal substructures and
    has fewer surface knobs. This M129 mutant supports assembly dispensability, not
    normal function or universal dispensability.
- evidence_id: p75471
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P75471.json
  locator: 'Reviewed UniProtKB entry: identity, gene/locus, taxon, SL-0020 localization
    and ECO:0000269 PubMed annotations'
  accessed_at: '2026-10-10T07:47:56Z'
  snapshot_sha256: 2a707fc0d111fe27f2068e4f04b93f7a004f1cd43d09a5af40bab235b9bf4eb2
  support: supports
  summary: Identity, M129 taxon and explicit localization source annotations agree
    with the protein example.
- evidence_id: p0cj81
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0CJ81.json
  locator: 'Reviewed UniProtKB entry: identity, gene/locus, taxon, SL-0020 localization
    and ECO:0000269 PubMed annotations'
  accessed_at: '2026-10-10T07:47:56Z'
  snapshot_sha256: 02110b278a3a439af5f6caae4e545e0c414313705e6b6607895845f992221388
  support: supports
  summary: Identity, M129 taxon and explicit localization source annotations agree
    with the protein example.
- evidence_id: q50360
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q50360.json
  locator: 'Reviewed UniProtKB entry: identity, gene/locus, taxon, SL-0020 localization
    and ECO:0000269 PubMed annotations'
  accessed_at: '2026-10-10T07:47:57Z'
  snapshot_sha256: 726ae02c17f3daa6eee0ad6a333dff8a86a4917aff4ddbd12bdf8fa21ddd0cad
  support: supports
  summary: Identity, M129 taxon and explicit localization source annotations agree
    with the protein example.
assessments:
- assessment_id: identity
  area: identity
  topic: Structure identity, category, kind and mereology
  outcome: supported
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  - go-identity
  - go-membrane
  - go-plasma
  - go-whole
  - go-projection
  - sl
  - mapping2015
  summary: Exact GO structure identity, not a protein or phenotype. Membrane is-a/parthood
    and whole-organelle cell-projection parent/membrane-part boundaries are sound;
    PROPOSED retained.
- assessment_id: taxonomy
  area: scope
  topic: Taxonomic distribution and canonical example
  outcome: concern
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  - taxonomy
  - taxon-parent
  - phylum
  - review2025
  - mapping2015
  summary: The M129 example and restricted bacterial occurrence are supported, but
    historical Mollicutes wording has been attached to current NCBITaxon:31969, outside
    the example lineage. Use the verified encompassing phylum with explicit literature
    scope, not an asserted taxon synonym or universal presence.
- assessment_id: composition
  area: evidence
  topic: All five components and essentiality
  outcome: concern
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  - mapping2015
  - ruler2021
  - ect2016
  - seto2003
  - ect2018
  - romero1999
  summary: P1/P40/P90 surface membership and corrected DISPENSABLE value, HMW2 parallel
    scaffold/length setting and ESSENTIAL value, P65 terminal button and HMW3 boundary
    are supported in M. pneumoniae. P30 front localization and adhesion/shape roles
    are supported, but ESSENTIAL conflates assembly and function. No numeric stoichiometry
    is asserted; parallel alignment is architectural free text.
- assessment_id: examples
  area: evidence
  topic: Three taxon-paired protein examples
  outcome: supported
  target_ids:
  - GO:0033099
  evidence_ids:
  - p75471
  - p0cj81
  - q50360
  - kenri2004
  - mapping2015
  - taxonomy
  summary: Reviewed accessions, protein labels, genes/loci and M129 taxon match UniProt.
    PMID 15466048 supports P65/HMW2 tagging and PMID 26633540 supports all three mapped
    examples; notes correctly attribute ECO annotations to UniProt.
- assessment_id: function-graph
  area: evidence
  topic: Synonym, two functions and all eight graph edges
  outcome: supported
  target_ids:
  - GO:0033099
  evidence_ids:
  - krause2004
  - mapping2015
  - ect2016
  - ruler2021
  - romero1999
  summary: Terminal-organelle synonym, cytadherence and gliding roles are supported.
    Eight edges preserve HMW2/P65/HMW3 core locations, internal core within organelle,
    surface P1/P30 locations, P30 adhesion role and organelle gliding. No graph edge
    asserts core deformation as established. Existing corrected gliding and P1 findings
    are not reopened.
- assessment_id: completeness
  area: completeness
  topic: Other fields, status and provenance
  outcome: supported
  target_ids:
  - GO:0033099
  evidence_ids:
  - record
  - mapping2015
  summary: All present material claims assessed. No images, physical measurements,
    traits, pathway links or datasets are asserted; their optional absence is not
    a defect. Both history surfaces remain intact. This is agent assessment, not human
    scientific promotion.
findings:
- finding_id: F1
  issue_key: attachment-organelle-mollicutes-taxon-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Ground the distribution to a current ancestor taxon
  description: NCBITaxon:31969 is current class Mollicutes, but NCBI full lineage
    places the characterized M129 example in Mycoplasmoidales directly under Mycoplasmatota.
    A historical review usage does not establish the current structured scope. Use
    verified Mycoplasmatota 544448 with VARIABLE and bounded pneumoniae-cluster notes;
    retain the historical source terminology explicitly.
  target_ids:
  - GO:0033099
  field_paths:
  - taxonomic_distribution[0]
  evidence_ids:
  - record
  - taxonomy
  - taxon-parent
  - phylum
  - review2025
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Structured clade assertion excludes the characterized lineage;
    not an id-label spelling issue.
- finding_id: F2
  issue_key: attachment-organelle-p30-assembly-essentiality
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate P30 assembly essentiality from normal function
  description: P30 is ESSENTIAL under an assembly-only field, although mutant II-3
    retains core/internal substructures. Change to DISPENSABLE with M129-mutant scope
    and retain adhesion, morphology and surface-knob defects; P30 remains a constituent.
  target_ids:
  - GO:0033099
  field_paths:
  - components[1].essentiality
  - components[1].evidence
  evidence_ids:
  - record
  - seto2003
  - ect2018
  - romero1999
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#components
  native_severity: major
  normalization_reason: Functional requirement is incorrectly encoded as inability
    to assemble the structure.
actions:
- action_id: A1
  description: Ground the distribution to a current ancestor taxon
  finding_ids:
  - F1
  target_ids:
  - GO:0033099
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
  generator: just text-embeddings-refresh; just render
  acceptance_checks:
  - NCBITaxon:31969 is current class Mollicutes, but NCBI full lineage places the
    characterized M129 example in Mycoplasmoidales directly under Mycoplasmatota.
    A historical review usage does not establish the current structured scope. Use
    verified Mycoplasmatota 544448 with VARIABLE and bounded pneumoniae-cluster notes;
    retain the historical source terminology explicitly.
  - Guarded writer; append both histories; preserve PROPOSED and unrelated claims;
    strict, labels, traits, history, QC and review contract pass.
- action_id: A2
  description: Separate P30 assembly essentiality from normal function
  finding_ids:
  - F2
  target_ids:
  - GO:0033099
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/attachment_organelle.yaml
    role: maintained scientific record
  generator: just text-embeddings-refresh; just render
  acceptance_checks:
  - P30 is ESSENTIAL under an assembly-only field, although mutant II-3 retains core/internal
    substructures. Change to DISPENSABLE with M129-mutant scope and retain adhesion,
    morphology and surface-knob defects; P30 remains a constituent.
  - Guarded writer; append both histories; preserve PROPOSED and unrelated claims;
    strict, labels, traits, history, QC and review contract pass.
limitations:
- Baseline full-corpus checks are reused exact-revision CI; only focused schema/strict
  checks were rerun before curation. CI checks are deterministic, not biological evidence.
- Cached same-day authority/primary files were inspected with original retrieval timestamps
  and hashes retained. Europe PMC legacy XML routes returned HTTP 500; readable publisher
  text or primary abstracts supplied the specific claims instead.
- 1999 and 2004 papers were assessed through their inspected abstracts plus explicit
  UniProt source annotations, not unavailable full text. No uninspected experimental
  detail is certified.
- Chen 2025 and Krause/Balish 2004 are reviews, not new experiments, despite generic
  source-document typing in this output.
- GO:0033111 has an upstream mycolate-outer-membrane wording error; it is not adopted
  by either native record. Independent cell-membrane evidence supports the curated
  boundary.
- 'Complete 28-dataset iModulonDB inventory was checked earlier this day: no applicable
  Mycoplasma/Mycoplasmoides dataset. This is not evidence of biological absence.'
- Ignored/hidden files were included in local review/history searches. GitHub all-state
  searches for P30 and Mollicutes returned no matching issue; resolved P1 and gliding
  issues are distinct.
- This covers one record, not the remaining corpus. No native record/history edit
  preceded this saved observation.
```
