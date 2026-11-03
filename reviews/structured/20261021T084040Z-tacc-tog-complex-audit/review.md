# TACC/TOG complex identity and mechanistic evidence review

- Review: 20261021T084040Z-tacc-tog-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:25:00Z
- Finished UTC: 2026-10-21T08:40:40Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact complex identity, constituent examples, all three bounded mechanistic graphs, four functions and the unchanged reconstitution figure are supported. The record preserves the source disagreement and experimental limits; no concrete curation defect was established.

## Scope And Provenance

Entire target and tracked image; native ontology, taxonomy, protein and family authorities; claim-bearing Results, Discussion and Methods in all five primary papers; Table1 in the2019 study and visual Figure7 inspection.

Selection: Fifth unreviewed target in batch twelve, selected in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0070850 | data/structures/cytoskeleton/tacc_tog_complex.yaml | maintained | TACC/TOG complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0070850 | Focused validator passed. |
| Focused native strict | passed | True | GO:0070850 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0070850 | 17 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Native UniProt causal-graphs | passed | True | GO:0070850 | Native read-only target check passed. |
| Native UniProt verify | passed | True | GO:0070850 | Native read-only target check passed. |
| Expression-module applicability | not_applicable | False | GO:0070850 | The graphs concern protein association, localization, phosphorylation and cytoskeletal function, without an expression-module mechanism. |
| Claim-level scientific review | passed | True | GO:0070850 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0070850 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0070850 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0070850 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0070850 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0070850 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact partnership and dynamic contexts

identity: supported. Targets: GO:0070850.

The GO definition, generic parent and exact/narrow synonym scopes are consistent. Nucleus, kinetochores, MTOCs and microtubule ends are localization contexts. The record correctly avoids making them universal parent organelles or invariant binary-complex subunits.

### Whole-protein family versus domain

grounding: supported. Targets: GO:0070850.

XMAP215 is an exact family with a native Alp14 crossreference. The TACC accession response supplies a domain and coiled coil; substituting either as the complete component class would overstate its scope. The bounded label-only exception and open TODO remain justified.

### Taxon-paired examples and external Ndc80 node

grounding: supported. Targets: GO:0070850.

Both constituent examples, their aliases, reviewed status and reference taxon match native authorities and unique exact-gene queries. Ndc80 is correctly represented as external docking context. Protein identity checks do not independently prove biological complex residence; the primary experiments supply that support.

### Purified partnership versus native assembly

representation: supported. Targets: GO:0070850.

The binding edge is supported by purified co-sedimentation and appropriately bounded to association. Hydrodynamic behavior does not establish a universal native2:2 stoichiometry, ordered assembly path or full interface; functional loss does not independently measure constituent assembly essentiality.

### Conflicting elongation results remain explicit

evidence: supported. Targets: GO:0070850.

The2016 and2018 experiments support different Alp7 deletion effects on elongation. The record attaches both papers directly to the function and graph edge, retains the discrepancy, and limits occupancy enhancement to the tested reconstitution. It does not claim a universal Alp7 requirement for polymerization.

### Recruitment and partial engineered rescue

evidence: supported. Targets: GO:0070850.

Deletion, time-resolved recruitment and artificial tethering support the Alp7-to-MTOC-Alp14-to-efficient-nucleation chain. Reduced frequencies and partial bypass do not make the binary complex sufficient alone or necessary for every nucleation event. Expression and Mto1-bonsai construct context are retained.

### Kinetochore docking and functional contribution

evidence: supported. Targets: GO:0070850.

The function graph correctly says recruitment is reduced, not abolished, by F420S; SPB localization persists. Purified loop peptides and Nuf2-Alp7C rescue support docking and attachment contributions without proving native geometry, stoichiometry or a depolymerization reaction.

### Phosphorylation, import competence and export assignment

representation: supported. Targets: GO:0070850.

The regulation graph separates Alp7 phosphorylation-dependent accumulation from import competence, and Alp14 export from Alp7 association. The five-site mutant retains delayed entry after LMB. Cut15-fragment two-hybrid and reporter export support bounded models, not a solved native affinity mechanism or NES-Crm1 interface.

### Nuclear accumulation and phenotype scope

evidence: supported. Targets: GO:0070850.

Localization defects and spindle phenotypes support the mitotic assembly function. Suppression by an added NLS is a growth assay result; the record correctly does not call it full rescue of every spindle phenotype.

### Paralog identity and expression-dependent functional tests

scope: supported. Targets: GO:0070850.

The2019 forced-targeting result is correctly confined to tested constructs and expression. Earlier overexpression cross-rescue precludes absolute nonexchangeability. Shared XMAP215 membership does not add Dis1 as a TACC partner.

### Experimental species, reference strain and expression host

scope: supported. Targets: GO:0070850.

The curated mechanism concerns S.pombe, while the protein entries are reference-strain exemplars. Sf9 expression, bacterial purification, budding-yeast two-hybrid and pig-brain tubulin do not establish native complex distribution in those organisms. Generic GO conservation is kept distinct from demonstrated prevalence.

### Unchanged reconstitution figure and accurate panel meaning

provenance: supported. Targets: GO:0070850.

The tracked image is byte-identical to the licensed native source. The paraphrased caption correctly describes mixed-species assay ingredients, focal S.pombe proteins, kymograph scales and growth histograms. It neither presents a whole-cell micrograph nor equates panelD with catastrophe-frequency data.

### Explicit scientific gaps and optional enrichment

completeness: supported. Targets: GO:0070850.

