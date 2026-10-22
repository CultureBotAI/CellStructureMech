# Source-grounded review of exodeoxyribonuclease V complex

- Review: 20261022T065208Z-recbcd-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:27:59Z
- Finished UTC: 2026-10-22T06:52:08Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No actionable issue observed in the declared scope. Exact RecBCD identity, three grounded constituents, reference proteins and bounded DNA-processing graph are supported, with primary abstracts and native PDB metadata distinguished from unread paper bodies.

## Scope And Provenance

Exactly one complete maintained target, with source-native and primary reading scopes declared individually.

Selection: One complete record in strict-path batch 55 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009338 | data/structures/other/exodeoxyribonuclease_v_complex.yaml | maintained | exodeoxyribonuclease V complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0009338 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009338 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0009338 | Focused check passed; scientific claims assessed separately. |
| Native focused verify | passed | True | GO:0009338 | Focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0009338 | No iModulon-specific claim is assessed; the relevant complex/assay evidence was inspected directly. |
| Claim-level scientific review | passed | True | GO:0009338 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0009338 | 13 of 16 collected target identifiers returned OK. PDB:1W36: SKIPPED; Exact RCSB entry identifier, structure title and primary citation DOI/PMID independently read. Deposition-specific composition, ligands and structural interpretation retain the separately reviewed evidence scopes; the paper title does not substitute for entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:15538360: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:1618858: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0009338 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009338 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009338 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009338 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0009338 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact three-protein enzyme identity

identity: supported. Targets: GO:0009338.

GO and native families identify RecB/RecC/RecD exodeoxyribonuclease V. The two declared parents are is_a ancestors. Source evidence supports a protein heterotrimer rather than promoting the bound DNA substrate to a constituent protein.

### Grounded constituents and matched reference examples

grounding: supported. Targets: GO:0009338.

All three exact InterPro classes, taxon-paired reviewed examples, exact-gene queries and RCSB polymer mappings agree. PDB source taxon562 and reference strain83333 are kept separate.

### Reconstitution does not establish universal assembly necessity

grounding: supported. Targets: GO:0009338.

Masterson1992 native abstract reports an approximately330kDa heterotrimer and restoration of nuclease,helicase,ATPase and Chi-specific activities after combining purified subunits. It also reports low RecBC activities at higher concentration/shorter substrates. Those activity comparisons do not justify reinstating the previously removed formation-essentiality claims.

### Bounded substrate-processing graph

graph: supported. Targets: GO:0009338.

The NONMECHANISTIC graph records whole-complex ATP-dependent cleavage, constituent contributions and DNA binding. Singleton abstract and native PDB substrate metadata support DNA-end engagement; GO supplies the reaction/products. This graph does not assert that RecC independently catalyzes cleavage or resolve Chi gating and RecA loading.

### Deposited versus canonical and reference organisms

scope: supported. Targets: GO:0009338.

The canonical E.coli example is supported by the three deposition source organisms. Reviewed K12 protein identities do not change the broader deposited source labels or prove an all-bacteria distribution.

### Complete maintained target and bounded follow-up

completeness: supported. Targets: GO:0009338.

