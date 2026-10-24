# Source-backed review of mre11 complex

- Review: 20261022T090915Z-mre11-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T08:39:56Z
- Finished UTC: 2026-10-22T09:09:15Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One grouped minor: Mre11 and Rad50 have verified exact family mappings. Complex identity, scoped Xrs2 membership, examples and coarse repair/recombination graph are supported; assembly and copy-number limits remain explicit.

## Scope And Provenance

Exactly one entire maintained target and 14 frozen inputs. No neighboring maintained record is an unstated premise. Actual source tiers/read extents are declared per evidence row.

Selection: Batch61 strict ordered selection index 6; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030870 | data/structures/other/mre11_complex.yaml | maintained | Mre11 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030870 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030870 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0030870 | Focused check passed; scientific assertions were independently assessed. |
| Focused native verify | passed | True | GO:0030870 | Focused check passed; scientific assertions were independently assessed. |
| Claim-level scientific review | passed | True | GO:0030870 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030870 | 13 of 18 collected target identifiers returned OK. PMID:10219078: UNREACHABLE; Native Europe PMC uniquely identifies PMID:10219078: Formation of the yeast Mre11-Rad50-Xrs2 complex is correlated with DNA repair and telomere maintenance. (1999), DOI10.1093/nar/27.10.2072. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:10523656: UNREACHABLE; Native Europe PMC uniquely identifies PMID:10523656: The Mre11-Rad50-Xrs2 protein complex facilitates homologous recombination-based double-strand break repair in Saccharomyces cerevisiae. (1999), DOI10.1128/mcb.19.11.7681. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:11988766: UNREACHABLE; Native Europe PMC uniquely identifies PMID:11988766: The Mre11 complex: at the crossroads of dna repair and checkpoint signalling. (2002), DOI10.1038/nrm805. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:17674145: UNREACHABLE; Native Europe PMC uniquely identifies PMID:17674145: The multiple roles of the Mre11 complex for meiotic recombination. (2007), DOI10.1007/s10577-007-1147-9. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:9845372: UNREACHABLE; Native Europe PMC uniquely identifies PMID:9845372: Complex formation and functional versatility of Mre11 of budding yeast in recombination. (1998), DOI10.1016/s0092-8674(00)81640-2. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030870 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030870 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030870 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030870 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030870 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Supported MRX/MRN class with a scoped budding-yeast third subunit

identity: supported. Targets: GO:0030870.

The current GO identity, exact synonym qualifications and nuclear parent agree. The maintained third component is specifically Xrs2, preserving the prior correction rather than claiming a universal Xrs2/Nbs1 protein identity.

### Two exact whole-protein families and one unresolved domain boundary

grounding: concern. Targets: GO:0030870.

IPR003701 Mre11 and eukaryotic IPR004584 Rad50 match represented classes with independent native accession cross-references. Xrs2 FHA domain IPR000253 is not substituted for a whole-family identifier.

### Three constituent classes and coarse repair functions

graph: supported. Targets: GO:0030870.

The five NONMECHANISTIC edges state three constituents and repair/recombination roles supported by GO and source-specific literature. The graph scope explicitly names three classes; its trimeric wording is not treated as a numerical1:1:1 assertion. Native comments describe two Mre11/two Rad50/one Xrs2 copies, so class count must not be silently converted into molecular stoichiometry.

### Unknown labels preserve domain and assay dependence

evidence: unknown. Targets: GO:0030870.

All three UNKNOWN labels remain defensible. Chamankhah abstract reports domain-dependent interactions and functional correlations, including a deletion retaining mitotic functions; Bressan separates nuclease and repair functions. These do not establish exhaustive universal physical-formation dependencies.

### Reference identities and an acknowledged query collision

grounding: supported. Targets: GO:0030870.

The three reviewed S288C proteins and Usui1998 nuclear annotation identities agree. MRE11/RAD50 exact queries are single-hit; XRS2 also returns CDC40 through an alias, and the maintained P33301 example already correctly says representative. No uniqueness correction is warranted.

### Budding-yeast context and qualified comparative terminology

scope: supported. Targets: GO:0030870.

COMMON retains majority occurrence with exceptional losses, supported qualitatively but not by a strain census. Bressan assay strains/cell-cycle/radiation conditions are distinct from S288C reference sequences. D’Amours/Jackson and Borde are secondary reviews at complete abstract tier, not independently observed experiments.

### Complete target review with bounded unresolved details

completeness: supported. Targets: GO:0030870.

All scientific fields, example identities, graphs, current discussions and history were read. Actionable exact mappings are distinguished from optional inventory enrichment, broader domain candidates and historical first-pass statements. No maintained scientific content was changed.

## Findings

### F1: Ground the Mre11 and Rad50 constituent classes

minor / open / confirmed; issue key: mre11-rad50-exact-family-groundings.

The represented Mre11 and Rad50 classes remain REVIEWED_LABEL_ONLY despite exact verified IPR003701 and eukaryotic IPR004584 families and separate accession cross-references. Xrs2 remains unresolved at whole-family level; the reviewed FHA domain is insufficient.

## Recommended Actions And Acceptance Checks

### A1

Add IPR003701 for Mre11 and IPR004584 for Rad50; update current grounding notes/status and the open task. Preserve the Xrs2-specific third row, representative XRS2 example, UNKNOWN essentiality and distinction between class count and molecular copy number.

