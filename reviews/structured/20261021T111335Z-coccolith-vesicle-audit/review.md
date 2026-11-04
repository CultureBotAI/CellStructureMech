# Organelle identity, composition and evidence review

- Review: 20261021T111335Z-coccolith-vesicle-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:57:32Z
- Finished UTC: 2026-10-21T11:13:35Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact intracellular-vesicle identity, two strain-supported examples, membrane observation, limited formation-site function and maintained image provenance are supported. No concrete curation issue was established.

## Scope And Provenance

Entire single record with exact authority identities, declared source-reading scopes, protein checks where applicable and component/function/graph boundaries.

Selection: Target 10 in batch twenty-three; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:coccolith_vesicle | data/structures/membrane_organelle/coccolith_vesicle.yaml | maintained | coccolith vesicle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | cellstructuremech:coccolith_vesicle | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Native protein causal-graphs | passed | True | cellstructuremech:coccolith_vesicle | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Focused native schema | passed | True | cellstructuremech:coccolith_vesicle | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:coccolith_vesicle | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:coccolith_vesicle | 6 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | cellstructuremech:coccolith_vesicle | No expression-module or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | cellstructuremech:coccolith_vesicle | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:coccolith_vesicle | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:coccolith_vesicle | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:coccolith_vesicle | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:coccolith_vesicle | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:coccolith_vesicle | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Formation compartment distinct from mineral products

identity: supported. Targets: cellstructuremech:coccolith_vesicle.

The local identifier denotes the membrane-bounded intracellular compartment in which coccoliths form. Its parent is intentionally broader; a coccolith is an individual mineral scale and a coccosphere the external assembled covering. Current bounded GO searches add no exact target term and do not certify historical exhaustive searches.

### Two directly evidenced taxa and strains

scope: supported. Targets: cellstructuremech:coccolith_vesicle.

The current native taxa verify Calcidiscus leptoporus127549 and Emiliania huxleyi2903, with Gephyrocapsa huxleyi explicitly a synonym of the latter. The primary culture Methods support RCC1130 and AWI1516 respectively. The qualitative occurrence is restricted to these supported contexts; a population prevalence is not inferred from imaging.

### Observed membrane with molecular necessity unresolved

grounding: supported. Targets: cellstructuremech:coccolith_vesicle.

The OTHER component denotes a structural bounding membrane and is appropriately grounded to GO0016020. The source directly images it. Its UNKNOWN essentiality and absence of asserted molecular constituents preserve the limit between observing a boundary and experimentally testing assembly necessity. Speculative ATPase-like densities and ion transport are not promoted to identified protein machinery.

### Site of intracellular mineral formation

evidence: supported. Targets: cellstructuremech:coccolith_vesicle.

The maintained function is a directly imaged site of crystal growth, not a causal mechanism for crystal shape, ion transfer or calcium storage. No causal graph is required for this explicitly observational record; no asserted causal graph is being scored as a mechanism.

### Traceable image, method and licence

provenance: supported. Targets: cellstructuremech:coccolith_vesicle.

The local Figure2 exactly matches the native retrieved bytes, the attribution and panel meanings match the primary caption, and native ALI metadata explicitly supplies CC BY4.0. The high-pressure-freeze/fracture and plunge-freeze/FIB workflows are distinguished correctly. No image pixels, data or record history are changed.

### Bounded record-level coverage

