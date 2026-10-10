# bacterial-type flagellum secretion apparatus: finding dispositions

- Review: 20261010T225629Z-flagellar-secretion-apparatus-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-10T22:51:12Z
- Finished UTC: 2026-10-10T22:56:29Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Every finding in the linked predecessor is resolved in the inspected maintained inputs. Native scientific status remains PROPOSED.

## Scope And Provenance

Reassessment of the exact prior finding fields, changed claim evidence and append-only provenance, not a new whole-record or corpus-wide assessment. Unchanged assertions retain the original review scope and limitations.

Selection: All findings in 20261010T224657Z-flagellar-secretion-apparatus-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 86c4a1bf7e2c617a2d5d5e36c78fce4dbbebcd73.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0120102 | data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml | maintained | bacterial-type flagellum secretion apparatus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0120102 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| strict | passed | True | GO:0120102 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| snippets | passed | True | GO:0120102 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. There are no quoted snippet fields in this target; this is not validation of paraphrase meaning. |
| history | passed | True | GO:0120102 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| labels | passed | True | GO:0120102 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| traits | passed | True | GO:0120102 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| curies | passed | True | GO:0120102 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. Unsupported namespaces remain explicitly skipped; scoped authority verification is retained in source evidence. |
| regressions | passed | True | GO:0120102 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| reviews | passed | True | GO:0120102 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| diff | passed | True | GO:0120102 | Actual post-curation check passed. Biological support was separately reassessed against inspected source text. |
| Exact-fix-commit authoritative CI QC | passed | True | GO:0120102 | Verified successful authoritative QC step on the exact inspected fix commit, including all corpus tests, generated-site and text-map drift checks. |

## Scientific And Domain Assessments

### Modern export-core architecture is falsely attributed to Fukumura 2017

evidence: supported. Targets: GO:0120102.

Current counts, geometry and exemplar cite Salmonella PQR in Kuhlen 2018 and Vibrio PQR-FlhB in Kuhlen 2020. FlhB wraps the base; FliR is integrated and FliQ peripheral. The historical 2017 evidence and FliO decision remain, without false modern-count or assembly-order attribution.

### ATPase model is described as a resolved complete complex

evidence: supported. Targets: GO:0120102.

All three ATPase component count fields and relevant notes distinguish the modeled FliH12-FliI6-FliJ1 assembly from the solved FliH C-terminal dimer-FliI heterotrimer; the ring edge explicitly identifies the model.

### Sodium coupling is conflated with the intact ATPase-assisted state

evidence: supported. Targets: GO:0120102.

The FlhA role, energy function, graph summary, energy node and edge preserve the experimental Salmonella contrast: intact ATPase-assisted PMF export versus sodium-capable ATPase-compromised export.

## Findings

### F1: Modern export-core architecture is falsely attributed to Fukumura 2017

major / resolved / confirmed; issue key: flagellar-export-core-stoichiometry-provenance.

Current counts, geometry and exemplar cite Salmonella PQR in Kuhlen 2018 and Vibrio PQR-FlhB in Kuhlen 2020. FlhB wraps the base; FliR is integrated and FliQ peripheral. The historical 2017 evidence and FliO decision remain, without false modern-count or assembly-order attribution.

Disposition: Current counts, geometry and exemplar cite Salmonella PQR in Kuhlen 2018 and Vibrio PQR-FlhB in Kuhlen 2020. FlhB wraps the base; FliR is integrated and FliQ peripheral. The historical 2017 evidence and FliO decision remain, without false modern-count or assembly-order attribution. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

### F2: ATPase model is described as a resolved complete complex

minor / resolved / confirmed; issue key: flagellar-export-atpase-model-provenance.

All three ATPase component count fields and relevant notes distinguish the modeled FliH12-FliI6-FliJ1 assembly from the solved FliH C-terminal dimer-FliI heterotrimer; the ring edge explicitly identifies the model.

Disposition: All three ATPase component count fields and relevant notes distinguish the modeled FliH12-FliI6-FliJ1 assembly from the solved FliH C-terminal dimer-FliI heterotrimer; the ring edge explicitly identifies the model. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

