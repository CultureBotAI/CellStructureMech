# Cmg complex scientific review

- Review: 20261022T050522Z-cmg-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:47:31Z
- Finished UTC: 2026-10-22T05:05:22Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

CMG identity, subcomplex boundaries and replication graph are supported. Two minor findings resolve Cdc45 grounding and distinguish the reference protein strain from the canonical study scope.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph claims and completeness.

Selection: Target 10 of batch47 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0071162 | data/structures/other/cmg_complex.yaml | maintained | CMG complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0071162 | Focused validator passed. |
| Focused native strict | passed | True | GO:0071162 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0071162 | Focused native check passed; claim-level support assessed separately. |
| Focused native verify | passed | True | GO:0071162 | Focused native check passed; claim-level support assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0071162 | No expression-module claim is maintained. |
| Claim-level scientific review | passed | True | GO:0071162 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0071162 | 9 of 11 collected target identifiers returned OK. PMID:19228417: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:9619628: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0071162 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0071162 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0071162 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0071162 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0071162 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### CMG retains distinct constituent subcomplexes

identity: supported. Targets: GO:0071162.

GO0071162 identifies CMG and its native preinitiation-complex parent. GINS and MCM are appropriately modeled as separately grounded constituent complexes, with one Cdc45 protein, rather than flattened or confused with an inactive loaded MCM assembly.

### Cdc45 has an exact whole-protein family

grounding: concern. Targets: GO:0071162.

Native IPR003874 directly identifies Cdc45 and is linked from O74113. The one-GINS, one-MCM, one-Cdc45 component model is consistent with the GO definition and does not claim that this BiFC experiment resolved full stoichiometry.

### Correct Cdc45 homolog with taxonomic-label precision needed

grounding: concern. Targets: GO:0071162.

O74113 is the reviewed sna41-encoded Cdc45 homolog. The CDC45 query result is a symbol distinction; it does not invalidate this representative. Its taxon284812 is the972h- reference strain and should have that precise label.

### Function and BiFC proximity do not resolve full assembly necessity

grounding: unknown. Targets: GO:0071162.

All three UNKNOWN fields remain appropriate for the assessed evidence. Essential DNA-replication function, tag synthetic lethality and Psf1-Mcm4 proximity do not independently establish a full CMG formation/depletion matrix.

### Separate broad eukaryotic machinery from the experiment strain

scope: concern. Targets: GO:0071162.

The eukaryotic COMMON assertion is a qualitative most-members/losses-exception synthesis from the source context. The canonical experimental note is species-level S.pombe but uses the972h- taxon identifier; the primary study includes multiple mating types and a diploid, so species4896 is the supported scope absent an explicit narrower strain mapping.

### DNA-replication role with a limited interaction assay

evidence: supported. Targets: GO:0071162.

GO and the native abstract support the general replication/helicase role. The full primary study demonstrates Psf1-Mcm4 association under specific conditions and warns of YFP trapping; it is not a direct purified-CMG unwinding assay or proof of a successful Cdc45 BiFC interaction.

### Appropriately nonmechanistic CMG function graph

graph: supported. Targets: GO:0071162.

Constituent contributions and replication support are correctly directed. NONMECHANISTIC withholds unresolved ring activation, interfaces and replisome coupling rather than importing experimental BiFC limitations as biological absence.

### Family identity and canonical taxon scope are actionable

completeness: supported. Targets: GO:0071162.

All fields and localization citation identities were checked. Ground the Cdc45 family and reconcile strain/species labeling; retain the exact accession and all three complex constituents.

## Findings

### F1: Ground the verified Cdc45 family

minor / open / confirmed; issue key: cmg-cdc45-exact-family.

Cdc45 remains REVIEWED_LABEL_ONLY although IPR003874 is the exact whole-protein family and is independently linked from the maintained reviewed O74113 example.

### F2: Distinguish the reference strain from the canonical study scope

minor / open / confirmed; issue key: cmg-strain-versus-species-scope.

Taxon284812 denotes S.pombe972h-, but both the O74113 example label and the canonical label say only S.pombe. O74113 correctly belongs to that reference strain; the cited BiFC study instead reports h-S/h+S strains and a diploid without establishing an exclusively972h- assay. The canonical note therefore exceeds the supported strain precision.

## Recommended Actions And Acceptance Checks

### A1

Add IPR003874 and reconcile the Cdc45 grounding note/TODO while retaining GINS/MCM subcomplex boundaries and the supported sna41 example.

