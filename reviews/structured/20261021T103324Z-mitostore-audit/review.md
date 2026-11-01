# MitoStore assembly, recovery and mitochondrial boundary review

- Review: 20261021T103324Z-mitostore-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:13:26Z
- Finished UTC: 2026-10-21T10:33:24Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The MitoStore identity, conditional assembly/recovery claims, reference proteins, family boundaries and Figure5 provenance are supported. No corrective issue was established; assay, inventory and repository-metadata limits remain explicit.

## Scope And Provenance

Entire single target and stated boundary context; native identities/family candidates, defining-study Results/Discussion and named Methods, limited comparison-paper passages, deposited-project metadata and full maintained image.

Selection: Seventh selected target in batch nineteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:mitostore | data/structures/inclusion/mitostore.yaml | maintained | MitoStore |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native UniProt verify | passed | False | cellstructuremech:mitostore | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | cellstructuremech:mitostore | Native command passed; scientific membership and graph scope assessed independently. |
| Focused native schema | passed | True | cellstructuremech:mitostore | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:mitostore | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:mitostore | 10 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | cellstructuremech:mitostore | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:mitostore | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:mitostore | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:mitostore | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:mitostore | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:mitostore | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Cytosolic deposit distinct from mitochondrial compartments

identity: supported. Targets: cellstructuremech:mitostore.

The local MitoStore identity and cytoplasmic inclusion hierarchy agree with the defining study. Surface association and a mitochondrial precursor bias do not relocate the deposit into the mitochondrial matrix or make it a membrane-enclosed mitochondrial-derived compartment. JUNQ/IPOD distinctions and the bounded exact-name search are preserved.

### Heterogeneous cargo and precise chaperone classes

grounding: supported. Targets: cellstructuremech:mitostore.

The cargo is a nonhomologous cohort and does not require a single family identifier. IPR031107 correctly grounds the small-HSP class, while the two domain/superfamily alternatives do not replace it. Hsp104-only grounding is appropriately withheld from the inspected broader Clp families. All three concrete reference proteins and gene/taxon pairings resolve; native identity is separate from inclusion association.

### Formation tests are component- and assay-specific

evidence: supported. Targets: cellstructuremech:mitostore.

CONDITIONAL Hsp104 and small-HSP necessity is supported only for the tested formation assays. In particular, Hsp42 has direct deletion evidence while Hsp26 is a co-eluting candidate; the maintained notes explicitly retain that distinction. Presequence dependence of the Mam33 reporter does not establish every cargo molecule as necessary for granule formation.

### Individual cargo and Hsp26 formation requirements

evidence: unknown. Targets: cellstructuremech:mitostore.

No inspected experiment establishes a requirement for every heterogeneous cargo class or for Hsp26 in MitoStore formation. The collective stored material is definitional, while a reporter recruitment sequence and Hsp26 co-elution do not establish universal assembly necessity. This unresolved scope is separate from the direct Hsp104/Hsp42 conditional formation tests.

### Study conditions, reference taxa and proteomics metadata

scope: supported. Targets: cellstructuremech:mitostore.

Taxonomy receipts establish their own species/strain identities. The record distinguishes the primary YPH499-derived experiments from S288C protein-reference entries and does not infer population prevalence. PRIDE metadata is cited with its unresolved linked-reference discrepancy; the deposited files were not used to invent a complete inventory.

### Storage, import competence and conditional protection

evidence: supported. Targets: cellstructuremech:mitostore.

The functions retain precursor bias and the defining import-stress context. Split-GFP recovery supports import competence after the chase but does not track each granule molecule into mitochondria. Survival effects in rpn4-deficient import stress are not generalized to all proteotoxic stress or attributed solely to granule architecture.

### Assembly and recovery transitions have direct experimental bounds

graph: supported. Targets: cellstructuremech:mitostore.

Both MECHANISTIC graphs represent tested perturbations and transitions, not merely parthood. They preserve presequence recruitment, Hsp104/Hsp42-dependent reporter granules, accessible mitochondrial-surface material, reporter recovery and conditional viability. Hsp26, Tom70 and a hypothetical physical tether are not promoted to obligatory machinery.

### Exact Figure5 media and license

evidence: supported. Targets: cellstructuremech:mitostore.

Local SHA-256 and native MD5 agree for the fully inspected image. The figure caption preserves multiple assays, scale bars and knockout context; native media numbering is correctly resolved against the actual source caption and explicit CC BY4.0 permissions.

### Open molecular census is a limitation

completeness: supported. Targets: cellstructuremech:mitostore.

