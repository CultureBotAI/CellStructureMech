# Chitosome identity, cargo and delivery-source audit

- Review: 20261021T110752Z-chitosome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:40:22Z
- Finished UTC: 2026-10-21T11:07:52Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Chitosome identity, bounded synthase cargo and regulated yeast delivery are supported. One minor current grounding gap is resolved by exact active GO0030661; no further concrete issue was found.

## Scope And Provenance

Entire exact target, all components/examples/functions, five graph edges, both discussions and exact-commit cross-corpus delivery relation.

Selection: Batch21 index6; one entire maintained record at frozen main9c0446.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0045009 | data/structures/membrane_organelle/chitosome.yaml | maintained | chitosome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native verify | passed | True | GO:0045009 | Focused native check passed. Read-only public-network retry resolved the preserved initial sandbox DNS failure. |
| Focused native causal-graphs | passed | True | GO:0045009 | Focused native check passed. |
| Focused native schema | passed | True | GO:0045009 | Focused validator passed. |
| Focused native strict | passed | True | GO:0045009 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0045009 | 14 identifiers OK; 4 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0045009 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0045009 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0045009 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0045009 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0045009 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0045009 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole vesicle, exact parent and membrane identity

identity: concern. Targets: GO:0045009.

The whole chitosome definition, membrane-bounded kind and cytoplasmic-vesicle parent are supported. The bilayer component has a now-verified exact GO term, contradicting the current open no-term rationale and leaving avoidable label-only grounding (F1).

### Constitutional boundary and enzyme cargo

evidence: supported. Targets: GO:0045009.

The collective lipid-bilayer boundary is constitutional to this membrane-bounded structure, supporting its collective ESSENTIAL label. The literature supports intracellular synthase cargo distinct from surface product. Chs1 biochemical fractionation and Chs3 trafficking are different assays and should not be collapsed into one universal activation pathway.

### Cargo membership versus organelle formation

evidence: unknown. Targets: GO:0045009.

The enzyme cohort correctly retains UNKNOWN formation necessity. Synthase activity, polarized targeting and transport-mutant phenotypes do not establish which individual synthase is necessary to form all fungal chitosomes. The collective membrane label does not identify a universally necessary lipid species.

### Taxon-paired examples and annotation provenance

evidence: supported. Targets: GO:0045009.

CHS1/P08004 and CHS3/P29465 are the uniquely reviewed examples for their exact genes in S288C. Their roles explicitly restrict them to identity evidence; the three P29465 PMIDs correctly identify Cell membrane annotations and are not falsely offered as chitosome-localization experiments.

### Fungal variability and Saccharomyces example

scope: supported. Targets: GO:0045009.

VARIABLE Fungi avoids unsupported universality. The canonical example accurately concerns Saccharomyces Chs6-dependent Chs3 traffic, not every isoenzyme or a generic fungal biogenesis machinery. Species-level exemplar and narrower S288C identifier/pathway scopes remain explicit.

### Storage, delivery and five coarse graph edges

graph: supported. Targets: GO:0045009.

All five edges retain the intended NONMECHANISTIC scale. The division-septum supply edge is proposed; Chs3 targeting is demonstrated in the particular yeast experiments. Chitin is the synthase product at the cell surface, not a resident native-vesicle component. In-vitro synthesis by isolated particles does not require a resident-polymer row.

### Exact-version delivery link and taxon boundary

evidence: supported. Targets: GO:0045009.

The declared PathwayMech object and full source commit resolve; CHS3 participates in its S288C chitin pathway. Separate Ziman trafficking evidence supports SUPPORTS_ENZYME_DELIVERY. The relation explicitly avoids intracellular chitosome synthesis or extending S288C pathway membership across Fungi.

### Current grounding TODO and bounded optional inventory

completeness: supported. Targets: GO:0045009.

Resolve the exact membrane term identified in F1. IPR004835 covers both protein examples but extends beyond the fungal cargo cohort; this limited candidate check does not force it as an exact whole-cohort mapping or prove no other exact family exists. Chs6, Chs5, exomer, particular lipids and detailed biogenesis intermediates are not required merely because sources discuss them. No record image or physical measurement requires separate validation.

### Contested origin and enzyme-activation scope

evidence: unknown. Targets: GO:0045009.

The2006 review disputes a general endocytic-origin account; the yeast paper discusses recycling and alternative transport models. The target does not settle origin and explicitly excludes activation-state claims for every fungal isoenzyme. This evidence supports the bounded storage/delivery model without a universal origin or activation mechanism.

## Findings

### F1: Ground the chitosome membrane to its exact active GO term

minor / open / confirmed; issue key: chitosome-exact-membrane-grounding.

The current component remains REVIEWED_LABEL_ONLY and the open grounding discussion says GO has no exact chitosome-membrane child. Native GO0045009 explicitly lists GO0030661 part_of, and native GO0030661 is chitosome membrane, defined as the lipid bilayer surrounding a chitosome. This is an exact match to the existing constituent, not a new optional inventory row. Ground the membrane component and update the active discussion accordingly while preserving historical curation notes and the separately unresolved fungal protein-cohort question.

## Recommended Actions And Acceptance Checks

### A1

Ground the existing bilayer component with GO0030661 and revise only the current membrane portion of the open grounding discussion.

