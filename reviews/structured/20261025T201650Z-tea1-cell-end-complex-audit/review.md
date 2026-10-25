# Tea1 cell-end complex — source-grounded record review

- Review: 20261025T201650Z-tea1-cell-end-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-25T19:59:50Z
- Finished UTC: 2026-10-25T20:16:50.962229Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Tea1 complex identity and core polarity function are supported. Five findings concern broad Tea1/Tea3 groundings, contextual Tea3 membership, a misattributed paper, Tea1 formation dispensability, and unsupported genus-level prevalence.

## Scope And Provenance

One complete maintained record; all populated scientific fields and graph edges assessed with the exact source tiers below.

Selection: Final8 unreviewed records in repository-relative path order after validated current-main and published-batch coverage reconciliation; one record per bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1497f644d59655f087825054920ef1a99ddebce4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031500 | data/structures/other/tea1_cell_end_complex.yaml | maintained | Tea1 cell-end complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native focused schema | passed | True | GO:0031500 | Native check passed; scientific assertions assessed separately. |
| Native focused strict | passed | True | GO:0031500 | Native check passed; scientific assertions assessed separately. |
| Current-base native corpus history | passed | True | GO:0031500 | Native append-only history validation passed for2065 history files. |
| Current-base native corpus products | passed | True | GO:0031500 | Native corpus ID-label validator returned0; it does not prove class-level identity or support biological scope. |
| Current-base native corpus traits | passed | True | GO:0031500 | All10 trait links matched the freshly obtained TraitMech index. This target has no asserted trait links. |
| Current-base native corpus curies | passed | True | GO:0031500 | Native corpus resolver returned0:6105 identifiers,4997 OK,856 UNREACHABLE,252 SKIPPED. BFO authority control was not exercised because unreachable. Native exit0 is not universal resolution; target source-native checks and limitations are recorded separately. |
| Current-base native corpus qc | passed | True | GO:0031500 | Full current-base native QC passed; review-only additions are checked separately after saving. Scientific content was unchanged. |
| Target native identifiers and residual reconciliation | passed | True | GO:0031500 | All target identifiers verified at native source level; source support assessed separately from identifier existence. |
| Claim-level source review | passed | True | GO:0031500 | Complete target assessed against source-native identities, cited primary text at declared tiers, and explicit experimental limitations; unresolved curation findings are preserved. |
| Native expression-dataset applicability check | passed | False | GO:0031500 | The native dataset-list command ran successfully. No dataset matches the exact named organisms, so downstream target-gene queries are not applicable. Listing absence is not biological absence; expression-module membership would not establish physical assembly. |

## Scientific And Domain Assessments

### Tea1-defined cell-end polarity assembly

identity: supported. Targets: GO:0031500.

GO identity, microtubule-associated-complex parent and polarisome parthood are supported. The source definition typo is inherited from GO and does not alter identity. The entity is a complex class, not an isolated Tea1 protein.

### Family boundaries and reference proteins

grounding: concern. Targets: GO:0031500.

Tea4 has a native family identity and exact reviewed protein. Tea1/Tea3 use a broad Kelch-type homologous superfamily as exact class identity, although their protein examples and gene synonyms are correct.

### State-dependent cortical organization

graph: concern. Targets: GO:0031500.

All four graph edges were assessed. The role already specifies non-growing ends, but omits the distinct cell-cycle context of Tea3 association with Tea1 assemblies. Tea1 and Tea4 effects on assembly remain distinct from viability.

### Species evidence versus genus prevalence

scope: concern. Targets: GO:0031500.

Native Schizosaccharomyces and strain972h- identities agree. The cited Mata experiment addresses S. pombe, so COMMON across the genus requires additional evidence; verified strain reference proteins alone do not establish the original experimental isolate.

### Populated fields and maintained ownership

completeness: supported. Targets: GO:0031500.

All target fields were read. No images, physical-property measurements, source compositions or trait links are asserted in this target; their optional absence is not a finding. Native PROPOSED status and an LLM-assisted creation event are appropriate. Future edits belong to the maintained YAML and require curation/history gates.

## Findings

### F1: Tea1 and Tea3 are grounded to a broad structural superfamily

major / open / confirmed; issue key: tea1-cell-end-complex-kelch-superfamily-groundings.

IPR015915 is the Kelch-type beta-propeller homologous superfamily, not an exact Tea1 or Tea3 protein-family identity. Both component and graph-node groundings inherit this mismatch.

### F2: Tea3 association needs cell-cycle context

minor / open / confirmed; issue key: tea1-cell-end-complex-tea3-assembly-context.

The Tea3 role already specifies non-growing cell ends. Dodgson found that growing-versus-nongrowing position did not explain Tea1–Tea3 cluster correlation, whereas mitosis increased association and made Tea3 important for Tea1 retention. Add this phase dependence to the anchoring role and graph; CONSTITUENT alone does not assert invariant coassembly.

### F3: The Tea3 citation has the wrong author attribution

minor / open / confirmed; issue key: tea1-cell-end-complex-paper-attribution.

PMID14663827 and DOI10.1002/yea.1054 identify the 2003 Niccoli, Arellano and Nurse study, not Snaith and Sawin. Its abstract reports comparative growth/microtubule phenotypes; do not use that abstract alone as proof of direct biochemical interaction.

### F4: Tea1 dispensability is unsupported for the named assembly

minor / open / confirmed; issue key: tea1-cell-end-complex-tea1-formation-necessity.

Tea1 is the defining scaffold but is marked DISPENSABLE for formation. Martin reports loss of Tea4 localization and loss of the Tip1–Tea4 association in tea1 deletion cells. Viability and remaining polarity factors do not establish persistence of the named Tea1 assembly.

### F5: Genus-wide COMMON occurrence is not established by the cited study

minor / open / confirmed; issue key: tea1-cell-end-complex-genus-prevalence.

The distribution uses COMMON for Schizosaccharomyces but cites a study confined to S. pombe. Neither the reference protein strain nor genus membership supplies evidence of frequent occurrence across species.

## Recommended Actions And Acceptance Checks

### A1

Use independently verified class-specific families where available or justified label-only representations; retain correct UniProt examples and keep graph references consistent.

