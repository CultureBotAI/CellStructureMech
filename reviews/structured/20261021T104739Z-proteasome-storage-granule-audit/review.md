# Proteasome storage granule identity, source integrity and recovery review

- Review: 20261021T104739Z-proteasome-storage-granule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:26:49Z
- Finished UTC: 2026-10-21T10:47:39Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The PSG identity, supported constituent subset, recovery graph and source exclusions are coherent. No concrete curation finding was established; assembly necessity and universal architecture remain bounded.

## Scope And Provenance

Whole single-record scientific review, all components/examples, all graph edges, source-limit discussions, native identifiers and the linked source figure.

Selection: Batch20 index1, one frozen target in strict path order; no neighboring scientific record dependency.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0034515 | data/structures/inclusion/proteasome_storage_granule.yaml | maintained | proteasome storage granule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0034515 | Target-specific read-only native check passed. |
| Native protein causal-graphs | passed | True | GO:0034515 | Target-specific read-only native check passed. |
| Focused native schema | passed | True | GO:0034515 | Focused validator passed. |
| Focused native strict | passed | True | GO:0034515 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0034515 | 17 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0034515 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0034515 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0034515 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0034515 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0034515 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0034515 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Identity, synonym and hierarchy

identity: supported. Targets: GO:0034515.

The PSG ontology identity, related abbreviation, membraneless parent and cytoplasmic parthood agree with native GO and the2008 experiments. Core/regulatory has_part assertions are supported by directly observed constituents. Nuclear proteasome assemblies in2026 are not silently substituted for the bounded cytoplasmic GO class.

### Supported constituent subset

completeness: supported. Targets: GO:0034515.

Core and regulatory particles, Blm10, Ubp6 and free ubiquitin have direct localization or enrichment support. Single protein accessions are reference examples, not whole-complex identifiers. P0CG63 is the UBI4 polyubiquitin precursor, distinguished from processed unconjugated ubiquitin and the engineered reporter. Upstream screen hits are correctly excluded without residence evidence.

### Assembly necessity remains unresolved

evidence: unknown. Targets: GO:0034515.

All five component essentialities are UNKNOWN. The studies contain condition-dependent depletion/active-site phenotypes but do not establish universal necessity of each component class across PSG states. Genetic effects, constitutive proteasome function and direct localization are not interchangeable with granule assembly necessity.

### Family and mature-product boundaries

grounding: supported. Targets: GO:0034515.

InterPro identifies the Blm10 and Ubp6 families, with matching reviewed proteins and correct genes/taxon. Complete P0CG63 matches do not supply an exact source-neutral unconjugated mature-ubiquitin identity: domains/sites and the broader ubiquitin-and-ubiquitin-like family are not exact replacements. The bounded label-only TODO is justified by these checked candidates.

### Experimental versus reference strains

scope: supported. Targets: GO:0034515.

Budding yeast BY4741/2/3-derived assays and fission yeast endogenous Pad1-GFP provide source-backed examples. S288C559292 remains a reference-sequence identity, not a reassignment of every experiment; no broad lineage prevalence is asserted.

### Intervention-supported mobilization

graph: supported. Targets: GO:0034515.

Both fresh-YPD edges are supported within the four-day Pre6-GFP assay. Water transfer and cycloheximide controls support mobilization of existing material; the graph makes no resolved molecular dissolution, proteolysis or protection-from-autophagy claim.

### Intact assemblies versus extract models

evidence: supported. Targets: GO:0034515.

The record correctly separates2008 colocalization/activity uncertainty,2017 lysate dissociation and2026 in situ architecture. Newly recovered full text reinforces intact26S arrays in measured states and unresolved associated factors/dissolution details. An open expansion TODO is not a false historical access claim or a mandatory inventory omission.

### Retraction exclusion and bibliographic integrity

provenance: supported. Targets: GO:0034515.

The independently supported2008/2017 claims survive exclusion of the2018 retracted study and derivative commentary. All exact cited DOI/PMID identities resolve natively. No Arabidopsis or proteaphagy-protection claim is imported from the withdrawn evidence.

### Figure identity and licensing

provenance: supported. Targets: GO:0034515.

