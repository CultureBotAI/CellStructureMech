# OmcE cytochrome nanowire: scoped scientific review

- Review: 20261020T032925Z-omce-cytochrome-nanowire-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-19T23:36:05Z
- Finished UTC: 2026-10-20T03:29:25Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full record review supports OmcE identity, protein/strain mapping, structural claims and the explicitly candidate conduction path. One major scope finding remains: COMMON occurrence is unsupported by the cited PDB source provenance. All cited material sources were accessed.

## Scope And Provenance

One complete maintained OmcE cytochrome nanowire record, every present section and material identifier/claim.

Selection: Exact batch-002 queued target data/structures/appendage/omce_cytochrome_nanowire.yaml; one record per bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:omce_cytochrome_nanowire | data/structures/appendage/omce_cytochrome_nanowire.yaml | maintained | OmcE cytochrome nanowire |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Open LinkML target validation | passed | True | cellstructuremech:omce_cytochrome_nanowire | Exit 0; No issues found. |
| Closed LinkML target validation | passed | True | cellstructuremech:omce_cytochrome_nanowire | Exit 0; one file, zero ERROR rows. |
| Authority and nearest-source claim audit | passed | True | cellstructuremech:omce_cytochrome_nanowire | Completed authority and full-body source review. Detected unsupported COMMON prevalence; successful source access is not a claim that all assertions pass scientifically. |
| Verbatim snippet verification | not_applicable | False | cellstructuremech:omce_cytochrome_nanowire | No snippet fields present. |
| Target resolver coverage including residuals | passed | True | cellstructuremech:omce_cytochrome_nanowire | Collected values resolve through shared report plus scoped PDB/local receipts; scientific claim support is separately assessed. |
| Full corpus QC | passed | True | cellstructuremech:omce_cytochrome_nanowire | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:omce_cytochrome_nanowire | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:omce_cytochrome_nanowire | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:omce_cytochrome_nanowire | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:omce_cytochrome_nanowire | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Filament identity, synonyms and local identifier

identity: supported. Targets: cellstructuremech:omce_cytochrome_nanowire.

The definition and synonyms denote the assembled OmcE extracellular filament, not soluble OmcE or other nanowire classes. APPENDAGE is consistent with its morphology. Exact GO identity was not recovered by the bounded search; an unrelated or broader term should not replace the local ID.

### OmcE component, essentiality and heme packing

grounding: supported. Targets: cellstructuremech:omce_cytochrome_nanowire.

The sole protein is a constituent that defines this homopolymeric filament, so ESSENTIAL concerns assembly identity rather than cell viability. Four covalently attached hemes and their packing are supported. The broad family mappings justify REVIEWED_LABEL_ONLY and the open exact-family task.

### Accession, strain, status and full polymer alignment

grounding: supported. Targets: cellstructuremech:omce_cytochrome_nanowire.

Q74FJ0/omcE is the correct unreviewed PCA protein, and the full-length 232-residue SIFTS entity-to-reference alignment is accurate. Full sequence coverage is not confused with complete resolved coordinates: the archive distinguishes 202 modeled from 30 unmodeled residues.

### PCA source provenance versus COMMON prevalence

scope: concern. Targets: cellstructuremech:omce_cytochrome_nanowire.

The PCA canonical example and natural-source note are correct, but the source deposition does not support the COMMON frequency assertion. The structural paper used engineered OmcS-variant PCA derivatives; prevalence across PCA cells or conditions was not measured. Its Introduction reports abundant surface OmcE protein under metal-oxide/electrode growth and condition-dependent expression, but protein production does not itself establish frequency of the assembled nanowire. No natural absence is inferred.

### Candidate electron-transfer function

evidence: supported. Targets: cellstructuremech:omce_cytochrome_nanowire.

The function accurately presents packed hemes as a candidate structural path. It avoids asserting a measured OmcE conductivity, a complete physiological circuit or interchangeability with OmcS/OmcZ.

### Every node and edge of the proposed mechanism

graph: supported. Targets: cellstructuremech:omce_cytochrome_nanowire.

The component reference and local structure ID resolve. Polymerization and tetraheme placement are structurally supported; the final electron-transfer edge is explicitly candidate/proposed. MECHANISTIC scope is an appropriately caveated structural mechanism, not a direct functional measurement.

