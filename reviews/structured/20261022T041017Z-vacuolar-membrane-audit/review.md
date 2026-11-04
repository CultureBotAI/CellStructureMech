# Vacuolar membrane scientific review

- Review: 20261022T041017Z-vacuolar-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:46:47Z
- Finished UTC: 2026-10-22T04:10:17Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact membrane identity, collective bilayer, two yeast graph protein identities, acidification direction and nuclear-vacuolar contact function are supported. No concrete curation finding; formation and source-assay limits remain explicit.

## Scope And Provenance

Exactly one complete target plus the two frozen generic vacuole boundary neighbors; all evidence and graph assertions checked. Native and literature scopes are declared per source. No scientific edits, record promotion, review save or publication.

Selection: Batch42 exact path-ordered target 3; initial native inspect/schema/strict passed on fresh f97b before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005774 | data/structures/membrane_organelle/vacuolar_membrane.yaml | maintained | vacuolar membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005774 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005774 | Focused validator passed. |
| Native verify | passed | True | GO:0005774 | Native read-only check passed; biological source scope was reviewed separately. |
| Native causal-graphs | passed | True | GO:0005774 | Native read-only check passed; biological source scope was reviewed separately. |
| Expression-module applicability | not_applicable | False | GO:0005774 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0005774 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005774 | 13 of 13 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005774 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005774 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005774 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005774 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005774 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Whole organelle, membrane and volume

identity: supported. Targets: GO:0005774.

The exact maintained identity, structural kind and relations are supported by native GO and the full local boundary set. Fungal subtype relationships, where represented, are checked as proper subtypes rather than equated to the generic class. No synonym or exact-identity substitution is needed.

### Yeast example within a generic class

scope: supported. Targets: GO:0005774.

The species and canonical example are supported by the explicitly yeast-focused review. The current occurrence rows are limited to S. cerevisiae, preserving the distinction between a generic ontology class and its experimentally characterized model example.

### Collective bilayer material versus functional actors

grounding: supported. Targets: GO:0005774.

The LIPID row is explicitly REVIEWED_LABEL_ONLY and avoids assigning a whole-membrane GO identifier as a chemical identity. The membrane node may refer to this collective bilayer material. The resolved discussion reasonably keeps yeast V-ATPase/Vac8 functional participants separate from a universal vacuolar-membrane constituent cohort.

### Individual formation requirements remain unresolved

evidence: unknown. Targets: GO:0005774.

The ESSENTIAL row concerns the complete constituting bilayer. No exact lipid species or individual protein is demonstrated necessary for formation of every vacuolar membrane. Pan specifically separates junction formation from vacuole biogenesis; the review does not reinterpret functional acidification or binding as generic membrane-formation necessity.

### Two correct graph accessions

grounding: supported. Targets: GO:0005774.

Both xrefs identify the intended yeast proteins, with the expected genes and source-linked locations. Native taxon559292 is a reference strain within the record species4932; Pan strain names remain distinct. No present protein_example row incorrectly pairs a species label with the strain identifier.

### Acidification and membrane contact at yeast scope

graph: supported. Targets: GO:0005774.

The eight NONMECHANISTIC edges preserve topology, V-ATPase residence and proton-pumping direction, and Vac8/Nvj1 contact formation. Pan supports the authors direct-interaction interpretation using two-hybrid/copurification and localization, with the assay limit retained. The record does not require the contact factors for all vacuole biogenesis.

### Historical grounding work and remaining questions

completeness: supported. Targets: GO:0005774.

The OPEN discussion predates the later graph-xref addition and explicitly says this pass did not verify exact identifiers. Current graph accessions are correct and separately verified here; exact lipid/family grounding and the universal constituent question remain unresolved. The historical qualifier is not treated as a current claim that UniProt identifiers do not exist, and no forced closure or duplicate finding is imposed.

### Complete target and bounded source audit

provenance: supported. Targets: GO:0005774.

