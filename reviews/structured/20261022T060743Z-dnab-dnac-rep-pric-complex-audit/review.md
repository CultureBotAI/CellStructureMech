# Dnab dnac rep pric complex scientific review

- Review: 20261022T060743Z-dnab-dnac-rep-pric-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:51:03Z
- Finished UTC: 2026-10-22T06:07:43Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The native Rep/PriC restart class and correct accessions are retained. One major corrects the mismatched canonical experiment; two minors resolve exact families and the Rep alias-sensitive uniqueness note.

## Scope And Provenance

Exactly one complete maintained target, frozen guidance and actual source scopes enumerated per evidence locator; no other maintained scientific record used as evidence.

Selection: Target 8 of batch52, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990160 | data/structures/other/dnab_dnac_rep_pric_complex.yaml | maintained | DnaB-DnaC-Rep-PriC complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990160 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990160 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:1990160 | Native focused check passed; scientific support is separately assessed. |
| Native verify | passed | True | GO:1990160 | Native focused check passed; scientific support is separately assessed. |
| Expression-module applicability | not_applicable | False | GO:1990160 | No expression-module claim requires this resource. |
| Claim-level scientific review | passed | True | GO:1990160 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990160 | 12 of 14 collected target identifiers returned OK. PMID:19941825: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:8663105: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990160 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990160 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990160 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990160 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990160 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Native restart class remains distinct from the measured active fork

identity: concern. Targets: GO:1990160.

GO1990160 supports the maintained class and sibling exclusions. Native Rep/PriC annotations support a restart pathway, but Guy2009 is not a direct demonstration of the exact four-protein loading intermediate. NgII likewise studies a different PriA/PriB/PriC cohort.

### Exact Rep and PriC class mappings

grounding: concern. Targets: GO:1990160.

IPR005752 and IPR010890 match the named full-protein classes and the separate native UniProt family xrefs. The mistaken hexamer sentence in the Rep family description is not promoted; exact signatures and hierarchy distinguish Rep from UvrD/PcrA. PAS-DNA remains unresolved rather than being mapped to oriC.

### Correct Rep accession with inaccurate query uniqueness

identity: concern. Targets: GO:1990160.

P09980 remains the correct reviewed Rep helicase. The exact-organism reviewed rep query returns it plus P03856, a distinct RepE entry with rep alias. The evidence note calling P09980 the single reviewed hit is therefore too strong; PriC query uniqueness remains supported.

### Canonical experiment has a different stage and composition

scope: concern. Targets: GO:1990160.

Species562 and reference strain83333 are correct; COMMON keeps its majority-occurrence meaning without an empirical census. The canonical Guy experiment tests Rep accessory helicase at an already initiated oriC replisome, not an isolated DnaB-DnaC-Rep-PriC preprimosome. Its functional result cannot serve as direct confirmation of this exact cohort.

### Coarse GO graph with source-limited empirical support

graph: concern. Targets: GO:1990160.

The NONMECHANISTIC graph accurately declares GO-level membership/restart scope, but empirical canonical support must be corrected. Guy main Methods omit PriC, and its DnaC competition result specifically distinguishes the active Rep-DnaB interaction from the loading complex. This does not refute all possible sequential Rep/PriC loading pathways.

### Formation requirement remains unresolved for the exact quartet

grounding: unknown. Targets: GO:1990160.

Rep deletion/complementation and fork-movement assays concern activity and viability; DnaC competition tests a different interaction stage. Neither establishes universal formation necessity of the maintained quartet or its PAS component.

### All maintained fields and unresolved boundaries

completeness: supported. Targets: GO:1990160.

The full target, graph, evidence, discussions and history were read. The current findings distinguish exact mappings from unresolved DNA features and source-specific biology from ontology provenance. Optional inventory/stoichiometry/assembly fields are not forced without suitable evidence.

## Findings

### F1: Use an exact Rep-PriC loading example rather than the active-fork experiment

major / open / confirmed; issue key: rep-pric-canonical-stage.

Guy2009 is the canonical example for this four-protein preprimosome, but its main replication assay omits PriC and studies Rep-assisted movement of oriC-initiated forks. Its Results explicitly show DnaC inhibition of Rep-DnaB binding and place that interaction after loading. NgII also does not supply the missing quartet: its retained PhiX assembly contains PriA/PriB/PriC/DnaT/DnaB.