### Citation accuracy, model/map and snippets

evidence: supported. Targets: cellstructuremech:omce_cytochrome_nanowire.

The DOI/title/authors, 7TFS identity, 4.3 Å resolution, EMD-25879 link and full-polymer UniProt mapping match their sources. Evidence is attached to the relevant claims. No snippet fields are present, so no verbatim quotation mismatch is possible.

### Hierarchy, cofactors, optional images/properties and other surfaces

completeness: supported. Targets: cellstructuremech:omce_cytochrome_nanowire.

No unsupported hierarchy or cross-corpus link is asserted. Covalent hemes are represented in the component/function mechanism; lack of a separate cofactor row, image or numeric-property row is not itself a defect. The study discusses putative glycosylation, but its identity is unresolved and the record need not invent a glycan component.

### Open discussion, PROPOSED status and history

provenance: supported. Targets: cellstructuremech:omce_cytochrome_nanowire.

The exact-family discussion is actionable and honest about scope. Three record events and the append-only CREATE history are consistent with the existing content. PROPOSED remains appropriate; this review neither promotes status nor reopens/closes historical remote issues.

### Focused open and closed validation

schema: supported. Targets: cellstructuremech:omce_cytochrome_nanowire.

Both focused validators pass. Native corpus checks are integrated separately by the coordinating reviewer.

## Findings

### F1: PDB source provenance does not establish COMMON occurrence

major / open / confirmed; issue key: omce-pdb-source-not-common-prevalence.

taxonomic_distribution[0] assigns COMMON to PCA while citing only the natural-source metadata for one deposited model. COMMON explicitly means occurrence in most members with losses exceptional. The paper establishes purified OmcE filaments in engineered OmcS-variant PCA derivatives, not population- or condition-level prevalence. The qualified note correctly identifies source provenance but does not support the stronger machine-readable frequency. The paper also documents prior evidence of native OmcE protein production; this finding does not imply natural absence. Preserve the canonical source example; remove this distribution row unless evidence for an actual occurrence-frequency claim is supplied. COMMON does not itself require constitutive expression in every condition; the finding concerns the unsupported most-member quantifier, not universal expression.

## Recommended Actions And Acceptance Checks

### A1

Remove the unsupported taxonomic_distribution row and retain the PCA canonical example and protein-example provenance. Alternatively, provide directly relevant occurrence evidence and encode only its supported scope; do not substitute another frequency enum based solely on the deposition.