- Verify exact source identities and reconcile the specified current fields and TODO scope.
- Preserve supported accessions and membership; retain assay, lineage and uncertainty limits.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.

### A2

Retain O74113/taxon284812 and label its reference strain precisely. Use species4896 for the general canonical experimental system unless a directly verified strain-specific mapping is supplied; do not transfer the protein reference strain automatically onto all experimental strains.

- Verify exact source identities and reconcile the specified current fields and TODO scope.
- Preserve supported accessions and membership; retain assay, lineage and uncertainty limits.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/cmg_complex.yaml; Entire maintained target, history, components, evidence, discussions and graphs | context_only | All maintained fields were read; history is provenance rather than independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Components, essentiality, COMMON and graph scope | context_only | Whole-protein families differ from shared domains and individual examples. Formation necessity differs from functional and cellular essentiality. COMMON means present in most members, with losses the exception. |
| curation | docs/CURATION.md; Source identity, exact grounding and claim-specific support | context_only | Reviewed label-only means no exact term exists. Verified whole-protein identity may be grounded independently of its separately evidenced role in a complex. Canonical taxon scope must match the cited experiment. |
| root47-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0006260,GO:0006338,GO:0006974,GO:0008623,GO:0015030,GO:0016604,GO:0030896,GO:0031010,GO:0031124,GO:0031261,GO:0031981,GO:0042555,GO:0071162,GO:0071920,GO:0140513; All16 requested terms: complete id/name/active/definition/synonyms/comments and relevant maintained typed links, not every descendant | supports | The requested native GO identities, definitions, synonyms and inspected maintained typed relationships agree with the target classes and functions. Missing direct ontology links alone do not disprove sourced biological parthood. |
| root47-sources-pmid-19228417 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19228417+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED19228417: MCM-GINS and MCM-MCM interactions in vivo visualised by bimolecular fluorescence complementation in fission yeast. DOI 10.1186/1471-2121-10-12. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-9619628 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9619628+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED9619628: Identification of sna41 gene, which is the suppressor of nda4 mutation and is involved in DNA replication in Schizosaccharomyces pombe. DOI 10.1046/j.1365-2443.1998.00177.x. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-protein-O74113 | https://rest.uniprot.org/uniprotkb/O74113.json; Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro/Pfam cross-references | supports | O74113 agrees with the maintained reviewed entry, protein name, gene identity and taxon identifier. Membership and experimental source scope are assessed separately. |
| root47-sources-gene-sna41-284812 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Asna41%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and all result accession/status/name/gene/taxon fields | supports | The exact reviewed gene/taxon query returns one result, matching the maintained accession, status, names and taxon. |
| root47-sources-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete native taxonomy response | supports | ENA verifies taxon 2759 and its rank, name and lineage. Species and strain identities are kept distinct. |
| root47-sources-tax4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; Complete native taxonomy response | supports | ENA verifies taxon 4896 and its rank, name and lineage. Species and strain identities are kept distinct. |
| root47-sources-tax284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Complete native taxonomy response | supports | ENA verifies taxon 284812 and its rank, name and lineage. Species and strain identities are kept distinct. |
| root47-sources-ipr-IPR003874 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003874/; Complete accession/name/type/description, curation flags and family metadata | supports | IPR003874 is a family named CDC45. Complete native description and its curation flags were inspected; example cross-references provide an independent identity join. This annotation is not primary evidence of complex membership. |
| root47-sources-gene-CDC45-284812 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACDC45%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and empty results; compared with exact sna41 result | supports | The exact reviewed CDC45 symbol query in taxon284812 returns zero entries, while the sna41 query returns O74113, whose recommended protein identity is the Cdc45 homolog. This is a nomenclature distinction, not evidence that Cdc45 is biologically absent. |
| root47-sources-legacy-PMC2652428 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2652428/?report=reader; Complete Results/Discussion sec5 including Table1/Fig1–3 captions, Conclusion sec6 and Methods sec8/9/10/11/12/13; Background not certified | supports | Native-locus BiFC detects Psf1-Mcm4 interaction on chromatin in S-phase and HU-treated cells. The Cdc45 pairing gives no signal; many tag combinations are inviable, and tight YFP-fragment association may trap complexes, preventing normal dynamic interpretation. Table1 includes h-S, h+S and a diploid rather than an exclusively972h- experiment. |
| schema-result | just validate data/structures/other/cmg_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/cmg_complex.yaml |
| strict-result | just validate-strict data/structures/other/cmg_complex.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/cmg_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/cmg_complex.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/cmg_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/cmg_complex-strict.tsv |
| native-cmg_complex-causal-graphs | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cmg_complex.yaml; Complete focused native report | supports | data/structures/other/cmg_complex.yaml  (GO:0071162)<br>  cmg_supports_dna_unwinding	cdc45_protein	COVERED	-&gt;cdc45_protein (UniProtKB:O74113)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-cmg_complex-verify | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/cmg_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/cmg_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 11 collected target identifiers returned OK. PMID:19228417: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:9619628: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw experimental data, supplementary files or sequence alignments were reanalyzed. Primary-body inspection is limited to the explicitly listed sections.
- Miyake/Yamashita1998 was read at complete native metadata/abstract level only. No complete CMG helicase purification or primary unwinding assay was independently inspected.
- The BiFC study cannot establish normal interaction dynamics because YFP fragments may trap complexes; failed tagged pairings are not evidence that native subunits fail to associate.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes reviews for all uncovered records, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T050522Z-cmg-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cmg complex scientific review
started_at: '2026-10-22T04:47:31Z'
finished_at: '2026-10-22T05:05:22Z'
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
summary: CMG identity, subcomplex boundaries and replication graph are supported.
  Two minor findings resolve Cdc45 grounding and distinguish the reference protein
  strain from the canonical study scope.
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
  - path: data/structures/other/cmg_complex.yaml
    sha256: c7ce81a2d35df2983545756bf9b962097d595b50ddeb4fa8de3e08e07cfd1ee4
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
- target_id: GO:0071162
  path: data/structures/other/cmg_complex.yaml
  label: CMG complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cmg_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph claims and completeness.
  selection: Target 10 of batch47 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0071162
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0071162
  command: just validate data/structures/other/cmg_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0071162
  command: just validate-strict data/structures/other/cmg_complex.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/cmg_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-cmg_complex-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0071162
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cmg_complex.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-cmg_complex-causal-graphs
- check_id: native-cmg_complex-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0071162
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/cmg_complex.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-cmg_complex-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0071162
  summary: No expression-module claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0071162
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root47-sources-go
  - root47-sources-pmid-19228417
  - root47-sources-pmid-9619628
  - root47-sources-protein-O74113
  - root47-sources-gene-sna41-284812
  - root47-sources-tax2759
  - root47-sources-tax4896
  - root47-sources-tax284812
  - root47-sources-ipr-IPR003874
  - root47-sources-gene-CDC45-284812
  - root47-sources-legacy-PMC2652428
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0071162
  summary: '9 of 11 collected target identifiers returned OK. PMID:19228417: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:9619628:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root47-sources-pmid-19228417
  - root47-sources-pmid-9619628
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0071162
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0071162
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0071162
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0071162
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0071162
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
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/cmg_complex.yaml
  locator: Entire maintained target, history, components, evidence, discussions and
    graphs
  accessed_at: '2026-10-22T04:59:19Z'
  support: context_only
  summary: All maintained fields were read; history is provenance rather than independent
    scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Components, essentiality, COMMON and graph scope
  accessed_at: '2026-10-22T04:59:19Z'
  support: context_only
  summary: Whole-protein families differ from shared domains and individual examples.
    Formation necessity differs from functional and cellular essentiality. COMMON
    means present in most members, with losses the exception.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Source identity, exact grounding and claim-specific support
  accessed_at: '2026-10-22T04:59:19Z'
  support: context_only
  summary: Reviewed label-only means no exact term exists. Verified whole-protein
    identity may be grounded independently of its separately evidenced role in a complex.
    Canonical taxon scope must match the cited experiment.
