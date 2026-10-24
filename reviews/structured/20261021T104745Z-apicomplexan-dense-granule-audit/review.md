# Apicomplexan dense granule identity, cargo and secretion review

- Review: 20261021T104745Z-apicomplexan-dense-granule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:27:13Z
- Finished UTC: 2026-10-21T10:47:45Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Dense-granule identity, heterogeneous cargo, model-specific secretion/permeability and the granule-versus-PVM boundary are supported. No corrective issue was established; source-access and formation-necessity limits remain explicit.

## Scope And Provenance

Entire single target and membrane neighbor; native ontology/taxon/protein/family identities; explicit primary and review-tier text scopes; no maintained image.

Selection: Eighth selected target in batch twenty, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0020026 | data/structures/membrane_organelle/apicomplexan_dense_granule.yaml | maintained | apicomplexan dense granule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native UniProt verify | passed | False | GO:0020026 | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | GO:0020026 | Native command passed; scientific membership and graph scope assessed independently. |
| Focused native schema | passed | True | GO:0020026 | Focused validator passed. |
| Focused native strict | passed | True | GO:0020026 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0020026 | 17 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0020026 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0020026 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0020026 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0020026 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0020026 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0020026 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Secretory organelle and membrane boundary

identity: supported. Targets: GO:0020026.

Exact GO identity, RELATED synonym and secretory-granule hierarchy are supported. The whole granule is kept separate from its membrane, lumen and the host-parasite vacuole membrane where secreted cargo later acts.

### Heterogeneous cargo and concrete examples

grounding: supported. Targets: GO:0020026.

The membrane and heterogeneous cargo cohorts are supported without a universal protein inventory. Specific Gra2/Gra6 families cannot ground the entire cargo or exported-effector cohort. GRA17/GRA23 functional relatedness is established, but the inspected exact-protein matches did not establish an exact family for the maintained pair. Native protein identity, the reviewed-query counts and the explicit ME49 GRA23 table bridge support the examples independently of membership.

### Unresolved individual assembly requirements

evidence: unknown. Targets: GO:0020026.

A lipid boundary constitutes this membrane-bounded organelle; the ESSENTIAL membrane row is collective material. None of the named GRA species is thereby proven necessary for formation of a dense granule. PVM permeability, parasite growth and cargo secretion phenotypes do not establish granule-assembly necessity; individual cargo entries correctly remain UNKNOWN.

### Taxonomy and model-system boundaries

scope: supported. Targets: GO:0020026.

The native taxonomy entries attest their own ranks and identities. Mercier2005 supplies review-tier cross-apicomplexan context for qualitative COMMON and specialized eukaryotic RARE wording; it is not a prevalence measurement. Toxoplasma experiments and ME49 reference identity remain distinct from a universal apicomplexan GRA inventory.

### Secretion, permeability and host-cell effects

evidence: supported. Targets: GO:0020026.

After-invasion secretion is supported and is not phrased as exclusive of extracellular secretion. Gold2015 supports the paired permeability function with unequal single-deletion phenotypes. The native Bougdour2013 abstract explicitly supports GRA16 nuclear export and host-gene effects; Masatani2013 abstract supports GRA23 dense-granule/PVM/IVN localization. Full bodies of those two studies were unavailable.

### Cargo release and later PVM activity

graph: supported. Targets: GO:0020026.

The graph represents cargo release, delivery/localization and an experimentally tested permeability consequence, in addition to boundary topology. It distinguishes granule membrane from PVM, does not identify a pore stoichiometry, and does not imply GRA17/GRA23 are required to build the secretory organelle.

### Bounded clean review

completeness: supported. Targets: GO:0020026.

