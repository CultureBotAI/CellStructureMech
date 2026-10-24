# Clathrin coat scientific review

- Review: 20261022T050516Z-clathrin-coat-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:47:07Z
- Finished UTC: 2026-10-22T05:05:16Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Generic clathrin-coat identity and six protein examples are supported. Two bounded minors concern available exact complex groundings and the current APS1 single-entry evidence note.

## Scope And Provenance

Exactly one full maintained target, with the full three-record generic coat/pit coat/pit boundary set (target plus two neighbors), current exact GO/protein/taxon authorities and precisely scoped primary sources. No generated pages or scientific records changed.

Selection: Target 3 of batch47, strict uncovered path order at unchanged origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030118 | data/structures/other/clathrin_coat.yaml | maintained | clathrin coat |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030118 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030118 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0030118 | Native focused check passed; scientific scope independently assessed. |
| Native verify | passed | True | GO:0030118 | Native focused check passed; scientific scope independently assessed. |
| Expression-module applicability | not_applicable | False | GO:0030118 | No expression-module or transcriptomic attribution is made. |
| Claim-level scientific review | passed | True | GO:0030118 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030118 | 16 of 16 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030118 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030118 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030118 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030118 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030118 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Species and experimental backgrounds

scope: supported. Targets: GO:0030118.

The species identity and yeast model are correct. COMMON retains the schema meaning present in most members/losses exception, supported qualitatively by normal yeast cell biology rather than a prevalence census. Newpher uses its specified SL/BWY laboratory strains and temperature/drug conditions, not a universal S288C experiment.

### Clathrin recruitment and endocytic dynamics

evidence: supported. Targets: GO:0030118.

The canonical note stays within Newpher cortical clathrin/adaptor recruitment and site dynamics. Kaksonen complete abstract supports modular coat, invagination, actin and scission behavior, including clathrin facilitating initiation without being essential for invagination or vesicle formation. No direct sealed-vesicle or precise scission observation is inferred from Newpher disappearance alone.

### Exact complex classes versus deferred label-only rows

grounding: concern. Targets: GO:0030118.

The triskelion complex has an exact source-neutral GO0071439 mapping. The AP-type clathrin-binding component also matches GO0030131, narrower than GO0030119; subtype-specific resolution is not required to map this stated class. Both current REVIEWED_LABEL_ONLY rationales therefore defer available exact complex identities.

### Assembly necessity remains unestablished

grounding: unknown. Targets: GO:0030118.

Verified coat constituents, a six-chain triskelion and AP binding behavior do not by themselves demonstrate the requirement of every constituent for formation under every condition. The existing UNKNOWN essentiality values are retained; endocytic-function phenotypes are not silently substituted for coat-assembly necessity.

### Generic coat and subtype boundaries

identity: supported. Targets: GO:0030118.

The exact GO class, definition, synonym and membrane-coat parent agree. The three frozen records distinguish a generic protein coat, its pit-associated subtype and the underlying membrane invagination. The parent includes intracellular and endocytic coats; it need not restrict all representative AP proteins to cortical endocytosis.

### Correct chain and AP-1 examples

grounding: supported. Targets: GO:0030118.

All six reviewed accessions, gene symbols and S288C strain identities agree with native entries. CHC1/CLC1 triskelions and the APL2/APL4/APM1/APS1 AP-1 quartet support the declared component classes. AP-1 examples do not imply all AP-family subtypes are clathrin-binding or that the Newpher cortical events were AP-1-specific.

### APS1 alias multiplicity

evidence: concern. Targets: GO:0030118.

Five current exact reviewed queries are single-hit. APS1 returns both the correct P35181 and unrelated DPS1/P04802 alias match. The role already says representative, but its evidence note still says single reviewed entry; correct only that present-tense uniqueness claim.

### Coarse coat assembly and function

graph: supported. Targets: GO:0030118.

NONMECHANISTIC faithfully bounds polymerization, adaptor linkage and part-of/type relationships. Native complex definitions and chain annotations support these coarse edges; Newpher/Kaksonen support endocytic context without resolving every recruitment or scission mechanism.

### Complete single-record review

completeness: supported. Targets: GO:0030118.

All maintained fields, evidence placement, current discussions and history were read. Positive source-native mappings and bounded source limitations were distinguished from hypothetical missing molecular inventories.

## Findings

### F1: Use the verified exact complex groundings

minor / open / confirmed; issue key: clathrin_coat-exact-complex-grounding.

The current reviewed-label-only rationale says no exact complex grounding was curated or defers subtype mappings, but native GO positively supplies the same declared complex classes: GO0071439 for the triskelion and GO0030131 for the clathrin-binding AP subset.

### F2: Correct the current APS1 single-entry evidence note

minor / open / confirmed; issue key: clathrin-coat-aps1-query-uniqueness.

The exact reviewed APS1/taxon559292 query returns P35181 and the DPS1 entry P04802 through its APS1 alias. The selected P35181 AP-1 sigma identity is correct and the role already says representative; only the evidence note retains an unsupported single-entry claim.

## Recommended Actions And Acceptance Checks

### A1

Ground the triskelion component to GO0071439 and the AP-type clathrin-binding component to GO0030131; update label-only status/rationale and the current TODO without changing valid component IDs, examples or UNKNOWN essentiality.

