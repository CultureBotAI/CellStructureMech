# Source-backed review of plasma membrane derived chromatophore membrane

- Review: 20261022T032301Z-plasma-membrane-derived-chromatophore-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:05:41Z
- Finished UTC: 2026-10-22T03:23:01Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact membrane identity and bounded Rhodobacter photophosphorylation support are sound. One minor grounding gap affects two existing, independently verified whole complexes.

## Scope And Provenance

Exactly one full target, with three other membrane/lumen records and three energy-complex records frozen only for boundary and identifier context. Relevant native authority/protein records, actual primary sections, complete abstracts, source tiers, assembly-necessity semantics and all source placements were assessed.

Selection: Batch38 fixed strict path order, index3; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0042717 | data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml | maintained | plasma membrane-derived chromatophore membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0042717 | Focused validator passed. |
| Focused native strict | passed | True | GO:0042717 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0042717 | Native focused read-only check passed. |
| Native focused verify | passed | True | GO:0042717 | Native focused read-only check passed. |
| Claim-level scientific review | passed | True | GO:0042717 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0042717 | 18 of 20 collected target identifiers returned OK. cellstructuremech:chromatophore_cytochrome_bc1_complex: SKIPPED; Exact local whole-complex identity occurs once in an ignored-inclusive top-level identifier search and is a frozen maintained input. The generic resolver has no external adapter for this locally minted identifier.; cellstructuremech:rc_lh1_pufx_core_complex: SKIPPED; Exact local whole-complex identity occurs once in an ignored-inclusive top-level identifier search and is a frozen maintained input. The generic resolver has no external adapter for this locally minted identifier. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0042717 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0042717 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0042717 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0042717 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0042717 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact identity, hierarchy and boundaries

identity: supported. Targets: GO:0042717.

GO0042717/SL0042 exactly identify the plasma-derived bacterial chromatophore membrane; GO0070112 separately identifies the organellar chromatophore membrane. The generic photosynthetic-membrane parent and related rather than exact broad chromatophore synonym preserve that boundary.

### Material and complex constituent scope

grounding: supported. Targets: GO:0042717.

The lipid row denotes the collective lipid matrix without misusing a whole-membrane GO term as chemical identity. Exact complexes or deliberately broad cohorts are evaluated at their declared level; existing protein examples are identities, not exhaustive stoichiometry or proof of incorporation. Photosynthetic function and membrane residence are supported at the stated cyanobacterial or Rhodobacter source scope.

### Individual assembly requirements remain unknown

grounding: unknown. Targets: GO:0042717.

The collective bilayer is constitutional to a membrane, and broad reaction-center/pigment/carrier classes define the photosynthetic class. Those definitions do not establish depletion requirements for each named complex, protein, pigment or lipid species. UNKNOWN labels on the specific chromatophore/thylakoid complexes are preserved. No individual assembly-necessity experiment is inferred from mature localization, native structure, photosynthetic activity or inferred UniProt function.

### Reviewed gene/taxon examples and annotation evidence

grounding: supported. Targets: GO:0042717.

All stated accessions, primary gene names or explicit aliases, organism nodes and reviewed status agree with the native records. Exact species and substrain nodes are retained. The current single-entry query agrees after exact-organism filtering. A curated localization annotation plus matching paper abstract is not presented as our own full-paper experiment audit.

### Purple-bacterial examples and bounded source strains

scope: supported. Targets: GO:0042717.

ENA confirms Cereibacter/Rhodobacter sphaeroides identity and exact protein substrains. Bahatyrova NCIB8253 architecture, Comayras Ga quinone/excitation work and Feniouk R.capsulatus vesicle physiology are distinct experimental contexts. The NONMECHANISTIC graph is a Rhodobacter-supported illustrative route; it does not establish invariant dimer architecture, universal c2 usage, stoichiometry or a prevalence census for every purple bacterium.

### Target-specific graph and functional scope

graph: supported. Targets: GO:0042717.

Six NONMECHANISTIC edges summarize LH2-to-core excitation, quinone reduction/reoxidation and sealed-vesicle proton motive force use. Comayras primary assay inhibition is retained as a source limit: the normal bc1 cycle is contextual synthesis, not an unperturbed cyclic-flux result from that experiment. Feniouk complete abstract supports PMF-coupled ATP-synthase charge transport; no detailed full-body ATP-product assay is certified.

### Complete record coverage without forced optional enrichment

completeness: supported. Targets: GO:0042717.

Every target claim, evidence placement, graph node/edge and discussion was reviewed. Existing local complexes were resolved through frozen inputs. Optional new protein examples, absent chemical species/ratios, unasserted quantitative dimensions and complete comparative inventories are not made mandatory. No maintained image or direct quotation is present to audit. The precise findings do not alter valid generic identity or historical curation statements.

## Findings

### F1: Ground the two existing complexes with verified whole-complex identifiers

minor / open / confirmed; issue key: plasma-membrane-derived-chromatophore-membrane-1.

The existing LH2 constituent remains REVIEWED_LABEL_ONLY while the frozen maintained record cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex supplies the exact whole-complex identity in the same chromatophore context. The existing F0F1 constituent also remains label-only solely pending a chromatophore-localized accession, although active GO0045259 exactly names the F1-F0 ATP synthase complex; location belongs in its role/context. This is a bounded gap in two already asserted constituents, not a demand for an optional new inventory or a claim that the historical pass had access to future records.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, ground LH2 to the exact maintained local complex and F0F1 to GO0045259, retain source-specific localization and UNKNOWN formation necessity, and resolve the current grounding task without rewriting historical events.

