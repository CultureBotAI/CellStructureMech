# Basal body A-C linker: image-provenance finding disposition

- Review: 20261011T105559Z-basal_body_a_c_linker-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T10:44:41Z
- Finished UTC: 2026-10-11T10:55:59Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact predecessor minor finding is resolved by a bounded source-provenance correction. Original review and native scientific status remain unchanged.

## Scope And Provenance

Reassessment of the exact saved image-processing provenance finding and preservation of surrounding claims, not a second whole-record scientific review.

Selection: 20261011T103510Z-basal_body_a_c_linker-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4a26f3b04e73502cfb362297a1d8e685fc599e22.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:basal_body_a_c_linker | data/structures/cytoskeleton/basal_body_a_c_linker.yaml | maintained | basal body A-C linker |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:basal_body_a_c_linker | Actual post-curation check passed; deterministic validation is not scientific certification. |
| strict | passed | True | cellstructuremech:basal_body_a_c_linker | Actual post-curation check passed; deterministic validation is not scientific certification. |
| snippets | passed | True | cellstructuremech:basal_body_a_c_linker | No verbatim snippets in this target; the caption and source-method paraphrase were directly assessed. |
| history | passed | True | cellstructuremech:basal_body_a_c_linker | Actual post-curation check passed; deterministic validation is not scientific certification. |
| labels | passed | True | cellstructuremech:basal_body_a_c_linker | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:basal_body_a_c_linker | Actual post-curation check passed; deterministic validation is not scientific certification. |
| curies | passed | True | cellstructuremech:basal_body_a_c_linker | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| focused | passed | True | cellstructuremech:basal_body_a_c_linker | ..........................                                               [100%]<br>26 passed in 45.17s |
| reviews | passed | True | cellstructuremech:basal_body_a_c_linker | Actual post-curation check passed; deterministic validation is not scientific certification. |
| diff | passed | True | cellstructuremech:basal_body_a_c_linker | Actual post-curation check passed; deterministic validation is not scientific certification. |
| release-qc | passed | True | cellstructuremech:basal_body_a_c_linker | Full local QC passed: 848 passed, 3 skipped in 550.09s (0:09:10). Required remote PR and native merge-group checks are separate publication gates. |

## Scientific And Domain Assessments

### Describe the A-C linker tomograms as denoised, not raw

provenance: supported. Targets: cellstructuremech:basal_body_a_c_linker.

The caption now describes denoised in-situ cryotomograms, and an appended source-method note names DeepDeWedge and the denoised Figure 1A volume. It explicitly attributes processing to the source authors. Original figure bytes, accession, license, attribution, panel roles and scale bars are unchanged. All biological fields and five discussions remain identical; only image wording and an appended curation event changed, with new repository EDIT history.

## Findings

### F1: Describe the A-C linker tomograms as denoised, not raw

minor / resolved / confirmed; issue key: ac-linker-denoised-tomogram-provenance.

The caption now describes denoised in-situ cryotomograms, and an appended source-method note names DeepDeWedge and the denoised Figure 1A volume. It explicitly attributes processing to the source authors. Original figure bytes, accession, license, attribution, panel roles and scale bars are unchanged. All biological fields and five discussions remain identical; only image wording and an appended curation event changed, with new repository EDIT history.

