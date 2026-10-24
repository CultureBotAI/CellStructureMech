# Endocytic clathrin vesicle identity, topology and evidence review

- Review: 20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:57:17Z
- Finished UTC: 2026-10-21T11:13:29Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact structure identities, parent/part boundaries and scoped material representation are coherent. No concrete curation finding was established. The yeast model evidence supports recruitment dynamics, with the unresolved sealed-vesicle transition explicitly retained as a source limitation.

## Scope And Provenance

Entire single maintained target, both endocytic siblings, the exact local generic-lumen parent and declared boundary portions of generic vesicle/membrane and coat records; native identities and named literature sections.

Selection: Target 4 in batch twenty-three; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030669 | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml | maintained | clathrin-coated endocytic vesicle membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0030669 | Focused command passed. The target asserts no UniProtKB protein examples or GENE_OR_PROTEIN graph nodes. |
| Native protein causal-graphs | passed | True | GO:0030669 | Focused command passed. The target asserts no UniProtKB protein examples or GENE_OR_PROTEIN graph nodes. |
| Focused native schema | passed | True | GO:0030669 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030669 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0030669 | 9 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0030669 | No expression-module or transcriptomic inference is asserted. |
| Claim-level scientific review | passed | True | GO:0030669 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0030669 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030669 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030669 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030669 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0030669 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole vesicle, lumen, membrane and coat boundaries

identity: supported. Targets: GO:0030669.

The active GO identities match the maintained target and distinguish the whole endocytic vesicle from its bilayer, enclosed volume and external protein coat. These endocytic subtypes are not synonyms of all clathrin-coated vesicles or coats at TGN/endosomal sites. The generic-lumen local parent remains broader than GO:0106176.

### Type, physical inclusion and membrane enclosure

consistency: supported. Targets: GO:0030669.

The maintained is_a parents and part_of/has_part statements agree with the returned native child relations and definitions. The two lumen parents express the independent endocytic and generic-clathrin-coated classifications; the local parent resolves to captured maintained bytes. The coat is a named structural part rather than lipid material. A membrane bounds a volume/vesicle without becoming identical to the cargo.

### Material identity and component responsibility

grounding: supported. Targets: GO:0030669.

The sole direct component is collective lipid-bilayer material. Its REVIEWED_LABEL_ONLY rationale correctly avoids using whole-membrane GO:0030669 as a chemical lipid identity. ESSENTIAL denotes the constitutive bilayer at this collective level; it asserts neither a specific lipid species nor universal clathrin necessity for membrane formation. The protein coat remains a separately named has_part structure.

### Yeast model context and observation limits

scope: supported. Targets: GO:0030669.

The taxon/name and S. cerevisiae experiment are verified. The maintained notes describe cortical clathrin/adaptor recruitment and an endocytic-site model. COMMON is qualitative occurrence context, not a measured population percentage. Newpher directly supports site-associated recruitment dynamics; it does not directly resolve the coat-retention/scission transition or image a sealed lumen. The lumen wording about dynamics marking formation is interpreted as this model context, not a claim that the paper measured lumen closure.

### Sealed-vesicle transition is not directly resolved

evidence: unknown. Targets: GO:0030669.

The source cannot discriminate clathrin disassembly before budding from movement of a clathrin-bearing vesicle or bud out of the TIRF field. Direct observation of a sealed, still-coated yeast carrier and its lumen is therefore not established by Newpher2005. This limitation does not refute the generic native topology and is not filled by treating fluorescent puncta as resolved vesicles.

### Bounded topology and endocytic participation

graph: supported. Targets: GO:0030669.

Every maintained graph edge was read. Coat/membrane parthood, bilayer enclosure and lumen inclusion are supported by the native structural definitions and typed relations. Where present, participation in clathrin-dependent endocytosis follows the exact process definition. All graphs remain NONMECHANISTIC and assert no complete adaptor-assembly, cargo-selection or actin-scission sequence. The membrane component_ref is a link to the collective constituent, not a chemical grounding of GO:0030669.

### Accurate bibliographic identities and source scope

provenance: supported. Targets: GO:0030669.

The actual retrieved sources match their declared URLs, hashes and access times. Primary PDF text was inspected only at the named sections; captions do not constitute image-pixel reanalysis. The native identifiers establish structure/type identity independently of experiment-specific recruitment and necessity claims. No verbatim snippet, image provenance or historical-source-read certification is added.

### Whole-target review with bounded neighboring inspection

completeness: supported. Targets: GO:0030669.

