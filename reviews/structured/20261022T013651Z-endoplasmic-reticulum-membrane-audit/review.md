# Endoplasmic reticulum membrane identity, source and compartment review

- Review: 20261022T013651Z-endoplasmic-reticulum-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:09:13Z
- Finished UTC: 2026-10-22T01:36:51Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed in the endoplasmic reticulum membrane record within the explicitly documented source scopes.

## Scope And Provenance

Entire single maintained target; exact identity, hierarchy, component/protein scope, organism contexts, cited evidence and every graph edge.

Selection: Target 9 of batch twenty-seven; strict uncovered path order on fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005789 | data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml | maintained | endoplasmic reticulum membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native verify | passed | True | GO:0005789 | The focused native identity/coverage check passed; it does not by itself establish biological membership. |
| Focused native causal-graphs | passed | True | GO:0005789 | The focused native identity/coverage check passed; it does not by itself establish biological membership. |
| Focused native schema | passed | True | GO:0005789 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005789 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005789 | Native UniProt is used as the structured protein adapter. No iModulon dataset or expression-module inference is needed to assess these cited physical/functional experiments; UPR evidence is kept at the primary paper scope. |
| Claim-level scientific review | passed | True | GO:0005789 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005789 | 9 of 11 collected target identifiers returned OK. PMID:8004676: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID8004676, DOI10.1016/0092-8674(94)90138-4 and COPII: a membrane coat formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections.; PMID:9568718: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID9568718, DOI10.1016/s0092-8674(00)81577-9 and COPII-coated vesicle formation reconstituted with purified coat proteins and chemically defined liposomes. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005789 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005789 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005789 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005789 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005789 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### ER, membrane and lumen distinctions

identity: supported. Targets: GO:0005789.

The target exact GO definition and stated kind denote the ER-bounding lipid bilayer. The exact ER synonym is native. The broader membrane parent is supported by the definitions; the returned list is not claimed to contain an unavailable direct edge. Membrane, lumen and Sec61 topology remains distinct.

### Budding yeast model and experimental scope

scope: supported. Targets: GO:0005789.

The species4932 identity is exact. COMMON is qualitative occurrence rather than a numerical survey. The distribution note is limited to COPII budding from yeast ER; the Sec61 example is separately supported. Stirling Table1 names multiple backgrounds and mutant contexts; the review does not silently assign all experiments to one sequenced reference strain.

### Constituent bilayer and optional molecular repertoire

grounding: supported. Targets: GO:0005789.

The LIPID row is a collective boundary material, not one identified chemical species. REVIEWED_LABEL_ONLY and the open lipid-grounding discussion distinguish constituent material from the whole-membrane class. No exhaustive absence of molecular identifiers or full composition inventory is asserted.

### Formation necessity versus protein/cell function

evidence: unknown. Targets: GO:0005789.

Collective membrane constitution supports the defining bilayer row. No individual lipid-species necessity is demonstrated. COPII reconstitution conditions are not a test of ER-organelle formation.

### ER donor context and fresh COPII edge

evidence: supported. Targets: GO:0005789.

GO0090114 defines ER evagination, GO0030127 supplies yeast coat identity, Barlowe supports washed-ER budding, and Matsuoka supports sequential assembly on ER membranes and defined liposomes. The newly added coat-mediates-budding edge states this coarse supported process. The artificial membrane assay is not silently equated with complete in-vivo lipid composition.

### Every descriptive ER edge

graph: supported. Targets: GO:0005789.

All five NONMECHANISTIC edges preserve membrane parthood/enclosure, Sec61 embedding, coat assembly and COPII budding. The fresh fifth edge is supported at the coarse process scope by GO and the cited primary abstracts; no recruitment kinetics or exact cellular lipid requirement is added.

### Full target and honest optional gaps

completeness: supported. Targets: GO:0005789.

