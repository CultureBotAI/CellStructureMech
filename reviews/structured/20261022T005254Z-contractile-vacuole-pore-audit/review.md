# Organelle identity, composition and evidence review

- Review: 20261022T005254Z-contractile-vacuole-pore-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T11:11:14Z
- Finished UTC: 2026-10-22T00:52:54Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact pore identity, native type/parthood, qualified Tetrahymena review example and descriptive discharge graph are supported. No concrete curation finding was established; molecular composition and individual assembly requirements remain unresolved.

## Scope And Provenance

Entire single record with exact authority identities, declared source-reading scopes, protein checks where applicable and component/function/graph boundaries.

Selection: Target 5 in batch twenty-four; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031913 | data/structures/membrane_organelle/contractile_vacuole_pore.yaml | maintained | contractile vacuole pore |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0031913 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Native protein causal-graphs | passed | True | GO:0031913 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Focused native schema | passed | True | GO:0031913 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031913 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0031913 | 7 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0031913 | No expression-module or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | GO:0031913 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0031913 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031913 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031913 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031913 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0031913 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Stable pore with exact authority classification

identity: supported. Targets: GO:0031913.

The target is the stable discharge pore, not the collecting vacuole, its fluid lumen, the entire contractile-vacuole complex or a transient image of an aperture. Its MULTIPROTEIN_COMPLEX kind is supported by the current native plasma-membrane-protein-complex parent; this does not establish its molecular inventory.

### Membrane and cytoskeletal parthood

consistency: supported. Targets: GO:0031913.

The declared type parent and both part_of links are explicit native GO relationships. Frankel and the McKanna synopsis provide concordant diaphragm and microtubule context. The membrane and cytoskeletal affiliations refer to the composite stable pore apparatus and do not make the entire surrounding vacuole a protein complex.

### Qualified Tetrahymena review example

scope: supported. Targets: GO:0031913.

The exact native taxon is T. thermophila, and the canonical note explicitly describes the organism as the model covered by the review cited by GO. The review chapter and GO citation support that narrow statement. The target makes no quantitative prevalence claim or experimental-strain assertion. Paramecium remains structural source context rather than an invented species-level canonical example.

### Molecular composition deliberately unresolved

grounding: supported. Targets: GO:0031913.

The record asserts no component-level protein identities, exact families, protein examples or essentiality values. The open component-grounding TODO accurately preserves that uncertainty. Observable microtubular architecture supports structural affiliation without supplying a complete lineage-neutral molecular inventory; omission of an optional detailed inventory is not itself a defect.

### No unsupported molecular requirement

evidence: unknown. Targets: GO:0031913.

The primary synopsis and review passages describe anatomy and discharge. They do not test assembly requirements for individual proteins. No such necessity claim is made by the maintained target, and no inference from membrane opening or cytoskeletal association is added.

### Three explicitly descriptive pore relations

graph: supported. Targets: GO:0031913.

The NONMECHANISTIC graph has two source-backed parthood edges and one coarse liquid-flow regulation edge. These match native GO identity and the inspected structural/discharge descriptions. No force-generating, fusion, channel-gating or complete subunit mechanism is claimed. The label-only process node is appropriately narrow; it does not require a forced generic process mapping.

### Citation and access limits preserved

provenance: supported. Targets: GO:0031913.

Exact citation identities, native taxon/GO responses and original source URL/time/hash receipts are traceable. Frankel is read at named chapter passages; McKanna at its publisher-deposited synopsis and metadata only. No verbatim-snippet or image claim requires repair, and no historical curator search or authorship is recertified.

### Bounded record-level coverage

