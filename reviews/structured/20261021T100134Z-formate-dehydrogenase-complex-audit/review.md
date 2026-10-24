# Formate dehydrogenase complex: identity, taxonomic evidence and mechanism scope

- Review: 20261021T100134Z-formate-dehydrogenase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:43:31Z
- Finished UTC: 2026-10-21T10:01:34Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generic identity and E.coli FDH-N composition/function are supported. One major finding concerns unrelated distribution evidence; one minor concerns mechanistic graph scope. Assembly necessity and broader soluble/archaeal generalizations remain bounded unknowns.

## Scope And Provenance

Whole single maintained target, exact native GO/taxa/chemical/protein/complex identifiers, every graph node and edge, and bounded primary/annotation source scope.

Selection: Index 1 in batch17, fixed strict sorted uncovered-path selection at fresh revision9c0446. One complete maintained target reviewed independently.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009326 | data/structures/energy_complex/formate_dehydrogenase_complex.yaml | maintained | formate dehydrogenase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native verify | passed | True | GO:0009326 | Focused native verification passed; identifier coverage is not independent evidence of membership or assembly necessity. |
| Native causal-graphs | passed | True | GO:0009326 | Focused native verification passed; identifier coverage is not independent evidence of membership or assembly necessity. |
| Expression-module applicability | not_applicable | False | GO:0009326 | These structural/compositional claims do not depend on expression-module inference; no iModulon absence claim is made. |
| Focused native schema | passed | True | GO:0009326 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009326 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0009326 | 16 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0009326 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0009326 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009326 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009326 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009326 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0009326 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Generic FDH complex and respiratory example

identity: supported. Targets: GO:0009326.

GO0009326 is the exact generic complex and GO1990204 is its native is-a parent. The record explicitly frames FdnGHI/FdoGHI as respiratory examples; the generic identity must remain distinct from their particular composition and quinone coupling.

### FdnGHI membership and canonical stoichiometry

evidence: supported. Targets: GO:0009326.

Three copies of each named subunit and the listed cofactors are directly represented in CPX1975; the recovered Jormakka main text supports trimeric packing, alpha-site oxidation, beta Fe-S relay and gamma hemes/quinone site. This is E.coli FDH-N evidence, not a universal inventory of soluble or archaeal FDHs.

### Assembly necessity of the conditional constituents

evidence: unknown. Targets: GO:0009326.

The record labels all three proteins CONDITIONAL. The inspected intact structures and electron-transfer functions establish membership and roles, but do not isolate removal of each protein or define assembly requirements across alternative FDH classes. Assembly necessity remains unverified; catalytic necessity is not substituted for it.

### Exact examples and bounded family withholding

grounding: supported. Targets: GO:0009326.

All three reviewed accession/name/gene/taxon pairs and bounded uniqueness queries agree. Checked Fdn and Fdo entries share candidate family mappings; IPR006471 also describes related hydrogenase/thiosulfate-reductase gamma subunits. Label-only status is defensible for these nitrate-inducible component labels, without claiming an exhaustive search or requiring optional additional examples.

### Bacterial and archaeal distribution references

scope: concern. Targets: GO:0009326.

Both broad taxonomic-distribution rows cite an unrelated viral/transcription study. E.coli FDH-N and the additional bacterial abstracts support bounded bacterial examples, but they cannot repair the declared broad bacterial frequency, methanogenic conservation or NAD+/F420-linked generalizations without appropriate sources.

### Respiratory reaction and PMF boundary

evidence: supported. Targets: GO:0009326.

GO0036397 and the native/primary evidence support formate oxidation with quinone reduction for the respiratory example. The definition explicitly invokes a redox loop, which is consistent with the primary discussion when read as the coupled FDH-N/Nar system; no standalone proton-pump claim is inferred. Broader soluble/NAD+/F420-dependent examples are outside the recovered experiment.

### Optional inventories and images

completeness: supported. Targets: GO:0009326.

The review identifies concrete existing evidence and graph defects. It does not require an image, measurement, exhaustive species inventory, or compulsory protein-family replacement merely because an optional slot is absent.

### Membership/activity summary versus mechanism

graph: concern. Targets: GO:0009326.

All five nodes and four edges were inspected. The component roles describe an electron-transfer sequence, but the graph connects each protein only by part-of and the complete structure to its activity. It does not represent transfer through the subunits or cofactor/quinone steps.

## Findings

### F1: Replace the unrelated taxonomic-distribution citation

major / open / confirmed; issue key: formate-dehydrogenase-complex-unrelated-distribution-reference.

Both bacterial and archaeal distribution claims cite PMID11884601, which resolves to a study of HA95/PKA and EBV-mediated transcription. It provides no support for formate-dehydrogenase occurrence, frequency, or conservation in either domain. The E.coli FDH-N structure supports a specific bacterial example, not the uncited archaeal/general-frequency claims.

### F2: Represent the supported electron-transfer steps or narrow graph scope

minor / open / confirmed; issue key: formate-dehydrogenase-complex-graph-explanatory-scope.

The FUNCTION graph is marked MECHANISTIC but contains only three constituent part-of edges and one whole-complex activity edge. These relationships are sound for the named example, yet they do not express the causal transfer route described in the prose. Preserve them as NONMECHANISTIC or add experimentally scoped electron-transfer transitions. Do not infer that a generic class always has this species-specific subunit set.

## Recommended Actions And Acceptance Checks

### A1

Attach relevant, directly inspected distribution sources or narrow/defer the unsupported rows.

- Preserve the verified broad complex identity and E.coli example.
- Each bacterial/archaeal occurrence and frequency claim must match its own source; do not use one bacterial structure paper to prove archaeal conservation.
- Any scientific correction requires separately authorized guarded curation, append-only history, rendering and native validation.

### A2

Match graph scope to its actual explanatory content.

