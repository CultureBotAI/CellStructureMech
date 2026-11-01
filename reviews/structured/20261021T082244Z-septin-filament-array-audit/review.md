# Septin filament array identity, composition and evidence review

- Review: 20261021T082244Z-septin-filament-array-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:08:45Z
- Finished UTC: 2026-10-21T08:22:44Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact array identity and stage-dependent membrane contexts are supported. One minor generic-family gap and one major mismatch between two mitotic examples and the stated Saccharomyces sporulation context remain.

## Scope And Provenance

Entire single array target; all asserted native identities and sequence-example annotations; GO source-chain review, primary array localization and direct Cdc12/Shs1 sporulation-membership experiments.

Selection: Second selected unreviewed path in batch eleven; path-ordered selection excluding 199 confirmed paths and 20 provisional pending paths from batches9–10.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032160 | data/structures/cytoskeleton/septin_filament_array.yaml | maintained | septin filament array |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032160 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032160 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0032160 | 16 identifiers OK; 3 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0032160 | No expression-module or transcriptional-regulator mechanism is asserted; expression membership is not used as structural localization evidence. |
| Claim-level scientific review | passed | True | GO:0032160 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0032160 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032160 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032160 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032160 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0032160 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Generic array and localized children

identity: supported. Targets: GO:0032160.

GO0032160 exactly matches the bar/filament-array definition, septin-cytoskeleton parent and cytoskeleton parthood. Prospore and chlamydospore terms remain narrower array classes; ring, collar and cap are distinguished rather than merged.

### Developmental species contexts

scope: supported. Targets: GO:0032160.

The GO-backed S. cerevisiae sporulation and C. albicans chlamydospore examples are accurately attributed, and VARIABLE preserves growth-stage dependence. Species identities and the S288C sequence-example strain are correct. Native GO does not constitute a primary experiment or a universal quantitative prevalence estimate.

### Composition and membrane-localization topology

graph: supported. Targets: GO:0032160.

The three NONMECHANISTIC edges are supported at the generic-family and stated membrane-context levels. Bars are not assigned molecular thickness or treated as directly resolved single filaments; optical-sheet interpretation is retained. Neither Don1 rings nor a complete recruitment/force-generation mechanism is imported.

### Accurate accession identity and imported compartment notes

grounding: supported. Targets: GO:0032160.

All five reviewed identities, labels, primary symbols, S288C taxon and exact-query uniqueness checks pass. Native UniProt supports the imported general membrane/bud-neck citations exactly. Those notes deliberately do not establish sporulation-array membership, and identity correctness is retained independently of the membership finding.

### Generic Septin family versus localized cohort

grounding: concern. Targets: GO:0032160.

The component is named septin proteins but its rationale withholds grounding until a family denotes the complete assembly-forming cohort. IPR016491 supplies the generic family identity; localized composition remains a separate scientific question.

### Mitotic examples versus the stated sporulation array

evidence: concern. Targets: GO:0032160.

The current Saccharomyces example is specifically a prospore-membrane array, yet its component declares the full mitotic five-gene set. Primary imaging contradicts unqualified Cdc12/Shs1 assignment in that context. This does not establish their absence from every conceivable filament array or invalidate the three other accurate identities; Cdc11 detection in the PSM literature is retained.

### Ontology source chain and independent primary falsification

provenance: supported. Targets: GO:0032160.

The current record correctly cites GO for its two example contexts; the review reads the underlying Douglas synthesis and separate primary tests. Native PubMed metadata and UniProt citations remain correct. The historical removal of unread Douglas evidence is not retroactively represented as a prior full-text read.

## Findings

### F1: Localized-cohort criterion leaves the generic Septin family ungrounded

minor / open / confirmed; issue key: septin-filament-array-generic-family-withheld.

The generic septin-proteins component is REVIEWED_LABEL_ONLY because its rationale asks for an accession matching the complete localized cohort. Verified IPR016491 identifies the named Septin family without requiring a localization-specific family. Reconcile grounding, status and rationale while preserving separate uncertainty about exact paralogs and associated proteins.

### F2: Cdc12 and Shs1 examples are not supported in the stated Saccharomyces array context

major / open / confirmed; issue key: septin-filament-array-mitotic-examples-in-sporulation-context.

The only S. cerevisiae array context declared by this record is the prospore membrane during sporulation. Its septin component nevertheless includes CDC12/P32468 and SHS1/Q07657 as unqualified structural examples alongside the mitotic set. Their identities are correct, but primary dual-color localization finds little or no Cdc12 and no Shs1 in the Cdc10-marked sporulation structures; later work independently distinguishes the development-specific assembly. Restrict these assignments or provide direct evidence for an explicitly stated alternative array context. This is not an assertion that Cdc12/Shs1 cannot occur in any structure described loosely as an array, nor that the accessions are wrong.

## Recommended Actions And Acceptance Checks

### A1

Under separately authorized curation, ground the generic Septin component to verified IPR016491 and reconcile the cohort-based rationale.

- Retain separate membership evidence; do not infer universal paralog usage or stoichiometry from a family match.
- Retain structure-level rather than individual-protein viability essentiality.
- Use guarded curation/history and run native schema, strict, identifier-label, protein-example and rendered-page checks.

### A2

Under separately authorized curation, reconcile the CDC12 and SHS1 symbols/examples with the stated S. cerevisiae sporulation-array scope: restrict/remove these structural assignments, or document a distinct source-supported context that actually fits this GO array class.

