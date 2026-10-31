# Scientific review of dna polymerase iii core complex

- Review: 20261022T055921Z-dna-polymerase-iii-core-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:37:15Z
- Finished UTC: 2026-10-22T05:59:21Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The alpha-epsilon-theta core identity, correct K12 examples and separated polymerase/proofreading activities are supported. One minor resolves the exact theta family; other mapping and formation boundaries remain explicit.

## Scope And Provenance

Exactly one complete maintained record, bounded native source fields and literature passages identified in each locator. No scientific input was changed.

Selection: Batch51 strict unreviewed path order, index 3; exactly one entire maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0044776 | data/structures/other/dna_polymerase_iii_core_complex.yaml | maintained | DNA polymerase III, core complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0044776 | Focused validator passed. |
| Focused native strict | passed | True | GO:0044776 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0044776 | Focused read-only check passed; scientific claims separately assessed. |
| Native focused verify | passed | True | GO:0044776 | Focused read-only check passed; scientific claims separately assessed. |
| Expression-module applicability | not_applicable | False | GO:0044776 | No target expression-module or transcriptomic claim requires this resource. |
| Claim-level scientific review | passed | True | GO:0044776 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0044776 | 9 of 10 collected target identifiers returned OK. PMID:3283127: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0044776 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0044776 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0044776 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0044776 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0044776 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Alpha-epsilon-theta catalytic subassembly

identity: supported. Targets: GO:0044776.

Native GO and the complete Maki/Kornberg abstract identify this core, polymerase/proofreading activities and holoenzyme parthood. DNA-polymerase-complex parentage is biologically supported by the core polymerase activity; it is not claimed as a direct native GO is-a edge.

### Correct examples and exact versus broad families

grounding: concern. Targets: GO:0044776.

P10443/dnaE, P03007/dnaQ and P0ABS8/holE are verified reviewed K12 examples with membership independently supported at primary-abstract tier. Exact theta family IPR009052 is available. DnaQ IPR006309 is proteobacterial, IPR006054 a domain, and IPR004805 includes DnaE2/PolC, so their scope must not be silently generalized.

### Species-level canonical reconstitution

scope: supported. Targets: GO:0044776.

Maki/Kornberg directly reports E.coli purified-subunit reconstitution in its abstract, supporting the species-level canonical note. K12 examples are independently verified identities; no exact Maki experimental strain, growth conditions or full methods are asserted.

### Membership and two catalytic activities

graph: supported. Targets: GO:0044776.

All three membership edges and both core activity edges agree with native GO and the Maki abstract. The polymerase molecular function remains separate from proofreading. Theta is not individually asserted to catalyze either activity, and the graph does not claim a tested assembly sequence.

### Named constituents and uncertain physical necessity

grounding: unknown. Targets: GO:0044776.

The defined core contains alpha, epsilon and theta; the cited abstract reports partial assemblies and functional reconstitution, not a complete loss-of-physical-assembly series. UNKNOWN formation essentiality remains explicit; theta annotation uncertainty is not evidence that theta is absent.

### Complete maintained target

completeness: supported. Targets: GO:0044776.

All fields, history, discussions and edge evidence were reviewed. Optional images, dimensions or prevalence inventories are not filled without evidence. Cited authority identities and source-scoped claims were checked separately.

## Findings

### F1: Ground the theta subunit with its exact family

minor / open / confirmed; issue key: pol-iii-core-theta-exact-family.

HolE remains REVIEWED_LABEL_ONLY and the current TODO defers all three core classes, although native IPR009052 is an exact full-protein theta family and P0ABS8 independently carries that family xref. Other inspected candidates are broader or taxon-limited.

## Recommended Actions And Acceptance Checks

### A1

Use IPR009052 for the theta class and narrow the current TODO. Preserve correct DnaE/DnaQ examples and unresolved exact taxon-neutral class boundaries.

