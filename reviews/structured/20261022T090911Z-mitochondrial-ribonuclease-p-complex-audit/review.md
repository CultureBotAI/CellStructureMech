# Source-grounded review of mitochondrial ribonuclease P complex

- Review: 20261022T090911Z-mitochondrial-ribonuclease-p-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T08:39:44Z
- Finished UTC: 2026-10-22T09:09:11Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: exact mitochondrial RNase P identity, species-variable scope and the nonmechanistic tRNA-processing graph are supported. Component architectures remain an explicitly bounded curation task.

## Scope And Provenance

Exactly one complete maintained target, with source tiers and experimental limits stated separately.

Selection: One complete record in strict-path batch61 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030678 | data/structures/other/mitochondrial_ribonuclease_p_complex.yaml | maintained | mitochondrial ribonuclease P complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030678 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030678 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0030678 | Focused native check passed; scientific claims assessed separately. |
| Native focused verify | passed | True | GO:0030678 | Focused native check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0030678 | No expression-module membership claim is assessed. Native protein/complex authorities and primary structure or binding evidence address these records; transcriptomic co-membership would not establish their assembly. |
| Claim-level scientific review | passed | True | GO:0030678 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030678 | 6 of 8 collected target identifiers returned OK. PMID:12045094: UNREACHABLE; Native Europe PMC uniquely identifies PMID:12045094: Eukaryotic ribonuclease P: a plurality of ribonucleoprotein enzymes. (2002), DOI10.1146/annurev.biochem.71.110601.135352. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:27187488: UNREACHABLE; Native Europe PMC uniquely identifies PMID:27187488: The Diversity of Ribonuclease P: Protein and RNA Catalysts with Analogous Biological Functions. (2016), DOI10.3390/biom6020027. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030678 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030678 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030678 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030678 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030678 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact mitochondrial RNase P complex with heterogeneous architecture

identity: supported. Targets: GO:0030678.

GO0030678, exact synonym and both typed is_a parents agree with the target. The older parent RNP wording is not extended into a claim that all mitochondrial forms contain RNA. OTHER kind avoids a universal protein-only architecture.

### Explicit species-variable constituent boundary

completeness: supported. Targets: GO:0030678.

The open discussion accurately defers distinct fungal RNA-plus-protein and human protein-only inventories. It does not claim exact families do not exist. Optional missing component rows alone are not a defect, and a three-protein-class statement is not treated as a three-molecule copy count.

### Nonmechanistic location and cleavage function

graph: supported. Targets: GO:0030678.

All four graph edges preserve mitochondrial localization and precursor-tRNA 5-prime leader removal without a species-universal mechanism or assembly requirement. GO activity/process meanings and the inspected synthesis support this limited function.

### Complete target and explicit access limits

completeness: supported. Targets: GO:0030678.