- Preserve correct accession identity and taxon information separately from structural membership.
- Do not infer absence from every array architecture or remove Cdc11 solely from a modern core-rod model; published PSM detection is distinct from integral rod composition.
- If adding Spr3/Spr28 as better-supported sporulation examples, verify their own exact native accession/taxon and localization evidence before editing.
- Do not infer Candida paralog membership from Saccharomyces or impose an exhaustive inventory requirement.
- Use guarded curation/history and run focused schema, strict, UniProt identity, label and generated-page checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/septin_filament_array.yaml; Entire target, all components/protein examples, taxonomy, graph edges, evidence and discussions | context_only | Complete target read after native inspection. Maintained record and mapping status remain PROPOSED; no scientific promotion or content change. |
| policy | docs/CURATION.md; Components: family grounding, composition and structure-formation essentiality | context_only | A generic family identifier is distinct from an exact localized cohort; ESSENTIAL refers to formation of the named structure, not viability or each named paralog. |
| example-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Non-negotiable rules1–5; captured as expanded native inspect input | context_only | Correct accession, gene, taxon and entry status do not independently establish structure membership. Native subcellular-location evidence is retained only for the actual compartment named. |
| septin-array-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032173,GO:0032156,GO:0032174,GO:0062140,GO:0005940,GO:0032160,GO:0005856,GO:0032165,GO:0032166,GO:0032159,GO:0005938,GO:0031105; Returned exact terms and isObsolete flags; definitions, synonyms and children with is_a versus part_of relations | supports | Exact active GO definitions, generic structure classes, named parents/children and structural parthood were checked. The returned broader terms expose the relevant child relations. |
| septin-array-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; metadata accession/name/type=family, description and hierarchy; original native receipt retained | supports | IPR016491 is the Septin family, appropriate to the generic septin-proteins label. It does not delimit one localized cohort, specify stoichiometry or prove membership of an individual example. |
| septin-array-agent-paper-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=25&amp;query=%28DOI%3A%2210.1091/mbc.E04-09-0764%22%29%20OR%20%28DOI%3A%2210.1534/genetics.107.073007%22%29%20OR%20%28DOI%3A%2210.1073/pnas.0803330105%22%29%20OR%20%28DOI%3A%2210.1016/j.devcel.2011.02.004%22%29%20OR%20%28DOI%3A%2210.3389/fcell.2016.00123%22%29%20OR%20%28DOI%3A%2210.1016/j.mib.2014.04.004%22%29%20OR%20%28DOI%3A%2210.1099/mic.0.000359%22%29%20OR%20%28EXT_ID%3A14562095%20AND%20SRC%3AMED%29%20OR%20%28EXT_ID%3A25971666%20AND%20SRC%3AMED%29%20OR%20%28EXT_ID%3A9790978%20AND%20SRC%3AMED%29; Relevant exact DOI/PMID result objects; publication metadata and abstracts | supports | Native metadata verifies exact DOI/PMID identities, authors, titles and source types for record-cited papers. Huh2003/PMID14562095, Finnigan2015/25971666 and Mino1998/9790978 resolve despite residuals in the original resolver TSV. Metadata and abstracts do not substitute for unavailable primary bodies. |
| septin-array-agent-P32457 | https://rest.uniprot.org/uniprotkb/P32457.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC3 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-array-agent-symbol-CDC3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC3%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC3 query in S. cerevisiae returns one entry, P32457. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-array-agent-P25342 | https://rest.uniprot.org/uniprotkb/P25342.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC10 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-array-agent-symbol-CDC10 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC10%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC10 query in S. cerevisiae returns one entry, P25342. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-array-agent-P32458 | https://rest.uniprot.org/uniprotkb/P32458.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC11 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-array-agent-symbol-CDC11 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC11%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC11 query in S. cerevisiae returns one entry, P32458. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-array-agent-P32468 | https://rest.uniprot.org/uniprotkb/P32468.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC12 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-array-agent-symbol-CDC12 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC12%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC12 query in S. cerevisiae returns one entry, P32468. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-array-agent-Q07657 | https://rest.uniprot.org/uniprotkb/Q07657.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary SHS1 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-array-agent-symbol-SHS1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ASHS1%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed SHS1 query in S. cerevisiae returns one entry, Q07657. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-array-agent-taxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank and lineage | supports | Native taxonomy confirms the exact taxon identifier, scientific name and rank; species scope is distinguished from the S288C sequence-example strain. |
| septin-array-agent-taxon-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId, scientificName, rank and lineage | supports | Native taxonomy confirms the exact taxon identifier, scientific name and rank; species scope is distinguished from the S288C sequence-example strain. |
| septin-array-agent-taxon-5476 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5476; taxId, scientificName, rank and lineage | supports | Native taxonomy confirms the exact taxon identifier, scientific name and rank; species scope is distinguished from the S288C sequence-example strain. |
| septin-array-agent-douglas-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/; PMC1214204 sec14 and sec17; original receipt retained; review-tier synthesis | supports | The GO definition source is a literature review. It describes prospore septin sheets appearing as bars in optical sections and Candida chlamydospore peripheral filament arrays after septation. These stage-dependent localizations are not a single universal mitotic paralog set. |
| septin-array-agent-versele-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render; PMC1761124 S2 paragraphP4; original receipt retained; review tier | supports | The review distinguishes mitotic Cdc3/Cdc10/Cdc11/Cdc12/Shs1 collars from a sporulation-specific cohort that replaces Cdc12/Shs1 with Spr3/Spr28. It provides context, not the primary exclusion experiment. |
| septin-array-agent-tachikawa2001 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2150859/?pdf=render; PMC2150859 Results sec7–10 and Figures5–9 legends; original receipt retained | supports | Primary Spr28/Gip1/Glc7 imaging supports a dynamic prospore-membrane array. Optical bars can represent parallel sheets; the Don1 leading-edge ring is distinct. Disrupted septin localization in gip1 mutants does not by itself establish that every membrane process requires every septin. |
| septin-array-agent-mcmurray2008 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2562167/; PMC2562167 Results and Discussion S1: sporulation paragraphs beginning Two septins required / Like Cdc10 / Unlike CDC3; Figure3A,C,E,F,G and caption; DOI10.1016/j.cub.2008.07.020, PMID18701287 | refutes | Primary dual-color imaging finds little or no Cdc12-GFP in Cdc10-mCherry-marked spore-associated structures and no Shs1-GFP colocalization there; Shs1 remains in ascal cytoplasm. Cdc12 persists by immunoblot, so failure to detect it in the array is not attributed simply to degradation. Cdc10 is reused through the developmental transition. This directly challenges the unqualified Cdc12/Shs1 examples in the record's S. cerevisiae sporulation context. |
| septin-array-agent-mcmurray2008-figure3 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/502c/2562167/a3850b2cb250/nihms67754f3.jpg; Original PMC image nihms67754f3.jpg, Figure3 panelsA–G; direct image and adjacent caption read | refutes | Native Figure3 was visually inspected: panelsC/F compare Cdc10-mCherry-marked spore structures with Cdc12-GFP/Shs1-GFP; panelE shows Cdc12 persistence. Interpretation follows the primary caption and Results, without extracting new quantitative intensity values. |
| septin-array-agent-garcia2016 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4772501/; PMC4772501 Introduction s01, Results s07–s08 and Figure4 caption; DOI10.1083/jcb.201511029, PMID26929450 | refutes | Later primary study tests development-specific complexes. Results s08 uses FRAP and BiFC: Cdc3–Cdc10 and Cdc3–Spr3 mark PSM structures, whereas forced Cdc3–Cdc12 interaction is predominantly peripheral ascal puncta. The Introduction explicitly preserves detectable Cdc11 at the PSM while the bulk of Cdc12/Shs1 is excluded. These observations are scoped to tested sporulating backgrounds. |
| schema-result | just validate data/structures/cytoskeleton/septin_filament_array.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/septin_filament_array.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/septin_filament_array.yaml --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_filament_array-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/septin_filament_array.yaml --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_filament_array-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_filament_array-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/septin_filament_array.yaml; exact collect() scope; hash identifies the complete original /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv, not the derived target slice | supports | 16 of 19 collected target identifiers returned OK at the unchanged base. Residuals: PMID:14562095: UNREACHABLE; resolved by evidence septin-array-agent-paper-metadata; PMID:25971666: UNREACHABLE; resolved by evidence septin-array-agent-paper-metadata; PMID:9790978: UNREACHABLE; resolved by evidence septin-array-agent-paper-metadata. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The composition finding concerns the stated S. cerevisiae sporulation context. It is not a universal exclusion of Cdc12/Shs1 from every possible septin filament assembly, and it does not assign the Candida cohort.
- Primary McMurray2008 Figure3 was visually inspected with its caption and Results. Other microscopy pixels, raw movies and all supplements were not independently reanalyzed; no new intensity or prevalence measurement is made.
- Cdc11 detection in prospore structures and the composition of a reconstituted core hetero-octamer are different claims; this review does not conflate them or flag Cdc11 as absent.
- Candida chlamydospore localization is corroborated here at GO and Douglas review tiers; its original primary images were not reanalyzed for this generic record.
- Huh2003 and Mino1998 are metadata/abstract and native-UniProt-attribution bounded; their general membrane/bud-neck evidence does not establish prospore membership.
- Exact accessory inventory, stoichiometry and each paralog's essentiality remain separate questions. Missing optional fields and uncurated Spr3/Spr28 examples are not standalone findings.
- No historical issue disposition or global source absence is reasserted. Current source review does not establish independent historical authorship.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Native inspection and focused gates preceded assessment; expanded inspection includes the protein-example review skill.
- Unsaved draft for independent root audit; finalization, shared gates and saving remain pending.
- Only a review bundle is saved. Scientific records, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082244Z-septin-filament-array-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Septin filament array identity, composition and evidence review
started_at: '2026-10-21T08:08:45Z'
finished_at: '2026-10-21T08:22:44Z'
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
summary: Exact array identity and stage-dependent membrane contexts are supported.
  One minor generic-family gap and one major mismatch between two mitotic examples
  and the stated Saccharomyces sporulation context remain.
