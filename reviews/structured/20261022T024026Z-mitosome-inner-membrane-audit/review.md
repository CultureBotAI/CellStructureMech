# Scientific review of mitosome inner membrane

- Review: 20261022T024026Z-mitosome-inner-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:27:18Z
- Finished UTC: 2026-10-22T02:40:26Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact mitosome inner membrane identity and bounded topology are supported. One minor finding corrects the DOI12922 bibliographic title; source-access and occurrence-frequency limits are retained.

## Scope And Provenance

Entire single maintained record, exact native authorities, source claim boundaries, component grounding and every topology edge at frozen f97b1abe.

Selection: Batch34 fixed strict path-order selection; one maintained target only. Initial inspect/schema/strict0 completed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:mitosome_inner_membrane | data/structures/membrane_organelle/mitosome_inner_membrane.yaml | maintained | mitosome inner membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:mitosome_inner_membrane | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:mitosome_inner_membrane | Focused validator passed. |
| Native focused graph protein-reference check | passed | True | cellstructuremech:mitosome_inner_membrane | Native check passed; no GENE_OR_PROTEIN actor is asserted. Topology independently assessed. |
| Individual protein verification applicability | not_applicable | False | cellstructuremech:mitosome_inner_membrane | Full target contains no individual gene symbol, protein example or UniProt accession. No optional protein inventory is mandated. |
| Expression-module applicability | not_applicable | False | cellstructuremech:mitosome_inner_membrane | No expression-module, gene-regulon or transcriptomic claim; anatomical topology does not require an expression-module lookup. |
| Claim-level scientific review | passed | True | cellstructuremech:mitosome_inner_membrane | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | cellstructuremech:mitosome_inner_membrane | 9 of 13 collected target identifiers returned OK. cellstructuremech:mitosome_envelope: SKIPPED; Exact local identifier uniquely resolves to data/structures/membrane_organelle/mitosome_envelope.yaml at frozen SHA256 762b8bad522664b480655908ccd92a258624f836a99d3e78232fe1e30aea8fc9. The maintained identity, definition and compartment boundary were independently read and match the cited native UniProt location SL0438. Local-reference validity is separate from any GO-first curation finding; no scientific identifier is renamed.; cellstructuremech:mitosome_inner_membrane: SKIPPED; Exact local identifier uniquely resolves to data/structures/membrane_organelle/mitosome_inner_membrane.yaml at frozen SHA256 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35. The maintained identity, definition and compartment boundary were independently read and match the cited native UniProt location SL0439. Local-reference validity is separate from any GO-first curation finding; no scientific identifier is renamed.; cellstructuremech:mitosome_intermembrane_space: SKIPPED; Exact local identifier uniquely resolves to data/structures/membrane_organelle/mitosome_intermembrane_space.yaml at frozen SHA256 c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95. The maintained identity, definition and compartment boundary were independently read and match the cited native UniProt location SL0440. Local-reference validity is separate from any GO-first curation finding; no scientific identifier is renamed.; cellstructuremech:mitosome_matrix: SKIPPED; Exact local identifier uniquely resolves to data/structures/membrane_organelle/mitosome_matrix.yaml at frozen SHA256 cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca. The maintained identity, definition and compartment boundary were independently read and match the cited native UniProt location SL0441. Local-reference validity is separate from any GO-first curation finding; no scientific identifier is renamed. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | cellstructuremech:mitosome_inner_membrane | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:mitosome_inner_membrane | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:mitosome_inner_membrane | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:mitosome_inner_membrane | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | cellstructuremech:mitosome_inner_membrane | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact compartment and relationships

identity: supported. Targets: cellstructuremech:mitosome_inner_membrane.

The local identifier and UniProt location represent mitosome inner membrane. Exact definition and synonyms match. GO0031090 is a suitable broader organelle-membrane class by its definition, distinct from envelope parthood. Frozen local boundary references resolve; source-native locations and local structures are not chemical entities.

### Taxonomic identity and qualitative occurrence

scope: supported. Targets: cellstructuremech:mitosome_inner_membrane.

Both native taxa match. Entamoeba organelle occurrence is supported by the original localization abstract and the later primary body. The broader patchy low-oxygen eukaryotic context is supported qualitatively by the additional evolutionary review.

### Original citation and frequency limits

evidence: unknown. Targets: cellstructuremech:mitosome_inner_membrane.

The Tovar1999 complete abstract does not establish the specifically attributed double-membrane observation, and the DOI12922 review body was not accessible. No quantitative Eukaryota prevalence or species-wide strain census was performed. These access and measurement gaps are not treated as biological contradictions.

### Label-only lipid constituent

grounding: supported. Targets: cellstructuremech:mitosome_inner_membrane.

The component explicitly denotes the lipid bilayer constituent, retains REVIEWED_LABEL_ONLY and does not ground a lipid class to the whole membrane location. Its positional role is consistent with the native anatomical definitions and nested generic membrane definition. The collective bilayer is constitutive of this membrane class; no individual lipid species or protein formation requirement is asserted.

### Specific molecular requirements remain unestablished

grounding: unknown. Targets: cellstructuremech:mitosome_inner_membrane.

The authority establishes a lipid-bilayer membrane architecture, not a depletion or reconstitution test for particular lipids or proteins. Exact molecular composition, stoichiometry and taxon-specific formation necessity remain unmeasured here; collective class constitution must not be extrapolated to individual essential constituents.

### Complete target topology graph

graph: supported. Targets: cellstructuremech:mitosome_inner_membrane.

All 3 edges in this target are topological and accurately marked NONMECHANISTIC. The inner membrane is part of envelope, encloses matrix and delimits intermembrane space. No molecular import pathway, translocase inventory or assembly mechanism is asserted.