No corrective issue was established. Optional GRA17 concrete examples, a complete granule proteome and universal molecular lipid inventory are not mandatory fields. Family searches remain bounded and no absence claim is inferred from an empty native endpoint. The mapping state and historical discussions remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/apicomplexan_dense_granule.yaml; Entire maintained YAML including definition, components, functions, hierarchy, examples, graph edges, discussions, image metadata and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| granule-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020026,GO:0030141,GO:0030668; Complete GO0020026, GO0030141 and GO0030668 definitions, synonyms and relevant relations | supports | Native GO confirms the secretory dense-granule definition, RELATED dense body synonym, secretory-granule parent and distinct bounding-membrane part. |
| granule-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Eukaryota, domain. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| granule-agent-tax-5794 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Apicomplexa, phylum. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| granule-agent-tax-5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Toxoplasma gondii, species. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| granule-agent-tax-508771 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/508771; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Toxoplasma gondii ME49, strain. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| granule-agent-P13403 | https://rest.uniprot.org/uniprotkb/P13403.json; primaryAccession, entryType, proteinDescription, genes, organism; relevant location/function comments, sequence references and cross-references | supports | Native UniProtKB reviewed (Swiss-Prot) P13403: Dense granule protein 1; taxon 5811; gene fields [{"geneName": {"value": "GRA1"}}]. Accession identity and predicted location annotations do not by themselves prove membership in the maintained structure. |
| granule-agent-P13404 | https://rest.uniprot.org/uniprotkb/P13404.json; primaryAccession, entryType, proteinDescription, genes, organism; relevant location/function comments, sequence references and cross-references | supports | Native UniProtKB reviewed (Swiss-Prot) P13404: Dense granule protein 2; taxon 5811; gene fields [{"geneName": {"value": "GRA2"}}]. Accession identity and predicted location annotations do not by themselves prove membership in the maintained structure. |
| granule-agent-Q27003 | https://rest.uniprot.org/uniprotkb/Q27003.json; primaryAccession, entryType, proteinDescription, genes, organism; relevant location/function comments, sequence references and cross-references | supports | Native UniProtKB reviewed (Swiss-Prot) Q27003: Dense granule protein 6; taxon 5811; gene fields [{"geneName": {"value": "GRA6"}, "synonyms": [{"value": "TG24"}]}]. Accession identity and predicted location annotations do not by themselves prove membership in the maintained structure. |
| granule-agent-A0A125YME4 | https://rest.uniprot.org/uniprotkb/A0A125YME4.json; primaryAccession, entryType, proteinDescription, genes, organism; relevant location/function comments, sequence references and cross-references | supports | Native UniProtKB unreviewed (TrEMBL) A0A125YME4: Dense granule protein DG32; taxon 508771; gene fields [{"orfNames": [{"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "EPT32203.1"}], "value": "TGME49_297880"}]}]. Accession identity and predicted location annotations do not by themselves prove membership in the maintained structure. |
| granule-agent-reviewed-GRA1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AGRA1%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29; Complete returned results for the exact query URL | context_only | Exactly one reviewed entry is returned for this exact gene and species query: P13403. |
| granule-agent-reviewed-GRA2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AGRA2%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29; Complete returned results for the exact query URL | context_only | Exactly one reviewed entry is returned for this exact gene and species query: P13404. |
| granule-agent-reviewed-GRA6 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AGRA6%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29; Complete returned results for the exact query URL | context_only | Exactly one reviewed entry is returned for this exact gene and species query: Q27003. |
| granule-agent-query-TGME49_297880-508771 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ATGME49_297880%29%20AND%20%28organism_id%3A508771%29; Complete returned results for the exact query URL | context_only | The exact ME49 locus query returns A0A125YME4; the native field is an ORF name, not a literal GRA23 gene-name synonym. |
| granule-agent-matches-P13404 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P13404/?page_size=200; All results; next is null | context_only | Complete integrated matches were inspected; these individual-family matches do not identify the aggregate GRA cargo or exported-effector cohort. |
| granule-agent-matches-Q27003 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q27003/?page_size=200; All results; next is null | context_only | Complete integrated matches were inspected; these individual-family matches do not identify the aggregate GRA cargo or exported-effector cohort. |
| granule-agent-matches-P13403 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P13403/?page_size=200; Actual response body and retrieval receipt | context_only | Native InterPro exact-protein endpoint returned HTTP204 with an empty body. This bounds this endpoint response, not an exhaustive absence of a family. |
| granule-agent-matches-A0A125YME4 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/A0A125YME4/?page_size=200; Actual response body and retrieval receipt | context_only | Native InterPro exact-protein endpoint returned HTTP204 with an empty body. This bounds this endpoint response, not an exhaustive absence of a family. |
| granule-agent-IPR008118 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008118/; Native InterPro metadata name/type, description and membership scope; predictive description provenance retained where marked | supports | Gra2 protein is a specific family, not an exact grounding for the whole dense-granule cargo cohort. |
| granule-agent-IPR008119 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008119/; Native InterPro metadata name/type, description and membership scope; predictive description provenance retained where marked | supports | Dense granule protein6/2 is a family entry for a subset of cargo, not the unrelated full GRA or exported-effector cohort. |
| granule-agent-doi-10.1111_jeu.12904 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/jeu.12904; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Dense granule biogenesis, secretion, and function in Toxoplasma gondii. Authors: Griffith MB, Pearce CS, Heaslip AT.; PMID 35302693; DOI 10.1111/jeu.12904. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| granule-agent-doi-10.1016_j.pt.2014.12.002 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.pt.2014.12.002; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Toxoplasma secretory granules: one population or more? Authors: Mercier C, Cesbron-Delauw MF.; PMID 25599584; DOI 10.1016/j.pt.2014.12.002. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| granule-agent-doi-10.1016_j.ijpara.2005.03.011 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.ijpara.2005.03.011; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Dense granules: are they key organelles to help understand the parasitophorous vacuole of all apicomplexa parasites? Authors: Mercier C, Adjogble KD, Däubener W, Delauw MF.; PMID 15978597; DOI 10.1016/j.ijpara.2005.03.011. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| granule-agent-doi-10.1016_j.chom.2015.04.003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.chom.2015.04.003; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The Toxoplasma Dense Granule Proteins GRA17 and GRA23 Mediate the Movement of Small Molecules between the Host and the Parasitophorous Vacuole. Authors: Gold DA, Kaplan AD, Lis A, Bett GC, Rosowski EE, Cirelli KM, Bougdour A, Sidik SM, Beck JR, Lourido S, Egea PF, Bradley PJ, Hakimi MA, Rasmusson RL, Saeij JP.; PMID 25974303; DOI 10.1016/j.chom.2015.04.003. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| granule-agent-doi-10.1016_j.parint.2013.04.003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.parint.2013.04.003; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies TgGRA23, a novel Toxoplasma gondii dense granule protein associated with the parasitophorous vacuole membrane and intravacuolar network. Authors: Masatani T, Matsuo T, Tanaka T, Terkawi MA, Lee EG, Goo YK, Aboge GO, Yamagishi J, Hayashi K, Kameyama K, Cao S, Nishikawa Y, Xuan X.; PMID 23583316; DOI 10.1016/j.parint.2013.04.003. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| granule-agent-doi-10.1016_j.chom.2013.03.002 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.chom.2013.03.002; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Host cell subversion by Toxoplasma GRA16, an exported dense granule protein that targets the host cell nucleus and alters gene expression. Authors: Bougdour A, Durandau E, Brenier-Pinchart MP, Ortet P, Barakat M, Kieffer S, Curt-Varesano A, Curt-Bertini RL, Bastien O, Coute Y, Pelloux H, Hakimi MA.; PMID 23601110; DOI 10.1016/j.chom.2013.03.002. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| granule-agent-pmid-9208224 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9208224%20AND%20SRC%3AMED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Sequential protein secretion from three distinct organelles of Toxoplasma gondii accompanies invasion of human fibroblasts. Authors: Carruthers VB, Sibley LD.; PMID 9208224; DOI None. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| granule-agent-jats-PMC9482668 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9482668.1/PMC9482668.1.xml; Introduction paragraphs1-3; S2 cargo processing, S3 granule formation, S4 transport, S5-S7 secretion, S8 function opening, S10 intravacuolar network, S13 diffusion, S18 exported effectors, S20-S21 cell cycle; no comprehensive audit of remaining sections or supplementary tables. | supports | Griffith2022 is review-tier synthesis. It describes membrane-enclosed dense granules, cargo processing/aggregation, post-Golgi biogenesis, secretion and later cargo functions. Stored transmembrane cargo is distinguished from resident granule-membrane proteins. It does not supply a universal lipid species list or establish every GRA as necessary for granule formation. |
| granule-agent-mercier2005-search | https://www.sciencedirect.com/science/article/abs/pii/S0020751905001414; Publisher abstract, Introduction and discontinuous opening of Dense-granule biogenesis; indexed body extract only, with status null rather than a native HTTP200 claim. | supports | This review-tier indexed publisher extract describes dense bodies/dense granules across invasive apicomplexan stages, their bounding membrane, and taxon-specific variation. It supports qualitative broad occurrence, not a measured prevalence across all Apicomplexa. Native full publisher body was not obtained. |
| granule-agent-jats-PMC4435723 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4435723.1/PMC4435723.1.xml; Entire Introduction, Results S3-S8 and Discussion S9; Methods S12 parasite culture, S14 microscopy, S15 fractionation, S16 dye assays, S18 oocyte electrophysiology; complete Table1 identifiers. Figure pixels and other supplementary data were not independently audited. | supports | Gold2015 directly identifies GRA17/GRA23, localizes them to dense granules/PVM and tests small-solute permeability and heterologous conductance. The GRA17 deletion has a strong permeability phenotype; GRA23 deletion alone resembles wild type in that assay but combined/genetic and overexpression evidence supports overlap. The proposed pore architecture and multimerization remain unresolved; the record does not assert a measured stoichiometry. |
| granule-agent-pmc-PMC13475723 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13475723/; Materials and methods S3; Results S15-S18, including Figures5-7 captions; complete Discussion S19 and Figure8 caption. Remaining methods/results and image pixels were not comprehensively audited. | supports | Carruthers/Sibley1997 directly measures GRA1/NTPase release after a synchronized invasion pulse. Release follows rhoptry secretion, rises after invasion, and GRA1 is also secreted extracellularly. The article distinguishes soluble cargo from cargo later associated with PV membranes; it does not make every GRA a resident granule-membrane protein. |
| granule-agent-jats-PMC7202600 | https://pmc-oa-opendata.s3.amazonaws.com/PMC7202600.1/PMC7202600.1.xml; Complete Table1 identity rows, specifically TGME49_297880 / GRA23, and article bibliographic identity only | supports | This additional primary source explicitly pairs TGME49_297880 with GRA23 in its protein-identification table. Together with native UniProt/NCBI locus identity this resolves the ME49 example without assuming that the Gold paper TGGT1 locus prefix is identical to TGME49. No other claim from this study is adopted. |
| granule-agent-gene-7901472 | https://api.ncbi.nlm.nih.gov/datasets/v2/gene/id/7901472; Complete gene identity, locus_tag, organism and annotation fields | supports | NCBI Gene7901472 identifies the ME49 locus TGME49_297880 as dense granule protein DG32, taxon508771. This is the native locus bridge, not independent functional evidence. |
| boundary-0 | data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | These maintained fields were read to verify the stated identity boundary. This is contextual corpus evidence, not an independent full scientific review of the neighboring record. |
| native-verify | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml --causal-graphs; Captured focused native causal-graphs log | supports | data/structures/membrane_organelle/apicomplexan_dense_granule.yaml  (GO:0020026)<br>  dense_granule_cargo_pvm_permeability	dense_granule_proteins	COVERED	-&gt;dense_granule_proteins (UniProtKB:P13403, UniProtKB:P13404, UniProtKB:Q27003)<br>  dense_granule_cargo_pvm_permeability	gra17_gra23_permeability_factors	PARTIAL_EXAMPLES	-&gt;gra17_gra23_permeability_factors (have: UniProtKB:A0A125YME4; missing: GRA17)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/apicomplexan_dense_granule.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/apicomplexan_dense_granule.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/apicomplexan_dense_granule.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/apicomplexan_dense_granule.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/apicomplexan_dense_granule.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 17 of18 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:9208224: UNREACHABLE; resolved by evidence granule-agent-pmid-9208224. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Mercier2005 was read through native metadata/abstract and indexed publisher Introduction/biogenesis excerpts, not a complete public body. COMMON/RARE is treated as qualitative source scope, not measured prevalence.
- Mercier/Cesbron-Delauw2015 review, Bougdour2013 and Masatani2013 are native metadata/abstract only; publisher responses were redirects/blocked content rather than complete papers. Their narrow abstract-supported claims are distinguished from the fully inspected Gold2015 body.
- Griffith2022 and Carruthers/Sibley1997 were inspected only at the explicit sections above. Gold2015 supplementary files and image pixels were not independently audited. The additional2020 primary table was used only for the exact ME49 GRA23 identity bridge.
- GRA23 is a source-supported alias of the native ME49 locus; UniProt itself displays an ORF identifier and DG32 protein name. Empty exact InterPro responses do not establish exhaustive family absence. Observed functional requirements do not establish universal dense-granule assembly necessity.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104745Z-apicomplexan-dense-granule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Apicomplexan dense granule identity, cargo and secretion review
started_at: '2026-10-21T10:27:13Z'
finished_at: '2026-10-21T10:47:45Z'
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
summary: Dense-granule identity, heterogeneous cargo, model-specific secretion/permeability
  and the granule-versus-PVM boundary are supported. No corrective issue was established;
  source-access and formation-necessity limits remain explicit.
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
  - path: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    sha256: 49d7347778d1dd9a80bf5ab53049d35eeefad4aee5581cb2c493dab7bb1c0bb2
    role: target
  - path: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    sha256: bd48fa3c1773cf7be7066602608acdd61ba386a9fbc5fc3fd19ddaa25dcab51b
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
- target_id: GO:0020026
  path: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
  label: apicomplexan dense granule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    role: maintained scientific record
