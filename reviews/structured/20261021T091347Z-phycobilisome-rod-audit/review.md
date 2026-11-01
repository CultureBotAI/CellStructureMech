# Phycobilisome rod source audit

- Review: 20261021T091347Z-phycobilisome-rod-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:50:14Z
- Finished UTC: 2026-10-21T09:13:47Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Rod architecture, scope and broad light-harvesting function are supported; one minor exact-gene provenance gap affects the cpcC representative example.

## Scope And Provenance

Entire rod record and exact local core boundary reviewed against primary Kawakami2022, native GO/taxa/InterPro/UniProt and source GenPept.

Selection: Batch14 strict path-order target3; one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:phycobilisome_rod | data/structures/energy_complex/phycobilisome_rod.yaml | maintained | phycobilisome rod |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native read-only protein verify | passed | True | cellstructuremech:phycobilisome_rod | Native command passed; role-level biological interpretation was checked separately. |
| Native read-only protein causal-graphs | passed | True | cellstructuremech:phycobilisome_rod | Native command passed; role-level biological interpretation was checked separately. |
| Focused native schema | passed | True | cellstructuremech:phycobilisome_rod | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:phycobilisome_rod | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:phycobilisome_rod | 13 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | cellstructuremech:phycobilisome_rod | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:phycobilisome_rod | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:phycobilisome_rod | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:phycobilisome_rod | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:phycobilisome_rod | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:phycobilisome_rod | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Peripheral rod, central core and whole antenna

identity: supported. Targets: cellstructuremech:phycobilisome_rod.

The local rod is a coherent peripheral light-harvesting subassembly, broader-parent and whole-PBS parthood are appropriate, and the graph core CURIE resolves exactly. The canonical example correctly says resolved from a preparation, not an intact atomic PBS reconstruction.

### Mixed constituent classes and source boundaries

grounding: supported. Targets: cellstructuremech:phycobilisome_rod.

Phycobiliproteins, linkers and covalent bilins are supported. Family withholding avoids substituting all phycobiliproteins or a linker domain for the exact mixed rod cohort. CpcG2 assignment in the primary reconstruction is tentative because heterogeneous CpcG rods could not be distinguished.

### Cyanobacteria, red algae and representative strain

scope: supported. Targets: cellstructuremech:phycobilisome_rod.

NIES-2134 PC rod is the direct experiment. Red-algal PE rods are comparative context from the paper, not a new red-algal experiment. Native taxon labels and Rupite examples are distinct and valid; no cross-strain localization or stoichiometry is inferred.

### Exact cpcC mapping is not established

provenance: concern. Targets: cellstructuremech:phycobilisome_rod.

Native validation correctly accepts the exact ORF/token/taxon. However, the role/evidence assert that JX360_02095 is cpcC, which neither its UniProt entry nor source GenPept supplies. The cited structure is from another strain and cannot independently establish that exact locus mapping. This narrow gap does not refute generic linker membership.

### Supported broad light harvesting; proposed detailed mechanism

graph: supported. Targets: cellstructuremech:phycobilisome_rod.

The five edges remain a NONMECHANISTIC structural/function summary: disk assembly, linker organization, bound pigments and inward energy flow. Precise bilin routes/energy-level tuning are interpreted from structure and prior spectroscopy, not a time-resolved transport measurement by this paper.

### Existing classes retained; optional cpcD example not forced

completeness: supported. Targets: cellstructuremech:phycobilisome_rod.

The core rod constituents and structural boundary are represented. The native graph audit reports an optional missing cpcD example, but the declared family-level membership is sourced; this alone is not a finding. The actionable issue is the affirmative unverified cpcC-to-ORF mapping.

## Findings

### F1: The cpcC-to-Rupite-locus mapping lacks exact source support

minor / open / confirmed; issue key: phycobilisome-rod-cpcc-locus-mapping-unverified.

The A0ABT0C7D6 example asserts that cpcC maps to JX360_02095. Its native UniProt and source GenPept instead provide only that ORF and a generic predicted rod-core linker annotation. The cited NIES-2134 structural paper does not map this Rupite locus. Verify exact orthology with an inspectable source, or remove/rephrase the unsupported cpcC identity assertion; retain the verified accession/taxon and distinguish generic linker membership from gene identity. A different Rupite candidate is not established as a replacement.

## Recommended Actions And Acceptance Checks

### A1

In authorized curation, verify the exact cpcC-to-JX360_02095 mapping with an explicit native gene/orthology source or retract that role/evidence mapping. Do not select another accession from length or generic linker annotation alone.

