# Ciliary transition fiber: scientific and identifier review

- Review: 20261019T233309Z-ciliary-transition-fiber-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-19T07:33:17Z
- Finished UTC: 2026-10-19T23:33:09Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Complete target content assessed. Exact structure identity, bounded experimental claims and link-only figure provenance are supported. One major incorrect TFK1 accession and one minor stale discussion statement require curation.

## Scope And Provenance

One complete maintained ciliary transition fiber record; all present native sections and cited identifiers assessed.

Selection: Exact queued path data/structures/appendage/ciliary_transition_fiber.yaml in the unreviewed corpus path order; one record per bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097539 | data/structures/appendage/ciliary_transition_fiber.yaml | maintained | ciliary transition fiber |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Open LinkML target validation | passed | True | GO:0097539 | No issues found; exit 0. |
| Closed LinkML target validation | passed | True | GO:0097539 | One file scanned; zero ERROR rows; exit 0. |
| Live identifiers and claim-by-claim source inspection | passed | True | GO:0097539 | All stable record identifiers and material claims checked against fetched authority data, the two primary studies, the 2017 author abstract and linked figure metadata. Scientific defects are recorded separately. |
| Verbatim evidence snippets | not_applicable | False | GO:0097539 | The target has no snippet fields; source-backed notes were assessed directly. |
| Target identifier coverage including resolver residuals | passed | True | GO:0097539 | All CURIE-shaped target values have issuing-authority or appropriate local/source-specific existence verification. Generic PMID HTTP414 failures and skipped namespaces were resolved by scoped receipts; biological mapping correctness is assessed separately. |
| Full corpus QC | passed | True | GO:0097539 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097539 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097539 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097539 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0097539 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Structure boundary, ontology identity and synonym scope

identity: supported. Targets: GO:0097539.

The target denotes a discrete appendage complex; neither the enclosing basal body nor the adjacent transition-zone Y-link is conflated with it. Definition, category, kind, synonyms and is-a placement are supported. Basal-body parthood is anatomical rather than an explicit QuickGO ancestor here.

### Component family grounding and protein-example identity

grounding: concern. Targets: GO:0097539.

The four component classes have bounded source support and retain unknown assembly essentiality. XRP2/FBF1 family terms and TFK1/CEP164 label-only decisions are appropriate. The TFK1 accession row denotes a different protein; other accession labels, entry statuses and loci are consistent with their source joins.

### Species, strain and experimental context

scope: supported. Targets: GO:0097539.

The canonical species and explicitly stated 2022 strain context are correct. Examples use TREU927 accessions; the 2024 study supplies that background for CEP164A/FBF1. No broad presence/absence or universal stoichiometry claim is made.

### Anatomical linkage and new-flagellum assembly

evidence: supported. Targets: GO:0097539.

Both functions are supported at the declared scope. The record avoids assigning direct lipid binding, exact docking steps or specific IFT-entry reactions to individual trypanosome proteins.

### All three TFK1 targeting and interaction edges

graph: supported. Targets: GO:0097539.

Each edge is supported by the cited assay. The graph separates yeast-two-hybrid interaction from targeting and does not infer their causal connection, native oligomer stoichiometry or complete fiber construction.

### Figure identity, caption, taxon and reuse boundary

provenance: supported. Targets: GO:0097539.

The figure is correctly identified, attributed and linked. Visual inspection confirms panel orientations and scale bars. Record notes follow the Results description of detergent-extracted material while avoiding an intact-membrane inference; the caption itself says whole cells. Link-only treatment matches HAL metadata.

### Declared inventory and optional scientific surfaces

completeness: supported. Targets: GO:0097539.

The incomplete component inventory and unresolved native assembly/gating questions are explicitly disclosed. Unset stoichiometry, distribution, physical properties, traits, datasets and complex compositions do not introduce an unsupported claim or alone constitute a defect.

### Discussion scope after protein-example enrichment

consistency: concern. Targets: GO:0097539.

The open inventory discussion retains a now-false statement that no strain-specific protein example is asserted. Its TFK1 accession caution also exposes the disagreement with the newly added TFK1 row. Other discussion distinctions remain supported.

### Native status, record history and source placement

provenance: supported. Targets: GO:0097539.

The record remains PROPOSED, with agent-attributed creation, scope correction and protein-example history. Source entries are attached to the relevant claims. No native status promotion is implied by this review.

### Open and closed target validation

schema: supported. Targets: GO:0097539.

Both documented target validators pass; scientific accession mismatch is not detected by schema validity.

## Findings

### tfk1-accession: TFK1 protein example points to an unrelated MSP-domain protein

major / open / confirmed; issue key: ciliary-transition-fiber-tfk1-protein-example-mismatch.

components#tfk1 assigns Q382L3/Tb11.01.4810 to TFK1. UniProt identifies it as a 216-residue MSP/VAP-family protein, while the cited study names TFK1 as Tb927.6.1180/XP_845240.1; Q585C9 matches that locus and 1271-residue sequence. Existing grounding and discussion notes already name Q585C9. The incorrect row therefore supplies a false accession-to-component identity, even though its UniProt entry itself resolves.

### stale-example-scope: Inventory discussion still claims that no strain-specific protein examples are asserted

minor / open / confirmed; issue key: ciliary-transition-fiber-stale-protein-example-scope.

The open complete_component_inventory_and_grounding discussion says no strain-specific protein example is asserted, but the current components contain four taxon-paired TREU927 examples. This stale scope statement obscures what was added and which experimental-strain limitation still applies.

## Recommended Actions And Acceptance Checks

### correct-tfk1-example