### F2: Ground Rep and PriC with exact families

minor / open / confirmed; issue key: rep-pric-exact-families.

Two reviewed-label-only rows defer exact mappings despite Rep IPR005752 and PriC IPR010890, supported by exact family signatures and the separately verified examples.

### F3: Qualify the Rep single-entry evidence note

minor / open / confirmed; issue key: rep-query-alias-uniqueness.

The maintained P09980 accession is correct, but the exact reviewed rep query for organism83333 also returns P03856 because rep is an alias for RepE. The current single-reviewed-entry claim is false at that stated query scope.

## Recommended Actions And Acceptance Checks

### A1

Replace or explicitly contextualize Guy2009 as accessory-fork evidence, and use an independently verified exact Rep/PriC loading/restart source for the canonical quartet. Preserve the ontology identity and distinguish sequential loading from the active-fork complex.

- Do not deny the native Rep/PriC restart pathway or infer that no such intermediate exists.
- Do not claim Guy tested PriC or directly isolated the maintained quartet.
- Keep the correct E.coli and reference-protein identifiers.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.

### A2

Apply the exact Rep/PriC protein-family identities and align current notes/TODO while retaining unresolved PAS DNA.

- Do not import the erroneous Rep hexamer prose or substitute the generic UvrD/helicase domain.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.

### A3

Keep P09980 and replace the single-hit rationale with explicit Rep-helicase identity/alias disambiguation.

