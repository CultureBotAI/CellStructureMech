# Septin ring identity, composition and evidence review

- Review: 20261021T082244Z-septin-ring-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:08:52Z
- Finished UTC: 2026-10-21T08:22:44Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact cortical ring identity, fungal and Saccharomyces scope, mitotic examples and bounded assembly/scaffold claims are supported. One minor generic Septin-family grounding gap remains.

## Scope And Provenance

Entire single ring target; every asserted native identifier; source-specific primary assembly/localization experiments, cited fungal reviews, all sequence examples and all graph edges.

Selection: Third selected unreviewed path in batch eleven; path-ordered selection excluding 199 confirmed paths and 20 provisional pending paths from batches9–10.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005940 | data/structures/cytoskeleton/septin_ring.yaml | maintained | septin ring |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005940 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005940 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0005940 | 18 identifiers OK; 3 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0005940 | No expression-module or transcriptional-regulator mechanism is asserted; expression membership is not used as structural localization evidence. |
| Claim-level scientific review | passed | True | GO:0005940 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0005940 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005940 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005940 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005940 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0005940 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Higher-order cortical ring versus smaller septin complexes

identity: supported. Targets: GO:0005940.

GO0005940 matches the defined higher-order ring, its septin-cytoskeleton parent and cell-cortex parthood. GO0031105 is a smaller oligomeric complex, appropriately retained as a distinct assembly level. The microbial record uses fungal examples without claiming that the GO class excludes animal rings.

### Five identity examples and mitotic structural cohort

grounding: supported. Targets: GO:0005940.

All sequence identities, primary symbols, reviewed statuses, S288C taxon labels and uniqueness checks pass. Primary and review evidence supports the five mitotic bud-neck septins. General membrane/bud-neck annotations are not silently promoted to a different localization. Collective ESSENTIAL is not a claim that each paralog is individually necessary for every ring.

### Fungal occurrence and Saccharomyces model

scope: supported. Targets: GO:0005940.

Native Fungi/species/strain identities agree. COMMON is a qualitative fungal occurrence statement with explicit variation by lineage and morphogenetic context, not universal occurrence, numerical prevalence or universal essentiality. The named Saccharomyces example is supported by Iwase; tested backgrounds are not equated to every S288C-derived strain.

### Division-site scaffold and cytokinesis factors

evidence: supported. Targets: GO:0005940.

Budding-yeast recruitment and cytokinesis-site organization have direct experimental support, while broader fungal scaffolding rests on reviews. The record does not claim direct binding for every cytokinesis factor or that septins generate constriction force or determine every fungal cleavage plane.

### Scoped oligomer-to-filament-to-ring hierarchy

graph: supported. Targets: GO:0005940.

The NONMECHANISTIC graph is explicitly a Saccharomyces assembly hierarchy, supported by the reconstituted Cdc11-capped core and budding-cell localization. It does not specify all five paralogs in one octamer or a universal fungal rod order. Shs1-capped rods and viable alternative hexamers limit universal reading of the generic rod-to-filament edge; these documented exceptions are retained in this assessment.

### Generic Septin family versus localized cohort

grounding: concern. Targets: GO:0005940.

The component is named septin proteins but its rationale withholds grounding until a family denotes the complete assembly-forming cohort. IPR016491 supplies the generic family identity; localized composition remains a separate scientific question.

### Primary experiments versus literature reviews

provenance: supported. Targets: GO:0005940.

Iwase/Bertin/McMurray are primary experiments, while Glomb/Bridges/Vargas are explicit review-tier authorities. The exact cited paper identities and native UniProt localization citations match. Generic PMC routes initially returned challenges, but report=xml routes delivered genuine readable HTML; no challenged response is used as body evidence.

### Optional detailed composition and mechanism

completeness: supported. Targets: GO:0005940.

No exhaustive accessory-protein list, molecular dimensions, image license or full ordered recruitment mechanism is asserted. Optional unresolved details and distinct localized ring subtypes do not create additional findings.

## Findings

### F1: Localized-cohort criterion leaves the generic Septin family ungrounded

