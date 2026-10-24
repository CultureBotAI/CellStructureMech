# Delta dna polymerase complex scientific review

- Review: 20261022T052920Z-delta-dna-polymerase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:15:46Z
- Finished UTC: 2026-10-22T05:29:20Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Pol-delta identity, three yeast proteins, corrected monomeric canonical assembly and coarse replication graph are supported. No concrete finding; source-body access, conditional subassemblies and exact family boundaries remain explicit limits.

## Scope And Provenance

Exactly one complete maintained record, exact native authorities and the source passages specified in each evidence locator; no scientific record changed.

Selection: Target 6 of batch49, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0043625 | data/structures/other/delta_dna_polymerase_complex.yaml | maintained | delta DNA polymerase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0043625 | Focused validator passed. |
| Focused native strict | passed | True | GO:0043625 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0043625 | Native read-only focused check passed; biological support assessed separately. |
| Native verify | passed | True | GO:0043625 | Native read-only focused check passed; biological support assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0043625 | No expression-module or transcriptomic assertion requires this resource. |
| Claim-level scientific review | passed | True | GO:0043625 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0043625 | 11 of 15 collected target identifiers returned OK. PMID:11568188: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:9677405: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:9677406: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0043625 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0043625 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0043625 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0043625 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0043625 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Corrected monomeric assembly with retained GO identity

identity: supported. Targets: GO:0043625.

Native identity, synonym, parents and nuclear-replisome parthood agree. The maintained resolved discussion explicitly rejects the still-retained GO dimer-of-heterotrimers sentence using Johansson2001. Its abstract directly reports the three subunits at1:1:1 and monomeric behavior under the tested0.1-20micromolar conditions; no new correction is required.

### Three valid examples and cautious candidate boundaries

grounding: supported. Targets: GO:0043625.

All three reviewed S288C accessions and current one-hit notes agree. The primary abstracts independently identify the three yeast constituents and reconstitution. Pol3 type-B and Pol31 delta/archaeal-II families are broader. POLD3/Cdc27 is a plausible Pol32 counterpart, but the source calls the yeast/fission subunits functionally analogous with very limited sequence similarity; the bounded current authority check does not establish an exact family assignment for the maintained budding-yeast class. No family mapping is forced.

### Subassemblies and physical assembly requirements

grounding: unknown. Targets: GO:0043625.

Burgers/Gerik explicitly recovers a Pol3/Pol31 two-subunit form and reconstitutes the three-subunit form by adding Pol32. This prevents treating Pol32 loss as universal destruction of all Pol-delta-like activity. The generic class varies across species, and a full conditional formation map is not inferred from membership or nonessential growth. UNKNOWN is retained with this positive subassembly evidence.

### Eukaryotic class and yeast canonical example

scope: supported. Targets: GO:0043625.

The typed native in_taxon relation supports the stated Eukaryota boundary. COMMON means present in most members with exceptional losses; this is qualitative conserved replication machinery rather than a numerical census. The canonical 1:1:1 yeast example is directly stated by Johansson abstract, while exact laboratory strains and detailed fractionation methods remain full-body access limits.

### Coarse replication and separately retained repair definition

graph: supported. Targets: GO:0043625.

The native definition supports replication and repair roles; the maintained function and NONMECHANISTIC graph only develop DNA replication. Three membership edges and the output claim are supported without asserting PCNA/RFC chemistry, strand specificity or repair mechanisms from the abstract alone.

### Full maintained target with bounded source review

completeness: supported. Targets: GO:0043625.

