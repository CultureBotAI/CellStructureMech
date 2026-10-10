# Archaellum whole record: distribution and claim-level evidence audit

- Review: 20261010T070625Z-archaellum-whole-scope
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T06:51:22Z
- Finished UTC: 2026-10-10T07:06:25Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

2 concrete finding(s); all target fields read. Source-access limitations prevent complete scientific coverage.

## Scope And Provenance

Claim-by-claim audit of one entire maintained target, with source-specific access limits.

Selection: Exact path data/structures/appendage/archaeal_type_flagellum.yaml; not a sample-based corpus inference.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f346ba56ced970ce94afed30ec349a61b3982c17.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097589 | data/structures/appendage/archaeal_type_flagellum.yaml | maintained | archaeal-type flagellum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| history | passed | True | GO:0097589 | Documented validator completed successfully; deterministic validation is not scientific approval. |
| labels | passed | True | GO:0097589 | Documented validator completed successfully; deterministic validation is not scientific approval. |
| traits | passed | True | GO:0097589 | Documented validator completed successfully; deterministic validation is not scientific approval. |
| qc | passed | True | GO:0097589 | Documented validator completed successfully; deterministic validation is not scientific approval. |
| Focused schema | passed | True | GO:0097589 | Executed separately in this audit; no issues reported. |
| Focused strict | passed | True | GO:0097589 | Executed separately in this audit; no issues reported. |
| Record reference and authority verification | passed | True | GO:0097589 | Read source-native DOI metadata/text and current-day GO/taxonomy authority responses; internal IDs resolve to the maintained whole, filament and motor records. |
| Structured expression inventory | passed | False | GO:0097589 | Inventory includes S. acidocaldarius but not the M. villosus filament exemplar or P. furiosus motor exemplar. |
| Sulfolobus expression lookup | failed | False | GO:0097589 | Adapter rejected imodulons[0].regulator=None. Native iModulonDB page fallback also failed to load; no expression evidence used. |
| Remaining full-text evidence depth | unavailable | True | GO:0097589 | 2012 FlaX and 2020 FlaG/FlaF assessments are abstract-bounded; attempted publisher/PMC/Europe PMC routes did not yield full articles. Review remains partial, not a complete scientific pass. |

## Scientific And Domain Assessments

### Structure identity, hierarchy and parthood

identity: supported. Targets: GO:0097589.

The target denotes the whole structure. Parentage and stated parthood do not merge the whole archaellum with its named subassemblies.

### Distribution and organism scope

scope: concern. Targets: GO:0097589.

Taxon identifiers are sound, but the current bacterial exclusion is contradicted. Genomic predictions outside the cultured example are not treated as experimental observations.

### Maturation, filament composition, examples and motility

evidence: supported. Targets: GO:0097589.

The historical archaellin-processing, type-IV-pilin-like filament and ATP-powered motility model is supported. Alternating subunits stay confined to M. villosus, and motor machinery is not asserted as a filament constituent.

### History, ownership and scientific status

provenance: supported. Targets: GO:0097589.

PROPOSED and agent history remain unchanged. Append-only repository history was read and validated. This audit grants no human sign-off or mutation authority.

### Optional slots and unresolved exact families

completeness: not_applicable. Targets: GO:0097589.

No defect inferred from missing optional properties, images, trait links, stoichiometry, or acknowledged unresolved family grounding. No exact family accession was independently established.

### Motor modules and examples

evidence: concern. Targets: GO:0097589.

Nucleotide-dependent regulator and narrow FlaX/FlaI and Pyrococcus examples have support. Combined-anchor evidence needs correction.

### Causal graph evidence and node types

graph: concern. Targets: GO:0097589.

Assembly, regulation and rotation edges were read individually. The combined-anchor edge exceeds its attached citation. Protein-complex nodes are permitted by the native GENE_OR_PROTEIN description, so no type-only finding is manufactured.

### Incomplete source depth

completeness: unknown. Targets: GO:0097589.

Full-text follow-up is still needed for the 2012 scaffold and 2020 anchor studies. All target fields were read; their entire experimental literature is not certified.

### Strain-specific FlaH example and prior corrections

grounding: supported. Targets: GO:0097589.

Q4J9K9 agrees with the named gene and strain. The previous two attribution corrections remain in place; this review neither reopens nor supersedes their resolved findings.

## Findings

