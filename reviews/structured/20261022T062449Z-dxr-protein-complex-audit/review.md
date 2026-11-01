# Source-grounded review of Dxr protein complex

- Review: 20261022T062449Z-dxr-protein-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:03:29Z
- Finished UTC: 2026-10-22T06:24:49Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: exact Dxr identity/family, reviewed dxr/ispC example, E. coli substrate/NADPH homodimer and coarse functional graph are supported. Primary-body, coordinate and assembly-necessity limits remain explicit.

## Scope And Provenance

Exactly one complete maintained target; native-source fields and primary reading scopes are declared in evidence. Scientific inputs remain unchanged.

Selection: One complete record in strict-path batch 53 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990065 | data/structures/other/dxr_protein_complex.yaml | maintained | Dxr protein complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990065 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990065 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:1990065 | Focused check passed; source claims assessed separately. |
| Native focused verify | passed | True | GO:1990065 | Focused check passed; source claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:1990065 | No expression-module or transcriptomic claim requires this resource. |
| Claim-level scientific review | passed | True | GO:1990065 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990065 | 8 of 10 collected target identifiers returned OK. PDB:1Q0Q: SKIPPED; Exact RCSB entry identifier, structure title and primary citation DOI/PMID independently read. Deposition-specific composition, ligands and structural interpretation retain the separately reviewed evidence scopes; the paper title does not substitute for entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:15567415: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990065 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990065 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990065 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990065 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990065 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Dxr homodimer as a protein complex

identity: supported. Targets: GO:1990065.

Exact GO identity, synonym and protein-complex parent are supported. The record describes a homomeric assembly rather than confusing a single protein family with an assembly; two-copy stoichiometry is explicitly scoped to E. coli PDB1Q0Q.

### Exact family, reference accession and two protein chains

grounding: supported. Targets: GO:1990065.

IPR003821 is the exact full-protein class and P45568 is the reviewed K12 dxr/ispC example. Native polymer and biological-assembly data corroborate the stated homodimer and scoped SUBUNIT_COUNT. Ligand entities are distinct from protein constituents.

### Substrate complex and NADPH chemistry

evidence: supported. Targets: GO:1990065.

PDB1Q0Q contains DXP and NADPH. The paper abstract distinguishes the 1.9 A substrate complex from the 2.2 A inhibitor complex and cautions about a second substrate diastereomer. Forward DXP-to-MEP reduction consumes NADPH; the formal GO reaction may be written in reverse. Generic NADP-dependent wording in the inherited definition is clarified by the record’s explicit NADPH functional description.

### Supported dimerization and functional conversion

graph: supported. Targets: GO:1990065.

The two edges encode homodimeric assembly and the NADPH-dependent reductoisomerase reaction. Those coarse steps have source support; MECHANISTIC scope is not treated as evidence of resolved intermediates, rate constants or a universal requirement for dimerization. The abstract supplies active-site closure context while the deposition supplies assembly identity.

### Species, reference strain and expression host

scope: supported. Targets: GO:1990065.

The E. coli canonical example is supported. P45568 is a K12 reference, while BL21(DE3) is recorded as an expression host. The two-copy physical property remains tied to the named deposition. No absent optional taxonomic-distribution row is treated as an error.

### Observed dimer versus necessity of assembly

grounding: unknown. Targets: GO:1990065.

The observed dimer does not constitute a component-removal experiment or establish that every catalytic state requires the same assembly. UNKNOWN formation essentiality is retained.

### Whole maintained record and bounded follow-up

completeness: supported. Targets: GO:1990065.