### F3: Sodium coupling is conflated with the intact ATPase-assisted state

major / resolved / confirmed; issue key: flagellar-export-dual-fuel-atpase-context.

The FlhA role, energy function, graph summary, energy node and edge preserve the experimental Salmonella contrast: intact ATPase-assisted PMF export versus sodium-capable ATPase-compromised export.

Disposition: The FlhA role, energy function, graph summary, energy node and edge preserve the experimental Salmonella contrast: intact ATPase-assisted PMF export versus sodium-capable ATPase-compromised export. Exact affected fields were checked against the cited primary or authority evidence and passing post-curation gates.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml; Entire target YAML, schema and recorded input histories | context_only | Re-read the changed target and complete diff against the predecessor; all identified claim corrections are present, with unchanged prior curation events and PROPOSED status. |
| paper-00 | DOI:10.1007/82_2019_170; Abstract | supports | Abstract: membrane export gate and cytoplasmic ATPase are distinct parts of the basal-body export machinery. |
| paper-02 | DOI:10.1016/j.bbamcr.2013.09.005; Abstract | supports | Abstract: axial protein export, ATPase-assisted entry and FliJ-FlhA coupling; older FliO inventory is refined by later assembly studies. |
| paper-09 | DOI:10.1038/nrmicro1887; Review context | supports | Review context: coordinated assembly and conditional occurrence in flagellated bacteria; not an all-Bacteria prevalence census. |
| paper-12 | DOI:10.1038/s42003-024-06081-0; Full text Introduction, mutant Results and Fig. 1 | supports | Full text Introduction, mutant Results and Fig. 1: FlhA GYXLI-mutant phenotypes support ATPase-assisted ordering; Fig. 1 uses modeled ATPase assembly. |
| paper-13 | DOI:10.1073/pnas.1524025113; Abstract | supports | Abstract: solved FliH C-terminal homodimer-FliI complex is distinct from the proposed hexamer model; complete ATPase assembly was not directly resolved by this paper. |
| paper-16 | DOI:10.1111/mmi.12529; Abstract | supports | Abstract: fluorescence measurements estimate about nine FlhA molecules and show coordinated assembly with the MS ring. |
| paper-18 | DOI:10.1128/JB.181.5.1388-1394.1999; Abstract | supports | Abstract: mutant substrate-export assays distinguish rod/hook and filament export classes; historic uncertainties do not override later FliJ evidence. |
| paper-19 | DOI:10.1128/JB.182.15.4207-4215.2000; Full text Introduction and Discussion | supports | Full text Introduction and Discussion: FliJ interactions are explicitly discussed as prior work; null mutants retain leaky motility, and temperature-shift experiments identify FliJ as a general export factor. |
| paper-20 | DOI:10.1371/journal.pbio.2002281; Full text Introduction and Results, oligomeric state and copurification sections | supports | Full text Introduction and Results, oligomeric state and copurification sections: isolated FliP hexamers and detergent-dependent associations, not FliP5Q4R1FlhB1 reconstruction. |
| paper-21 | DOI:10.1371/journal.pgen.1001143; Abstract and full-text introductory context | supports | Abstract and full-text introductory context: FliO deletion/bypass and coexpression experiments support an assembly/stability role outside the conserved mature core. |
| paper-22 | DOI:10.1371/journal.ppat.1005495; Full text Results sodium blockers, ATPase deletions and Discussion | supports | Full text Results sodium blockers, ATPase deletions and Discussion: sodium-dependent export in ATPase-compromised Salmonella contrasts with PMF-coupled wild type. |
| paper-23 | DOI:10.3389/fmicb.2015.00023; Review abstract and established comparative context | supports | Review abstract and established comparative context: archaella are type-IV-pilus-related, not bacterial flagellar structures. |
| go-0009425 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009425; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| go-0009431 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009431; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| go-0120102 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120102; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr000563 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000563/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr005837 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005837/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr006136 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006136/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr006301 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006301/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr006303 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006303/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr006305 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006305/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| interpro-ipr012823 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012823/; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p0a1k1 | https://rest.uniprot.org/uniprotkb/P0A1K1.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p0a1l5 | https://rest.uniprot.org/uniprotkb/P0A1L5.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p15934 | https://rest.uniprot.org/uniprotkb/P15934.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p26465 | https://rest.uniprot.org/uniprotkb/P26465.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p40727 | https://rest.uniprot.org/uniprotkb/P40727.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p40729 | https://rest.uniprot.org/uniprotkb/P40729.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p54700 | https://rest.uniprot.org/uniprotkb/P54700.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| uniprotkb-p54702 | https://rest.uniprot.org/uniprotkb/P54702.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-2 | https://rest.uniprot.org/taxonomy/2.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-2157 | https://rest.uniprot.org/taxonomy/2157.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-90371 | https://rest.uniprot.org/taxonomy/90371.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| ncbitaxon-99287 | https://rest.uniprot.org/taxonomy/99287.json; Identity, definition, status, family scope, gene and taxon metadata | supports | Live authority identity checked; a protein accession is not experimental membership evidence. |
| kuhlen2018 | DOI:10.1038/s41594-018-0086-9; Results, stoichiometry and helical architecture | supports | Salmonella Typhimurium FliP5Q4R1 is directly reconstructed; FliR is integrated and FliQ is peripheral, not an independently measured assembly sequence. |
| kuhlen2020 | DOI:10.1038/s41467-020-15071-9; Results, architecture, topology and Methods | supports | Vibrio mimicus FliP5Q4R1-FlhB1 shows FlhB around the base; this is not a Salmonella 2017 reconstruction. |
| ipr005714 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005714/; Family scope | supports | Mixed flagellar/injectisome ATPase family and narrower FliI clade support retaining FliI label-only scope. |
| ipr020005 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020005/; Family scope | supports | Mixed flagellar/injectisome ATPase family and narrower FliI clade support retaining FliI label-only scope. |
| prior-search | reviews/structured/ and reports/yaml_record_review/; Exact target IDs, labels and slugs | context_only | No canonical assessment targeting this exact record; related whole-flagellum/basal-body/C-ring reviews are context, not predecessors. |
| predecessor | reviews/structured/20261010T224657Z-flagellar-secretion-apparatus-audit/review.yaml | context_only | Immutable original observation; exact issue keys and finding identities are preserved in the successor. |
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
review_id: 20261010T225629Z-flagellar-secretion-apparatus-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'bacterial-type flagellum secretion apparatus: finding dispositions'
started_at: '2026-10-10T22:51:12Z'
finished_at: '2026-10-10T22:56:29Z'
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
  - path: data/structures/appendage/bacterial_type_flagellum_basal_body.yaml
    sha256: b73592ad4ea2dc9ea818266c440fb1e8e8070461592051cc9fa5c9c0c2a5c704
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    sha256: 1e9ed7330db81ab6f1d036d9c0ddc72e38e1c1232d0736f1518bab3cf04def6f
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
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-09-08T055224Z-claude-bc0dba.yaml
    sha256: 80a5ef3637eb2418cc604ee423af6348b2c45d3a43a18c7d1c45f0c753b6ffae
    role: context
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-09-08T055441Z-claude-68f36e.yaml
    sha256: 5e99658109c70a538b3342395310c86e4e9f120ccd3e98c3580a87aba33b9a2a
    role: context
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-09-08T063710Z-claude-886121.yaml
    sha256: d215737aa30dd4629698a4a5463f0b0de9248901e94ec183fbda34ddf613ef2f
    role: context
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-09-08T064542Z-claude-624821.yaml
    sha256: 6cee8b94451a3941c494fa373db8c0b57d3c644812a7987a881a3734d90bd6a4
    role: context
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-09-08T065716Z-claude-3234a8.yaml
    sha256: b7ccb84d2c5b8ab7a17a72b0a0af54b87a8a02fe4733d2ba74f63a2c57ed7ecf
    role: context
  - path: history/records/bacterial_type_flagellum_secretion_apparatus/2026-10-10T224849Z-codex-dae673.yaml
    sha256: 6305bc87227c168734f5261fe6af98c032e6b0ff843f31090a6b1b3f32c7f32e
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T224657Z-flagellar-secretion-apparatus-audit/review.yaml
    sha256: 5a693c8205865469efaeca03aa8838d4f104525f7134c7d5b6895caaa623dcdb
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
- target_id: GO:0120102
  path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
  label: bacterial-type flagellum secretion apparatus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