### F1: Remove the blanket bacterial absence assertion

major / open / confirmed; issue key: archaellum-whole-bacterial-absence-2025.

The NCBITaxon:2 ABSENT entry excludes an experimentally supported bacterial example. Its old citation cannot establish domain-wide absence in the current record.

### F2: Separate FlaF binding data from the combined FlaF/FlaG model

minor / open / confirmed; issue key: archaellum-whole-flafg-anchor-citation-scope.

The combined-anchor edge cites only the FlaF study. Add directly relevant FlaG/FlaF evidence and distinguish the demonstrated interaction from inferred motor anchoring; envelope localization alone does not prove the pairwise bridge.

## Recommended Actions And Acceptance Checks

### A1

Correct the bacterial distribution and reconcile any exclusivity wording; preserve the structure identity and PROPOSED status.

- The domain-wide ABSENT claim is removed or replaced with evidence-backed bounded distribution.
- The experimental example is separated from genome-only candidates and unresolved motor details.
- Guarded writer, curation event, repository history and all native gates pass under separate curation authorization.

### A2

Attach appropriate FlaG/FlaF evidence to the component and anchoring edge, and retain the model-versus-measurement distinction.

- Inspect the 2020 full article before adding claims beyond its abstract.
- Do not equate envelope localization or FlaF binding alone with direct demonstration of the complete anchor bridge.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/archaeal_type_flagellum.yaml; Entire maintained YAML, including all graph edges, discussions and history | context_only | Read the entire PROPOSED target. The maintained YAML owns future changes; generated pages do not. |
| bacterial | https://doi.org/10.1038/s41564-025-02110-8; Results: L. aerophila, an archaellated bacterium; filament cryoEM; motor predictions; Methods: growth and motility plates; Figs 3-5 | refutes | Litorilinea aerophila has experimentally identified archaellum filaments and swimming motility. Motor architecture is supported partly by predicted structures, not a resolved bacterial motor. |
| synthesis | https://doi.org/10.3389/fmicb.2015.00023; Source-native secondary review; processing, assembly machinery, rotation, glycosylation and distribution sections | partial | Inspected as a secondary synthesis, not a new primary experiment. Supports the historical model but predates the bacterial exception. |
| arlb | https://doi.org/10.1038/s41467-022-28337-1; Results: The M. villosus archaellum consists of the subunits ArlB1 and ArlB2; Figs 1-4; Discussion; culture and filament methods | supports | The species-specific alternating ArlB1/ArlB2 filament is supported; the record does not universalize its stoichiometry or hypothetical dimer-assembly mechanism. |
| go-whole | https://www.ebi.ac.uk/QuickGO/term/GO:0097589; Current term ID, name, definition, synonyms, aspect and obsolete status | supports | The term denotes the whole archaellum, not a filament-only or motor-only entity. |
| go-motility | https://www.ebi.ac.uk/QuickGO/term/GO:0097590; Current name, definition and biological_process aspect | supports | The motility grounding is specific to the archaellum. |
| go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=archaellum&amp;limit=100; QuickGO query archaellum, complete one-result response; separate broad name searches inspected only their first page | context_only | The exact archaellum query returns the whole-structure term. Neither that term nor bacterial motor/filament terms are exact replacements for the local subassemblies. |
| taxon-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; taxId, scientificName, rank and available lineage/synonyms | supports | The identifier and label agree; taxon identity does not validate the associated presence assertion. |
| taxon-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; taxId, scientificName, rank and available lineage/synonyms | supports | The identifier and label agree; taxon identity does not validate the associated presence assertion. |
| taxon-2285 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2285; taxId, scientificName, rank and available lineage/synonyms | supports | The identifier and label agree; taxon identity does not validate the associated presence assertion. |
| taxon-2261 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2261; taxId, scientificName, rank and available lineage/synonyms | supports | The identifier and label agree; taxon identity does not validate the associated presence assertion. |
| taxon-667126 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/667126; taxId, scientificName, rank and available lineage/synonyms | supports | The identifier and label agree; taxon identity does not validate the associated presence assertion. |
| taxon-330779 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/330779; taxId, scientificName, rank and available lineage/synonyms | supports | The identifier and label agree; taxon identity does not validate the associated presence assertion. |
| parent | https://www.ebi.ac.uk/QuickGO/term/GO:0042995; Current definition, aspect and obsolete status | supports | The broader parent is appropriate; it is not asserted as exact identity. |
| flaf | https://doi.org/10.1016/j.str.2015.03.001; Soluble Domain of FlaF Binds to S-layer Proteins; Discussion; Experimental Procedures | partial | Experiments establish soluble FlaF binding to isolated S-layer. The stator model is proposed, and collaboration with FlaG remains hypothetical in this article. |
| flafg | https://doi.org/10.1038/s41564-019-0622-3; Primary abstract from exact-DOI Europe PMC core response; PMID:31844299; full article unavailable through attempted routes | partial | Later FlaG-FlaF interaction and mutagenesis experiments support a combined anchor model. This is a suitable evidence lead, not proof of every motor-contact detail. |
| pyrococcus | https://doi.org/10.7554/eLife.27470; Results: Architecture; Integration into periplasm; Location of motor subunits; Discussion; Figures 1-3 | partial | In situ motor densities and docking support the envelope-associated example. The article leaves periplasmic density assignments uncertain and does not resolve a combined FlaF/FlaG bridge. |
| flax | https://doi.org/10.1074/jbc.M112.414383; Primary abstract in exact-DOI core JSON; PubMed figure legends inspected earlier; publisher full text returned 403 | partial | Supports FlaX ring formation and FlaI interaction in the narrow exemplar and scaffold claims. |
| flah | https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.13260; Summary; Results: Walker motifs, FlaI interaction and assembly complementation; Discussion | partial | FlaH binds ATP and supports nucleotide-dependent interactions; the tested proteins lacked detectable in vitro ATPase activity. ATP binding must not be conflated with demonstrated hydrolysis. |
| arlh-update | https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.14781; Introduction; Results 2.1-2.3; matched primary abstract PMID:34219289 | context_only | Later experiments demonstrate ArlH autophosphorylation in two species. This supports regulation and does not warrant an unqualified conventional ATPase label. |
| uniprot | https://rest.uniprot.org/uniprotkb/Q4J9K9.json; Reviewed entry; gene flaH; taxon 330779; subcellular-location ECO:0000269 with PMID:24103130 | supports | The protein example preserves the correct gene, strain, accession and localization evidence attribution. |
| interactions | https://doi.org/10.1111/febs.12534; Primary abstract, PMID:24103130; full text unavailable | partial | The already corrected scaffold citation names FlaX/FlaI/FlaH and explicitly declares abstract-only access. |

