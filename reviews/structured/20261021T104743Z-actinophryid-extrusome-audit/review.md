# Organelle identity, composition and evidence review

- Review: 20261021T104743Z-actinophryid-extrusome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:27:02Z
- Finished UTC: 2026-10-21T10:47:43Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The local organelle identity, cargo, physical fusion graph and bounded pharmacology are supported. One provisional minor frequency-evidence gap remains; molecular formation requirements and abstract-only sources remain explicit.

## Scope And Provenance

Entire single record with exact authority identities, declared source-reading scopes, protein checks where applicable and component/function/graph boundaries.

Selection: Target 5 in batch twenty; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:actinophryid_extrusome | data/structures/membrane_organelle/actinophryid_extrusome.yaml | maintained | actinophryid extrusome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | cellstructuremech:actinophryid_extrusome | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Native protein causal-graphs | passed | True | cellstructuremech:actinophryid_extrusome | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Focused native schema | passed | True | cellstructuremech:actinophryid_extrusome | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:actinophryid_extrusome | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:actinophryid_extrusome | 10 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | cellstructuremech:actinophryid_extrusome | No expression-module or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | cellstructuremech:actinophryid_extrusome | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:actinophryid_extrusome | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:actinophryid_extrusome | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:actinophryid_extrusome | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:actinophryid_extrusome | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:actinophryid_extrusome | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Bounded actinophryid organelle identity

identity: supported. Targets: cellstructuremech:actinophryid_extrusome.

The local structure is a secretory organelle rather than GP40 alone, a ciliate toxicyst or a parasite digestive vacuole. Its broader intracellular membrane-bounded parent is appropriate; no Golgi-origin claim is added.

### Observed cargo and bounding membrane

grounding: supported. Targets: cellstructuremech:actinophryid_extrusome.

GP40 storage and bead-adhesion/ingestion assays support cargo membership; the membrane-donation observation supports a physical bounding membrane. Unreviewed gp40 isoforms are not treated as experimentally localized exemplars. Label-only groundings and the open lipid-chemistry question preserve unknown specificity.

### Formation requirements remain unknown

evidence: unknown. Targets: cellstructuremech:actinophryid_extrusome.

Functional adhesion, pharmacological inhibition of prey capture and membrane donation do not test de novo assembly after loss of a specific GP40 isoform or lipid species. The collective bounding membrane is constitutional; individual molecular requirements remain unresolved.

### A physical fusion mechanism at its source scope

graph: supported. Targets: cellstructuremech:actinophryid_extrusome.

The graph represents observed granule expansion/fusion, membrane donation and prey enclosure, with source-level electron-microscopy evidence described in the abstract. It adds no unmeasured molecular fusion machinery or upstream channel inventory. The two adhesion sources support the separate function.

### Abundance in cultures versus taxonomic frequency

scope: concern. Targets: cellstructuremech:actinophryid_extrusome.

The species example is supported. The COMMON field is justified in the record by numerous extrusomes within examined cells, whereas the schema defines COMMON as occurrence in most members. The statement limiting all-strain generality does not supply a taxon-frequency observation.

### Bounded record-level coverage

completeness: supported. Targets: cellstructuremech:actinophryid_extrusome.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Additional exhaustive component inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. This bounded review does not assert exhaustive literature completeness.

## Findings

### F1: Separate cellular abundance from encoded taxonomic frequency

minor / open / provisional; issue key: actinophryid-extrusome-presence-abundance.

The distribution row uses COMMON while its note and cited publisher Summary describe numerous organelles under the axopodial membrane in studied cultures. The schema defines COMMON as presence in most taxon members. A within-cell count does not itself support that frequency claim. The species-level canonical example is already supported. Full1998 text remains unread, so this is a bounded evidence-placement gap rather than a claim of demonstrated strain variability.

## Recommended Actions And Acceptance Checks

### A1

Retain the canonical example; either provide evidence for the encoded taxon-wide frequency and explain it in the distribution note, or remove the unsupported frequency row. Do not substitute a guessed VARIABLE value.