All maintained fields, current discussions and historical entries were read. Optional new mechanisms, universal family claims and additional mandatory inventory fields were not invented. Identifier resolution and scientific support were assessed separately.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/delta_dna_polymerase_complex.yaml; Entire maintained target including definition, all components/examples, graph, evidence, discussions and history | context_only | The full maintained record was read. Historical curation notes are retained as history rather than independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent/ProteinExample; EssentialityEnum, TaxonomicPresenceEnum and NONMECHANISTIC graph scope | context_only | Component identity is a taxon-neutral class. Assembly necessity differs from membership, catalytic requirement and viability. COMMON means present in most members, with losses the exception. |
| curation | docs/CURATION.md; Exact family grounding and REVIEWED_LABEL_ONLY contract, especially lines159–160 | context_only | REVIEWED_LABEL_ONLY means no exact mapping can be asserted without overclaiming, not simply that an available exact mapping was deferred in this pass. |
| complex49-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776,GO:0000940,GO:0006260,GO:0006270,GO:0008608,GO:0031431,GO:0032991,GO:0042575,GO:0042729,GO:0043601,GO:0043625,GO:0140513,GO:1990102,GO:1990125; Complete relevant identity, definition, active status, synonyms and typed child links in the14-term response; not every unrelated descendant | supports | GO0043625 matches the variable-composition Pol delta class and exact synonym; DNA-polymerase and nuclear-complex parents plus nuclear-replisome parthood are supported. Its retained dimer-of-heterotrimers prose conflicts with the later Johansson abstract, a conflict already explicitly addressed in the maintained discussion. |
| complex49-agent-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete native taxonomy response | supports | ENA confirms taxon2759 as Eukaryota, rank domain. The exact native names and available lineage/synonyms were read. |
| complex49-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | ENA confirms taxon4932 as Saccharomyces cerevisiae, rank species. The exact native names and available lineage/synonyms were read. |
| complex49-agent-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | ENA confirms taxon559292 as Saccharomyces cerevisiae S288C, rank strain. The exact native names and available lineage/synonyms were read. |
| complex49-agent-protein-P15436 | https://rest.uniprot.org/uniprotkb/P15436.json; Native accession/status/name/genes/taxon, SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and InterPro xrefs | supports | Reviewed primary accession P15436 is DNA polymerase delta catalytic subunit, with exact gene token POL3 and native taxon559292. Native subunit/location/similarity annotations and family xrefs were read; database identity and annotation are distinguished from independently inspected primary experiments. |
| complex49-agent-gene-POL3-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete gene_exact AND taxonomy_id AND reviewed:true result, size500, all returned identities | supports | The complete current reviewed exact POL3/taxon559292 query returns only P15436, with the declared gene token and matching native organism. This supports the current single-reviewed-entry wording. |
| complex49-agent-protein-P46957 | https://rest.uniprot.org/uniprotkb/P46957.json; Native accession/status/name/genes/taxon, SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and InterPro xrefs | supports | Reviewed primary accession P46957 is DNA polymerase delta small subunit, with exact gene token POL31 and native taxon559292. Native subunit/location/similarity annotations and family xrefs were read; database identity and annotation are distinguished from independently inspected primary experiments. |
| complex49-agent-gene-POL31-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL31%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete gene_exact AND taxonomy_id AND reviewed:true result, size500, all returned identities | supports | The complete current reviewed exact POL31/taxon559292 query returns only P46957, with the declared gene token and matching native organism. This supports the current single-reviewed-entry wording. |
| complex49-agent-protein-P47110 | https://rest.uniprot.org/uniprotkb/P47110.json; Native accession/status/name/genes/taxon, SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and InterPro xrefs | supports | Reviewed primary accession P47110 is DNA polymerase delta subunit 3, with exact gene token POL32 and native taxon559292. Native subunit/location/similarity annotations and family xrefs were read; database identity and annotation are distinguished from independently inspected primary experiments. |
| complex49-agent-gene-POL32-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL32%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete gene_exact AND taxonomy_id AND reviewed:true result, size500, all returned identities | supports | The complete current reviewed exact POL32/taxon559292 query returns only P47110, with the declared gene token and matching native organism. This supports the current single-reviewed-entry wording. |
| complex49-agent-pmid-11568188 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11568188+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and complete native abstract | supports | Native MED11568188: Structure of DNA polymerase delta from Saccharomyces cerevisiae. Authors Johansson E, Majka J, Burgers PM.; DOI 10.1074/jbc.m108842200. Complete abstract read at primary-study abstract tier; no full body is implied by metadata. |
| complex49-agent-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and complete native abstract | supports | Native MED14562095: Global analysis of protein localization in budding yeast. Authors Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.; DOI 10.1038/nature02026. Complete abstract read at primary-study abstract tier; no full body is implied by metadata. |
| complex49-agent-pmid-9677405 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9677405+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and complete native abstract | supports | Native MED9677405: Characterization of the two small subunits of Saccharomyces cerevisiae DNA polymerase delta. Authors Gerik KJ, Li X, Pautz A, Burgers PM.; DOI 10.1074/jbc.273.31.19747. Complete abstract read at primary-study abstract tier; no full body is implied by metadata. |
| complex49-agent-pmid-9677406 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9677406+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and complete native abstract | supports | Native MED9677406: Structure and processivity of two forms of Saccharomyces cerevisiae DNA polymerase delta. Authors Burgers PM, Gerik KJ.; DOI 10.1074/jbc.273.31.19756. Complete abstract read at primary-study abstract tier; no full body is implied by metadata. |
| complex49-agent-ols-0043625-graph | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0043625/graph; Complete OLS nodes and typed edges | supports | The exact typed graph confirms both is-a parents, nuclear-replisome part_of and in_taxon Eukaryota. Mixed related-term response collections were not used as relation-specific proof. |
| complex49-agent-ipr-IPR024826 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024826/; Native accession/name/type, complete description, hierarchy, signatures and curation flags | context_only | IPR024826 spans eukaryotic Pol delta small subunits and archaeal Pol II small subunits, so it is broader than the specifically named Pol31 class. |
| complex49-agent-ipr-IPR050240 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050240/; Native accession/name/type, complete description, hierarchy, signatures and curation flags | context_only | IPR050240 spans type-B DNA polymerases, not just Pol3; its generated prose is not biological evidence. |
| complex49-agent-ipr-IPR019038 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019038/; Native accession/name/type, complete description, hierarchy, signatures and curation flags | context_only | IPR019038 is a POLD3/Cdc27 full-protein family. The retained member query includes fission-yeast Cdc27 but not the maintained budding-yeast P47110; native P47110 has no InterPro xref. This is a candidate, not an asserted sequence-family assignment for Pol32. |
| complex49-agent-pold3-members | https://rest.uniprot.org/uniprotkb/search?query=xref%3Ainterpro-IPR019038+AND+reviewed%3Atrue&amp;format=json&amp;size=100&amp;fields=accession%2Cprotein_name%2Cgene_names%2Corganism_name; Complete bounded native query response | context_only | All six reviewed returned member identities were read, including human POLD3, fission-yeast Cdc27 and a fungal PolD3. The query does not verify the divergent S.cerevisiae Pol32 sequence as a member. |
| complex49-agent-ipr-search-Pol32 | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=Pol32; Complete bounded native query response | context_only | The exact native Pol32 text search returnedHTTP204 empty; a subsequent POLD3 search found the separately assessed candidate. Empty text search is not proof that no family exists. |
| complex49-agent-burgers1998-pdf | https://www.jbc.org/article/S0021925818491673/pdf; Exact retained unsuccessful full-body access response | context_only | Publisher PDF route returnedHTTP403 rather than PDF. Only the complete native Burgers/Gerik abstract is certified here. |
| complex49-agent-johansson2001-doi | https://doi.org/10.1074/jbc.M108842200; Exact retained unsuccessful full-body access response | context_only | The DOI route failed TLS certificate verification with status0; no Johansson full body is certified. Its complete native abstract directly states the 1:1:1 monomer conclusion and the tested concentration range. |
| schema-result | just validate data/structures/other/delta_dna_polymerase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/delta_dna_polymerase_complex.yaml |
| strict-result | just validate-strict data/structures/other/delta_dna_polymerase_complex.yaml --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/delta_dna_polymerase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/delta_dna_polymerase_complex.yaml --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/delta_dna_polymerase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch49-20261022-3rpodnkz/delta_dna_polymerase_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/delta_dna_polymerase_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/delta_dna_polymerase_complex.yaml  (GO:0043625)<br>  pol_delta_supports_dna_replication	pol3_catalytic_subunit	COVERED	-&gt;pol3_catalytic_subunit (UniProtKB:P15436)<br>  pol_delta_supports_dna_replication	pol31_subunit	COVERED	-&gt;pol31_subunit (UniProtKB:P46957)<br>  pol_delta_supports_dna_replication	pol32_subunit	COVERED	-&gt;pol32_subunit (UniProtKB:P47110)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/delta_dna_polymerase_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/delta_dna_polymerase_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 15 collected target identifiers returned OK. PMID:11568188: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:9677405: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:9677406: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Five same-base batch26 global checks are staged for guarded parent integration; this unsaved review neither finalizes nor reruns the corpus gates.
- No figure pixels, supplementary data, sequence alignment or raw experimental measurements were independently reanalyzed. Exact literature-read scopes and authority tiers are stated in evidence locators.
- Gerik1998, Burgers/Gerik1998 and Johansson2001 were read at complete native abstract tier only. The publisher PDF403 and DOI TLS failure are retained. Detailed gels, numerical raw measurements and exact original strain preparations were not certified.
- POLD3/Cdc27 family IPR019038 is a named candidate, not a verified S.cerevisiae Pol32 assignment. The exact Pol32 text-search204 is not an exhaustive authority absence result.
- Native GO still includes obsolete dimeric prose; the record already documents its source-specific correction to the monomeric yeast assembly.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes qualified clean reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T052920Z-delta-dna-polymerase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Delta dna polymerase complex scientific review
started_at: '2026-10-22T05:15:46Z'
finished_at: '2026-10-22T05:29:20Z'
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
summary: Pol-delta identity, three yeast proteins, corrected monomeric canonical assembly
  and coarse replication graph are supported. No concrete finding; source-body access,
  conditional subassemblies and exact family boundaries remain explicit limits.
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
  - path: data/structures/other/delta_dna_polymerase_complex.yaml
    sha256: 4669ff292f802ea0157d1496279723caa0330ddb676bb6fa63a6f1399b414fdf
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
- target_id: GO:0043625
  path: data/structures/other/delta_dna_polymerase_complex.yaml
  label: delta DNA polymerase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/delta_dna_polymerase_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained record, exact native authorities and
    the source passages specified in each evidence locator; no scientific record changed.
  selection: Target 6 of batch49, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0043625
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: just validate data/structures/other/delta_dna_polymerase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: just validate-strict data/structures/other/delta_dna_polymerase_complex.yaml
    --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/delta_dna_polymerase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/delta_dna_polymerase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native read-only focused check passed; biological support assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/delta_dna_polymerase_complex.yaml
    --verify
  exit_code: 0
  summary: Native read-only focused check passed; biological support assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0043625
  summary: No expression-module or transcriptomic assertion requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0043625
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex49-agent-go
  - complex49-agent-tax2759
  - complex49-agent-tax4932
  - complex49-agent-tax559292
  - complex49-agent-protein-P15436
  - complex49-agent-gene-POL3-559292
  - complex49-agent-protein-P46957
  - complex49-agent-gene-POL31-559292
  - complex49-agent-protein-P47110
  - complex49-agent-gene-POL32-559292
  - complex49-agent-pmid-11568188
  - complex49-agent-pmid-14562095
  - complex49-agent-pmid-9677405
  - complex49-agent-pmid-9677406
  - complex49-agent-ols-0043625-graph
  - complex49-agent-ipr-IPR024826
  - complex49-agent-ipr-IPR050240
  - complex49-agent-ipr-IPR019038
  - complex49-agent-pold3-members
  - complex49-agent-ipr-search-Pol32
  - complex49-agent-burgers1998-pdf
  - complex49-agent-johansson2001-doi
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0043625
  summary: '11 of 15 collected target identifiers returned OK. PMID:11568188: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:14562095:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:9677405: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force.; PMID:9677406: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport
    failure. Identity resolution does not certify every attached biological claim;
    declared abstract/body reading scope remains in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - complex49-agent-pmid-11568188
  - complex49-agent-pmid-14562095
  - complex49-agent-pmid-9677405
  - complex49-agent-pmid-9677406
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0043625
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
    and current batch49 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/delta_dna_polymerase_complex.yaml
  locator: Entire maintained target including definition, all components/examples,
    graph, evidence, discussions and history
  accessed_at: '2026-10-22T05:24:18Z'
  support: context_only
  summary: The full maintained record was read. Historical curation notes are retained
    as history rather than independent biological evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent/ProteinExample; EssentialityEnum, TaxonomicPresenceEnum
    and NONMECHANISTIC graph scope
  accessed_at: '2026-10-22T05:24:18Z'
  support: context_only
  summary: Component identity is a taxon-neutral class. Assembly necessity differs
    from membership, catalytic requirement and viability. COMMON means present in
    most members, with losses the exception.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact family grounding and REVIEWED_LABEL_ONLY contract, especially lines159–160
  accessed_at: '2026-10-22T05:24:18Z'
  support: context_only
  summary: REVIEWED_LABEL_ONLY means no exact mapping can be asserted without overclaiming,
    not simply that an available exact mapping was deferred in this pass.