minor / open / confirmed; issue key: septin-ring-generic-family-withheld.

The generic septin-proteins component is REVIEWED_LABEL_ONLY because its rationale asks for an accession matching the complete localized cohort. Verified IPR016491 identifies the named Septin family without requiring a localization-specific family. Reconcile grounding, status and rationale while preserving separate uncertainty about exact paralogs and associated proteins.

## Recommended Actions And Acceptance Checks

### A1

Under separately authorized curation, ground the generic Septin component to verified IPR016491 and reconcile the cohort-based rationale.

- Retain separate membership evidence; do not infer universal paralog usage or stoichiometry from a family match.
- Retain structure-level rather than individual-protein viability essentiality.
- Use guarded curation/history and run native schema, strict, identifier-label, protein-example and rendered-page checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/septin_ring.yaml; Entire target, all components/protein examples, taxonomy, graph edges, evidence and discussions | context_only | Complete target read after native inspection. Maintained record and mapping status remain PROPOSED; no scientific promotion or content change. |
| policy | docs/CURATION.md; Components: family grounding, composition and structure-formation essentiality | context_only | A generic family identifier is distinct from an exact localized cohort; ESSENTIAL refers to formation of the named structure, not viability or each named paralog. |
| example-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Non-negotiable rules1–5; captured as expanded native inspect input | context_only | Correct accession, gene, taxon and entry status do not independently establish structure membership. Native subcellular-location evidence is retained only for the actual compartment named. |
| septin-ring-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032173,GO:0032156,GO:0032174,GO:0062140,GO:0005940,GO:0032160,GO:0005856,GO:0032165,GO:0032166,GO:0032159,GO:0005938,GO:0031105; Returned exact terms and isObsolete flags; definitions, synonyms and children with is_a versus part_of relations | supports | Exact active GO definitions, generic structure classes, named parents/children and structural parthood were checked. The returned broader terms expose the relevant child relations. |
| septin-ring-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; metadata accession/name/type=family, description and hierarchy; original native receipt retained | supports | IPR016491 is the Septin family, appropriate to the generic septin-proteins label. It does not delimit one localized cohort, specify stoichiometry or prove membership of an individual example. |
| septin-ring-agent-paper-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=25&amp;query=%28DOI%3A%2210.1091/mbc.E04-09-0764%22%29%20OR%20%28DOI%3A%2210.1534/genetics.107.073007%22%29%20OR%20%28DOI%3A%2210.1073/pnas.0803330105%22%29%20OR%20%28DOI%3A%2210.1016/j.devcel.2011.02.004%22%29%20OR%20%28DOI%3A%2210.3389/fcell.2016.00123%22%29%20OR%20%28DOI%3A%2210.1016/j.mib.2014.04.004%22%29%20OR%20%28DOI%3A%2210.1099/mic.0.000359%22%29%20OR%20%28EXT_ID%3A14562095%20AND%20SRC%3AMED%29%20OR%20%28EXT_ID%3A25971666%20AND%20SRC%3AMED%29%20OR%20%28EXT_ID%3A9790978%20AND%20SRC%3AMED%29; Relevant exact DOI/PMID result objects; publication metadata and abstracts | supports | Native metadata verifies exact DOI/PMID identities, authors, titles and source types for record-cited papers. Huh2003/PMID14562095, Finnigan2015/25971666 and Mino1998/9790978 resolve despite residuals in the original resolver TSV. Metadata and abstracts do not substitute for unavailable primary bodies. |
| septin-ring-agent-P32457 | https://rest.uniprot.org/uniprotkb/P32457.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC3 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-ring-agent-symbol-CDC3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC3%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC3 query in S. cerevisiae returns one entry, P32457. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-ring-agent-P25342 | https://rest.uniprot.org/uniprotkb/P25342.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC10 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-ring-agent-symbol-CDC10 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC10%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC10 query in S. cerevisiae returns one entry, P25342. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-ring-agent-P32458 | https://rest.uniprot.org/uniprotkb/P32458.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC11 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-ring-agent-symbol-CDC11 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC11%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC11 query in S. cerevisiae returns one entry, P32458. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-ring-agent-P32468 | https://rest.uniprot.org/uniprotkb/P32468.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC12 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-ring-agent-symbol-CDC12 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC12%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC12 query in S. cerevisiae returns one entry, P32468. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-ring-agent-Q07657 | https://rest.uniprot.org/uniprotkb/Q07657.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary SHS1 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-ring-agent-symbol-SHS1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ASHS1%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed SHS1 query in S. cerevisiae returns one entry, Q07657. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-ring-agent-taxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank and lineage | supports | Native taxonomy confirms the exact taxon identifier, scientific name and rank; species scope is distinguished from the S288C sequence-example strain. |
| septin-ring-agent-taxon-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId, scientificName, rank and lineage | supports | Native taxonomy confirms the exact taxon identifier, scientific name and rank; species scope is distinguished from the S288C sequence-example strain. |
| septin-ring-agent-taxon-4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; taxId, scientificName, rank and lineage | supports | Native taxonomy confirms the exact taxon identifier, scientific name and rank; species scope is distinguished from the S288C sequence-example strain. |
| septin-ring-agent-iwase2007-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC2013704/?report=xml; PMC2013704 abstract, Results sec8–9/Figures2–3 captions and Discussion sec14/sec16; PMID17603111, DOI10.1534/genetics.107.073007 | supports | Primary S. cerevisiae experiments verify Shs1 bud-neck localization and distinguish septin ring assembly from recruitment of cytokinesis factors. Shs1 deletion can leave Cdc3/Cdc10/Cdc11/Cdc12 rings assembled while Iqg1/Myo1/Cyk3 localization and cytokinesis are impaired; requirement depends on background and conditions. |
| septin-ring-agent-bertin2008-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC2426963/?report=xml; PMC2426963 Results sec2–6, especially sec2 and sec4/Figures1 and4 legends; exact DOI10.1073/pnas.0803330105 | supports | Purified recombinant Cdc3/Cdc10/Cdc11/Cdc12 complexes form nonpolar octameric rods; lowering salt yields end-to-end paired filaments. The direct reconstitution establishes a four-paralog core with two copies each, not simultaneous incorporation of all five listed mitotic paralogs. Shs1 replacement was a proposal in this paper. |
| septin-ring-agent-mcmurray2011-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC3079881/?report=xml; PMC3079881 Results S7/S9/S10 with Figures3,5,6 captions and Discussion S11; DOI10.1016/j.devcel.2011.02.004 | supports | Primary interface-mutant and microscopy experiments connect filament polymerization to cortical organization and viability in the tested yeast conditions. Cdc10- or Cdc11-deficient cells can survive via alternative hexameric assemblies, so neither individual necessity nor one oligomer size is universal. |
| septin-ring-agent-glomb2016-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC5093138/?report=xml; PMC5093138 main text paragraphs beginning The classical Hartwell screen / The mitotic yeast / Septin octamers containing Shs1 / In the living yeast cell / After bud formation / Taken together; Figure2 legend; review tier | supports | Review synthesis supports the five mitotic septins, bud-site recruitment, ring-to-collar/split-ring transitions and scaffold functions. It explicitly distinguishes Cdc11-capped rods that assemble end-to-end from Shs1-capped rods that preferentially form curved/lateral assemblies. |
| septin-ring-agent-bridges2014-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC4266239/?report=xml; PMC4266239 S1–S3 and Figure1 textual legend; review tier, DOI10.1016/j.mib.2014.04.004 | supports | Review of fungal pathogens supports septin scaffolding at division sites and species-specific higher-order localization, including bud-neck and hyphal septation contexts. It cautions that many mechanistic explanations remain unresolved and mutant phenotypes can be indirect. |
| septin-ring-agent-vargas2016-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC5068138/?report=xml; PMC5068138 s1-3, s1-5 and s1-6, Figure1 textual legend; review tier, DOI10.1099/mic.0.000359 | supports | Review supports broad fungal septin occurrence and functions in morphology, septation and development, while distinguishing species-dependent rod composition and Shs1-dependent assembly. Septin deletion often reduces rather than abolishes septation. |
| schema-result | just validate data/structures/cytoskeleton/septin_ring.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/septin_ring.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/septin_ring.yaml --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_ring-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/septin_ring.yaml --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_ring-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_ring-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/septin_ring.yaml; exact collect() scope; hash identifies the complete original /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv, not the derived target slice | supports | 18 of 21 collected target identifiers returned OK at the unchanged base. Residuals: PMID:14562095: UNREACHABLE; resolved by evidence septin-ring-agent-paper-metadata; PMID:25971666: UNREACHABLE; resolved by evidence septin-ring-agent-paper-metadata; PMID:9790978: UNREACHABLE; resolved by evidence septin-ring-agent-paper-metadata. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The rod-to-filament model is the representative Cdc11-capped Saccharomyces core. Shs1-capped assemblies and mutant hexamers differ; no all-five-in-one-octamer or universal fungal architecture is inferred.
- Primary text and selected figure legends were read; all microscopy pixels, raw datasets and supplementary experiments were not independently reanalyzed.
- The fungal distribution and cross-species scaffold generalization use review-tier synthesis. Quantitative fungal prevalence and universal division-plane determination are not established.
- Huh2003 and Mino1998 remain abstract/metadata and native-UniProt-attribution bounded. Those notes verify imported annotation scope, not every original experimental detail.
- Collective essential septin material is distinct from individual paralog or organismal viability requirements; a complete associated-protein inventory remains optional.
- Historical issue dispositions and unread-source claims are not revalidated; no prior finding is formally closed and no new absence claim is made.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Native inspection and focused gates preceded assessment; expanded inspection includes the protein-example review skill.
- Unsaved draft for independent root audit; finalization, shared gates and saving remain pending.
- Only a review bundle is saved. Scientific records, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082244Z-septin-ring-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Septin ring identity, composition and evidence review
started_at: '2026-10-21T08:08:52Z'
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
summary: Exact cortical ring identity, fungal and Saccharomyces scope, mitotic examples
  and bounded assembly/scaffold claims are supported. One minor generic Septin-family
  grounding gap remains.
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
  - path: data/structures/cytoskeleton/septin_ring.yaml
    sha256: a29add3311f4b53bf4b50c2ec527d5ef450cfff625eadd312324d625b8790b93
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
- target_id: GO:0005940
  path: data/structures/cytoskeleton/septin_ring.yaml
  label: septin ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_ring.yaml
    role: maintained scientific record
