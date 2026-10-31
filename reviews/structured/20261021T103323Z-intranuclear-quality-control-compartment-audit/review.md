# INQ identity, conditional deposition and clearance evidence review

- Review: 20261021T103323Z-intranuclear-quality-control-compartment-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:13:19Z
- Finished UTC: 2026-10-21T10:33:23Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete issue observed. Nuclear identity, conditional aggregation and reporter-specific clearance claims match the cited primary evidence with their stated boundaries.

## Scope And Provenance

Entire exact INQ record: identity, broader parents/parthood, four components and their protein/family/taxon examples, two functions, both six-edge graphs, discussions/status and hosted Figure3.

Selection: Batch19 index5; entire exact maintained record reviewed individually at frozen main9c0446.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:intranuclear_quality_control_compartment | data/structures/inclusion/intranuclear_quality_control_compartment.yaml | maintained | intranuclear quality control compartment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| native-verify | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Focused native check passed; biological claims assessed separately. |
| native-causal-graphs | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Focused native check passed; biological claims assessed separately. |
| Expression-module applicability | not_applicable | False | cellstructuremech:intranuclear_quality_control_compartment | No expression-module or transcriptomic mechanism claim; localization and perturbation are the relevant evidence types. |
| Focused native schema | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:intranuclear_quality_control_compartment | 12 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | cellstructuremech:intranuclear_quality_control_compartment | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Nuclear inclusion with distinct JUNQ and stress-granule boundaries

identity: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

The proposed local identifier, definition, class and kind denote a discrete membraneless nuclear inclusion. Nuclear body and inclusion body are broader is-a classes; nucleus is parthood. Gallina and Sontag support separation from cytoplasmic JUNQ, while Miller historical reinterpretation is explicitly acknowledged. GO0097165 is a distinct RNA/protein stress-granule class; shared stress context does not establish exact identity.

### Variable cargo, localized aggregase and associated disaggregase

evidence: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

The four component classes preserve direct localization versus function: heterogeneous cargo, INQ-enriched Btn2, associated Hsp104 and conditionally recruited Cmr1-family example. Engineered VHL/LuciTs do not define native composition. Partial CCT/proteasome/APC recruitment and genetic effects of transport/ESCRT factors do not justify fixed whole-complex membership. Hsp42-NLS rescue does not establish native Hsp42 residence.

### Assay-bounded conditional assembly and dispensability

evidence: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Btn2 CONDITIONAL is supported by deletion blocking tested nuclear deposition and engineered Hsp42-NLS substitution. Cmr1 DISPENSABLE is bounded by the explicitly stated Mrc1-focus readout: Mrc1 foci still form without Cmr1. This is not a claim that Cmr1 is dispensable for every INQ function or stress phenotype.

### Unresolved native cargo and Hsp104 assembly requirements

evidence: unknown. Targets: cellstructuremech:intranuclear_quality_control_compartment.

The heterogeneous cargo and associated Hsp104 classes retain UNKNOWN for formation or assembly necessity. Deposited cargo is constitutional material, but this does not establish a requirement for particular native cargo species. Hsp104 localization and inhibitor-sensitive recovery concern association or turnover, not demonstrated necessity for initial INQ assembly.

### Verified reference identities and non-exact family candidates

grounding: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

All three reviewed proteins, names, gene/locus tokens and tax559292 match the record and each exact gene query returns one result. Btn2 has only an integrated N-terminal domain match; Hsp104 matches broader ClpA/B families. Q12510 belongs to the exact family label used for its abstract component, with localization restricted to the yeast example. The unchecked LLM family description supplies no mechanism.

### Experimental species and reference strains remain separate

scope: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

The species-level canonical example is supported. Gallina primarily uses RAD5 W303 derivatives and S288C screening libraries with exceptions; Miller defers strain genotypes to supplements, and Sontag live-cell Methods name BY4741 while the full strain list is supplementary. The S288C protein examples explicitly establish reference identities rather than reassigning every experiment. No broad taxonomic distribution is inferred.

### Sequestration and condition-specific clearance

evidence: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Sequestration is observed, but Miller reporter degradation is unchanged when deposition is impaired, whereas Gallina links Btn2 loss to reduced Mrc1 turnover. These substrate/assay differences are retained. Sontag supports a vacuolar route for tested nuclear reporters with proteasomal processing in parallel, without proving the fate of every endogenous client or universal stress protection.

### Six bounded intervention edges

graph: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

NLS-LuciTs heat misfolding induces nuclear inclusions in Sontag; Miller Btn2 deletion impairs deposition and engineered nuclear Hsp42 restores it. Gallina MMS induces Cmr1 foci, while BTN2 and HSP42 deletions reduce that particular readout. These separate reporter/genotoxic-stress assays are not collapsed into one temporal pathway or universal Hsp42 requirement.

### Six positioning and delivery edges

graph: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Sontag supports convergence across the envelope without fusion, conditional vacuolar delivery, NVJ1/VAC8-dependent clearance, a CHM7-sensitive convergence phenotype and VPS4-sensitive clearance. Initial formation and convergence remain distinct from delivery. Directed genetic and imaging results justify MECHANISTIC scope while precise molecular tethers and membrane-budding steps remain models.

### Hosted Gallina Fig3 with exact native licence

provenance: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

The tracked image SHA9d15de2925ec7ada38d8b7281ed62110c4073fee15b464ed548b87b3687b1ecb and native package MD5 match. JATS explicitly gives CC BY4.0. Caption, image panels and microscopy scale/context agree with the curator description; the multi-panel image is not represented as a universal inventory. Sontag TDM metadata is not used as hosting permission.

### No forced inventory or material-state additions

completeness: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

The source-bounded discussions preserve native-client uncertainty, lack of universal dimensions/stoichiometry, incomplete supplemental strain mapping, and absence of direct evidence equating human WDR76 foci to yeast INQ. Q-body/JUNQ liquid-like interpretation is not transferred to INQ. No concrete required representation or unsupported claim was found.

### Source tiers, stable ownership and status

provenance: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

