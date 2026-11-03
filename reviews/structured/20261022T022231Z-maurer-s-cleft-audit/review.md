# Maurer's cleft identity, trafficking and evidence placement review

- Review: 20261022T022231Z-maurer-s-cleft-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:02:52Z
- Finished UTC: 2026-10-22T02:22:31Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Maurer's cleft identity, component membership, infected-erythrocyte scope and coarse trafficking graph are supported. One minor finding corrects the canonical example's combined genetic-study attribution.

## Scope And Provenance

Full target; exact native identities, all citation abstracts, complete Cooke scientific main text/Methods and enumerated Spycher publisher-body excerpts.

Selection: Batch32 target1; initial native inspect/schema/strict passed before assessment at immutable f97b1abe.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0020036 | data/structures/membrane_organelle/maurer_s_cleft.yaml | maintained | Maurer's cleft |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native verify | passed | True | GO:0020036 | Read-only check passed; diagnostic coverage is assessed separately. |
| Native causal-graphs | passed | True | GO:0020036 | Read-only check passed; diagnostic coverage is assessed separately. |
| Focused native schema | passed | True | GO:0020036 | Focused validator passed. |
| Focused native strict | passed | True | GO:0020036 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0020036 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0020036 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0020036 | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0020036 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0020036 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0020036 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0020036 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0020036 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Parasite-derived organelle in infected erythrocytes

identity: supported. Targets: GO:0020036.

The exact GO identity and broader intracellular-membrane parent are supported. The resolved interpretation correctly assigns parasite origin and infected-host cytoplasm without treating the cleft as a normal conserved erythrocyte organelle.

### Collective bilayer and source-defined protein classes

grounding: supported. Targets: GO:0020036.

The label-only bilayer represents collective constituting lipid material with no erroneous whole-organelle molecular grounding. SBP1, MAHRP1 and REX1 membership are supported. Neither an unrelated domain/family hit nor a complete resident-protein census is forced.

### Assembly necessity differs from PfEMP1 display

evidence: unknown. Targets: GO:0020036.

The collective bilayer is constitutive of this membrane-bounded identity, but individual chemical formation requirements are not experimentally established. SBP1 and MAHRP1 perturbations affect display while clefts persist, consistent with UNKNOWN component essentiality. Functional necessity cannot be substituted for structure formation necessity.

### Species and blood-stage bounds

scope: supported. Targets: GO:0020036.

Qualitative COMMON and the canonical P. falciparum example fit asexual blood-stage infected-erythrocyte studies. Native identity-only entries are not asserted to be identical 3D7 constructs. No extension to all apicomplexans or all life stages is inferred.

### Canonical note combines two genetic studies

evidence: concern. Targets: GO:0020036.

The biological example is supported across the record, but its sole Cooke2006 reference tests SBP1 deletion and uses MAHRP1 as a marker. The additional MAHRP1 genetic-test assertion needs the already-listed Spycher2008 source at this claim or narrower wording.

### Five descriptive trafficking and boundary edges

graph: supported. Targets: GO:0020036.

The five NONMECHANISTIC edges and trafficking function are supported. SBP1 localization is direct; anchoring remains implicated, not a settled mechanism. Cooke 3D7 cleft trapping and Spycher MAHRP1 earlier-trafficking defects are distinct. No direct cargo binding, vesicle itinerary or universal strain-specific phenotype is inferred.

### Open grounding follow-up

completeness: unknown. Targets: GO:0020036.

The inspected exact queries do not establish an exact class-wide mapping for the unrelated resident cohort or SBP1. IPR044661 is retained as a problematic broad candidate, not promoted to the maintained component. Optional inventory gaps alone are not findings.

## Findings

### F1: Align the canonical genetic-study note with its cited paper

minor / open / confirmed; issue key: maurer-canonical-genetic-study-attribution.

The canonical note attributes genetic testing of both SBP1 and MAHRP1 to its sole Cooke2006 citation. Cooke tests SBP1 deletion/complementation; the MAHRP1 genetic test is in Spycher2008, already listed elsewhere in the record.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, narrow the Cooke-linked canonical note to SBP1 or represent the MAHRP1 clause with the exact Spycher2008 supporting source.