scope:
  description: Entire single target and membrane neighbor; native ontology/taxon/protein/family
    identities; explicit primary and review-tier text scopes; no maintained image.
  selection: Eighth selected target in batch twenty, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0020026
checks:
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - GO:0020026
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    --verify
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native UniProt causal-graphs
  status: passed
  required: false
  target_ids:
  - GO:0020026
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    --causal-graphs
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0020026
  command: just validate data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0020026
  command: just validate-strict data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0020026
  summary: 17 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - granule-agent-pmid-9208224
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0020026
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - granule-agent-go
  - granule-agent-tax-2759
  - granule-agent-tax-5794
  - granule-agent-tax-5811
  - granule-agent-tax-508771
  - granule-agent-P13403
  - granule-agent-P13404
  - granule-agent-Q27003
  - granule-agent-A0A125YME4
  - granule-agent-reviewed-GRA1
  - granule-agent-reviewed-GRA2
  - granule-agent-reviewed-GRA6
  - granule-agent-query-TGME49_297880-508771
  - granule-agent-matches-P13404
  - granule-agent-matches-Q27003
  - granule-agent-matches-P13403
  - granule-agent-matches-A0A125YME4
  - granule-agent-IPR008118
  - granule-agent-IPR008119
  - granule-agent-doi-10.1111_jeu.12904
  - granule-agent-doi-10.1016_j.pt.2014.12.002
  - granule-agent-doi-10.1016_j.ijpara.2005.03.011
  - granule-agent-doi-10.1016_j.chom.2015.04.003
  - granule-agent-doi-10.1016_j.parint.2013.04.003
  - granule-agent-doi-10.1016_j.chom.2013.03.002
  - granule-agent-pmid-9208224
  - granule-agent-jats-PMC9482668
  - granule-agent-mercier2005-search
  - granule-agent-jats-PMC4435723
  - granule-agent-pmc-PMC13475723
  - granule-agent-jats-PMC7202600
  - granule-agent-gene-7901472
  - boundary-0
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0020026
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
  - GO:0020026
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
  - GO:0020026
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
  - GO:0020026
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
  - GO:0020026
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
  reference: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
  locator: Entire maintained YAML including definition, components, functions, hierarchy,
    examples, graph edges, discussions, image metadata and history
  accessed_at: '2026-10-21T10:45:59Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T10:45:59Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: granule-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020026,GO:0030141,GO:0030668
  locator: Complete GO0020026, GO0030141 and GO0030668 definitions, synonyms and relevant
    relations
  accessed_at: '2026-10-21T10:32:30.183554Z'
  support: supports
  summary: Native GO confirms the secretory dense-granule definition, RELATED dense
    body synonym, secretory-granule parent and distinct bounding-membrane part.
  snapshot_sha256: 695903e78d25a97c58e5261f3429538fd447ddb63c8855a77475aa24a0d0e2e6