- The justification for COMMON concerns occurrence among taxon members, not organelle abundance within a cell.
- Species/culture adhesion and membrane-donation evidence remain preserved.
- Use separately authorized guarded curation, append-only history, native focused/identifier/product checks and regeneration.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/actinophryid_extrusome.yaml; Entire maintained YAML including history, all evidence notes, components, functions, graph edges and discussions | context_only | All maintained fields were read. No scientific edit or mapping-status promotion is made. |
| policy | docs/CURATION.md; Exact identity, claim-level evidence, material versus localization grounding, and component assembly-essentiality contract | context_only | Family identity, concrete protein examples and structure membership are separate; activity and viability are not by themselves formation assays. Optional inventories are not mandatory. |
| root20-sources-extrusome-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020020,GO:0030141,GO:0043231; Complete returned term identities, definitions and relevant relationship fields | supports | Native intracellular membrane-bounded organelle is a valid broader parent. Secretory granule specifies Golgi origin and food vacuole specifies a parasite digesting host cytoplasm; those terms cannot be adopted solely by similar wording. |
| root20-sources-ols-exact-actinophryid-extrusome | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;queryFields=label,synonym&amp;rows=100&amp;q=actinophryid%20extrusome; Exact query URL and entire response numFound/docs | supports | The exact GO label/synonym query for actinophryid extrusome returns zero entries. This is a bounded query, not an exhaustive assertion about all possible terminology. |
| root20-sources-NCBITaxon-238771 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/238771; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Actinophrys sol at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root20-sources-doi-10.1016_j.ejop.2007.11.001 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.ejop.2007.11.001; Complete native bibliographic fields and abstract | supports | Native MED record identifies Ca(2+)- and glycoconjugates-dependent prey capture in the heliozoon Actinophrys sol. (Kakuta S, Suzaki T., 2008), PMID 18178392, DOI 10.1016/j.ejop.2007.11.001. Complete returned abstract and bibliographic fields were read; full-body extent is stated separately. |
| root20-sources-doi-10.1078_1434-4610-00041 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1078/1434-4610-00041; Complete native bibliographic fields and abstract | supports | Native MED record identifies Involvement of a 40-kDa glycoprotein in food recognition, prey capture, and induction of phagocytosis in the protozoon Actinophrys sol. (Sakaguchi M, Murakami H, Suzaki T., 2001), PMID 11401035, DOI 10.1078/1434-4610-00041. Complete returned abstract and bibliographic fields were read; full-body extent is stated separately. |
| root20-sources-kakuta2008-aam | https://da.lib.kobe-u.ac.jp/da/kernel/90000974/90000974.pdf; Accepted-manuscript printed pages2-9: Summary, complete Introduction, culture/prey-capture Methods and complete Results/Discussion. References and figure pixels not audited. | supports | The accepted manuscript describes amorphous electron-dense actinophryid granules and their prey-capture context. Its direct assays measure prey capture under calcium/drug/lectin treatments. Proposed L-type channels, calmodulin and gp40 involvement are not proof of granule-resident molecular machinery; ionophore-mediated granule depletion and the exact ConA target remain hypotheses. |
| root20-sources-sakaguchi1998-publisher | https://link.springer.com/article/10.1007/BF01279469; Complete Abs1-section Summary; abstract/access page, not full article | supports | The publisher Summary describes numerous extrusomes beneath axopodial membrane, isolated extrusome preparations adhering to prey, and a heat-extracted adhesive fraction. It supports localization and adhesion in the experimental system; abundance per cell is distinct from frequency across a taxon. |
| root20-sources-sakaguchi1998-crossref | https://api.crossref.org/works/10.1007/BF01279469; Title, DOI, authors and publication date | supports | Native publisher-deposited Crossref metadata confirms the exact title, authors,1998 publication and DOI for the adhesion study. |
| root20-sources-hausmann1982-crossref | https://api.crossref.org/works/10.1002/cm.970020103; Exact title/authors/date/DOI and complete deposited abstract | supports | The complete publisher-deposited abstract describes extrusomes expanding/fusing with one another and the plasma membrane during formation of a funnel-shaped feeding pseudopodium, supplying food-vacuole membrane. The earlier adhesion phase is distinguished and does not itself establish the function of expelled granule contents. |
| root20-sources-UniProtKB-B2NIF0 | https://rest.uniprot.org/uniprotkb/B2NIF0.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is B2NIF0, UniProtKB unreviewed (TrEMBL), organism taxon 238771. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root20-sources-UniProtKB-B2NIF1 | https://rest.uniprot.org/uniprotkb/B2NIF1.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is B2NIF1, UniProtKB unreviewed (TrEMBL), organism taxon 238771. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root20-sources-IPR000757 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000757/; Native accession, name, type, hierarchy and relevant description | supports | The active integrated match is a domain or homologous superfamily, not an exact GP40 adhesive-protein family. Its generic carbohydrate-related annotation is not direct evidence of enzymatic function for this granule cargo. |
| root20-sources-IPR013320 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013320/; Native accession, name, type, hierarchy and relevant description | supports | The active integrated match is a domain or homologous superfamily, not an exact GP40 adhesive-protein family. Its generic carbohydrate-related annotation is not direct evidence of enzymatic function for this granule cargo. |
| root20-sources-interpro-B2NIF0 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B2NIF0/?page_size=200; All results, member identity and terminal pagination | supports | The complete two-entry integrated match set contains IPR000757 domain and IPR013320 homologous superfamily; next=null. The two native sequence entries are unreviewed gp40-1 and gp40-2 submissions, not isoform-specific localization experiments. |
| root20-sources-interpro-B2NIF1 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B2NIF1/?page_size=200; All results, member identity and terminal pagination | supports | The complete two-entry integrated match set contains IPR000757 domain and IPR013320 homologous superfamily; next=null. The two native sequence entries are unreviewed gp40-1 and gp40-2 submissions, not isoform-specific localization experiments. |
| root20-sources-IPR050546 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050546/; Actual source-access response, not article content | context_only | The candidate family cross-reference returns410. It was not adopted by the record and is not used as an active exact identity. |
| root20-sources-hausmann1982-publisher | https://onlinelibrary.wiley.com/doi/10.1002/cm.970020103; Actual source-access response, not article content | context_only | The publisher request returned403; only the complete publisher-deposited Crossref abstract was read. |
| root20-sources-sakaguchi2001-doi | https://doi.org/10.1078/1434-4610-00041; Actual source-access response, not article content | context_only | The DOI route returns a redirect document, not an article body. |
| root20-sources-sakaguchi2001-publisher-resolved | https://www.sciencedirect.com/science/article/pii/S1434461004700413; Actual source-access response, not article content | context_only | The actual DOI-supplied publisher PII route returned403; the full2001 paper was not read. |
| native-verify | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml --verify; Exact focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml --causal-graphs; Exact focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/actinophryid_extrusome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/actinophryid_extrusome.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/actinophryid_extrusome.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/actinophryid_extrusome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/actinophryid_extrusome.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/actinophryid_extrusome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/actinophryid_extrusome-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/actinophryid_extrusome.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 10 of11 collected target identifiers returned OK in this fresh base resolver run. Residuals: cellstructuremech:actinophryid_extrusome: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| presence-enum | src/cellstructuremech/schema/cellstructuremech.yaml; PresenceEnum.COMMON, lines1094–1095 | context_only | COMMON means presence in most taxon members, with losses as exceptions; this is distinct from number of granules within a cell. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The1998 study was read only as the complete publisher Summary; the1982 paper only as the complete publisher-deposited abstract. The2001 GP40 study was read through native complete MED abstract, not full body.
- The2008 accepted-manuscript body was read at pages2-9; no microscopy pixels, raw assays or numerical reanalysis is claimed. Its original brackish-water culture does not establish broad taxonomic frequency.
- Exact GO and GP40-family checks are limited to the declared native queries and complete two-protein match sets. Historical search statements are not recertified.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization; identifier transport and label-adapter limits remain explicit.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for every uncovered target, including a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104743Z-actinophryid-extrusome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Organelle identity, composition and evidence review
started_at: '2026-10-21T10:27:02Z'
finished_at: '2026-10-21T10:47:43Z'
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
summary: The local organelle identity, cargo, physical fusion graph and bounded pharmacology
  are supported. One provisional minor frequency-evidence gap remains; molecular formation
  requirements and abstract-only sources remain explicit.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/actinophryid_extrusome.yaml
    sha256: 4b0f4ea17353cf6db5e343ef4a88ddc1458185fdcb508b74ca4fa8685421d0ea
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
  - path: scripts/score_causal_graphs.py
    sha256: 5ffe450c5b37c3dc3b0e62672caf0d99b358c8249fcc98a8c4fc7d78e8cd0d2f
    role: context
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: cellstructuremech:actinophryid_extrusome
  path: data/structures/membrane_organelle/actinophryid_extrusome.yaml
  label: actinophryid extrusome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/actinophryid_extrusome.yaml
    role: maintained scientific record