- Inspect exact accession, gene/ORF mapping and strain provenance in the supporting source.
- Keep NIES-2134 experimental evidence separate from Rupite identity-only examples and BP-1 model sequence references.
- Run native protein verify and graph audit in addition to schema/strict/history checks; verify role-level mapping manually.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/phycobilisome_rod.yaml; Entire maintained YAML, including history, nested evidence, all components/examples, graph and discussions | context_only | The entire exact target was read before assessment; source.inputs hashes bind this review. No scientific record edits were made. |
| policy | docs/CURATION.md; Components; evidence and essentiality rules | context_only | Components are taxon-agnostic classes; examples require exact gene and taxon identity. Essentiality concerns assembly, not cell viability or catalytic activity. Optional fields do not automatically require population. |
| protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Rules 2–5; ORF-only identifiers and literature-symbol mapping | context_only | An ORF token is permitted as gene_symbol, but the literature-symbol mapping in role still requires verification. A matching accession and ORF do not by themselves establish exact orthology or membership. |
| protein-verify | /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml --verify; /private/tmp/cellstructure-batch14-20261021-g0felisv/rod-agent/native-verify.log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| protein-causal-graphs | /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml --causal-graphs; /private/tmp/cellstructure-batch14-20261021-g0felisv/rod-agent/native-causal-graphs.log | supports | data/structures/energy_complex/phycobilisome_rod.yaml  (cellstructuremech:phycobilisome_rod)<br>  phycobilisome_rod_light_capture	rod_phycobiliproteins	COVERED	-&gt;rod_phycobiliproteins (UniProtKB:A0ABT0C7V5, UniProtKB:A0ABT0C7V6)<br>  phycobilisome_rod_light_capture	rod_linkers	PARTIAL_EXAMPLES	-&gt;rod_linker_polypeptides (have: UniProtKB:A0ABT0C7V3, UniProtKB:A0ABT0C7D6; missing: cpcD)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| local-core | data/structures/energy_complex/phycobilisome_core.yaml; Entire neighboring record; identifier, definition, part_of and rod/core boundary only | context_only | Exact local core CURIE resolves to the distinct central APC subassembly; its full YAML was read and included in source.inputs. Neighbor claims do not independently substitute for primary evidence. |
| rod-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030076,GO:0030089,GO:0009765; results definitions and GO0030076 children | supports | GO0030076 is the broad light-harvesting-complex class; GO0030089 is the whole phycobilisome, and GO0009765 is the light-harvesting process. These native entries do not assign local rod/core identifiers. |
| rod-agent-tax-1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; scientificName, rank, lineage, otherNames | supports | Native taxon1117 identifies Cyanobacteriota, rank phylum, including cyanobacteria/Cyanophyta synonyms. |
| rod-agent-tax-2763 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2763; scientificName, rank, lineage, otherNames | supports | Native taxon2763 identifies Rhodophyta, rank phylum, with red algae as common name. |
| rod-agent-tax-32053 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053; scientificName, rank, lineage, otherNames | supports | Native species32053 identifies Thermostichus vulcanus and accepts Thermosynechococcus vulcanus as a synonym. |
| rod-agent-tax-2813851 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2813851; scientificName, rank, lineage, otherNames | supports | Native taxon2813851 is Thermostichus vulcanus str. 'Rupite', rank strain; the source identifies that specific representative strain. |
| rod-agent-kawakami2022-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9205905/fullTextXML; Introduction; Subunit composition; Purification/overall structure; Structure of PC rod and arrangement of chromophores; Possible energy-transfer pathway; Methods preparation/model building/MS; Figs1,6–8 captions | supports | Primary study resolves NIES-2134 dissociated PC rods at4.2Å with CpcA/B, CpcC, CpcD and a tentatively assigned CpcG model. Rod/core separation and linker-associated packing are direct structural results; fine energy-transfer routes are proposed from structure and prior spectroscopy. |
| rod-agent-IPR012128 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012128/; metadata accession/name/type/description/hierarchy | supports | Native IPR012128 is the phycobilisome alpha/beta-subunit family, covering allophycocyanin core proteins as well as rod phycocyanins and phycoerythrins; it is broader than the rod-only cohort. |
| rod-agent-IPR001297 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001297/; metadata accession/name/type/description/hierarchy | supports | Native IPR001297 is a phycobilisome linker domain, not a protein family. Its description covers conserved domains occurring in core or rod linker polypeptides. |
| rod-agent-IPR038255 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038255/; metadata accession/name/type/description/hierarchy | supports | Native IPR038255 is the phycobilisome linker domain homologous superfamily, not an exact protein-family definition for a mixed rod/cap/rod-core cohort. |
| rod-agent-IPR016470 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016470/; metadata accession/name/type/description/hierarchy | supports | Native IPR016470 is a phycobilisome linker protein family described as a phycocyanin-associated rod linker. This entry alone does not establish coverage of the entire mixed linker cohort. |
| rod-agent-A0ABT0C7V5 | https://rest.uniprot.org/uniprotkb/A0ABT0C7V5.json; primaryAccession, entryType, genes.orfNames, organism, proteinDescription, sequence.length, InterPro/EMBL cross-references | supports | Native unreviewed Rupite entry verifies accession, protein label, ORF and taxon. Genes contain ORF names, with no curated cpc symbol; automatic location annotation is not experimental rod membership. |
| rod-agent-A0ABT0C7V6 | https://rest.uniprot.org/uniprotkb/A0ABT0C7V6.json; primaryAccession, entryType, genes.orfNames, organism, proteinDescription, sequence.length, InterPro/EMBL cross-references | supports | Native unreviewed Rupite entry verifies accession, protein label, ORF and taxon. Genes contain ORF names, with no curated cpc symbol; automatic location annotation is not experimental rod membership. |
| rod-agent-A0ABT0C7V3 | https://rest.uniprot.org/uniprotkb/A0ABT0C7V3.json; primaryAccession, entryType, genes.orfNames, organism, proteinDescription, sequence.length, InterPro/EMBL cross-references | supports | Native unreviewed Rupite entry verifies accession, protein label, ORF and taxon. Genes contain ORF names, with no curated cpc symbol; automatic location annotation is not experimental rod membership. |
| rod-agent-A0ABT0C7D6 | https://rest.uniprot.org/uniprotkb/A0ABT0C7D6.json; primaryAccession, entryType, genes.orfNames, organism, proteinDescription, sequence.length, InterPro/EMBL cross-references | supports | Native unreviewed Rupite entry verifies accession, protein label, ORF and taxon. Genes contain ORF names, with no curated cpc symbol; automatic location annotation is not experimental rod membership. |
| rod-agent-MCJ2541704.1-genpept | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=MCJ2541704.1&amp;db=protein&amp;report=genpept&amp;retmode=text; LOCUS, DEFINITION, COMMENT PGAP, FEATURES Protein/CDS locus_tag/inference and ORIGIN | supports | Source sequence record confirms JX360_02095 as a172-aa computationally predicted phycobilisome rod-core linker, with no cpcC gene assignment. It is a direct submission/PGAP annotation, not an experimental CpcC study. |
| rod-agent-P50034 | https://rest.uniprot.org/uniprotkb/P50034.json; genes cpcC/tlr1959, organism, sequence, InterPro cross-references | supports | Reviewed reference CpcC is287aa, carries linker and CpcD-like domains, and belongs to BP-1 taxon197221; it is a comparison reference, not a proven replacement for the Rupite example. |
| rod-agent-pdb-7veb-entity4 | https://data.rcsb.org/rest/v1/core/polymer_entity/7VEB/4; polymer sequence; rcsb_polymer_entity description and UniProt reference; entity_src_nat | supports | PDB7VEB entity4 is a287-aa rod-linker model linked to P50034 with BP-1 reference/source annotation. This database model annotation alone does not establish the experimental preparation strain. |
| rod-agent-A0ABT0C9G9 | https://rest.uniprot.org/uniprotkb/A0ABT0C9G9.json; genes.orfNames JX360_05505; sequence; InterPro IPR008213/IPR001297/IPR016470 | supports | Another Rupite linker has285aa and a CpcD-like domain, illustrating that generic linker annotation is insufficient to select the asserted cpcC locus. No replacement orthology is established here. |
| rod-agent-rupite-linkers | https://rest.uniprot.org/uniprotkb/search?query=taxonomy_id%3A2813851%20AND%20%28protein_name%3Alinker%20OR%20gene_exact%3AcpcC%20OR%20gene_exact%3AcpcG%20OR%20gene_exact%3AcpcD%29&amp;format=json&amp;size=500; Complete bounded query response; inspect metadata total-results and pagination | supports | Bounded native search returns seven Rupite linker entries; generic linker labels do not uniquely establish cpcC. |
| schema-result | just validate data/structures/energy_complex/phycobilisome_rod.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/phycobilisome_rod.yaml |
| strict-result | just validate-strict data/structures/energy_complex/phycobilisome_rod.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/phycobilisome_rod-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/phycobilisome_rod.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/phycobilisome_rod-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/phycobilisome_rod-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/phycobilisome_rod.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 13 of15 collected target identifiers returned OK at the unchanged base. Residuals: cellstructuremech:phycobilisome_core: SKIPPED; resolved by evidence local-core; cellstructuremech:phycobilisome_rod: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The primary cryo-EM rod is dissociated from NIES-2134 PBS; CpcG identity and precise energy-transfer paths remain tentative. Red-algal architecture is comparative literature context.
- No experimental Rupite rod localization is asserted. Exact cpcC orthology remains unresolved; neither length/domain comparison nor generic linker names establishes a replacement.
- Native verify passes exact accession/ORF/status/taxon but does not prove the role-level literature-symbol mapping. The optional missing cpcD example is not itself a finding.
- The review reads claim-bearing primary text and captions, not raw cryo-EM particles or every supplementary numerical table. No new exhaustive family/ontology absence claim is made.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091347Z-phycobilisome-rod-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Phycobilisome rod source audit
started_at: '2026-10-21T08:50:14Z'
finished_at: '2026-10-21T09:13:47Z'
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
summary: Rod architecture, scope and broad light-harvesting function are supported;
  one minor exact-gene provenance gap affects the cpcC representative example.
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
  - path: data/structures/energy_complex/phycobilisome_core.yaml
    sha256: 34cca2a846f5b2b84b95c6c2db929370814b4e2898eee052f3e2cbfecafde554
    role: context
  - path: data/structures/energy_complex/phycobilisome_rod.yaml
    sha256: 612013ed996da72581fa218e57c90acce39e6d069c3bbd2b75958cac0b273616
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
- target_id: cellstructuremech:phycobilisome_rod
  path: data/structures/energy_complex/phycobilisome_rod.yaml
  label: phycobilisome rod
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_rod.yaml
    role: maintained scientific record
