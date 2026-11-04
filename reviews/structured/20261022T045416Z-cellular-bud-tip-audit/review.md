# Source-backed review of cellular bud tip

- Review: 20261022T045416Z-cellular-bud-tip-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:37:02Z
- Finished UTC: 2026-10-22T04:54:16Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bud-tip region, bud boundary, yeast example and descriptive exocyst-localization graph are supported at the declared source tiers; no confirmed curation issue was found.

## Scope And Provenance

Exactly one complete target; no neighboring scientific-record verdict is imported. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch46 fixed strict path order, index 7; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005934 | data/structures/other/cellular_bud_tip.yaml | maintained | cellular bud tip |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005934 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005934 | Focused validator passed. |
| Focused native graphs | passed | True | GO:0005934 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:0005934 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005934 | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005934 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005934 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005934 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005934 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005934 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact region identity

identity: supported. Targets: GO:0005934.

GO0005934 and SL0030 consistently identify the distal bud region. Region structure_type, exact synonym and its bud part_of are supported; no molecular complex is substituted for the region.

### Yeast and small-bud context

scope: supported. Targets: GO:0005934.

Species4932 is valid. COMMON means present in most members, with losses exceptional; TerBush small-bud localization gives qualitative ordinary-yeast support, without measuring prevalence. The canonical example remains the examined S. cerevisiae system.

### Region versus localized machinery

grounding: supported. Targets: GO:0005934.

The empty molecular inventory is deliberate and consistent with a spatial region. The record does not claim an exhaustive molecular shell; exocyst and polarisome are distinct localized complexes. No forced component or family insertion follows merely from their localization.

### Canonical and functional source placement

evidence: supported. Targets: GO:0005934.

TerBush supports complex association plus Sec8 small-bud-tip localization; Valtz supports polarity-protein localization at growing sites. The record uses these as evidence for a site of polarized trafficking/polarity, without claiming purified region assembly.

### Descriptive regional graph

graph: supported. Targets: GO:0005934.

The three-node, two-edge FUNCTION graph states bud-tip part_of bud and exocyst localization to the tip. NONMECHANISTIC is accurate; a localized complex is not conflated with the region or with a de novo formation mechanism.

### Discussions, history and open enrichment

completeness: supported. Targets: GO:0005934.

