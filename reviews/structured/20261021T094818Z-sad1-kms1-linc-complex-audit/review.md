# Sad1–Kms1 LINC complex identity, species scope and mechanism review

- Review: 20261021T094818Z-sad1-kms1-linc-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:24:19Z
- Finished UTC: 2026-10-21T09:48:18Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact identity, native parent, four reviewed protein examples and bounded fission-yeast roles are supported. One major species/assembly scope transfer and one minor graph-scope issue require curation; assembly necessity and Kms2 context remain explicitly limited.

## Scope And Provenance

Full exact record, all declared native IDs, cited primary claim-bearing sections and additional native-GO-linked/meiotic primary context; no local neighbor dependency.

Selection: Batch16 index6; exact maintained record GO:1990612 at fresh-main base9c0446.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990612 | data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml | maintained | Sad1-Kms1 LINC complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990612 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990612 | Focused validator passed. |
| Native protein verify | passed | True | GO:1990612 | Native check passed; identity/graph coverage is distinct from scientific evidence support. |
| Native protein causal-graphs | passed | True | GO:1990612 | Native check passed; identity/graph coverage is distinct from scientific evidence support. |
| Expression-module source applicability | not_applicable | False | GO:1990612 | The record has protein identities and structural roles, all checked with native UniProt and primary sources. It has no expression-module assertion requiring iModulonDB. |
| Claim-level scientific review | passed | True | GO:1990612 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Target resolver slice with native transport-failure cross-checks | passed | True | GO:1990612 | 21 of 21 exact target identifiers returned OK. No target residuals. The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| Full corpus QC | passed | True | GO:1990612 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990612 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990612 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990612 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:1990612 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Named complex and exact native parent

identity: supported. Targets: GO:1990612.

GO1990612 exactly denotes Sad1–Kms1, and its DSB-repair opening is supported by native GO and Swartz2014. The GO0034993 parent relationship is explicitly is_a in the native graph. Meiotic roles are additional contexts, not evidence that DNA itself is a core subunit or that this named complex equals every fungal LINC system.

### Core constituents and conditional connector

representation: supported. Targets: GO:1990612.

Sad1 and Kms1 are the named envelope-spanning constituents; Bqt1/Bqt2 are appropriately ASSOCIATED_MACHINERY with meiotic context. Chikashige abstract, Amelina interaction assays, Moiseeva degradation and Yoshida localization support their bounded roles. Funaya2012 supplies cited background plus Hrs1 interaction evidence, not a standalone direct dynein-recruitment experiment.

### Assembly necessity distinct from viability and function

evidence: unknown. Targets: GO:1990612.

The inspected experiments establish identities, interactions, local recruitment and phenotypic effects. They do not provide a complete subunit-removal/reconstitution test of whether the named two-protein complex forms without each constituent. Retain this uncertainty when reading ESSENTIAL; neither Kms1 viability nor residual Sad1 foci establishes DISPENSABLE, and Bqt1-dependent bouquet loss is not destruction of every LINC assembly. The connector row’s CONDITIONAL value is likewise not verified as a requirement for assembly of the named core complex; bouquet attachment is a separate endpoint.

### Meiotic Kms2 recruitment versus DSB-associated complex

scope: unknown. Targets: GO:1990612.

The definition parenthetical and Kms2-related interpretations require context. Yoshida directly sees Kms2 at meiotic telocentrosomes; Funaya discusses possible Hrs1–Kms2 compensation. Swartz sees no Kms2 recruitment to MMS-induced foci but explicitly leaves redundancy possible. These observations do not prove a fixed three-subunit stoichiometry, nor global Kms2 absence; no absence finding is made.

### Four exact reference examples and SUN family

grounding: supported. Targets: GO:1990612.

All four reviewed accessions, native labels, gene symbols and taxon284812 match. IPR045119 is an appropriate SUN-family grounding and is cross-referenced by Q09825. The explicit reference-sequence roles avoid asserting that972h- was each experimental stock. Gene examples on all three protein graph nodes are inherited by valid component_ref; native verify and graph gates pass.

### Species and molecular subject of functional assays

scope: concern. Targets: GO:1990612.

The function description accurately names budding yeast, but the record and mediates edges still assign Fan Mps2/Csm4 assays to the Sad1–Kms1 subject. Fan assays are SK1/S288C Mps2–Mps3–Csm4 experiments. Moiseeva/Yoshida support fission-yeast bouquet roles separately. Retain the comparative account as comparison, or replace assigned claims with appropriate S. pombe evidence and conditions.

### Named assembly versus conserved LINC principle

scope: concern. Targets: GO:1990612.

Fungi is a valid taxon, but the cited Chikashige fission-yeast abstract does not establish COMMON prevalence of this named Sad1–Kms1 assembly. Budding-yeast sources demonstrate a different Mps2/Mps3/Csm4 and actin/Myo2 system. Conservation of a LINC principle does not establish common distribution of the exact named subunits or a uniform cytoplasmic-dynein coupling.

### Fission-yeast telomere attachment and spindle support

evidence: supported. Targets: GO:1990612.

The existing2017 notes correctly say support rather than an absolute requirement. Bqt1-AID disruption during prophase can cause spindle/SPB defects, with successful divisions retained in a subset; direct spindle experiments use rdh54 background. CDK activation/Sad1 fenestration interpretations remain partly proposed. The2025 example correctly distinguishes partial mitotic recruitment from complete meiotic bouquet.

### Functional summary versus mechanistic chain

graph: concern. Targets: GO:1990612.

The graph has two part-of edges, one association and three whole-complex mediates outputs. It has no represented bridge-to-motor/force-to-telomere or other causal intermediate explaining the functional transition. FUNCTION is reasonable, but MECHANISTIC overstates this summary. Correct the source-subject problem separately; broad mediates outputs alone do not show the cited mechanisms.

### Current source tiers and original access receipts

provenance: supported. Targets: GO:1990612.

Native identities, primary JATS bodies and Chikashige abstract were read at the listed locators. The2012 Kms1 topology statement is background within a primary Hrs1 paper. The Chikashige API200 is metadata-only and its failed routes are retained. Original copied timestamps/hashes remain unchanged. Historical access notes are not findings.

### Bounded follow-up for named DSB and meiotic contexts

completeness: supported. Targets: GO:1990612.

The existing DSB definition has direct source support in Swartz2014 and should remain distinct from the meiotic bouquet extensions. Future curation can represent that role with its S/G2/repair-choice limits rather than borrowing the budding-yeast conversion assay. No optional-empty image, property, protein-family or component finding is asserted; there are no dependent local-neighbor records.

## Findings

### F1: Budding-yeast assays and broad fungal coupling are assigned to the named complex

major / open / confirmed; issue key: sad1-kms1-fungal-linc-scope-transfer.

Fan2020 directly tests budding-yeast Mps2–Mps3–Csm4, while both Fan-only output edges use Sad1–Kms1 as their subject. The pairing description acknowledges budding yeast but that qualifier does not change the graph subject or make the result an assay of Sad1–Kms1. The Fungi COMMON note likewise generalizes this named assembly and dynein/microtubule coupling from fission yeast, despite the distinct actin-associated budding-yeast system. Separate comparative LINC context from functions/distribution of the named S. pombe assembly. This is not a claim that Sad1–Kms1 lacks telomere or recombination roles.

### F2: Membership and functional outputs are labeled mechanistic

minor / open / confirmed; issue key: sad1-kms1-summary-graph-overstates-mechanistic-scope.

The seven-node graph presents membership/association and whole-complex outputs, without a represented chain explaining how the LINC bridge produces those outcomes. Retain FUNCTION but use honest NONMECHANISTIC scope with notes, or add independently supported causal intermediates and exact edge evidence during authorized curation. This classification issue is separate from the cross-species assignment in F1.

