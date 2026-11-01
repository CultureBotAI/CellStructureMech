# Magnetosome membrane identity, composition and source-scope review

- Review: 20261022T021715Z-magnetosome-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:50:59Z
- Finished UTC: 2026-10-22T02:17:15Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact membrane identity, generic lipid material and scoped Mam/Mms association/function are supported; individual formation necessity and MamL localization certainty remain bounded, with no concrete finding.

## Scope And Provenance

Entire single target, exact identities, hierarchy/boundaries, composition, formation necessity, native protein evidence, taxonomic and experimental scope, function, all graph claims and discussions.

Selection: Target 10 of batch31 in strict uncovered path order; frozen native inspection/schema/strict completed before scientific assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0110146 | data/structures/membrane_organelle/magnetosome_membrane.yaml | maintained | magnetosome membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0110146 | Focused validator passed. |
| Focused native strict | passed | True | GO:0110146 | Focused validator passed. |
| Focused native verify | passed | True | GO:0110146 | Native read-only check passed; reporting coverage classes is not itself a scientific finding. |
| Focused native causal-graphs | passed | True | GO:0110146 | Native read-only check passed; reporting coverage classes is not itself a scientific finding. |
| Expression-module applicability | not_applicable | False | GO:0110146 | No regulatory expression-module assertion is used. |
| Claim-level scientific review | passed | True | GO:0110146 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0110146 | 14 of 15 collected target identifiers returned OK. PMID:14766587: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID14766587, DOI10.1128/aem.70.2.1040-1050.2004 and Biochemical and proteomic analysis of the magnetosome membrane in Magnetospirillum gryphiswaldense. Scientific scope remains limited to the separately documented inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0110146 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0110146 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0110146 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0110146 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0110146 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact organelle, lumen and membrane boundaries

identity: supported. Targets: GO:0110146.

The target matches the active GO and UniProt location identities. Native hierarchy and parthood distinguish the membrane-enclosed organelle, surrounding bilayer and enclosed volume. The whole record’s MICRO cross-reference is identity-level context where applicable.

### Native taxonomy and experimental conditions

scope: supported. Targets: GO:0110146.

Taxon identities and model strains are correct, including the current Paramagnetospirillum name for AMB-1 where present. Source experiments are assigned to MSR-1 or AMB-1, not exported as identical gene requirements across all bacteria. RARE/VARIABLE are broad qualitative occurrence statements, not a quantitative survey. The whole-record Archaea absence assertion is assessed separately as unknown.

### Generic lipid material and five identified protein actors

grounding: supported. Targets: GO:0110146.

The reviewed-label-only lipid constituent deliberately withholds the whole GO membrane as molecular grounding. The five native protein accessions are reviewed MSR-1 MamM/MamB/MamA/Mms6/MamL identities. The cohort residence edge does not assert exclusive or invariant residence of every molecule; MamL’s evidence is predicted and its localization is context dependent. Generic material wording and the boundary node preserve the same bilayer-level object.

### Constitutional bilayer versus molecular necessity

grounding: unknown. Targets: GO:0110146.

A lipid boundary is constitutive of the named membrane class. Neither ontology definitions nor the inspected biochemical isolation prove necessity of any individual lipid species, fixed mixture or membrane protein for formation; no such individual essentiality is inferred from this collective row.

### Three scoped membrane relations

graph: supported. Targets: GO:0110146.

The NONMECHANISTIC graph represents membrane parthood, Mam/Mms association and support of controlled biomineralization. The generic lipid-bilayer component is distinguished from a chemical-species assignment; the source supports the membrane boundary and cohort-level function without claiming complete iron-transport chemistry or an invariant protein residence pattern.

### Complete target with bounded optional enrichments

completeness: supported. Targets: GO:0110146.

