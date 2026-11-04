# Methionine importing abc transporter complex scientific review

- Review: 20261022T082337Z-methionine-importing-abc-transporter-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:58:03Z
- Finished UTC: 2026-10-22T08:23:37Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The MetNIQ identity and2:2:1 composition are supported. Two minors resolve exact MetI/MetQ family mappings and clarify the definition’s translocation subject; model and preparation limits remain explicit.

## Scope And Provenance

Exactly one complete maintained target plus frozen guidance and protein-example skill. Actual source-reading extents appear per evidence row; no unlisted primary experiments or assets are certified.

Selection: Target 8 of batch59, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990197 | data/structures/other/methionine_importing_abc_transporter_complex.yaml | maintained | methionine-importing ABC transporter complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990197 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990197 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:1990197 | Native focused check passed; biological claims assessed separately. |
| Native verify | passed | True | GO:1990197 | Native focused check passed; biological claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:1990197 | No expression-module inference is used. |
| Claim-level scientific review | passed | True | GO:1990197 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990197 | 11 of 14 collected target identifiers returned OK. PDB:6CVL: SKIPPED; Native released RCSB entry 6CVL: Crystal structure of the Escherichia coli ATPgS-bound MetNI methionine ABC transporter in complex with its MetQ binding protein; primary DOI10.1073/pnas.1811003115. No coordinate reanalysis is implied.; PMID:22095702: UNREACHABLE; Native Europe PMC uniquely identifies MED22095702: Inward facing conformations of the MetNI methionine ABC transporter: Implications for the mechanism of transinhibition. (2012); DOI10.1002/pro.765. Identifier transport verification is distinct from separately scoped primary-source reading.; PMID:30352853: UNREACHABLE; Native Europe PMC uniquely identifies MED30352853: Noncanonical role for the binding protein in substrate uptake by the MetNI methionine ATP Binding Cassette (ABC) transporter. (2018); DOI10.1073/pnas.1811003115. Identifier transport verification is distinct from separately scoped primary-source reading. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990197 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990197 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990197 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990197 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990197 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Three classes and2:2:1 deposited assembly

identity: supported. Targets: GO:1990197.

The native GO ancestor, exact three proteins/aliases and PDB assembly support the canonical2:2:1 E.coli complex. K12 describes gene origin; engineered substitutions and the separate expression/uptake backgrounds are retained as preparation limits.

### Exact MetI and MetQ mappings

grounding: concern. Targets: GO:1990197.

The two label-only rows have exact NCBIfam alternatives independently joined by their native protein cross-references. Broader NlpA/ABC-domain candidates remain distinct.

### MetQ delivery versus ATP-driven translocation

scope: concern. Targets: GO:1990197.

The copied GO final sentence grammatically makes MetQ capable of ATP-dependent periplasm-to-cytoplasm transport. The primary papers assign delivery/access to MetQ and transmembrane ATP-coupled transport to the MetNI system; changing the sentence subject preserves the supported complex identity.

### Coarse canonical transport and noncanonical alternative

graph: supported. Targets: GO:1990197.

Docking, ATP coupling and the two methionine transport functions are supported at the graph’s coarse mechanistic level.6CVL captures an engineered apo-MetQ state, not observed substrate delivery; Nguyen2018 explicitly models both canonical and noncanonical pathways, while Johnson2012 comparisons are not time-resolved motion measurements. The current general delivery role is not treated as an exclusive mechanism.

### Transport function is not formation necessity

grounding: unknown. Targets: GO:1990197.

MetQ deletion strongly reduces uptake, and structures establish assembled membership. Neither readout independently supplies universal individual formation necessity; the maintained UNKNOWN values remain appropriate.

### Whole maintained target and declared source coverage

completeness: supported. Targets: GO:1990197.

Every maintained field, source note, graph and discussion was inspected at the declared extents. Optional inventory/contact enrichment and acknowledged unknowns alone do not create findings.

## Findings

### F1: Ground the exact MetI and MetQ families

minor / open / confirmed; issue key: metniq-exact-subunit-families.

Both rows remain REVIEWED_LABEL_ONLY because shared InterPro entries were considered, while exact native NCBIfam full families and independent protein membership resolve their retained classes.

### F2: Assign ATP-dependent translocation to the transporter

minor / open / confirmed; issue key: metniq-definition-transport-subject.

The last definition sentence currently makes MetQ alone the subject of ATP-dependent membrane translocation. This is faithful to current GO wording, but disagrees with the clear division of roles in its cited primary source and the record’s own component roles.

## Recommended Actions And Acceptance Checks

### A1

Use NCBIfam:NF008049 for MetI and NCBIfam:NF008285 for MetQ, preserving correct examples,2:2:1 stoichiometry and unresolved individual necessity.

- Join each native family to its own protein cross-reference; do not substitute broad NlpA or a shared transporter domain.
- Preserve supported source-specific claims and pass applicable native gates.

### A2

Clarify that MetQ binds/presents substrate and the MetNI-containing complex performs ATP-dependent transport; retain the exact GO identity and add primary support for the clarified wording.

