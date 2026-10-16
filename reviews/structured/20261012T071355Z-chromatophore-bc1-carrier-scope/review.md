# Chromatophore cytochrome bc1 carrier-scope review

- Review: 20261012T071355Z-chromatophore-bc1-carrier-scope
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T07:06:38Z
- Finished UTC: 2026-10-12T07:13:55Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed major scope issue: the R. sphaeroides c2 route is described as the generic purple-bacterial bc1 route. All native fields were screened, but the original full-text citation remains unavailable; this is not a completed whole-record scientific review.

## Scope And Provenance

One entire native record read; identity, scope, relations, all graph edges, citations and history screened. Full-text support for the original bc1-specific citation remains incomplete.

Selection: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e74d0c3e33df7e44348afbba1695b61c23262ab0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:chromatophore_cytochrome_bc1_complex | data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml | maintained | chromatophore cytochrome bc1 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:chromatophore_cytochrome_bc1_complex | Fresh native schema check. |
| strict | passed | True | cellstructuremech:chromatophore_cytochrome_bc1_complex | Fresh closed-schema check. |
| snippets | passed | True | cellstructuremech:chromatophore_cytochrome_bc1_complex | No snippets: 0 of13 citations; not evidence of full-text readability. |
| history | passed | True | cellstructuremech:chromatophore_cytochrome_bc1_complex | Fresh full-corpus history validation,1729 valid. |
| reviews | passed | True | cellstructuremech:chromatophore_cytochrome_bc1_complex | Fresh pre-save archive check,196 valid bundles. |
| curies-live | passed | True | cellstructuremech:chromatophore_cytochrome_bc1_complex | Fresh authority controls passed;4023 OK,251 documented skips; cached fresh IDs are retained. |
| release-qc reused unchanged corpus | passed | True | cellstructuremech:chromatophore_cytochrome_bc1_complex | Reused actual prior command at 2026-10-12T06:45:16Z; SHA-verified log and unchanged local commit. 987 tests passed,3 skipped;909 strict records and generated site current. |
| release-labels reused unchanged corpus | passed | True | cellstructuremech:chromatophore_cytochrome_bc1_complex | Reused actual prior command at 2026-10-12T06:47:16Z; SHA-verified log and unchanged local commit. Label check includes603 no-adapter skips; sibling trait check used cached477-trait index and this target has no trait links. |
| release-traits reused unchanged corpus | passed | True | cellstructuremech:chromatophore_cytochrome_bc1_complex | Reused actual prior command at 2026-10-12T06:48:52Z; SHA-verified log and unchanged local commit. Label check includes603 no-adapter skips; sibling trait check used cached477-trait index and this target has no trait links. |
| adapter-datasets | failed | False | cellstructuremech:chromatophore_cytochrome_bc1_complex | Initial sandbox DNS failure, superseded by successful public read. |
| adapter-datasets-live | passed | False | cellstructuremech:chromatophore_cytochrome_bc1_complex | Inventory inspected; no matching organism dataset. No further adapter search applicable. |
| Original Comayras full-text support | unavailable | True | cellstructuremech:chromatophore_cytochrome_bc1_complex | Publisher API returned metadata only. ScienceDirect and journal PDF returned403; ResearchGate429; corrected HAL DOI query returned0 results. Abstract is readable, but full-text bc1-specific evidence is not established. |

## Scientific And Domain Assessments

### Structure identity, label, synonym and class

identity: supported. Targets: cellstructuremech:chromatophore_cytochrome_bc1_complex.

The target denotes a chromatophore-localized multiprotein bc1 complex, not the membrane, a single subunit, b6f or a phenotype. Related rather than exact generic bc1 synonymy preserves the location restriction.

### Parthood and internal references

grounding: supported. Targets: cellstructuremech:chromatophore_cytochrome_bc1_complex.

GO0042717 membrane parthood is supported. The graph RC-LH1-PufX reference resolves to a maintained record and was read as context, not itself scientifically reviewed here.

### Taxonomic distribution, exemplar and soluble carrier