- Retain valid membership and activity statements.
- A mechanistic version must resolve the supported subunit/cofactor electron route and distinguish the specific E.coli holoenzyme from the generic class.
- Any scientific correction requires separately authorized guarded curation, append-only history, rendering and native validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/formate_dehydrogenase_complex.yaml; Entire maintained YAML including definition, component roles/examples, taxonomic references, graph and history | context_only | The full target bytes were read after native inspection; no maintained scientific content was edited. |
| policy | docs/CURATION.md; Identity, grounding, evidence, and essentiality rules with frozen schema | context_only | Composition, catalytic function and necessity for structure assembly are separate claims. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Mechanistic scope and supported causal paths | context_only | Membership and whole-complex activity edges alone do not resolve causal electron-transfer steps. |
| formate-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009326,GO:1990204,GO:0098803,GO:0036397; All returned exact term names, definitions, source cross-references and relevant parent/child relations | supports | GO0009326 is the generic complex and a native child of GO1990204. GO0036397 denotes the quinone-linked reaction; GO0098803 is a broader respiratory-chain-complex class, with no invented formate subtype relationship. |
| formate-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Returned taxId, scientificName, rank and aliases | supports | This exact taxon is Escherichia coli K-12, rank strain; taxon identity alone establishes no structure distribution. |
| formate-agent-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Returned taxId, scientificName, rank and aliases | supports | This exact taxon is Bacteria, rank domain; taxon identity alone establishes no structure distribution. |
| formate-agent-tax-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; Returned taxId, scientificName, rank and aliases | supports | This exact taxon is Archaea, rank domain; taxon identity alone establishes no structure distribution. |
| formate-agent-CPX-1975 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1975; Exact identity/species; systematicName, complexAssemblies, all participant IDs/stoichiometries, functions and properties | supports | CPX-1975 curates three copies each of FdnG, FdnH and FdnI in the E.coli K-12 heterononamer; its redox-loop explanation explicitly couples Fdh-N to NarGHI. |
| formate-agent-P24183 | https://rest.uniprot.org/uniprotkb/P24183.json; entryType, primaryAccession, genes, organism, recommendedName, relevant comments and cross-references | supports | The reviewed entry is the declared fdnG protein at taxon83333, with the recorded recommended name and ComplexPortal/GO cross-references. Its own functional/subunit annotations were read separately from primary experimental bodies. |
| formate-agent-query-fdnG | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned result set and entry gene tokens | supports | The bounded reviewed exact-gene query returns one own-entry exact fdnG match at taxon83333; no automatic seeding or corpus-wide absence inference is made. |
| formate-agent-P0AAJ3 | https://rest.uniprot.org/uniprotkb/P0AAJ3.json; entryType, primaryAccession, genes, organism, recommendedName, relevant comments and cross-references | supports | The reviewed entry is the declared fdnH protein at taxon83333, with the recorded recommended name and ComplexPortal/GO cross-references. Its own functional/subunit annotations were read separately from primary experimental bodies. |
| formate-agent-query-fdnH | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned result set and entry gene tokens | supports | The bounded reviewed exact-gene query returns one own-entry exact fdnH match at taxon83333; no automatic seeding or corpus-wide absence inference is made. |
| formate-agent-P0AEK7 | https://rest.uniprot.org/uniprotkb/P0AEK7.json; entryType, primaryAccession, genes, organism, recommendedName, relevant comments and cross-references | supports | The reviewed entry is the declared fdnI protein at taxon83333, with the recorded recommended name and ComplexPortal/GO cross-references. Its own functional/subunit annotations were read separately from primary experimental bodies. |
| formate-agent-query-fdnI | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned result set and entry gene tokens | supports | The bounded reviewed exact-gene query returns one own-entry exact fdnI match at taxon83333; no automatic seeding or corpus-wide absence inference is made. |
| formate-agent-chebi-60539 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_60539; Exact native ChEBI ID, label, definition and relevant synonyms | supports | CHEBI:60539 resolves to Mo(=O)-bis(molybdopterin guanine dinucleotide)(4-); the listed CPX participant role is checked in the separate complex receipt. |
| formate-agent-chebi-16374 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16374; Exact native ChEBI ID, label, definition and relevant synonyms | supports | CHEBI:16374 resolves to menaquinone; the listed CPX participant role is checked in the separate complex receipt. |
| formate-agent-chebi-30413 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30413; Exact native ChEBI ID, label, definition and relevant synonyms | supports | CHEBI:30413 resolves to heme; the listed CPX participant role is checked in the separate complex receipt. |
| formate-agent-chebi-33725 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33725; Exact native ChEBI ID, label, definition and relevant synonyms | supports | CHEBI:33725 resolves to tetra-mu3-sulfido-tetrairon(0); the listed CPX participant role is checked in the separate complex receipt. |
| formate-agent-pmid-11884747 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11884747+AND+SRC%3AMED; Native title/authors/DOI/PMID and complete abstract; source is metadata/abstract, not the separate recovered main body | supports | Exact Jormakka2002 citation and primary abstract match DOI10.1126/science.1068186. The experiment concerns E.coli FDH-N and a structural explanation of the coupled FDH-N/Nar redox loop. |
| formate-agent-pmid-11884601 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11884601+AND+SRC%3AMED; Exact PMID identity and entire returned abstract | refutes | PMID11884601 is Han et al.2002 on HA95, protein kinase A and Epstein-Barr-virus nuclear-protein transcriptional coactivation. Its complete returned abstract concerns human lymphoid-cell/viral experiments, not bacterial or archaeal formate dehydrogenase distribution. |
| formate-agent-jormakka2002-browser | https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N; ResearchGate primary-paper portion only, displayed lines100–613: Abstract, Introduction, Overall structure and Electron transfer; archived browser-displayed source JSON, not an HTTP200 receipt | supports | The inspected paper opening and pp1863–64 establish the E.coli nitrate-respiration context, trimeric packing of heterotrimeric units, periplasmic alpha/beta modules and ordered cofactor electron transfer. The unrelated Caltech metadata in this combined browser output is excluded. |
| formate-agent-jormakka2002-browser2 | https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N; Primary-paper pp1863–66, displayed lines273–900: overall structure, electron transfer, alpha site and beta-subunit architecture; overlapping text is not independent replication; archived browser-displayed source JSON, not an HTTP200 receipt | supports | The alpha-subunit catalytic site and beta-subunit Fe-S relay support the component roles. Structural comparison and proposed catalytic/proton steps remain distinct from direct transfer or depletion measurements. |
| formate-agent-jormakka2002-browser3 | https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N; Primary-paper pp1866–68, displayed lines930–1762: beta/gamma sections, quinone mechanism, Table1 and PMF discussion; figures read as captions, not pixels; archived browser-displayed source JSON, not an HTTP200 receipt | supports | The gamma subunit contains two hemes and the quinone-binding site; HQNO is the analog in the complex structure. The proposed proton pathway and final PMF explanation concern a coupled FDH-N/Nar redox loop, not autonomous FDH proton pumping. |
| formate-agent-IPR006443 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006443/; Whole native family metadata, type, member databases, description and generated-description flags | supports | Native IPR006443 is the family Formate dehydrogenase-N, alpha subunit. Description and member databases were checked as candidate scope, not proof of exclusivity to the nitrate-inducible protein.  |
| formate-agent-IPR006470 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006470/; Whole native family metadata, type, member databases, description and generated-description flags | supports | Native IPR006470 is the family Formate dehydrogenase iron-sulphur subunit, Proteobacteria. Description and member databases were checked as candidate scope, not proof of exclusivity to the nitrate-inducible protein.  |
| formate-agent-IPR006471 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006471/; Whole native family metadata, type, member databases, description and generated-description flags | supports | Native IPR006471 is the family Formate dehydrogenase, gamma subunit. Description and member databases were checked as candidate scope, not proof of exclusivity to the nitrate-inducible protein.  |
| formate-agent-IPR014603 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014603/; Whole native family metadata, type, member databases, description and generated-description flags | supports | Native IPR014603 is the family Formate dehydrogenase iron-sulphur subunit. Description and member databases were checked as candidate scope, not proof of exclusivity to the nitrate-inducible protein.  |
| formate-agent-IPR051555 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051555/; Whole native family metadata, type, member databases, description and generated-description flags | supports | Native IPR051555 is the family Formate Dehydrogenase Electron Transfer Unit. Description and member databases were checked as candidate scope, not proof of exclusivity to the nitrate-inducible protein. The description is flagged as unchecked LLM text; no mechanistic conclusion relies on that generated prose. |
| formate-agent-IPR051817 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051817/; Whole native family metadata, type, member databases, description and generated-description flags | supports | Native IPR051817 is the family Formate dehydrogenase cytochrome b556 subunit. Description and member databases were checked as candidate scope, not proof of exclusivity to the nitrate-inducible protein. The description is flagged as unchecked LLM text; no mechanistic conclusion relies on that generated prose. |
| formate-agent-query-fdoG | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result, own gene tokens, organism and InterPro cross-references | supports | The exact reviewed fdoG entry P32176 at K-12 carries its own InterPro cross-references IPR006443. This row reports that entry alone; comparison with separately hashed Fdn entries is made in the grounding assessment. |
| formate-agent-query-fdoH | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result, own gene tokens, organism and InterPro cross-references | supports | The exact reviewed fdoH entry P0AAJ5 at K-12 carries its own InterPro cross-references IPR006470, IPR014603, IPR051555. This row reports that entry alone; comparison with separately hashed Fdn entries is made in the grounding assessment. |
| formate-agent-query-fdoI | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result, own gene tokens, organism and InterPro cross-references | supports | The exact reviewed fdoI entry P0AEL0 at K-12 carries its own InterPro cross-references IPR006471, IPR051817. This row reports that entry alone; comparison with separately hashed Fdn entries is made in the grounding assessment. |
| formate-agent-pmid-1504073 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A1504073+AND+SRC%3AMED; Exact GO-definition citation metadata and complete primary abstract only | supports | Native primary abstract reports a distinct E.coli formate dehydrogenase isoenzyme with different regulation and similar subunit composition. |
| formate-agent-pmid-8566699 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8566699+AND+SRC%3AMED; Exact GO-definition citation metadata and complete primary abstract only | supports | Native primary abstract describes a three-subunit Desulfovibrio vulgaris Hildenborough formate dehydrogenase with a c-type-heme small subunit; this bounds generalization of the FdnI b-heme example. |
| native-verify | /private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_complex.yaml --verify; Captured focused native command output and timestamped receipt | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_complex.yaml --causal-graphs; Captured focused native command output and timestamped receipt | supports | data/structures/energy_complex/formate_dehydrogenase_complex.yaml  (GO:0009326)<br>  formate_dehydrogenase_complex_mechanism	fdng_alpha_subunit	COVERED	-&gt;fdng_alpha_subunit (UniProtKB:P24183)<br>  formate_dehydrogenase_complex_mechanism	fdnh_iron_sulfur_subunit	COVERED	-&gt;fdnh_iron_sulfur_subunit (UniProtKB:P0AAJ3)<br>  formate_dehydrogenase_complex_mechanism	fdni_cytochrome_b_subunit	COVERED	-&gt;fdni_cytochrome_b_subunit (UniProtKB:P0AEK7)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/energy_complex/formate_dehydrogenase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/formate_dehydrogenase_complex.yaml |
| strict-result | just validate-strict data/structures/energy_complex/formate_dehydrogenase_complex.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/formate_dehydrogenase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/formate_dehydrogenase_complex.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/formate_dehydrogenase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch17-20261021-vub_b2nx/formate_dehydrogenase_complex-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/formate_dehydrogenase_complex.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 16 of18 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:11884601: UNREACHABLE; resolved by evidence formate-agent-pmid-11884601; PMID:11884747: UNREACHABLE; resolved by evidence formate-agent-pmid-11884747. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Jormakka2002 main scientific sections were inspected from three preserved browser-text snapshots, not native HTTP200 article responses. Their exact extents are given per row; the first includes excluded unrelated Caltech metadata. No supplementary Methods, raw diffraction, figure-pixel or reconstitution audit was performed.
- The primary paper proposes a quinone/proton pathway from structure and an HQNO analog; inferred steps are not relabeled direct proton-flux measurements.
- GO-definition source PMIDs1504073/8566699 were inspected only at native citation/abstract tier. No full-body audit or domain-wide census was performed.
- Six specified family candidates and exact K-12 Fdo comparisons were checked; no exhaustive assertion that an exact source-neutral family cannot exist is made. Unchecked generated InterPro descriptions are not used as mechanism evidence.
- Initial sandbox-network failures are retained separately as transport receipts; they are not biological absence evidence.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The exact fresh resolver residuals are supported by own native PMID receipts; resolving an identifier does not validate its biological use. Root adds final shared gates before finalization. No persistence or scientific edit is authorized by this draft.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100134Z-formate-dehydrogenase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Formate dehydrogenase complex: identity, taxonomic evidence and mechanism
  scope'