source:
  git_revision: 99692a3d5f16a7dcd6db7e3811344c299a977b81
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
  - path: data/structures/cytoskeleton/septin_filament_array.yaml
    sha256: 8413e81f4ac3c0daf46af8a81bbc0c819380242af370486f07865114e2edc1a0
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
- target_id: GO:0032160
  path: data/structures/cytoskeleton/septin_filament_array.yaml
  label: septin filament array
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained scientific record
scope:
  description: Entire single array target; all asserted native identities and sequence-example
    annotations; GO source-chain review, primary array localization and direct Cdc12/Shs1
    sporulation-membership experiments.
  selection: Second selected unreviewed path in batch eleven; path-ordered selection
    excluding 199 confirmed paths and 20 provisional pending paths from batches9–10.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032160
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032160
  command: just validate data/structures/cytoskeleton/septin_filament_array.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032160
  command: just validate-strict data/structures/cytoskeleton/septin_filament_array.yaml
    --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_filament_array-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0032160
  summary: 16 identifiers OK; 3 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - septin-array-agent-paper-metadata
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0032160
  summary: No expression-module or transcriptional-regulator mechanism is asserted;
    expression membership is not used as structural localization evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0032160
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - example-policy
  - septin-array-agent-go
  - septin-array-agent-family
  - septin-array-agent-paper-metadata
  - septin-array-agent-P32457
  - septin-array-agent-symbol-CDC3
  - septin-array-agent-P25342
  - septin-array-agent-symbol-CDC10
  - septin-array-agent-P32458
  - septin-array-agent-symbol-CDC11
  - septin-array-agent-P32468
  - septin-array-agent-symbol-CDC12
  - septin-array-agent-Q07657
  - septin-array-agent-symbol-SHS1
  - septin-array-agent-taxon-4932
  - septin-array-agent-taxon-559292
  - septin-array-agent-taxon-5476
  - septin-array-agent-douglas-pmc
  - septin-array-agent-versele-pmc
  - septin-array-agent-tachikawa2001
  - septin-array-agent-mcmurray2008
  - septin-array-agent-mcmurray2008-figure3
  - septin-array-agent-garcia2016
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032160
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0032160
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0032160
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0032160
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0032160
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/septin_filament_array.yaml
  locator: Entire target, all components/protein examples, taxonomy, graph edges,
    evidence and discussions
  accessed_at: '2026-10-21T08:17:20Z'
  support: context_only
  summary: Complete target read after native inspection. Maintained record and mapping
    status remain PROPOSED; no scientific promotion or content change.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: family grounding, composition and structure-formation essentiality'
  accessed_at: '2026-10-21T08:17:20Z'
  support: context_only
  summary: A generic family identifier is distinct from an exact localized cohort;
    ESSENTIAL refers to formation of the named structure, not viability or each named
    paralog.