## Limits And Additional Notes

- No new native record, generated page, curation history, GitHub issue or PR was changed. No paid research was used.
- Record-level review is not independent human approval or an exhaustive search of all literature. Missing bundles elsewhere do not establish coverage.
- The broad GO multiword searches were first-page bounded; no claim of exhaustive absence of an exact family or ontology term is made.
- Full-text limitations for the FlaX and newer FlaG/FlaF papers and optional expression-source failure leave this review partial.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T070625Z-archaellum-whole-scope
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Archaellum whole record: distribution and claim-level evidence audit'
started_at: '2026-10-10T06:51:22Z'
finished_at: '2026-10-10T07:06:25Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same agent recently corrected two other claims in this whole-archaellum
    record; this is not independent review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 2 concrete finding(s); all target fields read. Source-access limitations
  prevent complete scientific coverage.
source:
  git_revision: f346ba56ced970ce94afed30ec349a61b3982c17
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
  - path: data/structures/appendage/archaeal_type_flagellum.yaml
    sha256: a530ce0e281e35ea6fd630411c63471fe44f3e9820a67127dfa5239ec8e83c8a
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
  - path: history/records/archaeal_type_flagellum/2026-09-04T161802Z-claude-331d93.yaml
    sha256: ee5f9b9fbc551686b1102825c82930d0d30b5a0ce9bd818cba285e625ca48be4
    role: context
  - path: history/records/archaeal_type_flagellum/2026-10-10T060746Z-Codex-8e5363.yaml
    sha256: 30d6304719531bf043f441d11fbff242ddbfc94fc2f82f0a10d19c163638edd1
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T060647Z-archaellum-evidence/review.yaml
    sha256: e86be00b8c726b0fdcf979c02b1417c35ec6c1bd49aadf8bd37372e0e6c96454
    role: context
  - path: reviews/structured/20261010T062212Z-archaellum-disposition/review.yaml
    sha256: 2873de2f3914cc7a57438b46b6c95d995f84207690bb39b31cd69eb09da3b4ef
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0097589
  path: data/structures/appendage/archaeal_type_flagellum.yaml
  label: archaeal-type flagellum
  kind: maintained
  record_class: CellStructureRecord
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/archaeal_type_flagellum.yaml
    role: maintained scientific record