### Exact DOI12922 article identity

evidence: concern. Targets: cellstructuremech:mitosome_inner_membrane.

The target bibliographic note assigns a different title to the resolving DOI. This is a certain bounded provenance error, separate from the supported anatomical identity and qualitative distribution.

### Full bounded record review

completeness: supported. Targets: cellstructuremech:mitosome_inner_membrane.

All target fields, source notes, graph nodes/edges and history were read. The explicit lipid-identity TODO accurately distinguishes the whole-membrane location from a molecular constituent; no exact chemical class was established by the retained sources, so no forced grounding finding is added. No numerical physical property, maintained image, verbatim evidence snippet, individual gene symbol or UniProt protein example is asserted. Historical curation notes are not current absence claims.

## Findings

### F1: Correct the title attached to DOI10.1111/jeu.12922

minor / open / confirmed; issue key: mitosome-inner-membrane-tachezy-title.

The evidence note calls this article Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes. Exact native metadata identifies The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). The DOI is valid; its unread full body is not presumed to lack a mitosome passage.

## Recommended Actions And Acceptance Checks

### A1

Correct the bibliographic title/authorship for the retained DOI. Independently verify or replace its use for broad mitosome distribution without claiming unread full text proves absence.

- Confirm the retained DOI/title/author identity against native metadata.
- Run focused schema, strict and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/mitosome_inner_membrane.yaml; Complete maintained YAML, including all history, graph edges and discussions | context_only | Entire target read without modifying maintained scientific content. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent molecular-building-block description, grounding and essentiality; graph actor/component_ref semantics | context_only | Molecular components and anatomical parts are distinct. Essentiality concerns whether a structure forms without a component, not catalytic function or cell viability. |
| neighbor-mitosome_envelope | data/structures/membrane_organelle/mitosome_envelope.yaml; Frozen identifier, label, definition/source, parent_structures, part_of, has_part and xrefs | context_only | Exact local boundary identity resolved from captured neighbor bytes. No independent scientific endorsement of other neighbor claims. |
| neighbor-mitosome_matrix | data/structures/membrane_organelle/mitosome_matrix.yaml; Frozen identifier, label, definition/source, parent_structures, part_of, has_part and xrefs | context_only | Exact local boundary identity resolved from captured neighbor bytes. No independent scientific endorsement of other neighbor claims. |
| neighbor-mitosome_intermembrane_space | data/structures/membrane_organelle/mitosome_intermembrane_space.yaml; Frozen identifier, label, definition/source, parent_structures, part_of, has_part and xrefs | context_only | Exact local boundary identity resolved from captured neighbor bytes. No independent scientific endorsement of other neighbor claims. |
| mitosome-agent-SL0438 | https://rest.uniprot.org/locations/SL-0438.json; Complete JSON identity, definition, synonyms and nested isA/partOf records; SL0162 membrane definition where present | supports | SL0438 identifies the envelope as inner and outer membranes plus the intermembrane space; partOf points to the mitosome. Native protein statistics are not an inventory or absence argument. |
| mitosome-agent-SL0439 | https://rest.uniprot.org/locations/SL-0439.json; Complete JSON identity, definition, synonyms and nested isA/partOf records; SL0162 membrane definition where present | supports | SL0439 defines the matrix-facing membrane separating matrix from intermembrane space; both listed synonyms match. isA leads through SL0442 to membrane SL0162, and nested partOf to envelope. Native protein statistics are not an inventory or absence argument. |
| mitosome-agent-SL0440 | https://rest.uniprot.org/locations/SL-0440.json; Complete JSON identity, definition, synonyms and nested isA/partOf records; SL0162 membrane definition where present | supports | SL0440 identifies the space between inner and outer membranes, with all three target synonyms and partOf envelope. Native protein statistics are not an inventory or absence argument. |
| mitosome-agent-SL0441 | https://rest.uniprot.org/locations/SL-0441.json; Complete JSON identity, definition, synonyms and nested isA/partOf records; SL0162 membrane definition where present | supports | SL0441 defines the internal space enclosed by the inner membrane, with mitosomal matrix synonym and partOf mitosome. Native protein statistics are not an inventory or absence argument. |
| mitosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0031090%2CGO%3A0043233%2CGO%3A0032047%2CGO%3A0005737; Complete four returned entries; exact definitions, obsolete flags and relevant child relation; no mixed-ancestry inference | supports | The four active native entries identify organelle membrane GO0031090, organelle lumen GO0043233, mitosome GO0032047 and cytoplasm GO0005737. Definitions support the broader anatomical parents; mitosome is a returned part_of child of cytoplasm. Local mitosome subcompartments are resolved separately, not invented as native GO children. |
| mitosome-agent-tax2759 | https://rest.uniprot.org/taxonomy/2759.json; taxonId, scientificName, active, rank and lineage; not taxonId from a different API shape | supports | Eukaryota is active and ranked domain. Taxonomic identity alone does not measure occurrence frequency. |
| mitosome-agent-tax5759 | https://rest.uniprot.org/taxonomy/5759.json; taxonId, scientificName, active, rank and lineage; not taxonId from a different API shape | supports | Entamoeba histolytica is active and ranked species, under the returned Amoebozoa lineage. Taxonomic identity alone does not measure occurrence frequency. |
| mitosome-agent-tovar1999-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1046/j.1365-2958.1999.01414.x&amp;format=json&amp;resultType=core; Complete resultList.result[0] identity and abstractText; primary abstract only | supports | The exact DOI, PMID10361303, title, authors/year and complete abstract match Tovar et al. The abstract localizes native CPN60 to the Entamoeba mitochondrial-remnant organelle and tests N-terminal deletion/replacement targeting. It does not document the specific double-membrane ultrastructural observation attributed to this source in the target. |
| mitosome-agent-tachezy2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/jeu.12922; Complete resultList.result[0] bibliographic identity and abstractText; review abstract only | supports | DOI10.1111/jeu.12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022), PMID35567536. The complete abstract discusses hydrogenosome history, biogenesis, import and metabolism. It does not establish the target-supplied title or independently verify a mitosome-distribution synthesis. |
| mitosome-agent-roger2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/j.cub.2017.09.015%22; Complete native bibliographic result and abstract; supplementary source not originally cited by target | supports | Exact DOI10.1016/j.cub.2017.09.015, PMID29112874, title/authors/year and complete abstract identify the additional secondary review The Origin and Diversification of Mitochondria. |
| mitosome-agent-roger2017-pdf | https://ecsolab.com/assets/pdf/roger_etal_2017.pdf; Printed R1177 introduction, R1184 Diversity opening, R1186 hydrogenosome/mitosome comparison and ISC replacement discussion; Fig5 caption text; no figure-pixel or remaining full-review inspection claimed | supports | The secondary review describes divergent mitochondrion-related organelles in low-oxygen eukaryotes and the repeated evolution of reduced mitosomes. It names Entamoeba and preserves metabolic differences among lineages. This supports a qualitative patchy distribution, not a quantified census or every-species prevalence. |
| mitosome-agent-miichi2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.0907106106&amp;format=json&amp;resultType=core; Complete native result identity and abstractText; supplementary source distinct from the target citation | supports | Additional primary-study identity verified: Mi-ichi et al.2009 DOI10.1073/pnas.0907106106, PMID19995967; complete abstract describes Entamoeba mitosome purification, localization and sulfate activation. |
| mitosome-agent-miichi2009-pmc | https://pmc.ncbi.nlm.nih.gov/articles/2799805/; Complete introductory scientific paragraph; prior same-hash Results sec2-sec6, Discussion sec8, Methods sec10 purification and sec13 immunofluorescence; figures read as captions only, not pixels or supplements | supports | The introduction explicitly summarizes double membranes among shared mitochondrion-related-organelle characteristics and describes Entamoeba mitosomes. The primary purification/localization/biochemical results support Entamoeba organelle occurrence and heterogeneity; they are not used here as a direct ultrastructural reanalysis of Tovar1999 or as a universal protein inventory. |
| access-tovar1999-publisher | https://doi.org/10.1046/j.1365-2958.1999.01414.x; Retained original HTTP403 response, 5681 bytes; no genuine article body | context_only | This prior public route returned a blocked response rather than readable primary text. Only the separately captured complete native abstract is used; original URL, bytes and access time are preserved. |
| access-tovar1999-pdf | https://onlinelibrary.wiley.com/doi/pdf/10.1046/j.1365-2958.1999.01414.x; Retained original HTTP403 response, 5693 bytes; no genuine article body | context_only | This prior public route returned a blocked response rather than readable primary text. Only the separately captured complete native abstract is used; original URL, bytes and access time are preserved. |
| access-tachezy2022-publisher | https://onlinelibrary.wiley.com/doi/10.1111/jeu.12922; Retained original HTTP403 response, 5594 bytes; no genuine article body | context_only | This prior public route returned a blocked response rather than readable primary text. Only the separately captured complete native abstract is used; original URL, bytes and access time are preserved. |
| access-tachezy2022-pdf | https://onlinelibrary.wiley.com/doi/pdf/10.1111/jeu.12922; Retained original HTTP403 response, 5606 bytes; no genuine article body | context_only | This prior public route returned a blocked response rather than readable primary text. Only the separately captured complete native abstract is used; original URL, bytes and access time are preserved. |
| access-tachezy2022-rg-pdf | https://www.researchgate.net/profile/Ivan-Hrdy/publication/360605238_The_hydrogenosome_of_Trichomonas_vaginalis/links/66fa5b6ab753fa724d4ffa69/The-hydrogenosome-of-Trichomonas-vaginalis.pdf; Retained original HTTP403 response, 779 bytes; no genuine article body | context_only | This prior public route returned a blocked response rather than readable primary text. Only the separately captured complete native abstract is used; original URL, bytes and access time are preserved. |
| schema-result | just validate data/structures/membrane_organelle/mitosome_inner_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/mitosome_inner_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/mitosome_inner_membrane.yaml --out /private/tmp/cellstructure-batch34-20261022-36gi391b/mitosome_inner_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitosome_inner_membrane.yaml --out /private/tmp/cellstructure-batch34-20261022-36gi391b/mitosome_inner_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch34-20261022-36gi391b/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch34-20261022-36gi391b/mitosome_inner_membrane-strict.tsv |
| focused-causal | /private/tmp/cellstructure-batch34-20261022-36gi391b/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/mitosome_inner_membrane.yaml; /private/tmp/cellstructure-batch34-20261022-36gi391b/mitosome-agent/mitosome_inner_membrane-causal.log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/mitosome_inner_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 13 collected target identifiers returned OK. cellstructuremech:mitosome_envelope: SKIPPED; Exact local identifier uniquely resolves to data/structures/membrane_organelle/mitosome_envelope.yaml at frozen SHA256 762b8bad522664b480655908ccd92a258624f836a99d3e78232fe1e30aea8fc9. The maintained identity, definition and compartment boundary were independently read and match the cited native UniProt location SL0438. Local-reference validity is separate from any GO-first curation finding; no scientific identifier is renamed.; cellstructuremech:mitosome_inner_membrane: SKIPPED; Exact local identifier uniquely resolves to data/structures/membrane_organelle/mitosome_inner_membrane.yaml at frozen SHA256 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35. The maintained identity, definition and compartment boundary were independently read and match the cited native UniProt location SL0439. Local-reference validity is separate from any GO-first curation finding; no scientific identifier is renamed.; cellstructuremech:mitosome_intermembrane_space: SKIPPED; Exact local identifier uniquely resolves to data/structures/membrane_organelle/mitosome_intermembrane_space.yaml at frozen SHA256 c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95. The maintained identity, definition and compartment boundary were independently read and match the cited native UniProt location SL0440. Local-reference validity is separate from any GO-first curation finding; no scientific identifier is renamed.; cellstructuremech:mitosome_matrix: SKIPPED; Exact local identifier uniquely resolves to data/structures/membrane_organelle/mitosome_matrix.yaml at frozen SHA256 cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca. The maintained identity, definition and compartment boundary were independently read and match the cited native UniProt location SL0441. Local-reference validity is separate from any GO-first curation finding; no scientific identifier is renamed. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Tovar1999 and Tachezy2022 were inspected through complete native abstracts and bibliographic metadata only; retained403 responses are not primary bodies. The specific Tovar1999 double-membrane attribution and DOI12922 full-body distribution scope remain unverified.
- The supplementary Roger2017 review and Mi-ichi2009 primary body were read only at the precise locators above, using unchanged original source bytes and times. Neither source substitutes for a direct rereading of inaccessible Tovar1999 ultrastructure.
- No source figure pixels, supplemental data or raw microscopy were reanalyzed. Quantitative prevalence and exact taxon-specific lipid/protein formation requirements remain outside the available evidence.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T024026Z-mitosome-inner-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Scientific review of mitosome inner membrane
started_at: '2026-10-22T02:27:18Z'
finished_at: '2026-10-22T02:40:26Z'
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
summary: Exact mitosome inner membrane identity and bounded topology are supported.
  One minor finding corrects the DOI12922 bibliographic title; source-access and occurrence-frequency
  limits are retained.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/mitosome_envelope.yaml
    sha256: 762b8bad522664b480655908ccd92a258624f836a99d3e78232fe1e30aea8fc9
    role: context
  - path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    sha256: 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35
    role: target
  - path: data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
    sha256: c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95
    role: context
  - path: data/structures/membrane_organelle/mitosome_matrix.yaml
    sha256: cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca
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
- target_id: cellstructuremech:mitosome_inner_membrane
  path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  label: mitosome inner membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained record, exact native authorities, source claim
    boundaries, component grounding and every topology edge at frozen f97b1abe.
  selection: Batch34 fixed strict path-order selection; one maintained target only.
    Initial inspect/schema/strict0 completed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:mitosome_inner_membrane
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: just validate data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: just validate-strict data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    --out /private/tmp/cellstructure-batch34-20261022-36gi391b/mitosome_inner_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: focused-causal
  name: Native focused graph protein-reference check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: /private/tmp/cellstructure-batch34-20261022-36gi391b/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  exit_code: 0
  summary: Native check passed; no GENE_OR_PROTEIN actor is asserted. Topology independently
    assessed.
  evidence_ids:
  - focused-causal
