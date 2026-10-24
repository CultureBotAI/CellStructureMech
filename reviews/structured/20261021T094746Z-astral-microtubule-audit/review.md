# Astral microtubule identity and meiotic-versus-mitotic evidence review

- Review: 20261021T094746Z-astral-microtubule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:08:26Z
- Finished UTC: 2026-10-21T09:47:46Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The astral microtubule identity, tubulin components and specialized meiotic example are supported. One major finding concerns added cross-taxon mechanism scope; two minor findings concern source attribution and the unsubstantiated mechanistic graph classification.

## Scope And Provenance

Entire single target; all native ontology, family, gene/accession and taxon identities; source-specific body/abstract/supplement claims, generic-versus-specialized hierarchy and function/graph scope.

Selection: Ninth selected target in batch fifteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000235 | data/structures/cytoskeleton/astral_microtubule.yaml | maintained | astral microtubule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0000235 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000235 | Focused validator passed. |
| Native UniProt verify | passed | False | GO:0000235 | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | GO:0000235 | Native command passed; scientific membership and graph scope assessed independently. |
| Claim-level scientific review | passed | True | GO:0000235 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Target resolver slice with native transport-failure cross-checks | passed | True | GO:0000235 | 16 of 16 exact target identifiers returned OK. No target residuals. The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| Full corpus QC | passed | True | GO:0000235 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000235 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000235 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000235 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0000235 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Array versus constituent filament

identity: supported. Targets: GO:0000235.

The exact GO identity and maintained hierarchy distinguish the astral microtubule from its containing aster array. Native GO supports the declared spindle context. HAA is an aster subclass and its meiotic study is a legitimate specialized example, not an exact synonym for all asters.

### Exact tubulin classes and concrete identities

grounding: supported. Targets: GO:0000235.

Alpha/beta tubulin are supported polymer constituents; IPR002452/002453 are exact family-level identities. P04689/tub1 with atb2/alp2 aliases, P04688/nda2 and P05219/nda3 are correct reviewed strain284812 proteins. Direct mCherry-Atb2 observation supports the alpha-tubulin example; the other entries explicitly provide identity rather than an isoform census.

### Meiotic source preparation is kept separate from reference stock

scope: supported. Targets: GO:0000235.

KT2901 is the homothallic fluorescent Figure4A strain; pat1 mat-Pc diploids provide separate synchronized ultrastructure. The canonical example correctly keeps these preparations distinct and does not identify them with the UniProt reference strain.

### Supported specialized meiotic function

evidence: supported. Targets: GO:0000235.

GO0030989/0032117 and the Tanaka2005 abstract support dynein-driven meiotic nuclear oscillation associated with the astral array. Funaya2012 supports Hrs1-dependent organization and the transition to meiosis I. This does not imply that every aster/astral microtubule performs horsetail movement or directly demonstrate chromosome-pairing/recombination effects.

### Broad capture machinery exceeds the cited taxon and cell-cycle evidence

scope: concern. Targets: GO:0000235.

The appended definition applies Kar9/Bim1/EB1/Bik1 capture machinery and cortical dynein to a broad yeast/fungal/protist mitotic scope while naming only the GO term as definition source. The native definition does not contain this mechanism, and the maintained primary studies concern S.pombe meiotic Hrs1/rMTOC organization. Taxon-specific support or narrower wording is needed; no claim that these proteins are absent from every other taxon is made.

### Constituent contributions versus whole-array language

graph: concern. Targets: GO:0000235.

Tubulin-to-filament, filament-to-array and the specialized horsetail contribution are supported. The phrase provides the radial array is read as contribution by its constituent microtubules, not equivalence of one filament to the complete array. No distinct atomic motor-interface mechanism or universal meiotic function is inferred from the MECHANISTIC label. The supported topology does not justify the MECHANISTIC scope label: no actor-to-event or organization-to-movement transition is represented. A nonmechanistic summary is an appropriate bounded alternative; atomistic detail is not required.

### Claimed narrow synonym is not supplied by its cited GO term

provenance: concern. Targets: GO:0000235.

The record assigns cytoplasmic astral microtubule as a NARROW_SYNONYM with GO0000235 as source. The current exact native term has no synonyms. This is a concrete source-attribution gap, not evidence that the phrase is biologically invalid.

### No required missing molecular inventory

completeness: supported. Targets: GO:0000235.

The core alpha/beta polymer components and exact families are represented. UNKNOWN essentiality avoids inferring isoform assembly necessity from imaging or generic polymer composition. Additional organizer/motor proteins, images, dimensions and broader taxa require separate evidence and are optional; these are not treated as absent-required-field findings.

## Findings

### F1: Bound the appended mitotic capture mechanism to supported taxa