scope:
  description: Entire single ring target; every asserted native identifier; source-specific
    primary assembly/localization experiments, cited fungal reviews, all sequence
    examples and all graph edges.
  selection: Third selected unreviewed path in batch eleven; path-ordered selection
    excluding 199 confirmed paths and 20 provisional pending paths from batches9–10.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005940
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005940
  command: just validate data/structures/cytoskeleton/septin_ring.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005940
  command: just validate-strict data/structures/cytoskeleton/septin_ring.yaml --out
    /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_ring-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0005940
  summary: 18 identifiers OK; 3 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - septin-ring-agent-paper-metadata
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005940
  summary: No expression-module or transcriptional-regulator mechanism is asserted;
    expression membership is not used as structural localization evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005940
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - example-policy
  - septin-ring-agent-go
  - septin-ring-agent-family
  - septin-ring-agent-paper-metadata
  - septin-ring-agent-P32457
  - septin-ring-agent-symbol-CDC3
  - septin-ring-agent-P25342
  - septin-ring-agent-symbol-CDC10
  - septin-ring-agent-P32458
  - septin-ring-agent-symbol-CDC11
  - septin-ring-agent-P32468
  - septin-ring-agent-symbol-CDC12
  - septin-ring-agent-Q07657
  - septin-ring-agent-symbol-SHS1
  - septin-ring-agent-taxon-4932
  - septin-ring-agent-taxon-559292
  - septin-ring-agent-taxon-4751
  - septin-ring-agent-iwase2007-xml
  - septin-ring-agent-bertin2008-xml
  - septin-ring-agent-mcmurray2011-xml
  - septin-ring-agent-glomb2016-xml
  - septin-ring-agent-bridges2014-xml
  - septin-ring-agent-vargas2016-xml
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005940
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
  - GO:0005940
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
  - GO:0005940
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
  - GO:0005940
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
  - GO:0005940
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
  reference: data/structures/cytoskeleton/septin_ring.yaml
  locator: Entire target, all components/protein examples, taxonomy, graph edges,
    evidence and discussions
  accessed_at: '2026-10-21T08:17:23Z'
  support: context_only
  summary: Complete target read after native inspection. Maintained record and mapping
    status remain PROPOSED; no scientific promotion or content change.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: family grounding, composition and structure-formation essentiality'
  accessed_at: '2026-10-21T08:17:23Z'
  support: context_only
  summary: A generic family identifier is distinct from an exact localized cohort;
    ESSENTIAL refers to formation of the named structure, not viability or each named
    paralog.