- Every remaining presence enum is justified by evidence about occurrence consistency, not merely a PDB natural source.
- PCA source/strain information remains in canonical_examples and protein_examples.
- Run focused open/strict validators and required curation/history gates after any separately authorized edit.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/omce_cytochrome_nanowire.yaml | supports | Entire maintained OmcE record read; one protein component, strain occurrence/example, candidate function, four-node/three-edge graph and open family-grounding discussion were assessed. |
| paper | https://pmc.ncbi.nlm.nih.gov/articles/PMC9357133/; Abstract; Results: Detection of OmcE, Cryo-EM, Sequence and structural comparison, Stacking arrangement; Figs.1–3; Discussion; Materials and Methods; Data availability | supports | The full article supports extracellular helical OmcE identity, tetraheme packing, distinction from OmcS and a proposed electron-transfer path. Results and Fig.1 identify preparations from engineered OmcS-variant strains; methods identify the PCA parent and OmcS H38M/H41M/H357M constructs. The paper does not establish prevalence of OmcE filaments across PCA cells or conditions. |
| crossref | https://api.crossref.org/works/10.1038/s41564-022-01159-z; DOI, title, author and publication metadata | supports | DOI 10.1038/s41564-022-01159-z resolves to Wang et al. 2022, Cryo-EM structure of an extracellular Geobacter OmcE cytochrome filament reveals tetrahaem packing, Nature Microbiology. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=35798889&amp;retmode=xml; MedlineCitation and PubmedData/ArticleIdList | supports | PMID 35798889 is the exact Wang et al. 2022 paper, with the target DOI and PMCID PMC9357133. |
| pdb-entry | https://data.rcsb.org/rest/v1/core/entry/7TFS; struct, rcsb_entry_info, rcsb_primary_citation, pdbx_database_related | supports | PDB 7TFS is the OmcE nanowire cryo-EM model at 4.3 Å; the primary citation is the target Wang paper and associated map is EMD-25879. The deposited model includes one protein entity and four heme-c ligand instances. |
| pdb-polymer | https://data.rcsb.org/rest/v1/core/polymer_entity/7TFS/1; entity_src_nat; entity_poly; rcsb_polymer_entity_align; reference_sequence_identifiers | supports | Entity 1 is 232 residues; SIFTS aligns positions 1–232 to Q74FJ0 with full entity/reference coverage. Natural-source fields name Geobacter sulfurreducens, species taxon 35554, and strain ATCC 51573 / DSM 12127 / PCA. This is source/sequence provenance, not a frequency estimate. |
| uniprot | https://rest.uniprot.org/uniprotkb/Q74FJ0.json; entryType, proteinDescription, genes, organism, sequence and PDB cross-reference | supports | Q74FJ0 is unreviewed UniProtKB/TrEMBL Cytochrome c, gene omcE, locus GSU0618, 232 residues, taxon 243231. It cross-references 7TFS. The declared accession, gene, label and review status match. |
| taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=243231&amp;retmode=xml; TaxId, ScientificName and Rank | supports | NCBI Taxonomy 243231 is Geobacter sulfurreducens PCA at strain rank, matching the protein example and canonical source label. |
| emdb | https://www.ebi.ac.uk/emdb/api/entry/EMD-25879; admin and entry reconstruction/model metadata | supports | EMD-25879 is the released OmcE cryo-EM reconstruction associated with 7TFS. The article and structural archive agree on the map/model identity. |
| family | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q74FJ0/; Five entry results for Q74FJ0 | context_only | The Q74FJ0 mappings contain broad Multiheme cytochrome superfamily IPR036280 and doubled-CXXCH domain IPR010177/PF09699 (with TIGR01905 member mapping), not an exact OmcE nanowire-subunit family. Other returned broad models likewise do not establish exact OmcE identity. |
| family-search | https://www.ebi.ac.uk/interpro/api/entry/all/?search=OmcE&amp;page_size=100; search=OmcE; page_size=100 | context_only | The bounded exact-name InterPro search returned HTTP 204/no matching entry. Combined with the observed broad protein mappings, this supports retaining a label-only component and an open grounding task; it is not proof that no exact family exists anywhere. |
| go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=OmcE&amp;limit=100; numberOfHits and results | context_only | QuickGO exact-name search for OmcE returned zero hits. A second search for nanowire also returned zero hits. No exact GO identity was recovered; the local structure identifier is appropriately distinct from the protein accession. |
| presence-schema | src/cellstructuremech/schema/cellstructuremech.yaml; PresenceEnum.COMMON; TaxonomicScope; CanonicalExample | supports | PresenceEnum COMMON means present in most members, with losses exceptional. TaxonomicScope concerns consistency of occurrence; CanonicalExample separately records a source organism. |
| repository-context | history/records/omce_cytochrome_nanowire/ | supports | Ignored-inclusive search found this target, OmcS/OmcZ sibling records and one OmcE CREATE history file. The history records prior narrowing of source notes and candidate-conduction wording. No matching structured review was found in the searched reviews root; this observation does not close prior GitHub issues. |
| schema | justfile; validate and validate-strict recipes; external strict.tsv | supports | Focused open validation exited 0, No issues found; focused strict validation exited 0, one file scanned, zero ERROR rows. |
| target-resolver-coverage | just check-curies-strict; data/structures/appendage/omce_cytochrome_nanowire.yaml; exact collect() scope; shared reports/curie_check.tsv | supports | The exact collection has 5 CURIE-shaped scalars: {'OK': 3, 'SKIPPED': 2}. Skipped PDB identifiers resolve in the attached exact deposition receipts; the minted local target resolves in the maintained record. HTTP URLs and prose are checked separately. Existence does not imply correct biological mapping. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Exact source-neutral OmcE family grounding remains unresolved after bounded current authority searches; the existing label-only representation and open TODO preserve that uncertainty.
- Cryo-EM supports architecture; the electron-transfer path remains a proposed structural interpretation, as already stated by the record.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Explicit user instruction authorizes clean as well as issue-bearing review output; no finding is invented to satisfy the persistence gate.
- No scientific record, generated artifact, curation history, remote content or paid service was changed.
- Initial publisher/fullTextXML/PDF routes failed, but complete PMC HTML was retrieved and the relevant results, figures/captions, discussion and methods were read. No unresolved source-body access gap affects the reviewed claims.
- Structured UniProt, PDB, EMDB and InterPro APIs supplied protein/structure cross-checks. No expression-module or transcriptomic claim is asserted by this record.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T032925Z-omce-cytochrome-nanowire-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'OmcE cytochrome nanowire: scoped scientific review'
started_at: '2026-10-19T23:36:05Z'
finished_at: '2026-10-20T03:29:25Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Delegated Codex agent reviewed an existing agent-authored record
    in the isolated batch clone. No target authorship during this review or independent
    human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Full record review supports OmcE identity, protein/strain mapping, structural
  claims and the explicitly candidate conduction path. One major scope finding remains:
  COMMON occurrence is unsupported by the cited PDB source provenance. All cited material
  sources were accessed.'
