# Source-backed review of meiotic telomere bouquet

- Review: 20261022T082336Z-meiotic-telomere-bouquet-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:57:59Z
- Finished UTC: 2026-10-22T08:23:36Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: whole-bouquet identity, species-scoped components, causal dependencies, figures and dataset provenance are supported. Conflicting Csm4 interpretations, bounded family nulls and formation uncertainties are preserved.

## Scope And Provenance

Exactly one entire target and 15 frozen input files. Sources/native identities were independently read within the declared extents; no neighboring maintained record is an unstated premise.

Selection: Batch59 strict ordered selection index 6; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:meiotic_telomere_bouquet | data/structures/other/meiotic_telomere_bouquet.yaml | maintained | meiotic telomere bouquet |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:meiotic_telomere_bouquet | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:meiotic_telomere_bouquet | Focused validator passed. |
| Focused native causal-graphs | passed | True | cellstructuremech:meiotic_telomere_bouquet | Focused check passed; claim-level science assessed independently. |
| Focused native verify | passed | True | cellstructuremech:meiotic_telomere_bouquet | Focused check passed; claim-level science assessed independently. |
| Claim-level scientific review | passed | True | cellstructuremech:meiotic_telomere_bouquet | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | cellstructuremech:meiotic_telomere_bouquet | 34 of 35 collected target identifiers returned OK. cellstructuremech:meiotic_telomere_bouquet: SKIPPED; Exact local identifier uniquely resolves to this maintained target in the full data/structures YAML traversal, including ignored files. This proves local reference identity, not external ontology resolution. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | cellstructuremech:meiotic_telomere_bouquet | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:meiotic_telomere_bouquet | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:meiotic_telomere_bouquet | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:meiotic_telomere_bouquet | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | cellstructuremech:meiotic_telomere_bouquet | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Whole polarized DNA/protein arrangement

identity: supported. Targets: cellstructuremech:meiotic_telomere_bouquet.

The local identity correctly distinguishes a meiotic chromosome-end arrangement from the clustering process, LINC subcomplexes, a generic nuclear rim or an ectopic partial telocentrosome. DNA is a constituent of the structure, supporting the protein-DNA-complex parent.

### Ten classes and eleven protein examples

grounding: supported. Targets: cellstructuremech:meiotic_telomere_bouquet.

Existing Rap1, SUN, Mps2 and Ndj1 families are supported by native class metadata and separate protein memberships, including both yeast Rap1 sequences. Taz1/Kms1 matches are only domains/superfamily; Bqt1/Bqt2/Csm4 bounded204 responses justify retaining the exact classes label-only. No guessed domain-to-whole-class substitution is proposed.

### Species, reference strains and experimental contexts

scope: supported. Targets: cellstructuremech:meiotic_telomere_bouquet.

Budding SK1 meiosis, S288C mitotic reconstitution, fission-yeast live meiosis/pat1 synchronization and Rabl-deficient mitotic manipulations remain separate. This literature supports the curated yeast settings; the target has no taxonomic-distribution row and does not assert a population census.

### Bounded positive dependencies do not require universal essentiality

evidence: unknown. Targets: cellstructuremech:meiotic_telomere_bouquet.

Fan depletion/localization and Bqt1/Rap1 perturbations support the stated dependencies within their experimental contexts. All component UNKNOWN labels remain defensible for a cross-species structure without a universal per-component formation test. Maintenance, pairing, spindle progression and physical initial formation are not interchangeable.

### Two scoped causal models preserve conflicts and stages

graph: supported. Targets: cellstructuremech:meiotic_telomere_bouquet.

The budding assembly graph states tested localization/clustering dependencies without claiming fixed whole-bouquet stoichiometry. The fission graph addresses continued Bqt1-dependent linkage and timely prophase/spindle progression, preserving partial penetrance and artificial AID timing. Fan-versus-Lee Csm4 membership interpretations, Rap1 phosphomutant results and partial mitotic telocentrosomes remain explicit.

### Tracked figures, license and deposited experiment

evidence: supported. Targets: cellstructuremech:meiotic_telomere_bouquet.

Both Fig4 files were visually inspected and match their exact source package MD5. Article permissions specify CC BY4.0; Amelina data CC0 wording does not replace its article/figure license. PRIDE identity and experimental metadata agree without raw-data reanalysis.

### Entire maintained target with explicit source tiers

completeness: supported. Targets: cellstructuremech:meiotic_telomere_bouquet.

