# Source-backed review of mpp10 complex

- Review: 20261022T090914Z-mpp10-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T08:39:53Z
- Finished UTC: 2026-10-22T09:09:14Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor: the represented Mpp10 constituent has an exact verified family mapping. The three-protein module, example identities and coarse Pwp2/UTP-B assembly branch are supported with explicit experimental limits.

## Scope And Provenance

Exactly one entire maintained target and 14 frozen inputs. No neighboring maintained record is an unstated premise. Actual source tiers/read extents are declared per evidence row.

Selection: Batch61 strict ordered selection index 5; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0034457 | data/structures/other/mpp10_complex.yaml | maintained | Mpp10 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0034457 | Focused validator passed. |
| Focused native strict | passed | True | GO:0034457 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0034457 | Focused check passed; scientific assertions were independently assessed. |
| Focused native verify | passed | True | GO:0034457 | Focused check passed; scientific assertions were independently assessed. |
| Claim-level scientific review | passed | True | GO:0034457 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0034457 | 11 of 15 collected target identifiers returned OK. PMID:10409734: UNREACHABLE; Native Europe PMC uniquely identifies PMID:10409734: Imp3p and Imp4p, two specific components of the U3 small nucleolar ribonucleoprotein that are essential for pre-18S rRNA processing. (1999), DOI10.1128/mcb.19.8.5441. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:12068309: UNREACHABLE; Native Europe PMC uniquely identifies PMID:12068309: A large nucleolar U3 ribonucleoprotein required for 18S ribosomal RNA biogenesis. (2002), DOI10.1038/nature00769. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:17515605: UNREACHABLE; Native Europe PMC uniquely identifies PMID:17515605: The 90S preribosome is a multimodular structure that is assembled through a hierarchical mechanism. (2007), DOI10.1128/mcb.00380-07. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:9315638: UNREACHABLE; Native Europe PMC uniquely identifies PMID:9315638: Mpp10p, a U3 small nucleolar ribonucleoprotein component required for pre-18S rRNA processing in yeast. (1997), DOI10.1128/mcb.17.10.5803. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0034457 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0034457 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0034457 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0034457 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0034457 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact three-protein 90S module

identity: supported. Targets: GO:0034457.

The Mpp10 complex identity, nuclear parent and nucleolus/90S placements agree with native authorities. The three named budding-yeast constituent classes are supported by the primary source and earlier native abstracts.

### Exact Mpp10 family with two unresolved narrower boundaries

grounding: concern. Targets: GO:0034457.

IPR012173 matches Mpp10 itself, independently corroborated by its native accession and five reviewed members. The broader uS4 and Imp4/Rpf1 families do not establish exact Imp3 or Imp4 groundings; empty candidate-subfamily responses remain access limits.

### Coarse Pwp2/UTP-B branch is source supported

graph: supported. Targets: GO:0034457.

The five NONMECHANISTIC edges state three constituents, 90S parthood and support for assembly. The source supports this module/branch relationship while leaving sequential versus joint assembly and unmodeled factors unresolved; the record does not claim a strict order among the three subunits.

### Unknown necessity is distinct from processing or growth

evidence: unknown. Targets: GO:0034457.

All three component UNKNOWN labels are retained. Depletion/coprotein recovery and essential rRNA-processing functions are informative but do not establish a universal all-subunit physical-formation requirement. No corrective finding follows from optional missing necessity detail.

### Three verified reference proteins

grounding: supported. Targets: GO:0034457.

Reviewed Mpp10/Imp3/Imp4 S288C identities, exact single-hit gene queries and location annotation citations agree. Dunbar and Lee complete abstracts support U3/processing context, while their detailed body methods are not claimed as inspected.

### Model-system evidence with an uncensused majority qualifier

scope: supported. Targets: GO:0034457.

COMMON retains present-in-most-members and exceptional losses. The sources qualitatively support the budding-yeast system; S288C reference identities do not substitute for experimental construct details or an exhaustive strain prevalence survey. Analogous eukaryotic complexes are permitted by the native term without exporting every yeast dependency.

### Complete target review with bounded unresolved details

completeness: supported. Targets: GO:0034457.

All scientific fields, example identities, graphs, current discussions and history were read. Actionable exact mappings are distinguished from optional inventory enrichment, broader domain candidates and historical first-pass statements. No maintained scientific content was changed.

## Findings

### F1: Ground the Mpp10 constituent to its verified family

minor / open / confirmed; issue key: mpp10-exact-family-grounding.

The represented Mpp10 class remains REVIEWED_LABEL_ONLY, although native whole-family IPR012173, independent accession cross-reference and reviewed member identities now provide exact grounding. The Imp3 and Imp4 candidate families remain broader and are not forced.

## Recommended Actions And Acceptance Checks

### A1

Add IPR012173 for Mpp10 and update its current grounding note/status and the open discussion. Retain bounded Imp3/Imp4 family uncertainty and UNKNOWN essentiality; do not interpret empty candidate responses as ontology absence.

