# Y-shaped link identity, microscopy and protein provenance

- Review: 20261020T033236Z-y-shaped-link-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-19T23:40:32.963836Z
- Finished UTC: 2026-10-20T03:32:36Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact linker identity, bounded tethering mechanism and versioned microscopy are supported. Two minor issues remain: stale no-example caveats and inaccurate source placement for the CEP290 locus alias.

## Scope And Provenance

Entire target, all scientific surfaces, one image entry and two graph edges assessed.

Selection: Nineteenth originally unreviewed path; ninth target of batch2.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097537 | data/structures/appendage/y_shaped_link.yaml | maintained | Y-shaped link |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0097537 | Focused validator passed; captured log retained. |
| Focused native strict | passed | True | GO:0097537 | Focused validator passed; captured log retained. |
| All material claims and identifiers | passed | True | GO:0097537 | Full source, current authorities, versioned figure metadata and directly viewed microscopy were checked. Two minor provenance/consistency issues observed; no unresolved required source gap. |
| Native protein verification and graph coverage | passed | False | GO:0097537 | Scoped native protein verification reported all examples/xrefs verified. Graph coverage reported PARTIAL_EXAMPLES for POC3; primary source establishes POC3/CEP290 alias, so it is not evidence for a second missing constituent. |
| Target resolver residuals | passed | True | GO:0097537 | All collected target identifiers have appropriate authority/local verification; DOI/PMID joins and exact versioned figure identity are explicit. |
| Full corpus QC | passed | True | GO:0097537 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097537 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097537 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097537 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0097537 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact complex, synonyms and hierarchy

identity: supported. Targets: GO:0097537.

Exact GO identity and relation types are supported. The whole transition zone and external transition fibers are distinct; the GO definition retains regional gating context.

### CEP290-associated constituent and essentiality

grounding: supported. Targets: GO:0097537.

Family identity and localized association support the constituent. UNKNOWN avoids overstating absolute assembly necessity; the record acknowledges rare residual connectors and additional proteins.

### Representative locus mapping and source placement

provenance: concern. Targets: GO:0097537.

The selected accession is a supported gene representative when the resource-center mapping and primary alias are considered. UniProt alone does not provide the claimed primary CEP290 name. The current model is2518 residues versus2516 in the historical figure; a matching terminal peptide and locus context do not prove exact experimental-sequence identity.

### Bounded Chlamydomonas model

scope: supported. Targets: GO:0097537.

The exact species and wild-type/deletion/complementation context are correct. No distribution-frequency assertion or broad taxonomic generalization is present.

### Tethering and both edges

graph: supported. Targets: GO:0097537.

Localization and mutant/extraction comparisons support normal architecture and ensemble tethering. The graph preserves the affected wedge structures and does not assert Y-link-only sufficiency, direct lipid binding or molecular gating.

### Figure identity, caption and licence

provenance: supported. Targets: GO:0097537.

Literal versioned resource, native JATS and both image checksums resolve. Attribution, exact licence URL, TEM modality and panel-specific caption match; the record hosts only a link.

### Open inventory and stale no-example statements

completeness: concern. Targets: GO:0097537.

Additional composition, stoichiometry and linker-specific gating remain legitimate open questions. Statements that no organism-specific accession is asserted and examples remain unset contradict the populated example.

### Native status and optional fields

provenance: supported. Targets: GO:0097537.

PROPOSED status is retained. No quantitative property, dataset or trait link is claimed; optional omissions do not warrant invented defects.

## Findings

### F1: Accession caveats are stale after protein enrichment

minor / open / confirmed; issue key: y-shaped-link-stale-no-protein-example.

The component grounding note says no organism-specific accession is asserted, and the inventory discussion says protein examples remain unset. A0A2K3DWT6 is now present. Update only those stale statements while preserving unresolved exact experimental-sequence correspondence, stoichiometry and additional constituents.

### F2: The named-gene correspondence needs its actual source

minor / open / confirmed; issue key: y-shaped-link-cep290-alias-source-placement.

The example role says UniProt lists CHLRE_03g167550v5 as the primary name for CEP290, but the entry supplies only an ORF name and no CEP290/POC3 token. Cite the resource-center locus mapping and paper alias explicitly; describe the UniProt field accurately. This does not establish a wrong accession.

## Recommended Actions And Acceptance Checks

### A1

