# Post-anaphase microtubule array: identity, composition, mechanics and provenance review

- Review: 20261021T080756Z-post-anaphase-microtubule-array-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:53:45Z
- Finished UTC: 2026-10-21T08:07:56Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The PAA identity, composition, functions, graphs and figure are source-supported within their stated limits. One minor current discussion inconsistency incorrectly says no Nda3 example is supplied.

## Scope And Provenance

Entire target and tracked Figure2; three primary bodies, native GO/OLS, six UniProt entries, three InterPro families, two taxa, bibliographic abstracts and image provenance.

Selection: Fixed batch 10 selection, index 2; one maintained record, no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990295 | data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml | maintained | post-anaphase microtubule array |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990295 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990295 | Focused validator passed. |
| Target resolver slice | passed | True | GO:1990295 | 21 identifiers OK; 5 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:1990295 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:1990295 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990295 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990295 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990295 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:1990295 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact PAA identity and hierarchy

identity: supported. Targets: GO:1990295.

Native definition, aliases and outgoing relations match the whole array. Equatorial/longitudinal portions, individual microtubules, SPB networks and eMTOC are not equivalent identities; OTHER is appropriate for this multi-filament system.

### Constituents and assembly essentiality

grounding: supported. Targets: GO:1990295.

Alpha/beta classes form the polymer, Ase1 is a localized organizational constituent with altered arrays retained after deletion, and the GO eMTOC is represented at subassembly level. Myp2/F-actin remain external recruitment context. Unknown tubulin/center assembly essentiality is not replaced by organismal viability.

### Protein identity, genes and source tiers

grounding: supported. Targets: GO:1990295.

All six reviewed accessions, genes, taxa and relevant family memberships/annotation citations match. P04688 and P05219 are explicitly identity-only; Mto1/Mto2 examples remain within the nucleating subassembly. UniProt annotation supports attribution, while primary studies support localization.

### Species versus reference stocks

scope: supported. Targets: GO:1990295.

The canonical S. pombe example is supported. Taxon284812 names the reference strain and is not asserted to be each engineered experimental stock; no fungal-wide prevalence is claimed.

### Nuclear restraint and effective ring mechanics

evidence: supported. Targets: GO:1990295.

Both functions are supported at the stated inference level. PAA restraint opposes mSPB-driven displacement before septation. Ablation-derived effective stiffness is conditional on unchanged initial tension and limited by single-plane acquisition/incomplete recoil plateaus; it is not a direct calibrated stiffness or universal anchoring requirement.

### Assembly and nuclear-position graphs

graph: supported. Targets: GO:1990295.

Every graph edge is supported within its declared scope. Selective targeting, localization, temporal ordering and contact deformation support the edges without asserting purified binding, direct force calibration, or later interphase simulations as a PAA model.

### Source readability and placement

evidence: supported. Targets: GO:1990295.

Primary citations support nearby claims; exact annotation-only citations are verified against native UniProt and abstract records. No quote-snippet verification is needed because evidence is paraphrased notes. Historical source-access statements remain historical.

### Figure identity, license and interpretation

provenance: supported. Targets: GO:1990295.

Unchanged Figure2 matches stored hash and native media checksum; CC BY4.0 is explicit. Caption identifies image versus schematic, overlap limitations and scale bars without universal dimensions.

### Bounded inventory and current discussion consistency

completeness: concern. Targets: GO:1990295.

No unverified optional inventory or family gap is promoted to a defect. One current discussion sentence contradicts the now-present Nda3 identity example; it should retain the lack of an isoform-specific localization assay while acknowledging P05219.

## Findings

### F1: Composition discussion says Nda3 is absent although P05219 is present

minor / open / confirmed; issue key: post-anaphase-array-nda3-example-discussion.

The current OPEN composition_limits rationale states that no Nda3 protein example is supplied. The beta_tubulin component now supplies reviewed P05219 for nda3 and explicitly limits that example to identity, not PAA-specific localization. Update the rationale to acknowledge that identity-only example while preserving the distinction between family composition and isoform-specific localization evidence. This is a current internal contradiction, not a correction to a dated historical access statement.

## Recommended Actions And Acceptance Checks

### A1

In a future maintained-record curation, replace the no-Nda3-example sentence with wording that acknowledges P05219 as an identity-only example and states that no Nda3-specific PAA localization assay is established here.

