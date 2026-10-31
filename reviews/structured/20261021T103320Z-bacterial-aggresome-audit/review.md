# Bacterial aggresome identity, RNA protection and provenance review

- Review: 20261021T103320Z-bacterial-aggresome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:13:08Z
- Finished UTC: 2026-10-21T10:33:20Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The local bacterial identity, observed constituent subset, strain-scoped examples and six-edge RNA-protection mechanism are supported. No concrete curation finding was established; assembly necessity, physical-state generality and biochemical model boundaries remain bounded.

## Scope And Provenance

Whole single-record claim review, all three protein examples and family classes, both cited primary bodies at the declared extents, all graph edges and discussions; no neighboring record dependency.

Selection: Batch19 index2; one maintained record in the frozen strict path-order selection. No neighboring scientific record used as evidential input.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:bacterial_aggresome | data/structures/inclusion/bacterial_aggresome.yaml | maintained | bacterial aggresome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | cellstructuremech:bacterial_aggresome | Target-specific native check passed. |
| Native protein causal-graphs | passed | True | cellstructuremech:bacterial_aggresome | Target-specific native check passed. |
| Focused native schema | passed | True | cellstructuremech:bacterial_aggresome | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:bacterial_aggresome | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:bacterial_aggresome | 15 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | cellstructuremech:bacterial_aggresome | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:bacterial_aggresome | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:bacterial_aggresome | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:bacterial_aggresome | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:bacterial_aggresome | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:bacterial_aggresome | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Local bacterial identity and hierarchy

identity: supported. Targets: cellstructuremech:bacterial_aggresome.

A local proposed bacterial aggresome identity with inclusion-body parent and cytoplasmic parthood is supported. GO:0016235 requires dynein-mediated microtubule transport and is correctly not an exact match. The related stress-granule synonym and explicit BR-body distinction avoid claiming that all bacterial RNA condensates are the same structure.

### Observed constituent subset

completeness: supported. Targets: cellstructuremech:bacterial_aggresome.

HslU, Kbl and AcnB are directly observed fluorescent-marker constituents with differing kinetics; selective mRNA enrichment is supported by fractionation/RNA-seq, FISH and tagged transcripts. The four rows are a supported subset, not a fixed proteome. Upstream HokB and normally excluded wild-type RNB/RBN/ORN are correctly omitted as constituents.

### Unknown formation requirements

evidence: unknown. Targets: cellstructuremech:bacterial_aggresome.

The primary studies do not establish that every listed protein or RNA class is indispensable to assembly. All four essentialities remain UNKNOWN; colocalization, RNA protection and family identity are not promoted to scaffold necessity. The accepted-manuscript Figure1 heading does not itself provide a depletion test establishing an all-mRNA requirement.

### Native families, proteins and transcripts

grounding: supported. Targets: cellstructuremech:bacterial_aggresome.

Exact native families identify HslU, Kbl and Aconitase B and are present in the matching individual entries. The reviewed examples accurately identify K12 genes/proteins; HslU is an ATPase subunit, not HslV or the complete HslUV complex. SO:0000234 supplies mRNA material identity, with localization and transcript specificity supplied by the primary study.

### Experimental strain and state boundaries

scope: supported. Targets: cellstructuremech:bacterial_aggresome.

MG1655 is explicitly named for isolation from arsenite-treated, starved or HokB-induced cells. K12 UniProt reference entries are identity examples, not substituted MG1655-specific localization evidence. The record supplies no unwarranted prevalence estimate and does not promise liquid behavior for every bacterium or every aged protein aggregate.

### Six-edge RNA-protection mechanism

graph: supported. Targets: cellstructuremech:bacterial_aggresome.

The graph is mechanistic within its stated assays: RNA sequestration, restriction of tested RNases, active-versus-inactive RNase-entry controls, stress-removal release, preserved templates and renewed translation have direct experimental support. The record preserves the uncertainty about which material supplies the repulsive charge and does not generalize exclusion to all RNases; rRNA/tRNA-processing enzymes can be enriched.

### RNA stabilization and recovery

evidence: supported. Targets: cellstructuremech:bacterial_aggresome.

Preservation of selected mRNAs and their later cytoplasmic use fit GO:0048255. The rifampicin/tetracycline comparison separates new translation from maturation of existing fluorescent protein. The record correctly stops short of a universal survival edge: active RNase entry lengthens lag and increases persister fractions, while separate chemical inhibition of condensate formation reduces persistence.

### Evidence tiers and attribution

provenance: supported. Targets: cellstructuremech:bacterial_aggresome.

