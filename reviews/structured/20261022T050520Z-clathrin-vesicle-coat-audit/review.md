# Source-backed review of clathrin vesicle coat

- Review: 20261022T050520Z-clathrin-vesicle-coat-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:47:24Z
- Finished UTC: 2026-10-22T05:05:20Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The coat identity, yeast examples and descriptive graph are supported at the declared source tiers. One bounded minor resolves the two exact chain-family groundings.

## Scope And Provenance

Exactly one complete target; no neighboring scientific-record verdict is imported. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch47 fixed strict path order, index 8; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030125 | data/structures/other/clathrin_vesicle_coat.yaml | maintained | clathrin vesicle coat |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030125 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030125 | Focused validator passed. |
| Focused native proteins | passed | True | GO:0030125 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | GO:0030125 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:0030125 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030125 | 12 of 12 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030125 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030125 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030125 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030125 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030125 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact coat identity and topology

identity: supported. Targets: GO:0030125.

The exact active GO identity, definition and declared topology are supported. Specific coat-to-membrane part_of and is_a links are native typed relations; broad coat-to-whole-vesicle parthood is definition-supported rather than an exposed direct edge in this response. The proteinaceous coat remains distinct from a lipid membrane and from the whole vesicle. The endocytic and TGN terms are specific children of the broad vesicle-coat class.

### Species, strain and prevalence meaning

scope: supported. Targets: GO:0030125.

Species4932 and strain559292 identities are correct. COMMON means present in most species members with exceptional losses; ordinary yeast experiments provide qualitative support, not a measured prevalence denominator. Experimental strain/condition details are not silently replaced by the reference accession taxon.

### Native examples and query claims

grounding: supported. Targets: GO:0030125.

All retained accession/gene/status/taxon pairs are correct. Exact reviewed S288C queries support the current single-hit claims. Identity-only examples remain identity evidence; primary membership and localization are assessed separately. 

### Formation necessity

grounding: unknown. Targets: GO:0030125.

The component essentiality values are already UNKNOWN. The inspected localization, association and trafficking data do not establish a single universal requirement for formation of every coat represented by this class. No unsupported ESSENTIAL claim is introduced.

### Exact heavy/light-chain family identities

grounding: concern. Targets: GO:0030125.

The two constituent chain identities and roles are supported. Exact IPR016341 heavy-chain and IPR000996 light-chain families resolve their explicit reviewed-label-only statuses. The two-chain inventory is declared coarse; absence of every optional adaptor or triskelion stoichiometric row does not independently create a finding.

### Primary scope and component function

evidence: supported. Targets: GO:0030125.

Payne and Chu abstracts support their stated heavy/light-chain experimental context; Chu distinguishes efficient trimerization/proper coat formation and partial rescue. Newpher directly supports cortical recruitment and relative timing. The record does not turn these studies into proof that every endocytic vesicle absolutely requires clathrin or that a TIRF departure is directly observed scission.

### Descriptive assembly-timing graph

graph: supported. Targets: GO:0030125.

The six-node/five-edge NONMECHANISTIC ASSEMBLY graph uses heavy/light chain part-of, coat/vesicle topology and cortical recruitment preceding later actin. Its explicit coarse scope does not claim complete triskelion stoichiometry, all adaptors, or a resolved budding/scission sequence.

### Whole-target coverage and bounded enrichment

completeness: supported. Targets: GO:0030125.

The entire target, all current components/examples, source placements, graph, discussions and history were reviewed. The supported exact mapping issue is distinct from optional inventory expansion. No exhaustive absence claim is made for future broader-adaptor families; no local-neighbor scientific verdict is imported.

## Findings

### F1: Resolve the two exact clathrin-chain family groundings

minor / open / confirmed; issue key: clathrin.clathrin_vesicle_coat.exact_chain_families.

