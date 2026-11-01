# Kinetoplast scientific review

- Review: 20261022T042549Z-kinetoplast-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:58:36Z
- Finished UTC: 2026-10-22T04:25:49Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Kinetoplast identity, DNA/KAP organization, comparative scope and explicitly nonmechanistic network graph are supported; exact class grounding, individual formation requirements and source-body limits remain stated.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph claims and completeness.

Selection: Target 3 of batch43, strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0020023 | data/structures/nucleoid/kinetoplast.yaml | maintained | kinetoplast |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0020023 | Focused validator passed. |
| Focused native strict | passed | True | GO:0020023 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0020023 | Focused check passed; scientific claims assessed separately. |
| Focused native verify | passed | True | GO:0020023 | Focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0020023 | No expression-module claim is maintained. |
| Claim-level scientific review | passed | True | GO:0020023 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0020023 | 11 of 11 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0020023 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0020023 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0020023 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0020023 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0020023 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact mitochondrial DNA-containing region

identity: supported. Targets: GO:0020023.

GO0020023 and SL0150 support the region identity and mitochondrial parthood. kDNA-network synonyms are established contextual usage in the cited review, not a new claim that a purified DNA polymer is a whole mitochondrion.

### Two DNA classes and broad KAP cohort

grounding: supported. Targets: GO:0020023.

Minicircles, maxicircles and DNA-organizing proteins are supported. Label-only DNA context and multi-family KAP cohort avoid forcing one taxon protein or broad domain into an exact class identifier. KAP1–4 are real source-supported names in the broad comparative scope; they are not asserted as a complete T.brucei gene inventory.

### Formation necessity remains unresolved

grounding: unknown. Targets: GO:0020023.

All three components use UNKNOWN; no functional or replication phenotype is silently converted into universal formation necessity. Individual KAP depletion outcomes and DNA-copy distributions differ by organism.

### Comparative scope and explicit model organism

scope: supported. Targets: GO:0020023.

The record acknowledges architectural diversity and COMMON Kinetoplastea. The interlocked disk model, copy-number context and canonical microscopy example are trypanosomatid/T.brucei-specific; presence is not a newly calculated census.

### Explicitly nonmechanistic network organization

graph: supported. Targets: GO:0020023.

The catenation/condensation edges summarize organization and KAP contributions. NONMECHANISTIC and its scope note correctly withhold replication enzymology and a resolved compaction pathway. TAC machinery is contextual and need not be forced into the DNA-bound constituent inventory.

### Complete record including reinstated historical names

completeness: supported. Targets: GO:0020023.

