# Contractile vacuole lumen identity, compartment topology and evidence review

- Review: 20261022T005253Z-contractile-vacuole-lumen-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T11:11:11Z
- Finished UTC: 2026-10-22T00:52:53Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact SL-defined lumen identity, broader GO parent, organelle parthood, membrane boundary and scoped filling/discharge examples are coherent. No concrete curation defect was established.

## Scope And Provenance

Entire target reviewed: local identity, ontology/SL relations, distribution, canonical examples, water-accumulation function, both topology edges, evidence, discussion and history.

Selection: User-authorized all-record pass; batch24 indices1–4 are four distinct maintained contractile-vacuole records, each reviewed in full.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:contractile_vacuole_lumen | data/structures/membrane_organelle/contractile_vacuole_lumen.yaml | maintained | contractile vacuole lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | cellstructuremech:contractile_vacuole_lumen | Native command returned zero. Coverage warnings are interpreted separately from accession verification. |
| Native protein causal-graphs | passed | True | cellstructuremech:contractile_vacuole_lumen | Native command returned zero. Coverage warnings are interpreted separately from accession verification. |
| Focused native schema | passed | True | cellstructuremech:contractile_vacuole_lumen | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:contractile_vacuole_lumen | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:contractile_vacuole_lumen | 11 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | cellstructuremech:contractile_vacuole_lumen | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:contractile_vacuole_lumen | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:contractile_vacuole_lumen | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:contractile_vacuole_lumen | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:contractile_vacuole_lumen | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:contractile_vacuole_lumen | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Taxonomic distribution and model scope

scope: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

RARE is bounded by the note to patchy occurrence across Eukaryota; it is not interpreted as a quantitative prevalence estimate or universality within freshwater protists. Canonical examples establish particular models, not a conserved molecular inventory.

### Maintained input and neighboring boundaries

ownership: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

This maintained YAML owns future scientific corrections. Source-native identities and captured neighbors keep CVC, central vacuole, spongiome, membrane, pore and lumen separate. History entries are provenance, not independent experimental evidence. No maintained input was edited.

### Local lumen identity versus broader ontology parent

identity: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

The local ID preserves the exact SL-defined lumen, with GO:0005775 only as a broader parent and GO:0000331 as the containing organelle. The bounded GO search found no replacement exact identity in returned candidates; no broader GO term is misused as identity.

### Region boundary, graph and absence of fixed constituents

representation: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

The lumen is an internal region. Its membrane bounds it rather than being a lumen constituent; both graph edges are supported by SL and GO. Leaving components empty does not claim chemically pure water or an empty cavity. No permanent molecular inventory is demanded by the source-defined region.

### Water accumulation and model measurements

evidence: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