completeness: supported. Targets: GO:0031913.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Additional exhaustive component inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. This bounded review does not assert exhaustive literature completeness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/contractile_vacuole_pore.yaml; Entire maintained YAML including history, all evidence notes, components, functions, graph edges and discussions | context_only | All maintained fields were read. No scientific edit or mapping-status promotion is made. |
| policy | docs/CURATION.md; Exact identity, claim-level evidence, material versus localization grounding, and component assembly-essentiality contract | context_only | Family identity, concrete protein examples and structure membership are separate; activity and viability are not by themselves formation assays. Optional inventories are not mandatory. |
| boundary-contractile_vacuolar_membrane | data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml; Identifier, label, definition, parents, part_of, has_part and components only | context_only | Boundary fields distinguish the stable pore, bounding membrane, collecting vacuole and larger vacuole/spongiome complex. Neighboring records are not additional targets and their full scientific claims are not certified here. |
| boundary-contractile_vacuole | data/structures/membrane_organelle/contractile_vacuole.yaml; Identifier, label, definition, parents, part_of, has_part and components only | context_only | Boundary fields distinguish the stable pore, bounding membrane, collecting vacuole and larger vacuole/spongiome complex. Neighboring records are not additional targets and their full scientific claims are not certified here. |
| boundary-contractile_vacuole_complex | data/structures/membrane_organelle/contractile_vacuole_complex.yaml; Identifier, label, definition, parents, part_of, has_part and components only | context_only | Boundary fields distinguish the stable pore, bounding membrane, collecting vacuole and larger vacuole/spongiome complex. Neighboring records are not additional targets and their full scientific claims are not certified here. |
| root24-sources-pore-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0031164,GO:0031913,GO:0098797; Complete exact definitions/active status and relevant explicit child relations for GO0031913, GO0098797, GO0031164 and GO0005856 | supports | All four exact native GO terms are active. Their definitions match the target and named parents/parts; the plasma-membrane-protein-complex parent explicitly lists GO0031913 as is_a child, and contractile-vacuolar membrane and cytoskeleton explicitly list it as part_of child. The pore definition directly cites PMID10503189. |
| root24-sources-pore-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031913/ancestors?relations=is_a,part_of; Complete returned ancestry for GO0031913 | supports | The returned native is_a/part_of ancestry independently includes the maintained plasma-membrane protein complex parent and contractile-vacuolar membrane/cytoskeleton contexts. Type and physical parthood are not conflated. |
| root24-sources-NCBITaxon-5911 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Tetrahymena thermophila at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root24-sources-frankel2000-pmid | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:10503189%20AND%20SRC:MED; Complete citation, author, year, page and DOI/PMID fields; absence of abstractText in this response | supports | Native MED identifies Frankel, Cell biology of Tetrahymena thermophila, Methods in Cell Biology62:27–125, PMID10503189, exact DOI10.1016/s0091-679x(08)61528-9, year2000. It returns no abstract. This citation is explicitly the native GO definition source; readable body evidence is separately recorded. |
| root24-sources-frankel2000-quoteddoi | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI:%2210.1016/S0091-679X(08)61528-9%22; Complete single-result exact quoted DOI query | context_only | The quoted exact DOI query resolves the same PMID10503189 and citation. The prior unquoted DOI query returned zero results because query parsing matters; that zero result is not evidence the source is absent. |
| root24-sources-doi-10.1016_S0091-679X_08_61528-9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/S0091-679X%2808%2961528-9; Actual source-access response, not article content | context_only | The initial unquoted DOI query returned zero hits. The separately recorded quoted DOI and PMID requests resolve the source; no absence inference is made. |
| root24-sources-frankel2000-university-pdf | https://chemotaxis.semmelweis.hu/CHTXhpg/Bookshelf/Tetrahymena/Tetrahymena_thermophila_Methods_2000.pdf; Chapter title/author and contents on printedp27; complete II.F The Contractile-Vacuole System printedpp51–52; complete III.B.1.b Contractile Vacuole Pore and Cytoproct printedp56. The rest of the book/chapter, figure pixels and underlying experiments were not reanalysed. | supports | The university-hosted book contains the exact Frankel chapter. Its complete contractile-vacuole-system section distinguishes pores, collecting vacuole and surrounding spongiome, describes a pore diaphragm that opens during discharge, and places circular/radial microtubules around the pore. The dedicated cytoskeletal paragraph reinforces microtubule association. This is review-tier support, not an independently performed experiment or a universally conserved subunit inventory. Historical Tetrahymena pyriformis observations are identified as such in the review and are not silently assigned an experimental T. thermophila strain. |
| root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/j.1550-7408.1973.tb03587.x; Complete native bibliographic fields; no abstractText returned | supports | Native MED identifies McKanna1973, Fine structure of the contractile vacuole pore in Paramecium, PMID4357833, exact DOI, journal20(5):631–638. No abstract is present in this MED response. |
| root24-sources-mckanna1973-crossref | https://api.crossref.org/works/10.1111/j.1550-7408.1973.tb03587.x; Complete publisher-deposited abstract and exact DOI/title/journal/year fields in Crossref message | supports | The publisher-deposited complete synopsis describes the Paramecium pore diaphragm closing in diastole and parting during systole, membrane continuity and circular/radial microtubule systems. This supports the broad structural/discharge context. The synopsis does not identify an experimental Paramecium species/strain or isolate necessity of individual pore proteins. Crossref renders the author surname McKAN, while native MED identifies McKanna; no scientific identity mismatch is inferred from that metadata variation. |
| root24-sources-frankel2000-publisher | https://www.sciencedirect.com/science/chapter/abs/pii/S0091679X08615289; Actual source-access response, not article content | context_only | The ScienceDirect route returned403 and supplied no certified chapter body; a separately recorded university PDF supplied the stated passages. |
| root24-sources-frankel2000-api | https://api.elsevier.com/content/article/pii/S0091679X08615289?httpAccept=text/xml; Actual source-access response, not article content | context_only | The HTTP200 Elsevier API response contains bibliographic coredata only, not article text. Its coverDate1999-12-31 differs from native MED year2000; this is not treated as a different source. |
| root24-sources-mckanna1973-publisher | https://onlinelibrary.wiley.com/doi/10.1111/j.1550-7408.1973.tb03587.x; Actual source-access response, not article content | context_only | The native Wiley article route returned403 and no readable body. |
| root24-sources-mckanna1973-pdf | https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1550-7408.1973.tb03587.x; Actual source-access response, not article content | context_only | The Wiley PDF route returned403 and no readable PDF. |
| root24-sources-mckanna1973-tdm | https://api.wiley.com/onlinelibrary/tdm/v1/articles/10.1111%2Fj.1550-7408.1973.tb03587.x; Actual source-access response, not article content | context_only | The public TDM route returned400 with an empty body; no credentials, subscription access or full-text claim is inferred. |
| native-verify | /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml --verify; Exact focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml --causal-graphs; Exact focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/contractile_vacuole_pore.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/contractile_vacuole_pore.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/contractile_vacuole_pore.yaml --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_pore-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/contractile_vacuole_pore.yaml --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_pore-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch24-20261021-qayobm82/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_pore-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/contractile_vacuole_pore.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 7 of7 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Frankel was inspected only at chapter identity and the named complete pore/vacuole/cytoskeletal passages. The remaining chapter/book and figure pixels were not reviewed.
- McKanna1973 support is restricted to exact native bibliography and the complete publisher-deposited Crossref synopsis. Wiley body/PDF returned403 and TDM400; no full-paper or experimental-strain read is claimed.
- Boundary-only neighboring-record inspection does not review those records as additional targets. No exhaustive protein-family or ontology-absence claim is made.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization; identifier transport and label-adapter limits remain explicit.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for every uncovered target, including a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T005254Z-contractile-vacuole-pore-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Organelle identity, composition and evidence review
started_at: '2026-10-21T11:11:14Z'
finished_at: '2026-10-22T00:52:54Z'
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
summary: The exact pore identity, native type/parthood, qualified Tetrahymena review
  example and descriptive discharge graph are supported. No concrete curation finding
  was established; molecular composition and individual assembly requirements remain
  unresolved.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
    sha256: a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole.yaml
    sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole_complex.yaml
    sha256: 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    sha256: e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294
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
  - path: scripts/score_causal_graphs.py
    sha256: 5ffe450c5b37c3dc3b0e62672caf0d99b358c8249fcc98a8c4fc7d78e8cd0d2f
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0031913
  path: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
  label: contractile vacuole pore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    role: maintained scientific record