- Acknowledge both returned identities without replacing Rep with RepE.
- Leave dated historical actions unchanged.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dnab_dnac_rep_pric_complex.yaml; Entire target including all evidence, graph, discussions, examples and history | context_only | The full maintained target was read; prior curation history is not independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, EssentialityEnum, COMMON and NONMECHANISTIC graph scope | context_only | Protein identity, complex membership, formation necessity and downstream activity are distinct. COMMON means present in most members, with losses the exception. |
| curation | docs/CURATION.md; Exact class grounding and REVIEWED_LABEL_ONLY contract, especially159–160 | context_only | A verified exact full-protein family can resolve a label-only component; a broad domain or mismatched subgroup cannot. |
| helicase52-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003678,GO:0006269,GO:0031297,GO:0033202,GO:1990098,GO:1990099,GO:1990100,GO:1990156,GO:1990158,GO:1990159,GO:1990160,GO:1990161; Complete relevant definitions, synonyms, active status and typed child links in the twelve-term response; unrelated terms are not treated as target-specific proof | supports | GO1990160 exactly names DnaB-DnaC-Rep-PriC, associated DNA and restart scope, with exact and related synonyms. GO1990099 lists it as an is-a child. Its citations to Guy2009 and NgII are checked against the actual experiments separately. |
| helicase52-agent-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxon response | supports | ENA taxon562 is Escherichia coli, rank species; its native names and lineage were checked. |
| helicase52-agent-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxon response | supports | ENA taxon83333 is Escherichia coli K-12, rank strain; its native names and lineage were checked. |
| helicase52-agent-protein-P09980 | https://rest.uniprot.org/uniprotkb/P09980.json; Accession/status/name, all gene names and organism; FUNCTION/SUBUNIT/SIMILARITY comments and InterPro xrefs | supports | Reviewed P09980 is ATP-dependent DNA helicase Rep, gene rep, taxon83333. The native gene/organism, FUNCTION, SUBUNIT, SIMILARITY and InterPro xrefs support identity at their stated annotation scope; each annotation remains distinct from direct evidence for the entire reviewed complex. |
| helicase52-agent-gene-rep-exact83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Arep%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/gene-alias/organism identities | supports | The exact reviewed-gene query returns 2 identities: P09980, P03856. P09980 is the correct Rep helicase; P03856 is the distinct RepE protein with rep as an alias, so a single-hit claim is inaccurate. |
| helicase52-agent-protein-P23862 | https://rest.uniprot.org/uniprotkb/P23862.json; Accession/status/name, all gene names and organism; FUNCTION/SUBUNIT/SIMILARITY comments and InterPro xrefs | supports | Reviewed P23862 is Replication restart protein PriC, gene priC, taxon83333. The native gene/organism, FUNCTION, SUBUNIT, SIMILARITY and InterPro xrefs support identity at their stated annotation scope; each annotation remains distinct from direct evidence for the entire reviewed complex. |
| helicase52-agent-gene-priC-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/gene-alias/organism identities | supports | The exact reviewed-gene query returns 1 identities: P23862. The maintained example is the sole result at this query scope. |
| helicase52-agent-pmid-19941825 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19941825+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and complete native abstract | supports | Native MED19941825: Rep provides a second motor at the replisome to promote duplication of protein-bound DNA. Authors Guy CP, Atkinson J, Gupta MK, Mahdi AA, Gwynn EJ, Rudolph CJ, Moon PB, van Knippenberg IC, Cadman CJ, Dillingham MS, Lloyd RG, McGlynn P.; DOI 10.1016/j.molcel.2009.11.009. Complete primary-study abstract read; no full-body access is implied by the metadata response. |
| helicase52-agent-pmid-8663105 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663105+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact title/authors/year/DOI/PMID and complete native abstract | supports | Native MED8663105: The ordered assembly of the phiX174-type primosome. II. Preservation of primosome composition from assembly through replication. Authors Ng JY, Marians KJ.; DOI 10.1074/jbc.271.26.15649. Complete primary-study abstract read; no full-body access is implied by the metadata response. |
| helicase52-agent-ng1996ii-pdf | https://pdfs.semanticscholar.org/7cc3/a0885916eebe17fede5346ad9e4d97fab747.pdf; Genuine publisher-formatted PDF: title/authors/abstract; complete Introduction, Materials and Methods, Results, Discussion through p15654; TableI and Fig1–9 captions. References p15655 not treated as independently read studies; no pixels. | supports | Ng/Marians1996II directly isolates PhiX174 protein-DNA complexes by gel filtration and detects their composition by Western analysis. The retained complex contains PriA/PriB/PriC/DnaT/DnaB. Low DnaC coelution is explicitly not interpreted as stable membership (pp15653–54); restart/repair implications are hypotheses beyond the measured phage-complementary-strand reaction. PriA omission prevents the measured complex, but this is not automatically a test of the separate GO-defined branch. |
| helicase52-agent-ipr-IPR010890 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010890/; Native name/type, complete description, member signatures, hierarchy and curation flags | supports | IPR010890 is the full PriC bacterial restart-protein family, separate from its structural-domain classification. Family identity is supported by its native name/type/description and signatures; complex-specific membership is assessed separately. |
| helicase52-agent-ipr-IPR005752 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005752/; Native name/type, complete description, member signatures, hierarchy and curation flags | supports | IPR005752 is the Rep-specific full family, with exact HAMAP MF01920 and NCBIfam TIGR01074 signatures under the broader UvrD-like family. Its descriptive hexamer prose conflicts with native Rep homodimer annotation and is not adopted as mechanistic evidence; the family name/signatures remain specific. |
| helicase52-agent-guy2009-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC2807033/; Genuine PMC2807033: complete Introduction sec1, Results sec2.1 and sec2.6 including Fig1/6/7 captions, complete Discussion sec3 and main Experimental Procedures sec4. Other Results, supplements and pixels not certified. | supports | Guy2009 demonstrates Rep-assisted movement of oriC-initiated replication forks past protein barriers, direct Rep-DnaB association and enhanced unwinding. Its assay mixture does not contain PriC. Results sec2.6/Fig6I–J show DnaC inhibits Rep-DnaB interaction; the authors place this interaction after helicase loading. The Introduction separately cites earlier Rep/PriC restart work. |
| schema-result | just validate data/structures/other/dnab_dnac_rep_pric_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dnab_dnac_rep_pric_complex.yaml |
| strict-result | just validate-strict data/structures/other/dnab_dnac_rep_pric_complex.yaml --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_rep_pric_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dnab_dnac_rep_pric_complex.yaml --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_rep_pric_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_rep_pric_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/dnab_dnac_rep_pric_complex.yaml  (GO:1990160)<br>  dnab_dnac_rep_pric_restart	rep_helicase	COVERED	-&gt;rep_helicase (UniProtKB:P09980)<br>  dnab_dnac_rep_pric_restart	pric_restart_protein	COVERED	-&gt;pric_restart_protein (UniProtKB:P23862)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dnab_dnac_rep_pric_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 14 collected target identifiers returned OK. PMID:19941825: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:8663105: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Five completed same-base batch26 global gates await guarded parent manifest/hash integration; this unsaved draft does not finalize or rerun corpus checks.
- No figure pixels, supplementary experimental data or deposited coordinate geometry were reanalyzed. Text/caption and native-response reading extents are stated individually.
- Guy main text was read only at the explicitly listed sections; supplemental Methods/strain table and image pixels were not independently inspected.
- GO1990160 and native UniProt support a Rep/PriC restart class, but the cited Guy and Ng experiments do not independently establish the canonical four-protein intermediate. This is not an exhaustive literature-absence claim.
- Rep family metadata has an inconsistent hexamer description. Family grounding relies on its exact name/type/signatures/hierarchy plus independent UniProt membership, not that sentence.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes honest clean reviews as well as findings.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T060743Z-dnab-dnac-rep-pric-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Dnab dnac rep pric complex scientific review
started_at: '2026-10-22T05:51:03Z'
finished_at: '2026-10-22T06:07:43Z'
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
summary: The native Rep/PriC restart class and correct accessions are retained. One
  major corrects the mismatched canonical experiment; two minors resolve exact families
  and the Rep alias-sensitive uniqueness note.
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
  - path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    sha256: 50dccdc4d855065a8319372f4350453a2628309608fad038483bbf6524b0bb8f
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
- target_id: GO:1990160
  path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
  label: DnaB-DnaC-Rep-PriC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, frozen guidance and actual
    source scopes enumerated per evidence locator; no other maintained scientific
    record used as evidence.
  selection: Target 8 of batch52, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990160
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990160
  command: just validate data/structures/other/dnab_dnac_rep_pric_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990160
  command: just validate-strict data/structures/other/dnab_dnac_rep_pric_complex.yaml
    --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_rep_pric_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990160
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml
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
  - GO:1990160
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml
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
  - GO:1990160
  summary: No expression-module claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990160
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - helicase52-agent-go
  - helicase52-agent-tax562
  - helicase52-agent-tax83333
  - helicase52-agent-protein-P09980
  - helicase52-agent-gene-rep-exact83333
  - helicase52-agent-protein-P23862
  - helicase52-agent-gene-priC-83333
  - helicase52-agent-pmid-19941825
  - helicase52-agent-pmid-8663105
  - helicase52-agent-ng1996ii-pdf
  - helicase52-agent-ipr-IPR010890
  - helicase52-agent-ipr-IPR005752
  - helicase52-agent-guy2009-legacy
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990160
  summary: '12 of 14 collected target identifiers returned OK. PMID:19941825: UNREACHABLE;
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
  - helicase52-agent-pmid-19941825
  - helicase52-agent-pmid-8663105
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990160
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
  - GO:1990160
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
  - GO:1990160
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
  - GO:1990160
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
  - GO:1990160
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
  reference: data/structures/other/dnab_dnac_rep_pric_complex.yaml
  locator: Entire target including all evidence, graph, discussions, examples and
    history
  accessed_at: '2026-10-22T06:00:27Z'
  support: context_only
  summary: The full maintained target was read; prior curation history is not independent
    scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, EssentialityEnum, COMMON and NONMECHANISTIC
    graph scope
  accessed_at: '2026-10-22T06:00:27Z'
  support: context_only
  summary: Protein identity, complex membership, formation necessity and downstream
    activity are distinct. COMMON means present in most members, with losses the exception.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class grounding and REVIEWED_LABEL_ONLY contract, especially159–160
  accessed_at: '2026-10-22T06:00:27Z'
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
  summary: GO1990160 exactly names DnaB-DnaC-Rep-PriC, associated DNA and restart
    scope, with exact and related synonyms. GO1990099 lists it as an is-a child. Its
    citations to Guy2009 and NgII are checked against the actual experiments separately.
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
- evidence_id: helicase52-agent-protein-P09980
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09980.json
  locator: Accession/status/name, all gene names and organism; FUNCTION/SUBUNIT/SIMILARITY
    comments and InterPro xrefs
  accessed_at: '2026-10-22T05:52:55.465352Z'
  support: supports
  summary: Reviewed P09980 is ATP-dependent DNA helicase Rep, gene rep, taxon83333.
    The native gene/organism, FUNCTION, SUBUNIT, SIMILARITY and InterPro xrefs support
    identity at their stated annotation scope; each annotation remains distinct from
    direct evidence for the entire reviewed complex.
  snapshot_sha256: dae98d308334bb9a6a702afcdc378176d04b73345251906c02cc3560d8ccb5e7
