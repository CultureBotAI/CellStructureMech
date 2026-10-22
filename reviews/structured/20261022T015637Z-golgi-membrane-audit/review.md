# Golgi membrane identity, source and topology review

- Review: 20261022T015637Z-golgi-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:39:31Z
- Finished UTC: 2026-10-22T01:56:37Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed within the explicitly bounded source scope.

## Scope And Provenance

Entire single target: exact identity, structure/material boundaries, source and taxonomic claims, examples, functions and every graph edge.

Selection: Target 8 of batch thirty in strict uncovered path order from fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000139 | data/structures/membrane_organelle/golgi_membrane.yaml | maintained | Golgi membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0000139 | Focused native check passed; biological source scope reviewed separately. |
| Native protein causal-graphs | passed | True | GO:0000139 | Focused native check passed; biological source scope reviewed separately. |
| Focused native schema | passed | True | GO:0000139 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000139 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0000139 | No expression-module dataset or inference is used. Physical topology, native protein identities and microscopy/transport sources are applicable. |
| Claim-level scientific review | passed | True | GO:0000139 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0000139 | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0000139 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000139 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000139 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000139 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0000139 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Boundary material versus internal volume

grounding: supported. Targets: GO:0000139.

The label-only LIPID row describes collective bilayer material and explicitly avoids grounding it to a whole-membrane GO identifier. ESSENTIAL refers to the constitutive boundary, not a knockout result for each lipid. No exact species mixture or stoichiometry is asserted.

### Exact structure and mereology

identity: supported. Targets: GO:0000139.

Native GO definitions distinguish the Golgi membrane from the individual cisterna and associated coat. Recorded synonyms and broader class/parthood statements agree with the inspected authority definitions and relations.

### Saccharomyces example and experimental boundaries

scope: supported. Targets: GO:0000139.

Species4932 is exact. Both imaging papers directly observe budding-yeast cisternal marker changes. Unstacked yeast cisternae, microscopy conditions and mutant effects are not generalized to all eukaryotic architecture. COMMON remains qualitative occurrence.

### Compartment role and bounded functional evidence

evidence: supported. Targets: GO:0000139.

Membrane boundaries and the stated yeast cisternal context are supported; no separate optional function inventory or exact lipid composition is required.

### All target graph edges

graph: supported. Targets: GO:0000139.

All four NONMECHANISTIC edges describe membrane parthood/enclosure and COPI coat participation in budding. Native GO0035964 establishes Golgi membrane evagination; Serafini provides coat/ARF association and the separately read review provides recruitment/traffic context. The graph does not specify an isolated force-generation experiment, exclusive coat sufficiency or a full biochemical mechanism.

### Molecular requirements and complete inventories

evidence: unknown. Targets: GO:0000139.

An exact lipid composition, exhaustive machinery inventory and molecular formation-necessity tests are not established by these sources. Native protein identity and generic function annotations are distinguished from direct localization assays and from cisternal-maturation experiments.

### All maintained fields and bounded source tiers

completeness: supported. Targets: GO:0000139.

