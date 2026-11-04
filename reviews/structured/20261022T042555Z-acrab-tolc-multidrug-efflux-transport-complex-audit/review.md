# Source-backed review of acrab tolc multidrug efflux transport complex

- Review: 20261022T042555Z-acrab-tolc-multidrug-efflux-transport-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:58:53Z
- Finished UTC: 2026-10-22T04:25:55Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor correction resolves AcrA’s exact family grounding. The tripartite pump, source composition, native identities and coarse transport model are supported; formation necessity remains untested by the inspected evidence.

## Scope And Provenance

Exactly one complete target; no neighboring scientific-record verdict is imported. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch43 fixed strict path order, index 10; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml | maintained | AcrAB-TolC multidrug efflux transport complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Focused validator passed. |
| Focused native proteins | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | 9 of 13 collected target identifiers returned OK. ECO:0000353: SKIPPED; Native Complex Portal CPX-4263 explicitly returns this exact ECO identifier with physical interaction evidence description. Dedicated ECO authority metadata was not separately retrieved; no biological inference follows merely from this code.; PDB:5V5S: SKIPPED; Native PDB entry and assembly1 verify engineered apo AcrAB-TolC structure, 6:3:3 subunit stoichiometry and exact identity; the ligand-bound AcrABZ comparator is kept distinct.; PMID:28355133: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex: SKIPPED; Frozen current target identity matches exactly one maintained record in an ignored-inclusive local identifier search. This local identity verification does not establish exhaustive ontology absence. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Specific local identity and generic parent

identity: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

The local identifier denotes the exact CPX-supported AcrAB-TolC pump rather than claiming the broad GO parent is synonymous. Definition, heterododecamer and source-composition import are correct.

### Tripartite stoichiometry and family grounding

grounding: concern. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

The three component roles and 6:3:3 counts match CPX and deposited structure. TolC family grounding is correct. AcrA now has an exact verified family; the broader AcrB candidate is insufficient for forced replacement.

### Individual formation necessity remains unresolved

grounding: unknown. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

All three components are present in the defined tripartite pump, but CPX composition and engineered intact cryo-EM structures do not independently test the record’s three ESSENTIAL formation labels. This review does not redefine those labels as catalytic importance or mere membership and does not infer a contradiction solely from missing depletion experiments.

### Native references and source context

grounding: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

AcrA/AcrB/TolC accessions, reviewed status, symbols and K-12 taxonomy agree. All source interactor IDs and the three PDB polymer mappings match. CPX reference provenance remains distinct from engineered experimental constructs.

### Efflux activity and citation specificity

evidence: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

Xenobiotic export through the AcrB/AcrA/TolC conduit matches GO, CPX and the primary study. Native proton-coupling comments distinguish probable from directly supported assertions. Ligand-state AcrABZ data are not treated as the composition of apo 5V5S.

### Coarse explicitly non-mechanistic graph

graph: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

The graph’s stated NON_MECHANISTIC binding/recruitment/transport model agrees with the primary study and native subunit descriptions. It does not claim a new kinetic assembly order or stoichiometric measurement beyond its sources.

### K-12 composition and broader E. coli definition

scope: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

The exact K-12 canonical example derives from CPX-4263. The record’s E. coli scope is compatible with the referenced pump, while deposited source taxon 562 and C43(DE3) expression are not silently equated with the K-12 example.

### Full target and present grounding task

completeness: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

All source-composition fields, component rows, graph, open discussion and historical corrections were reviewed. The current AcrA family gap is resolvable; no automatic extra AcrZ component is required for the explicitly scoped AcrAB-TolC record. No images or verbatim snippets occur.

## Findings

### F1: Resolve the available exact AcrA family grounding

minor / open / confirmed; issue key: acrab-acra-family-grounding.

The component and open discussion retain AcrA as reviewed-label-only pending an exact family. IPR058628 now supplies the named AcrA family matching P0AE06 and the curated adaptor role. This finding concerns the current resolvable task, not the accuracy of its historical verification statement.