- Check the revised rationale against beta_tubulin.protein_examples and native P05219 identity.
- Preserve identity-only scope; do not remove the valid example or invent direct PAA localization.
- Run required native schema, strict, label, history and generated-page checks after maintained-record curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml; Entire YAML: identity, components, examples, functions, graph edges, evidence, discussions and image metadata. | context_only | Entire current target read. The tracked target hash is recorded in native source.inputs; no neighboring scientific record informs this judgment. |
| policy | .claude/skills/review-yaml-record/SKILL.md; Evidence Rules; completeness and boundary review | context_only | Apply source-specific support, distinguish direct evidence from inference, and evaluate concrete completeness gaps without treating optional empty fields as automatic failures. |
| paa-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990295,GO:0110165,GO:0015630,GO:0000923,GO:0005874,GO:0051647,GO:0051418; results indexed by GO:1990295, GO:0110165, GO:0015630, GO:0000923, GO:0005874, GO:0051647 and GO:0051418; definition, synonyms, children, isObsolete. | supports | Native QuickGO resolves all seven referenced GO classes as active, including the exact PAA definition/aliases, the alpha/beta microtubule class, the eMTOC, and the nucleation and nuclear-localization processes. Parent child lists expose PAA is_a cellular anatomical entity and part_of microtubule cytoskeleton. |
| paa-agent-go-ols | https://www.ebi.ac.uk/ols4/api/v2/ontologies/go/entities/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_1990295; GO:1990295 relatedTo and rdfs:subClassOf; property BFO_0000050/BFO_0000051 and someValuesFrom. | supports | Native OLS entity for GO:1990295 explicitly supplies is_a GO:0110165, BFO:0000050 some GO:0015630 and BFO:0000051 some GO:0000923. The existential has_part restriction is not inverted into a universal eMTOC relation. |
| paa-agent-go-haspart | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990295/paths/GO:0000923?relations=has_part; Complete error body; supported path relations. | context_only | QuickGO path request returned HTTP400 because has_part is unsupported by that path endpoint. It supplies no biological negative result; OLS provides the actual restriction. |
| paa-agent-bellingham2023-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC10047812.1/PMC10047812.1.xml; PMC10047812.1; sec2dot1–sec2dot5-cells-12-00917, sec3-cells-12-00917, sec4dot1–sec4dot4-cells-12-00917; cells-12-00917-f002; permissions. | supports | Full primary Introduction, Results 2.1–2.5, Discussion, Methods 4.1–4.4 and Figure2 caption read. Myp2-dependent Mto1 recruitment precedes ePAA/Ase1/lPAA; Ase1 deletion retains altered arrays. Selective mto1-427 effects support inferred effective ring stiffness under unchanged-tension assumptions; full mto1 deletion affects multiple networks. No universal anchoring, cytokinesis or direct-binding requirement follows. Permissions give CC BY4.0. |
| paa-agent-nuclear2023-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC10398876.1/PMC10398876.1.xml; PMC10398876.1; Results “The mSPB and PAA microtubules compete to position the nucleus” and “The PAA microtubules basket the nucleus and limit its movement toward the contractile ring”; Figures3–5; Discussion; Methods. | supports | Full primary Introduction, Results, Discussion and main Methods with embedded captions read. Selective mto1-427 versus mto1(1-1085) and imaging support opposing PAA/mSPB contributions before septation; longitudinal PAA contacts and envelope deformation support a basket interpretation. MBC and full mto1 deletion are not PAA-selective. Newborn-cell growth/interphase simulations concern a later mechanism; septal DNA protection remains unproven. |
| paa-agent-samejima2010-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2989437.1/PMC2989437.1.xml; PMC2989437.1; sec1.1 targeting and Figure1F–I; sec1.3 Myp2 and Figure3; sec1.5 Conclusions. | supports | Entire primary Results and Discussion read. Mto1-427 loses eMTOC localization and PAA nucleation while retaining SPB targeting/astral microtubules; truncation alleles provide separate Alp4 readouts. Myp2 deletion and latrunculin B impair equatorial recruitment; coimmunoprecipitation and two-hybrid assays do not exclude an intermediary. |
| paa-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.3390/cells12060917%22%20OR%20DOI%3A%2210.1091/mbc.E23-01-0034%22%20OR%20DOI%3A%2210.1016/j.cub.2010.10.006%22%20OR%20EXT_ID%3A15004232%20OR%20EXT_ID%3A15120067%20OR%20EXT_ID%3A15659644%20OR%20EXT_ID%3A10759889%20OR%20EXT_ID%3A15800064; resultList.result IDs 37099380,36980258,20970338,15800064,15659644,15120067,15004232,10759889; title, doi, abstractText. | supports | Native Europe PMC confirms the eight queried PMID identities/titles/DOIs and supplies abstracts. The five older PMID citations in protein examples are checked as UniProt attribution and abstract-level context; their original bodies were not independently audited. Abstracts of the 2005 Mto2 papers report eMTOC localization/formation defects, while the 2000 GFP-library abstract does not identify a specific Mto2 experiment. |
| paa-agent-uniprot-P04689 | https://rest.uniprot.org/uniprotkb/P04689.json; entryType, primaryAccession, proteinDescription, genes, organism; cross-references and specified SUBCELLULAR LOCATION evidence. | supports | Native reviewed P04689: Tubulin alpha-2 chain, gene tub1 (atb2, alp2), source taxon284812. IPR002452; GFP-Atb2 localization is supplied separately by primary Figure2. Reference-stock identity does not identify the experimental strain. |
| paa-agent-uniprot-P04688 | https://rest.uniprot.org/uniprotkb/P04688.json; entryType, primaryAccession, proteinDescription, genes, organism; cross-references and specified SUBCELLULAR LOCATION evidence. | supports | Native reviewed P04688: Tubulin alpha-1 chain, gene nda2, source taxon284812. IPR002452; identity-only exemplar, not a new PAA isoform-localization assay. Reference-stock identity does not identify the experimental strain. |
| paa-agent-uniprot-P05219 | https://rest.uniprot.org/uniprotkb/P05219.json; entryType, primaryAccession, proteinDescription, genes, organism; cross-references and specified SUBCELLULAR LOCATION evidence. | supports | Native reviewed P05219: Tubulin beta chain, gene nda3 (alp12), source taxon284812. IPR002453; identity-only exemplar, not direct Nda3 localization evidence. Reference-stock identity does not identify the experimental strain. |
| paa-agent-uniprot-Q9HDY1 | https://rest.uniprot.org/uniprotkb/Q9HDY1.json; entryType, primaryAccession, proteinDescription, genes, organism; cross-references and specified SUBCELLULAR LOCATION evidence. | supports | Native reviewed Q9HDY1: Anaphase spindle elongation protein 1, gene ase1, source taxon284812. IPR007145; PAA membership and dispensability come from the 2023 study. Reference-stock identity does not identify the experimental strain. |
| paa-agent-uniprot-O94488 | https://rest.uniprot.org/uniprotkb/O94488.json; entryType, primaryAccession, proteinDescription, genes, organism; cross-references and specified SUBCELLULAR LOCATION evidence. | supports | Native reviewed O94488: Gamma tubulin complex adapter mto1, gene mto1 (mbo1, mod20), source taxon284812. SUBCELLULAR LOCATION cites PMIDs15004232/15120067/15659644 for the recorded MTOC/SPB attribution; eMTOC note also cites15004232 and19001497. Reference-stock identity does not identify the experimental strain. |
| paa-agent-uniprot-Q9USP7 | https://rest.uniprot.org/uniprotkb/Q9USP7.json; entryType, primaryAccession, proteinDescription, genes, organism; cross-references and specified SUBCELLULAR LOCATION evidence. | supports | Native reviewed Q9USP7: Gamma tubulin complex adapter mto2, gene mto2, source taxon284812. SUBCELLULAR LOCATION cites PMID10759889 for cytoplasm and15659644/15800064 for MTOC/SPB; eMTOC note cites15800064. Reference-stock identity does not identify the experimental strain. |
| paa-agent-IPR002452 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/; metadata.accession, type, name, description and hierarchy. | supports | Native InterPro IPR002452 is a family for Alpha tubulin; the family defines a constituent class, not universal PAA residence of every member. |
| paa-agent-IPR002453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/; metadata.accession, type, name, description and hierarchy. | supports | Native InterPro IPR002453 is a family for Beta tubulin; the family defines a constituent class, not universal PAA residence of every member. |
| paa-agent-IPR007145 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007145/; metadata.accession, type, name, description and hierarchy. | supports | Native InterPro IPR007145 is a family for MAP65/Ase1/PRC1 microtubule-associated protein; the family defines a constituent class, not universal PAA residence of every member. |
| paa-agent-taxon-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; taxId, scientificName, rank, lineage, otherNames. | supports | Native ENA taxon4896 is Schizosaccharomyces pombe, rank species; this identity lookup does not establish prevalence or exact experimental stock. |
| paa-agent-taxon-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; taxId, scientificName, rank, lineage, otherNames. | supports | Native ENA taxon284812 is Schizosaccharomyces pombe 972h-, rank strain; this identity lookup does not establish prevalence or exact experimental stock. |
| paa-agent-bellingham2023-package | https://pmc-oa-opendata.s3.amazonaws.com/PMC10047812.1/PMC10047812.1.json; pmcid, version, doi, pmid, license_code, media_urls entry cells-12-00917-g002.jpg. | supports | Native PMC package identifies article version1, DOI/PMID and CC BY license code; its g002.jpg media MD5 is38c56497f326242cd4ffaeff8bae8188. Exact license version is established by JATS permissions. |
| paa-agent-figure2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10047812.1/cells-12-00917-g002.jpg; Original unchanged complete Figure2 panels A–I; tracked image included in source.inputs. | supports | Complete Figure2 pixels visually inspected. A–C/E show array geometry/dynamics, D is a schematic, F–G Ase1 timing/localization, H–I deletion comparison. C has2µm bar and other marked bars5µm. Fresh bytes equal tracked SHA256 e7b4b36cc890afa0a02ef9660162ddb78acbf3a53332515dd8880704e585f317 and package MD5. |
| schema-result | just validate data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml --out /private/tmp/cellstructure-batch10-20261021-giynduuy/post_anaphase_microtubule_array-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml --out /private/tmp/cellstructure-batch10-20261021-giynduuy/post_anaphase_microtubule_array-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch10-20261021-giynduuy/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch10-20261021-giynduuy/post_anaphase_microtubule_array-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml; exact collect() scope; snapshot hash identifies the entire original unchanged-base reports/curie_check.tsv, not resolver-slice.json. | supports | 21 of26 collected target identifiers returned OK at the unchanged base. Residuals: PMID:10759889: UNREACHABLE; resolved by evidence paa-agent-epmc; PMID:15004232: UNREACHABLE; resolved by evidence paa-agent-epmc; PMID:15120067: UNREACHABLE; resolved by evidence paa-agent-epmc; PMID:15659644: UNREACHABLE; resolved by evidence paa-agent-epmc; PMID:15800064: UNREACHABLE; resolved by evidence paa-agent-epmc. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The two 2023 primary bodies and main methods and the 2010 Results/Discussion were read. Separate strain supplements, actual movies, raw data and inline equation graphics were not inspected; the retrieved 2010 supplementary PDF was not used for scientific judgment.
- Only tracked Figure2 pixels were visually inspected; other figure captions and main text were read without independent pixel-level or raw-data reanalysis.
- Five older protein-example PMIDs were verified through native UniProt attribution and Europe PMC identities/abstracts, not independently audited full papers. This matches the annotation-only scope of those target notes.
- QuickGO has_part path request returned400; native OLS supplies the positive existential restriction. Native mappings alone do not prove physical membership, prevalence or exact experimental strain.
- No new local exhaustive absence claim or corpus-wide identity search was made. Historical corpus counts and source-access notes are not reinterpreted as current claims. No neighboring scientific record was relied on.
- The shared resolver slice has five transport-unreachable PMID residuals resolved by native Europe PMC identity evidence; shared full-corpus gates are handled by the parent reviewer.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Native focused schema and strict gates passed before drafting. All scientific repository inputs are the target and its tracked image, captured in the expanded native inspection.
- Root read the complete target and review, verified native-input/source hashes, checked selected primary claim-bearing sections, and visually inspected the unchanged tracked figure; a separate collaborator also audited source scope. Source reading limits remain as listed.
- Only this target receives scientific review coverage. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080756Z-post-anaphase-microtubule-array-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Post-anaphase microtubule array: identity, composition, mechanics and provenance
  review'
