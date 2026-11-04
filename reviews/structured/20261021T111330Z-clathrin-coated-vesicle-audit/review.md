# Clathrin vesicle identity and evidence review

- Review: 20261021T111330Z-clathrin-coated-vesicle-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:57:19Z
- Finished UTC: 2026-10-21T11:13:30Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact structural identity, yeast recruitment context, spatial parthood and the descriptive graph are supported within the declared source limits. No concrete curation issue was established.

## Scope And Provenance

Entire single maintained record; exact native identities, primary-source scope and membrane/coat/lumen distinctions.

Selection: Target 5 in batch23, exact sorted uncovered maintained path at frozen revision9c0446.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030136 | data/structures/membrane_organelle/clathrin_coated_vesicle.yaml | maintained | clathrin-coated vesicle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native verify | passed | True | GO:0030136 | Native command passed; target has no explicit protein examples or GENE_OR_PROTEIN graph nodes. |
| Focused native causal-graphs | passed | True | GO:0030136 | Native command passed; target has no explicit protein examples or GENE_OR_PROTEIN graph nodes. |
| Focused native schema | passed | True | GO:0030136 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030136 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0030136 | 9 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0030136 | No expression-module, transcriptomic or regulatory inference is made by these spatial/vesicle claims. |
| Claim-level scientific review | passed | True | GO:0030136 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0030136 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030136 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030136 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030136 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0030136 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact whole-vesicle, lumen or membrane identity

identity: supported. Targets: GO:0030136.

The target is the named physical structure, distinct from the clathrin lattice and from a budding pit. The generic whole class includes endocytic and intracellular traffic; neither the definition nor its maintained identity is restricted to plasma-membrane origin. GO/UniProt exact definitions and synonyms support the target and its is_a/part_of boundaries. The lumen local identifier is paired with exact SL0319; a broader cytoplasmic-vesicle-lumen term is appropriately retained as parent.

### Budding-yeast example and recruitment context

scope: supported. Targets: GO:0030136.

The species identity is exact and Newpher directly studies Saccharomyces cerevisiae. The maintained notes describe clathrin/adaptor recruitment at cortical endocytic sites, not a strain-independent molecular stoichiometry or a direct assay of luminal contents. COMMON is a qualitative occurrence label for this established yeast compartment class; no population survey or invariant presence in each cell state is certified. Methods and mutant perturbations are not silently converted to wild-type prevalence measurements.

### Whole-vesicle parts and delegated coat composition

completeness: supported. Targets: GO:0030136.

The clathrin coat and bilayer are represented as structural parts. The frozen local coat record contains heavy/light-chain component rows and leaves adaptor-module boundaries open, as the target discussion states. Repeating individual coat subunits as direct whole-vesicle components is not required; the optional absence of a separate direct component inventory is not itself a defect.

### Descriptive topology and one supported function

graph: supported. Targets: GO:0030136.

The NONMECHANISTIC graph correctly models coat/membrane parthood and the role of the endocytic subset in clathrin-dependent uptake. GO0072583 and the yeast primary studies support that function; listing it does not establish that every member of the broader clathrin-coated-vesicle class participates in endocytosis. No actin-driven scission mechanism, universal adaptor dependency or necessary clathrin role in all vesicle formation is asserted.

### Individual molecular formation requirements remain unresolved

evidence: unknown. Targets: GO:0030136.

No individual protein/adaptor or lipid-species assembly-necessity assertion is present in these target fields. The membrane target alone labels its defining collective bilayer ESSENTIAL. Localization, reporter dynamics, uptake function and viability are not substitutes for an experiment demonstrating necessity for formation of the entire target.

### Exact citation identities with primary-source limits

provenance: supported. Targets: GO:0030136.

All target native identities and DOI citations were checked. Newpher is a genuine primary PDF with declared body coverage and original access receipt. Kaksonen, where cited, is used only at its complete-abstract tier; failed routes and the metadata-only API response are not counted as full text. No snippet, image, numerical physical-property or dataset claim is present. Historical curation searches and attribution were read but not independently recertified.