Full target, every graph edge, discussion and history entry were read. No maintained image asset, numeric physical property, trait link or verbatim snippet is asserted. PROPOSED status is retained. Empty optional slots and inaccessible bodies alone are not findings.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/golgi_membrane.yaml; Entire maintained target, including all examples, evidence, graph edges, discussions and history | context_only | Full target read; no scientific record, native status, history or generated page is edited. |
| policy | docs/CURATION.md; Exact structure identity, hierarchy/parthood and narrow source support | context_only | Whole apparatus, individual cisterna, enclosing bilayer and internal volume are separate identities. A source for general trafficking does not establish every named molecular mechanism. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent and ProteinExample definitions, essentiality and graph representation | context_only | Protein examples identify taxon-paired instances; membership and formation necessity need separate evidence. Label-only collective lipid material is not an exact whole-membrane molecular grounding. |
| root30-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005794,GO:0043231,GO:0012505,GO:0000139,GO:0031985,GO:0032580,GO:0005796,GO:0070013,GO:0016020,GO:0030126,GO:0035964; Complete native definitions, names, synonyms, active flags and all returned child relations for eleven identifiers | supports | All eleven active native GO terms were read. Whole GO0005794 is a membrane-bounded organelle and part of the endomembrane system; its exact Golgi complex synonym and membrane/lumen children agree. GO0031985 is the bounded cisterna, GO0032580 its membrane, GO0005796 the internal volume, and GO0000139 the general Golgi membrane. GO0070013 directly lists the lumen as an is_a child. GO0030126 identifies COPI coat and GO0035964 defines budding as Golgi membrane evagination. |
| root30-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank, lineage and otherNames | supports | ENA4932 is Saccharomyces cerevisiae at species rank. Qualitative occurrence does not measure population prevalence or prove an exact experimental strain. |
| root30-sources-losev2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1038/nature04717%22; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID16699524, DOI10.1038/nature04717, Golgi maturation visualized in living yeast., Losev E, Reinke CA, Jellen J, Strongin DE, Bevis BJ, Glick BS.. Complete primary abstract reports time-resolved yeast cisternal marker changes and comparison with secretory-cargo pulse-chase kinetics. Actual marker and imaging conditions are checked in the primary body. |
| root30-sources-matsuura2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1038/nature04737%22; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID16699523, DOI10.1038/nature04737, Live imaging of yeast Golgi cisternal maturation., Matsuura-Tokita K, Takeuchi M, Ichihara A, Mikuriya K, Nakano A.. Complete primary abstract reports high-speed3D microscopy of changing yeast cisternal membrane-protein distribution. It does not establish a universal mechanism for all eukaryotes. |
| root30-sources-serafini1991-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/0092-8674%2891%2990176-y%22; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID1680566, DOI10.1016/0092-8674(91)90176-y, ADP-ribosylation factor is a subunit of the coat of Golgi-derived COP-coated vesicles: a novel role for a GTP-binding protein., Serafini T, Orci L, Amherdt M, Brunner M, Kahn RA, Rothman JE.. Complete primary abstract reports ARF enrichment on Golgi-derived coated vesicles, biochemical and morphological localization, GTP-dependent binding and uncoating. It proposes regulation of budding/uncoating; it is not a direct yeast coat-removal assay or a complete mechanochemical proof. |
| root30-sources-losev2006-pdf | https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized-Nature-2006.pdf; Genuine primary PDF mirrored by Kanazawa University; full main text pp1002–1005, Methods and included captions. Reference-only page1006 not used to infer unread experiments. No figure pixels or movie/supplement inspection. | supports | Complete main article pp1002–1005 including Fig1–4 captions and Methods read. Sec7/Vrg4 and additional markers undergo transient labeling; early-to-late transitions and pulse-chase kinetics support cisternal maturation. Cells were imaged at23C; only individually resolved cisternae were quantified. The paper leaves exact recycling pathways and direct cargo tracking for future work. It discusses possible COPI recycling of some SNAREs, which is not the same as measuring every named SNARE role. |
| root30-sources-matsuura2006-pdf | https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized(2)-Nature-2006.pdf; Genuine primary PDF mirrored by Kanazawa University; complete main text and Methods, included Fig1–4 captions; no original pixels, videos or separate supplements. | supports | Complete main article pp1007–1009 plus Methods continuation on1010 read with Fig1–4 captions. Rer1/Gos1 and Sed5/Sec7 fusion-marker changes support yeast maturation; ret1-1 slowed but did not abolish transitions at37C. Functional fusion controls, spatial overlap limits and alternative membrane-transfer mechanisms are retained. No absence of Golgi formation is inferred from coat mutants. |
| root30-sources-papanikou2014-pmc | https://pmc.ncbi.nlm.nih.gov/articles/4130901/; Genuine PMC4130901 numeric-URL body, complete main sectionsS1–S7 and embedded captions; no figure pixels or underlying primary datasets | supports | Complete review main sectionsS1–S7 including Fig1/2 captions read. Supports compartmental enzyme processing, vesicle/tubule traffic and ARF-dependent coat recruitment; three-stage maturation is a proposed organizing model. S4 explicitly leaves aspects of COPI cargo/directionality unresolved. The main text does not discuss SNARE pairing/cycling or the exact SED5/TLG2/SEC22 cohort; its general traffic synthesis cannot be attributed those specific statements. |
| root30-sources-ancestors-GO0000139 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139/ancestors?relations=is_a; Complete native ancestor list, relations=is_a | supports | The complete is_a-only response includes GO0016020 among GO0000139 ancestors, verifying the broader membrane parent transitively without claiming a direct edge. |
| native-verify | /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml --verify; Entire retained native focused output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml --causal-graphs; Entire retained native focused output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/golgi_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/golgi_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/golgi_membrane.yaml --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/golgi_membrane.yaml --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/golgi_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- COMMON denotes qualitative occurrence rather than measured prevalence. Reference-strain protein metadata do not prove that original experiments used that exact strain. Historical authorship and prior issue dispositions are not independently recertified.
- Losev2006 main pp1002–1005/Methods and Matsuura-Tokita2006 main pp1007–1009/Methods continuation1010 were read as genuine primary PDFs, including captions. Figure pixels, movies and separate supplements were not inspected; observed marker exchange does not uniquely establish every cargo-transfer/recycling mechanism.
- Papanikou/Glick2014 is a review; complete mainS1–S7 and embedded captions were inspected, without underlying primary datasets or figure pixels. Its three-stage model and unresolved trafficking questions remain qualified.
- Serafini1991 was read as its complete primary abstract only; publisher access returned403. Mammalian coat-association evidence is not represented as a yeast-specific knockout or isolated mechanochemical sufficiency test.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes review bundles for every uncovered record, including honest no-finding reviews. Maintained scientific content remains unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T015637Z-golgi-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Golgi membrane identity, source and topology review
started_at: '2026-10-22T01:39:31Z'
finished_at: '2026-10-22T01:56:37Z'
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
summary: No concrete curation defect observed within the explicitly bounded source
  scope.
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
  - path: data/structures/membrane_organelle/golgi_apparatus.yaml
    sha256: b064dc1116ec2814e2ecb946d8ebd554a4b176494c2259ff7e458bac0d3e5eb1
    role: context
  - path: data/structures/membrane_organelle/golgi_cisterna.yaml
    sha256: 09ebdf2a8646a8f51638cd933e9523e9e9170e0610567ad3e09efa7a97c6de7a
    role: context
  - path: data/structures/membrane_organelle/golgi_membrane.yaml
    sha256: 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c
    role: target
  - path: data/structures/other/copi_vesicle_coat.yaml
    sha256: 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195
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
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0000139
  path: data/structures/membrane_organelle/golgi_membrane.yaml
  label: Golgi membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_membrane.yaml
    role: maintained scientific record