The cited2021 and2025 identities and experimental source extents are verified. The2025 full-body claims are assessed from the accepted manuscript, as the record states; publisher markup inspected for availability contains abstract/extended data rather than the main article body. Native databases establish their own identity assertions, while membership and mechanism remain grounded in the studies.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-identity | data/structures/inclusion/bacterial_aggresome.yaml; identifier; definition; mapping_status; identity discussion | context_only | Frozen target defines this local proposed structure identifier. The resolver deliberately skips repository-minted identifiers; primary-source and native-ontology checks independently assess the stated identity, without asserting an external exact match. |
| aggresome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016234,GO:0016235,GO:0005737,GO:0048255; results for all four IDs: name, definition and available synonyms | supports | Native GO distinguishes dynein/microtubule-defined aggresome GO:0016235 from generic inclusion body GO:0016234, cytoplasm GO:0005737 and mRNA stabilization GO:0048255. The local bacterial identity avoids importing the eukaryotic transport definition. |
| aggresome-agent-so | https://www.ebi.ac.uk/ols4/api/ontologies/so/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0000234; obo_id; label; description; obo_definition_citation | supports | SO:0000234 is messenger RNA, supporting the declared RNA material class rather than every RNA species or an organelle-specific transcript type. |
| aggresome-agent-PMC8528417 | https://pmc-oa-opendata.s3.amazonaws.com/PMC8528417.1/PMC8528417.1.xml; JATS Results: Aggresome formation in bacteria; Aggresome formation occurs through LLPS; Aggresome formation increases the bacterial fitness; complete Discussion; Methods Bacterial strains, phage, and plasmid construction; included Figs1/2/4 captions | supports | Jin2021 observes chromosomally tagged HslU, Kbl and AcnB in bacterial aggresomes with different incorporation kinetics. Single-molecule mobility, fusion, FRAP and chemical perturbation support liquid-like behavior in the assayed states. Composition and physical state vary. MG1655 and HokB induction are experimental contexts; survival assays are condition-specific and do not establish a universal scaffold or fitness effect. |
| aggresome-agent-pei2025-aam | https://eprints.whiterose.ac.uk/id/eprint/229675/1/Aggresomes_protect_mRNA_AAM-ms_and_si.pdf; White Rose accepted manuscript PDF: complete Main/Results/Discussion pp3–25; Methods strain/plasmid construction, RNA labeling/imaging, isolation/fractionation/RNA assays, translation recovery and persister assay pp25–30; Fig5 pixels pp17–18 and Fig6 pixels/caption p20 | supports | Accepted manuscript supports selective longer-mRNA partitioning, observed transcript examples, preservation relative to cytosol, exclusion of tested RNB/RBN/ORN and charge-mutant controls. RNB-MO retains activity and enters/depletes RNA, whereas inactive RNB-ME enters without equivalent depletion. Arsenite washout releases RNA; GlpK-GFP recovery under rifampicin versus rifampicin+tetracycline supports reuse while controlling preexisting fluorophore maturation. RNase-mutant lag/persistence and chemical-disruption persistence are distinct outcomes. |
| aggresome-agent-doi-10.1126_sciadv.abh2929 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1126%2Fsciadv.abh2929&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString | supports | Exact native DOI metadata resolves PMID:34669478, Membraneless organelles formed by liquid-liquid phase separation increase bacterial fitness. (2021). This verifies bibliographic identity; scientific body support uses separately read primary sources. |
| aggresome-agent-doi-10.1038_s41564-025-02086-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41564-025-02086-5&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString | supports | Exact native DOI metadata resolves PMID:40830717, Aggresomes protect mRNA under stress in Escherichia coli. (2025). This verifies bibliographic identity; scientific body support uses separately read primary sources. |
| aggresome-agent-P0A6H5 | https://rest.uniprot.org/uniprotkb/P0A6H5.json; primaryAccession; entryType; proteinDescription.recommendedName; genes; organism | supports | Native UniProtKB reviewed (Swiss-Prot) entry P0A6H5 identifies hslU, ATP-dependent protease ATPase subunit HslU, in NCBITaxon:83333. This establishes accession/gene/taxon identity; deposit membership is evaluated from microscopy and interventions in the primary studies. |
| aggresome-agent-P0AB77 | https://rest.uniprot.org/uniprotkb/P0AB77.json; primaryAccession; entryType; proteinDescription.recommendedName; genes; organism | supports | Native UniProtKB reviewed (Swiss-Prot) entry P0AB77 identifies kbl, 2-amino-3-ketobutyrate coenzyme A ligase, in NCBITaxon:83333. This establishes accession/gene/taxon identity; deposit membership is evaluated from microscopy and interventions in the primary studies. |
| aggresome-agent-P36683 | https://rest.uniprot.org/uniprotkb/P36683.json; primaryAccession; entryType; proteinDescription.recommendedName; genes; organism | supports | Native UniProtKB reviewed (Swiss-Prot) entry P36683 identifies acnB, Aconitate hydratase B, in NCBITaxon:83333. This establishes accession/gene/taxon identity; deposit membership is evaluated from microscopy and interventions in the primary studies. |
| aggresome-agent-IPR004491 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004491/; metadata.accession; type; name; hierarchy | supports | Native InterPro family IPR004491: Heat shock protein HslU. Entry type, name and hierarchy delimit the sequence class; no localization or assembly-necessity conclusion is drawn from the family metadata. |
| aggresome-agent-IPR011282 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011282/; metadata.accession; type; name; hierarchy | supports | Native InterPro family IPR011282: 2-amino-3-ketobutyrate coenzyme A ligase. Entry type, name and hierarchy delimit the sequence class; no localization or assembly-necessity conclusion is drawn from the family metadata. |
| aggresome-agent-IPR004406 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004406/; metadata.accession; type; name; hierarchy | supports | Native InterPro family IPR004406: Aconitase B. Entry type, name and hierarchy delimit the sequence class; no localization or assembly-necessity conclusion is drawn from the family metadata. |
| aggresome-agent-ipr-matches-P0A6H5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A6H5/?page_size=200; count; next; results[].metadata.accession/name/type | supports | Complete current integrated InterPro match response for P0A6H5: 6 entries, next=null. Family entries: IPR004491 Heat shock protein HslU; IPR050052 ATP-dependent Clp protease ATP-binding subunit ClpX. Domain, site and superfamily entries do not become exact whole-protein groundings. |
| aggresome-agent-ipr-matches-P0AB77 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AB77/?page_size=200; count; next; results[].metadata.accession/name/type | supports | Complete current integrated InterPro match response for P0AB77: 7 entries, next=null. Family entries: IPR011282 2-amino-3-ketobutyrate coenzyme A ligase; IPR050087 8-amino-7-oxononanoate synthase class-II. Domain, site and superfamily entries do not become exact whole-protein groundings. |
| aggresome-agent-ipr-matches-P36683 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P36683/?page_size=200; count; next; results[].metadata.accession/name/type | supports | Complete current integrated InterPro match response for P36683: 12 entries, next=null. Family entries: IPR004406 Aconitase B; IPR050926 Aconitase/IPM Isomerase. Domain, site and superfamily entries do not become exact whole-protein groundings. |
| aggresome-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; taxId; scientificName; rank; otherNames | supports | Native taxonomy identifies NCBITaxon:83333 as Escherichia coli K-12 (rank strain). Strain examples and reference-proteome identities remain distinct from general lineage prevalence. |
| aggresome-agent-tax-511145 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/511145; taxId; scientificName; rank; otherNames | supports | Native taxonomy identifies NCBITaxon:511145 as Escherichia coli str. K-12 substr. MG1655 (rank no rank). Strain examples and reference-proteome identities remain distinct from general lineage prevalence. |
| aggresome-agent-reviewed-uniqueness | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A83333+AND+%28gene_exact%3AhslU+OR+gene_exact%3Akbl+OR+gene_exact%3AacnB%29&amp;format=json&amp;size=500; Query reviewed:true AND organism_id:83333 AND (gene_exact:hslU OR gene_exact:kbl OR gene_exact:acnB); size500; exactly three results; no next-page header | supports | Bounded native reviewed-UniProt query returns exactly P0A6H5/hslU, P0AB77/kbl and P36683/acnB in taxon83333. This supports the stated current one-reviewed-entry-per-gene identities; it does not test assembly membership. |
| native-verify | /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml --verify; Captured native target-specific log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml --causal-graphs; Captured native target-specific log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/inclusion/bacterial_aggresome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/inclusion/bacterial_aggresome.yaml |
| strict-result | just validate-strict data/structures/inclusion/bacterial_aggresome.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/bacterial_aggresome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/inclusion/bacterial_aggresome.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/bacterial_aggresome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/bacterial_aggresome-strict.tsv |
| target-curies | just check-curies-strict; data/structures/inclusion/bacterial_aggresome.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 15 of16 collected target identifiers returned OK in this fresh base resolver run. Residuals: cellstructuremech:bacterial_aggresome: SKIPPED; resolved by evidence local-identity. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Jin2021 reading covered the three claim-bearing experimental Results subsections, Discussion, strain/construction Methods and included captions; the separate simulation section, original movies and raw tracking data were not reanalyzed.
- Pei2025 full-body evidence comes from the openly deposited accepted manuscript. Complete Main/Results/Discussion and the specified Methods were read, with Figures5 and6 pixels inspected. The publisher response exposes abstract and extended-data material, not a readable main body; it is not used to inflate source access.
- Original RNA-seq/proteomics files, all videos, complete supplementary tables and mathematical supplementary derivations were not independently audited. Quantitative modeling assumptions do not become direct molecular observations.
- Assembly necessity for the listed components remains unknown. RNase exclusion is limited to the tested enzymes and interventions; neither every RNA nor every RNase behaves identically.
- Exact current family and reference-protein identities do not prove general bacterial prevalence, a fixed condensate composition or universal liquid-state properties. No local neighboring scientific YAML or new exhaustive ontology absence search informed this review.
- Initial network-restricted native protein verification failed from DNS resolution and was preserved. Public-network rerun and final protein/causal, schema and strict checks passed.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103320Z-bacterial-aggresome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Bacterial aggresome identity, RNA protection and provenance review
started_at: '2026-10-21T10:13:08Z'
finished_at: '2026-10-21T10:33:20Z'
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
summary: The local bacterial identity, observed constituent subset, strain-scoped
  examples and six-edge RNA-protection mechanism are supported. No concrete curation
  finding was established; assembly necessity, physical-state generality and biochemical
  model boundaries remain bounded.
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
  - path: data/structures/inclusion/bacterial_aggresome.yaml
    sha256: 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636
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
- target_id: cellstructuremech:bacterial_aggresome
  path: data/structures/inclusion/bacterial_aggresome.yaml
  label: bacterial aggresome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/bacterial_aggresome.yaml
    role: maintained scientific record