- evidence_id: example-policy
  kind: record_content
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Non-negotiable rules1–5; captured as expanded native inspect input
  accessed_at: '2026-10-21T08:17:23Z'
  support: context_only
  summary: Correct accession, gene, taxon and entry status do not independently establish
    structure membership. Native subcellular-location evidence is retained only for
    the actual compartment named.
- evidence_id: septin-ring-agent-go
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
- evidence_id: septin-ring-agent-family
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
- evidence_id: septin-ring-agent-paper-metadata
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
- evidence_id: septin-ring-agent-P32457
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
- evidence_id: septin-ring-agent-symbol-CDC3
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
- evidence_id: septin-ring-agent-P25342
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
- evidence_id: septin-ring-agent-symbol-CDC10
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
- evidence_id: septin-ring-agent-P32458
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
- evidence_id: septin-ring-agent-symbol-CDC11
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
- evidence_id: septin-ring-agent-P32468
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
- evidence_id: septin-ring-agent-symbol-CDC12
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
- evidence_id: septin-ring-agent-Q07657
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
- evidence_id: septin-ring-agent-symbol-SHS1
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
- evidence_id: septin-ring-agent-taxon-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T08:10:49.039898Z'
  support: supports
  summary: Native taxonomy confirms the exact taxon identifier, scientific name and
    rank; species scope is distinguished from the S288C sequence-example strain.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: septin-ring-agent-taxon-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T08:10:49.045688Z'
  support: supports
  summary: Native taxonomy confirms the exact taxon identifier, scientific name and
    rank; species scope is distinguished from the S288C sequence-example strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-ring-agent-taxon-4751
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T08:10:49.121136Z'
  support: supports
  summary: Native taxonomy confirms the exact taxon identifier, scientific name and
    rank; species scope is distinguished from the S288C sequence-example strain.
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: septin-ring-agent-iwase2007-xml
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2013704/?report=xml
  locator: PMC2013704 abstract, Results sec8–9/Figures2–3 captions and Discussion
    sec14/sec16; PMID17603111, DOI10.1534/genetics.107.073007
  accessed_at: '2026-10-21T08:12:10.187399Z'
  support: supports
  summary: Primary S. cerevisiae experiments verify Shs1 bud-neck localization and
    distinguish septin ring assembly from recruitment of cytokinesis factors. Shs1
    deletion can leave Cdc3/Cdc10/Cdc11/Cdc12 rings assembled while Iqg1/Myo1/Cyk3
    localization and cytokinesis are impaired; requirement depends on background and
    conditions.
  snapshot_sha256: 04a4d06dd95fbe340813d6fb87e5ba9fc376722b5d746b396ad56a0a73aa155d