scope:
  description: Entire single record with exact authority identities, declared source-reading
    scopes, protein checks where applicable and component/function/graph boundaries.
  selection: Target 5 in batch twenty-four; exact sorted uncovered path at frozen
    fresh-main revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031913
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0031913
  command: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml
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
  - GO:0031913
  command: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml
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
  - GO:0031913
  command: just validate data/structures/membrane_organelle/contractile_vacuole_pore.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031913
  command: just validate-strict data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_pore-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0031913
  summary: 7 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0031913
  summary: No expression-module or transcriptomic inference is made by this structural
    review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0031913
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - boundary-contractile_vacuolar_membrane
  - boundary-contractile_vacuole
  - boundary-contractile_vacuole_complex
  - root24-sources-pore-go
  - root24-sources-pore-ancestors
  - root24-sources-NCBITaxon-5911
  - root24-sources-frankel2000-pmid
  - root24-sources-frankel2000-quoteddoi
  - root24-sources-doi-10.1016_S0091-679X_08_61528-9
  - root24-sources-frankel2000-university-pdf
  - root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  - root24-sources-mckanna1973-crossref
  - root24-sources-frankel2000-publisher
  - root24-sources-frankel2000-api
  - root24-sources-mckanna1973-publisher
  - root24-sources-mckanna1973-pdf
  - root24-sources-mckanna1973-tdm
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031913
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
  - GO:0031913
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
  - GO:0031913
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
  - GO:0031913
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
  - GO:0031913
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
  reference: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
  locator: Entire maintained YAML including history, all evidence notes, components,
    functions, graph edges and discussions
  accessed_at: '2026-10-21T11:15:23Z'
  support: context_only
  summary: All maintained fields were read. No scientific edit or mapping-status promotion
    is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, claim-level evidence, material versus localization grounding,
    and component assembly-essentiality contract
  accessed_at: '2026-10-21T11:15:23Z'
  support: context_only
  summary: Family identity, concrete protein examples and structure membership are
    separate; activity and viability are not by themselves formation assays. Optional
    inventories are not mandatory.
