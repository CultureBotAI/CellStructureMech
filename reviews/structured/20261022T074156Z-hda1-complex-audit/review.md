# Source-grounded review of HDA1 complex

- Review: 20261022T074156Z-hda1-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:12:32Z
- Finished UTC: 2026-10-22T07:41:56Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor finding resolves Hda1 and Hda3 family mappings. The GO tetramer, chromatin relationship, reference proteins and scoped deacetylase function are supported.

## Scope And Provenance

Exactly one complete maintained target, with source-native and primary reading scopes declared individually.

Selection: One complete record in strict-path batch 57 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0070823 | data/structures/other/hda1_complex.yaml | maintained | HDA1 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0070823 | Focused validator passed. |
| Focused native strict | passed | True | GO:0070823 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0070823 | Focused check passed; scientific claims assessed separately. |
| Native focused verify | passed | True | GO:0070823 | Focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0070823 | No iModulon-specific claim is assessed; the relevant complex/assay evidence was inspected directly. |
| Claim-level scientific review | passed | True | GO:0070823 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0070823 | 11 of 14 collected target identifiers returned OK. PMID:11287668: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:14562095: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:8663039: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0070823 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0070823 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0070823 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0070823 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0070823 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### GO-defined tetramer and chromatin parthood

identity: supported. Targets: GO:0070823.

The exact GO class, histone-deacetylase parent and chromatin parthood agree. The paper suggests a 2:1:1 tetramer from interaction and hydrodynamic evidence; GO adopts that definition. The review preserves this provenance and does not convert the historical molecular-mass estimate into a modern structural measurement.

### Two resolved classes and one unresolved paralog boundary

grounding: concern. Targets: GO:0070823.

Hda1 and Hda3 have specific whole-family mappings. The inspected Hda2/3 family includes both paralogs and the Hda2 PANTHER subfamily route returned no body, so Hda2 is left unresolved within this bounded search.

### Distinct conditional subunit-association dependencies

grounding: supported. Targets: GO:0070823.

The generic roles correctly describe the Hda2/Hda3 subcomplex and activity. Wu additionally reports no detectable Hda1/Hda2 coassociation after Hda3 deletion, versus about 4 percent Hda1/Hda3 recovery after Hda2 deletion. Hda1 self-association and Hda2/Hda3 association persist without the other subcomplex. These bounded results enrich the supported inventory without establishing a material defect in its stated scope.

### Supported membership and deacetylase outcome

graph: supported. Targets: GO:0070823.

All three membership edges and the whole-complex activity edge are supported. In-vitro core-histone activity and in-vivo H3/H2B acetylation at ENA1 are distinct assays. The record does not assert that every histone site or promoter responds identically.

### Yeast assay backgrounds and reference examples

scope: supported. Targets: GO:0070823.

Wu specifies YDS2/YDS21U-derived strains and their WJY derivatives. S288C accessions are reference examples, not claims about every assay background. COMMON means present in most members with exceptional losses; no numerical census is inferred.

### Universal individual-constituent requirements remain unestablished

grounding: unknown. Targets: GO:0070823.

The bounded interaction, recruitment and activity results do not establish a universal per-constituent formation-necessity profile. UNKNOWN values are not automatically defects and are not converted to ESSENTIAL.

### Complete maintained target and bounded follow-up

completeness: supported. Targets: GO:0070823.

Every maintained field, evidence row, component/example, graph edge, discussion and history entry was read. Optional unpopulated slots are not defects. Scientific status/history remain unchanged.

## Findings

### F1: Resolve Hda1 and Hda3 family mappings

minor / open / confirmed; issue key: hda1-resolve-hda1-hda3-families.

The open task and label-only rows still defer all three families. Native IPR017321 and IPR026216 now resolve the Hda1 and Hda3 classes, while the inspected Hda2 candidate remains broader.

## Recommended Actions And Acceptance Checks

### A1

Ground Hda1 and Hda3 at their verified whole-family identities and narrow the remaining task to Hda2.

