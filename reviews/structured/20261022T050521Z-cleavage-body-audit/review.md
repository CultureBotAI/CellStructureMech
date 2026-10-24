# Cleavage body scientific review

- Review: 20261022T050521Z-cleavage-body-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:47:27Z
- Finished UTC: 2026-10-22T05:05:21Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Cleavage-body identity, marker components and bounded spatial graph are supported. Two minor findings resolve CPSF-100 grounding and the canonical example citation scope.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph claims and completeness.

Selection: Target 9 of batch47 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0071920 | data/structures/other/cleavage_body.yaml | maintained | cleavage body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0071920 | Focused validator passed. |
| Focused native strict | passed | True | GO:0071920 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0071920 | Focused native check passed; claim-level support assessed separately. |
| Focused native verify | passed | True | GO:0071920 | Focused native check passed; claim-level support assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0071920 | No expression-module claim is maintained. |
| Claim-level scientific review | passed | True | GO:0071920 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0071920 | 11 of 14 collected target identifiers returned OK. PMID:11598190: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:32816001: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:8654386: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0071920 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0071920 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0071920 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0071920 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0071920 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Protein-rich nuclear body with explicit marker boundaries

identity: supported. Targets: GO:0071920.

GO0071920, nuclear-body parent and nuclear-lumen location agree. The OTHER kind appropriately avoids declaring an obligate resident-RNA granule. GO definition language is interpreted with the maintained component-boundary TODO and graph caveats, not as universal DDX1 residency or demonstrated processing in every focus.

### CPSF-100 has an exact family

grounding: concern. Targets: GO:0071920.

CPSF2 IPR027075 is an exact whole-protein family corroborated by Q9P2I0. CstF-64 inspected xrefs identify hinge, C-terminal or RNA-binding domains rather than a demonstrated exact whole-family identity, so its unresolved grounding is not forced.

### Correct human protein examples

grounding: supported. Targets: GO:0071920.

CSTF2/P33240 and CPSF2/Q9P2I0 are reviewed, correctly named and uniquely resolved by the exact gene/taxon queries. Nuclear localization evidence is not conflated with a complete cleavage-body assembly experiment.

### Marker enrichment does not prove formation necessity

grounding: unknown. Targets: GO:0071920.

CstF-64 and CPSF-100 enrichment, differing cell-cycle persistence and proximity measurements do not establish which factors are indispensable for the whole body to form. UNKNOWN remains appropriate.

### Dynamic human-cell scope with a citation-placement gap

scope: concern. Targets: GO:0071920.

VARIABLE is compatible with the observed cell-type and cell-cycle differences. The canonical note combines T24 and HeLa but cites only the T24 study; the HeLa source is already elsewhere in the record and should be placed with that assertion.

### Concentration and association, not proven local catalysis

evidence: supported. Targets: GO:0071920.

The maintained functional description concentrates processing factors and states their spatial association with Cajal bodies and histone loci. This bounded wording fits the primary experiments, including the absence of detected RNA accumulation in the HeLa assays.

### Nonmechanistic localization and spatial-association graph

graph: supported. Targets: GO:0071920.

The graph explicitly excludes a complete condensate pathway and direct active processing inside the body. Directed localization, body associations and histone-locus overlaps are supported at the stated cell/assay level.

### One family and one canonical-source correction

completeness: supported. Targets: GO:0071920.

All maintained fields and the DDX1/resident-factor TODO were reviewed. The body studies justify retaining the open boundary question; they do not require treating every neighboring focus as a constituent.

## Findings

### F1: Ground the verified CPSF-100 family

minor / open / confirmed; issue key: cleavage-body-cpsf100-family.

CPSF-100/CPSF2 remains REVIEWED_LABEL_ONLY despite exact whole-family IPR027075 and the independently matching Q9P2I0 example. This resolves one named part of the broader component-boundary TODO.

### F2: Attach the HeLa source to the combined canonical example

minor / open / confirmed; issue key: cleavage-body-canonical-source-scope.