All target fields and edges were read. The target asserts no images, physical measurements, trait links or verbatim snippets. Open molecular inventories remain explicit optional gaps; source-access limits do not become invented defects. PROPOSED status and append-only historical decisions are preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml; Entire maintained target including history, component and protein examples, all evidence and graph edges, discussions | context_only | All target bytes were read. Scientific content, status and histories remain unchanged. |
| policy | docs/CURATION.md; Structure identity, is-a versus parthood, constituent versus associated machinery, narrow evidence | context_only | The whole organelle, limiting membrane and enclosed region remain distinct. Enzyme activity and gene viability do not establish organelle-formation necessity. |
| protein-contract | src/cellstructuremech/schema/cellstructuremech.yaml; Component.protein_examples and ProteinExample lines448–468; component essentiality contract | context_only | Protein examples require paired biological context; native accession verification alone is not proof of structure membership. Formation necessity differs from protein function and cell viability. |
| neighbor-endoplasmic_reticulum | data/structures/membrane_organelle/endoplasmic_reticulum.yaml; Entire neighboring record read, used solely for compartment boundary context | context_only | These neighboring records receive separate reviews. Their unrelated source claims are not incorporated as proof for this target. |
| neighbor-endoplasmic_reticulum_lumen | data/structures/membrane_organelle/endoplasmic_reticulum_lumen.yaml; Entire neighboring record read, used solely for compartment boundary context | context_only | These neighboring records receive separate reviews. Their unrelated source claims are not incorporated as proof for this target. |
| neighbor-endosome | data/structures/membrane_organelle/endosome.yaml; Entire neighboring record read, used solely for compartment boundary context | context_only | These neighboring records receive separate reviews. Their unrelated source claims are not incorporated as proof for this target. |
| root27-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005788,GO:0005789,GO:0005784,GO:0043231,GO:0012505,GO:0043233,GO:0016020,GO:0030968,GO:0036503,GO:0090114,GO:0030127,GO:0005768,GO:0010008,GO:0031904,GO:0005771,GO:0016197,GO:0000813,GO:0000814,GO:0000815; All20 identifiers, active flags, names, definitions, synonyms, comments and returned immediate child relations | supports | Twenty active GO terms were read in full. Exact ER/endosome, membrane/lumen, Sec61, ESCRT, transport and COPII definitions and synonyms support the scoped identities. GO0005784 explicitly names the yeast Sec61p/Sbh1p/Sss1p core. GO0036503 is now named ERAD quality control pathway, with ERAD pathway retained as a broad synonym; the record description specifically identifies misfolded-protein quality control. Returned child links support direct relations only; broader membrane/lumen classes may require transitive or definition-based inference. |
| root27-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and alternate names | supports | ENA identifies Saccharomyces cerevisiae at species4932; its rank and fungal lineage agree with the target. This does not certify any particular experimental strain or numerical prevalence. |
| root27-sources-stirling1992-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.3.2.129; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies Protein translocation mutants defective in the insertion of integral membrane proteins into the endoplasmic reticulum. by Stirling CJ, Rothblatt J, Hosobuchi M, Deshaies R, Schekman R.; PMID1550957, DOI10.1091/mbc.3.2.129. The complete primary abstract distinguishes old substrate-selective sec alleles from newly selected restrictive sec61/sec65 mutants, and reports Sec61 membrane localization. It supports yeast protein insertion and translocation, not a complete modern translocon structure or organelle-formation knockout. |
| root27-sources-barlowe1994-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8004676%20AND%20SRC%3AMED; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies COPII: a membrane coat formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum. by Barlowe C, Orci L, Yeung T, Hosobuchi M, Hamamoto S, Salama N, Rexach MF, Ravazzola M, Amherdt M, Schekman R.; PMID8004676, DOI10.1016/0092-8674(94)90138-4. The complete primary abstract reports budding from washed ER membranes using Sar1 and Sec13/Sec23 complexes; GTP versus GMP-PNP affects targeting/fusion. It supports the ER donor and COPII coat context, not every cellular lipid requirement. |
| root27-sources-matsuoka1998-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9568718%20AND%20SRC%3AMED; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies COPII-coated vesicle formation reconstituted with purified coat proteins and chemically defined liposomes. by Matsuoka K, Orci L, Amherdt M, Bednarek SY, Hamamoto S, Schekman R, Yeung T.; PMID9568718, DOI10.1016/s0092-8674(00)81577-9. The complete primary abstract directly describes purified Sar1, Sec23/24 and Sec13/31 recruitment to defined liposomes and ER membranes, phosphoinositide dependence in that assay and coated buds/vesicles. Artificial-liposome sufficiency is not a complete in-vivo ER composition inventory. |
| root27-sources-stirling1992-page129 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/f89735edf303/mbc00060-0006.png; Original primary page129 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | Title, full abstract and opening Introduction inspected directly in the original scan; old substrate-selective mutants are distinguished from newly restrictive sec61/sec65 alleles. |
| root27-sources-stirling1992-page130 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/55f33db3a3fc/mbc00060-0007.png; Original primary page130 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | Complete Table1 and Introduction continuation read; the experimental strains are explicitly named and not assumed to be the reference S288C accession strain. The strain/media paragraph and opening methods are read; subsequent methods are outside this scan scope. |
| root27-sources-stirling1992-page137 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/b76f0a0c7375/mbc00060-0014.png; Original primary page137 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | The SEC61 coding/viability Results are read. Lethality of the sec61 null and mutation effects establish protein/cell function, not proof that the ER organelle cannot form. |
| root27-sources-stirling1992-page138 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/a2683aa00787/mbc00060-0015.png; Original primary page138 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | The Identification and Localization of Sec61p Results begin here; antiserum and fractionation analysis are read. Fig6 and its caption are visible but the nucleotide sequence is not independently reannotated. |
| root27-sources-stirling1992-page139 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/694d066200ac/mbc00060-0016.png; Original primary page139 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | Localization Results conclude: Sec61p is solubilized by Triton, fractionates with ER material, and shows ER-pattern immunofluorescence. Fig7/caption and the beginning of Discussion were viewed; hydropathy predictions are not modern structure validation. |
| root27-sources-stirling1992-page140 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/8f3b5e3aa4a2/mbc00060-0017.png; Original primary page140 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | Complete Fig8 and caption and continuing Discussion read: the original fractionation/blot supports integral ER membrane localization, with different strains/conditions specified. Densities are not quantified; later Discussion is outside this scope. |
| native-verify | /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml --verify; Entire focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml --causal-graphs; Entire focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 11 collected target identifiers returned OK. PMID:8004676: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID8004676, DOI10.1016/0092-8674(94)90138-4 and COPII: a membrane coat formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections.; PMID:9568718: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID9568718, DOI10.1016/s0092-8674(00)81577-9 and COPII-coated vesicle formation reconstituted with purified coat proteins and chemically defined liposomes. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Native ontology terms, taxonomy and proteins were read directly; definitions and transitive parentage do not imply an unavailable direct ontology edge. Individual molecular formation necessity and exhaustive composition remain unknown.
- Primary access is bounded: Stirling original scans129,130,137–140 were read; other pages were not. Barlowe/Matsuoka are complete-abstract only; publisher retrieval failed. No full-body or quantitative lipid audit is claimed.
- Species scope and reference-strain accessions do not identify every primary experimental strain. Historical authorship, previous searches and prior review dispositions are not independently recertified.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User explicitly authorizes a bundle for every uncovered target, including honest no-finding reviews. No scientific record edit is authorized.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T013651Z-endoplasmic-reticulum-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Endoplasmic reticulum membrane identity, source and compartment review
started_at: '2026-10-22T01:09:13Z'
finished_at: '2026-10-22T01:36:51Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: No concrete curation defect observed in the endoplasmic reticulum membrane
  record within the explicitly documented source scopes.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    sha256: 7444c8cf7718146040d73012227215c8767122fa1bd1988e2b66e8278c6dcb2f
    role: context
  - path: data/structures/membrane_organelle/endoplasmic_reticulum_lumen.yaml
    sha256: 8ffe704fef493506e494107aba2b583e563921f2f12a6e98748971f64976b622
    role: context
  - path: data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    sha256: 599774aca4e215829787fe1a818ef52bd2c3772b48c289505d14417c05d0f679
    role: target
  - path: data/structures/membrane_organelle/endosome.yaml
    sha256: 7eb3c5b8022e63698365a49990831c7609d649c6024002eb19f6a28cdfff38a8
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
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0005789
  path: data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
  label: endoplasmic reticulum membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target; exact identity, hierarchy, component/protein
    scope, organism contexts, cited evidence and every graph edge.
  selection: Target 9 of batch twenty-seven; strict uncovered path order on fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005789
