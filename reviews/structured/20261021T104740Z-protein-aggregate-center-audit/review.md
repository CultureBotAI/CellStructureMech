# Protein aggregate center scope, intervention and provenance review

- Review: 20261021T104740Z-protein-aggregate-center-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:26:52Z
- Finished UTC: 2026-10-21T10:47:40Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The PAC umbrella identity, four bounded component classes, strain-specific intervention graphs and image/dataset metadata are supported. No concrete curation finding was established; broader assembly requirements and raw-data access remain limited.

## Scope And Provenance

Whole single-record scientific review, native identifiers, all three causal graphs, discussions, dataset metadata and frozen trackedFigure2; no neighboring scientific-record inference.

Selection: Batch20 index2, one frozen target in strict path order; no neighboring scientific record dependency.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0140453 | data/structures/inclusion/protein_aggregate_center.yaml | maintained | protein aggregate center |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0140453 | Target-specific read-only native check passed. |
| Native protein causal-graphs | passed | True | GO:0140453 | Target-specific read-only native check passed. |
| Focused native schema | passed | True | GO:0140453 | Focused validator passed. |
| Focused native strict | passed | True | GO:0140453 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0140453 | 12 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0140453 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0140453 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0140453 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0140453 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0140453 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0140453 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Umbrella identity and nomenclature

identity: supported. Targets: GO:0140453.

The reversible PAC identity and membraneless parent match native GO. Exact centre and broad PAC scopes are retained; source usage supports protein aggregate-like center. The target avoids exact equivalence to every INQ/CytoQ body or to severe-heat NuRs.

### Observed cargo and chaperones

completeness: supported. Targets: GO:0140453.

The heterogeneous client row and Hsp42/Btn2 constituents are supported by the specified reporter/time-course experiments. Hsp104 is associated disassembly machinery, not a small HSP. GFP reporter constructs are explicitly engineered probes rather than invariant endogenous subunits; Ydj1/Rsp5 phenotypes do not automatically establish residence.

### Condition-specific formation requirements

evidence: supported. Targets: GO:0140453.

Btn2 CONDITIONAL is supported by the specific Rho1/W303 formation defect while other reporter/background combinations retain foci. Hsp104 DISPENSABLE concerns formation, not its demonstrated clearance function: PACs still form in deletion cells. These labels do not claim the same requirement across all species or heat conditions.

### Unresolved cargo and small-HSP class necessity

evidence: unknown. Targets: GO:0140453.

The UNKNOWN cargo and small-HSP essentialities remain justified. Joint BTN2/HSP42 loss does not prove a universal individual or family-wide requirement; colocalization alone cannot establish necessity. Broader generalization of condition-specific requirements remains unresolved.

### Whole-protein class boundaries

grounding: supported. Targets: GO:0140453.

Native InterPro matches confirm Hsp42 in the small-HSP family. Btn2 supplies only a domain match, and available Hsp104 matches include broader ClpA/B families; the bounded label-only choices avoid replacing exact component classes with domains or overbroad families. Reviewed accessions, genes and S288C identities are correct.

### Yeast and reporter contexts

scope: supported. Targets: GO:0140453.

The2023 study directly compares fission-yeast972 with budding-yeastW303/BY4741 and describes differing persistence/requirements. S288C is explicitly only the reviewed reference-sequence taxon; none of these examples creates clade-wide prevalence or equates tagged reporters with native client inventories.

### Three intervention graphs

graph: supported. Targets: GO:0140453.

The graphs preserve37C induction, genotype/reporters, recovery25C with CHX added after assembly, and chronic heat as separate conditions. CHX-induced turnover is not equated with all translation inhibition; focus loss alone is not proteolysis. The2023 fluorescence and immunoblot experiments support the stated formation, maintenance and clearance edges.

### Reversible sequestration and delayed degradation

evidence: supported. Targets: GO:0140453.

Transient reporter sequestration and delayed turnover are supported under the specified assays, with recovery and prolonged-stress fates distinguished. The record does not promise that every deposited client is refolded or that degradation never occurs.

### Explicit bounded inventory and source-access TODOs

completeness: supported. Targets: GO:0140453.

Additional fission-yeast chaperone roles are now clearer from readable2020 primary text, but this heterogeneous structure is not presented as an exhaustive fixed complex. The existing expansion TODO is appropriate; new access does not make the earlier abstract-only statement false. No automatic finding is assigned for optional further examples.

### Dataset metadata and maintained figure

provenance: supported. Targets: GO:0140453.

The versioned dataset link/date/contributor/license are independently verified at metadata level; no raw-data analysis is claimed. Figure2 bytes match native source metadata and carry the documented CC BY4.0 attribution. Its content supports individual chaperone foci, not three-way colocalization.

### Source identity and readable extents

provenance: supported. Targets: GO:0140453.