The current KAP symbols are evaluated against current sources even though an older history event says an arbitrary list was removed. No new protein example is guessed without an exact taxon pairing. No confirmed defect was established within the declared evidence scope.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/nucleoid/kinetoplast.yaml; Entire maintained target including history, evidence, components, graphs and discussions | context_only | All maintained fields were read; past curation actions are historical provenance, not additional experimental evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Exact identity, constituent, formation-necessity and graph contracts | context_only | Source-neutral families differ from species proteins and domains; functional requirement is distinct from formation necessity. |
| root43-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005739,GO:0006338,GO:0008695,GO:0009334,GO:0016590,GO:0020023,GO:0031010,GO:1990204; Complete id/name/active/definition/synonym fields; direct typed parent child entries for the maintained links. Unrelated child lists are not an exhaustive ontology census. | supports | The eight native GO records support kinetoplast and mitochondrial parthood, the four-protein Hca dioxygenase and oxidoreductase parent/activity, and ACF as an ISWI-type complex with chromatin-remodeling activity. |
| root43-sources-tax5653 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5653; Complete native taxonomy response | supports | ENA verifies Kinetoplastea identity, rank and lineage. |
| root43-sources-tax5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Complete native taxonomy response | supports | ENA verifies Trypanosoma brucei identity, rank and lineage. |
| root43-sources-SL0150 | https://rest.uniprot.org/locations/SL-0150.json; Complete native response, including matrix/mitochondrion parthood | supports | Native SL0150 maps to GO0020023 and describes mitochondrial maxicircle/minicircle network organization. |
| root43-sources-doi-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.E02-08-0525&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | Ogbadoyi2003 MED12802053 DOI10.1091/mbc.E02-08-0525 identifies a TAC linkage across mitochondrial membranes to basal bodies; this is contextual machinery, not the DNA region itself. |
| root43-sources-doi-2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093%2Ffemsre%2Ffuac047&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | Amodeo2023 MED36449697 DOI10.1093/femsre/fuac047 is a secondary review centered on T.brucei and explicitly proposes an updated replication model. |
| root43-sources-doi-3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093%2Fnar%2Fgkz928&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | Cooper2019 MED31665448 DOI10.1093/nar/gkz928 reports391 assembled minicircle classes and predicted/expressed guide RNAs in a defined T.brucei strain, not391 total circles per organelle. |
| root43-sources-doi-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FMCB.01176-10&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | Gluenz2011 MED21173163 DOI10.1128/MCB.01176-10 reports serial-section microscopy and maxicircle/minicircle probes across the duplication cycle. Native MED omitted its PMC field; genuine PMC3067821 was recovered separately. |
| root43-sources-doi-8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-micro-092611-150057&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | Jensen2012 MED22994497 DOI10.1146/annurev-micro-092611-150057 is a review of network structure, replication and segregation. |
| root43-sources-doi-9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1371%2Fjournal.pone.0187516&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | deSouza2017 MED29131838 DOI10.1371/journal.pone.0187516 studies comparative KAP repertoires and distinct localization patterns in symbiont-bearing trypanosomatids. |
| root43-sources-legacy-PMC10719067 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10719067/?report=xml; Complete sec1 including Fig1/2 captions and Table1, sec8 with its two subsections, and sec10; other review sections not read | supports | Amodeo secondary synthesis supports interlocked minicircles/maxicircles, T.brucei sizes and copy numbers, KAP-associated condensation and basal-body/TAC-mediated segregation. Specific KAP functions, basic-protein locations and replication models remain explicitly uncertain. |
| root43-sources-legacy-PMC6868439 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6868439/?report=xml; Complete Results SEC3-1 and SEC3-2 with Fig1 caption; other Results/Methods/supplements not independently read | supports | Cooper primary Results distinguish391 minicircle sequence classes from thousands of copies per network; read-depth estimates give about30 maxicircles and about6000 minicircles in an unreplicated T.brucei network. |
| root43-sources-legacy-PMC5683618 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5683618/?report=xml; Complete Introduction sec001, Results sec013 and sec016 including Fig1/3 captions; other Results/Methods and supplements not read | supports | The primary study supports lineage-variable KAP types: KAP1/2 are not universal, KAP2/3 cluster together, and distinct novel types occur in symbiont-bearing species. KAP4 overlaps kDNA, whereas aKAP23 staining is anterior and does not coincide with DAPI. The broad cohort is not a claim that every named KAP binds or compacts DNA in every species. |
| root43-sources-gluenz2011-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC3067821/?report=xml; Complete Methods sec2/4 and Results sec7/8 including Fig1/2 captions; other sections and image pixels not read | supports | Genuine Gluenz primary body confirms procyclic T.brucei strains, serial thin sections and three-dimensional reconstructions, and five morphological stages of kDNA duplication linked to basal-body and flagellar-pocket organization. |
| schema-result | just validate data/structures/nucleoid/kinetoplast.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/nucleoid/kinetoplast.yaml |
| strict-result | just validate-strict data/structures/nucleoid/kinetoplast.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/kinetoplast-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/nucleoid/kinetoplast.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/kinetoplast-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/kinetoplast-strict.tsv |
| native-kinetoplast-causal-graphs | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/nucleoid/kinetoplast.yaml; Complete focused native report | supports | data/structures/nucleoid/kinetoplast.yaml  (GO:0020023)<br>  kdna_network_kinetoplast_organization	kinetoplast_associated_proteins	HAS_SYMBOLS_NO_EXAMPLES	-&gt;kinetoplast_associated_proteins (PROTEIN: KAP1, KAP2, KAP3, KAP4)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-kinetoplast-verify | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/nucleoid/kinetoplast.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/nucleoid/kinetoplast.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 11 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, supplements, raw experiments, sequence alignments or quantitative taxon census were reanalyzed. Reading scope is specified for each source.
- Jensen2012 and Ogbadoyi2003 were assessed from complete native abstracts. Jensen publisher retrieval returned403. Ogbadoyi genuine legacy body was fetched but not read beyond the already checked abstract.
- No complete inventory of KAP family identities or taxon-paired protein examples was established. KAP1/2 lineage restrictions and aKAP23 non-DNA localization preclude treating every KAP name as a universal compacting subunit.
- Cooper network counts are read-depth estimates for its cultured strain/populations; no whole-Kinetoplastea architectural or copy-number generalization is inferred.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes reviews for all uncovered records, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T042549Z-kinetoplast-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Kinetoplast scientific review
started_at: '2026-10-22T03:58:36Z'
finished_at: '2026-10-22T04:25:49Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Kinetoplast identity, DNA/KAP organization, comparative scope and explicitly
  nonmechanistic network graph are supported; exact class grounding, individual formation
  requirements and source-body limits remain stated.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
  state: working_tree
  inputs:
  - path: .claude/skills/curate-causal-graphs/SKILL.md
    sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
    role: context
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/nucleoid/kinetoplast.yaml
    sha256: e40505c18375c267ebabc32d2b4bd7101c7da9b7bdf1b1549469b8b4a7292f7a
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
- target_id: GO:0020023
  path: data/structures/nucleoid/kinetoplast.yaml
  label: kinetoplast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/kinetoplast.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph claims and completeness.
  selection: Target 3 of batch43, strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0020023
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: just validate data/structures/nucleoid/kinetoplast.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: just validate-strict data/structures/nucleoid/kinetoplast.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/kinetoplast-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-kinetoplast-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/nucleoid/kinetoplast.yaml
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-kinetoplast-causal-graphs
- check_id: native-kinetoplast-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/nucleoid/kinetoplast.yaml
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-kinetoplast-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0020023
  summary: No expression-module claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0020023
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - root43-sources-go
  - root43-sources-tax5653
  - root43-sources-tax5691
  - root43-sources-SL0150
  - root43-sources-doi-1
  - root43-sources-doi-2
  - root43-sources-doi-3
  - root43-sources-doi-5
  - root43-sources-doi-8
  - root43-sources-doi-9
  - root43-sources-legacy-PMC10719067
  - root43-sources-legacy-PMC6868439
  - root43-sources-legacy-PMC5683618
  - root43-sources-gluenz2011-legacy
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0020023
  summary: 11 of 11 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:34Z to
    2026-10-22T01:34:04Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/nucleoid/kinetoplast.yaml
  locator: Entire maintained target including history, evidence, components, graphs
    and discussions
  accessed_at: '2026-10-22T04:09:20Z'
  support: context_only
  summary: All maintained fields were read; past curation actions are historical provenance,
    not additional experimental evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Exact identity, constituent, formation-necessity and graph contracts
  accessed_at: '2026-10-22T04:09:20Z'
  support: context_only
  summary: Source-neutral families differ from species proteins and domains; functional
    requirement is distinct from formation necessity.
