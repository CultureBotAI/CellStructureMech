# Dnab dnac dnat pria pric complex scientific review

- Review: 20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:51:00Z
- Finished UTC: 2026-10-22T06:07:42Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

GO identity and protein accessions are correct. One major separates the Ng PhiX product from the differently bounded loading intermediate; one minor resolves three exact protein families.

## Scope And Provenance

Exactly one complete maintained target, frozen guidance and actual source scopes enumerated per evidence locator; no other maintained scientific record used as evidence.

Selection: Target 7 of batch52, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990159 | data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml | maintained | DnaB-DnaC-DnaT-PriA-PriC complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990159 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990159 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:1990159 | Native focused check passed; scientific support is separately assessed. |
| Native verify | passed | True | GO:1990159 | Native focused check passed; scientific support is separately assessed. |
| Expression-module applicability | not_applicable | False | GO:1990159 | No expression-module claim requires this resource. |
| Claim-level scientific review | passed | True | GO:1990159 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990159 | 13 of 15 collected target identifiers returned OK. PMID:8663104: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:8663105: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990159 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990159 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990159 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990159 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990159 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Ontology identity versus the cited isolated assembly

identity: concern. Targets: GO:1990159.

The label, definition, synonym types and pre-primosome parent match GO1990159. That authority match does not resolve the primary-source conflict: the target explicitly excludes PriB and retains DnaB-DnaC, while NgII experimentally retains PriB and rejects stable DnaC membership. Preserve the ontology identity while separating the loading intermediate from the isolated product.

### Exact DnaT, PriA and PriC families

grounding: concern. Targets: GO:1990159.

The three reviewed K12 examples are correct; their native family xrefs independently match IPR020917, IPR005259 and IPR010890. These are full named-protein families rather than generic ATPase/helicase domains. The source-neutral family deferral is resolvable. No exact PAS feature term was established, so that DNA row is not forced into oriC.

### E.coli identity does not prove this exact canonical cohort

scope: concern. Targets: GO:1990159.

Species562 and K12 reference identities are correct. COMMON retains majority-occurrence meaning; the study is not a population census. More fundamentally, its experimentally isolated PhiX complex is not the maintained PriB-excluded, DnaC-containing cohort, so the canonical example and source-based scope require reconciliation before this study is used as direct evidence for that exact assembly.

### Explicit source-stage conflict in the coarse graph

graph: concern. Targets: GO:1990159.

NONMECHANISTIC correctly avoids atomic loading steps. Nevertheless, the PAS scaffold edge cites NgI and the graph calls the PriB-excluded class a PhiX assembly; the cited primary abstracts and NgII body describe a PriB-containing product with DnaC acting during loading. The restart function is a GO-level classification, not a direct restart experiment in NgII.

### Do not transfer assembly controls across different cohorts

grounding: unknown. Targets: GO:1990159.

NgII directly tests PriA omission for its PhiX complex and discusses partial PriC effects, but those controls do not establish formation necessity for the separately bounded GO1990159 branch. UNKNOWN is not replaced using a mismatched experimental assembly.

### All maintained fields and unresolved boundaries

completeness: supported. Targets: GO:1990159.

The full target, graph, evidence, discussions and history were read. The current findings distinguish exact mappings from unresolved DNA features and source-specific biology from ontology provenance. Optional inventory/stoichiometry/assembly fields are not forced without suitable evidence.

## Findings

### F1: Separate the cited PhiX product from the maintained loading intermediate

major / open / confirmed; issue key: pria-pric-source-cohort.

The record treats NgII as direct evidence for a PriB-excluded DnaB-DnaC-DnaT-PriA-PriC assembly, including its canonical example, constituent notes and replication-through-restart function. NgII pp15653–54 explicitly reports a stable PriA/PriB/PriC/DnaT/DnaB complex and rejects DnaC as a stable constituent; its repair/restart extension is proposed. The correct GO identifier does not make the experimentally different cohort equivalent.

### F2: Ground DnaT, PriA and PriC with exact families

minor / open / confirmed; issue key: pria-pric-exact-families.

The three REVIEWED_LABEL_ONLY protein rows defer mapping despite exact full-protein families IPR020917, IPR005259 and IPR010890 and independent membership of their correct K12 examples.

## Recommended Actions And Acceptance Checks