### Bounded full-target assessment

completeness: supported. Targets: GO:0030136.

The entire single target and its claim-bearing sources were assessed. Additional component inventories, cargos, numerical properties, images or mechanisms are optional at these whole-vesicle and spatial-part scopes. No concrete curation issue was established within the documented evidence limits; no automatic finding is assigned for unavailable full text or optional empty fields.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/clathrin_coated_vesicle.yaml; Entire maintained YAML including all history, evidence notes, discussions, functions and graph edges | context_only | All maintained target fields were read. No scientific record, mapping status or curator history is changed. |
| policy | docs/CURATION.md; Identity, constituent grounding, claim-level evidence and formation-essentiality contract | context_only | Spatial identity, material identity, localization, activity and necessity for assembly are distinct. Optional inventories do not automatically create curation findings. |
| neighbor-clathrin_coated_vesicle_lumen | data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml; Entire local record including components and boundary discussions | context_only | Frozen local identity/context only. The coat record models heavy/light chains and explicitly leaves adaptor-module boundaries open; no independent correctness claim is imported from its protein accessions or other literature. |
| neighbor-clathrin_coated_vesicle_membrane | data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml; Entire local record including components and boundary discussions | context_only | Frozen local identity/context only. The coat record models heavy/light chains and explicitly leaves adaptor-module boundaries open; no independent correctness claim is imported from its protein accessions or other literature. |
| neighbor-clathrin_vesicle_coat | data/structures/other/clathrin_vesicle_coat.yaml; Entire local record including components and boundary discussions | context_only | Frozen local identity/context only. The coat record models heavy/light chains and explicitly leaves adaptor-module boundaries open; no independent correctness claim is imported from its protein accessions or other literature. |
| clathrin-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030136,GO:0030135,GO:0030125,GO:0030665,GO:0072583,GO:0060205,GO:0030659,GO:0030662; All8 returned identifiers, active status, names, aspects and definitions; exact relevant children relation objects. No unreturned direct relation is inferred as an explicit field. | supports | Eight active GO terms distinguish the coated-vesicle parent, clathrin-coated vesicle, clathrin coat, vesicle membrane and lumen parent, and clathrin-dependent endocytosis. GO0030135 lists GO0030136 is_a; GO0030136 lists GO0030665 part_of. The membrane is_a chain is GO0030659 to GO0030662 to GO0030665. GO0030665 lists GO0030125 part_of, supporting coat parthood through the membrane to the vesicle. GO0072583 is a biological process involving the endocytic subset, not the identity of the entire generic class. |
| clathrin-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, names and lineage | supports | NCBITaxon4932 identifies Saccharomyces cerevisiae at species rank, with the returned synonyms and fungal lineage. This establishes taxon identity, not a population prevalence or the genotype of any experimental strain. |
| clathrin-agent-SL-0070 | https://rest.uniprot.org/locations/SL-0070.json; Exact id, name, definition, synonym and returned geneOntologies/isA/partOf objects, distinguishing top-level from nested fields | supports | The native location identifies clathrin-coated vesicle, maps to GO0030136, lists CCV as synonym and places the class under cytoplasmic vesicle. Its definition includes post-Golgi and plasma-membrane transport and distinguishes clathrin/adaptor coat from the enclosed vesicle. |
| clathrin-agent-doi-10.1016_j.devcel.2005.04.014 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2005.04.014; Exact title, authors, publication year, PMID/DOI and complete abstract | supports | Native MED identifies Newpher, Smith, Lemmon and Lemmon2005, PMID15992543, DOI10.1016/j.devcel.2005.04.014, In vivo dynamics of clathrin and its adaptor-dependent recruitment to the actin-based endocytic machinery in yeast. The complete abstract distinguishes cortical recruitment from internal trans-Golgi/endosomal structures. |
| clathrin-agent-newpher2005-duke | https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content; Published pp87–96: Summary; entire Introduction, Results and Discussion; Experimental Procedures including Table1 and Fig1–6 captions. Especially pp91–93 transient association/adaptor recruitment and pp95–96 Dynamics of Cortical Clathrin Patches. Figure pixels, supplements, movies and raw quantitative data not reanalysed. | supports | The primary yeast study directly images fluorescent heavy/light-chain reporters at internal and cortical sites, documents adaptor-dependent cortical recruitment, and measures clathrin arrival before Abp1 accumulation. Table1 and Methods identify the strains, reporter construction, culture and LAT-A conditions. The Discussion explicitly cannot determine whether clathrin disassembles before budding or a coated vesicle/bud leaves the TIRF field; this is not direct imaging of a sealed lumen or a universal scission mechanism. |
| clathrin-agent-newpher2005-publisher | https://doi.org/10.1016/j.devcel.2005.04.014; Actual retained access response, not a paper body | context_only | The publisher route returned HTTP200 with a 3055-byte LinkingHub redirect/locator response, not an article body. The separately retained Duke PDF provides the genuine primary body read for this review. |
| clathrin-agent-kaksonen2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2005.09.024; Exact bibliographic identity and entire returned abstract; no full-body, Methods or figure read | supports | Native MED identifies Kaksonen, Toret and Drubin2005, PMID16239147, DOI10.1016/j.cell.2005.09.024, A modular design for the clathrin- and actin-mediated endocytosis machinery. The complete primary abstract describes four cooperating modules and reports that clathrin facilitates site initiation but is not necessary for membrane invagination or vesicle formation in the deletion experiments. No necessity assertion is imported into the target. |
| clathrin-agent-kaksonen2005-core | https://core.ac.uk/download/pdf/82329151.pdf; Actual retained access response, not a paper body | context_only | This attempted public full-text route returned403 and supplied no readable article body. The complete native MED abstract is the verified scientific source tier. |
| clathrin-agent-kaksonen2005-publisher | https://www.sciencedirect.com/science/article/pii/S0092867405009785; Actual retained access response, not a paper body | context_only | This attempted public full-text route returned403 and supplied no readable article body. The complete native MED abstract is the verified scientific source tier. |
| clathrin-agent-kaksonen2005-cellpdf | https://www.cell.com/article/S0092867405009785/pdf; Actual retained access response, not a paper body | context_only | This attempted public full-text route returned403 and supplied no readable article body. The complete native MED abstract is the verified scientific source tier. |
| clathrin-agent-kaksonen2005-corealternate | https://core.ac.uk/reader/82329151; Actual retained access response, not a paper body | context_only | This attempted public full-text route returned403 and supplied no readable article body. The complete native MED abstract is the verified scientific source tier. |
| clathrin-agent-kaksonen2005-api | https://api.elsevier.com/content/article/PII:S0092867405009785?httpAccept=text/xml; Actual retained access response, not a paper body | context_only | The public publisher API returned200 but contains only1937-byte coredata metadata, including open-access flags, without article body. Neither200 nor those flags establish full-text reading. |
| native-verify | /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml --verify; Complete focused native command output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml --causal-graphs; Complete focused native command output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/clathrin_coated_vesicle.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/clathrin_coated_vesicle.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/clathrin_coated_vesicle.yaml --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_vesicle-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/clathrin_coated_vesicle.yaml --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_vesicle-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_vesicle-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/clathrin_coated_vesicle.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 9 of9 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Newpher2005 was read through the stated primary-paper body and methods. No figure pixels, supplementary movies or raw data were analysed; its own coat-loss-versus-budding uncertainty is preserved.
- Kaksonen2005 was read as exact native metadata and complete abstract only. CORE PDF/reader, ScienceDirect and Cell PDF returned403; the public publisher API returned only coredata. Full Methods, figures and detailed mutant results were not read.
- The yeast lumen/bilayer existence follows from exact compartment definitions in the established vesicle context; the recruitment study is not a direct sealed-lumen imaging experiment.
- Species-wide COMMON occurrence is qualitative context, not a census or a claim about all genotypes and cell states.
- Local neighboring records are frozen identity/context inputs, not independent proof of their constituent accession mappings. No exhaustive absence claim or optional-inventory requirement is made.
- Historical searches, curator independence and historical issue dispositions are not recertified. Fresh-base completed global15 gates are attached by root only at finalization.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for each previously uncovered record, including clean reviews. No persistence, index update or scientific mutation is performed here.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T111330Z-clathrin-coated-vesicle-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Clathrin vesicle identity and evidence review
started_at: '2026-10-21T10:57:19Z'
finished_at: '2026-10-21T11:13:30Z'
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
summary: Exact structural identity, yeast recruitment context, spatial parthood and
  the descriptive graph are supported within the declared source limits. No concrete
  curation issue was established.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    sha256: cee241afc73475bcdec9d8c3c4c57bdf9c4cb2f726e4a78615dfb393613be9ad
    role: target
  - path: data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
    sha256: 2137a192f721232651c140497813cea3f15a73a67e910194d59fadc7837308f9
    role: context
  - path: data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
    sha256: 963e3cbe094c98b1279923d8f4ecc6a27343f82aa7240dece427fa09882c25f1
    role: context
  - path: data/structures/other/clathrin_vesicle_coat.yaml
    sha256: cef674eb9fc2b08323c1780daa340012db00fd43e3f89c7de880ac972594e17d
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
- target_id: GO:0030136
  path: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  label: clathrin-coated vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained record; exact native identities, primary-source
    scope and membrane/coat/lumen distinctions.
  selection: Target 5 in batch23, exact sorted uncovered maintained path at frozen
    revision9c0446.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030136
