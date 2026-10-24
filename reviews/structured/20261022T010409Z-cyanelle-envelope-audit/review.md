# Organelle identity, composition and evidence review

- Review: 20261022T010409Z-cyanelle-envelope-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T11:20:56Z
- Finished UTC: 2026-10-22T01:04:09Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed in the cyanelle envelope record. Exact native identities, material placement, taxonomic context and descriptive topology have support at the explicitly inspected source scopes.

## Scope And Provenance

Entire single record with exact authority identities, declared source-reading scopes, protein checks where applicable and component/function/graph boundaries.

Selection: Target 5 in batch twenty-five; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033112 | data/structures/membrane_organelle/cyanelle_envelope.yaml | maintained | cyanelle envelope |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0033112 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Native protein causal-graphs | passed | True | GO:0033112 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Focused native schema | passed | True | GO:0033112 | Focused validator passed. |
| Focused native strict | passed | True | GO:0033112 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0033112 | 14 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0033112 | No expression-module or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | GO:0033112 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0033112 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0033112 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0033112 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0033112 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0033112 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact whole and boundary identity

identity: supported. Targets: GO:0033112.

The maintained target denotes the entire double envelope GO:0033112, including the intermembrane space. Plastid-envelope is-a, cyanelle part-of and exact inner/outer/space has-part relations preserve the native scope. GO:0033113 is an unspecified individual envelope bilayer, not an interchangeable identity.

### Material versus compartment identity and assembly essentiality

grounding: supported. Targets: GO:0033112.

The lipid component rows identify actual constituent bilayers at exact GO membrane terms, rather than attaching a whole compartment identity to an arbitrary protein. The peptidoglycan sheet has biochemical support and an explicit reviewed-label-only grounding discussion; the entire intermembrane space is broader. UNKNOWN essentiality does not assert absence of function and correctly avoids treating occurrence, channel activity or peptidoglycan binding as an organelle-formation knockout. Exact molecular stoichiometry and complete membrane protein inventories are not claimed.

### Native taxa and experimental occurrence

scope: supported. Targets: GO:0033112.

ENA resolves species2762 Cyanophora paradoxa and class38254 Glaucocystophyceae, with glaucophyte alternative nomenclature. COMMON is used as qualitative characteristic occurrence, not a numerical census. The generic C. paradoxa canonical example is supported by the inspected Giddings microscopy source and separately by biochemical material studies. The cross-genus Pfanzagl abstract supports the named Glaucocystis, Cyanoptyche and Cyanophora context; no full-paper experimental details are inferred.

### Claim-level topology and functional scope

evidence: supported. Targets: GO:0033112.

Every six-edge envelope graph assertion was read. The explicitly NONMECHANISTIC graph preserves outer-facing versus stroma-facing membrane orientation, with the inner membrane bounding stroma and peptidoglycan residing in the intermembrane space. The envelope contains the intervening space; it is not equated to either individual bilayer. No unrepresented transport machinery is presented as an established mechanism.

### Bibliographic and source-reading boundaries

evidence: supported. Targets: GO:0033112.

Native DOI/PMID rows identify the cited works and full returned abstracts. Giddings scanned pages409,414,416,417 were visually read at the exact locators; the other pages are not attested by this reviewer. Kojima specified main-text sections and the cross-genus Pfanzagl complete abstract were inspected. Pfanzagl primary-structure support is abstract-level only. Existing evidence is paraphrased in notes; no verbatim snippet fidelity is claimed.

### Bounded record-level coverage