- evidence_id: example-policy
  kind: record_content
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Non-negotiable rules1–5; captured as expanded native inspect input
  accessed_at: '2026-10-21T08:17:20Z'
  support: context_only
  summary: Correct accession, gene, taxon and entry status do not independently establish
    structure membership. Native subcellular-location evidence is retained only for
    the actual compartment named.
- evidence_id: septin-array-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032173,GO:0032156,GO:0032174,GO:0062140,GO:0005940,GO:0032160,GO:0005856,GO:0032165,GO:0032166,GO:0032159,GO:0005938,GO:0031105
  locator: Returned exact terms and isObsolete flags; definitions, synonyms and children
    with is_a versus part_of relations
  accessed_at: '2026-10-21T08:10:47.915532Z'
  support: supports
  summary: Exact active GO definitions, generic structure classes, named parents/children
    and structural parthood were checked. The returned broader terms expose the relevant
    child relations.
  snapshot_sha256: c354da8bddce6953db86b6ed705e054d4600415453e594bf8fa3eca70b56e47e
- evidence_id: septin-array-agent-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: metadata accession/name/type=family, description and hierarchy; original
    native receipt retained
  accessed_at: '2026-10-21T06:58:21.193684Z'
  support: supports
  summary: IPR016491 is the Septin family, appropriate to the generic septin-proteins
    label. It does not delimit one localized cohort, specify stoichiometry or prove
    membership of an individual example.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: septin-array-agent-paper-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=25&query=%28DOI%3A%2210.1091/mbc.E04-09-0764%22%29%20OR%20%28DOI%3A%2210.1534/genetics.107.073007%22%29%20OR%20%28DOI%3A%2210.1073/pnas.0803330105%22%29%20OR%20%28DOI%3A%2210.1016/j.devcel.2011.02.004%22%29%20OR%20%28DOI%3A%2210.3389/fcell.2016.00123%22%29%20OR%20%28DOI%3A%2210.1016/j.mib.2014.04.004%22%29%20OR%20%28DOI%3A%2210.1099/mic.0.000359%22%29%20OR%20%28EXT_ID%3A14562095%20AND%20SRC%3AMED%29%20OR%20%28EXT_ID%3A25971666%20AND%20SRC%3AMED%29%20OR%20%28EXT_ID%3A9790978%20AND%20SRC%3AMED%29
  locator: Relevant exact DOI/PMID result objects; publication metadata and abstracts
  accessed_at: '2026-10-21T08:11:32.949739Z'
  support: supports
  summary: Native metadata verifies exact DOI/PMID identities, authors, titles and
    source types for record-cited papers. Huh2003/PMID14562095, Finnigan2015/25971666
    and Mino1998/9790978 resolve despite residuals in the original resolver TSV. Metadata
    and abstracts do not substitute for unavailable primary bodies.
  snapshot_sha256: 7a7b007e68f306c7d0de37c899db2eb8918b72d81701e76ea7bed008ceb7d981
- evidence_id: septin-array-agent-P32457
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32457.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR
    LOCATION evidence
  accessed_at: '2026-10-21T08:10:47.918386Z'
  support: supports
  summary: The reviewed accession, recommended protein label, primary CDC3 symbol
    and organism taxon559292 match the record. Native subcellular-location annotations
    and their experimental PubMed citations were inspected without treating general
    membrane/bud-neck evidence as another morphogenetic localization.
  snapshot_sha256: 7fc581a719d6b12f8611b58bfc0c11fc057c73e673b217485a3379b8330b6efe