All cited main primary sources are readable through the actual captured bodies, with exact read scopes above. Historical notes about uninspected supplements remain historical and are not findings. The local identity self-references resolve to the inspected target. PROPOSED status, maintained ownership and history remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/inclusion/intranuclear_quality_control_compartment.yaml; Entire maintained YAML, all components/functions/graphs/discussions/image/history | context_only | The local identity denotes a stress-induced yeast nuclear inclusion, preserving differences between original JUNQ reinterpretation and later nuclear/cytoplasmic compartment discrimination. It explicitly limits components and interventions to tested substrates and conditions. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Scope and completion; primary intervention evidence | context_only | Directed experimental effects can support a mechanistic graph, while inferred molecular tethers, native constituents and assembly necessity require separate evidence. |
| inq-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016604,GO:0016234,GO:0005634,GO:0097165; All four results: id/name/aspect/isObsolete/definition; classes and location are assessed separately | supports | Four native active terms are returned: GO0016604 nuclear body is a membraneless nucleoplasmic organelle; GO0016234 inclusion body is an intracellular aggregate; GO0005634 is nucleus; GO0097165 nuclear stress granule includes proteins and RNAs. The first two provide broader classes and nucleus provides parthood; none is treated as exact INQ identity. |
| inq-agent-go-search-0 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=INQ&amp;limit=100&amp;page=1; Native query response, counts and returned labels | supports | The INQ acronym search returns zero hits. |
| inq-agent-go-search-1 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=intranuclear+quality+control&amp;limit=100&amp;page=1; Native query response, counts and returned labels | supports | All89 returned labels were inspected; related quality-control processes, ER quality-control compartment and intranuclear rod do not denote this nuclear inclusion. |
| inq-agent-ols-exact | https://www.ebi.ac.uk/ols4/api/search?q=intranuclear+quality+control+compartment&amp;ontology=go&amp;exact=true&amp;rows=100; Native query response, counts and returned labels | supports | Native exact GO search for the full name returns numFound0; this supports retaining the local identifier within the inspected scope. |
| inq-agent-P53286 | https://rest.uniprot.org/uniprotkb/P53286.json; primaryAccession, entryType, proteinDescription, genes and organism | supports | P53286 is reviewed Protein BTN2, gene BTN2/YGR142W, at tax559292. This establishes the reference protein identity, not INQ residence or reassignment of every experiment to S288C. |
| inq-agent-query-BTN2 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ABTN2&amp;format=json&amp;size=500; results: one accession with native genes and organism | supports | The exact reviewed BTN2 query returns one native entry, P53286, with matching gene/locus and tax559292. |
| inq-agent-P31539 | https://rest.uniprot.org/uniprotkb/P31539.json; primaryAccession, entryType, proteinDescription, genes and organism | supports | P31539 is reviewed Heat shock protein104, gene HSP104/YLL026W, at tax559292. This establishes the reference protein identity, not INQ residence or reassignment of every experiment to S288C. |
| inq-agent-query-HSP104 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP104&amp;format=json&amp;size=500; results: one accession with native genes and organism | supports | The exact reviewed HSP104 query returns one native entry, P31539, with matching gene/locus and tax559292. |
| inq-agent-Q12510 | https://rest.uniprot.org/uniprotkb/Q12510.json; primaryAccession, entryType, proteinDescription, genes and organism | supports | Q12510 is reviewed DNA damage-binding protein CMR1, gene CMR1/YDL156W, at tax559292. This establishes the reference protein identity, not INQ residence or reassignment of every experiment to S288C. |
| inq-agent-query-CMR1 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ACMR1&amp;format=json&amp;size=500; results: one accession with native genes and organism | supports | The exact reviewed CMR1 query returns one native entry, Q12510, with matching gene/locus and tax559292. |
| inq-agent-interpro-P53286 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P53286/?page_size=200; count1/next=null/results.metadata and P53286 membership | supports | The complete single integrated match is IPR062150 BTN2-like N-terminal domain, type domain, next=null. It does not identify an exact integrated whole-protein Btn2 family. |
| inq-agent-interpro-P31539 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200; count11/next=null; all result metadata accession/name/type and P31539 membership | supports | The complete11-match set has next=null. Family entries IPR001270 and IPR050130 are ClpA/B classes broader than Hsp104; remaining entries are domains, sites or superfamilies. |
| inq-agent-interpro-Q12510 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12510/?page_size=200; count5/next=null; all metadata and Q12510 protein membership | supports | The complete five-match set has next=null and includes family IPR050853 alongside WD40 repeat/site/superfamily entries. This proves the Q12510 family membership, not localization of every family member to INQ. |
| inq-agent-IPR050853 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050853/; metadata accession/type/name/member_databases/hierarchy; description flags and is_llm/is_reviewed_llm | supports | Native IPR050853 is the family WD repeat-containing DNA damage-binding protein, integrated with PANTHER PTHR14773. Its description is explicitly llm=true and checked=false; no mechanistic claim is derived from that text. |
| inq-agent-taxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank, lineage | supports | Native taxonomy identifies Saccharomyces cerevisiae at species rank; identity and lineage only. |
| inq-agent-taxon-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId, scientificName, rank, lineage | supports | Native taxonomy identifies Saccharomyces cerevisiae S288C at strain rank; identity and lineage only. |
| inq-agent-miller2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.15252%2Fembj.201489524&amp;format=json&amp;resultType=core; resultList.result[0]: id/doi/pmcid/title/authorString/pubYear/abstractText | supports | Native metadata identifies Compartment-specific aggregases direct distinct nuclear and cytoplasmic aggregate deposition. by Miller SB, Ho CT, Winkler J, Khokhrina M, Neuner A, Mohamed MY, Guilbride DL, Richter K, Lisby M, Schiebel E, Mogk A, Bukau B. PMID25672362, DOI10.15252/embj.201489524. Bibliographic identity and abstract; primary body evidence is separately hashed. |
| inq-agent-gallina2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fncomms7533&amp;format=json&amp;resultType=core; resultList.result[0]: id/doi/pmcid/title/authorString/pubYear/abstractText | supports | Native metadata identifies Cmr1/WDR76 defines a nuclear genotoxic stress body linking genome integrity and protein quality control. by Gallina I, Colding C, Henriksen P, Beli P, Nakamura K, Offman J, Mathiasen DP, Silva S, Hoffmann E, Groth A, Choudhary C, Lisby M. PMID25817432, DOI10.1038/ncomms7533. Bibliographic identity and abstract; primary body evidence is separately hashed. |
| inq-agent-sontag2023-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41556-023-01128-6&amp;format=json&amp;resultType=core; resultList.result[0]: id/doi/pmcid/title/authorString/pubYear/abstractText | supports | Native metadata identifies Nuclear and cytoplasmic spatial protein quality control is coordinated by nuclear-vacuolar junctions and perinuclear ESCRT. by Sontag EM, Morales-Polanco F, Chen JH, McDermott G, Dolan PT, Gestaut D, Le Gros MA, Larabell C, Frydman J. PMID37081164, DOI10.1038/s41556-023-01128-6. Bibliographic identity and abstract; primary body evidence is separately hashed. |
| inq-agent-miller2015-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC4369314/?report=xml; Genuine PMC4369314 native HTML; Results sec3–9, Discussion sec10, initial Methods sec12–13; derived paragraph indices36–89 and91–97 read, including Fig1–8 captions. SupplementaryS6 and strain tables not independently read; figure pixels not inspected. | supports | Direct primary fluorescence and immunogold microscopy establish nuclear reporter/Hsp104 deposits. Btn2 loss blocks tested nuclear aggregation without blocking nuclear import; engineered Hsp42-NLS restores aggregation. Reporter degradation during recovery is similar despite impaired deposition. Hsp104-inhibition stabilization is reported in main Results with a SupplementaryS6 pointer. The article reinterprets earlier JUNQ as INQ, a historical interpretation preserved rather than imposed on later sources. |
| inq-agent-gallina2015-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4389229.1/PMC4389229.1.xml; PMC4389229.1 JATS Results titled Cmr1 marks an intranuclear quality control compartment and Btn2 promotes Mrc1 turnover and relocalization to INQ; full Discussion; Methods Yeast strains and cell culture; entire Fig3 caption. Front permissions/license explicitly CC BY4.0. Tracked Fig3 pixels are separately inspected local evidence. | supports | Direct primary Cmr1 imaging and genetic tests distinguish strictly nuclear INQ from cytoplasmic VHL foci. Cmr1 is stable rather than proven misfolded cargo; Mrc1 and Cmr1 focus formation are independent of each other. Btn2/Hsp42 dependencies vary with cargo and stress. Rpn11 and Cct6 overlap is partial, and genome-maintenance phenotypes are not proven direct consequences of INQ loss. Methods specify RAD5 W303 derivatives by default with S288C libraries and exceptions. |
| inq-agent-sontag2023-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC12349969.1/PMC12349969.1.xml; PMC12349969.1 author-manuscript JATS Results S1–S8 and Discussion S9 read in full; Methods S12,S13,S18,S19,S31,S35; Data availability S46; Fig1,3,5–8 captions. Actual image pixels, supplementary strain table, videos and raw data not independently analyzed. | supports | Direct primary nuclear-targeted LuciTs/VHL experiments distinguish INQ and cytoplasmic JUNQ. NLS-LuciTs forms INQ with or without MG132. Both inclusions form after CHM7 loss but a subset fails to converge; NVJ loss preserves initial convergence while disrupting clearance and permitting cytoplasmic egress. VPS4 loss preserves deposits and impairs delivery. Keima acidification, protease perturbations, reporter fragments and imaging support a vacuolar route alongside proteasomal clearance, while exact budding/tether steps remain proposed. Some imaging panels explicitly use MG132. |
| inq-agent-gallina2015-package | https://pmc-oa-opendata.s3.amazonaws.com/PMC4389229.1/PMC4389229.1.json; pmcid/version/doi/pmid/is_pmc_openaccess/license_code; media_urls ncomms7533-f3.jpg MD5 | supports | Native PMC4389229 version1 package identifies DOI/PMID, open-access flag and CC BY label. Fig3 media MD5 is378de78d4843fa8e28e8207b2664dc51, equal to the tracked image. Exact licence version is supported separately by JATS. |
| inq-agent-sontag2023-package | https://pmc-oa-opendata.s3.amazonaws.com/PMC12349969.1/PMC12349969.1.json; pmcid/version/doi/pmid/mid/is_manuscript/is_pmc_openaccess/license_code | supports | Native PMC12349969 version1 is an author manuscript, NIHMS2091077, DOI10.1038/s41556-023-01128-6, PMID37081164. Package flags is_pmc_openaccess=false and license_code=TDM. Public readable JATS does not establish Creative Commons permission to host figures. |
| image | data/images/inclusion/intranuclear_quality_control_compartment/pmc4389229_f3.jpg; Entire Fig3 visual inspection, panelsa–g; tracked SHA and native media MD5 comparison | context_only | Panelsd/e distinguish nuclear Cmr1/VHL overlap from cytoplasmic VHL; panelf explicitly shows MMS and partial Cct6/Cmr1 overlap. Other panels contain screening, deletion frequencies and blots. Figure-specific caption gives2μm scales, IG66 andIG111; no separate third-party credit appears in caption or pixels. |
| native-verify | /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/intranuclear_quality_control_compartment.yaml --verify; Captured focused native log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/intranuclear_quality_control_compartment.yaml --causal-graphs; Captured focused native log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/inclusion/intranuclear_quality_control_compartment.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/inclusion/intranuclear_quality_control_compartment.yaml |
| strict-result | just validate-strict data/structures/inclusion/intranuclear_quality_control_compartment.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/intranuclear_quality_control_compartment-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/inclusion/intranuclear_quality_control_compartment.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/intranuclear_quality_control_compartment-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/intranuclear_quality_control_compartment-strict.tsv |
| target-curies | just check-curies-strict; data/structures/inclusion/intranuclear_quality_control_compartment.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 12 of13 collected target identifiers returned OK in this fresh base resolver run. Residuals: cellstructuremech:intranuclear_quality_control_compartment: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Native identity searches are bounded to the exact named/acronym queries described; local identity is not a claim of exhaustive absence from every ontology or repository.
- Miller main Results/Discussion and initial Methods, Gallina named INQ/Mrc1 Results/full Discussion/strain Methods, and Sontag S1–S9 plus relevant Methods/captions were read. Only tracked Gallina Fig3 pixels were independently inspected; supplementary strain tables, supporting figures/videos and raw datasets were not reanalyzed.
- Assembly necessity is experimentally supported only within the stated Btn2 and Mrc1-focus assays. Unknown Hsp104/cargo necessity and precise membrane-budding or tether mechanisms remain unknown.
- Sontag is a genuine public author-manuscript body with TDM metadata, not evidence of a Creative Commons image-hosting licence. Native protein examples establish identity separately from membership and experimental strain provenance.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- User-directed batch review explicitly requests an unsaved review for clean records as well as issue-bearing records; no finding is manufactured.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103323Z-intranuclear-quality-control-compartment-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: INQ identity, conditional deposition and clearance evidence review
started_at: '2026-10-21T10:13:19Z'
finished_at: '2026-10-21T10:33:23Z'
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
summary: No concrete issue observed. Nuclear identity, conditional aggregation and
  reporter-specific clearance claims match the cited primary evidence with their stated
  boundaries.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
  state: working_tree
  inputs:
  - path: .claude/skills/curate-causal-graphs/SKILL.md
    sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
    role: context
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: efb5aa79a0016ae7f1e53e40a9f5789930d152686ea6467aefce0928f7d1900f
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
  - path: data/images/inclusion/intranuclear_quality_control_compartment/pmc4389229_f3.jpg
    sha256: 9d15de2925ec7ada38d8b7281ed62110c4073fee15b464ed548b87b3687b1ecb
    role: context
  - path: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    sha256: 7e6cc3b1915d2093b6712f349dea34cad79831f2d4b93f0eaff29351b37f3c36
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
- target_id: cellstructuremech:intranuclear_quality_control_compartment
  path: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
  label: intranuclear quality control compartment
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    role: maintained scientific record
scope:
  description: 'Entire exact INQ record: identity, broader parents/parthood, four
    components and their protein/family/taxon examples, two functions, both six-edge
    graphs, discussions/status and hosted Figure3.'
  selection: Batch19 index5; entire exact maintained record reviewed individually
    at frozen main9c0446.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