## Recommended Actions And Acceptance Checks

### A1

Ground AcrA to its verified family and narrow the remaining open grounding task to AcrB. Preserve exact protein references, source stoichiometry and the distinction between a protein family and the complete pump.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | Protein-family identity is distinct from an assembled complex. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic or transport function. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| micro43-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000148,GO:0003843,GO:0009277,GO:0031469,GO:0031472,GO:0042910,GO:0050215,GO:0051144,GO:0071970,GO:1990281; Complete exact GO1990281/0042910 names/definitions/active status. | supports | GO1990281 is the efflux-pump-complex parent and GO0042910 the xenobiotic transmembrane transporter activity. Neither is substituted for the exact locally identified AcrAB-TolC complex. |
| micro43-cpx | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4263; Complete native complex identity, taxon, assembly/composition, all three participants and stoichiometry/interactor IDs, evidence, properties and cross-references. | supports | CPX-4263 exactly identifies the E. coli K-12 AcrAB-TolC heterododecamer: six P0AE06/AcrA, three P31224/AcrB and three P02930/TolC, with the retained interactor IDs and ECO0000353 physical-interaction evidence. GO0042910, PMID28355133 and PDB5V5S cross-references are present. |
| micro43-pmid28355133 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28355133+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED28355133: An allosteric transport mechanism for the AcrAB-TolC multidrug efflux pump. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro43-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 83333 identifies Escherichia coli K-12 at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro43-pdb5V5S | https://data.rcsb.org/rest/v1/core/entry/5V5S; Native entry identity and primary citation; no independent map refinement. | supports | 5V5S is the Wang2017 apo AcrAB-TolC cryo-EM entry; exact publication DOI/PMID and structure identity match. |
| micro43-pdb5V5S-assembly1 | https://data.rcsb.org/rest/v1/core/assembly/5V5S/1; rcsb_assembly_info; pdbx_struct_assembly and oligomeric count/details. | supports | The deposited assembly is a twelve-subunit dodecamer. Its software-defined assembly record is not a separate depletion-based test of biological assembly necessity. |
| micro43-pdb5V5S-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/1; Exact UniProt reference_sequence_identifiers, polymer identifiers/chains and organism-source fields. | supports | Polymer entity 1 maps to P02930 with 3 chains in the deposited structure. Source-organism metadata are E. coli and genetically engineered; they do not independently specify K-12 as the experimental expression strain. |
| micro43-pdb5V5S-entity2 | https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/2; Exact UniProt reference_sequence_identifiers, polymer identifiers/chains and organism-source fields. | supports | Polymer entity 2 maps to P0AE06 with 6 chains in the deposited structure. Source-organism metadata are E. coli and genetically engineered; they do not independently specify K-12 as the experimental expression strain. |
| micro43-pdb5V5S-entity3 | https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/3; Exact UniProt reference_sequence_identifiers, polymer identifiers/chains and organism-source fields. | supports | Polymer entity 3 maps to P31224 with 3 chains in the deposited structure. Source-organism metadata are E. coli and genetically engineered; they do not independently specify K-12 as the experimental expression strain. |
| micro43-legacy-PMC5404916 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5404916/; Genuine primary HTML; entire s1, s2-1, s2-2, s2-3, s3, s4-1, s4-2 and s4-9 independently read. Interface details in s2-4, figure pixels and supplementary data not certified. | supports | Cryo-EM supports the tripartite 6:3:3 architecture, AcrA bridge and transport-coupled conformations. The apo 5V5S preparation uses engineered disulfide-stabilized AcrA/AcrB, while ligand-state experiments use distinct AcrABZ fusion preparations. Expression in C43(DE3) lacking acrAB is not the K-12 reference-protein provenance of CPX-4263. |
| micro43-up-P0AE06 | https://rest.uniprot.org/uniprotkb/P0AE06.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Complete FUNCTION and SUBUNIT text/comments were also read. | supports | P0AE06 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['acrA']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. Native FUNCTION/SUBUNIT comments preserve measured versus probable/inferred transport and assembly wording. |
| micro43-up-P31224 | https://rest.uniprot.org/uniprotkb/P31224.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Complete FUNCTION and SUBUNIT text/comments were also read. | supports | P31224 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['acrB']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. Native FUNCTION/SUBUNIT comments preserve measured versus probable/inferred transport and assembly wording. |
| micro43-up-P02930 | https://rest.uniprot.org/uniprotkb/P02930.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Complete FUNCTION and SUBUNIT text/comments were also read. | supports | P02930 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['tolC']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. Native FUNCTION/SUBUNIT comments preserve measured versus probable/inferred transport and assembly wording. |
| micro43-ipr-IPR058628 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058628/; Complete metadata accession/type/name/description/member databases/hierarchy. | supports | IPR058628 is the exact Multidrug efflux pump subunit AcrA family. Its native description matches the AcrA adaptor identity and supplies a current source-neutral grounding candidate. |
| micro43-ipr-IPR058622 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058622/; Complete metadata accession/type/name/description/member databases/hierarchy. | supports | IPR058622 is the exact TolC outer-membrane channel family already used by this record. Its family breadth does not make TolC exclusive to AcrAB. |
| micro43-ipr-IPR004764 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004764/; Complete metadata accession/type/name/description/hierarchy. | supports | The MdtF-like RND entry covers a broader transporter family, including distinct pump contexts. It is not used as an exact AcrB-only replacement. |
| schema-result | just validate data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml |
| strict-result | just validate-strict data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/acrab_tolc_multidrug_efflux_transport_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/acrab_tolc_multidrug_efflux_transport_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/acrab_tolc_multidrug_efflux_transport_complex-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml; Complete read-only focused native graphs log | supports | data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml  (cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex)<br>  acrab_tolc_xenobiotic_efflux	acra	COVERED	-&gt;acra_periplasmic_adaptor (UniProtKB:P0AE06)<br>  acrab_tolc_xenobiotic_efflux	acrb	COVERED	-&gt;acrb_inner_membrane_transporter (UniProtKB:P31224)<br>  acrab_tolc_xenobiotic_efflux	tolc	COVERED	-&gt;tolc_outer_membrane_channel (UniProtKB:P02930)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 13 collected target identifiers returned OK. ECO:0000353: SKIPPED; Native Complex Portal CPX-4263 explicitly returns this exact ECO identifier with physical interaction evidence description. Dedicated ECO authority metadata was not separately retrieved; no biological inference follows merely from this code.; PDB:5V5S: SKIPPED; Native PDB entry and assembly1 verify engineered apo AcrAB-TolC structure, 6:3:3 subunit stoichiometry and exact identity; the ligand-bound AcrABZ comparator is kept distinct.; PMID:28355133: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex: SKIPPED; Frozen current target identity matches exactly one maintained record in an ignored-inclusive local identifier search. This local identity verification does not establish exhaustive ontology absence. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Primary reading is confined to the listed Wang2017 sections. No raw cryo-EM maps, figure pixels, unlisted atomic-interface section or supplements were reanalyzed.
- 5V5S is an engineered disulfide-stabilized apo complex; separate ligand-state AcrABZ fusions and C43(DE3) expression are not native K-12 whole-cell assembly measurements.
- The three ESSENTIAL labels remain unknown as independent formation-necessity claims. Membership, catalytic contribution and intact engineered assembly do not by themselves establish a depletion phenotype.
- Native broader MdtF/RND family metadata do not provide an exact AcrB-only grounding in this bounded candidate check.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these complex identity, protein family, assembly and enzyme or transport claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T042555Z-acrab-tolc-multidrug-efflux-transport-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of acrab tolc multidrug efflux transport complex
started_at: '2026-10-22T03:58:53Z'
finished_at: '2026-10-22T04:25:55Z'
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
summary: One minor correction resolves AcrA’s exact family grounding. The tripartite
  pump, source composition, native identities and coarse transport model are supported;
  formation necessity remains untested by the inspected evidence.
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
  - path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    sha256: f6cb94dea736f627892fc1cdc8a1f44668752e605644876e937a6f11ecc0f62d
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
- target_id: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  label: AcrAB-TolC multidrug efflux transport complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; no neighboring scientific-record verdict
    is imported. Exact authority, all current component/function/graph/source placements,
    taxonomic scope, formation semantics, history and discussions were reviewed.
  selection: Batch43 fixed strict path order, index 10; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just validate data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just validate-strict data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/acrab_tolc_multidrug_efflux_transport_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-proteins
