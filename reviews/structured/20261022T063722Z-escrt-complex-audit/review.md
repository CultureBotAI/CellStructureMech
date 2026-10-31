# Source-backed review of escrt complex

- Review: 20261022T063722Z-escrt-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:16:16Z
- Finished UTC: 2026-10-22T06:37:22Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: exact generic ESCRT identity, distinct child classes, endosomal sorting scope and descriptive graph are supported. Detailed Henne body claims, child-specific assembly necessity and quantitative prevalence remain bounded.

## Scope And Provenance

Exactly one complete maintained target plus frozen governing/schema/protein/graph guidance. Native identity and directly read literature tiers are distinguished; no neighboring maintained record is an unstated scientific premise.

Selection: Batch54 strict ordered selection, index 6; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0036452 | data/structures/other/escrt_complex.yaml | maintained | ESCRT complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0036452 | Focused validator passed. |
| Focused native strict | passed | True | GO:0036452 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0036452 | Focused check passed; scientific scope independently assessed. |
| Focused native verify | passed | True | GO:0036452 | Focused check passed; scientific scope independently assessed. |
| Claim-level scientific review | passed | True | GO:0036452 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0036452 | 11 of 11 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0036452 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0036452 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0036452 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0036452 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0036452 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Generic ESCRT class rather than one combined supercomplex

identity: supported. Targets: GO:0036452.

Native GO confirms the identity, synonym, broad complex parent, endosome relation and five distinct child classes. The record does not combine all child subunits into one fixed-stoichiometry molecular assembly.

### Deliberately deferred child-specific composition

completeness: supported. Targets: GO:0036452.

The resolved boundary discussion appropriately keeps distinct ESCRT0/I/II/III/IV inventories on their child identities. An empty parent component table is not itself an omission. The historical future-record wording is not assessed as a current corpus-absence assertion.

### Coarse MVB-sorting function

evidence: supported. Targets: GO:0036452.

GO and the complete secondary abstract support cargo recognition and membrane remodeling in MVB biogenesis. The yeast primary sections corroborate the stated recruitment context without certifying unread detailed Henne prose or a universal pathway order in every process.

### Yeast example and general cellular scope

scope: supported. Targets: GO:0036452.

S.cerevisiae is a supported model for the endosomal sorting account. COMMON retains present-in-most-members meaning with exceptional losses, while the inspected literature provides qualitative support rather than a census. The broad definition lists additional process contexts without exporting every yeast-specific mechanism to them.

### Seven explicit class/topology/pathway relations

graph: supported. Targets: GO:0036452.

Five is_a edges match the native children; the endosome edge is corroborated by the typed part_of child response, and pathway participation is supported. ESCRT-IV wording matches its native Vps4/Vta1 definition. NONMECHANISTIC correctly limits this descriptive graph rather than asserting a full causal handoff sequence.

### No generic constituent formation claims

evidence: unknown. Targets: GO:0036452.

No constituent or essentiality inventory is asserted at this generic parent level. Child-specific assembly necessity and quantitative stoichiometry are not established here.

### Whole target with bounded source and unresolved scope

completeness: supported. Targets: GO:0036452.