checks:
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0005789
  command: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    --verify
  exit_code: 0
  summary: The focused native identity/coverage check passed; it does not by itself
    establish biological membership.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005789
  command: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: The focused native identity/coverage check passed; it does not by itself
    establish biological membership.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005789
  command: just validate data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005789
  command: just validate-strict data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005789
  summary: Native UniProt is used as the structured protein adapter. No iModulon dataset
    or expression-module inference is needed to assess these cited physical/functional
    experiments; UPR evidence is kept at the primary paper scope.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005789
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - protein-contract
  - neighbor-endoplasmic_reticulum
  - neighbor-endoplasmic_reticulum_lumen
  - neighbor-endosome
  - root27-sources-go
  - root27-sources-tax4932
  - root27-sources-stirling1992-meta
  - root27-sources-barlowe1994-meta
  - root27-sources-matsuoka1998-meta
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005789
  summary: '9 of 11 collected target identifiers returned OK. PMID:8004676: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID8004676, DOI10.1016/0092-8674(94)90138-4 and COPII: a membrane coat
    formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum.
    Bibliographic identity is resolved; scientific scope remains restricted to the
    separately documented abstract/body inspections.; PMID:9568718: UNREACHABLE; The
    bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID9568718, DOI10.1016/s0092-8674(00)81577-9 and COPII-coated vesicle
    formation reconstituted with purified coat proteins and chemically defined liposomes.
    Bibliographic identity is resolved; scientific scope remains restricted to the
    separately documented abstract/body inspections. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root27-sources-barlowe1994-meta
  - root27-sources-matsuoka1998-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005789
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005789
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005789
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005789
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005789
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
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
  locator: Entire maintained target including history, component and protein examples,
    all evidence and graph edges, discussions
  accessed_at: '2026-10-22T01:16:43Z'
  support: context_only
  summary: All target bytes were read. Scientific content, status and histories remain
    unchanged.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Structure identity, is-a versus parthood, constituent versus associated
    machinery, narrow evidence
  accessed_at: '2026-10-22T01:16:43Z'
  support: context_only
  summary: The whole organelle, limiting membrane and enclosed region remain distinct.
    Enzyme activity and gene viability do not establish organelle-formation necessity.