- The added family identifiers match the named whole-protein classes and independently verified member identities.
- Current grounding status and discussion reflect the verified mappings while broader candidates and UNKNOWN formation labels remain qualified.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/mre11_complex.yaml; Entire maintained YAML, including all scientific fields, examples, graphs, discussions and history | context_only | All target bytes were read. No neighboring maintained record supplies an unstated scientific premise. |
| curation | docs/CURATION.md; Component-class grounding and reviewed-label-only contract | context_only | Species accessions establish examples, not automatic class groundings. Unknowns and empty optional slots alone are not defects. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum and graph actor semantics | context_only | Formation necessity differs from activity, viability and localization. COMMON means present in most members with exceptional losses, not merely known occurrence. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Actor identity, source placement and descriptive versus mechanistic relationships | context_only | Assay, species and epistemic boundaries apply to each graph claim. Coarse descriptive membership/function need not invent unresolved intermediates or copy ratios. |
| micro61-md-10219078 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10219078+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID10219078: Formation of the yeast Mre11-Rad50-Xrs2 complex is correlated with DNA repair and telomere maintenance. Chamankhah M, Xiao W. (1999), DOI10.1093/nar/27.10.2072. Complete native abstract read; this metadata row does not attest main-body access. |
| micro61-md-10523656 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10523656+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID10523656: The Mre11-Rad50-Xrs2 protein complex facilitates homologous recombination-based double-strand break repair in Saccharomyces cerevisiae. Bressan DA, Baxter BK, Petrini JH. (1999), DOI10.1128/mcb.19.11.7681. Complete native abstract read; this metadata row does not attest main-body access. |
| micro61-md-11988766 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11988766+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID11988766: The Mre11 complex: at the crossroads of dna repair and checkpoint signalling. D'Amours D, Jackson SP. (2002), DOI10.1038/nrm805. Complete native abstract read; this metadata row does not attest main-body access. |
| micro61-md-17674145 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17674145+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID17674145: The multiple roles of the Mre11 complex for meiotic recombination. Borde V. (2007), DOI10.1007/s10577-007-1147-9. Complete native abstract read; this metadata row does not attest main-body access. |
| micro61-md-9845372 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9845372+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID9845372: Complex formation and functional versatility of Mre11 of budding yeast in recombination. Usui T, Ohta T, Oshiumi H, Tomizawa J, Ogawa H, Ogawa T. (1998), DOI10.1016/s0092-8674(00)81640-2. Complete native abstract read; this metadata row does not attest main-body access. |
| micro61-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and relevant synonyms. | supports | ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. Experimental backgrounds are not inferred from the reference sequence strain. |
| micro61-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Exact taxId, scientificName, rank, lineage and relevant synonyms. | supports | ENA taxId559292 identifies Saccharomyces cerevisiae S288C, rank strain. Experimental backgrounds are not inferred from the reference sequence strain. |
| micro61-protein-P12753 | https://rest.uniprot.org/uniprotkb/P12753.json; Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments; InterPro cross-references. | supports | Reviewed P12753 identifies RAD50 in taxon559292; complete function, subunit and location comments were inspected. InterPro cross-references establish accession membership separately from family-only metadata. Unlisted annotation papers are not certified as read. |
| micro61-protein-P32829 | https://rest.uniprot.org/uniprotkb/P32829.json; Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments; InterPro cross-references. | supports | Reviewed P32829 identifies MRE11 in taxon559292; complete function, subunit and location comments were inspected. InterPro cross-references establish accession membership separately from family-only metadata. Unlisted annotation papers are not certified as read. |
| micro61-protein-P33301 | https://rest.uniprot.org/uniprotkb/P33301.json; Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments; InterPro cross-references. | supports | Reviewed P33301 identifies XRS2 in taxon559292; complete function, subunit and location comments were inspected. InterPro cross-references establish accession membership separately from family-only metadata. Unlisted annotation papers are not certified as read. |
| micro61-gene-MRE11 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMRE11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set and exact gene_exact, organism_id and reviewed:true query in original URL. | supports | The exact reviewed MRE11 organism559292 query returns P32829. The sole returned primary gene and accession agree with the maintained example. |
| micro61-gene-RAD50 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARAD50%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set and exact gene_exact, organism_id and reviewed:true query in original URL. | supports | The exact reviewed RAD50 organism559292 query returns P12753. The sole returned primary gene and accession agree with the maintained example. |
| micro61-gene-XRS2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AXRS2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set and exact gene_exact, organism_id and reviewed:true query in original URL. | supports | The exact reviewed XRS2 organism559292 query returns P33301, P40968. The XRS2 result set includes the CDC40 alias collision P40968; P33301 has the exact primary gene XRS2. The maintained example already says representative rather than single-hit. |
| micro61-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776,GO:0005730,GO:0006281,GO:0007131,GO:0030686,GO:0030870,GO:0032991,GO:0033551,GO:0034457,GO:0034463,GO:0140513; Only these four complete native entries: identity, definition, synonyms and relevant typed links. | supports | GO0030870 identifies the Mre11 complex and all six exact synonyms. GO0140513 is its nuclear protein-containing-complex parent, while GO0006281 and GO0007131 describe the two coarse processes. The definition names three constituent classes. |
| micro61-GO0030870-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030870/ancestors?relations=is_a; Complete exact requested-term is_a ancestor array. | supports | The is_a-only response includes nuclear protein-containing complex GO0140513 and broader protein-complex ancestors. |
| micro61-PMC84807-ncbi2 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC84807/?report=xml; Genuine primary HTML: complete Methods sec1 and Table1, complete Results sec9 including Tables2/3 and Fig1–5 captions, complete Discussion sec14. Introduction, figure pixels, separate supplements and raw measurements not read. | supports | The tested yeast strains, radiation/cell-cycle assays and genetic comparisons connect MRX to homologous-recombination DSB repair. Nuclease-deficient mre11-3 retains assayed mitotic repair functions unlike deletion; nuclease activity, complex function and formation are not collapsed into one requirement. |
| micro61-PMC148425-legacy | https://pmc.ncbi.nlm.nih.gov/articles/148425/; Actual abstract and scan landing-page content only; no scanned pages inspected. | context_only | This genuine legacy page supplies the Chamankhah1999 abstract and scanned-PDF links, not a readable primary body. Scientific support is restricted to the independently retained complete MED abstract. |
| micro61-IPR003701 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003701/; Complete type/name/descriptions/member_databases and quality flags; scope compared with the represented whole-protein class. | supports | IPR003701 is the DNA double-strand break repair protein Mre11 family. Exact name, full description, integrated signatures and quality flags were read. Protein membership is independently established by separate UniProt evidence.  |
| micro61-IPR004584 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004584/; Complete type/name/descriptions/member_databases and quality flags; scope compared with the represented whole-protein class. | supports | IPR004584 is the DNA repair protein Rad50, eukaryotes family. Exact name, full description, integrated signatures and quality flags were read. Protein membership is independently established by separate UniProt evidence. This eukaryotic Rad50 family is distinct from the related bacterial SbcC class. |
| micro61-IPR000253 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000253/; Complete type/name/descriptions/member_databases and quality flags; scope compared with the represented whole-protein class. | supports | IPR000253 is the Forkhead-associated (FHA) domain domain. Exact name, full description, integrated signatures and quality flags were read. Protein membership is independently established by separate UniProt evidence. This FHA domain is not an exact whole-Xrs2 family and is withheld as a component-class mapping. |
| schema-result | just validate data/structures/other/mre11_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/mre11_complex.yaml |
| strict-result | just validate-strict data/structures/other/mre11_complex.yaml --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mre11_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/mre11_complex.yaml --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mre11_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mre11_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mre11_complex.yaml --causal-graphs; Complete focused read-only native log | supports | data/structures/other/mre11_complex.yaml  (GO:0030870)<br>  mre11_dna_repair_recombination	mre11_nuclease_subunit	COVERED	-&gt;mre11_nuclease_subunit (UniProtKB:P32829)<br>  mre11_dna_repair_recombination	rad50_atpase_subunit	COVERED	-&gt;rad50_atpase_subunit (UniProtKB:P12753)<br>  mre11_dna_repair_recombination	xrs2_regulatory_subunit	COVERED	-&gt;xrs2_regulatory_subunit (UniProtKB:P33301)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mre11_complex.yaml --verify; Complete focused read-only native log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/mre11_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 18 collected target identifiers returned OK. PMID:10219078: UNREACHABLE; Native Europe PMC uniquely identifies PMID:10219078: Formation of the yeast Mre11-Rad50-Xrs2 complex is correlated with DNA repair and telomere maintenance. (1999), DOI10.1093/nar/27.10.2072. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:10523656: UNREACHABLE; Native Europe PMC uniquely identifies PMID:10523656: The Mre11-Rad50-Xrs2 protein complex facilitates homologous recombination-based double-strand break repair in Saccharomyces cerevisiae. (1999), DOI10.1128/mcb.19.11.7681. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:11988766: UNREACHABLE; Native Europe PMC uniquely identifies PMID:11988766: The Mre11 complex: at the crossroads of dna repair and checkpoint signalling. (2002), DOI10.1038/nrm805. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:17674145: UNREACHABLE; Native Europe PMC uniquely identifies PMID:17674145: The multiple roles of the Mre11 complex for meiotic recombination. (2007), DOI10.1007/s10577-007-1147-9. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:9845372: UNREACHABLE; Native Europe PMC uniquely identifies PMID:9845372: Complex formation and functional versatility of Mre11 of budding yeast in recombination. (1998), DOI10.1016/s0092-8674(00)81640-2. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Bressan1999 was read in complete Methods/Results/Discussion with the declared tables/captions, not Introduction, figure pixels or raw data. Chamankhah1999 and Usui1998 were read at complete native abstract tier; Chamankhah scan links did not yield a readable body. D’Amours/Jackson2002 and Borde2007 are secondary-review abstracts only.
- The record explicitly models three constituent classes; no1:1:1 copy ratio is inferred from trimeric wording. Native stoichiometric comments are not a new quantitative reconstitution analysis. Domain-interaction/function evidence does not force universal formation necessity.
- Xrs2 FHA is a domain, not a whole-family mapping. XRS2 query alias collision is acknowledged in the existing representative example. COMMON retains majority meaning without an exhaustive prevalence census.
- Original source URL, UTC and SHA256 are retained. HTTP status alone does not establish article-body readability; initial DNS failures and unsuccessful access responses remain diagnostic only.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requests a review for every unreviewed record, including qualified clean cases.
- Initial inspections and failed access attempts are preserved. No scientific record, historical review, index or Git state was edited.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T090915Z-mre11-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of mre11 complex
started_at: '2026-10-22T08:39:56Z'
finished_at: '2026-10-22T09:09:15Z'
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
summary: 'One grouped minor: Mre11 and Rad50 have verified exact family mappings.
  Complex identity, scoped Xrs2 membership, examples and coarse repair/recombination
  graph are supported; assembly and copy-number limits remain explicit.'
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
  - path: data/structures/other/mre11_complex.yaml
    sha256: 51cfa599aa779c1d9c92c29309dfa6eb24a838bf76c6711b6ed3f7120842d884
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
- target_id: GO:0030870
  path: data/structures/other/mre11_complex.yaml
  label: Mre11 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mre11_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire maintained target and 14 frozen inputs. No neighboring
    maintained record is an unstated premise. Actual source tiers/read extents are
    declared per evidence row.
  selection: Batch61 strict ordered selection index 6; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030870
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030870
  command: just validate data/structures/other/mre11_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030870
  command: just validate-strict data/structures/other/mre11_complex.yaml --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mre11_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030870
  command: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mre11_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific assertions were independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0030870
  command: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mre11_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; scientific assertions were independently assessed.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030870
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-md-10219078
  - micro61-md-10523656
  - micro61-md-11988766
  - micro61-md-17674145
  - micro61-md-9845372
  - micro61-tax4932
  - micro61-tax559292
  - micro61-protein-P12753
  - micro61-protein-P32829
  - micro61-protein-P33301
  - micro61-gene-MRE11
  - micro61-gene-RAD50
  - micro61-gene-XRS2
  - micro61-go
  - micro61-GO0030870-ancestors
  - micro61-PMC84807-ncbi2
  - micro61-PMC148425-legacy
  - micro61-IPR003701
  - micro61-IPR004584
  - micro61-IPR000253
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030870
  summary: '13 of 18 collected target identifiers returned OK. PMID:10219078: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:10219078: Formation of the yeast Mre11-Rad50-Xrs2
    complex is correlated with DNA repair and telomere maintenance. (1999), DOI10.1093/nar/27.10.2072.
    Identifier/bibliographic verification is separate from the declared body or abstract
    scientific-reading scope.; PMID:10523656: UNREACHABLE; Native Europe PMC uniquely
    identifies PMID:10523656: The Mre11-Rad50-Xrs2 protein complex facilitates homologous
    recombination-based double-strand break repair in Saccharomyces cerevisiae. (1999),
    DOI10.1128/mcb.19.11.7681. Identifier/bibliographic verification is separate from
    the declared body or abstract scientific-reading scope.; PMID:11988766: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:11988766: The Mre11 complex: at the
    crossroads of dna repair and checkpoint signalling. (2002), DOI10.1038/nrm805.
    Identifier/bibliographic verification is separate from the declared body or abstract
    scientific-reading scope.; PMID:17674145: UNREACHABLE; Native Europe PMC uniquely
    identifies PMID:17674145: The multiple roles of the Mre11 complex for meiotic
    recombination. (2007), DOI10.1007/s10577-007-1147-9. Identifier/bibliographic
    verification is separate from the declared body or abstract scientific-reading
    scope.; PMID:9845372: UNREACHABLE; Native Europe PMC uniquely identifies PMID:9845372:
    Complex formation and functional versatility of Mre11 of budding yeast in recombination.
    (1998), DOI10.1016/s0092-8674(00)81640-2. Identifier/bibliographic verification
    is separate from the declared body or abstract scientific-reading scope. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro61-md-10219078
  - micro61-md-10523656
  - micro61-md-11988766
  - micro61-md-17674145
  - micro61-md-9845372
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030870
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch61 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0030870
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch61 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0030870
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch61 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0030870
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch61 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0030870
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
    and current batch61 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/mre11_complex.yaml
  locator: Entire maintained YAML, including all scientific fields, examples, graphs,
    discussions and history
  accessed_at: '2026-10-22T09:06:34Z'
  support: context_only
  summary: All target bytes were read. No neighboring maintained record supplies an
    unstated scientific premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component-class grounding and reviewed-label-only contract
  accessed_at: '2026-10-22T09:06:34Z'
  support: context_only
  summary: Species accessions establish examples, not automatic class groundings.
    Unknowns and empty optional slots alone are not defects.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum and graph actor semantics
  accessed_at: '2026-10-22T09:06:34Z'
  support: context_only
  summary: Formation necessity differs from activity, viability and localization.
    COMMON means present in most members with exceptional losses, not merely known
    occurrence.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Actor identity, source placement and descriptive versus mechanistic relationships
  accessed_at: '2026-10-22T09:06:34Z'
  support: context_only
  summary: Assay, species and epistemic boundaries apply to each graph claim. Coarse
    descriptive membership/function need not invent unresolved intermediates or copy
    ratios.