scope:
  description: Claim-by-claim audit of one entire maintained target, with source-specific
    access limits.
  selection: Exact path data/structures/appendage/archaeal_type_flagellum.yaml; not
    a sample-based corpus inference.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0097589
checks:
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0097589
  command: .venv/bin/python scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validator completed successfully; deterministic validation is
    not scientific approval.
  scope_note: 2026-10-10T06:49:30Z to 2026-10-10T06:50:19Z; log SHA-256 86e440ae4c54ba14bc23c67108fe3a209b94444c27774b1b0b3b3535704719e6;
    full corpus
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0097589
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validator completed successfully; deterministic validation is
    not scientific approval.
  scope_note: 2026-10-10T06:50:19Z to 2026-10-10T06:52:30Z; log SHA-256 553dd4c9f88c8a5289a33f588649f4677e541cc9da09ecd6c78c0e9f3cae8917;
    full corpus
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0097589
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validator completed successfully; deterministic validation is
    not scientific approval.
  scope_note: 2026-10-10T06:52:30Z to 2026-10-10T06:52:59Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f;
    full corpus
- check_id: qc
  name: qc
  status: passed
  required: true
  target_ids:
  - GO:0097589
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: Documented validator completed successfully; deterministic validation is
    not scientific approval.
  scope_note: 2026-10-10T06:52:59Z to 2026-10-10T07:06:08Z; log SHA-256 d2d47649ec6fd19e1d4b6fbeffe19366cc12c86cff12053c9bcb04ebea9d4ce5;
    full corpus
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  target_ids:
  - GO:0097589
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/archaeal_type_flagellum.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Executed separately in this audit; no issues reported.
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  target_ids:
  - GO:0097589
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/archaeal_type_flagellum.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Executed separately in this audit; no issues reported.
- check_id: source-identities
  name: Record reference and authority verification
  status: passed
  required: true
  target_ids:
  - GO:0097589
  evidence_ids:
  - record
  - bacterial
  - synthesis
  - arlb
  - go-whole
  - go-motility
  - go-search
  - taxon-2
  - taxon-2157
  - taxon-2285
  - taxon-2261
  - taxon-667126
  - taxon-330779
  - parent
  - flaf
  - flafg
  - pyrococcus
  - flax
  - flah
  - arlh-update
  - uniprot
  - interactions
  summary: Read source-native DOI metadata/text and current-day GO/taxonomy authority
    responses; internal IDs resolve to the maintained whole, filament and motor records.
- check_id: expression-inventory
  name: Structured expression inventory
  status: passed
  required: false
  target_ids:
  - GO:0097589
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
  summary: Inventory includes S. acidocaldarius but not the M. villosus filament exemplar
    or P. furiosus motor exemplar.
- check_id: expression-search
  name: Sulfolobus expression lookup
  status: failed
  required: false
  target_ids:
  - GO:0097589
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_acidocaldarius --dataset modulome --query fla
  exit_code: 2
  expected_exit_code: 0
  summary: Adapter rejected imodulons[0].regulator=None. Native iModulonDB page fallback
    also failed to load; no expression evidence used.
- check_id: fulltext-depth
  name: Remaining full-text evidence depth
  status: unavailable
  required: true
  target_ids:
  - GO:0097589
  evidence_ids:
  - flax
  - flafg
  summary: 2012 FlaX and 2020 FlaG/FlaF assessments are abstract-bounded; attempted
    publisher/PMC/Europe PMC routes did not yield full articles. Review remains partial,
    not a complete scientific pass.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/archaeal_type_flagellum.yaml
  locator: Entire maintained YAML, including all graph edges, discussions and history
  accessed_at: '2026-10-10T07:06:25Z'
  support: context_only
  snapshot_sha256: a530ce0e281e35ea6fd630411c63471fe44f3e9820a67127dfa5239ec8e83c8a
  summary: Read the entire PROPOSED target. The maintained YAML owns future changes;
    generated pages do not.