Every maintained field, evidence row, component/example, graph edge, discussion and history entry was read. Optional unpopulated slots are not defects. Scientific status/history remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/exodeoxyribonuclease_v_complex.yaml; Entire maintained target, including all components, evidence, graph edges, discussions and history | context_only | The complete target was read. The maintained YAML owns any later scientific correction. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope | context_only | Formation necessity is distinct from activity, localization and viability. COMMON is the qualitative category present in most members with exceptional losses, not a measured prevalence census. |
| curation | docs/CURATION.md; Exact class identity and taxon-paired protein examples | context_only | Protein examples do not replace constituent-class grounding. Shared domains and broader paralog families do not resolve exact class tasks. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Scope and edge-level source support | context_only | Descriptive membership graphs need not assert a complete mechanism; a directly observed conditional physical dependency can be stated without making every constituent universally essential. |
| root55-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000145,GO:0005802,GO:0006887,GO:0006893,GO:0008854,GO:0009338,GO:0032991,GO:0034044,GO:0140535,GO:1902494; Ten native terms: identities, status, complete definitions/comments/synonyms and relevant typed child relations only | supports | GO0009338 identifies exodeoxyribonuclease V, GO0140535 and GO1902494 are its declared is_a parents, and GO0008854 defines its ATP-dependent exonucleolytic reaction. |
| root55-sources-GO0009338-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009338/ancestors?relations=is_a; Complete native ancestor response | supports | The complete is_a-only ancestry corroborates the focal identity and any declared parent; it is not a parthood or occurrence survey. |
| root55-sources-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxonomy response | supports | Native taxId562 identifies Escherichia coli; species and reference-strain scopes remain distinct. |
| root55-sources-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxonomy response | supports | Native taxId83333 identifies Escherichia coli K-12; species and reference-strain scopes remain distinct. |
| root55-sources-pmid-15538360 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15538360+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED15538360: Crystal structure of RecBCD enzyme reveals a machine for processing DNA breaks. Singleton MR, Dillingham MS, Gaudier M, Kowalczykowski SC, Wigley DB. (2004); DOI10.1038/nature02988. Entire native abstract read; this row does not claim the paper body. |
| root55-sources-pmid-1618858 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A1618858+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED1618858: Reconstitution of the activities of the RecBCD holoenzyme of Escherichia coli from the purified subunits. Masterson C, Boehmer PE, McDonald F, Chaudhuri S, Hickson ID, Emmerson PT. (1992); DOI10.1016/s0021-9258(18)42249-1. Entire native abstract read; this row does not claim the paper body. |
| root55-sources-doi-10.1038_nature02988 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature02988%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED15538360: Crystal structure of RecBCD enzyme reveals a machine for processing DNA breaks. Singleton MR, Dillingham MS, Gaudier M, Kowalczykowski SC, Wigley DB. (2004). Complete native abstract read; separately declared body evidence has narrower locators. |
| root55-sources-protein-P08394 | https://rest.uniprot.org/uniprotkb/P08394.json; Identity/status, recommended and alternative names, genes/aliases, organism; InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | P08394 matches the declared reviewed recB example and reference taxon. Native function, membership, localization and family annotations were distinguished from direct primary experiments. |
| root55-sources-gene-recB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ArecB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set with gene/aliases, status and organism; native exact-gene, organism_id, reviewed and size500 parameters | supports | Exact-gene reviewed query restricted to the declared organism_id returns only P08394. |
| root55-sources-protein-P07648 | https://rest.uniprot.org/uniprotkb/P07648.json; Identity/status, recommended and alternative names, genes/aliases, organism; InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | P07648 matches the declared reviewed recC example and reference taxon. Native function, membership, localization and family annotations were distinguished from direct primary experiments. |
| root55-sources-gene-recC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ArecC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set with gene/aliases, status and organism; native exact-gene, organism_id, reviewed and size500 parameters | supports | Exact-gene reviewed query restricted to the declared organism_id returns only P07648. |
| root55-sources-protein-P04993 | https://rest.uniprot.org/uniprotkb/P04993.json; Identity/status, recommended and alternative names, genes/aliases, organism; InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | P04993 matches the declared reviewed recD example and reference taxon. Native function, membership, localization and family annotations were distinguished from direct primary experiments. |
| root55-sources-gene-recD | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ArecD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set with gene/aliases, status and organism; native exact-gene, organism_id, reviewed and size500 parameters | supports | Exact-gene reviewed query restricted to the declared organism_id returns only P04993. |
| root55-sources-ipr-IPR004586 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004586/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | Native exact RecBCD RecB family, with its integrated signatures and hierarchy. Broader ancestors and generic annotation prose are not substituted for this exact class. |
| root55-sources-ipr-IPR006697 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006697/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | Native exact RecBCD RecC family, with its integrated signatures and hierarchy. Broader ancestors and generic annotation prose are not substituted for this exact class. |
| root55-sources-ipr-IPR006344 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006344/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | Native exact RecBCD RecD family, with its integrated signatures and hierarchy. Broader ancestors and generic annotation prose are not substituted for this exact class. |
| root55-sources-pdb-entry-1W36 | https://data.rcsb.org/rest/v1/core/entry/1W36; Entry identifier/title, primary citation, experimental method and entry composition/resolution metadata | supports | RCSB1W36 is RecBCD:DNA, with Singleton2004 DOI10.1038/nature02988 and PMID15538360. Native entry metadata gives X-ray diffraction at3.1A and two assemblies; no coordinates were reanalyzed. |
| root55-sources-pdb-assembly-1W36-1 | https://data.rcsb.org/rest/v1/core/assembly/1W36/1; Assembly identifier, oligomeric details and complete rcsb_assembly_info | supports | Assembly1 contains three protein instances and one DNA instance. Its oligomeric_count4 includes DNA and does not make the protein enzyme a heterotetramer. Deposited duplicate protein-chain counts are distinguished from one biological assembly. |
| root55-sources-pdb-polymer_entity-1W36-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/1W36/1; Entity name/type, identifiers/SIFTS mapping, chain IDs/counts, sequence-length and mutation metadata, source and expression-host identities; sequence letters were not analyzed | supports | Entity 1 is the 1180-residue RecB protein, mapped by SIFTS to P08394, with deposited E. coli source taxon 562. |
| root55-sources-pdb-polymer_entity-1W36-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/1W36/2; Entity name/type, identifiers/SIFTS mapping, chain IDs/counts, sequence-length and mutation metadata, source and expression-host identities; sequence letters were not analyzed | supports | Entity 2 is the 1122-residue RecC protein, mapped by SIFTS to P07648, with deposited E. coli source taxon 562. |
| root55-sources-pdb-polymer_entity-1W36-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/1W36/3; Entity name/type, identifiers/SIFTS mapping, chain IDs/counts, sequence-length and mutation metadata, source and expression-host identities; sequence letters were not analyzed | supports | Entity 3 is the 608-residue RecD protein, mapped by SIFTS to P04993, with deposited E. coli source taxon 562. |
| root55-sources-pdb-polymer_entity-1W36-4 | https://data.rcsb.org/rest/v1/core/polymer_entity/1W36/4; Entity name/type, identifiers/SIFTS mapping, chain IDs/counts, sequence-length and mutation metadata, source and expression-host identities; sequence letters were not analyzed | supports | Entity 4 is a synthetic 43-nucleotide DNA hairpin, classified as DNA rather than protein; this response has no UniProt protein mapping. |
| access-singleton-publisher | https://www.nature.com/articles/nature02988; Retrieved response status/content type and diagnostic body only | context_only | HTTP200 returned a client challenge, not the readable Nature paper body. |
| access-masterson-pdf | https://www.jbc.org/article/S0021-9258(18)42249-1/pdf; Retrieved response status/content type and diagnostic body only | context_only | HTTP403 challenge response, not a readable PDF. |
| schema-result | just validate data/structures/other/exodeoxyribonuclease_v_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/exodeoxyribonuclease_v_complex.yaml |
| strict-result | just validate-strict data/structures/other/exodeoxyribonuclease_v_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exodeoxyribonuclease_v_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/exodeoxyribonuclease_v_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exodeoxyribonuclease_v_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exodeoxyribonuclease_v_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/exodeoxyribonuclease_v_complex.yaml --causal-graphs; Complete focused native report | supports | data/structures/other/exodeoxyribonuclease_v_complex.yaml  (GO:0009338)<br>  recbcd_dna_break_processing	recb_subunit	COVERED	-&gt;recb_subunit (UniProtKB:P08394)<br>  recbcd_dna_break_processing	recc_subunit	COVERED	-&gt;recc_subunit (UniProtKB:P07648)<br>  recbcd_dna_break_processing	recd_subunit	COVERED	-&gt;recd_subunit (UniProtKB:P04993)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/exodeoxyribonuclease_v_complex.yaml --verify; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/exodeoxyribonuclease_v_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 16 collected target identifiers returned OK. PDB:1W36: SKIPPED; Exact RCSB entry identifier, structure title and primary citation DOI/PMID independently read. Deposition-specific composition, ligands and structural interpretation retain the separately reviewed evidence scopes; the paper title does not substitute for entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:15538360: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:1618858: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw datasets, atomic coordinates, sequence alignments or supplemental files were reanalyzed. Body reading is bounded by the exact evidence locators.
- Singleton2004 and Masterson1992 were read at complete native abstract tier. RCSB entry, assembly and polymer metadata were inspected directly; paper bodies and coordinate-level mechanisms were not inspected.
- The observed activity restoration does not establish every component as universally necessary for physical assembly. No observed issue requires a scientific correction within this scope.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations and issue-bearing reviews alike.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T065208Z-recbcd-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of exodeoxyribonuclease V complex
started_at: '2026-10-22T06:27:59Z'
finished_at: '2026-10-22T06:52:08Z'
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
summary: No actionable issue observed in the declared scope. Exact RecBCD identity,
  three grounded constituents, reference proteins and bounded DNA-processing graph
  are supported, with primary abstracts and native PDB metadata distinguished from
  unread paper bodies.
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
  - path: data/structures/other/exodeoxyribonuclease_v_complex.yaml
    sha256: 520153b05eb0538317626522c15f966a14e2d050155952c04e0ec46dcd7ee028
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
- target_id: GO:0009338
  path: data/structures/other/exodeoxyribonuclease_v_complex.yaml
  label: exodeoxyribonuclease V complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/exodeoxyribonuclease_v_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, with source-native and primary
    reading scopes declared individually.
  selection: One complete record in strict-path batch 55 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009338
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009338
  command: just validate data/structures/other/exodeoxyribonuclease_v_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009338
  command: just validate-strict data/structures/other/exodeoxyribonuclease_v_complex.yaml
    --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exodeoxyribonuclease_v_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0009338
  command: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/exodeoxyribonuclease_v_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0009338
  command: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/exodeoxyribonuclease_v_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0009338
  summary: No iModulon-specific claim is assessed; the relevant complex/assay evidence
    was inspected directly.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009338
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root55-sources-go
  - root55-sources-GO0009338-ancestors
  - root55-sources-tax-562
  - root55-sources-tax-83333
  - root55-sources-pmid-15538360
  - root55-sources-pmid-1618858
  - root55-sources-doi-10.1038_nature02988
  - root55-sources-protein-P08394
  - root55-sources-gene-recB
  - root55-sources-protein-P07648
  - root55-sources-gene-recC
  - root55-sources-protein-P04993
  - root55-sources-gene-recD
  - root55-sources-ipr-IPR004586
  - root55-sources-ipr-IPR006697
  - root55-sources-ipr-IPR006344
  - root55-sources-pdb-entry-1W36
  - root55-sources-pdb-assembly-1W36-1
  - root55-sources-pdb-polymer_entity-1W36-1
  - root55-sources-pdb-polymer_entity-1W36-2
  - root55-sources-pdb-polymer_entity-1W36-3
  - root55-sources-pdb-polymer_entity-1W36-4
  - access-singleton-publisher
  - access-masterson-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0009338
  summary: '13 of 16 collected target identifiers returned OK. PDB:1W36: SKIPPED;
    Exact RCSB entry identifier, structure title and primary citation DOI/PMID independently
    read. Deposition-specific composition, ligands and structural interpretation retain
    the separately reviewed evidence scopes; the paper title does not substitute for
    entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:15538360:
    UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read
    following the bulk eutils414 transport failure. Resolution is identifier identity
    only; separate primary-body/abstract evidence limits remain in force.; PMID:1618858:
    UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read
    following the bulk eutils414 transport failure. Resolution is identifier identity
    only; separate primary-body/abstract evidence limits remain in force. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.'
  evidence_ids:
  - target-curies
  - root55-sources-pdb-entry-1W36
  - root55-sources-pmid-15538360
  - root55-sources-pmid-1618858
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009338
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
  - GO:0009338
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
  - GO:0009338
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
  - GO:0009338
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
  - GO:0009338
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
  reference: data/structures/other/exodeoxyribonuclease_v_complex.yaml
  locator: Entire maintained target, including all components, evidence, graph edges,
    discussions and history
  accessed_at: '2026-10-22T06:45:32Z'
  support: context_only
  summary: The complete target was read. The maintained YAML owns any later scientific
    correction.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope
  accessed_at: '2026-10-22T06:45:32Z'
  support: context_only
  summary: Formation necessity is distinct from activity, localization and viability.
    COMMON is the qualitative category present in most members with exceptional losses,
    not a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and taxon-paired protein examples
  accessed_at: '2026-10-22T06:45:32Z'
  support: context_only
  summary: Protein examples do not replace constituent-class grounding. Shared domains
    and broader paralog families do not resolve exact class tasks.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope and edge-level source support
  accessed_at: '2026-10-22T06:45:32Z'
  support: context_only
  summary: Descriptive membership graphs need not assert a complete mechanism; a directly
    observed conditional physical dependency can be stated without making every constituent
    universally essential.