Both source-neutral chain rows remain REVIEWED_LABEL_ONLY despite exact active InterPro families: IPR016341 for the heavy chain and IPR000996 for the light chain. Native reviewed CHC1/P22137 and CLC1/P17891 carry the respective family cross-references. This is a current actionable mapping gap, not a claim that the historical pass falsely reported its own work.

## Recommended Actions And Acceptance Checks

### A1

Ground heavy chain to InterPro:IPR016341 and light chain to InterPro:IPR000996, synchronize current grounding statuses/notes and linked graph nodes while preserving the coarse inventory and UNKNOWN formation necessity.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/clathrin_vesicle_coat.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic or transport function. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| micro47-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005768,GO:0005802,GO:0005905,GO:0012510,GO:0016020,GO:0030117,GO:0030118,GO:0030119,GO:0030120,GO:0030121,GO:0030122,GO:0030125,GO:0030128,GO:0030130,GO:0030132,GO:0030136,GO:0030140,GO:0030669,GO:0045334,GO:0072583; Complete exact entries GO0030128/0030130/0030125/0030120/0030118/0030117/0030119/0030121/0030122/0030669/0012510/0030140/0045334/0030136/0005768/0005802/0072583: id,name,definition,isObsolete,typed children and synonyms; shared response also includes pit/membrane entries. | supports | GO0030125 is an active exact clathrin-coat identity, distinct from the membrane and whole vesicle it coats. The combined native response verifies the maintained is_a relations, the two specific coat-to-membrane part_of links, AP1/AP2 boundaries and GO0072583 endocytosis. The broad coat-to-vesicle parthood is definition-supported; a direct GO0030125 part_of GO0030136 edge is not exposed in this response. GO0030118 describes polymerized heavy/light-chain triskelions linked to membranes by adaptors. No exhaustive future inventory is inferred. |
| micro47-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 4932 identifies Saccharomyces cerevisiae at rank species; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro47-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 559292 identifies Saccharomyces cerevisiae S288C at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro47-protein-P22137 | https://rest.uniprot.org/uniprotkb/P22137.json; primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P22137 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['CHC1']. Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro47-protein-P17891 | https://rest.uniprot.org/uniprotkb/P17891.json; primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P17891 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['CLC1']. Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro47-gene-CHC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACHC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results of the retained exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query for CHC1 returned 1 entry: P22137. Identity and primary gene symbol match; no current uniqueness discrepancy was observed. |
| micro47-gene-CLC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACLC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results of the retained exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query for CLC1 returned 1 entry: P17891. Identity and primary gene symbol match; no current uniqueness discrepancy was observed. |
| micro47-newpher2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2005.04.014; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED15992543: In vivo dynamics of clathrin and its adaptor-dependent recruitment to the actin-based endocytic machinery in yeast. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro47-kaksonen2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2005.09.024; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED16239147: A modular design for the clathrin- and actin-mediated endocytosis machinery. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro47-newpher2005-duke | https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content; Complete printed pp87–96: Summary/Introduction, Table1, all main Results/Discussion and Experimental Procedures, including Fig1–6 captions. Original Duke primary PDF; reading derivative only, no pixels, videos or supplements. | supports | Newpher2005 directly images cortical clathrin and endocytic factors in budding yeast. WT TIRFM places clathrin before Abp1; extensive adaptor colocalization/recruitment tests use sla2Δ or LAT-A and multi-adaptor perturbations. Sla2/End3/Pan1 affect progression or release rather than being required for initial cortical recruitment. The authors explicitly cannot distinguish clathrin disassembly from a coated vesicle/bud leaving the TIRF field; no direct scission claim follows. |
| micro47-payne1988-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083/jcb.106.5.1453%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED2836429: Protein transport to the vacuole and receptor-mediated endocytosis by clathrin heavy chain-deficient yeast. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro47-chu1996-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074/jbc.271.51.33123%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED8955161: The light chain subunit is required for clathrin function in Saccharomyces cerevisiae. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro47-payne1988-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2115047/; Complete native archived abstract/title/authors; scanned PDF link identified but not downloaded/read. | supports | The genuine legacy article page provides Payne1988 identity and its complete abstract: clathrin-heavy-chain-deficient yeast retain impaired endocytosis while CPY sorting remains selective. This supports the source’s experimental context, not an assertion of absolute endocytosis dependence. The scanned main article was not read. |
| micro47-chu1996-doi | https://doi.org/10.1074/jbc.271.51.33123; Raw response title/redirect signature; metadata status200; PII S0021925819788267. | context_only | The HTTP200 DOI response is a short LinkingHub Redirecting HTML locator, not a full primary body. Chu1996 content is assessed only from its complete native MED abstract. |
| micro47-ipr-IPR016341 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016341/; Complete metadata accession/name/type/description and integrated family signatures; compared with corresponding native protein InterPro cross-reference. | supports | IPR016341 is a native InterPro entry of type family for clathrin heavy chain. Its complete description matches the declared source-neutral component class, and the corresponding reviewed yeast accession carries this exact cross-reference. This is not a partial domain or a broader homologous superfamily. |
| micro47-ipr-IPR000996 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000996/; Complete metadata accession/name/type/description and integrated family signatures; compared with corresponding native protein InterPro cross-reference. | supports | IPR000996 is a native InterPro entry of type family for clathrin light chain. Its complete description matches the declared source-neutral component class, and the corresponding reviewed yeast accession carries this exact cross-reference. This is not a partial domain or a broader homologous superfamily. |
| schema-result | just validate data/structures/other/clathrin_vesicle_coat.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/clathrin_vesicle_coat.yaml |
| strict-result | just validate-strict data/structures/other/clathrin_vesicle_coat.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_vesicle_coat-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/clathrin_vesicle_coat.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_vesicle_coat-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_vesicle_coat-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/clathrin_vesicle_coat.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/clathrin_vesicle_coat.yaml; Complete read-only focused native graphs log | supports | data/structures/other/clathrin_vesicle_coat.yaml  (GO:0030125)<br>  yeast_clathrin_endocytic_coat_assembly	clathrin_heavy_chain	COVERED	-&gt;clathrin_heavy_chain (UniProtKB:P22137)<br>  yeast_clathrin_endocytic_coat_assembly	clathrin_light_chain	COVERED	-&gt;clathrin_light_chain (UniProtKB:P17891)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/clathrin_vesicle_coat.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 12 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- COMMON retains its schema meaning present in most members with exceptional losses. The cited yeast studies support ordinary species-level occurrence qualitatively; they do not measure a species-wide prevalence census.
- No primary microscopy pixels, supplemental files or videos were inspected. Text, Methods and embedded figure captions were read only within the stated source extents.
- S288C reference-entry identity is distinct from the particular strains, mutants, tagged constructs and drug-treated cells in the primary studies.
- UNKNOWN formation necessity is retained; localization, cargo-traffic phenotypes, functional loss and formation of an entire coat are not interchangeable.
- Kaksonen2005 was read at complete native abstract tier only. It supports the modular endocytosis and initiation interpretation but detailed unseen experiments are not certified. Newpher itself leaves coat release versus vesicle departure unresolved.
- Payne1988 and Chu1996 were read at complete native abstract tier only. Payne’s scanned main article was not read; the Chu DOI response is an HTTP200 redirect page rather than article text. No detailed unseen experiments are certified.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these clathrin-coat identity, molecular-family, localization and formation claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T050520Z-clathrin-vesicle-coat-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of clathrin vesicle coat
started_at: '2026-10-22T04:47:24Z'
finished_at: '2026-10-22T05:05:20Z'
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
summary: The coat identity, yeast examples and descriptive graph are supported at
  the declared source tiers. One bounded minor resolves the two exact chain-family
  groundings.
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
  - path: data/structures/other/clathrin_vesicle_coat.yaml
    sha256: cef674eb9fc2b08323c1780daa340012db00fd43e3f89c7de880ac972594e17d
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
- target_id: GO:0030125
  path: data/structures/other/clathrin_vesicle_coat.yaml
  label: clathrin vesicle coat
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_vesicle_coat.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; no neighboring scientific-record verdict
    is imported. Exact authority, all current component/function/graph/source placements,
    taxonomic scope, formation semantics, history and discussions were reviewed.
  selection: Batch47 fixed strict path order, index 8; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030125
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030125
  command: just validate data/structures/other/clathrin_vesicle_coat.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030125
  command: just validate-strict data/structures/other/clathrin_vesicle_coat.yaml --out
    /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_vesicle_coat-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - GO:0030125
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/clathrin_vesicle_coat.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-proteins
- check_id: native-graphs
  name: Focused native graphs
  status: passed
  required: true
  target_ids:
  - GO:0030125
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/clathrin_vesicle_coat.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030125
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - micro47-go
  - micro47-tax4932
  - micro47-tax559292
  - micro47-protein-P22137
  - micro47-protein-P17891
  - micro47-gene-CHC1
  - micro47-gene-CLC1
  - micro47-newpher2005-meta
  - micro47-kaksonen2005-meta
  - micro47-newpher2005-duke
  - micro47-payne1988-meta
  - micro47-chu1996-meta
  - micro47-payne1988-legacy
  - micro47-chu1996-doi
  - micro47-ipr-IPR016341
  - micro47-ipr-IPR000996
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030125
  summary: 12 of 12 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030125
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0030125
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0030125
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0030125
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0030125
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
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/clathrin_vesicle_coat.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:59:35Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:59:35Z'
  support: context_only
  summary: ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite
    class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic
    or transport function.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:59:35Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: micro47-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005768,GO:0005802,GO:0005905,GO:0012510,GO:0016020,GO:0030117,GO:0030118,GO:0030119,GO:0030120,GO:0030121,GO:0030122,GO:0030125,GO:0030128,GO:0030130,GO:0030132,GO:0030136,GO:0030140,GO:0030669,GO:0045334,GO:0072583
  locator: 'Complete exact entries GO0030128/0030130/0030125/0030120/0030118/0030117/0030119/0030121/0030122/0030669/0012510/0030140/0045334/0030136/0005768/0005802/0072583:
    id,name,definition,isObsolete,typed children and synonyms; shared response also
    includes pit/membrane entries.'
  accessed_at: '2026-10-22T04:48:27.885977Z'
  support: supports
  summary: GO0030125 is an active exact clathrin-coat identity, distinct from the
    membrane and whole vesicle it coats. The combined native response verifies the
    maintained is_a relations, the two specific coat-to-membrane part_of links, AP1/AP2
    boundaries and GO0072583 endocytosis. The broad coat-to-vesicle parthood is definition-supported;
    a direct GO0030125 part_of GO0030136 edge is not exposed in this response. GO0030118
    describes polymerized heavy/light-chain triskelions linked to membranes by adaptors.
    No exhaustive future inventory is inferred.
  snapshot_sha256: d99cebcf37913222815e3282d94e35f6fa629e25ca25660703949d4f38893d30