scope:
  description: Reassessment of the exact prior finding fields, changed claim evidence
    and append-only provenance, not a new whole-record or corpus-wide assessment.
    Unchanged assertions retain the original review scope and limitations.
  selection: All findings in 20261010T224657Z-flagellar-secretion-apparatus-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0120102
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0120102
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:49:39Z to 2026-10-10T22:49:41Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0120102
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text.
  scope_note: 2026-10-10T22:49:41Z to 2026-10-10T22:49:45Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0120102
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    --report /private/tmp/csm-review-20261010T223824Z/post-checks/bacterial_type_flagellum_secretion_apparatus-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed. Biological support was separately reassessed
    against inspected source text. There are no quoted snippet fields in this target;
    this is not validation of paraphrase meaning.
  scope_note: 2026-10-10T22:49:45Z to 2026-10-10T22:50:05Z; log SHA-256 3e19e3016f18693d97dfe0cbb6febb7a00b04f6570ced9fb34db3611042bff93
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  - GO:0120102
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
  reference: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
  locator: Entire target YAML, schema and recorded input histories
  accessed_at: '2026-10-10T22:56:29Z'
  support: context_only
  summary: Re-read the changed target and complete diff against the predecessor; all
    identified claim corrections are present, with unchanged prior curation events
    and PROPOSED status.
  snapshot_sha256: 1e9ed7330db81ab6f1d036d9c0ddc72e38e1c1232d0736f1518bab3cf04def6f