Every target field, source placement, history and discussion was inspected. No tracked image asset or verbatim snippet is asserted. Generic membrane lipid chemistry, optional inventories and historical image/TODO searches are not automatic defects. Local boundary records and the MamK record where applicable are frozen context only.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/magnetosome_membrane.yaml; Entire maintained target including history, discussions, evidence and every graph node/edge | context_only | The entire single target was read; its maintained scientific bytes remain unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; molecular grounding; essentiality; EssentialityEnum; CausalNode.component_ref | context_only | Essentiality states whether the structure forms without a component. Molecular species, material constituents, complete membranes and enclosed volumes remain distinct. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen actor-identity, evidence and graph-scope guidance | context_only | A graph actor must retain its chemical or structural identity; descriptive topology is not a complete molecular mechanism. |
| boundaries | data/structures/membrane_organelle/magnetosome.yaml; Entire frozen neighboring whole/lumen/membrane records as listed in expanded inspection inputs | context_only | All three boundary records were read as context. Only this target receives a review; neighboring prose is not independent biological proof. |
| magnetosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0110143,GO:0110145,GO:0110146,GO:0043231,GO:0043233,GO:0016020; All requested IDs, names, definitions, obsolete flags and typed returned child relations | supports | All six requested GO identities are active. GO0110143 denotes the magnetic-mineral organelle and directly has the lumen0110145 and membrane0110146 as part_of children; it is an is_a child of0043231. Lumen and membrane retain distinct native definitions. A subtype or contained-part relation is not converted into a universal subclass assertion. |
| magnetosome-agent-SL0512 | https://rest.uniprot.org/locations/SL-0512.json; Native subcellular-location ID, entry name, definition, GO cross-reference and typed hierarchy | supports | SL0512 identifies Magnetosome membrane, maps exactly to GO0110146 and gives its membrane classification and magnetosome parthood. |
| magnetosome-agent-membrane-is-a | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0110146/ancestors?relations=is_a; Exact requested target and complete is_a-only ancestor list | supports | The exact is_a-only ancestor response includes GO0016020 membrane. |
| magnetosome-agent-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete exact taxId, scientificName, rank, lineage and alternative-name fields | supports | ENA verifies the exact taxonomy identity, scientific name and rank for 2. This is identity evidence, not measured prevalence or a biological absence experiment. |
| magnetosome-agent-tax28211 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/28211; Complete exact taxId, scientificName, rank, lineage and alternative-name fields | supports | ENA verifies the exact taxonomy identity, scientific name and rank for 28211. This is identity evidence, not measured prevalence or a biological absence experiment. |
| magnetosome-agent-tax431944 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/431944; Complete exact taxId, scientificName, rank, lineage and alternative-name fields | supports | ENA verifies the exact taxonomy identity, scientific name and rank for 431944. This is identity evidence, not measured prevalence or a biological absence experiment. |
| magnetosome-agent-uebe2016-publisher | https://www.nature.com/articles/nrmicro.2016.99; Complete Key Points and Abstract only; Access options boundary inspected; not a complete main article | supports | The genuine publisher response exposes Key Points and Abstract for Uebe and Schuler2016. These support membrane-enclosed magnetic crystals, genetic model strains, and the overview of invagination, protein recruitment, iron transport, redox biomineralization and chain positioning. The subscription main body is not readable here. |
| magnetosome-agent-uebe2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nrmicro.2016.99; Exact title/authors/DOI/PMID and complete abstractText | supports | The exact native MED record identifies Uebe and Schuler2016, Magnetosome biogenesis in magnetotactic bacteria, DOI10.1038/nrmicro.2016.99, PMID27620945. Its complete abstract matches the publisher abstract. |
| magnetosome-agent-barber2015-pmc | https://pmc.ncbi.nlm.nih.gov/articles/4815348/; Complete scientific review sections pro2827-sec-0001–pro2827-sec-0007, Table1 and Fig1–2 captions; no image pixels or supplements | supports | This fully inspected review distinguishes magnetite from greigite producers, strain-dependent membrane biogenesis, MamA/Mms6 dispensability in particular experiments, proposed MamB/MamM metal-ion transport, and distinct MamK/MamJ chain functions. Its approximate crystal-size range is30–120nm; it does not independently verify the target exact35–120nm diameter range. |
| magnetosome-agent-barber2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1002/pro.2827; Exact native title/authors/DOI/PMID/publication dates and complete abstractText | supports | The native record identifies Barber-Zucker, Keren-Khadmy and Zarivach, DOI10.1002/pro.2827, PMID26457474;2015 online publication and2016 issue dates coexist. The abbreviated target author wording does not change source identity. |
| magnetosome-agent-PMID14766587 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A14766587%20AND%20SRC%3AMED; Exact MED id/source, title, DOI, authorString and complete abstractText | supports | The exact native MED record verifies PMID14766587, title “Biochemical and proteomic analysis of the magnetosome membrane in Magnetospirillum gryphiswaldense.”, DOI and authors. Complete abstract read; its experiment is retained at the stated organism/strain and assay scope. This separately resolves the full-corpus eutils414 transport result. |
| magnetosome-agent-grunberg2004-pmc | https://pmc.ncbi.nlm.nih.gov/articles/348919/; Complete Methods sec1, Results sec13 including subsections14–25 and Tables1–3, complete Discussion sec26; Fig1–7 captions read, no pixels | supports | Direct primary evidence from MSR-1 magnetosome isolation, lipid analysis, gels, sequencing and mass spectrometry supports a membrane with a distinct protein complement and the named Mam/Mms constituents. Table2 separates bona fide assignments from Table3 putative contaminants; binding, transient association and contamination limitations remain explicit. The paper does not establish formation necessity by depletion of each protein or lipid. |
| magnetosome-agent-protein-V6F235 | https://rest.uniprot.org/uniprotkb/V6F235.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry V6F235 identifies mamM in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-V6F510 | https://rest.uniprot.org/uniprotkb/V6F510.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry V6F510 identifies mamB in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-Q93DY9 | https://rest.uniprot.org/uniprotkb/Q93DY9.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry Q93DY9 identifies mamA in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-Q6NE76 | https://rest.uniprot.org/uniprotkb/Q6NE76.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry Q6NE76 identifies mms6 in taxon431944. Localization is interpreted at the source-specific location and evidence code, not as proof of assembly necessity or exclusive residence. |
| magnetosome-agent-protein-Q6NE58 | https://rest.uniprot.org/uniprotkb/Q6NE58.json; Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their cited evidence; MamJ InterPro cross-reference where applicable | supports | The reviewed entry Q6NE58 identifies mamL in taxon431944. The MamL location uses ECO0000305, not experimental ECO0000269; tagged-location comments and the2016 citation do not establish a universal constitutive residence. |
| schema-result | just validate data/structures/membrane_organelle/magnetosome_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/magnetosome_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/magnetosome_membrane.yaml --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/magnetosome_membrane.yaml --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome_membrane-strict.tsv |
| native-verify | /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/magnetosome_membrane.yaml; Exact retained native read-only log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/magnetosome_membrane.yaml; Exact retained native read-only log | supports | data/structures/membrane_organelle/magnetosome_membrane.yaml  (GO:0110146)<br>  magnetosome_membrane_biomineralization_boundary	mam_mms_proteins	UNANCHORED_WITH_UNIPROT	Mam/Mms magnetosome membrane proteins (UniProtKB:V6F235, UniProtKB:V6F510, UniProtKB:Q93DY9, UniProtKB:Q6NE76, UniProtKB:Q6NE58)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/magnetosome_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 15 collected target identifiers returned OK. PMID:14766587: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID14766587, DOI10.1128/aem.70.2.1040-1050.2004 and Biochemical and proteomic analysis of the magnetosome membrane in Magnetospirillum gryphiswaldense. Scientific scope remains limited to the separately documented inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- The fresh target-resolver slice and all five corpus receipt/manifest checks are integrated in this completed review.
- Uebe2016 publisher and nominal-PDF responses contain Key Points/Abstract and access options, not a complete main body. Uebe2011 is native abstract only; its publisher response is403. No unread source passage is certified.
- The Barber review is secondary authority. Its complete scientific main body was read, as were Grünberg2004 Methods/Results/Discussion. No paper image pixels, supplements or raw assay data were inspected.
- Strain-specific mutants, membrane formation, crystal formation and chain organization remain distinct. Collective constituents are not taken as proof that every individual member is required for structure formation.
- Qualitative taxon occurrence and literature-bounded absence are not an exhaustive contemporary prevalence survey. Historical retrieval/search statements are not re-certified or declared false merely because newer evidence exists.
- MamL Q6NE58 has a native predicted location evidence code, and the cited review discusses predominantly cell-membrane localization with minority/transient magnetosome association in AMB-1. This review does not transform that into exclusive MSR-1 localization or an experimental code.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User explicitly authorizes one review per uncovered record, including clean pass_with_limitations, overriding the local issue-only output restriction.
- Only unsaved support/review artifacts are written outside the maintained repository; no scientific record, save/index, Git or publication mutation.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T021715Z-magnetosome-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Magnetosome membrane identity, composition and source-scope review
started_at: '2026-10-22T01:50:59Z'
finished_at: '2026-10-22T02:17:15Z'
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
summary: The exact membrane identity, generic lipid material and scoped Mam/Mms association/function
  are supported; individual formation necessity and MamL localization certainty remain
  bounded, with no concrete finding.
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
  - path: data/structures/membrane_organelle/magnetosome.yaml
    sha256: dd4f1d27b520b8e0b00bc379f6adbac38204d45bed6c1cc9e27a5f3b37f6f4d3
    role: context
  - path: data/structures/membrane_organelle/magnetosome_lumen.yaml
    sha256: 6e777efa5c662d732dad014690fca690f9cad0ec08d9990e907ec04112e059c6
    role: context
  - path: data/structures/membrane_organelle/magnetosome_membrane.yaml
    sha256: 2c4667f86bae65f60cb8aa414079523e0b5f38a940b192e858d5a76f143c6ed4
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
- target_id: GO:0110146
  path: data/structures/membrane_organelle/magnetosome_membrane.yaml
  label: magnetosome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/magnetosome_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single target, exact identities, hierarchy/boundaries, composition,
    formation necessity, native protein evidence, taxonomic and experimental scope,
    function, all graph claims and discussions.
  selection: Target 10 of batch31 in strict uncovered path order; frozen native inspection/schema/strict
    completed before scientific assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0110146
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0110146
  command: just validate data/structures/membrane_organelle/magnetosome_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0110146
  command: just validate-strict data/structures/membrane_organelle/magnetosome_membrane.yaml
    --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0110146
  command: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/magnetosome_membrane.yaml
  exit_code: 0
  summary: Native read-only check passed; reporting coverage classes is not itself
    a scientific finding.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0110146
  command: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/magnetosome_membrane.yaml
  exit_code: 0
  summary: Native read-only check passed; reporting coverage classes is not itself
    a scientific finding.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0110146
  summary: No regulatory expression-module assertion is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0110146
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - boundaries
  - magnetosome-agent-go
  - magnetosome-agent-SL0512
  - magnetosome-agent-membrane-is-a
  - magnetosome-agent-tax2
  - magnetosome-agent-tax28211
  - magnetosome-agent-tax431944
  - magnetosome-agent-uebe2016-publisher
  - magnetosome-agent-uebe2016-meta
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-barber2015-meta
  - magnetosome-agent-PMID14766587
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-protein-V6F235
  - magnetosome-agent-protein-V6F510
  - magnetosome-agent-protein-Q93DY9
  - magnetosome-agent-protein-Q6NE76
  - magnetosome-agent-protein-Q6NE58
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0110146
  summary: '14 of 15 collected target identifiers returned OK. PMID:14766587: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID14766587, DOI10.1128/aem.70.2.1040-1050.2004 and Biochemical and
    proteomic analysis of the magnetosome membrane in Magnetospirillum gryphiswaldense.
    Scientific scope remains limited to the separately documented inspections. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - magnetosome-agent-PMID14766587
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0110146
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0110146
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0110146
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0110146
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0110146
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
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/magnetosome_membrane.yaml
  locator: Entire maintained target including history, discussions, evidence and every
    graph node/edge
  accessed_at: '2026-10-22T02:05:08Z'
  support: context_only
  summary: The entire single target was read; its maintained scientific bytes remain
    unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; molecular grounding; essentiality; EssentialityEnum;
    CausalNode.component_ref
  accessed_at: '2026-10-22T02:05:08Z'
  support: context_only
  summary: Essentiality states whether the structure forms without a component. Molecular
    species, material constituents, complete membranes and enclosed volumes remain
    distinct.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen actor-identity, evidence and graph-scope guidance
  accessed_at: '2026-10-22T02:05:08Z'
  support: context_only
  summary: A graph actor must retain its chemical or structural identity; descriptive
    topology is not a complete molecular mechanism.