- check_id: protein-verification
  name: Individual protein verification applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: Full target contains no individual gene symbol, protein example or UniProt
    accession. No optional protein inventory is mandated.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: No expression-module, gene-regulon or transcriptomic claim; anatomical
    topology does not require an expression-module lookup.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-mitosome_envelope
  - neighbor-mitosome_matrix
  - neighbor-mitosome_intermembrane_space
  - mitosome-agent-SL0438
  - mitosome-agent-SL0439
  - mitosome-agent-SL0440
  - mitosome-agent-SL0441
  - mitosome-agent-go
  - mitosome-agent-tax2759
  - mitosome-agent-tax5759
  - mitosome-agent-tovar1999-meta
  - mitosome-agent-tachezy2022-meta
  - mitosome-agent-roger2017-meta
  - mitosome-agent-roger2017-pdf
  - mitosome-agent-miichi2009-meta
  - mitosome-agent-miichi2009-pmc
  - access-tovar1999-publisher
  - access-tovar1999-pdf
  - access-tachezy2022-publisher
  - access-tachezy2022-pdf
  - access-tachezy2022-rg-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: '9 of 13 collected target identifiers returned OK. cellstructuremech:mitosome_envelope:
    SKIPPED; Exact local identifier uniquely resolves to data/structures/membrane_organelle/mitosome_envelope.yaml
    at frozen SHA256 762b8bad522664b480655908ccd92a258624f836a99d3e78232fe1e30aea8fc9.
    The maintained identity, definition and compartment boundary were independently
    read and match the cited native UniProt location SL0438. Local-reference validity
    is separate from any GO-first curation finding; no scientific identifier is renamed.;
    cellstructuremech:mitosome_inner_membrane: SKIPPED; Exact local identifier uniquely
    resolves to data/structures/membrane_organelle/mitosome_inner_membrane.yaml at
    frozen SHA256 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35.
    The maintained identity, definition and compartment boundary were independently
    read and match the cited native UniProt location SL0439. Local-reference validity
    is separate from any GO-first curation finding; no scientific identifier is renamed.;
    cellstructuremech:mitosome_intermembrane_space: SKIPPED; Exact local identifier
    uniquely resolves to data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
    at frozen SHA256 c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95.
    The maintained identity, definition and compartment boundary were independently
    read and match the cited native UniProt location SL0440. Local-reference validity
    is separate from any GO-first curation finding; no scientific identifier is renamed.;
    cellstructuremech:mitosome_matrix: SKIPPED; Exact local identifier uniquely resolves
    to data/structures/membrane_organelle/mitosome_matrix.yaml at frozen SHA256 cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca.
    The maintained identity, definition and compartment boundary were independently
    read and match the cited native UniProt location SL0441. Local-reference validity
    is separate from any GO-first curation finding; no scientific identifier is renamed.
    Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - neighbor-mitosome_envelope
  - mitosome-agent-SL0438
  - record
  - mitosome-agent-SL0439
  - neighbor-mitosome_intermembrane_space
  - mitosome-agent-SL0440
  - neighbor-mitosome_matrix
  - mitosome-agent-SL0441
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch34 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch34 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch34 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch34 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
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
    and current batch34 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  locator: Complete maintained YAML, including all history, graph edges and discussions
  accessed_at: '2026-10-22T02:33:25Z'
  support: context_only
  summary: Entire target read without modifying maintained scientific content.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent molecular-building-block description, grounding and
    essentiality; graph actor/component_ref semantics
  accessed_at: '2026-10-22T02:33:25Z'
  support: context_only
  summary: Molecular components and anatomical parts are distinct. Essentiality concerns
    whether a structure forms without a component, not catalytic function or cell
    viability.