scope: concern. Targets: cellstructuremech:chromatophore_cytochrome_bc1_complex.

Purple-bacterial distribution and the R. sphaeroides exemplar have support, but c2 is not the universal purple-bacterial return carrier. RARE is a qualitative restricted-lineage assertion, not a measured prevalence.

### Quinol oxidation and electron transport

evidence: concern. Targets: cellstructuremech:chromatophore_cytochrome_bc1_complex.

The functional outline is coherent for the named R. sphaeroides system. The c2-specific function needs an explicit organism context. Attribution of every bc1-specific detail to the original Comayras full text remains unverified.

### All five nonmechanistic edges

graph: concern. Targets: cellstructuremech:chromatophore_cytochrome_bc1_complex.

Membrane membership is directly supported by SL0042. RC quinone reduction has abstract support. bc1 quinol oxidation and c2 return are consistent with the R. sphaeroides route described by Kawakami, but the native Comayras citation was not fully readable. NONMECHANISTIC properly excludes Q-cycle chemistry but does not bound the graph to its model organism.

### Components, measurements, datasets and discussions

completeness: supported. Targets: cellstructuremech:chromatophore_cytochrome_bc1_complex.

The explicit subunit-grounding TODO is retained. No component stoichiometry, protein-example accession, image, dimension, trait or dataset assertion is present to audit; optional missing slots are not findings.

### Exact citation support and reading limits

provenance: unknown. Targets: cellstructuremech:chromatophore_cytochrome_bc1_complex.

The native DOI/PMID identity is verified, but the full original Comayras paper was not obtained. No title or inaccessible text was paraphrased into evidence. This prevents a completed whole-record verdict despite the independently confirmed scope issue.

### Status, audit trail and maintained owner

ownership: supported. Targets: cellstructuremech:chromatophore_cytochrome_bc1_complex.

The native record remains PROPOSED. Inline events and the append-only creation history were read; the review changes neither. Scientific correction belongs in the maintained YAML through the guarded writer, not in rendered products.

## Findings

### F1: Bound the c2 return-carrier route to its demonstrated organism context

major / open / confirmed; issue key: chromatophore-bc1-return-carrier-scope.

The definition and function unconditionally route purple-bacterial chromatophore bc1 electrons through soluble cytochrome c2; the general-scope graph also names c2 and an RC-LH1-PufX partner. The source organism is R. sphaeroides, while inspected primary literature distinguishes other purple-bacterial return carriers and resolves a T. tepidum HiPIP:LH1-RC complex. Keep the broader complex identity separate from the organism-specific c2/PufX pathway. This is a scope defect, not a claim that c2 is wrong for R. sphaeroides or that every alternative carrier is interchangeable.

## Recommended Actions And Acceptance Checks

### A1

Generalize the class definition to appropriate periplasmic electron carriers and explicitly scope the c2/RC-LH1-PufX function and graph to the supported R. sphaeroides system, or otherwise supply a precisely delimited narrower identity. Attach inspected evidence at the changed claims. Obtain and inspect the original paper before closing the remaining attribution uncertainty.

