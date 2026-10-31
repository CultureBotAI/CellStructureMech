# Photosystem II source audit

- Review: 20261021T091346Z-photosystem-ii-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:50:07Z
- Finished UTC: 2026-10-21T09:13:46Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

PSII identity, core/cofactor classes, canonical example, protein identifiers and net electron-transfer graph are supported; no concrete correction established.

## Scope And Provenance

Entire maintained record reviewed; native GO/taxonomy/UniProt/family scopes and primary Umena PDF inspected.

Selection: Batch14 strict path-order target2; one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009523 | data/structures/energy_complex/photosystem_ii.yaml | maintained | photosystem II |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native read-only protein verify | passed | True | GO:0009523 | Native command passed; role-level biological interpretation was checked separately. |
| Native read-only protein causal-graphs | passed | True | GO:0009523 | Native command passed; role-level biological interpretation was checked separately. |
| Focused native schema | passed | True | GO:0009523 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009523 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0009523 | 7 identifiers OK; 3 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0009523 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0009523 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009523 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009523 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009523 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0009523 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact photosystem boundary

identity: supported. Targets: GO:0009523.

Definition/parent match native GO. The comparison with anoxygenic bacteria is inherited GO wording, not an added cyanobacterial species claim. Umena supplies the oxygenic PSII canonical example.

### Grouped protein core and chemically distinct cofactors

grounding: supported. Targets: GO:0009523.

The three existing component classes distinguish core proteins, Mn4CaO5 and mixed pigments. Exact D1/D2 families cannot replace the entire mixed core, and broad L/M is less exact. This is an existing bounded representation rather than complete deferral of known membership.

### Canonical oxygen-evolving composition versus assembly necessity

scope: unknown. Targets: GO:0009523.

The source directly supports catalytic importance and presence of the metal cluster/pigments in the purified oxygen-evolving complex. It does not test assembly after depletion. ESSENTIAL should not be read as a demonstrated knockout/assembly result or as necessity of every member of each grouped class; this review has not independently established a contradictory assembly experiment.

### Species, genes and cited annotation scope

evidence: supported. Targets: GO:0009523.

Both reviewed examples and their exact experimental citation annotations are valid. Umena primary text directly places the complex in thylakoids; Kamiya/Kawakami citation identity and abstract scope are checked, but their body-level evidence was inaccessible in the attempted routes.

### Water-to-plastoquinone directionality

graph: supported. Targets: GO:0009523.

All five graph edges follow the native GO net photosynthetic function and Umena donor/acceptor context. The graph does not claim individual S-state chemistry, proton pathways, ATP synthesis by PSII or a universal exact subunit count.

### Material core represented; refinement remains bounded

completeness: supported. Targets: GO:0009523.