major / open / confirmed; issue key: astral-microtubule-cross-taxon-capture-mechanism-unsourced.

The definition extends the native GO identity with Kar9/Bim1/EB1/Bik1 and cortical-dynein mitotic positioning across broad yeast/fungal/microbial-eukaryote groups. GO does not state this mechanism, and the record primary sources inspect S.pombe meiotic Hrs1-dependent arrays and their replacement by a spindle. Add appropriate inspected taxon-specific evidence and qualify the mechanism, or remove the unsupported extension. The supported meiotic example and native ontology hierarchy should remain.

### F2: Correct the source attribution for the added narrow synonym

minor / open / confirmed; issue key: astral-microtubule-synonym-not-in-cited-go.

The synonym cytoplasmic astral microtubule is attributed to GO0000235, but the native exact term currently has no synonym entries. Retain the phrase only with an appropriate source/curator rationale, or remove this unsupported GO attribution. This is not a claim that the descriptive phrase is biologically wrong.

### F3: Distinguish a structural/function summary from a represented mechanism

minor / open / confirmed; issue key: astral-microtubule-static-graph-mechanistic-scope.

The graph consists of constituent and compartment parthood plus a whole-structure function output. These supported relations do not themselves represent how array organization or a motor event causes movement, yet the graph is labeled MECHANISTIC. Use NONMECHANISTIC for the existing summary or add a directly evidenced causal transition. This does not invalidate the underlying topology or demand an atomic motor model.

## Recommended Actions And Acceptance Checks

### A1

During authorized curation, separate general structural identity from taxon- and phase-specific spindle-positioning mechanisms.

- Retain the native GO definition and correct hierarchy.
- Use inspected primary evidence for each retained named capture mechanism and state its organism/cell-cycle scope.
- Preserve the valid S.pombe meiotic HAA example and its distinct Hrs1/rMTOC source context.
- Do not infer universal Kar9/Bim1 machinery from a specialized HAA experiment.
- Run focused schema, strict-reference and causal-graph checks.

### A2

During authorized curation, repair or remove the unsupported GO synonym attribution.

- Check the exact native term rather than inferring a synonym from a related class.
- If retaining a curated narrow synonym, provide a source that actually supports it.
- Run focused schema and strict-reference validation.

### A3

Narrow the graph scope to a nonmechanistic structural/function summary, or encode a source-supported causal transition with organism and meiotic context.