- The component uses active GO:0030661 with the schema-supported grounding fields and compatible canonical label.
- The current discussion no longer says no exact chitosome-membrane term exists; the fungal synthase family question remains independently scoped.
- Preserve historical curation entries and the chitin product boundary; rerun focused schema, strict and identifier checks after any separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/chitosome.yaml; Entire YAML, both discussions, five graph edges and exact-version related-record link | context_only | The record distinguishes intracellular carriers from their cell-wall product, scopes its Saccharomyces example to Chs3 trafficking, and keeps the septum reservoir role proposed. |
| policy | docs/CURATION.md; Component grounding, assembly necessity and source-scope rubric | context_only | Known exact component identities should be grounded. Localization or catalytic activity does not establish necessity for organelle formation. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; NONMECHANISTIC source and scope rubric | context_only | A coarse storage/delivery graph may retain proposed targeting without claiming a fully intervened biogenesis mechanism. |
| protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Taxon-paired identity versus evidence for structural membership | context_only | A reviewed identifier example is distinct from experimentally established structure membership; native annotation evidence must preserve its actual compartment. |
| chitosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045009,GO:0031410,GO:0005886,GO:0030428; Complete requested term identity, definition and relevant child relations | supports | The four stated GO terms are active. GO0045009 has the exact chitosome definition, including proposed septum-directed transport; GO0031410 lists chitosome as an is_a child. The chitosome response lists GO0030661 as a part_of child. Cell septum and plasma membrane are correctly labeled graph destinations. No inference is drawn from the other returned child. |
| chitosome-agent-go-parts | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030661,GO:0033162; results entry id GO:0030661: name, isObsolete, definition and aspect; paired with GO0045009 part_of relation in go.raw | supports | Active GO0030661 is exactly chitosome membrane and is defined as the lipid bilayer surrounding a chitosome. This directly matches components[0] and resolves its current label-only grounding question. The other requested child was read for identity only and is not used as evidence about this record. |
| chitosome-agent-chebi17029 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17029; _embedded.terms[0]: obo_id, label, is_obsolete and description | supports | Active CHEBI17029 is chitin, an aminoglycan of beta-1,4-linked N-acetyl-D-glucosamine residues. It grounds the chemical output, not a resident vesicle component. |
| chitosome-agent-tax-4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; taxId/scientificName/rank/lineage/otherNames | supports | Native taxonomy identifies Fungi kingdom. Species and strain scopes are distinct; identity is not occurrence evidence. |
| chitosome-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId/scientificName/rank/lineage/otherNames | supports | Native taxonomy identifies Saccharomyces cerevisiae species. Species and strain scopes are distinct; identity is not occurrence evidence. |
| chitosome-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId/scientificName/rank/lineage/otherNames | supports | Native taxonomy identifies Saccharomyces cerevisiae S288C strain. Species and strain scopes are distinct; identity is not occurrence evidence. |
| chitosome-agent-bartnicki2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111%2Fj.1567-1364.2006.00158.x&amp;format=json&amp;resultType=core; resultList.result[0] citation/author/year and complete abstractText | supports | Exact citation and complete abstract read: PMID16981903, DOI10.1111/j.1567-1364.2006.00158.x, Chitosomes: past, present and future. Bartnicki-Garcia2006 is a review of chitosome history and unresolved biogenesis, not a new primary experiment. |
| chitosome-agent-leal1988-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073%2Fpnas.85.22.8516&amp;format=json&amp;resultType=core; resultList.result[0] citation/author/year and complete abstractText | supports | Exact citation and complete abstract read: PMID2973065, DOI10.1073/pnas.85.22.8516, Localization of chitin synthetase in cell-free homogenates of Saccharomyces cerevisiae: chitosomes and plasma membrane. The primary abstract reports two separated Saccharomyces synthase pools: low-density microvesicles and larger plasma-membrane vesicles, with chitin synthase1 activity and zymogenicity in both. |
| chitosome-agent-santos1997-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1083%2Fjcb.136.1.95&amp;format=json&amp;resultType=core; resultList.result[0] citation/author/year and complete abstractText | supports | Exact citation and complete abstract read: PMID9008706, DOI10.1083/jcb.136.1.95, Targeting of chitin synthase 3 to polarized growth sites in yeast requires Chs5p and Myo2p. The primary abstract links Chs3 polarized localization to Chs5 and Myo2 in Saccharomyces; it does not establish every fungal isoenzyme or a universal vesicle mechanism. |
| chitosome-agent-ziman1998-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.9.6.1565&amp;format=json&amp;resultType=core; resultList.result[0] citation/author/year and complete abstractText | supports | Exact citation and complete abstract read: PMID9614194, DOI10.1091/mbc.9.6.1565, Chs6p-dependent anterograde transport of Chs3p from the chitosome to the plasma membrane in Saccharomyces cerevisiae. The primary abstract establishes selective Chs6-dependent Chs3 transport to the plasma membrane, while Chs1 transport remains normal in the chs6 mutant. |
| chitosome-agent-bartnicki2006-pdf | https://www.davidmoore.org.uk/21st_Century_Guidebook_to_Fungi_PLATINUM/REPRINT_collection/Bartnicki-Garcia_chitosomes2006.pdf; Printed pp957–964 complete scientific prose through Conclusion, including Disruption artefacts and Endocytosis vesicles; figure captions read as text only. Reference list not exhaustively audited. | supports | This secondary review supports membrane-bounded microvesicles carrying latent synthase and the distinction between enzyme delivery and cell-wall product. It surveys fungal examples and disputes whether yeast recycling explains chitosome origin generally. Its in-vitro fibril formation and reassembly observations do not establish resident chitin in native vesicles or a universal in-vivo origin mechanism. |
| chitosome-agent-jats-PMC2132460 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132460.1/PMC2132460.1.xml; Results subsections Chs3p glycoprotein through myo2-66 mutants (six subsections, including embedded captions); Discussion selected Chs3/Chs5 and pheromone paragraphs plus complete Myo2p Is Required subsection; Methods strains, epitope tagging and indirect immunofluorescence. No figure pixels or supplementary/raw-data reanalysis. | supports | Epitope-tagged Saccharomyces Chs3 localizes to cytoplasmic patches and polarized growth sites. chs5 deletion and restrictive-temperature myo2-66 perturb polarized targeting; pheromone-treated cells provide a separate growth context. The Discussion allows alternative indirect Myo2 effects and does not prove direct motor binding. |
| chitosome-agent-ziman1998-browser-discussion | https://pmc.ncbi.nlm.nih.gov/articles/PMC25385/; Browser-captured primary Discussion: five paragraphs from chs6 transport defect through proposed regulated delivery model; mixed search output, unrelated hits not used. Native full-text routes were not readable bodies. | supports | The Discussion distinguishes impaired Chs3 surface delivery from retained in-vitro activity, selective Chs3 versus Chs1 transport, and alternative carrier models. It supports regulated delivery while leaving vesicle origin and coat mechanisms provisional. This is a browser capture, not a native HTTP200 full-text audit. |
| chitosome-agent-P08004 | https://rest.uniprot.org/uniprotkb/P08004.json; entryType/primaryAccession/proteinDescription/genes/organism; FUNCTION and SUBCELLULAR LOCATION comments and evidence references | supports | Reviewed P08004 identifies CHS1 in S288C tax559292. Recommended name, gene/locus and native FUNCTION/SUBCELLULAR LOCATION annotations were inspected. The identity-only example does not use this entry alone to prove chitosome membership. |
| chitosome-agent-P29465 | https://rest.uniprot.org/uniprotkb/P29465.json; entryType/primaryAccession/proteinDescription/genes/organism; FUNCTION and SUBCELLULAR LOCATION comments and evidence references | supports | Reviewed P29465 identifies CHS3 in S288C tax559292. Recommended name, gene/locus and native FUNCTION/SUBCELLULAR LOCATION annotations were inspected. The three recorded PMIDs are exactly ECO0000269 Cell membrane annotation sources; chitosome/vesicle statements and other compartments have distinct annotation scope. |
| chitosome-agent-reviewed-uniqueness | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+%28gene_exact%3ACHS1+OR+gene_exact%3ACHS3%29&amp;format=json&amp;size=500; Complete query results primaryAccession, entryType, genes, organism; response total/pagination headers | supports | The exact reviewed tax559292 query for gene_exact CHS1 or CHS3 returns two entries: P08004 and P29465 respectively. X-Total-Results is2; no next-page link is present. This establishes bounded reviewed uniqueness, not all fungal cargo membership. |
| chitosome-agent-PMID-12928491 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12928491+AND+SRC%3AMED&amp;format=json&amp;resultType=core; resultList.result[0] citation and complete abstractText | supports | Exact PMID, title, author/year and complete native abstract inspected. Valdivia and Schekman2003 reports stress-regulated Chs3 export from internal stores to the plasma membrane involving Rho1/Pkc1. Full body not independently audited here. |
| chitosome-agent-PMID-17519287 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17519287+AND+SRC%3AMED&amp;format=json&amp;resultType=core; resultList.result[0] citation and complete abstractText | supports | Exact PMID, title, author/year and complete native abstract inspected. Reyes2007 distinguishes Chs4-dependent stable active plasma-membrane Chs3 from intracellular localization, rapid endocytosis and inactive surface accumulation. Full body not independently audited here. |
| chitosome-agent-PMID-28346351 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28346351+AND+SRC%3AMED&amp;format=json&amp;resultType=core; resultList.result[0] citation and complete abstractText | supports | Exact PMID, title, author/year and complete native abstract inspected. Gohlke2017 reports Chs3 oligomers in bud-neck/lateral membrane and intracellular Golgi-derived vesicles, with topology analyses. Full body not independently audited here. |
| chitosome-agent-IPR004835 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004835/; metadata accession/name/type and complete curated description; member database scope | supports | IPR004835 is a chitin synthase family; its curated description includes fungal and animal enzymes. This is a broader candidate than the explicitly fungal cargo cohort and is not silently treated as an exact taxon-specific replacement. |
| chitosome-agent-ipr-matches-P08004 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P08004/?page_size=200; count/next and all result metadata accession/name/type | supports | The exact P08004 InterPro protein-match endpoint includes IPR004835; the other matches are domains/superfamily entries. Complete results have count3 and next:null. These are family memberships, not chitosome localization experiments. |
| chitosome-agent-ipr-matches-P29465 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P29465/?page_size=200; count/next and all result metadata accession/name/type | supports | The exact P29465 InterPro protein-match endpoint includes IPR004835; the other matches are domains/superfamily entries. Complete results have count3 and next:null. These are family memberships, not chitosome localization experiments. |
| pathway-exact-snapshot | PathwayMech@d8ec2b69f7a4c615aecddff80498fef1e1fab0ce:data/pathways/chitin-biosynthesis.yaml; git show exact declared commit; identifier, label, target taxon, CHS3 participant and enabled reaction. Source is an immutable local Git object, not a web HTTP response; full unrelated pathway mechanism not reaudited. | supports | The exact declared commit contains gomodel:YeastPathways_PWY3O-15, chitin biosynthesis, scoped to S288C tax559292. CHS3 is an explicit participant and enables chitin polymerization. Together with the separate trafficking source this supports the narrowly stated enzyme-delivery link; it does not move synthesis inside the chitosome. |
| native-verify | /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml --verify; Complete focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml --causal-graphs; Complete focused native output | supports | data/structures/membrane_organelle/chitosome.yaml  (GO:0045009)<br>  chitosome_chitin_synthase_delivery	fungal_chitin_synthases	COVERED	-&gt;fungal_chitin_synthases (UniProtKB:P08004, UniProtKB:P29465)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-verify-initial-failure | /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml --verify; Initial focused verifier log; subsequently resolved by native-verify | context_only | Initial exit1 was a sandbox DNS/network failure reaching UniProt, not a protein-identity mismatch. The original failure receipt and log remain retained; the subsequent identical read-only verifier passed0. |
| schema-result | just validate data/structures/membrane_organelle/chitosome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/chitosome.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/chitosome.yaml --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chitosome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/chitosome.yaml --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chitosome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chitosome-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/chitosome.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 14 of18 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:12928491: UNREACHABLE; resolved by evidence chitosome-agent-PMID-12928491; PMID:17519287: UNREACHABLE; resolved by evidence chitosome-agent-PMID-17519287; PMID:28346351: UNREACHABLE; resolved by evidence chitosome-agent-PMID-28346351; gomodel:YeastPathways_PWY3O-15: SKIPPED; resolved by evidence pathway-exact-snapshot. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Bartnicki-Garcia2006 was read as a secondary review, not primary experimental evidence. Its endocytic-origin disagreement and unresolved in-vivo integration/activation questions remain bounded; no universal biogenesis model is inferred.
- Leal-Morales1988 was checked through exact metadata and the complete primary abstract; canonical/legacy native HTML returned challenge pages, S3 was404 and EPMC XML500. No full-body or micrograph audit is claimed.
- Ziman1998 complete native abstract and a genuine browser-captured primary Discussion passage were inspected. Native full-text routes returned challenges/errors or403; Methods/Results body and figure pixels were not independently audited. Browser status:null denotes a capture, not HTTP200.
- Santos1997 genuine JATS was inspected at the specified Chs3 Results, selected Discussion and Methods sections; no raw microscopy, supplemental files or figure pixels were audited. The three P29465 annotation PMIDs were verified with native annotations and abstracts, not complete independent paper audits.
- The InterPro candidate check is limited to the two declared proteins and IPR004835. It is not a comprehensive search for all fungal synthase classes or proof of term absence. The exact membrane term was directly verified without inferring missing ontology terms from search silence.
- The PathwayMech check reads the exact immutable declared Git object for identity, taxon and CHS3 linkage, not the whole pathway mechanism. No local CellStructureMech sibling was used as scientific evidence.
- Initial native protein verification failed from sandbox DNS; its preserved log/receipt is superseded by a successful read-only public-network retry, not discarded.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110752Z-chitosome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Chitosome identity, cargo and delivery-source audit
started_at: '2026-10-21T10:40:22Z'
finished_at: '2026-10-21T11:07:52Z'
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
summary: Chitosome identity, bounded synthase cargo and regulated yeast delivery are
  supported. One minor current grounding gap is resolved by exact active GO0030661;
  no further concrete issue was found.
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
  - path: data/structures/membrane_organelle/chitosome.yaml
    sha256: 7233ef84787e4a164a1388fbb12643f34bfc28bf12272f6c0898868975376938
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
- target_id: GO:0045009
  path: data/structures/membrane_organelle/chitosome.yaml
  label: chitosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chitosome.yaml
    role: maintained scientific record
