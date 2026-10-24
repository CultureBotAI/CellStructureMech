# Checkpoint clamp complex scientific review

- Review: 20261022T050515Z-checkpoint-clamp-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:46:58Z
- Finished UTC: 2026-10-22T05:05:15Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Checkpoint-clamp identity, constituents and examples are supported. Two minor findings resolve exact subunit families and directly tested, condition-scoped formation necessity.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph claims and completeness.

Selection: Target 1 of batch47 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030896 | data/structures/other/checkpoint_clamp_complex.yaml | maintained | checkpoint clamp complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030896 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030896 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0030896 | Focused native check passed; claim-level support assessed separately. |
| Focused native verify | passed | True | GO:0030896 | Focused native check passed; claim-level support assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0030896 | No expression-module claim is maintained. |
| Claim-level scientific review | passed | True | GO:0030896 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030896 | 12 of 17 collected target identifiers returned OK. PMID:11739777: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:12531008: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:15279787: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:16823372: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:19446481: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030896 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030896 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030896 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030896 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030896 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Conserved 9-1-1 checkpoint clamp

identity: supported. Targets: GO:0030896.

The GO identity, nuclear-complex parent and Rad9-Rad1-Hus1 synonym agree. Kaur2001 directly studies the fission-yeast association; Dore2009 native abstract supplies human structural evidence and is not represented as a fission-yeast crystal structure.

### Three exact subunit families resolve the TODO

grounding: concern. Targets: GO:0030896.

Native IPR026584, IPR003011 and IPR016580 identify the Rad9, Rad1 and Hus1 classes and are cross-referenced by their exact examples. Broader PCNA/DNA-clamp folds are not used as substitute identities.

### Correct fission-yeast reference examples

grounding: supported. Targets: GO:0030896.

All three reviewed entries, symbols, query uniqueness and 972h- strain identifiers agree. The Hus1 cytoplasmic annotation is accurately attributed to the localization screen and does not exclude a nuclear clamp pool.

### Direct stability assays can refine UNKNOWN

grounding: concern. Targets: GO:0030896.

Unlike a viability or checkpoint-function assay, the normal-growth deletion/coimmunoprecipitation experiment tests stable physical association. It supports a condition-scoped requirement for each named subunit, while mutant overexpression and cross-species pairwise behavior prevent universal extrapolation.

### Species experiment versus reference-strain examples

scope: supported. Targets: GO:0030896.

The canonical and distribution assertions are species-level S.pombe, matching the varied laboratory strains in Table1. Reference protein entries use the narrower 972h- identifier. COMMON is a qualitative ordinary-machinery assessment meaning most members, not a population census.

### Checkpoint association and DNA-damage response

evidence: supported. Targets: GO:0030896.

GO and the complete Carr/Parrilla-Castellar review abstracts support the DNA-damage role and clamp-loading context. Kaur separates functional checkpoints from stable trimer association; it is not presented as a direct complete DNA-loading assay.

### Bounded constituent and checkpoint-function graph

graph: supported. Targets: GO:0030896.

NONMECHANISTIC correctly summarizes constituent contributions, DNA loading and response without inventing an RFC-like loading sequence, Rad3-Rad26 pathway or resolved Chk1 mechanism.

### Exact identity and necessity follow-up

completeness: supported. Targets: GO:0030896.

All maintained fields and source identities were checked. The three family mappings and condition-scoped assembly evidence are actionable; secondary full bodies and human structural details beyond the abstract remain unverified.

## Findings

### F1: Ground the three checkpoint-clamp subunit families

minor / open / confirmed; issue key: checkpoint-three-exact-families.

Rad9, Rad1 and Hus1 remain REVIEWED_LABEL_ONLY although IPR026584, IPR003011 and IPR016580 respectively define the whole subunit classes and are linked by their reviewed examples.

### F2: Record the directly tested requirement for stable clamp association

minor / open / confirmed; issue key: checkpoint-scoped-formation-necessity.

