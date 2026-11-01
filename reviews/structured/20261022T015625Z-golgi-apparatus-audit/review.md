# Golgi apparatus identity, source and topology review

- Review: 20261022T015625Z-golgi-apparatus-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:39:15Z
- Finished UTC: 2026-10-22T01:56:25Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One bounded minor source-attribution finding; Golgi identity, representative protein identities and observed yeast cisternal maturation remain supported.

## Scope And Provenance

Entire single target: exact identity, structure/material boundaries, source and taxonomic claims, examples, functions and every graph edge.

Selection: Target 2 of batch thirty in strict uncovered path order from fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005794 | data/structures/membrane_organelle/golgi_apparatus.yaml | maintained | Golgi apparatus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0005794 | Focused native check passed; biological source scope reviewed separately. |
| Native protein causal-graphs | passed | True | GO:0005794 | Focused native check passed; biological source scope reviewed separately. |
| Focused native schema | passed | True | GO:0005794 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005794 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005794 | No expression-module dataset or inference is used. Physical topology, native protein identities and microscopy/transport sources are applicable. |
| Claim-level scientific review | passed | True | GO:0005794 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005794 | 16 of 19 collected target identifiers returned OK. PMID:14676282: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID14676282, DOI10.1242/jcs.00858 and Activity of recycling Golgi mannosyltransferases in the yeast endoplasmic reticulum. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented source inspections. The Lindmark1973 source is bibliographic metadata only; no abstract or body was provided.; PMID:15229219: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID15229219, DOI10.1074/jbc.m405500200 and Retrograde transport of the mannosyltransferase Och1p to the early Golgi requires a component of the COG transport complex. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented source inspections. The Lindmark1973 source is bibliographic metadata only; no abstract or body was provided.; PMID:1628616: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID1628616, DOI10.1002/j.1460-2075.1992.tb05316.x and OCH1 encodes a novel membrane bound mannosyltransferase: outer chain elongation of asparagine-linked oligosaccharides. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented source inspections. The Lindmark1973 source is bibliographic metadata only; no abstract or body was provided. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005794 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005794 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005794 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005794 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005794 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Two broad machinery cohorts and six exact exemplars

grounding: concern. Targets: GO:0005794.

The two ASSOCIATED_MACHINERY cohorts span distinct proteins and are appropriately label-only with UNKNOWN formation necessity. All six reviewed accessions/gene/strain pairs and bounded uniqueness queries match. Native functions and locations support the general enzyme/SNARE context, but the Papanikou-specific attribution for SNARE pairing/cycling needs correction. The cohort is not asserted to be one stoichiometric complex.

### Exact structure and mereology

identity: supported. Targets: GO:0005794.

Native GO definitions distinguish the whole Golgi apparatus and its cisternal/membrane parts. Recorded synonyms and broader class/parthood statements agree with the inspected authority definitions and relations.

### Saccharomyces example and experimental boundaries

scope: supported. Targets: GO:0005794.

Species4932 is exact. Both imaging papers directly observe budding-yeast cisternal marker changes. Unstacked yeast cisternae, microscopy conditions and mutant effects are not generalized to all eukaryotic architecture. COMMON remains qualitative occurrence.

### Compartment role and bounded functional evidence

evidence: supported. Targets: GO:0005794.

GO and the review support glycan processing/sorting; both primary imaging papers support the specifically yeast-scoped early-to-late maturation description. Direct cargo tracking and a complete determinant mechanism are not asserted.

### All target graph edges

graph: concern. Targets: GO:0005794.

Five NONMECHANISTIC edges distinguish topology, observed maturation and resident enzymes. The SNARE-support edge requires corrected source placement as inF1; broad function is not rejected.

### Molecular requirements and complete inventories

evidence: unknown. Targets: GO:0005794.

An exact lipid composition, exhaustive machinery inventory and molecular formation-necessity tests are not established by these sources. Native protein identity and generic function annotations are distinguished from direct localization assays and from cisternal-maturation experiments.

### All maintained fields and bounded source tiers

completeness: supported. Targets: GO:0005794.

Full target, every graph edge, discussion and history entry were read. No maintained image asset, numeric physical property, trait link or verbatim snippet is asserted. PROPOSED status is retained. Empty optional slots and inaccessible bodies alone are not findings.

## Findings

### F1: Correct the source attribution for SNARE pairing and cycling

minor / open / confirmed; issue key: golgi-apparatus-snare-review-attribution.

The component note, graph-edge note and discussion attribute SNARE pairing/cycling to Papanikou and Glick2014. Its complete main text reviews compartment traffic, coats, tethers and GTPases but does not supply those SNARE-specific statements. Native SED5/TLG2/SEC22 entries and the already cited imaging papers support relevant SNARE context, so this is a bounded source-placement problem rather than a claim that these proteins have no Golgi role.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, remove the inaccurate Papanikou-specific SNARE wording and attach directly inspected evidence to the exact SNARE traffic or maturation assertion, or narrow that assertion to the support actually available. Retain broad machinery scope and avoid implying that all three examples form one complex.