All current fields, graph relations and discussions were read. Evidence distinguishes primary Pan experiments, secondary reviews and native authorities; optional unknown inventories are not treated as mandatory defects. No maintained record or scientific status was changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/vacuolar_membrane.yaml; Entire maintained target including all fields, evidence, graphs, discussions and history | context_only | Every current claim was read; historical curation notes are not independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, essentiality, graph-node and evidence contracts | context_only | A whole compartment, its bounding membrane and enclosed volume are distinct. Constitutive material, functional activity and experimental formation necessity must not be conflated. |
| neighbor-vacuolar_lumen | data/structures/membrane_organelle/vacuolar_lumen.yaml; Entire frozen boundary neighbor | context_only | The complete three-record vacuole boundary set (target plus two neighbors) was read. Neighbor prose supplies local context, not independent experimental support. |
| neighbor-vacuole | data/structures/membrane_organelle/vacuole.yaml; Entire frozen boundary neighbor | context_only | The complete three-record vacuole boundary set (target plus two neighbors) was read. Neighbor prose supplies local context, not independent experimental support. |
| vacuole-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005773,GO:0005774,GO:0005775,GO:0070013,GO:0031090,GO:0043231,GO:0000324,GO:0000328,GO:0000329,GO:0016471,GO:0007035,GO:0005640; Complete target identity/definition/active status and named relation-bearing entries in the twelve-term response; unrelated child lists not exhaustively interpreted | supports | Active GO0005774 exactly defines the surrounding bilayer separating vacuolar contents from cytoplasm; GO0005773 lists it as part_of. GO0016471 is the vacuolar proton-pumping complex and is listed as part_of GO0005774. GO0007035 explicitly lowers pH by increasing hydrogen-ion concentration. GO0005640 is the cytoplasm-facing nuclear outer bilayer. |
| vacuole-agent-go-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005774,GO:0000324,GO:0000329,GO:0000328/ancestors?relations=is_a; Complete four is_a-only ancestor lists for GO0005774, GO0000324, GO0000329 and GO0000328 | supports | The is_a-only response confirms vacuolar membrane GO0005774 under organelle membrane GO0031090, and the three fungal-type classes under their respective generic vacuole/membrane/lumen classes. Some are transitive rather than immediate edges; parthood is checked separately in the term response. |
| vacuole-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId, scientificName, rank and lineage | supports | ENA4932 verifies Saccharomyces cerevisiae at species rank and its fungal lineage. It does not establish frequency, strain identity or universal vacuolar physiology across Eukaryota. |
| vacuole-agent-li2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/j.bbamcr.2008.08.003%22; Unique native MED title/authors/DOI/PMID/PMC/year and complete abstract | supports | Exact secondary source identity: Li SC and Kane PM, The yeast lysosome-like vacuole: endpoint and crossroads; DOI10.1016/j.bbamcr.2008.08.003, PMID18786576, PMC2906225, published2009. The complete abstract explicitly frames a review of S. cerevisiae vacuole biology. |
| vacuole-agent-li2009-numeric | https://pmc.ncbi.nlm.nih.gov/articles/2906225/; Genuine PMC2906225 review HTML: complete S1 Introduction, S3 protein content, S4 membrane lipids, S16 V-ATPase acidification including Figure3 caption, S20 degradation and S21 storage/homeostasis. Other sections, figure pixels and underlying cited experiments not independently audited for this review. | supports | The review describes acidic yeast vacuoles with proteolytic, storage and homeostatic functions, distinguishes luminal proteins from membrane/cargo inventories, and describes V-ATPase proton pumping. It notes degradation can retain appreciable activity without full acidification and that particular fusion-regulatory lipids are not synonymous with an entire formation requirement. Storage includes amino acids, phosphate and ions; no universal cargo or membrane composition is imposed. |
| uniprot-skill | .claude/skills/uniprot-protein-examples/SKILL.md; Identity, taxon, source-role and graph-xref verification requirements | context_only | Both graph protein identifiers are verified individually; a reference-strain accession does not automatically identify the experimental strain or establish all annotated functions. |
| vacuole-agent-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxId, scientificName, rank and lineage | supports | ENA559292 is Saccharomyces cerevisiae S288C at strain rank. This is the native taxon of the graph protein accessions, not a claim that Pan experiments used S288C. |
| vacuole-agent-kane2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1128/MMBR.70.1.177-191.2006%22; Unique native MED identity and complete abstract | supports | Exact review identity: Kane PM, The where, when, and how of organelle acidification by the yeast vacuolar H+-ATPase; DOI10.1128/MMBR.70.1.177-191.2006, PMID16524922, PMC1393255. Complete abstract distinguishes structure, assembly, transport and regulated acidification. |
| vacuole-agent-kane2006-numeric | https://pmc.ncbi.nlm.nih.gov/articles/1393255/; Genuine PMC1393255 review HTML: complete sec1 Introduction, sec3 structure including Figure1 caption, sec4 catalytic mechanism, and sec11 a-subunit localization. Other sections, pixels and cited primary experiments not independently audited. | supports | The review describes ATP-driven proton movement from cytosol into acidic organelles, membrane V0 and peripheral V1 sectors, and Vph1/Stv1 localization differences. Vph1 normally targets the vacuole while Stv1 favors Golgi/endosomes with conditional redistribution. This supports proton-pumping direction and compartment context, not a universal subunit inventory for every vacuolar membrane. |
| vacuole-agent-pan2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091/mbc.11.7.2445%22&amp;format=json&amp;resultType=core; Unique native MED authors/title/DOI/PMID/PMC/year and complete primary abstract | supports | Exact primary identity: Pan X etal2000, Nucleus-vacuole junctions in Saccharomyces cerevisiae are formed through the direct interaction of Vac8p with Nvj1p; DOI10.1091/mbc.11.7.2445, PMID10888680, PMC14931. |
| vacuole-agent-pan2000-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC14931/; Genuine PMC14931 primary HTML: complete Methods sec3 strain/plasmid/growth and sec4 affinity chromatography; Results sec11–15 (interaction, fractionation, binding region, biogenesis tests and localization), associated Figures1–7 captions, and Discussion sec19. No other sections, figure pixels or supplemental material independently inspected. | supports | Two-hybrid, affinity copurification, membrane fractionation and localization/deletion experiments support Vac8-Nvj1 complexes at nuclear-vacuolar contacts. Nvj1 is a nuclear-envelope integral membrane protein and Vac8 is lipid-anchored at the vacuole. C-terminal Nvj1 residues mediate binding; loss of NVJ1 does not abolish vacuole biogenesis. Authors infer direct interaction while acknowledging a remote indirect-interaction possibility in sec11. Methods use YEF473 derivatives and L40 rather than an asserted S288C identity. |
| vacuole-agent-protein-P39968 | https://rest.uniprot.org/uniprotkb/P39968.json; Exact accession/entryType/name/gene/locus/organism fields and function/subunit/location comments; no sequence or complete bibliography analysis | supports | Current reviewed P39968 is Vacuolar protein8, gene VAC8/YEB3, locus YEL013W, taxon559292. Native comments specifically cite PMID10888680 for junction function, NVJ1 interaction and vacuolar-membrane localization. It is the correct graph identity, not evidence of experimental strain equivalence. |
| vacuole-agent-protein-P38881 | https://rest.uniprot.org/uniprotkb/P38881.json; Exact accession/entryType/name/gene/locus/organism fields and function/subunit/location comments; no sequence or complete bibliography analysis | supports | Current reviewed P38881 is Nucleus-vacuole junction protein1, gene NVJ1/VAB36, locus YHR195W, taxon559292. Native comments cite PMID10888680 for VAC8 interaction and nuclear-outer-membrane localization. This is the correct graph identity. |
| schema-result | just validate data/structures/membrane_organelle/vacuolar_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/vacuolar_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/vacuolar_membrane.yaml --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/vacuolar_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/vacuolar_membrane.yaml --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/vacuolar_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch42-20261022-q4522lvm/vacuolar_membrane-strict.tsv |
| native-verify | /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/vacuolar_membrane.yaml; Complete native read-only log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/vacuolar_membrane.yaml; Complete native read-only log | supports | data/structures/membrane_organelle/vacuolar_membrane.yaml  (GO:0005774)<br>  yeast_vacuolar_membrane_functions	vac8p	UNANCHORED_WITH_UNIPROT	Vac8p (UniProtKB:P39968)<br>  yeast_vacuolar_membrane_functions	nvj1p	UNANCHORED_WITH_UNIPROT	Nvj1p (UniProtKB:P38881)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/vacuolar_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 13 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- The Li/Kane2009 and, where used, Kane2006 sources are reviews, not newly performed primary experiments. Exact inspected sections are declared in their evidence rows. No image pixels, supplemental datasets, complete source bibliographies or underlying cited experiments were independently reanalyzed.
- COMMON is a qualitative species occurrence designation. Yeast functional examples do not establish identical physiology, cargo or protein composition for every eukaryotic vacuole. Native generic ontology identity remains broader than the yeast example.
- The complete generic vacuole boundary set was read. Optional inventories of soluble cargo, all transporters, hydrolases, lipid species or exact stoichiometry are not required to establish a broad compartment, volume or membrane identity.
- Pan2000 has the precise bounded primary-body scope listed above. It uses YEF473-derived and L40 strains; the native S288C accessions verify protein identity, not strain equivalence or a sequence-level comparison across all experimental backgrounds.
- Pan sec11 explicitly allows a remote possibility of indirect interaction despite the paper title and authors direct-binding model. No purified two-protein binding experiment, binding affinity or complete junction machinery is newly certified here.
- The historical OPEN grounding rationale predates verified graph xrefs. Remaining exact lipid/family questions can stay open; this review does not certify that no candidate chemical or family authority exists.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes clean review bundles. Parent owns finalization and integration of the five completed same-base batch26 full-corpus gates.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T041017Z-vacuolar-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Vacuolar membrane scientific review
started_at: '2026-10-22T03:46:47Z'
finished_at: '2026-10-22T04:10:17Z'
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
summary: Exact membrane identity, collective bilayer, two yeast graph protein identities,
  acidification direction and nuclear-vacuolar contact function are supported. No
  concrete curation finding; formation and source-assay limits remain explicit.
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
  - path: data/structures/membrane_organelle/vacuolar_lumen.yaml
    sha256: c766d7de82bee8cf8d6f5c34f61cc41a7150e65686ba387255061a9449106b73
    role: context
  - path: data/structures/membrane_organelle/vacuolar_membrane.yaml
    sha256: 89c3bb9baf5507b45606c975ff1bb6ef8d705601ce44bc7e4c3d72572b5f36e0
    role: target
  - path: data/structures/membrane_organelle/vacuole.yaml
    sha256: 7db6bf4c90e74fed8acf83d164143fe3ef294c46012b631a01c1d241f05f370d
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
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0005774
  path: data/structures/membrane_organelle/vacuolar_membrane.yaml
  label: vacuolar membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/vacuolar_membrane.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target plus the two frozen generic vacuole boundary
    neighbors; all evidence and graph assertions checked. Native and literature scopes
    are declared per source. No scientific edits, record promotion, review save or
    publication.
  selection: Batch42 exact path-ordered target 3; initial native inspect/schema/strict
    passed on fresh f97b before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005774
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005774
  command: just validate data/structures/membrane_organelle/vacuolar_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005774
  command: just validate-strict data/structures/membrane_organelle/vacuolar_membrane.yaml
    --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/vacuolar_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0005774
  command: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/vacuolar_membrane.yaml
  exit_code: 0
  summary: Native read-only check passed; biological source scope was reviewed separately.
  evidence_ids:
  - native-verify
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005774
  command: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/vacuolar_membrane.yaml
  exit_code: 0
  summary: Native read-only check passed; biological source scope was reviewed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005774
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005774
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-vacuolar_lumen
  - neighbor-vacuole
  - vacuole-agent-go
  - vacuole-agent-go-ancestors
  - vacuole-agent-tax4932
  - vacuole-agent-li2009-meta
  - vacuole-agent-li2009-numeric
  - uniprot-skill
  - vacuole-agent-tax559292
  - vacuole-agent-kane2006-meta
  - vacuole-agent-kane2006-numeric
  - vacuole-agent-pan2000-meta
  - vacuole-agent-pan2000-pmc
  - vacuole-agent-protein-P39968
  - vacuole-agent-protein-P38881
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005774
  summary: 13 of 13 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005774
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005774
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005774
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005774
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005774
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
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/vacuolar_membrane.yaml
  locator: Entire maintained target including all fields, evidence, graphs, discussions
    and history
  accessed_at: '2026-10-22T03:51:00Z'
  support: context_only
  summary: Every current claim was read; historical curation notes are not independent
    scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, essentiality, graph-node and evidence contracts
  accessed_at: '2026-10-22T03:51:00Z'
  support: context_only
  summary: A whole compartment, its bounding membrane and enclosed volume are distinct.
    Constitutive material, functional activity and experimental formation necessity
    must not be conflated.