No corrective issue was established. The unknown tether, nonexhaustive precursor inventory, Hsp26 assembly uncertainty and distinction from the other Tom70-associated assemblies remain explicit. No phase-separation mechanism or universal cellular frequency is inferred. PROPOSED status and historical discussion remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/inclusion/mitostore.yaml; Entire maintained YAML including definition, components, functions, hierarchy, examples, graph edges, discussions, image metadata and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| mitostore-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005737,GO:0016234; Complete native definitions and relevant relationships | supports | GO0005737 cytoplasm and GO0016234 inclusion body match the maintained placement. Neither authority identifies MitoStores as intramitochondrial material or a membrane-enclosed mitochondrial-derived compartment. |
| mitostore-agent-local-ids | rg --no-ignore --hidden --files data/structures -g *.yaml; Exact top-level identifier comparison after parsing all 978 ignored- and hidden-inclusive maintained YAML records | supports | Each selected target and boundary-neighbor identifier resolves to exactly one maintained record in the frozen corpus. This verifies repository-local identity, not an external ontology equivalence or scientific membership. |
| mitostore-agent-ols-exact-0 | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=MitoStore; OLS native search response numFound and complete docs list; exact query is preserved in reference URL | context_only | This exact-name GO search returned zero results. The result bounds only the stated query; it is not an exhaustive synonym search or proof that no ontology representation exists. |
| mitostore-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Saccharomyces cerevisiae, species. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| mitostore-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Native ENA taxonomy identifies Saccharomyces cerevisiae S288C, strain. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| mitostore-agent-P31539 | https://rest.uniprot.org/uniprotkb/P31539.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P31539 identifies Heat shock protein 104, gene HSP104, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| mitostore-agent-query-HSP104 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AHSP104%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene HSP104, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P31539. This checks identifier resolution only. |
| mitostore-agent-Q12329 | https://rest.uniprot.org/uniprotkb/Q12329.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB Q12329 identifies Heat shock protein 42, gene HSP42, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| mitostore-agent-query-HSP42 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AHSP42%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene HSP42, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns Q12329. This checks identifier resolution only. |
| mitostore-agent-P15992 | https://rest.uniprot.org/uniprotkb/P15992.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P15992 identifies Heat shock protein 26, gene HSP26, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| mitostore-agent-query-HSP26 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AHSP26%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene HSP26, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P15992. This checks identifier resolution only. |
| mitostore-agent-matches-P31539 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| mitostore-agent-matches-Q12329 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12329/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| mitostore-agent-matches-P15992 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P15992/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| mitostore-agent-IPR031107 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031107/; Native InterPro metadata name/type, description and membership scope; predictive description provenance retained where marked | supports | Small heat shock protein is a family entry covering the two concrete small-HSP examples. This grounds a class without making every small HSP a MitoStore constituent. |
| mitostore-agent-IPR002068 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002068/; Native InterPro metadata name/type, description and membership scope; predictive description provenance retained where marked | supports | The HSP20-like chaperone entry is a domain, not a replacement for the exact maintained small-heat-shock-protein family class. |
| mitostore-agent-IPR008978 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008978/; Native InterPro metadata name/type, description and membership scope; predictive description provenance retained where marked | supports | The HSP20-like entry is a homologous superfamily, not a narrower family identity. |
| mitostore-agent-IPR001270 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/; Native InterPro metadata name/type, description and membership scope; predictive description provenance retained where marked | supports | ClpA/B spans Hsp104 and several broader Clp classes; it is not exact Hsp104-specific equivalence. |
| mitostore-agent-IPR050130 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/; Native InterPro metadata name/type, description and membership scope; predictive description provenance retained where marked | supports | ClpA/ClpB chaperone/protease-related grouping is broader than the Hsp104-specific component; predictive description text is not experimental assembly evidence. |
| mitostore-agent-doi-10.15252_embj.2022112309 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.15252/embj.2022112309; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies MitoStores: chaperone-controlled protein granules store mitochondrial precursors in the cytosol. Authors: Krämer L, Dalheimer N, Räschle M, Storchová Z, Pielage J, Boos F, Herrmann JM.; PMID 36704946; DOI 10.15252/embj.2022112309. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| mitostore-agent-doi-10.1073_pnas.2300475120 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.2300475120; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Nascent mitochondrial proteins initiate the localized condensation of cytosolic protein aggregates on the mitochondrial surface. Authors: Liu Q, Fong B, Yoo S, Unruh JR, Guo F, Yu Z, Chen J, Si K, Li R, Zhou C.; PMID 37494397; DOI 10.1073/pnas.2300475120. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| mitostore-agent-jats-PMC10068336 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10068336.1/PMC10068336.1.xml; Complete Results secs0003-0008 and Discussion0009; Methods0011 growth/strains,0012 viability,0016 mitochondrial isolation,0017-0018 mass-spectrometry sample preparation/analysis; Figures5-6 captions. Other supplementary pixels/raw proteomics not independently audited. | supports | Krämer2023 directly identifies cytosolic granules enriched for mitochondrial preproteins under import stress. Hsp104 and Hsp42 single deletions prevent the tested Aim17 granule phenotype; Hsp26 co-elution is weaker association evidence. Presequence reporter manipulation, protease-accessible surface-associated material, split-GFP import competence and conditional survival experiments support distinct represented steps. Neither the recovery assay nor survival experiment isolates a universal granule-only protective mechanism. Methods identify a YPH499-derived default strain; S288C accessions remain reference identities. JATS permissions specify CC BY4.0. |
| mitostore-agent-jats-PMC10401023 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10401023.1/PMC10401023.1.xml; Abstract, final Introduction paragraph, Results s2 opening Tom70 deletion/overexpression and nascent-protein/FCS paragraphs, and Discussion s7 MitoStore comparison only. Remaining study sections not comprehensively audited. | supports | Liu2023 supplies a distinct Tom70/proteostasis context. The inspected experiments and Discussion describe partial Tom70 dependence and overlapping features with MitoStores, not demonstrated exact equivalence or a fixed Tom70 structural constituent. |
| mitostore-agent-PXD035762 | https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD035762; Native project title, projectDescription, dataProcessingProtocol, organisms and references; no raw spectra or deposited quantitative files reanalysed | supports | The PRIDE project title and description concern MitoStore/Hsp104 affinity proteomics, but its linked reference is the different Ubc8 paper DOI10.26508/LSA.202201526. Project-wide protein counts and the paper-specific affinity-purification cohort are not interchangeable. The target already retains this metadata discrepancy. |
| mitostore-agent-image | data/images/inclusion/mitostore/pmc10068336_embj2022112309_fig_0005.jpg; Entire maintained figure and every panel visually inspected, including genotype/species labels, scale bars, blots/plots or schematic; source caption and license read separately. | supports | All panelsA-D of the maintained Figure5 were visually read, including tested Hsp104/Hsp42 deletion strains and distinct panel scale bars. Native package filename EMBJ-42-e112309-g007.jpg corresponds to source Figure5 because supplementary figures are interleaved; it does not indicate a figure-number mismatch. No third-party figure credit overrides the article license. Local SHA-256 matches the record, and local MD5 d5aed1d2f71065dd88d6dc617a55f368 matches the exact native PMC media entry. |
| mitostore-agent-native-package-PMC10068336 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10068336.1/PMC10068336.1.json; Article/package identity, license code and exact media_urls match | supports | The native PMC package identifies the article and matching media filename/MD5. The explicit CC BY4.0 license is read in the separately cited JATS permissions, rather than inferred from package shorthand. |
| boundary-0 | data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | These maintained fields were read to verify the stated identity boundary. This is contextual corpus evidence, not an independent full scientific review of the neighboring record. |
| boundary-1 | data/structures/inclusion/insoluble_protein_deposit.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | These maintained fields were read to verify the stated identity boundary. This is contextual corpus evidence, not an independent full scientific review of the neighboring record. |
| boundary-2 | data/structures/membrane_organelle/intramitochondrial_protein_quality_control_compartment.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | These maintained fields were read to verify the stated identity boundary. This is contextual corpus evidence, not an independent full scientific review of the neighboring record. |
| boundary-3 | data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | These maintained fields were read to verify the stated identity boundary. This is contextual corpus evidence, not an independent full scientific review of the neighboring record. |
| native-verify | /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml --causal-graphs; Captured focused native causal-graphs log | supports | data/structures/inclusion/mitostore.yaml  (cellstructuremech:mitostore)<br>  precursor_granule_assembly	cargo	NO_GENE_SYMBOLS	-&gt;precursor_cargo (OTHER: presequence-enriched protein precursor cargo)<br>  precursor_recovery_and_tolerance	cargo	NO_GENE_SYMBOLS	-&gt;precursor_cargo (OTHER: presequence-enriched protein precursor cargo)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/inclusion/mitostore.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/inclusion/mitostore.yaml |
| strict-result | just validate-strict data/structures/inclusion/mitostore.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/mitostore-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/inclusion/mitostore.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/mitostore-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/mitostore-strict.tsv |
| target-curies | just check-curies-strict; data/structures/inclusion/mitostore.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 10 of11 collected target identifiers returned OK in this fresh base resolver run. Residuals: cellstructuremech:mitostore: SKIPPED; resolved by evidence mitostore-agent-local-ids. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Only the named Krämer Results/Discussion/Methods and Figures5-6 captions, plus complete maintained Figure5 pixels, were audited. Raw mass-spectrometry files, all extended figures and numerical image datasets were not reanalysed.
- Liu2023 is used only at the explicitly named Tom70/proteostasis and comparison passages; the entire paper was not reviewed and distinct stress assemblies are not treated as exact synonyms.
- Split-GFP recovery and viability assays do not establish direct tracking of every stored molecule or isolate a universal granule-only protective effect. Hsp26 association is not evidence of formation necessity.
- The native PRIDE linked-reference discrepancy is unresolved; project-wide and paper-specific protein counts are not equated. Exact GO and family checks are bounded to the recorded queries and reviewed examples. Boundary neighbors were inspected at contextual fields only.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The authorized coverage task includes honest clean reviews.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103324Z-mitostore-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: MitoStore assembly, recovery and mitochondrial boundary review
started_at: '2026-10-21T10:13:26Z'
finished_at: '2026-10-21T10:33:24Z'
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
summary: The MitoStore identity, conditional assembly/recovery claims, reference proteins,
  family boundaries and Figure5 provenance are supported. No corrective issue was
  established; assay, inventory and repository-metadata limits remain explicit.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/images/inclusion/mitostore/pmc10068336_embj2022112309_fig_0005.jpg
    sha256: 08fe6da4832a3b949f031e367ee32323e88d73b83fece71cfd4ec02fd03e35d0
    role: context
  - path: data/structures/inclusion/insoluble_protein_deposit.yaml
    sha256: 45a74ced04c8c5714cd45f6a8a04c45ae8a5af22a04809aa51520c54884fb773
    role: context
  - path: data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
    sha256: c3fbd426fe95ef931039579f467743997b83a889fa00c53442b36f46ccd95545
    role: context
  - path: data/structures/inclusion/mitostore.yaml
    sha256: 6863a577037a5f308979f0c7cdcccda5b49ebe7f64586192cef53ca27291347a
    role: target
  - path: data/structures/membrane_organelle/intramitochondrial_protein_quality_control_compartment.yaml
    sha256: cc6a473ee1312f0604f6eb51a1b3bddf9cf02122523ee9b4ad2009651053d037
    role: context
  - path: data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
    sha256: 650d06fba3733f228b8a47fc38412ea5107fe8ee81592c2871d1a899dcbed407
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
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: cellstructuremech:mitostore
  path: data/structures/inclusion/mitostore.yaml
  label: MitoStore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/mitostore.yaml
    role: maintained scientific record