- Cooke2006 is attached only to its SBP1 intervention and observed phenotype.
- Any retained MAHRP1 genetic-test clause has Spycher2008 claim-level support; preserve correct P. falciparum identity and differing intervention effects.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/maurer_s_cleft.yaml; Entire maintained target, all components, examples, functions, graph edges and discussions | context_only | The complete record was read without editing its science or history. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent grounding, ProteinExample and component_role/essentiality | context_only | Molecular identity, organism-specific examples, localization, functional requirement and structure formation necessity are separate claims. |
| maurer-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020036,GO:0043231; Both complete labels, definitions, active flags, synonyms and returned relations | supports | Active GO0020036 matches the complete definition. GO0043231 defines intracellular single- or double-bilayer-bounded organelles; the broader parent is biologically compatible with the infected host-cell cytoplasm, without asserting a captured direct GO edge. |
| maurer-agent-tax5833 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833; Complete taxId/scientificName/rank/lineage | supports | ENA confirms Plasmodium falciparum as species5833. Taxon identity does not itself establish blood-stage occurrence. |
| maurer-agent-lanzer2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.ijpara.2005.10.001%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact MED result and complete abstract | supports | Exact native DOI, title, authors, year and complete abstract read for lanzer2006. This source is a literature review. |
| maurer-agent-blisnick2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2FS0166-6851%2800%2900301-7%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact MED result and complete abstract | supports | Exact native DOI, title, authors, year and complete abstract read for blisnick2000. This is a primary study. |
| maurer-agent-cooke2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200509122%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact MED result and complete abstract | supports | Exact native DOI, title, authors, year and complete abstract read for cooke2006. This is a primary study. |
| maurer-agent-spycher2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fj.1365-2958.2008.06235.x%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact MED result and complete abstract | supports | Exact native DOI, title, authors, year and complete abstract read for spycher2008. This is a primary study. |
| maurer-agent-cooke2006-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2063733/; Entire Introduction sec1; all Results sec3–8 and Figures1–7 captions; complete Discussion sec9 and Methods sec11–20. No figure pixels or separate supplemental experiment reanalysis. | supports | Primary 3D7 SBP1 deletion and complementation support PfEMP1 surface-display dependence while clefts and other exported proteins remain. MAHRP1 and REX1 are localization markers here, not the deleted gene. Discussion explicitly distinguishes functional display from cleft formation and does not establish direct SBP1–PfEMP1 binding. |
| maurer-agent-spycher2008-browser | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2008.06235.x; Publisher-displayed Summary, complete Introduction, Results through ultrastructure and Figure5 caption, displayed lines0–278 | supports | The primary 3D7 MAHRP1 disruption study tests its role in PfEMP1 trafficking; resident REX1/SBP1 and cleft formation are retained. |
| maurer-agent-spycher2008-browser-rest | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2008.06235.x; Publisher-displayed remaining Results/Figures6–7 captions and complete Discussion lines237–328; early Experimental procedures through Western blotting lines333–350 | supports | MAHRP1 complementation supports surface presentation. Discussion distinguishes its earlier trafficking defect from the Cooke 3D7 SBP1 phenotype; exact anchoring/chaperone mechanisms remain unresolved. |
| maurer-agent-Q6V0W9 | https://rest.uniprot.org/uniprotkb/Q6V0W9.json; Accession/status/protein names/gene/organism and source-sequence reference | supports | Unreviewed MAHRP1 fragment, gene mahrp1, P. falciparum5833; original sequence reference names IFA18. This is a representative identity, not the exact 3D7 experimental construct. |
| maurer-agent-Q9NFF5 | https://rest.uniprot.org/uniprotkb/Q9NFF5.json; Accession/status/protein names/gene/organism and available annotations | supports | Unreviewed skeleton-binding protein1, gene sbp1, P. falciparum5833. Native identity agrees; independent localization/function relies on primary papers. |
| maurer-agent-gene-MAHRP1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMAHRP1%29+AND+%28taxonomy_id%3A5833%29&amp;format=json&amp;size=100; Complete exact native query response | context_only | Exact query returns six unreviewed MAHRP1 entries including Q6V0W9; the record correctly calls its example representative. |
| maurer-agent-gene-SBP1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASBP1%29+AND+%28taxonomy_id%3A5833%29&amp;format=json&amp;size=100; Complete exact native query response | context_only | Exact query returns Q9NFF5; gene-case differences are not conflicting protein identities. |
| maurer-agent-gene-REX1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AREX1%29+AND+%28taxonomy_id%3A5833%29&amp;format=json&amp;size=100; Complete exact native query response | context_only | Exact UniProt gene query returns no entries. REX1 localization is directly reported by the inspected primary figures/captions; this empty query does not negate the protein or establish exhaustive identifier absence. |
| maurer-agent-ipr-Q6V0W9 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q6V0W9/?page_size=200; Complete exact native query response | context_only | Exact InterPro entry-by-protein query returns HTTP204 empty. It is a bounded candidate search, not proof of no possible family. |
| maurer-agent-ipr-Q9NFF5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9NFF5/?page_size=200; Complete returned entry match and next-page field | supports | The exact protein query returns an integrated IPR044661 match. A returned match is not automatically an exact family for the maintained SBP1 functional class. |
| maurer-agent-IPR044661 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044661/; Complete family name/type, description, member database and cited scope | supports | Native IPR044661 is the MED15a/b/c-like transcriptional mediator family, described using plant transcription studies. It does not independently establish equivalence to the Maurer-cleft SBP1 constituent class. |
| maurer-agent-verify | /private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/maurer_s_cleft.yaml --verify; Complete native read-only log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| maurer-agent-causal-graphs | /private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/maurer_s_cleft.yaml --causal-graphs; Complete native read-only log | supports | data/structures/membrane_organelle/maurer_s_cleft.yaml  (GO:0020036)<br>  maurers_cleft_pfemp1_trafficking	skeleton_binding_protein_1	COVERED	-&gt;skeleton_binding_protein_1 (UniProtKB:Q9NFF5)<br>  maurers_cleft_pfemp1_trafficking	maurers_cleft_resident_proteins	PARTIAL_EXAMPLES	-&gt;maurers_cleft_resident_proteins (have: UniProtKB:Q6V0W9; missing: REX1)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/maurer_s_cleft.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/maurer_s_cleft.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/maurer_s_cleft.yaml --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/maurer_s_cleft-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/maurer_s_cleft.yaml --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/maurer_s_cleft-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch32-20261022-k96_2wx1/maurer_s_cleft-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/maurer_s_cleft.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Lanzer2006 is review-tier and was inspected at complete native abstract level. Blisnick2000 primary evidence was inspected at complete native abstract level; direct DOI routes produced transport-error responses, not usable full bodies.
- Spycher2008 direct native publisher request returned403; genuine browser-displayed claim-bearing Results/Discussion were recovered and frozen with status:null, not an HTTP200 attestation. Methods after early Western-blotting subsection and figure pixels were not inspected.
- No raw microscopy, supplemental FRET/co-immunoprecipitation data, quantitative morphometry or full lipid composition was reanalyzed. Negative direct-binding inference is the primary Discussion report, not an independent experiment.
- Exact family searches are bounded; a returned broad mediator-family hit is not accepted as an exact SBP1-class identity. Optional constituent coverage is incomplete.
- Collective constitutive material, individual formation necessity, trafficking function and direct binding remain separate. Unreviewed fragment/strain provenance limits accession-specific functional inference.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- Original URL, UTC access and SHA256 are retained. Parent owns finalization.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T022231Z-maurer-s-cleft-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Maurer's cleft identity, trafficking and evidence placement review
started_at: '2026-10-22T02:02:52Z'
finished_at: '2026-10-22T02:22:31Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Maurer's cleft identity, component membership, infected-erythrocyte scope
  and coarse trafficking graph are supported. One minor finding corrects the canonical
  example's combined genetic-study attribution.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
  state: working_tree
  inputs:
  - path: .claude/skills/curate-causal-graphs/SKILL.md
    sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/literature-evidence/SKILL.md
    sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/maurer_s_cleft.yaml
    sha256: e8745451600446a168d2c417a41d1628fe36a02952f9d64157a9764e7ab44455
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
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0020036
  path: data/structures/membrane_organelle/maurer_s_cleft.yaml
  label: Maurer's cleft
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/maurer_s_cleft.yaml
    role: maintained scientific record