The lumen fills/expands before discharge, consistent with the review abstract and direct Chlamydomonas volume/cycle measurements. Paramecium microelectrodes support the lumen-side note. Komsic models osmotic gradients rather than directly measuring Chlamydomonas lumen osmolarity; the record does not assert that stronger measurement.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/contractile_vacuole_lumen.yaml; Entire YAML, every current field including all evidence, discussions and history | context_only | Full maintained target read. No source/generated row replaces this YAML as owner. Other three assigned targets and pore neighbor read fully; spongiome identity, hierarchy, components and discussion fields read for boundary context, not audited as a seventh target. |
| neighbors | data/structures/membrane_organelle; The six native-captured contractile-vacuole/spongiome records | context_only | Ignored-inclusive rg -l --no-ignore --hidden search under data/structures for GO:0000331, GO:0031164, GO:0062159, GO:0062160 and the local contractile-vacuole-lumen ID found these six distinct paths. Exact target and all five neighbors are captured by native inspect. No whole-corpus uniqueness beyond this identity neighborhood is claimed. |
| contractile-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031164,GO:0005774,GO:0000331,GO:0062159,GO:0062160,GO:0043232,GO:0005775,GO:0031913,GO:0098797,GO:0005856; Exact ten-term response: names, definitions, synonyms and relevant children/relation edges | supports | Current nonobsolete GO identities distinguish the vacuole, its lipid bilayer, the CVC and spongiome, and the broader vacuolar lumen. GO explicitly gives CVC the intracellular membraneless-organelle parent and lists vacuole and spongiome as parts; membrane components remain lipid-bounded despite this assembly-level ontology classification. |
| contractile-agent-more2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016%2Fj.ejop.2024.126078; PMID38688044; exact DOI/title and full abstract only | supports | More et al.2024 metadata and complete abstract describe CVs as common osmoregulatory devices of freshwater/soil protists with variable architecture and machinery, and discuss presence and absence across eukaryotes. This supports patchy distribution, not a measured fraction of all Eukaryota. |
| contractile-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; taxId, scientificName, rank | supports | NCBI-derived ENA taxonomy confirms2759 Eukaryota, current rank domain. It verifies identity, not CV prevalence. |
| access-more2024-publisher | https://doi.org/10.1016/j.ejop.2024.126078; Original HTTP response; final URL https://linkinghub.elsevier.com/retrieve/pii/S0932473924000282 | context_only | HTTP 200. The DOI route returned a LinkingHub HTML redirect/locator, not review body text. The complete abstract above, not this response, supplies the assessed content. |
| native-verify | /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml --verify; Actual command output for this exact target | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml --causal-graphs; Actual command output for this exact target | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| contractile-agent-SL-0320 | https://rest.uniprot.org/locations/SL-0320.json; Complete location entry: definition, synonyms, isA, partOf and mapping fields | supports | SL-0320 defines the CV compartment bounded by its membrane, lists the vacuolar-lumen synonym, places it under generic vacuole lumen and part_of the CV. It has no GO mapping of its own in the response. |
| contractile-agent-go-lumen-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=contractile%20vacuole%20lumen&amp;limit=100; Exact query, numberOfHits and returned first100 names/IDs | context_only | Bounded QuickGO text search for contractile vacuole lumen returned398 ranked hits; the first100 were inspected and include generic vacuolar lumen plus CV/membrane/CVC, but no exact named CV-lumen identity. This is not an exhaustive ontology-absence proof; the exact SL entry and explicit broader GO parent justify retaining the local ID. |
| contractile-agent-gronlien2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1242%2Fjeb.205.20.3261; Exact citation metadata and complete abstract; body unavailable through tested public routes | supports | Gronlien et al.2002 directly describe paired microelectrodes in the contractile vacuole and cytosol of Paramecium multimicronucleatum, including filling-phase potential changes. This supports the lumen-side canonical note, without adding a numerical property. |
| contractile-agent-allen2002-title | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=TITLE%3A%22Osmoregulation%20and%20contractile%20vacuoles%20of%20protozoa%22; PMID11952235 exact citation and full abstract only | supports | Allen and Naitoh2002 exact metadata and complete abstract describe a fluid-segregating apparatus and a reservoir that periodically discharges. This supports filling/discharge phases without defining the lumen as a molecular component. |
| contractile-agent-komsic2014-pmc-numeric | https://pmc.ncbi.nlm.nih.gov/articles/4248701/; Genuine PMC4248701 article HTML via numerical URL; abstract, Introduction, all Materials/Methods, Results and Discussion, Table1 and Fig1–9 captions read; supplementary movies and image pixels not inspected | supports | Komsic-Buchmann et al.2014 study Chlamydomonas CC-3395/UVM4 under altered osmolarity. They measure CV size and contraction intervals, calculate flux/permeability under stated geometric assumptions, localize MIP1 to CV membranes by immunogold and GFP, and discuss water flow into the lumen. MIP1 localization is directly supported; its water-channel activity and GFP construct functionality remain qualified. No overexpression effect establishes essentiality. The Introduction calls Dictyostelium aquaporin localization clear but cites von Bülow2012, whose primary results are less specific. |
| contractile-agent-tax-44030 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44030; Taxon ID, scientificName, rank and lineage | supports | NCBI-derived authority confirms 44030 Paramecium multimicronucleatum and eukaryotic species identity. |
| contractile-agent-tax-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Taxon ID, scientificName, rank and lineage | supports | NCBI-derived authority confirms 3055 Chlamydomonas reinhardtii and eukaryotic species identity. |
| access-gronlien2002-publisher | https://doi.org/10.1242/jeb.205.20.3261; Original HTTP response; final URL https://journals.biologists.com/jeb/article/205/20/3261/9066/Relationship-between-the-membrane-potential-of-the | context_only | HTTP 403. Publisher access-denial HTML, not article body. |
| access-allen2002-publisher | https://doi.org/10.1016/S0074-7696(02)15015-7; Original HTTP response; final URL https://linkinghub.elsevier.com/retrieve/pii/S0074769602150157 | context_only | HTTP 200. LinkingHub HTML locator/redirect, not article body. |
| schema-result | just validate data/structures/membrane_organelle/contractile_vacuole_lumen.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/contractile_vacuole_lumen.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/contractile_vacuole_lumen.yaml --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_lumen-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/contractile_vacuole_lumen.yaml --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_lumen-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch24-20261021-qayobm82/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_lumen-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/contractile_vacuole_lumen.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 11 of12 collected target identifiers returned OK in this fresh base resolver run. Residuals: cellstructuremech:contractile_vacuole_lumen: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- This is full coverage of one maintained record, not a full systematic review of all species or all CV-associated proteins. RARE is qualitative and model examples do not establish all-eukaryote molecular conservation.
- Several cited papers were readable only as complete indexed abstracts through the tested routes. HTTP200 redirects, API metadata stubs and reCAPTCHA pages were not treated as full text. Actual successful primary-body reads are separately located.
- No maintained snippet, image, numerical physical property or trait link is present in these four targets to validate. No new quotation, molecular inventory, scientific status or history event was introduced.
- Focused native checks and exact current-base resolver slices are reported here. Root owns batch-wide final gates and immutable saving; this author does not finalize or publish.
- The bounded GO search inspected100 of398 ranked responses and is not a universal absence claim. Allen2002 and Gronlien2002 were read as complete abstracts; Komsic2014 Methods/Results/Discussion were read as located.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T005253Z-contractile-vacuole-lumen-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Contractile vacuole lumen identity, compartment topology and evidence review
started_at: '2026-10-21T11:11:11Z'
finished_at: '2026-10-22T00:52:53Z'
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
summary: Exact SL-defined lumen identity, broader GO parent, organelle parthood, membrane
  boundary and scoped filling/discharge examples are coherent. No concrete curation
  defect was established.
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
  - path: data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
    sha256: a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole.yaml
    sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole_complex.yaml
    sha256: 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    sha256: 9c85ec352245d16e963b9d86d4d1cf0b41d499b956b0b2d05611dca3a4341622
    role: target
  - path: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    sha256: e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294
    role: context
  - path: data/structures/membrane_organelle/spongiome.yaml
    sha256: 4bdc11a86d247b6a45549a41c9aac3b25946b046f3b54d269fab634ca9d44019
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
- target_id: cellstructuremech:contractile_vacuole_lumen
  path: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
  label: contractile vacuole lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    role: maintained scientific record