- evidence_id: root47-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0006260,GO:0006338,GO:0006974,GO:0008623,GO:0015030,GO:0016604,GO:0030896,GO:0031010,GO:0031124,GO:0031261,GO:0031981,GO:0042555,GO:0071162,GO:0071920,GO:0140513
  locator: 'All16 requested terms: complete id/name/active/definition/synonyms/comments
    and relevant maintained typed links, not every descendant'
  accessed_at: '2026-10-22T04:47:53.214339Z'
  support: supports
  summary: The requested native GO identities, definitions, synonyms and inspected
    maintained typed relationships agree with the target classes and functions. Missing
    direct ontology links alone do not disprove sourced biological parthood.
  snapshot_sha256: 7e9a7e9f97cb8700350b218ea7610079c613603a48f19d04ce36665e94dc65ef
- evidence_id: root47-sources-pmid-19228417
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19228417+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:48:00.499906Z'
  support: supports
  summary: 'MED19228417: MCM-GINS and MCM-MCM interactions in vivo visualised by bimolecular
    fluorescence complementation in fission yeast. DOI 10.1186/1471-2121-10-12. Complete
    native bibliographic identity and abstract were inspected. This row certifies
    abstract-level access only; body inspection is recorded separately.'
  snapshot_sha256: 7a241d4de53fb3278c405634bb2418f8ad6ff1c640d26d59eee13d7c9a3dcf2d