- The added family identifiers match the named whole-protein classes and independently verified member identities.
- Current grounding status and discussion reflect the verified mappings while broader candidates and UNKNOWN formation labels remain qualified.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/mpp10_complex.yaml; Entire maintained YAML, including all scientific fields, examples, graphs, discussions and history | context_only | All target bytes were read. No neighboring maintained record supplies an unstated scientific premise. |
| curation | docs/CURATION.md; Component-class grounding and reviewed-label-only contract | context_only | Species accessions establish examples, not automatic class groundings. Unknowns and empty optional slots alone are not defects. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum and graph actor semantics | context_only | Formation necessity differs from activity, viability and localization. COMMON means present in most members with exceptional losses, not merely known occurrence. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Actor identity, source placement and descriptive versus mechanistic relationships | context_only | Assay, species and epistemic boundaries apply to each graph claim. Coarse descriptive membership/function need not invent unresolved intermediates or copy ratios. |
| micro61-md-10409734 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10409734+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID10409734: Imp3p and Imp4p, two specific components of the U3 small nucleolar ribonucleoprotein that are essential for pre-18S rRNA processing. Lee SJ, Baserga SJ. (1999), DOI10.1128/mcb.19.8.5441. Complete native abstract read; this metadata row does not attest main-body access. |
| micro61-md-12068309 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12068309+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID12068309: A large nucleolar U3 ribonucleoprotein required for 18S ribosomal RNA biogenesis. Dragon F, Gallagher JE, Compagnone-Post PA, Mitchell BM, Porwancher KA, Wehner KA, Wormsley S, Settlage RE, Shabanowitz J, Osheim Y, Beyer AL, Hunt DF, Baserga SJ. (2002), DOI10.1038/nature00769. Complete native abstract read; this metadata row does not attest main-body access. |
| micro61-md-17515605 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17515605+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID17515605: The 90S preribosome is a multimodular structure that is assembled through a hierarchical mechanism. Pérez-Fernández J, Román A, De Las Rivas J, Bustelo XR, Dosil M. (2007), DOI10.1128/mcb.00380-07. Complete native abstract read; this metadata row does not attest main-body access. |
| micro61-md-9315638 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9315638+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID9315638: Mpp10p, a U3 small nucleolar ribonucleoprotein component required for pre-18S rRNA processing in yeast. Dunbar DA, Wormsley S, Agentis TM, Baserga SJ. (1997), DOI10.1128/mcb.17.10.5803. Complete native abstract read; this metadata row does not attest main-body access. |
| micro61-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and relevant synonyms. | supports | ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. Experimental backgrounds are not inferred from the reference sequence strain. |
| micro61-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Exact taxId, scientificName, rank, lineage and relevant synonyms. | supports | ENA taxId559292 identifies Saccharomyces cerevisiae S288C, rank strain. Experimental backgrounds are not inferred from the reference sequence strain. |
| micro61-protein-P32899 | https://rest.uniprot.org/uniprotkb/P32899.json; Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments; InterPro cross-references. | supports | Reviewed P32899 identifies IMP3 in taxon559292; complete function, subunit and location comments were inspected. InterPro cross-references establish accession membership separately from family-only metadata. Unlisted annotation papers are not certified as read. |
| micro61-protein-P47083 | https://rest.uniprot.org/uniprotkb/P47083.json; Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments; InterPro cross-references. | supports | Reviewed P47083 identifies MPP10 in taxon559292; complete function, subunit and location comments were inspected. InterPro cross-references establish accession membership separately from family-only metadata. Unlisted annotation papers are not certified as read. |
| micro61-protein-P53941 | https://rest.uniprot.org/uniprotkb/P53941.json; Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments; InterPro cross-references. | supports | Reviewed P53941 identifies IMP4 in taxon559292; complete function, subunit and location comments were inspected. InterPro cross-references establish accession membership separately from family-only metadata. Unlisted annotation papers are not certified as read. |
| micro61-gene-MPP10 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMPP10%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set and exact gene_exact, organism_id and reviewed:true query in original URL. | supports | The exact reviewed MPP10 organism559292 query returns P47083. The sole returned primary gene and accession agree with the maintained example. |
| micro61-gene-IMP3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIMP3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set and exact gene_exact, organism_id and reviewed:true query in original URL. | supports | The exact reviewed IMP3 organism559292 query returns P32899. The sole returned primary gene and accession agree with the maintained example. |
| micro61-gene-IMP4 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIMP4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set and exact gene_exact, organism_id and reviewed:true query in original URL. | supports | The exact reviewed IMP4 organism559292 query returns P53941. The sole returned primary gene and accession agree with the maintained example. |
| micro61-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776,GO:0005730,GO:0006281,GO:0007131,GO:0030686,GO:0030870,GO:0032991,GO:0033551,GO:0034457,GO:0034463,GO:0140513; Only these five complete native entries: identity, definition, comments and relevant typed links. | supports | GO0034457 identifies the Mpp10/Imp3/Imp4 module, with nuclear protein-containing-complex parent and nucleolus/90S placement. GO0140513, GO0005730, GO0030686 and GO0034463 distinguish parent, locations and assembly process. |
| micro61-GO0034457-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034457/ancestors?relations=is_a; Complete requested-term is_a ancestor array. | supports | The exact is_a-only response includes nuclear protein-containing complex GO0140513 and its broader complex ancestors. Nucleolus/90S placement is assessed separately. |
| micro61-PMC1952102-ncbi2 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1952102/?report=xml; Genuine primary HTML despite report=xml URL: Methods sec2–6, Results sec9 and sec12, complete Discussion sec15; embedded Fig2/4/5/6/8 captions. Results sec10/11/13/14, separate supplementary tables and pixels not read. | supports | Depletion, coimmunoprecipitation and mass-spectrometry analyses support a Mpp10 module connected to the Pwp2/UTP-B branch. Thresholded copurification and dependence do not resolve a strict universal sequence; the discussion expressly permits coassembly and tentative earlier U3 interaction. |
| micro61-IPR012173 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012173/; Complete type/name/descriptions/member_databases and quality flags; scope compared with the represented whole-protein class. | supports | IPR012173 is the U3 small nucleolar ribonucleoprotein complex, subunit Mpp10 family. Exact name, full description, integrated signatures and quality flags were read. Protein membership is independently established by separate UniProt evidence.  |
| micro61-IPR012173-reviewed-members | https://rest.uniprot.org/uniprotkb/search?query=xref%3Ainterpro-IPR012173+AND+reviewed%3Atrue&amp;format=json&amp;size=100&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_name%2Corganism_id; Complete returned accession/status/primary-gene/taxon identity set and exact InterPro query URL; not all unreviewed members. | supports | The bounded reviewed member query returns 5 identities: O00566, P47083, Q9FJY5, Q810V0, O13910. The five reviewed identities span eukaryotic Mpp10 examples, supporting the whole-family mapping rather than only a budding-yeast instance. |
| micro61-IPR022801 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022801/; Complete type/name/descriptions/member_databases and quality flags; scope compared with the represented whole-protein class. | supports | IPR022801 is the Small ribosomal subunit protein uS4 family. Exact name, full description, integrated signatures and quality flags were read. Protein membership is independently established by separate UniProt evidence. This uS4 family includes ribosomal S4 as well as Imp3, so is not accepted as exact Imp3-only grounding. |
| micro61-IPR044281 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044281/; Complete type/name/descriptions/member_databases and quality flags; scope compared with the represented whole-protein class. | supports | IPR044281 is the U3 snoRNP protein/Ribosome production factor 1 family. Exact name, full description, integrated signatures and quality flags were read. Protein membership is independently established by separate UniProt evidence. The family includes both Imp4 and Rpf1, so its broader label is not substituted for an exact Imp4 class. |
| micro61-PTHR11831-SF1 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR11831:SF1/; Exact retained transport receipt and empty raw payload. | context_only | The candidate subfamily endpoint returned HTTP204 with an empty body. It supplies no native class description and does not establish that an exact family is absent. |
| micro61-PTHR22734-SF2 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR22734:SF2/; Exact retained transport receipt and empty raw payload. | context_only | The candidate subfamily endpoint returned HTTP204 with an empty body. It supplies no native class description and does not establish that an exact family is absent. |
| schema-result | just validate data/structures/other/mpp10_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/mpp10_complex.yaml |
| strict-result | just validate-strict data/structures/other/mpp10_complex.yaml --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mpp10_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/mpp10_complex.yaml --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mpp10_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mpp10_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mpp10_complex.yaml --causal-graphs; Complete focused read-only native log | supports | data/structures/other/mpp10_complex.yaml  (GO:0034457)<br>  yeast_mpp10_90s_preribosome_assembly	mpp10_mpp10_complex_subunit	COVERED	-&gt;mpp10_mpp10_complex_subunit (UniProtKB:P47083)<br>  yeast_mpp10_90s_preribosome_assembly	imp3_mpp10_complex_subunit	COVERED	-&gt;imp3_mpp10_complex_subunit (UniProtKB:P32899)<br>  yeast_mpp10_90s_preribosome_assembly	imp4_mpp10_complex_subunit	COVERED	-&gt;imp4_mpp10_complex_subunit (UniProtKB:P53941)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mpp10_complex.yaml --verify; Complete focused read-only native log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/mpp10_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 15 collected target identifiers returned OK. PMID:10409734: UNREACHABLE; Native Europe PMC uniquely identifies PMID:10409734: Imp3p and Imp4p, two specific components of the U3 small nucleolar ribonucleoprotein that are essential for pre-18S rRNA processing. (1999), DOI10.1128/mcb.19.8.5441. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:12068309: UNREACHABLE; Native Europe PMC uniquely identifies PMID:12068309: A large nucleolar U3 ribonucleoprotein required for 18S ribosomal RNA biogenesis. (2002), DOI10.1038/nature00769. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:17515605: UNREACHABLE; Native Europe PMC uniquely identifies PMID:17515605: The 90S preribosome is a multimodular structure that is assembled through a hierarchical mechanism. (2007), DOI10.1128/mcb.00380-07. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:9315638: UNREACHABLE; Native Europe PMC uniquely identifies PMID:9315638: Mpp10p, a U3 small nucleolar ribonucleoprotein component required for pre-18S rRNA processing in yeast. (1997), DOI10.1128/mcb.17.10.5803. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Perez-Fernandez2007 was read only in Methods sec2–6, Results sec9/12 and Discussion sec15 with specified embedded captions. Other Results, separate supplements, raw MS data and figure pixels were not read. Earlier papers were read at complete native abstract tier only.
- Copurification thresholds and depletion dependencies support a module/branch but do not resolve every assembly order or universal formation necessity. COMMON retains majority semantics without a population census.
- IPR022801 and IPR044281 are broader than the exact Imp3/Imp4 classes. PANTHER candidate responses were HTTP204 empty; no absence inference is made. Earlier failed/challenge body responses remain retained separately from the genuine ncbi2 HTML.
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
review_id: 20261022T090914Z-mpp10-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of mpp10 complex
started_at: '2026-10-22T08:39:53Z'
finished_at: '2026-10-22T09:09:14Z'
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
summary: 'One minor: the represented Mpp10 constituent has an exact verified family
  mapping. The three-protein module, example identities and coarse Pwp2/UTP-B assembly
  branch are supported with explicit experimental limits.'
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
  - path: data/structures/other/mpp10_complex.yaml
    sha256: 6bf32fcf28495ebdb11c5498d3d44a98933b39fd7ec86e7ba0fc1e46b0773809
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
- target_id: GO:0034457
  path: data/structures/other/mpp10_complex.yaml
  label: Mpp10 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mpp10_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire maintained target and 14 frozen inputs. No neighboring
    maintained record is an unstated premise. Actual source tiers/read extents are
    declared per evidence row.
  selection: Batch61 strict ordered selection index 5; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0034457
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0034457
  command: just validate data/structures/other/mpp10_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0034457
  command: just validate-strict data/structures/other/mpp10_complex.yaml --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mpp10_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0034457
  command: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mpp10_complex.yaml
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
  - GO:0034457
  command: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mpp10_complex.yaml
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
  - GO:0034457
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-md-10409734
  - micro61-md-12068309
  - micro61-md-17515605
  - micro61-md-9315638
  - micro61-tax4932
  - micro61-tax559292
  - micro61-protein-P32899
  - micro61-protein-P47083
  - micro61-protein-P53941
  - micro61-gene-MPP10
  - micro61-gene-IMP3
  - micro61-gene-IMP4
  - micro61-go
  - micro61-GO0034457-ancestors
  - micro61-PMC1952102-ncbi2
  - micro61-IPR012173
  - micro61-IPR012173-reviewed-members
  - micro61-IPR022801
  - micro61-IPR044281
  - micro61-PTHR11831-SF1
  - micro61-PTHR22734-SF2
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0034457
  summary: '11 of 15 collected target identifiers returned OK. PMID:10409734: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:10409734: Imp3p and Imp4p, two specific
    components of the U3 small nucleolar ribonucleoprotein that are essential for
    pre-18S rRNA processing. (1999), DOI10.1128/mcb.19.8.5441. Identifier/bibliographic
    verification is separate from the declared body or abstract scientific-reading
    scope.; PMID:12068309: UNREACHABLE; Native Europe PMC uniquely identifies PMID:12068309:
    A large nucleolar U3 ribonucleoprotein required for 18S ribosomal RNA biogenesis.
    (2002), DOI10.1038/nature00769. Identifier/bibliographic verification is separate
    from the declared body or abstract scientific-reading scope.; PMID:17515605: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:17515605: The 90S preribosome is a
    multimodular structure that is assembled through a hierarchical mechanism. (2007),
    DOI10.1128/mcb.00380-07. Identifier/bibliographic verification is separate from
    the declared body or abstract scientific-reading scope.; PMID:9315638: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:9315638: Mpp10p, a U3 small nucleolar
    ribonucleoprotein component required for pre-18S rRNA processing in yeast. (1997),
    DOI10.1128/mcb.17.10.5803. Identifier/bibliographic verification is separate from
    the declared body or abstract scientific-reading scope. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - micro61-md-10409734
  - micro61-md-12068309
  - micro61-md-17515605
  - micro61-md-9315638
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0034457
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
  - GO:0034457
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
  - GO:0034457
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
  - GO:0034457
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
  - GO:0034457
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
  reference: data/structures/other/mpp10_complex.yaml
  locator: Entire maintained YAML, including all scientific fields, examples, graphs,
    discussions and history
  accessed_at: '2026-10-22T09:06:20Z'
  support: context_only
  summary: All target bytes were read. No neighboring maintained record supplies an
    unstated scientific premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component-class grounding and reviewed-label-only contract
  accessed_at: '2026-10-22T09:06:20Z'
  support: context_only
  summary: Species accessions establish examples, not automatic class groundings.
    Unknowns and empty optional slots alone are not defects.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum and graph actor semantics
  accessed_at: '2026-10-22T09:06:20Z'
  support: context_only
  summary: Formation necessity differs from activity, viability and localization.
    COMMON means present in most members with exceptional losses, not merely known
    occurrence.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Actor identity, source placement and descriptive versus mechanistic relationships
  accessed_at: '2026-10-22T09:06:20Z'
  support: context_only
  summary: Assay, species and epistemic boundaries apply to each graph claim. Coarse
    descriptive membership/function need not invent unresolved intermediates or copy
    ratios.
