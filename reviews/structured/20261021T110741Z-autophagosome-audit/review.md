# Autophagosome identity, topology and evidence review

- Review: 20261021T110741Z-autophagosome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:40:03Z
- Finished UTC: 2026-10-21T11:07:41Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact structure, sibling topology, scoped composition and starvation-qualified yeast evidence are coherent. No concrete curation finding was established; source-reading and molecular-necessity limitations remain explicit.

## Scope And Provenance

Entire single maintained record, all three sibling topological records, exact native authority identifiers and the claim-specific literature sections declared in evidence.

Selection: Target 2 in batch twenty-one; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005776 | data/structures/membrane_organelle/autophagosome.yaml | maintained | autophagosome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0005776 | Focused native command passed. There are no asserted UniProtKB protein examples or GENE_OR_PROTEIN graph nodes to expand. |
| Native protein causal-graphs | passed | True | GO:0005776 | Focused native command passed. There are no asserted UniProtKB protein examples or GENE_OR_PROTEIN graph nodes to expand. |
| Focused native schema | passed | True | GO:0005776 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005776 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0005776 | 11 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0005776 | No expression-module or transcriptomic inference is asserted. |
| Claim-level scientific review | passed | True | GO:0005776 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0005776 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005776 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005776 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005776 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0005776 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact structure identity and synonymous boundaries

identity: supported. Targets: GO:0005776.

The target is the organelle, its enclosed lumen or its surrounding membrane as explicitly named, rather than the PAS, the later intravacuolar autophagic body, a generic process or an individual protein. Active native GO terms and exact UniProt location mappings support the separate identities; synonym scopes are preserved.

### Parent classification and parthood

consistency: supported. Targets: GO:0005776.

The sibling records consistently distinguish a membrane-bounded organelle from its membrane and enclosed volume. Parthood and boundary statements are supported. For the membrane and lumen, cytoplasmic-vesicle parent classes are explicitly native UniProt isA classifications, not assertions that those are current direct GO parent edges; current GO ancestry was separately examined.

### Component referent and essentiality

grounding: supported. Targets: GO:0005776.

The single component refers to the structural autophagosome membrane, so GO:0000421 grounds that structural part rather than a chemical lipid species. ESSENTIAL is scoped to the collective double-bilayer boundary constitutive of this membrane-bounded organelle. It does not claim any individual Atg protein or lipid species is universally indispensable. The stated TODO honestly leaves Atg8 lipidation, Atg conjugation systems, Atg9 and fusion machinery for later component-level grounding.

### Yeast occurrence and canonical experiment

scope: supported. Targets: GO:0005776.

The exact taxon is S. cerevisiae. COMMON is read together with its explicit starvation-induced macroautophagy note and the experimental induction evidence, not as a quantitative frequency across strains or all growth states. Takeshige establishes the conditioned phenotype; Suzuki supports the genetic/fluorescence model. Neither is generalized to all eukaryotic taxa or used to equate PAS with mature organelle.

### Topological and coarse functional edges

graph: supported. Targets: GO:0005776.

Every maintained edge was read and remains NONMECHANISTIC. Membrane-bounds-lumen and parthood are direct topological statements. Where present, macroautophagy support and yeast vacuolar delivery are coarse functions grounded in native process definitions and source descriptions, not a complete Atg initiation, closure or fusion mechanism. The 1992 vacuolar-body result is not mislabeled here as direct mechanistic proof of fusion.

### Bibliographic identity and claim-specific reading

evidence: supported. Targets: GO:0005776.

Citations identify the stated papers. Primary studies were inspected at the explicitly recorded article sections; no figure-level reanalysis or uninspected full-text passage is certified. Source evidence supports the current bounded statements. Native identity mappings and descriptive endpoints are kept separate from protein-specific membership or assembly-necessity evidence.

### Whole-record review with optional extensions

completeness: supported. Targets: GO:0005776.

