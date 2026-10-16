# NarGHI literature author-attribution review

- Review: 20261012T083110Z-narghi-review-author-attribution
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T08:24:42Z
- Finished UTC: 2026-10-12T08:31:10Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record scientific review completed with one minor provenance finding covering four author-misattribution notes for two secondary reviews. Structure identity, component roles, source-scoped composition and all five coarse graph edges are supported within the recorded source-reading limits.

## Scope And Provenance

One entire native record, every material assertion, all five graph edges, all seven imported participants, creation history and retained legacy review; no sampling.

Selection: data/structures/energy_complex/narghi_complex.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e74d0c3e33df7e44348afbba1695b61c23262ab0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0044799 | data/structures/energy_complex/narghi_complex.yaml | maintained | NarGHI complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0044799 | Fresh target check; actual UTC/log receipts retained.  |
| strict | passed | True | GO:0044799 | Fresh target check; actual UTC/log receipts retained.  |
| snippets | passed | True | GO:0044799 | Fresh target check; actual UTC/log receipts retained. Zero of38 citations carry snippets; not a full-text check. |
| reused-release-qc | passed | True | GO:0044799 | Reused actual result from 2026-10-12T06:45:16Z on hash-verified unchanged inputs. QC987passed/3skipped; labels603 no-adapter skips; trait index cached. Not a fresh execution or CI result. |
| reused-release-labels | passed | True | GO:0044799 | Reused actual result from 2026-10-12T06:47:16Z on hash-verified unchanged inputs. QC987passed/3skipped; labels603 no-adapter skips; trait index cached. Not a fresh execution or CI result. |
| reused-release-traits | passed | True | GO:0044799 | Reused actual result from 2026-10-12T06:48:52Z on hash-verified unchanged inputs. QC987passed/3skipped; labels603 no-adapter skips; trait index cached. Not a fresh execution or CI result. |
| reused-curies-live | passed | True | GO:0044799 | Reused actual result from 2026-10-12T07:10:58Z; log and unchanged maintained inputs verified. Live CURIE4023OK/251skips, archive200valid, contract4passed. Fresh post-save archive/contract checks follow separately. |
| reused-post-save-archive | passed | True | GO:0044799 | Reused actual result from 2026-10-12T08:18:57Z; log and unchanged maintained inputs verified. Live CURIE4023OK/251skips, archive200valid, contract4passed. Fresh post-save archive/contract checks follow separately. |
| reused-post-save-contract | passed | True | GO:0044799 | Reused actual result from 2026-10-12T08:20:34Z; log and unchanged maintained inputs verified. Live CURIE4023OK/251skips, archive200valid, contract4passed. Fresh post-save archive/contract checks follow separately. |
| adapter-datasets | passed | False | GO:0044799 | Fresh inventory or exact gene search; bounded gene hits only, no biological absence inference. |
| adapter-narG | passed | False | GO:0044799 | Fresh inventory or exact gene search; bounded gene hits only, no biological absence inference. |
| adapter-narH | passed | False | GO:0044799 | Fresh inventory or exact gene search; bounded gene hits only, no biological absence inference. |
| adapter-narI | passed | False | GO:0044799 | Fresh inventory or exact gene search; bounded gene hits only, no biological absence inference. |
| Initial draft contract validation | failed | False | GO:0044799 | Initial draft used unsupported assessment area composition. Corrected to evidence for component identity/roles and quantity for assembly counts. Scientific assessment unchanged; corrected draft separately validated before save. |

## Scientific And Domain Assessments

### Identity, definition, synonyms and parentage

identity: supported. Targets: GO:0044799.

Native GO identity denotes the respiratory NarGHI complex rather than NarG alone, assimilatory reductase or periplasmic Nap. Component kind, energy category, exact synonyms and is-a parent agree.

### Families, roles and protein examples

evidence: supported. Targets: GO:0044799.

All three native family groundings and reviewed E. coli examples agree with the intended constituent roles. ESSENTIAL is read as assembly membership, not cell viability. Family-level annotations are not substituted for experimental stoichiometry.

### Taxon-scoped complex composition and cofactors

quantity: supported. Targets: GO:0044799.

All seven CPX participant rows match. Heterotrimeric unit and dimeric heterohexamer are compatible levels of assembly. The source-scoped E. coli count is not universalized; generic cofactor identity is distinguished from exact experimental coordination/redox state.

