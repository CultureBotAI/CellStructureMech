# Periplasmic flagellum: finding dispositions

- Review: 20261011T052714Z-periplasmic_flagellum-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T05:12:33Z
- Finished UTC: 2026-10-11T05:27:14Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Both exact predecessor findings are resolved. Remaining source-access limits and scientific uncertainty are retained; native status is not promoted.

## Scope And Provenance

The two exact predecessor findings, changed fields and append-only provenance; not a new whole-record review.

Selection: F1 and F2 in 20261011T045750Z-periplasmic_flagellum-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base bf5cbb1bfca94164a675166bfde8e0ab3e355806.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0055040 | data/structures/appendage/periplasmic_flagellum.yaml | maintained | periplasmic flagellum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0055040 | Actual post-curation command passed. Scientific support assessed separately; resolver skips and empty quotation checks are not biological proof. |
| strict | passed | True | GO:0055040 | Actual post-curation command passed. Scientific support assessed separately; resolver skips and empty quotation checks are not biological proof. |
| snippets | passed | True | GO:0055040 | Actual post-curation command passed. Scientific support assessed separately; resolver skips and empty quotation checks are not biological proof. |
| history | passed | True | GO:0055040 | Actual post-curation command passed. Scientific support assessed separately; resolver skips and empty quotation checks are not biological proof. |
| labels | passed | True | GO:0055040 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0055040 | Actual post-curation command passed. Scientific support assessed separately; resolver skips and empty quotation checks are not biological proof. |
| curies | passed | True | GO:0055040 | resolver control: every resolver accepts a known id and rejects a fabricated one<br>resolving 1 DOI identifier(s)...<br><br>identifier liveness summary:<br>  OK             4011<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| regressions | passed | True | GO:0055040 | ............................                                             [100%]<br>28 passed in 35.42s |
| reviews | passed | True | GO:0055040 | Actual post-curation command passed. Scientific support assessed separately; resolver skips and empty quotation checks are not biological proof. |
| diff | passed | True | GO:0055040 | Actual post-curation command passed. Scientific support assessed separately; resolver skips and empty quotation checks are not biological proof. |
| attribution-regressions | passed | True | GO:0055040 | Actual post-curation command passed. Scientific support assessed separately; resolver skips and empty quotation checks are not biological proof. |
| attribution-embeddings | passed | True | GO:0055040 | Actual post-curation command passed. Scientific support assessed separately; resolver skips and empty quotation checks are not biological proof. |
| Authoritative local full QC | passed | True | GO:0055040 | Full native QC passed on the unchanged corrected input bytes, including corpus tests, all-record schema, history and generated site/embedding drift checks. This is local QC, not a claim that final PR or merge-group CI has already run. |

## Scientific And Domain Assessments

### Scope FlaA architecture to the demonstrated spirochete lineage

evidence: supported. Targets: GO:0055040.

FlaA remains a constituent with UNKNOWN essentiality and the original P70856 example. Component and graph prose distinguish Brachyspira sheath architecture, unresolved Borrelia localization and Leptospira sheath retention after FlaA deletion. The generic filament is no longer labeled sheathed, and the FlaA edge now states association instead of universal sheath formation.

### Separate static skeletal shape from rotation-driven deformation

evidence: supported. Targets: GO:0055040.

The active motor/rotation pathway introduced for #203 is preserved. The deformation state is now explicitly dynamic and swimming-related, supported by the Nakamura section 4.1 synthesis. The Motaleb CCCP result is retained as boundary evidence for rotation-independent resting shape, not direct proof of the active edge or evidence that rotation is unnecessary for swimming.

## Findings

### F1: Scope FlaA architecture to the demonstrated spirochete lineage

major / resolved / confirmed; issue key: periplasmic-flagellum-flaa-sheath-scope.

FlaA remains a constituent with UNKNOWN essentiality and the original P70856 example. Component and graph prose distinguish Brachyspira sheath architecture, unresolved Borrelia localization and Leptospira sheath retention after FlaA deletion. The generic filament is no longer labeled sheathed, and the FlaA edge now states association instead of universal sheath formation.