checks:
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0030136
  command: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    --verify
  exit_code: 0
  summary: Native command passed; target has no explicit protein examples or GENE_OR_PROTEIN
    graph nodes.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030136
  command: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Native command passed; target has no explicit protein examples or GENE_OR_PROTEIN
    graph nodes.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030136
  command: just validate data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030136
  command: just validate-strict data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_vesicle-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0030136
  summary: 9 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030136
  summary: No expression-module, transcriptomic or regulatory inference is made by
    these spatial/vesicle claims.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030136
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - neighbor-clathrin_coated_vesicle_lumen
  - neighbor-clathrin_coated_vesicle_membrane
  - neighbor-clathrin_vesicle_coat
  - clathrin-agent-go
  - clathrin-agent-tax4932
  - clathrin-agent-SL-0070
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - clathrin-agent-newpher2005-duke
  - clathrin-agent-newpher2005-publisher
  - clathrin-agent-kaksonen2005-meta
  - clathrin-agent-kaksonen2005-core
  - clathrin-agent-kaksonen2005-publisher
  - clathrin-agent-kaksonen2005-cellpdf
  - clathrin-agent-kaksonen2005-corealternate
  - clathrin-agent-kaksonen2005-api
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030136
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
  - GO:0030136
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
  - GO:0030136
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
  - GO:0030136
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
  - GO:0030136
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
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  locator: Entire maintained YAML including all history, evidence notes, discussions,
    functions and graph edges
  accessed_at: '2026-10-21T11:07:31Z'
  support: context_only
  summary: All maintained target fields were read. No scientific record, mapping status
    or curator history is changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Identity, constituent grounding, claim-level evidence and formation-essentiality
    contract
  accessed_at: '2026-10-21T11:07:31Z'
  support: context_only
  summary: Spatial identity, material identity, localization, activity and necessity
    for assembly are distinct. Optional inventories do not automatically create curation
    findings.
