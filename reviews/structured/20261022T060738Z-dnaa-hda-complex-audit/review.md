# Source-grounded review of DnaA-Hda complex

- Review: 20261022T060738Z-dnaa-hda-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:50:41Z
- Finished UTC: 2026-10-22T06:07:38Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major corrects an inherited phosphorylation-versus-hydrolysis definition error; one minor resolves exact DnaA/Hda families. Binary interaction, E.coli context and coarse negative-regulation graph remain supported.

## Scope And Provenance

Exactly one complete maintained target; source-specific native fields and literature reading scopes are given in evidence. Scientific inputs remain unchanged.

Selection: One complete record in strict-path batch52 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990083 | data/structures/other/dnaa_hda_complex.yaml | maintained | DnaA-Hda complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990083 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990083 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:1990083 | Focused check passed; source claims assessed separately. |
| Native focused verify | passed | True | GO:1990083 | Focused check passed; source claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:1990083 | No expression-module or transcriptomic claim requires this resource. |
| Claim-level scientific review | passed | True | GO:1990083 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990083 | 10 of 16 collected target identifiers returned OK. PMID:12618445: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:15150238: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:21708944: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:22574163: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:28166228: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:9478970: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990083 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990083 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990083 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990083 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990083 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Binary contact within the larger RIDA system

identity: supported. Targets: GO:1990083.

Exact DnaA-Hda identity and replication-inhibiting parentage are sound. Direct binding without the clamp supports the binary contact boundary; the efficient RIDA reaction also requires the DNA-loaded clamp context. Do not collapse this record into the separately named Hda-beta complex.

### Hydrolysis versus phosphorylation wording

evidence: concern. Targets: GO:1990083.

The maintained definition faithfully repeats native GO but incorrectly describes prevention of DnaA-ADP phosphorylation. The primary assay instead measures conversion of ATP-DnaA to ADP-DnaA by hydrolysis, and the target’s canonical note/final graph edge already use that chemistry. DARS reactivation proceeds by nucleotide exchange, not phosphorylation of DnaA-bound ADP.

### Two correct proteins with exact families

grounding: concern. Targets: GO:1990083.

Both K12 examples, source-scoped membership and localization annotations are correct. Exact class families are actionable; activity or viability is not a physical-formation requirement.

### Supported coarse negative-regulation graph

graph: supported. Targets: GO:1990083.

The two membership edges and final negative-regulation support edge correctly describe composition and ATP hydrolysis at a coarse level. NONMECHANISTIC scope preserves clamp context as outside the encoded detail; the definition chemistry, not the graph edge, needs correction.

### E.coli experiment versus reference entry

scope: supported. Targets: GO:1990083.

The study uses K12-derived strains and purified reconstitutions, supporting the named E.coli canonical example. Model geometry, residual binding and mutant phenotypes remain condition-scoped; the permissive cellular-organisms constraint is not a distribution claim.

### Constituent identity is not an absence assay

grounding: unknown. Targets: GO:1990083.

All component essentialities remain UNKNOWN. Direct binding, functional inhibition/stimulation and organism viability do not alone establish physical formation in every component-absence condition. No optional constituent inventory is invented.

### Whole maintained record and source boundaries

completeness: supported. Targets: GO:1990083.

Every maintained field, component/example, edge, discussion and history was read. Exact available mappings and substantive source conflicts are distinguished from optional enrichment and unresolved access limits. Historical deferral notes remain historical statements, not claims of fabrication.

## Findings

### F1: Correct the inherited RIDA chemistry

major / open / confirmed; issue key: dnaa-hda-definition-phosphorylation-versus-hydrolysis.

The definition says Hda inactivates DnaA by inhibiting phosphorylation of DnaA-ADP to DnaA-ATP. This matches current GO1990083 but conflicts with the cited Keyamura/Katayama2011 staged hydrolysis assay and the target’s own ATP-hydrolysis canonical/graph text. RIDA promotes hydrolysis of bound ATP; reactivation by DARS uses nucleotide exchange.

### F2: Resolve the exact DnaA and Hda families

minor / open / confirmed; issue key: dnaa-hda-exact-component-families.

DnaA IPR001957 and Hda IPR017788 are available exact whole-protein families and are independently present in the verified examples. The current REVIEWED_LABEL_ONLY rows and open TODO can therefore be resolved; narrower Hda IPR022864 is not the generic class.

## Recommended Actions And Acceptance Checks

### A1

Replace the mechanism sentence with source-backed DnaA-bound ATP hydrolysis in its DNA-loaded-clamp/ADP-Hda context. Preserve exact GO identity and record the upstream definition conflict; do not silently describe a revised primary-source definition as a verbatim GO definition.

- The corrected text distinguishes hydrolysis from nucleotide exchange and phosphorylation.
- Retain the binary contact versus full active RIDA-system boundary.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

### A2

Ground DnaA and Hda with the exact families and narrow/resolve the corresponding mapping task, retaining the taxon-paired examples.

