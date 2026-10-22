# Cytostome scientific review

- Review: 20261022T052918Z-cytostome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:15:39Z
- Finished UTC: 2026-10-22T05:29:18Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The bounded T.cruzi cytostome uptake route is supported. One major finding corrects the plasma-membrane relation from is-a to the explicit native part_of relationship.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph and completeness.

Selection: Target 3 of batch49 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031910 | data/structures/other/cytostome.yaml | maintained | cytostome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0031910 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031910 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0031910 | Focused native check passed; identity and biological support assessed independently. |
| Focused native verify | passed | True | GO:0031910 | Focused native check passed; identity and biological support assessed independently. |
| Expression-module applicability | not_applicable | False | GO:0031910 | No maintained expression-module assertion requires this resource. |
| Claim-level scientific review | passed | True | GO:0031910 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031910 | 7 of 8 collected target identifiers returned OK. cellstructuremech:reservosome: SKIPPED; Exact repository-minted identifier has one maintained-record match in the ignored-inclusive search. Its actual referenced record is a frozen input and is explicitly inspected by the linked local evidence; cross-record dependencies are not mistaken for the reviewed target. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031910 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031910 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031910 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031910 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031910 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Cytostome identity and larger complex boundary

identity: concern. Targets: GO:0031910.

GO denotes the ingestion structure; the record deliberately bounds the larger T.cruzi cytostome-cytopharynx complex. Native GO explicitly places cytostome part_of plasma membrane, but the record puts the membrane in its is-a parent list.

### Localized proteins do not settle the opening boundary

grounding: supported. Targets: GO:0031910.

CP1/CP2/CP3 are source-supported localized/associated proteins of the broader complex. Their whole-protein family identities and opening-specific constituent status are not established by the reported broad domains or overexpression patterns; the existing bounded TODO remains appropriate.

### No formation-essentiality inference

grounding: supported. Targets: GO:0031910.

The record has no unsupported molecular essentiality assertions. Native localization, association, uptake inhibition and growth effects do not constitute deletion-based physical assembly necessity for each protein.

### Epimastigote characterization remains within evidence

scope: supported. Targets: GO:0031910.

Alcantara abstract explicitly describes the epimastigote three-dimensional complex. Chasen uses Y-strain epimastigotes and amastigotes; the maintained narrow species/example note does not need expansion to every reported life stage. VARIABLE is compatible with demonstrated developmental differences.

### Endocytic entry with limited cargo scope

evidence: supported. Targets: GO:0031910.

Porto-Carreiro complete native abstract supports cytostome/cytopharynx entry, early endosomal network and subsequent reservosome storage. Chasen protein-feeding experiments reinforce uptake, without proving exclusive uptake for all cargo in all stages.

### Coarse cargo trajectory and exact local destination

graph: supported. Targets: GO:0031910.

The three edges summarize entry, intermediate passage and accumulation with the source transport route. They do not claim timing, required universal intermediates or molecular interactions. The local reservosome identifier resolves to the correct destination record.

### Correct the relation before optional molecular expansion

completeness: concern. Targets: GO:0031910.

The hierarchy error is directly actionable. Wider cytopharynx boundaries and protein groundings remain explicitly unresolved, with primary opening-versus-tubule evidence required before adding components.

## Findings

### F1: Represent plasma-membrane parthood instead of an is-a parent

major / open / confirmed; issue key: cytostome-plasma-membrane-parthood.

parent_structures currently contains GO:0005886 plasma membrane. Repository semantics make this an is-a assertion, meaning the cytostome is itself a plasma membrane. Native GO instead explicitly exposes GO:0031910 as a part_of child of GO:0005886. The specialized ingestion structure is part of the membrane, not a membrane subtype.

## Recommended Actions And Acceptance Checks

### A1

