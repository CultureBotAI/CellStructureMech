# Scientific review of mitosome envelope

- Review: 20261022T023317Z-mitosome-envelope-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:18:54Z
- Finished UTC: 2026-10-22T02:33:17Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact mitosome-envelope identity and topology are supported. One major finding concerns whole-membrane lipid groundings; one minor finding corrects the cited12922 article title.

## Scope And Provenance

One complete maintained record at the frozen f97b1abe base; exact native identities, source claim boundaries and molecular/graph representation assessed.

Selection: Batch33 fixed strict path-order selection, one maintained target only.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:mitosome_envelope | data/structures/membrane_organelle/mitosome_envelope.yaml | maintained | mitosome envelope |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:mitosome_envelope | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:mitosome_envelope | Focused validator passed. |
| Native focused causal | passed | True | cellstructuremech:mitosome_envelope | Focused native command completed successfully; scientific scope is assessed separately. |
| Expression-module applicability | not_applicable | False | cellstructuremech:mitosome_envelope | No expression-module or transcriptomic-regulon claim; structural microscopy and perturbations do not require an expression-module lookup. |
| Claim-level scientific review | passed | True | cellstructuremech:mitosome_envelope | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | cellstructuremech:mitosome_envelope | 12 of 16 collected target identifiers returned OK. cellstructuremech:mitosome_envelope: SKIPPED; Exact local identifier and label mitosome envelope resolve to the frozen maintained data/structures/membrane_organelle/mitosome_envelope.yaml; definition and boundary relations were read, with exact UniProt SL correspondence inspected. Ignored-inclusive anchored identifier search uniquely resolves this record. This resolves identity only, not all scientific claims of the neighboring record.; cellstructuremech:mitosome_inner_membrane: SKIPPED; Exact local identifier and label mitosome inner membrane resolve to the frozen maintained data/structures/membrane_organelle/mitosome_inner_membrane.yaml; definition and boundary relations were read, with exact UniProt SL correspondence inspected. Ignored-inclusive anchored identifier search uniquely resolves this record. This resolves identity only, not all scientific claims of the neighboring record.; cellstructuremech:mitosome_intermembrane_space: SKIPPED; Exact local identifier and label mitosome intermembrane space resolve to the frozen maintained data/structures/membrane_organelle/mitosome_intermembrane_space.yaml; definition and boundary relations were read, with exact UniProt SL correspondence inspected. Ignored-inclusive anchored identifier search uniquely resolves this record. This resolves identity only, not all scientific claims of the neighboring record.; cellstructuremech:mitosome_outer_membrane: SKIPPED; Exact local identifier and label mitosome outer membrane resolve to the frozen maintained data/structures/membrane_organelle/mitosome_outer_membrane.yaml; definition and boundary relations were read, with exact UniProt SL correspondence inspected. Ignored-inclusive anchored identifier search uniquely resolves this record. This resolves identity only, not all scientific claims of the neighboring record. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | cellstructuremech:mitosome_envelope | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:mitosome_envelope | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:mitosome_envelope | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:mitosome_envelope | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | cellstructuremech:mitosome_envelope | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact mitosomal compartment

identity: supported. Targets: cellstructuremech:mitosome_envelope.

GO0032047 identifies the mitosome. The envelope local identity is anchored by exact UniProtSL0438, with inner/outer membranes and intermembrane space separately resolved. GO0031967 supplies an organelle-envelope parent for that local class. Supported identity/topology is distinct from an assertion that all mitosomes use one metabolic system.

### Verified taxa and limits of source coverage

scope: unknown. Targets: cellstructuremech:mitosome_envelope.

Native taxon identities match, including the Giardia duodenalis/intestinalis naming equivalence where relevant. The listed studies support examples rather than numerical Eukaryota prevalence. The DOI12922 abstract does not verify the broad rare-mitosome distribution rationale, and Tovar1999 abstract-only access does not establish the specific attributed double-membrane observation.

### Formation necessity

grounding: unknown. Targets: cellstructuremech:mitosome_envelope.

Component essentiality is UNKNOWN. Functional replacement, protein import or organism viability cannot be promoted to organelle-formation necessity; no unsupported ESSENTIAL label is present.

### Anatomical membranes versus lipid building blocks

grounding: concern. Targets: cellstructuremech:mitosome_envelope.

Both molecular LIPID rows ground to exact local records for whole membranes. Their graph component_ref joins repeat this mismatch. The correct has_part links, STRUCTURE node groundings and four-edge NONMECHANISTIC topology remain supported.

### Envelope topology and protein-import boundary

scope: supported. Targets: cellstructuremech:mitosome_envelope.

Exact SL definitions support the inner/outer/IMS relationships and compartmentalization. Dolezal establishes N-terminally targeted cargo crossing the boundary; the wording can denote this supported subset and does not explicitly say all cargo uses N-terminal signals. Internal-signal targeting is preserved as a scope limit, not converted into a forced contrary finding.

### Exact12922 source identity

evidence: concern. Targets: cellstructuremech:mitosome_envelope.

The12922 DOI identifies The hydrogenosome of Trichomonas vaginalis. The supplied Hydrogenosomes and mitosomes title is a different bibliographic description; this is a certain bounded citation-label error, not proof that mitosome occurrence itself is false.

### Complete bounded target coverage

completeness: supported. Targets: cellstructuremech:mitosome_envelope.

Identity, hierarchy, scoped molecular components, taxonomy, functions, every graph edge and historical discussions were assessed. Resolved historical missing-child wording is not treated as a current absence claim. No images, quantitative properties, verbatim snippets or existing UniProt protein instances occur on this target; no optional example inventory is made mandatory.

## Findings

### F1: Separate whole mitosome membranes from lipid molecular components

major / open / confirmed; issue key: mitosome-envelope-1.