All maintained fields, source notes, history and neighboring topological records were inspected. Exact dimensions, numerical frequencies, images, traits, protein examples and exhaustive machinery inventories are not asserted; their absence alone is not a defect. No quoted source passage in the record requires quotation repair. Individual molecular necessity remains outside this bounded structural assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/autophagosome.yaml; Entire maintained YAML including history, evidence, components, functions, topology graph and discussions | context_only | Every maintained field was read. The record remains PROPOSED; no scientific or history edit is made. |
| policy | docs/CURATION.md; Component identity, composition, structural-part grounding and assembly-essentiality contract | context_only | A structural membrane part and its lipid material have different referents. Collective bilayer constitution does not establish necessity of any individual lipid species or Atg protein. |
| neighbor-autophagosome_lumen | data/structures/membrane_organelle/autophagosome_lumen.yaml; Entire neighboring record | context_only | The organelle, lumen and membrane records were read together to assess parthood, topology and the material-versus-structure distinction. An ignored-inclusive search of data/structures YAML for the three exact GO IDs returned these three paths; this is a bounded local search, not an ontology-wide absence claim. |
| neighbor-autophagosome_membrane | data/structures/membrane_organelle/autophagosome_membrane.yaml; Entire neighboring record | context_only | The organelle, lumen and membrane records were read together to assess parthood, topology and the material-versus-structure distinction. An ignored-inclusive search of data/structures YAML for the three exact GO IDs returned these three paths; this is a bounded local search, not an ontology-wide absence claim. |
| autophagosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005776,GO:0000421,GO:0034423,GO:0060205,GO:0030659,GO:0016236,GO:0061909,GO:0000324; Exact id, name, isObsolete, definition, synonym, comment and child-relation fields of the eight requested terms | supports | All eight returned GO terms are active. Exact target definitions, labels and synonyms distinguish autophagosome GO:0005776, membrane GO:0000421 and lumen GO:0034423; the remaining terms identify the declared broad parent classes, macroautophagy, fungal vacuole and autophagosome-lysosome fusion. GO:0061909 explicitly includes yeast vacuole fusion and autophagic-body release. GO:0034423 distinguishes normal lumen residents from cargo destined for degradation. |
| autophagosome-agent-ancestors-0005776 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005776/ancestors?relations=is_a,part_of; Complete returned ancestor list for the exact target; relation types is_a and part_of | supports | The current GO is_a/part_of ancestry was checked as a bounded identity/hierarchy cross-check. The membrane/lumen GO ancestry uses vacuolar classifications; it does not itself establish the declared cytoplasmic-vesicle membrane/lumen parent. Those broad classifications are explicitly supported by the separately inspected UniProt location hierarchy. |
| autophagosome-agent-SL-0022-json | https://rest.uniprot.org/locations/SL-0022.json; Exact id/name/definition, synonyms, geneOntologies, isA and partOf objects | supports | SL-0022 identifies autophagosome membrane and maps exactly to GO:0000421. All three maintained membrane synonyms match. Its isA location maps to GO:0030659 and its partOf autophagosome maps to GO:0005776. The nested autophagosome definition distinguishes outer membrane fusion from release and lysis of the inner autophagic body. |
| autophagosome-agent-SL-0318-json | https://rest.uniprot.org/locations/SL-0318.json; Exact id/name/definition, synonyms, geneOntologies, isA and partOf objects | supports | SL-0318 identifies autophagosome lumen and maps exactly to GO:0034423. All three maintained lumen synonyms match. Its isA cytoplasmic-vesicle lumen maps to GO:0060205 and its partOf autophagosome maps to GO:0005776. |
| autophagosome-agent-taxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank, lineage and otherNames | supports | Native ENA taxonomy identifies taxon 4932 as Saccharomyces cerevisiae at species rank. This verifies the name/identifier pair; the experiments separately establish the biological occurrence and condition. |
| autophagosome-agent-citations | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=20&amp;query=DOI%3A10.1083/jcb.119.2.301%20OR%20DOI%3A10.1093/emboj/20.21.5971%20OR%20DOI%3A10.1038/35044114%20OR%20DOI%3A10.1038/ncb1007-1102; Complete four-result Europe PMC core response for exact DOI query | supports | The four exact DOI records were checked for titles, authors, journal/year, PMID and complete returned abstracts: Takeshige 1992 (10.1083/jcb.119.2.301), Suzuki 2001 (10.1093/emboj/20.21.5971), Ichimura 2000 (10.1038/35044114), and Xie/Klionsky 2007 (10.1038/ncb1007-1102). This metadata row alone does not attest a full-text read. |
| autophagosome-agent-takeshige1992-xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC2289660.1/PMC2289660.1.xml; Abstract; Methods strains/media/starvation/microscopy; Results nutrient starvation and body accumulation; Discussion formation mechanism and normal autophagy | supports | Relevant Methods, starvation/autophagic-body Results and Discussion were read from the archived PMC article XML. Nutrient-starved yeast accumulated cytoplasm-containing autophagic bodies in vacuoles of proteinase-deficient cells, and PMSF permitted their observation in wild-type cells. These experiments support the qualified starvation-induced yeast occurrence and degradative endpoint. The Discussion explicitly does not resolve the body-formation mechanism; this paper is not treated as a direct assay of the later autophagosome-vacuole fusion mechanism. |
| autophagosome-agent-suzuki2001-publisher | https://www.embopress.org/doi/full/10.1093/emboj/20.21.5971; Publisher Abstract; Introduction; Results functional GFP-Aut7/PAS, Apg proteins and autophagosome distinction; Discussion; Methods yeast media, plasmids and fluorescence microscopy | supports | The publisher full article supplied the relevant Introduction, Results on functional GFP-Aut7, PAS localization, autophagosome distinction and mutant transport, Discussion and Methods on yeast cultivation and fluorescence microscopy. These support S. cerevisiae as a genetic/fluorescence model for PAS and autophagosome formation. The article distinguishes the PAS from mature autophagosomes; it also describes phagophore extension/closure and vacuolar delivery in its Introduction. The review does not identify every PAS punctum as a mature autophagosome or claim an exhaustive mechanistic inventory. |
| autophagosome-agent-xie2007-publisher | https://www.nature.com/articles/ncb1007-1102; Complete publisher abstract and bibliographic fields; full article body unavailable | partial | The publisher abstract and bibliographic information were readable. The abstract describes the double-membrane sequestering organelle, lysosomal cargo delivery and core ATG machinery for vesicle formation. The subscription page did not expose the full article body, so detailed review-text, figures or individual machinery necessity are not claimed as inspected. |
| autophagosome-agent-xie2007-pdf | https://www.nature.com/articles/ncb1007-1102.pdf; Actual HTTP 200 text/html response at the PDF URL | context_only | The publisher PDF URL returned an HTML subscription/abstract page, not PDF article content. This is an access receipt only and provides no additional full-text evidence. |
| autophagosome-agent-ichimura2000-publisher | https://www.nature.com/articles/35044114; Abstract; Main Apg8-PE identification, Apg7/Apg3 dependence and discussion; Methods yeast, extraction and mass spectrometry | supports | The publisher abstract, relevant Main results/discussion and Methods were read. Mass spectrometry, biochemical treatment and yeast mutant assays establish Apg8 C-terminal conjugation to phosphatidylethanolamine and the Apg7/Apg3-dependent lipidation pathway. This supports the record discussion of Atg8 lipidation; it does not turn a source-level mechanism into a curated complete mature-organelle protein inventory. |
| native-verify | /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml --verify; Exact focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml --causal-graphs; Exact focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/autophagosome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/autophagosome.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/autophagosome.yaml --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/autophagosome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/autophagosome.yaml --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/autophagosome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/autophagosome-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/autophagosome.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 11 of11 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The review covers the exact maintained record and stated source sections, not an exhaustive literature or component inventory. Protein-specific formation necessity and generic lipid chemical identity are not newly established.
- Xie and Klionsky 2007 was accessible at abstract/bibliographic scope only. The publisher PDF route returned HTML subscription content; the full article and figures were not read. No detailed individual-machinery claim relies solely on unseen text.
- The primary papers were read at the explicitly named Methods/Results/Discussion sections; all image panels and underlying microscopy data were not reanalysed. Historical curator searches and independent historical authorship are not certified.
- The fresh-base batch15 global gates are attached by root only at finalization. This draft contains the actual focused checks and exact fresh-base target resolver slice.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized a review for every uncovered target, including targets without findings. Only root may finalize or save this review bundle.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110741Z-autophagosome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Autophagosome identity, topology and evidence review
started_at: '2026-10-21T10:40:03Z'
finished_at: '2026-10-21T11:07:41Z'
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
summary: The exact structure, sibling topology, scoped composition and starvation-qualified
  yeast evidence are coherent. No concrete curation finding was established; source-reading
  and molecular-necessity limitations remain explicit.
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
  - path: data/structures/membrane_organelle/autophagosome.yaml
    sha256: 9d18c1f34ce5e4da65546eccf8f4ffc9a2273fcca1cd6db4efbb770f8591c3ba
    role: target
  - path: data/structures/membrane_organelle/autophagosome_lumen.yaml
    sha256: 33fbf9f3ae1591081dd1e113d0fd7476c64bdafaa238ec35c7705fb89bb0f98d
    role: context
  - path: data/structures/membrane_organelle/autophagosome_membrane.yaml
    sha256: aa651db3a9b5a208ae7a4deef9d3595d79c0296cda8ebdc9a1c524a11b948254
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
- target_id: GO:0005776
  path: data/structures/membrane_organelle/autophagosome.yaml
  label: autophagosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/autophagosome.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained record, all three sibling topological records,
    exact native authority identifiers and the claim-specific literature sections
    declared in evidence.
  selection: Target 2 in batch twenty-one; exact sorted uncovered path at frozen fresh-main
    revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005776
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0005776
  command: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml
    --verify
  exit_code: 0
  summary: Focused native command passed. There are no asserted UniProtKB protein
    examples or GENE_OR_PROTEIN graph nodes to expand.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005776
  command: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native command passed. There are no asserted UniProtKB protein
    examples or GENE_OR_PROTEIN graph nodes to expand.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005776
  command: just validate data/structures/membrane_organelle/autophagosome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005776
  command: just validate-strict data/structures/membrane_organelle/autophagosome.yaml
    --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/autophagosome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0005776
  summary: 11 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005776
  summary: No expression-module or transcriptomic inference is asserted.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005776
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - neighbor-autophagosome_lumen
  - neighbor-autophagosome_membrane
  - autophagosome-agent-go
  - autophagosome-agent-ancestors-0005776
  - autophagosome-agent-SL-0022-json
  - autophagosome-agent-SL-0318-json
  - autophagosome-agent-taxon-4932
  - autophagosome-agent-citations
  - autophagosome-agent-takeshige1992-xml
  - autophagosome-agent-suzuki2001-publisher
  - autophagosome-agent-xie2007-publisher
  - autophagosome-agent-xie2007-pdf
  - autophagosome-agent-ichimura2000-publisher
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005776
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
  - GO:0005776
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
  - GO:0005776
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
  - GO:0005776
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
  - GO:0005776
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
  reference: data/structures/membrane_organelle/autophagosome.yaml
  locator: Entire maintained YAML including history, evidence, components, functions,
    topology graph and discussions
  accessed_at: '2026-10-21T11:04:47Z'
  support: context_only
  summary: Every maintained field was read. The record remains PROPOSED; no scientific
    or history edit is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Component identity, composition, structural-part grounding and assembly-essentiality
    contract
  accessed_at: '2026-10-21T11:04:47Z'
  support: context_only
  summary: A structural membrane part and its lipid material have different referents.
    Collective bilayer constitution does not establish necessity of any individual
    lipid species or Atg protein.