- evidence_id: micro61-md-10409734
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10409734+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:45:49.935085Z'
  support: supports
  summary: 'PMID10409734: Imp3p and Imp4p, two specific components of the U3 small
    nucleolar ribonucleoprotein that are essential for pre-18S rRNA processing. Lee
    SJ, Baserga SJ. (1999), DOI10.1128/mcb.19.8.5441. Complete native abstract read;
    this metadata row does not attest main-body access.'
  snapshot_sha256: 2ae838a6a4cb82cf10712066fc11f7ab5accd940603b2ed374491918fb812855
- evidence_id: micro61-md-12068309
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12068309+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:45:50.563241Z'
  support: supports
  summary: 'PMID12068309: A large nucleolar U3 ribonucleoprotein required for 18S
    ribosomal RNA biogenesis. Dragon F, Gallagher JE, Compagnone-Post PA, Mitchell
    BM, Porwancher KA, Wehner KA, Wormsley S, Settlage RE, Shabanowitz J, Osheim Y,
    Beyer AL, Hunt DF, Baserga SJ. (2002), DOI10.1038/nature00769. Complete native
    abstract read; this metadata row does not attest main-body access.'
  snapshot_sha256: 1ebbcec0027076bb20fa3ae2ab6b77cdf6c0e2c7324968e68135cea0b8356008