- evidence_id: complex49-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776,GO:0000940,GO:0006260,GO:0006270,GO:0008608,GO:0031431,GO:0032991,GO:0042575,GO:0042729,GO:0043601,GO:0043625,GO:0140513,GO:1990102,GO:1990125
  locator: Complete relevant identity, definition, active status, synonyms and typed
    child links in the14-term response; not every unrelated descendant
  accessed_at: '2026-10-22T05:17:17.721517Z'
  support: supports
  summary: GO0043625 matches the variable-composition Pol delta class and exact synonym;
    DNA-polymerase and nuclear-complex parents plus nuclear-replisome parthood are
    supported. Its retained dimer-of-heterotrimers prose conflicts with the later
    Johansson abstract, a conflict already explicitly addressed in the maintained
    discussion.
  snapshot_sha256: effc676dda282ab5ec70dacdb4b4700afc26e2ac38836377a4f8705ee534e520
- evidence_id: complex49-agent-tax2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:17:17.721866Z'
  support: supports
  summary: ENA confirms taxon2759 as Eukaryota, rank domain. The exact native names
    and available lineage/synonyms were read.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: complex49-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:17:17.721925Z'
  support: supports
  summary: ENA confirms taxon4932 as Saccharomyces cerevisiae, rank species. The exact
    native names and available lineage/synonyms were read.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: complex49-agent-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:17:17.722002Z'
  support: supports
  summary: ENA confirms taxon559292 as Saccharomyces cerevisiae S288C, rank strain.
    The exact native names and available lineage/synonyms were read.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: complex49-agent-protein-P15436
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P15436.json
  locator: Native accession/status/name/genes/taxon, SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments and InterPro xrefs
  accessed_at: '2026-10-22T05:17:19.107116Z'
  support: supports
  summary: Reviewed primary accession P15436 is DNA polymerase delta catalytic subunit,
    with exact gene token POL3 and native taxon559292. Native subunit/location/similarity
    annotations and family xrefs were read; database identity and annotation are distinguished
    from independently inspected primary experiments.
  snapshot_sha256: c140646e1adb54eb6cbf96d96e007313c655e93b2ecd7dc1a8999d036f8846ee