All three essentiality fields are UNKNOWN, but the cited Kaur2001 normal-growth deletion experiment directly shows dependence of stable Hus1-Rad1-Rad9 association on each subunit. This is resolvable formation/stability evidence, distinct from checkpoint activity or viability. The paper also reports overexpressed mutant pairwise associations and cross-species differences, so the inference must remain scoped to the measured wild-type complex and assay conditions.

## Recommended Actions And Acceptance Checks

### A1

Add the three exact family groundings and reconcile their current notes and TODO; preserve fission-yeast names and distinguish unrelated same-name proteins.

- Verify exact source identities and reconcile the specified current fields and TODO scope.
- Preserve supported accessions and membership; retain assay, lineage and uncertainty limits.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.

### A2

Curate the experimentally supported structural requirement with explicit fission-yeast normal-growth/coimmunoprecipitation context and limitations; retain the distinction between stable trimer assembly, pairwise mutant interactions and checkpoint function.

- Verify exact source identities and reconcile the specified current fields and TODO scope.
- Preserve supported accessions and membership; retain assay, lineage and uncertainty limits.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/checkpoint_clamp_complex.yaml; Entire maintained target, history, components, evidence, discussions and graphs | context_only | All maintained fields were read; history is provenance rather than independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Components, essentiality, COMMON and graph scope | context_only | Whole-protein families differ from shared domains and individual examples. Formation necessity differs from functional and cellular essentiality. COMMON means present in most members, with losses the exception. |
| curation | docs/CURATION.md; Source identity, exact grounding and claim-specific support | context_only | Reviewed label-only means no exact term exists. Verified whole-protein identity may be grounded independently of its separately evidenced role in a complex. Canonical taxon scope must match the cited experiment. |
| root47-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0006260,GO:0006338,GO:0006974,GO:0008623,GO:0015030,GO:0016604,GO:0030896,GO:0031010,GO:0031124,GO:0031261,GO:0031981,GO:0042555,GO:0071162,GO:0071920,GO:0140513; All16 requested terms: complete id/name/active/definition/synonyms/comments and relevant maintained typed links, not every descendant | supports | The requested native GO identities, definitions, synonyms and inspected maintained typed relationships agree with the target classes and functions. Missing direct ontology links alone do not disprove sourced biological parthood. |
| root47-sources-pmid-12531008 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12531008+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED12531008: DNA structure dependent checkpoints as regulators of DNA repair. DOI 10.1016/s1568-7864(02)00165-9. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-11739777 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11739777+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED11739777: Structure-function analysis of fission yeast Hus1-Rad1-Rad9 checkpoint complex. DOI 10.1091/mbc.12.12.3744. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-15279787 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15279787+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED15279787: Dial 9-1-1 for DNA damage: the Rad9-Hus1-Rad1 (9-1-1) clamp complex. DOI 10.1016/j.dnarep.2004.03.032. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-19446481 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19446481+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED19446481: Crystal structure of the rad9-rad1-hus1 DNA damage checkpoint complex--implications for clamp loading and regulation. DOI 10.1016/j.molcel.2009.04.027. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-16823372 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16823372+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED16823372: ORFeome cloning and global analysis of protein localization in the fission yeast Schizosaccharomyces pombe. DOI 10.1038/nbt1222. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-protein-P26306 | https://rest.uniprot.org/uniprotkb/P26306.json; Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro/Pfam cross-references | supports | P26306 agrees with the maintained reviewed entry, protein name, gene identity and taxon identifier. Membership and experimental source scope are assessed separately. |
| root47-sources-protein-P22193 | https://rest.uniprot.org/uniprotkb/P22193.json; Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro/Pfam cross-references | supports | P22193 agrees with the maintained reviewed entry, protein name, gene identity and taxon identifier. Membership and experimental source scope are assessed separately. |
| root47-sources-protein-P78955 | https://rest.uniprot.org/uniprotkb/P78955.json; Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro/Pfam cross-references | supports | P78955 agrees with the maintained reviewed entry, protein name, gene identity and taxon identifier. Membership and experimental source scope are assessed separately. |
| root47-sources-gene-rad9-284812 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Arad9%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and all result accession/status/name/gene/taxon fields | supports | The exact reviewed gene/taxon query returns one result, matching the maintained accession, status, names and taxon. |
| root47-sources-gene-rad1-284812 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Arad1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and all result accession/status/name/gene/taxon fields | supports | The exact reviewed gene/taxon query returns one result, matching the maintained accession, status, names and taxon. |
| root47-sources-gene-hus1-284812 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahus1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and all result accession/status/name/gene/taxon fields | supports | The exact reviewed gene/taxon query returns one result, matching the maintained accession, status, names and taxon. |
| root47-sources-tax4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; Complete native taxonomy response | supports | ENA verifies taxon 4896 and its rank, name and lineage. Species and strain identities are kept distinct. |
| root47-sources-tax284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Complete native taxonomy response | supports | ENA verifies taxon 284812 and its rank, name and lineage. Species and strain identities are kept distinct. |
| root47-sources-ipr-IPR026584 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026584/; Complete accession/name/type/description, curation flags and family metadata | supports | IPR026584 is a family named Rad9. Complete native description and its curation flags were inspected; example cross-references provide an independent identity join. This annotation is not primary evidence of complex membership. |
| root47-sources-ipr-IPR003011 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003011/; Complete accession/name/type/description, curation flags and family metadata | supports | IPR003011 is a family named Cell cycle checkpoint protein, Rad1. Complete native description and its curation flags were inspected; example cross-references provide an independent identity join. This annotation is not primary evidence of complex membership. |
| root47-sources-ipr-IPR016580 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016580/; Complete accession/name/type/description, curation flags and family metadata | supports | IPR016580 is a family named HUS1. Complete native description and its curation flags were inspected; example cross-references provide an independent identity join. This annotation is not primary evidence of complex membership. |
| root47-sources-legacy-PMC60752 | https://pmc.ncbi.nlm.nih.gov/articles/PMC60752/?report=reader; Complete Methods sec3 (Table1)/sec7, Results sec9/10 (Fig1–3 captions), Discussion sec15 including nested sec16; remaining mutation results not certified | supports | Normal-growth reciprocal immunoprecipitations compare wild type with rad9, rad1 and hus1 deletions and show that stable association requires all three subunits under those conditions. The Rad9 N-terminal fragment supports stable assembly despite checkpoint defects. The Discussion describes overexpressed Hus1 mutants with Rad1 association despite lost Rad9 coprecipitation and differing pairwise results in other species; these do not justify a universal all-conditions interaction rule. |
| schema-result | just validate data/structures/other/checkpoint_clamp_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/checkpoint_clamp_complex.yaml |
| strict-result | just validate-strict data/structures/other/checkpoint_clamp_complex.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/checkpoint_clamp_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/checkpoint_clamp_complex.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/checkpoint_clamp_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/checkpoint_clamp_complex-strict.tsv |
| native-checkpoint_clamp_complex-causal-graphs | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/checkpoint_clamp_complex.yaml; Complete focused native report | supports | data/structures/other/checkpoint_clamp_complex.yaml  (GO:0030896)<br>  checkpoint_clamp_dna_damage_response	rad9_checkpoint_clamp_subunit	COVERED	-&gt;rad9_checkpoint_clamp_subunit (UniProtKB:P26306)<br>  checkpoint_clamp_dna_damage_response	rad1_checkpoint_clamp_subunit	COVERED	-&gt;rad1_checkpoint_clamp_subunit (UniProtKB:P22193)<br>  checkpoint_clamp_dna_damage_response	hus1_checkpoint_clamp_subunit	COVERED	-&gt;hus1_checkpoint_clamp_subunit (UniProtKB:P78955)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-checkpoint_clamp_complex-verify | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/checkpoint_clamp_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/checkpoint_clamp_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 17 collected target identifiers returned OK. PMID:11739777: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:12531008: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:15279787: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:16823372: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:19446481: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw experimental data, supplementary files or sequence alignments were reanalyzed. Primary-body inspection is limited to the explicitly listed sections.
- Carr2002, Parrilla-Castellar2004, Dore2009 and Matsuyama2006 were read as complete native metadata and abstracts only. Dore describes human structure; no unaccessed figure or full-body claim is certified.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes reviews for all uncovered records, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T050515Z-checkpoint-clamp-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Checkpoint clamp complex scientific review
started_at: '2026-10-22T04:46:58Z'
finished_at: '2026-10-22T05:05:15Z'
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
summary: Checkpoint-clamp identity, constituents and examples are supported. Two minor
  findings resolve exact subunit families and directly tested, condition-scoped formation
  necessity.
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
  - path: data/structures/other/checkpoint_clamp_complex.yaml
    sha256: ca0a307eaff1114aa1125b0301c053e2681f113318ceb0ccd743d9bcb163acaf
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
- target_id: GO:0030896
  path: data/structures/other/checkpoint_clamp_complex.yaml
  label: checkpoint clamp complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/checkpoint_clamp_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph claims and completeness.
  selection: Target 1 of batch47 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030896
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030896
  command: just validate data/structures/other/checkpoint_clamp_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030896
  command: just validate-strict data/structures/other/checkpoint_clamp_complex.yaml
    --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/checkpoint_clamp_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-checkpoint_clamp_complex-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030896
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/checkpoint_clamp_complex.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-checkpoint_clamp_complex-causal-graphs
- check_id: native-checkpoint_clamp_complex-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0030896
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/checkpoint_clamp_complex.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-checkpoint_clamp_complex-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030896
  summary: No expression-module claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030896
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root47-sources-go
  - root47-sources-pmid-12531008
  - root47-sources-pmid-11739777
  - root47-sources-pmid-15279787
  - root47-sources-pmid-19446481
  - root47-sources-pmid-16823372
  - root47-sources-protein-P26306
  - root47-sources-protein-P22193
  - root47-sources-protein-P78955
  - root47-sources-gene-rad9-284812
  - root47-sources-gene-rad1-284812
  - root47-sources-gene-hus1-284812
  - root47-sources-tax4896
  - root47-sources-tax284812
  - root47-sources-ipr-IPR026584
  - root47-sources-ipr-IPR003011
  - root47-sources-ipr-IPR016580
  - root47-sources-legacy-PMC60752
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030896
  summary: '12 of 17 collected target identifiers returned OK. PMID:11739777: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:12531008:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:15279787: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force.; PMID:16823372: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport
    failure. Identity resolution does not certify every attached biological claim;
    declared abstract/body reading scope remains in force.; PMID:19446481: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root47-sources-pmid-11739777
  - root47-sources-pmid-12531008
  - root47-sources-pmid-15279787
  - root47-sources-pmid-16823372
  - root47-sources-pmid-19446481
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030896
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
  - GO:0030896
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
  - GO:0030896
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
  - GO:0030896
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
  - GO:0030896
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
  reference: data/structures/other/checkpoint_clamp_complex.yaml
  locator: Entire maintained target, history, components, evidence, discussions and
    graphs
  accessed_at: '2026-10-22T04:59:17Z'
  support: context_only
  summary: All maintained fields were read; history is provenance rather than independent
    scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Components, essentiality, COMMON and graph scope
  accessed_at: '2026-10-22T04:59:17Z'
  support: context_only
  summary: Whole-protein families differ from shared domains and individual examples.
    Formation necessity differs from functional and cellular essentiality. COMMON
    means present in most members, with losses the exception.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Source identity, exact grounding and claim-specific support
  accessed_at: '2026-10-22T04:59:17Z'
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
- evidence_id: root47-sources-pmid-12531008
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12531008+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:58.626782Z'
  support: supports
  summary: 'MED12531008: DNA structure dependent checkpoints as regulators of DNA
    repair. DOI 10.1016/s1568-7864(02)00165-9. Complete native bibliographic identity
    and abstract were inspected. This row certifies abstract-level access only; body
    inspection is recorded separately.'
  snapshot_sha256: e04eca45e01fd4bf5d0fc1dc135818278a1e967c9a24514ace811ceb6b7115e5
