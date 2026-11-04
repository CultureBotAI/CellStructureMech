# Source-backed review of ammonium transmembrane transporter complex

- Review: 20261022T043541Z-ammonium-transmembrane-transporter-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:15:13Z
- Finished UTC: 2026-10-22T04:35:41Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor correction clarifies NH3 pore conduction versus net ammonium uptake. Exact ontology/family identity, trimeric structural example and native protein references are supported.

## Scope And Provenance

Exactly one complete target; no neighboring scientific-record verdict is imported. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch44 fixed strict path order, index 6; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0110067 | data/structures/other/ammonium_transmembrane_transporter_complex.yaml | maintained | ammonium transmembrane transporter complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0110067 | Focused validator passed. |
| Focused native strict | passed | True | GO:0110067 | Focused validator passed. |
| Focused native proteins | passed | True | GO:0110067 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | GO:0110067 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:0110067 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0110067 | 9 of 11 collected target identifiers returned OK. PDB:1U7G: SKIPPED; Native PDB entry, assembly and polymer entity verify engineered E.coli AmtB S68F/P126S/L255K trimer and exact accession mapping. Depositor1.35Angstrom versus combined1.4Angstrom values remain distinguished.; PMID:15361618: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0110067 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0110067 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0110067 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0110067 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0110067 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact ontology identity and hierarchy

identity: supported. Targets: GO:0110067.

The exact generic complex, narrow AMT1 synonym, transmembrane parent and capable-of function/process relations agree with native GO. Amt-family molecular grounding is distinguished from the assembled complex.

### Exact family and example stoichiometry

grounding: supported. Targets: GO:0110067.

The Amt-family constituent excludes Rh as claimed. Three copies are explicitly confined to the E. coli PDB1U7G assembly. The reviewed P69681 example and SIFTS mapping match; engineered structural provenance is not silently treated as an unmodified in-cell assembly assay.

### Formation necessity remains unknown

grounding: unknown. Targets: GO:0110067.

The existing UNKNOWN essentiality is appropriate. A mature homotrimer and transport function do not independently establish the formation requirement of a particular subunit mutation or a temporal assembly sequence.

### Ontology activity versus physical permeating species

evidence: supported. Targets: GO:0110067.

The generic ammonium-transport ontology labels and energy-independent channel description have native authority support. The 2004 experiment specifically interpreted neutral NH3 conduction, and later work supports separate NH3/H transfer with net electrogenicity. No contradiction is inferred merely from charge transport or the presence of a proton pathway.

### Per-pore chemical species precision

graph: concern. Targets: GO:0110067.

Homotrimerization and one channel per AmtB subunit are supported as a coarse assembly/function model. The hydrophobic-pore description and its Khademi source note should distinguish NH3 conduction from broader net ammonium uptake instead of the ambiguous ammonia/ammonium formulation. The ontology node itself is retained.

### Species and engineered structure boundaries

scope: supported. Targets: GO:0110067.

The E. coli canonical example is correct, while K-12 labels belong to the reviewed reference accession. The PDB genetically engineered sequence and explicit example-level count are preserved. No broad taxonomic occurrence percentage is asserted.

### Whole record and bounded source access

completeness: supported. Targets: GO:0110067.

All target fields, current graph, evidence placements and history were read. There are no record images, verbatim snippets or open grounding tasks. No additional Rh or regulatory GlnK constituent is forced into the example homotrimer. The primary reading scope is the retained body excerpts and independently read later primary sections, not an assertion of complete supplement access.

## Findings

### F1: Distinguish pore-conducted NH3 from net ammonium transport

minor / open / confirmed; issue key: amtb-hydrophobic-pore-species.

The mechanistic edge says the hydrophobic pore conducts ammonia/ammonium and attributes that combined wording to Khademi2004. The inspected original explicitly distinguishes NH4 recruitment from neutral NH3 passage through that pore. Later electrogenic evidence also separates the NH3 route from proton transfer. The broad GO ammonium-channel identity remains valid.