- evidence_id: neighbor-clathrin_coated_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
  locator: Entire local record including components and boundary discussions
  accessed_at: '2026-10-21T11:07:31Z'
  support: context_only
  summary: Frozen local identity/context only. The coat record models heavy/light
    chains and explicitly leaves adaptor-module boundaries open; no independent correctness
    claim is imported from its protein accessions or other literature.
- evidence_id: neighbor-clathrin_coated_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
  locator: Entire local record including components and boundary discussions
  accessed_at: '2026-10-21T11:07:31Z'
  support: context_only
  summary: Frozen local identity/context only. The coat record models heavy/light
    chains and explicitly leaves adaptor-module boundaries open; no independent correctness
    claim is imported from its protein accessions or other literature.
- evidence_id: neighbor-clathrin_vesicle_coat
  kind: record_content
  reference: data/structures/other/clathrin_vesicle_coat.yaml
  locator: Entire local record including components and boundary discussions
  accessed_at: '2026-10-21T11:07:31Z'
  support: context_only
  summary: Frozen local identity/context only. The coat record models heavy/light
    chains and explicitly leaves adaptor-module boundaries open; no independent correctness
    claim is imported from its protein accessions or other literature.
- evidence_id: clathrin-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030136,GO:0030135,GO:0030125,GO:0030665,GO:0072583,GO:0060205,GO:0030659,GO:0030662
  locator: All8 returned identifiers, active status, names, aspects and definitions;
    exact relevant children relation objects. No unreturned direct relation is inferred
    as an explicit field.
  accessed_at: '2026-10-21T11:04:40.022677Z'
  support: supports
  summary: Eight active GO terms distinguish the coated-vesicle parent, clathrin-coated
    vesicle, clathrin coat, vesicle membrane and lumen parent, and clathrin-dependent
    endocytosis. GO0030135 lists GO0030136 is_a; GO0030136 lists GO0030665 part_of.
    The membrane is_a chain is GO0030659 to GO0030662 to GO0030665. GO0030665 lists
    GO0030125 part_of, supporting coat parthood through the membrane to the vesicle.
    GO0072583 is a biological process involving the endocytic subset, not the identity
    of the entire generic class.
  snapshot_sha256: 99bb7c9eae759e77dbeb8efc316337e5593f176de6a769197070419135166ed5