- evidence_id: bacterial
  kind: primary_source
  reference: https://doi.org/10.1038/s41564-025-02110-8
  locator: 'Results: L. aerophila, an archaellated bacterium; filament cryoEM; motor
    predictions; Methods: growth and motility plates; Figs 3-5'
  accessed_at: '2026-10-10T06:51:21Z'
  snapshot_sha256: e3f6b0250391b28747f24fcf3f2621d85db8f9a4b6a96866ad566af095f96afe
  summary: Litorilinea aerophila has experimentally identified archaellum filaments
    and swimming motility. Motor architecture is supported partly by predicted structures,
    not a resolved bacterial motor.
  support: refutes
- evidence_id: synthesis
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2015.00023
  locator: Source-native secondary review; processing, assembly machinery, rotation,
    glycosylation and distribution sections
  accessed_at: '2026-10-10T05:03:52Z'
  snapshot_sha256: c2cec0461a17865f7242ef36df178bfc68d00c1f1e292b75f9682a6ba5461464
  summary: Inspected as a secondary synthesis, not a new primary experiment. Supports
    the historical model but predates the bacterial exception.
  support: partial
- evidence_id: arlb
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-022-28337-1
  locator: 'Results: The M. villosus archaellum consists of the subunits ArlB1 and
    ArlB2; Figs 1-4; Discussion; culture and filament methods'
  accessed_at: '2026-10-10T05:03:54Z'
  snapshot_sha256: def26a9b9abd602bf1d23d61ce02a180a603d91852544f5d76b4bc32825f8ae1
  summary: The species-specific alternating ArlB1/ArlB2 filament is supported; the
    record does not universalize its stoichiometry or hypothetical dimer-assembly
    mechanism.
  support: supports
- evidence_id: go-whole
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/term/GO:0097589
  locator: Current term ID, name, definition, synonyms, aspect and obsolete status
  accessed_at: '2026-10-10T05:04:03Z'
  snapshot_sha256: 136977fcd947e027684e55ebfdd698cf4f17470777c56a3693ccc858ca104ce1
  summary: The term denotes the whole archaellum, not a filament-only or motor-only
    entity.
  support: supports
- evidence_id: go-motility
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/term/GO:0097590
  locator: Current name, definition and biological_process aspect
  accessed_at: '2026-10-10T05:04:04Z'
  snapshot_sha256: fef853d9ce6a36042c99450a6a8a5cdb7373120539d157e459b393864c6e6ddc
  summary: The motility grounding is specific to the archaellum.
  support: supports
- evidence_id: go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=archaellum&limit=100
  locator: QuickGO query archaellum, complete one-result response; separate broad
    name searches inspected only their first page
  accessed_at: '2026-10-10T06:49:17Z'
  snapshot_sha256: be2922ae316517bc6802975dc8726012799d214d3c577c24a9d4cea5e29d7235
  summary: The exact archaellum query returns the whole-structure term. Neither that
    term nor bacterial motor/filament terms are exact replacements for the local subassemblies.
  support: context_only
  search_scope: QuickGO archaellum query complete at one hit. Broad multiword motor/filament
    queries returned more than one page; only first-page candidates were inspected.
    No exhaustive ontology-absence claim.
- evidence_id: taxon-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: taxId, scientificName, rank and available lineage/synonyms
  accessed_at: '2026-10-10T05:04:05Z'
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
  summary: The identifier and label agree; taxon identity does not validate the associated
    presence assertion.
  support: supports
- evidence_id: taxon-2157
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: taxId, scientificName, rank and available lineage/synonyms
  accessed_at: '2026-10-10T05:04:05Z'
  snapshot_sha256: c6e652011b95e43e933983bf5f3f5cec9508c1925adae00dc55e46cd4e816b19
  summary: The identifier and label agree; taxon identity does not validate the associated
    presence assertion.
  support: supports
- evidence_id: taxon-2285
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2285
  locator: taxId, scientificName, rank and available lineage/synonyms
  accessed_at: '2026-10-10T05:04:07Z'
  snapshot_sha256: 1d5a3970abbb1b837fc33a6900e102c20c4b0cfa68b371c6d9cd135f3ee18293
  summary: The identifier and label agree; taxon identity does not validate the associated
    presence assertion.
  support: supports