Every target field, current discussion, graph, example and history entry was read. Existing named proteins and source IDs were checked. Optional absent detail alone is not treated as a defect; no maintained scientific content was changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/meiotic_telomere_bouquet.yaml; Entire maintained YAML, including all scientific fields, examples, graphs, images, discussions and history | context_only | All target bytes were read; no neighboring record is an unstated scientific premise. |
| curation | docs/CURATION.md; Exact component-class grounding and reviewed-label-only contract | context_only | Species accessions establish examples, not automatic whole-class groundings; acknowledged unknowns and empty optional slots alone are not defects. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum, StructuralComponent and causal graphs | context_only | Physical formation necessity is distinct from function, viability and localization. COMMON means present in most members, with exceptional losses; VARIABLE means nonuniform occurrence, not merely unknown prevalence. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Actor, stage and edge-level source scope | context_only | A coarse mechanism may omit unresolved intermediates, but source-specific claims must retain assay, species and epistemic boundaries. |
| micro59-doi-10.1016_j.cell.2006.01.048 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2006.01.048%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity fields and complete abstractText. | supports | PMID16615890: Meiotic proteins bqt1 and bqt2 tether telomeres to form the bouquet arrangement of chromosomes. Chikashige Y, Tsutsumi C, Yamane M, Okamasa K, Haraguchi T, Hiraoka Y. (2006), DOI10.1016/j.cell.2006.01.048. The complete native abstract was read; this row does not imply main-body access. |
| micro59-doi-10.1016_j.cub.2020.01.054 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2020.01.054%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity fields and complete abstractText. | supports | PMID32059771: Extranuclear Structural Components that Mediate Dynamic Chromosome Movements in Yeast Meiosis. Lee CY, Bisig CG, Conrad MM, Ditamo Y, Previato de Almeida L, Dresser ME, Pezza RJ. (2020), DOI10.1016/j.cub.2020.01.054. The complete native abstract was read; this row does not imply main-body access. |
| micro59-doi-10.1038_celldisc.2017.41 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fcelldisc.2017.41%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity fields and complete abstractText. | supports | PMID29123917: The telomere bouquet facilitates meiotic prophase progression and exit in fission yeast. Moiseeva V, Amelina H, Collopy LC, Armstrong CA, Pearson SR, Tomita K. (2017), DOI10.1038/celldisc.2017.41. The complete native abstract was read; this row does not imply main-body access. |
| micro59-doi-10.1038_s41467-025-56049-9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41467-025-56049-9%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity fields and complete abstractText. | supports | PMID39833200: Centromere positioning orchestrates telomere bouquet formation and the initiation of meiotic differentiation. Jiménez-Martín A, Pineda-Santaella A, Martín-García R, Esteban-Villafañe R, Matarrese A, Pinto-Cruz J, Camacho-Cabañas S, León-Periñán D, Terrizzano A, Daga RR, Braun S, Fernández-Álvarez A. (2025), DOI10.1038/s41467-025-56049-9. The complete native abstract was read; this row does not imply main-body access. |
| micro59-doi-10.1186_s12915-015-0149-x | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1186%2Fs12915-015-0149-x%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity fields and complete abstractText. | supports | PMID26058898: Telomere protein Rap1 is a charge resistant scaffolding protein in chromosomal bouquet formation. Amelina H, Subramaniam S, Moiseeva V, Armstrong CA, Pearson SR, Tomita K. (2015), DOI10.1186/s12915-015-0149-x. The complete native abstract was read; this row does not imply main-body access. |
| micro59-doi-10.26508_lsa.202000824 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.26508%2Flsa.202000824%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity fields and complete abstractText. | supports | PMID32967926: Mps2 links Csm4 and Mps3 to form a telomere-associated LINC complex in budding yeast. Fan J, Jin H, Koch BA, Yu HG. (2020), DOI10.26508/lsa.202000824. The complete native abstract was read; this row does not imply main-body access. |
| micro59-protein-P11938 | https://rest.uniprot.org/uniprotkb/P11938.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed P11938 identifies RAP1 in taxon559292. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-RAP1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARAP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed RAP1 query for organism559292 returns only P11938; primary name or declared synonym matches. |
| micro59-protein-Q96TL7 | https://rest.uniprot.org/uniprotkb/Q96TL7.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed Q96TL7 identifies rap1 in taxon284812. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-rap1-284812 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Arap1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed rap1 query for organism284812 returns only Q96TL7; primary name or declared synonym matches. |
| micro59-protein-P79005 | https://rest.uniprot.org/uniprotkb/P79005.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed P79005 identifies taz1 in taxon284812. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-taz1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ataz1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed taz1 query for organism284812 returns only P79005; primary name or declared synonym matches. |
| micro59-protein-Q92358 | https://rest.uniprot.org/uniprotkb/Q92358.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed Q92358 identifies bqt1 in taxon284812. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-bqt1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Abqt1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed bqt1 query for organism284812 returns only Q92358; primary name or declared synonym matches. |
| micro59-protein-Q9US52 | https://rest.uniprot.org/uniprotkb/Q9US52.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed Q9US52 identifies bqt2 in taxon284812. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-bqt2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Abqt2%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed bqt2 query for organism284812 returns only Q9US52; primary name or declared synonym matches. |
| micro59-protein-P47069 | https://rest.uniprot.org/uniprotkb/P47069.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed P47069 identifies MPS3 in taxon559292. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-MPS3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMPS3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed MPS3 query for organism559292 returns only P47069; primary name or declared synonym matches. |
| micro59-protein-Q09825 | https://rest.uniprot.org/uniprotkb/Q09825.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed Q09825 identifies sad1 in taxon284812. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-sad1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Asad1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed sad1 query for organism284812 returns only Q09825; primary name or declared synonym matches. |
| micro59-protein-P53159 | https://rest.uniprot.org/uniprotkb/P53159.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed P53159 identifies MPS2 in taxon559292. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-MPS2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMPS2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed MPS2 query for organism559292 returns only P53159; primary name or declared synonym matches. |
| micro59-protein-Q08955 | https://rest.uniprot.org/uniprotkb/Q08955.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed Q08955 identifies CSM4 in taxon559292. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-CSM4 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACSM4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed CSM4 query for organism559292 returns only Q08955; primary name or declared synonym matches. |
| micro59-protein-Q12366 | https://rest.uniprot.org/uniprotkb/Q12366.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed Q12366 identifies NDJ1 in taxon559292. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-NDJ1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANDJ1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed NDJ1 query for organism559292 returns only Q12366; primary name or declared synonym matches. |
| micro59-protein-P87245 | https://rest.uniprot.org/uniprotkb/P87245.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed P87245 identifies kms1 in taxon284812. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-kms1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Akms1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed kms1 query for organism284812 returns only P87245; primary name or declared synonym matches. |
| micro59-tax284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Native taxId, scientificName, rank, lineage and relevant equivalent names. | supports | ENA taxId284812 identifies Schizosaccharomyces pombe 972h-, rank strain. Reference strains and experimental cultures are distinguished. |
| micro59-tax4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; Native taxId, scientificName, rank, lineage and relevant equivalent names. | supports | ENA taxId4896 identifies Schizosaccharomyces pombe, rank species. Reference strains and experimental cultures are distinguished. |
| micro59-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Native taxId, scientificName, rank, lineage and relevant equivalent names. | supports | ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. Reference strains and experimental cultures are distinguished. |
| micro59-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Native taxId, scientificName, rank, lineage and relevant equivalent names. | supports | ENA taxId559292 identifies Saccharomyces cerevisiae S288C, rank strain. Reference strains and experimental cultures are distinguished. |
| micro59-IPR031433 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031433/; Complete type/name/descriptions/member_databases; whole-family versus domain scope. | supports | IPR031433 is the Monopolar spindle protein 2 family. Native description and member signatures were read; protein accession membership is supplied separately by native UniProt evidence. Generic background mechanism is not treated as a new direct experiment. |
| micro59-IPR039595 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039595/; Complete type/name/descriptions/member_databases; whole-family versus domain scope. | supports | IPR039595 is the TE2IP/Rap1 family. Native description and member signatures were read; protein accession membership is supplied separately by native UniProt evidence. Generic background mechanism is not treated as a new direct experiment. |
| micro59-IPR045119 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045119/; Complete type/name/descriptions/member_databases; whole-family versus domain scope. | supports | IPR045119 is the SUN domain-containing protein 1-5 family. Native description and member signatures were read; protein accession membership is supplied separately by native UniProt evidence. Generic background mechanism is not treated as a new direct experiment. |
| micro59-IPR062583 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062583/; Complete type/name/descriptions/member_databases; whole-family versus domain scope. | supports | IPR062583 is the Non-disjunction protein 1 family. Native description and member signatures were read; protein accession membership is supplied separately by native UniProt evidence. Generic background mechanism is not treated as a new direct experiment. |
| micro59-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228,GO:0000781,GO:0005634,GO:0032200,GO:0032993,GO:0034993,GO:0042910,GO:0045141,GO:0140330,GO:1902495,GO:1990203,GO:1990281,GO:1990612; Named exact native entries in this response, including GO0005634; identity, aspect, definition and relevant typed links. No universal synonymy of bouquet and LINC is inferred. | supports | The bouquet is a DNA-containing nuclear arrangement, fitting broader GO0032993; GO0045141 is the clustering process, not this structure. GO0034993 and GO1990612 denote narrower LINC assemblies, while GO0000228/0000781 identify chromosomes/telomeric regions and GO0032200 telomere organization. |
| micro59-GO0032993-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032993/ancestors?relations=is_a; Complete exact requested-term is_a ancestor array and comment. | supports | The exact protein-DNA-complex term belongs to the protein-containing-complex hierarchy. Its comment requires DNA as a constituent, consistent with this chromosome-end arrangement. |
| micro59-SO0000624 | https://www.ebi.ac.uk/ols4/api/ontologies/so/terms?obo_id=SO:0000624; Complete exact SO term identity/definition/synonyms/active status. | supports | SO0000624 is the telomere sequence feature, with telomeric DNA/sequence synonyms; it denotes the chromosome-end DNA constituent, not the entire bouquet. |
| micro59-bouquet-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=bouquet&amp;limit=25; Complete native QuickGO search response and original URL, limit25. | context_only | The bounded bouquet search returned the clustering biological process GO0045141. This search does not demonstrate exhaustive absence of a differently named cellular-component term. |
| micro59-fan2020-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC7536833.1/PMC7536833.1.xml; Genuine original JATS: complete Introduction s1, Results s3–9, Discussion s10 and Methods s12–18, all embedded main/supplement captions; front permissions. Separate supplement files not read. Fig4 local pixels separately inspected. | supports | Native SK1 meiotic localization/depletion experiments support Ndj1/Mps3-dependent Mps2 at chromosome ends, Mps2-dependent Csm4 localization and efficient bouquet clustering. Mps2/Csm4 perturbations affect pairing/recombination. S288C mitotic ectopic reconstitution is a separate context; the Discussion nonamer is speculative and is not exported as whole-bouquet stoichiometry. |
| micro59-amelina2015-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4660835.1/PMC4660835.1.xml; Genuine original JATS: Results Sec4–6, Discussion Sec7, Methods Sec10–12/Sec15/Sec17, including Fig2–4 captions; front permissions. Other sections/supplement files not read. Fig4 local pixels separately inspected. | supports | Rap1 phosphorylation increases across meiotic prophase, but tested phosphomimetic/nonphosphorylatable clusters retain bouquet behavior. DD337AA preserves telomeric localization yet disrupts Bqt1/2 interaction and clustering. These are mutation/interaction assays, not evidence that physiological bouquet release is driven by those two residues. |
| micro59-moiseeva2017-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5674143.1/PMC5674143.1.xml; Genuine original JATS: complete Introduction; Results titled Bouquet formation ensures entry into meiosis I, The telomere bouquet stabilises CDK1cyclin B at the SPB prior to its termination, and Premature termination of the bouquet leads to spindle defects; complete Discussion; Methods Strains and media, Microscope image acquisition, Auxin-inducible system. Other Results/Methods, movies and supplemental files not read. | supports | The fission-yeast bouquet persists beyond horsetail oscillation. bqt1 deletion and conditional Bqt1-AID loss support continued chromosome-SPB association in timely CDK1/Cdc13 accumulation and spindle progression, with only subsets showing severe SPB failure. AID-induced loss is an experimental perturbation, not an identified physiological dissolution signal. |
| micro59-csm2020-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC7181386.1/PMC7181386.1.xml; Genuine original JATS: complete S3, S8 and Discussion S10; Methods S14/S19/S20. Other Results/Methods and supplement files not read. | supports | Meiotic Mps2 localization/association supports a LINC link; Csm4 interacts with Mps2 and contributes to Myo2 localization, but this paper explicitly interprets Csm4 as an accessory regulator rather than structural LINC component. That interpretation differs from Fan2020 and is retained in the record rather than erased. |
| micro59-jimenez2025-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/PMC11747273.1.xml; Genuine original JATS: Results Sec8–11, complete Discussion Sec12, Methods Sec14/Sec17, embedded Fig6–9 captions. Earlier Results, other Methods, supplements and pixels not read. | supports | Rabl-deficient mitotic cells with ectopic Bqt1/2 recruit selected telocentrosome factors and some telomeres reach the SPB, but do not form a complete ordinary bouquet and lack detected dynein. Separate diploid meiotic Ndc80-retention experiments constrain natural entry. Proposed Cdk1 recycling remains a mechanistic interpretation. |
| micro59-PXD001841 | https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD001841; Complete project identity/title/description/sample and data protocols, submissionType, organism, instrument and publication; raw files not downloaded or reanalysed. | supports | PXD001841 is the PARTIAL S.pombe Rap1 phosphoproteomics deposit. Native description/protocols specify homozygous diploid pat1-114 cultures, 3.5/4.5h, Rap1-3xPK immunoprecipitation, LC-MS/MS and LTQ Orbitrap Velos; its linked publication is Amelina2015. |
| micro59-ipr-matches-P79005 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P79005/; Complete results/count/next:null and metadata type/name for this accession only. No all-InterPro absence inference. | supports | The complete accession match set contains only domains or a broad homologous superfamily, not a verified exact whole-protein family for this named class. |
| micro59-ipr-matches-P87245 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P87245/; Complete results/count/next:null and metadata type/name for this accession only. No all-InterPro absence inference. | supports | The complete accession match set contains only domains or a broad homologous superfamily, not a verified exact whole-protein family for this named class. |
| micro59-ipr-protein-Q92358 | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q92358/entry/interpro/; Actual HTTP204 status, empty-body SHA and exact endpoint. | context_only | The retained exact accession request returned HTTP204 and an empty body. It supplies no integrated match evidence; this bounded null does not prove biological absence or lack of all possible external family mappings. |
| micro59-ipr-protein-Q9US52 | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q9US52/entry/interpro/; Actual HTTP204 status, empty-body SHA and exact endpoint. | context_only | The retained exact accession request returned HTTP204 and an empty body. It supplies no integrated match evidence; this bounded null does not prove biological absence or lack of all possible external family mappings. |
| micro59-ipr-protein-Q08955 | https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q08955/entry/interpro/; Actual HTTP204 status, empty-body SHA and exact endpoint. | context_only | The retained exact accession request returned HTTP204 and an empty body. It supplies no integrated match evidence; this bounded null does not prove biological absence or lack of all possible external family mappings. |
| micro59-PMC7536833-package | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC7536833.1.json; Exact pmcid/doi/license_code and Fig4 media_urls MD5; not a claim that other package media were inspected. | supports | Native package metadata identifies the cited article and its Fig4 media; the deposited Fig4 MD5 matches the tracked local bytes. CC BY package status is refined to CC BY4.0 by the separately inspected article permissions. |
| image-7536833 | data/images/other/meiotic_telomere_bouquet/pmc7536833_fig4.jpg; Entire tracked figure visually inspected; SHA256 940897253f430c6d6d5b4b80b1dca59d2a5b6db16a5bbfa4f3bb531dfc253b07 | context_only | Fig4 panel labels, microscopy channels, genotype/context and accompanying plots agree with the caption. Fan panelsA/B show clustering, C–E viability/recombination; AmelinaA is alignment, B asci, C mitotic colocalization, D meiotic time series. No raw pixel quantification was repeated. |
| micro59-PMC4660835-package | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC4660835.1.json; Exact pmcid/doi/license_code and Fig4 media_urls MD5; not a claim that other package media were inspected. | supports | Native package metadata identifies the cited article and its Fig4 media; the deposited Fig4 MD5 matches the tracked local bytes. CC BY package status is refined to CC BY4.0 by the separately inspected article permissions. |
| image-4660835 | data/images/other/meiotic_telomere_bouquet/pmc4660835_fig4.jpg; Entire tracked figure visually inspected; SHA256 c38253a30a2f55547b92f39c20ad0308a8ee450d1cf25af84dcc6659d5ac8ca4 | context_only | Fig4 panel labels, microscopy channels, genotype/context and accompanying plots agree with the caption. Fan panelsA/B show clustering, C–E viability/recombination; AmelinaA is alignment, B asci, C mitotic colocalization, D meiotic time series. No raw pixel quantification was repeated. |
| schema-result | just validate data/structures/other/meiotic_telomere_bouquet.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/meiotic_telomere_bouquet.yaml |
| strict-result | just validate-strict data/structures/other/meiotic_telomere_bouquet.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/meiotic_telomere_bouquet-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/meiotic_telomere_bouquet.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/meiotic_telomere_bouquet-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch59-20261022-t3ere5ku/meiotic_telomere_bouquet-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/meiotic_telomere_bouquet.yaml --causal-graphs; Complete focused read-only native log | supports | data/structures/other/meiotic_telomere_bouquet.yaml  (cellstructuremech:meiotic_telomere_bouquet)<br>  budding_yeast_tether_assembly	ndj1	COVERED	-&gt;ndj1 (UniProtKB:Q12366)<br>  budding_yeast_tether_assembly	mps3	COVERED	-&gt;sun (UniProtKB:P47069, UniProtKB:Q09825)<br>  budding_yeast_tether_assembly	mps2	COVERED	-&gt;mps2 (UniProtKB:P53159)<br>  budding_yeast_tether_assembly	csm4	COVERED	-&gt;csm4 (UniProtKB:Q08955)<br>  fission_yeast_bouquet_maintenance	bqt1	COVERED	-&gt;bqt1 (UniProtKB:Q92358)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     5  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     5  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/meiotic_telomere_bouquet.yaml --verify; Complete focused read-only native log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/meiotic_telomere_bouquet.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 34 of 35 collected target identifiers returned OK. cellstructuremech:meiotic_telomere_bouquet: SKIPPED; Exact local identifier uniquely resolves to this maintained target in the full data/structures YAML traversal, including ignored files. This proves local reference identity, not external ontology resolution. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Only the exact primary sections and captions named in evidence were read. Chikashige2006 was checked at complete native abstract tier only; no primary body or supplement access is implied. Other annotation papers remain uninspected.
- Only the two tracked Fig4 images were visually inspected. Separate supplemental files, movies and raw PRIDE data were not reanalysed; no microscopy quantification was independently reproduced.
- Family nulls are bounded accession responses, not exhaustive authority absence. The bouquet ontology search is a bounded candidate check, not proof that every possible cellular-component term was excluded.
- The eleven reviewed sequence examples are reference identities, not assertions that their exact reference strains supplied every experimental culture.
- Csm4 structural-versus-accessory LINC interpretations remain conflicting. Species-specific localization, formation and maintenance assays do not establish universal component necessity or a physiological bouquet-release trigger.
- Reused source bytes retain original URL, UTC and SHA256. HTTP status alone is not treated as evidence of article-body readability.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requests a review for every unreviewed record, including qualified clean cases.
- No maintained record, historical review or initial inspection snapshot is edited.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T082336Z-meiotic-telomere-bouquet-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of meiotic telomere bouquet
started_at: '2026-10-22T07:57:59Z'
finished_at: '2026-10-22T08:23:36Z'
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
summary: 'Qualified pass: whole-bouquet identity, species-scoped components, causal
  dependencies, figures and dataset provenance are supported. Conflicting Csm4 interpretations,
  bounded family nulls and formation uncertainties are preserved.'
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
  - path: data/images/other/meiotic_telomere_bouquet/pmc4660835_fig4.jpg
    sha256: c38253a30a2f55547b92f39c20ad0308a8ee450d1cf25af84dcc6659d5ac8ca4
    role: context
  - path: data/images/other/meiotic_telomere_bouquet/pmc7536833_fig4.jpg
    sha256: 940897253f430c6d6d5b4b80b1dca59d2a5b6db16a5bbfa4f3bb531dfc253b07
    role: context
  - path: data/structures/other/meiotic_telomere_bouquet.yaml
    sha256: 12c53db6d591b5706043614a227b34a9bd6bc8568db4f160d56f4e864a2506dd
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
- target_id: cellstructuremech:meiotic_telomere_bouquet
  path: data/structures/other/meiotic_telomere_bouquet.yaml
  label: meiotic telomere bouquet
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/meiotic_telomere_bouquet.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target and 15 frozen input files. Sources/native
    identities were independently read within the declared extents; no neighboring
    maintained record is an unstated premise.
  selection: Batch59 strict ordered selection index 6; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  command: just validate data/structures/other/meiotic_telomere_bouquet.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  command: just validate-strict data/structures/other/meiotic_telomere_bouquet.yaml
    --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/meiotic_telomere_bouquet-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/meiotic_telomere_bouquet.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; claim-level science assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/meiotic_telomere_bouquet.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; claim-level science assessed independently.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-doi-10.1016_j.cell.2006.01.048
  - micro59-doi-10.1016_j.cub.2020.01.054
  - micro59-doi-10.1038_celldisc.2017.41
  - micro59-doi-10.1038_s41467-025-56049-9
  - micro59-doi-10.1186_s12915-015-0149-x
  - micro59-doi-10.26508_lsa.202000824
  - micro59-protein-P11938
  - micro59-gene-RAP1-559292
  - micro59-protein-Q96TL7
  - micro59-gene-rap1-284812
  - micro59-protein-P79005
  - micro59-gene-taz1
  - micro59-protein-Q92358
  - micro59-gene-bqt1
  - micro59-protein-Q9US52
  - micro59-gene-bqt2
  - micro59-protein-P47069
  - micro59-gene-MPS3
  - micro59-protein-Q09825
  - micro59-gene-sad1
  - micro59-protein-P53159
  - micro59-gene-MPS2
  - micro59-protein-Q08955
  - micro59-gene-CSM4
  - micro59-protein-Q12366
  - micro59-gene-NDJ1
  - micro59-protein-P87245
  - micro59-gene-kms1
  - micro59-tax284812
  - micro59-tax4896
  - micro59-tax4932
  - micro59-tax559292
  - micro59-IPR031433
  - micro59-IPR039595
  - micro59-IPR045119
  - micro59-IPR062583
  - micro59-go
  - micro59-GO0032993-ancestors
  - micro59-SO0000624
  - micro59-bouquet-go-search
  - micro59-fan2020-jats
  - micro59-amelina2015-jats
  - micro59-moiseeva2017-jats
  - micro59-csm2020-jats
  - micro59-jimenez2025-jats
  - micro59-PXD001841
  - micro59-ipr-matches-P79005
  - micro59-ipr-matches-P87245
  - micro59-ipr-protein-Q92358
  - micro59-ipr-protein-Q9US52
  - micro59-ipr-protein-Q08955
  - micro59-PMC7536833-package
  - image-7536833
  - micro59-PMC4660835-package
  - image-4660835
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  summary: '34 of 35 collected target identifiers returned OK. cellstructuremech:meiotic_telomere_bouquet:
    SKIPPED; Exact local identifier uniquely resolves to this maintained target in
    the full data/structures YAML traversal, including ignored files. This proves
    local reference identity, not external ontology resolution. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
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
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/meiotic_telomere_bouquet.yaml
  locator: Entire maintained YAML, including all scientific fields, examples, graphs,
    images, discussions and history
  accessed_at: '2026-10-22T08:10:29Z'
  support: context_only
  summary: All target bytes were read; no neighboring record is an unstated scientific
    premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact component-class grounding and reviewed-label-only contract
  accessed_at: '2026-10-22T08:10:29Z'
  support: context_only
  summary: Species accessions establish examples, not automatic whole-class groundings;
    acknowledged unknowns and empty optional slots alone are not defects.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum, StructuralComponent and causal graphs
  accessed_at: '2026-10-22T08:10:29Z'
  support: context_only
  summary: Physical formation necessity is distinct from function, viability and localization.
    COMMON means present in most members, with exceptional losses; VARIABLE means
    nonuniform occurrence, not merely unknown prevalence.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Actor, stage and edge-level source scope
  accessed_at: '2026-10-22T08:10:29Z'
  support: context_only
  summary: A coarse mechanism may omit unresolved intermediates, but source-specific
    claims must retain assay, species and epistemic boundaries.