- evidence_id: neighbor-vacuolar_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/vacuolar_lumen.yaml
  locator: Entire frozen boundary neighbor
  accessed_at: '2026-10-22T03:51:00Z'
  support: context_only
  summary: The complete three-record vacuole boundary set (target plus two neighbors)
    was read. Neighbor prose supplies local context, not independent experimental
    support.
- evidence_id: neighbor-vacuole
  kind: record_content
  reference: data/structures/membrane_organelle/vacuole.yaml
  locator: Entire frozen boundary neighbor
  accessed_at: '2026-10-22T03:51:00Z'
  support: context_only
  summary: The complete three-record vacuole boundary set (target plus two neighbors)
    was read. Neighbor prose supplies local context, not independent experimental
    support.
- evidence_id: vacuole-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005773,GO:0005774,GO:0005775,GO:0070013,GO:0031090,GO:0043231,GO:0000324,GO:0000328,GO:0000329,GO:0016471,GO:0007035,GO:0005640
  locator: Complete target identity/definition/active status and named relation-bearing
    entries in the twelve-term response; unrelated child lists not exhaustively interpreted
  accessed_at: '2026-10-22T03:48:14.151533Z'
  support: supports
  summary: Active GO0005774 exactly defines the surrounding bilayer separating vacuolar
    contents from cytoplasm; GO0005773 lists it as part_of. GO0016471 is the vacuolar
    proton-pumping complex and is listed as part_of GO0005774. GO0007035 explicitly
    lowers pH by increasing hydrogen-ion concentration. GO0005640 is the cytoplasm-facing
    nuclear outer bilayer.
  snapshot_sha256: 936b23d01730645443fb47deb3a7a2480db5363d005460cb31866aa92cbefe87