- Do not claim MetQ itself is the ATPase or transmembrane permease; preserve the source’s noncanonical access alternative.
- Preserve supported source-specific claims and pass applicable native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/methionine_importing_abc_transporter_complex.yaml; Entire maintained record, all examples, evidence, graphs, properties, images, history and discussions | context_only | Every maintained field was read. Historical curation statements are context, not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component/ProteinExample, EssentialityEnum, PresenceEnum and graph-scope contracts | context_only | Formation necessity differs from function, viability and membership. COMMON means most members with losses the exception; VARIABLE means lineage- or strain-level patchiness, not cell-type-specific visibility. |
| curation | docs/CURATION.md; Component grounding and REVIEWED_LABEL_ONLY at159–160 | context_only | Exact full-family mappings differ from shared domains or broader paralog classes. Label-only is not merely uncurated in this pass. |
| complex59-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001401,GO:0005743,GO:0006935,GO:0015191,GO:0030117,GO:0030118,GO:0030119,GO:0030120,GO:0033232,GO:0061617,GO:0098561,GO:0098796,GO:0098800,GO:0140275,GO:1902495,GO:1990197; Complete target-relevant native definitions/synonyms and typed relationships; unrelated combined entries not attributed to this target | supports | GO1990197 identifies the MetNIQ example and current synonyms; its last definition sentence grammatically attributes ATP-dependent translocation to MetQ. This faithfully inherited wording is compared separately with the primary source. Transport-function terms retain their native identities. |
| complex59-agent-go-1990197-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990197/ancestors?relations=is_a; Complete is_a-only ancestor response | supports | The is_a-only closure supplies classification ancestry for this exact target. It does not establish parthood, experimental assembly necessity or prevalence. |
| complex59-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete ENA identity/names/lineage | supports | Taxon83333: Escherichia coli K-12, rank strain; exact native names and lineage inspected. |
| complex59-agent-protein-P28635 | https://rest.uniprot.org/uniprotkb/P28635.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P28635, D-methionine-binding lipoprotein MetQ; primary genes metQ, synonyms yaeC, taxon83333. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex59-agent-protein-P30750 | https://rest.uniprot.org/uniprotkb/P30750.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P30750, Methionine import ATP-binding protein MetN; primary genes metN, synonyms abc, taxon83333. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex59-agent-protein-P31547 | https://rest.uniprot.org/uniprotkb/P31547.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): P31547, D-methionine transport system permease protein MetI; primary genes metI, synonyms yaeE, taxon83333. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex59-agent-query-abc | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Aabc%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P30750. Every returned identity/gene/organism was read. |
| complex59-agent-query-metI | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmetI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P31547. Every returned identity/gene/organism was read. |
| complex59-agent-query-metN | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmetN%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P30750. Every returned identity/gene/organism was read. |
| complex59-agent-query-metQ | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmetQ%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P28635. Every returned identity/gene/organism was read. |
| complex59-agent-query-yaeC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AyaeC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P28635. Every returned identity/gene/organism was read. |
| complex59-agent-query-yaeE | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AyaeE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query results | supports | Exact native query returns 1 entry: P31547. Every returned identity/gene/organism was read. |
| complex59-agent-pmid-22095702 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22095702+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and available abstract | supports | MED22095702: Inward facing conformations of the MetNI methionine ABC transporter: Implications for the mechanism of transinhibition. Johnson E, Nguyen PT, Yeates TO, Rees DC. (2012), DOI10.1002/pro.765. Exact metadata and complete available abstract read; this does not claim body access.  |
| complex59-agent-pmid-30352853 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A30352853+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and available abstract | supports | MED30352853: Noncanonical role for the binding protein in substrate uptake by the MetNI methionine ATP Binding Cassette (ABC) transporter. Nguyen PT, Lai JY, Lee AT, Kaiser JT, Rees DC. (2018), DOI10.1073/pnas.1811003115. Exact metadata and complete available abstract read; this does not claim body access.  |
| complex59-agent-johnson2012-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3323783/; Introduction sec1, Results sec3/4/8/9, complete Discussion sec10, Methods sec12/13 and all captions embedded in those sections; no unlisted Results/Methods, pixels or supplements. | supports | Johnson2012 identifies two MetN plus two MetI subunits and a separate MetQ delivery protein. Inward-facing structures and comparisons support a qualified coupling/transinhibition model; the paper explicitly distinguishes proposed motions from measured dynamics. |
| complex59-agent-nguyen2018-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6233128/fullTextXML; Results/Discussion s1–s6, Methods s8/s14, Table1 and Fig1–9 captions embedded there; no figure pixels or supplements. | supports | Nguyen2018 measures D-selenomethionine uptake and resolves an ATPgammaS-bound engineered MetNIQ complex. Apo-MetQ association supports a proposed noncanonical pathway; canonical high-affinity delivery remains a comparison model. K12 gene origin, BL21 expression and BW2115 uptake background are distinct. |
| complex59-agent-pdb-entry-6CVL | https://data.rcsb.org/rest/v1/core/entry/6CVL; Entry title and complete primary-citation identity | supports | PDB6CVL is the Nguyen2018 ATPgammaS-bound E.coli MetNIQ structure. |
| complex59-agent-pdb-assembly-6CVL-1 | https://data.rcsb.org/rest/v1/core/assembly/6CVL/1; Complete assembly1 composition/counts/generation fields | supports | Biological assembly1 contains five protein instances from three entity classes; deposited nonpolymer ligands are not protein subunits. |
| complex59-agent-pdb-polymer_entity-6CVL-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/6CVL/1; Protein identity/source organism/genes, chain multiplicity, mutation count and UniProt mapping | supports | Entity1 is MetN, with 2 deposited copies, source taxon83333, UniProtP30750 and 2 annotated sequence mutations. The source is genetically engineered. |
| complex59-agent-pdb-polymer_entity-6CVL-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/6CVL/2; Protein identity/source organism/genes, chain multiplicity, mutation count and UniProt mapping | supports | Entity2 is MetI, with 2 deposited copies, source taxon83333, UniProtP31547 and 0 annotated sequence mutations. The source is genetically engineered. |
| complex59-agent-pdb-polymer_entity-6CVL-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/6CVL/3; Protein identity/source organism/genes, chain multiplicity, mutation count and UniProt mapping | supports | Entity3 is MetQ, with 1 deposited copies, source taxon83333, UniProtP28635 and 1 annotated sequence mutations. The source is genetically engineered. |
| complex59-agent-ipr-IPR012692 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012692/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | IPR012692 is the retained proteobacterial MetN full-family class. |
| complex59-agent-ncbifam-NF008049 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF008049/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | NF008049 is the methionine ABC transporter permease MetI family. |
| complex59-agent-ncbifam-NF008285 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF008285/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | NF008285 is the methionine ABC transporter substrate-binding lipoprotein MetQ family. |
| complex59-agent-interpro-IPR004872 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004872/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | The NlpA lipoprotein family is broader than the MetQ-specific class. |
| schema-result | just validate data/structures/other/methionine_importing_abc_transporter_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/methionine_importing_abc_transporter_complex.yaml |
| strict-result | just validate-strict data/structures/other/methionine_importing_abc_transporter_complex.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methionine_importing_abc_transporter_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/methionine_importing_abc_transporter_complex.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methionine_importing_abc_transporter_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methionine_importing_abc_transporter_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/methionine_importing_abc_transporter_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/methionine_importing_abc_transporter_complex.yaml  (GO:1990197)<br>  metniq_methionine_import	metq_periplasmic_binding_protein	COVERED	-&gt;metq_periplasmic_binding_protein (UniProtKB:P28635)<br>  metniq_methionine_import	metn_atp_binding_subunit	COVERED	-&gt;metn_atp_binding_subunit (UniProtKB:P30750)<br>  metniq_methionine_import	meti_transmembrane_subunit	COVERED	-&gt;meti_transmembrane_subunit (UniProtKB:P31547)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/methionine_importing_abc_transporter_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/methionine_importing_abc_transporter_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 14 collected target identifiers returned OK. PDB:6CVL: SKIPPED; Native released RCSB entry 6CVL: Crystal structure of the Escherichia coli ATPgS-bound MetNI methionine ABC transporter in complex with its MetQ binding protein; primary DOI10.1073/pnas.1811003115. No coordinate reanalysis is implied.; PMID:22095702: UNREACHABLE; Native Europe PMC uniquely identifies MED22095702: Inward facing conformations of the MetNI methionine ABC transporter: Implications for the mechanism of transinhibition. (2012); DOI10.1002/pro.765. Identifier transport verification is distinct from separately scoped primary-source reading.; PMID:30352853: UNREACHABLE; Native Europe PMC uniquely identifies MED30352853: Noncanonical role for the binding protein in substrate uptake by the MetNI methionine ATP Binding Cassette (ABC) transporter. (2018); DOI10.1073/pnas.1811003115. Identifier transport verification is distinct from separately scoped primary-source reading. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five completed same-base batch26 global gates are integrated with exact manifest/input/log hashes verified; no fresh full-site QC is claimed from this sparse checkout.
- Only the explicitly listed source sections/assets were inspected. No unlisted supplements, atomic coordinates or raw experimental data were analyzed.
- No PDB coordinates or supplements were analyzed. The deposited mutant ATPgammaS complex is not a direct wild-type substrate-flux trajectory. Johnson2012 gene expression uses BL21-gold; Nguyen2018 separates K12 gene origin from BL21 expression and BW2115 uptake experiments.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes both clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T082337Z-methionine-importing-abc-transporter-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Methionine importing abc transporter complex scientific review
started_at: '2026-10-22T07:58:03Z'
finished_at: '2026-10-22T08:23:37Z'
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
summary: The MetNIQ identity and2:2:1 composition are supported. Two minors resolve
  exact MetI/MetQ family mappings and clarify the definition’s translocation subject;
  model and preparation limits remain explicit.
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
  - path: data/structures/other/methionine_importing_abc_transporter_complex.yaml
    sha256: d142adebc4594df832813af4688c91daa5e93e59681fc6cfdf08a885d95cdc37
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
- target_id: GO:1990197
  path: data/structures/other/methionine_importing_abc_transporter_complex.yaml
  label: methionine-importing ABC transporter complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methionine_importing_abc_transporter_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target plus frozen guidance and protein-example
    skill. Actual source-reading extents appear per evidence row; no unlisted primary
    experiments or assets are certified.
  selection: Target 8 of batch59, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990197
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990197
  command: just validate data/structures/other/methionine_importing_abc_transporter_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990197
  command: just validate-strict data/structures/other/methionine_importing_abc_transporter_complex.yaml
    --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methionine_importing_abc_transporter_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990197
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/methionine_importing_abc_transporter_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; biological claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:1990197
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/methionine_importing_abc_transporter_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; biological claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990197
  summary: No expression-module inference is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990197
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex59-agent-go
  - complex59-agent-go-1990197-ancestors
  - complex59-agent-tax-83333
  - complex59-agent-protein-P28635
  - complex59-agent-protein-P30750
  - complex59-agent-protein-P31547
  - complex59-agent-query-abc
  - complex59-agent-query-metI
  - complex59-agent-query-metN
  - complex59-agent-query-metQ
  - complex59-agent-query-yaeC
  - complex59-agent-query-yaeE
  - complex59-agent-pmid-22095702
  - complex59-agent-pmid-30352853
  - complex59-agent-johnson2012-legacy
  - complex59-agent-nguyen2018-xml
  - complex59-agent-pdb-entry-6CVL
  - complex59-agent-pdb-assembly-6CVL-1
  - complex59-agent-pdb-polymer_entity-6CVL-1
  - complex59-agent-pdb-polymer_entity-6CVL-2
  - complex59-agent-pdb-polymer_entity-6CVL-3
  - complex59-agent-ipr-IPR012692
  - complex59-agent-ncbifam-NF008049
  - complex59-agent-ncbifam-NF008285
  - complex59-agent-interpro-IPR004872
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990197
  summary: '11 of 14 collected target identifiers returned OK. PDB:6CVL: SKIPPED;
    Native released RCSB entry 6CVL: Crystal structure of the Escherichia coli ATPgS-bound
    MetNI methionine ABC transporter in complex with its MetQ binding protein; primary
    DOI10.1073/pnas.1811003115. No coordinate reanalysis is implied.; PMID:22095702:
    UNREACHABLE; Native Europe PMC uniquely identifies MED22095702: Inward facing
    conformations of the MetNI methionine ABC transporter: Implications for the mechanism
    of transinhibition. (2012); DOI10.1002/pro.765. Identifier transport verification
    is distinct from separately scoped primary-source reading.; PMID:30352853: UNREACHABLE;
    Native Europe PMC uniquely identifies MED30352853: Noncanonical role for the binding
    protein in substrate uptake by the MetNI methionine ATP Binding Cassette (ABC)
    transporter. (2018); DOI10.1073/pnas.1811003115. Identifier transport verification
    is distinct from separately scoped primary-source reading. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - complex59-agent-pdb-entry-6CVL
  - complex59-agent-pmid-22095702
  - complex59-agent-pmid-30352853
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990197
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
  - GO:1990197
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
  - GO:1990197
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
  - GO:1990197
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
  - GO:1990197
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
  reference: data/structures/other/methionine_importing_abc_transporter_complex.yaml
  locator: Entire maintained record, all examples, evidence, graphs, properties, images,
    history and discussions
  accessed_at: '2026-10-22T08:10:31Z'
  support: context_only
  summary: Every maintained field was read. Historical curation statements are context,
    not independent biological evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component/ProteinExample, EssentialityEnum, PresenceEnum and graph-scope
    contracts
  accessed_at: '2026-10-22T08:10:31Z'
  support: context_only
  summary: Formation necessity differs from function, viability and membership. COMMON
    means most members with losses the exception; VARIABLE means lineage- or strain-level
    patchiness, not cell-type-specific visibility.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding and REVIEWED_LABEL_ONLY at159–160
  accessed_at: '2026-10-22T08:10:31Z'
  support: context_only
  summary: Exact full-family mappings differ from shared domains or broader paralog
    classes. Label-only is not merely uncurated in this pass.
