# AP-4 adaptor complex scientific review

- Review: 20261022T043543Z-ap-4-adaptor-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:15:22Z
- Finished UTC: 2026-10-22T04:35:43Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One bounded minor grounding finding for verified AP-4 subtype-specific subunit families. Exact complex identity, stated function and NONMECHANISTIC graph are supported within the declared experimental scope.

## Scope And Provenance

Exactly one complete AP-4 record with frozen guidance/schema, exact native identities, all maintained component/example/function/graph/evidence claims and source sections listed in evidence. No uninspected figure pixels, supplementary experiments or universal taxon inventory are claimed.

Selection: Batch44 strict path-ordered target 10; all initial native inspection/schema/strict gates passed at unchanged f97b before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030124 | data/structures/other/ap_4_adaptor_complex.yaml | maintained | AP-4 adaptor complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030124 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030124 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0030124 | Native diagnostic passed; claim-level science and optional coverage are assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0030124 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0030124 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030124 | 3 of 3 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030124 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030124 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030124 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030124 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030124 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Discovery contexts without an invented microbial example

scope: supported. Targets: GO:0030124.

The record has no taxonomic-distribution or canonical-example assertion. Pig-brain biochemical material, human beta4 expressed in Rat1 cells and yeast two-hybrid hosts are distinct experimental contexts. A yeast assay host is not evidence that budding yeast has a native AP4 complex.

### Cautious sorting implication and clathrin boundary

graph: supported. Targets: GO:0030124.

The four subunit and TGN-association edges are supported at their stated scope. The final is implicated in edge preserves the inferential step from a specific tyrosine-dependent CD63-tail interaction to cargo sorting. The graph does not assert a resolved trafficking destination, physiological flux or a universal clathrin coat, and its NONMECHANISTIC scope fits the evidence.

### Exact AP-4 heterotetramer and containing-structure boundaries

identity: supported. Targets: GO:0030124.

The maintained definition, ontology identity, parentage, subtype-specific core classes and any coat parthood match the native GO authority. Different AP subtypes and containing coats remain distinct; no identity remapping is warranted.

### Exact subtype families versus deferred broader candidates

grounding: concern. Targets: GO:0030124.

Native family entries support ap4_epsilon_subunit → InterPro:IPR017109. These are complete subtype-specific family classes, not merely domains or species-specific proteins, so their current REVIEWED_LABEL_ONLY status is not justified by saying no CURIE was curated in a prior pass. The other broader candidates do not close every remaining subunit class. Biological membership and identity remain supported.

### Constituent identity separated from assembly necessity

evidence: unknown. Targets: GO:0030124.

All four components use UNKNOWN essentiality. The evidence supports the four named constituent classes; transport phenotypes, viability outcomes, interaction assays and reconstituted activity do not independently establish universal formation necessity for every subunit. UNKNOWN is retained rather than replaced by an inferred requirement.

### All maintained fields and bounded source availability

completeness: supported. Targets: GO:0030124.

All target fields and explicit evidence placements were inspected. The four core components are represented. Missing additional taxa, isoforms or exhaustive accessory-protein inventories are not treated as defects; exact-family findings are limited to independently verified matches and the explicit label-only contract.

## Findings

### F1: Ground the verified AP-4 subtype-specific subunit families

minor / open / confirmed; issue key: ap4-verified-subtype-families-label-only.

Exact native InterPro family identities are available for ap4_epsilon_subunit → InterPro:IPR017109. The affected components nevertheless carry REVIEWED_LABEL_ONLY and notes saying no exact CURIE was curated in the prior pass. CURATION and schema define this status as no exact assertable family, not deferred curation. The native family types/descriptions match the component classes; other unresolved broad families and domains are not promoted.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, add the verified mappings ap4_epsilon_subunit → InterPro:IPR017109; remove the obsolete reviewed-label-only status/notes on those mapped rows and narrow the existing TODO to unresolved classes. Preserve the exact complex, roles, examples and UNKNOWN formation necessity; do not force broad beta/mu/sigma or domain entries onto other subtype classes.