completeness: supported. Targets: GO:0033112.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Additional exhaustive component inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. This bounded review does not assert exhaustive literature completeness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/cyanelle_envelope.yaml; Entire maintained YAML including history, all evidence notes, components, functions, graph edges and discussions | context_only | All maintained fields were read. No scientific edit or mapping-status promotion is made. |
| policy | docs/CURATION.md; Exact identity, claim-level evidence, material versus localization grounding, and component assembly-essentiality contract | context_only | Family identity, concrete protein examples and structure membership are separate; activity and viability are not by themselves formation assays. Optional inventories are not mandatory. |
| root25-sources-cyanelle-envelope-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009526,GO:0009842,GO:0033112,GO:0033113,GO:0034060,GO:0036012,GO:0036013,GO:0036014; Complete returned terms: identity, definitions, synonyms and immediate hierarchy | supports | All returned native GO identifiers, active status, names, definitions, relevant relationships and synonyms were read. Whole plastid, double envelope, unspecified envelope bilayer, exact inner/outer bilayers, intermembrane space and stroma are distinct identities. The peptidoglycan sheet is included in the intermembrane-space definition but is not identical to that entire space. |
| root25-sources-SL-0479 | https://rest.uniprot.org/locations/SL-0479.json; Exact accession, label, definition, GO cross-reference and location hierarchy | supports | Native UniProt location identity and hierarchy agree with the exact GO target. The cyanelle envelope includes the peptidoglycan layer; the whole plastid is not an individual envelope bilayer. |
| root25-sources-NCBITaxon-2762 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Cyanophora paradoxa at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root25-sources-NCBITaxon-38254 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Glaucocystophyceae at class rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root25-sources-doi-10.1104_pp.71.2.409 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1104/pp.71.2.409%22; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Structure of the Thylakoids and Envelope Membranes of the Cyanelles of Cyanophora paradoxa. PMID 16662839; DOI 10.1104/pp.71.2.409. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root25-sources-doi-10.1128_jb.178.2.332-339.1996 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1128/jb.178.2.332-339.1996%22; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Primary structure of cyanelle peptidoglycan of Cyanophora paradoxa: a prokaryotic cell wall as part of an organelle envelope. PMID 8550450; DOI 10.1128/jb.178.2.332-339.1996. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root25-sources-doi-10.1074_jbc.M116.746131 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1074/jbc.M116.746131%22; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Outer Membrane Proteins Derived from Non-cyanobacterial Lineage Cover the Peptidoglycan of Cyanophora paradoxa Cyanelles and Serve as a Cyanelle Diffusion Channel. PMID 27502278; DOI 10.1074/jbc.m116.746131. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root25-sources-PMID-8955325 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8955325%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies N-acetylputrescine as a characteristic constituent of cyanelle peptidoglycan in glaucocystophyte algae. PMID 8955325; DOI 10.1128/jb.178.23.6994-6997.1996. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| cyanelle-agent-pfanzagl1996-numeric | https://pmc.ncbi.nlm.nih.gov/articles/177662/; Complete abstract and bibliographic identity only | supports | The complete visible abstract describes the biochemical primary structure of Cyanophora paradoxa cyanelle peptidoglycan and its unusual N-acetylputrescine modification. This supports material identity and occurrence, not a full-paper read or a gene-specific necessity experiment. The page is a legacy abstract/PDF-link surface, not readable full article text. |
| cyanelle-agent-kojima2016-numeric | https://pmc.ncbi.nlm.nih.gov/articles/5025702/; Introduction section1; Results section5 including figure1–5 captions; Experimental Procedures sections13–19. Other prose, image pixels and table cells not certified here. | supports | Inspected complete Introduction, Results including figure 1–5 captions, and Experimental Procedures sections13–19. C. paradoxa NIES-547 outer-envelope preparations contain CppS/F associated with peptidoglycan; reduction of disulfides reduces binding and reconstituted channel experiments concern permeability. Those experiments support the outer/peptidoglycan relationship without proving every molecular species is essential to organelle formation. |
| cyanelle-agent-giddings1983-page409 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/6ed041edd2c7/plntphys00558-0203.png; Title, abstract, visible Introduction and first culture-method paragraph; original scanned page | supports | Native abstract identifies the thylakoid and envelope ultrastructure study. Visible culture methods identify C. paradoxa UTEX LB555 at26C; the record itself makes no strain or temperature assertion. |
| cyanelle-agent-giddings1983-page414 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/9d4d067999da/plntphys00558-0208.png; Original scanned Results: Envelope Membranes subsection and figure11–12 captions; paragraph continues on416 | supports | Visible envelope Results distinguish an inner membrane and intervening peptidoglycan-associated layer from the outer membrane. Historical provisional interpretation is preserved. |
| cyanelle-agent-giddings1983-page416 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png; Original scanned continuation of envelope Results and visible Discussion; histograms not quantitatively audited | supports | Outer-membrane fracture faces and peeling or blistering support the double-envelope boundary description. Visible Discussion relates thylakoid organization and phycobilisomes; microscopy alone does not establish chemical composition. |
| cyanelle-agent-giddings1983-page417 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png; Original scanned Discussion continuation including envelope interpretation; figure16–18 captions | supports | The membrane and layer relationships support the narrow topology. Dated discussion of symbiont versus organelle status is historical context, not the current taxonomic or organelle authority. |
| root25-sources-pfanzagl1996-taxa-pmc-numeric | https://pmc.ncbi.nlm.nih.gov/articles/178604/; Complete abstract and bibliographic identity only | supports | Read the complete visible abstract: cyanelle peptidoglycan isolated from Glaucocystis nostochinearum and Cyanoptyche gloeocystis was compared with Cyanophora paradoxa. The native surface supplies an abstract and scanned-PDF link, not readable main text. This supports occurrence across the named glaucophyte genera, not a numerical prevalence estimate. |
| root25-sources-pfanzagl1996-taxa-pdf-instance | https://pmc.ncbi.nlm.nih.gov/articles/instance/178604/pdf/1786994.pdf; Actual source-access response, not article content | context_only | The PDF-instance route returned an HTTP200 download challenge page, not PDF article content. No full-text claim is based on it. |
| root25-sources-pg-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cyanelle%20peptidoglycan&amp;limit=100; Complete returned result identifiers and labels for the recorded query | context_only | The bounded QuickGO cyanelle-peptidoglycan query returned64 of64 reported results. Returned labels and identifiers were inspected; related material or cellular-space terms are not an exact standalone cyanelle peptidoglycan-sheet identity. This does not prove universal ontology absence and does not force replacing an explicitly label-only structural component. |
| native-verify | /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml --verify; Exact focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml --causal-graphs; Exact focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/cyanelle_envelope.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/cyanelle_envelope.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/cyanelle_envelope.yaml --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_envelope-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/cyanelle_envelope.yaml --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_envelope-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_envelope-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/cyanelle_envelope.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 14 of15 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:8955325: UNREACHABLE; resolved by evidence root25-sources-PMID-8955325. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Pfanzagl1996 primary-structure evidence was inspected as the complete native abstract only; no full Methods/Results read is claimed. The cross-genus Pfanzagl1996 work is also abstract-only; full-text attempts returned unavailable or challenge responses.
- The reviewed-label-only peptidoglycan-sheet grounding remains open; the bounded authority search is not proof that no exact term exists anywhere.
- Qualitative COMMON occurrence is not a measured population prevalence. Constitutional membrane identity does not establish the necessity of each molecular constituent.
- Giddings direct source reading covers only scanned pages409,414,416,417 at the stated locators; historical terminology is not substituted for current native identities.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization; identifier transport and label-adapter limits remain explicit.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for every uncovered target, including a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T010409Z-cyanelle-envelope-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Organelle identity, composition and evidence review
started_at: '2026-10-21T11:20:56Z'
finished_at: '2026-10-22T01:04:09Z'
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
summary: No concrete curation defect observed in the cyanelle envelope record. Exact
  native identities, material placement, taxonomic context and descriptive topology
  have support at the explicitly inspected source scopes.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/cyanelle.yaml
    sha256: 24275c8050ca5d13c66d563c7aa697a4de65766f87499f876fc94c41cd2f0db7
    role: context
  - path: data/structures/membrane_organelle/cyanelle_envelope.yaml
    sha256: 4a25594b3a26541401976d3ab78f271bc8726951462af9073fafc0eff2389a67
    role: target
  - path: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    sha256: f10bb4f3ff44fb6d0b23e67379861768a590eb6d3da75686e296a0a5b3b26970
    role: context
  - path: data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
    sha256: aba8ad62f544ec82bea2f4767a8c79cc45d3fe117423163fc1ce1211a2527f8c
    role: context
  - path: data/structures/membrane_organelle/cyanelle_membrane.yaml
    sha256: b95c9fcb293bd9f434df3ccf9ecaa7c9bf04e1f83a95a2cd19673441a537a20b
    role: context
  - path: data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
    sha256: 2f058b25ce3bf1b49d52bc03391ee46d6e26376860035469f037d27c52234047
    role: context
  - path: data/structures/membrane_organelle/cyanelle_stroma.yaml
    sha256: 13d83e3dadca9cafaa6550a7bf84cd8066bf1539ccaacd3627ec23aa5b08e118
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
  - path: scripts/score_causal_graphs.py
    sha256: 5ffe450c5b37c3dc3b0e62672caf0d99b358c8249fcc98a8c4fc7d78e8cd0d2f
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0033112
  path: data/structures/membrane_organelle/cyanelle_envelope.yaml
  label: cyanelle envelope
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_envelope.yaml
    role: maintained scientific record