The link-only2008Figure2 has the stated reporter colocalization/time-course content and2micrometre scale; the source permission is CC BY-NC-SA3.0 rather than CC BY. No maintained image file is claimed for this row.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| psg-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034515,GO:0043232,GO:0005737,GO:0005839,GO:0005838; results for all five identifiers: names/definitions/synonyms; GO:0043232 and GO:0005737 children entries for GO:0034515 | supports | GO:0034515 is the active PSG cellular-component identity with related synonym PSG. The native parent response includes it as is_a GO:0043232, and cytoplasm includes it as part_of. GO:0005839 and GO:0005838 identify core and regulatory complexes. These are class identities, not proof that every fluorescent focus has one universal particle configuration. |
| psg-agent-jats-PMC2396804 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/PMC2396804.1.xml; All five Results and discussion subsections; Materials and methods strain/growth, GFP fusion and Microscopy sections; Figs1–5 captions, especially Fig2 and Fig4–5 | supports | Primary Results establish membrane-unenclosed cytoplasmic proteasome foci, colocalized 20S/19S reporters, rapid refeeding-induced Pre6-GFP nuclear return with water and cycloheximide controls, and analogous endogenous Pad1-GFP behavior in S.pombe. The paper expressly leaves intact-granule particle association and activity unresolved; native gels are extracts. BY4741/2/3-derived budding-yeast strains are specified. |
| psg-agent-jats-PMC5597321 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5597321.1/PMC5597321.1.xml; RESULTS all six subsections; DISCUSSION; METHODS yeast strains, fluorescence microscopy and proteomic analysis; Figs4,5,7 captions | supports | All six primary Results subsections and Discussion distinguish genetic effects from residence. Blm10 and Ubp6 colocalize; processed diglycine-deleted GFP-ubiquitin reporter and enriched free ubiquitin support the mature-product row. Formaldehyde-crosslinked PSG enrichment recovers core/regulatory subunits and Blm10. Weak polyubiquitin detection is assay-specific. Figure7 native PAGE measures lysates, not universal in situ dissociation. Kinase/karyopherin foci or knockout effects alone are not component evidence. |
| psg-agent-tang2026-mpg | https://pure.mpg.de/rest/items/item_3702910_1/component/file_3702923/content; Printed pp1153–1158: Summary, Introduction, Results in situ design, starvation onset and paracrystalline arrays; p1158 inactive-state and metabolic-control Results; pp1164–1165 Discussion/Limitations; STAR Methods yeast cell culture and fluorescent tagging; PDF extraction tang2026.txt lines1–340,435–495,830–920,1509–1531 | supports | Recovered primary PDF independently supports intact doubly capped 26S trimers and paracrystalline fiber bundles in the observed yeast states. Results compare untagged/tagged cells, structural s1-like inactivity and glucose-dependent redistribution. Discussion/limitations distinguish unresolved associated factors and proposed protection/dissolution mechanisms from observed architecture; purification disrupts assemblies. Current full-text recovery does not invalidate the target historical abstract-only access note. |
| psg-agent-retraction | https://elifesciences.org/articles/82988; Full retraction notice paragraphs beginning with original citation and ending with author responses | supports | Official notice retracts DOI10.7554/eLife.34532 after duplicated western-blot background bands, duplicated confocal images and poor experimental archiving. It is used only to exclude unreliable positive evidence; the corresponding author’s belief about the premise is not treated as independent experimental validation. |
| psg-agent-commentary30204036 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30204036%20AND%20SRC:MED&amp;format=json&amp;resultType=core; resultList.result[0] id/title/doi/pubTypeList/commentCorrectionList/abstractText | supports | Native metadata identifies PMID30204036 as an article-commentary and explicitly links it as Comment on PMID29624167, DOI10.7554/eLife.34532. Its abstract repeats the protection premise; it is not independent evidence after the underlying paper was retracted. |
| psg-agent-doi-10.1083_jcb.200711154 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1083%2Fjcb.200711154&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear | supports | Exact DOI query resolves PMID:18504300, Reversible cytoplasmic localization of the proteasome in quiescent yeast cells., DOI 10.1083/jcb.200711154. This binds bibliographic identity; body-level support is documented separately. |
| psg-agent-doi-10.1091_mbc.E17-03-0162 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.E17-03-0162&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear | supports | Exact DOI query resolves PMID:28768827, Ubiquitin orchestrates proteasome dynamics between proliferation and quiescence in yeast., DOI 10.1091/mbc.e17-03-0162. This binds bibliographic identity; body-level support is documented separately. |
| psg-agent-doi-10.1016_j.cell.2025.12.035 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.cell.2025.12.035&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear | supports | Exact DOI query resolves PMID:41605212, Metabolically regulated proteasome supramolecular organization in situ., DOI 10.1016/j.cell.2025.12.035. This binds bibliographic identity; body-level support is documented separately. |
| psg-agent-doi-10.7554_eLife.82988 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554%2FeLife.82988&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear | supports | Exact DOI query resolves PMID:36053058, Retraction: Proteasome storage granules protect proteasomes from autophagic degradation upon carbon starvation., DOI 10.7554/elife.82988. This binds bibliographic identity; body-level support is documented separately. |
| psg-agent-P43583 | https://rest.uniprot.org/uniprotkb/P43583.json; primaryAccession; entryType; genes; proteinDescription; organism | supports | Native reviewed entry identifies P43583, Proteasome activator BLM10, gene BLM10, taxon 559292. It verifies reference-sequence identity, while granule residence is assessed from the primary experiments. |
| psg-agent-P43593 | https://rest.uniprot.org/uniprotkb/P43593.json; primaryAccession; entryType; genes; proteinDescription; organism | supports | Native reviewed entry identifies P43593, Ubiquitin carboxyl-terminal hydrolase 6, gene UBP6, taxon 559292. It verifies reference-sequence identity, while granule residence is assessed from the primary experiments. |
| psg-agent-P0CG63 | https://rest.uniprot.org/uniprotkb/P0CG63.json; primaryAccession; entryType; genes; proteinDescription; organism | supports | Native reviewed entry identifies P0CG63, Polyubiquitin, gene UBI4, taxon 559292. It verifies reference-sequence identity, while granule residence is assessed from the primary experiments. |
| psg-agent-IPR035309 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035309/; metadata accession, name and type; description only where explicitly non-LLM | supports | Native entry IPR035309 is type family, named Proteasome activator complex subunit 4. This establishes sequence-class scope, not localization or assembly necessity. |
| psg-agent-IPR044635 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044635/; metadata accession, name and type; description only where explicitly non-LLM | supports | Native entry IPR044635 is type family, named Ubiquitin carboxyl-terminal hydrolase 14-like. This establishes sequence-class scope, not localization or assembly necessity. |
| psg-agent-IPR050158 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050158/; metadata accession, name and type; description only where explicitly non-LLM | supports | Native entry IPR050158 is type family, named Ubiquitin and ubiquitin-like. This establishes sequence-class scope, not localization or assembly necessity. |
| psg-agent-ipr-matches-P43583 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P43583/?page_size=200; count; next; results[].metadata accession/name/type | supports | Complete integrated InterPro response for P43583: 6 matches, next=null; family entries: IPR035309 Proteasome activator complex subunit 4. Other matches are domains, sites or superfamilies, not exact whole-protein class identifiers. |
| psg-agent-ipr-matches-P43593 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P43593/?page_size=200; count; next; results[].metadata accession/name/type | supports | Complete integrated InterPro response for P43593: 7 matches, next=null; family entries: IPR044635 Ubiquitin carboxyl-terminal hydrolase 14-like. Other matches are domains, sites or superfamilies, not exact whole-protein class identifiers. |
| psg-agent-ipr-matches-P0CG63 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0CG63/?page_size=200; count; next; results[].metadata accession/name/type | supports | Complete integrated InterPro response for P0CG63: 5 matches, next=null; family entries: IPR050158 Ubiquitin and ubiquitin-like. Other matches are domains, sites or superfamilies, not exact whole-protein class identifiers. |
| psg-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId; scientificName; rank; lineage | supports | Native taxonomy resolves 4932 to Saccharomyces cerevisiae, rank species. Species and reference-strain identities remain distinct from the experimental genotypes. |
| psg-agent-tax-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; taxId; scientificName; rank; lineage | supports | Native taxonomy resolves 4896 to Schizosaccharomyces pombe, rank species. Species and reference-strain identities remain distinct from the experimental genotypes. |
| psg-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId; scientificName; rank; lineage | supports | Native taxonomy resolves 559292 to Saccharomyces cerevisiae S288C, rank strain. Species and reference-strain identities remain distinct from the experimental genotypes. |
| psg-agent-laporte-fig2-native | https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/jcb1810737f02.jpg; Whole native jcb1810737f02.jpg; panelsA/B labels, merge channels, time axis and2micrometre bars | supports | Visually inspected complete native Figure2: panelA compares indicated 19S lid/base and20S alpha/beta reporter pairs, while panelB tracks core-subunit colocalization through culture age. This is localization, not proof of assembled active26S. Native image MD5 matches the PMC package. |
| psg-agent-package-PMC2396804 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/PMC2396804.1.json; pmcid/title/is_retracted/license_code; media_urls jcb1810737f02.jpg | supports | Native package identifies the2008 article as not retracted and CC BY-NC-SA; media_urls supplies Figure2 filename and MD5. This package alone does not specify the license version; that is checked separately in JATS permissions. |
| psg-figure-license | https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/PMC2396804.1.xml; front/article-meta/permissions; fig[@id=fig2]/caption | supports | JATS article permissions explicitly specify Creative Commons Attribution-Noncommercial-ShareAlike3.0 after the first six months; Figure2 caption identifies the reporter comparisons and2micrometre scale. |
| native-verify | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml --verify; Entire target-specific native log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml --causal-graphs; Entire target-specific native log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/inclusion/proteasome_storage_granule.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/inclusion/proteasome_storage_granule.yaml |
| strict-result | just validate-strict data/structures/inclusion/proteasome_storage_granule.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/proteasome_storage_granule-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/inclusion/proteasome_storage_granule.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/proteasome_storage_granule-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/proteasome_storage_granule-strict.tsv |
| target-curies | just check-curies-strict; data/structures/inclusion/proteasome_storage_granule.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 17 of18 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:30204036: UNREACHABLE; resolved by evidence psg-agent-commentary30204036. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Tang2026 full PDF was recovered in this review although the target documents an earlier abstract-only read. Specified structural Results, glucose-control Results, Discussion/limitations and cell-culture/tagging Methods were read; full raw tomograms, deposited maps/models and the complete supplement were not reanalyzed. The present review does not create new architecture or dataset claims in the maintained record.
- Laporte2008 all claim-bearing Results, strain/GFP/microscopy Methods and Figures1–5 captions were read; linkedFigure2 pixels were inspected. Gu2017 all Results/Discussion and specified Methods/captions were read, but raw proteomics, complete supplementary experiments and blot pixels were not independently reanalyzed.
- Native family searches are restricted to the complete matching-entry responses and stated candidate metadata. No exhaustive absence across all identifier systems is asserted; IPR050158 LLM-generated prose is not used as experimental evidence.
- No universal assembly necessity, fixed stoichiometry, physical state or broad taxonomic prevalence was inferred. Historical source-access/search notes are treated as historical statements, not falsely contradicted by newer access.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104739Z-proteasome-storage-granule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Proteasome storage granule identity, source integrity and recovery review
started_at: '2026-10-21T10:26:49Z'
finished_at: '2026-10-21T10:47:39Z'
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
summary: The PSG identity, supported constituent subset, recovery graph and source
  exclusions are coherent. No concrete curation finding was established; assembly
  necessity and universal architecture remain bounded.
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
  - path: data/structures/inclusion/proteasome_storage_granule.yaml
    sha256: e09339d5bc79d9ee31b2e5e342b82a67992e86fc4d2fd16559791fefa46121af
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
- target_id: GO:0034515
  path: data/structures/inclusion/proteasome_storage_granule.yaml
  label: proteasome storage granule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/proteasome_storage_granule.yaml
    role: maintained scientific record