Every maintained field, history entry, discussion and graph edge was read. Optional empty slots and acknowledged scientific uncertainty alone do not generate findings. Source claims remain limited to their declared reading scopes.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/mitochondrial_ribonuclease_p_complex.yaml; Entire maintained YAML, history, evidence and discussions | context_only | The full target was read after native inspection. This maintained YAML owns any scientific correction. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent grounding and essentiality, EssentialityEnum, graph scope | context_only | Exact class grounding can use InterPro, Pfam or NCBIfam. REVIEWED_LABEL_ONLY means no exact family can be asserted. Formation necessity differs from activity; DISPENSABLE permits defective assembly. Optional empty fields alone are not defects. |
| curation | docs/CURATION.md; Exact component identity and evidence placement | context_only | Taxon-neutral constituent classes, reference proteins and physical assembly evidence are separate claims. Source scope and real uncertainty must be retained. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Actor, direction, mechanistic status and evidence scope | context_only | Direct binding, static structure, functional perturbation and proposed conformational mechanisms provide distinct levels of evidence. |
| protein-guidance | .claude/skills/uniprot-protein-examples/SKILL.md; Exact gene match, reviewed entry, native taxonomy and external graph actor rules | context_only | Each selected accession is paired with its own taxon and gene tokens. A reviewed entry does not independently prove complex membership. |
| root61-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000987,GO:0001682,GO:0004526,GO:0005667,GO:0005739,GO:0015914,GO:0030151,GO:0030677,GO:0030678,GO:0043190,GO:0098798,GO:1990198; All12 exact identities, definitions, synonyms, aspects, comments and typed children | supports | The exact active GO definitions, synonym qualifiers and typed children support the declared complex identities, functions and parentage. GO0043190 is a broader ABC transporter class rather than an exact MlaFEDB identity; mitochondrial RNase P has both declared is_a parents and mitochondrial parthood. |
| root61-sources-pmid-12045094 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12045094+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText | supports | Unique MED12045094: Eukaryotic ribonuclease P: a plurality of ribonucleoprotein enzymes. (2002); DOI10.1146/annurev.biochem.71.110601.135352. Complete available abstract and native bibliography were read. Primary-body inspection is limited to separately declared sources. |
| root61-sources-pmid-27187488 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27187488+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText | supports | Unique MED27187488: The Diversity of Ribonuclease P: Protein and RNA Catalysts with Analogous Biological Functions. (2016); DOI10.3390/biom6020027. Complete available abstract and native bibliography were read. Primary-body inspection is limited to separately declared sources. |
| root61-sources-PMC4919922-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4919922/fullTextXML; Genuine JATS complete sec1,sec2dot1,sec2dot2,sec3dot3 text and full permissions; other sections, figure pixels, separately placed tables/captions and cited primary bodies not read. This is a review, not a primary experiment. | supports | Klemm2016 reviews species-variable mitochondrial RNase P: fungal RPM1 RNA with at least one RPM2 protein, human MRPP1/2/3 protein-only machinery, and independently active plant/trypanosome single-protein enzymes. Three human protein classes are not a proven total three-molecule stoichiometry. The current target represents the complex class, not every enzyme with RNase P activity. |
| access-PMC3759807-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3759807/fullTextXML; Transport/access response only; no primary-body evidence | context_only | Xiao2002 XML returnedHTTP500; the PMID bibliography and complete abstract were read separately. |
| access-PMC3759807-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC3759807/?_escaped_fragment_=; Transport/access response only; no primary-body evidence | context_only | The legacy PMC response was a recaptcha access page despiteHTTP200; no primary article body was read from it. |
| schema-result | just validate data/structures/other/mitochondrial_ribonuclease_p_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/mitochondrial_ribonuclease_p_complex.yaml |
| strict-result | just validate-strict data/structures/other/mitochondrial_ribonuclease_p_complex.yaml --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mitochondrial_ribonuclease_p_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/mitochondrial_ribonuclease_p_complex.yaml --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mitochondrial_ribonuclease_p_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mitochondrial_ribonuclease_p_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_ribonuclease_p_complex.yaml --causal-graphs; Complete focused native report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_ribonuclease_p_complex.yaml --verify; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/mitochondrial_ribonuclease_p_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 6 of 8 collected target identifiers returned OK. PMID:12045094: UNREACHABLE; Native Europe PMC uniquely identifies PMID:12045094: Eukaryotic ribonuclease P: a plurality of ribonucleoprotein enzymes. (2002), DOI10.1146/annurev.biochem.71.110601.135352. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope.; PMID:27187488: UNREACHABLE; Native Europe PMC uniquely identifies PMID:27187488: The Diversity of Ribonuclease P: Protein and RNA Catalysts with Analogous Biological Functions. (2016), DOI10.3390/biom6020027. Identifier/bibliographic verification is separate from the declared body or abstract scientific-reading scope. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five same-base batch26 corpus gates and exact target resolver rows are integrated with every manifested input hash verified.
- Klemm2016 was read only in the listed review sections. Xiao2002 is complete-abstract/bibliography tier; failed XML and challenge-page responses are retained without claiming full-text access.
- No primary reconstitution, raw enzymology, figure pixels or species-wide prevalence survey was independently reanalysed. Different mitochondrial RNase P architectures and single-protein activities must remain distinct.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- Explicit all-record goal authorizes issue-bearing and qualified clean observations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T090911Z-mitochondrial-ribonuclease-p-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of mitochondrial ribonuclease P complex
started_at: '2026-10-22T08:39:44Z'
finished_at: '2026-10-22T09:09:11Z'
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
summary: 'Qualified pass: exact mitochondrial RNase P identity, species-variable scope
  and the nonmechanistic tRNA-processing graph are supported. Component architectures
  remain an explicitly bounded curation task.'
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
  - path: data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
    sha256: 00c2bfe5567576213bd36b0ac68169c143c04f1a677e96f4b4bc2dbf4b78dd5c
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
- target_id: GO:0030678
  path: data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
  label: mitochondrial ribonuclease P complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, with source tiers and experimental
    limits stated separately.
  selection: One complete record in strict-path batch61 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030678
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030678
  command: just validate data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030678
  command: just validate-strict data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
    --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mitochondrial_ribonuclease_p_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030678
  command: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0030678
  command: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030678
  summary: No expression-module membership claim is assessed. Native protein/complex
    authorities and primary structure or binding evidence address these records; transcriptomic
    co-membership would not establish their assembly.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030678
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - protein-guidance
  - root61-sources-go
  - root61-sources-pmid-12045094
  - root61-sources-pmid-27187488
  - root61-sources-PMC4919922-xml
  - access-PMC3759807-xml
  - access-PMC3759807-legacy
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030678
  summary: '6 of 8 collected target identifiers returned OK. PMID:12045094: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:12045094: Eukaryotic ribonuclease P:
    a plurality of ribonucleoprotein enzymes. (2002), DOI10.1146/annurev.biochem.71.110601.135352.
    Identifier/bibliographic verification is separate from the declared body or abstract
    scientific-reading scope.; PMID:27187488: UNREACHABLE; Native Europe PMC uniquely
    identifies PMID:27187488: The Diversity of Ribonuclease P: Protein and RNA Catalysts
    with Analogous Biological Functions. (2016), DOI10.3390/biom6020027. Identifier/bibliographic
    verification is separate from the declared body or abstract scientific-reading
    scope. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root61-sources-pmid-12045094
  - root61-sources-pmid-27187488
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030678
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch61 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0030678
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch61 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0030678
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch61 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0030678
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch61 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0030678
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
    and current batch61 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
  locator: Entire maintained YAML, history, evidence and discussions
  accessed_at: '2026-10-22T08:54:23Z'
  support: context_only
  summary: The full target was read after native inspection. This maintained YAML
    owns any scientific correction.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent grounding and essentiality, EssentialityEnum, graph
    scope
  accessed_at: '2026-10-22T08:54:23Z'
  support: context_only
  summary: Exact class grounding can use InterPro, Pfam or NCBIfam. REVIEWED_LABEL_ONLY
    means no exact family can be asserted. Formation necessity differs from activity;
    DISPENSABLE permits defective assembly. Optional empty fields alone are not defects.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact component identity and evidence placement
  accessed_at: '2026-10-22T08:54:23Z'
  support: context_only
  summary: Taxon-neutral constituent classes, reference proteins and physical assembly
    evidence are separate claims. Source scope and real uncertainty must be retained.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Actor, direction, mechanistic status and evidence scope
  accessed_at: '2026-10-22T08:54:23Z'
  support: context_only
  summary: Direct binding, static structure, functional perturbation and proposed
    conformational mechanisms provide distinct levels of evidence.