Known central proteins are represented by a core row with D1/D2 examples, alongside catalytic cluster and pigments. Individual antenna/extrinsic-family decomposition and chemical groundings remain useful refinements; no verified exact family for the full mixed core was found in the explicitly inspected candidates. No exhaustive ontology absence claim or optional-field finding is made.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/photosystem_ii.yaml; Entire maintained YAML, including history, nested evidence, all components/examples, graph and discussions | context_only | The entire exact target was read before assessment; source.inputs hashes bind this review. No scientific record edits were made. |
| policy | docs/CURATION.md; Components; evidence and essentiality rules | context_only | Components are taxon-agnostic classes; examples require exact gene and taxon identity. Essentiality concerns assembly, not cell viability or catalytic activity. Optional fields do not automatically require population. |
| protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Rules 2–5; ORF-only identifiers and literature-symbol mapping | context_only | An ORF token is permitted as gene_symbol, but the literature-symbol mapping in role still requires verification. A matching accession and ORF do not by themselves establish exact orthology or membership. |
| protein-verify | /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml --verify; /private/tmp/cellstructure-batch14-20261021-g0felisv/psii-agent/native-verify.log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| protein-causal-graphs | /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml --causal-graphs; /private/tmp/cellstructure-batch14-20261021-g0felisv/psii-agent/native-causal-graphs.log | supports | data/structures/energy_complex/photosystem_ii.yaml  (GO:0009523)<br>  psii_light_driven_water_oxidation	reaction_center	COVERED	-&gt;pheophytin_quinone_reaction_center_core (UniProtKB:P51765, UniProtKB:D0VWR8)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| psii-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009523,GO:0009521,GO:0009767; results definitions and GO0009521 children | supports | Native GO0009523 definition matches the target and GO0009521 lists it as an is_a child. GO0009767 is the broader electron-transport process. |
| psii-agent-tax-1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; scientificName, rank, lineage, otherNames | supports | Native taxon1117 identifies Cyanobacteriota, rank phylum, with cyanobacteria/Cyanophyta synonyms. |
| psii-agent-tax-32053 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053; scientificName, rank, lineage, otherNames | supports | Native species32053 identifies Thermostichus vulcanus and lists Thermosynechococcus vulcanus and Synechococcus vulcanus as synonyms. |
| psii-agent-umena2011-pdf | https://chemie.uni-muenchen.de/ac/kluefers/homepage/L/bac/oec_2011.pdf; Article pp55–60: Overall structure, Mn4CaO5 cluster, YZ, pigments, plastoquinones; final Methods page Purification/crystallization and structure refinement | supports | The primary1.9Å T.vulcanus structure resolves D1/D2-containing PSII, pigments and Mn4CaO5. Its preparation is an oxygen-evolving purified dimer;19 subunits are modeled because PsbY was not found, while the introductory canonical count is20. |
| psii-agent-P51765 | https://rest.uniprot.org/uniprotkb/P51765.json; primaryAccession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and SUBUNIT comments | supports | Reviewed native D1 accession P51765 has gene psbA (synonym psbA-1), species32053, and cellular-thylakoid-membrane ECO0000269 annotations citing12518057/19433803/21499260. |
| psii-agent-D0VWR8 | https://rest.uniprot.org/uniprotkb/D0VWR8.json; primaryAccession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and SUBUNIT comments | supports | Reviewed native D2 accession D0VWR8 has gene psbD, species32053, and cellular-thylakoid-membrane ECO0000269 annotations citing12518057/19433803/21499260. The entry is a fragment. |
| psii-agent-uniprot-unique | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20taxonomy_id%3A32053%20AND%20%28gene_exact%3ApsbA%20OR%20gene_exact%3ApsbD%29&amp;format=json&amp;size=100; Complete bounded query response; inspect metadata total-results and pagination | supports | The bounded reviewed species query returns exactly P51765 and D0VWR8, two total with no next-page link. |
| psii-agent-IPR005867 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005867/; metadata accession/name/type/description/hierarchy | supports | Native IPR005867 is a family specifically for D1/PsbA, which forms the reaction-center heterodimer with D2. It is one protein family rather than the whole multi-subunit PSII core. |
| psii-agent-IPR005868 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005868/; metadata accession/name/type/description/hierarchy | supports | Native IPR005868 is a family specifically for D2/PsbD, which forms the reaction-center heterodimer with D1. It is one protein family rather than the whole multi-subunit PSII core. |
| psii-agent-IPR000484 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000484/; metadata accession/name/type/description/hierarchy | supports | Native IPR000484 is a family spanning bacterial L/M, PSII D1/D2 and ChlF. Its hierarchy and description make it broader than the represented complete PSII core. |
| psii-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A21499260%20OR%20EXT_ID%3A12518057%20OR%20EXT_ID%3A19433803; resultList.result IDs21499260/12518057/19433803, DOI/title/abstractText | supports | Native bibliographic identities and abstracts checked for Umena2011, Kamiya2003 and Kawakami2009. The latter two abstracts describe crystallographic PSII studies; this metadata is not full-body access. |
| psii-agent-kamiya2003-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140893/fullTextXML; Captured access response only; not article content | context_only | The Europe PMC fullTextXML request returned HTTP500; this response is access evidence only. |
| psii-agent-kawakami2009-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2688974/fullTextXML; Captured access response only; not article content | context_only | The Europe PMC fullTextXML request returned HTTP500; this response is access evidence only. |
| psii-agent-kamiya2003-render | https://europepmc.org/articles/PMC140893?pdf=render; Captured access response only; not article content | context_only | The Europe PMC PDF-render request returned HTTP403; this response is access evidence only. |
| psii-agent-kawakami2009-render | https://europepmc.org/articles/PMC2688974?pdf=render; Captured access response only; not article content | context_only | The Europe PMC PDF-render request returned HTTP403; this response is access evidence only. |
| psii-agent-kamiya2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC140893/; Captured access response only; not article content | context_only | HTTP200 returned a browser-check/challenge page, not the primary article; no full-body support is claimed. |
| psii-agent-kawakami2009-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2688974/; Captured access response only; not article content | context_only | HTTP200 returned a browser-check/challenge page, not the primary article; no full-body support is claimed. |
| schema-result | just validate data/structures/energy_complex/photosystem_ii.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/photosystem_ii.yaml |
| strict-result | just validate-strict data/structures/energy_complex/photosystem_ii.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/photosystem_ii-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/photosystem_ii.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/photosystem_ii-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/photosystem_ii-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/photosystem_ii.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 7 of10 collected target identifiers returned OK at the unchanged base. Residuals: PMID:12518057: UNREACHABLE; resolved by evidence psii-agent-epmc; PMID:19433803: UNREACHABLE; resolved by evidence psii-agent-epmc; PMID:21499260: UNREACHABLE; resolved by evidence psii-agent-epmc. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Kamiya2003 and Kawakami2009 full bodies were not recovered: native JATS500, challenge pages and PDF-render403 are retained. Their abstracts and exact UniProt citation annotations were inspected; these are not promoted to full-body evidence.
- Umena is one purified oxygen-evolving T.vulcanus preparation; absent PsbY and modeled19 versus canonical20 are preparation-specific and not universalized.
- Assembly necessity of the Mn4CaO5/pigment classes was not tested by the cited structural experiment. Essentiality is not equated with catalytic activity or organism viability.
- The review does not exhaust all possible ontology or chemical mappings, reanalyze diffraction data, or assert complete species-specific composition.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091346Z-photosystem-ii-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Photosystem II source audit
started_at: '2026-10-21T08:50:07Z'
finished_at: '2026-10-21T09:13:46Z'
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
summary: PSII identity, core/cofactor classes, canonical example, protein identifiers
  and net electron-transfer graph are supported; no concrete correction established.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/energy_complex/photosystem_ii.yaml
    sha256: fc05496451f76ed16643edb2ca590803fd07569abfe432111e31314375687a16
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
- target_id: GO:0009523
  path: data/structures/energy_complex/photosystem_ii.yaml
  label: photosystem II
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem_ii.yaml
    role: maintained scientific record
