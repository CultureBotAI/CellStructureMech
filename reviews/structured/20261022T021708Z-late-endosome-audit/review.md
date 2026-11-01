# Late endosome identity, source and topology review

- Review: 20261022T021708Z-late-endosome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:50:43Z
- Finished UTC: 2026-10-22T02:17:08Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed within the explicitly bounded source scope.

## Scope And Provenance

Entire single target: identity, hierarchy/parthood, material boundaries, source and taxonomic claims, examples, functions and every graph edge.

Selection: Target 4 of batch thirty-one in strict uncovered path order from fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005770 | data/structures/membrane_organelle/late_endosome.yaml | maintained | late endosome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0005770 | Focused native check passed; scientific scope assessed separately. |
| Native protein causal-graphs | passed | True | GO:0005770 | Focused native check passed; scientific scope assessed separately. |
| Focused native schema | passed | True | GO:0005770 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005770 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005770 | No expression-module claim or dataset is used. Genome preparation, compartment topology and direct recruitment sources apply. |
| Claim-level scientific review | passed | True | GO:0005770 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005770 | 13 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent sorting into the multivesicular body pathway requires the function of a conserved endosomal protein sorting complex, ESCRT-I. Scientific scope remains limited to the separately documented inspections.; PMID:12194857: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID12194857, DOI10.1016/s1534-5807(02)00220-4 and Escrt-III: an endosome-associated heterooligomeric protein complex required for mvb sorting. Scientific scope remains limited to the separately documented inspections.; cellstructuremech:multivesicular_body_intraluminal_vesicle: SKIPPED; The repository-minted identifier uniquely resolves to the frozen maintained multivesicular body intraluminal vesicle record at data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml. An anchored hidden/ignored-inclusive corpus search and exact input hash confirm reference identity, not all biological assertions. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005770 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005770 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005770 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005770 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005770 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact structure and mereology

identity: supported. Targets: GO:0005770.

Native definitions and relations support the late endosome, its enclosing membrane and internal lumen as distinct structures/regions. MVB is a child example rather than a synonym for every late endosome.

### Molecular material versus whole compartment

grounding: supported. Targets: GO:0005770.

The LIPID row denotes collective boundary material and leaves exact molecular grounding unset. ESSENTIAL is the constitutive enclosing bilayer, not a requirement for each unspecified lipid species. The graph membrane node is distinct from the enclosed whole-organelle or lumen nodes.

### Constitutive material versus experimental formation necessity

grounding: unknown. Targets: GO:0005770.

The collective lipid bilayer is constitutive of the enclosed compartment or named membrane. The inspected ontology and recruitment/sorting sources do not test formation after removal of all lipid material, nor establish necessity of any individual lipid species or fixed mixture. Supported boundary composition remains distinct from experimentally demonstrated formation necessity.

### Taxon and actual experimental context

scope: supported. Targets: GO:0005770.

Yeast MVB experiments support a late-endosome child example. COMMON is qualitative occurrence. Transient ESCRT complexes are not listed as stable organelle constituents, and the sources are not generalized to every endosome or cargo class.

### Bounded functional evidence

evidence: supported. Targets: GO:0005770.

GO0071985 and the yeast abstracts support cargo sorting into MVB luminal vesicles. Membrane sorting-surface and lumen receiving-space roles remain separate. Vps27 localization/recruitment is directly supported where cited.

### Every target graph edge

graph: supported. Targets: GO:0005770.

All six NONMECHANISTIC edges have bounded support: enclosure, ESCRT-I sorting, ESCRT-II recruitment via Vps20, ESCRT-III remodeling from complex requirements plus review synthesis, inward budding and MVB containment. GO definitions support the last two. The remodeling edge is not attributed solely to the Babst abstract as an isolated force assay; no complete scission/recycling cycle is asserted.

### Unresolved inventories and evidence tiers

evidence: unknown. Targets: GO:0005770.

No complete molecular inventory, quantitative prevalence or isolated physical sufficiency experiment is established. Primary abstracts, selected primary-body sections and review synthesis retain distinct evidentiary roles.

### Historical first-pass grounding discussion

completeness: supported. Targets: GO:0005770.

The OPEN note explicitly describes the first record and terms curated in that pass; it does not assert that exact late-specific terms do not exist. Verified membrane/lumen candidates make the optional node-grounding follow-up actionable. Their availability alone is not a defect, and whole-membrane identity must remain separate from unresolved lipid-material grounding.