- evidence_id: protein-guidance
  kind: record_content
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Exact gene match, reviewed entry, native taxonomy and external graph actor
    rules
  accessed_at: '2026-10-22T08:54:23Z'
  support: context_only
  summary: Each selected accession is paired with its own taxon and gene tokens. A
    reviewed entry does not independently prove complex membership.
- evidence_id: root61-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000987,GO:0001682,GO:0004526,GO:0005667,GO:0005739,GO:0015914,GO:0030151,GO:0030677,GO:0030678,GO:0043190,GO:0098798,GO:1990198
  locator: All12 exact identities, definitions, synonyms, aspects, comments and typed
    children
  accessed_at: '2026-10-22T08:29:00.675261Z'
  support: supports
  summary: The exact active GO definitions, synonym qualifiers and typed children
    support the declared complex identities, functions and parentage. GO0043190 is
    a broader ABC transporter class rather than an exact MlaFEDB identity; mitochondrial
    RNase P has both declared is_a parents and mitochondrial parthood.
  snapshot_sha256: 5d713c2404c3cdfab2cb949ad07b8dba27fbfc24e80b2bf6cce22e4878cf5726
- evidence_id: root61-sources-pmid-12045094
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12045094+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText
  accessed_at: '2026-10-22T08:29:03.624358Z'
  support: supports
  summary: 'Unique MED12045094: Eukaryotic ribonuclease P: a plurality of ribonucleoprotein
    enzymes. (2002); DOI10.1146/annurev.biochem.71.110601.135352. Complete available
    abstract and native bibliography were read. Primary-body inspection is limited
    to separately declared sources.'
  snapshot_sha256: ba715f1413ce641d5f174319368032ec82151ff0105ce7662d4827fff9ea9cbb