- Re-read each revised source at the exact component/edge/discussion placement.
- Preserve the directly observed yeast marker-maturation scope and reference-strain identity distinction.
- Run focused schema, strict and relevant native graph/protein checks after curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/golgi_apparatus.yaml; Entire maintained target, including all examples, evidence, graph edges, discussions and history | context_only | Full target read; no scientific record, native status, history or generated page is edited. |
| policy | docs/CURATION.md; Exact structure identity, hierarchy/parthood and narrow source support | context_only | Whole apparatus, individual cisterna, enclosing bilayer and internal volume are separate identities. A source for general trafficking does not establish every named molecular mechanism. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent and ProteinExample definitions, essentiality and graph representation | context_only | Protein examples identify taxon-paired instances; membership and formation necessity need separate evidence. Label-only collective lipid material is not an exact whole-membrane molecular grounding. |
| root30-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005794,GO:0043231,GO:0012505,GO:0000139,GO:0031985,GO:0032580,GO:0005796,GO:0070013,GO:0016020,GO:0030126,GO:0035964; Complete native definitions, names, synonyms, active flags and all returned child relations for eleven identifiers | supports | All eleven active native GO terms were read. Whole GO0005794 is a membrane-bounded organelle and part of the endomembrane system; its exact Golgi complex synonym and membrane/lumen children agree. GO0031985 is the bounded cisterna, GO0032580 its membrane, GO0005796 the internal volume, and GO0000139 the general Golgi membrane. GO0070013 directly lists the lumen as an is_a child. GO0030126 identifies COPI coat and GO0035964 defines budding as Golgi membrane evagination. |
| root30-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank, lineage and otherNames | supports | ENA4932 is Saccharomyces cerevisiae at species rank. Qualitative occurrence does not measure population prevalence or prove an exact experimental strain. |
| root30-sources-losev2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1038/nature04717%22; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID16699524, DOI10.1038/nature04717, Golgi maturation visualized in living yeast., Losev E, Reinke CA, Jellen J, Strongin DE, Bevis BJ, Glick BS.. Complete primary abstract reports time-resolved yeast cisternal marker changes and comparison with secretory-cargo pulse-chase kinetics. Actual marker and imaging conditions are checked in the primary body. |
| root30-sources-matsuura2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1038/nature04737%22; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID16699523, DOI10.1038/nature04737, Live imaging of yeast Golgi cisternal maturation., Matsuura-Tokita K, Takeuchi M, Ichihara A, Mikuriya K, Nakano A.. Complete primary abstract reports high-speed3D microscopy of changing yeast cisternal membrane-protein distribution. It does not establish a universal mechanism for all eukaryotes. |
| root30-sources-papanikou2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/j.ceb.2014.04.010%22; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID24840895, DOI10.1016/j.ceb.2014.04.010, Golgi compartmentation and identity., Papanikou E, Glick BS.. Review abstract proposes three maturation stages with distinct membrane traffic and Rab/Arf coordination. This is synthesis and a model, not a newly inspected primary experiment. |
| root30-sources-karhinen2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A14676282%20AND%20SRC%3AMED; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID14676282, DOI10.1242/jcs.00858, Activity of recycling Golgi mannosyltransferases in the yeast endoplasmic reticulum., Karhinen L, Makarow M.. Complete primary abstract reports Och1 accumulation and activity in the ER when ER export was blocked in COPII mutants, with recycling experiments. This is conditional ER localization of a Golgi enzyme, not evidence that it never resides in Golgi. |
| root30-sources-nakayama1992-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A1628616%20AND%20SRC%3AMED; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID1628616, DOI10.1002/j.1460-2075.1992.tb05316.x, OCH1 encodes a novel membrane bound mannosyltransferase: outer chain elongation of asparagine-linked oligosaccharides., Nakayama K, Nagasu T, Shimma Y, Kuromitsu J, Jigami Y.. Complete primary abstract reports OCH1 cloning, the mutant outer-chain phenotype, type-II topology with the large C-terminal region on the lumenal side of microsomal membranes, and mannosyltransferase activity. No individual original microscopy image or scanned full body is claimed. |
| root30-sources-bruinsma2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15229219%20AND%20SRC%3AMED; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID15229219, DOI10.1074/jbc.m405500200, Retrograde transport of the mannosyltransferase Och1p to the early Golgi requires a component of the COG transport complex., Bruinsma P, Spelbrink RG, Nothwehr SF.. Complete primary abstract reports Och1/Mnn1 mislocalization in cog3-202 cells and retrograde Och1 cycling, including sed5/sft1 vesicle accumulation. Intra-Golgi cycling and degradation itineraries are distinguished from permanent residence. |
| root30-sources-losev2006-pdf | https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized-Nature-2006.pdf; Genuine primary PDF mirrored by Kanazawa University; full main text pp1002–1005, Methods and included captions. Reference-only page1006 not used to infer unread experiments. No figure pixels or movie/supplement inspection. | supports | Complete main article pp1002–1005 including Fig1–4 captions and Methods read. Sec7/Vrg4 and additional markers undergo transient labeling; early-to-late transitions and pulse-chase kinetics support cisternal maturation. Cells were imaged at23C; only individually resolved cisternae were quantified. The paper leaves exact recycling pathways and direct cargo tracking for future work. It discusses possible COPI recycling of some SNAREs, which is not the same as measuring every named SNARE role. |
| root30-sources-matsuura2006-pdf | https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized(2)-Nature-2006.pdf; Genuine primary PDF mirrored by Kanazawa University; complete main text and Methods, included Fig1–4 captions; no original pixels, videos or separate supplements. | supports | Complete main article pp1007–1009 plus Methods continuation on1010 read with Fig1–4 captions. Rer1/Gos1 and Sed5/Sec7 fusion-marker changes support yeast maturation; ret1-1 slowed but did not abolish transitions at37C. Functional fusion controls, spatial overlap limits and alternative membrane-transfer mechanisms are retained. No absence of Golgi formation is inferred from coat mutants. |
| root30-sources-papanikou2014-pmc | https://pmc.ncbi.nlm.nih.gov/articles/4130901/; Genuine PMC4130901 numeric-URL body, complete main sectionsS1–S7 and embedded captions; no figure pixels or underlying primary datasets | supports | Complete review main sectionsS1–S7 including Fig1/2 captions read. Supports compartmental enzyme processing, vesicle/tubule traffic and ARF-dependent coat recruitment; three-stage maturation is a proposed organizing model. S4 explicitly leaves aspects of COPI cargo/directionality unresolved. The main text does not discuss SNARE pairing/cycling or the exact SED5/TLG2/SEC22 cohort; its general traffic synthesis cannot be attributed those specific statements. |
| root30-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Exact taxon ID, name, rank and lineage | supports | ENA559292 is Saccharomyces cerevisiae S288C at strain rank, distinct from species4932. Reference-strain protein metadata are not relabeled as the experimental genotype in the imaging papers. |
| root30-sources-protein-P31755 | https://rest.uniprot.org/uniprotkb/P31755.json; Primary accession, entryType, proteinDescription, genes, organism and complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Exact reviewed accessionP31755, primary geneOCH1, taxon559292 and protein nameInitiation-specific alpha-1,6-mannosyltransferase agree. Native ER-membrane ECO0000269 citations14676282/1628616 and Golgi-membrane citation15229219 match all three target attributions. Native Golgi location also has additional citations, not a contradiction. Recycling is explicitly noted. |
| root30-sources-query-OCH1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3AOCH1%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue; Literal query and complete result list, including primary and synonym gene tokens | supports | Complete gene_exact:OCH1, taxonomy_id:559292, reviewed:true query returns exactly P31755. The bounded uniqueness claim matches; no other-taxon uniqueness or biological necessity is inferred. |
| root30-sources-protein-P39106 | https://rest.uniprot.org/uniprotkb/P39106.json; Primary accession, entryType, proteinDescription, genes, organism and complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Exact reviewed accessionP39106, primary geneMNN1, taxon559292 and protein nameAlpha-1,3-mannosyltransferase MNN1 agree. Native function describes terminal mannosylation; Golgi membrane localization is ECO0000305 curation, not an independently inspected microscopy experiment. |
| root30-sources-query-MNN1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3AMNN1%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue; Literal query and complete result list, including primary and synonym gene tokens | supports | Complete gene_exact:MNN1, taxonomy_id:559292, reviewed:true query returns exactly P39106. The bounded uniqueness claim matches; no other-taxon uniqueness or biological necessity is inferred. |
| root30-sources-protein-P27809 | https://rest.uniprot.org/uniprotkb/P27809.json; Primary accession, entryType, proteinDescription, genes, organism and complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Exact reviewed accessionP27809, primary geneKRE2, taxon559292 and protein nameGlycolipid2-alpha-mannosyltransferase agree. KRE2/MNT1 native function and Golgi membrane localization support glycosylation context; no individual experimental localization citation is attached to that location comment. |
| root30-sources-query-KRE2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3AKRE2%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue; Literal query and complete result list, including primary and synonym gene tokens | supports | Complete gene_exact:KRE2, taxonomy_id:559292, reviewed:true query returns exactly P27809. The bounded uniqueness claim matches; no other-taxon uniqueness or biological necessity is inferred. |
| root30-sources-protein-Q01590 | https://rest.uniprot.org/uniprotkb/Q01590.json; Primary accession, entryType, proteinDescription, genes, organism and complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Exact reviewed accessionQ01590, primary geneSED5, taxon559292 and protein nameIntegral membrane protein SED5 agree. Native function identifies an ER-to-Golgi t-SNARE and Golgi membrane location. Native SUBUNIT partners are distinct from an assertion that the entire three-example cohort forms one complex. |
| root30-sources-query-SED5 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3ASED5%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue; Literal query and complete result list, including primary and synonym gene tokens | supports | Complete gene_exact:SED5, taxonomy_id:559292, reviewed:true query returns exactly Q01590. The bounded uniqueness claim matches; no other-taxon uniqueness or biological necessity is inferred. |
| root30-sources-protein-Q08144 | https://rest.uniprot.org/uniprotkb/Q08144.json; Primary accession, entryType, proteinDescription, genes, organism and complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Exact reviewed accessionQ08144, primary geneTLG2, taxon559292 and protein namet-SNARE affecting a late Golgi compartment protein2 agree. Native function specifies endosome-to-late-Golgi traffic and localization to TGN/endosome membranes. This is compatible with associated trafficking machinery, not a permanent constituent of every cisterna. |
| root30-sources-query-TLG2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3ATLG2%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue; Literal query and complete result list, including primary and synonym gene tokens | supports | Complete gene_exact:TLG2, taxonomy_id:559292, reviewed:true query returns exactly Q08144. The bounded uniqueness claim matches; no other-taxon uniqueness or biological necessity is inferred. |
| root30-sources-protein-P22214 | https://rest.uniprot.org/uniprotkb/P22214.json; Primary accession, entryType, proteinDescription, genes, organism and complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Exact reviewed accessionP22214, primary geneSEC22, taxon559292 and protein nameProtein transport protein SEC22 agree. Native function describes nonessential ER/Golgi anterograde and retrograde SNARE activity; SUBUNIT describes two different complexes and possible YKT6 substitution. Individual survival or formation essentiality is not inferred. |
| root30-sources-query-SEC22 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3ASEC22%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue; Literal query and complete result list, including primary and synonym gene tokens | supports | Complete gene_exact:SEC22, taxonomy_id:559292, reviewed:true query returns exactly P22214. The bounded uniqueness claim matches; no other-taxon uniqueness or biological necessity is inferred. |
| snare-attribution-search | rg --no-ignore --hidden -in SNARE&#124;SED5&#124;TLG2&#124;SEC22 /private/tmp/cellstructure-batch30-20261022-frro2xh0/root30-sources/papanikou2014-main.txt; Complete primary-body-derived main text sectionsS1–S7 | refutes | Ignored-inclusive explicit-file search for SNARE,SED5,TLG2,SEC22 returned no matches in the complete reviewed main text. Manual reading independently confirms the source centers on coats, tethers and GTPases rather than the claimed SNARE cycling. This is source-specific, not a claim that SNARE biology or other supporting papers are absent. |
| native-verify | /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml --verify; Entire retained native focused output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml --causal-graphs; Entire retained native focused output | supports | data/structures/membrane_organelle/golgi_apparatus.yaml  (GO:0005794)<br>  yeast_golgi_cisternal_maturation	golgi_snare_trafficking_machinery	COVERED	-&gt;golgi_snare_trafficking_machinery (UniProtKB:Q01590, UniProtKB:Q08144, UniProtKB:P22214)<br>  yeast_golgi_cisternal_maturation	golgi_glycosylation_enzymes	COVERED	-&gt;golgi_glycosylation_enzymes (UniProtKB:P31755, UniProtKB:P39106, UniProtKB:P27809)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/golgi_apparatus.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/golgi_apparatus.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/golgi_apparatus.yaml --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_apparatus-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/golgi_apparatus.yaml --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_apparatus-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_apparatus-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/golgi_apparatus.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 16 of 19 collected target identifiers returned OK. PMID:14676282: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID14676282, DOI10.1242/jcs.00858 and Activity of recycling Golgi mannosyltransferases in the yeast endoplasmic reticulum. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented source inspections. The Lindmark1973 source is bibliographic metadata only; no abstract or body was provided.; PMID:15229219: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID15229219, DOI10.1074/jbc.m405500200 and Retrograde transport of the mannosyltransferase Och1p to the early Golgi requires a component of the COG transport complex. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented source inspections. The Lindmark1973 source is bibliographic metadata only; no abstract or body was provided.; PMID:1628616: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID1628616, DOI10.1002/j.1460-2075.1992.tb05316.x and OCH1 encodes a novel membrane bound mannosyltransferase: outer chain elongation of asparagine-linked oligosaccharides. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented source inspections. The Lindmark1973 source is bibliographic metadata only; no abstract or body was provided. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- COMMON denotes qualitative occurrence rather than measured prevalence. Reference-strain protein metadata do not prove that original experiments used that exact strain. Historical authorship and prior issue dispositions are not independently recertified.
- Losev2006 main pp1002–1005/Methods and Matsuura-Tokita2006 main pp1007–1009/Methods continuation1010 were read as genuine primary PDFs, including captions. Figure pixels, movies and separate supplements were not inspected; observed marker exchange does not uniquely establish every cargo-transfer/recycling mechanism.
- Papanikou/Glick2014 is a review; complete mainS1–S7 and embedded captions were inspected, without underlying primary datasets or figure pixels. Its three-stage model and unresolved trafficking questions remain qualified.
- Karhinen2004, Nakayama1992 and Bruinsma2004 were read as complete primary abstracts only. Exact OCH1 location/ECO/PMID attribution was independently checked in native UniProt. The attempted Nakayama PDF returned a browser challenge despite HTTP200 and is not treated as full text.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes review bundles for every uncovered record, including honest no-finding reviews. Maintained scientific content remains unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T015625Z-golgi-apparatus-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Golgi apparatus identity, source and topology review
started_at: '2026-10-22T01:39:15Z'
finished_at: '2026-10-22T01:56:25Z'
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
summary: One bounded minor source-attribution finding; Golgi identity, representative
  protein identities and observed yeast cisternal maturation remain supported.
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
  - path: data/structures/membrane_organelle/golgi_apparatus.yaml
    sha256: b064dc1116ec2814e2ecb946d8ebd554a4b176494c2259ff7e458bac0d3e5eb1
    role: target
  - path: data/structures/membrane_organelle/golgi_cisterna.yaml
    sha256: 09ebdf2a8646a8f51638cd933e9523e9e9170e0610567ad3e09efa7a97c6de7a
    role: context
  - path: data/structures/membrane_organelle/golgi_lumen.yaml
    sha256: 609cac48e5a5d75c55ed731b281a531dbe76e9db2ad105b228f17194399f608b
    role: context
  - path: data/structures/membrane_organelle/golgi_membrane.yaml
    sha256: 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c
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
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0005794
  path: data/structures/membrane_organelle/golgi_apparatus.yaml
  label: Golgi apparatus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_apparatus.yaml
    role: maintained scientific record