## Recommended Actions And Acceptance Checks

### A1

During authorized curation, bind named Sad1–Kms1 functions and edges to appropriate fission-yeast primary passages. Retain Fan/Lee findings only as explicitly comparative budding-yeast context, with their actual molecular subject. Narrow distribution to evidenced named-complex scope and distinguish conserved LINC architecture from motor/taxon generalizations.

- Every resulting causal edge must have the same molecular subject and organism as its cited assay; retain SK1/S288C versus fission-yeast distinctions.
- Preserve supported S/G2 DSB and meiotic telomere roles without claiming that Swartz mitotic gene conversion is the same assay as Fan meiotic conversion.
- Do not infer COMMON exact-subunit distribution or dynein coupling from Fungi taxonomy or generic SUN-family conservation.
- Run native schema/strict, protein verify/causal coverage, fresh CURIE/history and scientific edge review after an authorized validated-writer change.

### A2

Reclassify the current graph as NONMECHANISTIC functional context with scope notes, or build a supported mechanistic chain. Distinguish direct localization/depletion results from proposed motor cross-linking, force transmission and CDK/Sad1 pathways.

- Read each new intermediate and edge against its exact primary result or explicitly labeled model passage.
- Preserve species, meiosis versus mitosis, preparation and mutant-background bounds.
- Recheck graph_kind/scope_status and run focused native validators; preserve PROPOSED status and history unless separately authorized.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml; Entire YAML: definition, parent, three components, four protein examples, canonical example, three functions, all evidence, seven graph nodes/six edges, taxonomic distribution and history. | context_only | Complete record read after native inspection. The exact named S. pombe complex remains PROPOSED; function prose explicitly identifies one budding-yeast experiment, yet its graph subject is Sad1–Kms1. No physical-property or image assertion is present. |
| policy | docs/CURATION.md; Evidence placement and source scope; checklist and review/evidence/UniProt/causal skills are separately hashed native inputs. | context_only | Evidence must support its exact biological subject and experimental context. Native identifier verification is separate from primary structural support; historical readability notes and empty optional fields are not automatic defects. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component.essentiality; EssentialityEnum; CausalGraph and CausalGraphScopeEnum. | context_only | Essentiality concerns whether the structure forms without a component, distinct from function, viability and localization. A graph of membership and whole-structure outputs does not by itself explain a mechanism. |
| linc-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990612,GO:0034993,GO:0032200,GO:0032993,GO:0005634,GO:0000228,GO:0000781; All seven results: id/isObsolete/name/definition/xrefs/synonyms/children. GO1990612 definition cites PMID24943839 and24947240; GO0034993 children relation is is_a. | supports | Seven native nonobsolete terms verify exact GO1990612 identity and DSB-repair definition. GO0034993 lists GO1990612 as an is_a child. GO0032200 denotes telomere organization; GO0032993 requires DNA as a complex member, while nucleus, nuclear chromosome and telomeric region are contextual entities, not synonyms of the LINC complex. |
| linc-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045119/; metadata.accession/type/name/hierarchy/description and member_databases; family distinct from SUN-domain identifier. | supports | IPR045119 is the SUN domain-containing protein1–5 family, including Sad1/UNC84 context. It supports a SUN-family grounding without defining the whole Sad1–Kms1 complex or implying every member has this exact role. |
| linc-agent-tax-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; taxId, scientificName, rank, lineage. | supports | NCBITaxon284812 is Schizosaccharomyces pombe972h-, rank strain. This verifies the reference-sequence example taxon, not the genotype of each published experimental stock. |
| linc-agent-tax-4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; taxId, scientificName, rank, lineage, otherNames. | supports | NCBITaxon4751 is Fungi, kingdom rank. Its existence and label do not establish COMMON distribution of the named Sad1–Kms1 assembly. |
| linc-agent-Q09825 | https://rest.uniprot.org/uniprotkb/Q09825.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism and comments; Q09825 also has InterProIPR045119 cross-reference. | supports | The native reviewed Q09825 entry has gene sad1, recommended label Spindle pole body-associated protein sad1, and organism284812. Its own annotation supports the recorded protein identity; primary structural roles are assessed separately. |
| linc-agent-P87245 | https://rest.uniprot.org/uniprotkb/P87245.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism and comments. | supports | The native reviewed P87245 entry has gene kms1, recommended label Karyogamy meiotic segregation protein 1, and organism284812. Its own annotation supports the recorded protein identity; primary structural roles are assessed separately. |
| linc-agent-Q92358 | https://rest.uniprot.org/uniprotkb/Q92358.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism and comments. | supports | The native reviewed Q92358 entry has gene bqt1, recommended label Telomere bouquet protein 1, and organism284812. Its own annotation supports the recorded protein identity; primary structural roles are assessed separately. |
| linc-agent-Q9US52 | https://rest.uniprot.org/uniprotkb/Q9US52.json; primaryAccession, entryType, proteinDescription.recommendedName, genes, organism and comments. | supports | The native reviewed Q9US52 entry has gene bqt2, recommended label Telomere bouquet protein 2, and organism284812. Its own annotation supports the recorded protein identity; primary structural roles are assessed separately. |
| linc-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.26508/lsa.202000824%22%20OR%20DOI:%2210.1186/s12915-015-0149-x%22%20OR%20DOI:%2210.1016/j.cub.2020.01.054%22%20OR%20DOI:%2210.1038/s41467-025-56049-9%22&amp;format=json&amp;resultType=core&amp;pageSize=100; All four resultList.result objects: DOI, PMID, PMCID, title/authors, publication metadata, abstractText and fullTextUrlList. | supports | Europe PMC matches the four cited DOIs to Fan2020/PMID32967926/PMC7536833, Amelina2015/26058898/PMC4660835, Lee2020/32059771/PMC7181386 and Jimenez2025/39833200/PMC11747273. Abstracts are distinguished from the separately read full JATS bodies. |
| linc-agent-2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1016/j.cub.2012.02.042%22&amp;format=json&amp;resultType=core; Single result: title, author list, DOI/PMID and structured abstract. | supports | Native metadata identifies Funaya et al.2012, with Tanaka as senior author, DOI10.1016/j.cub.2012.02.042 and PMID22425159. Its abstract concerns Hrs1-dependent rMTOC organization, not a direct Sad1–Kms1 dynein-binding experiment. |
| linc-agent-doi-j.cell.2006.01.048-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2006.01.048; resultList.result[0]: DOI, PMID, title/authors, complete abstractText and fullTextUrlList (subscription required). | supports | Chikashige2006 PMID16615890 abstract directly identifies joint Bqt1/Bqt2 bridging of Rap1 and Sad1 in fission yeast and ectopic mitotic bridge formation. Neither protein alone suffices in that connector assay. This receipt contains metadata and abstract, not body or experimental-stock methods. |
| linc-agent-chikashige2006-api | https://api.elsevier.com/content/article/pii/S0092867406003187?httpAccept=text/xml; Entire1953-byte response; coredata and absence of article body within these bytes. | context_only | Actual HTTP200 Elsevier XML is a coredata-only entitlement response with no article body; it supplies metadata, not additional experimental support. |
| linc-agent-chikashige2006-publisher | https://www.sciencedirect.com/science/article/pii/S0092867406003187; Entire failed-access response; no primary body inspected through this route. | context_only | Native HTTP403 response retained for this exact route. This does not imply that the paper is globally inaccessible. |
| linc-agent-chikashige2006-pdf | https://citeseerx.ist.psu.edu/document?doi=68a98bfe81f55110dde11ec829414da46fc427f2&amp;repid=rep1&amp;type=pdf; Entire failed-access response; no primary body inspected through this route. | context_only | Native HTTP404 response retained for this exact route. This does not imply that the paper is globally inaccessible. |
| linc-agent-fan2020-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC7536833.1/PMC7536833.1.xml; PMC7536833.1: Introduction s1; Results s3–s9, particularly s7/p1–2 and s8/p1–3; Discussion s10; Methods s12–s18 (strains, culture, affinity purification, imaging/spreads and conversion assay). | partial | Primary budding-yeast study identifies Mps2–Mps3–Csm4 telomere LINC. Mps2 depletion/csm4 deletion affects Rap1 clustering, delays LYS4 pairing and reduces ARG4/HIS4 gene conversion. Meiotic experiments use SK1; mitotic reconstruction uses S288C. Discussion distinguishes model-level nonamer/direct-cytoskeletal assumptions from observed interactions. These are not direct Sad1–Kms1 assays. |
| linc-agent-amelina2015-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4660835.1/PMC4660835.1.xml; PMC4660835.1: Background; Results Sec3–Sec6, especially Sec5 and Sec6; Discussion Sec7; Methods Sec10–Sec16. pat1-114 synchronization26→34°C is distinct from homothallic live-cell assays. Deposited raw mass spectra not reanalyzed. | supports | Primary S. pombe Rap1 study supports the Bqt1/2 connector interface: Rap1 DD337AA disrupts Bqt interaction and meiotic clustering while retaining other tested interactions. Phosphomimetic/nonphosphorylatable clusters do not establish the proposed phosphorylation switch; hydrogen-bond explanation remains speculation. These are connector-function assays, not removal tests of both core LINC subunits. |
| linc-agent-csm2020-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC7181386.1/PMC7181386.1.xml; PMC7181386.1: Introduction S1; Results S3–S8; Discussion S10; Methods S14/S16–S20. Chromosome-spread ends include envelope remnants; dominant-negative Myo2 can affect additional functions. | partial | Primary S. cerevisiae study uses localization, co-IP, two-hybrid and Myo2 dominant-negative perturbations to support an Mps2/Myo2-associated actin-motility model. Csm4 is interpreted as an accessory regulator, with stabilization versus actin recruitment alternatives. This supplies a concrete limit on extending a dynein/microtubule account to all fungal LINC systems. |
| linc-agent-moiseeva2017-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5674143.1/PMC5674143.1.xml; PMC5674143.1: Results The bouquet stage is retained; Bouquet formation ensures entry; CDK1cyclin B at SPB; Premature termination paragraphs1–3 and Figures7–8 captions; Discussion; Methods strains/media, AID construction, microscopy28°C and auxin-inducible system. Figure pixels/videos not reanalyzed. | supports | Primary fission-yeast live imaging and Bqt1-AID degradation support continued telomere–SPB attachment and normal spindle behavior. Roughly half of bouquet-deficient cells can still divide; spindle defects after premature loss are condition-dependent. Rdh54 background is used for direct spindle imaging, and CDK/Sad1 mechanistic links remain partly proposed. |
| linc-agent-jimenez2025-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/PMC11747273.1.xml; PMC11747273.1: Results Sec8/p1–6 (Figure6), Sec9/p1, Sec10/p1 (Figure7); Discussion Sec12/p1–5; Methods Sec14/p1–3 (haploid growth32°C; diploid induction28°C). Original08:24:58.921258Z receipt retained. | supports | Primary S. pombe Rabl-deficient mitotic recruitment study observes Bqt1/2, Sad1/Kms1, Alp4 and Mto1 at telomeres after ectopic Bqt expression, but no detected Dhc1 or complete bouquet. Natural meiotic-entry imaging is a separate diploid experiment. The existing Kms1 example correctly retains the partial-reconstitution limit. |
| linc-agent-tanaka2012-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml; PMC3382715.1 XML: article title/author list; Introduction sec1/p2–3; Results sec2.5/p4 and Discussion sec3/p7–8; Methods sec4.1. Original07:08:03.849693Z preserved. No claim of main-PDF inspection. | partial | These bytes are the genuine Funaya et al.2012 JATS article despite the local filename suffix. Introduction supplies prior-study Kms1 topology/Sad1 and dynein context. Direct Hrs1 phosphomutant two-hybrid results test Kms1/Alp4 interactions, with possible Kms2 compensation discussed. They are not direct dynein-recruitment assays. |
| linc-agent-yoshida2013-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3575533.1/PMC3575533.1.xml; PMC3575533.1 DOI10.1083/jcb.201207168: Results and discussion paragraphs1–12, especially5–6 and10–11 (Figures3–5); Methods Strains/media, Kms2 visualization, zygotic meiosis25°C, mat-induced haploid meiosis30°C/MBC and live-cell imaging25–27°C. Original08:24:58.783865Z retained. | supports | Additional primary S. pombe source directly finds Kms1 and Kms2 at meiotic telocentrosomes; Kms1-dependent Dlc1/Mto1/Alp4 localization supports a bridge-associated role. Microtubule recovery and motor mutants support clustering, while the detailed cross-linking/transport sequence is a model and kinesins also contribute. This does not establish a universal dynein-only fungal mechanism. |
| linc-agent-swartz2014-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4142617.1/PMC4142617.1.xml; PMC4142617.1 DOI10.1091/mbc.E13-10-0569: Introduction; Results induced DSBs, Sad1 foci, Kms1 colocalization, Kms1 promotes conversion, genetic interactions; Discussion/Figure6 caption; Methods cell culture30°C, HO induction24h, G1 arrest, microscopy and repair-pathway-choice assay. | supports | GO-linked primary S. pombe study supports S/G2 DSB association with Sad1/Kms1 and altered gene-conversion pathway choice after kms1 or mto1 loss. Kms2 is not detected at MMS-induced Sad1 foci, but Discussion explicitly leaves possible redundancy/unseen low-copy contributions open. Figure6 is a proposed repair model; viability, DSB localization and assembly necessity are distinct. |
| linc-agent-dsb-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:24943839%20OR%20EXT_ID:24947240&amp;format=json&amp;resultType=core&amp;pageSize=100; Both resultList.result objects: DOI, PMID, title/authors, publication type and abstractText. | supports | Native metadata matches PMID24943839 to Swartz2014 primary DSB-repair study. PMID24947240 is a LINC development/disease review chapter; its abstract is background only and is not used as direct experimental evidence. |
| schema-result | just validate data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/sad1_kms1_linc_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/sad1_kms1_linc_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch16-20261021-fjx428vi/sad1_kms1_linc_complex-strict.tsv |
| native-verify | /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml --verify; Complete focused native log. | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml --causal-graphs; Complete focused native log. | supports | data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml  (GO:1990612)<br>  sad1_kms1_linc_complex_mechanism	sad1_sun_protein	COVERED	-&gt;sad1_sun_protein (UniProtKB:Q09825)<br>  sad1_kms1_linc_complex_mechanism	kms1_kash_protein	COVERED	-&gt;kms1_kash_protein (UniProtKB:P87245)<br>  sad1_kms1_linc_complex_mechanism	bqt1_bqt2_meiotic_connector	COVERED	-&gt;bqt1_bqt2_meiotic_connector (UniProtKB:Q92358, UniProtKB:Q9US52)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| target-curies-result | just check-curies-strict; data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml; exact native collect() target slice of original fresh-base TSV | supports | 21 of 21 exact target identifiers returned OK. No target residuals. The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The exact target resolver slice is derived from the completed fresh-base run. Any PMID transport failures were checked against the separately cited native literature metadata; these identity checks do not establish full-body scientific support.
- Chikashige2006 is abstract-only in this source packet. Native publisher403, attempted PDF404 and API200 coredata-only responses are retained. Body-level experimental-stock and domain-detail claims are not inferred from the abstract.
- Primary body text and claim-bearing captions/methods were read at listed locators. Image pixels, original videos, raw mass spectra and complete supplementary experimental-stock tables were not independently reanalyzed. The record has no image asset requiring visual/license review.
- Four972h- protein entries are reference-sequence examples, not exact experimental strains. Fan meiotic SK1 and mitotic S288C, fission-yeast h90/temperature-sensitive/engineered backgrounds, and2025 mitotic partial recruitment remain distinct.
- ESSENTIAL retains its exact schema assembly meaning. Functional perturbation, gene viability and localization data do not supply a complete assembly necessity test for each core subunit; this uncertainty is not converted into an opposite essentiality finding.
- Kms2 localization at meiotic telocentrosomes and its absence from detected MMS foci apply to different contexts. Possible partial redundancy and low-copy detection limits remain open; no fixed three-subunit stoichiometry or global absence is asserted.
- Funaya2012 main-body source is JATS despite local tanaka2012-pdf filename; author/title/format were verified. Its introductory bridge account is prior-study context, while its own direct assays concern Hrs1/rMTOC behavior.
- All14 native repository inputs retain their inspected hashes. External source receipts preserve actual HTTP statuses and original UTCZ times; no browser extraction is represented as an HTTP attestation.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Root owns finalization/save after fresh global checks. No maintained scientific record, shared index, Git state or generated product was changed.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094818Z-sad1-kms1-linc-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Sad1–Kms1 LINC complex identity, species scope and mechanism review
started_at: '2026-10-21T09:24:19Z'
finished_at: '2026-10-21T09:48:18Z'
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
summary: Exact identity, native parent, four reviewed protein examples and bounded
  fission-yeast roles are supported. One major species/assembly scope transfer and
  one minor graph-scope issue require curation; assembly necessity and Kms2 context
  remain explicitly limited.
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
  - path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    sha256: 2dc179231cae9404e022e417327a94b550b75c47872ef2e467330ea79d5cdf17
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
- target_id: GO:1990612
  path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
  label: Sad1-Kms1 LINC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained scientific record
