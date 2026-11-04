# Reservosome matrix scientific review

- Review: 20261022T034125Z-reservosome-matrix-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:25:00Z
- Finished UTC: 2026-10-22T03:41:25Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact matrix identity, internal morphology and cholesterol storage/mobilization are supported at explicit preparation and life-stage scope. The label-only constituents and nonmechanistic graph do not overclaim biogenesis; no concrete curation finding.

## Scope And Provenance

Entire single target, every field/graph/history/discussion, and the complete four-record reservosome boundary set (target plus three neighbors). Additional incoming-reference records, where frozen, were inspected only at the exact search-returned grounding lines. Native and literature read scopes are declared separately for each evidence row.

Selection: Batch40 exact path-ordered target 4; fresh f97b initial native inspect/schema/strict passed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0106125 | data/structures/membrane_organelle/reservosome_matrix.yaml | maintained | reservosome matrix |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0106125 | Focused validator passed. |
| Focused native strict | passed | True | GO:0106125 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0106125 | Native check passed; source-level gene and mechanism claims were assessed independently. |
| Individual protein verification applicability | not_applicable | False | GO:0106125 | No individual protein accession or GENE_OR_PROTEIN graph node occurs in this target; ungrounded definition names are assessed scientifically. |
| Expression-module applicability | not_applicable | False | GO:0106125 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0106125 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0106125 | 8 of 10 collected target identifiers returned OK. PMID:18452191: UNREACHABLE; Exact native MED identity independently verifies PMID, title, DOI and PMC/null mapping after bulk eutils414 failure. Abstract and body scientific scopes remain separately bounded.; cellstructuremech:reservosome: SKIPPED; Exact current local identity occurs once in an ignored-inclusive identifier search and is a frozen maintained input. Resolver existence does not overturn the independent exact-GO identity curation finding. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0106125 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0106125 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0106125 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0106125 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0106125 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Organelle, volume, matrix and membrane boundary

identity: supported. Targets: GO:0106125.

The biological referents and distinct types are consistent with native GO and the complete frozen quartet. Existing local parthood/graph links resolve uniquely. The whole-record identifier choice is separately assessed; its successors must preserve stable provenance rather than invalidate current links.

### Species, developmental stage and canonical microscopy

scope: supported. Targets: GO:0106125.

Native5693 and exact primary abstracts support the T. cruzi epimastigote example and stage-qualified occurrence. VARIABLE denotes life-cycle context, not a measured prevalence. The canonical microscopy wording matches the2008 abstract; whole-record transferrin labeling matches2004. Dm28c2009 and Y-strain2011 experiments are not silently treated as the same strain.

### Internal architecture and label-only constituents

grounding: supported. Targets: GO:0106125.

Exact GO and the2008 abstract support planar profiles, vesicles and lipid inclusions. The LIPID rows describe aggregate membrane/lipid material without falsely using a whole-organelle GO identifier as chemical grounding; OTHER vesicles are structural constituents. Exact source-neutral identities remain unresolved, and the open discussion is honest rather than a forced inventory defect.

### Cholesterol storage with preparation boundaries

graph: supported. Targets: GO:0106125.

Pereira directly supports inclusion cholesterol storage and serum-starvation depletion. The coarse NONMECHANISTIC architecture/storage graph is faithful. The2002 note accurately describes its isolated whole-organelle result; it is not read as showing ergosterol inside pure lipid inclusions or an established boundary-efflux mechanism.

### Presence versus formation requirement

evidence: unknown. Targets: GO:0106125.

No explicit essentiality is asserted.2011 shows lipid-depleted organelles, so inclusion abundance is condition-dependent and cannot be promoted to a universal formation requirement. Internal-membrane/vesicle biogenesis remains unresolved.

### Source scopes and unchanged scientific state

provenance: supported. Targets: GO:0106125.