- Verify family type/name/PF06440 and separate example membership.
- Do not substitute the DnaQ domain or broad DnaE2/DnaE/PolC family.
- Preserve source scope and correct current protein examples; pass applicable native validators.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dna_polymerase_iii_core_complex.yaml; Entire maintained record, all evidence and graph edges, discussions and history | context_only | All target bytes were read. The current source-backed composition is distinguished from historical review notes and untested formation requirements. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, EssentialityEnum, NONMECHANISTIC graph contract | context_only | Taxon-specific accessions identify examples; they do not replace family grounding or experimental membership. Formation necessity differs from catalytic function and viability. |
| curation | docs/CURATION.md; Exact grounding, REVIEWED_LABEL_ONLY at159–160 and assembly essentiality | context_only | Label-only review status denotes a genuinely unresolved exact mapping. A domain or broader family must not replace an exact named protein class. |
| graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Membership versus assembly and coarse functional-edge scope | context_only | NONMECHANISTIC membership and catalogued activity are assessed without claiming that a static structure establishes a complete dynamic mechanism. |
| root51-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846,GO:0009360,GO:0044776,GO:0044775,GO:0043847,GO:0032991,GO:0042575,GO:0003887,GO:0006260,GO:0003689; All ten term identities/definitions/synonyms/comments; relevant typed child links. Unrelated GO0032991 descendants not audited. | supports | Exact active PolIII holoenzyme/core/clamp-loader identities, native synonyms and typed holoenzyme parthood links are present. The clamp-loader and core definitions match the named structures. The beta-clamp cross-class sentence is not used as a stoichiometric claim here. |
| root51-sources-pmid-3283127 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A3283127+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact identifier/title/author/year/DOI and complete abstract | supports | Native MED3283127: DNA polymerase III holoenzyme of Escherichia coli. III. Distinctive processive polymerases reconstituted from purified subunits. by Maki S, Kornberg A. (1988), DOI 10.1016/s0021-9258(18)68678-8. Complete native abstract read; source-specific body access is stated separately. |
| root51-sources-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxonomy response | supports | ENA identifies taxon562 as Escherichia coli. Species and reference-strain levels are kept separate. |
| root51-sources-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxonomy response | supports | ENA identifies taxon83333 as Escherichia coli K-12. Species and reference-strain levels are kept separate. |
| root51-sources-protein-P10443 | https://rest.uniprot.org/uniprotkb/P10443.json; Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY; relevant InterPro/GO xrefs | supports | P10443 is the reviewed K12 dnaE entry with the declared protein identity. Native gene/locus tokens, function/subunit annotations, relevant GO annotation and family cross-references were inspected. Annotation-referenced experiments are not independently certified unless a separate primary-source row says so. |
| root51-sources-gene-dnaE | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set for gene_exact:dnaE AND taxonomy_id:83333 AND reviewed:true; size500 | supports | The complete reviewed exact-gene query returns one result, P10443, with the expected primary gene and taxon83333. |
| root51-sources-protein-P03007 | https://rest.uniprot.org/uniprotkb/P03007.json; Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY; relevant InterPro/GO xrefs | supports | P03007 is the reviewed K12 dnaQ entry with the declared protein identity. Native gene/locus tokens, function/subunit annotations, relevant GO annotation and family cross-references were inspected. Annotation-referenced experiments are not independently certified unless a separate primary-source row says so. |
| root51-sources-gene-dnaQ | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaQ%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set for gene_exact:dnaQ AND taxonomy_id:83333 AND reviewed:true; size500 | supports | The complete reviewed exact-gene query returns one result, P03007, with the expected primary gene and taxon83333. |
| root51-sources-protein-P0ABS8 | https://rest.uniprot.org/uniprotkb/P0ABS8.json; Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY; relevant InterPro/GO xrefs | supports | P0ABS8 is the reviewed K12 holE entry with the declared protein identity. Native gene/locus tokens, function/subunit annotations, relevant GO annotation and family cross-references were inspected. Annotation-referenced experiments are not independently certified unless a separate primary-source row says so. |
| root51-sources-gene-holE | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set for gene_exact:holE AND taxonomy_id:83333 AND reviewed:true; size500 | supports | The complete reviewed exact-gene query returns one result, P0ABS8, with the expected primary gene and taxon83333. |
| root51-sources-maki1988-api | https://api.elsevier.com/content/article/pii/S0021925818686788?httpAccept=text/xml; Entire publisher coredata XML; no article body | supports | The native publisher XML confirms the exact DOI, title, journal and1988 publication date; this response contains core metadata only, despite its full-text-retrieval response name. |
| root51-maki1988-publisher | https://www.jbc.org/article/S0021-9258(18)68678-8/fulltext; Retained publisher403 response | context_only | The publisher route did not yield the primary body; this paper is assessed at complete native abstract tier. |
| root51-maki1988-pdf | https://www.jbc.org/article/S0021-9258(18)68678-8/pdf; Retained publisher403 response | context_only | The publisher route did not yield the primary body; this paper is assessed at complete native abstract tier. |
| root51-sources-GO0044776-is-a | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776/ancestors?relations=is_a; Complete is-a-only ancestor response | supports | The native is-a ancestry includes protein-containing complex but currently routes through nuclear protein-containing complex. This upstream topology is recorded as a conflict with the bacterial primary evidence, not propagated as a required biological classification. |
| root51-sources-GO0044776-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776/constraints; Complete focal taxonConstraints array; unrelated inherited protein blacklists not used | context_only | Native GO currently reports only_in_taxon Eukaryota for this bacterial complex. The record has no such assertion; primary E.coli evidence and the source definition conflict with that upstream restriction. |
| root51-sources-GO0044776-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776/history; Complete history array | context_only | Complete native history records the2020 nuclear-parent change and a2024 bad-taxon-ID constraint entry. This provides provenance of an upstream discrepancy, not bacterial taxonomic evidence. |
| root51-sources-ipr-IPR009052 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009052/; Native name/type, complete description and flags, hierarchy and member signatures | supports | Exact bacterial theta whole-protein family with PF06440. |
| root51-sources-ipr-IPR006309 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006309/; Native name/type, complete description and flags, hierarchy and member signatures | supports | Whole epsilon family is explicitly proteobacterial; useful for the E.coli instance, not automatically equivalent to a taxon-agnostic epsilon class. |
| root51-sources-ipr-IPR006054 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006054/; Native name/type, complete description and flags, hierarchy and member signatures | supports | DnaQ exonuclease domain also includes paralogs and DinG regions; it is not an exact whole-protein epsilon family. |
| root51-sources-ipr-IPR004805 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004805/; Native name/type, complete description and flags, hierarchy and member signatures | supports | Broader family includes DnaE2 error-prone polymerase, DnaE and PolC; it is not an exact stand-in for the core DnaE class. |
| schema-result | just validate data/structures/other/dna_polymerase_iii_core_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dna_polymerase_iii_core_complex.yaml |
| strict-result | just validate-strict data/structures/other/dna_polymerase_iii_core_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_core_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dna_polymerase_iii_core_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_core_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_core_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dna_polymerase_iii_core_complex.yaml; Complete focused native report | supports | data/structures/other/dna_polymerase_iii_core_complex.yaml  (GO:0044776)<br>  pol_iii_core_catalysis	alpha_subunit	COVERED	-&gt;alpha_subunit (UniProtKB:P10443)<br>  pol_iii_core_catalysis	epsilon_subunit	COVERED	-&gt;epsilon_subunit (UniProtKB:P03007)<br>  pol_iii_core_catalysis	theta_subunit	COVERED	-&gt;theta_subunit (UniProtKB:P0ABS8)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/dna_polymerase_iii_core_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dna_polymerase_iii_core_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 10 collected target identifiers returned OK. PMID:3283127: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, coordinates, sequence alignments or raw kinetic data were reanalyzed. Native annotations and a secondary review remain distinct from independently inspected primary methods.
- Maki/Kornberg1988 is verified at complete abstract tier only; publisher HTML and PDF requests returned403 and API returned metadata only. Exact assay methods, expression strains and figures are not certified. Its abstract directly supports the species-level reconstitution and stated core activities.
- Native GO currently assigns this term nuclear-complex ancestry and an Eukaryota-only restriction, conflicting with the cited E.coli evidence. Neither assertion is present in the target. Keep its exact named identity and supported bacterial example; do not import the erroneous source restriction or infer occurrence in every bacterium.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes qualified clean reviews as well as issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T055921Z-dna-polymerase-iii-core-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Scientific review of dna polymerase iii core complex
started_at: '2026-10-22T05:37:15Z'
finished_at: '2026-10-22T05:59:21Z'
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
summary: The alpha-epsilon-theta core identity, correct K12 examples and separated
  polymerase/proofreading activities are supported. One minor resolves the exact theta
  family; other mapping and formation boundaries remain explicit.
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
  - path: data/structures/other/dna_polymerase_iii_core_complex.yaml
    sha256: d3f7d2562674074de9eac445b01e2e20a566e590840dba0edac515a22b02d47b
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
- target_id: GO:0044776
  path: data/structures/other/dna_polymerase_iii_core_complex.yaml
  label: DNA polymerase III, core complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_core_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained record, bounded native source fields
    and literature passages identified in each locator. No scientific input was changed.
  selection: Batch51 strict unreviewed path order, index 3; exactly one entire maintained
    record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0044776
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: just validate data/structures/other/dna_polymerase_iii_core_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: just validate-strict data/structures/other/dna_polymerase_iii_core_complex.yaml
    --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_core_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dna_polymerase_iii_core_complex.yaml
  exit_code: 0
  summary: Focused read-only check passed; scientific claims separately assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dna_polymerase_iii_core_complex.yaml
  exit_code: 0
  summary: Focused read-only check passed; scientific claims separately assessed.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0044776
  summary: No target expression-module or transcriptomic claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0044776
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graph-rubric
  - root51-sources-go
  - root51-sources-pmid-3283127
  - root51-sources-tax562
  - root51-sources-tax83333
  - root51-sources-protein-P10443
  - root51-sources-gene-dnaE
  - root51-sources-protein-P03007
  - root51-sources-gene-dnaQ
  - root51-sources-protein-P0ABS8
  - root51-sources-gene-holE
  - root51-sources-maki1988-api
  - root51-maki1988-publisher
  - root51-maki1988-pdf
  - root51-sources-GO0044776-is-a
  - root51-sources-GO0044776-constraints
  - root51-sources-GO0044776-history
  - root51-sources-ipr-IPR009052
  - root51-sources-ipr-IPR006309
  - root51-sources-ipr-IPR006054
  - root51-sources-ipr-IPR004805
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0044776
  summary: '9 of 10 collected target identifiers returned OK. PMID:3283127: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root51-sources-pmid-3283127
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0044776
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
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_core_complex.yaml
  locator: Entire maintained record, all evidence and graph edges, discussions and
    history
  accessed_at: '2026-10-22T05:42:54Z'
  support: context_only
  summary: All target bytes were read. The current source-backed composition is distinguished
    from historical review notes and untested formation requirements.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, EssentialityEnum, NONMECHANISTIC graph
    contract
  accessed_at: '2026-10-22T05:42:54Z'
  support: context_only
  summary: Taxon-specific accessions identify examples; they do not replace family
    grounding or experimental membership. Formation necessity differs from catalytic
    function and viability.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact grounding, REVIEWED_LABEL_ONLY at159–160 and assembly essentiality
  accessed_at: '2026-10-22T05:42:54Z'
  support: context_only
  summary: Label-only review status denotes a genuinely unresolved exact mapping.
    A domain or broader family must not replace an exact named protein class.
