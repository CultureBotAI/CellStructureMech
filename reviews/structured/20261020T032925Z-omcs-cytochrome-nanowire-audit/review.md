# OmcS cytochrome nanowire: scoped scientific review

- Review: 20261020T032925Z-omcs-cytochrome-nanowire-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-19T23:38:57Z
- Finished UTC: 2026-10-20T03:29:25Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

All present OmcS claims were assessed against two full papers and live authorities. Identity, composition, strain mapping, purified-filament conductivity and structural graph are supported. One major scope finding remains: PDB natural-source provenance does not establish COMMON prevalence.

## Scope And Provenance

One complete maintained OmcS cytochrome nanowire record, including all present sections and material identifiers/claims.

Selection: Exact batch-002 queued path data/structures/appendage/omcs_cytochrome_nanowire.yaml; one record per bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:omcs_cytochrome_nanowire | data/structures/appendage/omcs_cytochrome_nanowire.yaml | maintained | OmcS cytochrome nanowire |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Open LinkML target validation | passed | True | cellstructuremech:omcs_cytochrome_nanowire | Exit0; No issues found. |
| Closed LinkML target validation | passed | True | cellstructuremech:omcs_cytochrome_nanowire | Exit0; one file scanned, zero ERROR rows. |
| Authority and nearest-source claim audit | passed | True | cellstructuremech:omcs_cytochrome_nanowire | Source review completed with exact DOI/PDB/UniProt/taxon verification and full-paper reading; unsupported frequency is recorded as a scientific finding. |
| Verbatim snippet verification | not_applicable | False | cellstructuremech:omcs_cytochrome_nanowire | No snippet fields present. |
| Target resolver coverage including residuals | passed | True | cellstructuremech:omcs_cytochrome_nanowire | Collected values resolve through shared report plus scoped PDB/local receipts; scientific claim support is separately assessed. |
| Full corpus QC | passed | True | cellstructuremech:omcs_cytochrome_nanowire | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:omcs_cytochrome_nanowire | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:omcs_cytochrome_nanowire | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:omcs_cytochrome_nanowire | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:omcs_cytochrome_nanowire | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Assembled filament, nomenclature and local identity

identity: supported. Targets: cellstructuremech:omcs_cytochrome_nanowire.

Definition and synonyms denote the assembled OmcS nanowire rather than the soluble protein, OmcE/OmcZ or all bacterial nanowires. The broader cytochrome-based bacterial nanowire phrase is correctly RELATED. No unsupported GO parent is asserted.

### Six-heme protein constituent and assembly essentiality

grounding: supported. Targets: cellstructuremech:omcs_cytochrome_nanowire.

Both cryo-EM sources establish a helical OmcS homopolymer with six covalently bound hemes per mature subunit. ESSENTIAL refers to formation of this named filament, not organism viability. The component is taxon-neutral while its accession example is strain-paired.

### Protein identity and structural mappings

grounding: supported. Targets: cellstructuremech:omcs_cytochrome_nanowire.

Q74A86/omcS is reviewed and correctly named; both PDB structures map the mature residues26–432 to it and declare PCA natural-source taxon243231. No precursor/mature-chain mismatch is asserted by the record.

### Natural occurrence versus unqualified COMMON

scope: concern. Targets: cellstructuremech:omcs_cytochrome_nanowire.

PCA is valid source provenance. Wang provides direct WT filament observations in electrode and fumarate preparations, and both papers support native production. That is positive occurrence evidence, but the cited PDB6EF8 natural-source field does not establish the COMMON quantifier across members/conditions. Neither natural absence nor failure of WT production is inferred.

### Purified-filament electron transport

evidence: supported. Targets: cellstructuremech:omcs_cytochrome_nanowire.

Wang combines structural evidence and hydrated individual-filament conductivity measurements; Filman independently supports the structural heme route. The record restricts its function to a path in purified nanowires and does not assert a specific hopping rate, physiological circuit or exclusion of other filament types.

### Three edges and four nodes

graph: supported. Targets: cellstructuremech:omcs_cytochrome_nanowire.

Polymerization, six-heme alignment and the structural path for electron transfer are supported at the stated level. Internal component and local structure references resolve. The graph does not specify unmeasured entry/exit chemistry or export machinery; its mechanistic scope remains a structural conduction explanation.

### Label-only family and CDD candidate