- evidence_id: neighbor-mitosome_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_envelope.yaml
  locator: Frozen identifier, label, definition/source, parent_structures, part_of,
    has_part and xrefs
  accessed_at: '2026-10-22T02:33:25Z'
  support: context_only
  summary: Exact local boundary identity resolved from captured neighbor bytes. No
    independent scientific endorsement of other neighbor claims.
- evidence_id: neighbor-mitosome_matrix
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_matrix.yaml
  locator: Frozen identifier, label, definition/source, parent_structures, part_of,
    has_part and xrefs
  accessed_at: '2026-10-22T02:33:25Z'
  support: context_only
  summary: Exact local boundary identity resolved from captured neighbor bytes. No
    independent scientific endorsement of other neighbor claims.
- evidence_id: neighbor-mitosome_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
  locator: Frozen identifier, label, definition/source, parent_structures, part_of,
    has_part and xrefs
  accessed_at: '2026-10-22T02:33:25Z'
  support: context_only
  summary: Exact local boundary identity resolved from captured neighbor bytes. No
    independent scientific endorsement of other neighbor claims.
- evidence_id: mitosome-agent-SL0438
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0438.json
  locator: Complete JSON identity, definition, synonyms and nested isA/partOf records;
    SL0162 membrane definition where present
  accessed_at: '2026-10-22T02:23:05.250737Z'
  support: supports
  summary: SL0438 identifies the envelope as inner and outer membranes plus the intermembrane
    space; partOf points to the mitosome. Native protein statistics are not an inventory
    or absence argument.
  snapshot_sha256: a74bbec342759e1d7c209e2d408a5dac8b077776c4a482b83b5d128d4c942895