Every target claim was read against the explicitly scoped source packet, with primary bodies, native abstracts, authority identities and search evidence distinguished. No draft claims scientific curation, promotion, persistence or publication.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/reservosome_matrix.yaml; Entire maintained YAML: every field, graph, evidence note, discussion and history | context_only | The entire target was independently read; no scientific record or status is changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; CellStructureRecord.identifier, StructuralComponent and ProteinExample classes; graph types | context_only | Exact identity, component/material versus complete structural entity, source-backed protein examples, and formation necessity are distinct contracts. Localization, catalytic function or material constitution does not demonstrate individual assembly necessity. |
| curation | docs/CURATION.md; Identifiers rules1–3, Evidence and Causal graphs sections | context_only | Use an exact GO cellular-component identity when available; preserve superseded identifiers through deprecation and successor replaces, never silently rename or reuse an identifier. Evidence applies to each actual scientific claim. |
| neighbor-reservosome | data/structures/membrane_organelle/reservosome.yaml; Complete maintained boundary neighbor | context_only | The full four-record boundary set (target plus three neighbors) was read, distinguishing the organelle, enclosed volume, internal matrix and limiting membrane. Neighbor claims are context rather than independent primary evidence. |
| neighbor-reservosome_lumen | data/structures/membrane_organelle/reservosome_lumen.yaml; Complete maintained boundary neighbor | context_only | The full four-record boundary set (target plus three neighbors) was read, distinguishing the organelle, enclosed volume, internal matrix and limiting membrane. Neighbor claims are context rather than independent primary evidence. |
| neighbor-reservosome_membrane | data/structures/membrane_organelle/reservosome_membrane.yaml; Complete maintained boundary neighbor | context_only | The full four-record boundary set (target plus three neighbors) was read, distinguishing the organelle, enclosed volume, internal matrix and limiting membrane. Neighbor claims are context rather than independent primary evidence. |
| reservosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106123,GO:0106124,GO:0106125,GO:0106126,GO:0043231,GO:0110165; Complete six exact term identities/definitions; filtered quartet typed-child relations; not a claim about every other returned child | supports | Active GO0106123 defines the posterior epimastigote endocytic storage organelle;0106124 is its enclosed volume,0106125 its planar-membrane/vesicle/lipid-inclusion matrix,0106126 its surrounding bilayer. The response directly lists all three part_of children of0106123 and their is_a links under0110165. GO0043231 supplies the intracellular membrane-bounded-organelle parent. |
| reservosome-agent-go-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106123,GO:0106124,GO:0106125,GO:0106126/ancestors?relations=is_a; Complete four is_a-only ancestor lists, including self identifiers | supports | The is_a-only response places reservosome under0043231 and the three substructure terms under0110165. It does not conflate is_a with parthood, which is independently visible in the term response. |
| reservosome-agent-tax5693 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5693; Complete native taxId/name/rank/lineage | supports | ENA5693 identifies Trypanosoma cruzi at species rank within Schizotrypanum; this authority establishes identity and lineage, not a prevalence census or experimental strain. |
| local-reservosome-resolution | rg --no-ignore --hidden -n cellstructuremech:reservosome&#124;GO:0106123 data/structures; Complete all-occurrence corpus string search, including anchored identifier inspection | supports | The ignored- and hidden-inclusive maintained corpus has one cellstructuremech:reservosome identifier declaration, the frozen whole record; GO0106123 occurs as authority references but has no identifier declaration. Incoming references include the three quartet neighbors plus cytostome and early_endosome. This resolves the local target without treating its present identifier choice as scientifically optimal. |
| reservosome-agent-figueiredo2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1017/S0031182004005797%22; Unique MED title/authors/DOI/PMID/year and complete primary abstract; original Methods/body not recovered | supports | Exact Figueiredo et al.2004 DOI10.1017/S0031182004005797/PMID15521631 primary study. Its complete abstract describes transferrin-gold during bloodstream-form differentiation, posterior reservosomes only in free-swimming epimastigotes, and cysteine-proteinase labeling of all reservosomes without tracer/enzyme colocalization in all of them. |
| reservosome-agent-santanna2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1002/jemt.20592%22; Unique MED identity and complete primary abstract; no original full body or image pixels recovered | supports | Exact Sant'Anna et al.2008 DOI10.1002/jemt.20592/PMID18452191 primary study. Complete abstract reports ultrathin, uranyl-acetate and freeze-fracture microscopy of epimastigotes and isolated reservosomes, internal profiles/vesicles and monolayer-surrounded lipid inclusions. Incoming cargo is described as entering the lumen by boundary fusion, not association with internal vesicles. |
| reservosome-agent-santanna2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1002/pmic.200800730%22; Unique MED identity and complete abstract | supports | Exact Sant'Anna et al.2009 DOI10.1002/pmic.200800730/PMID19288526/PMC2763633 primary proteomics study; metadata and abstract identify isolated whole-reservosome and membrane preparations and709 T. cruzi proteins. |
| reservosome-agent-santanna2009-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2763633/; Genuine PMC2763633 HTML: complete Introduction S1, Methods S3–S10, Results S12–S14 and Discussion S15 including complete Table1 and Figure1–3 captions. No figure pixels, supplementary protein datasets or independently cited prior experiments inspected. | supports | Dm28c epimastigote B1 and total-membrane B1M fractions contain hydrolases including cruzipain, pumps and transporters. Discussion explicitly cannot distinguish limiting from internal membranes, did not detect Rab11, and distinguishes prior immunofluorescence-only Rab11 localization from confirmed assignments. ABC/lipid mobilization and several Rab functions are hypotheses; possible contaminants/cargo and preparation/strain effects remain. Related LROs in other stages are discussed without making every such organelle the exact epimastigote reservosome class. |
| reservosome-agent-cunha2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1111/j.1574-6968.2002.tb11317.x%22; Unique MED identity and complete primary abstract only | supports | Exact Cunha-e-Silva et al.2002 DOI10.1111/j.1574-6968.2002.tb11317.x/PMID12204365 complete abstract describes a Y-strain5-day reservosome fraction, protease assays and neutral lipids including ergosterol/esterified cholesterol. It analyzes isolated organelles, not a pure lipid-inclusion or limiting-bilayer fraction. |
| reservosome-agent-pereira2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1371/journal.pone.0022359%22; Unique MED identity and complete primary abstract | supports | Exact Pereira et al.2011 DOI10.1371/journal.pone.0022359/PMID21818313/PMC3144899 identifies the primary cholesterol-storage/mobilization study. |
| reservosome-agent-pereira2011-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3144899/fullTextXML; Genuine PMC3144899 JATS: complete Introduction s1, Methods s2a–s2k, Results s3a–s3c and Discussion s4; Table1 and Figures1–10 captions read. No figure pixels or supplementary datasets independently inspected. | supports | Y-strain epimastigotes in defined FCS/LDL conditions form cholesterol/cholesteryl-ester-rich inclusions and consume them under serum starvation. The inclusion fraction lacks detected ergosterol; whole reservosomes contain1.5%, with older22% attributed to probable mitochondrial contamination. Organelles can persist with few/no inclusions. Fusion and ABCA1/Rab18 efflux models are hypotheses; the rich LIT starvation experiment did not produce metacyclic forms. |
| schema-result | just validate data/structures/membrane_organelle/reservosome_matrix.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/reservosome_matrix.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/reservosome_matrix.yaml --out /private/tmp/cellstructure-batch40-20261022-pllys1sh/reservosome_matrix-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/reservosome_matrix.yaml --out /private/tmp/cellstructure-batch40-20261022-pllys1sh/reservosome_matrix-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch40-20261022-pllys1sh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch40-20261022-pllys1sh/reservosome_matrix-strict.tsv |
| reservosome-matrix-causal-graphs | /private/tmp/cellstructure-batch40-20261022-pllys1sh/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/reservosome_matrix.yaml; Complete native read-only log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/reservosome_matrix.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 10 collected target identifiers returned OK. PMID:18452191: UNREACHABLE; Exact native MED identity independently verifies PMID, title, DOI and PMC/null mapping after bulk eutils414 failure. Abstract and body scientific scopes remain separately bounded.; cellstructuremech:reservosome: SKIPPED; Exact current local identity occurs once in an ignored-inclusive identifier search and is a frozen maintained input. Resolver existence does not overturn the independent exact-GO identity curation finding. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Figueiredo2004 and Sant'Anna2008 were verified by exact native metadata and complete abstracts. Cambridge DOI and linked PDF routes returned publisher HTML rather than a PDF; Wiley returned403. No full original body, figure pixels or strain details from these two papers are certified.
- Sant'Anna2009 EuropePMC XML returned500, but genuine legacy PMC full main science, Methods and Table1 were recovered and read. No figures or supplementary datasets were independently inspected. Whole-reservosome and total-membrane preparations do not establish limiting-membrane localization for every protein.
- The maintained stage restriction follows the exact GO class and Figueiredo abstract. Sant'Anna2009 discusses related lysosome-related organelles in other life-cycle stages; this review does not equate all such LROs with the exact epimastigote reservosome or claim all other-stage degradative compartments are absent.
- Cunha-e-Silva2002 is complete native abstract scope; its DOI route returned403. Pereira2011 full main science/Methods and captions were read, but no pixels or supplementary datasets were inspected.
- The2002 whole-organelle ergosterol estimate was revised in2011 as probably affected by mitochondrial contamination. The current inclusion function/graph claims cholesterol storage, not ergosterol enrichment of the inclusions or a proven ABCA1/Rab18 mechanism.
- The serum-starvation experiment used Y-strain epimastigotes and did not trigger metacyclogenesis; it does not establish universal lipid-inclusion abundance, biogenesis or formation necessity.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes clean reviews. Parent owns finalization/persistence and integration of the five same-base full-corpus gates.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T034125Z-reservosome-matrix-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Reservosome matrix scientific review
started_at: '2026-10-22T03:25:00Z'
finished_at: '2026-10-22T03:41:25Z'
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
summary: Exact matrix identity, internal morphology and cholesterol storage/mobilization
  are supported at explicit preparation and life-stage scope. The label-only constituents
  and nonmechanistic graph do not overclaim biogenesis; no concrete curation finding.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: data/structures/membrane_organelle/reservosome.yaml
    sha256: 0e733e8adbe97aaadfaaa43aafd271069aaa3fb14cad36f8c3281b31852e7aeb
    role: context
  - path: data/structures/membrane_organelle/reservosome_lumen.yaml
    sha256: d792cf1b253ed384ca734154902e13ebb5ac760a45635226ebe3c110bf4682a4
    role: context
  - path: data/structures/membrane_organelle/reservosome_matrix.yaml
    sha256: 96579f72d8aa8c8570ed688ff44ac93574640e579a33349333074f4b9e72a174
    role: target
  - path: data/structures/membrane_organelle/reservosome_membrane.yaml
    sha256: 73604615ebff7b587a19bac850af2728c5ff9cee59e065977e9498f59092a831
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
- target_id: GO:0106125
  path: data/structures/membrane_organelle/reservosome_matrix.yaml
  label: reservosome matrix
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/reservosome_matrix.yaml
    role: maintained scientific record