- Each added CURIE resolves to the stated native subtype-specific family, with current identifier/label correspondence.
- Only the verified classes lose reviewed-label-only status; genuinely unresolved classes and their bounded TODO remain.
- Focused schema/strict, protein/graph diagnostics and source-placement checks pass after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/ap_4_adaptor_complex.yaml; Entire maintained target, including all history, components, examples, evidence, functions, graph and discussions | context_only | Complete target read. Historical actions are provenance rather than independent experimental support. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent grounding/status and essentiality; graph and protein-example contracts | context_only | A reviewed label-only component means no exact family can be asserted; membership and biological activity do not establish individual assembly necessity. |
| curation | docs/CURATION.md; Grounding and REVIEWED_LABEL_ONLY rules, lines150–162 | context_only | The status represents a checked absence of an exact assertable term, not merely an identifier that was not curated in a prior pass. |
| ap44-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030121,GO:0030122,GO:0030123,GO:0030124,GO:0030119,GO:0030131,GO:0098797,GO:0030130,GO:0030128,GO:0030132,GO:0072583; All eleven returned IDs/names/active states/definitions/synonyms and the typed child entries corresponding to maintained parent/parthood links | supports | The eleven native terms exactly identify AP1–AP4, their named subunits and isoform qualifiers, AP-type/clathrin-adaptor parents, AP2 plasma-membrane-complex parent, AP1/AP2 typed coat parthood, and clathrin-dependent endocytosis. The AP3/AP4 definitions retain qualified clathrin association. Typed links were read from the exact parent children; unrelated children are not an exhaustive review scope. |
| ap44-agent-family-search-AP4 | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-4&amp;page_size=100; Complete returned candidate accession/name/type list and pagination | context_only | Bounded native InterPro search for AP-4 returned 10 entries with no next page. Names/types identify candidate adaptor families, alongside unrelated text matches and domains; exact candidate entries are verified separately. This is not an exhaustive search of all protein-family resources. |
| ap44-agent-ipr-IPR017109 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017109/; Complete accession/name/type, description and LLM flags, integrated member signatures and hierarchy | supports | IPR017109 is type family, named Adaptor protein complex AP-4, epsilon subunit. Its complete native description and integrated signatures were read to distinguish the named subunit class from broader adaptor families or partial domains. |
| ap44-agent-ipr-IPR016342 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016342/; Complete accession/name/type, description and LLM flags, integrated member signatures and hierarchy | supports | IPR016342 is type family, named AP-1/2/4 complex subunit beta. Its complete native description and integrated signatures were read to distinguish the named subunit class from broader adaptor families or partial domains. |
| ap44-agent-ipr-IPR001392 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001392/; Complete accession/name/type, description and LLM flags, integrated member signatures and hierarchy | supports | IPR001392 is type family, named Clathrin adaptor, mu subunit. Its complete native description and integrated signatures were read to distinguish the named subunit class from broader adaptor families or partial domains. |
| ap44-agent-ipr-IPR016635 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016635/; Complete accession/name/type, description and LLM flags, integrated member signatures and hierarchy | supports | IPR016635 is type family, named Adaptor protein complex, sigma subunit. Its complete native description and integrated signatures were read to distinguish the named subunit class from broader adaptor families or partial domains. |
| ap44-agent-hirst1999-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.10.8.2787&amp;format=json&amp;resultType=core; Unique Europe PMC MED bibliographic record: exact DOI/PMID/PMC if returned, authors/title/year and complete abstract | supports | Hirst, Bright, Rous and Robinson1999, DOI10.1091/mbc.10.8.2787/PMID10436028/PMC25515. Coimmunoprecipitation/two-hybrid evidence supports a four-subunit complex; sparse near-TGN localization and a tyrosine-dependent signal interaction suggest a sorting role. |
| ap44-agent-hirst1999-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC25515/?report=xml; Genuine PMC HTML: complete Introduction sec1; Methods sec6–11; Results sec14–17 with Figure3–8 captions; entire Discussion sec18 with Figure9/10 captions. Sequence-discovery Results sec13, other Methods, image pixels and underlying cited experiments not read. | supports | Pig-brain coimmunoprecipitation and specific pairwise two-hybrid interactions support AP4 subunits. Epitope-tagged human beta4 in Rat1 cells and controls support near-TGN tubulovesicular localization with sparse labeling; purified clathrin-coated vesicles do not enrich AP4. Partial mu4 interacts with a CD63 tail in a yeast two-hybrid assay, lost upon tyrosine-to-alanine substitution. These data implicate sorting but do not directly track physiological cargo transport or prove a universal coat scaffold. |
| schema-result | just validate data/structures/other/ap_4_adaptor_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/ap_4_adaptor_complex.yaml |
| strict-result | just validate-strict data/structures/other/ap_4_adaptor_complex.yaml --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_4_adaptor_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/ap_4_adaptor_complex.yaml --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_4_adaptor_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch44-20261022-b975f18l/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_4_adaptor_complex-strict.tsv |
| ap4-causal-graphs | /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ap_4_adaptor_complex.yaml; Complete native read-only diagnostic log | supports | data/structures/other/ap_4_adaptor_complex.yaml  (GO:0030124)<br>  ap4_adaptor_complex_topology	ap4_beta4_subunit	NO_GENE_SYMBOLS	-&gt;ap4_beta4_subunit (PROTEIN: AP-4 beta4 subunit)<br>  ap4_adaptor_complex_topology	ap4_epsilon_subunit	NO_GENE_SYMBOLS	-&gt;ap4_epsilon_subunit (PROTEIN: AP-4 epsilon subunit)<br>  ap4_adaptor_complex_topology	ap4_mu4_subunit	NO_GENE_SYMBOLS	-&gt;ap4_mu4_subunit (PROTEIN: AP-4 mu4 subunit)<br>  ap4_adaptor_complex_topology	ap4_sigma4_subunit	NO_GENE_SYMBOLS	-&gt;ap4_sigma4_subunit (PROTEIN: AP-4 sigma4 subunit)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/ap_4_adaptor_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 3 of 3 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- The five complete same-base batch26 corpus gates await guarded integration by the parent before finalization.
- No image pixels, new sequence alignments, supplementary datasets or quantitative prevalence census were inspected. Exact source-reading sections are declared individually.
- The native family search is bounded to the listed InterPro text query and separately retrieved exact entries. Broad beta1/2/4, mu and sigma families or partial domains do not establish an exact subtype mapping for every remaining component; no all-catalog absence is claimed.
- Hirst localization uses sparse immunogold labeling of tagged human beta4 in Rat1 cells; TGN association is supported but individual cargo delivery routes are not directly measured. Sigma4 membership in this paper includes pairwise two-hybrid support because a suitable antibody was not obtained. No universal budding-yeast occurrence or coat scaffold is inferred.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes this review bundle. Parent owns same-base global-gate integration and later finalization; no scientific edits or persistence performed.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T043543Z-ap-4-adaptor-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: AP-4 adaptor complex scientific review
started_at: '2026-10-22T04:15:22Z'
finished_at: '2026-10-22T04:35:43Z'
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
summary: One bounded minor grounding finding for verified AP-4 subtype-specific subunit
  families. Exact complex identity, stated function and NONMECHANISTIC graph are supported
  within the declared experimental scope.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/other/ap_4_adaptor_complex.yaml
    sha256: e5f16d7db120bac359a5e922826eebea96ee57839a61ec70e12ad1663593a38e
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
- target_id: GO:0030124
  path: data/structures/other/ap_4_adaptor_complex.yaml
  label: AP-4 adaptor complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_4_adaptor_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete AP-4 record with frozen guidance/schema, exact
    native identities, all maintained component/example/function/graph/evidence claims
    and source sections listed in evidence. No uninspected figure pixels, supplementary
    experiments or universal taxon inventory are claimed.
  selection: Batch44 strict path-ordered target 10; all initial native inspection/schema/strict
    gates passed at unchanged f97b before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030124
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030124
  command: just validate data/structures/other/ap_4_adaptor_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030124
  command: just validate-strict data/structures/other/ap_4_adaptor_complex.yaml --out
    /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_4_adaptor_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030124
  command: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ap_4_adaptor_complex.yaml
  exit_code: 0
  summary: Native diagnostic passed; claim-level science and optional coverage are
    assessed separately.
  evidence_ids:
  - ap4-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030124
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030124
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - ap44-agent-go
  - ap44-agent-family-search-AP4
  - ap44-agent-ipr-IPR017109
  - ap44-agent-ipr-IPR016342
  - ap44-agent-ipr-IPR001392
  - ap44-agent-ipr-IPR016635
  - ap44-agent-hirst1999-meta
  - ap44-agent-hirst1999-legacy
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030124
  summary: 3 of 3 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030124
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0030124
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0030124
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0030124
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0030124
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
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/ap_4_adaptor_complex.yaml
  locator: Entire maintained target, including all history, components, examples,
    evidence, functions, graph and discussions
  accessed_at: '2026-10-22T04:20:39Z'
  support: context_only
  summary: Complete target read. Historical actions are provenance rather than independent
    experimental support.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent grounding/status and essentiality; graph and protein-example
    contracts
  accessed_at: '2026-10-22T04:20:39Z'
  support: context_only
  summary: A reviewed label-only component means no exact family can be asserted;
    membership and biological activity do not establish individual assembly necessity.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Grounding and REVIEWED_LABEL_ONLY rules, lines150–162
  accessed_at: '2026-10-22T04:20:39Z'
  support: context_only
  summary: The status represents a checked absence of an exact assertable term, not
    merely an identifier that was not curated in a prior pass.