- evidence_id: granule-agent-tax-2759
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:32:30.183821Z'
  support: supports
  summary: Native ENA taxonomy identifies Eukaryota, domain. This receipt attests
    that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: granule-agent-tax-5794
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:32:30.183972Z'
  support: supports
  summary: Native ENA taxonomy identifies Apicomplexa, phylum. This receipt attests
    that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: 71f50f7adf0b7ad8670573c6c6ac0e6df37a9cf467fdec2ab20d612db477bc53
- evidence_id: granule-agent-tax-5811
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:32:30.184046Z'
  support: supports
  summary: Native ENA taxonomy identifies Toxoplasma gondii, species. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: 11679825fa4d00b18d5848862450ab6b3770aaa47ad6676d1196d9df61124b16
- evidence_id: granule-agent-tax-508771
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/508771
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:32:30.183895Z'
  support: supports
  summary: Native ENA taxonomy identifies Toxoplasma gondii ME49, strain. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: d1622dee69e1fe2abfea4351893585852f4200cfff6eac3b42e5a014283cd0b0
- evidence_id: granule-agent-P13403
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P13403.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; relevant
    location/function comments, sequence references and cross-references
  accessed_at: '2026-10-21T10:32:31.046113Z'
  support: supports
  summary: 'Native UniProtKB reviewed (Swiss-Prot) P13403: Dense granule protein 1;
    taxon 5811; gene fields [{"geneName": {"value": "GRA1"}}]. Accession identity
    and predicted location annotations do not by themselves prove membership in the
    maintained structure.'
  snapshot_sha256: 013fde27eadf7408ef9d4164b73b9b9f983364f784b16d9546996d6314517d56
- evidence_id: granule-agent-P13404
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P13404.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; relevant
    location/function comments, sequence references and cross-references
  accessed_at: '2026-10-21T10:32:31.062026Z'
  support: supports
  summary: 'Native UniProtKB reviewed (Swiss-Prot) P13404: Dense granule protein 2;
    taxon 5811; gene fields [{"geneName": {"value": "GRA2"}}]. Accession identity
    and predicted location annotations do not by themselves prove membership in the
    maintained structure.'
  snapshot_sha256: 8cb1d2d1b3a875fa86b5272522e5caee8050f737919eb05ab83b1fddd56f1fd3
- evidence_id: granule-agent-Q27003
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q27003.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; relevant
    location/function comments, sequence references and cross-references
  accessed_at: '2026-10-21T10:32:31.680391Z'
  support: supports
  summary: 'Native UniProtKB reviewed (Swiss-Prot) Q27003: Dense granule protein 6;
    taxon 5811; gene fields [{"geneName": {"value": "GRA6"}, "synonyms": [{"value":
    "TG24"}]}]. Accession identity and predicted location annotations do not by themselves
    prove membership in the maintained structure.'
  snapshot_sha256: 3ddafda8d3e05dcf6d5e658b1ee69409dcef54e7f55b2717d7c33d60a0abf8ca
- evidence_id: granule-agent-A0A125YME4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A125YME4.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; relevant
    location/function comments, sequence references and cross-references
  accessed_at: '2026-10-21T10:32:31.016445Z'
  support: supports
  summary: 'Native UniProtKB unreviewed (TrEMBL) A0A125YME4: Dense granule protein
    DG32; taxon 508771; gene fields [{"orfNames": [{"evidences": [{"evidenceCode":
    "ECO:0000313", "source": "EMBL", "id": "EPT32203.1"}], "value": "TGME49_297880"}]}].
    Accession identity and predicted location annotations do not by themselves prove
    membership in the maintained structure.'
  snapshot_sha256: 3d8f8e9505305e626813fb812d5c3ff040591ae3570a2fd6c4653bf90f4428d2