grounding: supported. Targets: cellstructuremech:omcs_cytochrome_nanowire.

The historical note says no exact InterPro/Pfam/NCBIfam grounding was verified, rather than claiming none can exist. Current broad mappings still do not establish exact equivalence. CDD cd21555 provides a useful candidate for the existing open discussion, but similarly matched proteins cannot automatically be declared filament subunits. No required identity is missing from this otherwise grounded component.

### DOI/PDB identities, 3.4 Å value and quotation status

evidence: supported. Targets: cellstructuremech:omcs_cytochrome_nanowire.

Both exact papers, authors/titles, PDB associations and the Filman3.4 Å resolution are verified. Evidence is local to the structural/functional claims. There are no snippet fields requiring verbatim text matching.

### Optional surfaces, discussions and record history

completeness: supported. Targets: cellstructuremech:omcs_cytochrome_nanowire.

No fixed filament stoichiometry, image, extra physical property or cross-corpus dataset link is mandatory for these claims. The family TODO is actionable. The PROPOSED status and three curation events agree with the append-only creation history; no historical remote issue disposition is made.

### Open and strict target checks

schema: supported. Targets: cellstructuremech:omcs_cytochrome_nanowire.

Both focused native validators pass.

## Findings

### F1: COMMON occurrence exceeds the PDB source-provenance evidence

major / open / confirmed; issue key: omcs-pdb-source-not-common-prevalence.

The distribution row cites PDB6EF8 and qualifies its note solely as PCA source provenance. That supports the canonical strain example, but COMMON separately asserts occurrence in most members with exceptional losses. The inspected studies show native WT OmcS filaments under specified culture/preparation conditions, not the prevalence implied by this unqualified frequency enum. Remove the unsupported distribution assertion unless directly relevant frequency evidence is supplied; retain PCA source information. This is not an absence claim. COMMON does not itself require constitutive expression in every condition; the finding concerns the unsupported most-member quantifier, not universal expression.

## Recommended Actions And Acceptance Checks

### A1

Remove the PDB-only COMMON distribution row while retaining the PCA canonical example and protein example, or provide evidence that directly establishes the chosen prevalence and add its experimental scope. Do not substitute another frequency label solely from a structure deposition.