scope:
  description: Whole single-record scientific review, all components/examples, all
    graph edges, source-limit discussions, native identifiers and the linked source
    figure.
  selection: Batch20 index1, one frozen target in strict path order; no neighboring
    scientific record dependency.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0034515
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0034515
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml
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
  - GO:0034515
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml
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
  - GO:0034515
  command: just validate data/structures/inclusion/proteasome_storage_granule.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0034515
  command: just validate-strict data/structures/inclusion/proteasome_storage_granule.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/proteasome_storage_granule-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0034515
  summary: 17 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - psg-agent-commentary30204036
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0034515
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - psg-agent-go
  - psg-agent-jats-PMC2396804
  - psg-agent-jats-PMC5597321
  - psg-agent-tang2026-mpg
  - psg-agent-retraction
  - psg-agent-commentary30204036
  - psg-agent-doi-10.1083_jcb.200711154
  - psg-agent-doi-10.1091_mbc.E17-03-0162
  - psg-agent-doi-10.1016_j.cell.2025.12.035
  - psg-agent-doi-10.7554_eLife.82988
  - psg-agent-P43583
  - psg-agent-P43593
  - psg-agent-P0CG63
  - psg-agent-IPR035309
  - psg-agent-IPR044635
  - psg-agent-IPR050158
  - psg-agent-ipr-matches-P43583
  - psg-agent-ipr-matches-P43593
  - psg-agent-ipr-matches-P0CG63
  - psg-agent-tax-4932
  - psg-agent-tax-4896
  - psg-agent-tax-559292
  - psg-agent-laporte-fig2-native
  - psg-agent-package-PMC2396804
  - psg-figure-license
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0034515
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
  - GO:0034515
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
  - GO:0034515
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
  - GO:0034515
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
  - GO:0034515
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
- evidence_id: psg-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034515,GO:0043232,GO:0005737,GO:0005839,GO:0005838
  locator: 'results for all five identifiers: names/definitions/synonyms; GO:0043232
    and GO:0005737 children entries for GO:0034515'
  accessed_at: '2026-10-21T10:28:46Z'
  support: supports
  summary: GO:0034515 is the active PSG cellular-component identity with related synonym
    PSG. The native parent response includes it as is_a GO:0043232, and cytoplasm
    includes it as part_of. GO:0005839 and GO:0005838 identify core and regulatory
    complexes. These are class identities, not proof that every fluorescent focus
    has one universal particle configuration.
  snapshot_sha256: 31b0e04cf34ad8d0d4de1cc7fada3f1833993008ca4475c1ecbe8261885cd92f