- evidence_id: neighbor-autophagosome_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/autophagosome_lumen.yaml
  locator: Entire neighboring record
  accessed_at: '2026-10-21T11:04:47Z'
  support: context_only
  summary: The organelle, lumen and membrane records were read together to assess
    parthood, topology and the material-versus-structure distinction. An ignored-inclusive
    search of data/structures YAML for the three exact GO IDs returned these three
    paths; this is a bounded local search, not an ontology-wide absence claim.
- evidence_id: neighbor-autophagosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/autophagosome_membrane.yaml
  locator: Entire neighboring record
  accessed_at: '2026-10-21T11:04:47Z'
  support: context_only
  summary: The organelle, lumen and membrane records were read together to assess
    parthood, topology and the material-versus-structure distinction. An ignored-inclusive
    search of data/structures YAML for the three exact GO IDs returned these three
    paths; this is a bounded local search, not an ontology-wide absence claim.
- evidence_id: autophagosome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005776,GO:0000421,GO:0034423,GO:0060205,GO:0030659,GO:0016236,GO:0061909,GO:0000324
  locator: Exact id, name, isObsolete, definition, synonym, comment and child-relation
    fields of the eight requested terms
  accessed_at: '2026-10-21T11:00:18.510092Z'
  support: supports
  summary: All eight returned GO terms are active. Exact target definitions, labels
    and synonyms distinguish autophagosome GO:0005776, membrane GO:0000421 and lumen
    GO:0034423; the remaining terms identify the declared broad parent classes, macroautophagy,
    fungal vacuole and autophagosome-lysosome fusion. GO:0061909 explicitly includes
    yeast vacuole fusion and autophagic-body release. GO:0034423 distinguishes normal
    lumen residents from cargo destined for degradation.
  snapshot_sha256: fe74c39bb2d12700df800c03833e04ab0657e0ce6e25675ee35f98fe8b2d5a85
