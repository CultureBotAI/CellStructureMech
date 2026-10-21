# Envelope identity, composition and evidence review

- Review: 20261021T101615Z-fungal-type-cell-wall-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:59:31Z
- Finished UTC: 2026-10-21T10:16:15Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The fungal-wall identity, scoped composition, functions and four protein examples are supported. No concrete curation issue was found within the stated source and assembly-necessity limits.

## Scope And Provenance

Entire single record with exact authority identities, declared source-reading scopes, protein checks where applicable and component/function/graph boundaries.

Selection: Target 4 in batch eighteen; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009277 | data/structures/envelope/fungal_type_cell_wall.yaml | maintained | fungal-type cell wall |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0009277 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Native protein causal-graphs | passed | True | GO:0009277 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Focused native schema | passed | True | GO:0009277 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009277 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0009277 | 15 identifiers OK; 3 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0009277 | No expression-module or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | GO:0009277 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0009277 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009277 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009277 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009277 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0009277 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Variable fungal wall with a separate capsule

identity: supported. Targets: GO:0009277.

The exact identity, narrow synonym, broad parent and membrane/capsule boundaries are supported. The definition is a restrained paraphrase of the native GO definition; it does not assert that all fungal walls contain chitin or identical proportions.

### Chemical classes and heterogeneous mannoproteins

grounding: supported. Targets: GO:0009277.

Beta-D-glucan and chitin use matching material-class CURIEs; their linkage and contribution remain source-qualified. The collective mannoprotein row spans unrelated proteins and attachment modes, so one sequence-family identifier would be narrower than the component. Specific protein examples do not convert this class into a single family.

### Four correct taxon-paired proteins and exact localization attribution

evidence: supported. Targets: GO:0009277.

All four reviewed accession/name/gene/strain pairs match current native records and uniquely resolve in the declared reviewed exact-gene queries. GAS1 PMID notes faithfully describe UniProt Cell membrane localization; they are not relabeled as cell-wall experiments. Native Gas1 also reports a wall-bound pool, and the inspected Orlean body independently supports wall-bound Gas1. No wrong-compartment finding is inferred from the legitimate membrane pool.

### Conditional components do not prove universal formation necessity

evidence: unknown. Targets: GO:0009277.

The reviews show species and growth-state variation and compensatory responses. Their membership, cell-wall sensitivity and viability observations do not by themselves establish that the entire structure cannot form without each broad component. The current CONDITIONAL rows are not converted into universal essentiality or a new dispensability claim; exact necessity remains unresolved here.

### Qualified fungal occurrence and model examples

scope: supported. Targets: GO:0009277.

Fungi, S.cerevisiae and C.neoformans identities agree with native taxonomy. The reviews support the stated model wall and capsule context. COMMON is a qualitative statement about most vegetative fungal cells, with composition/growth-state variation already acknowledged; no prevalence census is claimed.

### Supported wall functions and descriptive architecture

graph: supported. Targets: GO:0009277.

Osmotic integrity, shape and environmental interactions are supported at the review and model-organism scopes. Cross-links, wall glycoproteins and membrane enclosure are represented by an explicitly NONMECHANISTIC graph whose scope note already avoids a universal composition claim.

### Bounded record-level coverage