- evidence_id: boundary-contractile_vacuolar_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
  locator: Identifier, label, definition, parents, part_of, has_part and components
    only
  accessed_at: '2026-10-21T11:15:23Z'
  support: context_only
  summary: Boundary fields distinguish the stable pore, bounding membrane, collecting
    vacuole and larger vacuole/spongiome complex. Neighboring records are not additional
    targets and their full scientific claims are not certified here.
- evidence_id: boundary-contractile_vacuole
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole.yaml
  locator: Identifier, label, definition, parents, part_of, has_part and components
    only
  accessed_at: '2026-10-21T11:15:23Z'
  support: context_only
  summary: Boundary fields distinguish the stable pore, bounding membrane, collecting
    vacuole and larger vacuole/spongiome complex. Neighboring records are not additional
    targets and their full scientific claims are not certified here.
- evidence_id: boundary-contractile_vacuole_complex
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole_complex.yaml
  locator: Identifier, label, definition, parents, part_of, has_part and components
    only
  accessed_at: '2026-10-21T11:15:23Z'
  support: context_only
  summary: Boundary fields distinguish the stable pore, bounding membrane, collecting
    vacuole and larger vacuole/spongiome complex. Neighboring records are not additional
    targets and their full scientific claims are not certified here.
- evidence_id: root24-sources-pore-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0031164,GO:0031913,GO:0098797
  locator: Complete exact definitions/active status and relevant explicit child relations
    for GO0031913, GO0098797, GO0031164 and GO0005856
  accessed_at: '2026-10-21T11:12:42.299922Z'
  support: supports
  summary: All four exact native GO terms are active. Their definitions match the
    target and named parents/parts; the plasma-membrane-protein-complex parent explicitly
    lists GO0031913 as is_a child, and contractile-vacuolar membrane and cytoskeleton
    explicitly list it as part_of child. The pore definition directly cites PMID10503189.
  snapshot_sha256: d14b3bddf05a15bf4e17af18864ef860a59a9c2fcce46291f06f4ee3968fb30b