scope:
  description: Entire rod record and exact local core boundary reviewed against primary
    Kawakami2022, native GO/taxa/InterPro/UniProt and source GenPept.
  selection: Batch14 strict path-order target3; one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:phycobilisome_rod
checks:
- check_id: protein-verify
  name: Native read-only protein verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phycobilisome_rod
  command: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml
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
  - cellstructuremech:phycobilisome_rod
  command: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml
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
  - cellstructuremech:phycobilisome_rod
  command: just validate data/structures/energy_complex/phycobilisome_rod.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phycobilisome_rod
  command: just validate-strict data/structures/energy_complex/phycobilisome_rod.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/phycobilisome_rod-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: 13 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - record
  - local-core
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - protein-policy
  - local-core
  - rod-agent-go
  - rod-agent-tax-1117
  - rod-agent-tax-2763
  - rod-agent-tax-32053
  - rod-agent-tax-2813851
  - rod-agent-kawakami2022-jats
  - rod-agent-IPR012128
  - rod-agent-IPR001297
  - rod-agent-IPR038255
  - rod-agent-IPR016470
  - rod-agent-A0ABT0C7V5
  - rod-agent-A0ABT0C7V6
  - rod-agent-A0ABT0C7V3
  - rod-agent-A0ABT0C7D6
  - rod-agent-MCJ2541704.1-genpept
  - rod-agent-P50034
  - rod-agent-pdb-7veb-entity4
  - rod-agent-A0ABT0C9G9
  - rod-agent-rupite-linkers
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phycobilisome_rod
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
  - cellstructuremech:phycobilisome_rod
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
  - cellstructuremech:phycobilisome_rod
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
  - cellstructuremech:phycobilisome_rod
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
  - cellstructuremech:phycobilisome_rod
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
  reference: data/structures/energy_complex/phycobilisome_rod.yaml
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
    scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml
    --verify
  locator: /private/tmp/cellstructure-batch14-20261021-g0felisv/rod-agent/native-verify.log
  accessed_at: '2026-10-21T08:57:08.471064Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: protein-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batch14-20261021-g0felisv/rod-agent/native-causal-graphs.log
  accessed_at: '2026-10-21T08:57:09.673134Z'
  support: supports
  summary: "data/structures/energy_complex/phycobilisome_rod.yaml  (cellstructuremech:phycobilisome_rod)\n\
    \  phycobilisome_rod_light_capture\trod_phycobiliproteins\tCOVERED\t->rod_phycobiliproteins\
    \ (UniProtKB:A0ABT0C7V5, UniProtKB:A0ABT0C7V6)\n  phycobilisome_rod_light_capture\t\
    rod_linkers\tPARTIAL_EXAMPLES\t->rod_linker_polypeptides (have: UniProtKB:A0ABT0C7V3,\
    \ UniProtKB:A0ABT0C7D6; missing: cpcD)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n\
    \     1  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     1  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref\
    \ on the node\n     2  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 3a7aa401f0c2849f53d4438e8b7071b5c0788c63c874833e01cade3bdccb0566
