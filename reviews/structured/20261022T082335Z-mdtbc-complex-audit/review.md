# Source-backed review of mdtbc complex

- Review: 20261022T082335Z-mdtbc-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:57:57Z
- Finished UTC: 2026-10-22T08:23:35Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor oligomer-wording inconsistency in the MdtB role. Correct B2C stoichiometry, identities and transport context are otherwise supported, with source-stage and formation limits retained.

## Scope And Provenance

Exactly one entire target and 13 frozen input files. Sources/native identities were independently read within the declared extents; no neighboring maintained record is an unstated premise.

Selection: Batch59 strict ordered selection index 5; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990203 | data/structures/other/mdtbc_complex.yaml | maintained | MdtBC Complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990203 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990203 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:1990203 | Focused check passed; claim-level science assessed independently. |
| Focused native verify | passed | True | GO:1990203 | Focused check passed; claim-level science assessed independently. |
| Claim-level scientific review | passed | True | GO:1990203 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990203 | 11 of 12 collected target identifiers returned OK. PMID:20038594: UNREACHABLE; Native Europe PMC uniquely identifies MED20038594: Multidrug efflux pump MdtBC of Escherichia coli is active only as a B2C heterotrimer. (2010); DOI10.1128/jb.01448-09. Identifier transport verification is distinct from separately scoped primary-source reading. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990203 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990203 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990203 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990203 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990203 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact inner-membrane B2C class

identity: supported. Targets: GO:1990203.

Active GO1990203 and Kim2010 agree with the two protein classes and three physical protomers. The GO phrase two subunits refers to the two types; the record explicitly gives B2:C1. The whole MdtA/TolC conduit is not confused with this core.

### Unknown formation necessity retained

evidence: unknown. Targets: GO:1990203.

The two UNKNOWN labels appropriately avoid converting linked-construct transport activity or expression differences into universal subunit-formation requirements. The paper can recover B homooligomers and engineered incomplete constructs without establishing an active B-C dimer.

### Supported coarse heterotrimer and transport relationships

graph: supported. Targets: GO:1990203.

The graph explicitly describes two MdtB plus one MdtC and complementary contributions to proton-driven export. Kim2010 directly supports the heterotrimer and differential mutant effects, but leaves the precise MdtC role unresolved. No atomic proton route or equal AcrB-style rotating roles are read into the coarse edge; the later secondary synthesis is separately identified.

### Existing exact families and examples

grounding: supported. Targets: GO:1990203.

The existing MdtB and MdtC family identifiers and reviewed K-12 proteins match the two named classes.

### One local oligomer wording inconsistency

consistency: concern. Targets: GO:1990203.

Counts and the overall model correctly state B2:C1, but the MdtB role says it dimerizes with MdtC. Kim2010 distinguishes the active heterotrimer from an engineered B-C dimer.

### Bacterial distribution and assay backgrounds

scope: supported. Targets: GO:1990203.

VARIABLE retains the nonuniform-distribution meaning. Kim2010 Discussion describes widespread enterobacterial homologs and uneven distribution elsewhere, rather than a census. Reviewed K-12 exemplars and the source-specific K-12/B-lineage experimental backgrounds are distinct.

### Entire maintained target with explicit source tiers

completeness: supported. Targets: GO:1990203.

Every target field, current discussion, graph, example and history entry was read. Existing named proteins and source IDs were checked. Optional absent detail alone is not treated as a defect; no maintained scientific content was changed.

## Findings

### F1: Describe the MdtB2C heterotrimer precisely

minor / open / confirmed; issue key: mdtbc-complex-mdtb-dimer-wording.

The MdtB role says it dimerizes with MdtC, which reads as a two-protomer B-C complex. The same record correctly supplies two MdtB and one MdtC, and Kim2010 identifies the active assembly as B2C; its linked B-C dimer experiments do not establish an active heterodimer.

## Recommended Actions And Acceptance Checks

### A1

Replace the dimerizes-with wording with two MdtB protomers associating with one MdtC to form the B2C heterotrimer; preserve correct counts, family mappings and the broader transport model.