- evidence_id: micro61-md-10219078
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10219078+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:45:49.929673Z'
  support: supports
  summary: 'PMID10219078: Formation of the yeast Mre11-Rad50-Xrs2 complex is correlated
    with DNA repair and telomere maintenance. Chamankhah M, Xiao W. (1999), DOI10.1093/nar/27.10.2072.
    Complete native abstract read; this metadata row does not attest main-body access.'
  snapshot_sha256: 29ba7bfe97382c78b530ab621256b30e3755e1baaf11c18651cafd4605855c35
- evidence_id: micro61-md-10523656
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10523656+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:45:49.987428Z'
  support: supports
  summary: 'PMID10523656: The Mre11-Rad50-Xrs2 protein complex facilitates homologous
    recombination-based double-strand break repair in Saccharomyces cerevisiae. Bressan
    DA, Baxter BK, Petrini JH. (1999), DOI10.1128/mcb.19.11.7681. Complete native
    abstract read; this metadata row does not attest main-body access.'
  snapshot_sha256: 54457905173935244c7f01d8d080ee9db002eb3b20aa1408314b40ee9786a12c
- evidence_id: micro61-md-11988766
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11988766+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:45:50.553572Z'
  support: supports
  summary: 'PMID11988766: The Mre11 complex: at the crossroads of dna repair and checkpoint
    signalling. D''Amours D, Jackson SP. (2002), DOI10.1038/nrm805. Complete native
    abstract read; this metadata row does not attest main-body access.'
  snapshot_sha256: 3f5238411f78ff1fc9a487c0a9a125a28da38e9c6805439e7b25168ac8278640