All current scientific fields, source placements, graph edges, discussions and history were reviewed. Historical first-pass wording is not treated as false merely because present access differs. The stated findings isolate concrete current changes; optional unverified detail remains a limitation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/escrt_complex.yaml; Complete current YAML: every scientific field, citation, component/example, graph edge, discussion and history | context_only | The entire target was read. No neighboring maintained record supplies an unstated scientific premise. |
| curation | docs/CURATION.md; Component-class grounding, label-only representation and formation necessity | context_only | Known named constituents can be recorded with reviewed label-only grounding when exact families remain unresolved. Protein examples are not family identities; formation necessity is distinct from activity or viability. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentGroundingStatusEnum; EssentialityEnum; PresenceEnum | context_only | COMMON means present in most taxon members, with exceptional losses; UNKNOWN does not claim demonstrated formation necessity. An exact source-neutral class is distinct from a species accession or a shared domain. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope, typed nodes and source-specific edges | context_only | Descriptive composition/function graphs may remain NONMECHANISTIC. Experimental system and actor scope must match each edge. |
| micro54-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Native taxId/scientificName/rank and lineage fields. | supports | ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. This identity does not establish a quantitative within-species prevalence census. |
| micro54-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813,GO:0000814,GO:0000815,GO:0005768,GO:0010008,GO:0016887,GO:0032991,GO:0033565,GO:0036452,GO:0070676,GO:0071985,GO:0090148,GO:1990621; Shared native response: complete exact generic/child/boundary/function definitions and relevant typed children. Unrelated generic-complex children are not used. | supports | Active GO0036452 matches the generic definition and exact synonym. Its five is_a children are ESCRT-0/I/II/III/IV; GO0032991 lists the generic complex as an is_a child and GO0005768 lists it as part_of. Individual child definitions retain distinct cargo/recruitment/scission/Vps4-Vta1 scopes; GO0071985 is the declared pathway. |
| micro54-GO0036452-ancestors-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036452/ancestors?relations=is_a; Complete is_a-only ancestors array. | supports | The relations=is_a array confirms protein-containing-complex ancestry. It does not contain an endosomal-location relation; the latter is checked in the separate typed child response. |
| micro54-doi-j_devcel_2011_05_015 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2011.05.015%22&amp;format=json&amp;resultType=core; Unique native MED entry: exact title/authors/year/DOI/PMID and complete abstractText. | supports | Henne/Buchkovich/Emr2011 The ESCRT pathway, PMID21763610 DOI10.1016/j.devcel.2011.05.015, is a secondary review. Its complete abstract supports MVB biogenesis, cargo recognition, membrane sculpting, retroviral budding and abscission; it does not provide a separately read full subunit-by-subunit review body. |
| micro54-katzmann2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/; Genuine primary HTML, independently read sec3–6, Discussion sec9/sec10, Methods sec12–15 and embedded Figure1–4/7 captions. No pixels or unlisted Results sections. | supports | The yeast primary study supplies supplementary direct context for the coarse endosomal sorting account: Vps27 recruits ESCRT-I, which associates on membranes; downstream III and Vps4 roles are discussed separately. This is not presented as the main body of the cited Henne review. |
| micro54-henne2011-citeseer | https://citeseerx.ist.psu.edu/document?doi=d6f560e1a8e89ec5986bbcb4e2235d99c24bc8f4&amp;repid=rep1&amp;type=pdf; Original request and response diagnostic; not a main body. | context_only | The candidate public Henne PDF route returned HTTP404 HTML. The actual review reading remains limited to the complete native abstract. |
| schema-result | just validate data/structures/other/escrt_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/escrt_complex.yaml |
| strict-result | just validate-strict data/structures/other/escrt_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/escrt_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/escrt_complex.yaml --causal-graphs; Complete focused native read-only report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/escrt_complex.yaml --verify; Complete focused native read-only report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/escrt_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 11 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Henne2011 was independently inspected only through its complete native secondary-review abstract; the candidate PDF request returned404. Detailed review body prose, figures and methods are not certified.
- Katzmann primary sections provide supplementary yeast context at the exact declared scope, not a substitute attribution to Henne. No figure pixels or full modern ESCRT pathway reanalysis is claimed.
- The ontology child classes have different compositions and assembly boundaries. No parent-wide fixed stoichiometry, full subunit inventory or quantitative prevalence census is inferred.
- Original raw bytes, URL, UTC and SHA256 are retained for reused sources. Failed initial DNS fetches are diagnostic receipts, not scientific source bodies.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user requests a review for every unreviewed record, including qualified clean records.
- Native ontology and protein/family databases directly address these claims. No expression-module dataset is established as evidence of physical complex membership.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T063722Z-escrt-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of escrt complex
started_at: '2026-10-22T06:16:16Z'
finished_at: '2026-10-22T06:37:22Z'
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
summary: 'Qualified pass: exact generic ESCRT identity, distinct child classes, endosomal
  sorting scope and descriptive graph are supported. Detailed Henne body claims, child-specific
  assembly necessity and quantitative prevalence remain bounded.'
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
  - path: data/structures/other/escrt_complex.yaml
    sha256: 355f25710a97cee7e56f5b1438b71d21194f6130f84904091250df6e695bd17e
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
- target_id: GO:0036452
  path: data/structures/other/escrt_complex.yaml
  label: ESCRT complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target plus frozen governing/schema/protein/graph
    guidance. Native identity and directly read literature tiers are distinguished;
    no neighboring maintained record is an unstated scientific premise.
  selection: Batch54 strict ordered selection, index 6; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0036452
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: just validate data/structures/other/escrt_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: just validate-strict data/structures/other/escrt_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific scope independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; scientific scope independently assessed.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0036452
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro54-tax4932
  - micro54-go
  - micro54-GO0036452-ancestors-network
  - micro54-doi-j_devcel_2011_05_015
  - micro54-katzmann2003-pmc
  - micro54-henne2011-citeseer
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0036452
  summary: 11 of 11 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0036452
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
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/escrt_complex.yaml
  locator: 'Complete current YAML: every scientific field, citation, component/example,
    graph edge, discussion and history'
  accessed_at: '2026-10-22T06:30:28Z'
  support: context_only
  summary: The entire target was read. No neighboring maintained record supplies an
    unstated scientific premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component-class grounding, label-only representation and formation necessity
  accessed_at: '2026-10-22T06:30:28Z'
  support: context_only
  summary: Known named constituents can be recorded with reviewed label-only grounding
    when exact families remain unresolved. Protein examples are not family identities;
    formation necessity is distinct from activity or viability.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentGroundingStatusEnum; EssentialityEnum; PresenceEnum
  accessed_at: '2026-10-22T06:30:28Z'
  support: context_only
  summary: COMMON means present in most taxon members, with exceptional losses; UNKNOWN
    does not claim demonstrated formation necessity. An exact source-neutral class
    is distinct from a species accession or a shared domain.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope, typed nodes and source-specific edges
  accessed_at: '2026-10-22T06:30:28Z'
  support: context_only
  summary: Descriptive composition/function graphs may remain NONMECHANISTIC. Experimental
    system and actor scope must match each edge.