scope:
  description: Whole single-record claim review, all three protein examples and family
    classes, both cited primary bodies at the declared extents, all graph edges and
    discussions; no neighboring record dependency.
  selection: Batch19 index2; one maintained record in the frozen strict path-order
    selection. No neighboring scientific record used as evidential input.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:bacterial_aggresome
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
  command: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml
    --verify
  exit_code: 0
  summary: Target-specific native check passed.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
  command: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml
    --causal-graphs
  exit_code: 0
  summary: Target-specific native check passed.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
  command: just validate data/structures/inclusion/bacterial_aggresome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
  command: just validate-strict data/structures/inclusion/bacterial_aggresome.yaml
    --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/bacterial_aggresome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
  summary: 15 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - local-identity
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - local-identity
  - aggresome-agent-go
  - aggresome-agent-so
  - aggresome-agent-PMC8528417
  - aggresome-agent-pei2025-aam
  - aggresome-agent-doi-10.1126_sciadv.abh2929
  - aggresome-agent-doi-10.1038_s41564-025-02086-5
  - aggresome-agent-P0A6H5
  - aggresome-agent-P0AB77
  - aggresome-agent-P36683
  - aggresome-agent-IPR004491
  - aggresome-agent-IPR011282
  - aggresome-agent-IPR004406
  - aggresome-agent-ipr-matches-P0A6H5
  - aggresome-agent-ipr-matches-P0AB77
  - aggresome-agent-ipr-matches-P36683
  - aggresome-agent-tax-83333
  - aggresome-agent-tax-511145
  - aggresome-agent-reviewed-uniqueness
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
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
  - cellstructuremech:bacterial_aggresome
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
  - cellstructuremech:bacterial_aggresome
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
  - cellstructuremech:bacterial_aggresome
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
  - cellstructuremech:bacterial_aggresome
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
- evidence_id: local-identity
  kind: record_content
  reference: data/structures/inclusion/bacterial_aggresome.yaml
  locator: identifier; definition; mapping_status; identity discussion
  accessed_at: '2026-10-21T10:23:15Z'
  support: context_only
  summary: Frozen target defines this local proposed structure identifier. The resolver
    deliberately skips repository-minted identifiers; primary-source and native-ontology
    checks independently assess the stated identity, without asserting an external
    exact match.
  snapshot_sha256: 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636