started_at: '2026-10-21T09:43:31Z'
finished_at: '2026-10-21T10:01:34Z'
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
summary: The generic identity and E.coli FDH-N composition/function are supported.
  One major finding concerns unrelated distribution evidence; one minor concerns mechanistic
  graph scope. Assembly necessity and broader soluble/archaeal generalizations remain
  bounded unknowns.
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
  - path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    sha256: 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e
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
- target_id: GO:0009326
  path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
  label: formate dehydrogenase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained scientific record
scope:
  description: Whole single maintained target, exact native GO/taxa/chemical/protein/complex
    identifiers, every graph node and edge, and bounded primary/annotation source
    scope.
  selection: Index 1 in batch17, fixed strict sorted uncovered-path selection at fresh
    revision9c0446. One complete maintained target reviewed independently.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009326
checks:
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0009326
  command: /private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    --verify
  exit_code: 0
  summary: Focused native verification passed; identifier coverage is not independent
    evidence of membership or assembly necessity.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0009326
  command: /private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native verification passed; identifier coverage is not independent
    evidence of membership or assembly necessity.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0009326
  summary: These structural/compositional claims do not depend on expression-module
    inference; no iModulon absence claim is made.
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009326
  command: just validate data/structures/energy_complex/formate_dehydrogenase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009326
  command: just validate-strict data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/formate_dehydrogenase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0009326
  summary: 16 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - formate-agent-pmid-11884601
  - formate-agent-pmid-11884747
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009326
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - formate-agent-go
  - formate-agent-tax-83333
  - formate-agent-tax-2
  - formate-agent-tax-2157
  - formate-agent-CPX-1975
  - formate-agent-P24183
  - formate-agent-query-fdnG
  - formate-agent-P0AAJ3
  - formate-agent-query-fdnH
  - formate-agent-P0AEK7
  - formate-agent-query-fdnI
  - formate-agent-chebi-60539
  - formate-agent-chebi-16374
  - formate-agent-chebi-30413
  - formate-agent-chebi-33725
  - formate-agent-pmid-11884747
  - formate-agent-pmid-11884601
  - formate-agent-jormakka2002-browser
  - formate-agent-jormakka2002-browser2
  - formate-agent-jormakka2002-browser3
  - formate-agent-IPR006443
  - formate-agent-IPR006470
  - formate-agent-IPR006471
  - formate-agent-IPR014603
  - formate-agent-IPR051555
  - formate-agent-IPR051817
  - formate-agent-query-fdoG
  - formate-agent-query-fdoH
  - formate-agent-query-fdoI
  - formate-agent-pmid-1504073
  - formate-agent-pmid-8566699
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009326
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
  - GO:0009326
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
  - GO:0009326
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
  - GO:0009326
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
  - GO:0009326
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
  reference: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
  locator: Entire maintained YAML including definition, component roles/examples,
    taxonomic references, graph and history
  accessed_at: '2026-10-21T09:51:24Z'
  support: context_only
  summary: The full target bytes were read after native inspection; no maintained
    scientific content was edited.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Identity, grounding, evidence, and essentiality rules with frozen schema
  accessed_at: '2026-10-21T09:51:24Z'
  support: context_only
  summary: Composition, catalytic function and necessity for structure assembly are
    separate claims.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Mechanistic scope and supported causal paths
  accessed_at: '2026-10-21T09:51:24Z'
  support: context_only
  summary: Membership and whole-complex activity edges alone do not resolve causal
    electron-transfer steps.