- evidence_id: local-core
  kind: record_content
  reference: data/structures/energy_complex/phycobilisome_core.yaml
  locator: Entire neighboring record; identifier, definition, part_of and rod/core
    boundary only
  accessed_at: '2026-10-21T09:02:01Z'
  support: context_only
  summary: Exact local core CURIE resolves to the distinct central APC subassembly;
    its full YAML was read and included in source.inputs. Neighbor claims do not independently
    substitute for primary evidence.
- evidence_id: rod-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030076,GO:0030089,GO:0009765
  locator: results definitions and GO0030076 children
  accessed_at: '2026-10-21T08:51:22.923480Z'
  support: supports
  summary: GO0030076 is the broad light-harvesting-complex class; GO0030089 is the
    whole phycobilisome, and GO0009765 is the light-harvesting process. These native
    entries do not assign local rod/core identifiers.
  snapshot_sha256: b4871465e93372dd482ee7d60e01d82de4f68e4c30c501145f24f31a738ea20f
- evidence_id: rod-agent-tax-1117
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: scientificName, rank, lineage, otherNames
  accessed_at: '2026-10-21T08:51:24.325173Z'
  support: supports
  summary: Native taxon1117 identifies Cyanobacteriota, rank phylum, including cyanobacteria/Cyanophyta
    synonyms.
  snapshot_sha256: 0462d61ee879faf0de43deb3472da6e0fe29fdf63cc068591b0ca652eb921c4d