- Confirm each exact definition matches the component class rather than a protein domain or whole coat.
- Preserve the existing graph component_ref links and subtype boundaries.
- Pass applicable schema, strict, identifier and graph checks.

### A2

Replace the current single-reviewed-entry assertion with an accurate representative/multiple-alias-query description while preserving P35181 and its established AP-1 identity.

- Retain P35181, APS1, taxon559292 and REVIEWED status.
- Distinguish the DPS1 alias match from an AP-1 constituent.
- Preserve historical retrieval dates as historical provenance.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/clathrin_coat.yaml; Complete maintained record including all evidence, graph, discussions and history | context_only | All current fields were read; historical notes are provenance, not independent scientific confirmation. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent grounding, essentiality, COMMON and NONMECHANISTIC graph scope | context_only | Protein complexes may use exact GO complex groundings. UNKNOWN assembly necessity is distinct from verified membership or catalytic function. COMMON means present in most members with losses the exception. |
| curation | docs/CURATION.md; Exact component grounding and REVIEWED_LABEL_ONLY contract, especially lines159–160 | context_only | REVIEWED_LABEL_ONLY denotes an inspected absence of an exact grounding, not merely an exact mapping deferred in the current pass. |
| neighbor-pit-coat | data/structures/other/clathrin_coat_of_coated_pit.yaml; Complete record read for the three-record coat/pit boundary comparison | context_only | The separate generic coat, pit coat and membrane-invagination records preserve distinct biological granularity; this neighbor is not another target of this review. |
| neighbor-pit | data/structures/other/clathrin_coated_pit.yaml; Complete record read for the three-record coat/pit boundary comparison | context_only | The separate generic coat, pit coat and membrane-invagination records preserve distinct biological granularity; this neighbor is not another target of this review. |
| clathrin47-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005768,GO:0005802,GO:0005905,GO:0012510,GO:0016020,GO:0030117,GO:0030118,GO:0030119,GO:0030120,GO:0030121,GO:0030122,GO:0030125,GO:0030128,GO:0030130,GO:0030132,GO:0030136,GO:0030140,GO:0030669,GO:0045334,GO:0072583; Complete active identities/definitions/synonyms and exact typed child links for the target, maintained parents/parts, GO0072583 and named graph structures in the 20-term response | supports | GO0030118 exactly identifies the generic clathrin coat and its membrane-coat is-a parent. Its child relations independently place the clathrin complex and clathrin adaptor complex as parts, while pit and vesicle coats remain distinct subclasses. GO0030119 includes adaptor classes beyond the clathrin-binding subset. |
| clathrin47-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete tax4932 native names/rank/lineage response | supports | ENA confirms Saccharomyces cerevisiae at species rank. |
| clathrin47-agent-newpher2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2005.04.014; Native bibliographic identity/authors/year/DOI and complete abstract | supports | Exact native MED15992543 identity: In vivo dynamics of clathrin and its adaptor-dependent recruitment to the actin-based endocytic machinery in yeast. DOI 10.1016/j.devcel.2005.04.014. Complete abstract inspected; primary-body scope is separately stated. |
| clathrin47-agent-kaksonen2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2005.09.024; Native bibliographic identity/authors/year/DOI and complete abstract | supports | Exact native MED16239147 identity: A modular design for the clathrin- and actin-mediated endocytosis machinery. DOI 10.1016/j.cell.2005.09.024. Complete abstract inspected; primary-body scope is separately stated. |
| clathrin47-agent-newpher2005-duke | https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content; Complete scientific main text pp87–96: Introduction, all Results/Discussion, Table1, Fig1–6 captions and Experimental Procedures. PDF text read, no figure pixels or supplementary movies. | supports | Newpher directly images cortical and internal clathrin patches in budding yeast and temporal association with endocytic factors. The Discussion explicitly cannot distinguish coat loss before budding from movement of a coated bud/vesicle outside the TIRF field. Epsin/AP180 recruitment findings do not demonstrate that AP-1 is the cortical adaptor used in every event. |
| clathrin47-agent-go-triskelion-candidates | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071439,GO:0030131; Complete two exact native terms including active status, names, definitions, exact synonyms and child relationships | supports | Active GO0071439 clathrin complex has exact synonym clathrin triskelion and the three-heavy/three-light-chain definition. Active GO0030131 clathrin adaptor complex defines the AP-type subset linking clathrin to membrane; its AP-1/AP-2 children and the separate GO0030119 hierarchy distinguish it from all AP-family coats. |
| clathrin47-agent-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native tax559292 response | supports | ENA confirms Saccharomyces cerevisiae S288C at strain rank, distinct from the species-level canonical row. |
| clathrin47-agent-protein-P22137 | https://rest.uniprot.org/uniprotkb/P22137.json; Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR LOCATION comments | supports | Reviewed P22137 is Clathrin heavy chain, gene CHC1, taxon559292. The inspected subunit/function comments support its clathrin-chain or AP-1 membership; accession identity alone is not treated as the primary cortical localization experiment. |
| clathrin47-agent-gene-CHC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACHC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene_exact AND organism_id559292 AND reviewed:true query response; size100, all returned results | supports | Exact reviewed gene query for CHC1 in taxon559292 returned 1 entries: P22137. |
| clathrin47-agent-protein-P17891 | https://rest.uniprot.org/uniprotkb/P17891.json; Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR LOCATION comments | supports | Reviewed P17891 is Clathrin light chain, gene CLC1, taxon559292. The inspected subunit/function comments support its clathrin-chain or AP-1 membership; accession identity alone is not treated as the primary cortical localization experiment. |
| clathrin47-agent-gene-CLC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACLC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene_exact AND organism_id559292 AND reviewed:true query response; size100, all returned results | supports | Exact reviewed gene query for CLC1 in taxon559292 returned 1 entries: P17891. |
| clathrin47-agent-protein-P36000 | https://rest.uniprot.org/uniprotkb/P36000.json; Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR LOCATION comments | supports | Reviewed P36000 is AP-1 complex subunit beta-1, gene APL2, taxon559292. The inspected subunit/function comments support its clathrin-chain or AP-1 membership; accession identity alone is not treated as the primary cortical localization experiment. |
| clathrin47-agent-gene-APL2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPL2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene_exact AND organism_id559292 AND reviewed:true query response; size100, all returned results | supports | Exact reviewed gene query for APL2 in taxon559292 returned 1 entries: P36000. |
| clathrin47-agent-protein-Q12028 | https://rest.uniprot.org/uniprotkb/Q12028.json; Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR LOCATION comments | supports | Reviewed Q12028 is AP-1 complex subunit gamma-1, gene APL4, taxon559292. The inspected subunit/function comments support its clathrin-chain or AP-1 membership; accession identity alone is not treated as the primary cortical localization experiment. |
| clathrin47-agent-gene-APL4 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPL4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene_exact AND organism_id559292 AND reviewed:true query response; size100, all returned results | supports | Exact reviewed gene query for APL4 in taxon559292 returned 1 entries: Q12028. |
| clathrin47-agent-protein-Q00776 | https://rest.uniprot.org/uniprotkb/Q00776.json; Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR LOCATION comments | supports | Reviewed Q00776 is AP-1 complex subunit mu-1-I, gene APM1, taxon559292. The inspected subunit/function comments support its clathrin-chain or AP-1 membership; accession identity alone is not treated as the primary cortical localization experiment. |
| clathrin47-agent-gene-APM1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene_exact AND organism_id559292 AND reviewed:true query response; size100, all returned results | supports | Exact reviewed gene query for APM1 in taxon559292 returned 1 entries: Q00776. |
| clathrin47-agent-protein-P35181 | https://rest.uniprot.org/uniprotkb/P35181.json; Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR LOCATION comments | supports | Reviewed P35181 is AP-1 complex subunit sigma-1, gene APS1, taxon559292. The inspected subunit/function comments support its clathrin-chain or AP-1 membership; accession identity alone is not treated as the primary cortical localization experiment. |
| clathrin47-agent-gene-APS1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene_exact AND organism_id559292 AND reviewed:true query response; size100, all returned results | supports | Exact reviewed gene query for APS1 in taxon559292 returned 2 entries: P35181, P04802. P04802 is DPS1 with APS1 as a synonym; P35181 remains the correct AP-1 sigma example. The current evidence note claiming a single reviewed entry is inaccurate. |
| schema-result | just validate data/structures/other/clathrin_coat.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/clathrin_coat.yaml |
| strict-result | just validate-strict data/structures/other/clathrin_coat.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/clathrin_coat.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/other/clathrin_coat.yaml --causal-graphs; Complete native read-only focused report | supports | data/structures/other/clathrin_coat.yaml  (GO:0030118)<br>  clathrin_coat_topology	clathrin_triskelion_scaffold	COVERED	-&gt;clathrin_triskelion_scaffold (UniProtKB:P22137, UniProtKB:P17891)<br>  clathrin_coat_topology	ap_type_clathrin_adaptors	COVERED	-&gt;ap_type_clathrin_adaptors (UniProtKB:P36000, UniProtKB:Q12028, UniProtKB:Q00776, UniProtKB:P35181)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/other/clathrin_coat.yaml --verify; Complete native read-only focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/clathrin_coat.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 16 of 16 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Five completed same-base batch26 global gates remain staged for guarded parent integration; this unsaved draft does not independently rerun or finalize those corpus checks.
- No source figure pixels, supplementary movies, raw experiments or underlying references were independently reanalyzed. Evidence locators distinguish primary body, abstract and native-authority tiers.
- Kaksonen2005 is inspected at exact complete-native-abstract tier; no genuine main body or movies are represented as read. Newpher TIRF disappearance cannot distinguish coat disassembly before budding from movement out of the evanescent field.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user goal authorizes one review for every uncovered record, including honest qualified passes.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T050516Z-clathrin-coat-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Clathrin coat scientific review
started_at: '2026-10-22T04:47:07Z'
finished_at: '2026-10-22T05:05:16Z'
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
summary: Generic clathrin-coat identity and six protein examples are supported. Two
  bounded minors concern available exact complex groundings and the current APS1 single-entry
  evidence note.
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
  - path: data/structures/other/clathrin_coat.yaml
    sha256: 7b118032d28ca3f850fb2a1bb3070ff32923f58df02ae50e326e97e61d2092f7
    role: target
  - path: data/structures/other/clathrin_coat_of_coated_pit.yaml
    sha256: 859f324aa6a2b9ddd65cb2658a052bec387e3f2afd56d1cd49faf42ae663f55e
    role: context
  - path: data/structures/other/clathrin_coated_pit.yaml
    sha256: d64704a67303020e2f3c92a40d1d64ebc830398938e57acd568dc7e29e723e83
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
- target_id: GO:0030118
  path: data/structures/other/clathrin_coat.yaml
  label: clathrin coat
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_coat.yaml
    role: maintained scientific record