- evidence_id: micro61-md-17674145
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17674145+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:45:51.266482Z'
  support: supports
  summary: 'PMID17674145: The multiple roles of the Mre11 complex for meiotic recombination.
    Borde V. (2007), DOI10.1007/s10577-007-1147-9. Complete native abstract read;
    this metadata row does not attest main-body access.'
  snapshot_sha256: 62aba7305d499c1e99fb18bf5011ddd618e784698d825a92b472227fc4a8c7e4
- evidence_id: micro61-md-9845372
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9845372+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:45:51.760601Z'
  support: supports
  summary: 'PMID9845372: Complex formation and functional versatility of Mre11 of
    budding yeast in recombination. Usui T, Ohta T, Oshiumi H, Tomizawa J, Ogawa H,
    Ogawa T. (1998), DOI10.1016/s0092-8674(00)81640-2. Complete native abstract read;
    this metadata row does not attest main-body access.'
  snapshot_sha256: 2638a27a7fac2f71c7cb3bf45c6970e2b554b656d12d61e11c1742489d283446
- evidence_id: micro61-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and relevant synonyms.
  accessed_at: '2026-10-22T08:45:47.563798Z'
  support: supports
  summary: ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. Experimental
    backgrounds are not inferred from the reference sequence strain.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: micro61-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Exact taxId, scientificName, rank, lineage and relevant synonyms.
  accessed_at: '2026-10-22T08:45:47.574335Z'
  support: supports
  summary: ENA taxId559292 identifies Saccharomyces cerevisiae S288C, rank strain.
    Experimental backgrounds are not inferred from the reference sequence strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro61-protein-P12753
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P12753.json
  locator: Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:45:47.584012Z'
  support: supports
  summary: Reviewed P12753 identifies RAD50 in taxon559292; complete function, subunit
    and location comments were inspected. InterPro cross-references establish accession
    membership separately from family-only metadata. Unlisted annotation papers are
    not certified as read.
  snapshot_sha256: 0561a1235064cbaf9985a0da920e11a97db05f2c3245d02d7a9c1baa10d3923b