- evidence_id: ap44-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030121,GO:0030122,GO:0030123,GO:0030124,GO:0030119,GO:0030131,GO:0098797,GO:0030130,GO:0030128,GO:0030132,GO:0072583
  locator: All eleven returned IDs/names/active states/definitions/synonyms and the
    typed child entries corresponding to maintained parent/parthood links
  accessed_at: '2026-10-22T04:15:34.948559Z'
  support: supports
  summary: The eleven native terms exactly identify AP1–AP4, their named subunits
    and isoform qualifiers, AP-type/clathrin-adaptor parents, AP2 plasma-membrane-complex
    parent, AP1/AP2 typed coat parthood, and clathrin-dependent endocytosis. The AP3/AP4
    definitions retain qualified clathrin association. Typed links were read from
    the exact parent children; unrelated children are not an exhaustive review scope.
  snapshot_sha256: 3d9d1876f519efc4b9ea1714babdee7f40389f9729404bfc2b51810c509cffba
- evidence_id: ap44-agent-family-search-AP4
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-4&page_size=100
  locator: Complete returned candidate accession/name/type list and pagination
  accessed_at: '2026-10-22T04:18:12.765581Z'
  support: context_only
  summary: Bounded native InterPro search for AP-4 returned 10 entries with no next
    page. Names/types identify candidate adaptor families, alongside unrelated text
    matches and domains; exact candidate entries are verified separately. This is
    not an exhaustive search of all protein-family resources.
  snapshot_sha256: 658972a6be9d7480e01c7a22c9a6a1473208c57a544e545bec10126a8b0cc18c
  search_scope: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-4&page_size=100