Disposition: The caption now describes denoised in-situ cryotomograms, and an appended source-method note names DeepDeWedge and the denoised Figure 1A volume. It explicitly attributes processing to the source authors. Original figure bytes, accession, license, attribution, panel roles and scale bars are unchanged. All biological fields and five discussions remain identical; only image wording and an appended curation event changed, with new repository EDIT history. Verified against inspected primary Methods, exact original image hash, red/green regressions and full QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/basal_body_a_c_linker.yaml | context_only | Corrected native record reread; structured diff confirms only the declared image fields and appended curation event changed. |
| rules | .claude/skills/curate-yaml-record/references/review-checklist.md | context_only | Image method and figure provenance must agree with the exact source context. |
| profile | docs/record-review-profile.md | context_only | Issue-only persistence: this concrete caption provenance defect qualifies; unknown families and optional gaps do not. |
| history | /private/tmp/csm-review-20261011T101801Z/basal_body_a_c_linker-discussion-history.json | context_only | All committed discussion and curation versions inspected; no rationale or discussion lifecycle loss observed. |
| append-history | history/records/basal_body_a_c_linker/2026-10-04T075437Z-codex-9b6ab8.yaml | context_only | Original CREATE history and actor attribution retained. |
| legacy | reports/yaml_record_review/20261004T081554Z-basal_body_a_c_linker.md | context_only | Earlier clean same-agent report is historical context; it did not flag the raw-versus-denoised caption. It is not rewritten or fabricated as canonical lineage. |
| predecessors | /private/tmp/csm-review-20261011T101801Z/exact-target-predecessors.json | context_only | Gitignore-independent scan of canonical reviews found no exact-target predecessor. |
| adapter | /private/tmp/csm-review-20261011T101801Z/adapter.log | context_only | Live 28-dataset iModulonDB inventory has no Tetrahymena dataset. Not applicable to these structural claims; no biological absence inferred. |
| paper | DOI:10.1126/sciadv.ady3689; Complete relevant Results, Discussion, isolation, reconstruction, modeling, U-ExM Methods, data availability and figure captions; Methods section Cryo-ET data collection, cryo-tomogram reconstruction, and segmentation | supports | The Methods specify DeepDeWedge contrast improvement of FIB-milled cell tomograms and segmentation of the denoised Figure 1A tomogram. The figure displays processed tomographic sections, not raw in-situ images. Main text supports the four families, proximal/transitional distinction and bounded modeled contacts. |
| manifest | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC12506977.1.json; Official PMC12506977.1 DOI, PMID, license and media MD5 manifest | supports | DOI 10.1126/sciadv.ady3689 / PMID 41061066 match. JATS and figure checksums verified; JATS explicitly licenses CC BY 4.0. |
| figure1 | https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f1.jpg; Entire figure inspected visually, including A-C and F-G panels and scale bars | supports | Figure 1 shows the same preserved source bytes, with segmented and unsegmented image views, isolation schematic and gel. The term raw in the native caption does not disclose the documented denoising. |
| figure3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f3.jpg; Visually inspected original figure; official manifest MD5 matched | supports | Checks the C-link and A-link contacts, CEP135 bridge, and proximal/transitional composition. Figure 6 C/D caption labels conflict with the actual panel titles; native discussion already preserves this. |
| figure5 | https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f5.jpg; Visually inspected original figure; official manifest MD5 matched | supports | Checks the C-link and A-link contacts, CEP135 bridge, and proximal/transitional composition. Figure 6 C/D caption labels conflict with the actual panel titles; native discussion already preserves this. |
| figure6 | https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f6.jpg; Visually inspected original figure; official manifest MD5 matched | supports | Checks the C-link and A-link contacts, CEP135 bridge, and proximal/transitional composition. Figure 6 C/D caption labels conflict with the actual panel titles; native discussion already preserves this. |
| figure4 | https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f4.jpg; Visually inspected original Figure 4, panels A-F; official MD5 matched | supports | POC1 continues into the B-C junction, whereas I7LY02 is adjacent junction material, not an A-C-linker constituent. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005575,GO:0005856,GO:0005879,GO:0032053,GO:0032991,GO:0036064,GO:0097545,GO:0097649,GO:0097650,GO:0110165,GO:0120280,GO:0140180,GO:0140535,GO:0160110,GO:0160112,GO:0160113,GO:0160114; GO:0140535 and GO:0036064 definitions, aspect and obsolescence | supports | Intracellular protein-containing complex is a broader class and ciliary basal body is parthood; connected modules are distinct identities. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=285686%2C3055%2C5762%2C5888%2C5911%2C63628; Top-level NCBITaxon:5911 | supports | Tetrahymena thermophila is the species, not an assertion that SB210 reference sequences are paired with SB715 experimental material. |
| pdb | https://data.rcsb.org/rest/v1/core/entry/9QZC; Released entry, experimental method, primary citation and entity inventory | supports | One proximal repeating-unit model with the exact DOI/PMID, not a whole-linker composition or copy-number census. |
| i7mig5 | https://rest.uniprot.org/uniprotkb/I7MIG5.json; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| q22as4 | https://rest.uniprot.org/uniprotkb/Q22AS4.json; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| q24gz2 | https://rest.uniprot.org/uniprotkb/Q24GZ2.json; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| q23ad1 | https://rest.uniprot.org/uniprotkb/Q23AD1.json; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| q23k58 | https://rest.uniprot.org/uniprotkb/Q23K58.json; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| q229z6 | https://rest.uniprot.org/uniprotkb/Q229Z6.json; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| q22z96 | https://rest.uniprot.org/uniprotkb/Q22Z96.json; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| ipr052778 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052778; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| ipr051877 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051877; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| ipr051570 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051570; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| ipr050505 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050505; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| ipr020472 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020472; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| ipr056551 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR056551/; Native identifier, family/domain type or reference protein annotation | supports | Inspected authority annotation supports the bounded identity notes; broad families and domains do not establish exact grounding. Q229Z6 is POC1, unlike the transposed Q22Z96 in Methods. |
| entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/1; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity2 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/2; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity3 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/3; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity4 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/4; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity5 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/5; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity6 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/6; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity7 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/7; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity8 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/8; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity9 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/9; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity10 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/10; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity11 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/11; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity12 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/12; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity13 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/13; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity14 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/14; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| entity15 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/15; Entity description, SIFTS mapping and natural-source taxon | supports | All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain unidentified. |
| assembly | https://data.rcsb.org/rest/v1/core/assembly/9QZC/1; Assembly 1 identity and entity counts | supports | Deposited 18-chain repeating-unit assembly is not whole-linker stoichiometry. |
| predecessor | reviews/structured/20261011T103510Z-basal_body_a_c_linker-audit/review.yaml | context_only | Immutable original observation saved and committed before scientific mutation. |
| preservation | /private/tmp/csm-review-20261011T101801Z/preservation.json | context_only | 908 other native records, all previous review/history/legacy files and all biological target fields verified unchanged. |
| embeddings | /private/tmp/csm-review-20261011T101801Z/embedding-preservation.json | context_only | 909 semantic projections remain valid and stored vector artifact bytes are unchanged. |
| red-test | /private/tmp/csm-review-20261011T101801Z/regressions-red-command.json | context_only | New caption test failed on original native content; image-byte preservation test passed. |
| green-tests | /private/tmp/csm-review-20261011T101801Z/post-focused-command.json | context_only | Both new regression tests and guarded-writer tests passed after correction. |
| edit-history | history/records/basal_body_a_c_linker/2026-10-11T103637Z-codex-093184.yaml | context_only | Append-only EDIT history links issue 2206, the saved finding, original actor and narrow correction. |