- evidence_id: micro61-md-17515605
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17515605+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:45:51.222593Z'
  support: supports
  summary: 'PMID17515605: The 90S preribosome is a multimodular structure that is
    assembled through a hierarchical mechanism. Pérez-Fernández J, Román A, De Las
    Rivas J, Bustelo XR, Dosil M. (2007), DOI10.1128/mcb.00380-07. Complete native
    abstract read; this metadata row does not attest main-body access.'
  snapshot_sha256: 9d88d8c155369cbc3190743f4bc6de637862293798aefc0acde76593b74ed25c
- evidence_id: micro61-md-9315638
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9315638+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:45:51.266679Z'
  support: supports
  summary: 'PMID9315638: Mpp10p, a U3 small nucleolar ribonucleoprotein component
    required for pre-18S rRNA processing in yeast. Dunbar DA, Wormsley S, Agentis
    TM, Baserga SJ. (1997), DOI10.1128/mcb.17.10.5803. Complete native abstract read;
    this metadata row does not attest main-body access.'
  snapshot_sha256: 4d74fe15e7262ac2a8affd65e35910cc6ff6829d56b4349526e9966c2ed70e08
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
- evidence_id: micro61-protein-P32899
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32899.json
  locator: Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:45:48.435341Z'
  support: supports
  summary: Reviewed P32899 identifies IMP3 in taxon559292; complete function, subunit
    and location comments were inspected. InterPro cross-references establish accession
    membership separately from family-only metadata. Unlisted annotation papers are
    not certified as read.
  snapshot_sha256: cda12bb1970715ba9b5457fa1a1785a932486ab071cd965fc3ff3b6aa95a1e25