- evidence_id: autophagosome-agent-ancestors-0005776
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005776/ancestors?relations=is_a,part_of
  locator: Complete returned ancestor list for the exact target; relation types is_a
    and part_of
  accessed_at: '2026-10-21T11:00:19.040305Z'
  support: supports
  summary: The current GO is_a/part_of ancestry was checked as a bounded identity/hierarchy
    cross-check. The membrane/lumen GO ancestry uses vacuolar classifications; it
    does not itself establish the declared cytoplasmic-vesicle membrane/lumen parent.
    Those broad classifications are explicitly supported by the separately inspected
    UniProt location hierarchy.
  snapshot_sha256: cf61f376da609e840f241656a51bd5c45c67721def3d06321aa57d4a0e73443c
- evidence_id: autophagosome-agent-SL-0022-json
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0022.json
  locator: Exact id/name/definition, synonyms, geneOntologies, isA and partOf objects
  accessed_at: '2026-10-21T11:00:44.773680Z'
  support: supports
  summary: SL-0022 identifies autophagosome membrane and maps exactly to GO:0000421.
    All three maintained membrane synonyms match. Its isA location maps to GO:0030659
    and its partOf autophagosome maps to GO:0005776. The nested autophagosome definition
    distinguishes outer membrane fusion from release and lysis of the inner autophagic
    body.
  snapshot_sha256: eabd5326015a1e721e992120feec2b465d2137e7df7110ec6bcc3600fae87726
