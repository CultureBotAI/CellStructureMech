# Dna topoisomerase iv complex scientific review

- Review: 20261022T055924Z-dna-topoisomerase-iv-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:37:33Z
- Finished UTC: 2026-10-22T05:59:24Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

TopoIV identity, correct K12 proteins and coarse activity graph are supported. The inspected family candidates do not exactly map the generic ParC/ParE classes, so no forced mapping or optional-field finding is made.

## Scope And Provenance

Exactly one complete maintained record, native frozen guidance and actual source passages identified per evidence locator; no other maintained scientific record used as evidence.

Selection: Target 7 of batch51, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009340 | data/structures/other/dna_topoisomerase_iv_complex.yaml | maintained | DNA topoisomerase IV complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0009340 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009340 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0009340 | Native focused check passed; scientific support separately assessed. |
| Native verify | passed | True | GO:0009340 | Native focused check passed; scientific support separately assessed. |
| Expression-module applicability | not_applicable | False | GO:0009340 | No expression-module claim requires this resource. |
| Claim-level scientific review | passed | True | GO:0009340 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0009340 | 12 of 14 collected target identifiers returned OK. PMID:7783632: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:8227000: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0009340 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009340 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009340 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009340 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0009340 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### TopoIV identity and reaction class

identity: supported. Targets: GO:0009340.

The maintained bacterial ParC/ParE definition, parentage and exact synonym agree with source identity. Unlike the upstream GO heterodimer wording, the target does not misstate the2:2 E.coli enzyme.

### Correct examples and unresolved generic family boundary

grounding: supported. Targets: GO:0009340.

ParC/P0AFI2 and ParE/P20083 are correct reviewedK12 examples. The inspected candidate entries are genuinely narrower taxonomic families or broader topoisomerase classes. The existing label-only boundary and open TODO remain justified; optional stoichiometry fields are not required merely because2:2 is known.

### Species example and recombinant preparation

scope: supported. Targets: GO:0009340.

E.coli canonical scope is supported. The K12 accessions are reference identities; primary overexpression uses BL21(DE3)pLysS and is not falsely treated as a native reference-strain preparation. No taxonomic-distribution prevalence row is asserted.

### Nonmechanistic ATP-dependent topological activity

graph: supported. Targets: GO:0009340.

Primary relaxation/decatenation and native activity definition support the graph. The graph is explicitly NONMECHANISTIC and does not claim resolved gates or cleavage intermediates. ATP-dependent catalysis is distinguished from heterotetramer assembly that occurs withoutATP/DNA.

### Formation scope without adding optional enums

grounding: unknown. Targets: GO:0009340.

Terminal-truncation experiments directly test heterotetramer association, but the target supplies no essentiality fields. No optional field is invented and no claim of universal organism viability is made.

### Full record and maintained boundaries

completeness: supported. Targets: GO:0009340.

