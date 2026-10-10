# bacterial-type flagellum stator complex: finding dispositions

- Review: 20261010T225636Z-flagellar-stator-complex-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T22:51:14Z
- Finished UTC: 2026-10-10T22:56:36Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Every finding in the linked predecessor is resolved in the inspected maintained inputs. Native scientific status remains PROPOSED.

## Scope And Provenance

Reassessment of the exact prior finding fields, changed claim evidence and append-only provenance, not a new whole-record or corpus-wide assessment. Unchanged assertions retain the original review scope and limitations.

Selection: All findings in 20261010T224657Z-flagellar-stator-complex-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 86c4a1bf7e2c617a2d5d5e36c78fce4dbbebcd73.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0120101 | data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml | maintained | bacterial-type flagellum stator complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0120101 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| strict | passed | True | GO:0120101 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| snippets | passed | True | GO:0120101 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. There are no quoted snippet fields in this target; this is not validation of paraphrase meaning. |
| history | passed | True | GO:0120101 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| labels | passed | True | GO:0120101 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| traits | passed | True | GO:0120101 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| curies | passed | True | GO:0120101 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. Unsupported namespaces remain explicitly skipped; scoped authority verification is retained in source evidence. |
| regressions | passed | True | GO:0120101 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| reviews | passed | True | GO:0120101 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| diff | passed | True | GO:0120101 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| Exact-fix-commit authoritative CI QC | passed | True | GO:0120101 | Verified successful authoritative QC step on the exact inspected fix commit, including all corpus tests, generated-site and text-map drift checks. |

## Scientific And Domain Assessments

### Rotation claims exceed the context of the cited 2020 models

evidence: supported. Targets: GO:0120101.

The A-subunit role, torque function, graph summary and rotation/torque edges distinguish 2020 models from direct E. coli MotA rotation evidence and its limits.

### Dynamic exchange lacks a directly matched source and experimental scope

evidence: supported. Targets: GO:0120101.

The anchoring function separately cites Leake 2006 for measured E. coli turnover and does not imply that static structural/anchoring experiments measured exchange in all motors.

### A-subunit label-only decision is contradicted by an exact family

evidence: supported. Targets: GO:0120101.

The A component now uses verified IPR047055 and its canonical label, with the former label-only decision explicitly superseded in a dated note. MotA/PomA symbols and the B-subunit label-only boundary remain intact.

## Findings

### F1: Rotation claims exceed the context of the cited 2020 models

minor / resolved / confirmed; issue key: flagellar-stator-rotation-evidence-scope.

The A-subunit role, torque function, graph summary and rotation/torque edges distinguish 2020 models from direct E. coli MotA rotation evidence and its limits.

Disposition: The A-subunit role, torque function, graph summary and rotation/torque edges distinguish 2020 models from direct E. coli MotA rotation evidence and its limits. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

### F2: Dynamic exchange lacks a directly matched source and experimental scope

minor / resolved / confirmed; issue key: flagellar-stator-exchange-evidence-scope.

The anchoring function separately cites Leake 2006 for measured E. coli turnover and does not imply that static structural/anchoring experiments measured exchange in all motors.

Disposition: The anchoring function separately cites Leake 2006 for measured E. coli turnover and does not imply that static structural/anchoring experiments measured exchange in all motors. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

### F3: A-subunit label-only decision is contradicted by an exact family

minor / resolved / confirmed; issue key: flagellar-stator-mota-family-grounding.

The A component now uses verified IPR047055 and its canonical label, with the former label-only decision explicitly superseded in a dated note. MotA/PomA symbols and the B-subunit label-only boundary remain intact.