- evidence_id: septin-ring-agent-bertin2008-xml
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2426963/?report=xml
  locator: PMC2426963 Results sec2–6, especially sec2 and sec4/Figures1 and4 legends;
    exact DOI10.1073/pnas.0803330105
  accessed_at: '2026-10-21T08:12:10.171029Z'
  support: supports
  summary: Purified recombinant Cdc3/Cdc10/Cdc11/Cdc12 complexes form nonpolar octameric
    rods; lowering salt yields end-to-end paired filaments. The direct reconstitution
    establishes a four-paralog core with two copies each, not simultaneous incorporation
    of all five listed mitotic paralogs. Shs1 replacement was a proposal in this paper.
  snapshot_sha256: a0a9edefa289d439e0491c1e79986bf5404d8bc2b75c75010ebd53a0a2418a2d
- evidence_id: septin-ring-agent-mcmurray2011-xml
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3079881/?report=xml
  locator: PMC3079881 Results S7/S9/S10 with Figures3,5,6 captions and Discussion
    S11; DOI10.1016/j.devcel.2011.02.004
  accessed_at: '2026-10-21T08:12:10.154983Z'
  support: supports
  summary: Primary interface-mutant and microscopy experiments connect filament polymerization
    to cortical organization and viability in the tested yeast conditions. Cdc10-
    or Cdc11-deficient cells can survive via alternative hexameric assemblies, so
    neither individual necessity nor one oligomer size is universal.
  snapshot_sha256: 86542d24c79bdba161e9cabd56715f8b0f9831083c3b9296f235d39bc467e4c5
