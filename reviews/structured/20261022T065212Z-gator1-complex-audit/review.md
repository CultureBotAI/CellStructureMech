# Gator1 complex scientific review

- Review: 20261022T065212Z-gator1-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:28:19Z
- Finished UTC: 2026-10-22T06:52:12Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

GATOR1/SEACIT identity, yeast membership, GAP target and negative-signaling graph are supported. One grouped minor resolves the three exact families; source-system and formation limits remain explicit.

## Scope And Provenance

Exactly one whole maintained target plus frozen guidance and protein-example skill. Actual source-read extents are enumerated per evidence row; no maintained neighboring record supplies scientific evidence.

Selection: Target 8 of batch55, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990130 | data/structures/other/gator1_complex.yaml | maintained | GATOR1 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990130 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990130 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:1990130 | Native focused check passed; scientific claims assessed separately. |
| Native verify | passed | True | GO:1990130 | Native focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:1990130 | No expression-module inference is used. |
| Claim-level scientific review | passed | True | GO:1990130 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990130 | 15 of 17 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:21454883: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990130 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990130 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990130 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990130 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990130 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### GATOR1/SEACIT and SEA parthood

identity: supported. Targets: GO:1990130.

The exact identity, two exact synonyms, parent and SEA parthood agree with native GO and primary yeast/human counterpart studies. Gtr1 is a direct GAP target, not a constituent; the separate SEACAT branch is not conflated with SEACIT.

### Three verified constituent families

grounding: concern. Targets: GO:1990130.

Iml1, Npr2 and Npr3 have exact full-family identities. Correct reviewed accessions, gene aliases and exact query uniqueness are retained; shared domains are not substituted.

### Yeast deprivation response and reference metadata

scope: supported. Targets: GO:1990130.

Taxa4932/559292 are correct. CellCycle experiments use prototrophic BY4741/2-derived strains; native reference entries do not assert that every study used S288C unchanged. COMMON retains majority-occurrence/losses-exception meaning, supported by qualitative conserved yeast-system synthesis rather than a census.

### Gtr1 GAP target, vacuolar association and negative signaling

graph: supported. Targets: GO:1990130.

The high-level graph preserves source-supported direction and direct target context. The transient association is Iml1 with Gtr1 during deprivation, not a claim that all Iml1 vacuolar localization begins only on starvation. The retained SciSignal complete abstract and CellCycle source support this scope; human RagA/B biochemistry is not labeled a yeast experiment.

### Activity and localization are not blanket formation requirements

grounding: unknown. Targets: GO:1990130.

The inspected epistasis, GAP, knockdown and localization assays do not establish universal whole-complex formation necessity for each listed protein. UNKNOWN remains appropriate within this bounded evidence scope. Physical membership is supported separately.

### Complete maintained target with bounded source inspection

completeness: supported. Targets: GO:1990130.

All maintained fields, evidence notes, graph statements and discussions were checked at the declared source extents. Optional inventories and unmeasured formation requirements are not fabricated from native validation.

## Findings

### F1: Ground all three exact GATOR1/SEACIT classes

minor / open / confirmed; issue key: gator1-exact-families.

Exact Iml1/DEPDC5, Npr2/NPRL2 and Npr3/NPRL3 families are now verified, resolving the maintained label-only deferral.

## Recommended Actions And Acceptance Checks

### A1

Use IPR027244, IPR009348 and IPR005365 respectively, with the existing yeast roles and human counterpart scope intact.