- Verify the corrected claim against its exact native identifier or primary source and retain experimental scope.
- After separately authorized curation, run focused schema/strict checks, product correspondence, history validation and full QC; preserve PROPOSED status.

### A2

Retain the supported Tea3 association while adding the experimentally distinguished cell-cycle context to its anchoring role and graph. Reassess constituent versus associated-machinery representation with an explicit complex boundary.

- Verify the corrected claim against its exact native identifier or primary source and retain experimental scope.
- After separately authorized curation, run focused schema/strict checks, product correspondence, history validation and full QC; preserve PROPOSED status.

### A3

Correct the author attribution and tie interaction-specific wording to an inspected interaction experiment, keeping genetic/localization evidence distinct.

- Verify the corrected claim against its exact native identifier or primary source and retain experimental scope.
- After separately authorized curation, run focused schema/strict checks, product correspondence, history validation and full QC; preserve PROPOSED status.

### A4

Reassess Tea1 formation necessity for the exact complex boundary. Do not equate viability with structural dispensability; qualify other component necessity separately.

- Verify the corrected claim against its exact native identifier or primary source and retain experimental scope.
- After separately authorized curation, run focused schema/strict checks, product correspondence, history validation and full QC; preserve PROPOSED status.

### A5

Constrain the distribution to the demonstrated organism or cite an appropriate comparative source for genus-level occurrence.

- Verify the corrected claim against its exact native identifier or primary source and retain experimental scope.
- After separately authorized curation, run focused schema/strict checks, product correspondence, history validation and full QC; preserve PROPOSED status.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/tea1_cell_end_complex.yaml; Complete maintained YAML; all fields, graph nodes/edges and curation history | context_only | Complete target read after native inspect. Scientific changes belong to this maintained YAML; no record or generated product was changed. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000133,GO:0000910,GO:0000916,GO:0005875,GO:0005935,GO:0007163,GO:0031500,GO:0032991,GO:0120155; Complete selected term responses; child arrays of asserted parents/parthood containers | supports | Exact active GO identities, definitions, synonyms and child-to-parent typed relationships inspected; functions denote biological processes, not complexes. |
| ipr-IPR015915 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR015915/; Complete native metadata identity/type/name; description authoring status | supports | Native IPR015915 is Kelch-type beta-propeller of type homologous_superfamily. The identifier, type and name establish this entry’s scope. Accession-specific membership is recorded separately in the cited UniProt responses; descriptive prose is not experimental evidence. |
| ipr-IPR053039 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR053039/; Complete native metadata identity/type/name; description authoring status | supports | Native IPR053039 is Cell polarity protein Bud14/Tea4 of type family. The identifier, type and name establish this entry’s scope. Accession-specific membership is recorded separately in the cited UniProt responses; descriptive prose is not experimental evidence. |
| protein-P87061 | https://rest.uniprot.org/uniprotkb/P87061.json; Native reviewed entry identity/names/genes/taxon, comments, InterPro and publication references | supports | Reviewed P87061 names the declared gene and synonyms in taxon284812. Full native identity, protein name, gene list, taxon, function/subunit comments and cited-paper provenance were read; reference-strain accession is distinct from the strain used in a cited experiment. |
| protein-O14248 | https://rest.uniprot.org/uniprotkb/O14248.json; Native reviewed entry identity/names/genes/taxon, comments, InterPro and publication references | supports | Reviewed O14248 names the declared gene and synonyms in taxon284812. Full native identity, protein name, gene list, taxon, function/subunit comments and cited-paper provenance were read; reference-strain accession is distinct from the strain used in a cited experiment. |
| protein-O60132 | https://rest.uniprot.org/uniprotkb/O60132.json; Native reviewed entry identity/names/genes/taxon, comments, InterPro and publication references | supports | Reviewed O60132 names the declared gene and synonyms in taxon284812. Full native identity, protein name, gene list, taxon, function/subunit comments and cited-paper provenance were read; reference-strain accession is distinct from the strain used in a cited experiment. |
| tax-4895 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4895; Entire ENA native taxonomy response | supports | NCBI taxon4895 is Schizosaccharomyces at rank genus; lineage inspected. Taxonomic identity alone does not establish prevalence. |
| tax-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Entire ENA native taxonomy response | supports | NCBI taxon284812 is Schizosaccharomyces pombe 972h- at rank strain; lineage inspected. Taxonomic identity alone does not establish prevalence. |
| pmid-9200612 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9200612+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identifier, complete bibliography/abstractText and full-text routes | supports | Exact PMID9200612: Mata J, Nurse P. tea1 and the microtubular cytoskeleton are important for generating global spatial order within the fission yeast cell. DOI:10.1016/s0092-8674(00)80279-2. Complete abstract and bibliography read; no uninspected methods or figures are inferred from the abstract. |
| pmid-12007420 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12007420+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identifier, complete bibliography/abstractText and full-text routes | supports | Exact PMID12007420: Arellano M, Niccoli T, Nurse P. Tea3p is a cell end marker activating polarized growth in Schizosaccharomyces pombe. DOI:10.1016/s0960-9822(02)00821-7. Complete abstract and bibliography read; no uninspected methods or figures are inferred from the abstract. |
| pmid-14663827 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14663827+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identifier, complete bibliography/abstractText and full-text routes | supports | Exact PMID14663827: Niccoli T, Arellano M, Nurse P. Role of Tea1p, Tea3p and Pom1p in the determination of cell ends in Schizosaccharomyces pombe. DOI:10.1002/yea.1054. Complete abstract and bibliography read; no uninspected methods or figures are inferred from the abstract. |
| pmid-15936270 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15936270+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identifier, complete bibliography/abstractText and full-text routes | supports | Exact PMID15936270: Tatebe H, Shimada K, Uzawa S, Morigasaki S, Shiozaki K. Wsh3/Tea4 is a novel cell-end factor essential for bipolar distribution of Tea1 and protects cell polarity under environmental stress in S. pombe. DOI:10.1016/j.cub.2005.04.061. Complete abstract and bibliography read; no uninspected methods or figures are inferred from the abstract. |
| pmid-15809031 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15809031%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identifier, complete bibliography/abstractText and full-text routes | supports | Exact PMID15809031: Martin SG, McDonald WH, Yates JR, Chang F. Tea4p links microtubule plus ends with the formin for3p in the establishment of cell polarity. DOI:10.1016/j.devcel.2005.02.008. Complete abstract and bibliography read; no uninspected methods or figures are inferred from the abstract. |
| Tea2005-author-pdf | https://www.columbia.edu/cu/biology/dept/seminarPDFfiles/Martin%20Dev%2C%20Fred%20ChangCell05.pdf; Author-hosted primary PDF pages480–489: identification/localization, Tea4–For3 binding, linking and additional-functions sections; page489 strain-method paragraph. Figure1/2/4 captions as extracted; no image pixels or supplementary strain table. | supports | Martin2005 demonstrates direct Tea1–Tea4 and Tea4–For3 binding, with Tea4 bridging Tea1–For3. Deleting tea1 disperses Tea4; deleting tea4 preserves some Tea1 assemblies but removes this connection. |
| PMC3674234-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3674234/fullTextXML; Genuine JATS complete Results and Discussion; Methods strain and frontal-imaging subsections. Supplementary files, pixels and unlisted Methods were not inspected. | supports | Dodgson2013 distinguishes Tea1/Tea4 clusters from nearby Tea3 clusters during growth; association increases during mitosis, when Tea3 aids Tea1 retention. Forced persistent Tea1–Tea3 proximity disrupts polarity. |
| ro2436-go | https://www.ebi.ac.uk/ols4/api/ontologies/go/properties?obo_id=RO:0002436; Exact OLS property response including label and definition | supports | RO:0002436 is molecularly interacts with: a direct physical interaction between molecular entities. This relation identity does not itself verify a component-specific contact. |
| ro2213-go | https://www.ebi.ac.uk/ols4/api/ontologies/go/properties?obo_id=RO:0002213; Exact OLS property response including label and definition | supports | RO:0002213 is positively regulates: regulation increasing the rate or magnitude of a process. Its identity does not itself prove the stated biological effect. |
| schema-result | just validate data/structures/other/tea1_cell_end_complex.yaml; Complete focused native validator output | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/tea1_cell_end_complex.yaml |
| strict-result | just validate-strict data/structures/other/tea1_cell_end_complex.yaml --out /private/tmp/cellstructure-batch62-20261025-siz_24tk/tea1_cell_end_complex-strict.tsv; Complete focused native validator output | supports | uv run python scripts/validate_strict.py data/structures/other/tea1_cell_end_complex.yaml --out /private/tmp/cellstructure-batch62-20261025-siz_24tk/tea1_cell_end_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch62-20261025-siz_24tk/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch62-20261025-siz_24tk/tea1_cell_end_complex-strict.tsv |
| final-global-history | just validate-history; Exact current-base history stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Native append-only history validation passed for2065 history files. |
| final-global-products | just validate-products; Exact current-base products stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Native corpus ID-label validator returned0; it does not prove class-level identity or support biological scope. |
| final-global-traits | just check-trait-links --check; Exact current-base traits stdout; retained receipt binds command, UTC, input manifest and exit code | supports | All10 trait links matched the freshly obtained TraitMech index. This target has no asserted trait links. |
| final-global-curies | just check-curies-strict; Exact current-base curies stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Native corpus resolver returned0:6105 identifiers,4997 OK,856 UNREACHABLE,252 SKIPPED. BFO authority control was not exercised because unreachable. Native exit0 is not universal resolution; target source-native checks and limitations are recorded separately. |
| final-global-qc | just qc; Exact current-base qc stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Full current-base native QC passed; review-only additions are checked separately after saving. Scientific content was unchanged. |
| target-resolver-slice | just check-curies-strict; Exact native collect() target identifier slice from fresh full-corpus TSV | supports | 17 target identifiers; 13 native OK and 4 unreachable PMID endpoints. Each residual is independently resolved by its exact retained MED primary-article metadata and inspected text tier. |
| imodulondb-datasets | https://imodulondb.org/api/datasets; Complete native console datasets listing;28 rows; exact named-organism applicability checked | context_only | The current native dataset list has no Saccharomyces cerevisiae or Schizosaccharomyces pombe dataset. This is a bounded adapter-applicability observation, not evidence that a biological structure is absent. |