- evidence_id: complex49-agent-gene-POL3-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete gene_exact AND taxonomy_id AND reviewed:true result, size500,
    all returned identities
  accessed_at: '2026-10-22T05:17:24.421406Z'
  support: supports
  summary: The complete current reviewed exact POL3/taxon559292 query returns only
    P15436, with the declared gene token and matching native organism. This supports
    the current single-reviewed-entry wording.
  snapshot_sha256: eacd36eab01d3405332f56c954439292aefca3c09475342840a7b19314a162a0
  search_scope: UniProtKB gene_exact:POL3 AND taxonomy_id:559292 AND reviewed:true;
    all returned identities and aliases inspected. This is a bounded exact-organism
    or descendant-taxonomy query as specified in its URL, not gene-absence proof.
- evidence_id: complex49-agent-protein-P46957
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P46957.json
  locator: Native accession/status/name/genes/taxon, SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments and InterPro xrefs
  accessed_at: '2026-10-22T05:17:20.067230Z'
  support: supports
  summary: Reviewed primary accession P46957 is DNA polymerase delta small subunit,
    with exact gene token POL31 and native taxon559292. Native subunit/location/similarity
    annotations and family xrefs were read; database identity and annotation are distinguished
    from independently inspected primary experiments.
  snapshot_sha256: 934e41ac083022ce27adac013243afb66b3504ae34bb288fed4a759b4bf3a7b2
