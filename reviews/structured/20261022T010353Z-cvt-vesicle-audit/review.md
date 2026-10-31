# Cvt structure identity, membrane boundaries and source review

- Review: 20261022T010353Z-cvt-vesicle-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T11:20:43Z
- Finished UTC: 2026-10-22T01:03:53Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The Cvt carrier identity, membrane/cargo boundaries and selective transport context are supported at the declared source scopes. No concrete curation finding was established.

## Scope And Provenance

Entire single maintained target, exact authority identities, species/source contexts, all component/formation boundaries and every graph edge.

Selection: Target 1 in batch twenty-five, selected by native uncovered path order at frozen revision9c0446.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033107 | data/structures/membrane_organelle/cvt_vesicle.yaml | maintained | Cvt vesicle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0033107 | Focused validator passed. |
| Focused native strict | passed | True | GO:0033107 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0033107 | 11 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Focused native verify | passed | True | GO:0033107 | Native check passed. The target has no explicit protein accessions or GENE_OR_PROTEIN graph nodes; this does not independently prove biological membership. |
| Focused native causal-graphs | passed | True | GO:0033107 | Native check passed. The target has no explicit protein accessions or GENE_OR_PROTEIN graph nodes; this does not independently prove biological membership. |
| Expression-module applicability | not_applicable | False | GO:0033107 | No expression-module, regulator-network or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | GO:0033107 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0033107 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0033107 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0033107 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0033107 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0033107 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Carrier, lumen and individual surrounding bilayer remain distinct

identity: supported. Targets: GO:0033107.

The target identifies the stated structure or enclosed region rather than the Cvt cargo protein complex, an individual Atg protein or the pathway itself. Native GO and UniProt definitions support the asserted hierarchy and parthood. Either-bilayer language preserves the double-membrane carrier; it does not collapse both membranes into one bilayer. The mature cargo-containing interior is distinguished from the inner vesicle released after fusion and from the intermembrane space.

### Budding-yeast model and conditional experimental context

scope: supported. Targets: GO:0033107.

The species identity and canonical budding-yeast context are supported by Reggiori strains and experiments. COMMON is a qualitative occurrence statement, not a measured prevalence or an assertion that every cell contains a visible carrier. The source distinguishes nutrient-rich Cvt transport from starvation-induced autophagy; its temperature-sensitive mutant results are not generalized to all physiological conditions. Membrane/lumen occurrence follows from the described membrane-bounded carrier and exact location definitions.

### Membrane material and sequestered cargo complex

grounding: supported. Targets: GO:0033107.

The two direct components represent one surrounding bilayer and the Cvt cargo complex. GO0034270 supports the cargo-complex identity and Shintani supports its incorporation. Molecular details of the source cargo-receptor aggregate are not silently reduced to an exact subunit census, and neighboring cargo protein examples are not promoted into this target. The membrane row denotes the bilayer structural part explicitly defined by GO0033110. No numerical stoichiometry or complete molecular inventory is claimed.

### Collective bilayer versus condition-specific cargo contribution

grounding: unknown. Targets: GO:0033107.

The ESSENTIAL membrane row refers to the bilayer material constituting the defined double-membrane carrier, not to any named lipid species. Experimental necessity for individual lipids is unresolved. The Cvt-complex UNKNOWN row appropriately avoids converting the condition-specific cargo/receptor deletion phenotypes into universal necessity. Observed membership, formation rate and necessity are distinct conclusions.

### Selective cytoplasm-to-vacuole cargo transport

evidence: supported. Targets: GO:0033107.

The function and delivery endpoint are supported by GO0032258, Reggiori and Shintani. Scott directly supports the Cvt19/Atg19 receptor context. Cvt transport is not equated with nonselective starvation autophagy, nor is selective cargo binding converted into proof of every downstream membrane-assembly step.

### Open Atg inventory does not make the descriptive carrier record incomplete

completeness: supported. Targets: GO:0033107.

The open discussion records incomplete Atg representation. The target already represents its defining membrane and cargo complex, and explicitly scopes its graph as NONMECHANISTIC. Known receptor/membrane-associated observations are useful future curation context, but this is not a complete protein inventory. Any later Atg additions must distinguish retained cargo/constituents from transient assembly machinery; exact family uncertainty should not be mistaken for uncertainty that the published actors exist. No consequential missing-required-representation defect is established here.

### Edge-level topology and transport endpoint

graph: supported. Targets: GO:0033107.