Refresh stale no-example caveats, and attach the actual locus/alias evidence to the protein example. Preserve uncertainty about exact historical sequence identity and uncharacterized linker constituents.

- Current notes agree with the populated example and distinguish ORF names from primary gene names.
- The CEP290/POC3-to-locus mapping is traceable to its source; no family-only or terminal-peptide-only proof of exact historical sequence is claimed.
- After separately authorized curation, run focused open/strict checks and native history gates; derive pages with just render.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0097537%2CGO%3A0032991%2CGO%3A0035869%2CGO%3A0097539; Exact IDs, names, definitions, synonyms and relevant children | supports | All four terms are active; definition and seven related synonyms match. The source directly represents Y-link is-a protein-containing complex and part-of transition zone. Transition fiber remains distinct. |
| go-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0097537/ancestors?relations=is_a; GO:0097537 is_a ancestor response | supports | GO:0032991 is an is-a ancestor of the exact linker term. |
| interpro | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026201; metadata accession/name/type | supports | IPR026201 is the Centrosomal protein of 290kDa family, not the complete linker complex. |
| uniprot | https://rest.uniprot.org/uniprotkb/A0A2K3DWT6.json; entryType, proteinDescription, genes, organism and sequence | supports | A0A2K3DWT6 is an unreviewed 2518-residue Chlamydomonas protein with the matching label and ORF name CHLRE_03g167550v5. It has no primary geneName or CEP290/POC3 synonym in the retrieved entry. |
| gene | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&amp;id=5728998&amp;retmode=json; result5728998, nomenclature and genomicinfo | supports | NCBI Gene5728998 identifies the same ORF on chromosome3 with37 exons. This confirms locus context, not the named CEP290/POC3 alias by itself. |
| crc | https://www.chlamycollection.org/products/clip-strains/page/430/; CLiP catalogue entries listing POC3,CEP290 (Cre03.g167550) | supports | The Chlamydomonas Resource Center identifies Cre03.g167550 with both POC3 and CEP290. This is the missing source for the named-gene/locus correspondence; no claim about an individual insertion position is adopted. |
| taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3055; Top-level taxon identity | supports | NCBITaxon:3055 is Chlamydomonas reinhardtii. |
| paper-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20819941%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Exact top-level article result | supports | PMID20819941, PMC2935561 and DOI10.1083/jcb.201006105 identify Craige et al.2010 with the recorded title and authors. |
| paper | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2935561/fullTextXML; Identification, connector-defect/localization Results; Discussion; antibody/EM methods; Figures3–4 captions | supports | Full Results, Discussion and Methods support the scoped constituent, tethering and two-edge graph. Rare connectors in the null mutant and uncertainty about wedge equivalence limit the mechanism. The paper explicitly equates CEP290 and POC3. |
| figure3 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b4c8/2935561/d7002d41b063/JCB_201006105_GS_Fig3.jpg; Figure3 A–J; original CDN bytes | supports | Figure visually checked: caption and panel assignments match; averages are distinguished from individual connectors and scale bars vary. |
| figure4 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b4c8/2935561/164fdfcb1941/JCB_201006105_GS_Fig4.jpg; Figure4 A–D; original CDN bytes | supports | Figure visually checked: immunogold locations aggregate multiple sections, and the middle/C-terminal epitopes are distinguished. |
| version-metadata | https://pmc-oa-opendata.s3.amazonaws.com/PMC2935561.1/PMC2935561.1.json; Version, identifiers, licence_code, media_urls | supports | Official metadata identifies PMC2935561 version1, the exact DOI/PMID and CC BY-NC-SA licence. Downloaded figures3/4 match the listed MD5 values. |
| idconv | https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=PMC2935561&amp;format=json&amp;versions=yes; records and versions | supports | The official version-aware identifier conversion resolves PMC2935561.1 as the current article version. |
| native-version | https://pmc-oa-opendata.s3.amazonaws.com/PMC2935561.1/PMC2935561.1.xml; Official versioned JATS permissions and exact MD5 | supports | The native JATS MD5 matches version metadata. Permissions specify CC BY-NC-SA3.0, matching OTHER plus exact licence URL. Link-only representation avoids copying image bytes into this repository. |
| record | data/structures/appendage/y_shaped_link.yaml; Entire file | context_only | Complete target read, including the populated protein example and contradictory old accession caveats. All internal node/component/discussion references resolve. |
| history | history/records/y_shaped_link/2026-10-04T061144Z-codex-72cb15.yaml; Creation event plus target curation_history and later enrichment | context_only | Creation recorded an intentionally unresolved accession; later protein enrichment explains why unchanged no-example caveats are stale. PROPOSED status remains appropriate. |
| schema-result | just validate data/structures/appendage/y_shaped_link.yaml; Delegated focused check log, reported exit0 | supports | uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/appendage/y_shaped_link.yaml<br>No issues found |
| strict-result | just validate-strict data/structures/appendage/y_shaped_link.yaml --out /private/tmp/cellstructure-batch2-20261019-52rdp0/y-shaped-link/strict.tsv; Delegated focused check log, reported exit0 | supports | uv run python scripts/validate_strict.py data/structures/appendage/y_shaped_link.yaml --out /private/tmp/cellstructure-batch2-20261019-52rdp0/y-shaped-link/strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch2-20261019-52rdp0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch2-20261019-52rdp0/y-shaped-link/strict.tsv |
| target-resolver-coverage | just check-curies-strict; data/structures/appendage/y_shaped_link.yaml; exact collect() scope; reports/curie_check.tsv | supports | Ten CURIE-shaped scalars: eight OK, PMID20819941 transport-unreachable due to global batchHTTP414, and PMC2935561.1:fig3 skipped. Exact article metadata and versioned-figure receipts resolve both residuals. HTTP URLs and prose were inspected separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- A representative modern locus model is not necessarily the exact2516-residue experimental sequence; full historical sequence correspondence remains unresolved as the record already notes.
- The evidence concerns the connector ensemble, including wedge densities; linker-only sufficiency and gating mechanisms remain outside scope.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The review began with the timestamped delegated inspect artifact and was completed by the coordinating reviewer after source and figure reinspection.
- The user explicitly authorized one bundle for every unreviewed record. No maintained record, status, page or history was changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T033236Z-y-shaped-link-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Y-shaped link identity, microscopy and protein provenance
started_at: '2026-10-19T23:40:32.963836Z'
finished_at: '2026-10-20T03:32:36Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Delegated inspection and coordinating source audit; historical
    agent authorship is not independent human validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Exact linker identity, bounded tethering mechanism and versioned microscopy
  are supported. Two minor issues remain: stale no-example caveats and inaccurate
  source placement for the CEP290 locus alias.'
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: AGENTS.md
    sha256: ed0004703d4f76d2677e3fdf67aa39ef9a6c2c35ef2b51ec053fbaed9ba1ac86
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/appendage/ciliary_transition_fiber.yaml
    sha256: e26c76e51de98b9049c8ca7e2eaec7adc5412fc22c0d39174f6f8a9ef1af1d32
    role: context
  - path: data/structures/appendage/ciliary_transition_zone.yaml
    sha256: 86788583f1b2b4cb8bf5ac4e77323059cf48023b4c713a0d82b57ed4a066daa1
    role: context
  - path: data/structures/appendage/y_shaped_link.yaml
    sha256: 5fddc5796ce37906bdfd10a8e3a91cdb6b6ca38e4a78c04df65c88ac518c3eb7
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
  - path: history/README.md
    sha256: 1636df44f28547f440242afcb4a05ac293b9714b4d7b809cecc30b975e44a522
    role: context
  - path: history/infrastructure/uniprot-protein-examples/2026-10-18T053500Z-claude-code-1d4cdb.yaml
    sha256: 72f669bcf4fd3ecb68dc4bd592c937858602f7415ebba38d870cc7e73c8a7d1d
    role: context
  - path: history/records/y_shaped_link/2026-10-04T061144Z-codex-72cb15.yaml
    sha256: 310687cccc74fe854472c0160bddea5f0dcbf859fda7dc21b99deef3f4c59809
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261010T233617Z-ciliary-transition-zone-disposition/review.yaml
    sha256: f1cadc347f27ecb0512bd0cef31e5afa4cbb85bda076f1e8a0a9f6be15f16b57
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
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0097537
  path: data/structures/appendage/y_shaped_link.yaml
  label: Y-shaped link
  record_class: CellStructureRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/y_shaped_link.yaml
    role: maintained scientific record