- evidence_id: mitosome-agent-SL0439
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0439.json
  locator: Complete JSON identity, definition, synonyms and nested isA/partOf records;
    SL0162 membrane definition where present
  accessed_at: '2026-10-22T02:23:05.402199Z'
  support: supports
  summary: SL0439 defines the matrix-facing membrane separating matrix from intermembrane
    space; both listed synonyms match. isA leads through SL0442 to membrane SL0162,
    and nested partOf to envelope. Native protein statistics are not an inventory
    or absence argument.
  snapshot_sha256: aa08a6ef2b2463cf77e08466169f334ff002b0ed4c1aa82f85d4ff285dcf922b
- evidence_id: mitosome-agent-SL0440
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0440.json
  locator: Complete JSON identity, definition, synonyms and nested isA/partOf records;
    SL0162 membrane definition where present
  accessed_at: '2026-10-22T02:23:05.509314Z'
  support: supports
  summary: SL0440 identifies the space between inner and outer membranes, with all
    three target synonyms and partOf envelope. Native protein statistics are not an
    inventory or absence argument.
  snapshot_sha256: d6cdb2e1eda6f4ddf5e04ba1ad05c6105be6a430a606336ed682a6edbb1d452c
- evidence_id: mitosome-agent-SL0441
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0441.json
  locator: Complete JSON identity, definition, synonyms and nested isA/partOf records;
    SL0162 membrane definition where present
  accessed_at: '2026-10-22T02:23:05.627405Z'
  support: supports
  summary: SL0441 defines the internal space enclosed by the inner membrane, with
    mitosomal matrix synonym and partOf mitosome. Native protein statistics are not
    an inventory or absence argument.
  snapshot_sha256: 2e9390220f484888b3f63b14693f749d5661543f53d983c65252ecd11dda86a7
- evidence_id: mitosome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0031090%2CGO%3A0043233%2CGO%3A0032047%2CGO%3A0005737
  locator: Complete four returned entries; exact definitions, obsolete flags and relevant
    child relation; no mixed-ancestry inference
  accessed_at: '2026-10-22T02:31:58.787812Z'
  support: supports
  summary: The four active native entries identify organelle membrane GO0031090, organelle
    lumen GO0043233, mitosome GO0032047 and cytoplasm GO0005737. Definitions support
    the broader anatomical parents; mitosome is a returned part_of child of cytoplasm.
    Local mitosome subcompartments are resolved separately, not invented as native
    GO children.
  snapshot_sha256: 84447a4dcaa3c7b733c023a08264f43349ec6e5bb97548d49cdb69095cc61c93
- evidence_id: mitosome-agent-tax2759
  kind: database
  reference: https://rest.uniprot.org/taxonomy/2759.json
  locator: taxonId, scientificName, active, rank and lineage; not taxonId from a different
    API shape
  accessed_at: '2026-10-22T02:23:03.577699Z'
  support: supports
  summary: Eukaryota is active and ranked domain. Taxonomic identity alone does not
    measure occurrence frequency.
  snapshot_sha256: af5ba762219fdecb11d214126bb8184c0eb28fc6474d14777c4aaa7f7dd89369