scope:
  description: Entire single target, every field/graph/history/discussion, and the
    complete four-record reservosome boundary set (target plus three neighbors). Additional
    incoming-reference records, where frozen, were inspected only at the exact search-returned
    grounding lines. Native and literature read scopes are declared separately for
    each evidence row.
  selection: Batch40 exact path-ordered target 4; fresh f97b initial native inspect/schema/strict
    passed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0106125
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0106125
  command: just validate data/structures/membrane_organelle/reservosome_matrix.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0106125
  command: just validate-strict data/structures/membrane_organelle/reservosome_matrix.yaml
    --out /private/tmp/cellstructure-batch40-20261022-pllys1sh/reservosome_matrix-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0106125
  command: /private/tmp/cellstructure-batch40-20261022-pllys1sh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/reservosome_matrix.yaml
  exit_code: 0
  summary: Native check passed; source-level gene and mechanism claims were assessed
    independently.
  evidence_ids:
  - reservosome-matrix-causal-graphs
- check_id: protein-applicability
  name: Individual protein verification applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0106125
  summary: No individual protein accession or GENE_OR_PROTEIN graph node occurs in
    this target; ungrounded definition names are assessed scientifically.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0106125
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0106125
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - neighbor-reservosome
  - neighbor-reservosome_lumen
  - neighbor-reservosome_membrane
  - reservosome-agent-go
  - reservosome-agent-go-ancestors
  - reservosome-agent-tax5693
  - local-reservosome-resolution
  - reservosome-agent-figueiredo2004-meta
  - reservosome-agent-santanna2008-meta
  - reservosome-agent-santanna2009-meta
  - reservosome-agent-santanna2009-legacy
  - reservosome-agent-cunha2002-meta
  - reservosome-agent-pereira2011-meta
  - reservosome-agent-pereira2011-xml
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0106125
  summary: '8 of 10 collected target identifiers returned OK. PMID:18452191: UNREACHABLE;
    Exact native MED identity independently verifies PMID, title, DOI and PMC/null
    mapping after bulk eutils414 failure. Abstract and body scientific scopes remain
    separately bounded.; cellstructuremech:reservosome: SKIPPED; Exact current local
    identity occurs once in an ignored-inclusive identifier search and is a frozen
    maintained input. Resolver existence does not overturn the independent exact-GO
    identity curation finding. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - reservosome-agent-santanna2008-meta
  - neighbor-reservosome
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0106125
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch40 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0106125
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch40 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0106125
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch40 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0106125
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch40 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0106125
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
    and current batch40 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/reservosome_matrix.yaml
  locator: 'Entire maintained YAML: every field, graph, evidence note, discussion
    and history'
  accessed_at: '2026-10-22T03:32:20Z'
  support: context_only
  summary: The entire target was independently read; no scientific record or status
    is changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: CellStructureRecord.identifier, StructuralComponent and ProteinExample
    classes; graph types
  accessed_at: '2026-10-22T03:32:20Z'
  support: context_only
  summary: Exact identity, component/material versus complete structural entity, source-backed
    protein examples, and formation necessity are distinct contracts. Localization,
    catalytic function or material constitution does not demonstrate individual assembly
    necessity.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Identifiers rules1–3, Evidence and Causal graphs sections
  accessed_at: '2026-10-22T03:32:20Z'
  support: context_only
  summary: Use an exact GO cellular-component identity when available; preserve superseded
    identifiers through deprecation and successor replaces, never silently rename
    or reuse an identifier. Evidence applies to each actual scientific claim.