- evidence_id: autophagosome-agent-SL-0318-json
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0318.json
  locator: Exact id/name/definition, synonyms, geneOntologies, isA and partOf objects
  accessed_at: '2026-10-21T11:00:44.807013Z'
  support: supports
  summary: SL-0318 identifies autophagosome lumen and maps exactly to GO:0034423.
    All three maintained lumen synonyms match. Its isA cytoplasmic-vesicle lumen maps
    to GO:0060205 and its partOf autophagosome maps to GO:0005776.
  snapshot_sha256: ebef9b962bb00a5283ab0b9c024255499af7ceb9ebd05dec11e14fa5c9ded695
- evidence_id: autophagosome-agent-taxon-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-21T11:00:18.432042Z'
  support: supports
  summary: Native ENA taxonomy identifies taxon 4932 as Saccharomyces cerevisiae at
    species rank. This verifies the name/identifier pair; the experiments separately
    establish the biological occurrence and condition.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: autophagosome-agent-citations
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=20&query=DOI%3A10.1083/jcb.119.2.301%20OR%20DOI%3A10.1093/emboj/20.21.5971%20OR%20DOI%3A10.1038/35044114%20OR%20DOI%3A10.1038/ncb1007-1102
  locator: Complete four-result Europe PMC core response for exact DOI query
  accessed_at: '2026-10-21T11:00:18.863269Z'
  support: supports
  summary: 'The four exact DOI records were checked for titles, authors, journal/year,
    PMID and complete returned abstracts: Takeshige 1992 (10.1083/jcb.119.2.301),
    Suzuki 2001 (10.1093/emboj/20.21.5971), Ichimura 2000 (10.1038/35044114), and
    Xie/Klionsky 2007 (10.1038/ncb1007-1102). This metadata row alone does not attest
    a full-text read.'
  snapshot_sha256: 7ce86b23f517643beeefc7ce419961d24f0d2a2c80e460fc2ba5759463fe379f