- evidence_id: micro61-protein-P32829
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32829.json
  locator: Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:45:48.242305Z'
  support: supports
  summary: Reviewed P32829 identifies MRE11 in taxon559292; complete function, subunit
    and location comments were inspected. InterPro cross-references establish accession
    membership separately from family-only metadata. Unlisted annotation papers are
    not certified as read.
  snapshot_sha256: b68d4e981ac0fdfc507b8b591049f50a3a063b13c6c135357a3271607337e146
- evidence_id: micro61-protein-P33301
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33301.json
  locator: Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:45:48.486418Z'
  support: supports
  summary: Reviewed P33301 identifies XRS2 in taxon559292; complete function, subunit
    and location comments were inspected. InterPro cross-references establish accession
    membership separately from family-only metadata. Unlisted annotation papers are
    not certified as read.
  snapshot_sha256: 9f3465dbb07232e984b03432f88ab04385a8352dfbef5e1058263edf0da61df9
- evidence_id: micro61-gene-MRE11
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMRE11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set and exact gene_exact, organism_id and reviewed:true
    query in original URL.
  accessed_at: '2026-10-22T08:45:55.328156Z'
  support: supports
  summary: The exact reviewed MRE11 organism559292 query returns P32829. The sole
    returned primary gene and accession agree with the maintained example.
  snapshot_sha256: 4e2c328e7da1e58a09c12d024c8a4ec12a22a9db3f130e136da6738486e88b34
- evidence_id: micro61-gene-RAD50
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARAD50%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set and exact gene_exact, organism_id and reviewed:true
    query in original URL.
  accessed_at: '2026-10-22T08:45:55.454045Z'
  support: supports
  summary: The exact reviewed RAD50 organism559292 query returns P12753. The sole
    returned primary gene and accession agree with the maintained example.
  snapshot_sha256: 053ea50a95ee149b17f51ec0cc2ed34475f788413cbb8a6f31c0d89df9660975
