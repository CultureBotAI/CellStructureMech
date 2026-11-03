# Phagolysosome scientific review

- Review: 20261022T031046Z-phagolysosome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:58:54Z
- Finished UTC: 2026-10-22T03:10:46Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact phagolysosome identity, hierarchy and Dictyostelium maturation are supported. One major concerns the expanded defining molecular/taxon scope; two minors concern the graph's mechanistic scope label and acidification assay attribution.

## Scope And Provenance

Entire single target and its explicitly frozen boundary neighbors: native identity/hierarchy, collective molecular material and individual necessity, taxon/examples, all functions/edges, evidence, history and discussions. Source read extents are exact per evidence locator.

Selection: Batch37 exact path-ordered target9; initial native inspection/schema/strict passed on fresh f97b1abe before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032010 | data/structures/membrane_organelle/phagolysosome.yaml | maintained | phagolysosome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032010 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032010 | Focused validator passed. |
| Native protein-node graph coverage | passed | True | GO:0032010 | Zero GENE_OR_PROTEIN nodes; scientific edge scope independently assessed. |
| Protein-instance verification applicability | not_applicable | False | GO:0032010 | No individual protein accession or GENE_OR_PROTEIN node is asserted in the target. |
| Expression-module applicability | not_applicable | False | GO:0032010 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0032010 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0032010 | 13 of 15 collected target identifiers returned OK. PMID:12388753: UNREACHABLE; Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity, DOI and declared PMC/null status. This separately resolves citation identity after bulk eutils414; article-body scope is stated independently.; PMID:16926386: UNREACHABLE; Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity, DOI and declared PMC/null status. This separately resolves citation identity after bulk eutils414; article-body scope is stated independently. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0032010 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032010 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032010 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032010 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0032010 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact organelle and membrane/lumen boundaries

identity: supported. Targets: GO:0032010.

The exact GO0032010 identity, both parents, related synonyms and two has_part links are supported by native typed relations and definitions. Whole organelle, membrane and lumen remain distinct in the frozen boundary set.

### Collective bilayer constitution

grounding: supported. Targets: GO:0032010.

The label-only lipid row is a collective material constituent, with no whole-membrane CURIE used as chemical grounding. Membrane boundaries are positive observations in the primary work. Generic component naming does not make the mature membrane a different identity; stages have variable molecular composition.

### Formation requirement of individual constituents

evidence: unknown. Targets: GO:0032010.

A lipid boundary is constitutive of the membrane-bounded structure. Neither the generic ESSENTIAL designation nor component detection establishes that each lipid or protein species is experimentally necessary for formation. No individual requirement is inferred from the retained primary assays.

### Supported Dictyostelium maturation context

scope: supported. Targets: GO:0032010.

Tax44689 correctly names the experimental species. The canonical bead-phagosome time course and qualitative COMMON occurrence in this species are supported, including membrane remodeling and luminal phases. Purified organelle/proteomic observations are not universal per-cell frequency measurements or direct functional assays of every detected component.

### Expanded defining mechanism and taxon scope

evidence: concern. Targets: GO:0032010.

The added definition presents strongly acidified, V-ATPase-maintained, hydrolase/protease/lysozyme-rich digestive organization across Dictyostelium, Entamoeba and ciliates. The declared GO source contains only the maturation/marker definition. Inspected studies directly analyze Dictyostelium with stage-dependent remodeling and do not establish that full defining extension across the named taxa.

### Supported process association versus mechanism resolution

graph: concern. Targets: GO:0032010.

Broad phagocytosis/maturation associations are defensible: native phagocytosis includes lysosomal delivery and maturation ends in the phagolysosome. The displayed graph, however, consists of constituent/parthood edges followed by whole-structure mediates-process associations. It does not depict a molecular causal transition or actor explaining the stated assembly/functional mechanism.

### Measured time profiles versus synthesized acidification context

evidence: concern. Targets: GO:0032010.

Gotthardt2002 directly measured trafficking, component profiles and hydrolase localization; its Discussion synthesizes proton-pump acidification from earlier work. The function evidence note should distinguish that context from the directly dissected time profiles.

### Bounded source tiers and unchanged status

provenance: supported. Targets: GO:0032010.

Every maintained claim was assessed against native identities, the inspected literature scope and frozen boundaries. Positive identity and constituent observations are separated from experimental formation requirements and unsupported extensions. No scientific edit, status promotion or persistence is implied.