The full target record, two sibling targets and generic-lumen parent were read. Other named neighbor records were inspected only at the declared boundary/component fields; their separate scientific completeness is not claimed. Optional molecular inventories, exact dimensions, images, traits and expression modules are not required for these topological records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml; Entire maintained YAML, including all evidence notes, graphs, discussions and history | context_only | All maintained fields were read; no scientific, mapping-status, history or generated-page edit is made. |
| policy | docs/CURATION.md; Exact identity, structural-part versus molecular-component grounding, and component assembly-essentiality contract | context_only | Whole vesicle, protein coat, membrane and lumen have distinct identities. Constitutive collective bilayer material does not imply that each lipid species or coat protein is required for membrane formation. |
| neighbor-clathrin_coated_endocytic_vesicle | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml; Entire neighboring endocytic record | context_only | Read for the organelle/membrane/lumen boundary and consistency of coat parthood. This is context, not a second review target. |
| neighbor-clathrin_coated_endocytic_vesicle_lumen | data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml; Entire neighboring endocytic record | context_only | Read for the organelle/membrane/lumen boundary and consistency of coat parthood. This is context, not a second review target. |
| generic-lumen | data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml; Entire record; exact identifier, definition, parent and enclosing vesicle | context_only | The maintained local identifier cellstructuremech:clathrin_coated_vesicle_lumen resolves to the broader clathrin-coated vesicle lumen. Its definition and host class make the endocytic lumen a proper subtype; a local CURIE is not itself a missing scientific grounding. |
| neighbor-clathrin_coated_vesicle | data/structures/membrane_organelle/clathrin_coated_vesicle.yaml; Identifier, definition, hierarchy, components and discussions | context_only | The generic vesicle and membrane are broader classes than their endocytic subtypes. Their material/structure distinction is consistent with this target; other fields of these neighboring records are not separately certified. |
| neighbor-clathrin_coated_vesicle_membrane | data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml; Identifier, definition, hierarchy, components and discussions | context_only | The generic vesicle and membrane are broader classes than their endocytic subtypes. Their material/structure distinction is consistent with this target; other fields of these neighboring records are not separately certified. |
| coat-boundary | data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml; Identifier, definition, parent/parthood, component classes and boundary discussions | context_only | The separate GO:0030128 record owns the clathrin scaffold and adaptor-level inventory. Reading its boundary and component entries does not independently revalidate its protein examples or require their duplication on this whole-vesicle/membrane/lumen target. |
| local-search | data/structures/; Ignored-inclusive exact-ID search of data/structures YAML for GO:0045334, GO:0106176, GO:0030669, GO:0030128 and the local generic-lumen identifier | context_only | The search included hidden and ignored files and identified related records for boundary checking. It is a bounded corpus search; no exhaustive ontology or literature absence claim is made. |
| endocytic-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045334,GO:0106176,GO:0030669,GO:0030136,GO:0030139,GO:0030128,GO:0072583,GO:0071682,GO:0030665,GO:0030666; Complete returned exact identifiers, names, isObsolete, definitions, aspects and relevant child-relation fields | supports | All ten returned GO terms are active. Exact names/definitions identify the endocytic vesicle GO:0045334, membrane GO:0030669 and lumen GO:0106176. Returned children explicitly establish the vesicle and membrane is_a parents, lumen GO:0071682 parent, membrane/lumen part_of the whole vesicle, and coat GO:0030128 part_of the membrane. GO:0072583 defines the clathrin-dependent endocytic process. Membrane enclosure is also supported by the exact definitions; no separate bounding-layer relation absent from this response is claimed to have been observed. |
| endocytic-agent-ancestors-0030669 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030669/ancestors?relations=is_a,part_of; Exact target id and complete ancestors response; requested relations is_a,part_of | supports | The complete combined is_a/part_of closure for the exact target agrees with its endocytic and clathrin-coated context. Relation types are checked separately in term children and definitions rather than inferred from an untyped ancestor list. |
| clathrin-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank and lineage | supports | Native ENA taxonomy identifies NCBITaxon:4932 as Saccharomyces cerevisiae at species rank. This verifies the identifier/name pair, not the frequency of any phenotype or identity of a particular experimental stock. |
| clathrin-agent-doi-10.1016_j.devcel.2005.04.014 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2005.04.014; Exact title, authors, DOI/PMID, publication year and complete abstract | supports | Native Europe PMC MED identifies Newpher, Smith, Lemmon and Lemmon 2005, PMID15992543, DOI10.1016/j.devcel.2005.04.014, with the maintained title. The complete abstract describes cortical clathrin recruitment, adaptor dependence and actin-associated endocytic sites; full-body scope is recorded separately. |
| root23-sources-newpher2005-duke | https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content; Published pages87–96: Summary/Introduction, relevant Results and Discussion, Table1, figure captions1–6 and Experimental Procedures/Microscopy; no figure pixels or supplementary movies reanalysed | supports | The genuine publisher-format PDF in Duke repository was inspected at Summary/Introduction, Results on localization, cortical accumulation, cargo/Abp1 association and adaptor recruitment, Discussion including the TIRF limitations, Table1 and relevant microscopy Methods. S. cerevisiae fluorescent clathrin reporters mark dynamic cortical endocytic sites, distinct from internal TGN/endosome-associated clathrin. The Discussion explicitly cannot distinguish disassembly before budding from a clathrin-bearing vesicle or bud leaving the TIRF field. Thus this paper supports the yeast model and coat recruitment timing, not direct observation of sealed lumen, membrane scission or retained coat on every released vesicle. |
| clathrin-agent-SL-0319 | https://rest.uniprot.org/locations/SL-0319.json; id, name, definition, absence of a top-level geneOntologies field, exact isA and partOf objects | supports | Native SL-0319 identifies the generic clathrin-coated vesicle lumen as the compartment bounded by its membrane, classifies it under cytoplasmic-vesicle lumen and names the generic clathrin-coated vesicle as its partOf host. It has no direct geneOntologies field in this response. The local parent is retained as a broader local structure, not misidentified as the endocytic-specific GO:0106176. |
| clathrin-agent-kaksonen2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2005.09.024; Exact bibliography and complete native abstract | partial | Native MED identifies Kaksonen, Toret and Drubin2005, PMID16239147, DOI10.1016/j.cell.2005.09.024. The complete abstract describes mutant/live-imaging analysis and modules for coat formation, invagination, actin assembly and scission. It explicitly finds clathrin facilitates initiation but is not needed for membrane invagination or vesicle formation in the studied yeast system. This is abstract-level evidence, not a Methods or figure audit. |
| clathrin-agent-kaksonen2005-api | https://api.elsevier.com/content/article/PII:S0092867405009785?httpAccept=text/xml; Complete1937-byte API response; coredata and no article body | context_only | The public Elsevier article API returned HTTP200 XML with bibliographic coredata only; it contained no article body. Full-text-retrieval in the XML root name is not evidence that full text was obtained. |
| clathrin-agent-kaksonen2005-core | https://core.ac.uk/download/pdf/82329151.pdf; Actual source-access response, not article text | context_only | This legitimate public full-text route returned HTTP403; no article body was read from this response. |
| clathrin-agent-kaksonen2005-publisher | https://www.sciencedirect.com/science/article/pii/S0092867405009785; Actual source-access response, not article text | context_only | This legitimate public full-text route returned HTTP403; no article body was read from this response. |
| clathrin-agent-kaksonen2005-cellpdf | https://www.cell.com/article/S0092867405009785/pdf; Actual source-access response, not article text | context_only | This legitimate public full-text route returned HTTP403; no article body was read from this response. |
| native-verify | /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml --verify; Exact focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml --causal-graphs; Exact focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_endocytic_vesicle_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_endocytic_vesicle_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_endocytic_vesicle_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 9 of9 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Newpher2005 directly supports yeast cortical recruitment and endocytic-site dynamics, but explicitly leaves clathrin disassembly versus coated-vesicle departure unresolved. No direct sealed-lumen, scission or universal coat-retention assay is claimed.
- Kaksonen2005 was read through its complete native abstract and metadata only. Public publisher/repository routes returned403, while the HTTP200 API returned bibliographic coredata without article text. No body or figure read is claimed.
- The qualitative COMMON scope is not a numerical prevalence measurement across strains or growth conditions. No exhaustive molecular inventory, lipid composition or individual formation necessity is established.
- Figure pixels, supplementary movies and raw microscopy were not reanalysed. Historical curator searches and independent historical authorship are not certified.
- Root attaches the completed fresh-base global gates only at finalization; this temporary draft records actual focused native checks and the exact target resolver slice.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized a review for every uncovered target, including a target without findings. Only root may finalize or save the bundle.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T111329Z-clathrin-coated-endocytic-vesicle-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Endocytic clathrin vesicle identity, topology and evidence review
started_at: '2026-10-21T10:57:17Z'
finished_at: '2026-10-21T11:13:29Z'
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
summary: Exact structure identities, parent/part boundaries and scoped material representation
  are coherent. No concrete curation finding was established. The yeast model evidence
  supports recruitment dynamics, with the unresolved sealed-vesicle transition explicitly
  retained as a source limitation.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
    sha256: 3193e3f6ea811d515c1545dc4e9179c8122e8718a328ed11261c7b648e94343d
    role: context
  - path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
    sha256: d3a53daa5cc28635e48242bfa4d7dab04186a8c7f17b40a1491de51e94a33951
    role: context
  - path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    sha256: 70d8d315440e5cc7cc4c8f8c11a9103d74deffa773df25d9051113122d8a189a
    role: target
  - path: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
    sha256: cee241afc73475bcdec9d8c3c4c57bdf9c4cb2f726e4a78615dfb393613be9ad
    role: context
  - path: data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
    sha256: 2137a192f721232651c140497813cea3f15a73a67e910194d59fadc7837308f9
    role: context
  - path: data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
    sha256: 963e3cbe094c98b1279923d8f4ecc6a27343f82aa7240dece427fa09882c25f1
    role: context
  - path: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
    sha256: 1c156e9a910b42e01f74505011a1f24644ca3ad0a8eeb48d438b3b8eeb7ed372
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
- target_id: GO:0030669
  path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
  label: clathrin-coated endocytic vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target, both endocytic siblings, the exact
    local generic-lumen parent and declared boundary portions of generic vesicle/membrane
    and coat records; native identities and named literature sections.
  selection: Target 4 in batch twenty-three; exact sorted uncovered path at frozen
    fresh-main revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030669
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0030669
  command: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    --verify
  exit_code: 0
  summary: Focused command passed. The target asserts no UniProtKB protein examples
    or GENE_OR_PROTEIN graph nodes.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030669
  command: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused command passed. The target asserts no UniProtKB protein examples
    or GENE_OR_PROTEIN graph nodes.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030669
  command: just validate data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030669
  command: just validate-strict data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_endocytic_vesicle_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0030669
  summary: 9 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030669
  summary: No expression-module or transcriptomic inference is asserted.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030669
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - neighbor-clathrin_coated_endocytic_vesicle
  - neighbor-clathrin_coated_endocytic_vesicle_lumen
  - generic-lumen
  - neighbor-clathrin_coated_vesicle
  - neighbor-clathrin_coated_vesicle_membrane
  - coat-boundary
  - local-search
  - endocytic-agent-go
  - endocytic-agent-ancestors-0030669
  - clathrin-agent-tax4932
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - root23-sources-newpher2005-duke
  - clathrin-agent-SL-0319
  - clathrin-agent-kaksonen2005-meta
  - clathrin-agent-kaksonen2005-api
  - clathrin-agent-kaksonen2005-core
  - clathrin-agent-kaksonen2005-publisher
  - clathrin-agent-kaksonen2005-cellpdf
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030669
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
  - GO:0030669
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
  - GO:0030669
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
  - GO:0030669
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
  - GO:0030669
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
  reference: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
  locator: Entire maintained YAML, including all evidence notes, graphs, discussions
    and history
  accessed_at: '2026-10-21T11:08:14Z'
  support: context_only
  summary: All maintained fields were read; no scientific, mapping-status, history
    or generated-page edit is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, structural-part versus molecular-component grounding, and
    component assembly-essentiality contract
  accessed_at: '2026-10-21T11:08:14Z'
  support: context_only
  summary: Whole vesicle, protein coat, membrane and lumen have distinct identities.
    Constitutive collective bilayer material does not imply that each lipid species
    or coat protein is required for membrane formation.