Disposition: The A component now uses verified IPR047055 and its canonical label, with the former label-only decision explicitly superseded in a dated note. MotA/PomA symbols and the B-subunit label-only boundary remain intact. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml; Entire target YAML, schema and recorded input histories | context_only | Re-read the changed target and complete diff against the predecessor; all identified claim corrections are present, with unchanged prior curation events and PROPOSED status. |
| paper-01 | DOI:10.1016/S0022-2836(03)00096-2; Abstract | supports | Abstract: ion-coupling experiments with Mot/Pom chimeras distinguish the A/B core from MotX/MotY accessories. |
| paper-03 | DOI:10.1016/j.cell.2020.08.016; Abstract | supports | Abstract: five MotA and two MotB subunits were resolved; motion and switching were mechanistic models, not direct movies. Campylobacter provenance independently checked with EMDB. |
| paper-05 | DOI:10.1016/j.str.2018.02.016; Abstract | supports | Abstract: MotB L119P fragment binds peptidoglycan; NMR, crystallography and in-vivo crosslinking support activation-linked rearrangement. Not a stator-turnover experiment. |
| paper-09 | DOI:10.1038/nrmicro1887; Review context | supports | Review context: coordinated assembly and conditional occurrence in flagellated bacteria; not an all-Bacteria prevalence census. |
| paper-11 | DOI:10.1038/s41564-020-0788-8; Full text Results, coupling-of-ion-flow section, Discussion and Methods | supports | Full text Results, coupling-of-ion-flow section, Discussion and Methods: 5:2 stators include Vibrio PomAB and MotAB preparations; processive rotation and oscillating ratchet were alternative models. |
| paper-23 | DOI:10.3389/fmicb.2015.00023; Review abstract and established comparative context | supports | Review abstract and established comparative context: archaella are type-IV-pilus-related, not bacterial flagellar structures. |
| paper-24 | DOI:10.7554/eLife.48979; Full text Introduction and Discussion | supports | Full text Introduction and Discussion: Borrelia in-situ stator contacts and conformational changes; exchange is cited for other systems and may differ in scaffolded motors. |
| go-0009274 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009274; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| go-0009433 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009433; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| go-0120100 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120100; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| go-0120101 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120101; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-197 | https://rest.uniprot.org/taxonomy/197.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| hosu2025 | DOI:10.1073/pnas.2515291122; Results, Fig. 2, Discussion and Methods | supports | E. coli polarized photobleaching measures MotA rotation relative to anchored MotB; this does not measure rotation direction or every sodium stator. |
| leake2006 | DOI:10.1038/nature05135; Primary abstract | supports | GFP-MotB exchange measured in functioning E. coli motors by fluorescence recovery/loss; does not establish exchange in every bacterial motor. |
| ipr047055 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR047055/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| ipr022522 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022522/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| ipr025713 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR025713/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| ipr050330 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050330/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| ipr002898 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002898/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| ipr006665 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006665/; Entry type and complete family/domain description | supports | MotA-like is an integrated family explicitly including MotA/PomA/LafT. Alternatives are narrower, broad domains, or unrelated-family mixtures. |
| mota-proteins | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AmotA+AND+reviewed%3Atrue&amp;format=json&amp;size=5; Reviewed exact-gene search, first five results | supports | Bounded gene search cross-checks family matches; an empty PomB result is not proof of biological or database absence. |
| motb-proteins | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AmotB+AND+reviewed%3Atrue&amp;format=json&amp;size=5; Reviewed exact-gene search, first five results | supports | Bounded gene search cross-checks family matches; an empty PomB result is not proof of biological or database absence. |
| poma-proteins | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApomA+AND+reviewed%3Atrue&amp;format=json&amp;size=5; Reviewed exact-gene search, first five results | supports | Bounded gene search cross-checks family matches; an empty PomB result is not proof of biological or database absence. |
| pomb-proteins | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApomB+AND+reviewed%3Atrue&amp;format=json&amp;size=5; Reviewed exact-gene search, first five results | supports | Bounded gene search cross-checks family matches; an empty PomB result is not proof of biological or database absence. |
| campylobacter-structure | https://www.ebi.ac.uk/emdb/api/entry/EMD-10828; Deposited sample and publication metadata | supports | Campylobacter jejuni MotAB deposition linked to Santiveri 2020 supports canonical organism and solved stoichiometry context. |
| prior-search | reviews/structured/ and reports/yaml_record_review/; Exact target IDs, labels and slugs | context_only | No canonical assessment targeting this exact record; related whole-flagellum/basal-body/C-ring reviews are context, not predecessors. |
| predecessor | reviews/structured/20261010T224657Z-flagellar-stator-complex-audit/review.yaml | context_only | Immutable original observation; exact issue keys and finding identities are preserved in the successor. |
| preservation | /private/tmp/csm-review-20261010T223824Z/preservation.json | supports | Verified only three scientific records changed; the clean rotor record remained unchanged, all pre-existing history/review/legacy-report bytes remained unchanged, and prior in-record events and native PROPOSED status were preserved. |