- evidence_id: rod-agent-tax-2763
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2763
  locator: scientificName, rank, lineage, otherNames
  accessed_at: '2026-10-21T08:51:24.342075Z'
  support: supports
  summary: Native taxon2763 identifies Rhodophyta, rank phylum, with red algae as
    common name.
  snapshot_sha256: 73c5fb9f4e663ee9f81162bbef7158f567879f7e39c91ee4823564289385434b
- evidence_id: rod-agent-tax-32053
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053
  locator: scientificName, rank, lineage, otherNames
  accessed_at: '2026-10-21T08:51:23.821004Z'
  support: supports
  summary: Native species32053 identifies Thermostichus vulcanus and accepts Thermosynechococcus
    vulcanus as a synonym.
  snapshot_sha256: fc530968cc8ae8239a8d2d36338d08aa9d41b347fa96df0ad41db960f4a7fbb9
- evidence_id: rod-agent-tax-2813851
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2813851
  locator: scientificName, rank, lineage, otherNames
  accessed_at: '2026-10-21T08:51:24.444097Z'
  support: supports
  summary: Native taxon2813851 is Thermostichus vulcanus str. 'Rupite', rank strain;
    the source identifies that specific representative strain.
  snapshot_sha256: 5dbd710f7409b10ef40f3c02ab8226cf6654f0e74b703ecfb94dbb1abe8613c6
- evidence_id: rod-agent-kawakami2022-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9205905/fullTextXML
  locator: Introduction; Subunit composition; Purification/overall structure; Structure
    of PC rod and arrangement of chromophores; Possible energy-transfer pathway; Methods
    preparation/model building/MS; Figs1,6–8 captions
  accessed_at: '2026-10-21T08:52:48.110400Z'
  support: supports
  summary: Primary study resolves NIES-2134 dissociated PC rods at4.2Å with CpcA/B,
    CpcC, CpcD and a tentatively assigned CpcG model. Rod/core separation and linker-associated
    packing are direct structural results; fine energy-transfer routes are proposed
    from structure and prior spectroscopy.
  snapshot_sha256: d428f0c1cc2ccea5b0e4e343d5841355b892f65e6cb694481ee1ff13c9087713
- evidence_id: rod-agent-IPR012128
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012128/
  locator: metadata accession/name/type/description/hierarchy
  accessed_at: '2026-10-21T08:51:22.924028Z'
  support: supports
  summary: Native IPR012128 is the phycobilisome alpha/beta-subunit family, covering
    allophycocyanin core proteins as well as rod phycocyanins and phycoerythrins;
    it is broader than the rod-only cohort.
  snapshot_sha256: 7de870a6ff5da7e35feb341d61ad7f902c7f7d78fcb8370e124adf8a85728c58
- evidence_id: rod-agent-IPR001297
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001297/
  locator: metadata accession/name/type/description/hierarchy
  accessed_at: '2026-10-21T08:56:47.415494Z'
  support: supports
  summary: Native IPR001297 is a phycobilisome linker domain, not a protein family.
    Its description covers conserved domains occurring in core or rod linker polypeptides.
  snapshot_sha256: 66a740823ed894519ff244d02540651633989c0fa16f581c0625354a9ca2b831
- evidence_id: rod-agent-IPR038255
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038255/
  locator: metadata accession/name/type/description/hierarchy
  accessed_at: '2026-10-21T08:56:47.450376Z'
  support: supports
  summary: Native IPR038255 is the phycobilisome linker domain homologous superfamily,
    not an exact protein-family definition for a mixed rod/cap/rod-core cohort.
  snapshot_sha256: 9cff262c0e9f667225a0e684f2661399b61f81c58368f0aeb49719713665b7ed