### Reaction and all five NONMECHANISTIC graph edges

evidence: supported. Targets: GO:0044799.

Quinol oxidation coupled to nitrate reduction agrees with the GO reaction. Each native edge has relevant nearby evidence; coarse NarI-to-NarH-to-NarG direction is supported without asserting individual redox-state transitions. Unconnected product nodes do not alone establish a scientific defect.

### Taxonomy, evidence tier and optional content

scope: supported. Targets: GO:0044799.

The canonical example and imported assembly are explicitly E. coli K-12. No distribution census, imaging, quantitative measurement, trait, regulatory module or transcriptomics dataset is asserted. Missing optional slots do not justify invented findings.

### Bibliographic attribution and identifiers

provenance: concern. Targets: GO:0044799.

All native stable references resolve, but four notes misname authors of two correctly identified secondary reviews. Correct attribution is Richardson et al.2001 and Rothery et al.2008; retain matching PMID, DOI, title and print year. The defect does not invalidate the separately supported biology.

### Maintained owner, history and status

ownership: supported. Targets: GO:0044799.

Entire native record, append-only creation history and legacy clean review were inspected. Native YAML is the future correction owner. PROPOSED status and every prior record/history/review byte remain unchanged.

## Findings

### F1: Correct author attribution for two review citations

minor / open / confirmed; issue key: narghi-review-author-attribution.

Four top-level evidence notes misattribute correctly identified review articles. PMID11289299 / DOI10.1007/PL00000845 is Richardson, Berks, Russell, Spiro and Taylor (2001), not Moreno-Vivian et al. PMID17964535 / DOI10.1016/j.bbamem.2007.09.002 is Rothery, Workun and Weiner (2008 print), not Jormakka et al. Correct only the misleading author wording; the identifiers, titles, print years and independently supported biological claims need not change for this finding.

## Recommended Actions And Acceptance Checks

### A1

Correct the four maintained author notes to Richardson et al.2001 and Rothery et al.2008 while retaining correct IDs, titles and years. Do not alter biology or native review status as part of this correction.