scope:
  description: Entire single record with exact authority identities, declared source-reading
    scopes, protein checks where applicable and component/function/graph boundaries.
  selection: Target 5 in batch twenty-five; exact sorted uncovered path at frozen
    fresh-main revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033112
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0033112
  command: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml
    --verify
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0033112
  command: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0033112
  command: just validate data/structures/membrane_organelle/cyanelle_envelope.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0033112
  command: just validate-strict data/structures/membrane_organelle/cyanelle_envelope.yaml
    --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_envelope-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0033112
  summary: 14 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - root25-sources-PMID-8955325
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0033112
  summary: No expression-module or transcriptomic inference is made by this structural
    review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0033112
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - root25-sources-cyanelle-envelope-go
  - root25-sources-SL-0479
  - root25-sources-NCBITaxon-2762
  - root25-sources-NCBITaxon-38254
  - root25-sources-doi-10.1104_pp.71.2.409
  - root25-sources-doi-10.1128_jb.178.2.332-339.1996
  - root25-sources-doi-10.1074_jbc.M116.746131
  - root25-sources-PMID-8955325
  - cyanelle-agent-pfanzagl1996-numeric
  - cyanelle-agent-kojima2016-numeric
  - cyanelle-agent-giddings1983-page409
  - cyanelle-agent-giddings1983-page414
  - cyanelle-agent-giddings1983-page416
  - cyanelle-agent-giddings1983-page417
  - root25-sources-pfanzagl1996-taxa-pmc-numeric
  - root25-sources-pfanzagl1996-taxa-pdf-instance
  - root25-sources-pg-go-search
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0033112
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
  - GO:0033112
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
  - GO:0033112
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
  - GO:0033112
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
  - GO:0033112
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
  reference: data/structures/membrane_organelle/cyanelle_envelope.yaml
  locator: Entire maintained YAML including history, all evidence notes, components,
    functions, graph edges and discussions
  accessed_at: '2026-10-22T00:57:58Z'
  support: context_only
  summary: All maintained fields were read. No scientific edit or mapping-status promotion
    is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, claim-level evidence, material versus localization grounding,
    and component assembly-essentiality contract
  accessed_at: '2026-10-22T00:57:58Z'
  support: context_only
  summary: Family identity, concrete protein examples and structure membership are
    separate; activity and viability are not by themselves formation assays. Optional
    inventories are not mandatory.