- evidence_id: root47-sources-pmid-11739777
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11739777+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:58.621391Z'
  support: supports
  summary: 'MED11739777: Structure-function analysis of fission yeast Hus1-Rad1-Rad9
    checkpoint complex. DOI 10.1091/mbc.12.12.3744. Complete native bibliographic
    identity and abstract were inspected. This row certifies abstract-level access
    only; body inspection is recorded separately.'
  snapshot_sha256: b27577d87004e8ef0ea73d7858b9f60f59ae9b9cbca61e4754c67cfc0248eedc
- evidence_id: root47-sources-pmid-15279787
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15279787+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:59.748510Z'
  support: supports
  summary: 'MED15279787: Dial 9-1-1 for DNA damage: the Rad9-Hus1-Rad1 (9-1-1) clamp
    complex. DOI 10.1016/j.dnarep.2004.03.032. Complete native bibliographic identity
    and abstract were inspected. This row certifies abstract-level access only; body
    inspection is recorded separately.'
  snapshot_sha256: de3d40f27424173eb694dbb46aa966de1d2296b8e908f498439cf652dea1ec07
- evidence_id: root47-sources-pmid-19446481
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19446481+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:48:00.519617Z'
  support: supports
  summary: 'MED19446481: Crystal structure of the rad9-rad1-hus1 DNA damage checkpoint
    complex--implications for clamp loading and regulation. DOI 10.1016/j.molcel.2009.04.027.
    Complete native bibliographic identity and abstract were inspected. This row certifies
    abstract-level access only; body inspection is recorded separately.'
  snapshot_sha256: 3767aca11ad4d11f7fa091355c30a3ed8433cdf89640dd72406bd406c7507820