Remove or correct the erroneous TFK1 protein-example mapping in the maintained YAML through the guarded writer. If Q585C9 is used, preserve the distinction between the TREU927 genomic accession and SmOx427 assay backgrounds, and cite the locus-to-accession join. Append required curation/history records and regenerate pages only during separately authorized curation.

- Resolve the selected accession at UniProt and compare gene locus, RefSeq crossreference and sequence length with DOI:10.1242/jcs.259893.
- Confirm no TFK1 protein example retains Q382L3/Tb11.01.4810; search ignored and hidden files for stale maintained references.
- Run just validate and just validate-strict for the changed target, then the documented corpus/provenance gates and generated-site checks.

### refresh-discussion-scope

Update the inventory discussion to describe the retained protein examples and remaining experimental-strain caveat accurately after resolving the TFK1 row. Preserve its unresolved inventory, family-grounding and stoichiometry questions.

- Read the discussion against every current protein_examples row and verify that its accession and strain statements agree.
- Validate the target and required curation history; regenerate and check rendered output as part of any authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/ciliary_transition_fiber.yaml; Entire YAML; especially components#tfk1 and discussions#complete_component_inventory_and_grounding | context_only | Full maintained record read. Four protein examples are present; the TFK1 row uses Q382L3 although existing grounding/discussion notes identify Q585C9. The discussion still says that no strain-specific protein example is asserted. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097539,GO:0140535,GO:0036064,GO:0097537; results: GO:0097539, GO:0140535, GO:0036064, GO:0097537; definitions, synonyms and children | supports | All terms are current cellular components. Definition and all eleven synonym scopes match. GO:0140535 explicitly lists the target as an is_a child; basal body and Y-shaped link remain distinct structures. |
| go-relations | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097539/ancestors?relations=part_of,is_a; GO:0097539 ancestors for is_a and part_of | partial | The intracellular-complex hierarchy is confirmed. The endpoint does not expose basal-body parthood for this term; its anatomical placement is supported by the primary microscopy studies. |
| uniprot | https://rest.uniprot.org/uniprotkb/search?query=accession%3AQ382L3+OR+accession%3AQ582C1+OR+accession%3AQ388J8+OR+accession%3AQ586A8+OR+accession%3AQ585C9&amp;format=json; Full JSON entries Q382L3, Q585C9, Q582C1, Q388J8 and Q586A8; accession, ORF names, sequence length, taxon, entry status and RefSeq/InterPro crossreferences | refutes | Q382L3 is Tb11.01.4810, a 216-residue MSP/VAP-family protein; Q585C9 is Tb927.6.1180, 1271 residues, linked to XP_845240.1. Q582C1 maps to Tb927.5.2440, Q388J8 to Tb10.61.2870 and Q586A8 to Tb927.6.4100. All are unreviewed in taxon 185431; listed protein labels match. |
| xrp2-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039093/; metadata accession, name, type | supports | IPR039093 is the family Protein XRP2; Q388J8 also carries this InterPro crossreference. Family annotation is not treated as direct tubulin-binding evidence. |
| fbf1-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033561/; metadata accession, name, type | supports | IPR033561 is the Fas-binding factor 1 family. Its non-trypanosome mechanistic annotations do not establish specific reactions in the record organism. |
| tfk1-grounding | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q585C9/; Exact Q585C9 integrated-entry query; HTTP 204 | supports | No integrated InterPro entry returned for Q585C9 in this bounded authority query; retaining reviewed label-only grounding is justified. |
| tfk1-search | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=TFK1; Integrated InterPro search=TFK1; HTTP 204 | supports | The exact TFK1 text search also returned no integrated entry. |
| cep164-grounding | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=CEP164; count=2; IPR063650 and IPR064006 | supports | CEP164 search returned coiled-coil and N-terminal domain entries, both type domain; these do not justify whole-family grounding. |
| ncbi-taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=5691,185431&amp;retmode=xml; Taxon records 5691 and 185431 | supports | 5691 is Trypanosoma brucei (species); 185431 is Trypanosoma brucei brucei TREU927 (strain). Record labels match. |
| tfk1-study | https://hal.science/hal-03817184/document; Accepted manuscript pp.7-14,17-20,24-26; Figures 2,3,5 and S5; Figure 3 p.50 and Figure 5 p.52 visually inspected | supports | The paper identifies TFK1 as Tb927.6.1180/XP_845240.1. It supports relative localization, bounded RNAi interpretation, full-length and T4 yeast-two-hybrid interaction, and T4 targeting with endogenous TFK1 retained. Figure/Methods specify T4 residues 75-536; SmOx P427/B427 are experimental backgrounds. |
| mapping-study | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11190437/fullTextXML; PMC11190437 JATS: Results, Discussion, Materials and Methods; Figure 1H image visually inspected; Figure 5D caption/results | supports | The study supports distinct CEP164 paralogue timing, FBF1 localization and new-flagellum phenotype, and explicitly unresolved docking versus marker-recruitment alternatives. Thirty mapped proteins supplement RP2 and TFK1. Methods use SmOxP9 derived from TREU927. |
| supplement-loci | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11190437/supplementaryFiles; joces-137-261692-TableS1.xlsx, sheet1; rows for FBF1, CEP164A, CEP164b and CEP164C | supports | Table S1 pairs FBF1 with Tb927.6.4100 and CEP164A with Tb927.5.2440, independently confirming the paper-name to UniProt-locus joins for Q586A8 and Q582C1. |
| rp2-antibody | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.protis.2017.07.002&amp;format=json&amp;resultType=core; Europe PMC MED PMID:28822909 author abstract, DOI:10.1016/j.protis.2017.07.002 | supports | The inspected primary abstract attributes mature-basal-body YL1/2 recognition to RP2 rather than tyrosinated alpha-tubulin, supporting the record caution. Full article text was not obtained. |
| pubmed-identities | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=35588197,38572631&amp;retmode=xml; PMIDs 35588197 and 38572631; titles, authors, DOI links and abstracts | supports | Both PMID-to-DOI and article identities match the target bibliography. |
| doi-2022 | https://api.crossref.org/works/10.1242/jcs.259893; Crossref message.DOI, title and authors | supports | DOI resolves to the cited primary article: TFK1, a basal body transition fibre protein that is essential for cytokinesis in &lt;i&gt;Trypanosoma brucei&lt;/i&gt; |
| doi-2024 | https://api.crossref.org/works/10.1242/jcs.261692; Crossref message.DOI, title and authors | supports | DOI resolves to the cited primary article: Identification of 30 transition fibre proteins in<br>                    &lt;i&gt;Trypanosoma brucei&lt;/i&gt;<br>                    reveals a complex and dynamic structure |
| doi-2017 | https://api.crossref.org/works/10.1016/j.protis.2017.07.002; Crossref message.DOI, title and authors | supports | DOI resolves to the cited primary article: Variation in Basal Body Localisation and Targeting of Trypanosome RP2 and FOR20 Proteins |
| hal-metadata | https://api.archives-ouvertes.fr/search/?q=halId_s%3Ahal-03817184&amp;wt=json&amp;fl=%2A; HAL hal-03817184v1 metadata: DOI, authors, fileMain_s, licence_s | supports | The linked deposit matches the 2022 article and author list. Licence metadata identifies HAL deposit authorization; the record correctly keeps the image link-only. |
| hal-authorization | https://about.hal.science/hal-authorisation-v1/; HAL authorization explanatory text | supports | The authorization permits HAL distribution and retains copyright; it is not a Creative Commons figure-reuse licence. |
| search-and-history | repository working tree; history/records/ciliary_transition_fiber; data/structures; reviews; research; curation; git log --all --follow | context_only | Ignored-inclusive search found the maintained target, two sibling boundary mentions, and two record history files; no earlier structured target review was found within the searched review tree. Git history identifies creation in 3e10707b46a5109785636c75aa015b7ced7d0a94 and protein-example update in 00f869634ffe809258200c47a3aa842bbd0bdd24. |
| schema-checks | just validate; just validate-strict; Target file; strict report /private/tmp/cellstructure-record-reviews-UhRFh7/ciliary-review/strict.tsv | supports | Both target validation commands exited 0. Open validation: No issues found. Strict validation: one file scanned, zero files with ERROR, zero ERROR rows. |
| target-resolver-coverage | just check-curies-strict; data/structures/appendage/ciliary_transition_fiber.yaml; exact scripts/check_curies.py collect() scope; reports/curie_check.tsv | supports | This target contains 18 distinct CURIE-shaped scalar values: 15 OK, 2 transport-unreachable and 1 skipped in the global report. The attached scoped receipts resolve each non-OK identifier. HTTP URLs and prose are outside collect(); their content was inspected separately. Existence is not proof of correct biological mapping. |
| liveness-pmid-35588197 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=35588197,38572631&amp;retmode=xml; PubmedArticle/MedlineCitation/PMID joined only to that article's PubmedData/ArticleIdList (not nested cited-reference IDs) | supports | PMID:35588197 resolves through the scoped source inspection. Exact article join: pubmed=35588197, doi=10.1242/jcs.259893, pii=275643. Bibliographic identifier identity; source-claim sufficiency is assessed separately. |
| liveness-pmid-38572631 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=35588197,38572631&amp;retmode=xml; PubmedArticle/MedlineCitation/PMID joined only to that article's PubmedData/ArticleIdList (not nested cited-reference IDs) | supports | PMID:38572631 resolves through the scoped source inspection. Exact article join: pubmed=38572631, pmc=PMC11190437, doi=10.1242/jcs.261692, pii=352266. Bibliographic identifier identity; source-claim sufficiency is assessed separately. |
| liveness-hal-03817184-figure3 | https://api.archives-ouvertes.fr/search/?q=halId_s%3Ahal-03817184&amp;wt=json&amp;fl=%2A; TFK1 accepted manuscript, Figure 3, PDF page 50; visual-inspection receipt in transition-fiber review | supports | hal-03817184:figure3 resolves through the scoped source inspection. HAL identifier and Figure 3 location verified outside the generic CURIE resolver; no image-license conclusion follows from resolution. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- For DOI:10.1016/j.protis.2017.07.002, the primary author abstract supports the sole antibody claim. Europe PMC metadata and the publisher DOI landing route were inspected; complete article text was not obtained.
- This review assesses evidence and source consistency, not experimental replication or a complete cross-taxon component inventory. iModulon expression-module analysis was not used: no expression-module claim informs this structural record.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- User explicitly requested a saved review for every unreviewed target; this review also independently meets the local issue-bearing persistence gate.
- Target and native scientific status were not modified. Temporary source downloads remain outside the repository.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233309Z-ciliary-transition-fiber-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Ciliary transition fiber: scientific and identifier review'
started_at: '2026-10-19T07:33:17Z'
finished_at: '2026-10-19T23:33:09Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Delegated Codex agent review of an existing agent-authored record
    in the coordinating reviewer isolated clone. Reviewer did not author or edit the
    inspected target during this task; no independent human scientific approval is
    claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Complete target content assessed. Exact structure identity, bounded experimental
  claims and link-only figure provenance are supported. One major incorrect TFK1 accession
  and one minor stale discussion statement require curation.
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
  - path: data/structures/appendage/ciliary_transition_fiber.yaml
    sha256: e26c76e51de98b9049c8ca7e2eaec7adc5412fc22c0d39174f6f8a9ef1af1d32
    role: target
  - path: data/structures/appendage/y_shaped_link.yaml
    sha256: 5fddc5796ce37906bdfd10a8e3a91cdb6b6ca38e4a78c04df65c88ac518c3eb7
    role: context
  - path: data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
    sha256: ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36
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
  - path: history/records/ciliary_transition_fiber/2026-10-04T065753Z-codex-1e3045.yaml
    sha256: 36755ca5316ade6e3d21055fe6c6c16bc153d9871ccbf17090422527ebf93e36
    role: context
  - path: history/records/ciliary_transition_fiber/2026-10-04T071625Z-codex-1ffcc8.yaml
    sha256: 6b89ef4de9c402b1710fee6fd476a4bdda55b48ae5f13aaad26e416268ab3136
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
- target_id: GO:0097539
  path: data/structures/appendage/ciliary_transition_fiber.yaml
  label: ciliary transition fiber
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_transition_fiber.yaml
    role: maintained scientific record