- Keep Rag GTPases and SEACAT outside the three-member constituent boundary.
- Preserve supported identities and source scope; pass applicable native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/gator1_complex.yaml; Entire maintained record, including all evidence, examples, graphs, history and discussions | context_only | The entire record was read. Dated curation history is not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, essentiality, taxonomy and graph-scope contracts | context_only | Essentiality concerns formation rather than activity or viability. COMMON means present in most members, with losses the exception; qualitative synthesis is distinct from a measured census. |
| curation | docs/CURATION.md; Component grounding, including REVIEWED_LABEL_ONLY at159–160 | context_only | A verified exact full-protein family is distinct from a shared domain or broader paralog group. Label-only is not simply a placeholder for an available exact mapping uncurated this pass. |
| complex55-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000329,GO:0000938,GO:0005802,GO:0015030,GO:0016604,GO:0031981,GO:0032991,GO:0035859,GO:0038202,GO:0042147,GO:0061700,GO:0097504,GO:0099023,GO:1904262,GO:1904263,GO:1990130; Complete target-relevant definitions/synonyms and typed relationships in combined response; no unrelated child is attributed to this target | supports | GO1990130 identifies GATOR1/SEACIT and exact synonyms, distinguishes yeast Iml1/Npr2/Npr3 from human DEPDC5/NPRL2/NPRL3, and GO0035859 supplies the part_of child relationship. GO1904262/0038202 and0000329 define negative TORC1 regulation, signaling and vacuole membrane. |
| complex55-agent-GO1990130-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990130/ancestors?relations=is_a; Complete is_a-only ancestor response | supports | The is_a-only closure contains the maintained parent class; this request does not establish parthood. |
| complex55-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete ENA taxonomy identity/names/lineage | supports | Taxon4932 is Saccharomyces cerevisiae, rank species; native names and lineage identify this exact taxon. |
| complex55-agent-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete ENA taxonomy identity/names/lineage | supports | Taxon559292 is Saccharomyces cerevisiae S288C, rank strain; native names and lineage identify this exact taxon. |
| complex55-agent-protein-P38742 | https://rest.uniprot.org/uniprotkb/P38742.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed P38742: Nitrogen permease regulator 3; primary genes NPR3, synonyms RMD11, taxon559292. Native comments preserve their own experimental/inferred evidence scope. This protein response supplies its family membership xrefs independently of the family-entry metadata. |
| complex55-agent-protein-P39923 | https://rest.uniprot.org/uniprotkb/P39923.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed P39923: Nitrogen permease regulator 2; primary genes NPR2, synonyms none, taxon559292. Native comments preserve their own experimental/inferred evidence scope. This protein response supplies its family membership xrefs independently of the family-entry metadata. |
| complex55-agent-protein-P47170 | https://rest.uniprot.org/uniprotkb/P47170.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed P47170: Vacuolar membrane-associated protein IML1; primary genes IML1, synonyms SEA1, taxon559292. Native comments preserve their own experimental/inferred evidence scope. This protein response supplies its family membership xrefs independently of the family-entry metadata. |
| complex55-agent-protein-Q00582 | https://rest.uniprot.org/uniprotkb/Q00582.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed Q00582: GTP-binding protein GTR1; primary genes GTR1, synonyms none, taxon559292. Native comments preserve their own experimental/inferred evidence scope. This protein response supplies its family membership xrefs independently of the family-entry metadata. |
| complex55-agent-gene-IML1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIML1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; All returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: P47170. Complete returned gene tokens distinguish primary names from queried aliases. |
| complex55-agent-gene-NPR2-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANPR2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; All returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: P39923. Complete returned gene tokens distinguish primary names from queried aliases. |
| complex55-agent-gene-NPR3-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANPR3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; All returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: P38742. Complete returned gene tokens distinguish primary names from queried aliases. |
| complex55-agent-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete MED identity and abstract | supports | MED14562095: Global analysis of protein localization in budding yeast. Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK. (2003), DOI10.1038/nature02026. Exact metadata and complete native abstract read; primary body is not implied by this row. |
| complex55-agent-pmid-21454883 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21454883+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete MED identity and abstract | supports | MED21454883: A conserved coatomer-related complex containing Sec13 and Seh1 dynamically associates with the vacuole in Saccharomyces cerevisiae. Dokudovskaya S, Waharte F, Schlessinger A, Pieper U, Devos DP, Cristea IM, Williams R, Salamero J, Chait BT, Sali A, Field MC, Rout MP, Dargemont C. (2011), DOI10.1074/mcp.m110.006478. Exact metadata and complete native abstract read; primary body is not implied by this row. |
| complex55-agent-doi-science_1232044 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1232044%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract when present | supports | Exact DOI/MED identity: A Tumor suppressor complex with GAP activity for the Rag GTPases that signal amino acid sufficiency to mTORC1. Bar-Peled L, Chantranupong L, Cherniack AD, Chen WW, Ottina KA, Grabiner BC, Spear ED, Carter SL, Meyerson M, Sabatini DM. (2013), PMID23723238. Complete native abstract read.  |
| complex55-agent-doi-scisignal_2004112 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscisignal.2004112%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract when present | supports | Exact DOI/MED identity: Amino acid deprivation inhibits TORC1 through a GTPase-activating protein complex for the Rag family GTPase Gtr1. Panchaud N, Péli-Gulli MP, De Virgilio C. (2013), PMID23716719. Complete native abstract read.  |
| complex55-agent-primary-PMC3108837 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3108837/; Methods sec4/5/6/9; Results sec17 and sec20; embedded Fig1/3/5 captions. Supplemental strain tables and pixels not independently read. | supports | Dokudovskaya2011 reciprocally purifies the eight-member SEA system and detects vacuole-associated proteins. Npr3-GFP was below detection, while carbonate extraction supports peripheral association; the paper explicitly leaves other locations possible. Earlier GFP-atlas discrepancies are discussed rather than erased. Shared Sec13/Seh1 NPC or COPII functions do not make those entire complexes SEA constituents. |
| complex55-agent-primary-PMC3875668 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3875668/; Complete Introduction sec1, Results/Discussion sec2, Materials/Methods sec3–5 including all strains, Fig1–3 captions. No figure pixels. | supports | Panchaud2013 Cell Cycle contains new yeast epistasis data, not merely a literature review: sec13-1 at25C and seh1 deletion at30C reduce Sch9-phosphorylation TORC1 output, rescued by loss of Iml1. The source names SEACIT and SEACAT and presents their antagonism as a model supported by those genetic experiments. Proposed NPC/secretory coupling remains speculative. |
| complex55-agent-primary-PMC3728654 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3728654/; Complete main prose P1–P14, including in-text experimental descriptions. Supplementary Methods/data and figure pixels/captions were not independently used. | supports | Bar-Peled2013 distinguishes human GATOR1 and GATOR2 by co-IP, tests opposite signaling effects in HEK293T and Drosophila S2 cells, and directly assays GATOR1 GAP activity for RagA/B. Sec13 was excluded from functional knockdown interpretation. Those experiments provide cross-system counterpart context, not direct yeast assays. |
| complex55-agent-ipr-IPR027244 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027244/; Native name/type, complete descriptions/curation flags, signatures and hierarchy; protein membership is independently supplied by UniProt | supports | IPR027244 is the full Iml1/DEPDC5 family (PTHR13179), not simply the DEP domain. |
| complex55-agent-ipr-IPR009348 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009348/; Native name/type, complete descriptions/curation flags, signatures and hierarchy; protein membership is independently supplied by UniProt | supports | IPR009348 is the complete nitrogen-permease-regulator2/NPRL2 family (PF06218/PTHR12991). |
| complex55-agent-ipr-IPR005365 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005365/; Native name/type, complete descriptions/curation flags, signatures and hierarchy; protein membership is independently supplied by UniProt | supports | IPR005365 is the complete Npr3/NPRL3 family (PF03666/PTHR13153), separate from a single HTH segment. |
| schema-result | just validate data/structures/other/gator1_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/gator1_complex.yaml |
| strict-result | just validate-strict data/structures/other/gator1_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator1_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/gator1_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator1_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator1_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/gator1_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/gator1_complex.yaml  (GO:1990130)<br>  yeast_gator1_torc1_regulation	iml1_gator1_subunit	COVERED	-&gt;iml1_gator1_subunit (UniProtKB:P47170)<br>  yeast_gator1_torc1_regulation	npr2_gator1_subunit	COVERED	-&gt;npr2_gator1_subunit (UniProtKB:P39923)<br>  yeast_gator1_torc1_regulation	npr3_gator1_subunit	COVERED	-&gt;npr3_gator1_subunit (UniProtKB:P38742)<br>  yeast_gator1_torc1_regulation	gtr1_rag_gtpase	UNANCHORED_WITH_UNIPROT	Gtr1 Rag-family GTPase (UniProtKB:Q00582)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/gator1_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/gator1_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 15 of 17 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:21454883: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Five completed same-base batch26 global gates await guarded parent manifest/hash integration.
- No supplemental experiments or atomic coordinates were independently analyzed. Source reading is limited to the exact evidence locators.
- The retained SciSignal2013 author-PDF routes returned503. A transient browser display was not retained with a complete response receipt and is not used as hashed full-body evidence; formal SciSignal support here is its complete native abstract, supplemented by the separately read CellCycle body.
- Huh2003 and, for GATOR2, Rout2000 were read at native complete-abstract scope. UniProt annotation-source placement is verified, but a multi-reference annotation is not taken to mean every cited paper independently tested every localization.
- Dokudovskaya Npr3 fluorescence was below detection and earlier Sea2 atlas localization differed; the record accurately reports the current UniProt annotation rather than claiming a fresh reanalysis of those images.
- No SEA/GATOR source figure pixels or supplements were read; functional epistasis and direct biochemical activity are distinguished.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T065212Z-gator1-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Gator1 complex scientific review
started_at: '2026-10-22T06:28:19Z'
finished_at: '2026-10-22T06:52:12Z'
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
summary: GATOR1/SEACIT identity, yeast membership, GAP target and negative-signaling
  graph are supported. One grouped minor resolves the three exact families; source-system
  and formation limits remain explicit.
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
  - path: data/structures/other/gator1_complex.yaml
    sha256: 7baf105999145f4439e69771264fb5c37a524efbc9a879d20cf1f365430c4ed6
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
- target_id: GO:1990130
  path: data/structures/other/gator1_complex.yaml
  label: GATOR1 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gator1_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one whole maintained target plus frozen guidance and protein-example
    skill. Actual source-read extents are enumerated per evidence row; no maintained
    neighboring record supplies scientific evidence.
  selection: Target 8 of batch55, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990130
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990130
  command: just validate data/structures/other/gator1_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990130
  command: just validate-strict data/structures/other/gator1_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator1_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990130
  command: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gator1_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:1990130
  command: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gator1_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990130
  summary: No expression-module inference is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990130
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex55-agent-go
  - complex55-agent-GO1990130-ancestors
  - complex55-agent-tax4932
  - complex55-agent-tax559292
  - complex55-agent-protein-P38742
  - complex55-agent-protein-P39923
  - complex55-agent-protein-P47170
  - complex55-agent-protein-Q00582
  - complex55-agent-gene-IML1-559292
  - complex55-agent-gene-NPR2-559292
  - complex55-agent-gene-NPR3-559292
  - complex55-agent-pmid-14562095
  - complex55-agent-pmid-21454883
  - complex55-agent-doi-science_1232044
  - complex55-agent-doi-scisignal_2004112
  - complex55-agent-primary-PMC3108837
  - complex55-agent-primary-PMC3875668
  - complex55-agent-primary-PMC3728654
  - complex55-agent-ipr-IPR027244
  - complex55-agent-ipr-IPR009348
  - complex55-agent-ipr-IPR005365
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990130
  summary: '15 of 17 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:21454883: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - complex55-agent-pmid-14562095
  - complex55-agent-pmid-21454883
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990130
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990130
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990130
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990130
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990130
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
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/gator1_complex.yaml
  locator: Entire maintained record, including all evidence, examples, graphs, history
    and discussions
  accessed_at: '2026-10-22T06:42:30Z'
  support: context_only
  summary: The entire record was read. Dated curation history is not independent biological
    evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, essentiality, taxonomy and graph-scope contracts
  accessed_at: '2026-10-22T06:42:30Z'
  support: context_only
  summary: Essentiality concerns formation rather than activity or viability. COMMON
    means present in most members, with losses the exception; qualitative synthesis
    is distinct from a measured census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding, including REVIEWED_LABEL_ONLY at159–160
  accessed_at: '2026-10-22T06:42:30Z'
  support: context_only
  summary: A verified exact full-protein family is distinct from a shared domain or
    broader paralog group. Label-only is not simply a placeholder for an available
    exact mapping uncurated this pass.