The canonical note names both T24 and HeLa but its sole reference, Schul1999 DOI10.1091/mbc.10.11.3815, documents the T24 experiment. Li2006 DOI10.1091/mbc.e05-08-0768 directly supplies the HeLa experiments and already appears elsewhere in the record. The biological examples are supported collectively; the row-level attribution is incomplete.

## Recommended Actions And Acceptance Checks

### A1

Ground CPSF-100 with IPR027075 and reconcile that portion of the TODO while preserving unresolved CstF-64 and resident-versus-neighboring-factor questions.

- Verify exact source identities and reconcile the specified current fields and TODO scope.
- Preserve supported accessions and membership; retain assay, lineage and uncertainty limits.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.

### A2

Either narrow the existing canonical note to T24 and add a separately sourced HeLa entry, or use a supported evidence representation that places each experimental source beside its claim. Preserve their different cell-cycle and cell-line behavior.

- Verify exact source identities and reconcile the specified current fields and TODO scope.
- Preserve supported accessions and membership; retain assay, lineage and uncertainty limits.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/cleavage_body.yaml; Entire maintained target, history, components, evidence, discussions and graphs | context_only | All maintained fields were read; history is provenance rather than independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Components, essentiality, COMMON and graph scope | context_only | Whole-protein families differ from shared domains and individual examples. Formation necessity differs from functional and cellular essentiality. COMMON means present in most members, with losses the exception. |
| curation | docs/CURATION.md; Source identity, exact grounding and claim-specific support | context_only | Reviewed label-only means no exact term exists. Verified whole-protein identity may be grounded independently of its separately evidenced role in a complex. Canonical taxon scope must match the cited experiment. |
| root47-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0006260,GO:0006338,GO:0006974,GO:0008623,GO:0015030,GO:0016604,GO:0030896,GO:0031010,GO:0031124,GO:0031261,GO:0031981,GO:0042555,GO:0071162,GO:0071920,GO:0140513; All16 requested terms: complete id/name/active/definition/synonyms/comments and relevant maintained typed links, not every descendant | supports | The requested native GO identities, definitions, synonyms and inspected maintained typed relationships agree with the target classes and functions. Missing direct ontology links alone do not disprove sourced biological parthood. |
| root47-sources-pmid-8654386 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8654386+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED8654386: The RNA 3' cleavage factors CstF 64 kDa and CPSF 100 kDa are concentrated in nuclear domains closely associated with coiled bodies and newly synthesized RNA. DOI 10.1002/j.1460-2075.1996.tb00649.x. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-11598190 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11598190+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED11598190: Association of human DEAD box protein DDX1 with a cleavage stimulation factor involved in 3'-end processing of pre-MRNA. DOI 10.1091/mbc.12.10.3046. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-10564273 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10564273+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED10564273: Nuclear domains enriched in RNA 3'-processing factors associate with coiled bodies and histone genes in a cell cycle-dependent manner. DOI 10.1091/mbc.10.11.3815. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-32816001 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A32816001+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED32816001: A missense mutation in the CSTF2 gene that impairs the function of the RNA recognition motif and causes defects in 3' end processing is associated with intellectual disability in humans. DOI 10.1093/nar/gkaa689. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-doi-7 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e05-08-0768%22&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED16371507: Dynamic nature of cleavage bodies and their spatial relationship to DDX1 bodies, Cajal bodies, and gems. DOI 10.1091/mbc.e05-08-0768. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-protein-P33240 | https://rest.uniprot.org/uniprotkb/P33240.json; Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro/Pfam cross-references | supports | P33240 agrees with the maintained reviewed entry, protein name, gene identity and taxon identifier. Membership and experimental source scope are assessed separately. |
| root47-sources-protein-Q9P2I0 | https://rest.uniprot.org/uniprotkb/Q9P2I0.json; Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro/Pfam cross-references | supports | Q9P2I0 agrees with the maintained reviewed entry, protein name, gene identity and taxon identifier. Membership and experimental source scope are assessed separately. |
| root47-sources-gene-CSTF2-9606 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACSTF2%29+AND+%28organism_id%3A9606%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and all result accession/status/name/gene/taxon fields | supports | The exact reviewed gene/taxon query returns one result, matching the maintained accession, status, names and taxon. |
| root47-sources-gene-CPSF2-9606 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACPSF2%29+AND+%28organism_id%3A9606%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and all result accession/status/name/gene/taxon fields | supports | The exact reviewed gene/taxon query returns one result, matching the maintained accession, status, names and taxon. |
| root47-sources-tax9606 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9606; Complete native taxonomy response | supports | ENA verifies taxon 9606 and its rank, name and lineage. Species and strain identities are kept distinct. |
| root47-sources-ipr-IPR027075 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027075/; Complete accession/name/type/description, curation flags and family metadata | supports | IPR027075 is a family named Cleavage and polyadenylation specificity factor subunit 2. Complete native description and its curation flags were inspected; example cross-references provide an independent identity join. This annotation is not primary evidence of complex membership. |
| root47-sources-legacy-PMC25681 | https://pmc.ncbi.nlm.nih.gov/articles/PMC25681/?report=reader; Complete Methods sec3/4/5/6 and Results sec10/11/12 with Fig1–5 captions; remaining sections not certified | supports | The experiment cultures T24 cells, synchronizes populations, stains CstF-64/coilin, and uses locus FISH. Cleavage-body/Cajal-body relationships change during the cell cycle; S-phase bodies often overlap the 6p21 histone cluster but not tested snRNA loci. This source does not itself establish a HeLa canonical experiment. |
| root47-sources-legacy-PMC1382303 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1382303/?report=reader; Complete Methods sec3/4 and Results sec9/10/11/12/13/14, including Table1/2 and embedded Fig1–9 captions as located in those sections; later inhibitor/latrunculin Results and Discussion not certified | supports | HeLa ATCC cells show strongly cell-cycle-dependent CstF-64 foci and more persistent CPSF-100 foci; HeLa PV and other cells differ. DDX1 bodies can exist independently, especially in G1. Pulse/pulse-chase experiments do not show RNA accumulation in S-phase HeLa cleavage bodies, so marker enrichment is not direct proof of active RNA processing there. |
| root47-sources-legacy-PMC60154 | https://pmc.ncbi.nlm.nih.gov/articles/PMC60154/?report=reader; Complete Methods sec3/5 and Results sec12/13/14/15/16 including embedded Fig3–6 captions; other sections and videos not certified | supports | HeLa imaging, limited coimmunoprecipitation and antibody-based FRET support DDX1/CstF-64 proximity in a subset of foci. Some DDX1 foci lack CstF-64; the FRET antibody geometry limits direct distance interpretation. Nascent-RNA labeling and mitotic/G1 behavior further separate DDX1 foci from an invariably active cleavage body. |
| schema-result | just validate data/structures/other/cleavage_body.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/cleavage_body.yaml |
| strict-result | just validate-strict data/structures/other/cleavage_body.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/cleavage_body-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/cleavage_body.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/cleavage_body-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/cleavage_body-strict.tsv |
| native-cleavage_body-causal-graphs | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cleavage_body.yaml; Complete focused native report | supports | data/structures/other/cleavage_body.yaml  (GO:0071920)<br>  cstf_cpsf_cleavage_body_positioning	cstf64	COVERED	-&gt;cstf64 (UniProtKB:P33240)<br>  cstf_cpsf_cleavage_body_positioning	cpsf100	COVERED	-&gt;cpsf100 (UniProtKB:Q9P2I0)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-cleavage_body-verify | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/cleavage_body.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/cleavage_body.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 14 collected target identifiers returned OK. PMID:11598190: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:32816001: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:8654386: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw experimental data, supplementary files or sequence alignments were reanalyzed. Primary-body inspection is limited to the explicitly listed sections.
- Schul1996 is available as complete native metadata/abstract and a scanned legacy page; its full scanned article was not read. Grozdanov2020 was read at native abstract level only; the retained body is not certified.
- Li2006 inhibitor and latrunculin-result sections and the cited videos were not read; no new mechanism or complete resident-factor inventory is claimed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes reviews for all uncovered records, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T050521Z-cleavage-body-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cleavage body scientific review
started_at: '2026-10-22T04:47:27Z'
finished_at: '2026-10-22T05:05:21Z'
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
summary: Cleavage-body identity, marker components and bounded spatial graph are supported.
  Two minor findings resolve CPSF-100 grounding and the canonical example citation
  scope.
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
  - path: data/structures/other/cleavage_body.yaml
    sha256: 790cd51917a39d31d033994a33784891cd76bd8d06ca98d0f43cfdba2aef65c2
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
- target_id: GO:0071920
  path: data/structures/other/cleavage_body.yaml
  label: cleavage body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cleavage_body.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph claims and completeness.
  selection: Target 9 of batch47 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0071920
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0071920
  command: just validate data/structures/other/cleavage_body.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0071920
  command: just validate-strict data/structures/other/cleavage_body.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/cleavage_body-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-cleavage_body-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0071920
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cleavage_body.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-cleavage_body-causal-graphs
- check_id: native-cleavage_body-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0071920
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/cleavage_body.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-cleavage_body-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0071920
  summary: No expression-module claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0071920
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root47-sources-go
  - root47-sources-pmid-8654386
  - root47-sources-pmid-11598190
  - root47-sources-pmid-10564273
  - root47-sources-pmid-32816001
  - root47-sources-doi-7
  - root47-sources-protein-P33240
  - root47-sources-protein-Q9P2I0
  - root47-sources-gene-CSTF2-9606
  - root47-sources-gene-CPSF2-9606
  - root47-sources-tax9606
  - root47-sources-ipr-IPR027075
  - root47-sources-legacy-PMC25681
  - root47-sources-legacy-PMC1382303
  - root47-sources-legacy-PMC60154
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0071920
  summary: '11 of 14 collected target identifiers returned OK. PMID:11598190: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:32816001:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:8654386: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root47-sources-pmid-11598190
  - root47-sources-pmid-32816001
  - root47-sources-pmid-8654386
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0071920
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0071920
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0071920
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0071920
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0071920
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
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/cleavage_body.yaml
  locator: Entire maintained target, history, components, evidence, discussions and
    graphs
  accessed_at: '2026-10-22T04:59:19Z'
  support: context_only
  summary: All maintained fields were read; history is provenance rather than independent
    scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Components, essentiality, COMMON and graph scope
  accessed_at: '2026-10-22T04:59:19Z'
  support: context_only
  summary: Whole-protein families differ from shared domains and individual examples.
    Formation necessity differs from functional and cellular essentiality. COMMON
    means present in most members, with losses the exception.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Source identity, exact grounding and claim-specific support
  accessed_at: '2026-10-22T04:59:19Z'
  support: context_only
  summary: Reviewed label-only means no exact term exists. Verified whole-protein
    identity may be grounded independently of its separately evidenced role in a complex.
    Canonical taxon scope must match the cited experiment.