Both cited DOI/PMID identities are exact. The2023 full JATS supports the principal claim inventory. The2020 browser-captured primary-text sections supplement the historical abstract read without upgrading the failed native publisher403 response to full text.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| pac-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140453,GO:0043232; results GO:0140453 name/definition/synonyms; GO:0043232 children entry for GO:0140453 | supports | GO:0140453 defines reversible misfolded-protein/chaperone aggregates that protect thermosensitive clients pending disaggregation/refolding. Native synonym scopes are exact centre and broad PAC; GO:0043232 lists this term as is_a. No exclusive nuclear/cytoplasmic parthood is supplied. |
| pac-agent-jats-PMC10342647 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.xml; JATS Results sec2dot1 through sec2dot5; Discussion sec3; Methods sec4dot1 through sec4dot7; Conclusions sec5; Figures1–4 and6 captions; Figure2 pixels separately recorded | supports | Results2.1–2.4 establish reporter- and strain-dependent PAC kinetics, Hsp42/Btn2/Hsp104 foci, joint sorting-factor effects, continued assembly without Hsp104 and delayed clearance/turnover. CHX at induction differs from recovery-only CHX; immunoblot turnover differs from focus loss. Results2.5/Discussion separate severe-heat NuRs and do not identify every indirect regulator as a constituent. Figure1c/Methods identify strains; Fig2 shows separate GFP-tagged chaperone time courses. |
| pac-agent-cabrera2020-browser2 | https://www.researchgate.net/publication/339340598_Chaperone-Facilitated_Aggregation_of_Thermo-Sensitive_Proteins_Shields_Them_from_Degradation_during_Heat_Stress; Printed pp2431–2435; Results reporter construction, Several Chaperones..., Mas5/Ssa2..., and stress-granule/CHX sections; captured lines359–1027 | supports | Primary browser text supports chaperone colocalization and separates strong Mas5 loss from partial Ssa2 effects. PACs and stress granules have distinct temperature requirements. |
| pac-agent-cabrera2020-browser3 | https://www.researchgate.net/publication/339340598_Chaperone-Facilitated_Aggregation_of_Thermo-Sensitive_Proteins_Shields_Them_from_Degradation_during_Heat_Stress; Printed pp2435–2438; Results degradation, refolding and endogenous-protein sections; captured lines1007–1372, with surrounding caption context | supports | Primary browser text distinguishes CHX/PUR and proteasome controls from recovery assays. Recovery restores GTP-bound reporter; Hsp104 dependence varies with prior temperature. |
| pac-agent-doi-10.3390_ijms241311202 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.3390/ijms241311202; hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear | supports | Exact DOI query resolves PMID:37446379, Formation of Transient Protein Aggregate-like Centers Is a General Strategy Postponing Degradation of Misfolded Intermediates., DOI 10.3390/ijms241311202. This binds bibliographic identity; body-level support is documented separately. |
| pac-agent-doi-10.1016_j.celrep.2020.01.077 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.celrep.2020.01.077&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear | supports | Exact DOI query resolves PMID:32075773, Chaperone-Facilitated Aggregation of Thermo-Sensitive Proteins Shields Them from Degradation during Heat Stress., DOI 10.1016/j.celrep.2020.01.077. This binds bibliographic identity; body-level support is documented separately. |
| pac-agent-Q12329 | https://rest.uniprot.org/uniprotkb/Q12329.json; primaryAccession; entryType; genes; proteinDescription; organism | supports | Native reviewed entry identifies Q12329, Heat shock protein 42, gene HSP42, taxon 559292. It verifies reference-sequence identity, while granule residence is assessed from the primary experiments. |
| pac-agent-P53286 | https://rest.uniprot.org/uniprotkb/P53286.json; primaryAccession; entryType; genes; proteinDescription; organism | supports | Native reviewed entry identifies P53286, Protein BTN2, gene BTN2, taxon 559292. It verifies reference-sequence identity, while granule residence is assessed from the primary experiments. |
| pac-agent-P31539 | https://rest.uniprot.org/uniprotkb/P31539.json; primaryAccession; entryType; genes; proteinDescription; organism | supports | Native reviewed entry identifies P31539, Heat shock protein 104, gene HSP104, taxon 559292. It verifies reference-sequence identity, while granule residence is assessed from the primary experiments. |
| pac-agent-IPR031107 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031107/; metadata accession, name and type; description only where explicitly non-LLM | supports | Native entry IPR031107 is type family, named Small heat shock protein. This establishes sequence-class scope, not localization or assembly necessity. |
| pac-agent-IPR001270 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/; metadata accession, name and type; description only where explicitly non-LLM | supports | Native entry IPR001270 is type family, named ClpA/B family. This establishes sequence-class scope, not localization or assembly necessity. |
| pac-agent-IPR050130 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/; metadata accession, name and type; description only where explicitly non-LLM | supports | Native entry IPR050130 is type family, named ATP-dependent Clp protease/Chaperone ClpA/ClpB. This establishes sequence-class scope, not localization or assembly necessity. |
| pac-agent-ipr-matches-Q12329 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12329/?page_size=200; count; next; results[].metadata accession/name/type | supports | Complete integrated InterPro response for Q12329: 3 matches, next=null; family entries: IPR031107 Small heat shock protein. Other matches are domains, sites or superfamilies, not exact whole-protein class identifiers. |
| pac-agent-interpro-P53286 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P53286/?page_size=200; count; next; results[].metadata accession/name/type | supports | Complete integrated InterPro response for P53286: 1 matches, next=null; family entries: none. Other matches are domains, sites or superfamilies, not exact whole-protein class identifiers. |
| pac-agent-ipr-matches-P31539 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200; count; next; results[].metadata accession/name/type | supports | Complete integrated InterPro response for P31539: 11 matches, next=null; family entries: IPR001270 ClpA/B family; IPR050130 ATP-dependent Clp protease/Chaperone ClpA/ClpB. Other matches are domains, sites or superfamilies, not exact whole-protein class identifiers. |
| pac-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId; scientificName; rank; lineage | supports | Native taxonomy resolves 4932 to Saccharomyces cerevisiae, rank species. Species and reference-strain identities remain distinct from the experimental genotypes. |
| pac-agent-tax-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; taxId; scientificName; rank; lineage | supports | Native taxonomy resolves 4896 to Schizosaccharomyces pombe, rank species. Species and reference-strain identities remain distinct from the experimental genotypes. |
| pac-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId; scientificName; rank; lineage | supports | Native taxonomy resolves 559292 to Saccharomyces cerevisiae S288C, rank strain. Species and reference-strain identities remain distinct from the experimental genotypes. |
| pac-agent-mendeley-datacite | https://api.datacite.org/dois/10.17632/z3hvg9wtvg.2; data.attributes doi/titles/creators/dates/rightsList/url/descriptions | supports | Native DataCite resolves DOI10.17632/z3hvg9wtvg.2 and its version2 landing URL, article-matching title/description, contributor Margarita Cabrera, issued date2023-03-21 and CC BY4.0. This verifies metadata only; the abbreviated target dataset title is a descriptive label, not a verbatim title quote. |
| tracked-figure2 | data/images/inclusion/protein_aggregate_center/pmc10342647_ijms_24_11202_f002.jpg; Entire Figure2 visually inspected: BY4741 Btn2-GFP, Hsp42-GFP and Hsp104-GFP rows at25C and15–120min37C | context_only | The tracked figure shows separate reporter time courses and the stated5micrometre bar, not simultaneous three-way colocalization. The target correctly avoids the original caption’s mistaken classification of Hsp104 as a small HSP. |
| pac-agent-native-package-PMC10342647 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.json; pmcid/title/license_code; media_urls ijms-24-11202-g002.jpg MD5 | supports | Native package identifies the2023 article and CC BY license; Figure2 media filename/MD5 exactly matches the tracked file. This package identifies the license family; its exact version is checked separately in JATS permissions. |
| pac-figure-license | https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.xml; front/article-meta/permissions; fig[@id=ijms-24-11202-f002]/caption | supports | JATS permissions specify CC BY4.0 for the2023 article. Figure2 caption identifies separate GFP-tagged chaperone imaging at37C and5micrometre scale; the target avoids its Hsp104 classification error. |
| native-verify | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml --verify; Entire target-specific native log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml --causal-graphs; Entire target-specific native log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/inclusion/protein_aggregate_center.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/inclusion/protein_aggregate_center.yaml |
| strict-result | just validate-strict data/structures/inclusion/protein_aggregate_center.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/protein_aggregate_center-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/inclusion/protein_aggregate_center.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/protein_aggregate_center-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/protein_aggregate_center-strict.tsv |
| target-curies | just check-curies-strict; data/structures/inclusion/protein_aggregate_center.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 12 of12 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Boronat2023 Results2.1–2.5, Discussion, Methods4.1–4.7, Conclusions and claim-bearing Figure1–4/6 captions were read. TrackedFigure2 pixels were inspected. Complete supplements, raw microscopy and underlying immunoblot datasets were not reanalyzed; source-reported supplemental outcomes are not presented as independently inspected supplemental images.
- Cabrera2020 primary body was partially recovered as browser-indexed article text, including chaperone colocalization/deletions, stress-granule boundary, turnover, recovery and endogenous-client Results. The full Methods, complete supplements and original figure pixels were not read; OCR artifacts are retained. Native publisher download remained403. This is not a claim of complete full-paper inspection.
- DataCite metadata was read for the version2 dataset. Mendeley native landing/API requests returned403; manifest/files and raw archives were not inspected. The record itself claims metadata-only use.
- Family absence conclusions are bounded to complete native protein-match responses and specific candidate metadata. IPR050130 LLM-generated description is not used as scientific evidence. Unknown component-class assembly necessities remain unknown rather than inferred from localization or clearance functions.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104740Z-protein-aggregate-center-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Protein aggregate center scope, intervention and provenance review
started_at: '2026-10-21T10:26:52Z'
finished_at: '2026-10-21T10:47:40Z'
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
summary: The PAC umbrella identity, four bounded component classes, strain-specific
  intervention graphs and image/dataset metadata are supported. No concrete curation
  finding was established; broader assembly requirements and raw-data access remain
  limited.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/images/inclusion/protein_aggregate_center/pmc10342647_ijms_24_11202_f002.jpg
    sha256: 7d9c957cdb378c0a51800a3890e66cf2d0d0b05d7596bf0e220e0224b374c6da
    role: context
  - path: data/structures/inclusion/protein_aggregate_center.yaml
    sha256: c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b
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
- target_id: GO:0140453
  path: data/structures/inclusion/protein_aggregate_center.yaml
  label: protein aggregate center
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/protein_aggregate_center.yaml
    role: maintained scientific record