## Limits And Additional Notes

- Same-agent disposition, not independent human approval or a new whole-record review.
- No source image was reprocessed and no raw experimental data were reanalyzed. Existing protein-family and model-assignment uncertainties remain unchanged.
- Native resolver and label namespace skips are retained in check logs, not claimed as successful resolutions. Full QC retains the three existing empty-parameter skips.
- Exact disposition source revision retained by review-base/ac-linker-image-provenance-20261011. Required PR and native merge-group CI remain separate publication gates.
- This disposition concerns only the A-C linker finding; adjacent-record coverage is accounted for separately in the operational worklist.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T105559Z-basal_body_a_c_linker-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Basal body A-C linker: image-provenance finding disposition'
started_at: '2026-10-11T10:44:41Z'
finished_at: '2026-10-11T10:55:59Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent correction and source-based diff assessment, not
    independent or human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact predecessor minor finding is resolved by a bounded source-provenance
  correction. Original review and native scientific status remain unchanged.
source:
  git_revision: 4a26f3b04e73502cfb362297a1d8e685fc599e22
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
  - path: README.md
    sha256: 64862db2087298ae832b8a8410185349cc277151af31d88ce231e43201ab9440
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/images/cytoskeleton/basal_body_a_c_linker/pmc12506977_f1.jpg
    sha256: fe0ce1a1e2152db5441413b3f999800bb60903ecfd8664ddcb78b352d3d995ad
    role: context
  - path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    sha256: 818592b3a8a807ee94f6de26d50992ac0589c4bdcd261a0443df16dbc16edff9
    role: context
  - path: data/structures/cytoskeleton/basal_body_a_c_linker.yaml
    sha256: 7f775011ac08af6de13ae9266f909d83a190c2b7a02d633945eee4c094dad6a9
    role: target
  - path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    sha256: 1fda2a9ff6bec4d4b314bdd8f5995a2a2e21a8f6d11286eed800057257e2028b
    role: context
  - path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
    sha256: ad4e6fcf7639e0fffc00b553b0ab2e0e2a8eac5981b87ae9da1ee783ba942957
    role: context
  - path: data/structures/cytoskeleton/basal_body_d2_rod.yaml
    sha256: acd457cb1d0121248e5d11bdebc1d70a815a42f240f31e02eaa556bc54e7bc27
    role: context
  - path: data/structures/cytoskeleton/basal_body_inner_scaffold.yaml
    sha256: b320c60ebc92c55021e2a673b4a4d696ad3a2d8dc8fae6a704cb972814ce2443
    role: context
  - path: data/structures/cytoskeleton/basal_body_pinhead.yaml
    sha256: ef3da1eee8d7e92150c0bf3ab1c6e2c67a410aa366416ab03454e3929e25bff2
    role: context
  - path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    sha256: 8f80489e9683ac36bb07ed5c1c435a1627df5e71c9458f1fcc1f842d65a93128
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
  - path: history/records/basal_body_a_c_linker/2026-10-04T075437Z-codex-9b6ab8.yaml
    sha256: 1f970a4805d9ee578dcd412093e8b23cbe6b0f637e5d5cd546e014ef2fbe2cd6
    role: context
  - path: history/records/basal_body_a_c_linker/2026-10-11T103637Z-codex-093184.yaml
    sha256: 48e2b3fe0d605552b47d6e5cd40e8bc07c2cf92c133992c80918486f2500f6bc
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/20261004T081554Z-basal_body_a_c_linker.md
    sha256: c45ebf7d5184587944bba727c880a3f2b71924c9c93a9e3ba5c67d0dd942bb1a
    role: context
  - path: reviews/structured/20261011T103510Z-basal_body_a_c_linker-audit/review.yaml
    sha256: 332fe17d2722af061802424fc9901e974fb244cbf31f9a745e3caacb29252e96
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_ac_linker_image_provenance.py
    sha256: eed60948994a87efe49cc629cdd03669e3421d948e7c9726cb8c9d1934d9600e
    role: context