started_at: '2026-10-21T07:53:45Z'
finished_at: '2026-10-21T08:07:56Z'
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
summary: The PAA identity, composition, functions, graphs and figure are source-supported
  within their stated limits. One minor current discussion inconsistency incorrectly
  says no Nda3 example is supplied.
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
  - path: data/images/cytoskeleton/post_anaphase_microtubule_array/pmc10047812_cells_12_00917_f002.jpg
    sha256: e7b4b36cc890afa0a02ef9660162ddb78acbf3a53332515dd8880704e585f317
    role: context
  - path: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
    sha256: f8b698394b595d435b10633cac0cef969d32aae261b770d3ea60b974e5c4cd15
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
- target_id: GO:1990295
  path: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
  label: post-anaphase microtubule array
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
    role: maintained scientific record
scope:
  description: Entire target and tracked Figure2; three primary bodies, native GO/OLS,
    six UniProt entries, three InterPro families, two taxa, bibliographic abstracts
    and image provenance.
  selection: Fixed batch 10 selection, index 2; one maintained record, no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990295
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990295
  command: just validate data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990295
  command: just validate-strict data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
    --out /private/tmp/cellstructure-batch10-20261021-giynduuy/post_anaphase_microtubule_array-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:1990295
  summary: 21 identifiers OK; 5 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - paa-agent-epmc
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990295
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - paa-agent-go
  - paa-agent-go-ols
  - paa-agent-go-haspart
  - paa-agent-bellingham2023-jats
  - paa-agent-nuclear2023-jats
  - paa-agent-samejima2010-jats
  - paa-agent-epmc
  - paa-agent-uniprot-P04689
  - paa-agent-uniprot-P04688
  - paa-agent-uniprot-P05219
  - paa-agent-uniprot-Q9HDY1
  - paa-agent-uniprot-O94488
  - paa-agent-uniprot-Q9USP7
  - paa-agent-IPR002452
  - paa-agent-IPR002453
  - paa-agent-IPR007145
  - paa-agent-taxon-4896
  - paa-agent-taxon-284812
  - paa-agent-bellingham2023-package
  - paa-agent-figure2
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990295
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990295
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990295
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990295
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990295
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch10 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
  locator: 'Entire YAML: identity, components, examples, functions, graph edges, evidence,
    discussions and image metadata.'
  accessed_at: '2026-10-21T08:01:52Z'
  support: context_only
  summary: Entire current target read. The tracked target hash is recorded in native
    source.inputs; no neighboring scientific record informs this judgment.
