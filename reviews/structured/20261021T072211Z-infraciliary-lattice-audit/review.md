# Infraciliary lattice identity, constituent scope and calcium-function review

- Review: 20261021T072211Z-infraciliary-lattice-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:16:59Z
- Finished UTC: 2026-10-21T07:22:11Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The extended-lattice identity, constituent classes, scoped assembly dependencies, calcium-response functions and Figure2 provenance are supported. One minor role-wording issue remains: calcium-binding is not uniform across lattice centrin isoforms.

## Scope And Provenance

Entire single target including graph, all discussions/history and tracked Figure2; native identifier sources and relevant primary experimental text, methods, captions and Table1.

Selection: Tenth target in batch seven, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:infraciliary_lattice | data/structures/cytoskeleton/infraciliary_lattice.yaml | maintained | infraciliary lattice |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:infraciliary_lattice | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:infraciliary_lattice | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:infraciliary_lattice | 9 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | cellstructuremech:infraciliary_lattice | This review concerns physical ICL composition, depletion/localization and calcium-response experiments, with no transcriptional regulator or expression-module mechanism asserted. |
| Claim-level scientific review | passed | True | cellstructuremech:infraciliary_lattice | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:infraciliary_lattice | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:infraciliary_lattice | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:infraciliary_lattice | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:infraciliary_lattice | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:infraciliary_lattice | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Extended lattice identity and hierarchy

identity: supported. Targets: cellstructuremech:infraciliary_lattice.

The local record denotes the Paramecium subcortical extended mesh, with broad intracellular parent and proper parthood in cortical cytoskeleton. ICLOC, ICL1e complex, ciliary centrin assemblies and unrelated ontology lattices are not equated with the target.

### Experimentally delimited constituent classes

grounding: supported. Targets: cellstructuremech:infraciliary_lattice.

Reviewed-label-only grounding is justified for these ICL-specific classes: the two inspected InterPro families are broader, and their names alone do not establish an exact constituent mapping. PtCenBP1 remains an exemplar rather than complete scaffold inventory.

### Calcium-binding heterogeneity within ICL centrins

scope: concern. Targets: cellstructuremech:infraciliary_lattice.

The role wording describes the collective centrin component as calcium-binding without distinguishing nonbinding isoforms. Table1 and Results identify ICL1e/ICL7/ICL8 lacking predicted functional binding sites and cite measured nonbinding for ICL7/ICL8. This warrants a narrow wording correction, not removal of the component.

### Class requirements for mesh assembly

graph: supported. Targets: cellstructuremech:infraciliary_lattice.

Depletion, loss of lattice and recovery support component-class assembly dependencies. The graph excludes detailed assembly order, stoichiometry, shortening and basal-body anchoring. RNAi co-silencing and exceptions bar a claim that every centrin homologue is individually essential; the record expressly avoids that claim.

### Contractility and post-stimulation calcium recovery

evidence: supported. Targets: cellstructuremech:infraciliary_lattice.

The 2007 AED/RNAi assay supports calcium-dependent lattice contraction separately from normal swimming. The 2009 imaging supports delayed post-stimulation calcium decay in ICL-less cells and the authors buffering interpretation. The record appropriately avoids quantitative kinetics and a resolved molecular contraction mechanism; unchanged initial generation is limited to the measured comparison.

### Species and strain boundaries

scope: supported. Targets: cellstructuremech:infraciliary_lattice.

The verified canonical taxon is P. tetraurelia, with d4-2 and documented mutant backgrounds. Neither shared centrin families nor neighboring assemblies establish universal ciliate distribution; no broader prevalence or guessed strain ID is asserted.

### Figure identity, media integrity and exact license

provenance: supported. Targets: cellstructuremech:infraciliary_lattice.

The tracked Figure2 matches the freshly retrieved media byte-for-byte and the native MD5. Confocal panels, retained versus extended structures, GFP-Cen15 label, colors and scale bars agree. JATS establishes CC BY3.0 and the copyright/publisher distinction retained in attribution.

### Historical readability and current evidence

provenance: supported. Targets: cellstructuremech:infraciliary_lattice.

The record describes its earlier abstract-only access to the 2008/2009 studies. Newly successful author-deposited text and PDF access does not make those historical notes false. Current review separates browser-rendered primary passages, native JATS, the public PDF and failed HTTP/challenge routes.

### Bounded representation and unresolved details

completeness: supported. Targets: cellstructuremech:infraciliary_lattice.

Both major constituent classes, a canonical species, supported calcium functions, assembly dependencies and a verified image are represented. Unresolved exact family mapping, broader taxonomic distribution and detailed mechanisms are retained as bounded uncertainty. No empty optional inventory or unavailable copy number is promoted to a finding.

## Findings

### F1: Centrin role wording omits non-calcium-binding lattice isoforms

minor / open / confirmed; issue key: infraciliary-lattice-centrin-calcium-binding-heterogeneity.

The collective ICL-centrin role starts with Calcium-binding centrin-family constituents, which implies a uniform binding property. The 2008 Results/Table1 identify ICL1e, ICL7 and ICL8 as lacking predicted functional calcium-binding sites; Table1 separately reports prior experimental nonbinding for ICL7 and ICL8. Qualify the role to accommodate calcium-binding and nonbinding members while preserving the source-backed calcium-responsive network identity and class-level assembly requirement.

## Recommended Actions And Acceptance Checks

### A1