- evidence_id: mitosome-agent-tax5759
  kind: database
  reference: https://rest.uniprot.org/taxonomy/5759.json
  locator: taxonId, scientificName, active, rank and lineage; not taxonId from a different
    API shape
  accessed_at: '2026-10-22T02:23:04.665391Z'
  support: supports
  summary: Entamoeba histolytica is active and ranked species, under the returned
    Amoebozoa lineage. Taxonomic identity alone does not measure occurrence frequency.
  snapshot_sha256: c3e1193b8db9c26e67399e29fe6c58a9fd849517b36f3fc3125cd2974d635b32
- evidence_id: mitosome-agent-tovar1999-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1046/j.1365-2958.1999.01414.x&format=json&resultType=core
  locator: Complete resultList.result[0] identity and abstractText; primary abstract
    only
  accessed_at: '2026-10-22T02:23:01.552416Z'
  support: supports
  summary: The exact DOI, PMID10361303, title, authors/year and complete abstract
    match Tovar et al. The abstract localizes native CPN60 to the Entamoeba mitochondrial-remnant
    organelle and tests N-terminal deletion/replacement targeting. It does not document
    the specific double-membrane ultrastructural observation attributed to this source
    in the target.
  snapshot_sha256: ead9f087057c39b9c57d53a6cd147ef8edb681d6bfd540216e1620e20716f2fb
- evidence_id: mitosome-agent-tachezy2022-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/jeu.12922
  locator: Complete resultList.result[0] bibliographic identity and abstractText;
    review abstract only
  accessed_at: '2026-10-22T01:40:29.609875Z'
  support: supports
  summary: DOI10.1111/jeu.12922 resolves to The hydrogenosome of Trichomonas vaginalis
    by Tachezy, Makki and Hrdy (2022), PMID35567536. The complete abstract discusses
    hydrogenosome history, biogenesis, import and metabolism. It does not establish
    the target-supplied title or independently verify a mitosome-distribution synthesis.
  snapshot_sha256: d04be05b15294eca215c38660eed08c45e0a78d2486043a183144b4682706944
- evidence_id: mitosome-agent-roger2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.cub.2017.09.015%22
  locator: Complete native bibliographic result and abstract; supplementary source
    not originally cited by target
  accessed_at: '2026-10-22T02:20:19.311159Z'
  support: supports
  summary: Exact DOI10.1016/j.cub.2017.09.015, PMID29112874, title/authors/year and
    complete abstract identify the additional secondary review The Origin and Diversification
    of Mitochondria.
  snapshot_sha256: 79f51ae3193414033e9a85ac0cf692509624280a75f6e63345c2edf5389fef45
- evidence_id: mitosome-agent-roger2017-pdf
  kind: authority
  reference: https://ecsolab.com/assets/pdf/roger_etal_2017.pdf
  locator: Printed R1177 introduction, R1184 Diversity opening, R1186 hydrogenosome/mitosome
    comparison and ISC replacement discussion; Fig5 caption text; no figure-pixel
    or remaining full-review inspection claimed
  accessed_at: '2026-10-22T02:21:01.426006Z'
  support: supports
  summary: The secondary review describes divergent mitochondrion-related organelles
    in low-oxygen eukaryotes and the repeated evolution of reduced mitosomes. It names
    Entamoeba and preserves metabolic differences among lineages. This supports a
    qualitative patchy distribution, not a quantified census or every-species prevalence.
  snapshot_sha256: b0ddb1d89fda3d1e929ef0d65c68b15864c0e602a5736305abbb08673010982e
- evidence_id: mitosome-agent-miichi2009-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.0907106106&format=json&resultType=core
  locator: Complete native result identity and abstractText; supplementary source
    distinct from the target citation
  accessed_at: '2026-10-22T02:24:28.666244Z'
  support: supports
  summary: 'Additional primary-study identity verified: Mi-ichi et al.2009 DOI10.1073/pnas.0907106106,
    PMID19995967; complete abstract describes Entamoeba mitosome purification, localization
    and sulfate activation.'
  snapshot_sha256: 6ef807865fd7b4b185fafda4f87613ea83ac1ddf7339092fcd0254e655b605fc
- evidence_id: mitosome-agent-miichi2009-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/2799805/
  locator: Complete introductory scientific paragraph; prior same-hash Results sec2-sec6,
    Discussion sec8, Methods sec10 purification and sec13 immunofluorescence; figures
    read as captions only, not pixels or supplements
  accessed_at: '2026-10-22T02:24:28.666046Z'
  support: supports
  summary: The introduction explicitly summarizes double membranes among shared mitochondrion-related-organelle
    characteristics and describes Entamoeba mitosomes. The primary purification/localization/biochemical
    results support Entamoeba organelle occurrence and heterogeneity; they are not
    used here as a direct ultrastructural reanalysis of Tovar1999 or as a universal
    protein inventory.
  snapshot_sha256: fabbfae1c61c4c168b4a96c84caac2b62209aea2311d8d3ea6ab8ac936929ffa
- evidence_id: access-tovar1999-publisher
  kind: authority
  reference: https://doi.org/10.1046/j.1365-2958.1999.01414.x
  locator: Retained original HTTP403 response, 5681 bytes; no genuine article body
  accessed_at: '2026-10-22T02:23:01.553193Z'
  support: context_only
  summary: This prior public route returned a blocked response rather than readable
    primary text. Only the separately captured complete native abstract is used; original
    URL, bytes and access time are preserved.
  snapshot_sha256: 991e82b7deb9552f9e0d9a13f6c3b66b828b4b3bdbb4b5d4f13dc0b185916a38