- evidence_id: policy
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; completeness and boundary review
  accessed_at: '2026-10-21T08:01:52Z'
  support: context_only
  summary: Apply source-specific support, distinguish direct evidence from inference,
    and evaluate concrete completeness gaps without treating optional empty fields
    as automatic failures.
- evidence_id: paa-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990295,GO:0110165,GO:0015630,GO:0000923,GO:0005874,GO:0051647,GO:0051418
  locator: results indexed by GO:1990295, GO:0110165, GO:0015630, GO:0000923, GO:0005874,
    GO:0051647 and GO:0051418; definition, synonyms, children, isObsolete.
  accessed_at: '2026-10-21T07:55:14.358394Z'
  support: supports
  summary: Native QuickGO resolves all seven referenced GO classes as active, including
    the exact PAA definition/aliases, the alpha/beta microtubule class, the eMTOC,
    and the nucleation and nuclear-localization processes. Parent child lists expose
    PAA is_a cellular anatomical entity and part_of microtubule cytoskeleton.
  snapshot_sha256: 7a5acd582a76aafc8cd075b0413d40d52446176d6d15089093fee791bafe9978
- evidence_id: paa-agent-go-ols
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/v2/ontologies/go/entities/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_1990295
  locator: GO:1990295 relatedTo and rdfs:subClassOf; property BFO_0000050/BFO_0000051
    and someValuesFrom.
  accessed_at: '2026-10-21T07:56:06.259100Z'
  support: supports
  summary: Native OLS entity for GO:1990295 explicitly supplies is_a GO:0110165, BFO:0000050
    some GO:0015630 and BFO:0000051 some GO:0000923. The existential has_part restriction
    is not inverted into a universal eMTOC relation.
  snapshot_sha256: 0ef163791dd92390652fd521d29b39f180233eb2ffb50d42d451e91c3a717f1d
- evidence_id: paa-agent-go-haspart
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990295/paths/GO:0000923?relations=has_part
  locator: Complete error body; supported path relations.
  accessed_at: '2026-10-21T07:55:14.216118Z'
  support: context_only
  summary: QuickGO path request returned HTTP400 because has_part is unsupported by
    that path endpoint. It supplies no biological negative result; OLS provides the
    actual restriction.
  snapshot_sha256: f47546a8a45146b2f99d5b049eac94249aa10c9812db3d50ef70a4abebee6d64