All four NONMECHANISTIC edges are supported at their stated scope: individual membrane parthood, Cvt-complex enclosure by the whole vesicle, carrier participation in Cvt transport and eventual delivery to the fungal vacuole. The enclosure edge correctly targets the whole carrier, not one of its bilayers. Bulk-cytoplasm exclusion comes from GO0032258 and the primary cargo discussion. The graph does not assert complete Atg molecular mechanisms.

### All maintained fields and bounded source scopes

completeness: supported. Targets: GO:0033107.

The complete target, every graph edge and discussion were read. No quantitative property, image licence, trait link, verbatim snippet or individual protein accession is asserted in this target. Empty optional inventories or mechanics do not by themselves establish defects. PROPOSED status and inherited history are preserved; historical search completeness and independent authorship are not recertified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/cvt_vesicle.yaml; Entire maintained YAML, including every definition, evidence note, component, history, graph edge and discussion | context_only | The entire maintained record was read. No scientific content, curation history or status was changed. Retained input bytes were rechecked on resumed work. |
| policy | docs/CURATION.md; Exact identity, constituent/associated-machinery boundary, molecular grounding and structure-formation necessity | context_only | A whole vesicle, surrounding membrane, enclosed compartment, cargo complex and assembly machinery are distinct. Essentiality concerns whether the structure forms, not cell viability or catalytic activity. |
| neighbor-cvt_vesicle_lumen | data/structures/membrane_organelle/cvt_vesicle_lumen.yaml; Entire neighboring maintained YAML read; used only for identity and component/part boundary context | context_only | The neighboring carrier, membrane, lumen and cargo-complex records are distinct maintained owners. Their additional protein examples, evidence and historical decisions are not separately certified by this review. |
| neighbor-cvt_vesicle_membrane | data/structures/membrane_organelle/cvt_vesicle_membrane.yaml; Entire neighboring maintained YAML read; used only for identity and component/part boundary context | context_only | The neighboring carrier, membrane, lumen and cargo-complex records are distinct maintained owners. Their additional protein examples, evidence and historical decisions are not separately certified by this review. |
| neighbor-cvt_complex | data/structures/other/cvt_complex.yaml; Entire neighboring maintained YAML read; used only for identity and component/part boundary context | context_only | The neighboring carrier, membrane, lumen and cargo-complex records are distinct maintained owners. Their additional protein examples, evidence and historical decisions are not separately certified by this review. |
| cvt-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033107,GO:0033110,GO:0034270,GO:0032258,GO:0031410,GO:0060205,GO:0030659,GO:0000324; All eight terms: identifiers, names, definitions, active status, synonyms and relevant is_a/part_of child relations | supports | Eight active GO terms were inspected. GO0033107 defines the double-membrane yeast carrier and its two exact synonyms; GO0033110 denotes either of its two bilayers and is explicitly part_of the vesicle. The cytoplasmic-vesicle and membrane parents explicitly list the target child classes. GO0034270 denotes a preApe1-containing Cvt cargo complex; GO0032258 describes Atg19/Atg11-dependent targeting and expansion around cargo excluding bulk cytoplasm. GO0000324 denotes the fungal destination, and GO0060205 denotes enclosed cytoplasmic-vesicle volume. |
| cvt-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and alternative names | supports | ENA identifies only the asserted NCBITaxon4932 species as Saccharomyces cerevisiae, with fungal lineage. It does not identify a particular experimental strain or quantify occurrence. |
| cvt-agent-reggiori2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15004240%20AND%20SRC%3AMED; Exact PMID, DOI, title, authors, publication year/type and complete abstract | supports | Native MED identifies Early stages of the secretory pathway, but not endosomes, are required for Cvt vesicle and autophagosome assembly in Saccharomyces cerevisiae. (Reggiori F, Wang CW, Nair U, Shintani T, Abeliovich H, Klionsky DJ., 2004), PMID15004240, DOI10.1091/mbc.e03-07-0479. Exact bibliography and complete abstract were read; primary body scope is recorded separately. |
| cvt-agent-reggiori2004-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC404015/; Complete Introduction sec1; Methods sec3 including strain Table1 and sec6 pulse-chase protocol; complete Results sec13 and sec14, including Figures5–8 captions; complete Discussion sec15–18 including Figure9 caption. Other Results/Methods, figure pixels and underlying data were not independently reanalysed. | supports | The primary paper describes hydrolase sequestration within cytosolic double-membrane Cvt vesicles, outer-membrane fusion and release of an inner vesicle into the vacuole. Yeast sec12/sec7 experiments test PAS organization and transport under explicit growth/temperature conditions. The authors report early-secretory contributions but state that the results cannot distinguish ER from Golgi membrane origin. This supports the maintained yeast example and broad carrier context, without fixing a unique donor or a universal molecular assembly mechanism. |
| cvt-agent-reggiori2004-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC404015/fullTextXML; Actual failed fullTextXML response only | context_only | This specific Europe PMC XML route returned HTTP500 and no article body. Genuine primary PMC HTML was independently recovered and read; this failure does not imply that the paper body is unavailable. |
| cvt-agent-SL-0080 | https://rest.uniprot.org/locations/SL-0080.json; Exact native identifier, label, definition, isA/partOf hierarchy and nested GO mappings | supports | SL0080 exactly maps Cvt vesicle to GO0033107 and places it under cytoplasmic vesicle GO0031410. Its definition preserves the double membrane. |
| cvt-agent-shintani2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15138258%20AND%20SRC%3AMED; Exact PMID, DOI, title, authors, publication year/type and complete abstract | supports | Native MED identifies Cargo proteins facilitate the formation of transport vesicles in the cytoplasm to vacuole targeting pathway. (Shintani T, Klionsky DJ., 2004), PMID15138258, DOI10.1074/jbc.m404399200. Exact bibliography and complete abstract were read; primary body scope is recorded separately. |
| cvt-agent-shintani2004-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1712665/; Complete scientific main body: Introduction S1; Experimental Procedures S2–5 and TableI; Results S6–9 and Figures1–3 captions; Discussion S10. Figure pixels, raw measurements and references as independent sources were not reanalysed. | supports | This is a primary experimental study, not a literature review. It tests cargo/receptor contributions using GFP-Atg8 delivery and PAS localization. APE1 or ATG19 loss strongly delays Cvt vesicle formation under growth conditions, whereas rapamycin/starvation autophagy is comparatively preserved; ATG11 loss is more severe. The paper supports selective cargo enclosure and a contribution to formation, not unconditional necessity for every related vesicle. It distinguishes the cargo-receptor aggregate, membrane-associated factors and the enclosing double-membrane carrier. |
| cvt-agent-shintani2004-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1712665/fullTextXML; Actual failed fullTextXML response only | context_only | This specific Europe PMC XML route returned HTTP500 and no article body. Genuine primary PMC HTML was independently recovered and read; this failure does not imply that the paper body is unavailable. |
| cvt-agent-scott2001-pmid | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11430817%20AND%20SRC%3AMED; Exact PMID, DOI, title, authors, publication year/type and complete abstract | supports | Native MED identifies Cvt19 is a receptor for the cytoplasm-to-vacuole targeting pathway. (Scott SV, Guan J, Hutchins MU, Kim J, Klionsky DJ., 2001), PMID11430817, DOI10.1016/s1097-2765(01)00263-5. Exact bibliography and complete abstract were read; primary body scope is recorded separately. |
| cvt-agent-scott2001-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2767243/; Complete Introduction S1; Results S3, S5, S6 and S8 including Figures1,3,4,6 captions; complete Discussion S9–14; Methods S18 including Table1, S24 coimmunoprecipitation and S25 in-vitro binding. Remaining Results/Methods and all image pixels were not reviewed. | supports | The primary study identifies Cvt19 as a selective hydrolase receptor. Deletion, transport assays, precursor-specific coimmunoprecipitation and heterologous/in-vitro binding support the receptor claim. The paper distinguishes prAPI/Ams1 delivery from bulk autophagy and pexophagy, and follows Cvt19 with cargo into the vacuole. It does not establish every proposed Atg scaffold or membrane-expansion mechanism. Shintani2004 supplies the later Atg19/Cvt19 naming bridge. |
| cvt-agent-scott2001-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2767243/fullTextXML; Actual failed fullTextXML response only | context_only | This specific Europe PMC XML route returned HTTP500 and no article body. Genuine primary PMC HTML was independently recovered and read; this failure does not imply that the paper body is unavailable. |
| schema-result | just validate data/structures/membrane_organelle/cvt_vesicle.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/cvt_vesicle.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/cvt_vesicle.yaml --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/cvt_vesicle.yaml --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/cvt_vesicle.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 11 of13 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:15004240: UNREACHABLE; resolved by evidence cvt-agent-reggiori2004-meta; PMID:15138258: UNREACHABLE; resolved by evidence cvt-agent-shintani2004-meta. Source-native identity checked separately. |
| native-verify | /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle.yaml --verify; Complete focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle.yaml --causal-graphs; Complete focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Shintani2004 scientific main text was read completely; Scott2001 was read only in the specified primary sections. The target word review in one Shintani evidence note is not used here to misclassify that primary experiment as a secondary source.
- Reggiori2004 was read in the named primary sections, not the entire paper. Figure pixels, underlying data and measurements were not independently reanalysed. The cited experiments do not establish quantitative population prevalence or a unique membrane donor.
- The native XML routes returned500; genuine archived primary HTML was read instead. Original source access times and raw hashes are retained after resumption.
- Neighbors provide boundary context only. No other record, historical curation decision or individual neighboring protein example is separately reviewed.
- Optional molecular inventories remain incomplete. Collective bilayer constitution does not establish necessity of an individual lipid species, and conditional cargo effects are not universalized.
- Same-base global gates are integrated by the parent at finalization. Deterministic checks do not independently certify scientific claims.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized an honest review for every uncovered target, including clean observations. No finding is invented to satisfy the local issue-only gate.
- Work paused before drafting and resumed with unchanged input/source bytes. Original source receipts were retained; no new retrieval time was substituted.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T010353Z-cvt-vesicle-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cvt structure identity, membrane boundaries and source review
started_at: '2026-10-21T11:20:43Z'
finished_at: '2026-10-22T01:03:53Z'
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
summary: The Cvt carrier identity, membrane/cargo boundaries and selective transport
  context are supported at the declared source scopes. No concrete curation finding
  was established.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/structures/membrane_organelle/cvt_vesicle.yaml
    sha256: cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c
    role: target
  - path: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    sha256: 3bb8cb5c3f751ec93619bb4658fb51a2c6e6a94e4e0b16aa0ea8a0833a28c243
    role: context
  - path: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
    sha256: 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67
    role: context
  - path: data/structures/other/cvt_complex.yaml
    sha256: 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902
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
- target_id: GO:0033107
  path: data/structures/membrane_organelle/cvt_vesicle.yaml
  label: Cvt vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cvt_vesicle.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target, exact authority identities, species/source
    contexts, all component/formation boundaries and every graph edge.
  selection: Target 1 in batch twenty-five, selected by native uncovered path order
    at frozen revision9c0446.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033107
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: just validate data/structures/membrane_organelle/cvt_vesicle.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: just validate-strict data/structures/membrane_organelle/cvt_vesicle.yaml
    --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0033107
  summary: 11 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - cvt-agent-reggiori2004-meta
  - cvt-agent-shintani2004-meta
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle.yaml
    --verify
  exit_code: 0
  summary: Native check passed. The target has no explicit protein accessions or GENE_OR_PROTEIN
    graph nodes; this does not independently prove biological membership.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Native check passed. The target has no explicit protein accessions or GENE_OR_PROTEIN
    graph nodes; this does not independently prove biological membership.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0033107
  summary: No expression-module, regulator-network or transcriptomic inference is
    made by this structural review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0033107
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - neighbor-cvt_vesicle_lumen
  - neighbor-cvt_vesicle_membrane
  - neighbor-cvt_complex
  - cvt-agent-go
  - cvt-agent-tax4932
  - cvt-agent-reggiori2004-meta
  - cvt-agent-reggiori2004-pmc
  - cvt-agent-reggiori2004-jats
  - cvt-agent-SL-0080
  - cvt-agent-shintani2004-meta
  - cvt-agent-shintani2004-pmc
  - cvt-agent-shintani2004-jats
  - cvt-agent-scott2001-pmid
  - cvt-agent-scott2001-pmc
  - cvt-agent-scott2001-jats
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0033107
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle.yaml
  locator: Entire maintained YAML, including every definition, evidence note, component,
    history, graph edge and discussion
  accessed_at: '2026-10-22T00:53:48Z'
  support: context_only
  summary: The entire maintained record was read. No scientific content, curation
    history or status was changed. Retained input bytes were rechecked on resumed
    work.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, constituent/associated-machinery boundary, molecular grounding
    and structure-formation necessity
  accessed_at: '2026-10-22T00:53:48Z'
  support: context_only
  summary: A whole vesicle, surrounding membrane, enclosed compartment, cargo complex
    and assembly machinery are distinct. Essentiality concerns whether the structure
    forms, not cell viability or catalytic activity.