completeness: supported. Targets: cellstructuremech:coccolith_vesicle.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Additional exhaustive component inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. This bounded review does not assert exhaustive literature completeness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/coccolith_vesicle.yaml; Entire maintained YAML including history, all evidence notes, components, functions, graph edges and discussions | context_only | All maintained fields were read. No scientific edit or mapping-status promotion is made. |
| policy | docs/CURATION.md; Exact identity, claim-level evidence, material versus localization grounding, and component assembly-essentiality contract | context_only | Family identity, concrete protein examples and structure membership are separate; activity and viability are not by themselves formation assays. Optional inventories are not mandatory. |
| root23-sources-NCBITaxon-127549 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/127549; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Calcidiscus leptoporus at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root23-sources-NCBITaxon-2903 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2903; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Emiliania huxleyi at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root23-sources-doi-10.1021_jacs.6c02151 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1021/jacs.6c02151; Exact native bibliography and complete abstract | supports | Native MED identifies Spatial Relations between Coccoliths and Their Confining Membrane During Crystal Morphogenesis. (Avrahami EM, Karpov D, Aram L, Elad N, Safadi R, Rosenhek-Goldian I, Sui XM, de Haan D, Varsano N, Cohen SR, Zlotnikov I, Gal A., 2026), PMID 41875313, DOI 10.1021/jacs.6c02151. Bibliographic identity and the complete returned abstract were read. Article body scope is separately declared. |
| root23-sources-doi-10.1038_ncomms11228 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/ncomms11228; Exact native bibliography and complete abstract | supports | Native MED identifies A vacuole-like compartment concentrates a disordered calcium phase in a key coccolithophorid alga. (Sviben S, Gal A, Hood MA, Bertinetti L, Politi Y, Bennet M, Krishnamoorthy P, Schertel A, Wirth R, Sorrentino A, Pereiro E, Faivre D, Scheffel A., 2016), PMID 27075521, DOI 10.1038/ncomms11228. Bibliographic identity and the complete returned abstract were read. Article body scope is separately declared. |
| root23-sources-coccolith-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016020,GO:0043231; All returned exact identifiers, labels, definitions, active status and relevant children | supports | Active native GO terms identify the declared broad vesicle parent and membrane constituent. These terms are deliberately broader than the exact coccolith-vesicle local identity. |
| root23-sources-coccolith-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=coccolith&amp;limit=100&amp;page=1; Complete response and exact query URL; numberOfHits=0 | context_only | The current exact submitted text query returned zero matches. This bounded lookup does not certify every ontology or repeat the historical curator search. |
| root23-sources-coccolithogenesis-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=coccolithogenesis&amp;limit=100&amp;page=1; Complete response and exact query URL; numberOfHits=0 | context_only | The current exact submitted text query returned zero matches. This bounded lookup does not certify every ontology or repeat the historical curator search. |
| root23-sources-jats-PMC13067266 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13067266/fullTextXML; Complete main scientific body sections1–4 and Figure2 caption. Figure2 was visually inspected separately; no cryo-ET volumes or raw data were reanalysed. | supports | The primary Results directly image membrane-enclosed calcite growth in Calcidiscus leptoporus, distinguish the membrane/crystal spacing across developmental stages, and qualify the possible functions of observed densities. Complete scientific Introduction, Results, Discussion and Conclusions were read. The observed intraluminal environment is not equated with the separate calcium-storage compartment of another organism. |
| root23-sources-coccolith2026-supplement | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_si_001.pdf; Supplementary PDF from Cell cultures through complete Cryo-FIB-SEM methods and processing, stopping at the beginning of Cryo-FIB lamellae milling. The entire supplement and raw reconstructions were not read. | supports | Supplementary Methods explicitly identify C. leptoporus RCC1130. The complete culture, freeze-fracture, external-coccolith EDTA removal, cryofixation/FIB-SEM preparation, slice-and-view and image-processing passages support the maintained strain and method distinctions. High-pressure freezing/freeze fracture applies to Figure2B; external decalcification precedes the plunge-freezing/FIB workflow. |
| root23-sources-jats-PMC4834641 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4834641/fullTextXML; Complete Results subsections on 3D ultrastructure, composition and variability (sec4–6); complete Discussion(sec7); Methods culture(sec9); Figure3,4,6 captions. Earlier XANES/X-ray sections and image pixels were not reanalysed. | supports | The primary ultrastructural and chemical observations distinguish the calcite-containing coccolith-vesicle/reticular-body system from an independently membrane-bounded Ca/P-rich storage compartment in E. huxleyi. Close contact is not direct proof of ion transfer or membrane continuity. Methods identifies the AWI1516 culture. |
| root23-sources-coccolith2026-s3xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/PMC13067266.1.xml; Front/article-meta/permissions, license text and namespace-qualified ALI license_ref | supports | The native PMC archived XML includes the publisher human-readable CC BY permission and exact machine-readable ALI license_ref https://creativecommons.org/licenses/by/4.0/ with content-type ccbylicense. This verifies the reuse licence for the maintained Figure2 at its source. |
| root23-sources-coccolith-fig2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_0002.jpg; Figure2 image pixels and complete source Figure2 caption; exact local/source SHA256 match | supports | The downloaded native figure is byte-identical to the maintained image. Visual inspection confirms a schematic and cryo-SEM/FIB-SEM panels of membrane boundaries and successive coccolith stages; panel ordering is not a time-lapse experiment. The maintained microscopy/attribution/caption context agrees with the source caption. |
| image | data/images/membrane_organelle/coccolith_vesicle/pmc13067266_fig2.jpg; Entire maintained image visually inspected at native 700x418 pixels | context_only | Byte identity to the directly retrieved source image and licence were checked; no image edit is proposed. |
| boundary-coccolith | data/structures/envelope/coccolith.yaml; Identifier, label, definition and parent_structures only | context_only | Boundary-only inspection distinguishes the mineral scale and assembled external covering from the intracellular formation vesicle. This neighbor is not a second target. |
| boundary-coccosphere | data/structures/envelope/coccosphere.yaml; Identifier, label, definition and parent_structures only | context_only | Boundary-only inspection distinguishes the mineral scale and assembled external covering from the intracellular formation vesicle. This neighbor is not a second target. |
| native-verify | /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml --verify; Exact focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml --causal-graphs; Exact focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/coccolith_vesicle.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/coccolith_vesicle.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/coccolith_vesicle.yaml --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/coccolith_vesicle-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/coccolith_vesicle.yaml --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/coccolith_vesicle-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/coccolith_vesicle-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/coccolith_vesicle.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 6 of7 collected target identifiers returned OK in this fresh base resolver run. Residuals: cellstructuremech:coccolith_vesicle: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The complete main scientific body of Avrahami2026 and named Sviben2016 sections were read; the precise supplementary Methods subset is stated in evidence. This is not an entire-supplement or raw-data audit.
- Figure2 was visually inspected and byte/license checked. Other microscopy panels, tomographic volumes and inferred protein densities were not independently reanalysed.
- The neighboring coccolith and coccosphere records were read only at their identity/boundary fields; their full scientific claims are not reviewed here.
- Current bounded ontology queries and an ignored-inclusive local path search do not recertify historical exhaustive searches or prove a molecular mechanism.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization; identifier transport and label-adapter limits remain explicit.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for every uncovered target, including a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T111335Z-coccolith-vesicle-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Organelle identity, composition and evidence review
started_at: '2026-10-21T10:57:32Z'
finished_at: '2026-10-21T11:13:35Z'
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
summary: The exact intracellular-vesicle identity, two strain-supported examples,
  membrane observation, limited formation-site function and maintained image provenance
  are supported. No concrete curation issue was established.
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
  - path: data/images/membrane_organelle/coccolith_vesicle/pmc13067266_fig2.jpg
    sha256: f41e31add721c5f01869b2ce9ebe38b8aa7add53acb9a6445f6d2335858d2020
    role: context
  - path: data/structures/envelope/coccolith.yaml
    sha256: 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa
    role: context
  - path: data/structures/envelope/coccosphere.yaml
    sha256: b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299
    role: context
  - path: data/structures/membrane_organelle/coccolith_vesicle.yaml
    sha256: 89b7e793211332507189d1ba872fc1eb901cf8703323853cd10d65b45e971655
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
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: cellstructuremech:coccolith_vesicle
  path: data/structures/membrane_organelle/coccolith_vesicle.yaml
  label: coccolith vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/coccolith_vesicle.yaml
    role: maintained scientific record