- evidence_id: paa-agent-bellingham2023-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10047812.1/PMC10047812.1.xml
  locator: PMC10047812.1; sec2dot1–sec2dot5-cells-12-00917, sec3-cells-12-00917, sec4dot1–sec4dot4-cells-12-00917;
    cells-12-00917-f002; permissions.
  accessed_at: '2026-10-21T07:55:16.094019Z'
  support: supports
  summary: Full primary Introduction, Results 2.1–2.5, Discussion, Methods 4.1–4.4
    and Figure2 caption read. Myp2-dependent Mto1 recruitment precedes ePAA/Ase1/lPAA;
    Ase1 deletion retains altered arrays. Selective mto1-427 effects support inferred
    effective ring stiffness under unchanged-tension assumptions; full mto1 deletion
    affects multiple networks. No universal anchoring, cytokinesis or direct-binding
    requirement follows. Permissions give CC BY4.0.
  snapshot_sha256: 519b1918af37108acb4ae400b29e82b597cdc3e21480263bbf1041f17bf96521
- evidence_id: paa-agent-nuclear2023-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10398876.1/PMC10398876.1.xml
  locator: PMC10398876.1; Results “The mSPB and PAA microtubules compete to position
    the nucleus” and “The PAA microtubules basket the nucleus and limit its movement
    toward the contractile ring”; Figures3–5; Discussion; Methods.
  accessed_at: '2026-10-21T07:55:16.101089Z'
  support: supports
  summary: Full primary Introduction, Results, Discussion and main Methods with embedded
    captions read. Selective mto1-427 versus mto1(1-1085) and imaging support opposing
    PAA/mSPB contributions before septation; longitudinal PAA contacts and envelope
    deformation support a basket interpretation. MBC and full mto1 deletion are not
    PAA-selective. Newborn-cell growth/interphase simulations concern a later mechanism;
    septal DNA protection remains unproven.
  snapshot_sha256: aeda46b2d51023587780e3500b33fa1109119c4ab1124f5f82bd7197d697e555
- evidence_id: paa-agent-samejima2010-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2989437.1/PMC2989437.1.xml
  locator: PMC2989437.1; sec1.1 targeting and Figure1F–I; sec1.3 Myp2 and Figure3;
    sec1.5 Conclusions.
  accessed_at: '2026-10-21T07:55:16.105173Z'
  support: supports
  summary: Entire primary Results and Discussion read. Mto1-427 loses eMTOC localization
    and PAA nucleation while retaining SPB targeting/astral microtubules; truncation
    alleles provide separate Alp4 readouts. Myp2 deletion and latrunculin B impair
    equatorial recruitment; coimmunoprecipitation and two-hybrid assays do not exclude
    an intermediary.
  snapshot_sha256: 9337fd098562acbf278e8fa6b6fdb2bce9ed3f0ef1ed2bdd8cbe6d5f66e8edaa
- evidence_id: paa-agent-epmc
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.3390/cells12060917%22%20OR%20DOI%3A%2210.1091/mbc.E23-01-0034%22%20OR%20DOI%3A%2210.1016/j.cub.2010.10.006%22%20OR%20EXT_ID%3A15004232%20OR%20EXT_ID%3A15120067%20OR%20EXT_ID%3A15659644%20OR%20EXT_ID%3A10759889%20OR%20EXT_ID%3A15800064
  locator: resultList.result IDs 37099380,36980258,20970338,15800064,15659644,15120067,15004232,10759889;
    title, doi, abstractText.
  accessed_at: '2026-10-21T07:55:16.480034Z'
  support: supports
  summary: Native Europe PMC confirms the eight queried PMID identities/titles/DOIs
    and supplies abstracts. The five older PMID citations in protein examples are
    checked as UniProt attribution and abstract-level context; their original bodies
    were not independently audited. Abstracts of the 2005 Mto2 papers report eMTOC
    localization/formation defects, while the 2000 GFP-library abstract does not identify
    a specific Mto2 experiment.
  snapshot_sha256: 853e2c5b2894a3e2c0517ac24ef5cbca2630b5b71cebee288a20043ef756f435
- evidence_id: paa-agent-uniprot-P04689
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P04689.json
  locator: entryType, primaryAccession, proteinDescription, genes, organism; cross-references
    and specified SUBCELLULAR LOCATION evidence.
  accessed_at: '2026-10-21T07:55:14.239363Z'
  support: supports
  summary: 'Native reviewed P04689: Tubulin alpha-2 chain, gene tub1 (atb2, alp2),
    source taxon284812. IPR002452; GFP-Atb2 localization is supplied separately by
    primary Figure2. Reference-stock identity does not identify the experimental strain.'
  snapshot_sha256: 3bfa569ef452b581ecc2013f8b85880667fd4de3e6d11df1bdcbbc3319ade3e3
- evidence_id: paa-agent-uniprot-P04688
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P04688.json
  locator: entryType, primaryAccession, proteinDescription, genes, organism; cross-references
    and specified SUBCELLULAR LOCATION evidence.
  accessed_at: '2026-10-21T07:55:14.842382Z'
  support: supports
  summary: 'Native reviewed P04688: Tubulin alpha-1 chain, gene nda2, source taxon284812.
    IPR002452; identity-only exemplar, not a new PAA isoform-localization assay. Reference-stock
    identity does not identify the experimental strain.'
  snapshot_sha256: f6104d4ad0cb6eae74ad3cdbfc6a3c779f42c9522e262843d52d6ca7ef46f4fd
