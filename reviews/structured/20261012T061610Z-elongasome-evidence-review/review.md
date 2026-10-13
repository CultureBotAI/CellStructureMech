# elongasome whole-record evidence review

- Review: 20261012T061610Z-elongasome-evidence-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T06:04:07Z
- Finished UTC: 2026-10-12T06:16:10Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review found 4 concrete major issues in evidence, mechanism or scope. Observation saved before native curation; source-reading limits are explicit.

## Scope And Provenance

Every material assertion in the entire maintained record, with identifier, history, source and validator checks.

Selection: data/structures/division_machinery/elongasome.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 937ba6254eb987adcbd92e82b21b2ce8651dc5e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:elongasome | data/structures/division_machinery/elongasome.yaml | maintained | elongasome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| elongasome-schema | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| elongasome-strict | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| elongasome-snippets | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| pathway-links | failed | False | cellstructuremech:elongasome | Unsupported --check invocation; corrected invocation is separately recorded as passed. |
| pathway-links-corrected | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| history | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| labels | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| curies | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| traits | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| reviews | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| contract | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| diff | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |
| baseline-ci | passed | True | cellstructuremech:elongasome | Actual exit0. Deterministic validation does not establish scientific support. |

## Scientific And Domain Assessments

### Identity, synonyms and class

identity: concern. Targets: cellstructuremech:elongasome.

Distinct local elongasome/Rod-complex identity, class and membrane-complex parent are appropriate, but definition and synonym evidence require the2016 primary sources. Bounded ontology queries do not establish global term absence.

### Hierarchy and parthood

grounding: concern. Targets: cellstructuremech:elongasome.

Plasma-membrane-protein-complex parent is valid; peptidoglycan wall product is not valid parthood.

### Component roles, essentiality and examples

evidence: concern. Targets: cellstructuremech:elongasome.

RodA/PBP2 and MreC/D roles are supported in named model systems. ESSENTIAL is assembly/function scope, not all-organism viability. RodZ has conditional coupling evidence; no new stoichiometry or universal membership is inferred. False RodA source-absence notes need correction.

### Taxonomic distribution and canonical examples

scope: concern. Targets: cellstructuremech:elongasome.

Named E. coli and B. subtilis reference systems are supported. Domain-level occurrence assertions must not transfer a protein or wall chemistry to the entire machine. Removing unsupported rows does not assert the opposite.

### Functions, traits and pathway link

evidence: concern. Targets: cellstructuremech:elongasome.

Sidewall synthesis and WP5060 overlap are supported, not whole-pathway identity. Rod-shape necessity requires bounded model-system interpretation and exceptions.

### Mechanism and experimental limits

graph: concern. Targets: cellstructuremech:elongasome.

Separate MreB rotation from synthase movement and synthesis output; retain perturbation contexts, suppressor exceptions and direction-of-evidence limits.

### Measurements, discussions and optional content

completeness: supported. Targets: cellstructuremech:elongasome.

No optional physical measurement or image is required. The guided-by-MreB relation discussion remains legitimate; definition-source TODO has actionable primary evidence. Component inventory is not a complete stoichiometric model.

### Provenance, prior issues and ownership

ownership: supported. Targets: cellstructuremech:elongasome.

No native change preceded this observation. Historical statements remain history, even where mistaken. Corrections belong in the maintained target with guarded writer and new events; earlier reports and62 untracked legacy reports remain untouched.

## Findings

### F1: Finish the deferred RodA definition and synonym evidence correction

major / open / confirmed; issue key: elongasome-definition-source-residual.

The definition still attributes the2016 RodA SEDS-polymerase finding to Typas2011, and the narrow RodA-PBP2 synonym cites a review not establishing that pair. Current RodA notes and the open discussion also falsely say Typas never mentions RodA: its Table1 does. Closed161 fixed only the component, explicitly leaving the definition.

### F2: Remove peptidoglycan-wall parthood from its synthesis machine

major / open / confirmed; issue key: elongasome-wall-parthood.

part_of GO0009274 makes the membrane protein machine a constituent of the peptidoglycan wall product. The GO definition and inspected wall-synthesis sources distinguish wall material from the membrane-associated complex that synthesizes it.

### F3: Separate MreB rotation, synthase movement and conditional shape phenotypes

major / open / confirmed; issue key: elongasome-motion-and-shape-scope.

The graph names measured MreB rotation as whole-complex motion, treats RodZ as required for it and implies movement produces rod shape. The cited Shi review and Morgenstein primary abstract explicitly report rod-shaped suppressors without MreB rotation. The record-wide REQUIRED_FOR rod-shape trait also ignores MreB-independent rod-shaped lineages discussed by its sources.

### F4: Remove an unsupported domain-wide negative occurrence claim