scope:
  description: Full exact record, all declared native IDs, cited primary claim-bearing
    sections and additional native-GO-linked/meiotic primary context; no local neighbor
    dependency.
  selection: Batch16 index6; exact maintained record GO:1990612 at fresh-main base9c0446.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990612
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990612
  command: just validate data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990612
  command: just validate-strict data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/sad1_kms1_linc_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:1990612
  command: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    --verify
  exit_code: 0
  summary: Native check passed; identity/graph coverage is distinct from scientific
    evidence support.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990612
  command: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native check passed; identity/graph coverage is distinct from scientific
    evidence support.
  evidence_ids:
  - native-causal-graphs
- check_id: expression-applicability
  name: Expression-module source applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990612
  summary: The record has protein identities and structural roles, all checked with
    native UniProt and primary sources. It has no expression-module assertion requiring
    iModulonDB.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990612
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - schema
  - linc-agent-go
  - linc-agent-family
  - linc-agent-tax-284812
  - linc-agent-tax-4751
  - linc-agent-Q09825
  - linc-agent-P87245
  - linc-agent-Q92358
  - linc-agent-Q9US52
  - linc-agent-epmc
  - linc-agent-2012-meta
  - linc-agent-doi-j.cell.2006.01.048-meta
  - linc-agent-chikashige2006-api
  - linc-agent-chikashige2006-publisher
  - linc-agent-chikashige2006-pdf
  - linc-agent-fan2020-jats
  - linc-agent-amelina2015-jats
  - linc-agent-csm2020-jats
  - linc-agent-moiseeva2017-jats
  - linc-agent-jimenez2025-jats
  - linc-agent-tanaka2012-pdf
  - linc-agent-yoshida2013-jats
  - linc-agent-swartz2014-jats
  - linc-agent-dsb-meta