## Limits And Additional Notes

- Mata1997, Arellano2002, Niccoli2003 and Tatebe2005 were read at complete native abstract/bibliography tier; publisher routes failed. No uninspected primary-body assertion is treated as verified.
- Martin2005 author PDF and Dodgson2013 JATS were read only in the named scopes. No figure pixels, raw imaging, supplementary strain tables or multi-species occurrence survey were reanalysed.
- Native InterPro entry IPR053039 has an unchecked LLM-authored description; only family metadata and reciprocal protein membership support grounding, while primary literature supports function.
- Corpus identifier resolution includes856 unreachable and252 skipped identifiers despite native exit0; BFO authority control was not exercised. These residuals are not evidence of absence or scientific validity.
- Explicit user all-record review goal authorizes a bundle for each uncovered record and a final remainder batch below10.
- No scientific records, native mapping status, curation history or generated products were edited.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T201650Z-tea1-cell-end-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Tea1 cell-end complex — source-grounded record review
started_at: '2026-10-25T19:59:50Z'
finished_at: '2026-10-25T20:16:50.962229Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Source verification is fresh; historical record authorship independence
    is not established.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Tea1 complex identity and core polarity function are supported. Five findings
  concern broad Tea1/Tea3 groundings, contextual Tea3 membership, a misattributed
  paper, Tea1 formation dispensability, and unsupported genus-level prevalence.
source:
  git_revision: 1497f644d59655f087825054920ef1a99ddebce4
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
  - path: data/structures/other/tea1_cell_end_complex.yaml
    sha256: 101c05283ca3b984dd09423eae44834b7ece1dc77d0eb39363043b2db73f3041
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
- target_id: GO:0031500
  path: data/structures/other/tea1_cell_end_complex.yaml
  label: Tea1 cell-end complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
scope:
  description: One complete maintained record; all populated scientific fields and
    graph edges assessed with the exact source tiers below.
  selection: Final8 unreviewed records in repository-relative path order after validated
    current-main and published-batch coverage reconciliation; one record per bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031500