- evidence_id: complex55-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000329,GO:0000938,GO:0005802,GO:0015030,GO:0016604,GO:0031981,GO:0032991,GO:0035859,GO:0038202,GO:0042147,GO:0061700,GO:0097504,GO:0099023,GO:1904262,GO:1904263,GO:1990130
  locator: Complete target-relevant definitions/synonyms and typed relationships in
    combined response; no unrelated child is attributed to this target
  accessed_at: '2026-10-22T06:33:48.736958Z'
  support: supports
  summary: GO1990130 identifies GATOR1/SEACIT and exact synonyms, distinguishes yeast
    Iml1/Npr2/Npr3 from human DEPDC5/NPRL2/NPRL3, and GO0035859 supplies the part_of
    child relationship. GO1904262/0038202 and0000329 define negative TORC1 regulation,
    signaling and vacuole membrane.
  snapshot_sha256: e0100a96ac860dcc76d15e08ab106834853c60e10df6b0165c53a6068133006f
- evidence_id: complex55-agent-GO1990130-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990130/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response
  accessed_at: '2026-10-22T06:33:57.346131Z'
  support: supports
  summary: The is_a-only closure contains the maintained parent class; this request
    does not establish parthood.
  snapshot_sha256: 2eac7009d11defad2d5d642b903eaa9534b2761dbac83b9640a23066ee2e680f