- evidence_id: neighbor-cvt_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
  locator: Entire neighboring maintained YAML read; used only for identity and component/part
    boundary context
  accessed_at: '2026-10-22T00:53:48Z'
  support: context_only
  summary: The neighboring carrier, membrane, lumen and cargo-complex records are
    distinct maintained owners. Their additional protein examples, evidence and historical
    decisions are not separately certified by this review.
- evidence_id: neighbor-cvt_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
  locator: Entire neighboring maintained YAML read; used only for identity and component/part
    boundary context
  accessed_at: '2026-10-22T00:53:48Z'
  support: context_only
  summary: The neighboring carrier, membrane, lumen and cargo-complex records are
    distinct maintained owners. Their additional protein examples, evidence and historical
    decisions are not separately certified by this review.
- evidence_id: neighbor-cvt_complex
  kind: record_content
  reference: data/structures/other/cvt_complex.yaml
  locator: Entire neighboring maintained YAML read; used only for identity and component/part
    boundary context
  accessed_at: '2026-10-22T00:53:48Z'
  support: context_only
  summary: The neighboring carrier, membrane, lumen and cargo-complex records are
    distinct maintained owners. Their additional protein examples, evidence and historical
    decisions are not separately certified by this review.
- evidence_id: cvt-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033107,GO:0033110,GO:0034270,GO:0032258,GO:0031410,GO:0060205,GO:0030659,GO:0000324
  locator: 'All eight terms: identifiers, names, definitions, active status, synonyms
    and relevant is_a/part_of child relations'
  accessed_at: '2026-10-21T11:21:38.146133Z'
  support: supports
  summary: Eight active GO terms were inspected. GO0033107 defines the double-membrane
    yeast carrier and its two exact synonyms; GO0033110 denotes either of its two
    bilayers and is explicitly part_of the vesicle. The cytoplasmic-vesicle and membrane
    parents explicitly list the target child classes. GO0034270 denotes a preApe1-containing
    Cvt cargo complex; GO0032258 describes Atg19/Atg11-dependent targeting and expansion
    around cargo excluding bulk cytoplasm. GO0000324 denotes the fungal destination,
    and GO0060205 denotes enclosed cytoplasmic-vesicle volume.
  snapshot_sha256: 996f6e9edc4ec2167e0ee08326490b7e55c8f2c135f0edf88023f2475d5efca1