scope:
  description: One complete maintained ciliary transition fiber record; all present
    native sections and cited identifiers assessed.
  selection: Exact queued path data/structures/appendage/ciliary_transition_fiber.yaml
    in the unreviewed corpus path order; one record per bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097539
checks:
- check_id: open-schema
  name: Open LinkML target validation
  status: passed
  required: true
  summary: No issues found; exit 0.
  target_ids:
  - GO:0097539
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate data/structures/appendage/ciliary_transition_fiber.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema-checks
- check_id: strict-schema
  name: Closed LinkML target validation
  status: passed
  required: true
  summary: One file scanned; zero ERROR rows; exit 0.
  target_ids:
  - GO:0097539
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate-strict data/structures/appendage/ciliary_transition_fiber.yaml --out
    /private/tmp/cellstructure-record-reviews-UhRFh7/ciliary-review/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema-checks
- check_id: authority-source-review
  name: Live identifiers and claim-by-claim source inspection
  status: passed
  required: true
  summary: All stable record identifiers and material claims checked against fetched
    authority data, the two primary studies, the 2017 author abstract and linked figure
    metadata. Scientific defects are recorded separately.
  target_ids:
  - GO:0097539
  evidence_ids:
  - go
  - go-relations
  - uniprot
  - xrp2-family
  - fbf1-family
  - tfk1-study
  - mapping-study
  - supplement-loci
  - rp2-antibody
  - ncbi-taxa
  - pubmed-identities
  - doi-2022
  - doi-2024
  - doi-2017
  - hal-metadata