scope:
  description: Entire single target and stated boundary context; native identities/family
    candidates, defining-study Results/Discussion and named Methods, limited comparison-paper
    passages, deposited-project metadata and full maintained image.
  selection: Seventh selected target in batch nineteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:mitostore
checks:
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - cellstructuremech:mitostore
  command: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml --verify
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native UniProt causal-graphs
  status: passed
  required: false
  target_ids:
  - cellstructuremech:mitostore
  command: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml --causal-graphs
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitostore
  command: just validate data/structures/inclusion/mitostore.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitostore
  command: just validate-strict data/structures/inclusion/mitostore.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/mitostore-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitostore
  summary: 10 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - mitostore-agent-local-ids
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitostore
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - mitostore-agent-go
  - mitostore-agent-local-ids
  - mitostore-agent-ols-exact-0
  - mitostore-agent-tax-4932
  - mitostore-agent-tax-559292
  - mitostore-agent-P31539
  - mitostore-agent-query-HSP104
  - mitostore-agent-Q12329
  - mitostore-agent-query-HSP42
  - mitostore-agent-P15992
  - mitostore-agent-query-HSP26
  - mitostore-agent-matches-P31539
  - mitostore-agent-matches-Q12329
  - mitostore-agent-matches-P15992
  - mitostore-agent-IPR031107
  - mitostore-agent-IPR002068
  - mitostore-agent-IPR008978
  - mitostore-agent-IPR001270
  - mitostore-agent-IPR050130
  - mitostore-agent-doi-10.15252_embj.2022112309
  - mitostore-agent-doi-10.1073_pnas.2300475120
  - mitostore-agent-jats-PMC10068336
  - mitostore-agent-jats-PMC10401023
  - mitostore-agent-PXD035762
  - mitostore-agent-image
  - mitostore-agent-native-package-PMC10068336
  - boundary-0
  - boundary-1
  - boundary-2
  - boundary-3
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitostore
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
  - cellstructuremech:mitostore
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
  - cellstructuremech:mitostore
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
  - cellstructuremech:mitostore
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
  - cellstructuremech:mitostore
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
- evidence_id: record
  kind: record_content
  reference: data/structures/inclusion/mitostore.yaml
  locator: Entire maintained YAML including definition, components, functions, hierarchy,
    examples, graph edges, discussions, image metadata and history
  accessed_at: '2026-10-21T10:31:36Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T10:31:36Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: mitostore-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005737,GO:0016234
  locator: Complete native definitions and relevant relationships
  accessed_at: '2026-10-21T10:17:14.220895Z'
  support: supports
  summary: GO0005737 cytoplasm and GO0016234 inclusion body match the maintained placement.
    Neither authority identifies MitoStores as intramitochondrial material or a membrane-enclosed
    mitochondrial-derived compartment.
  snapshot_sha256: 94c9a43328badeef75d174318ba7a648cba7cfe99eb407fa0b30879f5d18dddb