- evidence_id: root25-sources-cyanelle-envelope-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009526,GO:0009842,GO:0033112,GO:0033113,GO:0034060,GO:0036012,GO:0036013,GO:0036014
  locator: 'Complete returned terms: identity, definitions, synonyms and immediate
    hierarchy'
  accessed_at: '2026-10-21T11:21:15.176356Z'
  support: supports
  summary: All returned native GO identifiers, active status, names, definitions,
    relevant relationships and synonyms were read. Whole plastid, double envelope,
    unspecified envelope bilayer, exact inner/outer bilayers, intermembrane space
    and stroma are distinct identities. The peptidoglycan sheet is included in the
    intermembrane-space definition but is not identical to that entire space.
  snapshot_sha256: 1556173574763de2ba8d4db3e81fde049a26a7eeac779aa2a104df89fa3e26ce
- evidence_id: root25-sources-SL-0479
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0479.json
  locator: Exact accession, label, definition, GO cross-reference and location hierarchy
  accessed_at: '2026-10-21T11:21:15.248090Z'
  support: supports
  summary: Native UniProt location identity and hierarchy agree with the exact GO
    target. The cyanelle envelope includes the peptidoglycan layer; the whole plastid
    is not an individual envelope bilayer.
  snapshot_sha256: f926a2da38e46b3f002892ab0db2dab5d69d1cbc5d703d2cf0fe3f9d1f3312b6
- evidence_id: root25-sources-NCBITaxon-2762
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T11:21:14.553866Z'
  support: supports
  summary: Native ENA taxonomy identifies Cyanophora paradoxa at species rank. Only
    this taxon's identity and names are asserted by this row, not occurrence or experimental
    stock identity.
  snapshot_sha256: 285d213ba479ce1d232bf54aac3efda6f16d45546b5ce13284818fc16482408a