- Both PMID and DOI notes use the verified author attributions; all four affected notes corrected.
- Correct source identifiers, titles and print years preserved; no unsupported biological expansion.
- Guarded write with llm_assisted event and append-only history; status remains PROPOSED.
- Fresh native target checks/QC and lineage-linked successor disposition retaining this stable issue key.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/energy_complex/narghi_complex.yaml; Entire native YAML, creation history and retained 20261002 legacy report | supports | The record assigns PMID11289299 and its DOI to Moreno-Vivian, and PMID17964535 and its DOI to Jormakka. All four top-level notes require author correction; title, identifier and print year are otherwise correct. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044799,GO:0009325,GO:0160182; Full active definitions, names, aspects, synonyms and relationships | supports | Exact NarGHI cellular component, nitrate-reductase-complex parent and quinol-dependent reaction agree. The GO heterotrimeric unit does not exclude a source-scoped dimer of heterotrimers. |
| complex | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1974; Complete function/properties and all seven participant identities, counts, types and source interactor IDs | supports | E. coli K-12 heterohexamer is 2NarG:2NarH:2NarI with 2[3Fe-4S], 8[4Fe-4S], 2Mo-bisMGD and 4heme entries. Every native imported participant identifier, count, type and interactor ID matches current source data. |
| families | InterPro:IPR006468; InterPro:IPR006547; NCBIfam:TIGR00351; Complete entry metadata, descriptions, integrated models and hierarchy fields in three separate snapshots | supports | Alpha and beta nitrate-reductase families and the narI gamma model match the component identities. NarH family also includes NarY and its description retains an older tetramer statement; the native source-scoped count is supported by CPX-1974 instead of that family prose. |
| proteins | UniProtKB:P09152; UniProtKB:P11349; UniProtKB:P11350; All three reviewed entries: names, genes, taxon, function, subunit/cofactor annotations and relevant cross-references | supports | Reviewed E. coli K-12 NarG, NarH and NarI examples agree. NarG carries one [4Fe-4S] plus Mo cofactor, NarH three [4Fe-4S] plus one [3Fe-4S], and NarI two hemes per chain; dimer totals match the import. |
| taxon | NCBITaxon:83333; Full ENA taxonomy response | supports | Escherichia coli K-12 is the correctly identified strain; no broad prevalence or absence claim is made. |
| cofactors | CHEBI:21137; CHEBI:49883; CHEBI:60539; CHEBI:30413; ECO:0000353; Active OLS records: names, definitions and obsolete flags | supports | The four cofactor terms and physical-interaction evidence code resolve to the imported source labels. The oxo-cofactor identifier is a CPX source assertion, not a claim of the exact ligand/redox state in the structural experiment. |
| bertero-abstract | DOI:10.1038/nsb969; Complete PMID12910261 abstract and verified DOI/title/authors | supports | The primary structural study supports the architecture and a cofactor-based route for respiratory electron transfer. |
| bertero-body | https://www.researchgate.net/publication/10620539_Insights_into_the_respiratory_electron_transfer_pathway_from_the_structure_of_nitrate_reductase_A; Author-uploaded paper text: pages681-685, including NarG/NarH/NarI sections; later discussion/methods and figure pixels not inspected | supports | E. coli NarGHI has membrane-anchored NarI and cytoplasmic NarGH. The structural arrangement supports a plausible quinol-to-nitrate electron route through hemes, iron-sulfur centers and Mo. Dimerization is supported by the crystal interface and detergent light scattering. This is not direct visualization of electron motion. |
| richardson | https://pubmed.ncbi.nlm.nih.gov/11289299/; Full PubMed author list, title and abstract; secondary review, not a new primary experiment | refutes | Authors are Richardson DJ, Berks BC, Russell DA, Spiro S and Taylor CJ (2001), not Moreno-Vivian. The review concerns diversity of prokaryotic nitrate reductases. |
| richardson-doi | https://api.crossref.org/works/10.1007/PL00000845; Complete title, author list, DOI and publication dates | refutes | Crossref independently agrees with Richardson as first author and the native title/DOI/year. |
| rothery | https://pubmed.ncbi.nlm.nih.gov/17964535/; Full PubMed author list, title and abstract; secondary review, not a new primary experiment | refutes | Authors are Rothery RA, Workun GJ and Weiner JH, not Jormakka. Print year2008 is correct despite2007 online publication. |
| rothery-doi | https://api.crossref.org/works/10.1016/j.bbamem.2007.09.002; Complete title, author list, DOI and publication dates | refutes | Crossref independently confirms Rothery, Workun and Weiner and the native review title, DOI and2008 print year. |
| adapter | https://imodulondb.org/; Fresh28-dataset inventory and exact narG/narH/narI searches in e_coli/precise1k | supports | Gene hits are e_coli/precise1k/b1224, b1225 and b1227 respectively; no iModulon-name hits informed the verdict. No expression-module, assembly or negative biological inference is drawn. |
| validation | /private/tmp/csm-review-20261012T082415Z-nar/baseline-verification.json; Fresh target checks and hash-verified broader check reuse on unchanged inputs | supports | Schema and strict checks pass. Zero of38 citations carry snippets, so that check is not full-text validation. Wider QC987passed/3skipped, cached traits, label-adapter skips, live CURIE check and prior200-bundle archive/four contract tests are explicitly reused, not new CI. |
| predecessors | reviews/structured/; Ignored-inclusive canonical inventory and rg -uu across reviews/reports/history/research/curation | supports | No canonical predecessor for this target among200 bundles. The retained legacy clean report is historical context, not a disposition of this newly observed author error. No existing use of the new issue key found. |

## Limits And Additional Notes