### A1

Keep the intended GO1990159 identity, but separate GO-defined loading/restart scope from NgI/II experimental context. Replace or qualify the canonical example and affected source notes with evidence for the exact PriA/PriC intermediate; explicitly distinguish loading factors from isolated product composition.

- Do not add PriB or remove DnaC solely to turn this record into a different assembly.
- Do not present NgII as a directly measured repaired-fork restart experiment.
- Retain correct protein identities and the genuinely supported PhiX study context.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.

### A2

Use the verified DnaT/PriA/PriC family mappings and align current grounding notes/TODO, retaining unresolved PAS-DNA grounding.

- Do not substitute a generic helicase/ATPase or DnaT domain.
- Do not convert PAS DNA to chromosomal oriC.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml; Entire target including all evidence, graph, discussions, examples and history | context_only | The full maintained target was read; prior curation history is not independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, EssentialityEnum, COMMON and NONMECHANISTIC graph scope | context_only | Protein identity, complex membership, formation necessity and downstream activity are distinct. COMMON means present in most members, with losses the exception. |
| curation | docs/CURATION.md; Exact class grounding and REVIEWED_LABEL_ONLY contract, especially159–160 | context_only | A verified exact full-protein family can resolve a label-only component; a broad domain or mismatched subgroup cannot. |
| helicase52-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003678,GO:0006269,GO:0031297,GO:0033202,GO:1990098,GO:1990099,GO:1990100,GO:1990156,GO:1990158,GO:1990159,GO:1990160,GO:1990161; Complete relevant definitions, synonyms, active status and typed child links in the twelve-term response; unrelated terms are not treated as target-specific proof | supports | GO1990159 has the exact maintained protein-DNA definition, exact preprimosome synonym and related phi-X174 synonym; GO1990099 lists it as an is-a child. GO1990158/1990160 name distinct sibling classes. The term cites NgII, but that citation link does not independently establish agreement with its experimental cohort. |
| helicase52-agent-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxon response | supports | ENA taxon562 is Escherichia coli, rank species; its native names and lineage were checked. |
| helicase52-agent-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxon response | supports | ENA taxon83333 is Escherichia coli K-12, rank strain; its native names and lineage were checked. |
| helicase52-agent-protein-P0A8J2 | https://rest.uniprot.org/uniprotkb/P0A8J2.json; Accession/status/name, all gene names and organism; FUNCTION/SUBUNIT/SIMILARITY comments and InterPro xrefs | supports | Reviewed P0A8J2 is Replication restart protein DnaT, gene dnaT, taxon83333. The native gene/organism, FUNCTION, SUBUNIT, SIMILARITY and InterPro xrefs support identity at their stated annotation scope; each annotation remains distinct from direct evidence for the entire reviewed complex. |
| helicase52-agent-gene-dnaT-exact83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaT%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/gene-alias/organism identities | supports | The exact reviewed-gene query returns 1 identities: P0A8J2. The maintained example is the sole result at this query scope. |
| helicase52-agent-protein-P17888 | https://rest.uniprot.org/uniprotkb/P17888.json; Accession/status/name, all gene names and organism; FUNCTION/SUBUNIT/SIMILARITY comments and InterPro xrefs | supports | Reviewed P17888 is Replication restart protein PriA, gene priA, taxon83333. The native gene/organism, FUNCTION, SUBUNIT, SIMILARITY and InterPro xrefs support identity at their stated annotation scope; each annotation remains distinct from direct evidence for the entire reviewed complex. |
| helicase52-agent-gene-priA-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/gene-alias/organism identities | supports | The exact reviewed-gene query returns 1 identities: P17888. The maintained example is the sole result at this query scope. |
| helicase52-agent-protein-P23862 | https://rest.uniprot.org/uniprotkb/P23862.json; Accession/status/name, all gene names and organism; FUNCTION/SUBUNIT/SIMILARITY comments and InterPro xrefs | supports | Reviewed P23862 is Replication restart protein PriC, gene priC, taxon83333. The native gene/organism, FUNCTION, SUBUNIT, SIMILARITY and InterPro xrefs support identity at their stated annotation scope; each annotation remains distinct from direct evidence for the entire reviewed complex. |
| helicase52-agent-gene-priC-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/gene-alias/organism identities | supports | The exact reviewed-gene query returns 1 identities: P23862. The maintained example is the sole result at this query scope. |
| helicase52-agent-pmid-8663104 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663104+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and complete native abstract | supports | Native MED8663104: The ordered assembly of the phiX174-type primosome. I. Isolation and identification of intermediate protein-DNA complexes. Authors Ng JY, Marians KJ.; DOI 10.1074/jbc.271.26.15642. Complete primary-study abstract read; no full-body access is implied by the metadata response. |
| helicase52-agent-pmid-8663105 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663105+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and complete native abstract | supports | Native MED8663105: The ordered assembly of the phiX174-type primosome. II. Preservation of primosome composition from assembly through replication. Authors Ng JY, Marians KJ.; DOI 10.1074/jbc.271.26.15649. Complete primary-study abstract read; no full-body access is implied by the metadata response. |
| helicase52-agent-ng1996ii-pdf | https://pdfs.semanticscholar.org/7cc3/a0885916eebe17fede5346ad9e4d97fab747.pdf; Genuine publisher-formatted PDF: title/authors/abstract; complete Introduction, Materials and Methods, Results, Discussion through p15654; TableI and Fig1–9 captions. References p15655 not treated as independently read studies; no pixels. | supports | Ng/Marians1996II directly isolates PhiX174 protein-DNA complexes by gel filtration and detects their composition by Western analysis. The retained complex contains PriA/PriB/PriC/DnaT/DnaB. Low DnaC coelution is explicitly not interpreted as stable membership (pp15653–54); restart/repair implications are hypotheses beyond the measured phage-complementary-strand reaction. PriA omission prevents the measured complex, but this is not automatically a test of the separate GO-defined branch. |
| helicase52-agent-ipr-IPR010890 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010890/; Native name/type, complete description, member signatures, hierarchy and curation flags | supports | IPR010890 is the full PriC bacterial restart-protein family, separate from its structural-domain classification. Family identity is supported by its native name/type/description and signatures; complex-specific membership is assessed separately. |
| helicase52-agent-ipr-IPR005259 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005259/; Native name/type, complete description, member signatures, hierarchy and curation flags | supports | IPR005259 is the full PriA primosomal-protein family, not one helicase or DNA-binding domain. Its native description and specific family hierarchy distinguish the named protein class. |
| helicase52-agent-ipr-IPR020917 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020917/; Native name/type, complete description, member signatures, hierarchy and curation flags | supports | IPR020917 is the DnaT family with exact HAMAP MF01061 and NCBIfam NF002770 signatures. Its description states DnaT and similar proteobacterial proteins; it is not the separate DnaT C-terminal domain. Native example membership is evidenced by the separate UniProt response. |
| schema-result | just validate data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml |
| strict-result | just validate-strict data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_pric_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_pric_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_pric_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml  (GO:1990159)<br>  dnab_dnac_dnat_pria_pric_restart	dnat_restart_protein	COVERED	-&gt;dnat_restart_protein (UniProtKB:P0A8J2)<br>  dnab_dnac_dnat_pria_pric_restart	pria_restart_protein	COVERED	-&gt;pria_restart_protein (UniProtKB:P17888)<br>  dnab_dnac_dnat_pria_pric_restart	pric_restart_protein	COVERED	-&gt;pric_restart_protein (UniProtKB:P23862)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 15 collected target identifiers returned OK. PMID:8663104: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:8663105: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Five completed same-base batch26 global gates await guarded parent manifest/hash integration; this unsaved draft does not finalize or rerun corpus checks.
- No figure pixels, supplementary experimental data or deposited coordinate geometry were reanalyzed. Text/caption and native-response reading extents are stated individually.
- NgI is used only at its complete native abstract scope; NgII genuine PDF main text was read. The displayed NgI web preview was not retained as claim evidence.
- The native GO definition and its cited primary cohort are in tension. This review does not deny the existence of a PriA/PriC restart pathway; it identifies the exact evidence-placement and assembly-stage mismatch.
- DnaT exact-organism83333 query has one hit; the broader taxonomy83333 query also includes descendant strains. Those additional strain entries do not invalidate the exact-organism note.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes honest clean reviews as well as findings.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Dnab dnac dnat pria pric complex scientific review
started_at: '2026-10-22T05:51:00Z'
finished_at: '2026-10-22T06:07:42Z'
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
summary: GO identity and protein accessions are correct. One major separates the Ng
  PhiX product from the differently bounded loading intermediate; one minor resolves
  three exact protein families.
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
  - path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    sha256: af55566f43167e28b8f1cca9fc819d6914d7281179845fc6f3bfb153e67cae43
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
- target_id: GO:1990159
  path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
  label: DnaB-DnaC-DnaT-PriA-PriC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, frozen guidance and actual
    source scopes enumerated per evidence locator; no other maintained scientific
    record used as evidence.
  selection: Target 7 of batch52, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990159
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: just validate data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: just validate-strict data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_pric_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; scientific support is separately assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; scientific support is separately assessed.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990159
  summary: No expression-module claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990159
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - helicase52-agent-go
  - helicase52-agent-tax562
  - helicase52-agent-tax83333
  - helicase52-agent-protein-P0A8J2
  - helicase52-agent-gene-dnaT-exact83333
  - helicase52-agent-protein-P17888
  - helicase52-agent-gene-priA-83333
  - helicase52-agent-protein-P23862
  - helicase52-agent-gene-priC-83333
  - helicase52-agent-pmid-8663104
  - helicase52-agent-pmid-8663105
  - helicase52-agent-ng1996ii-pdf
  - helicase52-agent-ipr-IPR010890
  - helicase52-agent-ipr-IPR005259
  - helicase52-agent-ipr-IPR020917
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990159
  summary: '13 of 15 collected target identifiers returned OK. PMID:8663104: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:8663105: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - helicase52-agent-pmid-8663104
  - helicase52-agent-pmid-8663105
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990159
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
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
  locator: Entire target including all evidence, graph, discussions, examples and
    history
  accessed_at: '2026-10-22T06:00:20Z'
  support: context_only
  summary: The full maintained target was read; prior curation history is not independent
    scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, EssentialityEnum, COMMON and NONMECHANISTIC
    graph scope
  accessed_at: '2026-10-22T06:00:20Z'
  support: context_only
  summary: Protein identity, complex membership, formation necessity and downstream
    activity are distinct. COMMON means present in most members, with losses the exception.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class grounding and REVIEWED_LABEL_ONLY contract, especially159–160
  accessed_at: '2026-10-22T06:00:20Z'
  support: context_only
  summary: A verified exact full-protein family can resolve a label-only component;
    a broad domain or mismatched subgroup cannot.