- check_id: native-graphs
  name: Focused native graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - micro43-go
  - micro43-cpx
  - micro43-pmid28355133
  - micro43-tax83333
  - micro43-pdb5V5S
  - micro43-pdb5V5S-assembly1
  - micro43-pdb5V5S-entity1
  - micro43-pdb5V5S-entity2
  - micro43-pdb5V5S-entity3
  - micro43-legacy-PMC5404916
  - micro43-up-P0AE06
  - micro43-up-P31224
  - micro43-up-P02930
  - micro43-ipr-IPR058628
  - micro43-ipr-IPR058622
  - micro43-ipr-IPR004764
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: '9 of 13 collected target identifiers returned OK. ECO:0000353: SKIPPED;
    Native Complex Portal CPX-4263 explicitly returns this exact ECO identifier with
    physical interaction evidence description. Dedicated ECO authority metadata was
    not separately retrieved; no biological inference follows merely from this code.;
    PDB:5V5S: SKIPPED; Native PDB entry and assembly1 verify engineered apo AcrAB-TolC
    structure, 6:3:3 subunit stoichiometry and exact identity; the ligand-bound AcrABZ
    comparator is kept distinct.; PMID:28355133: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport
    failure. Biological support remains bounded by the separately recorded abstract
    or primary-body sections; identity resolution alone is not confirmation of every
    attached claim.; cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex:
    SKIPPED; Frozen current target identity matches exactly one maintained record
    in an ignored-inclusive local identifier search. This local identity verification
    does not establish exhaustive ontology absence. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro43-cpx
  - micro43-pdb5V5S
  - micro43-pdb5V5S-assembly1
  - micro43-pmid28355133
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
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
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:17:31Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:17:31Z'
  support: context_only
  summary: Protein-family identity is distinct from an assembled complex. ESSENTIAL
    concerns failure of structure formation, not merely loss of catalytic or transport
    function.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:17:31Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: micro43-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000148,GO:0003843,GO:0009277,GO:0031469,GO:0031472,GO:0042910,GO:0050215,GO:0051144,GO:0071970,GO:1990281
  locator: Complete exact GO1990281/0042910 names/definitions/active status.
  accessed_at: '2026-10-22T04:09:03.496578Z'
  support: supports
  summary: GO1990281 is the efflux-pump-complex parent and GO0042910 the xenobiotic
    transmembrane transporter activity. Neither is substituted for the exact locally
    identified AcrAB-TolC complex.
  snapshot_sha256: d40f3f203eaad9efb2ceba4c52209731a537cf62d0528a69af69d7b7d9c252f6