scope:
  description: Entire single record with exact authority identities, declared source-reading
    scopes, protein checks where applicable and component/function/graph boundaries.
  selection: Target 5 in batch twenty; exact sorted uncovered path at frozen fresh-main
    revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:actinophryid_extrusome
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml
    --verify
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: just validate data/structures/membrane_organelle/actinophryid_extrusome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: just validate-strict data/structures/membrane_organelle/actinophryid_extrusome.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/actinophryid_extrusome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  summary: 10 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - record
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  summary: No expression-module or transcriptomic inference is made by this structural
    review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - root20-sources-extrusome-go
  - root20-sources-ols-exact-actinophryid-extrusome
  - root20-sources-NCBITaxon-238771
  - root20-sources-doi-10.1016_j.ejop.2007.11.001
  - root20-sources-doi-10.1078_1434-4610-00041
  - root20-sources-kakuta2008-aam
  - root20-sources-sakaguchi1998-publisher
  - root20-sources-sakaguchi1998-crossref
  - root20-sources-hausmann1982-crossref
  - root20-sources-UniProtKB-B2NIF0
  - root20-sources-UniProtKB-B2NIF1
  - root20-sources-IPR000757
  - root20-sources-IPR013320
  - root20-sources-interpro-B2NIF0
  - root20-sources-interpro-B2NIF1
  - root20-sources-IPR050546
  - root20-sources-hausmann1982-publisher
  - root20-sources-sakaguchi2001-doi
  - root20-sources-sakaguchi2001-publisher-resolved
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/actinophryid_extrusome.yaml
  locator: Entire maintained YAML including history, all evidence notes, components,
    functions, graph edges and discussions
  accessed_at: '2026-10-21T10:39:35Z'
  support: context_only
  summary: All maintained fields were read. No scientific edit or mapping-status promotion
    is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, claim-level evidence, material versus localization grounding,
    and component assembly-essentiality contract
  accessed_at: '2026-10-21T10:39:35Z'
  support: context_only
  summary: Family identity, concrete protein examples and structure membership are
    separate; activity and viability are not by themselves formation assays. Optional
    inventories are not mandatory.