- evidence_id: neighbor-clathrin_coated_endocytic_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle.yaml
  locator: Entire neighboring endocytic record
  accessed_at: '2026-10-21T11:08:14Z'
  support: context_only
  summary: Read for the organelle/membrane/lumen boundary and consistency of coat
    parthood. This is context, not a second review target.
- evidence_id: neighbor-clathrin_coated_endocytic_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_lumen.yaml
  locator: Entire neighboring endocytic record
  accessed_at: '2026-10-21T11:08:14Z'
  support: context_only
  summary: Read for the organelle/membrane/lumen boundary and consistency of coat
    parthood. This is context, not a second review target.
- evidence_id: generic-lumen
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle_lumen.yaml
  locator: Entire record; exact identifier, definition, parent and enclosing vesicle
  accessed_at: '2026-10-21T11:08:14Z'
  support: context_only
  summary: The maintained local identifier cellstructuremech:clathrin_coated_vesicle_lumen
    resolves to the broader clathrin-coated vesicle lumen. Its definition and host
    class make the endocytic lumen a proper subtype; a local CURIE is not itself a
    missing scientific grounding.
- evidence_id: neighbor-clathrin_coated_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle.yaml
  locator: Identifier, definition, hierarchy, components and discussions
  accessed_at: '2026-10-21T11:08:14Z'
  support: context_only
  summary: The generic vesicle and membrane are broader classes than their endocytic
    subtypes. Their material/structure distinction is consistent with this target;
    other fields of these neighboring records are not separately certified.
