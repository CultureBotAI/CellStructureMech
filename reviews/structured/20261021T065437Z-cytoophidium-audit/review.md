# Cytoophidium identity, curvature mechanism and component-family review

- Review: 20261021T065437Z-cytoophidium-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T06:52:03Z
- Finished UTC: 2026-10-21T06:54:37Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Cytoophidium identity, Caulobacter CtpS membership, strain examples and the scoped curvature graph are supported. One minor finding concerns withholding the verified CTP synthase family mapping on an assembly-specific cohort criterion.

## Scope And Provenance

Complete read-only review of the target YAML, all stable identifiers, internal crescentin reference, discovery manuscript and the cited 2023 review’s broad occurrence statement.

Selection: Second unreviewed path in batch six, following cryptophyte cortical centrin network; one record per saved bundle in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097268 | data/structures/cytoskeleton/cytoophidium.yaml | maintained | cytoophidium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0097268 | Focused validator passed. |
| Focused native strict | passed | True | GO:0097268 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0097268 | 12 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0097268 | This record makes no transcriptional regulation or expression-module assertion. Native protein/taxon authorities and the direct filament experiments address its actual claims. |
| Claim-level scientific review | passed | True | GO:0097268 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0097268 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097268 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097268 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097268 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0097268 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Ontology-grounded enzyme assembly

identity: supported. Targets: GO:0097268.

Exact native ontology identity and supramolecular-fiber parent are supported. Related CTPS/CtpS synonyms do not redefine every metabolic-enzyme cytoophidium as a single enzyme class.

### Caulobacter constituent and strain examples

evidence: supported. Targets: GO:0097268.

Discovery experiments, rather than automated sequence annotations, support CtpS filament membership. Both curated protein examples have matching enzyme, gene, strain and reviewed status. UNKNOWN essentiality avoids conflating catalytic viability with universal assembly necessity.

### Generic family versus assembly-specific cohort

grounding: concern. Targets: GO:0097268.

The target withholds an exact verified CTP synthase family because it seeks a term restricted to cytoophidium-forming proteins. That narrower criterion is unnecessary for this generic component class; the experimental assembly role can retain its scope after family grounding.

### Occurrence across domains and laboratory strain context

scope: supported. Targets: GO:0097268.

The review abstract supports variable occurrence across Bacteria, Archaea and Eukaryota. CB15N is the direct laboratory imaging example. COMMON is qualitative occurrence, not a claim that every cell or strain contains a visible filament; native-expression ECT detected bundles in a subset of cells.

### Four scoped nonmechanistic edges

graph: supported. Targets: GO:0097268.

Assembly, changing inner-curvature localization, functional interaction with crescentin and curvature regulation are experimentally supported. The source shows negative regulation: overexpression straightens and depletion hypercurves. Read with neutral regulates/tune edges, the description supports normal curved morphology without asserting a positive dose-response or direct molecular contact.

### Interacting filaments and mesoscale terminology

consistency: supported. Targets: GO:0097268.

Crescentin remains a separate filament; its absence affects CtpS positioning and morphogenesis without preventing filament formation. The 2023 terminology distinguishes mesoscale cytoophidia from elementary enzyme polymers; the related synonym and whole-assembly ontology identity do not require a structural split in this bounded review.

### Supported example with resolvable family TODO

completeness: supported. Targets: GO:0097268.

No unsupported measurement, image, trait or molecular mechanism is asserted. The generic CTPS family discussion has a concrete verified resolution; broad enzyme-composition diversity is not claimed to be exhaustively catalogued.

## Findings

### F1: Assembly-specific cohort criterion blocks verified CTP synthase family grounding

minor / open / confirmed; issue key: cytoophidium-ctp-synthase-family-grounding-scope.

The generic CTP synthase component is REVIEWED_LABEL_ONLY because the rationale seeks a term restricted to cytoophidium-forming CTPS. IPR004468 is the exact whole CTP synthase family and both taxon-paired examples carry it. The repository component model separates family identity from experimental assembly role. Resolve the missing mapping and reconcile the rationale/TODO without claiming universal filament formation.