- evidence_id: protein-contract
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component.protein_examples and ProteinExample lines448–468; component essentiality
    contract
  accessed_at: '2026-10-22T01:16:43Z'
  support: context_only
  summary: Protein examples require paired biological context; native accession verification
    alone is not proof of structure membership. Formation necessity differs from protein
    function and cell viability.
- evidence_id: neighbor-endoplasmic_reticulum
  kind: record_content
  reference: data/structures/membrane_organelle/endoplasmic_reticulum.yaml
  locator: Entire neighboring record read, used solely for compartment boundary context
  accessed_at: '2026-10-22T01:16:43Z'
  support: context_only
  summary: These neighboring records receive separate reviews. Their unrelated source
    claims are not incorporated as proof for this target.
- evidence_id: neighbor-endoplasmic_reticulum_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/endoplasmic_reticulum_lumen.yaml
  locator: Entire neighboring record read, used solely for compartment boundary context
  accessed_at: '2026-10-22T01:16:43Z'
  support: context_only
  summary: These neighboring records receive separate reviews. Their unrelated source
    claims are not incorporated as proof for this target.
- evidence_id: neighbor-endosome
  kind: record_content
  reference: data/structures/membrane_organelle/endosome.yaml
  locator: Entire neighboring record read, used solely for compartment boundary context
  accessed_at: '2026-10-22T01:16:43Z'
  support: context_only
  summary: These neighboring records receive separate reviews. Their unrelated source
    claims are not incorporated as proof for this target.