Remove the plasma-membrane is-a assertion and express the verified relation through part_of, retaining exact cytostome identity and the separately discussed broader cytostome-cytopharynx boundary.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/cytostome.yaml; Entire maintained record including history, components, evidence, graph and discussions | context_only | All maintained fields were read. Historical curation notes document earlier decisions rather than independently proving current assertions. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component grounding, formation essentiality, taxonomic presence and graph scope | context_only | Whole-protein families differ from domains and individual examples. Assembly necessity differs from viability or function. COMMON means present in most members, with losses the exception; a qualitative ordinary-machinery assertion need not imply a numerical census. |
| curation | docs/CURATION.md; Exact identities and claim-specific evidence | context_only | A verified component identity and its membership in a complex require distinct support. Reviewed label-only status is reserved for the absence of an exact term; historical deferred searches can be revisited without alleging historical fabrication. |
| root49-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005737,GO:0005886,GO:0031461,GO:0031910,GO:0032258,GO:0032991,GO:0033107,GO:0034270; Complete maintained-term identity and definition fields and relevant typed links; not every descendant | supports | All eight requested native GO identities, active status, definitions, synonyms, comments and relevant typed links inspected. The cytostome is explicitly a part_of child of plasma membrane, while the Cvt pathway definition includes Atg19 in formation of the Cvt complex. |
| root49-sources-doi-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1006%2Fexpr.1999.4419%22&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED10425150: The cytostome of Trypanosoma cruzi epimastigotes is associated with the flagellar complex. DOI 10.1006/expr.1999.4419. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root49-sources-doi-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1078%2F0171-9335-00112%22&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED11139150: Trypanosoma cruzi epimastigote endocytic pathway: cargo enters the cytostome and passes through an early endosomal network before storage in reservosomes. DOI 10.1078/0171-9335-00112. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root49-sources-doi-6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1242%2Fjcs.135491%22&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED24610945: The three-dimensional structure of the cytostome-cytopharynx complex of Trypanosoma cruzi epimastigotes. DOI 10.1242/jcs.135491. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root49-sources-doi-8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.3389%2Ffcimb.2019.00445%22&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED32010635: Identification and Localization of the First Known Proteins of the &lt;i&gt;Trypanosoma cruzi&lt;/i&gt; Cytostome Cytopharynx Endocytic Complex. DOI 10.3389/fcimb.2019.00445. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root49-sources-tax5693 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5693; Complete native taxonomy response | supports | Native taxon 5693 name, rank, lineage and synonym data inspected. Reference strains are distinguished from experimental strains. |
| reservosome | data/structures/membrane_organelle/reservosome.yaml; Identifier, label, definition and endocytosed-cargo dependency fields | context_only | The exact local identifier resolves to the posterior membrane-bounded endocytic organelle that receives internalized macromolecular cargo; this dependency inspection is not a new review of that record. |
| root49-sources-chasen2020-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC6978632/?report=xml; Complete Results sec15-sec18 with Fig1-4 captions, Discussion s6, Methods sec3/sec5/sec6/sec9 and s3 co-IP/mass spectrometry; no figure pixels or supplementary reanalysis | supports | Endogenous CP1 tagging and immunoelectron microscopy, protein-feeding assays and CP1-associated CP2/CP3 overexpression localize proteins across the cytostome-cytopharynx complex. CP1/CP2 have predicted SMC/coiled-coil regions, not exact established whole-protein family identities. Localization and co-isolation do not define a universal three-subunit cytostome-opening assembly or necessity for uptake. |
| schema-result | just validate data/structures/other/cytostome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/cytostome.yaml |
| strict-result | just validate-strict data/structures/other/cytostome.yaml --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/cytostome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/cytostome.yaml --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/cytostome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch49-20261022-3rpodnkz/cytostome-strict.tsv |
| native-cytostome-causal-graphs | /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cytostome.yaml; Complete focused native report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| native-cytostome-verify | /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/cytostome.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/cytostome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 7 of 8 collected target identifiers returned OK. cellstructuremech:reservosome: SKIPPED; Exact repository-minted identifier has one maintained-record match in the ignored-inclusive search. Its actual referenced record is a frozen input and is explicitly inspected by the linked local evidence; cross-record dependencies are not mistaken for the reviewed target. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Primary reading is limited to the explicitly recorded sections, captions and datasets; no raw spectra or sequence alignments were reanalyzed.
- Okuda1999, Porto-Carreiro2000 and Alcantara2014 were inspected at complete native metadata/abstract tier only. The JCS403 and Porto TLS routes are preserved as failed access attempts; no primary body, tomography pixels or detailed kinetic reanalysis from those papers is claimed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes all uncovered reviews, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T052918Z-cytostome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cytostome scientific review
started_at: '2026-10-22T05:15:39Z'
finished_at: '2026-10-22T05:29:18Z'
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
summary: The bounded T.cruzi cytostome uptake route is supported. One major finding
  corrects the plasma-membrane relation from is-a to the explicit native part_of relationship.
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
  - path: data/structures/membrane_organelle/reservosome.yaml
    sha256: 0e733e8adbe97aaadfaaa43aafd271069aaa3fb14cad36f8c3281b31852e7aeb
    role: context
  - path: data/structures/other/cytostome.yaml
    sha256: e098724aea296245130198ea537eab00b38dd2429c7d91aeac78d09efab7d735
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
- target_id: GO:0031910
  path: data/structures/other/cytostome.yaml
  label: cytostome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cytostome.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph and completeness.
  selection: Target 3 of batch49 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031910
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: just validate data/structures/other/cytostome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: just validate-strict data/structures/other/cytostome.yaml --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/cytostome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-cytostome-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cytostome.yaml
  exit_code: 0
  summary: Focused native check passed; identity and biological support assessed independently.
  evidence_ids:
  - native-cytostome-causal-graphs