The outer and inner membrane rows are typed LIPID but grounded to cellstructuremech:mitosome_outer_membrane and cellstructuremech:mitosome_inner_membrane, complete anatomical structures established by their exact UniProt locations and frozen neighbor definitions. These are not lipid chemical classes under the molecular-component contract. The corresponding graph nodes reference the mismatched molecular rows even though their STRUCTURE identities and topology are correct.

### F2: Correct the title attached to DOI10.1111/jeu.12922

minor / open / confirmed; issue key: mitosome-envelope-2.

The target labels DOI10.1111/jeu.12922 as Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes. Native bibliographic metadata identifies The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). Its full-body applicability to mitosome distribution remains unverified; the article title is definitively wrong.

## Recommended Actions And Acceptance Checks

### A1

Keep the exact anatomical has_part links and STRUCTURE nodes. Remove whole-membrane molecular rows or replace them with independently supported lipid classes and appropriate chemical or justified label-only identity; reconcile component_ref references.

- Preserve the supported biological scope and source experimental conditions.
- Run focused native schema, strict and applicable graph/protein checks after separately authorized curation.

### A2

Correct the bibliographic title/authorship for the retained DOI. Independently verify or replace the source used for broad mitosome-distribution claims without treating unread full text as proof of absence.

- Preserve the supported biological scope and source experimental conditions.
- Run focused native schema, strict and applicable graph/protein checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/mitosome_envelope.yaml; Entire maintained YAML, all components, functions, graph nodes/edges, discussions and history | context_only | Entire target inspected without modifying scientific content. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent description/grounding and essentiality; graph actor and component_ref semantics | context_only | Components denote molecular building blocks. A LIPID grounding denotes a chemical class, whereas GO/local whole-membrane records denote structures. Essentiality concerns formation, not catalytic importance or organism viability. |
| curation | docs/CURATION.md; Components section | context_only | Molecular constituents and machinery acting on an assembled structure are distinct; formation necessity is separate from function. |
| mitosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005739,GO:0043231,GO:0005740,GO:0005741,GO:0005743,GO:0005759,GO:0005742,GO:0006119,GO:0030150,GO:0032047,GO:0005737,GO:0031967; Complete twelve returned entries; specific target/parent entries and relevant children relations; no is_a inferred from mixed relation ancestry. | supports | Twelve active native GO entries checked for exact identifiers, definitions, synonym scopes and returned relation types. Mitochondrion and mitosome are is_a children of intracellular membrane-bounded organelle; mitosome is a part_of child of cytoplasm. Whole membranes and envelope remain cellular structures, not lipid chemical identities. The mitosome definition reproduces the current GO wording, including its broad Fe-S statement. |
| mitosome-agent-tax2759 | https://rest.uniprot.org/taxonomy/2759.json; taxonId, scientificName, rank, active, synonyms/otherNames; taxonomy identity | supports | Eukaryota is an active domain. Native identity does not independently measure prevalence. |
| mitosome-agent-tax5759 | https://rest.uniprot.org/taxonomy/5759.json; taxonId, scientificName, rank, active, synonyms/otherNames; taxonomy identity | supports | Entamoeba histolytica is an active species. Native identity does not independently measure prevalence. |
| mitosome-agent-SL0438 | https://rest.uniprot.org/locations/SL-0438.json; Complete JSON entry and nested isA/partOf records; current protein counts are not used as completeness evidence. | supports | Exact UniProt location identity, definition, synonyms and returned isA/partOf relations checked. These entries denote anatomical compartments; embedded parent descriptions also state genome absence and mitochondrial derivation. |
| mitosome-agent-SL0439 | https://rest.uniprot.org/locations/SL-0439.json; Complete JSON entry and nested isA/partOf records; current protein counts are not used as completeness evidence. | supports | Exact UniProt location identity, definition, synonyms and returned isA/partOf relations checked. These entries denote anatomical compartments; embedded parent descriptions also state genome absence and mitochondrial derivation. |
| mitosome-agent-SL0440 | https://rest.uniprot.org/locations/SL-0440.json; Complete JSON entry and nested isA/partOf records; current protein counts are not used as completeness evidence. | supports | Exact UniProt location identity, definition, synonyms and returned isA/partOf relations checked. These entries denote anatomical compartments; embedded parent descriptions also state genome absence and mitochondrial derivation. |
| mitosome-agent-SL0443 | https://rest.uniprot.org/locations/SL-0443.json; Complete JSON entry and nested isA/partOf records; current protein counts are not used as completeness evidence. | supports | Exact UniProt location identity, definition, synonyms and returned isA/partOf relations checked. These entries denote anatomical compartments; embedded parent descriptions also state genome absence and mitochondrial derivation. |
| mitosome-agent-tovar1999-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1046/j.1365-2958.1999.01414.x&amp;format=json&amp;resultType=core; Complete resultList.result[0] bibliographic identity and abstractText; abstract-only source tier where full-body evidence is not separately listed. | supports | Exact DOI, PMID, title, authors, year and entire abstract checked. CPN60 localization and deletion/replacement targeting assays support the Entamoeba mitochondrial-remnant identity. The abstract does not document its membrane ultrastructure. |
| mitosome-agent-tovar2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature01945&amp;format=json&amp;resultType=core; Complete resultList.result[0] bibliographic identity and abstractText; abstract-only source tier where full-body evidence is not separately listed. | supports | Exact DOI, PMID, title, authors, year and entire abstract checked. The abstract explicitly reports Giardia double membranes, IscS/IscU localization and an in-vitro reconstitution assay; detailed Methods/Results were not accessible. |
| mitosome-agent-dolezal2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0500349102; Complete resultList.result[0] bibliographic identity and abstractText; abstract-only source tier where full-body evidence is not separately listed. | supports | Exact DOI, PMID, title, authors, year and entire abstract checked. |
| mitosome-agent-tachezy2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/jeu.12922; Complete resultList.result[0] bibliographic identity and abstractText; abstract-only source tier where full-body evidence is not separately listed. | supports | Exact DOI, PMID, title, authors, year and entire abstract checked. DOI10.1111/jeu.12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdy, not the title given in the target. Its abstract concerns hydrogenosomes; a broad mitosome taxonomic synthesis is not established by this access. |
| mitosome-agent-dolezal2005-pmc | https://pmc.ncbi.nlm.nih.gov/articles/1182405/; Complete Materials and Methods sec1, Results sec2 and Discussion sec3, including Fig1-5 captions. Supplements and image pixels not independently inspected. | supports | Giardia WB localization, subcellular fractions and immuno-EM support import of IscU/IscS/ferredoxin into double-membrane mitosomes. IscU and ferredoxin use N-terminal signals; IscS uses internal signals, with both truncated halves tested in Trichomonas T1 hydrogenosomes. Pam18/MPP localization supports homologous machinery, but the paper explicitly lacked an assay dissecting Pam18 function. No molecular translocase complex was reconstituted here. |
| access-tovar1999-publisher | https://doi.org/10.1046/j.1365-2958.1999.01414.x; Exact retained response; HTTP status 403; 5681 bytes | context_only | Wiley403 response, not a primary article body. The native complete abstract was inspected separately. |
| access-tovar1999-pdf | https://onlinelibrary.wiley.com/doi/pdf/10.1046/j.1365-2958.1999.01414.x; Exact retained response; HTTP status 403; 5693 bytes | context_only | Wiley PDF route also returned403 HTML, not a PDF. No full Tovar1999 Methods/ultrastructure reading is claimed. |
| access-tovar2003-publisher | https://doi.org/10.1038/nature01945; Exact retained response; HTTP status 200; 315684 bytes | context_only | Publisher HTTP200 page inspected for title, complete abstract and access boundary. Main Results/Methods are behind the access section; markup size is not evidence of full text. |
| access-tovar2003-pdf | https://www.nature.com/articles/nature01945.pdf; Exact retained response; HTTP status 200; 315684 bytes | context_only | The PDF URL returned HTTP200 HTML with abstract/access options, not a PDF or readable primary main body. |
| access-tachezy2022-publisher | https://onlinelibrary.wiley.com/doi/10.1111/jeu.12922; Exact retained response; HTTP status 403; 5594 bytes | context_only | Retained prior access attempt, status 403; no genuine full review body was established from this response. Original source timestamp and bytes retained. |
| access-tachezy2022-pdf | https://onlinelibrary.wiley.com/doi/pdf/10.1111/jeu.12922; Exact retained response; HTTP status 403; 5606 bytes | context_only | Retained prior access attempt, status 403; no genuine full review body was established from this response. Original source timestamp and bytes retained. |
| access-tachezy2022-rg-pdf | https://www.researchgate.net/profile/Ivan-Hrdy/publication/360605238_The_hydrogenosome_of_Trichomonas_vaginalis/links/66fa5b6ab753fa724d4ffa69/The-hydrogenosome-of-Trichomonas-vaginalis.pdf; Exact retained response; HTTP status 403; 779 bytes | context_only | Retained prior access attempt, status 403; no genuine full review body was established from this response. Original source timestamp and bytes retained. |
| boundary | data/structures/membrane_organelle/mitosome.yaml; Frozen neighbor identity, definition/source, parent_structures, part_of, has_part and xrefs only | context_only | Local envelope/matrix or inner/outer/intermembrane-space identifiers resolve against the exact inspected neighboring records. Only their boundary fields informed this judgment; the maintained target remains the sole reviewed record. |
| schema-result | just validate data/structures/membrane_organelle/mitosome_envelope.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/mitosome_envelope.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/mitosome_envelope.yaml --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitosome_envelope-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitosome_envelope.yaml --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitosome_envelope-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitosome_envelope-strict.tsv |
| focused-causal | /private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/mitosome_envelope.yaml; /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitosome-agent/mitosome_envelope-causal.log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/mitosome_envelope.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 16 collected target identifiers returned OK. cellstructuremech:mitosome_envelope: SKIPPED; Exact local identifier and label mitosome envelope resolve to the frozen maintained data/structures/membrane_organelle/mitosome_envelope.yaml; definition and boundary relations were read, with exact UniProt SL correspondence inspected. Ignored-inclusive anchored identifier search uniquely resolves this record. This resolves identity only, not all scientific claims of the neighboring record.; cellstructuremech:mitosome_inner_membrane: SKIPPED; Exact local identifier and label mitosome inner membrane resolve to the frozen maintained data/structures/membrane_organelle/mitosome_inner_membrane.yaml; definition and boundary relations were read, with exact UniProt SL correspondence inspected. Ignored-inclusive anchored identifier search uniquely resolves this record. This resolves identity only, not all scientific claims of the neighboring record.; cellstructuremech:mitosome_intermembrane_space: SKIPPED; Exact local identifier and label mitosome intermembrane space resolve to the frozen maintained data/structures/membrane_organelle/mitosome_intermembrane_space.yaml; definition and boundary relations were read, with exact UniProt SL correspondence inspected. Ignored-inclusive anchored identifier search uniquely resolves this record. This resolves identity only, not all scientific claims of the neighboring record.; cellstructuremech:mitosome_outer_membrane: SKIPPED; Exact local identifier and label mitosome outer membrane resolve to the frozen maintained data/structures/membrane_organelle/mitosome_outer_membrane.yaml; definition and boundary relations were read, with exact UniProt SL correspondence inspected. Ignored-inclusive anchored identifier search uniquely resolves this record. This resolves identity only, not all scientific claims of the neighboring record. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Tovar1999, Tovar2003 and Williams2002 where applicable were inspected through exact complete native abstracts; blocked/subscription responses are retained and no unread full Methods or membrane-ultrastructure panels are certified.
- DOI12922 is verified bibliographically and through its abstract only. Retained failed public routes do not prove the full review lacks a particular statement.
- Dolezal uses Giardia WB and Trichomonas T1; the IscS-half targeting experiment is heterologous hydrogenosomal targeting. N-terminal signals are a supported route, not a universal requirement.
- No source figure pixels, raw data or supplemental experiments were reanalyzed. Goldberg main text/captions and appended Methods were read for the whole mitosome target only.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T023317Z-mitosome-envelope-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Scientific review of mitosome envelope
started_at: '2026-10-22T02:18:54Z'
finished_at: '2026-10-22T02:33:17Z'
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
summary: The exact mitosome-envelope identity and topology are supported. One major
  finding concerns whole-membrane lipid groundings; one minor finding corrects the
  cited12922 article title.
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
  - path: data/structures/membrane_organelle/mitosome.yaml
    sha256: 6c663b4b22120c931071ef1b26da5d7859ec9b98cfbda7631cda2d2425ffd59f
    role: context
  - path: data/structures/membrane_organelle/mitosome_envelope.yaml
    sha256: 762b8bad522664b480655908ccd92a258624f836a99d3e78232fe1e30aea8fc9
    role: target
  - path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    sha256: 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35
    role: context
  - path: data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
    sha256: c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95
    role: context
  - path: data/structures/membrane_organelle/mitosome_outer_membrane.yaml
    sha256: 8c9ed412d5d033717ea703db6c61c6960078608448a4cc6a57743a0ed37b7a58
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
- target_id: cellstructuremech:mitosome_envelope
  path: data/structures/membrane_organelle/mitosome_envelope.yaml
  label: mitosome envelope
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_envelope.yaml
    role: maintained scientific record