Disposition: FlaA remains a constituent with UNKNOWN essentiality and the original P70856 example. Component and graph prose distinguish Brachyspira sheath architecture, unresolved Borrelia localization and Leptospira sheath retention after FlaA deletion. The generic filament is no longer labeled sheathed, and the FlaA edge now states association instead of universal sheath formation. Verified against the inspected primary evidence or explicitly labeled synthesis, focused regressions and full local QC.

### F2: Separate static skeletal shape from rotation-driven deformation

major / resolved / confirmed; issue key: periplasmic-flagellum-static-shape-rotation-evidence.

The active motor/rotation pathway introduced for #203 is preserved. The deformation state is now explicitly dynamic and swimming-related, supported by the Nakamura section 4.1 synthesis. The Motaleb CCCP result is retained as boundary evidence for rotation-independent resting shape, not direct proof of the active edge or evidence that rotation is unnecessary for swimming.

Disposition: The active motor/rotation pathway introduced for #203 is preserved. The deformation state is now explicitly dynamic and swimming-related, supported by the Nakamura section 4.1 synthesis. The Motaleb CCCP result is retained as boundary evidence for rotation-independent resting shape, not direct proof of the active edge or evidence that rotation is unnecessary for swimming. Verified against the inspected primary evidence or explicitly labeled synthesis, focused regressions and full local QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/periplasmic_flagellum.yaml; Full native YAML and exact append-only record histories | context_only | Corrected native bytes read and compared against the original findings and inspected sources; status and earlier history retained. |
| prior | reviews/structured/ and reports/yaml_record_review/; Exact slugs and GO identifiers | context_only | No earlier exact-target saved review bundle found in these two roots. Closed issue #203 concerns introducing an active rotation node, not the static-versus-dynamic evidence mismatch; #293 concerns the PFR synonym citation, not family mapping. Earlier histories remain authoritative historical observations. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009289,GO:0097740,GO:0097729,GO:0005930,GO:0055040,GO:0009288,GO:0120100,GO:0071973; Exact target term and asserted parent/parthood/function terms only | supports | Active GO identifiers and current relations match the native identity and hierarchy. Ontology wording is not experimental validation of uniform molecular architecture. |
| nakamura | DOI:10.3390/biom10040550; Review sections 2, 3.1-3.3 and 4.1-4.3; secondary synthesis | supports | The cited review distinguishes FlaA architecture by lineage and discusses swimming from flagellar rotation. It is not a primary experiment: Borrelia FlaA placement near the base is tentative, and Leptospira sheath persists after FlaA deletion. |
| ge | DOI:10.1128/JB.180.9.2418-2425.1998; Abstract, FlaA copurification Results and final Discussion paragraph | supports | FlaA copurifies with Borrelia flagella using gentle extraction. Its precise location and a sheath role were not determined; localization near the hook was a hypothesis. |
| motaleb | DOI:10.1073/pnas.200221797; Abstract, flaB mutant Results, CCCP immobilization Methods and Results, Discussion | supports | Loss of flaB eliminates filaments and changes morphology; CCCP-immobilized cells retain flat-wave shape. This distinguishes the resting skeletal effect from dynamic wave propagation. |
| qin | DOI:10.1371/journal.pbio.3000050; Abstract, Introduction, motor/ATPase structural Results and Fig. 1-3 captions | supports | CryoET places the filament and motor assembly in Borrelia and resolves collar/ATPase architecture. Static reconstructions support proposed rotary arrangement, not direct movies of filament rotation. |
| san-martin | DOI:10.1016/j.tim.2022.09.010; Bibliographic identity and primary abstract only | context_only | Supports endoflagellum/periplasmic placement. Publisher retrieval returned an HTML shell without article text; it does not establish the record generic FlaA sheath edge. |
| uniprot | https://rest.uniprot.org/uniprotkb/P70856.json; Reviewed accession, gene, source protein label and taxonomy | supports | P70856 matches flaA and B31; the historical source protein name is retained as provenance, not proof of a continuous Borrelia sheath. |
| taxon-203691 | https://rest.uniprot.org/taxonomy/203691.json; Exact taxonomy identity | supports | Taxon identity, rank and source name match the native row at the stated scope. |
| taxon-2 | https://rest.uniprot.org/taxonomy/2.json; Exact taxonomy identity | supports | Taxon identity, rank and source name match the native row at the stated scope. |
| taxon-139 | https://rest.uniprot.org/taxonomy/139.json; Exact taxonomy identity | supports | Taxon identity, rank and source name match the native row at the stated scope. |
| taxon-224326 | https://rest.uniprot.org/taxonomy/224326.json; Exact taxonomy identity | supports | Taxon identity, rank and source name match the native row at the stated scope. |
| predecessor | reviews/structured/20261011T045750Z-periplasmic_flagellum-audit/review.yaml | context_only | Immutable original F1/F2 observations, saved and committed before mutation. |
| preservation | /private/tmp/csm-review-20261011T044732Z/preservation.json | supports | Only these two native records changed; 907 others and all prior history, canonical reviews and legacy reports are byte-preserved. |
| embeddings | /private/tmp/csm-review-20261011T044732Z/embedding-refresh.json | supports | Only these two semantic vectors changed under the pinned local model; 907 others retained exactly, with derived maps/neighbors and pages regenerated. |