- evidence_id: aggresome-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016234,GO:0016235,GO:0005737,GO:0048255
  locator: 'results for all four IDs: name, definition and available synonyms'
  accessed_at: '2026-10-21T10:15:28.030181Z'
  support: supports
  summary: Native GO distinguishes dynein/microtubule-defined aggresome GO:0016235
    from generic inclusion body GO:0016234, cytoplasm GO:0005737 and mRNA stabilization
    GO:0048255. The local bacterial identity avoids importing the eukaryotic transport
    definition.
  snapshot_sha256: f2a31c4df2153f36417cd25d3ce8f59a4743ec32f437f207b52104deb0bbcfbb
- evidence_id: aggresome-agent-so
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/so/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0000234
  locator: obo_id; label; description; obo_definition_citation
  accessed_at: '2026-10-21T10:15:28.145461Z'
  support: supports
  summary: SO:0000234 is messenger RNA, supporting the declared RNA material class
    rather than every RNA species or an organelle-specific transcript type.
  snapshot_sha256: d11dcc2fd540bdf6528172e73d4bea70206ce9f9ccb212c1323642a27dd609d7
- evidence_id: aggresome-agent-PMC8528417
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8528417.1/PMC8528417.1.xml
  locator: 'JATS Results: Aggresome formation in bacteria; Aggresome formation occurs
    through LLPS; Aggresome formation increases the bacterial fitness; complete Discussion;
    Methods Bacterial strains, phage, and plasmid construction; included Figs1/2/4
    captions'
  accessed_at: '2026-10-21T10:15:26.814715Z'
  support: supports
  summary: Jin2021 observes chromosomally tagged HslU, Kbl and AcnB in bacterial aggresomes
    with different incorporation kinetics. Single-molecule mobility, fusion, FRAP
    and chemical perturbation support liquid-like behavior in the assayed states.
    Composition and physical state vary. MG1655 and HokB induction are experimental
    contexts; survival assays are condition-specific and do not establish a universal
    scaffold or fitness effect.
  snapshot_sha256: 541eafcd7f01686c8c5a80e986beb4be9cab84bcece5383651d31d9108baf1c0