- evidence_id: root24-sources-pore-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031913/ancestors?relations=is_a,part_of
  locator: Complete returned ancestry for GO0031913
  accessed_at: '2026-10-21T11:13:00.840684Z'
  support: supports
  summary: The returned native is_a/part_of ancestry independently includes the maintained
    plasma-membrane protein complex parent and contractile-vacuolar membrane/cytoskeleton
    contexts. Type and physical parthood are not conflated.
  snapshot_sha256: 4a11f0c59e8fe1713f53f5ab5b209a6561842f348916b347ddea43698938070f
- evidence_id: root24-sources-NCBITaxon-5911
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T11:12:42.248736Z'
  support: supports
  summary: Native ENA taxonomy identifies Tetrahymena thermophila at species rank.
    Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: e848a1295088ad42e73c4c2c42d45869b4c9c2b10858e2c32086dc67b066a8c5
- evidence_id: root24-sources-frankel2000-pmid
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:10503189%20AND%20SRC:MED
  locator: Complete citation, author, year, page and DOI/PMID fields; absence of abstractText
    in this response
  accessed_at: '2026-10-21T11:13:49.219976Z'
  support: supports
  summary: Native MED identifies Frankel, Cell biology of Tetrahymena thermophila,
    Methods in Cell Biology62:27–125, PMID10503189, exact DOI10.1016/s0091-679x(08)61528-9,
    year2000. It returns no abstract. This citation is explicitly the native GO definition
    source; readable body evidence is separately recorded.
  snapshot_sha256: bbddf4df91f90d17e89a02811f28cfcfe6a92033c26e8e1b89d730bc86f186ee
- evidence_id: root24-sources-frankel2000-quoteddoi
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:%2210.1016/S0091-679X(08)61528-9%22
  locator: Complete single-result exact quoted DOI query
  accessed_at: '2026-10-21T11:13:49.362528Z'
  support: context_only
  summary: The quoted exact DOI query resolves the same PMID10503189 and citation.
    The prior unquoted DOI query returned zero results because query parsing matters;
    that zero result is not evidence the source is absent.
  snapshot_sha256: 06e947e1aa749fd3509fa037702470008c63acf2383d572a6d2da2e9ec77cdcf
- evidence_id: root24-sources-doi-10.1016_S0091-679X_08_61528-9
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/S0091-679X%2808%2961528-9
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T11:12:42.285045Z'
  support: context_only
  summary: The initial unquoted DOI query returned zero hits. The separately recorded
    quoted DOI and PMID requests resolve the source; no absence inference is made.
  snapshot_sha256: e386d67df522635be61ce827a274a5dcbc85954283a3b8da7c477edc5a485e40
- evidence_id: root24-sources-frankel2000-university-pdf
  kind: authority
  reference: https://chemotaxis.semmelweis.hu/CHTXhpg/Bookshelf/Tetrahymena/Tetrahymena_thermophila_Methods_2000.pdf
  locator: Chapter title/author and contents on printedp27; complete II.F The Contractile-Vacuole
    System printedpp51–52; complete III.B.1.b Contractile Vacuole Pore and Cytoproct
    printedp56. The rest of the book/chapter, figure pixels and underlying experiments
    were not reanalysed.
  accessed_at: '2026-10-21T11:13:51.637635Z'
  support: supports
  summary: The university-hosted book contains the exact Frankel chapter. Its complete
    contractile-vacuole-system section distinguishes pores, collecting vacuole and
    surrounding spongiome, describes a pore diaphragm that opens during discharge,
    and places circular/radial microtubules around the pore. The dedicated cytoskeletal
    paragraph reinforces microtubule association. This is review-tier support, not
    an independently performed experiment or a universally conserved subunit inventory.
    Historical Tetrahymena pyriformis observations are identified as such in the review
    and are not silently assigned an experimental T. thermophila strain.
  snapshot_sha256: 48598713aee2c6aabd3c6aaf8f3085f7fc12824dd5c9fa0592f71ccc9716c615