- evidence_id: neighbor-clathrin_coated_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/clathrin_coated_vesicle_membrane.yaml
  locator: Identifier, definition, hierarchy, components and discussions
  accessed_at: '2026-10-21T11:08:14Z'
  support: context_only
  summary: The generic vesicle and membrane are broader classes than their endocytic
    subtypes. Their material/structure distinction is consistent with this target;
    other fields of these neighboring records are not separately certified.
- evidence_id: coat-boundary
  kind: record_content
  reference: data/structures/other/clathrin_coat_of_endocytic_vesicle.yaml
  locator: Identifier, definition, parent/parthood, component classes and boundary
    discussions
  accessed_at: '2026-10-21T11:08:14Z'
  support: context_only
  summary: The separate GO:0030128 record owns the clathrin scaffold and adaptor-level
    inventory. Reading its boundary and component entries does not independently revalidate
    its protein examples or require their duplication on this whole-vesicle/membrane/lumen
    target.
- evidence_id: local-search
  kind: record_content
  reference: data/structures/
  locator: Ignored-inclusive exact-ID search of data/structures YAML for GO:0045334,
    GO:0106176, GO:0030669, GO:0030128 and the local generic-lumen identifier
  accessed_at: '2026-10-21T11:08:14Z'
  support: context_only
  summary: The search included hidden and ignored files and identified related records
    for boundary checking. It is a bounded corpus search; no exhaustive ontology or
    literature absence claim is made.