- evidence_id: septin-array-agent-symbol-CDC3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ACDC3%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in receipt, results cardinality, primaryAccession and gene
    token
  accessed_at: '2026-10-21T08:10:49.124537Z'
  support: context_only
  summary: Exact reviewed CDC3 query in S. cerevisiae returns one entry, P32457. The
    gene token and taxon were checked directly; this is an identity/uniqueness result,
    not membership evidence.
  snapshot_sha256: d15bf1b00b3f29538132111c0a6ab994f6bf134478224348f6857db31c1f4aee
- evidence_id: septin-array-agent-P25342
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P25342.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR
    LOCATION evidence
  accessed_at: '2026-10-21T08:10:47.919289Z'
  support: supports
  summary: The reviewed accession, recommended protein label, primary CDC10 symbol
    and organism taxon559292 match the record. Native subcellular-location annotations
    and their experimental PubMed citations were inspected without treating general
    membrane/bud-neck evidence as another morphogenetic localization.
  snapshot_sha256: 5a5194945989f266f18122a50805faa45f7bc00a599dcefcf7cf6592d753174d
- evidence_id: septin-array-agent-symbol-CDC10
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ACDC10%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in receipt, results cardinality, primaryAccession and gene
    token
  accessed_at: '2026-10-21T08:10:49.666227Z'
  support: context_only
  summary: Exact reviewed CDC10 query in S. cerevisiae returns one entry, P25342.
    The gene token and taxon were checked directly; this is an identity/uniqueness
    result, not membership evidence.
  snapshot_sha256: f9b9dc13ffea60b8a6bfb9d653d7a4ede1157e95cf417161793bf122b409fa8c
- evidence_id: septin-array-agent-P32458
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32458.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR
    LOCATION evidence
  accessed_at: '2026-10-21T08:10:47.920001Z'
  support: supports
  summary: The reviewed accession, recommended protein label, primary CDC11 symbol
    and organism taxon559292 match the record. Native subcellular-location annotations
    and their experimental PubMed citations were inspected without treating general
    membrane/bud-neck evidence as another morphogenetic localization.
  snapshot_sha256: 839db168d3ac73f1e1718845d2d92024c8bd535a96081c789ff55a1a0e98c922
- evidence_id: septin-array-agent-symbol-CDC11
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ACDC11%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in receipt, results cardinality, primaryAccession and gene
    token
  accessed_at: '2026-10-21T08:10:49.685815Z'
  support: context_only
  summary: Exact reviewed CDC11 query in S. cerevisiae returns one entry, P32458.
    The gene token and taxon were checked directly; this is an identity/uniqueness
    result, not membership evidence.
  snapshot_sha256: 384fe6c570f5d6549a3469d520685905279ff9f0303a7f72da1f0d9399322fc5
- evidence_id: septin-array-agent-P32468
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32468.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR
    LOCATION evidence
  accessed_at: '2026-10-21T08:10:47.920733Z'
  support: supports
  summary: The reviewed accession, recommended protein label, primary CDC12 symbol
    and organism taxon559292 match the record. Native subcellular-location annotations
    and their experimental PubMed citations were inspected without treating general
    membrane/bud-neck evidence as another morphogenetic localization.
  snapshot_sha256: 3a96072071fa02a2e65a0d5d80ebcf82c631ff8f674fc6ce5ae642b8b273619e
- evidence_id: septin-array-agent-symbol-CDC12
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ACDC12%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in receipt, results cardinality, primaryAccession and gene
    token
  accessed_at: '2026-10-21T08:10:49.721314Z'
  support: context_only
  summary: Exact reviewed CDC12 query in S. cerevisiae returns one entry, P32468.
    The gene token and taxon were checked directly; this is an identity/uniqueness
    result, not membership evidence.
  snapshot_sha256: 0096f0d783694af4a97eabab1e461dba9433f5de30a034cd6f25b0b667097721
- evidence_id: septin-array-agent-Q07657
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q07657.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR
    LOCATION evidence
  accessed_at: '2026-10-21T08:10:48.935670Z'
  support: supports
  summary: The reviewed accession, recommended protein label, primary SHS1 symbol
    and organism taxon559292 match the record. Native subcellular-location annotations
    and their experimental PubMed citations were inspected without treating general
    membrane/bud-neck evidence as another morphogenetic localization.
  snapshot_sha256: 4b3fa80abaa9782dee6cb8412786a5eed43b5df173dd4a150079a04064ec2627
- evidence_id: septin-array-agent-symbol-SHS1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ASHS1%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in receipt, results cardinality, primaryAccession and gene
    token
  accessed_at: '2026-10-21T08:10:49.790448Z'
  support: context_only
  summary: Exact reviewed SHS1 query in S. cerevisiae returns one entry, Q07657. The
    gene token and taxon were checked directly; this is an identity/uniqueness result,
    not membership evidence.
  snapshot_sha256: 0a077959f8d07e4292e2a3362dd78fb89992cf62800d84b1ad922eca984fd0c2
- evidence_id: septin-array-agent-taxon-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T08:10:49.039898Z'
  support: supports
  summary: Native taxonomy confirms the exact taxon identifier, scientific name and
    rank; species scope is distinguished from the S288C sequence-example strain.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: septin-array-agent-taxon-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T08:10:49.045688Z'
  support: supports
  summary: Native taxonomy confirms the exact taxon identifier, scientific name and
    rank; species scope is distinguished from the S288C sequence-example strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-array-agent-taxon-5476
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5476
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T08:10:49.122575Z'
  support: supports
  summary: Native taxonomy confirms the exact taxon identifier, scientific name and
    rank; species scope is distinguished from the S288C sequence-example strain.
  snapshot_sha256: 08e8826cff83a3f5a49f421aabb8521db87bea533522187fb8649669a097d4dc