- evidence_id: granule-agent-reviewed-GRA1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AGRA1%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned results for the exact query URL
  accessed_at: '2026-10-21T10:41:03.282185Z'
  support: context_only
  summary: 'Exactly one reviewed entry is returned for this exact gene and species
    query: P13403.'
  snapshot_sha256: a3eef02bb01acdcb3793b00e9830cd33ff247b1f92d0612218157a7dac3686e8
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AGRA1%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29;
    only this exact gene/taxon/filter scope, not exhaustive synonym or family absence.
- evidence_id: granule-agent-reviewed-GRA2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AGRA2%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned results for the exact query URL
  accessed_at: '2026-10-21T10:41:03.282554Z'
  support: context_only
  summary: 'Exactly one reviewed entry is returned for this exact gene and species
    query: P13404.'
  snapshot_sha256: e8f942d01bfe7048d28a2ac5ca31cd58be6b31ec16c751e0cb5d5a14cdb8380f
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AGRA2%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29;
    only this exact gene/taxon/filter scope, not exhaustive synonym or family absence.
- evidence_id: granule-agent-reviewed-GRA6
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AGRA6%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned results for the exact query URL
  accessed_at: '2026-10-21T10:41:03.282668Z'
  support: context_only
  summary: 'Exactly one reviewed entry is returned for this exact gene and species
    query: Q27003.'
  snapshot_sha256: 9fe8e36d180cbd8365b3899c3337b876c71f0e31909035172ee28d02b8e9158f
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AGRA6%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29;
    only this exact gene/taxon/filter scope, not exhaustive synonym or family absence.
- evidence_id: granule-agent-query-TGME49_297880-508771
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ATGME49_297880%29%20AND%20%28organism_id%3A508771%29
  locator: Complete returned results for the exact query URL
  accessed_at: '2026-10-21T10:34:53.075818Z'
  support: context_only
  summary: The exact ME49 locus query returns A0A125YME4; the native field is an ORF
    name, not a literal GRA23 gene-name synonym.
  snapshot_sha256: b6ab1b85e3a20f328a58caf63f55f275f42563e57f73533cc3484ba0e69584aa
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ATGME49_297880%29%20AND%20%28organism_id%3A508771%29;
    only this exact gene/taxon/filter scope, not exhaustive synonym or family absence.
- evidence_id: granule-agent-matches-P13404
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P13404/?page_size=200
  locator: All results; next is null
  accessed_at: '2026-10-21T10:32:31.630134Z'
  support: context_only
  summary: Complete integrated matches were inspected; these individual-family matches
    do not identify the aggregate GRA cargo or exported-effector cohort.
  snapshot_sha256: 9aebb3e387072f6dd110eb330e5ddfc3fabb5773ae1e483d76ff643bdada3b55
- evidence_id: granule-agent-matches-Q27003
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q27003/?page_size=200
  locator: All results; next is null
  accessed_at: '2026-10-21T10:32:31.714871Z'
  support: context_only
  summary: Complete integrated matches were inspected; these individual-family matches
    do not identify the aggregate GRA cargo or exported-effector cohort.
  snapshot_sha256: 523e3999008513c979d787768d1ed295135662690d308959c8acc3ecfdeabe18
- evidence_id: granule-agent-matches-P13403
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P13403/?page_size=200
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:32:31.061192Z'
  support: context_only
  summary: Native InterPro exact-protein endpoint returned HTTP204 with an empty body.
    This bounds this endpoint response, not an exhaustive absence of a family.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P13403/?page_size=200
- evidence_id: granule-agent-matches-A0A125YME4
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/A0A125YME4/?page_size=200
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:32:31.038028Z'
  support: context_only
  summary: Native InterPro exact-protein endpoint returned HTTP204 with an empty body.
    This bounds this endpoint response, not an exhaustive absence of a family.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/A0A125YME4/?page_size=200
- evidence_id: granule-agent-IPR008118
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008118/
  locator: Native InterPro metadata name/type, description and membership scope; predictive
    description provenance retained where marked
  accessed_at: '2026-10-21T10:33:08.730829Z'
  support: supports
  summary: Gra2 protein is a specific family, not an exact grounding for the whole
    dense-granule cargo cohort.
  snapshot_sha256: e6e63144405f10b9cc7313f0fdc4806301bf642d16e8e3391a9919b3da1be685
- evidence_id: granule-agent-IPR008119
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008119/
  locator: Native InterPro metadata name/type, description and membership scope; predictive
    description provenance retained where marked
  accessed_at: '2026-10-21T10:33:08.731815Z'
  support: supports
  summary: Dense granule protein6/2 is a family entry for a subset of cargo, not the
    unrelated full GRA or exported-effector cohort.
  snapshot_sha256: 2ddf4eaa83d6dc7a9d0de341b9299784a55e841fd0b966aea5d526077d41ed02
- evidence_id: granule-agent-doi-10.1111_jeu.12904
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/jeu.12904
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:32:32.935707Z'
  support: supports
  summary: 'Native metadata identifies Dense granule biogenesis, secretion, and function
    in Toxoplasma gondii. Authors: Griffith MB, Pearce CS, Heaslip AT.; PMID 35302693;
    DOI 10.1111/jeu.12904. Bibliographic identity and available abstract only; not
    a substitute for inspected article body.'
  snapshot_sha256: deab13eca62c55b1cdbdff5590b100d2be74786a62b86faca60ae5aefcb396c6
- evidence_id: granule-agent-doi-10.1016_j.pt.2014.12.002
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.pt.2014.12.002
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:32:32.670115Z'
  support: supports
  summary: 'Native metadata identifies Toxoplasma secretory granules: one population
    or more? Authors: Mercier C, Cesbron-Delauw MF.; PMID 25599584; DOI 10.1016/j.pt.2014.12.002.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: a768f5d3f4d5b32b154174ab3e2d869dc81bb19fcc12ef39431645696ee626de