- evidence_id: cvt-agent-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and alternative names
  accessed_at: '2026-10-21T11:21:38.146620Z'
  support: supports
  summary: ENA identifies only the asserted NCBITaxon4932 species as Saccharomyces
    cerevisiae, with fungal lineage. It does not identify a particular experimental
    strain or quantify occurrence.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: cvt-agent-reggiori2004-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15004240%20AND%20SRC%3AMED
  locator: Exact PMID, DOI, title, authors, publication year/type and complete abstract
  accessed_at: '2026-10-21T11:21:38.147062Z'
  support: supports
  summary: Native MED identifies Early stages of the secretory pathway, but not endosomes,
    are required for Cvt vesicle and autophagosome assembly in Saccharomyces cerevisiae.
    (Reggiori F, Wang CW, Nair U, Shintani T, Abeliovich H, Klionsky DJ., 2004), PMID15004240,
    DOI10.1091/mbc.e03-07-0479. Exact bibliography and complete abstract were read;
    primary body scope is recorded separately.
  snapshot_sha256: 923b0a91aaa2e0a2ecc4153f810d909c42f0129f6a71ea504c25908ef75af1a8
- evidence_id: cvt-agent-reggiori2004-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC404015/
  locator: Complete Introduction sec1; Methods sec3 including strain Table1 and sec6
    pulse-chase protocol; complete Results sec13 and sec14, including Figures5–8 captions;
    complete Discussion sec15–18 including Figure9 caption. Other Results/Methods,
    figure pixels and underlying data were not independently reanalysed.
  accessed_at: '2026-10-21T11:21:59.995942Z'
  support: supports
  summary: The primary paper describes hydrolase sequestration within cytosolic double-membrane
    Cvt vesicles, outer-membrane fusion and release of an inner vesicle into the vacuole.
    Yeast sec12/sec7 experiments test PAS organization and transport under explicit
    growth/temperature conditions. The authors report early-secretory contributions
    but state that the results cannot distinguish ER from Golgi membrane origin. This
    supports the maintained yeast example and broad carrier context, without fixing
    a unique donor or a universal molecular assembly mechanism.
  snapshot_sha256: 46db4d7121047a31dc3d6ea7c9eced6272d1228d8ac215109e65cb70f0766022