- evidence_id: clathrin-agent-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, names and lineage
  accessed_at: '2026-10-21T11:04:40.023078Z'
  support: supports
  summary: NCBITaxon4932 identifies Saccharomyces cerevisiae at species rank, with
    the returned synonyms and fungal lineage. This establishes taxon identity, not
    a population prevalence or the genotype of any experimental strain.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: clathrin-agent-SL-0070
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0070.json
  locator: Exact id, name, definition, synonym and returned geneOntologies/isA/partOf
    objects, distinguishing top-level from nested fields
  accessed_at: '2026-10-21T11:04:40.023283Z'
  support: supports
  summary: The native location identifies clathrin-coated vesicle, maps to GO0030136,
    lists CCV as synonym and places the class under cytoplasmic vesicle. Its definition
    includes post-Golgi and plasma-membrane transport and distinguishes clathrin/adaptor
    coat from the enclosed vesicle.
  snapshot_sha256: f43fcdaa17e965bb510e8bfbfc25cac322e28c331a29ea44ff71953a61d7840c
- evidence_id: clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2005.04.014
  locator: Exact title, authors, publication year, PMID/DOI and complete abstract
  accessed_at: '2026-10-21T10:57:50.523144Z'
  support: supports
  summary: Native MED identifies Newpher, Smith, Lemmon and Lemmon2005, PMID15992543,
    DOI10.1016/j.devcel.2005.04.014, In vivo dynamics of clathrin and its adaptor-dependent
    recruitment to the actin-based endocytic machinery in yeast. The complete abstract
    distinguishes cortical recruitment from internal trans-Golgi/endosomal structures.
  snapshot_sha256: c99ec084fa3f65e3b5107699c30f42b09489dbc49d6be518d71ff9352d5a199c
- evidence_id: clathrin-agent-newpher2005-duke
  kind: primary_source
  reference: https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content
  locator: 'Published pp87–96: Summary; entire Introduction, Results and Discussion;
    Experimental Procedures including Table1 and Fig1–6 captions. Especially pp91–93
    transient association/adaptor recruitment and pp95–96 Dynamics of Cortical Clathrin
    Patches. Figure pixels, supplements, movies and raw quantitative data not reanalysed.'
  accessed_at: '2026-10-21T11:00:52.091438Z'
  support: supports
  summary: The primary yeast study directly images fluorescent heavy/light-chain reporters
    at internal and cortical sites, documents adaptor-dependent cortical recruitment,
    and measures clathrin arrival before Abp1 accumulation. Table1 and Methods identify
    the strains, reporter construction, culture and LAT-A conditions. The Discussion
    explicitly cannot determine whether clathrin disassembles before budding or a
    coated vesicle/bud leaves the TIRF field; this is not direct imaging of a sealed
    lumen or a universal scission mechanism.
  snapshot_sha256: c848e911372b9afb9902e4a74e3cb3dd66ef90eb5e102024cc95fff648bb6c21