- evidence_id: aggresome-agent-pei2025-aam
  kind: primary_source
  reference: https://eprints.whiterose.ac.uk/id/eprint/229675/1/Aggresomes_protect_mRNA_AAM-ms_and_si.pdf
  locator: 'White Rose accepted manuscript PDF: complete Main/Results/Discussion pp3–25;
    Methods strain/plasmid construction, RNA labeling/imaging, isolation/fractionation/RNA
    assays, translation recovery and persister assay pp25–30; Fig5 pixels pp17–18
    and Fig6 pixels/caption p20'
  accessed_at: '2026-10-21T10:15:27.666735Z'
  support: supports
  summary: Accepted manuscript supports selective longer-mRNA partitioning, observed
    transcript examples, preservation relative to cytosol, exclusion of tested RNB/RBN/ORN
    and charge-mutant controls. RNB-MO retains activity and enters/depletes RNA, whereas
    inactive RNB-ME enters without equivalent depletion. Arsenite washout releases
    RNA; GlpK-GFP recovery under rifampicin versus rifampicin+tetracycline supports
    reuse while controlling preexisting fluorophore maturation. RNase-mutant lag/persistence
    and chemical-disruption persistence are distinct outcomes.
  snapshot_sha256: 8390cd9dbd5f3eb121cafedcb879ec5511cf6b88988c4ded24fd18e8e3c2d852
- evidence_id: aggresome-agent-doi-10.1126_sciadv.abh2929
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1126%2Fsciadv.abh2929&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString
  accessed_at: '2026-10-21T10:15:27.512342Z'
  support: supports
  summary: Exact native DOI metadata resolves PMID:34669478, Membraneless organelles
    formed by liquid-liquid phase separation increase bacterial fitness. (2021). This
    verifies bibliographic identity; scientific body support uses separately read
    primary sources.
  snapshot_sha256: 330b83673d72870e6f52400041855ce1fd707168102ebb8bdb9fa875fa53e42c
- evidence_id: aggresome-agent-doi-10.1038_s41564-025-02086-5
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41564-025-02086-5&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString
  accessed_at: '2026-10-21T10:15:27.527069Z'
  support: supports
  summary: Exact native DOI metadata resolves PMID:40830717, Aggresomes protect mRNA
    under stress in Escherichia coli. (2025). This verifies bibliographic identity;
    scientific body support uses separately read primary sources.
  snapshot_sha256: 946bfd924732f71fcc4d6c5e3d5a85234102c76f8d97cc5a738682443f0673d1
- evidence_id: aggresome-agent-P0A6H5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A6H5.json
  locator: primaryAccession; entryType; proteinDescription.recommendedName; genes;
    organism
  accessed_at: '2026-10-21T10:15:31.517354Z'
  support: supports
  summary: Native UniProtKB reviewed (Swiss-Prot) entry P0A6H5 identifies hslU, ATP-dependent
    protease ATPase subunit HslU, in NCBITaxon:83333. This establishes accession/gene/taxon
    identity; deposit membership is evaluated from microscopy and interventions in
    the primary studies.
  snapshot_sha256: 5b1f0a0cd15bf350edb1348cfeb803e6b9774608266b6f7b8cf1f254ca6e22b1
- evidence_id: aggresome-agent-P0AB77
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AB77.json
  locator: primaryAccession; entryType; proteinDescription.recommendedName; genes;
    organism
  accessed_at: '2026-10-21T10:15:31.653454Z'
  support: supports
  summary: Native UniProtKB reviewed (Swiss-Prot) entry P0AB77 identifies kbl, 2-amino-3-ketobutyrate
    coenzyme A ligase, in NCBITaxon:83333. This establishes accession/gene/taxon identity;
    deposit membership is evaluated from microscopy and interventions in the primary
    studies.
  snapshot_sha256: 9407fd76a12ceb1f0afbd7cf7ee9d2de0c48d6d60b2a965afcdd6e048e032332