- evidence_id: septin-array-agent-douglas-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/
  locator: PMC1214204 sec14 and sec17; original receipt retained; review-tier synthesis
  accessed_at: '2026-10-21T07:11:03.050463Z'
  support: supports
  summary: The GO definition source is a literature review. It describes prospore
    septin sheets appearing as bars in optical sections and Candida chlamydospore
    peripheral filament arrays after septation. These stage-dependent localizations
    are not a single universal mitotic paralog set.
  snapshot_sha256: 31a2dd0109697492854f84701ef3f1d1be31f62312b613ab8432223332b69dd3
- evidence_id: septin-array-agent-versele-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render
  locator: PMC1761124 S2 paragraphP4; original receipt retained; review tier
  accessed_at: '2026-10-21T07:29:14.610794Z'
  support: supports
  summary: The review distinguishes mitotic Cdc3/Cdc10/Cdc11/Cdc12/Shs1 collars from
    a sporulation-specific cohort that replaces Cdc12/Shs1 with Spr3/Spr28. It provides
    context, not the primary exclusion experiment.
  snapshot_sha256: bfa7c582507daf47688819cdd2ed31ed4dab32ed0d9e14a0d74d40c29249ac9d
- evidence_id: septin-array-agent-tachikawa2001
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2150859/?pdf=render
  locator: PMC2150859 Results sec7–10 and Figures5–9 legends; original receipt retained
  accessed_at: '2026-10-21T07:55:41.272676Z'
  support: supports
  summary: Primary Spr28/Gip1/Glc7 imaging supports a dynamic prospore-membrane array.
    Optical bars can represent parallel sheets; the Don1 leading-edge ring is distinct.
    Disrupted septin localization in gip1 mutants does not by itself establish that
    every membrane process requires every septin.
  snapshot_sha256: 27192ba28363973204c857601dde3518874638519f0d30c6d5b5b7f20719bba2
- evidence_id: septin-array-agent-mcmurray2008
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2562167/
  locator: 'PMC2562167 Results and Discussion S1: sporulation paragraphs beginning
    Two septins required / Like Cdc10 / Unlike CDC3; Figure3A,C,E,F,G and caption;
    DOI10.1016/j.cub.2008.07.020, PMID18701287'
  accessed_at: '2026-10-21T08:11:51.098761Z'
  support: refutes
  summary: Primary dual-color imaging finds little or no Cdc12-GFP in Cdc10-mCherry-marked
    spore-associated structures and no Shs1-GFP colocalization there; Shs1 remains
    in ascal cytoplasm. Cdc12 persists by immunoblot, so failure to detect it in the
    array is not attributed simply to degradation. Cdc10 is reused through the developmental
    transition. This directly challenges the unqualified Cdc12/Shs1 examples in the
    record's S. cerevisiae sporulation context.
  snapshot_sha256: 733f9847b03c2a17ebb778371ce63027f260d901cbaf0746b298a22a3ca13f26
- evidence_id: septin-array-agent-mcmurray2008-figure3
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/502c/2562167/a3850b2cb250/nihms67754f3.jpg
  locator: Original PMC image nihms67754f3.jpg, Figure3 panelsA–G; direct image and
    adjacent caption read
  accessed_at: '2026-10-21T08:13:34.046259Z'
  support: refutes
  summary: 'Native Figure3 was visually inspected: panelsC/F compare Cdc10-mCherry-marked
    spore structures with Cdc12-GFP/Shs1-GFP; panelE shows Cdc12 persistence. Interpretation
    follows the primary caption and Results, without extracting new quantitative intensity
    values.'
  snapshot_sha256: 09d4e5f7c061be87831d7ce567a851b3b48c639ae4d9b234dd80564e0a86260b
- evidence_id: septin-array-agent-garcia2016
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4772501/
  locator: PMC4772501 Introduction s01, Results s07–s08 and Figure4 caption; DOI10.1083/jcb.201511029,
    PMID26929450
  accessed_at: '2026-10-21T08:11:51.098969Z'
  support: refutes
  summary: 'Later primary study tests development-specific complexes. Results s08
    uses FRAP and BiFC: Cdc3–Cdc10 and Cdc3–Spr3 mark PSM structures, whereas forced
    Cdc3–Cdc12 interaction is predominantly peripheral ascal puncta. The Introduction
    explicitly preserves detectable Cdc11 at the PSM while the bulk of Cdc12/Shs1
    is excluded. These observations are scoped to tested sporulating backgrounds.'
  snapshot_sha256: 9ed04f473b63a27b574363c12a31e28b4cab81e31006fd0713e1602dc9769229
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/septin_filament_array.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:08:50Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/septin_filament_array.yaml'
  snapshot_sha256: 854197a6476c0c85ebcf0b5681f50e5eff43f5eb28a6ca74f8240bd4d6b816ba
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/septin_filament_array.yaml
    --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_filament_array-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:08:52Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/septin_filament_array.yaml\
    \ --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_filament_array-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_filament_array-strict.tsv"
  snapshot_sha256: af6b8cffbee95702418e66e702e8f2054677129f70355bd522c35bdd48f97f13
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/septin_filament_array.yaml; exact collect()
    scope; hash identifies the complete original /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv,
    not the derived target slice
  accessed_at: '2026-10-21T08:17:20Z'
  support: supports
  summary: '16 of 19 collected target identifiers returned OK at the unchanged base.
    Residuals: PMID:14562095: UNREACHABLE; resolved by evidence septin-array-agent-paper-metadata;
    PMID:25971666: UNREACHABLE; resolved by evidence septin-array-agent-paper-metadata;
    PMID:9790978: UNREACHABLE; resolved by evidence septin-array-agent-paper-metadata.
    Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec
  accessed_at: '2026-10-19T07:38:12Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 7b6165ba8532d080a336f7a5a4c29b456fdf7182dd596410b700dfe60af61a06
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-19T07:29:37Z'
  support: supports
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: b98e3eecd58a81fa46033e6baca6977811a439f119b943fd5d9931964adb2680
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad
  accessed_at: '2026-10-19T07:32:39Z'
  support: supports
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-19T07:29:45Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4
  accessed_at: '2026-10-19T08:04:01Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  snapshot_sha256: 7cb413edccc92ee6ce79a32cd2b96a59bc4da37f2cb7b326eaca51a64f723cfb