- evidence_id: micro59-doi-10.1016_j.cell.2006.01.048
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2006.01.048%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity fields and complete abstractText.
  accessed_at: '2026-10-22T08:02:50.021723Z'
  support: supports
  summary: 'PMID16615890: Meiotic proteins bqt1 and bqt2 tether telomeres to form
    the bouquet arrangement of chromosomes. Chikashige Y, Tsutsumi C, Yamane M, Okamasa
    K, Haraguchi T, Hiraoka Y. (2006), DOI10.1016/j.cell.2006.01.048. The complete
    native abstract was read; this row does not imply main-body access.'
  snapshot_sha256: e9fce5a295786a47264e8f33be0f8b8fe4788aad086ae424b34e1e2a6f3431db
- evidence_id: micro59-doi-10.1016_j.cub.2020.01.054
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2020.01.054%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity fields and complete abstractText.
  accessed_at: '2026-10-22T08:02:50.272236Z'
  support: supports
  summary: 'PMID32059771: Extranuclear Structural Components that Mediate Dynamic
    Chromosome Movements in Yeast Meiosis. Lee CY, Bisig CG, Conrad MM, Ditamo Y,
    Previato de Almeida L, Dresser ME, Pezza RJ. (2020), DOI10.1016/j.cub.2020.01.054.
    The complete native abstract was read; this row does not imply main-body access.'
  snapshot_sha256: c290232a3c51c2c52603930b37629bad71f58a3f7566f460279678a3990f3ca8