- No general purple-bacterial assertion requires c2 or RC-LH1-PufX; the named R. sphaeroides c2 route is retained with explicit scope.
- Claim-level citations are inspected; unavailable original-paper support is not silently marked verified.
- Guarded writer, new curation event and append-only repository history; PROPOSED status and all prior artifacts preserved.
- Fresh target validation, authoritative full QC, rendered/embedding drift checks and a lineage-linked evidence-backed successor review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml; Entire captured native YAML, all five graph edges, inline and repository history | supports | The general purple-bacterial definition and function specify cytochrome c2 without taxonomic qualification. The graph includes RC-LH1-PufX and c2 under a purple-bacterial scope; a canonical example is not a scope constraint on these claims. |
| comayras | DOI:10.1074/jbc.M412088200; Complete primary abstract via PMID15632164 and Europe PMC; Crossref identity and publisher metadata | partial | Experiments and modeling concern R. sphaeroides RC-LH1 units, excitation transfer and quinone confinement. This inspected abstract supports the named exemplar and quinone-domain context, but does not expose all bc1/c2 discussion from the full article. |
| hipip | DOI:10.1038/s41467-021-21397-9; NCBI full-text JATS PMC7889895; complete Introduction, Structural overview and co-crystallization Methods; Discussion inspected, no new measurements | supports | Kawakami et al. 2021 distinguish the R. sphaeroides c2 route from donor diversity in purple bacteria and resolve a T. tepidum HiPIP:LH1-RC complex. A c2-only class definition loses this lineage dependence. The crystallization is a purified-protein experiment, not a direct in vivo bc1-to-HiPIP flux measurement. |
| location | uniprot.location:SL-0042; Complete live UniProt location definition and GO mapping | supports | Confirms bc1 as a constituent of purple-bacterial cellular chromatophore membranes; does not require a particular soluble return carrier. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042717,GO:0009767; Live names, definitions, aspects and obsolete flags; bounded candidate search | supports | The membrane and electron-transport terms are current and correctly used. The inspected broader respiratory-chain complex III term is not an exact identity for the location-restricted record. The 100-result search is not an exhaustive ontology-absence proof. |
| taxon | NCBITaxon:1063; ENA live taxonomy record, scientific name and synonyms | supports | Cereibacter sphaeroides and the cited Rhodobacter sphaeroides are the same species under current and older names. |
| validation | /private/tmp/csm-review-20261012T070144Z/baseline-verification.json; SHA-verified previous full QC and final input captures; fresh target checks, history, archive and live CURIE checks | supports | Unchanged scientific corpus passed prior full QC: 987 tests, three skips, 909 strict records. Fresh target schema/strict passed. Live CURIE control pairs passed; 4023 identifiers resolved with 251 documented skips. These checks do not establish claim-level scientific support. |
| adapter | https://imodulondb.org/; Installed kg-microbe-sources imodulondb datasets, successful live retry | supports | The inspected 28-dataset inventory has no Cereibacter/Rhodobacter sphaeroides dataset. No applicable gene/module query was inferred. Database noncoverage is not biological absence. |
| prior | reviews/structured/; 196 canonical bundles scanned for exact target ID/path, plus ignored-inclusive rg over reviews, reports, history, research and curation | supports | No canonical predecessor for this target was found in those local roots. The creation history links historical issue762 to an event-label correction, not to this new carrier-scope finding. GitHub was not mutated or exhaustively re-triaged. |

## Limits And Additional Notes

- Original Comayras full text remains unavailable; the readable abstract is not proof that omitted bc1 details are absent from the paper. The failed first HAL query was a syntax/API error, not zero results; the corrected quoted DOI query returned0.
- Kawakami Introduction, Structural overview and co-crystallization Methods were completely read in bounded tool output; Discussion was read, but not all supplementary material. No figure-pixel analysis, new measurement, structural refinement or direct in vivo flux inference was performed.
- A successful network-control run does not mean every fresh-cache identifier was refetched. Label validation retains603 no-adapter skips; CURIE validation251 documented skips; prior full QC three skipped tests. No biological claims are inferred from those skips.
- The iModulonDB inventory lacks the named organism; expression-module noncoverage is not a negative localization or phenotype result.
- Bounded local predecessor search includes ignored files; it is not an exhaustive current GitHub issue triage. No new external issue, PR, push or merge was performed.
- Only this issue-bearing bundle is written. Native scientific data, histories and generated products are unchanged. Existing local publication approval remains outstanding.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T071355Z-chromatophore-bc1-carrier-scope
kind: record
repository: CultureBotAI/CellStructureMech
title: Chromatophore cytochrome bc1 carrier-scope review
started_at: '2026-10-12T07:06:38Z'
finished_at: '2026-10-12T07:13:55Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same coding-agent context; no independent human or second-agent
    review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One confirmed major scope issue: the R. sphaeroides c2 route is described
  as the generic purple-bacterial bc1 route. All native fields were screened, but
  the original full-text citation remains unavailable; this is not a completed whole-record
  scientific review.'
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
  - path: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
    sha256: 3f0499e90f5596370983a6559b8b438c03cf606b61c2766063b6be5d7fa84062
    role: target
  - path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
    sha256: 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824
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
  - path: history/records/chromatophore_cytochrome_bc1_complex/2026-09-13T073520Z-codex-c976eb.yaml
    sha256: b61982eaee22ed0519ed7de58c31e50a45bd0c675013e327450a0f41a2e400c3
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
- target_id: cellstructuremech:chromatophore_cytochrome_bc1_complex
  path: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
  label: chromatophore cytochrome bc1 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
    role: maintained scientific record