- evidence_id: endocytic-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045334,GO:0106176,GO:0030669,GO:0030136,GO:0030139,GO:0030128,GO:0072583,GO:0071682,GO:0030665,GO:0030666
  locator: Complete returned exact identifiers, names, isObsolete, definitions, aspects
    and relevant child-relation fields
  accessed_at: '2026-10-21T11:06:24.236585Z'
  support: supports
  summary: All ten returned GO terms are active. Exact names/definitions identify
    the endocytic vesicle GO:0045334, membrane GO:0030669 and lumen GO:0106176. Returned
    children explicitly establish the vesicle and membrane is_a parents, lumen GO:0071682
    parent, membrane/lumen part_of the whole vesicle, and coat GO:0030128 part_of
    the membrane. GO:0072583 defines the clathrin-dependent endocytic process. Membrane
    enclosure is also supported by the exact definitions; no separate bounding-layer
    relation absent from this response is claimed to have been observed.
  snapshot_sha256: 3e0c3bb0d57477942c2058c1ea14c0ed8c37a64856901ab4ee6c6e204c4bbded
- evidence_id: endocytic-agent-ancestors-0030669
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030669/ancestors?relations=is_a,part_of
  locator: Exact target id and complete ancestors response; requested relations is_a,part_of
  accessed_at: '2026-10-21T11:06:24.239942Z'
  support: supports
  summary: The complete combined is_a/part_of closure for the exact target agrees
    with its endocytic and clathrin-coated context. Relation types are checked separately
    in term children and definitions rather than inferred from an untyped ancestor
    list.
  snapshot_sha256: 54ff2635dbf02e51579fe91f6e986b70aad68d119d015d86d0edf91e789db488
- evidence_id: clathrin-agent-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T11:04:40.023078Z'
  support: supports
  summary: Native ENA taxonomy identifies NCBITaxon:4932 as Saccharomyces cerevisiae
    at species rank. This verifies the identifier/name pair, not the frequency of
    any phenotype or identity of a particular experimental stock.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2005.04.014
  locator: Exact title, authors, DOI/PMID, publication year and complete abstract
  accessed_at: '2026-10-21T10:57:50.523144Z'
  support: supports
  summary: Native Europe PMC MED identifies Newpher, Smith, Lemmon and Lemmon 2005,
    PMID15992543, DOI10.1016/j.devcel.2005.04.014, with the maintained title. The
    complete abstract describes cortical clathrin recruitment, adaptor dependence
    and actin-associated endocytic sites; full-body scope is recorded separately.
  snapshot_sha256: c99ec084fa3f65e3b5107699c30f42b09489dbc49d6be518d71ff9352d5a199c