- evidence_id: root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/j.1550-7408.1973.tb03587.x
  locator: Complete native bibliographic fields; no abstractText returned
  accessed_at: '2026-10-21T11:12:42.295652Z'
  support: supports
  summary: Native MED identifies McKanna1973, Fine structure of the contractile vacuole
    pore in Paramecium, PMID4357833, exact DOI, journal20(5):631–638. No abstract
    is present in this MED response.
  snapshot_sha256: 83bffb09f8dcbe167c359d9d51c21c0bc5a3e1e2bace220af7898423cfef3c8c
- evidence_id: root24-sources-mckanna1973-crossref
  kind: database
  reference: https://api.crossref.org/works/10.1111/j.1550-7408.1973.tb03587.x
  locator: Complete publisher-deposited abstract and exact DOI/title/journal/year
    fields in Crossref message
  accessed_at: '2026-10-21T11:13:00.331239Z'
  support: supports
  summary: The publisher-deposited complete synopsis describes the Paramecium pore
    diaphragm closing in diastole and parting during systole, membrane continuity
    and circular/radial microtubule systems. This supports the broad structural/discharge
    context. The synopsis does not identify an experimental Paramecium species/strain
    or isolate necessity of individual pore proteins. Crossref renders the author
    surname McKAN, while native MED identifies McKanna; no scientific identity mismatch
    is inferred from that metadata variation.
  snapshot_sha256: 51856ef9e197e03ac04ff19bea4f69dcb5120796b7ae78b99d21969173378035
- evidence_id: root24-sources-frankel2000-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/chapter/abs/pii/S0091679X08615289
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T11:13:00.942874Z'
  support: context_only
  summary: The ScienceDirect route returned403 and supplied no certified chapter body;
    a separately recorded university PDF supplied the stated passages.
  snapshot_sha256: 8f5b11a54cb418c890998fe81090c1c62e6a8905c5889d1fa48ed0f98bba2465
- evidence_id: root24-sources-frankel2000-api
  kind: authority
  reference: https://api.elsevier.com/content/article/pii/S0091679X08615289?httpAccept=text/xml
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T11:13:00.738513Z'
  support: context_only
  summary: The HTTP200 Elsevier API response contains bibliographic coredata only,
    not article text. Its coverDate1999-12-31 differs from native MED year2000; this
    is not treated as a different source.
  snapshot_sha256: 5250385de297cf06660172d016d3d68e6cfaab2ec2061267016a220e066e38c4
- evidence_id: root24-sources-mckanna1973-publisher
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/10.1111/j.1550-7408.1973.tb03587.x
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T11:13:00.167033Z'
  support: context_only
  summary: The native Wiley article route returned403 and no readable body.
  snapshot_sha256: 278a4822e8e07fbe814f30784449e0c337f154660feffee0527779ec49bc06e9
- evidence_id: root24-sources-mckanna1973-pdf
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1550-7408.1973.tb03587.x
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T11:13:00.167511Z'
  support: context_only
  summary: The Wiley PDF route returned403 and no readable PDF.
  snapshot_sha256: 4158afe82b27e32dea5c9a0f6ac50a9b92787e99e2455874c43b3c54cec2dce2