- Check native family types/signatures and separate example cross-references.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dnaa_hda_complex.yaml; Entire maintained record, all evidence, components, graph, discussions and history | context_only | The complete maintained target was read; related complex boundaries are assessed only where this record names them. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, PresenceEnum and graph scope | context_only | Formation necessity differs from activity or viability; COMMON describes most members with exceptional losses, not a measured prevalence count. |
| curation | docs/CURATION.md; Exact class identity and REVIEWED_LABEL_ONLY contract | context_only | A protein family grounds the named protein class; an organism accession is a representative instance. An available exact class mapping can resolve the current label-only task. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Descriptive topology and claim-level causal support | context_only | Composition and broad function do not establish a complete molecular mechanism or component-absence formation experiment. |
| root52-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006270,GO:0032297,GO:1990077,GO:1990078,GO:1990082,GO:1990083,GO:1990084,GO:1990085,GO:1990100,GO:1990101,GO:1990102,GO:1990103; All twelve definitions, exact source xrefs, synonyms/comments and typed child links; no unspecified ontology relations inferred | supports | The twelve active native terms identify DnaA-Hda, DnaA-HU and DnaA-L2, their distinct neighboring complexes, their declared functions and typed primosome/replication-inhibiting-complex hierarchy. GO1990083 itself contains the phosphorylation wording that conflicts with its cited primary paper. |
| root52-sources-GO1990083-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990083/ancestors?relations=is_a; Complete native ancestor response; no parthood inferred from ancestry | supports | The is_a-only ancestry confirms replication-inhibiting and protein-containing-complex parentage. |
| root52-sources-GO1990083-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990083/constraints; Complete focal taxonConstraints array only; inherited protein blacklists are not biological evidence | context_only | The focal constraint is only_in_taxon cellular organisms. This is a permissive ontology restriction, not evidence that every permitted taxon has this complex. |
| root52-sources-GO1990083-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990083/history; Complete native term history | context_only | The native term history documents its definition and parent relation. The phosphorylation wording has been present since the2013 definition and was copied accurately into this record; copying does not resolve the conflict with primary evidence. |
| root52-sources-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxonomy response | supports | ENA identifies 562 as Escherichia coli. Species and reference-strain identity are distinguished. |
| root52-sources-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxonomy response | supports | ENA identifies 83333 as Escherichia coli K-12. Species and reference-strain identity are distinguished. |
| root52-sources-pmid-12618445 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12618445+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and complete abstractText | supports | Native MED12618445: Identification of a novel membrane-associated gene product that suppresses toxicity of a TrfA peptide from plasmid RK2 and its relationship to the DnaA host initiation protein. Authors Kim PD, Banack T, Lerman DM, Tracy JC, Camara JE, Crooke E, Oliver D, Firshein W.; year 2003; DOI 10.1128/jb.185.6.1817-1824.2003. Complete abstract inspected; body reading is declared separately. |
| root52-sources-pmid-15150238 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15150238+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and complete abstractText | supports | Native MED15150238: Interaction of the sliding clamp beta-subunit and Hda, a DnaA-related protein. Authors Kurz M, Dalrymple B, Wijffels G, Kongsuwan K.; year 2004; DOI 10.1128/jb.186.11.3508-3515.2004. Complete abstract inspected; body reading is declared separately. |
| root52-sources-pmid-21708944 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21708944+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and complete abstractText | supports | Native MED21708944: DnaA protein DNA-binding domain binds to Hda protein to promote inter-AAA+ domain interaction involved in regulatory inactivation of DnaA. Authors Keyamura K, Katayama T.; year 2011; DOI 10.1074/jbc.m111.233403. Complete abstract inspected; body reading is declared separately. |
| root52-sources-pmid-22574163 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22574163+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and complete abstractText | supports | Native MED22574163: Association of the chromosome replication initiator DnaA with the Escherichia coli inner membrane in vivo: quantity and mode of binding. Authors Regev T, Myers N, Zarivach R, Fishov I.; year 2012; DOI 10.1371/journal.pone.0036441. Complete abstract inspected; body reading is declared separately. |
| root52-sources-pmid-28166228 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28166228+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and complete abstractText | supports | Native MED28166228: Rapid turnover of DnaA at replication origin regions contributes to initiation control of DNA replication. Authors Schenk K, Hervás AB, Rösch TC, Eisemann M, Schmitt BA, Dahlke S, Kleine-Borgmann L, Murray SM, Graumann PL.; year 2017; DOI 10.1371/journal.pgen.1006561. Complete abstract inspected; body reading is declared separately. |
| root52-sources-pmid-9478970 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9478970+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and complete abstractText | supports | Native MED9478970: Membrane-mediated release of nucleotide from an initiator of chromosomal replication, Escherichia coli DnaA, occurs with insertion of a distinct region of the protein into the lipid bilayer. Authors Garner J, Durrer P, Kitchen J, Brunner J, Crooke E.; year 1998; DOI 10.1074/jbc.273.9.5167. Complete abstract inspected; body reading is declared separately. |
| root52-sources-protein-P03004 | https://rest.uniprot.org/uniprotkb/P03004.json; Complete identity/status/recommended and alternative names, genes, organism; all InterPro/NCBIfam/Pfam xrefs; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments where present | supports | P03004 is the reviewed K12 dnaA entry with the declared identity, exact gene/taxon and family cross-references. Its three declared localization ECO/PMID links match current annotation. The source’s BL21 membrane assay is not relabeled as a K12 complex-isolation experiment. |
| root52-sources-gene-dnaA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set for gene_exact:dnaA AND organism_id:83333 AND reviewed:true; size500 | supports | The reviewed exact-gene query restricted to organism_id83333 returns one entry, P03004. Descendant taxonomy scope is not substituted for this exact organism query. |
| root52-sources-protein-P69931 | https://rest.uniprot.org/uniprotkb/P69931.json; Complete identity/status/recommended and alternative names, genes, organism; all InterPro/NCBIfam/Pfam xrefs; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments where present | supports | P69931 is the reviewed K12 hda entry with the declared identity, exact gene/taxon and family cross-references. Its inner-membrane ECO0000269/PMID12618445 annotation is present. The TrfA assay and Hda-RIDA activity are separate biological contexts. |
| root52-sources-gene-hda | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahda%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set for gene_exact:hda AND organism_id:83333 AND reviewed:true; size500 | supports | The reviewed exact-gene query restricted to organism_id83333 returns one entry, P69931. Descendant taxonomy scope is not substituted for this exact organism query. |
| root52-sources-ipr-IPR001957 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001957/; Native accession/name/type, complete descriptions/flags, member signatures and hierarchy | supports | IPR001957 is the exact whole-protein DnaA initiator family with MF00377/TIGR00362 signatures, distinct from the broader DnaA-like parent and Hda sibling. This response establishes family identity; separate UniProt data establish example membership. |
| root52-sources-keyamura2011-modern | https://pmc.ncbi.nlm.nih.gov/articles/PMC3190739/; Complete scientific article text: abstract/Introduction/Fig1 caption; all Experimental Procedures; Resultssec19–25 and Fig2–6/Table1 captions; complete Discussion/Fig7 caption. No figure pixels, supplement or coordinates. | supports | The paper directly measures RIDA-dependent hydrolysis of DnaA-bound ATP to ADP, with DNA-loaded clamp and ADP-Hda. Direct DnaA-Hda binding is also measured by SPR without DNA-loaded clamps and is weak. L422/P423 mutants reduce interaction and hydrolysis while retaining initiation functions. Structural contacts are a model, not a solved DnaA-Hda co-crystal. |
| root52-sources-ipr-IPR017788 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017788/; Native name/type, complete descriptions/flags, hierarchy and member signatures | supports | Exact whole-protein Hda family with TIGR03420, distinct from the DnaA sibling and the narrower Enterobacteriaceae subgroup. Individual example membership is supplied by a separate UniProt source. |
| root52-sources-ipr-IPR022864 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022864/; Native name/type, complete descriptions/flags, hierarchy and member signatures | supports | Enterobacteriaceae-specific Hda subgroup with MF01158; narrower than the generic Hda constituent and not substituted for it. |
| keyamura2011-legacy-access | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3190739/; Retained failed/challenge route | context_only | Legacy HTTP200 returned a reCAPTCHA challenge, not the paper. |
| keyamura2011-xml-access | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3190739/fullTextXML; Retained failed/challenge route | context_only | EuropePMC fullTextXML route returned500; the separate modern PMC HTML supplied the genuine body. |
| schema-result | just validate data/structures/other/dnaa_hda_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dnaa_hda_complex.yaml |
| strict-result | just validate-strict data/structures/other/dnaa_hda_complex.yaml --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnaa_hda_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dnaa_hda_complex.yaml --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnaa_hda_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnaa_hda_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dnaa_hda_complex.yaml; Complete focused native report | supports | data/structures/other/dnaa_hda_complex.yaml  (GO:1990083)<br>  dnaa_hda_rida	dnaa_initiator	COVERED	-&gt;dnaa_initiator (UniProtKB:P03004)<br>  dnaa_hda_rida	hda_regulator	COVERED	-&gt;hda_regulator (UniProtKB:P69931)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/dnaa_hda_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dnaa_hda_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 16 collected target identifiers returned OK. PMID:12618445: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:15150238: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:21708944: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:22574163: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:28166228: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:9478970: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw data, sequence alignments or supplements were reanalyzed. Native protein annotation links and primary text reading remain separate evidence tiers.
- Legacy PMC yielded challenge HTML and the XML route returned500; genuine modern PMC HTML was read. Kurz2004 and the localization papers remain complete native abstract/annotation tiers, not independently read full methods.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations as well as issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T060738Z-dnaa-hda-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of DnaA-Hda complex
started_at: '2026-10-22T05:50:41Z'
finished_at: '2026-10-22T06:07:38Z'
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
summary: One major corrects an inherited phosphorylation-versus-hydrolysis definition
  error; one minor resolves exact DnaA/Hda families. Binary interaction, E.coli context
  and coarse negative-regulation graph remain supported.
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
  - path: data/structures/other/dnaa_hda_complex.yaml
    sha256: 483a497d765d330fb525a7294da3190f44406843dd7acf5e563fedd971533a8e
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
- target_id: GO:1990083
  path: data/structures/other/dnaa_hda_complex.yaml
  label: DnaA-Hda complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hda_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target; source-specific native fields
    and literature reading scopes are given in evidence. Scientific inputs remain
    unchanged.
  selection: One complete record in strict-path batch52 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990083
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: just validate data/structures/other/dnaa_hda_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: just validate-strict data/structures/other/dnaa_hda_complex.yaml --out
    /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnaa_hda_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dnaa_hda_complex.yaml
  exit_code: 0
  summary: Focused check passed; source claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dnaa_hda_complex.yaml
  exit_code: 0
  summary: Focused check passed; source claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990083
  summary: No expression-module or transcriptomic claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990083
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root52-sources-go
  - root52-sources-GO1990083-ancestors
  - root52-sources-GO1990083-constraints
  - root52-sources-GO1990083-history
  - root52-sources-tax562
  - root52-sources-tax83333
  - root52-sources-pmid-12618445
  - root52-sources-pmid-15150238
  - root52-sources-pmid-21708944
  - root52-sources-pmid-22574163
  - root52-sources-pmid-28166228
  - root52-sources-pmid-9478970
  - root52-sources-protein-P03004
  - root52-sources-gene-dnaA
  - root52-sources-protein-P69931
  - root52-sources-gene-hda
  - root52-sources-ipr-IPR001957
  - root52-sources-keyamura2011-modern
  - root52-sources-ipr-IPR017788
  - root52-sources-ipr-IPR022864
  - keyamura2011-legacy-access
  - keyamura2011-xml-access
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990083
  summary: '10 of 16 collected target identifiers returned OK. PMID:12618445: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:15150238: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:21708944: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:22574163: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:28166228: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:9478970: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - root52-sources-pmid-12618445
  - root52-sources-pmid-15150238
  - root52-sources-pmid-21708944
  - root52-sources-pmid-22574163
  - root52-sources-pmid-28166228
  - root52-sources-pmid-9478970
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990083
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
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dnaa_hda_complex.yaml
  locator: Entire maintained record, all evidence, components, graph, discussions
    and history
  accessed_at: '2026-10-22T05:58:39Z'
  support: context_only
  summary: The complete maintained target was read; related complex boundaries are
    assessed only where this record names them.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, PresenceEnum and graph scope
  accessed_at: '2026-10-22T05:58:39Z'
  support: context_only
  summary: Formation necessity differs from activity or viability; COMMON describes
    most members with exceptional losses, not a measured prevalence count.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and REVIEWED_LABEL_ONLY contract
  accessed_at: '2026-10-22T05:58:39Z'
  support: context_only
  summary: A protein family grounds the named protein class; an organism accession
    is a representative instance. An available exact class mapping can resolve the
    current label-only task.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Descriptive topology and claim-level causal support
  accessed_at: '2026-10-22T05:58:39Z'
  support: context_only
  summary: Composition and broad function do not establish a complete molecular mechanism
    or component-absence formation experiment.