- evidence_id: boundaries
  kind: record_content
  reference: data/structures/membrane_organelle/magnetosome.yaml
  locator: Entire frozen neighboring whole/lumen/membrane records as listed in expanded
    inspection inputs
  accessed_at: '2026-10-22T02:05:08Z'
  support: context_only
  summary: All three boundary records were read as context. Only this target receives
    a review; neighboring prose is not independent biological proof.
- evidence_id: magnetosome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0110143,GO:0110145,GO:0110146,GO:0043231,GO:0043233,GO:0016020
  locator: All requested IDs, names, definitions, obsolete flags and typed returned
    child relations
  accessed_at: '2026-10-22T01:54:50.489778Z'
  support: supports
  summary: All six requested GO identities are active. GO0110143 denotes the magnetic-mineral
    organelle and directly has the lumen0110145 and membrane0110146 as part_of children;
    it is an is_a child of0043231. Lumen and membrane retain distinct native definitions.
    A subtype or contained-part relation is not converted into a universal subclass
    assertion.
  snapshot_sha256: fe60b747acb4743040bfafb812bd181bf6b2cac0a8f5ba821cb441ace1f051c8
- evidence_id: magnetosome-agent-SL0512
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0512.json
  locator: Native subcellular-location ID, entry name, definition, GO cross-reference
    and typed hierarchy
  accessed_at: '2026-10-22T01:54:53.425483Z'
  support: supports
  summary: SL0512 identifies Magnetosome membrane, maps exactly to GO0110146 and gives
    its membrane classification and magnetosome parthood.
  snapshot_sha256: 1a5e2619ee57df8b04098c35c9768ec4ef04c4d511e4f0f5eccaed6141d65f19