- evidence_id: clathrin-agent-newpher2005-publisher
  kind: authority
  reference: https://doi.org/10.1016/j.devcel.2005.04.014
  locator: Actual retained access response, not a paper body
  accessed_at: '2026-10-21T10:58:29.695830Z'
  support: context_only
  summary: The publisher route returned HTTP200 with a 3055-byte LinkingHub redirect/locator
    response, not an article body. The separately retained Duke PDF provides the genuine
    primary body read for this review.
  snapshot_sha256: 5df941bcc76d6caccdb7f7d86b8fd5365874521f4d3dc8eafc0e5e62b77b6f04
- evidence_id: clathrin-agent-kaksonen2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2005.09.024
  locator: Exact bibliographic identity and entire returned abstract; no full-body,
    Methods or figure read
  accessed_at: '2026-10-21T11:04:40.023205Z'
  support: supports
  summary: Native MED identifies Kaksonen, Toret and Drubin2005, PMID16239147, DOI10.1016/j.cell.2005.09.024,
    A modular design for the clathrin- and actin-mediated endocytosis machinery. The
    complete primary abstract describes four cooperating modules and reports that
    clathrin facilitates site initiation but is not necessary for membrane invagination
    or vesicle formation in the deletion experiments. No necessity assertion is imported
    into the target.
  snapshot_sha256: b21f04a2ca620468ebafa02936207fe7e04553d44f862f3f18d72a85b6c4aba2
- evidence_id: clathrin-agent-kaksonen2005-core
  kind: authority
  reference: https://core.ac.uk/download/pdf/82329151.pdf
  locator: Actual retained access response, not a paper body
  accessed_at: '2026-10-21T11:04:59.142587Z'
  support: context_only
  summary: This attempted public full-text route returned403 and supplied no readable
    article body. The complete native MED abstract is the verified scientific source
    tier.
  snapshot_sha256: 38e27fd66e47f5347e47c3c9212a49e6a5d401fccbe055531492a18087eb5c8e
- evidence_id: clathrin-agent-kaksonen2005-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0092867405009785
  locator: Actual retained access response, not a paper body
  accessed_at: '2026-10-21T11:04:59.142998Z'
  support: context_only
  summary: This attempted public full-text route returned403 and supplied no readable
    article body. The complete native MED abstract is the verified scientific source
    tier.
  snapshot_sha256: 2f404f9566166ed7addf3acf1a84c3823e680c96afec905b2082e988e618856e
- evidence_id: clathrin-agent-kaksonen2005-cellpdf
  kind: authority
  reference: https://www.cell.com/article/S0092867405009785/pdf
  locator: Actual retained access response, not a paper body
  accessed_at: '2026-10-21T11:05:34.915188Z'
  support: context_only
  summary: This attempted public full-text route returned403 and supplied no readable
    article body. The complete native MED abstract is the verified scientific source
    tier.
  snapshot_sha256: fb778dfc2ae275f47682a0f33f6db4981424deaf07c53c01d57dea505437f700
- evidence_id: clathrin-agent-kaksonen2005-corealternate
  kind: authority
  reference: https://core.ac.uk/reader/82329151
  locator: Actual retained access response, not a paper body
  accessed_at: '2026-10-21T11:05:34.915266Z'
  support: context_only
  summary: This attempted public full-text route returned403 and supplied no readable
    article body. The complete native MED abstract is the verified scientific source
    tier.
  snapshot_sha256: db49b113c0c181640a267bca62b7691e46c8a36d3cf4becad4d7f0517cc3faee