checks:
- check_id: native-verify
  name: native-verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  command: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; biological claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: native-causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  command: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; biological claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: No expression-module or transcriptomic mechanism claim; localization and
    perturbation are the relevant evidence types.
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  command: just validate data/structures/inclusion/intranuclear_quality_control_compartment.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  command: just validate-strict data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/intranuclear_quality_control_compartment-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: 12 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - record
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - graph-policy
  - inq-agent-go
  - inq-agent-go-search-0
  - inq-agent-go-search-1
  - inq-agent-ols-exact
  - inq-agent-P53286
  - inq-agent-query-BTN2
  - inq-agent-P31539
  - inq-agent-query-HSP104
  - inq-agent-Q12510
  - inq-agent-query-CMR1
  - inq-agent-interpro-P53286
  - inq-agent-interpro-P31539
  - inq-agent-interpro-Q12510
  - inq-agent-IPR050853
  - inq-agent-taxon-4932
  - inq-agent-taxon-559292
  - inq-agent-miller2015-meta
  - inq-agent-gallina2015-meta
  - inq-agent-sontag2023-meta
  - inq-agent-miller2015-pmc
  - inq-agent-gallina2015-jats
  - inq-agent-sontag2023-jats
  - inq-agent-gallina2015-package
  - inq-agent-sontag2023-package
  - image
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
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
  - cellstructuremech:intranuclear_quality_control_compartment
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
  - cellstructuremech:intranuclear_quality_control_compartment
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
  - cellstructuremech:intranuclear_quality_control_compartment
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
  - cellstructuremech:intranuclear_quality_control_compartment
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
  reference: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
  locator: Entire maintained YAML, all components/functions/graphs/discussions/image/history
  accessed_at: '2026-10-21T10:22:06Z'
  support: context_only
  summary: The local identity denotes a stress-induced yeast nuclear inclusion, preserving
    differences between original JUNQ reinterpretation and later nuclear/cytoplasmic
    compartment discrimination. It explicitly limits components and interventions
    to tested substrates and conditions.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope and completion; primary intervention evidence
  accessed_at: '2026-10-21T10:22:06Z'
  support: context_only
  summary: Directed experimental effects can support a mechanistic graph, while inferred
    molecular tethers, native constituents and assembly necessity require separate
    evidence.