- evidence_id: autophagosome-agent-takeshige1992-xml
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2289660.1/PMC2289660.1.xml
  locator: Abstract; Methods strains/media/starvation/microscopy; Results nutrient
    starvation and body accumulation; Discussion formation mechanism and normal autophagy
  accessed_at: '2026-10-21T11:00:44.647174Z'
  support: supports
  summary: Relevant Methods, starvation/autophagic-body Results and Discussion were
    read from the archived PMC article XML. Nutrient-starved yeast accumulated cytoplasm-containing
    autophagic bodies in vacuoles of proteinase-deficient cells, and PMSF permitted
    their observation in wild-type cells. These experiments support the qualified
    starvation-induced yeast occurrence and degradative endpoint. The Discussion explicitly
    does not resolve the body-formation mechanism; this paper is not treated as a
    direct assay of the later autophagosome-vacuole fusion mechanism.
  snapshot_sha256: d9234befa5757085ce8dd6be2333dbe0c6a49f3ae59c87f8904818a0f51ceec2
- evidence_id: autophagosome-agent-suzuki2001-publisher
  kind: primary_source
  reference: https://www.embopress.org/doi/full/10.1093/emboj/20.21.5971
  locator: Publisher Abstract; Introduction; Results functional GFP-Aut7/PAS, Apg
    proteins and autophagosome distinction; Discussion; Methods yeast media, plasmids
    and fluorescence microscopy
  accessed_at: '2026-10-21T11:01:20.869203Z'
  support: supports
  summary: The publisher full article supplied the relevant Introduction, Results
    on functional GFP-Aut7, PAS localization, autophagosome distinction and mutant
    transport, Discussion and Methods on yeast cultivation and fluorescence microscopy.
    These support S. cerevisiae as a genetic/fluorescence model for PAS and autophagosome
    formation. The article distinguishes the PAS from mature autophagosomes; it also
    describes phagophore extension/closure and vacuolar delivery in its Introduction.
    The review does not identify every PAS punctum as a mature autophagosome or claim
    an exhaustive mechanistic inventory.
  snapshot_sha256: 076e15057603b0fb39978191d651e5cb7070dfea3e389091bcf34184b37184a6
- evidence_id: autophagosome-agent-xie2007-publisher
  kind: authority
  reference: https://www.nature.com/articles/ncb1007-1102
  locator: Complete publisher abstract and bibliographic fields; full article body
    unavailable
  accessed_at: '2026-10-21T11:00:45.974758Z'
  support: partial
  summary: The publisher abstract and bibliographic information were readable. The
    abstract describes the double-membrane sequestering organelle, lysosomal cargo
    delivery and core ATG machinery for vesicle formation. The subscription page did
    not expose the full article body, so detailed review-text, figures or individual
    machinery necessity are not claimed as inspected.
  snapshot_sha256: 3b5b5641ad3b6cb09fe9a6b121572f00260af0bafec667c69497e38cbffd02d3
- evidence_id: autophagosome-agent-xie2007-pdf
  kind: authority
  reference: https://www.nature.com/articles/ncb1007-1102.pdf
  locator: Actual HTTP 200 text/html response at the PDF URL
  accessed_at: '2026-10-21T11:00:46.460388Z'
  support: context_only
  summary: The publisher PDF URL returned an HTML subscription/abstract page, not
    PDF article content. This is an access receipt only and provides no additional
    full-text evidence.
  snapshot_sha256: e150c7493af93a6b622ab02fcbf5b761f8ab62f8d3bb4d27ee50c7aaba2ab9bc