- check_id: snippet-verification
  name: Verbatim evidence snippets
  status: not_applicable
  required: false
  summary: The target has no snippet fields; source-backed notes were assessed directly.
  target_ids:
  - GO:0097539
  evidence_ids:
  - record
- check_id: target-identifier-coverage
  name: Target identifier coverage including resolver residuals
  status: passed
  required: true
  target_ids:
  - GO:0097539
  summary: All CURIE-shaped target values have issuing-authority or appropriate local/source-specific
    existence verification. Generic PMID HTTP414 failures and skipped namespaces were
    resolved by scoped receipts; biological mapping correctness is assessed separately.
  evidence_ids:
  - target-resolver-coverage
  - liveness-pmid-35588197
  - liveness-pmid-38572631
  - liveness-hal-03817184-figure3
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097539
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
  - GO:0097539
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
  - GO:0097539
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
  - GO:0097539
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
  - GO:0097539
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
  reference: data/structures/appendage/ciliary_transition_fiber.yaml
  locator: Entire YAML; especially components#tfk1 and discussions#complete_component_inventory_and_grounding
  accessed_at: '2026-10-19T07:37:52Z'
  support: context_only
  summary: Full maintained record read. Four protein examples are present; the TFK1
    row uses Q382L3 although existing grounding/discussion notes identify Q585C9.
    The discussion still says that no strain-specific protein example is asserted.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097539,GO:0140535,GO:0036064,GO:0097537
  locator: 'results: GO:0097539, GO:0140535, GO:0036064, GO:0097537; definitions,
    synonyms and children'
  accessed_at: '2026-10-19T07:33:53Z'
  support: supports
  summary: All terms are current cellular components. Definition and all eleven synonym
    scopes match. GO:0140535 explicitly lists the target as an is_a child; basal body
    and Y-shaped link remain distinct structures.
  snapshot_sha256: 0e455310bdc4dcd7e40fb7f656ecf5fa31fb467772f9c8249150c892a133578c
- evidence_id: go-relations
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097539/ancestors?relations=part_of,is_a
  locator: GO:0097539 ancestors for is_a and part_of
  accessed_at: '2026-10-19T07:35:30Z'
  support: partial
  summary: The intracellular-complex hierarchy is confirmed. The endpoint does not
    expose basal-body parthood for this term; its anatomical placement is supported
    by the primary microscopy studies.
  snapshot_sha256: 7c6dc3bc26906cfe604e767e2a05a8ee92961b708ae502fda3f5ddb3dda18534
- evidence_id: uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=accession%3AQ382L3+OR+accession%3AQ582C1+OR+accession%3AQ388J8+OR+accession%3AQ586A8+OR+accession%3AQ585C9&format=json
  locator: Full JSON entries Q382L3, Q585C9, Q582C1, Q388J8 and Q586A8; accession,
    ORF names, sequence length, taxon, entry status and RefSeq/InterPro crossreferences
  accessed_at: '2026-10-19T07:33:53Z'
  support: refutes
  summary: Q382L3 is Tb11.01.4810, a 216-residue MSP/VAP-family protein; Q585C9 is
    Tb927.6.1180, 1271 residues, linked to XP_845240.1. Q582C1 maps to Tb927.5.2440,
    Q388J8 to Tb10.61.2870 and Q586A8 to Tb927.6.4100. All are unreviewed in taxon
    185431; listed protein labels match.
  snapshot_sha256: 84192f220ad5a9d69f38978fb4a115173af74630eb66e48ae43e8e45d9ac6051