- Preserve correct ontology nodes and supported membership relations.
- Check each retained causal edge against an inspected primary passage; a proposed future mechanism is not a completed graph.
- Any scientific edit requires separate curation authorization and the guarded writer, append-only history, rendering and native validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/astral_microtubule.yaml; Entire maintained YAML including all imported participants, component examples, functions, graph edges, discussions and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| astral-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000235,GO:0005818,GO:0005819,GO:0005874,GO:0005876,GO:0030989,GO:0032117; All returned term identities, definitions, synonyms and relevant is_a/part_of children; GO0005818,0000235,0032117,0030989 and declared hierarchy/polymer terms | supports | Native terms distinguish the whole aster, its astral-microtubule constituents, spindle relationships and the specific meiotic HAA example. The source definitions do not contain the appended Kar9/Bim1/Bik1 cross-taxon mitotic mechanism. |
| astral-agent-tax-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; Complete native taxon identity, rank and lineage | supports | Native taxon4896 identifies Schizosaccharomyces pombe at rank species. This single snapshot attests only this taxon; comparisons to the other species or strain use its separate evidence row. |
| astral-agent-tax-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Complete native taxon identity, rank and lineage | supports | Native taxon284812 identifies Schizosaccharomyces pombe 972h- at rank strain. This single snapshot attests only this taxon; comparisons to the other species or strain use its separate evidence row. |
| astral-agent-IPR002452 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/; Complete native accession, family type/name, family description and hierarchy | supports | Native InterPro identifies the exact Alpha tubulin family, distinct from generic Tubulin/FtsZ domains and from the other tubulin families. This grounds the component class rather than an isoform-specific meiotic localization claim. |
| astral-agent-IPR002453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/; Complete native accession, family type/name, family description and hierarchy | supports | Native InterPro identifies the exact Beta tubulin family, distinct from generic Tubulin/FtsZ domains and from the other tubulin families. This grounds the component class rather than an isoform-specific meiotic localization claim. |
| astral-agent-P04689 | https://rest.uniprot.org/uniprotkb/P04689.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P04689 identifies Tubulin alpha-2 chain, gene tub1, taxon284812. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| astral-agent-query-tub1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Atub1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene tub1, organism 284812, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P04689. This checks identifier resolution only. |
| astral-agent-P04688 | https://rest.uniprot.org/uniprotkb/P04688.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P04688 identifies Tubulin alpha-1 chain, gene nda2, taxon284812. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| astral-agent-query-nda2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Anda2%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene nda2, organism 284812, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P04688. This checks identifier resolution only. |
| astral-agent-P05219 | https://rest.uniprot.org/uniprotkb/P05219.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P05219 identifies Tubulin beta chain, gene nda3, taxon284812. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| astral-agent-query-nda3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Anda3%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene nda3, organism 284812, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P05219. This checks identifier resolution only. |
| astral-agent-doi-j.cub.2005.07.058 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2005.07.058; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Hrs1p/Mcp6p on the meiotic SPB organizes astral microtubule arrays for oscillatory nuclear movement. Authors: Tanaka K, Kohda T, Yamashita A, Nonaka N, Yamamoto M.; PMID 16111942; DOI 10.1016/j.cub.2005.07.058. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| astral-agent-doi-j.cub.2012.02.042 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2012.02.042; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Transient structure associated with the spindle pole body directs meiotic microtubule reorganization in S. pombe. Authors: Funaya C, Samarasinghe S, Pruggnaller S, Ohta M, Connolly Y, Müller J, Murakami H, Grallert A, Yamamoto M, Smith D, Antony C, Tanaka K.; PMID 22425159; DOI 10.1016/j.cub.2012.02.042. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| astral-agent-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml; Native PMC3382715.1 JATS: complete main Introduction, Results/Discussion, Conclusion and Experimental Procedures; Figure4 caption read in full, especially4A. Original batch7 receipt/hash preserved. | supports | Funaya2012 demonstrates the Hrs1-dependent meiotic radial microtubule array and a cytoplasmic radial MTOC distinct from the core SPB. Hrs1 downregulation and array disassembly accompany replacement by the meiosis-I spindle. Figure4A follows mCherry-Atb2 and Hrs1; this is a valid S.pombe meiotic example, not a cross-taxon Kar9/Bim1 mitotic study. |
| astral-agent-supplement | https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/mmc1.pdf; Actual mmc1.pdf: TableS1 Figure4A KT2901 and Figure3/EM strain rows; Supplemental Experimental Procedures, Yeast Strains and Media, Fluorescent Microscopy, Electron Microscopy/Tomography/Immunolabelling. Selected claim-bearing text read; not all22pages or movies. Original receipt/hash preserved. | supports | Supplemental TableS1 identifies KT2901 for Figure4A and separate pat1.114 mat-Pc diploid preparations for ultrastructure. The methods specify meiotic induction, fluorescence imaging and electron-tomography preparation. The reference UniProt stock is not thereby asserted to be the experimental strain. |
| schema-result | just validate data/structures/cytoskeleton/astral_microtubule.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/astral_microtubule.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/astral_microtubule.yaml --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/astral_microtubule-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/astral_microtubule.yaml --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/astral_microtubule-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch15-20261021-ohdkgt21/astral_microtubule-strict.tsv |
| native-verify | /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/astral_microtubule.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/astral_microtubule.yaml --causal-graphs; Captured focused native causal-graphs log | supports | data/structures/cytoskeleton/astral_microtubule.yaml  (GO:0000235)<br>  astral_microtubule_mechanism	alpha_tubulin	COVERED	-&gt;alpha_tubulin (UniProtKB:P04689, UniProtKB:P04688)<br>  astral_microtubule_mechanism	beta_tubulin	COVERED	-&gt;beta_tubulin (UniProtKB:P05219)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| graph-scope-policy | .claude/skills/curate-causal-graphs/SKILL.md; Review directed edges and preserve mechanism versus membership distinctions; primary-source scope | context_only | The graph rubric requires source-supported mechanism claims and distinguishes association or composition from causality. The present topology has no causal transition beyond membership and whole-structure output. |
| target-curies-result | just check-curies-strict; data/structures/cytoskeleton/astral_microtubule.yaml; exact native collect() target slice of original fresh-base TSV | supports | 16 of 16 exact target identifiers returned OK. No target residuals. The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The complete Funaya2012 main body and Figure4 caption were read, together with the listed supplemental strain/methods passages. No movies, raw tomography/fluorescence data or complete supplement-wide reanalysis was performed; historical record claims of visual inspection were not assumed to be new work by this reviewer.
- Tanaka2005 was inspected at native primary abstract/metadata level only. The prior record reports publisher403; no new full body or supplement access is asserted here.
- The primary studies establish S.pombe meiotic organization. A broad systematic survey of Kar9/Bim1/Bik1 homologs or mitotic mechanisms across fungi/protists was not undertaken; the finding is unsupported current attribution/scope, not universal absence.
- The native tubulin classes ground composition, but no complete alpha/beta isoform occupancy census or isoform-specific assembly necessity follows from mCherry-Atb2 imaging. UNKNOWN essentiality remains appropriate.
- No fixed microtubule count, dimensions, exact stoichiometry, quantitative oscillation parameter or quantitative recombination outcome is asserted. Source-native relationship and specialized experimental context are kept separate.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- All13 fresh batch15 inspection input hashes verified. Focused native and UniProt checks passed; no scientific edit or mapping-status promotion.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Root and source reviewer cross-checked graph classification against the other batch15 composition/function summaries; supported topology is distinguished from a represented causal transition.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094746Z-astral-microtubule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Astral microtubule identity and meiotic-versus-mitotic evidence review
started_at: '2026-10-21T09:08:26Z'
finished_at: '2026-10-21T09:47:46Z'
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
summary: The astral microtubule identity, tubulin components and specialized meiotic
  example are supported. One major finding concerns added cross-taxon mechanism scope;
  two minor findings concern source attribution and the unsubstantiated mechanistic
  graph classification.
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
  - path: data/structures/cytoskeleton/astral_microtubule.yaml
    sha256: 7c5c19cbf7cc39406dcc7d8bf376e4fcff12dcf7c71f702cf8058e766138be1f
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
- target_id: GO:0000235
  path: data/structures/cytoskeleton/astral_microtubule.yaml
  label: astral microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