- evidence_id: root47-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0006260,GO:0006338,GO:0006974,GO:0008623,GO:0015030,GO:0016604,GO:0030896,GO:0031010,GO:0031124,GO:0031261,GO:0031981,GO:0042555,GO:0071162,GO:0071920,GO:0140513
  locator: 'All16 requested terms: complete id/name/active/definition/synonyms/comments
    and relevant maintained typed links, not every descendant'
  accessed_at: '2026-10-22T04:47:53.214339Z'
  support: supports
  summary: The requested native GO identities, definitions, synonyms and inspected
    maintained typed relationships agree with the target classes and functions. Missing
    direct ontology links alone do not disprove sourced biological parthood.
  snapshot_sha256: 7e9a7e9f97cb8700350b218ea7610079c613603a48f19d04ce36665e94dc65ef
- evidence_id: root47-sources-pmid-8654386
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8654386+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:48:00.524362Z'
  support: supports
  summary: 'MED8654386: The RNA 3'' cleavage factors CstF 64 kDa and CPSF 100 kDa
    are concentrated in nuclear domains closely associated with coiled bodies and
    newly synthesized RNA. DOI 10.1002/j.1460-2075.1996.tb00649.x. Complete native
    bibliographic identity and abstract were inspected. This row certifies abstract-level
    access only; body inspection is recorded separately.'
  snapshot_sha256: 784ab6766cdb4cf8711c7e17e024460edec5d194c40ec3950c9cef4cb5d64d43