completeness: supported. Targets: GO:0009277.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Exact additional polymer inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. A clean result does not assert exhaustive literature completeness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/envelope/fungal_type_cell_wall.yaml; Entire maintained YAML including history, all evidence notes, components, functions, graph edges and discussions | context_only | All maintained fields were read. No scientific edit or mapping-status promotion is made. |
| policy | docs/CURATION.md; Exact identity, claim-level evidence, material versus localization grounding, and component assembly-essentiality contract | context_only | Family identity, concrete protein examples and structure membership are separate; activity and viability are not by themselves formation assays. Optional inventories are not mandatory. |
| root18-sources-fungal-wall-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005618,GO:0005886,GO:0009277; All three exact returned terms: definitions, synonyms and relevant inverse child relations | supports | GO0009277 supports the broad variable fungal wall, its narrow chitin/beta-glucan synonym, cell-wall parent and exclusion of an external capsule. GO0005886 identifies the enclosed plasma membrane. The literature-sourced exact fungal-cell-wall synonym is not falsely attributed to GO. |
| root18-sources-CHEBI-28793 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/28793/; Exact accession, name, definition where present, synonyms and chemical-class relations | supports | Released three-star CHEBI:28793 identifies beta-D-glucan. Its chemical-class identity and returned definition/ontology relations are assessed independently of placement in a wall or membrane. |
| root18-sources-CHEBI-17029 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/17029/; Exact accession, name, definition where present, synonyms and chemical-class relations | supports | Released three-star CHEBI:17029 identifies chitin. Its chemical-class identity and returned definition/ontology relations are assessed independently of placement in a wall or membrane. |
| root18-sources-NCBITaxon-4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Fungi at kingdom rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-NCBITaxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Saccharomyces cerevisiae at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-NCBITaxon-5207 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5207; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Cryptococcus neoformans at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-NCBITaxon-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Saccharomyces cerevisiae S288C at strain rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-doi-10.1128_microbiolspec.FUNK-0035-2016 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/microbiolspec.FUNK-0035-2016; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies The Fungal Cell Wall: Structure, Biosynthesis, and Function. PMID 28513415; DOI 10.1128/microbiolspec.funk-0035-2016. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-doi-10.1534_genetics.112.144485 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1534/genetics.112.144485; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Architecture and biosynthesis of the Saccharomyces cerevisiae cell wall. PMID 23135325; DOI 10.1534/genetics.112.144485. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-legacy-PMC11687499 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11687499/; Genuine PMC HTML: Abstract/Introduction and complete composition paragraphs12–28 with Fig1 caption; Cell Wall Proteins paragraphs52–68; immune-recognition/capsule context93–100. No complete biosynthetic/regulatory chapter or figure-pixel read claimed. | supports | Gow, Latge and Munro2017 is review-tier evidence for variable fungal wall polymers, cross-links, glycoprotein classes and environmental interactions. It distinguishes Cryptococcus capsule from the underlying wall, describes species differences, and does not give one universal wall protein family or polymer recipe. |
| root18-sources-legacy-PMC3522159 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3522159/; Genuine PMC HTML: Abstract/Introduction and entire Wall Composition and Architecture paragraphs11–43; cross-link context191/232; Gas1 family250–253; Tip1/Cwp1/Cwp2 and Sed1/Spi1 paragraphs262–267. No whole44-page review or supplements claim. | supports | Orlean2012 supports the S.cerevisiae wall, glucan/chitin cross-links, differently attached mannoproteins and variable growth/stress composition. Named sections support Cwp1/Cwp2, Sed1 and Gas1 wall association, including covalent wall-bound Gas1 as well as its membrane-linked pool. These examples do not imply that one protein is universally necessary for all fungal walls. |
| root18-sources-UniProtKB-P28319 | https://rest.uniprot.org/uniprotkb/P28319.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is P28319, UniProtKB reviewed (Swiss-Prot), organism taxon 559292. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root18-sources-UniProtKB-P43497 | https://rest.uniprot.org/uniprotkb/P43497.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is P43497, UniProtKB reviewed (Swiss-Prot), organism taxon 559292. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root18-sources-UniProtKB-Q01589 | https://rest.uniprot.org/uniprotkb/Q01589.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is Q01589, UniProtKB reviewed (Swiss-Prot), organism taxon 559292. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root18-sources-UniProtKB-P22146 | https://rest.uniprot.org/uniprotkb/P22146.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is P22146, UniProtKB reviewed (Swiss-Prot), organism taxon 559292. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root18-sources-query-CWP1-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ACWP1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for gene_exact, taxonomy_id and reviewed:true | supports | Current exact-gene/taxon reviewed query returned 1 entries: P28319. Returned gene tokens were checked against each native entry; zero reviewed matches do not invalidate a separately identified unreviewed sequence. |
| root18-sources-query-CWP2-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ACWP2%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for gene_exact, taxonomy_id and reviewed:true | supports | Current exact-gene/taxon reviewed query returned 1 entries: P43497. Returned gene tokens were checked against each native entry; zero reviewed matches do not invalidate a separately identified unreviewed sequence. |
| root18-sources-query-SED1-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ASED1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for gene_exact, taxonomy_id and reviewed:true | supports | Current exact-gene/taxon reviewed query returned 1 entries: Q01589. Returned gene tokens were checked against each native entry; zero reviewed matches do not invalidate a separately identified unreviewed sequence. |
| root18-sources-query-GAS1-559292 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AGAS1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for gene_exact, taxonomy_id and reviewed:true | supports | Current exact-gene/taxon reviewed query returned 1 entries: P22146. Returned gene tokens were checked against each native entry; zero reviewed matches do not invalidate a separately identified unreviewed sequence. |
| root18-sources-PMID-18434410 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A18434410%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies An engineered Saccharomyces cerevisiae strain binds the broadly neutralizing human immunodeficiency virus type 1 antibody 2G12 and elicits mannose-specific gp120-binding antibodies. PMID 18434410; DOI 10.1128/jvi.00412-08. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-PMID-3046936 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A3046936%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies A major 125-kd membrane glycoprotein of Saccharomyces cerevisiae is attached to the lipid bilayer through an inositol-containing phospholipid. PMID 3046936; DOI 10.1002/j.1460-2075.1988.tb03063.x. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-PMID-3072201 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A3072201%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Immunochemical characterization of gp115, a yeast glycoprotein modulated by the cell cycle. PMID 3072201; DOI not returned. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| native-verify | /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/fungal_type_cell_wall.yaml --verify; Exact focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/fungal_type_cell_wall.yaml --causal-graphs; Exact focused native output | supports | data/structures/envelope/fungal_type_cell_wall.yaml  (GO:0009277)<br>  crosslinked_polysaccharide_wall_network	wall_mannoproteins	COVERED	-&gt;wall_mannoproteins (UniProtKB:P28319, UniProtKB:P43497, UniProtKB:Q01589, UniProtKB:P22146)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/envelope/fungal_type_cell_wall.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/envelope/fungal_type_cell_wall.yaml |
| strict-result | just validate-strict data/structures/envelope/fungal_type_cell_wall.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/fungal_type_cell_wall-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/envelope/fungal_type_cell_wall.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/fungal_type_cell_wall-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/fungal_type_cell_wall-strict.tsv |
| target-curies | just check-curies-strict; data/structures/envelope/fungal_type_cell_wall.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 15 of18 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:18434410: UNREACHABLE; resolved by evidence root18-sources-PMID-18434410; PMID:3046936: UNREACHABLE; resolved by evidence root18-sources-PMID-3046936; PMID:3072201: UNREACHABLE; resolved by evidence root18-sources-PMID-3072201. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Gow and Orlean are reviews, read only at the exact named sections. Their underlying primary experiments and all biochemical mechanisms were not independently reanalysed.
- The three GAS1 localization publications were checked by exact native metadata/abstract and UniProt location-evidence linkage, not full bodies. Membrane localization remains distinct from the wall evidence in Orlean.
- Current protein identity checks do not certify the historical retrieval date or prove universal assembly necessity.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization; identifier transport and label-adapter limits remain explicit.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for every uncovered target, including a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101615Z-fungal-type-cell-wall-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Envelope identity, composition and evidence review
started_at: '2026-10-21T09:59:31Z'
finished_at: '2026-10-21T10:16:15Z'
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
summary: The fungal-wall identity, scoped composition, functions and four protein
  examples are supported. No concrete curation issue was found within the stated source
  and assembly-necessity limits.
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
  - path: data/structures/envelope/fungal_type_cell_wall.yaml
    sha256: 4baef5e8cd747edc51bba48a001e2284ca225b28a25d153629006ef1ab782f64
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
  - path: scripts/score_causal_graphs.py
    sha256: 5ffe450c5b37c3dc3b0e62672caf0d99b358c8249fcc98a8c4fc7d78e8cd0d2f
    role: context
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0009277
  path: data/structures/envelope/fungal_type_cell_wall.yaml
  label: fungal-type cell wall
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/fungal_type_cell_wall.yaml
    role: maintained scientific record