scope:
  description: Whole single-record scientific review, native identifiers, all three
    causal graphs, discussions, dataset metadata and frozen trackedFigure2; no neighboring
    scientific-record inference.
  selection: Batch20 index2, one frozen target in strict path order; no neighboring
    scientific record dependency.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0140453
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0140453
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml
    --verify
  exit_code: 0
  summary: Target-specific read-only native check passed.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0140453
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml
    --causal-graphs
  exit_code: 0
  summary: Target-specific read-only native check passed.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0140453
  command: just validate data/structures/inclusion/protein_aggregate_center.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0140453
  command: just validate-strict data/structures/inclusion/protein_aggregate_center.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/protein_aggregate_center-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0140453
  summary: 12 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0140453
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - pac-agent-go
  - pac-agent-jats-PMC10342647
  - pac-agent-cabrera2020-browser2
  - pac-agent-cabrera2020-browser3
  - pac-agent-doi-10.3390_ijms241311202
  - pac-agent-doi-10.1016_j.celrep.2020.01.077
  - pac-agent-Q12329
  - pac-agent-P53286
  - pac-agent-P31539
  - pac-agent-IPR031107
  - pac-agent-IPR001270
  - pac-agent-IPR050130
  - pac-agent-ipr-matches-Q12329
  - pac-agent-interpro-P53286
  - pac-agent-ipr-matches-P31539
  - pac-agent-tax-4932
  - pac-agent-tax-4896
  - pac-agent-tax-559292
  - pac-agent-mendeley-datacite
  - tracked-figure2
  - pac-agent-native-package-PMC10342647
  - pac-figure-license
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0140453
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
  - GO:0140453
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
  - GO:0140453
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
  - GO:0140453
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
  - GO:0140453
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
- evidence_id: pac-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140453,GO:0043232
  locator: results GO:0140453 name/definition/synonyms; GO:0043232 children entry
    for GO:0140453
  accessed_at: '2026-10-21T10:28:46Z'
  support: supports
  summary: GO:0140453 defines reversible misfolded-protein/chaperone aggregates that
    protect thermosensitive clients pending disaggregation/refolding. Native synonym
    scopes are exact centre and broad PAC; GO:0043232 lists this term as is_a. No
    exclusive nuclear/cytoplasmic parthood is supplied.
  snapshot_sha256: 2612362e16b1c36800877883e55dc3674c9576febc2243bf963a6a8eaa64efce