- evidence_id: root52-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006270,GO:0032297,GO:1990077,GO:1990078,GO:1990082,GO:1990083,GO:1990084,GO:1990085,GO:1990100,GO:1990101,GO:1990102,GO:1990103
  locator: All twelve definitions, exact source xrefs, synonyms/comments and typed
    child links; no unspecified ontology relations inferred
  accessed_at: '2026-10-22T05:53:55.452807Z'
  support: supports
  summary: The twelve active native terms identify DnaA-Hda, DnaA-HU and DnaA-L2,
    their distinct neighboring complexes, their declared functions and typed primosome/replication-inhibiting-complex
    hierarchy. GO1990083 itself contains the phosphorylation wording that conflicts
    with its cited primary paper.
  snapshot_sha256: 8c62be05bc636ae3523b77665ad1b2e87cb6261fa754bdfc7d6103c709eecd3d
- evidence_id: root52-sources-GO1990083-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990083/ancestors?relations=is_a
  locator: Complete native ancestor response; no parthood inferred from ancestry
  accessed_at: '2026-10-22T05:53:58.400095Z'
  support: supports
  summary: The is_a-only ancestry confirms replication-inhibiting and protein-containing-complex
    parentage.
  snapshot_sha256: e81bfbf274efd5ccb3b50567d9d897c45c85f66a5c9a36cfc594b04a9dab927f