## Limits And Additional Notes

- San Martin 2023 was accessible only at primary-abstract level; its publisher response was an unreadable HTML shell. No unseen text or supplements are claimed as inspected.
- Nakamura is secondary synthesis. Ge, Motaleb and Qin main-text sections were inspected; raw tomograms, supplemental movies and experimental data were not reanalysed.
- Same-agent review, not independent human sign-off or completion of the 909-record goal.
- No relevant iModulonDB coverage. No quoted snippets to verify; identifier/label validation cannot establish scientific accuracy.
- Original evidence access tiers and snapshot times are retained. Resolution covers the exact findings, not unreviewed papers, experimental uncertainties or the remaining corpus.
- Full QC here is local. Final PR and merge-group checks remain separate publication gates. The exact inspected final fix revision is retained by review-base/flagellar-evidence-final-20261011 for reproducibility after squash merge.
- A separate same-agent adversarial pass caught incorrect curator attribution in the two newly introduced inline events. The events now correctly identify Codex, matching the unchanged session histories. The provenance-only issue is tracked separately; it is not a new scientific finding.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T052714Z-periplasmic_flagellum-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Periplasmic flagellum: finding dispositions'
started_at: '2026-10-11T05:12:33Z'
finished_at: '2026-10-11T05:27:14Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source-backed reassessment and separate adversarial
    inspection of the corrected diff; not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Both exact predecessor findings are resolved. Remaining source-access limits
  and scientific uncertainty are retained; native status is not promoted.