## Findings

### F1: Bound the expanded definition to demonstrated taxa and mechanisms

major / open / confirmed; issue key: phagolysosome-expanded-definition-scope.

The first ontology-based clause is exact, but the appended molecular and taxonomic description is not contained in the cited GO entry. The primary evidence establishes staged Dictyostelium phagosome behavior; it does not demonstrate the entire added cross-taxon mechanistic definition. Supported digestion/acidification in the studied context should be retained, but not silently generalized into a defining molecular program for all listed microbial groups.

### F2: Match the graph scope to its descriptive edges

minor / open / confirmed; issue key: phagolysosome-graph-scope-label.

The graph is labeled MECHANISTIC and titled an assembly and functional mechanism, but its edges give material/parthood and generic whole-structure process associations. The primary papers contain mechanisms worth separately curating, yet those actors and transitions are not represented in this graph.

### F3: Qualify the source scope of the acidification note

minor / open / confirmed; issue key: phagolysosome-acidification-source-method-scope.

functions[1].evidence[1].notes attributes distinct luminal-acidification behavior to the Gotthardt2002 dissection. Its Methods/Results do not present a direct luminal-pH assay; acidification is synthesized in Discussion from earlier work, and the2006 Fig4C pH scheme is explicitly adapted from macropinocytosis. Trafficking-phase measurements are genuine and should be retained.

## Recommended Actions And Acceptance Checks

### A1

Retain the exact ontology boundary/maturation definition and move supported extra biology into explicitly taxon-, stage- and source-qualified fields. Remove or qualify unestablished extensions, or add directly inspected evidence that actually supports each retained mechanism and taxon.

- Native GO text is distinguished from curator-added biology.
- No comparative mechanism or fixed molecular inventory is inferred solely from Dictyostelium time profiles.
- Correct organelle identity, boundary hierarchy and experimentally supported maturation remain intact.
- Native schema, strict, identifier, graph and history checks pass after separately authorized curation.

### A2

Use NONMECHANISTIC with a precise descriptive scope note and aligned title, or separately curate a source-backed mechanistic path without inventing obligatory actors.

- Declared scope and title describe the actual edges.
- Correct identities, parthood and broad process associations are preserved.
- Native schema, strict, identifier, graph and history checks pass after separately authorized curation.

### A3

State that the study directly dissected trafficking/component phases and discussed acidification using earlier evidence, or cite an inspected direct pH study for a measurement claim.