- evidence_id: mitostore-agent-local-ids
  kind: search
  reference: rg --no-ignore --hidden --files data/structures -g *.yaml
  locator: Exact top-level identifier comparison after parsing all 978 ignored- and
    hidden-inclusive maintained YAML records
  accessed_at: '2026-10-21T10:24:20.020977Z'
  support: supports
  summary: Each selected target and boundary-neighbor identifier resolves to exactly
    one maintained record in the frozen corpus. This verifies repository-local identity,
    not an external ontology equivalence or scientific membership.
  snapshot_sha256: 297c8bc97976a06a3825d81b1a063033f3d749049e0ace05dbd16d551a028b7a
  search_scope: Ignored- and hidden-inclusive maintained data/structures YAML universe;
    parse every top-level identifier, compare exact selected identifiers. No absence
    or broad ontology-uniqueness claim.
- evidence_id: mitostore-agent-ols-exact-0
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=MitoStore
  locator: OLS native search response numFound and complete docs list; exact query
    is preserved in reference URL
  accessed_at: '2026-10-21T10:25:00.362168Z'
  support: context_only
  summary: This exact-name GO search returned zero results. The result bounds only
    the stated query; it is not an exhaustive synonym search or proof that no ontology
    representation exists.
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  search_scope: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=MitoStore
- evidence_id: mitostore-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:17:14.328921Z'
  support: supports
  summary: Native ENA taxonomy identifies Saccharomyces cerevisiae, species. This
    receipt attests that identity and rank only, not occurrence or the experimental
    strain.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: mitostore-agent-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:17:14.351153Z'
  support: supports
  summary: Native ENA taxonomy identifies Saccharomyces cerevisiae S288C, strain.
    This receipt attests that identity and rank only, not occurrence or the experimental
    strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: mitostore-agent-P31539
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P31539.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T10:17:16.337306Z'
  support: supports
  summary: Native reviewed UniProtKB P31539 identifies Heat shock protein 104, gene
    HSP104, taxon559292. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 8636decea760cdb2a2da238bfa589822867a778a41fd6a04c45a74fe5802ee13