- Use IPR017321 for the yeast class-II Hda1 class and IPR026216 for Hda3.
- Do not use shared IPR021006 as an exact Hda2-only mapping.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/hda1_complex.yaml; Entire maintained target, including all components, evidence, graph edges, discussions and history | context_only | The complete target was read. The maintained YAML owns any later scientific correction. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope | context_only | Formation necessity is distinct from activity, localization and viability. COMMON is the qualitative category present in most members with exceptional losses, not a measured prevalence census. |
| curation | docs/CURATION.md; Exact class identity and taxon-paired protein examples | context_only | Protein examples do not replace constituent-class grounding. Shared domains and broader paralog families do not resolve exact class tasks. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Scope and edge-level source support | context_only | Descriptive membership graphs need not assert a complete mechanism; a directly observed conditional physical dependency can be stated without making every constituent universally essential. |
| root57-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000118,GO:0000417,GO:0000785,GO:0004407,GO:0006334,GO:0032297,GO:0032991,GO:0044775,GO:0070823,GO:1990078,GO:1990083,GO:1990085; Native identities, status, complete definitions/comments/synonyms and focal typed relationships | supports | The twelve inspected terms establish the focal HDA1, Hda-beta and HIR identities, their parent classes and the named function/substructure targets. Only relevant typed relations were used. |
| root57-sources-GO0070823-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070823/ancestors?relations=is_a; Complete native is_a ancestor response | supports | The complete is_a-only ancestry supports the declared parent class. It does not establish parthood or taxonomic frequency. |
| root57-sources-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | Native taxId 4932 identifies Saccharomyces cerevisiae; broad taxon, species and reference strain are kept distinct. |
| root57-sources-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | Native taxId 559292 identifies Saccharomyces cerevisiae S288C; broad taxon, species and reference strain are kept distinct. |
| root57-sources-pmid-11287668 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11287668+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 11287668: HDA2 and HDA3 are related proteins that interact with and are essential for the activity of the yeast histone deacetylase HDA1. Wu J, Carmen AA, Kobayashi R, Suka N, Grunstein M. (2001); DOI 10.1073/pnas.081560698. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 14562095: Global analysis of protein localization in budding yeast. Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK. (2003); DOI 10.1038/nature02026. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-pmid-8663039 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663039+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 8663039: HDA1 and HDA3 are components of a yeast histone deacetylase (HDA) complex. Carmen AA, Rundlett SE, Grunstein M. (1996); DOI 10.1074/jbc.271.26.15837. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-doi-10.1073_pnas.081560698 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.081560698%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED 11287668: HDA2 and HDA3 are related proteins that interact with and are essential for the activity of the yeast histone deacetylase HDA1. Wu J, Carmen AA, Kobayashi R, Suka N, Grunstein M. (2001). Complete abstract read; body evidence is separately located. |
| root57-sources-doi-10.1074_jbc.271.26.15837 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.271.26.15837%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED 8663039: HDA1 and HDA3 are components of a yeast histone deacetylase (HDA) complex. Carmen AA, Rundlett SE, Grunstein M. (1996). Complete abstract read; body evidence is separately located. |
| root57-sources-protein-P53973 | https://rest.uniprot.org/uniprotkb/P53973.json; Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY and MISCELLANEOUS comments where present | supports | P53973 is the reviewed HDA1 reference in taxon 559292. Native names/aliases, organism, family cross-references and annotations support the stated identity. Its localization evidence tags were checked directly; this does not imply primary-body inspection of every cited localization assay. |
| root57-sources-gene-HDA1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and literal query parameters | supports | The exact gene and organism query, restricted to reviewed entries, returns exactly P53973. |
| root57-sources-protein-Q06629 | https://rest.uniprot.org/uniprotkb/Q06629.json; Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY and MISCELLANEOUS comments where present | supports | Q06629 is the reviewed HDA2 reference in taxon 559292. Native names/aliases, organism, family cross-references and annotations support the stated identity. Its localization evidence tags were checked directly; this does not imply primary-body inspection of every cited localization assay. |
| root57-sources-gene-HDA2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and literal query parameters | supports | The exact gene and organism query, restricted to reviewed entries, returns exactly Q06629. |
| root57-sources-protein-Q06623 | https://rest.uniprot.org/uniprotkb/Q06623.json; Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY and MISCELLANEOUS comments where present | supports | Q06623 is the reviewed HDA3 reference in taxon 559292. Native names/aliases, organism, family cross-references and annotations support the stated identity. Its localization evidence tags were checked directly; this does not imply primary-body inspection of every cited localization assay. |
| root57-sources-gene-HDA3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and literal query parameters | supports | The exact gene and organism query, restricted to reviewed entries, returns exactly Q06623. |
| root57-sources-ipr-IPR017321 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017321/; Native accession/name/type, complete description with curation flags, integrated signatures and hierarchy | supports | The yeast class-II histone-deacetylase whole family provides a precise Hda1 mapping and integrates PIRSF037919. |
| root57-sources-ipr-IPR026216 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026216/; Native accession/name/type, complete description with curation flags, integrated signatures and hierarchy | supports | The HDA1 subunit-3 whole family is the narrower Hda3 child of Hda2/3 and integrates PR02093. |
| root57-sources-ipr-IPR021006 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021006/; Native accession/name/type, complete description with curation flags, integrated signatures and hierarchy | supports | This family explicitly includes both fungal Hda2 and Hda3, so it does not distinguish the exact Hda2 class. |
| root57-sources-ipr-IPR000286 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000286/; Native accession/name/type, complete description with curation flags, integrated signatures and hierarchy | supports | This broad histone-deacetylase entry includes multiple classes and an AcuC child; it is not an exact Hda1 mapping. |
| access-panther-PTHR31882-SF11 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR31882:SF11/; Retrieved response status/content type and diagnostic body only | context_only | The candidate subfamily identified by Q06629 returned HTTP204 with an empty body; this route did not independently resolve its class boundary. |
| access-carmen1996-doi | https://doi.org/10.1074/jbc.271.26.15837; Retrieved response status/content type and diagnostic body only | context_only | The DOI resolved to an Elsevier redirect page naming the correct title and PII, without article body text. |
| access-carmen1996-jbc | https://www.jbc.org/article/S0021-9258(18)36134-9/fulltext; Retrieved response status/content type and diagnostic body only | context_only | The publisher article route derived from the DOI PII returned HTTP403. Carmen1996 remains verified at native complete-abstract tier. |
| root57-sources-PMC31845-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC31845/; Results/Discussion sec10–sec17 in full including Figures1–6 captions; Methods sec2 (including Table1), sec4, sec5 and sec6 in full | supports | Wu2001 distinguishes Hda1 self-association, an Hda2/Hda3 subcomplex and their association through Hda3. In hda3 deletion, Hda2 is not detected in Hda1 precipitates despite reported unchanged Hda2 amount; hda2 deletion reduces but does not abolish Hda1/Hda3 association. Separate assays measure deacetylase activity and promoter histone acetylation. |
| schema-result | just validate data/structures/other/hda1_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/hda1_complex.yaml |
| strict-result | just validate-strict data/structures/other/hda1_complex.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda1_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/hda1_complex.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda1_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda1_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml --causal-graphs; Complete focused native report | supports | data/structures/other/hda1_complex.yaml  (GO:0070823)<br>  yeast_hda1_histone_deacetylase_activity	hda1_hda1_complex_subunit	COVERED	-&gt;hda1_hda1_complex_subunit (UniProtKB:P53973)<br>  yeast_hda1_histone_deacetylase_activity	hda2_hda1_complex_subunit	COVERED	-&gt;hda2_hda1_complex_subunit (UniProtKB:Q06629)<br>  yeast_hda1_histone_deacetylase_activity	hda3_hda1_complex_subunit	COVERED	-&gt;hda3_hda1_complex_subunit (UniProtKB:Q06623)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml --verify; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/hda1_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 14 collected target identifiers returned OK. PMID:11287668: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:14562095: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:8663039: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five same-base batch26 corpus gates and exact target resolver rows are integrated with every manifested input hash verified.
- No figure pixels, atomic coordinates, raw assay datasets or sequence alignments were reanalyzed. Primary body reading is limited to the explicitly named sections and embedded captions.
- Any absence finding is confined to the complete inspected target and its existing task; bounded native family queries do not establish absence from all databases.
- Protein localization source notes match native annotation provenance. Except where explicitly described, the cited localization papers were read at abstract tier; their detailed assays were not independently rechecked.
- Carmen1996 was read at complete native abstract tier; its publisher body was unavailable through the retained routes. Wu Methods sec3/sec7/sec8 were not read, and no independent reanalysis of ChIP or densitometry is claimed.
- The paper describes the HDA1 tetramer as likely; GO states the tetrameric definition. The two source strengths are retained separately.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations and issue-bearing reviews alike.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Materiality reassessment removed an optional association-detail omission finding; the source observation remains explicitly assessed and universal formation necessity remains unknown.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T074156Z-hda1-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of HDA1 complex
started_at: '2026-10-22T07:12:32Z'
finished_at: '2026-10-22T07:41:56Z'
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
summary: One minor finding resolves Hda1 and Hda3 family mappings. The GO tetramer,
  chromatin relationship, reference proteins and scoped deacetylase function are supported.
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
  - path: data/structures/other/hda1_complex.yaml
    sha256: 6b19f4b66623b018af2496a92442c707fecaf0e551591afaff220957c2bb7b90
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
- target_id: GO:0070823
  path: data/structures/other/hda1_complex.yaml
  label: HDA1 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda1_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, with source-native and primary
    reading scopes declared individually.
  selection: One complete record in strict-path batch 57 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0070823
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: just validate data/structures/other/hda1_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: just validate-strict data/structures/other/hda1_complex.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda1_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml --verify
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0070823
  summary: No iModulon-specific claim is assessed; the relevant complex/assay evidence
    was inspected directly.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0070823
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root57-sources-go
  - root57-sources-GO0070823-ancestors
  - root57-sources-tax-4932
  - root57-sources-tax-559292
  - root57-sources-pmid-11287668
  - root57-sources-pmid-14562095
  - root57-sources-pmid-8663039
  - root57-sources-doi-10.1073_pnas.081560698
  - root57-sources-doi-10.1074_jbc.271.26.15837
  - root57-sources-protein-P53973
  - root57-sources-gene-HDA1
  - root57-sources-protein-Q06629
  - root57-sources-gene-HDA2
  - root57-sources-protein-Q06623
  - root57-sources-gene-HDA3
  - root57-sources-ipr-IPR017321
  - root57-sources-ipr-IPR026216
  - root57-sources-ipr-IPR021006
  - root57-sources-ipr-IPR000286
  - access-panther-PTHR31882-SF11
  - access-carmen1996-doi
  - access-carmen1996-jbc
  - root57-sources-PMC31845-html
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0070823
  summary: '11 of 14 collected target identifiers returned OK. PMID:11287668: UNREACHABLE;
    Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport
    failure in the corpus resolver is not treated as identifier invalidity or as proof
    that its primary body was read.; PMID:14562095: UNREACHABLE; Unique native MED
    identity, exact PMID/title/DOI and bibliography inspected; transport failure in
    the corpus resolver is not treated as identifier invalidity or as proof that its
    primary body was read.; PMID:8663039: UNREACHABLE; Unique native MED identity,
    exact PMID/title/DOI and bibliography inspected; transport failure in the corpus
    resolver is not treated as identifier invalidity or as proof that its primary
    body was read. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root57-sources-pmid-11287668
  - root57-sources-doi-10.1073_pnas.081560698
  - root57-sources-pmid-14562095
  - root57-sources-pmid-8663039
  - root57-sources-doi-10.1074_jbc.271.26.15837
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0070823
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
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/hda1_complex.yaml
  locator: Entire maintained target, including all components, evidence, graph edges,
    discussions and history
  accessed_at: '2026-10-22T07:22:37Z'
  support: context_only
  summary: The complete target was read. The maintained YAML owns any later scientific
    correction.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope
  accessed_at: '2026-10-22T07:22:37Z'
  support: context_only
  summary: Formation necessity is distinct from activity, localization and viability.
    COMMON is the qualitative category present in most members with exceptional losses,
    not a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and taxon-paired protein examples
  accessed_at: '2026-10-22T07:22:37Z'
  support: context_only
  summary: Protein examples do not replace constituent-class grounding. Shared domains
    and broader paralog families do not resolve exact class tasks.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope and edge-level source support
  accessed_at: '2026-10-22T07:22:37Z'
  support: context_only
  summary: Descriptive membership graphs need not assert a complete mechanism; a directly
    observed conditional physical dependency can be stated without making every constituent
    universally essential.