- evidence_id: micro47-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:15:34.948894Z'
  support: supports
  summary: ENA taxId 4932 identifies Saccharomyces cerevisiae at rank species; aliases
    and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro47-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:15:34.948991Z'
  support: supports
  summary: ENA taxId 559292 identifies Saccharomyces cerevisiae S288C at rank strain;
    aliases and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro47-protein-P22137
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P22137.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T04:48:27.888375Z'
  support: supports
  summary: P22137 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['CHC1'].
    Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION
    comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 09d51b91c677526fa74c1513304fdd8c51215ce5c9511a6654355fbd16c61648
- evidence_id: micro47-protein-P17891
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P17891.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T04:48:27.888620Z'
  support: supports
  summary: P17891 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['CLC1'].
    Recommended identity, gene aliases, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION
    comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 1b6e6853470eea45530073217e5f1abcfbe6fba0fc5568df34d83a73130d25af
- evidence_id: micro47-gene-CHC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACHC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results of the retained exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T04:48:28.846864Z'
  support: supports
  summary: 'The exact reviewed S288C query for CHC1 returned 1 entry: P22137. Identity
    and primary gene symbol match; no current uniqueness discrepancy was observed.'
  snapshot_sha256: 2a920614f72637e8dca08d8a782c81c920e1e8a01fd1b0b958f6d70602c68b89
  search_scope: Remote UniProt exact gene CHC1, reviewed entries, organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro47-gene-CLC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACLC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results of the retained exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T04:48:28.900316Z'
  support: supports
  summary: 'The exact reviewed S288C query for CLC1 returned 1 entry: P17891. Identity
    and primary gene symbol match; no current uniqueness discrepancy was observed.'
  snapshot_sha256: 263ed77f230c390b1cf03ce642b609d8cff66ef219794d4c6bccab47942bbc69
  search_scope: Remote UniProt exact gene CLC1, reviewed entries, organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro47-newpher2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2005.04.014
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-21T10:57:50.523144Z'
  support: supports
  summary: 'Unique MED15992543: In vivo dynamics of clathrin and its adaptor-dependent
    recruitment to the actin-based endocytic machinery in yeast. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: c99ec084fa3f65e3b5107699c30f42b09489dbc49d6be518d71ff9352d5a199c