source:
  git_revision: bf5cbb1bfca94164a675166bfde8e0ab3e355806
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
  - path: data/structures/appendage/bacterial_type_flagellum.yaml
    sha256: 4e3e6bf50835a3134d50e5a20a87cdfa86e1e37c21085757402df7dd628095e6
    role: context
  - path: data/structures/appendage/cilium.yaml
    sha256: 2536d421f9c482abf35c2d2bf026eb6158ddfec5c2df1f319ca80698cbb56bb8
    role: context
  - path: data/structures/appendage/p_pilus.yaml
    sha256: c9e8371a5cc6cda0a28d5264a6a2c2368a703670b3c285fc12f1aa58b6adafa9
    role: context
  - path: data/structures/appendage/paraflagellar_rod.yaml
    sha256: 41db80e5c5c665d307b779916056e1b77f7a6c36b3dfec7e0ec8a07f453b41b3
    role: context
  - path: data/structures/appendage/periplasmic_flagellum.yaml
    sha256: 3e23745177fb5608a01398ffa97cac02daebfd40fa9c561a8c2d7cc394558c57
    role: target
  - path: data/structures/appendage/pilus.yaml
    sha256: b82205e792d181aa2e2cb76eb56a2ecafdb3021302c7b86a5819c649528bc06b
    role: context
  - path: data/structures/appendage/type_i_pilus.yaml
    sha256: 35b161df2bab54d5b56efde936dc2ee7e5de57789ae583a26a8265b04dc17f00
    role: context
  - path: data/structures/appendage/type_iv_pilus.yaml
    sha256: 744f19aeb3b62c9f4d470fcbf47038056069904d998eb7c5e2b83f6821037d4e
    role: context
  - path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
    sha256: a3c88e9e9a6b27327238a732a4d6cdc4740ba50f26c581d251bfb5ad12f7dc0c
    role: context
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
  - path: history/records/periplasmic_flagellum/2026-09-06T114213Z-claude-0ed7e0.yaml
    sha256: 62bad23a92f6ae71568a6e407e8340e790177c35a104436057b0338bb7bfaa17
    role: context
  - path: history/records/periplasmic_flagellum/2026-09-06T123801Z-claude-cb3b36.yaml
    sha256: 9a77a06c7cae366c95bd2293fc096b09c16907fd69e13d369eb5a48baeee21cf
    role: context
  - path: history/records/periplasmic_flagellum/2026-10-11T045847Z-codex-c3f085.yaml
    sha256: a4d29f18aad4758f065b27b8edc037aa878e858029eea25d1b372e79b3fbc8ac
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/evidence_readability.periplasmic_flagellum.tsv
    sha256: 970a896af9d89fbfc08b9e266b82e60501429712f3a254a0863f42d3dae1ad52
    role: context
  - path: reviews/structured/20261011T045750Z-periplasmic_flagellum-audit/review.yaml
    sha256: d44222a9ac4d4273c620ea30ee2066d917fb5a37f4177960021add2179989fe9
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_flagellar_evidence_review.py
    sha256: 8eb5a720d1c312b94c35d692a3cb3956f42c7162339b355939032fa15a51a45e
    role: context
targets:
- target_id: GO:0055040
  path: data/structures/appendage/periplasmic_flagellum.yaml
  label: periplasmic flagellum
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/periplasmic_flagellum.yaml
    role: maintained scientific record
scope:
  description: The two exact predecessor findings, changed fields and append-only
    provenance; not a new whole-record review.
  selection: F1 and F2 in 20261011T045750Z-periplasmic_flagellum-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0055040
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/periplasmic_flagellum.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    resolver skips and empty quotation checks are not biological proof.
  scope_note: 2026-10-11T04:59:45Z to 2026-10-11T04:59:49Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/periplasmic_flagellum.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    resolver skips and empty quotation checks are not biological proof.
  scope_note: 2026-10-11T04:59:49Z to 2026-10-11T04:59:54Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/periplasmic_flagellum.yaml
    --report /private/tmp/csm-review-20261011T044732Z/periplasmic_flagellum-post-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    resolver skips and empty quotation checks are not biological proof.
  scope_note: 2026-10-11T04:59:54Z to 2026-10-11T05:00:14Z; log SHA-256 3004cdb37fefd667237244d73eb93fbc48d2bc8e1d676c754005978f1447e6ea
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    resolver skips and empty quotation checks are not biological proof.
  scope_note: 2026-10-11T05:00:14Z to 2026-10-11T05:00:28Z; log SHA-256 7d8379458f5adf9726b5df01dc5d6092c1500b8c1627b771ec131d9c4c3c3aaf
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T05:00:28Z to 2026-10-11T05:01:47Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    resolver skips and empty quotation checks are not biological proof.
  scope_note: 2026-10-11T05:01:47Z to 2026-10-11T05:02:07Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\nresolving 1 DOI identifier(s)...\n\nidentifier liveness summary:\n  OK\
    \             4011\n  SKIPPED         251\n\nEvery identifier resolves at its\
    \ issuing authority."
  scope_note: 2026-10-11T05:02:07Z to 2026-10-11T05:02:58Z; log SHA-256 d9e0433a1be6e833659961c54fbb18396d52994a8cae86aa0c5a2c78cf8d874e