scope:
  description: Exactly one full maintained target, with the full three-record generic
    coat/pit coat/pit boundary set (target plus two neighbors), current exact GO/protein/taxon
    authorities and precisely scoped primary sources. No generated pages or scientific
    records changed.
  selection: Target 3 of batch47, strict uncovered path order at unchanged origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030118
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030118
  command: just validate data/structures/other/clathrin_coat.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030118
  command: just validate-strict data/structures/other/clathrin_coat.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030118
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/other/clathrin_coat.yaml --causal-graphs
  exit_code: 0
  summary: Native focused check passed; scientific scope independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0030118
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/other/clathrin_coat.yaml --verify
  exit_code: 0
  summary: Native focused check passed; scientific scope independently assessed.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030118
  summary: No expression-module or transcriptomic attribution is made.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030118
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - neighbor-pit-coat
  - neighbor-pit
  - clathrin47-agent-go
  - clathrin47-agent-tax4932
  - clathrin47-agent-newpher2005-meta
  - clathrin47-agent-kaksonen2005-meta
  - clathrin47-agent-newpher2005-duke
  - clathrin47-agent-go-triskelion-candidates
  - clathrin47-agent-tax559292
  - clathrin47-agent-protein-P22137
  - clathrin47-agent-gene-CHC1
  - clathrin47-agent-protein-P17891
  - clathrin47-agent-gene-CLC1
  - clathrin47-agent-protein-P36000
  - clathrin47-agent-gene-APL2
  - clathrin47-agent-protein-Q12028
  - clathrin47-agent-gene-APL4
  - clathrin47-agent-protein-Q00776
  - clathrin47-agent-gene-APM1
  - clathrin47-agent-protein-P35181
  - clathrin47-agent-gene-APS1
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030118
  summary: 16 of 16 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030118
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0030118
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0030118
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0030118
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0030118
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
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/clathrin_coat.yaml
  locator: Complete maintained record including all evidence, graph, discussions and
    history
  accessed_at: '2026-10-22T04:53:57Z'
  support: context_only
  summary: All current fields were read; historical notes are provenance, not independent
    scientific confirmation.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent grounding, essentiality, COMMON and NONMECHANISTIC
    graph scope
  accessed_at: '2026-10-22T04:53:57Z'
  support: context_only
  summary: Protein complexes may use exact GO complex groundings. UNKNOWN assembly
    necessity is distinct from verified membership or catalytic function. COMMON means
    present in most members with losses the exception.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact component grounding and REVIEWED_LABEL_ONLY contract, especially
    lines159–160
  accessed_at: '2026-10-22T04:53:57Z'
  support: context_only
  summary: REVIEWED_LABEL_ONLY denotes an inspected absence of an exact grounding,
    not merely an exact mapping deferred in the current pass.