- evidence_id: root57-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000118,GO:0000417,GO:0000785,GO:0004407,GO:0006334,GO:0032297,GO:0032991,GO:0044775,GO:0070823,GO:1990078,GO:1990083,GO:1990085
  locator: Native identities, status, complete definitions/comments/synonyms and focal
    typed relationships
  accessed_at: '2026-10-22T07:09:06.769100Z'
  support: supports
  summary: The twelve inspected terms establish the focal HDA1, Hda-beta and HIR identities,
    their parent classes and the named function/substructure targets. Only relevant
    typed relations were used.
  snapshot_sha256: 21ed713180a84eeed2230337bf1f89ecd5489141f8030b26157ee5ec18456ad0
- evidence_id: root57-sources-GO0070823-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070823/ancestors?relations=is_a
  locator: Complete native is_a ancestor response
  accessed_at: '2026-10-22T07:09:17.605658Z'
  support: supports
  summary: The complete is_a-only ancestry supports the declared parent class. It
    does not establish parthood or taxonomic frequency.
  snapshot_sha256: 536e5048998a508ae3656808f9a6a22e1560fb1b49b0b22ebfec3fb5dab7af49
- evidence_id: root57-sources-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T07:09:06.769364Z'
  support: supports
  summary: Native taxId 4932 identifies Saccharomyces cerevisiae; broad taxon, species
    and reference strain are kept distinct.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root57-sources-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T07:09:07.391453Z'
  support: supports
  summary: Native taxId 559292 identifies Saccharomyces cerevisiae S288C; broad taxon,
    species and reference strain are kept distinct.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root57-sources-pmid-11287668
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11287668+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:11.919519Z'
  support: supports
  summary: 'MED 11287668: HDA2 and HDA3 are related proteins that interact with and
    are essential for the activity of the yeast histone deacetylase HDA1. Wu J, Carmen
    AA, Kobayashi R, Suka N, Grunstein M. (2001); DOI 10.1073/pnas.081560698. Entire
    native abstract read; this evidence row does not claim the paper body.'
  snapshot_sha256: 8b84ed89a0c193389060b1ec76ec16cb819810528eeddb2b94b931ddc7eb7956