- evidence_id: autophagosome-agent-ichimura2000-publisher
  kind: primary_source
  reference: https://www.nature.com/articles/35044114
  locator: Abstract; Main Apg8-PE identification, Apg7/Apg3 dependence and discussion;
    Methods yeast, extraction and mass spectrometry
  accessed_at: '2026-10-21T11:00:46.163020Z'
  support: supports
  summary: The publisher abstract, relevant Main results/discussion and Methods were
    read. Mass spectrometry, biochemical treatment and yeast mutant assays establish
    Apg8 C-terminal conjugation to phosphatidylethanolamine and the Apg7/Apg3-dependent
    lipidation pathway. This supports the record discussion of Atg8 lipidation; it
    does not turn a source-level mechanism into a curated complete mature-organelle
    protein inventory.
  snapshot_sha256: 38b417b936e82c02ecc35be44339063f04657a3a3f58b4b5020fb57e7e5772a9
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml
    --verify
  locator: Exact focused native output
  accessed_at: '2026-10-21T11:02:02.603576Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml
    --causal-graphs
  locator: Exact focused native output
  accessed_at: '2026-10-21T11:02:03.216924Z'
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
  reference: just validate data/structures/membrane_organelle/autophagosome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:40:05Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/autophagosome.yaml'
  snapshot_sha256: d689dbe06a9ab72f40d8759b698a7fec464bd830e0055d542b30931ab2ee89e3
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/autophagosome.yaml
    --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/autophagosome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:40:06Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/autophagosome.yaml\
    \ --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/autophagosome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/autophagosome-strict.tsv"
  snapshot_sha256: 4190dcb83a4e70d3e7b11347c5ededbd6e11e827411a83e06dd5042aed33b0fa
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/autophagosome.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T11:04:47Z'
  support: supports
  summary: '11 of11 collected target identifiers returned OK in this fresh base resolver
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
  topic: Exact structure identity and synonymous boundaries
  outcome: supported
  target_ids:
  - GO:0005776
  summary: The target is the organelle, its enclosed lumen or its surrounding membrane
    as explicitly named, rather than the PAS, the later intravacuolar autophagic body,
    a generic process or an individual protein. Active native GO terms and exact UniProt
    location mappings support the separate identities; synonym scopes are preserved.
  evidence_ids:
  - autophagosome-agent-go
  - autophagosome-agent-SL-0022-json
  - autophagosome-agent-SL-0318-json
  - record
- assessment_id: hierarchy
  area: consistency
  topic: Parent classification and parthood
  outcome: supported
  target_ids:
  - GO:0005776
  summary: The sibling records consistently distinguish a membrane-bounded organelle
    from its membrane and enclosed volume. Parthood and boundary statements are supported.
    For the membrane and lumen, cytoplasmic-vesicle parent classes are explicitly
    native UniProt isA classifications, not assertions that those are current direct
    GO parent edges; current GO ancestry was separately examined.
  evidence_ids:
  - autophagosome-agent-go
  - autophagosome-agent-ancestors-0005776
  - autophagosome-agent-SL-0022-json
  - autophagosome-agent-SL-0318-json
  - neighbor-autophagosome_lumen
  - neighbor-autophagosome_membrane
- assessment_id: composition
  area: grounding
  topic: Component referent and essentiality
  outcome: supported
  target_ids:
  - GO:0005776
  summary: The single component refers to the structural autophagosome membrane, so
    GO:0000421 grounds that structural part rather than a chemical lipid species.
    ESSENTIAL is scoped to the collective double-bilayer boundary constitutive of
    this membrane-bounded organelle. It does not claim any individual Atg protein
    or lipid species is universally indispensable. The stated TODO honestly leaves
    Atg8 lipidation, Atg conjugation systems, Atg9 and fusion machinery for later
    component-level grounding.
  evidence_ids:
  - autophagosome-agent-go
  - autophagosome-agent-SL-0022-json
  - autophagosome-agent-SL-0318-json
  - policy
  - record
  - autophagosome-agent-ichimura2000-publisher