In a future curation change, describe ICL centrins as constituents including calcium-binding and nonbinding isoforms. Preserve the distinction between predicted absent sites for ICL1e/ICL7/ICL8 and measured nonbinding reported for ICL7/ICL8, and retain class-level assembly essentiality.

- Check the revised role against the 2008 Results/Table1 and preserve predicted versus measured scope.
- Do not remove the calcium-responsive network definition or infer individual essentiality of every homologue.
- Run native schema, strict, label, history and generated-page checks after maintained-record curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| infraciliary-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0030863,GO:0140095,GO:0140419,GO:0140366; Results for GO:0005622, GO:0030863, GO:0140095, GO:0140419 and GO:0140366; names, definitions and obsolete flags | supports | Native QuickGO verifies active GO:0005622 intracellular anatomical structure and GO:0030863 cortical cytoskeleton. The three inspected GO lattice alternatives concern galectin or mammalian oocytes and do not denote the Paramecium infraciliary lattice. No native GO edge for the local identifier is asserted. |
| infraciliary-agent-go-search-infraciliary | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=infraciliary&amp;limit=100; QuickGO search query=infraciliary, limit=100; results and numberOfHits | context_only | Exact infraciliary search returns zero results in this bounded native query. |
| infraciliary-agent-go-search-lattice | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=infraciliary%20lattice&amp;limit=100; QuickGO search query=infraciliary lattice, limit=100; all returned definitions | context_only | The bounded infraciliary lattice query returns four nonmatching terms: galectin lattice, mammalian cytoplasmic lattice/complex and a molecular-function constituent term. It does not establish ontology-wide absence. |
| infraciliary-agent-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5888; ENA taxonId, scientificName and rank | supports | NCBITaxon:5888 denotes Paramecium tetraurelia at species rank. d4-2 remains a documented experimental strain, without a guessed strain identifier. |
| infraciliary-agent-family-centrin | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050145/; InterPro metadata accession, type, name, hierarchy and description; description marked LLM-assisted/reviewed | supports | IPR050145 is family Centrin/CML-like and explicitly includes obelin and plant CML proteins, so it is broader than the experimentally delimited ICL constituent class. The original reused retrieval timestamp is preserved. |
| infraciliary-agent-family-scaffold | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052270/; InterPro metadata accession, type, name and description | supports | IPR052270 is family Centrin-binding protein SFI1-like and includes SFI1 and CCDC191; this authority record does not establish exact coverage of Paramecium ICL scaffold subfamilies. |
| infraciliary-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1242/bio.024273%20OR%20DOI:10.1128/EC.00197-07%20OR%20DOI:10.1242/jcs.019414%20OR%20DOI:10.1016/j.ceca.2008.06.004&amp;format=json&amp;resultType=core; Four matching Europe PMC core records: bibliographic fields and abstractText | supports | The four DOI/title/author identities and primary abstracts match the cited studies: 2017 PMID28432105/PMC5483020; 2007 PMID17675401/PMC2168399; 2008 PMID18057024; 2009 PMID18653233. Metadata verifies identity separately from experimental support. |
| infraciliary-agent-jats2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5483020.1/PMC5483020.1.xml; PMC5483020.1 JATS: Introduction s1; Results s2b/s2d; Discussion s3a; Methods s4a/s4e/s4f/s4g; figures BIO024273F2/F4; permissions | supports | The extended subcortical centrin/Sfi1 mesh is distinct from ICLOC and the separate basal-body ICL1e complex. ICL1e depletion strips the WT lattice; fully developed unanchored basal bodies support an anchoring rather than duplication-per-se defect. 1A9 excludes ICL1e. Methods identify d4-2 and mutant backgrounds. Figure2 is confocal; permissions state CC BY 3.0 without assigning a separate copyright holder. |
| infraciliary-agent-meta2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5483020.1/PMC5483020.1.json; PMC5483020.1 native metadata: identifiers, version, license_code, is_retracted, xml_url and media_urls | supports | Native PMC version1 metadata matches the DOI/title, marks the article open access and not retracted, gives CC BY and provides Figure2 media MD5 7650e2fa9ca316b23e0408de743acfc1. Exact license version is established by JATS. |
| infraciliary-agent-image2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5483020.1/biolopen-6-024273-g2.jpg; Unmodified biolopen-6-024273-g2.jpg; all six panels and scale bars; compared with tracked data/images/cytoskeleton/infraciliary_lattice/pmc5483020_bio024273f2.jpg | supports | Entire Figure2 was visually inspected and is byte-identical to the tracked image and stated SHA-256; its MD5 matches native media metadata. A/A1/A2 show intact WT lattice and B/B1/B2 the BP residual structures. Actual panels label GFP-Cen15, legend generically GFP-ICL1e. Colors, arrows and 20/1 micrometre bars agree with the record. |
| infraciliary-agent-paper2007-browser | https://www.researchgate.net/publication/6164793_An_Sfi1p-Like_Centrin-Binding_Protein_Mediates_Centrin-Based_Ca2-Dependent_Contractility_in_Paramecium_tetraurelia; Printed p1993, Materials and Methods: Strains and culture conditions, In vivo contractility assay, Gene silencing by feeding; browser source lines410–502 | supports | Public author-deposited primary article text, rendered by web.run and saved as a JSON string; this is not publisher HTML and the tool exposes no HTTP status. Methods specify d4-2, dem1 and Delta-PtCenBP1, the AED-induced calcium-influx contraction assay and feeding RNAi. This establishes experimental context for contractility. |
| infraciliary-agent-paper2007-results-browser | https://www.researchgate.net/publication/6164793_An_Sfi1p-Like_Centrin-Binding_Protein_Mediates_Centrin-Based_Ca2-Dependent_Contractility_in_Paramecium_tetraurelia; Printed pp1995–1997, Functional analysis of PtCenBP1p: RNAi experiments and In vivo localization of GFP-PtCenBP1p; Figures5–7; browser lines821–1025 and following localization text | supports | Public author-deposited primary article passages rendered by web.run, not publisher HTML; no HTTP status supplied. PtCenBP1 RNAi causes loss of AED-induced contraction with normal swimming/growth, then lattice disassembly. Recovery permits reassembly from residual ICLOCs. GFP-fragment localization supports membership; neither molecular shortening nor complete scaffold inventory follows. |
| infraciliary-agent-paper2008-browser | https://www.researchgate.net/publication/5791225_Functional_diversification_of_centrins_and_cell_morphological_complexity; Printed pp66–70: major-constituents Results; scaffold Results and Figure1; Table1 and calcium-binding discussion pp67–68; centrin RNAi Results. Browser lines412–602,639–754,820–1038 | partial | Public author-deposited primary article text/Table1 rendered by web.run and saved as a JSON string, not raw publisher HTML; no HTTP status exposed. Results distinguish PtCenBP1 from PtCenBP2/3 and ten centrin subfamilies. ICL1e/ICL7/ICL8 lack predicted functional calcium-binding sites; Table1 reports previous measured nonbinding for ICL7/8. Subfamily co-silencing assumptions and an ICL8a no-observed-effect exception prevent universal per-isoform necessity claims. |
| infraciliary-agent-paper2008-methods-browser | https://www.researchgate.net/publication/5791225_Functional_diversification_of_centrins_and_cell_morphological_complexity; Printed p72, Materials and Methods: Strains and culture conditions; RNAi by feeding; GFP constructs; browser lines1460–1597 | supports | Public author-deposited Methods rendered by web.run, not publisher raw HTML. d4-2 was used for feeding and nd7-1 for GFP experiments; constructs target centrin coding sequences and a PtCenBP3 fragment. Native gene counts in this study are not copy numbers per lattice. |
| infraciliary-agent-paper2009-pdf | https://citeseerx.ist.psu.edu/document?doi=cfbd04fb65135d0652c79f5dd135e6c4be291c8f&amp;repid=rep1&amp;type=pdf; Printed pp90–91 Methods; pp92–94 Results, Ca2+ transients in the cell periphery, Figures3–5/Table1; pp95–96 Discussion/Conclusions. Text extracted and read; figure pixels not inspected. | supports | Readable public PDF supports the d4-2 versus Delta-PtCenBP1 qualitative decay comparison, with nd7-1 controls and Fura Red ratio imaging. Signal decay is slower without the lattice and authors interpret this as lost buffering. Comparable initial measured rise/amplitude does not establish identical rapid generation kinetics: filter cycling limits time resolution and peak fluorochrome saturation limits inference. |
| infraciliary-agent-paper2007 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2168399/; Preserved response body and metadata for unsuccessful direct route | unknown | HTTP200 response is a reCAPTCHA challenge, not article text. Later public author-deposited text supplied the inspected body. |
| infraciliary-agent-paper2008-publisher | https://doi.org/10.1242/jcs.019414; Preserved response body and metadata for unsuccessful direct route | unknown | HTTP403 publisher retrieval did not supply readable article text. Later public author-deposited text supplied inspected Results/Table1/Methods. |
| infraciliary-agent-paper2009-publisher | https://www.sciencedirect.com/science/article/abs/pii/S0143416008001097; Preserved response body and metadata for unsuccessful direct route | unknown | HTTP403 publisher retrieval failed; the separate public PDF subsequently supplied the inspected body. |
| record | data/structures/cytoskeleton/infraciliary_lattice.yaml; Entire YAML, all fields and local identifier | context_only | The complete maintained record was read. The local identifier self-resolves to this tracked YAML; broad ontology parents, scoped class dependencies, one species example and historical access notes are explicit. |
| policy | .claude/skills/review-yaml-record/SKILL.md; Evidence Rules and workflow severity rubric | context_only | Claim scope must match inspected source evidence. Weak, bounded wording is minor when identity, class membership and main biological functions remain supported. |
| schema-result | just validate data/structures/cytoskeleton/infraciliary_lattice.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/infraciliary_lattice.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/infraciliary_lattice.yaml --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/infraciliary_lattice-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/infraciliary_lattice.yaml --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/infraciliary_lattice-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch7-20261021-dz9x5cv0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/infraciliary_lattice-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/infraciliary_lattice.yaml; exact collect() scope; snapshot_sha256 hashes the full original reports/curie_check.tsv, while lattice/resolver-slice.json preserves the target-only extracted rows | supports | 9 of10 collected target identifiers returned OK at the unchanged base. Residuals: cellstructuremech:infraciliary_lattice: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The native 2017 JATS body was available; listed relevant sections and captions were read, and all Figure2 pixels were visually inspected. Supplementary experimental data were not audited.
- The 2007/2008 evidence includes public author-deposited primary article passages rendered by web.run. Snapshot hashes identify saved JSON-encoded tool text, not raw publisher HTML; the tool exposes no HTTP status.
- The 2009 public PDF was readable and relevant Methods/Results/Discussion, caption and table text were inspected. Figure panels were not visually interpreted; filter-cycle timing and peak fluorochrome saturation limit initial-signal claims.
- InterPro entry inspection establishes broader family scope, not an exhaustive search for every possible exact ICL constituent-family mapping. QuickGO negative results are limited to the two recorded queries.
- One local identifier was SKIPPED by the shared resolver and independently matched to its tracked record; this is not a resolved external authority accession.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- All scientific repository inputs are the entire target and tracked Figure2, both included in the native inspection digest.
- Native schema and strict checks passed before this assessment; shared full-corpus gate reuse is added by the parent reviewer before finalization.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072211Z-infraciliary-lattice-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Infraciliary lattice identity, constituent scope and calcium-function review
started_at: '2026-10-21T07:16:59Z'
finished_at: '2026-10-21T07:22:11Z'
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
summary: 'The extended-lattice identity, constituent classes, scoped assembly dependencies,
  calcium-response functions and Figure2 provenance are supported. One minor role-wording
  issue remains: calcium-binding is not uniform across lattice centrin isoforms.'
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
  - path: data/images/cytoskeleton/infraciliary_lattice/pmc5483020_bio024273f2.jpg
    sha256: c5d90f9f49f6d7e5039205c08adda9620a37aa7da5085986f9ea73436fb7b60a
    role: context
  - path: data/structures/cytoskeleton/infraciliary_lattice.yaml
    sha256: 4c0d123ba0fcc1f65ea9ccf7d139013039bf1db51f987dec87b6df5286e5c00e
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
- target_id: cellstructuremech:infraciliary_lattice
  path: data/structures/cytoskeleton/infraciliary_lattice.yaml
  label: infraciliary lattice
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/infraciliary_lattice.yaml
    role: maintained scientific record