- evidence_id: helicase52-agent-gene-rep-exact83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Arep%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned accession/name/gene-alias/organism identities
  accessed_at: '2026-10-22T05:53:37.903557Z'
  support: supports
  summary: 'The exact reviewed-gene query returns 2 identities: P09980, P03856. P09980
    is the correct Rep helicase; P03856 is the distinct RepE protein with rep as an
    alias, so a single-hit claim is inaccurate.'
  snapshot_sha256: ba41b4d4eabcc6162cb859ac819e7489fd4fc8bb0671638f4fa069569c4b0fe8
  search_scope: UniProt gene_exact:rep, reviewed:true, organism_id:83333; size500;
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
- evidence_id: helicase52-agent-pmid-19941825
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19941825+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact title/authors/year/DOI/PMID and complete native abstract
  accessed_at: '2026-10-22T05:52:59.741818Z'
  support: supports
  summary: 'Native MED19941825: Rep provides a second motor at the replisome to promote
    duplication of protein-bound DNA. Authors Guy CP, Atkinson J, Gupta MK, Mahdi
    AA, Gwynn EJ, Rudolph CJ, Moon PB, van Knippenberg IC, Cadman CJ, Dillingham MS,
    Lloyd RG, McGlynn P.; DOI 10.1016/j.molcel.2009.11.009. Complete primary-study
    abstract read; no full-body access is implied by the metadata response.'
  snapshot_sha256: 7e989a383aff796a1311908218c83d1aeb00b0ea3a9d26f1c65bfc18663286a0
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
- evidence_id: helicase52-agent-ipr-IPR005752
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005752/
  locator: Native name/type, complete description, member signatures, hierarchy and
    curation flags
  accessed_at: '2026-10-22T05:53:37.121687Z'
  support: supports
  summary: IPR005752 is the Rep-specific full family, with exact HAMAP MF01920 and
    NCBIfam TIGR01074 signatures under the broader UvrD-like family. Its descriptive
    hexamer prose conflicts with native Rep homodimer annotation and is not adopted
    as mechanistic evidence; the family name/signatures remain specific.
  snapshot_sha256: b91a95d3c03328d5bc9aed574996b6c0e5cef2c6a40bfc72039baa4cb8810562