- evidence_id: root55-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000145,GO:0005802,GO:0006887,GO:0006893,GO:0008854,GO:0009338,GO:0032991,GO:0034044,GO:0140535,GO:1902494
  locator: 'Ten native terms: identities, status, complete definitions/comments/synonyms
    and relevant typed child relations only'
  accessed_at: '2026-10-22T06:38:51.764560Z'
  support: supports
  summary: GO0009338 identifies exodeoxyribonuclease V, GO0140535 and GO1902494 are
    its declared is_a parents, and GO0008854 defines its ATP-dependent exonucleolytic
    reaction.
  snapshot_sha256: 30bebfa68466084ceae0cad027ebee585d5b955925774938ac3aac92d37c72d7
- evidence_id: root55-sources-GO0009338-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009338/ancestors?relations=is_a
  locator: Complete native ancestor response
  accessed_at: '2026-10-22T06:39:10.702568Z'
  support: supports
  summary: The complete is_a-only ancestry corroborates the focal identity and any
    declared parent; it is not a parthood or occurrence survey.
  snapshot_sha256: 2f50c01c68b8a9540c5d050f4a2708b01d032e0a7c4dd28658eb093d42c84700
- evidence_id: root55-sources-tax-562
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:38:53.630918Z'
  support: supports
  summary: Native taxId562 identifies Escherichia coli; species and reference-strain
    scopes remain distinct.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: root55-sources-tax-83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:38:53.777303Z'
  support: supports
  summary: Native taxId83333 identifies Escherichia coli K-12; species and reference-strain
    scopes remain distinct.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: root55-sources-pmid-15538360
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15538360+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T06:39:01.620301Z'
  support: supports
  summary: 'MED15538360: Crystal structure of RecBCD enzyme reveals a machine for
    processing DNA breaks. Singleton MR, Dillingham MS, Gaudier M, Kowalczykowski
    SC, Wigley DB. (2004); DOI10.1038/nature02988. Entire native abstract read; this
    row does not claim the paper body.'
  snapshot_sha256: 5515e6ec304b3af8f8bdbe0e23e00582648a5b8c0cbdfc657eeb6b203ded14eb