- evidence_id: root43-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005739,GO:0006338,GO:0008695,GO:0009334,GO:0016590,GO:0020023,GO:0031010,GO:1990204
  locator: Complete id/name/active/definition/synonym fields; direct typed parent
    child entries for the maintained links. Unrelated child lists are not an exhaustive
    ontology census.
  accessed_at: '2026-10-22T04:03:43.609653Z'
  support: supports
  summary: The eight native GO records support kinetoplast and mitochondrial parthood,
    the four-protein Hca dioxygenase and oxidoreductase parent/activity, and ACF as
    an ISWI-type complex with chromatin-remodeling activity.
  snapshot_sha256: 758170e2adf2bdecccd550d870e811d4aa0171ee8322ea75ccf5c4e3fd84ca83
- evidence_id: root43-sources-tax5653
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5653
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:03:43.610667Z'
  support: supports
  summary: ENA verifies Kinetoplastea identity, rank and lineage.
  snapshot_sha256: 6e467f5ff25d9bd8189b9c916942db46996eee6ad67fa41afd146096c2fb0556
- evidence_id: root43-sources-tax5691
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:03:43.612605Z'
  support: supports
  summary: ENA verifies Trypanosoma brucei identity, rank and lineage.
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: root43-sources-SL0150
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0150.json
  locator: Complete native response, including matrix/mitochondrion parthood
  accessed_at: '2026-10-22T04:03:47.691361Z'
  support: supports
  summary: Native SL0150 maps to GO0020023 and describes mitochondrial maxicircle/minicircle
    network organization.
  snapshot_sha256: a2ff48cddc11468ae130307891a3b1b0593051d67fe6ae0f108861f392d75148
