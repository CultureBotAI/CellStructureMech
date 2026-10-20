# Actin body identity, contextual composition and metabolic disassembly

- Review: 20261020T033714Z-actin-body-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-19T23:42:01.491995Z
- Finished UTC: 2026-10-20T03:37:14Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All material assertions are supported within their stated experimental limits. No curation defect observed; unresolved family/reporter identities and reserve-function mechanism are explicitly documented.

## Scope And Provenance

Complete maintained target, all components/examples, both graph edges, all discussions and hosted image.

Selection: Twentieth originally unreviewed path; tenth target of batch2.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0099079 | data/structures/cytoskeleton/actin_body.yaml | maintained | actin body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0099079 | Passed using writable UV_CACHE_DIR. Initial invocation exited2 because the default uv cache was sandbox-inaccessible; retry did not change record inputs. |
| Focused native strict | passed | True | GO:0099079 | Passed using writable UV_CACHE_DIR. Initial invocation exited2 because the default uv cache was sandbox-inaccessible; retry did not change record inputs. |
| Claim-level source and identifier audit | passed | True | GO:0099079 | All material assertions and current authority mappings inspected; no observed defect. Existing acknowledged unknowns are retained. |
| Expression-module applicability | not_applicable | False | GO:0099079 | No expression-module assertion or dataset mapping is needed to assess the cited yeast microscopy and pathway-level perturbation evidence. |
| Target resolver coverage | passed | True | GO:0099079 | All36 collected target identifiers returned OK. Current authority receipts separately establish scientific identity, and image version/HTTP references were inspected. |
| Full corpus QC | passed | True | GO:0099079 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0099079 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0099079 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0099079 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0099079 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact actin-body identity and relation types

identity: supported. Targets: GO:0099079.

An actin-rich assembly is distinct from patches, cables and protein monomers. is-a anatomical structure and part-of cytoskeleton/cytoplasm are appropriate. Later single-cell observations justify the cautious growth-arrested definition.

### Eleven classes and partial membership

completeness: supported. Targets: GO:0099079.

The localization inventory preserves strict/partial overlap, species-specific observations, unknown essentiality and absent stoichiometric reconstruction. Scp1 and displaced polarity factors are correctly excluded.

### Nine family groundings and two label-only components

grounding: supported. Targets: GO:0099079.

All assigned InterPro families match their exemplars. Abp1 domain architecture and the broader Abp140 methyltransferase family are not substituted for precise whole-component identities.

### Species and reference-strain examples

scope: supported. Targets: GO:0099079.

Fourteen reviewed sequence exemplars are explicitly illustrative. Conditional species distributions do not assert universal occurrence or that reference stocks were directly imaged.

### Two glucose-metabolism disassembly edges

graph: supported. Targets: GO:0099079.

Both edges match the assigned Figure4 perturbation evidence. The graph does not identify a downstream metabolite or mistake ATP replenishment for basal ATP requirements.

### Reserve hypothesis and cell-fate limits

completeness: supported. Targets: GO:0099079.

No established storage function is asserted. Heterogeneous cell fates and stationary-phase actin organizations remain explicit; body presence is not treated as a diagnostic of viable quiescence.

### Hosted microscopy and licence

provenance: supported. Targets: GO:0099079.

Checksum, exact version, authorship, species, panel assignments and CC BY4.0 permissions match. Cell-volume measurements are not presented as actin-body dimensions.

### Six discussions and native status

completeness: supported. Targets: GO:0099079.