Native stoichiometry, interface, exact TACC whole-protein family, cause of the elongation discrepancy and broader microbial examples remain explicit gaps. No exact missing required assertion or contradiction was established; no stronger mechanism is supplied by inference.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| tacc-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0007020,GO:0051315,GO:0061863,GO:0070850,GO:0090307,GO:0140535; All six term definitions, active flags and parent child relation | supports | Active GO0070850 matches the exact complex definition and is an is_a child of GO0140535. The four active function terms match polymerase activity, nucleation, mitotic spindle assembly and kinetochore attachment. |
| tacc-prep-tax-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; taxId, scientificName and rank | supports | Taxon4896 is S.pombe at species rank. |
| tacc-prep-tax-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; taxId, scientificName and rank | supports | Taxon284812 is S.pombe972h- at strain rank; this is the reference protein taxon, not the identity of every experimental stock. |
| tacc-prep-IPR045110 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045110/; Accession, family type and definition | supports | IPR045110 is the XMAP215 family. Family membership does not by itself establish TACC binding for every member. |
| tacc-prep-IPR024312 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024312/; Accession, domain type and name | supports | IPR024312 is the fungal TACC C-terminal domain, not an exact whole-protein family. |
| tacc-prep-matches-Q9URY2 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q9URY2/; All returned match metadata and pagination | supports | The complete combined match response has count2, no next page, and contains only IPR024312 domain and PF12709 coiled_coil. This bounded accession match supports the retained label-only component and open grounding task. |
| tacc-prep-Q9URY2 | https://rest.uniprot.org/uniprotkb/Q9URY2.json; Primary accession, entry status, protein name, genes, taxon and relevant crossreferences | supports | Reviewed Q9URY2 is Microtubule protein alp7, with gene alp7 and synonym mia1, taxon284812. |
| tacc-prep-O94534 | https://rest.uniprot.org/uniprotkb/O94534.json; Primary accession, entry status, protein name, genes, taxon and relevant crossreferences | supports | Reviewed O94534 is Spindle pole body component alp14, with gene alp14 and synonym mtc1, taxon284812; its native InterPro crossreference includes IPR045110. |
| tacc-prep-Q10198 | https://rest.uniprot.org/uniprotkb/Q10198.json; Primary accession, entry status, protein name, genes, taxon and relevant crossreferences | supports | Reviewed Q10198 is Kinetochore protein ndc80, with gene ndc80, taxon284812. It grounds the external docking-context node, not an additional binary-complex constituent. |
| tacc-prep-query-alp7 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Aalp7%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Complete results accession and gene tokens | supports | The exact reviewed gene query for alp7 in taxon284812 returns only Q9URY2. |
| tacc-prep-query-mia1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Amia1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Complete results accession and gene tokens | supports | The exact reviewed gene query for mia1 in taxon284812 returns only Q9URY2. |
| tacc-prep-query-alp14 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Aalp14%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Complete results accession and gene tokens | supports | The exact reviewed gene query for alp14 in taxon284812 returns only O94534. |
| tacc-prep-query-mtc1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Amtc1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Complete results accession and gene tokens | supports | The exact reviewed gene query for mtc1 in taxon284812 returns only O94534. |
| tacc-prep-hussmann2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/srep20653; Single result DOI, title, PMID and PMCID | supports | The exact DOI query identifies the corresponding primary paper and matches the native PMC package. |
| tacc-prep-hussmann2016-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4749977.1/PMC4749977.1.xml; Entire main Results, Discussion and Methods; Figure7 caption and native figure; article licence | supports | Purified full-length Alp7 and Alp14 co-sediment; Alp14 binds soluble tubulin while Alp7 alone does not detectably bind under the assay conditions. Cellular deletions and reconstitution support assay-specific elongation effects. Mixed-tubulin TIRF distinguishes enhanced Alp14 occupancy from universal cellular necessity. |
| tacc-prep-hussmann2016-package | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC4749977.1.json; Identity, version, retraction flag and XML MD5 | supports | The native version1 package has the matching DOI/PMID, is not marked retracted, and its XML MD5 equals the fetched primary body. |
| tacc-prep-nucleation2018-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2018.04.008; Single result DOI, title, PMID and PMCID | supports | The exact DOI query identifies the corresponding primary paper and matches the native PMC package. |
| tacc-prep-nucleation2018-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC7263743.1/PMC7263743.1.xml; Entire main Results, Discussion and STAR Methods; Figures4-7 captions | supports | Alp7 loss reduces Alp14 recruitment to MTOCs and nucleation, while plus-end tracking and normal elongation persist. Engineered Alp14-GBP/Mto1-bonsai targeting partially bypasses Alp7 for nucleation. The authors explicitly retain the discrepancy with the2016 elongation result. |
| tacc-prep-nucleation2018-package | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC7263743.1.json; Identity, version, retraction flag and XML MD5 | supports | The native version1 package has the matching DOI/PMID, is not marked retracted, and its XML MD5 equals the fetched primary body. |
| tacc-prep-attachment2013-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.E12-11-0817; Single result DOI, title, PMID and PMCID | supports | The exact DOI query identifies the corresponding primary paper and matches the native PMC package. |
| tacc-prep-attachment2013-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3623634.1/PMC3623634.1.xml; Entire main Results, Discussion and Methods; Figures1-8 captions, especially4-6 | supports | Ndc80 F420S reduces kinetochore Alp7/Alp14 signals by30-40percent while SPB localization remains. Pull-down, co-IP and peptide arrays support docking contacts; Nuf2-Alp7C targeting suppresses attachment-related defects without resolving a full native interface. |
| tacc-prep-attachment2013-package | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC3623634.1.json; Identity, version, retraction flag and XML MD5 | supports | The native version1 package has the matching DOI/PMID, is not marked retracted, and its XML MD5 equals the fetched primary body. |
| tacc-prep-transport2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.E13-11-0679; Single result DOI, title, PMID and PMCID | supports | The exact DOI query identifies the corresponding primary paper and matches the native PMC package. |
| tacc-prep-transport2014-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4072571.1/PMC4072571.1.xml; Entire main Results, Discussion and Methods; Figures1-7 captions | supports | Alp14 L615A retains Alp7 binding but changes export; Alp14601-620 confers reporter export. Alp7 five-site mutation impairs mitotic nuclear accumulation while preserving binding and delayed LMB-dependent nuclear entry. Truncated two-hybrid results support an importin-affinity model; artificial NLS suppresses growth defects. |
| tacc-prep-transport2014-package | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC4072571.1.json; Identity, version, retraction flag and XML MD5 | supports | The native version1 package has the matching DOI/PMID, is not marked retracted, and its XML MD5 equals the fetched primary body. |
| tacc-prep-dis1_2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.3390/ijms20205108; Single result DOI, title, PMID and PMCID | supports | The exact DOI query identifies the corresponding primary paper and matches the native PMC package. |
| tacc-prep-dis1_2019-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6834199.1/PMC6834199.1.xml; Results2.1-2.6; Discussion3.1-3.2; Methods4.1-4.7; Figures5-6 captions; Table1 strain/construct details | supports | Reciprocal targeting at tested endogenous expression fails to exchange Alp14 and Dis1 functions. The source retains earlier overexpression cross-rescue. Engineered Alp14-NLS targeting and conditional double-mutant phenotypes do not establish universal nonexchangeability or a Dis1-containing TACC complex. |
| tacc-prep-dis1_2019-package | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC6834199.1.json; Identity, version, retraction flag and XML MD5 | supports | The native version1 package has the matching DOI/PMID, is not marked retracted, and its XML MD5 equals the fetched primary body. |
| tacc-prep-figure7 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4749977.1/srep20653-f7.jpg; Native Figure7 A-D,2micrometer and1minute bars, and exact byte comparisons | supports | Visual inspection confirms assay diagramA, kymographsB/C and growth-rate histogramsD. PanelD does not plot catastrophe frequencies. The native bytes exactly match the tracked image SHA256 and package MD5; source licence is CC BY4.0. |
| record | data/structures/cytoskeleton/tacc_tog_complex.yaml; Entire maintained YAML, all three graphs, eight discussions, history, examples, functions and image metadata | context_only | The target preserves a binary complex, species-specific mechanisms, UNKNOWN assembly essentiality and explicit unresolved family, stoichiometry, elongation and taxon boundaries. There are no stored verbatim evidence snippets. |
| schema-result | just validate data/structures/cytoskeleton/tacc_tog_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/tacc_tog_complex.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/tacc_tog_complex.yaml --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/tacc_tog_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/tacc_tog_complex.yaml --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/tacc_tog_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch12-20261021-ipvr425j/tacc_tog_complex-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/tacc_tog_complex.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 17 of 17 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| native-causal-graphs | /private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/tacc_tog_complex.yaml --causal-graphs; Complete captured native target output | supports | data/structures/cytoskeleton/tacc_tog_complex.yaml  (GO:0070850)<br>  tacc_tog_association	tacc	COVERED	-&gt;tacc (UniProtKB:Q9URY2)<br>  tacc_tog_association	xmap215	COVERED	-&gt;xmap215 (UniProtKB:O94534)<br>  tacc_tog_function	tacc	COVERED	-&gt;tacc (UniProtKB:Q9URY2)<br>  tacc_tog_function	ndc80	UNANCHORED_WITH_UNIPROT	Ndc80 kinetochore docking context (UniProtKB:Q10198)<br>  tacc_tog_transport	tacc	COVERED	-&gt;tacc (UniProtKB:Q9URY2)<br>  tacc_tog_transport	xmap215	COVERED	-&gt;xmap215 (UniProtKB:O94534)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     5  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     6  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/tacc_tog_complex.yaml --verify; Complete captured native target output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The2016 and2018 Alp7 deletion effects on elongation differ; strain or assay context is a proposed explanation, not a demonstrated resolution.
- Purified association does not determine universal native stoichiometry, assembly order or interface. Constituent assembly essentiality remains UNKNOWN.
- Forced targeting, truncations, reporter export and two-hybrid fragments are engineered assays; they do not establish complete native recruitment or transport interfaces.
- Native TACC matching is bounded to Q9URY2 and its complete current InterPro response. It does not establish absence of homologs or of a suitable family elsewhere.
- The five primary claim-bearing main-text Results, Discussion and Methods were read. Supplementary files/movies and raw datasets were not independently audited; main-text descriptions of those experiments are not represented as direct supplementary-data inspection.
- Only Figure7 was visually inspected. Other relevant figure captions were read with the main text; numerical results were not independently recomputed from images or raw data.
- The species exemplar and reference sequence taxon are distinct from the engineered experimental stocks and heterologous assay ingredients. Broader occurrence and universal transport mechanisms are not established.
- Alp14 and Dis1 nonexchangeability is limited to the tested endogenous-expression targeting experiments, including the Alp14-NLS construct in Table1; prior overexpression cross-rescue remains relevant.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- No scientific record, tracked image or generated page is edited. Private primary-source bytes are not included in the review bundle.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084040Z-tacc-tog-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: TACC/TOG complex identity and mechanistic evidence review
started_at: '2026-10-21T08:25:00Z'
finished_at: '2026-10-21T08:40:40Z'
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
summary: Exact complex identity, constituent examples, all three bounded mechanistic
  graphs, four functions and the unchanged reconstitution figure are supported. The
  record preserves the source disagreement and experimental limits; no concrete curation
  defect was established.