- evidence_id: inq-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016604,GO:0016234,GO:0005634,GO:0097165
  locator: 'All four results: id/name/aspect/isObsolete/definition; classes and location
    are assessed separately'
  accessed_at: '2026-10-21T10:16:27.161871Z'
  support: supports
  summary: 'Four native active terms are returned: GO0016604 nuclear body is a membraneless
    nucleoplasmic organelle; GO0016234 inclusion body is an intracellular aggregate;
    GO0005634 is nucleus; GO0097165 nuclear stress granule includes proteins and RNAs.
    The first two provide broader classes and nucleus provides parthood; none is treated
    as exact INQ identity.'
  snapshot_sha256: 6fad49bdc72bf568b34cb2973957faf8be1273852c41d8e4b2c4cf55beda0f24
- evidence_id: inq-agent-go-search-0
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=INQ&limit=100&page=1
  locator: Native query response, counts and returned labels
  accessed_at: '2026-10-21T10:18:12.720609Z'
  support: supports
  summary: The INQ acronym search returns zero hits.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: QuickGO query INQ, page1 limit100; numberOfHits0, complete zero-result
    response.
- evidence_id: inq-agent-go-search-1
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=intranuclear+quality+control&limit=100&page=1
  locator: Native query response, counts and returned labels
  accessed_at: '2026-10-21T10:18:12.721132Z'
  support: supports
  summary: All89 returned labels were inspected; related quality-control processes,
    ER quality-control compartment and intranuclear rod do not denote this nuclear
    inclusion.
  snapshot_sha256: c383e6530c470a4464b3c00bd16cbc3a63ca40e1f1915e20acdd4a1b5b0f1b80
  search_scope: QuickGO query intranuclear quality control, page1 limit100;89hits,
    onepage, all returned labels inspected.