scope:
  description: 'Entire single target: exact identity, structure/material boundaries,
    source and taxonomic claims, examples, functions and every graph edge.'
  selection: Target 8 of batch thirty in strict uncovered path order from fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000139
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; biological source scope reviewed separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; biological source scope reviewed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: just validate data/structures/membrane_organelle/golgi_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: just validate-strict data/structures/membrane_organelle/golgi_membrane.yaml
    --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0000139
  summary: No expression-module dataset or inference is used. Physical topology, native
    protein identities and microscopy/transport sources are applicable.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000139
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - schema
  - root30-sources-go
  - root30-sources-tax4932
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-serafini1991-meta
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
  - root30-sources-ancestors-GO0000139
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0000139
  summary: 10 of 10 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0000139
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
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_membrane.yaml
  locator: Entire maintained target, including all examples, evidence, graph edges,
    discussions and history
  accessed_at: '2026-10-22T01:49:01Z'
  support: context_only
  summary: Full target read; no scientific record, native status, history or generated
    page is edited.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact structure identity, hierarchy/parthood and narrow source support
  accessed_at: '2026-10-22T01:49:01Z'
  support: context_only
  summary: Whole apparatus, individual cisterna, enclosing bilayer and internal volume
    are separate identities. A source for general trafficking does not establish every
    named molecular mechanism.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent and ProteinExample definitions, essentiality and graph
    representation
  accessed_at: '2026-10-22T01:49:01Z'
  support: context_only
  summary: Protein examples identify taxon-paired instances; membership and formation
    necessity need separate evidence. Label-only collective lipid material is not
    an exact whole-membrane molecular grounding.