## Recommended Actions And Acceptance Checks

### A1

Under separately authorized curation, map the generic CTP synthase component to InterPro:IPR004468, reconcile grounding status/notes and resolve the family TODO. Preserve lineage-specific assembly evidence, protein examples and UNKNOWN essentiality.

- Native InterPro confirms exact CTP synthase family name/type; both examples retain that mapping.
- Role and evidence remain limited to demonstrated filament-forming contexts; no universal family-wide assembly claim is added.
- Run schema, strict, controlled-label, history and generated-page checks after curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cytoophidium-agent-discovery-pdf | https://authors.library.caltech.edu/records/q1v55-6sf11/files/nihms215754.pdf; Ingerson-Mahar et al. 2010 accepted manuscript: Results pp. 2–7, Figures 1–5, Methods p. 8; independently read through PMC and the deposited PDF | supports | The complete accepted manuscript supports CtpS-dependent filaments in Caulobacter CB15N, dynamic localization, crescentin-dependent morphogenic effects and separability from catalytic activity. Overexpression straightens cells and depletion hypercurves them: the source describes negative regulation, not positive promotion of curvature. E. coli native and purified CtpS form filaments. The durable repository file URL is cited; the retained request receipt records its public signed-download redirect. |
| review-abstract | https://pubmed.ncbi.nlm.nih.gov/37248970/; Guo and Liu 2023, DOI 10.1042/BST20221410, complete abstract; publisher abstract independently displayed | supports | The abstract explicitly reports CTPS cytoophidia across all three domains of life. It distinguishes light-microscopy-visible mesoscale cytoophidia from smaller oligomeric filaments. Used only for broad occurrence and terminology, not detailed structural or functional mechanisms. |
| cytoophidium-authority-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097268,GO:0099512; Native GO definitions, obsolete flags and parent child relation | supports | Active GO:0097268 exactly matches the record label and definition. GO:0099512 supramolecular fiber explicitly lists cytoophidium as an is-a child. |
| cytoophidium-authority-agent-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cytoophidium&amp;limit=100; QuickGO cytoophidium search; complete returned result names | context_only | Bounded cytoophidium query returns the exact cellular component and a distinct organization process; the target denotes an assembly rather than an enzyme or process. |
| cytoophidium-authority-agent-IPR004468 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004468/; InterPro metadata name CTP synthase, type family and description | supports | IPR004468 is the whole CTP synthase family, not a catalytic domain or broad fold. It matches the record’s generic component class. |
| cytoophidium-authority-agent-Q9A7K3 | https://rest.uniprot.org/uniprotkb/Q9A7K3.json; UniProt native entryType, recommendedName, genes, organism and InterPro cross-references | supports | Reviewed CTP synthase/pyrG entry has the exact recorded taxon and carries IPR004468. Q9A7K3 identifies CB15 CC_1720; B8GW64 identifies NA1000/CB15N CCNA_01791. Automated cytoophidium annotations are not used as experimental membership proof. |
| cytoophidium-authority-agent-B8GW64 | https://rest.uniprot.org/uniprotkb/B8GW64.json; UniProt native entryType, recommendedName, genes, organism and InterPro cross-references | supports | Reviewed CTP synthase/pyrG entry has the exact recorded taxon and carries IPR004468. Q9A7K3 identifies CB15 CC_1720; B8GW64 identifies NA1000/CB15N CCNA_01791. Automated cytoophidium annotations are not used as experimental membership proof. |
| cytoophidium-authority-agent-taxon-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; ENA taxonomy tax-id/2 scientificName, rank and synonyms | supports | Native NCBI taxonomy served by ENA agrees with the asserted label and rank; Caulobacter crescentus is reconciled with C. vibrioides, and strain identities remain distinct. |
| cytoophidium-authority-agent-taxon-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; ENA taxonomy tax-id/2157 scientificName, rank and synonyms | supports | Native NCBI taxonomy served by ENA agrees with the asserted label and rank; Caulobacter crescentus is reconciled with C. vibrioides, and strain identities remain distinct. |
| cytoophidium-authority-agent-taxon-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; ENA taxonomy tax-id/2759 scientificName, rank and synonyms | supports | Native NCBI taxonomy served by ENA agrees with the asserted label and rank; Caulobacter crescentus is reconciled with C. vibrioides, and strain identities remain distinct. |
| cytoophidium-authority-agent-taxon-155892 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/155892; ENA taxonomy tax-id/155892 scientificName, rank and synonyms | supports | Native NCBI taxonomy served by ENA agrees with the asserted label and rank; Caulobacter crescentus is reconciled with C. vibrioides, and strain identities remain distinct. |
| cytoophidium-authority-agent-taxon-190650 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/190650; ENA taxonomy tax-id/190650 scientificName, rank and synonyms | supports | Native NCBI taxonomy served by ENA agrees with the asserted label and rank; Caulobacter crescentus is reconciled with C. vibrioides, and strain identities remain distinct. |
| cytoophidium-authority-agent-taxon-565050 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/565050; ENA taxonomy tax-id/565050 scientificName, rank and synonyms | supports | Native NCBI taxonomy served by ENA agrees with the asserted label and rank; Caulobacter crescentus is reconciled with C. vibrioides, and strain identities remain distinct. |
| cytoophidium-agent-discovery-crossref | https://api.crossref.org/works/10.1038/ncb2087; Crossref DOI metadata | supports | Native DOI metadata resolves the cited article with the recorded authors, year and title. |
| cytoophidium-agent-review-crossref | https://api.crossref.org/works/10.1042/BST20221410; Crossref DOI metadata | supports | Native DOI metadata resolves the cited article with the recorded authors, year and title. |
| record | data/structures/cytoskeleton/cytoophidium.yaml; Entire maintained YAML | context_only | The record is PROPOSED, uses neutral regulates/tune graph edges and limits the functional example to Caulobacter. It does not assert that every CTPS protein forms filaments or that all cytoophidia are CTPS-only. |
| policy | docs/CURATION.md; Components: taxon-agnostic family or class | context_only | A component is a taxon-agnostic family/class. Experimentally established localization and assembly scope belong in role/evidence; a family term need not encode that localization. |
| internal-reference | data/structures/cytoskeleton/crescentin_filament.yaml; Entire neighboring record; ignored- and hidden-inclusive identifier/alias search of data/structures | context_only | The local crescentin filament node resolves to a separate maintained assembly. The target uniquely declares GO:0097268 in the searched corpus. Crescentin is a functional interacting system, not asserted as a CtpS filament subunit. |
| schema-result | just validate data/structures/cytoskeleton/cytoophidium.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/cytoophidium.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/cytoophidium.yaml --out /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/cytoophidium-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/cytoophidium.yaml --out /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/cytoophidium-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch6-20261021-hj8mnf9r/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/cytoophidium-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/cytoophidium.yaml; exact collect() scope | supports | 12 of13 collected target identifiers returned OK at the unchanged base. Residuals: cellstructuremech:crescentin_filament: SKIPPED; resolved by evidence internal-reference. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The 2023 review was checked at complete abstract level through PubMed/publisher displays; direct publisher retrieval returned HTTP 403. Detailed review-body claims were not assumed.
- Caulobacter evidence is from laboratory strains, with method- and cell-cycle-dependent detection. COMMON is not validated as a population prevalence estimate across all strains.
- The molecular CtpS–crescentin contact and downstream envelope coupling remain unresolved; no direct physical mechanism is inferred from functional interaction.
- Neither a family annotation nor the E. coli replacement experiment establishes that every CTPS orthologue forms a cytoophidium or regulates curvature in its native species.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Read-only collaborating agents independently inspected native identifiers and the discovery source. Final record assessment integrates those checks with the entire YAML.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T065437Z-cytoophidium-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cytoophidium identity, curvature mechanism and component-family review
started_at: '2026-10-21T06:52:03Z'
finished_at: '2026-10-21T06:54:37Z'
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
summary: Cytoophidium identity, Caulobacter CtpS membership, strain examples and the
  scoped curvature graph are supported. One minor finding concerns withholding the
  verified CTP synthase family mapping on an assembly-specific cohort criterion.
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
  - path: data/structures/cytoskeleton/crescentin_filament.yaml
    sha256: 8a7528bc96ddf0c0d8935ba4a308d49e7390262d09de979fe5138dbf1fcd2f0a
    role: context
  - path: data/structures/cytoskeleton/cytoophidium.yaml
    sha256: 4e75070209f20d340a776a5ea708588484f39dc1f0a8859a0f0520ba2acda553
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
- target_id: GO:0097268
  path: data/structures/cytoskeleton/cytoophidium.yaml
  label: cytoophidium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cytoophidium.yaml
    role: maintained scientific record