- check_id: regressions
  name: regressions
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python -m pytest -q tests/test_flagellar_evidence_review.py tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '............................                                             [100%]

    28 passed in 35.42s'
  scope_note: 2026-10-11T05:02:58Z to 2026-10-11T05:03:34Z; log SHA-256 726f3241bfad70f16dc7989207da80ddd8eb4bce4857b8790b0a27a30a447be9
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python scripts/record_review.py check --base fe0a41e4cd9c1bfa27f72ef427f045022df862c0
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    resolver skips and empty quotation checks are not biological proof.
  scope_note: 2026-10-11T05:03:34Z to 2026-10-11T05:04:43Z; log SHA-256 0536b40c7ae5df08e85d61b7dfdf17da8e026cbfd7ed8ed182d9bc9193b54227
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    resolver skips and empty quotation checks are not biological proof.
  scope_note: 2026-10-11T05:04:43Z to 2026-10-11T05:04:43Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: attribution-regressions
  name: attribution-regressions
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python -m pytest -q tests/test_flagellar_evidence_review.py tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    resolver skips and empty quotation checks are not biological proof.
  scope_note: 2026-10-11T05:11:48Z to 2026-10-11T05:12:18Z; log SHA-256 6270b00647d3a7e4b9ebcaea94ba639c0ffb78649d28fd50b91fdcf4ffc9e818
- check_id: attribution-embeddings
  name: attribution-embeddings
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python scripts/build_text_embedding_map.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Scientific support assessed separately;
    resolver skips and empty quotation checks are not biological proof.
  scope_note: 2026-10-11T05:12:18Z to 2026-10-11T05:12:36Z; log SHA-256 faab91135b11d9032aedb96eee09f6eac44ff7c58be84c007d155ecb4d3220a4
- check_id: qc
  name: Authoritative local full QC
  status: passed
  required: true
  target_ids:
  - GO:0055040
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: Full native QC passed on the unchanged corrected input bytes, including
    corpus tests, all-record schema, history and generated site/embedding drift checks.
    This is local QC, not a claim that final PR or merge-group CI has already run.
  scope_note: 2026-10-11T05:12:44Z to 2026-10-11T05:27:03Z; log SHA-256 ea4a609fe07a10e839125debf9c7524c309e041b323aeb822c5e082024018153;
    RECORD_REVIEW_BASE=fe0a41e4cd9c1bfa27f72ef427f045022df862c0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/periplasmic_flagellum.yaml
  locator: Full native YAML and exact append-only record histories
  accessed_at: '2026-10-11T05:27:14Z'
  snapshot_sha256: 3e23745177fb5608a01398ffa97cac02daebfd40fa9c561a8c2d7cc394558c57
  support: context_only
  summary: Corrected native bytes read and compared against the original findings
    and inspected sources; status and earlier history retained.
- evidence_id: prior
  kind: search
  reference: reviews/structured/ and reports/yaml_record_review/
  locator: Exact slugs and GO identifiers
  accessed_at: '2026-10-11T04:57:50Z'
  support: context_only
  search_scope: rg --no-ignore --hidden across both review roots included ignored
    files. GitHub all-state bounded query paraflagellar OR periplasmic returned nine
    items, below the 100-result limit.
  summary: 'No earlier exact-target saved review bundle found in these two roots.
    Closed issue #203 concerns introducing an active rotation node, not the static-versus-dynamic
    evidence mismatch; #293 concerns the PFR synonym citation, not family mapping.
    Earlier histories remain authoritative historical observations.'
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009289,GO:0097740,GO:0097729,GO:0005930,GO:0055040,GO:0009288,GO:0120100,GO:0071973
  locator: Exact target term and asserted parent/parthood/function terms only
  accessed_at: '2026-10-11T04:49:10Z'
  snapshot_sha256: 58999ee2fac67a7a971a451530f3a1fa4281636cf7762a139ead03851aa01c92
  support: supports
  summary: Active GO identifiers and current relations match the native identity and
    hierarchy. Ontology wording is not experimental validation of uniform molecular
    architecture.