- evidence_id: root25-sources-NCBITaxon-38254
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T11:21:14.559158Z'
  support: supports
  summary: Native ENA taxonomy identifies Glaucocystophyceae at class rank. Only this
    taxon's identity and names are asserted by this row, not occurrence or experimental
    stock identity.
  snapshot_sha256: 4b487eb0e34bcb4941fbb315aae5214c96ea6f60255d71a2aca172cd35844009
- evidence_id: root25-sources-doi-10.1104_pp.71.2.409
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1104/pp.71.2.409%22
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T11:21:14.649813Z'
  support: supports
  summary: Native citation identifies Structure of the Thylakoids and Envelope Membranes
    of the Cyanelles of Cyanophora paradoxa. PMID 16662839; DOI 10.1104/pp.71.2.409.
    Exact bibliographic fields and the complete returned abstract were inspected;
    this row does not attest a full-text read.
  snapshot_sha256: 63e06e7891bc1f0bf83152a34ce823faa160c98bf984757e546f4acb00f202dc
- evidence_id: root25-sources-doi-10.1128_jb.178.2.332-339.1996
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1128/jb.178.2.332-339.1996%22
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T11:21:15.265478Z'
  support: supports
  summary: 'Native citation identifies Primary structure of cyanelle peptidoglycan
    of Cyanophora paradoxa: a prokaryotic cell wall as part of an organelle envelope.
    PMID 8550450; DOI 10.1128/jb.178.2.332-339.1996. Exact bibliographic fields and
    the complete returned abstract were inspected; this row does not attest a full-text
    read.'
  snapshot_sha256: 1f192e6160692da29293cf7e4a716b43fafe82d4c880157bed2a9a265ff1bd4a
- evidence_id: root25-sources-doi-10.1074_jbc.M116.746131
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1074/jbc.M116.746131%22
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T11:21:14.809391Z'
  support: supports
  summary: Native citation identifies Outer Membrane Proteins Derived from Non-cyanobacterial
    Lineage Cover the Peptidoglycan of Cyanophora paradoxa Cyanelles and Serve as
    a Cyanelle Diffusion Channel. PMID 27502278; DOI 10.1074/jbc.m116.746131. Exact
    bibliographic fields and the complete returned abstract were inspected; this row
    does not attest a full-text read.
  snapshot_sha256: b835645082c5bb585962834b3e53b0e285fecd37ac866ca00e807e49145881b7
- evidence_id: root25-sources-PMID-8955325
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8955325%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T11:21:15.252863Z'
  support: supports
  summary: Native citation identifies N-acetylputrescine as a characteristic constituent
    of cyanelle peptidoglycan in glaucocystophyte algae. PMID 8955325; DOI 10.1128/jb.178.23.6994-6997.1996.
    Exact bibliographic fields and the complete returned abstract were inspected;
    this row does not attest a full-text read.
  snapshot_sha256: 524d7aaf7d2bbac6330c4f400d2e42d83ce18d7df7dbb059bf40f3d209b72760
- evidence_id: cyanelle-agent-pfanzagl1996-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/177662/
  locator: Complete abstract and bibliographic identity only
  accessed_at: '2026-10-21T11:23:30.540460Z'
  support: supports
  summary: The complete visible abstract describes the biochemical primary structure
    of Cyanophora paradoxa cyanelle peptidoglycan and its unusual N-acetylputrescine
    modification. This supports material identity and occurrence, not a full-paper
    read or a gene-specific necessity experiment. The page is a legacy abstract/PDF-link
    surface, not readable full article text.
  snapshot_sha256: 533ae6d93d44f03a0b85dbabde710151a4ab65530e6eadb64348fc30527781b7
- evidence_id: cyanelle-agent-kojima2016-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/5025702/
  locator: Introduction section1; Results section5 including figure1–5 captions; Experimental
    Procedures sections13–19. Other prose, image pixels and table cells not certified
    here.
  accessed_at: '2026-10-21T11:23:30.539986Z'
  support: supports
  summary: Inspected complete Introduction, Results including figure 1–5 captions,
    and Experimental Procedures sections13–19. C. paradoxa NIES-547 outer-envelope
    preparations contain CppS/F associated with peptidoglycan; reduction of disulfides
    reduces binding and reconstituted channel experiments concern permeability. Those
    experiments support the outer/peptidoglycan relationship without proving every
    molecular species is essential to organelle formation.
  snapshot_sha256: 12d136f74e19613b9c83a0dc5ace6fd69346fa2459a2a29a719e3acc69463ce7