scope:
  description: 'Entire single target: exact identity, structure/material boundaries,
    source and taxonomic claims, examples, functions and every graph edge.'
  selection: Target 2 of batch thirty in strict uncovered path order from fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005794
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; biological source scope reviewed separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; biological source scope reviewed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: just validate data/structures/membrane_organelle/golgi_apparatus.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: just validate-strict data/structures/membrane_organelle/golgi_apparatus.yaml
    --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_apparatus-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005794
  summary: No expression-module dataset or inference is used. Physical topology, native
    protein identities and microscopy/transport sources are applicable.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005794
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - schema
  - root30-sources-go
  - root30-sources-tax4932
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-papanikou2014-meta
  - root30-sources-karhinen2004-meta
  - root30-sources-nakayama1992-meta
  - root30-sources-bruinsma2004-meta
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
  - root30-sources-tax559292
  - root30-sources-protein-P31755
  - root30-sources-query-OCH1
  - root30-sources-protein-P39106
  - root30-sources-query-MNN1
  - root30-sources-protein-P27809
  - root30-sources-query-KRE2
  - root30-sources-protein-Q01590
  - root30-sources-query-SED5
  - root30-sources-protein-Q08144
  - root30-sources-query-TLG2
  - root30-sources-protein-P22214
  - root30-sources-query-SEC22
  - snare-attribution-search
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005794
  summary: '16 of 19 collected target identifiers returned OK. PMID:14676282: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID14676282, DOI10.1242/jcs.00858 and Activity of recycling Golgi mannosyltransferases
    in the yeast endoplasmic reticulum. Bibliographic identity is resolved; scientific
    scope remains restricted to the separately documented source inspections. The
    Lindmark1973 source is bibliographic metadata only; no abstract or body was provided.;
    PMID:15229219: UNREACHABLE; The bulk PMID transport returned414; the independently
    retrieved exact MED record verifies PMID15229219, DOI10.1074/jbc.m405500200 and
    Retrograde transport of the mannosyltransferase Och1p to the early Golgi requires
    a component of the COG transport complex. Bibliographic identity is resolved;
    scientific scope remains restricted to the separately documented source inspections.
    The Lindmark1973 source is bibliographic metadata only; no abstract or body was
    provided.; PMID:1628616: UNREACHABLE; The bulk PMID transport returned414; the
    independently retrieved exact MED record verifies PMID1628616, DOI10.1002/j.1460-2075.1992.tb05316.x
    and OCH1 encodes a novel membrane bound mannosyltransferase: outer chain elongation
    of asparagine-linked oligosaccharides. Bibliographic identity is resolved; scientific
    scope remains restricted to the separately documented source inspections. The
    Lindmark1973 source is bibliographic metadata only; no abstract or body was provided.
    Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root30-sources-karhinen2004-meta
  - root30-sources-bruinsma2004-meta
  - root30-sources-nakayama1992-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005794
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
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_apparatus.yaml
  locator: Entire maintained target, including all examples, evidence, graph edges,
    discussions and history
  accessed_at: '2026-10-22T01:48:38Z'
  support: context_only
  summary: Full target read; no scientific record, native status, history or generated
    page is edited.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact structure identity, hierarchy/parthood and narrow source support
  accessed_at: '2026-10-22T01:48:38Z'
  support: context_only
  summary: Whole apparatus, individual cisterna, enclosing bilayer and internal volume
    are separate identities. A source for general trafficking does not establish every
    named molecular mechanism.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent and ProteinExample definitions, essentiality and graph
    representation
  accessed_at: '2026-10-22T01:48:38Z'
  support: context_only
  summary: Protein examples identify taxon-paired instances; membership and formation
    necessity need separate evidence. Label-only collective lipid material is not
    an exact whole-membrane molecular grounding.