scope:
  description: Entire target, all scientific surfaces, one image entry and two graph
    edges assessed.
  selection: Nineteenth originally unreviewed path; ninth target of batch2.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097537
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0097537
  command: just validate data/structures/appendage/y_shaped_link.yaml
  exit_code: 0
  summary: Focused validator passed; captured log retained.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0097537
  command: just validate-strict data/structures/appendage/y_shaped_link.yaml --out
    /private/tmp/cellstructure-batch2-20261019-52rdp0/y-shaped-link/strict.tsv
  exit_code: 0
  summary: Focused validator passed; captured log retained.
  evidence_ids:
  - strict-result
- check_id: source-audit
  name: All material claims and identifiers
  status: passed
  required: true
  target_ids:
  - GO:0097537
  summary: Full source, current authorities, versioned figure metadata and directly
    viewed microscopy were checked. Two minor provenance/consistency issues observed;
    no unresolved required source gap.
  evidence_ids:
  - go
  - go-isa
  - interpro
  - uniprot
  - gene
  - crc
  - taxon
  - paper-metadata
  - paper
  - figure3
  - figure4
  - version-metadata
  - idconv
  - native-version
  - record
  - history
  - schema-result
  - strict-result
- check_id: protein-native
  name: Native protein verification and graph coverage
  status: passed
  required: false
  target_ids:
  - GO:0097537
  summary: Scoped native protein verification reported all examples/xrefs verified.
    Graph coverage reported PARTIAL_EXAMPLES for POC3; primary source establishes
    POC3/CEP290 alias, so it is not evidence for a second missing constituent.
  evidence_ids:
  - uniprot
  - paper
  - crc