All maintained fields, evidence, component/example rows, graph edges, discussion entries and history were read. Available exact mappings are distinguished from optional enrichment and source-access limitations. Scientific status and provenance history remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dxr_protein_complex.yaml; Entire maintained record, including all evidence, components, graph, discussions and history | context_only | The complete maintained target was read; related structures are assessed only where this target names them. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, PresenceEnum and graph scope | context_only | Formation necessity differs from activity, recruitment into a larger assembly or viability. Where used, COMMON means present in most members with exceptional losses. This category is distinct from a measured prevalence census. |
| curation | docs/CURATION.md; Exact class identity and REVIEWED_LABEL_ONLY contract | context_only | A family grounds the named protein class, while the taxon-paired accession is a representative instance. Exact class mappings can resolve a label-only task. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Graph evidence and scope | context_only | Composition, coarse functional chemistry and a detailed molecular mechanism are assessed separately. |
| root53-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000124,GO:0004843,GO:0005783,GO:0006890,GO:0030604,GO:0032991,GO:0046695,GO:0070939,GO:0071819,GO:0099023,GO:0140513,GO:1990065; All twelve term definitions, identity/status, synonyms, comments, source xrefs and relevant typed child links; relation types preserved | supports | The twelve active native terms establish the focal complex identities, declared parents, SAGA/SLIK boundaries, cellular locations and functions. GO0070939 has an unrelated acetolactate-synthase comment that the target does not import. GO0030604 specifies the reversible reductoisomerase reaction; its written reverse direction does not contradict forward NADPH consumption. |
| root53-sources-GO1990065-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990065/ancestors?relations=is_a; Complete native ancestor response; no parthood inferred from ancestry | supports | The is_a-only ancestry includes protein-containing complex GO0032991. |
| root53-sources-GO1990065-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990065/constraints; Focal taxonConstraints presence and complete array where present; inherited broad-term exclusions are not distribution evidence | context_only | The focal response has no taxonConstraints field; this does not establish universal distribution. |
| root53-sources-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxonomy response | supports | ENA identifies 562 as Escherichia coli. Species and reference-strain scopes remain distinct. |
| root53-sources-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxonomy response | supports | ENA identifies 83333 as Escherichia coli K-12. Species and reference-strain scopes remain distinct. |
| root53-sources-pmid-15567415 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15567415+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and entire abstractText | supports | MED 15567415: The crystal structure of E.coli 1-deoxy-D-xylulose-5-phosphate reductoisomerase in a ternary complex with the antimalarial compound fosmidomycin and NADPH reveals a tight-binding closed enzyme conformation. Authors Mac Sweeney A, Lange R, Fernandes RP, Schulz H, Dale GE, Douangamath A, Proteau PJ, Oefner C.; year 2005; DOI 10.1016/j.jmb.2004.10.030. Complete abstract read; primary body scope is separately declared. |
| root53-sources-doi-10.1016_j.jmb.2004.10.030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jmb.2004.10.030%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and entire abstractText | supports | The exact DOI resolves to MED 15567415, The crystal structure of E.coli 1-deoxy-D-xylulose-5-phosphate reductoisomerase in a ternary complex with the antimalarial compound fosmidomycin and NADPH reveals a tight-binding closed enzyme conformation., Mac Sweeney A, Lange R, Fernandes RP, Schulz H, Dale GE, Douangamath A, Proteau PJ, Oefner C. (2005). Its full abstract was read; fetching a body elsewhere does not imply full-body inspection. |
| root53-sources-protein-P45568 | https://rest.uniprot.org/uniprotkb/P45568.json; Identity/status/recommended and alternative names, genes, organism; all InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments where present | supports | P45568 is the reviewed dxr entry in taxon 83333. The entry lists dxr, ispC and yaeM names, homodimeric subunits and the NADPH-dependent reductoisomerase reaction. |
| root53-sources-gene-dxr | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adxr%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set; exact-gene plus organism_id and reviewed filter; size 500 | supports | The exact-gene reviewed query restricted to organism_id 83333 returns the declared single accession P45568. |
| root53-sources-gene-ispC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AispC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set; exact-gene plus organism_id and reviewed filter; size 500 | supports | The exact-gene reviewed query restricted to organism_id 83333 returns the declared single accession P45568. |
| root53-sources-ipr-IPR003821 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003821/; Native accession/name/type, complete descriptions and flags, hierarchy and integrated member signatures | supports | Exact Dxr reductoisomerase whole-protein family, with MF00183/TIGR00243/PIRSF006205/PTHR30525 signatures. Separate P45568 data establish example membership. |
| root53-sources-pdb-1Q0Q-entry | https://data.rcsb.org/rest/v1/core/entry/1Q0Q; Entry title, experiment/resolution, deposited entity and instance counts, entity identifiers and complete primary citation | supports | The entry is the 1.9 A substrate-bound E. coli Dxr structure with two deposited protein chains and primary citation PMID15567415/DOI10.1016/j.jmb.2004.10.030. The paper also describes a separate fosmidomycin complex; that title does not rename this deposition. |
| root53-sources-pdb-1Q0Q-polymer1 | https://data.rcsb.org/rest/v1/core/polymer_entity/1Q0Q/1; Entity description, chain/asym IDs, sequence length and mutation count, source/expression taxonomy and complete reference sequence mapping | supports | Polymer entity 1 has Dxr chains A and B, species E. coli and UniProt P45568 SIFTS mapping. The reference covers the native sequence while the construct includes a tag. BL21(DE3) is the expression host; it is not a claim that the K12 reference entry is that host strain. |
| root53-sources-pdb-1Q0Q-assembly1 | https://data.rcsb.org/rest/v1/core/assembly/1Q0Q/1; Complete biological-assembly metadata, oligomeric count/details, protein cluster and symmetry descriptors | supports | Author/software biological assembly 1 is dimeric, with two protein instances and an A2/C2 protein symmetry cluster. Its full asym-unit list includes small molecules and must not be counted as additional protein subunits. |
| root53-sources-pdb1q0q-nonpolymer2 | https://data.rcsb.org/rest/v1/core/nonpolymer_entity/1Q0Q/2; Complete native nonpolymer entity record, chemical identity, chain instances and molecule count | supports | Entity 2 is DXP, 1-deoxy-D-xylulose-5-phosphate, with two molecules associated with protein chains A/B. |
| root53-sources-pdb1q0q-nonpolymer3 | https://data.rcsb.org/rest/v1/core/nonpolymer_entity/1Q0Q/3; Complete native nonpolymer entity record, chemical identity, chain instances and molecule count | supports | Entity 3 is NDP, explicitly named NADPH, with two molecules associated with protein chains A/B. |
| schema-result | just validate data/structures/other/dxr_protein_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dxr_protein_complex.yaml |
| strict-result | just validate-strict data/structures/other/dxr_protein_complex.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dxr_protein_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dxr_protein_complex.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dxr_protein_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch53-20261022-kx679dvh/dxr_protein_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dxr_protein_complex.yaml; Complete focused native report | supports | data/structures/other/dxr_protein_complex.yaml  (GO:1990065)<br>  dxr_reductoisomerase_function	dxr_reductoisomerase	COVERED	-&gt;dxr_reductoisomerase (UniProtKB:P45568)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/dxr_protein_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dxr_protein_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 10 collected target identifiers returned OK. PDB:1Q0Q: SKIPPED; Exact RCSB entry identifier, structure title and primary citation DOI/PMID independently read. Deposition-specific composition, ligands and structural interpretation retain the separately reviewed evidence scopes; the paper title does not substitute for entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:15567415: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw data, atomic coordinates, sequence alignments or supplements were reanalyzed. Native protein annotation links and separately read primary text are distinct evidence tiers.
- Mac Sweeney 2005 was assessed at complete native abstract plus deposition-metadata tier; the article body, detailed assay methods and raw coordinates were not read. The abstract cautions that the substrate complex contains a second diastereomer. This qualified pass does not certify detailed inhibitor geometry, kinetic necessity of dimerization or taxon-wide stoichiometry.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations as well as issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T062449Z-dxr-protein-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of Dxr protein complex
started_at: '2026-10-22T06:03:29Z'
finished_at: '2026-10-22T06:24:49Z'
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
summary: 'Qualified pass: exact Dxr identity/family, reviewed dxr/ispC example, E.
  coli substrate/NADPH homodimer and coarse functional graph are supported. Primary-body,
  coordinate and assembly-necessity limits remain explicit.'
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
  - path: data/structures/other/dxr_protein_complex.yaml
    sha256: 0a9e8c00028f315a781db6e7d819a864d844254eaa639b885573f818907bae5e
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
- target_id: GO:1990065
  path: data/structures/other/dxr_protein_complex.yaml
  label: Dxr protein complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dxr_protein_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target; native-source fields and primary
    reading scopes are declared in evidence. Scientific inputs remain unchanged.
  selection: One complete record in strict-path batch 53 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990065
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: just validate data/structures/other/dxr_protein_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: just validate-strict data/structures/other/dxr_protein_complex.yaml --out
    /private/tmp/cellstructure-batch53-20261022-kx679dvh/dxr_protein_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dxr_protein_complex.yaml
  exit_code: 0
  summary: Focused check passed; source claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dxr_protein_complex.yaml
  exit_code: 0
  summary: Focused check passed; source claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990065
  summary: No expression-module or transcriptomic claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990065
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root53-sources-go
  - root53-sources-GO1990065-ancestors
  - root53-sources-GO1990065-constraints
  - root53-sources-tax562
  - root53-sources-tax83333
  - root53-sources-pmid-15567415
  - root53-sources-doi-10.1016_j.jmb.2004.10.030
  - root53-sources-protein-P45568
  - root53-sources-gene-dxr
  - root53-sources-gene-ispC
  - root53-sources-ipr-IPR003821
  - root53-sources-pdb-1Q0Q-entry
  - root53-sources-pdb-1Q0Q-polymer1
  - root53-sources-pdb-1Q0Q-assembly1
  - root53-sources-pdb1q0q-nonpolymer2
  - root53-sources-pdb1q0q-nonpolymer3
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990065
  summary: '8 of 10 collected target identifiers returned OK. PDB:1Q0Q: SKIPPED; Exact
    RCSB entry identifier, structure title and primary citation DOI/PMID independently
    read. Deposition-specific composition, ligands and structural interpretation retain
    the separately reviewed evidence scopes; the paper title does not substitute for
    entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:15567415:
    UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read
    following the bulk eutils414 transport failure. Resolution is identifier identity
    only; separate primary-body/abstract evidence limits remain in force. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.'
  evidence_ids:
  - target-curies
  - root53-sources-pdb-1Q0Q-entry
  - root53-sources-pmid-15567415
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch53 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch53 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch53 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch53 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990065
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
    and current batch53 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dxr_protein_complex.yaml
  locator: Entire maintained record, including all evidence, components, graph, discussions
    and history
  accessed_at: '2026-10-22T06:15:30Z'
  support: context_only
  summary: The complete maintained target was read; related structures are assessed
    only where this target names them.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, PresenceEnum and graph scope
  accessed_at: '2026-10-22T06:15:30Z'
  support: context_only
  summary: Formation necessity differs from activity, recruitment into a larger assembly
    or viability. Where used, COMMON means present in most members with exceptional
    losses. This category is distinct from a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and REVIEWED_LABEL_ONLY contract
  accessed_at: '2026-10-22T06:15:30Z'
  support: context_only
  summary: A family grounds the named protein class, while the taxon-paired accession
    is a representative instance. Exact class mappings can resolve a label-only task.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph evidence and scope
  accessed_at: '2026-10-22T06:15:30Z'
  support: context_only
  summary: Composition, coarse functional chemistry and a detailed molecular mechanism
    are assessed separately.