scope:
  description: Complete read-only review of the target YAML, all stable identifiers,
    internal crescentin reference, discovery manuscript and the cited 2023 review’s
    broad occurrence statement.
  selection: Second unreviewed path in batch six, following cryptophyte cortical centrin
    network; one record per saved bundle in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097268
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0097268
  command: just validate data/structures/cytoskeleton/cytoophidium.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0097268
  command: just validate-strict data/structures/cytoskeleton/cytoophidium.yaml --out
    /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/cytoophidium-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0097268
  summary: 12 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - internal-reference
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0097268
  summary: This record makes no transcriptional regulation or expression-module assertion.
    Native protein/taxon authorities and the direct filament experiments address its
    actual claims.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0097268
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - cytoophidium-agent-discovery-pdf
  - review-abstract
  - cytoophidium-authority-agent-go
  - cytoophidium-authority-agent-go-search
  - cytoophidium-authority-agent-IPR004468
  - cytoophidium-authority-agent-Q9A7K3
  - cytoophidium-authority-agent-B8GW64
  - cytoophidium-authority-agent-taxon-2
  - cytoophidium-authority-agent-taxon-2157
  - cytoophidium-authority-agent-taxon-2759
  - cytoophidium-authority-agent-taxon-155892
  - cytoophidium-authority-agent-taxon-190650
  - cytoophidium-authority-agent-taxon-565050
  - cytoophidium-agent-discovery-crossref
  - cytoophidium-agent-review-crossref
  - record
  - policy
  - internal-reference
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097268
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch6 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0097268
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch6 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0097268
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch6 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0097268
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch6 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0097268
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch6 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: cytoophidium-agent-discovery-pdf
  kind: primary_source
  reference: https://authors.library.caltech.edu/records/q1v55-6sf11/files/nihms215754.pdf
  locator: 'Ingerson-Mahar et al. 2010 accepted manuscript: Results pp. 2–7, Figures
    1–5, Methods p. 8; independently read through PMC and the deposited PDF'
  accessed_at: '2026-10-21T06:53:23.511067Z'
  support: supports
  summary: 'The complete accepted manuscript supports CtpS-dependent filaments in
    Caulobacter CB15N, dynamic localization, crescentin-dependent morphogenic effects
    and separability from catalytic activity. Overexpression straightens cells and
    depletion hypercurves them: the source describes negative regulation, not positive
    promotion of curvature. E. coli native and purified CtpS form filaments. The durable
    repository file URL is cited; the retained request receipt records its public
    signed-download redirect.'
  snapshot_sha256: ed74c343c4e33b7899fa8789aa5df0cb84db90ae0c899386fc6f9bb2bae4db24