- check_id: target-resolver-coverage
  name: Target resolver residuals
  status: passed
  required: true
  target_ids:
  - GO:0097537
  summary: All collected target identifiers have appropriate authority/local verification;
    DOI/PMID joins and exact versioned figure identity are explicit.
  evidence_ids:
  - target-resolver-coverage
  - paper-metadata
  - version-metadata
  - idconv
  - native-version
  - figure3
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097537
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0097537
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0097537
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0097537
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0097537
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0097537%2CGO%3A0032991%2CGO%3A0035869%2CGO%3A0097539
  locator: Exact IDs, names, definitions, synonyms and relevant children
  accessed_at: '2026-10-19T23:40:53Z'
  support: supports
  summary: All four terms are active; definition and seven related synonyms match.
    The source directly represents Y-link is-a protein-containing complex and part-of
    transition zone. Transition fiber remains distinct.
  snapshot_sha256: 10c01aa5a17e37380a94b4d01efeb5b8a78b43d7c1ebe3a321b800b68a94f5de
- evidence_id: go-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0097537/ancestors?relations=is_a
  locator: GO:0097537 is_a ancestor response
  accessed_at: '2026-10-19T23:40:53Z'
  support: supports
  summary: GO:0032991 is an is-a ancestor of the exact linker term.
  snapshot_sha256: 9a75fa7b16a8162200d2cba998c88cd57e51433ef81ccd0aa50806df5c8020dc
- evidence_id: interpro
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026201
  locator: metadata accession/name/type
  accessed_at: '2026-10-19T23:40:53Z'
  support: supports
  summary: IPR026201 is the Centrosomal protein of 290kDa family, not the complete
    linker complex.
  snapshot_sha256: 6128f1c9582592d0becda0a6383c3e0933b0dbf7130d9cb5fd0aeb641fa0ca0f
- evidence_id: uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0A2K3DWT6.json
  locator: entryType, proteinDescription, genes, organism and sequence
  accessed_at: '2026-10-19T23:40:53Z'
  support: supports
  summary: A0A2K3DWT6 is an unreviewed 2518-residue Chlamydomonas protein with the
    matching label and ORF name CHLRE_03g167550v5. It has no primary geneName or CEP290/POC3
    synonym in the retrieved entry.
  snapshot_sha256: 2e8f6214c08ae3f786a8184d814b6051335991d83e2d80d7c2a0081942e0fd49
- evidence_id: gene
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=5728998&retmode=json
  locator: result5728998, nomenclature and genomicinfo
  accessed_at: '2026-10-19T23:41:16Z'
  support: supports
  summary: NCBI Gene5728998 identifies the same ORF on chromosome3 with37 exons. This
    confirms locus context, not the named CEP290/POC3 alias by itself.
  snapshot_sha256: 670e7a7df310ce3f5fb75180c773c31291ac399681ca7b2038b893e7824bea14