- evidence_id: cvt-agent-reggiori2004-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC404015/fullTextXML
  locator: Actual failed fullTextXML response only
  accessed_at: '2026-10-21T11:21:59.995547Z'
  support: context_only
  summary: This specific Europe PMC XML route returned HTTP500 and no article body.
    Genuine primary PMC HTML was independently recovered and read; this failure does
    not imply that the paper body is unavailable.
  snapshot_sha256: 491961d1d36a1d672c7f5033c56bfd163055c47bbb923db31182d2201d708457
- evidence_id: cvt-agent-SL-0080
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0080.json
  locator: Exact native identifier, label, definition, isA/partOf hierarchy and nested
    GO mappings
  accessed_at: '2026-10-21T11:21:38.146741Z'
  support: supports
  summary: SL0080 exactly maps Cvt vesicle to GO0033107 and places it under cytoplasmic
    vesicle GO0031410. Its definition preserves the double membrane.
  snapshot_sha256: 78f6059d78715afb4efd1a3f54296f0e7d1fb0c915b1a8d1d5a18e9721c43e9f
- evidence_id: cvt-agent-shintani2004-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15138258%20AND%20SRC%3AMED
  locator: Exact PMID, DOI, title, authors, publication year/type and complete abstract
  accessed_at: '2026-10-21T11:21:38.147149Z'
  support: supports
  summary: Native MED identifies Cargo proteins facilitate the formation of transport
    vesicles in the cytoplasm to vacuole targeting pathway. (Shintani T, Klionsky
    DJ., 2004), PMID15138258, DOI10.1074/jbc.m404399200. Exact bibliography and complete
    abstract were read; primary body scope is recorded separately.
  snapshot_sha256: eaa7b0da8ee454d86a5c7a75af92bb0d5475ae3a7ec3b93c6a182057cbfb3277