- Measured trafficking phases are distinguished from review/synthesis-level pH context.
- The note does not imply a direct pH assay in the cited2002 experiment.
- Native schema, strict, identifier, graph and history checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/phagolysosome.yaml; Entire maintained YAML including all graphs, evidence, history and discussion | context_only | The entire target was read; scientific content and PROPOSED status remain unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent lines391–448 and causal graph/node/scope contracts | context_only | A label-only collective lipid constituent differs from a whole-membrane CURIE used as chemical grounding. Essentiality concerns formation, not merely localization or catalytic function. Graph scope must match what its edges explain. |
| neighbor-phagolysosome_membrane | data/structures/membrane_organelle/phagolysosome_membrane.yaml; Entire frozen boundary neighbor; maintained context only | context_only | The complete adjacent boundary record was read and frozen to distinguish whole organelle, membrane and lumen identities. It is not independent experimental evidence and its other scientific assertions are not certified by this review. |
| neighbor-phagolysosome_vesicle_lumen | data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml; Entire frozen boundary neighbor; maintained context only | context_only | The complete adjacent boundary record was read and frozen to distinguish whole organelle, membrane and lumen identities. It is not independent experimental evidence and its other scientific assertions are not certified by this review. |
| phagolysosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032010,GO:0061474,GO:0106174,GO:0005767,GO:0045335,GO:0030670,GO:0097013,GO:0032009,GO:0006909,GO:0090382,GO:0031410,GO:0030659; Complete twelve native entries, definitions, synonyms and typed children; especially0032010/0061474/0106174/0005767/0045335/0030670/0006909/0090382 | supports | The active phagolysosome and membrane entries give only the maturation/late-marker and bilayer definitions, respectively. GO0032010 is a direct is_a child of GO0005767 and GO0045335 and has0061474/0106174 part_of children; GO0030670 lists0061474 is_a. The process terms describe broad phagocytosis and maturation ending in the phagolysosome, not a detailed taxon-specific mechanism. |
| phagolysosome-agent-SL0206 | https://rest.uniprot.org/locations/SL-0206.json; Complete native entry including nested hierarchy, definition, synonyms and GO mapping | supports | SL0206 identifies the generic phagosome as a membrane-bounded phagocytic compartment, maps to GO0045335 and places it under cytoplasmic vesicle. |
| phagolysosome-agent-tax44689 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689; Complete native taxId/scientificName/rank/lineage | supports | ENA confirms Dictyostelium discoideum44689 at species rank. The experimental Ax2 culture is specified separately in the primary studies. |
| phagolysosome-agent-PMID-12388753 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12388753%20AND%20SRC%3AMED; Unique MED identity and complete primary abstract | supports | PMID12388753/DOI10.1091/mbc.e02-04-0206 identifies Gotthardt2002. Complete abstract reports D. discoideum latex-bead time courses, staged hydrolase/glycoprotein delivery and recycling, and accompanying Rab7/SNARE profiles. |
| phagolysosome-agent-PMID-16926386 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A16926386%20AND%20SRC%3AMED; Unique MED identity and complete primary abstract | supports | PMID16926386/DOI10.1074/mcp.m600113-mcp200 identifies Gotthardt2006. Complete abstract reports D. discoideum temporal2D-gel/MS analysis and separate G-protein mutant uptake assays. |
| phagolysosome-agent-gotthardt2002-numeric | https://pmc.ncbi.nlm.nih.gov/articles/129962/; Genuine PMC129962 HTML: complete Introductionsec1, Methodssec2, Resultssec12 and Discussionsec20, including embedded Figures1–7 captions; no pixels or supplemental datasets. | supports | The actual study uses D. discoideum Ax2 at22C in HL5c, latex-bead pulse/chase and yeast comparison. Intact isolated phagosomes retain boundary membranes; membrane and luminal constituents are delivered/retrieved in distinct phases. Lysosomal Lmp glycoproteins are explicitly CD36/LIMPII-family, while Vti1/Vamp7/Rab7 profiles accompany trafficking; this is not a cross-protist demonstration of LAMP-mediated membrane protection or Nramp-dependent efflux. Acidification is associated with proton-pump delivery, not a universally constant pH stage. |
| phagolysosome-agent-gotthardt2006-unige-pdf | https://access.archive-ouverte.unige.ch/access/metadata/eae2ae90-5a91-4330-85a9-04fa245d5d63/download; Genuine author-hosted publisher PDF, exact title/DOI p2228; Introduction/Methods pp2228–2230; Results/Discussion pp2230,2236–2237,2239–2241 including Fig4C and5/6 captions. TableI images, other figure pixels and supplementary data not reanalyzed. | supports | The primary study profiles D. discoideum Ax2 phagosomes by2D gels/MS across six pulse/chase time points, including carbonate extraction of membrane preparations. Temporal groups support digestive and recycling phases, while the text cautions that a linear maturation scheme is an oversimplification. Fig4C explicitly borrows the acidification/neutralization scheme from a macropinocytosis model. This is not a direct comparative demonstration of all added defining molecular traits in Entamoeba or ciliates. |
| schema-result | just validate data/structures/membrane_organelle/phagolysosome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/phagolysosome.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/phagolysosome.yaml --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagolysosome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/phagolysosome.yaml --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagolysosome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagolysosome-strict.tsv |
| phagolysosome-causal-graphs | /private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/phagolysosome.yaml; Complete native read-only GENE_OR_PROTEIN coverage log | supports | Native coverage command exited0 and reports zero GENE_OR_PROTEIN nodes; no accession-specific protein verification is applicable. |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/phagolysosome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 15 collected target identifiers returned OK. PMID:12388753: UNREACHABLE; Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity, DOI and declared PMC/null status. This separately resolves citation identity after bulk eutils414; article-body scope is stated independently.; PMID:16926386: UNREACHABLE; Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity, DOI and declared PMC/null status. This separately resolves citation identity after bulk eutils414; article-body scope is stated independently. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- The two Gotthardt studies directly examine D. discoideum Ax2. Their introductory discussion of other systems and shared factors does not prove the full added defining program in Entamoeba or ciliates. The limitation is evidence scope, not proof those organisms lack any individual feature.
- The2002 genuine main body was read completely at declared sections. The2006 body was read only at the explicitly listed pages; TableI images, figure pixels, supplementary tables and raw proteomics were not reanalyzed. The Fig4C pH model is explicitly adapted from macropinocytosis and not a universal phagolysosome pH measurement.
- Label-only collective bilayer constitution is accepted independently of unknown formation necessity for individual molecular species. No optional enzyme or trafficking-protein row is required merely because the cited papers identify it.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes clean reviews without invented findings. Parent owns finalization and persistence. Five same-base full-corpus gates are staged for guarded finalization.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T031046Z-phagolysosome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Phagolysosome scientific review
started_at: '2026-10-22T02:58:54Z'
finished_at: '2026-10-22T03:10:46Z'
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
summary: Exact phagolysosome identity, hierarchy and Dictyostelium maturation are
  supported. One major concerns the expanded defining molecular/taxon scope; two minors
  concern the graph's mechanistic scope label and acidification assay attribution.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/phagolysosome.yaml
    sha256: 1aa7bcc22c4b8a9bb65c69fad0c276e2446d28534b72a8abf930ed0e64c70e1e
    role: target
  - path: data/structures/membrane_organelle/phagolysosome_membrane.yaml
    sha256: 7f7e638a499bf7a56376a0f51d9de765fe0e3b9f7563bdb2ee13e9d332306b32
    role: context
  - path: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    sha256: 096069e6ecc9f33d640dfb9621fa69dedfab50cb9a9f08e6186e9583a823c319
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
- target_id: GO:0032010
  path: data/structures/membrane_organelle/phagolysosome.yaml
  label: phagolysosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome.yaml
    role: maintained scientific record