- evidence_id: pac-agent-jats-PMC10342647
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.xml
  locator: JATS Results sec2dot1 through sec2dot5; Discussion sec3; Methods sec4dot1
    through sec4dot7; Conclusions sec5; Figures1–4 and6 captions; Figure2 pixels separately
    recorded
  accessed_at: '2026-10-21T10:17:53.990542Z'
  support: supports
  summary: Results2.1–2.4 establish reporter- and strain-dependent PAC kinetics, Hsp42/Btn2/Hsp104
    foci, joint sorting-factor effects, continued assembly without Hsp104 and delayed
    clearance/turnover. CHX at induction differs from recovery-only CHX; immunoblot
    turnover differs from focus loss. Results2.5/Discussion separate severe-heat NuRs
    and do not identify every indirect regulator as a constituent. Figure1c/Methods
    identify strains; Fig2 shows separate GFP-tagged chaperone time courses.
  snapshot_sha256: 0d9e2ef9309ef2e4467b02c001c4919d47818a1423120307660a6fee775d7552
- evidence_id: pac-agent-cabrera2020-browser2
  kind: primary_source
  reference: https://www.researchgate.net/publication/339340598_Chaperone-Facilitated_Aggregation_of_Thermo-Sensitive_Proteins_Shields_Them_from_Degradation_during_Heat_Stress
  locator: Printed pp2431–2435; Results reporter construction, Several Chaperones...,
    Mas5/Ssa2..., and stress-granule/CHX sections; captured lines359–1027
  accessed_at: '2026-10-21T10:32:33Z'
  support: supports
  summary: Primary browser text supports chaperone colocalization and separates strong
    Mas5 loss from partial Ssa2 effects. PACs and stress granules have distinct temperature
    requirements.
  snapshot_sha256: 552676c93f2feb2aef1f0ae6d3f20ecf31e31821d3e50ddcd14656ec9cede042