scope:
  description: Entire maintained record reviewed; native GO/taxonomy/UniProt/family
    scopes and primary Umena PDF inspected.
  selection: Batch14 strict path-order target2; one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009523
checks:
- check_id: protein-verify
  name: Native read-only protein verify
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml
    --verify
  exit_code: 0
  summary: Native command passed; role-level biological interpretation was checked
    separately.
  evidence_ids:
  - protein-verify
- check_id: protein-causal-graphs
  name: Native read-only protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml
    --causal-graphs
  exit_code: 0
  summary: Native command passed; role-level biological interpretation was checked
    separately.
  evidence_ids:
  - protein-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: just validate data/structures/energy_complex/photosystem_ii.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: just validate-strict data/structures/energy_complex/photosystem_ii.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/photosystem_ii-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0009523
  summary: 7 identifiers OK; 3 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - psii-agent-epmc
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009523
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - protein-policy
  - psii-agent-go
  - psii-agent-tax-1117
  - psii-agent-tax-32053
  - psii-agent-umena2011-pdf
  - psii-agent-P51765
  - psii-agent-D0VWR8
  - psii-agent-uniprot-unique
  - psii-agent-IPR005867
  - psii-agent-IPR005868
  - psii-agent-IPR000484
  - psii-agent-epmc
  - psii-agent-kamiya2003-jats
  - psii-agent-kawakami2009-jats
  - psii-agent-kamiya2003-render
  - psii-agent-kawakami2009-render
  - psii-agent-kamiya2003-pmc
  - psii-agent-kawakami2009-pmc
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/energy_complex/photosystem_ii.yaml
  locator: Entire maintained YAML, including history, nested evidence, all components/examples,
    graph and discussions
  accessed_at: '2026-10-21T09:02:01Z'
  support: context_only
  summary: The entire exact target was read before assessment; source.inputs hashes
    bind this review. No scientific record edits were made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; evidence and essentiality rules
  accessed_at: '2026-10-21T09:02:01Z'
  support: context_only
  summary: Components are taxon-agnostic classes; examples require exact gene and
    taxon identity. Essentiality concerns assembly, not cell viability or catalytic
    activity. Optional fields do not automatically require population.