Open family, reporter-identity, reserve-function and metabolic-signal questions remain bounded. No unsupported protein is silently added. Historical figure correction is retained; no trait or physical-measurement claim is made.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0099079,GO:0110165,GO:0015629,GO:0005737; Exact term names, definitions and relationships | supports | All four terms are active and identify the body, cellular anatomical structure, actin cytoskeleton and cytoplasm. The record uses the exact body term; its growth-arrested scope is informed by later experimental evidence. |
| proteins | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=accession%3AP60010%20OR%20accession%3AP32381%20OR%20accession%3AP15891%20OR%20accession%3AQ08641%20OR%20accession%3AP32599%20OR%20accession%3AO59945%20OR%20accession%3AP28495%20OR%20accession%3AP13517%20OR%20accession%3AQ9HGP5%20OR%20accession%3AP40518%20OR%20accession%3AQ05933%20OR%20accession%3AP53731%20OR%20accession%3AQ06440%20OR%20accession%3AP17555; All fourteen results: accession, genes, proteinDescription, entryType, organism | supports | All fourteen accessions have matching reviewed status, gene names and reference-strain taxa. ACT1 and ARP2 remain distinct roles; SRV2 and capping-subunit CAP1 are not conflated. Reference sequences are not claimed as exact imaged stocks. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=4932,4896,559292,284812&amp;retmode=xml; Exact taxon records and species/strain context | supports | Species4932/4896 and reference strains559292/284812 resolve to the recorded budding- and fission-yeast names. |
| IPR001698 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001698/; metadata accession, name and type | supports | Current InterPro family: F-actin-capping protein subunit beta. |
| IPR001837 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001837/; metadata accession, name and type | supports | Current InterPro family: Adenylate cyclase-associated CAP. |
| IPR002189 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002189/; metadata accession, name and type | supports | Current InterPro family: F-actin-capping protein subunit alpha. |
| IPR004000 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004000/; metadata accession, name and type | supports | Current InterPro family: Actin family. |
| IPR006789 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006789/; metadata accession, name and type | supports | Current InterPro family: Actin-related protein 2/3 complex subunit 5. |
| IPR007188 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007188/; metadata accession, name and type | supports | Current InterPro family: Actin-related protein 2/3 complex subunit 2. |
| IPR007204 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007204/; metadata accession, name and type | supports | Current InterPro family: Actin-related protein 2/3 complex subunit 3. |
| IPR015505 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR015505/; metadata accession, name and type | supports | Current InterPro family: Coronin. |
| IPR039959 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039959/; metadata accession, name and type | supports | Current InterPro family: Fimbrin/Plastin. |
| ip-O59945 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/O59945/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-P13517 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P13517/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-P15891 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P15891/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-P17555 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P17555/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-P28495 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P28495/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-P32381 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P32381/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-P32599 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P32599/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-P40518 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P40518/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-P53731 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P53731/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-P60010 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P60010/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-Q05933 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q05933/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-Q06440 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q06440/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-Q08641 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q08641/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| ip-Q9HGP5 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q9HGP5/?page_size=200; All results; next=null | supports | Complete integrated-family/domain match list inspected for the selected representative. Family-level grounding matches where assigned; broad domains alone do not establish exact Abp1/Abp140 whole-component identity. |
| doi-2006 | https://api.crossref.org/works/10.1091/mbc.E06-04-0282; message DOI/title and bibliographic metadata | supports | Exact DOI and title verified against the cited article. |
| doi-2011 | https://api.crossref.org/works/10.1083/jcb.201009028; message DOI/title and bibliographic metadata | supports | Exact DOI and title verified against the cited article. |
| doi-2015 | https://api.crossref.org/works/10.1083/jcb.201502025; message DOI/title and bibliographic metadata | supports | Exact DOI and title verified against the cited article. |
| doi-2018 | https://api.crossref.org/works/10.7554/eLife.35685; message DOI/title and bibliographic metadata | supports | Exact DOI and title verified against the cited article. |
| doi-2015b | https://api.crossref.org/works/10.1128/MCB.00811-15; message DOI/title and bibliographic metadata | supports | Exact DOI and title verified against the cited article. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=30299253,26351139,26124291,21402786,16914523&amp;retmode=xml; Exact article identifiers | supports | Cited PubMed records inspected for article identifiers and bibliographic correspondence. |
| paper2006 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1635378/?pdf=1; Full Results, Discussion and Methods; Figures1–4 | supports | Results distinguish strict from partial localizers; morphology, cytoplasmic location, slow turnover and refeeding response support the record. Methods identify the reporter and strain context. Reserve function remains a hypothesis; Scp1 residence is not established. |
| paper2011 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3063145/fullTextXML; Glucose-catabolism Results, Figure4 caption and experimental context | supports | Figure4 and accompanying Results support the two pathway-level edges. Glucose metabolism is required in tested perturbations; ATP replenishment is neither necessary nor sufficient. The downstream molecular signal is unresolved. |
| paper2015 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4494004/fullTextXML; Actin-body Results; Figures6–7; Discussion | supports | Figure6 and Results support fission-yeast Fim1/Acp2 localization and distinguish excluded polarity proteins. The text inconsistently uses Aap1 and App1; the record appropriately retains reporter identity as unresolved. |
| paper2018 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6177259/fullTextXML; Cell-fate Results, Figure5 and supplement1, permissions | supports | Individual-cell fate observations support growth-arrested rather than exclusively quiescent scope. Figure5 supplement1 caption and permissions match the hosted image and CC BY4.0 licence. |
| paper2015b | https://pmc.ncbi.nlm.nih.gov/articles/PMC4609741/; Primary abstract | supports | The abstract supports heterogeneous stationary-phase actin organization; it is used only for that bounded context. |
| image | https://pmc-oa-opendata.s3.amazonaws.com/PMC6177259.1/elife-35685-fig5-figsupp1.jpg; Figure5 supplement1 original JPEG; all panels | supports | Viewed all three panels. PanelA depicts actin, panelB proteasome localization and panelC cell volume. Hosted bytes and SHA256 match the download; image MD5 matches official version metadata. |
| image-version | https://pmc-oa-opendata.s3.amazonaws.com/PMC6177259.1/PMC6177259.1.json; Article identifiers, license_code, media_urls | supports | Official metadata identifies PMC6177259 version1, exact DOI/PMID, CC BY and the matching image MD5. |
| record | data/structures/cytoskeleton/actin_body.yaml; Entire file plus both actin_body history events | context_only | Read all eleven component classes, fourteen examples, two edges, species distributions, image and six discussions. Historical access notes describe earlier curation; full2006 Methods were recovered during this review. PROPOSED is preserved. |
| schema-result | just validate data/structures/cytoskeleton/actin_body.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/actin_body.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/actin_body.yaml --out /private/tmp/cellstructure-batch2-20261019-52rdp0/actin-body/strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/actin_body.yaml --out /private/tmp/cellstructure-batch2-20261019-52rdp0/actin-body/strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch2-20261019-52rdp0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch2-20261019-52rdp0/actin-body/strict.tsv |
| target-resolver-coverage | just check-curies-strict; data/structures/cytoskeleton/actin_body.yaml; exact collect() scope; reports/curie_check.tsv | supports | All36 CURIE-shaped target scalars returned OK; HTTP URLs and prose inspected separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Localization is not a complete stoichiometric reconstruction or proof of essentiality.
- The fission-yeast Aap1/App1 reporter correspondence, exact label-only protein families and proposed reserve function remain unresolved as acknowledged in the record.
- No inference is made about all growth-arrested cells, universal survival or the identity of the downstream metabolic signal.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The actual review start is the timestamp of the delegated inspect artifact; coordinating review subsequently recovered full2006 Methods and verified hosted microscopy.
- Initial focused validator invocations encountered a default-cache permission failure; successful reruns used the existing writable cache. No record bytes changed.
- The explicit user request authorizes saving clean reviews. Scientific status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T033714Z-actin-body-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Actin body identity, contextual composition and metabolic disassembly
started_at: '2026-10-19T23:42:01.491995Z'
finished_at: '2026-10-20T03:37:14Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Delegated inspection and coordinating scientific review; prior
    agent authorship does not establish independent human review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All material assertions are supported within their stated experimental limits.
  No curation defect observed; unresolved family/reporter identities and reserve-function
  mechanism are explicitly documented.
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
  - path: data/images/cytoskeleton/actin_body/pmc6177259_fig5s1.jpg
    sha256: 9e19d13e1ff55ea63391b6398cb9950b60c7ff0f0b61695660676dbfa20a3e61
    role: context
  - path: data/structures/cytoskeleton/actin_body.yaml
    sha256: b0abd6f5cb40fec99ab2d5a23a56b7307041f4ac8eda2a32b9db8d57680f22ea
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
  - path: history/records/actin_body/2026-10-05T144337Z-codex-fd20b4.yaml
    sha256: 0a879d8fca34350ee116d01940f0a4a7398084166290821d7ddc86d9b665885e
    role: context
  - path: history/records/actin_body/2026-10-05T144436Z-codex-d12eef.yaml
    sha256: 74a938199e0682fbce2ae8283592463f174f24bdf9099abf7fb6d296552c3668
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reviews/structured/20261011T071241Z-a_axonemal_microtubule-audit/review.yaml
    sha256: ca141a2a562d013be835294b517a018a257eed053888a28bfe1255179ca29234
    role: context
  - path: reviews/structured/20261011T071248Z-actin_cortical_patch-audit/review.yaml
    sha256: 263be87cbbe13142a0bfb2f501659bddc2af5d499cefd7998c9a308d0d79da8f
    role: context
  - path: reviews/structured/20261011T071255Z-actomyosin_contractile_ring-audit/review.yaml
    sha256: cdab961234925eb51a7bd43c6cd51d8a38c9561d547083967dc5a1d5467e59eb
    role: context
  - path: reviews/structured/20261011T071302Z-alfa_filament-audit/review.yaml
    sha256: d46949144ceca9996ec4d37388a687d91f58eb1e5c8e6c29077b8eb8f8e71cba
    role: context
  - path: reviews/structured/20261011T074246Z-a_axonemal_microtubule-disposition/review.yaml
    sha256: 1256abb96de27cbcb2d7aec810027a12f858c2140ce6d04a326f899b81bf51ae
    role: context
  - path: reviews/structured/20261011T074252Z-actin_cortical_patch-disposition/review.yaml
    sha256: ac86765452fa22abb8fe3aad4db5b3b6113ab43a57bb4108cd7625be1c0cbbab
    role: context
  - path: reviews/structured/20261011T074258Z-actomyosin_contractile_ring-disposition/review.yaml
    sha256: ddbae3e0856760edafbfb64c0c3b9afa60016247141f64c20097332c361eb1c8
    role: context
  - path: reviews/structured/20261011T074304Z-alfa_filament-disposition/review.yaml
    sha256: 40673f9464201fb271a9c6124a3cb9f251ac9c9d9ad27e1041ede3ca6bc02d67
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
- kind: maintained
  label: actin body
  owner_paths:
  - path: data/structures/cytoskeleton/actin_body.yaml
    repository: CultureBotAI/CellStructureMech
    role: maintained scientific record
  path: data/structures/cytoskeleton/actin_body.yaml
  target_id: GO:0099079