- evidence_id: root52-sources-GO1990083-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990083/constraints
  locator: Complete focal taxonConstraints array only; inherited protein blacklists
    are not biological evidence
  accessed_at: '2026-10-22T05:53:58.209049Z'
  support: context_only
  summary: The focal constraint is only_in_taxon cellular organisms. This is a permissive
    ontology restriction, not evidence that every permitted taxon has this complex.
  snapshot_sha256: bdead7778d39cd2467b2b48b37f5754f41b9c213f7c0865c9bc105f450dac3ee
- evidence_id: root52-sources-GO1990083-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990083/history
  locator: Complete native term history
  accessed_at: '2026-10-22T05:53:57.760755Z'
  support: context_only
  summary: The native term history documents its definition and parent relation. The
    phosphorylation wording has been present since the2013 definition and was copied
    accurately into this record; copying does not resolve the conflict with primary
    evidence.
  snapshot_sha256: f7d13cc813c69fa0c4f5f97ffa20bcf78874ed09d374bcf14a56dd94e76f7697
- evidence_id: root52-sources-tax562
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:53:56.559131Z'
  support: supports
  summary: ENA identifies 562 as Escherichia coli. Species and reference-strain identity
    are distinguished.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: root52-sources-tax83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:53:56.569314Z'
  support: supports
  summary: ENA identifies 83333 as Escherichia coli K-12. Species and reference-strain
    identity are distinguished.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: root52-sources-pmid-12618445
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12618445+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and complete abstractText
  accessed_at: '2026-10-22T05:53:56.849780Z'
  support: supports
  summary: 'Native MED12618445: Identification of a novel membrane-associated gene
    product that suppresses toxicity of a TrfA peptide from plasmid RK2 and its relationship
    to the DnaA host initiation protein. Authors Kim PD, Banack T, Lerman DM, Tracy
    JC, Camara JE, Crooke E, Oliver D, Firshein W.; year 2003; DOI 10.1128/jb.185.6.1817-1824.2003.
    Complete abstract inspected; body reading is declared separately.'
  snapshot_sha256: 9a4cf8f2fc413e18680829d20076a9510e53ab4c4f3f8d5163e9f4ce829a0189