- evidence_id: micro47-kaksonen2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2005.09.024
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-21T11:04:40.023205Z'
  support: supports
  summary: 'Unique MED16239147: A modular design for the clathrin- and actin-mediated
    endocytosis machinery. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: b21f04a2ca620468ebafa02936207fe7e04553d44f862f3f18d72a85b6c4aba2
- evidence_id: micro47-newpher2005-duke
  kind: primary_source
  reference: https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content
  locator: 'Complete printed pp87–96: Summary/Introduction, Table1, all main Results/Discussion
    and Experimental Procedures, including Fig1–6 captions. Original Duke primary
    PDF; reading derivative only, no pixels, videos or supplements.'
  accessed_at: '2026-10-21T11:00:52.091438Z'
  support: supports
  summary: Newpher2005 directly images cortical clathrin and endocytic factors in
    budding yeast. WT TIRFM places clathrin before Abp1; extensive adaptor colocalization/recruitment
    tests use sla2Δ or LAT-A and multi-adaptor perturbations. Sla2/End3/Pan1 affect
    progression or release rather than being required for initial cortical recruitment.
    The authors explicitly cannot distinguish clathrin disassembly from a coated vesicle/bud
    leaving the TIRF field; no direct scission claim follows.
  snapshot_sha256: c848e911372b9afb9902e4a74e3cb3dd66ef90eb5e102024cc95fff648bb6c21