- evidence_id: magnetosome-agent-membrane-is-a
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0110146/ancestors?relations=is_a
  locator: Exact requested target and complete is_a-only ancestor list
  accessed_at: '2026-10-22T01:54:50.511161Z'
  support: supports
  summary: The exact is_a-only ancestor response includes GO0016020 membrane.
  snapshot_sha256: c094c21da265bd5cd07c85a4894c307bb25d75e01dd072cf98f5f67470bcffb6
- evidence_id: magnetosome-agent-tax2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete exact taxId, scientificName, rank, lineage and alternative-name
    fields
  accessed_at: '2026-10-22T01:54:50.498308Z'
  support: supports
  summary: ENA verifies the exact taxonomy identity, scientific name and rank for
    2. This is identity evidence, not measured prevalence or a biological absence
    experiment.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: magnetosome-agent-tax28211
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/28211
  locator: Complete exact taxId, scientificName, rank, lineage and alternative-name
    fields
  accessed_at: '2026-10-22T01:54:50.505577Z'
  support: supports
  summary: ENA verifies the exact taxonomy identity, scientific name and rank for
    28211. This is identity evidence, not measured prevalence or a biological absence
    experiment.
  snapshot_sha256: eb9d44c1e2cf0944eb4414649c09418a757a87de66fc01f51cc6c980ef68e802