- evidence_id: micro61-protein-P47083
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47083.json
  locator: Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:45:49.083103Z'
  support: supports
  summary: Reviewed P47083 identifies MPP10 in taxon559292; complete function, subunit
    and location comments were inspected. InterPro cross-references establish accession
    membership separately from family-only metadata. Unlisted annotation papers are
    not certified as read.
  snapshot_sha256: c1a5f425ac3d98aaac85da7d11fe4b9aa2c78d427bed9672cf89cf694ca68b33
- evidence_id: micro61-protein-P53941
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53941.json
  locator: Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:45:49.208700Z'
  support: supports
  summary: Reviewed P53941 identifies IMP4 in taxon559292; complete function, subunit
    and location comments were inspected. InterPro cross-references establish accession
    membership separately from family-only metadata. Unlisted annotation papers are
    not certified as read.
  snapshot_sha256: d1d2d2cf3293909f786621331ca75b499c6db5320923e1bce9c4052fbd5144ee
- evidence_id: micro61-gene-MPP10
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMPP10%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set and exact gene_exact, organism_id and reviewed:true
    query in original URL.
  accessed_at: '2026-10-22T08:45:54.570530Z'
  support: supports
  summary: The exact reviewed MPP10 organism559292 query returns P47083. The sole
    returned primary gene and accession agree with the maintained example.
  snapshot_sha256: eb2320e82a436569d0f0b1d66df394fd80990b88e8cef13ec7ca4f1a00ac1233
- evidence_id: micro61-gene-IMP3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIMP3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set and exact gene_exact, organism_id and reviewed:true
    query in original URL.
  accessed_at: '2026-10-22T08:45:54.699690Z'
  support: supports
  summary: The exact reviewed IMP3 organism559292 query returns P32899. The sole returned
    primary gene and accession agree with the maintained example.
  snapshot_sha256: 2b25b38cdd270572df80fe51c2dfd0c5c1d03cd7a2b238838a54dbf4b323c082
- evidence_id: micro61-gene-IMP4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIMP4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set and exact gene_exact, organism_id and reviewed:true
    query in original URL.
  accessed_at: '2026-10-22T08:45:54.864499Z'
  support: supports
  summary: The exact reviewed IMP4 organism559292 query returns P53941. The sole returned
    primary gene and accession agree with the maintained example.
  snapshot_sha256: 626c311b4a7d360171a56d236110b78dbf4a2551659cf33eaefde716fcc83d5c