- evidence_id: micro43-cpx
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4263
  locator: Complete native complex identity, taxon, assembly/composition, all three
    participants and stoichiometry/interactor IDs, evidence, properties and cross-references.
  accessed_at: '2026-10-22T04:09:11.121578Z'
  support: supports
  summary: 'CPX-4263 exactly identifies the E. coli K-12 AcrAB-TolC heterododecamer:
    six P0AE06/AcrA, three P31224/AcrB and three P02930/TolC, with the retained interactor
    IDs and ECO0000353 physical-interaction evidence. GO0042910, PMID28355133 and
    PDB5V5S cross-references are present.'
  snapshot_sha256: 1a9e770385d9bc12e054f7d93f09f0e0a5cde7977ed42367698b0eaa004c9fad
- evidence_id: micro43-pmid28355133
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28355133+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:09:07.665738Z'
  support: supports
  summary: 'Unique MED28355133: An allosteric transport mechanism for the AcrAB-TolC
    multidrug efflux pump. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 1d45eec07db97525be200ba5604b86c5e73012e734e14ecf4bedb88450b63221
- evidence_id: micro43-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:09:06.395271Z'
  support: supports
  summary: ENA taxId 83333 identifies Escherichia coli K-12 at rank strain; aliases
    and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro43-pdb5V5S
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/5V5S
  locator: Native entry identity and primary citation; no independent map refinement.
  accessed_at: '2026-10-22T04:09:11.187181Z'
  support: supports
  summary: 5V5S is the Wang2017 apo AcrAB-TolC cryo-EM entry; exact publication DOI/PMID
    and structure identity match.
  snapshot_sha256: 033ab55d54cac2f6c3941468b74921b8cf4fafe5bc1460fa5ca869011002f3fb