scope:
  description: Entire single record with exact authority identities, declared source-reading
    scopes, protein checks where applicable and component/function/graph boundaries.
  selection: Target 10 in batch twenty-three; exact sorted uncovered path at frozen
    fresh-main revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:coccolith_vesicle
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith_vesicle
  command: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml
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
  - cellstructuremech:coccolith_vesicle
  command: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml
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
  - cellstructuremech:coccolith_vesicle
  command: just validate data/structures/membrane_organelle/coccolith_vesicle.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith_vesicle
  command: just validate-strict data/structures/membrane_organelle/coccolith_vesicle.yaml
    --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/coccolith_vesicle-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith_vesicle
  summary: 6 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - record
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:coccolith_vesicle
  summary: No expression-module or transcriptomic inference is made by this structural
    review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith_vesicle
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - root23-sources-NCBITaxon-127549
  - root23-sources-NCBITaxon-2903
  - root23-sources-doi-10.1021_jacs.6c02151
  - root23-sources-doi-10.1038_ncomms11228
  - root23-sources-coccolith-go
  - root23-sources-coccolith-go-search
  - root23-sources-coccolithogenesis-go-search
  - root23-sources-jats-PMC13067266
  - root23-sources-coccolith2026-supplement
  - root23-sources-jats-PMC4834641
  - root23-sources-coccolith2026-s3xml
  - root23-sources-coccolith-fig2
  - image
  - boundary-coccolith
  - boundary-coccosphere
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith_vesicle
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
  - cellstructuremech:coccolith_vesicle
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
  - cellstructuremech:coccolith_vesicle
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
  - cellstructuremech:coccolith_vesicle
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
  - cellstructuremech:coccolith_vesicle
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
  reference: data/structures/membrane_organelle/coccolith_vesicle.yaml
  locator: Entire maintained YAML including history, all evidence notes, components,
    functions, graph edges and discussions
  accessed_at: '2026-10-21T11:06:56Z'
  support: context_only
  summary: All maintained fields were read. No scientific edit or mapping-status promotion
    is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, claim-level evidence, material versus localization grounding,
    and component assembly-essentiality contract
  accessed_at: '2026-10-21T11:06:56Z'
  support: context_only
  summary: Family identity, concrete protein examples and structure membership are
    separate; activity and viability are not by themselves formation assays. Optional
    inventories are not mandatory.