- check_id: target-curies
  name: Target resolver slice with native transport-failure cross-checks
  status: passed
  required: true
  target_ids:
  - GO:1990612
  summary: 21 of 21 exact target identifiers returned OK. No target residuals. The
    shared command exit zero is not interpreted as successful network resolution for
    transport failures.
  evidence_ids:
  - target-curies-result
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990612
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
  - GO:1990612
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
  - GO:1990612
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
  - GO:1990612
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
  - GO:1990612
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
  reference: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
  locator: 'Entire YAML: definition, parent, three components, four protein examples,
    canonical example, three functions, all evidence, seven graph nodes/six edges,
    taxonomic distribution and history.'
  accessed_at: '2026-10-21T09:32:35Z'
  support: context_only
  summary: Complete record read after native inspection. The exact named S. pombe
    complex remains PROPOSED; function prose explicitly identifies one budding-yeast
    experiment, yet its graph subject is Sad1–Kms1. No physical-property or image
    assertion is present.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Evidence placement and source scope; checklist and review/evidence/UniProt/causal
    skills are separately hashed native inputs.
  accessed_at: '2026-10-21T09:32:35Z'
  support: context_only
  summary: Evidence must support its exact biological subject and experimental context.
    Native identifier verification is separate from primary structural support; historical
    readability notes and empty optional fields are not automatic defects.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component.essentiality; EssentialityEnum; CausalGraph and CausalGraphScopeEnum.
  accessed_at: '2026-10-21T09:32:35Z'
  support: context_only
  summary: Essentiality concerns whether the structure forms without a component,
    distinct from function, viability and localization. A graph of membership and
    whole-structure outputs does not by itself explain a mechanism.
- evidence_id: linc-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990612,GO:0034993,GO:0032200,GO:0032993,GO:0005634,GO:0000228,GO:0000781
  locator: 'All seven results: id/isObsolete/name/definition/xrefs/synonyms/children.
    GO1990612 definition cites PMID24943839 and24947240; GO0034993 children relation
    is is_a.'
  accessed_at: '2026-10-21T09:25:22.693747Z'
  support: supports
  summary: Seven native nonobsolete terms verify exact GO1990612 identity and DSB-repair
    definition. GO0034993 lists GO1990612 as an is_a child. GO0032200 denotes telomere
    organization; GO0032993 requires DNA as a complex member, while nucleus, nuclear
    chromosome and telomeric region are contextual entities, not synonyms of the LINC
    complex.
  snapshot_sha256: 7eb3c9ffaf4a96aa8a6f064a948d01cacb5f8dba064480cd9ff1add57a3875c6
- evidence_id: linc-agent-family
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045119/
  locator: metadata.accession/type/name/hierarchy/description and member_databases;
    family distinct from SUN-domain identifier.
  accessed_at: '2026-10-21T09:25:22.694806Z'
  support: supports
  summary: IPR045119 is the SUN domain-containing protein1–5 family, including Sad1/UNC84
    context. It supports a SUN-family grounding without defining the whole Sad1–Kms1
    complex or implying every member has this exact role.
  snapshot_sha256: ebf2e470f10e591fe8475c39ac5142261438a51a9bba2571c0282d80a75d359e
- evidence_id: linc-agent-tax-284812
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: taxId, scientificName, rank, lineage.
  accessed_at: '2026-10-21T09:25:22.695146Z'
  support: supports
  summary: NCBITaxon284812 is Schizosaccharomyces pombe972h-, rank strain. This verifies
    the reference-sequence example taxon, not the genotype of each published experimental
    stock.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: linc-agent-tax-4751
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: taxId, scientificName, rank, lineage, otherNames.
  accessed_at: '2026-10-21T09:25:22.695973Z'
  support: supports
  summary: NCBITaxon4751 is Fungi, kingdom rank. Its existence and label do not establish
    COMMON distribution of the named Sad1–Kms1 assembly.
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: linc-agent-Q09825
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q09825.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism and comments; Q09825 also has InterProIPR045119 cross-reference.
  accessed_at: '2026-10-21T09:25:23.318041Z'
  support: supports
  summary: The native reviewed Q09825 entry has gene sad1, recommended label Spindle
    pole body-associated protein sad1, and organism284812. Its own annotation supports
    the recorded protein identity; primary structural roles are assessed separately.
  snapshot_sha256: af97b71167c7297318086add00ac1143a9ab78a2f714035f76ff4c31bf77993d