- evidence_id: root61-sources-pmid-27187488
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27187488+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText
  accessed_at: '2026-10-22T08:29:04.232642Z'
  support: supports
  summary: 'Unique MED27187488: The Diversity of Ribonuclease P: Protein and RNA Catalysts
    with Analogous Biological Functions. (2016); DOI10.3390/biom6020027. Complete
    available abstract and native bibliography were read. Primary-body inspection
    is limited to separately declared sources.'
  snapshot_sha256: d46b0fa93e13a379d50cc2e2997e1041cebf3324baa3c00508c77e84c704948a
- evidence_id: root61-sources-PMC4919922-xml
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4919922/fullTextXML
  locator: Genuine JATS complete sec1,sec2dot1,sec2dot2,sec3dot3 text and full permissions;
    other sections, figure pixels, separately placed tables/captions and cited primary
    bodies not read. This is a review, not a primary experiment.
  accessed_at: '2026-10-22T08:29:43.126017Z'
  support: supports
  summary: 'Klemm2016 reviews species-variable mitochondrial RNase P: fungal RPM1
    RNA with at least one RPM2 protein, human MRPP1/2/3 protein-only machinery, and
    independently active plant/trypanosome single-protein enzymes. Three human protein
    classes are not a proven total three-molecule stoichiometry. The current target
    represents the complex class, not every enzyme with RNase P activity.'
  snapshot_sha256: 08c68dc5f90b540aa6156fa35675c88cb78f123133cdda281c3e1203a8ffd6f2
- evidence_id: access-PMC3759807-xml
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3759807/fullTextXML
  locator: Transport/access response only; no primary-body evidence
  accessed_at: '2026-10-22T08:29:43.125750Z'
  support: context_only
  summary: Xiao2002 XML returnedHTTP500; the PMID bibliography and complete abstract
    were read separately.
  snapshot_sha256: 84a0929041ce472e4bf48d93d670ae9d624bf85a5aea19a8c42a28814ae394ef