- evidence_id: root47-sources-pmid-9619628
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9619628+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:48:00.728538Z'
  support: supports
  summary: 'MED9619628: Identification of sna41 gene, which is the suppressor of nda4
    mutation and is involved in DNA replication in Schizosaccharomyces pombe. DOI
    10.1046/j.1365-2443.1998.00177.x. Complete native bibliographic identity and abstract
    were inspected. This row certifies abstract-level access only; body inspection
    is recorded separately.'
  snapshot_sha256: 8d81f68c286bd825719423c55e487fb5cd85dc38153e12fb2bc183ccfc1c6b9f
- evidence_id: root47-sources-protein-O74113
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O74113.json
  locator: Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION and SIMILARITY comments; InterPro/Pfam cross-references
  accessed_at: '2026-10-22T04:47:54.043900Z'
  support: supports
  summary: O74113 agrees with the maintained reviewed entry, protein name, gene identity
    and taxon identifier. Membership and experimental source scope are assessed separately.
  snapshot_sha256: 0a78020aed917ca15d9f1560fe4677a817885a421693c826aaad0184706cbe4e
- evidence_id: root47-sources-gene-sna41-284812
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Asna41%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and all result accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:48:50.042001Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one result, matching the maintained
    accession, status, names and taxon.
  snapshot_sha256: 7fb0a67254702fa88679a9576bad802424a40e6a9f24b2ff592f652e390ac072
- evidence_id: root47-sources-tax2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:47:53.215529Z'
  support: supports
  summary: ENA verifies taxon 2759 and its rank, name and lineage. Species and strain
    identities are kept distinct.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: root47-sources-tax4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:47:53.215328Z'
  support: supports
  summary: ENA verifies taxon 4896 and its rank, name and lineage. Species and strain
    identities are kept distinct.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: root47-sources-tax284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:47:53.215600Z'
  support: supports
  summary: ENA verifies taxon 284812 and its rank, name and lineage. Species and strain
    identities are kept distinct.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: root47-sources-ipr-IPR003874
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003874/
  locator: Complete accession/name/type/description, curation flags and family metadata
  accessed_at: '2026-10-22T04:48:43.432563Z'
  support: supports
  summary: IPR003874 is a family named CDC45. Complete native description and its
    curation flags were inspected; example cross-references provide an independent
    identity join. This annotation is not primary evidence of complex membership.
  snapshot_sha256: 580caef553ebf001a0fece61778bae151bde22735cc960091381b8c90b4a4646
- evidence_id: root47-sources-gene-CDC45-284812
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACDC45%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and empty results; compared with exact sna41 result
  accessed_at: '2026-10-22T04:48:49.793665Z'
  support: supports
  summary: The exact reviewed CDC45 symbol query in taxon284812 returns zero entries,
    while the sna41 query returns O74113, whose recommended protein identity is the
    Cdc45 homolog. This is a nomenclature distinction, not evidence that Cdc45 is
    biologically absent.
  snapshot_sha256: e286802fb4f0964548f49b3b3c5f7eabd0f999b4c3d3a2e0e947320f308cb072