- evidence_id: root53-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000124,GO:0004843,GO:0005783,GO:0006890,GO:0030604,GO:0032991,GO:0046695,GO:0070939,GO:0071819,GO:0099023,GO:0140513,GO:1990065
  locator: All twelve term definitions, identity/status, synonyms, comments, source
    xrefs and relevant typed child links; relation types preserved
  accessed_at: '2026-10-22T06:06:00.951715Z'
  support: supports
  summary: The twelve active native terms establish the focal complex identities,
    declared parents, SAGA/SLIK boundaries, cellular locations and functions. GO0070939
    has an unrelated acetolactate-synthase comment that the target does not import.
    GO0030604 specifies the reversible reductoisomerase reaction; its written reverse
    direction does not contradict forward NADPH consumption.
  snapshot_sha256: 1ca0dac2d9f398d290817228e2290a52a1444cc9ebea6b8324d0a056c9cd4c84
- evidence_id: root53-sources-GO1990065-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990065/ancestors?relations=is_a
  locator: Complete native ancestor response; no parthood inferred from ancestry
  accessed_at: '2026-10-22T06:06:08.823924Z'
  support: supports
  summary: The is_a-only ancestry includes protein-containing complex GO0032991.
  snapshot_sha256: 9b7b56bd21c9039545b6bb1c56b0bed9f02238c1f52583ba80beb1dc9a6bf7a2