scope:
  description: 'Entire target reviewed: local identity, ontology/SL relations, distribution,
    canonical examples, water-accumulation function, both topology edges, evidence,
    discussion and history.'
  selection: User-authorized all-record pass; batch24 indices1–4 are four distinct
    maintained contractile-vacuole records, each reviewed in full.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:contractile_vacuole_lumen
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  command: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    --verify
  exit_code: 0
  summary: Native command returned zero. Coverage warnings are interpreted separately
    from accession verification.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  command: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Native command returned zero. Coverage warnings are interpreted separately
    from accession verification.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  command: just validate data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  command: just validate-strict data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_lumen-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  summary: 11 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - record
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - neighbors
  - contractile-agent-go
  - contractile-agent-more2024-meta
  - contractile-agent-tax-2759
  - access-more2024-publisher
  - contractile-agent-SL-0320
  - contractile-agent-go-lumen-search
  - contractile-agent-gronlien2002-meta
  - contractile-agent-allen2002-title
  - contractile-agent-komsic2014-pmc-numeric
  - contractile-agent-tax-44030
  - contractile-agent-tax-3055
  - access-gronlien2002-publisher
  - access-allen2002-publisher
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
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
  - cellstructuremech:contractile_vacuole_lumen
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
  - cellstructuremech:contractile_vacuole_lumen
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
  - cellstructuremech:contractile_vacuole_lumen
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
  - cellstructuremech:contractile_vacuole_lumen
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
  reference: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
  locator: Entire YAML, every current field including all evidence, discussions and
    history
  accessed_at: '2026-10-21T11:23:07Z'
  support: context_only
  summary: Full maintained target read. No source/generated row replaces this YAML
    as owner. Other three assigned targets and pore neighbor read fully; spongiome
    identity, hierarchy, components and discussion fields read for boundary context,
    not audited as a seventh target.