scope:
  description: One complete maintained record at the frozen f97b1abe base; exact native
    identities, source claim boundaries and molecular/graph representation assessed.
  selection: Batch33 fixed strict path-order selection, one maintained target only.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:mitosome_envelope
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_envelope
  command: just validate data/structures/membrane_organelle/mitosome_envelope.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_envelope
  command: just validate-strict data/structures/membrane_organelle/mitosome_envelope.yaml
    --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitosome_envelope-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: focused-causal
  name: Native focused causal
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_envelope
  command: /private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/mitosome_envelope.yaml
  exit_code: 0
  summary: Focused native command completed successfully; scientific scope is assessed
    separately.
  evidence_ids:
  - focused-causal
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:mitosome_envelope
  summary: No expression-module or transcriptomic-regulon claim; structural microscopy
    and perturbations do not require an expression-module lookup.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_envelope
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - mitosome-agent-go
  - mitosome-agent-tax2759
  - mitosome-agent-tax5759
  - mitosome-agent-SL0438
  - mitosome-agent-SL0439
  - mitosome-agent-SL0440
  - mitosome-agent-SL0443
  - mitosome-agent-tovar1999-meta
  - mitosome-agent-tovar2003-meta
  - mitosome-agent-dolezal2005-meta
  - mitosome-agent-tachezy2022-meta
  - mitosome-agent-dolezal2005-pmc
  - access-tovar1999-publisher
  - access-tovar1999-pdf
  - access-tovar2003-publisher
  - access-tovar2003-pdf
  - access-tachezy2022-publisher
  - access-tachezy2022-pdf
  - access-tachezy2022-rg-pdf
  - boundary
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_envelope
  summary: '12 of 16 collected target identifiers returned OK. cellstructuremech:mitosome_envelope:
    SKIPPED; Exact local identifier and label mitosome envelope resolve to the frozen
    maintained data/structures/membrane_organelle/mitosome_envelope.yaml; definition
    and boundary relations were read, with exact UniProt SL correspondence inspected.
    Ignored-inclusive anchored identifier search uniquely resolves this record. This
    resolves identity only, not all scientific claims of the neighboring record.;
    cellstructuremech:mitosome_inner_membrane: SKIPPED; Exact local identifier and
    label mitosome inner membrane resolve to the frozen maintained data/structures/membrane_organelle/mitosome_inner_membrane.yaml;
    definition and boundary relations were read, with exact UniProt SL correspondence
    inspected. Ignored-inclusive anchored identifier search uniquely resolves this
    record. This resolves identity only, not all scientific claims of the neighboring
    record.; cellstructuremech:mitosome_intermembrane_space: SKIPPED; Exact local
    identifier and label mitosome intermembrane space resolve to the frozen maintained
    data/structures/membrane_organelle/mitosome_intermembrane_space.yaml; definition
    and boundary relations were read, with exact UniProt SL correspondence inspected.
    Ignored-inclusive anchored identifier search uniquely resolves this record. This
    resolves identity only, not all scientific claims of the neighboring record.;
    cellstructuremech:mitosome_outer_membrane: SKIPPED; Exact local identifier and
    label mitosome outer membrane resolve to the frozen maintained data/structures/membrane_organelle/mitosome_outer_membrane.yaml;
    definition and boundary relations were read, with exact UniProt SL correspondence
    inspected. Ignored-inclusive anchored identifier search uniquely resolves this
    record. This resolves identity only, not all scientific claims of the neighboring
    record. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - record
  - boundary
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_envelope
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch33 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_envelope
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch33 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_envelope
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch33 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_envelope
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch33 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_envelope
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
    and current batch33 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_envelope.yaml
  locator: Entire maintained YAML, all components, functions, graph nodes/edges, discussions
    and history
  accessed_at: '2026-10-22T02:27:57Z'
  support: context_only
  summary: Entire target inspected without modifying scientific content.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent description/grounding and essentiality; graph actor
    and component_ref semantics
  accessed_at: '2026-10-22T02:27:57Z'
  support: context_only
  summary: Components denote molecular building blocks. A LIPID grounding denotes
    a chemical class, whereas GO/local whole-membrane records denote structures. Essentiality
    concerns formation, not catalytic importance or organism viability.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components section
  accessed_at: '2026-10-22T02:27:57Z'
  support: context_only
  summary: Molecular constituents and machinery acting on an assembled structure are
    distinct; formation necessity is separate from function.