- evidence_id: root57-sources-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:12.881913Z'
  support: supports
  summary: 'MED 14562095: Global analysis of protein localization in budding yeast.
    Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea EK. (2003);
    DOI 10.1038/nature02026. Entire native abstract read; this evidence row does not
    claim the paper body.'
  snapshot_sha256: 571f7249c52d66a3b53ae05fa04cfe3012ab729c63308d338c745e9f3c1daa72
- evidence_id: root57-sources-pmid-8663039
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663039+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:15.019083Z'
  support: supports
  summary: 'MED 8663039: HDA1 and HDA3 are components of a yeast histone deacetylase
    (HDA) complex. Carmen AA, Rundlett SE, Grunstein M. (1996); DOI 10.1074/jbc.271.26.15837.
    Entire native abstract read; this evidence row does not claim the paper body.'
  snapshot_sha256: 8d46a5564c73d6a675c2416c9e8668e0eb3c0a7fa7aeb1c0a6ef4f5ab2ce9c6c
- evidence_id: root57-sources-doi-10.1073_pnas.081560698
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.081560698%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T07:09:16.904438Z'
  support: supports
  summary: 'Unique DOI result MED 11287668: HDA2 and HDA3 are related proteins that
    interact with and are essential for the activity of the yeast histone deacetylase
    HDA1. Wu J, Carmen AA, Kobayashi R, Suka N, Grunstein M. (2001). Complete abstract
    read; body evidence is separately located.'
  snapshot_sha256: 78da99ab61986d9b34e2db5c507881525076b104956b3b96688195347fa32576