- evidence_id: graph-rubric
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Membership versus assembly and coarse functional-edge scope
  accessed_at: '2026-10-22T05:42:54Z'
  support: context_only
  summary: NONMECHANISTIC membership and catalogued activity are assessed without
    claiming that a static structure establishes a complete dynamic mechanism.
- evidence_id: root51-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846,GO:0009360,GO:0044776,GO:0044775,GO:0043847,GO:0032991,GO:0042575,GO:0003887,GO:0006260,GO:0003689
  locator: All ten term identities/definitions/synonyms/comments; relevant typed child
    links. Unrelated GO0032991 descendants not audited.
  accessed_at: '2026-10-22T05:38:54.490511Z'
  support: supports
  summary: Exact active PolIII holoenzyme/core/clamp-loader identities, native synonyms
    and typed holoenzyme parthood links are present. The clamp-loader and core definitions
    match the named structures. The beta-clamp cross-class sentence is not used as
    a stoichiometric claim here.
  snapshot_sha256: ddeb6461ed42738f76028c9ac0011c145d7cf09bf15815fc3ca84b50701c9d14
- evidence_id: root51-sources-pmid-3283127
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A3283127+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact identifier/title/author/year/DOI and complete abstract
  accessed_at: '2026-10-22T05:38:57.977154Z'
  support: supports
  summary: 'Native MED3283127: DNA polymerase III holoenzyme of Escherichia coli.
    III. Distinctive processive polymerases reconstituted from purified subunits.
    by Maki S, Kornberg A. (1988), DOI 10.1016/s0021-9258(18)68678-8. Complete native
    abstract read; source-specific body access is stated separately.'
  snapshot_sha256: e60e241e1e61deefc7e23fe8b4e4e2ee05d059de9f6c30ea27993a8ab0597074