scope:
  description: One entire native record read; identity, scope, relations, all graph
    edges, citations and history screened. Full-text support for the original bc1-specific
    citation remains incomplete.
  selection: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  exclusions:
  - target: Full-text attribution of bc1/c2-specific claims to DOI:10.1074/jbc.M412088200
    reason: Only primary abstract and metadata obtained through the attempted legitimate
      public routes.
checks:
- check_id: schema
  name: schema
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
  exit_code: 0
  status: passed
  required: true
  summary: Fresh native schema check.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - validation
- check_id: strict
  name: strict
  command: .venv/bin/python scripts/validate_strict.py data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
  exit_code: 0
  status: passed
  required: true
  summary: Fresh closed-schema check.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - validation
- check_id: snippets
  name: snippets
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
    --report /private/tmp/csm-review-20261012T070144Z-bc1/snippets.md
  exit_code: 0
  status: passed
  required: true
  summary: 'No snippets: 0 of13 citations; not evidence of full-text readability.'
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - validation
- check_id: history
  name: history
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  status: passed
  required: true
  summary: Fresh full-corpus history validation,1729 valid.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - validation
- check_id: reviews
  name: reviews
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  status: passed
  required: true
  summary: Fresh pre-save archive check,196 valid bundles.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - validation
- check_id: curies-live
  name: curies-live
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  status: passed
  required: true
  summary: Fresh authority controls passed;4023 OK,251 documented skips; cached fresh
    IDs are retained.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - validation
- check_id: release-qc
  name: release-qc reused unchanged corpus
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  status: passed
  required: true
  summary: Reused actual prior command at 2026-10-12T06:45:16Z; SHA-verified log and
    unchanged local commit. 987 tests passed,3 skipped;909 strict records and generated
    site current.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - validation
- check_id: release-labels
  name: release-labels reused unchanged corpus
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  status: passed
  required: true
  summary: Reused actual prior command at 2026-10-12T06:47:16Z; SHA-verified log and
    unchanged local commit. Label check includes603 no-adapter skips; sibling trait
    check used cached477-trait index and this target has no trait links.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - validation
- check_id: release-traits
  name: release-traits reused unchanged corpus
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  status: passed
  required: true
  summary: Reused actual prior command at 2026-10-12T06:48:52Z; SHA-verified log and
    unchanged local commit. Label check includes603 no-adapter skips; sibling trait
    check used cached477-trait index and this target has no trait links.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - validation
- check_id: adapter-datasets
  name: adapter-datasets
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 2
  status: failed
  required: false
  summary: Initial sandbox DNS failure, superseded by successful public read.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - adapter
- check_id: adapter-datasets-live
  name: adapter-datasets-live
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  status: passed
  required: false
  summary: Inventory inspected; no matching organism dataset. No further adapter search
    applicable.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - adapter
- check_id: original-fulltext
  name: Original Comayras full-text support
  status: unavailable
  required: true
  summary: Publisher API returned metadata only. ScienceDirect and journal PDF returned403;
    ResearchGate429; corrected HAL DOI query returned0 results. Abstract is readable,
    but full-text bc1-specific evidence is not established.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - comayras
