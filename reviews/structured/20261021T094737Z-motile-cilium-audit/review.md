# Motile cilium scope, IFT examples and graph evidence review

- Review: 20261021T094737Z-motile-cilium-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:07:31Z
- Finished UTC: 2026-10-21T09:47:37Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Motile-cilium identity, coarse composition and exact IFT examples are supported. Two minor issues concern unqualified mastigoneme scope and the mechanism label/product-to-assembly edge.

## Scope And Provenance

Whole single target and identity-only neighboring context; all native terms and five protein examples; all graph nodes/edges; source-specific primary passages and explicit inaccessible-body limits.

Selection: Target 5 in batch fifteen; first uncovered paths in the fresh expanded corpus, sorted by path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031514 | data/structures/appendage/motile_cilium.yaml | maintained | motile cilium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native verify | passed | True | GO:0031514 | Focused native command passed; identifier coverage is not independent membership evidence. |
| Native causal-graphs | passed | True | GO:0031514 | Focused native command passed; identifier coverage is not independent membership evidence. |
| Expression-module applicability | not_applicable | False | GO:0031514 | No transcriptomic or expression-module assertion under review. |
| Focused native schema | passed | True | GO:0031514 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031514 | Focused validator passed. |
| Claim-level scientific review | passed | True | GO:0031514 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Target resolver slice with native transport-failure cross-checks | passed | True | GO:0031514 | 21 of 26 exact target identifiers returned OK. Residuals: PMID:15955805 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-15955805-meta; PMID:17312020 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-17312020-meta; PMID:17326139 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-17326139-meta; PMID:18852297 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-18852297-meta; PMID:9585417 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-9585417-meta The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| Full corpus QC | passed | True | GO:0031514 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031514 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031514 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031514 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0031514 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Broad motile-cilium class

identity: supported. Targets: GO:0031514.

The exact native term, parent and synonym scopes are correct. Broad motile cilia include variable axonemal arrangements; Chlamydomonas9+2 observations are explicitly examples rather than a new universal nine-plus-two definition.

### Regions and associated IFT machinery

evidence: supported. Targets: GO:0031514.

Axoneme, membrane, basal-body/base and transition-zone identities are source supported. IFT is correctly marked associated machinery, with assembly/maintenance functions distinguished from a permanently incorporated structural constituent.

### Assembly necessity is separately unverified

scope: unknown. Targets: GO:0031514.

Native definitions and intact structural preparations establish anatomy. They do not independently establish every ESSENTIAL assembly-necessity annotation; no suitable regional depletion/reconstitution experiment was checked. Activity and organismal viability are not substituted.

### Five exact examples and experimental attribution

grounding: supported. Targets: GO:0031514.

All five accessions, gene tokens, status and taxon pairs match native records. The four reviewed examples are unique in the bounded query; IFT88 is honestly unreviewed. Localization-source notes accurately attribute database evidence; limited primary bodies are distinguished from full experimental audits.

### Canonical model and extracted preparations

scope: supported. Targets: GO:0031514.

Chlamydomonas species scope is supported. Pazour uses both WT and outer-arm mutant fractions; Nicastro examines demembranated axonemes. These preparations support the existing coarse structural claims without equating co-isolation or fraction abundance with universal membership.

### Optional algal part versus broad class

scope: concern. Targets: GO:0031514.

Native GO restricts mastigonemes to some algae. The unqualified target has_part and graph node/edge present this part without that restriction. The native part_of relation runs from mastigoneme to motile cilium and does not justify the inverse as an obligatory class-wide constituent.

### Anatomy and function summary versus mechanism

graph: concern. Targets: GO:0031514.

All nine nodes and eight edges were inspected. Parthood/association and generic motility summarize anatomy/function. The motile-cilium-to-cilium-assembly edge assigns assembly to the assembled product, while its evidence concerns IFT delivery and regional machinery. A MECHANISTIC label overstates the graph actually represented.

### Bounded optional additions

completeness: supported. Targets: GO:0031514.

No optional missing image/property or absent sixth IFT example is treated as a defect. Native graph audit counts zero GENE_OR_PROTEIN nodes because these nodes are STRUCTURE; that successful command is not evidence that every component gene has an example.

## Findings

### F1: Qualify mastigoneme parthood within the broad motile-cilium class

minor / open / confirmed; issue key: motile-cilium-mastigoneme-scope.

The unqualified has_part and corresponding graph element make mastigoneme appear as a constituent of the entire motile-cilium class, while the native term explicitly describes some algal flagella. Preserve the supported conditional algal relation and avoid treating an inverse GO part_of lookup as obligatory universal composition.

### F2: The graph labels anatomical summary and product-to-assembly edges as mechanism

minor / open / confirmed; issue key: motile-cilium-graph-self-assembly-and-scope.

Most edges are parthood/association or generic function. The motile_cilium mediates cilium_assembly edge uses a source about IFT delivering precursors and does not establish the assembled cilium as its own assembly driver. Narrow to a NONMECHANISTIC summary or represent source-backed machinery-to-assembly directions.

## Recommended Actions And Acceptance Checks

### A1

Represent mastigoneme as a taxon-qualified optional part, or retain the one-way parthood on its own record without an unqualified broad-class inverse.

- Preserve Chlamydomonas/algal support without generalizing to every motile cilium.
- Read exact source support and term direction; do not infer inverse class restrictions from a child listing.
- Apply only in separately authorized curation through the guarded writer and required history, rendering and validation gates.

### A2

Correct the assembly-edge direction/actor and graph scope to match the supported level of explanation.