## Limits And Additional Notes

- Scoped same-agent disposition of prior findings, not human scientific approval or completion of the 909-record review goal.
- Original source access tiers, snapshots and access times are retained. Abstract-only access and failed full-text routes are not upgraded to unseen full-text evidence.
- Organism/preparation context is retained; structural models are distinct from measured molecular dynamics, and a new experiment does not retroactively change an older source's methods.
- The global identifier checker skips unsupported namespaces; separately inspected exact authorities provide scoped support, not blanket certification.
- Full QC is verified CI at the exact fix commit. Final review-only PR-head and merge-queue checks remain separate publication gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T225636Z-flagellar-stator-complex-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum stator complex: finding dispositions'
started_at: '2026-10-10T22:51:14Z'
finished_at: '2026-10-10T22:56:36Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent evidence-backed verification of the exact saved findings
    after curation; separate adversarial diff pass is recorded on the PR. Not independent
    human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Every finding in the linked predecessor is resolved in the inspected maintained
  inputs. Native scientific status remains PROPOSED.
source:
  git_revision: 86c4a1bf7e2c617a2d5d5e36c78fce4dbbebcd73
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
  - path: data/structures/appendage/bacterial_type_flagellum_motor.yaml
    sha256: d89fe6a4eba32214dc3ead7400cee889208b1133dc6edcf7ed6ba24969e6fc0e
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    sha256: 897c01817ac11985b892e136b95d8549e5a11ce36c85ac144e6d9f3d8811f680
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
  - path: history/records/bacterial_type_flagellum_stator_complex/2026-09-08T041542Z-claude-481cc0.yaml
    sha256: f6f23ba5694ed8776617d40f66a2592c03792569ab08a171d2e455afabd59cb1
    role: context
  - path: history/records/bacterial_type_flagellum_stator_complex/2026-09-08T042328Z-claude-605873.yaml
    sha256: 29fdc402ec53d0d2c0d84e08443d20409e8a033b700593132c59a473109ae240
    role: context
  - path: history/records/bacterial_type_flagellum_stator_complex/2026-09-08T042544Z-claude-158451.yaml
    sha256: 7485b67815635fcc667d59494b6c17554278f4750eb71a7a45c5a593137b88fa
    role: context
  - path: history/records/bacterial_type_flagellum_stator_complex/2026-10-10T224851Z-codex-3799ac.yaml
    sha256: 42faaec009e848223a9ee276a2c921285b4fa49459edc214073f65ee0bbbcb17
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T224657Z-flagellar-stator-complex-audit/review.yaml
    sha256: a899c0cb73d7d215bdbeeb45eaf1fb2d95372e9d520af85fe0c13d54912ba0a9
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_flagellar_review_corrections.py
    sha256: a7d74cd70dc0ca41e662b3cdedc9315be1927763a43d99ea2668f8af3bf85cb9
    role: context
targets:
- target_id: GO:0120101
  path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
  label: bacterial-type flagellum stator complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