major / open / confirmed; issue key: elongasome-archaeal-negative-evidence.

The Archaea ABSENT row infers absence of the defined complex from an uncited domain-wide wall statement, attributed to a bacterial review that does not establish the archaeal claim. The primary archaeal comparison distinguishes pseudomurein from bacterial PG, but does not assay absence of every Rod-complex component or all archaeal taxa.

## Recommended Actions And Acceptance Checks

### A1

Rebase the bounded definition and synonym references on inspected2016 primary evidence; distinguish RodA being mentioned from its polymerase activity being established; resolve the deferred discussion while preserving historical rationale/date and append-only events.

- The affected native assertions and rendered graph/prose agree with the cited bounded evidence.
- Guarded write, append-only history, PROPOSED status and previous history are preserved.
- Fresh full QC, direct target checks and successor dispositions pass.

### A2

Remove this unsupported parthood assertion, retain the supported plasma-membrane-protein-complex is-a parent, and do not guess replacement parthood.

- The affected native assertions and rendered graph/prose agree with the cited bounded evidence.
- Guarded write, append-only history, PROPOSED status and previous history are preserved.
- Fresh full QC, direct target checks and successor dispositions pass.

### A3

Name MreB rotation separately from RodA/PBP2 motion, qualify perturbation-derived edges and suppressor exceptions, and weaken universal shape necessity to a model-system-scoped association with direct evidence.

- The affected native assertions and rendered graph/prose agree with the cited bounded evidence.
- Guarded write, append-only history, PROPOSED status and previous history are preserved.
- Fresh full QC, direct target checks and successor dispositions pass.

### A4

Remove the unsupported ABSENT row without asserting presence; retain a bounded bacterial distribution and explain that absence of a curated row is not biological absence.

- The affected native assertions and rendered graph/prose agree with the cited bounded evidence.
- Guarded write, append-only history, PROPOSED status and previous history are preserved.
- Fresh full QC, direct target checks and successor dispositions pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/division_machinery/elongasome.yaml; Entire captured YAML and inline history; repository history and generated-page headings | supports | Pre-curation record inspected in full; concrete issues enumerated below. Source hash captures the unchanged native bytes. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990586,GO:0098797,GO:0009274; Eight live GO identifiers, definitions, aspects and obsolete flags | supports | Divisome exact identity and division-site parthood are coherent. GO0098797 is a plasma membrane protein complex. GO0009274 denotes the peptidoglycan wall, not its synthesis machinery. Function CURIEs resolve. |
| typas | DOI:10.1038/nrmicro2677; Author review full-text JATS: Introduction, synthesis and cytoskeletal sections; complete Table1 and Figure2 legend | supports | The 2011-online review distinguishes wall material from synthetic complexes and describes MreB motion inhibition in E. coli and B. subtilis. Table1 explicitly includes RodA with its then-proposed flippase assignment. It does not establish the later RodA polymerase discovery. Review evidence is secondary, not a new primary experiment. |
| shi | DOI:10.1016/j.cell.2018.02.050; Complete main review body, 42207 characters, including exception and RodZ sections | supports | Review distinguishes MreB-guided growth from MreB-independent rod-shaped lineages. RodZ deletion impairs MreB rotation in ordinary E. coli backgrounds, but suppressors can restore rod shape without rotation. It does not establish that all complex motion is necessary for rod shape. Secondary synthesis, not primary experimental evidence. |
| meeske | DOI:10.1038/nature19331; Complete Introduction, Results and Discussion; start of Methods (first15000 body characters) | supports | B. subtilis genetic, biochemical and imaging experiments establish RodA as a SEDS peptidoglycan polymerase in the Rod complex. This is the post-2011 primary source already attached to the component, but not to the current definition. |
| cho | DOI:10.1038/nmicrobiol.2016.172; Complete main Introduction, Results and Discussion plus start of Methods (first16500 body characters) | supports | E. coli radiolabeling, specific synthase inhibition and imaging distinguish RodA/PBP2 synthesis from semi-autonomous aPBPs. RodA and PBP2 show MreB-like directional motion; inhibiting RodA activity halts MreB rotation. The wall product and membrane machine are distinct. |
| morgenstein | DOI:10.1073/pnas.1509610112; Complete primary abstract PMID26396257; full Methods unavailable in attempted public routes | supports | RodZ couples MreB rotation to wall synthesis. Suppressor mutations restore rod shape without rotation under standard laboratory conditions; rotation promotes robustness to wall stress. Not proof that all synthase motion is absent. |
| mcquillen | DOI:10.1146/annurev-biophys-121219-081703; Entire review body63919 characters; radial-thickness and two-track sections reread | supports | Secondary review explicitly distinguishes a fast FtsZ-dependent inactive FtsW population from a slow synthesis-dependent active population in E. coli. It gives method-dependent ring radial-thickness estimates and summarizes C. crescentus filament dimensions. Its approximately13nm membrane-spacing statement differs from the inspected primary16nm peak-to-peak experiment. |
| pende | DOI:10.1038/s41467-021-23099-8; Verified PMID34088904; entire Introduction and Discussion, first Results localization section | supports | M. smithii has an archaeal FtsZ/SepF division system and pseudomurein wall chemically distinct from bacterial peptidoglycan. Shared FtsZ does not establish occurrence of the bacterial FtsW/FtsI PG machine. Removing an occurrence assertion is not asserting no archaeal divisomes. |
| bibliography | https://pubmed.ncbi.nlm.nih.gov/; 15 complete native primary abstracts and identities; five Crossref records and EuropePMC DOI records | supports | Native FtsZ/FtsA/ZipA/SepF/FtsW/FtsI and RodA/PBP2/MreC/D/RodZ identity/localization references match. Abstract-only evidence remains bounded. Online versus issue year differences are not errors; metadata inspection is not exhaustive retraction screening. |
| authorities | https://rest.uniprot.org/uniprotkb/; 11 full JSON entry identity fields; six ENA taxon identities; OLS nanometer; pinned WP5060 hash | supports | All11 accessions match named reviewed proteins and taxa. RodA alias maps to mrdB and PBP2 to mrdA. These are identity checks, not independent membership proof. Existing WP5060 links remain organism- and segment-scoped; E. coli PBP2 entries are not equated. |
| adapter | https://imodulondb.org/; Installed adapter28-dataset inventory; precise1k ftsZ,rodZ,rodA,mrdB and B.subtilis sepF queries | supports | Covered gene hits confirm useful keys but return no informative iModulon hit for these queries. No module summary is warranted. Alias lookup miss for rodA was followed through mrdB; it is not biological absence. |
| prior | https://github.com/CultureBotAI/CellStructureMech/issues/161; All-state name searches and issues64,65,66,102,119,120,161;191 canonical bundles scanned including ignored/hidden paths under reviews/structured | supports | No exact-ID/path canonical predecessor for either target. Closed161 corrected RodA component evidence but explicitly deferred the definition; this is a residual defect, not a claim that the earlier fix never happened. Guided-by schema discussion and earlier pathway fixes remain intact. |
| baseline-qc | https://github.com/CultureBotAI/CellStructureMech/actions/runs/38208737726; Successful exact-base merge-group QC and checksum-verified complete cached log | supports | Baseline937ba6254eb987adcbd92e82b21b2ce8651dc5e3 passed987 tests with3 skips,909 strict records,1724 histories. Target schema/strict/snippets and current global checks are separately recorded. This is unchanged-base CI reuse, not a new local full run. |