scope:
  description: Complete maintained target, all components/examples, both graph edges,
    all discussions and hosted image.
  selection: Twentieth originally unreviewed path; tenth target of batch2.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0099079
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0099079
  command: just validate data/structures/cytoskeleton/actin_body.yaml
  exit_code: 0
  summary: Passed using writable UV_CACHE_DIR. Initial invocation exited2 because
    the default uv cache was sandbox-inaccessible; retry did not change record inputs.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0099079
  command: just validate-strict data/structures/cytoskeleton/actin_body.yaml --out
    /private/tmp/cellstructure-batch2-20261019-52rdp0/actin-body/strict.tsv
  exit_code: 0
  summary: Passed using writable UV_CACHE_DIR. Initial invocation exited2 because
    the default uv cache was sandbox-inaccessible; retry did not change record inputs.
  evidence_ids:
  - strict-result
- check_id: source-audit
  name: Claim-level source and identifier audit
  status: passed
  required: true
  target_ids:
  - GO:0099079
  summary: All material assertions and current authority mappings inspected; no observed
    defect. Existing acknowledged unknowns are retained.
  evidence_ids:
  - go
  - proteins
  - taxa
  - IPR001698
  - IPR001837
  - IPR002189
  - IPR004000
  - IPR006789
  - IPR007188
  - IPR007204
  - IPR015505
  - IPR039959
  - ip-O59945
  - ip-P13517
  - ip-P15891
  - ip-P17555
  - ip-P28495
  - ip-P32381
  - ip-P32599
  - ip-P40518
  - ip-P53731
  - ip-P60010
  - ip-Q05933
  - ip-Q06440
  - ip-Q08641
  - ip-Q9HGP5
  - doi-2006
  - doi-2011
  - doi-2015
  - doi-2018
  - doi-2015b
  - pubmed
  - paper2006
  - paper2011
  - paper2015
  - paper2018
  - paper2015b
  - image
  - image-version
  - record
  - schema-result
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0099079
  summary: No expression-module assertion or dataset mapping is needed to assess the
    cited yeast microscopy and pathway-level perturbation evidence.