- evidence_id: mitostore-agent-query-HSP104
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AHSP104%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene HSP104, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T10:17:17.396643Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P31539. This checks identifier
    resolution only.
  snapshot_sha256: 4e2938a5a1292a9626b18e30b225ebfc7a30d63069235f01cd0bc3d007279322
  search_scope: UniProtKB query gene_exact:HSP104 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: mitostore-agent-Q12329
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12329.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T10:17:16.368633Z'
  support: supports
  summary: Native reviewed UniProtKB Q12329 identifies Heat shock protein 42, gene
    HSP42, taxon559292. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 2fd80fe65790b403d51e6d01659e4c94ec91a1455e5b4be00301e2350656a1cc
- evidence_id: mitostore-agent-query-HSP42
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AHSP42%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene HSP42, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T10:17:17.014725Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns Q12329. This checks identifier
    resolution only.
  snapshot_sha256: f293170bb43d8482c94e6ef06e0447afe7d1dcb10ffa734d42c94920324e5ae4
  search_scope: UniProtKB query gene_exact:HSP42 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: mitostore-agent-P15992
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P15992.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T10:17:16.161560Z'
  support: supports
  summary: Native reviewed UniProtKB P15992 identifies Heat shock protein 26, gene
    HSP26, taxon559292. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: cbaa80ed16718c9eb01d31f4ae461fe665e1390d99bccaee7d6a277c4352b523
- evidence_id: mitostore-agent-query-HSP26
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AHSP26%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene HSP26, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T10:17:17.079954Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P15992. This checks identifier
    resolution only.
  snapshot_sha256: 62a0910bbcb49e0d05afd2960add90e935340ecc9909ff5d559a12353efc6d53
  search_scope: UniProtKB query gene_exact:HSP26 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: mitostore-agent-matches-P31539
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T10:17:16.354169Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: 750867aa538d4dd5c6c6a982138e7401b8b788d9653ecb84bf5d145c8ff6d3ee
- evidence_id: mitostore-agent-matches-Q12329
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12329/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T10:17:16.781670Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: b5fd5350c5ea8e5ac5d6bdda8ab01a8f4ab0036d09974a5a02fce9361203a6a2
- evidence_id: mitostore-agent-matches-P15992
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P15992/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T10:17:16.325637Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: 2a832a0014d7563f99c26af41dd62810eda86625e204d5e0bed963bcec7b6d04
- evidence_id: mitostore-agent-IPR031107
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031107/
  locator: Native InterPro metadata name/type, description and membership scope; predictive
    description provenance retained where marked
  accessed_at: '2026-10-21T10:17:14.956698Z'
  support: supports
  summary: Small heat shock protein is a family entry covering the two concrete small-HSP
    examples. This grounds a class without making every small HSP a MitoStore constituent.
  snapshot_sha256: 7db6f5da4dd897dfbcaa6435cbeb744a4691f43cb10433977995a30bb1d91293
- evidence_id: mitostore-agent-IPR002068
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002068/
  locator: Native InterPro metadata name/type, description and membership scope; predictive
    description provenance retained where marked
  accessed_at: '2026-10-21T10:17:14.829387Z'
  support: supports
  summary: The HSP20-like chaperone entry is a domain, not a replacement for the exact
    maintained small-heat-shock-protein family class.
  snapshot_sha256: 729375e0c4a4deaf090825f659ab2273b13f15eac1bee4b1fb133ce4006ab3d7
- evidence_id: mitostore-agent-IPR008978
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008978/
  locator: Native InterPro metadata name/type, description and membership scope; predictive
    description provenance retained where marked
  accessed_at: '2026-10-21T10:17:14.947052Z'
  support: supports
  summary: The HSP20-like entry is a homologous superfamily, not a narrower family
    identity.
  snapshot_sha256: ba6677dcb173c00f37d8ccc3cabc05df5e0969bcd1794b428fcfe76141188049
- evidence_id: mitostore-agent-IPR001270
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/
  locator: Native InterPro metadata name/type, description and membership scope; predictive
    description provenance retained where marked
  accessed_at: '2026-10-21T10:17:14.627551Z'
  support: supports
  summary: ClpA/B spans Hsp104 and several broader Clp classes; it is not exact Hsp104-specific
    equivalence.
  snapshot_sha256: ed0a09c17fa611e58cd0d00b904d4dce2757228cd7e411301eddcfb9b391e0dd