scope:
  description: Entire single target; all native ontology, family, gene/accession and
    taxon identities; source-specific body/abstract/supplement claims, generic-versus-specialized
    hierarchy and function/graph scope.
  selection: Ninth selected target in batch fifteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000235
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000235
  command: just validate data/structures/cytoskeleton/astral_microtubule.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000235
  command: just validate-strict data/structures/cytoskeleton/astral_microtubule.yaml
    --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/astral_microtubule-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - GO:0000235
  command: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/astral_microtubule.yaml
    --verify
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native UniProt causal-graphs
  status: passed
  required: false
  target_ids:
  - GO:0000235
  command: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/astral_microtubule.yaml
    --causal-graphs
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000235
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - astral-agent-go
  - astral-agent-tax-4896
  - astral-agent-tax-284812
  - astral-agent-IPR002452
  - astral-agent-IPR002453
  - astral-agent-P04689
  - astral-agent-query-tub1
  - astral-agent-P04688
  - astral-agent-query-nda2
  - astral-agent-P05219
  - astral-agent-query-nda3
  - astral-agent-doi-j.cub.2005.07.058
  - astral-agent-doi-j.cub.2012.02.042
  - astral-agent-paper
  - astral-agent-supplement
- check_id: target-curies
  name: Target resolver slice with native transport-failure cross-checks
  status: passed
  required: true
  target_ids:
  - GO:0000235
  summary: 16 of 16 exact target identifiers returned OK. No target residuals. The
    shared command exit zero is not interpreted as successful network resolution for
    transport failures.
  evidence_ids:
  - target-curies-result
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000235
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
  - GO:0000235
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
  - GO:0000235
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
  - GO:0000235
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
  - GO:0000235
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
  reference: data/structures/cytoskeleton/astral_microtubule.yaml
  locator: Entire maintained YAML including all imported participants, component examples,
    functions, graph edges, discussions and history
  accessed_at: '2026-10-21T09:24:07Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T09:24:07Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: astral-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000235,GO:0005818,GO:0005819,GO:0005874,GO:0005876,GO:0030989,GO:0032117
  locator: All returned term identities, definitions, synonyms and relevant is_a/part_of
    children; GO0005818,0000235,0032117,0030989 and declared hierarchy/polymer terms
  accessed_at: '2026-10-21T09:15:01.352338Z'
  support: supports
  summary: Native terms distinguish the whole aster, its astral-microtubule constituents,
    spindle relationships and the specific meiotic HAA example. The source definitions
    do not contain the appended Kar9/Bim1/Bik1 cross-taxon mitotic mechanism.
  snapshot_sha256: 9a41356e287c3a6268afcba7e91591f19f6d7e1ff4c80623664293a74800771a
- evidence_id: astral-agent-tax-4896
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: Complete native taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:15:01.958807Z'
  support: supports
  summary: Native taxon4896 identifies Schizosaccharomyces pombe at rank species.
    This single snapshot attests only this taxon; comparisons to the other species
    or strain use its separate evidence row.
  snapshot_sha256: cdb53b3f4ab5e6bb4476de3bf0db333ae647e307a9fa8f98108827f98fe7f4d3