- The role explicitly describes two MdtB protomers associating with one MdtC to form the active heterotrimer.
- No required standalone MdtB-MdtC heterodimer intermediate is inferred from the engineered linked-dimer experiments.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/mdtbc_complex.yaml; Entire maintained YAML, including all scientific fields, examples, graphs, images, discussions and history | context_only | All target bytes were read; no neighboring record is an unstated scientific premise. |
| curation | docs/CURATION.md; Exact component-class grounding and reviewed-label-only contract | context_only | Species accessions establish examples, not automatic whole-class groundings; acknowledged unknowns and empty optional slots alone are not defects. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum, StructuralComponent and causal graphs | context_only | Physical formation necessity is distinct from function, viability and localization. COMMON means present in most members, with exceptional losses; VARIABLE means nonuniform occurrence, not merely unknown prevalence. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Actor, stage and edge-level source scope | context_only | A coarse mechanism may omit unresolved intermediates, but source-specific claims must retain assay, species and epistemic boundaries. |
| micro59-pmid-20038594 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20038594+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity fields and complete abstractText. | supports | PMID20038594: Multidrug efflux pump MdtBC of Escherichia coli is active only as a B2C heterotrimer. Kim HS, Nagore D, Nikaido H. (2010), DOI10.1128/jb.01448-09. The complete native abstract was read; this row does not imply main-body access. |
| micro59-protein-P76398 | https://rest.uniprot.org/uniprotkb/P76398.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed P76398 identifies mdtB in taxon83333. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-mdtB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmdtB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed mdtB query for organism83333 returns only P76398; primary name or declared synonym matches. |
| micro59-protein-P76399 | https://rest.uniprot.org/uniprotkb/P76399.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references. | supports | Reviewed P76399 identifies mdtC in taxon83333. Native protein/gene aliases, organism, function, subunit and location comments were inspected. Its InterPro cross-references independently corroborate the relevant class mapping where present. Unlisted annotation papers are not certified as read. |
| micro59-gene-mdtC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmdtC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set; exact gene_exact, organism_id and reviewed:true query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename conflation. | supports | The exact reviewed mdtC query for organism83333 returns only P76399; primary name or declared synonym matches. |
| micro59-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Native taxId, scientificName, rank, lineage and relevant equivalent names. | supports | ENA taxId2 identifies Bacteria, rank domain. Reference strains and experimental cultures are distinguished. |
| micro59-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Native taxId, scientificName, rank, lineage and relevant equivalent names. | supports | ENA taxId562 identifies Escherichia coli, rank species. Reference strains and experimental cultures are distinguished. |
| micro59-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Native taxId, scientificName, rank, lineage and relevant equivalent names. | supports | ENA taxId83333 identifies Escherichia coli K-12, rank strain. Reference strains and experimental cultures are distinguished. |
| micro59-IPR022831 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022831/; Complete type/name/descriptions/member_databases; whole-family versus domain scope. | supports | IPR022831 is the Multidrug resistance protein MdtB family. Native description and member signatures were read; protein accession membership is supplied separately by native UniProt evidence. Generic background mechanism is not treated as a new direct experiment. |
| micro59-IPR023931 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023931/; Complete type/name/descriptions/member_databases; whole-family versus domain scope. | supports | IPR023931 is the Multidrug resistance protein MdtC family. Native description and member signatures were read; protein accession membership is supplied separately by native UniProt evidence. Generic background mechanism is not treated as a new direct experiment. |
| micro59-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228,GO:0000781,GO:0005634,GO:0032200,GO:0032993,GO:0034993,GO:0042910,GO:0045141,GO:0140330,GO:1902495,GO:1990203,GO:1990281,GO:1990612; Only these five exact entries in the combined native response: active identity, definition, synonyms and typed links. | supports | GO1990203 is the MdtBC complex with two MdtB and one MdtC; GO1902495 is its transmembrane-transporter parent. GO1990281 denotes the broader efflux-pump complex. GO0042910 is xenobiotic transmembrane transporter activity and GO0140330 concerns export across the outer membrane. |
| micro59-GO1990203-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990203/ancestors?relations=is_a; Complete exact requested-term ancestor array. | supports | The exact is_a-only response supports the named transporter/protein-complex hierarchy. It is not a physical-part inventory. |
| micro59-kim2010-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2820868/; Genuine primary HTML: Results sec11–14 and sec16, Discussion sec17; Methods sec2, sec6–8; Tables1/2 and embedded captions in those sections. Results sec15, other Methods, supplements and figure pixels not read. | supports | Co-purification/BN-PAGE and engineered linked constructs support the active B2C heterotrimer. Marginal activity from a linked B-C dimer is attributed to reassembly with an additional B protomer, not an active heterodimer. Mutations distinguish the subunits, but the precise MdtC role remains unresolved in the 2010 Discussion. K-12 AG100A and B-derived BL21KAMR assays are distinct. |
| micro59-anes2015-numeric | https://pmc.ncbi.nlm.nih.gov/articles/4462101/; Secondary review: complete sec6, Multidrug Transport (Mdt) Efflux System, including MdtABC and the separate MdtEF paragraphs. Other sections and figure pixels not read. | supports | The secondary Mdt-system synthesis lists the broader substrate set and distinguishes MdtB2C architecture from homotrimeric RND pumps. Its proposed MdtC substrate pathway/MdtB coupling account draws on later studies; it is not a result uniquely demonstrated by Kim2010. |
| schema-result | just validate data/structures/other/mdtbc_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/mdtbc_complex.yaml |
| strict-result | just validate-strict data/structures/other/mdtbc_complex.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mdtbc_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/mdtbc_complex.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mdtbc_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mdtbc_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mdtbc_complex.yaml --causal-graphs; Complete focused read-only native log | supports | data/structures/other/mdtbc_complex.yaml  (GO:1990203)<br>  mdtbc_heterotrimer_efflux	mdtb_multidrug_resistance_protein	COVERED	-&gt;mdtb_multidrug_resistance_protein (UniProtKB:P76398)<br>  mdtbc_heterotrimer_efflux	mdtc_multidrug_resistance_protein	COVERED	-&gt;mdtc_multidrug_resistance_protein (UniProtKB:P76399)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mdtbc_complex.yaml --verify; Complete focused read-only native log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/mdtbc_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 12 collected target identifiers returned OK. PMID:20038594: UNREACHABLE; Native Europe PMC uniquely identifies MED20038594: Multidrug efflux pump MdtBC of Escherichia coli is active only as a B2C heterotrimer. (2010); DOI10.1128/jb.01448-09. Identifier transport verification is distinct from separately scoped primary-source reading. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Primary bodies were read only in the exact sections/captions stated per source. No Mdt figure pixels, raw measurements or supplements were inspected. Anes2015 is a secondary synthesis, not a new primary assay.
- Kim2010 did not settle the precise MdtC mechanism. Later proposed MdtC substrate routing is not attributed to the 2010 study. Engineered linked constructs and strain-specific resistance assays are not universal formation tests.
- Reference K-12 proteins do not imply that BL21KAMR is K-12. VARIABLE is qualitative nonuniform distribution rather than an exhaustive prevalence measurement.
- Reused source bytes retain original URL, UTC and SHA256. HTTP status alone is not treated as evidence of article-body readability.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requests a review for every unreviewed record, including qualified clean cases.
- No maintained record, historical review or initial inspection snapshot is edited.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T082335Z-mdtbc-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of mdtbc complex
started_at: '2026-10-22T07:57:57Z'
finished_at: '2026-10-22T08:23:35Z'
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
summary: One minor oligomer-wording inconsistency in the MdtB role. Correct B2C stoichiometry,
  identities and transport context are otherwise supported, with source-stage and
  formation limits retained.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/other/mdtbc_complex.yaml
    sha256: c89b2ca25a4a0f79dde997d4df92cf552d7a7e34c523850879a1a06812967f7b
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
- target_id: GO:1990203
  path: data/structures/other/mdtbc_complex.yaml
  label: MdtBC Complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mdtbc_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target and 13 frozen input files. Sources/native
    identities were independently read within the declared extents; no neighboring
    maintained record is an unstated premise.
  selection: Batch59 strict ordered selection index 5; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990203
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990203
  command: just validate data/structures/other/mdtbc_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990203
  command: just validate-strict data/structures/other/mdtbc_complex.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mdtbc_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990203
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mdtbc_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; claim-level science assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:1990203
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mdtbc_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; claim-level science assessed independently.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990203
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-pmid-20038594
  - micro59-protein-P76398
  - micro59-gene-mdtB
  - micro59-protein-P76399
  - micro59-gene-mdtC
  - micro59-tax2
  - micro59-tax562
  - micro59-tax83333
  - micro59-IPR022831
  - micro59-IPR023931
  - micro59-go
  - micro59-GO1990203-ancestors
  - micro59-kim2010-legacy
  - micro59-anes2015-numeric
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990203
  summary: '11 of 12 collected target identifiers returned OK. PMID:20038594: UNREACHABLE;
    Native Europe PMC uniquely identifies MED20038594: Multidrug efflux pump MdtBC
    of Escherichia coli is active only as a B2C heterotrimer. (2010); DOI10.1128/jb.01448-09.
    Identifier transport verification is distinct from separately scoped primary-source
    reading. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro59-pmid-20038594
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990203
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990203
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990203
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990203
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990203
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
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/mdtbc_complex.yaml
  locator: Entire maintained YAML, including all scientific fields, examples, graphs,
    images, discussions and history
  accessed_at: '2026-10-22T08:10:24Z'
  support: context_only
  summary: All target bytes were read; no neighboring record is an unstated scientific
    premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact component-class grounding and reviewed-label-only contract
  accessed_at: '2026-10-22T08:10:24Z'
  support: context_only
  summary: Species accessions establish examples, not automatic whole-class groundings;
    acknowledged unknowns and empty optional slots alone are not defects.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum, StructuralComponent and causal graphs
  accessed_at: '2026-10-22T08:10:24Z'
  support: context_only
  summary: Physical formation necessity is distinct from function, viability and localization.
    COMMON means present in most members, with exceptional losses; VARIABLE means
    nonuniform occurrence, not merely unknown prevalence.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Actor, stage and edge-level source scope
  accessed_at: '2026-10-22T08:10:24Z'
  support: context_only
  summary: A coarse mechanism may omit unresolved intermediates, but source-specific
    claims must retain assay, species and epistemic boundaries.