- Every presence enum is supported by occurrence-consistency evidence, not just a deposited source organism.
- PCA identity and PDB/UniProt mappings remain intact.
- Run focused validators and required curation/history gates after any separately authorized scientific change.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/omcs_cytochrome_nanowire.yaml | supports | Full maintained record read: local identity, two synonyms, one protein component, PCA distribution/example, one function, four-node/three-edge graph and open family-grounding discussion. |
| wang | https://pmc.ncbi.nlm.nih.gov/articles/PMC6720112/; Results; Figs.1–4 and S4; STAR Methods: strains, purification and DC conductivity | supports | Full Wang et al. body supports a helical OmcS homopolymer with six covalently bound hemes per subunit and an axial heme path. WT electrode-grown material supplied the atomic model; fumarate-grown filaments had similar structure. Figure 4 and methods report hydrated individual-filament DC conductivity, using OmcS-deletion filaments and buffer as comparators. |
| filman | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6584659/fullTextXML; Results and Discussion; Table 1; Figs.1–3; Methods | supports | Full Filman et al. body independently identifies a 3.4 Å OmcS filament with contiguous mature subunits and an unbranched heme stack. It proposes the stack as a long-range electron pathway while leaving charge entry/exit open. Preparation involved electrode-grown biofilms; it does not estimate prevalence across PCA cells or conditions. |
| doi-wang | https://api.crossref.org/works/10.1016/j.cell.2019.03.029; Crossref DOI/title/authors/publication metadata | supports | DOI 10.1016/j.cell.2019.03.029 is Wang, Gu, OBrien et al. 2019, Structure of Microbial Nanowires Reveals Stacked Hemes that Transport Electrons over Micrometers, Cell. |
| doi-filman | https://api.crossref.org/works/10.1038/s42003-019-0448-9; Crossref DOI/title/authors/publication metadata | supports | DOI 10.1038/s42003-019-0448-9 is Filman, Marino, Ward et al. 2019, Cryo-EM reveals the structural basis of long-range electron transport in a cytochrome-based bacterial nanowire, Communications Biology. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=30951668,31240257&amp;retmode=xml; MedlineCitation and PubmedData/ArticleIdList | supports | PMIDs 30951668 and 31240257 map respectively to the exact Wang and Filman DOIs and PMC6720112/PMC6584659. |
| pdb-wang | https://data.rcsb.org/rest/v1/core/entry/6EF8; struct, rcsb_entry_info, rcsb_primary_citation | supports | PDB 6EF8 is the OmcS cryo-EM model at 3.7 Å with the exact Wang et al. 2019 primary citation. |
| polymer-wang | https://data.rcsb.org/rest/v1/core/polymer_entity/6EF8/1; entity_src_nat; rcsb_entity_source_organism; rcsb_polymer_entity_align | supports | PDB 6EF8 entity 1 natural source is PCA, taxon 243231. Its 407-residue mature polymer maps by SIFTS to Q74A86 residues 26–432. The record correctly asserts the accession linkage without claiming full precursor coverage. |
| pdb-filman | https://data.rcsb.org/rest/v1/core/entry/6NEF; struct, rcsb_entry_info, rcsb_primary_citation | supports | PDB 6NEF is the OmcS cryo-EM model at 3.4 Å with the exact Filman et al. 2019 primary citation. |
| polymer-filman | https://data.rcsb.org/rest/v1/core/polymer_entity/6NEF/1; entity_src_nat; rcsb_entity_source_organism; rcsb_polymer_entity_align | supports | PDB 6NEF entity 1 natural source is PCA, taxon 243231. Its 407-residue mature polymer maps by SIFTS to Q74A86 residues 26–432. The record correctly asserts the accession linkage without claiming full precursor coverage. |
| uniprot | https://rest.uniprot.org/uniprotkb/Q74A86.json; entryType, proteinDescription, genes, organism and sequence | supports | Q74A86 is reviewed Swiss-Prot C-type cytochrome OmcS, gene omcS, locus GSU2504, a 432-residue precursor at taxon 243231; name, accession, gene and status agree. |
| taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=243231&amp;retmode=xml; TaxId, ScientificName and Rank | supports | NCBI Taxonomy 243231 is Geobacter sulfurreducens PCA at strain rank. |
| family | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q74A86/; Six protein-entry mappings | context_only | Q74A86 maps to broad InterPro IPR036280 and IPR051174 models and to CDD cd21555, OmcS-like, over residues 26–430. A broad multiheme/electron-transfer InterPro mapping should not be used as exact filament-subunit family identity. |
| cdd | https://www.ebi.ac.uk/interpro/api/entry/cdd/cd21555/; metadata description, literature and accession; corroborated at NCBI CDD landing page | context_only | CDD cd21555, C-type cytochrome OmcS and similar proteins, explicitly discusses OmcS filament assembly and cites both target papers. It is a relevant source-neutral candidate for the existing TODO; its similar-protein membership and repository CURIE support need evaluation before adopting it as exact nanowire-subunit grounding. |
| go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=OmcS&amp;limit=100; numberOfHits/results | context_only | QuickGO search for OmcS returned zero hits. This supports retaining the local structure identifier within the bounded terminology check; it is not an exhaustive claim about every synonym. |
| presence-schema | src/cellstructuremech/schema/cellstructuremech.yaml; PresenceEnum.COMMON, TaxonomicScope and CanonicalExample | supports | COMMON means present in most members, losses exceptional. TaxonomicScope models occurrence consistency; CanonicalExample separately records a source organism. |
| repository-context | history/records/omcs_cytochrome_nanowire/ | supports | Ignored-inclusive search located this record, OmcE/OmcZ siblings and one CREATE history file; no matching structured review was found in the bounded reviews root. History explains prior narrowing to PCA and removal of unsupported projection parentage; the existing history is not a new review finding. |
| schema | justfile; validate and validate-strict recipes; external strict.tsv | supports | Focused open validation exited0, No issues found; strict validation exited0, one file scanned with zero ERROR rows. |
| target-resolver-coverage | just check-curies-strict; data/structures/appendage/omcs_cytochrome_nanowire.yaml; exact collect() scope; shared reports/curie_check.tsv | supports | The exact collection has 7 CURIE-shaped scalars: {'OK': 4, 'SKIPPED': 3}. Skipped PDB identifiers resolve in the attached exact deposition receipts; the minted local target resolves in the maintained record. HTTP URLs and prose are checked separately. Existence does not imply correct biological mapping. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The heme-stack path is supported structurally and the purified filaments conduct electricity; the complete microscopic transport mechanism, charge entry/exit and physiological circuitry are outside the encoded scope.
- CDD cd21555 is a verified OmcS-like candidate, not an adopted exact grounding for all extracellular OmcS filament subunits.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Explicit user instruction requests clean and issue-bearing review bundles; no finding was invented to justify persistence.
- No maintained record, generated artifact, history, remote content or paid provider was changed.
- Full Wang HTML and full Filman JATS were accessible despite alternate publisher/XML failures. No unresolved paper-body access gap affects these claims.
- Structured UniProt/PDB/InterPro/CDD sources supplied gene and protein checks; no expression-module or transcriptomic claim is asserted by the record.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T032925Z-omcs-cytochrome-nanowire-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'OmcS cytochrome nanowire: scoped scientific review'
started_at: '2026-10-19T23:38:57Z'
finished_at: '2026-10-20T03:29:25Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Delegated Codex agent reviewed an existing agent-authored record
    in the isolated batch clone. Reviewer did not author or edit the target during
    this task; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'All present OmcS claims were assessed against two full papers and live authorities.
  Identity, composition, strain mapping, purified-filament conductivity and structural
  graph are supported. One major scope finding remains: PDB natural-source provenance
  does not establish COMMON prevalence.'
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
    role: context
  - path: data/structures/appendage/omcs_cytochrome_nanowire.yaml
    sha256: ca7929cfc24552723a28266b0c42c392052caa65a5a7115f6b41c1fde5248eb2
    role: target
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
  - path: history/records/omcs_cytochrome_nanowire/2026-09-11T150406Z-codex-bc6a30.yaml
    sha256: 6f0eb289d3e06d27f029e0d84c20da2a742d060ccc64a2bd52b9e247f271bee3
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
- target_id: cellstructuremech:omcs_cytochrome_nanowire
  path: data/structures/appendage/omcs_cytochrome_nanowire.yaml
  label: OmcS cytochrome nanowire
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/omcs_cytochrome_nanowire.yaml
    role: maintained scientific record