- evidence_id: pac-agent-cabrera2020-browser3
  kind: primary_source
  reference: https://www.researchgate.net/publication/339340598_Chaperone-Facilitated_Aggregation_of_Thermo-Sensitive_Proteins_Shields_Them_from_Degradation_during_Heat_Stress
  locator: Printed pp2435–2438; Results degradation, refolding and endogenous-protein
    sections; captured lines1007–1372, with surrounding caption context
  accessed_at: '2026-10-21T10:33:05Z'
  support: supports
  summary: Primary browser text distinguishes CHX/PUR and proteasome controls from
    recovery assays. Recovery restores GTP-bound reporter; Hsp104 dependence varies
    with prior temperature.
  snapshot_sha256: 6b96ce876d4d2fe8d640582e33e58404a65f71baa53012be2200770e97e833bd
- evidence_id: pac-agent-doi-10.3390_ijms241311202
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.3390/ijms241311202
  locator: hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear
  accessed_at: '2026-10-21T10:17:23.540161Z'
  support: supports
  summary: Exact DOI query resolves PMID:37446379, Formation of Transient Protein
    Aggregate-like Centers Is a General Strategy Postponing Degradation of Misfolded
    Intermediates., DOI 10.3390/ijms241311202. This binds bibliographic identity;
    body-level support is documented separately.
  snapshot_sha256: 12234535d2cce14fbfa7268e778c4b46a93d4f24177284616313ac283c82a43a
- evidence_id: pac-agent-doi-10.1016_j.celrep.2020.01.077
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.celrep.2020.01.077&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear
  accessed_at: '2026-10-21T10:28:44Z'
  support: supports
  summary: Exact DOI query resolves PMID:32075773, Chaperone-Facilitated Aggregation
    of Thermo-Sensitive Proteins Shields Them from Degradation during Heat Stress.,
    DOI 10.1016/j.celrep.2020.01.077. This binds bibliographic identity; body-level
    support is documented separately.
  snapshot_sha256: 7cefb0dc8cebed0766dc384ffcdffc8c2de6c3e3269088519783b1bb47d77cab
- evidence_id: pac-agent-Q12329
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12329.json
  locator: primaryAccession; entryType; genes; proteinDescription; organism
  accessed_at: '2026-10-21T10:15:28.493398Z'
  support: supports
  summary: Native reviewed entry identifies Q12329, Heat shock protein 42, gene HSP42,
    taxon 559292. It verifies reference-sequence identity, while granule residence
    is assessed from the primary experiments.
  snapshot_sha256: 2fd80fe65790b403d51e6d01659e4c94ec91a1455e5b4be00301e2350656a1cc
- evidence_id: pac-agent-P53286
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53286.json
  locator: primaryAccession; entryType; genes; proteinDescription; organism
  accessed_at: '2026-10-21T10:16:27.877044Z'
  support: supports
  summary: Native reviewed entry identifies P53286, Protein BTN2, gene BTN2, taxon
    559292. It verifies reference-sequence identity, while granule residence is assessed
    from the primary experiments.
  snapshot_sha256: d0122a2554484d191dfb1e8f702aeaca61392ab658f762dbc30916c27580c110
- evidence_id: pac-agent-P31539
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P31539.json
  locator: primaryAccession; entryType; genes; proteinDescription; organism
  accessed_at: '2026-10-21T10:15:28.994133Z'
  support: supports
  summary: Native reviewed entry identifies P31539, Heat shock protein 104, gene HSP104,
    taxon 559292. It verifies reference-sequence identity, while granule residence
    is assessed from the primary experiments.
  snapshot_sha256: 8636decea760cdb2a2da238bfa589822867a778a41fd6a04c45a74fe5802ee13
- evidence_id: pac-agent-IPR031107
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031107/
  locator: metadata accession, name and type; description only where explicitly non-LLM
  accessed_at: '2026-10-21T10:15:30.788260Z'
  support: supports
  summary: Native entry IPR031107 is type family, named Small heat shock protein.
    This establishes sequence-class scope, not localization or assembly necessity.
  snapshot_sha256: 7db6f5da4dd897dfbcaa6435cbeb744a4691f43cb10433977995a30bb1d91293
- evidence_id: pac-agent-IPR001270
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/
  locator: metadata accession, name and type; description only where explicitly non-LLM
  accessed_at: '2026-10-21T10:15:31.115090Z'
  support: supports
  summary: Native entry IPR001270 is type family, named ClpA/B family. This establishes
    sequence-class scope, not localization or assembly necessity.
  snapshot_sha256: ed0a09c17fa611e58cd0d00b904d4dce2757228cd7e411301eddcfb9b391e0dd
- evidence_id: pac-agent-IPR050130
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/
  locator: metadata accession, name and type; description only where explicitly non-LLM
  accessed_at: '2026-10-21T10:15:31.421976Z'
  support: supports
  summary: Native entry IPR050130 is type family, named ATP-dependent Clp protease/Chaperone
    ClpA/ClpB. This establishes sequence-class scope, not localization or assembly
    necessity.
  snapshot_sha256: e654bc8d2d359d203a225be0690247071616a63341156fcd507f197717f78701