checks:
- check_id: schema
  name: Native focused schema
  status: passed
  required: true
  target_ids:
  - GO:0031500
  command: just validate data/structures/other/tea1_cell_end_complex.yaml
  exit_code: 0
  summary: Native check passed; scientific assertions assessed separately.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Native focused strict
  status: passed
  required: true
  target_ids:
  - GO:0031500
  command: just validate-strict data/structures/other/tea1_cell_end_complex.yaml --out
    /private/tmp/cellstructure-batch62-20261025-siz_24tk/tea1_cell_end_complex-strict.tsv
  exit_code: 0
  summary: Native check passed; scientific assertions assessed separately.
  evidence_ids:
  - strict-result
- check_id: final-global-history
  name: Current-base native corpus history
  status: passed
  required: true
  target_ids:
  - GO:0031500
  command: just validate-history
  exit_code: 0
  evidence_ids:
  - final-global-history
  summary: Native append-only history validation passed for2065 history files.
  scope_note: Run against unchanged scientific inputs at 1497f644d59655f087825054920ef1a99ddebce4;
    complete baseline regular-file manifest SHA256 29137a831cea7ea233f8d3f7930a920c51f63760b1c23623e2e4c0bf7bfac77e.
- check_id: final-global-products
  name: Current-base native corpus products
  status: passed
  required: true
  target_ids:
  - GO:0031500
  command: just validate-products
  exit_code: 0
  evidence_ids:
  - final-global-products
  summary: Native corpus ID-label validator returned0; it does not prove class-level
    identity or support biological scope.
  scope_note: Run against unchanged scientific inputs at 1497f644d59655f087825054920ef1a99ddebce4;
    complete baseline regular-file manifest SHA256 29137a831cea7ea233f8d3f7930a920c51f63760b1c23623e2e4c0bf7bfac77e.
- check_id: final-global-traits
  name: Current-base native corpus traits
  status: passed
  required: true
  target_ids:
  - GO:0031500
  command: just check-trait-links --check
  exit_code: 0
  evidence_ids:
  - final-global-traits
  summary: All10 trait links matched the freshly obtained TraitMech index. This target
    has no asserted trait links.
  scope_note: Run against unchanged scientific inputs at 1497f644d59655f087825054920ef1a99ddebce4;
    complete baseline regular-file manifest SHA256 29137a831cea7ea233f8d3f7930a920c51f63760b1c23623e2e4c0bf7bfac77e.
- check_id: final-global-curies
  name: Current-base native corpus curies
  status: passed
  required: true
  target_ids:
  - GO:0031500
  command: just check-curies-strict
  exit_code: 0
  evidence_ids:
  - final-global-curies
  summary: Native corpus resolver returned0:6105 identifiers,4997 OK,856 UNREACHABLE,252
    SKIPPED. BFO authority control was not exercised because unreachable. Native exit0
    is not universal resolution; target source-native checks and limitations are recorded
    separately.
  scope_note: Run against unchanged scientific inputs at 1497f644d59655f087825054920ef1a99ddebce4;
    complete baseline regular-file manifest SHA256 29137a831cea7ea233f8d3f7930a920c51f63760b1c23623e2e4c0bf7bfac77e.
- check_id: final-global-qc
  name: Current-base native corpus qc
  status: passed
  required: true
  target_ids:
  - GO:0031500
  command: just qc
  exit_code: 0
  evidence_ids:
  - final-global-qc
  summary: Full current-base native QC passed; review-only additions are checked separately
    after saving. Scientific content was unchanged.
  scope_note: Run against unchanged scientific inputs at 1497f644d59655f087825054920ef1a99ddebce4;
    complete baseline regular-file manifest SHA256 29137a831cea7ea233f8d3f7930a920c51f63760b1c23623e2e4c0bf7bfac77e.
- check_id: target-identifiers
  name: Target native identifiers and residual reconciliation
  required: true
  status: passed
  target_ids:
  - GO:0031500
  summary: All target identifiers verified at native source level; source support
    assessed separately from identifier existence.
  evidence_ids:
  - target-resolver-slice
  - pmid-12007420
  - pmid-14663827
  - pmid-15936270
  - pmid-9200612
- check_id: scientific-assessment
  name: Claim-level source review
  required: true
  status: passed
  target_ids:
  - GO:0031500
  summary: Complete target assessed against source-native identities, cited primary
    text at declared tiers, and explicit experimental limitations; unresolved curation
    findings are preserved.
  evidence_ids:
  - go
  - ipr-IPR015915
  - ipr-IPR053039
  - protein-P87061
  - protein-O14248
  - protein-O60132
  - tax-4895
  - tax-284812
  - pmid-9200612
  - pmid-12007420
  - pmid-14663827
  - pmid-15936270
  - pmid-15809031
  - Tea2005-author-pdf
  - PMC3674234-xml
  - ro2436-go
  - ro2213-go
- check_id: imodulondb-applicability
  name: Native expression-dataset applicability check
  status: passed
  required: false
  target_ids:
  - GO:0031500
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  summary: The native dataset-list command ran successfully. No dataset matches the
    exact named organisms, so downstream target-gene queries are not applicable. Listing
    absence is not biological absence; expression-module membership would not establish
    physical assembly.
  evidence_ids:
  - imodulondb-datasets
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/tea1_cell_end_complex.yaml
  locator: Complete maintained YAML; all fields, graph nodes/edges and curation history
  accessed_at: '2026-10-25T20:04:27Z'
  support: context_only
  summary: Complete target read after native inspect. Scientific changes belong to
    this maintained YAML; no record or generated product was changed.
  snapshot_sha256: 101c05283ca3b984dd09423eae44834b7ece1dc77d0eb39363043b2db73f3041
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000133,GO:0000910,GO:0000916,GO:0005875,GO:0005935,GO:0007163,GO:0031500,GO:0032991,GO:0120155
  locator: Complete selected term responses; child arrays of asserted parents/parthood
    containers
  accessed_at: '2026-10-25T19:59:57.087024Z'
  support: supports
  summary: Exact active GO identities, definitions, synonyms and child-to-parent typed
    relationships inspected; functions denote biological processes, not complexes.
  snapshot_sha256: 02e55c430fd5915d19fe9ea71035990b0000b1e867ebd939718d2773c7428665