scope:
  description: Entire single target including graph, all discussions/history and tracked
    Figure2; native identifier sources and relevant primary experimental text, methods,
    captions and Table1.
  selection: Tenth target in batch seven, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:infraciliary_lattice
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:infraciliary_lattice
  command: just validate data/structures/cytoskeleton/infraciliary_lattice.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:infraciliary_lattice
  command: just validate-strict data/structures/cytoskeleton/infraciliary_lattice.yaml
    --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/infraciliary_lattice-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: 9 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - record
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: This review concerns physical ICL composition, depletion/localization and
    calcium-response experiments, with no transcriptional regulator or expression-module
    mechanism asserted.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - infraciliary-agent-go
  - infraciliary-agent-go-search-infraciliary
  - infraciliary-agent-go-search-lattice
  - infraciliary-agent-taxon
  - infraciliary-agent-family-centrin
  - infraciliary-agent-family-scaffold
  - infraciliary-agent-epmc
  - infraciliary-agent-jats2017
  - infraciliary-agent-meta2017
  - infraciliary-agent-image2017
  - infraciliary-agent-paper2007-browser
  - infraciliary-agent-paper2007-results-browser
  - infraciliary-agent-paper2008-browser
  - infraciliary-agent-paper2008-methods-browser
  - infraciliary-agent-paper2009-pdf
  - infraciliary-agent-paper2007
  - infraciliary-agent-paper2008-publisher
  - infraciliary-agent-paper2009-publisher
  - record
  - policy
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:infraciliary_lattice
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:infraciliary_lattice
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:infraciliary_lattice
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:infraciliary_lattice
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:infraciliary_lattice
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: infraciliary-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0030863,GO:0140095,GO:0140419,GO:0140366
  locator: Results for GO:0005622, GO:0030863, GO:0140095, GO:0140419 and GO:0140366;
    names, definitions and obsolete flags
  accessed_at: '2026-10-21T07:14:04.788092Z'
  support: supports
  summary: Native QuickGO verifies active GO:0005622 intracellular anatomical structure
    and GO:0030863 cortical cytoskeleton. The three inspected GO lattice alternatives
    concern galectin or mammalian oocytes and do not denote the Paramecium infraciliary
    lattice. No native GO edge for the local identifier is asserted.
  snapshot_sha256: 7f7cd7ea9fc7c79e5170e4d2cb7d803e4cf54a29bd2c7272a0b3a97855e40aa0