- evidence_id: vacuole-agent-go-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005774,GO:0000324,GO:0000329,GO:0000328/ancestors?relations=is_a
  locator: Complete four is_a-only ancestor lists for GO0005774, GO0000324, GO0000329
    and GO0000328
  accessed_at: '2026-10-22T03:49:13.745402Z'
  support: supports
  summary: The is_a-only response confirms vacuolar membrane GO0005774 under organelle
    membrane GO0031090, and the three fungal-type classes under their respective generic
    vacuole/membrane/lumen classes. Some are transitive rather than immediate edges;
    parthood is checked separately in the term response.
  snapshot_sha256: 9a043cf51a611fe10deb5f596d5f5bc5beef5d2f9dc9ba5493b53f896d3634c0
- evidence_id: vacuole-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T03:48:14.151924Z'
  support: supports
  summary: ENA4932 verifies Saccharomyces cerevisiae at species rank and its fungal
    lineage. It does not establish frequency, strain identity or universal vacuolar
    physiology across Eukaryota.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: vacuole-agent-li2009-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.bbamcr.2008.08.003%22
  locator: Unique native MED title/authors/DOI/PMID/PMC/year and complete abstract
  accessed_at: '2026-10-22T01:31:22.508649Z'
  support: supports
  summary: 'Exact secondary source identity: Li SC and Kane PM, The yeast lysosome-like
    vacuole: endpoint and crossroads; DOI10.1016/j.bbamcr.2008.08.003, PMID18786576,
    PMC2906225, published2009. The complete abstract explicitly frames a review of
    S. cerevisiae vacuole biology.'
  snapshot_sha256: a80dfab6ca988c4f031b90afb9ca5816e91805513281ba402d81aad11ac0142e