- evidence_id: neighbor-pit-coat
  kind: record_content
  reference: data/structures/other/clathrin_coat_of_coated_pit.yaml
  locator: Complete record read for the three-record coat/pit boundary comparison
  accessed_at: '2026-10-22T04:53:57Z'
  support: context_only
  summary: The separate generic coat, pit coat and membrane-invagination records preserve
    distinct biological granularity; this neighbor is not another target of this review.
- evidence_id: neighbor-pit
  kind: record_content
  reference: data/structures/other/clathrin_coated_pit.yaml
  locator: Complete record read for the three-record coat/pit boundary comparison
  accessed_at: '2026-10-22T04:53:57Z'
  support: context_only
  summary: The separate generic coat, pit coat and membrane-invagination records preserve
    distinct biological granularity; this neighbor is not another target of this review.
- evidence_id: clathrin47-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005768,GO:0005802,GO:0005905,GO:0012510,GO:0016020,GO:0030117,GO:0030118,GO:0030119,GO:0030120,GO:0030121,GO:0030122,GO:0030125,GO:0030128,GO:0030130,GO:0030132,GO:0030136,GO:0030140,GO:0030669,GO:0045334,GO:0072583
  locator: Complete active identities/definitions/synonyms and exact typed child links
    for the target, maintained parents/parts, GO0072583 and named graph structures
    in the 20-term response
  accessed_at: '2026-10-22T04:48:27.885977Z'
  support: supports
  summary: GO0030118 exactly identifies the generic clathrin coat and its membrane-coat
    is-a parent. Its child relations independently place the clathrin complex and
    clathrin adaptor complex as parts, while pit and vesicle coats remain distinct
    subclasses. GO0030119 includes adaptor classes beyond the clathrin-binding subset.
  snapshot_sha256: d99cebcf37913222815e3282d94e35f6fa629e25ca25660703949d4f38893d30