- evidence_id: septin-ring-agent-glomb2016-xml
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5093138/?report=xml
  locator: PMC5093138 main text paragraphs beginning The classical Hartwell screen
    / The mitotic yeast / Septin octamers containing Shs1 / In the living yeast cell
    / After bud formation / Taken together; Figure2 legend; review tier
  accessed_at: '2026-10-21T08:12:09.597497Z'
  support: supports
  summary: Review synthesis supports the five mitotic septins, bud-site recruitment,
    ring-to-collar/split-ring transitions and scaffold functions. It explicitly distinguishes
    Cdc11-capped rods that assemble end-to-end from Shs1-capped rods that preferentially
    form curved/lateral assemblies.
  snapshot_sha256: 73f8135ddd5beb0a4f937757190372a5a881bc331a34a9e837b6c1264f0c35d8
- evidence_id: septin-ring-agent-bridges2014-xml
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4266239/?report=xml
  locator: PMC4266239 S1–S3 and Figure1 textual legend; review tier, DOI10.1016/j.mib.2014.04.004
  accessed_at: '2026-10-21T08:12:09.598368Z'
  support: supports
  summary: Review of fungal pathogens supports septin scaffolding at division sites
    and species-specific higher-order localization, including bud-neck and hyphal
    septation contexts. It cautions that many mechanistic explanations remain unresolved
    and mutant phenotypes can be indirect.
  snapshot_sha256: b0f438b55aa22ae032544d66478a51780ad4b6e7e1e5575fb644e80b4eb6d197
- evidence_id: septin-ring-agent-vargas2016-xml
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5068138/?report=xml
  locator: PMC5068138 s1-3, s1-5 and s1-6, Figure1 textual legend; review tier, DOI10.1099/mic.0.000359
  accessed_at: '2026-10-21T08:12:09.597924Z'
  support: supports
  summary: Review supports broad fungal septin occurrence and functions in morphology,
    septation and development, while distinguishing species-dependent rod composition
    and Shs1-dependent assembly. Septin deletion often reduces rather than abolishes
    septation.
  snapshot_sha256: 69ae7a9c9cac3c98cbcbdf8860f1a82d0ee379e3de487290abd11346af60aace
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/septin_ring.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:08:55Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/septin_ring.yaml'
  snapshot_sha256: 52fc299b8e2d93d735e83581c882f4e5e1b9074de217ac1de796d234edbcf892
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/septin_ring.yaml --out
    /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_ring-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:09:02Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/septin_ring.yaml\
    \ --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_ring-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../septin_ring-strict.tsv"
  snapshot_sha256: 35d30ca3e5a83cc14ff030ffe05a05a0b21f863fce483c760df58182d15d6975
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/septin_ring.yaml; exact collect() scope; hash
    identifies the complete original /private/tmp/cellstructure-record-reviews-UhRFh7/repo/reports/curie_check.tsv,
    not the derived target slice
  accessed_at: '2026-10-21T08:17:23Z'
  support: supports
  summary: '18 of 21 collected target identifiers returned OK at the unchanged base.
    Residuals: PMID:14562095: UNREACHABLE; resolved by evidence septin-ring-agent-paper-metadata;
    PMID:25971666: UNREACHABLE; resolved by evidence septin-ring-agent-paper-metadata;
    PMID:9790978: UNREACHABLE; resolved by evidence septin-ring-agent-paper-metadata.
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
  topic: Higher-order cortical ring versus smaller septin complexes
  outcome: supported
  target_ids:
  - GO:0005940
  summary: GO0005940 matches the defined higher-order ring, its septin-cytoskeleton
    parent and cell-cortex parthood. GO0031105 is a smaller oligomeric complex, appropriately
    retained as a distinct assembly level. The microbial record uses fungal examples
    without claiming that the GO class excludes animal rings.
  evidence_ids:
  - septin-ring-agent-go
  - septin-ring-agent-iwase2007-xml
  - septin-ring-agent-glomb2016-xml
  - record