- check_id: target-resolver-coverage
  name: Target resolver coverage
  status: passed
  required: true
  target_ids:
  - GO:0099079
  summary: All36 collected target identifiers returned OK. Current authority receipts
    separately establish scientific identity, and image version/HTTP references were
    inspected.
  evidence_ids:
  - target-resolver-coverage
  - go
  - proteins
  - taxa
  - image-version
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0099079
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
  - GO:0099079
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
  - GO:0099079
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
  - GO:0099079
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
  - GO:0099079
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
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0099079,GO:0110165,GO:0015629,GO:0005737
  locator: Exact term names, definitions and relationships
  accessed_at: '2026-10-19T23:42:20Z'
  support: supports
  summary: All four terms are active and identify the body, cellular anatomical structure,
    actin cytoskeleton and cytoplasm. The record uses the exact body term; its growth-arrested
    scope is informed by later experimental evidence.
  snapshot_sha256: 069b5f7e98661a407b5e33ccc17b8f59e0acaa27d704ba4c18e539c7e90f1b44
- evidence_id: proteins
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=accession%3AP60010%20OR%20accession%3AP32381%20OR%20accession%3AP15891%20OR%20accession%3AQ08641%20OR%20accession%3AP32599%20OR%20accession%3AO59945%20OR%20accession%3AP28495%20OR%20accession%3AP13517%20OR%20accession%3AQ9HGP5%20OR%20accession%3AP40518%20OR%20accession%3AQ05933%20OR%20accession%3AP53731%20OR%20accession%3AQ06440%20OR%20accession%3AP17555
  locator: 'All fourteen results: accession, genes, proteinDescription, entryType,
    organism'
  accessed_at: '2026-10-19T23:42:20Z'
  support: supports
  summary: All fourteen accessions have matching reviewed status, gene names and reference-strain
    taxa. ACT1 and ARP2 remain distinct roles; SRV2 and capping-subunit CAP1 are not
    conflated. Reference sequences are not claimed as exact imaged stocks.
  snapshot_sha256: 6a6383447f2963c5e00a68b1598da5ecbf5728a479d0b55423de338d083d6e1e
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=4932,4896,559292,284812&retmode=xml
  locator: Exact taxon records and species/strain context
  accessed_at: '2026-10-19T23:42:20Z'
  support: supports
  summary: Species4932/4896 and reference strains559292/284812 resolve to the recorded
    budding- and fission-yeast names.
  snapshot_sha256: 065df56c039e8e774a1bb654361ee8e43bcfc85dfc16676e8bd78dfa1f900060