- evidence_id: root24-sources-mckanna1973-tdm
  kind: authority
  reference: https://api.wiley.com/onlinelibrary/tdm/v1/articles/10.1111%2Fj.1550-7408.1973.tb03587.x
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T11:13:48.930334Z'
  support: context_only
  summary: The public TDM route returned400 with an empty body; no credentials, subscription
    access or full-text claim is inferred.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    --verify
  locator: Exact focused native output
  accessed_at: '2026-10-21T11:12:24.205546Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    --causal-graphs
  locator: Exact focused native output
  accessed_at: '2026-10-21T11:12:24.755392Z'
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
  reference: just validate data/structures/membrane_organelle/contractile_vacuole_pore.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:11:15Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/contractile_vacuole_pore.yaml'
  snapshot_sha256: 53e71f9bc886398ae4cde9ae2fb068f5f39044d73039b2bf0539b8c4ffa3639b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_pore-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:11:17Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/contractile_vacuole_pore.yaml\
    \ --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_pore-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch24-20261021-qayobm82/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_pore-strict.tsv"
  snapshot_sha256: d5390ef95466aa6d4fd86a25953e64ecbb8b22dc9f827295edd3ffae2b3bf72c
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/contractile_vacuole_pore.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T11:15:23Z'
  support: supports
  summary: '7 of7 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
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
  topic: Stable pore with exact authority classification
  outcome: supported
  target_ids:
  - GO:0031913
  summary: The target is the stable discharge pore, not the collecting vacuole, its
    fluid lumen, the entire contractile-vacuole complex or a transient image of an
    aperture. Its MULTIPROTEIN_COMPLEX kind is supported by the current native plasma-membrane-protein-complex
    parent; this does not establish its molecular inventory.
  evidence_ids:
  - record
  - policy
  - root24-sources-pore-go
  - root24-sources-pore-ancestors
  - root24-sources-NCBITaxon-5911
  - root24-sources-frankel2000-pmid
  - root24-sources-frankel2000-university-pdf
  - root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  - root24-sources-mckanna1973-crossref
- assessment_id: hierarchy
  area: consistency
  topic: Membrane and cytoskeletal parthood
  outcome: supported
  target_ids:
  - GO:0031913
  summary: The declared type parent and both part_of links are explicit native GO
    relationships. Frankel and the McKanna synopsis provide concordant diaphragm and
    microtubule context. The membrane and cytoskeletal affiliations refer to the composite
    stable pore apparatus and do not make the entire surrounding vacuole a protein
    complex.
  evidence_ids:
  - record
  - policy
  - root24-sources-pore-go
  - root24-sources-pore-ancestors
  - root24-sources-NCBITaxon-5911
  - root24-sources-frankel2000-pmid
  - root24-sources-frankel2000-university-pdf
  - root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  - root24-sources-mckanna1973-crossref
- assessment_id: example
  area: scope
  topic: Qualified Tetrahymena review example
  outcome: supported
  target_ids:
  - GO:0031913
  summary: The exact native taxon is T. thermophila, and the canonical note explicitly
    describes the organism as the model covered by the review cited by GO. The review
    chapter and GO citation support that narrow statement. The target makes no quantitative
    prevalence claim or experimental-strain assertion. Paramecium remains structural
    source context rather than an invented species-level canonical example.
  evidence_ids:
  - record
  - policy
  - root24-sources-pore-go
  - root24-sources-pore-ancestors
  - root24-sources-NCBITaxon-5911
  - root24-sources-frankel2000-pmid
  - root24-sources-frankel2000-university-pdf
  - root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  - root24-sources-mckanna1973-crossref
- assessment_id: composition
  area: grounding
  topic: Molecular composition deliberately unresolved
  outcome: supported
  target_ids:
  - GO:0031913
  summary: The record asserts no component-level protein identities, exact families,
    protein examples or essentiality values. The open component-grounding TODO accurately
    preserves that uncertainty. Observable microtubular architecture supports structural
    affiliation without supplying a complete lineage-neutral molecular inventory;
    omission of an optional detailed inventory is not itself a defect.
  evidence_ids:
  - record
  - policy
  - root24-sources-pore-go
  - root24-sources-pore-ancestors
  - root24-sources-NCBITaxon-5911
  - root24-sources-frankel2000-pmid
  - root24-sources-frankel2000-university-pdf
  - root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  - root24-sources-mckanna1973-crossref