- evidence_id: root27-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005788,GO:0005789,GO:0005784,GO:0043231,GO:0012505,GO:0043233,GO:0016020,GO:0030968,GO:0036503,GO:0090114,GO:0030127,GO:0005768,GO:0010008,GO:0031904,GO:0005771,GO:0016197,GO:0000813,GO:0000814,GO:0000815
  locator: All20 identifiers, active flags, names, definitions, synonyms, comments
    and returned immediate child relations
  accessed_at: '2026-10-22T01:10:57.099012Z'
  support: supports
  summary: Twenty active GO terms were read in full. Exact ER/endosome, membrane/lumen,
    Sec61, ESCRT, transport and COPII definitions and synonyms support the scoped
    identities. GO0005784 explicitly names the yeast Sec61p/Sbh1p/Sss1p core. GO0036503
    is now named ERAD quality control pathway, with ERAD pathway retained as a broad
    synonym; the record description specifically identifies misfolded-protein quality
    control. Returned child links support direct relations only; broader membrane/lumen
    classes may require transitive or definition-based inference.
  snapshot_sha256: ea021845778f0e54effaf639a0ab1d071361b49a8060eac188ad56277eae8350
- evidence_id: root27-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-10-22T01:10:58.502766Z'
  support: supports
  summary: ENA identifies Saccharomyces cerevisiae at species4932; its rank and fungal
    lineage agree with the target. This does not certify any particular experimental
    strain or numerical prevalence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root27-sources-stirling1992-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.3.2.129
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:10:57.099383Z'
  support: supports
  summary: Native MED identifies Protein translocation mutants defective in the insertion
    of integral membrane proteins into the endoplasmic reticulum. by Stirling CJ,
    Rothblatt J, Hosobuchi M, Deshaies R, Schekman R.; PMID1550957, DOI10.1091/mbc.3.2.129.
    The complete primary abstract distinguishes old substrate-selective sec alleles
    from newly selected restrictive sec61/sec65 mutants, and reports Sec61 membrane
    localization. It supports yeast protein insertion and translocation, not a complete
    modern translocon structure or organelle-formation knockout.
  snapshot_sha256: bc349d2da602b21d01dd29d83db504f59222406f3393a8dea8054d3fc4f848ba
- evidence_id: root27-sources-barlowe1994-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8004676%20AND%20SRC%3AMED
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:10:57.099755Z'
  support: supports
  summary: 'Native MED identifies COPII: a membrane coat formed by Sec proteins that
    drive vesicle budding from the endoplasmic reticulum. by Barlowe C, Orci L, Yeung
    T, Hosobuchi M, Hamamoto S, Salama N, Rexach MF, Ravazzola M, Amherdt M, Schekman
    R.; PMID8004676, DOI10.1016/0092-8674(94)90138-4. The complete primary abstract
    reports budding from washed ER membranes using Sar1 and Sec13/Sec23 complexes;
    GTP versus GMP-PNP affects targeting/fusion. It supports the ER donor and COPII
    coat context, not every cellular lipid requirement.'
  snapshot_sha256: f3ff438cc130518602efe6aa0252c6d5634fafad949d62cf23e3a6e837819fc7
- evidence_id: root27-sources-matsuoka1998-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9568718%20AND%20SRC%3AMED
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:10:57.832309Z'
  support: supports
  summary: Native MED identifies COPII-coated vesicle formation reconstituted with
    purified coat proteins and chemically defined liposomes. by Matsuoka K, Orci L,
    Amherdt M, Bednarek SY, Hamamoto S, Schekman R, Yeung T.; PMID9568718, DOI10.1016/s0092-8674(00)81577-9.
    The complete primary abstract directly describes purified Sar1, Sec23/24 and Sec13/31
    recruitment to defined liposomes and ER membranes, phosphoinositide dependence
    in that assay and coated buds/vesicles. Artificial-liposome sufficiency is not
    a complete in-vivo ER composition inventory.
  snapshot_sha256: 0cdaf91dc4f4bf9261f55530522a8ed41116b930c39ac656de0d729c318bf1c0
- evidence_id: root27-sources-stirling1992-page129
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/f89735edf303/mbc00060-0006.png
  locator: Original primary page129 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.367993Z'
  support: supports
  summary: Title, full abstract and opening Introduction inspected directly in the
    original scan; old substrate-selective mutants are distinguished from newly restrictive
    sec61/sec65 alleles.
  snapshot_sha256: e593c63dc67e772fd28b3332411e80793ba9d9ec0a828ebc19735125d53f88b8