- evidence_id: protein-policy
  kind: record_content
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Rules 2–5; ORF-only identifiers and literature-symbol mapping
  accessed_at: '2026-10-21T09:02:01Z'
  support: context_only
  summary: An ORF token is permitted as gene_symbol, but the literature-symbol mapping
    in role still requires verification. A matching accession and ORF do not by themselves
    establish exact orthology or membership.
- evidence_id: protein-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml
    --verify
  locator: /private/tmp/cellstructure-batch14-20261021-g0felisv/psii-agent/native-verify.log
  accessed_at: '2026-10-21T08:57:05.147066Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: protein-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batch14-20261021-g0felisv/psii-agent/native-causal-graphs.log
  accessed_at: '2026-10-21T08:57:05.759845Z'
  support: supports
  summary: "data/structures/energy_complex/photosystem_ii.yaml  (GO:0009523)\n  psii_light_driven_water_oxidation\t\
    reaction_center\tCOVERED\t->pheophytin_quinone_reaction_center_core (UniProtKB:P51765,\
    \ UniProtKB:D0VWR8)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     1\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 1b362f8d9f0be4071f98c0d7ecd71d55a3d2e2d32fab049477ca26edf0406830
- evidence_id: psii-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009523,GO:0009521,GO:0009767
  locator: results definitions and GO0009521 children
  accessed_at: '2026-10-21T08:51:22.921144Z'
  support: supports
  summary: Native GO0009523 definition matches the target and GO0009521 lists it as
    an is_a child. GO0009767 is the broader electron-transport process.
  snapshot_sha256: 453e4448a23ef80ffebd9ffa18ff1f8ca95f9e543eebbe6db5262a2c6a7fd288
- evidence_id: psii-agent-tax-1117
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: scientificName, rank, lineage, otherNames
  accessed_at: '2026-10-21T08:51:23.722750Z'
  support: supports
  summary: Native taxon1117 identifies Cyanobacteriota, rank phylum, with cyanobacteria/Cyanophyta
    synonyms.
  snapshot_sha256: 0462d61ee879faf0de43deb3472da6e0fe29fdf63cc068591b0ca652eb921c4d
- evidence_id: psii-agent-tax-32053
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053
  locator: scientificName, rank, lineage, otherNames
  accessed_at: '2026-10-21T08:51:23.686814Z'
  support: supports
  summary: Native species32053 identifies Thermostichus vulcanus and lists Thermosynechococcus
    vulcanus and Synechococcus vulcanus as synonyms.
  snapshot_sha256: fc530968cc8ae8239a8d2d36338d08aa9d41b347fa96df0ad41db960f4a7fbb9
- evidence_id: psii-agent-umena2011-pdf
  kind: primary_source
  reference: https://chemie.uni-muenchen.de/ac/kluefers/homepage/L/bac/oec_2011.pdf
  locator: 'Article pp55–60: Overall structure, Mn4CaO5 cluster, YZ, pigments, plastoquinones;
    final Methods page Purification/crystallization and structure refinement'
  accessed_at: '2026-10-21T08:52:47.347624Z'
  support: supports
  summary: The primary1.9Å T.vulcanus structure resolves D1/D2-containing PSII, pigments
    and Mn4CaO5. Its preparation is an oxygen-evolving purified dimer;19 subunits
    are modeled because PsbY was not found, while the introductory canonical count
    is20.
  snapshot_sha256: 29e5d7be00bc7ccf1acf26fe3276d2176b6fe92fe5736280637602b52623f693