- Distinguish assembled product, constituent regions, transport machinery and assembly process.
- Retain valid structural edges without claiming that parthood itself establishes causality.
- Apply only in separately authorized curation through the guarded writer and required history, rendering and validation gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/motile_cilium.yaml; Entire maintained YAML including all graph and evidence fields | context_only | Complete target read at inspected revision; scientific status/history remain unchanged. |
| policy | docs/CURATION.md; Evidence and component rules together with inspected schema/review profile | context_only | Read-only assessment preserves source scope, exact identity, assembly necessity and distinctions between spatial relations and mechanism. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph source and scope paragraphs | context_only | Mechanistic claims require appropriate source support; association and component coverage alone do not establish causality. |
| motile-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005929,GO:0005930,GO:0030990,GO:0031514,GO:0035869,GO:0036064,GO:0060170,GO:0060271,GO:0060285,GO:0097546,GO:0097741; All eleven terms: definitions, synonyms, child relations and source xrefs | supports | Native terms support the motile-cilium identity, cilium parent and named regional components. Mastigoneme is defined for some algae; its part_of relation alone does not establish a universal motile-cilium has_part assertion. |
| motile-prep-tax-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Identity, species rank and aliases | supports | NCBI/ENA taxon3055 matches Chlamydomonas reinhardtii. |
| motile-prep-pazour2005-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2171396.1/PMC2171396.1.xml; Introduction; Results identification/completeness/exclusiveness/distribution; Discussion opening, motors and membrane-axoneme subsection; all Methods and associated captions | supports | Proteomics distinguishes WT137c Tergitol samples from oda1-1 Nonidet/KCl fractions and high-confidence proteins from candidates/contaminants. It directly supports the purified-flagellum example and membrane/matrix/axoneme context without assigning every detected peptide to a structural constituent. |
| motile-prep-cole1998-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132775.1/PMC2132775.1.xml; Cultures, isolation and immunofluorescence Methods; Results immunolocalization; Discussion colocalization | supports | IFT172 and IFT complex polypeptides localize around basal bodies and within flagella. Exact Methods and mutant comparisons distinguish peribasal accumulation from intrinsic basal-body incorporation; p172 targeting can persist in bld2. |
| motile-prep-hou2007-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2064023.1/PMC2064023.1.xml; Results IFT46 necessity and A/B compartments; Figs3/4/6 captions; cells/culture Methods | supports | IFT46-null YH6 forms short nonmotile flagella; genomic rescue restores expression and swimming. IFT46 and IFT172 overlap in the peribasal region, while complex-A distribution differs. These findings distinguish assembly quality, activity and regional localization. |
| motile-prep-ahmed2008-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2568026.1/PMC2568026.1.xml; Results ODA16 localization and in-vivo interaction; strains Methods | supports | ODA16 and IFT components concentrate in peribasal and flagellar compartments; tagged ODA16 co-precipitates IFT46/81 and FLA10. This is not proof of stable incorporation into axonemal dynein. |
| motile-prep-rosenbaum2002-publisher | https://www.nature.com/articles/nrm952; Key Points and Abstract only; main-body access unavailable | supports | Publisher Key Points/Abstract describe IFT delivering precursors to distal assembly sites and maintaining cilia. The main review body is subscription-limited despite HTTP200. |
| nine-two-agent-nicastro-browser | https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography; Primary-text lines112–215, Fig1caption250–315 and preparation/reconstruction330–380 | supports | Primary cryo-ET resolves isolated Chlamydomonas axonemal architecture. Force generation and coordination are structural models, not a direct time-resolved beating sequence. |
| nine-two-agent-nicastro-methods-browser | https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography; Supporting Methods lines1562–1605, specimen preparation and microscopy | supports | WT137c and pf9-3 flagella were isolated by pH shock, demembranated with NP40 and rapidly frozen. Preparation must be distinguished from live, membrane-intact cilia. |
| motile-prep-Q5DM57 | https://rest.uniprot.org/uniprotkb/Q5DM57.json; Entry identity; genes; organism; SUBCELLULAR LOCATION evidence; exact cited references | supports | Native Q5DM57 verifies exact gene token, taxon3055, recommended/submitted protein name and reviewed status; the maintained localization-citation attribution was inspected where present. |
| motile-prep-Q68RJ5 | https://rest.uniprot.org/uniprotkb/Q68RJ5.json; Entry identity; genes; organism; SUBCELLULAR LOCATION evidence; exact cited references | supports | Native Q68RJ5 verifies exact gene token, taxon3055, recommended/submitted protein name and reviewed status; the maintained localization-citation attribution was inspected where present. |
| motile-prep-Q6RCE1 | https://rest.uniprot.org/uniprotkb/Q6RCE1.json; Entry identity; genes; organism; SUBCELLULAR LOCATION evidence; exact cited references | supports | Native Q6RCE1 verifies exact gene token, taxon3055, recommended/submitted protein name and reviewed status; the maintained localization-citation attribution was inspected where present. |
| motile-prep-A2T2X4 | https://rest.uniprot.org/uniprotkb/A2T2X4.json; Entry identity; genes; organism; SUBCELLULAR LOCATION evidence; exact cited references | supports | Native A2T2X4 verifies exact gene token, taxon3055, recommended/submitted protein name and reviewed status; the maintained localization-citation attribution was inspected where present. |
| motile-prep-Q9FPW0 | https://rest.uniprot.org/uniprotkb/Q9FPW0.json; Entry identity; genes; organism; SUBCELLULAR LOCATION evidence; exact cited references | supports | Native Q9FPW0 verifies exact gene token, taxon3055, recommended/submitted protein name and reviewed status; the maintained localization-citation attribution was inspected where present. |
| motile-prep-reviewed-uniqueness | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIFT172%20OR%20gene_exact%3AIFT81%20OR%20gene_exact%3AIFT74%20OR%20gene_exact%3AIFT46%29%20AND%20organism_id%3A3055%20AND%20reviewed%3Atrue&amp;format=json&amp;size=100; Complete result set of four entries | supports | The bounded reviewed exact-gene query returns one correct entry each for IFT172,IFT81,IFT74 andIFT46, with all four own-entry gene tokens checked. |
| motile-prep-silflow2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1104/pp.010807; Exact article title, authors, year, DOI/PMID only; no abstract | supports | Exact maintained citation identity and access tier verified; metadata is not represented as full-body access. No abstract was returned for Silflow2001. |
| motile-prep-rosenbaum2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nrm952; Exact article title, authors, year, DOI/PMID and abstract | supports | Exact maintained citation identity and access tier verified; metadata is not represented as full-body access. The returned abstract was inspected. |
| motile-prep-pazour2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.200504008; Exact article title, authors, year, DOI/PMID and abstract | supports | Exact maintained citation identity and access tier verified; metadata is not represented as full-body access. The returned abstract was inspected. |
| motile-prep-nicastro2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1126/science.1128618; Exact article title, authors, year, DOI/PMID and abstract | supports | Exact maintained citation identity and access tier verified; metadata is not represented as full-body access. The returned abstract was inspected. |
| motile-prep-pmid-17326139-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A17326139%20AND%20SRC%3AMED; Exact article title, authors, year, DOI/PMID and abstract | supports | Exact maintained citation identity and access tier verified; metadata is not represented as full-body access. The returned abstract was inspected. |
| motile-prep-pmid-9585417-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9585417%20AND%20SRC%3AMED; Exact article title, authors, year, DOI/PMID and abstract | supports | Exact maintained citation identity and access tier verified; metadata is not represented as full-body access. The returned abstract was inspected. |
| motile-prep-pmid-15955805-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15955805%20AND%20SRC%3AMED; Exact article title, authors, year, DOI/PMID and abstract | supports | Exact maintained citation identity and access tier verified; metadata is not represented as full-body access. The returned abstract was inspected. |
| motile-prep-pmid-17312020-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A17312020%20AND%20SRC%3AMED; Exact article title, authors, year, DOI/PMID and abstract | supports | Exact maintained citation identity and access tier verified; metadata is not represented as full-body access. The returned abstract was inspected. |
| motile-prep-pmid-18852297-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A18852297%20AND%20SRC%3AMED; Exact article title, authors, year, DOI/PMID and abstract | supports | Exact maintained citation identity and access tier verified; metadata is not represented as full-body access. The returned abstract was inspected. |
| neighbor | data/structures/appendage/mastigoneme.yaml; Entire neighboring maintained record; identity/context only | context_only | The separate mastigoneme record describes bounded Chlamydomonas evidence and unresolved broader taxon scope; it is not an additional reviewed target. |
| native-verify | /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml --verify; Exact focused native log and receipt | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml --causal-graphs; Exact focused native log and receipt | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/appendage/motile_cilium.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/appendage/motile_cilium.yaml |
| strict-result | just validate-strict data/structures/appendage/motile_cilium.yaml --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/motile_cilium-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/appendage/motile_cilium.yaml --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/motile_cilium-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch15-20261021-ohdkgt21/motile_cilium-strict.tsv |
| target-curies-result | just check-curies-strict; data/structures/appendage/motile_cilium.yaml; exact native collect() target slice of original fresh-base TSV | supports | 21 of 26 exact target identifiers returned OK. Residuals: PMID:15955805 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-15955805-meta; PMID:17312020 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-17312020-meta; PMID:17326139 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-17326139-meta; PMID:18852297 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-18852297-meta; PMID:9585417 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-9585417-meta The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Rosenbaum2002 was read at publisher Key Points/Abstract level, not full body. Silflow2001 has bibliographic metadata only, with no returned abstract. Sloboda2007/Lucker2005 have metadata/abstract and native attribution support; inaccessible body routes are retained.
- Nicastro evidence is a preserved primary-text browser capture with original access times and null HTTP status. Listed main/SOM passages were read, not the complete paper, raw cryo-ET data or image pixels.
- Pazour, Cole, Hou and Ahmed were read at the recorded claim-bearing Methods/Results/Discussion passages. No complete supplementary table, figure-pixel or raw-data audit is asserted.
- Assembly-necessity annotations remain unverified; membership and catalytic importance alone do not establish that the structure cannot form without a component.
- The mastigoneme neighbor was read for exact identity and current modeling context, not counted as another completed scientific review.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The exact target resolver slice is derived from the completed fresh-base run. Any PMID transport failures were checked against the separately cited native literature metadata; these identity checks do not establish full-body scientific support.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094737Z-motile-cilium-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Motile cilium scope, IFT examples and graph evidence review
started_at: '2026-10-21T09:07:31Z'
finished_at: '2026-10-21T09:47:37Z'
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
summary: Motile-cilium identity, coarse composition and exact IFT examples are supported.
  Two minor issues concern unqualified mastigoneme scope and the mechanism label/product-to-assembly
  edge.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/structures/appendage/mastigoneme.yaml
    sha256: d494a06dcfd0686ab910c8ae88a4899c1f5dd58634339194d24c4dac64d3fbd1
    role: context
  - path: data/structures/appendage/motile_cilium.yaml
    sha256: 4c6689b83a38d84b34e3775c18d0b7e6706e6c069e37790c8549db6f14729e1e
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
- target_id: GO:0031514
  path: data/structures/appendage/motile_cilium.yaml
  label: motile cilium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/motile_cilium.yaml
    role: maintained scientific record