- evidence_id: root47-sources-pmid-11598190
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11598190+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:58.618804Z'
  support: supports
  summary: 'MED11598190: Association of human DEAD box protein DDX1 with a cleavage
    stimulation factor involved in 3''-end processing of pre-MRNA. DOI 10.1091/mbc.12.10.3046.
    Complete native bibliographic identity and abstract were inspected. This row certifies
    abstract-level access only; body inspection is recorded separately.'
  snapshot_sha256: 7f7dfce3867bcb48d6ccac614c09266a7359c4d10fe9f5ad35e141e29299f40a
- evidence_id: root47-sources-pmid-10564273
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10564273+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:57.573040Z'
  support: supports
  summary: 'MED10564273: Nuclear domains enriched in RNA 3''-processing factors associate
    with coiled bodies and histone genes in a cell cycle-dependent manner. DOI 10.1091/mbc.10.11.3815.
    Complete native bibliographic identity and abstract were inspected. This row certifies
    abstract-level access only; body inspection is recorded separately.'
  snapshot_sha256: e4d4161b76c42ac2fbe9c4f6c6d888256579c75af4cd90756a7a7c4421910533
- evidence_id: root47-sources-pmid-32816001
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A32816001+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:48:00.520597Z'
  support: supports
  summary: 'MED32816001: A missense mutation in the CSTF2 gene that impairs the function
    of the RNA recognition motif and causes defects in 3'' end processing is associated
    with intellectual disability in humans. DOI 10.1093/nar/gkaa689. Complete native
    bibliographic identity and abstract were inspected. This row certifies abstract-level
    access only; body inspection is recorded separately.'
  snapshot_sha256: 7b17404a83f1abb92dec7bb0896dc838e790974dc7781425cc51088d92ccd89e