- evidence_id: root30-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005794,GO:0043231,GO:0012505,GO:0000139,GO:0031985,GO:0032580,GO:0005796,GO:0070013,GO:0016020,GO:0030126,GO:0035964
  locator: Complete native definitions, names, synonyms, active flags and all returned
    child relations for eleven identifiers
  accessed_at: '2026-10-22T01:41:10.238173Z'
  support: supports
  summary: All eleven active native GO terms were read. Whole GO0005794 is a membrane-bounded
    organelle and part of the endomembrane system; its exact Golgi complex synonym
    and membrane/lumen children agree. GO0031985 is the bounded cisterna, GO0032580
    its membrane, GO0005796 the internal volume, and GO0000139 the general Golgi membrane.
    GO0070013 directly lists the lumen as an is_a child. GO0030126 identifies COPI
    coat and GO0035964 defines budding as Golgi membrane evagination.
  snapshot_sha256: fb5e6b3a9919bf3958eff2c08470766c15c8c1bb4cfe3986d1b702863179c24e
- evidence_id: root30-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-22T01:10:58.502766Z'
  support: supports
  summary: ENA4932 is Saccharomyces cerevisiae at species rank. Qualitative occurrence
    does not measure population prevalence or prove an exact experimental strain.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root30-sources-losev2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/nature04717%22
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:41:12.606096Z'
  support: supports
  summary: Exact MED PMID16699524, DOI10.1038/nature04717, Golgi maturation visualized
    in living yeast., Losev E, Reinke CA, Jellen J, Strongin DE, Bevis BJ, Glick BS..
    Complete primary abstract reports time-resolved yeast cisternal marker changes
    and comparison with secretory-cargo pulse-chase kinetics. Actual marker and imaging
    conditions are checked in the primary body.
  snapshot_sha256: 438af45289e12594bc6c09b8fdcaf9ad230e1399908c29f79c7027d1503d5b5f