- evidence_id: nakamura
  kind: primary_source
  reference: DOI:10.3390/biom10040550
  locator: Review sections 2, 3.1-3.3 and 4.1-4.3; secondary synthesis
  accessed_at: '2026-10-11T04:49:09Z'
  snapshot_sha256: 8dbfe5794bbdda7bc2815bec1b378cffc6d423b09774d9dda579084b8e2e1a13
  support: supports
  summary: 'The cited review distinguishes FlaA architecture by lineage and discusses
    swimming from flagellar rotation. It is not a primary experiment: Borrelia FlaA
    placement near the base is tentative, and Leptospira sheath persists after FlaA
    deletion.'
- evidence_id: ge
  kind: primary_source
  reference: DOI:10.1128/JB.180.9.2418-2425.1998
  locator: Abstract, FlaA copurification Results and final Discussion paragraph
  accessed_at: '2026-10-11T04:49:46Z'
  snapshot_sha256: ea87f6e484e41b9f7bc4d789ff4e308862b3f312b34482070d4ac0ee4accbf69
  support: supports
  summary: FlaA copurifies with Borrelia flagella using gentle extraction. Its precise
    location and a sheath role were not determined; localization near the hook was
    a hypothesis.
- evidence_id: motaleb
  kind: primary_source
  reference: DOI:10.1073/pnas.200221797
  locator: Abstract, flaB mutant Results, CCCP immobilization Methods and Results,
    Discussion
  accessed_at: '2026-10-11T04:49:45Z'
  snapshot_sha256: 875f84fd1957f40c55df1386e8ea6022d95c025e8060a11369438b8a8b44e76c
  support: supports
  summary: Loss of flaB eliminates filaments and changes morphology; CCCP-immobilized
    cells retain flat-wave shape. This distinguishes the resting skeletal effect from
    dynamic wave propagation.
- evidence_id: qin
  kind: primary_source
  reference: DOI:10.1371/journal.pbio.3000050
  locator: Abstract, Introduction, motor/ATPase structural Results and Fig. 1-3 captions
  accessed_at: '2026-10-11T04:49:05Z'
  snapshot_sha256: 5ece51b43bb79ce73973dd4ec25e9a57ab33436c13f62b0e167f38f780e10739
  support: supports
  summary: CryoET places the filament and motor assembly in Borrelia and resolves
    collar/ATPase architecture. Static reconstructions support proposed rotary arrangement,
    not direct movies of filament rotation.
- evidence_id: san-martin
  kind: primary_source
  reference: DOI:10.1016/j.tim.2022.09.010
  locator: Bibliographic identity and primary abstract only
  accessed_at: '2026-10-11T04:48:44Z'
  snapshot_sha256: 671692ad7126c403cbbf268cbe38b59d54476b37ab980ae21fa14400c0081f49
  support: context_only
  summary: Supports endoflagellum/periplasmic placement. Publisher retrieval returned
    an HTML shell without article text; it does not establish the record generic FlaA
    sheath edge.
- evidence_id: uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P70856.json
  locator: Reviewed accession, gene, source protein label and taxonomy
  accessed_at: '2026-10-11T04:49:04Z'
  snapshot_sha256: da4ffcfbdb420013638a05f24b2c8b8ec1d0cc4286b0f4da18af45e6e2c32694
  support: supports
  summary: P70856 matches flaA and B31; the historical source protein name is retained
    as provenance, not proof of a continuous Borrelia sheath.