- evidence_id: helicase52-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003678,GO:0006269,GO:0031297,GO:0033202,GO:1990098,GO:1990099,GO:1990100,GO:1990156,GO:1990158,GO:1990159,GO:1990160,GO:1990161
  locator: Complete relevant definitions, synonyms, active status and typed child
    links in the twelve-term response; unrelated terms are not treated as target-specific
    proof
  accessed_at: '2026-10-22T05:52:55.465072Z'
  support: supports
  summary: GO1990159 has the exact maintained protein-DNA definition, exact preprimosome
    synonym and related phi-X174 synonym; GO1990099 lists it as an is-a child. GO1990158/1990160
    name distinct sibling classes. The term cites NgII, but that citation link does
    not independently establish agreement with its experimental cohort.
  snapshot_sha256: 86f76f1170ba0ae06e64efedbe695c9dcbed34ee35821eb6229ab8f12eda1d32
- evidence_id: helicase52-agent-tax562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxon response
  accessed_at: '2026-10-22T05:52:55.465240Z'
  support: supports
  summary: ENA taxon562 is Escherichia coli, rank species; its native names and lineage
    were checked.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: helicase52-agent-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxon response
  accessed_at: '2026-10-22T05:52:55.465376Z'
  support: supports
  summary: ENA taxon83333 is Escherichia coli K-12, rank strain; its native names
    and lineage were checked.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: helicase52-agent-protein-P0A8J2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A8J2.json
  locator: Accession/status/name, all gene names and organism; FUNCTION/SUBUNIT/SIMILARITY
    comments and InterPro xrefs
  accessed_at: '2026-10-22T05:52:56.246138Z'
  support: supports
  summary: Reviewed P0A8J2 is Replication restart protein DnaT, gene dnaT, taxon83333.
    The native gene/organism, FUNCTION, SUBUNIT, SIMILARITY and InterPro xrefs support
    identity at their stated annotation scope; each annotation remains distinct from
    direct evidence for the entire reviewed complex.
  snapshot_sha256: 0386cc1a24225bd2163f02bb9321fd59c773a862df700e6e11a442f2478a0eb8