- evidence_id: micro59-doi-10.1038_celldisc.2017.41
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fcelldisc.2017.41%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity fields and complete abstractText.
  accessed_at: '2026-10-22T08:02:50.302797Z'
  support: supports
  summary: 'PMID29123917: The telomere bouquet facilitates meiotic prophase progression
    and exit in fission yeast. Moiseeva V, Amelina H, Collopy LC, Armstrong CA, Pearson
    SR, Tomita K. (2017), DOI10.1038/celldisc.2017.41. The complete native abstract
    was read; this row does not imply main-body access.'
  snapshot_sha256: ca7f7535dfe376fa468e9cdf620a9e2a374962c376ed21b1109d8d97f4b22f05
- evidence_id: micro59-doi-10.1038_s41467-025-56049-9
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41467-025-56049-9%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity fields and complete abstractText.
  accessed_at: '2026-10-22T08:02:50.620303Z'
  support: supports
  summary: 'PMID39833200: Centromere positioning orchestrates telomere bouquet formation
    and the initiation of meiotic differentiation. Jiménez-Martín A, Pineda-Santaella
    A, Martín-García R, Esteban-Villafañe R, Matarrese A, Pinto-Cruz J, Camacho-Cabañas
    S, León-Periñán D, Terrizzano A, Daga RR, Braun S, Fernández-Álvarez A. (2025),
    DOI10.1038/s41467-025-56049-9. The complete native abstract was read; this row
    does not imply main-body access.'
  snapshot_sha256: 73b33c6a6a4314b3deefcb27be1ce69a82dabb62901294862bc9cda504eca236
- evidence_id: micro59-doi-10.1186_s12915-015-0149-x
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1186%2Fs12915-015-0149-x%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity fields and complete abstractText.
  accessed_at: '2026-10-22T08:02:51.027791Z'
  support: supports
  summary: 'PMID26058898: Telomere protein Rap1 is a charge resistant scaffolding
    protein in chromosomal bouquet formation. Amelina H, Subramaniam S, Moiseeva V,
    Armstrong CA, Pearson SR, Tomita K. (2015), DOI10.1186/s12915-015-0149-x. The
    complete native abstract was read; this row does not imply main-body access.'
  snapshot_sha256: 0eb45d0e97ef0d2eed669e139c1d2b1e07d0ffef40b77444c83321e14686515e
- evidence_id: micro59-doi-10.26508_lsa.202000824
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.26508%2Flsa.202000824%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity fields and complete abstractText.
  accessed_at: '2026-10-22T08:02:51.243360Z'
  support: supports
  summary: 'PMID32967926: Mps2 links Csm4 and Mps3 to form a telomere-associated LINC
    complex in budding yeast. Fan J, Jin H, Koch BA, Yu HG. (2020), DOI10.26508/lsa.202000824.
    The complete native abstract was read; this row does not imply main-body access.'
  snapshot_sha256: fcde324b4bf088b3b88fa159d9056fba36991b372f01c825eceeb76928bd7dd8