- evidence_id: root47-sources-pmid-16823372
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16823372+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:59.791562Z'
  support: supports
  summary: 'MED16823372: ORFeome cloning and global analysis of protein localization
    in the fission yeast Schizosaccharomyces pombe. DOI 10.1038/nbt1222. Complete
    native bibliographic identity and abstract were inspected. This row certifies
    abstract-level access only; body inspection is recorded separately.'
  snapshot_sha256: bc97fb418a2596aeb5ce583afd10616b89a5b71b7d3e4557d84e566c4a67a992
- evidence_id: root47-sources-protein-P26306
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P26306.json
  locator: Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION and SIMILARITY comments; InterPro/Pfam cross-references
  accessed_at: '2026-10-22T04:47:54.056161Z'
  support: supports
  summary: P26306 agrees with the maintained reviewed entry, protein name, gene identity
    and taxon identifier. Membership and experimental source scope are assessed separately.
  snapshot_sha256: ce4062bbe7024b8b0a58046d325279690ae0301c356e4cbabc27750393e2bd99
- evidence_id: root47-sources-protein-P22193
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P22193.json
  locator: Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION and SIMILARITY comments; InterPro/Pfam cross-references
  accessed_at: '2026-10-22T04:47:54.054142Z'
  support: supports
  summary: P22193 agrees with the maintained reviewed entry, protein name, gene identity
    and taxon identifier. Membership and experimental source scope are assessed separately.
  snapshot_sha256: 141b523ceebc3f170b48de6aed1da3d0411649bd65c10886222d14819e1391b2