- evidence_id: root53-sources-GO1990065-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990065/constraints
  locator: Focal taxonConstraints presence and complete array where present; inherited
    broad-term exclusions are not distribution evidence
  accessed_at: '2026-10-22T06:06:09.142177Z'
  support: context_only
  summary: The focal response has no taxonConstraints field; this does not establish
    universal distribution.
  snapshot_sha256: 69479b43ae0ea84b767eac640779af8d8ef72e70acd00c073e774c8ad439156d
- evidence_id: root53-sources-tax562
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:06:02.432813Z'
  support: supports
  summary: ENA identifies 562 as Escherichia coli. Species and reference-strain scopes
    remain distinct.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: root53-sources-tax83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:06:02.497347Z'
  support: supports
  summary: ENA identifies 83333 as Escherichia coli K-12. Species and reference-strain
    scopes remain distinct.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: root53-sources-pmid-15567415
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15567415+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and entire abstractText
  accessed_at: '2026-10-22T06:06:03.083944Z'
  support: supports
  summary: 'MED 15567415: The crystal structure of E.coli 1-deoxy-D-xylulose-5-phosphate
    reductoisomerase in a ternary complex with the antimalarial compound fosmidomycin
    and NADPH reveals a tight-binding closed enzyme conformation. Authors Mac Sweeney
    A, Lange R, Fernandes RP, Schulz H, Dale GE, Douangamath A, Proteau PJ, Oefner
    C.; year 2005; DOI 10.1016/j.jmb.2004.10.030. Complete abstract read; primary
    body scope is separately declared.'
  snapshot_sha256: 87a75c10075ef6940192438abe689af0e34b4a7816dade4ef3c3b74cb170b00b