## Recommended Actions And Acceptance Checks

### A1

Specify neutral NH3 passage in the hydrophobic pore when citing Khademi2004, and distinguish recruitment/net NH4 transport from pore-permeating species. If adding the later proton pathway, cite its own tested mechanism and preserve the no-PMF-symport qualification.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/ammonium_transmembrane_transporter_complex.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | Protein-family identity is distinct from an assembled complex. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic or transport function. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| micro44-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990281,GO:0042910,GO:0140330,GO:0110067,GO:1902495,GO:0008519,GO:0072488; Complete GO0110067/1902495/0008519/0072488 definitions, synonyms and typed child relations; no relation inferred from an untyped ancestor list. | supports | GO0110067 exact identity, narrow AMT1 synonym and transmembrane-transporter parent are retained. GO0008519 lists the capable_of child GO0110067; GO0072488 lists capable_of_part_of. The broad ontology channel terminology does not by itself distinguish NH3 from NH4 in a specified physical pore. |
| micro44-ipr-IPR001905 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001905/; Complete metadata identity/type/name/description/hierarchy/member databases and literature identities. | supports | IPR001905 is the Amt ammonium-transporter family and explicitly excludes Rh. Current description distinguishes NH4 sequestration/deprotonation from separate neutral NH3 and proton transfer; this is family authority, not a direct experimental assay. |
| micro44-pmid15361618 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15361618+AND+SRC%3AMED; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED15361618: Mechanism of ammonia transport by Amt/MEP/Rh: structure of AmtB at 1.35 A. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro44-up-P69681 | https://rest.uniprot.org/uniprotkb/P69681.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full FUNCTION/SUBUNIT comments and ComplexPortal cross-references also read. | supports | P69681 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['amtB']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. FUNCTION/SUBUNIT qualifiers and exact ComplexPortal cross-references were checked; probable/inferred assertions remain distinguished. |
| micro44-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 562 identifies Escherichia coli at rank species; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro44-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 83333 identifies Escherichia coli K-12 at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro44-pdb1U7G | https://data.rcsb.org/rest/v1/core/entry/1U7G; Entry identity/exptl, rcsb_primary_citation and rcsb_entry_info resolution fields. | supports | 1U7G is the Khademi2004 E. coli AmtB X-ray entry with matching DOI/PMID. Depositor-assigned high resolution is 1.35 A; current combined resolution is 1.4 A. This difference is not treated as a false paper title. |
| micro44-pdb1U7G-assembly1 | https://data.rcsb.org/rest/v1/core/assembly/1U7G/1; pdbx_struct_assembly; rcsb_assembly_info protein/entity counts and homomeric composition. | supports | Biological assembly1 is an author/software-defined homotrimer with three protein copies. Deposited mature architecture is not a timed assembly pathway or a depletion-based necessity test. |
| micro44-pdb1U7G-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/1U7G/1; rcsb_polymer_entity; rcsb_polymer_entity_container_identifiers/reference_sequence_identifiers; source/host organism and entity_poly fields. | supports | Entity1 maps to P69681 by SIFTS and originates from E. coli; it is genetically engineered with listed S68F/P126S/L255K changes and selenomethionine. The structure-source taxon is562 and the native UniProt reference is K-12/83333; these are compatible but distinct levels of provenance. |
| micro44-khademi2004-browser | https://www.researchgate.net/publication/8352229_Mechanism_of_Ammonia_Transport_by_AmtMEPRh_Structure_of_AmtB_at_135_A; Browser-extracted representation, not native HTTP200: retained lines78–790, printed pp1587–1589 including Introduction, Structure Determination, A Trimer of Three Channels and topology section. No figures pixels or supplementary methods. | supports | The author-uploaded primary text supports a trimer with one channel per AmtB subunit, cleaved signal sequences and the 1.35-A E. coli structure. It distinguishes NH4 recruitment from NH3 conduction. |
| micro44-khademi2004-browser2 | https://www.researchgate.net/publication/8352229_Mechanism_of_Ammonia_Transport_by_AmtMEPRh_Structure_of_AmtB_at_135_A; Browser-extracted primary text, no native HTTP status: returned lines1486–2452, printed pp1591–1593; proteoliposome conductance, water controls, recruitment/filter mechanism, pH discussion and initial transmembrane-potential discussion. Fig4/5 captions read; terminal electrogenic paragraph is incomplete. | supports | The primary study measures intravesicular pH changes after ammonium addition and interprets them as neutral NH3 conduction; its hydrophobic-channel mechanism excludes the proton from that pore. It acknowledges family-level electrogenic observations not fully explained by the 2004 model. |
| micro44-williamson2020-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7447429/fullTextXML; Genuine primary XML; complete s2-1 and s2-4 direct text, s2-8 and s2-9 including Fig6/7 captions, Methods s3-3/s3-4/s3-5; no raw figure pixels or supplementary data. Other mechanistic sections are not certified. | supports | Later primary work distinguishes electrogenic net NH4 transport from NH3 passage through the hydrophobic route and separate proton transfer. The same paper explicitly reports no PMF-driven H-dependent symport under its tested conditions; electrogenicity alone does not refute the record’s energy-independent wording. |
| micro44-pmid32662768 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A32662768%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED32662768: A two-lane mechanism for selective biological ammonium transport. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro44-khademi2004-publisher | https://www.science.org/doi/10.1126/science.1101952; Complete retained response/access diagnostic; no scientific main-body content inferred. | context_only | Recorded status 403: HTTP403 publisher denial. Separately retained browser primary excerpts provide the stated body scope. |
| schema-result | just validate data/structures/other/ammonium_transmembrane_transporter_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/ammonium_transmembrane_transporter_complex.yaml |
| strict-result | just validate-strict data/structures/other/ammonium_transmembrane_transporter_complex.yaml --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ammonium_transmembrane_transporter_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/ammonium_transmembrane_transporter_complex.yaml --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ammonium_transmembrane_transporter_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch44-20261022-b975f18l/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch44-20261022-b975f18l/ammonium_transmembrane_transporter_complex-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/ammonium_transmembrane_transporter_complex.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ammonium_transmembrane_transporter_complex.yaml; Complete read-only focused native graphs log | supports | data/structures/other/ammonium_transmembrane_transporter_complex.yaml  (GO:0110067)<br>  amtb_channel_function	ammonium_transporter	COVERED	-&gt;ammonium_transporter (UniProtKB:P69681)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/ammonium_transmembrane_transporter_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 11 collected target identifiers returned OK. PDB:1U7G: SKIPPED; Native PDB entry, assembly and polymer entity verify engineered E.coli AmtB S68F/P126S/L255K trimer and exact accession mapping. Depositor1.35Angstrom versus combined1.4Angstrom values remain distinguished.; PMID:15361618: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Khademi2004 primary reading is limited to the two retained browser-extracted body ranges; intervening detailed site analysis, the end of the electrogenic discussion and supplementary methods were not fully read. The native publisher returned403.
- No structure-coordinate reanalysis, figure pixels or supplements were inspected. PDB1U7G contains an engineered structural construct and is not an in-cell assembly trajectory.
- Williamson2020 reading is limited to the specified Results/Discussion and Methods sections. Electrogenic activity is not equated with PMF-driven symport; the paper directly distinguishes those concepts.
- The record already preserves UNKNOWN formation necessity; optional GlnK/Rh inventories are not required for this bounded AmtB homotrimer example.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these complex identity, protein family, assembly and enzyme or transport claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T043541Z-ammonium-transmembrane-transporter-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of ammonium transmembrane transporter complex
started_at: '2026-10-22T04:15:13Z'
finished_at: '2026-10-22T04:35:41Z'
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
summary: One minor correction clarifies NH3 pore conduction versus net ammonium uptake.
  Exact ontology/family identity, trimeric structural example and native protein references
  are supported.
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
  - path: data/structures/other/ammonium_transmembrane_transporter_complex.yaml
    sha256: 5817cfb54453674b3d5c595474173ea79cca6f9d88c6ac8ea97f3445e1e775a4
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
- target_id: GO:0110067
  path: data/structures/other/ammonium_transmembrane_transporter_complex.yaml
  label: ammonium transmembrane transporter complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ammonium_transmembrane_transporter_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; no neighboring scientific-record verdict
    is imported. Exact authority, all current component/function/graph/source placements,
    taxonomic scope, formation semantics, history and discussions were reviewed.
  selection: Batch44 fixed strict path order, index 6; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0110067
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0110067
  command: just validate data/structures/other/ammonium_transmembrane_transporter_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0110067
  command: just validate-strict data/structures/other/ammonium_transmembrane_transporter_complex.yaml
    --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ammonium_transmembrane_transporter_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - GO:0110067
  command: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/ammonium_transmembrane_transporter_complex.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-proteins