- evidence_id: ap44-agent-ipr-IPR017109
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017109/
  locator: Complete accession/name/type, description and LLM flags, integrated member
    signatures and hierarchy
  accessed_at: '2026-10-22T04:18:33.162169Z'
  support: supports
  summary: IPR017109 is type family, named Adaptor protein complex AP-4, epsilon subunit.
    Its complete native description and integrated signatures were read to distinguish
    the named subunit class from broader adaptor families or partial domains.
  snapshot_sha256: 8a8fa62739216a1dea224f99eff7330d36f73f89fb4f52cb1d558c18304cfa5a
- evidence_id: ap44-agent-ipr-IPR016342
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016342/
  locator: Complete accession/name/type, description and LLM flags, integrated member
    signatures and hierarchy
  accessed_at: '2026-10-22T04:16:34.048687Z'
  support: supports
  summary: IPR016342 is type family, named AP-1/2/4 complex subunit beta. Its complete
    native description and integrated signatures were read to distinguish the named
    subunit class from broader adaptor families or partial domains.
  snapshot_sha256: c4471532cb7d1df1f3ac04253e0efb8a2b918bd6d9987262e4715a65518cf48d
- evidence_id: ap44-agent-ipr-IPR001392
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001392/
  locator: Complete accession/name/type, description and LLM flags, integrated member
    signatures and hierarchy
  accessed_at: '2026-10-22T04:16:34.864178Z'
  support: supports
  summary: IPR001392 is type family, named Clathrin adaptor, mu subunit. Its complete
    native description and integrated signatures were read to distinguish the named
    subunit class from broader adaptor families or partial domains.
  snapshot_sha256: b514537350700a251483339024cec9ab501f94f7bcb632df44e9dcd5aa3415f4