- evidence_id: root52-sources-pmid-15150238
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15150238+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and complete abstractText
  accessed_at: '2026-10-22T05:53:57.084962Z'
  support: supports
  summary: 'Native MED15150238: Interaction of the sliding clamp beta-subunit and
    Hda, a DnaA-related protein. Authors Kurz M, Dalrymple B, Wijffels G, Kongsuwan
    K.; year 2004; DOI 10.1128/jb.186.11.3508-3515.2004. Complete abstract inspected;
    body reading is declared separately.'
  snapshot_sha256: 96bea6a3440ac806cd1daddf7692540308d3cf9b7282b5c37e589d7554ddf015
- evidence_id: root52-sources-pmid-21708944
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21708944+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and complete abstractText
  accessed_at: '2026-10-22T05:53:57.475061Z'
  support: supports
  summary: 'Native MED21708944: DnaA protein DNA-binding domain binds to Hda protein
    to promote inter-AAA+ domain interaction involved in regulatory inactivation of
    DnaA. Authors Keyamura K, Katayama T.; year 2011; DOI 10.1074/jbc.m111.233403.
    Complete abstract inspected; body reading is declared separately.'
  snapshot_sha256: 6ccf985cb6131770309ce19344595a3fb2aa8cbcedf37146ca85b7c2001a4122
- evidence_id: root52-sources-pmid-22574163
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22574163+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and complete abstractText
  accessed_at: '2026-10-22T05:53:57.701925Z'
  support: supports
  summary: 'Native MED22574163: Association of the chromosome replication initiator
    DnaA with the Escherichia coli inner membrane in vivo: quantity and mode of binding.
    Authors Regev T, Myers N, Zarivach R, Fishov I.; year 2012; DOI 10.1371/journal.pone.0036441.
    Complete abstract inspected; body reading is declared separately.'
  snapshot_sha256: 606182e9806d23b9bf7730d38e83960a8b1336283390495aabe7d55367902d79
- evidence_id: root52-sources-pmid-28166228
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28166228+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and complete abstractText
  accessed_at: '2026-10-22T05:53:57.752002Z'
  support: supports
  summary: 'Native MED28166228: Rapid turnover of DnaA at replication origin regions
    contributes to initiation control of DNA replication. Authors Schenk K, Hervás
    AB, Rösch TC, Eisemann M, Schmitt BA, Dahlke S, Kleine-Borgmann L, Murray SM,
    Graumann PL.; year 2017; DOI 10.1371/journal.pgen.1006561. Complete abstract inspected;
    body reading is declared separately.'
  snapshot_sha256: 62b379003572dabe10f78cc8b7642794dc900df5ca5799cd0f29217cbf4c1bc3
- evidence_id: root52-sources-pmid-9478970
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9478970+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and complete abstractText
  accessed_at: '2026-10-22T05:53:57.754760Z'
  support: supports
  summary: 'Native MED9478970: Membrane-mediated release of nucleotide from an initiator
    of chromosomal replication, Escherichia coli DnaA, occurs with insertion of a
    distinct region of the protein into the lipid bilayer. Authors Garner J, Durrer
    P, Kitchen J, Brunner J, Crooke E.; year 1998; DOI 10.1074/jbc.273.9.5167. Complete
    abstract inspected; body reading is declared separately.'
  snapshot_sha256: 46d168668e549dce45c86e1638c9d1bed0b4ae65a45b00090e1150e5de2a19bf