- evidence_id: micro59-protein-P11938
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P11938.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:47.142992Z'
  support: supports
  summary: Reviewed P11938 identifies RAP1 in taxon559292. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: 2494bab8cd33b37ad8c1f05bdd1b39aa0f9a87966d42099d849451138cddcd7c
- evidence_id: micro59-gene-RAP1-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARAP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:05:24.468870Z'
  support: supports
  summary: The exact reviewed RAP1 query for organism559292 returns only P11938; primary
    name or declared synonym matches.
  snapshot_sha256: ab7ff1efdd46ef94142e21243af99cf3598f9a1dbbd9a7cab65f02a41625ecab
- evidence_id: micro59-protein-Q96TL7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q96TL7.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:49.280004Z'
  support: supports
  summary: Reviewed Q96TL7 identifies rap1 in taxon284812. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: 078e07543602ed7f3b35b3bf70673ee22c6eac984356be396631678a49d82557
- evidence_id: micro59-gene-rap1-284812
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Arap1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:05:24.469212Z'
  support: supports
  summary: The exact reviewed rap1 query for organism284812 returns only Q96TL7; primary
    name or declared synonym matches.
  snapshot_sha256: 2ffe996a7b041c6de6e42281d29790acc7fbd58d3ad722f4329d46f37c2fa912
- evidence_id: micro59-protein-P79005
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P79005.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:48.000253Z'
  support: supports
  summary: Reviewed P79005 identifies taz1 in taxon284812. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: fa9ec78e0138e83e9d8b7200c2efc6ff4b6fde882075a0a8981271d0eaf170a0
- evidence_id: micro59-gene-taz1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ataz1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:52.754615Z'
  support: supports
  summary: The exact reviewed taz1 query for organism284812 returns only P79005; primary
    name or declared synonym matches.
  snapshot_sha256: 055451ed88b545f35717b3894e25936a8d74716222773b14ffac07979c110223
- evidence_id: micro59-protein-Q92358
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q92358.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:48.743584Z'
  support: supports
  summary: Reviewed Q92358 identifies bqt1 in taxon284812. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: f4cfccab706bbf9515cd342b8bf6a7409bdb96c9a45f0e6ac5320e967827dd42
- evidence_id: micro59-gene-bqt1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Abqt1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:53.065978Z'
  support: supports
  summary: The exact reviewed bqt1 query for organism284812 returns only Q92358; primary
    name or declared synonym matches.
  snapshot_sha256: 6be1fc85736b7c4c2ee56f5d93cfc4b48478ea03ce032e84c8dcf7394db6f47a
- evidence_id: micro59-protein-Q9US52
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9US52.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:49.355310Z'
  support: supports
  summary: Reviewed Q9US52 identifies bqt2 in taxon284812. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: 51cfcf49971d8963b57f32b278b49e710b600813b392a15565ffb4b80b2b09e9
- evidence_id: micro59-gene-bqt2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Abqt2%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:53.209384Z'
  support: supports
  summary: The exact reviewed bqt2 query for organism284812 returns only Q9US52; primary
    name or declared synonym matches.
  snapshot_sha256: de04fa46801632073190ecca778cd03ce1e98cdd3f0800c7ad14b54d4584501f
- evidence_id: micro59-protein-P47069
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47069.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:47.165497Z'
  support: supports
  summary: Reviewed P47069 identifies MPS3 in taxon559292. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: 9f17e95c1a6b7cae0a31b29cb1f9fda9844310b2bb78188c29737219904b48bc
- evidence_id: micro59-gene-MPS3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMPS3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:53.620147Z'
  support: supports
  summary: The exact reviewed MPS3 query for organism559292 returns only P47069; primary
    name or declared synonym matches.
  snapshot_sha256: 51f164fe91071b4ab7427831466ca45d34ffb8f46668c5a87fdc6cdb933b8c71
- evidence_id: micro59-protein-Q09825
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q09825.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:48.698023Z'
  support: supports
  summary: Reviewed Q09825 identifies sad1 in taxon284812. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: af97b71167c7297318086add00ac1143a9ab78a2f714035f76ff4c31bf77993d
- evidence_id: micro59-gene-sad1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Asad1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:53.820624Z'
  support: supports
  summary: The exact reviewed sad1 query for organism284812 returns only Q09825; primary
    name or declared synonym matches.
  snapshot_sha256: b27a8202180896da0753b5eaec6a7f7808b8730993689b8388bc390111a8f90e
- evidence_id: micro59-protein-P53159
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53159.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:47.182492Z'
  support: supports
  summary: Reviewed P53159 identifies MPS2 in taxon559292. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: 8b3bc0f8080249f11ca0198a5ed29fd0a508d1e660168ae1ca94a8e0e6cfcc75
- evidence_id: micro59-gene-MPS2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMPS2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:53.842901Z'
  support: supports
  summary: The exact reviewed MPS2 query for organism559292 returns only P53159; primary
    name or declared synonym matches.
  snapshot_sha256: 5b19a3e891029524557404a2bc2182f571dc7519e7277e99bbec4469c752e97b
- evidence_id: micro59-protein-Q08955
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08955.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:48.654452Z'
  support: supports
  summary: Reviewed Q08955 identifies CSM4 in taxon559292. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: aea16832642a882ded862712b1e3e627c030887302f75aafc8d76e228d906b29
- evidence_id: micro59-gene-CSM4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACSM4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:54.130761Z'
  support: supports
  summary: The exact reviewed CSM4 query for organism559292 returns only Q08955; primary
    name or declared synonym matches.
  snapshot_sha256: 91cf39eaf11b94b7c4ab3dc38a6537014481ff3265c217c4071faba85b08eae0
- evidence_id: micro59-protein-Q12366
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12366.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:48.737993Z'
  support: supports
  summary: Reviewed Q12366 identifies NDJ1 in taxon559292. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: 1b4c4671cb757e6c50185a1ac5574edafd58472828820f2409da90ba5f8610c2
- evidence_id: micro59-gene-NDJ1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANDJ1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:54.989917Z'
  support: supports
  summary: The exact reviewed NDJ1 query for organism559292 returns only Q12366; primary
    name or declared synonym matches.
  snapshot_sha256: aaefe9fbcae63fb3ba7347400ed38fb94d7107ddaf14d0f9c41d7648b586389b
- evidence_id: micro59-protein-P87245
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P87245.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:48.116385Z'
  support: supports
  summary: Reviewed P87245 identifies kms1 in taxon284812. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: 84aa928d02abba093e6be0c791d5d9f775268e8701d7955ab7f7d7cbb36eb234
- evidence_id: micro59-gene-kms1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Akms1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:55.255549Z'
  support: supports
  summary: The exact reviewed kms1 query for organism284812 returns only P87245; primary
    name or declared synonym matches.
  snapshot_sha256: 764b9bc53b3cd2e74bbdee8d0ee4220e19d2e6cd98ea33d8bd70a721459963ec
- evidence_id: micro59-tax284812
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Native taxId, scientificName, rank, lineage and relevant equivalent names.
  accessed_at: '2026-10-22T08:02:45.884915Z'
  support: supports
  summary: ENA taxId284812 identifies Schizosaccharomyces pombe 972h-, rank strain.
    Reference strains and experimental cultures are distinguished.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: micro59-tax4896
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: Native taxId, scientificName, rank, lineage and relevant equivalent names.
  accessed_at: '2026-10-22T08:02:45.940970Z'
  support: supports
  summary: ENA taxId4896 identifies Schizosaccharomyces pombe, rank species. Reference
    strains and experimental cultures are distinguished.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: micro59-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Native taxId, scientificName, rank, lineage and relevant equivalent names.
  accessed_at: '2026-10-22T08:02:45.971669Z'
  support: supports
  summary: ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. Reference
    strains and experimental cultures are distinguished.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro59-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Native taxId, scientificName, rank, lineage and relevant equivalent names.
  accessed_at: '2026-10-22T08:02:46.511505Z'
  support: supports
  summary: ENA taxId559292 identifies Saccharomyces cerevisiae S288C, rank strain.
    Reference strains and experimental cultures are distinguished.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro59-IPR031433
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031433/
  locator: Complete type/name/descriptions/member_databases; whole-family versus domain
    scope.
  accessed_at: '2026-10-22T08:02:56.093033Z'
  support: supports
  summary: IPR031433 is the Monopolar spindle protein 2 family. Native description
    and member signatures were read; protein accession membership is supplied separately
    by native UniProt evidence. Generic background mechanism is not treated as a new
    direct experiment.
  snapshot_sha256: b15cbfc3de00301ef03e60c6200cc2262c7f0ad6cc9f9b3368abda9f585cca58