- evidence_id: vacuole-agent-li2009-numeric
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/2906225/
  locator: 'Genuine PMC2906225 review HTML: complete S1 Introduction, S3 protein content,
    S4 membrane lipids, S16 V-ATPase acidification including Figure3 caption, S20
    degradation and S21 storage/homeostasis. Other sections, figure pixels and underlying
    cited experiments not independently audited for this review.'
  accessed_at: '2026-10-22T01:32:07.202194Z'
  support: supports
  summary: The review describes acidic yeast vacuoles with proteolytic, storage and
    homeostatic functions, distinguishes luminal proteins from membrane/cargo inventories,
    and describes V-ATPase proton pumping. It notes degradation can retain appreciable
    activity without full acidification and that particular fusion-regulatory lipids
    are not synonymous with an entire formation requirement. Storage includes amino
    acids, phosphate and ions; no universal cargo or membrane composition is imposed.
  snapshot_sha256: 949eb84ba53fa6400a1c205d2459f909e323b5f8eeb58e3672234730830c256b
- evidence_id: uniprot-skill
  kind: record_content
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Identity, taxon, source-role and graph-xref verification requirements
  accessed_at: '2026-10-22T03:51:00Z'
  support: context_only
  summary: Both graph protein identifiers are verified individually; a reference-strain
    accession does not automatically identify the experimental strain or establish
    all annotated functions.