- evidence_id: inq-agent-ols-exact
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?q=intranuclear+quality+control+compartment&ontology=go&exact=true&rows=100
  locator: Native query response, counts and returned labels
  accessed_at: '2026-10-21T10:18:38.347666Z'
  support: supports
  summary: Native exact GO search for the full name returns numFound0; this supports
    retaining the local identifier within the inspected scope.
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  search_scope: OLS4 ontology=go, exact=true, q=intranuclear quality control compartment,
    rows100; zero matches, no pagination.
- evidence_id: inq-agent-P53286
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53286.json
  locator: primaryAccession, entryType, proteinDescription, genes and organism
  accessed_at: '2026-10-21T10:16:27.877044Z'
  support: supports
  summary: P53286 is reviewed Protein BTN2, gene BTN2/YGR142W, at tax559292. This
    establishes the reference protein identity, not INQ residence or reassignment
    of every experiment to S288C.
  snapshot_sha256: d0122a2554484d191dfb1e8f702aeaca61392ab658f762dbc30916c27580c110
- evidence_id: inq-agent-query-BTN2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ABTN2&format=json&size=500
  locator: 'results: one accession with native genes and organism'
  accessed_at: '2026-10-21T10:16:27.881968Z'
  support: supports
  summary: The exact reviewed BTN2 query returns one native entry, P53286, with matching
    gene/locus and tax559292.
  snapshot_sha256: b2f4bdbd062bb47911a6c781f0eeb60f29e4558d1e1772e425012e87471f5159
  search_scope: UniProtKB reviewed:true AND organism_id:559292 AND gene_exact:BTN2,
    size500; one result, no pagination needed.
- evidence_id: inq-agent-P31539
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P31539.json
  locator: primaryAccession, entryType, proteinDescription, genes and organism
  accessed_at: '2026-10-21T10:16:27.163517Z'
  support: supports
  summary: P31539 is reviewed Heat shock protein104, gene HSP104/YLL026W, at tax559292.
    This establishes the reference protein identity, not INQ residence or reassignment
    of every experiment to S288C.
  snapshot_sha256: 8636decea760cdb2a2da238bfa589822867a778a41fd6a04c45a74fe5802ee13
- evidence_id: inq-agent-query-HSP104
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP104&format=json&size=500
  locator: 'results: one accession with native genes and organism'
  accessed_at: '2026-10-21T10:16:27.163895Z'
  support: supports
  summary: The exact reviewed HSP104 query returns one native entry, P31539, with
    matching gene/locus and tax559292.
  snapshot_sha256: 4e2938a5a1292a9626b18e30b225ebfc7a30d63069235f01cd0bc3d007279322
  search_scope: UniProtKB reviewed:true AND organism_id:559292 AND gene_exact:HSP104,
    size500; one result, no pagination needed.
- evidence_id: inq-agent-Q12510
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12510.json
  locator: primaryAccession, entryType, proteinDescription, genes and organism
  accessed_at: '2026-10-21T10:16:28.187586Z'
  support: supports
  summary: Q12510 is reviewed DNA damage-binding protein CMR1, gene CMR1/YDL156W,
    at tax559292. This establishes the reference protein identity, not INQ residence
    or reassignment of every experiment to S288C.
  snapshot_sha256: 1239def629e5b6dff77c2943d8e36218cb3b65349df792cd534d1accb4e6c126
- evidence_id: inq-agent-query-CMR1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ACMR1&format=json&size=500
  locator: 'results: one accession with native genes and organism'
  accessed_at: '2026-10-21T10:16:28.520514Z'
  support: supports
  summary: The exact reviewed CMR1 query returns one native entry, Q12510, with matching
    gene/locus and tax559292.
  snapshot_sha256: 44046a9911dff52899aa764915540f9310dbfcd4465e52a163db7d7ccab21fec
  search_scope: UniProtKB reviewed:true AND organism_id:559292 AND gene_exact:CMR1,
    size500; one result, no pagination needed.
- evidence_id: inq-agent-interpro-P53286
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P53286/?page_size=200
  locator: count1/next=null/results.metadata and P53286 membership
  accessed_at: '2026-10-21T10:16:28.014916Z'
  support: supports
  summary: The complete single integrated match is IPR062150 BTN2-like N-terminal
    domain, type domain, next=null. It does not identify an exact integrated whole-protein
    Btn2 family.
  snapshot_sha256: 2150123692223413fbe5ca58407117f0775384d53d6c3c9d16f7af500dbea6ab
- evidence_id: inq-agent-interpro-P31539
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200
  locator: count11/next=null; all result metadata accession/name/type and P31539 membership
  accessed_at: '2026-10-21T10:16:27.867842Z'
  support: supports
  summary: The complete11-match set has next=null. Family entries IPR001270 and IPR050130
    are ClpA/B classes broader than Hsp104; remaining entries are domains, sites or
    superfamilies.
  snapshot_sha256: 750867aa538d4dd5c6c6a982138e7401b8b788d9653ecb84bf5d145c8ff6d3ee
- evidence_id: inq-agent-interpro-Q12510
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12510/?page_size=200
  locator: count5/next=null; all metadata and Q12510 protein membership
  accessed_at: '2026-10-21T10:16:28.695592Z'
  support: supports
  summary: The complete five-match set has next=null and includes family IPR050853
    alongside WD40 repeat/site/superfamily entries. This proves the Q12510 family
    membership, not localization of every family member to INQ.
  snapshot_sha256: 53626d2b59f132b8d9318a1ffbfa366ed96077f4955e5793ac029eb6e052e610
- evidence_id: inq-agent-IPR050853
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050853/
  locator: metadata accession/type/name/member_databases/hierarchy; description flags
    and is_llm/is_reviewed_llm
  accessed_at: '2026-10-21T10:16:28.791293Z'
  support: supports
  summary: Native IPR050853 is the family WD repeat-containing DNA damage-binding
    protein, integrated with PANTHER PTHR14773. Its description is explicitly llm=true
    and checked=false; no mechanistic claim is derived from that text.
  snapshot_sha256: ea066ab30aab6f2701eebcb4ece6aeabf81226bd0203014ff051b7247895f686