- evidence_id: micro47-payne1988-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083/jcb.106.5.1453%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:51:26.650597Z'
  support: supports
  summary: 'Unique MED2836429: Protein transport to the vacuole and receptor-mediated
    endocytosis by clathrin heavy chain-deficient yeast. Authors/year/DOI and the
    complete native abstract were inspected. This row establishes bibliographic identity
    and abstract-level content only; detailed experiments require separately specified
    body evidence.'
  snapshot_sha256: 8f59acc01024a1f3401d8cd9940f2bc7e7d9405411a54d8ca542688f61f78d81
- evidence_id: micro47-chu1996-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074/jbc.271.51.33123%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:51:27.036466Z'
  support: supports
  summary: 'Unique MED8955161: The light chain subunit is required for clathrin function
    in Saccharomyces cerevisiae. Authors/year/DOI and the complete native abstract
    were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 5a8a250589567657c845c1a67443bb6d865d7e4f1bb1c33f8e0462d8b62f8e96
- evidence_id: micro47-payne1988-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2115047/
  locator: Complete native archived abstract/title/authors; scanned PDF link identified
    but not downloaded/read.
  accessed_at: '2026-10-22T04:52:19.992384Z'
  support: supports
  summary: 'The genuine legacy article page provides Payne1988 identity and its complete
    abstract: clathrin-heavy-chain-deficient yeast retain impaired endocytosis while
    CPY sorting remains selective. This supports the source’s experimental context,
    not an assertion of absolute endocytosis dependence. The scanned main article
    was not read.'
  snapshot_sha256: ac9d8d98d54ce1937a739f4ce2e6e70c4d84cc4433430eec35f3aaaf9441d664