- evidence_id: cvt-agent-shintani2004-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1712665/
  locator: 'Complete scientific main body: Introduction S1; Experimental Procedures
    S2–5 and TableI; Results S6–9 and Figures1–3 captions; Discussion S10. Figure
    pixels, raw measurements and references as independent sources were not reanalysed.'
  accessed_at: '2026-10-21T11:21:59.996119Z'
  support: supports
  summary: This is a primary experimental study, not a literature review. It tests
    cargo/receptor contributions using GFP-Atg8 delivery and PAS localization. APE1
    or ATG19 loss strongly delays Cvt vesicle formation under growth conditions, whereas
    rapamycin/starvation autophagy is comparatively preserved; ATG11 loss is more
    severe. The paper supports selective cargo enclosure and a contribution to formation,
    not unconditional necessity for every related vesicle. It distinguishes the cargo-receptor
    aggregate, membrane-associated factors and the enclosing double-membrane carrier.
  snapshot_sha256: e0d9145aede1d6f906206866e7c331084b7c522b57090447c7a361d39d61928f
- evidence_id: cvt-agent-shintani2004-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1712665/fullTextXML
  locator: Actual failed fullTextXML response only
  accessed_at: '2026-10-21T11:21:59.996040Z'
  support: context_only
  summary: This specific Europe PMC XML route returned HTTP500 and no article body.
    Genuine primary PMC HTML was independently recovered and read; this failure does
    not imply that the paper body is unavailable.
  snapshot_sha256: 9692dfa38ff9ac245893e927f1c7d9e6204884806f7cd6bfaa5cc876963a6d9e
- evidence_id: cvt-agent-scott2001-pmid
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11430817%20AND%20SRC%3AMED
  locator: Exact PMID, DOI, title, authors, publication year/type and complete abstract
  accessed_at: '2026-10-21T11:22:15.606214Z'
  support: supports
  summary: Native MED identifies Cvt19 is a receptor for the cytoplasm-to-vacuole
    targeting pathway. (Scott SV, Guan J, Hutchins MU, Kim J, Klionsky DJ., 2001),
    PMID11430817, DOI10.1016/s1097-2765(01)00263-5. Exact bibliography and complete
    abstract were read; primary body scope is recorded separately.
  snapshot_sha256: e09eec16b4d1689e48182b6db62f5e14eb4835aa076868b228c83b0c9ac8a6fc
- evidence_id: cvt-agent-scott2001-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2767243/
  locator: Complete Introduction S1; Results S3, S5, S6 and S8 including Figures1,3,4,6
    captions; complete Discussion S9–14; Methods S18 including Table1, S24 coimmunoprecipitation
    and S25 in-vitro binding. Remaining Results/Methods and all image pixels were
    not reviewed.
  accessed_at: '2026-10-21T11:22:15.606503Z'
  support: supports
  summary: The primary study identifies Cvt19 as a selective hydrolase receptor. Deletion,
    transport assays, precursor-specific coimmunoprecipitation and heterologous/in-vitro
    binding support the receptor claim. The paper distinguishes prAPI/Ams1 delivery
    from bulk autophagy and pexophagy, and follows Cvt19 with cargo into the vacuole.
    It does not establish every proposed Atg scaffold or membrane-expansion mechanism.
    Shintani2004 supplies the later Atg19/Cvt19 naming bridge.
  snapshot_sha256: 8bcf3971ee7a49e0c0feedee5188f33a5076a9505ca1158644767eab7f6b228b