- evidence_id: formate-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009326,GO:1990204,GO:0098803,GO:0036397
  locator: All returned exact term names, definitions, source cross-references and
    relevant parent/child relations
  accessed_at: '2026-10-21T09:45:17.059904Z'
  support: supports
  summary: GO0009326 is the generic complex and a native child of GO1990204. GO0036397
    denotes the quinone-linked reaction; GO0098803 is a broader respiratory-chain-complex
    class, with no invented formate subtype relationship.
  snapshot_sha256: b831ec9219123db26f8d348c099a7acd8949e884e6965fa10ed49b393510bebc
- evidence_id: formate-agent-tax-83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Returned taxId, scientificName, rank and aliases
  accessed_at: '2026-10-21T09:45:17.064841Z'
  support: supports
  summary: This exact taxon is Escherichia coli K-12, rank strain; taxon identity
    alone establishes no structure distribution.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: formate-agent-tax-2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Returned taxId, scientificName, rank and aliases
  accessed_at: '2026-10-21T09:45:17.850306Z'
  support: supports
  summary: This exact taxon is Bacteria, rank domain; taxon identity alone establishes
    no structure distribution.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: formate-agent-tax-2157
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: Returned taxId, scientificName, rank and aliases
  accessed_at: '2026-10-21T09:45:17.892256Z'
  support: supports
  summary: This exact taxon is Archaea, rank domain; taxon identity alone establishes
    no structure distribution.
  snapshot_sha256: c6e652011b95e43e933983bf5f3f5cec9508c1925adae00dc55e46cd4e816b19
- evidence_id: formate-agent-CPX-1975
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1975
  locator: Exact identity/species; systematicName, complexAssemblies, all participant
    IDs/stoichiometries, functions and properties
  accessed_at: '2026-10-21T09:45:18.547152Z'
  support: supports
  summary: CPX-1975 curates three copies each of FdnG, FdnH and FdnI in the E.coli
    K-12 heterononamer; its redox-loop explanation explicitly couples Fdh-N to NarGHI.
  snapshot_sha256: ed6cdaac9f3fd6c7c485a7721f2c97842d4a80b3fd18339a924bf918350cdc9a
- evidence_id: formate-agent-P24183
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P24183.json
  locator: entryType, primaryAccession, genes, organism, recommendedName, relevant
    comments and cross-references
  accessed_at: '2026-10-21T09:45:17.060646Z'
  support: supports
  summary: The reviewed entry is the declared fdnG protein at taxon83333, with the
    recorded recommended name and ComplexPortal/GO cross-references. Its own functional/subunit
    annotations were read separately from primary experimental bodies.
  snapshot_sha256: ba2315e5da95abf93454652ba95bbb88544bacfd880ab626d0de191d2a4bbcfd
- evidence_id: formate-agent-query-fdnG
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned result set and entry gene tokens
  accessed_at: '2026-10-21T09:45:17.062629Z'
  support: supports
  summary: The bounded reviewed exact-gene query returns one own-entry exact fdnG
    match at taxon83333; no automatic seeding or corpus-wide absence inference is
    made.
  snapshot_sha256: fd97d9165d2474db32a0256d5d281eee329201683eae5b7ebb318e64c155f782