- evidence_id: review-abstract
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/37248970/
  locator: Guo and Liu 2023, DOI 10.1042/BST20221410, complete abstract; publisher
    abstract independently displayed
  accessed_at: '2026-10-21T06:54:36Z'
  support: supports
  summary: The abstract explicitly reports CTPS cytoophidia across all three domains
    of life. It distinguishes light-microscopy-visible mesoscale cytoophidia from
    smaller oligomeric filaments. Used only for broad occurrence and terminology,
    not detailed structural or functional mechanisms.
- evidence_id: cytoophidium-authority-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097268,GO:0099512
  locator: Native GO definitions, obsolete flags and parent child relation
  accessed_at: '2026-10-21T06:51:38.262137Z'
  support: supports
  summary: Active GO:0097268 exactly matches the record label and definition. GO:0099512
    supramolecular fiber explicitly lists cytoophidium as an is-a child.
  snapshot_sha256: a412795f0f4fe971e035e4afb242da340bcdd0ee9cd8ee7c4f873790b00b6905
- evidence_id: cytoophidium-authority-agent-go-search
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=cytoophidium&limit=100
  locator: QuickGO cytoophidium search; complete returned result names
  accessed_at: '2026-10-21T06:51:38.274667Z'
  support: context_only
  summary: Bounded cytoophidium query returns the exact cellular component and a distinct
    organization process; the target denotes an assembly rather than an enzyme or
    process.
  snapshot_sha256: 4445fd88a8eba9122711c2ba0d7b15582d387696d4f872f10ceb16d8b13eaf40