- evidence_id: root20-sources-extrusome-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020020,GO:0030141,GO:0043231
  locator: Complete returned term identities, definitions and relevant relationship
    fields
  accessed_at: '2026-10-21T10:28:23.560564Z'
  support: supports
  summary: Native intracellular membrane-bounded organelle is a valid broader parent.
    Secretory granule specifies Golgi origin and food vacuole specifies a parasite
    digesting host cytoplasm; those terms cannot be adopted solely by similar wording.
  snapshot_sha256: 52360e66a2072c8a88c1486d45ead7b0ef962c0fd0c7412e51838129100abe9b
- evidence_id: root20-sources-ols-exact-actinophryid-extrusome
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&queryFields=label,synonym&rows=100&q=actinophryid%20extrusome
  locator: Exact query URL and entire response numFound/docs
  accessed_at: '2026-10-21T10:33:53.059033Z'
  support: supports
  summary: The exact GO label/synonym query for actinophryid extrusome returns zero
    entries. This is a bounded query, not an exhaustive assertion about all possible
    terminology.
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
- evidence_id: root20-sources-NCBITaxon-238771
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/238771
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:28:23.593668Z'
  support: supports
  summary: Native ENA taxonomy identifies Actinophrys sol at species rank. Only this
    taxon's identity and names are asserted by this row, not occurrence or experimental
    stock identity.
  snapshot_sha256: 2e46c5c00b4f08e19a36b6d73764c1d4521ef34535eaac7eb2cedc3445cb4eb1