- check_id: native-graphs
  name: Focused native graphs
  status: passed
  required: true
  target_ids:
  - GO:0110067
  command: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ammonium_transmembrane_transporter_complex.yaml
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
  - GO:0110067
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - micro44-go
  - micro44-ipr-IPR001905
  - micro44-pmid15361618
  - micro44-up-P69681
  - micro44-tax562
  - micro44-tax83333
  - micro44-pdb1U7G
  - micro44-pdb1U7G-assembly1
  - micro44-pdb1U7G-entity1
  - micro44-khademi2004-browser
  - micro44-khademi2004-browser2
  - micro44-williamson2020-xml
  - micro44-pmid32662768
  - micro44-khademi2004-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0110067
  summary: '9 of 11 collected target identifiers returned OK. PDB:1U7G: SKIPPED; Native
    PDB entry, assembly and polymer entity verify engineered E.coli AmtB S68F/P126S/L255K
    trimer and exact accession mapping. Depositor1.35Angstrom versus combined1.4Angstrom
    values remain distinguished.; PMID:15361618: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport
    failure. Identity resolution does not certify every attached biological claim;
    declared abstract/body reading scope remains in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - micro44-pdb1U7G
  - micro44-pdb1U7G-assembly1
  - micro44-pdb1U7G-entity1
  - micro44-pmid15361618
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0110067
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0110067
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0110067
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0110067
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0110067
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
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/ammonium_transmembrane_transporter_complex.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:27:40Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:27:40Z'
  support: context_only
  summary: Protein-family identity is distinct from an assembled complex. ESSENTIAL
    concerns failure of structure formation, not merely loss of catalytic or transport
    function.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:27:40Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: micro44-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990281,GO:0042910,GO:0140330,GO:0110067,GO:1902495,GO:0008519,GO:0072488
  locator: Complete GO0110067/1902495/0008519/0072488 definitions, synonyms and typed
    child relations; no relation inferred from an untyped ancestor list.
  accessed_at: '2026-10-22T04:22:33.314420Z'
  support: supports
  summary: GO0110067 exact identity, narrow AMT1 synonym and transmembrane-transporter
    parent are retained. GO0008519 lists the capable_of child GO0110067; GO0072488
    lists capable_of_part_of. The broad ontology channel terminology does not by itself
    distinguish NH3 from NH4 in a specified physical pore.
  snapshot_sha256: 84212830407680914329f5be4038a3c5dd3494912885c4100404cd02f3c97d7b