source:
  git_revision: 99692a3d5f16a7dcd6db7e3811344c299a977b81
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/appendage/omce_cytochrome_nanowire.yaml
    sha256: 46831d86d93aa73f427a5ac189fa4e439ee57d3a598ce023917bac623d8d92a9
    role: target
  - path: data/structures/appendage/omcs_cytochrome_nanowire.yaml
    sha256: ca7929cfc24552723a28266b0c42c392052caa65a5a7115f6b41c1fde5248eb2
    role: context
  - path: data/structures/appendage/omcz_cytochrome_nanowire.yaml
    sha256: 5072025a6196c3c09b9acc76dae5970908799e8daf4a2977d8f04f120eba13c6
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
  - path: history/records/omce_cytochrome_nanowire/2026-09-11T154123Z-codex-18acac.yaml
    sha256: 8b3b33333acf0a0f1236c78373318914d21f92d497e14fcc4c20e3cc6c00fa97
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
- target_id: cellstructuremech:omce_cytochrome_nanowire
  path: data/structures/appendage/omce_cytochrome_nanowire.yaml
  label: OmcE cytochrome nanowire
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/omce_cytochrome_nanowire.yaml
    role: maintained scientific record
scope:
  description: One complete maintained OmcE cytochrome nanowire record, every present
    section and material identifier/claim.
  selection: Exact batch-002 queued target data/structures/appendage/omce_cytochrome_nanowire.yaml;
    one record per bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
checks:
- check_id: open-schema
  name: Open LinkML target validation
  status: passed
  required: true
  summary: Exit 0; No issues found.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate data/structures/appendage/omce_cytochrome_nanowire.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema
- check_id: strict-schema
  name: Closed LinkML target validation
  status: passed
  required: true
  summary: Exit 0; one file, zero ERROR rows.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate-strict data/structures/appendage/omce_cytochrome_nanowire.yaml --out
    /private/tmp/cellstructure-batch2-20261019-52rdp0/omce-review/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema
- check_id: source-audit
  name: Authority and nearest-source claim audit
  status: passed
  required: true
  summary: Completed authority and full-body source review. Detected unsupported COMMON
    prevalence; successful source access is not a claim that all assertions pass scientifically.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - paper
  - crossref
  - pubmed
  - pdb-entry
  - pdb-polymer
  - uniprot
  - taxon
  - emdb
  - family
- check_id: snippets
  name: Verbatim snippet verification
  status: not_applicable
  required: false
  summary: No snippet fields present.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - record