- evidence_id: pac-agent-ipr-matches-Q12329
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12329/?page_size=200
  locator: count; next; results[].metadata accession/name/type
  accessed_at: '2026-10-21T10:15:28.547223Z'
  support: supports
  summary: 'Complete integrated InterPro response for Q12329: 3 matches, next=null;
    family entries: IPR031107 Small heat shock protein. Other matches are domains,
    sites or superfamilies, not exact whole-protein class identifiers.'
  snapshot_sha256: b5fd5350c5ea8e5ac5d6bdda8ab01a8f4ab0036d09974a5a02fce9361203a6a2
  search_scope: Remote public InterPro integrated entries matching exactly UniProt
    Q12329; all 3 returned entries read and next=null. Filesystem ignore rules are
    not applicable to this bounded remote query; no assertion of local-file absence
    or exhaustive absence across every ontology.
- evidence_id: pac-agent-interpro-P53286
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P53286/?page_size=200
  locator: count; next; results[].metadata accession/name/type
  accessed_at: '2026-10-21T10:16:28.014916Z'
  support: supports
  summary: 'Complete integrated InterPro response for P53286: 1 matches, next=null;
    family entries: none. Other matches are domains, sites or superfamilies, not exact
    whole-protein class identifiers.'
  snapshot_sha256: 2150123692223413fbe5ca58407117f0775384d53d6c3c9d16f7af500dbea6ab
  search_scope: Remote public InterPro integrated entries matching exactly UniProt
    P53286; all 1 returned entries read and next=null. Filesystem ignore rules are
    not applicable to this bounded remote query; no assertion of local-file absence
    or exhaustive absence across every ontology.
- evidence_id: pac-agent-ipr-matches-P31539
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200
  locator: count; next; results[].metadata accession/name/type
  accessed_at: '2026-10-21T10:15:29.150971Z'
  support: supports
  summary: 'Complete integrated InterPro response for P31539: 11 matches, next=null;
    family entries: IPR001270 ClpA/B family; IPR050130 ATP-dependent Clp protease/Chaperone
    ClpA/ClpB. Other matches are domains, sites or superfamilies, not exact whole-protein
    class identifiers.'
  snapshot_sha256: 750867aa538d4dd5c6c6a982138e7401b8b788d9653ecb84bf5d145c8ff6d3ee
  search_scope: Remote public InterPro integrated entries matching exactly UniProt
    P31539; all 11 returned entries read and next=null. Filesystem ignore rules are
    not applicable to this bounded remote query; no assertion of local-file absence
    or exhaustive absence across every ontology.
- evidence_id: pac-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId; scientificName; rank; lineage
  accessed_at: '2026-10-21T10:15:30.282122Z'
  support: supports
  summary: Native taxonomy resolves 4932 to Saccharomyces cerevisiae, rank species.
    Species and reference-strain identities remain distinct from the experimental
    genotypes.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: pac-agent-tax-4896
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: taxId; scientificName; rank; lineage
  accessed_at: '2026-10-21T10:28:46Z'
  support: supports
  summary: Native taxonomy resolves 4896 to Schizosaccharomyces pombe, rank species.
    Species and reference-strain identities remain distinct from the experimental
    genotypes.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: pac-agent-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId; scientificName; rank; lineage
  accessed_at: '2026-10-21T10:15:30.380033Z'
  support: supports
  summary: Native taxonomy resolves 559292 to Saccharomyces cerevisiae S288C, rank
    strain. Species and reference-strain identities remain distinct from the experimental
    genotypes.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: pac-agent-mendeley-datacite
  kind: database
  reference: https://api.datacite.org/dois/10.17632/z3hvg9wtvg.2
  locator: data.attributes doi/titles/creators/dates/rightsList/url/descriptions
  accessed_at: '2026-10-21T10:30:40Z'
  support: supports
  summary: Native DataCite resolves DOI10.17632/z3hvg9wtvg.2 and its version2 landing
    URL, article-matching title/description, contributor Margarita Cabrera, issued
    date2023-03-21 and CC BY4.0. This verifies metadata only; the abbreviated target
    dataset title is a descriptive label, not a verbatim title quote.
  snapshot_sha256: 63433417e861604b5d15f61d207b47669e38e48be2a89d88284a66fdc19a3f02
- evidence_id: tracked-figure2
  kind: record_content
  reference: data/images/inclusion/protein_aggregate_center/pmc10342647_ijms_24_11202_f002.jpg
  locator: 'Entire Figure2 visually inspected: BY4741 Btn2-GFP, Hsp42-GFP and Hsp104-GFP
    rows at25C and15–120min37C'
  accessed_at: '2026-10-21T10:35:37Z'
  support: context_only
  summary: The tracked figure shows separate reporter time courses and the stated5micrometre
    bar, not simultaneous three-way colocalization. The target correctly avoids the
    original caption’s mistaken classification of Hsp104 as a small HSP.
  snapshot_sha256: 7d9c957cdb378c0a51800a3890e66cf2d0d0b05d7596bf0e220e0224b374c6da