- evidence_id: complex55-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete ENA taxonomy identity/names/lineage
  accessed_at: '2026-10-22T06:33:48.737823Z'
  support: supports
  summary: Taxon4932 is Saccharomyces cerevisiae, rank species; native names and lineage
    identify this exact taxon.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: complex55-agent-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete ENA taxonomy identity/names/lineage
  accessed_at: '2026-10-22T06:33:48.737778Z'
  support: supports
  summary: Taxon559292 is Saccharomyces cerevisiae S288C, rank strain; native names
    and lineage identify this exact taxon.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: complex55-agent-protein-P38742
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38742.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:33:49.488734Z'
  support: supports
  summary: 'Reviewed P38742: Nitrogen permease regulator 3; primary genes NPR3, synonyms
    RMD11, taxon559292. Native comments preserve their own experimental/inferred evidence
    scope. This protein response supplies its family membership xrefs independently
    of the family-entry metadata.'
  snapshot_sha256: 94e7edc60bbaac3305b1d96e8ccadde4a512ed3df75b3d54a15ec738ad4bab1d
- evidence_id: complex55-agent-protein-P39923
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39923.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:33:49.609257Z'
  support: supports
  summary: 'Reviewed P39923: Nitrogen permease regulator 2; primary genes NPR2, synonyms
    none, taxon559292. Native comments preserve their own experimental/inferred evidence
    scope. This protein response supplies its family membership xrefs independently
    of the family-entry metadata.'
  snapshot_sha256: bdd2b1275f0312eb864f8f3a33824e0becc559f41a1e6f8f9a0df125a8460724