All target fields, evidence, discussions and historical entries were read, including adjacent-complex exclusions. Historical reviewer conclusions are not biological evidence. No optional inventory or uninspected detailed mechanism is forced.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dna_topoisomerase_iv_complex.yaml; Entire target, including all components/examples, graph, evidence, discussions and history | context_only | The full maintained record was read. Historical curation notes are not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, EssentialityEnum and NONMECHANISTIC graph scope | context_only | Family identity is separate from a taxon-specific example. Assembly necessity differs from composition, catalytic requirement and viability. |
| curation | docs/CURATION.md; Exact family mapping and REVIEWED_LABEL_ONLY contract, especially159–160 | context_only | Reviewed label-only status requires an unresolved exact mapping, rather than simply deferring a verified available family. |
| replication51-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003918,GO:0006270,GO:0009330,GO:0009340,GO:0032297,GO:0032991,GO:1990077,GO:1990078,GO:1990083,GO:1990084,GO:1990085,GO:1990099,GO:1990100,GO:1990101,GO:1990102,GO:1990125,GO:1990157; Complete relevant definitions, synonyms, active status and typed child links within the17-term response; unrelated children are not promoted | supports | GO0009340 identifies ParC/ParE topoisomeraseIV and GO0009330 lists it as an is-a child. GO0003918 identifies ATP-dependent typeII activity. The target appropriately avoids the native heterodimeric wording, which conflicts with the primary2:2 architecture. |
| replication51-agent-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxon response | supports | ENA taxon562 is Escherichia coli, rank species; native names and lineage distinguish species from reference strain. |
| replication51-agent-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxon response | supports | ENA taxon83333 is Escherichia coli K-12, rank strain; native names and lineage distinguish species from reference strain. |
| replication51-agent-protein-P0AFI2 | https://rest.uniprot.org/uniprotkb/P0AFI2.json; Accession/status/name/genes/organism; complete relevant comments, localization evidence references and InterPro xrefs | supports | Reviewed P0AFI2 is the declared parC protein in E.coli K12 taxon83333. Native identity, gene names, function/subunit/similarity annotations and family xrefs were read. |
| replication51-agent-gene-parC-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AparC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identities, organism and gene aliases | supports | Exact reviewed gene parC in the stated K12 organism83333 returns one entry, P0AFI2; the current single-entry note is supported where asserted. |
| replication51-agent-protein-P20083 | https://rest.uniprot.org/uniprotkb/P20083.json; Accession/status/name/genes/organism; complete relevant comments, localization evidence references and InterPro xrefs | supports | Reviewed P20083 is the declared parE protein in E.coli K12 taxon83333. Native identity, gene names, function/subunit/similarity annotations and family xrefs were read. |
| replication51-agent-gene-parE-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AparE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identities, organism and gene aliases | supports | Exact reviewed gene parE in the stated K12 organism83333 returns one entry, P20083; the current single-entry note is supported where asserted. |
| replication51-agent-pmid-7783632 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7783632+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and entire native abstract | supports | Native MED7783632: The twisted 'life' of DNA in the cell: bacterial topoisomerases. Authors Luttinger A.; DOI 10.1111/j.1365-2958.1995.tb02369.x. Complete abstract read at secondary-review abstract tier; metadata is not a claim of full-body access. |
| replication51-agent-pmid-8227000 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8227000+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and entire native abstract | supports | Native MED8227000: Escherichia coli topoisomerase IV. Purification, characterization, subunit structure, and subunit interactions. Authors Peng H, Marians KJ.; DOI 10.1016/s0021-9258(20)80551-1. Complete abstract read at primary-study abstract tier; metadata is not a claim of full-body access. |
| replication51-agent-peng1993-browser | https://www.researchgate.net/publication/14972288_Escherichia_coli_topoisomerase_IV_Purification_characterization_subunit_structure_and_subunit_interactions; ResearchGate-displayed primary article lines0–1159: front matter, complete abstract, Introduction and Methods DNA sequencing/overexpression opening; discontinuous browser source, not a recovered native PDF | supports | The primary title/abstract and opening text establish the exact Peng/Marians1993 paper and reconstituted ParC2ParE2 enzyme. Its overexpression Methods opening identifies T7 constructs and BL21(DE3)pLysS expression, not an unmodifiedK12 strain experiment. |
| replication51-agent-peng1993-browser-subunits | https://www.researchgate.net/publication/14972288_Escherichia_coli_topoisomerase_IV_Purification_characterization_subunit_structure_and_subunit_interactions; Displayed primary lines3839–5013: late Results heterotetramer/truncation-association paragraphs, Fig8/9 captions, Discussion opening/nucleotide requirement/assembly paragraphs and partial antibiotic context; no pixels or unshown body certified | supports | Primary late Results and Discussion establish the2:2 enzyme and failure of terminally truncated subunits to associate. Assembly requires neither DNA norATP, whereas relaxation/decatenation require ATP or dATP. These distinct assays support the coarse activity graph without equating catalysis and formation. |
| replication51-agent-peng1993-publisher | https://www.jbc.org/article/S0021-9258(20)80551-1/pdf; Retained publisher access response | context_only | Publisher fulltext request returned HTTP403; no primary body was obtained from this route. |
| replication51-agent-ipr-IPR005742 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005742/; Native name/type, complete description, hierarchy/signatures and curation flags | supports | IPR005742 is a Gram-negative ParC full-protein family; its specific taxonomic boundary is narrower than the generic bacterial subunit class. |
| replication51-agent-ipr-IPR005737 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005737/; Native name/type, complete description, hierarchy/signatures and curation flags | supports | IPR005737 is a Gram-negative ParE family; its narrower scope and other subgroup hierarchy do not justify treating it as a universal ParE family. |
| replication51-agent-ipr-IPR050220 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050220/; Native name/type, complete description, hierarchy/signatures and curation flags | supports | IPR050220 spans typeII topoisomerases and is broader than ParC; its LLM-generated unchecked descriptive text is not primary biological evidence. |
| replication51-agent-ipr-IPR001241 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001241/; Native name/type, complete description, hierarchy/signatures and curation flags | supports | IPR001241 encompasses typeIIA topoisomerase proteins beyond the specific generic ParE class; broad family membership is not an exact subclass mapping. |
| schema-result | just validate data/structures/other/dna_topoisomerase_iv_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dna_topoisomerase_iv_complex.yaml |
| strict-result | just validate-strict data/structures/other/dna_topoisomerase_iv_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_topoisomerase_iv_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dna_topoisomerase_iv_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_topoisomerase_iv_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_topoisomerase_iv_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/dna_topoisomerase_iv_complex.yaml  (GO:0009340)<br>  topoisomerase_iv_type_ii_activity	topoisomerase_iv_subunit_a	COVERED	-&gt;topoisomerase_iv_subunit_a (UniProtKB:P0AFI2)<br>  topoisomerase_iv_type_ii_activity	topoisomerase_iv_subunit_b	COVERED	-&gt;topoisomerase_iv_subunit_b (UniProtKB:P20083)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dna_topoisomerase_iv_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 14 collected target identifiers returned OK. PMID:7783632: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:8227000: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, supplementary experimental data, sequence alignment or deposited coordinate geometry was independently reanalyzed. Actual text/caption and native-response scopes are specified per evidence row.
- Peng1993 publisher PDF returned403. Genuine displayed primary excerpts and its complete native abstract were read, not a complete downloaded primary body. Luttinger1995 is a complete secondary-review abstract only.
- Native GO0009340 heterodimeric language conflicts with the inspected ParC2ParE2 primary result; the maintained definition already avoids that wording.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes qualified clean reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T055924Z-dna-topoisomerase-iv-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Dna topoisomerase iv complex scientific review
started_at: '2026-10-22T05:37:33Z'
finished_at: '2026-10-22T05:59:24Z'
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
summary: TopoIV identity, correct K12 proteins and coarse activity graph are supported.
  The inspected family candidates do not exactly map the generic ParC/ParE classes,
  so no forced mapping or optional-field finding is made.
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
  - path: data/structures/other/dna_topoisomerase_iv_complex.yaml
    sha256: fb14ab25e6bf5e766d86b767a0f20597e77782d62fae6c5b48ed82dcee0ef070
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
- target_id: GO:0009340
  path: data/structures/other/dna_topoisomerase_iv_complex.yaml
  label: DNA topoisomerase IV complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_topoisomerase_iv_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained record, native frozen guidance and
    actual source passages identified per evidence locator; no other maintained scientific
    record used as evidence.
  selection: Target 7 of batch51, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009340
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009340
  command: just validate data/structures/other/dna_topoisomerase_iv_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009340
  command: just validate-strict data/structures/other/dna_topoisomerase_iv_complex.yaml
    --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_topoisomerase_iv_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0009340
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; scientific support separately assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0009340
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; scientific support separately assessed.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0009340
  summary: No expression-module claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009340
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - replication51-agent-go
  - replication51-agent-tax562
  - replication51-agent-tax83333
  - replication51-agent-protein-P0AFI2
  - replication51-agent-gene-parC-83333
  - replication51-agent-protein-P20083
  - replication51-agent-gene-parE-83333
  - replication51-agent-pmid-7783632
  - replication51-agent-pmid-8227000
  - replication51-agent-peng1993-browser
  - replication51-agent-peng1993-browser-subunits
  - replication51-agent-peng1993-publisher
  - replication51-agent-ipr-IPR005742
  - replication51-agent-ipr-IPR005737
  - replication51-agent-ipr-IPR050220
  - replication51-agent-ipr-IPR001241
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0009340
  summary: '12 of 14 collected target identifiers returned OK. PMID:7783632: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force.; PMID:8227000: UNREACHABLE; Exact native EuropePMC MED identifier, title
    and DOI independently inspected after the bulk eutils414 transport failure. Identifier
    resolution does not certify all biological claims; declared primary-body and abstract
    reading limits remain in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - replication51-agent-pmid-7783632
  - replication51-agent-pmid-8227000
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009340
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
  - GO:0009340
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
  - GO:0009340
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
  - GO:0009340
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
  - GO:0009340
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
  reference: data/structures/other/dna_topoisomerase_iv_complex.yaml
  locator: Entire target, including all components/examples, graph, evidence, discussions
    and history
  accessed_at: '2026-10-22T05:49:32Z'
  support: context_only
  summary: The full maintained record was read. Historical curation notes are not
    independent biological evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, EssentialityEnum and NONMECHANISTIC
    graph scope
  accessed_at: '2026-10-22T05:49:32Z'
  support: context_only
  summary: Family identity is separate from a taxon-specific example. Assembly necessity
    differs from composition, catalytic requirement and viability.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact family mapping and REVIEWED_LABEL_ONLY contract, especially159–160
  accessed_at: '2026-10-22T05:49:32Z'
  support: context_only
  summary: Reviewed label-only status requires an unresolved exact mapping, rather
    than simply deferring a verified available family.