- evidence_id: complex49-agent-gene-POL31-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL31%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete gene_exact AND taxonomy_id AND reviewed:true result, size500,
    all returned identities
  accessed_at: '2026-10-22T05:17:24.538015Z'
  support: supports
  summary: The complete current reviewed exact POL31/taxon559292 query returns only
    P46957, with the declared gene token and matching native organism. This supports
    the current single-reviewed-entry wording.
  snapshot_sha256: 32f913817a94215af6f28e9f8b688d6e1534cf8b4174548ab9e0f6ec0972e3a9
  search_scope: UniProtKB gene_exact:POL31 AND taxonomy_id:559292 AND reviewed:true;
    all returned identities and aliases inspected. This is a bounded exact-organism
    or descendant-taxonomy query as specified in its URL, not gene-absence proof.
- evidence_id: complex49-agent-protein-P47110
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47110.json
  locator: Native accession/status/name/genes/taxon, SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments and InterPro xrefs
  accessed_at: '2026-10-22T05:17:20.381074Z'
  support: supports
  summary: Reviewed primary accession P47110 is DNA polymerase delta subunit 3, with
    exact gene token POL32 and native taxon559292. Native subunit/location/similarity
    annotations and family xrefs were read; database identity and annotation are distinguished
    from independently inspected primary experiments.
  snapshot_sha256: e977ad040fbc43ef434b2f25805fbddabea676641681c5a4cc50da8fa35fa70e
- evidence_id: complex49-agent-gene-POL32-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL32%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete gene_exact AND taxonomy_id AND reviewed:true result, size500,
    all returned identities
  accessed_at: '2026-10-22T05:17:24.992751Z'
  support: supports
  summary: The complete current reviewed exact POL32/taxon559292 query returns only
    P47110, with the declared gene token and matching native organism. This supports
    the current single-reviewed-entry wording.
  snapshot_sha256: 6a69f3ac8c260450d0a83bdd9f3f6656308b3403da906581e6eea352d6e83037
  search_scope: UniProtKB gene_exact:POL32 AND taxonomy_id:559292 AND reviewed:true;
    all returned identities and aliases inspected. This is a bounded exact-organism
    or descendant-taxonomy query as specified in its URL, not gene-absence proof.