- Same-agent review, not independent human sign-off or an exhaustive literature/retraction survey.
- Bertero2003 complete abstract and relevant author-uploaded body text on pages681-685 were inspected. Remaining discussion/methods, raw figure pixels, raw data and later literature were not exhaustively reviewed. Publisher page was unavailable; no local PDF snapshot hash is claimed for web-read body text.
- Richardson2001 and Rothery2008 were inspected as full bibliographic metadata and complete secondary-review abstracts, not complete review bodies or new primary experiments.
- IPR006547 includes related beta subunits and retains older oligomer wording; the native assembly count is explicitly taken from CPX-1974 and is supported by the inspected primary study. Imported cofactor identifiers are not experimental redox-state measurements.
- Fresh target checks; wider checks reused after hash verification with original caches/skips. No fresh GitHub CI, publication, issues, PR or merge. Existing publication approval remains unanswered.
- Issue-only observation changes no native record, generated artifact, history or scientific status. Legacy clean review remains historical and is not overwritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T083110Z-narghi-review-author-attribution
kind: record
repository: CultureBotAI/CellStructureMech
title: NarGHI literature author-attribution review
started_at: '2026-10-12T08:24:42Z'
finished_at: '2026-10-12T08:31:10Z'
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
summary: Whole-record scientific review completed with one minor provenance finding
  covering four author-misattribution notes for two secondary reviews. Structure identity,
  component roles, source-scoped composition and all five coarse graph edges are supported
  within the recorded source-reading limits.
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
  - path: data/structures/energy_complex/narghi_complex.yaml
    sha256: 8bae0def8ab7c219e6fccc6d33a10c8918ba2f3b79996f5506d55dd7b64596d5
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
  - path: history/records/narghi_complex/2026-10-02T042057Z-codex-34a26c.yaml
    sha256: 6290169e8059057ef26fefcf12859041ea86751c49604c09a0ca3bfb87879576
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20261002T043308Z-narghi_complex.md
    sha256: 5aab9fb44c7a5ecd35fd542ca5474611f5644fce40200d81af04068a5360261a
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
- target_id: GO:0044799
  path: data/structures/energy_complex/narghi_complex.yaml
  label: NarGHI complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/narghi_complex.yaml
    role: maintained scientific record
scope:
  description: One entire native record, every material assertion, all five graph
    edges, all seven imported participants, creation history and retained legacy review;
    no sampling.
  selection: data/structures/energy_complex/narghi_complex.yaml
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0044799
checks:
- check_id: schema
  name: schema
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/narghi_complex.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target check; actual UTC/log receipts retained. '
  target_ids:
  - GO:0044799
  evidence_ids:
  - validation
- check_id: strict
  name: strict
  command: .venv/bin/python scripts/validate_strict.py data/structures/energy_complex/narghi_complex.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target check; actual UTC/log receipts retained. '
  target_ids:
  - GO:0044799
  evidence_ids:
  - validation
- check_id: snippets
  name: snippets
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/energy_complex/narghi_complex.yaml
    --report /private/tmp/csm-review-20261012T082415Z-nar/snippets.md
  exit_code: 0
  status: passed
  required: true
  summary: Fresh target check; actual UTC/log receipts retained. Zero of38 citations
    carry snippets; not a full-text check.
  target_ids:
  - GO:0044799
  evidence_ids:
  - validation
- check_id: reused-release-qc
  name: reused-release-qc
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  status: passed
  required: true
  summary: Reused actual result from 2026-10-12T06:45:16Z on hash-verified unchanged
    inputs. QC987passed/3skipped; labels603 no-adapter skips; trait index cached.
    Not a fresh execution or CI result.
  target_ids:
  - GO:0044799
  evidence_ids:
  - validation
- check_id: reused-release-labels
  name: reused-release-labels
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  status: passed
  required: true
  summary: Reused actual result from 2026-10-12T06:47:16Z on hash-verified unchanged
    inputs. QC987passed/3skipped; labels603 no-adapter skips; trait index cached.
    Not a fresh execution or CI result.
  target_ids:
  - GO:0044799
  evidence_ids:
  - validation
- check_id: reused-release-traits
  name: reused-release-traits
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  status: passed
  required: true
  summary: Reused actual result from 2026-10-12T06:48:52Z on hash-verified unchanged
    inputs. QC987passed/3skipped; labels603 no-adapter skips; trait index cached.
    Not a fresh execution or CI result.
  target_ids:
  - GO:0044799
  evidence_ids:
  - validation
- check_id: reused-curies-live
  name: reused-curies-live
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  status: passed
  required: true
  summary: Reused actual result from 2026-10-12T07:10:58Z; log and unchanged maintained
    inputs verified. Live CURIE4023OK/251skips, archive200valid, contract4passed.
    Fresh post-save archive/contract checks follow separately.
  target_ids:
  - GO:0044799
  evidence_ids:
  - validation
- check_id: reused-post-save-archive
  name: reused-post-save-archive
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  status: passed
  required: true
  summary: Reused actual result from 2026-10-12T08:18:57Z; log and unchanged maintained
    inputs verified. Live CURIE4023OK/251skips, archive200valid, contract4passed.
    Fresh post-save archive/contract checks follow separately.
  target_ids:
  - GO:0044799
  evidence_ids:
  - validation