- evidence_id: replication51-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003918,GO:0006270,GO:0009330,GO:0009340,GO:0032297,GO:0032991,GO:1990077,GO:1990078,GO:1990083,GO:1990084,GO:1990085,GO:1990099,GO:1990100,GO:1990101,GO:1990102,GO:1990125,GO:1990157
  locator: Complete relevant definitions, synonyms, active status and typed child
    links within the17-term response; unrelated children are not promoted
  accessed_at: '2026-10-22T05:42:45.973692Z'
  support: supports
  summary: GO0009340 identifies ParC/ParE topoisomeraseIV and GO0009330 lists it as
    an is-a child. GO0003918 identifies ATP-dependent typeII activity. The target
    appropriately avoids the native heterodimeric wording, which conflicts with the
    primary2:2 architecture.
  snapshot_sha256: 20acc6fb4f33b15254c0883eb10baca7a549febfef3948d31b5eafda0771038b
- evidence_id: replication51-agent-tax562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxon response
  accessed_at: '2026-10-22T05:42:45.974189Z'
  support: supports
  summary: ENA taxon562 is Escherichia coli, rank species; native names and lineage
    distinguish species from reference strain.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: replication51-agent-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxon response
  accessed_at: '2026-10-22T05:42:45.974327Z'
  support: supports
  summary: ENA taxon83333 is Escherichia coli K-12, rank strain; native names and
    lineage distinguish species from reference strain.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: replication51-agent-protein-P0AFI2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AFI2.json
  locator: Accession/status/name/genes/organism; complete relevant comments, localization
    evidence references and InterPro xrefs
  accessed_at: '2026-10-22T05:42:46.852257Z'
  support: supports
  summary: Reviewed P0AFI2 is the declared parC protein in E.coli K12 taxon83333.
    Native identity, gene names, function/subunit/similarity annotations and family
    xrefs were read.
  snapshot_sha256: c4fc919de9d73e0d96e4a47ee12eff2b031d7a2e927aa9033082b8e3c6caf1d4