- evidence_id: pac-agent-native-package-PMC10342647
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.json
  locator: pmcid/title/license_code; media_urls ijms-24-11202-g002.jpg MD5
  accessed_at: '2026-10-21T10:17:53.515129Z'
  support: supports
  summary: Native package identifies the2023 article and CC BY license; Figure2 media
    filename/MD5 exactly matches the tracked file. This package identifies the license
    family; its exact version is checked separately in JATS permissions.
  snapshot_sha256: 3c1b51d3c79b6d45de60c44b57038bcd6baca139e8e531d549a36f570cf1eda5
- evidence_id: pac-figure-license
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.xml
  locator: front/article-meta/permissions; fig[@id=ijms-24-11202-f002]/caption
  accessed_at: '2026-10-21T10:17:53.990542Z'
  support: supports
  summary: JATS permissions specify CC BY4.0 for the2023 article. Figure2 caption
    identifies separate GFP-tagged chaperone imaging at37C and5micrometre scale; the
    target avoids its Hsp104 classification error.
  snapshot_sha256: 0d9e2ef9309ef2e4467b02c001c4919d47818a1423120307660a6fee775d7552
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml
    --verify
  locator: Entire target-specific native log
  accessed_at: '2026-10-21T10:32:06.096169Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml
    --causal-graphs
  locator: Entire target-specific native log
  accessed_at: '2026-10-21T10:32:06.556918Z'
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
  reference: just validate data/structures/inclusion/protein_aggregate_center.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:26:54Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/inclusion/protein_aggregate_center.yaml'
  snapshot_sha256: 05a39a7474e7e87ce4019cad9740579dacb2716f9d91c57525bb838e6954ab11
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/inclusion/protein_aggregate_center.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/protein_aggregate_center-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:26:56Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/inclusion/protein_aggregate_center.yaml\
    \ --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/protein_aggregate_center-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/protein_aggregate_center-strict.tsv"
  snapshot_sha256: 8a5e8d0470865a5142fd0800ac30f12355f0a38375f021e1a1f34f2c4f79474d
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/inclusion/protein_aggregate_center.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:35:37Z'
  support: supports
  summary: '12 of12 collected target identifiers returned OK in this fresh base resolver
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
  topic: Umbrella identity and nomenclature
  outcome: supported
  target_ids:
  - GO:0140453
  summary: The reversible PAC identity and membraneless parent match native GO. Exact
    centre and broad PAC scopes are retained; source usage supports protein aggregate-like
    center. The target avoids exact equivalence to every INQ/CytoQ body or to severe-heat
    NuRs.
  evidence_ids:
  - pac-agent-go
  - pac-agent-jats-PMC10342647
- assessment_id: composition
  area: completeness
  topic: Observed cargo and chaperones
  outcome: supported
  target_ids:
  - GO:0140453
  summary: The heterogeneous client row and Hsp42/Btn2 constituents are supported
    by the specified reporter/time-course experiments. Hsp104 is associated disassembly
    machinery, not a small HSP. GFP reporter constructs are explicitly engineered
    probes rather than invariant endogenous subunits; Ydj1/Rsp5 phenotypes do not
    automatically establish residence.
  evidence_ids:
  - pac-agent-jats-PMC10342647
  - pac-agent-Q12329
  - pac-agent-P53286
  - pac-agent-P31539
- assessment_id: conditional-necessity
  area: evidence
  topic: Condition-specific formation requirements
  outcome: supported
  target_ids:
  - GO:0140453
  summary: 'Btn2 CONDITIONAL is supported by the specific Rho1/W303 formation defect
    while other reporter/background combinations retain foci. Hsp104 DISPENSABLE concerns
    formation, not its demonstrated clearance function: PACs still form in deletion
    cells. These labels do not claim the same requirement across all species or heat
    conditions.'
  evidence_ids:
  - pac-agent-jats-PMC10342647
- assessment_id: unknown-necessity
  area: evidence
  topic: Unresolved cargo and small-HSP class necessity
  outcome: unknown
  target_ids:
  - GO:0140453
  summary: The UNKNOWN cargo and small-HSP essentialities remain justified. Joint
    BTN2/HSP42 loss does not prove a universal individual or family-wide requirement;
    colocalization alone cannot establish necessity. Broader generalization of condition-specific
    requirements remains unresolved.
  evidence_ids:
  - pac-agent-jats-PMC10342647
- assessment_id: grounding
  area: grounding
  topic: Whole-protein class boundaries
  outcome: supported
  target_ids:
  - GO:0140453
  summary: Native InterPro matches confirm Hsp42 in the small-HSP family. Btn2 supplies
    only a domain match, and available Hsp104 matches include broader ClpA/B families;
    the bounded label-only choices avoid replacing exact component classes with domains
    or overbroad families. Reviewed accessions, genes and S288C identities are correct.
  evidence_ids:
  - pac-agent-Q12329
  - pac-agent-P53286
  - pac-agent-P31539
  - pac-agent-IPR031107
  - pac-agent-IPR001270
  - pac-agent-IPR050130
  - pac-agent-ipr-matches-Q12329
  - pac-agent-interpro-P53286
  - pac-agent-ipr-matches-P31539