scope:
  description: 'Entire single target and its explicitly frozen boundary neighbors:
    native identity/hierarchy, collective molecular material and individual necessity,
    taxon/examples, all functions/edges, evidence, history and discussions. Source
    read extents are exact per evidence locator.'
  selection: Batch37 exact path-ordered target9; initial native inspection/schema/strict
    passed on fresh f97b1abe before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032010
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032010
  command: just validate data/structures/membrane_organelle/phagolysosome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032010
  command: just validate-strict data/structures/membrane_organelle/phagolysosome.yaml
    --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagolysosome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: causal-graphs
  name: Native protein-node graph coverage
  status: passed
  required: true
  target_ids:
  - GO:0032010
  command: /private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/phagolysosome.yaml
  exit_code: 0
  summary: Zero GENE_OR_PROTEIN nodes; scientific edge scope independently assessed.
  evidence_ids:
  - phagolysosome-causal-graphs
- check_id: protein-applicability
  name: Protein-instance verification applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0032010
  summary: No individual protein accession or GENE_OR_PROTEIN node is asserted in
    the target.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0032010
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0032010
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-phagolysosome_membrane
  - neighbor-phagolysosome_vesicle_lumen
  - phagolysosome-agent-go
  - phagolysosome-agent-SL0206
  - phagolysosome-agent-tax44689
  - phagolysosome-agent-PMID-12388753
  - phagolysosome-agent-PMID-16926386
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0032010
  summary: '13 of 15 collected target identifiers returned OK. PMID:12388753: UNREACHABLE;
    Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity,
    DOI and declared PMC/null status. This separately resolves citation identity after
    bulk eutils414; article-body scope is stated independently.; PMID:16926386: UNREACHABLE;
    Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity,
    DOI and declared PMC/null status. This separately resolves citation identity after
    bulk eutils414; article-body scope is stated independently. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - phagolysosome-agent-PMID-12388753
  - phagolysosome-agent-PMID-16926386
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032010
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0032010
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0032010
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0032010
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0032010
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
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/phagolysosome.yaml
  locator: Entire maintained YAML including all graphs, evidence, history and discussion
  accessed_at: '2026-10-22T03:05:54Z'
  support: context_only
  summary: The entire target was read; scientific content and PROPOSED status remain
    unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent lines391–448 and causal graph/node/scope contracts
  accessed_at: '2026-10-22T03:05:54Z'
  support: context_only
  summary: A label-only collective lipid constituent differs from a whole-membrane
    CURIE used as chemical grounding. Essentiality concerns formation, not merely
    localization or catalytic function. Graph scope must match what its edges explain.