- evidence_id: paper-00
  kind: primary_source
  reference: DOI:10.1007/82_2019_170
  locator: Abstract
  accessed_at: '2026-10-10T22:40:28Z'
  snapshot_sha256: 094767a5fb71610b43bac3627fc935a1fb967390844a1e8066c891674acd192d
  support: supports
  summary: 'Abstract: membrane export gate and cytoplasmic ATPase are distinct parts
    of the basal-body export machinery.'
- evidence_id: paper-02
  kind: primary_source
  reference: DOI:10.1016/j.bbamcr.2013.09.005
  locator: Abstract
  accessed_at: '2026-10-10T22:40:29Z'
  snapshot_sha256: 768fdf17054ce15656cd912d6c62453168a473b0b797ae87873af30bbfdd566a
  support: supports
  summary: 'Abstract: axial protein export, ATPase-assisted entry and FliJ-FlhA coupling;
    older FliO inventory is refined by later assembly studies.'
- evidence_id: paper-09
  kind: primary_source
  reference: DOI:10.1038/nrmicro1887
  locator: Review context
  accessed_at: '2026-10-10T22:40:35Z'
  snapshot_sha256: 648eac60aca511dba55bd983fcc746cd1c173f143b5259fa8bd78daa609ca3c6
  support: supports
  summary: 'Review context: coordinated assembly and conditional occurrence in flagellated
    bacteria; not an all-Bacteria prevalence census.'
- evidence_id: paper-12
  kind: primary_source
  reference: DOI:10.1038/s42003-024-06081-0
  locator: Full text Introduction, mutant Results and Fig. 1
  accessed_at: '2026-10-10T22:40:41Z'
  snapshot_sha256: 19258fd6576cbf0b5a726a667e820d14d51f11174007c61426fe6ef8f07b871f
  support: supports
  summary: 'Full text Introduction, mutant Results and Fig. 1: FlhA GYXLI-mutant phenotypes
    support ATPase-assisted ordering; Fig. 1 uses modeled ATPase assembly.'