- evidence_id: psii-agent-P51765
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P51765.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and SUBUNIT comments
  accessed_at: '2026-10-21T08:51:24.953174Z'
  support: supports
  summary: Reviewed native D1 accession P51765 has gene psbA (synonym psbA-1), species32053,
    and cellular-thylakoid-membrane ECO0000269 annotations citing12518057/19433803/21499260.
  snapshot_sha256: 04887fcce267947732efc1a8148837c6691f19aedf33874357ac93e63338b2f7
- evidence_id: psii-agent-D0VWR8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/D0VWR8.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and SUBUNIT comments
  accessed_at: '2026-10-21T08:51:24.958291Z'
  support: supports
  summary: Reviewed native D2 accession D0VWR8 has gene psbD, species32053, and cellular-thylakoid-membrane
    ECO0000269 annotations citing12518057/19433803/21499260. The entry is a fragment.
  snapshot_sha256: 3b383aa42a19d3fd926532422025ccb924def2c56cf45f212de3d50786155663
- evidence_id: psii-agent-uniprot-unique
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20taxonomy_id%3A32053%20AND%20%28gene_exact%3ApsbA%20OR%20gene_exact%3ApsbD%29&format=json&size=100
  locator: Complete bounded query response; inspect metadata total-results and pagination
  accessed_at: '2026-10-21T08:52:48.817599Z'
  support: supports
  summary: The bounded reviewed species query returns exactly P51765 and D0VWR8, two
    total with no next-page link.
  snapshot_sha256: e384401ab283e369cbd5420ec28f61a00684b2868f42cb5b9b7a7bffb1dea974
  search_scope: Remote UniProtKB reviewed:true AND taxonomy_id:32053 AND (gene_exact:psbA
    OR gene_exact:psbD), size100; both results inspected. Ignored local files are
    not applicable; no claim about all unreviewed paralogues.
- evidence_id: psii-agent-IPR005867
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005867/
  locator: metadata accession/name/type/description/hierarchy
  accessed_at: '2026-10-21T08:56:47.480878Z'
  support: supports
  summary: Native IPR005867 is a family specifically for D1/PsbA, which forms the
    reaction-center heterodimer with D2. It is one protein family rather than the
    whole multi-subunit PSII core.
  snapshot_sha256: faa113a0f5552d7f408c1f01950cfacd1859166aa8d679c30989cb105f8c1a46
- evidence_id: psii-agent-IPR005868
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005868/
  locator: metadata accession/name/type/description/hierarchy
  accessed_at: '2026-10-21T08:56:47.482887Z'
  support: supports
  summary: Native IPR005868 is a family specifically for D2/PsbD, which forms the
    reaction-center heterodimer with D1. It is one protein family rather than the
    whole multi-subunit PSII core.
  snapshot_sha256: 4f698a778bf556dfaf7c827388d3eade093a92f055c47ef1734aef5e36bdad9a
- evidence_id: psii-agent-IPR000484
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000484/
  locator: metadata accession/name/type/description/hierarchy
  accessed_at: '2026-10-21T08:56:48.044157Z'
  support: supports
  summary: Native IPR000484 is a family spanning bacterial L/M, PSII D1/D2 and ChlF.
    Its hierarchy and description make it broader than the represented complete PSII
    core.
  snapshot_sha256: d8aae07dcf579cb89473e738ece6d8310e55a73c30ac5e8e6ef32a94d2cc9ae5
- evidence_id: psii-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A21499260%20OR%20EXT_ID%3A12518057%20OR%20EXT_ID%3A19433803
  locator: resultList.result IDs21499260/12518057/19433803, DOI/title/abstractText
  accessed_at: '2026-10-21T08:51:22.922445Z'
  support: supports
  summary: Native bibliographic identities and abstracts checked for Umena2011, Kamiya2003
    and Kawakami2009. The latter two abstracts describe crystallographic PSII studies;
    this metadata is not full-body access.
  snapshot_sha256: 3c650dc041318d1e2333535684a4895edf8a6384bf623561788d6c538cfdea61