- evidence_id: root23-sources-newpher2005-duke
  kind: primary_source
  reference: https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content
  locator: 'Published pages87–96: Summary/Introduction, relevant Results and Discussion,
    Table1, figure captions1–6 and Experimental Procedures/Microscopy; no figure pixels
    or supplementary movies reanalysed'
  accessed_at: '2026-10-21T11:00:52.091438Z'
  support: supports
  summary: The genuine publisher-format PDF in Duke repository was inspected at Summary/Introduction,
    Results on localization, cortical accumulation, cargo/Abp1 association and adaptor
    recruitment, Discussion including the TIRF limitations, Table1 and relevant microscopy
    Methods. S. cerevisiae fluorescent clathrin reporters mark dynamic cortical endocytic
    sites, distinct from internal TGN/endosome-associated clathrin. The Discussion
    explicitly cannot distinguish disassembly before budding from a clathrin-bearing
    vesicle or bud leaving the TIRF field. Thus this paper supports the yeast model
    and coat recruitment timing, not direct observation of sealed lumen, membrane
    scission or retained coat on every released vesicle.
  snapshot_sha256: c848e911372b9afb9902e4a74e3cb3dd66ef90eb5e102024cc95fff648bb6c21
- evidence_id: clathrin-agent-SL-0319
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0319.json
  locator: id, name, definition, absence of a top-level geneOntologies field, exact
    isA and partOf objects
  accessed_at: '2026-10-21T11:04:40.023475Z'
  support: supports
  summary: Native SL-0319 identifies the generic clathrin-coated vesicle lumen as
    the compartment bounded by its membrane, classifies it under cytoplasmic-vesicle
    lumen and names the generic clathrin-coated vesicle as its partOf host. It has
    no direct geneOntologies field in this response. The local parent is retained
    as a broader local structure, not misidentified as the endocytic-specific GO:0106176.
  snapshot_sha256: 60adcc470cf8170aeb6ca0842437084ca80cb1a3e5fbd7c87e7a4b3a735d0e4e
- evidence_id: clathrin-agent-kaksonen2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2005.09.024
  locator: Exact bibliography and complete native abstract
  accessed_at: '2026-10-21T11:04:40.023205Z'
  support: partial
  summary: Native MED identifies Kaksonen, Toret and Drubin2005, PMID16239147, DOI10.1016/j.cell.2005.09.024.
    The complete abstract describes mutant/live-imaging analysis and modules for coat
    formation, invagination, actin assembly and scission. It explicitly finds clathrin
    facilitates initiation but is not needed for membrane invagination or vesicle
    formation in the studied yeast system. This is abstract-level evidence, not a
    Methods or figure audit.
  snapshot_sha256: b21f04a2ca620468ebafa02936207fe7e04553d44f862f3f18d72a85b6c4aba2
- evidence_id: clathrin-agent-kaksonen2005-api
  kind: authority
  reference: https://api.elsevier.com/content/article/PII:S0092867405009785?httpAccept=text/xml
  locator: Complete1937-byte API response; coredata and no article body
  accessed_at: '2026-10-21T11:05:34.914917Z'
  support: context_only
  summary: The public Elsevier article API returned HTTP200 XML with bibliographic
    coredata only; it contained no article body. Full-text-retrieval in the XML root
    name is not evidence that full text was obtained.
  snapshot_sha256: 53993cd92f3bb1d1dcd4f4f4887c8a8acd6f0e64d35250a3fd23d05fc0dd0f51
- evidence_id: clathrin-agent-kaksonen2005-core
  kind: authority
  reference: https://core.ac.uk/download/pdf/82329151.pdf
  locator: Actual source-access response, not article text
  accessed_at: '2026-10-21T11:04:59.142587Z'
  support: context_only
  summary: This legitimate public full-text route returned HTTP403; no article body
    was read from this response.
  snapshot_sha256: 38e27fd66e47f5347e47c3c9212a49e6a5d401fccbe055531492a18087eb5c8e