- evidence_id: micro59-IPR039595
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039595/
  locator: Complete type/name/descriptions/member_databases; whole-family versus domain
    scope.
  accessed_at: '2026-10-22T08:02:56.096257Z'
  support: supports
  summary: IPR039595 is the TE2IP/Rap1 family. Native description and member signatures
    were read; protein accession membership is supplied separately by native UniProt
    evidence. Generic background mechanism is not treated as a new direct experiment.
  snapshot_sha256: 053a534a50641a078493fdda88cebfb892868b997eece9084e82527fb288e599
- evidence_id: micro59-IPR045119
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045119/
  locator: Complete type/name/descriptions/member_databases; whole-family versus domain
    scope.
  accessed_at: '2026-10-22T08:02:56.236251Z'
  support: supports
  summary: IPR045119 is the SUN domain-containing protein 1-5 family. Native description
    and member signatures were read; protein accession membership is supplied separately
    by native UniProt evidence. Generic background mechanism is not treated as a new
    direct experiment.
  snapshot_sha256: ebf2e470f10e591fe8475c39ac5142261438a51a9bba2571c0282d80a75d359e
- evidence_id: micro59-IPR062583
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062583/
  locator: Complete type/name/descriptions/member_databases; whole-family versus domain
    scope.
  accessed_at: '2026-10-22T08:02:56.732357Z'
  support: supports
  summary: IPR062583 is the Non-disjunction protein 1 family. Native description and
    member signatures were read; protein accession membership is supplied separately
    by native UniProt evidence. Generic background mechanism is not treated as a new
    direct experiment.
  snapshot_sha256: 2ec04da899f42036e20b7a5e57075ca24b3da21ba7908ceb57ec1277768ff044
- evidence_id: micro59-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228,GO:0000781,GO:0005634,GO:0032200,GO:0032993,GO:0034993,GO:0042910,GO:0045141,GO:0140330,GO:1902495,GO:1990203,GO:1990281,GO:1990612
  locator: Named exact native entries in this response, including GO0005634; identity,
    aspect, definition and relevant typed links. No universal synonymy of bouquet
    and LINC is inferred.
  accessed_at: '2026-10-22T08:02:45.199131Z'
  support: supports
  summary: The bouquet is a DNA-containing nuclear arrangement, fitting broader GO0032993;
    GO0045141 is the clustering process, not this structure. GO0034993 and GO1990612
    denote narrower LINC assemblies, while GO0000228/0000781 identify chromosomes/telomeric
    regions and GO0032200 telomere organization.
  snapshot_sha256: 9e094b28069fbc79cfeda88c524a5f4e8008c759ca9c3cf282ef6cb86f379f6e
- evidence_id: micro59-GO0032993-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032993/ancestors?relations=is_a
  locator: Complete exact requested-term is_a ancestor array and comment.
  accessed_at: '2026-10-22T08:02:45.199537Z'
  support: supports
  summary: The exact protein-DNA-complex term belongs to the protein-containing-complex
    hierarchy. Its comment requires DNA as a constituent, consistent with this chromosome-end
    arrangement.
  snapshot_sha256: 09794c71b65808a3a8c0254afb706809d2ba3443597d71cedbe31e18b244a59f
- evidence_id: micro59-SO0000624
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/so/terms?obo_id=SO:0000624
  locator: Complete exact SO term identity/definition/synonyms/active status.
  accessed_at: '2026-10-22T08:03:31.323716Z'
  support: supports
  summary: SO0000624 is the telomere sequence feature, with telomeric DNA/sequence
    synonyms; it denotes the chromosome-end DNA constituent, not the entire bouquet.
  snapshot_sha256: ad4789100ab24d513505fdfc30d62b29afc6a6fd381b0aadd6b656388579c49c
- evidence_id: micro59-bouquet-go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=bouquet&limit=25
  locator: Complete native QuickGO search response and original URL, limit25.
  accessed_at: '2026-10-22T08:05:25.368966Z'
  support: context_only
  summary: The bounded bouquet search returned the clustering biological process GO0045141.
    This search does not demonstrate exhaustive absence of a differently named cellular-component
    term.
  snapshot_sha256: 06baf59dd4f495aa1c5c2b6c9095b8ab66fb3093c82c50ccbb01143200f4c8b2
  search_scope: Remote QuickGO search for bouquet, limit25, one returned page. Ignored
    files do not apply to this remote query; no local or all-authority absence claim.
- evidence_id: micro59-fan2020-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7536833.1/PMC7536833.1.xml
  locator: 'Genuine original JATS: complete Introduction s1, Results s3–9, Discussion
    s10 and Methods s12–18, all embedded main/supplement captions; front permissions.
    Separate supplement files not read. Fig4 local pixels separately inspected.'
  accessed_at: '2026-10-21T09:25:46.268839Z'
  support: supports
  summary: Native SK1 meiotic localization/depletion experiments support Ndj1/Mps3-dependent
    Mps2 at chromosome ends, Mps2-dependent Csm4 localization and efficient bouquet
    clustering. Mps2/Csm4 perturbations affect pairing/recombination. S288C mitotic
    ectopic reconstitution is a separate context; the Discussion nonamer is speculative
    and is not exported as whole-bouquet stoichiometry.
  snapshot_sha256: 0013a1fcdd1d7b85b83d74900747997300119411c46cc5a932d59d25f75db9c0
- evidence_id: micro59-amelina2015-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4660835.1/PMC4660835.1.xml
  locator: 'Genuine original JATS: Results Sec4–6, Discussion Sec7, Methods Sec10–12/Sec15/Sec17,
    including Fig2–4 captions; front permissions. Other sections/supplement files
    not read. Fig4 local pixels separately inspected.'
  accessed_at: '2026-10-21T09:25:46.269721Z'
  support: supports
  summary: Rap1 phosphorylation increases across meiotic prophase, but tested phosphomimetic/nonphosphorylatable
    clusters retain bouquet behavior. DD337AA preserves telomeric localization yet
    disrupts Bqt1/2 interaction and clustering. These are mutation/interaction assays,
    not evidence that physiological bouquet release is driven by those two residues.
  snapshot_sha256: 928c024c3338595e5fe589c9d3c9174f03bdccf5c75eb89648eca6459a5d4112
- evidence_id: micro59-moiseeva2017-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5674143.1/PMC5674143.1.xml
  locator: 'Genuine original JATS: complete Introduction; Results titled Bouquet formation
    ensures entry into meiosis I, The telomere bouquet stabilises CDK1cyclin B at
    the SPB prior to its termination, and Premature termination of the bouquet leads
    to spindle defects; complete Discussion; Methods Strains and media, Microscope
    image acquisition, Auxin-inducible system. Other Results/Methods, movies and supplemental
    files not read.'
  accessed_at: '2026-10-21T09:27:43.695545Z'
  support: supports
  summary: The fission-yeast bouquet persists beyond horsetail oscillation. bqt1 deletion
    and conditional Bqt1-AID loss support continued chromosome-SPB association in
    timely CDK1/Cdc13 accumulation and spindle progression, with only subsets showing
    severe SPB failure. AID-induced loss is an experimental perturbation, not an identified
    physiological dissolution signal.
  snapshot_sha256: e5b2fc8c46775b2f6a9e0b176bb16d6f2bae801e78e90b191369414ca23f84a3
- evidence_id: micro59-csm2020-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7181386.1/PMC7181386.1.xml
  locator: 'Genuine original JATS: complete S3, S8 and Discussion S10; Methods S14/S19/S20.
    Other Results/Methods and supplement files not read.'
  accessed_at: '2026-10-21T09:25:46.270923Z'
  support: supports
  summary: Meiotic Mps2 localization/association supports a LINC link; Csm4 interacts
    with Mps2 and contributes to Myo2 localization, but this paper explicitly interprets
    Csm4 as an accessory regulator rather than structural LINC component. That interpretation
    differs from Fan2020 and is retained in the record rather than erased.
  snapshot_sha256: fc2ee1f306bcb93fb50bd1335c1a60bdd901b50f1ece7f7b1f8c63371a362c9a