scope:
  description: Reassessment of the exact prior finding fields, changed claim evidence
    and append-only provenance, not a new whole-record or corpus-wide assessment.
    Unchanged assertions retain the original review scope and limitations.
  selection: All findings in 20261010T224657Z-flagellar-stator-complex-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0120101
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:50:05Z to 2026-10-10T22:50:07Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:50:07Z to 2026-10-10T22:50:11Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    --report /private/tmp/csm-review-20261010T223824Z/post-checks/bacterial_type_flagellum_stator_complex-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text. There are no quoted snippet fields in this target;
    this is not validation of paraphrase meaning.
  scope_note: 2026-10-10T22:50:11Z to 2026-10-10T22:50:30Z; log SHA-256 1a5bfca75c79a4da3b5001c29007e5361c3cdcb859842211008955f1261284a4
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:50:30Z to 2026-10-10T22:50:43Z; log SHA-256 4b9a602c272c2a2c4b63a7fe2117a11dd354c25b685adcde10c8e4ceea274afe
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:50:43Z to 2026-10-10T22:52:17Z; log SHA-256 4e7c08d40597390917ae73f20ed6755095022904244e88833405c338595173d1
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:52:17Z to 2026-10-10T22:52:49Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text. Unsupported namespaces remain explicitly skipped;
    scoped authority verification is retained in source evidence.
  scope_note: 2026-10-10T22:52:49Z to 2026-10-10T22:53:38Z; log SHA-256 9ad86316c2e158c953f2c820b4057f696eabe90e3e5f6ca9cb8b430215bfbaf6
- check_id: regressions
  name: regressions
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python -m pytest -q tests/test_flagellar_review_corrections.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:53:38Z to 2026-10-10T22:54:18Z; log SHA-256 4853891c0b70c5df7838fbd6438cc18eb3e5aa95b5953c98ba5fc23d5601cc5e
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: .venv/bin/python scripts/record_review.py check --base b7453b637b71268e49710d17aa5c34743bce7a6c
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:54:18Z to 2026-10-10T22:55:02Z; log SHA-256 1a7d57ebb94a25d9d9a333a2844804756e7c6c71612407d1c8b07e7d0b67d9fb
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:55:02Z to 2026-10-10T22:55:02Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: qc
  name: Exact-fix-commit authoritative CI QC
  status: passed
  required: true
  target_ids:
  - GO:0120101
  command: gh run view 38092951150 --json databaseId,conclusion,headSha,event,jobs,startedAt,updatedAt,url
  exit_code: 0
  expected_exit_code: 0
  summary: Verified successful authoritative QC step on the exact inspected fix commit,
    including all corpus tests, generated-site and text-map drift checks.
  scope_note: 2026-10-10T22:52:00Z to 2026-10-10T22:55:03Z; https://github.com/CultureBotAI/CellStructureMech/actions/runs/38092951150;
    log SHA-256 beb8056fc61e15b5afddb20274c8c46822df61e40e3fde2fa103b3983443b685
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
  locator: Entire target YAML, schema and recorded input histories
  accessed_at: '2026-10-10T22:56:36Z'
  support: context_only
  summary: Re-read the changed target and complete diff against the predecessor; all
    identified claim corrections are present, with unchanged prior curation events
    and PROPOSED status.
  snapshot_sha256: 897c01817ac11985b892e136b95d8549e5a11ce36c85ac144e6d9f3d8811f680
- evidence_id: paper-01
  kind: primary_source
  reference: DOI:10.1016/S0022-2836(03)00096-2
  locator: Abstract
  accessed_at: '2026-10-10T22:40:29Z'
  snapshot_sha256: 8919ebe29443b7d30762a7138cabf1df7143ee91fc95b5fa462ad4d9415c5a45
  support: supports
  summary: 'Abstract: ion-coupling experiments with Mot/Pom chimeras distinguish the
    A/B core from MotX/MotY accessories.'