The complete target was checked. Historical boundary decisions correctly keep compartment-independent localized complexes separate. Optional molecular additions are not automatically required, and there are no protein_examples requiring accession enrichment in this target.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/cellular_bud_tip.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic or transport function. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| micro46-shared-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005938,GO:0005737,GO:0005886,GO:0030479,GO:0005940,GO:0097610,GO:0110165,GO:0009986,GO:0097611,GO:0097612,GO:0005933,GO:0033101,GO:0005935,GO:0005934; Exact results for GO0005933/0005934/0005935: name, definition, children and relation types. | supports | The inspected GO0005933 cellular bud, GO0005934 cellular bud tip and GO0005935 cellular bud neck entries identify a whole outgrowth and its distinct regions. The tip is distal to the attachment; the neck is the mother-daughter constriction. Listed part_of children support the corresponding localized-polarisome boundaries. Unrelated entries in this combined response are not relied upon. |
| micro46-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031560,GO:0031561,GO:0000133,GO:0000145; Complete four exact term results: id/name/definition/isObsolete/children, including relation labels and PMID9632790 cross-reference. | supports | GO0031560 is the bud-neck polarisome and GO0031561 the growing-bud-tip polarisome; both are is_a children of GO0000133 and part_of their corresponding regions. Generic GO0000133 names Bni1, Spa2, Pea2 and Bud6, but does not make the present localized inventory exhaustive. GO0000145 is the exocyst tethering complex, distinct from the region receiving it. |
| micro46-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 4932 identifies Saccharomyces cerevisiae at rank species; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro46-valtz1996-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1083/jcb.135.3.725%22; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED8909546: Pea2 protein of yeast is localized to sites of polarized growth and is required for efficient mating and bipolar budding. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro46-valtz1996-pdf | https://pdfs.semanticscholar.org/8982/cdabd9dce19878a052f4e0fd2474e5ed5917.pdf; Printed pp725–726,728,731–735: abstract/introduction, growth and immunofluorescence methods, antibody controls, expression and localization Results; Fig3–6 captions. Extracted primary PDF text read; figure pixels not inspected. | supports | Valtz and Herskowitz directly localize Pea2 to incipient/small-bud growth sites and to the mother-daughter neck after nuclear division but before cytokinesis. The pattern matches Spa2. Pea2 loss reduces Spa2 localization without eliminating its abundance; Spa2 loss eliminates detectable Pea2 in these experiments. These results support localized scaffold membership and interdependence, not a census of all polarisome subunits or a universal formation-dependency assay. |
| micro46-SL-0027 | https://rest.uniprot.org/locations/SL-0027.json; Complete native id/name/definition/geneOntologies/synonyms; SL0030 partOf. | supports | The exact UniProt subcellular-location definition and GO mapping are consistent with the cellular bud/bud-tip boundary. SL0030 explicitly gives partOf SL0027; this region is not the exocyst or polarisome complex. |
| micro46-SL-0030 | https://rest.uniprot.org/locations/SL-0030.json; Complete native id/name/definition/geneOntologies/synonyms; SL0030 partOf. | supports | The exact UniProt subcellular-location definition and GO mapping are consistent with the cellular bud/bud-tip boundary. SL0030 explicitly gives partOf SL0027; this region is not the exocyst or polarisome complex. |
| micro46-terbush1995-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1083/jcb.130.2.299%22; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED7615633: Sec6, Sec8, and Sec15 are components of a multisubunit complex which localizes to small bud tips in Saccharomyces cerevisiae. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro46-terbush1995-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2199927/; Complete article title/authors/abstract on the legacy PMC page. Full article is scanned; its body was not read. | supports | The native archived primary abstract reports Sec6 association with Sec8/Sec15 by chromatography, gradients and immunoprecipitation, and immunofluorescent localization of c-myc-tagged Sec8 to small-bud tips. This supports localized Sec6/8/15 complex evidence; it is not evidence that every subunit was independently imaged. |
| micro46-terbush1995-pdf | https://rupress.org/jcb/article-pdf/130/2/299/1264808/299.pdf; Raw response signature and status from original matching metadata. | context_only | Retained HTTP 403 access outcome: publisher/EuropePMC blocked responses, PMC Preparing to download page, or legacy reCAPTCHA HTML as applicable. None is a PDF body or scientific negative result. |
| micro46-terbush1995-europepmc-pdf | https://europepmc.org/articles/PMC2199927?pdf=render; Raw response signature and status from original matching metadata. | context_only | Retained HTTP 403 access outcome: publisher/EuropePMC blocked responses, PMC Preparing to download page, or legacy reCAPTCHA HTML as applicable. None is a PDF body or scientific negative result. |
| micro46-terbush1995-pmc-pdf | https://pmc.ncbi.nlm.nih.gov/articles/instance/2199927/pdf/jc1302299.pdf; Raw response signature and status from original matching metadata. | context_only | Retained HTTP 200 access outcome: publisher/EuropePMC blocked responses, PMC Preparing to download page, or legacy reCAPTCHA HTML as applicable. None is a PDF body or scientific negative result. |
| micro46-terbush1995-legacy-pdf | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2199927/pdf/jc1302299.pdf; Raw response signature and status from original matching metadata. | context_only | Retained HTTP 200 access outcome: publisher/EuropePMC blocked responses, PMC Preparing to download page, or legacy reCAPTCHA HTML as applicable. None is a PDF body or scientific negative result. |
| schema-result | just validate data/structures/other/cellular_bud_tip.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/cellular_bud_tip.yaml |
| strict-result | just validate-strict data/structures/other/cellular_bud_tip.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/cellular_bud_tip.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip-strict.tsv |
| native-graphs | /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cellular_bud_tip.yaml; Complete read-only focused native graphs log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/cellular_bud_tip.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- No raw microscopy pixels, supplementary files or videos were inspected. Figure captions were read only within the explicitly identified main-body sections.
- COMMON retains the schema meaning present in most members with exceptional losses. The cited yeast experiments support ordinary localized occurrence qualitatively, not a quantitative species-wide prevalence census.
- Only explicitly listed body sections were read; none of the retained access failures or HTML download/challenge responses is treated as full article text.
- TerBush1995 was independently read at complete native abstract tier only. Neither detailed purification conditions nor figure pixels were recovered/read. Its title, authors, year and DOI were verified; no detailed primary-body claim is certified.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these localized polarity-complex identity, protein family, localization and formation claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T045416Z-cellular-bud-tip-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of cellular bud tip
started_at: '2026-10-22T04:37:02Z'
finished_at: '2026-10-22T04:54:16Z'
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
summary: The bud-tip region, bud boundary, yeast example and descriptive exocyst-localization
  graph are supported at the declared source tiers; no confirmed curation issue was
  found.
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
  - path: data/structures/other/cellular_bud_tip.yaml
    sha256: c5e468cb63bf8195e8d5c7567d1737bca98fb2f466bbc1982cc66df390dbd1bc
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
- target_id: GO:0005934
  path: data/structures/other/cellular_bud_tip.yaml
  label: cellular bud tip
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cellular_bud_tip.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; no neighboring scientific-record verdict
    is imported. Exact authority, all current component/function/graph/source placements,
    taxonomic scope, formation semantics, history and discussions were reviewed.
  selection: Batch46 fixed strict path order, index 7; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005934
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005934
  command: just validate data/structures/other/cellular_bud_tip.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005934
  command: just validate-strict data/structures/other/cellular_bud_tip.yaml --out
    /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-graphs
  name: Focused native graphs
  status: passed
  required: true
  target_ids:
  - GO:0005934
  command: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cellular_bud_tip.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005934
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - micro46-shared-go
  - micro46-go
  - micro46-tax4932
  - micro46-valtz1996-meta
  - micro46-valtz1996-pdf
  - micro46-SL-0027
  - micro46-SL-0030
  - micro46-terbush1995-meta
  - micro46-terbush1995-legacy
  - micro46-terbush1995-pdf
  - micro46-terbush1995-europepmc-pdf
  - micro46-terbush1995-pmc-pdf
  - micro46-terbush1995-legacy-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005934
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005934
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005934
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005934
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005934
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005934
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
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/cellular_bud_tip.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:48:34Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:48:34Z'
  support: context_only
  summary: ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite
    class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic
    or transport function.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:48:34Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: micro46-shared-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005938,GO:0005737,GO:0005886,GO:0030479,GO:0005940,GO:0097610,GO:0110165,GO:0009986,GO:0097611,GO:0097612,GO:0005933,GO:0033101,GO:0005935,GO:0005934
  locator: 'Exact results for GO0005933/0005934/0005935: name, definition, children
    and relation types.'
  accessed_at: '2026-10-22T04:38:31.207999Z'
  support: supports
  summary: The inspected GO0005933 cellular bud, GO0005934 cellular bud tip and GO0005935
    cellular bud neck entries identify a whole outgrowth and its distinct regions.
    The tip is distal to the attachment; the neck is the mother-daughter constriction.
    Listed part_of children support the corresponding localized-polarisome boundaries.
    Unrelated entries in this combined response are not relied upon.
  snapshot_sha256: 04958c90f60f753443ae327ebf353b3ab6ac7a8bfaf5cea58634921b40b55b5a