evidence:
- evidence_id: native
  kind: record_content
  reference: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
  locator: Entire captured native YAML, all five graph edges, inline and repository
    history
  summary: The general purple-bacterial definition and function specify cytochrome
    c2 without taxonomic qualification. The graph includes RC-LH1-PufX and c2 under
    a purple-bacterial scope; a canonical example is not a scope constraint on these
    claims.
  support: supports
  accessed_at: '2026-10-12T07:13:55Z'
  snapshot_sha256: 3f0499e90f5596370983a6559b8b438c03cf606b61c2766063b6be5d7fa84062
- evidence_id: comayras
  kind: primary_source
  reference: DOI:10.1074/jbc.M412088200
  locator: Complete primary abstract via PMID15632164 and Europe PMC; Crossref identity
    and publisher metadata
  summary: Experiments and modeling concern R. sphaeroides RC-LH1 units, excitation
    transfer and quinone confinement. This inspected abstract supports the named exemplar
    and quinone-domain context, but does not expose all bc1/c2 discussion from the
    full article.
  support: partial
  accessed_at: '2026-10-12T07:06:55Z'
  snapshot_sha256: a6dac666a5234e57bce6df2c7def0b89f97e071d34369f04295ec0bfbd29612b
- evidence_id: hipip
  kind: primary_source
  reference: DOI:10.1038/s41467-021-21397-9
  locator: NCBI full-text JATS PMC7889895; complete Introduction, Structural overview
    and co-crystallization Methods; Discussion inspected, no new measurements
  summary: Kawakami et al. 2021 distinguish the R. sphaeroides c2 route from donor
    diversity in purple bacteria and resolve a T. tepidum HiPIP:LH1-RC complex. A
    c2-only class definition loses this lineage dependence. The crystallization is
    a purified-protein experiment, not a direct in vivo bc1-to-HiPIP flux measurement.
  support: supports
  accessed_at: '2026-10-12T07:08:06Z'
  snapshot_sha256: ad2b6100c49972c84e09121c931e2ef82dc91e362bf7bd70211babe70362a495
- evidence_id: location
  kind: authority
  reference: uniprot.location:SL-0042
  locator: Complete live UniProt location definition and GO mapping
  summary: Confirms bc1 as a constituent of purple-bacterial cellular chromatophore
    membranes; does not require a particular soluble return carrier.
  support: supports
  accessed_at: '2026-10-12T07:06:56Z'
  snapshot_sha256: f16f40b6a8cfdb7911506598df2106649cf2e49643691a2077726a4384262ead
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042717,GO:0009767
  locator: Live names, definitions, aspects and obsolete flags; bounded candidate
    search
  summary: The membrane and electron-transport terms are current and correctly used.
    The inspected broader respiratory-chain complex III term is not an exact identity
    for the location-restricted record. The 100-result search is not an exhaustive
    ontology-absence proof.
  support: supports
  accessed_at: '2026-10-12T07:06:57Z'
  snapshot_sha256: a9ebf46fb99807cbd088c421c45834e88fc68f21d1abdd1f394e70ef458c0271
- evidence_id: taxon
  kind: authority
  reference: NCBITaxon:1063
  locator: ENA live taxonomy record, scientific name and synonyms
  summary: Cereibacter sphaeroides and the cited Rhodobacter sphaeroides are the same
    species under current and older names.
  support: supports
  accessed_at: '2026-10-12T07:06:57Z'
  snapshot_sha256: fa64efd9e90dfef7e7b8c197e6e6449c311f1bb11557801f0d11551e830c23e8
- evidence_id: validation
  kind: validation
  reference: /private/tmp/csm-review-20261012T070144Z/baseline-verification.json
  locator: SHA-verified previous full QC and final input captures; fresh target checks,
    history, archive and live CURIE checks
  summary: 'Unchanged scientific corpus passed prior full QC: 987 tests, three skips,
    909 strict records. Fresh target schema/strict passed. Live CURIE control pairs
    passed; 4023 identifiers resolved with 251 documented skips. These checks do not
    establish claim-level scientific support.'
  support: supports
  accessed_at: '2026-10-12T07:13:55Z'
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/
  locator: Installed kg-microbe-sources imodulondb datasets, successful live retry
  summary: The inspected 28-dataset inventory has no Cereibacter/Rhodobacter sphaeroides
    dataset. No applicable gene/module query was inferred. Database noncoverage is
    not biological absence.
  support: supports
  accessed_at: '2026-10-12T07:13:55Z'