assessments:
- assessment_id: identity
  area: identity
  topic: Generic array and localized children
  outcome: supported
  target_ids:
  - GO:0032160
  summary: GO0032160 exactly matches the bar/filament-array definition, septin-cytoskeleton
    parent and cytoskeleton parthood. Prospore and chlamydospore terms remain narrower
    array classes; ring, collar and cap are distinguished rather than merged.
  evidence_ids:
  - septin-array-agent-go
  - septin-array-agent-douglas-pmc
  - record
- assessment_id: scope
  area: scope
  topic: Developmental species contexts
  outcome: supported
  target_ids:
  - GO:0032160
  summary: The GO-backed S. cerevisiae sporulation and C. albicans chlamydospore examples
    are accurately attributed, and VARIABLE preserves growth-stage dependence. Species
    identities and the S288C sequence-example strain are correct. Native GO does not
    constitute a primary experiment or a universal quantitative prevalence estimate.
  evidence_ids:
  - septin-array-agent-go
  - septin-array-agent-douglas-pmc
  - septin-array-agent-tachikawa2001
  - septin-array-agent-taxon-4932
  - septin-array-agent-taxon-559292
  - septin-array-agent-taxon-5476
  - record
- assessment_id: graph
  area: graph
  topic: Composition and membrane-localization topology
  outcome: supported
  target_ids:
  - GO:0032160
  summary: The three NONMECHANISTIC edges are supported at the generic-family and
    stated membrane-context levels. Bars are not assigned molecular thickness or treated
    as directly resolved single filaments; optical-sheet interpretation is retained.
    Neither Don1 rings nor a complete recruitment/force-generation mechanism is imported.
  evidence_ids:
  - septin-array-agent-go
  - septin-array-agent-douglas-pmc
  - septin-array-agent-tachikawa2001
  - record
- assessment_id: sequence-identities
  area: grounding
  topic: Accurate accession identity and imported compartment notes
  outcome: supported
  target_ids:
  - GO:0032160
  summary: All five reviewed identities, labels, primary symbols, S288C taxon and
    exact-query uniqueness checks pass. Native UniProt supports the imported general
    membrane/bud-neck citations exactly. Those notes deliberately do not establish
    sporulation-array membership, and identity correctness is retained independently
    of the membership finding.
  evidence_ids:
  - septin-array-agent-P32457
  - septin-array-agent-symbol-CDC3
  - septin-array-agent-P25342
  - septin-array-agent-symbol-CDC10
  - septin-array-agent-P32458
  - septin-array-agent-symbol-CDC11
  - septin-array-agent-P32468
  - septin-array-agent-symbol-CDC12
  - septin-array-agent-Q07657
  - septin-array-agent-symbol-SHS1
  - record
  - example-policy
- assessment_id: family
  area: grounding
  topic: Generic Septin family versus localized cohort
  outcome: concern
  target_ids:
  - GO:0032160
  summary: The component is named septin proteins but its rationale withholds grounding
    until a family denotes the complete assembly-forming cohort. IPR016491 supplies
    the generic family identity; localized composition remains a separate scientific
    question.
  evidence_ids:
  - septin-array-agent-family
  - record
  - policy
- assessment_id: array-membership
  area: evidence
  topic: Mitotic examples versus the stated sporulation array
  outcome: concern
  target_ids:
  - GO:0032160
  summary: The current Saccharomyces example is specifically a prospore-membrane array,
    yet its component declares the full mitotic five-gene set. Primary imaging contradicts
    unqualified Cdc12/Shs1 assignment in that context. This does not establish their
    absence from every conceivable filament array or invalidate the three other accurate
    identities; Cdc11 detection in the PSM literature is retained.
  evidence_ids:
  - septin-array-agent-mcmurray2008
  - septin-array-agent-mcmurray2008-figure3
  - septin-array-agent-garcia2016
  - septin-array-agent-versele-pmc
  - septin-array-agent-douglas-pmc
  - record
  - example-policy
- assessment_id: provenance
  area: provenance
  topic: Ontology source chain and independent primary falsification
  outcome: supported
  target_ids:
  - GO:0032160
  summary: The current record correctly cites GO for its two example contexts; the
    review reads the underlying Douglas synthesis and separate primary tests. Native
    PubMed metadata and UniProt citations remain correct. The historical removal of
    unread Douglas evidence is not retroactively represented as a prior full-text
    read.
  evidence_ids:
  - septin-array-agent-go
  - septin-array-agent-douglas-pmc
  - septin-array-agent-tachikawa2001
  - septin-array-agent-mcmurray2008
  - septin-array-agent-garcia2016
  - septin-array-agent-paper-metadata
  - record