- evidence_id: linc-agent-P87245
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P87245.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism and comments.
  accessed_at: '2026-10-21T09:25:23.320416Z'
  support: supports
  summary: The native reviewed P87245 entry has gene kms1, recommended label Karyogamy
    meiotic segregation protein 1, and organism284812. Its own annotation supports
    the recorded protein identity; primary structural roles are assessed separately.
  snapshot_sha256: 84aa928d02abba093e6be0c791d5d9f775268e8701d7955ab7f7d7cbb36eb234
- evidence_id: linc-agent-Q92358
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q92358.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism and comments.
  accessed_at: '2026-10-21T09:25:23.322668Z'
  support: supports
  summary: The native reviewed Q92358 entry has gene bqt1, recommended label Telomere
    bouquet protein 1, and organism284812. Its own annotation supports the recorded
    protein identity; primary structural roles are assessed separately.
  snapshot_sha256: f4cfccab706bbf9515cd342b8bf6a7409bdb96c9a45f0e6ac5320e967827dd42
- evidence_id: linc-agent-Q9US52
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9US52.json
  locator: primaryAccession, entryType, proteinDescription.recommendedName, genes,
    organism and comments.
  accessed_at: '2026-10-21T09:25:23.328539Z'
  support: supports
  summary: The native reviewed Q9US52 entry has gene bqt2, recommended label Telomere
    bouquet protein 2, and organism284812. Its own annotation supports the recorded
    protein identity; primary structural roles are assessed separately.
  snapshot_sha256: 51cfcf49971d8963b57f32b278b49e710b600813b392a15565ffb4b80b2b09e9
- evidence_id: linc-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.26508/lsa.202000824%22%20OR%20DOI:%2210.1186/s12915-015-0149-x%22%20OR%20DOI:%2210.1016/j.cub.2020.01.054%22%20OR%20DOI:%2210.1038/s41467-025-56049-9%22&format=json&resultType=core&pageSize=100
  locator: 'All four resultList.result objects: DOI, PMID, PMCID, title/authors, publication
    metadata, abstractText and fullTextUrlList.'
  accessed_at: '2026-10-21T09:25:46.270686Z'
  support: supports
  summary: Europe PMC matches the four cited DOIs to Fan2020/PMID32967926/PMC7536833,
    Amelina2015/26058898/PMC4660835, Lee2020/32059771/PMC7181386 and Jimenez2025/39833200/PMC11747273.
    Abstracts are distinguished from the separately read full JATS bodies.
  snapshot_sha256: bd8d91d49111eea37d422d02343761960020f4d8390c85ec100d8f123a2fbc15
- evidence_id: linc-agent-2012-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1016/j.cub.2012.02.042%22&format=json&resultType=core
  locator: 'Single result: title, author list, DOI/PMID and structured abstract.'
  accessed_at: '2026-10-21T09:25:22.696889Z'
  support: supports
  summary: Native metadata identifies Funaya et al.2012, with Tanaka as senior author,
    DOI10.1016/j.cub.2012.02.042 and PMID22425159. Its abstract concerns Hrs1-dependent
    rMTOC organization, not a direct Sad1–Kms1 dynein-binding experiment.
  snapshot_sha256: cb2a9bbadec30edf9cbc7db3fb875967aa30edf57b4c38969fe751991a94be54
- evidence_id: linc-agent-doi-j.cell.2006.01.048-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2006.01.048
  locator: 'resultList.result[0]: DOI, PMID, title/authors, complete abstractText
    and fullTextUrlList (subscription required).'
  accessed_at: '2026-10-21T09:25:52.864043Z'
  support: supports
  summary: Chikashige2006 PMID16615890 abstract directly identifies joint Bqt1/Bqt2
    bridging of Rap1 and Sad1 in fission yeast and ectopic mitotic bridge formation.
    Neither protein alone suffices in that connector assay. This receipt contains
    metadata and abstract, not body or experimental-stock methods.
  snapshot_sha256: fd5cac1bd8170b876a62b1c8047774632bb68ee6b345e9e7f6748cd5ef216a78
- evidence_id: linc-agent-chikashige2006-api
  kind: database
  reference: https://api.elsevier.com/content/article/pii/S0092867406003187?httpAccept=text/xml
  locator: Entire1953-byte response; coredata and absence of article body within these
    bytes.
  accessed_at: '2026-10-21T09:27:43.453084Z'
  support: context_only
  summary: Actual HTTP200 Elsevier XML is a coredata-only entitlement response with
    no article body; it supplies metadata, not additional experimental support.
  snapshot_sha256: 27c2e01cb879e50c3450a2143481c0fcb9f545b956a5caf4b957e2fe94046d95
- evidence_id: linc-agent-chikashige2006-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0092867406003187
  locator: Entire failed-access response; no primary body inspected through this route.
  accessed_at: '2026-10-21T09:27:43.248709Z'
  support: context_only
  summary: Native HTTP403 response retained for this exact route. This does not imply
    that the paper is globally inaccessible.
  snapshot_sha256: 941cd44c9bc96feee6c75580b52cd167703d218a83303e305499758774a1627a
- evidence_id: linc-agent-chikashige2006-pdf
  kind: authority
  reference: https://citeseerx.ist.psu.edu/document?doi=68a98bfe81f55110dde11ec829414da46fc427f2&repid=rep1&type=pdf
  locator: Entire failed-access response; no primary body inspected through this route.
  accessed_at: '2026-10-21T09:27:43.691209Z'
  support: context_only
  summary: Native HTTP404 response retained for this exact route. This does not imply
    that the paper is globally inaccessible.
  snapshot_sha256: 8e7548f00d7f002af43c4325ac23387121ddb731b9bb27c7c54c658275a4375e
- evidence_id: linc-agent-fan2020-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7536833.1/PMC7536833.1.xml
  locator: 'PMC7536833.1: Introduction s1; Results s3–s9, particularly s7/p1–2 and
    s8/p1–3; Discussion s10; Methods s12–s18 (strains, culture, affinity purification,
    imaging/spreads and conversion assay).'
  accessed_at: '2026-10-21T09:25:46.268839Z'
  support: partial
  summary: Primary budding-yeast study identifies Mps2–Mps3–Csm4 telomere LINC. Mps2
    depletion/csm4 deletion affects Rap1 clustering, delays LYS4 pairing and reduces
    ARG4/HIS4 gene conversion. Meiotic experiments use SK1; mitotic reconstruction
    uses S288C. Discussion distinguishes model-level nonamer/direct-cytoskeletal assumptions
    from observed interactions. These are not direct Sad1–Kms1 assays.
  snapshot_sha256: 0013a1fcdd1d7b85b83d74900747997300119411c46cc5a932d59d25f75db9c0
- evidence_id: linc-agent-amelina2015-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4660835.1/PMC4660835.1.xml
  locator: 'PMC4660835.1: Background; Results Sec3–Sec6, especially Sec5 and Sec6;
    Discussion Sec7; Methods Sec10–Sec16. pat1-114 synchronization26→34°C is distinct
    from homothallic live-cell assays. Deposited raw mass spectra not reanalyzed.'
  accessed_at: '2026-10-21T09:25:46.269721Z'
  support: supports
  summary: 'Primary S. pombe Rap1 study supports the Bqt1/2 connector interface: Rap1
    DD337AA disrupts Bqt interaction and meiotic clustering while retaining other
    tested interactions. Phosphomimetic/nonphosphorylatable clusters do not establish
    the proposed phosphorylation switch; hydrogen-bond explanation remains speculation.
    These are connector-function assays, not removal tests of both core LINC subunits.'
  snapshot_sha256: 928c024c3338595e5fe589c9d3c9174f03bdccf5c75eb89648eca6459a5d4112