- evidence_id: root51-sources-tax562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:38:57.355358Z'
  support: supports
  summary: ENA identifies taxon562 as Escherichia coli. Species and reference-strain
    levels are kept separate.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: root51-sources-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:38:57.520022Z'
  support: supports
  summary: ENA identifies taxon83333 as Escherichia coli K-12. Species and reference-strain
    levels are kept separate.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: root51-sources-protein-P10443
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P10443.json
  locator: Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY;
    relevant InterPro/GO xrefs
  accessed_at: '2026-10-22T05:38:56.318686Z'
  support: supports
  summary: P10443 is the reviewed K12 dnaE entry with the declared protein identity.
    Native gene/locus tokens, function/subunit annotations, relevant GO annotation
    and family cross-references were inspected. Annotation-referenced experiments
    are not independently certified unless a separate primary-source row says so.
  snapshot_sha256: b7b6bd780313462cb8f38d4a595395fa1a25b608f07fb9610d6bf8b894a202e9
- evidence_id: root51-sources-gene-dnaE
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set for gene_exact:dnaE AND taxonomy_id:83333
    AND reviewed:true; size500
  accessed_at: '2026-10-22T05:38:56.373790Z'
  support: supports
  summary: The complete reviewed exact-gene query returns one result, P10443, with
    the expected primary gene and taxon83333.
  snapshot_sha256: 24a7c7506484b0c644f37cd46d3060a98b52c24a536dc774afdcbc7ba2c4e5e4