- evidence_id: root20-sources-doi-10.1016_j.ejop.2007.11.001
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.ejop.2007.11.001
  locator: Complete native bibliographic fields and abstract
  accessed_at: '2026-10-21T10:28:24.493560Z'
  support: supports
  summary: Native MED record identifies Ca(2+)- and glycoconjugates-dependent prey
    capture in the heliozoon Actinophrys sol. (Kakuta S, Suzaki T., 2008), PMID 18178392,
    DOI 10.1016/j.ejop.2007.11.001. Complete returned abstract and bibliographic fields
    were read; full-body extent is stated separately.
  snapshot_sha256: 7faabf1b3473276ab7cd7d5c7130297637b8e381af8f64093791a52a58f5e615
- evidence_id: root20-sources-doi-10.1078_1434-4610-00041
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1078/1434-4610-00041
  locator: Complete native bibliographic fields and abstract
  accessed_at: '2026-10-21T10:28:24.310702Z'
  support: supports
  summary: Native MED record identifies Involvement of a 40-kDa glycoprotein in food
    recognition, prey capture, and induction of phagocytosis in the protozoon Actinophrys
    sol. (Sakaguchi M, Murakami H, Suzaki T., 2001), PMID 11401035, DOI 10.1078/1434-4610-00041.
    Complete returned abstract and bibliographic fields were read; full-body extent
    is stated separately.
  snapshot_sha256: f3fc45f4c3328ddd069fba345a65cc243c855eb409fed816179ccb68c8e50593
- evidence_id: root20-sources-kakuta2008-aam
  kind: primary_source
  reference: https://da.lib.kobe-u.ac.jp/da/kernel/90000974/90000974.pdf
  locator: 'Accepted-manuscript printed pages2-9: Summary, complete Introduction,
    culture/prey-capture Methods and complete Results/Discussion. References and figure
    pixels not audited.'
  accessed_at: '2026-10-21T10:28:27.455440Z'
  support: supports
  summary: The accepted manuscript describes amorphous electron-dense actinophryid
    granules and their prey-capture context. Its direct assays measure prey capture
    under calcium/drug/lectin treatments. Proposed L-type channels, calmodulin and
    gp40 involvement are not proof of granule-resident molecular machinery; ionophore-mediated
    granule depletion and the exact ConA target remain hypotheses.
  snapshot_sha256: 9ed27a66e3f0262060eb10274d9e2f2add0018dc4491636886e9ffe847202551
- evidence_id: root20-sources-sakaguchi1998-publisher
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/BF01279469
  locator: Complete Abs1-section Summary; abstract/access page, not full article
  accessed_at: '2026-10-21T10:28:28.040698Z'
  support: supports
  summary: The publisher Summary describes numerous extrusomes beneath axopodial membrane,
    isolated extrusome preparations adhering to prey, and a heat-extracted adhesive
    fraction. It supports localization and adhesion in the experimental system; abundance
    per cell is distinct from frequency across a taxon.
  snapshot_sha256: cd9ba00dd64f189a51ad5d66399dd9dbe2c0932ee49c6010b0e074cd219ca294
- evidence_id: root20-sources-sakaguchi1998-crossref
  kind: database
  reference: https://api.crossref.org/works/10.1007/BF01279469
  locator: Title, DOI, authors and publication date
  accessed_at: '2026-10-21T10:29:14.066247Z'
  support: supports
  summary: Native publisher-deposited Crossref metadata confirms the exact title,
    authors,1998 publication and DOI for the adhesion study.
  snapshot_sha256: ac91d6102dc4dd8aed4d9f84c0b480029008a83bc34fa8af126f7a4d3ad151c1
- evidence_id: root20-sources-hausmann1982-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1002/cm.970020103
  locator: Exact title/authors/date/DOI and complete deposited abstract
  accessed_at: '2026-10-21T10:28:26.492900Z'
  support: supports
  summary: The complete publisher-deposited abstract describes extrusomes expanding/fusing
    with one another and the plasma membrane during formation of a funnel-shaped feeding
    pseudopodium, supplying food-vacuole membrane. The earlier adhesion phase is distinguished
    and does not itself establish the function of expelled granule contents.
  snapshot_sha256: 23ee7d7ac2e25bb5b1335a60658c77d34dc17e5f8501b3624ec75b11a55f6a45