- evidence_id: psii-agent-kamiya2003-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140893/fullTextXML
  locator: Captured access response only; not article content
  accessed_at: '2026-10-21T08:52:47.348353Z'
  support: context_only
  summary: The Europe PMC fullTextXML request returned HTTP500; this response is access
    evidence only.
  snapshot_sha256: 4ef2bf528c21616cb9489c3e5241fe0116b7d440879d01e60e5ce44f5c4d5527
- evidence_id: psii-agent-kawakami2009-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2688974/fullTextXML
  locator: Captured access response only; not article content
  accessed_at: '2026-10-21T08:52:47.348261Z'
  support: context_only
  summary: The Europe PMC fullTextXML request returned HTTP500; this response is access
    evidence only.
  snapshot_sha256: ec24667680f9cd5fdaad50ad404d43c9d425e04095104accbd1f08f0d014f30b
- evidence_id: psii-agent-kamiya2003-render
  kind: authority
  reference: https://europepmc.org/articles/PMC140893?pdf=render
  locator: Captured access response only; not article content
  accessed_at: '2026-10-21T08:58:56.272155Z'
  support: context_only
  summary: The Europe PMC PDF-render request returned HTTP403; this response is access
    evidence only.
  snapshot_sha256: 2635156a17e9af9120b4786e9eddd8b62e7f4113970eb5fed2604732dc64cdda
- evidence_id: psii-agent-kawakami2009-render
  kind: authority
  reference: https://europepmc.org/articles/PMC2688974?pdf=render
  locator: Captured access response only; not article content
  accessed_at: '2026-10-21T08:58:56.272867Z'
  support: context_only
  summary: The Europe PMC PDF-render request returned HTTP403; this response is access
    evidence only.
  snapshot_sha256: 31537bb1b919487be3ff40b0e44307c10acb3c9f692d54094f4663df9987c3ca
- evidence_id: psii-agent-kamiya2003-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC140893/
  locator: Captured access response only; not article content
  accessed_at: '2026-10-21T08:56:47.112835Z'
  support: context_only
  summary: HTTP200 returned a browser-check/challenge page, not the primary article;
    no full-body support is claimed.
  snapshot_sha256: d3ac823f97e3da92325df67af31414c258c180f4b753e99a8c1799ad890c5e2a
- evidence_id: psii-agent-kawakami2009-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2688974/
  locator: Captured access response only; not article content
  accessed_at: '2026-10-21T08:56:47.113496Z'
  support: context_only
  summary: HTTP200 returned a browser-check/challenge page, not the primary article;
    no full-body support is claimed.
  snapshot_sha256: 0994fb543f66de308a1222915d898ae2098134864c45f4a4dfd62fdaa4f9b97e
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/photosystem_ii.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:50:11Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/photosystem_ii.yaml'
  snapshot_sha256: d9b042a05d55386231cc0c739efc2840d84b7ecaeefe50f8dc4113614bab9a8a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/photosystem_ii.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/photosystem_ii-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:50:14Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/photosystem_ii.yaml\
    \ --out /private/tmp/cellstructure-batch14-20261021-g0felisv/photosystem_ii-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/photosystem_ii-strict.tsv"
  snapshot_sha256: 0fabdfd16127c10348bfb1be64111be8c9c14ca89218fa4b28c4061301b96c2e
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/photosystem_ii.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T09:02:01Z'
  support: supports
  summary: '7 of10 collected target identifiers returned OK at the unchanged base.
    Residuals: PMID:12518057: UNREACHABLE; resolved by evidence psii-agent-epmc; PMID:19433803:
    UNREACHABLE; resolved by evidence psii-agent-epmc; PMID:21499260: UNREACHABLE;
    resolved by evidence psii-agent-epmc. Source-native identity checked separately.'
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
  topic: Exact photosystem boundary
  outcome: supported
  target_ids:
  - GO:0009523
  summary: Definition/parent match native GO. The comparison with anoxygenic bacteria
    is inherited GO wording, not an added cyanobacterial species claim. Umena supplies
    the oxygenic PSII canonical example.
  evidence_ids:
  - psii-agent-go
  - psii-agent-umena2011-pdf
  - psii-agent-tax-1117
  - psii-agent-tax-32053