- evidence_id: granule-agent-doi-10.1016_j.ijpara.2005.03.011
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.ijpara.2005.03.011
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:32:32.284076Z'
  support: supports
  summary: 'Native metadata identifies Dense granules: are they key organelles to
    help understand the parasitophorous vacuole of all apicomplexa parasites? Authors:
    Mercier C, Adjogble KD, Däubener W, Delauw MF.; PMID 15978597; DOI 10.1016/j.ijpara.2005.03.011.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 676306a8292b4688db4432a0bf7274977650407a19d0812ebe6be47b78d1718a
- evidence_id: granule-agent-doi-10.1016_j.chom.2015.04.003
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.chom.2015.04.003
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:32:31.860160Z'
  support: supports
  summary: 'Native metadata identifies The Toxoplasma Dense Granule Proteins GRA17
    and GRA23 Mediate the Movement of Small Molecules between the Host and the Parasitophorous
    Vacuole. Authors: Gold DA, Kaplan AD, Lis A, Bett GC, Rosowski EE, Cirelli KM,
    Bougdour A, Sidik SM, Beck JR, Lourido S, Egea PF, Bradley PJ, Hakimi MA, Rasmusson
    RL, Saeij JP.; PMID 25974303; DOI 10.1016/j.chom.2015.04.003. Bibliographic identity
    and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 119701b55cf51ac3b94abaf7c581534c55d26f7b6661f23af7e6e6b0ed1cd546
- evidence_id: granule-agent-doi-10.1016_j.parint.2013.04.003
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.parint.2013.04.003
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:32:32.541751Z'
  support: supports
  summary: 'Native metadata identifies TgGRA23, a novel Toxoplasma gondii dense granule
    protein associated with the parasitophorous vacuole membrane and intravacuolar
    network. Authors: Masatani T, Matsuo T, Tanaka T, Terkawi MA, Lee EG, Goo YK,
    Aboge GO, Yamagishi J, Hayashi K, Kameyama K, Cao S, Nishikawa Y, Xuan X.; PMID
    23583316; DOI 10.1016/j.parint.2013.04.003. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 567c406836a8b0a22c356a0b80ba01019afd35fe7a643443b18913c7758a14ab
- evidence_id: granule-agent-doi-10.1016_j.chom.2013.03.002
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.chom.2013.03.002
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:32:31.847728Z'
  support: supports
  summary: 'Native metadata identifies Host cell subversion by Toxoplasma GRA16, an
    exported dense granule protein that targets the host cell nucleus and alters gene
    expression. Authors: Bougdour A, Durandau E, Brenier-Pinchart MP, Ortet P, Barakat
    M, Kieffer S, Curt-Varesano A, Curt-Bertini RL, Bastien O, Coute Y, Pelloux H,
    Hakimi MA.; PMID 23601110; DOI 10.1016/j.chom.2013.03.002. Bibliographic identity
    and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 0c7fd65efbe716b72124b08e4fa7e583eeee576d6c72641190c5660d61347c34
- evidence_id: granule-agent-pmid-9208224
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9208224%20AND%20SRC%3AMED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:32:32.966852Z'
  support: supports
  summary: 'Native metadata identifies Sequential protein secretion from three distinct
    organelles of Toxoplasma gondii accompanies invasion of human fibroblasts. Authors:
    Carruthers VB, Sibley LD.; PMID 9208224; DOI None. Bibliographic identity and
    available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 6c65c0203fec06444aeeb999cf41ff2f22179f5f0de3a19f3542a8b55b49d7c0
- evidence_id: granule-agent-jats-PMC9482668
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9482668.1/PMC9482668.1.xml
  locator: Introduction paragraphs1-3; S2 cargo processing, S3 granule formation,
    S4 transport, S5-S7 secretion, S8 function opening, S10 intravacuolar network,
    S13 diffusion, S18 exported effectors, S20-S21 cell cycle; no comprehensive audit
    of remaining sections or supplementary tables.
  accessed_at: '2026-10-21T10:33:24.005355Z'
  support: supports
  summary: Griffith2022 is review-tier synthesis. It describes membrane-enclosed dense
    granules, cargo processing/aggregation, post-Golgi biogenesis, secretion and later
    cargo functions. Stored transmembrane cargo is distinguished from resident granule-membrane
    proteins. It does not supply a universal lipid species list or establish every
    GRA as necessary for granule formation.
  snapshot_sha256: c299f0194d8df4f3f95ed870283b1cc9212a3b8f7a39bfab4328c318d08a1b8c
- evidence_id: granule-agent-mercier2005-search
  kind: authority
  reference: https://www.sciencedirect.com/science/article/abs/pii/S0020751905001414
  locator: Publisher abstract, Introduction and discontinuous opening of Dense-granule
    biogenesis; indexed body extract only, with status null rather than a native HTTP200
    claim.
  accessed_at: '2026-10-21T10:35:00.260Z'
  support: supports
  summary: This review-tier indexed publisher extract describes dense bodies/dense
    granules across invasive apicomplexan stages, their bounding membrane, and taxon-specific
    variation. It supports qualitative broad occurrence, not a measured prevalence
    across all Apicomplexa. Native full publisher body was not obtained.
  snapshot_sha256: cc62d73c79c01ec94ed5baa90427143c95f4c1f88f7c96c147365807de86d565
- evidence_id: granule-agent-jats-PMC4435723
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4435723.1/PMC4435723.1.xml
  locator: Entire Introduction, Results S3-S8 and Discussion S9; Methods S12 parasite
    culture, S14 microscopy, S15 fractionation, S16 dye assays, S18 oocyte electrophysiology;
    complete Table1 identifiers. Figure pixels and other supplementary data were not
    independently audited.
  accessed_at: '2026-10-21T10:33:24.005690Z'
  support: supports
  summary: Gold2015 directly identifies GRA17/GRA23, localizes them to dense granules/PVM
    and tests small-solute permeability and heterologous conductance. The GRA17 deletion
    has a strong permeability phenotype; GRA23 deletion alone resembles wild type
    in that assay but combined/genetic and overexpression evidence supports overlap.
    The proposed pore architecture and multimerization remain unresolved; the record
    does not assert a measured stoichiometry.
  snapshot_sha256: e6f28f80777e2f2b3133f12e50371e7e9835d4ef70e2c409b7cb02ce88bda3d6