- evidence_id: taxon-2261
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2261
  locator: taxId, scientificName, rank and available lineage/synonyms
  accessed_at: '2026-10-10T05:04:07Z'
  snapshot_sha256: 42be3ef89d164a780682596a5f4de3790826010ba93cfd7569729a878216d916
  summary: The identifier and label agree; taxon identity does not validate the associated
    presence assertion.
  support: supports
- evidence_id: taxon-667126
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/667126
  locator: taxId, scientificName, rank and available lineage/synonyms
  accessed_at: '2026-10-10T05:04:06Z'
  snapshot_sha256: 3c462a758dc7ee73cdf47f2edaa17ab951cfeba44ec50ff42b3236a1f4bacc77
  summary: The identifier and label agree; taxon identity does not validate the associated
    presence assertion.
  support: supports
- evidence_id: taxon-330779
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/330779
  locator: taxId, scientificName, rank and available lineage/synonyms
  accessed_at: '2026-10-10T05:04:08Z'
  snapshot_sha256: 4003f0e0a0d4defc9838adb3cea70ae4c4762ba65ffeaaae4947bd23cb38607d
  summary: The identifier and label agree; taxon identity does not validate the associated
    presence assertion.
  support: supports
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/term/GO:0042995
  locator: Current definition, aspect and obsolete status
  accessed_at: '2026-10-10T05:00:15Z'
  snapshot_sha256: b7bc936645b14ccf7b8d96f309e7ff4b3965e82c0b305cc6e5d3c2ae03005bd5
  summary: The broader parent is appropriate; it is not asserted as exact identity.
  support: supports
- evidence_id: flaf
  kind: primary_source
  reference: https://doi.org/10.1016/j.str.2015.03.001
  locator: Soluble Domain of FlaF Binds to S-layer Proteins; Discussion; Experimental
    Procedures
  accessed_at: '2026-10-10T05:03:57Z'
  snapshot_sha256: 1f91e3ad404aef42c701b0962abc53e1be639c62e98d86c1af3d5f6a57c9af65
  summary: Experiments establish soluble FlaF binding to isolated S-layer. The stator
    model is proposed, and collaboration with FlaG remains hypothetical in this article.
  support: partial
- evidence_id: flafg
  kind: primary_source
  reference: https://doi.org/10.1038/s41564-019-0622-3
  locator: Primary abstract from exact-DOI Europe PMC core response; PMID:31844299;
    full article unavailable through attempted routes
  accessed_at: '2026-10-10T06:49:15Z'
  snapshot_sha256: 61854286ef7c29e7105eac43e88f489463345053233d2ebb5f299c2ae7c70b12
  summary: Later FlaG-FlaF interaction and mutagenesis experiments support a combined
    anchor model. This is a suitable evidence lead, not proof of every motor-contact
    detail.
  support: partial
- evidence_id: pyrococcus
  kind: primary_source
  reference: https://doi.org/10.7554/eLife.27470
  locator: 'Results: Architecture; Integration into periplasm; Location of motor subunits;
    Discussion; Figures 1-3'
  accessed_at: '2026-10-10T05:04:01Z'
  snapshot_sha256: 8d3388daf8be92d10a276aa67596fefd9424c7102908782b9665a742072cd37a
  summary: In situ motor densities and docking support the envelope-associated example.
    The article leaves periplasmic density assignments uncertain and does not resolve
    a combined FlaF/FlaG bridge.
  support: partial
- evidence_id: flax
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M112.414383
  locator: Primary abstract in exact-DOI core JSON; PubMed figure legends inspected
    earlier; publisher full text returned 403
  accessed_at: '2026-10-10T05:03:55Z'
  snapshot_sha256: fe0bfb9548001123d7b635b152981e3c19ca549332bf44e466dd16cdd27351c9
  summary: Supports FlaX ring formation and FlaI interaction in the narrow exemplar
    and scaffold claims.
  support: partial
- evidence_id: flah
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.13260
  locator: 'Summary; Results: Walker motifs, FlaI interaction and assembly complementation;
    Discussion'
  accessed_at: '2026-10-10T06:53:20Z'
  support: partial
  summary: FlaH binds ATP and supports nucleotide-dependent interactions; the tested
    proteins lacked detectable in vitro ATPase activity. ATP binding must not be conflated
    with demonstrated hydrolysis.
- evidence_id: arlh-update
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.14781
  locator: Introduction; Results 2.1-2.3; matched primary abstract PMID:34219289
  accessed_at: '2026-10-10T06:53:20Z'
  support: context_only
  summary: Later experiments demonstrate ArlH autophosphorylation in two species.
    This supports regulation and does not warrant an unqualified conventional ATPase
    label.