- evidence_id: root43-sources-doi-1
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.E02-08-0525&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:45.772432Z'
  support: supports
  summary: Ogbadoyi2003 MED12802053 DOI10.1091/mbc.E02-08-0525 identifies a TAC linkage
    across mitochondrial membranes to basal bodies; this is contextual machinery,
    not the DNA region itself.
  snapshot_sha256: d4a5d06c3dd0cfb0cb12c35d12037426ea573dd4bc80cc48218e542ffb707d9a
- evidence_id: root43-sources-doi-2
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093%2Ffemsre%2Ffuac047&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:45.875663Z'
  support: supports
  summary: Amodeo2023 MED36449697 DOI10.1093/femsre/fuac047 is a secondary review
    centered on T.brucei and explicitly proposes an updated replication model.
  snapshot_sha256: 4dd435c8a25c9a2e8119cc39381a74901437024ab15966565625236dd2e40ca1
- evidence_id: root43-sources-doi-3
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093%2Fnar%2Fgkz928&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:46.095117Z'
  support: supports
  summary: Cooper2019 MED31665448 DOI10.1093/nar/gkz928 reports391 assembled minicircle
    classes and predicted/expressed guide RNAs in a defined T.brucei strain, not391
    total circles per organelle.
  snapshot_sha256: 51d1adabcdf778a6ce3c998d6bf812fee27da465d9086c53e5be7c089bf9d046
- evidence_id: root43-sources-doi-5
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FMCB.01176-10&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:46.339807Z'
  support: supports
  summary: Gluenz2011 MED21173163 DOI10.1128/MCB.01176-10 reports serial-section microscopy
    and maxicircle/minicircle probes across the duplication cycle. Native MED omitted
    its PMC field; genuine PMC3067821 was recovered separately.
  snapshot_sha256: 5dceac143dcf9815bdf9d0870702d40b2cdb7b5610b822b0e582e5edde6f4d7a
- evidence_id: root43-sources-doi-8
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-micro-092611-150057&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:46.764583Z'
  support: supports
  summary: Jensen2012 MED22994497 DOI10.1146/annurev-micro-092611-150057 is a review
    of network structure, replication and segregation.
  snapshot_sha256: 340bb78f4a61993112a200d3770f34bea810b89b804ee4bcc5a24363e53c75e6
- evidence_id: root43-sources-doi-9
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1371%2Fjournal.pone.0187516&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:46.847334Z'
  support: supports
  summary: deSouza2017 MED29131838 DOI10.1371/journal.pone.0187516 studies comparative
    KAP repertoires and distinct localization patterns in symbiont-bearing trypanosomatids.
  snapshot_sha256: d3a6f36c2994f793c42f0dba3718c5610c2b85b25fdeec0eb7dcdc3f32fe87e6
- evidence_id: root43-sources-legacy-PMC10719067
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10719067/?report=xml
  locator: Complete sec1 including Fig1/2 captions and Table1, sec8 with its two subsections,
    and sec10; other review sections not read
  accessed_at: '2026-10-22T04:04:06.423180Z'
  support: supports
  summary: Amodeo secondary synthesis supports interlocked minicircles/maxicircles,
    T.brucei sizes and copy numbers, KAP-associated condensation and basal-body/TAC-mediated
    segregation. Specific KAP functions, basic-protein locations and replication models
    remain explicitly uncertain.
  snapshot_sha256: de1b1fc91c5edea36fa56bd839fbf411c0ea30666ef6c01f2c62139a39d58840