- evidence_id: root57-sources-doi-10.1074_jbc.271.26.15837
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.271.26.15837%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T07:09:16.936243Z'
  support: supports
  summary: 'Unique DOI result MED 8663039: HDA1 and HDA3 are components of a yeast
    histone deacetylase (HDA) complex. Carmen AA, Rundlett SE, Grunstein M. (1996).
    Complete abstract read; body evidence is separately located.'
  snapshot_sha256: 59810c36da09111fbc372cdb43c4df0c00bae42cb16e96012bbfec35afa8a97b
- evidence_id: root57-sources-protein-P53973
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53973.json
  locator: Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY
    and MISCELLANEOUS comments where present
  accessed_at: '2026-10-22T07:09:09.940808Z'
  support: supports
  summary: P53973 is the reviewed HDA1 reference in taxon 559292. Native names/aliases,
    organism, family cross-references and annotations support the stated identity.
    Its localization evidence tags were checked directly; this does not imply primary-body
    inspection of every cited localization assay.
  snapshot_sha256: e50191724ca3e786967c7b5ce8763d21fac7d51e9223d3f56c17a31de328b92c
- evidence_id: root57-sources-gene-HDA1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and literal query parameters
  accessed_at: '2026-10-22T07:09:18.220787Z'
  support: supports
  summary: The exact gene and organism query, restricted to reviewed entries, returns
    exactly P53973.
  snapshot_sha256: 7da88f294fab60508ac10e385aa01f893bdcd109ac205710f49cc52ef030e780
- evidence_id: root57-sources-protein-Q06629
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q06629.json
  locator: Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY
    and MISCELLANEOUS comments where present
  accessed_at: '2026-10-22T07:09:11.543810Z'
  support: supports
  summary: Q06629 is the reviewed HDA2 reference in taxon 559292. Native names/aliases,
    organism, family cross-references and annotations support the stated identity.
    Its localization evidence tags were checked directly; this does not imply primary-body
    inspection of every cited localization assay.
  snapshot_sha256: c95cc08c295d630c447171a145ae4619f8ead6254b1e4cf7810d65d507b76479