- evidence_id: root53-sources-doi-10.1016_j.jmb.2004.10.030
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jmb.2004.10.030%22+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and
    entire abstractText'
  accessed_at: '2026-10-22T06:06:00.952156Z'
  support: supports
  summary: The exact DOI resolves to MED 15567415, The crystal structure of E.coli
    1-deoxy-D-xylulose-5-phosphate reductoisomerase in a ternary complex with the
    antimalarial compound fosmidomycin and NADPH reveals a tight-binding closed enzyme
    conformation., Mac Sweeney A, Lange R, Fernandes RP, Schulz H, Dale GE, Douangamath
    A, Proteau PJ, Oefner C. (2005). Its full abstract was read; fetching a body elsewhere
    does not imply full-body inspection.
  snapshot_sha256: 99c6f4e827b66bbe75cd93bd7c618749a4e58be556032de94d50970d1276bbd1
- evidence_id: root53-sources-protein-P45568
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P45568.json
  locator: Identity/status/recommended and alternative names, genes, organism; all
    InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:06:04.040721Z'
  support: supports
  summary: P45568 is the reviewed dxr entry in taxon 83333. The entry lists dxr, ispC
    and yaeM names, homodimeric subunits and the NADPH-dependent reductoisomerase
    reaction.
  snapshot_sha256: 3cc676d623cb06e717c43f25cfe46cd3972378877ebb100d5fbf9951f39c4aa8