- evidence_id: complex49-agent-pmid-11568188
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11568188+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and complete native abstract
  accessed_at: '2026-10-22T05:17:25.344140Z'
  support: supports
  summary: 'Native MED11568188: Structure of DNA polymerase delta from Saccharomyces
    cerevisiae. Authors Johansson E, Majka J, Burgers PM.; DOI 10.1074/jbc.m108842200.
    Complete abstract read at primary-study abstract tier; no full body is implied
    by metadata.'
  snapshot_sha256: 7ca1c099e740ae464f57a71f9511a3d5f7ac04ef4ce7aa7800456940375e16d6
- evidence_id: complex49-agent-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and complete native abstract
  accessed_at: '2026-10-22T05:17:25.907959Z'
  support: supports
  summary: 'Native MED14562095: Global analysis of protein localization in budding
    yeast. Authors Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS,
    O''Shea EK.; DOI 10.1038/nature02026. Complete abstract read at primary-study
    abstract tier; no full body is implied by metadata.'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: complex49-agent-pmid-9677405
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9677405+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and complete native abstract
  accessed_at: '2026-10-22T05:17:27.273160Z'
  support: supports
  summary: 'Native MED9677405: Characterization of the two small subunits of Saccharomyces
    cerevisiae DNA polymerase delta. Authors Gerik KJ, Li X, Pautz A, Burgers PM.;
    DOI 10.1074/jbc.273.31.19747. Complete abstract read at primary-study abstract
    tier; no full body is implied by metadata.'
  snapshot_sha256: 3f104b241bed55f49d4035f4d67309eb5f8f9dc2a940fad5acb36f2d4d914487
- evidence_id: complex49-agent-pmid-9677406
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9677406+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and complete native abstract
  accessed_at: '2026-10-22T05:17:27.477252Z'
  support: supports
  summary: 'Native MED9677406: Structure and processivity of two forms of Saccharomyces
    cerevisiae DNA polymerase delta. Authors Burgers PM, Gerik KJ.; DOI 10.1074/jbc.273.31.19756.
    Complete abstract read at primary-study abstract tier; no full body is implied
    by metadata.'
  snapshot_sha256: 82bbadf8d9bffe7057bc8336f446ce6a785c671a35c87e6728381e199c43a355
- evidence_id: complex49-agent-ols-0043625-graph
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0043625/graph
  locator: Complete OLS nodes and typed edges
  accessed_at: '2026-10-22T05:19:46.756271Z'
  support: supports
  summary: The exact typed graph confirms both is-a parents, nuclear-replisome part_of
    and in_taxon Eukaryota. Mixed related-term response collections were not used
    as relation-specific proof.
  snapshot_sha256: 1967625e1ab1c42fd1f492800c7d38c84f577a12abb3c6e6d782399a566cbd84
- evidence_id: complex49-agent-ipr-IPR024826
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024826/
  locator: Native accession/name/type, complete description, hierarchy, signatures
    and curation flags
  accessed_at: '2026-10-22T05:17:52.486818Z'
  support: context_only
  summary: IPR024826 spans eukaryotic Pol delta small subunits and archaeal Pol II
    small subunits, so it is broader than the specifically named Pol31 class.
  snapshot_sha256: 44ca7da0d7b46dfaba6049af96e41bb15c0054421278767145190c5705bc57a2
- evidence_id: complex49-agent-ipr-IPR050240
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050240/
  locator: Native accession/name/type, complete description, hierarchy, signatures
    and curation flags
  accessed_at: '2026-10-22T05:17:52.967301Z'
  support: context_only
  summary: IPR050240 spans type-B DNA polymerases, not just Pol3; its generated prose
    is not biological evidence.
  snapshot_sha256: e4d65d9f86a12d9090e4c96e9859946f2b53deb1241bb4aeddf412b12feaa574
- evidence_id: complex49-agent-ipr-IPR019038
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019038/
  locator: Native accession/name/type, complete description, hierarchy, signatures
    and curation flags
  accessed_at: '2026-10-22T05:19:30.075787Z'
  support: context_only
  summary: IPR019038 is a POLD3/Cdc27 full-protein family. The retained member query
    includes fission-yeast Cdc27 but not the maintained budding-yeast P47110; native
    P47110 has no InterPro xref. This is a candidate, not an asserted sequence-family
    assignment for Pol32.
  snapshot_sha256: b98b2422d08e00f80f798e6dedf126c172d2b6e15794074efe67f0a8449db212