### All maintained fields and native status

completeness: supported. Targets: GO:0005770.

Entire target, all graph edges, source placements, discussions and history inspected. No maintained image asset, numeric physical property, trait link, protein example or verbatim snippet is asserted. PROPOSED remains unchanged; historic issue closures are not independently recertified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/late_endosome.yaml; Entire maintained target, all sources, examples, graph edges, discussions and history | context_only | Full target read; no scientific record or native status changed. |
| policy | docs/CURATION.md; Exact identity, hierarchy versus parthood and narrow source support | context_only | Whole structures, enclosed volumes and molecular material remain distinct; optional inventories do not require speculative completion. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, graph nodes and essentiality | context_only | Constitutive boundary material is not a knockout assertion about every chemical species. A descriptive graph still needs support at each edge. |
| root31-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005770,GO:0005768,GO:0005771,GO:0010008,GO:0031904,GO:0031906,GO:0031902,GO:0071985,GO:0000813,GO:0000814,GO:0000815,GO:0031039,GO:0005634,GO:0000228; Complete names, definitions, synonyms, active flags and all returned child relations for fourteen identifiers | supports | All fourteen active native entries were read. GO0005770 is an endosome child with MVB as an is_a child. Exact membrane0031902 and lumen0031906 are late-endosome parts, with direct generic membrane/lumen parents. GO0071985 describes MVB luminal-vesicle cargo entry. ESCRT definitions match the sorting context. Macronucleus0031039 denotes the transcriptional polyploid ciliate compartment, distinct from nuclear chromosome0000228. |
| root31-sources-katzmann2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11511343%20AND%20SRC%3AMED; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID11511343, DOI10.1016/s0092-8674(01)00434-2, Ubiquitin-dependent sorting into the multivesicular body pathway requires the function of a conserved endosomal protein sorting complex, ESCRT-I., Katzmann DJ, Babst M, Emr SD.. The complete primary abstract supports yeast ESCRT-I ubiquitin recognition and required MVB cargo sorting; its historical subunit description is not treated as a complete current inventory. |
| root31-sources-katzmann2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.200302136; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID12900393, DOI10.1083/jcb.200302136, Vps27 recruits ESCRT machinery to endosomes during MVB sorting., Katzmann DJ, Stefan CJ, Babst M, Emr SD.. The complete primary abstract describes Vps27 upstream recruitment of ESCRT-I to endosomes and linkage to PI3P and ubiquitinated cargo. Selected primary body experiments were separately read. |
| root31-sources-babst2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12194857%20AND%20SRC%3AMED; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID12194857, DOI10.1016/s1534-5807(02)00220-4, Escrt-III: an endosome-associated heterooligomeric protein complex required for mvb sorting., Babst M, Katzmann DJ, Estepa-Sabal EJ, Meerloo T, Emr SD.. The complete primary abstract describes transient yeast ESCRT-III assembly, endosomal recruitment and MVB sorting requirements. It does not independently isolate the physical force of membrane deformation. |
| root31-sources-teo2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2004.09.003; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID15469844, DOI10.1016/j.devcel.2004.09.003, ESCRT-II, an endosome-associated complex required for protein sorting: crystal structure and interactions with ESCRT-III and membranes., Teo H, Perisic O, González B, Williams RL.. The complete primary abstract describes the3.6-Angstrom ESCRT-II core, direct Vps20 binding and enhanced lipid-vesicle association. It does not reconstitute the full scission cycle. |
| root31-sources-henne2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2011.05.015; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID21763610, DOI10.1016/j.devcel.2011.05.015, The ESCRT pathway., Henne WM, Buchkovich NJ, Emr SD.. The complete review abstract summarizes MVB cargo delivery and membrane remodeling. This is synthesis, not a newly inspected primary remodeling assay. |
| root31-sources-katzmann2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/; Complete body sec4 Vps27 localization, sec5 ESCRT-I recruitment, sec6 interaction, sec12 plasmids/strains and sec13 microscopy, with captions; no original image pixels | supports | Genuine PMC2172707 complete sections4–6 and12–13 read with Fig2–4 captions. GFP-Vps27/PI3P colocalization and vps34/FYVE perturbations support endosomal recruitment; Vps23 recruitment depends on Vps27, and membrane-fraction coimmunoprecipitation supports their association. The strain table and microscopy methods were read. Species4932 is not used to infer S288C. |
| root31-sources-teo2004-primary-pdf | https://www2.mrc-lmb.cam.ac.uk/groups/rlw/download/publications/15469844.pdf; Primary MRC-hosted PDF p559 summary/Introduction and pp564–567 Results/Conclusions/Methods, including Fig4–6 captions and pull-down/liposome protocols; no pixels or supplements | supports | Genuine primary PDF read at p559 and complete pp564–567. Purified Vps25 binds Vps20 in reciprocal pulldowns; ESCRT-II or Vps25 increases Vps20 association with bovine-brain lipid vesicles. The5micromolar-protein sedimentation assay supports a recruitment step, not reconstitution of all ESCRT-III assembly/scission. Fig6 membrane orientation remains a model. |
| local-ilv | data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml; Full neighbor read; exact identifier, definition, hierarchy, graph and discussions | context_only | The repository-minted identifier uniquely resolves to an intraluminal vesicle part of MVB. Reference resolution does not count this neighbor as another reviewed target. |
| neighbor-late_endosome_lumen | data/structures/membrane_organelle/late_endosome_lumen.yaml; Entire maintained neighbor read | context_only | The exact boundary/localization terms are already maintained. Their availability is a bounded follow-up option; it does not refute the historical first-pass discussion or require a whole-membrane CURIE on lipid material. |
| neighbor-late_endosome_membrane | data/structures/membrane_organelle/late_endosome_membrane.yaml; Entire maintained neighbor read | context_only | The exact boundary/localization terms are already maintained. Their availability is a bounded follow-up option; it does not refute the historical first-pass discussion or require a whole-membrane CURIE on lipid material. |
| boundary-search | rg --no-ignore --hidden -n --glob *.yaml ^identifier: (GO:0031902&#124;GO:0031906&#124;cellstructuremech:multivesicular_body_intraluminal_vesicle)$ data/structures; Anchored exact identifier matches under data/structures | context_only | data/structures/membrane_organelle/late_endosome_lumen.yaml:1:identifier: GO:0031906<br>data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml:1:identifier: cellstructuremech:multivesicular_body_intraluminal_vesicle<br>data/structures/membrane_organelle/late_endosome_membrane.yaml:1:identifier: GO:0031902 |
| root31-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and otherNames | supports | ENA4932 is Saccharomyces cerevisiae at species rank. Qualitative occurrence is not a measured prevalence or an exact experimental-strain determination. |
| native-verify | /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome.yaml --verify; Entire retained focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome.yaml --causal-graphs; Entire retained focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/late_endosome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/late_endosome.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/late_endosome.yaml --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/late_endosome.yaml --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/late_endosome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent sorting into the multivesicular body pathway requires the function of a conserved endosomal protein sorting complex, ESCRT-I. Scientific scope remains limited to the separately documented inspections.; PMID:12194857: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID12194857, DOI10.1016/s1534-5807(02)00220-4 and Escrt-III: an endosome-associated heterooligomeric protein complex required for mvb sorting. Scientific scope remains limited to the separately documented inspections.; cellstructuremech:multivesicular_body_intraluminal_vesicle: SKIPPED; The repository-minted identifier uniquely resolves to the frozen maintained multivesicular body intraluminal vesicle record at data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml. An anchored hidden/ignored-inclusive corpus search and exact input hash confirm reference identity, not all biological assertions. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- COMMON is qualitative occurrence, not measured prevalence. Historical authorship and earlier issue dispositions are not independently recertified.
- Katzmann2001 and, where cited, Babst2002 were read as complete primary abstracts only. They do not establish every physical mechanism or exact experimental genotype.
- Katzmann2003 body scope is complete sec4–6 and12–13, including captions; original pixels and remaining body sections were not inspected.
- Teo2004 genuine primary PDF scope is p559 and complete pp564–567 with captions/methods. Other structural-analysis sections, pixels and supplements were not inspected. Henne2011 is a review whose complete abstract was read, not a newly inspected primary remodeling assay.
- The linked ILV record was read for exact reference resolution and relevant containment, not counted as another reviewed target. Exact late-endosome membrane/lumen node groundings remain optional follow-up candidates, distinct from ungrounded lipid material.
- The collective lipid ESSENTIAL row is interpreted at its constitutive material scope; experimental formation necessity was not established by the inspected sources.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes bundles for every uncovered record, including honest no-finding reviews. Scientific content remains unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T021708Z-late-endosome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Late endosome identity, source and topology review
started_at: '2026-10-22T01:50:43Z'
finished_at: '2026-10-22T02:17:08Z'
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
summary: No concrete curation defect observed within the explicitly bounded source
  scope.
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
  - path: data/structures/membrane_organelle/endosome.yaml
    sha256: 7eb3c5b8022e63698365a49990831c7609d649c6024002eb19f6a28cdfff38a8
    role: context
  - path: data/structures/membrane_organelle/late_endosome.yaml
    sha256: af154194fa19aa780722ab1444ffedd803936571c202be13ce49983c7d9352a0
    role: target
  - path: data/structures/membrane_organelle/late_endosome_lumen.yaml
    sha256: f4f801cc662e9d680eec7749b54e4c69b699e76e8af5faba7b27316d3b0ecc91
    role: context
  - path: data/structures/membrane_organelle/late_endosome_membrane.yaml
    sha256: abd97317590eaf6f8b21b611d08470cc92e1a3b8bb4773381d092e2e4ddb27cc
    role: context
  - path: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    sha256: 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916
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
- target_id: GO:0005770
  path: data/structures/membrane_organelle/late_endosome.yaml
  label: late endosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/late_endosome.yaml
    role: maintained scientific record
scope:
  description: 'Entire single target: identity, hierarchy/parthood, material boundaries,
    source and taxonomic claims, examples, functions and every graph edge.'
  selection: Target 4 of batch thirty-one in strict uncovered path order from fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005770
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0005770
  command: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; scientific scope assessed separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005770
  command: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; scientific scope assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005770
  command: just validate data/structures/membrane_organelle/late_endosome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005770
  command: just validate-strict data/structures/membrane_organelle/late_endosome.yaml
    --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005770
  summary: No expression-module claim or dataset is used. Genome preparation, compartment
    topology and direct recruitment sources apply.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005770
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - schema
  - root31-sources-go
  - root31-sources-katzmann2001-meta
  - root31-sources-katzmann2003-meta
  - root31-sources-babst2002-meta
  - root31-sources-teo2004-meta
  - root31-sources-henne2011-meta
  - root31-sources-katzmann2003-pmc
  - root31-sources-teo2004-primary-pdf
  - local-ilv
  - neighbor-late_endosome_lumen
  - neighbor-late_endosome_membrane
  - boundary-search
  - root31-sources-tax4932
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005770
  summary: '13 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent
    sorting into the multivesicular body pathway requires the function of a conserved
    endosomal protein sorting complex, ESCRT-I. Scientific scope remains limited to
    the separately documented inspections.; PMID:12194857: UNREACHABLE; The bulk transport
    returned414; the independently retrieved exact MED identity confirms PMID12194857,
    DOI10.1016/s1534-5807(02)00220-4 and Escrt-III: an endosome-associated heterooligomeric
    protein complex required for mvb sorting. Scientific scope remains limited to
    the separately documented inspections.; cellstructuremech:multivesicular_body_intraluminal_vesicle:
    SKIPPED; The repository-minted identifier uniquely resolves to the frozen maintained
    multivesicular body intraluminal vesicle record at data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml.
    An anchored hidden/ignored-inclusive corpus search and exact input hash confirm
    reference identity, not all biological assertions. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root31-sources-katzmann2001-meta
  - root31-sources-babst2002-meta
  - local-ilv
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005770
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
  - GO:0005770
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
  - GO:0005770
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
  - GO:0005770
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
  - GO:0005770
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
  reference: data/structures/membrane_organelle/late_endosome.yaml
  locator: Entire maintained target, all sources, examples, graph edges, discussions
    and history
  accessed_at: '2026-10-22T02:01:16Z'
  support: context_only
  summary: Full target read; no scientific record or native status changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, hierarchy versus parthood and narrow source support
  accessed_at: '2026-10-22T02:01:16Z'
  support: context_only
  summary: Whole structures, enclosed volumes and molecular material remain distinct;
    optional inventories do not require speculative completion.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, graph nodes and essentiality
  accessed_at: '2026-10-22T02:01:16Z'
  support: context_only
  summary: Constitutive boundary material is not a knockout assertion about every
    chemical species. A descriptive graph still needs support at each edge.
- evidence_id: root31-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005770,GO:0005768,GO:0005771,GO:0010008,GO:0031904,GO:0031906,GO:0031902,GO:0071985,GO:0000813,GO:0000814,GO:0000815,GO:0031039,GO:0005634,GO:0000228
  locator: Complete names, definitions, synonyms, active flags and all returned child
    relations for fourteen identifiers
  accessed_at: '2026-10-22T01:51:20.292950Z'
  support: supports
  summary: All fourteen active native entries were read. GO0005770 is an endosome
    child with MVB as an is_a child. Exact membrane0031902 and lumen0031906 are late-endosome
    parts, with direct generic membrane/lumen parents. GO0071985 describes MVB luminal-vesicle
    cargo entry. ESCRT definitions match the sorting context. Macronucleus0031039
    denotes the transcriptional polyploid ciliate compartment, distinct from nuclear
    chromosome0000228.
  snapshot_sha256: 9247adc57897e68974e7ff5d2e137b8a39b0af19d4dbba94a647479312167c7a
- evidence_id: root31-sources-katzmann2001-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11511343%20AND%20SRC%3AMED
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:10:57.861587Z'
  support: supports
  summary: Exact MED PMID11511343, DOI10.1016/s0092-8674(01)00434-2, Ubiquitin-dependent
    sorting into the multivesicular body pathway requires the function of a conserved
    endosomal protein sorting complex, ESCRT-I., Katzmann DJ, Babst M, Emr SD.. The
    complete primary abstract supports yeast ESCRT-I ubiquitin recognition and required
    MVB cargo sorting; its historical subunit description is not treated as a complete
    current inventory.
  snapshot_sha256: 89b0ab16f1c997094ab3253063701f5097b815c030e16320d5d41f485e3d50a9
- evidence_id: root31-sources-katzmann2003-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.200302136
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:10:57.875261Z'
  support: supports
  summary: Exact MED PMID12900393, DOI10.1083/jcb.200302136, Vps27 recruits ESCRT
    machinery to endosomes during MVB sorting., Katzmann DJ, Stefan CJ, Babst M, Emr
    SD.. The complete primary abstract describes Vps27 upstream recruitment of ESCRT-I
    to endosomes and linkage to PI3P and ubiquitinated cargo. Selected primary body
    experiments were separately read.
  snapshot_sha256: 7db90817ea355af4a50a7af4ff871e6469a57ef9b2c9e03388f6d02e8c202720
- evidence_id: root31-sources-babst2002-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12194857%20AND%20SRC%3AMED
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:10:58.446989Z'
  support: supports
  summary: 'Exact MED PMID12194857, DOI10.1016/s1534-5807(02)00220-4, Escrt-III: an
    endosome-associated heterooligomeric protein complex required for mvb sorting.,
    Babst M, Katzmann DJ, Estepa-Sabal EJ, Meerloo T, Emr SD.. The complete primary
    abstract describes transient yeast ESCRT-III assembly, endosomal recruitment and
    MVB sorting requirements. It does not independently isolate the physical force
    of membrane deformation.'
  snapshot_sha256: 154c66e5c81005bcb646718e07a114e6c610e20c4a80803a5505061f4c107317
- evidence_id: root31-sources-teo2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2004.09.003
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:10:57.877564Z'
  support: supports
  summary: 'Exact MED PMID15469844, DOI10.1016/j.devcel.2004.09.003, ESCRT-II, an
    endosome-associated complex required for protein sorting: crystal structure and
    interactions with ESCRT-III and membranes., Teo H, Perisic O, González B, Williams
    RL.. The complete primary abstract describes the3.6-Angstrom ESCRT-II core, direct
    Vps20 binding and enhanced lipid-vesicle association. It does not reconstitute
    the full scission cycle.'
  snapshot_sha256: 092a112c9409a79c051d42786aeccd62376d565f07ed37f3176165fd5bc1fddf
- evidence_id: root31-sources-henne2011-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2011.05.015
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:10:57.861442Z'
  support: supports
  summary: Exact MED PMID21763610, DOI10.1016/j.devcel.2011.05.015, The ESCRT pathway.,
    Henne WM, Buchkovich NJ, Emr SD.. The complete review abstract summarizes MVB
    cargo delivery and membrane remodeling. This is synthesis, not a newly inspected
    primary remodeling assay.
  snapshot_sha256: 460a530ee4c6be779250900ab8aa406f9e827f57f923f35fbf21cc507303cb55
- evidence_id: root31-sources-katzmann2003-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/
  locator: Complete body sec4 Vps27 localization, sec5 ESCRT-I recruitment, sec6 interaction,
    sec12 plasmids/strains and sec13 microscopy, with captions; no original image
    pixels
  accessed_at: '2026-10-22T01:12:25.464014Z'
  support: supports
  summary: Genuine PMC2172707 complete sections4–6 and12–13 read with Fig2–4 captions.
    GFP-Vps27/PI3P colocalization and vps34/FYVE perturbations support endosomal recruitment;
    Vps23 recruitment depends on Vps27, and membrane-fraction coimmunoprecipitation
    supports their association. The strain table and microscopy methods were read.
    Species4932 is not used to infer S288C.
  snapshot_sha256: d4bc3fc8fd5cbf98c1b88722373dbd34c271f2df8da4bbb78d4f808dc7197233
- evidence_id: root31-sources-teo2004-primary-pdf
  kind: primary_source
  reference: https://www2.mrc-lmb.cam.ac.uk/groups/rlw/download/publications/15469844.pdf
  locator: Primary MRC-hosted PDF p559 summary/Introduction and pp564–567 Results/Conclusions/Methods,
    including Fig4–6 captions and pull-down/liposome protocols; no pixels or supplements
  accessed_at: '2026-10-22T01:12:25.464317Z'
  support: supports
  summary: Genuine primary PDF read at p559 and complete pp564–567. Purified Vps25
    binds Vps20 in reciprocal pulldowns; ESCRT-II or Vps25 increases Vps20 association
    with bovine-brain lipid vesicles. The5micromolar-protein sedimentation assay supports
    a recruitment step, not reconstitution of all ESCRT-III assembly/scission. Fig6
    membrane orientation remains a model.
  snapshot_sha256: 9a62830da92c7a92939524b134a277cf6381382e5539dfdfb47ab58e22817dce
- evidence_id: local-ilv
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
  locator: Full neighbor read; exact identifier, definition, hierarchy, graph and
    discussions
  accessed_at: '2026-10-22T02:01:16Z'
  support: context_only
  summary: The repository-minted identifier uniquely resolves to an intraluminal vesicle
    part of MVB. Reference resolution does not count this neighbor as another reviewed
    target.
- evidence_id: neighbor-late_endosome_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/late_endosome_lumen.yaml
  locator: Entire maintained neighbor read
  accessed_at: '2026-10-22T02:01:16Z'
  support: context_only
  summary: The exact boundary/localization terms are already maintained. Their availability
    is a bounded follow-up option; it does not refute the historical first-pass discussion
    or require a whole-membrane CURIE on lipid material.
- evidence_id: neighbor-late_endosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/late_endosome_membrane.yaml
  locator: Entire maintained neighbor read
  accessed_at: '2026-10-22T02:01:16Z'
  support: context_only
  summary: The exact boundary/localization terms are already maintained. Their availability
    is a bounded follow-up option; it does not refute the historical first-pass discussion
    or require a whole-membrane CURIE on lipid material.
- evidence_id: boundary-search
  kind: search
  reference: 'rg --no-ignore --hidden -n --glob *.yaml ^identifier: (GO:0031902|GO:0031906|cellstructuremech:multivesicular_body_intraluminal_vesicle)$
    data/structures'
  locator: Anchored exact identifier matches under data/structures
  accessed_at: '2026-10-22T01:56:58.215749Z'
  support: context_only
  summary: 'data/structures/membrane_organelle/late_endosome_lumen.yaml:1:identifier:
    GO:0031906

    data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml:1:identifier:
    cellstructuremech:multivesicular_body_intraluminal_vesicle

    data/structures/membrane_organelle/late_endosome_membrane.yaml:1:identifier: GO:0031902'
  search_scope: All data/structures YAML, including ignored and hidden files; anchored
    exact identifiers; positive matches only.
  snapshot_sha256: a4e573da0f5c166d1887ce1d98effcc4b83fe29eed2feb3bfaf79dc17da51e03
- evidence_id: root31-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-22T01:10:58.502766Z'
  support: supports
  summary: ENA4932 is Saccharomyces cerevisiae at species rank. Qualitative occurrence
    is not a measured prevalence or an exact experimental-strain determination.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome.yaml
    --verify
  locator: Entire retained focused native output
  accessed_at: '2026-10-22T01:51:17.218440Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/late_endosome.yaml
    --causal-graphs
  locator: Entire retained focused native output
  accessed_at: '2026-10-22T01:51:17.744595Z'
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
  reference: just validate data/structures/membrane_organelle/late_endosome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:50:44Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/late_endosome.yaml'
  snapshot_sha256: ca3f8cb08efdc2ae1ffe5125538285275bcc419bb434fa77b24c42ebc37a64ab
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/late_endosome.yaml
    --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:50:45Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/late_endosome.yaml\
    \ --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch31-20261022-ag46a4d4/late_endosome-strict.tsv"
  snapshot_sha256: 9d7e7d309c782ca74501c0b773561866d3879126f891ef613d5b9241f875f274
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/late_endosome.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '13 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent
    sorting into the multivesicular body pathway requires the function of a conserved
    endosomal protein sorting complex, ESCRT-I. Scientific scope remains limited to
    the separately documented inspections.; PMID:12194857: UNREACHABLE; The bulk transport
    returned414; the independently retrieved exact MED identity confirms PMID12194857,
    DOI10.1016/s1534-5807(02)00220-4 and Escrt-III: an endosome-associated heterooligomeric
    protein complex required for mvb sorting. Scientific scope remains limited to
    the separately documented inspections.; cellstructuremech:multivesicular_body_intraluminal_vesicle:
    SKIPPED; The repository-minted identifier uniquely resolves to the frozen maintained
    multivesicular body intraluminal vesicle record at data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml.
    An anchored hidden/ignored-inclusive corpus search and exact input hash confirm
    reference identity, not all biological assertions. Native source checks are separately
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
  topic: Exact structure and mereology
  outcome: supported
  target_ids:
  - GO:0005770
  summary: Native definitions and relations support the late endosome, its enclosing
    membrane and internal lumen as distinct structures/regions. MVB is a child example
    rather than a synonym for every late endosome.
  evidence_ids:
  - record
  - policy
  - root31-sources-go
  - neighbor-late_endosome_lumen
  - neighbor-late_endosome_membrane
  - boundary-search
  - root31-sources-katzmann2003-pmc
  - root31-sources-teo2004-primary-pdf
- assessment_id: composition
  area: grounding
  topic: Molecular material versus whole compartment
  outcome: supported
  target_ids:
  - GO:0005770
  summary: The LIPID row denotes collective boundary material and leaves exact molecular
    grounding unset. ESSENTIAL is the constitutive enclosing bilayer, not a requirement
    for each unspecified lipid species. The graph membrane node is distinct from the
    enclosed whole-organelle or lumen nodes.
  evidence_ids:
  - record
  - schema
  - root31-sources-go
  - root31-sources-katzmann2003-pmc
  - root31-sources-teo2004-primary-pdf
- assessment_id: formation-necessity
  area: grounding
  topic: Constitutive material versus experimental formation necessity
  outcome: unknown
  target_ids:
  - GO:0005770
  summary: The collective lipid bilayer is constitutive of the enclosed compartment
    or named membrane. The inspected ontology and recruitment/sorting sources do not
    test formation after removal of all lipid material, nor establish necessity of
    any individual lipid species or fixed mixture. Supported boundary composition
    remains distinct from experimentally demonstrated formation necessity.
  evidence_ids:
  - record
  - schema
  - root31-sources-go
  - root31-sources-katzmann2003-pmc
  - root31-sources-teo2004-primary-pdf
- assessment_id: scope
  area: scope
  topic: Taxon and actual experimental context
  outcome: supported
  target_ids:
  - GO:0005770
  summary: Yeast MVB experiments support a late-endosome child example. COMMON is
    qualitative occurrence. Transient ESCRT complexes are not listed as stable organelle
    constituents, and the sources are not generalized to every endosome or cargo class.
  evidence_ids:
  - record
  - root31-sources-tax4932
  - root31-sources-katzmann2001-meta
  - root31-sources-katzmann2003-meta
  - root31-sources-babst2002-meta
  - root31-sources-teo2004-meta
  - root31-sources-henne2011-meta
  - root31-sources-katzmann2003-pmc
  - root31-sources-teo2004-primary-pdf
- assessment_id: function
  area: evidence
  topic: Bounded functional evidence
  outcome: supported
  target_ids:
  - GO:0005770
  summary: GO0071985 and the yeast abstracts support cargo sorting into MVB luminal
    vesicles. Membrane sorting-surface and lumen receiving-space roles remain separate.
    Vps27 localization/recruitment is directly supported where cited.
  evidence_ids:
  - record
  - root31-sources-go
  - root31-sources-katzmann2001-meta
  - root31-sources-katzmann2003-meta
  - root31-sources-babst2002-meta
  - root31-sources-teo2004-meta
  - root31-sources-henne2011-meta
  - root31-sources-katzmann2003-pmc
  - root31-sources-teo2004-primary-pdf
- assessment_id: graph
  area: graph
  topic: Every target graph edge
  outcome: supported
  target_ids:
  - GO:0005770
  summary: 'All six NONMECHANISTIC edges have bounded support: enclosure, ESCRT-I
    sorting, ESCRT-II recruitment via Vps20, ESCRT-III remodeling from complex requirements
    plus review synthesis, inward budding and MVB containment. GO definitions support
    the last two. The remodeling edge is not attributed solely to the Babst abstract
    as an isolated force assay; no complete scission/recycling cycle is asserted.'
  evidence_ids:
  - record
  - root31-sources-go
  - root31-sources-katzmann2001-meta
  - root31-sources-katzmann2003-meta
  - root31-sources-babst2002-meta
  - root31-sources-teo2004-meta
  - root31-sources-henne2011-meta
  - root31-sources-katzmann2003-pmc
  - root31-sources-teo2004-primary-pdf
  - neighbor-late_endosome_lumen
  - neighbor-late_endosome_membrane
  - boundary-search
  - local-ilv
- assessment_id: limits
  area: evidence
  topic: Unresolved inventories and evidence tiers
  outcome: unknown
  target_ids:
  - GO:0005770
  summary: No complete molecular inventory, quantitative prevalence or isolated physical
    sufficiency experiment is established. Primary abstracts, selected primary-body
    sections and review synthesis retain distinct evidentiary roles.
  evidence_ids:
  - record
  - schema
  - root31-sources-go
  - root31-sources-katzmann2001-meta
  - root31-sources-katzmann2003-meta
  - root31-sources-babst2002-meta
  - root31-sources-teo2004-meta
  - root31-sources-henne2011-meta
  - root31-sources-katzmann2003-pmc
  - root31-sources-teo2004-primary-pdf
- assessment_id: discussion
  area: completeness
  topic: Historical first-pass grounding discussion
  outcome: supported
  target_ids:
  - GO:0005770
  summary: The OPEN note explicitly describes the first record and terms curated in
    that pass; it does not assert that exact late-specific terms do not exist. Verified
    membrane/lumen candidates make the optional node-grounding follow-up actionable.
    Their availability alone is not a defect, and whole-membrane identity must remain
    separate from unresolved lipid-material grounding.
  evidence_ids:
  - record
  - root31-sources-go
  - neighbor-late_endosome_lumen
  - neighbor-late_endosome_membrane
  - boundary-search
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and native status
  outcome: supported
  target_ids:
  - GO:0005770
  summary: Entire target, all graph edges, source placements, discussions and history
    inspected. No maintained image asset, numeric physical property, trait link, protein
    example or verbatim snippet is asserted. PROPOSED remains unchanged; historic
    issue closures are not independently recertified.
  evidence_ids:
  - record
  - policy
  - root31-sources-go
  - root31-sources-katzmann2001-meta
  - root31-sources-katzmann2003-meta
  - root31-sources-babst2002-meta
  - root31-sources-teo2004-meta
  - root31-sources-henne2011-meta
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- COMMON is qualitative occurrence, not measured prevalence. Historical authorship
  and earlier issue dispositions are not independently recertified.
- Katzmann2001 and, where cited, Babst2002 were read as complete primary abstracts
  only. They do not establish every physical mechanism or exact experimental genotype.
- Katzmann2003 body scope is complete sec4–6 and12–13, including captions; original
  pixels and remaining body sections were not inspected.
- Teo2004 genuine primary PDF scope is p559 and complete pp564–567 with captions/methods.
  Other structural-analysis sections, pixels and supplements were not inspected. Henne2011
  is a review whose complete abstract was read, not a newly inspected primary remodeling
  assay.
- The linked ILV record was read for exact reference resolution and relevant containment,
  not counted as another reviewed target. Exact late-endosome membrane/lumen node
  groundings remain optional follow-up candidates, distinct from ungrounded lipid
  material.
- The collective lipid ESSENTIAL row is interpreted at its constitutive material scope;
  experimental formation necessity was not established by the inspected sources.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorizes bundles for every uncovered record, including honest
  no-finding reviews. Scientific content remains unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