- evidence_id: complex59-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001401,GO:0005743,GO:0006935,GO:0015191,GO:0030117,GO:0030118,GO:0030119,GO:0030120,GO:0033232,GO:0061617,GO:0098561,GO:0098796,GO:0098800,GO:0140275,GO:1902495,GO:1990197
  locator: Complete target-relevant native definitions/synonyms and typed relationships;
    unrelated combined entries not attributed to this target
  accessed_at: '2026-10-22T07:52:24.329077Z'
  support: supports
  summary: GO1990197 identifies the MetNIQ example and current synonyms; its last
    definition sentence grammatically attributes ATP-dependent translocation to MetQ.
    This faithfully inherited wording is compared separately with the primary source.
    Transport-function terms retain their native identities.
  snapshot_sha256: dbd460ba253a79f76308983bfbf11d984337e32c973e044f3f1b30f1394901af
- evidence_id: complex59-agent-go-1990197-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990197/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response
  accessed_at: '2026-10-22T07:52:40.609082Z'
  support: supports
  summary: The is_a-only closure supplies classification ancestry for this exact target.
    It does not establish parthood, experimental assembly necessity or prevalence.
  snapshot_sha256: b76796ce534a51412a9ee65a7d27dd42826f496c4963c647d0f8b1dd064dd1df