scope:
  description: Full target; exact native identities, all citation abstracts, complete
    Cooke scientific main text/Methods and enumerated Spycher publisher-body excerpts.
  selection: Batch32 target1; initial native inspect/schema/strict passed before assessment
    at immutable f97b1abe.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0020036
checks:
- check_id: verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: /private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/maurer_s_cleft.yaml
    --verify
  exit_code: 0
  summary: Read-only check passed; diagnostic coverage is assessed separately.
  evidence_ids:
  - maurer-agent-verify
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: /private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/maurer_s_cleft.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only check passed; diagnostic coverage is assessed separately.
  evidence_ids:
  - maurer-agent-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: just validate data/structures/membrane_organelle/maurer_s_cleft.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: just validate-strict data/structures/membrane_organelle/maurer_s_cleft.yaml
    --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/maurer_s_cleft-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0020036
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0020036
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - maurer-agent-go
  - maurer-agent-tax5833
  - maurer-agent-lanzer2006-meta
  - maurer-agent-blisnick2000-meta
  - maurer-agent-cooke2006-meta
  - maurer-agent-spycher2008-meta
  - maurer-agent-cooke2006-pmc
  - maurer-agent-spycher2008-browser
  - maurer-agent-spycher2008-browser-rest
  - maurer-agent-Q6V0W9
  - maurer-agent-Q9NFF5
  - maurer-agent-gene-MAHRP1
  - maurer-agent-gene-SBP1
  - maurer-agent-gene-REX1
  - maurer-agent-ipr-Q6V0W9
  - maurer-agent-ipr-Q9NFF5
  - maurer-agent-IPR044661
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0020036
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch32 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch32 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch32 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch32 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:34Z to
    2026-10-22T01:34:04Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch32 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/maurer_s_cleft.yaml
  locator: Entire maintained target, all components, examples, functions, graph edges
    and discussions
  accessed_at: '2026-10-22T02:13:44Z'
  support: context_only
  summary: The complete record was read without editing its science or history.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent grounding, ProteinExample and component_role/essentiality
  accessed_at: '2026-10-22T02:13:44Z'
  support: context_only
  summary: Molecular identity, organism-specific examples, localization, functional
    requirement and structure formation necessity are separate claims.