- evidence_id: magnetosome-agent-tax431944
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/431944
  locator: Complete exact taxId, scientificName, rank, lineage and alternative-name
    fields
  accessed_at: '2026-10-22T01:54:51.109038Z'
  support: supports
  summary: ENA verifies the exact taxonomy identity, scientific name and rank for
    431944. This is identity evidence, not measured prevalence or a biological absence
    experiment.
  snapshot_sha256: 8e6916672afb4c32a2a99e2dcc07f5a14b4ba7b0969243ce89646042ce60476d
- evidence_id: magnetosome-agent-uebe2016-publisher
  kind: authority
  reference: https://www.nature.com/articles/nrmicro.2016.99
  locator: Complete Key Points and Abstract only; Access options boundary inspected;
    not a complete main article
  accessed_at: '2026-10-22T01:55:29.602449Z'
  support: supports
  summary: The genuine publisher response exposes Key Points and Abstract for Uebe
    and Schuler2016. These support membrane-enclosed magnetic crystals, genetic model
    strains, and the overview of invagination, protein recruitment, iron transport,
    redox biomineralization and chain positioning. The subscription main body is not
    readable here.
  snapshot_sha256: 068e5eea78b8f17c89b712fb2777cfebe58c6b78f2b83707d8c554273a8e9359