- evidence_id: micro61-gene-XRS2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AXRS2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set and exact gene_exact, organism_id and reviewed:true
    query in original URL.
  accessed_at: '2026-10-22T08:45:55.564168Z'
  support: supports
  summary: The exact reviewed XRS2 organism559292 query returns P33301, P40968. The
    XRS2 result set includes the CDC40 alias collision P40968; P33301 has the exact
    primary gene XRS2. The maintained example already says representative rather than
    single-hit.
  snapshot_sha256: 3e2a27e2fddb75e0217276655b999e739a186fbafa3b0b2e87c7200145200af5
- evidence_id: micro61-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776,GO:0005730,GO:0006281,GO:0007131,GO:0030686,GO:0030870,GO:0032991,GO:0033551,GO:0034457,GO:0034463,GO:0140513
  locator: 'Only these four complete native entries: identity, definition, synonyms
    and relevant typed links.'
  accessed_at: '2026-10-22T08:45:46.871612Z'
  support: supports
  summary: GO0030870 identifies the Mre11 complex and all six exact synonyms. GO0140513
    is its nuclear protein-containing-complex parent, while GO0006281 and GO0007131
    describe the two coarse processes. The definition names three constituent classes.
  snapshot_sha256: 2d3568ba02c04018c9315aba7e1101a1a9eb6f2cb8be3d9f92ea31cfea10c19f
- evidence_id: micro61-GO0030870-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030870/ancestors?relations=is_a
  locator: Complete exact requested-term is_a ancestor array.
  accessed_at: '2026-10-22T08:45:46.871851Z'
  support: supports
  summary: The is_a-only response includes nuclear protein-containing complex GO0140513
    and broader protein-complex ancestors.
  snapshot_sha256: 40b0f8dac9be3c8b7d69b488bc8061f7ee0c61d007081d6e20ff510b0ad920b8
- evidence_id: micro61-PMC84807-ncbi2
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC84807/?report=xml
  locator: 'Genuine primary HTML: complete Methods sec1 and Table1, complete Results
    sec9 including Tables2/3 and Fig1–5 captions, complete Discussion sec14. Introduction,
    figure pixels, separate supplements and raw measurements not read.'
  accessed_at: '2026-10-22T08:49:29.318710Z'
  support: supports
  summary: The tested yeast strains, radiation/cell-cycle assays and genetic comparisons
    connect MRX to homologous-recombination DSB repair. Nuclease-deficient mre11-3
    retains assayed mitotic repair functions unlike deletion; nuclease activity, complex
    function and formation are not collapsed into one requirement.
  snapshot_sha256: 6041ca528e265601a4fc35131e89c242e6d9c231a6480e4d0bdc5594d731fec9
- evidence_id: micro61-PMC148425-legacy
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/148425/
  locator: Actual abstract and scan landing-page content only; no scanned pages inspected.
  accessed_at: '2026-10-22T08:47:33.480732Z'
  support: context_only
  summary: This genuine legacy page supplies the Chamankhah1999 abstract and scanned-PDF
    links, not a readable primary body. Scientific support is restricted to the independently
    retained complete MED abstract.
  snapshot_sha256: 99a7176d9dd0f4fef04ab77cf6092ecd958592efda87fa799eb5203d7afe2371
- evidence_id: micro61-IPR003701
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003701/
  locator: Complete type/name/descriptions/member_databases and quality flags; scope
    compared with the represented whole-protein class.
  accessed_at: '2026-10-22T08:47:34.806228Z'
  support: supports
  summary: 'IPR003701 is the DNA double-strand break repair protein Mre11 family.
    Exact name, full description, integrated signatures and quality flags were read.
    Protein membership is independently established by separate UniProt evidence. '
  snapshot_sha256: 3fcfb8beeeb6bdb77d6a892d4222bbb88a46f43d47b6d059f81801ececc8be27
- evidence_id: micro61-IPR004584
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004584/
  locator: Complete type/name/descriptions/member_databases and quality flags; scope
    compared with the represented whole-protein class.
  accessed_at: '2026-10-22T08:47:35.157164Z'
  support: supports
  summary: IPR004584 is the DNA repair protein Rad50, eukaryotes family. Exact name,
    full description, integrated signatures and quality flags were read. Protein membership
    is independently established by separate UniProt evidence. This eukaryotic Rad50
    family is distinct from the related bacterial SbcC class.
  snapshot_sha256: 7f3b442eee0df2dea9c2429cf4e335c91e763456a35483db60f10101d250d7c3