- evidence_id: maurer-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020036,GO:0043231
  locator: Both complete labels, definitions, active flags, synonyms and returned
    relations
  accessed_at: '2026-10-22T02:07:36.265099Z'
  support: supports
  summary: Active GO0020036 matches the complete definition. GO0043231 defines intracellular
    single- or double-bilayer-bounded organelles; the broader parent is biologically
    compatible with the infected host-cell cytoplasm, without asserting a captured
    direct GO edge.
  snapshot_sha256: 144c59239293c0df3e0bd26b340fadf76ef1aae1329721865f0750eb06f21333
- evidence_id: maurer-agent-tax5833
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833
  locator: Complete taxId/scientificName/rank/lineage
  accessed_at: '2026-10-22T02:07:36.264282Z'
  support: supports
  summary: ENA confirms Plasmodium falciparum as species5833. Taxon identity does
    not itself establish blood-stage occurrence.
  snapshot_sha256: 47c9da135299ea0515b9cbddde80166e0e7256bcf1daac4cdf87f8ae3e0ecd11
- evidence_id: maurer-agent-lanzer2006-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.ijpara.2005.10.001%22&format=json&resultType=core&pageSize=100
  locator: Exact MED result and complete abstract
  accessed_at: '2026-10-22T02:07:39.748746Z'
  support: supports
  summary: Exact native DOI, title, authors, year and complete abstract read for lanzer2006.
    This source is a literature review.
  snapshot_sha256: f855246d36e359585f64d538ab7aa49c5f78463bfa6e15381f934deb55d071fa
- evidence_id: maurer-agent-blisnick2000-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2FS0166-6851%2800%2900301-7%22&format=json&resultType=core&pageSize=100
  locator: Exact MED result and complete abstract
  accessed_at: '2026-10-22T02:07:39.749343Z'
  support: supports
  summary: Exact native DOI, title, authors, year and complete abstract read for blisnick2000.
    This is a primary study.
  snapshot_sha256: 0f0c7a7275774af7fca448d53703c37d483c227ee63ad63417fc3c2d012d6b5d
- evidence_id: maurer-agent-cooke2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200509122%22&format=json&resultType=core&pageSize=100
  locator: Exact MED result and complete abstract
  accessed_at: '2026-10-22T02:07:40.798201Z'
  support: supports
  summary: Exact native DOI, title, authors, year and complete abstract read for cooke2006.
    This is a primary study.
  snapshot_sha256: cabd0d96d1c68dae2465a0cc3baf509b0ec7590c65eab787dcea23bbc5c1515e