- evidence_id: root55-sources-pmid-1618858
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A1618858+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T06:39:02.331937Z'
  support: supports
  summary: 'MED1618858: Reconstitution of the activities of the RecBCD holoenzyme
    of Escherichia coli from the purified subunits. Masterson C, Boehmer PE, McDonald
    F, Chaudhuri S, Hickson ID, Emmerson PT. (1992); DOI10.1016/s0021-9258(18)42249-1.
    Entire native abstract read; this row does not claim the paper body.'
  snapshot_sha256: 90aabe26446fc93a9e2ee933915a9fe7d0f350927c3c7476202995bf106886bb
- evidence_id: root55-sources-doi-10.1038_nature02988
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature02988%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique native DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T06:39:04.209607Z'
  support: supports
  summary: 'Unique DOI result MED15538360: Crystal structure of RecBCD enzyme reveals
    a machine for processing DNA breaks. Singleton MR, Dillingham MS, Gaudier M, Kowalczykowski
    SC, Wigley DB. (2004). Complete native abstract read; separately declared body
    evidence has narrower locators.'
  snapshot_sha256: a5126a4ef176eadfb84b86d5d77b6f333f8ee33bf4ce811664ac240624e9d261
- evidence_id: root55-sources-protein-P08394
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P08394.json
  locator: Identity/status, recommended and alternative names, genes/aliases, organism;
    InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC
    ACTIVITY and SIMILARITY comments where present
  accessed_at: '2026-10-22T06:38:55.551584Z'
  support: supports
  summary: P08394 matches the declared reviewed recB example and reference taxon.
    Native function, membership, localization and family annotations were distinguished
    from direct primary experiments.
  snapshot_sha256: 48feb52c54e9c20fb181b97e20fa55fdae3b6abd38bbf1ce66b07d78bcd89c5c