- evidence_id: root57-sources-gene-HDA2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and literal query parameters
  accessed_at: '2026-10-22T07:09:18.244857Z'
  support: supports
  summary: The exact gene and organism query, restricted to reviewed entries, returns
    exactly Q06629.
  snapshot_sha256: f70e68b0e42f34d170def711100c9d8d122b4c13e00b4a7fcb402e46c7ee2010
- evidence_id: root57-sources-protein-Q06623
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q06623.json
  locator: Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY
    and MISCELLANEOUS comments where present
  accessed_at: '2026-10-22T07:09:11.145038Z'
  support: supports
  summary: Q06623 is the reviewed HDA3 reference in taxon 559292. Native names/aliases,
    organism, family cross-references and annotations support the stated identity.
    Its localization evidence tags were checked directly; this does not imply primary-body
    inspection of every cited localization assay.
  snapshot_sha256: 5a71ecc7341f2b1495a8c62bce3fcbea0022bdb71b629f8db1bd9f4fd1a24420
- evidence_id: root57-sources-gene-HDA3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and literal query parameters
  accessed_at: '2026-10-22T07:09:19.111166Z'
  support: supports
  summary: The exact gene and organism query, restricted to reviewed entries, returns
    exactly Q06623.
  snapshot_sha256: 795e8fbb802b47e30bc08a7f98e76bde37deaf7b16dbeeaa82e8d46546629a05
- evidence_id: root57-sources-ipr-IPR017321
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017321/
  locator: Native accession/name/type, complete description with curation flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:12:52.049304Z'
  support: supports
  summary: The yeast class-II histone-deacetylase whole family provides a precise
    Hda1 mapping and integrates PIRSF037919.
  snapshot_sha256: 6aa1d1d924b6c91decebcc7cd09ae8835f9c6e3e79963b9c0aeccba041ef213b
- evidence_id: root57-sources-ipr-IPR026216
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026216/
  locator: Native accession/name/type, complete description with curation flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:12:52.049616Z'
  support: supports
  summary: The HDA1 subunit-3 whole family is the narrower Hda3 child of Hda2/3 and
    integrates PR02093.
  snapshot_sha256: a4c9bf5c6c00b7f375ec628e7de68503f5e89852c21c3243f1089eb3c83f0f05
- evidence_id: root57-sources-ipr-IPR021006
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021006/
  locator: Native accession/name/type, complete description with curation flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:12:52.649507Z'
  support: supports
  summary: This family explicitly includes both fungal Hda2 and Hda3, so it does not
    distinguish the exact Hda2 class.
  snapshot_sha256: cd3f7ac1eda2c12e0e34aef59d59a330014c6373981bab6405ef0ebee027ac22
- evidence_id: root57-sources-ipr-IPR000286
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000286/
  locator: Native accession/name/type, complete description with curation flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:12:54.939778Z'
  support: supports
  summary: This broad histone-deacetylase entry includes multiple classes and an AcuC
    child; it is not an exact Hda1 mapping.
  snapshot_sha256: 65691d9d3d7eeb24628309fb3d164063dd7c60bd545eb804683db71cee53a88e
- evidence_id: access-panther-PTHR31882-SF11
  kind: primary_source
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR31882:SF11/
  locator: Retrieved response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:18:52.670333Z'
  support: context_only
  summary: The candidate subfamily identified by Q06629 returned HTTP204 with an empty
    body; this route did not independently resolve its class boundary.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: access-carmen1996-doi
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.271.26.15837
  locator: Retrieved response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:12:56.724441Z'
  support: context_only
  summary: The DOI resolved to an Elsevier redirect page naming the correct title
    and PII, without article body text.
  snapshot_sha256: 904124333ad441cefb964fba199f91bb7cf9eb82d36db393ccb9cda9448695a9
- evidence_id: access-carmen1996-jbc
  kind: primary_source
  reference: https://www.jbc.org/article/S0021-9258(18)36134-9/fulltext
  locator: Retrieved response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:18:53.284553Z'
  support: context_only
  summary: The publisher article route derived from the DOI PII returned HTTP403.
    Carmen1996 remains verified at native complete-abstract tier.
  snapshot_sha256: 7b96b333029e36921285ba0dc0602765fe24e8d39390887c60bd1a193286eca6