- evidence_id: complex49-agent-pold3-members
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=xref%3Ainterpro-IPR019038+AND+reviewed%3Atrue&format=json&size=100&fields=accession%2Cprotein_name%2Cgene_names%2Corganism_name
  locator: Complete bounded native query response
  accessed_at: '2026-10-22T05:19:30.076246Z'
  support: context_only
  summary: All six reviewed returned member identities were read, including human
    POLD3, fission-yeast Cdc27 and a fungal PolD3. The query does not verify the divergent
    S.cerevisiae Pol32 sequence as a member.
  snapshot_sha256: 5f43ef3988b5d4dd2b619d826e1a1efc1c29473d75575453d50210f5f1d4be66
  search_scope: UniProt reviewed:true AND xref:interpro-IPR019038; size100; complete
    six returned identities; no universal absence claim.
- evidence_id: complex49-agent-ipr-search-Pol32
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=Pol32
  locator: Complete bounded native query response
  accessed_at: '2026-10-22T05:17:53.809518Z'
  support: context_only
  summary: The exact native Pol32 text search returnedHTTP204 empty; a subsequent
    POLD3 search found the separately assessed candidate. Empty text search is not
    proof that no family exists.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: InterPro search=Pol32; retainedHTTP204 empty response. Bounded search
    only.
- evidence_id: complex49-agent-burgers1998-pdf
  kind: database
  reference: https://www.jbc.org/article/S0021925818491673/pdf
  locator: Exact retained unsuccessful full-body access response
  accessed_at: '2026-10-22T05:18:09.394275Z'
  support: context_only
  summary: Publisher PDF route returnedHTTP403 rather than PDF. Only the complete
    native Burgers/Gerik abstract is certified here.
  snapshot_sha256: d58db1e26234f9fb77a679cc7bbf637b97222748503d7ad270bca9da99c06144
- evidence_id: complex49-agent-johansson2001-doi
  kind: database
  reference: https://doi.org/10.1074/jbc.M108842200
  locator: Exact retained unsuccessful full-body access response
  accessed_at: '2026-10-22T05:18:09.394671Z'
  support: context_only
  summary: The DOI route failed TLS certificate verification with status0; no Johansson
    full body is certified. Its complete native abstract directly states the 1:1:1
    monomer conclusion and the tested concentration range.
  snapshot_sha256: a8014ecefc9b9c4cc3987abe484f64b8ee37dd3e6bc0182a0f12915e702dedb3
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/delta_dna_polymerase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:15:47Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/delta_dna_polymerase_complex.yaml'
  snapshot_sha256: e1237d5fbc1becfbb98be9c5915845bd30cdf5395fd5e69aad0237bd1a9d2826
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/delta_dna_polymerase_complex.yaml
    --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/delta_dna_polymerase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:15:48Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/delta_dna_polymerase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch49-20261022-3rpodnkz/delta_dna_polymerase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch49-20261022-3rpodnkz/delta_dna_polymerase_complex-strict.tsv"
  snapshot_sha256: c07f0f9171ed99261ca78a5f1e13d2a67dee216dc0125ea56644408fe60fe51f
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/delta_dna_polymerase_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:17:35.933414Z'
  support: supports
  summary: "data/structures/other/delta_dna_polymerase_complex.yaml  (GO:0043625)\n\
    \  pol_delta_supports_dna_replication\tpol3_catalytic_subunit\tCOVERED\t->pol3_catalytic_subunit\
    \ (UniProtKB:P15436)\n  pol_delta_supports_dna_replication\tpol31_subunit\tCOVERED\t\
    ->pol31_subunit (UniProtKB:P46957)\n  pol_delta_supports_dna_replication\tpol32_subunit\t\
    COVERED\t->pol32_subunit (UniProtKB:P47110)\n\ncausal_graphs GENE_OR_PROTEIN node\
    \ summary:\n     3  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref\
    \ on the node\n     3  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 9d47952c8ac17bd446c4fab095faa0a2308bb3d31ccca4a3cc88179ae930d58e
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch49-20261022-3rpodnkz/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/delta_dna_polymerase_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:17:37.193954Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/delta_dna_polymerase_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 15 collected target identifiers returned OK. PMID:11568188: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:14562095:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:9677405: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force.; PMID:9677406: UNREACHABLE; Exact native Europe
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
  topic: Corrected monomeric assembly with retained GO identity
  outcome: supported
  target_ids:
  - GO:0043625
  summary: Native identity, synonym, parents and nuclear-replisome parthood agree.
    The maintained resolved discussion explicitly rejects the still-retained GO dimer-of-heterotrimers
    sentence using Johansson2001. Its abstract directly reports the three subunits
    at1:1:1 and monomeric behavior under the tested0.1-20micromolar conditions; no
    new correction is required.
  evidence_ids:
  - record
  - complex49-agent-go
  - complex49-agent-ols-0043625-graph
  - complex49-agent-pmid-11568188
  - complex49-agent-pmid-9677406