- evidence_id: root55-sources-gene-recB
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ArecB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set with gene/aliases, status and organism; native
    exact-gene, organism_id, reviewed and size500 parameters
  accessed_at: '2026-10-22T06:39:10.717936Z'
  support: supports
  summary: Exact-gene reviewed query restricted to the declared organism_id returns
    only P08394.
  snapshot_sha256: 083c95092ecef09c67bbb2e96090bc2ec2b038a909e81b4fe7e22a3d0009eb02
- evidence_id: root55-sources-protein-P07648
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P07648.json
  locator: Identity/status, recommended and alternative names, genes/aliases, organism;
    InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC
    ACTIVITY and SIMILARITY comments where present
  accessed_at: '2026-10-22T06:38:55.103362Z'
  support: supports
  summary: P07648 matches the declared reviewed recC example and reference taxon.
    Native function, membership, localization and family annotations were distinguished
    from direct primary experiments.
  snapshot_sha256: ef459887c8427389501da1e7d14d1096c0bb41e177fdfa9a120e0195ceb51066
- evidence_id: root55-sources-gene-recC
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ArecC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set with gene/aliases, status and organism; native
    exact-gene, organism_id, reviewed and size500 parameters
  accessed_at: '2026-10-22T06:39:11.293825Z'
  support: supports
  summary: Exact-gene reviewed query restricted to the declared organism_id returns
    only P07648.
  snapshot_sha256: 9c848f22d60a233d03e755b6dd2c67aeb48fbac9f716955ba1dd0ea07d5ab1b5
- evidence_id: root55-sources-protein-P04993
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P04993.json
  locator: Identity/status, recommended and alternative names, genes/aliases, organism;
    InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC
    ACTIVITY and SIMILARITY comments where present
  accessed_at: '2026-10-22T06:38:54.223952Z'
  support: supports
  summary: P04993 matches the declared reviewed recD example and reference taxon.
    Native function, membership, localization and family annotations were distinguished
    from direct primary experiments.
  snapshot_sha256: 058c9f19f6606a0afe3e5c66ed3ad97e1c8bef8dcaac1cecd69d910321621ee8