- evidence_id: xrp2-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039093/
  locator: metadata accession, name, type
  accessed_at: '2026-10-19T07:33:53Z'
  support: supports
  summary: IPR039093 is the family Protein XRP2; Q388J8 also carries this InterPro
    crossreference. Family annotation is not treated as direct tubulin-binding evidence.
  snapshot_sha256: 2806334f00b93f3b9551e6b0c08e44c7d16173ffc8f214b6e528275422c0a5dd
- evidence_id: fbf1-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033561/
  locator: metadata accession, name, type
  accessed_at: '2026-10-19T07:33:53Z'
  support: supports
  summary: IPR033561 is the Fas-binding factor 1 family. Its non-trypanosome mechanistic
    annotations do not establish specific reactions in the record organism.
  snapshot_sha256: 45ebe8fe4c467e3ae5c9ac8d5668d35ee92f9759e9d1d35d924b3ea9575ff5e2
- evidence_id: tfk1-grounding
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q585C9/
  locator: Exact Q585C9 integrated-entry query; HTTP 204
  accessed_at: '2026-10-19T07:33:53Z'
  support: supports
  summary: No integrated InterPro entry returned for Q585C9 in this bounded authority
    query; retaining reviewed label-only grounding is justified.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: InterPro entry/interpro/protein/uniprot/Q585C9/ only; HTTP 204, no
    integrated-entry body. Not a claim that all possible family databases lack a match.
- evidence_id: tfk1-search
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=TFK1
  locator: Integrated InterPro search=TFK1; HTTP 204
  accessed_at: '2026-10-19T07:35:30Z'
  support: supports
  summary: The exact TFK1 text search also returned no integrated entry.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: InterPro integrated entries search=TFK1, queried on the recorded access
    date; no inference about other names or future releases.
- evidence_id: cep164-grounding
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=CEP164
  locator: count=2; IPR063650 and IPR064006
  accessed_at: '2026-10-19T07:33:54Z'
  support: supports
  summary: CEP164 search returned coiled-coil and N-terminal domain entries, both
    type domain; these do not justify whole-family grounding.
  snapshot_sha256: 22d51e1b50fa28da5037415d4ad54b5a4d7d4189493f02b44a07411df9b20a2a
- evidence_id: ncbi-taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5691,185431&retmode=xml
  locator: Taxon records 5691 and 185431
  accessed_at: '2026-10-19T07:33:54Z'
  support: supports
  summary: 5691 is Trypanosoma brucei (species); 185431 is Trypanosoma brucei brucei
    TREU927 (strain). Record labels match.
  snapshot_sha256: 1a5bb5bc4ddc1716b55ad564fb9a1ab13788ed12c34a056a6088051924adcd70
- evidence_id: tfk1-study
  kind: primary_source
  reference: https://hal.science/hal-03817184/document
  locator: Accepted manuscript pp.7-14,17-20,24-26; Figures 2,3,5 and S5; Figure 3
    p.50 and Figure 5 p.52 visually inspected
  accessed_at: '2026-10-19T07:34:00Z'
  support: supports
  summary: The paper identifies TFK1 as Tb927.6.1180/XP_845240.1. It supports relative
    localization, bounded RNAi interpretation, full-length and T4 yeast-two-hybrid
    interaction, and T4 targeting with endogenous TFK1 retained. Figure/Methods specify
    T4 residues 75-536; SmOx P427/B427 are experimental backgrounds.
  snapshot_sha256: 956f8fbe8da8944e1ede538900f8d606debb3df1f2ff64c28f51904686271105
- evidence_id: mapping-study
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11190437/fullTextXML
  locator: 'PMC11190437 JATS: Results, Discussion, Materials and Methods; Figure 1H
    image visually inspected; Figure 5D caption/results'
  accessed_at: '2026-10-19T07:33:54Z'
  support: supports
  summary: The study supports distinct CEP164 paralogue timing, FBF1 localization
    and new-flagellum phenotype, and explicitly unresolved docking versus marker-recruitment
    alternatives. Thirty mapped proteins supplement RP2 and TFK1. Methods use SmOxP9
    derived from TREU927.
  snapshot_sha256: b25d9f0e4a60d093b36077a61dbbf73ea721dcac891ff64f031b30a36200fca5
- evidence_id: supplement-loci
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11190437/supplementaryFiles
  locator: joces-137-261692-TableS1.xlsx, sheet1; rows for FBF1, CEP164A, CEP164b
    and CEP164C
  accessed_at: '2026-10-19T07:36:14Z'
  support: supports
  summary: Table S1 pairs FBF1 with Tb927.6.4100 and CEP164A with Tb927.5.2440, independently
    confirming the paper-name to UniProt-locus joins for Q586A8 and Q582C1.
  snapshot_sha256: 4bd0cb747c7c0396dd79a8db587943d28eebf01c519659092b29634c8b64a176
- evidence_id: rp2-antibody
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.protis.2017.07.002&format=json&resultType=core
  locator: Europe PMC MED PMID:28822909 author abstract, DOI:10.1016/j.protis.2017.07.002
  accessed_at: '2026-10-19T07:33:54Z'
  support: supports
  summary: The inspected primary abstract attributes mature-basal-body YL1/2 recognition
    to RP2 rather than tyrosinated alpha-tubulin, supporting the record caution. Full
    article text was not obtained.
  snapshot_sha256: d21c96ff16c46e92b4e111b4d7adfc3a71843aa62d23d1b1c7391be6ad8bc834