- evidence_id: root23-sources-NCBITaxon-127549
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/127549
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:57:51.369057Z'
  support: supports
  summary: Native ENA taxonomy identifies Calcidiscus leptoporus at species rank.
    Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: 941880c35c418c0aacec8a8042e96504d7f40a25b3a969d25fda463a354c1cc9
- evidence_id: root23-sources-NCBITaxon-2903
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2903
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:57:51.817696Z'
  support: supports
  summary: Native ENA taxonomy identifies Emiliania huxleyi at species rank. Only
    this taxon's identity and names are asserted by this row, not occurrence or experimental
    stock identity.
  snapshot_sha256: e66e5ff5bd50e8c2736f1d3bd7afd7d27b8c62ef753454708067bc1c1ef9af22
- evidence_id: root23-sources-doi-10.1021_jacs.6c02151
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1021/jacs.6c02151
  locator: Exact native bibliography and complete abstract
  accessed_at: '2026-10-21T10:57:51.883871Z'
  support: supports
  summary: Native MED identifies Spatial Relations between Coccoliths and Their Confining
    Membrane During Crystal Morphogenesis. (Avrahami EM, Karpov D, Aram L, Elad N,
    Safadi R, Rosenhek-Goldian I, Sui XM, de Haan D, Varsano N, Cohen SR, Zlotnikov
    I, Gal A., 2026), PMID 41875313, DOI 10.1021/jacs.6c02151. Bibliographic identity
    and the complete returned abstract were read. Article body scope is separately
    declared.
  snapshot_sha256: ac00ca5a592b21ef9dee0d22139285198b21a3c8f4383a36d7e74574efc90895