- evidence_id: root30-sources-matsuura2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/nature04737%22
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:41:12.638150Z'
  support: supports
  summary: Exact MED PMID16699523, DOI10.1038/nature04737, Live imaging of yeast Golgi
    cisternal maturation., Matsuura-Tokita K, Takeuchi M, Ichihara A, Mikuriya K,
    Nakano A.. Complete primary abstract reports high-speed3D microscopy of changing
    yeast cisternal membrane-protein distribution. It does not establish a universal
    mechanism for all eukaryotes.
  snapshot_sha256: 992411620c5017423ba1f32e69265c4da58b85823dcd9688b293efbb9dfb956e
- evidence_id: root30-sources-papanikou2014-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.ceb.2014.04.010%22
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:41:12.642065Z'
  support: supports
  summary: Exact MED PMID24840895, DOI10.1016/j.ceb.2014.04.010, Golgi compartmentation
    and identity., Papanikou E, Glick BS.. Review abstract proposes three maturation
    stages with distinct membrane traffic and Rab/Arf coordination. This is synthesis
    and a model, not a newly inspected primary experiment.
  snapshot_sha256: a69018a63680dbec1397a9dfbb42cf7d3c509b619af150fcc8a9e0f6273d4655
- evidence_id: root30-sources-karhinen2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A14676282%20AND%20SRC%3AMED
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:41:13.258604Z'
  support: supports
  summary: Exact MED PMID14676282, DOI10.1242/jcs.00858, Activity of recycling Golgi
    mannosyltransferases in the yeast endoplasmic reticulum., Karhinen L, Makarow
    M.. Complete primary abstract reports Och1 accumulation and activity in the ER
    when ER export was blocked in COPII mutants, with recycling experiments. This
    is conditional ER localization of a Golgi enzyme, not evidence that it never resides
    in Golgi.
  snapshot_sha256: e211a009225167a17126e3ea3abcc9018a024218a0b4d669fde3253e58423727
- evidence_id: root30-sources-nakayama1992-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A1628616%20AND%20SRC%3AMED
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:41:13.353971Z'
  support: supports
  summary: 'Exact MED PMID1628616, DOI10.1002/j.1460-2075.1992.tb05316.x, OCH1 encodes
    a novel membrane bound mannosyltransferase: outer chain elongation of asparagine-linked
    oligosaccharides., Nakayama K, Nagasu T, Shimma Y, Kuromitsu J, Jigami Y.. Complete
    primary abstract reports OCH1 cloning, the mutant outer-chain phenotype, type-II
    topology with the large C-terminal region on the lumenal side of microsomal membranes,
    and mannosyltransferase activity. No individual original microscopy image or scanned
    full body is claimed.'
  snapshot_sha256: 7f6af8fff08ae25d4a1a720dedf46ee9f2fb4043bb791a4433e880f0198063c9
- evidence_id: root30-sources-bruinsma2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15229219%20AND%20SRC%3AMED
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:41:13.366951Z'
  support: supports
  summary: Exact MED PMID15229219, DOI10.1074/jbc.m405500200, Retrograde transport
    of the mannosyltransferase Och1p to the early Golgi requires a component of the
    COG transport complex., Bruinsma P, Spelbrink RG, Nothwehr SF.. Complete primary
    abstract reports Och1/Mnn1 mislocalization in cog3-202 cells and retrograde Och1
    cycling, including sed5/sft1 vesicle accumulation. Intra-Golgi cycling and degradation
    itineraries are distinguished from permanent residence.
  snapshot_sha256: 3affd0b99c0a01fc036788eb31aada04e42f59a4d0b2e80148fd55a901e332b9
- evidence_id: root30-sources-losev2006-pdf
  kind: primary_source
  reference: https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized-Nature-2006.pdf
  locator: Genuine primary PDF mirrored by Kanazawa University; full main text pp1002–1005,
    Methods and included captions. Reference-only page1006 not used to infer unread
    experiments. No figure pixels or movie/supplement inspection.
  accessed_at: '2026-10-22T01:44:30.716438Z'
  support: supports
  summary: Complete main article pp1002–1005 including Fig1–4 captions and Methods
    read. Sec7/Vrg4 and additional markers undergo transient labeling; early-to-late
    transitions and pulse-chase kinetics support cisternal maturation. Cells were
    imaged at23C; only individually resolved cisternae were quantified. The paper
    leaves exact recycling pathways and direct cargo tracking for future work. It
    discusses possible COPI recycling of some SNAREs, which is not the same as measuring
    every named SNARE role.
  snapshot_sha256: 9cd6a98c307575ce19f0b88a5943b10dc7732d655c2b75a9d34228a4fbbc188f
- evidence_id: root30-sources-matsuura2006-pdf
  kind: primary_source
  reference: https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized(2)-Nature-2006.pdf
  locator: Genuine primary PDF mirrored by Kanazawa University; complete main text
    and Methods, included Fig1–4 captions; no original pixels, videos or separate
    supplements.
  accessed_at: '2026-10-22T01:45:15.447608Z'
  support: supports
  summary: Complete main article pp1007–1009 plus Methods continuation on1010 read
    with Fig1–4 captions. Rer1/Gos1 and Sed5/Sec7 fusion-marker changes support yeast
    maturation; ret1-1 slowed but did not abolish transitions at37C. Functional fusion
    controls, spatial overlap limits and alternative membrane-transfer mechanisms
    are retained. No absence of Golgi formation is inferred from coat mutants.
  snapshot_sha256: e0e393bc775432869db495e2a836df223a0be5128ab04aae51a9d31bbf323583
- evidence_id: root30-sources-papanikou2014-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4130901/
  locator: Genuine PMC4130901 numeric-URL body, complete main sectionsS1–S7 and embedded
    captions; no figure pixels or underlying primary datasets
  accessed_at: '2026-10-22T01:44:30.713167Z'
  support: supports
  summary: Complete review main sectionsS1–S7 including Fig1/2 captions read. Supports
    compartmental enzyme processing, vesicle/tubule traffic and ARF-dependent coat
    recruitment; three-stage maturation is a proposed organizing model. S4 explicitly
    leaves aspects of COPI cargo/directionality unresolved. The main text does not
    discuss SNARE pairing/cycling or the exact SED5/TLG2/SEC22 cohort; its general
    traffic synthesis cannot be attributed those specific statements.
  snapshot_sha256: cf70ce9e4c9463c83cad4d05b0c40de9f76ca35a3053d3e5a0c2e2b88dce846a