## Limits And Additional Notes

- Same-agent assessment, not human sign-off, raw image reanalysis, a new measurement or exhaustive literature search. Abstract-only native protein references support only statements present in those abstracts.
- Typas review synthesis/cytoskeleton sections and complete Table1/Figure2 legend inspected, not every mechanics/metabolic paragraph. Shi and McQuillen complete main bodies inspected. Meeske and Cho complete main Results/Discussion but not all Methods/supplements. Reviews are secondary evidence even when the shared evidence kind is primary_source (directly inspected source).
- Yang2021 complete Results/Discussion and start Statistics; Yang2017 entire main body; BissonFilho main Results and initial Methods. No new speed estimate is inferred from uninspected figure pixels.
- Li2007 publisher Results and Methods, including density-profile method and Figure6 caption, read in full. The review13nm and primary16nm values are kept distinct; their discrepancy is not claimed resolved. No new radial-thickness measurement is curated.
- Pende2021 verified identity, Introduction/Discussion and localization Results inspected, not all structural/phylogeny Methods. An accidentally retrieved unrelated PMID34088901 was explicitly rejected and never used. Morgenstein full primary abstract only; unsuccessful full-text attempts are not counted as full reading.
- Some EuropePMC fullText routes returned500, S3 routes404, and web pages showed access challenges. Documented NCBI efetch and legitimate publisher/institutional routes were used; no challenges bypassed. EganVollmer complete abstract only, not full text.
- The initial pathway checker invocation used unsupported --check and exited2. Its corrected documented invocation passed; both outcomes are retained. Exact-base full CI is reused before mutation; later changes require fresh full QC.
- Identifier/label global checks include documented no-adapter skips; these are not biological verification. Eleven accession identities, six taxa, target GO terms and the nanometer unit were separately inspected. iModulon gene hits are not localization/membership evidence.
- No canonical predecessor in191 bundles under reviews/structured (ignored files included). Bounded ontology and GitHub searches do not prove universal absence. Other context records are not completed by this bundle.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T061610Z-elongasome-evidence-review
kind: record
repository: CultureBotAI/CellStructureMech
title: elongasome whole-record evidence review
started_at: '2026-10-12T06:04:07Z'
finished_at: '2026-10-12T06:16:10Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same coding agent; not independent human review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole-record review found 4 concrete major issues in evidence, mechanism
  or scope. Observation saved before native curation; source-reading limits are explicit.