scope:
  description: Entire exact target, all components/examples/functions, five graph
    edges, both discussions and exact-commit cross-corpus delivery relation.
  selection: Batch21 index6; one entire maintained record at frozen main9c0446.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0045009
checks:
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0045009
  command: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed. Read-only public-network retry resolved the
    preserved initial sandbox DNS failure.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0045009
  command: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0045009
  command: just validate data/structures/membrane_organelle/chitosome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0045009
  command: just validate-strict data/structures/membrane_organelle/chitosome.yaml
    --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chitosome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0045009
  summary: 14 identifiers OK; 4 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - chitosome-agent-PMID-12928491
  - chitosome-agent-PMID-17519287
  - chitosome-agent-PMID-28346351
  - pathway-exact-snapshot
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0045009
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - protein-policy
  - chitosome-agent-go
  - chitosome-agent-go-parts
  - chitosome-agent-chebi17029
  - chitosome-agent-tax-4751
  - chitosome-agent-tax-4932
  - chitosome-agent-tax-559292
  - chitosome-agent-bartnicki2006-meta
  - chitosome-agent-leal1988-meta
  - chitosome-agent-santos1997-meta
  - chitosome-agent-ziman1998-meta
  - chitosome-agent-bartnicki2006-pdf
  - chitosome-agent-jats-PMC2132460
  - chitosome-agent-ziman1998-browser-discussion
  - chitosome-agent-P08004
  - chitosome-agent-P29465
  - chitosome-agent-reviewed-uniqueness
  - chitosome-agent-PMID-12928491
  - chitosome-agent-PMID-17519287
  - chitosome-agent-PMID-28346351
  - chitosome-agent-IPR004835
  - chitosome-agent-ipr-matches-P08004
  - chitosome-agent-ipr-matches-P29465
  - pathway-exact-snapshot
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0045009
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
  - GO:0045009
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
  - GO:0045009
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
  - GO:0045009
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
  - GO:0045009
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
  reference: data/structures/membrane_organelle/chitosome.yaml
  locator: Entire YAML, both discussions, five graph edges and exact-version related-record
    link
  accessed_at: '2026-10-21T10:53:48Z'
  support: context_only
  summary: The record distinguishes intracellular carriers from their cell-wall product,
    scopes its Saccharomyces example to Chs3 trafficking, and keeps the septum reservoir
    role proposed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding, assembly necessity and source-scope rubric
  accessed_at: '2026-10-21T10:53:48Z'
  support: context_only
  summary: Known exact component identities should be grounded. Localization or catalytic
    activity does not establish necessity for organelle formation.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: NONMECHANISTIC source and scope rubric
  accessed_at: '2026-10-21T10:53:48Z'
  support: context_only
  summary: A coarse storage/delivery graph may retain proposed targeting without claiming
    a fully intervened biogenesis mechanism.