- evidence_id: neighbor-phagolysosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/phagolysosome_membrane.yaml
  locator: Entire frozen boundary neighbor; maintained context only
  accessed_at: '2026-10-22T03:05:54Z'
  support: context_only
  summary: The complete adjacent boundary record was read and frozen to distinguish
    whole organelle, membrane and lumen identities. It is not independent experimental
    evidence and its other scientific assertions are not certified by this review.
- evidence_id: neighbor-phagolysosome_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
  locator: Entire frozen boundary neighbor; maintained context only
  accessed_at: '2026-10-22T03:05:54Z'
  support: context_only
  summary: The complete adjacent boundary record was read and frozen to distinguish
    whole organelle, membrane and lumen identities. It is not independent experimental
    evidence and its other scientific assertions are not certified by this review.
- evidence_id: phagolysosome-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032010,GO:0061474,GO:0106174,GO:0005767,GO:0045335,GO:0030670,GO:0097013,GO:0032009,GO:0006909,GO:0090382,GO:0031410,GO:0030659
  locator: Complete twelve native entries, definitions, synonyms and typed children;
    especially0032010/0061474/0106174/0005767/0045335/0030670/0006909/0090382
  accessed_at: '2026-10-22T02:59:56.802595Z'
  support: supports
  summary: The active phagolysosome and membrane entries give only the maturation/late-marker
    and bilayer definitions, respectively. GO0032010 is a direct is_a child of GO0005767
    and GO0045335 and has0061474/0106174 part_of children; GO0030670 lists0061474
    is_a. The process terms describe broad phagocytosis and maturation ending in the
    phagolysosome, not a detailed taxon-specific mechanism.
  snapshot_sha256: 6740690b1300ee1c52cf7b22391d2d56e075a2dd3003a46c6436ca1193d350dc
- evidence_id: phagolysosome-agent-SL0206
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0206.json
  locator: Complete native entry including nested hierarchy, definition, synonyms
    and GO mapping
  accessed_at: '2026-10-22T02:59:56.810501Z'
  support: supports
  summary: SL0206 identifies the generic phagosome as a membrane-bounded phagocytic
    compartment, maps to GO0045335 and places it under cytoplasmic vesicle.
  snapshot_sha256: 2dad97fc89fd4ac3bb8dd8e488d84eaf3a59f68f79c8686828f9d7c2d6b7408e
- evidence_id: phagolysosome-agent-tax44689
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689
  locator: Complete native taxId/scientificName/rank/lineage
  accessed_at: '2026-10-22T02:59:56.811450Z'
  support: supports
  summary: ENA confirms Dictyostelium discoideum44689 at species rank. The experimental
    Ax2 culture is specified separately in the primary studies.
  snapshot_sha256: 6f53a1ddbf831afbc0544e18351c92d099e28c4e8258ef29d0f841829af7c37f
- evidence_id: phagolysosome-agent-PMID-12388753
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12388753%20AND%20SRC%3AMED
  locator: Unique MED identity and complete primary abstract
  accessed_at: '2026-10-22T01:10:31.455988Z'
  support: supports
  summary: PMID12388753/DOI10.1091/mbc.e02-04-0206 identifies Gotthardt2002. Complete
    abstract reports D. discoideum latex-bead time courses, staged hydrolase/glycoprotein
    delivery and recycling, and accompanying Rab7/SNARE profiles.
  snapshot_sha256: 7ba1845e0950b4eb8287d04190a939a374cb06b9baee8d880bbd3829a813c22c
- evidence_id: phagolysosome-agent-PMID-16926386
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A16926386%20AND%20SRC%3AMED
  locator: Unique MED identity and complete primary abstract
  accessed_at: '2026-10-22T01:10:31.456120Z'
  support: supports
  summary: PMID16926386/DOI10.1074/mcp.m600113-mcp200 identifies Gotthardt2006. Complete
    abstract reports D. discoideum temporal2D-gel/MS analysis and separate G-protein
    mutant uptake assays.
  snapshot_sha256: 434f8f37aafcf032d8142418f47aef2693fd65ceeb4ebae2c5cd5d31e2a00ce6