- evidence_id: root30-sources-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Exact taxon ID, name, rank and lineage
  accessed_at: '2026-10-22T01:10:58.507227Z'
  support: supports
  summary: ENA559292 is Saccharomyces cerevisiae S288C at strain rank, distinct from
    species4932. Reference-strain protein metadata are not relabeled as the experimental
    genotype in the imaging papers.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root30-sources-protein-P31755
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P31755.json
  locator: Primary accession, entryType, proteinDescription, genes, organism and complete
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-22T01:41:10.238744Z'
  support: supports
  summary: Exact reviewed accessionP31755, primary geneOCH1, taxon559292 and protein
    nameInitiation-specific alpha-1,6-mannosyltransferase agree. Native ER-membrane
    ECO0000269 citations14676282/1628616 and Golgi-membrane citation15229219 match
    all three target attributions. Native Golgi location also has additional citations,
    not a contradiction. Recycling is explicitly noted.
  snapshot_sha256: d9e08176a5ae755fb9f2e831db8e914751b10ccd12df96c404604bcbbc0c1666
- evidence_id: root30-sources-query-OCH1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3AOCH1%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue
  locator: Literal query and complete result list, including primary and synonym gene
    tokens
  accessed_at: '2026-10-22T01:41:11.140921Z'
  support: supports
  summary: Complete gene_exact:OCH1, taxonomy_id:559292, reviewed:true query returns
    exactly P31755. The bounded uniqueness claim matches; no other-taxon uniqueness
    or biological necessity is inferred.
  snapshot_sha256: 5c298b13b6c9d94db63caba59445b1eaaef38067995a0185d904ec30231ac69e
- evidence_id: root30-sources-protein-P39106
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39106.json
  locator: Primary accession, entryType, proteinDescription, genes, organism and complete
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-22T01:41:10.238796Z'
  support: supports
  summary: Exact reviewed accessionP39106, primary geneMNN1, taxon559292 and protein
    nameAlpha-1,3-mannosyltransferase MNN1 agree. Native function describes terminal
    mannosylation; Golgi membrane localization is ECO0000305 curation, not an independently
    inspected microscopy experiment.
  snapshot_sha256: 06df97f0147ff075bde02c34aa2a1f4ea35267ef88dc3c5b40fa7b885a692157
- evidence_id: root30-sources-query-MNN1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3AMNN1%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue
  locator: Literal query and complete result list, including primary and synonym gene
    tokens
  accessed_at: '2026-10-22T01:41:11.178127Z'
  support: supports
  summary: Complete gene_exact:MNN1, taxonomy_id:559292, reviewed:true query returns
    exactly P39106. The bounded uniqueness claim matches; no other-taxon uniqueness
    or biological necessity is inferred.
  snapshot_sha256: 5c0845db2c21c7f6eb20c6c0414a9b3541d56b12a058bd870e9b8f9019001938
- evidence_id: root30-sources-protein-P27809
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27809.json
  locator: Primary accession, entryType, proteinDescription, genes, organism and complete
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-22T01:41:10.238928Z'
  support: supports
  summary: Exact reviewed accessionP27809, primary geneKRE2, taxon559292 and protein
    nameGlycolipid2-alpha-mannosyltransferase agree. KRE2/MNT1 native function and
    Golgi membrane localization support glycosylation context; no individual experimental
    localization citation is attached to that location comment.
  snapshot_sha256: d9937a8a2c1e27de6fdfa747c81fd72399fd0d750110e39cd65fc3c8e2d6ae4c
- evidence_id: root30-sources-query-KRE2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3AKRE2%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue
  locator: Literal query and complete result list, including primary and synonym gene
    tokens
  accessed_at: '2026-10-22T01:41:11.740359Z'
  support: supports
  summary: Complete gene_exact:KRE2, taxonomy_id:559292, reviewed:true query returns
    exactly P27809. The bounded uniqueness claim matches; no other-taxon uniqueness
    or biological necessity is inferred.
  snapshot_sha256: cca74c6799561ef94fb7fa6734b44830e22fc10edcee3b241c4d7a8655ffc5cd
- evidence_id: root30-sources-protein-Q01590
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q01590.json
  locator: Primary accession, entryType, proteinDescription, genes, organism and complete
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-22T01:41:10.973892Z'
  support: supports
  summary: Exact reviewed accessionQ01590, primary geneSED5, taxon559292 and protein
    nameIntegral membrane protein SED5 agree. Native function identifies an ER-to-Golgi
    t-SNARE and Golgi membrane location. Native SUBUNIT partners are distinct from
    an assertion that the entire three-example cohort forms one complex.
  snapshot_sha256: 586b494279d831cbe36781c791833fd8b3f93022d69dc6872ed00753a71f4843
- evidence_id: root30-sources-query-SED5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3ASED5%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue
  locator: Literal query and complete result list, including primary and synonym gene
    tokens
  accessed_at: '2026-10-22T01:41:11.822273Z'
  support: supports
  summary: Complete gene_exact:SED5, taxonomy_id:559292, reviewed:true query returns
    exactly Q01590. The bounded uniqueness claim matches; no other-taxon uniqueness
    or biological necessity is inferred.
  snapshot_sha256: c501ae657b04d3b2311646ce8008d132de39cf5aa217c9c93c95ec878669ef78
- evidence_id: root30-sources-protein-Q08144
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08144.json
  locator: Primary accession, entryType, proteinDescription, genes, organism and complete
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-22T01:41:11.010973Z'
  support: supports
  summary: Exact reviewed accessionQ08144, primary geneTLG2, taxon559292 and protein
    namet-SNARE affecting a late Golgi compartment protein2 agree. Native function
    specifies endosome-to-late-Golgi traffic and localization to TGN/endosome membranes.
    This is compatible with associated trafficking machinery, not a permanent constituent
    of every cisterna.
  snapshot_sha256: 001ba611c8d23e65cf9d6665abaf092e799b3dedc8141843990f8a60a442499c
- evidence_id: root30-sources-query-TLG2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3ATLG2%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue
  locator: Literal query and complete result list, including primary and synonym gene
    tokens
  accessed_at: '2026-10-22T01:41:11.874394Z'
  support: supports
  summary: Complete gene_exact:TLG2, taxonomy_id:559292, reviewed:true query returns
    exactly Q08144. The bounded uniqueness claim matches; no other-taxon uniqueness
    or biological necessity is inferred.
  snapshot_sha256: 804ee1ab086ef0138ad3a6c861b568dfd39f0653348d51ecd05593ad222fdc50