- evidence_id: psg-agent-jats-PMC2396804
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/PMC2396804.1.xml
  locator: All five Results and discussion subsections; Materials and methods strain/growth,
    GFP fusion and Microscopy sections; Figs1–5 captions, especially Fig2 and Fig4–5
  accessed_at: '2026-10-21T10:28:44Z'
  support: supports
  summary: Primary Results establish membrane-unenclosed cytoplasmic proteasome foci,
    colocalized 20S/19S reporters, rapid refeeding-induced Pre6-GFP nuclear return
    with water and cycloheximide controls, and analogous endogenous Pad1-GFP behavior
    in S.pombe. The paper expressly leaves intact-granule particle association and
    activity unresolved; native gels are extracts. BY4741/2/3-derived budding-yeast
    strains are specified.
  snapshot_sha256: fdb31b38a84b5b23ca9c704375068b54582e998b5bd92aedc88ebeaaea18b1d9
- evidence_id: psg-agent-jats-PMC5597321
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5597321.1/PMC5597321.1.xml
  locator: RESULTS all six subsections; DISCUSSION; METHODS yeast strains, fluorescence
    microscopy and proteomic analysis; Figs4,5,7 captions
  accessed_at: '2026-10-21T10:28:45Z'
  support: supports
  summary: All six primary Results subsections and Discussion distinguish genetic
    effects from residence. Blm10 and Ubp6 colocalize; processed diglycine-deleted
    GFP-ubiquitin reporter and enriched free ubiquitin support the mature-product
    row. Formaldehyde-crosslinked PSG enrichment recovers core/regulatory subunits
    and Blm10. Weak polyubiquitin detection is assay-specific. Figure7 native PAGE
    measures lysates, not universal in situ dissociation. Kinase/karyopherin foci
    or knockout effects alone are not component evidence.
  snapshot_sha256: 065f844203d82efea45e3eb6a2135cc231dd0484ae6f7646801cd58ac9ccc0d4