- evidence_id: ap44-agent-ipr-IPR016635
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016635/
  locator: Complete accession/name/type, description and LLM flags, integrated member
    signatures and hierarchy
  accessed_at: '2026-10-22T04:16:34.821416Z'
  support: supports
  summary: IPR016635 is type family, named Adaptor protein complex, sigma subunit.
    Its complete native description and integrated signatures were read to distinguish
    the named subunit class from broader adaptor families or partial domains.
  snapshot_sha256: 597cc84578003af4a8f1b735aab9676edda62e82a0a06a4fa1422f1658b8aa8e
- evidence_id: ap44-agent-hirst1999-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.10.8.2787&format=json&resultType=core
  locator: 'Unique Europe PMC MED bibliographic record: exact DOI/PMID/PMC if returned,
    authors/title/year and complete abstract'
  accessed_at: '2026-10-22T04:15:37.620015Z'
  support: supports
  summary: Hirst, Bright, Rous and Robinson1999, DOI10.1091/mbc.10.8.2787/PMID10436028/PMC25515.
    Coimmunoprecipitation/two-hybrid evidence supports a four-subunit complex; sparse
    near-TGN localization and a tyrosine-dependent signal interaction suggest a sorting
    role.
  snapshot_sha256: a7085381558c7b096b30502be022be04d350c9fc57165f48df880c01c0fa7a63
- evidence_id: ap44-agent-hirst1999-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC25515/?report=xml
  locator: 'Genuine PMC HTML: complete Introduction sec1; Methods sec6–11; Results
    sec14–17 with Figure3–8 captions; entire Discussion sec18 with Figure9/10 captions.
    Sequence-discovery Results sec13, other Methods, image pixels and underlying cited
    experiments not read.'
  accessed_at: '2026-10-22T04:16:06.687412Z'
  support: supports
  summary: Pig-brain coimmunoprecipitation and specific pairwise two-hybrid interactions
    support AP4 subunits. Epitope-tagged human beta4 in Rat1 cells and controls support
    near-TGN tubulovesicular localization with sparse labeling; purified clathrin-coated
    vesicles do not enrich AP4. Partial mu4 interacts with a CD63 tail in a yeast
    two-hybrid assay, lost upon tyrosine-to-alanine substitution. These data implicate
    sorting but do not directly track physiological cargo transport or prove a universal
    coat scaffold.
  snapshot_sha256: 35f2526998b5825d759229949d6a875e2d18ef6194bbca07f33bb41322b6e996
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/ap_4_adaptor_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:15:24Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/ap_4_adaptor_complex.yaml'
  snapshot_sha256: 1764c3feac01dd1026ce9949fbe6d95f74442969f59e2e708ef2faf06dc8576e
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/ap_4_adaptor_complex.yaml
    --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_4_adaptor_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:15:25Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/ap_4_adaptor_complex.yaml\
    \ --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_4_adaptor_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch44-20261022-b975f18l/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_4_adaptor_complex-strict.tsv"
  snapshot_sha256: f99138dcd242a6936aeba7694c7a7f8b8051e1091f644b39b04af50dd517896a