- evidence_id: root30-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005794,GO:0043231,GO:0012505,GO:0000139,GO:0031985,GO:0032580,GO:0005796,GO:0070013,GO:0016020,GO:0030126,GO:0035964
  locator: Complete native definitions, names, synonyms, active flags and all returned
    child relations for eleven identifiers
  accessed_at: '2026-10-22T01:41:10.238173Z'
  support: supports
  summary: All eleven active native GO terms were read. Whole GO0005794 is a membrane-bounded
    organelle and part of the endomembrane system; its exact Golgi complex synonym
    and membrane/lumen children agree. GO0031985 is the bounded cisterna, GO0032580
    its membrane, GO0005796 the internal volume, and GO0000139 the general Golgi membrane.
    GO0070013 directly lists the lumen as an is_a child. GO0030126 identifies COPI
    coat and GO0035964 defines budding as Golgi membrane evagination.
  snapshot_sha256: fb5e6b3a9919bf3958eff2c08470766c15c8c1bb4cfe3986d1b702863179c24e
- evidence_id: root30-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-22T01:10:58.502766Z'
  support: supports
  summary: ENA4932 is Saccharomyces cerevisiae at species rank. Qualitative occurrence
    does not measure population prevalence or prove an exact experimental strain.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root30-sources-losev2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/nature04717%22
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:41:12.606096Z'
  support: supports
  summary: Exact MED PMID16699524, DOI10.1038/nature04717, Golgi maturation visualized
    in living yeast., Losev E, Reinke CA, Jellen J, Strongin DE, Bevis BJ, Glick BS..
    Complete primary abstract reports time-resolved yeast cisternal marker changes
    and comparison with secretory-cargo pulse-chase kinetics. Actual marker and imaging
    conditions are checked in the primary body.
  snapshot_sha256: 438af45289e12594bc6c09b8fdcaf9ad230e1399908c29f79c7027d1503d5b5f
- evidence_id: root30-sources-matsuura2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/nature04737%22
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:41:12.638150Z'
  support: supports
  summary: Exact MED PMID16699523, DOI10.1038/nature04737, Live imaging of yeast Golgi
    cisternal maturation., Matsuura-Tokita K, Takeuchi M, Ichihara A, Mikuriya K,
    Nakano A.. Complete primary abstract reports high-speed3D microscopy of changing
    yeast cisternal membrane-protein distribution. It does not establish a universal
    mechanism for all eukaryotes.
  snapshot_sha256: 992411620c5017423ba1f32e69265c4da58b85823dcd9688b293efbb9dfb956e
- evidence_id: root30-sources-serafini1991-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/0092-8674%2891%2990176-y%22
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:41:12.704965Z'
  support: supports
  summary: 'Exact MED PMID1680566, DOI10.1016/0092-8674(91)90176-y, ADP-ribosylation
    factor is a subunit of the coat of Golgi-derived COP-coated vesicles: a novel
    role for a GTP-binding protein., Serafini T, Orci L, Amherdt M, Brunner M, Kahn
    RA, Rothman JE.. Complete primary abstract reports ARF enrichment on Golgi-derived
    coated vesicles, biochemical and morphological localization, GTP-dependent binding
    and uncoating. It proposes regulation of budding/uncoating; it is not a direct
    yeast coat-removal assay or a complete mechanochemical proof.'
  snapshot_sha256: dea8968c03304cd9777691eda5c7ba9969cbd3d2e353a2a5c9ac6ff2ac69538f
- evidence_id: root30-sources-losev2006-pdf
  kind: primary_source
  reference: https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized-Nature-2006.pdf
  locator: Genuine primary PDF mirrored by Kanazawa University; full main text pp1002–1005,
    Methods and included captions. Reference-only page1006 not used to infer unread
    experiments. No figure pixels or movie/supplement inspection.
  accessed_at: '2026-10-22T01:44:30.716438Z'
  support: supports
  summary: Complete main article pp1002–1005 including Fig1–4 captions and Methods
    read. Sec7/Vrg4 and additional markers undergo transient labeling; early-to-late
    transitions and pulse-chase kinetics support cisternal maturation. Cells were
    imaged at23C; only individually resolved cisternae were quantified. The paper
    leaves exact recycling pathways and direct cargo tracking for future work. It
    discusses possible COPI recycling of some SNAREs, which is not the same as measuring
    every named SNARE role.
  snapshot_sha256: 9cd6a98c307575ce19f0b88a5943b10dc7732d655c2b75a9d34228a4fbbc188f