- evidence_id: micro54-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Native taxId/scientificName/rank and lineage fields.
  accessed_at: '2026-10-22T06:20:02.063372Z'
  support: supports
  summary: ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. This identity
    does not establish a quantitative within-species prevalence census.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro54-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813,GO:0000814,GO:0000815,GO:0005768,GO:0010008,GO:0016887,GO:0032991,GO:0033565,GO:0036452,GO:0070676,GO:0071985,GO:0090148,GO:1990621
  locator: 'Shared native response: complete exact generic/child/boundary/function
    definitions and relevant typed children. Unrelated generic-complex children are
    not used.'
  accessed_at: '2026-10-22T06:20:02.063646Z'
  support: supports
  summary: Active GO0036452 matches the generic definition and exact synonym. Its
    five is_a children are ESCRT-0/I/II/III/IV; GO0032991 lists the generic complex
    as an is_a child and GO0005768 lists it as part_of. Individual child definitions
    retain distinct cargo/recruitment/scission/Vps4-Vta1 scopes; GO0071985 is the
    declared pathway.
  snapshot_sha256: 563ffa6dea1c58c1c92024214051980b0b5f3eefd7984f1ef56cb02432f9999b
- evidence_id: micro54-GO0036452-ancestors-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036452/ancestors?relations=is_a
  locator: Complete is_a-only ancestors array.
  accessed_at: '2026-10-22T06:23:18.294329Z'
  support: supports
  summary: The relations=is_a array confirms protein-containing-complex ancestry.
    It does not contain an endosomal-location relation; the latter is checked in the
    separate typed child response.
  snapshot_sha256: 670982463b4374a0bbf92d464fc2199259f236006ccaec317228e17444f294c5