- evidence_id: mitostore-agent-IPR050130
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/
  locator: Native InterPro metadata name/type, description and membership scope; predictive
    description provenance retained where marked
  accessed_at: '2026-10-21T10:17:15.335733Z'
  support: supports
  summary: ClpA/ClpB chaperone/protease-related grouping is broader than the Hsp104-specific
    component; predictive description text is not experimental assembly evidence.
  snapshot_sha256: e654bc8d2d359d203a225be0690247071616a63341156fcd507f197717f78701
- evidence_id: mitostore-agent-doi-10.15252_embj.2022112309
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.15252/embj.2022112309
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:17:17.774562Z'
  support: supports
  summary: 'Native metadata identifies MitoStores: chaperone-controlled protein granules
    store mitochondrial precursors in the cytosol. Authors: Krämer L, Dalheimer N,
    Räschle M, Storchová Z, Pielage J, Boos F, Herrmann JM.; PMID 36704946; DOI 10.15252/embj.2022112309.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: c2c0961593c368c204aec91ef0bc9ef79c8082edeeab66932d09e779cf7038aa
- evidence_id: mitostore-agent-doi-10.1073_pnas.2300475120
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.2300475120
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T10:17:17.413296Z'
  support: supports
  summary: 'Native metadata identifies Nascent mitochondrial proteins initiate the
    localized condensation of cytosolic protein aggregates on the mitochondrial surface.
    Authors: Liu Q, Fong B, Yoo S, Unruh JR, Guo F, Yu Z, Chen J, Si K, Li R, Zhou
    C.; PMID 37494397; DOI 10.1073/pnas.2300475120. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 16eda6c568410191f9f4404ac22619a8e631e657df0f8eba866222e3edef12b9
- evidence_id: mitostore-agent-jats-PMC10068336
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10068336.1/PMC10068336.1.xml
  locator: Complete Results secs0003-0008 and Discussion0009; Methods0011 growth/strains,0012
    viability,0016 mitochondrial isolation,0017-0018 mass-spectrometry sample preparation/analysis;
    Figures5-6 captions. Other supplementary pixels/raw proteomics not independently
    audited.
  accessed_at: '2026-10-21T10:17:53.514442Z'
  support: supports
  summary: Krämer2023 directly identifies cytosolic granules enriched for mitochondrial
    preproteins under import stress. Hsp104 and Hsp42 single deletions prevent the
    tested Aim17 granule phenotype; Hsp26 co-elution is weaker association evidence.
    Presequence reporter manipulation, protease-accessible surface-associated material,
    split-GFP import competence and conditional survival experiments support distinct
    represented steps. Neither the recovery assay nor survival experiment isolates
    a universal granule-only protective mechanism. Methods identify a YPH499-derived
    default strain; S288C accessions remain reference identities. JATS permissions
    specify CC BY4.0.
  snapshot_sha256: 87eb1d7c8582e4a27cf3946f75e350994be651438829164bda912c2307e46a14
- evidence_id: mitostore-agent-jats-PMC10401023
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10401023.1/PMC10401023.1.xml
  locator: Abstract, final Introduction paragraph, Results s2 opening Tom70 deletion/overexpression
    and nascent-protein/FCS paragraphs, and Discussion s7 MitoStore comparison only.
    Remaining study sections not comprehensively audited.
  accessed_at: '2026-10-21T10:18:31.364664Z'
  support: supports
  summary: Liu2023 supplies a distinct Tom70/proteostasis context. The inspected experiments
    and Discussion describe partial Tom70 dependence and overlapping features with
    MitoStores, not demonstrated exact equivalence or a fixed Tom70 structural constituent.
  snapshot_sha256: 5fcea748c80a6d7c2ebdf5f52ad077883e6a6042d2334909f10cc41899c87c14
- evidence_id: mitostore-agent-PXD035762
  kind: database
  reference: https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD035762
  locator: Native project title, projectDescription, dataProcessingProtocol, organisms
    and references; no raw spectra or deposited quantitative files reanalysed
  accessed_at: '2026-10-21T10:17:18.058167Z'
  support: supports
  summary: The PRIDE project title and description concern MitoStore/Hsp104 affinity
    proteomics, but its linked reference is the different Ubc8 paper DOI10.26508/LSA.202201526.
    Project-wide protein counts and the paper-specific affinity-purification cohort
    are not interchangeable. The target already retains this metadata discrepancy.
  snapshot_sha256: c08653cb860157b90b4ddf491cf26d5c036912a9939af239d520bed2c6b4c7b2
- evidence_id: mitostore-agent-image
  kind: record_content
  reference: data/images/inclusion/mitostore/pmc10068336_embj2022112309_fig_0005.jpg
  locator: Entire maintained figure and every panel visually inspected, including
    genotype/species labels, scale bars, blots/plots or schematic; source caption
    and license read separately.
  accessed_at: '2026-10-21T10:24:12.642178Z'
  support: supports
  summary: All panelsA-D of the maintained Figure5 were visually read, including tested
    Hsp104/Hsp42 deletion strains and distinct panel scale bars. Native package filename
    EMBJ-42-e112309-g007.jpg corresponds to source Figure5 because supplementary figures
    are interleaved; it does not indicate a figure-number mismatch. No third-party
    figure credit overrides the article license. Local SHA-256 matches the record,
    and local MD5 d5aed1d2f71065dd88d6dc617a55f368 matches the exact native PMC media
    entry.
  snapshot_sha256: 08fe6da4832a3b949f031e367ee32323e88d73b83fece71cfd4ec02fd03e35d0