- evidence_id: magnetosome-agent-uebe2016-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrmicro.2016.99
  locator: Exact title/authors/DOI/PMID and complete abstractText
  accessed_at: '2026-10-22T01:54:53.760632Z'
  support: supports
  summary: The exact native MED record identifies Uebe and Schuler2016, Magnetosome
    biogenesis in magnetotactic bacteria, DOI10.1038/nrmicro.2016.99, PMID27620945.
    Its complete abstract matches the publisher abstract.
  snapshot_sha256: aafc33cb7d6402c95ed55eda17b01e3ef154db512917948d8161ed5bd3ac945e
- evidence_id: magnetosome-agent-barber2015-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4815348/
  locator: Complete scientific review sections pro2827-sec-0001–pro2827-sec-0007,
    Table1 and Fig1–2 captions; no image pixels or supplements
  accessed_at: '2026-10-22T01:55:28.453057Z'
  support: supports
  summary: This fully inspected review distinguishes magnetite from greigite producers,
    strain-dependent membrane biogenesis, MamA/Mms6 dispensability in particular experiments,
    proposed MamB/MamM metal-ion transport, and distinct MamK/MamJ chain functions.
    Its approximate crystal-size range is30–120nm; it does not independently verify
    the target exact35–120nm diameter range.
  snapshot_sha256: a052d6b82e120fa4f253f6aa7abeaf5c9a5080f7748fbbe35cfd2150c3713934
- evidence_id: magnetosome-agent-barber2015-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1002/pro.2827
  locator: Exact native title/authors/DOI/PMID/publication dates and complete abstractText
  accessed_at: '2026-10-22T01:54:54.045286Z'
  support: supports
  summary: The native record identifies Barber-Zucker, Keren-Khadmy and Zarivach,
    DOI10.1002/pro.2827, PMID26457474;2015 online publication and2016 issue dates
    coexist. The abbreviated target author wording does not change source identity.
  snapshot_sha256: 2fbe01feb61de63ae0641fcb7d783622f8e45a56acbb420948f5bb24612f50e1
- evidence_id: magnetosome-agent-PMID14766587
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A14766587%20AND%20SRC%3AMED
  locator: Exact MED id/source, title, DOI, authorString and complete abstractText
  accessed_at: '2026-10-22T01:54:53.146827Z'
  support: supports
  summary: The exact native MED record verifies PMID14766587, title “Biochemical and
    proteomic analysis of the magnetosome membrane in Magnetospirillum gryphiswaldense.”,
    DOI and authors. Complete abstract read; its experiment is retained at the stated
    organism/strain and assay scope. This separately resolves the full-corpus eutils414
    transport result.
  snapshot_sha256: 58b737f08ab3ed694909eba9351656b618908df49ab83cd7d6a72fb030650b66
- evidence_id: magnetosome-agent-grunberg2004-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/348919/
  locator: Complete Methods sec1, Results sec13 including subsections14–25 and Tables1–3,
    complete Discussion sec26; Fig1–7 captions read, no pixels
  accessed_at: '2026-10-22T01:55:28.245268Z'
  support: supports
  summary: Direct primary evidence from MSR-1 magnetosome isolation, lipid analysis,
    gels, sequencing and mass spectrometry supports a membrane with a distinct protein
    complement and the named Mam/Mms constituents. Table2 separates bona fide assignments
    from Table3 putative contaminants; binding, transient association and contamination
    limitations remain explicit. The paper does not establish formation necessity
    by depletion of each protein or lipid.
  snapshot_sha256: ca7ae2f19185633cd778e9550909b7f68bb2ea18c80f4c0a7a65aa7c59527485
- evidence_id: magnetosome-agent-protein-V6F235
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/V6F235.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:52.105347Z'
  support: supports
  summary: The reviewed entry V6F235 identifies mamM in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: 1e87ed2625ca608d68e069dbff2376d2b08f269da840189abf695e91b2b1c3d6
- evidence_id: magnetosome-agent-protein-V6F510
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/V6F510.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:51.327522Z'
  support: supports
  summary: The reviewed entry V6F510 identifies mamB in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: 526814c66af4b8bbf66cd0f3399455f2537c025fe9045475737b4e5293e75212
- evidence_id: magnetosome-agent-protein-Q93DY9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q93DY9.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:51.333535Z'
  support: supports
  summary: The reviewed entry Q93DY9 identifies mamA in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: d0806f93bc6b1b2c700e6d781028aded4bb2194d74302a4cb4074f45dadb9580