- evidence_id: protein-policy
  kind: record_content
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Taxon-paired identity versus evidence for structural membership
  accessed_at: '2026-10-21T10:53:48Z'
  support: context_only
  summary: A reviewed identifier example is distinct from experimentally established
    structure membership; native annotation evidence must preserve its actual compartment.
- evidence_id: chitosome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045009,GO:0031410,GO:0005886,GO:0030428
  locator: Complete requested term identity, definition and relevant child relations
  accessed_at: '2026-10-21T10:44:32.350944Z'
  support: supports
  summary: The four stated GO terms are active. GO0045009 has the exact chitosome
    definition, including proposed septum-directed transport; GO0031410 lists chitosome
    as an is_a child. The chitosome response lists GO0030661 as a part_of child. Cell
    septum and plasma membrane are correctly labeled graph destinations. No inference
    is drawn from the other returned child.
  snapshot_sha256: 3a8c2319d7dcd662445edde2e22b70808dbe684e52a6c61eb52b0902fea873f9
- evidence_id: chitosome-agent-go-parts
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030661,GO:0033162
  locator: 'results entry id GO:0030661: name, isObsolete, definition and aspect;
    paired with GO0045009 part_of relation in go.raw'
  accessed_at: '2026-10-21T10:51:32.650448Z'
  support: supports
  summary: Active GO0030661 is exactly chitosome membrane and is defined as the lipid
    bilayer surrounding a chitosome. This directly matches components[0] and resolves
    its current label-only grounding question. The other requested child was read
    for identity only and is not used as evidence about this record.
  snapshot_sha256: e8c2ee2e0b71c77ecf3017af483e57a2825907545636b5502e65a05465b8e2df
- evidence_id: chitosome-agent-chebi17029
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17029
  locator: '_embedded.terms[0]: obo_id, label, is_obsolete and description'
  accessed_at: '2026-10-21T10:44:33.111500Z'
  support: supports
  summary: Active CHEBI17029 is chitin, an aminoglycan of beta-1,4-linked N-acetyl-D-glucosamine
    residues. It grounds the chemical output, not a resident vesicle component.
  snapshot_sha256: a246bef2108be925e56d8768f8c27c89aaede533a7fe4ba246aeed52355e658c