- evidence_id: micro46-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031560,GO:0031561,GO:0000133,GO:0000145
  locator: 'Complete four exact term results: id/name/definition/isObsolete/children,
    including relation labels and PMID9632790 cross-reference.'
  accessed_at: '2026-10-22T04:42:12.245944Z'
  support: supports
  summary: GO0031560 is the bud-neck polarisome and GO0031561 the growing-bud-tip
    polarisome; both are is_a children of GO0000133 and part_of their corresponding
    regions. Generic GO0000133 names Bni1, Spa2, Pea2 and Bud6, but does not make
    the present localized inventory exhaustive. GO0000145 is the exocyst tethering
    complex, distinct from the region receiving it.
  snapshot_sha256: a1ee5792ff712e6ca100621f8ac56712c2d64004b5a8e1dfa383c387714819f3
- evidence_id: micro46-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:38:31.951602Z'
  support: supports
  summary: ENA taxId 4932 identifies Saccharomyces cerevisiae at rank species; aliases
    and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro46-valtz1996-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1083/jcb.135.3.725%22
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:38:32.557137Z'
  support: supports
  summary: 'Unique MED8909546: Pea2 protein of yeast is localized to sites of polarized
    growth and is required for efficient mating and bipolar budding. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 5995f18fa905450fc26415293cae1475f7acb5da7cc4752f3db0356906c58c43
- evidence_id: micro46-valtz1996-pdf
  kind: primary_source
  reference: https://pdfs.semanticscholar.org/8982/cdabd9dce19878a052f4e0fd2474e5ed5917.pdf
  locator: 'Printed pp725–726,728,731–735: abstract/introduction, growth and immunofluorescence
    methods, antibody controls, expression and localization Results; Fig3–6 captions.
    Extracted primary PDF text read; figure pixels not inspected.'
  accessed_at: '2026-10-21T09:48:11.208322Z'
  support: supports
  summary: Valtz and Herskowitz directly localize Pea2 to incipient/small-bud growth
    sites and to the mother-daughter neck after nuclear division but before cytokinesis.
    The pattern matches Spa2. Pea2 loss reduces Spa2 localization without eliminating
    its abundance; Spa2 loss eliminates detectable Pea2 in these experiments. These
    results support localized scaffold membership and interdependence, not a census
    of all polarisome subunits or a universal formation-dependency assay.
  snapshot_sha256: c06951939912dcb3700b5cd867b40a7d9c2a74f41460bb93f31839852509d9c9