- evidence_id: root23-sources-doi-10.1038_ncomms11228
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/ncomms11228
  locator: Exact native bibliography and complete abstract
  accessed_at: '2026-10-21T10:57:52.094946Z'
  support: supports
  summary: Native MED identifies A vacuole-like compartment concentrates a disordered
    calcium phase in a key coccolithophorid alga. (Sviben S, Gal A, Hood MA, Bertinetti
    L, Politi Y, Bennet M, Krishnamoorthy P, Schertel A, Wirth R, Sorrentino A, Pereiro
    E, Faivre D, Scheffel A., 2016), PMID 27075521, DOI 10.1038/ncomms11228. Bibliographic
    identity and the complete returned abstract were read. Article body scope is separately
    declared.
  snapshot_sha256: 6d66db69b7bcb6b95452f685503467f72a033efac65fb889eae31ad09d456dbe
- evidence_id: root23-sources-coccolith-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016020,GO:0043231
  locator: All returned exact identifiers, labels, definitions, active status and
    relevant children
  accessed_at: '2026-10-21T10:57:51.355441Z'
  support: supports
  summary: Active native GO terms identify the declared broad vesicle parent and membrane
    constituent. These terms are deliberately broader than the exact coccolith-vesicle
    local identity.
  snapshot_sha256: 62ae267eca80e0297bca56833f905cbd02db3e689d5d24ba8e16e10b1c451dc5
- evidence_id: root23-sources-coccolith-go-search
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=coccolith&limit=100&page=1
  locator: Complete response and exact query URL; numberOfHits=0
  accessed_at: '2026-10-21T11:01:29.210443Z'
  support: context_only
  summary: The current exact submitted text query returned zero matches. This bounded
    lookup does not certify every ontology or repeat the historical curator search.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
- evidence_id: root23-sources-coccolithogenesis-go-search
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=coccolithogenesis&limit=100&page=1
  locator: Complete response and exact query URL; numberOfHits=0
  accessed_at: '2026-10-21T11:01:29.174657Z'
  support: context_only
  summary: The current exact submitted text query returned zero matches. This bounded
    lookup does not certify every ontology or repeat the historical curator search.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
- evidence_id: root23-sources-jats-PMC13067266
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13067266/fullTextXML
  locator: Complete main scientific body sections1–4 and Figure2 caption. Figure2
    was visually inspected separately; no cryo-ET volumes or raw data were reanalysed.
  accessed_at: '2026-10-21T10:57:52.553331Z'
  support: supports
  summary: The primary Results directly image membrane-enclosed calcite growth in
    Calcidiscus leptoporus, distinguish the membrane/crystal spacing across developmental
    stages, and qualify the possible functions of observed densities. Complete scientific
    Introduction, Results, Discussion and Conclusions were read. The observed intraluminal
    environment is not equated with the separate calcium-storage compartment of another
    organism.
  snapshot_sha256: 394a5731e2fdd83227a7bf515488f6add3b971c53697b6297c1e581f7c6baec9