- evidence_id: mitosome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005739,GO:0043231,GO:0005740,GO:0005741,GO:0005743,GO:0005759,GO:0005742,GO:0006119,GO:0030150,GO:0032047,GO:0005737,GO:0031967
  locator: Complete twelve returned entries; specific target/parent entries and relevant
    children relations; no is_a inferred from mixed relation ancestry.
  accessed_at: '2026-10-22T02:23:06.014793Z'
  support: supports
  summary: Twelve active native GO entries checked for exact identifiers, definitions,
    synonym scopes and returned relation types. Mitochondrion and mitosome are is_a
    children of intracellular membrane-bounded organelle; mitosome is a part_of child
    of cytoplasm. Whole membranes and envelope remain cellular structures, not lipid
    chemical identities. The mitosome definition reproduces the current GO wording,
    including its broad Fe-S statement.
  snapshot_sha256: 2416968b432f819ccb69ee2cb039f135911d631e025817407654ef739c5d239c
- evidence_id: mitosome-agent-tax2759
  kind: database
  reference: https://rest.uniprot.org/taxonomy/2759.json
  locator: taxonId, scientificName, rank, active, synonyms/otherNames; taxonomy identity
  accessed_at: '2026-10-22T02:23:03.577699Z'
  support: supports
  summary: Eukaryota is an active domain. Native identity does not independently measure
    prevalence.
  snapshot_sha256: af5ba762219fdecb11d214126bb8184c0eb28fc6474d14777c4aaa7f7dd89369