- evidence_id: cvt-agent-scott2001-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2767243/fullTextXML
  locator: Actual failed fullTextXML response only
  accessed_at: '2026-10-21T11:22:15.606615Z'
  support: context_only
  summary: This specific Europe PMC XML route returned HTTP500 and no article body.
    Genuine primary PMC HTML was independently recovered and read; this failure does
    not imply that the paper body is unavailable.
  snapshot_sha256: af36377f1d46dfc2f72ff70d7023c7d53a58bc681003e455d04c4a786edacc4b
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/cvt_vesicle.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:20:46Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/cvt_vesicle.yaml'
  snapshot_sha256: 03339d6cc6c5f9a4e439da4d9837cafa3a7a3603411868c161ff8141f58379dc
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/cvt_vesicle.yaml
    --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:20:48Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/cvt_vesicle.yaml\
    \ --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle-strict.tsv"
  snapshot_sha256: 4389cec3e53d3563d297a4c5000f2ffadd72f3d9132bb921e8e52b15ee3078fc
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/cvt_vesicle.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-22T00:53:48Z'
  support: supports
  summary: '11 of13 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:15004240: UNREACHABLE; resolved by evidence cvt-agent-reggiori2004-meta;
    PMID:15138258: UNREACHABLE; resolved by evidence cvt-agent-shintani2004-meta.
    Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle.yaml
    --verify
  locator: Complete focused native output
  accessed_at: '2026-10-21T11:22:13.692358Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle.yaml
    --causal-graphs
  locator: Complete focused native output
  accessed_at: '2026-10-21T11:22:14.243643Z'
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
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: identity
  area: identity
  topic: Carrier, lumen and individual surrounding bilayer remain distinct
  outcome: supported
  target_ids:
  - GO:0033107
  summary: The target identifies the stated structure or enclosed region rather than
    the Cvt cargo protein complex, an individual Atg protein or the pathway itself.
    Native GO and UniProt definitions support the asserted hierarchy and parthood.
    Either-bilayer language preserves the double-membrane carrier; it does not collapse
    both membranes into one bilayer. The mature cargo-containing interior is distinguished
    from the inner vesicle released after fusion and from the intermembrane space.
  evidence_ids:
  - record
  - cvt-agent-go
  - cvt-agent-SL-0080
  - cvt-agent-reggiori2004-pmc
- assessment_id: scope
  area: scope
  topic: Budding-yeast model and conditional experimental context
  outcome: supported
  target_ids:
  - GO:0033107
  summary: The species identity and canonical budding-yeast context are supported
    by Reggiori strains and experiments. COMMON is a qualitative occurrence statement,
    not a measured prevalence or an assertion that every cell contains a visible carrier.
    The source distinguishes nutrient-rich Cvt transport from starvation-induced autophagy;
    its temperature-sensitive mutant results are not generalized to all physiological
    conditions. Membrane/lumen occurrence follows from the described membrane-bounded
    carrier and exact location definitions.
  evidence_ids:
  - record
  - cvt-agent-tax4932
  - cvt-agent-reggiori2004-meta
  - cvt-agent-reggiori2004-pmc
  - cvt-agent-SL-0080
- assessment_id: composition
  area: grounding
  topic: Membrane material and sequestered cargo complex
  outcome: supported
  target_ids:
  - GO:0033107
  summary: The two direct components represent one surrounding bilayer and the Cvt
    cargo complex. GO0034270 supports the cargo-complex identity and Shintani supports
    its incorporation. Molecular details of the source cargo-receptor aggregate are
    not silently reduced to an exact subunit census, and neighboring cargo protein
    examples are not promoted into this target. The membrane row denotes the bilayer
    structural part explicitly defined by GO0033110. No numerical stoichiometry or
    complete molecular inventory is claimed.
  evidence_ids:
  - record
  - policy
  - cvt-agent-go
  - cvt-agent-SL-0080
  - cvt-agent-shintani2004-pmc