- evidence_id: root55-sources-gene-recD
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ArecD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set with gene/aliases, status and organism; native
    exact-gene, organism_id, reviewed and size500 parameters
  accessed_at: '2026-10-22T06:39:11.736841Z'
  support: supports
  summary: Exact-gene reviewed query restricted to the declared organism_id returns
    only P04993.
  snapshot_sha256: 047e212e64933b340088a8787a2973aea09a8ab68cbf88d60302c4d4b5362131
- evidence_id: root55-sources-ipr-IPR004586
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004586/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:38:51.764850Z'
  support: supports
  summary: Native exact RecBCD RecB family, with its integrated signatures and hierarchy.
    Broader ancestors and generic annotation prose are not substituted for this exact
    class.
  snapshot_sha256: 76c0f6811a39fa2770765d92a7244b85b3eeed92fa2f3c896ed62f903805e5e7
- evidence_id: root55-sources-ipr-IPR006697
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006697/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:38:52.558621Z'
  support: supports
  summary: Native exact RecBCD RecC family, with its integrated signatures and hierarchy.
    Broader ancestors and generic annotation prose are not substituted for this exact
    class.
  snapshot_sha256: 6cbb6d7418ddd10ca600a5f61b4b4e33d51cbc2addbbdc2d61e425286ccc3e4d
- evidence_id: root55-sources-ipr-IPR006344
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006344/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:38:52.461593Z'
  support: supports
  summary: Native exact RecBCD RecD family, with its integrated signatures and hierarchy.
    Broader ancestors and generic annotation prose are not substituted for this exact
    class.
  snapshot_sha256: 5778c1fe08d27cd183cfe177721b700b6ce93346bd594756993ab55b0685c1da
- evidence_id: root55-sources-pdb-entry-1W36
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1W36
  locator: Entry identifier/title, primary citation, experimental method and entry
    composition/resolution metadata
  accessed_at: '2026-10-22T06:39:14.654578Z'
  support: supports
  summary: RCSB1W36 is RecBCD:DNA, with Singleton2004 DOI10.1038/nature02988 and PMID15538360.
    Native entry metadata gives X-ray diffraction at3.1A and two assemblies; no coordinates
    were reanalyzed.
  snapshot_sha256: 325138f4f8b2139f551e78bad21a361e103a9dc12e7e1fd9eab9852054220c1c
- evidence_id: root55-sources-pdb-assembly-1W36-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/1W36/1
  locator: Assembly identifier, oligomeric details and complete rcsb_assembly_info
  accessed_at: '2026-10-22T06:39:14.730490Z'
  support: supports
  summary: Assembly1 contains three protein instances and one DNA instance. Its oligomeric_count4
    includes DNA and does not make the protein enzyme a heterotetramer. Deposited
    duplicate protein-chain counts are distinguished from one biological assembly.
  snapshot_sha256: 9ba07b7638e6c5b6549165f00e34e3ecfcdf97333e9ddf36d220d3b8bc8695c7
- evidence_id: root55-sources-pdb-polymer_entity-1W36-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1W36/1
  locator: Entity name/type, identifiers/SIFTS mapping, chain IDs/counts, sequence-length
    and mutation metadata, source and expression-host identities; sequence letters
    were not analyzed
  accessed_at: '2026-10-22T06:39:14.791125Z'
  support: supports
  summary: Entity 1 is the 1180-residue RecB protein, mapped by SIFTS to P08394, with
    deposited E. coli source taxon 562.
  snapshot_sha256: 8e9f4ffb31db609334e2a53c1cd677ced63a182763fe100940475b729803dbee
- evidence_id: root55-sources-pdb-polymer_entity-1W36-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1W36/2
  locator: Entity name/type, identifiers/SIFTS mapping, chain IDs/counts, sequence-length
    and mutation metadata, source and expression-host identities; sequence letters
    were not analyzed
  accessed_at: '2026-10-22T06:39:14.877895Z'
  support: supports
  summary: Entity 2 is the 1122-residue RecC protein, mapped by SIFTS to P07648, with
    deposited E. coli source taxon 562.
  snapshot_sha256: c03d1291f7b733e203c58bfa5a8b5045f9a59d46493b8dab0c2a665ca944fc8c