- evidence_id: paper-13
  kind: primary_source
  reference: DOI:10.1073/pnas.1524025113
  locator: Abstract
  accessed_at: '2026-10-10T22:40:42Z'
  snapshot_sha256: 9342e85433a3a3bf79436962b57ceb97039f92d2a65d19cdff9a2e887d6406c0
  support: supports
  summary: 'Abstract: solved FliH C-terminal homodimer-FliI complex is distinct from
    the proposed hexamer model; complete ATPase assembly was not directly resolved
    by this paper.'
- evidence_id: paper-16
  kind: primary_source
  reference: DOI:10.1111/mmi.12529
  locator: Abstract
  accessed_at: '2026-10-10T22:40:46Z'
  snapshot_sha256: 47b9098caf7be7493c050705a75707031ca7907595972f61051c37f3d2cf3547
  support: supports
  summary: 'Abstract: fluorescence measurements estimate about nine FlhA molecules
    and show coordinated assembly with the MS ring.'
- evidence_id: paper-18
  kind: primary_source
  reference: DOI:10.1128/JB.181.5.1388-1394.1999
  locator: Abstract
  accessed_at: '2026-10-10T22:40:48Z'
  snapshot_sha256: 4bf4116fb7df61b9a40845e045056bb3e2ab2ada22063a2014da1c2b341c4df8
  support: supports
  summary: 'Abstract: mutant substrate-export assays distinguish rod/hook and filament
    export classes; historic uncertainties do not override later FliJ evidence.'
- evidence_id: paper-19
  kind: primary_source
  reference: DOI:10.1128/JB.182.15.4207-4215.2000
  locator: Full text Introduction and Discussion
  accessed_at: '2026-10-10T22:41:31Z'
  snapshot_sha256: 57c2e837c363c9fd3e5933975b7dba79c9e73cee5cf9740084aa3d5ab52ec869
  support: supports
  summary: 'Full text Introduction and Discussion: FliJ interactions are explicitly
    discussed as prior work; null mutants retain leaky motility, and temperature-shift
    experiments identify FliJ as a general export factor.'
- evidence_id: paper-20
  kind: primary_source
  reference: DOI:10.1371/journal.pbio.2002281
  locator: Full text Introduction and Results, oligomeric state and copurification
    sections
  accessed_at: '2026-10-10T22:40:52Z'
  snapshot_sha256: 269798c3e008d2d3c5fc49e39fb99dbb5a12e381b8e9bf106115bb65f8071b60
  support: supports
  summary: 'Full text Introduction and Results, oligomeric state and copurification
    sections: isolated FliP hexamers and detergent-dependent associations, not FliP5Q4R1FlhB1
    reconstruction.'
- evidence_id: paper-21
  kind: primary_source
  reference: DOI:10.1371/journal.pgen.1001143
  locator: Abstract and full-text introductory context
  accessed_at: '2026-10-10T22:40:53Z'
  snapshot_sha256: d72bc529b0e03696b62ddfd195cc88e8a133f99f36a7197e50b3deb14e232a83
  support: supports
  summary: 'Abstract and full-text introductory context: FliO deletion/bypass and
    coexpression experiments support an assembly/stability role outside the conserved
    mature core.'
- evidence_id: paper-22
  kind: primary_source
  reference: DOI:10.1371/journal.ppat.1005495
  locator: Full text Results sodium blockers, ATPase deletions and Discussion
  accessed_at: '2026-10-10T22:40:55Z'
  snapshot_sha256: 5b4edd242fc3d5653a65316bdcacb05220f6d3aa27dda347f8ba35a5c625426b
  support: supports
  summary: 'Full text Results sodium blockers, ATPase deletions and Discussion: sodium-dependent
    export in ATPase-compromised Salmonella contrasts with PMF-coupled wild type.'