- evidence_id: micro47-chu1996-doi
  kind: database
  reference: https://doi.org/10.1074/jbc.271.51.33123
  locator: Raw response title/redirect signature; metadata status200; PII S0021925819788267.
  accessed_at: '2026-10-22T04:52:19.992848Z'
  support: context_only
  summary: The HTTP200 DOI response is a short LinkingHub Redirecting HTML locator,
    not a full primary body. Chu1996 content is assessed only from its complete native
    MED abstract.
  snapshot_sha256: 8f779b3fda0f63faca0c7c4aa3a5067d55cc4341e13bbc1591510186b84b6579
- evidence_id: micro47-ipr-IPR016341
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016341/
  locator: Complete metadata accession/name/type/description and integrated family
    signatures; compared with corresponding native protein InterPro cross-reference.
  accessed_at: '2026-10-22T04:52:19.992724Z'
  support: supports
  summary: IPR016341 is a native InterPro entry of type family for clathrin heavy
    chain. Its complete description matches the declared source-neutral component
    class, and the corresponding reviewed yeast accession carries this exact cross-reference.
    This is not a partial domain or a broader homologous superfamily.
  snapshot_sha256: d7ba4fc389c5301ae037863402c9f51a1206527896388911d9e0c84a50e8e4b1
- evidence_id: micro47-ipr-IPR000996
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000996/
  locator: Complete metadata accession/name/type/description and integrated family
    signatures; compared with corresponding native protein InterPro cross-reference.
  accessed_at: '2026-10-22T04:52:19.991763Z'
  support: supports
  summary: IPR000996 is a native InterPro entry of type family for clathrin light
    chain. Its complete description matches the declared source-neutral component
    class, and the corresponding reviewed yeast accession carries this exact cross-reference.
    This is not a partial domain or a broader homologous superfamily.
  snapshot_sha256: 5995836efc7574dac95b9b8cc8eefc98bbcc11929a451614df5cf290e35c0a66
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/clathrin_vesicle_coat.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:26Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/clathrin_vesicle_coat.yaml'
  snapshot_sha256: e5ebf247054c38c09c5585facd416f77e3abc44383c5a4dd73385fa89dfcb07d
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/clathrin_vesicle_coat.yaml
    --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_vesicle_coat-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:27Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/clathrin_vesicle_coat.yaml\
    \ --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_vesicle_coat-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_vesicle_coat-strict.tsv"
  snapshot_sha256: 6f02cc32175ba28a0305e9bd980e187e4dd97c85b18a3d1020f6e2e2f1a73ee6
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/clathrin_vesicle_coat.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T04:51:52.680593Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/clathrin_vesicle_coat.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T04:51:53.147629Z'
  support: supports
  summary: "data/structures/other/clathrin_vesicle_coat.yaml  (GO:0030125)\n  yeast_clathrin_endocytic_coat_assembly\t\
    clathrin_heavy_chain\tCOVERED\t->clathrin_heavy_chain (UniProtKB:P22137)\n  yeast_clathrin_endocytic_coat_assembly\t\
    clathrin_light_chain\tCOVERED\t->clathrin_light_chain (UniProtKB:P17891)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: ce2df1aa1796fdecdd90f79d6e1cd4c9910648438457424a4c2a9cc920eb6de9
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/clathrin_vesicle_coat.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 12 of 12 collected target identifiers returned OK. No residuals. Native
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
  topic: Exact coat identity and topology
  outcome: supported
  target_ids:
  - GO:0030125
  summary: The exact active GO identity, definition and declared topology are supported.
    Specific coat-to-membrane part_of and is_a links are native typed relations; broad
    coat-to-whole-vesicle parthood is definition-supported rather than an exposed
    direct edge in this response. The proteinaceous coat remains distinct from a lipid
    membrane and from the whole vesicle. The endocytic and TGN terms are specific
    children of the broad vesicle-coat class.
  evidence_ids:
  - micro47-go
  - record