- evidence_id: root43-sources-legacy-PMC6868439
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6868439/?report=xml
  locator: Complete Results SEC3-1 and SEC3-2 with Fig1 caption; other Results/Methods/supplements
    not independently read
  accessed_at: '2026-10-22T04:04:07.033531Z'
  support: supports
  summary: Cooper primary Results distinguish391 minicircle sequence classes from
    thousands of copies per network; read-depth estimates give about30 maxicircles
    and about6000 minicircles in an unreplicated T.brucei network.
  snapshot_sha256: 108eace7085a89fcd3a46a4e30887df51b3742f6c2e2f59ca9047ac7661859b2
- evidence_id: root43-sources-legacy-PMC5683618
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5683618/?report=xml
  locator: Complete Introduction sec001, Results sec013 and sec016 including Fig1/3
    captions; other Results/Methods and supplements not read
  accessed_at: '2026-10-22T04:04:08.277424Z'
  support: supports
  summary: 'The primary study supports lineage-variable KAP types: KAP1/2 are not
    universal, KAP2/3 cluster together, and distinct novel types occur in symbiont-bearing
    species. KAP4 overlaps kDNA, whereas aKAP23 staining is anterior and does not
    coincide with DAPI. The broad cohort is not a claim that every named KAP binds
    or compacts DNA in every species.'
  snapshot_sha256: e6dcbea8a1557230996679fe599782f7726eaaf1b0398d3b3aa6f56b5722523c
- evidence_id: root43-sources-gluenz2011-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3067821/?report=xml
  locator: Complete Methods sec2/4 and Results sec7/8 including Fig1/2 captions; other
    sections and image pixels not read
  accessed_at: '2026-10-22T04:06:48.391401Z'
  support: supports
  summary: Genuine Gluenz primary body confirms procyclic T.brucei strains, serial
    thin sections and three-dimensional reconstructions, and five morphological stages
    of kDNA duplication linked to basal-body and flagellar-pocket organization.
  snapshot_sha256: fe8185ff4bab6353956f60cafdfd9dfe8bf4e925e1d0fcb770ad98bff08d496d
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/nucleoid/kinetoplast.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:37Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/nucleoid/kinetoplast.yaml'
  snapshot_sha256: 4c774e4ec9f6d9a139c48cdd9a6fd59ff540a7fd835cab264bce9ca4414f714a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/nucleoid/kinetoplast.yaml --out
    /private/tmp/cellstructure-batch43-20261022-u_vlughs/kinetoplast-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:39Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/nucleoid/kinetoplast.yaml\
    \ --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/kinetoplast-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/kinetoplast-strict.tsv"
  snapshot_sha256: 005ba5e089a9c511e3cda34879af4479810304b49a42717b523cb14580d3b737
- evidence_id: native-kinetoplast-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/nucleoid/kinetoplast.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:04:25.601984Z'
  support: supports
  summary: "data/structures/nucleoid/kinetoplast.yaml  (GO:0020023)\n  kdna_network_kinetoplast_organization\t\
    kinetoplast_associated_proteins\tHAS_SYMBOLS_NO_EXAMPLES\t->kinetoplast_associated_proteins\
    \ (PROTEIN: KAP1, KAP2, KAP3, KAP4)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n\
    \     1  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref\
    \ on the node\n     1  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 8676810ab064da164f9b59c268811a6c76f4dbc7dc0297ac3e4089301cd09f4d
- evidence_id: native-kinetoplast-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/nucleoid/kinetoplast.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:04:26.248640Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/nucleoid/kinetoplast.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 11 of 11 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  snapshot_sha256: 173c367ec1621e2a96027e149b5cad9f4db0a86f0a3c916455ce192a9aa5f428
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:05:35Z'
  support: supports
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 8696c0d603149cee93ac200eaa3ed26c84320204285cd22cca542eb1ae7ba572
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:37Z'
  support: supports
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  snapshot_sha256: 98a7952c42add0416633f4dee73ff64331e5c6c4c4c8d707e98a152f04fc5b6d
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:59:14Z'
  support: supports
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:40Z'
  support: supports
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  snapshot_sha256: 00cc5664a9143235d28fb9885fc5c43a8a78c9a9c9f47603b1232e1eddddeac1
assessments:
- assessment_id: identity
  area: identity
  topic: Exact mitochondrial DNA-containing region
  outcome: supported
  target_ids:
  - GO:0020023
  summary: GO0020023 and SL0150 support the region identity and mitochondrial parthood.
    kDNA-network synonyms are established contextual usage in the cited review, not
    a new claim that a purified DNA polymer is a whole mitochondrion.
  evidence_ids:
  - record
  - root43-sources-go
  - root43-sources-SL0150
  - root43-sources-legacy-PMC10719067
  - root43-sources-gluenz2011-legacy