- evidence_id: pubmed-identities
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=35588197,38572631&retmode=xml
  locator: PMIDs 35588197 and 38572631; titles, authors, DOI links and abstracts
  accessed_at: '2026-10-19T07:33:53Z'
  support: supports
  summary: Both PMID-to-DOI and article identities match the target bibliography.
  snapshot_sha256: 30b97ea83b8e07ac9e51b51e2ad83273517e26017f1d07cf30c8e057e30ecf13
- evidence_id: doi-2022
  kind: authority
  reference: https://api.crossref.org/works/10.1242/jcs.259893
  locator: Crossref message.DOI, title and authors
  accessed_at: '2026-10-19T07:35:30Z'
  support: supports
  summary: 'DOI resolves to the cited primary article: TFK1, a basal body transition
    fibre protein that is essential for cytokinesis in <i>Trypanosoma brucei</i>'
  snapshot_sha256: 1817942cef19648eca3b30cc7d9aa3343cbf2c4eaca97807db1e74267081c888
- evidence_id: doi-2024
  kind: authority
  reference: https://api.crossref.org/works/10.1242/jcs.261692
  locator: Crossref message.DOI, title and authors
  accessed_at: '2026-10-19T07:35:30Z'
  support: supports
  summary: "DOI resolves to the cited primary article: Identification of 30 transition\
    \ fibre proteins in\n                    <i>Trypanosoma brucei</i>\n         \
    \           reveals a complex and dynamic structure"
  snapshot_sha256: 38325e12ac751644ff31329e699fd262cf40ae9934f0fb6360d8b07dd0b655c1
- evidence_id: doi-2017
  kind: authority
  reference: https://api.crossref.org/works/10.1016/j.protis.2017.07.002
  locator: Crossref message.DOI, title and authors
  accessed_at: '2026-10-19T07:35:30Z'
  support: supports
  summary: 'DOI resolves to the cited primary article: Variation in Basal Body Localisation
    and Targeting of Trypanosome RP2 and FOR20 Proteins'
  snapshot_sha256: f857e8116f2837426656cc0b960683eddd157107f966ebb7ed61bbef35be2f2b
- evidence_id: hal-metadata
  kind: authority
  reference: https://api.archives-ouvertes.fr/search/?q=halId_s%3Ahal-03817184&wt=json&fl=%2A
  locator: 'HAL hal-03817184v1 metadata: DOI, authors, fileMain_s, licence_s'
  accessed_at: '2026-10-19T07:33:55Z'
  support: supports
  summary: The linked deposit matches the 2022 article and author list. Licence metadata
    identifies HAL deposit authorization; the record correctly keeps the image link-only.
  snapshot_sha256: 2344e4e6999b4940926f1f47d4106ff5bf770211e1be4800c9a8ff12fa7b5d60
- evidence_id: hal-authorization
  kind: authority
  reference: https://about.hal.science/hal-authorisation-v1/
  locator: HAL authorization explanatory text
  accessed_at: '2026-10-19T07:33:55Z'
  support: supports
  summary: The authorization permits HAL distribution and retains copyright; it is
    not a Creative Commons figure-reuse licence.
  snapshot_sha256: 7650e28c874f20fb87b1a5e2ae9079556b2598b7b8fff1555db8641314c52fdf
- evidence_id: search-and-history
  kind: search
  reference: repository working tree
  locator: history/records/ciliary_transition_fiber; data/structures; reviews; research;
    curation; git log --all --follow
  accessed_at: '2026-10-19T07:37:52Z'
  support: context_only
  summary: Ignored-inclusive search found the maintained target, two sibling boundary
    mentions, and two record history files; no earlier structured target review was
    found within the searched review tree. Git history identifies creation in 3e10707b46a5109785636c75aa015b7ced7d0a94
    and protein-example update in 00f869634ffe809258200c47a3aa842bbd0bdd24.
  search_scope: rg --no-ignore --hidden -n with GO:0097539, ciliary_transition_fiber,
    ciliary transition fiber and Q382L3 across history reviews data/structures research
    curation in the isolated clone. Ignored/hidden files included; .git and .venv
    excluded. git log --all --follow separately inspected for target path. This is
    bounded identity/provenance search, not a fleet absence assertion.
- evidence_id: schema-checks
  kind: validation
  reference: just validate; just validate-strict
  locator: Target file; strict report /private/tmp/cellstructure-record-reviews-UhRFh7/ciliary-review/strict.tsv
  accessed_at: '2026-10-19T07:37:52Z'
  support: supports
  summary: 'Both target validation commands exited 0. Open validation: No issues found.
    Strict validation: one file scanned, zero files with ERROR, zero ERROR rows.'
- evidence_id: target-resolver-coverage
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/ciliary_transition_fiber.yaml; exact scripts/check_curies.py
    collect() scope; reports/curie_check.tsv
  accessed_at: '2026-10-19T23:32:25.400320Z'
  support: supports
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
  summary: 'This target contains 18 distinct CURIE-shaped scalar values: 15 OK, 2
    transport-unreachable and 1 skipped in the global report. The attached scoped
    receipts resolve each non-OK identifier. HTTP URLs and prose are outside collect();
    their content was inspected separately. Existence is not proof of correct biological
    mapping.'
- evidence_id: liveness-pmid-35588197
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=35588197,38572631&retmode=xml
  locator: PubmedArticle/MedlineCitation/PMID joined only to that article's PubmedData/ArticleIdList
    (not nested cited-reference IDs)
  accessed_at: '2026-10-19T07:33:53Z'
  support: supports
  summary: 'PMID:35588197 resolves through the scoped source inspection. Exact article
    join: pubmed=35588197, doi=10.1242/jcs.259893, pii=275643. Bibliographic identifier
    identity; source-claim sufficiency is assessed separately.'
  snapshot_sha256: 30b97ea83b8e07ac9e51b51e2ad83273517e26017f1d07cf30c8e057e30ecf13