- evidence_id: micro43-pdb5V5S-assembly1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/5V5S/1
  locator: rcsb_assembly_info; pdbx_struct_assembly and oligomeric count/details.
  accessed_at: '2026-10-22T04:09:11.222390Z'
  support: supports
  summary: The deposited assembly is a twelve-subunit dodecamer. Its software-defined
    assembly record is not a separate depletion-based test of biological assembly
    necessity.
  snapshot_sha256: 23c8d8106feeded729eef819fdb13d19ec2699341ebea89d07f3f181fa9f8de1
- evidence_id: micro43-pdb5V5S-entity1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/1
  locator: Exact UniProt reference_sequence_identifiers, polymer identifiers/chains
    and organism-source fields.
  accessed_at: '2026-10-22T04:09:11.264515Z'
  support: supports
  summary: Polymer entity 1 maps to P02930 with 3 chains in the deposited structure.
    Source-organism metadata are E. coli and genetically engineered; they do not independently
    specify K-12 as the experimental expression strain.
  snapshot_sha256: 772e77504605462f2a6a86427f46f91c4107bb13e6b97b3ce1f0d287fede2512
- evidence_id: micro43-pdb5V5S-entity2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/2
  locator: Exact UniProt reference_sequence_identifiers, polymer identifiers/chains
    and organism-source fields.
  accessed_at: '2026-10-22T04:09:11.264757Z'
  support: supports
  summary: Polymer entity 2 maps to P0AE06 with 6 chains in the deposited structure.
    Source-organism metadata are E. coli and genetically engineered; they do not independently
    specify K-12 as the experimental expression strain.
  snapshot_sha256: dcf4b6dfb04f35ae0af2422d351aae0b18e857fd4cca276e465848b7446be9fc
- evidence_id: micro43-pdb5V5S-entity3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/3
  locator: Exact UniProt reference_sequence_identifiers, polymer identifiers/chains
    and organism-source fields.
  accessed_at: '2026-10-22T04:09:11.280813Z'
  support: supports
  summary: Polymer entity 3 maps to P31224 with 3 chains in the deposited structure.
    Source-organism metadata are E. coli and genetically engineered; they do not independently
    specify K-12 as the experimental expression strain.
  snapshot_sha256: 91573424724bf707c099ee63012acb3b8de2c86d3700ef84c72c661d1c716052
- evidence_id: micro43-legacy-PMC5404916
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5404916/
  locator: Genuine primary HTML; entire s1, s2-1, s2-2, s2-3, s3, s4-1, s4-2 and s4-9
    independently read. Interface details in s2-4, figure pixels and supplementary
    data not certified.
  accessed_at: '2026-10-22T04:10:07.206063Z'
  support: supports
  summary: Cryo-EM supports the tripartite 6:3:3 architecture, AcrA bridge and transport-coupled
    conformations. The apo 5V5S preparation uses engineered disulfide-stabilized AcrA/AcrB,
    while ligand-state experiments use distinct AcrABZ fusion preparations. Expression
    in C43(DE3) lacking acrAB is not the K-12 reference-protein provenance of CPX-4263.
  snapshot_sha256: 002f74f5b1bbbd45ab7b3e4ea6c1bd57e076e1f67de1c11c386f8e658545b99e