- Each changed field matches the exact source organism, process or whole-complex identity.
- Correct structure boundaries, protein identities and original history remain intact.
- Native schema, strict, CURIE, graph and history gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml; Entire maintained YAML: every field, source note, component/example, graph edge, history and discussion | context_only | The complete target was read. Historical notes retain their original temporal scope; scientific content remains unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, graph scope and constituent/actor semantics | context_only | Constitutional collective material is distinguished from individual molecular formation necessity. Location GO classes are not chemical identities; protein examples establish identity separately from membership. |
| local-chromatophore_cytochrome_bc1_complex | data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml; Complete frozen local record; identity, composition and graph/boundary context | context_only | The exact local identifier and whole-complex or membrane/lumen boundary were checked. Neighbor source interpretations are not adopted as independent experimental evidence. |
| local-lh2_peripheral_light_harvesting_antenna_complex | data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml; Complete frozen local record; identity, composition and graph/boundary context | context_only | The exact local identifier and whole-complex or membrane/lumen boundary were checked. Neighbor source interpretations are not adopted as independent experimental evidence. |
| local-rc_lh1_pufx_core_complex | data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml; Complete frozen local record; identity, composition and graph/boundary context | context_only | The exact local identifier and whole-complex or membrane/lumen boundary were checked. Neighbor source interpretations are not adopted as independent experimental evidence. |
| local-photosynthetic_membrane | data/structures/membrane_organelle/photosynthetic_membrane.yaml; Complete frozen local record; identity, composition and graph/boundary context | context_only | The exact local identifier and whole-complex or membrane/lumen boundary were checked. Neighbor source interpretations are not adopted as independent experimental evidence. |
| local-plasma_membrane_derived_thylakoid_lumen | data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml; Complete frozen local record; identity, composition and graph/boundary context | context_only | The exact local identifier and whole-complex or membrane/lumen boundary were checked. Neighbor source interpretations are not adopted as independent experimental evidence. |
| local-plasma_membrane_derived_thylakoid_membrane | data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml; Complete frozen local record; identity, composition and graph/boundary context | context_only | The exact local identifier and whole-complex or membrane/lumen boundary were checked. Neighbor source interpretations are not adopted as independent experimental evidence. |
| photo-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009512,GO:0009579,GO:0009767,GO:0016020,GO:0019684,GO:0030075,GO:0030076,GO:0030094,GO:0030096,GO:0031676,GO:0031979,GO:0034357,GO:0042651,GO:0042717,GO:0043233,GO:0045259,GO:0070112; All17 complete entries: id/name/definition/isObsolete/synonyms/comments/typed children. Exact IDs listed in retained response; relation direction retained. | supports | The17 active entries distinguish generic photosynthetic membrane, bacterial and organellar chromatophore membranes, bacterial thylakoid membrane/lumen, PSI/PSII and other complexes. Typed child edges support the stated membrane subclasses and bacterial-thylakoid parts. GO0045259 explicitly includes the F1-F0 ATP synthase synonym and sectors. GO0019684 is specifically an oxygenic PSI/PSII, water-to-NADPH process, while GO0009767 is broader. A returned whole-thylakoid part_of edge is not silently rewritten as a direct membrane has_part edge. |
| photo-agent-SL-0042 | https://rest.uniprot.org/locations/SL-0042.json; Complete top-level identity/definition/synonyms/GO mapping and immediate isA/partOf with nested parent cross-references. | supports | SL0042 maps directly to GO0042717 and defines purple-bacterial plasma-derived internal photosynthetic membranes with reaction centers, antennae, bc1 and F0F1. Its broad chromatophore-membrane synonym does not erase the organellar distinction. |
| photo-agent-SL-0044 | https://rest.uniprot.org/locations/SL-0044.json; Complete top-level identity/definition/synonyms/GO mapping and immediate isA/partOf with nested parent cross-references. | supports | SL0044 directly maps cellular thylakoid lumen to GO0031979 and places it within cellular thylakoid. Its nested terminology calls thylakoid an organelle, whereas the native GO0009579 comment says it is not considered one; this vocabulary difference is retained rather than silently reconciled. |
| photo-agent-SL-0045 | https://rest.uniprot.org/locations/SL-0045.json; Complete top-level identity/definition/synonyms/GO mapping and immediate isA/partOf with nested parent cross-references. | supports | SL0045 directly maps cellular thylakoid membrane to GO0031676 and places it within cellular thylakoid, with the generic membrane broader class. The top-level identity is distinct from nested parent definitions. |
| photo-agent-tax-1063 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1063; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA identifies taxId1063 as Cereibacter sphaeroides at rank species. The native lineage and otherNames were checked; this response supplies identity, not experimental prevalence or a strain's assay result. |
| photo-agent-tax-272943 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/272943; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA identifies taxId272943 as Cereibacter sphaeroides 2.4.1 at rank strain. The native lineage and otherNames were checked; this response supplies identity, not experimental prevalence or a strain's assay result. |
| photo-agent-tax-349102 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/349102; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA identifies taxId349102 as Cereibacter sphaeroides ATCC 17025 at rank strain. The native lineage and otherNames were checked; this response supplies identity, not experimental prevalence or a strain's assay result. |
| photo-agent-bahatyrova2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nature02823; Unique MED identity/title/authors/year/DOI and complete abstract. | supports | The exact MED15329728 record matches DOI10.1038/nature02823 and The native architecture of a photosynthetic membrane.. Complete abstract, author/year identity and publication type were read. This row does not imply access to a full body. |
| photo-agent-comayras2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1074/jbc.M412088200; Unique MED identity/title/authors/year/DOI and complete abstract. | supports | The exact MED15632164 record matches DOI10.1074/jbc.m412088200 and Functional consequences of the organization of the photosynthetic apparatus in Rhodobacter sphaeroides. I. Quinone domains and excitation transfer in chromatophores and reaction center.antenna complexes.. Complete abstract, author/year identity and publication type were read. This row does not imply access to a full body. |
| photo-agent-feniouk2002-pmid | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11867431%20AND%20SRC%3AMED; Unique MED identity/title/authors/year/DOI and complete abstract. | supports | The exact MED11867431 record matches DOI10.1016/s0006-3495(02)75470-2 and Chromatophore vesicles of Rhodobacter capsulatus contain on average one F(O)F(1)-ATP synthase each.. Complete abstract, author/year identity and publication type were read. This row does not imply access to a full body. |
| photo-agent-bahatyrova2004-whiterose-pdf | https://eprints.whiterose.ac.uk/id/eprint/102/1/huntercn1.pdf; Genuine university-hosted published PDF, main article pp1058–1061 and Methods, Fig1–3 captions. Adjacent unrelated paper/reference matter excluded; no figure pixels/supplements analyzed. | supports | Bahatyrova2004 directly images native R.sphaeroides NCIB8253 membrane patches by AFM and resolves RC-LH1-PufX dimers/arrays and LH2-rich domains. Main-text energy-transfer routes combine architecture with cited earlier kinetic studies; AFM is not itself a new energy-transfer timing assay. Methods use defined light growth, isolated vesicles, dilute detergent for patches and mica adsorption. The paper explicitly leaves bc1/ATP-synthase location questions unresolved, so its AFM result is not evidence for localizing those proteins. |
| photo-agent-comayras2005-browser-body1 | https://www.researchgate.net/publication/8099149_Functional_consequences_of_the_organization_of_the_photosynthetic_apparatus_in_Rhodobacter_sphaeroides_I_Quinone_domains_and_excitation_transfer_in_chromatophores_and_reaction_centerantenna_complexes; Browser-captured primary excerpt, status:null: native excerpt lines410–634 Intro/Experimental,606–885 acceptor-pool photoreduction/redox/model and initial Results,1004–1283 Fig1/excitation/quinone Results. Exact overlapping capture ranges inspected; not the complete paper. | supports | Comayras2005 partI studies R.sphaeroides Ga chromatophores and isolated RC-LH1 complexes. Flash/redox and excitation experiments support quinone domains and connectivity. The acceptor-pool assay inhibits bc1 with myxothiazol/antimycin and uses other blockers/uncouplers; normal bc1 cyclic traffic appears in contextual pathway reasoning, not as an unperturbed directly measured cycle in that assay. The record’s broad pathway can be supported while respecting this distinction. |
| photo-agent-feniouk2002-numeric | https://pmc.ncbi.nlm.nih.gov/articles/1301917/; HTML title/content and response metadata; body unreadable. | context_only | This HTTP200 PMC response is a reCAPTCHA/challenge page, not the Feniouk body. The complete native MED abstract is the inspected scientific source; it describes flash-generated proton motive force and ATP-synthase-coupled charge transport detected by electrochromic carotenoid transients with inhibitors, in R.capsulatus. No full Methods or direct ATP-product assay is certified. |
| photo-agent-feniouk2002-author | https://www.home.uni-osnabrueck.de/wjunge/public/230.pdf; Native request exception and exact retained transport error. | context_only | The university PDF request timed out (status0); the retained error bytes do not contain a paper. |
| photo-agent-protein-P0C0Y0 | https://rest.uniprot.org/uniprotkb/P0C0Y0.json; Exact accession/entryType/proteinDescription/genes/organism; complete relevant comments and cited-reference records. | supports | Native P0C0Y0 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter sphaeroides (1063), primary gene names pucA. Synonyms, protein name, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence citations were read. These identify the stated example; automated or homology annotations are not promoted to direct formation or localization experiments. |
| photo-agent-protein-P0C0Y2 | https://rest.uniprot.org/uniprotkb/P0C0Y2.json; Exact accession/entryType/proteinDescription/genes/organism; complete relevant comments and cited-reference records. | supports | Native P0C0Y2 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter sphaeroides (1063), primary gene names pucB. Synonyms, protein name, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence citations were read. These identify the stated example; automated or homology annotations are not promoted to direct formation or localization experiments. |
| photo-agent-protein-A4WUM7 | https://rest.uniprot.org/uniprotkb/A4WUM7.json; Exact accession/entryType/proteinDescription/genes/organism; complete relevant comments and cited-reference records. | supports | Native A4WUM7 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter sphaeroides (strain ATCC 17025 / ATH 2.4.3) (349102), primary gene names atpD. Synonyms, protein name, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence citations were read. These identify the stated example; automated or homology annotations are not promoted to direct formation or localization experiments. |
| photo-agent-protein-Q3J433 | https://rest.uniprot.org/uniprotkb/Q3J433.json; Exact accession/entryType/proteinDescription/genes/organism; complete relevant comments and cited-reference records. | supports | Native Q3J433 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 / NBRC 12203 / NCIMB 8253 / ATH 2.4.1.) (272943), primary gene names atpA. Synonyms, protein name, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence citations were read. These identify the stated example; automated or homology annotations are not promoted to direct formation or localization experiments. |
| photo-agent-protein-Q3IZ12 | https://rest.uniprot.org/uniprotkb/Q3IZ12.json; Exact accession/entryType/proteinDescription/genes/organism; complete relevant comments and cited-reference records. | supports | Native Q3IZ12 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 / NBRC 12203 / NCIMB 8253 / ATH 2.4.1.) (272943), primary gene names atpB. Synonyms, protein name, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence citations were read. These identify the stated example; automated or homology annotations are not promoted to direct formation or localization experiments. |
| photo-agent-protein-Q3IZ13 | https://rest.uniprot.org/uniprotkb/Q3IZ13.json; Exact accession/entryType/proteinDescription/genes/organism; complete relevant comments and cited-reference records. | supports | Native Q3IZ13 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 / NBRC 12203 / NCIMB 8253 / ATH 2.4.1.) (272943), primary gene names atpE. Synonyms, protein name, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence citations were read. These identify the stated example; automated or homology annotations are not promoted to direct formation or localization experiments. |
| photo-agent-reviewed-uniqueness | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+%28%28taxonomy_id%3A1111708+AND+%28gene_exact%3ApsaA+OR+gene_exact%3ApsbA2+OR+gene_exact%3ApsbA3+OR+gene_exact%3ApetA+OR+gene_exact%3ApetB%29%29+OR+%28taxonomy_id%3A1063+AND+%28gene_exact%3ApufL+OR+gene_exact%3ApufM+OR+gene_exact%3ApetB+OR+gene_exact%3ApetC+OR+gene_exact%3ApucA+OR+gene_exact%3ApucB%29%29%29&amp;format=json&amp;fields=accession%2Cid%2Creviewed%2Cgene_names%2Corganism_id%2Corganism_name&amp;size=500; Exact query URL; all14 returned rows and organism IDs; no additional page indicated. | supports | The bounded reviewed exact-gene query returned14 rows including descendant-strain entries. Filtering by exact returned organism IDs confirms single relevant entries at tax1111708 and1063 for the stated primary symbols; descendant272943 rows are not counted as exact-species duplicates. P16033 contains both psbA2 and psbA3; fbcB/fbcC remain native synonyms for petB/petC. This is identity checking, not complex membership proof. |
| schema-result | just validate data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml --out /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plasma_membrane_derived_chromatophore_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml --out /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plasma_membrane_derived_chromatophore_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plasma_membrane_derived_chromatophore_membrane-strict.tsv |
| focused-causal-graphs | /private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml; Complete read-only native focused log | supports | data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml  (GO:0042717)<br>  chromatophore_photophosphorylation	lh2	COVERED	-&gt;lh2_antenna_complexes (UniProtKB:P0C0Y0, UniProtKB:P0C0Y2)<br>  chromatophore_photophosphorylation	f0f1_atp_synthase	COVERED	-&gt;f0f1_atp_synthase (UniProtKB:A4WUM7, UniProtKB:Q3J433, UniProtKB:Q3IZ12, UniProtKB:Q3IZ13)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| focused-verify | /private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml; Complete read-only native focused log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 18 of 20 collected target identifiers returned OK. cellstructuremech:chromatophore_cytochrome_bc1_complex: SKIPPED; Exact local whole-complex identity occurs once in an ignored-inclusive top-level identifier search and is a frozen maintained input. The generic resolver has no external adapter for this locally minted identifier.; cellstructuremech:rc_lh1_pufx_core_complex: SKIPPED; Exact local whole-complex identity occurs once in an ignored-inclusive top-level identifier search and is a frozen maintained input. The generic resolver has no external adapter for this locally minted identifier. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Original source URL, UTC time and raw hash are preserved on unchanged imports. Browser-extracted representations have status:null and are not native HTTP200 bodies. Only the named paper sections or complete abstracts were actually read; no raw-data, figure-pixel or supplemental reanalysis was performed.
- Perez2024 is secondary synthesis available in bounded Introduction and electron-transport excerpts; native full-body routes returned403. Sui2021 and Feniouk2002 were assessed at complete native abstract scope; Feniouk numericPMC returned a challenge and university download timed out. No complete Methods or ATP-product measurement is inferred.
- Casella native/tagged-cell observations and Huokko light-shift biogenesis belong to Syn7942. Bahatyrova NCIB8253, Comayras Ga and Feniouk R.capsulatus are separate contexts; no universal strain-specific architecture, quantitative prevalence or exact stoichiometry is inferred.
- Individual formation necessity, exact lipid composition and exhaustive taxon-neutral protein inventories remain unknown beyond the declared collective class. Correct native protein identities and database experimental citation links are not a substitute for independently read full experiment bodies.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User explicitly requests one review for every unreviewed record; no scientific or history edits are made.
- iModulonDB is not applicable: these records assert physical complex identities and photochemistry, not expression-module membership or regulator-response claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T032301Z-plasma-membrane-derived-chromatophore-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of plasma membrane derived chromatophore membrane
started_at: '2026-10-22T03:05:41Z'
finished_at: '2026-10-22T03:23:01Z'
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
summary: Exact membrane identity and bounded Rhodobacter photophosphorylation support
  are sound. One minor grounding gap affects two existing, independently verified
  whole complexes.
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
  - path: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
    sha256: 7f6582722d2f5376262287856929ec073f8550493eee88c6cb92dfc7624ec7ed
    role: context
  - path: data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml
    sha256: 4bb84c48c2bb27f1a8dded06f479771b494070977ef26e0b14f0708bc446a7ce
    role: context
  - path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
    sha256: 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824
    role: context
  - path: data/structures/membrane_organelle/photosynthetic_membrane.yaml
    sha256: 5fe446aae99635ba843cf22d1144ab1312a2c30224367c49efd0bedcbd06db97
    role: context
  - path: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    sha256: f3130fc795ff500febb7d273c6a7b281ec7d2cc230d6e44fb5363c6c9256b064
    role: target
  - path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
    sha256: 4b4fbe694529235b322625d85f5c210eddea0cc03e5e1a684d5bff2d698bca82
    role: context
  - path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
    sha256: 66205b2d304df6e2b425730f885ccf46de08dc94c99c60636eab667d3bf68410
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
- target_id: GO:0042717
  path: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  label: plasma membrane-derived chromatophore membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    role: maintained scientific record