- check_id: target-resolver-coverage
  name: Target resolver coverage including residuals
  status: passed
  required: true
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  summary: Collected values resolve through shared report plus scoped PDB/local receipts;
    scientific claim support is separately assessed.
  evidence_ids:
  - target-resolver-coverage
  - pdb-entry
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
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
  - cellstructuremech:omce_cytochrome_nanowire
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
  - cellstructuremech:omce_cytochrome_nanowire
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
  - cellstructuremech:omce_cytochrome_nanowire
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
  - cellstructuremech:omce_cytochrome_nanowire
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
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/omce_cytochrome_nanowire.yaml
  accessed_at: '2026-10-19T23:38:54Z'
  support: supports
  summary: Entire maintained OmcE record read; one protein component, strain occurrence/example,
    candidate function, four-node/three-edge graph and open family-grounding discussion
    were assessed.
  snapshot_sha256: 46831d86d93aa73f427a5ac189fa4e439ee57d3a598ce023917bac623d8d92a9
- evidence_id: paper
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9357133/
  accessed_at: '2026-10-19T23:37:04Z'
  support: supports
  summary: The full article supports extracellular helical OmcE identity, tetraheme
    packing, distinction from OmcS and a proposed electron-transfer path. Results
    and Fig.1 identify preparations from engineered OmcS-variant strains; methods
    identify the PCA parent and OmcS H38M/H41M/H357M constructs. The paper does not
    establish prevalence of OmcE filaments across PCA cells or conditions.
  locator: 'Abstract; Results: Detection of OmcE, Cryo-EM, Sequence and structural
    comparison, Stacking arrangement; Figs.1–3; Discussion; Materials and Methods;
    Data availability'
  snapshot_sha256: dc02c7f999f36d3d27fe6a2657395a72e289e46ba2906012809c1236ff3a11f3
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1038/s41564-022-01159-z
  accessed_at: '2026-10-19T23:36:32Z'
  support: supports
  summary: DOI 10.1038/s41564-022-01159-z resolves to Wang et al. 2022, Cryo-EM structure
    of an extracellular Geobacter OmcE cytochrome filament reveals tetrahaem packing,
    Nature Microbiology.
  locator: DOI, title, author and publication metadata
  snapshot_sha256: 33c530eee4c272f009547a42cef90f582dbb1ef46124298e29c90f4ca0e06b96
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=35798889&retmode=xml
  accessed_at: '2026-10-19T23:36:54Z'
  support: supports
  summary: PMID 35798889 is the exact Wang et al. 2022 paper, with the target DOI
    and PMCID PMC9357133.
  locator: MedlineCitation and PubmedData/ArticleIdList
  snapshot_sha256: 4edcb1598e70323aa38580957aacad700f7ab0a397e65f8ad98bb1cf26114f2d
- evidence_id: pdb-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/7TFS
  accessed_at: '2026-10-19T23:36:32Z'
  support: supports
  summary: PDB 7TFS is the OmcE nanowire cryo-EM model at 4.3 Å; the primary citation
    is the target Wang paper and associated map is EMD-25879. The deposited model
    includes one protein entity and four heme-c ligand instances.
  locator: struct, rcsb_entry_info, rcsb_primary_citation, pdbx_database_related
  snapshot_sha256: f9d047c5d7159a7b5d96b67e43ad4785046554ac788bedcad2d1b043aad74c0f
- evidence_id: pdb-polymer
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7TFS/1
  accessed_at: '2026-10-19T23:36:32Z'
  support: supports
  summary: Entity 1 is 232 residues; SIFTS aligns positions 1–232 to Q74FJ0 with full
    entity/reference coverage. Natural-source fields name Geobacter sulfurreducens,
    species taxon 35554, and strain ATCC 51573 / DSM 12127 / PCA. This is source/sequence
    provenance, not a frequency estimate.
  locator: entity_src_nat; entity_poly; rcsb_polymer_entity_align; reference_sequence_identifiers
  snapshot_sha256: 51c4dded7af2f6b7383350dfc7aa8ee812e2af8685094bbcb32fee7b6b42ace3
- evidence_id: uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q74FJ0.json
  accessed_at: '2026-10-19T23:36:32Z'
  support: supports
  summary: Q74FJ0 is unreviewed UniProtKB/TrEMBL Cytochrome c, gene omcE, locus GSU0618,
    232 residues, taxon 243231. It cross-references 7TFS. The declared accession,
    gene, label and review status match.
  locator: entryType, proteinDescription, genes, organism, sequence and PDB cross-reference
  snapshot_sha256: 577f1df3f22ad698b2514eb6405d4eff9c482d7aac7a47350ec4ef6cd1a8b394