- evidence_id: mitostore-agent-native-package-PMC10068336
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10068336.1/PMC10068336.1.json
  locator: Article/package identity, license code and exact media_urls match
  accessed_at: '2026-10-21T10:17:53.513699Z'
  support: supports
  summary: The native PMC package identifies the article and matching media filename/MD5.
    The explicit CC BY4.0 license is read in the separately cited JATS permissions,
    rather than inferred from package shorthand.
  snapshot_sha256: f6ece7ab1fb2387ccb182314341d9aba437b0061c4cefdc8965285dfe90d2f7b
- evidence_id: boundary-0
  kind: record_content
  reference: data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:31:36Z'
  support: context_only
  summary: These maintained fields were read to verify the stated identity boundary.
    This is contextual corpus evidence, not an independent full scientific review
    of the neighboring record.
- evidence_id: boundary-1
  kind: record_content
  reference: data/structures/inclusion/insoluble_protein_deposit.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:31:36Z'
  support: context_only
  summary: These maintained fields were read to verify the stated identity boundary.
    This is contextual corpus evidence, not an independent full scientific review
    of the neighboring record.
- evidence_id: boundary-2
  kind: record_content
  reference: data/structures/membrane_organelle/intramitochondrial_protein_quality_control_compartment.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:31:36Z'
  support: context_only
  summary: These maintained fields were read to verify the stated identity boundary.
    This is contextual corpus evidence, not an independent full scientific review
    of the neighboring record.
- evidence_id: boundary-3
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:31:36Z'
  support: context_only
  summary: These maintained fields were read to verify the stated identity boundary.
    This is contextual corpus evidence, not an independent full scientific review
    of the neighboring record.
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T10:18:05.320983Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T10:18:07.399025Z'
  support: supports
  summary: "data/structures/inclusion/mitostore.yaml  (cellstructuremech:mitostore)\n\
    \  precursor_granule_assembly\tcargo\tNO_GENE_SYMBOLS\t->precursor_cargo (OTHER:\
    \ presequence-enriched protein precursor cargo)\n  precursor_recovery_and_tolerance\t\
    cargo\tNO_GENE_SYMBOLS\t->precursor_cargo (OTHER: presequence-enriched protein\
    \ precursor cargo)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     2  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 448ddff38bf088be0c748c4d74ce9a0cfffd623e46490b160132b8904cc5aa64
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/inclusion/mitostore.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:27Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/inclusion/mitostore.yaml'
  snapshot_sha256: a30b4a4014a2aaea50bda57975c34913ffe5dc384d9e2847901a4ec1a48b928e
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/inclusion/mitostore.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/mitostore-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:29Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/inclusion/mitostore.yaml\
    \ --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/mitostore-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/mitostore-strict.tsv"
  snapshot_sha256: ef39600288ac9440e763faf8164bbf489c6deb2fa1721ddfa9a5cdf155a8be34
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/inclusion/mitostore.yaml; exact collect() scope; hash identifies
    the entire original resolver TSV
  accessed_at: '2026-10-21T10:31:36Z'
  support: supports
  summary: '10 of11 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: cellstructuremech:mitostore: SKIPPED; resolved by evidence mitostore-agent-local-ids.
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
  topic: Cytosolic deposit distinct from mitochondrial compartments
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: The local MitoStore identity and cytoplasmic inclusion hierarchy agree
    with the defining study. Surface association and a mitochondrial precursor bias
    do not relocate the deposit into the mitochondrial matrix or make it a membrane-enclosed
    mitochondrial-derived compartment. JUNQ/IPOD distinctions and the bounded exact-name
    search are preserved.
  evidence_ids:
  - mitostore-agent-go
  - mitostore-agent-local-ids
  - mitostore-agent-ols-exact-0
  - mitostore-agent-jats-PMC10068336
  - mitostore-agent-jats-PMC10401023
  - boundary-0
  - boundary-1
  - boundary-2
  - boundary-3
  - record
- assessment_id: grounding
  area: grounding
  topic: Heterogeneous cargo and precise chaperone classes
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: The cargo is a nonhomologous cohort and does not require a single family
    identifier. IPR031107 correctly grounds the small-HSP class, while the two domain/superfamily
    alternatives do not replace it. Hsp104-only grounding is appropriately withheld
    from the inspected broader Clp families. All three concrete reference proteins
    and gene/taxon pairings resolve; native identity is separate from inclusion association.
  evidence_ids:
  - mitostore-agent-P31539
  - mitostore-agent-Q12329
  - mitostore-agent-P15992
  - mitostore-agent-matches-P31539
  - mitostore-agent-matches-Q12329
  - mitostore-agent-matches-P15992
  - mitostore-agent-IPR031107
  - mitostore-agent-IPR002068
  - mitostore-agent-IPR008978
  - mitostore-agent-IPR001270
  - mitostore-agent-IPR050130
  - mitostore-agent-jats-PMC10068336
  - record
  - policy