- evidence_id: root47-sources-protein-P78955
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P78955.json
  locator: Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION and SIMILARITY comments; InterPro/Pfam cross-references
  accessed_at: '2026-10-22T04:47:54.910538Z'
  support: supports
  summary: P78955 agrees with the maintained reviewed entry, protein name, gene identity
    and taxon identifier. Membership and experimental source scope are assessed separately.
  snapshot_sha256: 961fe8a81c39d3a9e43e6d427f561ab139044c1360d65002acdeecd69d55620c
- evidence_id: root47-sources-gene-rad9-284812
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Arad9%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and all result accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:48:48.271415Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one result, matching the maintained
    accession, status, names and taxon.
  snapshot_sha256: 41ff970f47682adf73b931c2bc321c1ae77d0365ee85dfebb4e508f741a4b0f9
- evidence_id: root47-sources-gene-rad1-284812
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Arad1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and all result accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:48:48.321627Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one result, matching the maintained
    accession, status, names and taxon.
  snapshot_sha256: 6474aa42565471c2f650fce0cd2f470ef1c606fca5daf3710440913bbc8b7568
- evidence_id: root47-sources-gene-hus1-284812
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahus1%29+AND+%28organism_id%3A284812%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and all result accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:48:48.721845Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one result, matching the maintained
    accession, status, names and taxon.
  snapshot_sha256: e8f58cec29a9357466dbdd3bc5e25a9b691f2ffbd59443e552de7819b765f4d8