- evidence_id: paper-03
  kind: primary_source
  reference: DOI:10.1016/j.cell.2020.08.016
  locator: Abstract
  accessed_at: '2026-10-10T22:40:30Z'
  snapshot_sha256: ed7bc59593098f61fd42172109253eea289f0af4e88155b081df4140b41d23e6
  support: supports
  summary: 'Abstract: five MotA and two MotB subunits were resolved; motion and switching
    were mechanistic models, not direct movies. Campylobacter provenance independently
    checked with EMDB.'
- evidence_id: paper-05
  kind: primary_source
  reference: DOI:10.1016/j.str.2018.02.016
  locator: Abstract
  accessed_at: '2026-10-10T22:40:31Z'
  snapshot_sha256: 0ef80132e76e1f74714ebf8df86b2bc29919e795704f8da61348d97d44ea139a
  support: supports
  summary: 'Abstract: MotB L119P fragment binds peptidoglycan; NMR, crystallography
    and in-vivo crosslinking support activation-linked rearrangement. Not a stator-turnover
    experiment.'
- evidence_id: paper-09
  kind: primary_source
  reference: DOI:10.1038/nrmicro1887
  locator: Review context
  accessed_at: '2026-10-10T22:40:35Z'
  snapshot_sha256: 648eac60aca511dba55bd983fcc746cd1c173f143b5259fa8bd78daa609ca3c6
  support: supports
  summary: 'Review context: coordinated assembly and conditional occurrence in flagellated
    bacteria; not an all-Bacteria prevalence census.'
- evidence_id: paper-11
  kind: primary_source
  reference: DOI:10.1038/s41564-020-0788-8
  locator: Full text Results, coupling-of-ion-flow section, Discussion and Methods
  accessed_at: '2026-10-10T22:40:39Z'
  snapshot_sha256: 2250b535735358b44b02046731afdf6ad1fac623468bfd82d7145248b1a6b072
  support: supports
  summary: 'Full text Results, coupling-of-ion-flow section, Discussion and Methods:
    5:2 stators include Vibrio PomAB and MotAB preparations; processive rotation and
    oscillating ratchet were alternative models.'
- evidence_id: paper-23
  kind: primary_source
  reference: DOI:10.3389/fmicb.2015.00023
  locator: Review abstract and established comparative context
  accessed_at: '2026-10-10T22:40:56Z'
  snapshot_sha256: 5e2b4c125d1d01c22b2d7eb326b7e73bb6b17e9d1c0b660c785ea11667745677
  support: supports
  summary: 'Review abstract and established comparative context: archaella are type-IV-pilus-related,
    not bacterial flagellar structures.'
- evidence_id: paper-24
  kind: primary_source
  reference: DOI:10.7554/eLife.48979
  locator: Full text Introduction and Discussion
  accessed_at: '2026-10-10T22:40:59Z'
  snapshot_sha256: bf6a96bd205a6cbaea786a35c1c2c68367f8d7f97ddddea875c45760113e1b68
  support: supports
  summary: 'Full text Introduction and Discussion: Borrelia in-situ stator contacts
    and conformational changes; exchange is cited for other systems and may differ
    in scaffolded motors.'