- evidence_id: root53-sources-gene-dxr
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adxr%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set; exact-gene plus organism_id and reviewed
    filter; size 500
  accessed_at: '2026-10-22T06:06:07.749876Z'
  support: supports
  summary: The exact-gene reviewed query restricted to organism_id 83333 returns the
    declared single accession P45568.
  snapshot_sha256: 72aa997329fd9ec39c983db4b58a3a87fab2b868cf67e2d50316a456264bece2
- evidence_id: root53-sources-gene-ispC
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AispC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set; exact-gene plus organism_id and reviewed
    filter; size 500
  accessed_at: '2026-10-22T06:06:07.848682Z'
  support: supports
  summary: The exact-gene reviewed query restricted to organism_id 83333 returns the
    declared single accession P45568.
  snapshot_sha256: 72aa997329fd9ec39c983db4b58a3a87fab2b868cf67e2d50316a456264bece2
- evidence_id: root53-sources-ipr-IPR003821
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003821/
  locator: Native accession/name/type, complete descriptions and flags, hierarchy
    and integrated member signatures
  accessed_at: '2026-10-22T06:06:01.827201Z'
  support: supports
  summary: Exact Dxr reductoisomerase whole-protein family, with MF00183/TIGR00243/PIRSF006205/PTHR30525
    signatures. Separate P45568 data establish example membership.
  snapshot_sha256: a3fbe1c1ff8c08bfe94fb7f6c3b1e116dc3a025d6e96adba27e2d2e62b79b6d4
- evidence_id: root53-sources-pdb-1Q0Q-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1Q0Q
  locator: Entry title, experiment/resolution, deposited entity and instance counts,
    entity identifiers and complete primary citation
  accessed_at: '2026-10-22T06:06:09.385437Z'
  support: supports
  summary: The entry is the 1.9 A substrate-bound E. coli Dxr structure with two deposited
    protein chains and primary citation PMID15567415/DOI10.1016/j.jmb.2004.10.030.
    The paper also describes a separate fosmidomycin complex; that title does not
    rename this deposition.
  snapshot_sha256: cd09cbe75bd95d779c6a1c3f8442aab0c4de5475703e856330974b088b1da0dc
- evidence_id: root53-sources-pdb-1Q0Q-polymer1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1Q0Q/1
  locator: Entity description, chain/asym IDs, sequence length and mutation count,
    source/expression taxonomy and complete reference sequence mapping
  accessed_at: '2026-10-22T06:06:09.410581Z'
  support: supports
  summary: Polymer entity 1 has Dxr chains A and B, species E. coli and UniProt P45568
    SIFTS mapping. The reference covers the native sequence while the construct includes
    a tag. BL21(DE3) is the expression host; it is not a claim that the K12 reference
    entry is that host strain.
  snapshot_sha256: a772fc5c2b6cb75e80900f22daa31217457638cb02b3f867f6249cc99eb54ddc
- evidence_id: root53-sources-pdb-1Q0Q-assembly1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/1Q0Q/1
  locator: Complete biological-assembly metadata, oligomeric count/details, protein
    cluster and symmetry descriptors
  accessed_at: '2026-10-22T06:06:09.460379Z'
  support: supports
  summary: Author/software biological assembly 1 is dimeric, with two protein instances
    and an A2/C2 protein symmetry cluster. Its full asym-unit list includes small
    molecules and must not be counted as additional protein subunits.
  snapshot_sha256: a652f9f8739e0d113e77502e95fe955aaa57a69fbcd2ddf43f182608655191d2