source:
  git_revision: 937ba6254eb987adcbd92e82b21b2ce8651dc5e3
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
  - path: conf/pathwaymech_targets.json
    sha256: 625e474ce45903a482587deb9b26237088d1298d88a017920a69370c89db5dd0
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/cytoskeleton/mreb_filament.yaml
    sha256: b27d315ff07c11f2aa9eb1f1c1f4c65203ba62509fe6999c7804397e76ab9711
    role: context
  - path: data/structures/division_machinery/elongasome.yaml
    sha256: 905ccf8a905e7074c55451346807afb7057bbb936ea01d71950bf2002268346b
    role: target
  - path: data/structures/envelope/division_septum.yaml
    sha256: 956d96777f95a2db040b1e94d2f2d9be78932ef0dac1c49cefd6b095a148ca80
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
  - path: history/records/elongasome/2026-09-02T235514Z-claude-code-3ca393.yaml
    sha256: b4072723c5ee7df3c62e6e4a38d8bb981af0e055676c422844f9fbdf946fafc2
    role: context
  - path: history/records/elongasome/2026-10-05T174720Z-codex-dc9dd5.yaml
    sha256: 62f6f99e8823038b34ddc11ec598cd987a502d6d11020f7b6a32239220904e90
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: pages/structures/division_machinery/elongasome.html
    sha256: c4c3d3b7d1ab9e0ebc70bfbe7816f7f28bd2ec9e21d0aa65d77e7877bc16cc50
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: cellstructuremech:elongasome
  path: data/structures/division_machinery/elongasome.yaml
  label: elongasome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained scientific record
scope:
  description: Every material assertion in the entire maintained record, with identifier,
    history, source and validator checks.
  selection: data/structures/division_machinery/elongasome.yaml
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:elongasome
checks:
- check_id: elongasome-schema
  name: elongasome-schema
  status: passed
  required: true
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/division_machinery/elongasome.yaml
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: elongasome-strict
  name: elongasome-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/structures/division_machinery/elongasome.yaml
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: elongasome-snippets
  name: elongasome-snippets
  status: passed
  required: true
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/division_machinery/elongasome.yaml
    --report /private/tmp/csm-review-20261012T060311Z/elongasome-snippets.md
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: pathway-links
  name: pathway-links
  status: failed
  required: false
  command: .venv/bin/python scripts/check_pathway_links.py --check
  exit_code: 2
  summary: Unsupported --check invocation; corrected invocation is separately recorded
    as passed.
  target_ids:
  - cellstructuremech:elongasome
- check_id: pathway-links-corrected
  name: pathway-links-corrected
  status: passed
  required: true
  command: .venv/bin/python scripts/check_pathway_links.py
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: history
  name: history
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: labels
  name: labels
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: curies
  name: curies
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: traits
  name: traits
  status: passed
  required: true
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: reviews
  name: reviews
  status: passed
  required: true
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: contract
  name: contract
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: diff
  name: diff
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
- check_id: baseline-ci
  name: baseline-ci
  status: passed
  required: true
  command: gh run view 38208737726 --repo CultureBotAI/CellStructureMech --json headSha,status,conclusion,event,name,url,jobs
  exit_code: 0
  summary: Actual exit0. Deterministic validation does not establish scientific support.
  target_ids:
  - cellstructuremech:elongasome
evidence:
- evidence_id: native
  kind: record_content
  reference: data/structures/division_machinery/elongasome.yaml
  locator: Entire captured YAML and inline history; repository history and generated-page
    headings
  summary: Pre-curation record inspected in full; concrete issues enumerated below.
    Source hash captures the unchanged native bytes.
  support: supports
  accessed_at: '2026-10-12T06:16:10Z'
  snapshot_sha256: 905ccf8a905e7074c55451346807afb7057bbb936ea01d71950bf2002268346b
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990586,GO:0098797,GO:0009274
  locator: Eight live GO identifiers, definitions, aspects and obsolete flags
  summary: Divisome exact identity and division-site parthood are coherent. GO0098797
    is a plasma membrane protein complex. GO0009274 denotes the peptidoglycan wall,
    not its synthesis machinery. Function CURIEs resolve.
  support: supports
  accessed_at: '2026-10-12T06:04:21Z'
  snapshot_sha256: f4b8df5544b3c8841a1790cead8201facef2eca97c2bb0ca52fd293365838f26