- evidence_id: infraciliary-agent-go-search-infraciliary
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=infraciliary&limit=100
  locator: QuickGO search query=infraciliary, limit=100; results and numberOfHits
  accessed_at: '2026-10-21T07:14:04.795532Z'
  support: context_only
  summary: Exact infraciliary search returns zero results in this bounded native query.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: Only the recorded QuickGO remote lexical query at https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=infraciliary&limit=100;
    limit=100, all returned hits inspected. No broader ontology search or local-file
    absence is inferred; ignored-file inclusion is not applicable to this remote authority
    query.
- evidence_id: infraciliary-agent-go-search-lattice
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=infraciliary%20lattice&limit=100
  locator: QuickGO search query=infraciliary lattice, limit=100; all returned definitions
  accessed_at: '2026-10-21T07:14:04.805253Z'
  support: context_only
  summary: 'The bounded infraciliary lattice query returns four nonmatching terms:
    galectin lattice, mammalian cytoplasmic lattice/complex and a molecular-function
    constituent term. It does not establish ontology-wide absence.'
  snapshot_sha256: 744b45d834f5493867d263cc253a5a104a175879c1b560894c71a2dc92b2e78f
  search_scope: Only the recorded QuickGO remote lexical query at https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=infraciliary%20lattice&limit=100;
    limit=100, all returned hits inspected. No broader ontology search or local-file
    absence is inferred; ignored-file inclusion is not applicable to this remote authority
    query.