- evidence_id: helicase52-agent-gene-dnaT-exact83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaT%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned accession/name/gene-alias/organism identities
  accessed_at: '2026-10-22T05:53:37.865414Z'
  support: supports
  summary: 'The exact reviewed-gene query returns 1 identities: P0A8J2. The maintained
    example is the sole result at this query scope.'
  snapshot_sha256: 098bbb792557c7cee62ac410f631525fb18878c8a368f6dc6a608934b785ac70
  search_scope: UniProt gene_exact:dnaT, reviewed:true, organism_id:83333; size500;
    all returned identities read. Exact-organism and descendant-inclusive taxonomy
    queries are distinguished.
- evidence_id: helicase52-agent-protein-P17888
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P17888.json
  locator: Accession/status/name, all gene names and organism; FUNCTION/SUBUNIT/SIMILARITY
    comments and InterPro xrefs
  accessed_at: '2026-10-22T05:52:56.395030Z'
  support: supports
  summary: Reviewed P17888 is Replication restart protein PriA, gene priA, taxon83333.
    The native gene/organism, FUNCTION, SUBUNIT, SIMILARITY and InterPro xrefs support
    identity at their stated annotation scope; each annotation remains distinct from
    direct evidence for the entire reviewed complex.
  snapshot_sha256: 17504956503542663f62e0d18d9f987a50081497aa0daea13b6b7d96496536aa