- evidence_id: root52-sources-protein-P03004
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P03004.json
  locator: Complete identity/status/recommended and alternative names, genes, organism;
    all InterPro/NCBIfam/Pfam xrefs; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments where present
  accessed_at: '2026-10-22T05:53:55.453248Z'
  support: supports
  summary: P03004 is the reviewed K12 dnaA entry with the declared identity, exact
    gene/taxon and family cross-references. Its three declared localization ECO/PMID
    links match current annotation. The source’s BL21 membrane assay is not relabeled
    as a K12 complex-isolation experiment.
  snapshot_sha256: 20b9ed0385942a0aebc3645f0f499a77e9aab0741218e2327ee80b6ae7590dca
- evidence_id: root52-sources-gene-dnaA
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set for gene_exact:dnaA AND organism_id:83333
    AND reviewed:true; size500
  accessed_at: '2026-10-22T05:53:55.453826Z'
  support: supports
  summary: The reviewed exact-gene query restricted to organism_id83333 returns one
    entry, P03004. Descendant taxonomy scope is not substituted for this exact organism
    query.
  snapshot_sha256: 3db63cf0e2bda46f5e0d2292b32f98621aa2da23fba568a428d8ad2f1fb148a0
- evidence_id: root52-sources-protein-P69931
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P69931.json
  locator: Complete identity/status/recommended and alternative names, genes, organism;
    all InterPro/NCBIfam/Pfam xrefs; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments where present
  accessed_at: '2026-10-22T05:53:55.453442Z'
  support: supports
  summary: P69931 is the reviewed K12 hda entry with the declared identity, exact
    gene/taxon and family cross-references. Its inner-membrane ECO0000269/PMID12618445
    annotation is present. The TrfA assay and Hda-RIDA activity are separate biological
    contexts.
  snapshot_sha256: 426a92b935654ddf255d7bb462d2bd0bce6ab02033aed38b8e324916751c0b1d
- evidence_id: root52-sources-gene-hda
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahda%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set for gene_exact:hda AND organism_id:83333 AND
    reviewed:true; size500
  accessed_at: '2026-10-22T05:53:56.164333Z'
  support: supports
  summary: The reviewed exact-gene query restricted to organism_id83333 returns one
    entry, P69931. Descendant taxonomy scope is not substituted for this exact organism
    query.
  snapshot_sha256: eb8af1bf9d21c98c3becc40e269fbb9fd003455df2925d8b91c12c8d659df4c1
- evidence_id: root52-sources-ipr-IPR001957
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001957/
  locator: Native accession/name/type, complete descriptions/flags, member signatures
    and hierarchy
  accessed_at: '2026-10-22T05:53:59.459010Z'
  support: supports
  summary: IPR001957 is the exact whole-protein DnaA initiator family with MF00377/TIGR00362
    signatures, distinct from the broader DnaA-like parent and Hda sibling. This response
    establishes family identity; separate UniProt data establish example membership.
  snapshot_sha256: 364ea5ab4304d290b099574c7f9527e5577eefec2872f8fc2adde34de7eb2fc2
- evidence_id: root52-sources-keyamura2011-modern
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3190739/
  locator: 'Complete scientific article text: abstract/Introduction/Fig1 caption;
    all Experimental Procedures; Resultssec19–25 and Fig2–6/Table1 captions; complete
    Discussion/Fig7 caption. No figure pixels, supplement or coordinates.'
  accessed_at: '2026-10-22T05:54:59.990472Z'
  support: supports
  summary: The paper directly measures RIDA-dependent hydrolysis of DnaA-bound ATP
    to ADP, with DNA-loaded clamp and ADP-Hda. Direct DnaA-Hda binding is also measured
    by SPR without DNA-loaded clamps and is weak. L422/P423 mutants reduce interaction
    and hydrolysis while retaining initiation functions. Structural contacts are a
    model, not a solved DnaA-Hda co-crystal.
  snapshot_sha256: ec00aa9f568c3d06c76181d224fecead337060988a54037380367dd409e6a6a6
- evidence_id: root52-sources-ipr-IPR017788
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017788/
  locator: Native name/type, complete descriptions/flags, hierarchy and member signatures
  accessed_at: '2026-10-22T05:54:59.989755Z'
  support: supports
  summary: Exact whole-protein Hda family with TIGR03420, distinct from the DnaA sibling
    and the narrower Enterobacteriaceae subgroup. Individual example membership is
    supplied by a separate UniProt source.
  snapshot_sha256: 7e9d3b5937bd2091b11b482deda5c5328592a0121f84c369e97a6ba8390abb6c
- evidence_id: root52-sources-ipr-IPR022864
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022864/
  locator: Native name/type, complete descriptions/flags, hierarchy and member signatures
  accessed_at: '2026-10-22T05:54:59.990446Z'
  support: supports
  summary: Enterobacteriaceae-specific Hda subgroup with MF01158; narrower than the
    generic Hda constituent and not substituted for it.
  snapshot_sha256: a3300bce98be51679d5018b6ad7ad5dc4ad5108f0c7c19c006f084c8f43425f0