- evidence_id: vacuole-agent-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T03:48:14.152174Z'
  support: supports
  summary: ENA559292 is Saccharomyces cerevisiae S288C at strain rank. This is the
    native taxon of the graph protein accessions, not a claim that Pan experiments
    used S288C.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: vacuole-agent-kane2006-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1128/MMBR.70.1.177-191.2006%22
  locator: Unique native MED identity and complete abstract
  accessed_at: '2026-10-22T01:31:22.576024Z'
  support: supports
  summary: 'Exact review identity: Kane PM, The where, when, and how of organelle
    acidification by the yeast vacuolar H+-ATPase; DOI10.1128/MMBR.70.1.177-191.2006,
    PMID16524922, PMC1393255. Complete abstract distinguishes structure, assembly,
    transport and regulated acidification.'
  snapshot_sha256: 61b77e1e74943bfce906bd49ed525db7b02ead05cea30b802740df4dcbdf1ed4
- evidence_id: vacuole-agent-kane2006-numeric
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/1393255/
  locator: 'Genuine PMC1393255 review HTML: complete sec1 Introduction, sec3 structure
    including Figure1 caption, sec4 catalytic mechanism, and sec11 a-subunit localization.
    Other sections, pixels and cited primary experiments not independently audited.'
  accessed_at: '2026-10-22T01:32:07.202322Z'
  support: supports
  summary: The review describes ATP-driven proton movement from cytosol into acidic
    organelles, membrane V0 and peripheral V1 sectors, and Vph1/Stv1 localization
    differences. Vph1 normally targets the vacuole while Stv1 favors Golgi/endosomes
    with conditional redistribution. This supports proton-pumping direction and compartment
    context, not a universal subunit inventory for every vacuolar membrane.
  snapshot_sha256: 20b0e18976d5c76dee0ae4e1d58559f54fa8e2b6409bc902ac708c5e1654e1bd
- evidence_id: vacuole-agent-pan2000-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091/mbc.11.7.2445%22&format=json&resultType=core
  locator: Unique native MED authors/title/DOI/PMID/PMC/year and complete primary
    abstract
  accessed_at: '2026-10-22T02:39:01.003242Z'
  support: supports
  summary: 'Exact primary identity: Pan X etal2000, Nucleus-vacuole junctions in Saccharomyces
    cerevisiae are formed through the direct interaction of Vac8p with Nvj1p; DOI10.1091/mbc.11.7.2445,
    PMID10888680, PMC14931.'
  snapshot_sha256: 8fd13375de562999edc00fab8fd5103111b6f6e00b90719774f0bf6f17fa1fe6
- evidence_id: vacuole-agent-pan2000-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC14931/
  locator: 'Genuine PMC14931 primary HTML: complete Methods sec3 strain/plasmid/growth
    and sec4 affinity chromatography; Results sec11–15 (interaction, fractionation,
    binding region, biogenesis tests and localization), associated Figures1–7 captions,
    and Discussion sec19. No other sections, figure pixels or supplemental material
    independently inspected.'
  accessed_at: '2026-10-22T02:39:21.042109Z'
  support: supports
  summary: Two-hybrid, affinity copurification, membrane fractionation and localization/deletion
    experiments support Vac8-Nvj1 complexes at nuclear-vacuolar contacts. Nvj1 is
    a nuclear-envelope integral membrane protein and Vac8 is lipid-anchored at the
    vacuole. C-terminal Nvj1 residues mediate binding; loss of NVJ1 does not abolish
    vacuole biogenesis. Authors infer direct interaction while acknowledging a remote
    indirect-interaction possibility in sec11. Methods use YEF473 derivatives and
    L40 rather than an asserted S288C identity.
  snapshot_sha256: 21ca47f90e10c08bef74688b1d99cb48079becd20b5613d7fc569a70de30001c
- evidence_id: vacuole-agent-protein-P39968
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39968.json
  locator: Exact accession/entryType/name/gene/locus/organism fields and function/subunit/location
    comments; no sequence or complete bibliography analysis
  accessed_at: '2026-10-22T03:48:14.152118Z'
  support: supports
  summary: Current reviewed P39968 is Vacuolar protein8, gene VAC8/YEB3, locus YEL013W,
    taxon559292. Native comments specifically cite PMID10888680 for junction function,
    NVJ1 interaction and vacuolar-membrane localization. It is the correct graph identity,
    not evidence of experimental strain equivalence.
  snapshot_sha256: 8717485852a2be10a3d083ada88ed1cbbfbfe2a8ac02095c565a428ad14a6be8