- evidence_id: crc
  kind: authority
  reference: https://www.chlamycollection.org/products/clip-strains/page/430/
  locator: CLiP catalogue entries listing POC3,CEP290 (Cre03.g167550)
  accessed_at: '2026-10-19T23:42:52Z'
  support: supports
  summary: The Chlamydomonas Resource Center identifies Cre03.g167550 with both POC3
    and CEP290. This is the missing source for the named-gene/locus correspondence;
    no claim about an individual insertion position is adopted.
  snapshot_sha256: 79edec0cdb352c07079d18301f7a7d0f5285235f064c56f152f8a117697ba23a
- evidence_id: taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3055
  locator: Top-level taxon identity
  accessed_at: '2026-10-19T23:40:53Z'
  support: supports
  summary: NCBITaxon:3055 is Chlamydomonas reinhardtii.
  snapshot_sha256: a17bc1c97fea9112288574ef15727ed7e37c42787a430ef074ae5fc654547e6b
- evidence_id: paper-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20819941%20AND%20SRC:MED&format=json&resultType=core
  locator: Exact top-level article result
  accessed_at: '2026-10-19T23:40:53Z'
  support: supports
  summary: PMID20819941, PMC2935561 and DOI10.1083/jcb.201006105 identify Craige et
    al.2010 with the recorded title and authors.
  snapshot_sha256: 7784f20cdd0bc8485f541da3d4ecb95ec8909d504619b7c023cae3792eeeef91
- evidence_id: paper
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2935561/fullTextXML
  locator: Identification, connector-defect/localization Results; Discussion; antibody/EM
    methods; Figures3–4 captions
  accessed_at: '2026-10-19T23:40:54Z'
  support: supports
  summary: Full Results, Discussion and Methods support the scoped constituent, tethering
    and two-edge graph. Rare connectors in the null mutant and uncertainty about wedge
    equivalence limit the mechanism. The paper explicitly equates CEP290 and POC3.
  snapshot_sha256: a83f54c0f615e5ac6f3fa935a59ace211da887d0d8c92cbebf04dddc25715f7c
- evidence_id: figure3
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b4c8/2935561/d7002d41b063/JCB_201006105_GS_Fig3.jpg
  locator: Figure3 A–J; original CDN bytes
  accessed_at: '2026-10-19T23:42:12Z'
  support: supports
  summary: 'Figure visually checked: caption and panel assignments match; averages
    are distinguished from individual connectors and scale bars vary.'
  snapshot_sha256: acd15f385e9e726a865413abec893d3f329ce1c84f565caf63b7949942d30624
- evidence_id: figure4
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b4c8/2935561/164fdfcb1941/JCB_201006105_GS_Fig4.jpg
  locator: Figure4 A–D; original CDN bytes
  accessed_at: '2026-10-19T23:42:51Z'
  support: supports
  summary: 'Figure visually checked: immunogold locations aggregate multiple sections,
    and the middle/C-terminal epitopes are distinguished.'
  snapshot_sha256: face3676b8e007ea9d8a5d615669eeae9e95a7d21c9955324eeb4a0aecb9a11a
- evidence_id: version-metadata
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2935561.1/PMC2935561.1.json
  locator: Version, identifiers, licence_code, media_urls
  accessed_at: '2026-10-19T23:42:51Z'
  support: supports
  summary: Official metadata identifies PMC2935561 version1, the exact DOI/PMID and
    CC BY-NC-SA licence. Downloaded figures3/4 match the listed MD5 values.
  snapshot_sha256: ca9913ba27c82451977434d271d442ca8df7ced8337483a2c4df27ccf9d46742
- evidence_id: idconv
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=PMC2935561&format=json&versions=yes
  locator: records and versions
  accessed_at: '2026-10-19T23:42:51Z'
  support: supports
  summary: The official version-aware identifier conversion resolves PMC2935561.1
    as the current article version.
  snapshot_sha256: 10dd3871c4a219e27596e50086139fe3b0b8cade202aa56e0a6bc81c62e71da9