- evidence_id: maurer-agent-spycher2008-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fj.1365-2958.2008.06235.x%22&format=json&resultType=core&pageSize=100
  locator: Exact MED result and complete abstract
  accessed_at: '2026-10-22T02:07:41.321113Z'
  support: supports
  summary: Exact native DOI, title, authors, year and complete abstract read for spycher2008.
    This is a primary study.
  snapshot_sha256: 8698ee24585705d47d1f451dadd48f52a4ecb877e36dbb383088be56501ece3e
- evidence_id: maurer-agent-cooke2006-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2063733/
  locator: Entire Introduction sec1; all Results sec3–8 and Figures1–7 captions; complete
    Discussion sec9 and Methods sec11–20. No figure pixels or separate supplemental
    experiment reanalysis.
  accessed_at: '2026-10-22T02:08:16.981576Z'
  support: supports
  summary: Primary 3D7 SBP1 deletion and complementation support PfEMP1 surface-display
    dependence while clefts and other exported proteins remain. MAHRP1 and REX1 are
    localization markers here, not the deleted gene. Discussion explicitly distinguishes
    functional display from cleft formation and does not establish direct SBP1–PfEMP1
    binding.
  snapshot_sha256: ad4a24db3ec1461ccb3c2efe81d326a81bdadec6ba6b7051d59f58cf4dd68c09
- evidence_id: maurer-agent-spycher2008-browser
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2008.06235.x
  locator: Publisher-displayed Summary, complete Introduction, Results through ultrastructure
    and Figure5 caption, displayed lines0–278
  accessed_at: '2026-10-22T02:08:32Z'
  support: supports
  summary: The primary 3D7 MAHRP1 disruption study tests its role in PfEMP1 trafficking;
    resident REX1/SBP1 and cleft formation are retained.
  snapshot_sha256: 7f29c61656b32b3fc5d2acc58114cf55e0526f7840e58f45cd766cba46045dff
- evidence_id: maurer-agent-spycher2008-browser-rest
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2008.06235.x
  locator: Publisher-displayed remaining Results/Figures6–7 captions and complete
    Discussion lines237–328; early Experimental procedures through Western blotting
    lines333–350
  accessed_at: '2026-10-22T02:08:49Z'
  support: supports
  summary: MAHRP1 complementation supports surface presentation. Discussion distinguishes
    its earlier trafficking defect from the Cooke 3D7 SBP1 phenotype; exact anchoring/chaperone
    mechanisms remain unresolved.
  snapshot_sha256: f1c9bccccd70300b1540f3169288c944c4a5335f2c3bbfb82c80aa1d34189f59
- evidence_id: maurer-agent-Q6V0W9
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q6V0W9.json
  locator: Accession/status/protein names/gene/organism and source-sequence reference
  accessed_at: '2026-10-22T02:07:37.820152Z'
  support: supports
  summary: Unreviewed MAHRP1 fragment, gene mahrp1, P. falciparum5833; original sequence
    reference names IFA18. This is a representative identity, not the exact 3D7 experimental
    construct.
  snapshot_sha256: 09072d663ec1d345fac57842b18f828aca1785367468892b3b8a58b554dd7df5
- evidence_id: maurer-agent-Q9NFF5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9NFF5.json
  locator: Accession/status/protein names/gene/organism and available annotations
  accessed_at: '2026-10-22T02:07:37.834744Z'
  support: supports
  summary: Unreviewed skeleton-binding protein1, gene sbp1, P. falciparum5833. Native
    identity agrees; independent localization/function relies on primary papers.
  snapshot_sha256: 59a86d923f7785e2771d46622599d0521312197891f59801c67aa72557a16242
- evidence_id: maurer-agent-gene-MAHRP1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMAHRP1%29+AND+%28taxonomy_id%3A5833%29&format=json&size=100
  locator: Complete exact native query response
  accessed_at: '2026-10-22T02:07:43.941910Z'
  support: context_only
  summary: Exact query returns six unreviewed MAHRP1 entries including Q6V0W9; the
    record correctly calls its example representative.
  snapshot_sha256: c001ccecdab258bc54c0003269475454d0f86cdd19a3061348aa4e99b6436627
  search_scope: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMAHRP1%29+AND+%28taxonomy_id%3A5833%29&format=json&size=100;
    exact live native query only