- evidence_id: root23-sources-coccolith2026-supplement
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_si_001.pdf
  locator: Supplementary PDF from Cell cultures through complete Cryo-FIB-SEM methods
    and processing, stopping at the beginning of Cryo-FIB lamellae milling. The entire
    supplement and raw reconstructions were not read.
  accessed_at: '2026-10-21T10:58:30.073350Z'
  support: supports
  summary: Supplementary Methods explicitly identify C. leptoporus RCC1130. The complete
    culture, freeze-fracture, external-coccolith EDTA removal, cryofixation/FIB-SEM
    preparation, slice-and-view and image-processing passages support the maintained
    strain and method distinctions. High-pressure freezing/freeze fracture applies
    to Figure2B; external decalcification precedes the plunge-freezing/FIB workflow.
  snapshot_sha256: b919d05e8a48887245d56be37a7aa917366f68cdf058e6b742bae29d385a3248
- evidence_id: root23-sources-jats-PMC4834641
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4834641/fullTextXML
  locator: Complete Results subsections on 3D ultrastructure, composition and variability
    (sec4–6); complete Discussion(sec7); Methods culture(sec9); Figure3,4,6 captions.
    Earlier XANES/X-ray sections and image pixels were not reanalysed.
  accessed_at: '2026-10-21T10:58:30.264387Z'
  support: supports
  summary: The primary ultrastructural and chemical observations distinguish the calcite-containing
    coccolith-vesicle/reticular-body system from an independently membrane-bounded
    Ca/P-rich storage compartment in E. huxleyi. Close contact is not direct proof
    of ion transfer or membrane continuity. Methods identifies the AWI1516 culture.
  snapshot_sha256: cb92f360326ea29a36cd37f6bf417250926d35f9dd2327659475a6bcb26633ab
- evidence_id: root23-sources-coccolith2026-s3xml
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/PMC13067266.1.xml
  locator: Front/article-meta/permissions, license text and namespace-qualified ALI
    license_ref
  accessed_at: '2026-10-21T10:58:29.621057Z'
  support: supports
  summary: The native PMC archived XML includes the publisher human-readable CC BY
    permission and exact machine-readable ALI license_ref https://creativecommons.org/licenses/by/4.0/
    with content-type ccbylicense. This verifies the reuse licence for the maintained
    Figure2 at its source.
  snapshot_sha256: c65411d5c5adb24f2e42120962c24d0fd3ecaffda72f9f485a728a313f2acdef
- evidence_id: root23-sources-coccolith-fig2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_0002.jpg
  locator: Figure2 image pixels and complete source Figure2 caption; exact local/source
    SHA256 match
  accessed_at: '2026-10-21T10:57:51.898130Z'
  support: supports
  summary: The downloaded native figure is byte-identical to the maintained image.
    Visual inspection confirms a schematic and cryo-SEM/FIB-SEM panels of membrane
    boundaries and successive coccolith stages; panel ordering is not a time-lapse
    experiment. The maintained microscopy/attribution/caption context agrees with
    the source caption.
  snapshot_sha256: f41e31add721c5f01869b2ce9ebe38b8aa7add53acb9a6445f6d2335858d2020
- evidence_id: image
  kind: record_content
  reference: data/images/membrane_organelle/coccolith_vesicle/pmc13067266_fig2.jpg
  locator: Entire maintained image visually inspected at native 700x418 pixels
  accessed_at: '2026-10-21T11:06:56Z'
  support: context_only
  summary: Byte identity to the directly retrieved source image and licence were checked;
    no image edit is proposed.
- evidence_id: boundary-coccolith
  kind: record_content
  reference: data/structures/envelope/coccolith.yaml
  locator: Identifier, label, definition and parent_structures only
  accessed_at: '2026-10-21T11:06:56Z'
  support: context_only
  summary: Boundary-only inspection distinguishes the mineral scale and assembled
    external covering from the intracellular formation vesicle. This neighbor is not
    a second target.
