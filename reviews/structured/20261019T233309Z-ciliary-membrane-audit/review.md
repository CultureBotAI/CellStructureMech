# Ciliary membrane identity, composition and evidence review

- Review: 20261019T233309Z-ciliary-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-19T07:33:06Z
- Finished UTC: 2026-10-19T23:33:09Z
- Reviewer: Codex scientific review agent (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire maintained record assessed. Exact GO identity, hierarchy, membrane composition, Chlamydomonas example, protein identifier and membrane-growth function are supported. One minor edge-level provenance issue: proteomics is cited for a selectively sorted membrane-protein set without the sorting/localization support already available in other literature.

## Scope And Provenance

Full single-record review: definition, four synonyms, two is-a parents and cilium parthood, two aggregate components, PKD2 and FMG1-B examples, one UniProt accession, taxonomic distribution and canonical example, assembly function, all four graph edges, inventory discussion, and available history.

Selection: Second unreviewed corpus path in the coordinator's fresh-origin/main inventory: data/structures/appendage/ciliary_membrane.yaml. This document assesses exactly one target, not a corpus sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0060170 | data/structures/appendage/ciliary_membrane.yaml | maintained | ciliary membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema validation | passed | True | GO:0060170 | Focused LinkML schema validation reports No issues found. |
| strict validation | passed | True | GO:0060170 | Focused closed-schema validation scanned one record with zero error rows. |
| Source and stable identifier inspection | passed | True | GO:0060170 | Inspected all three cited papers as full text and exact GO, taxonomy and UniProt records; independently corroborated PKD2 and FMG1-B membership. This is a manual scientific assessment, not merely metadata resolution. |
| Verbatim snippet check | not_applicable | False | GO:0060170 | The entire target contains no snippet fields; no quoted evidence was added. Citation support was manually assessed. |
| Target identifier coverage including resolver residuals | passed | True | GO:0060170 | All CURIE-shaped target values have issuing-authority or appropriate local/source-specific existence verification. Generic PMID HTTP414 failures and skipped namespaces were resolved by scoped receipts; biological mapping correctness is assessed separately. |
| Full corpus QC | passed | True | GO:0060170 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0060170 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0060170 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0060170 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0060170 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact microbial membrane domain

identity: supported. Targets: GO:0060170.

GO:0060170 denotes exactly this plasma-membrane domain surrounding a eukaryotic cilium; it is a structure, not a protein or phenotype. APPENDAGE/MEMBRANE and all synonym scopes are consistent.

### Is-a parents and cilium parthood

representation: supported. Targets: GO:0060170.

Both parent relations are is-a and cilium is the containing organelle. The record does not mistake the membrane for the whole cilium or bacterial flagellum.

### Aggregate lipid and protein composition

completeness: supported. Targets: GO:0060170.

The two label-only aggregates are explicitly bounded. A lipid phase is necessary to a membrane, while protein essentiality is left unknown and molecular inventory remains an open question. PKD2 and FMG1-B are legitimate Chlamydomonas membrane examples; accession and annotation tier match. Exact conserved lipid classes, counts or a universal protein repertoire are not asserted.

The inventory TODO is acknowledged scientific incompleteness, not an invented defect. Protein example provenance expressly separates identifier verification from structural membership.

### Chlamydomonas presence and example

scope: supported. Targets: GO:0060170.

Species label and taxon match. Membrane-bounded Chlamydomonas flagella are directly observed in the proteomics paper, and Dentler used this organism for regeneration experiments. COMMON is interpreted qualitatively, not as a measured prevalence estimate.

### Membrane supply during cilium assembly

evidence: supported. Targets: GO:0060170.

Dentler supports the Chlamydomonas-specific assembly/length description. GO:0060271 supplies the correct process label; the record does not claim membrane supply is the sole length-control mechanism.

### Four nonmechanistic topology and localization edges

graph: concern. Targets: GO:0060170.

The lipid-phase, membrane-boundary and expansion edges are supported at their stated scale. The protein-localization edge adds selectively sorted composition while citing only a proteomic inventory; the sorting/localization evidence should accompany that edge.

NONMECHANISTIC scope is appropriate. The generic bounds relation does not claim complete isolation from cytosol, consistent with the open ciliary base described in Garcia. No specific transport machinery is silently asserted as a constituent.

### Optional measurements, images and datasets

completeness: not_applicable. Targets: GO:0060170.

No numerical physical property, image, licence or dataset assertion appears in the complete target. Their absence is not a defect under the local checklist.

### Evidence placement and scientific status

provenance: supported. Targets: GO:0060170.

Citations resolve to the stated works; label-only notes and inventory discussion are explicit. The target remains PROPOSED and carries curation provenance. Available repository-level history records the initial creation and earlier evidence narrowing.

## Findings

### F1: Selective membrane-protein composition needs evidence on its graph edge

minor / open / confirmed; issue key: ciliary-membrane-sorted-protein-edge-evidence.

The localize-to edge describes a sorted set of Chlamydomonas membrane proteins but cites only Pazour 2005, whose pertinent result is detection of predicted membrane proteins in fractionated flagella. That experiment alone does not establish selective sorting or retention in the membrane. Garcia 2018, already cited elsewhere in the record, reviews membrane targeting/retention; Awata 2014 provides Chlamydomonas experiments on selective composition including FMG1-B and PKD2. Attach appropriate evidence at this edge or narrow its wording to the proteomic observation. This is a bounded evidence-placement gap, not evidence that the proteins or membrane are biologically wrong.

## Recommended Actions And Acceptance Checks

### A1

Curator should attach the existing Garcia review and/or a Chlamydomonas localization/sorting study to the protein-localization edge, explicitly distinguishing proteomic candidates from experimentally localized or selectively retained proteins. Alternatively narrow the edge description to what Pazour directly establishes.

- Read the selected source context and confirm it supports every retained qualifier at the edge.
- Use write_validated_structure with an append-only curation event and repository history for any later authorized mutation.
- Run just validate, just validate-strict and just qc; regenerate pages with just render only as part of separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/ciliary_membrane.yaml; Entire YAML; components; causal_graphs; discussions; curation_history | context_only | Maintained GO-grounded membrane record with two explicitly label-only component aggregates, one taxon-paired protein example, an open molecular-inventory discussion and NONMECHANISTIC graph. Mapping remains PROPOSED. |
| go-authority | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0060170%2CGO%3A0031253%2CGO%3A0098588%2CGO%3A0005929%2CGO%3A0060271; results: id, name, isObsolete, aspect, definition, synonyms, and parent-term children relations | supports | All five terms are current and labels/aspects match. GO:0060170 definition and exact/narrow synonym scopes match the YAML. Both asserted parents list ciliary membrane as an is-a child, while cilium lists it as part_of. Cilium assembly denotes assembly of a membrane-bounded eukaryotic cilium. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3055; TaxaSet/Taxon: TaxId, ScientificName, Rank | supports | NCBITaxon:3055 resolves to the species Chlamydomonas reinhardtii; all record occurrences use the matching scientific label. |
| uniprot | https://rest.uniprot.org/uniprotkb/A9LE42.json; primaryAccession; entryType; proteinDescription; genes; organism; entryAudit | supports | A9LE42 is an active unreviewed TrEMBL entry with submitted protein name PKD2, gene PKD2 and taxon 3055. Entry version 49, sequence version 1, annotation updated 2026-06-10. This verifies accession/gene/taxon/status only; membrane membership is assessed from papers. |
| pazour | https://pmc.ncbi.nlm.nih.gov/articles/PMC2171396/?pdf=1; DOI:10.1083/jcb.200504008; Introduction; Figure 2; Results proteomic analysis; Discussion membrane-associated proteins; Materials and methods flagellar fractionation | partial | Full text confirms title/authors/year and Chlamydomonas flagellar membranes. Mass spectrometry used wild-type 137c and oda1-1 flagella separated into membrane-plus-matrix and axonemal fractions, identifying predicted membrane proteins including a polycystin-2 homologue. This supports record notes about proteomic candidates. It does not directly test selective entry, sorting or retention of the asserted membrane-protein set. |
| garcia | https://pmc.ncbi.nlm.nih.gov/articles/PMC6434934/?pdf=1; DOI:10.1016/j.cub.2018.03.010; Abstract; introductory membrane specialization paragraphs; protein/lipid trafficking sections | supports | Full review text confirms title, Garcia/Raleigh/Reiter authorship and year. Ciliary membranes contain distinctive proteins and lipids, remain continuous with plasma membrane and incompletely enclose cilia. Lipid bilayers, ciliary targeting/retention and selective membrane composition are reviewed. Chlamydomonas agglutinins provide a microbial example; many detailed phosphoinositide and receptor mechanisms concern animal systems. Aggregate components and bounded nonmechanistic topology are supported. |
| dentler | https://pmc.ncbi.nlm.nih.gov/articles/PMC3554728/?pdf=1; DOI:10.1371/journal.pone.0053366; Abstract; Results Figure 1; Discussion secretory pathway and membrane availability | supports | Full text confirms Dentler 2013 identity. Chlamydomonas experiments, chiefly wild-type L8 with relevant motility/IFT mutants, tested regeneration and maintenance during brefeldin-A inhibition and surface-protein turnover. Results support membrane resupply constraining growth and maintenance. The record keeps the organism explicit, avoids claiming purified ciliary lipidomics and contains no unsupported numerical estimate. |
| pkd2-localization | https://pubmed.ncbi.nlm.nih.gov/17984324/; Huang et al. 2007; DOI:10.1083/jcb.200704069; PubMed Abstract read through efetch XML | supports | The abstract reports cloned Chlamydomonas PKD2, flagellar cleavage products and observed PKD2-GFP movement in the flagellar membrane. This independent primary support confirms the protein example belongs in the membrane context; it is not presently attached to the component evidence in the reviewed record. |
| fmg1-localization | https://pmc.ncbi.nlm.nih.gov/articles/PMC4215714/; Awata et al. 2014; DOI:10.1242/jcs.155275; Results protein composition; Figure 7C; paragraphs on FMG1-B and PKD2 | supports | Directly inspected full-text paragraphs identify FMG1-B as a transmembrane flagellar glycoprotein and show its reduced abundance in nphp4 flagella and restoration in rescued material, with immunoblot corroboration. PKD2 remains present. These experiments support selective composition and the named Chlamydomonas proteins more directly than unqualified use of the 2005 inventory. |
| history | history/records/ciliary_membrane/; 2026-09-15T133921Z-codex-03185b.yaml and 2026-09-15T134730Z-codex-930de8.yaml; target curation_history | context_only | Inspected creation and follow-up history record narrow Dentler example and label-only lipid edge corrections. The current record preserves PROPOSED status and later protein-example provenance; no status promotion is claimed. |
| history-search | history/ and reviews/structured/; rg --no-ignore --hidden -n ciliary_membrane&#124;GO:0060170&#124;FMG1-B&#124;A9LE42 history reviews/structured --glob *.yaml | context_only | Bounded search found the two target-specific history documents and GO context mentions in radial-spoke review bundles. Context mentions do not review this target; authoritative coverage remains the coordinator's validated list. |
| schema-result | UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache just validate data/structures/appendage/ciliary_membrane.yaml; stdout/stderr log retained outside repository | supports | Focused LinkML schema validation reports No issues found. |
| strict-result | UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache just validate-strict data/structures/appendage/ciliary_membrane.yaml --out /private/tmp/cellstructure-record-reviews-UhRFh7/ciliary-membrane/strict.tsv; stdout/stderr log retained outside repository | supports | Focused closed-schema validation scanned one record with zero error rows. |
| target-resolver-coverage | just check-curies-strict; data/structures/appendage/ciliary_membrane.yaml; exact scripts/check_curies.py collect() scope; reports/curie_check.tsv | supports | This target contains 10 distinct CURIE-shaped scalar values: 10 OK, 0 transport-unreachable and 0 skipped in the global report. The attached scoped receipts resolve each non-OK identifier. HTTP URLs and prose are outside collect(); their content was inspected separately. Existence is not proof of correct biological mapping. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Pazour 2005 provides purified-flagellum proteomics and predicted membrane associations; its supplemental molecular inventory was not retrieved. Exact FMG1-B identity and flagellar association were independently corroborated in Awata 2014, and PKD2 membrane localization in Huang 2007.
- Huang 2007 was inspected at the PubMed abstract tier after PMC and publisher body access failures. The three papers already cited by the record were all inspected as full text.
- Review is limited to stated biological claims and proportionate completeness; it does not establish an exhaustive cross-taxon lipid/protein inventory or measure population prevalence.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly requested one validated bundle per previously unreviewed record; that instruction overrides the local issue-only persistence gate.
- No record, generated page, curation history, or external communication was modified.
- No verbatim paper quotations are reproduced.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233309Z-ciliary-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Ciliary membrane identity, composition and evidence review
started_at: '2026-10-19T07:33:06Z'
finished_at: '2026-10-19T23:33:09Z'
reviewer:
  identity: Codex scientific review agent
  kind: agent
  independence: unknown
  independence_basis: Delegated source review of an existing agent-authored record.
    Prior Codex and Claude authorship is not treated as demonstrably independent human
    review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Entire maintained record assessed. Exact GO identity, hierarchy, membrane
  composition, Chlamydomonas example, protein identifier and membrane-growth function
  are supported. One minor edge-level provenance issue: proteomics is cited for a
  selectively sorted membrane-protein set without the sorting/localization support
  already available in other literature.'
source:
  git_revision: 99692a3d5f16a7dcd6db7e3811344c299a977b81
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
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/appendage/ciliary_membrane.yaml
    sha256: be5035248f05df4bfc22b39cf6d07b2b76778d02bfbaf5aff0f5dee1f5785a00
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
  - path: history/records/ciliary_membrane/2026-09-15T133921Z-codex-03185b.yaml
    sha256: da5e928653fb89b99f051e7d036c92c2feb44dcc179ae3cd7be8056d925121c6
    role: context
  - path: history/records/ciliary_membrane/2026-09-15T134730Z-codex-930de8.yaml
    sha256: a4745d326165826848bb29cbb42f604b5c6ae751096352e023da3cbb1caae7ac
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
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0060170
  path: data/structures/appendage/ciliary_membrane.yaml
  label: ciliary membrane
  record_class: CellStructureRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_membrane.yaml
    role: maintained scientific record
scope:
  description: 'Full single-record review: definition, four synonyms, two is-a parents
    and cilium parthood, two aggregate components, PKD2 and FMG1-B examples, one UniProt
    accession, taxonomic distribution and canonical example, assembly function, all
    four graph edges, inventory discussion, and available history.'
  selection: 'Second unreviewed corpus path in the coordinator''s fresh-origin/main
    inventory: data/structures/appendage/ciliary_membrane.yaml. This document assesses
    exactly one target, not a corpus sample.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0060170
checks:
- check_id: schema
  name: schema validation
  status: passed
  required: true
  summary: Focused LinkML schema validation reports No issues found.
  target_ids:
  - GO:0060170
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate data/structures/appendage/ciliary_membrane.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema-result
  scope_note: Only the selected maintained record was checked. Global native gates
    are coordinated separately.
- check_id: strict
  name: strict validation
  status: passed
  required: true
  summary: Focused closed-schema validation scanned one record with zero error rows.
  target_ids:
  - GO:0060170
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate-strict data/structures/appendage/ciliary_membrane.yaml --out /private/tmp/cellstructure-record-reviews-UhRFh7/ciliary-membrane/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - strict-result
  scope_note: Only the selected maintained record was checked. Global native gates
    are coordinated separately.
- check_id: source-inspection
  name: Source and stable identifier inspection
  status: passed
  required: true
  summary: Inspected all three cited papers as full text and exact GO, taxonomy and
    UniProt records; independently corroborated PKD2 and FMG1-B membership. This is
    a manual scientific assessment, not merely metadata resolution.
  target_ids:
  - GO:0060170
  evidence_ids:
  - go-authority
  - taxonomy
  - uniprot
  - pazour
  - garcia
  - dentler
  - pkd2-localization
  - fmg1-localization
- check_id: snippets
  name: Verbatim snippet check
  status: not_applicable
  required: false
  summary: The entire target contains no snippet fields; no quoted evidence was added.
    Citation support was manually assessed.
  target_ids:
  - GO:0060170
  evidence_ids:
  - record
- check_id: target-identifier-coverage
  name: Target identifier coverage including resolver residuals
  status: passed
  required: true
  target_ids:
  - GO:0060170
  summary: All CURIE-shaped target values have issuing-authority or appropriate local/source-specific
    existence verification. Generic PMID HTTP414 failures and skipped namespaces were
    resolved by scoped receipts; biological mapping correctness is assessed separately.
  evidence_ids:
  - target-resolver-coverage
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0060170
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0060170
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0060170
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0060170
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0060170
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/ciliary_membrane.yaml
  locator: Entire YAML; components; causal_graphs; discussions; curation_history
  accessed_at: '2026-10-19T07:33:06Z'
  support: context_only
  summary: Maintained GO-grounded membrane record with two explicitly label-only component
    aggregates, one taxon-paired protein example, an open molecular-inventory discussion
    and NONMECHANISTIC graph. Mapping remains PROPOSED.
  snapshot_sha256: be5035248f05df4bfc22b39cf6d07b2b76778d02bfbaf5aff0f5dee1f5785a00
- evidence_id: go-authority
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0060170%2CGO%3A0031253%2CGO%3A0098588%2CGO%3A0005929%2CGO%3A0060271
  locator: 'results: id, name, isObsolete, aspect, definition, synonyms, and parent-term
    children relations'
  accessed_at: '2026-10-19T07:33:44Z'
  support: supports
  summary: All five terms are current and labels/aspects match. GO:0060170 definition
    and exact/narrow synonym scopes match the YAML. Both asserted parents list ciliary
    membrane as an is-a child, while cilium lists it as part_of. Cilium assembly denotes
    assembly of a membrane-bounded eukaryotic cilium.
  snapshot_sha256: 8ea11c4c867db4b3568b0fadf92117fe2895cc920faba7a4193d4eb450597609
- evidence_id: taxonomy
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3055
  locator: 'TaxaSet/Taxon: TaxId, ScientificName, Rank'
  accessed_at: '2026-10-19T07:33:43Z'
  support: supports
  summary: NCBITaxon:3055 resolves to the species Chlamydomonas reinhardtii; all record
    occurrences use the matching scientific label.
  snapshot_sha256: a17bc1c97fea9112288574ef15727ed7e37c42787a430ef074ae5fc654547e6b
- evidence_id: uniprot
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A9LE42.json
  locator: primaryAccession; entryType; proteinDescription; genes; organism; entryAudit
  accessed_at: '2026-10-19T07:33:44Z'
  support: supports
  summary: A9LE42 is an active unreviewed TrEMBL entry with submitted protein name
    PKD2, gene PKD2 and taxon 3055. Entry version 49, sequence version 1, annotation
    updated 2026-06-10. This verifies accession/gene/taxon/status only; membrane membership
    is assessed from papers.
  snapshot_sha256: 7ac3d1a5dcf39a997b4059cc8971de89ee677fca19b88645896bc5633d650806
- evidence_id: pazour
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2171396/?pdf=1
  locator: DOI:10.1083/jcb.200504008; Introduction; Figure 2; Results proteomic analysis;
    Discussion membrane-associated proteins; Materials and methods flagellar fractionation
  accessed_at: '2026-10-19T07:33:43Z'
  support: partial
  summary: Full text confirms title/authors/year and Chlamydomonas flagellar membranes.
    Mass spectrometry used wild-type 137c and oda1-1 flagella separated into membrane-plus-matrix
    and axonemal fractions, identifying predicted membrane proteins including a polycystin-2
    homologue. This supports record notes about proteomic candidates. It does not
    directly test selective entry, sorting or retention of the asserted membrane-protein
    set.
  snapshot_sha256: 97a83604a43745f9ae198c5d9caabe96b014011d050ae2d18881d16086d7e06c
- evidence_id: garcia
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6434934/?pdf=1
  locator: DOI:10.1016/j.cub.2018.03.010; Abstract; introductory membrane specialization
    paragraphs; protein/lipid trafficking sections
  accessed_at: '2026-10-19T07:33:43Z'
  support: supports
  summary: Full review text confirms title, Garcia/Raleigh/Reiter authorship and year.
    Ciliary membranes contain distinctive proteins and lipids, remain continuous with
    plasma membrane and incompletely enclose cilia. Lipid bilayers, ciliary targeting/retention
    and selective membrane composition are reviewed. Chlamydomonas agglutinins provide
    a microbial example; many detailed phosphoinositide and receptor mechanisms concern
    animal systems. Aggregate components and bounded nonmechanistic topology are supported.
  snapshot_sha256: df16c207129c2fcbd3e5b5da9817d88c6adb6cf8e2b56e6419edc5fdfe36d9e9
- evidence_id: dentler
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3554728/?pdf=1
  locator: DOI:10.1371/journal.pone.0053366; Abstract; Results Figure 1; Discussion
    secretory pathway and membrane availability
  accessed_at: '2026-10-19T07:33:43Z'
  support: supports
  summary: Full text confirms Dentler 2013 identity. Chlamydomonas experiments, chiefly
    wild-type L8 with relevant motility/IFT mutants, tested regeneration and maintenance
    during brefeldin-A inhibition and surface-protein turnover. Results support membrane
    resupply constraining growth and maintenance. The record keeps the organism explicit,
    avoids claiming purified ciliary lipidomics and contains no unsupported numerical
    estimate.
  snapshot_sha256: 0a9df24e84162ae53b814ddc83724b49438a7f2629fcd76cdd8bd7cd9f5d4b18
- evidence_id: pkd2-localization
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/17984324/
  locator: Huang et al. 2007; DOI:10.1083/jcb.200704069; PubMed Abstract read through
    efetch XML
  accessed_at: '2026-10-19T07:34:54Z'
  support: supports
  summary: The abstract reports cloned Chlamydomonas PKD2, flagellar cleavage products
    and observed PKD2-GFP movement in the flagellar membrane. This independent primary
    support confirms the protein example belongs in the membrane context; it is not
    presently attached to the component evidence in the reviewed record.
  snapshot_sha256: 3ff07be452de5cf6830b4e068602a7e127170eb6f568975be7e6a415c92fc796
- evidence_id: fmg1-localization
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4215714/
  locator: Awata et al. 2014; DOI:10.1242/jcs.155275; Results protein composition;
    Figure 7C; paragraphs on FMG1-B and PKD2
  accessed_at: '2026-10-19T07:34:54Z'
  support: supports
  summary: Directly inspected full-text paragraphs identify FMG1-B as a transmembrane
    flagellar glycoprotein and show its reduced abundance in nphp4 flagella and restoration
    in rescued material, with immunoblot corroboration. PKD2 remains present. These
    experiments support selective composition and the named Chlamydomonas proteins
    more directly than unqualified use of the 2005 inventory.
- evidence_id: history
  kind: record_content
  reference: history/records/ciliary_membrane/
  locator: 2026-09-15T133921Z-codex-03185b.yaml and 2026-09-15T134730Z-codex-930de8.yaml;
    target curation_history
  accessed_at: '2026-10-19T07:33:27Z'
  support: context_only
  summary: Inspected creation and follow-up history record narrow Dentler example
    and label-only lipid edge corrections. The current record preserves PROPOSED status
    and later protein-example provenance; no status promotion is claimed.
- evidence_id: history-search
  kind: search
  reference: history/ and reviews/structured/
  locator: rg --no-ignore --hidden -n ciliary_membrane|GO:0060170|FMG1-B|A9LE42 history
    reviews/structured --glob *.yaml
  accessed_at: '2026-10-19T07:34:34Z'
  support: context_only
  summary: Bounded search found the two target-specific history documents and GO context
    mentions in radial-spoke review bundles. Context mentions do not review this target;
    authoritative coverage remains the coordinator's validated list.
  search_scope: Searched all YAML files below history/ and reviews/structured/, including
    hidden and ignored files, for the exact slug, GO identifier, gene symbol and accession.
    Not a whole-repository absence claim.
- evidence_id: schema-result
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate data/structures/appendage/ciliary_membrane.yaml
  locator: stdout/stderr log retained outside repository
  accessed_at: '2026-10-19T07:33:44Z'
  support: supports
  summary: Focused LinkML schema validation reports No issues found.
  snapshot_sha256: 80ec59f38c2c32b7e98a997ff0c21f83980c3458a18098e534c6a6845b2255d6
- evidence_id: strict-result
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate-strict data/structures/appendage/ciliary_membrane.yaml --out /private/tmp/cellstructure-record-reviews-UhRFh7/ciliary-membrane/strict.tsv
  locator: stdout/stderr log retained outside repository
  accessed_at: '2026-10-19T07:33:44Z'
  support: supports
  summary: Focused closed-schema validation scanned one record with zero error rows.
  snapshot_sha256: c06d84b106723b369319eb17201a987db6306f281c461911fee9ac4332421431
- evidence_id: target-resolver-coverage
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/ciliary_membrane.yaml; exact scripts/check_curies.py
    collect() scope; reports/curie_check.tsv
  accessed_at: '2026-10-19T23:32:25.400320Z'
  support: supports
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
  summary: 'This target contains 10 distinct CURIE-shaped scalar values: 10 OK, 0
    transport-unreachable and 0 skipped in the global report. The attached scoped
    receipts resolve each non-OK identifier. HTTP URLs and prose are outside collect();
    their content was inspected separately. Existence is not proof of correct biological
    mapping.'
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec
  accessed_at: '2026-10-19T07:38:12Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 7b6165ba8532d080a336f7a5a4c29b456fdf7182dd596410b700dfe60af61a06
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-19T07:29:37Z'
  support: supports
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: b98e3eecd58a81fa46033e6baca6977811a439f119b943fd5d9931964adb2680
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad
  accessed_at: '2026-10-19T07:32:39Z'
  support: supports
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-19T07:29:45Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4
  accessed_at: '2026-10-19T08:04:01Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  snapshot_sha256: 7cb413edccc92ee6ce79a32cd2b96a59bc4da37f2cb7b326eaca51a64f723cfb
assessments:
- assessment_id: identity
  area: identity
  topic: Exact microbial membrane domain
  outcome: supported
  summary: GO:0060170 denotes exactly this plasma-membrane domain surrounding a eukaryotic
    cilium; it is a structure, not a protein or phenotype. APPENDAGE/MEMBRANE and
    all synonym scopes are consistent.
  target_ids:
  - GO:0060170
  evidence_ids:
  - record
  - go-authority
  - garcia
- assessment_id: hierarchy
  area: representation
  topic: Is-a parents and cilium parthood
  outcome: supported
  summary: Both parent relations are is-a and cilium is the containing organelle.
    The record does not mistake the membrane for the whole cilium or bacterial flagellum.
  target_ids:
  - GO:0060170
  evidence_ids:
  - go-authority
  - record
- assessment_id: composition
  area: completeness
  topic: Aggregate lipid and protein composition
  outcome: supported
  summary: The two label-only aggregates are explicitly bounded. A lipid phase is
    necessary to a membrane, while protein essentiality is left unknown and molecular
    inventory remains an open question. PKD2 and FMG1-B are legitimate Chlamydomonas
    membrane examples; accession and annotation tier match. Exact conserved lipid
    classes, counts or a universal protein repertoire are not asserted.
  target_ids:
  - GO:0060170
  evidence_ids:
  - record
  - garcia
  - uniprot
  - pkd2-localization
  - fmg1-localization
  details: The inventory TODO is acknowledged scientific incompleteness, not an invented
    defect. Protein example provenance expressly separates identifier verification
    from structural membership.
- assessment_id: taxonomic-scope
  area: scope
  topic: Chlamydomonas presence and example
  outcome: supported
  summary: Species label and taxon match. Membrane-bounded Chlamydomonas flagella
    are directly observed in the proteomics paper, and Dentler used this organism
    for regeneration experiments. COMMON is interpreted qualitatively, not as a measured
    prevalence estimate.
  target_ids:
  - GO:0060170
  evidence_ids:
  - taxonomy
  - pazour
  - dentler
  dimensions:
  - name: taxon_rank
    value: species
    definition: Rank of the sole explicitly asserted distribution/example taxon.
    evidence_ids:
    - taxonomy
  - name: experimental_context
    value: 'Pazour: wild-type 137c and oda1-1 fractionated flagella; Dentler: chiefly
      wild-type L8 regeneration/maintenance with brefeldin A.'
    definition: Organism and preparation limits of the primary evidence.
    evidence_ids:
    - pazour
    - dentler
- assessment_id: function
  area: evidence
  topic: Membrane supply during cilium assembly
  outcome: supported
  summary: Dentler supports the Chlamydomonas-specific assembly/length description.
    GO:0060271 supplies the correct process label; the record does not claim membrane
    supply is the sole length-control mechanism.
  target_ids:
  - GO:0060170
  evidence_ids:
  - go-authority
  - dentler
- assessment_id: graph-topology
  area: graph
  topic: Four nonmechanistic topology and localization edges
  outcome: concern
  summary: The lipid-phase, membrane-boundary and expansion edges are supported at
    their stated scale. The protein-localization edge adds selectively sorted composition
    while citing only a proteomic inventory; the sorting/localization evidence should
    accompany that edge.
  target_ids:
  - GO:0060170
  evidence_ids:
  - record
  - go-authority
  - pazour
  - garcia
  - dentler
  - fmg1-localization
  details: NONMECHANISTIC scope is appropriate. The generic bounds relation does not
    claim complete isolation from cytosol, consistent with the open ciliary base described
    in Garcia. No specific transport machinery is silently asserted as a constituent.
- assessment_id: properties-images
  area: completeness
  topic: Optional measurements, images and datasets
  outcome: not_applicable
  summary: No numerical physical property, image, licence or dataset assertion appears
    in the complete target. Their absence is not a defect under the local checklist.
  target_ids:
  - GO:0060170
  evidence_ids:
  - record
- assessment_id: provenance
  area: provenance
  topic: Evidence placement and scientific status
  outcome: supported
  summary: Citations resolve to the stated works; label-only notes and inventory discussion
    are explicit. The target remains PROPOSED and carries curation provenance. Available
    repository-level history records the initial creation and earlier evidence narrowing.
  target_ids:
  - GO:0060170
  evidence_ids:
  - record
  - history
  - pazour
  - garcia
  - dentler
  - uniprot
findings:
- finding_id: F1
  issue_key: ciliary-membrane-sorted-protein-edge-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Selective membrane-protein composition needs evidence on its graph edge
  description: The localize-to edge describes a sorted set of Chlamydomonas membrane
    proteins but cites only Pazour 2005, whose pertinent result is detection of predicted
    membrane proteins in fractionated flagella. That experiment alone does not establish
    selective sorting or retention in the membrane. Garcia 2018, already cited elsewhere
    in the record, reviews membrane targeting/retention; Awata 2014 provides Chlamydomonas
    experiments on selective composition including FMG1-B and PKD2. Attach appropriate
    evidence at this edge or narrow its wording to the proteomic observation. This
    is a bounded evidence-placement gap, not evidence that the proteins or membrane
    are biologically wrong.
  target_ids:
  - GO:0060170
  field_paths:
  - causal_graphs[graph_id=ciliary_membrane_bounds_ciliary_compartment].edges[subject=ciliary_membrane_proteins].description
  - causal_graphs[graph_id=ciliary_membrane_bounds_ciliary_compartment].edges[subject=ciliary_membrane_proteins].evidence
  evidence_ids:
  - record
  - pazour
  - garcia
  - fmg1-localization
  rule_id: review-checklist/evidence-standard+narrowest-claim
  native_severity: minor
  normalization_reason: The underlying membership and selective composition are independently
    supported, and related support is present elsewhere in the record; the defect
    is limited to the precision and placement of one edge citation.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_membrane.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Curator should attach the existing Garcia review and/or a Chlamydomonas
    localization/sorting study to the protein-localization edge, explicitly distinguishing
    proteomic candidates from experimentally localized or selectively retained proteins.
    Alternatively narrow the edge description to what Pazour directly establishes.
  finding_ids:
  - F1
  target_ids:
  - GO:0060170
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_membrane.yaml
    role: maintained scientific record
  acceptance_checks:
  - Read the selected source context and confirm it supports every retained qualifier
    at the edge.
  - Use write_validated_structure with an append-only curation event and repository
    history for any later authorized mutation.
  - Run just validate, just validate-strict and just qc; regenerate pages with just
    render only as part of separately authorized curation.
  generator: No generated input owns the scientific record; any later generated-page
    update uses just render.
limitations:
- Pazour 2005 provides purified-flagellum proteomics and predicted membrane associations;
  its supplemental molecular inventory was not retrieved. Exact FMG1-B identity and
  flagellar association were independently corroborated in Awata 2014, and PKD2 membrane
  localization in Huang 2007.
- Huang 2007 was inspected at the PubMed abstract tier after PMC and publisher body
  access failures. The three papers already cited by the record were all inspected
  as full text.
- Review is limited to stated biological claims and proportionate completeness; it
  does not establish an exhaustive cross-taxon lipid/protein inventory or measure
  population prevalence.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The user explicitly requested one validated bundle per previously unreviewed record;
  that instruction overrides the local issue-only persistence gate.
- No record, generated page, curation history, or external communication was modified.
- No verbatim paper quotations are reproduced.
```