- evidence_id: helicase52-agent-gene-priA-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned accession/name/gene-alias/organism identities
  accessed_at: '2026-10-22T05:52:58.144220Z'
  support: supports
  summary: 'The exact reviewed-gene query returns 1 identities: P17888. The maintained
    example is the sole result at this query scope.'
  snapshot_sha256: c618bd342375bdeea25c1ad6bad58c8a2e1caa6e8251a59b765619b44080f160
  search_scope: UniProt gene_exact:priA, reviewed:true, taxonomy_id:83333; size500;
    all returned identities read. Exact-organism and descendant-inclusive taxonomy
    queries are distinguished.
- evidence_id: helicase52-agent-protein-P23862
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P23862.json
  locator: Accession/status/name, all gene names and organism; FUNCTION/SUBUNIT/SIMILARITY
    comments and InterPro xrefs
  accessed_at: '2026-10-22T05:52:56.507424Z'
  support: supports
  summary: Reviewed P23862 is Replication restart protein PriC, gene priC, taxon83333.
    The native gene/organism, FUNCTION, SUBUNIT, SIMILARITY and InterPro xrefs support
    identity at their stated annotation scope; each annotation remains distinct from
    direct evidence for the entire reviewed complex.
  snapshot_sha256: 96930e6dc73122793f5d39f5c396641a24b6699043a4c497e2dfd2ab41051f13
- evidence_id: helicase52-agent-gene-priC-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned accession/name/gene-alias/organism identities
  accessed_at: '2026-10-22T05:52:58.144358Z'
  support: supports
  summary: 'The exact reviewed-gene query returns 1 identities: P23862. The maintained
    example is the sole result at this query scope.'
  snapshot_sha256: bc4010a8d7187e308ab78e6895a971fdf39dc06b77d51b9164ca15db0550f673
  search_scope: UniProt gene_exact:priC, reviewed:true, taxonomy_id:83333; size500;
    all returned identities read. Exact-organism and descendant-inclusive taxonomy
    queries are distinguished.
- evidence_id: helicase52-agent-pmid-8663104
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663104+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and complete native abstract
  accessed_at: '2026-10-22T05:53:00.243834Z'
  support: supports
  summary: 'Native MED8663104: The ordered assembly of the phiX174-type primosome.
    I. Isolation and identification of intermediate protein-DNA complexes. Authors
    Ng JY, Marians KJ.; DOI 10.1074/jbc.271.26.15642. Complete primary-study abstract
    read; no full-body access is implied by the metadata response.'
  snapshot_sha256: 3e2d617075aaee60c3c0381e1c40f1f145200075473e7d5f158c1f9c030d203a