- evidence_id: psg-agent-tang2026-mpg
  kind: primary_source
  reference: https://pure.mpg.de/rest/items/item_3702910_1/component/file_3702923/content
  locator: 'Printed pp1153–1158: Summary, Introduction, Results in situ design, starvation
    onset and paracrystalline arrays; p1158 inactive-state and metabolic-control Results;
    pp1164–1165 Discussion/Limitations; STAR Methods yeast cell culture and fluorescent
    tagging; PDF extraction tang2026.txt lines1–340,435–495,830–920,1509–1531'
  accessed_at: '2026-10-21T10:30:40Z'
  support: supports
  summary: Recovered primary PDF independently supports intact doubly capped 26S trimers
    and paracrystalline fiber bundles in the observed yeast states. Results compare
    untagged/tagged cells, structural s1-like inactivity and glucose-dependent redistribution.
    Discussion/limitations distinguish unresolved associated factors and proposed
    protection/dissolution mechanisms from observed architecture; purification disrupts
    assemblies. Current full-text recovery does not invalidate the target historical
    abstract-only access note.
  snapshot_sha256: b0b18cfb67343d26ad1630f02775cb843141169a5b70542d45ca86909718f7d2
- evidence_id: psg-agent-retraction
  kind: authority
  reference: https://elifesciences.org/articles/82988
  locator: Full retraction notice paragraphs beginning with original citation and
    ending with author responses
  accessed_at: '2026-10-21T10:28:45Z'
  support: supports
  summary: Official notice retracts DOI10.7554/eLife.34532 after duplicated western-blot
    background bands, duplicated confocal images and poor experimental archiving.
    It is used only to exclude unreliable positive evidence; the corresponding author’s
    belief about the premise is not treated as independent experimental validation.
  snapshot_sha256: ff506ad64f737b83722f503caf45f81c1c683ae85182e577385c0267192411b5
- evidence_id: psg-agent-commentary30204036
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30204036%20AND%20SRC:MED&format=json&resultType=core
  locator: resultList.result[0] id/title/doi/pubTypeList/commentCorrectionList/abstractText
  accessed_at: '2026-10-21T10:28:44Z'
  support: supports
  summary: Native metadata identifies PMID30204036 as an article-commentary and explicitly
    links it as Comment on PMID29624167, DOI10.7554/eLife.34532. Its abstract repeats
    the protection premise; it is not independent evidence after the underlying paper
    was retracted.
  snapshot_sha256: e90c0daf4dd569383cff9336c1fd66f0198ed7417eeb28cc372d87974dbe55e8
- evidence_id: psg-agent-doi-10.1083_jcb.200711154
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1083%2Fjcb.200711154&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear
  accessed_at: '2026-10-21T10:28:44Z'
  support: supports
  summary: Exact DOI query resolves PMID:18504300, Reversible cytoplasmic localization
    of the proteasome in quiescent yeast cells., DOI 10.1083/jcb.200711154. This binds
    bibliographic identity; body-level support is documented separately.
  snapshot_sha256: b8adb1924e52e558cd5ff3e736454a54fdc53f8f26ef138fc27d24eccd1afc9d
- evidence_id: psg-agent-doi-10.1091_mbc.E17-03-0162
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.E17-03-0162&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear
  accessed_at: '2026-10-21T10:28:44Z'
  support: supports
  summary: Exact DOI query resolves PMID:28768827, Ubiquitin orchestrates proteasome
    dynamics between proliferation and quiescence in yeast., DOI 10.1091/mbc.e17-03-0162.
    This binds bibliographic identity; body-level support is documented separately.
  snapshot_sha256: 340ebcb902438da569ee93d9325125a9e6f639628e3d46cbf60a2e4eb8812dee
- evidence_id: psg-agent-doi-10.1016_j.cell.2025.12.035
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.cell.2025.12.035&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear
  accessed_at: '2026-10-21T10:28:44Z'
  support: supports
  summary: Exact DOI query resolves PMID:41605212, Metabolically regulated proteasome
    supramolecular organization in situ., DOI 10.1016/j.cell.2025.12.035. This binds
    bibliographic identity; body-level support is documented separately.
  snapshot_sha256: 4d9336c00616c0e92fed2f4faab0a0847f2c74fdd4f3ccafc42c41ba17d0f2cf
- evidence_id: psg-agent-doi-10.7554_eLife.82988
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554%2FeLife.82988&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/authorString/pubYear
  accessed_at: '2026-10-21T10:28:44Z'
  support: supports
  summary: 'Exact DOI query resolves PMID:36053058, Retraction: Proteasome storage
    granules protect proteasomes from autophagic degradation upon carbon starvation.,
    DOI 10.7554/elife.82988. This binds bibliographic identity; body-level support
    is documented separately.'
  snapshot_sha256: 4ccac6ddf55b31fd3c28ec48ab222c6a198b004a5fccebfb1c482ef99138ed7b
- evidence_id: psg-agent-P43583
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P43583.json
  locator: primaryAccession; entryType; genes; proteinDescription; organism
  accessed_at: '2026-10-21T10:28:45Z'
  support: supports
  summary: Native reviewed entry identifies P43583, Proteasome activator BLM10, gene
    BLM10, taxon 559292. It verifies reference-sequence identity, while granule residence
    is assessed from the primary experiments.
  snapshot_sha256: fff0ae0abd33c736a3fa6cdfac72d5ba8ea9aacc4f315bdd02b168f220b13a97