- evidence_id: root53-sources-pdb1q0q-nonpolymer2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/nonpolymer_entity/1Q0Q/2
  locator: Complete native nonpolymer entity record, chemical identity, chain instances
    and molecule count
  accessed_at: '2026-10-22T06:12:46.523182Z'
  support: supports
  summary: Entity 2 is DXP, 1-deoxy-D-xylulose-5-phosphate, with two molecules associated
    with protein chains A/B.
  snapshot_sha256: 2e9d2a9da7a3640e0d1f73b91adcbd16e214a1913dd02f38795e90e3fdb97468
- evidence_id: root53-sources-pdb1q0q-nonpolymer3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/nonpolymer_entity/1Q0Q/3
  locator: Complete native nonpolymer entity record, chemical identity, chain instances
    and molecule count
  accessed_at: '2026-10-22T06:12:46.598716Z'
  support: supports
  summary: Entity 3 is NDP, explicitly named NADPH, with two molecules associated
    with protein chains A/B.
  snapshot_sha256: 32dd31ca5a3bd0c7f58e8a0c822498cd0149e957ad086a41cf2105b93939760a
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dxr_protein_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:03:33Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dxr_protein_complex.yaml'
  snapshot_sha256: 6e85dc78dd6221e26a6b230dd4c1939aa75042bf89b55ecd36f2fa7a1cc5ce05
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dxr_protein_complex.yaml --out
    /private/tmp/cellstructure-batch53-20261022-kx679dvh/dxr_protein_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:03:34Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dxr_protein_complex.yaml\
    \ --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dxr_protein_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch53-20261022-kx679dvh/dxr_protein_complex-strict.tsv"
  snapshot_sha256: 631f76e65ad6618bfb6d0c56e6bb7c014f8baac3fc90742e2cfe8a36de913ae1
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dxr_protein_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:06:10.120264Z'
  support: supports
  summary: "data/structures/other/dxr_protein_complex.yaml  (GO:1990065)\n  dxr_reductoisomerase_function\t\
    dxr_reductoisomerase\tCOVERED\t->dxr_reductoisomerase (UniProtKB:P45568)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     1  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     1  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: df2ee219a494b4e317e88c9b090a533138fc496c62bc029f1baba3b3c92f069c
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dxr_protein_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:06:11.619254Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dxr_protein_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 10 collected target identifiers returned OK. PDB:1Q0Q: SKIPPED; Exact
    RCSB entry identifier, structure title and primary citation DOI/PMID independently
    read. Deposition-specific composition, ligands and structural interpretation retain
    the separately reviewed evidence scopes; the paper title does not substitute for
    entry identity. No PDB resolver adapter exists in the bulk gate.; PMID:15567415:
    UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read
    following the bulk eutils414 transport failure. Resolution is identifier identity
    only; separate primary-body/abstract evidence limits remain in force. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.'
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
  topic: Dxr homodimer as a protein complex
  outcome: supported
  target_ids:
  - GO:1990065
  summary: Exact GO identity, synonym and protein-complex parent are supported. The
    record describes a homomeric assembly rather than confusing a single protein family
    with an assembly; two-copy stoichiometry is explicitly scoped to E. coli PDB1Q0Q.
  evidence_ids:
  - record
  - root53-sources-go
  - root53-sources-GO1990065-ancestors
  - root53-sources-pdb-1Q0Q-entry
  - root53-sources-pdb-1Q0Q-polymer1
  - root53-sources-pdb-1Q0Q-assembly1
- assessment_id: composition
  area: grounding
  topic: Exact family, reference accession and two protein chains
  outcome: supported
  target_ids:
  - GO:1990065
  summary: IPR003821 is the exact full-protein class and P45568 is the reviewed K12
    dxr/ispC example. Native polymer and biological-assembly data corroborate the
    stated homodimer and scoped SUBUNIT_COUNT. Ligand entities are distinct from protein
    constituents.
  evidence_ids:
  - record
  - root53-sources-ipr-IPR003821
  - root53-sources-pdb-1Q0Q-entry
  - root53-sources-pdb-1Q0Q-polymer1
  - root53-sources-pdb-1Q0Q-assembly1
  - root53-sources-protein-P45568
  - root53-sources-gene-dxr
  - root53-sources-gene-ispC
  - root53-sources-pdb1q0q-nonpolymer2
  - root53-sources-pdb1q0q-nonpolymer3