- evidence_id: mitosome-agent-tax5759
  kind: database
  reference: https://rest.uniprot.org/taxonomy/5759.json
  locator: taxonId, scientificName, rank, active, synonyms/otherNames; taxonomy identity
  accessed_at: '2026-10-22T02:23:04.665391Z'
  support: supports
  summary: Entamoeba histolytica is an active species. Native identity does not independently
    measure prevalence.
  snapshot_sha256: c3e1193b8db9c26e67399e29fe6c58a9fd849517b36f3fc3125cd2974d635b32
- evidence_id: mitosome-agent-SL0438
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0438.json
  locator: Complete JSON entry and nested isA/partOf records; current protein counts
    are not used as completeness evidence.
  accessed_at: '2026-10-22T02:23:05.250737Z'
  support: supports
  summary: Exact UniProt location identity, definition, synonyms and returned isA/partOf
    relations checked. These entries denote anatomical compartments; embedded parent
    descriptions also state genome absence and mitochondrial derivation.
  snapshot_sha256: a74bbec342759e1d7c209e2d408a5dac8b077776c4a482b83b5d128d4c942895
- evidence_id: mitosome-agent-SL0439
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0439.json
  locator: Complete JSON entry and nested isA/partOf records; current protein counts
    are not used as completeness evidence.
  accessed_at: '2026-10-22T02:23:05.402199Z'
  support: supports
  summary: Exact UniProt location identity, definition, synonyms and returned isA/partOf
    relations checked. These entries denote anatomical compartments; embedded parent
    descriptions also state genome absence and mitochondrial derivation.
  snapshot_sha256: aa08a6ef2b2463cf77e08466169f334ff002b0ed4c1aa82f85d4ff285dcf922b
- evidence_id: mitosome-agent-SL0440
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0440.json
  locator: Complete JSON entry and nested isA/partOf records; current protein counts
    are not used as completeness evidence.
  accessed_at: '2026-10-22T02:23:05.509314Z'
  support: supports
  summary: Exact UniProt location identity, definition, synonyms and returned isA/partOf
    relations checked. These entries denote anatomical compartments; embedded parent
    descriptions also state genome absence and mitochondrial derivation.
  snapshot_sha256: d6cdb2e1eda6f4ddf5e04ba1ad05c6105be6a430a606336ed682a6edbb1d452c
- evidence_id: mitosome-agent-SL0443
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0443.json
  locator: Complete JSON entry and nested isA/partOf records; current protein counts
    are not used as completeness evidence.
  accessed_at: '2026-10-22T02:23:05.661167Z'
  support: supports
  summary: Exact UniProt location identity, definition, synonyms and returned isA/partOf
    relations checked. These entries denote anatomical compartments; embedded parent
    descriptions also state genome absence and mitochondrial derivation.
  snapshot_sha256: c3f24e9fa67fc04328b89defb79fb3ece008eb113320b4c4f7abc99703d0b204
- evidence_id: mitosome-agent-tovar1999-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1046/j.1365-2958.1999.01414.x&format=json&resultType=core
  locator: Complete resultList.result[0] bibliographic identity and abstractText;
    abstract-only source tier where full-body evidence is not separately listed.
  accessed_at: '2026-10-22T02:23:01.552416Z'
  support: supports
  summary: Exact DOI, PMID, title, authors, year and entire abstract checked. CPN60
    localization and deletion/replacement targeting assays support the Entamoeba mitochondrial-remnant
    identity. The abstract does not document its membrane ultrastructure.
  snapshot_sha256: ead9f087057c39b9c57d53a6cd147ef8edb681d6bfd540216e1620e20716f2fb