scope:
  description: Entire single record with exact authority identities, declared source-reading
    scopes, protein checks where applicable and component/function/graph boundaries.
  selection: Target 4 in batch eighteen; exact sorted uncovered path at frozen fresh-main
    revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009277
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0009277
  command: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/fungal_type_cell_wall.yaml
    --verify
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0009277
  command: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/fungal_type_cell_wall.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009277
  command: just validate data/structures/envelope/fungal_type_cell_wall.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009277
  command: just validate-strict data/structures/envelope/fungal_type_cell_wall.yaml
    --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/fungal_type_cell_wall-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0009277
  summary: 15 identifiers OK; 3 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - root18-sources-PMID-18434410
  - root18-sources-PMID-3046936
  - root18-sources-PMID-3072201
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0009277
  summary: No expression-module or transcriptomic inference is made by this structural
    review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009277
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - root18-sources-fungal-wall-go
  - root18-sources-CHEBI-28793
  - root18-sources-CHEBI-17029
  - root18-sources-NCBITaxon-4751
  - root18-sources-NCBITaxon-4932
  - root18-sources-NCBITaxon-5207
  - root18-sources-NCBITaxon-559292
  - root18-sources-doi-10.1128_microbiolspec.FUNK-0035-2016
  - root18-sources-doi-10.1534_genetics.112.144485
  - root18-sources-legacy-PMC11687499
  - root18-sources-legacy-PMC3522159
  - root18-sources-UniProtKB-P28319
  - root18-sources-UniProtKB-P43497
  - root18-sources-UniProtKB-Q01589
  - root18-sources-UniProtKB-P22146
  - root18-sources-query-CWP1-559292
  - root18-sources-query-CWP2-559292
  - root18-sources-query-SED1-559292
  - root18-sources-query-GAS1-559292
  - root18-sources-PMID-18434410
  - root18-sources-PMID-3046936
  - root18-sources-PMID-3072201
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009277
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
  - GO:0009277
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
  - GO:0009277
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
  - GO:0009277
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
  - GO:0009277
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
  reference: data/structures/envelope/fungal_type_cell_wall.yaml
  locator: Entire maintained YAML including history, all evidence notes, components,
    functions, graph edges and discussions
  accessed_at: '2026-10-21T10:07:58Z'
  support: context_only
  summary: All maintained fields were read. No scientific edit or mapping-status promotion
    is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, claim-level evidence, material versus localization grounding,
    and component assembly-essentiality contract
  accessed_at: '2026-10-21T10:07:58Z'
  support: context_only
  summary: Family identity, concrete protein examples and structure membership are
    separate; activity and viability are not by themselves formation assays. Optional
    inventories are not mandatory.