- evidence_id: micro43-up-P0AE06
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AE06.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Complete
    FUNCTION and SUBUNIT text/comments were also read.
  accessed_at: '2026-10-22T04:09:09.006215Z'
  support: supports
  summary: P0AE06 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['acrA'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge. Native FUNCTION/SUBUNIT comments
    preserve measured versus probable/inferred transport and assembly wording.
  snapshot_sha256: 3353ebe0339b2686335d36fa720ceee4c8808ae38f2a2c975d3ef3cdba6cdb9d
- evidence_id: micro43-up-P31224
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P31224.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Complete
    FUNCTION and SUBUNIT text/comments were also read.
  accessed_at: '2026-10-22T04:09:09.339828Z'
  support: supports
  summary: P31224 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['acrB'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge. Native FUNCTION/SUBUNIT comments
    preserve measured versus probable/inferred transport and assembly wording.
  snapshot_sha256: cd8e89b948d93accd44fa9e734affcae68c35ac537710cbca4aedd1ea46d47ae
- evidence_id: micro43-up-P02930
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P02930.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Complete
    FUNCTION and SUBUNIT text/comments were also read.
  accessed_at: '2026-10-22T04:09:08.342290Z'
  support: supports
  summary: P02930 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['tolC'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge. Native FUNCTION/SUBUNIT comments
    preserve measured versus probable/inferred transport and assembly wording.
  snapshot_sha256: cef14f6af1999fe0b5218d959cca8788ec00afc1b145201ba48344a4b15bbb04
- evidence_id: micro43-ipr-IPR058628
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058628/
  locator: Complete metadata accession/type/name/description/member databases/hierarchy.
  accessed_at: '2026-10-22T04:09:49.522195Z'
  support: supports
  summary: IPR058628 is the exact Multidrug efflux pump subunit AcrA family. Its native
    description matches the AcrA adaptor identity and supplies a current source-neutral
    grounding candidate.
  snapshot_sha256: 122db3dd9fef2511493cb2808549931269cfb075d3fdb63230bf5d05f01c1b9b
- evidence_id: micro43-ipr-IPR058622
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058622/
  locator: Complete metadata accession/type/name/description/member databases/hierarchy.
  accessed_at: '2026-10-22T04:09:05.823477Z'
  support: supports
  summary: IPR058622 is the exact TolC outer-membrane channel family already used
    by this record. Its family breadth does not make TolC exclusive to AcrAB.
  snapshot_sha256: d3c58cbb9737d5f395f703b634f84df048f355555af2b817f321a5e474b8e310
- evidence_id: micro43-ipr-IPR004764
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004764/
  locator: Complete metadata accession/type/name/description/hierarchy.
  accessed_at: '2026-10-22T04:09:49.522419Z'
  support: supports
  summary: The MdtF-like RND entry covers a broader transporter family, including
    distinct pump contexts. It is not used as an exact AcrB-only replacement.
  snapshot_sha256: 4c678f9531dce3a032e17ba34b6f2578dee02575c7431a9bfb9bd2df4e9a5aeb
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:54Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml'
  snapshot_sha256: 9acac2ebbcc94ac0a2a0cecdf96e18288a9f952b07d983282ed955f2cab86388
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/acrab_tolc_multidrug_efflux_transport_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:55Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml\
    \ --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/acrab_tolc_multidrug_efflux_transport_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/acrab_tolc_multidrug_efflux_transport_complex-strict.tsv"
  snapshot_sha256: 1eea23e8cf68a9a223bb653e30ba573a37a82f592c722becb0c428c0790985aa
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T04:09:31.421420Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T04:09:31.871468Z'
  support: supports
  summary: "data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml\
    \  (cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex)\n  acrab_tolc_xenobiotic_efflux\t\
    acra\tCOVERED\t->acra_periplasmic_adaptor (UniProtKB:P0AE06)\n  acrab_tolc_xenobiotic_efflux\t\
    acrb\tCOVERED\t->acrb_inner_membrane_transporter (UniProtKB:P31224)\n  acrab_tolc_xenobiotic_efflux\t\
    tolc\tCOVERED\t->tolc_outer_membrane_channel (UniProtKB:P02930)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     3  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     3  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: d006bc9e9c113add93b358d1af24eb05ca200ab4c477df0f514cbcca129b7518
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '9 of 13 collected target identifiers returned OK. ECO:0000353: SKIPPED;
    Native Complex Portal CPX-4263 explicitly returns this exact ECO identifier with
    physical interaction evidence description. Dedicated ECO authority metadata was
    not separately retrieved; no biological inference follows merely from this code.;
    PDB:5V5S: SKIPPED; Native PDB entry and assembly1 verify engineered apo AcrAB-TolC
    structure, 6:3:3 subunit stoichiometry and exact identity; the ligand-bound AcrABZ
    comparator is kept distinct.; PMID:28355133: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport
    failure. Biological support remains bounded by the separately recorded abstract
    or primary-body sections; identity resolution alone is not confirmation of every
    attached claim.; cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex:
    SKIPPED; Frozen current target identity matches exactly one maintained record
    in an ignored-inclusive local identifier search. This local identity verification
    does not establish exhaustive ontology absence. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
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
  topic: Specific local identity and generic parent
  outcome: supported
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: The local identifier denotes the exact CPX-supported AcrAB-TolC pump rather
    than claiming the broad GO parent is synonymous. Definition, heterododecamer and
    source-composition import are correct.
  evidence_ids:
  - record
  - micro43-go
  - micro43-cpx
- assessment_id: composition
  area: grounding
  topic: Tripartite stoichiometry and family grounding
  outcome: concern
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: The three component roles and 6:3:3 counts match CPX and deposited structure.
    TolC family grounding is correct. AcrA now has an exact verified family; the broader
    AcrB candidate is insufficient for forced replacement.
  evidence_ids:
  - record
  - curation
  - micro43-cpx
  - micro43-pdb5V5S
  - micro43-pdb5V5S-assembly1
  - micro43-ipr-IPR058628
  - micro43-ipr-IPR058622
  - micro43-ipr-IPR004764
  - micro43-pdb5V5S-entity1
  - micro43-pdb5V5S-entity2
  - micro43-pdb5V5S-entity3
- assessment_id: necessity
  area: grounding
  topic: Individual formation necessity remains unresolved
  outcome: unknown
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: All three components are present in the defined tripartite pump, but CPX
    composition and engineered intact cryo-EM structures do not independently test
    the record’s three ESSENTIAL formation labels. This review does not redefine those
    labels as catalytic importance or mere membership and does not infer a contradiction
    solely from missing depletion experiments.
  evidence_ids:
  - record
  - schema
  - micro43-cpx
  - micro43-legacy-PMC5404916
  - micro43-pdb5V5S-assembly1
- assessment_id: proteins
  area: grounding
  topic: Native references and source context
  outcome: supported
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: AcrA/AcrB/TolC accessions, reviewed status, symbols and K-12 taxonomy agree.
    All source interactor IDs and the three PDB polymer mappings match. CPX reference
    provenance remains distinct from engineered experimental constructs.
  evidence_ids:
  - record
  - micro43-cpx
  - micro43-tax83333
  - micro43-legacy-PMC5404916
  - micro43-up-P0AE06
  - micro43-up-P31224
  - micro43-up-P02930
  - micro43-pdb5V5S-entity1
  - micro43-pdb5V5S-entity2
  - micro43-pdb5V5S-entity3
- assessment_id: functions
  area: evidence
  topic: Efflux activity and citation specificity
  outcome: supported
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: Xenobiotic export through the AcrB/AcrA/TolC conduit matches GO, CPX and
    the primary study. Native proton-coupling comments distinguish probable from directly
    supported assertions. Ligand-state AcrABZ data are not treated as the composition
    of apo 5V5S.
  evidence_ids:
  - record
  - micro43-go
  - micro43-cpx
  - micro43-legacy-PMC5404916
  - micro43-up-P0AE06
  - micro43-up-P31224
  - micro43-up-P02930
- assessment_id: graph
  area: graph
  topic: Coarse explicitly non-mechanistic graph
  outcome: supported
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: The graph’s stated NON_MECHANISTIC binding/recruitment/transport model
    agrees with the primary study and native subunit descriptions. It does not claim
    a new kinetic assembly order or stoichiometric measurement beyond its sources.
  evidence_ids:
  - record
  - micro43-cpx
  - micro43-legacy-PMC5404916
  - micro43-up-P0AE06
  - micro43-up-P31224
  - micro43-up-P02930
- assessment_id: scope
  area: scope
  topic: K-12 composition and broader E. coli definition
  outcome: supported
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: The exact K-12 canonical example derives from CPX-4263. The record’s E.
    coli scope is compatible with the referenced pump, while deposited source taxon
    562 and C43(DE3) expression are not silently equated with the K-12 example.
  evidence_ids:
  - record
  - micro43-cpx
  - micro43-tax83333
  - micro43-legacy-PMC5404916
  - micro43-pdb5V5S
  - micro43-pdb5V5S-entity1
  - micro43-pdb5V5S-entity2
  - micro43-pdb5V5S-entity3
- assessment_id: coverage
  area: completeness
  topic: Full target and present grounding task
  outcome: supported
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: All source-composition fields, component rows, graph, open discussion and
    historical corrections were reviewed. The current AcrA family gap is resolvable;
    no automatic extra AcrZ component is required for the explicitly scoped AcrAB-TolC
    record. No images or verbatim snippets occur.
  evidence_ids:
  - record
  - micro43-cpx
  - micro43-legacy-PMC5404916
  - micro43-ipr-IPR058628
  - micro43-ipr-IPR058622
  - micro43-ipr-IPR004764
findings:
- finding_id: F1
  issue_key: acrab-acra-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the available exact AcrA family grounding
  description: The component and open discussion retain AcrA as reviewed-label-only
    pending an exact family. IPR058628 now supplies the named AcrA family matching
    P0AE06 and the curated adaptor role. This finding concerns the current resolvable
    task, not the accuracy of its historical verification statement.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  field_paths:
  - components[0].grounding
  - components[0].grounding_status
  - components[0].grounding_notes
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - micro43-ipr-IPR058628
  - micro43-up-P0AE06
  - micro43-cpx
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: The protein and pump identities are correct; this is a bounded
    source-neutral family-grounding correction. AcrB is left unresolved rather than
    forced into a broader RND family.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  description: Ground AcrA to its verified family and narrow the remaining open grounding
    task to AcrB. Preserve exact protein references, source stoichiometry and the
    distinction between a protein family and the complete pump.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
limitations:
- Primary reading is confined to the listed Wang2017 sections. No raw cryo-EM maps,
  figure pixels, unlisted atomic-interface section or supplements were reanalyzed.
- 5V5S is an engineered disulfide-stabilized apo complex; separate ligand-state AcrABZ
  fusions and C43(DE3) expression are not native K-12 whole-cell assembly measurements.
- The three ESSENTIAL labels remain unknown as independent formation-necessity claims.
  Membership, catalytic contribution and intact engineered assembly do not by themselves
  establish a depletion phenotype.
- Native broader MdtF/RND family metadata do not provide an exact AcrB-only grounding
  in this bounded candidate check.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these complex identity, protein family, assembly
  and enzyme or transport claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