- assessment_id: components
  area: grounding
  topic: Three valid examples and cautious candidate boundaries
  outcome: supported
  target_ids:
  - GO:0043625
  summary: All three reviewed S288C accessions and current one-hit notes agree. The
    primary abstracts independently identify the three yeast constituents and reconstitution.
    Pol3 type-B and Pol31 delta/archaeal-II families are broader. POLD3/Cdc27 is a
    plausible Pol32 counterpart, but the source calls the yeast/fission subunits functionally
    analogous with very limited sequence similarity; the bounded current authority
    check does not establish an exact family assignment for the maintained budding-yeast
    class. No family mapping is forced.
  evidence_ids:
  - record
  - curation
  - complex49-agent-ipr-IPR024826
  - complex49-agent-ipr-IPR050240
  - complex49-agent-ipr-IPR019038
  - complex49-agent-pold3-members
  - complex49-agent-ipr-search-Pol32
  - complex49-agent-pmid-9677405
  - complex49-agent-pmid-9677406
  - complex49-agent-pmid-11568188
  - complex49-agent-protein-P15436
  - complex49-agent-protein-P46957
  - complex49-agent-protein-P47110
  - complex49-agent-gene-POL3-559292
  - complex49-agent-gene-POL31-559292
  - complex49-agent-gene-POL32-559292
- assessment_id: formation
  area: grounding
  topic: Subassemblies and physical assembly requirements
  outcome: unknown
  target_ids:
  - GO:0043625
  summary: Burgers/Gerik explicitly recovers a Pol3/Pol31 two-subunit form and reconstitutes
    the three-subunit form by adding Pol32. This prevents treating Pol32 loss as universal
    destruction of all Pol-delta-like activity. The generic class varies across species,
    and a full conditional formation map is not inferred from membership or nonessential
    growth. UNKNOWN is retained with this positive subassembly evidence.
  evidence_ids:
  - record
  - schema
  - complex49-agent-pmid-9677405
  - complex49-agent-pmid-9677406
  - complex49-agent-pmid-11568188
- assessment_id: scope
  area: scope
  topic: Eukaryotic class and yeast canonical example
  outcome: supported
  target_ids:
  - GO:0043625
  summary: The typed native in_taxon relation supports the stated Eukaryota boundary.
    COMMON means present in most members with exceptional losses; this is qualitative
    conserved replication machinery rather than a numerical census. The canonical
    1:1:1 yeast example is directly stated by Johansson abstract, while exact laboratory
    strains and detailed fractionation methods remain full-body access limits.
  evidence_ids:
  - record
  - schema
  - complex49-agent-go
  - complex49-agent-ols-0043625-graph
  - complex49-agent-pmid-11568188
  - complex49-agent-tax2759
  - complex49-agent-tax4932
  - complex49-agent-tax559292
- assessment_id: function-graph
  area: graph
  topic: Coarse replication and separately retained repair definition
  outcome: supported
  target_ids:
  - GO:0043625
  summary: The native definition supports replication and repair roles; the maintained
    function and NONMECHANISTIC graph only develop DNA replication. Three membership
    edges and the output claim are supported without asserting PCNA/RFC chemistry,
    strand specificity or repair mechanisms from the abstract alone.
  evidence_ids:
  - record
  - schema
  - complex49-agent-go
  - complex49-agent-pmid-9677406
- assessment_id: coverage
  area: completeness
  topic: Full maintained target with bounded source review
  outcome: supported
  target_ids:
  - GO:0043625
  summary: All maintained fields, current discussions and historical entries were
    read. Optional new mechanisms, universal family claims and additional mandatory
    inventory fields were not invented. Identifier resolution and scientific support
    were assessed separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex49-agent-go
findings: []
actions: []
limitations:
- Five same-base batch26 global checks are staged for guarded parent integration;
  this unsaved review neither finalizes nor reruns the corpus gates.
- No figure pixels, supplementary data, sequence alignment or raw experimental measurements
  were independently reanalyzed. Exact literature-read scopes and authority tiers
  are stated in evidence locators.
- Gerik1998, Burgers/Gerik1998 and Johansson2001 were read at complete native abstract
  tier only. The publisher PDF403 and DOI TLS failure are retained. Detailed gels,
  numerical raw measurements and exact original strain preparations were not certified.
- POLD3/Cdc27 family IPR019038 is a named candidate, not a verified S.cerevisiae Pol32
  assignment. The exact Pol32 text-search204 is not an exhaustive authority absence
  result.
- Native GO still includes obsolete dimeric prose; the record already documents its
  source-specific correction to the monomeric yeast assembly.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes qualified clean reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