- evidence_id: neighbor-reservosome
  kind: record_content
  reference: data/structures/membrane_organelle/reservosome.yaml
  locator: Complete maintained boundary neighbor
  accessed_at: '2026-10-22T03:32:20Z'
  support: context_only
  summary: The full four-record boundary set (target plus three neighbors) was read,
    distinguishing the organelle, enclosed volume, internal matrix and limiting membrane.
    Neighbor claims are context rather than independent primary evidence.
- evidence_id: neighbor-reservosome_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/reservosome_lumen.yaml
  locator: Complete maintained boundary neighbor
  accessed_at: '2026-10-22T03:32:20Z'
  support: context_only
  summary: The full four-record boundary set (target plus three neighbors) was read,
    distinguishing the organelle, enclosed volume, internal matrix and limiting membrane.
    Neighbor claims are context rather than independent primary evidence.
- evidence_id: neighbor-reservosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/reservosome_membrane.yaml
  locator: Complete maintained boundary neighbor
  accessed_at: '2026-10-22T03:32:20Z'
  support: context_only
  summary: The full four-record boundary set (target plus three neighbors) was read,
    distinguishing the organelle, enclosed volume, internal matrix and limiting membrane.
    Neighbor claims are context rather than independent primary evidence.
- evidence_id: reservosome-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106123,GO:0106124,GO:0106125,GO:0106126,GO:0043231,GO:0110165
  locator: Complete six exact term identities/definitions; filtered quartet typed-child
    relations; not a claim about every other returned child
  accessed_at: '2026-10-22T03:25:17.665855Z'
  support: supports
  summary: Active GO0106123 defines the posterior epimastigote endocytic storage organelle;0106124
    is its enclosed volume,0106125 its planar-membrane/vesicle/lipid-inclusion matrix,0106126
    its surrounding bilayer. The response directly lists all three part_of children
    of0106123 and their is_a links under0110165. GO0043231 supplies the intracellular
    membrane-bounded-organelle parent.
  snapshot_sha256: 1f8ae8902a5fb16d7ee0b17e585335b691ae509122b2be1de7a2db7cc7904c93