- evidence_id: boundary-coccosphere
  kind: record_content
  reference: data/structures/envelope/coccosphere.yaml
  locator: Identifier, label, definition and parent_structures only
  accessed_at: '2026-10-21T11:06:56Z'
  support: context_only
  summary: Boundary-only inspection distinguishes the mineral scale and assembled
    external covering from the intracellular formation vesicle. This neighbor is not
    a second target.
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml
    --verify
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:58:40.445912Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/coccolith_vesicle.yaml
    --causal-graphs
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:58:42.172597Z'
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
  reference: just validate data/structures/membrane_organelle/coccolith_vesicle.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:57:33Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/coccolith_vesicle.yaml'
  snapshot_sha256: 88ee29171cce84bc07cecfe97b63279accbbd55320ddd580569133b349ceea90
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/coccolith_vesicle.yaml
    --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/coccolith_vesicle-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:57:35Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/coccolith_vesicle.yaml\
    \ --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/coccolith_vesicle-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/coccolith_vesicle-strict.tsv"
  snapshot_sha256: f467b0656ae430501c230a760cce48a58ffbe793056e043da5975f508f661c8c
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/coccolith_vesicle.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T11:06:56Z'
  support: supports
  summary: '6 of7 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: cellstructuremech:coccolith_vesicle: SKIPPED; resolved by evidence
    record. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
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
  topic: Formation compartment distinct from mineral products
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith_vesicle
  summary: The local identifier denotes the membrane-bounded intracellular compartment
    in which coccoliths form. Its parent is intentionally broader; a coccolith is
    an individual mineral scale and a coccosphere the external assembled covering.
    Current bounded GO searches add no exact target term and do not certify historical
    exhaustive searches.
  evidence_ids:
  - record
  - policy
  - root23-sources-NCBITaxon-127549
  - root23-sources-NCBITaxon-2903
  - root23-sources-doi-10.1021_jacs.6c02151
  - root23-sources-doi-10.1038_ncomms11228
  - root23-sources-coccolith-go
  - root23-sources-coccolith-go-search
  - root23-sources-coccolithogenesis-go-search
  - root23-sources-jats-PMC13067266
  - root23-sources-coccolith2026-supplement
  - root23-sources-jats-PMC4834641
  - root23-sources-coccolith2026-s3xml
  - root23-sources-coccolith-fig2
- assessment_id: scope
  area: scope
  topic: Two directly evidenced taxa and strains
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith_vesicle
  summary: The current native taxa verify Calcidiscus leptoporus127549 and Emiliania
    huxleyi2903, with Gephyrocapsa huxleyi explicitly a synonym of the latter. The
    primary culture Methods support RCC1130 and AWI1516 respectively. The qualitative
    occurrence is restricted to these supported contexts; a population prevalence
    is not inferred from imaging.
  evidence_ids:
  - record
  - policy
  - root23-sources-NCBITaxon-127549
  - root23-sources-NCBITaxon-2903
  - root23-sources-doi-10.1021_jacs.6c02151
  - root23-sources-doi-10.1038_ncomms11228
  - root23-sources-coccolith-go
  - root23-sources-coccolith-go-search
  - root23-sources-coccolithogenesis-go-search
  - root23-sources-jats-PMC13067266
  - root23-sources-coccolith2026-supplement
  - root23-sources-jats-PMC4834641
  - root23-sources-coccolith2026-s3xml
  - root23-sources-coccolith-fig2
- assessment_id: composition
  area: grounding
  topic: Observed membrane with molecular necessity unresolved
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith_vesicle
  summary: The OTHER component denotes a structural bounding membrane and is appropriately
    grounded to GO0016020. The source directly images it. Its UNKNOWN essentiality
    and absence of asserted molecular constituents preserve the limit between observing
    a boundary and experimentally testing assembly necessity. Speculative ATPase-like
    densities and ion transport are not promoted to identified protein machinery.
  evidence_ids:
  - record
  - policy
  - root23-sources-NCBITaxon-127549
  - root23-sources-NCBITaxon-2903
  - root23-sources-doi-10.1021_jacs.6c02151
  - root23-sources-doi-10.1038_ncomms11228
  - root23-sources-coccolith-go
  - root23-sources-coccolith-go-search
  - root23-sources-coccolithogenesis-go-search
  - root23-sources-jats-PMC13067266
  - root23-sources-coccolith2026-supplement
  - root23-sources-jats-PMC4834641
  - root23-sources-coccolith2026-s3xml
  - root23-sources-coccolith-fig2