- evidence_id: complex59-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete ENA identity/names/lineage
  accessed_at: '2026-10-22T07:52:31.662631Z'
  support: supports
  summary: 'Taxon83333: Escherichia coli K-12, rank strain; exact native names and
    lineage inspected.'
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: complex59-agent-protein-P28635
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P28635.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:52:27.309731Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P28635, D-methionine-binding lipoprotein
    MetQ; primary genes metQ, synonyms yaeC, taxon83333. Its own native comments and
    family cross-references were inspected with their original evidence qualifiers.'
  snapshot_sha256: 512d42373c7ec864f0dac52f88f840f07d63700615b72a7cb292e2abb0126e90
- evidence_id: complex59-agent-protein-P30750
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P30750.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:52:27.474362Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P30750, Methionine import ATP-binding
    protein MetN; primary genes metN, synonyms abc, taxon83333. Its own native comments
    and family cross-references were inspected with their original evidence qualifiers.'
  snapshot_sha256: 3198440565d8fd662a2367e7debb926d5dd132f0e6afec469faa2cfa0451fabd
- evidence_id: complex59-agent-protein-P31547
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P31547.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:52:27.513246Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): P31547, D-methionine transport system
    permease protein MetI; primary genes metI, synonyms yaeE, taxon83333. Its own
    native comments and family cross-references were inspected with their original
    evidence qualifiers.'
  snapshot_sha256: 7464a675656c9f4870e43eb67e0f72e03f03d096d94af66f4f001bda0ad74889