scope:
  description: One complete maintained OmcS cytochrome nanowire record, including
    all present sections and material identifiers/claims.
  selection: Exact batch-002 queued path data/structures/appendage/omcs_cytochrome_nanowire.yaml;
    one record per bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
checks:
- check_id: open-schema
  name: Open LinkML target validation
  status: passed
  required: true
  summary: Exit0; No issues found.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate data/structures/appendage/omcs_cytochrome_nanowire.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema
- check_id: strict-schema
  name: Closed LinkML target validation
  status: passed
  required: true
  summary: Exit0; one file scanned, zero ERROR rows.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate-strict data/structures/appendage/omcs_cytochrome_nanowire.yaml --out
    /private/tmp/cellstructure-batch2-20261019-52rdp0/omcs-review/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema
- check_id: source-audit
  name: Authority and nearest-source claim audit
  status: passed
  required: true
  summary: Source review completed with exact DOI/PDB/UniProt/taxon verification and
    full-paper reading; unsupported frequency is recorded as a scientific finding.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - wang
  - filman
  - doi-wang
  - doi-filman
  - pubmed
  - pdb-wang
  - pdb-filman
  - polymer-wang
  - polymer-filman
  - uniprot
  - taxon
  - family
  - cdd
- check_id: snippets
  name: Verbatim snippet verification
  status: not_applicable
  required: false
  summary: No snippet fields present.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - record
- check_id: target-resolver-coverage
  name: Target resolver coverage including residuals
  status: passed
  required: true
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  summary: Collected values resolve through shared report plus scoped PDB/local receipts;
    scientific claim support is separately assessed.
  evidence_ids:
  - target-resolver-coverage
  - pdb-wang
  - pdb-filman
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
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
  - cellstructuremech:omcs_cytochrome_nanowire
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
  - cellstructuremech:omcs_cytochrome_nanowire
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
  - cellstructuremech:omcs_cytochrome_nanowire
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
  - cellstructuremech:omcs_cytochrome_nanowire
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
  reference: data/structures/appendage/omcs_cytochrome_nanowire.yaml
  accessed_at: '2026-10-19T23:41:35Z'
  support: supports
  summary: 'Full maintained record read: local identity, two synonyms, one protein
    component, PCA distribution/example, one function, four-node/three-edge graph
    and open family-grounding discussion.'
  snapshot_sha256: ca7929cfc24552723a28266b0c42c392052caa65a5a7115f6b41c1fde5248eb2