- evidence_id: root47-sources-tax4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:47:53.215328Z'
  support: supports
  summary: ENA verifies taxon 4896 and its rank, name and lineage. Species and strain
    identities are kept distinct.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: root47-sources-tax284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:47:53.215600Z'
  support: supports
  summary: ENA verifies taxon 284812 and its rank, name and lineage. Species and strain
    identities are kept distinct.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: root47-sources-ipr-IPR026584
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026584/
  locator: Complete accession/name/type/description, curation flags and family metadata
  accessed_at: '2026-10-22T04:48:46.031480Z'
  support: supports
  summary: IPR026584 is a family named Rad9. Complete native description and its curation
    flags were inspected; example cross-references provide an independent identity
    join. This annotation is not primary evidence of complex membership.
  snapshot_sha256: 5a391772ea2b1b1f9b125a79dc732ed71094f2928b79f92bbf2edd4fdb0b1078
- evidence_id: root47-sources-ipr-IPR003011
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003011/
  locator: Complete accession/name/type/description, curation flags and family metadata
  accessed_at: '2026-10-22T04:48:43.389997Z'
  support: supports
  summary: IPR003011 is a family named Cell cycle checkpoint protein, Rad1. Complete
    native description and its curation flags were inspected; example cross-references
    provide an independent identity join. This annotation is not primary evidence
    of complex membership.
  snapshot_sha256: 881ba7cc34d274485a7c6062c0e154176df252eee6f3bdb6500df00451433fa9
- evidence_id: root47-sources-ipr-IPR016580
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016580/
  locator: Complete accession/name/type/description, curation flags and family metadata
  accessed_at: '2026-10-22T04:48:45.048304Z'
  support: supports
  summary: IPR016580 is a family named HUS1. Complete native description and its curation
    flags were inspected; example cross-references provide an independent identity
    join. This annotation is not primary evidence of complex membership.
  snapshot_sha256: 84bffb1c31b8990230aaa72980532b64081d67a50fe2c083f1c2422c6796c21a
- evidence_id: root47-sources-legacy-PMC60752
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC60752/?report=reader
  locator: Complete Methods sec3 (Table1)/sec7, Results sec9/10 (Fig1–3 captions),
    Discussion sec15 including nested sec16; remaining mutation results not certified
  accessed_at: '2026-10-22T04:48:51.351010Z'
  support: supports
  summary: Normal-growth reciprocal immunoprecipitations compare wild type with rad9,
    rad1 and hus1 deletions and show that stable association requires all three subunits
    under those conditions. The Rad9 N-terminal fragment supports stable assembly
    despite checkpoint defects. The Discussion describes overexpressed Hus1 mutants
    with Rad1 association despite lost Rad9 coprecipitation and differing pairwise
    results in other species; these do not justify a universal all-conditions interaction
    rule.
  snapshot_sha256: 485fd151750959b4d2a87b3ae71776afffd05c0acd8b8252ccaa6c957a84b25b
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/checkpoint_clamp_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:00Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/checkpoint_clamp_complex.yaml'
  snapshot_sha256: 053f5974c75d9b46a611650b335d3bc817b00e26fe102ff4fc831d974cd54537
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/checkpoint_clamp_complex.yaml
    --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/checkpoint_clamp_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:03Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/checkpoint_clamp_complex.yaml\
    \ --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/checkpoint_clamp_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/checkpoint_clamp_complex-strict.tsv"
  snapshot_sha256: 433ebc7d69c48afad30095b1200b844ebe08040919b2addde1220f7497395117