- evidence_id: paper-23
  kind: primary_source
  reference: DOI:10.3389/fmicb.2015.00023
  locator: Review abstract and established comparative context
  accessed_at: '2026-10-10T22:40:56Z'
  snapshot_sha256: 5e2b4c125d1d01c22b2d7eb326b7e73bb6b17e9d1c0b660c785ea11667745677
  support: supports
  summary: 'Review abstract and established comparative context: archaella are type-IV-pilus-related,
    not bacterial flagellar structures.'
- evidence_id: go-0009425
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009425
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:01Z'
  snapshot_sha256: 9fce7e21efecbd6edee814457befdcbf6d3ae546aaefe4cc9aa56657b40e75c3
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: go-0009431
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009431
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:01Z'
  snapshot_sha256: 8fa717593fed9c5b9a18b86d902b375a8f28422667e63070ee4988be66704544
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: go-0120102
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120102
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:04Z'
  snapshot_sha256: 055a3f19d9543943bae1968a31e6e38237a324177cfc4838170addef9e155be7
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr000563
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000563/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:06Z'
  snapshot_sha256: da032e6daa2729b74eab74384f35cb289030007d77375d61d0991c9d3f468bf1
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr005837
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005837/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:06Z'
  snapshot_sha256: 4aeec8e78fa51c118c7c252827abac929456c4f49696138dbf23754cc6d7ab9f
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr006136
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006136/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:07Z'
  snapshot_sha256: 17aa937c9237830f6fdbfd313d8d0621128189f71d80499a3a959f068ddc25ca
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr006301
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006301/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:07Z'
  snapshot_sha256: dac127fb9423cd80fcb00ffcbc6a9a52aad30aa017cf4277cdc4ff7bb72f9b89
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr006303
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006303/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:09Z'
  snapshot_sha256: 0eff657e3ceedd37a2a443a9c9d2ce8b8ba805208086256ed9e4daa6ede92835
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr006305
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006305/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:09Z'
  snapshot_sha256: 7116fae07149a094a565ba362726d4ef2be82f599e451a54b8ba6fa7424d9459
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: interpro-ipr012823
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012823/
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:10Z'
  snapshot_sha256: 9ed57d962a1db87bea7ed65bca0eff2dbef1c0e0cd8f9bcdde4c9ce7ae95ce98
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p0a1k1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A1K1.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:11Z'
  snapshot_sha256: dccaeed0ce183620be6057154dac4fce1ed00f3344d843146f4959bb79be63f5
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p0a1l5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A1L5.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:11Z'
  snapshot_sha256: 213efa332ee418f7e57cde18af9bd30c03b40eec8058df89129ca4f2760eeb25
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p15934
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P15934.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:12Z'
  snapshot_sha256: 8cb6c4b9232608015ae7dffabf69d04620c734bea1d8213cb523d658252a23f1
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p26465
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P26465.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:12Z'
  snapshot_sha256: f90c3356bc134ea01f7deb28628cdac4d92ab835cfed5ef610676a12e8283c9b
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p40727
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40727.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:13Z'
  snapshot_sha256: 83267535894609c8071bf26fd3ac30e3aace016fdbc663160e3ab52cf6f1c948
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p40729
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40729.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:14Z'
  snapshot_sha256: 1ad67856f963a01dc7a862d448e7c57ece9db0b4683ea5cf6045551058ce8f6d
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p54700
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P54700.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:15Z'
  snapshot_sha256: 92716e36e5df581ba3fbbce12fe8b0e098050165c2d445ee5de84530e1645944
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: uniprotkb-p54702
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P54702.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:15Z'
  snapshot_sha256: f5d8f69e84b8946a569a6f9661857dabe309aeb56662affcfe4172ca2abaf808
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
- evidence_id: ncbitaxon-90371
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/90371.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:18Z'
  snapshot_sha256: 46c958747209e78a835996643e63aafb6d1e94a8a632f0094dba733eb1bd3dee
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: ncbitaxon-99287
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/99287.json
  locator: Identity, definition, status, family scope, gene and taxon metadata
  accessed_at: '2026-10-10T22:41:18Z'
  snapshot_sha256: 107ebfece75c5a7147abe7547dec9166f87ff267e6cbc3f67bea9ab9df694a59
  support: supports
  summary: Live authority identity checked; a protein accession is not experimental
    membership evidence.