- evidence_id: helicase52-agent-guy2009-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2807033/
  locator: 'Genuine PMC2807033: complete Introduction sec1, Results sec2.1 and sec2.6
    including Fig1/6/7 captions, complete Discussion sec3 and main Experimental Procedures
    sec4. Other Results, supplements and pixels not certified.'
  accessed_at: '2026-10-22T05:53:38.497487Z'
  support: supports
  summary: Guy2009 demonstrates Rep-assisted movement of oriC-initiated replication
    forks past protein barriers, direct Rep-DnaB association and enhanced unwinding.
    Its assay mixture does not contain PriC. Results sec2.6/Fig6I–J show DnaC inhibits
    Rep-DnaB interaction; the authors place this interaction after helicase loading.
    The Introduction separately cites earlier Rep/PriC restart work.
  snapshot_sha256: cb5888366879d2ddca22076b20b1dc8af5cfc6233e118fa24e2691a9d45a7d6e
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dnab_dnac_rep_pric_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:51:04Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dnab_dnac_rep_pric_complex.yaml'
  snapshot_sha256: d9e037f2d65079e0b0e504f4e10282481e15717ce8211d687ade07c2653dcf0f
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dnab_dnac_rep_pric_complex.yaml
    --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_rep_pric_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:51:05Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dnab_dnac_rep_pric_complex.yaml\
    \ --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_rep_pric_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_rep_pric_complex-strict.tsv"
  snapshot_sha256: e063e670d0ae3498b8c504102309b7198436f632fcec61c18c8df11eb92aca07
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:55:34.719767Z'
  support: supports
  summary: "data/structures/other/dnab_dnac_rep_pric_complex.yaml  (GO:1990160)\n\
    \  dnab_dnac_rep_pric_restart\trep_helicase\tCOVERED\t->rep_helicase (UniProtKB:P09980)\n\
    \  dnab_dnac_rep_pric_restart\tpric_restart_protein\tCOVERED\t->pric_restart_protein\
    \ (UniProtKB:P23862)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     2  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 6e9daeea33d397f83257ca4de9aacdc420b905a89c38bf3d23a0a5b10a4a6358
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T05:55:35.933130Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dnab_dnac_rep_pric_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '12 of 14 collected target identifiers returned OK. PMID:19941825: UNREACHABLE;
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
  topic: Native restart class remains distinct from the measured active fork
  outcome: concern
  target_ids:
  - GO:1990160
  summary: GO1990160 supports the maintained class and sibling exclusions. Native
    Rep/PriC annotations support a restart pathway, but Guy2009 is not a direct demonstration
    of the exact four-protein loading intermediate. NgII likewise studies a different
    PriA/PriB/PriC cohort.
  evidence_ids:
  - record
  - helicase52-agent-go
  - helicase52-agent-guy2009-legacy
  - helicase52-agent-ng1996ii-pdf
  - helicase52-agent-protein-P09980
  - helicase52-agent-protein-P23862