source:
  git_revision: 99692a3d5f16a7dcd6db7e3811344c299a977b81
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
  - path: data/images/cytoskeleton/tacc_tog_complex/pmc4749977_f7.jpg
    sha256: 435c851418d002e2c49b2ccc3d39eac1f3bf5b30e5881c56f40c8876d81ef752
    role: context
  - path: data/structures/cytoskeleton/tacc_tog_complex.yaml
    sha256: 7d2c57864f3928f8ab9bbc0d7e702aa142292ae00252b385f40a5a8dbcd7b787
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
- target_id: GO:0070850
  path: data/structures/cytoskeleton/tacc_tog_complex.yaml
  label: TACC/TOG complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/tacc_tog_complex.yaml
    role: maintained scientific record
scope:
  description: Entire target and tracked image; native ontology, taxonomy, protein
    and family authorities; claim-bearing Results, Discussion and Methods in all five
    primary papers; Table1 in the2019 study and visual Figure7 inspection.
  selection: Fifth unreviewed target in batch twelve, selected in repository path
    order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0070850
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: just validate data/structures/cytoskeleton/tacc_tog_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: just validate-strict data/structures/cytoskeleton/tacc_tog_complex.yaml
    --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/tacc_tog_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0070850
  summary: 17 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: native-causal-graphs
  name: Native UniProt causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: /private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/tacc_tog_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native read-only target check passed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: /private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/tacc_tog_complex.yaml
    --verify
  exit_code: 0
  summary: Native read-only target check passed.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0070850
  summary: The graphs concern protein association, localization, phosphorylation and
    cytoskeletal function, without an expression-module mechanism.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0070850
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - tacc-prep-go
  - tacc-prep-tax-4896
  - tacc-prep-tax-284812
  - tacc-prep-IPR045110
  - tacc-prep-IPR024312
  - tacc-prep-matches-Q9URY2
  - tacc-prep-Q9URY2
  - tacc-prep-O94534
  - tacc-prep-Q10198
  - tacc-prep-query-alp7
  - tacc-prep-query-mia1
  - tacc-prep-query-alp14
  - tacc-prep-query-mtc1
  - tacc-prep-hussmann2016-meta
  - tacc-prep-hussmann2016-jats
  - tacc-prep-hussmann2016-package
  - tacc-prep-nucleation2018-meta
  - tacc-prep-nucleation2018-jats
  - tacc-prep-nucleation2018-package
  - tacc-prep-attachment2013-meta
  - tacc-prep-attachment2013-jats
  - tacc-prep-attachment2013-package
  - tacc-prep-transport2014-meta
  - tacc-prep-transport2014-jats
  - tacc-prep-transport2014-package
  - tacc-prep-dis1_2019-meta
  - tacc-prep-dis1_2019-jats
  - tacc-prep-dis1_2019-package
  - tacc-prep-figure7
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: tacc-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0007020,GO:0051315,GO:0061863,GO:0070850,GO:0090307,GO:0140535
  locator: All six term definitions, active flags and parent child relation
  accessed_at: '2026-10-21T08:24:46.878467Z'
  support: supports
  summary: Active GO0070850 matches the exact complex definition and is an is_a child
    of GO0140535. The four active function terms match polymerase activity, nucleation,
    mitotic spindle assembly and kinetochore attachment.
  snapshot_sha256: cdf00b1e3e72e625e9dc0785a818930f660ce068dbf53a7503f22da8524fb27b