- evidence_id: typas
  kind: primary_source
  reference: DOI:10.1038/nrmicro2677
  locator: 'Author review full-text JATS: Introduction, synthesis and cytoskeletal
    sections; complete Table1 and Figure2 legend'
  summary: The 2011-online review distinguishes wall material from synthetic complexes
    and describes MreB motion inhibition in E. coli and B. subtilis. Table1 explicitly
    includes RodA with its then-proposed flippase assignment. It does not establish
    the later RodA polymerase discovery. Review evidence is secondary, not a new primary
    experiment.
  support: supports
  accessed_at: '2026-10-12T06:05:54Z'
  snapshot_sha256: 5d58623346677d6ecd21e26fff4f0e373028b6d0a679e7a041981805380810f1
- evidence_id: shi
  kind: primary_source
  reference: DOI:10.1016/j.cell.2018.02.050
  locator: Complete main review body, 42207 characters, including exception and RodZ
    sections
  summary: Review distinguishes MreB-guided growth from MreB-independent rod-shaped
    lineages. RodZ deletion impairs MreB rotation in ordinary E. coli backgrounds,
    but suppressors can restore rod shape without rotation. It does not establish
    that all complex motion is necessary for rod shape. Secondary synthesis, not primary
    experimental evidence.
  support: supports
  accessed_at: '2026-10-12T06:05:53Z'
  snapshot_sha256: 85461821236439e38067b63c72a9d974ee718cf73430bf07acd76995eb3c0d4a
- evidence_id: meeske
  kind: primary_source
  reference: DOI:10.1038/nature19331
  locator: Complete Introduction, Results and Discussion; start of Methods (first15000
    body characters)
  summary: B. subtilis genetic, biochemical and imaging experiments establish RodA
    as a SEDS peptidoglycan polymerase in the Rod complex. This is the post-2011 primary
    source already attached to the component, but not to the current definition.
  support: supports
  accessed_at: '2026-10-12T06:05:54Z'
  snapshot_sha256: ce826b647f0bea8ba669448b76323a7726fadddf9739544f4eba5eab019d28f3
- evidence_id: cho
  kind: primary_source
  reference: DOI:10.1038/nmicrobiol.2016.172
  locator: Complete main Introduction, Results and Discussion plus start of Methods
    (first16500 body characters)
  summary: E. coli radiolabeling, specific synthase inhibition and imaging distinguish
    RodA/PBP2 synthesis from semi-autonomous aPBPs. RodA and PBP2 show MreB-like directional
    motion; inhibiting RodA activity halts MreB rotation. The wall product and membrane
    machine are distinct.
  support: supports
  accessed_at: '2026-10-12T06:09:00Z'
  snapshot_sha256: 394ddc19e2663964c0e03c8c88ad29b40f702a4f2e46ec76f8c160b2d82db050
- evidence_id: morgenstein
  kind: primary_source
  reference: DOI:10.1073/pnas.1509610112
  locator: Complete primary abstract PMID26396257; full Methods unavailable in attempted
    public routes
  summary: RodZ couples MreB rotation to wall synthesis. Suppressor mutations restore
    rod shape without rotation under standard laboratory conditions; rotation promotes
    robustness to wall stress. Not proof that all synthase motion is absent.
  support: supports
  accessed_at: '2026-10-12T06:09:49Z'
  snapshot_sha256: 3215d8593a891fa93ffbcdf3819c2601df04f60552e0c4c031f949630fb336dd
- evidence_id: mcquillen
  kind: primary_source
  reference: DOI:10.1146/annurev-biophys-121219-081703
  locator: Entire review body63919 characters; radial-thickness and two-track sections
    reread
  summary: Secondary review explicitly distinguishes a fast FtsZ-dependent inactive
    FtsW population from a slow synthesis-dependent active population in E. coli.
    It gives method-dependent ring radial-thickness estimates and summarizes C. crescentus
    filament dimensions. Its approximately13nm membrane-spacing statement differs
    from the inspected primary16nm peak-to-peak experiment.
  support: supports
  accessed_at: '2026-10-12T06:05:55Z'
  snapshot_sha256: 7505fc0aee367d900e0c370e3fac89266b3cf6467aad3e721df3c7507834b373
- evidence_id: pende
  kind: primary_source
  reference: DOI:10.1038/s41467-021-23099-8
  locator: Verified PMID34088904; entire Introduction and Discussion, first Results
    localization section
  summary: M. smithii has an archaeal FtsZ/SepF division system and pseudomurein wall
    chemically distinct from bacterial peptidoglycan. Shared FtsZ does not establish
    occurrence of the bacterial FtsW/FtsI PG machine. Removing an occurrence assertion
    is not asserting no archaeal divisomes.
  support: supports
  accessed_at: '2026-10-12T06:09:48Z'
  snapshot_sha256: 1a4c3f61e079a23268586ca7325bca848974cfd8e932d6a256953cbb9b91313f