scope:
  description: Exactly one full target, with three other membrane/lumen records and
    three energy-complex records frozen only for boundary and identifier context.
    Relevant native authority/protein records, actual primary sections, complete abstracts,
    source tiers, assembly-necessity semantics and all source placements were assessed.
  selection: Batch38 fixed strict path order, index3; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0042717
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: just validate data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: just validate-strict data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    --out /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plasma_membrane_derived_chromatophore_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: focused-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: /private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  exit_code: 0
  summary: Native focused read-only check passed.
  evidence_ids:
  - focused-causal-graphs
- check_id: focused-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: /private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  exit_code: 0
  summary: Native focused read-only check passed.
  evidence_ids:
  - focused-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0042717
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - local-chromatophore_cytochrome_bc1_complex
  - local-lh2_peripheral_light_harvesting_antenna_complex
  - local-rc_lh1_pufx_core_complex
  - local-photosynthetic_membrane
  - local-plasma_membrane_derived_thylakoid_lumen
  - local-plasma_membrane_derived_thylakoid_membrane
  - photo-agent-go
  - photo-agent-SL-0042
  - photo-agent-SL-0044
  - photo-agent-SL-0045
  - photo-agent-tax-1063
  - photo-agent-tax-272943
  - photo-agent-tax-349102
  - photo-agent-bahatyrova2004-meta
  - photo-agent-comayras2005-meta
  - photo-agent-feniouk2002-pmid
  - photo-agent-bahatyrova2004-whiterose-pdf
  - photo-agent-comayras2005-browser-body1
  - photo-agent-feniouk2002-numeric
  - photo-agent-feniouk2002-author
  - photo-agent-protein-P0C0Y0
  - photo-agent-protein-P0C0Y2
  - photo-agent-protein-A4WUM7
  - photo-agent-protein-Q3J433
  - photo-agent-protein-Q3IZ12
  - photo-agent-protein-Q3IZ13
  - photo-agent-reviewed-uniqueness
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0042717
  summary: '18 of 20 collected target identifiers returned OK. cellstructuremech:chromatophore_cytochrome_bc1_complex:
    SKIPPED; Exact local whole-complex identity occurs once in an ignored-inclusive
    top-level identifier search and is a frozen maintained input. The generic resolver
    has no external adapter for this locally minted identifier.; cellstructuremech:rc_lh1_pufx_core_complex:
    SKIPPED; Exact local whole-complex identity occurs once in an ignored-inclusive
    top-level identifier search and is a frozen maintained input. The generic resolver
    has no external adapter for this locally minted identifier. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - local-chromatophore_cytochrome_bc1_complex
  - local-rc_lh1_pufx_core_complex
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch38 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch38 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch38 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch38 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0042717
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
    and current batch38 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  locator: 'Entire maintained YAML: every field, source note, component/example, graph
    edge, history and discussion'
  accessed_at: '2026-10-22T03:19:46Z'
  support: context_only
  summary: The complete target was read. Historical notes retain their original temporal
    scope; scientific content remains unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, graph scope and constituent/actor
    semantics
  accessed_at: '2026-10-22T03:19:46Z'
  support: context_only
  summary: Constitutional collective material is distinguished from individual molecular
    formation necessity. Location GO classes are not chemical identities; protein
    examples establish identity separately from membership.