- evidence_id: tacc-prep-tax-4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: taxId, scientificName and rank
  accessed_at: '2026-10-21T08:24:47.543159Z'
  support: supports
  summary: Taxon4896 is S.pombe at species rank.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: tacc-prep-tax-284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: taxId, scientificName and rank
  accessed_at: '2026-10-21T08:24:46.881223Z'
  support: supports
  summary: Taxon284812 is S.pombe972h- at strain rank; this is the reference protein
    taxon, not the identity of every experimental stock.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: tacc-prep-IPR045110
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045110/
  locator: Accession, family type and definition
  accessed_at: '2026-10-21T08:24:48.119499Z'
  support: supports
  summary: IPR045110 is the XMAP215 family. Family membership does not by itself establish
    TACC binding for every member.
  snapshot_sha256: e0ba89dab0b5c5383525985f74a81b6a5862a318c457d70882d37afa9b94017e
- evidence_id: tacc-prep-IPR024312
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024312/
  locator: Accession, domain type and name
  accessed_at: '2026-10-21T08:24:48.060338Z'
  support: supports
  summary: IPR024312 is the fungal TACC C-terminal domain, not an exact whole-protein
    family.
  snapshot_sha256: e605d3b7216ab19f4229b3206ce52b2e41631b14fd70741a8c821d50d642fb4e
- evidence_id: tacc-prep-matches-Q9URY2
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q9URY2/
  locator: All returned match metadata and pagination
  accessed_at: '2026-10-21T08:24:50.221153Z'
  support: supports
  summary: The complete combined match response has count2, no next page, and contains
    only IPR024312 domain and PF12709 coiled_coil. This bounded accession match supports
    the retained label-only component and open grounding task.
  snapshot_sha256: 5c2231b4f665a8293114eb467b243f6ee50b206aed10efaaf73d8af44cae0748
- evidence_id: tacc-prep-Q9URY2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9URY2.json
  locator: Primary accession, entry status, protein name, genes, taxon and relevant
    crossreferences
  accessed_at: '2026-10-21T08:24:48.169338Z'
  support: supports
  summary: Reviewed Q9URY2 is Microtubule protein alp7, with gene alp7 and synonym
    mia1, taxon284812.
  snapshot_sha256: 69a22093a5968e9a614a5170718632ab935b0628867cab263df68ad3bb240fe7
- evidence_id: tacc-prep-O94534
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O94534.json
  locator: Primary accession, entry status, protein name, genes, taxon and relevant
    crossreferences
  accessed_at: '2026-10-21T08:24:47.644177Z'
  support: supports
  summary: Reviewed O94534 is Spindle pole body component alp14, with gene alp14 and
    synonym mtc1, taxon284812; its native InterPro crossreference includes IPR045110.
  snapshot_sha256: 257ba28d9d0e8203582177682405142bf2445317baad602e9f31a1171e13a722