- evidence_id: complex55-agent-protein-P47170
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47170.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:33:50.249350Z'
  support: supports
  summary: 'Reviewed P47170: Vacuolar membrane-associated protein IML1; primary genes
    IML1, synonyms SEA1, taxon559292. Native comments preserve their own experimental/inferred
    evidence scope. This protein response supplies its family membership xrefs independently
    of the family-entry metadata.'
  snapshot_sha256: affaf52daae5d96320a6cfd7e176efd159a2ee1114b8febdeb5906e9c7444729
- evidence_id: complex55-agent-protein-Q00582
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q00582.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:33:50.384042Z'
  support: supports
  summary: 'Reviewed Q00582: GTP-binding protein GTR1; primary genes GTR1, synonyms
    none, taxon559292. Native comments preserve their own experimental/inferred evidence
    scope. This protein response supplies its family membership xrefs independently
    of the family-entry metadata.'
  snapshot_sha256: 2dfdb52d191bd77dfc08f5c9669d6bc5f1fe2f34c38bad326255dec0adab5063
- evidence_id: complex55-agent-gene-IML1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIML1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: All returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:33:52.848416Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: P47170. Complete returned
    gene tokens distinguish primary names from queried aliases.'
  snapshot_sha256: da7cd1c0322ef014be7e254bf64b2075156767b12787e578d2535c04f2c23d86
  search_scope: UniProt gene_exact:IML1, organism_id:559292, reviewed:true, size500;
    every returned identity inspected.
- evidence_id: complex55-agent-gene-NPR2-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANPR2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: All returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:33:52.932957Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: P39923. Complete returned
    gene tokens distinguish primary names from queried aliases.'
  snapshot_sha256: 595bfdc12681df7d1c5058b546d58ed88933ebe69f473cafdab11794fde01945
  search_scope: UniProt gene_exact:NPR2, organism_id:559292, reviewed:true, size500;
    every returned identity inspected.
- evidence_id: complex55-agent-gene-NPR3-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANPR3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: All returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:33:53.139933Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: P38742. Complete returned
    gene tokens distinguish primary names from queried aliases.'
  snapshot_sha256: 2ca11825c682f5250eb9ea9e1a83e0a8012a272cf2f6a4cd1e44c9a68d120981
  search_scope: UniProt gene_exact:NPR3, organism_id:559292, reviewed:true, size500;
    every returned identity inspected.
- evidence_id: complex55-agent-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete MED identity and abstract
  accessed_at: '2026-10-22T06:33:55.616568Z'
  support: supports
  summary: 'MED14562095: Global analysis of protein localization in budding yeast.
    Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea EK. (2003),
    DOI10.1038/nature02026. Exact metadata and complete native abstract read; primary
    body is not implied by this row.'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: complex55-agent-pmid-21454883
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21454883+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete MED identity and abstract
  accessed_at: '2026-10-22T06:33:56.083276Z'
  support: supports
  summary: 'MED21454883: A conserved coatomer-related complex containing Sec13 and
    Seh1 dynamically associates with the vacuole in Saccharomyces cerevisiae. Dokudovskaya
    S, Waharte F, Schlessinger A, Pieper U, Devos DP, Cristea IM, Williams R, Salamero
    J, Chait BT, Sali A, Field MC, Rout MP, Dargemont C. (2011), DOI10.1074/mcp.m110.006478.
    Exact metadata and complete native abstract read; primary body is not implied
    by this row.'
  snapshot_sha256: 1a6d5e9622ab6bffaf489ff3ef11e5b3ca9c3e41de9dfdb446a36759f2697253