- evidence_id: clathrin-agent-kaksonen2005-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0092867405009785
  locator: Actual source-access response, not article text
  accessed_at: '2026-10-21T11:04:59.142998Z'
  support: context_only
  summary: This legitimate public full-text route returned HTTP403; no article body
    was read from this response.
  snapshot_sha256: 2f404f9566166ed7addf3acf1a84c3823e680c96afec905b2082e988e618856e
- evidence_id: clathrin-agent-kaksonen2005-cellpdf
  kind: authority
  reference: https://www.cell.com/article/S0092867405009785/pdf
  locator: Actual source-access response, not article text
  accessed_at: '2026-10-21T11:05:34.915188Z'
  support: context_only
  summary: This legitimate public full-text route returned HTTP403; no article body
    was read from this response.
  snapshot_sha256: fb778dfc2ae275f47682a0f33f6db4981424deaf07c53c01d57dea505437f700
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    --verify
  locator: Exact focused native output
  accessed_at: '2026-10-21T11:06:30.355427Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    --causal-graphs
  locator: Exact focused native output
  accessed_at: '2026-10-21T11:06:30.958418Z'
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
  reference: just validate data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:57:18Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml'
  snapshot_sha256: e834f2f30dec5e17be26fafbcd3b5c64ec5f5be2f8f4c680aa212e26dd45e8ab
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml
    --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_endocytic_vesicle_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:57:19Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_endocytic_vesicle_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch23-20261021-fk4xe2ee/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch23-20261021-fk4xe2ee/clathrin_coated_endocytic_vesicle_membrane-strict.tsv"
  snapshot_sha256: 46fbe4cbbdd233f485624860952bb1d5104baf641bb344dd285a0d654e12ac8b
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/clathrin_coated_endocytic_vesicle_membrane.yaml;
    exact collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T11:08:14Z'
  support: supports
  summary: '9 of9 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
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
  topic: Whole vesicle, lumen, membrane and coat boundaries
  outcome: supported
  target_ids:
  - GO:0030669
  summary: The active GO identities match the maintained target and distinguish the
    whole endocytic vesicle from its bilayer, enclosed volume and external protein
    coat. These endocytic subtypes are not synonyms of all clathrin-coated vesicles
    or coats at TGN/endosomal sites. The generic-lumen local parent remains broader
    than GO:0106176.
  evidence_ids:
  - endocytic-agent-go
  - endocytic-agent-ancestors-0030669
  - clathrin-agent-SL-0319
  - record
  - generic-lumen
  - coat-boundary
- assessment_id: hierarchy
  area: consistency
  topic: Type, physical inclusion and membrane enclosure
  outcome: supported
  target_ids:
  - GO:0030669
  summary: The maintained is_a parents and part_of/has_part statements agree with
    the returned native child relations and definitions. The two lumen parents express
    the independent endocytic and generic-clathrin-coated classifications; the local
    parent resolves to captured maintained bytes. The coat is a named structural part
    rather than lipid material. A membrane bounds a volume/vesicle without becoming
    identical to the cargo.
  evidence_ids:
  - endocytic-agent-go
  - endocytic-agent-ancestors-0030669
  - clathrin-agent-SL-0319
  - record
  - generic-lumen
  - coat-boundary
- assessment_id: composition
  area: grounding
  topic: Material identity and component responsibility
  outcome: supported
  target_ids:
  - GO:0030669
  summary: The sole direct component is collective lipid-bilayer material. Its REVIEWED_LABEL_ONLY
    rationale correctly avoids using whole-membrane GO:0030669 as a chemical lipid
    identity. ESSENTIAL denotes the constitutive bilayer at this collective level;
    it asserts neither a specific lipid species nor universal clathrin necessity for
    membrane formation. The protein coat remains a separately named has_part structure.
  evidence_ids:
  - endocytic-agent-go
  - record
  - policy
  - coat-boundary
  - clathrin-agent-kaksonen2005-meta
- assessment_id: taxon-example
  area: scope
  topic: Yeast model context and observation limits
  outcome: supported
  target_ids:
  - GO:0030669
  summary: The taxon/name and S. cerevisiae experiment are verified. The maintained
    notes describe cortical clathrin/adaptor recruitment and an endocytic-site model.
    COMMON is qualitative occurrence context, not a measured population percentage.
    Newpher directly supports site-associated recruitment dynamics; it does not directly
    resolve the coat-retention/scission transition or image a sealed lumen. The lumen
    wording about dynamics marking formation is interpreted as this model context,
    not a claim that the paper measured lumen closure.
  evidence_ids:
  - clathrin-agent-tax4932
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - root23-sources-newpher2005-duke
  - record