- evidence_id: micro59-pmid-20038594
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20038594+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity fields and complete abstractText.
  accessed_at: '2026-10-22T08:02:49.411428Z'
  support: supports
  summary: 'PMID20038594: Multidrug efflux pump MdtBC of Escherichia coli is active
    only as a B2C heterotrimer. Kim HS, Nagore D, Nikaido H. (2010), DOI10.1128/jb.01448-09.
    The complete native abstract was read; this row does not imply main-body access.'
  snapshot_sha256: 36ae37c4c32b2baca2495022b792b7690181247d0c325985c6857f441b05b038
- evidence_id: micro59-protein-P76398
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P76398.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:47.913320Z'
  support: supports
  summary: Reviewed P76398 identifies mdtB in taxon83333. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: 09888b8e7f53fb5d09e78201af8b6d8e8ea40638658816d5f3075e5268a139f9
- evidence_id: micro59-gene-mdtB
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmdtB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:51.645495Z'
  support: supports
  summary: The exact reviewed mdtB query for organism83333 returns only P76398; primary
    name or declared synonym matches.
  snapshot_sha256: 34d82633080e7b02c33b0f42829a05deccc2193dff7caa95b6c8504a92975436
- evidence_id: micro59-protein-P76399
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P76399.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:02:47.969582Z'
  support: supports
  summary: Reviewed P76399 identifies mdtC in taxon83333. Native protein/gene aliases,
    organism, function, subunit and location comments were inspected. Its InterPro
    cross-references independently corroborate the relevant class mapping where present.
    Unlisted annotation papers are not certified as read.
  snapshot_sha256: 95198345e4a0d484155f88604eb9911f0eb47aa7b6f8b68b748851bc31e16515