- check_id: reused-post-save-contract
  name: reused-post-save-contract
  command: .venv/bin/pytest -q tests/test_record_review_contract.py
  exit_code: 0
  status: passed
  required: true
  summary: Reused actual result from 2026-10-12T08:20:34Z; log and unchanged maintained
    inputs verified. Live CURIE4023OK/251skips, archive200valid, contract4passed.
    Fresh post-save archive/contract checks follow separately.
  target_ids:
  - GO:0044799
  evidence_ids:
  - validation
- check_id: adapter-datasets
  name: adapter-datasets
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  status: passed
  required: false
  summary: Fresh inventory or exact gene search; bounded gene hits only, no biological
    absence inference.
  target_ids:
  - GO:0044799
  evidence_ids:
  - adapter
- check_id: adapter-narG
  name: adapter-narG
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query narG
  exit_code: 0
  status: passed
  required: false
  summary: Fresh inventory or exact gene search; bounded gene hits only, no biological
    absence inference.
  target_ids:
  - GO:0044799
  evidence_ids:
  - adapter
- check_id: adapter-narH
  name: adapter-narH
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query narH
  exit_code: 0
  status: passed
  required: false
  summary: Fresh inventory or exact gene search; bounded gene hits only, no biological
    absence inference.
  target_ids:
  - GO:0044799
  evidence_ids:
  - adapter
- check_id: adapter-narI
  name: adapter-narI
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query narI
  exit_code: 0
  status: passed
  required: false
  summary: Fresh inventory or exact gene search; bounded gene hits only, no biological
    absence inference.
  target_ids:
  - GO:0044799
  evidence_ids:
  - adapter
- check_id: draft-contract-corrected
  name: Initial draft contract validation
  command: .venv/bin/python scripts/record_review.py validate /private/tmp/csm-review-20261012T082415Z-nar/observation.yaml
  exit_code: 1
  status: failed
  required: false
  summary: Initial draft used unsupported assessment area composition. Corrected to
    evidence for component identity/roles and quantity for assembly counts. Scientific
    assessment unchanged; corrected draft separately validated before save.
  target_ids:
  - GO:0044799
  evidence_ids:
  - validation
evidence:
- evidence_id: native
  kind: record_content
  reference: data/structures/energy_complex/narghi_complex.yaml
  locator: Entire native YAML, creation history and retained 20261002 legacy report
  summary: The record assigns PMID11289299 and its DOI to Moreno-Vivian, and PMID17964535
    and its DOI to Jormakka. All four top-level notes require author correction; title,
    identifier and print year are otherwise correct.
  support: supports
  accessed_at: '2026-10-12T08:30:43Z'
  snapshot_sha256: 8bae0def8ab7c219e6fccc6d33a10c8918ba2f3b79996f5506d55dd7b64596d5
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044799,GO:0009325,GO:0160182
  locator: Full active definitions, names, aspects, synonyms and relationships
  summary: Exact NarGHI cellular component, nitrate-reductase-complex parent and quinol-dependent
    reaction agree. The GO heterotrimeric unit does not exclude a source-scoped dimer
    of heterotrimers.
  support: supports
  accessed_at: '2026-10-12T08:24:44Z'
  snapshot_sha256: 07f38aea93fa8fad94b502c4e45363127b7b2fddd7b4c2052ec12b3a203e147d
- evidence_id: complex
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1974
  locator: Complete function/properties and all seven participant identities, counts,
    types and source interactor IDs
  summary: E. coli K-12 heterohexamer is 2NarG:2NarH:2NarI with 2[3Fe-4S], 8[4Fe-4S],
    2Mo-bisMGD and 4heme entries. Every native imported participant identifier, count,
    type and interactor ID matches current source data.
  support: supports
  accessed_at: '2026-10-12T08:24:45Z'
  snapshot_sha256: 06b91684910e1ee11bb247f8ff505e3fa7a4a95ff7f26574221738023eb68d61
- evidence_id: families
  kind: authority
  reference: InterPro:IPR006468; InterPro:IPR006547; NCBIfam:TIGR00351
  locator: Complete entry metadata, descriptions, integrated models and hierarchy
    fields in three separate snapshots
  summary: Alpha and beta nitrate-reductase families and the narI gamma model match
    the component identities. NarH family also includes NarY and its description retains
    an older tetramer statement; the native source-scoped count is supported by CPX-1974
    instead of that family prose.
  support: supports
  accessed_at: '2026-10-12T08:30:43Z'