- evidence_id: astral-agent-tax-284812
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Complete native taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:15:01.930076Z'
  support: supports
  summary: Native taxon284812 identifies Schizosaccharomyces pombe 972h- at rank strain.
    This single snapshot attests only this taxon; comparisons to the other species
    or strain use its separate evidence row.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: astral-agent-IPR002452
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/
  locator: Complete native accession, family type/name, family description and hierarchy
  accessed_at: '2026-10-21T09:15:01.985561Z'
  support: supports
  summary: Native InterPro identifies the exact Alpha tubulin family, distinct from
    generic Tubulin/FtsZ domains and from the other tubulin families. This grounds
    the component class rather than an isoform-specific meiotic localization claim.
  snapshot_sha256: ff28f4d004d8f82a804f7263ff1df3ab78d7bdbdeee755fa924a58e872602b5a
- evidence_id: astral-agent-IPR002453
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/
  locator: Complete native accession, family type/name, family description and hierarchy
  accessed_at: '2026-10-21T09:15:02.535633Z'
  support: supports
  summary: Native InterPro identifies the exact Beta tubulin family, distinct from
    generic Tubulin/FtsZ domains and from the other tubulin families. This grounds
    the component class rather than an isoform-specific meiotic localization claim.
  snapshot_sha256: edbfe5509d6e568069c7105eacc2b7e296e84e0790a16a63d836c45a094d20ef
- evidence_id: astral-agent-P04689
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P04689.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:15:02.644856Z'
  support: supports
  summary: Native reviewed UniProtKB P04689 identifies Tubulin alpha-2 chain, gene
    tub1, taxon284812. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 3bfa569ef452b581ecc2013f8b85880667fd4de3e6d11df1bdcbbc3319ade3e3
- evidence_id: astral-agent-query-tub1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Atub1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene tub1, organism 284812, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:15:03.198766Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P04689. This checks identifier
    resolution only.
  snapshot_sha256: 002ff4e9a7f59e2d3d6e32bf57e151690c33deb1d844b6dce12d600e6327fd5e
  search_scope: UniProtKB query gene_exact:tub1 AND organism_id:284812 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: astral-agent-P04688
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P04688.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:15:02.598938Z'
  support: supports
  summary: Native reviewed UniProtKB P04688 identifies Tubulin alpha-1 chain, gene
    nda2, taxon284812. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: f6104d4ad0cb6eae74ad3cdbfc6a3c779f42c9522e262843d52d6ca7ef46f4fd
- evidence_id: astral-agent-query-nda2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Anda2%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene nda2, organism 284812, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:15:03.244224Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P04688. This checks identifier
    resolution only.
  snapshot_sha256: d1fc305203c3dddb4514d3973ea77f424df3ae4d0b108dffb6c31d1d9ed60ca3
  search_scope: UniProtKB query gene_exact:nda2 AND organism_id:284812 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: astral-agent-P05219
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P05219.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:15:03.192143Z'
  support: supports
  summary: Native reviewed UniProtKB P05219 identifies Tubulin beta chain, gene nda3,
    taxon284812. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 748f30a9ed411acc3358c1828f32354becece0ef6d16b60ef4319c8d6bbe66b2
- evidence_id: astral-agent-query-nda3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Anda3%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene nda3, organism 284812, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:15:03.696568Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P05219. This checks identifier
    resolution only.
  snapshot_sha256: bb80a570bfc520130e8d196c38f607995175eaec231abebdea20b19676434523
  search_scope: UniProtKB query gene_exact:nda3 AND organism_id:284812 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: astral-agent-doi-j.cub.2005.07.058
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2005.07.058
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:15:03.805057Z'
  support: supports
  summary: 'Native metadata identifies Hrs1p/Mcp6p on the meiotic SPB organizes astral
    microtubule arrays for oscillatory nuclear movement. Authors: Tanaka K, Kohda
    T, Yamashita A, Nonaka N, Yamamoto M.; PMID 16111942; DOI 10.1016/j.cub.2005.07.058.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: b774d7d9ae22e94d9758b59c0f24de4bda443578035c5a69ac6db64622120e93
- evidence_id: astral-agent-doi-j.cub.2012.02.042
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2012.02.042
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:15:03.811425Z'
  support: supports
  summary: 'Native metadata identifies Transient structure associated with the spindle
    pole body directs meiotic microtubule reorganization in S. pombe. Authors: Funaya
    C, Samarasinghe S, Pruggnaller S, Ohta M, Connolly Y, Müller J, Murakami H, Grallert
    A, Yamamoto M, Smith D, Antony C, Tanaka K.; PMID 22425159; DOI 10.1016/j.cub.2012.02.042.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 74ff9c0672edac602df99d3e760b7346e0642f4100839c6381f1696d4599f944