- evidence_id: maurer-agent-gene-SBP1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASBP1%29+AND+%28taxonomy_id%3A5833%29&format=json&size=100
  locator: Complete exact native query response
  accessed_at: '2026-10-22T02:07:44.465273Z'
  support: context_only
  summary: Exact query returns Q9NFF5; gene-case differences are not conflicting protein
    identities.
  snapshot_sha256: ff17fde5dc18d86e5c497a3f0762ea71695bc3f37510b88b9f049e19953d8e10
  search_scope: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASBP1%29+AND+%28taxonomy_id%3A5833%29&format=json&size=100;
    exact live native query only
- evidence_id: maurer-agent-gene-REX1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AREX1%29+AND+%28taxonomy_id%3A5833%29&format=json&size=100
  locator: Complete exact native query response
  accessed_at: '2026-10-22T02:07:44.467610Z'
  support: context_only
  summary: Exact UniProt gene query returns no entries. REX1 localization is directly
    reported by the inspected primary figures/captions; this empty query does not
    negate the protein or establish exhaustive identifier absence.
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AREX1%29+AND+%28taxonomy_id%3A5833%29&format=json&size=100;
    exact live native query only
- evidence_id: maurer-agent-ipr-Q6V0W9
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q6V0W9/?page_size=200
  locator: Complete exact native query response
  accessed_at: '2026-10-22T02:07:42.894472Z'
  support: context_only
  summary: Exact InterPro entry-by-protein query returns HTTP204 empty. It is a bounded
    candidate search, not proof of no possible family.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q6V0W9/?page_size=200;
    exact live native query only
- evidence_id: maurer-agent-ipr-Q9NFF5
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9NFF5/?page_size=200
  locator: Complete returned entry match and next-page field
  accessed_at: '2026-10-22T02:07:42.894733Z'
  support: supports
  summary: The exact protein query returns an integrated IPR044661 match. A returned
    match is not automatically an exact family for the maintained SBP1 functional
    class.
  snapshot_sha256: 60a68fb3ff1de33c4f842517b5d0c3819055913e241200a31cfa3593610d3f8d
- evidence_id: maurer-agent-IPR044661
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044661/
  locator: Complete family name/type, description, member database and cited scope
  accessed_at: '2026-10-22T02:09:12.639670Z'
  support: supports
  summary: Native IPR044661 is the MED15a/b/c-like transcriptional mediator family,
    described using plant transcription studies. It does not independently establish
    equivalence to the Maurer-cleft SBP1 constituent class.
  snapshot_sha256: 23c996f0f35e4e0ac06cbdddba954108020a8e5e8bf750b6d4a72a3aa514ac96