- evidence_id: neighbors
  kind: record_content
  reference: data/structures/membrane_organelle
  locator: The six native-captured contractile-vacuole/spongiome records
  accessed_at: '2026-10-21T11:23:07Z'
  support: context_only
  summary: Ignored-inclusive rg -l --no-ignore --hidden search under data/structures
    for GO:0000331, GO:0031164, GO:0062159, GO:0062160 and the local contractile-vacuole-lumen
    ID found these six distinct paths. Exact target and all five neighbors are captured
    by native inspect. No whole-corpus uniqueness beyond this identity neighborhood
    is claimed.
- evidence_id: contractile-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031164,GO:0005774,GO:0000331,GO:0062159,GO:0062160,GO:0043232,GO:0005775,GO:0031913,GO:0098797,GO:0005856
  locator: 'Exact ten-term response: names, definitions, synonyms and relevant children/relation
    edges'
  accessed_at: '2026-10-21T11:12:36.483337Z'
  support: supports
  summary: Current nonobsolete GO identities distinguish the vacuole, its lipid bilayer,
    the CVC and spongiome, and the broader vacuolar lumen. GO explicitly gives CVC
    the intracellular membraneless-organelle parent and lists vacuole and spongiome
    as parts; membrane components remain lipid-bounded despite this assembly-level
    ontology classification.
  snapshot_sha256: 3001e9aa0de9d2828e1a1a727af2c84d192398885fe3080a1f75b13f34bad99a
- evidence_id: contractile-agent-more2024-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016%2Fj.ejop.2024.126078
  locator: PMID38688044; exact DOI/title and full abstract only
  accessed_at: '2026-10-21T11:12:38.019911Z'
  support: supports
  summary: More et al.2024 metadata and complete abstract describe CVs as common osmoregulatory
    devices of freshwater/soil protists with variable architecture and machinery,
    and discuss presence and absence across eukaryotes. This supports patchy distribution,
    not a measured fraction of all Eukaryota.
  snapshot_sha256: b6c0fbe9809f35dec2f0151eb3a8e6e212d4ce1fb60f1cd001785fdff3bf3e0b
- evidence_id: contractile-agent-tax-2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: taxId, scientificName, rank
  accessed_at: '2026-10-21T11:12:36.484828Z'
  support: supports
  summary: NCBI-derived ENA taxonomy confirms2759 Eukaryota, current rank domain.
    It verifies identity, not CV prevalence.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: access-more2024-publisher
  kind: search
  reference: https://doi.org/10.1016/j.ejop.2024.126078
  locator: Original HTTP response; final URL https://linkinghub.elsevier.com/retrieve/pii/S0932473924000282
  accessed_at: '2026-10-21T11:13:13.494252Z'
  support: context_only
  summary: HTTP 200. The DOI route returned a LinkingHub HTML redirect/locator, not
    review body text. The complete abstract above, not this response, supplies the
    assessed content.
  snapshot_sha256: 39c152a279323c8fddcea53c5aed455c7f3a0f3d51945c4e1b1c8f4f76ed25bb
  search_scope: One public source-access request to the exact recorded URL, following
    HTTP redirects; inspect response body for full text rather than infer access from
    HTTP status.
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    --verify
  locator: Actual command output for this exact target
  accessed_at: '2026-10-21T11:13:09.562341Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    --causal-graphs
  locator: Actual command output for this exact target
  accessed_at: '2026-10-21T11:13:10.100905Z'
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
- evidence_id: contractile-agent-SL-0320
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0320.json
  locator: 'Complete location entry: definition, synonyms, isA, partOf and mapping
    fields'
  accessed_at: '2026-10-21T11:12:36.484698Z'
  support: supports
  summary: SL-0320 defines the CV compartment bounded by its membrane, lists the vacuolar-lumen
    synonym, places it under generic vacuole lumen and part_of the CV. It has no GO
    mapping of its own in the response.
  snapshot_sha256: 15bcef9dacd1cd9ae0614f3ab9da225a2e53c0259e083d3535f5b223fd9d9771
- evidence_id: contractile-agent-go-lumen-search
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=contractile%20vacuole%20lumen&limit=100
  locator: Exact query, numberOfHits and returned first100 names/IDs
  accessed_at: '2026-10-21T11:18:13.091398Z'
  support: context_only
  summary: Bounded QuickGO text search for contractile vacuole lumen returned398 ranked
    hits; the first100 were inspected and include generic vacuolar lumen plus CV/membrane/CVC,
    but no exact named CV-lumen identity. This is not an exhaustive ontology-absence
    proof; the exact SL entry and explicit broader GO parent justify retaining the
    local ID.
  snapshot_sha256: 47df92545b845b05013e72ad32873b1d1ef78e80fa1c628d17f48efbebe62ba3