- evidence_id: tacc-prep-Q10198
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q10198.json
  locator: Primary accession, entry status, protein name, genes, taxon and relevant
    crossreferences
  accessed_at: '2026-10-21T08:24:47.604695Z'
  support: supports
  summary: Reviewed Q10198 is Kinetochore protein ndc80, with gene ndc80, taxon284812.
    It grounds the external docking-context node, not an additional binary-complex
    constituent.
  snapshot_sha256: 74dfc8ac8dfe5d6bb01ea8ef213bcfab5de60eaad94002910b2641df21ba3234
- evidence_id: tacc-prep-query-alp7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Aalp7%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete results accession and gene tokens
  accessed_at: '2026-10-21T08:24:48.349926Z'
  support: supports
  summary: The exact reviewed gene query for alp7 in taxon284812 returns only Q9URY2.
  snapshot_sha256: 85a9ab6b3fa150223334efcf5eb54f2eb1f93a74afb8b0337782971b6a8741b0
- evidence_id: tacc-prep-query-mia1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amia1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete results accession and gene tokens
  accessed_at: '2026-10-21T08:24:48.460786Z'
  support: supports
  summary: The exact reviewed gene query for mia1 in taxon284812 returns only Q9URY2.
  snapshot_sha256: 85a9ab6b3fa150223334efcf5eb54f2eb1f93a74afb8b0337782971b6a8741b0
- evidence_id: tacc-prep-query-alp14
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Aalp14%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete results accession and gene tokens
  accessed_at: '2026-10-21T08:24:48.763513Z'
  support: supports
  summary: The exact reviewed gene query for alp14 in taxon284812 returns only O94534.
  snapshot_sha256: e23245d00978cff6a713e7e7a13dca05e5f49f13fe2ad5e7af6deb290cb48622
- evidence_id: tacc-prep-query-mtc1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amtc1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete results accession and gene tokens
  accessed_at: '2026-10-21T08:24:48.892800Z'
  support: supports
  summary: The exact reviewed gene query for mtc1 in taxon284812 returns only O94534.
  snapshot_sha256: e23245d00978cff6a713e7e7a13dca05e5f49f13fe2ad5e7af6deb290cb48622
- evidence_id: tacc-prep-hussmann2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/srep20653
  locator: Single result DOI, title, PMID and PMCID
  accessed_at: '2026-10-21T08:24:56.253501Z'
  support: supports
  summary: The exact DOI query identifies the corresponding primary paper and matches
    the native PMC package.
  snapshot_sha256: 354458b0bcbec363f7b356fa3ddb226bd061d148940194781b076f6fa5774c10
- evidence_id: tacc-prep-hussmann2016-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4749977.1/PMC4749977.1.xml
  locator: Entire main Results, Discussion and Methods; Figure7 caption and native
    figure; article licence
  accessed_at: '2026-10-21T08:24:58.321391Z'
  support: supports
  summary: Purified full-length Alp7 and Alp14 co-sediment; Alp14 binds soluble tubulin
    while Alp7 alone does not detectably bind under the assay conditions. Cellular
    deletions and reconstitution support assay-specific elongation effects. Mixed-tubulin
    TIRF distinguishes enhanced Alp14 occupancy from universal cellular necessity.
  snapshot_sha256: 12a9df0a6cd70f2a6c93d068946c8bbe569417d91d70a49bc53da9564473c5b4
- evidence_id: tacc-prep-hussmann2016-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC4749977.1.json
  locator: Identity, version, retraction flag and XML MD5
  accessed_at: '2026-10-21T08:24:58.282693Z'
  support: supports
  summary: The native version1 package has the matching DOI/PMID, is not marked retracted,
    and its XML MD5 equals the fetched primary body.
  snapshot_sha256: c488d784ad6e9388055b3c84ecc432d60f8cf56c00dcdb719362c34c74b26f35
- evidence_id: tacc-prep-nucleation2018-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2018.04.008
  locator: Single result DOI, title, PMID and PMCID
  accessed_at: '2026-10-21T08:24:56.998533Z'
  support: supports
  summary: The exact DOI query identifies the corresponding primary paper and matches
    the native PMC package.
  snapshot_sha256: b74df11fa0ddb1e1e7bf647c1472afe82395fed286563761d94c47485e995f99
- evidence_id: tacc-prep-nucleation2018-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7263743.1/PMC7263743.1.xml
  locator: Entire main Results, Discussion and STAR Methods; Figures4-7 captions
  accessed_at: '2026-10-21T08:25:37.526729Z'
  support: supports
  summary: Alp7 loss reduces Alp14 recruitment to MTOCs and nucleation, while plus-end
    tracking and normal elongation persist. Engineered Alp14-GBP/Mto1-bonsai targeting
    partially bypasses Alp7 for nucleation. The authors explicitly retain the discrepancy
    with the2016 elongation result.
  snapshot_sha256: 5c6000e8b847fcdedb2b6d328d7a87e026432a1cb816daf6c5461f8cde76c9aa
- evidence_id: tacc-prep-nucleation2018-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC7263743.1.json
  locator: Identity, version, retraction flag and XML MD5
  accessed_at: '2026-10-21T08:25:37.450615Z'
  support: supports
  summary: The native version1 package has the matching DOI/PMID, is not marked retracted,
    and its XML MD5 equals the fetched primary body.
  snapshot_sha256: 791a4b1158cc49e85d5d0352bbb5a7f548d1a25906d381770bf1a18ae4260a8f
- evidence_id: tacc-prep-attachment2013-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E12-11-0817
  locator: Single result DOI, title, PMID and PMCID
  accessed_at: '2026-10-21T08:24:57.838564Z'
  support: supports
  summary: The exact DOI query identifies the corresponding primary paper and matches
    the native PMC package.
  snapshot_sha256: 645ddf68db8420489cd79e638494223454ac5f67da38c09f9fd2b1db93625f69