- assessment_id: formation
  area: evidence
  topic: No unsupported molecular requirement
  outcome: unknown
  target_ids:
  - GO:0031913
  summary: The primary synopsis and review passages describe anatomy and discharge.
    They do not test assembly requirements for individual proteins. No such necessity
    claim is made by the maintained target, and no inference from membrane opening
    or cytoskeletal association is added.
  evidence_ids:
  - record
  - policy
  - root24-sources-pore-go
  - root24-sources-pore-ancestors
  - root24-sources-NCBITaxon-5911
  - root24-sources-frankel2000-pmid
  - root24-sources-frankel2000-university-pdf
  - root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  - root24-sources-mckanna1973-crossref
- assessment_id: graph
  area: graph
  topic: Three explicitly descriptive pore relations
  outcome: supported
  target_ids:
  - GO:0031913
  summary: The NONMECHANISTIC graph has two source-backed parthood edges and one coarse
    liquid-flow regulation edge. These match native GO identity and the inspected
    structural/discharge descriptions. No force-generating, fusion, channel-gating
    or complete subunit mechanism is claimed. The label-only process node is appropriately
    narrow; it does not require a forced generic process mapping.
  evidence_ids:
  - record
  - policy
  - root24-sources-pore-go
  - root24-sources-pore-ancestors
  - root24-sources-NCBITaxon-5911
  - root24-sources-frankel2000-pmid
  - root24-sources-frankel2000-university-pdf
  - root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  - root24-sources-mckanna1973-crossref
- assessment_id: provenance
  area: provenance
  topic: Citation and access limits preserved
  outcome: supported
  target_ids:
  - GO:0031913
  summary: Exact citation identities, native taxon/GO responses and original source
    URL/time/hash receipts are traceable. Frankel is read at named chapter passages;
    McKanna at its publisher-deposited synopsis and metadata only. No verbatim-snippet
    or image claim requires repair, and no historical curator search or authorship
    is recertified.
  evidence_ids:
  - record
  - policy
  - root24-sources-pore-go
  - root24-sources-pore-ancestors
  - root24-sources-NCBITaxon-5911
  - root24-sources-frankel2000-pmid
  - root24-sources-frankel2000-university-pdf
  - root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  - root24-sources-mckanna1973-crossref
- assessment_id: coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - GO:0031913
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Additional exhaustive component inventories, numerical
    properties, images, traits and expanded mechanisms are optional. No verbatim quotation
    requires repair, and no status or history rewrite is proposed. This bounded review
    does not assert exhaustive literature completeness.
  evidence_ids:
  - record
  - policy
  - boundary-contractile_vacuolar_membrane
  - boundary-contractile_vacuole
  - boundary-contractile_vacuole_complex
  - root24-sources-pore-go
  - root24-sources-pore-ancestors
  - root24-sources-NCBITaxon-5911
  - root24-sources-frankel2000-pmid
  - root24-sources-frankel2000-quoteddoi
  - root24-sources-doi-10.1016_S0091-679X_08_61528-9
  - root24-sources-frankel2000-university-pdf
  - root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  - root24-sources-mckanna1973-crossref
  - root24-sources-frankel2000-publisher
  - root24-sources-frankel2000-api
  - root24-sources-mckanna1973-publisher
  - root24-sources-mckanna1973-pdf
  - root24-sources-mckanna1973-tdm
findings: []
actions: []
limitations:
- Frankel was inspected only at chapter identity and the named complete pore/vacuole/cytoskeletal
  passages. The remaining chapter/book and figure pixels were not reviewed.
- McKanna1973 support is restricted to exact native bibliography and the complete
  publisher-deposited Crossref synopsis. Wiley body/PDF returned403 and TDM400; no
  full-paper or experimental-strain read is claimed.
- Boundary-only neighboring-record inspection does not review those records as additional
  targets. No exhaustive protein-family or ontology-absence claim is made.
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