- assessment_id: grounding
  area: grounding
  topic: Exact Rep and PriC class mappings
  outcome: concern
  target_ids:
  - GO:1990160
  summary: IPR005752 and IPR010890 match the named full-protein classes and the separate
    native UniProt family xrefs. The mistaken hexamer sentence in the Rep family description
    is not promoted; exact signatures and hierarchy distinguish Rep from UvrD/PcrA.
    PAS-DNA remains unresolved rather than being mapped to oriC.
  evidence_ids:
  - record
  - curation
  - helicase52-agent-ipr-IPR005752
  - helicase52-agent-ipr-IPR010890
  - helicase52-agent-protein-P09980
  - helicase52-agent-protein-P23862
- assessment_id: examples
  area: identity
  topic: Correct Rep accession with inaccurate query uniqueness
  outcome: concern
  target_ids:
  - GO:1990160
  summary: P09980 remains the correct reviewed Rep helicase. The exact-organism reviewed
    rep query returns it plus P03856, a distinct RepE entry with rep alias. The evidence
    note calling P09980 the single reviewed hit is therefore too strong; PriC query
    uniqueness remains supported.
  evidence_ids:
  - record
  - helicase52-agent-protein-P09980
  - helicase52-agent-protein-P23862
  - helicase52-agent-gene-rep-exact83333
  - helicase52-agent-gene-priC-83333
- assessment_id: scope
  area: scope
  topic: Canonical experiment has a different stage and composition
  outcome: concern
  target_ids:
  - GO:1990160
  summary: Species562 and reference strain83333 are correct; COMMON keeps its majority-occurrence
    meaning without an empirical census. The canonical Guy experiment tests Rep accessory
    helicase at an already initiated oriC replisome, not an isolated DnaB-DnaC-Rep-PriC
    preprimosome. Its functional result cannot serve as direct confirmation of this
    exact cohort.
  evidence_ids:
  - record
  - schema
  - helicase52-agent-guy2009-legacy
  - helicase52-agent-go
  - helicase52-agent-tax562
  - helicase52-agent-tax83333
- assessment_id: graph
  area: graph
  topic: Coarse GO graph with source-limited empirical support
  outcome: concern
  target_ids:
  - GO:1990160
  summary: The NONMECHANISTIC graph accurately declares GO-level membership/restart
    scope, but empirical canonical support must be corrected. Guy main Methods omit
    PriC, and its DnaC competition result specifically distinguishes the active Rep-DnaB
    interaction from the loading complex. This does not refute all possible sequential
    Rep/PriC loading pathways.
  evidence_ids:
  - record
  - schema
  - helicase52-agent-go
  - helicase52-agent-guy2009-legacy