- evidence_id: native-checkpoint_clamp_complex-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/checkpoint_clamp_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:47:55.735655Z'
  support: supports
  summary: "data/structures/other/checkpoint_clamp_complex.yaml  (GO:0030896)\n  checkpoint_clamp_dna_damage_response\t\
    rad9_checkpoint_clamp_subunit\tCOVERED\t->rad9_checkpoint_clamp_subunit (UniProtKB:P26306)\n\
    \  checkpoint_clamp_dna_damage_response\trad1_checkpoint_clamp_subunit\tCOVERED\t\
    ->rad1_checkpoint_clamp_subunit (UniProtKB:P22193)\n  checkpoint_clamp_dna_damage_response\t\
    hus1_checkpoint_clamp_subunit\tCOVERED\t->hus1_checkpoint_clamp_subunit (UniProtKB:P78955)\n\
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
  snapshot_sha256: 19f64374b8622995ba74b4a4e1eaac1df4e5589a7ea1957f73b6fadbecc5a520
- evidence_id: native-checkpoint_clamp_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/checkpoint_clamp_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:47:57.850027Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/checkpoint_clamp_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '12 of 17 collected target identifiers returned OK. PMID:11739777: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:12531008:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:15279787: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force.; PMID:16823372: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport
    failure. Identity resolution does not certify every attached biological claim;
    declared abstract/body reading scope remains in force.; PMID:19446481: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
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
  topic: Conserved 9-1-1 checkpoint clamp
  outcome: supported
  target_ids:
  - GO:0030896
  summary: The GO identity, nuclear-complex parent and Rad9-Rad1-Hus1 synonym agree.
    Kaur2001 directly studies the fission-yeast association; Dore2009 native abstract
    supplies human structural evidence and is not represented as a fission-yeast crystal
    structure.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC60752
  - root47-sources-pmid-19446481
- assessment_id: composition
  area: grounding
  topic: Three exact subunit families resolve the TODO
  outcome: concern
  target_ids:
  - GO:0030896
  summary: Native IPR026584, IPR003011 and IPR016580 identify the Rad9, Rad1 and Hus1
    classes and are cross-referenced by their exact examples. Broader PCNA/DNA-clamp
    folds are not used as substitute identities.
  evidence_ids:
  - record
  - curation
  - root47-sources-ipr-IPR026584
  - root47-sources-ipr-IPR003011
  - root47-sources-ipr-IPR016580
  - root47-sources-protein-P26306
  - root47-sources-protein-P22193
  - root47-sources-protein-P78955
- assessment_id: examples
  area: grounding
  topic: Correct fission-yeast reference examples
  outcome: supported
  target_ids:
  - GO:0030896
  summary: All three reviewed entries, symbols, query uniqueness and 972h- strain
    identifiers agree. The Hus1 cytoplasmic annotation is accurately attributed to
    the localization screen and does not exclude a nuclear clamp pool.
  evidence_ids:
  - record
  - root47-sources-protein-P26306
  - root47-sources-protein-P22193
  - root47-sources-protein-P78955
  - root47-sources-gene-rad9-284812
  - root47-sources-gene-rad1-284812
  - root47-sources-gene-hus1-284812
  - root47-sources-tax4896
  - root47-sources-tax284812
  - root47-sources-pmid-16823372
- assessment_id: necessity
  area: grounding
  topic: Direct stability assays can refine UNKNOWN
  outcome: concern
  target_ids:
  - GO:0030896
  summary: Unlike a viability or checkpoint-function assay, the normal-growth deletion/coimmunoprecipitation
    experiment tests stable physical association. It supports a condition-scoped requirement
    for each named subunit, while mutant overexpression and cross-species pairwise
    behavior prevent universal extrapolation.
  evidence_ids:
  - record
  - schema
  - root47-sources-legacy-PMC60752
- assessment_id: scope
  area: scope
  topic: Species experiment versus reference-strain examples
  outcome: supported
  target_ids:
  - GO:0030896
  summary: The canonical and distribution assertions are species-level S.pombe, matching
    the varied laboratory strains in Table1. Reference protein entries use the narrower
    972h- identifier. COMMON is a qualitative ordinary-machinery assessment meaning
    most members, not a population census.
  evidence_ids:
  - record
  - schema
  - root47-sources-legacy-PMC60752
  - root47-sources-tax4896
  - root47-sources-tax284812