- evidence_id: replication51-agent-gene-parC-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AparC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identities, organism and gene aliases
  accessed_at: '2026-10-22T05:42:47.434736Z'
  support: supports
  summary: Exact reviewed gene parC in the stated K12 organism83333 returns one entry,
    P0AFI2; the current single-entry note is supported where asserted.
  snapshot_sha256: 5f1885061e1cbd160c0a16d8e638641a25f23f40bdd535e1a0287a35c5bb7e9d
  search_scope: UniProt gene_exact:parC, reviewed:true, taxonomy_id:83333; size500;
    complete returned identities read. Descendant-strain search results are not used
    to falsify an exact-organism claim.
- evidence_id: replication51-agent-protein-P20083
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P20083.json
  locator: Accession/status/name/genes/organism; complete relevant comments, localization
    evidence references and InterPro xrefs
  accessed_at: '2026-10-22T05:42:46.948399Z'
  support: supports
  summary: Reviewed P20083 is the declared parE protein in E.coli K12 taxon83333.
    Native identity, gene names, function/subunit/similarity annotations and family
    xrefs were read.
  snapshot_sha256: 018fe3a977ac2df60e8ccf94ea6ceec53c7b80c32b7616e380be45989b0ea97c
- evidence_id: replication51-agent-gene-parE-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AparE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identities, organism and gene aliases
  accessed_at: '2026-10-22T05:42:47.625128Z'
  support: supports
  summary: Exact reviewed gene parE in the stated K12 organism83333 returns one entry,
    P20083; the current single-entry note is supported where asserted.
  snapshot_sha256: 7cae2215f3d27b62d077ee0ba4d48d096dd0c5bff2a113e90a7b14db1c259032
  search_scope: UniProt gene_exact:parE, reviewed:true, taxonomy_id:83333; size500;
    complete returned identities read. Descendant-strain search results are not used
    to falsify an exact-organism claim.