- evidence_id: complex59-agent-query-abc
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Aabc%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:25.192553Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P30750. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: 5ca7f7151f3acc4059a9848562c0a6df6b7d449d765e4e5850ef88e438f3dc2e
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Aabc%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-query-metI
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmetI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:25.289988Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P31547. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: 45010fa1d4f4428d3923057c75a70b751993990f28b5341e9bbd38fc495392c6
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmetI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-query-metN
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmetN%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:24.780737Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P30750. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: 5ca7f7151f3acc4059a9848562c0a6df6b7d449d765e4e5850ef88e438f3dc2e
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmetN%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-query-metQ
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmetQ%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:26.041902Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P28635. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: ddcbe6475474728361f5d8643f53371f75daa6bdced3d1e6859a98f3dc09a119
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmetQ%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-query-yaeC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AyaeC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:26.181028Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P28635. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: ddcbe6475474728361f5d8643f53371f75daa6bdced3d1e6859a98f3dc09a119
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AyaeC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-query-yaeE
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AyaeE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query results
  accessed_at: '2026-10-22T07:57:25.745239Z'
  support: supports
  summary: 'Exact native query returns 1 entry: P31547. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: 45010fa1d4f4428d3923057c75a70b751993990f28b5341e9bbd38fc495392c6
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AyaeE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    all returned identities inspected.
- evidence_id: complex59-agent-pmid-22095702
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22095702+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and available abstract
  accessed_at: '2026-10-22T07:52:34.315744Z'
  support: supports
  summary: 'MED22095702: Inward facing conformations of the MetNI methionine ABC transporter:
    Implications for the mechanism of transinhibition. Johnson E, Nguyen PT, Yeates
    TO, Rees DC. (2012), DOI10.1002/pro.765. Exact metadata and complete available
    abstract read; this does not claim body access. '
  snapshot_sha256: 188ce7932a2387b56a1d43ca772a3db1054774613d0dcd0e8ce2a190f3c8f0a8
- evidence_id: complex59-agent-pmid-30352853
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A30352853+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and available abstract
  accessed_at: '2026-10-22T07:52:34.916323Z'
  support: supports
  summary: 'MED30352853: Noncanonical role for the binding protein in substrate uptake
    by the MetNI methionine ATP Binding Cassette (ABC) transporter. Nguyen PT, Lai
    JY, Lee AT, Kaiser JT, Rees DC. (2018), DOI10.1073/pnas.1811003115. Exact metadata
    and complete available abstract read; this does not claim body access. '
  snapshot_sha256: 2bb7ac7b5a531e584ab4a80b8f80a4e632e402f3359fb234e4bfd9cace8d19d2
- evidence_id: complex59-agent-johnson2012-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3323783/
  locator: Introduction sec1, Results sec3/4/8/9, complete Discussion sec10, Methods
    sec12/13 and all captions embedded in those sections; no unlisted Results/Methods,
    pixels or supplements.
  accessed_at: '2026-10-22T07:57:58.106358Z'
  support: supports
  summary: Johnson2012 identifies two MetN plus two MetI subunits and a separate MetQ
    delivery protein. Inward-facing structures and comparisons support a qualified
    coupling/transinhibition model; the paper explicitly distinguishes proposed motions
    from measured dynamics.
  snapshot_sha256: b7204fd43e786886edb32e6a13ec426f052df69a625699065b2ff961a78e1a07