- evidence_id: micro61-IPR000253
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000253/
  locator: Complete type/name/descriptions/member_databases and quality flags; scope
    compared with the represented whole-protein class.
  accessed_at: '2026-10-22T08:47:35.241562Z'
  support: supports
  summary: IPR000253 is the Forkhead-associated (FHA) domain domain. Exact name, full
    description, integrated signatures and quality flags were read. Protein membership
    is independently established by separate UniProt evidence. This FHA domain is
    not an exact whole-Xrs2 family and is withheld as a component-class mapping.
  snapshot_sha256: ad3d5843bb1129e56bdc0a9d117e2691699119dbe5dc86bb87262f1719d6a891
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/mre11_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T08:39:57Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/mre11_complex.yaml'
  snapshot_sha256: 294a90c972f57ddde03fa10b6ae5ac5b044d7c52e81a903eecf264ee1a4ad5c2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/mre11_complex.yaml --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mre11_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T08:39:58Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/mre11_complex.yaml\
    \ --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mre11_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mre11_complex-strict.tsv"
  snapshot_sha256: 0c36af4f154e37d57164aeb29c7525f54b4181a689d533bce857d70f9d402692
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mre11_complex.yaml
    --causal-graphs
  locator: Complete focused read-only native log
  accessed_at: '2026-10-22T08:48:14.967967Z'
  support: supports
  summary: "data/structures/other/mre11_complex.yaml  (GO:0030870)\n  mre11_dna_repair_recombination\t\
    mre11_nuclease_subunit\tCOVERED\t->mre11_nuclease_subunit (UniProtKB:P32829)\n\
    \  mre11_dna_repair_recombination\trad50_atpase_subunit\tCOVERED\t->rad50_atpase_subunit\
    \ (UniProtKB:P12753)\n  mre11_dna_repair_recombination\txrs2_regulatory_subunit\t\
    COVERED\t->xrs2_regulatory_subunit (UniProtKB:P33301)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     3  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     3  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 4b0d73665f4d9271348fdc485b773f2e487aa2dc7d7d47e00fb539b7770a943b
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mre11_complex.yaml
    --verify
  locator: Complete focused read-only native log
  accessed_at: '2026-10-22T08:48:16.415712Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/mre11_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '13 of 18 collected target identifiers returned OK. PMID:10219078: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:10219078: Formation of the yeast Mre11-Rad50-Xrs2
    complex is correlated with DNA repair and telomere maintenance. (1999), DOI10.1093/nar/27.10.2072.
    Identifier/bibliographic verification is separate from the declared body or abstract
    scientific-reading scope.; PMID:10523656: UNREACHABLE; Native Europe PMC uniquely
    identifies PMID:10523656: The Mre11-Rad50-Xrs2 protein complex facilitates homologous
    recombination-based double-strand break repair in Saccharomyces cerevisiae. (1999),
    DOI10.1128/mcb.19.11.7681. Identifier/bibliographic verification is separate from
    the declared body or abstract scientific-reading scope.; PMID:11988766: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:11988766: The Mre11 complex: at the
    crossroads of dna repair and checkpoint signalling. (2002), DOI10.1038/nrm805.
    Identifier/bibliographic verification is separate from the declared body or abstract
    scientific-reading scope.; PMID:17674145: UNREACHABLE; Native Europe PMC uniquely
    identifies PMID:17674145: The multiple roles of the Mre11 complex for meiotic
    recombination. (2007), DOI10.1007/s10577-007-1147-9. Identifier/bibliographic
    verification is separate from the declared body or abstract scientific-reading
    scope.; PMID:9845372: UNREACHABLE; Native Europe PMC uniquely identifies PMID:9845372:
    Complex formation and functional versatility of Mre11 of budding yeast in recombination.
    (1998), DOI10.1016/s0092-8674(00)81640-2. Identifier/bibliographic verification
    is separate from the declared body or abstract scientific-reading scope. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
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
  topic: Supported MRX/MRN class with a scoped budding-yeast third subunit
  outcome: supported
  target_ids:
  - GO:0030870
  summary: The current GO identity, exact synonym qualifications and nuclear parent
    agree. The maintained third component is specifically Xrs2, preserving the prior
    correction rather than claiming a universal Xrs2/Nbs1 protein identity.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-go
  - micro61-GO0030870-ancestors
  - micro61-md-10219078
  - micro61-md-10523656
  - micro61-md-11988766
  - micro61-md-17674145
  - micro61-md-9845372
  - micro61-protein-P12753
  - micro61-protein-P32829
  - micro61-protein-P33301
- assessment_id: grounding
  area: grounding
  topic: Two exact whole-protein families and one unresolved domain boundary
  outcome: concern
  target_ids:
  - GO:0030870
  summary: IPR003701 Mre11 and eukaryotic IPR004584 Rad50 match represented classes
    with independent native accession cross-references. Xrs2 FHA domain IPR000253
    is not substituted for a whole-family identifier.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-IPR003701
  - micro61-IPR004584
  - micro61-IPR000253
  - micro61-protein-P12753
  - micro61-protein-P32829
  - micro61-protein-P33301
- assessment_id: graph
  area: graph
  topic: Three constituent classes and coarse repair functions
  outcome: supported
  target_ids:
  - GO:0030870
  summary: The five NONMECHANISTIC edges state three constituents and repair/recombination
    roles supported by GO and source-specific literature. The graph scope explicitly
    names three classes; its trimeric wording is not treated as a numerical1:1:1 assertion.
    Native comments describe two Mre11/two Rad50/one Xrs2 copies, so class count must
    not be silently converted into molecular stoichiometry.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-go
  - micro61-PMC84807-ncbi2
  - micro61-md-10219078
  - micro61-md-10523656
  - micro61-md-11988766
  - micro61-md-17674145
  - micro61-md-9845372
  - micro61-protein-P12753
  - micro61-protein-P32829
  - micro61-protein-P33301
- assessment_id: formation
  area: evidence
  topic: Unknown labels preserve domain and assay dependence
  outcome: unknown
  target_ids:
  - GO:0030870
  summary: All three UNKNOWN labels remain defensible. Chamankhah abstract reports
    domain-dependent interactions and functional correlations, including a deletion
    retaining mitotic functions; Bressan separates nuclease and repair functions.
    These do not establish exhaustive universal physical-formation dependencies.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-PMC84807-ncbi2
  - micro61-md-10219078
  - micro61-md-10523656
  - micro61-md-11988766
  - micro61-md-17674145
  - micro61-md-9845372