- evidence_id: go-0009274
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009274
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:00Z'
  snapshot_sha256: 7537b72bc1f481b91ed2b9eb404bf7b61ddc0c3d4c04a1745d5c33ad7af1b604
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: go-0009433
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009433
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:02Z'
  snapshot_sha256: 2dff37996895f1d80a7d89878d916a2fbcd0c787ca925b7223375f9ba3e66a40
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: go-0120100
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120100
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:03Z'
  snapshot_sha256: 66ebccd6448ecf8935cb12ab851dd382e1cf09579d0eec0c58619bb30497a73b
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: go-0120101
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120101
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:04Z'
  snapshot_sha256: b66361210ff4cadc3cbf771ff6415a9f205fcfddf22b234a2428339f1ed43eff
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: ncbitaxon-197
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/197.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:16Z'
  snapshot_sha256: 7346dd32eb9f3fb96e5a5f775bb9a0dc8dc761a5dd41712b84d65f148ed90c77
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: ncbitaxon-2
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:17Z'
  snapshot_sha256: 8074c9bcd59cd4da1da4bc9ec98c040bbecd52ef5c91c4c4bb9bed0f3a7cb5a9
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: ncbitaxon-2157
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2157.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:17Z'
  snapshot_sha256: 14f5852a1db0f9f5ef8d60e4a11c1916bf005bf549c57dd4bc860d39194a1799
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: hosu2025
  kind: primary_source
  reference: DOI:10.1073/pnas.2515291122
  locator: Results, Fig. 2, Discussion and Methods
  accessed_at: '2026-10-10T22:41:32Z'
  snapshot_sha256: fc24ba6f21145cc7393d410061c9fbb338353d85222338758e4173c9b6220533
  support: supports
  summary: E. coli polarized photobleaching measures MotA rotation relative to anchored
    MotB; this does not measure rotation direction or every sodium stator.
- evidence_id: leake2006
  kind: primary_source
  reference: DOI:10.1038/nature05135
  locator: Primary abstract
  accessed_at: '2026-10-10T22:41:33Z'
  snapshot_sha256: 19f0bc7def0abb3a8030edd50960e52d32268f16ba670a9bb07dd951f80a390b
  support: supports
  summary: GFP-MotB exchange measured in functioning E. coli motors by fluorescence
    recovery/loss; does not establish exchange in every bacterial motor.
- evidence_id: ipr047055
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR047055/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:40Z'
  snapshot_sha256: 7d009e86c040fd31abe97acd37092073a3ce78b4e3e717fb943c059d9f77549a
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: ipr022522
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022522/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:36Z'
  snapshot_sha256: 4bd53a0b33400552433dbdc83e05095e6260544b67bb8442d89d374558ec5b7a
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: ipr025713
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR025713/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:37Z'
  snapshot_sha256: 67caa5798ab5a42b0dd34ea7829d017d753079b26217da4167f6e8b68f28ba29
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: ipr050330
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050330/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:40Z'
  snapshot_sha256: 34125ff0dbe649f6cdf83e47f283d084ece2d1a7537572e0b5444282850d7288
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: ipr002898
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002898/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:33Z'
  snapshot_sha256: 9b24f5c01cc61ab3b12873224dbdf95e84eac06794b1253f677e61fa6b8e0de2
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: ipr006665
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006665/
  locator: Entry type and complete family/domain description
  accessed_at: '2026-10-10T22:42:34Z'
  snapshot_sha256: c170b9b182156f8b2e5310140f94899b9a8a2ef8ae4c5add06d60cfa29f862ec
  support: supports
  summary: MotA-like is an integrated family explicitly including MotA/PomA/LafT.
    Alternatives are narrower, broad domains, or unrelated-family mixtures.
- evidence_id: mota-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AmotA+AND+reviewed%3Atrue&format=json&size=5
  locator: Reviewed exact-gene search, first five results
  accessed_at: '2026-10-10T22:42:29Z'
  snapshot_sha256: 9b503de9ab55c664ee7feeb9baf5cd6bd398070b87eae28a34e02c3d4b7cce62
  support: supports
  summary: Bounded gene search cross-checks family matches; an empty PomB result is
    not proof of biological or database absence.
- evidence_id: motb-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AmotB+AND+reviewed%3Atrue&format=json&size=5
  locator: Reviewed exact-gene search, first five results
  accessed_at: '2026-10-10T22:42:30Z'
  snapshot_sha256: ea9f75ef99ea68c3e2e6d77fc3cb5cf18e7f1bfb15c799d00936da009a672eaa
  support: supports
  summary: Bounded gene search cross-checks family matches; an empty PomB result is
    not proof of biological or database absence.