- evidence_id: linc-agent-csm2020-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7181386.1/PMC7181386.1.xml
  locator: 'PMC7181386.1: Introduction S1; Results S3–S8; Discussion S10; Methods
    S14/S16–S20. Chromosome-spread ends include envelope remnants; dominant-negative
    Myo2 can affect additional functions.'
  accessed_at: '2026-10-21T09:25:46.270923Z'
  support: partial
  summary: Primary S. cerevisiae study uses localization, co-IP, two-hybrid and Myo2
    dominant-negative perturbations to support an Mps2/Myo2-associated actin-motility
    model. Csm4 is interpreted as an accessory regulator, with stabilization versus
    actin recruitment alternatives. This supplies a concrete limit on extending a
    dynein/microtubule account to all fungal LINC systems.
  snapshot_sha256: fc2ee1f306bcb93fb50bd1335c1a60bdd901b50f1ece7f7b1f8c63371a362c9a
- evidence_id: linc-agent-moiseeva2017-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5674143.1/PMC5674143.1.xml
  locator: 'PMC5674143.1: Results The bouquet stage is retained; Bouquet formation
    ensures entry; CDK1cyclin B at SPB; Premature termination paragraphs1–3 and Figures7–8
    captions; Discussion; Methods strains/media, AID construction, microscopy28°C
    and auxin-inducible system. Figure pixels/videos not reanalyzed.'
  accessed_at: '2026-10-21T09:27:43.695545Z'
  support: supports
  summary: Primary fission-yeast live imaging and Bqt1-AID degradation support continued
    telomere–SPB attachment and normal spindle behavior. Roughly half of bouquet-deficient
    cells can still divide; spindle defects after premature loss are condition-dependent.
    Rdh54 background is used for direct spindle imaging, and CDK/Sad1 mechanistic
    links remain partly proposed.
  snapshot_sha256: e5b2fc8c46775b2f6a9e0b176bb16d6f2bae801e78e90b191369414ca23f84a3
- evidence_id: linc-agent-jimenez2025-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/PMC11747273.1.xml
  locator: 'PMC11747273.1: Results Sec8/p1–6 (Figure6), Sec9/p1, Sec10/p1 (Figure7);
    Discussion Sec12/p1–5; Methods Sec14/p1–3 (haploid growth32°C; diploid induction28°C).
    Original08:24:58.921258Z receipt retained.'
  accessed_at: '2026-10-21T08:24:58.921258Z'
  support: supports
  summary: Primary S. pombe Rabl-deficient mitotic recruitment study observes Bqt1/2,
    Sad1/Kms1, Alp4 and Mto1 at telomeres after ectopic Bqt expression, but no detected
    Dhc1 or complete bouquet. Natural meiotic-entry imaging is a separate diploid
    experiment. The existing Kms1 example correctly retains the partial-reconstitution
    limit.
  snapshot_sha256: 1e0470a799e49976e35584be8e8449af77c2e85fd1e11576a460227cd526e4ed
- evidence_id: linc-agent-tanaka2012-pdf
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml
  locator: 'PMC3382715.1 XML: article title/author list; Introduction sec1/p2–3; Results
    sec2.5/p4 and Discussion sec3/p7–8; Methods sec4.1. Original07:08:03.849693Z preserved.
    No claim of main-PDF inspection.'
  accessed_at: '2026-10-21T07:08:03.849693Z'
  support: partial
  summary: These bytes are the genuine Funaya et al.2012 JATS article despite the
    local filename suffix. Introduction supplies prior-study Kms1 topology/Sad1 and
    dynein context. Direct Hrs1 phosphomutant two-hybrid results test Kms1/Alp4 interactions,
    with possible Kms2 compensation discussed. They are not direct dynein-recruitment
    assays.
  snapshot_sha256: 59f662c998abf622fbb9bccbabc3867cb5ffd3174943cc52cb6228b1e35cd93d
- evidence_id: linc-agent-yoshida2013-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3575533.1/PMC3575533.1.xml
  locator: 'PMC3575533.1 DOI10.1083/jcb.201207168: Results and discussion paragraphs1–12,
    especially5–6 and10–11 (Figures3–5); Methods Strains/media, Kms2 visualization,
    zygotic meiosis25°C, mat-induced haploid meiosis30°C/MBC and live-cell imaging25–27°C.
    Original08:24:58.783865Z retained.'
  accessed_at: '2026-10-21T08:24:58.783865Z'
  support: supports
  summary: Additional primary S. pombe source directly finds Kms1 and Kms2 at meiotic
    telocentrosomes; Kms1-dependent Dlc1/Mto1/Alp4 localization supports a bridge-associated
    role. Microtubule recovery and motor mutants support clustering, while the detailed
    cross-linking/transport sequence is a model and kinesins also contribute. This
    does not establish a universal dynein-only fungal mechanism.
  snapshot_sha256: 0f228ac437c8af6f3d9edc0552d70b3b15a670714423cd3d32e094ec0cc4e274
- evidence_id: linc-agent-swartz2014-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4142617.1/PMC4142617.1.xml
  locator: 'PMC4142617.1 DOI10.1091/mbc.E13-10-0569: Introduction; Results induced
    DSBs, Sad1 foci, Kms1 colocalization, Kms1 promotes conversion, genetic interactions;
    Discussion/Figure6 caption; Methods cell culture30°C, HO induction24h, G1 arrest,
    microscopy and repair-pathway-choice assay.'
  accessed_at: '2026-10-21T09:26:39.370247Z'
  support: supports
  summary: GO-linked primary S. pombe study supports S/G2 DSB association with Sad1/Kms1
    and altered gene-conversion pathway choice after kms1 or mto1 loss. Kms2 is not
    detected at MMS-induced Sad1 foci, but Discussion explicitly leaves possible redundancy/unseen
    low-copy contributions open. Figure6 is a proposed repair model; viability, DSB
    localization and assembly necessity are distinct.
  snapshot_sha256: 96757e335f80ab5d8d85587382e5be1bd0c74a00689ca413aeaa4598600d595e
- evidence_id: linc-agent-dsb-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:24943839%20OR%20EXT_ID:24947240&format=json&resultType=core&pageSize=100
  locator: 'Both resultList.result objects: DOI, PMID, title/authors, publication
    type and abstractText.'
  accessed_at: '2026-10-21T09:26:39.370903Z'
  support: supports
  summary: Native metadata matches PMID24943839 to Swartz2014 primary DSB-repair study.
    PMID24947240 is a LINC development/disease review chapter; its abstract is background
    only and is not used as direct experimental evidence.
  snapshot_sha256: 9d509718f05d362581890100835ab87c8ddfc194249f51316fd8a7f1cc2af60b
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:24:22Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml'
  snapshot_sha256: ca26a804bb2a8165f5565c02535dc05b85133939fe090bf65dfab5f4bdf73104
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/sad1_kms1_linc_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:24:23Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml\
    \ --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/sad1_kms1_linc_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch16-20261021-fjx428vi/sad1_kms1_linc_complex-strict.tsv"
  snapshot_sha256: 4b5f34f66117780137a39c27900e2769e418bce6603fac491f88966a3d11c182
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    --verify
  locator: Complete focused native log.
  accessed_at: '2026-10-21T09:26:20.288088Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    --causal-graphs
  locator: Complete focused native log.
  accessed_at: '2026-10-21T09:26:21.032309Z'
  support: supports
  summary: "data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml  (GO:1990612)\n\
    \  sad1_kms1_linc_complex_mechanism\tsad1_sun_protein\tCOVERED\t->sad1_sun_protein\
    \ (UniProtKB:Q09825)\n  sad1_kms1_linc_complex_mechanism\tkms1_kash_protein\t\
    COVERED\t->kms1_kash_protein (UniProtKB:P87245)\n  sad1_kms1_linc_complex_mechanism\t\
    bqt1_bqt2_meiotic_connector\tCOVERED\t->bqt1_bqt2_meiotic_connector (UniProtKB:Q92358,\
    \ UniProtKB:Q9US52)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: f7904ee0c4b1bcdcbd512a8673dee9e3c7dd3e97c6ad16dc0b8734af0bbca87d