- evidence_id: clathrin-agent-kaksonen2005-api
  kind: authority
  reference: https://api.elsevier.com/content/article/PII:S0092867405009785?httpAccept=text/xml
  locator: Actual retained access response, not a paper body
  accessed_at: '2026-10-21T11:05:34.914917Z'
  support: context_only
  summary: The public publisher API returned200 but contains only1937-byte coredata
    metadata, including open-access flags, without article body. Neither200 nor those
    flags establish full-text reading.
  snapshot_sha256: 53993cd92f3bb1d1dcd4f4f4887c8a8acd6f0e64d35250a3fd23d05fc0dd0f51
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    --verify
  locator: Complete focused native command output
  accessed_at: '2026-10-21T11:05:59.963255Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    --causal-graphs
  locator: Complete focused native command output
  accessed_at: '2026-10-21T11:06:00.534668Z'
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
  reference: just validate data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:57:21Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/clathrin_coated_vesicle.yaml'
  snapshot_sha256: 4368a687b4017f2184986f7a4d47b6772097f83641dee7157a87f5e879c255ed
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_vesicle-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:57:22Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/clathrin_coated_vesicle.yaml\
    \ --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_vesicle-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_vesicle-strict.tsv"
  snapshot_sha256: a49f83c33301146ddf055e39f201aa211614b8873e44018ff2ac8e320a7fc9d1
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T11:07:31Z'
  support: supports
  summary: '9 of9 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
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
  topic: Exact whole-vesicle, lumen or membrane identity
  outcome: supported
  target_ids:
  - GO:0030136
  summary: The target is the named physical structure, distinct from the clathrin
    lattice and from a budding pit. The generic whole class includes endocytic and
    intracellular traffic; neither the definition nor its maintained identity is restricted
    to plasma-membrane origin. GO/UniProt exact definitions and synonyms support the
    target and its is_a/part_of boundaries. The lumen local identifier is paired with
    exact SL0319; a broader cytoplasmic-vesicle-lumen term is appropriately retained
    as parent.
  evidence_ids:
  - record
  - policy
  - clathrin-agent-go
  - clathrin-agent-tax4932
  - clathrin-agent-SL-0070
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - clathrin-agent-newpher2005-duke
  - clathrin-agent-kaksonen2005-meta
- assessment_id: scope
  area: scope
  topic: Budding-yeast example and recruitment context
  outcome: supported
  target_ids:
  - GO:0030136
  summary: The species identity is exact and Newpher directly studies Saccharomyces
    cerevisiae. The maintained notes describe clathrin/adaptor recruitment at cortical
    endocytic sites, not a strain-independent molecular stoichiometry or a direct
    assay of luminal contents. COMMON is a qualitative occurrence label for this established
    yeast compartment class; no population survey or invariant presence in each cell
    state is certified. Methods and mutant perturbations are not silently converted
    to wild-type prevalence measurements.
  evidence_ids:
  - record
  - policy
  - clathrin-agent-go
  - clathrin-agent-tax4932
  - clathrin-agent-SL-0070
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - clathrin-agent-newpher2005-duke
  - clathrin-agent-kaksonen2005-meta
- assessment_id: composition
  area: completeness
  topic: Whole-vesicle parts and delegated coat composition
  outcome: supported
  target_ids:
  - GO:0030136
  summary: The clathrin coat and bilayer are represented as structural parts. The
    frozen local coat record contains heavy/light-chain component rows and leaves
    adaptor-module boundaries open, as the target discussion states. Repeating individual
    coat subunits as direct whole-vesicle components is not required; the optional
    absence of a separate direct component inventory is not itself a defect.
  evidence_ids:
  - record
  - policy
  - clathrin-agent-go
  - clathrin-agent-tax4932
  - clathrin-agent-SL-0070
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - clathrin-agent-newpher2005-duke
  - clathrin-agent-kaksonen2005-meta