- evidence_id: granule-agent-pmc-PMC13475723
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13475723/
  locator: Materials and methods S3; Results S15-S18, including Figures5-7 captions;
    complete Discussion S19 and Figure8 caption. Remaining methods/results and image
    pixels were not comprehensively audited.
  accessed_at: '2026-10-21T10:37:51.425835Z'
  support: supports
  summary: Carruthers/Sibley1997 directly measures GRA1/NTPase release after a synchronized
    invasion pulse. Release follows rhoptry secretion, rises after invasion, and GRA1
    is also secreted extracellularly. The article distinguishes soluble cargo from
    cargo later associated with PV membranes; it does not make every GRA a resident
    granule-membrane protein.
  snapshot_sha256: ea24c272fe4e0707d956ec6cc25958f2e4a39896182e81d62d57515fcb9e7dff
- evidence_id: granule-agent-jats-PMC7202600
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7202600.1/PMC7202600.1.xml
  locator: Complete Table1 identity rows, specifically TGME49_297880 / GRA23, and
    article bibliographic identity only
  accessed_at: '2026-10-21T10:42:55.925983Z'
  support: supports
  summary: This additional primary source explicitly pairs TGME49_297880 with GRA23
    in its protein-identification table. Together with native UniProt/NCBI locus identity
    this resolves the ME49 example without assuming that the Gold paper TGGT1 locus
    prefix is identical to TGME49. No other claim from this study is adopted.
  snapshot_sha256: e6d90de8d0e521999bafd7a9252ffc16a6d8538e241e659aa2f8690306764ff4
- evidence_id: granule-agent-gene-7901472
  kind: database
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/gene/id/7901472
  locator: Complete gene identity, locus_tag, organism and annotation fields
  accessed_at: '2026-10-21T10:41:03.282860Z'
  support: supports
  summary: NCBI Gene7901472 identifies the ME49 locus TGME49_297880 as dense granule
    protein DG32, taxon508771. This is the native locus bridge, not independent functional
    evidence.
  snapshot_sha256: a1058c5ab71e61a5237d6f5a12d5357b54b90f98cb31b1e9f00851259583a57a
- evidence_id: boundary-0
  kind: record_content
  reference: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:45:59Z'
  support: context_only
  summary: These maintained fields were read to verify the stated identity boundary.
    This is contextual corpus evidence, not an independent full scientific review
    of the neighboring record.
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T10:32:34.485387Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T10:32:35.015692Z'
  support: supports
  summary: "data/structures/membrane_organelle/apicomplexan_dense_granule.yaml  (GO:0020026)\n\
    \  dense_granule_cargo_pvm_permeability\tdense_granule_proteins\tCOVERED\t->dense_granule_proteins\
    \ (UniProtKB:P13403, UniProtKB:P13404, UniProtKB:Q27003)\n  dense_granule_cargo_pvm_permeability\t\
    gra17_gra23_permeability_factors\tPARTIAL_EXAMPLES\t->gra17_gra23_permeability_factors\
    \ (have: UniProtKB:A0A125YME4; missing: GRA17)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     1  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     1  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: b6550992e3376ae84270b6ef2aaf55446130e50ab876322bc05aaaa64f9f5fe4
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:27:14Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/apicomplexan_dense_granule.yaml'
  snapshot_sha256: 7236ebc464a8c806f0121dd9a817959060053c6b3a1631925f233d180ac00a32
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:27:16Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/apicomplexan_dense_granule.yaml\
    \ --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/apicomplexan_dense_granule-strict.tsv"
  snapshot_sha256: a9e6b7918e57aa07f60be8aec28e8e0e9f845f2455ecc36f270b0ef36b91daba
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:45:59Z'
  support: supports
  summary: '17 of18 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:9208224: UNREACHABLE; resolved by evidence granule-agent-pmid-9208224.
    Source-native identity checked separately.'
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
  topic: Secretory organelle and membrane boundary
  outcome: supported
  target_ids:
  - GO:0020026
  summary: Exact GO identity, RELATED synonym and secretory-granule hierarchy are
    supported. The whole granule is kept separate from its membrane, lumen and the
    host-parasite vacuole membrane where secreted cargo later acts.
  evidence_ids:
  - granule-agent-go
  - boundary-0
  - granule-agent-jats-PMC9482668
  - granule-agent-jats-PMC4435723
  - granule-agent-pmc-PMC13475723
  - record
- assessment_id: composition
  area: grounding
  topic: Heterogeneous cargo and concrete examples
  outcome: supported
  target_ids:
  - GO:0020026
  summary: The membrane and heterogeneous cargo cohorts are supported without a universal
    protein inventory. Specific Gra2/Gra6 families cannot ground the entire cargo
    or exported-effector cohort. GRA17/GRA23 functional relatedness is established,
    but the inspected exact-protein matches did not establish an exact family for
    the maintained pair. Native protein identity, the reviewed-query counts and the
    explicit ME49 GRA23 table bridge support the examples independently of membership.
  evidence_ids:
  - granule-agent-P13403
  - granule-agent-P13404
  - granule-agent-Q27003
  - granule-agent-A0A125YME4
  - granule-agent-reviewed-GRA1
  - granule-agent-reviewed-GRA2
  - granule-agent-reviewed-GRA6
  - granule-agent-query-TGME49_297880-508771
  - granule-agent-matches-P13404
  - granule-agent-matches-Q27003
  - granule-agent-matches-P13403
  - granule-agent-matches-A0A125YME4
  - granule-agent-IPR008118
  - granule-agent-IPR008119
  - granule-agent-jats-PMC7202600
  - granule-agent-gene-7901472
  - granule-agent-jats-PMC4435723
  - granule-agent-jats-PMC9482668
  - record