- assessment_id: formation-necessity
  area: grounding
  topic: Collective bilayer versus condition-specific cargo contribution
  outcome: unknown
  target_ids:
  - GO:0033107
  summary: The ESSENTIAL membrane row refers to the bilayer material constituting
    the defined double-membrane carrier, not to any named lipid species. Experimental
    necessity for individual lipids is unresolved. The Cvt-complex UNKNOWN row appropriately
    avoids converting the condition-specific cargo/receptor deletion phenotypes into
    universal necessity. Observed membership, formation rate and necessity are distinct
    conclusions.
  evidence_ids:
  - record
  - policy
  - cvt-agent-go
  - cvt-agent-shintani2004-pmc
- assessment_id: function
  area: evidence
  topic: Selective cytoplasm-to-vacuole cargo transport
  outcome: supported
  target_ids:
  - GO:0033107
  summary: The function and delivery endpoint are supported by GO0032258, Reggiori
    and Shintani. Scott directly supports the Cvt19/Atg19 receptor context. Cvt transport
    is not equated with nonselective starvation autophagy, nor is selective cargo
    binding converted into proof of every downstream membrane-assembly step.
  evidence_ids:
  - record
  - cvt-agent-go
  - cvt-agent-reggiori2004-pmc
  - cvt-agent-shintani2004-pmc
  - cvt-agent-scott2001-pmid
  - cvt-agent-scott2001-pmc
- assessment_id: machinery-boundary
  area: completeness
  topic: Open Atg inventory does not make the descriptive carrier record incomplete
  outcome: supported
  target_ids:
  - GO:0033107
  summary: The open discussion records incomplete Atg representation. The target already
    represents its defining membrane and cargo complex, and explicitly scopes its
    graph as NONMECHANISTIC. Known receptor/membrane-associated observations are useful
    future curation context, but this is not a complete protein inventory. Any later
    Atg additions must distinguish retained cargo/constituents from transient assembly
    machinery; exact family uncertainty should not be mistaken for uncertainty that
    the published actors exist. No consequential missing-required-representation defect
    is established here.
  evidence_ids:
  - record
  - policy
  - cvt-agent-go
  - cvt-agent-shintani2004-pmc
  - cvt-agent-scott2001-pmc
- assessment_id: graph
  area: graph
  topic: Edge-level topology and transport endpoint
  outcome: supported
  target_ids:
  - GO:0033107
  summary: 'All four NONMECHANISTIC edges are supported at their stated scope: individual
    membrane parthood, Cvt-complex enclosure by the whole vesicle, carrier participation
    in Cvt transport and eventual delivery to the fungal vacuole. The enclosure edge
    correctly targets the whole carrier, not one of its bilayers. Bulk-cytoplasm exclusion
    comes from GO0032258 and the primary cargo discussion. The graph does not assert
    complete Atg molecular mechanisms.'
  evidence_ids:
  - record
  - cvt-agent-go
  - cvt-agent-SL-0080
  - cvt-agent-reggiori2004-pmc
  - cvt-agent-shintani2004-pmc
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and bounded source scopes
  outcome: supported
  target_ids:
  - GO:0033107
  summary: The complete target, every graph edge and discussion were read. No quantitative
    property, image licence, trait link, verbatim snippet or individual protein accession
    is asserted in this target. Empty optional inventories or mechanics do not by
    themselves establish defects. PROPOSED status and inherited history are preserved;
    historical search completeness and independent authorship are not recertified.
  evidence_ids:
  - record
  - policy
  - cvt-agent-go
  - cvt-agent-reggiori2004-pmc
  - cvt-agent-SL-0080
findings: []
actions: []
limitations:
- Shintani2004 scientific main text was read completely; Scott2001 was read only in
  the specified primary sections. The target word review in one Shintani evidence
  note is not used here to misclassify that primary experiment as a secondary source.
- Reggiori2004 was read in the named primary sections, not the entire paper. Figure
  pixels, underlying data and measurements were not independently reanalysed. The
  cited experiments do not establish quantitative population prevalence or a unique
  membrane donor.
- The native XML routes returned500; genuine archived primary HTML was read instead.
  Original source access times and raw hashes are retained after resumption.
- Neighbors provide boundary context only. No other record, historical curation decision
  or individual neighboring protein example is separately reviewed.
- Optional molecular inventories remain incomplete. Collective bilayer constitution
  does not establish necessity of an individual lipid species, and conditional cargo
  effects are not universalized.
- Same-base global gates are integrated by the parent at finalization. Deterministic
  checks do not independently certify scientific claims.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized an honest review for every uncovered target, including
  clean observations. No finding is invented to satisfy the local issue-only gate.
- Work paused before drafting and resumed with unchanged input/source bytes. Original
  source receipts were retained; no new retrieval time was substituted.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