- evidence_id: clathrin47-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete tax4932 native names/rank/lineage response
  accessed_at: '2026-10-22T04:15:34.948894Z'
  support: supports
  summary: ENA confirms Saccharomyces cerevisiae at species rank.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: clathrin47-agent-newpher2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2005.04.014
  locator: Native bibliographic identity/authors/year/DOI and complete abstract
  accessed_at: '2026-10-21T10:57:50.523144Z'
  support: supports
  summary: 'Exact native MED15992543 identity: In vivo dynamics of clathrin and its
    adaptor-dependent recruitment to the actin-based endocytic machinery in yeast.
    DOI 10.1016/j.devcel.2005.04.014. Complete abstract inspected; primary-body scope
    is separately stated.'
  snapshot_sha256: c99ec084fa3f65e3b5107699c30f42b09489dbc49d6be518d71ff9352d5a199c
- evidence_id: clathrin47-agent-kaksonen2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2005.09.024
  locator: Native bibliographic identity/authors/year/DOI and complete abstract
  accessed_at: '2026-10-21T11:04:40.023205Z'
  support: supports
  summary: 'Exact native MED16239147 identity: A modular design for the clathrin-
    and actin-mediated endocytosis machinery. DOI 10.1016/j.cell.2005.09.024. Complete
    abstract inspected; primary-body scope is separately stated.'
  snapshot_sha256: b21f04a2ca620468ebafa02936207fe7e04553d44f862f3f18d72a85b6c4aba2
- evidence_id: clathrin47-agent-newpher2005-duke
  kind: primary_source
  reference: https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content
  locator: 'Complete scientific main text pp87–96: Introduction, all Results/Discussion,
    Table1, Fig1–6 captions and Experimental Procedures. PDF text read, no figure
    pixels or supplementary movies.'
  accessed_at: '2026-10-21T11:00:52.091438Z'
  support: supports
  summary: Newpher directly images cortical and internal clathrin patches in budding
    yeast and temporal association with endocytic factors. The Discussion explicitly
    cannot distinguish coat loss before budding from movement of a coated bud/vesicle
    outside the TIRF field. Epsin/AP180 recruitment findings do not demonstrate that
    AP-1 is the cortical adaptor used in every event.
  snapshot_sha256: c848e911372b9afb9902e4a74e3cb3dd66ef90eb5e102024cc95fff648bb6c21
- evidence_id: clathrin47-agent-go-triskelion-candidates
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071439,GO:0030131
  locator: Complete two exact native terms including active status, names, definitions,
    exact synonyms and child relationships
  accessed_at: '2026-10-22T04:48:54.266838Z'
  support: supports
  summary: Active GO0071439 clathrin complex has exact synonym clathrin triskelion
    and the three-heavy/three-light-chain definition. Active GO0030131 clathrin adaptor
    complex defines the AP-type subset linking clathrin to membrane; its AP-1/AP-2
    children and the separate GO0030119 hierarchy distinguish it from all AP-family
    coats.
  snapshot_sha256: a425c7a31777f7b3c4b24ac1e05fc89fcc459966ef577607175f719c142e4e80
- evidence_id: clathrin47-agent-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native tax559292 response
  accessed_at: '2026-10-22T04:15:34.948991Z'
  support: supports
  summary: ENA confirms Saccharomyces cerevisiae S288C at strain rank, distinct from
    the species-level canonical row.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: clathrin47-agent-protein-P22137
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P22137.json
  locator: Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR
    LOCATION comments
  accessed_at: '2026-10-22T04:48:27.888375Z'
  support: supports
  summary: Reviewed P22137 is Clathrin heavy chain, gene CHC1, taxon559292. The inspected
    subunit/function comments support its clathrin-chain or AP-1 membership; accession
    identity alone is not treated as the primary cortical localization experiment.
  snapshot_sha256: 09d51b91c677526fa74c1513304fdd8c51215ce5c9511a6654355fbd16c61648
- evidence_id: clathrin47-agent-gene-CHC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACHC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene_exact AND organism_id559292 AND reviewed:true query
    response; size100, all returned results
  accessed_at: '2026-10-22T04:48:28.846864Z'
  support: supports
  summary: 'Exact reviewed gene query for CHC1 in taxon559292 returned 1 entries:
    P22137.'
  snapshot_sha256: 2a920614f72637e8dca08d8a782c81c920e1e8a01fd1b0b958f6d70602c68b89
  search_scope: UniProtKB exact gene symbol CHC1, taxon559292, reviewed:true; complete
    returned result set, including aliases. This is a bounded authority query, not
    gene absence across all databases.
- evidence_id: clathrin47-agent-protein-P17891
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P17891.json
  locator: Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR
    LOCATION comments
  accessed_at: '2026-10-22T04:48:27.888620Z'
  support: supports
  summary: Reviewed P17891 is Clathrin light chain, gene CLC1, taxon559292. The inspected
    subunit/function comments support its clathrin-chain or AP-1 membership; accession
    identity alone is not treated as the primary cortical localization experiment.
  snapshot_sha256: 1b6e6853470eea45530073217e5f1abcfbe6fba0fc5568df34d83a73130d25af
- evidence_id: clathrin47-agent-gene-CLC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACLC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene_exact AND organism_id559292 AND reviewed:true query
    response; size100, all returned results
  accessed_at: '2026-10-22T04:48:28.900316Z'
  support: supports
  summary: 'Exact reviewed gene query for CLC1 in taxon559292 returned 1 entries:
    P17891.'
  snapshot_sha256: 263ed77f230c390b1cf03ce642b609d8cff66ef219794d4c6bccab47942bbc69
  search_scope: UniProtKB exact gene symbol CLC1, taxon559292, reviewed:true; complete
    returned result set, including aliases. This is a bounded authority query, not
    gene absence across all databases.