- evidence_id: reservosome-agent-go-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106123,GO:0106124,GO:0106125,GO:0106126/ancestors?relations=is_a
  locator: Complete four is_a-only ancestor lists, including self identifiers
  accessed_at: '2026-10-22T03:29:13.710157Z'
  support: supports
  summary: The is_a-only response places reservosome under0043231 and the three substructure
    terms under0110165. It does not conflate is_a with parthood, which is independently
    visible in the term response.
  snapshot_sha256: 1b14e31af3c4a78a2b2fa1d7d7147663f880f1623699e7737d54ab309ceb275e
- evidence_id: reservosome-agent-tax5693
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5693
  locator: Complete native taxId/name/rank/lineage
  accessed_at: '2026-10-22T03:25:17.666488Z'
  support: supports
  summary: ENA5693 identifies Trypanosoma cruzi at species rank within Schizotrypanum;
    this authority establishes identity and lineage, not a prevalence census or experimental
    strain.
  snapshot_sha256: 29ca5f9c41995471a462d22be4406f02aa99f2f23760f2ea91ac33282f22482f
- evidence_id: local-reservosome-resolution
  kind: search
  reference: rg --no-ignore --hidden -n cellstructuremech:reservosome|GO:0106123 data/structures
  locator: Complete all-occurrence corpus string search, including anchored identifier
    inspection
  accessed_at: '2026-10-22T03:29:31.029961Z'
  support: supports
  summary: The ignored- and hidden-inclusive maintained corpus has one cellstructuremech:reservosome
    identifier declaration, the frozen whole record; GO0106123 occurs as authority
    references but has no identifier declaration. Incoming references include the
    three quartet neighbors plus cytostome and early_endosome. This resolves the local
    target without treating its present identifier choice as scientifically optimal.
  snapshot_sha256: 4905c28c83b1643392de484c732b12bd5bdcbaba30314ffbc53538701499df30
  search_scope: All data/structures recursively including ignored and hidden files;
    exact local/GO identifier strings, all occurrences, not only declarations; current
    f97b corpus. All returned lines manually classified as identifier, grounding,
    parthood, evidence or history.