- evidence_id: keyamura2011-legacy-access
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3190739/
  locator: Retained failed/challenge route
  accessed_at: '2026-10-22T05:53:59.700989Z'
  support: context_only
  summary: Legacy HTTP200 returned a reCAPTCHA challenge, not the paper.
  snapshot_sha256: a174414fa66636d2fc2c092b7be9cbd7570dc05fd40d2bec4e03d2e2f6a62c30
- evidence_id: keyamura2011-xml-access
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3190739/fullTextXML
  locator: Retained failed/challenge route
  accessed_at: '2026-10-22T05:55:00.428545Z'
  support: context_only
  summary: EuropePMC fullTextXML route returned500; the separate modern PMC HTML supplied
    the genuine body.
  snapshot_sha256: 65650040210570c95714538412d01052ede574689048a0655cb16319c4acd2bc
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dnaa_hda_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:50:44Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dnaa_hda_complex.yaml'
  snapshot_sha256: 74098f9dc259dd672d4ff3ffb7454fe171594ecc466742549c3a7dc09cc4e3df
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dnaa_hda_complex.yaml --out
    /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnaa_hda_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:50:45Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dnaa_hda_complex.yaml\
    \ --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnaa_hda_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnaa_hda_complex-strict.tsv"
  snapshot_sha256: 0a46473ae945128f0f642d31f08fc7b5e7e6961d7fb57f35e2cdcef398ac3893
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dnaa_hda_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:53:40.739043Z'
  support: supports
  summary: "data/structures/other/dnaa_hda_complex.yaml  (GO:1990083)\n  dnaa_hda_rida\t\
    dnaa_initiator\tCOVERED\t->dnaa_initiator (UniProtKB:P03004)\n  dnaa_hda_rida\t\
    hda_regulator\tCOVERED\t->hda_regulator (UniProtKB:P69931)\n\ncausal_graphs GENE_OR_PROTEIN\
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
  snapshot_sha256: c1b02a106da2af87da59359f83b31b146fdd3ba83f7f8364b563ee0084a53520
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dnaa_hda_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:53:42.148096Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dnaa_hda_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 16 collected target identifiers returned OK. PMID:12618445: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:15150238: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:21708944: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:22574163: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:28166228: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:9478970: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
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
  topic: Binary contact within the larger RIDA system
  outcome: supported
  target_ids:
  - GO:1990083
  summary: Exact DnaA-Hda identity and replication-inhibiting parentage are sound.
    Direct binding without the clamp supports the binary contact boundary; the efficient
    RIDA reaction also requires the DNA-loaded clamp context. Do not collapse this
    record into the separately named Hda-beta complex.
  evidence_ids:
  - record
  - root52-sources-go
  - root52-sources-GO1990083-ancestors
  - root52-sources-keyamura2011-modern
- assessment_id: chemistry
  area: evidence
  topic: Hydrolysis versus phosphorylation wording
  outcome: concern
  target_ids:
  - GO:1990083
  summary: The maintained definition faithfully repeats native GO but incorrectly
    describes prevention of DnaA-ADP phosphorylation. The primary assay instead measures
    conversion of ATP-DnaA to ADP-DnaA by hydrolysis, and the target’s canonical note/final
    graph edge already use that chemistry. DARS reactivation proceeds by nucleotide
    exchange, not phosphorylation of DnaA-bound ADP.
  evidence_ids:
  - record
  - root52-sources-go
  - root52-sources-GO1990083-history
  - root52-sources-keyamura2011-modern
  - root52-sources-pmid-21708944
  - root52-sources-protein-P03004
  - root52-sources-protein-P69931
- assessment_id: composition
  area: grounding
  topic: Two correct proteins with exact families
  outcome: concern
  target_ids:
  - GO:1990083
  summary: Both K12 examples, source-scoped membership and localization annotations
    are correct. Exact class families are actionable; activity or viability is not
    a physical-formation requirement.
  evidence_ids:
  - record
  - root52-sources-keyamura2011-modern
  - root52-sources-ipr-IPR001957
  - root52-sources-ipr-IPR017788
  - root52-sources-ipr-IPR022864
  - root52-sources-protein-P03004
  - root52-sources-protein-P69931
  - root52-sources-gene-dnaA
  - root52-sources-gene-hda
- assessment_id: graph
  area: graph
  topic: Supported coarse negative-regulation graph
  outcome: supported
  target_ids:
  - GO:1990083
  summary: The two membership edges and final negative-regulation support edge correctly
    describe composition and ATP hydrolysis at a coarse level. NONMECHANISTIC scope
    preserves clamp context as outside the encoded detail; the definition chemistry,
    not the graph edge, needs correction.
  evidence_ids:
  - record
  - graphs
  - root52-sources-go
  - root52-sources-keyamura2011-modern