- evidence_id: clathrin47-agent-protein-P36000
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36000.json
  locator: Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR
    LOCATION comments
  accessed_at: '2026-10-22T04:15:34.949204Z'
  support: supports
  summary: Reviewed P36000 is AP-1 complex subunit beta-1, gene APL2, taxon559292.
    The inspected subunit/function comments support its clathrin-chain or AP-1 membership;
    accession identity alone is not treated as the primary cortical localization experiment.
  snapshot_sha256: 526b13f0578f674f0da6edd6f5d896d27525277aaa24102a9f138d00afb7c2f0
- evidence_id: clathrin47-agent-gene-APL2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPL2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene_exact AND organism_id559292 AND reviewed:true query
    response; size100, all returned results
  accessed_at: '2026-10-22T04:15:35.899164Z'
  support: supports
  summary: 'Exact reviewed gene query for APL2 in taxon559292 returned 1 entries:
    P36000.'
  snapshot_sha256: 43e854e42512755d38608a38375b2f320cf989cd66644bf4dbeec296798c6006
  search_scope: UniProtKB exact gene symbol APL2, taxon559292, reviewed:true; complete
    returned result set, including aliases. This is a bounded authority query, not
    gene absence across all databases.
- evidence_id: clathrin47-agent-protein-Q12028
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12028.json
  locator: Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR
    LOCATION comments
  accessed_at: '2026-10-22T04:15:35.760679Z'
  support: supports
  summary: Reviewed Q12028 is AP-1 complex subunit gamma-1, gene APL4, taxon559292.
    The inspected subunit/function comments support its clathrin-chain or AP-1 membership;
    accession identity alone is not treated as the primary cortical localization experiment.
  snapshot_sha256: 7b81a7d2f259bb7cebda9a454da0bdef2f2cad9042a287d72432713b1464de9c
- evidence_id: clathrin47-agent-gene-APL4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPL4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene_exact AND organism_id559292 AND reviewed:true query
    response; size100, all returned results
  accessed_at: '2026-10-22T04:15:35.979624Z'
  support: supports
  summary: 'Exact reviewed gene query for APL4 in taxon559292 returned 1 entries:
    Q12028.'
  snapshot_sha256: f0f5f1c2494566eeb96c492f6225a4c186a5c40ac3adc76c1a294d14ce64920b
  search_scope: UniProtKB exact gene symbol APL4, taxon559292, reviewed:true; complete
    returned result set, including aliases. This is a bounded authority query, not
    gene absence across all databases.
- evidence_id: clathrin47-agent-protein-Q00776
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q00776.json
  locator: Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR
    LOCATION comments
  accessed_at: '2026-10-22T04:15:35.874306Z'
  support: supports
  summary: Reviewed Q00776 is AP-1 complex subunit mu-1-I, gene APM1, taxon559292.
    The inspected subunit/function comments support its clathrin-chain or AP-1 membership;
    accession identity alone is not treated as the primary cortical localization experiment.
  snapshot_sha256: de4a35f47bed9a42163c4850e0c8be64e1a3c1041a655a53cf00c9071ccd174c
- evidence_id: clathrin47-agent-gene-APM1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene_exact AND organism_id559292 AND reviewed:true query
    response; size100, all returned results
  accessed_at: '2026-10-22T04:15:36.452873Z'
  support: supports
  summary: 'Exact reviewed gene query for APM1 in taxon559292 returned 1 entries:
    Q00776.'
  snapshot_sha256: 9d0251049fa9718e8bc777afe874497ae899fd5266fed0462cadb8474b17cfd6
  search_scope: UniProtKB exact gene symbol APM1, taxon559292, reviewed:true; complete
    returned result set, including aliases. This is a bounded authority query, not
    gene absence across all databases.
- evidence_id: clathrin47-agent-protein-P35181
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P35181.json
  locator: Native primary accession, status, protein name, genes, organism and SUBUNIT/FUNCTION/SUBCELLULAR
    LOCATION comments
  accessed_at: '2026-10-22T04:15:35.880526Z'
  support: supports
  summary: Reviewed P35181 is AP-1 complex subunit sigma-1, gene APS1, taxon559292.
    The inspected subunit/function comments support its clathrin-chain or AP-1 membership;
    accession identity alone is not treated as the primary cortical localization experiment.
  snapshot_sha256: d6393e7fc10d38610adc6e52a17a230fe2ab9ec35268039718826364a1480fbb