- evidence_id: aggresome-agent-P36683
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36683.json
  locator: primaryAccession; entryType; proteinDescription.recommendedName; genes;
    organism
  accessed_at: '2026-10-21T10:15:32.104175Z'
  support: supports
  summary: Native UniProtKB reviewed (Swiss-Prot) entry P36683 identifies acnB, Aconitate
    hydratase B, in NCBITaxon:83333. This establishes accession/gene/taxon identity;
    deposit membership is evaluated from microscopy and interventions in the primary
    studies.
  snapshot_sha256: 6b47f414de4336cbd14a07e459d1bc8c1a540dad0d4c1d10e899c79d2d212f45
- evidence_id: aggresome-agent-IPR004491
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004491/
  locator: metadata.accession; type; name; hierarchy
  accessed_at: '2026-10-21T10:15:32.774174Z'
  support: supports
  summary: 'Native InterPro family IPR004491: Heat shock protein HslU. Entry type,
    name and hierarchy delimit the sequence class; no localization or assembly-necessity
    conclusion is drawn from the family metadata.'
  snapshot_sha256: 951e85c4faccb707ab1ab1faa7439da273827a28977d4d806f1a4dddd41b64ca
- evidence_id: aggresome-agent-IPR011282
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011282/
  locator: metadata.accession; type; name; hierarchy
  accessed_at: '2026-10-21T10:15:32.969337Z'
  support: supports
  summary: 'Native InterPro family IPR011282: 2-amino-3-ketobutyrate coenzyme A ligase.
    Entry type, name and hierarchy delimit the sequence class; no localization or
    assembly-necessity conclusion is drawn from the family metadata.'
  snapshot_sha256: 7ad07d461c7ee5fb160f71c0148c217d445ed90e9869e24f55d8358ca5dd8654
- evidence_id: aggresome-agent-IPR004406
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004406/
  locator: metadata.accession; type; name; hierarchy
  accessed_at: '2026-10-21T10:15:33.167455Z'
  support: supports
  summary: 'Native InterPro family IPR004406: Aconitase B. Entry type, name and hierarchy
    delimit the sequence class; no localization or assembly-necessity conclusion is
    drawn from the family metadata.'
  snapshot_sha256: 31e5072ecdf886cf06d48c0c607defcf979a412f2e6504bdb7f2c71c5a2f3900
- evidence_id: aggresome-agent-ipr-matches-P0A6H5
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A6H5/?page_size=200
  locator: count; next; results[].metadata.accession/name/type
  accessed_at: '2026-10-21T10:15:31.571914Z'
  support: supports
  summary: 'Complete current integrated InterPro match response for P0A6H5: 6 entries,
    next=null. Family entries: IPR004491 Heat shock protein HslU; IPR050052 ATP-dependent
    Clp protease ATP-binding subunit ClpX. Domain, site and superfamily entries do
    not become exact whole-protein groundings.'
  snapshot_sha256: 8b8e83bf3e83d0adda7b14bfc2211f7ffb4d3b364cf0ac4e74fb4787b55f9993
- evidence_id: aggresome-agent-ipr-matches-P0AB77
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AB77/?page_size=200
  locator: count; next; results[].metadata.accession/name/type
  accessed_at: '2026-10-21T10:15:31.772010Z'
  support: supports
  summary: 'Complete current integrated InterPro match response for P0AB77: 7 entries,
    next=null. Family entries: IPR011282 2-amino-3-ketobutyrate coenzyme A ligase;
    IPR050087 8-amino-7-oxononanoate synthase class-II. Domain, site and superfamily
    entries do not become exact whole-protein groundings.'
  snapshot_sha256: 787db1246babcf64a482031fc244cef7e5680deeb15e62f6f228a6215d844409
- evidence_id: aggresome-agent-ipr-matches-P36683
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P36683/?page_size=200
  locator: count; next; results[].metadata.accession/name/type
  accessed_at: '2026-10-21T10:15:32.160789Z'
  support: supports
  summary: 'Complete current integrated InterPro match response for P36683: 12 entries,
    next=null. Family entries: IPR004406 Aconitase B; IPR050926 Aconitase/IPM Isomerase.
    Domain, site and superfamily entries do not become exact whole-protein groundings.'
  snapshot_sha256: b97a111f85e809ccdf13e0fd7f8a262f418b7aae864b0298af0175233fa19085
- evidence_id: aggresome-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: taxId; scientificName; rank; otherNames
  accessed_at: '2026-10-21T10:15:32.362455Z'
  support: supports
  summary: Native taxonomy identifies NCBITaxon:83333 as Escherichia coli K-12 (rank
    strain). Strain examples and reference-proteome identities remain distinct from
    general lineage prevalence.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: aggresome-agent-tax-511145
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/511145
  locator: taxId; scientificName; rank; otherNames
  accessed_at: '2026-10-21T10:15:32.566862Z'
  support: supports
  summary: Native taxonomy identifies NCBITaxon:511145 as Escherichia coli str. K-12
    substr. MG1655 (rank no rank). Strain examples and reference-proteome identities
    remain distinct from general lineage prevalence.
  snapshot_sha256: e3a402d3d5b5d1b11deda22f50922b38962f0bb955b7fa8edfea0a937277199e