- evidence_id: replication51-agent-pmid-7783632
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7783632+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and entire native abstract
  accessed_at: '2026-10-22T05:42:49.364776Z'
  support: supports
  summary: 'Native MED7783632: The twisted ''life'' of DNA in the cell: bacterial
    topoisomerases. Authors Luttinger A.; DOI 10.1111/j.1365-2958.1995.tb02369.x.
    Complete abstract read at secondary-review abstract tier; metadata is not a claim
    of full-body access.'
  snapshot_sha256: 00002d1b45474e5b4fd08ee6f0ce4e5f23b21906385379dd7e16f731c9d91450
- evidence_id: replication51-agent-pmid-8227000
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8227000+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and entire native abstract
  accessed_at: '2026-10-22T05:42:49.399741Z'
  support: supports
  summary: 'Native MED8227000: Escherichia coli topoisomerase IV. Purification, characterization,
    subunit structure, and subunit interactions. Authors Peng H, Marians KJ.; DOI
    10.1016/s0021-9258(20)80551-1. Complete abstract read at primary-study abstract
    tier; metadata is not a claim of full-body access.'
  snapshot_sha256: 788b6ff5caa16fcb853371f371cd8690e20f76e5c2e71c2e59124b3bfa01379c
- evidence_id: replication51-agent-peng1993-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/14972288_Escherichia_coli_topoisomerase_IV_Purification_characterization_subunit_structure_and_subunit_interactions
  locator: 'ResearchGate-displayed primary article lines0–1159: front matter, complete
    abstract, Introduction and Methods DNA sequencing/overexpression opening; discontinuous
    browser source, not a recovered native PDF'
  accessed_at: '2026-10-22T05:44:08Z'
  support: supports
  summary: The primary title/abstract and opening text establish the exact Peng/Marians1993
    paper and reconstituted ParC2ParE2 enzyme. Its overexpression Methods opening
    identifies T7 constructs and BL21(DE3)pLysS expression, not an unmodifiedK12 strain
    experiment.
  snapshot_sha256: ae0145a3c531850464e872a8f21ceff592b819ffd74a7fa6cee6e0a2d0d5fd82
- evidence_id: replication51-agent-peng1993-browser-subunits
  kind: primary_source
  reference: https://www.researchgate.net/publication/14972288_Escherichia_coli_topoisomerase_IV_Purification_characterization_subunit_structure_and_subunit_interactions
  locator: 'Displayed primary lines3839–5013: late Results heterotetramer/truncation-association
    paragraphs, Fig8/9 captions, Discussion opening/nucleotide requirement/assembly
    paragraphs and partial antibiotic context; no pixels or unshown body certified'
  accessed_at: '2026-10-22T05:45:16Z'
  support: supports
  summary: Primary late Results and Discussion establish the2:2 enzyme and failure
    of terminally truncated subunits to associate. Assembly requires neither DNA norATP,
    whereas relaxation/decatenation require ATP or dATP. These distinct assays support
    the coarse activity graph without equating catalysis and formation.
  snapshot_sha256: 684f361797a10b3ba3a9c34dc081c08d04e2e5c349d179efe270145f8a7bb621