- assessment_id: formation
  area: grounding
  topic: Formation requirement remains unresolved for the exact quartet
  outcome: unknown
  target_ids:
  - GO:1990160
  summary: Rep deletion/complementation and fork-movement assays concern activity
    and viability; DnaC competition tests a different interaction stage. Neither establishes
    universal formation necessity of the maintained quartet or its PAS component.
  evidence_ids:
  - record
  - schema
  - helicase52-agent-guy2009-legacy
  - helicase52-agent-ng1996ii-pdf
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and unresolved boundaries
  outcome: supported
  target_ids:
  - GO:1990160
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
  issue_key: rep-pric-canonical-stage
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Use an exact Rep-PriC loading example rather than the active-fork experiment
  description: 'Guy2009 is the canonical example for this four-protein preprimosome,
    but its main replication assay omits PriC and studies Rep-assisted movement of
    oriC-initiated forks. Its Results explicitly show DnaC inhibition of Rep-DnaB
    binding and place that interaction after loading. NgII also does not supply the
    missing quartet: its retained PhiX assembly contains PriA/PriB/PriC/DnaT/DnaB.'
  target_ids:
  - GO:1990160
  field_paths:
  - canonical_examples[0]
  - taxonomic_distribution[0].reference
  - evidence
  evidence_ids:
  - record
  - helicase52-agent-go
  - helicase52-agent-guy2009-legacy
  - helicase52-agent-ng1996ii-pdf
  - helicase52-agent-protein-P09980
  - helicase52-agent-protein-P23862
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: major
  normalization_reason: A different experimental cohort and stage currently serves
    as the canonical exemplar of the entire structure. Correcting the citation alone
    is insufficient; the structure-to-experiment association must be reconciled.
- finding_id: F2
  issue_key: rep-pric-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground Rep and PriC with exact families
  description: Two reviewed-label-only rows defer exact mappings despite Rep IPR005752
    and PriC IPR010890, supported by exact family signatures and the separately verified
    examples.
  target_ids:
  - GO:1990160
  field_paths:
  - components#rep_helicase.grounding_status
  - components#pric_restart_protein.grounding_status
  - discussions#resolve_rep_pric_component_groundings
  evidence_ids:
  - record
  - curation
  - helicase52-agent-ipr-IPR005752
  - helicase52-agent-ipr-IPR010890
  - helicase52-agent-protein-P09980
  - helicase52-agent-protein-P23862
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correct protein identifiers remain
    intact; the issue is a bounded exact-family or evidence-attribution correction.
- finding_id: F3
  issue_key: rep-query-alias-uniqueness
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the Rep single-entry evidence note
  description: The maintained P09980 accession is correct, but the exact reviewed
    rep query for organism83333 also returns P03856 because rep is an alias for RepE.
    The current single-reviewed-entry claim is false at that stated query scope.
  target_ids:
  - GO:1990160
  field_paths:
  - components#rep_helicase.protein_examples[0].evidence
  evidence_ids:
  - record
  - helicase52-agent-protein-P09980
  - helicase52-agent-gene-rep-exact83333
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
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
  - GO:1990160
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
  description: Replace or explicitly contextualize Guy2009 as accessory-fork evidence,
    and use an independently verified exact Rep/PriC loading/restart source for the
    canonical quartet. Preserve the ontology identity and distinguish sequential loading
    from the active-fork complex.
  acceptance_checks:
  - Do not deny the native Rep/PriC restart pathway or infer that no such intermediate
    exists.
  - Do not claim Guy tested PriC or directly isolated the maintained quartet.
  - Keep the correct E.coli and reference-protein identifiers.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:1990160
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
  description: Apply the exact Rep/PriC protein-family identities and align current
    notes/TODO while retaining unresolved PAS DNA.
  acceptance_checks:
  - Do not import the erroneous Rep hexamer prose or substitute the generic UvrD/helicase
    domain.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:1990160
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
  description: Keep P09980 and replace the single-hit rationale with explicit Rep-helicase
    identity/alias disambiguation.
  acceptance_checks:
  - Acknowledge both returned identities without replacing Rep with RepE.
  - Leave dated historical actions unchanged.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
limitations:
- Five completed same-base batch26 global gates await guarded parent manifest/hash
  integration; this unsaved draft does not finalize or rerun corpus checks.
- No figure pixels, supplementary experimental data or deposited coordinate geometry
  were reanalyzed. Text/caption and native-response reading extents are stated individually.
- Guy main text was read only at the explicitly listed sections; supplemental Methods/strain
  table and image pixels were not independently inspected.
- GO1990160 and native UniProt support a Rep/PriC restart class, but the cited Guy
  and Ng experiments do not independently establish the canonical four-protein intermediate.
  This is not an exhaustive literature-absence claim.
- Rep family metadata has an inconsistent hexamer description. Family grounding relies
  on its exact name/type/signatures/hierarchy plus independent UniProt membership,
  not that sentence.
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