- assessment_id: necessity
  area: evidence
  topic: Unresolved individual assembly requirements
  outcome: unknown
  target_ids:
  - GO:0020026
  summary: A lipid boundary constitutes this membrane-bounded organelle; the ESSENTIAL
    membrane row is collective material. None of the named GRA species is thereby
    proven necessary for formation of a dense granule. PVM permeability, parasite
    growth and cargo secretion phenotypes do not establish granule-assembly necessity;
    individual cargo entries correctly remain UNKNOWN.
  evidence_ids:
  - granule-agent-jats-PMC4435723
  - granule-agent-pmc-PMC13475723
  - granule-agent-jats-PMC9482668
  - record
  - policy
- assessment_id: scope
  area: scope
  topic: Taxonomy and model-system boundaries
  outcome: supported
  target_ids:
  - GO:0020026
  summary: The native taxonomy entries attest their own ranks and identities. Mercier2005
    supplies review-tier cross-apicomplexan context for qualitative COMMON and specialized
    eukaryotic RARE wording; it is not a prevalence measurement. Toxoplasma experiments
    and ME49 reference identity remain distinct from a universal apicomplexan GRA
    inventory.
  evidence_ids:
  - granule-agent-tax-2759
  - granule-agent-tax-5794
  - granule-agent-tax-5811
  - granule-agent-tax-508771
  - granule-agent-doi-10.1111_jeu.12904
  - granule-agent-doi-10.1016_j.pt.2014.12.002
  - granule-agent-doi-10.1016_j.ijpara.2005.03.011
  - granule-agent-doi-10.1016_j.chom.2015.04.003
  - granule-agent-doi-10.1016_j.parint.2013.04.003
  - granule-agent-doi-10.1016_j.chom.2013.03.002
  - granule-agent-pmid-9208224
  - granule-agent-mercier2005-search
  - granule-agent-jats-PMC4435723
  - granule-agent-pmc-PMC13475723
  - record
- assessment_id: functions
  area: evidence
  topic: Secretion, permeability and host-cell effects
  outcome: supported
  target_ids:
  - GO:0020026
  summary: After-invasion secretion is supported and is not phrased as exclusive of
    extracellular secretion. Gold2015 supports the paired permeability function with
    unequal single-deletion phenotypes. The native Bougdour2013 abstract explicitly
    supports GRA16 nuclear export and host-gene effects; Masatani2013 abstract supports
    GRA23 dense-granule/PVM/IVN localization. Full bodies of those two studies were
    unavailable.
  evidence_ids:
  - granule-agent-jats-PMC4435723
  - granule-agent-pmc-PMC13475723
  - granule-agent-jats-PMC9482668
  - granule-agent-doi-10.1111_jeu.12904
  - granule-agent-doi-10.1016_j.pt.2014.12.002
  - granule-agent-doi-10.1016_j.ijpara.2005.03.011
  - granule-agent-doi-10.1016_j.chom.2015.04.003
  - granule-agent-doi-10.1016_j.parint.2013.04.003
  - granule-agent-doi-10.1016_j.chom.2013.03.002
  - granule-agent-pmid-9208224
  - record
- assessment_id: graph
  area: graph
  topic: Cargo release and later PVM activity
  outcome: supported
  target_ids:
  - GO:0020026
  summary: The graph represents cargo release, delivery/localization and an experimentally
    tested permeability consequence, in addition to boundary topology. It distinguishes
    granule membrane from PVM, does not identify a pore stoichiometry, and does not
    imply GRA17/GRA23 are required to build the secretory organelle.
  evidence_ids:
  - granule-agent-jats-PMC4435723
  - granule-agent-pmc-PMC13475723
  - granule-agent-jats-PMC9482668
  - granule-agent-doi-10.1111_jeu.12904
  - granule-agent-doi-10.1016_j.pt.2014.12.002
  - granule-agent-doi-10.1016_j.ijpara.2005.03.011
  - granule-agent-doi-10.1016_j.chom.2015.04.003
  - granule-agent-doi-10.1016_j.parint.2013.04.003
  - granule-agent-doi-10.1016_j.chom.2013.03.002
  - granule-agent-pmid-9208224
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded clean review
  outcome: supported
  target_ids:
  - GO:0020026
  summary: No corrective issue was established. Optional GRA17 concrete examples,
    a complete granule proteome and universal molecular lipid inventory are not mandatory
    fields. Family searches remain bounded and no absence claim is inferred from an
    empty native endpoint. The mapping state and historical discussions remain unchanged.
  evidence_ids:
  - granule-agent-go
  - granule-agent-jats-PMC4435723
  - granule-agent-jats-PMC9482668
  - granule-agent-matches-P13404
  - granule-agent-matches-Q27003
  - granule-agent-matches-P13403
  - granule-agent-matches-A0A125YME4
  - granule-agent-IPR008118
  - granule-agent-IPR008119
  - record
  - policy
findings: []
actions: []
limitations:
- Mercier2005 was read through native metadata/abstract and indexed publisher Introduction/biogenesis
  excerpts, not a complete public body. COMMON/RARE is treated as qualitative source
  scope, not measured prevalence.
- Mercier/Cesbron-Delauw2015 review, Bougdour2013 and Masatani2013 are native metadata/abstract
  only; publisher responses were redirects/blocked content rather than complete papers.
  Their narrow abstract-supported claims are distinguished from the fully inspected
  Gold2015 body.
- Griffith2022 and Carruthers/Sibley1997 were inspected only at the explicit sections
  above. Gold2015 supplementary files and image pixels were not independently audited.
  The additional2020 primary table was used only for the exact ME49 GRA23 identity
  bridge.
- GRA23 is a source-supported alias of the native ME49 locus; UniProt itself displays
  an ORF identifier and DG32 protein name. Empty exact InterPro responses do not establish
  exhaustive family absence. Observed functional requirements do not establish universal
  dense-granule assembly necessity.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