- assessment_id: direct-lumen-observation
  area: evidence
  topic: Sealed-vesicle transition is not directly resolved
  outcome: unknown
  target_ids:
  - GO:0030669
  summary: The source cannot discriminate clathrin disassembly before budding from
    movement of a clathrin-bearing vesicle or bud out of the TIRF field. Direct observation
    of a sealed, still-coated yeast carrier and its lumen is therefore not established
    by Newpher2005. This limitation does not refute the generic native topology and
    is not filled by treating fluorescent puncta as resolved vesicles.
  evidence_ids:
  - root23-sources-newpher2005-duke
  - endocytic-agent-go
- assessment_id: graph
  area: graph
  topic: Bounded topology and endocytic participation
  outcome: supported
  target_ids:
  - GO:0030669
  summary: Every maintained graph edge was read. Coat/membrane parthood, bilayer enclosure
    and lumen inclusion are supported by the native structural definitions and typed
    relations. Where present, participation in clathrin-dependent endocytosis follows
    the exact process definition. All graphs remain NONMECHANISTIC and assert no complete
    adaptor-assembly, cargo-selection or actin-scission sequence. The membrane component_ref
    is a link to the collective constituent, not a chemical grounding of GO:0030669.
  evidence_ids:
  - endocytic-agent-go
  - record
  - root23-sources-newpher2005-duke
  - clathrin-agent-kaksonen2005-meta
- assessment_id: provenance
  area: provenance
  topic: Accurate bibliographic identities and source scope
  outcome: supported
  target_ids:
  - GO:0030669
  summary: The actual retrieved sources match their declared URLs, hashes and access
    times. Primary PDF text was inspected only at the named sections; captions do
    not constitute image-pixel reanalysis. The native identifiers establish structure/type
    identity independently of experiment-specific recruitment and necessity claims.
    No verbatim snippet, image provenance or historical-source-read certification
    is added.
  evidence_ids:
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - root23-sources-newpher2005-duke
  - endocytic-agent-go
  - clathrin-agent-kaksonen2005-meta
- assessment_id: completeness
  area: completeness
  topic: Whole-target review with bounded neighboring inspection
  outcome: supported
  target_ids:
  - GO:0030669
  summary: The full target record, two sibling targets and generic-lumen parent were
    read. Other named neighbor records were inspected only at the declared boundary/component
    fields; their separate scientific completeness is not claimed. Optional molecular
    inventories, exact dimensions, images, traits and expression modules are not required
    for these topological records.
  evidence_ids:
  - record
  - policy
  - neighbor-clathrin_coated_endocytic_vesicle
  - neighbor-clathrin_coated_endocytic_vesicle_lumen
  - generic-lumen
  - neighbor-clathrin_coated_vesicle
  - neighbor-clathrin_coated_vesicle_membrane
  - coat-boundary
  - local-search
  - endocytic-agent-go
  - endocytic-agent-ancestors-0030669
  - clathrin-agent-tax4932
  - clathrin-agent-doi-10.1016_j.devcel.2005.04.014
  - root23-sources-newpher2005-duke
  - clathrin-agent-SL-0319
  - clathrin-agent-kaksonen2005-meta
  - clathrin-agent-kaksonen2005-api
  - clathrin-agent-kaksonen2005-core
  - clathrin-agent-kaksonen2005-publisher
  - clathrin-agent-kaksonen2005-cellpdf
findings: []
actions: []
limitations:
- Newpher2005 directly supports yeast cortical recruitment and endocytic-site dynamics,
  but explicitly leaves clathrin disassembly versus coated-vesicle departure unresolved.
  No direct sealed-lumen, scission or universal coat-retention assay is claimed.
- Kaksonen2005 was read through its complete native abstract and metadata only. Public
  publisher/repository routes returned403, while the HTTP200 API returned bibliographic
  coredata without article text. No body or figure read is claimed.
- The qualitative COMMON scope is not a numerical prevalence measurement across strains
  or growth conditions. No exhaustive molecular inventory, lipid composition or individual
  formation necessity is established.
- Figure pixels, supplementary movies and raw microscopy were not reanalysed. Historical
  curator searches and independent historical authorship are not certified.
- Root attaches the completed fresh-base global gates only at finalization; this temporary
  draft records actual focused native checks and the exact target resolver slice.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized a review for every uncovered target, including a
  target without findings. Only root may finalize or save the bundle.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