- evidence_id: psg-agent-P43593
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P43593.json
  locator: primaryAccession; entryType; genes; proteinDescription; organism
  accessed_at: '2026-10-21T10:28:45Z'
  support: supports
  summary: Native reviewed entry identifies P43593, Ubiquitin carboxyl-terminal hydrolase
    6, gene UBP6, taxon 559292. It verifies reference-sequence identity, while granule
    residence is assessed from the primary experiments.
  snapshot_sha256: 9b33a9a6fa866ed3baf1243cc28f84adfb6659b658057773871fda6202ff14ac
- evidence_id: psg-agent-P0CG63
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0CG63.json
  locator: primaryAccession; entryType; genes; proteinDescription; organism
  accessed_at: '2026-10-21T10:28:45Z'
  support: supports
  summary: Native reviewed entry identifies P0CG63, Polyubiquitin, gene UBI4, taxon
    559292. It verifies reference-sequence identity, while granule residence is assessed
    from the primary experiments.
  snapshot_sha256: b0987c6267a3608e544fac75e771b2f931b95c2cac977b2dd206806fcce863bb
- evidence_id: psg-agent-IPR035309
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035309/
  locator: metadata accession, name and type; description only where explicitly non-LLM
  accessed_at: '2026-10-21T10:28:46Z'
  support: supports
  summary: Native entry IPR035309 is type family, named Proteasome activator complex
    subunit 4. This establishes sequence-class scope, not localization or assembly
    necessity.
  snapshot_sha256: fdbc1221b8adce63ab7091a28e6befcd142df6653ddc0033da5d1b453d400fef
- evidence_id: psg-agent-IPR044635
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044635/
  locator: metadata accession, name and type; description only where explicitly non-LLM
  accessed_at: '2026-10-21T10:28:46Z'
  support: supports
  summary: Native entry IPR044635 is type family, named Ubiquitin carboxyl-terminal
    hydrolase 14-like. This establishes sequence-class scope, not localization or
    assembly necessity.
  snapshot_sha256: 1caae0331f5173bdc4bc19b430fead937b0cc4116be2eca5e2108870ee351bef
- evidence_id: psg-agent-IPR050158
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050158/
  locator: metadata accession, name and type; description only where explicitly non-LLM
  accessed_at: '2026-10-21T10:28:46Z'
  support: supports
  summary: Native entry IPR050158 is type family, named Ubiquitin and ubiquitin-like.
    This establishes sequence-class scope, not localization or assembly necessity.
  snapshot_sha256: 665d6b43cc1bedd8b45b2ba5fada2f4994418d081996b5f644c4b1c871733491
- evidence_id: psg-agent-ipr-matches-P43583
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P43583/?page_size=200
  locator: count; next; results[].metadata accession/name/type
  accessed_at: '2026-10-21T10:28:45Z'
  support: supports
  summary: 'Complete integrated InterPro response for P43583: 6 matches, next=null;
    family entries: IPR035309 Proteasome activator complex subunit 4. Other matches
    are domains, sites or superfamilies, not exact whole-protein class identifiers.'
  snapshot_sha256: af48ff95cae271a6befc0c0d70f0c641789af1951ffadb7b6e163059e1212c88
  search_scope: Remote public InterPro integrated entries matching exactly UniProt
    P43583; all 6 returned entries read and next=null. Filesystem ignore rules are
    not applicable to this bounded remote query; no assertion of local-file absence
    or exhaustive absence across every ontology.
- evidence_id: psg-agent-ipr-matches-P43593
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P43593/?page_size=200
  locator: count; next; results[].metadata accession/name/type
  accessed_at: '2026-10-21T10:28:45Z'
  support: supports
  summary: 'Complete integrated InterPro response for P43593: 7 matches, next=null;
    family entries: IPR044635 Ubiquitin carboxyl-terminal hydrolase 14-like. Other
    matches are domains, sites or superfamilies, not exact whole-protein class identifiers.'
  snapshot_sha256: 5f73c565ef0fb334e0bddaf3e66c2710c19c6745f24de5d5fc2e63706a55d9b5
  search_scope: Remote public InterPro integrated entries matching exactly UniProt
    P43593; all 7 returned entries read and next=null. Filesystem ignore rules are
    not applicable to this bounded remote query; no assertion of local-file absence
    or exhaustive absence across every ontology.
- evidence_id: psg-agent-ipr-matches-P0CG63
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0CG63/?page_size=200
  locator: count; next; results[].metadata accession/name/type
  accessed_at: '2026-10-21T10:28:45Z'
  support: supports
  summary: 'Complete integrated InterPro response for P0CG63: 5 matches, next=null;
    family entries: IPR050158 Ubiquitin and ubiquitin-like. Other matches are domains,
    sites or superfamilies, not exact whole-protein class identifiers.'
  snapshot_sha256: 279adb4f854a9497dc9f3d8d8a22be5c24c9f96460e1e6cbc8175f97c4dcb615
  search_scope: Remote public InterPro integrated entries matching exactly UniProt
    P0CG63; all 5 returned entries read and next=null. Filesystem ignore rules are
    not applicable to this bounded remote query; no assertion of local-file absence
    or exhaustive absence across every ontology.