- evidence_id: cyanelle-agent-giddings1983-page409
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/6ed041edd2c7/plntphys00558-0203.png
  locator: Title, abstract, visible Introduction and first culture-method paragraph;
    original scanned page
  accessed_at: '2026-10-22T00:53:33.924113Z'
  support: supports
  summary: Native abstract identifies the thylakoid and envelope ultrastructure study.
    Visible culture methods identify C. paradoxa UTEX LB555 at26C; the record itself
    makes no strain or temperature assertion.
  snapshot_sha256: c0184058c66810b2544be1af57fac9acc2bbbfcdf71ee1186aade8232e5c9f61
- evidence_id: cyanelle-agent-giddings1983-page414
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/9d4d067999da/plntphys00558-0208.png
  locator: 'Original scanned Results: Envelope Membranes subsection and figure11–12
    captions; paragraph continues on416'
  accessed_at: '2026-10-22T00:53:33.927250Z'
  support: supports
  summary: Visible envelope Results distinguish an inner membrane and intervening
    peptidoglycan-associated layer from the outer membrane. Historical provisional
    interpretation is preserved.
  snapshot_sha256: 331f5f9fdd4e16e2a8cb67d9b5d45cca5467dc6554051cfa6696e34471e7bb82
- evidence_id: cyanelle-agent-giddings1983-page416
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png
  locator: Original scanned continuation of envelope Results and visible Discussion;
    histograms not quantitatively audited
  accessed_at: '2026-10-22T00:53:34.247595Z'
  support: supports
  summary: Outer-membrane fracture faces and peeling or blistering support the double-envelope
    boundary description. Visible Discussion relates thylakoid organization and phycobilisomes;
    microscopy alone does not establish chemical composition.
  snapshot_sha256: 41f820c6bde6abc4318ac32baa45293634543bb4aceb0dc5129c3d25414e91ef
- evidence_id: cyanelle-agent-giddings1983-page417
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png
  locator: Original scanned Discussion continuation including envelope interpretation;
    figure16–18 captions
  accessed_at: '2026-10-22T00:53:34.248245Z'
  support: supports
  summary: The membrane and layer relationships support the narrow topology. Dated
    discussion of symbiont versus organelle status is historical context, not the
    current taxonomic or organelle authority.
  snapshot_sha256: 276c1cb60d1a909200199f8e24495840d2caa5f5131c8a896d3f97d70e5bcf6f
- evidence_id: root25-sources-pfanzagl1996-taxa-pmc-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/178604/
  locator: Complete abstract and bibliographic identity only
  accessed_at: '2026-10-21T11:22:53.944087Z'
  support: supports
  summary: 'Read the complete visible abstract: cyanelle peptidoglycan isolated from
    Glaucocystis nostochinearum and Cyanoptyche gloeocystis was compared with Cyanophora
    paradoxa. The native surface supplies an abstract and scanned-PDF link, not readable
    main text. This supports occurrence across the named glaucophyte genera, not a
    numerical prevalence estimate.'
  snapshot_sha256: de267d803d78831735844842bf3eff87bed0cdccbd1a12c794b5793e32058b26
- evidence_id: root25-sources-pfanzagl1996-taxa-pdf-instance
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/instance/178604/pdf/1786994.pdf
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-22T00:53:05.830548Z'
  support: context_only
  summary: The PDF-instance route returned an HTTP200 download challenge page, not
    PDF article content. No full-text claim is based on it.
  snapshot_sha256: 29fb4e791c207b13a145afb50f69fd4b21facf25f1abbb446f082fbec9449e12