- evidence_id: uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q4J9K9.json
  locator: Reviewed entry; gene flaH; taxon 330779; subcellular-location ECO:0000269
    with PMID:24103130
  accessed_at: '2026-10-10T05:04:08Z'
  snapshot_sha256: 0c7549fb636a380c7c25448ac4b5a33145b7a0bffe2d7392288d33e5363abd6d
  summary: The protein example preserves the correct gene, strain, accession and localization
    evidence attribution.
  support: supports
- evidence_id: interactions
  kind: primary_source
  reference: https://doi.org/10.1111/febs.12534
  locator: Primary abstract, PMID:24103130; full text unavailable
  accessed_at: '2026-10-10T05:04:02Z'
  snapshot_sha256: 21526e358b3f10876259faf59afc0a47faedb36edaf004fa0e6566c986f5f05b
  summary: The already corrected scaffold citation names FlaX/FlaI/FlaH and explicitly
    declares abstract-only access.
  support: partial
assessments:
- assessment_id: identity
  area: identity
  topic: Structure identity, hierarchy and parthood
  outcome: supported
  target_ids:
  - GO:0097589
  evidence_ids:
  - record
  - go-whole
  - parent
  - go-search
  - arlb
  summary: The target denotes the whole structure. Parentage and stated parthood do
    not merge the whole archaellum with its named subassemblies.
- assessment_id: taxonomy
  area: scope
  topic: Distribution and organism scope
  outcome: concern
  target_ids:
  - GO:0097589
  evidence_ids:
  - record
  - bacterial
  - synthesis
  - taxon-2
  - taxon-2157
  - taxon-2285
  - taxon-2261
  - taxon-667126
  - taxon-330779
  summary: Taxon identifiers are sound, but the current bacterial exclusion is contradicted.
    Genomic predictions outside the cultured example are not treated as experimental
    observations.
  dimensions:
  - name: experimental-scope
    value: Litorilinea aerophila DSM 25763 / ATCC BAA-2444; motility-plate-derived
      cells
    definition: Experimental organism and growth context, distinct from the genome
      survey
    evidence_ids:
    - bacterial
  - name: motor-evidence-tier
    value: Functional machinery with sequence/structure-model support; not a directly
      resolved bacterial motor
    definition: Limit on interpretation of the new exception
    evidence_ids:
    - bacterial
- assessment_id: filament-function
  area: evidence
  topic: Maturation, filament composition, examples and motility
  outcome: supported
  target_ids:
  - GO:0097589
  evidence_ids:
  - record
  - synthesis
  - arlb
  - go-motility
  summary: The historical archaellin-processing, type-IV-pilin-like filament and ATP-powered
    motility model is supported. Alternating subunits stay confined to M. villosus,
    and motor machinery is not asserted as a filament constituent.
- assessment_id: status
  area: provenance
  topic: History, ownership and scientific status
  outcome: supported
  target_ids:
  - GO:0097589
  evidence_ids:
  - record
  summary: PROPOSED and agent history remain unchanged. Append-only repository history
    was read and validated. This audit grants no human sign-off or mutation authority.
- assessment_id: optional
  area: completeness
  topic: Optional slots and unresolved exact families
  outcome: not_applicable
  target_ids:
  - GO:0097589
  evidence_ids:
  - record
  summary: No defect inferred from missing optional properties, images, trait links,
    stoichiometry, or acknowledged unresolved family grounding. No exact family accession
    was independently established.
- assessment_id: motor-evidence
  area: evidence
  topic: Motor modules and examples
  outcome: concern
  target_ids:
  - GO:0097589
  evidence_ids:
  - record
  - flah
  - flax
  - flaf
  - flafg
  - pyrococcus
  - arlh-update
  summary: Nucleotide-dependent regulator and narrow FlaX/FlaI and Pyrococcus examples
    have support. Combined-anchor evidence needs correction.
  dimensions:
  - name: sulfolobus-construct-scope
    value: Purified soluble/truncated proteins and defined mutant/complementation
      experiments
    definition: Not direct observation of every contact in an intact motor
    evidence_ids:
    - flah
    - flaf
    - flax