- evidence_id: micro46-SL-0027
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0027.json
  locator: Complete native id/name/definition/geneOntologies/synonyms; SL0030 partOf.
  accessed_at: '2026-10-22T04:38:31.208429Z'
  support: supports
  summary: The exact UniProt subcellular-location definition and GO mapping are consistent
    with the cellular bud/bud-tip boundary. SL0030 explicitly gives partOf SL0027;
    this region is not the exocyst or polarisome complex.
  snapshot_sha256: 3367af44f7485396df649e631b15487f577a11026c6701fbbd535fec005f759d
- evidence_id: micro46-SL-0030
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0030.json
  locator: Complete native id/name/definition/geneOntologies/synonyms; SL0030 partOf.
  accessed_at: '2026-10-22T04:38:31.208783Z'
  support: supports
  summary: The exact UniProt subcellular-location definition and GO mapping are consistent
    with the cellular bud/bud-tip boundary. SL0030 explicitly gives partOf SL0027;
    this region is not the exocyst or polarisome complex.
  snapshot_sha256: 6947119e52ad8021360b342a15d99f13085292f3e4d9a0dcf499ddddbd1272fc
- evidence_id: micro46-terbush1995-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1083/jcb.130.2.299%22
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:42:13.347251Z'
  support: supports
  summary: 'Unique MED7615633: Sec6, Sec8, and Sec15 are components of a multisubunit
    complex which localizes to small bud tips in Saccharomyces cerevisiae. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 318f5c337905b7b57da72006b83d12005379c9c0babd83b23c2fc39fde2c612d
- evidence_id: micro46-terbush1995-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2199927/
  locator: Complete article title/authors/abstract on the legacy PMC page. Full article
    is scanned; its body was not read.
  accessed_at: '2026-10-22T04:42:46.388329Z'
  support: supports
  summary: The native archived primary abstract reports Sec6 association with Sec8/Sec15
    by chromatography, gradients and immunoprecipitation, and immunofluorescent localization
    of c-myc-tagged Sec8 to small-bud tips. This supports localized Sec6/8/15 complex
    evidence; it is not evidence that every subunit was independently imaged.
  snapshot_sha256: be9b7b1f5843e2799254c514e479598429687c329e71ab4fd4306a2f0e35ed99
- evidence_id: micro46-terbush1995-pdf
  kind: database
  reference: https://rupress.org/jcb/article-pdf/130/2/299/1264808/299.pdf
  locator: Raw response signature and status from original matching metadata.
  accessed_at: '2026-10-22T04:42:46.388659Z'
  support: context_only
  summary: 'Retained HTTP 403 access outcome: publisher/EuropePMC blocked responses,
    PMC Preparing to download page, or legacy reCAPTCHA HTML as applicable. None is
    a PDF body or scientific negative result.'
  snapshot_sha256: 7968e134eca155c787ae1f8007b49b524bd035c65770e701922966db5f9a464b
- evidence_id: micro46-terbush1995-europepmc-pdf
  kind: database
  reference: https://europepmc.org/articles/PMC2199927?pdf=render
  locator: Raw response signature and status from original matching metadata.
  accessed_at: '2026-10-22T04:46:12.764532Z'
  support: context_only
  summary: 'Retained HTTP 403 access outcome: publisher/EuropePMC blocked responses,
    PMC Preparing to download page, or legacy reCAPTCHA HTML as applicable. None is
    a PDF body or scientific negative result.'
  snapshot_sha256: b2d60ddfbda7a01247bd2448d7953c9b402495604c22e7c037512c938e612e10
- evidence_id: micro46-terbush1995-pmc-pdf
  kind: database
  reference: https://pmc.ncbi.nlm.nih.gov/articles/instance/2199927/pdf/jc1302299.pdf
  locator: Raw response signature and status from original matching metadata.
  accessed_at: '2026-10-22T04:45:40.803167Z'
  support: context_only
  summary: 'Retained HTTP 200 access outcome: publisher/EuropePMC blocked responses,
    PMC Preparing to download page, or legacy reCAPTCHA HTML as applicable. None is
    a PDF body or scientific negative result.'
  snapshot_sha256: 3e8e8bd20806c4d15f1d2eb533969c30b7fa186d881f6930f7faa0bc87d98664