- evidence_id: local-chromatophore_cytochrome_bc1_complex
  kind: record_content
  reference: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
  locator: Complete frozen local record; identity, composition and graph/boundary
    context
  accessed_at: '2026-10-22T03:19:46Z'
  support: context_only
  summary: The exact local identifier and whole-complex or membrane/lumen boundary
    were checked. Neighbor source interpretations are not adopted as independent experimental
    evidence.
- evidence_id: local-lh2_peripheral_light_harvesting_antenna_complex
  kind: record_content
  reference: data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml
  locator: Complete frozen local record; identity, composition and graph/boundary
    context
  accessed_at: '2026-10-22T03:19:46Z'
  support: context_only
  summary: The exact local identifier and whole-complex or membrane/lumen boundary
    were checked. Neighbor source interpretations are not adopted as independent experimental
    evidence.
- evidence_id: local-rc_lh1_pufx_core_complex
  kind: record_content
  reference: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
  locator: Complete frozen local record; identity, composition and graph/boundary
    context
  accessed_at: '2026-10-22T03:19:46Z'
  support: context_only
  summary: The exact local identifier and whole-complex or membrane/lumen boundary
    were checked. Neighbor source interpretations are not adopted as independent experimental
    evidence.
- evidence_id: local-photosynthetic_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/photosynthetic_membrane.yaml
  locator: Complete frozen local record; identity, composition and graph/boundary
    context
  accessed_at: '2026-10-22T03:19:46Z'
  support: context_only
  summary: The exact local identifier and whole-complex or membrane/lumen boundary
    were checked. Neighbor source interpretations are not adopted as independent experimental
    evidence.