- assessment_id: graph
  area: graph
  topic: Causal graph evidence and node types
  outcome: concern
  target_ids:
  - GO:0097589
  evidence_ids:
  - record
  - synthesis
  - flah
  - flaf
  - flafg
  summary: Assembly, regulation and rotation edges were read individually. The combined-anchor
    edge exceeds its attached citation. Protein-complex nodes are permitted by the
    native GENE_OR_PROTEIN description, so no type-only finding is manufactured.
- assessment_id: depth
  area: completeness
  topic: Incomplete source depth
  outcome: unknown
  target_ids:
  - GO:0097589
  evidence_ids:
  - flax
  - flafg
  summary: Full-text follow-up is still needed for the 2012 scaffold and 2020 anchor
    studies. All target fields were read; their entire experimental literature is
    not certified.
- assessment_id: protein-example
  area: grounding
  topic: Strain-specific FlaH example and prior corrections
  outcome: supported
  target_ids:
  - GO:0097589
  evidence_ids:
  - record
  - uniprot
  - taxon-330779
  - interactions
  summary: Q4J9K9 agrees with the named gene and strain. The previous two attribution
    corrections remain in place; this review neither reopens nor supersedes their
    resolved findings.
findings:
- finding_id: F1
  issue_key: archaellum-whole-bacterial-absence-2025
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Remove the blanket bacterial absence assertion
  description: The NCBITaxon:2 ABSENT entry excludes an experimentally supported bacterial
    example. Its old citation cannot establish domain-wide absence in the current
    record.
  target_ids:
  - GO:0097589
  field_paths:
  - taxonomic_distribution[1].presence
  - taxonomic_distribution[1].note
  evidence_ids:
  - record
  - bacterial
  - taxon-2
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/archaeal_type_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: A false domain-wide taxonomic exclusion, not merely a missing
    optional exemplar.
- finding_id: F2
  issue_key: archaellum-whole-flafg-anchor-citation-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Separate FlaF binding data from the combined FlaF/FlaG model
  description: The combined-anchor edge cites only the FlaF study. Add directly relevant
    FlaG/FlaF evidence and distinguish the demonstrated interaction from inferred
    motor anchoring; envelope localization alone does not prove the pairwise bridge.
  target_ids:
  - GO:0097589
  field_paths:
  - components[3].evidence
  - causal_graphs[0].edges[4].evidence
  evidence_ids:
  - record
  - flaf
  - pyrococcus
  - flafg
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/archaeal_type_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded claim-level citation and certainty gap; later evidence
    supports the module, so this is not a claim that the biology is false.
actions:
- action_id: A1
  description: Correct the bacterial distribution and reconcile any exclusivity wording;
    preserve the structure identity and PROPOSED status.
  finding_ids:
  - F1
  target_ids:
  - GO:0097589
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/archaeal_type_flagellum.yaml
    role: maintained scientific record
  generator: just render
  acceptance_checks:
  - The domain-wide ABSENT claim is removed or replaced with evidence-backed bounded
    distribution.
  - The experimental example is separated from genome-only candidates and unresolved
    motor details.
  - Guarded writer, curation event, repository history and all native gates pass under
    separate curation authorization.
- action_id: A2
  description: Attach appropriate FlaG/FlaF evidence to the component and anchoring
    edge, and retain the model-versus-measurement distinction.
  finding_ids:
  - F2
  target_ids:
  - GO:0097589
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/archaeal_type_flagellum.yaml
    role: maintained scientific record
  generator: just render
  acceptance_checks:
  - Inspect the 2020 full article before adding claims beyond its abstract.
  - Do not equate envelope localization or FlaF binding alone with direct demonstration
    of the complete anchor bridge.
limitations:
- No new native record, generated page, curation history, GitHub issue or PR was changed.
  No paid research was used.
- Record-level review is not independent human approval or an exhaustive search of
  all literature. Missing bundles elsewhere do not establish coverage.
- The broad GO multiword searches were first-page bounded; no claim of exhaustive
  absence of an exact family or ontology term is made.
- Full-text limitations for the FlaX and newer FlaG/FlaF papers and optional expression-source
  failure leave this review partial.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261010T060647Z-archaellum-evidence
  relationship: Extends scientific scope with new issue keys; does not supersede or
    change prior dispositions.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261010T062212Z-archaellum-disposition
  relationship: Extends scientific scope with new issue keys; does not supersede or
    change prior dispositions.
```