- evidence_id: clathrin47-agent-gene-APS1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene_exact AND organism_id559292 AND reviewed:true query
    response; size100, all returned results
  accessed_at: '2026-10-22T04:15:36.553905Z'
  support: supports
  summary: 'Exact reviewed gene query for APS1 in taxon559292 returned 2 entries:
    P35181, P04802. P04802 is DPS1 with APS1 as a synonym; P35181 remains the correct
    AP-1 sigma example. The current evidence note claiming a single reviewed entry
    is inaccurate.'
  snapshot_sha256: c97e8ef19fb1de6f681e884ef0174cc3581ecacefdceeb4353fa6520049aed59
  search_scope: UniProtKB exact gene symbol APS1, taxon559292, reviewed:true; complete
    returned result set, including aliases. This is a bounded authority query, not
    gene absence across all databases.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/clathrin_coat.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:09Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/clathrin_coat.yaml'
  snapshot_sha256: fc7c915684245bbda523cd0a67bc00b057588e66d6830d8282579f1d3608a8ad
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/clathrin_coat.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:11Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/clathrin_coat.yaml\
    \ --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/clathrin_coat-strict.tsv"
  snapshot_sha256: 54f75e59828d9462405692b481de883e4c7b0f0a3d055e083a5b7e99bba7d0ac
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/other/clathrin_coat.yaml --causal-graphs
  locator: Complete native read-only focused report
  accessed_at: '2026-10-22T04:51:57.141494Z'
  support: supports
  summary: "data/structures/other/clathrin_coat.yaml  (GO:0030118)\n  clathrin_coat_topology\t\
    clathrin_triskelion_scaffold\tCOVERED\t->clathrin_triskelion_scaffold (UniProtKB:P22137,\
    \ UniProtKB:P17891)\n  clathrin_coat_topology\tap_type_clathrin_adaptors\tCOVERED\t\
    ->ap_type_clathrin_adaptors (UniProtKB:P36000, UniProtKB:Q12028, UniProtKB:Q00776,\
    \ UniProtKB:P35181)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     2  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: a8e2bdca601043de0c79de562400bd9b1b2577bae3324a9a93fa39cd120fed03
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/other/clathrin_coat.yaml --verify
  locator: Complete native read-only focused report
  accessed_at: '2026-10-22T04:51:58.390479Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/clathrin_coat.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 16 of 16 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
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
- assessment_id: taxon
  area: scope
  topic: Species and experimental backgrounds
  outcome: supported
  target_ids:
  - GO:0030118
  summary: The species identity and yeast model are correct. COMMON retains the schema
    meaning present in most members/losses exception, supported qualitatively by normal
    yeast cell biology rather than a prevalence census. Newpher uses its specified
    SL/BWY laboratory strains and temperature/drug conditions, not a universal S288C
    experiment.
  evidence_ids:
  - record
  - schema
  - clathrin47-agent-tax4932
  - clathrin47-agent-newpher2005-meta
  - clathrin47-agent-newpher2005-duke
  - clathrin47-agent-kaksonen2005-meta
- assessment_id: canonical
  area: evidence
  topic: Clathrin recruitment and endocytic dynamics
  outcome: supported
  target_ids:
  - GO:0030118
  summary: The canonical note stays within Newpher cortical clathrin/adaptor recruitment
    and site dynamics. Kaksonen complete abstract supports modular coat, invagination,
    actin and scission behavior, including clathrin facilitating initiation without
    being essential for invagination or vesicle formation. No direct sealed-vesicle
    or precise scission observation is inferred from Newpher disappearance alone.
  evidence_ids:
  - record
  - clathrin47-agent-newpher2005-meta
  - clathrin47-agent-newpher2005-duke
  - clathrin47-agent-kaksonen2005-meta
- assessment_id: complex-grounding
  area: grounding
  topic: Exact complex classes versus deferred label-only rows
  outcome: concern
  target_ids:
  - GO:0030118
  summary: The triskelion complex has an exact source-neutral GO0071439 mapping. The
    AP-type clathrin-binding component also matches GO0030131, narrower than GO0030119;
    subtype-specific resolution is not required to map this stated class. Both current
    REVIEWED_LABEL_ONLY rationales therefore defer available exact complex identities.
  evidence_ids:
  - record
  - schema
  - curation
  - clathrin47-agent-go
  - clathrin47-agent-go-triskelion-candidates
- assessment_id: formation
  area: grounding
  topic: Assembly necessity remains unestablished
  outcome: unknown
  target_ids:
  - GO:0030118
  summary: Verified coat constituents, a six-chain triskelion and AP binding behavior
    do not by themselves demonstrate the requirement of every constituent for formation
    under every condition. The existing UNKNOWN essentiality values are retained;
    endocytic-function phenotypes are not silently substituted for coat-assembly necessity.
  evidence_ids:
  - record
  - schema
  - clathrin47-agent-go
  - clathrin47-agent-go-triskelion-candidates
- assessment_id: identity
  area: identity
  topic: Generic coat and subtype boundaries
  outcome: supported
  target_ids:
  - GO:0030118
  summary: The exact GO class, definition, synonym and membrane-coat parent agree.
    The three frozen records distinguish a generic protein coat, its pit-associated
    subtype and the underlying membrane invagination. The parent includes intracellular
    and endocytic coats; it need not restrict all representative AP proteins to cortical
    endocytosis.
  evidence_ids:
  - record
  - neighbor-pit-coat
  - neighbor-pit
  - clathrin47-agent-go
- assessment_id: proteins
  area: grounding
  topic: Correct chain and AP-1 examples
  outcome: supported
  target_ids:
  - GO:0030118
  summary: All six reviewed accessions, gene symbols and S288C strain identities agree
    with native entries. CHC1/CLC1 triskelions and the APL2/APL4/APM1/APS1 AP-1 quartet
    support the declared component classes. AP-1 examples do not imply all AP-family
    subtypes are clathrin-binding or that the Newpher cortical events were AP-1-specific.
  evidence_ids:
  - record
  - clathrin47-agent-go
  - clathrin47-agent-go-triskelion-candidates
  - clathrin47-agent-tax559292
  - clathrin47-agent-protein-P22137
  - clathrin47-agent-protein-P17891
  - clathrin47-agent-protein-P36000
  - clathrin47-agent-protein-Q12028
  - clathrin47-agent-protein-Q00776
  - clathrin47-agent-protein-P35181