- evidence_id: local-plasma_membrane_derived_thylakoid_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
  locator: Complete frozen local record; identity, composition and graph/boundary
    context
  accessed_at: '2026-10-22T03:19:46Z'
  support: context_only
  summary: The exact local identifier and whole-complex or membrane/lumen boundary
    were checked. Neighbor source interpretations are not adopted as independent experimental
    evidence.
- evidence_id: local-plasma_membrane_derived_thylakoid_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
  locator: Complete frozen local record; identity, composition and graph/boundary
    context
  accessed_at: '2026-10-22T03:19:46Z'
  support: context_only
  summary: The exact local identifier and whole-complex or membrane/lumen boundary
    were checked. Neighbor source interpretations are not adopted as independent experimental
    evidence.
- evidence_id: photo-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009512,GO:0009579,GO:0009767,GO:0016020,GO:0019684,GO:0030075,GO:0030076,GO:0030094,GO:0030096,GO:0031676,GO:0031979,GO:0034357,GO:0042651,GO:0042717,GO:0043233,GO:0045259,GO:0070112
  locator: 'All17 complete entries: id/name/definition/isObsolete/synonyms/comments/typed
    children. Exact IDs listed in retained response; relation direction retained.'
  accessed_at: '2026-10-22T03:11:17.482907Z'
  support: supports
  summary: The17 active entries distinguish generic photosynthetic membrane, bacterial
    and organellar chromatophore membranes, bacterial thylakoid membrane/lumen, PSI/PSII
    and other complexes. Typed child edges support the stated membrane subclasses
    and bacterial-thylakoid parts. GO0045259 explicitly includes the F1-F0 ATP synthase
    synonym and sectors. GO0019684 is specifically an oxygenic PSI/PSII, water-to-NADPH
    process, while GO0009767 is broader. A returned whole-thylakoid part_of edge is
    not silently rewritten as a direct membrane has_part edge.
  snapshot_sha256: 2670c336056b66e0fc70989170ece908a50d83712fffcc5c39dc917e6b9250ab
- evidence_id: photo-agent-SL-0042
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0042.json
  locator: Complete top-level identity/definition/synonyms/GO mapping and immediate
    isA/partOf with nested parent cross-references.
  accessed_at: '2026-10-22T03:11:20.769095Z'
  support: supports
  summary: SL0042 maps directly to GO0042717 and defines purple-bacterial plasma-derived
    internal photosynthetic membranes with reaction centers, antennae, bc1 and F0F1.
    Its broad chromatophore-membrane synonym does not erase the organellar distinction.
  snapshot_sha256: f16f40b6a8cfdb7911506598df2106649cf2e49643691a2077726a4384262ead
- evidence_id: photo-agent-SL-0044
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0044.json
  locator: Complete top-level identity/definition/synonyms/GO mapping and immediate
    isA/partOf with nested parent cross-references.
  accessed_at: '2026-10-22T03:11:20.801784Z'
  support: supports
  summary: SL0044 directly maps cellular thylakoid lumen to GO0031979 and places it
    within cellular thylakoid. Its nested terminology calls thylakoid an organelle,
    whereas the native GO0009579 comment says it is not considered one; this vocabulary
    difference is retained rather than silently reconciled.
  snapshot_sha256: ac9afb75436945fe5aa2b05c693b8eb87cb6511b9907d3bc922b43d81ad136a8
- evidence_id: photo-agent-SL-0045
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0045.json
  locator: Complete top-level identity/definition/synonyms/GO mapping and immediate
    isA/partOf with nested parent cross-references.
  accessed_at: '2026-10-22T03:11:20.863830Z'
  support: supports
  summary: SL0045 directly maps cellular thylakoid membrane to GO0031676 and places
    it within cellular thylakoid, with the generic membrane broader class. The top-level
    identity is distinct from nested parent definitions.
  snapshot_sha256: ef7ca37f3d79b995c2c2f4d5f47200aa88b6166b17c66bf4792a5dfc1cf77af6
- evidence_id: photo-agent-tax-1063
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1063
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:11:17.484582Z'
  support: supports
  summary: ENA identifies taxId1063 as Cereibacter sphaeroides at rank species. The
    native lineage and otherNames were checked; this response supplies identity, not
    experimental prevalence or a strain's assay result.
  snapshot_sha256: 8285496c8734b387fd123717f2706cee39315debabb01990f225569e47e4420d
- evidence_id: photo-agent-tax-272943
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/272943
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:11:18.296878Z'
  support: supports
  summary: ENA identifies taxId272943 as Cereibacter sphaeroides 2.4.1 at rank strain.
    The native lineage and otherNames were checked; this response supplies identity,
    not experimental prevalence or a strain's assay result.
  snapshot_sha256: d049cb77bc4090d3737dda669b8a5b0e418737c098f7bb33bb059334c96bb3b0
- evidence_id: photo-agent-tax-349102
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/349102
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:11:18.306185Z'
  support: supports
  summary: ENA identifies taxId349102 as Cereibacter sphaeroides ATCC 17025 at rank
    strain. The native lineage and otherNames were checked; this response supplies
    identity, not experimental prevalence or a strain's assay result.
  snapshot_sha256: a26d7173bff82f58ff2b753ce2dbd6d60e57dce60b78cb43eefdb10b10f35394
- evidence_id: photo-agent-bahatyrova2004-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nature02823
  locator: Unique MED identity/title/authors/year/DOI and complete abstract.
  accessed_at: '2026-10-21T08:52:54.960760Z'
  support: supports
  summary: The exact MED15329728 record matches DOI10.1038/nature02823 and The native
    architecture of a photosynthetic membrane.. Complete abstract, author/year identity
    and publication type were read. This row does not imply access to a full body.
  snapshot_sha256: cdd0a3a0fab5cf8136a8c5e9e2246441b2cbf420c78c71eaf28cf9620293f722
- evidence_id: photo-agent-comayras2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1074/jbc.M412088200
  locator: Unique MED identity/title/authors/year/DOI and complete abstract.
  accessed_at: '2026-10-21T08:52:54.958102Z'
  support: supports
  summary: The exact MED15632164 record matches DOI10.1074/jbc.m412088200 and Functional
    consequences of the organization of the photosynthetic apparatus in Rhodobacter
    sphaeroides. I. Quinone domains and excitation transfer in chromatophores and
    reaction center.antenna complexes.. Complete abstract, author/year identity and
    publication type were read. This row does not imply access to a full body.
  snapshot_sha256: f0a2f6d4c18cf31ffaaddcebf08e2e79dffad94e116ffecf30b579b254acd745
- evidence_id: photo-agent-feniouk2002-pmid
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11867431%20AND%20SRC%3AMED
  locator: Unique MED identity/title/authors/year/DOI and complete abstract.
  accessed_at: '2026-10-22T03:12:15.108617Z'
  support: supports
  summary: The exact MED11867431 record matches DOI10.1016/s0006-3495(02)75470-2 and
    Chromatophore vesicles of Rhodobacter capsulatus contain on average one F(O)F(1)-ATP
    synthase each.. Complete abstract, author/year identity and publication type were
    read. This row does not imply access to a full body.
  snapshot_sha256: da8fdb8afe6b2200561ca5fc42c6506b86ad032be65a87bbb5a538bc65bfb770