- evidence_id: reservosome-agent-figueiredo2004-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1017/S0031182004005797%22
  locator: Unique MED title/authors/DOI/PMID/year and complete primary abstract; original
    Methods/body not recovered
  accessed_at: '2026-10-22T03:25:17.667191Z'
  support: supports
  summary: Exact Figueiredo et al.2004 DOI10.1017/S0031182004005797/PMID15521631 primary
    study. Its complete abstract describes transferrin-gold during bloodstream-form
    differentiation, posterior reservosomes only in free-swimming epimastigotes, and
    cysteine-proteinase labeling of all reservosomes without tracer/enzyme colocalization
    in all of them.
  snapshot_sha256: 43dacf6cae8a9ff1f22b52d1ec026ca44b923db051a7660de47cef94c3cdc1c8
- evidence_id: reservosome-agent-santanna2008-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1002/jemt.20592%22
  locator: Unique MED identity and complete primary abstract; no original full body
    or image pixels recovered
  accessed_at: '2026-10-22T03:25:18.450316Z'
  support: supports
  summary: Exact Sant'Anna et al.2008 DOI10.1002/jemt.20592/PMID18452191 primary study.
    Complete abstract reports ultrathin, uranyl-acetate and freeze-fracture microscopy
    of epimastigotes and isolated reservosomes, internal profiles/vesicles and monolayer-surrounded
    lipid inclusions. Incoming cargo is described as entering the lumen by boundary
    fusion, not association with internal vesicles.
  snapshot_sha256: ca1bc970edc5602182448807a7905f4bd2d2781766ad0dced75354765b715c70
- evidence_id: reservosome-agent-santanna2009-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1002/pmic.200800730%22
  locator: Unique MED identity and complete abstract
  accessed_at: '2026-10-22T03:25:18.436807Z'
  support: supports
  summary: Exact Sant'Anna et al.2009 DOI10.1002/pmic.200800730/PMID19288526/PMC2763633
    primary proteomics study; metadata and abstract identify isolated whole-reservosome
    and membrane preparations and709 T. cruzi proteins.
  snapshot_sha256: 5d6f3ceed89f0e205cdd01ba7f6aa759e9ef8edc6e9ddf8054055bbc12c333d4
- evidence_id: reservosome-agent-santanna2009-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2763633/
  locator: 'Genuine PMC2763633 HTML: complete Introduction S1, Methods S3–S10, Results
    S12–S14 and Discussion S15 including complete Table1 and Figure1–3 captions. No
    figure pixels, supplementary protein datasets or independently cited prior experiments
    inspected.'
  accessed_at: '2026-10-22T03:25:57.264825Z'
  support: supports
  summary: Dm28c epimastigote B1 and total-membrane B1M fractions contain hydrolases
    including cruzipain, pumps and transporters. Discussion explicitly cannot distinguish
    limiting from internal membranes, did not detect Rab11, and distinguishes prior
    immunofluorescence-only Rab11 localization from confirmed assignments. ABC/lipid
    mobilization and several Rab functions are hypotheses; possible contaminants/cargo
    and preparation/strain effects remain. Related LROs in other stages are discussed
    without making every such organelle the exact epimastigote reservosome class.
  snapshot_sha256: 69d6be78f8c338a6304cc006628145ad4ac481e6c5aa10fd691675950dc1e869
- evidence_id: reservosome-agent-cunha2002-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1111/j.1574-6968.2002.tb11317.x%22
  locator: Unique MED identity and complete primary abstract only
  accessed_at: '2026-10-22T03:25:18.451607Z'
  support: supports
  summary: Exact Cunha-e-Silva et al.2002 DOI10.1111/j.1574-6968.2002.tb11317.x/PMID12204365
    complete abstract describes a Y-strain5-day reservosome fraction, protease assays
    and neutral lipids including ergosterol/esterified cholesterol. It analyzes isolated
    organelles, not a pure lipid-inclusion or limiting-bilayer fraction.
  snapshot_sha256: 11cb05d03ef1336ef1637f1ce498c91e7748ae582d8aee4518a0f5b4630f81fa