- evidence_id: root57-sources-PMC31845-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC31845/
  locator: Results/Discussion sec10–sec17 in full including Figures1–6 captions; Methods
    sec2 (including Table1), sec4, sec5 and sec6 in full
  accessed_at: '2026-10-22T07:12:55.014684Z'
  support: supports
  summary: Wu2001 distinguishes Hda1 self-association, an Hda2/Hda3 subcomplex and
    their association through Hda3. In hda3 deletion, Hda2 is not detected in Hda1
    precipitates despite reported unchanged Hda2 amount; hda2 deletion reduces but
    does not abolish Hda1/Hda3 association. Separate assays measure deacetylase activity
    and promoter histone acetylation.
  snapshot_sha256: 9245042afddf989b741e6ea8135189895dc20185473540ec25e6c88067f68309
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/hda1_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:12:34Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/hda1_complex.yaml'
  snapshot_sha256: 9e698d30faac47f37040fa3112eeb60b2d218f885dad9df3ec9553e984f48c65
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/hda1_complex.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda1_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:12:35Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/hda1_complex.yaml\
    \ --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda1_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda1_complex-strict.tsv"
  snapshot_sha256: d739f8736b7f9f9523446de27237f1ff604edb5e20c6ba5d7c141923fde9cfbe
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml --causal-graphs
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:17:29.139328Z'
  support: supports
  summary: "data/structures/other/hda1_complex.yaml  (GO:0070823)\n  yeast_hda1_histone_deacetylase_activity\t\
    hda1_hda1_complex_subunit\tCOVERED\t->hda1_hda1_complex_subunit (UniProtKB:P53973)\n\
    \  yeast_hda1_histone_deacetylase_activity\thda2_hda1_complex_subunit\tCOVERED\t\
    ->hda2_hda1_complex_subunit (UniProtKB:Q06629)\n  yeast_hda1_histone_deacetylase_activity\t\
    hda3_hda1_complex_subunit\tCOVERED\t->hda3_hda1_complex_subunit (UniProtKB:Q06623)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 0698baa112f4c65d51a87fc7cdc54fa4c097af5e3283457b5e188c37526b371c
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml --verify
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:17:30.648445Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/hda1_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 14 collected target identifiers returned OK. PMID:11287668: UNREACHABLE;
    Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport
    failure in the corpus resolver is not treated as identifier invalidity or as proof
    that its primary body was read.; PMID:14562095: UNREACHABLE; Unique native MED
    identity, exact PMID/title/DOI and bibliography inspected; transport failure in
    the corpus resolver is not treated as identifier invalidity or as proof that its
    primary body was read.; PMID:8663039: UNREACHABLE; Unique native MED identity,
    exact PMID/title/DOI and bibliography inspected; transport failure in the corpus
    resolver is not treated as identifier invalidity or as proof that its primary
    body was read. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
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
  topic: GO-defined tetramer and chromatin parthood
  outcome: supported
  target_ids:
  - GO:0070823
  summary: The exact GO class, histone-deacetylase parent and chromatin parthood agree.
    The paper suggests a 2:1:1 tetramer from interaction and hydrodynamic evidence;
    GO adopts that definition. The review preserves this provenance and does not convert
    the historical molecular-mass estimate into a modern structural measurement.
  evidence_ids:
  - record
  - root57-sources-go
  - root57-sources-GO0070823-ancestors
  - root57-sources-PMC31845-html
- assessment_id: composition
  area: grounding
  topic: Two resolved classes and one unresolved paralog boundary
  outcome: concern
  target_ids:
  - GO:0070823
  summary: Hda1 and Hda3 have specific whole-family mappings. The inspected Hda2/3
    family includes both paralogs and the Hda2 PANTHER subfamily route returned no
    body, so Hda2 is left unresolved within this bounded search.
  evidence_ids:
  - record
  - curation
  - root57-sources-ipr-IPR017321
  - root57-sources-ipr-IPR026216
  - root57-sources-ipr-IPR021006
  - root57-sources-ipr-IPR000286
  - root57-sources-protein-P53973
  - root57-sources-protein-Q06629
  - root57-sources-protein-Q06623
  - root57-sources-gene-HDA1
  - root57-sources-gene-HDA2
  - root57-sources-gene-HDA3
- assessment_id: formation
  area: grounding
  topic: Distinct conditional subunit-association dependencies
  outcome: supported
  target_ids:
  - GO:0070823
  summary: The generic roles correctly describe the Hda2/Hda3 subcomplex and activity.
    Wu additionally reports no detectable Hda1/Hda2 coassociation after Hda3 deletion,
    versus about 4 percent Hda1/Hda3 recovery after Hda2 deletion. Hda1 self-association
    and Hda2/Hda3 association persist without the other subcomplex. These bounded
    results enrich the supported inventory without establishing a material defect
    in its stated scope.
  evidence_ids:
  - record
  - schema
  - root57-sources-PMC31845-html