- evidence_id: photo-agent-bahatyrova2004-whiterose-pdf
  kind: primary_source
  reference: https://eprints.whiterose.ac.uk/id/eprint/102/1/huntercn1.pdf
  locator: Genuine university-hosted published PDF, main article pp1058–1061 and Methods,
    Fig1–3 captions. Adjacent unrelated paper/reference matter excluded; no figure
    pixels/supplements analyzed.
  accessed_at: '2026-10-21T08:53:33.388205Z'
  support: supports
  summary: Bahatyrova2004 directly images native R.sphaeroides NCIB8253 membrane patches
    by AFM and resolves RC-LH1-PufX dimers/arrays and LH2-rich domains. Main-text
    energy-transfer routes combine architecture with cited earlier kinetic studies;
    AFM is not itself a new energy-transfer timing assay. Methods use defined light
    growth, isolated vesicles, dilute detergent for patches and mica adsorption. The
    paper explicitly leaves bc1/ATP-synthase location questions unresolved, so its
    AFM result is not evidence for localizing those proteins.
  snapshot_sha256: 18b555872af69d3ebed8f51dcfab485e048eaa892d83e9ac71cb998564f3bd25
- evidence_id: photo-agent-comayras2005-browser-body1
  kind: primary_source
  reference: https://www.researchgate.net/publication/8099149_Functional_consequences_of_the_organization_of_the_photosynthetic_apparatus_in_Rhodobacter_sphaeroides_I_Quinone_domains_and_excitation_transfer_in_chromatophores_and_reaction_centerantenna_complexes
  locator: 'Browser-captured primary excerpt, status:null: native excerpt lines410–634
    Intro/Experimental,606–885 acceptor-pool photoreduction/redox/model and initial
    Results,1004–1283 Fig1/excitation/quinone Results. Exact overlapping capture ranges
    inspected; not the complete paper.'
  accessed_at: '2026-10-21T08:55:40.204360Z'
  support: supports
  summary: Comayras2005 partI studies R.sphaeroides Ga chromatophores and isolated
    RC-LH1 complexes. Flash/redox and excitation experiments support quinone domains
    and connectivity. The acceptor-pool assay inhibits bc1 with myxothiazol/antimycin
    and uses other blockers/uncouplers; normal bc1 cyclic traffic appears in contextual
    pathway reasoning, not as an unperturbed directly measured cycle in that assay.
    The record’s broad pathway can be supported while respecting this distinction.
  snapshot_sha256: 41d62a5b4399ea3b11d95703cb686d447ba32e5854f314f3a2a54fc6790b4b2a
- evidence_id: photo-agent-feniouk2002-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/1301917/
  locator: HTML title/content and response metadata; body unreadable.
  accessed_at: '2026-10-22T03:12:15.108998Z'
  support: context_only
  summary: This HTTP200 PMC response is a reCAPTCHA/challenge page, not the Feniouk
    body. The complete native MED abstract is the inspected scientific source; it
    describes flash-generated proton motive force and ATP-synthase-coupled charge
    transport detected by electrochromic carotenoid transients with inhibitors, in
    R.capsulatus. No full Methods or direct ATP-product assay is certified.
  snapshot_sha256: 941d3605b9a02678007677fd4f970960180bb61a11efd9f60b24dc36ecebb343
- evidence_id: photo-agent-feniouk2002-author
  kind: primary_source
  reference: https://www.home.uni-osnabrueck.de/wjunge/public/230.pdf
  locator: Native request exception and exact retained transport error.
  accessed_at: '2026-10-22T03:12:15.109279Z'
  support: context_only
  summary: The university PDF request timed out (status0); the retained error bytes
    do not contain a paper.
  snapshot_sha256: cc35a273124032df31efa83073c3af3ae07ae99d235717de0eaf27d9f5427af8
- evidence_id: photo-agent-protein-P0C0Y0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0C0Y0.json
  locator: Exact accession/entryType/proteinDescription/genes/organism; complete relevant
    comments and cited-reference records.
  accessed_at: '2026-10-22T03:11:18.869306Z'
  support: supports
  summary: Native P0C0Y0 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter
    sphaeroides (1063), primary gene names pucA. Synonyms, protein name, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence citations were read. These identify the stated
    example; automated or homology annotations are not promoted to direct formation
    or localization experiments.
  snapshot_sha256: 400956bf4478dd3351939ef06edeea0b6b5076faf74ac7d306bbe8a485d365d8
- evidence_id: photo-agent-protein-P0C0Y2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0C0Y2.json
  locator: Exact accession/entryType/proteinDescription/genes/organism; complete relevant
    comments and cited-reference records.
  accessed_at: '2026-10-22T03:11:18.933810Z'
  support: supports
  summary: Native P0C0Y2 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter
    sphaeroides (1063), primary gene names pucB. Synonyms, protein name, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence citations were read. These identify the stated
    example; automated or homology annotations are not promoted to direct formation
    or localization experiments.
  snapshot_sha256: 87f9dfdbccde25c9a9258efeaba7ce4d1a173827f52e0902b7f4efabac1d354b
- evidence_id: photo-agent-protein-A4WUM7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A4WUM7.json
  locator: Exact accession/entryType/proteinDescription/genes/organism; complete relevant
    comments and cited-reference records.
  accessed_at: '2026-10-22T03:11:18.864615Z'
  support: supports
  summary: Native A4WUM7 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter
    sphaeroides (strain ATCC 17025 / ATH 2.4.3) (349102), primary gene names atpD.
    Synonyms, protein name, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their
    evidence citations were read. These identify the stated example; automated or
    homology annotations are not promoted to direct formation or localization experiments.
  snapshot_sha256: 5c3aae23062a2df4d944cb0bdd71f3bdb0172e4d1d7b3ebaa37a3e8b13338c36
- evidence_id: photo-agent-protein-Q3J433
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q3J433.json
  locator: Exact accession/entryType/proteinDescription/genes/organism; complete relevant
    comments and cited-reference records.
  accessed_at: '2026-10-22T03:11:20.178553Z'
  support: supports
  summary: Native Q3J433 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter
    sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 /
    NBRC 12203 / NCIMB 8253 / ATH 2.4.1.) (272943), primary gene names atpA. Synonyms,
    protein name, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence
    citations were read. These identify the stated example; automated or homology
    annotations are not promoted to direct formation or localization experiments.
  snapshot_sha256: 32297fbd8e0d7ea8b1a198aa3e9ea6a1a173c47ff5d741c300ee174a12a475f1