- evidence_id: target-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml; exact native
    collect() target slice of original fresh-base TSV
  accessed_at: '2026-10-21T09:48:00.329300Z'
  support: supports
  summary: 21 of 21 exact target identifiers returned OK. No target residuals. The
    shared command exit zero is not interpreted as successful network resolution for
    transport failures.
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
  topic: Named complex and exact native parent
  outcome: supported
  target_ids:
  - GO:1990612
  summary: GO1990612 exactly denotes Sad1–Kms1, and its DSB-repair opening is supported
    by native GO and Swartz2014. The GO0034993 parent relationship is explicitly is_a
    in the native graph. Meiotic roles are additional contexts, not evidence that
    DNA itself is a core subunit or that this named complex equals every fungal LINC
    system.
  evidence_ids:
  - record
  - linc-agent-go
  - linc-agent-swartz2014-jats
- assessment_id: composition
  area: representation
  topic: Core constituents and conditional connector
  outcome: supported
  target_ids:
  - GO:1990612
  summary: Sad1 and Kms1 are the named envelope-spanning constituents; Bqt1/Bqt2 are
    appropriately ASSOCIATED_MACHINERY with meiotic context. Chikashige abstract,
    Amelina interaction assays, Moiseeva degradation and Yoshida localization support
    their bounded roles. Funaya2012 supplies cited background plus Hrs1 interaction
    evidence, not a standalone direct dynein-recruitment experiment.
  evidence_ids:
  - record
  - linc-agent-doi-j.cell.2006.01.048-meta
  - linc-agent-amelina2015-jats
  - linc-agent-moiseeva2017-jats
  - linc-agent-yoshida2013-jats
  - linc-agent-tanaka2012-pdf
- assessment_id: assembly
  area: evidence
  topic: Assembly necessity distinct from viability and function
  outcome: unknown
  target_ids:
  - GO:1990612
  summary: The inspected experiments establish identities, interactions, local recruitment
    and phenotypic effects. They do not provide a complete subunit-removal/reconstitution
    test of whether the named two-protein complex forms without each constituent.
    Retain this uncertainty when reading ESSENTIAL; neither Kms1 viability nor residual
    Sad1 foci establishes DISPENSABLE, and Bqt1-dependent bouquet loss is not destruction
    of every LINC assembly. The connector row’s CONDITIONAL value is likewise not
    verified as a requirement for assembly of the named core complex; bouquet attachment
    is a separate endpoint.
  evidence_ids:
  - record
  - schema
  - linc-agent-swartz2014-jats
  - linc-agent-moiseeva2017-jats
- assessment_id: kms2-context
  area: scope
  topic: Meiotic Kms2 recruitment versus DSB-associated complex
  outcome: unknown
  target_ids:
  - GO:1990612
  summary: The definition parenthetical and Kms2-related interpretations require context.
    Yoshida directly sees Kms2 at meiotic telocentrosomes; Funaya discusses possible
    Hrs1–Kms2 compensation. Swartz sees no Kms2 recruitment to MMS-induced foci but
    explicitly leaves redundancy possible. These observations do not prove a fixed
    three-subunit stoichiometry, nor global Kms2 absence; no absence finding is made.
  evidence_ids:
  - record
  - linc-agent-yoshida2013-jats
  - linc-agent-tanaka2012-pdf
  - linc-agent-swartz2014-jats
- assessment_id: native-proteins
  area: grounding
  topic: Four exact reference examples and SUN family
  outcome: supported
  target_ids:
  - GO:1990612
  summary: All four reviewed accessions, native labels, gene symbols and taxon284812
    match. IPR045119 is an appropriate SUN-family grounding and is cross-referenced
    by Q09825. The explicit reference-sequence roles avoid asserting that972h- was
    each experimental stock. Gene examples on all three protein graph nodes are inherited
    by valid component_ref; native verify and graph gates pass.
  evidence_ids:
  - linc-agent-family
  - linc-agent-tax-284812
  - linc-agent-Q09825
  - linc-agent-P87245
  - linc-agent-Q92358
  - linc-agent-Q9US52
  - native-verify
  - native-causal-graphs
  - record
- assessment_id: function-transfer
  area: scope
  topic: Species and molecular subject of functional assays
  outcome: concern
  target_ids:
  - GO:1990612
  summary: The function description accurately names budding yeast, but the record
    and mediates edges still assign Fan Mps2/Csm4 assays to the Sad1–Kms1 subject.
    Fan assays are SK1/S288C Mps2–Mps3–Csm4 experiments. Moiseeva/Yoshida support
    fission-yeast bouquet roles separately. Retain the comparative account as comparison,
    or replace assigned claims with appropriate S. pombe evidence and conditions.
  evidence_ids:
  - record
  - linc-agent-fan2020-jats
  - linc-agent-moiseeva2017-jats
  - linc-agent-yoshida2013-jats
- assessment_id: taxonomic-scope
  area: scope
  topic: Named assembly versus conserved LINC principle
  outcome: concern
  target_ids:
  - GO:1990612
  summary: Fungi is a valid taxon, but the cited Chikashige fission-yeast abstract
    does not establish COMMON prevalence of this named Sad1–Kms1 assembly. Budding-yeast
    sources demonstrate a different Mps2/Mps3/Csm4 and actin/Myo2 system. Conservation
    of a LINC principle does not establish common distribution of the exact named
    subunits or a uniform cytoplasmic-dynein coupling.
  evidence_ids:
  - record
  - linc-agent-tax-4751
  - linc-agent-doi-j.cell.2006.01.048-meta
  - linc-agent-fan2020-jats
  - linc-agent-csm2020-jats
- assessment_id: spindle-function
  area: evidence
  topic: Fission-yeast telomere attachment and spindle support
  outcome: supported
  target_ids:
  - GO:1990612
  summary: The existing2017 notes correctly say support rather than an absolute requirement.
    Bqt1-AID disruption during prophase can cause spindle/SPB defects, with successful
    divisions retained in a subset; direct spindle experiments use rdh54 background.
    CDK activation/Sad1 fenestration interpretations remain partly proposed. The2025
    example correctly distinguishes partial mitotic recruitment from complete meiotic
    bouquet.
  evidence_ids:
  - record
  - linc-agent-moiseeva2017-jats
  - linc-agent-jimenez2025-jats
- assessment_id: graph
  area: graph
  topic: Functional summary versus mechanistic chain
  outcome: concern
  target_ids:
  - GO:1990612
  summary: The graph has two part-of edges, one association and three whole-complex
    mediates outputs. It has no represented bridge-to-motor/force-to-telomere or other
    causal intermediate explaining the functional transition. FUNCTION is reasonable,
    but MECHANISTIC overstates this summary. Correct the source-subject problem separately;
    broad mediates outputs alone do not show the cited mechanisms.
  evidence_ids:
  - record
  - schema
  - linc-agent-fan2020-jats
  - linc-agent-moiseeva2017-jats
  - linc-agent-yoshida2013-jats