- evidence_id: micro59-gene-mdtC
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmdtC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set; exact gene_exact, organism_id and reviewed:true
    query in retained URL. Taxon-suffixed RAP1/rap1 files avoid case-insensitive filename
    conflation.
  accessed_at: '2026-10-22T08:02:51.859557Z'
  support: supports
  summary: The exact reviewed mdtC query for organism83333 returns only P76399; primary
    name or declared synonym matches.
  snapshot_sha256: b9178105202005af6e40d69fc7e8709d80b4255440b3482fc6c5a1ec255dfcb8
- evidence_id: micro59-tax2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Native taxId, scientificName, rank, lineage and relevant equivalent names.
  accessed_at: '2026-10-22T08:02:45.872475Z'
  support: supports
  summary: ENA taxId2 identifies Bacteria, rank domain. Reference strains and experimental
    cultures are distinguished.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: micro59-tax562
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Native taxId, scientificName, rank, lineage and relevant equivalent names.
  accessed_at: '2026-10-22T08:02:46.541746Z'
  support: supports
  summary: ENA taxId562 identifies Escherichia coli, rank species. Reference strains
    and experimental cultures are distinguished.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: micro59-tax83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Native taxId, scientificName, rank, lineage and relevant equivalent names.
  accessed_at: '2026-10-22T08:02:46.566205Z'
  support: supports
  summary: ENA taxId83333 identifies Escherichia coli K-12, rank strain. Reference
    strains and experimental cultures are distinguished.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro59-IPR022831
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022831/
  locator: Complete type/name/descriptions/member_databases; whole-family versus domain
    scope.
  accessed_at: '2026-10-22T08:02:55.296286Z'
  support: supports
  summary: IPR022831 is the Multidrug resistance protein MdtB family. Native description
    and member signatures were read; protein accession membership is supplied separately
    by native UniProt evidence. Generic background mechanism is not treated as a new
    direct experiment.
  snapshot_sha256: 02cb7fd2daee17c35410a58e635d6d3cdc8097a0ca7db10083f6743d890b9f14