- evidence_id: rod-agent-IPR016470
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016470/
  locator: metadata accession/name/type/description/hierarchy
  accessed_at: '2026-10-21T08:56:47.416205Z'
  support: supports
  summary: Native IPR016470 is a phycobilisome linker protein family described as
    a phycocyanin-associated rod linker. This entry alone does not establish coverage
    of the entire mixed linker cohort.
  snapshot_sha256: 4f5ab2b535dee706d9b8d31f7be25fc069adadef5454d3573683e399706202eb
- evidence_id: rod-agent-A0ABT0C7V5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0C7V5.json
  locator: primaryAccession, entryType, genes.orfNames, organism, proteinDescription,
    sequence.length, InterPro/EMBL cross-references
  accessed_at: '2026-10-21T08:51:25.061083Z'
  support: supports
  summary: Native unreviewed Rupite entry verifies accession, protein label, ORF and
    taxon. Genes contain ORF names, with no curated cpc symbol; automatic location
    annotation is not experimental rod membership.
  snapshot_sha256: dda82df881e3ce27aa2794e2deef3984c9b8391a3d07dca2452884523d58a842
- evidence_id: rod-agent-A0ABT0C7V6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0C7V6.json
  locator: primaryAccession, entryType, genes.orfNames, organism, proteinDescription,
    sequence.length, InterPro/EMBL cross-references
  accessed_at: '2026-10-21T08:51:25.254660Z'
  support: supports
  summary: Native unreviewed Rupite entry verifies accession, protein label, ORF and
    taxon. Genes contain ORF names, with no curated cpc symbol; automatic location
    annotation is not experimental rod membership.
  snapshot_sha256: c88aa1be83dba1e643cca17e159edf063a98f91f632213c22ea8652077cf6cad
- evidence_id: rod-agent-A0ABT0C7V3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0C7V3.json
  locator: primaryAccession, entryType, genes.orfNames, organism, proteinDescription,
    sequence.length, InterPro/EMBL cross-references
  accessed_at: '2026-10-21T08:51:25.603088Z'
  support: supports
  summary: Native unreviewed Rupite entry verifies accession, protein label, ORF and
    taxon. Genes contain ORF names, with no curated cpc symbol; automatic location
    annotation is not experimental rod membership.
  snapshot_sha256: 84b7e5f2cd126c4172b653028377112ab3d41557c3ae15968804cdef4e65a818
- evidence_id: rod-agent-A0ABT0C7D6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0C7D6.json
  locator: primaryAccession, entryType, genes.orfNames, organism, proteinDescription,
    sequence.length, InterPro/EMBL cross-references
  accessed_at: '2026-10-21T08:51:25.605744Z'
  support: supports
  summary: Native unreviewed Rupite entry verifies accession, protein label, ORF and
    taxon. Genes contain ORF names, with no curated cpc symbol; automatic location
    annotation is not experimental rod membership.
  snapshot_sha256: c1fcb9b60d36f25177316177ea0239890ec5e6444d9faecd85d959ab80834bab
- evidence_id: rod-agent-MCJ2541704.1-genpept
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=MCJ2541704.1&db=protein&report=genpept&retmode=text
  locator: LOCUS, DEFINITION, COMMENT PGAP, FEATURES Protein/CDS locus_tag/inference
    and ORIGIN
  accessed_at: '2026-10-21T08:57:55.201887Z'
  support: supports
  summary: Source sequence record confirms JX360_02095 as a172-aa computationally
    predicted phycobilisome rod-core linker, with no cpcC gene assignment. It is a
    direct submission/PGAP annotation, not an experimental CpcC study.
  snapshot_sha256: f37c9de8d1f38f25d3caa7b3be35a4d2e4867637bee0c91ddfa87f42709c119b
- evidence_id: rod-agent-P50034
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P50034.json
  locator: genes cpcC/tlr1959, organism, sequence, InterPro cross-references
  accessed_at: '2026-10-21T08:57:54.997804Z'
  support: supports
  summary: Reviewed reference CpcC is287aa, carries linker and CpcD-like domains,
    and belongs to BP-1 taxon197221; it is a comparison reference, not a proven replacement
    for the Rupite example.
  snapshot_sha256: 3a6c5f28ac97d8f12ddbaa40329cecd5095ebdbe2ebeac8d492b430f186ccd98