- evidence_id: kuhlen2018
  kind: primary_source
  reference: DOI:10.1038/s41594-018-0086-9
  locator: Results, stoichiometry and helical architecture
  accessed_at: '2026-10-10T22:42:25Z'
  snapshot_sha256: 84119543ebc833359db85a898054a9d7373eb9461856beaf55e6dfeb3d5a8bae
  support: supports
  summary: Salmonella Typhimurium FliP5Q4R1 is directly reconstructed; FliR is integrated
    and FliQ is peripheral, not an independently measured assembly sequence.
- evidence_id: kuhlen2020
  kind: primary_source
  reference: DOI:10.1038/s41467-020-15071-9
  locator: Results, architecture, topology and Methods
  accessed_at: '2026-10-10T22:42:27Z'
  snapshot_sha256: 79e116a60e00199c24c484a4bd7dcd945673fc7edb0211c15a9de27c7c11180e
  support: supports
  summary: Vibrio mimicus FliP5Q4R1-FlhB1 shows FlhB around the base; this is not
    a Salmonella 2017 reconstruction.
- evidence_id: ipr005714
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005714/
  locator: Family scope
  accessed_at: '2026-10-10T22:42:34Z'
  snapshot_sha256: 2ca94be2375f8785c55b6e9cb0b2e8a4d081481056375a1d0aca5a3cdda6e72f
  support: supports
  summary: Mixed flagellar/injectisome ATPase family and narrower FliI clade support
    retaining FliI label-only scope.
- evidence_id: ipr020005
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020005/
  locator: Family scope
  accessed_at: '2026-10-10T22:42:35Z'
  snapshot_sha256: 4bde8c0f0532639f234f9e2d7e30b1f90a35401436779ee783afa4e6dd9a14cd
  support: supports
  summary: Mixed flagellar/injectisome ATPase family and narrower FliI clade support
    retaining FliI label-only scope.
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
  reference: reviews/structured/20261010T224657Z-flagellar-secretion-apparatus-audit/review.yaml
  accessed_at: '2026-10-10T22:56:29Z'
  snapshot_sha256: 5a693c8205865469efaeca03aa8838d4f104525f7134c7d5b6895caaa623dcdb
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
  topic: Modern export-core architecture is falsely attributed to Fukumura 2017
  outcome: supported
  target_ids:
  - GO:0120102
  evidence_ids:
  - record
  - paper-20
  - kuhlen2018
  - kuhlen2020
  - predecessor
  - preservation
  summary: Current counts, geometry and exemplar cite Salmonella PQR in Kuhlen 2018
    and Vibrio PQR-FlhB in Kuhlen 2020. FlhB wraps the base; FliR is integrated and
    FliQ peripheral. The historical 2017 evidence and FliO decision remain, without
    false modern-count or assembly-order attribution.
- assessment_id: resolved-f2
  area: evidence
  topic: ATPase model is described as a resolved complete complex
  outcome: supported
  target_ids:
  - GO:0120102
  evidence_ids:
  - record
  - paper-13
  - paper-12
  - predecessor
  - preservation
  summary: All three ATPase component count fields and relevant notes distinguish
    the modeled FliH12-FliI6-FliJ1 assembly from the solved FliH C-terminal dimer-FliI
    heterotrimer; the ring edge explicitly identifies the model.
- assessment_id: resolved-f3
  area: evidence
  topic: Sodium coupling is conflated with the intact ATPase-assisted state
  outcome: supported
  target_ids:
  - GO:0120102
  evidence_ids:
  - record
  - paper-22
  - predecessor
  - preservation
  summary: 'The FlhA role, energy function, graph summary, energy node and edge preserve
    the experimental Salmonella contrast: intact ATPase-assisted PMF export versus
    sodium-capable ATPase-compromised export.'