- evidence_id: prior
  kind: search
  reference: reviews/structured/
  locator: 196 canonical bundles scanned for exact target ID/path, plus ignored-inclusive
    rg over reviews, reports, history, research and curation
  summary: No canonical predecessor for this target was found in those local roots.
    The creation history links historical issue762 to an event-label correction, not
    to this new carrier-scope finding. GitHub was not mutated or exhaustively re-triaged.
  support: supports
  accessed_at: '2026-10-12T07:13:55Z'
  search_scope: Exact target ID/path in all196 YAML bundles under reviews/structured
    using Path.rglob, which includes ignored and hidden paths; identifier and label
    with rg -uu in reviews, reports, history, research and curation. No GitHub-wide
    absence claim.
assessments:
- assessment_id: identity
  area: identity
  topic: Structure identity, label, synonym and class
  outcome: supported
  summary: The target denotes a chromatophore-localized multiprotein bc1 complex,
    not the membrane, a single subunit, b6f or a phenotype. Related rather than exact
    generic bc1 synonymy preserves the location restriction.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - native
  - location
  - go
- assessment_id: relations
  area: grounding
  topic: Parthood and internal references
  outcome: supported
  summary: GO0042717 membrane parthood is supported. The graph RC-LH1-PufX reference
    resolves to a maintained record and was read as context, not itself scientifically
    reviewed here.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - native
  - location
  - go
  - validation
- assessment_id: scope
  area: scope
  topic: Taxonomic distribution, exemplar and soluble carrier
  outcome: concern
  summary: Purple-bacterial distribution and the R. sphaeroides exemplar have support,
    but c2 is not the universal purple-bacterial return carrier. RARE is a qualitative
    restricted-lineage assertion, not a measured prevalence.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - native
  - location
  - taxon
  - comayras
  - hipip
  dimensions:
  - name: supported_model
    value: Cereibacter sphaeroides (Rhodobacter sphaeroides), NCBITaxon:1063
    definition: Organism context of the native quinone-domain source and c2 route,
      not a universal purple-bacterial pathway.
    evidence_ids:
    - comayras
    - taxon
    - hipip
  - name: counterexample_context
    value: Thermochromatium tepidum strain MC; purified HiPIP:LH1-RC co-crystal
    definition: Alternative electron-donor family demonstrated structurally; kinetic
      electron paths are predictions and not new measurements in this review.
    evidence_ids:
    - hipip
- assessment_id: function
  area: evidence
  topic: Quinol oxidation and electron transport
  outcome: concern
  summary: The functional outline is coherent for the named R. sphaeroides system.
    The c2-specific function needs an explicit organism context. Attribution of every
    bc1-specific detail to the original Comayras full text remains unverified.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - native
  - go
  - comayras
  - hipip
- assessment_id: graph
  area: graph
  topic: All five nonmechanistic edges
  outcome: concern
  summary: Membrane membership is directly supported by SL0042. RC quinone reduction
    has abstract support. bc1 quinol oxidation and c2 return are consistent with the
    R. sphaeroides route described by Kawakami, but the native Comayras citation was
    not fully readable. NONMECHANISTIC properly excludes Q-cycle chemistry but does
    not bound the graph to its model organism.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - native
  - location
  - comayras
  - hipip
- assessment_id: completeness
  area: completeness
  topic: Components, measurements, datasets and discussions
  outcome: supported
  summary: The explicit subunit-grounding TODO is retained. No component stoichiometry,
    protein-example accession, image, dimension, trait or dataset assertion is present
    to audit; optional missing slots are not findings.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - native