- evidence_id: root20-sources-UniProtKB-B2NIF0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/B2NIF0.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:28:23.595869Z'
  support: supports
  summary: The primary accession is B2NIF0, UniProtKB unreviewed (TrEMBL), organism
    taxon 238771. Exact name/gene tokens, evidence-qualified location comments and
    linked publication metadata were inspected. Database identity is not independently
    a formation-necessity experiment.
  snapshot_sha256: 89519e99dc7c08c3d797401a8cb7e4056afc4fe558a62d2f9d25904efa269b6f
- evidence_id: root20-sources-UniProtKB-B2NIF1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/B2NIF1.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:28:24.466549Z'
  support: supports
  summary: The primary accession is B2NIF1, UniProtKB unreviewed (TrEMBL), organism
    taxon 238771. Exact name/gene tokens, evidence-qualified location comments and
    linked publication metadata were inspected. Database identity is not independently
    a formation-necessity experiment.
  snapshot_sha256: 527dea7c98d06606040a8141560bf03237c2e3ff4c6f434737a4ad7a070d7290
- evidence_id: root20-sources-IPR000757
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000757/
  locator: Native accession, name, type, hierarchy and relevant description
  accessed_at: '2026-10-21T10:28:27.113077Z'
  support: supports
  summary: The active integrated match is a domain or homologous superfamily, not
    an exact GP40 adhesive-protein family. Its generic carbohydrate-related annotation
    is not direct evidence of enzymatic function for this granule cargo.
  snapshot_sha256: 57b8272533921c9703879d38d4e62e9448412f969928ff6f3dd3031d7698c019
- evidence_id: root20-sources-IPR013320
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013320/
  locator: Native accession, name, type, hierarchy and relevant description
  accessed_at: '2026-10-21T10:28:27.749813Z'
  support: supports
  summary: The active integrated match is a domain or homologous superfamily, not
    an exact GP40 adhesive-protein family. Its generic carbohydrate-related annotation
    is not direct evidence of enzymatic function for this granule cargo.
  snapshot_sha256: 1a6d786fbc2d08458a4cafec72c3ce8f2a87b5a8e6369196333aab188899ca56
- evidence_id: root20-sources-interpro-B2NIF0
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B2NIF0/?page_size=200
  locator: All results, member identity and terminal pagination
  accessed_at: '2026-10-21T10:28:28.004281Z'
  support: supports
  summary: The complete two-entry integrated match set contains IPR000757 domain and
    IPR013320 homologous superfamily; next=null. The two native sequence entries are
    unreviewed gp40-1 and gp40-2 submissions, not isoform-specific localization experiments.
  snapshot_sha256: 303b28811f2395af46f74a4eb26f655cfb018abe1a42dc179fbd81c808a75c79
- evidence_id: root20-sources-interpro-B2NIF1
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B2NIF1/?page_size=200
  locator: All results, member identity and terminal pagination
  accessed_at: '2026-10-21T10:28:28.156202Z'
  support: supports
  summary: The complete two-entry integrated match set contains IPR000757 domain and
    IPR013320 homologous superfamily; next=null. The two native sequence entries are
    unreviewed gp40-1 and gp40-2 submissions, not isoform-specific localization experiments.
  snapshot_sha256: a5b6e22df882dbb3241e4397bebf8f17bee67695f0f512d1c98eb529a99c959a
- evidence_id: root20-sources-IPR050546
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050546/
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:28:28.127999Z'
  support: context_only
  summary: The candidate family cross-reference returns410. It was not adopted by
    the record and is not used as an active exact identity.
  snapshot_sha256: 7b43a6c3facfb712608446516580f235ab94c0b0239442015a3394b2015e87b7
- evidence_id: root20-sources-hausmann1982-publisher
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/10.1002/cm.970020103
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:29:14.143607Z'
  support: context_only
  summary: The publisher request returned403; only the complete publisher-deposited
    Crossref abstract was read.
  snapshot_sha256: 6bb5bc70cb995f4c4c02253481c5000ba3ac3cdb4ce25ba88c5510efbee4e1fd
- evidence_id: root20-sources-sakaguchi2001-doi
  kind: authority
  reference: https://doi.org/10.1078/1434-4610-00041
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:31:55.819700Z'
  support: context_only
  summary: The DOI route returns a redirect document, not an article body.
  snapshot_sha256: af0bc473a0bc8c5b92d483d24499bf78e93474227d955ff506210877e1fdf016