- evidence_id: astral-agent-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml
  locator: 'Native PMC3382715.1 JATS: complete main Introduction, Results/Discussion,
    Conclusion and Experimental Procedures; Figure4 caption read in full, especially4A.
    Original batch7 receipt/hash preserved.'
  accessed_at: '2026-10-21T07:08:03.849693Z'
  support: supports
  summary: Funaya2012 demonstrates the Hrs1-dependent meiotic radial microtubule array
    and a cytoplasmic radial MTOC distinct from the core SPB. Hrs1 downregulation
    and array disassembly accompany replacement by the meiosis-I spindle. Figure4A
    follows mCherry-Atb2 and Hrs1; this is a valid S.pombe meiotic example, not a
    cross-taxon Kar9/Bim1 mitotic study.
  snapshot_sha256: 59f662c998abf622fbb9bccbabc3867cb5ffd3174943cc52cb6228b1e35cd93d
- evidence_id: astral-agent-supplement
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/mmc1.pdf
  locator: 'Actual mmc1.pdf: TableS1 Figure4A KT2901 and Figure3/EM strain rows; Supplemental
    Experimental Procedures, Yeast Strains and Media, Fluorescent Microscopy, Electron
    Microscopy/Tomography/Immunolabelling. Selected claim-bearing text read; not all22pages
    or movies. Original receipt/hash preserved.'
  accessed_at: '2026-10-21T07:08:38.276610Z'
  support: supports
  summary: Supplemental TableS1 identifies KT2901 for Figure4A and separate pat1.114
    mat-Pc diploid preparations for ultrastructure. The methods specify meiotic induction,
    fluorescence imaging and electron-tomography preparation. The reference UniProt
    stock is not thereby asserted to be the experimental strain.
  snapshot_sha256: 6dde9cc7999b0e3294aa95f3d3036a319c90b9390920d84bd7194c883dc213f9
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/astral_microtubule.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:08:35Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/astral_microtubule.yaml'
  snapshot_sha256: 0fc59643ca54be053158b3268bce435afe170e99cf1ad49482275b78f258667c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/astral_microtubule.yaml
    --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/astral_microtubule-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:08:40Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/astral_microtubule.yaml\
    \ --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/astral_microtubule-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch15-20261021-ohdkgt21/astral_microtubule-strict.tsv"
  snapshot_sha256: e5407447130efd1867c2d18a6ce9526022aca1673baa1b34aa0b863df3b971f3
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/astral_microtubule.yaml
    --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T09:15:00.441467Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/astral_microtubule.yaml
    --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T09:15:01.010429Z'
  support: supports
  summary: "data/structures/cytoskeleton/astral_microtubule.yaml  (GO:0000235)\n \
    \ astral_microtubule_mechanism\talpha_tubulin\tCOVERED\t->alpha_tubulin (UniProtKB:P04689,\
    \ UniProtKB:P04688)\n  astral_microtubule_mechanism\tbeta_tubulin\tCOVERED\t->beta_tubulin\
    \ (UniProtKB:P05219)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     2  COVERED\
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
  snapshot_sha256: 3af3eda494e52b5c40947022f17f4d21039caecc662afbe457cdf6f14057ca92
- evidence_id: graph-scope-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Review directed edges and preserve mechanism versus membership distinctions;
    primary-source scope
  accessed_at: '2026-10-21T09:29:05.026359Z'
  support: context_only
  summary: The graph rubric requires source-supported mechanism claims and distinguishes
    association or composition from causality. The present topology has no causal
    transition beyond membership and whole-structure output.
- evidence_id: target-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/astral_microtubule.yaml; exact native collect()
    target slice of original fresh-base TSV
  accessed_at: '2026-10-21T09:47:06.901851Z'
  support: supports
  summary: 16 of 16 exact target identifiers returned OK. No target residuals. The
    shared command exit zero is not interpreted as successful network resolution for
    transport failures.
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
  topic: Array versus constituent filament
  outcome: supported
  target_ids:
  - GO:0000235
  summary: The exact GO identity and maintained hierarchy distinguish the astral microtubule
    from its containing aster array. Native GO supports the declared spindle context.
    HAA is an aster subclass and its meiotic study is a legitimate specialized example,
    not an exact synonym for all asters.
  evidence_ids:
  - astral-agent-go
  - astral-agent-paper
  - record
- assessment_id: composition
  area: grounding
  topic: Exact tubulin classes and concrete identities
  outcome: supported
  target_ids:
  - GO:0000235
  summary: Alpha/beta tubulin are supported polymer constituents; IPR002452/002453
    are exact family-level identities. P04689/tub1 with atb2/alp2 aliases, P04688/nda2
    and P05219/nda3 are correct reviewed strain284812 proteins. Direct mCherry-Atb2
    observation supports the alpha-tubulin example; the other entries explicitly provide
    identity rather than an isoform census.
  evidence_ids:
  - astral-agent-go
  - astral-agent-IPR002452
  - astral-agent-IPR002453
  - astral-agent-P04689
  - astral-agent-P04688
  - astral-agent-P05219
  - astral-agent-paper
  - record