- evidence_id: formate-agent-P0AAJ3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AAJ3.json
  locator: entryType, primaryAccession, genes, organism, recommendedName, relevant
    comments and cross-references
  accessed_at: '2026-10-21T09:45:17.060273Z'
  support: supports
  summary: The reviewed entry is the declared fdnH protein at taxon83333, with the
    recorded recommended name and ComplexPortal/GO cross-references. Its own functional/subunit
    annotations were read separately from primary experimental bodies.
  snapshot_sha256: dfd5786fd27795f7864c49e371f7f6a2cf4a1be773a8fac4ea377a4a963ba349
- evidence_id: formate-agent-query-fdnH
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned result set and entry gene tokens
  accessed_at: '2026-10-21T09:45:17.063435Z'
  support: supports
  summary: The bounded reviewed exact-gene query returns one own-entry exact fdnH
    match at taxon83333; no automatic seeding or corpus-wide absence inference is
    made.
  snapshot_sha256: 58db8e9048d4c7d73e40a9829a93684bab444f8f15ca2e739b71c55b70dad468
- evidence_id: formate-agent-P0AEK7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AEK7.json
  locator: entryType, primaryAccession, genes, organism, recommendedName, relevant
    comments and cross-references
  accessed_at: '2026-10-21T09:45:17.062406Z'
  support: supports
  summary: The reviewed entry is the declared fdnI protein at taxon83333, with the
    recorded recommended name and ComplexPortal/GO cross-references. Its own functional/subunit
    annotations were read separately from primary experimental bodies.
  snapshot_sha256: 944e58794aef18b85feefa6325421b4962db8fc0cc0dbb3a3c9c534b3bb00611
- evidence_id: formate-agent-query-fdnI
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned result set and entry gene tokens
  accessed_at: '2026-10-21T09:45:17.063882Z'
  support: supports
  summary: The bounded reviewed exact-gene query returns one own-entry exact fdnI
    match at taxon83333; no automatic seeding or corpus-wide absence inference is
    made.
  snapshot_sha256: b4349e8db16c10f14b726c577918be9e7ec446e677516d46ed531953dcc57150
- evidence_id: formate-agent-chebi-60539
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_60539
  locator: Exact native ChEBI ID, label, definition and relevant synonyms
  accessed_at: '2026-10-21T09:45:17.987510Z'
  support: supports
  summary: CHEBI:60539 resolves to Mo(=O)-bis(molybdopterin guanine dinucleotide)(4-);
    the listed CPX participant role is checked in the separate complex receipt.
  snapshot_sha256: d4af89178cd9f6d2d13474e41ce605ebf40f7984a52f488232f4cb42b10771b5
- evidence_id: formate-agent-chebi-16374
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16374
  locator: Exact native ChEBI ID, label, definition and relevant synonyms
  accessed_at: '2026-10-21T09:45:17.999102Z'
  support: supports
  summary: CHEBI:16374 resolves to menaquinone; the listed CPX participant role is
    checked in the separate complex receipt.
  snapshot_sha256: 2de776b9c8383ac4a359573a9d404e233ec52e5c4ce828ff580a436451466eac
- evidence_id: formate-agent-chebi-30413
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30413
  locator: Exact native ChEBI ID, label, definition and relevant synonyms
  accessed_at: '2026-10-21T09:45:18.452589Z'
  support: supports
  summary: CHEBI:30413 resolves to heme; the listed CPX participant role is checked
    in the separate complex receipt.
  snapshot_sha256: 674cfe9540f1509052fe3ca7d406154865585bac0d66e0663e1b4bdbb9e27d80
- evidence_id: formate-agent-chebi-33725
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33725
  locator: Exact native ChEBI ID, label, definition and relevant synonyms
  accessed_at: '2026-10-21T09:45:18.514891Z'
  support: supports
  summary: CHEBI:33725 resolves to tetra-mu3-sulfido-tetrairon(0); the listed CPX
    participant role is checked in the separate complex receipt.
  snapshot_sha256: 3f443234ffd6663280774061bb05a66b042e5a19c07bc55713ed522ee5787371
- evidence_id: formate-agent-pmid-11884747
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11884747+AND+SRC%3AMED
  locator: Native title/authors/DOI/PMID and complete abstract; source is metadata/abstract,
    not the separate recovered main body
  accessed_at: '2026-10-21T09:45:17.895257Z'
  support: supports
  summary: Exact Jormakka2002 citation and primary abstract match DOI10.1126/science.1068186.
    The experiment concerns E.coli FDH-N and a structural explanation of the coupled
    FDH-N/Nar redox loop.
  snapshot_sha256: fde1a729d4929a7436d64ed57055f5b6a9517a22b5020c221687d93c6ee61360
- evidence_id: formate-agent-pmid-11884601
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11884601+AND+SRC%3AMED
  locator: Exact PMID identity and entire returned abstract
  accessed_at: '2026-10-21T09:45:17.937923Z'
  support: refutes
  summary: PMID11884601 is Han et al.2002 on HA95, protein kinase A and Epstein-Barr-virus
    nuclear-protein transcriptional coactivation. Its complete returned abstract concerns
    human lymphoid-cell/viral experiments, not bacterial or archaeal formate dehydrogenase
    distribution.
  snapshot_sha256: e26b54b63f1f7bb6d50fd13deaf093be0352ea02fc92bc35afe2ec68944fe012
- evidence_id: formate-agent-jormakka2002-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N
  locator: 'ResearchGate primary-paper portion only, displayed lines100–613: Abstract,
    Introduction, Overall structure and Electron transfer; archived browser-displayed
    source JSON, not an HTTP200 receipt'
  accessed_at: '2026-10-21T08:42:36Z'
  support: supports
  summary: The inspected paper opening and pp1863–64 establish the E.coli nitrate-respiration
    context, trimeric packing of heterotrimeric units, periplasmic alpha/beta modules
    and ordered cofactor electron transfer. The unrelated Caltech metadata in this
    combined browser output is excluded.
  snapshot_sha256: cfd04dd5b54ad13716d5aa429d44d3d94e48cfcb427c3f090bcc6e23c34be4b9
- evidence_id: formate-agent-jormakka2002-browser2
  kind: primary_source
  reference: https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N
  locator: 'Primary-paper pp1863–66, displayed lines273–900: overall structure, electron
    transfer, alpha site and beta-subunit architecture; overlapping text is not independent
    replication; archived browser-displayed source JSON, not an HTTP200 receipt'
  accessed_at: '2026-10-21T08:48:50Z'
  support: supports
  summary: The alpha-subunit catalytic site and beta-subunit Fe-S relay support the
    component roles. Structural comparison and proposed catalytic/proton steps remain
    distinct from direct transfer or depletion measurements.
  snapshot_sha256: 3a7d4cf752bc7fc1f0b7f2c8d310f8feee6e4cec7e1be745ebd73733132bc7fd