- evidence_id: root18-sources-fungal-wall-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005618,GO:0005886,GO:0009277
  locator: 'All three exact returned terms: definitions, synonyms and relevant inverse
    child relations'
  accessed_at: '2026-10-21T10:00:57.282374Z'
  support: supports
  summary: GO0009277 supports the broad variable fungal wall, its narrow chitin/beta-glucan
    synonym, cell-wall parent and exclusion of an external capsule. GO0005886 identifies
    the enclosed plasma membrane. The literature-sourced exact fungal-cell-wall synonym
    is not falsely attributed to GO.
  snapshot_sha256: bf5396e95ec4d1ec713c39d51dfd629b528f0dec74b3a194dd6ec48fb2c85c88
- evidence_id: root18-sources-CHEBI-28793
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/28793/
  locator: Exact accession, name, definition where present, synonyms and chemical-class
    relations
  accessed_at: '2026-10-21T10:00:57.907426Z'
  support: supports
  summary: Released three-star CHEBI:28793 identifies beta-D-glucan. Its chemical-class
    identity and returned definition/ontology relations are assessed independently
    of placement in a wall or membrane.
  snapshot_sha256: 262e8b077edeaaf9d7734e03846b9e37879ad8d1b3fd480b893682c0669c8283
- evidence_id: root18-sources-CHEBI-17029
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/17029/
  locator: Exact accession, name, definition where present, synonyms and chemical-class
    relations
  accessed_at: '2026-10-21T10:00:57.318418Z'
  support: supports
  summary: Released three-star CHEBI:17029 identifies chitin. Its chemical-class identity
    and returned definition/ontology relations are assessed independently of placement
    in a wall or membrane.
  snapshot_sha256: 7c415fb77b4409029942e424c08178e97b0282a0c24214f799bd5e69e235944e
- evidence_id: root18-sources-NCBITaxon-4751
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:00:57.280842Z'
  support: supports
  summary: Native ENA taxonomy identifies Fungi at kingdom rank. Only this taxon's
    identity and names are asserted by this row, not occurrence or experimental stock
    identity.
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: root18-sources-NCBITaxon-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:00:57.288389Z'
  support: supports
  summary: Native ENA taxonomy identifies Saccharomyces cerevisiae at species rank.
    Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: root18-sources-NCBITaxon-5207
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5207
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:00:57.273511Z'
  support: supports
  summary: Native ENA taxonomy identifies Cryptococcus neoformans at species rank.
    Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: 01d4433d3abf63df415058063ffa2eb63e97970f8de2ffdd2a250fc0f572114c