targets:
- target_id: cellstructuremech:basal_body_a_c_linker
  path: data/structures/cytoskeleton/basal_body_a_c_linker.yaml
  label: basal body A-C linker
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_a_c_linker.yaml
    role: maintained scientific record
scope:
  description: Reassessment of the exact saved image-processing provenance finding
    and preservation of surrounding claims, not a second whole-record scientific review.
  selection: 20261011T103510Z-basal_body_a_c_linker-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:basal_body_a_c_linker
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_a_c_linker.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed; deterministic validation is not scientific
    certification.
  scope_note: 2026-10-11T10:36:47Z to 2026-10-11T10:36:52Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_a_c_linker.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed; deterministic validation is not scientific
    certification.
  scope_note: 2026-10-11T10:36:52Z to 2026-10-11T10:36:59Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/basal_body_a_c_linker.yaml
    --report /private/tmp/csm-review-20261011T101801Z/ac-post-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets in this target; the caption and source-method paraphrase
    were directly assessed.
  scope_note: 2026-10-11T10:36:59Z to 2026-10-11T10:37:46Z; log SHA-256 8382e8c9525a451b2f9cdf0fb8e2fede4154cb09b7c7e823eaff9c5c31939116
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed; deterministic validation is not scientific
    certification.
  scope_note: 2026-10-11T10:37:46Z to 2026-10-11T10:38:11Z; log SHA-256 f00ebf2ee1c204d28f7f6dcfd42f18015316dc3f19eaaecca2d1e886dd49b57f
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T10:38:11Z to 2026-10-11T10:39:58Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed; deterministic validation is not scientific
    certification.
  scope_note: 2026-10-11T10:39:58Z to 2026-10-11T10:40:24Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T10:40:24Z to 2026-10-11T10:41:17Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: focused
  name: focused
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: .venv/bin/python -m pytest -q tests/test_ac_linker_image_provenance.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '..........................                                               [100%]

    26 passed in 45.17s'
  scope_note: 2026-10-11T10:41:17Z to 2026-10-11T10:42:04Z; log SHA-256 8e8af38afcde797dc1329a1bf9ed44fe2ba12bf58a1b8ce791e7cf60d8af61b9
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: .venv/bin/python scripts/record_review.py check --base 527564e7ff415530f51e19691746fbd2fb790a31
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed; deterministic validation is not scientific
    certification.
  scope_note: 2026-10-11T10:42:04Z to 2026-10-11T10:43:24Z; log SHA-256 a62b5862716669b676a79de93f0983a82cba1da5f37806b95b39827e14a1fe46
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation check passed; deterministic validation is not scientific
    certification.
  scope_note: 2026-10-11T10:43:24Z to 2026-10-11T10:43:24Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: release-qc
  name: release-qc
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full local QC passed: 848 passed, 3 skipped in 550.09s (0:09:10). Required
    remote PR and native merge-group checks are separate publication gates.'
  scope_note: 2026-10-11T10:44:01Z to 2026-10-11T10:55:56Z; log SHA-256 43b62d3d6e915b2ac5cd651719375da75ccb8778dff2c4939f247cb6d1e8665d
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_a_c_linker.yaml
  accessed_at: '2026-10-11T10:55:59Z'
  snapshot_sha256: 7f775011ac08af6de13ae9266f909d83a190c2b7a02d633945eee4c094dad6a9
  support: context_only
  summary: Corrected native record reread; structured diff confirms only the declared
    image fields and appended curation event changed.
- evidence_id: rules
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  accessed_at: '2026-10-11T10:35:10Z'
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
  support: context_only
  summary: Image method and figure provenance must agree with the exact source context.