- assessment_id: components
  area: grounding
  topic: Two DNA classes and broad KAP cohort
  outcome: supported
  target_ids:
  - GO:0020023
  summary: Minicircles, maxicircles and DNA-organizing proteins are supported. Label-only
    DNA context and multi-family KAP cohort avoid forcing one taxon protein or broad
    domain into an exact class identifier. KAP1–4 are real source-supported names
    in the broad comparative scope; they are not asserted as a complete T.brucei gene
    inventory.
  evidence_ids:
  - record
  - schema
  - root43-sources-legacy-PMC10719067
  - root43-sources-legacy-PMC6868439
  - root43-sources-legacy-PMC5683618
- assessment_id: necessity
  area: grounding
  topic: Formation necessity remains unresolved
  outcome: unknown
  target_ids:
  - GO:0020023
  summary: All three components use UNKNOWN; no functional or replication phenotype
    is silently converted into universal formation necessity. Individual KAP depletion
    outcomes and DNA-copy distributions differ by organism.
  evidence_ids:
  - record
  - schema
  - root43-sources-legacy-PMC10719067
  - root43-sources-legacy-PMC5683618
- assessment_id: scope
  area: scope
  topic: Comparative scope and explicit model organism
  outcome: supported
  target_ids:
  - GO:0020023
  summary: The record acknowledges architectural diversity and COMMON Kinetoplastea.
    The interlocked disk model, copy-number context and canonical microscopy example
    are trypanosomatid/T.brucei-specific; presence is not a newly calculated census.
  evidence_ids:
  - record
  - root43-sources-tax5653
  - root43-sources-tax5691
  - root43-sources-legacy-PMC10719067
  - root43-sources-legacy-PMC6868439
  - root43-sources-gluenz2011-legacy
- assessment_id: graph
  area: graph
  topic: Explicitly nonmechanistic network organization
  outcome: supported
  target_ids:
  - GO:0020023
  summary: The catenation/condensation edges summarize organization and KAP contributions.
    NONMECHANISTIC and its scope note correctly withhold replication enzymology and
    a resolved compaction pathway. TAC machinery is contextual and need not be forced
    into the DNA-bound constituent inventory.
  evidence_ids:
  - record
  - root43-sources-legacy-PMC10719067
  - root43-sources-legacy-PMC6868439
  - root43-sources-legacy-PMC5683618
  - root43-sources-doi-1
- assessment_id: coverage
  area: completeness
  topic: Complete record including reinstated historical names
  outcome: supported
  target_ids:
  - GO:0020023
  summary: The current KAP symbols are evaluated against current sources even though
    an older history event says an arbitrary list was removed. No new protein example
    is guessed without an exact taxon pairing. No confirmed defect was established
    within the declared evidence scope.
  evidence_ids:
  - record
  - root43-sources-legacy-PMC10719067
  - root43-sources-legacy-PMC5683618
  - root43-sources-gluenz2011-legacy
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, supplements, raw experiments, sequence alignments or quantitative
  taxon census were reanalyzed. Reading scope is specified for each source.
- Jensen2012 and Ogbadoyi2003 were assessed from complete native abstracts. Jensen
  publisher retrieval returned403. Ogbadoyi genuine legacy body was fetched but not
  read beyond the already checked abstract.
- No complete inventory of KAP family identities or taxon-paired protein examples
  was established. KAP1/2 lineage restrictions and aKAP23 non-DNA localization preclude
  treating every KAP name as a universal compacting subunit.
- Cooper network counts are read-depth estimates for its cultured strain/populations;
  no whole-Kinetoplastea architectural or copy-number generalization is inferred.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorizes reviews for all uncovered records, including honest zero-finding
  bundles.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