- evidence_id: wang
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6720112/
  accessed_at: '2026-10-19T23:39:49Z'
  support: supports
  summary: Full Wang et al. body supports a helical OmcS homopolymer with six covalently
    bound hemes per subunit and an axial heme path. WT electrode-grown material supplied
    the atomic model; fumarate-grown filaments had similar structure. Figure 4 and
    methods report hydrated individual-filament DC conductivity, using OmcS-deletion
    filaments and buffer as comparators.
  locator: 'Results; Figs.1–4 and S4; STAR Methods: strains, purification and DC conductivity'
  snapshot_sha256: a9d90e24f29212af0dab76ef7334880f204722e71345c2ffb14a178014f3e2db
- evidence_id: filman
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6584659/fullTextXML
  accessed_at: '2026-10-19T23:39:49Z'
  support: supports
  summary: Full Filman et al. body independently identifies a 3.4 Å OmcS filament
    with contiguous mature subunits and an unbranched heme stack. It proposes the
    stack as a long-range electron pathway while leaving charge entry/exit open. Preparation
    involved electrode-grown biofilms; it does not estimate prevalence across PCA
    cells or conditions.
  locator: Results and Discussion; Table 1; Figs.1–3; Methods
  snapshot_sha256: 68faadf0f159d0f8cbb26afa4c3fd9a9418fe22e88fbb6768ae29aae6074eed9
- evidence_id: doi-wang
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.cell.2019.03.029
  accessed_at: '2026-10-19T23:39:34Z'
  support: supports
  summary: DOI 10.1016/j.cell.2019.03.029 is Wang, Gu, OBrien et al. 2019, Structure
    of Microbial Nanowires Reveals Stacked Hemes that Transport Electrons over Micrometers,
    Cell.
  locator: Crossref DOI/title/authors/publication metadata
  snapshot_sha256: 9824161346cb42e64e1bcce0f08ab7c95798a3218be01424afd1e95403c4b638
- evidence_id: doi-filman
  kind: database
  reference: https://api.crossref.org/works/10.1038/s42003-019-0448-9
  accessed_at: '2026-10-19T23:39:34Z'
  support: supports
  summary: DOI 10.1038/s42003-019-0448-9 is Filman, Marino, Ward et al. 2019, Cryo-EM
    reveals the structural basis of long-range electron transport in a cytochrome-based
    bacterial nanowire, Communications Biology.
  locator: Crossref DOI/title/authors/publication metadata
  snapshot_sha256: f835f0bcbee53a4dd7274636cbaf336fe6e0c9f2a14f3d63472755a551819cd8
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=30951668,31240257&retmode=xml
  accessed_at: '2026-10-19T23:40:24Z'
  support: supports
  summary: PMIDs 30951668 and 31240257 map respectively to the exact Wang and Filman
    DOIs and PMC6720112/PMC6584659.
  locator: MedlineCitation and PubmedData/ArticleIdList
  snapshot_sha256: 72398384afa7bd89317ccf2d514e62781f73b02ac61016670bc1e91acd02366e
- evidence_id: pdb-wang
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/6EF8
  accessed_at: '2026-10-19T23:39:34Z'
  support: supports
  summary: PDB 6EF8 is the OmcS cryo-EM model at 3.7 Å with the exact Wang et al.
    2019 primary citation.
  locator: struct, rcsb_entry_info, rcsb_primary_citation
  snapshot_sha256: de2672f1a5f12f3f5b66ab091432593a6f35fdf37eadd694a28fe5b31c044035
- evidence_id: polymer-wang
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6EF8/1
  accessed_at: '2026-10-19T23:39:34Z'
  support: supports
  summary: PDB 6EF8 entity 1 natural source is PCA, taxon 243231. Its 407-residue
    mature polymer maps by SIFTS to Q74A86 residues 26–432. The record correctly asserts
    the accession linkage without claiming full precursor coverage.
  locator: entity_src_nat; rcsb_entity_source_organism; rcsb_polymer_entity_align
  snapshot_sha256: 15f3fa8b5a2fcace3dc6d19a49883654e8529459b0a346e8ef43232f0996b5d7