- evidence_id: chitosome-agent-tax-4751
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-21T10:44:32.478978Z'
  support: supports
  summary: Native taxonomy identifies Fungi kingdom. Species and strain scopes are
    distinct; identity is not occurrence evidence.
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: chitosome-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-21T10:44:32.481789Z'
  support: supports
  summary: Native taxonomy identifies Saccharomyces cerevisiae species. Species and
    strain scopes are distinct; identity is not occurrence evidence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: chitosome-agent-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-21T10:44:32.796749Z'
  support: supports
  summary: Native taxonomy identifies Saccharomyces cerevisiae S288C strain. Species
    and strain scopes are distinct; identity is not occurrence evidence.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: chitosome-agent-bartnicki2006-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111%2Fj.1567-1364.2006.00158.x&format=json&resultType=core
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T10:44:31.000059Z'
  support: supports
  summary: 'Exact citation and complete abstract read: PMID16981903, DOI10.1111/j.1567-1364.2006.00158.x,
    Chitosomes: past, present and future. Bartnicki-Garcia2006 is a review of chitosome
    history and unresolved biogenesis, not a new primary experiment.'
  snapshot_sha256: fc1d192c9581874e7353bf3ab5fc98be15ad59511905115df5683aae61cf31e2
- evidence_id: chitosome-agent-leal1988-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073%2Fpnas.85.22.8516&format=json&resultType=core
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T10:44:30.999717Z'
  support: supports
  summary: 'Exact citation and complete abstract read: PMID2973065, DOI10.1073/pnas.85.22.8516,
    Localization of chitin synthetase in cell-free homogenates of Saccharomyces cerevisiae:
    chitosomes and plasma membrane. The primary abstract reports two separated Saccharomyces
    synthase pools: low-density microvesicles and larger plasma-membrane vesicles,
    with chitin synthase1 activity and zymogenicity in both.'
  snapshot_sha256: 878b2f0e97931b07893d402419f3a588adc10a86dc788dec9d8a7cf6ebdd1b02
- evidence_id: chitosome-agent-santos1997-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1083%2Fjcb.136.1.95&format=json&resultType=core
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T10:44:31.001033Z'
  support: supports
  summary: 'Exact citation and complete abstract read: PMID9008706, DOI10.1083/jcb.136.1.95,
    Targeting of chitin synthase 3 to polarized growth sites in yeast requires Chs5p
    and Myo2p. The primary abstract links Chs3 polarized localization to Chs5 and
    Myo2 in Saccharomyces; it does not establish every fungal isoenzyme or a universal
    vesicle mechanism.'
  snapshot_sha256: 4d5928e943ea9dc3246f38ff0162f87efa85a2326cc00d595649a42f4c5a7129
- evidence_id: chitosome-agent-ziman1998-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.9.6.1565&format=json&resultType=core
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T10:44:31.000780Z'
  support: supports
  summary: 'Exact citation and complete abstract read: PMID9614194, DOI10.1091/mbc.9.6.1565,
    Chs6p-dependent anterograde transport of Chs3p from the chitosome to the plasma
    membrane in Saccharomyces cerevisiae. The primary abstract establishes selective
    Chs6-dependent Chs3 transport to the plasma membrane, while Chs1 transport remains
    normal in the chs6 mutant.'
  snapshot_sha256: 6b38932ccc4ba371a67de5121b2b6d5a2ee899cb07cfce518fd68086d8e810e2
- evidence_id: chitosome-agent-bartnicki2006-pdf
  kind: authority
  reference: https://www.davidmoore.org.uk/21st_Century_Guidebook_to_Fungi_PLATINUM/REPRINT_collection/Bartnicki-Garcia_chitosomes2006.pdf
  locator: Printed pp957–964 complete scientific prose through Conclusion, including
    Disruption artefacts and Endocytosis vesicles; figure captions read as text only.
    Reference list not exhaustively audited.
  accessed_at: '2026-10-21T10:45:58.269057Z'
  support: supports
  summary: This secondary review supports membrane-bounded microvesicles carrying
    latent synthase and the distinction between enzyme delivery and cell-wall product.
    It surveys fungal examples and disputes whether yeast recycling explains chitosome
    origin generally. Its in-vitro fibril formation and reassembly observations do
    not establish resident chitin in native vesicles or a universal in-vivo origin
    mechanism.
  snapshot_sha256: e8071dd556203864ae1d31963e73c344a2bf9f3f210d8bf8bb6f3a958def993d
- evidence_id: chitosome-agent-jats-PMC2132460
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132460.1/PMC2132460.1.xml
  locator: Results subsections Chs3p glycoprotein through myo2-66 mutants (six subsections,
    including embedded captions); Discussion selected Chs3/Chs5 and pheromone paragraphs
    plus complete Myo2p Is Required subsection; Methods strains, epitope tagging and
    indirect immunofluorescence. No figure pixels or supplementary/raw-data reanalysis.
  accessed_at: '2026-10-21T10:45:06.272466Z'
  support: supports
  summary: Epitope-tagged Saccharomyces Chs3 localizes to cytoplasmic patches and
    polarized growth sites. chs5 deletion and restrictive-temperature myo2-66 perturb
    polarized targeting; pheromone-treated cells provide a separate growth context.
    The Discussion allows alternative indirect Myo2 effects and does not prove direct
    motor binding.
  snapshot_sha256: ac284c0c2cf5124a2fa5947b7405732415ed0d657f35be8a943f3eb2211a0112
- evidence_id: chitosome-agent-ziman1998-browser-discussion
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC25385/
  locator: 'Browser-captured primary Discussion: five paragraphs from chs6 transport
    defect through proposed regulated delivery model; mixed search output, unrelated
    hits not used. Native full-text routes were not readable bodies.'
  accessed_at: '2026-10-21T10:48:38.227347Z'
  support: supports
  summary: The Discussion distinguishes impaired Chs3 surface delivery from retained
    in-vitro activity, selective Chs3 versus Chs1 transport, and alternative carrier
    models. It supports regulated delivery while leaving vesicle origin and coat mechanisms
    provisional. This is a browser capture, not a native HTTP200 full-text audit.
  snapshot_sha256: 754bc55e12e999b1e6ef96db8d58b82e291ee8f35ef1a89e7a06466d1700dc31