- evidence_id: IPR001698
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001698/
  locator: metadata accession, name and type
  accessed_at: '2026-10-19T23:42:28Z'
  support: supports
  summary: 'Current InterPro family: F-actin-capping protein subunit beta.'
  snapshot_sha256: df864a54e42ec02945e439401150bf5c6a71e2fe76397f382c85f2194c99b90d
- evidence_id: IPR001837
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001837/
  locator: metadata accession, name and type
  accessed_at: '2026-10-19T23:42:28Z'
  support: supports
  summary: 'Current InterPro family: Adenylate cyclase-associated CAP.'
  snapshot_sha256: b6a7f27ac2d060972b4bd1efa375eb3a79a71a52bcdd6d9981b117b8b3bc3d41
- evidence_id: IPR002189
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002189/
  locator: metadata accession, name and type
  accessed_at: '2026-10-19T23:42:29Z'
  support: supports
  summary: 'Current InterPro family: F-actin-capping protein subunit alpha.'
  snapshot_sha256: cad430581ce4bd6bc04dfb239f994dbdff85d1e9978b29dcb19753639cc9fb80
- evidence_id: IPR004000
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004000/
  locator: metadata accession, name and type
  accessed_at: '2026-10-19T23:42:29Z'
  support: supports
  summary: 'Current InterPro family: Actin family.'
  snapshot_sha256: 353427570f0d1c3842a14f7737374f68e9dd70a98b09cf9fc2a8e8c86062edca
- evidence_id: IPR006789
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006789/
  locator: metadata accession, name and type
  accessed_at: '2026-10-19T23:42:29Z'
  support: supports
  summary: 'Current InterPro family: Actin-related protein 2/3 complex subunit 5.'
  snapshot_sha256: 19f0985b91fb7114d142083d9af263cb2ccc14a1f63dbcf980fca4641650835d
- evidence_id: IPR007188
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007188/
  locator: metadata accession, name and type
  accessed_at: '2026-10-19T23:42:29Z'
  support: supports
  summary: 'Current InterPro family: Actin-related protein 2/3 complex subunit 2.'
  snapshot_sha256: eeb3fb965de48a92013aafde43e9f902a3ab23e388577c98d92e74a8a80d258b
- evidence_id: IPR007204
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007204/
  locator: metadata accession, name and type
  accessed_at: '2026-10-19T23:42:30Z'
  support: supports
  summary: 'Current InterPro family: Actin-related protein 2/3 complex subunit 3.'
  snapshot_sha256: e9ad815196e4c3c264cb69a9fb97db0de5b59d8ba123f8b4f16affe6c58dfb15
- evidence_id: IPR015505
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR015505/
  locator: metadata accession, name and type
  accessed_at: '2026-10-19T23:42:30Z'
  support: supports
  summary: 'Current InterPro family: Coronin.'
  snapshot_sha256: 6c879f6aa8a5d94e8a2f86cfb3179eec5d2f9597513e12eb3b134a1c14736e5d
- evidence_id: IPR039959
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039959/
  locator: metadata accession, name and type
  accessed_at: '2026-10-19T23:42:30Z'
  support: supports
  summary: 'Current InterPro family: Fimbrin/Plastin.'
  snapshot_sha256: 14c90c39dfa026428772c576e2db8bba7bc071c01b6449463ca22f50845d8ec6