- assessment_id: provenance
  area: provenance
  topic: Exact citation support and reading limits
  outcome: unknown
  summary: The native DOI/PMID identity is verified, but the full original Comayras
    paper was not obtained. No title or inaccessible text was paraphrased into evidence.
    This prevents a completed whole-record verdict despite the independently confirmed
    scope issue.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - comayras
  - validation
- assessment_id: history
  area: ownership
  topic: Status, audit trail and maintained owner
  outcome: supported
  summary: The native record remains PROPOSED. Inline events and the append-only creation
    history were read; the review changes neither. Scientific correction belongs in
    the maintained YAML through the guarded writer, not in rendered products.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  evidence_ids:
  - native
  - prior
findings:
- finding_id: F1
  issue_key: chromatophore-bc1-return-carrier-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Bound the c2 return-carrier route to its demonstrated organism context
  description: The definition and function unconditionally route purple-bacterial
    chromatophore bc1 electrons through soluble cytochrome c2; the general-scope graph
    also names c2 and an RC-LH1-PufX partner. The source organism is R. sphaeroides,
    while inspected primary literature distinguishes other purple-bacterial return
    carriers and resolves a T. tepidum HiPIP:LH1-RC complex. Keep the broader complex
    identity separate from the organism-specific c2/PufX pathway. This is a scope
    defect, not a claim that c2 is wrong for R. sphaeroides or that every alternative
    carrier is interchangeable.
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  field_paths:
  - definition
  - functions[photosynthetic_electron_transport].description
  - causal_graphs[chromatophore_bc1_quinol_oxidation].description
  - causal_graphs[chromatophore_bc1_quinol_oxidation].scope_notes
  - causal_graphs[chromatophore_bc1_quinol_oxidation].edges
  evidence_ids:
  - native
  - comayras
  - hipip
  - location
  rule_id: review-checklist:taxonomic-and-edge-level-evidence-scope
  native_severity: major
  normalization_reason: Material scope inflation affects the class definition and
    machine-readable functional graph, while the record identity remains recognizable.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Generalize the class definition to appropriate periplasmic electron
    carriers and explicitly scope the c2/RC-LH1-PufX function and graph to the supported
    R. sphaeroides system, or otherwise supply a precisely delimited narrower identity.
    Attach inspected evidence at the changed claims. Obtain and inspect the original
    paper before closing the remaining attribution uncertainty.
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
    role: maintained scientific record
  generator: just render; native embedding workflow if the semantic projection changes
  acceptance_checks:
  - No general purple-bacterial assertion requires c2 or RC-LH1-PufX; the named R.
    sphaeroides c2 route is retained with explicit scope.
  - Claim-level citations are inspected; unavailable original-paper support is not
    silently marked verified.
  - Guarded writer, new curation event and append-only repository history; PROPOSED
    status and all prior artifacts preserved.
  - Fresh target validation, authoritative full QC, rendered/embedding drift checks
    and a lineage-linked evidence-backed successor review.
limitations:
- Original Comayras full text remains unavailable; the readable abstract is not proof
  that omitted bc1 details are absent from the paper. The failed first HAL query was
  a syntax/API error, not zero results; the corrected quoted DOI query returned0.
- Kawakami Introduction, Structural overview and co-crystallization Methods were completely
  read in bounded tool output; Discussion was read, but not all supplementary material.
  No figure-pixel analysis, new measurement, structural refinement or direct in vivo
  flux inference was performed.
- A successful network-control run does not mean every fresh-cache identifier was
  refetched. Label validation retains603 no-adapter skips; CURIE validation251 documented
  skips; prior full QC three skipped tests. No biological claims are inferred from
  those skips.
- The iModulonDB inventory lacks the named organism; expression-module noncoverage
  is not a negative localization or phenotype result.
- Bounded local predecessor search includes ignored files; it is not an exhaustive
  current GitHub issue triage. No new external issue, PR, push or merge was performed.
- Only this issue-bearing bundle is written. Native scientific data, histories and
  generated products are unchanged. Existing local publication approval remains outstanding.
tags:
- scientific-review
- energy-complex
- carrier-scope
- partial
```