- evidence_id: ipr-IPR015915
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR015915/
  locator: Complete native metadata identity/type/name; description authoring status
  accessed_at: '2026-10-25T19:59:57.764771Z'
  support: supports
  summary: Native IPR015915 is Kelch-type beta-propeller of type homologous_superfamily.
    The identifier, type and name establish this entry’s scope. Accession-specific
    membership is recorded separately in the cited UniProt responses; descriptive
    prose is not experimental evidence.
  snapshot_sha256: 02a15780f6b0f6cf190ece0b0eea63476147937c86e7b695b454f08c081a53e6
- evidence_id: ipr-IPR053039
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR053039/
  locator: Complete native metadata identity/type/name; description authoring status
  accessed_at: '2026-10-25T19:59:58.381104Z'
  support: supports
  summary: Native IPR053039 is Cell polarity protein Bud14/Tea4 of type family. The
    identifier, type and name establish this entry’s scope. Accession-specific membership
    is recorded separately in the cited UniProt responses; descriptive prose is not
    experimental evidence.
  snapshot_sha256: 923a036f25f0027fae659b9e88dc16732445b0bd08ab5e3c700e4c4a3d79590e
- evidence_id: protein-P87061
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P87061.json
  locator: Native reviewed entry identity/names/genes/taxon, comments, InterPro and
    publication references
  accessed_at: '2026-10-25T20:00:01.094711Z'
  support: supports
  summary: Reviewed P87061 names the declared gene and synonyms in taxon284812. Full
    native identity, protein name, gene list, taxon, function/subunit comments and
    cited-paper provenance were read; reference-strain accession is distinct from
    the strain used in a cited experiment.
  snapshot_sha256: dbc56cc1d1571b09f356a69077b451bc588f04b36b62fefa10bd331873619abd
- evidence_id: protein-O14248
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O14248.json
  locator: Native reviewed entry identity/names/genes/taxon, comments, InterPro and
    publication references
  accessed_at: '2026-10-25T20:00:00.241126Z'
  support: supports
  summary: Reviewed O14248 names the declared gene and synonyms in taxon284812. Full
    native identity, protein name, gene list, taxon, function/subunit comments and
    cited-paper provenance were read; reference-strain accession is distinct from
    the strain used in a cited experiment.
  snapshot_sha256: 82d6b76b3e408ac614d2202db23d0d000ec5042ad3dcb765374bd0c9bdab4270
- evidence_id: protein-O60132
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O60132.json
  locator: Native reviewed entry identity/names/genes/taxon, comments, InterPro and
    publication references
  accessed_at: '2026-10-25T20:00:00.345946Z'
  support: supports
  summary: Reviewed O60132 names the declared gene and synonyms in taxon284812. Full
    native identity, protein name, gene list, taxon, function/subunit comments and
    cited-paper provenance were read; reference-strain accession is distinct from
    the strain used in a cited experiment.
  snapshot_sha256: 68109d72b536df6b379c6e69efe7db4559f65c44755271c3594f48cf0c2156f2
- evidence_id: tax-4895
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4895
  locator: Entire ENA native taxonomy response
  accessed_at: '2026-10-25T19:59:59.595716Z'
  support: supports
  summary: NCBI taxon4895 is Schizosaccharomyces at rank genus; lineage inspected.
    Taxonomic identity alone does not establish prevalence.
  snapshot_sha256: 74ffbdd6b529650cbab65abad4eab52744dda99f6ce7f967c741d07505e0f8aa
- evidence_id: tax-284812
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Entire ENA native taxonomy response
  accessed_at: '2026-10-25T19:59:58.986425Z'
  support: supports
  summary: NCBI taxon284812 is Schizosaccharomyces pombe 972h- at rank strain; lineage
    inspected. Taxonomic identity alone does not establish prevalence.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: pmid-9200612
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9200612+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identifier, complete bibliography/abstractText and full-text
    routes
  accessed_at: '2026-10-25T20:00:04.097524Z'
  support: supports
  summary: 'Exact PMID9200612: Mata J, Nurse P. tea1 and the microtubular cytoskeleton
    are important for generating global spatial order within the fission yeast cell.
    DOI:10.1016/s0092-8674(00)80279-2. Complete abstract and bibliography read; no
    uninspected methods or figures are inferred from the abstract.'
  snapshot_sha256: c5c1f745d384ec252284cfc5d6003403103a4f8ab2de398da6c9d555ecb6d51a
- evidence_id: pmid-12007420
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12007420+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identifier, complete bibliography/abstractText and full-text
    routes
  accessed_at: '2026-10-25T20:00:02.412754Z'
  support: supports
  summary: 'Exact PMID12007420: Arellano M, Niccoli T, Nurse P. Tea3p is a cell end
    marker activating polarized growth in Schizosaccharomyces pombe. DOI:10.1016/s0960-9822(02)00821-7.
    Complete abstract and bibliography read; no uninspected methods or figures are
    inferred from the abstract.'
  snapshot_sha256: 176afb75d89df6c1e822f7baa391535ae6637201c1cd6fea65451914584f7d03
- evidence_id: pmid-14663827
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14663827+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identifier, complete bibliography/abstractText and full-text
    routes
  accessed_at: '2026-10-25T20:00:02.634711Z'
  support: supports
  summary: 'Exact PMID14663827: Niccoli T, Arellano M, Nurse P. Role of Tea1p, Tea3p
    and Pom1p in the determination of cell ends in Schizosaccharomyces pombe. DOI:10.1002/yea.1054.
    Complete abstract and bibliography read; no uninspected methods or figures are
    inferred from the abstract.'
  snapshot_sha256: 79b43bb5f7665de09080dcd0a4d1676abcea237685710fbd310b5ed3b7d9f3dd