- evidence_id: phagolysosome-agent-gotthardt2002-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/129962/
  locator: 'Genuine PMC129962 HTML: complete Introductionsec1, Methodssec2, Resultssec12
    and Discussionsec20, including embedded Figures1–7 captions; no pixels or supplemental
    datasets.'
  accessed_at: '2026-10-22T01:11:10.565148Z'
  support: supports
  summary: The actual study uses D. discoideum Ax2 at22C in HL5c, latex-bead pulse/chase
    and yeast comparison. Intact isolated phagosomes retain boundary membranes; membrane
    and luminal constituents are delivered/retrieved in distinct phases. Lysosomal
    Lmp glycoproteins are explicitly CD36/LIMPII-family, while Vti1/Vamp7/Rab7 profiles
    accompany trafficking; this is not a cross-protist demonstration of LAMP-mediated
    membrane protection or Nramp-dependent efflux. Acidification is associated with
    proton-pump delivery, not a universally constant pH stage.
  snapshot_sha256: 5c333f3d4898a3eac26fb3d8571f723db3ae547e0996914b4696718002408777
- evidence_id: phagolysosome-agent-gotthardt2006-unige-pdf
  kind: primary_source
  reference: https://access.archive-ouverte.unige.ch/access/metadata/eae2ae90-5a91-4330-85a9-04fa245d5d63/download
  locator: Genuine author-hosted publisher PDF, exact title/DOI p2228; Introduction/Methods
    pp2228–2230; Results/Discussion pp2230,2236–2237,2239–2241 including Fig4C and5/6
    captions. TableI images, other figure pixels and supplementary data not reanalyzed.
  accessed_at: '2026-10-22T01:11:52.952323Z'
  support: supports
  summary: The primary study profiles D. discoideum Ax2 phagosomes by2D gels/MS across
    six pulse/chase time points, including carbonate extraction of membrane preparations.
    Temporal groups support digestive and recycling phases, while the text cautions
    that a linear maturation scheme is an oversimplification. Fig4C explicitly borrows
    the acidification/neutralization scheme from a macropinocytosis model. This is
    not a direct comparative demonstration of all added defining molecular traits
    in Entamoeba or ciliates.
  snapshot_sha256: 5e34df34378099b87d70b1920b422d2a575515ecd8ad372dcfb4e2a322ee88cd
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/phagolysosome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:58:55Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/phagolysosome.yaml'
  snapshot_sha256: 57f3f8cf377fe284875e8fc91fc327a0f738cf61113bc4610e9bf736890ddca1
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/phagolysosome.yaml
    --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagolysosome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:58:57Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/phagolysosome.yaml\
    \ --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagolysosome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagolysosome-strict.tsv"
  snapshot_sha256: d6f16348c5fda1870fce04fc1c5bdb4625730f4359032b15d69620d3987b52c6
- evidence_id: phagolysosome-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/phagolysosome.yaml
  locator: Complete native read-only GENE_OR_PROTEIN coverage log
  accessed_at: '2026-10-22T03:02:34.371430Z'
  support: supports
  summary: Native coverage command exited0 and reports zero GENE_OR_PROTEIN nodes;
    no accession-specific protein verification is applicable.
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/phagolysosome.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '13 of 15 collected target identifiers returned OK. PMID:12388753: UNREACHABLE;
    Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity,
    DOI and declared PMC/null status. This separately resolves citation identity after
    bulk eutils414; article-body scope is stated independently.; PMID:16926386: UNREACHABLE;
    Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity,
    DOI and declared PMC/null status. This separately resolves citation identity after
    bulk eutils414; article-body scope is stated independently. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
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
  topic: Exact organelle and membrane/lumen boundaries
  outcome: supported
  target_ids:
  - GO:0032010
  summary: The exact GO0032010 identity, both parents, related synonyms and two has_part
    links are supported by native typed relations and definitions. Whole organelle,
    membrane and lumen remain distinct in the frozen boundary set.
  evidence_ids:
  - record
  - phagolysosome-agent-go
  - phagolysosome-agent-SL0206