- evidence_id: tacc-prep-attachment2013-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3623634.1/PMC3623634.1.xml
  locator: Entire main Results, Discussion and Methods; Figures1-8 captions, especially4-6
  accessed_at: '2026-10-21T08:25:37.983277Z'
  support: supports
  summary: Ndc80 F420S reduces kinetochore Alp7/Alp14 signals by30-40percent while
    SPB localization remains. Pull-down, co-IP and peptide arrays support docking
    contacts; Nuf2-Alp7C targeting suppresses attachment-related defects without resolving
    a full native interface.
  snapshot_sha256: a175c7cb3756c9d5d46dde7bdac3d4badc4639f5a9e5cd40820da74b997e9c18
- evidence_id: tacc-prep-attachment2013-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC3623634.1.json
  locator: Identity, version, retraction flag and XML MD5
  accessed_at: '2026-10-21T08:25:37.784367Z'
  support: supports
  summary: The native version1 package has the matching DOI/PMID, is not marked retracted,
    and its XML MD5 equals the fetched primary body.
  snapshot_sha256: 32e9d5e12c0b64eb454779d24184930dce0cfeee93a5c8afe99e58941656d519
- evidence_id: tacc-prep-transport2014-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E13-11-0679
  locator: Single result DOI, title, PMID and PMCID
  accessed_at: '2026-10-21T08:24:56.927168Z'
  support: supports
  summary: The exact DOI query identifies the corresponding primary paper and matches
    the native PMC package.
  snapshot_sha256: 2c916766c3faab23a50a94be7c8d81c10f5b0f8ca3e3ac9dd828ee2c41d17eef
- evidence_id: tacc-prep-transport2014-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4072571.1/PMC4072571.1.xml
  locator: Entire main Results, Discussion and Methods; Figures1-7 captions
  accessed_at: '2026-10-21T08:25:37.579401Z'
  support: supports
  summary: Alp14 L615A retains Alp7 binding but changes export; Alp14601-620 confers
    reporter export. Alp7 five-site mutation impairs mitotic nuclear accumulation
    while preserving binding and delayed LMB-dependent nuclear entry. Truncated two-hybrid
    results support an importin-affinity model; artificial NLS suppresses growth defects.
  snapshot_sha256: 7de093d110f396a921dcb99f1aae9c5280a88e1498a67496caa0c7f595c20398
- evidence_id: tacc-prep-transport2014-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC4072571.1.json
  locator: Identity, version, retraction flag and XML MD5
  accessed_at: '2026-10-21T08:25:37.450328Z'
  support: supports
  summary: The native version1 package has the matching DOI/PMID, is not marked retracted,
    and its XML MD5 equals the fetched primary body.
  snapshot_sha256: ac5c9e626ed6fc45b040885a9fc1418d25d143fc0a2b591cb77b0b7c84fa5afa
- evidence_id: tacc-prep-dis1_2019-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.3390/ijms20205108
  locator: Single result DOI, title, PMID and PMCID
  accessed_at: '2026-10-21T08:24:57.838659Z'
  support: supports
  summary: The exact DOI query identifies the corresponding primary paper and matches
    the native PMC package.
  snapshot_sha256: a02668b811df46dd4c571f7e99afb718b981ad4d234ecb8fa486d70b2674760e
- evidence_id: tacc-prep-dis1_2019-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6834199.1/PMC6834199.1.xml
  locator: Results2.1-2.6; Discussion3.1-3.2; Methods4.1-4.7; Figures5-6 captions;
    Table1 strain/construct details
  accessed_at: '2026-10-21T08:25:38.023246Z'
  support: supports
  summary: Reciprocal targeting at tested endogenous expression fails to exchange
    Alp14 and Dis1 functions. The source retains earlier overexpression cross-rescue.
    Engineered Alp14-NLS targeting and conditional double-mutant phenotypes do not
    establish universal nonexchangeability or a Dis1-containing TACC complex.
  snapshot_sha256: 308dd12b0a92c836d2337214dae7cede96eeab5b2fb45c2e866a6f03e46db690
- evidence_id: tacc-prep-dis1_2019-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC6834199.1.json
  locator: Identity, version, retraction flag and XML MD5
  accessed_at: '2026-10-21T08:25:37.903405Z'
  support: supports
  summary: The native version1 package has the matching DOI/PMID, is not marked retracted,
    and its XML MD5 equals the fetched primary body.
  snapshot_sha256: 5cb5c3ba97bdcf98a7d66eedcd3b2d9d70e445f0b35a6ca346d7153bbe853827