- evidence_id: root18-sources-NCBITaxon-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:00:57.230520Z'
  support: supports
  summary: Native ENA taxonomy identifies Saccharomyces cerevisiae S288C at strain
    rank. Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root18-sources-doi-10.1128_microbiolspec.FUNK-0035-2016
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/microbiolspec.FUNK-0035-2016
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:00:58.680404Z'
  support: supports
  summary: 'Native citation identifies The Fungal Cell Wall: Structure, Biosynthesis,
    and Function. PMID 28513415; DOI 10.1128/microbiolspec.funk-0035-2016. Bibliographic
    fields and returned abstract were inspected; this row does not attest a full-text
    read.'
  snapshot_sha256: eeb7e69ec2cdeb8220f9e7bfb99c48d69c7dbbab3bb53479570d15a7ec32a070
- evidence_id: root18-sources-doi-10.1534_genetics.112.144485
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1534/genetics.112.144485
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:00:58.737654Z'
  support: supports
  summary: Native citation identifies Architecture and biosynthesis of the Saccharomyces
    cerevisiae cell wall. PMID 23135325; DOI 10.1534/genetics.112.144485. Bibliographic
    fields and returned abstract were inspected; this row does not attest a full-text
    read.
  snapshot_sha256: 936251ccea65f9f9be6455a0ab65b2735a5783404cc109d7447892182e574ebf
- evidence_id: root18-sources-legacy-PMC11687499
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11687499/
  locator: 'Genuine PMC HTML: Abstract/Introduction and complete composition paragraphs12–28
    with Fig1 caption; Cell Wall Proteins paragraphs52–68; immune-recognition/capsule
    context93–100. No complete biosynthetic/regulatory chapter or figure-pixel read
    claimed.'
  accessed_at: '2026-10-21T10:02:33.446763Z'
  support: supports
  summary: Gow, Latge and Munro2017 is review-tier evidence for variable fungal wall
    polymers, cross-links, glycoprotein classes and environmental interactions. It
    distinguishes Cryptococcus capsule from the underlying wall, describes species
    differences, and does not give one universal wall protein family or polymer recipe.
  snapshot_sha256: ccd99579302a7f2e3d90d2b13028e83a4288badc352a9f3f59f295c1377cff08
- evidence_id: root18-sources-legacy-PMC3522159
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3522159/
  locator: 'Genuine PMC HTML: Abstract/Introduction and entire Wall Composition and
    Architecture paragraphs11–43; cross-link context191/232; Gas1 family250–253; Tip1/Cwp1/Cwp2
    and Sed1/Spi1 paragraphs262–267. No whole44-page review or supplements claim.'
  accessed_at: '2026-10-21T10:02:33.588671Z'
  support: supports
  summary: Orlean2012 supports the S.cerevisiae wall, glucan/chitin cross-links, differently
    attached mannoproteins and variable growth/stress composition. Named sections
    support Cwp1/Cwp2, Sed1 and Gas1 wall association, including covalent wall-bound
    Gas1 as well as its membrane-linked pool. These examples do not imply that one
    protein is universally necessary for all fungal walls.
  snapshot_sha256: 3305fa267a12ceed023227aba1864be8d440459d298e5321792fe3ed99eb4046
- evidence_id: root18-sources-UniProtKB-P28319
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P28319.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:00:58.008723Z'
  support: supports
  summary: The primary accession is P28319, UniProtKB reviewed (Swiss-Prot), organism
    taxon 559292. Exact name/gene tokens, evidence-qualified location comments and
    linked publication metadata were inspected. Database identity is not independently
    a formation-necessity experiment.
  snapshot_sha256: dc39da2266cd6a391d46f76e47af717e049e1714ada800a885f2e418e3f25886
- evidence_id: root18-sources-UniProtKB-P43497
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P43497.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:00:58.025395Z'
  support: supports
  summary: The primary accession is P43497, UniProtKB reviewed (Swiss-Prot), organism
    taxon 559292. Exact name/gene tokens, evidence-qualified location comments and
    linked publication metadata were inspected. Database identity is not independently
    a formation-necessity experiment.
  snapshot_sha256: d8c646a16e8daa253d11239cc3a75a7e6e5e8c5549a9e5acbcd345f8a8e273a4