- evidence_id: root51-sources-protein-P03007
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P03007.json
  locator: Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY;
    relevant InterPro/GO xrefs
  accessed_at: '2026-10-22T05:38:56.392810Z'
  support: supports
  summary: P03007 is the reviewed K12 dnaQ entry with the declared protein identity.
    Native gene/locus tokens, function/subunit annotations, relevant GO annotation
    and family cross-references were inspected. Annotation-referenced experiments
    are not independently certified unless a separate primary-source row says so.
  snapshot_sha256: 21e6df3ed69332415da811c4d066d8ea6b0a2234a0d4c3dbcb2ff4d3613f7aef
- evidence_id: root51-sources-gene-dnaQ
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaQ%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set for gene_exact:dnaQ AND taxonomy_id:83333
    AND reviewed:true; size500
  accessed_at: '2026-10-22T05:38:56.585343Z'
  support: supports
  summary: The complete reviewed exact-gene query returns one result, P03007, with
    the expected primary gene and taxon83333.
  snapshot_sha256: 2cc26f272453252c03d79d4ceba13fa02254b94b95d2501d84300b975d38f6ba
- evidence_id: root51-sources-protein-P0ABS8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ABS8.json
  locator: Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY;
    relevant InterPro/GO xrefs
  accessed_at: '2026-10-22T05:38:56.803506Z'
  support: supports
  summary: P0ABS8 is the reviewed K12 holE entry with the declared protein identity.
    Native gene/locus tokens, function/subunit annotations, relevant GO annotation
    and family cross-references were inspected. Annotation-referenced experiments
    are not independently certified unless a separate primary-source row says so.
  snapshot_sha256: 0cce0044d1aa6208572485d8e5c538603e9fe638aa1bafcb67fca6bb9c3f0673
- evidence_id: root51-sources-gene-holE
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set for gene_exact:holE AND taxonomy_id:83333
    AND reviewed:true; size500
  accessed_at: '2026-10-22T05:38:57.124454Z'
  support: supports
  summary: The complete reviewed exact-gene query returns one result, P0ABS8, with
    the expected primary gene and taxon83333.
  snapshot_sha256: 0eb3d97acbb204347081e21cec2bf1265cd6b21eda9d8a31ba83a8c96df42680