- evidence_id: helicase52-agent-pmid-8663105
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663105+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and complete native abstract
  accessed_at: '2026-10-22T05:53:00.501593Z'
  support: supports
  summary: 'Native MED8663105: The ordered assembly of the phiX174-type primosome.
    II. Preservation of primosome composition from assembly through replication. Authors
    Ng JY, Marians KJ.; DOI 10.1074/jbc.271.26.15649. Complete primary-study abstract
    read; no full-body access is implied by the metadata response.'
  snapshot_sha256: 1e0127e96480f8699dc718488f73eeef23f1a0f84fc8d3595c6c67c146d809e0
- evidence_id: helicase52-agent-ng1996ii-pdf
  kind: primary_source
  reference: https://pdfs.semanticscholar.org/7cc3/a0885916eebe17fede5346ad9e4d97fab747.pdf
  locator: 'Genuine publisher-formatted PDF: title/authors/abstract; complete Introduction,
    Materials and Methods, Results, Discussion through p15654; TableI and Fig1–9 captions.
    References p15655 not treated as independently read studies; no pixels.'
  accessed_at: '2026-10-22T05:55:37.199474Z'
  support: supports
  summary: Ng/Marians1996II directly isolates PhiX174 protein-DNA complexes by gel
    filtration and detects their composition by Western analysis. The retained complex
    contains PriA/PriB/PriC/DnaT/DnaB. Low DnaC coelution is explicitly not interpreted
    as stable membership (pp15653–54); restart/repair implications are hypotheses
    beyond the measured phage-complementary-strand reaction. PriA omission prevents
    the measured complex, but this is not automatically a test of the separate GO-defined
    branch.
  snapshot_sha256: 1789a6bf1cfb26aeeacf73f6ba45b732d43eb3576268435c1736b357e3be6755
- evidence_id: helicase52-agent-ipr-IPR010890
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010890/
  locator: Native name/type, complete description, member signatures, hierarchy and
    curation flags
  accessed_at: '2026-10-22T05:53:37.121587Z'
  support: supports
  summary: IPR010890 is the full PriC bacterial restart-protein family, separate from
    its structural-domain classification. Family identity is supported by its native
    name/type/description and signatures; complex-specific membership is assessed
    separately.
  snapshot_sha256: 0c8cb9aa7f1d6e1f45397fce72a6935dd2151706a90f512c92628c92bbc0217c
- evidence_id: helicase52-agent-ipr-IPR005259
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005259/
  locator: Native name/type, complete description, member signatures, hierarchy and
    curation flags
  accessed_at: '2026-10-22T05:53:37.121803Z'
  support: supports
  summary: IPR005259 is the full PriA primosomal-protein family, not one helicase
    or DNA-binding domain. Its native description and specific family hierarchy distinguish
    the named protein class.
  snapshot_sha256: fd26c216e78be07f400f25ecd11062366714b19eda510840dbb92be4fb1e9db2
- evidence_id: helicase52-agent-ipr-IPR020917
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020917/
  locator: Native name/type, complete description, member signatures, hierarchy and
    curation flags
  accessed_at: '2026-10-22T05:53:37.121052Z'
  support: supports
  summary: IPR020917 is the DnaT family with exact HAMAP MF01061 and NCBIfam NF002770
    signatures. Its description states DnaT and similar proteobacterial proteins;
    it is not the separate DnaT C-terminal domain. Native example membership is evidenced
    by the separate UniProt response.
  snapshot_sha256: 6737844952628c1e6c0e30133e8134728c11a4bc28c213dedc4afd497ef082cd
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:51:01Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml'
  snapshot_sha256: 784b6416bc219017bb7b7035ad1f0b543970da61ef942ac9470cb0ea6ce1c18a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_pric_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:51:03Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml\
    \ --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_pric_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_pric_complex-strict.tsv"
  snapshot_sha256: c332cceb496f15491d69f00ba22a3d85bb36d7472fbf7b72a8d9c2f2c0eec965
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:55:32.413364Z'
  support: supports
  summary: "data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml  (GO:1990159)\n\
    \  dnab_dnac_dnat_pria_pric_restart\tdnat_restart_protein\tCOVERED\t->dnat_restart_protein\
    \ (UniProtKB:P0A8J2)\n  dnab_dnac_dnat_pria_pric_restart\tpria_restart_protein\t\
    COVERED\t->pria_restart_protein (UniProtKB:P17888)\n  dnab_dnac_dnat_pria_pric_restart\t\
    pric_restart_protein\tCOVERED\t->pric_restart_protein (UniProtKB:P23862)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     3  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     3  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: a61be5ffd377d729d7aee4e31668d88690314dce25c4496b9f83c9d4636e782c
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:55:33.689981Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '13 of 15 collected target identifiers returned OK. PMID:8663104: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:8663105: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
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
  topic: Ontology identity versus the cited isolated assembly
  outcome: concern
  target_ids:
  - GO:1990159
  summary: 'The label, definition, synonym types and pre-primosome parent match GO1990159.
    That authority match does not resolve the primary-source conflict: the target
    explicitly excludes PriB and retains DnaB-DnaC, while NgII experimentally retains
    PriB and rejects stable DnaC membership. Preserve the ontology identity while
    separating the loading intermediate from the isolated product.'
  evidence_ids:
  - record
  - helicase52-agent-go
  - helicase52-agent-ng1996ii-pdf