- evidence_id: complex55-agent-doi-science_1232044
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1232044%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract when present
  accessed_at: '2026-10-22T06:33:56.698667Z'
  support: supports
  summary: 'Exact DOI/MED identity: A Tumor suppressor complex with GAP activity for
    the Rag GTPases that signal amino acid sufficiency to mTORC1. Bar-Peled L, Chantranupong
    L, Cherniack AD, Chen WW, Ottina KA, Grabiner BC, Spear ED, Carter SL, Meyerson
    M, Sabatini DM. (2013), PMID23723238. Complete native abstract read. '
  snapshot_sha256: 8c43f2aa2133806feabd98634063eb47c9a5badce649c0d0394718c853058ff1
- evidence_id: complex55-agent-doi-scisignal_2004112
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscisignal.2004112%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract when present
  accessed_at: '2026-10-22T06:33:56.728400Z'
  support: supports
  summary: 'Exact DOI/MED identity: Amino acid deprivation inhibits TORC1 through
    a GTPase-activating protein complex for the Rag family GTPase Gtr1. Panchaud N,
    Péli-Gulli MP, De Virgilio C. (2013), PMID23716719. Complete native abstract read. '
  snapshot_sha256: f4e2231866ac58d27d5205904ae63729994978f0d2d0b4047a9ab01d534572f0
- evidence_id: complex55-agent-primary-PMC3108837
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3108837/
  locator: Methods sec4/5/6/9; Results sec17 and sec20; embedded Fig1/3/5 captions.
    Supplemental strain tables and pixels not independently read.
  accessed_at: '2026-10-22T06:34:37.482929Z'
  support: supports
  summary: Dokudovskaya2011 reciprocally purifies the eight-member SEA system and
    detects vacuole-associated proteins. Npr3-GFP was below detection, while carbonate
    extraction supports peripheral association; the paper explicitly leaves other
    locations possible. Earlier GFP-atlas discrepancies are discussed rather than
    erased. Shared Sec13/Seh1 NPC or COPII functions do not make those entire complexes
    SEA constituents.
  snapshot_sha256: 59b547269d880b49202c1dcdaaa0b7c0a11b73e37d49ac6d5bf72bfef492e299
- evidence_id: complex55-agent-primary-PMC3875668
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3875668/
  locator: Complete Introduction sec1, Results/Discussion sec2, Materials/Methods
    sec3–5 including all strains, Fig1–3 captions. No figure pixels.
  accessed_at: '2026-10-22T06:34:37.254805Z'
  support: supports
  summary: 'Panchaud2013 Cell Cycle contains new yeast epistasis data, not merely
    a literature review: sec13-1 at25C and seh1 deletion at30C reduce Sch9-phosphorylation
    TORC1 output, rescued by loss of Iml1. The source names SEACIT and SEACAT and
    presents their antagonism as a model supported by those genetic experiments. Proposed
    NPC/secretory coupling remains speculative.'
  snapshot_sha256: ec064c7f24e67a4243056b6a8635b2ec44f853a0cf6aff5637cfcba15e0f7cda
- evidence_id: complex55-agent-primary-PMC3728654
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3728654/
  locator: Complete main prose P1–P14, including in-text experimental descriptions.
    Supplementary Methods/data and figure pixels/captions were not independently used.
  accessed_at: '2026-10-22T06:34:37.297541Z'
  support: supports
  summary: Bar-Peled2013 distinguishes human GATOR1 and GATOR2 by co-IP, tests opposite
    signaling effects in HEK293T and Drosophila S2 cells, and directly assays GATOR1
    GAP activity for RagA/B. Sec13 was excluded from functional knockdown interpretation.
    Those experiments provide cross-system counterpart context, not direct yeast assays.
  snapshot_sha256: 962f3e240d6c762e9d8978a81c8f8baf08f2a55af78ba36779156707837d8b58
- evidence_id: complex55-agent-ipr-IPR027244
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027244/
  locator: Native name/type, complete descriptions/curation flags, signatures and
    hierarchy; protein membership is independently supplied by UniProt
  accessed_at: '2026-10-22T06:34:24.906595Z'
  support: supports
  summary: IPR027244 is the full Iml1/DEPDC5 family (PTHR13179), not simply the DEP
    domain.
  snapshot_sha256: 01022dac269a0446cf5db8387c61cc00d5b13518c730228f9f45d326c43e4915