- evidence_id: poma-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApomA+AND+reviewed%3Atrue&format=json&size=5
  locator: Reviewed exact-gene search, first five results
  accessed_at: '2026-10-10T22:42:31Z'
  snapshot_sha256: 7723ca9e4c0f108706cbb98882ce7c57409c081504eaf45f5cdad7313053906a
  support: supports
  summary: Bounded gene search cross-checks family matches; an empty PomB result is
    not proof of biological or database absence.
- evidence_id: pomb-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApomB+AND+reviewed%3Atrue&format=json&size=5
  locator: Reviewed exact-gene search, first five results
  accessed_at: '2026-10-10T22:42:31Z'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  support: supports
  summary: Bounded gene search cross-checks family matches; an empty PomB result is
    not proof of biological or database absence.
- evidence_id: campylobacter-structure
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-10828
  locator: Deposited sample and publication metadata
  accessed_at: '2026-10-10T22:43:46Z'
  snapshot_sha256: 9d1f0ef2fe20e53e19516c805d73366d52df3f54774f033fe17c5449511833cc
  support: supports
  summary: Campylobacter jejuni MotAB deposition linked to Santiveri 2020 supports
    canonical organism and solved stoichiometry context.
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/ and reports/yaml_record_review/
  locator: Exact target IDs, labels and slugs
  accessed_at: '2026-10-10T22:46:57Z'
  support: context_only
  search_scope: Path.rglob parsed all 48 canonical review YAMLs including ignored/hidden
    entries; rg --no-ignore --hidden searched reviews and legacy reports for target
    IDs/slugs.
  summary: No canonical assessment targeting this exact record; related whole-flagellum/basal-body/C-ring
    reviews are context, not predecessors.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261010T224657Z-flagellar-stator-complex-audit/review.yaml
  accessed_at: '2026-10-10T22:56:36Z'
  snapshot_sha256: a899c0cb73d7d215bdbeeb45eaf1fb2d95372e9d520af85fe0c13d54912ba0a9
  support: context_only
  summary: Immutable original observation; exact issue keys and finding identities
    are preserved in the successor.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261010T223824Z/preservation.json
  accessed_at: '2026-10-10T22:50:03Z'
  snapshot_sha256: 2d49265ee6570d83a496653da30e82cfe8eec93ce91d2014b43c915e7a5741de
  support: supports
  summary: Verified only three scientific records changed; the clean rotor record
    remained unchanged, all pre-existing history/review/legacy-report bytes remained
    unchanged, and prior in-record events and native PROPOSED status were preserved.
assessments:
- assessment_id: resolved-f1
  area: evidence
  topic: Rotation claims exceed the context of the cited 2020 models
  outcome: supported
  target_ids:
  - GO:0120101
  evidence_ids:
  - record
  - paper-03
  - paper-11
  - hosu2025
  - predecessor
  - preservation
  summary: The A-subunit role, torque function, graph summary and rotation/torque
    edges distinguish 2020 models from direct E. coli MotA rotation evidence and its
    limits.
- assessment_id: resolved-f2
  area: evidence
  topic: Dynamic exchange lacks a directly matched source and experimental scope
  outcome: supported
  target_ids:
  - GO:0120101
  evidence_ids:
  - record
  - paper-05
  - paper-24
  - leake2006
  - predecessor
  - preservation
  summary: The anchoring function separately cites Leake 2006 for measured E. coli
    turnover and does not imply that static structural/anchoring experiments measured
    exchange in all motors.
- assessment_id: resolved-f3
  area: evidence
  topic: A-subunit label-only decision is contradicted by an exact family
  outcome: supported
  target_ids:
  - GO:0120101
  evidence_ids:
  - record
  - ipr047055
  - mota-proteins
  - poma-proteins
  - predecessor
  - preservation
  summary: The A component now uses verified IPR047055 and its canonical label, with
    the former label-only decision explicitly superseded in a dated note. MotA/PomA
    symbols and the B-subunit label-only boundary remain intact.