- assessment_id: scope
  area: scope
  topic: Species, strain and prevalence meaning
  outcome: supported
  target_ids:
  - GO:0030125
  summary: Species4932 and strain559292 identities are correct. COMMON means present
    in most species members with exceptional losses; ordinary yeast experiments provide
    qualitative support, not a measured prevalence denominator. Experimental strain/condition
    details are not silently replaced by the reference accession taxon.
  evidence_ids:
  - micro47-tax4932
  - micro47-tax559292
  - schema
  - micro47-newpher2005-meta
  - micro47-newpher2005-duke
  - micro47-kaksonen2005-meta
- assessment_id: proteins
  area: grounding
  topic: Native examples and query claims
  outcome: supported
  target_ids:
  - GO:0030125
  summary: 'All retained accession/gene/status/taxon pairs are correct. Exact reviewed
    S288C queries support the current single-hit claims. Identity-only examples remain
    identity evidence; primary membership and localization are assessed separately. '
  evidence_ids:
  - micro47-protein-P22137
  - micro47-protein-P17891
  - micro47-gene-CHC1
  - micro47-gene-CLC1
- assessment_id: necessity
  area: grounding
  topic: Formation necessity
  outcome: unknown
  target_ids:
  - GO:0030125
  summary: The component essentiality values are already UNKNOWN. The inspected localization,
    association and trafficking data do not establish a single universal requirement
    for formation of every coat represented by this class. No unsupported ESSENTIAL
    claim is introduced.
  evidence_ids:
  - micro47-go
  - schema
  - record
  - micro47-newpher2005-meta
  - micro47-newpher2005-duke
  - micro47-kaksonen2005-meta
- assessment_id: components
  area: grounding
  topic: Exact heavy/light-chain family identities
  outcome: concern
  target_ids:
  - GO:0030125
  summary: The two constituent chain identities and roles are supported. Exact IPR016341
    heavy-chain and IPR000996 light-chain families resolve their explicit reviewed-label-only
    statuses. The two-chain inventory is declared coarse; absence of every optional
    adaptor or triskelion stoichiometric row does not independently create a finding.
  evidence_ids:
  - micro47-go
  - micro47-ipr-IPR016341
  - micro47-ipr-IPR000996
  - micro47-protein-P22137
  - micro47-protein-P17891
  - micro47-payne1988-meta
  - micro47-chu1996-meta
  - micro47-payne1988-legacy
  - micro47-newpher2005-duke
  - record
  - curation
- assessment_id: sources
  area: evidence
  topic: Primary scope and component function
  outcome: supported
  target_ids:
  - GO:0030125
  summary: Payne and Chu abstracts support their stated heavy/light-chain experimental
    context; Chu distinguishes efficient trimerization/proper coat formation and partial
    rescue. Newpher directly supports cortical recruitment and relative timing. The
    record does not turn these studies into proof that every endocytic vesicle absolutely
    requires clathrin or that a TIRF departure is directly observed scission.
  evidence_ids:
  - micro47-payne1988-meta
  - micro47-chu1996-meta
  - micro47-payne1988-legacy
  - micro47-chu1996-doi
  - micro47-newpher2005-meta
  - micro47-newpher2005-duke
  - micro47-kaksonen2005-meta
  - record