- evidence_id: micro59-IPR023931
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023931/
  locator: Complete type/name/descriptions/member_databases; whole-family versus domain
    scope.
  accessed_at: '2026-10-22T08:02:56.074228Z'
  support: supports
  summary: IPR023931 is the Multidrug resistance protein MdtC family. Native description
    and member signatures were read; protein accession membership is supplied separately
    by native UniProt evidence. Generic background mechanism is not treated as a new
    direct experiment.
  snapshot_sha256: 0a97dcde85af41232323457a898e0fa0a4dfcca45569fd65fb786d855a3e0b56
- evidence_id: micro59-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228,GO:0000781,GO:0005634,GO:0032200,GO:0032993,GO:0034993,GO:0042910,GO:0045141,GO:0140330,GO:1902495,GO:1990203,GO:1990281,GO:1990612
  locator: 'Only these five exact entries in the combined native response: active
    identity, definition, synonyms and typed links.'
  accessed_at: '2026-10-22T08:02:45.199131Z'
  support: supports
  summary: GO1990203 is the MdtBC complex with two MdtB and one MdtC; GO1902495 is
    its transmembrane-transporter parent. GO1990281 denotes the broader efflux-pump
    complex. GO0042910 is xenobiotic transmembrane transporter activity and GO0140330
    concerns export across the outer membrane.
  snapshot_sha256: 9e094b28069fbc79cfeda88c524a5f4e8008c759ca9c3cf282ef6cb86f379f6e
- evidence_id: micro59-GO1990203-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990203/ancestors?relations=is_a
  locator: Complete exact requested-term ancestor array.
  accessed_at: '2026-10-22T08:02:45.199583Z'
  support: supports
  summary: The exact is_a-only response supports the named transporter/protein-complex
    hierarchy. It is not a physical-part inventory.
  snapshot_sha256: a2e6a25db2ce190942f7e29da0cb5b1e7861c7c2235f47d46682a90fe1b218d0
- evidence_id: micro59-kim2010-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2820868/
  locator: 'Genuine primary HTML: Results sec11–14 and sec16, Discussion sec17; Methods
    sec2, sec6–8; Tables1/2 and embedded captions in those sections. Results sec15,
    other Methods, supplements and figure pixels not read.'
  accessed_at: '2026-10-22T08:03:31.323662Z'
  support: supports
  summary: Co-purification/BN-PAGE and engineered linked constructs support the active
    B2C heterotrimer. Marginal activity from a linked B-C dimer is attributed to reassembly
    with an additional B protomer, not an active heterodimer. Mutations distinguish
    the subunits, but the precise MdtC role remains unresolved in the 2010 Discussion.
    K-12 AG100A and B-derived BL21KAMR assays are distinct.
  snapshot_sha256: e6000c963789e568c48abda4c23e6e30dc95888caf5e3a1ce6a75f9fd005c97e