- evidence_id: taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=243231&retmode=xml
  accessed_at: '2026-10-19T23:36:32Z'
  support: supports
  summary: NCBI Taxonomy 243231 is Geobacter sulfurreducens PCA at strain rank, matching
    the protein example and canonical source label.
  locator: TaxId, ScientificName and Rank
  snapshot_sha256: f1291f188fae1b43a82d2f75e98d90aa41434ef36115f217a9485629eebb2736
- evidence_id: emdb
  kind: database
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-25879
  accessed_at: '2026-10-19T23:36:32Z'
  support: supports
  summary: EMD-25879 is the released OmcE cryo-EM reconstruction associated with 7TFS.
    The article and structural archive agree on the map/model identity.
  locator: admin and entry reconstruction/model metadata
  snapshot_sha256: a827c854b762e597f31e2b1ebb2638b0fa5c5ee985a064ad6d86a09f873e5a04
- evidence_id: family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q74FJ0/
  accessed_at: '2026-10-19T23:36:32Z'
  support: context_only
  summary: The Q74FJ0 mappings contain broad Multiheme cytochrome superfamily IPR036280
    and doubled-CXXCH domain IPR010177/PF09699 (with TIGR01905 member mapping), not
    an exact OmcE nanowire-subunit family. Other returned broad models likewise do
    not establish exact OmcE identity.
  locator: Five entry results for Q74FJ0
  snapshot_sha256: cc4aca1648c1f35af35c8a1de054bd1135bf940d1585e3533890b1e112d3faad
- evidence_id: family-search
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/?search=OmcE&page_size=100
  accessed_at: '2026-10-19T23:37:04Z'
  support: context_only
  summary: The bounded exact-name InterPro search returned HTTP 204/no matching entry.
    Combined with the observed broad protein mappings, this supports retaining a label-only
    component and an open grounding task; it is not proof that no exact family exists
    anywhere.
  locator: search=OmcE; page_size=100
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: Public InterPro all-entry name search for OmcE, plus exact Q74FJ0
    mapping endpoint; no exhaustive sequence-family reassignment performed.
- evidence_id: go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=OmcE&limit=100
  accessed_at: '2026-10-19T23:36:32Z'
  support: context_only
  summary: QuickGO exact-name search for OmcE returned zero hits. A second search
    for nanowire also returned zero hits. No exact GO identity was recovered; the
    local structure identifier is appropriately distinct from the protein accession.
  locator: numberOfHits and results
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: QuickGO ontology/go/search queries OmcE and nanowire, limit=100, both
    0 hits. This is a bounded current terminology search, not an exhaustive assertion
    about all possible synonyms.
- evidence_id: presence-schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  accessed_at: '2026-10-19T23:38:54Z'
  support: supports
  summary: PresenceEnum COMMON means present in most members, with losses exceptional.
    TaxonomicScope concerns consistency of occurrence; CanonicalExample separately
    records a source organism.
  locator: PresenceEnum.COMMON; TaxonomicScope; CanonicalExample
- evidence_id: repository-context
  kind: search
  reference: history/records/omce_cytochrome_nanowire/
  accessed_at: '2026-10-19T23:38:54Z'
  support: supports
  summary: Ignored-inclusive search found this target, OmcS/OmcZ sibling records and
    one OmcE CREATE history file. The history records prior narrowing of source notes
    and candidate-conduction wording. No matching structured review was found in the
    searched reviews root; this observation does not close prior GitHub issues.
  search_scope: rg --no-ignore --hidden -l --glob '!.git/**' --glob '!.venv/**' --glob
    '!review.md' 'omce_cytochrome_nanowire|OmcE|7TFS|Q74FJ0' history/records data/structures
    reviews/structured; git log --format='%H %cI %s' -- target path. Ignored files
    included within those roots; source commit 7192f9fd379c1a789fe43a7ed4a014e6657ead48
    adds the record.
- evidence_id: schema
  kind: validation
  reference: justfile
  accessed_at: '2026-10-19T23:38:54Z'
  support: supports
  summary: Focused open validation exited 0, No issues found; focused strict validation
    exited 0, one file scanned, zero ERROR rows.
  locator: validate and validate-strict recipes; external strict.tsv
  snapshot_sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