- evidence_id: profile
  kind: record_content
  reference: docs/record-review-profile.md
  accessed_at: '2026-10-11T10:35:10Z'
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
  support: context_only
  summary: 'Issue-only persistence: this concrete caption provenance defect qualifies;
    unknown families and optional gaps do not.'
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T101801Z/basal_body_a_c_linker-discussion-history.json
  accessed_at: '2026-10-11T10:35:10Z'
  snapshot_sha256: 38c0b027b0068063a850e087ff8743ce086a5399223fd78253dc7a6b0a117110
  support: context_only
  summary: All committed discussion and curation versions inspected; no rationale
    or discussion lifecycle loss observed.
- evidence_id: append-history
  kind: record_content
  reference: history/records/basal_body_a_c_linker/2026-10-04T075437Z-codex-9b6ab8.yaml
  accessed_at: '2026-10-11T10:35:10Z'
  snapshot_sha256: 1f970a4805d9ee578dcd412093e8b23cbe6b0f637e5d5cd546e014ef2fbe2cd6
  support: context_only
  summary: Original CREATE history and actor attribution retained.
- evidence_id: legacy
  kind: prior_review
  reference: reports/yaml_record_review/20261004T081554Z-basal_body_a_c_linker.md
  accessed_at: '2026-10-11T10:35:10Z'
  snapshot_sha256: c45ebf7d5184587944bba727c880a3f2b71924c9c93a9e3ba5c67d0dd942bb1a
  support: context_only
  summary: Earlier clean same-agent report is historical context; it did not flag
    the raw-versus-denoised caption. It is not rewritten or fabricated as canonical
    lineage.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T101801Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T10:35:10Z'
  snapshot_sha256: 87353797a95ce55d12096f92c2033b9eb662b583a2a125c3dda14c26140ad426
  support: context_only
  summary: Gitignore-independent scan of canonical reviews found no exact-target predecessor.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T101801Z/adapter.log
  accessed_at: '2026-10-11T10:35:10Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live 28-dataset iModulonDB inventory has no Tetrahymena dataset. Not applicable
    to these structural claims; no biological absence inferred.
- evidence_id: paper
  kind: primary_source
  reference: DOI:10.1126/sciadv.ady3689
  locator: Complete relevant Results, Discussion, isolation, reconstruction, modeling,
    U-ExM Methods, data availability and figure captions; Methods section Cryo-ET
    data collection, cryo-tomogram reconstruction, and segmentation
  accessed_at: '2026-10-11T09:44:46Z'
  snapshot_sha256: ab8bf23b7821eaa514f3eebd1c4f281e1eb1c2af9ef4dc429aced2fe5dfcb04a
  support: supports
  summary: The Methods specify DeepDeWedge contrast improvement of FIB-milled cell
    tomograms and segmentation of the denoised Figure 1A tomogram. The figure displays
    processed tomographic sections, not raw in-situ images. Main text supports the
    four families, proximal/transitional distinction and bounded modeled contacts.
- evidence_id: manifest
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC12506977.1.json
  locator: Official PMC12506977.1 DOI, PMID, license and media MD5 manifest
  accessed_at: '2026-10-11T09:44:46Z'
  snapshot_sha256: dac56c13e812b5becaf404619dfddcfafbaa975a0afe83db8cb1d6895f62d109
  support: supports
  summary: DOI 10.1126/sciadv.ady3689 / PMID 41061066 match. JATS and figure checksums
    verified; JATS explicitly licenses CC BY 4.0.
- evidence_id: figure1
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f1.jpg
  locator: Entire figure inspected visually, including A-C and F-G panels and scale
    bars
  accessed_at: '2026-10-11T09:44:54Z'
  snapshot_sha256: fe0ce1a1e2152db5441413b3f999800bb60903ecfd8664ddcb78b352d3d995ad
  support: supports
  summary: Figure 1 shows the same preserved source bytes, with segmented and unsegmented
    image views, isolation schematic and gel. The term raw in the native caption does
    not disclose the documented denoising.
- evidence_id: figure3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f3.jpg
  locator: Visually inspected original figure; official manifest MD5 matched
  accessed_at: '2026-10-11T10:33:17Z'
  snapshot_sha256: 04ddc43ec96b711f4f4b55fe134856028aa1fa0c66748aa7a731626ed82d5a6b
  support: supports
  summary: Checks the C-link and A-link contacts, CEP135 bridge, and proximal/transitional
    composition. Figure 6 C/D caption labels conflict with the actual panel titles;
    native discussion already preserves this.