- evidence_id: root47-sources-doi-7
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e05-08-0768%22&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:56.821703Z'
  support: supports
  summary: 'MED16371507: Dynamic nature of cleavage bodies and their spatial relationship
    to DDX1 bodies, Cajal bodies, and gems. DOI 10.1091/mbc.e05-08-0768. Complete
    native bibliographic identity and abstract were inspected. This row certifies
    abstract-level access only; body inspection is recorded separately.'
  snapshot_sha256: f6604d23546840ea858b85c2ebdd9f1d889fd37e9ec1a68c894b53da3bd96bee
- evidence_id: root47-sources-protein-P33240
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33240.json
  locator: Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION and SIMILARITY comments; InterPro/Pfam cross-references
  accessed_at: '2026-10-22T04:47:54.756428Z'
  support: supports
  summary: P33240 agrees with the maintained reviewed entry, protein name, gene identity
    and taxon identifier. Membership and experimental source scope are assessed separately.
  snapshot_sha256: addb37de638cf7e0da95c0361cafa8fb803a0b2b18b997b33503ce7dee8b1c64
- evidence_id: root47-sources-protein-Q9P2I0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9P2I0.json
  locator: Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION and SIMILARITY comments; InterPro/Pfam cross-references
  accessed_at: '2026-10-22T04:47:55.690243Z'
  support: supports
  summary: Q9P2I0 agrees with the maintained reviewed entry, protein name, gene identity
    and taxon identifier. Membership and experimental source scope are assessed separately.
  snapshot_sha256: 7573e1dba083367d120c213fc1e81694b971aa2481efe06567871f5adf55dd8a
- evidence_id: root47-sources-gene-CSTF2-9606
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACSTF2%29+AND+%28organism_id%3A9606%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and all result accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:48:49.427501Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one result, matching the maintained
    accession, status, names and taxon.
  snapshot_sha256: 2582528c77c85883893aa0ddb8ac9cf2ae3b78a3b647e196e22d6d4b2d1a5f68
- evidence_id: root47-sources-gene-CPSF2-9606
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACPSF2%29+AND+%28organism_id%3A9606%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and all result accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:48:49.558691Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one result, matching the maintained
    accession, status, names and taxon.
  snapshot_sha256: 0f2ed6fe7615b44332fe21100a483918645ec259ccf86deeeedab921b4337f1a