- evidence_id: bibliography
  kind: authority
  reference: https://pubmed.ncbi.nlm.nih.gov/
  locator: 15 complete native primary abstracts and identities; five Crossref records
    and EuropePMC DOI records
  summary: Native FtsZ/FtsA/ZipA/SepF/FtsW/FtsI and RodA/PBP2/MreC/D/RodZ identity/localization
    references match. Abstract-only evidence remains bounded. Online versus issue
    year differences are not errors; metadata inspection is not exhaustive retraction
    screening.
  support: supports
  accessed_at: '2026-10-12T06:04:20Z'
  snapshot_sha256: 50acb38cc5b547acf4d3da99704c968fdf5e970d52082acf818bee05ae28ab51
- evidence_id: authorities
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/
  locator: 11 full JSON entry identity fields; six ENA taxon identities; OLS nanometer;
    pinned WP5060 hash
  summary: All11 accessions match named reviewed proteins and taxa. RodA alias maps
    to mrdB and PBP2 to mrdA. These are identity checks, not independent membership
    proof. Existing WP5060 links remain organism- and segment-scoped; E. coli PBP2
    entries are not equated.
  support: supports
  accessed_at: '2026-10-12T06:16:10Z'
- evidence_id: adapter
  kind: authority
  reference: https://imodulondb.org/
  locator: Installed adapter28-dataset inventory; precise1k ftsZ,rodZ,rodA,mrdB and
    B.subtilis sepF queries
  summary: Covered gene hits confirm useful keys but return no informative iModulon
    hit for these queries. No module summary is warranted. Alias lookup miss for rodA
    was followed through mrdB; it is not biological absence.
  support: supports
  accessed_at: '2026-10-12T06:16:10Z'
- evidence_id: prior
  kind: prior_review
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/161
  locator: All-state name searches and issues64,65,66,102,119,120,161;191 canonical
    bundles scanned including ignored/hidden paths under reviews/structured
  summary: No exact-ID/path canonical predecessor for either target. Closed161 corrected
    RodA component evidence but explicitly deferred the definition; this is a residual
    defect, not a claim that the earlier fix never happened. Guided-by schema discussion
    and earlier pathway fixes remain intact.
  support: supports
  accessed_at: '2026-10-12T06:16:10Z'
- evidence_id: baseline-qc
  kind: validation
  reference: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38208737726
  locator: Successful exact-base merge-group QC and checksum-verified complete cached
    log
  summary: Baseline937ba6254eb987adcbd92e82b21b2ce8651dc5e3 passed987 tests with3
    skips,909 strict records,1724 histories. Target schema/strict/snippets and current
    global checks are separately recorded. This is unchanged-base CI reuse, not a
    new local full run.
  support: supports
  accessed_at: '2026-10-12T06:16:10Z'
assessments:
- assessment_id: identity
  area: identity
  topic: Identity, synonyms and class
  outcome: concern
  summary: Distinct local elongasome/Rod-complex identity, class and membrane-complex
    parent are appropriate, but definition and synonym evidence require the2016 primary
    sources. Bounded ontology queries do not establish global term absence.
  target_ids:
  - cellstructuremech:elongasome
  evidence_ids:
  - native
  - go
  - typas
  - meeske
  - cho
- assessment_id: hierarchy
  area: grounding
  topic: Hierarchy and parthood
  outcome: concern
  summary: Plasma-membrane-protein-complex parent is valid; peptidoglycan wall product
    is not valid parthood.
  target_ids:
  - cellstructuremech:elongasome
  evidence_ids:
  - native
  - go
  - typas
- assessment_id: components
  area: evidence
  topic: Component roles, essentiality and examples
  outcome: concern
  summary: RodA/PBP2 and MreC/D roles are supported in named model systems. ESSENTIAL
    is assembly/function scope, not all-organism viability. RodZ has conditional coupling
    evidence; no new stoichiometry or universal membership is inferred. False RodA
    source-absence notes need correction.
  target_ids:
  - cellstructuremech:elongasome
  evidence_ids:
  - native
  - bibliography
  - authorities
  - meeske
  - cho
  - mcquillen
- assessment_id: taxonomic
  area: scope
  topic: Taxonomic distribution and canonical examples
  outcome: concern
  summary: Named E. coli and B. subtilis reference systems are supported. Domain-level
    occurrence assertions must not transfer a protein or wall chemistry to the entire
    machine. Removing unsupported rows does not assert the opposite.
  target_ids:
  - cellstructuremech:elongasome
  evidence_ids:
  - native
  - typas
  - mcquillen
  - pende
  - authorities