- evidence_id: infraciliary-agent-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5888
  locator: ENA taxonId, scientificName and rank
  accessed_at: '2026-10-21T07:14:04.796705Z'
  support: supports
  summary: NCBITaxon:5888 denotes Paramecium tetraurelia at species rank. d4-2 remains
    a documented experimental strain, without a guessed strain identifier.
  snapshot_sha256: f61b6efb81712a2238027b99b8ffb913a14a76f878a47c93caa996b6217b52d2
- evidence_id: infraciliary-agent-family-centrin
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050145/
  locator: InterPro metadata accession, type, name, hierarchy and description; description
    marked LLM-assisted/reviewed
  accessed_at: '2026-10-21T06:54:21.523807Z'
  support: supports
  summary: IPR050145 is family Centrin/CML-like and explicitly includes obelin and
    plant CML proteins, so it is broader than the experimentally delimited ICL constituent
    class. The original reused retrieval timestamp is preserved.
  snapshot_sha256: 386371fb67a7de41d9f9a6ded2bbb77530d9a27411b46349d2ac050d45832910
- evidence_id: infraciliary-agent-family-scaffold
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052270/
  locator: InterPro metadata accession, type, name and description
  accessed_at: '2026-10-21T07:14:04.815469Z'
  support: supports
  summary: IPR052270 is family Centrin-binding protein SFI1-like and includes SFI1
    and CCDC191; this authority record does not establish exact coverage of Paramecium
    ICL scaffold subfamilies.
  snapshot_sha256: 1b31c05d82a1ef155a91ee9b419e70a5e28f9414358e858d34f79e55ea5b54bb
- evidence_id: infraciliary-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1242/bio.024273%20OR%20DOI:10.1128/EC.00197-07%20OR%20DOI:10.1242/jcs.019414%20OR%20DOI:10.1016/j.ceca.2008.06.004&format=json&resultType=core
  locator: 'Four matching Europe PMC core records: bibliographic fields and abstractText'
  accessed_at: '2026-10-21T07:14:17.155127Z'
  support: supports
  summary: 'The four DOI/title/author identities and primary abstracts match the cited
    studies: 2017 PMID28432105/PMC5483020; 2007 PMID17675401/PMC2168399; 2008 PMID18057024;
    2009 PMID18653233. Metadata verifies identity separately from experimental support.'
  snapshot_sha256: 8500aac0d17f530a412c32837122b93544002ca31ef6e98a056c8587b6f1d79f
- evidence_id: infraciliary-agent-jats2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5483020.1/PMC5483020.1.xml
  locator: 'PMC5483020.1 JATS: Introduction s1; Results s2b/s2d; Discussion s3a; Methods
    s4a/s4e/s4f/s4g; figures BIO024273F2/F4; permissions'
  accessed_at: '2026-10-21T07:14:05.326257Z'
  support: supports
  summary: The extended subcortical centrin/Sfi1 mesh is distinct from ICLOC and the
    separate basal-body ICL1e complex. ICL1e depletion strips the WT lattice; fully
    developed unanchored basal bodies support an anchoring rather than duplication-per-se
    defect. 1A9 excludes ICL1e. Methods identify d4-2 and mutant backgrounds. Figure2
    is confocal; permissions state CC BY 3.0 without assigning a separate copyright
    holder.
  snapshot_sha256: 54758ab66e922d852a9af9c4d632496ff76629fc38c5f6879017512dcf4c60d6
- evidence_id: infraciliary-agent-meta2017
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5483020.1/PMC5483020.1.json
  locator: 'PMC5483020.1 native metadata: identifiers, version, license_code, is_retracted,
    xml_url and media_urls'
  accessed_at: '2026-10-21T07:14:05.131357Z'
  support: supports
  summary: Native PMC version1 metadata matches the DOI/title, marks the article open
    access and not retracted, gives CC BY and provides Figure2 media MD5 7650e2fa9ca316b23e0408de743acfc1.
    Exact license version is established by JATS.
  snapshot_sha256: 7ef6803d0fa254e0c5db267bfcde77a9035df3ecdec525fb99d0bf2cae1ee483
- evidence_id: infraciliary-agent-image2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5483020.1/biolopen-6-024273-g2.jpg
  locator: Unmodified biolopen-6-024273-g2.jpg; all six panels and scale bars; compared
    with tracked data/images/cytoskeleton/infraciliary_lattice/pmc5483020_bio024273f2.jpg
  accessed_at: '2026-10-21T07:14:05.408382Z'
  support: supports
  summary: Entire Figure2 was visually inspected and is byte-identical to the tracked
    image and stated SHA-256; its MD5 matches native media metadata. A/A1/A2 show
    intact WT lattice and B/B1/B2 the BP residual structures. Actual panels label
    GFP-Cen15, legend generically GFP-ICL1e. Colors, arrows and 20/1 micrometre bars
    agree with the record.
  snapshot_sha256: c5d90f9f49f6d7e5039205c08adda9620a37aa7da5085986f9ea73436fb7b60a