- evidence_id: root47-sources-tax9606
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9606
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:47:53.997014Z'
  support: supports
  summary: ENA verifies taxon 9606 and its rank, name and lineage. Species and strain
    identities are kept distinct.
  snapshot_sha256: ae6861231eabbe5c76a3e6240a9109a3163b77f2061b644c22bbdd1b01b15840
- evidence_id: root47-sources-ipr-IPR027075
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027075/
  locator: Complete accession/name/type/description, curation flags and family metadata
  accessed_at: '2026-10-22T04:48:46.237505Z'
  support: supports
  summary: IPR027075 is a family named Cleavage and polyadenylation specificity factor
    subunit 2. Complete native description and its curation flags were inspected;
    example cross-references provide an independent identity join. This annotation
    is not primary evidence of complex membership.
  snapshot_sha256: 70cbafb0b5ded36fe8064c99b9cef50866ae2c1eb127155cfba899cb720ac36e
- evidence_id: root47-sources-legacy-PMC25681
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC25681/?report=reader
  locator: Complete Methods sec3/4/5/6 and Results sec10/11/12 with Fig1–5 captions;
    remaining sections not certified
  accessed_at: '2026-10-22T04:48:50.626270Z'
  support: supports
  summary: The experiment cultures T24 cells, synchronizes populations, stains CstF-64/coilin,
    and uses locus FISH. Cleavage-body/Cajal-body relationships change during the
    cell cycle; S-phase bodies often overlap the 6p21 histone cluster but not tested
    snRNA loci. This source does not itself establish a HeLa canonical experiment.
  snapshot_sha256: ad6bb553d75e20a311f499f7b29ea6cdb789ead2ad23a212c0828af9878c00b0
- evidence_id: root47-sources-legacy-PMC1382303
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1382303/?report=reader
  locator: Complete Methods sec3/4 and Results sec9/10/11/12/13/14, including Table1/2
    and embedded Fig1–9 captions as located in those sections; later inhibitor/latrunculin
    Results and Discussion not certified
  accessed_at: '2026-10-22T04:48:50.496893Z'
  support: supports
  summary: HeLa ATCC cells show strongly cell-cycle-dependent CstF-64 foci and more
    persistent CPSF-100 foci; HeLa PV and other cells differ. DDX1 bodies can exist
    independently, especially in G1. Pulse/pulse-chase experiments do not show RNA
    accumulation in S-phase HeLa cleavage bodies, so marker enrichment is not direct
    proof of active RNA processing there.
  snapshot_sha256: 168af20dd2c9255014565ced068c3e686ad88ea2936edc39ba0e03f492fd0371
- evidence_id: root47-sources-legacy-PMC60154
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC60154/?report=reader
  locator: Complete Methods sec3/5 and Results sec12/13/14/15/16 including embedded
    Fig3–6 captions; other sections and videos not certified
  accessed_at: '2026-10-22T04:48:51.092055Z'
  support: supports
  summary: HeLa imaging, limited coimmunoprecipitation and antibody-based FRET support
    DDX1/CstF-64 proximity in a subset of foci. Some DDX1 foci lack CstF-64; the FRET
    antibody geometry limits direct distance interpretation. Nascent-RNA labeling
    and mitotic/G1 behavior further separate DDX1 foci from an invariably active cleavage
    body.
  snapshot_sha256: 44a41bddb949b61e8b60be563b17165099794f7c78cbde9fc8d1235da72b1aed
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/cleavage_body.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:29Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/cleavage_body.yaml'
  snapshot_sha256: 0423117e25af1f496dd7ed7beb78a8083a27d47a24dfadf88c2df26bf4c3033b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/cleavage_body.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/cleavage_body-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:31Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/cleavage_body.yaml\
    \ --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/cleavage_body-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/cleavage_body-strict.tsv"
  snapshot_sha256: 4c942a81076fbd93057f5da06ea08b25c40b3cc843c0ec76f50d9834357d1ae3