- evidence_id: root55-sources-pdb-polymer_entity-1W36-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1W36/3
  locator: Entity name/type, identifiers/SIFTS mapping, chain IDs/counts, sequence-length
    and mutation metadata, source and expression-host identities; sequence letters
    were not analyzed
  accessed_at: '2026-10-22T06:39:14.957278Z'
  support: supports
  summary: Entity 3 is the 608-residue RecD protein, mapped by SIFTS to P04993, with
    deposited E. coli source taxon 562.
  snapshot_sha256: 61044aedd3565177bf3d8d65a1afd462519ba529456e0b01d36234524201aeb2
- evidence_id: root55-sources-pdb-polymer_entity-1W36-4
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1W36/4
  locator: Entity name/type, identifiers/SIFTS mapping, chain IDs/counts, sequence-length
    and mutation metadata, source and expression-host identities; sequence letters
    were not analyzed
  accessed_at: '2026-10-22T06:39:15.039651Z'
  support: supports
  summary: Entity 4 is a synthetic 43-nucleotide DNA hairpin, classified as DNA rather
    than protein; this response has no UniProt protein mapping.
  snapshot_sha256: ad1cee0eec0c5f399f712545ecc0156dfd2eed4c893c6b13915bf0a7b39d399d
- evidence_id: access-singleton-publisher
  kind: primary_source
  reference: https://www.nature.com/articles/nature02988
  locator: Retrieved response status/content type and diagnostic body only
  accessed_at: '2026-10-22T06:40:05.980218Z'
  support: context_only
  summary: HTTP200 returned a client challenge, not the readable Nature paper body.
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: access-masterson-pdf
  kind: primary_source
  reference: https://www.jbc.org/article/S0021-9258(18)42249-1/pdf
  locator: Retrieved response status/content type and diagnostic body only
  accessed_at: '2026-10-22T06:40:06.086205Z'
  support: context_only
  summary: HTTP403 challenge response, not a readable PDF.
  snapshot_sha256: d2d5961e616dc5dfdd9ba818de5874556e0c3c29a98ac2cb85adb638bbc1ed25
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/exodeoxyribonuclease_v_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:28:01Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/exodeoxyribonuclease_v_complex.yaml'
  snapshot_sha256: e6102a5e8d27ff3f7e9fbd8efc87c12b3f40141b3a90597809224a9fb7d8ec69
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/exodeoxyribonuclease_v_complex.yaml
    --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exodeoxyribonuclease_v_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:28:03Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/exodeoxyribonuclease_v_complex.yaml\
    \ --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exodeoxyribonuclease_v_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exodeoxyribonuclease_v_complex-strict.tsv"
  snapshot_sha256: f91355a9adede1ca254c6c9e7fe2ebc9886a21dd3e20d75b348709d47e084ccd
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/exodeoxyribonuclease_v_complex.yaml
    --causal-graphs
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:38:55.085908Z'
  support: supports
  summary: "data/structures/other/exodeoxyribonuclease_v_complex.yaml  (GO:0009338)\n\
    \  recbcd_dna_break_processing\trecb_subunit\tCOVERED\t->recb_subunit (UniProtKB:P08394)\n\
    \  recbcd_dna_break_processing\trecc_subunit\tCOVERED\t->recc_subunit (UniProtKB:P07648)\n\
    \  recbcd_dna_break_processing\trecd_subunit\tCOVERED\t->recd_subunit (UniProtKB:P04993)\n\
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
  snapshot_sha256: 01a53a3123ac3dc4609a368f0b79b9a22d6c7c3430ac66e5cdfa2162bfe008d9
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/exodeoxyribonuclease_v_complex.yaml
    --verify
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:38:56.501078Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/exodeoxyribonuclease_v_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '13 of 16 collected target identifiers returned OK. PDB:1W36: SKIPPED;
    Exact RCSB entry identifier, structure title and primary citation DOI/PMID independently
    read. Deposition-specific composition, ligands and structural interpretation retain
    the separately reviewed evidence scopes; the paper title does not substitute for
    entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:15538360:
    UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read
    following the bulk eutils414 transport failure. Resolution is identifier identity
    only; separate primary-body/abstract evidence limits remain in force.; PMID:1618858:
    UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read
    following the bulk eutils414 transport failure. Resolution is identifier identity
    only; separate primary-body/abstract evidence limits remain in force. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.'
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
  topic: Exact three-protein enzyme identity
  outcome: supported
  target_ids:
  - GO:0009338
  summary: GO and native families identify RecB/RecC/RecD exodeoxyribonuclease V.
    The two declared parents are is_a ancestors. Source evidence supports a protein
    heterotrimer rather than promoting the bound DNA substrate to a constituent protein.
  evidence_ids:
  - record
  - root55-sources-go
  - root55-sources-GO0009338-ancestors
  - root55-sources-pdb-entry-1W36
  - root55-sources-pdb-assembly-1W36-1
  - root55-sources-ipr-IPR004586
  - root55-sources-ipr-IPR006697
  - root55-sources-ipr-IPR006344
  - root55-sources-pdb-polymer_entity-1W36-1
  - root55-sources-pdb-polymer_entity-1W36-2
  - root55-sources-pdb-polymer_entity-1W36-3
  - root55-sources-pdb-polymer_entity-1W36-4