- evidence_id: magnetosome-agent-protein-Q6NE76
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q6NE76.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:51.904548Z'
  support: supports
  summary: The reviewed entry Q6NE76 identifies mms6 in taxon431944. Localization
    is interpreted at the source-specific location and evidence code, not as proof
    of assembly necessity or exclusive residence.
  snapshot_sha256: 4bdaae8944c2f60830514481d846baf51e91fd39fcb5288d13fab7d526fe52a8
- evidence_id: magnetosome-agent-protein-Q6NE58
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q6NE58.json
  locator: Exact accession/review status, recommended name, primary gene, taxon, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their cited evidence; MamJ InterPro cross-reference where
    applicable
  accessed_at: '2026-10-22T01:54:52.504317Z'
  support: supports
  summary: The reviewed entry Q6NE58 identifies mamL in taxon431944. The MamL location
    uses ECO0000305, not experimental ECO0000269; tagged-location comments and the2016
    citation do not establish a universal constitutive residence.
  snapshot_sha256: c212d204735c53d726f181ec53604bf04160fe80e87206c0fe04dd5dd9836e13
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/magnetosome_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:51:00Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/magnetosome_membrane.yaml'
  snapshot_sha256: bc5d1a298e255bc0d07fa72804ba6a198162b656b7fb09f732e65f8292635ef6
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/magnetosome_membrane.yaml
    --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:51:01Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/magnetosome_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch31-20261022-ag46a4d4/magnetosome_membrane-strict.tsv"
  snapshot_sha256: 804549ee28037141b8bf2e6d732f75fdeb3a25b2669bd6b7aec402dfefa307ac
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/magnetosome_membrane.yaml
  locator: Exact retained native read-only log
  accessed_at: '2026-10-22T02:00:57.038730Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/magnetosome_membrane.yaml
  locator: Exact retained native read-only log
  accessed_at: '2026-10-22T02:01:18.981464Z'
  support: supports
  summary: "data/structures/membrane_organelle/magnetosome_membrane.yaml  (GO:0110146)\n\
    \  magnetosome_membrane_biomineralization_boundary\tmam_mms_proteins\tUNANCHORED_WITH_UNIPROT\t\
    Mam/Mms magnetosome membrane proteins (UniProtKB:V6F235, UniProtKB:V6F510, UniProtKB:Q93DY9,\
    \ UniProtKB:Q6NE76, UniProtKB:Q6NE58)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n\
    \     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or\
    \ xref on the node\n     1  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 3abc710ac03ac07db44a23f8b9dd00fa2df37d724e1ea9e8bf9eda70fd8816a7
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/magnetosome_membrane.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '14 of 15 collected target identifiers returned OK. PMID:14766587: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID14766587, DOI10.1128/aem.70.2.1040-1050.2004 and Biochemical and
    proteomic analysis of the magnetosome membrane in Magnetospirillum gryphiswaldense.
    Scientific scope remains limited to the separately documented inspections. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
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
  topic: Exact organelle, lumen and membrane boundaries
  outcome: supported
  target_ids:
  - GO:0110146
  summary: The target matches the active GO and UniProt location identities. Native
    hierarchy and parthood distinguish the membrane-enclosed organelle, surrounding
    bilayer and enclosed volume. The whole record’s MICRO cross-reference is identity-level
    context where applicable.
  evidence_ids:
  - record
  - boundaries
  - magnetosome-agent-go
  - magnetosome-agent-membrane-is-a
  - magnetosome-agent-SL0512
- assessment_id: taxon-scope
  area: scope
  topic: Native taxonomy and experimental conditions
  outcome: supported
  target_ids:
  - GO:0110146
  summary: Taxon identities and model strains are correct, including the current Paramagnetospirillum
    name for AMB-1 where present. Source experiments are assigned to MSR-1 or AMB-1,
    not exported as identical gene requirements across all bacteria. RARE/VARIABLE
    are broad qualitative occurrence statements, not a quantitative survey. The whole-record
    Archaea absence assertion is assessed separately as unknown.
  evidence_ids:
  - record
  - magnetosome-agent-tax2
  - magnetosome-agent-tax28211
  - magnetosome-agent-tax431944
  - magnetosome-agent-uebe2016-publisher
  - magnetosome-agent-uebe2016-meta
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-barber2015-meta
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-PMID14766587
- assessment_id: composition
  area: grounding
  topic: Generic lipid material and five identified protein actors
  outcome: supported
  target_ids:
  - GO:0110146
  summary: The reviewed-label-only lipid constituent deliberately withholds the whole
    GO membrane as molecular grounding. The five native protein accessions are reviewed
    MSR-1 MamM/MamB/MamA/Mms6/MamL identities. The cohort residence edge does not
    assert exclusive or invariant residence of every molecule; MamL’s evidence is
    predicted and its localization is context dependent. Generic material wording
    and the boundary node preserve the same bilayer-level object.
  evidence_ids:
  - record
  - policy
  - magnetosome-agent-go
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-protein-V6F235
  - magnetosome-agent-protein-V6F510
  - magnetosome-agent-protein-Q93DY9
  - magnetosome-agent-protein-Q6NE76
  - magnetosome-agent-protein-Q6NE58