- evidence_id: complex59-agent-nguyen2018-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6233128/fullTextXML
  locator: Results/Discussion s1–s6, Methods s8/s14, Table1 and Fig1–9 captions embedded
    there; no figure pixels or supplements.
  accessed_at: '2026-10-22T07:57:20.613801Z'
  support: supports
  summary: Nguyen2018 measures D-selenomethionine uptake and resolves an ATPgammaS-bound
    engineered MetNIQ complex. Apo-MetQ association supports a proposed noncanonical
    pathway; canonical high-affinity delivery remains a comparison model. K12 gene
    origin, BL21 expression and BW2115 uptake background are distinct.
  snapshot_sha256: 1bbb1294bf328788e42fcc8f9a8fa77bed925cc1b2eb957705397fb2a77635dc
- evidence_id: complex59-agent-pdb-entry-6CVL
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/6CVL
  locator: Entry title and complete primary-citation identity
  accessed_at: '2026-10-22T07:57:29.444418Z'
  support: supports
  summary: PDB6CVL is the Nguyen2018 ATPgammaS-bound E.coli MetNIQ structure.
  snapshot_sha256: 0dec5d47a32999d5739fb7ae6f6f63e746cac194495cff729f0083c2d3b566ed
- evidence_id: complex59-agent-pdb-assembly-6CVL-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/6CVL/1
  locator: Complete assembly1 composition/counts/generation fields
  accessed_at: '2026-10-22T07:57:29.540113Z'
  support: supports
  summary: Biological assembly1 contains five protein instances from three entity
    classes; deposited nonpolymer ligands are not protein subunits.
  snapshot_sha256: c9bc281a9b9c56c3b6e4997b23d18253bdda960306c61b05bbd2f0ffba0e6772
- evidence_id: complex59-agent-pdb-polymer_entity-6CVL-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6CVL/1
  locator: Protein identity/source organism/genes, chain multiplicity, mutation count
    and UniProt mapping
  accessed_at: '2026-10-22T07:57:29.623011Z'
  support: supports
  summary: Entity1 is MetN, with 2 deposited copies, source taxon83333, UniProtP30750
    and 2 annotated sequence mutations. The source is genetically engineered.
  snapshot_sha256: b5a767db2e5693b65692b6bade1fa713cc4b3a367c06f4a862f682f22da3a1e9
- evidence_id: complex59-agent-pdb-polymer_entity-6CVL-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6CVL/2
  locator: Protein identity/source organism/genes, chain multiplicity, mutation count
    and UniProt mapping
  accessed_at: '2026-10-22T07:57:29.726209Z'
  support: supports
  summary: Entity2 is MetI, with 2 deposited copies, source taxon83333, UniProtP31547
    and 0 annotated sequence mutations. The source is genetically engineered.
  snapshot_sha256: 4de0ee65fc71c4b795fca0d5d728c7a74a60289c6bbdd34def2f41cf6b7bff43
- evidence_id: complex59-agent-pdb-polymer_entity-6CVL-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6CVL/3
  locator: Protein identity/source organism/genes, chain multiplicity, mutation count
    and UniProt mapping
  accessed_at: '2026-10-22T07:57:29.824975Z'
  support: supports
  summary: Entity3 is MetQ, with 1 deposited copies, source taxon83333, UniProtP28635
    and 1 annotated sequence mutations. The source is genetically engineered.
  snapshot_sha256: 18f5ff9474564640990885ad7f5f043290069a171c0b0171c3efd341f0883479
- evidence_id: complex59-agent-ipr-IPR012692
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012692/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:52:29.265010Z'
  support: supports
  summary: IPR012692 is the retained proteobacterial MetN full-family class.
  snapshot_sha256: 2166dd9b6fb3b07c8888531695dda3409e191b6877c25cddf7f78875c6eee302
- evidence_id: complex59-agent-ncbifam-NF008049
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF008049/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:57:29.301660Z'
  support: supports
  summary: NF008049 is the methionine ABC transporter permease MetI family.
  snapshot_sha256: fea15aed980bdb2ee07c444c477c5e5973af1cf4c692df19e74319baded3627f
- evidence_id: complex59-agent-ncbifam-NF008285
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF008285/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:57:29.417550Z'
  support: supports
  summary: NF008285 is the methionine ABC transporter substrate-binding lipoprotein
    MetQ family.
  snapshot_sha256: 90c469f6256f65f52910675919c6ea9fa7a3498b432a60fb7a6995482ca89b5f