- assessment_id: composition
  area: grounding
  topic: Five identity examples and mitotic structural cohort
  outcome: supported
  target_ids:
  - GO:0005940
  summary: All sequence identities, primary symbols, reviewed statuses, S288C taxon
    labels and uniqueness checks pass. Primary and review evidence supports the five
    mitotic bud-neck septins. General membrane/bud-neck annotations are not silently
    promoted to a different localization. Collective ESSENTIAL is not a claim that
    each paralog is individually necessary for every ring.
  evidence_ids:
  - septin-ring-agent-iwase2007-xml
  - septin-ring-agent-glomb2016-xml
  - septin-ring-agent-P32457
  - septin-ring-agent-symbol-CDC3
  - septin-ring-agent-P25342
  - septin-ring-agent-symbol-CDC10
  - septin-ring-agent-P32458
  - septin-ring-agent-symbol-CDC11
  - septin-ring-agent-P32468
  - septin-ring-agent-symbol-CDC12
  - septin-ring-agent-Q07657
  - septin-ring-agent-symbol-SHS1
  - record
  - policy
  - example-policy
- assessment_id: scope
  area: scope
  topic: Fungal occurrence and Saccharomyces model
  outcome: supported
  target_ids:
  - GO:0005940
  summary: Native Fungi/species/strain identities agree. COMMON is a qualitative fungal
    occurrence statement with explicit variation by lineage and morphogenetic context,
    not universal occurrence, numerical prevalence or universal essentiality. The
    named Saccharomyces example is supported by Iwase; tested backgrounds are not
    equated to every S288C-derived strain.
  evidence_ids:
  - septin-ring-agent-iwase2007-xml
  - septin-ring-agent-bridges2014-xml
  - septin-ring-agent-vargas2016-xml
  - septin-ring-agent-taxon-4932
  - septin-ring-agent-taxon-559292
  - septin-ring-agent-taxon-4751
  - record
- assessment_id: function
  area: evidence
  topic: Division-site scaffold and cytokinesis factors
  outcome: supported
  target_ids:
  - GO:0005940
  summary: Budding-yeast recruitment and cytokinesis-site organization have direct
    experimental support, while broader fungal scaffolding rests on reviews. The record
    does not claim direct binding for every cytokinesis factor or that septins generate
    constriction force or determine every fungal cleavage plane.
  evidence_ids:
  - septin-ring-agent-iwase2007-xml
  - septin-ring-agent-glomb2016-xml
  - septin-ring-agent-bridges2014-xml
  - septin-ring-agent-vargas2016-xml
  - record