- evidence_id: access-tovar1999-pdf
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/pdf/10.1046/j.1365-2958.1999.01414.x
  locator: Retained original HTTP403 response, 5693 bytes; no genuine article body
  accessed_at: '2026-10-22T02:24:28.665291Z'
  support: context_only
  summary: This prior public route returned a blocked response rather than readable
    primary text. Only the separately captured complete native abstract is used; original
    URL, bytes and access time are preserved.
  snapshot_sha256: d73a416866f0c5dbcc7829b88ac2040a75f3ac9b9c16ffee8c8cb3dbefe8b323
- evidence_id: access-tachezy2022-publisher
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/10.1111/jeu.12922
  locator: Retained original HTTP403 response, 5594 bytes; no genuine article body
  accessed_at: '2026-10-22T01:40:30.857706Z'
  support: context_only
  summary: This prior public route returned a blocked response rather than readable
    primary text. Only the separately captured complete native abstract is used; original
    URL, bytes and access time are preserved.
  snapshot_sha256: e4d24e93c0e2164b2a6f6e5c5821696fa986cb3d2ac001b49d8005f104c4ac45
- evidence_id: access-tachezy2022-pdf
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/pdf/10.1111/jeu.12922
  locator: Retained original HTTP403 response, 5606 bytes; no genuine article body
  accessed_at: '2026-10-22T01:41:03.725783Z'
  support: context_only
  summary: This prior public route returned a blocked response rather than readable
    primary text. Only the separately captured complete native abstract is used; original
    URL, bytes and access time are preserved.
  snapshot_sha256: b82924736a7926aaafae1950a545054c1110e821620d503247d59aaee715b5bf
- evidence_id: access-tachezy2022-rg-pdf
  kind: authority
  reference: https://www.researchgate.net/profile/Ivan-Hrdy/publication/360605238_The_hydrogenosome_of_Trichomonas_vaginalis/links/66fa5b6ab753fa724d4ffa69/The-hydrogenosome-of-Trichomonas-vaginalis.pdf
  locator: Retained original HTTP403 response, 779 bytes; no genuine article body
  accessed_at: '2026-10-22T01:41:36.649756Z'
  support: context_only
  summary: This prior public route returned a blocked response rather than readable
    primary text. Only the separately captured complete native abstract is used; original
    URL, bytes and access time are preserved.
  snapshot_sha256: f63b045138ec5f63f7443d87ceece69a35acc9a19ca71ab1e903b025d5f9e4fe
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:27:20Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/mitosome_inner_membrane.yaml'
  snapshot_sha256: 3b3b633ed840e318fbbb910a1d640721627136a0f6d7636a1a7a8f07ef24d2e4
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    --out /private/tmp/cellstructure-batch34-20261022-36gi391b/mitosome_inner_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:27:22Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitosome_inner_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch34-20261022-36gi391b/mitosome_inner_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch34-20261022-36gi391b/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch34-20261022-36gi391b/mitosome_inner_membrane-strict.tsv"
  snapshot_sha256: 803c5e0c95112f9a1b4ba1f7b4e8716ab875625bf78ebd8e472979fa42f3c773
- evidence_id: focused-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch34-20261022-36gi391b/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  locator: /private/tmp/cellstructure-batch34-20261022-36gi391b/mitosome-agent/mitosome_inner_membrane-causal.log
  accessed_at: '2026-10-22T02:32:08.850858Z'
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
  locator: data/structures/membrane_organelle/mitosome_inner_membrane.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '9 of 13 collected target identifiers returned OK. cellstructuremech:mitosome_envelope:
    SKIPPED; Exact local identifier uniquely resolves to data/structures/membrane_organelle/mitosome_envelope.yaml
    at frozen SHA256 762b8bad522664b480655908ccd92a258624f836a99d3e78232fe1e30aea8fc9.
    The maintained identity, definition and compartment boundary were independently
    read and match the cited native UniProt location SL0438. Local-reference validity
    is separate from any GO-first curation finding; no scientific identifier is renamed.;
    cellstructuremech:mitosome_inner_membrane: SKIPPED; Exact local identifier uniquely
    resolves to data/structures/membrane_organelle/mitosome_inner_membrane.yaml at
    frozen SHA256 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35.
    The maintained identity, definition and compartment boundary were independently
    read and match the cited native UniProt location SL0439. Local-reference validity
    is separate from any GO-first curation finding; no scientific identifier is renamed.;
    cellstructuremech:mitosome_intermembrane_space: SKIPPED; Exact local identifier
    uniquely resolves to data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
    at frozen SHA256 c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95.
    The maintained identity, definition and compartment boundary were independently
    read and match the cited native UniProt location SL0440. Local-reference validity
    is separate from any GO-first curation finding; no scientific identifier is renamed.;
    cellstructuremech:mitosome_matrix: SKIPPED; Exact local identifier uniquely resolves
    to data/structures/membrane_organelle/mitosome_matrix.yaml at frozen SHA256 cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca.
    The maintained identity, definition and compartment boundary were independently
    read and match the cited native UniProt location SL0441. Local-reference validity
    is separate from any GO-first curation finding; no scientific identifier is renamed.
    Native source checks are separately scoped; skipped or unreachable identifiers
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
  topic: Exact compartment and relationships
  outcome: supported
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: The local identifier and UniProt location represent mitosome inner membrane.
    Exact definition and synonyms match. GO0031090 is a suitable broader organelle-membrane
    class by its definition, distinct from envelope parthood. Frozen local boundary
    references resolve; source-native locations and local structures are not chemical
    entities.
  evidence_ids:
  - mitosome-agent-SL0438
  - mitosome-agent-SL0439
  - mitosome-agent-SL0440
  - mitosome-agent-SL0441
  - mitosome-agent-go
  - record
  - neighbor-mitosome_envelope
  - neighbor-mitosome_matrix
  - neighbor-mitosome_intermembrane_space