- assessment_id: grounding
  area: grounding
  topic: Exact DnaT, PriA and PriC families
  outcome: concern
  target_ids:
  - GO:1990159
  summary: The three reviewed K12 examples are correct; their native family xrefs
    independently match IPR020917, IPR005259 and IPR010890. These are full named-protein
    families rather than generic ATPase/helicase domains. The source-neutral family
    deferral is resolvable. No exact PAS feature term was established, so that DNA
    row is not forced into oriC.
  evidence_ids:
  - record
  - curation
  - helicase52-agent-ipr-IPR020917
  - helicase52-agent-ipr-IPR005259
  - helicase52-agent-ipr-IPR010890
  - helicase52-agent-protein-P0A8J2
  - helicase52-agent-protein-P17888
  - helicase52-agent-protein-P23862
  - helicase52-agent-gene-dnaT-exact83333
  - helicase52-agent-gene-priA-83333
  - helicase52-agent-gene-priC-83333
- assessment_id: scope
  area: scope
  topic: E.coli identity does not prove this exact canonical cohort
  outcome: concern
  target_ids:
  - GO:1990159
  summary: Species562 and K12 reference identities are correct. COMMON retains majority-occurrence
    meaning; the study is not a population census. More fundamentally, its experimentally
    isolated PhiX complex is not the maintained PriB-excluded, DnaC-containing cohort,
    so the canonical example and source-based scope require reconciliation before
    this study is used as direct evidence for that exact assembly.
  evidence_ids:
  - record
  - schema
  - helicase52-agent-go
  - helicase52-agent-ng1996ii-pdf
  - helicase52-agent-tax562
  - helicase52-agent-tax83333
- assessment_id: graph
  area: graph
  topic: Explicit source-stage conflict in the coarse graph
  outcome: concern
  target_ids:
  - GO:1990159
  summary: NONMECHANISTIC correctly avoids atomic loading steps. Nevertheless, the
    PAS scaffold edge cites NgI and the graph calls the PriB-excluded class a PhiX
    assembly; the cited primary abstracts and NgII body describe a PriB-containing
    product with DnaC acting during loading. The restart function is a GO-level classification,
    not a direct restart experiment in NgII.
  evidence_ids:
  - record
  - schema
  - helicase52-agent-go
  - helicase52-agent-ng1996ii-pdf
  - helicase52-agent-pmid-8663104
  - helicase52-agent-pmid-8663105
- assessment_id: formation
  area: grounding
  topic: Do not transfer assembly controls across different cohorts
  outcome: unknown
  target_ids:
  - GO:1990159
  summary: NgII directly tests PriA omission for its PhiX complex and discusses partial
    PriC effects, but those controls do not establish formation necessity for the
    separately bounded GO1990159 branch. UNKNOWN is not replaced using a mismatched
    experimental assembly.
  evidence_ids:
  - record
  - schema
  - helicase52-agent-ng1996ii-pdf
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and unresolved boundaries
  outcome: supported
  target_ids:
  - GO:1990159
  summary: The full target, graph, evidence, discussions and history were read. The
    current findings distinguish exact mappings from unresolved DNA features and source-specific
    biology from ontology provenance. Optional inventory/stoichiometry/assembly fields
    are not forced without suitable evidence.
  evidence_ids:
  - record
  - schema
  - curation
  - helicase52-agent-go