- assessment_id: necessity
  area: evidence
  topic: Formation tests are component- and assay-specific
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: CONDITIONAL Hsp104 and small-HSP necessity is supported only for the tested
    formation assays. In particular, Hsp42 has direct deletion evidence while Hsp26
    is a co-eluting candidate; the maintained notes explicitly retain that distinction.
    Presequence dependence of the Mam33 reporter does not establish every cargo molecule
    as necessary for granule formation.
  evidence_ids:
  - mitostore-agent-jats-PMC10068336
  - mitostore-agent-P31539
  - mitostore-agent-Q12329
  - mitostore-agent-P15992
  - record
  - policy
- assessment_id: unresolved-necessity
  area: evidence
  topic: Individual cargo and Hsp26 formation requirements
  outcome: unknown
  target_ids:
  - cellstructuremech:mitostore
  summary: No inspected experiment establishes a requirement for every heterogeneous
    cargo class or for Hsp26 in MitoStore formation. The collective stored material
    is definitional, while a reporter recruitment sequence and Hsp26 co-elution do
    not establish universal assembly necessity. This unresolved scope is separate
    from the direct Hsp104/Hsp42 conditional formation tests.
  evidence_ids:
  - mitostore-agent-jats-PMC10068336
  - record
  - policy
- assessment_id: scope
  area: scope
  topic: Study conditions, reference taxa and proteomics metadata
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: Taxonomy receipts establish their own species/strain identities. The record
    distinguishes the primary YPH499-derived experiments from S288C protein-reference
    entries and does not infer population prevalence. PRIDE metadata is cited with
    its unresolved linked-reference discrepancy; the deposited files were not used
    to invent a complete inventory.
  evidence_ids:
  - mitostore-agent-tax-4932
  - mitostore-agent-tax-559292
  - mitostore-agent-doi-10.15252_embj.2022112309
  - mitostore-agent-doi-10.1073_pnas.2300475120
  - mitostore-agent-jats-PMC10068336
  - mitostore-agent-PXD035762
  - record
- assessment_id: function
  area: evidence
  topic: Storage, import competence and conditional protection
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: The functions retain precursor bias and the defining import-stress context.
    Split-GFP recovery supports import competence after the chase but does not track
    each granule molecule into mitochondria. Survival effects in rpn4-deficient import
    stress are not generalized to all proteotoxic stress or attributed solely to granule
    architecture.
  evidence_ids:
  - mitostore-agent-jats-PMC10068336
  - mitostore-agent-jats-PMC10401023
  - record
- assessment_id: graphs
  area: graph
  topic: Assembly and recovery transitions have direct experimental bounds
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: Both MECHANISTIC graphs represent tested perturbations and transitions,
    not merely parthood. They preserve presequence recruitment, Hsp104/Hsp42-dependent
    reporter granules, accessible mitochondrial-surface material, reporter recovery
    and conditional viability. Hsp26, Tom70 and a hypothetical physical tether are
    not promoted to obligatory machinery.
  evidence_ids:
  - mitostore-agent-jats-PMC10068336
  - mitostore-agent-jats-PMC10401023
  - record
  - policy
- assessment_id: image
  area: evidence
  topic: Exact Figure5 media and license
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: Local SHA-256 and native MD5 agree for the fully inspected image. The figure
    caption preserves multiple assays, scale bars and knockout context; native media
    numbering is correctly resolved against the actual source caption and explicit
    CC BY4.0 permissions.
  evidence_ids:
  - mitostore-agent-jats-PMC10068336
  - mitostore-agent-image
  - mitostore-agent-native-package-PMC10068336
  - record
- assessment_id: coverage
  area: completeness
  topic: Open molecular census is a limitation
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: No corrective issue was established. The unknown tether, nonexhaustive
    precursor inventory, Hsp26 assembly uncertainty and distinction from the other
    Tom70-associated assemblies remain explicit. No phase-separation mechanism or
    universal cellular frequency is inferred. PROPOSED status and historical discussion
    remain unchanged.
  evidence_ids:
  - mitostore-agent-jats-PMC10068336
  - mitostore-agent-jats-PMC10401023
  - mitostore-agent-PXD035762
  - mitostore-agent-IPR031107
  - mitostore-agent-IPR002068
  - mitostore-agent-IPR008978
  - mitostore-agent-IPR001270
  - mitostore-agent-IPR050130
  - record
  - policy
findings: []
actions: []
limitations:
- Only the named Krämer Results/Discussion/Methods and Figures5-6 captions, plus complete
  maintained Figure5 pixels, were audited. Raw mass-spectrometry files, all extended
  figures and numerical image datasets were not reanalysed.
- Liu2023 is used only at the explicitly named Tom70/proteostasis and comparison passages;
  the entire paper was not reviewed and distinct stress assemblies are not treated
  as exact synonyms.
- Split-GFP recovery and viability assays do not establish direct tracking of every
  stored molecule or isolate a universal granule-only protective effect. Hsp26 association
  is not evidence of formation necessity.
- The native PRIDE linked-reference discrepancy is unresolved; project-wide and paper-specific
  protein counts are not equated. Exact GO and family checks are bounded to the recorded
  queries and reviewed examples. Boundary neighbors were inspected at contextual fields
  only.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The authorized coverage task includes honest clean reviews.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