- assessment_id: function
  area: evidence
  topic: Checkpoint association and DNA-damage response
  outcome: supported
  target_ids:
  - GO:0030896
  summary: GO and the complete Carr/Parrilla-Castellar review abstracts support the
    DNA-damage role and clamp-loading context. Kaur separates functional checkpoints
    from stable trimer association; it is not presented as a direct complete DNA-loading
    assay.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC60752
  - root47-sources-pmid-12531008
  - root47-sources-pmid-15279787
- assessment_id: graph
  area: graph
  topic: Bounded constituent and checkpoint-function graph
  outcome: supported
  target_ids:
  - GO:0030896
  summary: NONMECHANISTIC correctly summarizes constituent contributions, DNA loading
    and response without inventing an RFC-like loading sequence, Rad3-Rad26 pathway
    or resolved Chk1 mechanism.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC60752
  - root47-sources-pmid-15279787
- assessment_id: coverage
  area: completeness
  topic: Exact identity and necessity follow-up
  outcome: supported
  target_ids:
  - GO:0030896
  summary: All maintained fields and source identities were checked. The three family
    mappings and condition-scoped assembly evidence are actionable; secondary full
    bodies and human structural details beyond the abstract remain unverified.
  evidence_ids:
  - record
  - root47-sources-ipr-IPR026584
  - root47-sources-ipr-IPR003011
  - root47-sources-ipr-IPR016580
  - root47-sources-legacy-PMC60752
  - root47-sources-pmid-12531008
  - root47-sources-pmid-11739777
  - root47-sources-pmid-15279787
  - root47-sources-pmid-19446481
  - root47-sources-pmid-16823372
findings:
- finding_id: F1
  issue_key: checkpoint-three-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the three checkpoint-clamp subunit families
  description: Rad9, Rad1 and Hus1 remain REVIEWED_LABEL_ONLY although IPR026584,
    IPR003011 and IPR016580 respectively define the whole subunit classes and are
    linked by their reviewed examples.
  target_ids:
  - GO:0030896
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - components[2].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root47-sources-ipr-IPR026584
  - root47-sources-ipr-IPR003011
  - root47-sources-ipr-IPR016580
  - root47-sources-protein-P26306
  - root47-sources-protein-P22193
  - root47-sources-protein-P78955
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/checkpoint_clamp_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and claim-specific source scope
  native_severity: minor
  normalization_reason: Bounded evidence-backed curation correction; supported structural
    identity and constituent membership remain intact. Historical search honesty is
    not questioned.
- finding_id: F2
  issue_key: checkpoint-scoped-formation-necessity
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Record the directly tested requirement for stable clamp association
  description: All three essentiality fields are UNKNOWN, but the cited Kaur2001 normal-growth
    deletion experiment directly shows dependence of stable Hus1-Rad1-Rad9 association
    on each subunit. This is resolvable formation/stability evidence, distinct from
    checkpoint activity or viability. The paper also reports overexpressed mutant
    pairwise associations and cross-species differences, so the inference must remain
    scoped to the measured wild-type complex and assay conditions.
  target_ids:
  - GO:0030896
  field_paths:
  - components[0].essentiality
  - components[1].essentiality
  - components[2].essentiality
  evidence_ids:
  - record
  - schema
  - root47-sources-legacy-PMC60752
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/checkpoint_clamp_complex.yaml
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
  - GO:0030896
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/checkpoint_clamp_complex.yaml
    role: maintained scientific record
  description: Add the three exact family groundings and reconcile their current notes
    and TODO; preserve fission-yeast names and distinguish unrelated same-name proteins.
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
  - GO:0030896
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/checkpoint_clamp_complex.yaml
    role: maintained scientific record
  description: Curate the experimentally supported structural requirement with explicit
    fission-yeast normal-growth/coimmunoprecipitation context and limitations; retain
    the distinction between stable trimer assembly, pairwise mutant interactions and
    checkpoint function.
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
- Carr2002, Parrilla-Castellar2004, Dore2009 and Matsuyama2006 were read as complete
  native metadata and abstracts only. Dore describes human structure; no unaccessed
  figure or full-body claim is certified.
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