- evidence_id: mitosome-agent-tovar2003-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature01945&format=json&resultType=core
  locator: Complete resultList.result[0] bibliographic identity and abstractText;
    abstract-only source tier where full-body evidence is not separately listed.
  accessed_at: '2026-10-22T02:23:01.553439Z'
  support: supports
  summary: Exact DOI, PMID, title, authors, year and entire abstract checked. The
    abstract explicitly reports Giardia double membranes, IscS/IscU localization and
    an in-vitro reconstitution assay; detailed Methods/Results were not accessible.
  snapshot_sha256: b12e6bd8ecfbdc81a391401a4275bb150caac2c6f6edfe6a0034f34036474ae9
- evidence_id: mitosome-agent-dolezal2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0500349102
  locator: Complete resultList.result[0] bibliographic identity and abstractText;
    abstract-only source tier where full-body evidence is not separately listed.
  accessed_at: '2026-10-22T01:40:29.610245Z'
  support: supports
  summary: Exact DOI, PMID, title, authors, year and entire abstract checked.
  snapshot_sha256: ebc78023358ad6d9ca35e7b34606dfe84cb1cac48319f509490547d40b38fdb8
- evidence_id: mitosome-agent-tachezy2022-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/jeu.12922
  locator: Complete resultList.result[0] bibliographic identity and abstractText;
    abstract-only source tier where full-body evidence is not separately listed.
  accessed_at: '2026-10-22T01:40:29.609875Z'
  support: supports
  summary: Exact DOI, PMID, title, authors, year and entire abstract checked. DOI10.1111/jeu.12922
    resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdy,
    not the title given in the target. Its abstract concerns hydrogenosomes; a broad
    mitosome taxonomic synthesis is not established by this access.
  snapshot_sha256: d04be05b15294eca215c38660eed08c45e0a78d2486043a183144b4682706944
- evidence_id: mitosome-agent-dolezal2005-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/1182405/
  locator: Complete Materials and Methods sec1, Results sec2 and Discussion sec3,
    including Fig1-5 captions. Supplements and image pixels not independently inspected.
  accessed_at: '2026-10-22T01:41:03.724804Z'
  support: supports
  summary: Giardia WB localization, subcellular fractions and immuno-EM support import
    of IscU/IscS/ferredoxin into double-membrane mitosomes. IscU and ferredoxin use
    N-terminal signals; IscS uses internal signals, with both truncated halves tested
    in Trichomonas T1 hydrogenosomes. Pam18/MPP localization supports homologous machinery,
    but the paper explicitly lacked an assay dissecting Pam18 function. No molecular
    translocase complex was reconstituted here.
  snapshot_sha256: c00dba08f0c96be17027452ba9880e94defbfe0d16acc77aab2892c54c3cbf97
- evidence_id: access-tovar1999-publisher
  kind: authority
  reference: https://doi.org/10.1046/j.1365-2958.1999.01414.x
  locator: Exact retained response; HTTP status 403; 5681 bytes
  accessed_at: '2026-10-22T02:23:01.553193Z'
  support: context_only
  summary: Wiley403 response, not a primary article body. The native complete abstract
    was inspected separately.
  snapshot_sha256: 991e82b7deb9552f9e0d9a13f6c3b66b828b4b3bdbb4b5d4f13dc0b185916a38
- evidence_id: access-tovar1999-pdf
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/pdf/10.1046/j.1365-2958.1999.01414.x
  locator: Exact retained response; HTTP status 403; 5693 bytes
  accessed_at: '2026-10-22T02:24:28.665291Z'
  support: context_only
  summary: Wiley PDF route also returned403 HTML, not a PDF. No full Tovar1999 Methods/ultrastructure
    reading is claimed.
  snapshot_sha256: d73a416866f0c5dbcc7829b88ac2040a75f3ac9b9c16ffee8c8cb3dbefe8b323
- evidence_id: access-tovar2003-publisher
  kind: authority
  reference: https://doi.org/10.1038/nature01945
  locator: Exact retained response; HTTP status 200; 315684 bytes
  accessed_at: '2026-10-22T02:23:01.553814Z'
  support: context_only
  summary: Publisher HTTP200 page inspected for title, complete abstract and access
    boundary. Main Results/Methods are behind the access section; markup size is not
    evidence of full text.
  snapshot_sha256: 142a3b3004a4eb77a06a007607c3e7cb357279b152413bce33d44deabcbe2dbc
- evidence_id: access-tovar2003-pdf
  kind: authority
  reference: https://www.nature.com/articles/nature01945.pdf
  locator: Exact retained response; HTTP status 200; 315684 bytes
  accessed_at: '2026-10-22T02:24:28.665826Z'
  support: context_only
  summary: The PDF URL returned HTTP200 HTML with abstract/access options, not a PDF
    or readable primary main body.
  snapshot_sha256: c05d8e9d8b5e6125d8a203d48fa7cf45591b09c37a015e9ce9eb83e9522905fd
- evidence_id: access-tachezy2022-publisher
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/10.1111/jeu.12922
  locator: Exact retained response; HTTP status 403; 5594 bytes
  accessed_at: '2026-10-22T01:40:30.857706Z'
  support: context_only
  summary: Retained prior access attempt, status 403; no genuine full review body
    was established from this response. Original source timestamp and bytes retained.
  snapshot_sha256: e4d24e93c0e2164b2a6f6e5c5821696fa986cb3d2ac001b49d8005f104c4ac45
- evidence_id: access-tachezy2022-pdf
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/pdf/10.1111/jeu.12922
  locator: Exact retained response; HTTP status 403; 5606 bytes
  accessed_at: '2026-10-22T01:41:03.725783Z'
  support: context_only
  summary: Retained prior access attempt, status 403; no genuine full review body
    was established from this response. Original source timestamp and bytes retained.
  snapshot_sha256: b82924736a7926aaafae1950a545054c1110e821620d503247d59aaee715b5bf