- evidence_id: contractile-agent-gronlien2002-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1242%2Fjeb.205.20.3261
  locator: Exact citation metadata and complete abstract; body unavailable through
    tested public routes
  accessed_at: '2026-10-21T11:12:38.043509Z'
  support: supports
  summary: Gronlien et al.2002 directly describe paired microelectrodes in the contractile
    vacuole and cytosol of Paramecium multimicronucleatum, including filling-phase
    potential changes. This supports the lumen-side canonical note, without adding
    a numerical property.
  snapshot_sha256: ed91c2bbcf0e9848dc377c9dfce281d36a5e7b2a45713b068b748fafcb61638f
- evidence_id: contractile-agent-allen2002-title
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=TITLE%3A%22Osmoregulation%20and%20contractile%20vacuoles%20of%20protozoa%22
  locator: PMID11952235 exact citation and full abstract only
  accessed_at: '2026-10-21T11:13:14.354512Z'
  support: supports
  summary: Allen and Naitoh2002 exact metadata and complete abstract describe a fluid-segregating
    apparatus and a reservoir that periodically discharges. This supports filling/discharge
    phases without defining the lumen as a molecular component.
  snapshot_sha256: 6134ebe0236e6aea28c6e683db8fdb2ae275a717eaaecf476bc3408d11cdd142
- evidence_id: contractile-agent-komsic2014-pmc-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4248701/
  locator: Genuine PMC4248701 article HTML via numerical URL; abstract, Introduction,
    all Materials/Methods, Results and Discussion, Table1 and Fig1–9 captions read;
    supplementary movies and image pixels not inspected
  accessed_at: '2026-10-21T11:16:09.163473Z'
  support: supports
  summary: Komsic-Buchmann et al.2014 study Chlamydomonas CC-3395/UVM4 under altered
    osmolarity. They measure CV size and contraction intervals, calculate flux/permeability
    under stated geometric assumptions, localize MIP1 to CV membranes by immunogold
    and GFP, and discuss water flow into the lumen. MIP1 localization is directly
    supported; its water-channel activity and GFP construct functionality remain qualified.
    No overexpression effect establishes essentiality. The Introduction calls Dictyostelium
    aquaporin localization clear but cites von Bülow2012, whose primary results are
    less specific.
  snapshot_sha256: d804d3e2266b0a877bd9a448e18d257bb6267ed8cd0d0c49075ca5e88397cc4d
- evidence_id: contractile-agent-tax-44030
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44030
  locator: Taxon ID, scientificName, rank and lineage
  accessed_at: '2026-10-21T11:12:37.285255Z'
  support: supports
  summary: NCBI-derived authority confirms 44030 Paramecium multimicronucleatum and
    eukaryotic species identity.
  snapshot_sha256: 4be4e352120325ebd0564f246f7c6af841f2f1a81fbf3b2f6db5c11d7c0393d7
- evidence_id: contractile-agent-tax-3055
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Taxon ID, scientificName, rank and lineage
  accessed_at: '2026-10-21T11:12:37.270798Z'
  support: supports
  summary: NCBI-derived authority confirms 3055 Chlamydomonas reinhardtii and eukaryotic
    species identity.
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: access-gronlien2002-publisher
  kind: search
  reference: https://doi.org/10.1242/jeb.205.20.3261
  locator: Original HTTP response; final URL https://journals.biologists.com/jeb/article/205/20/3261/9066/Relationship-between-the-membrane-potential-of-the
  accessed_at: '2026-10-21T11:13:13.950081Z'
  support: context_only
  summary: HTTP 403. Publisher access-denial HTML, not article body.
  snapshot_sha256: eb623dd977d6f7bc6c78992f85d6d48776068c277460cfd9f8c35b8f47b84c85
  search_scope: One public source-access request to the exact recorded URL, following
    HTTP redirects; inspect response body for full text rather than infer access from
    HTTP status.