- evidence_id: micro44-ipr-IPR001905
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001905/
  locator: Complete metadata identity/type/name/description/hierarchy/member databases
    and literature identities.
  accessed_at: '2026-10-22T04:22:33.314917Z'
  support: supports
  summary: IPR001905 is the Amt ammonium-transporter family and explicitly excludes
    Rh. Current description distinguishes NH4 sequestration/deprotonation from separate
    neutral NH3 and proton transfer; this is family authority, not a direct experimental
    assay.
  snapshot_sha256: 631763d05a01a1901dee5ddad54ec5c232d8bb79783cbd2be0396d659eefcbca
- evidence_id: micro44-pmid15361618
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15361618+AND+SRC%3AMED
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:22:34.880627Z'
  support: supports
  summary: 'Unique MED15361618: Mechanism of ammonia transport by Amt/MEP/Rh: structure
    of AmtB at 1.35 A. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: c951ca92f151b955dbd0934c2d9f66af48fe724a61f2e5a6aa253322387581b4
- evidence_id: micro44-up-P69681
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P69681.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references. Full
    FUNCTION/SUBUNIT comments and ComplexPortal cross-references also read.
  accessed_at: '2026-10-22T04:22:34.366533Z'
  support: supports
  summary: P69681 is UniProtKB reviewed (Swiss-Prot), taxon 83333, genes ['amtB'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge. FUNCTION/SUBUNIT qualifiers and
    exact ComplexPortal cross-references were checked; probable/inferred assertions
    remain distinguished.
  snapshot_sha256: a9d67c5ee128ed57357b64c117f1c26b9e23566a21ecff68d86e82b07cbd582a
- evidence_id: micro44-tax562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:22:33.314845Z'
  support: supports
  summary: ENA taxId 562 identifies Escherichia coli at rank species; aliases and
    lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: micro44-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:09:06.395271Z'
  support: supports
  summary: ENA taxId 83333 identifies Escherichia coli K-12 at rank strain; aliases
    and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro44-pdb1U7G
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1U7G
  locator: Entry identity/exptl, rcsb_primary_citation and rcsb_entry_info resolution
    fields.
  accessed_at: '2026-10-22T04:22:35.089069Z'
  support: supports
  summary: 1U7G is the Khademi2004 E. coli AmtB X-ray entry with matching DOI/PMID.
    Depositor-assigned high resolution is 1.35 A; current combined resolution is 1.4
    A. This difference is not treated as a false paper title.
  snapshot_sha256: 984aa5fc5aae9ae5f65f5a40d1c4870b558888a5fc563c9d393da28309516179
- evidence_id: micro44-pdb1U7G-assembly1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/1U7G/1
  locator: pdbx_struct_assembly; rcsb_assembly_info protein/entity counts and homomeric
    composition.
  accessed_at: '2026-10-22T04:22:35.168413Z'
  support: supports
  summary: Biological assembly1 is an author/software-defined homotrimer with three
    protein copies. Deposited mature architecture is not a timed assembly pathway
    or a depletion-based necessity test.
  snapshot_sha256: 6900516a2287aeaae2cb21c689e4ef1ded064f62d9d0f9bee563f120a4b0d681
- evidence_id: micro44-pdb1U7G-entity1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1U7G/1
  locator: rcsb_polymer_entity; rcsb_polymer_entity_container_identifiers/reference_sequence_identifiers;
    source/host organism and entity_poly fields.
  accessed_at: '2026-10-22T04:22:35.248447Z'
  support: supports
  summary: Entity1 maps to P69681 by SIFTS and originates from E. coli; it is genetically
    engineered with listed S68F/P126S/L255K changes and selenomethionine. The structure-source
    taxon is562 and the native UniProt reference is K-12/83333; these are compatible
    but distinct levels of provenance.
  snapshot_sha256: 8a62d53df2c755ec5068c609219d567a54189b03d532e2f84f56f4cd0c5a8000
- evidence_id: micro44-khademi2004-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/8352229_Mechanism_of_Ammonia_Transport_by_AmtMEPRh_Structure_of_AmtB_at_135_A
  locator: 'Browser-extracted representation, not native HTTP200: retained lines78–790,
    printed pp1587–1589 including Introduction, Structure Determination, A Trimer
    of Three Channels and topology section. No figures pixels or supplementary methods.'
  accessed_at: '2026-10-22T04:24:29.707880Z'
  support: supports
  summary: The author-uploaded primary text supports a trimer with one channel per
    AmtB subunit, cleaved signal sequences and the 1.35-A E. coli structure. It distinguishes
    NH4 recruitment from NH3 conduction.
  snapshot_sha256: 76e42fd0ca2049a760c953b92fa6ffe077725e9cdf4bab1dfad849459b278672
- evidence_id: micro44-khademi2004-browser2
  kind: primary_source
  reference: https://www.researchgate.net/publication/8352229_Mechanism_of_Ammonia_Transport_by_AmtMEPRh_Structure_of_AmtB_at_135_A
  locator: 'Browser-extracted primary text, no native HTTP status: returned lines1486–2452,
    printed pp1591–1593; proteoliposome conductance, water controls, recruitment/filter
    mechanism, pH discussion and initial transmembrane-potential discussion. Fig4/5
    captions read; terminal electrogenic paragraph is incomplete.'
  accessed_at: '2026-10-22T04:24:41.078796Z'
  support: supports
  summary: The primary study measures intravesicular pH changes after ammonium addition
    and interprets them as neutral NH3 conduction; its hydrophobic-channel mechanism
    excludes the proton from that pore. It acknowledges family-level electrogenic
    observations not fully explained by the 2004 model.
  snapshot_sha256: b291ed3682005b5087630f533ae3df13f2c4b26968b108ac08907cac30d9375c
- evidence_id: micro44-williamson2020-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7447429/fullTextXML
  locator: Genuine primary XML; complete s2-1 and s2-4 direct text, s2-8 and s2-9
    including Fig6/7 captions, Methods s3-3/s3-4/s3-5; no raw figure pixels or supplementary
    data. Other mechanistic sections are not certified.
  accessed_at: '2026-10-22T04:24:11.126537Z'
  support: supports
  summary: Later primary work distinguishes electrogenic net NH4 transport from NH3
    passage through the hydrophobic route and separate proton transfer. The same paper
    explicitly reports no PMF-driven H-dependent symport under its tested conditions;
    electrogenicity alone does not refute the record’s energy-independent wording.
  snapshot_sha256: 8af39dd63100a225b0f142be83eddb2442d5516cab2f8448aa3f3d68338145ae
- evidence_id: micro44-pmid32662768
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A32662768%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:23:28.685126Z'
  support: supports
  summary: 'Unique MED32662768: A two-lane mechanism for selective biological ammonium
    transport. Authors/year/DOI and the complete native abstract were inspected. This
    row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: f4710132c01a890532f6ec195c115b88f5f3db27c55e49471d8d2df75c191a5a
- evidence_id: micro44-khademi2004-publisher
  kind: authority
  reference: https://www.science.org/doi/10.1126/science.1101952
  locator: Complete retained response/access diagnostic; no scientific main-body content
    inferred.
  accessed_at: '2026-10-22T04:23:28.684984Z'
  support: context_only
  summary: 'Recorded status 403: HTTP403 publisher denial. Separately retained browser
    primary excerpts provide the stated body scope.'
  snapshot_sha256: 974e58b52a080efd44945487aa7e636244f3936fbc06031723a2dc89261cabb7
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/ammonium_transmembrane_transporter_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:15:14Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/ammonium_transmembrane_transporter_complex.yaml'
  snapshot_sha256: fc89fa6dec9eb54e2009df815bb86604fd1533fb5480d5abc7cc3f1d248f8778
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/ammonium_transmembrane_transporter_complex.yaml
    --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ammonium_transmembrane_transporter_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:15:16Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/ammonium_transmembrane_transporter_complex.yaml\
    \ --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ammonium_transmembrane_transporter_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch44-20261022-b975f18l/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch44-20261022-b975f18l/ammonium_transmembrane_transporter_complex-strict.tsv"
  snapshot_sha256: 9733b0b1dff2816c444ce298c35d4313b2c090ad6043ab174cf3b6fd46cd5def
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/ammonium_transmembrane_transporter_complex.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T04:23:18.976496Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ammonium_transmembrane_transporter_complex.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T04:23:19.601172Z'
  support: supports
  summary: "data/structures/other/ammonium_transmembrane_transporter_complex.yaml\
    \  (GO:0110067)\n  amtb_channel_function\tammonium_transporter\tCOVERED\t->ammonium_transporter\
    \ (UniProtKB:P69681)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED\
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
  snapshot_sha256: 1b157a19976129a4951b5bb9dfad86d94c8bbf91d8e5453ef46148ed2e640e84
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/ammonium_transmembrane_transporter_complex.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '9 of 11 collected target identifiers returned OK. PDB:1U7G: SKIPPED; Native
    PDB entry, assembly and polymer entity verify engineered E.coli AmtB S68F/P126S/L255K
    trimer and exact accession mapping. Depositor1.35Angstrom versus combined1.4Angstrom
    values remain distinguished.; PMID:15361618: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport
    failure. Identity resolution does not certify every attached biological claim;
    declared abstract/body reading scope remains in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
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
  topic: Exact ontology identity and hierarchy
  outcome: supported
  target_ids:
  - GO:0110067
  summary: The exact generic complex, narrow AMT1 synonym, transmembrane parent and
    capable-of function/process relations agree with native GO. Amt-family molecular
    grounding is distinguished from the assembled complex.
  evidence_ids:
  - record
  - micro44-go
  - micro44-ipr-IPR001905
- assessment_id: composition
  area: grounding
  topic: Exact family and example stoichiometry
  outcome: supported
  target_ids:
  - GO:0110067
  summary: The Amt-family constituent excludes Rh as claimed. Three copies are explicitly
    confined to the E. coli PDB1U7G assembly. The reviewed P69681 example and SIFTS
    mapping match; engineered structural provenance is not silently treated as an
    unmodified in-cell assembly assay.
  evidence_ids:
  - record
  - micro44-ipr-IPR001905
  - micro44-pdb1U7G
  - micro44-pdb1U7G-assembly1
  - micro44-pdb1U7G-entity1
  - micro44-up-P69681
- assessment_id: necessity
  area: grounding
  topic: Formation necessity remains unknown
  outcome: unknown
  target_ids:
  - GO:0110067
  summary: The existing UNKNOWN essentiality is appropriate. A mature homotrimer and
    transport function do not independently establish the formation requirement of
    a particular subunit mutation or a temporal assembly sequence.
  evidence_ids:
  - record
  - schema
  - micro44-pdb1U7G-assembly1
  - micro44-khademi2004-browser
- assessment_id: function
  area: evidence
  topic: Ontology activity versus physical permeating species
  outcome: supported
  target_ids:
  - GO:0110067
  summary: The generic ammonium-transport ontology labels and energy-independent channel
    description have native authority support. The 2004 experiment specifically interpreted
    neutral NH3 conduction, and later work supports separate NH3/H transfer with net
    electrogenicity. No contradiction is inferred merely from charge transport or
    the presence of a proton pathway.
  evidence_ids:
  - record
  - micro44-go
  - micro44-pmid15361618
  - micro44-khademi2004-browser2
  - micro44-williamson2020-xml
  - micro44-ipr-IPR001905
  - micro44-up-P69681
- assessment_id: graph
  area: graph
  topic: Per-pore chemical species precision
  outcome: concern
  target_ids:
  - GO:0110067
  summary: Homotrimerization and one channel per AmtB subunit are supported as a coarse
    assembly/function model. The hydrophobic-pore description and its Khademi source
    note should distinguish NH3 conduction from broader net ammonium uptake instead
    of the ambiguous ammonia/ammonium formulation. The ontology node itself is retained.
  evidence_ids:
  - record
  - micro44-pdb1U7G-assembly1
  - micro44-khademi2004-browser
  - micro44-khademi2004-browser2
  - micro44-williamson2020-xml
  - micro44-go
- assessment_id: scope
  area: scope
  topic: Species and engineered structure boundaries
  outcome: supported
  target_ids:
  - GO:0110067
  summary: The E. coli canonical example is correct, while K-12 labels belong to the
    reviewed reference accession. The PDB genetically engineered sequence and explicit
    example-level count are preserved. No broad taxonomic occurrence percentage is
    asserted.
  evidence_ids:
  - record
  - micro44-pdb1U7G
  - micro44-pdb1U7G-entity1
  - micro44-tax562
  - micro44-tax83333
- assessment_id: coverage
  area: completeness
  topic: Whole record and bounded source access
  outcome: supported
  target_ids:
  - GO:0110067
  summary: All target fields, current graph, evidence placements and history were
    read. There are no record images, verbatim snippets or open grounding tasks. No
    additional Rh or regulatory GlnK constituent is forced into the example homotrimer.
    The primary reading scope is the retained body excerpts and independently read
    later primary sections, not an assertion of complete supplement access.
  evidence_ids:
  - record
  - micro44-go
  - micro44-ipr-IPR001905
  - micro44-khademi2004-browser
  - micro44-khademi2004-browser2
  - micro44-williamson2020-xml
findings:
- finding_id: F1
  issue_key: amtb-hydrophobic-pore-species
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish pore-conducted NH3 from net ammonium transport
  description: The mechanistic edge says the hydrophobic pore conducts ammonia/ammonium
    and attributes that combined wording to Khademi2004. The inspected original explicitly
    distinguishes NH4 recruitment from neutral NH3 passage through that pore. Later
    electrogenic evidence also separates the NH3 route from proton transfer. The broad
    GO ammonium-channel identity remains valid.
  target_ids:
  - GO:0110067
  field_paths:
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[2].notes
  evidence_ids:
  - record
  - micro44-pmid15361618
  - micro44-khademi2004-browser2
  - micro44-williamson2020-xml
  - micro44-go
  - micro44-ipr-IPR001905
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ammonium_transmembrane_transporter_complex.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: The coarse transporter identity, direction, topology and net
    uptake function are correct. This is a localized mechanistic chemical-species
    ambiguity and source-precision correction, not rejection of ammonium uptake or
    energy independence.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0110067
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ammonium_transmembrane_transporter_complex.yaml
    role: maintained scientific record
  description: Specify neutral NH3 passage in the hydrophobic pore when citing Khademi2004,
    and distinguish recruitment/net NH4 transport from pore-permeating species. If
    adding the later proton pathway, cite its own tested mechanism and preserve the
    no-PMF-symport qualification.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
limitations:
- Khademi2004 primary reading is limited to the two retained browser-extracted body
  ranges; intervening detailed site analysis, the end of the electrogenic discussion
  and supplementary methods were not fully read. The native publisher returned403.
- No structure-coordinate reanalysis, figure pixels or supplements were inspected.
  PDB1U7G contains an engineered structural construct and is not an in-cell assembly
  trajectory.
- Williamson2020 reading is limited to the specified Results/Discussion and Methods
  sections. Electrogenic activity is not equated with PMF-driven symport; the paper
  directly distinguishes those concepts.
- The record already preserves UNKNOWN formation necessity; optional GlnK/Rh inventories
  are not required for this bounded AmtB homotrimer example.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these complex identity, protein family, assembly
  and enzyme or transport claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