- evidence_id: reservosome-agent-pereira2011-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1371/journal.pone.0022359%22
  locator: Unique MED identity and complete primary abstract
  accessed_at: '2026-10-22T03:25:18.592886Z'
  support: supports
  summary: Exact Pereira et al.2011 DOI10.1371/journal.pone.0022359/PMID21818313/PMC3144899
    identifies the primary cholesterol-storage/mobilization study.
  snapshot_sha256: d51ccf88d88fc3dc623b2dfa73d7d0665b0524d5db0698652e630c2fe6aa9f97
- evidence_id: reservosome-agent-pereira2011-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3144899/fullTextXML
  locator: 'Genuine PMC3144899 JATS: complete Introduction s1, Methods s2a–s2k, Results
    s3a–s3c and Discussion s4; Table1 and Figures1–10 captions read. No figure pixels
    or supplementary datasets independently inspected.'
  accessed_at: '2026-10-22T03:25:57.264949Z'
  support: supports
  summary: Y-strain epimastigotes in defined FCS/LDL conditions form cholesterol/cholesteryl-ester-rich
    inclusions and consume them under serum starvation. The inclusion fraction lacks
    detected ergosterol; whole reservosomes contain1.5%, with older22% attributed
    to probable mitochondrial contamination. Organelles can persist with few/no inclusions.
    Fusion and ABCA1/Rab18 efflux models are hypotheses; the rich LIT starvation experiment
    did not produce metacyclic forms.
  snapshot_sha256: c3217d07622d7ebc3d2570502d336b68dd0920266ea5b36e919e6a4cb3e1d1fb
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/reservosome_matrix.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:25:02Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/reservosome_matrix.yaml'
  snapshot_sha256: fab4af008f90e99404a31fa4ac81cdaf84b5bd576dfe8ce3d9d4914b19c4aa4a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/reservosome_matrix.yaml
    --out /private/tmp/cellstructure-batch40-20261022-pllys1sh/reservosome_matrix-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:25:04Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/reservosome_matrix.yaml\
    \ --out /private/tmp/cellstructure-batch40-20261022-pllys1sh/reservosome_matrix-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch40-20261022-pllys1sh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch40-20261022-pllys1sh/reservosome_matrix-strict.tsv"
  snapshot_sha256: 721ae5fcca1c200a07f7ec6fffe0a98919d3b7169217c660c277b8add6b81f63
- evidence_id: reservosome-matrix-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch40-20261022-pllys1sh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/reservosome_matrix.yaml
  locator: Complete native read-only log
  accessed_at: '2026-10-22T03:29:59.872495Z'
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
  locator: data/structures/membrane_organelle/reservosome_matrix.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 10 collected target identifiers returned OK. PMID:18452191: UNREACHABLE;
    Exact native MED identity independently verifies PMID, title, DOI and PMC/null
    mapping after bulk eutils414 failure. Abstract and body scientific scopes remain
    separately bounded.; cellstructuremech:reservosome: SKIPPED; Exact current local
    identity occurs once in an ignored-inclusive identifier search and is a frozen
    maintained input. Resolver existence does not overturn the independent exact-GO
    identity curation finding. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
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
  topic: Organelle, volume, matrix and membrane boundary
  outcome: supported
  target_ids:
  - GO:0106125
  summary: The biological referents and distinct types are consistent with native
    GO and the complete frozen quartet. Existing local parthood/graph links resolve
    uniquely. The whole-record identifier choice is separately assessed; its successors
    must preserve stable provenance rather than invalidate current links.
  evidence_ids:
  - record
  - reservosome-agent-go
  - reservosome-agent-go-ancestors
  - local-reservosome-resolution
- assessment_id: scope
  area: scope
  topic: Species, developmental stage and canonical microscopy
  outcome: supported
  target_ids:
  - GO:0106125
  summary: Native5693 and exact primary abstracts support the T. cruzi epimastigote
    example and stage-qualified occurrence. VARIABLE denotes life-cycle context, not
    a measured prevalence. The canonical microscopy wording matches the2008 abstract;
    whole-record transferrin labeling matches2004. Dm28c2009 and Y-strain2011 experiments
    are not silently treated as the same strain.
  evidence_ids:
  - record
  - reservosome-agent-tax5693
  - reservosome-agent-figueiredo2004-meta
  - reservosome-agent-santanna2008-meta
  - reservosome-agent-santanna2009-legacy
  - reservosome-agent-pereira2011-xml