- assessment_id: taxa
  area: scope
  topic: Yeast and reporter contexts
  outcome: supported
  target_ids:
  - GO:0140453
  summary: The2023 study directly compares fission-yeast972 with budding-yeastW303/BY4741
    and describes differing persistence/requirements. S288C is explicitly only the
    reviewed reference-sequence taxon; none of these examples creates clade-wide prevalence
    or equates tagged reporters with native client inventories.
  evidence_ids:
  - pac-agent-jats-PMC10342647
  - pac-agent-tax-4932
  - pac-agent-tax-4896
  - pac-agent-tax-559292
  - pac-agent-Q12329
  - pac-agent-P53286
  - pac-agent-P31539
- assessment_id: graphs
  area: graph
  topic: Three intervention graphs
  outcome: supported
  target_ids:
  - GO:0140453
  summary: The graphs preserve37C induction, genotype/reporters, recovery25C with
    CHX added after assembly, and chronic heat as separate conditions. CHX-induced
    turnover is not equated with all translation inhibition; focus loss alone is not
    proteolysis. The2023 fluorescence and immunoblot experiments support the stated
    formation, maintenance and clearance edges.
  evidence_ids:
  - pac-agent-jats-PMC10342647
- assessment_id: function
  area: evidence
  topic: Reversible sequestration and delayed degradation
  outcome: supported
  target_ids:
  - GO:0140453
  summary: Transient reporter sequestration and delayed turnover are supported under
    the specified assays, with recovery and prolonged-stress fates distinguished.
    The record does not promise that every deposited client is refolded or that degradation
    never occurs.
  evidence_ids:
  - pac-agent-go
  - pac-agent-jats-PMC10342647
- assessment_id: completeness
  area: completeness
  topic: Explicit bounded inventory and source-access TODOs
  outcome: supported
  target_ids:
  - GO:0140453
  summary: Additional fission-yeast chaperone roles are now clearer from readable2020
    primary text, but this heterogeneous structure is not presented as an exhaustive
    fixed complex. The existing expansion TODO is appropriate; new access does not
    make the earlier abstract-only statement false. No automatic finding is assigned
    for optional further examples.
  evidence_ids:
  - pac-agent-jats-PMC10342647
  - pac-agent-cabrera2020-browser2
  - pac-agent-cabrera2020-browser3
- assessment_id: dataset-image
  area: provenance
  topic: Dataset metadata and maintained figure
  outcome: supported
  target_ids:
  - GO:0140453
  summary: The versioned dataset link/date/contributor/license are independently verified
    at metadata level; no raw-data analysis is claimed. Figure2 bytes match native
    source metadata and carry the documented CC BY4.0 attribution. Its content supports
    individual chaperone foci, not three-way colocalization.
  evidence_ids:
  - pac-agent-mendeley-datacite
  - pac-agent-native-package-PMC10342647
  - pac-figure-license
  - tracked-figure2
  - pac-agent-jats-PMC10342647
- assessment_id: provenance
  area: provenance
  topic: Source identity and readable extents
  outcome: supported
  target_ids:
  - GO:0140453
  summary: Both cited DOI/PMID identities are exact. The2023 full JATS supports the
    principal claim inventory. The2020 browser-captured primary-text sections supplement
    the historical abstract read without upgrading the failed native publisher403
    response to full text.
  evidence_ids:
  - pac-agent-doi-10.3390_ijms241311202
  - pac-agent-doi-10.1016_j.celrep.2020.01.077
  - pac-agent-jats-PMC10342647
  - pac-agent-cabrera2020-browser2
  - pac-agent-cabrera2020-browser3
findings: []
actions: []
limitations:
- Boronat2023 Results2.1–2.5, Discussion, Methods4.1–4.7, Conclusions and claim-bearing
  Figure1–4/6 captions were read. TrackedFigure2 pixels were inspected. Complete supplements,
  raw microscopy and underlying immunoblot datasets were not reanalyzed; source-reported
  supplemental outcomes are not presented as independently inspected supplemental
  images.
- Cabrera2020 primary body was partially recovered as browser-indexed article text,
  including chaperone colocalization/deletions, stress-granule boundary, turnover,
  recovery and endogenous-client Results. The full Methods, complete supplements and
  original figure pixels were not read; OCR artifacts are retained. Native publisher
  download remained403. This is not a claim of complete full-paper inspection.
- DataCite metadata was read for the version2 dataset. Mendeley native landing/API
  requests returned403; manifest/files and raw archives were not inspected. The record
  itself claims metadata-only use.
- Family absence conclusions are bounded to complete native protein-match responses
  and specific candidate metadata. IPR050130 LLM-generated description is not used
  as scientific evidence. Unknown component-class assembly necessities remain unknown
  rather than inferred from localization or clearance functions.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