- evidence_id: root18-sources-UniProtKB-Q01589
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q01589.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:00:58.037146Z'
  support: supports
  summary: The primary accession is Q01589, UniProtKB reviewed (Swiss-Prot), organism
    taxon 559292. Exact name/gene tokens, evidence-qualified location comments and
    linked publication metadata were inspected. Database identity is not independently
    a formation-necessity experiment.
  snapshot_sha256: fbf15af0f0849402dd5f4054c45eb7ce98389d089759f299893a0d44191d0f5e
- evidence_id: root18-sources-UniProtKB-P22146
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P22146.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:00:57.935752Z'
  support: supports
  summary: The primary accession is P22146, UniProtKB reviewed (Swiss-Prot), organism
    taxon 559292. Exact name/gene tokens, evidence-qualified location comments and
    linked publication metadata were inspected. Database identity is not independently
    a formation-necessity experiment.
  snapshot_sha256: fc316b4a780273f86f60dd00fc418abe4140e985203c96293a98fdffaf7e32e7
- evidence_id: root18-sources-query-CWP1-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ACWP1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for gene_exact, taxonomy_id and reviewed:true
  accessed_at: '2026-10-21T10:00:58.741568Z'
  support: supports
  summary: 'Current exact-gene/taxon reviewed query returned 1 entries: P28319. Returned
    gene tokens were checked against each native entry; zero reviewed matches do not
    invalidate a separately identified unreviewed sequence.'
  snapshot_sha256: 25bc37b7135a91abf3ade027ab0d20e1cd5bc9664381079087e4e7618b3b6d82
- evidence_id: root18-sources-query-CWP2-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ACWP2%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for gene_exact, taxonomy_id and reviewed:true
  accessed_at: '2026-10-21T10:00:58.895470Z'
  support: supports
  summary: 'Current exact-gene/taxon reviewed query returned 1 entries: P43497. Returned
    gene tokens were checked against each native entry; zero reviewed matches do not
    invalidate a separately identified unreviewed sequence.'
  snapshot_sha256: 01ef49e228558709b45a3e7719fde102ad214d8402535ee1f4565529986d72b6
- evidence_id: root18-sources-query-SED1-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ASED1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for gene_exact, taxonomy_id and reviewed:true
  accessed_at: '2026-10-21T10:00:59.357207Z'
  support: supports
  summary: 'Current exact-gene/taxon reviewed query returned 1 entries: Q01589. Returned
    gene tokens were checked against each native entry; zero reviewed matches do not
    invalidate a separately identified unreviewed sequence.'
  snapshot_sha256: 237e8a88b4a770f59e171ed3dc84ca1828da88e9f6846371e23d4f37878279a4
- evidence_id: root18-sources-query-GAS1-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AGAS1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for gene_exact, taxonomy_id and reviewed:true
  accessed_at: '2026-10-21T10:00:59.453019Z'
  support: supports
  summary: 'Current exact-gene/taxon reviewed query returned 1 entries: P22146. Returned
    gene tokens were checked against each native entry; zero reviewed matches do not
    invalidate a separately identified unreviewed sequence.'
  snapshot_sha256: fd1ea841d93d3ae5a6e4a83e8730c91b50ffa02e32f6983053934cff16ba7524
- evidence_id: root18-sources-PMID-18434410
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A18434410%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:00:58.134576Z'
  support: supports
  summary: Native citation identifies An engineered Saccharomyces cerevisiae strain
    binds the broadly neutralizing human immunodeficiency virus type 1 antibody 2G12
    and elicits mannose-specific gp120-binding antibodies. PMID 18434410; DOI 10.1128/jvi.00412-08.
    Bibliographic fields and returned abstract were inspected; this row does not attest
    a full-text read.
  snapshot_sha256: eee1f5e6f879a79e76531578d0a905ed5f0abd753407b5d035610181429d3934
- evidence_id: root18-sources-PMID-3046936
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A3046936%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:00:58.555462Z'
  support: supports
  summary: Native citation identifies A major 125-kd membrane glycoprotein of Saccharomyces
    cerevisiae is attached to the lipid bilayer through an inositol-containing phospholipid.
    PMID 3046936; DOI 10.1002/j.1460-2075.1988.tb03063.x. Bibliographic fields and
    returned abstract were inspected; this row does not attest a full-text read.
  snapshot_sha256: 0aca115bbdc75137a26372a3843d4e41fa47a6c40dc6d08405fc716ade6d928c