- evidence_id: maurer-agent-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/maurer_s_cleft.yaml
    --verify
  locator: Complete native read-only log
  accessed_at: '2026-10-22T02:12:29.913317Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: maurer-agent-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/maurer_s_cleft.yaml
    --causal-graphs
  locator: Complete native read-only log
  accessed_at: '2026-10-22T02:12:30.408532Z'
  support: supports
  summary: "data/structures/membrane_organelle/maurer_s_cleft.yaml  (GO:0020036)\n\
    \  maurers_cleft_pfemp1_trafficking\tskeleton_binding_protein_1\tCOVERED\t->skeleton_binding_protein_1\
    \ (UniProtKB:Q9NFF5)\n  maurers_cleft_pfemp1_trafficking\tmaurers_cleft_resident_proteins\t\
    PARTIAL_EXAMPLES\t->maurers_cleft_resident_proteins (have: UniProtKB:Q6V0W9; missing:\
    \ REX1)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED      \
    \             component_ref target holds protein_examples covering all declared\
    \ symbols\n     1  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 4f49d03491abb54350d0463ec1f28fa011ac79e50d21edac603544fa6717cd90
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/maurer_s_cleft.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:02:54Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/maurer_s_cleft.yaml'
  snapshot_sha256: bb88e3bfbcaa7a51b31e0aaaa6e8e9c331e2c4c6ef019f72eda38515b61f2ce6
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/maurer_s_cleft.yaml
    --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/maurer_s_cleft-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:02:55Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/maurer_s_cleft.yaml\
    \ --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/maurer_s_cleft-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch32-20261022-k96_2wx1/maurer_s_cleft-strict.tsv"
  snapshot_sha256: d3dbe449eb4b2917b8c89a118cdfab0ca5720c486a2c19133a522bf443af5cde
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/maurer_s_cleft.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  snapshot_sha256: 173c367ec1621e2a96027e149b5cad9f4db0a86f0a3c916455ce192a9aa5f428
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:05:35Z'
  support: supports
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 8696c0d603149cee93ac200eaa3ed26c84320204285cd22cca542eb1ae7ba572
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:37Z'
  support: supports
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  snapshot_sha256: 98a7952c42add0416633f4dee73ff64331e5c6c4c4c8d707e98a152f04fc5b6d
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:59:14Z'
  support: supports
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:40Z'
  support: supports
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  snapshot_sha256: 00cc5664a9143235d28fb9885fc5c43a8a78c9a9c9f47603b1232e1eddddeac1
assessments:
- assessment_id: identity
  area: identity
  topic: Parasite-derived organelle in infected erythrocytes
  outcome: supported
  target_ids:
  - GO:0020036
  summary: The exact GO identity and broader intracellular-membrane parent are supported.
    The resolved interpretation correctly assigns parasite origin and infected-host
    cytoplasm without treating the cleft as a normal conserved erythrocyte organelle.
  evidence_ids:
  - record
  - maurer-agent-go
  - maurer-agent-tax5833
  - maurer-agent-lanzer2006-meta
  - maurer-agent-cooke2006-pmc
  - maurer-agent-spycher2008-browser
  - maurer-agent-spycher2008-browser-rest
- assessment_id: components
  area: grounding
  topic: Collective bilayer and source-defined protein classes
  outcome: supported
  target_ids:
  - GO:0020036
  summary: The label-only bilayer represents collective constituting lipid material
    with no erroneous whole-organelle molecular grounding. SBP1, MAHRP1 and REX1 membership
    are supported. Neither an unrelated domain/family hit nor a complete resident-protein
    census is forced.
  evidence_ids:
  - record
  - schema
  - maurer-agent-cooke2006-pmc
  - maurer-agent-blisnick2000-meta
  - maurer-agent-ipr-Q9NFF5
  - maurer-agent-IPR044661
  - maurer-agent-spycher2008-browser
  - maurer-agent-spycher2008-browser-rest
  - maurer-agent-Q6V0W9
  - maurer-agent-Q9NFF5
  - maurer-agent-gene-MAHRP1
  - maurer-agent-gene-SBP1
  - maurer-agent-gene-REX1
  - maurer-agent-ipr-Q6V0W9
- assessment_id: necessity
  area: evidence
  topic: Assembly necessity differs from PfEMP1 display
  outcome: unknown
  target_ids:
  - GO:0020036
  summary: The collective bilayer is constitutive of this membrane-bounded identity,
    but individual chemical formation requirements are not experimentally established.
    SBP1 and MAHRP1 perturbations affect display while clefts persist, consistent
    with UNKNOWN component essentiality. Functional necessity cannot be substituted
    for structure formation necessity.
  evidence_ids:
  - record
  - schema
  - maurer-agent-cooke2006-pmc
  - maurer-agent-spycher2008-browser
  - maurer-agent-spycher2008-browser-rest
- assessment_id: scope
  area: scope
  topic: Species and blood-stage bounds
  outcome: supported
  target_ids:
  - GO:0020036
  summary: Qualitative COMMON and the canonical P. falciparum example fit asexual
    blood-stage infected-erythrocyte studies. Native identity-only entries are not
    asserted to be identical 3D7 constructs. No extension to all apicomplexans or
    all life stages is inferred.
  evidence_ids:
  - record
  - maurer-agent-tax5833
  - maurer-agent-cooke2006-pmc
  - maurer-agent-lanzer2006-meta
  - maurer-agent-spycher2008-browser
  - maurer-agent-spycher2008-browser-rest
  - maurer-agent-Q6V0W9
  - maurer-agent-Q9NFF5