- evidence_id: root47-sources-legacy-PMC2652428
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2652428/?report=reader
  locator: Complete Results/Discussion sec5 including Table1/Fig1–3 captions, Conclusion
    sec6 and Methods sec8/9/10/11/12/13; Background not certified
  accessed_at: '2026-10-22T04:48:50.676697Z'
  support: supports
  summary: Native-locus BiFC detects Psf1-Mcm4 interaction on chromatin in S-phase
    and HU-treated cells. The Cdc45 pairing gives no signal; many tag combinations
    are inviable, and tight YFP-fragment association may trap complexes, preventing
    normal dynamic interpretation. Table1 includes h-S, h+S and a diploid rather than
    an exclusively972h- experiment.
  snapshot_sha256: 22903b0d9c86cf5a99481b1b2fd6740ac02309e614ba2ba11405de615485cca2
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/cmg_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:33Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/cmg_complex.yaml'
  snapshot_sha256: 9c03a927e4b060d226a5e70f1c80e907a577377ee074d9550b4f14b5b3f4d4b7
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/cmg_complex.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/cmg_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:34Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/cmg_complex.yaml\
    \ --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/cmg_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/cmg_complex-strict.tsv"
  snapshot_sha256: 245d2f7a7f7775836650faff3f5e64ecba237f2d1549c4e0bf9468611dc2062a
- evidence_id: native-cmg_complex-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cmg_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:48:08.245306Z'
  support: supports
  summary: "data/structures/other/cmg_complex.yaml  (GO:0071162)\n  cmg_supports_dna_unwinding\t\
    cdc45_protein\tCOVERED\t->cdc45_protein (UniProtKB:O74113)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     1  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     1  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 7ddce78a3a8c451ae442bdb8710db9b3f515ee0df0849ff6b0445b7aefab6f00
- evidence_id: native-cmg_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/cmg_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:48:10.575045Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/cmg_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '9 of 11 collected target identifiers returned OK. PMID:19228417: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:9619628:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
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
  topic: CMG retains distinct constituent subcomplexes
  outcome: supported
  target_ids:
  - GO:0071162
  summary: GO0071162 identifies CMG and its native preinitiation-complex parent. GINS
    and MCM are appropriately modeled as separately grounded constituent complexes,
    with one Cdc45 protein, rather than flattened or confused with an inactive loaded
    MCM assembly.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC2652428
  - root47-sources-pmid-19228417
- assessment_id: composition
  area: grounding
  topic: Cdc45 has an exact whole-protein family
  outcome: concern
  target_ids:
  - GO:0071162
  summary: Native IPR003874 directly identifies Cdc45 and is linked from O74113. The
    one-GINS, one-MCM, one-Cdc45 component model is consistent with the GO definition
    and does not claim that this BiFC experiment resolved full stoichiometry.
  evidence_ids:
  - record
  - curation
  - root47-sources-go
  - root47-sources-ipr-IPR003874
  - root47-sources-protein-O74113
- assessment_id: examples
  area: grounding
  topic: Correct Cdc45 homolog with taxonomic-label precision needed
  outcome: concern
  target_ids:
  - GO:0071162
  summary: O74113 is the reviewed sna41-encoded Cdc45 homolog. The CDC45 query result
    is a symbol distinction; it does not invalidate this representative. Its taxon284812
    is the972h- reference strain and should have that precise label.
  evidence_ids:
  - record
  - root47-sources-gene-CDC45-284812
  - root47-sources-protein-O74113
  - root47-sources-gene-sna41-284812
  - root47-sources-tax2759
  - root47-sources-tax4896
  - root47-sources-tax284812
- assessment_id: necessity
  area: grounding
  topic: Function and BiFC proximity do not resolve full assembly necessity
  outcome: unknown
  target_ids:
  - GO:0071162
  summary: All three UNKNOWN fields remain appropriate for the assessed evidence.
    Essential DNA-replication function, tag synthetic lethality and Psf1-Mcm4 proximity
    do not independently establish a full CMG formation/depletion matrix.
  evidence_ids:
  - record
  - schema
  - root47-sources-legacy-PMC2652428
- assessment_id: scope
  area: scope
  topic: Separate broad eukaryotic machinery from the experiment strain
  outcome: concern
  target_ids:
  - GO:0071162
  summary: The eukaryotic COMMON assertion is a qualitative most-members/losses-exception
    synthesis from the source context. The canonical experimental note is species-level
    S.pombe but uses the972h- taxon identifier; the primary study includes multiple
    mating types and a diploid, so species4896 is the supported scope absent an explicit
    narrower strain mapping.
  evidence_ids:
  - record
  - schema
  - root47-sources-legacy-PMC2652428
  - root47-sources-pmid-19228417
  - root47-sources-tax2759
  - root47-sources-tax4896
  - root47-sources-tax284812