- evidence_id: psg-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId; scientificName; rank; lineage
  accessed_at: '2026-10-21T10:15:30.282122Z'
  support: supports
  summary: Native taxonomy resolves 4932 to Saccharomyces cerevisiae, rank species.
    Species and reference-strain identities remain distinct from the experimental
    genotypes.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: psg-agent-tax-4896
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: taxId; scientificName; rank; lineage
  accessed_at: '2026-10-21T10:28:46Z'
  support: supports
  summary: Native taxonomy resolves 4896 to Schizosaccharomyces pombe, rank species.
    Species and reference-strain identities remain distinct from the experimental
    genotypes.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: psg-agent-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId; scientificName; rank; lineage
  accessed_at: '2026-10-21T10:15:30.380033Z'
  support: supports
  summary: Native taxonomy resolves 559292 to Saccharomyces cerevisiae S288C, rank
    strain. Species and reference-strain identities remain distinct from the experimental
    genotypes.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: psg-agent-laporte-fig2-native
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/jcb1810737f02.jpg
  locator: Whole native jcb1810737f02.jpg; panelsA/B labels, merge channels, time
    axis and2micrometre bars
  accessed_at: '2026-10-21T10:32:06Z'
  support: supports
  summary: 'Visually inspected complete native Figure2: panelA compares indicated
    19S lid/base and20S alpha/beta reporter pairs, while panelB tracks core-subunit
    colocalization through culture age. This is localization, not proof of assembled
    active26S. Native image MD5 matches the PMC package.'
  snapshot_sha256: ceedede7c232a35e128bbd7a2771f6bbacfa073410611bc8bc50e0759a60977a
- evidence_id: psg-agent-package-PMC2396804
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/PMC2396804.1.json
  locator: pmcid/title/is_retracted/license_code; media_urls jcb1810737f02.jpg
  accessed_at: '2026-10-21T10:28:44Z'
  support: supports
  summary: Native package identifies the2008 article as not retracted and CC BY-NC-SA;
    media_urls supplies Figure2 filename and MD5. This package alone does not specify
    the license version; that is checked separately in JATS permissions.
  snapshot_sha256: fa1dd566efaf7dd07ac9f73731bc445e96675fd58b3cc00384c4206a22677acc
- evidence_id: psg-figure-license
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/PMC2396804.1.xml
  locator: front/article-meta/permissions; fig[@id=fig2]/caption
  accessed_at: '2026-10-21T10:28:44Z'
  support: supports
  summary: JATS article permissions explicitly specify Creative Commons Attribution-Noncommercial-ShareAlike3.0
    after the first six months; Figure2 caption identifies the reporter comparisons
    and2micrometre scale.
  snapshot_sha256: fdb31b38a84b5b23ca9c704375068b54582e998b5bd92aedc88ebeaaea18b1d9
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml
    --verify
  locator: Entire target-specific native log
  accessed_at: '2026-10-21T10:32:04.294266Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml
    --causal-graphs
  locator: Entire target-specific native log
  accessed_at: '2026-10-21T10:32:04.794355Z'
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
  reference: just validate data/structures/inclusion/proteasome_storage_granule.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:26:51Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/inclusion/proteasome_storage_granule.yaml'
  snapshot_sha256: cada8daf496eaeb7b5075bbb8287803e1d96de853dd1b56bc330690e70224c68
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/inclusion/proteasome_storage_granule.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/proteasome_storage_granule-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:26:52Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/inclusion/proteasome_storage_granule.yaml\
    \ --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/proteasome_storage_granule-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/proteasome_storage_granule-strict.tsv"
  snapshot_sha256: ee50a973dad86a6e742f3c9fab574469e438897a338b87db31d252b128ac486b
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/inclusion/proteasome_storage_granule.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:35:37Z'
  support: supports
  summary: '17 of18 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:30204036: UNREACHABLE; resolved by evidence psg-agent-commentary30204036.
    Source-native identity checked separately.'
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
  topic: Identity, synonym and hierarchy
  outcome: supported
  target_ids:
  - GO:0034515
  summary: The PSG ontology identity, related abbreviation, membraneless parent and
    cytoplasmic parthood agree with native GO and the2008 experiments. Core/regulatory
    has_part assertions are supported by directly observed constituents. Nuclear proteasome
    assemblies in2026 are not silently substituted for the bounded cytoplasmic GO
    class.
  evidence_ids:
  - psg-agent-go
  - psg-agent-jats-PMC2396804
  - psg-agent-tang2026-mpg
- assessment_id: composition
  area: completeness
  topic: Supported constituent subset
  outcome: supported
  target_ids:
  - GO:0034515
  summary: Core and regulatory particles, Blm10, Ubp6 and free ubiquitin have direct
    localization or enrichment support. Single protein accessions are reference examples,
    not whole-complex identifiers. P0CG63 is the UBI4 polyubiquitin precursor, distinguished
    from processed unconjugated ubiquitin and the engineered reporter. Upstream screen
    hits are correctly excluded without residence evidence.
  evidence_ids:
  - psg-agent-jats-PMC2396804
  - psg-agent-jats-PMC5597321
  - psg-agent-P43583
  - psg-agent-P43593
  - psg-agent-P0CG63
- assessment_id: necessity
  area: evidence
  topic: Assembly necessity remains unresolved
  outcome: unknown
  target_ids:
  - GO:0034515
  summary: All five component essentialities are UNKNOWN. The studies contain condition-dependent
    depletion/active-site phenotypes but do not establish universal necessity of each
    component class across PSG states. Genetic effects, constitutive proteasome function
    and direct localization are not interchangeable with granule assembly necessity.
  evidence_ids:
  - psg-agent-jats-PMC2396804
  - psg-agent-jats-PMC5597321
  - psg-agent-tang2026-mpg