- check_id: native-cytostome-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/cytostome.yaml
  exit_code: 0
  summary: Focused native check passed; identity and biological support assessed independently.
  evidence_ids:
  - native-cytostome-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0031910
  summary: No maintained expression-module assertion requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0031910
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root49-sources-go
  - root49-sources-doi-1
  - root49-sources-doi-5
  - root49-sources-doi-6
  - root49-sources-doi-8
  - root49-sources-tax5693
  - reservosome
  - root49-sources-chasen2020-legacy
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031910
  summary: '7 of 8 collected target identifiers returned OK. cellstructuremech:reservosome:
    SKIPPED; Exact repository-minted identifier has one maintained-record match in
    the ignored-inclusive search. Its actual referenced record is a frozen input and
    is explicitly inspected by the linked local evidence; cross-record dependencies
    are not mistaken for the reviewed target. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - reservosome
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0031910
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
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/cytostome.yaml
  locator: Entire maintained record including history, components, evidence, graph
    and discussions
  accessed_at: '2026-10-22T05:26:44Z'
  support: context_only
  summary: All maintained fields were read. Historical curation notes document earlier
    decisions rather than independently proving current assertions.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component grounding, formation essentiality, taxonomic presence and graph
    scope
  accessed_at: '2026-10-22T05:26:44Z'
  support: context_only
  summary: Whole-protein families differ from domains and individual examples. Assembly
    necessity differs from viability or function. COMMON means present in most members,
    with losses the exception; a qualitative ordinary-machinery assertion need not
    imply a numerical census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identities and claim-specific evidence
  accessed_at: '2026-10-22T05:26:44Z'
  support: context_only
  summary: A verified component identity and its membership in a complex require distinct
    support. Reviewed label-only status is reserved for the absence of an exact term;
    historical deferred searches can be revisited without alleging historical fabrication.
- evidence_id: root49-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005737,GO:0005886,GO:0031461,GO:0031910,GO:0032258,GO:0032991,GO:0033107,GO:0034270
  locator: Complete maintained-term identity and definition fields and relevant typed
    links; not every descendant
  accessed_at: '2026-10-22T05:16:37.461732Z'
  support: supports
  summary: All eight requested native GO identities, active status, definitions, synonyms,
    comments and relevant typed links inspected. The cytostome is explicitly a part_of
    child of plasma membrane, while the Cvt pathway definition includes Atg19 in formation
    of the Cvt complex.
  snapshot_sha256: d24e5122fae367cf9a2d8fb7c6570ebcb8f08890d0147e4ae81b987297a086a9
- evidence_id: root49-sources-doi-1
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1006%2Fexpr.1999.4419%22&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:16:40.167154Z'
  support: supports
  summary: 'MED10425150: The cytostome of Trypanosoma cruzi epimastigotes is associated
    with the flagellar complex. DOI 10.1006/expr.1999.4419. Complete bibliographic
    identity and abstract inspected; full-body access is certified only in separate
    evidence rows.'
  snapshot_sha256: 962c7a2219b2600356f1e4416430b30d48dfaebda97ebcfe70f28b25fbbacf22
- evidence_id: root49-sources-doi-5
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1078%2F0171-9335-00112%22&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:16:41.129754Z'
  support: supports
  summary: 'MED11139150: Trypanosoma cruzi epimastigote endocytic pathway: cargo enters
    the cytostome and passes through an early endosomal network before storage in
    reservosomes. DOI 10.1078/0171-9335-00112. Complete bibliographic identity and
    abstract inspected; full-body access is certified only in separate evidence rows.'
  snapshot_sha256: 471a381dd60a54bed5d6a5e5e925aac4cf14d83489b0e01578ed4f5a64164bb5