- evidence_id: root51-sources-maki1988-api
  kind: database
  reference: https://api.elsevier.com/content/article/pii/S0021925818686788?httpAccept=text/xml
  locator: Entire publisher coredata XML; no article body
  accessed_at: '2026-10-22T05:39:47.294325Z'
  support: supports
  summary: The native publisher XML confirms the exact DOI, title, journal and1988
    publication date; this response contains core metadata only, despite its full-text-retrieval
    response name.
  snapshot_sha256: c1bed0605d12c6dc3ac2272a61b03286e8fecae29104f90c2efb114058984b53
- evidence_id: root51-maki1988-publisher
  kind: database
  reference: https://www.jbc.org/article/S0021-9258(18)68678-8/fulltext
  locator: Retained publisher403 response
  accessed_at: '2026-10-22T05:39:47.294023Z'
  support: context_only
  summary: The publisher route did not yield the primary body; this paper is assessed
    at complete native abstract tier.
  snapshot_sha256: 7db7b0f002f2747181469b72daf45bf858d9125401da12cca2f8a09cc97961bd
- evidence_id: root51-maki1988-pdf
  kind: database
  reference: https://www.jbc.org/article/S0021-9258(18)68678-8/pdf
  locator: Retained publisher403 response
  accessed_at: '2026-10-22T05:39:47.294276Z'
  support: context_only
  summary: The publisher route did not yield the primary body; this paper is assessed
    at complete native abstract tier.
  snapshot_sha256: ebfcff9aa58d658572a47664652741787c4a534e9002f88f76d98e3daa9d8735
- evidence_id: root51-sources-GO0044776-is-a
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776/ancestors?relations=is_a
  locator: Complete is-a-only ancestor response
  accessed_at: '2026-10-22T05:40:52.370677Z'
  support: supports
  summary: The native is-a ancestry includes protein-containing complex but currently
    routes through nuclear protein-containing complex. This upstream topology is recorded
    as a conflict with the bacterial primary evidence, not propagated as a required
    biological classification.
  snapshot_sha256: ab4cb6cea7010b6cf36cc956057da7b449aa48a3c9b48064faa49923274a58ab
- evidence_id: root51-sources-GO0044776-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776/constraints
  locator: Complete focal taxonConstraints array; unrelated inherited protein blacklists
    not used
  accessed_at: '2026-10-22T05:38:59.040229Z'
  support: context_only
  summary: Native GO currently reports only_in_taxon Eukaryota for this bacterial
    complex. The record has no such assertion; primary E.coli evidence and the source
    definition conflict with that upstream restriction.
  snapshot_sha256: e70c1e9bafcda161d87935729c4dfa60dcd64a8e4c324c92063982fe305f2af1
- evidence_id: root51-sources-GO0044776-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776/history
  locator: Complete history array
  accessed_at: '2026-10-22T05:38:58.925881Z'
  support: context_only
  summary: Complete native history records the2020 nuclear-parent change and a2024
    bad-taxon-ID constraint entry. This provides provenance of an upstream discrepancy,
    not bacterial taxonomic evidence.
  snapshot_sha256: 59b1db327dbb914146f4ce1406d92f19dbdefa22a195ec32dc96891743f99d7a
- evidence_id: root51-sources-ipr-IPR009052
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009052/
  locator: Native name/type, complete description and flags, hierarchy and member
    signatures
  accessed_at: '2026-10-22T05:39:48.139822Z'
  support: supports
  summary: Exact bacterial theta whole-protein family with PF06440.
  snapshot_sha256: 45912f79b5935dd572120ecb8fcf31e9a8343e5e8539ccbc69483c268708432b
- evidence_id: root51-sources-ipr-IPR006309
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006309/
  locator: Native name/type, complete description and flags, hierarchy and member
    signatures
  accessed_at: '2026-10-22T05:39:48.090368Z'
  support: supports
  summary: Whole epsilon family is explicitly proteobacterial; useful for the E.coli
    instance, not automatically equivalent to a taxon-agnostic epsilon class.
  snapshot_sha256: 7a5dca1c5c7696f56079daf029888fd3b04af5cd59190ad06c3c1c1e9aebacbf