- assessment_id: provenance
  area: provenance
  topic: Current source tiers and original access receipts
  outcome: supported
  target_ids:
  - GO:1990612
  summary: Native identities, primary JATS bodies and Chikashige abstract were read
    at the listed locators. The2012 Kms1 topology statement is background within a
    primary Hrs1 paper. The Chikashige API200 is metadata-only and its failed routes
    are retained. Original copied timestamps/hashes remain unchanged. Historical access
    notes are not findings.
  evidence_ids:
  - linc-agent-epmc
  - linc-agent-2012-meta
  - linc-agent-doi-j.cell.2006.01.048-meta
  - linc-agent-chikashige2006-api
  - linc-agent-fan2020-jats
  - linc-agent-amelina2015-jats
  - linc-agent-csm2020-jats
  - linc-agent-jimenez2025-jats
  - linc-agent-tanaka2012-pdf
  - linc-agent-dsb-meta
  - record
- assessment_id: completeness
  area: completeness
  topic: Bounded follow-up for named DSB and meiotic contexts
  outcome: supported
  target_ids:
  - GO:1990612
  summary: The existing DSB definition has direct source support in Swartz2014 and
    should remain distinct from the meiotic bouquet extensions. Future curation can
    represent that role with its S/G2/repair-choice limits rather than borrowing the
    budding-yeast conversion assay. No optional-empty image, property, protein-family
    or component finding is asserted; there are no dependent local-neighbor records.
  evidence_ids:
  - record
  - policy
  - linc-agent-go
  - linc-agent-swartz2014-jats
findings:
- finding_id: F1
  issue_key: sad1-kms1-fungal-linc-scope-transfer
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Budding-yeast assays and broad fungal coupling are assigned to the named
    complex
  description: Fan2020 directly tests budding-yeast Mps2–Mps3–Csm4, while both Fan-only
    output edges use Sad1–Kms1 as their subject. The pairing description acknowledges
    budding yeast but that qualifier does not change the graph subject or make the
    result an assay of Sad1–Kms1. The Fungi COMMON note likewise generalizes this
    named assembly and dynein/microtubule coupling from fission yeast, despite the
    distinct actin-associated budding-yeast system. Separate comparative LINC context
    from functions/distribution of the named S. pombe assembly. This is not a claim
    that Sad1–Kms1 lacks telomere or recombination roles.
  target_ids:
  - GO:1990612
  field_paths:
  - functions[function_id=pairing_and_recombination]
  - functions[function_id=telomere_organization].evidence
  - causal_graphs[graph_id=sad1_kms1_linc_complex_mechanism].edges
  - taxonomic_distribution[0]
  evidence_ids:
  - record
  - linc-agent-fan2020-jats
  - linc-agent-csm2020-jats
  - linc-agent-doi-j.cell.2006.01.048-meta
  - linc-agent-yoshida2013-jats
  - linc-agent-swartz2014-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained scientific record
  rule_id: review-checklist:Taxonomic scope and Evidence standard; docs/CURATION.md:Evidence
  native_severity: major
  normalization_reason: Major because the molecular subject and taxonomic/motor scope
    of existing causal assignments exceed their direct evidence; this is more than
    an imprecise citation label. Exact named identity and the native parent remain
    valid.
- finding_id: F2
  issue_key: sad1-kms1-summary-graph-overstates-mechanistic-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Membership and functional outputs are labeled mechanistic
  description: The seven-node graph presents membership/association and whole-complex
    outputs, without a represented chain explaining how the LINC bridge produces those
    outcomes. Retain FUNCTION but use honest NONMECHANISTIC scope with notes, or add
    independently supported causal intermediates and exact edge evidence during authorized
    curation. This classification issue is separate from the cross-species assignment
    in F1.
  target_ids:
  - GO:1990612
  field_paths:
  - causal_graphs[graph_id=sad1_kms1_linc_complex_mechanism].scope_status
  - causal_graphs[graph_id=sad1_kms1_linc_complex_mechanism].description
  - causal_graphs[graph_id=sad1_kms1_linc_complex_mechanism].edges
  evidence_ids:
  - record
  - schema
  - linc-agent-yoshida2013-jats
  - linc-agent-moiseeva2017-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained scientific record
  rule_id: src/cellstructuremech/schema/cellstructuremech.yaml:CausalGraphScopeEnum;
    review-checklist:Causal graph
  native_severity: minor
  normalization_reason: Minor because supported membership and bounded functional
    associations can remain after scope correction; the graph representation omits
    explanatory steps without independently inventing a new molecular mechanism.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990612
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained scientific record
  description: During authorized curation, bind named Sad1–Kms1 functions and edges
    to appropriate fission-yeast primary passages. Retain Fan/Lee findings only as
    explicitly comparative budding-yeast context, with their actual molecular subject.
    Narrow distribution to evidenced named-complex scope and distinguish conserved
    LINC architecture from motor/taxon generalizations.
  acceptance_checks:
  - Every resulting causal edge must have the same molecular subject and organism
    as its cited assay; retain SK1/S288C versus fission-yeast distinctions.
  - Preserve supported S/G2 DSB and meiotic telomere roles without claiming that Swartz
    mitotic gene conversion is the same assay as Fan meiotic conversion.
  - Do not infer COMMON exact-subunit distribution or dynein coupling from Fungi taxonomy
    or generic SUN-family conservation.
  - Run native schema/strict, protein verify/causal coverage, fresh CURIE/history
    and scientific edge review after an authorized validated-writer change.
  generator: Maintained YAML via guarded writer; no scientific edit is made by this
    review.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:1990612
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained scientific record
  description: Reclassify the current graph as NONMECHANISTIC functional context with
    scope notes, or build a supported mechanistic chain. Distinguish direct localization/depletion
    results from proposed motor cross-linking, force transmission and CDK/Sad1 pathways.
  acceptance_checks:
  - Read each new intermediate and edge against its exact primary result or explicitly
    labeled model passage.
  - Preserve species, meiosis versus mitosis, preparation and mutant-background bounds.
  - Recheck graph_kind/scope_status and run focused native validators; preserve PROPOSED
    status and history unless separately authorized.
  generator: Maintained YAML graph; derived products only after authorized curation.
limitations:
- The exact target resolver slice is derived from the completed fresh-base run. Any
  PMID transport failures were checked against the separately cited native literature
  metadata; these identity checks do not establish full-body scientific support.
- Chikashige2006 is abstract-only in this source packet. Native publisher403, attempted
  PDF404 and API200 coredata-only responses are retained. Body-level experimental-stock
  and domain-detail claims are not inferred from the abstract.
- Primary body text and claim-bearing captions/methods were read at listed locators.
  Image pixels, original videos, raw mass spectra and complete supplementary experimental-stock
  tables were not independently reanalyzed. The record has no image asset requiring
  visual/license review.
- Four972h- protein entries are reference-sequence examples, not exact experimental
  strains. Fan meiotic SK1 and mitotic S288C, fission-yeast h90/temperature-sensitive/engineered
  backgrounds, and2025 mitotic partial recruitment remain distinct.
- ESSENTIAL retains its exact schema assembly meaning. Functional perturbation, gene
  viability and localization data do not supply a complete assembly necessity test
  for each core subunit; this uncertainty is not converted into an opposite essentiality
  finding.
- Kms2 localization at meiotic telocentrosomes and its absence from detected MMS foci
  apply to different contexts. Possible partial redundancy and low-copy detection
  limits remain open; no fixed three-subunit stoichiometry or global absence is asserted.
- Funaya2012 main-body source is JATS despite local tanaka2012-pdf filename; author/title/format
  were verified. Its introductory bridge account is prior-study context, while its
  own direct assays concern Hrs1/rMTOC behavior.
- All14 native repository inputs retain their inspected hashes. External source receipts
  preserve actual HTTP statuses and original UTCZ times; no browser extraction is
  represented as an HTTP attestation.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Root owns finalization/save after fresh global checks. No maintained scientific
  record, shared index, Git state or generated product was changed.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