scope:
  description: Whole single target and identity-only neighboring context; all native
    terms and five protein examples; all graph nodes/edges; source-specific primary
    passages and explicit inaccessible-body limits.
  selection: Target 5 in batch fifteen; first uncovered paths in the fresh expanded
    corpus, sorted by path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031514
checks:
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0031514
  command: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml
    --verify
  exit_code: 0
  summary: Focused native command passed; identifier coverage is not independent membership
    evidence.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0031514
  command: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native command passed; identifier coverage is not independent membership
    evidence.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0031514
  summary: No transcriptomic or expression-module assertion under review.
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031514
  command: just validate data/structures/appendage/motile_cilium.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031514
  command: just validate-strict data/structures/appendage/motile_cilium.yaml --out
    /private/tmp/cellstructure-batch15-20261021-ohdkgt21/motile_cilium-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0031514
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - motile-prep-go
  - motile-prep-tax-3055
  - motile-prep-pazour2005-jats
  - motile-prep-cole1998-jats
  - motile-prep-hou2007-jats
  - motile-prep-ahmed2008-jats
  - motile-prep-rosenbaum2002-publisher
  - nine-two-agent-nicastro-browser
  - nine-two-agent-nicastro-methods-browser
  - motile-prep-Q5DM57
  - motile-prep-Q68RJ5
  - motile-prep-Q6RCE1
  - motile-prep-A2T2X4
  - motile-prep-Q9FPW0
  - motile-prep-reviewed-uniqueness
  - motile-prep-silflow2001-meta
  - motile-prep-rosenbaum2002-meta
  - motile-prep-pazour2005-meta
  - motile-prep-nicastro2006-meta
  - motile-prep-pmid-17326139-meta
  - motile-prep-pmid-9585417-meta
  - motile-prep-pmid-15955805-meta
  - motile-prep-pmid-17312020-meta
  - motile-prep-pmid-18852297-meta
  - neighbor