- evidence_id: ap4-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ap_4_adaptor_complex.yaml
  locator: Complete native read-only diagnostic log
  accessed_at: '2026-10-22T04:16:26.666069Z'
  support: supports
  summary: "data/structures/other/ap_4_adaptor_complex.yaml  (GO:0030124)\n  ap4_adaptor_complex_topology\t\
    ap4_beta4_subunit\tNO_GENE_SYMBOLS\t->ap4_beta4_subunit (PROTEIN: AP-4 beta4 subunit)\n\
    \  ap4_adaptor_complex_topology\tap4_epsilon_subunit\tNO_GENE_SYMBOLS\t->ap4_epsilon_subunit\
    \ (PROTEIN: AP-4 epsilon subunit)\n  ap4_adaptor_complex_topology\tap4_mu4_subunit\t\
    NO_GENE_SYMBOLS\t->ap4_mu4_subunit (PROTEIN: AP-4 mu4 subunit)\n  ap4_adaptor_complex_topology\t\
    ap4_sigma4_subunit\tNO_GENE_SYMBOLS\t->ap4_sigma4_subunit (PROTEIN: AP-4 sigma4\
    \ subunit)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     4  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     4\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 58b5cb9bb66770212fbbc28f979e05d445e48ef1da552e7721420c8224611037
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/ap_4_adaptor_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 3 of 3 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
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
- assessment_id: scope
  area: scope
  topic: Discovery contexts without an invented microbial example
  outcome: supported
  target_ids:
  - GO:0030124
  summary: The record has no taxonomic-distribution or canonical-example assertion.
    Pig-brain biochemical material, human beta4 expressed in Rat1 cells and yeast
    two-hybrid hosts are distinct experimental contexts. A yeast assay host is not
    evidence that budding yeast has a native AP4 complex.
  evidence_ids:
  - record
  - ap44-agent-go
  - ap44-agent-hirst1999-meta
  - ap44-agent-hirst1999-legacy
- assessment_id: function-graph
  area: graph
  topic: Cautious sorting implication and clathrin boundary
  outcome: supported
  target_ids:
  - GO:0030124
  summary: The four subunit and TGN-association edges are supported at their stated
    scope. The final is implicated in edge preserves the inferential step from a specific
    tyrosine-dependent CD63-tail interaction to cargo sorting. The graph does not
    assert a resolved trafficking destination, physiological flux or a universal clathrin
    coat, and its NONMECHANISTIC scope fits the evidence.
  evidence_ids:
  - record
  - ap44-agent-go
  - ap44-agent-hirst1999-meta
  - ap44-agent-hirst1999-legacy
- assessment_id: identity
  area: identity
  topic: Exact AP-4 heterotetramer and containing-structure boundaries
  outcome: supported
  target_ids:
  - GO:0030124
  summary: The maintained definition, ontology identity, parentage, subtype-specific
    core classes and any coat parthood match the native GO authority. Different AP
    subtypes and containing coats remain distinct; no identity remapping is warranted.
  evidence_ids:
  - record
  - ap44-agent-go
  - ap44-agent-hirst1999-meta
  - ap44-agent-hirst1999-legacy
- assessment_id: grounding
  area: grounding
  topic: Exact subtype families versus deferred broader candidates
  outcome: concern
  target_ids:
  - GO:0030124
  summary: Native family entries support ap4_epsilon_subunit → InterPro:IPR017109.
    These are complete subtype-specific family classes, not merely domains or species-specific
    proteins, so their current REVIEWED_LABEL_ONLY status is not justified by saying
    no CURIE was curated in a prior pass. The other broader candidates do not close
    every remaining subunit class. Biological membership and identity remain supported.
  evidence_ids:
  - record
  - schema
  - curation
  - ap44-agent-family-search-AP4
  - ap44-agent-ipr-IPR017109
  - ap44-agent-ipr-IPR016342
  - ap44-agent-ipr-IPR001392
  - ap44-agent-ipr-IPR016635