- evidence_id: liveness-pmid-38572631
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=35588197,38572631&retmode=xml
  locator: PubmedArticle/MedlineCitation/PMID joined only to that article's PubmedData/ArticleIdList
    (not nested cited-reference IDs)
  accessed_at: '2026-10-19T07:33:53Z'
  support: supports
  summary: 'PMID:38572631 resolves through the scoped source inspection. Exact article
    join: pubmed=38572631, pmc=PMC11190437, doi=10.1242/jcs.261692, pii=352266. Bibliographic
    identifier identity; source-claim sufficiency is assessed separately.'
  snapshot_sha256: 30b97ea83b8e07ac9e51b51e2ad83273517e26017f1d07cf30c8e057e30ecf13
- evidence_id: liveness-hal-03817184-figure3
  kind: authority
  reference: https://api.archives-ouvertes.fr/search/?q=halId_s%3Ahal-03817184&wt=json&fl=%2A
  locator: TFK1 accepted manuscript, Figure 3, PDF page 50; visual-inspection receipt
    in transition-fiber review
  accessed_at: '2026-10-19T07:33:55Z'
  support: supports
  summary: hal-03817184:figure3 resolves through the scoped source inspection. HAL
    identifier and Figure 3 location verified outside the generic CURIE resolver;
    no image-license conclusion follows from resolution.
  snapshot_sha256: 2344e4e6999b4940926f1f47d4106ff5bf770211e1be4800c9a8ff12fa7b5d60
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
  topic: Structure boundary, ontology identity and synonym scope
  outcome: supported
  summary: The target denotes a discrete appendage complex; neither the enclosing
    basal body nor the adjacent transition-zone Y-link is conflated with it. Definition,
    category, kind, synonyms and is-a placement are supported. Basal-body parthood
    is anatomical rather than an explicit QuickGO ancestor here.
  target_ids:
  - GO:0097539
  evidence_ids:
  - go
  - go-relations
  - tfk1-study
  - mapping-study
- assessment_id: components
  area: grounding
  topic: Component family grounding and protein-example identity
  outcome: concern
  summary: The four component classes have bounded source support and retain unknown
    assembly essentiality. XRP2/FBF1 family terms and TFK1/CEP164 label-only decisions
    are appropriate. The TFK1 accession row denotes a different protein; other accession
    labels, entry statuses and loci are consistent with their source joins.
  target_ids:
  - GO:0097539
  evidence_ids:
  - record
  - uniprot
  - xrp2-family
  - fbf1-family
  - tfk1-grounding
  - tfk1-search
  - cep164-grounding
  - tfk1-study
  - supplement-loci
- assessment_id: taxon
  area: scope
  topic: Species, strain and experimental context
  outcome: supported
  summary: The canonical species and explicitly stated 2022 strain context are correct.
    Examples use TREU927 accessions; the 2024 study supplies that background for CEP164A/FBF1.
    No broad presence/absence or universal stoichiometry claim is made.
  target_ids:
  - GO:0097539
  evidence_ids:
  - ncbi-taxa
  - tfk1-study
  - mapping-study
  - uniprot
  dimensions:
  - name: experimental-strain-2022
    value: SmOx P427 and SmOx B427
    definition: Backgrounds for 2022 localization/domain and bloodstream RNAi experiments.
    evidence_ids:
    - tfk1-study
  - name: experimental-strain-2024
    value: SmOxP9, TREU927-derived
    definition: Background for the 2024 mapping and RNAi experiments.
    evidence_ids:
    - mapping-study
  - name: protein-example-taxon
    value: NCBITaxon:185431, strain
    definition: Genomic accession context; not proof that all experiments used this
      strain.
    evidence_ids:
    - uniprot
    - ncbi-taxa
- assessment_id: functions
  area: evidence
  topic: Anatomical linkage and new-flagellum assembly
  outcome: supported
  summary: Both functions are supported at the declared scope. The record avoids assigning
    direct lipid binding, exact docking steps or specific IFT-entry reactions to individual
    trypanosome proteins.
  target_ids:
  - GO:0097539
  evidence_ids:
  - go
  - mapping-study
- assessment_id: graph
  area: graph
  topic: All three TFK1 targeting and interaction edges
  outcome: supported
  summary: Each edge is supported by the cited assay. The graph separates yeast-two-hybrid
    interaction from targeting and does not infer their causal connection, native
    oligomer stoichiometry or complete fiber construction.
  target_ids:
  - GO:0097539
  evidence_ids:
  - tfk1-study
  dimensions:
  - name: evidence-type
    value: Yeast-two-hybrid and ectopic domain-localization assays
    definition: Experimental scope for the three graph edges.
    evidence_ids:
    - tfk1-study
- assessment_id: image
  area: provenance
  topic: Figure identity, caption, taxon and reuse boundary
  outcome: supported
  summary: The figure is correctly identified, attributed and linked. Visual inspection
    confirms panel orientations and scale bars. Record notes follow the Results description
    of detergent-extracted material while avoiding an intact-membrane inference; the
    caption itself says whole cells. Link-only treatment matches HAL metadata.
  target_ids:
  - GO:0097539
  evidence_ids:
  - tfk1-study
  - hal-metadata
  - hal-authorization
  - ncbi-taxa