- evidence_id: formate-agent-jormakka2002-browser3
  kind: primary_source
  reference: https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N
  locator: 'Primary-paper pp1866–68, displayed lines930–1762: beta/gamma sections,
    quinone mechanism, Table1 and PMF discussion; figures read as captions, not pixels;
    archived browser-displayed source JSON, not an HTTP200 receipt'
  accessed_at: '2026-10-21T08:49:03Z'
  support: supports
  summary: The gamma subunit contains two hemes and the quinone-binding site; HQNO
    is the analog in the complex structure. The proposed proton pathway and final
    PMF explanation concern a coupled FDH-N/Nar redox loop, not autonomous FDH proton
    pumping.
  snapshot_sha256: e5bda83037ed42c0ed4e5009f4932dd31a2ece97de2ff36bbcd3deb07d449eeb
- evidence_id: formate-agent-IPR006443
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006443/
  locator: Whole native family metadata, type, member databases, description and generated-description
    flags
  accessed_at: '2026-10-21T08:42:36.843597Z'
  support: supports
  summary: 'Native IPR006443 is the family Formate dehydrogenase-N, alpha subunit.
    Description and member databases were checked as candidate scope, not proof of
    exclusivity to the nitrate-inducible protein. '
  snapshot_sha256: 24f4e300ffb3d9d955944ac1e052fc9f8fa01990be18ca8488598f57636b60d8
- evidence_id: formate-agent-IPR006470
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006470/
  locator: Whole native family metadata, type, member databases, description and generated-description
    flags
  accessed_at: '2026-10-21T08:42:36.174210Z'
  support: supports
  summary: 'Native IPR006470 is the family Formate dehydrogenase iron-sulphur subunit,
    Proteobacteria. Description and member databases were checked as candidate scope,
    not proof of exclusivity to the nitrate-inducible protein. '
  snapshot_sha256: 84eb09c9e62a1c1e495491e40225da1f78ff6a2058fd88392189ec969758187f
- evidence_id: formate-agent-IPR006471
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006471/
  locator: Whole native family metadata, type, member databases, description and generated-description
    flags
  accessed_at: '2026-10-21T08:42:36.831198Z'
  support: supports
  summary: 'Native IPR006471 is the family Formate dehydrogenase, gamma subunit. Description
    and member databases were checked as candidate scope, not proof of exclusivity
    to the nitrate-inducible protein. '
  snapshot_sha256: 3d1551fd8933584086ab05290617b611d20f1703641048bbade7301cbe877851
- evidence_id: formate-agent-IPR014603
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014603/
  locator: Whole native family metadata, type, member databases, description and generated-description
    flags
  accessed_at: '2026-10-21T08:42:36.177143Z'
  support: supports
  summary: 'Native IPR014603 is the family Formate dehydrogenase iron-sulphur subunit.
    Description and member databases were checked as candidate scope, not proof of
    exclusivity to the nitrate-inducible protein. '
  snapshot_sha256: 8bb0299ccaad43b41a404c591262616896e7787d67647ff3ab87de310c5fdd02
- evidence_id: formate-agent-IPR051555
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051555/
  locator: Whole native family metadata, type, member databases, description and generated-description
    flags
  accessed_at: '2026-10-21T08:42:36.409338Z'
  support: supports
  summary: Native IPR051555 is the family Formate Dehydrogenase Electron Transfer
    Unit. Description and member databases were checked as candidate scope, not proof
    of exclusivity to the nitrate-inducible protein. The description is flagged as
    unchecked LLM text; no mechanistic conclusion relies on that generated prose.
  snapshot_sha256: 0b9a9eff7be9ed6a6c783399f853c007079e2ce7f1d5797ee6f85f0e9997fd77
- evidence_id: formate-agent-IPR051817
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051817/
  locator: Whole native family metadata, type, member databases, description and generated-description
    flags
  accessed_at: '2026-10-21T08:42:36.833427Z'
  support: supports
  summary: Native IPR051817 is the family Formate dehydrogenase cytochrome b556 subunit.
    Description and member databases were checked as candidate scope, not proof of
    exclusivity to the nitrate-inducible protein. The description is flagged as unchecked
    LLM text; no mechanistic conclusion relies on that generated prose.
  snapshot_sha256: 9a9fde2804cf8d99257b1bc6434666fd667d70b4eda23fc484a9be2eb6f68331
- evidence_id: formate-agent-query-fdoG
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result, own gene tokens, organism and InterPro cross-references
  accessed_at: '2026-10-21T09:47:41.443742Z'
  support: supports
  summary: The exact reviewed fdoG entry P32176 at K-12 carries its own InterPro cross-references
    IPR006443. This row reports that entry alone; comparison with separately hashed
    Fdn entries is made in the grounding assessment.
  snapshot_sha256: 350efd301bc048134be70e6a58641f001e4b66b0c4a4f3fe7e1b63f5a4152fda
- evidence_id: formate-agent-query-fdoH
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result, own gene tokens, organism and InterPro cross-references
  accessed_at: '2026-10-21T09:47:41.446413Z'
  support: supports
  summary: The exact reviewed fdoH entry P0AAJ5 at K-12 carries its own InterPro cross-references
    IPR006470, IPR014603, IPR051555. This row reports that entry alone; comparison
    with separately hashed Fdn entries is made in the grounding assessment.
  snapshot_sha256: b8c2eb6df27a506406be65181d6b237534f629492ba3302c0156d208fa61a2c6
- evidence_id: formate-agent-query-fdoI
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result, own gene tokens, organism and InterPro cross-references
  accessed_at: '2026-10-21T09:47:41.446646Z'
  support: supports
  summary: The exact reviewed fdoI entry P0AEL0 at K-12 carries its own InterPro cross-references
    IPR006471, IPR051817. This row reports that entry alone; comparison with separately
    hashed Fdn entries is made in the grounding assessment.
  snapshot_sha256: a3d914b2c3a4e07590693bb6a7cd668cebb58121df1ca5cc88a6c615f005d9f3
- evidence_id: formate-agent-pmid-1504073
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A1504073+AND+SRC%3AMED
  locator: Exact GO-definition citation metadata and complete primary abstract only
  accessed_at: '2026-10-21T09:47:41.441833Z'
  support: supports
  summary: Native primary abstract reports a distinct E.coli formate dehydrogenase
    isoenzyme with different regulation and similar subunit composition.
  snapshot_sha256: 5abcc0c7ef25235f581380df72e3dac6c1ead893aee5d39c3d2605d7f497592a