- assessment_id: grounding
  area: grounding
  topic: Family and mature-product boundaries
  outcome: supported
  target_ids:
  - GO:0034515
  summary: 'InterPro identifies the Blm10 and Ubp6 families, with matching reviewed
    proteins and correct genes/taxon. Complete P0CG63 matches do not supply an exact
    source-neutral unconjugated mature-ubiquitin identity: domains/sites and the broader
    ubiquitin-and-ubiquitin-like family are not exact replacements. The bounded label-only
    TODO is justified by these checked candidates.'
  evidence_ids:
  - psg-agent-P43583
  - psg-agent-P43593
  - psg-agent-P0CG63
  - psg-agent-IPR035309
  - psg-agent-IPR044635
  - psg-agent-IPR050158
  - psg-agent-ipr-matches-P43583
  - psg-agent-ipr-matches-P43593
  - psg-agent-ipr-matches-P0CG63
- assessment_id: taxa
  area: scope
  topic: Experimental versus reference strains
  outcome: supported
  target_ids:
  - GO:0034515
  summary: Budding yeast BY4741/2/3-derived assays and fission yeast endogenous Pad1-GFP
    provide source-backed examples. S288C559292 remains a reference-sequence identity,
    not a reassignment of every experiment; no broad lineage prevalence is asserted.
  evidence_ids:
  - psg-agent-jats-PMC2396804
  - psg-agent-jats-PMC5597321
  - psg-agent-tax-4932
  - psg-agent-tax-4896
  - psg-agent-tax-559292
  - psg-agent-P43583
  - psg-agent-P43593
  - psg-agent-P0CG63
- assessment_id: graph
  area: graph
  topic: Intervention-supported mobilization
  outcome: supported
  target_ids:
  - GO:0034515
  summary: Both fresh-YPD edges are supported within the four-day Pre6-GFP assay.
    Water transfer and cycloheximide controls support mobilization of existing material;
    the graph makes no resolved molecular dissolution, proteolysis or protection-from-autophagy
    claim.
  evidence_ids:
  - psg-agent-jats-PMC2396804
- assessment_id: architecture
  area: evidence
  topic: Intact assemblies versus extract models
  outcome: supported
  target_ids:
  - GO:0034515
  summary: The record correctly separates2008 colocalization/activity uncertainty,2017
    lysate dissociation and2026 in situ architecture. Newly recovered full text reinforces
    intact26S arrays in measured states and unresolved associated factors/dissolution
    details. An open expansion TODO is not a false historical access claim or a mandatory
    inventory omission.
  evidence_ids:
  - psg-agent-jats-PMC2396804
  - psg-agent-jats-PMC5597321
  - psg-agent-tang2026-mpg
- assessment_id: provenance
  area: provenance
  topic: Retraction exclusion and bibliographic integrity
  outcome: supported
  target_ids:
  - GO:0034515
  summary: The independently supported2008/2017 claims survive exclusion of the2018
    retracted study and derivative commentary. All exact cited DOI/PMID identities
    resolve natively. No Arabidopsis or proteaphagy-protection claim is imported from
    the withdrawn evidence.
  evidence_ids:
  - psg-agent-retraction
  - psg-agent-commentary30204036
  - psg-agent-doi-10.1083_jcb.200711154
  - psg-agent-doi-10.1091_mbc.E17-03-0162
  - psg-agent-doi-10.1016_j.cell.2025.12.035
  - psg-agent-doi-10.7554_eLife.82988
- assessment_id: image
  area: provenance
  topic: Figure identity and licensing
  outcome: supported
  target_ids:
  - GO:0034515
  summary: The link-only2008Figure2 has the stated reporter colocalization/time-course
    content and2micrometre scale; the source permission is CC BY-NC-SA3.0 rather than
    CC BY. No maintained image file is claimed for this row.
  evidence_ids:
  - psg-agent-laporte-fig2-native
  - psg-agent-package-PMC2396804
  - psg-figure-license
  - psg-agent-jats-PMC2396804
findings: []
actions: []
limitations:
- Tang2026 full PDF was recovered in this review although the target documents an
  earlier abstract-only read. Specified structural Results, glucose-control Results,
  Discussion/limitations and cell-culture/tagging Methods were read; full raw tomograms,
  deposited maps/models and the complete supplement were not reanalyzed. The present
  review does not create new architecture or dataset claims in the maintained record.
- Laporte2008 all claim-bearing Results, strain/GFP/microscopy Methods and Figures1–5
  captions were read; linkedFigure2 pixels were inspected. Gu2017 all Results/Discussion
  and specified Methods/captions were read, but raw proteomics, complete supplementary
  experiments and blot pixels were not independently reanalyzed.
- Native family searches are restricted to the complete matching-entry responses and
  stated candidate metadata. No exhaustive absence across all identifier systems is
  asserted; IPR050158 LLM-generated prose is not used as experimental evidence.
- No universal assembly necessity, fixed stoichiometry, physical state or broad taxonomic
  prevalence was inferred. Historical source-access/search notes are treated as historical
  statements, not falsely contradicted by newer access.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