findings:
- finding_id: F1
  issue_key: flagellar-export-core-stoichiometry-provenance
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Modern export-core architecture is falsely attributed to Fukumura 2017
  description: Current counts, geometry and exemplar cite Salmonella PQR in Kuhlen
    2018 and Vibrio PQR-FlhB in Kuhlen 2020. FlhB wraps the base; FliR is integrated
    and FliQ peripheral. The historical 2017 evidence and FliO decision remain, without
    false modern-count or assembly-order attribution.
  target_ids:
  - GO:0120102
  field_paths:
  - definition
  - components[1:5]
  - canonical_examples[0]
  - functions[1]
  - causal_graphs[0].description
  - causal_graphs[0].edges[0:3]
  - causal_graphs[0].edges[10]
  - discussions[0].rationale
  evidence_ids:
  - record
  - paper-20
  - kuhlen2018
  - kuhlen2020
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Unsupported or conflicting scientific scope.
  disposition_reason: Current counts, geometry and exemplar cite Salmonella PQR in
    Kuhlen 2018 and Vibrio PQR-FlhB in Kuhlen 2020. FlhB wraps the base; FliR is integrated
    and FliQ peripheral. The historical 2017 evidence and FliO decision remain, without
    false modern-count or assembly-order attribution. Exact affected fields were checked
    against the cited primary or authority evidence and passing post-curation gates.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T224657Z-flagellar-secretion-apparatus-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2157
- finding_id: F2
  issue_key: flagellar-export-atpase-model-provenance
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: ATPase model is described as a resolved complete complex
  description: All three ATPase component count fields and relevant notes distinguish
    the modeled FliH12-FliI6-FliJ1 assembly from the solved FliH C-terminal dimer-FliI
    heterotrimer; the ring edge explicitly identifies the model.
  target_ids:
  - GO:0120102
  field_paths:
  - components[5:8].stoichiometry
  - components[5:8].evidence
  - causal_graphs[0].edges[4:6]
  evidence_ids:
  - record
  - paper-13
  - paper-12
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: minor
  normalization_reason: Bounded provenance, claim-qualification or grounding defect;
    record identity is sound.
  disposition_reason: All three ATPase component count fields and relevant notes distinguish
    the modeled FliH12-FliI6-FliJ1 assembly from the solved FliH C-terminal dimer-FliI
    heterotrimer; the ring edge explicitly identifies the model. Exact affected fields
    were checked against the cited primary or authority evidence and passing post-curation
    gates.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T224657Z-flagellar-secretion-apparatus-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2158
- finding_id: F3
  issue_key: flagellar-export-dual-fuel-atpase-context
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Sodium coupling is conflated with the intact ATPase-assisted state
  description: 'The FlhA role, energy function, graph summary, energy node and edge
    preserve the experimental Salmonella contrast: intact ATPase-assisted PMF export
    versus sodium-capable ATPase-compromised export.'
  target_ids:
  - GO:0120102
  field_paths:
  - components[0].role
  - components[6].evidence[1]
  - functions[2]
  - causal_graphs[0].description
  - causal_graphs[0].nodes
  - causal_graphs[0].edges[8]
  evidence_ids:
  - record
  - paper-22
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/bacterial_type_flagellum_secretion_apparatus.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md#evidence
  native_severity: major
  normalization_reason: Unsupported or conflicting scientific scope.
  disposition_reason: 'The FlhA role, energy function, graph summary, energy node
    and edge preserve the experimental Salmonella contrast: intact ATPase-assisted
    PMF export versus sodium-capable ATPase-compromised export. Exact affected fields
    were checked against the cited primary or authority evidence and passing post-curation
    gates.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261010T224657Z-flagellar-secretion-apparatus-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2159
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
  review_id: 20261010T224657Z-flagellar-secretion-apparatus-audit
  relationship: Resolves all exact predecessor findings without rewriting the original
    observation.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2157
- https://github.com/CultureBotAI/CellStructureMech/issues/2158
- https://github.com/CultureBotAI/CellStructureMech/issues/2159
```