- evidence_id: native-cleavage_body-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cleavage_body.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:48:03.253869Z'
  support: supports
  summary: "data/structures/other/cleavage_body.yaml  (GO:0071920)\n  cstf_cpsf_cleavage_body_positioning\t\
    cstf64\tCOVERED\t->cstf64 (UniProtKB:P33240)\n  cstf_cpsf_cleavage_body_positioning\t\
    cpsf100\tCOVERED\t->cpsf100 (UniProtKB:Q9P2I0)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     2  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 2d29252cee7b1ea91ce00f9275b476e1114b62078722b00bcd0bee9aa6529a4d
- evidence_id: native-cleavage_body-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/cleavage_body.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:48:06.198844Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/cleavage_body.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 14 collected target identifiers returned OK. PMID:11598190: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:32816001:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:8654386: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
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
  topic: Protein-rich nuclear body with explicit marker boundaries
  outcome: supported
  target_ids:
  - GO:0071920
  summary: GO0071920, nuclear-body parent and nuclear-lumen location agree. The OTHER
    kind appropriately avoids declaring an obligate resident-RNA granule. GO definition
    language is interpreted with the maintained component-boundary TODO and graph
    caveats, not as universal DDX1 residency or demonstrated processing in every focus.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC25681
  - root47-sources-legacy-PMC1382303
  - root47-sources-legacy-PMC60154
- assessment_id: composition
  area: grounding
  topic: CPSF-100 has an exact family
  outcome: concern
  target_ids:
  - GO:0071920
  summary: CPSF2 IPR027075 is an exact whole-protein family corroborated by Q9P2I0.
    CstF-64 inspected xrefs identify hinge, C-terminal or RNA-binding domains rather
    than a demonstrated exact whole-family identity, so its unresolved grounding is
    not forced.
  evidence_ids:
  - record
  - curation
  - root47-sources-ipr-IPR027075
  - root47-sources-protein-P33240
  - root47-sources-protein-Q9P2I0
- assessment_id: examples
  area: grounding
  topic: Correct human protein examples
  outcome: supported
  target_ids:
  - GO:0071920
  summary: CSTF2/P33240 and CPSF2/Q9P2I0 are reviewed, correctly named and uniquely
    resolved by the exact gene/taxon queries. Nuclear localization evidence is not
    conflated with a complete cleavage-body assembly experiment.
  evidence_ids:
  - record
  - root47-sources-protein-P33240
  - root47-sources-protein-Q9P2I0
  - root47-sources-gene-CSTF2-9606
  - root47-sources-gene-CPSF2-9606
  - root47-sources-tax9606
  - root47-sources-pmid-11598190
  - root47-sources-pmid-32816001
- assessment_id: necessity
  area: grounding
  topic: Marker enrichment does not prove formation necessity
  outcome: unknown
  target_ids:
  - GO:0071920
  summary: CstF-64 and CPSF-100 enrichment, differing cell-cycle persistence and proximity
    measurements do not establish which factors are indispensable for the whole body
    to form. UNKNOWN remains appropriate.
  evidence_ids:
  - record
  - schema
  - root47-sources-legacy-PMC25681
  - root47-sources-legacy-PMC1382303
  - root47-sources-legacy-PMC60154
- assessment_id: scope
  area: scope
  topic: Dynamic human-cell scope with a citation-placement gap
  outcome: concern
  target_ids:
  - GO:0071920
  summary: VARIABLE is compatible with the observed cell-type and cell-cycle differences.
    The canonical note combines T24 and HeLa but cites only the T24 study; the HeLa
    source is already elsewhere in the record and should be placed with that assertion.
  evidence_ids:
  - record
  - root47-sources-legacy-PMC25681
  - root47-sources-legacy-PMC1382303
  - root47-sources-tax9606
- assessment_id: function
  area: evidence
  topic: Concentration and association, not proven local catalysis
  outcome: supported
  target_ids:
  - GO:0071920
  summary: The maintained functional description concentrates processing factors and
    states their spatial association with Cajal bodies and histone loci. This bounded
    wording fits the primary experiments, including the absence of detected RNA accumulation
    in the HeLa assays.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC25681
  - root47-sources-legacy-PMC1382303
  - root47-sources-legacy-PMC60154