- assessment_id: taxa
  area: scope
  topic: Yeast occurrence and canonical experiment
  outcome: supported
  target_ids:
  - GO:0005776
  summary: The exact taxon is S. cerevisiae. COMMON is read together with its explicit
    starvation-induced macroautophagy note and the experimental induction evidence,
    not as a quantitative frequency across strains or all growth states. Takeshige
    establishes the conditioned phenotype; Suzuki supports the genetic/fluorescence
    model. Neither is generalized to all eukaryotic taxa or used to equate PAS with
    mature organelle.
  evidence_ids:
  - autophagosome-agent-taxon-4932
  - autophagosome-agent-takeshige1992-xml
  - autophagosome-agent-suzuki2001-publisher
  - autophagosome-agent-citations
- assessment_id: graph
  area: graph
  topic: Topological and coarse functional edges
  outcome: supported
  target_ids:
  - GO:0005776
  summary: Every maintained edge was read and remains NONMECHANISTIC. Membrane-bounds-lumen
    and parthood are direct topological statements. Where present, macroautophagy
    support and yeast vacuolar delivery are coarse functions grounded in native process
    definitions and source descriptions, not a complete Atg initiation, closure or
    fusion mechanism. The 1992 vacuolar-body result is not mislabeled here as direct
    mechanistic proof of fusion.
  evidence_ids:
  - autophagosome-agent-go
  - autophagosome-agent-SL-0022-json
  - autophagosome-agent-SL-0318-json
  - autophagosome-agent-takeshige1992-xml
  - autophagosome-agent-suzuki2001-publisher
  - record
- assessment_id: source-scope
  area: evidence
  topic: Bibliographic identity and claim-specific reading
  outcome: supported
  target_ids:
  - GO:0005776
  summary: Citations identify the stated papers. Primary studies were inspected at
    the explicitly recorded article sections; no figure-level reanalysis or uninspected
    full-text passage is certified. Source evidence supports the current bounded statements.
    Native identity mappings and descriptive endpoints are kept separate from protein-specific
    membership or assembly-necessity evidence.
  evidence_ids:
  - autophagosome-agent-citations
  - autophagosome-agent-takeshige1992-xml
  - autophagosome-agent-suzuki2001-publisher
  - autophagosome-agent-ichimura2000-publisher
  - autophagosome-agent-xie2007-publisher
- assessment_id: coverage
  area: completeness
  topic: Whole-record review with optional extensions
  outcome: supported
  target_ids:
  - GO:0005776
  summary: All maintained fields, source notes, history and neighboring topological
    records were inspected. Exact dimensions, numerical frequencies, images, traits,
    protein examples and exhaustive machinery inventories are not asserted; their
    absence alone is not a defect. No quoted source passage in the record requires
    quotation repair. Individual molecular necessity remains outside this bounded
    structural assessment.
  evidence_ids:
  - record
  - policy
  - neighbor-autophagosome_lumen
  - neighbor-autophagosome_membrane
  - autophagosome-agent-go
  - autophagosome-agent-ancestors-0005776
  - autophagosome-agent-SL-0022-json
  - autophagosome-agent-SL-0318-json
  - autophagosome-agent-taxon-4932
  - autophagosome-agent-citations
  - autophagosome-agent-takeshige1992-xml
  - autophagosome-agent-suzuki2001-publisher
  - autophagosome-agent-xie2007-publisher
  - autophagosome-agent-xie2007-pdf
  - autophagosome-agent-ichimura2000-publisher
findings: []
actions: []
limitations:
- The review covers the exact maintained record and stated source sections, not an
  exhaustive literature or component inventory. Protein-specific formation necessity
  and generic lipid chemical identity are not newly established.
- Xie and Klionsky 2007 was accessible at abstract/bibliographic scope only. The publisher
  PDF route returned HTML subscription content; the full article and figures were
  not read. No detailed individual-machinery claim relies solely on unseen text.
- The primary papers were read at the explicitly named Methods/Results/Discussion
  sections; all image panels and underlying microscopy data were not reanalysed. Historical
  curator searches and independent historical authorship are not certified.
- The fresh-base batch15 global gates are attached by root only at finalization. This
  draft contains the actual focused checks and exact fresh-base target resolver slice.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized a review for every uncovered target, including targets
  without findings. Only root may finalize or save this review bundle.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