- assessment_id: formation
  area: evidence
  topic: Constituent identity separated from assembly necessity
  outcome: unknown
  target_ids:
  - GO:0030124
  summary: All four components use UNKNOWN essentiality. The evidence supports the
    four named constituent classes; transport phenotypes, viability outcomes, interaction
    assays and reconstituted activity do not independently establish universal formation
    necessity for every subunit. UNKNOWN is retained rather than replaced by an inferred
    requirement.
  evidence_ids:
  - record
  - schema
  - ap44-agent-go
  - ap44-agent-hirst1999-meta
  - ap44-agent-hirst1999-legacy
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and bounded source availability
  outcome: supported
  target_ids:
  - GO:0030124
  summary: All target fields and explicit evidence placements were inspected. The
    four core components are represented. Missing additional taxa, isoforms or exhaustive
    accessory-protein inventories are not treated as defects; exact-family findings
    are limited to independently verified matches and the explicit label-only contract.
  evidence_ids:
  - record
  - ap44-agent-go
  - ap44-agent-family-search-AP4
  - ap44-agent-hirst1999-meta
  - ap44-agent-hirst1999-legacy
findings:
- finding_id: F1
  issue_key: ap4-verified-subtype-families-label-only
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the verified AP-4 subtype-specific subunit families
  description: Exact native InterPro family identities are available for ap4_epsilon_subunit
    → InterPro:IPR017109. The affected components nevertheless carry REVIEWED_LABEL_ONLY
    and notes saying no exact CURIE was curated in the prior pass. CURATION and schema
    define this status as no exact assertable family, not deferred curation. The native
    family types/descriptions match the component classes; other unresolved broad
    families and domains are not promoted.
  target_ids:
  - GO:0030124
  field_paths:
  - components#ap4_epsilon_subunit.grounding_status
  - components#ap4_epsilon_subunit.grounding_notes
  - discussions#resolve_ap4_subunit_groundings
  evidence_ids:
  - record
  - schema
  - curation
  - ap44-agent-family-search-AP4
  - ap44-agent-ipr-IPR017109
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_4_adaptor_complex.yaml
    role: maintained scientific record
  rule_id: Exact protein-family grounding and reviewed-label-only semantics
  native_severity: minor
  normalization_reason: The correct complex and biological subunits are retained.
    The defect is a bounded omitted family mapping and incompatible status/notes for
    verified exact classes; it does not invalidate the whole record or require broader-domain
    substitution.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0030124
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_4_adaptor_complex.yaml
    role: maintained scientific record
  description: In separately authorized curation, add the verified mappings ap4_epsilon_subunit
    → InterPro:IPR017109; remove the obsolete reviewed-label-only status/notes on
    those mapped rows and narrow the existing TODO to unresolved classes. Preserve
    the exact complex, roles, examples and UNKNOWN formation necessity; do not force
    broad beta/mu/sigma or domain entries onto other subtype classes.
  acceptance_checks:
  - Each added CURIE resolves to the stated native subtype-specific family, with current
    identifier/label correspondence.
  - Only the verified classes lose reviewed-label-only status; genuinely unresolved
    classes and their bounded TODO remain.
  - Focused schema/strict, protein/graph diagnostics and source-placement checks pass
    after authorized curation.
limitations:
- The five complete same-base batch26 corpus gates await guarded integration by the
  parent before finalization.
- No image pixels, new sequence alignments, supplementary datasets or quantitative
  prevalence census were inspected. Exact source-reading sections are declared individually.
- The native family search is bounded to the listed InterPro text query and separately
  retrieved exact entries. Broad beta1/2/4, mu and sigma families or partial domains
  do not establish an exact subtype mapping for every remaining component; no all-catalog
  absence is claimed.
- Hirst localization uses sparse immunogold labeling of tagged human beta4 in Rat1
  cells; TGN association is supported but individual cargo delivery routes are not
  directly measured. Sigma4 membership in this paper includes pairwise two-hybrid
  support because a suitable antibody was not obtained. No universal budding-yeast
  occurrence or coat scaffold is inferred.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes this review bundle. Parent owns same-base global-gate
  integration and later finalization; no scientific edits or persistence performed.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