- evidence_id: access-tachezy2022-rg-pdf
  kind: authority
  reference: https://www.researchgate.net/profile/Ivan-Hrdy/publication/360605238_The_hydrogenosome_of_Trichomonas_vaginalis/links/66fa5b6ab753fa724d4ffa69/The-hydrogenosome-of-Trichomonas-vaginalis.pdf
  locator: Exact retained response; HTTP status 403; 779 bytes
  accessed_at: '2026-10-22T01:41:36.649756Z'
  support: context_only
  summary: Retained prior access attempt, status 403; no genuine full review body
    was established from this response. Original source timestamp and bytes retained.
  snapshot_sha256: f63b045138ec5f63f7443d87ceece69a35acc9a19ca71ab1e903b025d5f9e4fe
- evidence_id: boundary
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome.yaml
  locator: Frozen neighbor identity, definition/source, parent_structures, part_of,
    has_part and xrefs only
  accessed_at: '2026-10-22T02:27:57Z'
  support: context_only
  summary: Local envelope/matrix or inner/outer/intermembrane-space identifiers resolve
    against the exact inspected neighboring records. Only their boundary fields informed
    this judgment; the maintained target remains the sole reviewed record.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/mitosome_envelope.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:18:56Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/mitosome_envelope.yaml'
  snapshot_sha256: 1c6ff14291a676c5f9db95c5bccfe1af6e385e0155657a8f09c299992ae84154
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/mitosome_envelope.yaml
    --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitosome_envelope-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:18:57Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitosome_envelope.yaml\
    \ --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitosome_envelope-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitosome_envelope-strict.tsv"
  snapshot_sha256: 5f75ac038651aaa3b42eb2cc2df4338ad9b254cb5129996ff75b062ff30b2f1d
- evidence_id: focused-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/mitosome_envelope.yaml
  locator: /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitosome-agent/mitosome_envelope-causal.log
  accessed_at: '2026-10-22T02:24:58.865837Z'
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
  locator: data/structures/membrane_organelle/mitosome_envelope.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '12 of 16 collected target identifiers returned OK. cellstructuremech:mitosome_envelope:
    SKIPPED; Exact local identifier and label mitosome envelope resolve to the frozen
    maintained data/structures/membrane_organelle/mitosome_envelope.yaml; definition
    and boundary relations were read, with exact UniProt SL correspondence inspected.
    Ignored-inclusive anchored identifier search uniquely resolves this record. This
    resolves identity only, not all scientific claims of the neighboring record.;
    cellstructuremech:mitosome_inner_membrane: SKIPPED; Exact local identifier and
    label mitosome inner membrane resolve to the frozen maintained data/structures/membrane_organelle/mitosome_inner_membrane.yaml;
    definition and boundary relations were read, with exact UniProt SL correspondence
    inspected. Ignored-inclusive anchored identifier search uniquely resolves this
    record. This resolves identity only, not all scientific claims of the neighboring
    record.; cellstructuremech:mitosome_intermembrane_space: SKIPPED; Exact local
    identifier and label mitosome intermembrane space resolve to the frozen maintained
    data/structures/membrane_organelle/mitosome_intermembrane_space.yaml; definition
    and boundary relations were read, with exact UniProt SL correspondence inspected.
    Ignored-inclusive anchored identifier search uniquely resolves this record. This
    resolves identity only, not all scientific claims of the neighboring record.;
    cellstructuremech:mitosome_outer_membrane: SKIPPED; Exact local identifier and
    label mitosome outer membrane resolve to the frozen maintained data/structures/membrane_organelle/mitosome_outer_membrane.yaml;
    definition and boundary relations were read, with exact UniProt SL correspondence
    inspected. Ignored-inclusive anchored identifier search uniquely resolves this
    record. This resolves identity only, not all scientific claims of the neighboring
    record. Native source checks are separately scoped; skipped or unreachable identifiers
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
  topic: Exact mitosomal compartment
  outcome: supported
  target_ids:
  - cellstructuremech:mitosome_envelope
  summary: GO0032047 identifies the mitosome. The envelope local identity is anchored
    by exact UniProtSL0438, with inner/outer membranes and intermembrane space separately
    resolved. GO0031967 supplies an organelle-envelope parent for that local class.
    Supported identity/topology is distinct from an assertion that all mitosomes use
    one metabolic system.
  evidence_ids:
  - mitosome-agent-go
  - mitosome-agent-SL0438
  - boundary
  - record
- assessment_id: taxa
  area: scope
  topic: Verified taxa and limits of source coverage
  outcome: unknown
  target_ids:
  - cellstructuremech:mitosome_envelope
  summary: Native taxon identities match, including the Giardia duodenalis/intestinalis
    naming equivalence where relevant. The listed studies support examples rather
    than numerical Eukaryota prevalence. The DOI12922 abstract does not verify the
    broad rare-mitosome distribution rationale, and Tovar1999 abstract-only access
    does not establish the specific attributed double-membrane observation.
  evidence_ids:
  - mitosome-agent-tax2759
  - mitosome-agent-tax5759
  - mitosome-agent-tovar1999-meta
  - mitosome-agent-tachezy2022-meta
- assessment_id: necessity
  area: grounding
  topic: Formation necessity
  outcome: unknown
  target_ids:
  - cellstructuremech:mitosome_envelope
  summary: Component essentiality is UNKNOWN. Functional replacement, protein import
    or organism viability cannot be promoted to organelle-formation necessity; no
    unsupported ESSENTIAL label is present.
  evidence_ids:
  - mitosome-agent-dolezal2005-pmc
  - schema