- evidence_id: inq-agent-taxon-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank, lineage
  accessed_at: '2026-10-21T10:16:27.162305Z'
  support: supports
  summary: Native taxonomy identifies Saccharomyces cerevisiae at species rank; identity
    and lineage only.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: inq-agent-taxon-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId, scientificName, rank, lineage
  accessed_at: '2026-10-21T10:16:27.162591Z'
  support: supports
  summary: Native taxonomy identifies Saccharomyces cerevisiae S288C at strain rank;
    identity and lineage only.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: inq-agent-miller2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.15252%2Fembj.201489524&format=json&resultType=core
  locator: 'resultList.result[0]: id/doi/pmcid/title/authorString/pubYear/abstractText'
  accessed_at: '2026-10-21T10:16:29.420475Z'
  support: supports
  summary: Native metadata identifies Compartment-specific aggregases direct distinct
    nuclear and cytoplasmic aggregate deposition. by Miller SB, Ho CT, Winkler J,
    Khokhrina M, Neuner A, Mohamed MY, Guilbride DL, Richter K, Lisby M, Schiebel
    E, Mogk A, Bukau B. PMID25672362, DOI10.15252/embj.201489524. Bibliographic identity
    and abstract; primary body evidence is separately hashed.
  snapshot_sha256: 9f55ca90881cd3016024aa115ca7445a76d7eb078739f47f356daeb63a50835d
- evidence_id: inq-agent-gallina2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fncomms7533&format=json&resultType=core
  locator: 'resultList.result[0]: id/doi/pmcid/title/authorString/pubYear/abstractText'
  accessed_at: '2026-10-21T10:16:29.565802Z'
  support: supports
  summary: Native metadata identifies Cmr1/WDR76 defines a nuclear genotoxic stress
    body linking genome integrity and protein quality control. by Gallina I, Colding
    C, Henriksen P, Beli P, Nakamura K, Offman J, Mathiasen DP, Silva S, Hoffmann
    E, Groth A, Choudhary C, Lisby M. PMID25817432, DOI10.1038/ncomms7533. Bibliographic
    identity and abstract; primary body evidence is separately hashed.
  snapshot_sha256: 71dfd3ecd76a05109c4e10d77478c09c2d350472597edd946a7c8b4433cb9f2c
- evidence_id: inq-agent-sontag2023-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41556-023-01128-6&format=json&resultType=core
  locator: 'resultList.result[0]: id/doi/pmcid/title/authorString/pubYear/abstractText'
  accessed_at: '2026-10-21T10:16:30.017464Z'
  support: supports
  summary: Native metadata identifies Nuclear and cytoplasmic spatial protein quality
    control is coordinated by nuclear-vacuolar junctions and perinuclear ESCRT. by
    Sontag EM, Morales-Polanco F, Chen JH, McDermott G, Dolan PT, Gestaut D, Le Gros
    MA, Larabell C, Frydman J. PMID37081164, DOI10.1038/s41556-023-01128-6. Bibliographic
    identity and abstract; primary body evidence is separately hashed.
  snapshot_sha256: a478966aa0ce6f14ed713e853d34145b01971c1c652c552d5f88e6f01c67187c
- evidence_id: inq-agent-miller2015-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4369314/?report=xml
  locator: Genuine PMC4369314 native HTML; Results sec3–9, Discussion sec10, initial
    Methods sec12–13; derived paragraph indices36–89 and91–97 read, including Fig1–8
    captions. SupplementaryS6 and strain tables not independently read; figure pixels
    not inspected.
  accessed_at: '2026-10-21T10:16:30.515412Z'
  support: supports
  summary: Direct primary fluorescence and immunogold microscopy establish nuclear
    reporter/Hsp104 deposits. Btn2 loss blocks tested nuclear aggregation without
    blocking nuclear import; engineered Hsp42-NLS restores aggregation. Reporter degradation
    during recovery is similar despite impaired deposition. Hsp104-inhibition stabilization
    is reported in main Results with a SupplementaryS6 pointer. The article reinterprets
    earlier JUNQ as INQ, a historical interpretation preserved rather than imposed
    on later sources.
  snapshot_sha256: 99a2957189aed4b9b48128e16bd8e5a76a1ee69ff967c58c139dcbd150d794cf
- evidence_id: inq-agent-gallina2015-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4389229.1/PMC4389229.1.xml
  locator: PMC4389229.1 JATS Results titled Cmr1 marks an intranuclear quality control
    compartment and Btn2 promotes Mrc1 turnover and relocalization to INQ; full Discussion;
    Methods Yeast strains and cell culture; entire Fig3 caption. Front permissions/license
    explicitly CC BY4.0. Tracked Fig3 pixels are separately inspected local evidence.
  accessed_at: '2026-10-21T10:16:58.771617Z'
  support: supports
  summary: Direct primary Cmr1 imaging and genetic tests distinguish strictly nuclear
    INQ from cytoplasmic VHL foci. Cmr1 is stable rather than proven misfolded cargo;
    Mrc1 and Cmr1 focus formation are independent of each other. Btn2/Hsp42 dependencies
    vary with cargo and stress. Rpn11 and Cct6 overlap is partial, and genome-maintenance
    phenotypes are not proven direct consequences of INQ loss. Methods specify RAD5
    W303 derivatives by default with S288C libraries and exceptions.
  snapshot_sha256: ee9cb1c4fe41567584285f617bea8a6e42d5fdd99989c71689ddedd86c85ded9
- evidence_id: inq-agent-sontag2023-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12349969.1/PMC12349969.1.xml
  locator: PMC12349969.1 author-manuscript JATS Results S1–S8 and Discussion S9 read
    in full; Methods S12,S13,S18,S19,S31,S35; Data availability S46; Fig1,3,5–8 captions.
    Actual image pixels, supplementary strain table, videos and raw data not independently
    analyzed.
  accessed_at: '2026-10-21T10:16:59.262853Z'
  support: supports
  summary: Direct primary nuclear-targeted LuciTs/VHL experiments distinguish INQ
    and cytoplasmic JUNQ. NLS-LuciTs forms INQ with or without MG132. Both inclusions
    form after CHM7 loss but a subset fails to converge; NVJ loss preserves initial
    convergence while disrupting clearance and permitting cytoplasmic egress. VPS4
    loss preserves deposits and impairs delivery. Keima acidification, protease perturbations,
    reporter fragments and imaging support a vacuolar route alongside proteasomal
    clearance, while exact budding/tether steps remain proposed. Some imaging panels
    explicitly use MG132.
  snapshot_sha256: b01cac2d5de22e22250023435417325276855d8685f38d072c994ff3835264bb