- assessment_id: function
  area: evidence
  topic: DNA-replication role with a limited interaction assay
  outcome: supported
  target_ids:
  - GO:0071162
  summary: GO and the native abstract support the general replication/helicase role.
    The full primary study demonstrates Psf1-Mcm4 association under specific conditions
    and warns of YFP trapping; it is not a direct purified-CMG unwinding assay or
    proof of a successful Cdc45 BiFC interaction.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC2652428
  - root47-sources-pmid-9619628
- assessment_id: graph
  area: graph
  topic: Appropriately nonmechanistic CMG function graph
  outcome: supported
  target_ids:
  - GO:0071162
  summary: Constituent contributions and replication support are correctly directed.
    NONMECHANISTIC withholds unresolved ring activation, interfaces and replisome
    coupling rather than importing experimental BiFC limitations as biological absence.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC2652428
- assessment_id: coverage
  area: completeness
  topic: Family identity and canonical taxon scope are actionable
  outcome: supported
  target_ids:
  - GO:0071162
  summary: All fields and localization citation identities were checked. Ground the
    Cdc45 family and reconcile strain/species labeling; retain the exact accession
    and all three complex constituents.
  evidence_ids:
  - record
  - root47-sources-ipr-IPR003874
  - root47-sources-legacy-PMC2652428
  - root47-sources-tax2759
  - root47-sources-tax4896
  - root47-sources-tax284812
  - root47-sources-protein-O74113
findings:
- finding_id: F1
  issue_key: cmg-cdc45-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the verified Cdc45 family
  description: Cdc45 remains REVIEWED_LABEL_ONLY although IPR003874 is the exact whole-protein
    family and is independently linked from the maintained reviewed O74113 example.
  target_ids:
  - GO:0071162
  field_paths:
  - components[2].grounding_status
  - components[2].grounding_notes
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root47-sources-ipr-IPR003874
  - root47-sources-protein-O74113
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cmg_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and claim-specific source scope
  native_severity: minor
  normalization_reason: Bounded evidence-backed curation correction; supported structural
    identity and constituent membership remain intact. Historical search honesty is
    not questioned.
- finding_id: F2
  issue_key: cmg-strain-versus-species-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish the reference strain from the canonical study scope
  description: Taxon284812 denotes S.pombe972h-, but both the O74113 example label
    and the canonical label say only S.pombe. O74113 correctly belongs to that reference
    strain; the cited BiFC study instead reports h-S/h+S strains and a diploid without
    establishing an exclusively972h- assay. The canonical note therefore exceeds the
    supported strain precision.
  target_ids:
  - GO:0071162
  field_paths:
  - components[2].protein_examples[0].taxon_label
  - canonical_examples[0].taxon_id
  - canonical_examples[0].taxon_label
  - canonical_examples[0].note
  evidence_ids:
  - record
  - root47-sources-legacy-PMC2652428
  - root47-sources-protein-O74113
  - root47-sources-tax2759
  - root47-sources-tax4896
  - root47-sources-tax284812
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cmg_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and claim-specific source scope
  native_severity: minor
  normalization_reason: Bounded evidence-backed curation correction; supported structural
    identity and constituent membership remain intact. Historical search honesty is
    not questioned.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0071162
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cmg_complex.yaml
    role: maintained scientific record
  description: Add IPR003874 and reconcile the Cdc45 grounding note/TODO while retaining
    GINS/MCM subcomplex boundaries and the supported sna41 example.
  acceptance_checks:
  - Verify exact source identities and reconcile the specified current fields and
    TODO scope.
  - Preserve supported accessions and membership; retain assay, lineage and uncertainty
    limits.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0071162
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cmg_complex.yaml
    role: maintained scientific record
  description: Retain O74113/taxon284812 and label its reference strain precisely.
    Use species4896 for the general canonical experimental system unless a directly
    verified strain-specific mapping is supplied; do not transfer the protein reference
    strain automatically onto all experimental strains.
  acceptance_checks:
  - Verify exact source identities and reconcile the specified current fields and
    TODO scope.
  - Preserve supported accessions and membership; retain assay, lineage and uncertainty
    limits.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw experimental data, supplementary files or sequence alignments
  were reanalyzed. Primary-body inspection is limited to the explicitly listed sections.
- Miyake/Yamashita1998 was read at complete native metadata/abstract level only. No
  complete CMG helicase purification or primary unwinding assay was independently
  inspected.
- The BiFC study cannot establish normal interaction dynamics because YFP fragments
  may trap complexes; failed tagged pairings are not evidence that native subunits
  fail to associate.
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