- evidence_id: micro54-doi-j_devcel_2011_05_015
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2011.05.015%22&format=json&resultType=core
  locator: 'Unique native MED entry: exact title/authors/year/DOI/PMID and complete
    abstractText.'
  accessed_at: '2026-10-22T06:20:10.119810Z'
  support: supports
  summary: Henne/Buchkovich/Emr2011 The ESCRT pathway, PMID21763610 DOI10.1016/j.devcel.2011.05.015,
    is a secondary review. Its complete abstract supports MVB biogenesis, cargo recognition,
    membrane sculpting, retroviral budding and abscission; it does not provide a separately
    read full subunit-by-subunit review body.
  snapshot_sha256: c1eb20e3ee3b89412437434900f82d42282d787ea5e51ef2d765091fa59227b0
- evidence_id: micro54-katzmann2003-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/
  locator: Genuine primary HTML, independently read sec3–6, Discussion sec9/sec10,
    Methods sec12–15 and embedded Figure1–4/7 captions. No pixels or unlisted Results
    sections.
  accessed_at: '2026-10-22T01:12:25.464014Z'
  support: supports
  summary: 'The yeast primary study supplies supplementary direct context for the
    coarse endosomal sorting account: Vps27 recruits ESCRT-I, which associates on
    membranes; downstream III and Vps4 roles are discussed separately. This is not
    presented as the main body of the cited Henne review.'
  snapshot_sha256: d4bc3fc8fd5cbf98c1b88722373dbd34c271f2df8da4bbb78d4f808dc7197233
- evidence_id: micro54-henne2011-citeseer
  kind: authority
  reference: https://citeseerx.ist.psu.edu/document?doi=d6f560e1a8e89ec5986bbcb4e2235d99c24bc8f4&repid=rep1&type=pdf
  locator: Original request and response diagnostic; not a main body.
  accessed_at: '2026-10-22T06:27:03.280566Z'
  support: context_only
  summary: The candidate public Henne PDF route returned HTTP404 HTML. The actual
    review reading remains limited to the complete native abstract.
  snapshot_sha256: 687dd819f7af05e60aee60b6885521ddf2373a3eebf141975e936763a929a0bd
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/escrt_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:16:17Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/escrt_complex.yaml'
  snapshot_sha256: 81fbb318e12c8adaa25eee0a2dad2bfeb4591924c7bf8946ed6a85482d39448e
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/escrt_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:16:18Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/escrt_complex.yaml\
    \ --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_complex-strict.tsv"
  snapshot_sha256: bc906370d3da6c39bbf646388d322e8d5033111c9166e3c562466658678dd825
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_complex.yaml
    --causal-graphs
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T06:23:33.384095Z'
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
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_complex.yaml
    --verify
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T06:23:33.867080Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/escrt_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 11 of 11 collected target identifiers returned OK. No residuals. Native
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
- assessment_id: identity
  area: identity
  topic: Generic ESCRT class rather than one combined supercomplex
  outcome: supported
  target_ids:
  - GO:0036452
  summary: Native GO confirms the identity, synonym, broad complex parent, endosome
    relation and five distinct child classes. The record does not combine all child
    subunits into one fixed-stoichiometry molecular assembly.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-go
  - micro54-GO0036452-ancestors-network
  - micro54-doi-j_devcel_2011_05_015