findings:
- finding_id: F1
  issue_key: septin-filament-array-generic-family-withheld
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Localized-cohort criterion leaves the generic Septin family ungrounded
  description: The generic septin-proteins component is REVIEWED_LABEL_ONLY because
    its rationale asks for an accession matching the complete localized cohort. Verified
    IPR016491 identifies the named Septin family without requiring a localization-specific
    family. Reconcile grounding, status and rationale while preserving separate uncertainty
    about exact paralogs and associated proteins.
  target_ids:
  - GO:0032160
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions
  evidence_ids:
  - septin-array-agent-family
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: A bounded generic-family mapping gap; exact structure identity
    and species-specific composition are separate.
- finding_id: F2
  issue_key: septin-filament-array-mitotic-examples-in-sporulation-context
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Cdc12 and Shs1 examples are not supported in the stated Saccharomyces array
    context
  description: The only S. cerevisiae array context declared by this record is the
    prospore membrane during sporulation. Its septin component nevertheless includes
    CDC12/P32468 and SHS1/Q07657 as unqualified structural examples alongside the
    mitotic set. Their identities are correct, but primary dual-color localization
    finds little or no Cdc12 and no Shs1 in the Cdc10-marked sporulation structures;
    later work independently distinguishes the development-specific assembly. Restrict
    these assignments or provide direct evidence for an explicitly stated alternative
    array context. This is not an assertion that Cdc12/Shs1 cannot occur in any structure
    described loosely as an array, nor that the accessions are wrong.
  target_ids:
  - GO:0032160
  field_paths:
  - components[component_id=septin_proteins].gene_symbols
  - components[component_id=septin_proteins].protein_examples
  evidence_ids:
  - septin-array-agent-mcmurray2008
  - septin-array-agent-mcmurray2008-figure3
  - septin-array-agent-garcia2016
  - septin-array-agent-versele-pmc
  - septin-array-agent-P32457
  - septin-array-agent-symbol-CDC3
  - septin-array-agent-P25342
  - septin-array-agent-symbol-CDC10
  - septin-array-agent-P32458
  - septin-array-agent-symbol-CDC11
  - septin-array-agent-P32468
  - septin-array-agent-symbol-CDC12
  - septin-array-agent-Q07657
  - septin-array-agent-symbol-SHS1
  - record
  - example-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: major
  normalization_reason: A material localized-component assignment conflicts with direct
    primary evidence in the specific developmental context that the record supplies;
    generic family membership does not resolve it.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032160
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained scientific record
  description: Under separately authorized curation, ground the generic Septin component
    to verified IPR016491 and reconcile the cohort-based rationale.
  acceptance_checks:
  - Retain separate membership evidence; do not infer universal paralog usage or stoichiometry
    from a family match.
  - Retain structure-level rather than individual-protein viability essentiality.
  - Use guarded curation/history and run native schema, strict, identifier-label,
    protein-example and rendered-page checks.
  generator: Maintained scientific YAML; generated pages derive through just render.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0032160
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained scientific record
  description: 'Under separately authorized curation, reconcile the CDC12 and SHS1
    symbols/examples with the stated S. cerevisiae sporulation-array scope: restrict/remove
    these structural assignments, or document a distinct source-supported context
    that actually fits this GO array class.'
  acceptance_checks:
  - Preserve correct accession identity and taxon information separately from structural
    membership.
  - Do not infer absence from every array architecture or remove Cdc11 solely from
    a modern core-rod model; published PSM detection is distinct from integral rod
    composition.
  - If adding Spr3/Spr28 as better-supported sporulation examples, verify their own
    exact native accession/taxon and localization evidence before editing.
  - Do not infer Candida paralog membership from Saccharomyces or impose an exhaustive
    inventory requirement.
  - Use guarded curation/history and run focused schema, strict, UniProt identity,
    label and generated-page checks.
  generator: Maintained scientific YAML; generated pages derive through just render.
limitations:
- The composition finding concerns the stated S. cerevisiae sporulation context. It
  is not a universal exclusion of Cdc12/Shs1 from every possible septin filament assembly,
  and it does not assign the Candida cohort.
- Primary McMurray2008 Figure3 was visually inspected with its caption and Results.
  Other microscopy pixels, raw movies and all supplements were not independently reanalyzed;
  no new intensity or prevalence measurement is made.
- Cdc11 detection in prospore structures and the composition of a reconstituted core
  hetero-octamer are different claims; this review does not conflate them or flag
  Cdc11 as absent.
- Candida chlamydospore localization is corroborated here at GO and Douglas review
  tiers; its original primary images were not reanalyzed for this generic record.
- Huh2003 and Mino1998 are metadata/abstract and native-UniProt-attribution bounded;
  their general membrane/bud-neck evidence does not establish prospore membership.
- Exact accessory inventory, stoichiometry and each paralog's essentiality remain
  separate questions. Missing optional fields and uncurated Spr3/Spr28 examples are
  not standalone findings.
- No historical issue disposition or global source absence is reasserted. Current
  source review does not establish independent historical authorship.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Native inspection and focused gates preceded assessment; expanded inspection includes
  the protein-example review skill.
- Unsaved draft for independent root audit; finalization, shared gates and saving
  remain pending.
- Only a review bundle is saved. Scientific records, native status, history and generated
  pages remain unchanged.
```