- assessment_id: function-graph
  area: graph
  topic: Descriptive topology and one supported function
  outcome: supported
  target_ids:
  - GO:0030136
  summary: The NONMECHANISTIC graph correctly models coat/membrane parthood and the
    role of the endocytic subset in clathrin-dependent uptake. GO0072583 and the yeast
    primary studies support that function; listing it does not establish that every
    member of the broader clathrin-coated-vesicle class participates in endocytosis.
    No actin-driven scission mechanism, universal adaptor dependency or necessary
    clathrin role in all vesicle formation is asserted.
  evidence_ids:
  - record
  - policy
  - clathrin-agent-go
  - clathrin-agent-tax4932
  - clathrin-agent-SL-0070
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - clathrin-agent-newpher2005-duke
  - clathrin-agent-kaksonen2005-meta
- assessment_id: assembly-necessity
  area: evidence
  topic: Individual molecular formation requirements remain unresolved
  outcome: unknown
  target_ids:
  - GO:0030136
  summary: No individual protein/adaptor or lipid-species assembly-necessity assertion
    is present in these target fields. The membrane target alone labels its defining
    collective bilayer ESSENTIAL. Localization, reporter dynamics, uptake function
    and viability are not substitutes for an experiment demonstrating necessity for
    formation of the entire target.
  evidence_ids:
  - record
  - policy
  - clathrin-agent-go
  - clathrin-agent-tax4932
  - clathrin-agent-SL-0070
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - clathrin-agent-newpher2005-duke
  - clathrin-agent-kaksonen2005-meta
- assessment_id: provenance
  area: provenance
  topic: Exact citation identities with primary-source limits
  outcome: supported
  target_ids:
  - GO:0030136
  summary: All target native identities and DOI citations were checked. Newpher is
    a genuine primary PDF with declared body coverage and original access receipt.
    Kaksonen, where cited, is used only at its complete-abstract tier; failed routes
    and the metadata-only API response are not counted as full text. No snippet, image,
    numerical physical-property or dataset claim is present. Historical curation searches
    and attribution were read but not independently recertified.
  evidence_ids:
  - record
  - policy
  - clathrin-agent-go
  - clathrin-agent-tax4932
  - clathrin-agent-SL-0070
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - clathrin-agent-newpher2005-duke
  - clathrin-agent-kaksonen2005-meta
- assessment_id: coverage
  area: completeness
  topic: Bounded full-target assessment
  outcome: supported
  target_ids:
  - GO:0030136
  summary: The entire single target and its claim-bearing sources were assessed. Additional
    component inventories, cargos, numerical properties, images or mechanisms are
    optional at these whole-vesicle and spatial-part scopes. No concrete curation
    issue was established within the documented evidence limits; no automatic finding
    is assigned for unavailable full text or optional empty fields.
  evidence_ids:
  - record
  - policy
  - clathrin-agent-go
  - clathrin-agent-tax4932
  - clathrin-agent-SL-0070
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - clathrin-agent-newpher2005-duke
  - clathrin-agent-kaksonen2005-meta
findings: []
actions: []
limitations:
- Newpher2005 was read through the stated primary-paper body and methods. No figure
  pixels, supplementary movies or raw data were analysed; its own coat-loss-versus-budding
  uncertainty is preserved.
- Kaksonen2005 was read as exact native metadata and complete abstract only. CORE
  PDF/reader, ScienceDirect and Cell PDF returned403; the public publisher API returned
  only coredata. Full Methods, figures and detailed mutant results were not read.
- The yeast lumen/bilayer existence follows from exact compartment definitions in
  the established vesicle context; the recruitment study is not a direct sealed-lumen
  imaging experiment.
- Species-wide COMMON occurrence is qualitative context, not a census or a claim about
  all genotypes and cell states.
- Local neighboring records are frozen identity/context inputs, not independent proof
  of their constituent accession mappings. No exhaustive absence claim or optional-inventory
  requirement is made.
- Historical searches, curator independence and historical issue dispositions are
  not recertified. Fresh-base completed global15 gates are attached by root only at
  finalization.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized one review for each previously uncovered record,
  including clean reviews. No persistence, index update or scientific mutation is
  performed here.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