- evidence_id: root27-sources-stirling1992-page130
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/55f33db3a3fc/mbc00060-0007.png
  locator: Original primary page130 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.368737Z'
  support: supports
  summary: Complete Table1 and Introduction continuation read; the experimental strains
    are explicitly named and not assumed to be the reference S288C accession strain.
    The strain/media paragraph and opening methods are read; subsequent methods are
    outside this scan scope.
  snapshot_sha256: d3362a4527251af8da220c3164757d26148c1edad8ab6f4f54cc66be6833d733
- evidence_id: root27-sources-stirling1992-page137
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/b76f0a0c7375/mbc00060-0014.png
  locator: Original primary page137 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.369340Z'
  support: supports
  summary: The SEC61 coding/viability Results are read. Lethality of the sec61 null
    and mutation effects establish protein/cell function, not proof that the ER organelle
    cannot form.
  snapshot_sha256: ab1ffab6cdf5b7955663c903b6158182effa9bfd0845cb6121f2cbb01698b56e
- evidence_id: root27-sources-stirling1992-page138
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/a2683aa00787/mbc00060-0015.png
  locator: Original primary page138 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.369507Z'
  support: supports
  summary: The Identification and Localization of Sec61p Results begin here; antiserum
    and fractionation analysis are read. Fig6 and its caption are visible but the
    nucleotide sequence is not independently reannotated.
  snapshot_sha256: 32d58645d26060035af1178eb5876043b1497a548410ddfe3635d8cad117eeac
- evidence_id: root27-sources-stirling1992-page139
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/694d066200ac/mbc00060-0016.png
  locator: Original primary page139 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.715334Z'
  support: supports
  summary: 'Localization Results conclude: Sec61p is solubilized by Triton, fractionates
    with ER material, and shows ER-pattern immunofluorescence. Fig7/caption and the
    beginning of Discussion were viewed; hydropathy predictions are not modern structure
    validation.'
  snapshot_sha256: b7684416c694989dfc41afdd05cc51d8498b823af6fd7a98b676868654e27405
- evidence_id: root27-sources-stirling1992-page140
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/8f3b5e3aa4a2/mbc00060-0017.png
  locator: Original primary page140 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.756969Z'
  support: supports
  summary: 'Complete Fig8 and caption and continuing Discussion read: the original
    fractionation/blot supports integral ER membrane localization, with different
    strains/conditions specified. Densities are not quantified; later Discussion is
    outside this scope.'
  snapshot_sha256: 2e05803d7f0719e16200e9b22fd30da2e9f7687e55454baeb8bc755cc91464f4
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    --verify
  locator: Entire focused native output
  accessed_at: '2026-10-22T01:11:34.368610Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    --causal-graphs
  locator: Entire focused native output
  accessed_at: '2026-10-22T01:11:35.084248Z'
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
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:09:15Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml'
  snapshot_sha256: 473d81df539c2100c298ec14790427da534236c65afa5266ce9174a252ec93a0
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:09:16Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum_membrane-strict.tsv"
  snapshot_sha256: 3dd9030b5eeb14a45d44ff14c2ed5e0cc7f6ea067dc1c9caee773e873f9d528b
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '9 of 11 collected target identifiers returned OK. PMID:8004676: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID8004676, DOI10.1016/0092-8674(94)90138-4 and COPII: a membrane coat
    formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum.
    Bibliographic identity is resolved; scientific scope remains restricted to the
    separately documented abstract/body inspections.; PMID:9568718: UNREACHABLE; The
    bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID9568718, DOI10.1016/s0092-8674(00)81577-9 and COPII-coated vesicle
    formation reconstituted with purified coat proteins and chemically defined liposomes.
    Bibliographic identity is resolved; scientific scope remains restricted to the
    separately documented abstract/body inspections. Native source checks are separately
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
  topic: ER, membrane and lumen distinctions
  outcome: supported
  target_ids:
  - GO:0005789
  summary: The target exact GO definition and stated kind denote the ER-bounding lipid
    bilayer. The exact ER synonym is native. The broader membrane parent is supported
    by the definitions; the returned list is not claimed to contain an unavailable
    direct edge. Membrane, lumen and Sec61 topology remains distinct.
  evidence_ids:
  - record
  - root27-sources-go
  - policy