- evidence_id: taxon-203691
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/203691.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T04:49:08Z'
  snapshot_sha256: 57da54f373467c59ca5cf1a136267cf9b8b48f38e6c5bb7b3f91bc264b54eba8
  support: supports
  summary: Taxon identity, rank and source name match the native row at the stated
    scope.
- evidence_id: taxon-2
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T04:49:09Z'
  snapshot_sha256: 8074c9bcd59cd4da1da4bc9ec98c040bbecd52ef5c91c4c4bb9bed0f3a7cb5a9
  support: supports
  summary: Taxon identity, rank and source name match the native row at the stated
    scope.
- evidence_id: taxon-139
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/139.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T04:49:10Z'
  snapshot_sha256: 821432967fae0153b376db0094d7e72e19814b2f592007e4c4d269d47fa799dc
  support: supports
  summary: Taxon identity, rank and source name match the native row at the stated
    scope.
- evidence_id: taxon-224326
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/224326.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T04:49:08Z'
  snapshot_sha256: 2c1f7467e9b5f58df305e9ad8ba853fa379e41de29a7b53a851a89cc9dcad70b
  support: supports
  summary: Taxon identity, rank and source name match the native row at the stated
    scope.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T045750Z-periplasmic_flagellum-audit/review.yaml
  accessed_at: '2026-10-11T05:27:14Z'
  snapshot_sha256: d44222a9ac4d4273c620ea30ee2066d917fb5a37f4177960021add2179989fe9
  support: context_only
  summary: Immutable original F1/F2 observations, saved and committed before mutation.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T044732Z/preservation.json
  accessed_at: '2026-10-11T04:59:08Z'
  snapshot_sha256: 01dde8c3852699300f5d016366e6199cae8021de99de7bfd415463bd9e215173
  support: supports
  summary: Only these two native records changed; 907 others and all prior history,
    canonical reviews and legacy reports are byte-preserved.
- evidence_id: embeddings
  kind: validation
  reference: /private/tmp/csm-review-20261011T044732Z/embedding-refresh.json
  accessed_at: '2026-10-11T05:27:14Z'
  snapshot_sha256: a77fd0c82ce86decc4ed76ff19a3b89581ecf5e24bdd9e7d731d610333793f33
  support: supports
  summary: Only these two semantic vectors changed under the pinned local model; 907
    others retained exactly, with derived maps/neighbors and pages regenerated.
assessments:
- assessment_id: resolved-f1
  area: evidence
  topic: Scope FlaA architecture to the demonstrated spirochete lineage
  outcome: supported
  target_ids:
  - GO:0055040
  evidence_ids:
  - record
  - ge
  - nakamura
  - predecessor
  - preservation
  summary: FlaA remains a constituent with UNKNOWN essentiality and the original P70856
    example. Component and graph prose distinguish Brachyspira sheath architecture,
    unresolved Borrelia localization and Leptospira sheath retention after FlaA deletion.
    The generic filament is no longer labeled sheathed, and the FlaA edge now states
    association instead of universal sheath formation.
- assessment_id: resolved-f2
  area: evidence
  topic: Separate static skeletal shape from rotation-driven deformation
  outcome: supported
  target_ids:
  - GO:0055040
  evidence_ids:
  - record
  - motaleb
  - nakamura
  - predecessor
  - preservation
  summary: 'The active motor/rotation pathway introduced for #203 is preserved. The
    deformation state is now explicitly dynamic and swimming-related, supported by
    the Nakamura section 4.1 synthesis. The Motaleb CCCP result is retained as boundary
    evidence for rotation-independent resting shape, not direct proof of the active
    edge or evidence that rotation is unnecessary for swimming.'