- evidence_id: replication51-agent-peng1993-publisher
  kind: database
  reference: https://www.jbc.org/article/S0021-9258(20)80551-1/pdf
  locator: Retained publisher access response
  accessed_at: '2026-10-22T05:43:16.589132Z'
  support: context_only
  summary: Publisher fulltext request returned HTTP403; no primary body was obtained
    from this route.
  snapshot_sha256: 9fc7ab8d1025f66a87cf5348de1b52b4aee5c751864a6c6c6f0a3115140b4713
- evidence_id: replication51-agent-ipr-IPR005742
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005742/
  locator: Native name/type, complete description, hierarchy/signatures and curation
    flags
  accessed_at: '2026-10-22T05:42:49.995659Z'
  support: supports
  summary: IPR005742 is a Gram-negative ParC full-protein family; its specific taxonomic
    boundary is narrower than the generic bacterial subunit class.
  snapshot_sha256: 6071e1005b83c8ef30ac399047c0feb257d967ad29b3b14ee8732e150c447946
- evidence_id: replication51-agent-ipr-IPR005737
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005737/
  locator: Native name/type, complete description, hierarchy/signatures and curation
    flags
  accessed_at: '2026-10-22T05:42:50.023809Z'
  support: supports
  summary: IPR005737 is a Gram-negative ParE family; its narrower scope and other
    subgroup hierarchy do not justify treating it as a universal ParE family.
  snapshot_sha256: b8cc98f01329dff69753daf4d9fa545fa7da26c791f6de0df07b8928853c4b40
- evidence_id: replication51-agent-ipr-IPR050220
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050220/
  locator: Native name/type, complete description, hierarchy/signatures and curation
    flags
  accessed_at: '2026-10-22T05:42:50.118928Z'
  support: supports
  summary: IPR050220 spans typeII topoisomerases and is broader than ParC; its LLM-generated
    unchecked descriptive text is not primary biological evidence.
  snapshot_sha256: 6e0a444bf2047aca694717d1dab349a1fea6ed034f48c6a854555b50e3cac224
- evidence_id: replication51-agent-ipr-IPR001241
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001241/
  locator: Native name/type, complete description, hierarchy/signatures and curation
    flags
  accessed_at: '2026-10-22T05:42:50.612128Z'
  support: supports
  summary: IPR001241 encompasses typeIIA topoisomerase proteins beyond the specific
    generic ParE class; broad family membership is not an exact subclass mapping.
  snapshot_sha256: d61fcaf53fbc962df1bd2ef49b6c8988637eca6ab75ae7f1d4e119f16926dc1e
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dna_topoisomerase_iv_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:35Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dna_topoisomerase_iv_complex.yaml'
  snapshot_sha256: eb30f08a66291d8e63d1494812145e6b4a27494ca6071e18a619d6696105630d
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dna_topoisomerase_iv_complex.yaml
    --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_topoisomerase_iv_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:37Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dna_topoisomerase_iv_complex.yaml\
    \ --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_topoisomerase_iv_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_topoisomerase_iv_complex-strict.tsv"
  snapshot_sha256: 3dc9af8eb65b75fb5e20dd40e02fb564d66746875ba40efd04c7c5cc7fd18e6b
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:42:48.171716Z'
  support: supports
  summary: "data/structures/other/dna_topoisomerase_iv_complex.yaml  (GO:0009340)\n\
    \  topoisomerase_iv_type_ii_activity\ttopoisomerase_iv_subunit_a\tCOVERED\t->topoisomerase_iv_subunit_a\
    \ (UniProtKB:P0AFI2)\n  topoisomerase_iv_type_ii_activity\ttopoisomerase_iv_subunit_b\t\
    COVERED\t->topoisomerase_iv_subunit_b (UniProtKB:P20083)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     2  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 6de87a107b6e984920696fdc44e3c3d1a38f70dc028887322f39804be0c9c0af
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:42:49.820365Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dna_topoisomerase_iv_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '12 of 14 collected target identifiers returned OK. PMID:7783632: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force.; PMID:8227000: UNREACHABLE; Exact native EuropePMC MED identifier, title
    and DOI independently inspected after the bulk eutils414 transport failure. Identifier
    resolution does not certify all biological claims; declared primary-body and abstract
    reading limits remain in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
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
  topic: TopoIV identity and reaction class
  outcome: supported
  target_ids:
  - GO:0009340
  summary: The maintained bacterial ParC/ParE definition, parentage and exact synonym
    agree with source identity. Unlike the upstream GO heterodimer wording, the target
    does not misstate the2:2 E.coli enzyme.
  evidence_ids:
  - record
  - replication51-agent-go
  - replication51-agent-peng1993-browser
  - replication51-agent-peng1993-browser-subunits