- evidence_id: root18-sources-PMID-3072201
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A3072201%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:00:58.643182Z'
  support: supports
  summary: Native citation identifies Immunochemical characterization of gp115, a
    yeast glycoprotein modulated by the cell cycle. PMID 3072201; DOI not returned.
    Bibliographic fields and returned abstract were inspected; this row does not attest
    a full-text read.
  snapshot_sha256: 133bacc66badfdeec17aad35510334ef80e485271c8c7444272afbdbab2030f1
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/fungal_type_cell_wall.yaml
    --verify
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:03:56.608425Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/fungal_type_cell_wall.yaml
    --causal-graphs
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:03:57.113127Z'
  support: supports
  summary: "data/structures/envelope/fungal_type_cell_wall.yaml  (GO:0009277)\n  crosslinked_polysaccharide_wall_network\t\
    wall_mannoproteins\tCOVERED\t->wall_mannoproteins (UniProtKB:P28319, UniProtKB:P43497,\
    \ UniProtKB:Q01589, UniProtKB:P22146)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n\
    \     1  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref\
    \ on the node\n     1  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 06aded19ed4fa63d2b27899d0b797bd2024c3500eab4c0894d96fec5fb874f0e
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/envelope/fungal_type_cell_wall.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:33Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/envelope/fungal_type_cell_wall.yaml'
  snapshot_sha256: 80805a2dc33dc08bbf7de029c6ee106086c11993a9b5dd204bad8a22be37c4ed
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/envelope/fungal_type_cell_wall.yaml
    --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/fungal_type_cell_wall-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:35Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/envelope/fungal_type_cell_wall.yaml\
    \ --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/fungal_type_cell_wall-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/fungal_type_cell_wall-strict.tsv"
  snapshot_sha256: c049946061274659d7b275d7926fea82374d80271213aaec3576193e8427e404
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/envelope/fungal_type_cell_wall.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:07:58Z'
  support: supports
  summary: '15 of18 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:18434410: UNREACHABLE; resolved by evidence root18-sources-PMID-18434410;
    PMID:3046936: UNREACHABLE; resolved by evidence root18-sources-PMID-3046936; PMID:3072201:
    UNREACHABLE; resolved by evidence root18-sources-PMID-3072201. Source-native identity
    checked separately.'
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
  topic: Variable fungal wall with a separate capsule
  outcome: supported
  target_ids:
  - GO:0009277
  summary: The exact identity, narrow synonym, broad parent and membrane/capsule boundaries
    are supported. The definition is a restrained paraphrase of the native GO definition;
    it does not assert that all fungal walls contain chitin or identical proportions.
  evidence_ids:
  - root18-sources-fungal-wall-go
  - root18-sources-legacy-PMC11687499
  - root18-sources-legacy-PMC3522159
  - record
- assessment_id: composition
  area: grounding
  topic: Chemical classes and heterogeneous mannoproteins
  outcome: supported
  target_ids:
  - GO:0009277
  summary: Beta-D-glucan and chitin use matching material-class CURIEs; their linkage
    and contribution remain source-qualified. The collective mannoprotein row spans
    unrelated proteins and attachment modes, so one sequence-family identifier would
    be narrower than the component. Specific protein examples do not convert this
    class into a single family.
  evidence_ids:
  - root18-sources-fungal-wall-go
  - root18-sources-CHEBI-28793
  - root18-sources-CHEBI-17029
  - root18-sources-legacy-PMC11687499
  - root18-sources-legacy-PMC3522159
  - root18-sources-UniProtKB-P28319
  - root18-sources-UniProtKB-P43497
  - root18-sources-UniProtKB-Q01589
  - root18-sources-UniProtKB-P22146
  - record
  - policy
- assessment_id: protein
  area: evidence
  topic: Four correct taxon-paired proteins and exact localization attribution
  outcome: supported
  target_ids:
  - GO:0009277
  summary: All four reviewed accession/name/gene/strain pairs match current native
    records and uniquely resolve in the declared reviewed exact-gene queries. GAS1
    PMID notes faithfully describe UniProt Cell membrane localization; they are not
    relabeled as cell-wall experiments. Native Gas1 also reports a wall-bound pool,
    and the inspected Orlean body independently supports wall-bound Gas1. No wrong-compartment
    finding is inferred from the legitimate membrane pool.
  evidence_ids:
  - root18-sources-UniProtKB-P28319
  - root18-sources-UniProtKB-P43497
  - root18-sources-UniProtKB-Q01589
  - root18-sources-UniProtKB-P22146
  - root18-sources-query-CWP1-559292
  - root18-sources-query-CWP2-559292
  - root18-sources-query-SED1-559292
  - root18-sources-query-GAS1-559292
  - root18-sources-PMID-18434410
  - root18-sources-PMID-3046936
  - root18-sources-PMID-3072201
  - root18-sources-legacy-PMC3522159
  - root18-sources-NCBITaxon-4751
  - root18-sources-NCBITaxon-4932
  - root18-sources-NCBITaxon-5207
  - root18-sources-NCBITaxon-559292
  - record