- evidence_id: root30-sources-protein-P22214
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P22214.json
  locator: Primary accession, entryType, proteinDescription, genes, organism and complete
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-22T01:41:11.135152Z'
  support: supports
  summary: Exact reviewed accessionP22214, primary geneSEC22, taxon559292 and protein
    nameProtein transport protein SEC22 agree. Native function describes nonessential
    ER/Golgi anterograde and retrograde SNARE activity; SUBUNIT describes two different
    complexes and possible YKT6 substitution. Individual survival or formation essentiality
    is not inferred.
  snapshot_sha256: 259b6c9a371007a3b8942f52581ace55de61b0a721bc20799833d764de1d0c10
- evidence_id: root30-sources-query-SEC22
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3ASEC22%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue
  locator: Literal query and complete result list, including primary and synonym gene
    tokens
  accessed_at: '2026-10-22T01:41:12.119919Z'
  support: supports
  summary: Complete gene_exact:SEC22, taxonomy_id:559292, reviewed:true query returns
    exactly P22214. The bounded uniqueness claim matches; no other-taxon uniqueness
    or biological necessity is inferred.
  snapshot_sha256: 2f02196a0b43a4c1d97d3618433076a62c67a6538708bd3330f9ca0f186986a2
- evidence_id: snare-attribution-search
  kind: search
  reference: rg --no-ignore --hidden -in SNARE|SED5|TLG2|SEC22 /private/tmp/cellstructure-batch30-20261022-frro2xh0/root30-sources/papanikou2014-main.txt
  locator: Complete primary-body-derived main text sectionsS1–S7
  accessed_at: '2026-10-22T01:46:17.727442Z'
  support: refutes
  summary: Ignored-inclusive explicit-file search for SNARE,SED5,TLG2,SEC22 returned
    no matches in the complete reviewed main text. Manual reading independently confirms
    the source centers on coats, tethers and GTPases rather than the claimed SNARE
    cycling. This is source-specific, not a claim that SNARE biology or other supporting
    papers are absent.
  search_scope: All complete main-text sections S1–S7 including embedded captions
    in genuine PMC body, explicit file passed to rg --no-ignore --hidden; references
    and raw supplemental data excluded. This verifies source-specific attribution
    only, not absence of SNARE biology or a corpus-wide source.
  snapshot_sha256: 147016281af992c1c3a874dba01c8495aa42272e88873f7c20a3ff575ce0993e
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml
    --verify
  locator: Entire retained native focused output
  accessed_at: '2026-10-22T01:41:10.740505Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml
    --causal-graphs
  locator: Entire retained native focused output
  accessed_at: '2026-10-22T01:41:11.185737Z'
  support: supports
  summary: "data/structures/membrane_organelle/golgi_apparatus.yaml  (GO:0005794)\n\
    \  yeast_golgi_cisternal_maturation\tgolgi_snare_trafficking_machinery\tCOVERED\t\
    ->golgi_snare_trafficking_machinery (UniProtKB:Q01590, UniProtKB:Q08144, UniProtKB:P22214)\n\
    \  yeast_golgi_cisternal_maturation\tgolgi_glycosylation_enzymes\tCOVERED\t->golgi_glycosylation_enzymes\
    \ (UniProtKB:P31755, UniProtKB:P39106, UniProtKB:P27809)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     2  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: c43cea8c606cb2810b4f9b7c7a5c88f1dfd70ae0fb115897019bc9f86a673fad
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/golgi_apparatus.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:39:17Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/golgi_apparatus.yaml'
  snapshot_sha256: 4de0844a42ed9b4ea35f8e1012161fb02a1da7161dea111c4a6b1ac526e79b04
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/golgi_apparatus.yaml
    --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_apparatus-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:39:18Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/golgi_apparatus.yaml\
    \ --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_apparatus-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_apparatus-strict.tsv"
  snapshot_sha256: 53f2fd7697afb4ecd111816d8c6d026e69d467e3fb0119640349cc3bb8a8896e
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/golgi_apparatus.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '16 of 19 collected target identifiers returned OK. PMID:14676282: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID14676282, DOI10.1242/jcs.00858 and Activity of recycling Golgi mannosyltransferases
    in the yeast endoplasmic reticulum. Bibliographic identity is resolved; scientific
    scope remains restricted to the separately documented source inspections. The
    Lindmark1973 source is bibliographic metadata only; no abstract or body was provided.;
    PMID:15229219: UNREACHABLE; The bulk PMID transport returned414; the independently
    retrieved exact MED record verifies PMID15229219, DOI10.1074/jbc.m405500200 and
    Retrograde transport of the mannosyltransferase Och1p to the early Golgi requires
    a component of the COG transport complex. Bibliographic identity is resolved;
    scientific scope remains restricted to the separately documented source inspections.
    The Lindmark1973 source is bibliographic metadata only; no abstract or body was
    provided.; PMID:1628616: UNREACHABLE; The bulk PMID transport returned414; the
    independently retrieved exact MED record verifies PMID1628616, DOI10.1002/j.1460-2075.1992.tb05316.x
    and OCH1 encodes a novel membrane bound mannosyltransferase: outer chain elongation
    of asparagine-linked oligosaccharides. Bibliographic identity is resolved; scientific
    scope remains restricted to the separately documented source inspections. The
    Lindmark1973 source is bibliographic metadata only; no abstract or body was provided.
    Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
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
- assessment_id: composition
  area: grounding
  topic: Two broad machinery cohorts and six exact exemplars
  outcome: concern
  target_ids:
  - GO:0005794
  summary: The two ASSOCIATED_MACHINERY cohorts span distinct proteins and are appropriately
    label-only with UNKNOWN formation necessity. All six reviewed accessions/gene/strain
    pairs and bounded uniqueness queries match. Native functions and locations support
    the general enzyme/SNARE context, but the Papanikou-specific attribution for SNARE
    pairing/cycling needs correction. The cohort is not asserted to be one stoichiometric
    complex.
  evidence_ids:
  - record
  - schema
  - root30-sources-tax559292
  - root30-sources-protein-P31755
  - root30-sources-query-OCH1
  - root30-sources-protein-P39106
  - root30-sources-query-MNN1
  - root30-sources-protein-P27809
  - root30-sources-query-KRE2
  - root30-sources-protein-Q01590
  - root30-sources-query-SED5
  - root30-sources-protein-Q08144
  - root30-sources-query-TLG2
  - root30-sources-protein-P22214
  - root30-sources-query-SEC22
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-papanikou2014-meta
  - root30-sources-karhinen2004-meta
  - root30-sources-nakayama1992-meta
  - root30-sources-bruinsma2004-meta
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
  - snare-attribution-search