- assessment_id: grounding
  area: grounding
  topic: Correct examples and unresolved generic family boundary
  outcome: supported
  target_ids:
  - GO:0009340
  summary: ParC/P0AFI2 and ParE/P20083 are correct reviewedK12 examples. The inspected
    candidate entries are genuinely narrower taxonomic families or broader topoisomerase
    classes. The existing label-only boundary and open TODO remain justified; optional
    stoichiometry fields are not required merely because2:2 is known.
  evidence_ids:
  - record
  - curation
  - replication51-agent-protein-P0AFI2
  - replication51-agent-protein-P20083
  - replication51-agent-gene-parC-83333
  - replication51-agent-gene-parE-83333
  - replication51-agent-ipr-IPR005742
  - replication51-agent-ipr-IPR005737
  - replication51-agent-ipr-IPR050220
  - replication51-agent-ipr-IPR001241
  - replication51-agent-peng1993-browser
  - replication51-agent-peng1993-browser-subunits
- assessment_id: scope
  area: scope
  topic: Species example and recombinant preparation
  outcome: supported
  target_ids:
  - GO:0009340
  summary: E.coli canonical scope is supported. The K12 accessions are reference identities;
    primary overexpression uses BL21(DE3)pLysS and is not falsely treated as a native
    reference-strain preparation. No taxonomic-distribution prevalence row is asserted.
  evidence_ids:
  - record
  - replication51-agent-peng1993-browser
  - replication51-agent-tax562
  - replication51-agent-tax83333
  - replication51-agent-protein-P0AFI2
  - replication51-agent-protein-P20083
- assessment_id: graph
  area: graph
  topic: Nonmechanistic ATP-dependent topological activity
  outcome: supported
  target_ids:
  - GO:0009340
  summary: Primary relaxation/decatenation and native activity definition support
    the graph. The graph is explicitly NONMECHANISTIC and does not claim resolved
    gates or cleavage intermediates. ATP-dependent catalysis is distinguished from
    heterotetramer assembly that occurs withoutATP/DNA.
  evidence_ids:
  - record
  - schema
  - replication51-agent-go
  - replication51-agent-peng1993-browser-subunits
- assessment_id: formation
  area: grounding
  topic: Formation scope without adding optional enums
  outcome: unknown
  target_ids:
  - GO:0009340
  summary: Terminal-truncation experiments directly test heterotetramer association,
    but the target supplies no essentiality fields. No optional field is invented
    and no claim of universal organism viability is made.
  evidence_ids:
  - record
  - schema
  - replication51-agent-peng1993-browser-subunits
- assessment_id: coverage
  area: completeness
  topic: Full record and maintained boundaries
  outcome: supported
  target_ids:
  - GO:0009340
  summary: All target fields, evidence, discussions and historical entries were read,
    including adjacent-complex exclusions. Historical reviewer conclusions are not
    biological evidence. No optional inventory or uninspected detailed mechanism is
    forced.
  evidence_ids:
  - record
  - schema
  - curation
  - replication51-agent-go
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, supplementary experimental data, sequence alignment or deposited
  coordinate geometry was independently reanalyzed. Actual text/caption and native-response
  scopes are specified per evidence row.
- Peng1993 publisher PDF returned403. Genuine displayed primary excerpts and its complete
  native abstract were read, not a complete downloaded primary body. Luttinger1995
  is a complete secondary-review abstract only.
- Native GO0009340 heterodimeric language conflicts with the inspected ParC2ParE2
  primary result; the maintained definition already avoids that wording.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes qualified clean reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