- evidence_id: complex59-agent-interpro-IPR004872
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004872/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:57:28.248474Z'
  support: supports
  summary: The NlpA lipoprotein family is broader than the MetQ-specific class.
  snapshot_sha256: ddbb0b9ac8286d9f1a317b8e6b14e6376cd085b13217d389aeb69dfcc66bb90a
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/methionine_importing_abc_transporter_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:58:04Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/methionine_importing_abc_transporter_complex.yaml'
  snapshot_sha256: 1c42612fc48d768a087a1a8fbc9191e22732ccf08523a9bb8dcecc9049bc307c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/methionine_importing_abc_transporter_complex.yaml
    --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methionine_importing_abc_transporter_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:58:05Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/methionine_importing_abc_transporter_complex.yaml\
    \ --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methionine_importing_abc_transporter_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch59-20261022-t3ere5ku/methionine_importing_abc_transporter_complex-strict.tsv"
  snapshot_sha256: ffba6dd9947b08957745a11efff2ce9a3b4a3ed5f56d4ee7bb717adc693a6531
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/methionine_importing_abc_transporter_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T08:00:12.905258Z'
  support: supports
  summary: "data/structures/other/methionine_importing_abc_transporter_complex.yaml\
    \  (GO:1990197)\n  metniq_methionine_import\tmetq_periplasmic_binding_protein\t\
    COVERED\t->metq_periplasmic_binding_protein (UniProtKB:P28635)\n  metniq_methionine_import\t\
    metn_atp_binding_subunit\tCOVERED\t->metn_atp_binding_subunit (UniProtKB:P30750)\n\
    \  metniq_methionine_import\tmeti_transmembrane_subunit\tCOVERED\t->meti_transmembrane_subunit\
    \ (UniProtKB:P31547)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 50d703641ce59be20015c0e098f3baab6af6973fe4f63ecae41637e232c4d7cf
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/methionine_importing_abc_transporter_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T08:00:14.215172Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/methionine_importing_abc_transporter_complex.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 14 collected target identifiers returned OK. PDB:6CVL: SKIPPED;
    Native released RCSB entry 6CVL: Crystal structure of the Escherichia coli ATPgS-bound
    MetNI methionine ABC transporter in complex with its MetQ binding protein; primary
    DOI10.1073/pnas.1811003115. No coordinate reanalysis is implied.; PMID:22095702:
    UNREACHABLE; Native Europe PMC uniquely identifies MED22095702: Inward facing
    conformations of the MetNI methionine ABC transporter: Implications for the mechanism
    of transinhibition. (2012); DOI10.1002/pro.765. Identifier transport verification
    is distinct from separately scoped primary-source reading.; PMID:30352853: UNREACHABLE;
    Native Europe PMC uniquely identifies MED30352853: Noncanonical role for the binding
    protein in substrate uptake by the MetNI methionine ATP Binding Cassette (ABC)
    transporter. (2018); DOI10.1073/pnas.1811003115. Identifier transport verification
    is distinct from separately scoped primary-source reading. Native source checks
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
  topic: Three classes and2:2:1 deposited assembly
  outcome: supported
  target_ids:
  - GO:1990197
  summary: The native GO ancestor, exact three proteins/aliases and PDB assembly support
    the canonical2:2:1 E.coli complex. K12 describes gene origin; engineered substitutions
    and the separate expression/uptake backgrounds are retained as preparation limits.
  evidence_ids:
  - record
  - complex59-agent-go
  - complex59-agent-go-1990197-ancestors
  - complex59-agent-johnson2012-legacy
  - complex59-agent-nguyen2018-xml
  - complex59-agent-pdb-entry-6CVL
  - complex59-agent-pdb-assembly-6CVL-1
  - complex59-agent-pdb-polymer_entity-6CVL-1
  - complex59-agent-pdb-polymer_entity-6CVL-2
  - complex59-agent-pdb-polymer_entity-6CVL-3
  - complex59-agent-protein-P28635
  - complex59-agent-protein-P30750
  - complex59-agent-protein-P31547
  - complex59-agent-query-abc
  - complex59-agent-query-metI
  - complex59-agent-query-metN
  - complex59-agent-query-metQ
  - complex59-agent-query-yaeC
  - complex59-agent-query-yaeE
  - complex59-agent-tax-83333
- assessment_id: grounding
  area: grounding
  topic: Exact MetI and MetQ mappings
  outcome: concern
  target_ids:
  - GO:1990197
  summary: The two label-only rows have exact NCBIfam alternatives independently joined
    by their native protein cross-references. Broader NlpA/ABC-domain candidates remain
    distinct.
  evidence_ids:
  - record
  - curation
  - complex59-agent-ipr-IPR012692
  - complex59-agent-ncbifam-NF008049
  - complex59-agent-ncbifam-NF008285
  - complex59-agent-interpro-IPR004872
  - complex59-agent-protein-P28635
  - complex59-agent-protein-P30750
  - complex59-agent-protein-P31547
- assessment_id: definition
  area: scope
  topic: MetQ delivery versus ATP-driven translocation
  outcome: concern
  target_ids:
  - GO:1990197
  summary: The copied GO final sentence grammatically makes MetQ capable of ATP-dependent
    periplasm-to-cytoplasm transport. The primary papers assign delivery/access to
    MetQ and transmembrane ATP-coupled transport to the MetNI system; changing the
    sentence subject preserves the supported complex identity.
  evidence_ids:
  - record
  - complex59-agent-go
  - complex59-agent-johnson2012-legacy
  - complex59-agent-nguyen2018-xml