- evidence_id: paa-agent-uniprot-P05219
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P05219.json
  locator: entryType, primaryAccession, proteinDescription, genes, organism; cross-references
    and specified SUBCELLULAR LOCATION evidence.
  accessed_at: '2026-10-21T07:55:14.891839Z'
  support: supports
  summary: 'Native reviewed P05219: Tubulin beta chain, gene nda3 (alp12), source
    taxon284812. IPR002453; identity-only exemplar, not direct Nda3 localization evidence.
    Reference-stock identity does not identify the experimental strain.'
  snapshot_sha256: 748f30a9ed411acc3358c1828f32354becece0ef6d16b60ef4319c8d6bbe66b2
- evidence_id: paa-agent-uniprot-Q9HDY1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9HDY1.json
  locator: entryType, primaryAccession, proteinDescription, genes, organism; cross-references
    and specified SUBCELLULAR LOCATION evidence.
  accessed_at: '2026-10-21T07:55:14.847983Z'
  support: supports
  summary: 'Native reviewed Q9HDY1: Anaphase spindle elongation protein 1, gene ase1,
    source taxon284812. IPR007145; PAA membership and dispensability come from the
    2023 study. Reference-stock identity does not identify the experimental strain.'
  snapshot_sha256: 6eaa54b440390539f06f41d4cf10735eeb6d10b0840d2616d8edc4f3093bc08a
- evidence_id: paa-agent-uniprot-O94488
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O94488.json
  locator: entryType, primaryAccession, proteinDescription, genes, organism; cross-references
    and specified SUBCELLULAR LOCATION evidence.
  accessed_at: '2026-10-21T07:55:14.925744Z'
  support: supports
  summary: 'Native reviewed O94488: Gamma tubulin complex adapter mto1, gene mto1
    (mbo1, mod20), source taxon284812. SUBCELLULAR LOCATION cites PMIDs15004232/15120067/15659644
    for the recorded MTOC/SPB attribution; eMTOC note also cites15004232 and19001497.
    Reference-stock identity does not identify the experimental strain.'
  snapshot_sha256: 4903509b256bf5164ea7e5b80970bbb89056a71a4ea4a257e9feb8adcaf0e46b
- evidence_id: paa-agent-uniprot-Q9USP7
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9USP7.json
  locator: entryType, primaryAccession, proteinDescription, genes, organism; cross-references
    and specified SUBCELLULAR LOCATION evidence.
  accessed_at: '2026-10-21T07:55:15.613950Z'
  support: supports
  summary: 'Native reviewed Q9USP7: Gamma tubulin complex adapter mto2, gene mto2,
    source taxon284812. SUBCELLULAR LOCATION cites PMID10759889 for cytoplasm and15659644/15800064
    for MTOC/SPB; eMTOC note cites15800064. Reference-stock identity does not identify
    the experimental strain.'
  snapshot_sha256: ae275cdd142bdffa04ce4e120465b57fbd20dbe1223de0be9a72966ec6e40698
- evidence_id: paa-agent-IPR002452
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/
  locator: metadata.accession, type, name, description and hierarchy.
  accessed_at: '2026-10-21T07:55:15.038713Z'
  support: supports
  summary: Native InterPro IPR002452 is a family for Alpha tubulin; the family defines
    a constituent class, not universal PAA residence of every member.
  snapshot_sha256: ff28f4d004d8f82a804f7263ff1df3ab78d7bdbdeee755fa924a58e872602b5a
- evidence_id: paa-agent-IPR002453
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/
  locator: metadata.accession, type, name, description and hierarchy.
  accessed_at: '2026-10-21T07:55:16.456530Z'
  support: supports
  summary: Native InterPro IPR002453 is a family for Beta tubulin; the family defines
    a constituent class, not universal PAA residence of every member.
  snapshot_sha256: edbfe5509d6e568069c7105eacc2b7e296e84e0790a16a63d836c45a094d20ef
- evidence_id: paa-agent-IPR007145
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007145/
  locator: metadata.accession, type, name, description and hierarchy.
  accessed_at: '2026-10-21T07:55:15.454941Z'
  support: supports
  summary: Native InterPro IPR007145 is a family for MAP65/Ase1/PRC1 microtubule-associated
    protein; the family defines a constituent class, not universal PAA residence of
    every member.
  snapshot_sha256: e2a689c1455d008bbb9885458d09d3b5d914d67afb595cf29457e2efb02b768d
- evidence_id: paa-agent-taxon-4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: taxId, scientificName, rank, lineage, otherNames.
  accessed_at: '2026-10-21T07:55:14.239396Z'
  support: supports
  summary: Native ENA taxon4896 is Schizosaccharomyces pombe, rank species; this identity
    lookup does not establish prevalence or exact experimental stock.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: paa-agent-taxon-284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: taxId, scientificName, rank, lineage, otherNames.
  accessed_at: '2026-10-21T07:55:14.243431Z'
  support: supports
  summary: Native ENA taxon284812 is Schizosaccharomyces pombe 972h-, rank strain;
    this identity lookup does not establish prevalence or exact experimental stock.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: paa-agent-bellingham2023-package
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10047812.1/PMC10047812.1.json
  locator: pmcid, version, doi, pmid, license_code, media_urls entry cells-12-00917-g002.jpg.
  accessed_at: '2026-10-21T07:55:15.935451Z'
  support: supports
  summary: Native PMC package identifies article version1, DOI/PMID and CC BY license
    code; its g002.jpg media MD5 is38c56497f326242cd4ffaeff8bae8188. Exact license
    version is established by JATS permissions.
  snapshot_sha256: 90652face5516c0a0cafefdd007b5cca386ec42d330e9a91d8038a8a9c0b267f