- assessment_id: graph
  area: graph
  topic: Nonmechanistic localization and spatial-association graph
  outcome: supported
  target_ids:
  - GO:0071920
  summary: The graph explicitly excludes a complete condensate pathway and direct
    active processing inside the body. Directed localization, body associations and
    histone-locus overlaps are supported at the stated cell/assay level.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC25681
  - root47-sources-legacy-PMC1382303
  - root47-sources-legacy-PMC60154
  - root47-sources-pmid-8654386
- assessment_id: coverage
  area: completeness
  topic: One family and one canonical-source correction
  outcome: supported
  target_ids:
  - GO:0071920
  summary: All maintained fields and the DDX1/resident-factor TODO were reviewed.
    The body studies justify retaining the open boundary question; they do not require
    treating every neighboring focus as a constituent.
  evidence_ids:
  - record
  - root47-sources-ipr-IPR027075
  - root47-sources-legacy-PMC25681
  - root47-sources-legacy-PMC1382303
  - root47-sources-legacy-PMC60154
findings:
- finding_id: F1
  issue_key: cleavage-body-cpsf100-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the verified CPSF-100 family
  description: CPSF-100/CPSF2 remains REVIEWED_LABEL_ONLY despite exact whole-family
    IPR027075 and the independently matching Q9P2I0 example. This resolves one named
    part of the broader component-boundary TODO.
  target_ids:
  - GO:0071920
  field_paths:
  - components[1].grounding_status
  - components[1].grounding_notes
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root47-sources-ipr-IPR027075
  - root47-sources-protein-Q9P2I0
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cleavage_body.yaml
    role: maintained scientific record
  rule_id: Exact component identity and claim-specific source scope
  native_severity: minor
  normalization_reason: Bounded evidence-backed curation correction; supported structural
    identity and constituent membership remain intact. Historical search honesty is
    not questioned.
- finding_id: F2
  issue_key: cleavage-body-canonical-source-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach the HeLa source to the combined canonical example
  description: The canonical note names both T24 and HeLa but its sole reference,
    Schul1999 DOI10.1091/mbc.10.11.3815, documents the T24 experiment. Li2006 DOI10.1091/mbc.e05-08-0768
    directly supplies the HeLa experiments and already appears elsewhere in the record.
    The biological examples are supported collectively; the row-level attribution
    is incomplete.
  target_ids:
  - GO:0071920
  field_paths:
  - canonical_examples[0].note
  - canonical_examples[0].reference
  evidence_ids:
  - record
  - root47-sources-legacy-PMC25681
  - root47-sources-legacy-PMC1382303
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cleavage_body.yaml
    role: maintained scientific record
  rule_id: Exact component identity and claim-specific source scope
  native_severity: minor
  normalization_reason: Bounded evidence-backed curation correction; supported structural
    identity and constituent membership remain intact. Historical search honesty is
    not questioned.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0071920
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cleavage_body.yaml
    role: maintained scientific record
  description: Ground CPSF-100 with IPR027075 and reconcile that portion of the TODO
    while preserving unresolved CstF-64 and resident-versus-neighboring-factor questions.
  acceptance_checks:
  - Verify exact source identities and reconcile the specified current fields and
    TODO scope.
  - Preserve supported accessions and membership; retain assay, lineage and uncertainty
    limits.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0071920
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cleavage_body.yaml
    role: maintained scientific record
  description: Either narrow the existing canonical note to T24 and add a separately
    sourced HeLa entry, or use a supported evidence representation that places each
    experimental source beside its claim. Preserve their different cell-cycle and
    cell-line behavior.
  acceptance_checks:
  - Verify exact source identities and reconcile the specified current fields and
    TODO scope.
  - Preserve supported accessions and membership; retain assay, lineage and uncertainty
    limits.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw experimental data, supplementary files or sequence alignments
  were reanalyzed. Primary-body inspection is limited to the explicitly listed sections.
- Schul1996 is available as complete native metadata/abstract and a scanned legacy
  page; its full scanned article was not read. Grozdanov2020 was read at native abstract
  level only; the retained body is not certified.
- Li2006 inhibitor and latrunculin-result sections and the cited videos were not read;
  no new mechanism or complete resident-factor inventory is claimed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorizes reviews for all uncovered records, including honest zero-finding
  bundles.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