- evidence_id: inq-agent-gallina2015-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4389229.1/PMC4389229.1.json
  locator: pmcid/version/doi/pmid/is_pmc_openaccess/license_code; media_urls ncomms7533-f3.jpg
    MD5
  accessed_at: '2026-10-21T10:16:58.773148Z'
  support: supports
  summary: Native PMC4389229 version1 package identifies DOI/PMID, open-access flag
    and CC BY label. Fig3 media MD5 is378de78d4843fa8e28e8207b2664dc51, equal to the
    tracked image. Exact licence version is supported separately by JATS.
  snapshot_sha256: 7e3fcca1320858765ebb4cd1b04864f9ef2fd2233c34a18186536d3fc61a3e1a
- evidence_id: inq-agent-sontag2023-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12349969.1/PMC12349969.1.json
  locator: pmcid/version/doi/pmid/mid/is_manuscript/is_pmc_openaccess/license_code
  accessed_at: '2026-10-21T10:16:59.302805Z'
  support: supports
  summary: Native PMC12349969 version1 is an author manuscript, NIHMS2091077, DOI10.1038/s41556-023-01128-6,
    PMID37081164. Package flags is_pmc_openaccess=false and license_code=TDM. Public
    readable JATS does not establish Creative Commons permission to host figures.
  snapshot_sha256: c0583b03e49c41fe4aaa05c4ed5fecc7a210ccf79b0652eb3a5a9cbf2a678c74
- evidence_id: image
  kind: record_content
  reference: data/images/inclusion/intranuclear_quality_control_compartment/pmc4389229_f3.jpg
  locator: Entire Fig3 visual inspection, panelsa–g; tracked SHA and native media
    MD5 comparison
  accessed_at: '2026-10-21T10:22:06Z'
  support: context_only
  summary: Panelsd/e distinguish nuclear Cmr1/VHL overlap from cytoplasmic VHL; panelf
    explicitly shows MMS and partial Cct6/Cmr1 overlap. Other panels contain screening,
    deletion frequencies and blots. Figure-specific caption gives2μm scales, IG66
    andIG111; no separate third-party credit appears in caption or pixels.
  snapshot_sha256: 9d15de2925ec7ada38d8b7281ed62110c4073fee15b464ed548b87b3687b1ecb
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    --verify
  locator: Captured focused native log
  accessed_at: '2026-10-21T10:17:37.218617Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    --causal-graphs
  locator: Captured focused native log
  accessed_at: '2026-10-21T10:17:38.987285Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/inclusion/intranuclear_quality_control_compartment.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:21Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/inclusion/intranuclear_quality_control_compartment.yaml'
  snapshot_sha256: 10d8c421ad309c4492623644b3b31a023244b9d5511482bcfe377a746bfa64dd
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/intranuclear_quality_control_compartment-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:23Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/inclusion/intranuclear_quality_control_compartment.yaml\
    \ --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/intranuclear_quality_control_compartment-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/intranuclear_quality_control_compartment-strict.tsv"
  snapshot_sha256: 856988e5cfa64d1e56791ed886392b4bc0dc466ff90f9a071cb8605e04c11206
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/inclusion/intranuclear_quality_control_compartment.yaml;
    exact collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:22:06Z'
  support: supports
  summary: '12 of13 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: cellstructuremech:intranuclear_quality_control_compartment: SKIPPED;
    resolved by evidence record. Source-native identity checked separately.'
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
  topic: Nuclear inclusion with distinct JUNQ and stress-granule boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: The proposed local identifier, definition, class and kind denote a discrete
    membraneless nuclear inclusion. Nuclear body and inclusion body are broader is-a
    classes; nucleus is parthood. Gallina and Sontag support separation from cytoplasmic
    JUNQ, while Miller historical reinterpretation is explicitly acknowledged. GO0097165
    is a distinct RNA/protein stress-granule class; shared stress context does not
    establish exact identity.
  evidence_ids:
  - inq-agent-go
  - inq-agent-miller2015-pmc
  - inq-agent-gallina2015-jats
  - inq-agent-sontag2023-jats
  - record
  - inq-agent-go-search-0
  - inq-agent-go-search-1
  - inq-agent-ols-exact
- assessment_id: components
  area: evidence
  topic: Variable cargo, localized aggregase and associated disaggregase
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: 'The four component classes preserve direct localization versus function:
    heterogeneous cargo, INQ-enriched Btn2, associated Hsp104 and conditionally recruited
    Cmr1-family example. Engineered VHL/LuciTs do not define native composition. Partial
    CCT/proteasome/APC recruitment and genetic effects of transport/ESCRT factors
    do not justify fixed whole-complex membership. Hsp42-NLS rescue does not establish
    native Hsp42 residence.'
  evidence_ids:
  - inq-agent-miller2015-pmc
  - inq-agent-gallina2015-jats
  - inq-agent-sontag2023-jats
  - record
- assessment_id: necessity
  area: evidence
  topic: Assay-bounded conditional assembly and dispensability
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: 'Btn2 CONDITIONAL is supported by deletion blocking tested nuclear deposition
    and engineered Hsp42-NLS substitution. Cmr1 DISPENSABLE is bounded by the explicitly
    stated Mrc1-focus readout: Mrc1 foci still form without Cmr1. This is not a claim
    that Cmr1 is dispensable for every INQ function or stress phenotype.'
  evidence_ids:
  - inq-agent-miller2015-pmc
  - inq-agent-gallina2015-jats
  - record
- assessment_id: necessity-unknown
  area: evidence
  topic: Unresolved native cargo and Hsp104 assembly requirements
  outcome: unknown
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: The heterogeneous cargo and associated Hsp104 classes retain UNKNOWN for
    formation or assembly necessity. Deposited cargo is constitutional material, but
    this does not establish a requirement for particular native cargo species. Hsp104
    localization and inhibitor-sensitive recovery concern association or turnover,
    not demonstrated necessity for initial INQ assembly.
  evidence_ids:
  - inq-agent-miller2015-pmc
  - inq-agent-gallina2015-jats
  - record