- evidence_id: photo-agent-protein-Q3IZ12
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q3IZ12.json
  locator: Exact accession/entryType/proteinDescription/genes/organism; complete relevant
    comments and cited-reference records.
  accessed_at: '2026-10-22T03:11:20.103257Z'
  support: supports
  summary: Native Q3IZ12 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter
    sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 /
    NBRC 12203 / NCIMB 8253 / ATH 2.4.1.) (272943), primary gene names atpB. Synonyms,
    protein name, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence
    citations were read. These identify the stated example; automated or homology
    annotations are not promoted to direct formation or localization experiments.
  snapshot_sha256: adeb72617b0c8e6929af69eb2f91d4bf3663d2d9e0247456abda566ad90020e9
- evidence_id: photo-agent-protein-Q3IZ13
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q3IZ13.json
  locator: Exact accession/entryType/proteinDescription/genes/organism; complete relevant
    comments and cited-reference records.
  accessed_at: '2026-10-22T03:11:20.141191Z'
  support: supports
  summary: Native Q3IZ13 is UniProtKB reviewed (Swiss-Prot), organism Cereibacter
    sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 /
    NBRC 12203 / NCIMB 8253 / ATH 2.4.1.) (272943), primary gene names atpE. Synonyms,
    protein name, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and their evidence
    citations were read. These identify the stated example; automated or homology
    annotations are not promoted to direct formation or localization experiments.
  snapshot_sha256: 9ef24a139908492f9978f6f81f757064dd2eea71ba8952a91afb5522a22c68d9
- evidence_id: photo-agent-reviewed-uniqueness
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+%28%28taxonomy_id%3A1111708+AND+%28gene_exact%3ApsaA+OR+gene_exact%3ApsbA2+OR+gene_exact%3ApsbA3+OR+gene_exact%3ApetA+OR+gene_exact%3ApetB%29%29+OR+%28taxonomy_id%3A1063+AND+%28gene_exact%3ApufL+OR+gene_exact%3ApufM+OR+gene_exact%3ApetB+OR+gene_exact%3ApetC+OR+gene_exact%3ApucA+OR+gene_exact%3ApucB%29%29%29&format=json&fields=accession%2Cid%2Creviewed%2Cgene_names%2Corganism_id%2Corganism_name&size=500
  locator: Exact query URL; all14 returned rows and organism IDs; no additional page
    indicated.
  accessed_at: '2026-10-22T03:16:15.563982Z'
  support: supports
  summary: The bounded reviewed exact-gene query returned14 rows including descendant-strain
    entries. Filtering by exact returned organism IDs confirms single relevant entries
    at tax1111708 and1063 for the stated primary symbols; descendant272943 rows are
    not counted as exact-species duplicates. P16033 contains both psbA2 and psbA3;
    fbcB/fbcC remain native synonyms for petB/petC. This is identity checking, not
    complex membership proof.
  snapshot_sha256: 177527fe7305d84cd2bbc481936a1a9adad1a60acef652b7980bebf65c636ecc
  search_scope: Public UniProt reviewed:true exact-gene query restricted to taxa1111708/1063,
    with returned descendants separately filtered by exact organism ID; size500 and14
    returned entries. Ignored local files are not applicable to this remote query.
    No local or global absence claim.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:05:42Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml'
  snapshot_sha256: acfeb29b4cdbc6c10aa0e86a62fd7da1ad787d95b424f2287fa66a1bf7594066
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    --out /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plasma_membrane_derived_chromatophore_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:05:43Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plasma_membrane_derived_chromatophore_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch38-20261022-tpqg0c05/plasma_membrane_derived_chromatophore_membrane-strict.tsv"
  snapshot_sha256: 804ce1089ae0cabaa9993c4b09258c56122e14bd16a975501498f01ca3b6fbc4
- evidence_id: focused-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  locator: Complete read-only native focused log
  accessed_at: '2026-10-22T03:11:42.079672Z'
  support: supports
  summary: "data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml\
    \  (GO:0042717)\n  chromatophore_photophosphorylation\tlh2\tCOVERED\t->lh2_antenna_complexes\
    \ (UniProtKB:P0C0Y0, UniProtKB:P0C0Y2)\n  chromatophore_photophosphorylation\t\
    f0f1_atp_synthase\tCOVERED\t->f0f1_atp_synthase (UniProtKB:A4WUM7, UniProtKB:Q3J433,\
    \ UniProtKB:Q3IZ12, UniProtKB:Q3IZ13)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n\
    \     2  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref\
    \ on the node\n     2  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: ef929a0e5157d1f3a48c9b179788b36c46452a947a43e0ed87cabc93cd342188
- evidence_id: focused-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch38-20261022-tpqg0c05/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  locator: Complete read-only native focused log
  accessed_at: '2026-10-22T03:11:43.535843Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '18 of 20 collected target identifiers returned OK. cellstructuremech:chromatophore_cytochrome_bc1_complex:
    SKIPPED; Exact local whole-complex identity occurs once in an ignored-inclusive
    top-level identifier search and is a frozen maintained input. The generic resolver
    has no external adapter for this locally minted identifier.; cellstructuremech:rc_lh1_pufx_core_complex:
    SKIPPED; Exact local whole-complex identity occurs once in an ignored-inclusive
    top-level identifier search and is a frozen maintained input. The generic resolver
    has no external adapter for this locally minted identifier. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
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
  topic: Exact identity, hierarchy and boundaries
  outcome: supported
  target_ids:
  - GO:0042717
  summary: GO0042717/SL0042 exactly identify the plasma-derived bacterial chromatophore
    membrane; GO0070112 separately identifies the organellar chromatophore membrane.
    The generic photosynthetic-membrane parent and related rather than exact broad
    chromatophore synonym preserve that boundary.
  evidence_ids:
  - record
  - photo-agent-go
  - photo-agent-SL-0042
  - photo-agent-SL-0044
  - photo-agent-SL-0045
- assessment_id: composition
  area: grounding
  topic: Material and complex constituent scope
  outcome: supported
  target_ids:
  - GO:0042717
  summary: The lipid row denotes the collective lipid matrix without misusing a whole-membrane
    GO term as chemical identity. Exact complexes or deliberately broad cohorts are
    evaluated at their declared level; existing protein examples are identities, not
    exhaustive stoichiometry or proof of incorporation. Photosynthetic function and
    membrane residence are supported at the stated cyanobacterial or Rhodobacter source
    scope.
  evidence_ids:
  - record
  - schema
  - photo-agent-go
  - photo-agent-SL-0042
  - photo-agent-bahatyrova2004-whiterose-pdf
  - photo-agent-comayras2005-browser-body1
  - photo-agent-feniouk2002-pmid
- assessment_id: necessity
  area: grounding
  topic: Individual assembly requirements remain unknown
  outcome: unknown
  target_ids:
  - GO:0042717
  summary: The collective bilayer is constitutional to a membrane, and broad reaction-center/pigment/carrier
    classes define the photosynthetic class. Those definitions do not establish depletion
    requirements for each named complex, protein, pigment or lipid species. UNKNOWN
    labels on the specific chromatophore/thylakoid complexes are preserved. No individual
    assembly-necessity experiment is inferred from mature localization, native structure,
    photosynthetic activity or inferred UniProt function.
  evidence_ids:
  - record
  - schema
  - photo-agent-go
  - photo-agent-bahatyrova2004-whiterose-pdf
  - photo-agent-feniouk2002-pmid