- evidence_id: cytoophidium-authority-agent-IPR004468
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004468/
  locator: InterPro metadata name CTP synthase, type family and description
  accessed_at: '2026-10-21T06:52:03.558521Z'
  support: supports
  summary: IPR004468 is the whole CTP synthase family, not a catalytic domain or broad
    fold. It matches the record’s generic component class.
  snapshot_sha256: 129350579998d3554983179ee054310a6ae15750014fe433b25c0ead10acce00
- evidence_id: cytoophidium-authority-agent-Q9A7K3
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9A7K3.json
  locator: UniProt native entryType, recommendedName, genes, organism and InterPro
    cross-references
  accessed_at: '2026-10-21T06:51:38.264322Z'
  support: supports
  summary: Reviewed CTP synthase/pyrG entry has the exact recorded taxon and carries
    IPR004468. Q9A7K3 identifies CB15 CC_1720; B8GW64 identifies NA1000/CB15N CCNA_01791.
    Automated cytoophidium annotations are not used as experimental membership proof.
  snapshot_sha256: 58b463547f5d63c67aaabb71a0b4214f53b019e19fde7c93becb7c3c92fce693
- evidence_id: cytoophidium-authority-agent-B8GW64
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/B8GW64.json
  locator: UniProt native entryType, recommendedName, genes, organism and InterPro
    cross-references
  accessed_at: '2026-10-21T06:51:38.974860Z'
  support: supports
  summary: Reviewed CTP synthase/pyrG entry has the exact recorded taxon and carries
    IPR004468. Q9A7K3 identifies CB15 CC_1720; B8GW64 identifies NA1000/CB15N CCNA_01791.
    Automated cytoophidium annotations are not used as experimental membership proof.
  snapshot_sha256: 9b3617df92d7c071acf820f7255bff63a59063a2977c560912faacd2377be43c
- evidence_id: cytoophidium-authority-agent-taxon-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: ENA taxonomy tax-id/2 scientificName, rank and synonyms
  accessed_at: '2026-10-21T06:51:38.907955Z'
  support: supports
  summary: Native NCBI taxonomy served by ENA agrees with the asserted label and rank;
    Caulobacter crescentus is reconciled with C. vibrioides, and strain identities
    remain distinct.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: cytoophidium-authority-agent-taxon-2157
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: ENA taxonomy tax-id/2157 scientificName, rank and synonyms
  accessed_at: '2026-10-21T06:51:38.916346Z'
  support: supports
  summary: Native NCBI taxonomy served by ENA agrees with the asserted label and rank;
    Caulobacter crescentus is reconciled with C. vibrioides, and strain identities
    remain distinct.
  snapshot_sha256: c6e652011b95e43e933983bf5f3f5cec9508c1925adae00dc55e46cd4e816b19