- evidence_id: root51-sources-ipr-IPR006054
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006054/
  locator: Native name/type, complete description and flags, hierarchy and member
    signatures
  accessed_at: '2026-10-22T05:39:48.080636Z'
  support: supports
  summary: DnaQ exonuclease domain also includes paralogs and DinG regions; it is
    not an exact whole-protein epsilon family.
  snapshot_sha256: 319bb97f2f94ae18c1a3f2bcbad55764516d14a4cd05ded2abaf1e45cfc9aaf8
- evidence_id: root51-sources-ipr-IPR004805
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004805/
  locator: Native name/type, complete description and flags, hierarchy and member
    signatures
  accessed_at: '2026-10-22T05:39:48.327592Z'
  support: supports
  summary: Broader family includes DnaE2 error-prone polymerase, DnaE and PolC; it
    is not an exact stand-in for the core DnaE class.
  snapshot_sha256: 570a9854bc1ebd4db316953b55a0d871d2d11cd2449df72aa370eb9cab8ff7a1
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dna_polymerase_iii_core_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:17Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dna_polymerase_iii_core_complex.yaml'
  snapshot_sha256: 66a8c2568d45d0f174582835802af440a0b7ec1cf266a9a6559908a663362bf9
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dna_polymerase_iii_core_complex.yaml
    --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_core_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:20Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dna_polymerase_iii_core_complex.yaml\
    \ --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_core_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_core_complex-strict.tsv"
  snapshot_sha256: 8946219079db2432b36174017ec1a556cbde68f789d52f281e3532e86142b552
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dna_polymerase_iii_core_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:39:33.718304Z'
  support: supports
  summary: "data/structures/other/dna_polymerase_iii_core_complex.yaml  (GO:0044776)\n\
    \  pol_iii_core_catalysis\talpha_subunit\tCOVERED\t->alpha_subunit (UniProtKB:P10443)\n\
    \  pol_iii_core_catalysis\tepsilon_subunit\tCOVERED\t->epsilon_subunit (UniProtKB:P03007)\n\
    \  pol_iii_core_catalysis\ttheta_subunit\tCOVERED\t->theta_subunit (UniProtKB:P0ABS8)\n\
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
  snapshot_sha256: 622c34a9d261773a36cbd6c978ead78ec02d5fe3b0cb7c2e0e1c6688ceff466d
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dna_polymerase_iii_core_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:39:35.184492Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dna_polymerase_iii_core_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '9 of 10 collected target identifiers returned OK. PMID:3283127: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
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
  topic: Alpha-epsilon-theta catalytic subassembly
  outcome: supported
  target_ids:
  - GO:0044776
  summary: Native GO and the complete Maki/Kornberg abstract identify this core, polymerase/proofreading
    activities and holoenzyme parthood. DNA-polymerase-complex parentage is biologically
    supported by the core polymerase activity; it is not claimed as a direct native
    GO is-a edge.
  evidence_ids:
  - record
  - root51-sources-go
  - root51-sources-pmid-3283127
  - root51-sources-GO0044776-is-a
- assessment_id: composition
  area: grounding
  topic: Correct examples and exact versus broad families
  outcome: concern
  target_ids:
  - GO:0044776
  summary: P10443/dnaE, P03007/dnaQ and P0ABS8/holE are verified reviewed K12 examples
    with membership independently supported at primary-abstract tier. Exact theta
    family IPR009052 is available. DnaQ IPR006309 is proteobacterial, IPR006054 a
    domain, and IPR004805 includes DnaE2/PolC, so their scope must not be silently
    generalized.
  evidence_ids:
  - record
  - curation
  - root51-sources-protein-P10443
  - root51-sources-protein-P03007
  - root51-sources-protein-P0ABS8
  - root51-sources-gene-dnaE
  - root51-sources-gene-dnaQ
  - root51-sources-gene-holE
  - root51-sources-ipr-IPR009052
  - root51-sources-ipr-IPR006309
  - root51-sources-ipr-IPR006054
  - root51-sources-ipr-IPR004805
  - root51-sources-pmid-3283127