- evidence_id: tacc-prep-figure7
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4749977.1/srep20653-f7.jpg
  locator: Native Figure7 A-D,2micrometer and1minute bars, and exact byte comparisons
  accessed_at: '2026-10-21T08:24:59.479727Z'
  support: supports
  summary: Visual inspection confirms assay diagramA, kymographsB/C and growth-rate
    histogramsD. PanelD does not plot catastrophe frequencies. The native bytes exactly
    match the tracked image SHA256 and package MD5; source licence is CC BY4.0.
  snapshot_sha256: 435c851418d002e2c49b2ccc3d39eac1f3bf5b30e5881c56f40c8876d81ef752
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/tacc_tog_complex.yaml
  locator: Entire maintained YAML, all three graphs, eight discussions, history, examples,
    functions and image metadata
  accessed_at: '2026-10-21T08:33:53Z'
  support: context_only
  summary: The target preserves a binary complex, species-specific mechanisms, UNKNOWN
    assembly essentiality and explicit unresolved family, stoichiometry, elongation
    and taxon boundaries. There are no stored verbatim evidence snippets.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/tacc_tog_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:25:01Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/tacc_tog_complex.yaml'
  snapshot_sha256: 825c52e99d80f6ee9390bde108dde0f7f0f8b6cdf68039d09184bf88c25997e8
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/tacc_tog_complex.yaml
    --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/tacc_tog_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:25:03Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/tacc_tog_complex.yaml\
    \ --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/tacc_tog_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch12-20261021-ipvr425j/tacc_tog_complex-strict.tsv"
  snapshot_sha256: 24661729ff144c51add6cfab79053f32547eea06194766b0f10132634180d597
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/tacc_tog_complex.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T08:33:53Z'
  support: supports
  summary: '17 of 17 collected target identifiers returned OK at the unchanged base.
    Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/tacc_tog_complex.yaml
    --causal-graphs
  locator: Complete captured native target output
  accessed_at: '2026-10-21T08:31:00.213011Z'
  support: supports
  summary: "data/structures/cytoskeleton/tacc_tog_complex.yaml  (GO:0070850)\n  tacc_tog_association\t\
    tacc\tCOVERED\t->tacc (UniProtKB:Q9URY2)\n  tacc_tog_association\txmap215\tCOVERED\t\
    ->xmap215 (UniProtKB:O94534)\n  tacc_tog_function\ttacc\tCOVERED\t->tacc (UniProtKB:Q9URY2)\n\
    \  tacc_tog_function\tndc80\tUNANCHORED_WITH_UNIPROT\tNdc80 kinetochore docking\
    \ context (UniProtKB:Q10198)\n  tacc_tog_transport\ttacc\tCOVERED\t->tacc (UniProtKB:Q9URY2)\n\
    \  tacc_tog_transport\txmap215\tCOVERED\t->xmap215 (UniProtKB:O94534)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     5  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     1  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ PARTIAL_EXAMPLES          component_ref target holds protein_examples but has\
    \ unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target\
    \ declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_NO_UNIPROT     no component_ref\
    \ and no UniProtKB grounding or xref on the node\n     6  total GENE_OR_PROTEIN\
    \ causal nodes"
  snapshot_sha256: 044e7cbbd36531339745734edc80fb6ecb88657e47067af280500204392bf6ca
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/tacc_tog_complex.yaml
    --verify
  locator: Complete captured native target output
  accessed_at: '2026-10-21T08:31:03.396003Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec
  accessed_at: '2026-10-19T07:38:12Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 7b6165ba8532d080a336f7a5a4c29b456fdf7182dd596410b700dfe60af61a06
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-19T07:29:37Z'
  support: supports
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: b98e3eecd58a81fa46033e6baca6977811a439f119b943fd5d9931964adb2680
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad
  accessed_at: '2026-10-19T07:32:39Z'
  support: supports
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-19T07:29:45Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4
  accessed_at: '2026-10-19T08:04:01Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  snapshot_sha256: 7cb413edccc92ee6ce79a32cd2b96a59bc4da37f2cb7b326eaca51a64f723cfb
assessments:
- assessment_id: identity
  area: identity
  topic: Exact partnership and dynamic contexts
  outcome: supported
  target_ids:
  - GO:0070850
  summary: The GO definition, generic parent and exact/narrow synonym scopes are consistent.
    Nucleus, kinetochores, MTOCs and microtubule ends are localization contexts. The
    record correctly avoids making them universal parent organelles or invariant binary-complex
    subunits.
  evidence_ids:
  - tacc-prep-go
  - tacc-prep-nucleation2018-jats
  - tacc-prep-transport2014-jats
  - record
- assessment_id: families
  area: grounding
  topic: Whole-protein family versus domain
  outcome: supported
  target_ids:
  - GO:0070850
  summary: XMAP215 is an exact family with a native Alp14 crossreference. The TACC
    accession response supplies a domain and coiled coil; substituting either as the
    complete component class would overstate its scope. The bounded label-only exception
    and open TODO remain justified.
  evidence_ids:
  - tacc-prep-IPR045110
  - tacc-prep-IPR024312
  - tacc-prep-matches-Q9URY2
  - tacc-prep-Q9URY2
  - tacc-prep-O94534
  - tacc-prep-Q10198
  - record
- assessment_id: proteins
  area: grounding
  topic: Taxon-paired examples and external Ndc80 node
  outcome: supported
  target_ids:
  - GO:0070850
  summary: Both constituent examples, their aliases, reviewed status and reference
    taxon match native authorities and unique exact-gene queries. Ndc80 is correctly
    represented as external docking context. Protein identity checks do not independently
    prove biological complex residence; the primary experiments supply that support.
  evidence_ids:
  - tacc-prep-Q9URY2
  - tacc-prep-O94534
  - tacc-prep-Q10198
  - tacc-prep-query-alp7
  - tacc-prep-query-mia1
  - tacc-prep-query-alp14
  - tacc-prep-query-mtc1
  - tacc-prep-tax-4896
  - tacc-prep-tax-284812
  - tacc-prep-hussmann2016-jats
  - tacc-prep-attachment2013-jats
  - record
- assessment_id: association
  area: representation
  topic: Purified partnership versus native assembly
  outcome: supported
  target_ids:
  - GO:0070850
  summary: The binding edge is supported by purified co-sedimentation and appropriately
    bounded to association. Hydrodynamic behavior does not establish a universal native2:2
    stoichiometry, ordered assembly path or full interface; functional loss does not
    independently measure constituent assembly essentiality.
  evidence_ids:
  - tacc-prep-hussmann2016-jats
  - record
- assessment_id: polymerase
  area: evidence
  topic: Conflicting elongation results remain explicit
  outcome: supported
  target_ids:
  - GO:0070850
  summary: The2016 and2018 experiments support different Alp7 deletion effects on
    elongation. The record attaches both papers directly to the function and graph
    edge, retains the discrepancy, and limits occupancy enhancement to the tested
    reconstitution. It does not claim a universal Alp7 requirement for polymerization.
  evidence_ids:
  - tacc-prep-hussmann2016-jats
  - tacc-prep-nucleation2018-jats
  - tacc-prep-figure7
  - record