- evidence_id: cytoophidium-authority-agent-taxon-2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: ENA taxonomy tax-id/2759 scientificName, rank and synonyms
  accessed_at: '2026-10-21T06:51:38.916621Z'
  support: supports
  summary: Native NCBI taxonomy served by ENA agrees with the asserted label and rank;
    Caulobacter crescentus is reconciled with C. vibrioides, and strain identities
    remain distinct.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: cytoophidium-authority-agent-taxon-155892
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/155892
  locator: ENA taxonomy tax-id/155892 scientificName, rank and synonyms
  accessed_at: '2026-10-21T06:51:39.567039Z'
  support: supports
  summary: Native NCBI taxonomy served by ENA agrees with the asserted label and rank;
    Caulobacter crescentus is reconciled with C. vibrioides, and strain identities
    remain distinct.
  snapshot_sha256: 99691bdcc66af16241d0a4d0a9ef13c3e6e87ecf9c4d36331ea8e40757bffce7
- evidence_id: cytoophidium-authority-agent-taxon-190650
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/190650
  locator: ENA taxonomy tax-id/190650 scientificName, rank and synonyms
  accessed_at: '2026-10-21T06:51:39.584259Z'
  support: supports
  summary: Native NCBI taxonomy served by ENA agrees with the asserted label and rank;
    Caulobacter crescentus is reconciled with C. vibrioides, and strain identities
    remain distinct.
  snapshot_sha256: 1ee188a0befe230048162264bc667bcaf7616a5b6be3199d21f340408d42f5ef
- evidence_id: cytoophidium-authority-agent-taxon-565050
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/565050
  locator: ENA taxonomy tax-id/565050 scientificName, rank and synonyms
  accessed_at: '2026-10-21T06:51:39.601739Z'
  support: supports
  summary: Native NCBI taxonomy served by ENA agrees with the asserted label and rank;
    Caulobacter crescentus is reconciled with C. vibrioides, and strain identities
    remain distinct.
  snapshot_sha256: d3c932efaddd17db870d54241a8c2441cc71fa808cad435ef9bfd60976641685
- evidence_id: cytoophidium-agent-discovery-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.1038/ncb2087
  locator: Crossref DOI metadata
  accessed_at: '2026-10-21T06:51:18.061332Z'
  support: supports
  summary: Native DOI metadata resolves the cited article with the recorded authors,
    year and title.
  snapshot_sha256: c150fd6f19d9f0e4848f08c31a1981d7c99c9ccdd9ab7ae2f7a0db1a590fc747
- evidence_id: cytoophidium-agent-review-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.1042/BST20221410
  locator: Crossref DOI metadata
  accessed_at: '2026-10-21T06:51:18.063605Z'
  support: supports
  summary: Native DOI metadata resolves the cited article with the recorded authors,
    year and title.
  snapshot_sha256: b4b9ce3b5178b5f8c20260711feb5f8a7224e800c1236d671bf2f60c8a558661
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/cytoophidium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T06:54:36Z'
  support: context_only
  summary: The record is PROPOSED, uses neutral regulates/tune graph edges and limits
    the functional example to Caulobacter. It does not assert that every CTPS protein
    forms filaments or that all cytoophidia are CTPS-only.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: taxon-agnostic family or class'
  accessed_at: '2026-10-21T06:54:36Z'
  support: context_only
  summary: A component is a taxon-agnostic family/class. Experimentally established
    localization and assembly scope belong in role/evidence; a family term need not
    encode that localization.