- assessment_id: examples
  area: grounding
  topic: Reference identities and an acknowledged query collision
  outcome: supported
  target_ids:
  - GO:0030870
  summary: The three reviewed S288C proteins and Usui1998 nuclear annotation identities
    agree. MRE11/RAD50 exact queries are single-hit; XRS2 also returns CDC40 through
    an alias, and the maintained P33301 example already correctly says representative.
    No uniqueness correction is warranted.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-protein-P12753
  - micro61-protein-P32829
  - micro61-protein-P33301
  - micro61-gene-MRE11
  - micro61-gene-RAD50
  - micro61-gene-XRS2
  - micro61-md-10219078
  - micro61-md-10523656
  - micro61-md-11988766
  - micro61-md-17674145
  - micro61-md-9845372
- assessment_id: scope
  area: scope
  topic: Budding-yeast context and qualified comparative terminology
  outcome: supported
  target_ids:
  - GO:0030870
  summary: COMMON retains majority occurrence with exceptional losses, supported qualitatively
    but not by a strain census. Bressan assay strains/cell-cycle/radiation conditions
    are distinct from S288C reference sequences. D’Amours/Jackson and Borde are secondary
    reviews at complete abstract tier, not independently observed experiments.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-tax4932
  - micro61-tax559292
  - micro61-PMC84807-ncbi2
  - micro61-md-10219078
  - micro61-md-10523656
  - micro61-md-11988766
  - micro61-md-17674145
  - micro61-md-9845372
- assessment_id: coverage
  area: completeness
  topic: Complete target review with bounded unresolved details
  outcome: supported
  target_ids:
  - GO:0030870
  summary: All scientific fields, example identities, graphs, current discussions
    and history were read. Actionable exact mappings are distinguished from optional
    inventory enrichment, broader domain candidates and historical first-pass statements.
    No maintained scientific content was changed.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-go
  - micro61-GO0030870-ancestors
  - micro61-PMC84807-ncbi2
  - micro61-PMC148425-legacy
  - micro61-IPR000253
  - micro61-IPR003701
  - micro61-IPR004584
  - micro61-md-10219078
  - micro61-md-10523656
  - micro61-md-11988766
  - micro61-md-17674145
  - micro61-md-9845372
  - micro61-tax4932
  - micro61-tax559292
  - micro61-protein-P12753
  - micro61-protein-P32829
  - micro61-protein-P33301
  - micro61-gene-MRE11
  - micro61-gene-RAD50
  - micro61-gene-XRS2
findings:
- finding_id: F1
  issue_key: mre11-rad50-exact-family-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the Mre11 and Rad50 constituent classes
  description: The represented Mre11 and Rad50 classes remain REVIEWED_LABEL_ONLY
    despite exact verified IPR003701 and eukaryotic IPR004584 families and separate
    accession cross-references. Xrs2 remains unresolved at whole-family level; the
    reviewed FHA domain is insufficient.
  target_ids:
  - GO:0030870
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-IPR003701
  - micro61-IPR004584
  - micro61-protein-P12753
  - micro61-protein-P32829
  - micro61-protein-P33301
  - micro61-IPR000253
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mre11_complex.yaml
    role: maintained scientific record
  rule_id: Exact component-class grounding and reviewed-label-only contract
  native_severity: minor
  normalization_reason: Existing identities and scientific membership are supported.
    This localized correction supplies verified class identifiers without changing
    the complex model or treating a historical first-pass search as false.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0030870
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mre11_complex.yaml
    role: maintained scientific record
  description: Add IPR003701 for Mre11 and IPR004584 for Rad50; update current grounding
    notes/status and the open task. Preserve the Xrs2-specific third row, representative
    XRS2 example, UNKNOWN essentiality and distinction between class count and molecular
    copy number.
  acceptance_checks:
  - The added family identifiers match the named whole-protein classes and independently
    verified member identities.
  - Current grounding status and discussion reflect the verified mappings while broader
    candidates and UNKNOWN formation labels remain qualified.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- Bressan1999 was read in complete Methods/Results/Discussion with the declared tables/captions,
  not Introduction, figure pixels or raw data. Chamankhah1999 and Usui1998 were read
  at complete native abstract tier; Chamankhah scan links did not yield a readable
  body. D’Amours/Jackson2002 and Borde2007 are secondary-review abstracts only.
- The record explicitly models three constituent classes; no1:1:1 copy ratio is inferred
  from trimeric wording. Native stoichiometric comments are not a new quantitative
  reconstitution analysis. Domain-interaction/function evidence does not force universal
  formation necessity.
- Xrs2 FHA is a domain, not a whole-family mapping. XRS2 query alias collision is
  acknowledged in the existing representative example. COMMON retains majority meaning
  without an exhaustive prevalence census.
- Original source URL, UTC and SHA256 are retained. HTTP status alone does not establish
  article-body readability; initial DNS failures and unsuccessful access responses
  remain diagnostic only.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requests a review for every unreviewed record, including qualified
  clean cases.
- Initial inspections and failed access attempts are preserved. No scientific record,
  historical review, index or Git state was edited.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