- evidence_id: micro59-jimenez2025-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/PMC11747273.1.xml
  locator: 'Genuine original JATS: Results Sec8–11, complete Discussion Sec12, Methods
    Sec14/Sec17, embedded Fig6–9 captions. Earlier Results, other Methods, supplements
    and pixels not read.'
  accessed_at: '2026-10-21T08:24:58.921258Z'
  support: supports
  summary: Rabl-deficient mitotic cells with ectopic Bqt1/2 recruit selected telocentrosome
    factors and some telomeres reach the SPB, but do not form a complete ordinary
    bouquet and lack detected dynein. Separate diploid meiotic Ndc80-retention experiments
    constrain natural entry. Proposed Cdk1 recycling remains a mechanistic interpretation.
  snapshot_sha256: 1e0470a799e49976e35584be8e8449af77c2e85fd1e11576a460227cd526e4ed
- evidence_id: micro59-PXD001841
  kind: database
  reference: https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD001841
  locator: Complete project identity/title/description/sample and data protocols,
    submissionType, organism, instrument and publication; raw files not downloaded
    or reanalysed.
  accessed_at: '2026-10-22T08:02:56.880691Z'
  support: supports
  summary: PXD001841 is the PARTIAL S.pombe Rap1 phosphoproteomics deposit. Native
    description/protocols specify homozygous diploid pat1-114 cultures, 3.5/4.5h,
    Rap1-3xPK immunoprecipitation, LC-MS/MS and LTQ Orbitrap Velos; its linked publication
    is Amelina2015.
  snapshot_sha256: bd15f9f4750d759da3b7bb75782757892fc7edecd55dd3a3e4fdc020d2186c17
- evidence_id: micro59-ipr-matches-P79005
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P79005/
  locator: Complete results/count/next:null and metadata type/name for this accession
    only. No all-InterPro absence inference.
  accessed_at: '2026-10-22T08:05:24.469162Z'
  support: supports
  summary: The complete accession match set contains only domains or a broad homologous
    superfamily, not a verified exact whole-protein family for this named class.
  snapshot_sha256: b6dbbb9f425b8a989171d98dd4039de8257c295dedbd3d72f6ec7c215ca160d1
- evidence_id: micro59-ipr-matches-P87245
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P87245/
  locator: Complete results/count/next:null and metadata type/name for this accession
    only. No all-InterPro absence inference.
  accessed_at: '2026-10-22T08:05:25.249806Z'
  support: supports
  summary: The complete accession match set contains only domains or a broad homologous
    superfamily, not a verified exact whole-protein family for this named class.
  snapshot_sha256: fc2c3fa0cf4b315fd6bf85587320a1115d3db926b89531da051f9fd2c0f947b9
- evidence_id: micro59-ipr-protein-Q92358
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q92358/entry/interpro/
  locator: Actual HTTP204 status, empty-body SHA and exact endpoint.
  accessed_at: '2026-10-22T08:03:32.098502Z'
  support: context_only
  summary: The retained exact accession request returned HTTP204 and an empty body.
    It supplies no integrated match evidence; this bounded null does not prove biological
    absence or lack of all possible external family mappings.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro59-ipr-protein-Q9US52
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q9US52/entry/interpro/
  locator: Actual HTTP204 status, empty-body SHA and exact endpoint.
  accessed_at: '2026-10-22T08:03:33.511409Z'
  support: context_only
  summary: The retained exact accession request returned HTTP204 and an empty body.
    It supplies no integrated match evidence; this bounded null does not prove biological
    absence or lack of all possible external family mappings.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro59-ipr-protein-Q08955
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/protein/uniprot/Q08955/entry/interpro/
  locator: Actual HTTP204 status, empty-body SHA and exact endpoint.
  accessed_at: '2026-10-22T08:03:33.733155Z'
  support: context_only
  summary: The retained exact accession request returned HTTP204 and an empty body.
    It supplies no integrated match evidence; this bounded null does not prove biological
    absence or lack of all possible external family mappings.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro59-PMC7536833-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC7536833.1.json
  locator: Exact pmcid/doi/license_code and Fig4 media_urls MD5; not a claim that
    other package media were inspected.
  accessed_at: '2026-10-22T08:02:57.388089Z'
  support: supports
  summary: Native package metadata identifies the cited article and its Fig4 media;
    the deposited Fig4 MD5 matches the tracked local bytes. CC BY package status is
    refined to CC BY4.0 by the separately inspected article permissions.
  snapshot_sha256: 8693a7ef6e75d29e3b38111070a782cd8d9bac24623a1c66900dd781a36e9290
- evidence_id: image-7536833
  kind: record_content
  reference: data/images/other/meiotic_telomere_bouquet/pmc7536833_fig4.jpg
  locator: Entire tracked figure visually inspected; SHA256 940897253f430c6d6d5b4b80b1dca59d2a5b6db16a5bbfa4f3bb531dfc253b07
  accessed_at: '2026-10-22T08:10:29Z'
  support: context_only
  summary: Fig4 panel labels, microscopy channels, genotype/context and accompanying
    plots agree with the caption. Fan panelsA/B show clustering, C–E viability/recombination;
    AmelinaA is alignment, B asci, C mitotic colocalization, D meiotic time series.
    No raw pixel quantification was repeated.
- evidence_id: micro59-PMC4660835-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC4660835.1.json
  locator: Exact pmcid/doi/license_code and Fig4 media_urls MD5; not a claim that
    other package media were inspected.
  accessed_at: '2026-10-22T08:02:57.388415Z'
  support: supports
  summary: Native package metadata identifies the cited article and its Fig4 media;
    the deposited Fig4 MD5 matches the tracked local bytes. CC BY package status is
    refined to CC BY4.0 by the separately inspected article permissions.
  snapshot_sha256: 9c08ddafa09c974791b3435bf8cb5111d6b4b02fe766429b3d2c12f1e3788f7d
- evidence_id: image-4660835
  kind: record_content
  reference: data/images/other/meiotic_telomere_bouquet/pmc4660835_fig4.jpg
  locator: Entire tracked figure visually inspected; SHA256 c38253a30a2f55547b92f39c20ad0308a8ee450d1cf25af84dcc6659d5ac8ca4
  accessed_at: '2026-10-22T08:10:29Z'
  support: context_only
  summary: Fig4 panel labels, microscopy channels, genotype/context and accompanying
    plots agree with the caption. Fan panelsA/B show clustering, C–E viability/recombination;
    AmelinaA is alignment, B asci, C mitotic colocalization, D meiotic time series.
    No raw pixel quantification was repeated.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/meiotic_telomere_bouquet.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:58:00Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/meiotic_telomere_bouquet.yaml'
  snapshot_sha256: bd4322e42ab509e7128b2d6b7cc11361ce3d414545decbe498bdd45c4bc6f274
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/meiotic_telomere_bouquet.yaml
    --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/meiotic_telomere_bouquet-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:58:01Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/meiotic_telomere_bouquet.yaml\
    \ --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/meiotic_telomere_bouquet-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch59-20261022-t3ere5ku/meiotic_telomere_bouquet-strict.tsv"
  snapshot_sha256: 0b37257292290120a1a03e5ebfb12e64d0153af4a440568210386f503870da37
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/meiotic_telomere_bouquet.yaml
    --causal-graphs
  locator: Complete focused read-only native log
  accessed_at: '2026-10-22T08:04:29.549169Z'
  support: supports
  summary: "data/structures/other/meiotic_telomere_bouquet.yaml  (cellstructuremech:meiotic_telomere_bouquet)\n\
    \  budding_yeast_tether_assembly\tndj1\tCOVERED\t->ndj1 (UniProtKB:Q12366)\n \
    \ budding_yeast_tether_assembly\tmps3\tCOVERED\t->sun (UniProtKB:P47069, UniProtKB:Q09825)\n\
    \  budding_yeast_tether_assembly\tmps2\tCOVERED\t->mps2 (UniProtKB:P53159)\n \
    \ budding_yeast_tether_assembly\tcsm4\tCOVERED\t->csm4 (UniProtKB:Q08955)\n  fission_yeast_bouquet_maintenance\t\
    bqt1\tCOVERED\t->bqt1 (UniProtKB:Q92358)\n\ncausal_graphs GENE_OR_PROTEIN node\
    \ summary:\n     5  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref\
    \ on the node\n     5  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: a715c6bfb00ed0cb7cf96bf6279dd56c68d089639f1219e5cf4b9541bf59c523
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/meiotic_telomere_bouquet.yaml
    --verify
  locator: Complete focused read-only native log
  accessed_at: '2026-10-22T08:04:30.864677Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/meiotic_telomere_bouquet.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '34 of 35 collected target identifiers returned OK. cellstructuremech:meiotic_telomere_bouquet:
    SKIPPED; Exact local identifier uniquely resolves to this maintained target in
    the full data/structures YAML traversal, including ignored files. This proves
    local reference identity, not external ontology resolution. Native source checks
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
  topic: Whole polarized DNA/protein arrangement
  outcome: supported
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  summary: The local identity correctly distinguishes a meiotic chromosome-end arrangement
    from the clustering process, LINC subcomplexes, a generic nuclear rim or an ectopic
    partial telocentrosome. DNA is a constituent of the structure, supporting the
    protein-DNA-complex parent.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-go
  - micro59-GO0032993-ancestors
  - micro59-SO0000624
  - micro59-bouquet-go-search
  - micro59-fan2020-jats
  - micro59-moiseeva2017-jats
  - micro59-jimenez2025-jats