- evidence_id: micro61-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776,GO:0005730,GO:0006281,GO:0007131,GO:0030686,GO:0030870,GO:0032991,GO:0033551,GO:0034457,GO:0034463,GO:0140513
  locator: 'Only these five complete native entries: identity, definition, comments
    and relevant typed links.'
  accessed_at: '2026-10-22T08:45:46.871612Z'
  support: supports
  summary: GO0034457 identifies the Mpp10/Imp3/Imp4 module, with nuclear protein-containing-complex
    parent and nucleolus/90S placement. GO0140513, GO0005730, GO0030686 and GO0034463
    distinguish parent, locations and assembly process.
  snapshot_sha256: 2d3568ba02c04018c9315aba7e1101a1a9eb6f2cb8be3d9f92ea31cfea10c19f
- evidence_id: micro61-GO0034457-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034457/ancestors?relations=is_a
  locator: Complete requested-term is_a ancestor array.
  accessed_at: '2026-10-22T08:45:46.871880Z'
  support: supports
  summary: The exact is_a-only response includes nuclear protein-containing complex
    GO0140513 and its broader complex ancestors. Nucleolus/90S placement is assessed
    separately.
  snapshot_sha256: 1a43a9e75b341d51e03c899d29322c4874a4fc8d83781c90179669adff6456df
- evidence_id: micro61-PMC1952102-ncbi2
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1952102/?report=xml
  locator: 'Genuine primary HTML despite report=xml URL: Methods sec2–6, Results sec9
    and sec12, complete Discussion sec15; embedded Fig2/4/5/6/8 captions. Results
    sec10/11/13/14, separate supplementary tables and pixels not read.'
  accessed_at: '2026-10-22T08:49:29.318594Z'
  support: supports
  summary: Depletion, coimmunoprecipitation and mass-spectrometry analyses support
    a Mpp10 module connected to the Pwp2/UTP-B branch. Thresholded copurification
    and dependence do not resolve a strict universal sequence; the discussion expressly
    permits coassembly and tentative earlier U3 interaction.
  snapshot_sha256: 611db5496dc717616abf2af115199530517682584a037886c15ee06527f5ae86
- evidence_id: micro61-IPR012173
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012173/
  locator: Complete type/name/descriptions/member_databases and quality flags; scope
    compared with the represented whole-protein class.
  accessed_at: '2026-10-22T08:47:34.559910Z'
  support: supports
  summary: 'IPR012173 is the U3 small nucleolar ribonucleoprotein complex, subunit
    Mpp10 family. Exact name, full description, integrated signatures and quality
    flags were read. Protein membership is independently established by separate UniProt
    evidence. '
  snapshot_sha256: 1b4fca8fe2c638fc61ac8ef46e28226c26ae081186e2b9080fdddd0b5d2c6ebd
- evidence_id: micro61-IPR012173-reviewed-members
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=xref%3Ainterpro-IPR012173+AND+reviewed%3Atrue&format=json&size=100&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_name%2Corganism_id
  locator: Complete returned accession/status/primary-gene/taxon identity set and
    exact InterPro query URL; not all unreviewed members.
  accessed_at: '2026-10-22T08:49:30.541552Z'
  support: supports
  summary: 'The bounded reviewed member query returns 5 identities: O00566, P47083,
    Q9FJY5, Q810V0, O13910. The five reviewed identities span eukaryotic Mpp10 examples,
    supporting the whole-family mapping rather than only a budding-yeast instance.'
  snapshot_sha256: 0f1537f94785d3d9fad716a95dd6411593f88cb31cba6a6220d56e2aa1bb2b20
- evidence_id: micro61-IPR022801
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022801/
  locator: Complete type/name/descriptions/member_databases and quality flags; scope
    compared with the represented whole-protein class.
  accessed_at: '2026-10-22T08:47:34.634583Z'
  support: supports
  summary: IPR022801 is the Small ribosomal subunit protein uS4 family. Exact name,
    full description, integrated signatures and quality flags were read. Protein membership
    is independently established by separate UniProt evidence. This uS4 family includes
    ribosomal S4 as well as Imp3, so is not accepted as exact Imp3-only grounding.
  snapshot_sha256: 00c2dcffb31da3096a2ef5fb7a56ce99e1d7d4d6bdb7a95908a953b687783bfd
- evidence_id: micro61-IPR044281
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044281/
  locator: Complete type/name/descriptions/member_databases and quality flags; scope
    compared with the represented whole-protein class.
  accessed_at: '2026-10-22T08:47:34.764428Z'
  support: supports
  summary: IPR044281 is the U3 snoRNP protein/Ribosome production factor 1 family.
    Exact name, full description, integrated signatures and quality flags were read.
    Protein membership is independently established by separate UniProt evidence.
    The family includes both Imp4 and Rpf1, so its broader label is not substituted
    for an exact Imp4 class.
  snapshot_sha256: 0ea4ca84cb716c5c638adb43977bf891899a3ec8d080a626413ba755cadd04a6