- evidence_id: vacuole-agent-protein-P38881
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38881.json
  locator: Exact accession/entryType/name/gene/locus/organism fields and function/subunit/location
    comments; no sequence or complete bibliography analysis
  accessed_at: '2026-10-22T03:48:14.152228Z'
  support: supports
  summary: Current reviewed P38881 is Nucleus-vacuole junction protein1, gene NVJ1/VAB36,
    locus YHR195W, taxon559292. Native comments cite PMID10888680 for VAC8 interaction
    and nuclear-outer-membrane localization. This is the correct graph identity.
  snapshot_sha256: 4e3daf10d4a641ffad9c2e3c2850dd073e2a69da5e833626c484de0d5807b86b
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/vacuolar_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:46:49Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/vacuolar_membrane.yaml'
  snapshot_sha256: 0803439c03bdece8160a23161e3107358abc02bb0f8c2da3464b57c54b9e700b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/vacuolar_membrane.yaml
    --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/vacuolar_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:46:50Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/vacuolar_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/vacuolar_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch42-20261022-q4522lvm/vacuolar_membrane-strict.tsv"
  snapshot_sha256: 0fdb6e54c23a8a13495d3fd654e9409611ff2cb399146f4f06b076bb93dbb690
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/vacuolar_membrane.yaml
  locator: Complete native read-only log
  accessed_at: '2026-10-22T03:49:33.800895Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/vacuolar_membrane.yaml
  locator: Complete native read-only log
  accessed_at: '2026-10-22T03:49:17.916127Z'
  support: supports
  summary: "data/structures/membrane_organelle/vacuolar_membrane.yaml  (GO:0005774)\n\
    \  yeast_vacuolar_membrane_functions\tvac8p\tUNANCHORED_WITH_UNIPROT\tVac8p (UniProtKB:P39968)\n\
    \  yeast_vacuolar_membrane_functions\tnvj1p\tUNANCHORED_WITH_UNIPROT\tNvj1p (UniProtKB:P38881)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     2  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ COVERED                   component_ref target holds protein_examples covering\
    \ all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref target\
    \ holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 92aaaf1ac430136910645f50210f00c60fdada7e3d185ffd76c059deb34026eb
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/vacuolar_membrane.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 13 of 13 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
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
  topic: Whole organelle, membrane and volume
  outcome: supported
  target_ids:
  - GO:0005774
  summary: The exact maintained identity, structural kind and relations are supported
    by native GO and the full local boundary set. Fungal subtype relationships, where
    represented, are checked as proper subtypes rather than equated to the generic
    class. No synonym or exact-identity substitution is needed.
  evidence_ids:
  - record
  - vacuole-agent-go
  - vacuole-agent-go-ancestors
- assessment_id: taxonomy
  area: scope
  topic: Yeast example within a generic class
  outcome: supported
  target_ids:
  - GO:0005774
  summary: The species and canonical example are supported by the explicitly yeast-focused
    review. The current occurrence rows are limited to S. cerevisiae, preserving the
    distinction between a generic ontology class and its experimentally characterized
    model example.
  evidence_ids:
  - record
  - vacuole-agent-tax4932
  - vacuole-agent-li2009-meta
  - vacuole-agent-li2009-numeric
- assessment_id: composition
  area: grounding
  topic: Collective bilayer material versus functional actors
  outcome: supported
  target_ids:
  - GO:0005774
  summary: The LIPID row is explicitly REVIEWED_LABEL_ONLY and avoids assigning a
    whole-membrane GO identifier as a chemical identity. The membrane node may refer
    to this collective bilayer material. The resolved discussion reasonably keeps
    yeast V-ATPase/Vac8 functional participants separate from a universal vacuolar-membrane
    constituent cohort.
  evidence_ids:
  - record
  - schema
  - vacuole-agent-go
  - vacuole-agent-li2009-numeric
- assessment_id: formation
  area: evidence
  topic: Individual formation requirements remain unresolved
  outcome: unknown
  target_ids:
  - GO:0005774
  summary: The ESSENTIAL row concerns the complete constituting bilayer. No exact
    lipid species or individual protein is demonstrated necessary for formation of
    every vacuolar membrane. Pan specifically separates junction formation from vacuole
    biogenesis; the review does not reinterpret functional acidification or binding
    as generic membrane-formation necessity.
  evidence_ids:
  - record
  - schema
  - vacuole-agent-li2009-numeric
  - vacuole-agent-pan2000-pmc