- evidence_id: root25-sources-pg-go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cyanelle%20peptidoglycan&limit=100
  locator: Complete returned result identifiers and labels for the recorded query
  accessed_at: '2026-10-21T11:22:54.253789Z'
  support: context_only
  summary: The bounded QuickGO cyanelle-peptidoglycan query returned64 of64 reported
    results. Returned labels and identifiers were inspected; related material or cellular-space
    terms are not an exact standalone cyanelle peptidoglycan-sheet identity. This
    does not prove universal ontology absence and does not force replacing an explicitly
    label-only structural component.
  snapshot_sha256: 3d8aae3b2ec8cd6a34b229f338851ac92353011aee8804df8e0a35b1cdce8358
  search_scope: Native QuickGO query cyanelle peptidoglycan, limit100;64 results reported
    and all64 returned labels/identifiers inspected. This authority search is bounded
    to the recorded query, not an exhaustive all-ontology absence search; local absence
    is not asserted.
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml
    --verify
  locator: Exact focused native output
  accessed_at: '2026-10-21T11:22:08.075278Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_envelope.yaml
    --causal-graphs
  locator: Exact focused native output
  accessed_at: '2026-10-21T11:22:08.545090Z'
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
  reference: just validate data/structures/membrane_organelle/cyanelle_envelope.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:20:58Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/cyanelle_envelope.yaml'
  snapshot_sha256: e0d8837b3629d4c193db21c4d8556c21df55270117decc53b85f545207c687e8
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/cyanelle_envelope.yaml
    --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_envelope-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:20:59Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/cyanelle_envelope.yaml\
    \ --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_envelope-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_envelope-strict.tsv"
  snapshot_sha256: aa450d5f1f66dd442c8d786f39c7fe8e4cb969af09aa7a055cc1d265f8b6fb99
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/cyanelle_envelope.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-22T00:57:58Z'
  support: supports
  summary: '14 of15 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:8955325: UNREACHABLE; resolved by evidence root25-sources-PMID-8955325.
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
  topic: Exact whole and boundary identity
  outcome: supported
  target_ids:
  - GO:0033112
  summary: The maintained target denotes the entire double envelope GO:0033112, including
    the intermembrane space. Plastid-envelope is-a, cyanelle part-of and exact inner/outer/space
    has-part relations preserve the native scope. GO:0033113 is an unspecified individual
    envelope bilayer, not an interchangeable identity.
  evidence_ids:
  - record
  - root25-sources-cyanelle-envelope-go
  - root25-sources-SL-0479
- assessment_id: materials
  area: grounding
  topic: Material versus compartment identity and assembly essentiality
  outcome: supported
  target_ids:
  - GO:0033112
  summary: The lipid component rows identify actual constituent bilayers at exact
    GO membrane terms, rather than attaching a whole compartment identity to an arbitrary
    protein. The peptidoglycan sheet has biochemical support and an explicit reviewed-label-only
    grounding discussion; the entire intermembrane space is broader. UNKNOWN essentiality
    does not assert absence of function and correctly avoids treating occurrence,
    channel activity or peptidoglycan binding as an organelle-formation knockout.
    Exact molecular stoichiometry and complete membrane protein inventories are not
    claimed.
  evidence_ids:
  - record
  - policy
  - root25-sources-cyanelle-envelope-go
  - root25-sources-SL-0479
  - cyanelle-agent-pfanzagl1996-numeric
  - cyanelle-agent-kojima2016-numeric
  - root25-sources-pg-go-search
- assessment_id: taxa
  area: scope
  topic: Native taxa and experimental occurrence
  outcome: supported
  target_ids:
  - GO:0033112
  summary: ENA resolves species2762 Cyanophora paradoxa and class38254 Glaucocystophyceae,
    with glaucophyte alternative nomenclature. COMMON is used as qualitative characteristic
    occurrence, not a numerical census. The generic C. paradoxa canonical example
    is supported by the inspected Giddings microscopy source and separately by biochemical
    material studies. The cross-genus Pfanzagl abstract supports the named Glaucocystis,
    Cyanoptyche and Cyanophora context; no full-paper experimental details are inferred.
  evidence_ids:
  - record
  - root25-sources-NCBITaxon-2762
  - root25-sources-NCBITaxon-38254
  - root25-sources-doi-10.1104_pp.71.2.409
  - root25-sources-doi-10.1128_jb.178.2.332-339.1996
  - root25-sources-doi-10.1074_jbc.M116.746131
  - root25-sources-PMID-8955325
  - cyanelle-agent-giddings1983-page409
  - cyanelle-agent-giddings1983-page414
  - cyanelle-agent-giddings1983-page416
  - cyanelle-agent-giddings1983-page417
  - cyanelle-agent-pfanzagl1996-numeric
  - root25-sources-pfanzagl1996-taxa-pmc-numeric