- assessment_id: composition
  area: grounding
  topic: Grounded constituents and matched reference examples
  outcome: supported
  target_ids:
  - GO:0009338
  summary: All three exact InterPro classes, taxon-paired reviewed examples, exact-gene
    queries and RCSB polymer mappings agree. PDB source taxon562 and reference strain83333
    are kept separate.
  evidence_ids:
  - record
  - root55-sources-ipr-IPR004586
  - root55-sources-ipr-IPR006697
  - root55-sources-ipr-IPR006344
  - root55-sources-protein-P08394
  - root55-sources-protein-P07648
  - root55-sources-protein-P04993
  - root55-sources-gene-recB
  - root55-sources-gene-recC
  - root55-sources-gene-recD
  - root55-sources-pdb-polymer_entity-1W36-1
  - root55-sources-pdb-polymer_entity-1W36-2
  - root55-sources-pdb-polymer_entity-1W36-3
  - root55-sources-pdb-polymer_entity-1W36-4
  - root55-sources-tax-562
  - root55-sources-tax-83333
- assessment_id: formation
  area: grounding
  topic: Reconstitution does not establish universal assembly necessity
  outcome: supported
  target_ids:
  - GO:0009338
  summary: Masterson1992 native abstract reports an approximately330kDa heterotrimer
    and restoration of nuclease,helicase,ATPase and Chi-specific activities after
    combining purified subunits. It also reports low RecBC activities at higher concentration/shorter
    substrates. Those activity comparisons do not justify reinstating the previously
    removed formation-essentiality claims.
  evidence_ids:
  - record
  - schema
  - root55-sources-pmid-1618858
  - root55-sources-pdb-assembly-1W36-1
- assessment_id: graph
  area: graph
  topic: Bounded substrate-processing graph
  outcome: supported
  target_ids:
  - GO:0009338
  summary: The NONMECHANISTIC graph records whole-complex ATP-dependent cleavage,
    constituent contributions and DNA binding. Singleton abstract and native PDB substrate
    metadata support DNA-end engagement; GO supplies the reaction/products. This graph
    does not assert that RecC independently catalyzes cleavage or resolve Chi gating
    and RecA loading.
  evidence_ids:
  - record
  - graphs
  - root55-sources-go
  - root55-sources-pdb-entry-1W36
  - root55-sources-pmid-15538360
  - root55-sources-pdb-polymer_entity-1W36-1
  - root55-sources-pdb-polymer_entity-1W36-2
  - root55-sources-pdb-polymer_entity-1W36-3
  - root55-sources-pdb-polymer_entity-1W36-4
- assessment_id: scope
  area: scope
  topic: Deposited versus canonical and reference organisms
  outcome: supported
  target_ids:
  - GO:0009338
  summary: The canonical E.coli example is supported by the three deposition source
    organisms. Reviewed K12 protein identities do not change the broader deposited
    source labels or prove an all-bacteria distribution.
  evidence_ids:
  - record
  - root55-sources-pdb-entry-1W36
  - root55-sources-tax-562
  - root55-sources-tax-83333
  - root55-sources-protein-P08394
  - root55-sources-protein-P07648
  - root55-sources-protein-P04993
  - root55-sources-pdb-polymer_entity-1W36-1
  - root55-sources-pdb-polymer_entity-1W36-2
  - root55-sources-pdb-polymer_entity-1W36-3
  - root55-sources-pdb-polymer_entity-1W36-4
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target and bounded follow-up
  outcome: supported
  target_ids:
  - GO:0009338
  summary: Every maintained field, evidence row, component/example, graph edge, discussion
    and history entry was read. Optional unpopulated slots are not defects. Scientific
    status/history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root55-sources-go
  - root55-sources-doi-10.1038_nature02988
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw datasets, atomic coordinates, sequence alignments or supplemental
  files were reanalyzed. Body reading is bounded by the exact evidence locators.
- Singleton2004 and Masterson1992 were read at complete native abstract tier. RCSB
  entry, assembly and polymer metadata were inspected directly; paper bodies and coordinate-level
  mechanisms were not inspected.
- The observed activity restoration does not establish every component as universally
  necessary for physical assembly. No observed issue requires a scientific correction
  within this scope.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations and issue-bearing reviews
  alike.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