- assessment_id: graph
  area: graph
  topic: Descriptive assembly-timing graph
  outcome: supported
  target_ids:
  - GO:0030125
  summary: The six-node/five-edge NONMECHANISTIC ASSEMBLY graph uses heavy/light chain
    part-of, coat/vesicle topology and cortical recruitment preceding later actin.
    Its explicit coarse scope does not claim complete triskelion stoichiometry, all
    adaptors, or a resolved budding/scission sequence.
  evidence_ids:
  - micro47-go
  - micro47-newpher2005-duke
  - micro47-kaksonen2005-meta
  - record
- assessment_id: coverage
  area: completeness
  topic: Whole-target coverage and bounded enrichment
  outcome: supported
  target_ids:
  - GO:0030125
  summary: The entire target, all current components/examples, source placements,
    graph, discussions and history were reviewed. The supported exact mapping issue
    is distinct from optional inventory expansion. No exhaustive absence claim is
    made for future broader-adaptor families; no local-neighbor scientific verdict
    is imported.
  evidence_ids:
  - micro47-go
  - record
  - curation
  - micro47-newpher2005-meta
  - micro47-newpher2005-duke
  - micro47-kaksonen2005-meta
findings:
- finding_id: F1
  issue_key: clathrin.clathrin_vesicle_coat.exact_chain_families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the two exact clathrin-chain family groundings
  description: 'Both source-neutral chain rows remain REVIEWED_LABEL_ONLY despite
    exact active InterPro families: IPR016341 for the heavy chain and IPR000996 for
    the light chain. Native reviewed CHC1/P22137 and CLC1/P17891 carry the respective
    family cross-references. This is a current actionable mapping gap, not a claim
    that the historical pass falsely reported its own work.'
  target_ids:
  - GO:0030125
  field_paths:
  - components[0].grounding
  - components[0].grounding_status
  - components[0].grounding_notes
  - components[1].grounding
  - components[1].grounding_status
  - components[1].grounding_notes
  evidence_ids:
  - micro47-ipr-IPR016341
  - micro47-ipr-IPR000996
  - micro47-protein-P22137
  - micro47-protein-P17891
  - schema
  - curation
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_vesicle_coat.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: 'Minor: the biological chain identities and membership remain
    supported; two exact native family mappings resolve a bounded non-blocking completeness/grounding
    gap.'
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0030125
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_vesicle_coat.yaml
    role: maintained scientific record
  description: Ground heavy chain to InterPro:IPR016341 and light chain to InterPro:IPR000996,
    synchronize current grounding statuses/notes and linked graph nodes while preserving
    the coarse inventory and UNKNOWN formation necessity.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
limitations:
- COMMON retains its schema meaning present in most members with exceptional losses.
  The cited yeast studies support ordinary species-level occurrence qualitatively;
  they do not measure a species-wide prevalence census.
- No primary microscopy pixels, supplemental files or videos were inspected. Text,
  Methods and embedded figure captions were read only within the stated source extents.
- S288C reference-entry identity is distinct from the particular strains, mutants,
  tagged constructs and drug-treated cells in the primary studies.
- UNKNOWN formation necessity is retained; localization, cargo-traffic phenotypes,
  functional loss and formation of an entire coat are not interchangeable.
- Kaksonen2005 was read at complete native abstract tier only. It supports the modular
  endocytosis and initiation interpretation but detailed unseen experiments are not
  certified. Newpher itself leaves coat release versus vesicle departure unresolved.
- Payne1988 and Chu1996 were read at complete native abstract tier only. Payne’s scanned
  main article was not read; the Chu DOI response is an HTTP200 redirect page rather
  than article text. No detailed unseen experiments are certified.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these clathrin-coat identity, molecular-family,
  localization and formation claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