- evidence_id: root30-sources-matsuura2006-pdf
  kind: primary_source
  reference: https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized(2)-Nature-2006.pdf
  locator: Genuine primary PDF mirrored by Kanazawa University; complete main text
    and Methods, included Fig1–4 captions; no original pixels, videos or separate
    supplements.
  accessed_at: '2026-10-22T01:45:15.447608Z'
  support: supports
  summary: Complete main article pp1007–1009 plus Methods continuation on1010 read
    with Fig1–4 captions. Rer1/Gos1 and Sed5/Sec7 fusion-marker changes support yeast
    maturation; ret1-1 slowed but did not abolish transitions at37C. Functional fusion
    controls, spatial overlap limits and alternative membrane-transfer mechanisms
    are retained. No absence of Golgi formation is inferred from coat mutants.
  snapshot_sha256: e0e393bc775432869db495e2a836df223a0be5128ab04aae51a9d31bbf323583
- evidence_id: root30-sources-papanikou2014-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4130901/
  locator: Genuine PMC4130901 numeric-URL body, complete main sectionsS1–S7 and embedded
    captions; no figure pixels or underlying primary datasets
  accessed_at: '2026-10-22T01:44:30.713167Z'
  support: supports
  summary: Complete review main sectionsS1–S7 including Fig1/2 captions read. Supports
    compartmental enzyme processing, vesicle/tubule traffic and ARF-dependent coat
    recruitment; three-stage maturation is a proposed organizing model. S4 explicitly
    leaves aspects of COPI cargo/directionality unresolved. The main text does not
    discuss SNARE pairing/cycling or the exact SED5/TLG2/SEC22 cohort; its general
    traffic synthesis cannot be attributed those specific statements.
  snapshot_sha256: cf70ce9e4c9463c83cad4d05b0c40de9f76ca35a3053d3e5a0c2e2b88dce846a
- evidence_id: root30-sources-ancestors-GO0000139
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139/ancestors?relations=is_a
  locator: Complete native ancestor list, relations=is_a
  accessed_at: '2026-10-22T01:46:17.310722Z'
  support: supports
  summary: The complete is_a-only response includes GO0016020 among GO0000139 ancestors,
    verifying the broader membrane parent transitively without claiming a direct edge.
  snapshot_sha256: c423ff74b8b8b7ad57c67c74cd15a0603fade2086c012fa2e6c23cd5fe928851
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml
    --verify
  locator: Entire retained native focused output
  accessed_at: '2026-10-22T01:41:15.235201Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml
    --causal-graphs
  locator: Entire retained native focused output
  accessed_at: '2026-10-22T01:41:15.680979Z'
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
  reference: just validate data/structures/membrane_organelle/golgi_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:39:33Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/golgi_membrane.yaml'
  snapshot_sha256: 5e75127bcdfe7ca0e162aba4a4f222f4ed2987a4f17575122e43cb82e3a6fe05
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/golgi_membrane.yaml
    --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:39:34Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/golgi_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch30-20261022-frro2xh0/golgi_membrane-strict.tsv"
  snapshot_sha256: 60d5a8cef42b21f4a0862a351b937c37aa75899d64d7ad4d31efa39950f938fc
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/golgi_membrane.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 10 of 10 collected target identifiers returned OK. No residuals. Native
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
- assessment_id: composition
  area: grounding
  topic: Boundary material versus internal volume
  outcome: supported
  target_ids:
  - GO:0000139
  summary: The label-only LIPID row describes collective bilayer material and explicitly
    avoids grounding it to a whole-membrane GO identifier. ESSENTIAL refers to the
    constitutive boundary, not a knockout result for each lipid. No exact species
    mixture or stoichiometry is asserted.
  evidence_ids:
  - record
  - schema
  - root30-sources-go