- evidence_id: root49-sources-doi-6
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1242%2Fjcs.135491%22&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:16:41.410863Z'
  support: supports
  summary: 'MED24610945: The three-dimensional structure of the cytostome-cytopharynx
    complex of Trypanosoma cruzi epimastigotes. DOI 10.1242/jcs.135491. Complete bibliographic
    identity and abstract inspected; full-body access is certified only in separate
    evidence rows.'
  snapshot_sha256: b46de2cdfd08da0725dd224f3cd81c034bda7ebd04a74913cc58522a29b50e04
- evidence_id: root49-sources-doi-8
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.3389%2Ffcimb.2019.00445%22&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:16:41.805479Z'
  support: supports
  summary: 'MED32010635: Identification and Localization of the First Known Proteins
    of the <i>Trypanosoma cruzi</i> Cytostome Cytopharynx Endocytic Complex. DOI 10.3389/fcimb.2019.00445.
    Complete bibliographic identity and abstract inspected; full-body access is certified
    only in separate evidence rows.'
  snapshot_sha256: c52cc10e198aa2b1e3e6abd27e2eb210314e99b1f955171f9cbfd1d167c15dac
- evidence_id: root49-sources-tax5693
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5693
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:16:38.289696Z'
  support: supports
  summary: Native taxon 5693 name, rank, lineage and synonym data inspected. Reference
    strains are distinguished from experimental strains.
  snapshot_sha256: 29ca5f9c41995471a462d22be4406f02aa99f2f23760f2ea91ac33282f22482f
- evidence_id: reservosome
  kind: record_content
  reference: data/structures/membrane_organelle/reservosome.yaml
  locator: Identifier, label, definition and endocytosed-cargo dependency fields
  accessed_at: '2026-10-22T05:26:44Z'
  support: context_only
  summary: The exact local identifier resolves to the posterior membrane-bounded endocytic
    organelle that receives internalized macromolecular cargo; this dependency inspection
    is not a new review of that record.
- evidence_id: root49-sources-chasen2020-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6978632/?report=xml
  locator: Complete Results sec15-sec18 with Fig1-4 captions, Discussion s6, Methods
    sec3/sec5/sec6/sec9 and s3 co-IP/mass spectrometry; no figure pixels or supplementary
    reanalysis
  accessed_at: '2026-10-22T05:18:32.168563Z'
  support: supports
  summary: Endogenous CP1 tagging and immunoelectron microscopy, protein-feeding assays
    and CP1-associated CP2/CP3 overexpression localize proteins across the cytostome-cytopharynx
    complex. CP1/CP2 have predicted SMC/coiled-coil regions, not exact established
    whole-protein family identities. Localization and co-isolation do not define a
    universal three-subunit cytostome-opening assembly or necessity for uptake.
  snapshot_sha256: 7399c98e552de532441d65c524b8ce5b81c6ae92bbb7bd26c6203f274a0cc432
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/cytostome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:15:40Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/cytostome.yaml'
  snapshot_sha256: dd3beabf19ac30d4a1abb11b867f04325329dc7413b3bbbd05f8f17844b0aa7d
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/cytostome.yaml --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/cytostome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:15:41Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/cytostome.yaml\
    \ --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/cytostome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch49-20261022-3rpodnkz/cytostome-strict.tsv"
  snapshot_sha256: b7e5faf6f5772d4802c5d8b11b82cbda22798a4f85ec05ee467970f14d9057c8
- evidence_id: native-cytostome-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cytostome.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:20:55.179966Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: native-cytostome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/cytostome.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:20:55.609912Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/cytostome.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '7 of 8 collected target identifiers returned OK. cellstructuremech:reservosome:
    SKIPPED; Exact repository-minted identifier has one maintained-record match in
    the ignored-inclusive search. Its actual referenced record is a frozen input and
    is explicitly inspected by the linked local evidence; cross-record dependencies
    are not mistaken for the reviewed target. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
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
  topic: Cytostome identity and larger complex boundary
  outcome: concern
  target_ids:
  - GO:0031910
  summary: GO denotes the ingestion structure; the record deliberately bounds the
    larger T.cruzi cytostome-cytopharynx complex. Native GO explicitly places cytostome
    part_of plasma membrane, but the record puts the membrane in its is-a parent list.
  evidence_ids:
  - record
  - schema
  - root49-sources-go
  - root49-sources-doi-1
  - root49-sources-doi-5
  - root49-sources-doi-6
  - root49-sources-doi-8