- evidence_id: pmid-15936270
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15936270+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identifier, complete bibliography/abstractText and full-text
    routes
  accessed_at: '2026-10-25T20:00:03.065056Z'
  support: supports
  summary: 'Exact PMID15936270: Tatebe H, Shimada K, Uzawa S, Morigasaki S, Shiozaki
    K. Wsh3/Tea4 is a novel cell-end factor essential for bipolar distribution of
    Tea1 and protects cell polarity under environmental stress in S. pombe. DOI:10.1016/j.cub.2005.04.061.
    Complete abstract and bibliography read; no uninspected methods or figures are
    inferred from the abstract.'
  snapshot_sha256: 9f9d16653d74fcd3694bce3aeebce08c13510381018badd75fe7b9bbe2c84577
- evidence_id: pmid-15809031
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15809031%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Unique MED identifier, complete bibliography/abstractText and full-text
    routes
  accessed_at: '2026-10-25T20:00:39.450009Z'
  support: supports
  summary: 'Exact PMID15809031: Martin SG, McDonald WH, Yates JR, Chang F. Tea4p links
    microtubule plus ends with the formin for3p in the establishment of cell polarity.
    DOI:10.1016/j.devcel.2005.02.008. Complete abstract and bibliography read; no
    uninspected methods or figures are inferred from the abstract.'
  snapshot_sha256: c7cfd19f54260ce64dc08fa9ac01aa63340e15f64fdd7e9cdbf672a68711cfdb
- evidence_id: Tea2005-author-pdf
  kind: primary_source
  reference: https://www.columbia.edu/cu/biology/dept/seminarPDFfiles/Martin%20Dev%2C%20Fred%20ChangCell05.pdf
  locator: 'Author-hosted primary PDF pages480–489: identification/localization, Tea4–For3
    binding, linking and additional-functions sections; page489 strain-method paragraph.
    Figure1/2/4 captions as extracted; no image pixels or supplementary strain table.'
  accessed_at: '2026-10-25T20:01:19.706958Z'
  support: supports
  summary: Martin2005 demonstrates direct Tea1–Tea4 and Tea4–For3 binding, with Tea4
    bridging Tea1–For3. Deleting tea1 disperses Tea4; deleting tea4 preserves some
    Tea1 assemblies but removes this connection.
  snapshot_sha256: 57856c831c21e049a5620ff99e3510e4b824b27f366aff99694ea6460b1cb5d4
- evidence_id: PMC3674234-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3674234/fullTextXML
  locator: Genuine JATS complete Results and Discussion; Methods strain and frontal-imaging
    subsections. Supplementary files, pixels and unlisted Methods were not inspected.
  accessed_at: '2026-10-25T20:01:18.838664Z'
  support: supports
  summary: Dodgson2013 distinguishes Tea1/Tea4 clusters from nearby Tea3 clusters
    during growth; association increases during mitosis, when Tea3 aids Tea1 retention.
    Forced persistent Tea1–Tea3 proximity disrupts polarity.
  snapshot_sha256: eec59298a585eb04d377d9b2fa55da0a21fefc53217f213fbff4e76c91a54819
- evidence_id: ro2436-go
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/properties?obo_id=RO:0002436
  locator: Exact OLS property response including label and definition
  accessed_at: '2026-10-25T20:02:22.203819Z'
  support: supports
  summary: 'RO:0002436 is molecularly interacts with: a direct physical interaction
    between molecular entities. This relation identity does not itself verify a component-specific
    contact.'
  snapshot_sha256: 62992a7c016646736c4f24663e3e64b03e875f577cc2b424af7233a59e211563
- evidence_id: ro2213-go
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/properties?obo_id=RO:0002213
  locator: Exact OLS property response including label and definition
  accessed_at: '2026-10-25T20:02:22.591668Z'
  support: supports
  summary: 'RO:0002213 is positively regulates: regulation increasing the rate or
    magnitude of a process. Its identity does not itself prove the stated biological
    effect.'
  snapshot_sha256: f439df6d927bce177f38477e03707c3436c8fb0f24bc113c40741967279b9745
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/tea1_cell_end_complex.yaml
  locator: Complete focused native validator output
  accessed_at: '2026-10-25T19:59:51Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/tea1_cell_end_complex.yaml'
  snapshot_sha256: 8cdda250430cb439f460d568f8553f16af2c2b2b45354471013600cfa92c469f
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/tea1_cell_end_complex.yaml
    --out /private/tmp/cellstructure-batch62-20261025-siz_24tk/tea1_cell_end_complex-strict.tsv
  locator: Complete focused native validator output
  accessed_at: '2026-10-25T19:59:53Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/tea1_cell_end_complex.yaml\
    \ --out /private/tmp/cellstructure-batch62-20261025-siz_24tk/tea1_cell_end_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch62-20261025-siz_24tk/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch62-20261025-siz_24tk/tea1_cell_end_complex-strict.tsv"
  snapshot_sha256: e68e9f772523ea62547b78a8cdff52e71373a89dc01893ff04634eff17509aaa
- evidence_id: final-global-history
  kind: validation
  reference: just validate-history
  locator: Exact current-base history stdout; retained receipt binds command, UTC,
    input manifest and exit code
  accessed_at: '2026-10-25T19:59:33.039839Z'
  support: supports
  summary: Native append-only history validation passed for2065 history files.
  snapshot_sha256: beb8780a7910df045dcae7003d8ede2f8b6d08b9a311c15982997c40796d02d8
- evidence_id: final-global-products
  kind: validation
  reference: just validate-products
  locator: Exact current-base products stdout; retained receipt binds command, UTC,
    input manifest and exit code
  accessed_at: '2026-10-25T20:00:11.856400Z'
  support: supports
  summary: Native corpus ID-label validator returned0; it does not prove class-level
    identity or support biological scope.
  snapshot_sha256: 0158645d825815955f637f5ec44265e94950a33f646e419a0c8999be5aff8d2f
- evidence_id: final-global-traits
  kind: validation
  reference: just check-trait-links --check
  locator: Exact current-base traits stdout; retained receipt binds command, UTC,
    input manifest and exit code
  accessed_at: '2026-10-25T19:59:53.599030Z'
  support: supports
  summary: All10 trait links matched the freshly obtained TraitMech index. This target
    has no asserted trait links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: final-global-curies
  kind: validation
  reference: just check-curies-strict
  locator: Exact current-base curies stdout; retained receipt binds command, UTC,
    input manifest and exit code
  accessed_at: '2026-10-25T20:01:08.675608Z'
  support: supports
  summary: Native corpus resolver returned0:6105 identifiers,4997 OK,856 UNREACHABLE,252
    SKIPPED. BFO authority control was not exercised because unreachable. Native exit0
    is not universal resolution; target source-native checks and limitations are recorded
    separately.
  snapshot_sha256: 1429e55e1cb3667b4710ad56b2b9d90bd7104a24f4899edc6470f15152838e7d