- assessment_id: function
  area: evidence
  topic: Functions, traits and pathway link
  outcome: concern
  summary: Sidewall synthesis and WP5060 overlap are supported, not whole-pathway
    identity. Rod-shape necessity requires bounded model-system interpretation and
    exceptions.
  target_ids:
  - cellstructuremech:elongasome
  evidence_ids:
  - native
  - typas
  - cho
  - shi
  - authorities
- assessment_id: graph
  area: graph
  topic: Mechanism and experimental limits
  outcome: concern
  summary: Separate MreB rotation from synthase movement and synthesis output; retain
    perturbation contexts, suppressor exceptions and direction-of-evidence limits.
  target_ids:
  - cellstructuremech:elongasome
  evidence_ids:
  - native
  - typas
  - shi
  - cho
  - morgenstein
- assessment_id: completeness
  area: completeness
  topic: Measurements, discussions and optional content
  outcome: supported
  summary: No optional physical measurement or image is required. The guided-by-MreB
    relation discussion remains legitimate; definition-source TODO has actionable
    primary evidence. Component inventory is not a complete stoichiometric model.
  target_ids:
  - cellstructuremech:elongasome
  evidence_ids:
  - native
  - prior
  - meeske
- assessment_id: history
  area: ownership
  topic: Provenance, prior issues and ownership
  outcome: supported
  summary: No native change preceded this observation. Historical statements remain
    history, even where mistaken. Corrections belong in the maintained target with
    guarded writer and new events; earlier reports and62 untracked legacy reports
    remain untouched.
  target_ids:
  - cellstructuremech:elongasome
  evidence_ids:
  - native
  - prior
  - baseline-qc
findings:
- finding_id: F1
  issue_key: elongasome-definition-source-residual
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Finish the deferred RodA definition and synonym evidence correction
  description: 'The definition still attributes the2016 RodA SEDS-polymerase finding
    to Typas2011, and the narrow RodA-PBP2 synonym cites a review not establishing
    that pair. Current RodA notes and the open discussion also falsely say Typas never
    mentions RodA: its Table1 does. Closed161 fixed only the component, explicitly
    leaving the definition.'
  target_ids:
  - cellstructuremech:elongasome
  field_paths:
  - definition
  - definition_source
  - synonyms
  - components[roda].evidence
  - discussions[definition_source_predates_roda]
  evidence_ids:
  - native
  - typas
  - meeske
  - cho
  - shi
  - prior
  rule_id: review-checklist:claim-scope-evidence-and-relations
  native_severity: P2
  normalization_reason: Major scientific evidence or relation error affecting machine-readable
    interpretation; exact record identity is retained.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained scientific record
- finding_id: F2
  issue_key: elongasome-wall-parthood
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Remove peptidoglycan-wall parthood from its synthesis machine
  description: part_of GO0009274 makes the membrane protein machine a constituent
    of the peptidoglycan wall product. The GO definition and inspected wall-synthesis
    sources distinguish wall material from the membrane-associated complex that synthesizes
    it.
  target_ids:
  - cellstructuremech:elongasome
  field_paths:
  - part_of
  evidence_ids:
  - native
  - go
  - typas
  - cho
  rule_id: review-checklist:claim-scope-evidence-and-relations
  native_severity: P2
  normalization_reason: Major scientific evidence or relation error affecting machine-readable
    interpretation; exact record identity is retained.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained scientific record
- finding_id: F3
  issue_key: elongasome-motion-and-shape-scope
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Separate MreB rotation, synthase movement and conditional shape phenotypes
  description: The graph names measured MreB rotation as whole-complex motion, treats
    RodZ as required for it and implies movement produces rod shape. The cited Shi
    review and Morgenstein primary abstract explicitly report rod-shaped suppressors
    without MreB rotation. The record-wide REQUIRED_FOR rod-shape trait also ignores
    MreB-independent rod-shaped lineages discussed by its sources.
  target_ids:
  - cellstructuremech:elongasome
  field_paths:
  - causal_graphs[elongasome_sidewall_elongation]
  - associated_traits
  evidence_ids:
  - native
  - typas
  - shi
  - cho
  - morgenstein
  rule_id: review-checklist:claim-scope-evidence-and-relations
  native_severity: P2
  normalization_reason: Major scientific evidence or relation error affecting machine-readable
    interpretation; exact record identity is retained.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained scientific record