- evidence_id: internal-reference
  kind: record_content
  reference: data/structures/cytoskeleton/crescentin_filament.yaml
  locator: Entire neighboring record; ignored- and hidden-inclusive identifier/alias
    search of data/structures
  accessed_at: '2026-10-21T06:54:36Z'
  support: context_only
  summary: The local crescentin filament node resolves to a separate maintained assembly.
    The target uniquely declares GO:0097268 in the searched corpus. Crescentin is
    a functional interacting system, not asserted as a CtpS filament subunit.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/cytoophidium.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T06:52:05Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/cytoophidium.yaml'
  snapshot_sha256: ab99863fe65ba8e237656e1ccefc3397666dbf826bf129381fb61fefe491b7b0
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/cytoophidium.yaml --out
    /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/cytoophidium-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T06:52:07Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/cytoophidium.yaml\
    \ --out /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/cytoophidium-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch6-20261021-hj8mnf9r/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch6-20261021-hj8mnf9r/cytoophidium-strict.tsv"
  snapshot_sha256: 7b5fbc20fa49d2ee24c45efa654a81fef0ceb7afaf05ba16111c65d1336f353c
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/cytoophidium.yaml; exact collect() scope
  accessed_at: '2026-10-21T06:54:36Z'
  support: supports
  summary: '12 of13 collected target identifiers returned OK at the unchanged base.
    Residuals: cellstructuremech:crescentin_filament: SKIPPED; resolved by evidence
    internal-reference. Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
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
  topic: Ontology-grounded enzyme assembly
  outcome: supported
  target_ids:
  - GO:0097268
  summary: Exact native ontology identity and supramolecular-fiber parent are supported.
    Related CTPS/CtpS synonyms do not redefine every metabolic-enzyme cytoophidium
    as a single enzyme class.
  evidence_ids:
  - cytoophidium-authority-agent-go
  - cytoophidium-authority-agent-go-search
  - record
- assessment_id: composition
  area: evidence
  topic: Caulobacter constituent and strain examples
  outcome: supported
  target_ids:
  - GO:0097268
  summary: Discovery experiments, rather than automated sequence annotations, support
    CtpS filament membership. Both curated protein examples have matching enzyme,
    gene, strain and reviewed status. UNKNOWN essentiality avoids conflating catalytic
    viability with universal assembly necessity.
  evidence_ids:
  - cytoophidium-agent-discovery-pdf
  - cytoophidium-authority-agent-Q9A7K3
  - cytoophidium-authority-agent-B8GW64
  - record
- assessment_id: grounding
  area: grounding
  topic: Generic family versus assembly-specific cohort
  outcome: concern
  target_ids:
  - GO:0097268
  summary: The target withholds an exact verified CTP synthase family because it seeks
    a term restricted to cytoophidium-forming proteins. That narrower criterion is
    unnecessary for this generic component class; the experimental assembly role can
    retain its scope after family grounding.
  evidence_ids:
  - cytoophidium-authority-agent-IPR004468
  - cytoophidium-authority-agent-Q9A7K3
  - cytoophidium-authority-agent-B8GW64
  - policy
  - record
- assessment_id: scope
  area: scope
  topic: Occurrence across domains and laboratory strain context
  outcome: supported
  target_ids:
  - GO:0097268
  summary: The review abstract supports variable occurrence across Bacteria, Archaea
    and Eukaryota. CB15N is the direct laboratory imaging example. COMMON is qualitative
    occurrence, not a claim that every cell or strain contains a visible filament;
    native-expression ECT detected bundles in a subset of cells.
  evidence_ids:
  - cytoophidium-agent-discovery-pdf
  - review-abstract
  - cytoophidium-authority-agent-taxon-2
  - cytoophidium-authority-agent-taxon-2157
  - cytoophidium-authority-agent-taxon-2759
  - cytoophidium-authority-agent-taxon-155892
  - cytoophidium-authority-agent-taxon-190650
  - cytoophidium-authority-agent-taxon-565050
- assessment_id: function
  area: graph
  topic: Four scoped nonmechanistic edges
  outcome: supported
  target_ids:
  - GO:0097268
  summary: 'Assembly, changing inner-curvature localization, functional interaction
    with crescentin and curvature regulation are experimentally supported. The source
    shows negative regulation: overexpression straightens and depletion hypercurves.
    Read with neutral regulates/tune edges, the description supports normal curved
    morphology without asserting a positive dose-response or direct molecular contact.'
  evidence_ids:
  - cytoophidium-agent-discovery-pdf
  - record
  - internal-reference