- evidence_id: chitosome-agent-P08004
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P08004.json
  locator: entryType/primaryAccession/proteinDescription/genes/organism; FUNCTION
    and SUBCELLULAR LOCATION comments and evidence references
  accessed_at: '2026-10-21T10:44:32.948412Z'
  support: supports
  summary: Reviewed P08004 identifies CHS1 in S288C tax559292. Recommended name, gene/locus
    and native FUNCTION/SUBCELLULAR LOCATION annotations were inspected. The identity-only
    example does not use this entry alone to prove chitosome membership.
  snapshot_sha256: a2d134e2e1ca0e5fa1e6ffcc0cbabfd557544af36d14a885afde32238ed3e763
- evidence_id: chitosome-agent-P29465
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P29465.json
  locator: entryType/primaryAccession/proteinDescription/genes/organism; FUNCTION
    and SUBCELLULAR LOCATION comments and evidence references
  accessed_at: '2026-10-21T10:44:32.971949Z'
  support: supports
  summary: Reviewed P29465 identifies CHS3 in S288C tax559292. Recommended name, gene/locus
    and native FUNCTION/SUBCELLULAR LOCATION annotations were inspected. The three
    recorded PMIDs are exactly ECO0000269 Cell membrane annotation sources; chitosome/vesicle
    statements and other compartments have distinct annotation scope.
  snapshot_sha256: 63f91ca6bb09dd735b34f1430f55a85d5a0ba4c48ba7d2b31e76e02187dda1a0
- evidence_id: chitosome-agent-reviewed-uniqueness
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+%28gene_exact%3ACHS1+OR+gene_exact%3ACHS3%29&format=json&size=500
  locator: Complete query results primaryAccession, entryType, genes, organism; response
    total/pagination headers
  accessed_at: '2026-10-21T10:44:33.015170Z'
  support: supports
  summary: 'The exact reviewed tax559292 query for gene_exact CHS1 or CHS3 returns
    two entries: P08004 and P29465 respectively. X-Total-Results is2; no next-page
    link is present. This establishes bounded reviewed uniqueness, not all fungal
    cargo membership.'
  snapshot_sha256: 576c4d50fc66040e399deb527cd60a1693c1897e7b3a511d05d5b697beffdf94
- evidence_id: chitosome-agent-PMID-12928491
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12928491+AND+SRC%3AMED&format=json&resultType=core
  locator: resultList.result[0] citation and complete abstractText
  accessed_at: '2026-10-21T10:44:31.002323Z'
  support: supports
  summary: Exact PMID, title, author/year and complete native abstract inspected.
    Valdivia and Schekman2003 reports stress-regulated Chs3 export from internal stores
    to the plasma membrane involving Rho1/Pkc1. Full body not independently audited
    here.
  snapshot_sha256: ae5d47b4803a450ee25cd07f8a5b8b18b5f7afd306a9cf1f25a9bd361522e651
- evidence_id: chitosome-agent-PMID-17519287
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17519287+AND+SRC%3AMED&format=json&resultType=core
  locator: resultList.result[0] citation and complete abstractText
  accessed_at: '2026-10-21T10:44:32.128006Z'
  support: supports
  summary: Exact PMID, title, author/year and complete native abstract inspected.
    Reyes2007 distinguishes Chs4-dependent stable active plasma-membrane Chs3 from
    intracellular localization, rapid endocytosis and inactive surface accumulation.
    Full body not independently audited here.
  snapshot_sha256: 834e16478cb586a2df18db7e9f98107748bf37246cbda12ed08a833d17e44cac
- evidence_id: chitosome-agent-PMID-28346351
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28346351+AND+SRC%3AMED&format=json&resultType=core
  locator: resultList.result[0] citation and complete abstractText
  accessed_at: '2026-10-21T10:44:32.274119Z'
  support: supports
  summary: Exact PMID, title, author/year and complete native abstract inspected.
    Gohlke2017 reports Chs3 oligomers in bud-neck/lateral membrane and intracellular
    Golgi-derived vesicles, with topology analyses. Full body not independently audited
    here.
  snapshot_sha256: 53da0c9455b41b03d1185f5b2513f4cec3f6ee7c7f24c3f8e495808d8622168c
- evidence_id: chitosome-agent-IPR004835
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004835/
  locator: metadata accession/name/type and complete curated description; member database
    scope
  accessed_at: '2026-10-21T10:45:06.744489Z'
  support: supports
  summary: IPR004835 is a chitin synthase family; its curated description includes
    fungal and animal enzymes. This is a broader candidate than the explicitly fungal
    cargo cohort and is not silently treated as an exact taxon-specific replacement.
  snapshot_sha256: 4ea95627f5806df27f8e91b2a42796b48fa75c88915491138530003e40425061
- evidence_id: chitosome-agent-ipr-matches-P08004
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P08004/?page_size=200
  locator: count/next and all result metadata accession/name/type
  accessed_at: '2026-10-21T10:44:32.968799Z'
  support: supports
  summary: The exact P08004 InterPro protein-match endpoint includes IPR004835; the
    other matches are domains/superfamily entries. Complete results have count3 and
    next:null. These are family memberships, not chitosome localization experiments.
  snapshot_sha256: 2fb845200fde3b061a28ed9a023cf60beab2e1a47a3228f2c6e64122dd147b8e
- evidence_id: chitosome-agent-ipr-matches-P29465
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P29465/?page_size=200
  locator: count/next and all result metadata accession/name/type
  accessed_at: '2026-10-21T10:44:33.012050Z'
  support: supports
  summary: The exact P29465 InterPro protein-match endpoint includes IPR004835; the
    other matches are domains/superfamily entries. Complete results have count3 and
    next:null. These are family memberships, not chitosome localization experiments.
  snapshot_sha256: 1851ce85abaea603ab3695517705aaebded413c0df291bd74c1b6b461427616c