- evidence_id: micro59-anes2015-numeric
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4462101/
  locator: 'Secondary review: complete sec6, Multidrug Transport (Mdt) Efflux System,
    including MdtABC and the separate MdtEF paragraphs. Other sections and figure
    pixels not read.'
  accessed_at: '2026-10-22T04:23:28.684685Z'
  support: supports
  summary: The secondary Mdt-system synthesis lists the broader substrate set and
    distinguishes MdtB2C architecture from homotrimeric RND pumps. Its proposed MdtC
    substrate pathway/MdtB coupling account draws on later studies; it is not a result
    uniquely demonstrated by Kim2010.
  snapshot_sha256: f3de337eac24e04a75268bfe64674aa246c6a575bafff92cfad5aea68158070d
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/mdtbc_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:57:58Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/mdtbc_complex.yaml'
  snapshot_sha256: e873e7b55f0feda1810d883a85930ea15fe271d2e3503b3c6eaef99a38ae800a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/mdtbc_complex.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mdtbc_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:57:59Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/mdtbc_complex.yaml\
    \ --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mdtbc_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mdtbc_complex-strict.tsv"
  snapshot_sha256: 3f368685e98b746fc4b5a427000394d21ad19b8c8513ffc9d1b11fcd88cbd626
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mdtbc_complex.yaml
    --causal-graphs
  locator: Complete focused read-only native log
  accessed_at: '2026-10-22T08:04:28.065146Z'
  support: supports
  summary: "data/structures/other/mdtbc_complex.yaml  (GO:1990203)\n  mdtbc_heterotrimer_efflux\t\
    mdtb_multidrug_resistance_protein\tCOVERED\t->mdtb_multidrug_resistance_protein\
    \ (UniProtKB:P76398)\n  mdtbc_heterotrimer_efflux\tmdtc_multidrug_resistance_protein\t\
    COVERED\t->mdtc_multidrug_resistance_protein (UniProtKB:P76399)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 05d1cf0de11e0139b8b8d515e36edca4b1802c68aef221a7d4d13698257bde29
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mdtbc_complex.yaml
    --verify
  locator: Complete focused read-only native log
  accessed_at: '2026-10-22T08:04:29.197936Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/mdtbc_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 12 collected target identifiers returned OK. PMID:20038594: UNREACHABLE;
    Native Europe PMC uniquely identifies MED20038594: Multidrug efflux pump MdtBC
    of Escherichia coli is active only as a B2C heterotrimer. (2010); DOI10.1128/jb.01448-09.
    Identifier transport verification is distinct from separately scoped primary-source
    reading. Native source checks are separately scoped; skipped or unreachable identifiers
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
  topic: Exact inner-membrane B2C class
  outcome: supported
  target_ids:
  - GO:1990203
  summary: Active GO1990203 and Kim2010 agree with the two protein classes and three
    physical protomers. The GO phrase two subunits refers to the two types; the record
    explicitly gives B2:C1. The whole MdtA/TolC conduit is not confused with this
    core.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-go
  - micro59-GO1990203-ancestors
  - micro59-kim2010-legacy
- assessment_id: formation
  area: evidence
  topic: Unknown formation necessity retained
  outcome: unknown
  target_ids:
  - GO:1990203
  summary: The two UNKNOWN labels appropriately avoid converting linked-construct
    transport activity or expression differences into universal subunit-formation
    requirements. The paper can recover B homooligomers and engineered incomplete
    constructs without establishing an active B-C dimer.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-kim2010-legacy
- assessment_id: graph
  area: graph
  topic: Supported coarse heterotrimer and transport relationships
  outcome: supported
  target_ids:
  - GO:1990203
  summary: The graph explicitly describes two MdtB plus one MdtC and complementary
    contributions to proton-driven export. Kim2010 directly supports the heterotrimer
    and differential mutant effects, but leaves the precise MdtC role unresolved.
    No atomic proton route or equal AcrB-style rotating roles are read into the coarse
    edge; the later secondary synthesis is separately identified.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-kim2010-legacy
  - micro59-anes2015-numeric
  - micro59-go