- assessment_id: scope
  area: scope
  topic: E.coli experiment versus reference entry
  outcome: supported
  target_ids:
  - GO:1990083
  summary: The study uses K12-derived strains and purified reconstitutions, supporting
    the named E.coli canonical example. Model geometry, residual binding and mutant
    phenotypes remain condition-scoped; the permissive cellular-organisms constraint
    is not a distribution claim.
  evidence_ids:
  - record
  - root52-sources-keyamura2011-modern
  - root52-sources-GO1990083-constraints
  - root52-sources-tax562
  - root52-sources-tax83333
  - root52-sources-protein-P03004
  - root52-sources-protein-P69931
- assessment_id: formation
  area: grounding
  topic: Constituent identity is not an absence assay
  outcome: unknown
  target_ids:
  - GO:1990083
  summary: All component essentialities remain UNKNOWN. Direct binding, functional
    inhibition/stimulation and organism viability do not alone establish physical
    formation in every component-absence condition. No optional constituent inventory
    is invented.
  evidence_ids:
  - record
  - schema
  - root52-sources-go
  - root52-sources-pmid-12618445
  - root52-sources-pmid-15150238
  - root52-sources-pmid-21708944
  - root52-sources-pmid-22574163
  - root52-sources-pmid-28166228
  - root52-sources-pmid-9478970
- assessment_id: coverage
  area: completeness
  topic: Whole maintained record and source boundaries
  outcome: supported
  target_ids:
  - GO:1990083
  summary: Every maintained field, component/example, edge, discussion and history
    was read. Exact available mappings and substantive source conflicts are distinguished
    from optional enrichment and unresolved access limits. Historical deferral notes
    remain historical statements, not claims of fabrication.
  evidence_ids:
  - record
  - curation
  - schema
  - root52-sources-go
  - root52-sources-pmid-12618445
  - root52-sources-pmid-15150238
  - root52-sources-pmid-21708944
  - root52-sources-pmid-22574163
  - root52-sources-pmid-28166228
  - root52-sources-pmid-9478970
findings:
- finding_id: F1
  issue_key: dnaa-hda-definition-phosphorylation-versus-hydrolysis
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the inherited RIDA chemistry
  description: The definition says Hda inactivates DnaA by inhibiting phosphorylation
    of DnaA-ADP to DnaA-ATP. This matches current GO1990083 but conflicts with the
    cited Keyamura/Katayama2011 staged hydrolysis assay and the target’s own ATP-hydrolysis
    canonical/graph text. RIDA promotes hydrolysis of bound ATP; reactivation by DARS
    uses nucleotide exchange.
  target_ids:
  - GO:1990083
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - record
  - root52-sources-go
  - root52-sources-GO1990083-history
  - root52-sources-keyamura2011-modern
  - root52-sources-pmid-21708944
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hda_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and source-scoped scientific assertions
  native_severity: major
  normalization_reason: The defining chemistry contradicts the cited primary experiment
    and the record’s own hydrolysis description; this is a substantive mechanism error
    while complex identity remains correct.
- finding_id: F2
  issue_key: dnaa-hda-exact-component-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the exact DnaA and Hda families
  description: DnaA IPR001957 and Hda IPR017788 are available exact whole-protein
    families and are independently present in the verified examples. The current REVIEWED_LABEL_ONLY
    rows and open TODO can therefore be resolved; narrower Hda IPR022864 is not the
    generic class.
  target_ids:
  - GO:1990083
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root52-sources-ipr-IPR001957
  - root52-sources-ipr-IPR017788
  - root52-sources-ipr-IPR022864
  - root52-sources-protein-P03004
  - root52-sources-protein-P69931
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hda_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and source-scoped scientific assertions
  native_severity: minor
  normalization_reason: Correct complex identity and supported membership remain intact;
    this is a bounded actionable class-grounding gap, not a requirement to fill optional
    examples.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990083
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hda_complex.yaml
    role: maintained scientific record
  description: Replace the mechanism sentence with source-backed DnaA-bound ATP hydrolysis
    in its DNA-loaded-clamp/ADP-Hda context. Preserve exact GO identity and record
    the upstream definition conflict; do not silently describe a revised primary-source
    definition as a verbatim GO definition.
  acceptance_checks:
  - The corrected text distinguishes hydrolysis from nucleotide exchange and phosphorylation.
  - Retain the binary contact versus full active RIDA-system boundary.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:1990083
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hda_complex.yaml
    role: maintained scientific record
  description: Ground DnaA and Hda with the exact families and narrow/resolve the
    corresponding mapping task, retaining the taxon-paired examples.
  acceptance_checks:
  - Check native family types/signatures and separate example cross-references.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw data, sequence alignments or supplements were reanalyzed.
  Native protein annotation links and primary text reading remain separate evidence
  tiers.
- Legacy PMC yielded challenge HTML and the XML route returned500; genuine modern
  PMC HTML was read. Kurz2004 and the localization papers remain complete native abstract/annotation
  tiers, not independently read full methods.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations as well as issue-bearing
  reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