- assessment_id: nucleation
  area: evidence
  topic: Recruitment and partial engineered rescue
  outcome: supported
  target_ids:
  - GO:0070850
  summary: Deletion, time-resolved recruitment and artificial tethering support the
    Alp7-to-MTOC-Alp14-to-efficient-nucleation chain. Reduced frequencies and partial
    bypass do not make the binary complex sufficient alone or necessary for every
    nucleation event. Expression and Mto1-bonsai construct context are retained.
  evidence_ids:
  - tacc-prep-nucleation2018-jats
  - record
- assessment_id: attachment
  area: evidence
  topic: Kinetochore docking and functional contribution
  outcome: supported
  target_ids:
  - GO:0070850
  summary: The function graph correctly says recruitment is reduced, not abolished,
    by F420S; SPB localization persists. Purified loop peptides and Nuf2-Alp7C rescue
    support docking and attachment contributions without proving native geometry,
    stoichiometry or a depolymerization reaction.
  evidence_ids:
  - tacc-prep-attachment2013-jats
  - record
- assessment_id: transport
  area: representation
  topic: Phosphorylation, import competence and export assignment
  outcome: supported
  target_ids:
  - GO:0070850
  summary: The regulation graph separates Alp7 phosphorylation-dependent accumulation
    from import competence, and Alp14 export from Alp7 association. The five-site
    mutant retains delayed entry after LMB. Cut15-fragment two-hybrid and reporter
    export support bounded models, not a solved native affinity mechanism or NES-Crm1
    interface.
  evidence_ids:
  - tacc-prep-transport2014-jats
  - record
- assessment_id: spindle
  area: evidence
  topic: Nuclear accumulation and phenotype scope
  outcome: supported
  target_ids:
  - GO:0070850
  summary: Localization defects and spindle phenotypes support the mitotic assembly
    function. Suppression by an added NLS is a growth assay result; the record correctly
    does not call it full rescue of every spindle phenotype.
  evidence_ids:
  - tacc-prep-transport2014-jats
  - record
- assessment_id: dis1
  area: scope
  topic: Paralog identity and expression-dependent functional tests
  outcome: supported
  target_ids:
  - GO:0070850
  summary: The2019 forced-targeting result is correctly confined to tested constructs
    and expression. Earlier overexpression cross-rescue precludes absolute nonexchangeability.
    Shared XMAP215 membership does not add Dis1 as a TACC partner.
  evidence_ids:
  - tacc-prep-dis1_2019-jats
  - tacc-prep-IPR045110
  - record
- assessment_id: species
  area: scope
  topic: Experimental species, reference strain and expression host
  outcome: supported
  target_ids:
  - GO:0070850
  summary: The curated mechanism concerns S.pombe, while the protein entries are reference-strain
    exemplars. Sf9 expression, bacterial purification, budding-yeast two-hybrid and
    pig-brain tubulin do not establish native complex distribution in those organisms.
    Generic GO conservation is kept distinct from demonstrated prevalence.
  evidence_ids:
  - tacc-prep-tax-4896
  - tacc-prep-tax-284812
  - tacc-prep-hussmann2016-jats
  - tacc-prep-transport2014-jats
  - tacc-prep-go
  - record
- assessment_id: image
  area: provenance
  topic: Unchanged reconstitution figure and accurate panel meaning
  outcome: supported
  target_ids:
  - GO:0070850
  summary: The tracked image is byte-identical to the licensed native source. The
    paraphrased caption correctly describes mixed-species assay ingredients, focal
    S.pombe proteins, kymograph scales and growth histograms. It neither presents
    a whole-cell micrograph nor equates panelD with catastrophe-frequency data.
  evidence_ids:
  - tacc-prep-figure7
  - tacc-prep-hussmann2016-jats
  - record
- assessment_id: completeness
  area: completeness
  topic: Explicit scientific gaps and optional enrichment
  outcome: supported
  target_ids:
  - GO:0070850
  summary: Native stoichiometry, interface, exact TACC whole-protein family, cause
    of the elongation discrepancy and broader microbial examples remain explicit gaps.
    No exact missing required assertion or contradiction was established; no stronger
    mechanism is supplied by inference.
  evidence_ids:
  - tacc-prep-hussmann2016-jats
  - tacc-prep-nucleation2018-jats
  - tacc-prep-attachment2013-jats
  - tacc-prep-transport2014-jats
  - tacc-prep-dis1_2019-jats
  - tacc-prep-matches-Q9URY2
  - record
findings: []
actions: []
limitations:
- The2016 and2018 Alp7 deletion effects on elongation differ; strain or assay context
  is a proposed explanation, not a demonstrated resolution.
- Purified association does not determine universal native stoichiometry, assembly
  order or interface. Constituent assembly essentiality remains UNKNOWN.
- Forced targeting, truncations, reporter export and two-hybrid fragments are engineered
  assays; they do not establish complete native recruitment or transport interfaces.
- Native TACC matching is bounded to Q9URY2 and its complete current InterPro response.
  It does not establish absence of homologs or of a suitable family elsewhere.
- The five primary claim-bearing main-text Results, Discussion and Methods were read.
  Supplementary files/movies and raw datasets were not independently audited; main-text
  descriptions of those experiments are not represented as direct supplementary-data
  inspection.
- Only Figure7 was visually inspected. Other relevant figure captions were read with
  the main text; numerical results were not independently recomputed from images or
  raw data.
- The species exemplar and reference sequence taxon are distinct from the engineered
  experimental stocks and heterologous assay ingredients. Broader occurrence and universal
  transport mechanisms are not established.
- Alp14 and Dis1 nonexchangeability is limited to the tested endogenous-expression
  targeting experiments, including the Alp14-NLS construct in Table1; prior overexpression
  cross-rescue remains relevant.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- No scientific record, tracked image or generated page is edited. Private primary-source
  bytes are not included in the review bundle.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