- evidence_id: rod-agent-pdb-7veb-entity4
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7VEB/4
  locator: polymer sequence; rcsb_polymer_entity description and UniProt reference;
    entity_src_nat
  accessed_at: '2026-10-21T08:56:47.398730Z'
  support: supports
  summary: PDB7VEB entity4 is a287-aa rod-linker model linked to P50034 with BP-1
    reference/source annotation. This database model annotation alone does not establish
    the experimental preparation strain.
  snapshot_sha256: 1b0f728289ab11f2cfb3e885be5a5a8443b3ac3c3b410c9c3c2227bdf65c4d49
- evidence_id: rod-agent-A0ABT0C9G9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0C9G9.json
  locator: genes.orfNames JX360_05505; sequence; InterPro IPR008213/IPR001297/IPR016470
  accessed_at: '2026-10-21T08:57:55.200751Z'
  support: supports
  summary: Another Rupite linker has285aa and a CpcD-like domain, illustrating that
    generic linker annotation is insufficient to select the asserted cpcC locus. No
    replacement orthology is established here.
  snapshot_sha256: 670be0a88c17efd16e0213cbafc3bd67783323a8cf9850f96cde0ba6fef1fc06
- evidence_id: rod-agent-rupite-linkers
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=taxonomy_id%3A2813851%20AND%20%28protein_name%3Alinker%20OR%20gene_exact%3AcpcC%20OR%20gene_exact%3AcpcG%20OR%20gene_exact%3AcpcD%29&format=json&size=500
  locator: Complete bounded query response; inspect metadata total-results and pagination
  accessed_at: '2026-10-21T08:56:48.129013Z'
  support: supports
  summary: Bounded native search returns seven Rupite linker entries; generic linker
    labels do not uniquely establish cpcC.
  snapshot_sha256: 6723bea8cb29ac66c856ddc1458480c1e2d5e0f4db8798c3cf966cdb9eb80068
  search_scope: Remote UniProtKB taxonomy_id:2813851 AND (protein_name:linker OR gene_exact:cpcC
    OR gene_exact:cpcG OR gene_exact:cpcD), size500; all7 results inspected, no pagination.
    Ignored local files are not applicable; not an exhaustive homology search.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/phycobilisome_rod.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:50:17Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/phycobilisome_rod.yaml'
  snapshot_sha256: bd45805e3f6c88de694d46f45b36712256a22337bf8adc412b563deaa2275229
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/phycobilisome_rod.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/phycobilisome_rod-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:50:20Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/phycobilisome_rod.yaml\
    \ --out /private/tmp/cellstructure-batch14-20261021-g0felisv/phycobilisome_rod-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/phycobilisome_rod-strict.tsv"
  snapshot_sha256: 7935acac00a310665e84a67a995cae7d22d7a23faef7cbdf834da2808e434b3c
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/phycobilisome_rod.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T09:02:01Z'
  support: supports
  summary: '13 of15 collected target identifiers returned OK at the unchanged base.
    Residuals: cellstructuremech:phycobilisome_core: SKIPPED; resolved by evidence
    local-core; cellstructuremech:phycobilisome_rod: SKIPPED; resolved by evidence
    record. Source-native identity checked separately.'
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
  topic: Peripheral rod, central core and whole antenna
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: The local rod is a coherent peripheral light-harvesting subassembly, broader-parent
    and whole-PBS parthood are appropriate, and the graph core CURIE resolves exactly.
    The canonical example correctly says resolved from a preparation, not an intact
    atomic PBS reconstruction.
  evidence_ids:
  - rod-agent-go
  - rod-agent-kawakami2022-jats
  - local-core
  - record
- assessment_id: composition
  area: grounding
  topic: Mixed constituent classes and source boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: Phycobiliproteins, linkers and covalent bilins are supported. Family withholding
    avoids substituting all phycobiliproteins or a linker domain for the exact mixed
    rod cohort. CpcG2 assignment in the primary reconstruction is tentative because
    heterogeneous CpcG rods could not be distinguished.
  evidence_ids:
  - rod-agent-kawakami2022-jats
  - rod-agent-IPR012128
  - rod-agent-IPR001297
  - rod-agent-IPR038255
  - rod-agent-IPR016470
- assessment_id: taxa
  area: scope
  topic: Cyanobacteria, red algae and representative strain
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: NIES-2134 PC rod is the direct experiment. Red-algal PE rods are comparative
    context from the paper, not a new red-algal experiment. Native taxon labels and
    Rupite examples are distinct and valid; no cross-strain localization or stoichiometry
    is inferred.
  evidence_ids:
  - rod-agent-kawakami2022-jats
  - rod-agent-tax-1117
  - rod-agent-tax-2763
  - rod-agent-tax-32053
  - rod-agent-tax-2813851