- evidence_id: infraciliary-agent-paper2007-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/6164793_An_Sfi1p-Like_Centrin-Binding_Protein_Mediates_Centrin-Based_Ca2-Dependent_Contractility_in_Paramecium_tetraurelia
  locator: 'Printed p1993, Materials and Methods: Strains and culture conditions,
    In vivo contractility assay, Gene silencing by feeding; browser source lines410–502'
  accessed_at: '2026-10-21T07:17:28.839Z'
  support: supports
  summary: Public author-deposited primary article text, rendered by web.run and saved
    as a JSON string; this is not publisher HTML and the tool exposes no HTTP status.
    Methods specify d4-2, dem1 and Delta-PtCenBP1, the AED-induced calcium-influx
    contraction assay and feeding RNAi. This establishes experimental context for
    contractility.
  snapshot_sha256: f0e8de1e04d02a1cbf05333078be90317b06957c5e5caf9a1fbeb1f6a31bb3a9
- evidence_id: infraciliary-agent-paper2007-results-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/6164793_An_Sfi1p-Like_Centrin-Binding_Protein_Mediates_Centrin-Based_Ca2-Dependent_Contractility_in_Paramecium_tetraurelia
  locator: 'Printed pp1995–1997, Functional analysis of PtCenBP1p: RNAi experiments
    and In vivo localization of GFP-PtCenBP1p; Figures5–7; browser lines821–1025 and
    following localization text'
  accessed_at: '2026-10-21T07:17:30.176Z'
  support: supports
  summary: Public author-deposited primary article passages rendered by web.run, not
    publisher HTML; no HTTP status supplied. PtCenBP1 RNAi causes loss of AED-induced
    contraction with normal swimming/growth, then lattice disassembly. Recovery permits
    reassembly from residual ICLOCs. GFP-fragment localization supports membership;
    neither molecular shortening nor complete scaffold inventory follows.
  snapshot_sha256: d04a7bec914b4838378dcc3ddcebfb2b30f38f2ed06ec1ad2ee702dc627ed986
- evidence_id: infraciliary-agent-paper2008-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/5791225_Functional_diversification_of_centrins_and_cell_morphological_complexity
  locator: 'Printed pp66–70: major-constituents Results; scaffold Results and Figure1;
    Table1 and calcium-binding discussion pp67–68; centrin RNAi Results. Browser lines412–602,639–754,820–1038'
  accessed_at: '2026-10-21T07:17:31.430Z'
  support: partial
  summary: Public author-deposited primary article text/Table1 rendered by web.run
    and saved as a JSON string, not raw publisher HTML; no HTTP status exposed. Results
    distinguish PtCenBP1 from PtCenBP2/3 and ten centrin subfamilies. ICL1e/ICL7/ICL8
    lack predicted functional calcium-binding sites; Table1 reports previous measured
    nonbinding for ICL7/8. Subfamily co-silencing assumptions and an ICL8a no-observed-effect
    exception prevent universal per-isoform necessity claims.
  snapshot_sha256: 4d7dea9886dd92a7f9d4af88ca8c5c21aa600e632975ed4066327a5ee04c8f82
- evidence_id: infraciliary-agent-paper2008-methods-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/5791225_Functional_diversification_of_centrins_and_cell_morphological_complexity
  locator: 'Printed p72, Materials and Methods: Strains and culture conditions; RNAi
    by feeding; GFP constructs; browser lines1460–1597'
  accessed_at: '2026-10-21T07:17:34.232Z'
  support: supports
  summary: Public author-deposited Methods rendered by web.run, not publisher raw
    HTML. d4-2 was used for feeding and nd7-1 for GFP experiments; constructs target
    centrin coding sequences and a PtCenBP3 fragment. Native gene counts in this study
    are not copy numbers per lattice.
  snapshot_sha256: 28d7d37307a4fbe2867b3ea3e3bdd72689dafd6ec170af1e5006b7da69f6a643
- evidence_id: infraciliary-agent-paper2009-pdf
  kind: primary_source
  reference: https://citeseerx.ist.psu.edu/document?doi=cfbd04fb65135d0652c79f5dd135e6c4be291c8f&repid=rep1&type=pdf
  locator: Printed pp90–91 Methods; pp92–94 Results, Ca2+ transients in the cell periphery,
    Figures3–5/Table1; pp95–96 Discussion/Conclusions. Text extracted and read; figure
    pixels not inspected.
  accessed_at: '2026-10-21T07:14:39.106765Z'
  support: supports
  summary: 'Readable public PDF supports the d4-2 versus Delta-PtCenBP1 qualitative
    decay comparison, with nd7-1 controls and Fura Red ratio imaging. Signal decay
    is slower without the lattice and authors interpret this as lost buffering. Comparable
    initial measured rise/amplitude does not establish identical rapid generation
    kinetics: filter cycling limits time resolution and peak fluorochrome saturation
    limits inference.'
  snapshot_sha256: 4e52a56c0528db9b6ff3ebf6e34b838cd4e63c7d6617c1a7bc6103104d2ece81
- evidence_id: infraciliary-agent-paper2007
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2168399/
  locator: Preserved response body and metadata for unsuccessful direct route
  accessed_at: '2026-10-21T07:14:38.045593Z'
  support: unknown
  summary: HTTP200 response is a reCAPTCHA challenge, not article text. Later public
    author-deposited text supplied the inspected body.
  snapshot_sha256: 0c9f25f3d036c8707adb62a74df42f397192635e1622332fba9233d9e3f87038
- evidence_id: infraciliary-agent-paper2008-publisher
  kind: primary_source
  reference: https://doi.org/10.1242/jcs.019414
  locator: Preserved response body and metadata for unsuccessful direct route
  accessed_at: '2026-10-21T07:14:38.080523Z'
  support: unknown
  summary: HTTP403 publisher retrieval did not supply readable article text. Later
    public author-deposited text supplied inspected Results/Table1/Methods.
  snapshot_sha256: 8ba7db6b1287fde7484171aee7030eb26e04cab5989087a26dabd67779ac135b