- assessment_id: graph
  area: graph
  topic: Coarse canonical transport and noncanonical alternative
  outcome: supported
  target_ids:
  - GO:1990197
  summary: Docking, ATP coupling and the two methionine transport functions are supported
    at the graph’s coarse mechanistic level.6CVL captures an engineered apo-MetQ state,
    not observed substrate delivery; Nguyen2018 explicitly models both canonical and
    noncanonical pathways, while Johnson2012 comparisons are not time-resolved motion
    measurements. The current general delivery role is not treated as an exclusive
    mechanism.
  evidence_ids:
  - record
  - complex59-agent-johnson2012-legacy
  - complex59-agent-nguyen2018-xml
  - complex59-agent-pdb-entry-6CVL
  - complex59-agent-pdb-assembly-6CVL-1
- assessment_id: formation
  area: grounding
  topic: Transport function is not formation necessity
  outcome: unknown
  target_ids:
  - GO:1990197
  summary: MetQ deletion strongly reduces uptake, and structures establish assembled
    membership. Neither readout independently supplies universal individual formation
    necessity; the maintained UNKNOWN values remain appropriate.
  evidence_ids:
  - record
  - schema
  - complex59-agent-nguyen2018-xml
  - complex59-agent-johnson2012-legacy
- assessment_id: coverage
  area: completeness
  topic: Whole maintained target and declared source coverage
  outcome: supported
  target_ids:
  - GO:1990197
  summary: Every maintained field, source note, graph and discussion was inspected
    at the declared extents. Optional inventory/contact enrichment and acknowledged
    unknowns alone do not create findings.
  evidence_ids:
  - record
  - schema
  - curation
  - complex59-agent-go
findings:
- finding_id: F1
  issue_key: metniq-exact-subunit-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the exact MetI and MetQ families
  description: Both rows remain REVIEWED_LABEL_ONLY because shared InterPro entries
    were considered, while exact native NCBIfam full families and independent protein
    membership resolve their retained classes.
  target_ids:
  - GO:1990197
  field_paths:
  - components#meti_transmembrane_subunit.grounding_status
  - components#metq_periplasmic_binding_protein.grounding_status
  - discussions#resolve_metniq_component_groundings
  evidence_ids:
  - record
  - curation
  - complex59-agent-ipr-IPR012692
  - complex59-agent-ncbifam-NF008049
  - complex59-agent-ncbifam-NF008285
  - complex59-agent-interpro-IPR004872
  - complex59-agent-protein-P28635
  - complex59-agent-protein-P30750
  - complex59-agent-protein-P31547
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methionine_importing_abc_transporter_complex.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: minor
  normalization_reason: A bounded correction preserves the supported complex identity
    and principal biological function.
- finding_id: F2
  issue_key: metniq-definition-transport-subject
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Assign ATP-dependent translocation to the transporter
  description: The last definition sentence currently makes MetQ alone the subject
    of ATP-dependent membrane translocation. This is faithful to current GO wording,
    but disagrees with the clear division of roles in its cited primary source and
    the record’s own component roles.
  target_ids:
  - GO:1990197
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - record
  - complex59-agent-go
  - complex59-agent-johnson2012-legacy
  - complex59-agent-nguyen2018-xml
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methionine_importing_abc_transporter_complex.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: minor
  normalization_reason: A bounded correction preserves the supported complex identity
    and principal biological function.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990197
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methionine_importing_abc_transporter_complex.yaml
    role: maintained scientific record
  description: Use NCBIfam:NF008049 for MetI and NCBIfam:NF008285 for MetQ, preserving
    correct examples,2:2:1 stoichiometry and unresolved individual necessity.
  acceptance_checks:
  - Join each native family to its own protein cross-reference; do not substitute
    broad NlpA or a shared transporter domain.
  - Preserve supported source-specific claims and pass applicable native gates.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:1990197
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/methionine_importing_abc_transporter_complex.yaml
    role: maintained scientific record
  description: Clarify that MetQ binds/presents substrate and the MetNI-containing
    complex performs ATP-dependent transport; retain the exact GO identity and add
    primary support for the clarified wording.
  acceptance_checks:
  - Do not claim MetQ itself is the ATPase or transmembrane permease; preserve the
    source’s noncanonical access alternative.
  - Preserve supported source-specific claims and pass applicable native gates.
limitations:
- All five completed same-base batch26 global gates are integrated with exact manifest/input/log
  hashes verified; no fresh full-site QC is claimed from this sparse checkout.
- Only the explicitly listed source sections/assets were inspected. No unlisted supplements,
  atomic coordinates or raw experimental data were analyzed.
- No PDB coordinates or supplements were analyzed. The deposited mutant ATPgammaS
  complex is not a direct wild-type substrate-flux trajectory. Johnson2012 gene expression
  uses BL21-gold; Nguyen2018 separates K12 gene origin from BL21 expression and BW2115
  uptake experiments.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes both clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