- assessment_id: material
  area: grounding
  topic: Collective bilayer constitution
  outcome: supported
  target_ids:
  - GO:0032010
  summary: The label-only lipid row is a collective material constituent, with no
    whole-membrane CURIE used as chemical grounding. Membrane boundaries are positive
    observations in the primary work. Generic component naming does not make the mature
    membrane a different identity; stages have variable molecular composition.
  evidence_ids:
  - record
  - schema
  - phagolysosome-agent-go
  - phagolysosome-agent-SL0206
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
- assessment_id: necessity
  area: evidence
  topic: Formation requirement of individual constituents
  outcome: unknown
  target_ids:
  - GO:0032010
  summary: A lipid boundary is constitutive of the membrane-bounded structure. Neither
    the generic ESSENTIAL designation nor component detection establishes that each
    lipid or protein species is experimentally necessary for formation. No individual
    requirement is inferred from the retained primary assays.
  evidence_ids:
  - record
  - schema
  - phagolysosome-agent-go
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
- assessment_id: scope
  area: scope
  topic: Supported Dictyostelium maturation context
  outcome: supported
  target_ids:
  - GO:0032010
  summary: Tax44689 correctly names the experimental species. The canonical bead-phagosome
    time course and qualitative COMMON occurrence in this species are supported, including
    membrane remodeling and luminal phases. Purified organelle/proteomic observations
    are not universal per-cell frequency measurements or direct functional assays
    of every detected component.
  evidence_ids:
  - record
  - phagolysosome-agent-tax44689
  - phagolysosome-agent-PMID-12388753
  - phagolysosome-agent-PMID-16926386
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
- assessment_id: definition
  area: evidence
  topic: Expanded defining mechanism and taxon scope
  outcome: concern
  target_ids:
  - GO:0032010
  summary: The added definition presents strongly acidified, V-ATPase-maintained,
    hydrolase/protease/lysozyme-rich digestive organization across Dictyostelium,
    Entamoeba and ciliates. The declared GO source contains only the maturation/marker
    definition. Inspected studies directly analyze Dictyostelium with stage-dependent
    remodeling and do not establish that full defining extension across the named
    taxa.
  evidence_ids:
  - record
  - phagolysosome-agent-go
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
- assessment_id: function-graph
  area: graph
  topic: Supported process association versus mechanism resolution
  outcome: concern
  target_ids:
  - GO:0032010
  summary: 'Broad phagocytosis/maturation associations are defensible: native phagocytosis
    includes lysosomal delivery and maturation ends in the phagolysosome. The displayed
    graph, however, consists of constituent/parthood edges followed by whole-structure
    mediates-process associations. It does not depict a molecular causal transition
    or actor explaining the stated assembly/functional mechanism.'
  evidence_ids:
  - record
  - schema
  - phagolysosome-agent-go
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
- assessment_id: acidification-attribution
  area: evidence
  topic: Measured time profiles versus synthesized acidification context
  outcome: concern
  target_ids:
  - GO:0032010
  summary: Gotthardt2002 directly measured trafficking, component profiles and hydrolase
    localization; its Discussion synthesizes proton-pump acidification from earlier
    work. The function evidence note should distinguish that context from the directly
    dissected time profiles.
  evidence_ids:
  - record
  - phagolysosome-agent-PMID-12388753
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
- assessment_id: provenance
  area: provenance
  topic: Bounded source tiers and unchanged status
  outcome: supported
  target_ids:
  - GO:0032010
  summary: Every maintained claim was assessed against native identities, the inspected
    literature scope and frozen boundaries. Positive identity and constituent observations
    are separated from experimental formation requirements and unsupported extensions.
    No scientific edit, status promotion or persistence is implied.
  evidence_ids:
  - record
  - phagolysosome-agent-go
  - phagolysosome-agent-SL0206
  - phagolysosome-agent-tax44689
  - phagolysosome-agent-PMID-12388753
  - phagolysosome-agent-PMID-16926386
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
findings:
- finding_id: F1
  issue_key: phagolysosome-expanded-definition-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Bound the expanded definition to demonstrated taxa and mechanisms
  description: The first ontology-based clause is exact, but the appended molecular
    and taxonomic description is not contained in the cited GO entry. The primary
    evidence establishes staged Dictyostelium phagosome behavior; it does not demonstrate
    the entire added cross-taxon mechanistic definition. Supported digestion/acidification
    in the studied context should be retained, but not silently generalized into a
    defining molecular program for all listed microbial groups.
  target_ids:
  - GO:0032010
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - record
  - phagolysosome-agent-go
  - phagolysosome-agent-PMID-12388753
  - phagolysosome-agent-PMID-16926386
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome.yaml
    role: maintained scientific record
  rule_id: Source-specific claim support, biological scope and graph contract
  native_severity: major
  normalization_reason: The unqualified additions define molecular mechanism, stage
    properties and biological scope; this is materially unsupported scope, not merely
    a missing citation or damaged ontology identity.