- evidence_id: aggresome-agent-reviewed-uniqueness
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A83333+AND+%28gene_exact%3AhslU+OR+gene_exact%3Akbl+OR+gene_exact%3AacnB%29&format=json&size=500
  locator: Query reviewed:true AND organism_id:83333 AND (gene_exact:hslU OR gene_exact:kbl
    OR gene_exact:acnB); size500; exactly three results; no next-page header
  accessed_at: '2026-10-21T10:21:13Z'
  support: supports
  summary: Bounded native reviewed-UniProt query returns exactly P0A6H5/hslU, P0AB77/kbl
    and P36683/acnB in taxon83333. This supports the stated current one-reviewed-entry-per-gene
    identities; it does not test assembly membership.
  snapshot_sha256: 232e256a842a61b847a0732d27eb3f10cc930638eb222407b2151080812282ae
  search_scope: Remote public UniProtKB only; reviewed entries with organism_id83333
    and exact gene hslU, kbl or acnB; one response with size500 and exactly three
    results. Filesystem ignore rules are not applicable to this bounded remote query;
    no claim of local-file absence.
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml
    --verify
  locator: Captured native target-specific log
  accessed_at: '2026-10-21T10:17:09.160453Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml
    --causal-graphs
  locator: Captured native target-specific log
  accessed_at: '2026-10-21T10:17:11.144626Z'
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
  reference: just validate data/structures/inclusion/bacterial_aggresome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:09Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/inclusion/bacterial_aggresome.yaml'
  snapshot_sha256: c5855585d119f531b31f6685ce8d0a76f9c29086984172aed3f8e16274730ea3
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/inclusion/bacterial_aggresome.yaml
    --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/bacterial_aggresome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:11Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/inclusion/bacterial_aggresome.yaml\
    \ --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/bacterial_aggresome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/bacterial_aggresome-strict.tsv"
  snapshot_sha256: 27b49b993a66055fde5cb93332c272bdef480b4e5b3cddd9e20da062f8ffecd3
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/inclusion/bacterial_aggresome.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:23:15Z'
  support: supports
  summary: '15 of16 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: cellstructuremech:bacterial_aggresome: SKIPPED; resolved by evidence
    local-identity. Source-native identity checked separately.'
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
  topic: Local bacterial identity and hierarchy
  outcome: supported
  target_ids:
  - cellstructuremech:bacterial_aggresome
  summary: A local proposed bacterial aggresome identity with inclusion-body parent
    and cytoplasmic parthood is supported. GO:0016235 requires dynein-mediated microtubule
    transport and is correctly not an exact match. The related stress-granule synonym
    and explicit BR-body distinction avoid claiming that all bacterial RNA condensates
    are the same structure.
  evidence_ids:
  - local-identity
  - aggresome-agent-go
  - aggresome-agent-PMC8528417
  - aggresome-agent-pei2025-aam
- assessment_id: composition
  area: completeness
  topic: Observed constituent subset
  outcome: supported
  target_ids:
  - cellstructuremech:bacterial_aggresome
  summary: HslU, Kbl and AcnB are directly observed fluorescent-marker constituents
    with differing kinetics; selective mRNA enrichment is supported by fractionation/RNA-seq,
    FISH and tagged transcripts. The four rows are a supported subset, not a fixed
    proteome. Upstream HokB and normally excluded wild-type RNB/RBN/ORN are correctly
    omitted as constituents.
  evidence_ids:
  - aggresome-agent-PMC8528417
  - aggresome-agent-pei2025-aam
  - aggresome-agent-so
- assessment_id: necessity
  area: evidence
  topic: Unknown formation requirements
  outcome: unknown
  target_ids:
  - cellstructuremech:bacterial_aggresome
  summary: The primary studies do not establish that every listed protein or RNA class
    is indispensable to assembly. All four essentialities remain UNKNOWN; colocalization,
    RNA protection and family identity are not promoted to scaffold necessity. The
    accepted-manuscript Figure1 heading does not itself provide a depletion test establishing
    an all-mRNA requirement.
  evidence_ids:
  - aggresome-agent-PMC8528417
  - aggresome-agent-pei2025-aam