- assessment_id: composition
  area: grounding
  topic: Localized proteins do not settle the opening boundary
  outcome: supported
  target_ids:
  - GO:0031910
  summary: CP1/CP2/CP3 are source-supported localized/associated proteins of the broader
    complex. Their whole-protein family identities and opening-specific constituent
    status are not established by the reported broad domains or overexpression patterns;
    the existing bounded TODO remains appropriate.
  evidence_ids:
  - record
  - curation
  - root49-sources-chasen2020-legacy
- assessment_id: necessity
  area: grounding
  topic: No formation-essentiality inference
  outcome: supported
  target_ids:
  - GO:0031910
  summary: The record has no unsupported molecular essentiality assertions. Native
    localization, association, uptake inhibition and growth effects do not constitute
    deletion-based physical assembly necessity for each protein.
  evidence_ids:
  - record
  - schema
  - root49-sources-chasen2020-legacy
- assessment_id: scope
  area: scope
  topic: Epimastigote characterization remains within evidence
  outcome: supported
  target_ids:
  - GO:0031910
  summary: Alcantara abstract explicitly describes the epimastigote three-dimensional
    complex. Chasen uses Y-strain epimastigotes and amastigotes; the maintained narrow
    species/example note does not need expansion to every reported life stage. VARIABLE
    is compatible with demonstrated developmental differences.
  evidence_ids:
  - record
  - root49-sources-chasen2020-legacy
  - root49-sources-doi-1
  - root49-sources-doi-5
  - root49-sources-doi-6
  - root49-sources-doi-8
  - root49-sources-tax5693
- assessment_id: functions
  area: evidence
  topic: Endocytic entry with limited cargo scope
  outcome: supported
  target_ids:
  - GO:0031910
  summary: Porto-Carreiro complete native abstract supports cytostome/cytopharynx
    entry, early endosomal network and subsequent reservosome storage. Chasen protein-feeding
    experiments reinforce uptake, without proving exclusive uptake for all cargo in
    all stages.
  evidence_ids:
  - record
  - root49-sources-chasen2020-legacy
  - root49-sources-doi-1
  - root49-sources-doi-5
  - root49-sources-doi-6
  - root49-sources-doi-8
- assessment_id: graph
  area: graph
  topic: Coarse cargo trajectory and exact local destination
  outcome: supported
  target_ids:
  - GO:0031910
  summary: The three edges summarize entry, intermediate passage and accumulation
    with the source transport route. They do not claim timing, required universal
    intermediates or molecular interactions. The local reservosome identifier resolves
    to the correct destination record.
  evidence_ids:
  - record
  - reservosome
  - root49-sources-doi-1
  - root49-sources-doi-5
  - root49-sources-doi-6
  - root49-sources-doi-8
- assessment_id: coverage
  area: completeness
  topic: Correct the relation before optional molecular expansion
  outcome: concern
  target_ids:
  - GO:0031910
  summary: The hierarchy error is directly actionable. Wider cytopharynx boundaries
    and protein groundings remain explicitly unresolved, with primary opening-versus-tubule
    evidence required before adding components.
  evidence_ids:
  - record
  - schema
  - root49-sources-go
  - root49-sources-chasen2020-legacy
findings:
- finding_id: F1
  issue_key: cytostome-plasma-membrane-parthood
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Represent plasma-membrane parthood instead of an is-a parent
  description: parent_structures currently contains GO:0005886 plasma membrane. Repository
    semantics make this an is-a assertion, meaning the cytostome is itself a plasma
    membrane. Native GO instead explicitly exposes GO:0031910 as a part_of child of
    GO:0005886. The specialized ingestion structure is part of the membrane, not a
    membrane subtype.
  target_ids:
  - GO:0031910
  field_paths:
  - parent_structures
  - part_of
  evidence_ids:
  - record
  - schema
  - root49-sources-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cytostome.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: major
  normalization_reason: The asserted molecular identity, structural boundary or typed
    hierarchy is materially incorrect, rather than an optional enrichment.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0031910
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cytostome.yaml
    role: maintained scientific record
  description: Remove the plasma-membrane is-a assertion and express the verified
    relation through part_of, retaining exact cytostome identity and the separately
    discussed broader cytostome-cytopharynx boundary.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Primary reading is limited to the explicitly recorded sections, captions and datasets;
  no raw spectra or sequence alignments were reanalyzed.
- Okuda1999, Porto-Carreiro2000 and Alcantara2014 were inspected at complete native
  metadata/abstract tier only. The JCS403 and Porto TLS routes are preserved as failed
  access attempts; no primary body, tomography pixels or detailed kinetic reanalysis
  from those papers is claimed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorizes all uncovered reviews, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