- assessment_id: query-note
  area: evidence
  topic: APS1 alias multiplicity
  outcome: concern
  target_ids:
  - GO:0030118
  summary: Five current exact reviewed queries are single-hit. APS1 returns both the
    correct P35181 and unrelated DPS1/P04802 alias match. The role already says representative,
    but its evidence note still says single reviewed entry; correct only that present-tense
    uniqueness claim.
  evidence_ids:
  - record
  - clathrin47-agent-gene-APS1
  - clathrin47-agent-protein-P35181
- assessment_id: graph
  area: graph
  topic: Coarse coat assembly and function
  outcome: supported
  target_ids:
  - GO:0030118
  summary: NONMECHANISTIC faithfully bounds polymerization, adaptor linkage and part-of/type
    relationships. Native complex definitions and chain annotations support these
    coarse edges; Newpher/Kaksonen support endocytic context without resolving every
    recruitment or scission mechanism.
  evidence_ids:
  - record
  - schema
  - clathrin47-agent-go
  - clathrin47-agent-go-triskelion-candidates
  - clathrin47-agent-newpher2005-duke
  - clathrin47-agent-kaksonen2005-meta
  - clathrin47-agent-protein-P22137
  - clathrin47-agent-protein-P17891
- assessment_id: coverage
  area: completeness
  topic: Complete single-record review
  outcome: supported
  target_ids:
  - GO:0030118
  summary: All maintained fields, evidence placement, current discussions and history
    were read. Positive source-native mappings and bounded source limitations were
    distinguished from hypothetical missing molecular inventories.
  evidence_ids:
  - record
  - schema
  - curation
  - clathrin47-agent-go
findings:
- finding_id: F1
  issue_key: clathrin_coat-exact-complex-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Use the verified exact complex groundings
  description: 'The current reviewed-label-only rationale says no exact complex grounding
    was curated or defers subtype mappings, but native GO positively supplies the
    same declared complex classes: GO0071439 for the triskelion and GO0030131 for
    the clathrin-binding AP subset.'
  target_ids:
  - GO:0030118
  field_paths:
  - components[0].grounding
  - components[0].grounding_status
  - components[0].grounding_notes
  - components[1].grounding
  - components[1].grounding_status
  - components[1].grounding_notes
  evidence_ids:
  - record
  - curation
  - clathrin47-agent-go
  - clathrin47-agent-go-triskelion-candidates
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_coat.yaml
    role: maintained scientific record
  rule_id: Exact component grounding / REVIEWED_LABEL_ONLY
  native_severity: minor
  normalization_reason: The component identities and membership are correct; the bounded
    defect is an available exact ontology mapping left under a status meaning no exact
    grounding exists.
- finding_id: F2
  issue_key: clathrin-coat-aps1-query-uniqueness
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the current APS1 single-entry evidence note
  description: The exact reviewed APS1/taxon559292 query returns P35181 and the DPS1
    entry P04802 through its APS1 alias. The selected P35181 AP-1 sigma identity is
    correct and the role already says representative; only the evidence note retains
    an unsupported single-entry claim.
  target_ids:
  - GO:0030118
  field_paths:
  - components[1].protein_examples[3].evidence[0].notes
  evidence_ids:
  - record
  - clathrin47-agent-gene-APS1
  - clathrin47-agent-protein-P35181
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_coat.yaml
    role: maintained scientific record
  rule_id: Native protein query scope
  native_severity: minor
  normalization_reason: This is a bounded current provenance claim; protein identity,
    taxon and component membership remain valid.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0030118
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_coat.yaml
    role: maintained scientific record
  description: Ground the triskelion component to GO0071439 and the AP-type clathrin-binding
    component to GO0030131; update label-only status/rationale and the current TODO
    without changing valid component IDs, examples or UNKNOWN essentiality.
  acceptance_checks:
  - Confirm each exact definition matches the component class rather than a protein
    domain or whole coat.
  - Preserve the existing graph component_ref links and subtype boundaries.
  - Pass applicable schema, strict, identifier and graph checks.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0030118
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/clathrin_coat.yaml
    role: maintained scientific record
  description: Replace the current single-reviewed-entry assertion with an accurate
    representative/multiple-alias-query description while preserving P35181 and its
    established AP-1 identity.
  acceptance_checks:
  - Retain P35181, APS1, taxon559292 and REVIEWED status.
  - Distinguish the DPS1 alias match from an AP-1 constituent.
  - Preserve historical retrieval dates as historical provenance.
limitations:
- Five completed same-base batch26 global gates remain staged for guarded parent integration;
  this unsaved draft does not independently rerun or finalize those corpus checks.
- No source figure pixels, supplementary movies, raw experiments or underlying references
  were independently reanalyzed. Evidence locators distinguish primary body, abstract
  and native-authority tiers.
- Kaksonen2005 is inspected at exact complete-native-abstract tier; no genuine main
  body or movies are represented as read. Newpher TIRF disappearance cannot distinguish
  coat disassembly before budding from movement out of the evanescent field.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user goal authorizes one review for every uncovered record, including honest
  qualified passes.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