- evidence_id: infraciliary-agent-paper2009-publisher
  kind: primary_source
  reference: https://www.sciencedirect.com/science/article/abs/pii/S0143416008001097
  locator: Preserved response body and metadata for unsuccessful direct route
  accessed_at: '2026-10-21T07:14:37.953062Z'
  support: unknown
  summary: HTTP403 publisher retrieval failed; the separate public PDF subsequently
    supplied the inspected body.
  snapshot_sha256: 639d0b185977370f2166a750df7a057d419f2900b014af72b73317f8521c14c5
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/infraciliary_lattice.yaml
  locator: Entire YAML, all fields and local identifier
  accessed_at: '2026-10-21T07:20:46Z'
  support: context_only
  summary: The complete maintained record was read. The local identifier self-resolves
    to this tracked YAML; broad ontology parents, scoped class dependencies, one species
    example and historical access notes are explicit.
- evidence_id: policy
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules and workflow severity rubric
  accessed_at: '2026-10-21T07:20:46Z'
  support: context_only
  summary: Claim scope must match inspected source evidence. Weak, bounded wording
    is minor when identity, class membership and main biological functions remain
    supported.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/infraciliary_lattice.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:17:09Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/infraciliary_lattice.yaml'
  snapshot_sha256: 888e336f72ac586eb78eb76627282ef9ae39fa340d597eba72c1d67e93e151b3
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/infraciliary_lattice.yaml
    --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/infraciliary_lattice-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:17:20Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/infraciliary_lattice.yaml\
    \ --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/infraciliary_lattice-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch7-20261021-dz9x5cv0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/infraciliary_lattice-strict.tsv"
  snapshot_sha256: 3f5a1c841d44c1dee623975a08f8c88ae9036b3c4156b4ced95ebbf3df17914f
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/infraciliary_lattice.yaml; exact collect()
    scope; snapshot_sha256 hashes the full original reports/curie_check.tsv, while
    lattice/resolver-slice.json preserves the target-only extracted rows
  accessed_at: '2026-10-21T07:20:46Z'
  support: supports
  summary: '9 of10 collected target identifiers returned OK at the unchanged base.
    Residuals: cellstructuremech:infraciliary_lattice: SKIPPED; resolved by evidence
    record. Source-native identity checked separately.'
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
  topic: Extended lattice identity and hierarchy
  outcome: supported
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: The local record denotes the Paramecium subcortical extended mesh, with
    broad intracellular parent and proper parthood in cortical cytoskeleton. ICLOC,
    ICL1e complex, ciliary centrin assemblies and unrelated ontology lattices are
    not equated with the target.
  evidence_ids:
  - infraciliary-agent-go
  - infraciliary-agent-go-search-infraciliary
  - infraciliary-agent-go-search-lattice
  - infraciliary-agent-jats2017
  - record
- assessment_id: grounding
  area: grounding
  topic: Experimentally delimited constituent classes
  outcome: supported
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: 'Reviewed-label-only grounding is justified for these ICL-specific classes:
    the two inspected InterPro families are broader, and their names alone do not
    establish an exact constituent mapping. PtCenBP1 remains an exemplar rather than
    complete scaffold inventory.'
  evidence_ids:
  - infraciliary-agent-family-centrin
  - infraciliary-agent-family-scaffold
  - infraciliary-agent-paper2007-results-browser
  - infraciliary-agent-paper2008-browser
  - record
- assessment_id: constituent-wording
  area: scope
  topic: Calcium-binding heterogeneity within ICL centrins
  outcome: concern
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: The role wording describes the collective centrin component as calcium-binding
    without distinguishing nonbinding isoforms. Table1 and Results identify ICL1e/ICL7/ICL8
    lacking predicted functional binding sites and cite measured nonbinding for ICL7/ICL8.
    This warrants a narrow wording correction, not removal of the component.
  evidence_ids:
  - infraciliary-agent-paper2008-browser
  - record
  - policy
- assessment_id: assembly
  area: graph
  topic: Class requirements for mesh assembly
  outcome: supported
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: Depletion, loss of lattice and recovery support component-class assembly
    dependencies. The graph excludes detailed assembly order, stoichiometry, shortening
    and basal-body anchoring. RNAi co-silencing and exceptions bar a claim that every
    centrin homologue is individually essential; the record expressly avoids that
    claim.
  evidence_ids:
  - infraciliary-agent-jats2017
  - infraciliary-agent-paper2007-results-browser
  - infraciliary-agent-paper2008-browser
  - infraciliary-agent-paper2008-methods-browser
  - record
- assessment_id: functions
  area: evidence
  topic: Contractility and post-stimulation calcium recovery
  outcome: supported
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: The 2007 AED/RNAi assay supports calcium-dependent lattice contraction
    separately from normal swimming. The 2009 imaging supports delayed post-stimulation
    calcium decay in ICL-less cells and the authors buffering interpretation. The
    record appropriately avoids quantitative kinetics and a resolved molecular contraction
    mechanism; unchanged initial generation is limited to the measured comparison.
  evidence_ids:
  - infraciliary-agent-paper2007-browser
  - infraciliary-agent-paper2007-results-browser
  - infraciliary-agent-paper2009-pdf
  - record