- assessment_id: taxa
  area: scope
  topic: Taxonomic identity and qualitative occurrence
  outcome: supported
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: Both native taxa match. Entamoeba organelle occurrence is supported by
    the original localization abstract and the later primary body. The broader patchy
    low-oxygen eukaryotic context is supported qualitatively by the additional evolutionary
    review.
  evidence_ids:
  - mitosome-agent-tax2759
  - mitosome-agent-tax5759
  - mitosome-agent-tovar1999-meta
  - mitosome-agent-miichi2009-pmc
  - mitosome-agent-roger2017-pdf
- assessment_id: taxa-limits
  area: evidence
  topic: Original citation and frequency limits
  outcome: unknown
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: The Tovar1999 complete abstract does not establish the specifically attributed
    double-membrane observation, and the DOI12922 review body was not accessible.
    No quantitative Eukaryota prevalence or species-wide strain census was performed.
    These access and measurement gaps are not treated as biological contradictions.
  evidence_ids:
  - mitosome-agent-tovar1999-meta
  - mitosome-agent-tachezy2022-meta
  - mitosome-agent-roger2017-pdf
  - mitosome-agent-miichi2009-pmc
- assessment_id: materials
  area: grounding
  topic: Label-only lipid constituent
  outcome: supported
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: The component explicitly denotes the lipid bilayer constituent, retains
    REVIEWED_LABEL_ONLY and does not ground a lipid class to the whole membrane location.
    Its positional role is consistent with the native anatomical definitions and nested
    generic membrane definition. The collective bilayer is constitutive of this membrane
    class; no individual lipid species or protein formation requirement is asserted.
  evidence_ids:
  - mitosome-agent-SL0439
  - mitosome-agent-go
  - schema
  - record
- assessment_id: necessity
  area: grounding
  topic: Specific molecular requirements remain unestablished
  outcome: unknown
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: The authority establishes a lipid-bilayer membrane architecture, not a
    depletion or reconstitution test for particular lipids or proteins. Exact molecular
    composition, stoichiometry and taxon-specific formation necessity remain unmeasured
    here; collective class constitution must not be extrapolated to individual essential
    constituents.
  evidence_ids:
  - mitosome-agent-SL0439
  - schema
  - record
- assessment_id: graph
  area: graph
  topic: Complete target topology graph
  outcome: supported
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: All 3 edges in this target are topological and accurately marked NONMECHANISTIC.
    The inner membrane is part of envelope, encloses matrix and delimits intermembrane
    space. No molecular import pathway, translocase inventory or assembly mechanism
    is asserted.
  evidence_ids:
  - mitosome-agent-SL0438
  - mitosome-agent-SL0439
  - mitosome-agent-SL0440
  - mitosome-agent-SL0441
  - mitosome-agent-go
  - record
  - neighbor-mitosome_envelope
  - neighbor-mitosome_matrix
  - neighbor-mitosome_intermembrane_space
- assessment_id: bibliography
  area: evidence
  topic: Exact DOI12922 article identity
  outcome: concern
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: The target bibliographic note assigns a different title to the resolving
    DOI. This is a certain bounded provenance error, separate from the supported anatomical
    identity and qualitative distribution.
  evidence_ids:
  - mitosome-agent-tachezy2022-meta
  - record
- assessment_id: coverage
  area: completeness
  topic: Full bounded record review
  outcome: supported
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  summary: All target fields, source notes, graph nodes/edges and history were read.
    The explicit lipid-identity TODO accurately distinguishes the whole-membrane location
    from a molecular constituent; no exact chemical class was established by the retained
    sources, so no forced grounding finding is added. No numerical physical property,
    maintained image, verbatim evidence snippet, individual gene symbol or UniProt
    protein example is asserted. Historical curation notes are not current absence
    claims.
  evidence_ids:
  - record
  - schema
  - mitosome-agent-SL0438
  - mitosome-agent-SL0439
  - mitosome-agent-SL0440
  - mitosome-agent-SL0441
findings:
- finding_id: F1
  issue_key: mitosome-inner-membrane-tachezy-title
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the title attached to DOI10.1111/jeu.12922
  description: 'The evidence note calls this article Hydrogenosomes and mitosomes:
    Mitochondria of anaerobic eukaryotes. Exact native metadata identifies The hydrogenosome
    of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). The DOI is valid;
    its unread full body is not presumed to lack a mitosome passage.'
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  field_paths:
  - evidence[6].notes
  evidence_ids:
  - mitosome-agent-tachezy2022-meta
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact source identity
  native_severity: minor
  normalization_reason: Minor bibliographic title/attribution error; no wrong compartment
    identity or demonstrated false distribution follows from the access limitation.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    role: maintained scientific record
  description: Correct the bibliographic title/authorship for the retained DOI. Independently
    verify or replace its use for broad mitosome distribution without claiming unread
    full text proves absence.
  acceptance_checks:
  - Confirm the retained DOI/title/author identity against native metadata.
  - Run focused schema, strict and graph checks after separately authorized curation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Tovar1999 and Tachezy2022 were inspected through complete native abstracts and bibliographic
  metadata only; retained403 responses are not primary bodies. The specific Tovar1999
  double-membrane attribution and DOI12922 full-body distribution scope remain unverified.
- The supplementary Roger2017 review and Mi-ichi2009 primary body were read only at
  the precise locators above, using unchanged original source bytes and times. Neither
  source substitutes for a direct rereading of inaccessible Tovar1999 ultrastructure.
- No source figure pixels, supplemental data or raw microscopy were reanalyzed. Quantitative
  prevalence and exact taxon-specific lipid/protein formation requirements remain
  outside the available evidence.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