- finding_id: F4
  issue_key: elongasome-archaeal-negative-evidence
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Remove an unsupported domain-wide negative occurrence claim
  description: The Archaea ABSENT row infers absence of the defined complex from an
    uncited domain-wide wall statement, attributed to a bacterial review that does
    not establish the archaeal claim. The primary archaeal comparison distinguishes
    pseudomurein from bacterial PG, but does not assay absence of every Rod-complex
    component or all archaeal taxa.
  target_ids:
  - cellstructuremech:elongasome
  field_paths:
  - taxonomic_distribution
  evidence_ids:
  - native
  - typas
  - pende
  rule_id: review-checklist:claim-scope-evidence-and-relations
  native_severity: P2
  normalization_reason: Major scientific evidence or relation error affecting machine-readable
    interpretation; exact record identity is retained.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Rebase the bounded definition and synonym references on inspected2016
    primary evidence; distinguish RodA being mentioned from its polymerase activity
    being established; resolve the deferred discussion while preserving historical
    rationale/date and append-only events.
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:elongasome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained scientific record
  generator: just render
  acceptance_checks:
  - The affected native assertions and rendered graph/prose agree with the cited bounded
    evidence.
  - Guarded write, append-only history, PROPOSED status and previous history are preserved.
  - Fresh full QC, direct target checks and successor dispositions pass.
- action_id: A2
  description: Remove this unsupported parthood assertion, retain the supported plasma-membrane-protein-complex
    is-a parent, and do not guess replacement parthood.
  finding_ids:
  - F2
  target_ids:
  - cellstructuremech:elongasome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained scientific record
  generator: just render
  acceptance_checks:
  - The affected native assertions and rendered graph/prose agree with the cited bounded
    evidence.
  - Guarded write, append-only history, PROPOSED status and previous history are preserved.
  - Fresh full QC, direct target checks and successor dispositions pass.
- action_id: A3
  description: Name MreB rotation separately from RodA/PBP2 motion, qualify perturbation-derived
    edges and suppressor exceptions, and weaken universal shape necessity to a model-system-scoped
    association with direct evidence.
  finding_ids:
  - F3
  target_ids:
  - cellstructuremech:elongasome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained scientific record
  generator: just render
  acceptance_checks:
  - The affected native assertions and rendered graph/prose agree with the cited bounded
    evidence.
  - Guarded write, append-only history, PROPOSED status and previous history are preserved.
  - Fresh full QC, direct target checks and successor dispositions pass.
- action_id: A4
  description: Remove the unsupported ABSENT row without asserting presence; retain
    a bounded bacterial distribution and explain that absence of a curated row is
    not biological absence.
  finding_ids:
  - F4
  target_ids:
  - cellstructuremech:elongasome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/elongasome.yaml
    role: maintained scientific record
  generator: just render
  acceptance_checks:
  - The affected native assertions and rendered graph/prose agree with the cited bounded
    evidence.
  - Guarded write, append-only history, PROPOSED status and previous history are preserved.
  - Fresh full QC, direct target checks and successor dispositions pass.
limitations:
- Same-agent assessment, not human sign-off, raw image reanalysis, a new measurement
  or exhaustive literature search. Abstract-only native protein references support
  only statements present in those abstracts.
- Typas review synthesis/cytoskeleton sections and complete Table1/Figure2 legend
  inspected, not every mechanics/metabolic paragraph. Shi and McQuillen complete main
  bodies inspected. Meeske and Cho complete main Results/Discussion but not all Methods/supplements.
  Reviews are secondary evidence even when the shared evidence kind is primary_source
  (directly inspected source).
- Yang2021 complete Results/Discussion and start Statistics; Yang2017 entire main
  body; BissonFilho main Results and initial Methods. No new speed estimate is inferred
  from uninspected figure pixels.
- Li2007 publisher Results and Methods, including density-profile method and Figure6
  caption, read in full. The review13nm and primary16nm values are kept distinct;
  their discrepancy is not claimed resolved. No new radial-thickness measurement is
  curated.
- Pende2021 verified identity, Introduction/Discussion and localization Results inspected,
  not all structural/phylogeny Methods. An accidentally retrieved unrelated PMID34088901
  was explicitly rejected and never used. Morgenstein full primary abstract only;
  unsuccessful full-text attempts are not counted as full reading.
- Some EuropePMC fullText routes returned500, S3 routes404, and web pages showed access
  challenges. Documented NCBI efetch and legitimate publisher/institutional routes
  were used; no challenges bypassed. EganVollmer complete abstract only, not full
  text.
- The initial pathway checker invocation used unsupported --check and exited2. Its
  corrected documented invocation passed; both outcomes are retained. Exact-base full
  CI is reused before mutation; later changes require fresh full QC.
- Identifier/label global checks include documented no-adapter skips; these are not
  biological verification. Eleven accession identities, six taxa, target GO terms
  and the nanometer unit were separately inspected. iModulon gene hits are not localization/membership
  evidence.
- No canonical predecessor in191 bundles under reviews/structured (ignored files included).
  Bounded ontology and GitHub searches do not prove universal absence. Other context
  records are not completed by this bundle.
tags:
- scientific-review
- division-machinery
- evidence-scope
```