- assessment_id: graph
  area: graph
  topic: Supported membership and deacetylase outcome
  outcome: supported
  target_ids:
  - GO:0070823
  summary: All three membership edges and the whole-complex activity edge are supported.
    In-vitro core-histone activity and in-vivo H3/H2B acetylation at ENA1 are distinct
    assays. The record does not assert that every histone site or promoter responds
    identically.
  evidence_ids:
  - record
  - graphs
  - root57-sources-go
  - root57-sources-PMC31845-html
  - root57-sources-doi-10.1073_pnas.081560698
  - root57-sources-doi-10.1074_jbc.271.26.15837
- assessment_id: scope
  area: scope
  topic: Yeast assay backgrounds and reference examples
  outcome: supported
  target_ids:
  - GO:0070823
  summary: Wu specifies YDS2/YDS21U-derived strains and their WJY derivatives. S288C
    accessions are reference examples, not claims about every assay background. COMMON
    means present in most members with exceptional losses; no numerical census is
    inferred.
  evidence_ids:
  - record
  - schema
  - root57-sources-PMC31845-html
  - root57-sources-tax-4932
  - root57-sources-tax-559292
  - root57-sources-protein-P53973
  - root57-sources-protein-Q06629
  - root57-sources-protein-Q06623
- assessment_id: formation-necessity
  area: grounding
  topic: Universal individual-constituent requirements remain unestablished
  outcome: unknown
  target_ids:
  - GO:0070823
  summary: The bounded interaction, recruitment and activity results do not establish
    a universal per-constituent formation-necessity profile. UNKNOWN values are not
    automatically defects and are not converted to ESSENTIAL.
  evidence_ids:
  - record
  - schema
  - root57-sources-PMC31845-html
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target and bounded follow-up
  outcome: supported
  target_ids:
  - GO:0070823
  summary: Every maintained field, evidence row, component/example, graph edge, discussion
    and history entry was read. Optional unpopulated slots are not defects. Scientific
    status/history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root57-sources-go
  - root57-sources-doi-10.1073_pnas.081560698
  - root57-sources-doi-10.1074_jbc.271.26.15837
findings:
- finding_id: F1
  issue_key: hda1-resolve-hda1-hda3-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve Hda1 and Hda3 family mappings
  description: The open task and label-only rows still defer all three families. Native
    IPR017321 and IPR026216 now resolve the Hda1 and Hda3 classes, while the inspected
    Hda2 candidate remains broader.
  target_ids:
  - GO:0070823
  field_paths:
  - components[0].grounding_status
  - components[2].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root57-sources-ipr-IPR017321
  - root57-sources-ipr-IPR026216
  - root57-sources-protein-P53973
  - root57-sources-protein-Q06629
  - root57-sources-protein-Q06623
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda1_complex.yaml
    role: maintained scientific record
  rule_id: Exact constituent-class grounding
  native_severity: minor
  normalization_reason: A bounded actionable class mapping under the existing explicit
    task; the complex identity and named protein examples remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0070823
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda1_complex.yaml
    role: maintained scientific record
  description: Ground Hda1 and Hda3 at their verified whole-family identities and
    narrow the remaining task to Hda2.
  acceptance_checks:
  - Use IPR017321 for the yeast class-II Hda1 class and IPR026216 for Hda3.
  - Do not use shared IPR021006 as an exact Hda2-only mapping.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
limitations:
- All five same-base batch26 corpus gates and exact target resolver rows are integrated
  with every manifested input hash verified.
- No figure pixels, atomic coordinates, raw assay datasets or sequence alignments
  were reanalyzed. Primary body reading is limited to the explicitly named sections
  and embedded captions.
- Any absence finding is confined to the complete inspected target and its existing
  task; bounded native family queries do not establish absence from all databases.
- Protein localization source notes match native annotation provenance. Except where
  explicitly described, the cited localization papers were read at abstract tier;
  their detailed assays were not independently rechecked.
- Carmen1996 was read at complete native abstract tier; its publisher body was unavailable
  through the retained routes. Wu Methods sec3/sec7/sec8 were not read, and no independent
  reanalysis of ChIP or densitometry is claimed.
- The paper describes the HDA1 tetramer as likely; GO states the tetrameric definition.
  The two source strengths are retained separately.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations and issue-bearing reviews
  alike.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Materiality reassessment removed an optional association-detail omission finding;
  the source observation remains explicitly assessed and universal formation necessity
  remains unknown.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