- assessment_id: composition
  area: completeness
  topic: Deliberately deferred child-specific composition
  outcome: supported
  target_ids:
  - GO:0036452
  summary: The resolved boundary discussion appropriately keeps distinct ESCRT0/I/II/III/IV
    inventories on their child identities. An empty parent component table is not
    itself an omission. The historical future-record wording is not assessed as a
    current corpus-absence assertion.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-go
  - micro54-GO0036452-ancestors-network
  - micro54-doi-j_devcel_2011_05_015
- assessment_id: function
  area: evidence
  topic: Coarse MVB-sorting function
  outcome: supported
  target_ids:
  - GO:0036452
  summary: GO and the complete secondary abstract support cargo recognition and membrane
    remodeling in MVB biogenesis. The yeast primary sections corroborate the stated
    recruitment context without certifying unread detailed Henne prose or a universal
    pathway order in every process.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-go
  - micro54-GO0036452-ancestors-network
  - micro54-doi-j_devcel_2011_05_015
  - micro54-katzmann2003-pmc
- assessment_id: scope
  area: scope
  topic: Yeast example and general cellular scope
  outcome: supported
  target_ids:
  - GO:0036452
  summary: S.cerevisiae is a supported model for the endosomal sorting account. COMMON
    retains present-in-most-members meaning with exceptional losses, while the inspected
    literature provides qualitative support rather than a census. The broad definition
    lists additional process contexts without exporting every yeast-specific mechanism
    to them.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-go
  - micro54-GO0036452-ancestors-network
  - micro54-doi-j_devcel_2011_05_015
  - micro54-katzmann2003-pmc
- assessment_id: graph
  area: graph
  topic: Seven explicit class/topology/pathway relations
  outcome: supported
  target_ids:
  - GO:0036452
  summary: Five is_a edges match the native children; the endosome edge is corroborated
    by the typed part_of child response, and pathway participation is supported. ESCRT-IV
    wording matches its native Vps4/Vta1 definition. NONMECHANISTIC correctly limits
    this descriptive graph rather than asserting a full causal handoff sequence.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-go
  - micro54-GO0036452-ancestors-network
  - graphs
  - micro54-doi-j_devcel_2011_05_015
  - micro54-katzmann2003-pmc
- assessment_id: formation
  area: evidence
  topic: No generic constituent formation claims
  outcome: unknown
  target_ids:
  - GO:0036452
  summary: No constituent or essentiality inventory is asserted at this generic parent
    level. Child-specific assembly necessity and quantitative stoichiometry are not
    established here.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-go
  - micro54-GO0036452-ancestors-network
- assessment_id: coverage
  area: completeness
  topic: Whole target with bounded source and unresolved scope
  outcome: supported
  target_ids:
  - GO:0036452
  summary: All current scientific fields, source placements, graph edges, discussions
    and history were reviewed. Historical first-pass wording is not treated as false
    merely because present access differs. The stated findings isolate concrete current
    changes; optional unverified detail remains a limitation.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-go
  - micro54-GO0036452-ancestors-network
  - micro54-doi-j_devcel_2011_05_015
  - micro54-katzmann2003-pmc
findings: []
actions: []
limitations:
- Henne2011 was independently inspected only through its complete native secondary-review
  abstract; the candidate PDF request returned404. Detailed review body prose, figures
  and methods are not certified.
- Katzmann primary sections provide supplementary yeast context at the exact declared
  scope, not a substitute attribution to Henne. No figure pixels or full modern ESCRT
  pathway reanalysis is claimed.
- The ontology child classes have different compositions and assembly boundaries.
  No parent-wide fixed stoichiometry, full subunit inventory or quantitative prevalence
  census is inferred.
- Original raw bytes, URL, UTC and SHA256 are retained for reused sources. Failed
  initial DNS fetches are diagnostic receipts, not scientific source bodies.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user requests a review for every unreviewed record, including qualified clean
  records.
- Native ontology and protein/family databases directly address these claims. No expression-module
  dataset is established as evidence of physical complex membership.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