- assessment_id: identity
  area: identity
  topic: Exact structure and mereology
  outcome: supported
  target_ids:
  - GO:0000139
  summary: Native GO definitions distinguish the Golgi membrane from the individual
    cisterna and associated coat. Recorded synonyms and broader class/parthood statements
    agree with the inspected authority definitions and relations.
  evidence_ids:
  - record
  - policy
  - root30-sources-go
  - root30-sources-ancestors-GO0000139
- assessment_id: scope
  area: scope
  topic: Saccharomyces example and experimental boundaries
  outcome: supported
  target_ids:
  - GO:0000139
  summary: Species4932 is exact. Both imaging papers directly observe budding-yeast
    cisternal marker changes. Unstacked yeast cisternae, microscopy conditions and
    mutant effects are not generalized to all eukaryotic architecture. COMMON remains
    qualitative occurrence.
  evidence_ids:
  - record
  - root30-sources-tax4932
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-serafini1991-meta
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
- assessment_id: function
  area: evidence
  topic: Compartment role and bounded functional evidence
  outcome: supported
  target_ids:
  - GO:0000139
  summary: Membrane boundaries and the stated yeast cisternal context are supported;
    no separate optional function inventory or exact lipid composition is required.
  evidence_ids:
  - record
  - root30-sources-go
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-serafini1991-meta
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
- assessment_id: graph
  area: graph
  topic: All target graph edges
  outcome: supported
  target_ids:
  - GO:0000139
  summary: All four NONMECHANISTIC edges describe membrane parthood/enclosure and
    COPI coat participation in budding. Native GO0035964 establishes Golgi membrane
    evagination; Serafini provides coat/ARF association and the separately read review
    provides recruitment/traffic context. The graph does not specify an isolated force-generation
    experiment, exclusive coat sufficiency or a full biochemical mechanism.
  evidence_ids:
  - record
  - root30-sources-go
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-serafini1991-meta
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
  - root30-sources-ancestors-GO0000139
- assessment_id: limits
  area: evidence
  topic: Molecular requirements and complete inventories
  outcome: unknown
  target_ids:
  - GO:0000139
  summary: An exact lipid composition, exhaustive machinery inventory and molecular
    formation-necessity tests are not established by these sources. Native protein
    identity and generic function annotations are distinguished from direct localization
    assays and from cisternal-maturation experiments.
  evidence_ids:
  - record
  - schema
  - root30-sources-go
  - root30-sources-losev2006-pdf
  - root30-sources-matsuura2006-pdf
  - root30-sources-papanikou2014-pmc
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and bounded source tiers
  outcome: supported
  target_ids:
  - GO:0000139
  summary: Full target, every graph edge, discussion and history entry were read.
    No maintained image asset, numeric physical property, trait link or verbatim snippet
    is asserted. PROPOSED status is retained. Empty optional slots and inaccessible
    bodies alone are not findings.
  evidence_ids:
  - record
  - policy
  - root30-sources-go
  - root30-sources-losev2006-meta
  - root30-sources-matsuura2006-meta
  - root30-sources-serafini1991-meta
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- COMMON denotes qualitative occurrence rather than measured prevalence. Reference-strain
  protein metadata do not prove that original experiments used that exact strain.
  Historical authorship and prior issue dispositions are not independently recertified.
- Losev2006 main pp1002–1005/Methods and Matsuura-Tokita2006 main pp1007–1009/Methods
  continuation1010 were read as genuine primary PDFs, including captions. Figure pixels,
  movies and separate supplements were not inspected; observed marker exchange does
  not uniquely establish every cargo-transfer/recycling mechanism.
- Papanikou/Glick2014 is a review; complete mainS1–S7 and embedded captions were inspected,
  without underlying primary datasets or figure pixels. Its three-stage model and
  unresolved trafficking questions remain qualified.
- Serafini1991 was read as its complete primary abstract only; publisher access returned403.
  Mammalian coat-association evidence is not represented as a yeast-specific knockout
  or isolated mechanochemical sufficiency test.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorizes review bundles for every uncovered record, including
  honest no-finding reviews. Maintained scientific content remains unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