findings:
- finding_id: F1
  issue_key: periplasmic-flagellum-flaa-sheath-scope
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Scope FlaA architecture to the demonstrated spirochete lineage
  description: FlaA remains a constituent with UNKNOWN essentiality and the original
    P70856 example. Component and graph prose distinguish Brachyspira sheath architecture,
    unresolved Borrelia localization and Leptospira sheath retention after FlaA deletion.
    The generic filament is no longer labeled sheathed, and the FlaA edge now states
    association instead of universal sheath formation.
  target_ids:
  - GO:0055040
  field_paths:
  - components[1]
  - causal_graphs[0].title
  - causal_graphs[0].description
  - causal_graphs[0].nodes
  - causal_graphs[0].edges
  evidence_ids:
  - record
  - ge
  - nakamura
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/periplasmic_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material component identity, scope or edge-evidence defect;
    the structure record itself retains valid identity.
  disposition_reason: FlaA remains a constituent with UNKNOWN essentiality and the
    original P70856 example. Component and graph prose distinguish Brachyspira sheath
    architecture, unresolved Borrelia localization and Leptospira sheath retention
    after FlaA deletion. The generic filament is no longer labeled sheathed, and the
    FlaA edge now states association instead of universal sheath formation. Verified
    against the inspected primary evidence or explicitly labeled synthesis, focused
    regressions and full local QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T045750Z-periplasmic_flagellum-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2173
- finding_id: F2
  issue_key: periplasmic-flagellum-static-shape-rotation-evidence
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Separate static skeletal shape from rotation-driven deformation
  description: 'The active motor/rotation pathway introduced for #203 is preserved.
    The deformation state is now explicitly dynamic and swimming-related, supported
    by the Nakamura section 4.1 synthesis. The Motaleb CCCP result is retained as
    boundary evidence for rotation-independent resting shape, not direct proof of
    the active edge or evidence that rotation is unnecessary for swimming.'
  target_ids:
  - GO:0055040
  field_paths:
  - causal_graphs[0].nodes
  - causal_graphs[0].edges[5]
  - functions[0].evidence
  evidence_ids:
  - record
  - motaleb
  - nakamura
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/periplasmic_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material component identity, scope or edge-evidence defect;
    the structure record itself retains valid identity.
  disposition_reason: 'The active motor/rotation pathway introduced for #203 is preserved.
    The deformation state is now explicitly dynamic and swimming-related, supported
    by the Nakamura section 4.1 synthesis. The Motaleb CCCP result is retained as
    boundary evidence for rotation-independent resting shape, not direct proof of
    the active edge or evidence that rotation is unnecessary for swimming. Verified
    against the inspected primary evidence or explicitly labeled synthesis, focused
    regressions and full local QC.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T045750Z-periplasmic_flagellum-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2174
actions: []
limitations:
- San Martin 2023 was accessible only at primary-abstract level; its publisher response
  was an unreadable HTML shell. No unseen text or supplements are claimed as inspected.
- Nakamura is secondary synthesis. Ge, Motaleb and Qin main-text sections were inspected;
  raw tomograms, supplemental movies and experimental data were not reanalysed.
- Same-agent review, not independent human sign-off or completion of the 909-record
  goal.
- No relevant iModulonDB coverage. No quoted snippets to verify; identifier/label
  validation cannot establish scientific accuracy.
- Original evidence access tiers and snapshot times are retained. Resolution covers
  the exact findings, not unreviewed papers, experimental uncertainties or the remaining
  corpus.
- Full QC here is local. Final PR and merge-group checks remain separate publication
  gates. The exact inspected final fix revision is retained by review-base/flagellar-evidence-final-20261011
  for reproducibility after squash merge.
- A separate same-agent adversarial pass caught incorrect curator attribution in the
  two newly introduced inline events. The events now correctly identify Codex, matching
  the unchanged session histories. The provenance-only issue is tracked separately;
  it is not a new scientific finding.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T045750Z-periplasmic_flagellum-audit
  relationship: Resolves exact F1 and F2 without rewriting the original observation.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2173
- https://github.com/CultureBotAI/CellStructureMech/issues/2174
- https://github.com/CultureBotAI/CellStructureMech/issues/2175
```