findings:
- finding_id: F1
  issue_key: flagellar-stator-rotation-evidence-scope
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Rotation claims exceed the context of the cited 2020 models
  description: The A-subunit role, torque function, graph summary and rotation/torque
    edges distinguish 2020 models from direct E. coli MotA rotation evidence and its
    limits.
  target_ids:
  - GO:0120101
  field_paths:
  - causal_graphs[0].edges
  - functions[0]
  - components[0].role
  - causal_graphs[0].description
  evidence_ids:
  - record
  - paper-03
  - paper-11
  - hosu2025
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded provenance, claim-qualification or grounding defect;
    record identity is sound.
  disposition_reason: The A-subunit role, torque function, graph summary and rotation/torque
    edges distinguish 2020 models from direct E. coli MotA rotation evidence and its
    limits. Exact affected fields were checked against the cited primary or authority
    evidence and passing post-curation gates.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T224657Z-flagellar-stator-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2160
- finding_id: F2
  issue_key: flagellar-stator-exchange-evidence-scope
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Dynamic exchange lacks a directly matched source and experimental scope
  description: The anchoring function separately cites Leake 2006 for measured E.
    coli turnover and does not imply that static structural/anchoring experiments
    measured exchange in all motors.
  target_ids:
  - GO:0120101
  field_paths:
  - functions[1]
  evidence_ids:
  - record
  - paper-05
  - paper-24
  - leake2006
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded provenance, claim-qualification or grounding defect;
    record identity is sound.
  disposition_reason: The anchoring function separately cites Leake 2006 for measured
    E. coli turnover and does not imply that static structural/anchoring experiments
    measured exchange in all motors. Exact affected fields were checked against the
    cited primary or authority evidence and passing post-curation gates.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T224657Z-flagellar-stator-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2161
- finding_id: F3
  issue_key: flagellar-stator-mota-family-grounding
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: A-subunit label-only decision is contradicted by an exact family
  description: The A component now uses verified IPR047055 and its canonical label,
    with the former label-only decision explicitly superseded in a dated note. MotA/PomA
    symbols and the B-subunit label-only boundary remain intact.
  target_ids:
  - GO:0120101
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  evidence_ids:
  - record
  - ipr047055
  - mota-proteins
  - poma-proteins
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_stator_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded provenance, claim-qualification or grounding defect;
    record identity is sound.
  disposition_reason: The A component now uses verified IPR047055 and its canonical
    label, with the former label-only decision explicitly superseded in a dated note.
    MotA/PomA symbols and the B-subunit label-only boundary remain intact. Exact affected
    fields were checked against the cited primary or authority evidence and passing
    post-curation gates.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T224657Z-flagellar-stator-complex-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2162
actions: []
limitations:
- Scoped same-agent disposition of prior findings, not human scientific approval or
  completion of the 909-record review goal.
- Original source access tiers, snapshots and access times are retained. Abstract-only
  access and failed full-text routes are not upgraded to unseen full-text evidence.
- Organism/preparation context is retained; structural models are distinct from measured
  molecular dynamics, and a new experiment does not retroactively change an older
  source's methods.
- The global identifier checker skips unsupported namespaces; separately inspected
  exact authorities provide scoped support, not blanket certification.
- Full QC is verified CI at the exact fix commit. Final review-only PR-head and merge-queue
  checks remain separate publication gates.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261010T224657Z-flagellar-stator-complex-audit
  relationship: Resolves all exact predecessor findings without rewriting the original
    observation.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2160
- https://github.com/CultureBotAI/CellStructureMech/issues/2161
- https://github.com/CultureBotAI/CellStructureMech/issues/2162
```