- assessment_id: evidence
  area: evidence
  topic: Substrate complex and NADPH chemistry
  outcome: supported
  target_ids:
  - GO:1990065
  summary: PDB1Q0Q contains DXP and NADPH. The paper abstract distinguishes the 1.9
    A substrate complex from the 2.2 A inhibitor complex and cautions about a second
    substrate diastereomer. Forward DXP-to-MEP reduction consumes NADPH; the formal
    GO reaction may be written in reverse. Generic NADP-dependent wording in the inherited
    definition is clarified by the record’s explicit NADPH functional description.
  evidence_ids:
  - record
  - root53-sources-go
  - root53-sources-pdb-1Q0Q-entry
  - root53-sources-pmid-15567415
  - root53-sources-pdb1q0q-nonpolymer2
  - root53-sources-pdb1q0q-nonpolymer3
  - root53-sources-doi-10.1016_j.jmb.2004.10.030
  - root53-sources-protein-P45568
- assessment_id: graph
  area: graph
  topic: Supported dimerization and functional conversion
  outcome: supported
  target_ids:
  - GO:1990065
  summary: The two edges encode homodimeric assembly and the NADPH-dependent reductoisomerase
    reaction. Those coarse steps have source support; MECHANISTIC scope is not treated
    as evidence of resolved intermediates, rate constants or a universal requirement
    for dimerization. The abstract supplies active-site closure context while the
    deposition supplies assembly identity.
  evidence_ids:
  - record
  - graphs
  - root53-sources-go
  - root53-sources-pdb-1Q0Q-assembly1
  - root53-sources-pmid-15567415
  - root53-sources-protein-P45568
- assessment_id: scope
  area: scope
  topic: Species, reference strain and expression host
  outcome: supported
  target_ids:
  - GO:1990065
  summary: The E. coli canonical example is supported. P45568 is a K12 reference,
    while BL21(DE3) is recorded as an expression host. The two-copy physical property
    remains tied to the named deposition. No absent optional taxonomic-distribution
    row is treated as an error.
  evidence_ids:
  - record
  - root53-sources-GO1990065-constraints
  - root53-sources-pdb-1Q0Q-entry
  - root53-sources-pdb-1Q0Q-polymer1
  - root53-sources-pdb-1Q0Q-assembly1
  - root53-sources-tax562
  - root53-sources-tax83333
  - root53-sources-protein-P45568
- assessment_id: formation
  area: grounding
  topic: Observed dimer versus necessity of assembly
  outcome: unknown
  target_ids:
  - GO:1990065
  summary: The observed dimer does not constitute a component-removal experiment or
    establish that every catalytic state requires the same assembly. UNKNOWN formation
    essentiality is retained.
  evidence_ids:
  - record
  - schema
  - root53-sources-pdb-1Q0Q-assembly1
  - root53-sources-pmid-15567415
- assessment_id: coverage
  area: completeness
  topic: Whole maintained record and bounded follow-up
  outcome: supported
  target_ids:
  - GO:1990065
  summary: All maintained fields, evidence, component/example rows, graph edges, discussion
    entries and history were read. Available exact mappings are distinguished from
    optional enrichment and source-access limitations. Scientific status and provenance
    history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root53-sources-go
  - root53-sources-doi-10.1016_j.jmb.2004.10.030
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw data, atomic coordinates, sequence alignments or supplements
  were reanalyzed. Native protein annotation links and separately read primary text
  are distinct evidence tiers.
- Mac Sweeney 2005 was assessed at complete native abstract plus deposition-metadata
  tier; the article body, detailed assay methods and raw coordinates were not read.
  The abstract cautions that the substrate complex contains a second diastereomer.
  This qualified pass does not certify detailed inhibitor geometry, kinetic necessity
  of dimerization or taxon-wide stoichiometry.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations as well as issue-bearing
  reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