- assessment_id: grounding
  area: grounding
  topic: Ten classes and eleven protein examples
  outcome: supported
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  summary: Existing Rap1, SUN, Mps2 and Ndj1 families are supported by native class
    metadata and separate protein memberships, including both yeast Rap1 sequences.
    Taz1/Kms1 matches are only domains/superfamily; Bqt1/Bqt2/Csm4 bounded204 responses
    justify retaining the exact classes label-only. No guessed domain-to-whole-class
    substitution is proposed.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-IPR031433
  - micro59-IPR039595
  - micro59-IPR045119
  - micro59-IPR062583
  - micro59-ipr-matches-P79005
  - micro59-ipr-matches-P87245
  - micro59-ipr-protein-Q92358
  - micro59-ipr-protein-Q9US52
  - micro59-ipr-protein-Q08955
  - micro59-protein-P11938
  - micro59-protein-Q96TL7
  - micro59-protein-P79005
  - micro59-protein-Q92358
  - micro59-protein-Q9US52
  - micro59-protein-P47069
  - micro59-protein-Q09825
  - micro59-protein-P53159
  - micro59-protein-Q08955
  - micro59-protein-Q12366
  - micro59-protein-P87245
  - micro59-gene-RAP1-559292
  - micro59-gene-rap1-284812
  - micro59-gene-taz1
  - micro59-gene-bqt1
  - micro59-gene-bqt2
  - micro59-gene-MPS3
  - micro59-gene-sad1
  - micro59-gene-MPS2
  - micro59-gene-CSM4
  - micro59-gene-NDJ1
  - micro59-gene-kms1
- assessment_id: scope
  area: scope
  topic: Species, reference strains and experimental contexts
  outcome: supported
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  summary: Budding SK1 meiosis, S288C mitotic reconstitution, fission-yeast live meiosis/pat1
    synchronization and Rabl-deficient mitotic manipulations remain separate. This
    literature supports the curated yeast settings; the target has no taxonomic-distribution
    row and does not assert a population census.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-tax284812
  - micro59-tax4896
  - micro59-tax4932
  - micro59-tax559292
  - micro59-fan2020-jats
  - micro59-amelina2015-jats
  - micro59-moiseeva2017-jats
  - micro59-jimenez2025-jats
  - micro59-PXD001841
- assessment_id: formation
  area: evidence
  topic: Bounded positive dependencies do not require universal essentiality
  outcome: unknown
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  summary: Fan depletion/localization and Bqt1/Rap1 perturbations support the stated
    dependencies within their experimental contexts. All component UNKNOWN labels
    remain defensible for a cross-species structure without a universal per-component
    formation test. Maintenance, pairing, spindle progression and physical initial
    formation are not interchangeable.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-fan2020-jats
  - micro59-amelina2015-jats
  - micro59-moiseeva2017-jats
  - micro59-csm2020-jats
  - micro59-jimenez2025-jats
- assessment_id: graph
  area: graph
  topic: Two scoped causal models preserve conflicts and stages
  outcome: supported
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  summary: The budding assembly graph states tested localization/clustering dependencies
    without claiming fixed whole-bouquet stoichiometry. The fission graph addresses
    continued Bqt1-dependent linkage and timely prophase/spindle progression, preserving
    partial penetrance and artificial AID timing. Fan-versus-Lee Csm4 membership interpretations,
    Rap1 phosphomutant results and partial mitotic telocentrosomes remain explicit.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-fan2020-jats
  - micro59-amelina2015-jats
  - micro59-moiseeva2017-jats
  - micro59-csm2020-jats
  - micro59-jimenez2025-jats
- assessment_id: images
  area: evidence
  topic: Tracked figures, license and deposited experiment
  outcome: supported
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  summary: Both Fig4 files were visually inspected and match their exact source package
    MD5. Article permissions specify CC BY4.0; Amelina data CC0 wording does not replace
    its article/figure license. PRIDE identity and experimental metadata agree without
    raw-data reanalysis.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-fan2020-jats
  - micro59-amelina2015-jats
  - micro59-PXD001841
  - micro59-PMC7536833-package
  - image-7536833
  - micro59-PMC4660835-package
  - image-4660835
- assessment_id: coverage
  area: completeness
  topic: Entire maintained target with explicit source tiers
  outcome: supported
  target_ids:
  - cellstructuremech:meiotic_telomere_bouquet
  summary: Every target field, current discussion, graph, example and history entry
    was read. Existing named proteins and source IDs were checked. Optional absent
    detail alone is not treated as a defect; no maintained scientific content was
    changed.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-go
  - micro59-GO0032993-ancestors
  - micro59-SO0000624
  - micro59-bouquet-go-search
  - micro59-fan2020-jats
  - micro59-amelina2015-jats
  - micro59-moiseeva2017-jats
  - micro59-csm2020-jats
  - micro59-jimenez2025-jats
  - micro59-PXD001841
  - micro59-doi-10.1016_j.cell.2006.01.048
  - micro59-doi-10.1016_j.cub.2020.01.054
  - micro59-doi-10.1038_celldisc.2017.41
  - micro59-doi-10.1038_s41467-025-56049-9
  - micro59-doi-10.1186_s12915-015-0149-x
  - micro59-doi-10.26508_lsa.202000824
  - micro59-protein-P11938
  - micro59-protein-Q96TL7
  - micro59-protein-P79005
  - micro59-protein-Q92358
  - micro59-protein-Q9US52
  - micro59-protein-P47069
  - micro59-protein-Q09825
  - micro59-protein-P53159
  - micro59-protein-Q08955
  - micro59-protein-Q12366
  - micro59-protein-P87245
  - micro59-gene-RAP1-559292
  - micro59-gene-rap1-284812
  - micro59-gene-taz1
  - micro59-gene-bqt1
  - micro59-gene-bqt2
  - micro59-gene-MPS3
  - micro59-gene-sad1
  - micro59-gene-MPS2
  - micro59-gene-CSM4
  - micro59-gene-NDJ1
  - micro59-gene-kms1
  - micro59-tax284812
  - micro59-tax4896
  - micro59-tax4932
  - micro59-tax559292
  - micro59-IPR031433
  - micro59-IPR039595
  - micro59-IPR045119
  - micro59-IPR062583
  - micro59-ipr-matches-P79005
  - micro59-ipr-matches-P87245
  - micro59-ipr-protein-Q92358
  - micro59-ipr-protein-Q9US52
  - micro59-ipr-protein-Q08955
  - micro59-PMC7536833-package
  - image-7536833
  - micro59-PMC4660835-package
  - image-4660835
findings: []
actions: []
limitations:
- Only the exact primary sections and captions named in evidence were read. Chikashige2006
  was checked at complete native abstract tier only; no primary body or supplement
  access is implied. Other annotation papers remain uninspected.
- Only the two tracked Fig4 images were visually inspected. Separate supplemental
  files, movies and raw PRIDE data were not reanalysed; no microscopy quantification
  was independently reproduced.
- Family nulls are bounded accession responses, not exhaustive authority absence.
  The bouquet ontology search is a bounded candidate check, not proof that every possible
  cellular-component term was excluded.
- The eleven reviewed sequence examples are reference identities, not assertions that
  their exact reference strains supplied every experimental culture.
- Csm4 structural-versus-accessory LINC interpretations remain conflicting. Species-specific
  localization, formation and maintenance assays do not establish universal component
  necessity or a physiological bouquet-release trigger.
- Reused source bytes retain original URL, UTC and SHA256. HTTP status alone is not
  treated as evidence of article-body readability.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requests a review for every unreviewed record, including qualified
  clean cases.
- No maintained record, historical review or initial inspection snapshot is edited.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