- assessment_id: strain
  area: scope
  topic: Meiotic source preparation is kept separate from reference stock
  outcome: supported
  target_ids:
  - GO:0000235
  summary: KT2901 is the homothallic fluorescent Figure4A strain; pat1 mat-Pc diploids
    provide separate synchronized ultrastructure. The canonical example correctly
    keeps these preparations distinct and does not identify them with the UniProt
    reference strain.
  evidence_ids:
  - astral-agent-tax-4896
  - astral-agent-tax-284812
  - astral-agent-paper
  - astral-agent-supplement
  - record
- assessment_id: horsetail
  area: evidence
  topic: Supported specialized meiotic function
  outcome: supported
  target_ids:
  - GO:0000235
  summary: GO0030989/0032117 and the Tanaka2005 abstract support dynein-driven meiotic
    nuclear oscillation associated with the astral array. Funaya2012 supports Hrs1-dependent
    organization and the transition to meiosis I. This does not imply that every aster/astral
    microtubule performs horsetail movement or directly demonstrate chromosome-pairing/recombination
    effects.
  evidence_ids:
  - astral-agent-go
  - astral-agent-doi-j.cub.2005.07.058
  - astral-agent-paper
  - record
- assessment_id: definition-mechanism
  area: scope
  topic: Broad capture machinery exceeds the cited taxon and cell-cycle evidence
  outcome: concern
  target_ids:
  - GO:0000235
  summary: The appended definition applies Kar9/Bim1/EB1/Bik1 capture machinery and
    cortical dynein to a broad yeast/fungal/protist mitotic scope while naming only
    the GO term as definition source. The native definition does not contain this
    mechanism, and the maintained primary studies concern S.pombe meiotic Hrs1/rMTOC
    organization. Taxon-specific support or narrower wording is needed; no claim that
    these proteins are absent from every other taxon is made.
  evidence_ids:
  - astral-agent-go
  - astral-agent-doi-j.cub.2005.07.058
  - astral-agent-paper
  - record
- assessment_id: graph-context
  area: graph
  topic: Constituent contributions versus whole-array language
  outcome: concern
  target_ids:
  - GO:0000235
  summary: 'Tubulin-to-filament, filament-to-array and the specialized horsetail contribution
    are supported. The phrase provides the radial array is read as contribution by
    its constituent microtubules, not equivalence of one filament to the complete
    array. No distinct atomic motor-interface mechanism or universal meiotic function
    is inferred from the MECHANISTIC label. The supported topology does not justify
    the MECHANISTIC scope label: no actor-to-event or organization-to-movement transition
    is represented. A nonmechanistic summary is an appropriate bounded alternative;
    atomistic detail is not required.'
  evidence_ids:
  - astral-agent-go
  - astral-agent-paper
  - astral-agent-doi-j.cub.2005.07.058
  - record
  - graph-scope-policy
- assessment_id: synonym
  area: provenance
  topic: Claimed narrow synonym is not supplied by its cited GO term
  outcome: concern
  target_ids:
  - GO:0000235
  summary: The record assigns cytoplasmic astral microtubule as a NARROW_SYNONYM with
    GO0000235 as source. The current exact native term has no synonyms. This is a
    concrete source-attribution gap, not evidence that the phrase is biologically
    invalid.
  evidence_ids:
  - astral-agent-go
  - record
- assessment_id: completeness
  area: completeness
  topic: No required missing molecular inventory
  outcome: supported
  target_ids:
  - GO:0000235
  summary: The core alpha/beta polymer components and exact families are represented.
    UNKNOWN essentiality avoids inferring isoform assembly necessity from imaging
    or generic polymer composition. Additional organizer/motor proteins, images, dimensions
    and broader taxa require separate evidence and are optional; these are not treated
    as absent-required-field findings.
  evidence_ids:
  - astral-agent-go
  - astral-agent-IPR002452
  - astral-agent-IPR002453
  - astral-agent-paper
  - astral-agent-supplement
  - record
  - policy
findings:
- finding_id: F1
  issue_key: astral-microtubule-cross-taxon-capture-mechanism-unsourced
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Bound the appended mitotic capture mechanism to supported taxa
  description: The definition extends the native GO identity with Kar9/Bim1/EB1/Bik1
    and cortical-dynein mitotic positioning across broad yeast/fungal/microbial-eukaryote
    groups. GO does not state this mechanism, and the record primary sources inspect
    S.pombe meiotic Hrs1-dependent arrays and their replacement by a spindle. Add
    appropriate inspected taxon-specific evidence and qualify the mechanism, or remove
    the unsupported extension. The supported meiotic example and native ontology hierarchy
    should remain.
  target_ids:
  - GO:0000235
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - astral-agent-go
  - astral-agent-doi-j.cub.2005.07.058
  - astral-agent-paper
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: This is a consequential unqualified molecular mechanism and
    taxonomic scope claim in the definition, not a demand for a broader literature
    inventory. The finding concerns support and scope rather than asserting that the
    mechanism is false in every listed organism.