- assessment_id: molecular
  area: grounding
  topic: Anatomical membranes versus lipid building blocks
  outcome: concern
  target_ids:
  - cellstructuremech:mitosome_envelope
  summary: Both molecular LIPID rows ground to exact local records for whole membranes.
    Their graph component_ref joins repeat this mismatch. The correct has_part links,
    STRUCTURE node groundings and four-edge NONMECHANISTIC topology remain supported.
  evidence_ids:
  - mitosome-agent-SL0439
  - mitosome-agent-SL0443
  - boundary
  - schema
  - curation
  - record
- assessment_id: function
  area: scope
  topic: Envelope topology and protein-import boundary
  outcome: supported
  target_ids:
  - cellstructuremech:mitosome_envelope
  summary: Exact SL definitions support the inner/outer/IMS relationships and compartmentalization.
    Dolezal establishes N-terminally targeted cargo crossing the boundary; the wording
    can denote this supported subset and does not explicitly say all cargo uses N-terminal
    signals. Internal-signal targeting is preserved as a scope limit, not converted
    into a forced contrary finding.
  evidence_ids:
  - mitosome-agent-SL0438
  - mitosome-agent-SL0439
  - mitosome-agent-SL0440
  - mitosome-agent-SL0443
  - mitosome-agent-dolezal2005-pmc
- assessment_id: bibliography
  area: evidence
  topic: Exact12922 source identity
  outcome: concern
  target_ids:
  - cellstructuremech:mitosome_envelope
  summary: The12922 DOI identifies The hydrogenosome of Trichomonas vaginalis. The
    supplied Hydrogenosomes and mitosomes title is a different bibliographic description;
    this is a certain bounded citation-label error, not proof that mitosome occurrence
    itself is false.
  evidence_ids:
  - mitosome-agent-tachezy2022-meta
  - record
- assessment_id: complete
  area: completeness
  topic: Complete bounded target coverage
  outcome: supported
  target_ids:
  - cellstructuremech:mitosome_envelope
  summary: Identity, hierarchy, scoped molecular components, taxonomy, functions,
    every graph edge and historical discussions were assessed. Resolved historical
    missing-child wording is not treated as a current absence claim. No images, quantitative
    properties, verbatim snippets or existing UniProt protein instances occur on this
    target; no optional example inventory is made mandatory.
  evidence_ids:
  - record
  - boundary
  - mitosome-agent-go
  - mitosome-agent-dolezal2005-pmc
findings:
- finding_id: F1
  issue_key: mitosome-envelope-1
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate whole mitosome membranes from lipid molecular components
  description: The outer and inner membrane rows are typed LIPID but grounded to cellstructuremech:mitosome_outer_membrane
    and cellstructuremech:mitosome_inner_membrane, complete anatomical structures
    established by their exact UniProt locations and frozen neighbor definitions.
    These are not lipid chemical classes under the molecular-component contract. The
    corresponding graph nodes reference the mismatched molecular rows even though
    their STRUCTURE identities and topology are correct.
  target_ids:
  - cellstructuremech:mitosome_envelope
  field_paths:
  - components[0].component_type
  - components[0].grounding
  - components[1].component_type
  - components[1].grounding
  - causal_graphs[0].nodes[2].component_ref
  - causal_graphs[0].nodes[3].component_ref
  evidence_ids:
  - mitosome-agent-SL0439
  - mitosome-agent-SL0443
  - boundary
  - schema
  - curation
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_envelope.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity and claim-level
    support
  native_severity: major
  normalization_reason: Major categorical molecular-grounding mismatch, while the
    compartment identity and topology remain valid.
- finding_id: F2
  issue_key: mitosome-envelope-2
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the title attached to DOI10.1111/jeu.12922
  description: 'The target labels DOI10.1111/jeu.12922 as Hydrogenosomes and mitosomes:
    Mitochondria of anaerobic eukaryotes. Native bibliographic metadata identifies
    The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022).
    Its full-body applicability to mitosome distribution remains unverified; the article
    title is definitively wrong.'
  target_ids:
  - cellstructuremech:mitosome_envelope
  field_paths:
  - evidence[9].notes
  evidence_ids:
  - mitosome-agent-tachezy2022-meta
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_envelope.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity and claim-level
    support
  native_severity: minor
  normalization_reason: Minor bibliographic attribution error; the DOI resolves and
    organelle identity remains intact.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:mitosome_envelope
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_envelope.yaml
    role: maintained scientific record
  description: Keep the exact anatomical has_part links and STRUCTURE nodes. Remove
    whole-membrane molecular rows or replace them with independently supported lipid
    classes and appropriate chemical or justified label-only identity; reconcile component_ref
    references.
  acceptance_checks:
  - Preserve the supported biological scope and source experimental conditions.
  - Run focused native schema, strict and applicable graph/protein checks after separately
    authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - cellstructuremech:mitosome_envelope
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_envelope.yaml
    role: maintained scientific record
  description: Correct the bibliographic title/authorship for the retained DOI. Independently
    verify or replace the source used for broad mitosome-distribution claims without
    treating unread full text as proof of absence.
  acceptance_checks:
  - Preserve the supported biological scope and source experimental conditions.
  - Run focused native schema, strict and applicable graph/protein checks after separately
    authorized curation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Tovar1999, Tovar2003 and Williams2002 where applicable were inspected through exact
  complete native abstracts; blocked/subscription responses are retained and no unread
  full Methods or membrane-ultrastructure panels are certified.
- DOI12922 is verified bibliographically and through its abstract only. Retained failed
  public routes do not prove the full review lacks a particular statement.
- Dolezal uses Giardia WB and Trichomonas T1; the IscS-half targeting experiment is
  heterologous hydrogenosomal targeting. N-terminal signals are a supported route,
  not a universal requirement.
- No source figure pixels, raw data or supplemental experiments were reanalyzed. Goldberg
  main text/captions and appended Methods were read for the whole mitosome target
  only.
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