- assessment_id: protein-mapping
  area: provenance
  topic: Exact cpcC mapping is not established
  outcome: concern
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: Native validation correctly accepts the exact ORF/token/taxon. However,
    the role/evidence assert that JX360_02095 is cpcC, which neither its UniProt entry
    nor source GenPept supplies. The cited structure is from another strain and cannot
    independently establish that exact locus mapping. This narrow gap does not refute
    generic linker membership.
  evidence_ids:
  - rod-agent-A0ABT0C7D6
  - rod-agent-MCJ2541704.1-genpept
  - rod-agent-kawakami2022-jats
  - rod-agent-P50034
  - rod-agent-pdb-7veb-entity4
  - rod-agent-A0ABT0C9G9
  - rod-agent-rupite-linkers
  - protein-policy
  - protein-verify
- assessment_id: function
  area: graph
  topic: Supported broad light harvesting; proposed detailed mechanism
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: 'The five edges remain a NONMECHANISTIC structural/function summary: disk
    assembly, linker organization, bound pigments and inward energy flow. Precise
    bilin routes/energy-level tuning are interpreted from structure and prior spectroscopy,
    not a time-resolved transport measurement by this paper.'
  evidence_ids:
  - rod-agent-kawakami2022-jats
  - rod-agent-go
  - record
- assessment_id: completeness
  area: completeness
  topic: Existing classes retained; optional cpcD example not forced
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: The core rod constituents and structural boundary are represented. The
    native graph audit reports an optional missing cpcD example, but the declared
    family-level membership is sourced; this alone is not a finding. The actionable
    issue is the affirmative unverified cpcC-to-ORF mapping.
  evidence_ids:
  - rod-agent-kawakami2022-jats
  - record
  - protein-causal-graphs
  - policy
findings:
- finding_id: F1
  issue_key: phycobilisome-rod-cpcc-locus-mapping-unverified
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The cpcC-to-Rupite-locus mapping lacks exact source support
  description: The A0ABT0C7D6 example asserts that cpcC maps to JX360_02095. Its native
    UniProt and source GenPept instead provide only that ORF and a generic predicted
    rod-core linker annotation. The cited NIES-2134 structural paper does not map
    this Rupite locus. Verify exact orthology with an inspectable source, or remove/rephrase
    the unsupported cpcC identity assertion; retain the verified accession/taxon and
    distinguish generic linker membership from gene identity. A different Rupite candidate
    is not established as a replacement.
  target_ids:
  - cellstructuremech:phycobilisome_rod
  field_paths:
  - components[component_id=rod_linker_polypeptides].protein_examples[uniprot_id=UniProtKB:A0ABT0C7D6].role
  - components[component_id=rod_linker_polypeptides].protein_examples[uniprot_id=UniProtKB:A0ABT0C7D6].evidence
  evidence_ids:
  - rod-agent-A0ABT0C7D6
  - rod-agent-MCJ2541704.1-genpept
  - rod-agent-kawakami2022-jats
  - rod-agent-P50034
  - rod-agent-pdb-7veb-entity4
  - protein-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_rod.yaml
    role: maintained scientific record
  rule_id: .claude/skills/uniprot-protein-examples/SKILL.md:Rules 2–4
  native_severity: minor
  normalization_reason: This is a bounded example-level provenance gap; rod identity,
    constituent classes and source-backed function remain supported. The review does
    not establish a wrong replacement accession.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:phycobilisome_rod
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_rod.yaml
    role: maintained scientific record
  description: In authorized curation, verify the exact cpcC-to-JX360_02095 mapping
    with an explicit native gene/orthology source or retract that role/evidence mapping.
    Do not select another accession from length or generic linker annotation alone.
  acceptance_checks:
  - Inspect exact accession, gene/ORF mapping and strain provenance in the supporting
    source.
  - Keep NIES-2134 experimental evidence separate from Rupite identity-only examples
    and BP-1 model sequence references.
  - Run native protein verify and graph audit in addition to schema/strict/history
    checks; verify role-level mapping manually.
  generator: Maintained structure YAML; derived pages regenerate only after authorized
    curation.
limitations:
- The primary cryo-EM rod is dissociated from NIES-2134 PBS; CpcG identity and precise
  energy-transfer paths remain tentative. Red-algal architecture is comparative literature
  context.
- No experimental Rupite rod localization is asserted. Exact cpcC orthology remains
  unresolved; neither length/domain comparison nor generic linker names establishes
  a replacement.
- Native verify passes exact accession/ORF/status/taxon but does not prove the role-level
  literature-symbol mapping. The optional missing cpcD example is not itself a finding.
- The review reads claim-bearing primary text and captions, not raw cryo-EM particles
  or every supplementary numerical table. No new exhaustive family/ontology absence
  claim is made.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