- evidence_id: micro61-PTHR11831-SF1
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR11831:SF1/
  locator: Exact retained transport receipt and empty raw payload.
  accessed_at: '2026-10-22T08:47:35.352342Z'
  support: context_only
  summary: The candidate subfamily endpoint returned HTTP204 with an empty body. It
    supplies no native class description and does not establish that an exact family
    is absent.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro61-PTHR22734-SF2
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR22734:SF2/
  locator: Exact retained transport receipt and empty raw payload.
  accessed_at: '2026-10-22T08:47:35.405704Z'
  support: context_only
  summary: The candidate subfamily endpoint returned HTTP204 with an empty body. It
    supplies no native class description and does not establish that an exact family
    is absent.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/mpp10_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T08:39:54Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/mpp10_complex.yaml'
  snapshot_sha256: d656451d8a6e8700b76271d9cde0c988c7e0d3aa2a3763ed8bcc84149088ae31
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/mpp10_complex.yaml --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mpp10_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T08:39:56Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/mpp10_complex.yaml\
    \ --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mpp10_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mpp10_complex-strict.tsv"
  snapshot_sha256: b65f24359f298c5954ee7d482e1c7d465986793631743e8573e29ba753a054af
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mpp10_complex.yaml
    --causal-graphs
  locator: Complete focused read-only native log
  accessed_at: '2026-10-22T08:48:13.004330Z'
  support: supports
  summary: "data/structures/other/mpp10_complex.yaml  (GO:0034457)\n  yeast_mpp10_90s_preribosome_assembly\t\
    mpp10_mpp10_complex_subunit\tCOVERED\t->mpp10_mpp10_complex_subunit (UniProtKB:P47083)\n\
    \  yeast_mpp10_90s_preribosome_assembly\timp3_mpp10_complex_subunit\tCOVERED\t\
    ->imp3_mpp10_complex_subunit (UniProtKB:P32899)\n  yeast_mpp10_90s_preribosome_assembly\t\
    imp4_mpp10_complex_subunit\tCOVERED\t->imp4_mpp10_complex_subunit (UniProtKB:P53941)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 47c76703ea684b552649723eaa9fffafa19cfe91cd432f5669278f1bb60acb2f
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mpp10_complex.yaml
    --verify
  locator: Complete focused read-only native log
  accessed_at: '2026-10-22T08:48:14.575023Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/mpp10_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 15 collected target identifiers returned OK. PMID:10409734: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:10409734: Imp3p and Imp4p, two specific
    components of the U3 small nucleolar ribonucleoprotein that are essential for
    pre-18S rRNA processing. (1999), DOI10.1128/mcb.19.8.5441. Identifier/bibliographic
    verification is separate from the declared body or abstract scientific-reading
    scope.; PMID:12068309: UNREACHABLE; Native Europe PMC uniquely identifies PMID:12068309:
    A large nucleolar U3 ribonucleoprotein required for 18S ribosomal RNA biogenesis.
    (2002), DOI10.1038/nature00769. Identifier/bibliographic verification is separate
    from the declared body or abstract scientific-reading scope.; PMID:17515605: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:17515605: The 90S preribosome is a
    multimodular structure that is assembled through a hierarchical mechanism. (2007),
    DOI10.1128/mcb.00380-07. Identifier/bibliographic verification is separate from
    the declared body or abstract scientific-reading scope.; PMID:9315638: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:9315638: Mpp10p, a U3 small nucleolar
    ribonucleoprotein component required for pre-18S rRNA processing in yeast. (1997),
    DOI10.1128/mcb.17.10.5803. Identifier/bibliographic verification is separate from
    the declared body or abstract scientific-reading scope. Native source checks are
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
  topic: Exact three-protein 90S module
  outcome: supported
  target_ids:
  - GO:0034457
  summary: The Mpp10 complex identity, nuclear parent and nucleolus/90S placements
    agree with native authorities. The three named budding-yeast constituent classes
    are supported by the primary source and earlier native abstracts.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-go
  - micro61-GO0034457-ancestors
  - micro61-PMC1952102-ncbi2
  - micro61-md-10409734
  - micro61-md-12068309
  - micro61-md-17515605
  - micro61-md-9315638
  - micro61-protein-P32899
  - micro61-protein-P47083
  - micro61-protein-P53941
- assessment_id: grounding
  area: grounding
  topic: Exact Mpp10 family with two unresolved narrower boundaries
  outcome: concern
  target_ids:
  - GO:0034457
  summary: IPR012173 matches Mpp10 itself, independently corroborated by its native
    accession and five reviewed members. The broader uS4 and Imp4/Rpf1 families do
    not establish exact Imp3 or Imp4 groundings; empty candidate-subfamily responses
    remain access limits.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-IPR012173
  - micro61-IPR012173-reviewed-members
  - micro61-IPR022801
  - micro61-IPR044281
  - micro61-PTHR11831-SF1
  - micro61-PTHR22734-SF2
  - micro61-protein-P32899
  - micro61-protein-P47083
  - micro61-protein-P53941