- assessment_id: completeness
  area: completeness
  topic: Declared inventory and optional scientific surfaces
  outcome: supported
  summary: The incomplete component inventory and unresolved native assembly/gating
    questions are explicitly disclosed. Unset stoichiometry, distribution, physical
    properties, traits, datasets and complex compositions do not introduce an unsupported
    claim or alone constitute a defect.
  target_ids:
  - GO:0097539
  evidence_ids:
  - record
  - mapping-study
  - tfk1-study
- assessment_id: discussion
  area: consistency
  topic: Discussion scope after protein-example enrichment
  outcome: concern
  summary: The open inventory discussion retains a now-false statement that no strain-specific
    protein example is asserted. Its TFK1 accession caution also exposes the disagreement
    with the newly added TFK1 row. Other discussion distinctions remain supported.
  target_ids:
  - GO:0097539
  evidence_ids:
  - record
  - uniprot
  - rp2-antibody
  - tfk1-study
  - mapping-study
- assessment_id: status
  area: provenance
  topic: Native status, record history and source placement
  outcome: supported
  summary: The record remains PROPOSED, with agent-attributed creation, scope correction
    and protein-example history. Source entries are attached to the relevant claims.
    No native status promotion is implied by this review.
  target_ids:
  - GO:0097539
  evidence_ids:
  - record
  - search-and-history
  - pubmed-identities
  - doi-2022
  - doi-2024
  - doi-2017
- assessment_id: schema
  area: schema
  topic: Open and closed target validation
  outcome: supported
  summary: Both documented target validators pass; scientific accession mismatch is
    not detected by schema validity.
  target_ids:
  - GO:0097539
  evidence_ids:
  - schema-checks
findings:
- finding_id: tfk1-accession
  issue_key: ciliary-transition-fiber-tfk1-protein-example-mismatch
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: TFK1 protein example points to an unrelated MSP-domain protein
  description: components#tfk1 assigns Q382L3/Tb11.01.4810 to TFK1. UniProt identifies
    it as a 216-residue MSP/VAP-family protein, while the cited study names TFK1 as
    Tb927.6.1180/XP_845240.1; Q585C9 matches that locus and 1271-residue sequence.
    Existing grounding and discussion notes already name Q585C9. The incorrect row
    therefore supplies a false accession-to-component identity, even though its UniProt
    entry itself resolves.
  target_ids:
  - GO:0097539
  field_paths:
  - components[component_id=tfk1].protein_examples[uniprot_id=UniProtKB:Q382L3]
  evidence_ids:
  - record
  - uniprot
  - tfk1-study
  rule_id: review-checklist:Components; docs/CURATION.md:Never guess a CURIE
  native_severity: major
  normalization_reason: Wrong protein-example grounding is a major scientific identity
    defect within an otherwise correctly identified structure.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_transition_fiber.yaml
    role: maintained scientific record
- finding_id: stale-example-scope
  issue_key: ciliary-transition-fiber-stale-protein-example-scope
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Inventory discussion still claims that no strain-specific protein examples
    are asserted
  description: The open complete_component_inventory_and_grounding discussion says
    no strain-specific protein example is asserted, but the current components contain
    four taxon-paired TREU927 examples. This stale scope statement obscures what was
    added and which experimental-strain limitation still applies.
  target_ids:
  - GO:0097539
  field_paths:
  - discussions[discussion_id=complete_component_inventory_and_grounding].notes
  evidence_ids:
  - record
  - uniprot
  rule_id: review-checklist:Discussions/datasets; review-checklist:Status/audit
  native_severity: minor
  normalization_reason: Bounded internal provenance contradiction; it does not change
    the structure identity.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_transition_fiber.yaml
    role: maintained scientific record
actions:
- action_id: correct-tfk1-example
  description: Remove or correct the erroneous TFK1 protein-example mapping in the
    maintained YAML through the guarded writer. If Q585C9 is used, preserve the distinction
    between the TREU927 genomic accession and SmOx427 assay backgrounds, and cite
    the locus-to-accession join. Append required curation/history records and regenerate
    pages only during separately authorized curation.
  finding_ids:
  - tfk1-accession
  target_ids:
  - GO:0097539
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_transition_fiber.yaml
    role: maintained scientific record
  acceptance_checks:
  - Resolve the selected accession at UniProt and compare gene locus, RefSeq crossreference
    and sequence length with DOI:10.1242/jcs.259893.
  - Confirm no TFK1 protein example retains Q382L3/Tb11.01.4810; search ignored and
    hidden files for stale maintained references.
  - Run just validate and just validate-strict for the changed target, then the documented
    corpus/provenance gates and generated-site checks.
- action_id: refresh-discussion-scope
  description: Update the inventory discussion to describe the retained protein examples
    and remaining experimental-strain caveat accurately after resolving the TFK1 row.
    Preserve its unresolved inventory, family-grounding and stoichiometry questions.
  finding_ids:
  - stale-example-scope
  target_ids:
  - GO:0097539
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_transition_fiber.yaml
    role: maintained scientific record
  depends_on:
  - correct-tfk1-example
  acceptance_checks:
  - Read the discussion against every current protein_examples row and verify that
    its accession and strain statements agree.
  - Validate the target and required curation history; regenerate and check rendered
    output as part of any authorized curation.
limitations:
- For DOI:10.1016/j.protis.2017.07.002, the primary author abstract supports the sole
  antibody claim. Europe PMC metadata and the publisher DOI landing route were inspected;
  complete article text was not obtained.
- 'This review assesses evidence and source consistency, not experimental replication
  or a complete cross-taxon component inventory. iModulon expression-module analysis
  was not used: no expression-module claim informs this structural record.'
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- User explicitly requested a saved review for every unreviewed target; this review
  also independently meets the local issue-bearing persistence gate.
- Target and native scientific status were not modified. Temporary source downloads
  remain outside the repository.
```