- evidence_id: native-version
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2935561.1/PMC2935561.1.xml
  locator: Official versioned JATS permissions and exact MD5
  accessed_at: '2026-10-20T03:30:43.154807Z'
  support: supports
  summary: The native JATS MD5 matches version metadata. Permissions specify CC BY-NC-SA3.0,
    matching OTHER plus exact licence URL. Link-only representation avoids copying
    image bytes into this repository.
  snapshot_sha256: 16b42e69696668b0d2464aca13cc3163fcc0f557d034dfa99efa055a9b728ac1
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/y_shaped_link.yaml
  locator: Entire file
  accessed_at: '2026-10-20T03:31:49Z'
  support: context_only
  summary: Complete target read, including the populated protein example and contradictory
    old accession caveats. All internal node/component/discussion references resolve.
- evidence_id: history
  kind: record_content
  reference: history/records/y_shaped_link/2026-10-04T061144Z-codex-72cb15.yaml
  locator: Creation event plus target curation_history and later enrichment
  accessed_at: '2026-10-20T03:31:49Z'
  support: context_only
  summary: Creation recorded an intentionally unresolved accession; later protein
    enrichment explains why unchanged no-example caveats are stale. PROPOSED status
    remains appropriate.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/appendage/y_shaped_link.yaml
  locator: Delegated focused check log, reported exit0
  accessed_at: '2026-10-19T23:40:53.141276Z'
  support: supports
  summary: 'uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/y_shaped_link.yaml

    No issues found'
  snapshot_sha256: 87afabcaa3a569079db20f682e5126286533f6554c19e1a0f97dd1e0b9812853
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/appendage/y_shaped_link.yaml --out
    /private/tmp/cellstructure-batch2-20261019-52rdp0/y-shaped-link/strict.tsv
  locator: Delegated focused check log, reported exit0
  accessed_at: '2026-10-19T23:40:54.989591Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/appendage/y_shaped_link.yaml\
    \ --out /private/tmp/cellstructure-batch2-20261019-52rdp0/y-shaped-link/strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch2-20261019-52rdp0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch2-20261019-52rdp0/y-shaped-link/strict.tsv"
  snapshot_sha256: 04d786b55b256d0f5caeac1c631dc2d939bb6036c9510b77a828605c37f216f6
- evidence_id: target-resolver-coverage
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/y_shaped_link.yaml; exact collect() scope; reports/curie_check.tsv
  accessed_at: '2026-10-19T23:41:41.324461Z'
  support: supports
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
  summary: 'Ten CURIE-shaped scalars: eight OK, PMID20819941 transport-unreachable
    due to global batchHTTP414, and PMC2935561.1:fig3 skipped. Exact article metadata
    and versioned-figure receipts resolve both residuals. HTTP URLs and prose were
    inspected separately.'
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
  topic: Exact complex, synonyms and hierarchy
  outcome: supported
  summary: Exact GO identity and relation types are supported. The whole transition
    zone and external transition fibers are distinct; the GO definition retains regional
    gating context.
  target_ids:
  - GO:0097537
  evidence_ids:
  - go
  - go-isa
  - record
- assessment_id: component
  area: grounding
  topic: CEP290-associated constituent and essentiality
  outcome: supported
  summary: Family identity and localized association support the constituent. UNKNOWN
    avoids overstating absolute assembly necessity; the record acknowledges rare residual
    connectors and additional proteins.
  target_ids:
  - GO:0097537
  evidence_ids:
  - interpro
  - paper
  - figure4
  - record
- assessment_id: protein
  area: provenance
  topic: Representative locus mapping and source placement
  outcome: concern
  summary: The selected accession is a supported gene representative when the resource-center
    mapping and primary alias are considered. UniProt alone does not provide the claimed
    primary CEP290 name. The current model is2518 residues versus2516 in the historical
    figure; a matching terminal peptide and locus context do not prove exact experimental-sequence
    identity.
  target_ids:
  - GO:0097537
  evidence_ids:
  - uniprot
  - gene
  - crc
  - paper
  - figure4
- assessment_id: scope
  area: scope
  topic: Bounded Chlamydomonas model
  outcome: supported
  summary: The exact species and wild-type/deletion/complementation context are correct.
    No distribution-frequency assertion or broad taxonomic generalization is present.
  target_ids:
  - GO:0097537
  evidence_ids:
  - taxon
  - paper
  - record
- assessment_id: function-graph
  area: graph
  topic: Tethering and both edges
  outcome: supported
  summary: Localization and mutant/extraction comparisons support normal architecture
    and ensemble tethering. The graph preserves the affected wedge structures and
    does not assert Y-link-only sufficiency, direct lipid binding or molecular gating.
  target_ids:
  - GO:0097537
  evidence_ids:
  - paper
  - figure3
  - figure4
  - record