- assessment_id: identifiers
  area: grounding
  topic: Native families, proteins and transcripts
  outcome: supported
  target_ids:
  - cellstructuremech:bacterial_aggresome
  summary: Exact native families identify HslU, Kbl and Aconitase B and are present
    in the matching individual entries. The reviewed examples accurately identify
    K12 genes/proteins; HslU is an ATPase subunit, not HslV or the complete HslUV
    complex. SO:0000234 supplies mRNA material identity, with localization and transcript
    specificity supplied by the primary study.
  evidence_ids:
  - aggresome-agent-P0A6H5
  - aggresome-agent-P0AB77
  - aggresome-agent-P36683
  - aggresome-agent-IPR004491
  - aggresome-agent-IPR011282
  - aggresome-agent-IPR004406
  - aggresome-agent-ipr-matches-P0A6H5
  - aggresome-agent-ipr-matches-P0AB77
  - aggresome-agent-ipr-matches-P36683
  - aggresome-agent-so
  - aggresome-agent-reviewed-uniqueness
- assessment_id: taxa
  area: scope
  topic: Experimental strain and state boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:bacterial_aggresome
  summary: MG1655 is explicitly named for isolation from arsenite-treated, starved
    or HokB-induced cells. K12 UniProt reference entries are identity examples, not
    substituted MG1655-specific localization evidence. The record supplies no unwarranted
    prevalence estimate and does not promise liquid behavior for every bacterium or
    every aged protein aggregate.
  evidence_ids:
  - aggresome-agent-tax-83333
  - aggresome-agent-tax-511145
  - aggresome-agent-P0A6H5
  - aggresome-agent-P0AB77
  - aggresome-agent-P36683
  - aggresome-agent-PMC8528417
  - aggresome-agent-pei2025-aam
- assessment_id: mechanism
  area: graph
  topic: Six-edge RNA-protection mechanism
  outcome: supported
  target_ids:
  - cellstructuremech:bacterial_aggresome
  summary: 'The graph is mechanistic within its stated assays: RNA sequestration,
    restriction of tested RNases, active-versus-inactive RNase-entry controls, stress-removal
    release, preserved templates and renewed translation have direct experimental
    support. The record preserves the uncertainty about which material supplies the
    repulsive charge and does not generalize exclusion to all RNases; rRNA/tRNA-processing
    enzymes can be enriched.'
  evidence_ids:
  - aggresome-agent-pei2025-aam
- assessment_id: function
  area: evidence
  topic: RNA stabilization and recovery
  outcome: supported
  target_ids:
  - cellstructuremech:bacterial_aggresome
  summary: 'Preservation of selected mRNAs and their later cytoplasmic use fit GO:0048255.
    The rifampicin/tetracycline comparison separates new translation from maturation
    of existing fluorescent protein. The record correctly stops short of a universal
    survival edge: active RNase entry lengthens lag and increases persister fractions,
    while separate chemical inhibition of condensate formation reduces persistence.'
  evidence_ids:
  - aggresome-agent-go
  - aggresome-agent-pei2025-aam
- assessment_id: provenance
  area: provenance
  topic: Evidence tiers and attribution
  outcome: supported
  target_ids:
  - cellstructuremech:bacterial_aggresome
  summary: The cited2021 and2025 identities and experimental source extents are verified.
    The2025 full-body claims are assessed from the accepted manuscript, as the record
    states; publisher markup inspected for availability contains abstract/extended
    data rather than the main article body. Native databases establish their own identity
    assertions, while membership and mechanism remain grounded in the studies.
  evidence_ids:
  - aggresome-agent-doi-10.1126_sciadv.abh2929
  - aggresome-agent-doi-10.1038_s41564-025-02086-5
  - aggresome-agent-PMC8528417
  - aggresome-agent-pei2025-aam
  - aggresome-agent-P0A6H5
  - aggresome-agent-P0AB77
  - aggresome-agent-P36683
  - aggresome-agent-IPR004491
  - aggresome-agent-IPR011282
  - aggresome-agent-IPR004406
findings: []
actions: []
limitations:
- Jin2021 reading covered the three claim-bearing experimental Results subsections,
  Discussion, strain/construction Methods and included captions; the separate simulation
  section, original movies and raw tracking data were not reanalyzed.
- Pei2025 full-body evidence comes from the openly deposited accepted manuscript.
  Complete Main/Results/Discussion and the specified Methods were read, with Figures5
  and6 pixels inspected. The publisher response exposes abstract and extended-data
  material, not a readable main body; it is not used to inflate source access.
- Original RNA-seq/proteomics files, all videos, complete supplementary tables and
  mathematical supplementary derivations were not independently audited. Quantitative
  modeling assumptions do not become direct molecular observations.
- Assembly necessity for the listed components remains unknown. RNase exclusion is
  limited to the tested enzymes and interventions; neither every RNA nor every RNase
  behaves identically.
- Exact current family and reference-protein identities do not prove general bacterial
  prevalence, a fixed condensate composition or universal liquid-state properties.
  No local neighboring scientific YAML or new exhaustive ontology absence search informed
  this review.
- Initial network-restricted native protein verification failed from DNS resolution
  and was preserved. Public-network rerun and final protein/causal, schema and strict
  checks passed.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