- evidence_id: complex55-agent-ipr-IPR009348
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009348/
  locator: Native name/type, complete descriptions/curation flags, signatures and
    hierarchy; protein membership is independently supplied by UniProt
  accessed_at: '2026-10-22T06:34:29.483783Z'
  support: supports
  summary: IPR009348 is the complete nitrogen-permease-regulator2/NPRL2 family (PF06218/PTHR12991).
  snapshot_sha256: 6f3fbab2e6a6228a6ae8b8c095d941a359a5da9b4a970afe9c2b17065203ed7c
- evidence_id: complex55-agent-ipr-IPR005365
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005365/
  locator: Native name/type, complete descriptions/curation flags, signatures and
    hierarchy; protein membership is independently supplied by UniProt
  accessed_at: '2026-10-22T06:34:29.500251Z'
  support: supports
  summary: IPR005365 is the complete Npr3/NPRL3 family (PF03666/PTHR13153), separate
    from a single HTH segment.
  snapshot_sha256: 7c0fc176e47b3038571175711c4fc0701a94d237f1daf6ee8bcc8ebe73e27e94
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/gator1_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:28:21Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/gator1_complex.yaml'
  snapshot_sha256: 40d1bdc953c0557480f9e34741bcf7484436816b1ecb61a393fd1133605bab2a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/gator1_complex.yaml --out
    /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator1_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:28:23Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/gator1_complex.yaml\
    \ --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator1_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator1_complex-strict.tsv"
  snapshot_sha256: ef3dd3bca2f43244ddcba8c9e136fdb6699f0e2a18bad6e13b2c864f51b41c1b
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gator1_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T06:33:57.176775Z'
  support: supports
  summary: "data/structures/other/gator1_complex.yaml  (GO:1990130)\n  yeast_gator1_torc1_regulation\t\
    iml1_gator1_subunit\tCOVERED\t->iml1_gator1_subunit (UniProtKB:P47170)\n  yeast_gator1_torc1_regulation\t\
    npr2_gator1_subunit\tCOVERED\t->npr2_gator1_subunit (UniProtKB:P39923)\n  yeast_gator1_torc1_regulation\t\
    npr3_gator1_subunit\tCOVERED\t->npr3_gator1_subunit (UniProtKB:P38742)\n  yeast_gator1_torc1_regulation\t\
    gtr1_rag_gtpase\tUNANCHORED_WITH_UNIPROT\tGtr1 Rag-family GTPase (UniProtKB:Q00582)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  PARTIAL_EXAMPLES          component_ref target holds\
    \ protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     4\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 12ced6f0f34184e7513c99561c2913631f30e4d14b6ef7d56da9f4cdd5233532
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gator1_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T06:33:58.353834Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/gator1_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '15 of 17 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:21454883: UNREACHABLE;
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
  topic: GATOR1/SEACIT and SEA parthood
  outcome: supported
  target_ids:
  - GO:1990130
  summary: The exact identity, two exact synonyms, parent and SEA parthood agree with
    native GO and primary yeast/human counterpart studies. Gtr1 is a direct GAP target,
    not a constituent; the separate SEACAT branch is not conflated with SEACIT.
  evidence_ids:
  - record
  - complex55-agent-go
  - complex55-agent-GO1990130-ancestors
  - complex55-agent-primary-PMC3108837
  - complex55-agent-primary-PMC3875668
  - complex55-agent-primary-PMC3728654
  - complex55-agent-doi-scisignal_2004112
  - complex55-agent-protein-P38742
  - complex55-agent-protein-P39923
  - complex55-agent-protein-P47170
  - complex55-agent-protein-Q00582
- assessment_id: grounding
  area: grounding
  topic: Three verified constituent families
  outcome: concern
  target_ids:
  - GO:1990130
  summary: Iml1, Npr2 and Npr3 have exact full-family identities. Correct reviewed
    accessions, gene aliases and exact query uniqueness are retained; shared domains
    are not substituted.
  evidence_ids:
  - record
  - curation
  - complex55-agent-ipr-IPR027244
  - complex55-agent-ipr-IPR009348
  - complex55-agent-ipr-IPR005365
  - complex55-agent-protein-P38742
  - complex55-agent-protein-P39923
  - complex55-agent-protein-P47170
  - complex55-agent-protein-Q00582
  - complex55-agent-gene-IML1-559292
  - complex55-agent-gene-NPR2-559292
  - complex55-agent-gene-NPR3-559292