- evidence_id: pathway-exact-snapshot
  kind: database
  reference: PathwayMech@d8ec2b69f7a4c615aecddff80498fef1e1fab0ce:data/pathways/chitin-biosynthesis.yaml
  locator: git show exact declared commit; identifier, label, target taxon, CHS3 participant
    and enabled reaction. Source is an immutable local Git object, not a web HTTP
    response; full unrelated pathway mechanism not reaudited.
  accessed_at: '2026-10-21T10:45:59.759705Z'
  support: supports
  summary: The exact declared commit contains gomodel:YeastPathways_PWY3O-15, chitin
    biosynthesis, scoped to S288C tax559292. CHS3 is an explicit participant and enables
    chitin polymerization. Together with the separate trafficking source this supports
    the narrowly stated enzyme-delivery link; it does not move synthesis inside the
    chitosome.
  snapshot_sha256: d02205589a895098dc0a361cd0134f3075895103db2db82f21a1e36d56572a1a
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml
    --verify
  locator: Complete focused native output
  accessed_at: '2026-10-21T10:48:38.631333Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml
    --causal-graphs
  locator: Complete focused native output
  accessed_at: '2026-10-21T10:47:10.886877Z'
  support: supports
  summary: "data/structures/membrane_organelle/chitosome.yaml  (GO:0045009)\n  chitosome_chitin_synthase_delivery\t\
    fungal_chitin_synthases\tCOVERED\t->fungal_chitin_synthases (UniProtKB:P08004,\
    \ UniProtKB:P29465)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     1\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 4e39579edbac102eb474e951a3f5210ea7d1bbe4ce137cc84e38915fca388d63
- evidence_id: native-verify-initial-failure
  kind: validation
  reference: /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml
    --verify
  locator: Initial focused verifier log; subsequently resolved by native-verify
  accessed_at: '2026-10-21T10:47:08.970500Z'
  support: context_only
  summary: Initial exit1 was a sandbox DNS/network failure reaching UniProt, not a
    protein-identity mismatch. The original failure receipt and log remain retained;
    the subsequent identical read-only verifier passed0.
  snapshot_sha256: ead217e8c19470642cc6f11ec35daf23e7e3a769c10770ed75d0513133e3150d
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/chitosome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:40:25Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/chitosome.yaml'
  snapshot_sha256: b68c3a8bd4e692c376c4a1f174704656461f85a092fe4e11a08634580601c81f
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/chitosome.yaml
    --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chitosome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:40:28Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/chitosome.yaml\
    \ --out /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chitosome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch21-20261021-jc4u1a6u/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch21-20261021-jc4u1a6u/chitosome-strict.tsv"
  snapshot_sha256: 599a3480e87fbc69e42f32224f1e94f13391db272472d3af56da31dda2b39653
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/chitosome.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:53:48Z'
  support: supports
  summary: '14 of18 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:12928491: UNREACHABLE; resolved by evidence chitosome-agent-PMID-12928491;
    PMID:17519287: UNREACHABLE; resolved by evidence chitosome-agent-PMID-17519287;
    PMID:28346351: UNREACHABLE; resolved by evidence chitosome-agent-PMID-28346351;
    gomodel:YeastPathways_PWY3O-15: SKIPPED; resolved by evidence pathway-exact-snapshot.
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
  topic: Whole vesicle, exact parent and membrane identity
  outcome: concern
  target_ids:
  - GO:0045009
  summary: The whole chitosome definition, membrane-bounded kind and cytoplasmic-vesicle
    parent are supported. The bilayer component has a now-verified exact GO term,
    contradicting the current open no-term rationale and leaving avoidable label-only
    grounding (F1).
  evidence_ids:
  - record
  - chitosome-agent-go
  - chitosome-agent-go-parts
- assessment_id: composition
  area: evidence
  topic: Constitutional boundary and enzyme cargo
  outcome: supported
  target_ids:
  - GO:0045009
  summary: The collective lipid-bilayer boundary is constitutional to this membrane-bounded
    structure, supporting its collective ESSENTIAL label. The literature supports
    intracellular synthase cargo distinct from surface product. Chs1 biochemical fractionation
    and Chs3 trafficking are different assays and should not be collapsed into one
    universal activation pathway.
  evidence_ids:
  - record
  - chitosome-agent-go
  - chitosome-agent-leal1988-meta
  - chitosome-agent-bartnicki2006-pdf
  - chitosome-agent-ziman1998-meta
  - chitosome-agent-jats-PMC2132460
- assessment_id: assembly-necessity
  area: evidence
  topic: Cargo membership versus organelle formation
  outcome: unknown
  target_ids:
  - GO:0045009
  summary: The enzyme cohort correctly retains UNKNOWN formation necessity. Synthase
    activity, polarized targeting and transport-mutant phenotypes do not establish
    which individual synthase is necessary to form all fungal chitosomes. The collective
    membrane label does not identify a universally necessary lipid species.
  evidence_ids:
  - record
  - policy
  - chitosome-agent-bartnicki2006-pdf
  - chitosome-agent-jats-PMC2132460
  - chitosome-agent-ziman1998-meta
- assessment_id: protein-identity
  area: evidence
  topic: Taxon-paired examples and annotation provenance
  outcome: supported
  target_ids:
  - GO:0045009
  summary: CHS1/P08004 and CHS3/P29465 are the uniquely reviewed examples for their
    exact genes in S288C. Their roles explicitly restrict them to identity evidence;
    the three P29465 PMIDs correctly identify Cell membrane annotations and are not
    falsely offered as chitosome-localization experiments.
  evidence_ids:
  - record
  - protein-policy
  - chitosome-agent-reviewed-uniqueness
  - chitosome-agent-P08004
  - chitosome-agent-P29465
  - chitosome-agent-PMID-12928491
  - chitosome-agent-PMID-17519287
  - chitosome-agent-PMID-28346351
- assessment_id: taxon
  area: scope
  topic: Fungal variability and Saccharomyces example
  outcome: supported
  target_ids:
  - GO:0045009
  summary: VARIABLE Fungi avoids unsupported universality. The canonical example accurately
    concerns Saccharomyces Chs6-dependent Chs3 traffic, not every isoenzyme or a generic
    fungal biogenesis machinery. Species-level exemplar and narrower S288C identifier/pathway
    scopes remain explicit.
  evidence_ids:
  - record
  - chitosome-agent-bartnicki2006-pdf
  - chitosome-agent-ziman1998-meta
  - chitosome-agent-ziman1998-browser-discussion
  - chitosome-agent-tax-4751
  - chitosome-agent-tax-4932
  - chitosome-agent-tax-559292