- evidence_id: formate-agent-pmid-8566699
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8566699+AND+SRC%3AMED
  locator: Exact GO-definition citation metadata and complete primary abstract only
  accessed_at: '2026-10-21T09:47:41.443068Z'
  support: supports
  summary: Native primary abstract describes a three-subunit Desulfovibrio vulgaris
    Hildenborough formate dehydrogenase with a c-type-heme small subunit; this bounds
    generalization of the FdnI b-heme example.
  snapshot_sha256: cf35cb31d99cf3559c458fea2ea884ffc595c4a055b1685c2ab6388da3bc4330
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    --verify
  locator: Captured focused native command output and timestamped receipt
  accessed_at: '2026-10-21T09:47:16.120407Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    --causal-graphs
  locator: Captured focused native command output and timestamped receipt
  accessed_at: '2026-10-21T09:47:18.346858Z'
  support: supports
  summary: "data/structures/energy_complex/formate_dehydrogenase_complex.yaml  (GO:0009326)\n\
    \  formate_dehydrogenase_complex_mechanism\tfdng_alpha_subunit\tCOVERED\t->fdng_alpha_subunit\
    \ (UniProtKB:P24183)\n  formate_dehydrogenase_complex_mechanism\tfdnh_iron_sulfur_subunit\t\
    COVERED\t->fdnh_iron_sulfur_subunit (UniProtKB:P0AAJ3)\n  formate_dehydrogenase_complex_mechanism\t\
    fdni_cytochrome_b_subunit\tCOVERED\t->fdni_cytochrome_b_subunit (UniProtKB:P0AEK7)\n\
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
  snapshot_sha256: 0d1606e67e7adec4d9a42a5ba7bc7c8f70ecf7a91349686b0cb351992185d8f7
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/formate_dehydrogenase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:43:37Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/formate_dehydrogenase_complex.yaml'
  snapshot_sha256: c4a135ddce51618f4e7995940814fe8ff56354867b7c57b48820d1cfdf6511e5
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/formate_dehydrogenase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:43:41Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/formate_dehydrogenase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/formate_dehydrogenase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch17-20261021-vub_b2nx/formate_dehydrogenase_complex-strict.tsv"
  snapshot_sha256: 6d86c615fb76a99ce5a905be9cc3ad0678259e538ba55db1b9b32b790c24bcde
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/formate_dehydrogenase_complex.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T09:51:24Z'
  support: supports
  summary: '16 of18 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:11884601: UNREACHABLE; resolved by evidence formate-agent-pmid-11884601;
    PMID:11884747: UNREACHABLE; resolved by evidence formate-agent-pmid-11884747.
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
  topic: Generic FDH complex and respiratory example
  outcome: supported
  target_ids:
  - GO:0009326
  summary: GO0009326 is the exact generic complex and GO1990204 is its native is-a
    parent. The record explicitly frames FdnGHI/FdoGHI as respiratory examples; the
    generic identity must remain distinct from their particular composition and quinone
    coupling.
  evidence_ids:
  - formate-agent-go
  - formate-agent-pmid-11884747
  - formate-agent-CPX-1975
  - formate-agent-pmid-1504073
  - formate-agent-pmid-8566699
  - record
- assessment_id: composition
  area: evidence
  topic: FdnGHI membership and canonical stoichiometry
  outcome: supported
  target_ids:
  - GO:0009326
  summary: Three copies of each named subunit and the listed cofactors are directly
    represented in CPX1975; the recovered Jormakka main text supports trimeric packing,
    alpha-site oxidation, beta Fe-S relay and gamma hemes/quinone site. This is E.coli
    FDH-N evidence, not a universal inventory of soluble or archaeal FDHs.
  evidence_ids:
  - formate-agent-CPX-1975
  - formate-agent-jormakka2002-browser
  - formate-agent-jormakka2002-browser2
  - formate-agent-jormakka2002-browser3
  - formate-agent-chebi-60539
  - formate-agent-chebi-16374
  - formate-agent-chebi-30413
  - formate-agent-chebi-33725
  - formate-agent-P24183
  - formate-agent-P0AAJ3
  - formate-agent-P0AEK7
  - record
- assessment_id: necessity
  area: evidence
  topic: Assembly necessity of the conditional constituents
  outcome: unknown
  target_ids:
  - GO:0009326
  summary: The record labels all three proteins CONDITIONAL. The inspected intact
    structures and electron-transfer functions establish membership and roles, but
    do not isolate removal of each protein or define assembly requirements across
    alternative FDH classes. Assembly necessity remains unverified; catalytic necessity
    is not substituted for it.
  evidence_ids:
  - formate-agent-CPX-1975
  - formate-agent-jormakka2002-browser
  - formate-agent-jormakka2002-browser2
  - formate-agent-jormakka2002-browser3
  - record
  - policy
- assessment_id: grounding
  area: grounding
  topic: Exact examples and bounded family withholding
  outcome: supported
  target_ids:
  - GO:0009326
  summary: All three reviewed accession/name/gene/taxon pairs and bounded uniqueness
    queries agree. Checked Fdn and Fdo entries share candidate family mappings; IPR006471
    also describes related hydrogenase/thiosulfate-reductase gamma subunits. Label-only
    status is defensible for these nitrate-inducible component labels, without claiming
    an exhaustive search or requiring optional additional examples.
  evidence_ids:
  - formate-agent-P24183
  - formate-agent-P0AAJ3
  - formate-agent-P0AEK7
  - formate-agent-query-fdnG
  - formate-agent-query-fdnH
  - formate-agent-query-fdnI
  - formate-agent-IPR006443
  - formate-agent-IPR006470
  - formate-agent-IPR006471
  - formate-agent-IPR014603
  - formate-agent-IPR051555
  - formate-agent-IPR051817
  - formate-agent-query-fdoG
  - formate-agent-query-fdoH
  - formate-agent-query-fdoI
  - formate-agent-tax-83333
  - formate-agent-tax-2
  - formate-agent-tax-2157
  - record