- assessment_id: function
  area: evidence
  topic: Site of intracellular mineral formation
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith_vesicle
  summary: The maintained function is a directly imaged site of crystal growth, not
    a causal mechanism for crystal shape, ion transfer or calcium storage. No causal
    graph is required for this explicitly observational record; no asserted causal
    graph is being scored as a mechanism.
  evidence_ids:
  - record
  - policy
  - root23-sources-NCBITaxon-127549
  - root23-sources-NCBITaxon-2903
  - root23-sources-doi-10.1021_jacs.6c02151
  - root23-sources-doi-10.1038_ncomms11228
  - root23-sources-coccolith-go
  - root23-sources-coccolith-go-search
  - root23-sources-coccolithogenesis-go-search
  - root23-sources-jats-PMC13067266
  - root23-sources-coccolith2026-supplement
  - root23-sources-jats-PMC4834641
  - root23-sources-coccolith2026-s3xml
  - root23-sources-coccolith-fig2
- assessment_id: image-license
  area: provenance
  topic: Traceable image, method and licence
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith_vesicle
  summary: The local Figure2 exactly matches the native retrieved bytes, the attribution
    and panel meanings match the primary caption, and native ALI metadata explicitly
    supplies CC BY4.0. The high-pressure-freeze/fracture and plunge-freeze/FIB workflows
    are distinguished correctly. No image pixels, data or record history are changed.
  evidence_ids:
  - record
  - policy
  - root23-sources-NCBITaxon-127549
  - root23-sources-NCBITaxon-2903
  - root23-sources-doi-10.1021_jacs.6c02151
  - root23-sources-doi-10.1038_ncomms11228
  - root23-sources-coccolith-go
  - root23-sources-coccolith-go-search
  - root23-sources-coccolithogenesis-go-search
  - root23-sources-jats-PMC13067266
  - root23-sources-coccolith2026-supplement
  - root23-sources-jats-PMC4834641
  - root23-sources-coccolith2026-s3xml
  - root23-sources-coccolith-fig2
  - image
- assessment_id: coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith_vesicle
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Additional exhaustive component inventories, numerical
    properties, images, traits and expanded mechanisms are optional. No verbatim quotation
    requires repair, and no status or history rewrite is proposed. This bounded review
    does not assert exhaustive literature completeness.
  evidence_ids:
  - record
  - policy
  - root23-sources-NCBITaxon-127549
  - root23-sources-NCBITaxon-2903
  - root23-sources-doi-10.1021_jacs.6c02151
  - root23-sources-doi-10.1038_ncomms11228
  - root23-sources-coccolith-go
  - root23-sources-coccolith-go-search
  - root23-sources-coccolithogenesis-go-search
  - root23-sources-jats-PMC13067266
  - root23-sources-coccolith2026-supplement
  - root23-sources-jats-PMC4834641
  - root23-sources-coccolith2026-s3xml
  - root23-sources-coccolith-fig2
  - image
  - boundary-coccolith
  - boundary-coccosphere
findings: []
actions: []
limitations:
- The complete main scientific body of Avrahami2026 and named Sviben2016 sections
  were read; the precise supplementary Methods subset is stated in evidence. This
  is not an entire-supplement or raw-data audit.
- Figure2 was visually inspected and byte/license checked. Other microscopy panels,
  tomographic volumes and inferred protein densities were not independently reanalysed.
- The neighboring coccolith and coccosphere records were read only at their identity/boundary
  fields; their full scientific claims are not reviewed here.
- Current bounded ontology queries and an ignored-inclusive local path search do not
  recertify historical exhaustive searches or prove a molecular mechanism.
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