- evidence_id: target-resolver-coverage
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/omce_cytochrome_nanowire.yaml; exact collect()
    scope; shared reports/curie_check.tsv
  accessed_at: '2026-10-19T23:41:41.324461Z'
  support: supports
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
  summary: 'The exact collection has 5 CURIE-shaped scalars: {''OK'': 3, ''SKIPPED'':
    2}. Skipped PDB identifiers resolve in the attached exact deposition receipts;
    the minted local target resolves in the maintained record. HTTP URLs and prose
    are checked separately. Existence does not imply correct biological mapping.'
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
  topic: Filament identity, synonyms and local identifier
  outcome: supported
  summary: The definition and synonyms denote the assembled OmcE extracellular filament,
    not soluble OmcE or other nanowire classes. APPENDAGE is consistent with its morphology.
    Exact GO identity was not recovered by the bounded search; an unrelated or broader
    term should not replace the local ID.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - record
  - paper
  - pdb-entry
  - go-search
- assessment_id: composition
  area: grounding
  topic: OmcE component, essentiality and heme packing
  outcome: supported
  summary: The sole protein is a constituent that defines this homopolymeric filament,
    so ESSENTIAL concerns assembly identity rather than cell viability. Four covalently
    attached hemes and their packing are supported. The broad family mappings justify
    REVIEWED_LABEL_ONLY and the open exact-family task.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - paper
  - pdb-entry
  - uniprot
  - family
  - family-search
- assessment_id: protein-example
  area: grounding
  topic: Accession, strain, status and full polymer alignment
  outcome: supported
  summary: 'Q74FJ0/omcE is the correct unreviewed PCA protein, and the full-length
    232-residue SIFTS entity-to-reference alignment is accurate. Full sequence coverage
    is not confused with complete resolved coordinates: the archive distinguishes
    202 modeled from 30 unmodeled residues.'
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - uniprot
  - taxon
  - pdb-polymer
  - pdb-entry
- assessment_id: taxonomic-scope
  area: scope
  topic: PCA source provenance versus COMMON prevalence
  outcome: concern
  summary: The PCA canonical example and natural-source note are correct, but the
    source deposition does not support the COMMON frequency assertion. The structural
    paper used engineered OmcS-variant PCA derivatives; prevalence across PCA cells
    or conditions was not measured. Its Introduction reports abundant surface OmcE
    protein under metal-oxide/electrode growth and condition-dependent expression,
    but protein production does not itself establish frequency of the assembled nanowire.
    No natural absence is inferred.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - record
  - pdb-polymer
  - paper
  - taxon
  - presence-schema
  dimensions:
  - name: experimental-context
    value: PCA-derived engineered OmcS variants; extracellular material mechanically
      sheared and purified for cryo-EM
    definition: Context establishing structure occurrence and limiting extrapolation
      to prevalence.
    evidence_ids:
    - paper
- assessment_id: function
  area: evidence
  topic: Candidate electron-transfer function
  outcome: supported
  summary: The function accurately presents packed hemes as a candidate structural
    path. It avoids asserting a measured OmcE conductivity, a complete physiological
    circuit or interchangeability with OmcS/OmcZ.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - record
  - paper
- assessment_id: graph
  area: graph
  topic: Every node and edge of the proposed mechanism
  outcome: supported
  summary: The component reference and local structure ID resolve. Polymerization
    and tetraheme placement are structurally supported; the final electron-transfer
    edge is explicitly candidate/proposed. MECHANISTIC scope is an appropriately caveated
    structural mechanism, not a direct functional measurement.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - record
  - paper
  - pdb-entry
  dimensions:
  - name: evidence-tier
    value: Cryo-EM architecture plus proposed electron-transfer path
    definition: Separates measured structural relations from the inferential conduction
      edge.
    evidence_ids:
    - paper
- assessment_id: evidence-placement
  area: evidence
  topic: Citation accuracy, model/map and snippets
  outcome: supported
  summary: The DOI/title/authors, 7TFS identity, 4.3 Å resolution, EMD-25879 link
    and full-polymer UniProt mapping match their sources. Evidence is attached to
    the relevant claims. No snippet fields are present, so no verbatim quotation mismatch
    is possible.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - record
  - crossref
  - pubmed
  - pdb-entry
  - pdb-polymer
  - emdb