- evidence_id: final-global-qc
  kind: validation
  reference: just qc
  locator: Exact current-base qc stdout; retained receipt binds command, UTC, input
    manifest and exit code
  accessed_at: '2026-10-25T20:06:17.301813Z'
  support: supports
  summary: Full current-base native QC passed; review-only additions are checked separately
    after saving. Scientific content was unchanged.
  snapshot_sha256: 3b50443af049a5f09641445e5c29c66e5f96c4f7a3bb046b344e96fa0d223d8b
- evidence_id: target-resolver-slice
  kind: validation
  reference: just check-curies-strict
  locator: Exact native collect() target identifier slice from fresh full-corpus TSV
  accessed_at: '2026-10-25T20:07:42.038086Z'
  support: supports
  summary: 17 target identifiers; 13 native OK and 4 unreachable PMID endpoints. Each
    residual is independently resolved by its exact retained MED primary-article metadata
    and inspected text tier.
  snapshot_sha256: 930445bdb54031f3fbd1d6eec57323e330bddc5386757c0e421c1970fd6eb961
- evidence_id: imodulondb-datasets
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete native console datasets listing;28 rows; exact named-organism
    applicability checked
  accessed_at: '2026-10-25T20:04:24.215410Z'
  support: context_only
  summary: The current native dataset list has no Saccharomyces cerevisiae or Schizosaccharomyces
    pombe dataset. This is a bounded adapter-applicability observation, not evidence
    that a biological structure is absent.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  search_scope: All28 dataset rows returned by kg-microbe-sources imodulondb datasets;
    exact named-organism matching, not an exhaustive transcriptomics search.
assessments:
- assessment_id: identity
  area: identity
  topic: Tea1-defined cell-end polarity assembly
  outcome: supported
  target_ids:
  - GO:0031500
  summary: GO identity, microtubule-associated-complex parent and polarisome parthood
    are supported. The source definition typo is inherited from GO and does not alter
    identity. The entity is a complex class, not an isolated Tea1 protein.
  evidence_ids:
  - record
  - go
  - protein-P87061
  - protein-O14248
  - protein-O60132
  - pmid-15936270
- assessment_id: grounding
  area: grounding
  topic: Family boundaries and reference proteins
  outcome: concern
  target_ids:
  - GO:0031500
  summary: Tea4 has a native family identity and exact reviewed protein. Tea1/Tea3
    use a broad Kelch-type homologous superfamily as exact class identity, although
    their protein examples and gene synonyms are correct.
  evidence_ids:
  - record
  - go
  - protein-P87061
  - protein-O14248
  - protein-O60132
  - ipr-IPR015915
  - ipr-IPR053039
- assessment_id: architecture
  area: graph
  topic: State-dependent cortical organization
  outcome: concern
  target_ids:
  - GO:0031500
  summary: All four graph edges were assessed. The role already specifies non-growing
    ends, but omits the distinct cell-cycle context of Tea3 association with Tea1
    assemblies. Tea1 and Tea4 effects on assembly remain distinct from viability.
  evidence_ids:
  - record
  - go
  - protein-P87061
  - protein-O14248
  - protein-O60132
  - Tea2005-author-pdf
  - PMC3674234-xml
  - ro2436-go
  - ro2213-go
- assessment_id: taxa
  area: scope
  topic: Species evidence versus genus prevalence
  outcome: concern
  target_ids:
  - GO:0031500
  summary: Native Schizosaccharomyces and strain972h- identities agree. The cited
    Mata experiment addresses S. pombe, so COMMON across the genus requires additional
    evidence; verified strain reference proteins alone do not establish the original
    experimental isolate.
  evidence_ids:
  - tax-4895
  - tax-284812
  - pmid-9200612
  - record
  - go
  - protein-P87061
  - protein-O14248
  - protein-O60132
- assessment_id: record-completeness
  area: completeness
  topic: Populated fields and maintained ownership
  outcome: supported
  target_ids:
  - GO:0031500
  summary: All target fields were read. No images, physical-property measurements,
    source compositions or trait links are asserted in this target; their optional
    absence is not a finding. Native PROPOSED status and an LLM-assisted creation
    event are appropriate. Future edits belong to the maintained YAML and require
    curation/history gates.
  evidence_ids:
  - record
  - go
  - protein-P87061
  - protein-O14248
  - protein-O60132
findings:
- finding_id: F1
  issue_key: tea1-cell-end-complex-kelch-superfamily-groundings
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Tea1 and Tea3 are grounded to a broad structural superfamily
  description: IPR015915 is the Kelch-type beta-propeller homologous superfamily,
    not an exact Tea1 or Tea3 protein-family identity. Both component and graph-node
    groundings inherit this mismatch.
  field_paths:
  - components[0].grounding
  - components[1].grounding
  - causal_graphs[0].nodes[0].grounding
  - causal_graphs[0].nodes[1].grounding
  target_ids:
  - GO:0031500
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
  evidence_ids:
  - record
  - ipr-IPR015915
  rule_id: 'CellStructureRecord review checklist: exact identity, claim-level source
    scope and component formation semantics'
  native_severity: major
  normalization_reason: Major for wrong class grounding or materially inflated scope;
    minor for localized wording, attribution or unsupported formation labels without
    loss of complex identity.
- finding_id: F2
  issue_key: tea1-cell-end-complex-tea3-assembly-context
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Tea3 association needs cell-cycle context
  description: The Tea3 role already specifies non-growing cell ends. Dodgson found
    that growing-versus-nongrowing position did not explain Tea1–Tea3 cluster correlation,
    whereas mitosis increased association and made Tea3 important for Tea1 retention.
    Add this phase dependence to the anchoring role and graph; CONSTITUENT alone does
    not assert invariant coassembly.
  field_paths:
  - components[1].component_role
  - components[1].role
  - causal_graphs[0].edges[1]
  target_ids:
  - GO:0031500
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
  evidence_ids:
  - record
  - PMC3674234-xml
  rule_id: 'CellStructureRecord review checklist: exact identity, claim-level source
    scope and component formation semantics'
  native_severity: minor
  normalization_reason: Major for wrong class grounding or materially inflated scope;
    minor for localized wording, attribution or unsupported formation labels without
    loss of complex identity.