- assessment_id: image
  area: provenance
  topic: Figure identity, caption and licence
  outcome: supported
  summary: Literal versioned resource, native JATS and both image checksums resolve.
    Attribution, exact licence URL, TEM modality and panel-specific caption match;
    the record hosts only a link.
  target_ids:
  - GO:0097537
  evidence_ids:
  - version-metadata
  - idconv
  - native-version
  - figure3
  - paper-metadata
  - record
- assessment_id: discussion
  area: completeness
  topic: Open inventory and stale no-example statements
  outcome: concern
  summary: Additional composition, stoichiometry and linker-specific gating remain
    legitimate open questions. Statements that no organism-specific accession is asserted
    and examples remain unset contradict the populated example.
  target_ids:
  - GO:0097537
  evidence_ids:
  - record
  - history
  - paper
- assessment_id: status
  area: provenance
  topic: Native status and optional fields
  outcome: supported
  summary: PROPOSED status is retained. No quantitative property, dataset or trait
    link is claimed; optional omissions do not warrant invented defects.
  target_ids:
  - GO:0097537
  evidence_ids:
  - record
  - history
findings:
- finding_id: F1
  issue_key: y-shaped-link-stale-no-protein-example
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Accession caveats are stale after protein enrichment
  description: The component grounding note says no organism-specific accession is
    asserted, and the inventory discussion says protein examples remain unset. A0A2K3DWT6
    is now present. Update only those stale statements while preserving unresolved
    exact experimental-sequence correspondence, stoichiometry and additional constituents.
  target_ids:
  - GO:0097537
  field_paths:
  - components[0].grounding_notes
  - discussions[discussion_id=complete_linker_inventory_and_protein_examples].notes
  evidence_ids:
  - record
  - history
  - uniprot
  rule_id: review-checklist:Components and Discussions/datasets
  native_severity: minor
  normalization_reason: Nonblocking current-record consistency/provenance issue; the
    linker identity and scoped mechanism remain supported.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/y_shaped_link.yaml
    role: maintained scientific record
- finding_id: F2
  issue_key: y-shaped-link-cep290-alias-source-placement
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The named-gene correspondence needs its actual source
  description: The example role says UniProt lists CHLRE_03g167550v5 as the primary
    name for CEP290, but the entry supplies only an ORF name and no CEP290/POC3 token.
    Cite the resource-center locus mapping and paper alias explicitly; describe the
    UniProt field accurately. This does not establish a wrong accession.
  target_ids:
  - GO:0097537
  field_paths:
  - components[0].protein_examples[0].role
  - components[0].protein_examples[0].evidence[0].notes
  evidence_ids:
  - uniprot
  - gene
  - crc
  - paper
  rule_id: review-checklist:Components and Discussions/datasets
  native_severity: minor
  normalization_reason: Nonblocking current-record consistency/provenance issue; the
    linker identity and scoped mechanism remain supported.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/y_shaped_link.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Refresh stale no-example caveats, and attach the actual locus/alias
    evidence to the protein example. Preserve uncertainty about exact historical sequence
    identity and uncharacterized linker constituents.
  finding_ids:
  - F1
  - F2
  target_ids:
  - GO:0097537
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/y_shaped_link.yaml
    role: maintained scientific record
  acceptance_checks:
  - Current notes agree with the populated example and distinguish ORF names from
    primary gene names.
  - The CEP290/POC3-to-locus mapping is traceable to its source; no family-only or
    terminal-peptide-only proof of exact historical sequence is claimed.
  - After separately authorized curation, run focused open/strict checks and native
    history gates; derive pages with just render.
  generator: Maintained YAML owns the change; just render derives pages.
limitations:
- A representative modern locus model is not necessarily the exact2516-residue experimental
  sequence; full historical sequence correspondence remains unresolved as the record
  already notes.
- The evidence concerns the connector ensemble, including wedge densities; linker-only
  sufficiency and gating mechanisms remain outside scope.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The review began with the timestamped delegated inspect artifact and was completed
  by the coordinating reviewer after source and figure reinspection.
- The user explicitly authorized one bundle for every unreviewed record. No maintained
  record, status, page or history was changed.
```