- evidence_id: micro46-terbush1995-legacy-pdf
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2199927/pdf/jc1302299.pdf
  locator: Raw response signature and status from original matching metadata.
  accessed_at: '2026-10-22T04:46:12.764882Z'
  support: context_only
  summary: 'Retained HTTP 200 access outcome: publisher/EuropePMC blocked responses,
    PMC Preparing to download page, or legacy reCAPTCHA HTML as applicable. None is
    a PDF body or scientific negative result.'
  snapshot_sha256: b6c611ebf3ba53fe072e7b9c3277624e4b0114b368d8ec4852991531c966b694
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/cellular_bud_tip.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:37:03Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/cellular_bud_tip.yaml'
  snapshot_sha256: 21d5afff745810cb7c743c8c2d940a3072f155bb46d66df202ce711df7f7af4b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/cellular_bud_tip.yaml --out
    /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:37:04Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/cellular_bud_tip.yaml\
    \ --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip-strict.tsv"
  snapshot_sha256: 5255fe7844791bd029080acebd3e651202e23ff2546faf5abd686d2d1540aa56
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cellular_bud_tip.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T04:43:21.933571Z'
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
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/cellular_bud_tip.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
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
  topic: Exact region identity
  outcome: supported
  target_ids:
  - GO:0005934
  summary: GO0005934 and SL0030 consistently identify the distal bud region. Region
    structure_type, exact synonym and its bud part_of are supported; no molecular
    complex is substituted for the region.
  evidence_ids:
  - micro46-shared-go
  - micro46-SL-0027
  - micro46-SL-0030
- assessment_id: scope
  area: scope
  topic: Yeast and small-bud context
  outcome: supported
  target_ids:
  - GO:0005934
  summary: Species4932 is valid. COMMON means present in most members, with losses
    exceptional; TerBush small-bud localization gives qualitative ordinary-yeast support,
    without measuring prevalence. The canonical example remains the examined S. cerevisiae
    system.
  evidence_ids:
  - micro46-tax4932
  - micro46-terbush1995-meta
  - micro46-terbush1995-legacy
  - schema
- assessment_id: grounding
  area: grounding
  topic: Region versus localized machinery
  outcome: supported
  target_ids:
  - GO:0005934
  summary: The empty molecular inventory is deliberate and consistent with a spatial
    region. The record does not claim an exhaustive molecular shell; exocyst and polarisome
    are distinct localized complexes. No forced component or family insertion follows
    merely from their localization.
  evidence_ids:
  - micro46-go
  - micro46-shared-go
  - micro46-terbush1995-legacy
  - record
- assessment_id: function
  area: evidence
  topic: Canonical and functional source placement
  outcome: supported
  target_ids:
  - GO:0005934
  summary: TerBush supports complex association plus Sec8 small-bud-tip localization;
    Valtz supports polarity-protein localization at growing sites. The record uses
    these as evidence for a site of polarized trafficking/polarity, without claiming
    purified region assembly.
  evidence_ids:
  - micro46-terbush1995-meta
  - micro46-terbush1995-legacy
  - micro46-valtz1996-meta
  - micro46-valtz1996-pdf
- assessment_id: graph
  area: graph
  topic: Descriptive regional graph
  outcome: supported
  target_ids:
  - GO:0005934
  summary: The three-node, two-edge FUNCTION graph states bud-tip part_of bud and
    exocyst localization to the tip. NONMECHANISTIC is accurate; a localized complex
    is not conflated with the region or with a de novo formation mechanism.
  evidence_ids:
  - micro46-shared-go
  - micro46-go
  - micro46-terbush1995-legacy
  - record
- assessment_id: coverage
  area: completeness
  topic: Discussions, history and open enrichment
  outcome: supported
  target_ids:
  - GO:0005934
  summary: The complete target was checked. Historical boundary decisions correctly
    keep compartment-independent localized complexes separate. Optional molecular
    additions are not automatically required, and there are no protein_examples requiring
    accession enrichment in this target.
  evidence_ids:
  - micro46-shared-go
  - micro46-go
  - record
  - curation
findings: []
actions: []
limitations:
- No raw microscopy pixels, supplementary files or videos were inspected. Figure captions
  were read only within the explicitly identified main-body sections.
- COMMON retains the schema meaning present in most members with exceptional losses.
  The cited yeast experiments support ordinary localized occurrence qualitatively,
  not a quantitative species-wide prevalence census.
- Only explicitly listed body sections were read; none of the retained access failures
  or HTML download/challenge responses is treated as full article text.
- TerBush1995 was independently read at complete native abstract tier only. Neither
  detailed purification conditions nor figure pixels were recovered/read. Its title,
  authors, year and DOI were verified; no detailed primary-body claim is certified.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these localized polarity-complex identity, protein
  family, localization and formation claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