- finding_id: F3
  issue_key: tea1-cell-end-complex-paper-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The Tea3 citation has the wrong author attribution
  description: PMID14663827 and DOI10.1002/yea.1054 identify the 2003 Niccoli, Arellano
    and Nurse study, not Snaith and Sawin. Its abstract reports comparative growth/microtubule
    phenotypes; do not use that abstract alone as proof of direct biochemical interaction.
  field_paths:
  - components[1].evidence[1].notes
  target_ids:
  - GO:0031500
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
  evidence_ids:
  - record
  - pmid-14663827
  rule_id: 'CellStructureRecord review checklist: exact identity, claim-level source
    scope and component formation semantics'
  native_severity: minor
  normalization_reason: Major for wrong class grounding or materially inflated scope;
    minor for localized wording, attribution or unsupported formation labels without
    loss of complex identity.
- finding_id: F4
  issue_key: tea1-cell-end-complex-tea1-formation-necessity
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Tea1 dispensability is unsupported for the named assembly
  description: Tea1 is the defining scaffold but is marked DISPENSABLE for formation.
    Martin reports loss of Tea4 localization and loss of the Tip1–Tea4 association
    in tea1 deletion cells. Viability and remaining polarity factors do not establish
    persistence of the named Tea1 assembly.
  field_paths:
  - components[0].essentiality
  target_ids:
  - GO:0031500
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
  evidence_ids:
  - record
  - Tea2005-author-pdf
  rule_id: 'CellStructureRecord review checklist: exact identity, claim-level source
    scope and component formation semantics'
  native_severity: minor
  normalization_reason: Major for wrong class grounding or materially inflated scope;
    minor for localized wording, attribution or unsupported formation labels without
    loss of complex identity.
- finding_id: F5
  issue_key: tea1-cell-end-complex-genus-prevalence
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Genus-wide COMMON occurrence is not established by the cited study
  description: The distribution uses COMMON for Schizosaccharomyces but cites a study
    confined to S. pombe. Neither the reference protein strain nor genus membership
    supplies evidence of frequent occurrence across species.
  field_paths:
  - taxonomic_distribution[0].presence
  target_ids:
  - GO:0031500
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
  evidence_ids:
  - record
  - pmid-9200612
  - tax-4895
  rule_id: 'CellStructureRecord review checklist: exact identity, claim-level source
    scope and component formation semantics'
  native_severity: minor
  normalization_reason: Major for wrong class grounding or materially inflated scope;
    minor for localized wording, attribution or unsupported formation labels without
    loss of complex identity.
actions:
- action_id: A1
  finding_ids:
  - F1
  description: Use independently verified class-specific families where available
    or justified label-only representations; retain correct UniProt examples and keep
    graph references consistent.
  target_ids:
  - GO:0031500
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - Verify the corrected claim against its exact native identifier or primary source
    and retain experimental scope.
  - After separately authorized curation, run focused schema/strict checks, product
    correspondence, history validation and full QC; preserve PROPOSED status.
- action_id: A2
  finding_ids:
  - F2
  description: Retain the supported Tea3 association while adding the experimentally
    distinguished cell-cycle context to its anchoring role and graph. Reassess constituent
    versus associated-machinery representation with an explicit complex boundary.
  target_ids:
  - GO:0031500
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - Verify the corrected claim against its exact native identifier or primary source
    and retain experimental scope.
  - After separately authorized curation, run focused schema/strict checks, product
    correspondence, history validation and full QC; preserve PROPOSED status.
- action_id: A3
  finding_ids:
  - F3
  description: Correct the author attribution and tie interaction-specific wording
    to an inspected interaction experiment, keeping genetic/localization evidence
    distinct.
  target_ids:
  - GO:0031500
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - Verify the corrected claim against its exact native identifier or primary source
    and retain experimental scope.
  - After separately authorized curation, run focused schema/strict checks, product
    correspondence, history validation and full QC; preserve PROPOSED status.
- action_id: A4
  finding_ids:
  - F4
  description: Reassess Tea1 formation necessity for the exact complex boundary. Do
    not equate viability with structural dispensability; qualify other component necessity
    separately.
  target_ids:
  - GO:0031500
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - Verify the corrected claim against its exact native identifier or primary source
    and retain experimental scope.
  - After separately authorized curation, run focused schema/strict checks, product
    correspondence, history validation and full QC; preserve PROPOSED status.
- action_id: A5
  finding_ids:
  - F5
  description: Constrain the distribution to the demonstrated organism or cite an
    appropriate comparative source for genus-level occurrence.
  target_ids:
  - GO:0031500
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/tea1_cell_end_complex.yaml
    role: maintained scientific record
  acceptance_checks:
  - Verify the corrected claim against its exact native identifier or primary source
    and retain experimental scope.
  - After separately authorized curation, run focused schema/strict checks, product
    correspondence, history validation and full QC; preserve PROPOSED status.
limitations:
- Mata1997, Arellano2002, Niccoli2003 and Tatebe2005 were read at complete native
  abstract/bibliography tier; publisher routes failed. No uninspected primary-body
  assertion is treated as verified.
- Martin2005 author PDF and Dodgson2013 JATS were read only in the named scopes. No
  figure pixels, raw imaging, supplementary strain tables or multi-species occurrence
  survey were reanalysed.
- Native InterPro entry IPR053039 has an unchecked LLM-authored description; only
  family metadata and reciprocal protein membership support grounding, while primary
  literature supports function.
- Corpus identifier resolution includes856 unreachable and252 skipped identifiers
  despite native exit0; BFO authority control was not exercised. These residuals are
  not evidence of absence or scientific validity.
notes:
- Explicit user all-record review goal authorizes a bundle for each uncovered record
  and a final remainder batch below10.
- No scientific records, native mapping status, curation history or generated products
  were edited.
```