- assessment_id: scope
  area: scope
  topic: Species-level canonical reconstitution
  outcome: supported
  target_ids:
  - GO:0044776
  summary: Maki/Kornberg directly reports E.coli purified-subunit reconstitution in
    its abstract, supporting the species-level canonical note. K12 examples are independently
    verified identities; no exact Maki experimental strain, growth conditions or full
    methods are asserted.
  evidence_ids:
  - record
  - root51-sources-pmid-3283127
  - root51-sources-tax562
  - root51-sources-tax83333
  - root51-sources-protein-P10443
  - root51-sources-protein-P03007
  - root51-sources-protein-P0ABS8
- assessment_id: graph
  area: graph
  topic: Membership and two catalytic activities
  outcome: supported
  target_ids:
  - GO:0044776
  summary: All three membership edges and both core activity edges agree with native
    GO and the Maki abstract. The polymerase molecular function remains separate from
    proofreading. Theta is not individually asserted to catalyze either activity,
    and the graph does not claim a tested assembly sequence.
  evidence_ids:
  - record
  - graph-rubric
  - root51-sources-go
  - root51-sources-pmid-3283127
- assessment_id: formation
  area: grounding
  topic: Named constituents and uncertain physical necessity
  outcome: unknown
  target_ids:
  - GO:0044776
  summary: The defined core contains alpha, epsilon and theta; the cited abstract
    reports partial assemblies and functional reconstitution, not a complete loss-of-physical-assembly
    series. UNKNOWN formation essentiality remains explicit; theta annotation uncertainty
    is not evidence that theta is absent.
  evidence_ids:
  - record
  - schema
  - root51-sources-pmid-3283127
  - root51-sources-protein-P10443
  - root51-sources-protein-P03007
  - root51-sources-protein-P0ABS8
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target
  outcome: supported
  target_ids:
  - GO:0044776
  summary: All fields, history, discussions and edge evidence were reviewed. Optional
    images, dimensions or prevalence inventories are not filled without evidence.
    Cited authority identities and source-scoped claims were checked separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root51-sources-go
findings:
- finding_id: F1
  issue_key: pol-iii-core-theta-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the theta subunit with its exact family
  description: HolE remains REVIEWED_LABEL_ONLY and the current TODO defers all three
    core classes, although native IPR009052 is an exact full-protein theta family
    and P0ABS8 independently carries that family xref. Other inspected candidates
    are broader or taxon-limited.
  target_ids:
  - GO:0044776
  field_paths:
  - components#theta_subunit.grounding_status
  - discussions#resolve_pol_iii_core_subunit_groundings
  evidence_ids:
  - record
  - curation
  - root51-sources-ipr-IPR009052
  - root51-sources-ipr-IPR006309
  - root51-sources-ipr-IPR006054
  - root51-sources-ipr-IPR004805
  - root51-sources-protein-P10443
  - root51-sources-protein-P03007
  - root51-sources-protein-P0ABS8
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_core_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-scoped composition
  native_severity: minor
  normalization_reason: Correct structure identity, supported protein examples and
    core functional model remain intact; the defect is a bounded mapping or composition-wording
    gap.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0044776
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_core_complex.yaml
    role: maintained scientific record
  description: Use IPR009052 for the theta class and narrow the current TODO. Preserve
    correct DnaE/DnaQ examples and unresolved exact taxon-neutral class boundaries.
  acceptance_checks:
  - Verify family type/name/PF06440 and separate example membership.
  - Do not substitute the DnaQ domain or broad DnaE2/DnaE/PolC family.
  - Preserve source scope and correct current protein examples; pass applicable native
    validators.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, coordinates, sequence alignments or raw kinetic data were reanalyzed.
  Native annotations and a secondary review remain distinct from independently inspected
  primary methods.
- Maki/Kornberg1988 is verified at complete abstract tier only; publisher HTML and
  PDF requests returned403 and API returned metadata only. Exact assay methods, expression
  strains and figures are not certified. Its abstract directly supports the species-level
  reconstitution and stated core activities.
- Native GO currently assigns this term nuclear-complex ancestry and an Eukaryota-only
  restriction, conflicting with the cited E.coli evidence. Neither assertion is present
  in the target. Keep its exact named identity and supported bacterial example; do
  not import the erroneous source restriction or infer occurrence in every bacterium.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes qualified clean reviews as well as issue-bearing
  reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