- evidence_id: figure5
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f5.jpg
  locator: Visually inspected original figure; official manifest MD5 matched
  accessed_at: '2026-10-11T10:33:18Z'
  snapshot_sha256: f3cc84042d2a0b109d5de9b7970c47bba8bb286208282558f17a1bed3e256dd8
  support: supports
  summary: Checks the C-link and A-link contacts, CEP135 bridge, and proximal/transitional
    composition. Figure 6 C/D caption labels conflict with the actual panel titles;
    native discussion already preserves this.
- evidence_id: figure6
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f6.jpg
  locator: Visually inspected original figure; official manifest MD5 matched
  accessed_at: '2026-10-11T10:33:18Z'
  snapshot_sha256: 269c7e2c41cfdcd2b6e270a4210bfc7534bbe99ee154ffa541c6d5fa667daea8
  support: supports
  summary: Checks the C-link and A-link contacts, CEP135 bridge, and proximal/transitional
    composition. Figure 6 C/D caption labels conflict with the actual panel titles;
    native discussion already preserves this.
- evidence_id: figure4
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f4.jpg
  locator: Visually inspected original Figure 4, panels A-F; official MD5 matched
  accessed_at: '2026-10-11T10:32:01Z'
  snapshot_sha256: 1db3325f905ae3d30234a23b6184ebfac416f2b1fd56a63ca9e84c63c1094fd7
  support: supports
  summary: POC1 continues into the B-C junction, whereas I7LY02 is adjacent junction
    material, not an A-C-linker constituent.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005575,GO:0005856,GO:0005879,GO:0032053,GO:0032991,GO:0036064,GO:0097545,GO:0097649,GO:0097650,GO:0110165,GO:0120280,GO:0140180,GO:0140535,GO:0160110,GO:0160112,GO:0160113,GO:0160114
  locator: GO:0140535 and GO:0036064 definitions, aspect and obsolescence
  accessed_at: '2026-10-11T09:44:12Z'
  snapshot_sha256: 55218f64ea9ce115bdafbfb9b583c1799457662afcd378d4d01d29704fdc8d09
  support: supports
  summary: Intracellular protein-containing complex is a broader class and ciliary
    basal body is parthood; connected modules are distinct identities.
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=285686%2C3055%2C5762%2C5888%2C5911%2C63628
  locator: Top-level NCBITaxon:5911
  accessed_at: '2026-10-11T09:36:27Z'
  snapshot_sha256: dc9bf03533798607ae6a53c723c8b6f9c70991fc4b14d36a48a152a3c938d348
  support: supports
  summary: Tetrahymena thermophila is the species, not an assertion that SB210 reference
    sequences are paired with SB715 experimental material.
- evidence_id: pdb
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/entry/9QZC
  locator: Released entry, experimental method, primary citation and entity inventory
  accessed_at: '2026-10-11T09:45:04Z'
  snapshot_sha256: fa18389adfa6aca86365858ae57403936e2d6bb8846950c1756e9c5ea85a3848
  support: supports
  summary: One proximal repeating-unit model with the exact DOI/PMID, not a whole-linker
    composition or copy-number census.
- evidence_id: i7mig5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/I7MIG5.json
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:48Z'
  snapshot_sha256: 4abb4a9a55eead81a4e033cd835b533031bb3d4d57300167231d6b3bfc617e26
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: q22as4
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q22AS4.json
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:51Z'
  snapshot_sha256: 235e534db841bb328f8f11e812c2587f804274ec9975a9a5cf2a2430b0d9b8fc
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: q24gz2
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q24GZ2.json
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:57Z'
  snapshot_sha256: f45a91f4f8de5b4c4ab7b1a234aa13c322710b7ee491fdff3b46f2a134a5933f
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: q23ad1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q23AD1.json
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:54Z'
  snapshot_sha256: 2f65f8c5eef168f1e427262e6737cc783a4325bb1825fb2ad35d70016e9b211e
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: q23k58
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q23K58.json
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:56Z'
  snapshot_sha256: 6463d22eca77ce4b0347e800b0aa13c70576af21bd8e46ef2e755baa56803b10
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: q229z6
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q229Z6.json
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:50Z'
  snapshot_sha256: 45fe8bfe44940fa5e6f88c4006a73023c6cba9d2d9a81911e7922be2e3fa72d7
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: q22z96
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q22Z96.json
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:52Z'
  snapshot_sha256: 26e83308d798f7e2c18b91b26f96b48045ba48436158cf3f511e6bd188cbd24e
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: ipr052778
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052778
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:43Z'
  snapshot_sha256: fb0d34d6366b09dddcd5c6e05bd448bc6d9d0e4a7ddb9c6bdbf54d44dacc1e82
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: ipr051877
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051877
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:42Z'
  snapshot_sha256: ef5b481674874d1e56d39f6808f575fbee42919f894ad36b3aef1ea0d1b1645e
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: ipr051570
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051570
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:41Z'
  snapshot_sha256: 15a86a5889439fccc900a2af44cb0977a2ddd34ab62497f3fda9289bda099e8d
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: ipr050505
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050505
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:39Z'
  snapshot_sha256: a441faeaa7da8487b8e14015dcc322403b37d7620dc71a539ed189b411dac195
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: ipr020472
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020472
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T09:44:34Z'
  snapshot_sha256: f5ceeddc437713cad39c49c699d92bf1b9a5bb9ef18d46e036338a736f24f673
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: ipr056551
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR056551/
  locator: Native identifier, family/domain type or reference protein annotation
  accessed_at: '2026-10-11T10:32:45Z'
  snapshot_sha256: 0d4fad01d608cfc20b180d46f26792250befd95a1930d7615e3a832db3169936
  support: supports
  summary: Inspected authority annotation supports the bounded identity notes; broad
    families and domains do not establish exact grounding. Q229Z6 is POC1, unlike
    the transposed Q22Z96 in Methods.