- evidence_id: pdb-filman
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/6NEF
  accessed_at: '2026-10-19T23:39:34Z'
  support: supports
  summary: PDB 6NEF is the OmcS cryo-EM model at 3.4 Å with the exact Filman et al.
    2019 primary citation.
  locator: struct, rcsb_entry_info, rcsb_primary_citation
  snapshot_sha256: 6aead5ea79d50d564fec3563294c33b23e5d32ffa08e4c5a4eb779190bd32960
- evidence_id: polymer-filman
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6NEF/1
  accessed_at: '2026-10-19T23:39:34Z'
  support: supports
  summary: PDB 6NEF entity 1 natural source is PCA, taxon 243231. Its 407-residue
    mature polymer maps by SIFTS to Q74A86 residues 26–432. The record correctly asserts
    the accession linkage without claiming full precursor coverage.
  locator: entity_src_nat; rcsb_entity_source_organism; rcsb_polymer_entity_align
  snapshot_sha256: 7dc9162e4c5beedd43588eec0769e780b2819dfc7e9527fc79911808a00cd71e
- evidence_id: uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q74A86.json
  accessed_at: '2026-10-19T23:39:34Z'
  support: supports
  summary: Q74A86 is reviewed Swiss-Prot C-type cytochrome OmcS, gene omcS, locus
    GSU2504, a 432-residue precursor at taxon 243231; name, accession, gene and status
    agree.
  locator: entryType, proteinDescription, genes, organism and sequence
  snapshot_sha256: a404e1d1c232dfbac470cf500de60d52e76d4b6b4888814d1e539b1bc4eb00f2
- evidence_id: taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=243231&retmode=xml
  accessed_at: '2026-10-19T23:39:34Z'
  support: supports
  summary: NCBI Taxonomy 243231 is Geobacter sulfurreducens PCA at strain rank.
  locator: TaxId, ScientificName and Rank
  snapshot_sha256: f1291f188fae1b43a82d2f75e98d90aa41434ef36115f217a9485629eebb2736
- evidence_id: family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q74A86/
  accessed_at: '2026-10-19T23:39:34Z'
  support: context_only
  summary: Q74A86 maps to broad InterPro IPR036280 and IPR051174 models and to CDD
    cd21555, OmcS-like, over residues 26–430. A broad multiheme/electron-transfer
    InterPro mapping should not be used as exact filament-subunit family identity.
  locator: Six protein-entry mappings
  snapshot_sha256: d93ac404e1579e212c297ff91efb8b5f9d262b2407d8966a3d95f146e51a64ef
- evidence_id: cdd
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/cdd/cd21555/
  accessed_at: '2026-10-19T23:40:24Z'
  support: context_only
  summary: CDD cd21555, C-type cytochrome OmcS and similar proteins, explicitly discusses
    OmcS filament assembly and cites both target papers. It is a relevant source-neutral
    candidate for the existing TODO; its similar-protein membership and repository
    CURIE support need evaluation before adopting it as exact nanowire-subunit grounding.
  locator: metadata description, literature and accession; corroborated at NCBI CDD
    landing page
  snapshot_sha256: 8702af0371dbdbe73dd4d8b17c04b4eee9b8fc40e497d0cd9fed778a97de6d19
- evidence_id: go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=OmcS&limit=100
  accessed_at: '2026-10-19T23:39:34Z'
  support: context_only
  summary: QuickGO search for OmcS returned zero hits. This supports retaining the
    local structure identifier within the bounded terminology check; it is not an
    exhaustive claim about every synonym.
  locator: numberOfHits/results
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: QuickGO ontology/go/search query OmcS, limit100. InterPro all-entry
    search OmcS returned one CDD candidate, inspected separately.
- evidence_id: presence-schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  accessed_at: '2026-10-19T23:41:35Z'
  support: supports
  summary: COMMON means present in most members, losses exceptional. TaxonomicScope
    models occurrence consistency; CanonicalExample separately records a source organism.
  locator: PresenceEnum.COMMON, TaxonomicScope and CanonicalExample