- check_id: target-curies
  name: Target resolver slice with native transport-failure cross-checks
  status: passed
  required: true
  target_ids:
  - GO:0031514
  summary: '21 of 26 exact target identifiers returned OK. Residuals: PMID:15955805
    returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently
    verified by motile-prep-pmid-15955805-meta; PMID:17312020 returned UNREACHABLE
    (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-17312020-meta;
    PMID:17326139 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata
    independently verified by motile-prep-pmid-17326139-meta; PMID:18852297 returned
    UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified
    by motile-prep-pmid-18852297-meta; PMID:9585417 returned UNREACHABLE (eutils HTTP414);
    exact native PMID metadata independently verified by motile-prep-pmid-9585417-meta
    The shared command exit zero is not interpreted as successful network resolution
    for transport failures.'
  evidence_ids:
  - target-curies-result
  - motile-prep-pmid-15955805-meta
  - motile-prep-pmid-17312020-meta
  - motile-prep-pmid-17326139-meta
  - motile-prep-pmid-18852297-meta
  - motile-prep-pmid-9585417-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031514
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
  - GO:0031514
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
  - GO:0031514
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
  - GO:0031514
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
  - GO:0031514
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
  reference: data/structures/appendage/motile_cilium.yaml
  locator: Entire maintained YAML including all graph and evidence fields
  accessed_at: '2026-10-21T09:21:19Z'
  support: context_only
  summary: Complete target read at inspected revision; scientific status/history remain
    unchanged.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Evidence and component rules together with inspected schema/review profile
  accessed_at: '2026-10-21T09:21:19Z'
  support: context_only
  summary: Read-only assessment preserves source scope, exact identity, assembly necessity
    and distinctions between spatial relations and mechanism.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph source and scope paragraphs
  accessed_at: '2026-10-21T09:21:19Z'
  support: context_only
  summary: Mechanistic claims require appropriate source support; association and
    component coverage alone do not establish causality.
- evidence_id: motile-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005929,GO:0005930,GO:0030990,GO:0031514,GO:0035869,GO:0036064,GO:0060170,GO:0060271,GO:0060285,GO:0097546,GO:0097741
  locator: 'All eleven terms: definitions, synonyms, child relations and source xrefs'
  accessed_at: '2026-10-21T09:07:57.362672Z'
  support: supports
  summary: Native terms support the motile-cilium identity, cilium parent and named
    regional components. Mastigoneme is defined for some algae; its part_of relation
    alone does not establish a universal motile-cilium has_part assertion.
  snapshot_sha256: cb34e0b8daab61dbc7951187fdf61a225ac63da8793dff22984cfb7072a4d33b
- evidence_id: motile-prep-tax-3055
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Identity, species rank and aliases
  accessed_at: '2026-10-21T09:07:57.313814Z'
  support: supports
  summary: NCBI/ENA taxon3055 matches Chlamydomonas reinhardtii.
  snapshot_sha256: a24c8f85014097148d9e865ea324b01b8d04f6bae27e893834f8abb5bd8b6a1f
- evidence_id: motile-prep-pazour2005-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2171396.1/PMC2171396.1.xml
  locator: Introduction; Results identification/completeness/exclusiveness/distribution;
    Discussion opening, motors and membrane-axoneme subsection; all Methods and associated
    captions
  accessed_at: '2026-10-21T09:08:55.907700Z'
  support: supports
  summary: Proteomics distinguishes WT137c Tergitol samples from oda1-1 Nonidet/KCl
    fractions and high-confidence proteins from candidates/contaminants. It directly
    supports the purified-flagellum example and membrane/matrix/axoneme context without
    assigning every detected peptide to a structural constituent.
  snapshot_sha256: 07d7ef18479239d9cb12f3064152e086c0abc0f1a9657ac65b3e0cecb43701fa
- evidence_id: motile-prep-cole1998-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132775.1/PMC2132775.1.xml
  locator: Cultures, isolation and immunofluorescence Methods; Results immunolocalization;
    Discussion colocalization
  accessed_at: '2026-10-21T09:08:55.880926Z'
  support: supports
  summary: IFT172 and IFT complex polypeptides localize around basal bodies and within
    flagella. Exact Methods and mutant comparisons distinguish peribasal accumulation
    from intrinsic basal-body incorporation; p172 targeting can persist in bld2.
  snapshot_sha256: 7a1055581fe4adc86ed8142286edcde67e4059b3c02d89f317f5019b0f1e55ca
- evidence_id: motile-prep-hou2007-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2064023.1/PMC2064023.1.xml
  locator: Results IFT46 necessity and A/B compartments; Figs3/4/6 captions; cells/culture
    Methods
  accessed_at: '2026-10-21T09:08:55.893269Z'
  support: supports
  summary: IFT46-null YH6 forms short nonmotile flagella; genomic rescue restores
    expression and swimming. IFT46 and IFT172 overlap in the peribasal region, while
    complex-A distribution differs. These findings distinguish assembly quality, activity
    and regional localization.
  snapshot_sha256: d855eecdba394dedd578180b69d1ef7b24d4d5337688f8fd28fb3b1b93d64908
- evidence_id: motile-prep-ahmed2008-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2568026.1/PMC2568026.1.xml
  locator: Results ODA16 localization and in-vivo interaction; strains Methods
  accessed_at: '2026-10-21T09:08:55.944134Z'
  support: supports
  summary: ODA16 and IFT components concentrate in peribasal and flagellar compartments;
    tagged ODA16 co-precipitates IFT46/81 and FLA10. This is not proof of stable incorporation
    into axonemal dynein.
  snapshot_sha256: 2fde994c6f14e35e2cc5678fc946909c4f3fdc14951956c357be01cfcb1359d2
- evidence_id: motile-prep-rosenbaum2002-publisher
  kind: authority
  reference: https://www.nature.com/articles/nrm952
  locator: Key Points and Abstract only; main-body access unavailable
  accessed_at: '2026-10-21T09:08:57.195239Z'
  support: supports
  summary: Publisher Key Points/Abstract describe IFT delivering precursors to distal
    assembly sites and maintaining cilia. The main review body is subscription-limited
    despite HTTP200.
  snapshot_sha256: e7b15f14479ca2686ee8f849cc26206dfcdac20dba06ec7eb1efd2594483a0fa
- evidence_id: nine-two-agent-nicastro-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography
  locator: Primary-text lines112–215, Fig1caption250–315 and preparation/reconstruction330–380
  accessed_at: '2026-10-21T07:38:16.675911Z'
  support: supports
  summary: Primary cryo-ET resolves isolated Chlamydomonas axonemal architecture.
    Force generation and coordination are structural models, not a direct time-resolved
    beating sequence.
  snapshot_sha256: 0d28f5c7269d892d9ff78d7f8699840cf5ca9887d0b8967c9a2f8afbf12d8d11
- evidence_id: nine-two-agent-nicastro-methods-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography
  locator: Supporting Methods lines1562–1605, specimen preparation and microscopy
  accessed_at: '2026-10-21T07:38:38.502409Z'
  support: supports
  summary: WT137c and pf9-3 flagella were isolated by pH shock, demembranated with
    NP40 and rapidly frozen. Preparation must be distinguished from live, membrane-intact
    cilia.
  snapshot_sha256: 6a9ed325f07a171d0f956a008bddea206631151f957a0463f11d687f68dda60e
- evidence_id: motile-prep-Q5DM57
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q5DM57.json
  locator: Entry identity; genes; organism; SUBCELLULAR LOCATION evidence; exact cited
    references
  accessed_at: '2026-10-21T09:07:58.418366Z'
  support: supports
  summary: Native Q5DM57 verifies exact gene token, taxon3055, recommended/submitted
    protein name and reviewed status; the maintained localization-citation attribution
    was inspected where present.
  snapshot_sha256: 81d0a74e5bda18c90d8bc7a12d6abdcfbb0219f5829ae8bdf58bd9eb6d125b1c
- evidence_id: motile-prep-Q68RJ5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q68RJ5.json
  locator: Entry identity; genes; organism; SUBCELLULAR LOCATION evidence; exact cited
    references
  accessed_at: '2026-10-21T09:07:58.416899Z'
  support: supports
  summary: Native Q68RJ5 verifies exact gene token, taxon3055, recommended/submitted
    protein name and reviewed status; the maintained localization-citation attribution
    was inspected where present.
  snapshot_sha256: d200c715553d94a8e16d56f2aab24412a810c125e11f1153c68095486cd9153c
- evidence_id: motile-prep-Q6RCE1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q6RCE1.json
  locator: Entry identity; genes; organism; SUBCELLULAR LOCATION evidence; exact cited
    references
  accessed_at: '2026-10-21T09:07:58.418203Z'
  support: supports
  summary: Native Q6RCE1 verifies exact gene token, taxon3055, recommended/submitted
    protein name and reviewed status; the maintained localization-citation attribution
    was inspected where present.
  snapshot_sha256: d392121fd9271634adef9cc3a4b4309205c022bef3ae3efe733ac90b5cf64bf9
- evidence_id: motile-prep-A2T2X4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A2T2X4.json
  locator: Entry identity; genes; organism; SUBCELLULAR LOCATION evidence; exact cited
    references
  accessed_at: '2026-10-21T09:07:57.316303Z'
  support: supports
  summary: Native A2T2X4 verifies exact gene token, taxon3055, recommended/submitted
    protein name and reviewed status; the maintained localization-citation attribution
    was inspected where present.
  snapshot_sha256: 9da98899eae02d8a3c974a888104e0e89a3f1b7f6468b130c60fd6e59a9db19e
- evidence_id: motile-prep-Q9FPW0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9FPW0.json
  locator: Entry identity; genes; organism; SUBCELLULAR LOCATION evidence; exact cited
    references
  accessed_at: '2026-10-21T09:07:58.340298Z'
  support: supports
  summary: Native Q9FPW0 verifies exact gene token, taxon3055, recommended/submitted
    protein name and reviewed status; the maintained localization-citation attribution
    was inspected where present.
  snapshot_sha256: 2317af7a1a68536f1c6ca22036f78420bb40ae73394e48d681b1edc7ee1a6f82
- evidence_id: motile-prep-reviewed-uniqueness
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIFT172%20OR%20gene_exact%3AIFT81%20OR%20gene_exact%3AIFT74%20OR%20gene_exact%3AIFT46%29%20AND%20organism_id%3A3055%20AND%20reviewed%3Atrue&format=json&size=100
  locator: Complete result set of four entries
  accessed_at: '2026-10-21T09:12:34.687595Z'
  support: supports
  summary: The bounded reviewed exact-gene query returns one correct entry each for
    IFT172,IFT81,IFT74 andIFT46, with all four own-entry gene tokens checked.
  snapshot_sha256: 240c126103910e1e296caa2b223dca221e81b893bc4d435ea5ae0f6ebd0b60fa
- evidence_id: motile-prep-silflow2001-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1104/pp.010807
  locator: Exact article title, authors, year, DOI/PMID only; no abstract
  accessed_at: '2026-10-21T09:07:59.415819Z'
  support: supports
  summary: Exact maintained citation identity and access tier verified; metadata is
    not represented as full-body access. No abstract was returned for Silflow2001.
  snapshot_sha256: e8551b55d1a2d4377bc57c543f1fd8ea8019869b0933dabb0be6c453c436249c
- evidence_id: motile-prep-rosenbaum2002-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrm952
  locator: Exact article title, authors, year, DOI/PMID and abstract
  accessed_at: '2026-10-21T09:07:59.542553Z'
  support: supports
  summary: Exact maintained citation identity and access tier verified; metadata is
    not represented as full-body access. The returned abstract was inspected.
  snapshot_sha256: 79536f000e09b8357f2caff66d00292b68e5c96350780aed7ce5458e89400154
- evidence_id: motile-prep-pazour2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.200504008
  locator: Exact article title, authors, year, DOI/PMID and abstract
  accessed_at: '2026-10-21T09:07:59.772309Z'
  support: supports
  summary: Exact maintained citation identity and access tier verified; metadata is
    not represented as full-body access. The returned abstract was inspected.
  snapshot_sha256: 747fb5b21678ae5300f8f74994922a31f0dc55f92b12958be4ffa17f23e61be6
- evidence_id: motile-prep-nicastro2006-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1126/science.1128618
  locator: Exact article title, authors, year, DOI/PMID and abstract
  accessed_at: '2026-10-21T09:07:59.543005Z'
  support: supports
  summary: Exact maintained citation identity and access tier verified; metadata is
    not represented as full-body access. The returned abstract was inspected.
  snapshot_sha256: 4c756c1a4b0b72ca268113b4f63df7d6cf29255043e4d9a78ae29ee6c914ff43
- evidence_id: motile-prep-pmid-17326139-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A17326139%20AND%20SRC%3AMED
  locator: Exact article title, authors, year, DOI/PMID and abstract
  accessed_at: '2026-10-21T09:08:02.145375Z'
  support: supports
  summary: Exact maintained citation identity and access tier verified; metadata is
    not represented as full-body access. The returned abstract was inspected.
  snapshot_sha256: 924cdde0c0db6c5a1c6783b78ea11abbde3dc8af0d3806b441691ef08dbcf946
- evidence_id: motile-prep-pmid-9585417-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9585417%20AND%20SRC%3AMED
  locator: Exact article title, authors, year, DOI/PMID and abstract
  accessed_at: '2026-10-21T09:08:00.569048Z'
  support: supports
  summary: Exact maintained citation identity and access tier verified; metadata is
    not represented as full-body access. The returned abstract was inspected.
  snapshot_sha256: 00baf9756e0029ef28d1b519b1c16c32ae879f12821f5e00d6326269112e8741
- evidence_id: motile-prep-pmid-15955805-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15955805%20AND%20SRC%3AMED
  locator: Exact article title, authors, year, DOI/PMID and abstract
  accessed_at: '2026-10-21T09:08:00.695642Z'
  support: supports
  summary: Exact maintained citation identity and access tier verified; metadata is
    not represented as full-body access. The returned abstract was inspected.
  snapshot_sha256: 1edc2c35fd96ea7e3950e01a73e3bfa8a04007012c9dff73f0b8275c04d2715d
- evidence_id: motile-prep-pmid-17312020-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A17312020%20AND%20SRC%3AMED
  locator: Exact article title, authors, year, DOI/PMID and abstract
  accessed_at: '2026-10-21T09:08:00.643800Z'
  support: supports
  summary: Exact maintained citation identity and access tier verified; metadata is
    not represented as full-body access. The returned abstract was inspected.
  snapshot_sha256: 406ed5b037626e74878e8a1ec5d19663941c08ac3b7448d6c1b2fd9d211f9187
- evidence_id: motile-prep-pmid-18852297-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A18852297%20AND%20SRC%3AMED
  locator: Exact article title, authors, year, DOI/PMID and abstract
  accessed_at: '2026-10-21T09:08:01.055578Z'
  support: supports
  summary: Exact maintained citation identity and access tier verified; metadata is
    not represented as full-body access. The returned abstract was inspected.
  snapshot_sha256: cea6b5c8724ffd7c58d7eaf7e0d3a69a27539e05b3705baac34290d10de0be4b
- evidence_id: neighbor
  kind: record_content
  reference: data/structures/appendage/mastigoneme.yaml
  locator: Entire neighboring maintained record; identity/context only
  accessed_at: '2026-10-21T09:21:19Z'
  support: context_only
  summary: The separate mastigoneme record describes bounded Chlamydomonas evidence
    and unresolved broader taxon scope; it is not an additional reviewed target.
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml
    --verify
  locator: Exact focused native log and receipt
  accessed_at: '2026-10-21T09:09:58.747815Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml
    --causal-graphs
  locator: Exact focused native log and receipt
  accessed_at: '2026-10-21T09:09:59.712307Z'
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
  reference: just validate data/structures/appendage/motile_cilium.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:07:36Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/motile_cilium.yaml'
  snapshot_sha256: c6314fea58c2472987a86d1ad65505f4e51d7a93f021cf48353ec8095164e292
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/appendage/motile_cilium.yaml --out
    /private/tmp/cellstructure-batch15-20261021-ohdkgt21/motile_cilium-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:07:44Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/appendage/motile_cilium.yaml\
    \ --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/motile_cilium-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch15-20261021-ohdkgt21/motile_cilium-strict.tsv"
  snapshot_sha256: c25b77a67520cfd7072d43b00df60c1294f152489b9de5bdebd15bfed1c30a97
- evidence_id: target-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/motile_cilium.yaml; exact native collect() target
    slice of original fresh-base TSV
  accessed_at: '2026-10-21T09:47:06.373657Z'
  support: supports
  summary: '21 of 26 exact target identifiers returned OK. Residuals: PMID:15955805
    returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently
    verified by motile-prep-pmid-15955805-meta; PMID:17312020 returned UNREACHABLE
    (eutils HTTP414); exact native PMID metadata independently verified by motile-prep-pmid-17312020-meta;
    PMID:17326139 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata
    independently verified by motile-prep-pmid-17326139-meta; PMID:18852297 returned
    UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified
    by motile-prep-pmid-18852297-meta; PMID:9585417 returned UNREACHABLE (eutils HTTP414);
    exact native PMID metadata independently verified by motile-prep-pmid-9585417-meta
    The shared command exit zero is not interpreted as successful network resolution
    for transport failures.'
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
  topic: Broad motile-cilium class
  outcome: supported
  target_ids:
  - GO:0031514
  summary: The exact native term, parent and synonym scopes are correct. Broad motile
    cilia include variable axonemal arrangements; Chlamydomonas9+2 observations are
    explicitly examples rather than a new universal nine-plus-two definition.
  evidence_ids:
  - motile-prep-go
  - motile-prep-tax-3055
  - nine-two-agent-nicastro-browser
  - record
- assessment_id: components
  area: evidence
  topic: Regions and associated IFT machinery
  outcome: supported
  target_ids:
  - GO:0031514
  summary: Axoneme, membrane, basal-body/base and transition-zone identities are source
    supported. IFT is correctly marked associated machinery, with assembly/maintenance
    functions distinguished from a permanently incorporated structural constituent.
  evidence_ids:
  - motile-prep-go
  - motile-prep-pazour2005-jats
  - motile-prep-cole1998-jats
  - motile-prep-hou2007-jats
  - motile-prep-rosenbaum2002-publisher
  - record
- assessment_id: essentiality
  area: scope
  topic: Assembly necessity is separately unverified
  outcome: unknown
  target_ids:
  - GO:0031514
  summary: Native definitions and intact structural preparations establish anatomy.
    They do not independently establish every ESSENTIAL assembly-necessity annotation;
    no suitable regional depletion/reconstitution experiment was checked. Activity
    and organismal viability are not substituted.
  evidence_ids:
  - motile-prep-go
  - motile-prep-pazour2005-jats
  - nine-two-agent-nicastro-browser
  - nine-two-agent-nicastro-methods-browser
  - record
  - policy
- assessment_id: proteins
  area: grounding
  topic: Five exact examples and experimental attribution
  outcome: supported
  target_ids:
  - GO:0031514
  summary: All five accessions, gene tokens, status and taxon pairs match native records.
    The four reviewed examples are unique in the bounded query; IFT88 is honestly
    unreviewed. Localization-source notes accurately attribute database evidence;
    limited primary bodies are distinguished from full experimental audits.
  evidence_ids:
  - motile-prep-Q5DM57
  - motile-prep-Q68RJ5
  - motile-prep-Q6RCE1
  - motile-prep-A2T2X4
  - motile-prep-Q9FPW0
  - motile-prep-reviewed-uniqueness
  - motile-prep-tax-3055
  - motile-prep-cole1998-jats
  - motile-prep-hou2007-jats
  - motile-prep-ahmed2008-jats
  - motile-prep-silflow2001-meta
  - motile-prep-rosenbaum2002-meta
  - motile-prep-pazour2005-meta
  - motile-prep-nicastro2006-meta
  - motile-prep-pmid-17326139-meta
  - motile-prep-pmid-9585417-meta
  - motile-prep-pmid-15955805-meta
  - motile-prep-pmid-17312020-meta
  - motile-prep-pmid-18852297-meta
  - record
- assessment_id: taxon-preparation
  area: scope
  topic: Canonical model and extracted preparations
  outcome: supported
  target_ids:
  - GO:0031514
  summary: Chlamydomonas species scope is supported. Pazour uses both WT and outer-arm
    mutant fractions; Nicastro examines demembranated axonemes. These preparations
    support the existing coarse structural claims without equating co-isolation or
    fraction abundance with universal membership.
  evidence_ids:
  - motile-prep-pazour2005-jats
  - nine-two-agent-nicastro-browser
  - nine-two-agent-nicastro-methods-browser
  - motile-prep-tax-3055
  - record
- assessment_id: mastigoneme-scope
  area: scope
  topic: Optional algal part versus broad class
  outcome: concern
  target_ids:
  - GO:0031514
  summary: Native GO restricts mastigonemes to some algae. The unqualified target
    has_part and graph node/edge present this part without that restriction. The native
    part_of relation runs from mastigoneme to motile cilium and does not justify the
    inverse as an obligatory class-wide constituent.
  evidence_ids:
  - motile-prep-go
  - neighbor
  - record
- assessment_id: graph
  area: graph
  topic: Anatomy and function summary versus mechanism
  outcome: concern
  target_ids:
  - GO:0031514
  summary: All nine nodes and eight edges were inspected. Parthood/association and
    generic motility summarize anatomy/function. The motile-cilium-to-cilium-assembly
    edge assigns assembly to the assembled product, while its evidence concerns IFT
    delivery and regional machinery. A MECHANISTIC label overstates the graph actually
    represented.
  evidence_ids:
  - motile-prep-go
  - motile-prep-rosenbaum2002-publisher
  - motile-prep-cole1998-jats
  - nine-two-agent-nicastro-browser
  - record
  - graph-policy
- assessment_id: completeness
  area: completeness
  topic: Bounded optional additions
  outcome: supported
  target_ids:
  - GO:0031514
  summary: No optional missing image/property or absent sixth IFT example is treated
    as a defect. Native graph audit counts zero GENE_OR_PROTEIN nodes because these
    nodes are STRUCTURE; that successful command is not evidence that every component
    gene has an example.
  evidence_ids:
  - native-causal-graphs
  - native-verify
  - record
  - policy
findings:
- finding_id: F1
  issue_key: motile-cilium-mastigoneme-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify mastigoneme parthood within the broad motile-cilium class
  description: The unqualified has_part and corresponding graph element make mastigoneme
    appear as a constituent of the entire motile-cilium class, while the native term
    explicitly describes some algal flagella. Preserve the supported conditional algal
    relation and avoid treating an inverse GO part_of lookup as obligatory universal
    composition.
  target_ids:
  - GO:0031514
  field_paths:
  - has_part
  - causal_graphs[graph_id=motile_cilium_mechanism].nodes[node_id=mastigoneme]
  - causal_graphs[graph_id=motile_cilium_mechanism].edges[subject=mastigoneme]
  evidence_ids:
  - motile-prep-go
  - neighbor
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/motile_cilium.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and scope
  native_severity: minor
  normalization_reason: Bounded representation or attribution defect; exact structure
    identity remains supported.
- finding_id: F2
  issue_key: motile-cilium-graph-self-assembly-and-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: The graph labels anatomical summary and product-to-assembly edges as mechanism
  description: Most edges are parthood/association or generic function. The motile_cilium
    mediates cilium_assembly edge uses a source about IFT delivering precursors and
    does not establish the assembled cilium as its own assembly driver. Narrow to
    a NONMECHANISTIC summary or represent source-backed machinery-to-assembly directions.
  target_ids:
  - GO:0031514
  field_paths:
  - causal_graphs[graph_id=motile_cilium_mechanism].scope_status
  - causal_graphs[graph_id=motile_cilium_mechanism].edges[subject=motile_cilium,object=cilium_assembly]
  evidence_ids:
  - motile-prep-rosenbaum2002-publisher
  - motile-prep-cole1998-jats
  - nine-two-agent-nicastro-browser
  - motile-prep-go
  - record
  - graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/motile_cilium.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and scope
  native_severity: minor
  normalization_reason: Bounded representation or attribution defect; exact structure
    identity remains supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0031514
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/motile_cilium.yaml
    role: maintained scientific record
  description: Represent mastigoneme as a taxon-qualified optional part, or retain
    the one-way parthood on its own record without an unqualified broad-class inverse.
  acceptance_checks:
  - Preserve Chlamydomonas/algal support without generalizing to every motile cilium.
  - Read exact source support and term direction; do not infer inverse class restrictions
    from a child listing.
  - Apply only in separately authorized curation through the guarded writer and required
    history, rendering and validation gates.
  generator: Maintained scientific YAML; generated pages are derived.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0031514
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/motile_cilium.yaml
    role: maintained scientific record
  description: Correct the assembly-edge direction/actor and graph scope to match
    the supported level of explanation.
  acceptance_checks:
  - Distinguish assembled product, constituent regions, transport machinery and assembly
    process.
  - Retain valid structural edges without claiming that parthood itself establishes
    causality.
  - Apply only in separately authorized curation through the guarded writer and required
    history, rendering and validation gates.
  generator: Maintained scientific YAML; generated pages are derived.
limitations:
- Rosenbaum2002 was read at publisher Key Points/Abstract level, not full body. Silflow2001
  has bibliographic metadata only, with no returned abstract. Sloboda2007/Lucker2005
  have metadata/abstract and native attribution support; inaccessible body routes
  are retained.
- Nicastro evidence is a preserved primary-text browser capture with original access
  times and null HTTP status. Listed main/SOM passages were read, not the complete
  paper, raw cryo-ET data or image pixels.
- Pazour, Cole, Hou and Ahmed were read at the recorded claim-bearing Methods/Results/Discussion
  passages. No complete supplementary table, figure-pixel or raw-data audit is asserted.
- Assembly-necessity annotations remain unverified; membership and catalytic importance
  alone do not establish that the structure cannot form without a component.
- The mastigoneme neighbor was read for exact identity and current modeling context,
  not counted as another completed scientific review.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The exact target resolver slice is derived from the completed fresh-base run. Any
  PMID transport failures were checked against the separately cited native literature
  metadata; these identity checks do not establish full-body scientific support.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