findings:
- finding_id: F1
  issue_key: pria-pric-source-cohort
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate the cited PhiX product from the maintained loading intermediate
  description: The record treats NgII as direct evidence for a PriB-excluded DnaB-DnaC-DnaT-PriA-PriC
    assembly, including its canonical example, constituent notes and replication-through-restart
    function. NgII pp15653–54 explicitly reports a stable PriA/PriB/PriC/DnaT/DnaB
    complex and rejects DnaC as a stable constituent; its repair/restart extension
    is proposed. The correct GO identifier does not make the experimentally different
    cohort equivalent.
  target_ids:
  - GO:1990159
  field_paths:
  - canonical_examples[0]
  - components#dnab_dnac_complex.evidence
  - functions#replication_fork_processing.evidence
  - causal_graphs#dnab_dnac_dnat_pria_pric_restart
  - discussions#exclude_prib_rep_and_dnag_from_pric_preprimosome
  evidence_ids:
  - record
  - helicase52-agent-go
  - helicase52-agent-ng1996ii-pdf
  - helicase52-agent-pmid-8663104
  - helicase52-agent-pmid-8663105
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: major
  normalization_reason: The cited experiment is used to substantiate the defining
    molecular cohort and canonical example, but its retained composition differs in
    two named proteins and its repair extension is hypothetical. This is material
    source-to-structure scope transfer, not a citation-format defect.
- finding_id: F2
  issue_key: pria-pric-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground DnaT, PriA and PriC with exact families
  description: The three REVIEWED_LABEL_ONLY protein rows defer mapping despite exact
    full-protein families IPR020917, IPR005259 and IPR010890 and independent membership
    of their correct K12 examples.
  target_ids:
  - GO:1990159
  field_paths:
  - components#dnat_restart_protein.grounding_status
  - components#pria_restart_protein.grounding_status
  - components#pric_restart_protein.grounding_status
  - discussions#resolve_pric_restart_component_groundings
  evidence_ids:
  - record
  - curation
  - helicase52-agent-ipr-IPR020917
  - helicase52-agent-ipr-IPR005259
  - helicase52-agent-ipr-IPR010890
  - helicase52-agent-protein-P0A8J2
  - helicase52-agent-protein-P17888
  - helicase52-agent-protein-P23862
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correct protein identifiers remain
    intact; the issue is a bounded exact-family or evidence-attribution correction.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990159
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    role: maintained scientific record
  description: Keep the intended GO1990159 identity, but separate GO-defined loading/restart
    scope from NgI/II experimental context. Replace or qualify the canonical example
    and affected source notes with evidence for the exact PriA/PriC intermediate;
    explicitly distinguish loading factors from isolated product composition.
  acceptance_checks:
  - Do not add PriB or remove DnaC solely to turn this record into a different assembly.
  - Do not present NgII as a directly measured repaired-fork restart experiment.
  - Retain correct protein identities and the genuinely supported PhiX study context.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:1990159
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    role: maintained scientific record
  description: Use the verified DnaT/PriA/PriC family mappings and align current grounding
    notes/TODO, retaining unresolved PAS-DNA grounding.
  acceptance_checks:
  - Do not substitute a generic helicase/ATPase or DnaT domain.
  - Do not convert PAS DNA to chromosomal oriC.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
limitations:
- Five completed same-base batch26 global gates await guarded parent manifest/hash
  integration; this unsaved draft does not finalize or rerun corpus checks.
- No figure pixels, supplementary experimental data or deposited coordinate geometry
  were reanalyzed. Text/caption and native-response reading extents are stated individually.
- NgI is used only at its complete native abstract scope; NgII genuine PDF main text
  was read. The displayed NgI web preview was not retained as claim evidence.
- The native GO definition and its cited primary cohort are in tension. This review
  does not deny the existence of a PriA/PriC restart pathway; it identifies the exact
  evidence-placement and assembly-stage mismatch.
- DnaT exact-organism83333 query has one hit; the broader taxonomy83333 query also
  includes descendant strains. Those additional strain entries do not invalidate the
  exact-organism note.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes honest clean reviews as well as findings.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