- evidence_id: ip-O59945
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/O59945/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:21Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: 8b90ca930311587eba08c4aae640978f61076c9fa9ed91de1f40f4846f1d6c14
- evidence_id: ip-P13517
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P13517/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:24Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: 0234297e8b631aaac197146090cd980bc75dece99b80fe4aeba24c5019a45b37
- evidence_id: ip-P15891
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P15891/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:20Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: bb8b7bf4241b46a12b67e92e6a66f73e949c819c440dd3ff5730a85762fe4a74
- evidence_id: ip-P17555
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P17555/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:28Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: 9bfc02ddad75430930425880d38ddf419536be158d40399678af896d0ca2a630
- evidence_id: ip-P28495
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P28495/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:23Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: a94f731803dd01ac99781ffc7fc4e5409661fb2bda293565bc651bf583ea316b
- evidence_id: ip-P32381
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P32381/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:20Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: 97ab1769a1aab4f6c2f6ed83e93953af44bafe56dee7d1ad9a1549fea1d25431
- evidence_id: ip-P32599
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P32599/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:21Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: ee9ed8f23beb323c12265834751f07c325a3250abe036e49c45f1f9d68920153
- evidence_id: ip-P40518
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P40518/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:26Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: 0636876abab9add76f07936c22cf05b933fcf662e9364c9189ec667e5dcb6e5d
- evidence_id: ip-P53731
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P53731/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:28Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: 0e4cc8db7ec5139a24f7f2525ceba424d37af8c1cad84807e757bbd682a147f6
- evidence_id: ip-P60010
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P60010/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:20Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: e2fd8224573c7bc6dda61f6b2f1ad5b6bd3b8f9a076b9ba9256bae55264017e8
- evidence_id: ip-Q05933
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q05933/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:27Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: ed189b84a588b6c77b43fdf49e49d003e43eeb67c804b5d1b878eb4d670dcfba
- evidence_id: ip-Q06440
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q06440/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:28Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: 9806b4f78c9545415b25462c1c50de706cc28ec08603712b6e5531171e40bfe3
- evidence_id: ip-Q08641
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q08641/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:21Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: b00e69de1e60f2fe4595918cea11af1b2eff1b5b92d1c3d5f49042eaeafbe746
- evidence_id: ip-Q9HGP5
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q9HGP5/?page_size=200
  locator: All results; next=null
  accessed_at: '2026-10-19T23:42:24Z'
  support: supports
  summary: Complete integrated-family/domain match list inspected for the selected
    representative. Family-level grounding matches where assigned; broad domains alone
    do not establish exact Abp1/Abp140 whole-component identity.
  snapshot_sha256: fee85d8c8a14fc4aaddc41726fefd506813dcedf1fd776a0d01eb766e0fb2f55
- evidence_id: doi-2006
  kind: database
  reference: https://api.crossref.org/works/10.1091/mbc.E06-04-0282
  locator: message DOI/title and bibliographic metadata
  accessed_at: '2026-10-19T23:42:30Z'
  support: supports
  summary: Exact DOI and title verified against the cited article.
  snapshot_sha256: 39afe4b79a321eba87573c904ff703301b4ce175a2f3e9bf16d45b8d526b18e0
- evidence_id: doi-2011
  kind: database
  reference: https://api.crossref.org/works/10.1083/jcb.201009028
  locator: message DOI/title and bibliographic metadata
  accessed_at: '2026-10-19T23:42:30Z'
  support: supports
  summary: Exact DOI and title verified against the cited article.
  snapshot_sha256: 040475c5679117b91339adec6d9c222fbcb21d361cf44324d10fffd2f3c87684
- evidence_id: doi-2015
  kind: database
  reference: https://api.crossref.org/works/10.1083/jcb.201502025
  locator: message DOI/title and bibliographic metadata
  accessed_at: '2026-10-19T23:42:30Z'
  support: supports
  summary: Exact DOI and title verified against the cited article.
  snapshot_sha256: 707cc1b1eeece4ea09c114b44e4701ea647e85a38d0bec5052f22fe5e0abe48b
- evidence_id: doi-2018
  kind: database
  reference: https://api.crossref.org/works/10.7554/eLife.35685
  locator: message DOI/title and bibliographic metadata
  accessed_at: '2026-10-19T23:42:30Z'
  support: supports
  summary: Exact DOI and title verified against the cited article.
  snapshot_sha256: 17b22efeb1b22ef260cc2716f331de54ebb808672b877733ca8b01c83367ed1f
- evidence_id: doi-2015b
  kind: database
  reference: https://api.crossref.org/works/10.1128/MCB.00811-15
  locator: message DOI/title and bibliographic metadata
  accessed_at: '2026-10-19T23:42:30Z'
  support: supports
  summary: Exact DOI and title verified against the cited article.
  snapshot_sha256: 0ceda618db69d91a4354f6ac1c05b2231c3166ab58ffff565f7956816804ba29
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=30299253,26351139,26124291,21402786,16914523&retmode=xml
  locator: Exact article identifiers
  accessed_at: '2026-10-19T23:42:41Z'
  support: supports
  summary: Cited PubMed records inspected for article identifiers and bibliographic
    correspondence.
  snapshot_sha256: 43ff8472e0042383cb08a5b39a4aab5ce38c6eaae382b48f7fba27da3643019e