- assessment_id: scope
  area: scope
  topic: Budding yeast model and experimental scope
  outcome: supported
  target_ids:
  - GO:0005789
  summary: The species4932 identity is exact. COMMON is qualitative occurrence rather
    than a numerical survey. The distribution note is limited to COPII budding from
    yeast ER; the Sec61 example is separately supported. Stirling Table1 names multiple
    backgrounds and mutant contexts; the review does not silently assign all experiments
    to one sequenced reference strain.
  evidence_ids:
  - record
  - root27-sources-tax4932
  - root27-sources-stirling1992-meta
  - root27-sources-barlowe1994-meta
  - root27-sources-matsuoka1998-meta
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
- assessment_id: composition
  area: grounding
  topic: Constituent bilayer and optional molecular repertoire
  outcome: supported
  target_ids:
  - GO:0005789
  summary: The LIPID row is a collective boundary material, not one identified chemical
    species. REVIEWED_LABEL_ONLY and the open lipid-grounding discussion distinguish
    constituent material from the whole-membrane class. No exhaustive absence of molecular
    identifiers or full composition inventory is asserted.
  evidence_ids:
  - record
  - root27-sources-go
  - policy
- assessment_id: necessity
  area: evidence
  topic: Formation necessity versus protein/cell function
  outcome: unknown
  target_ids:
  - GO:0005789
  summary: Collective membrane constitution supports the defining bilayer row. No
    individual lipid-species necessity is demonstrated. COPII reconstitution conditions
    are not a test of ER-organelle formation.
  evidence_ids:
  - record
  - root27-sources-go
  - protein-contract
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
- assessment_id: budding
  area: evidence
  topic: ER donor context and fresh COPII edge
  outcome: supported
  target_ids:
  - GO:0005789
  summary: GO0090114 defines ER evagination, GO0030127 supplies yeast coat identity,
    Barlowe supports washed-ER budding, and Matsuoka supports sequential assembly
    on ER membranes and defined liposomes. The newly added coat-mediates-budding edge
    states this coarse supported process. The artificial membrane assay is not silently
    equated with complete in-vivo lipid composition.
  evidence_ids:
  - record
  - root27-sources-go
  - root27-sources-stirling1992-meta
  - root27-sources-barlowe1994-meta
  - root27-sources-matsuoka1998-meta
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
- assessment_id: graph
  area: graph
  topic: Every descriptive ER edge
  outcome: supported
  target_ids:
  - GO:0005789
  summary: All five NONMECHANISTIC edges preserve membrane parthood/enclosure, Sec61
    embedding, coat assembly and COPII budding. The fresh fifth edge is supported
    at the coarse process scope by GO and the cited primary abstracts; no recruitment
    kinetics or exact cellular lipid requirement is added.
  evidence_ids:
  - record
  - root27-sources-go
  - root27-sources-stirling1992-meta
  - root27-sources-barlowe1994-meta
  - root27-sources-matsuoka1998-meta
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
- assessment_id: coverage
  area: completeness
  topic: Full target and honest optional gaps
  outcome: supported
  target_ids:
  - GO:0005789
  summary: All target fields and edges were read. The target asserts no images, physical
    measurements, trait links or verbatim snippets. Open molecular inventories remain
    explicit optional gaps; source-access limits do not become invented defects. PROPOSED
    status and append-only historical decisions are preserved.
  evidence_ids:
  - record
  - policy
  - root27-sources-go
  - root27-sources-stirling1992-meta
  - root27-sources-barlowe1994-meta
  - root27-sources-matsuoka1998-meta
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Native ontology terms, taxonomy and proteins were read directly; definitions and
  transitive parentage do not imply an unavailable direct ontology edge. Individual
  molecular formation necessity and exhaustive composition remain unknown.
- 'Primary access is bounded: Stirling original scans129,130,137–140 were read; other
  pages were not. Barlowe/Matsuoka are complete-abstract only; publisher retrieval
  failed. No full-body or quantitative lipid audit is claimed.'
- Species scope and reference-strain accessions do not identify every primary experimental
  strain. Historical authorship, previous searches and prior review dispositions are
  not independently recertified.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User explicitly authorizes a bundle for every uncovered target, including honest
  no-finding reviews. No scientific record edit is authorized.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