- assessment_id: scope
  area: scope
  topic: Yeast deprivation response and reference metadata
  outcome: supported
  target_ids:
  - GO:1990130
  summary: Taxa4932/559292 are correct. CellCycle experiments use prototrophic BY4741/2-derived
    strains; native reference entries do not assert that every study used S288C unchanged.
    COMMON retains majority-occurrence/losses-exception meaning, supported by qualitative
    conserved yeast-system synthesis rather than a census.
  evidence_ids:
  - record
  - schema
  - complex55-agent-primary-PMC3108837
  - complex55-agent-primary-PMC3875668
  - complex55-agent-tax4932
  - complex55-agent-tax559292
- assessment_id: graph
  area: graph
  topic: Gtr1 GAP target, vacuolar association and negative signaling
  outcome: supported
  target_ids:
  - GO:1990130
  summary: The high-level graph preserves source-supported direction and direct target
    context. The transient association is Iml1 with Gtr1 during deprivation, not a
    claim that all Iml1 vacuolar localization begins only on starvation. The retained
    SciSignal complete abstract and CellCycle source support this scope; human RagA/B
    biochemistry is not labeled a yeast experiment.
  evidence_ids:
  - record
  - complex55-agent-go
  - complex55-agent-primary-PMC3108837
  - complex55-agent-primary-PMC3875668
  - complex55-agent-primary-PMC3728654
  - complex55-agent-doi-scisignal_2004112
  - complex55-agent-protein-P38742
  - complex55-agent-protein-P39923
  - complex55-agent-protein-P47170
  - complex55-agent-protein-Q00582
- assessment_id: formation
  area: grounding
  topic: Activity and localization are not blanket formation requirements
  outcome: unknown
  target_ids:
  - GO:1990130
  summary: The inspected epistasis, GAP, knockdown and localization assays do not
    establish universal whole-complex formation necessity for each listed protein.
    UNKNOWN remains appropriate within this bounded evidence scope. Physical membership
    is supported separately.
  evidence_ids:
  - record
  - schema
  - complex55-agent-primary-PMC3108837
  - complex55-agent-primary-PMC3875668
  - complex55-agent-primary-PMC3728654
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target with bounded source inspection
  outcome: supported
  target_ids:
  - GO:1990130
  summary: All maintained fields, evidence notes, graph statements and discussions
    were checked at the declared source extents. Optional inventories and unmeasured
    formation requirements are not fabricated from native validation.
  evidence_ids:
  - record
  - schema
  - curation
  - complex55-agent-go
findings:
- finding_id: F1
  issue_key: gator1-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground all three exact GATOR1/SEACIT classes
  description: Exact Iml1/DEPDC5, Npr2/NPRL2 and Npr3/NPRL3 families are now verified,
    resolving the maintained label-only deferral.
  target_ids:
  - GO:1990130
  field_paths:
  - components[*].grounding_status
  - discussions#resolve_gator1_subunit_family_groundings
  evidence_ids:
  - record
  - curation
  - complex55-agent-ipr-IPR027244
  - complex55-agent-ipr-IPR009348
  - complex55-agent-ipr-IPR005365
  - complex55-agent-protein-P38742
  - complex55-agent-protein-P39923
  - complex55-agent-protein-P47170
  - complex55-agent-protein-Q00582
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gator1_complex.yaml
    role: maintained scientific record
  rule_id: Exact component grounding and source-backed completeness
  native_severity: minor
  normalization_reason: Structure identity, membership and biological direction remain
    correct; this resolves a bounded existing grounding deferral without changing
    the scientific class.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990130
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gator1_complex.yaml
    role: maintained scientific record
  description: Use IPR027244, IPR009348 and IPR005365 respectively, with the existing
    yeast roles and human counterpart scope intact.
  acceptance_checks:
  - Keep Rag GTPases and SEACAT outside the three-member constituent boundary.
  - Preserve supported identities and source scope; pass applicable native gates.
limitations:
- Five completed same-base batch26 global gates await guarded parent manifest/hash
  integration.
- No supplemental experiments or atomic coordinates were independently analyzed. Source
  reading is limited to the exact evidence locators.
- The retained SciSignal2013 author-PDF routes returned503. A transient browser display
  was not retained with a complete response receipt and is not used as hashed full-body
  evidence; formal SciSignal support here is its complete native abstract, supplemented
  by the separately read CellCycle body.
- Huh2003 and, for GATOR2, Rout2000 were read at native complete-abstract scope. UniProt
  annotation-source placement is verified, but a multi-reference annotation is not
  taken to mean every cited paper independently tested every localization.
- Dokudovskaya Npr3 fluorescence was below detection and earlier Sea2 atlas localization
  differed; the record accurately reports the current UniProt annotation rather than
  claiming a fresh reanalysis of those images.
- No SEA/GATOR source figure pixels or supplements were read; functional epistasis
  and direct biochemical activity are distinguished.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