- assessment_id: taxonomic-evidence
  area: scope
  topic: Bacterial and archaeal distribution references
  outcome: concern
  target_ids:
  - GO:0009326
  summary: Both broad taxonomic-distribution rows cite an unrelated viral/transcription
    study. E.coli FDH-N and the additional bacterial abstracts support bounded bacterial
    examples, but they cannot repair the declared broad bacterial frequency, methanogenic
    conservation or NAD+/F420-linked generalizations without appropriate sources.
  evidence_ids:
  - formate-agent-pmid-11884601
  - formate-agent-pmid-11884747
  - formate-agent-jormakka2002-browser
  - formate-agent-pmid-1504073
  - formate-agent-pmid-8566699
  - formate-agent-tax-83333
  - formate-agent-tax-2
  - formate-agent-tax-2157
  - record
- assessment_id: function
  area: evidence
  topic: Respiratory reaction and PMF boundary
  outcome: supported
  target_ids:
  - GO:0009326
  summary: GO0036397 and the native/primary evidence support formate oxidation with
    quinone reduction for the respiratory example. The definition explicitly invokes
    a redox loop, which is consistent with the primary discussion when read as the
    coupled FDH-N/Nar system; no standalone proton-pump claim is inferred. Broader
    soluble/NAD+/F420-dependent examples are outside the recovered experiment.
  evidence_ids:
  - formate-agent-go
  - formate-agent-CPX-1975
  - formate-agent-jormakka2002-browser
  - formate-agent-jormakka2002-browser2
  - formate-agent-jormakka2002-browser3
  - formate-agent-pmid-11884747
  - record
- assessment_id: completeness
  area: completeness
  topic: Optional inventories and images
  outcome: supported
  target_ids:
  - GO:0009326
  summary: The review identifies concrete existing evidence and graph defects. It
    does not require an image, measurement, exhaustive species inventory, or compulsory
    protein-family replacement merely because an optional slot is absent.
  evidence_ids:
  - formate-agent-CPX-1975
  - formate-agent-go
  - record
  - policy
- assessment_id: graph
  area: graph
  topic: Membership/activity summary versus mechanism
  outcome: concern
  target_ids:
  - GO:0009326
  summary: All five nodes and four edges were inspected. The component roles describe
    an electron-transfer sequence, but the graph connects each protein only by part-of
    and the complete structure to its activity. It does not represent transfer through
    the subunits or cofactor/quinone steps.
  evidence_ids:
  - formate-agent-go
  - formate-agent-CPX-1975
  - formate-agent-jormakka2002-browser
  - formate-agent-jormakka2002-browser2
  - formate-agent-jormakka2002-browser3
  - record
  - graph-policy
findings:
- finding_id: F1
  issue_key: formate-dehydrogenase-complex-unrelated-distribution-reference
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Replace the unrelated taxonomic-distribution citation
  description: Both bacterial and archaeal distribution claims cite PMID11884601,
    which resolves to a study of HA95/PKA and EBV-mediated transcription. It provides
    no support for formate-dehydrogenase occurrence, frequency, or conservation in
    either domain. The E.coli FDH-N structure supports a specific bacterial example,
    not the uncited archaeal/general-frequency claims.
  target_ids:
  - GO:0009326
  field_paths:
  - taxonomic_distribution[0].reference
  - taxonomic_distribution[1].reference
  - taxonomic_distribution[0].note
  - taxonomic_distribution[1].note
  evidence_ids:
  - formate-agent-pmid-11884601
  - formate-agent-pmid-11884747
  - formate-agent-jormakka2002-browser
  - formate-agent-go
  - formate-agent-tax-83333
  - formate-agent-tax-2
  - formate-agent-tax-2157
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: major
  normalization_reason: A material asserted biological claim has an unrelated supporting
    citation or contradicts the demonstrated reaction.
- finding_id: F2
  issue_key: formate-dehydrogenase-complex-graph-explanatory-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Represent the supported electron-transfer steps or narrow graph scope
  description: The FUNCTION graph is marked MECHANISTIC but contains only three constituent
    part-of edges and one whole-complex activity edge. These relationships are sound
    for the named example, yet they do not express the causal transfer route described
    in the prose. Preserve them as NONMECHANISTIC or add experimentally scoped electron-transfer
    transitions. Do not infer that a generic class always has this species-specific
    subunit set.
  target_ids:
  - GO:0009326
  field_paths:
  - causal_graphs[0].scope_status
  - causal_graphs[0].edges
  evidence_ids:
  - formate-agent-go
  - formate-agent-CPX-1975
  - formate-agent-jormakka2002-browser
  - formate-agent-jormakka2002-browser2
  - formate-agent-jormakka2002-browser3
  - record
  - graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: minor
  normalization_reason: The supported constituent membership and activity remain valid;
    the defect is bounded to explanatory graph scope.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0009326
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained scientific record
  description: Attach relevant, directly inspected distribution sources or narrow/defer
    the unsupported rows.
  acceptance_checks:
  - Preserve the verified broad complex identity and E.coli example.
  - Each bacterial/archaeal occurrence and frequency claim must match its own source;
    do not use one bacterial structure paper to prove archaeal conservation.
  - Any scientific correction requires separately authorized guarded curation, append-only
    history, rendering and native validation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0009326
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained scientific record
  description: Match graph scope to its actual explanatory content.
  acceptance_checks:
  - Retain valid membership and activity statements.
  - A mechanistic version must resolve the supported subunit/cofactor electron route
    and distinguish the specific E.coli holoenzyme from the generic class.
  - Any scientific correction requires separately authorized guarded curation, append-only
    history, rendering and native validation.
limitations:
- Jormakka2002 main scientific sections were inspected from three preserved browser-text
  snapshots, not native HTTP200 article responses. Their exact extents are given per
  row; the first includes excluded unrelated Caltech metadata. No supplementary Methods,
  raw diffraction, figure-pixel or reconstitution audit was performed.
- The primary paper proposes a quinone/proton pathway from structure and an HQNO analog;
  inferred steps are not relabeled direct proton-flux measurements.
- GO-definition source PMIDs1504073/8566699 were inspected only at native citation/abstract
  tier. No full-body audit or domain-wide census was performed.
- Six specified family candidates and exact K-12 Fdo comparisons were checked; no
  exhaustive assertion that an exact source-neutral family cannot exist is made. Unchecked
  generated InterPro descriptions are not used as mechanism evidence.
- Initial sandbox-network failures are retained separately as transport receipts;
  they are not biological absence evidence.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The exact fresh resolver residuals are supported by own native PMID receipts; resolving
  an identifier does not validate its biological use. Root adds final shared gates
  before finalization. No persistence or scientific edit is authorized by this draft.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