- assessment_id: identity
  area: identity
  topic: Exact structure and mereology
  outcome: supported
  target_ids:
  - GO:0005794
  summary: Native GO definitions distinguish the whole Golgi apparatus and its cisternal/membrane
    parts. Recorded synonyms and broader class/parthood statements agree with the
    inspected authority definitions and relations.
  evidence_ids:
  - record
  - policy
  - root30-sources-go
- assessment_id: scope
  area: scope
  topic: Saccharomyces example and experimental boundaries
  outcome: supported
  target_ids:
  - GO:0005794
  summary: Species4932 is exact. Both imaging papers directly observe budding-yeast
    cisternal marker changes. Unstacked yeast cisternae, microscopy conditions and
    mutant effects are not generalized to all eukaryotic architecture. COMMON remains
    qualitative occurrence.
  evidence_ids:
  - record
  - root30-sources-tax4932
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-papanikou2014-meta
  - root30-sources-karhinen2004-meta
  - root30-sources-nakayama1992-meta
  - root30-sources-bruinsma2004-meta
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
- assessment_id: function
  area: evidence
  topic: Compartment role and bounded functional evidence
  outcome: supported
  target_ids:
  - GO:0005794
  summary: GO and the review support glycan processing/sorting; both primary imaging
    papers support the specifically yeast-scoped early-to-late maturation description.
    Direct cargo tracking and a complete determinant mechanism are not asserted.
  evidence_ids:
  - record
  - root30-sources-go
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-papanikou2014-meta
  - root30-sources-karhinen2004-meta
  - root30-sources-nakayama1992-meta
  - root30-sources-bruinsma2004-meta
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
- assessment_id: graph
  area: graph
  topic: All target graph edges
  outcome: concern
  target_ids:
  - GO:0005794
  summary: Five NONMECHANISTIC edges distinguish topology, observed maturation and
    resident enzymes. The SNARE-support edge requires corrected source placement as
    inF1; broad function is not rejected.
  evidence_ids:
  - record
  - root30-sources-go
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-papanikou2014-meta
  - root30-sources-karhinen2004-meta
  - root30-sources-nakayama1992-meta
  - root30-sources-bruinsma2004-meta
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
- assessment_id: limits
  area: evidence
  topic: Molecular requirements and complete inventories
  outcome: unknown
  target_ids:
  - GO:0005794
  summary: An exact lipid composition, exhaustive machinery inventory and molecular
    formation-necessity tests are not established by these sources. Native protein
    identity and generic function annotations are distinguished from direct localization
    assays and from cisternal-maturation experiments.
  evidence_ids:
  - record
  - schema
  - root30-sources-go
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and bounded source tiers
  outcome: supported
  target_ids:
  - GO:0005794
  summary: Full target, every graph edge, discussion and history entry were read.
    No maintained image asset, numeric physical property, trait link or verbatim snippet
    is asserted. PROPOSED status is retained. Empty optional slots and inaccessible
    bodies alone are not findings.
  evidence_ids:
  - record
  - policy
  - root30-sources-go
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-papanikou2014-meta
  - root30-sources-karhinen2004-meta
  - root30-sources-nakayama1992-meta
  - root30-sources-bruinsma2004-meta
findings:
- finding_id: F1
  issue_key: golgi-apparatus-snare-review-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the source attribution for SNARE pairing and cycling
  description: The component note, graph-edge note and discussion attribute SNARE
    pairing/cycling to Papanikou and Glick2014. Its complete main text reviews compartment
    traffic, coats, tethers and GTPases but does not supply those SNARE-specific statements.
    Native SED5/TLG2/SEC22 entries and the already cited imaging papers support relevant
    SNARE context, so this is a bounded source-placement problem rather than a claim
    that these proteins have no Golgi role.
  target_ids:
  - GO:0005794
  field_paths:
  - components#golgi_snare_trafficking_machinery.evidence
  - causal_graphs#yeast_golgi_cisternal_maturation.edges
  - discussions#ground_golgi_resident_machinery.evidence
  evidence_ids:
  - record
  - snare-attribution-search
  - root30-sources-papanikou2014-pmc
  - root30-sources-tax559292
  - root30-sources-protein-P31755
  - root30-sources-query-OCH1
  - root30-sources-protein-P39106
  - root30-sources-query-MNN1
  - root30-sources-protein-P27809
  - root30-sources-query-KRE2
  - root30-sources-protein-Q01590
  - root30-sources-query-SED5
  - root30-sources-protein-Q08144
  - root30-sources-query-TLG2
  - root30-sources-protein-P22214
  - root30-sources-query-SEC22
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_apparatus.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level source support
  native_severity: minor
  normalization_reason: Bounded incorrect source attribution; organelle identity,
    observed yeast maturation and native protein identities remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005794
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_apparatus.yaml
    role: maintained scientific record
  description: In separately authorized curation, remove the inaccurate Papanikou-specific
    SNARE wording and attach directly inspected evidence to the exact SNARE traffic
    or maturation assertion, or narrow that assertion to the support actually available.
    Retain broad machinery scope and avoid implying that all three examples form one
    complex.
  acceptance_checks:
  - Re-read each revised source at the exact component/edge/discussion placement.
  - Preserve the directly observed yeast marker-maturation scope and reference-strain
    identity distinction.
  - Run focused schema, strict and relevant native graph/protein checks after curation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- COMMON denotes qualitative occurrence rather than measured prevalence. Reference-strain
  protein metadata do not prove that original experiments used that exact strain.
  Historical authorship and prior issue dispositions are not independently recertified.
- Losev2006 main pp1002–1005/Methods and Matsuura-Tokita2006 main pp1007–1009/Methods
  continuation1010 were read as genuine primary PDFs, including captions. Figure pixels,
  movies and separate supplements were not inspected; observed marker exchange does
  not uniquely establish every cargo-transfer/recycling mechanism.
- Papanikou/Glick2014 is a review; complete mainS1–S7 and embedded captions were inspected,
  without underlying primary datasets or figure pixels. Its three-stage model and
  unresolved trafficking questions remain qualified.
- Karhinen2004, Nakayama1992 and Bruinsma2004 were read as complete primary abstracts
  only. Exact OCH1 location/ECO/PMID attribution was independently checked in native
  UniProt. The attempted Nakayama PDF returned a browser challenge despite HTTP200
  and is not treated as full text.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorizes review bundles for every uncovered record, including
  honest no-finding reviews. Maintained scientific content remains unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