- finding_id: F2
  issue_key: phagolysosome-graph-scope-label
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Match the graph scope to its descriptive edges
  description: The graph is labeled MECHANISTIC and titled an assembly and functional
    mechanism, but its edges give material/parthood and generic whole-structure process
    associations. The primary papers contain mechanisms worth separately curating,
    yet those actors and transitions are not represented in this graph.
  target_ids:
  - GO:0032010
  field_paths:
  - causal_graphs[0].scope_status
  - causal_graphs[0].title
  - causal_graphs[0].description
  evidence_ids:
  - record
  - schema
  - phagolysosome-agent-go
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome.yaml
    role: maintained scientific record
  rule_id: Source-specific claim support, biological scope and graph contract
  native_severity: minor
  normalization_reason: The existing identities and coarse associations remain useful;
    the bounded mismatch is the scope/title promise, not evidence that the structure
    or process is wrong.
- finding_id: F3
  issue_key: phagolysosome-acidification-source-method-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the source scope of the acidification note
  description: functions[1].evidence[1].notes attributes distinct luminal-acidification
    behavior to the Gotthardt2002 dissection. Its Methods/Results do not present a
    direct luminal-pH assay; acidification is synthesized in Discussion from earlier
    work, and the2006 Fig4C pH scheme is explicitly adapted from macropinocytosis.
    Trafficking-phase measurements are genuine and should be retained.
  target_ids:
  - GO:0032010
  field_paths:
  - functions[1].evidence[1].notes
  evidence_ids:
  - record
  - phagolysosome-agent-PMID-12388753
  - phagolysosome-agent-gotthardt2002-numeric
  - phagolysosome-agent-gotthardt2006-unige-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome.yaml
    role: maintained scientific record
  rule_id: Source-specific claim support, biological scope and graph contract
  native_severity: minor
  normalization_reason: This is a bounded assay-attribution precision problem, independent
    of the broader definition-scope finding; the evidence does support maturation
    and qualitative acidification context.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032010
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome.yaml
    role: maintained scientific record
  description: Retain the exact ontology boundary/maturation definition and move supported
    extra biology into explicitly taxon-, stage- and source-qualified fields. Remove
    or qualify unestablished extensions, or add directly inspected evidence that actually
    supports each retained mechanism and taxon.
  acceptance_checks:
  - Native GO text is distinguished from curator-added biology.
  - No comparative mechanism or fixed molecular inventory is inferred solely from
    Dictyostelium time profiles.
  - Correct organelle identity, boundary hierarchy and experimentally supported maturation
    remain intact.
  - Native schema, strict, identifier, graph and history checks pass after separately
    authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0032010
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome.yaml
    role: maintained scientific record
  description: Use NONMECHANISTIC with a precise descriptive scope note and aligned
    title, or separately curate a source-backed mechanistic path without inventing
    obligatory actors.
  acceptance_checks:
  - Declared scope and title describe the actual edges.
  - Correct identities, parthood and broad process associations are preserved.
  - Native schema, strict, identifier, graph and history checks pass after separately
    authorized curation.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0032010
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome.yaml
    role: maintained scientific record
  description: State that the study directly dissected trafficking/component phases
    and discussed acidification using earlier evidence, or cite an inspected direct
    pH study for a measurement claim.
  acceptance_checks:
  - Measured trafficking phases are distinguished from review/synthesis-level pH context.
  - The note does not imply a direct pH assay in the cited2002 experiment.
  - Native schema, strict, identifier, graph and history checks pass after separately
    authorized curation.
limitations:
- The two Gotthardt studies directly examine D. discoideum Ax2. Their introductory
  discussion of other systems and shared factors does not prove the full added defining
  program in Entamoeba or ciliates. The limitation is evidence scope, not proof those
  organisms lack any individual feature.
- The2002 genuine main body was read completely at declared sections. The2006 body
  was read only at the explicitly listed pages; TableI images, figure pixels, supplementary
  tables and raw proteomics were not reanalyzed. The Fig4C pH model is explicitly
  adapted from macropinocytosis and not a universal phagolysosome pH measurement.
- Label-only collective bilayer constitution is accepted independently of unknown
  formation necessity for individual molecular species. No optional enzyme or trafficking-protein
  row is required merely because the cited papers identify it.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes clean reviews without invented findings. Parent
  owns finalization and persistence. Five same-base full-corpus gates are staged for
  guarded finalization.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