- assessment_id: composition
  area: grounding
  topic: Grouped protein core and chemically distinct cofactors
  outcome: supported
  target_ids:
  - GO:0009523
  summary: The three existing component classes distinguish core proteins, Mn4CaO5
    and mixed pigments. Exact D1/D2 families cannot replace the entire mixed core,
    and broad L/M is less exact. This is an existing bounded representation rather
    than complete deferral of known membership.
  evidence_ids:
  - psii-agent-umena2011-pdf
  - record
  - policy
  - psii-agent-IPR005867
  - psii-agent-IPR005868
  - psii-agent-IPR000484
- assessment_id: essentiality
  area: scope
  topic: Canonical oxygen-evolving composition versus assembly necessity
  outcome: unknown
  target_ids:
  - GO:0009523
  summary: The source directly supports catalytic importance and presence of the metal
    cluster/pigments in the purified oxygen-evolving complex. It does not test assembly
    after depletion. ESSENTIAL should not be read as a demonstrated knockout/assembly
    result or as necessity of every member of each grouped class; this review has
    not independently established a contradictory assembly experiment.
  evidence_ids:
  - psii-agent-umena2011-pdf
  - policy
- assessment_id: proteins
  area: evidence
  topic: Species, genes and cited annotation scope
  outcome: supported
  target_ids:
  - GO:0009523
  summary: Both reviewed examples and their exact experimental citation annotations
    are valid. Umena primary text directly places the complex in thylakoids; Kamiya/Kawakami
    citation identity and abstract scope are checked, but their body-level evidence
    was inaccessible in the attempted routes.
  evidence_ids:
  - psii-agent-P51765
  - psii-agent-D0VWR8
  - psii-agent-uniprot-unique
  - psii-agent-epmc
  - psii-agent-umena2011-pdf
  - protein-verify
- assessment_id: function
  area: graph
  topic: Water-to-plastoquinone directionality
  outcome: supported
  target_ids:
  - GO:0009523
  summary: All five graph edges follow the native GO net photosynthetic function and
    Umena donor/acceptor context. The graph does not claim individual S-state chemistry,
    proton pathways, ATP synthesis by PSII or a universal exact subunit count.
  evidence_ids:
  - psii-agent-go
  - psii-agent-umena2011-pdf
- assessment_id: completeness
  area: completeness
  topic: Material core represented; refinement remains bounded
  outcome: supported
  target_ids:
  - GO:0009523
  summary: Known central proteins are represented by a core row with D1/D2 examples,
    alongside catalytic cluster and pigments. Individual antenna/extrinsic-family
    decomposition and chemical groundings remain useful refinements; no verified exact
    family for the full mixed core was found in the explicitly inspected candidates.
    No exhaustive ontology absence claim or optional-field finding is made.
  evidence_ids:
  - psii-agent-umena2011-pdf
  - record
  - policy
  - psii-agent-IPR005867
  - psii-agent-IPR005868
  - psii-agent-IPR000484
findings: []
actions: []
limitations:
- 'Kamiya2003 and Kawakami2009 full bodies were not recovered: native JATS500, challenge
  pages and PDF-render403 are retained. Their abstracts and exact UniProt citation
  annotations were inspected; these are not promoted to full-body evidence.'
- Umena is one purified oxygen-evolving T.vulcanus preparation; absent PsbY and modeled19
  versus canonical20 are preparation-specific and not universalized.
- Assembly necessity of the Mn4CaO5/pigment classes was not tested by the cited structural
  experiment. Essentiality is not equated with catalytic activity or organism viability.
- The review does not exhaust all possible ontology or chemical mappings, reanalyze
  diffraction data, or assert complete species-specific composition.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