- evidence_id: entity1
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/1
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:04Z'
  snapshot_sha256: 08e396551030caf367f99d4acbfb2b5a520a8e7e8166f6ae1b53501b2f01aadd
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity2
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/2
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:04Z'
  snapshot_sha256: fd614980bac9e58dbf487d4684158ec745e299bc55975f442a35217c3a31ceb7
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity3
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/3
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:04Z'
  snapshot_sha256: 27126063be24c1314412009f3e9e24b58519d251a4f2fca7e3d88615f5b6153b
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity4
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/4
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:04Z'
  snapshot_sha256: 98b8d76cf7eae5de791d5b347a6abb26541035b1a423f7b9943bf09483a994d7
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity5
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/5
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:04Z'
  snapshot_sha256: dcfa684cbb9e0f6374069b18e38ff708f3477f8b4e7cf3035a865ce579fe74e4
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity6
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/6
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: 07337e36fd5c511d281ca41171b665c22a3b263d5a08cc919c9217dac01ac52e
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity7
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/7
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: 466b9f1991952c91da6b2cae3ca3c566c41697d65c1fcec75203b3315b980185
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity8
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/8
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: 6346307a226c5c69d683630ea84e883c4f38ede63bfeae6dbad15632f879f396
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity9
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/9
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: 59ad601e45ad05e42067ea3c79745efed85427e8e78a02101e384425bd2014d5
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity10
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/10
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: 686464f09cbe1928df83b8e969d162d9a4edc0ae04a83220de57c1a3f10f72ff
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity11
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/11
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: 5e04d913ebc78004b756e5fd2cb8288fdd128e01b124b0c2a34fa26a67a4968f
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity12
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/12
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: 1fbdbb9108866fc9f851ff828ba04883fbf5e12d44643435889c711e4de464c9
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity13
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/13
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: 83915908f2453d06eea3cae6f0149f8f19de216581a7b70801beb74222f49ac4
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity14
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/14
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: 788cfa1d3db9afe359ed8f77faa68b64bc89624b5451e7640b0f1728fdea4142
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: entity15
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/15
  locator: Entity description, SIFTS mapping and natural-source taxon
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: cd4da302e16b8965d2d8a6224842bffe7b3d7804f2ba58e844e98dfe4d4bd696
  support: supports
  summary: All 15 entities inspected; entity 2 maps to Q24GZ2 despite Methods choosing
    Q22AS4, entity 8 maps to junction ladder I7LY02, and unassigned chains remain
    unidentified.
- evidence_id: assembly
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/assembly/9QZC/1
  locator: Assembly 1 identity and entity counts
  accessed_at: '2026-10-11T09:45:05Z'
  snapshot_sha256: 15881766371c578441ec74aadeda1a6d414b82ccaaeb5123cf6e17a5771872af
  support: supports
  summary: Deposited 18-chain repeating-unit assembly is not whole-linker stoichiometry.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T103510Z-basal_body_a_c_linker-audit/review.yaml
  accessed_at: '2026-10-11T10:55:59Z'
  snapshot_sha256: 332fe17d2722af061802424fc9901e974fb244cbf31f9a745e3caacb29252e96
  support: context_only
  summary: Immutable original observation saved and committed before scientific mutation.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T101801Z/preservation.json
  accessed_at: '2026-10-11T10:55:59Z'
  snapshot_sha256: a4a7e7ec0593504845d7f6230ac1b55f041eef4bf9e608e9723f666419d6b673
  support: context_only
  summary: 908 other native records, all previous review/history/legacy files and
    all biological target fields verified unchanged.