- evidence_id: proteins
  kind: database
  reference: UniProtKB:P09152; UniProtKB:P11349; UniProtKB:P11350
  locator: 'All three reviewed entries: names, genes, taxon, function, subunit/cofactor
    annotations and relevant cross-references'
  summary: Reviewed E. coli K-12 NarG, NarH and NarI examples agree. NarG carries
    one [4Fe-4S] plus Mo cofactor, NarH three [4Fe-4S] plus one [3Fe-4S], and NarI
    two hemes per chain; dimer totals match the import.
  support: supports
  accessed_at: '2026-10-12T08:30:43Z'
- evidence_id: taxon
  kind: authority
  reference: NCBITaxon:83333
  locator: Full ENA taxonomy response
  summary: Escherichia coli K-12 is the correctly identified strain; no broad prevalence
    or absence claim is made.
  support: supports
  accessed_at: '2026-10-12T08:24:46Z'
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: cofactors
  kind: authority
  reference: CHEBI:21137; CHEBI:49883; CHEBI:60539; CHEBI:30413; ECO:0000353
  locator: 'Active OLS records: names, definitions and obsolete flags'
  summary: The four cofactor terms and physical-interaction evidence code resolve
    to the imported source labels. The oxo-cofactor identifier is a CPX source assertion,
    not a claim of the exact ligand/redox state in the structural experiment.
  support: supports
  accessed_at: '2026-10-12T08:30:43Z'
- evidence_id: bertero-abstract
  kind: primary_source
  reference: DOI:10.1038/nsb969
  locator: Complete PMID12910261 abstract and verified DOI/title/authors
  summary: The primary structural study supports the architecture and a cofactor-based
    route for respiratory electron transfer.
  support: supports
  accessed_at: '2026-10-12T08:24:46Z'
  snapshot_sha256: 7f8c395f38db5be890932b6c406f4e78ce4380115fe445e04055de53ad345339
- evidence_id: bertero-body
  kind: primary_source
  reference: https://www.researchgate.net/publication/10620539_Insights_into_the_respiratory_electron_transfer_pathway_from_the_structure_of_nitrate_reductase_A
  locator: 'Author-uploaded paper text: pages681-685, including NarG/NarH/NarI sections;
    later discussion/methods and figure pixels not inspected'
  summary: E. coli NarGHI has membrane-anchored NarI and cytoplasmic NarGH. The structural
    arrangement supports a plausible quinol-to-nitrate electron route through hemes,
    iron-sulfur centers and Mo. Dimerization is supported by the crystal interface
    and detergent light scattering. This is not direct visualization of electron motion.
  support: supports
  accessed_at: '2026-10-12T08:30:43Z'
- evidence_id: richardson
  kind: authority
  reference: https://pubmed.ncbi.nlm.nih.gov/11289299/
  locator: Full PubMed author list, title and abstract; secondary review, not a new
    primary experiment
  summary: Authors are Richardson DJ, Berks BC, Russell DA, Spiro S and Taylor CJ
    (2001), not Moreno-Vivian. The review concerns diversity of prokaryotic nitrate
    reductases.
  support: refutes
  accessed_at: '2026-10-12T08:24:46Z'
  snapshot_sha256: 7f8c395f38db5be890932b6c406f4e78ce4380115fe445e04055de53ad345339
- evidence_id: richardson-doi
  kind: authority
  reference: https://api.crossref.org/works/10.1007/PL00000845
  locator: Complete title, author list, DOI and publication dates
  summary: Crossref independently agrees with Richardson as first author and the native
    title/DOI/year.
  support: refutes
  accessed_at: '2026-10-12T08:24:56Z'
  snapshot_sha256: fd75bb187f41395372419882e6186e3e0e60e16468f2a07d5c066dbdb0a524ff
- evidence_id: rothery
  kind: authority
  reference: https://pubmed.ncbi.nlm.nih.gov/17964535/
  locator: Full PubMed author list, title and abstract; secondary review, not a new
    primary experiment
  summary: Authors are Rothery RA, Workun GJ and Weiner JH, not Jormakka. Print year2008
    is correct despite2007 online publication.
  support: refutes
  accessed_at: '2026-10-12T08:24:46Z'
  snapshot_sha256: 7f8c395f38db5be890932b6c406f4e78ce4380115fe445e04055de53ad345339