- assessment_id: proteins
  area: grounding
  topic: Two correct graph accessions
  outcome: supported
  target_ids:
  - GO:0005774
  summary: Both xrefs identify the intended yeast proteins, with the expected genes
    and source-linked locations. Native taxon559292 is a reference strain within the
    record species4932; Pan strain names remain distinct. No present protein_example
    row incorrectly pairs a species label with the strain identifier.
  evidence_ids:
  - record
  - vacuole-agent-protein-P39968
  - vacuole-agent-protein-P38881
  - vacuole-agent-tax559292
  - vacuole-agent-pan2000-meta
  - vacuole-agent-pan2000-pmc
- assessment_id: function-graph
  area: graph
  topic: Acidification and membrane contact at yeast scope
  outcome: supported
  target_ids:
  - GO:0005774
  summary: The eight NONMECHANISTIC edges preserve topology, V-ATPase residence and
    proton-pumping direction, and Vac8/Nvj1 contact formation. Pan supports the authors
    direct-interaction interpretation using two-hybrid/copurification and localization,
    with the assay limit retained. The record does not require the contact factors
    for all vacuole biogenesis.
  evidence_ids:
  - record
  - vacuole-agent-go
  - vacuole-agent-li2009-numeric
  - vacuole-agent-kane2006-numeric
  - vacuole-agent-pan2000-pmc
  - vacuole-agent-protein-P39968
  - vacuole-agent-protein-P38881
- assessment_id: discussion
  area: completeness
  topic: Historical grounding work and remaining questions
  outcome: supported
  target_ids:
  - GO:0005774
  summary: The OPEN discussion predates the later graph-xref addition and explicitly
    says this pass did not verify exact identifiers. Current graph accessions are
    correct and separately verified here; exact lipid/family grounding and the universal
    constituent question remain unresolved. The historical qualifier is not treated
    as a current claim that UniProt identifiers do not exist, and no forced closure
    or duplicate finding is imposed.
  evidence_ids:
  - record
  - vacuole-agent-go
  - vacuole-agent-protein-P39968
  - vacuole-agent-protein-P38881
  - vacuole-agent-pan2000-pmc
- assessment_id: coverage
  area: provenance
  topic: Complete target and bounded source audit
  outcome: supported
  target_ids:
  - GO:0005774
  summary: All current fields, graph relations and discussions were read. Evidence
    distinguishes primary Pan experiments, secondary reviews and native authorities;
    optional unknown inventories are not treated as mandatory defects. No maintained
    record or scientific status was changed.
  evidence_ids:
  - record
  - vacuole-agent-go
  - vacuole-agent-tax4932
  - vacuole-agent-li2009-meta
  - vacuole-agent-li2009-numeric
findings: []
actions: []
limitations:
- The Li/Kane2009 and, where used, Kane2006 sources are reviews, not newly performed
  primary experiments. Exact inspected sections are declared in their evidence rows.
  No image pixels, supplemental datasets, complete source bibliographies or underlying
  cited experiments were independently reanalyzed.
- COMMON is a qualitative species occurrence designation. Yeast functional examples
  do not establish identical physiology, cargo or protein composition for every eukaryotic
  vacuole. Native generic ontology identity remains broader than the yeast example.
- The complete generic vacuole boundary set was read. Optional inventories of soluble
  cargo, all transporters, hydrolases, lipid species or exact stoichiometry are not
  required to establish a broad compartment, volume or membrane identity.
- Pan2000 has the precise bounded primary-body scope listed above. It uses YEF473-derived
  and L40 strains; the native S288C accessions verify protein identity, not strain
  equivalence or a sequence-level comparison across all experimental backgrounds.
- Pan sec11 explicitly allows a remote possibility of indirect interaction despite
  the paper title and authors direct-binding model. No purified two-protein binding
  experiment, binding affinity or complete junction machinery is newly certified here.
- The historical OPEN grounding rationale predates verified graph xrefs. Remaining
  exact lipid/family questions can stay open; this review does not certify that no
  candidate chemical or family authority exists.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes clean review bundles. Parent owns finalization and
  integration of the five completed same-base batch26 full-corpus gates.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