- evidence_id: paper2006
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1635378/?pdf=1
  locator: Full Results, Discussion and Methods; Figures1–4
  accessed_at: '2026-10-20T03:32:35.499576Z'
  support: supports
  summary: Results distinguish strict from partial localizers; morphology, cytoplasmic
    location, slow turnover and refeeding response support the record. Methods identify
    the reporter and strain context. Reserve function remains a hypothesis; Scp1 residence
    is not established.
  snapshot_sha256: a481d871aa8c0c9bfc1cb85dcdad030be760907514d9605418094a89a9c50a13
- evidence_id: paper2011
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3063145/fullTextXML
  locator: Glucose-catabolism Results, Figure4 caption and experimental context
  accessed_at: '2026-10-19T23:42:41Z'
  support: supports
  summary: Figure4 and accompanying Results support the two pathway-level edges. Glucose
    metabolism is required in tested perturbations; ATP replenishment is neither necessary
    nor sufficient. The downstream molecular signal is unresolved.
  snapshot_sha256: 3348da0258b33ad5667521e834646aed6edf72e305ce8ffacb34560002dbd65e
- evidence_id: paper2015
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4494004/fullTextXML
  locator: Actin-body Results; Figures6–7; Discussion
  accessed_at: '2026-10-19T23:42:41Z'
  support: supports
  summary: Figure6 and Results support fission-yeast Fim1/Acp2 localization and distinguish
    excluded polarity proteins. The text inconsistently uses Aap1 and App1; the record
    appropriately retains reporter identity as unresolved.
  snapshot_sha256: 5d18449e993f7d0ceab30dd777686f38c74dfe1d5c9b1568988e4d40ecd9d064
- evidence_id: paper2018
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6177259/fullTextXML
  locator: Cell-fate Results, Figure5 and supplement1, permissions
  accessed_at: '2026-10-19T23:42:41Z'
  support: supports
  summary: Individual-cell fate observations support growth-arrested rather than exclusively
    quiescent scope. Figure5 supplement1 caption and permissions match the hosted
    image and CC BY4.0 licence.
  snapshot_sha256: 5b48bab44f99443eb870596f81f4fa6ea9a7d50cfe9a540ce678e9eb8b41ae74
- evidence_id: paper2015b
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4609741/
  locator: Primary abstract
  accessed_at: '2026-10-19T23:42:41Z'
  support: supports
  summary: The abstract supports heterogeneous stationary-phase actin organization;
    it is used only for that bounded context.
  snapshot_sha256: 7eb03901fc83dab65633f0172be833b803a55445b5aa5a05b5c5e60ee7f84176
- evidence_id: image
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6177259.1/elife-35685-fig5-figsupp1.jpg
  locator: Figure5 supplement1 original JPEG; all panels
  accessed_at: '2026-10-19T23:42:20Z'
  support: supports
  summary: Viewed all three panels. PanelA depicts actin, panelB proteasome localization
    and panelC cell volume. Hosted bytes and SHA256 match the download; image MD5
    matches official version metadata.
  snapshot_sha256: 9e19d13e1ff55ea63391b6398cb9950b60c7ff0f0b61695660676dbfa20a3e61
- evidence_id: image-version
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6177259.1/PMC6177259.1.json
  locator: Article identifiers, license_code, media_urls
  accessed_at: '2026-10-20T03:32:35.608772Z'
  support: supports
  summary: Official metadata identifies PMC6177259 version1, exact DOI/PMID, CC BY
    and the matching image MD5.
  snapshot_sha256: 732857340580aab01088d55f7c8afe09b4ef48d21d2ab460dbfa483f5220eb7f
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/actin_body.yaml
  locator: Entire file plus both actin_body history events
  accessed_at: '2026-10-20T03:36:51Z'
  support: context_only
  summary: Read all eleven component classes, fourteen examples, two edges, species
    distributions, image and six discussions. Historical access notes describe earlier
    curation; full2006 Methods were recovered during this review. PROPOSED is preserved.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/actin_body.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-20T03:35:57.906104Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/actin_body.yaml'
  snapshot_sha256: 3f17d6e041329171e04d0edd3742910b58c4bc6fd0806ef03e15340ded89065b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/actin_body.yaml --out
    /private/tmp/cellstructure-batch2-20261019-52rdp0/actin-body/strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-20T03:35:59.626510Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/actin_body.yaml\
    \ --out /private/tmp/cellstructure-batch2-20261019-52rdp0/actin-body/strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch2-20261019-52rdp0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch2-20261019-52rdp0/actin-body/strict.tsv"
  snapshot_sha256: 31e5e42a799da2e761a60aeb9c8b7b02ae9d104765ac8fc866ef5dc8e4ae1fbe