- assessment_id: functions-graph
  area: graph
  topic: Storage, delivery and five coarse graph edges
  outcome: supported
  target_ids:
  - GO:0045009
  summary: All five edges retain the intended NONMECHANISTIC scale. The division-septum
    supply edge is proposed; Chs3 targeting is demonstrated in the particular yeast
    experiments. Chitin is the synthase product at the cell surface, not a resident
    native-vesicle component. In-vitro synthesis by isolated particles does not require
    a resident-polymer row.
  evidence_ids:
  - record
  - graph-policy
  - chitosome-agent-go
  - chitosome-agent-chebi17029
  - chitosome-agent-bartnicki2006-pdf
  - chitosome-agent-jats-PMC2132460
  - chitosome-agent-ziman1998-meta
  - chitosome-agent-ziman1998-browser-discussion
- assessment_id: pathway
  area: evidence
  topic: Exact-version delivery link and taxon boundary
  outcome: supported
  target_ids:
  - GO:0045009
  summary: The declared PathwayMech object and full source commit resolve; CHS3 participates
    in its S288C chitin pathway. Separate Ziman trafficking evidence supports SUPPORTS_ENZYME_DELIVERY.
    The relation explicitly avoids intracellular chitosome synthesis or extending
    S288C pathway membership across Fungi.
  evidence_ids:
  - record
  - pathway-exact-snapshot
  - chitosome-agent-ziman1998-meta
- assessment_id: completeness
  area: completeness
  topic: Current grounding TODO and bounded optional inventory
  outcome: supported
  target_ids:
  - GO:0045009
  summary: Resolve the exact membrane term identified in F1. IPR004835 covers both
    protein examples but extends beyond the fungal cargo cohort; this limited candidate
    check does not force it as an exact whole-cohort mapping or prove no other exact
    family exists. Chs6, Chs5, exomer, particular lipids and detailed biogenesis intermediates
    are not required merely because sources discuss them. No record image or physical
    measurement requires separate validation.
  evidence_ids:
  - record
  - policy
  - chitosome-agent-go-parts
  - chitosome-agent-IPR004835
  - chitosome-agent-ipr-matches-P08004
  - chitosome-agent-ipr-matches-P29465
- assessment_id: origin-limits
  area: evidence
  topic: Contested origin and enzyme-activation scope
  outcome: unknown
  target_ids:
  - GO:0045009
  summary: The2006 review disputes a general endocytic-origin account; the yeast paper
    discusses recycling and alternative transport models. The target does not settle
    origin and explicitly excludes activation-state claims for every fungal isoenzyme.
    This evidence supports the bounded storage/delivery model without a universal
    origin or activation mechanism.
  evidence_ids:
  - record
  - chitosome-agent-bartnicki2006-pdf
  - chitosome-agent-ziman1998-browser-discussion
findings:
- finding_id: F1
  issue_key: chitosome-exact-membrane-grounding
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the chitosome membrane to its exact active GO term
  description: The current component remains REVIEWED_LABEL_ONLY and the open grounding
    discussion says GO has no exact chitosome-membrane child. Native GO0045009 explicitly
    lists GO0030661 part_of, and native GO0030661 is chitosome membrane, defined as
    the lipid bilayer surrounding a chitosome. This is an exact match to the existing
    constituent, not a new optional inventory row. Ground the membrane component and
    update the active discussion accordingly while preserving historical curation
    notes and the separately unresolved fungal protein-cohort question.
  target_ids:
  - GO:0045009
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - components[0].grounding
  - discussions[0].prompt
  - discussions[0].rationale
  evidence_ids:
  - record
  - policy
  - chitosome-agent-go
  - chitosome-agent-go-parts
  normalization_reason: 'Minor: the membrane identity and scientific role are already
    correct; the concrete defect is avoidable missing exact grounding and a stale
    open no-term rationale.'
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chitosome.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Ground the existing bilayer component with GO0030661 and revise only
    the current membrane portion of the open grounding discussion.
  finding_ids:
  - F1
  target_ids:
  - GO:0045009
  acceptance_checks:
  - The component uses active GO:0030661 with the schema-supported grounding fields
    and compatible canonical label.
  - The current discussion no longer says no exact chitosome-membrane term exists;
    the fungal synthase family question remains independently scoped.
  - Preserve historical curation entries and the chitin product boundary; rerun focused
    schema, strict and identifier checks after any separately authorized curation.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chitosome.yaml
    role: maintained scientific record
limitations:
- Bartnicki-Garcia2006 was read as a secondary review, not primary experimental evidence.
  Its endocytic-origin disagreement and unresolved in-vivo integration/activation
  questions remain bounded; no universal biogenesis model is inferred.
- Leal-Morales1988 was checked through exact metadata and the complete primary abstract;
  canonical/legacy native HTML returned challenge pages, S3 was404 and EPMC XML500.
  No full-body or micrograph audit is claimed.
- Ziman1998 complete native abstract and a genuine browser-captured primary Discussion
  passage were inspected. Native full-text routes returned challenges/errors or403;
  Methods/Results body and figure pixels were not independently audited. Browser status:null
  denotes a capture, not HTTP200.
- Santos1997 genuine JATS was inspected at the specified Chs3 Results, selected Discussion
  and Methods sections; no raw microscopy, supplemental files or figure pixels were
  audited. The three P29465 annotation PMIDs were verified with native annotations
  and abstracts, not complete independent paper audits.
- The InterPro candidate check is limited to the two declared proteins and IPR004835.
  It is not a comprehensive search for all fungal synthase classes or proof of term
  absence. The exact membrane term was directly verified without inferring missing
  ontology terms from search silence.
- The PathwayMech check reads the exact immutable declared Git object for identity,
  taxon and CHS3 linkage, not the whole pathway mechanism. No local CellStructureMech
  sibling was used as scientific evidence.
- Initial native protein verification failed from sandbox DNS; its preserved log/receipt
  is superseded by a successful read-only public-network retry, not discarded.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