- evidence_id: access-allen2002-publisher
  kind: search
  reference: https://doi.org/10.1016/S0074-7696(02)15015-7
  locator: Original HTTP response; final URL https://linkinghub.elsevier.com/retrieve/pii/S0074769602150157
  accessed_at: '2026-10-21T11:13:13.493488Z'
  support: context_only
  summary: HTTP 200. LinkingHub HTML locator/redirect, not article body.
  snapshot_sha256: ecc1d4f218b8c031ef1815831f798766028a220881b3654576ab30109c15bfbc
  search_scope: One public source-access request to the exact recorded URL, following
    HTTP redirects; inspect response body for full text rather than infer access from
    HTTP status.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:11:12Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/contractile_vacuole_lumen.yaml'
  snapshot_sha256: 2fb023c497d64455458d19d3990fb2754fade030f361609b33d381070379b58e
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_lumen-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:11:13Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/contractile_vacuole_lumen.yaml\
    \ --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_lumen-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch24-20261021-qayobm82/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole_lumen-strict.tsv"
  snapshot_sha256: 0f7bdffafe4fc497c038f68ff1d3592cb9b54b2173df84910f2f84777f0b7480
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T11:23:07Z'
  support: supports
  summary: '11 of12 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: cellstructuremech:contractile_vacuole_lumen: SKIPPED; resolved
    by evidence record. Source-native identity checked separately.'
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
- assessment_id: scope
  area: scope
  topic: Taxonomic distribution and model scope
  outcome: supported
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  summary: RARE is bounded by the note to patchy occurrence across Eukaryota; it is
    not interpreted as a quantitative prevalence estimate or universality within freshwater
    protists. Canonical examples establish particular models, not a conserved molecular
    inventory.
  evidence_ids:
  - contractile-agent-tax-2759
  - contractile-agent-more2024-meta
- assessment_id: ownership
  area: ownership
  topic: Maintained input and neighboring boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  summary: This maintained YAML owns future scientific corrections. Source-native
    identities and captured neighbors keep CVC, central vacuole, spongiome, membrane,
    pore and lumen separate. History entries are provenance, not independent experimental
    evidence. No maintained input was edited.
  evidence_ids:
  - record
  - neighbors
  - contractile-agent-go
- assessment_id: identity
  area: identity
  topic: Local lumen identity versus broader ontology parent
  outcome: supported
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  summary: The local ID preserves the exact SL-defined lumen, with GO:0005775 only
    as a broader parent and GO:0000331 as the containing organelle. The bounded GO
    search found no replacement exact identity in returned candidates; no broader
    GO term is misused as identity.
  evidence_ids:
  - contractile-agent-SL-0320
  - contractile-agent-go
  - contractile-agent-go-lumen-search
  - record
- assessment_id: topology
  area: representation
  topic: Region boundary, graph and absence of fixed constituents
  outcome: supported
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  summary: The lumen is an internal region. Its membrane bounds it rather than being
    a lumen constituent; both graph edges are supported by SL and GO. Leaving components
    empty does not claim chemically pure water or an empty cavity. No permanent molecular
    inventory is demanded by the source-defined region.
  evidence_ids:
  - contractile-agent-SL-0320
  - contractile-agent-go
  - record
- assessment_id: function-examples
  area: evidence
  topic: Water accumulation and model measurements
  outcome: supported
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  summary: The lumen fills/expands before discharge, consistent with the review abstract
    and direct Chlamydomonas volume/cycle measurements. Paramecium microelectrodes
    support the lumen-side note. Komsic models osmotic gradients rather than directly
    measuring Chlamydomonas lumen osmolarity; the record does not assert that stronger
    measurement.
  evidence_ids:
  - contractile-agent-allen2002-title
  - contractile-agent-komsic2014-pmc-numeric
  - contractile-agent-gronlien2002-meta
  - contractile-agent-tax-44030
  - contractile-agent-tax-3055
findings: []
actions: []
limitations:
- This is full coverage of one maintained record, not a full systematic review of
  all species or all CV-associated proteins. RARE is qualitative and model examples
  do not establish all-eukaryote molecular conservation.
- Several cited papers were readable only as complete indexed abstracts through the
  tested routes. HTTP200 redirects, API metadata stubs and reCAPTCHA pages were not
  treated as full text. Actual successful primary-body reads are separately located.
- No maintained snippet, image, numerical physical property or trait link is present
  in these four targets to validate. No new quotation, molecular inventory, scientific
  status or history event was introduced.
- Focused native checks and exact current-base resolver slices are reported here.
  Root owns batch-wide final gates and immutable saving; this author does not finalize
  or publish.
- The bounded GO search inspected100 of398 ranked responses and is not a universal
  absence claim. Allen2002 and Gronlien2002 were read as complete abstracts; Komsic2014
  Methods/Results/Discussion were read as located.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