- assessment_id: grounding
  area: grounding
  topic: Existing exact families and examples
  outcome: supported
  target_ids:
  - GO:1990203
  summary: The existing MdtB and MdtC family identifiers and reviewed K-12 proteins
    match the two named classes.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-IPR022831
  - micro59-IPR023931
  - micro59-protein-P76398
  - micro59-protein-P76399
  - micro59-gene-mdtB
  - micro59-gene-mdtC
- assessment_id: stoichiometry
  area: consistency
  topic: One local oligomer wording inconsistency
  outcome: concern
  target_ids:
  - GO:1990203
  summary: Counts and the overall model correctly state B2:C1, but the MdtB role says
    it dimerizes with MdtC. Kim2010 distinguishes the active heterotrimer from an
    engineered B-C dimer.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-kim2010-legacy
  - micro59-go
- assessment_id: scope
  area: scope
  topic: Bacterial distribution and assay backgrounds
  outcome: supported
  target_ids:
  - GO:1990203
  summary: VARIABLE retains the nonuniform-distribution meaning. Kim2010 Discussion
    describes widespread enterobacterial homologs and uneven distribution elsewhere,
    rather than a census. Reviewed K-12 exemplars and the source-specific K-12/B-lineage
    experimental backgrounds are distinct.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-kim2010-legacy
  - micro59-anes2015-numeric
  - micro59-tax2
  - micro59-tax562
  - micro59-tax83333
  - micro59-protein-P76398
  - micro59-protein-P76399
- assessment_id: coverage
  area: completeness
  topic: Entire maintained target with explicit source tiers
  outcome: supported
  target_ids:
  - GO:1990203
  summary: Every target field, current discussion, graph, example and history entry
    was read. Existing named proteins and source IDs were checked. Optional absent
    detail alone is not treated as a defect; no maintained scientific content was
    changed.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-go
  - micro59-GO1990203-ancestors
  - micro59-kim2010-legacy
  - micro59-anes2015-numeric
  - micro59-pmid-20038594
  - micro59-protein-P76398
  - micro59-protein-P76399
  - micro59-gene-mdtB
  - micro59-gene-mdtC
  - micro59-tax2
  - micro59-tax562
  - micro59-tax83333
  - micro59-IPR022831
  - micro59-IPR023931
findings:
- finding_id: F1
  issue_key: mdtbc-complex-mdtb-dimer-wording
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Describe the MdtB2C heterotrimer precisely
  description: The MdtB role says it dimerizes with MdtC, which reads as a two-protomer
    B-C complex. The same record correctly supplies two MdtB and one MdtC, and Kim2010
    identifies the active assembly as B2C; its linked B-C dimer experiments do not
    establish an active heterodimer.
  target_ids:
  - GO:1990203
  field_paths:
  - components[0].role
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro59-kim2010-legacy
  - micro59-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mdtbc_complex.yaml
    role: maintained scientific record
  rule_id: Stoichiometry and claim-level source precision
  native_severity: minor
  normalization_reason: Localized oligomer wording conflicts with correct B2C stoichiometry
    already represented elsewhere; the structure identity, component inventory and
    functional heterotrimer remain sound.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990203
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mdtbc_complex.yaml
    role: maintained scientific record
  description: Replace the dimerizes-with wording with two MdtB protomers associating
    with one MdtC to form the B2C heterotrimer; preserve correct counts, family mappings
    and the broader transport model.
  acceptance_checks:
  - The role explicitly describes two MdtB protomers associating with one MdtC to
    form the active heterotrimer.
  - No required standalone MdtB-MdtC heterodimer intermediate is inferred from the
    engineered linked-dimer experiments.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- Primary bodies were read only in the exact sections/captions stated per source.
  No Mdt figure pixels, raw measurements or supplements were inspected. Anes2015 is
  a secondary synthesis, not a new primary assay.
- Kim2010 did not settle the precise MdtC mechanism. Later proposed MdtC substrate
  routing is not attributed to the 2010 study. Engineered linked constructs and strain-specific
  resistance assays are not universal formation tests.
- Reference K-12 proteins do not imply that BL21KAMR is K-12. VARIABLE is qualitative
  nonuniform distribution rather than an exhaustive prevalence measurement.
- Reused source bytes retain original URL, UTC and SHA256. HTTP status alone is not
  treated as evidence of article-body readability.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requests a review for every unreviewed record, including qualified
  clean cases.
- No maintained record, historical review or initial inspection snapshot is edited.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