- assessment_id: graph
  area: graph
  topic: Coarse Pwp2/UTP-B branch is source supported
  outcome: supported
  target_ids:
  - GO:0034457
  summary: The five NONMECHANISTIC edges state three constituents, 90S parthood and
    support for assembly. The source supports this module/branch relationship while
    leaving sequential versus joint assembly and unmodeled factors unresolved; the
    record does not claim a strict order among the three subunits.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-go
  - micro61-GO0034457-ancestors
  - micro61-PMC1952102-ncbi2
  - micro61-md-10409734
  - micro61-md-12068309
  - micro61-md-17515605
  - micro61-md-9315638
- assessment_id: formation
  area: evidence
  topic: Unknown necessity is distinct from processing or growth
  outcome: unknown
  target_ids:
  - GO:0034457
  summary: All three component UNKNOWN labels are retained. Depletion/coprotein recovery
    and essential rRNA-processing functions are informative but do not establish a
    universal all-subunit physical-formation requirement. No corrective finding follows
    from optional missing necessity detail.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-PMC1952102-ncbi2
  - micro61-md-10409734
  - micro61-md-12068309
  - micro61-md-17515605
  - micro61-md-9315638
- assessment_id: examples
  area: grounding
  topic: Three verified reference proteins
  outcome: supported
  target_ids:
  - GO:0034457
  summary: Reviewed Mpp10/Imp3/Imp4 S288C identities, exact single-hit gene queries
    and location annotation citations agree. Dunbar and Lee complete abstracts support
    U3/processing context, while their detailed body methods are not claimed as inspected.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-protein-P32899
  - micro61-protein-P47083
  - micro61-protein-P53941
  - micro61-gene-MPP10
  - micro61-gene-IMP3
  - micro61-gene-IMP4
  - micro61-md-10409734
  - micro61-md-12068309
  - micro61-md-17515605
  - micro61-md-9315638
- assessment_id: scope
  area: scope
  topic: Model-system evidence with an uncensused majority qualifier
  outcome: supported
  target_ids:
  - GO:0034457
  summary: COMMON retains present-in-most-members and exceptional losses. The sources
    qualitatively support the budding-yeast system; S288C reference identities do
    not substitute for experimental construct details or an exhaustive strain prevalence
    survey. Analogous eukaryotic complexes are permitted by the native term without
    exporting every yeast dependency.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-tax4932
  - micro61-tax559292
  - micro61-go
  - micro61-PMC1952102-ncbi2
  - micro61-md-10409734
  - micro61-md-12068309
  - micro61-md-17515605
  - micro61-md-9315638
- assessment_id: coverage
  area: completeness
  topic: Complete target review with bounded unresolved details
  outcome: supported
  target_ids:
  - GO:0034457
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
  - micro61-GO0034457-ancestors
  - micro61-PMC1952102-ncbi2
  - micro61-IPR012173
  - micro61-IPR012173-reviewed-members
  - micro61-IPR022801
  - micro61-IPR044281
  - micro61-PTHR11831-SF1
  - micro61-PTHR22734-SF2
  - micro61-md-10409734
  - micro61-md-12068309
  - micro61-md-17515605
  - micro61-md-9315638
  - micro61-tax4932
  - micro61-tax559292
  - micro61-protein-P32899
  - micro61-protein-P47083
  - micro61-protein-P53941
  - micro61-gene-MPP10
  - micro61-gene-IMP3
  - micro61-gene-IMP4
findings:
- finding_id: F1
  issue_key: mpp10-exact-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the Mpp10 constituent to its verified family
  description: The represented Mpp10 class remains REVIEWED_LABEL_ONLY, although native
    whole-family IPR012173, independent accession cross-reference and reviewed member
    identities now provide exact grounding. The Imp3 and Imp4 candidate families remain
    broader and are not forced.
  target_ids:
  - GO:0034457
  field_paths:
  - components[0].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro61-IPR012173
  - micro61-IPR012173-reviewed-members
  - micro61-protein-P32899
  - micro61-protein-P47083
  - micro61-protein-P53941
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mpp10_complex.yaml
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
  - GO:0034457
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mpp10_complex.yaml
    role: maintained scientific record
  description: Add IPR012173 for Mpp10 and update its current grounding note/status
    and the open discussion. Retain bounded Imp3/Imp4 family uncertainty and UNKNOWN
    essentiality; do not interpret empty candidate responses as ontology absence.
  acceptance_checks:
  - The added family identifiers match the named whole-protein classes and independently
    verified member identities.
  - Current grounding status and discussion reflect the verified mappings while broader
    candidates and UNKNOWN formation labels remain qualified.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- Perez-Fernandez2007 was read only in Methods sec2–6, Results sec9/12 and Discussion
  sec15 with specified embedded captions. Other Results, separate supplements, raw
  MS data and figure pixels were not read. Earlier papers were read at complete native
  abstract tier only.
- Copurification thresholds and depletion dependencies support a module/branch but
  do not resolve every assembly order or universal formation necessity. COMMON retains
  majority semantics without a population census.
- IPR022801 and IPR044281 are broader than the exact Imp3/Imp4 classes. PANTHER candidate
  responses were HTTP204 empty; no absence inference is made. Earlier failed/challenge
  body responses remain retained separately from the genuine ncbi2 HTML.
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