- assessment_id: completeness
  area: completeness
  topic: Hierarchy, cofactors, optional images/properties and other surfaces
  outcome: supported
  summary: No unsupported hierarchy or cross-corpus link is asserted. Covalent hemes
    are represented in the component/function mechanism; lack of a separate cofactor
    row, image or numeric-property row is not itself a defect. The study discusses
    putative glycosylation, but its identity is unresolved and the record need not
    invent a glycan component.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - record
  - paper
  - repository-context
- assessment_id: provenance
  area: provenance
  topic: Open discussion, PROPOSED status and history
  outcome: supported
  summary: The exact-family discussion is actionable and honest about scope. Three
    record events and the append-only CREATE history are consistent with the existing
    content. PROPOSED remains appropriate; this review neither promotes status nor
    reopens/closes historical remote issues.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - record
  - repository-context
  - family
- assessment_id: validation
  area: schema
  topic: Focused open and closed validation
  outcome: supported
  summary: Both focused validators pass. Native corpus checks are integrated separately
    by the coordinating reviewer.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  evidence_ids:
  - schema
findings:
- finding_id: F1
  issue_key: omce-pdb-source-not-common-prevalence
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: PDB source provenance does not establish COMMON occurrence
  description: taxonomic_distribution[0] assigns COMMON to PCA while citing only the
    natural-source metadata for one deposited model. COMMON explicitly means occurrence
    in most members with losses exceptional. The paper establishes purified OmcE filaments
    in engineered OmcS-variant PCA derivatives, not population- or condition-level
    prevalence. The qualified note correctly identifies source provenance but does
    not support the stronger machine-readable frequency. The paper also documents
    prior evidence of native OmcE protein production; this finding does not imply
    natural absence. Preserve the canonical source example; remove this distribution
    row unless evidence for an actual occurrence-frequency claim is supplied. COMMON
    does not itself require constitutive expression in every condition; the finding
    concerns the unsupported most-member quantifier, not universal expression.
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  field_paths:
  - taxonomic_distribution[0].presence
  - taxonomic_distribution[0].reference
  evidence_ids:
  - record
  - presence-schema
  - pdb-polymer
  - paper
  rule_id: 'review-yaml-record: preserve taxon and experimental scope; local checklist
    taxonomic distribution'
  normalization_reason: Major because a machine-readable biological prevalence claim
    exceeds the cited evidence, even though the adjacent source-provenance note is
    accurate.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/omce_cytochrome_nanowire.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Remove the unsupported taxonomic_distribution row and retain the PCA
    canonical example and protein-example provenance. Alternatively, provide directly
    relevant occurrence evidence and encode only its supported scope; do not substitute
    another frequency enum based solely on the deposition.
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:omce_cytochrome_nanowire
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/omce_cytochrome_nanowire.yaml
    role: maintained scientific record
  acceptance_checks:
  - Every remaining presence enum is justified by evidence about occurrence consistency,
    not merely a PDB natural source.
  - PCA source/strain information remains in canonical_examples and protein_examples.
  - Run focused open/strict validators and required curation/history gates after any
    separately authorized edit.
limitations:
- Exact source-neutral OmcE family grounding remains unresolved after bounded current
  authority searches; the existing label-only representation and open TODO preserve
  that uncertainty.
- Cryo-EM supports architecture; the electron-transfer path remains a proposed structural
  interpretation, as already stated by the record.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Explicit user instruction authorizes clean as well as issue-bearing review output;
  no finding is invented to satisfy the persistence gate.
- No scientific record, generated artifact, curation history, remote content or paid
  service was changed.
- Initial publisher/fullTextXML/PDF routes failed, but complete PMC HTML was retrieved
  and the relevant results, figures/captions, discussion and methods were read. No
  unresolved source-body access gap affects the reviewed claims.
- Structured UniProt, PDB, EMDB and InterPro APIs supplied protein/structure cross-checks.
  No expression-module or transcriptomic claim is asserted by this record.
```