- evidence_id: target-resolver-coverage
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/actin_body.yaml; exact collect() scope; reports/curie_check.tsv
  accessed_at: '2026-10-19T23:41:41.324461Z'
  support: supports
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
  summary: All36 CURIE-shaped target scalars returned OK; HTTP URLs and prose inspected
    separately.
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
  topic: Exact actin-body identity and relation types
  outcome: supported
  summary: An actin-rich assembly is distinct from patches, cables and protein monomers.
    is-a anatomical structure and part-of cytoskeleton/cytoplasm are appropriate.
    Later single-cell observations justify the cautious growth-arrested definition.
  target_ids:
  - GO:0099079
  evidence_ids:
  - go
  - paper2006
  - paper2018
  - record
- assessment_id: components
  area: completeness
  topic: Eleven classes and partial membership
  outcome: supported
  summary: The localization inventory preserves strict/partial overlap, species-specific
    observations, unknown essentiality and absent stoichiometric reconstruction. Scp1
    and displaced polarity factors are correctly excluded.
  target_ids:
  - GO:0099079
  evidence_ids:
  - paper2006
  - paper2015
  - record
- assessment_id: grounding
  area: grounding
  topic: Nine family groundings and two label-only components
  outcome: supported
  summary: All assigned InterPro families match their exemplars. Abp1 domain architecture
    and the broader Abp140 methyltransferase family are not substituted for precise
    whole-component identities.
  target_ids:
  - GO:0099079
  evidence_ids:
  - proteins
  - IPR001698
  - IPR001837
  - IPR002189
  - IPR004000
  - IPR006789
  - IPR007188
  - IPR007204
  - IPR015505
  - IPR039959
  - ip-O59945
  - ip-P13517
  - ip-P15891
  - ip-P17555
  - ip-P28495
  - ip-P32381
  - ip-P32599
  - ip-P40518
  - ip-P53731
  - ip-P60010
  - ip-Q05933
  - ip-Q06440
  - ip-Q08641
  - ip-Q9HGP5
- assessment_id: examples
  area: scope
  topic: Species and reference-strain examples
  outcome: supported
  summary: Fourteen reviewed sequence exemplars are explicitly illustrative. Conditional
    species distributions do not assert universal occurrence or that reference stocks
    were directly imaged.
  target_ids:
  - GO:0099079
  evidence_ids:
  - proteins
  - taxa
  - paper2006
  - paper2015
  - paper2018
  - record
- assessment_id: mechanism
  area: graph
  topic: Two glucose-metabolism disassembly edges
  outcome: supported
  summary: Both edges match the assigned Figure4 perturbation evidence. The graph
    does not identify a downstream metabolite or mistake ATP replenishment for basal
    ATP requirements.
  target_ids:
  - GO:0099079
  evidence_ids:
  - paper2011
  - record
- assessment_id: function
  area: completeness
  topic: Reserve hypothesis and cell-fate limits
  outcome: supported
  summary: No established storage function is asserted. Heterogeneous cell fates and
    stationary-phase actin organizations remain explicit; body presence is not treated
    as a diagnostic of viable quiescence.
  target_ids:
  - GO:0099079
  evidence_ids:
  - paper2006
  - paper2018
  - paper2015b
  - record
- assessment_id: image
  area: provenance
  topic: Hosted microscopy and licence
  outcome: supported
  summary: Checksum, exact version, authorship, species, panel assignments and CC
    BY4.0 permissions match. Cell-volume measurements are not presented as actin-body
    dimensions.
  target_ids:
  - GO:0099079
  evidence_ids:
  - image
  - image-version
  - paper2018
  - record
- assessment_id: discussion
  area: completeness
  topic: Six discussions and native status
  outcome: supported
  summary: Open family, reporter-identity, reserve-function and metabolic-signal questions
    remain bounded. No unsupported protein is silently added. Historical figure correction
    is retained; no trait or physical-measurement claim is made.
  target_ids:
  - GO:0099079
  evidence_ids:
  - record
  - paper2011
  - paper2015
findings: []
actions: []
limitations:
- Localization is not a complete stoichiometric reconstruction or proof of essentiality.
- The fission-yeast Aap1/App1 reporter correspondence, exact label-only protein families
  and proposed reserve function remain unresolved as acknowledged in the record.
- No inference is made about all growth-arrested cells, universal survival or the
  identity of the downstream metabolic signal.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The actual review start is the timestamp of the delegated inspect artifact; coordinating
  review subsequently recovered full2006 Methods and verified hosted microscopy.
- Initial focused validator invocations encountered a default-cache permission failure;
  successful reruns used the existing writable cache. No record bytes changed.
- The explicit user request authorizes saving clean reviews. Scientific status, history
  and generated pages remain unchanged.
```