- evidence_id: rothery-doi
  kind: authority
  reference: https://api.crossref.org/works/10.1016/j.bbamem.2007.09.002
  locator: Complete title, author list, DOI and publication dates
  summary: Crossref independently confirms Rothery, Workun and Weiner and the native
    review title, DOI and2008 print year.
  support: refutes
  accessed_at: '2026-10-12T08:24:57Z'
  snapshot_sha256: f980b093816f8f0f1d70bf8236e485cd309af55df379dbd0b1b38e4757e33d4a
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/
  locator: Fresh28-dataset inventory and exact narG/narH/narI searches in e_coli/precise1k
  summary: Gene hits are e_coli/precise1k/b1224, b1225 and b1227 respectively; no
    iModulon-name hits informed the verdict. No expression-module, assembly or negative
    biological inference is drawn.
  support: supports
  accessed_at: '2026-10-12T08:30:43Z'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/csm-review-20261012T082415Z-nar/baseline-verification.json
  locator: Fresh target checks and hash-verified broader check reuse on unchanged
    inputs
  summary: Schema and strict checks pass. Zero of38 citations carry snippets, so that
    check is not full-text validation. Wider QC987passed/3skipped, cached traits,
    label-adapter skips, live CURIE check and prior200-bundle archive/four contract
    tests are explicitly reused, not new CI.
  support: supports
  accessed_at: '2026-10-12T08:30:43Z'
- evidence_id: predecessors
  kind: search
  reference: reviews/structured/
  locator: Ignored-inclusive canonical inventory and rg -uu across reviews/reports/history/research/curation
  summary: No canonical predecessor for this target among200 bundles. The retained
    legacy clean report is historical context, not a disposition of this newly observed
    author error. No existing use of the new issue key found.
  support: supports
  accessed_at: '2026-10-12T08:30:43Z'
  search_scope: Path.rglob includes hidden/ignored canonical bundles; rg -uu searched
    target slug, label, GO identifier, primary DOI/PMID and new issue key in reviews,
    reports, history, research and curation. No GitHub-wide absence claim.
assessments:
- assessment_id: identity
  area: identity
  topic: Identity, definition, synonyms and parentage
  outcome: supported
  summary: Native GO identity denotes the respiratory NarGHI complex rather than NarG
    alone, assimilatory reductase or periplasmic Nap. Component kind, energy category,
    exact synonyms and is-a parent agree.
  target_ids:
  - GO:0044799
  evidence_ids:
  - native
  - go
  - complex
- assessment_id: components
  area: evidence
  topic: Families, roles and protein examples
  outcome: supported
  summary: All three native family groundings and reviewed E. coli examples agree
    with the intended constituent roles. ESSENTIAL is read as assembly membership,
    not cell viability. Family-level annotations are not substituted for experimental
    stoichiometry.
  target_ids:
  - GO:0044799
  evidence_ids:
  - native
  - families
  - proteins
  - complex
- assessment_id: assembly
  area: quantity
  topic: Taxon-scoped complex composition and cofactors
  outcome: supported
  summary: All seven CPX participant rows match. Heterotrimeric unit and dimeric heterohexamer
    are compatible levels of assembly. The source-scoped E. coli count is not universalized;
    generic cofactor identity is distinguished from exact experimental coordination/redox
    state.
  target_ids:
  - GO:0044799
  evidence_ids:
  - complex
  - cofactors
  - taxon
  - proteins
  - bertero-body
  dimensions:
  - name: assembly_scope
    value: Escherichia coli K-12; CPX-1974 heterohexamer
    definition: Source-specific dimer of NarGHI heterotrimers, not a universal oligomer
      count.
    evidence_ids:
    - complex
    - taxon
  - name: evidence_tier
    value: Curated complex composition plus primary structural evidence
    definition: Authority identity/counts, structural organization and functional
      interpretation are distinguished.
    evidence_ids:
    - complex
    - bertero-body
- assessment_id: function
  area: evidence
  topic: Reaction and all five NONMECHANISTIC graph edges
  outcome: supported
  summary: Quinol oxidation coupled to nitrate reduction agrees with the GO reaction.
    Each native edge has relevant nearby evidence; coarse NarI-to-NarH-to-NarG direction
    is supported without asserting individual redox-state transitions. Unconnected
    product nodes do not alone establish a scientific defect.
  target_ids:
  - GO:0044799
  evidence_ids:
  - native
  - go
  - complex
  - bertero-abstract
  - bertero-body