- evidence_id: paa-agent-figure2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10047812.1/cells-12-00917-g002.jpg
  locator: Original unchanged complete Figure2 panels A–I; tracked image included
    in source.inputs.
  accessed_at: '2026-10-21T07:55:16.696422Z'
  support: supports
  summary: Complete Figure2 pixels visually inspected. A–C/E show array geometry/dynamics,
    D is a schematic, F–G Ase1 timing/localization, H–I deletion comparison. C has2µm
    bar and other marked bars5µm. Fresh bytes equal tracked SHA256 e7b4b36cc890afa0a02ef9660162ddb78acbf3a53332515dd8880704e585f317
    and package MD5.
  snapshot_sha256: e7b4b36cc890afa0a02ef9660162ddb78acbf3a53332515dd8880704e585f317
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:53:46Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml'
  snapshot_sha256: 28fdd844f97b53cb0bd24f31722588d122520cb6cf464da766392737f5ad86d5
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
    --out /private/tmp/cellstructure-batch10-20261021-giynduuy/post_anaphase_microtubule_array-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:53:47Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml\
    \ --out /private/tmp/cellstructure-batch10-20261021-giynduuy/post_anaphase_microtubule_array-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch10-20261021-giynduuy/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch10-20261021-giynduuy/post_anaphase_microtubule_array-strict.tsv"
  snapshot_sha256: 00e94bfeeebce379aafac2bbe6451aea746969a67e52a51ef117a98f05d35499
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml; exact
    collect() scope; snapshot hash identifies the entire original unchanged-base reports/curie_check.tsv,
    not resolver-slice.json.
  accessed_at: '2026-10-21T08:01:52Z'
  support: supports
  summary: '21 of26 collected target identifiers returned OK at the unchanged base.
    Residuals: PMID:10759889: UNREACHABLE; resolved by evidence paa-agent-epmc; PMID:15004232:
    UNREACHABLE; resolved by evidence paa-agent-epmc; PMID:15120067: UNREACHABLE;
    resolved by evidence paa-agent-epmc; PMID:15659644: UNREACHABLE; resolved by evidence
    paa-agent-epmc; PMID:15800064: UNREACHABLE; resolved by evidence paa-agent-epmc.
    Source-native identity checked separately.'
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
  topic: Exact PAA identity and hierarchy
  outcome: supported
  target_ids:
  - GO:1990295
  summary: Native definition, aliases and outgoing relations match the whole array.
    Equatorial/longitudinal portions, individual microtubules, SPB networks and eMTOC
    are not equivalent identities; OTHER is appropriate for this multi-filament system.
  evidence_ids:
  - paa-agent-go
  - paa-agent-go-ols
  - paa-agent-bellingham2023-jats
  - paa-agent-nuclear2023-jats
- assessment_id: grounding
  area: grounding
  topic: Constituents and assembly essentiality
  outcome: supported
  target_ids:
  - GO:1990295
  summary: Alpha/beta classes form the polymer, Ase1 is a localized organizational
    constituent with altered arrays retained after deletion, and the GO eMTOC is represented
    at subassembly level. Myp2/F-actin remain external recruitment context. Unknown
    tubulin/center assembly essentiality is not replaced by organismal viability.
  evidence_ids:
  - paa-agent-go
  - paa-agent-go-ols
  - paa-agent-bellingham2023-jats
  - paa-agent-samejima2010-jats
  - paa-agent-IPR002452
  - paa-agent-IPR002453
  - paa-agent-IPR007145
- assessment_id: proteins
  area: grounding
  topic: Protein identity, genes and source tiers
  outcome: supported
  target_ids:
  - GO:1990295
  summary: All six reviewed accessions, genes, taxa and relevant family memberships/annotation
    citations match. P04688 and P05219 are explicitly identity-only; Mto1/Mto2 examples
    remain within the nucleating subassembly. UniProt annotation supports attribution,
    while primary studies support localization.
  evidence_ids:
  - paa-agent-uniprot-P04689
  - paa-agent-uniprot-P04688
  - paa-agent-uniprot-P05219
  - paa-agent-uniprot-Q9HDY1
  - paa-agent-uniprot-O94488
  - paa-agent-uniprot-Q9USP7
  - paa-agent-epmc
  - paa-agent-bellingham2023-jats
  - paa-agent-samejima2010-jats
- assessment_id: scope
  area: scope
  topic: Species versus reference stocks
  outcome: supported
  target_ids:
  - GO:1990295
  summary: The canonical S. pombe example is supported. Taxon284812 names the reference
    strain and is not asserted to be each engineered experimental stock; no fungal-wide
    prevalence is claimed.
  evidence_ids:
  - paa-agent-taxon-4896
  - paa-agent-taxon-284812
  - paa-agent-bellingham2023-jats
  - paa-agent-nuclear2023-jats
- assessment_id: function
  area: evidence
  topic: Nuclear restraint and effective ring mechanics
  outcome: supported
  target_ids:
  - GO:1990295
  summary: Both functions are supported at the stated inference level. PAA restraint
    opposes mSPB-driven displacement before septation. Ablation-derived effective
    stiffness is conditional on unchanged initial tension and limited by single-plane
    acquisition/incomplete recoil plateaus; it is not a direct calibrated stiffness
    or universal anchoring requirement.
  evidence_ids:
  - paa-agent-bellingham2023-jats
  - paa-agent-nuclear2023-jats