- assessment_id: necessity
  area: evidence
  topic: Conditional components do not prove universal formation necessity
  outcome: unknown
  target_ids:
  - GO:0009277
  summary: The reviews show species and growth-state variation and compensatory responses.
    Their membership, cell-wall sensitivity and viability observations do not by themselves
    establish that the entire structure cannot form without each broad component.
    The current CONDITIONAL rows are not converted into universal essentiality or
    a new dispensability claim; exact necessity remains unresolved here.
  evidence_ids:
  - root18-sources-legacy-PMC11687499
  - root18-sources-legacy-PMC3522159
  - record
  - policy
- assessment_id: scope
  area: scope
  topic: Qualified fungal occurrence and model examples
  outcome: supported
  target_ids:
  - GO:0009277
  summary: Fungi, S.cerevisiae and C.neoformans identities agree with native taxonomy.
    The reviews support the stated model wall and capsule context. COMMON is a qualitative
    statement about most vegetative fungal cells, with composition/growth-state variation
    already acknowledged; no prevalence census is claimed.
  evidence_ids:
  - root18-sources-legacy-PMC11687499
  - root18-sources-legacy-PMC3522159
  - root18-sources-NCBITaxon-4751
  - root18-sources-NCBITaxon-4932
  - root18-sources-NCBITaxon-5207
  - root18-sources-NCBITaxon-559292
  - record
- assessment_id: function-graph
  area: graph
  topic: Supported wall functions and descriptive architecture
  outcome: supported
  target_ids:
  - GO:0009277
  summary: Osmotic integrity, shape and environmental interactions are supported at
    the review and model-organism scopes. Cross-links, wall glycoproteins and membrane
    enclosure are represented by an explicitly NONMECHANISTIC graph whose scope note
    already avoids a universal composition claim.
  evidence_ids:
  - root18-sources-fungal-wall-go
  - root18-sources-legacy-PMC11687499
  - root18-sources-legacy-PMC3522159
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - GO:0009277
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Exact additional polymer inventories, numerical properties,
    images, traits and expanded mechanisms are optional. No verbatim quotation requires
    repair, and no status or history rewrite is proposed. A clean result does not
    assert exhaustive literature completeness.
  evidence_ids:
  - record
  - policy
  - root18-sources-fungal-wall-go
  - root18-sources-CHEBI-28793
  - root18-sources-CHEBI-17029
  - root18-sources-NCBITaxon-4751
  - root18-sources-NCBITaxon-4932
  - root18-sources-NCBITaxon-5207
  - root18-sources-NCBITaxon-559292
  - root18-sources-doi-10.1128_microbiolspec.FUNK-0035-2016
  - root18-sources-doi-10.1534_genetics.112.144485
  - root18-sources-legacy-PMC11687499
  - root18-sources-legacy-PMC3522159
  - root18-sources-UniProtKB-P28319
  - root18-sources-UniProtKB-P43497
  - root18-sources-UniProtKB-Q01589
  - root18-sources-UniProtKB-P22146
  - root18-sources-query-CWP1-559292
  - root18-sources-query-CWP2-559292
  - root18-sources-query-SED1-559292
  - root18-sources-query-GAS1-559292
  - root18-sources-PMID-18434410
  - root18-sources-PMID-3046936
  - root18-sources-PMID-3072201
findings: []
actions: []
limitations:
- Gow and Orlean are reviews, read only at the exact named sections. Their underlying
  primary experiments and all biochemical mechanisms were not independently reanalysed.
- The three GAS1 localization publications were checked by exact native metadata/abstract
  and UniProt location-evidence linkage, not full bodies. Membrane localization remains
  distinct from the wall evidence in Orlean.
- Current protein identity checks do not certify the historical retrieval date or
  prove universal assembly necessity.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches
  and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization;
  identifier transport and label-adapter limits remain explicit.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized one review for every uncovered target, including
  a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