- assessment_id: scope
  area: scope
  topic: Taxonomy, evidence tier and optional content
  outcome: supported
  summary: The canonical example and imported assembly are explicitly E. coli K-12.
    No distribution census, imaging, quantitative measurement, trait, regulatory module
    or transcriptomics dataset is asserted. Missing optional slots do not justify
    invented findings.
  target_ids:
  - GO:0044799
  evidence_ids:
  - native
  - taxon
  - complex
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Bibliographic attribution and identifiers
  outcome: concern
  summary: All native stable references resolve, but four notes misname authors of
    two correctly identified secondary reviews. Correct attribution is Richardson
    et al.2001 and Rothery et al.2008; retain matching PMID, DOI, title and print
    year. The defect does not invalidate the separately supported biology.
  target_ids:
  - GO:0044799
  evidence_ids:
  - native
  - richardson
  - richardson-doi
  - rothery
  - rothery-doi
- assessment_id: ownership
  area: ownership
  topic: Maintained owner, history and status
  outcome: supported
  summary: Entire native record, append-only creation history and legacy clean review
    were inspected. Native YAML is the future correction owner. PROPOSED status and
    every prior record/history/review byte remain unchanged.
  target_ids:
  - GO:0044799
  evidence_ids:
  - native
  - predecessors
  - validation
findings:
- finding_id: F1
  issue_key: narghi-review-author-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct author attribution for two review citations
  description: Four top-level evidence notes misattribute correctly identified review
    articles. PMID11289299 / DOI10.1007/PL00000845 is Richardson, Berks, Russell,
    Spiro and Taylor (2001), not Moreno-Vivian et al. PMID17964535 / DOI10.1016/j.bbamem.2007.09.002
    is Rothery, Workun and Weiner (2008 print), not Jormakka et al. Correct only the
    misleading author wording; the identifiers, titles, print years and independently
    supported biological claims need not change for this finding.
  target_ids:
  - GO:0044799
  field_paths:
  - evidence[reference=PMID:11289299].notes
  - evidence[reference=DOI:10.1007/PL00000845].notes
  - evidence[reference=PMID:17964535].notes
  - evidence[reference=DOI:10.1016/j.bbamem.2007.09.002].notes
  evidence_ids:
  - native
  - richardson
  - richardson-doi
  - rothery
  - rothery-doi
  rule_id: review-checklist:source-identity-and-provenance
  native_severity: minor
  normalization_reason: Bounded non-blocking bibliographic attribution defect. Correct
    source identifiers and titles resolve; the defect does not establish wrong structure
    identity or unsupported mechanism.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/narghi_complex.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Correct the four maintained author notes to Richardson et al.2001 and
    Rothery et al.2008 while retaining correct IDs, titles and years. Do not alter
    biology or native review status as part of this correction.
  finding_ids:
  - F1
  target_ids:
  - GO:0044799
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/narghi_complex.yaml
    role: maintained scientific record
  generator: Native guarded writer and documented product workflow when required.
  acceptance_checks:
  - Both PMID and DOI notes use the verified author attributions; all four affected
    notes corrected.
  - Correct source identifiers, titles and print years preserved; no unsupported biological
    expansion.
  - Guarded write with llm_assisted event and append-only history; status remains
    PROPOSED.
  - Fresh native target checks/QC and lineage-linked successor disposition retaining
    this stable issue key.
limitations:
- Same-agent review, not independent human sign-off or an exhaustive literature/retraction
  survey.
- Bertero2003 complete abstract and relevant author-uploaded body text on pages681-685
  were inspected. Remaining discussion/methods, raw figure pixels, raw data and later
  literature were not exhaustively reviewed. Publisher page was unavailable; no local
  PDF snapshot hash is claimed for web-read body text.
- Richardson2001 and Rothery2008 were inspected as full bibliographic metadata and
  complete secondary-review abstracts, not complete review bodies or new primary experiments.
- IPR006547 includes related beta subunits and retains older oligomer wording; the
  native assembly count is explicitly taken from CPX-1974 and is supported by the
  inspected primary study. Imported cofactor identifiers are not experimental redox-state
  measurements.
- Fresh target checks; wider checks reused after hash verification with original caches/skips.
  No fresh GitHub CI, publication, issues, PR or merge. Existing publication approval
  remains unanswered.
- Issue-only observation changes no native record, generated artifact, history or
  scientific status. Legacy clean review remains historical and is not overwritten.
tags:
- scientific-review
- energy-complex
- provenance
- minor
```