- evidence_id: root20-sources-sakaguchi2001-publisher-resolved
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S1434461004700413
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:33:52.228187Z'
  support: context_only
  summary: The actual DOI-supplied publisher PII route returned403; the full2001 paper
    was not read.
  snapshot_sha256: 330b52128485b92a9573533ee7aabc1f7422af976de59cf0865f462e492778ff
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml
    --verify
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:28:46.575246Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml
    --causal-graphs
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:28:47.163710Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/actinophryid_extrusome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:27:04Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/actinophryid_extrusome.yaml'
  snapshot_sha256: f283da71c50d7bdf1e0303f1cbd193969bf973e59fae2b85974b5fd42c13febd
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/actinophryid_extrusome.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/actinophryid_extrusome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:27:06Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/actinophryid_extrusome.yaml\
    \ --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/actinophryid_extrusome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/actinophryid_extrusome-strict.tsv"
  snapshot_sha256: 348a6534927dddda743ae0253c0b1312637cda41ec3f39902596d9d294b7ab5a
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/actinophryid_extrusome.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:39:36Z'
  support: supports
  summary: '10 of11 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: cellstructuremech:actinophryid_extrusome: SKIPPED; resolved by
    evidence record. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: presence-enum
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: PresenceEnum.COMMON, lines1094–1095
  accessed_at: '2026-10-21T10:42:57.446994Z'
  support: context_only
  summary: COMMON means presence in most taxon members, with losses as exceptions;
    this is distinct from number of granules within a cell.
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: identity
  area: identity
  topic: Bounded actinophryid organelle identity
  outcome: supported
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  summary: The local structure is a secretory organelle rather than GP40 alone, a
    ciliate toxicyst or a parasite digestive vacuole. Its broader intracellular membrane-bounded
    parent is appropriate; no Golgi-origin claim is added.
  evidence_ids:
  - root20-sources-extrusome-go
  - root20-sources-ols-exact-actinophryid-extrusome
  - root20-sources-kakuta2008-aam
  - root20-sources-hausmann1982-crossref
- assessment_id: composition
  area: grounding
  topic: Observed cargo and bounding membrane
  outcome: supported
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  summary: GP40 storage and bead-adhesion/ingestion assays support cargo membership;
    the membrane-donation observation supports a physical bounding membrane. Unreviewed
    gp40 isoforms are not treated as experimentally localized exemplars. Label-only
    groundings and the open lipid-chemistry question preserve unknown specificity.
  evidence_ids:
  - root20-sources-doi-10.1078_1434-4610-00041
  - root20-sources-hausmann1982-crossref
  - root20-sources-kakuta2008-aam
  - root20-sources-UniProtKB-B2NIF0
  - root20-sources-UniProtKB-B2NIF1
  - root20-sources-IPR000757
  - root20-sources-IPR013320
  - root20-sources-interpro-B2NIF0
  - root20-sources-interpro-B2NIF1
- assessment_id: necessity
  area: evidence
  topic: Formation requirements remain unknown
  outcome: unknown
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  summary: Functional adhesion, pharmacological inhibition of prey capture and membrane
    donation do not test de novo assembly after loss of a specific GP40 isoform or
    lipid species. The collective bounding membrane is constitutional; individual
    molecular requirements remain unresolved.
  evidence_ids:
  - root20-sources-doi-10.1078_1434-4610-00041
  - root20-sources-hausmann1982-crossref
  - root20-sources-kakuta2008-aam
  - policy
- assessment_id: function-graph
  area: graph
  topic: A physical fusion mechanism at its source scope
  outcome: supported
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  summary: The graph represents observed granule expansion/fusion, membrane donation
    and prey enclosure, with source-level electron-microscopy evidence described in
    the abstract. It adds no unmeasured molecular fusion machinery or upstream channel
    inventory. The two adhesion sources support the separate function.
  evidence_ids:
  - root20-sources-hausmann1982-crossref
  - root20-sources-doi-10.1078_1434-4610-00041
  - root20-sources-sakaguchi1998-publisher
  - root20-sources-kakuta2008-aam