- assessment_id: boundaries
  area: consistency
  topic: Interacting filaments and mesoscale terminology
  outcome: supported
  target_ids:
  - GO:0097268
  summary: Crescentin remains a separate filament; its absence affects CtpS positioning
    and morphogenesis without preventing filament formation. The 2023 terminology
    distinguishes mesoscale cytoophidia from elementary enzyme polymers; the related
    synonym and whole-assembly ontology identity do not require a structural split
    in this bounded review.
  evidence_ids:
  - cytoophidium-agent-discovery-pdf
  - review-abstract
  - cytoophidium-authority-agent-go
  - internal-reference
- assessment_id: completeness
  area: completeness
  topic: Supported example with resolvable family TODO
  outcome: supported
  target_ids:
  - GO:0097268
  summary: No unsupported measurement, image, trait or molecular mechanism is asserted.
    The generic CTPS family discussion has a concrete verified resolution; broad enzyme-composition
    diversity is not claimed to be exhaustively catalogued.
  evidence_ids:
  - cytoophidium-agent-discovery-pdf
  - cytoophidium-authority-agent-IPR004468
  - record
findings:
- finding_id: F1
  issue_key: cytoophidium-ctp-synthase-family-grounding-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Assembly-specific cohort criterion blocks verified CTP synthase family grounding
  description: The generic CTP synthase component is REVIEWED_LABEL_ONLY because the
    rationale seeks a term restricted to cytoophidium-forming CTPS. IPR004468 is the
    exact whole CTP synthase family and both taxon-paired examples carry it. The repository
    component model separates family identity from experimental assembly role. Resolve
    the missing mapping and reconcile the rationale/TODO without claiming universal
    filament formation.
  target_ids:
  - GO:0097268
  field_paths:
  - components[component_id=ctp_synthase].grounding_status
  - components[component_id=ctp_synthase].grounding_notes
  - discussions[discussion_id=resolve_ctps_family_grounding]
  evidence_ids:
  - cytoophidium-authority-agent-IPR004468
  - cytoophidium-authority-agent-Q9A7K3
  - cytoophidium-authority-agent-B8GW64
  - policy
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cytoophidium.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Biological identity and membership remain supported; the defect
    is a bounded, verifiably resolvable family-mapping gap.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0097268
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cytoophidium.yaml
    role: maintained scientific record
  description: Under separately authorized curation, map the generic CTP synthase
    component to InterPro:IPR004468, reconcile grounding status/notes and resolve
    the family TODO. Preserve lineage-specific assembly evidence, protein examples
    and UNKNOWN essentiality.
  acceptance_checks:
  - Native InterPro confirms exact CTP synthase family name/type; both examples retain
    that mapping.
  - Role and evidence remain limited to demonstrated filament-forming contexts; no
    universal family-wide assembly claim is added.
  - Run schema, strict, controlled-label, history and generated-page checks after
    curation.
  generator: Maintained structure YAML; just render derives pages.
limitations:
- The 2023 review was checked at complete abstract level through PubMed/publisher
  displays; direct publisher retrieval returned HTTP 403. Detailed review-body claims
  were not assumed.
- Caulobacter evidence is from laboratory strains, with method- and cell-cycle-dependent
  detection. COMMON is not validated as a population prevalence estimate across all
  strains.
- The molecular CtpS–crescentin contact and downstream envelope coupling remain unresolved;
  no direct physical mechanism is inferred from functional interaction.
- Neither a family annotation nor the E. coli replacement experiment establishes that
  every CTPS orthologue forms a cytoophidium or regulates curvature in its native
  species.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Read-only collaborating agents independently inspected native identifiers and the
  discovery source. Final record assessment integrates those checks with the entire
  YAML.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