- assessment_id: taxon
  area: scope
  topic: Species and strain boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: The verified canonical taxon is P. tetraurelia, with d4-2 and documented
    mutant backgrounds. Neither shared centrin families nor neighboring assemblies
    establish universal ciliate distribution; no broader prevalence or guessed strain
    ID is asserted.
  evidence_ids:
  - infraciliary-agent-taxon
  - infraciliary-agent-jats2017
  - infraciliary-agent-paper2007-browser
  - infraciliary-agent-paper2008-methods-browser
  - infraciliary-agent-paper2009-pdf
  - record
- assessment_id: image
  area: provenance
  topic: Figure identity, media integrity and exact license
  outcome: supported
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: The tracked Figure2 matches the freshly retrieved media byte-for-byte and
    the native MD5. Confocal panels, retained versus extended structures, GFP-Cen15
    label, colors and scale bars agree. JATS establishes CC BY3.0 and the copyright/publisher
    distinction retained in attribution.
  evidence_ids:
  - infraciliary-agent-image2017
  - infraciliary-agent-meta2017
  - infraciliary-agent-jats2017
  - record
- assessment_id: access
  area: provenance
  topic: Historical readability and current evidence
  outcome: supported
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: The record describes its earlier abstract-only access to the 2008/2009
    studies. Newly successful author-deposited text and PDF access does not make those
    historical notes false. Current review separates browser-rendered primary passages,
    native JATS, the public PDF and failed HTTP/challenge routes.
  evidence_ids:
  - infraciliary-agent-epmc
  - infraciliary-agent-paper2007-browser
  - infraciliary-agent-paper2007-results-browser
  - infraciliary-agent-paper2008-browser
  - infraciliary-agent-paper2008-methods-browser
  - infraciliary-agent-paper2009-pdf
  - infraciliary-agent-jats2017
  - record
- assessment_id: completeness
  area: completeness
  topic: Bounded representation and unresolved details
  outcome: supported
  target_ids:
  - cellstructuremech:infraciliary_lattice
  summary: Both major constituent classes, a canonical species, supported calcium
    functions, assembly dependencies and a verified image are represented. Unresolved
    exact family mapping, broader taxonomic distribution and detailed mechanisms are
    retained as bounded uncertainty. No empty optional inventory or unavailable copy
    number is promoted to a finding.
  evidence_ids:
  - infraciliary-agent-jats2017
  - infraciliary-agent-paper2007-results-browser
  - infraciliary-agent-paper2008-browser
  - infraciliary-agent-paper2009-pdf
  - infraciliary-agent-family-centrin
  - infraciliary-agent-family-scaffold
  - record
findings:
- finding_id: F1
  issue_key: infraciliary-lattice-centrin-calcium-binding-heterogeneity
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Centrin role wording omits non-calcium-binding lattice isoforms
  description: The collective ICL-centrin role starts with Calcium-binding centrin-family
    constituents, which implies a uniform binding property. The 2008 Results/Table1
    identify ICL1e, ICL7 and ICL8 as lacking predicted functional calcium-binding
    sites; Table1 separately reports prior experimental nonbinding for ICL7 and ICL8.
    Qualify the role to accommodate calcium-binding and nonbinding members while preserving
    the source-backed calcium-responsive network identity and class-level assembly
    requirement.
  target_ids:
  - cellstructuremech:infraciliary_lattice
  field_paths:
  - components[component_id=icl_centrins].role
  evidence_ids:
  - infraciliary-agent-paper2008-browser
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/infraciliary_lattice.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:Evidence Rules
  native_severity: minor
  normalization_reason: Bounded constituent-role wording; the record identity, membership,
    scoped assembly dependence and network calcium responses remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:infraciliary_lattice
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/infraciliary_lattice.yaml
    role: maintained scientific record
  description: In a future curation change, describe ICL centrins as constituents
    including calcium-binding and nonbinding isoforms. Preserve the distinction between
    predicted absent sites for ICL1e/ICL7/ICL8 and measured nonbinding reported for
    ICL7/ICL8, and retain class-level assembly essentiality.
  acceptance_checks:
  - Check the revised role against the 2008 Results/Table1 and preserve predicted
    versus measured scope.
  - Do not remove the calcium-responsive network definition or infer individual essentiality
    of every homologue.
  - Run native schema, strict, label, history and generated-page checks after maintained-record
    curation.
  generator: Maintained structure YAML; just render derives pages.
limitations:
- The native 2017 JATS body was available; listed relevant sections and captions were
  read, and all Figure2 pixels were visually inspected. Supplementary experimental
  data were not audited.
- The 2007/2008 evidence includes public author-deposited primary article passages
  rendered by web.run. Snapshot hashes identify saved JSON-encoded tool text, not
  raw publisher HTML; the tool exposes no HTTP status.
- The 2009 public PDF was readable and relevant Methods/Results/Discussion, caption
  and table text were inspected. Figure panels were not visually interpreted; filter-cycle
  timing and peak fluorochrome saturation limit initial-signal claims.
- InterPro entry inspection establishes broader family scope, not an exhaustive search
  for every possible exact ICL constituent-family mapping. QuickGO negative results
  are limited to the two recorded queries.
- One local identifier was SKIPPED by the shared resolver and independently matched
  to its tracked record; this is not a resolved external authority accession.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- All scientific repository inputs are the entire target and tracked Figure2, both
  included in the native inspection digest.
- Native schema and strict checks passed before this assessment; shared full-corpus
  gate reuse is added by the parent reviewer before finalization.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