- evidence_id: repository-context
  kind: search
  reference: history/records/omcs_cytochrome_nanowire/
  accessed_at: '2026-10-19T23:41:35Z'
  support: supports
  summary: Ignored-inclusive search located this record, OmcE/OmcZ siblings and one
    CREATE history file; no matching structured review was found in the bounded reviews
    root. History explains prior narrowing to PCA and removal of unsupported projection
    parentage; the existing history is not a new review finding.
  search_scope: rg --no-ignore --hidden -l --glob '!.git/**' --glob '!.venv/**' --glob
    '!review.md' 'omcs_cytochrome_nanowire|OmcS|6EF8|6NEF|Q74A86' history/records
    data/structures reviews/structured; git log --format='%H %cI %s' -- target path.
    Ignored files included in those roots. Addition commit49bb9764b1f3c9634fa24bd81da0618504748a6b.
- evidence_id: schema
  kind: validation
  reference: justfile
  accessed_at: '2026-10-19T23:41:35Z'
  support: supports
  summary: Focused open validation exited0, No issues found; strict validation exited0,
    one file scanned with zero ERROR rows.
  locator: validate and validate-strict recipes; external strict.tsv
  snapshot_sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
- evidence_id: target-resolver-coverage
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/omcs_cytochrome_nanowire.yaml; exact collect()
    scope; shared reports/curie_check.tsv
  accessed_at: '2026-10-19T23:41:41.324461Z'
  support: supports
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
  summary: 'The exact collection has 7 CURIE-shaped scalars: {''OK'': 4, ''SKIPPED'':
    3}. Skipped PDB identifiers resolve in the attached exact deposition receipts;
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
  topic: Assembled filament, nomenclature and local identity
  outcome: supported
  summary: Definition and synonyms denote the assembled OmcS nanowire rather than
    the soluble protein, OmcE/OmcZ or all bacterial nanowires. The broader cytochrome-based
    bacterial nanowire phrase is correctly RELATED. No unsupported GO parent is asserted.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - record
  - wang
  - filman
  - go-search
- assessment_id: composition
  area: grounding
  topic: Six-heme protein constituent and assembly essentiality
  outcome: supported
  summary: Both cryo-EM sources establish a helical OmcS homopolymer with six covalently
    bound hemes per mature subunit. ESSENTIAL refers to formation of this named filament,
    not organism viability. The component is taxon-neutral while its accession example
    is strain-paired.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - record
  - wang
  - filman
  - uniprot
- assessment_id: protein-example
  area: grounding
  topic: Protein identity and structural mappings
  outcome: supported
  summary: Q74A86/omcS is reviewed and correctly named; both PDB structures map the
    mature residues26–432 to it and declare PCA natural-source taxon243231. No precursor/mature-chain
    mismatch is asserted by the record.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - uniprot
  - taxon
  - polymer-wang
  - polymer-filman
  - pdb-wang
  - pdb-filman
- assessment_id: taxonomic-scope
  area: scope
  topic: Natural occurrence versus unqualified COMMON
  outcome: concern
  summary: PCA is valid source provenance. Wang provides direct WT filament observations
    in electrode and fumarate preparations, and both papers support native production.
    That is positive occurrence evidence, but the cited PDB6EF8 natural-source field
    does not establish the COMMON quantifier across members/conditions. Neither natural
    absence nor failure of WT production is inferred.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - record
  - presence-schema
  - polymer-wang
  - polymer-filman
  - wang
  - filman
  dimensions:
  - name: experimental-context
    value: WT DL1/PCA source material; electrode-grown atomic-model preparations and
      fumarate-grown comparison; hydrated purified-filament DC measurements
    definition: Preserves experimentally established conditions without turning model-source
      provenance into a frequency estimate.
    evidence_ids:
    - wang
    - filman
    - polymer-wang
- assessment_id: function
  area: evidence
  topic: Purified-filament electron transport
  outcome: supported
  summary: Wang combines structural evidence and hydrated individual-filament conductivity
    measurements; Filman independently supports the structural heme route. The record
    restricts its function to a path in purified nanowires and does not assert a specific
    hopping rate, physiological circuit or exclusion of other filament types.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - record
  - wang
  - filman
  dimensions:
  - name: evidence-tier
    value: Direct conductivity measurements plus cryo-EM structural interpretation
    definition: Distinguishes measured electrical behavior from the detailed microscopic
      transport mechanism.
    evidence_ids:
    - wang
    - filman
- assessment_id: graph
  area: graph
  topic: Three edges and four nodes
  outcome: supported
  summary: Polymerization, six-heme alignment and the structural path for electron
    transfer are supported at the stated level. Internal component and local structure
    references resolve. The graph does not specify unmeasured entry/exit chemistry
    or export machinery; its mechanistic scope remains a structural conduction explanation.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - record
  - wang
  - filman