- assessment_id: canonical-reference
  area: evidence
  topic: Canonical note combines two genetic studies
  outcome: concern
  target_ids:
  - GO:0020036
  summary: The biological example is supported across the record, but its sole Cooke2006
    reference tests SBP1 deletion and uses MAHRP1 as a marker. The additional MAHRP1
    genetic-test assertion needs the already-listed Spycher2008 source at this claim
    or narrower wording.
  evidence_ids:
  - record
  - maurer-agent-cooke2006-pmc
  - maurer-agent-spycher2008-browser
  - maurer-agent-spycher2008-browser-rest
- assessment_id: functions-graph
  area: graph
  topic: Five descriptive trafficking and boundary edges
  outcome: supported
  target_ids:
  - GO:0020036
  summary: The five NONMECHANISTIC edges and trafficking function are supported. SBP1
    localization is direct; anchoring remains implicated, not a settled mechanism.
    Cooke 3D7 cleft trapping and Spycher MAHRP1 earlier-trafficking defects are distinct.
    No direct cargo binding, vesicle itinerary or universal strain-specific phenotype
    is inferred.
  evidence_ids:
  - record
  - maurer-agent-go
  - maurer-agent-cooke2006-pmc
  - maurer-agent-blisnick2000-meta
  - maurer-agent-lanzer2006-meta
  - maurer-agent-spycher2008-browser
  - maurer-agent-spycher2008-browser-rest
- assessment_id: family-followup
  area: completeness
  topic: Open grounding follow-up
  outcome: unknown
  target_ids:
  - GO:0020036
  summary: The inspected exact queries do not establish an exact class-wide mapping
    for the unrelated resident cohort or SBP1. IPR044661 is retained as a problematic
    broad candidate, not promoted to the maintained component. Optional inventory
    gaps alone are not findings.
  evidence_ids:
  - record
  - maurer-agent-ipr-Q9NFF5
  - maurer-agent-IPR044661
  - maurer-agent-gene-MAHRP1
  - maurer-agent-gene-SBP1
  - maurer-agent-gene-REX1
  - maurer-agent-ipr-Q6V0W9
findings:
- finding_id: F1
  issue_key: maurer-canonical-genetic-study-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Align the canonical genetic-study note with its cited paper
  description: The canonical note attributes genetic testing of both SBP1 and MAHRP1
    to its sole Cooke2006 citation. Cooke tests SBP1 deletion/complementation; the
    MAHRP1 genetic test is in Spycher2008, already listed elsewhere in the record.
  target_ids:
  - GO:0020036
  field_paths:
  - canonical_examples[0].note
  - canonical_examples[0].reference
  evidence_ids:
  - record
  - maurer-agent-cooke2006-pmc
  - maurer-agent-spycher2008-browser
  - maurer-agent-spycher2008-browser-rest
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/maurer_s_cleft.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level evidence placement
  native_severity: minor
  normalization_reason: The species, organelle and genetic findings are supported;
    this is a bounded citation-placement error, not a biological identity or mechanism
    contradiction.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0020036
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/maurer_s_cleft.yaml
    role: maintained scientific record
  description: In separately authorized curation, narrow the Cooke-linked canonical
    note to SBP1 or represent the MAHRP1 clause with the exact Spycher2008 supporting
    source.
  acceptance_checks:
  - Cooke2006 is attached only to its SBP1 intervention and observed phenotype.
  - Any retained MAHRP1 genetic-test clause has Spycher2008 claim-level support; preserve
    correct P. falciparum identity and differing intervention effects.
limitations:
- Lanzer2006 is review-tier and was inspected at complete native abstract level. Blisnick2000
  primary evidence was inspected at complete native abstract level; direct DOI routes
  produced transport-error responses, not usable full bodies.
- Spycher2008 direct native publisher request returned403; genuine browser-displayed
  claim-bearing Results/Discussion were recovered and frozen with status:null, not
  an HTTP200 attestation. Methods after early Western-blotting subsection and figure
  pixels were not inspected.
- No raw microscopy, supplemental FRET/co-immunoprecipitation data, quantitative morphometry
  or full lipid composition was reanalyzed. Negative direct-binding inference is the
  primary Discussion report, not an independent experiment.
- Exact family searches are bounded; a returned broad mediator-family hit is not accepted
  as an exact SBP1-class identity. Optional constituent coverage is incomplete.
- Collective constitutive material, individual formation necessity, trafficking function
  and direct binding remain separate. Unreviewed fragment/strain provenance limits
  accession-specific functional inference.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- Original URL, UTC access and SHA256 are retained. Parent owns finalization.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