- evidence_id: access-PMC3759807-legacy
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3759807/?_escaped_fragment_=
  locator: Transport/access response only; no primary-body evidence
  accessed_at: '2026-10-22T08:35:29.325944Z'
  support: context_only
  summary: The legacy PMC response was a recaptcha access page despiteHTTP200; no
    primary article body was read from it.
  snapshot_sha256: 002763de887b4c93e131755ffecdbd2de4f3c12c71ec95864e28dd0425c718c0
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T08:39:46Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/mitochondrial_ribonuclease_p_complex.yaml'
  snapshot_sha256: 5c57044a638fd1951a4a5d8d0b1ebb677706455a7237067e3aadcb9303e5a1eb
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
    --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mitochondrial_ribonuclease_p_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T08:39:47Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/mitochondrial_ribonuclease_p_complex.yaml\
    \ --out /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mitochondrial_ribonuclease_p_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch61-20261022-t_eoxa78/mitochondrial_ribonuclease_p_complex-strict.tsv"
  snapshot_sha256: 468dd545bc9e5e23bf6278029b325b151ec20ae49208fa3757d033808e774872
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
    --causal-graphs
  locator: Complete focused native report
  accessed_at: '2026-10-22T08:46:26.215403Z'
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
  reference: /private/tmp/cellstructure-batch61-20261022-t_eoxa78/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_ribonuclease_p_complex.yaml
    --verify
  locator: Complete focused native report
  accessed_at: '2026-10-22T08:46:26.608620Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/mitochondrial_ribonuclease_p_complex.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '6 of 8 collected target identifiers returned OK. PMID:12045094: UNREACHABLE;
    Native Europe PMC uniquely identifies PMID:12045094: Eukaryotic ribonuclease P:
    a plurality of ribonucleoprotein enzymes. (2002), DOI10.1146/annurev.biochem.71.110601.135352.
    Identifier/bibliographic verification is separate from the declared body or abstract
    scientific-reading scope.; PMID:27187488: UNREACHABLE; Native Europe PMC uniquely
    identifies PMID:27187488: The Diversity of Ribonuclease P: Protein and RNA Catalysts
    with Analogous Biological Functions. (2016), DOI10.3390/biom6020027. Identifier/bibliographic
    verification is separate from the declared body or abstract scientific-reading
    scope. Native source checks are separately scoped; skipped or unreachable identifiers
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
  topic: Exact mitochondrial RNase P complex with heterogeneous architecture
  outcome: supported
  target_ids:
  - GO:0030678
  summary: GO0030678, exact synonym and both typed is_a parents agree with the target.
    The older parent RNP wording is not extended into a claim that all mitochondrial
    forms contain RNA. OTHER kind avoids a universal protein-only architecture.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - protein-guidance
  - root61-sources-go
  - root61-sources-PMC4919922-xml
  - root61-sources-pmid-12045094
  - root61-sources-pmid-27187488
- assessment_id: composition
  area: completeness
  topic: Explicit species-variable constituent boundary
  outcome: supported
  target_ids:
  - GO:0030678
  summary: The open discussion accurately defers distinct fungal RNA-plus-protein
    and human protein-only inventories. It does not claim exact families do not exist.
    Optional missing component rows alone are not a defect, and a three-protein-class
    statement is not treated as a three-molecule copy count.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - protein-guidance
  - root61-sources-go
  - root61-sources-PMC4919922-xml
- assessment_id: graph
  area: graph
  topic: Nonmechanistic location and cleavage function
  outcome: supported
  target_ids:
  - GO:0030678
  summary: All four graph edges preserve mitochondrial localization and precursor-tRNA
    5-prime leader removal without a species-universal mechanism or assembly requirement.
    GO activity/process meanings and the inspected synthesis support this limited
    function.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - protein-guidance
  - root61-sources-go
  - root61-sources-PMC4919922-xml
- assessment_id: coverage
  area: completeness
  topic: Complete target and explicit access limits
  outcome: supported
  target_ids:
  - GO:0030678
  summary: Every maintained field, history entry, discussion and graph edge was read.
    Optional empty slots and acknowledged scientific uncertainty alone do not generate
    findings. Source claims remain limited to their declared reading scopes.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - protein-guidance
  - root61-sources-go
  - root61-sources-PMC4919922-xml
findings: []
actions: []
limitations:
- All five same-base batch26 corpus gates and exact target resolver rows are integrated
  with every manifested input hash verified.
- Klemm2016 was read only in the listed review sections. Xiao2002 is complete-abstract/bibliography
  tier; failed XML and challenge-page responses are retained without claiming full-text
  access.
- No primary reconstitution, raw enzymology, figure pixels or species-wide prevalence
  survey was independently reanalysed. Different mitochondrial RNase P architectures
  and single-protein activities must remain distinct.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- Explicit all-record goal authorizes issue-bearing and qualified clean observations.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