- evidence_id: embeddings
  kind: validation
  reference: /private/tmp/csm-review-20261011T101801Z/embedding-preservation.json
  accessed_at: '2026-10-11T10:55:59Z'
  snapshot_sha256: 78da96344eaef54b136e1d63283106344855ccddef434b940b096e2b4a2e4d49
  support: context_only
  summary: 909 semantic projections remain valid and stored vector artifact bytes
    are unchanged.
- evidence_id: red-test
  kind: validation
  reference: /private/tmp/csm-review-20261011T101801Z/regressions-red-command.json
  accessed_at: '2026-10-11T10:55:59Z'
  snapshot_sha256: 33851e28d6197933fee6071d04a3205d1a3360dc1a463350ba36e907f1fed0b5
  support: context_only
  summary: New caption test failed on original native content; image-byte preservation
    test passed.
- evidence_id: green-tests
  kind: validation
  reference: /private/tmp/csm-review-20261011T101801Z/post-focused-command.json
  accessed_at: '2026-10-11T10:55:59Z'
  snapshot_sha256: d36d1cdb36c2a978edab44226c8fc860c3f23dca083534242d1b2d0fa26042d3
  support: context_only
  summary: Both new regression tests and guarded-writer tests passed after correction.
- evidence_id: edit-history
  kind: record_content
  reference: history/records/basal_body_a_c_linker/2026-10-11T103637Z-codex-093184.yaml
  accessed_at: '2026-10-11T10:55:59Z'
  snapshot_sha256: 48e2b3fe0d605552b47d6e5cd40e8bc07c2cf92c133992c80918486f2500f6bc
  support: context_only
  summary: Append-only EDIT history links issue 2206, the saved finding, original
    actor and narrow correction.
assessments:
- assessment_id: resolved-image-provenance
  area: provenance
  topic: Describe the A-C linker tomograms as denoised, not raw
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  evidence_ids:
  - record
  - paper
  - figure1
  - rules
  - predecessor
  - preservation
  - red-test
  - green-tests
  - edit-history
  summary: The caption now describes denoised in-situ cryotomograms, and an appended
    source-method note names DeepDeWedge and the denoised Figure 1A volume. It explicitly
    attributes processing to the source authors. Original figure bytes, accession,
    license, attribution, panel roles and scale bars are unchanged. All biological
    fields and five discussions remain identical; only image wording and an appended
    curation event changed, with new repository EDIT history.
findings:
- finding_id: F1
  issue_key: ac-linker-denoised-tomogram-provenance
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Describe the A-C linker tomograms as denoised, not raw
  description: The caption now describes denoised in-situ cryotomograms, and an appended
    source-method note names DeepDeWedge and the denoised Figure 1A volume. It explicitly
    attributes processing to the source authors. Original figure bytes, accession,
    license, attribution, panel roles and scale bars are unchanged. All biological
    fields and five discussions remain identical; only image wording and an appended
    curation event changed, with new repository EDIT history.
  target_ids:
  - cellstructuremech:basal_body_a_c_linker
  field_paths:
  - images[0].caption
  - images[0].notes
  evidence_ids:
  - record
  - paper
  - figure1
  - rules
  - predecessor
  - preservation
  - red-test
  - green-tests
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_a_c_linker.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md#field-by-field-audit
  native_severity: minor
  normalization_reason: A bounded source-attribution or discussion-provenance defect;
    the biological identity and structure boundaries remain supported.
  disposition_reason: The caption now describes denoised in-situ cryotomograms, and
    an appended source-method note names DeepDeWedge and the denoised Figure 1A volume.
    It explicitly attributes processing to the source authors. Original figure bytes,
    accession, license, attribution, panel roles and scale bars are unchanged. All
    biological fields and five discussions remain identical; only image wording and
    an appended curation event changed, with new repository EDIT history. Verified
    against inspected primary Methods, exact original image hash, red/green regressions
    and full QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T103510Z-basal_body_a_c_linker-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2206
actions: []
limitations:
- Same-agent disposition, not independent human approval or a new whole-record review.
- No source image was reprocessed and no raw experimental data were reanalyzed. Existing
  protein-family and model-assignment uncertainties remain unchanged.
- Native resolver and label namespace skips are retained in check logs, not claimed
  as successful resolutions. Full QC retains the three existing empty-parameter skips.
- Exact disposition source revision retained by review-base/ac-linker-image-provenance-20261011.
  Required PR and native merge-group CI remain separate publication gates.
- This disposition concerns only the A-C linker finding; adjacent-record coverage
  is accounted for separately in the operational worklist.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2206
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T103510Z-basal_body_a_c_linker-audit
  relationship: Resolves the exact predecessor finding without overwriting its observation.
```