- assessment_id: proteins
  area: grounding
  topic: Reviewed gene/taxon examples and annotation evidence
  outcome: supported
  target_ids:
  - GO:0042717
  summary: All stated accessions, primary gene names or explicit aliases, organism
    nodes and reviewed status agree with the native records. Exact species and substrain
    nodes are retained. The current single-entry query agrees after exact-organism
    filtering. A curated localization annotation plus matching paper abstract is not
    presented as our own full-paper experiment audit.
  evidence_ids:
  - record
  - photo-agent-protein-P0C0Y0
  - photo-agent-protein-P0C0Y2
  - photo-agent-protein-A4WUM7
  - photo-agent-protein-Q3J433
  - photo-agent-protein-Q3IZ12
  - photo-agent-protein-Q3IZ13
  - photo-agent-reviewed-uniqueness
- assessment_id: taxon
  area: scope
  topic: Purple-bacterial examples and bounded source strains
  outcome: supported
  target_ids:
  - GO:0042717
  summary: ENA confirms Cereibacter/Rhodobacter sphaeroides identity and exact protein
    substrains. Bahatyrova NCIB8253 architecture, Comayras Ga quinone/excitation work
    and Feniouk R.capsulatus vesicle physiology are distinct experimental contexts.
    The NONMECHANISTIC graph is a Rhodobacter-supported illustrative route; it does
    not establish invariant dimer architecture, universal c2 usage, stoichiometry
    or a prevalence census for every purple bacterium.
  evidence_ids:
  - record
  - photo-agent-bahatyrova2004-whiterose-pdf
  - photo-agent-comayras2005-browser-body1
  - photo-agent-feniouk2002-pmid
  - photo-agent-tax-1063
  - photo-agent-tax-272943
  - photo-agent-tax-349102
- assessment_id: graph
  area: graph
  topic: Target-specific graph and functional scope
  outcome: supported
  target_ids:
  - GO:0042717
  summary: 'Six NONMECHANISTIC edges summarize LH2-to-core excitation, quinone reduction/reoxidation
    and sealed-vesicle proton motive force use. Comayras primary assay inhibition
    is retained as a source limit: the normal bc1 cycle is contextual synthesis, not
    an unperturbed cyclic-flux result from that experiment. Feniouk complete abstract
    supports PMF-coupled ATP-synthase charge transport; no detailed full-body ATP-product
    assay is certified.'
  evidence_ids:
  - record
  - photo-agent-go
  - photo-agent-SL-0042
  - photo-agent-SL-0044
  - photo-agent-SL-0045
  - photo-agent-bahatyrova2004-whiterose-pdf
  - photo-agent-comayras2005-browser-body1
  - photo-agent-feniouk2002-pmid
- assessment_id: coverage
  area: completeness
  topic: Complete record coverage without forced optional enrichment
  outcome: supported
  target_ids:
  - GO:0042717
  summary: Every target claim, evidence placement, graph node/edge and discussion
    was reviewed. Existing local complexes were resolved through frozen inputs. Optional
    new protein examples, absent chemical species/ratios, unasserted quantitative
    dimensions and complete comparative inventories are not made mandatory. No maintained
    image or direct quotation is present to audit. The precise findings do not alter
    valid generic identity or historical curation statements.
  evidence_ids:
  - record
  - schema
  - photo-agent-go
  - photo-agent-bahatyrova2004-whiterose-pdf
  - photo-agent-comayras2005-browser-body1
findings:
- finding_id: F1
  issue_key: plasma-membrane-derived-chromatophore-membrane-1
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the two existing complexes with verified whole-complex identifiers
  description: The existing LH2 constituent remains REVIEWED_LABEL_ONLY while the
    frozen maintained record cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex
    supplies the exact whole-complex identity in the same chromatophore context. The
    existing F0F1 constituent also remains label-only solely pending a chromatophore-localized
    accession, although active GO0045259 exactly names the F1-F0 ATP synthase complex;
    location belongs in its role/context. This is a bounded gap in two already asserted
    constituents, not a demand for an optional new inventory or a claim that the historical
    pass had access to future records.
  target_ids:
  - GO:0042717
  field_paths:
  - components[2].grounding_status
  - components[2].grounding_notes
  - components[4].grounding_status
  - components[4].grounding_notes
  - discussions[1]
  evidence_ids:
  - record
  - photo-agent-go
  - local-lh2_peripheral_light_harvesting_antenna_complex
  - photo-agent-SL-0042
  - photo-agent-bahatyrova2004-whiterose-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    role: maintained scientific record
  rule_id: Exact source identity, claim scope and grounded constituent identity
  native_severity: minor
  normalization_reason: Both constituents are already correctly described and supported;
    the available exact mappings improve interoperability without changing biology.
    A localization-specific new term is not required for the already named whole-complex
    identity.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0042717
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    role: maintained scientific record
  description: In separately authorized curation, ground LH2 to the exact maintained
    local complex and F0F1 to GO0045259, retain source-specific localization and UNKNOWN
    formation necessity, and resolve the current grounding task without rewriting
    historical events.
  acceptance_checks:
  - Each changed field matches the exact source organism, process or whole-complex
    identity.
  - Correct structure boundaries, protein identities and original history remain intact.
  - Native schema, strict, CURIE, graph and history gates pass.
limitations:
- Original source URL, UTC time and raw hash are preserved on unchanged imports. Browser-extracted
  representations have status:null and are not native HTTP200 bodies. Only the named
  paper sections or complete abstracts were actually read; no raw-data, figure-pixel
  or supplemental reanalysis was performed.
- Perez2024 is secondary synthesis available in bounded Introduction and electron-transport
  excerpts; native full-body routes returned403. Sui2021 and Feniouk2002 were assessed
  at complete native abstract scope; Feniouk numericPMC returned a challenge and university
  download timed out. No complete Methods or ATP-product measurement is inferred.
- Casella native/tagged-cell observations and Huokko light-shift biogenesis belong
  to Syn7942. Bahatyrova NCIB8253, Comayras Ga and Feniouk R.capsulatus are separate
  contexts; no universal strain-specific architecture, quantitative prevalence or
  exact stoichiometry is inferred.
- Individual formation necessity, exact lipid composition and exhaustive taxon-neutral
  protein inventories remain unknown beyond the declared collective class. Correct
  native protein identities and database experimental citation links are not a substitute
  for independently read full experiment bodies.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User explicitly requests one review for every unreviewed record; no scientific or
  history edits are made.
- 'iModulonDB is not applicable: these records assert physical complex identities
  and photochemistry, not expression-module membership or regulator-response claims.'
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