- assessment_id: graph
  area: graph
  topic: Scoped oligomer-to-filament-to-ring hierarchy
  outcome: supported
  target_ids:
  - GO:0005940
  summary: The NONMECHANISTIC graph is explicitly a Saccharomyces assembly hierarchy,
    supported by the reconstituted Cdc11-capped core and budding-cell localization.
    It does not specify all five paralogs in one octamer or a universal fungal rod
    order. Shs1-capped rods and viable alternative hexamers limit universal reading
    of the generic rod-to-filament edge; these documented exceptions are retained
    in this assessment.
  evidence_ids:
  - septin-ring-agent-bertin2008-xml
  - septin-ring-agent-mcmurray2011-xml
  - septin-ring-agent-glomb2016-xml
  - septin-ring-agent-vargas2016-xml
  - septin-ring-agent-go
  - record
- assessment_id: family
  area: grounding
  topic: Generic Septin family versus localized cohort
  outcome: concern
  target_ids:
  - GO:0005940
  summary: The component is named septin proteins but its rationale withholds grounding
    until a family denotes the complete assembly-forming cohort. IPR016491 supplies
    the generic family identity; localized composition remains a separate scientific
    question.
  evidence_ids:
  - septin-ring-agent-family
  - record
  - policy
- assessment_id: provenance
  area: provenance
  topic: Primary experiments versus literature reviews
  outcome: supported
  target_ids:
  - GO:0005940
  summary: Iwase/Bertin/McMurray are primary experiments, while Glomb/Bridges/Vargas
    are explicit review-tier authorities. The exact cited paper identities and native
    UniProt localization citations match. Generic PMC routes initially returned challenges,
    but report=xml routes delivered genuine readable HTML; no challenged response
    is used as body evidence.
  evidence_ids:
  - septin-ring-agent-paper-metadata
  - septin-ring-agent-iwase2007-xml
  - septin-ring-agent-bertin2008-xml
  - septin-ring-agent-mcmurray2011-xml
  - septin-ring-agent-glomb2016-xml
  - septin-ring-agent-bridges2014-xml
  - septin-ring-agent-vargas2016-xml
  - septin-ring-agent-P32457
  - septin-ring-agent-symbol-CDC3
  - septin-ring-agent-P25342
  - septin-ring-agent-symbol-CDC10
  - septin-ring-agent-P32458
  - septin-ring-agent-symbol-CDC11
  - septin-ring-agent-P32468
  - septin-ring-agent-symbol-CDC12
  - septin-ring-agent-Q07657
  - septin-ring-agent-symbol-SHS1
- assessment_id: completeness
  area: completeness
  topic: Optional detailed composition and mechanism
  outcome: supported
  target_ids:
  - GO:0005940
  summary: No exhaustive accessory-protein list, molecular dimensions, image license
    or full ordered recruitment mechanism is asserted. Optional unresolved details
    and distinct localized ring subtypes do not create additional findings.
  evidence_ids:
  - septin-ring-agent-go
  - septin-ring-agent-iwase2007-xml
  - septin-ring-agent-bertin2008-xml
  - record
findings:
- finding_id: F1
  issue_key: septin-ring-generic-family-withheld
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
  - GO:0005940
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions
  evidence_ids:
  - septin-ring-agent-family
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: A bounded generic-family mapping gap; exact structure identity
    and species-specific composition are separate.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005940
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_ring.yaml
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
limitations:
- The rod-to-filament model is the representative Cdc11-capped Saccharomyces core.
  Shs1-capped assemblies and mutant hexamers differ; no all-five-in-one-octamer or
  universal fungal architecture is inferred.
- Primary text and selected figure legends were read; all microscopy pixels, raw datasets
  and supplementary experiments were not independently reanalyzed.
- The fungal distribution and cross-species scaffold generalization use review-tier
  synthesis. Quantitative fungal prevalence and universal division-plane determination
  are not established.
- Huh2003 and Mino1998 remain abstract/metadata and native-UniProt-attribution bounded.
  Those notes verify imported annotation scope, not every original experimental detail.
- Collective essential septin material is distinct from individual paralog or organismal
  viability requirements; a complete associated-protein inventory remains optional.
- Historical issue dispositions and unread-source claims are not revalidated; no prior
  finding is formally closed and no new absence claim is made.
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