- assessment_id: graph
  area: evidence
  topic: Claim-level topology and functional scope
  outcome: supported
  target_ids:
  - GO:0033112
  summary: Every six-edge envelope graph assertion was read. The explicitly NONMECHANISTIC
    graph preserves outer-facing versus stroma-facing membrane orientation, with the
    inner membrane bounding stroma and peptidoglycan residing in the intermembrane
    space. The envelope contains the intervening space; it is not equated to either
    individual bilayer. No unrepresented transport machinery is presented as an established
    mechanism.
  evidence_ids:
  - record
  - root25-sources-cyanelle-envelope-go
  - root25-sources-SL-0479
  - cyanelle-agent-pfanzagl1996-numeric
  - cyanelle-agent-kojima2016-numeric
  - root25-sources-pfanzagl1996-taxa-pmc-numeric
  - cyanelle-agent-giddings1983-page409
  - cyanelle-agent-giddings1983-page414
  - cyanelle-agent-giddings1983-page416
  - cyanelle-agent-giddings1983-page417
- assessment_id: source-scope
  area: evidence
  topic: Bibliographic and source-reading boundaries
  outcome: supported
  target_ids:
  - GO:0033112
  summary: Native DOI/PMID rows identify the cited works and full returned abstracts.
    Giddings scanned pages409,414,416,417 were visually read at the exact locators;
    the other pages are not attested by this reviewer. Kojima specified main-text
    sections and the cross-genus Pfanzagl complete abstract were inspected. Pfanzagl
    primary-structure support is abstract-level only. Existing evidence is paraphrased
    in notes; no verbatim snippet fidelity is claimed.
  evidence_ids:
  - record
  - root25-sources-doi-10.1104_pp.71.2.409
  - root25-sources-doi-10.1128_jb.178.2.332-339.1996
  - root25-sources-doi-10.1074_jbc.M116.746131
  - root25-sources-PMID-8955325
  - cyanelle-agent-pfanzagl1996-numeric
  - cyanelle-agent-kojima2016-numeric
  - root25-sources-pfanzagl1996-taxa-pmc-numeric
  - cyanelle-agent-giddings1983-page409
  - cyanelle-agent-giddings1983-page414
  - cyanelle-agent-giddings1983-page416
  - cyanelle-agent-giddings1983-page417
- assessment_id: coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - GO:0033112
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Additional exhaustive component inventories, numerical
    properties, images, traits and expanded mechanisms are optional. No verbatim quotation
    requires repair, and no status or history rewrite is proposed. This bounded review
    does not assert exhaustive literature completeness.
  evidence_ids:
  - record
  - policy
  - root25-sources-cyanelle-envelope-go
  - root25-sources-SL-0479
  - root25-sources-NCBITaxon-2762
  - root25-sources-NCBITaxon-38254
  - root25-sources-doi-10.1104_pp.71.2.409
  - root25-sources-doi-10.1128_jb.178.2.332-339.1996
  - root25-sources-doi-10.1074_jbc.M116.746131
  - root25-sources-PMID-8955325
  - cyanelle-agent-pfanzagl1996-numeric
  - cyanelle-agent-kojima2016-numeric
  - cyanelle-agent-giddings1983-page409
  - cyanelle-agent-giddings1983-page414
  - cyanelle-agent-giddings1983-page416
  - cyanelle-agent-giddings1983-page417
  - root25-sources-pfanzagl1996-taxa-pmc-numeric
  - root25-sources-pfanzagl1996-taxa-pdf-instance
  - root25-sources-pg-go-search
findings: []
actions: []
limitations:
- Pfanzagl1996 primary-structure evidence was inspected as the complete native abstract
  only; no full Methods/Results read is claimed. The cross-genus Pfanzagl1996 work
  is also abstract-only; full-text attempts returned unavailable or challenge responses.
- The reviewed-label-only peptidoglycan-sheet grounding remains open; the bounded
  authority search is not proof that no exact term exists anywhere.
- Qualitative COMMON occurrence is not a measured population prevalence. Constitutional
  membrane identity does not establish the necessity of each molecular constituent.
- Giddings direct source reading covers only scanned pages409,414,416,417 at the stated
  locators; historical terminology is not substituted for current native identities.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches
  and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization;
  identifier transport and label-adapter limits remain explicit.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized one review for every uncovered target, including
  a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