- assessment_id: proteins
  area: grounding
  topic: Verified reference identities and non-exact family candidates
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: All three reviewed proteins, names, gene/locus tokens and tax559292 match
    the record and each exact gene query returns one result. Btn2 has only an integrated
    N-terminal domain match; Hsp104 matches broader ClpA/B families. Q12510 belongs
    to the exact family label used for its abstract component, with localization restricted
    to the yeast example. The unchecked LLM family description supplies no mechanism.
  evidence_ids:
  - inq-agent-P53286
  - inq-agent-P31539
  - inq-agent-Q12510
  - inq-agent-query-BTN2
  - inq-agent-query-HSP104
  - inq-agent-query-CMR1
  - inq-agent-interpro-P53286
  - inq-agent-interpro-P31539
  - inq-agent-interpro-Q12510
  - inq-agent-IPR050853
  - record
- assessment_id: taxa
  area: scope
  topic: Experimental species and reference strains remain separate
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: The species-level canonical example is supported. Gallina primarily uses
    RAD5 W303 derivatives and S288C screening libraries with exceptions; Miller defers
    strain genotypes to supplements, and Sontag live-cell Methods name BY4741 while
    the full strain list is supplementary. The S288C protein examples explicitly establish
    reference identities rather than reassigning every experiment. No broad taxonomic
    distribution is inferred.
  evidence_ids:
  - inq-agent-taxon-4932
  - inq-agent-taxon-559292
  - inq-agent-P53286
  - inq-agent-P31539
  - inq-agent-Q12510
  - inq-agent-miller2015-pmc
  - inq-agent-gallina2015-jats
  - inq-agent-sontag2023-jats
  - record
- assessment_id: functions
  area: evidence
  topic: Sequestration and condition-specific clearance
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: Sequestration is observed, but Miller reporter degradation is unchanged
    when deposition is impaired, whereas Gallina links Btn2 loss to reduced Mrc1 turnover.
    These substrate/assay differences are retained. Sontag supports a vacuolar route
    for tested nuclear reporters with proteasomal processing in parallel, without
    proving the fate of every endogenous client or universal stress protection.
  evidence_ids:
  - inq-agent-miller2015-pmc
  - inq-agent-gallina2015-jats
  - inq-agent-sontag2023-jats
  - record
- assessment_id: assembly-graph
  area: graph
  topic: Six bounded intervention edges
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: NLS-LuciTs heat misfolding induces nuclear inclusions in Sontag; Miller
    Btn2 deletion impairs deposition and engineered nuclear Hsp42 restores it. Gallina
    MMS induces Cmr1 foci, while BTN2 and HSP42 deletions reduce that particular readout.
    These separate reporter/genotoxic-stress assays are not collapsed into one temporal
    pathway or universal Hsp42 requirement.
  evidence_ids:
  - inq-agent-miller2015-pmc
  - inq-agent-gallina2015-jats
  - inq-agent-sontag2023-jats
  - record
  - graph-policy
- assessment_id: clearance-graph
  area: graph
  topic: Six positioning and delivery edges
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: Sontag supports convergence across the envelope without fusion, conditional
    vacuolar delivery, NVJ1/VAC8-dependent clearance, a CHM7-sensitive convergence
    phenotype and VPS4-sensitive clearance. Initial formation and convergence remain
    distinct from delivery. Directed genetic and imaging results justify MECHANISTIC
    scope while precise molecular tethers and membrane-budding steps remain models.
  evidence_ids:
  - inq-agent-sontag2023-jats
  - record
  - graph-policy
- assessment_id: image
  area: provenance
  topic: Hosted Gallina Fig3 with exact native licence
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: The tracked image SHA9d15de2925ec7ada38d8b7281ed62110c4073fee15b464ed548b87b3687b1ecb
    and native package MD5 match. JATS explicitly gives CC BY4.0. Caption, image panels
    and microscopy scale/context agree with the curator description; the multi-panel
    image is not represented as a universal inventory. Sontag TDM metadata is not
    used as hosting permission.
  evidence_ids:
  - inq-agent-gallina2015-jats
  - inq-agent-gallina2015-package
  - image
  - inq-agent-sontag2023-package
  - record
- assessment_id: limits
  area: completeness
  topic: No forced inventory or material-state additions
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: The source-bounded discussions preserve native-client uncertainty, lack
    of universal dimensions/stoichiometry, incomplete supplemental strain mapping,
    and absence of direct evidence equating human WDR76 foci to yeast INQ. Q-body/JUNQ
    liquid-like interpretation is not transferred to INQ. No concrete required representation
    or unsupported claim was found.
  evidence_ids:
  - inq-agent-miller2015-pmc
  - inq-agent-gallina2015-jats
  - inq-agent-sontag2023-jats
  - record
- assessment_id: status
  area: provenance
  topic: Source tiers, stable ownership and status
  outcome: supported
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  summary: All cited main primary sources are readable through the actual captured
    bodies, with exact read scopes above. Historical notes about uninspected supplements
    remain historical and are not findings. The local identity self-references resolve
    to the inspected target. PROPOSED status, maintained ownership and history remain
    unchanged.
  evidence_ids:
  - record
  - inq-agent-miller2015-pmc
  - inq-agent-gallina2015-jats
  - inq-agent-sontag2023-jats
findings: []
actions: []
limitations:
- Native identity searches are bounded to the exact named/acronym queries described;
  local identity is not a claim of exhaustive absence from every ontology or repository.
- Miller main Results/Discussion and initial Methods, Gallina named INQ/Mrc1 Results/full
  Discussion/strain Methods, and Sontag S1–S9 plus relevant Methods/captions were
  read. Only tracked Gallina Fig3 pixels were independently inspected; supplementary
  strain tables, supporting figures/videos and raw datasets were not reanalyzed.
- Assembly necessity is experimentally supported only within the stated Btn2 and Mrc1-focus
  assays. Unknown Hsp104/cargo necessity and precise membrane-budding or tether mechanisms
  remain unknown.
- Sontag is a genuine public author-manuscript body with TDM metadata, not evidence
  of a Creative Commons image-hosting licence. Native protein examples establish identity
  separately from membership and experimental strain provenance.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- User-directed batch review explicitly requests an unsaved review for clean records
  as well as issue-bearing records; no finding is manufactured.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