- assessment_id: family-grounding
  area: grounding
  topic: Label-only family and CDD candidate
  outcome: supported
  summary: The historical note says no exact InterPro/Pfam/NCBIfam grounding was verified,
    rather than claiming none can exist. Current broad mappings still do not establish
    exact equivalence. CDD cd21555 provides a useful candidate for the existing open
    discussion, but similarly matched proteins cannot automatically be declared filament
    subunits. No required identity is missing from this otherwise grounded component.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - record
  - family
  - cdd
- assessment_id: bibliography
  area: evidence
  topic: DOI/PDB identities, 3.4 Å value and quotation status
  outcome: supported
  summary: Both exact papers, authors/titles, PDB associations and the Filman3.4 Å
    resolution are verified. Evidence is local to the structural/functional claims.
    There are no snippet fields requiring verbatim text matching.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - record
  - doi-wang
  - doi-filman
  - pubmed
  - pdb-wang
  - pdb-filman
- assessment_id: completeness-provenance
  area: completeness
  topic: Optional surfaces, discussions and record history
  outcome: supported
  summary: No fixed filament stoichiometry, image, extra physical property or cross-corpus
    dataset link is mandatory for these claims. The family TODO is actionable. The
    PROPOSED status and three curation events agree with the append-only creation
    history; no historical remote issue disposition is made.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - record
  - repository-context
- assessment_id: validation
  area: schema
  topic: Open and strict target checks
  outcome: supported
  summary: Both focused native validators pass.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  evidence_ids:
  - schema
findings:
- finding_id: F1
  issue_key: omcs-pdb-source-not-common-prevalence
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: COMMON occurrence exceeds the PDB source-provenance evidence
  description: The distribution row cites PDB6EF8 and qualifies its note solely as
    PCA source provenance. That supports the canonical strain example, but COMMON
    separately asserts occurrence in most members with exceptional losses. The inspected
    studies show native WT OmcS filaments under specified culture/preparation conditions,
    not the prevalence implied by this unqualified frequency enum. Remove the unsupported
    distribution assertion unless directly relevant frequency evidence is supplied;
    retain PCA source information. This is not an absence claim. COMMON does not itself
    require constitutive expression in every condition; the finding concerns the unsupported
    most-member quantifier, not universal expression.
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  field_paths:
  - taxonomic_distribution[0].presence
  - taxonomic_distribution[0].reference
  evidence_ids:
  - record
  - presence-schema
  - polymer-wang
  - wang
  - filman
  rule_id: 'review-yaml-record: preserve experimental/taxonomic scope; local taxonomic-distribution
    checklist'
  normalization_reason: Major because machine-readable prevalence extends beyond the
    exact cited source, although native filament occurrence and source strain are
    well supported.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/omcs_cytochrome_nanowire.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Remove the PDB-only COMMON distribution row while retaining the PCA
    canonical example and protein example, or provide evidence that directly establishes
    the chosen prevalence and add its experimental scope. Do not substitute another
    frequency label solely from a structure deposition.
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:omcs_cytochrome_nanowire
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/omcs_cytochrome_nanowire.yaml
    role: maintained scientific record
  acceptance_checks:
  - Every presence enum is supported by occurrence-consistency evidence, not just
    a deposited source organism.
  - PCA identity and PDB/UniProt mappings remain intact.
  - Run focused validators and required curation/history gates after any separately
    authorized scientific change.
limitations:
- The heme-stack path is supported structurally and the purified filaments conduct
  electricity; the complete microscopic transport mechanism, charge entry/exit and
  physiological circuitry are outside the encoded scope.
- CDD cd21555 is a verified OmcS-like candidate, not an adopted exact grounding for
  all extracellular OmcS filament subunits.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Explicit user instruction requests clean and issue-bearing review bundles; no finding
  was invented to justify persistence.
- No maintained record, generated artifact, history, remote content or paid provider
  was changed.
- Full Wang HTML and full Filman JATS were accessible despite alternate publisher/XML
  failures. No unresolved paper-body access gap affects these claims.
- Structured UniProt/PDB/InterPro/CDD sources supplied gene and protein checks; no
  expression-module or transcriptomic claim is asserted by the record.
```