- assessment_id: scope
  area: scope
  topic: Abundance in cultures versus taxonomic frequency
  outcome: concern
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  summary: The species example is supported. The COMMON field is justified in the
    record by numerous extrusomes within examined cells, whereas the schema defines
    COMMON as occurrence in most members. The statement limiting all-strain generality
    does not supply a taxon-frequency observation.
  evidence_ids:
  - root20-sources-sakaguchi1998-publisher
  - root20-sources-kakuta2008-aam
  - root20-sources-NCBITaxon-238771
  - record
  - policy
  - presence-enum
- assessment_id: coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Additional exhaustive component inventories, numerical
    properties, images, traits and expanded mechanisms are optional. No verbatim quotation
    requires repair, and no status or history rewrite is proposed. This bounded review
    does not assert exhaustive literature completeness.
  evidence_ids:
  - record
  - policy
  - root20-sources-extrusome-go
  - root20-sources-ols-exact-actinophryid-extrusome
  - root20-sources-NCBITaxon-238771
  - root20-sources-doi-10.1016_j.ejop.2007.11.001
  - root20-sources-doi-10.1078_1434-4610-00041
  - root20-sources-kakuta2008-aam
  - root20-sources-sakaguchi1998-publisher
  - root20-sources-sakaguchi1998-crossref
  - root20-sources-hausmann1982-crossref
  - root20-sources-UniProtKB-B2NIF0
  - root20-sources-UniProtKB-B2NIF1
  - root20-sources-IPR000757
  - root20-sources-IPR013320
  - root20-sources-interpro-B2NIF0
  - root20-sources-interpro-B2NIF1
  - root20-sources-IPR050546
  - root20-sources-hausmann1982-publisher
  - root20-sources-sakaguchi2001-doi
  - root20-sources-sakaguchi2001-publisher-resolved
findings:
- finding_id: F1
  issue_key: actinophryid-extrusome-presence-abundance
  category: scope
  severity: minor
  status: open
  certainty: provisional
  title: Separate cellular abundance from encoded taxonomic frequency
  description: The distribution row uses COMMON while its note and cited publisher
    Summary describe numerous organelles under the axopodial membrane in studied cultures.
    The schema defines COMMON as presence in most taxon members. A within-cell count
    does not itself support that frequency claim. The species-level canonical example
    is already supported. Full1998 text remains unread, so this is a bounded evidence-placement
    gap rather than a claim of demonstrated strain variability.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  field_paths:
  - taxonomic_distribution[taxon_id=NCBITaxon:238771].presence
  - taxonomic_distribution[taxon_id=NCBITaxon:238771].note
  evidence_ids:
  - root20-sources-sakaguchi1998-publisher
  - root20-sources-kakuta2008-aam
  - root20-sources-NCBITaxon-238771
  - record
  - policy
  - presence-enum
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/actinophryid_extrusome.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; docs/record-reviews.md:Verdict And Severity
  native_severity: minor
  normalization_reason: A bounded provenance or scope correction preserves the structure
    identity.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/actinophryid_extrusome.yaml
    role: maintained scientific record
  description: Retain the canonical example; either provide evidence for the encoded
    taxon-wide frequency and explain it in the distribution note, or remove the unsupported
    frequency row. Do not substitute a guessed VARIABLE value.
  acceptance_checks:
  - The justification for COMMON concerns occurrence among taxon members, not organelle
    abundance within a cell.
  - Species/culture adhesion and membrane-donation evidence remain preserved.
  - Use separately authorized guarded curation, append-only history, native focused/identifier/product
    checks and regeneration.
limitations:
- The1998 study was read only as the complete publisher Summary; the1982 paper only
  as the complete publisher-deposited abstract. The2001 GP40 study was read through
  native complete MED abstract, not full body.
- The2008 accepted-manuscript body was read at pages2-9; no microscopy pixels, raw
  assays or numerical reanalysis is claimed. Its original brackish-water culture does
  not establish broad taxonomic frequency.
- Exact GO and GP40-family checks are limited to the declared native queries and complete
  two-protein match sets. Historical search statements are not recertified.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches
  and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization;
  identifier transport and label-adapter limits remain explicit.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized one review for every uncovered target, including
  a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