- assessment_id: composition
  area: grounding
  topic: Internal architecture and label-only constituents
  outcome: supported
  target_ids:
  - GO:0106125
  summary: Exact GO and the2008 abstract support planar profiles, vesicles and lipid
    inclusions. The LIPID rows describe aggregate membrane/lipid material without
    falsely using a whole-organelle GO identifier as chemical grounding; OTHER vesicles
    are structural constituents. Exact source-neutral identities remain unresolved,
    and the open discussion is honest rather than a forced inventory defect.
  evidence_ids:
  - record
  - schema
  - reservosome-agent-go
  - reservosome-agent-santanna2008-meta
  - reservosome-agent-pereira2011-xml
- assessment_id: function-graph
  area: graph
  topic: Cholesterol storage with preparation boundaries
  outcome: supported
  target_ids:
  - GO:0106125
  summary: Pereira directly supports inclusion cholesterol storage and serum-starvation
    depletion. The coarse NONMECHANISTIC architecture/storage graph is faithful. The2002
    note accurately describes its isolated whole-organelle result; it is not read
    as showing ergosterol inside pure lipid inclusions or an established boundary-efflux
    mechanism.
  evidence_ids:
  - record
  - reservosome-agent-go
  - reservosome-agent-cunha2002-meta
  - reservosome-agent-pereira2011-xml
- assessment_id: necessity
  area: evidence
  topic: Presence versus formation requirement
  outcome: unknown
  target_ids:
  - GO:0106125
  summary: No explicit essentiality is asserted.2011 shows lipid-depleted organelles,
    so inclusion abundance is condition-dependent and cannot be promoted to a universal
    formation requirement. Internal-membrane/vesicle biogenesis remains unresolved.
  evidence_ids:
  - record
  - schema
  - reservosome-agent-pereira2011-xml
- assessment_id: provenance
  area: provenance
  topic: Source scopes and unchanged scientific state
  outcome: supported
  target_ids:
  - GO:0106125
  summary: Every target claim was read against the explicitly scoped source packet,
    with primary bodies, native abstracts, authority identities and search evidence
    distinguished. No draft claims scientific curation, promotion, persistence or
    publication.
  evidence_ids:
  - record
  - reservosome-agent-go
  - reservosome-agent-go-ancestors
  - reservosome-agent-tax5693
  - reservosome-agent-figueiredo2004-meta
  - reservosome-agent-santanna2008-meta
  - reservosome-agent-santanna2009-meta
  - reservosome-agent-santanna2009-legacy
  - reservosome-agent-cunha2002-meta
  - reservosome-agent-pereira2011-meta
  - reservosome-agent-pereira2011-xml
findings: []
actions: []
limitations:
- Figueiredo2004 and Sant'Anna2008 were verified by exact native metadata and complete
  abstracts. Cambridge DOI and linked PDF routes returned publisher HTML rather than
  a PDF; Wiley returned403. No full original body, figure pixels or strain details
  from these two papers are certified.
- Sant'Anna2009 EuropePMC XML returned500, but genuine legacy PMC full main science,
  Methods and Table1 were recovered and read. No figures or supplementary datasets
  were independently inspected. Whole-reservosome and total-membrane preparations
  do not establish limiting-membrane localization for every protein.
- The maintained stage restriction follows the exact GO class and Figueiredo abstract.
  Sant'Anna2009 discusses related lysosome-related organelles in other life-cycle
  stages; this review does not equate all such LROs with the exact epimastigote reservosome
  or claim all other-stage degradative compartments are absent.
- Cunha-e-Silva2002 is complete native abstract scope; its DOI route returned403.
  Pereira2011 full main science/Methods and captions were read, but no pixels or supplementary
  datasets were inspected.
- The2002 whole-organelle ergosterol estimate was revised in2011 as probably affected
  by mitochondrial contamination. The current inclusion function/graph claims cholesterol
  storage, not ergosterol enrichment of the inclusions or a proven ABCA1/Rab18 mechanism.
- The serum-starvation experiment used Y-strain epimastigotes and did not trigger
  metacyclogenesis; it does not establish universal lipid-inclusion abundance, biogenesis
  or formation necessity.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes clean reviews. Parent owns finalization/persistence
  and integration of the five same-base full-corpus gates.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