- finding_id: F2
  issue_key: astral-microtubule-synonym-not-in-cited-go
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the source attribution for the added narrow synonym
  description: The synonym cytoplasmic astral microtubule is attributed to GO0000235,
    but the native exact term currently has no synonym entries. Retain the phrase
    only with an appropriate source/curator rationale, or remove this unsupported
    GO attribution. This is not a claim that the descriptive phrase is biologically
    wrong.
  target_ids:
  - GO:0000235
  field_paths:
  - synonyms[synonym_text=cytoplasmic astral microtubule]
  evidence_ids:
  - astral-agent-go
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The structure identity is correct and the phrase may be reasonable;
    only the asserted authority/source provenance is unverified and inconsistent with
    the checked current term.
- finding_id: F3
  issue_key: astral-microtubule-static-graph-mechanistic-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish a structural/function summary from a represented mechanism
  description: The graph consists of constituent and compartment parthood plus a whole-structure
    function output. These supported relations do not themselves represent how array
    organization or a motor event causes movement, yet the graph is labeled MECHANISTIC.
    Use NONMECHANISTIC for the existing summary or add a directly evidenced causal
    transition. This does not invalidate the underlying topology or demand an atomic
    motor model.
  target_ids:
  - GO:0000235
  field_paths:
  - causal_graphs[graph_id=astral_microtubule_mechanism].scope_status
  evidence_ids:
  - record
  - astral-agent-paper
  - graph-scope-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-causal-graphs/SKILL.md:Evidence and graph scope
  native_severity: minor
  normalization_reason: The underlying structure, membership and scoped function remain
    supported. This is a bounded classification defect consistent with the analogous
    composition/function-summary graphs in this batch.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0000235
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  description: During authorized curation, separate general structural identity from
    taxon- and phase-specific spindle-positioning mechanisms.
  acceptance_checks:
  - Retain the native GO definition and correct hierarchy.
  - Use inspected primary evidence for each retained named capture mechanism and state
    its organism/cell-cycle scope.
  - Preserve the valid S.pombe meiotic HAA example and its distinct Hrs1/rMTOC source
    context.
  - Do not infer universal Kar9/Bim1 machinery from a specialized HAA experiment.
  - Run focused schema, strict-reference and causal-graph checks.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0000235
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  description: During authorized curation, repair or remove the unsupported GO synonym
    attribution.
  acceptance_checks:
  - Check the exact native term rather than inferring a synonym from a related class.
  - If retaining a curated narrow synonym, provide a source that actually supports
    it.
  - Run focused schema and strict-reference validation.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0000235
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  description: Narrow the graph scope to a nonmechanistic structural/function summary,
    or encode a source-supported causal transition with organism and meiotic context.
  acceptance_checks:
  - Preserve correct ontology nodes and supported membership relations.
  - Check each retained causal edge against an inspected primary passage; a proposed
    future mechanism is not a completed graph.
  - Any scientific edit requires separate curation authorization and the guarded writer,
    append-only history, rendering and native validation.
limitations:
- The complete Funaya2012 main body and Figure4 caption were read, together with the
  listed supplemental strain/methods passages. No movies, raw tomography/fluorescence
  data or complete supplement-wide reanalysis was performed; historical record claims
  of visual inspection were not assumed to be new work by this reviewer.
- Tanaka2005 was inspected at native primary abstract/metadata level only. The prior
  record reports publisher403; no new full body or supplement access is asserted here.
- The primary studies establish S.pombe meiotic organization. A broad systematic survey
  of Kar9/Bim1/Bik1 homologs or mitotic mechanisms across fungi/protists was not undertaken;
  the finding is unsupported current attribution/scope, not universal absence.
- The native tubulin classes ground composition, but no complete alpha/beta isoform
  occupancy census or isoform-specific assembly necessity follows from mCherry-Atb2
  imaging. UNKNOWN essentiality remains appropriate.
- No fixed microtubule count, dimensions, exact stoichiometry, quantitative oscillation
  parameter or quantitative recombination outcome is asserted. Source-native relationship
  and specialized experimental context are kept separate.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- All13 fresh batch15 inspection input hashes verified. Focused native and UniProt
  checks passed; no scientific edit or mapping-status promotion.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Root and source reviewer cross-checked graph classification against the other batch15
  composition/function summaries; supported topology is distinguished from a represented
  causal transition.
```