- assessment_id: formation-necessity
  area: grounding
  topic: Constitutional bilayer versus molecular necessity
  outcome: unknown
  target_ids:
  - GO:0110146
  summary: A lipid boundary is constitutive of the named membrane class. Neither ontology
    definitions nor the inspected biochemical isolation prove necessity of any individual
    lipid species, fixed mixture or membrane protein for formation; no such individual
    essentiality is inferred from this collective row.
  evidence_ids:
  - record
  - policy
  - magnetosome-agent-go
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-barber2015-pmc
- assessment_id: function-graph
  area: graph
  topic: Three scoped membrane relations
  outcome: supported
  target_ids:
  - GO:0110146
  summary: The NONMECHANISTIC graph represents membrane parthood, Mam/Mms association
    and support of controlled biomineralization. The generic lipid-bilayer component
    is distinguished from a chemical-species assignment; the source supports the membrane
    boundary and cohort-level function without claiming complete iron-transport chemistry
    or an invariant protein residence pattern.
  evidence_ids:
  - record
  - graph-policy
  - magnetosome-agent-go
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-protein-V6F235
  - magnetosome-agent-protein-V6F510
  - magnetosome-agent-protein-Q93DY9
  - magnetosome-agent-protein-Q6NE76
  - magnetosome-agent-protein-Q6NE58
- assessment_id: completeness
  area: completeness
  topic: Complete target with bounded optional enrichments
  outcome: supported
  target_ids:
  - GO:0110146
  summary: Every target field, source placement, history and discussion was inspected.
    No tracked image asset or verbatim snippet is asserted. Generic membrane lipid
    chemistry, optional inventories and historical image/TODO searches are not automatic
    defects. Local boundary records and the MamK record where applicable are frozen
    context only.
  evidence_ids:
  - record
  - policy
  - magnetosome-agent-go
  - magnetosome-agent-uebe2016-publisher
  - magnetosome-agent-uebe2016-meta
  - magnetosome-agent-barber2015-pmc
  - magnetosome-agent-barber2015-meta
  - magnetosome-agent-grunberg2004-pmc
  - magnetosome-agent-PMID14766587
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- The fresh target-resolver slice and all five corpus receipt/manifest checks are
  integrated in this completed review.
- Uebe2016 publisher and nominal-PDF responses contain Key Points/Abstract and access
  options, not a complete main body. Uebe2011 is native abstract only; its publisher
  response is403. No unread source passage is certified.
- The Barber review is secondary authority. Its complete scientific main body was
  read, as were Grünberg2004 Methods/Results/Discussion. No paper image pixels, supplements
  or raw assay data were inspected.
- Strain-specific mutants, membrane formation, crystal formation and chain organization
  remain distinct. Collective constituents are not taken as proof that every individual
  member is required for structure formation.
- Qualitative taxon occurrence and literature-bounded absence are not an exhaustive
  contemporary prevalence survey. Historical retrieval/search statements are not re-certified
  or declared false merely because newer evidence exists.
- MamL Q6NE58 has a native predicted location evidence code, and the cited review
  discusses predominantly cell-membrane localization with minority/transient magnetosome
  association in AMB-1. This review does not transform that into exclusive MSR-1 localization
  or an experimental code.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User explicitly authorizes one review per uncovered record, including clean pass_with_limitations,
  overriding the local issue-only output restriction.
- Only unsaved support/review artifacts are written outside the maintained repository;
  no scientific record, save/index, Git or publication mutation.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