- assessment_id: graphs
  area: graph
  topic: Assembly and nuclear-position graphs
  outcome: supported
  target_ids:
  - GO:1990295
  summary: Every graph edge is supported within its declared scope. Selective targeting,
    localization, temporal ordering and contact deformation support the edges without
    asserting purified binding, direct force calibration, or later interphase simulations
    as a PAA model.
  evidence_ids:
  - paa-agent-samejima2010-jats
  - paa-agent-bellingham2023-jats
  - paa-agent-nuclear2023-jats
  - paa-agent-go
- assessment_id: evidence
  area: evidence
  topic: Source readability and placement
  outcome: supported
  target_ids:
  - GO:1990295
  summary: Primary citations support nearby claims; exact annotation-only citations
    are verified against native UniProt and abstract records. No quote-snippet verification
    is needed because evidence is paraphrased notes. Historical source-access statements
    remain historical.
  evidence_ids:
  - paa-agent-bellingham2023-jats
  - paa-agent-nuclear2023-jats
  - paa-agent-samejima2010-jats
  - paa-agent-epmc
  - paa-agent-uniprot-P04689
  - paa-agent-uniprot-P04688
  - paa-agent-uniprot-P05219
  - paa-agent-uniprot-Q9HDY1
  - paa-agent-uniprot-O94488
  - paa-agent-uniprot-Q9USP7
- assessment_id: image
  area: provenance
  topic: Figure identity, license and interpretation
  outcome: supported
  target_ids:
  - GO:1990295
  summary: Unchanged Figure2 matches stored hash and native media checksum; CC BY4.0
    is explicit. Caption identifies image versus schematic, overlap limitations and
    scale bars without universal dimensions.
  evidence_ids:
  - paa-agent-figure2
  - paa-agent-bellingham2023-package
  - paa-agent-bellingham2023-jats
- assessment_id: completeness
  area: completeness
  topic: Bounded inventory and current discussion consistency
  outcome: concern
  target_ids:
  - GO:1990295
  summary: No unverified optional inventory or family gap is promoted to a defect.
    One current discussion sentence contradicts the now-present Nda3 identity example;
    it should retain the lack of an isoform-specific localization assay while acknowledging
    P05219.
  evidence_ids:
  - record
  - paa-agent-uniprot-P05219
findings:
- finding_id: F1
  issue_key: post-anaphase-array-nda3-example-discussion
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Composition discussion says Nda3 is absent although P05219 is present
  description: The current OPEN composition_limits rationale states that no Nda3 protein
    example is supplied. The beta_tubulin component now supplies reviewed P05219 for
    nda3 and explicitly limits that example to identity, not PAA-specific localization.
    Update the rationale to acknowledge that identity-only example while preserving
    the distinction between family composition and isoform-specific localization evidence.
    This is a current internal contradiction, not a correction to a dated historical
    access statement.
  target_ids:
  - GO:1990295
  field_paths:
  - discussions[discussion_id=composition_limits].rationale
  - components[component_id=beta_tubulin].protein_examples
  evidence_ids:
  - record
  - paa-agent-uniprot-P05219
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:Evidence Rules
  native_severity: minor
  normalization_reason: Bounded stale inventory wording; the component identity, source
    limitation and array interpretation remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990295
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
    role: maintained scientific record
  description: In a future maintained-record curation, replace the no-Nda3-example
    sentence with wording that acknowledges P05219 as an identity-only example and
    states that no Nda3-specific PAA localization assay is established here.
  acceptance_checks:
  - Check the revised rationale against beta_tubulin.protein_examples and native P05219
    identity.
  - Preserve identity-only scope; do not remove the valid example or invent direct
    PAA localization.
  - Run required native schema, strict, label, history and generated-page checks after
    maintained-record curation.
  generator: Maintained structure YAML; just render derives pages.
limitations:
- The two 2023 primary bodies and main methods and the 2010 Results/Discussion were
  read. Separate strain supplements, actual movies, raw data and inline equation graphics
  were not inspected; the retrieved 2010 supplementary PDF was not used for scientific
  judgment.
- Only tracked Figure2 pixels were visually inspected; other figure captions and main
  text were read without independent pixel-level or raw-data reanalysis.
- Five older protein-example PMIDs were verified through native UniProt attribution
  and Europe PMC identities/abstracts, not independently audited full papers. This
  matches the annotation-only scope of those target notes.
- QuickGO has_part path request returned400; native OLS supplies the positive existential
  restriction. Native mappings alone do not prove physical membership, prevalence
  or exact experimental strain.
- No new local exhaustive absence claim or corpus-wide identity search was made. Historical
  corpus counts and source-access notes are not reinterpreted as current claims. No
  neighboring scientific record was relied on.
- The shared resolver slice has five transport-unreachable PMID residuals resolved
  by native Europe PMC identity evidence; shared full-corpus gates are handled by
  the parent reviewer.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Native focused schema and strict gates passed before drafting. All scientific repository
  inputs are the target and its tracked image, captured in the expanded native inspection.
- Root read the complete target and review, verified native-input/source hashes, checked
  selected primary claim-bearing sections, and visually inspected the unchanged tracked
  figure; a separate collaborator also audited source scope. Source reading limits
  remain as listed.
- Only this target receives scientific review coverage. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
