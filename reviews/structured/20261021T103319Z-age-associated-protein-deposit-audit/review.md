# Age-associated protein deposit identity, intervention and provenance review

- Review: 20261021T103319Z-age-associated-protein-deposit-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:13:04Z
- Finished UTC: 2026-10-21T10:33:19Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The record’s aging-deposit identity, bounded constituent set, experimental strain examples and four intervention-based graphs are supported. No concrete curation finding was established; assembly uncertainties, model boundaries and source-reading limits remain explicit.

## Scope And Provenance

Whole single-record claim review, all seven protein identities and current integrated family matches, four cited sources at the stated read tiers, four graphs, discussions, and the tracked image.

Selection: Batch19 index1; one maintained record in the frozen strict path-order selection. No neighboring scientific record used as evidential input.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:age_associated_protein_deposit | data/structures/inclusion/age_associated_protein_deposit.yaml | maintained | age-associated protein deposit |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | cellstructuremech:age_associated_protein_deposit | Target-specific native check passed. |
| Native protein causal-graphs | passed | True | cellstructuremech:age_associated_protein_deposit | Target-specific native check passed. |
| Focused native schema | passed | True | cellstructuremech:age_associated_protein_deposit | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:age_associated_protein_deposit | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:age_associated_protein_deposit | 19 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | cellstructuremech:age_associated_protein_deposit | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:age_associated_protein_deposit | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:age_associated_protein_deposit | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:age_associated_protein_deposit | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:age_associated_protein_deposit | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:age_associated_protein_deposit | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Local identity, nomenclature and compartment boundaries

identity: supported. Targets: cellstructuremech:age_associated_protein_deposit.

The local proposed aging-deposit identity and inclusion-body parent are supported. Agepod and APOD usage is source-grounded. ER association and the small-sample intranuclear observations do not justify exclusive cytoplasmic/nuclear parthood or an asserted equivalence to INQ. Current source comparison supports the record’s deliberately bounded distinctions; it does not reproduce the historical ontology-search counts.

### Observed components and minimal inventory

completeness: supported. Targets: cellstructuremech:age_associated_protein_deposit.

The variable client pool, small-HSP/Hsp70 cohorts, Hsp104, conditional Ydj1 enrichment and prion-state-dependent Sup35 cargo are supported as scoped. Hsp26 enrichment is limited, Ydj1 is not a universal coat, and Sup35 was recruited into pre-existing deposits without measurable potentiation of deposit formation by [PSI+] in the tested assay. The six rows form a supported subset; the source itself leaves the native client inventory unresolved, so omission of speculative constituents is not a completeness defect.

### Protein families versus individual accessions

grounding: supported. Targets: cellstructuremech:age_associated_protein_deposit.

The small-HSP, Hsp70 and Sup35/eRF3 families match their declared generic classes and example proteins. Complete native match sets do not supply an exact narrow Hsp104 or Ydj1-type class: the inspected ClpA/B and DnaJ-family names are broader. Retaining bounded label-only rows therefore does not automatically create a grounding finding. Protein example identities are correctly paired to S288C and do not imply every family member resides in the deposit.

### Assay-bounded formation and dispensability

evidence: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Hsp42-dependent normal deposit assembly, conditional small-HSP wording, and formation of Ssa1-marked deposits without Hsp104 support the record’s bounded assembly claims. Hsp26 deletion and Ssa1/Ssa2 single deletions must not be mistaken for a requirement of every family member or a double-mutant experiment. Sup35 presence is prion-state-dependent cargo, not a universal assembly requirement.

### Unresolved cohort assembly requirements

evidence: unknown. Targets: cellstructuremech:age_associated_protein_deposit.

Requirements for the heterogeneous client pool, entire Hsp70 cohort and Ydj1-type class remain unknown. Single-paralog perturbation and conditional localization do not establish necessity of the full class; Ydj1 deletion’s pleiotropy/fragmentation and C406S effects do not identify a required mature-deposit tether. The record retains these unknowns.

### Species and experimental strains

scope: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Species-level S.cerevisiae, the independently observed S288C background, and BY4741-derived2025 assays are valid distinct examples. Reviewed S288C protein identifiers identify reference sequences; they are not presented as evidence that every2017 assay used S288C or as lineage-wide prevalence.

### Chaperone and lineage intervention graphs

graph: supported. Targets: cellstructuremech:age_associated_protein_deposit.

The first two graphs encode experimentally perturbed formation/merger/lineage confinement rather than static parthood. Hsp42/Hsp104 opposition, separate Ssa1/Ssa2 deletions, mating/prm3 perturbation, and barrier/Ydj1-C406S effects are supported. New daughter deposition is kept separate from mature-deposit passage, bud6 has an actin confound, and Ydj1 precursor capture remains an explicit model.

### TOR and clearance graphs

graph: supported. Targets: cellstructuremech:age_associated_protein_deposit.

The aging-specific npr3/tco89 directions and young-versus-old rapamycin response are supported. Acute pro3-1 heat-stress translation/Hsf1 assays are not exported to the aging mechanism. The graph’s operational foci endpoint does not overclaim clearance by a particular biochemical route, and the cycloheximide-dose conflict is not silently normalized.

### Collection and asymmetric inheritance functions

evidence: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Concentration into predominantly singular mother-retained deposits and confinement of new deposition are supported in the tested yeast conditions. The record avoids turning lifespan associations, early/midlife stress handling or reporter turnover into universal fitness benefits of the deposit.

### Citation, image and source placement

provenance: supported. Targets: cellstructuremech:age_associated_protein_deposit.

All four cited paper identities are verified. The2018 review supplies only nomenclature; primary mechanistic claims use2015/2017/2025 bodies. Tracked Figure6 bytes, panel labels and native CC BY4.0 attribution are consistent. Historical curation access/search statements are not recertified as present-day exhaustive searches.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-identity | data/structures/inclusion/age_associated_protein_deposit.yaml; identifier; definition; mapping_status; identity discussion | context_only | Frozen target defines this local proposed structure identifier. The resolver deliberately skips repository-minted identifiers; primary-source and native-ontology checks independently assess the stated identity, without asserting an external exact match. |
| agepod-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016234,GO:0140453; results for GO:0016234 and GO:0140453: names, definitions, synonyms | supports | GO:0016234 defines inclusion body as an intracellular aggregate of molecules. GO:0140453 protein aggregate center instead denotes reversible thermosensitive-protein sequestration. This supports the broad parent and cautions against equating the local aging deposit with that stress-centered ontology term. |
| agepod-agent-PMC4635334 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4635334.1/PMC4635334.1.xml; JATS Results s2-1 through s2-7, Discussion s3, Methods s4; Figs1–7 and cited supplement captions; especially Fig1 supplement2, Fig6 and Fig6 supplement2 | supports | Primary study establishes age-associated Hsp104-marked deposits in budding yeast, mother retention, differential chaperone recruitment, bounded distinctness from stress foci/other inclusions, conditional Sup35 recruitment, and opposing Hsp42/Hsp104 perturbation effects. Figure6C separates SSA1 and SSA2 single deletions. Figure6 supplement2 shows deposits with Ssa1 reporter in hsp104 deletion; small speckles in the double mutant are distinguished from collected deposits. Lifespan pleiotropy and unresolved endogenous composition limit functional inference. |
| agepod-agent-saarikangas2017-aam | https://kclpure.kcl.ac.uk/ws/files/67186035/Saarikangas_et_al.pdf; King’s accepted manuscript: Summary/Introduction; complete Results and Discussion, printed pp3–15; Experimental Procedures pp15–16; Figure legends pp19–21; PDF pp35–36 Supplemental FigS5 pixels/caption; supplemental procedures and strain table PDF pp37–39 | supports | Accepted manuscript supports ER apposition, variable intranuclear localization, mating-deposit merging and impaired merging with homozygous prm3 deletion; barrier perturbations and Ydj1 C406S promote new daughter deposits without generally increasing passage of existing deposits. GFP-Ydj1 enrichment is 9.4% of 53 deposits; C406S preserves ER apposition and barrier function. Precursor capture by ER-bound Ydj1 remains a mechanistic model, not direct proof of a mature-deposit tether. |
| agepod-agent-PMC11849620 | https://pmc-oa-opendata.s3.amazonaws.com/PMC11849620.1/PMC11849620.1.xml; JATS Results sec1.1–sec1.3 with Figs1–5 captions; Experimental procedures sec2.1 strain/growth and sec2.4 old-cell isolation; Data availability sec3 | supports | Primary study distinguishes acute heat-stress pro3-1 assays from aging Hsp104-foci assays. In BY4741-derived aging cells, npr3 deletion accelerates foci and manually generated tco89 deletion suppresses them; an SGA isolate differs. Rapamycin/cycloheximide reduce young-cell foci, while old cells of median twelve divisions retain foci after rapamycin. Focus loss alone does not identify proteolysis versus refolding; the Figure5A/Methods cycloheximide-dose discrepancy remains visible. |
| agepod-agent-PMC6064742 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6064742.1/PMC6064742.1.xml; JATS Figure1 (F1) caption only | supports | This secondary review’s Figure1 caption explicitly calls the aging-cell site age-associated protein deposit site (APOD). It is used for nomenclature only, not as independent experimental support for the mechanism. |
| agepod-agent-doi-10.7554_eLife.06197 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554%2FeLife.06197&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString | supports | Exact native DOI metadata resolves PMID:26544680, Protein aggregates are associated with replicative aging without compromising protein quality control. (2015). Used to bind bibliographic identity, not substitute for the separately inspected body. |
| agepod-agent-doi-10.1016_j.cub.2017.01.069 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.cub.2017.01.069&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString | supports | Exact native DOI metadata resolves PMID:28262489, Compartmentalization of ER-Bound Chaperone Confines Protein Deposit Formation to the Aging Yeast Cell. (2017). Used to bind bibliographic identity, not substitute for the separately inspected body. |
| agepod-agent-doi-10.1016_j.jbc.2025.108172 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.jbc.2025.108172&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString | supports | Exact native DOI metadata resolves PMID:39798875, mTOR signaling controls protein aggregation during heat stress and cellular aging in a translation- and Hsf1-independent manner. (2025). Used to bind bibliographic identity, not substitute for the separately inspected body. |
| agepod-agent-doi-10.3389_fnmol.2018.00249 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffnmol.2018.00249&amp;format=json&amp;resultType=core; hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString | supports | Exact native DOI metadata resolves PMID:30083092, Studying Spatial Protein Quality Control, Proteopathies, and Aging Using Different Model Misfolding Proteins in &lt;i&gt;S. cerevisiae&lt;/i&gt;. (2018). Used to bind bibliographic identity, not substitute for the separately inspected body. |
| agepod-agent-Q12329 | https://rest.uniprot.org/uniprotkb/Q12329.json; primaryAccession; entryType; proteinDescription.recommendedName; genes; organism | supports | Native UniProtKB reviewed (Swiss-Prot) entry Q12329 identifies HSP42, Heat shock protein 42, in NCBITaxon:559292. This establishes accession/gene/taxon identity; deposit membership is evaluated from microscopy and interventions in the primary studies. |
| agepod-agent-P15992 | https://rest.uniprot.org/uniprotkb/P15992.json; primaryAccession; entryType; proteinDescription.recommendedName; genes; organism | supports | Native UniProtKB reviewed (Swiss-Prot) entry P15992 identifies HSP26, Heat shock protein 26, in NCBITaxon:559292. This establishes accession/gene/taxon identity; deposit membership is evaluated from microscopy and interventions in the primary studies. |
| agepod-agent-P31539 | https://rest.uniprot.org/uniprotkb/P31539.json; primaryAccession; entryType; proteinDescription.recommendedName; genes; organism | supports | Native UniProtKB reviewed (Swiss-Prot) entry P31539 identifies HSP104, Heat shock protein 104, in NCBITaxon:559292. This establishes accession/gene/taxon identity; deposit membership is evaluated from microscopy and interventions in the primary studies. |
| agepod-agent-P10591 | https://rest.uniprot.org/uniprotkb/P10591.json; primaryAccession; entryType; proteinDescription.recommendedName; genes; organism | supports | Native UniProtKB reviewed (Swiss-Prot) entry P10591 identifies SSA1, Heat shock protein SSA1, in NCBITaxon:559292. This establishes accession/gene/taxon identity; deposit membership is evaluated from microscopy and interventions in the primary studies. |
| agepod-agent-P10592 | https://rest.uniprot.org/uniprotkb/P10592.json; primaryAccession; entryType; proteinDescription.recommendedName; genes; organism | supports | Native UniProtKB reviewed (Swiss-Prot) entry P10592 identifies SSA2, Heat shock protein SSA2, in NCBITaxon:559292. This establishes accession/gene/taxon identity; deposit membership is evaluated from microscopy and interventions in the primary studies. |
| agepod-agent-P25491 | https://rest.uniprot.org/uniprotkb/P25491.json; primaryAccession; entryType; proteinDescription.recommendedName; genes; organism | supports | Native UniProtKB reviewed (Swiss-Prot) entry P25491 identifies YDJ1, Mitochondrial protein import protein MAS5, in NCBITaxon:559292. This establishes accession/gene/taxon identity; deposit membership is evaluated from microscopy and interventions in the primary studies. |
| agepod-agent-P05453 | https://rest.uniprot.org/uniprotkb/P05453.json; primaryAccession; entryType; proteinDescription.recommendedName; genes; organism | supports | Native UniProtKB reviewed (Swiss-Prot) entry P05453 identifies SUP35, Eukaryotic peptide chain release factor GTP-binding subunit, in NCBITaxon:559292. This establishes accession/gene/taxon identity; deposit membership is evaluated from microscopy and interventions in the primary studies. |
| agepod-agent-IPR031107 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031107/; metadata.accession; type; name; hierarchy | supports | Native InterPro family IPR031107: Small heat shock protein. Entry type, name and hierarchy delimit the sequence class; no localization or assembly-necessity conclusion is drawn from the family metadata. |
| agepod-agent-IPR013126 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013126/; metadata.accession; type; name; hierarchy | supports | Native InterPro family IPR013126: Heat shock protein 70 family. Entry type, name and hierarchy delimit the sequence class; no localization or assembly-necessity conclusion is drawn from the family metadata. |
| agepod-agent-IPR003285 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003285/; metadata.accession; type; name; hierarchy | supports | Native InterPro family IPR003285: Eukaryotic peptide chain release factor GTP-binding subunit. Entry type, name and hierarchy delimit the sequence class; no localization or assembly-necessity conclusion is drawn from the family metadata. |
| agepod-agent-IPR001270 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/; metadata.accession; type; name; hierarchy | supports | Native InterPro family IPR001270: ClpA/B family. Entry type, name and hierarchy delimit the sequence class; no localization or assembly-necessity conclusion is drawn from the family metadata. |
| agepod-agent-IPR050130 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/; metadata.accession; type; name; hierarchy | supports | Native InterPro family IPR050130: ATP-dependent Clp protease/Chaperone ClpA/ClpB. Entry type, name and hierarchy delimit the sequence class; no localization or assembly-necessity conclusion is drawn from the family metadata. |
| agepod-agent-ipr-matches-Q12329 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12329/?page_size=200; count; next; results[].metadata.accession/name/type | supports | Complete current integrated InterPro match response for Q12329: 3 entries, next=null. Family entries: IPR031107 Small heat shock protein. Domain, site and superfamily entries do not become exact whole-protein groundings. |
| agepod-agent-ipr-matches-P15992 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P15992/?page_size=200; count; next; results[].metadata.accession/name/type | supports | Complete current integrated InterPro match response for P15992: 3 entries, next=null. Family entries: IPR031107 Small heat shock protein. Domain, site and superfamily entries do not become exact whole-protein groundings. |
| agepod-agent-ipr-matches-P31539 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200; count; next; results[].metadata.accession/name/type | supports | Complete current integrated InterPro match response for P31539: 11 entries, next=null. Family entries: IPR001270 ClpA/B family; IPR050130 ATP-dependent Clp protease/Chaperone ClpA/ClpB. Domain, site and superfamily entries do not become exact whole-protein groundings. |
| agepod-agent-ipr-matches-P10591 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P10591/?page_size=200; count; next; results[].metadata.accession/name/type | supports | Complete current integrated InterPro match response for P10591: 5 entries, next=null. Family entries: IPR013126 Heat shock protein 70 family. Domain, site and superfamily entries do not become exact whole-protein groundings. |
| agepod-agent-ipr-matches-P10592 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P10592/?page_size=200; count; next; results[].metadata.accession/name/type | supports | Complete current integrated InterPro match response for P10592: 5 entries, next=null. Family entries: IPR013126 Heat shock protein 70 family. Domain, site and superfamily entries do not become exact whole-protein groundings. |
| agepod-agent-ipr-matches-P25491 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P25491/?page_size=200; count; next; results[].metadata.accession/name/type | supports | Complete current integrated InterPro match response for P25491: 9 entries, next=null. Family entries: IPR012724 Chaperone DnaJ; IPR044713 DnaJ homolog subfamily A member 1/2-like. Domain, site and superfamily entries do not become exact whole-protein groundings. |
| agepod-agent-ipr-matches-P05453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P05453/?page_size=200; count; next; results[].metadata.accession/name/type | supports | Complete current integrated InterPro match response for P05453: 9 entries, next=null. Family entries: IPR003285 Eukaryotic peptide chain release factor GTP-binding subunit; IPR050100 Translation factor GTPase superfamily members. Domain, site and superfamily entries do not become exact whole-protein groundings. |
| agepod-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId; scientificName; rank; otherNames | supports | Native taxonomy identifies NCBITaxon:4932 as Saccharomyces cerevisiae (rank species). Strain examples and reference-proteome identities remain distinct from general lineage prevalence. |
| agepod-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId; scientificName; rank; otherNames | supports | Native taxonomy identifies NCBITaxon:559292 as Saccharomyces cerevisiae S288C (rank strain). Strain examples and reference-proteome identities remain distinct from general lineage prevalence. |
| agepod-agent-tax-1247190 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1247190; taxId; scientificName; rank; otherNames | supports | Native taxonomy identifies NCBITaxon:1247190 as Saccharomyces cerevisiae BY4741 (rank strain). Strain examples and reference-proteome identities remain distinct from general lineage prevalence. |
| tracked-figure6 | data/images/inclusion/age_associated_protein_deposit/pmc4635334_fig6.jpg; Entire Figure6 visually inspected; particularly panelC individual mutant labels and panelsD–F overexpression series | context_only | The frozen tracked Figure6 distinguishes SSA1 and SSA2 single deletions and the opposing Hsp42/Hsp104 overexpression effects. Its actual bytes match the recorded SHA256; the JATS source identifies Figure6 and supplies the article’s CC BY4.0 permission. |
| agepod-figure6-license | https://pmc-oa-opendata.s3.amazonaws.com/PMC4635334.1/PMC4635334.1.xml; front/article-meta/permissions; fig[@id="fig6"] object-id, caption and graphic | supports | Article permissions explicitly grant Creative Commons Attribution4.0. Figure6 caption identifies chaperone-assembly panels A–G, source DOI10.7554/eLife.06197.011 and 5µm scale bars. This source licensing is consistent with the tracked-image attribution. |
| native-verify | /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml --verify; Captured native target-specific log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml --causal-graphs; Captured native target-specific log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/inclusion/age_associated_protein_deposit.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/inclusion/age_associated_protein_deposit.yaml |
| strict-result | just validate-strict data/structures/inclusion/age_associated_protein_deposit.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/age_associated_protein_deposit-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/inclusion/age_associated_protein_deposit.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/age_associated_protein_deposit-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/age_associated_protein_deposit-strict.tsv |
| target-curies | just check-curies-strict; data/structures/inclusion/age_associated_protein_deposit.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 19 of20 collected target identifiers returned OK in this fresh base resolver run. Residuals: cellstructuremech:age_associated_protein_deposit: SKIPPED; resolved by evidence local-identity. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- 2015 primary body reading covered all Results, Discussion and Methods and associated captions, with tracked Figure6 pixels inspected; Introduction, original videos, raw data and the strain workbook were not independently audited.
- 2017 evidence is the openly deposited accepted manuscript, not publisher version-of-record markup. Main Results/Discussion, figure legends, supplemental procedures/strain table and Supplemental Figure5 pixels/caption were inspected; other microscopy pixels and original movies were not comprehensively reanalyzed.
- 2025 reading covered claim-bearing Results sec1.1–sec1.3, Figures1–5 captions and specified Methods; raw data, all microscopy pixels and the unrelated huntingtin experiment were not audited. Focus loss does not distinguish degradation/refolding; the stated cycloheximide-dose discrepancy remains unresolved.
- 2018 review evidence is limited to Figure1 caption nomenclature. No new exhaustive ontology absence search or re-verification of historical search-hit totals was performed; no neighboring scientific YAML informed this judgment.
- Family-wide assembly requirements and full client inventory remain unknown where stated. Reviewed reference-proteome IDs do not change experimental strain boundaries.
- Initial network-restricted native protein verification failed from DNS resolution; original failure logs were retained. Rerun with public-network access and all final native protein/causal, schema and strict checks passed.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103319Z-age-associated-protein-deposit-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Age-associated protein deposit identity, intervention and provenance review
started_at: '2026-10-21T10:13:04Z'
finished_at: '2026-10-21T10:33:19Z'
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
summary: The record’s aging-deposit identity, bounded constituent set, experimental
  strain examples and four intervention-based graphs are supported. No concrete curation
  finding was established; assembly uncertainties, model boundaries and source-reading
  limits remain explicit.
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
  - path: data/images/inclusion/age_associated_protein_deposit/pmc4635334_fig6.jpg
    sha256: abf686034f035ecdf81b1c3fb79c1504412f436b4c695c07bbcfc31525f8d74a
    role: context
  - path: data/structures/inclusion/age_associated_protein_deposit.yaml
    sha256: f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30
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
- target_id: cellstructuremech:age_associated_protein_deposit
  path: data/structures/inclusion/age_associated_protein_deposit.yaml
  label: age-associated protein deposit
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/age_associated_protein_deposit.yaml
    role: maintained scientific record
scope:
  description: Whole single-record claim review, all seven protein identities and
    current integrated family matches, four cited sources at the stated read tiers,
    four graphs, discussions, and the tracked image.
  selection: Batch19 index1; one maintained record in the frozen strict path-order
    selection. No neighboring scientific record used as evidential input.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:age_associated_protein_deposit
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  command: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml
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
  - cellstructuremech:age_associated_protein_deposit
  command: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml
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
  - cellstructuremech:age_associated_protein_deposit
  command: just validate data/structures/inclusion/age_associated_protein_deposit.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  command: just validate-strict data/structures/inclusion/age_associated_protein_deposit.yaml
    --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/age_associated_protein_deposit-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: 19 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - local-identity
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - local-identity
  - agepod-agent-go
  - agepod-agent-PMC4635334
  - agepod-agent-saarikangas2017-aam
  - agepod-agent-PMC11849620
  - agepod-agent-PMC6064742
  - agepod-agent-doi-10.7554_eLife.06197
  - agepod-agent-doi-10.1016_j.cub.2017.01.069
  - agepod-agent-doi-10.1016_j.jbc.2025.108172
  - agepod-agent-doi-10.3389_fnmol.2018.00249
  - agepod-agent-Q12329
  - agepod-agent-P15992
  - agepod-agent-P31539
  - agepod-agent-P10591
  - agepod-agent-P10592
  - agepod-agent-P25491
  - agepod-agent-P05453
  - agepod-agent-IPR031107
  - agepod-agent-IPR013126
  - agepod-agent-IPR003285
  - agepod-agent-IPR001270
  - agepod-agent-IPR050130
  - agepod-agent-ipr-matches-Q12329
  - agepod-agent-ipr-matches-P15992
  - agepod-agent-ipr-matches-P31539
  - agepod-agent-ipr-matches-P10591
  - agepod-agent-ipr-matches-P10592
  - agepod-agent-ipr-matches-P25491
  - agepod-agent-ipr-matches-P05453
  - agepod-agent-tax-4932
  - agepod-agent-tax-559292
  - agepod-agent-tax-1247190
  - tracked-figure6
  - agepod-figure6-license
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
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
  - cellstructuremech:age_associated_protein_deposit
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
  - cellstructuremech:age_associated_protein_deposit
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
  - cellstructuremech:age_associated_protein_deposit
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
  - cellstructuremech:age_associated_protein_deposit
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
  reference: data/structures/inclusion/age_associated_protein_deposit.yaml
  locator: identifier; definition; mapping_status; identity discussion
  accessed_at: '2026-10-21T10:23:15Z'
  support: context_only
  summary: Frozen target defines this local proposed structure identifier. The resolver
    deliberately skips repository-minted identifiers; primary-source and native-ontology
    checks independently assess the stated identity, without asserting an external
    exact match.
  snapshot_sha256: f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30
- evidence_id: agepod-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016234,GO:0140453
  locator: 'results for GO:0016234 and GO:0140453: names, definitions, synonyms'
  accessed_at: '2026-10-21T10:15:27.994155Z'
  support: supports
  summary: GO:0016234 defines inclusion body as an intracellular aggregate of molecules.
    GO:0140453 protein aggregate center instead denotes reversible thermosensitive-protein
    sequestration. This supports the broad parent and cautions against equating the
    local aging deposit with that stress-centered ontology term.
  snapshot_sha256: 5ed653a30c1d3cf06157d105229a124a0f231addc56690c29a6c1662f367c0ca
- evidence_id: agepod-agent-PMC4635334
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4635334.1/PMC4635334.1.xml
  locator: JATS Results s2-1 through s2-7, Discussion s3, Methods s4; Figs1–7 and
    cited supplement captions; especially Fig1 supplement2, Fig6 and Fig6 supplement2
  accessed_at: '2026-10-21T10:15:26.810788Z'
  support: supports
  summary: Primary study establishes age-associated Hsp104-marked deposits in budding
    yeast, mother retention, differential chaperone recruitment, bounded distinctness
    from stress foci/other inclusions, conditional Sup35 recruitment, and opposing
    Hsp42/Hsp104 perturbation effects. Figure6C separates SSA1 and SSA2 single deletions.
    Figure6 supplement2 shows deposits with Ssa1 reporter in hsp104 deletion; small
    speckles in the double mutant are distinguished from collected deposits. Lifespan
    pleiotropy and unresolved endogenous composition limit functional inference.
  snapshot_sha256: e8931b516ea7c92b41da19c7df230bed7c0d1f390d5c4edd5a31bbacfda0ab0c
- evidence_id: agepod-agent-saarikangas2017-aam
  kind: primary_source
  reference: https://kclpure.kcl.ac.uk/ws/files/67186035/Saarikangas_et_al.pdf
  locator: 'King’s accepted manuscript: Summary/Introduction; complete Results and
    Discussion, printed pp3–15; Experimental Procedures pp15–16; Figure legends pp19–21;
    PDF pp35–36 Supplemental FigS5 pixels/caption; supplemental procedures and strain
    table PDF pp37–39'
  accessed_at: '2026-10-21T10:15:27.613162Z'
  support: supports
  summary: Accepted manuscript supports ER apposition, variable intranuclear localization,
    mating-deposit merging and impaired merging with homozygous prm3 deletion; barrier
    perturbations and Ydj1 C406S promote new daughter deposits without generally increasing
    passage of existing deposits. GFP-Ydj1 enrichment is 9.4% of 53 deposits; C406S
    preserves ER apposition and barrier function. Precursor capture by ER-bound Ydj1
    remains a mechanistic model, not direct proof of a mature-deposit tether.
  snapshot_sha256: 576956a462e6c327ebc2de0ff00dca884f53466eaa9f2693a533cae981d64097
- evidence_id: agepod-agent-PMC11849620
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11849620.1/PMC11849620.1.xml
  locator: JATS Results sec1.1–sec1.3 with Figs1–5 captions; Experimental procedures
    sec2.1 strain/growth and sec2.4 old-cell isolation; Data availability sec3
  accessed_at: '2026-10-21T10:15:26.812589Z'
  support: supports
  summary: Primary study distinguishes acute heat-stress pro3-1 assays from aging
    Hsp104-foci assays. In BY4741-derived aging cells, npr3 deletion accelerates foci
    and manually generated tco89 deletion suppresses them; an SGA isolate differs.
    Rapamycin/cycloheximide reduce young-cell foci, while old cells of median twelve
    divisions retain foci after rapamycin. Focus loss alone does not identify proteolysis
    versus refolding; the Figure5A/Methods cycloheximide-dose discrepancy remains
    visible.
  snapshot_sha256: e086c564436b4d9ad6f43a78ad8a5e4058e0e979c55b37a5a6bfb0791e8a96b6
- evidence_id: agepod-agent-PMC6064742
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6064742.1/PMC6064742.1.xml
  locator: JATS Figure1 (F1) caption only
  accessed_at: '2026-10-21T10:15:26.814578Z'
  support: supports
  summary: This secondary review’s Figure1 caption explicitly calls the aging-cell
    site age-associated protein deposit site (APOD). It is used for nomenclature only,
    not as independent experimental support for the mechanism.
  snapshot_sha256: d2d06af7ae94f495609e14e3cde3c072264d5a30bb84ddf83c06389e72040941
- evidence_id: agepod-agent-doi-10.7554_eLife.06197
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554%2FeLife.06197&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString
  accessed_at: '2026-10-21T10:15:26.816306Z'
  support: supports
  summary: Exact native DOI metadata resolves PMID:26544680, Protein aggregates are
    associated with replicative aging without compromising protein quality control.
    (2015). Used to bind bibliographic identity, not substitute for the separately
    inspected body.
  snapshot_sha256: 1e70c86ea74f4a8f3646d537cec7e65ff7610bcd314697eebf98572b56d3e438
- evidence_id: agepod-agent-doi-10.1016_j.cub.2017.01.069
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.cub.2017.01.069&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString
  accessed_at: '2026-10-21T10:15:26.817944Z'
  support: supports
  summary: Exact native DOI metadata resolves PMID:28262489, Compartmentalization
    of ER-Bound Chaperone Confines Protein Deposit Formation to the Aging Yeast Cell.
    (2017). Used to bind bibliographic identity, not substitute for the separately
    inspected body.
  snapshot_sha256: d4cc8563836adac0160a8919ec3541b983a1eeb746ec3168e7c5c2ef34020f02
- evidence_id: agepod-agent-doi-10.1016_j.jbc.2025.108172
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.jbc.2025.108172&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString
  accessed_at: '2026-10-21T10:15:26.816194Z'
  support: supports
  summary: Exact native DOI metadata resolves PMID:39798875, mTOR signaling controls
    protein aggregation during heat stress and cellular aging in a translation- and
    Hsf1-independent manner. (2025). Used to bind bibliographic identity, not substitute
    for the separately inspected body.
  snapshot_sha256: faaab48ebb0ae0752adaafdd32f191182ae5024a0f445a104b4e0b829a2d0855
- evidence_id: agepod-agent-doi-10.3389_fnmol.2018.00249
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffnmol.2018.00249&format=json&resultType=core
  locator: hitCount=1; resultList.result[0] id/title/doi/pubYear/authorString
  accessed_at: '2026-10-21T10:15:26.816952Z'
  support: supports
  summary: Exact native DOI metadata resolves PMID:30083092, Studying Spatial Protein
    Quality Control, Proteopathies, and Aging Using Different Model Misfolding Proteins
    in <i>S. cerevisiae</i>. (2018). Used to bind bibliographic identity, not substitute
    for the separately inspected body.
  snapshot_sha256: 2e7846c093ed16feb37ea2ceb99d48d273dc37157c96c886c389b7a685030fd9
- evidence_id: agepod-agent-Q12329
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12329.json
  locator: primaryAccession; entryType; proteinDescription.recommendedName; genes;
    organism
  accessed_at: '2026-10-21T10:15:28.493398Z'
  support: supports
  summary: Native UniProtKB reviewed (Swiss-Prot) entry Q12329 identifies HSP42, Heat
    shock protein 42, in NCBITaxon:559292. This establishes accession/gene/taxon identity;
    deposit membership is evaluated from microscopy and interventions in the primary
    studies.
  snapshot_sha256: 2fd80fe65790b403d51e6d01659e4c94ec91a1455e5b4be00301e2350656a1cc
- evidence_id: agepod-agent-P15992
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P15992.json
  locator: primaryAccession; entryType; proteinDescription.recommendedName; genes;
    organism
  accessed_at: '2026-10-21T10:15:28.623471Z'
  support: supports
  summary: Native UniProtKB reviewed (Swiss-Prot) entry P15992 identifies HSP26, Heat
    shock protein 26, in NCBITaxon:559292. This establishes accession/gene/taxon identity;
    deposit membership is evaluated from microscopy and interventions in the primary
    studies.
  snapshot_sha256: cbaa80ed16718c9eb01d31f4ae461fe665e1390d99bccaee7d6a277c4352b523
- evidence_id: agepod-agent-P31539
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P31539.json
  locator: primaryAccession; entryType; proteinDescription.recommendedName; genes;
    organism
  accessed_at: '2026-10-21T10:15:28.994133Z'
  support: supports
  summary: Native UniProtKB reviewed (Swiss-Prot) entry P31539 identifies HSP104,
    Heat shock protein 104, in NCBITaxon:559292. This establishes accession/gene/taxon
    identity; deposit membership is evaluated from microscopy and interventions in
    the primary studies.
  snapshot_sha256: 8636decea760cdb2a2da238bfa589822867a778a41fd6a04c45a74fe5802ee13
- evidence_id: agepod-agent-P10591
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P10591.json
  locator: primaryAccession; entryType; proteinDescription.recommendedName; genes;
    organism
  accessed_at: '2026-10-21T10:15:29.362375Z'
  support: supports
  summary: Native UniProtKB reviewed (Swiss-Prot) entry P10591 identifies SSA1, Heat
    shock protein SSA1, in NCBITaxon:559292. This establishes accession/gene/taxon
    identity; deposit membership is evaluated from microscopy and interventions in
    the primary studies.
  snapshot_sha256: 7459cff48ea4a5bb0deb45f6da0f61e77cf00ee2168622b6ea7af8949890b64e
- evidence_id: agepod-agent-P10592
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P10592.json
  locator: primaryAccession; entryType; proteinDescription.recommendedName; genes;
    organism
  accessed_at: '2026-10-21T10:15:29.513983Z'
  support: supports
  summary: Native UniProtKB reviewed (Swiss-Prot) entry P10592 identifies SSA2, Heat
    shock protein SSA2, in NCBITaxon:559292. This establishes accession/gene/taxon
    identity; deposit membership is evaluated from microscopy and interventions in
    the primary studies.
  snapshot_sha256: 45fb36c0787ae44ba78e30b21c47ae26f4ab816e781a732073171c4a70e269f6
- evidence_id: agepod-agent-P25491
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P25491.json
  locator: primaryAccession; entryType; proteinDescription.recommendedName; genes;
    organism
  accessed_at: '2026-10-21T10:15:29.745871Z'
  support: supports
  summary: Native UniProtKB reviewed (Swiss-Prot) entry P25491 identifies YDJ1, Mitochondrial
    protein import protein MAS5, in NCBITaxon:559292. This establishes accession/gene/taxon
    identity; deposit membership is evaluated from microscopy and interventions in
    the primary studies.
  snapshot_sha256: 9d11d2a3ddb00c55584a3469c546628b4c7a1e5986e9d3dbd8ecba60f5af8d3b
- evidence_id: agepod-agent-P05453
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P05453.json
  locator: primaryAccession; entryType; proteinDescription.recommendedName; genes;
    organism
  accessed_at: '2026-10-21T10:15:30.018770Z'
  support: supports
  summary: Native UniProtKB reviewed (Swiss-Prot) entry P05453 identifies SUP35, Eukaryotic
    peptide chain release factor GTP-binding subunit, in NCBITaxon:559292. This establishes
    accession/gene/taxon identity; deposit membership is evaluated from microscopy
    and interventions in the primary studies.
  snapshot_sha256: 220c5b10197e36ddf025b193e782fac495ad6d399f1b624d769c5b62a36af85a
- evidence_id: agepod-agent-IPR031107
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031107/
  locator: metadata.accession; type; name; hierarchy
  accessed_at: '2026-10-21T10:15:30.788260Z'
  support: supports
  summary: 'Native InterPro family IPR031107: Small heat shock protein. Entry type,
    name and hierarchy delimit the sequence class; no localization or assembly-necessity
    conclusion is drawn from the family metadata.'
  snapshot_sha256: 7db6f5da4dd897dfbcaa6435cbeb744a4691f43cb10433977995a30bb1d91293
- evidence_id: agepod-agent-IPR013126
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013126/
  locator: metadata.accession; type; name; hierarchy
  accessed_at: '2026-10-21T10:15:30.917612Z'
  support: supports
  summary: 'Native InterPro family IPR013126: Heat shock protein 70 family. Entry
    type, name and hierarchy delimit the sequence class; no localization or assembly-necessity
    conclusion is drawn from the family metadata.'
  snapshot_sha256: 43e5cb816d24b41f9660bca2ce79602ba65d8013352745427fc0fb1f4a3a6d9c
- evidence_id: agepod-agent-IPR003285
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003285/
  locator: metadata.accession; type; name; hierarchy
  accessed_at: '2026-10-21T10:15:31.022158Z'
  support: supports
  summary: 'Native InterPro family IPR003285: Eukaryotic peptide chain release factor
    GTP-binding subunit. Entry type, name and hierarchy delimit the sequence class;
    no localization or assembly-necessity conclusion is drawn from the family metadata.'
  snapshot_sha256: 0b72fb273b4c505328a072ea7a047466f31f35fbb0507a93530de22f27c0cc3e
- evidence_id: agepod-agent-IPR001270
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/
  locator: metadata.accession; type; name; hierarchy
  accessed_at: '2026-10-21T10:15:31.115090Z'
  support: supports
  summary: 'Native InterPro family IPR001270: ClpA/B family. Entry type, name and
    hierarchy delimit the sequence class; no localization or assembly-necessity conclusion
    is drawn from the family metadata.'
  snapshot_sha256: ed0a09c17fa611e58cd0d00b904d4dce2757228cd7e411301eddcfb9b391e0dd
- evidence_id: agepod-agent-IPR050130
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/
  locator: metadata.accession; type; name; hierarchy
  accessed_at: '2026-10-21T10:15:31.421976Z'
  support: supports
  summary: 'Native InterPro family IPR050130: ATP-dependent Clp protease/Chaperone
    ClpA/ClpB. Entry type, name and hierarchy delimit the sequence class; no localization
    or assembly-necessity conclusion is drawn from the family metadata.'
  snapshot_sha256: e654bc8d2d359d203a225be0690247071616a63341156fcd507f197717f78701
- evidence_id: agepod-agent-ipr-matches-Q12329
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12329/?page_size=200
  locator: count; next; results[].metadata.accession/name/type
  accessed_at: '2026-10-21T10:15:28.547223Z'
  support: supports
  summary: 'Complete current integrated InterPro match response for Q12329: 3 entries,
    next=null. Family entries: IPR031107 Small heat shock protein. Domain, site and
    superfamily entries do not become exact whole-protein groundings.'
  snapshot_sha256: b5fd5350c5ea8e5ac5d6bdda8ab01a8f4ab0036d09974a5a02fce9361203a6a2
- evidence_id: agepod-agent-ipr-matches-P15992
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P15992/?page_size=200
  locator: count; next; results[].metadata.accession/name/type
  accessed_at: '2026-10-21T10:15:28.644197Z'
  support: supports
  summary: 'Complete current integrated InterPro match response for P15992: 3 entries,
    next=null. Family entries: IPR031107 Small heat shock protein. Domain, site and
    superfamily entries do not become exact whole-protein groundings.'
  snapshot_sha256: 2a832a0014d7563f99c26af41dd62810eda86625e204d5e0bed963bcec7b6d04
- evidence_id: agepod-agent-ipr-matches-P31539
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200
  locator: count; next; results[].metadata.accession/name/type
  accessed_at: '2026-10-21T10:15:29.150971Z'
  support: supports
  summary: 'Complete current integrated InterPro match response for P31539: 11 entries,
    next=null. Family entries: IPR001270 ClpA/B family; IPR050130 ATP-dependent Clp
    protease/Chaperone ClpA/ClpB. Domain, site and superfamily entries do not become
    exact whole-protein groundings.'
  snapshot_sha256: 750867aa538d4dd5c6c6a982138e7401b8b788d9653ecb84bf5d145c8ff6d3ee
- evidence_id: agepod-agent-ipr-matches-P10591
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P10591/?page_size=200
  locator: count; next; results[].metadata.accession/name/type
  accessed_at: '2026-10-21T10:15:29.367300Z'
  support: supports
  summary: 'Complete current integrated InterPro match response for P10591: 5 entries,
    next=null. Family entries: IPR013126 Heat shock protein 70 family. Domain, site
    and superfamily entries do not become exact whole-protein groundings.'
  snapshot_sha256: 19cd7491705e3561a05df7016c70c1091734040f5815bfc16f04ecdfcd59b082
- evidence_id: agepod-agent-ipr-matches-P10592
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P10592/?page_size=200
  locator: count; next; results[].metadata.accession/name/type
  accessed_at: '2026-10-21T10:15:29.671527Z'
  support: supports
  summary: 'Complete current integrated InterPro match response for P10592: 5 entries,
    next=null. Family entries: IPR013126 Heat shock protein 70 family. Domain, site
    and superfamily entries do not become exact whole-protein groundings.'
  snapshot_sha256: b78ecf727cc28004c68ea1a1b954adad836011894a71c3e845f14a11d2565952
- evidence_id: agepod-agent-ipr-matches-P25491
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P25491/?page_size=200
  locator: count; next; results[].metadata.accession/name/type
  accessed_at: '2026-10-21T10:15:30.006050Z'
  support: supports
  summary: 'Complete current integrated InterPro match response for P25491: 9 entries,
    next=null. Family entries: IPR012724 Chaperone DnaJ; IPR044713 DnaJ homolog subfamily
    A member 1/2-like. Domain, site and superfamily entries do not become exact whole-protein
    groundings.'
  snapshot_sha256: 7dafb7f8631f188fc8cf64685b0db62424c61885dddefdd8ff979e543782b431
- evidence_id: agepod-agent-ipr-matches-P05453
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P05453/?page_size=200
  locator: count; next; results[].metadata.accession/name/type
  accessed_at: '2026-10-21T10:15:30.171153Z'
  support: supports
  summary: 'Complete current integrated InterPro match response for P05453: 9 entries,
    next=null. Family entries: IPR003285 Eukaryotic peptide chain release factor GTP-binding
    subunit; IPR050100 Translation factor GTPase superfamily members. Domain, site
    and superfamily entries do not become exact whole-protein groundings.'
  snapshot_sha256: 15dbf9ca4f9076cdf87ce83dcbfb2081a2d2120e028bfe885c6591223ac294a3
- evidence_id: agepod-agent-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId; scientificName; rank; otherNames
  accessed_at: '2026-10-21T10:15:30.282122Z'
  support: supports
  summary: Native taxonomy identifies NCBITaxon:4932 as Saccharomyces cerevisiae (rank
    species). Strain examples and reference-proteome identities remain distinct from
    general lineage prevalence.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: agepod-agent-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId; scientificName; rank; otherNames
  accessed_at: '2026-10-21T10:15:30.380033Z'
  support: supports
  summary: Native taxonomy identifies NCBITaxon:559292 as Saccharomyces cerevisiae
    S288C (rank strain). Strain examples and reference-proteome identities remain
    distinct from general lineage prevalence.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: agepod-agent-tax-1247190
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1247190
  locator: taxId; scientificName; rank; otherNames
  accessed_at: '2026-10-21T10:15:30.502764Z'
  support: supports
  summary: Native taxonomy identifies NCBITaxon:1247190 as Saccharomyces cerevisiae
    BY4741 (rank strain). Strain examples and reference-proteome identities remain
    distinct from general lineage prevalence.
  snapshot_sha256: caee974f39d598c4001a51c78b0dc0c7dfba575de9526277d845019da6abe202
- evidence_id: tracked-figure6
  kind: record_content
  reference: data/images/inclusion/age_associated_protein_deposit/pmc4635334_fig6.jpg
  locator: Entire Figure6 visually inspected; particularly panelC individual mutant
    labels and panelsD–F overexpression series
  accessed_at: '2026-10-21T10:23:15Z'
  support: context_only
  summary: The frozen tracked Figure6 distinguishes SSA1 and SSA2 single deletions
    and the opposing Hsp42/Hsp104 overexpression effects. Its actual bytes match the
    recorded SHA256; the JATS source identifies Figure6 and supplies the article’s
    CC BY4.0 permission.
  snapshot_sha256: abf686034f035ecdf81b1c3fb79c1504412f436b4c695c07bbcfc31525f8d74a
- evidence_id: agepod-figure6-license
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4635334.1/PMC4635334.1.xml
  locator: front/article-meta/permissions; fig[@id="fig6"] object-id, caption and
    graphic
  accessed_at: '2026-10-21T10:15:26.810788Z'
  support: supports
  summary: Article permissions explicitly grant Creative Commons Attribution4.0. Figure6
    caption identifies chaperone-assembly panels A–G, source DOI10.7554/eLife.06197.011
    and 5µm scale bars. This source licensing is consistent with the tracked-image
    attribution.
  snapshot_sha256: e8931b516ea7c92b41da19c7df230bed7c0d1f390d5c4edd5a31bbacfda0ab0c
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml
    --verify
  locator: Captured native target-specific log
  accessed_at: '2026-10-21T10:17:03.429816Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml
    --causal-graphs
  locator: Captured native target-specific log
  accessed_at: '2026-10-21T10:17:06.041204Z'
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
  reference: just validate data/structures/inclusion/age_associated_protein_deposit.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:06Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/inclusion/age_associated_protein_deposit.yaml'
  snapshot_sha256: e9ef93e900a0b7480a466e4afc6619cd0d5c814d40e450b4cbf856cf10658464
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/inclusion/age_associated_protein_deposit.yaml
    --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/age_associated_protein_deposit-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:08Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/inclusion/age_associated_protein_deposit.yaml\
    \ --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/age_associated_protein_deposit-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/age_associated_protein_deposit-strict.tsv"
  snapshot_sha256: 7582f1f98fdbd9edcc1aa08c02f1a6269bfc7133f9a98b8de55475213f82d3b4
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/inclusion/age_associated_protein_deposit.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:23:15Z'
  support: supports
  summary: '19 of20 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: cellstructuremech:age_associated_protein_deposit: SKIPPED; resolved
    by evidence local-identity. Source-native identity checked separately.'
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
  topic: Local identity, nomenclature and compartment boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: The local proposed aging-deposit identity and inclusion-body parent are
    supported. Agepod and APOD usage is source-grounded. ER association and the small-sample
    intranuclear observations do not justify exclusive cytoplasmic/nuclear parthood
    or an asserted equivalence to INQ. Current source comparison supports the record’s
    deliberately bounded distinctions; it does not reproduce the historical ontology-search
    counts.
  evidence_ids:
  - local-identity
  - agepod-agent-go
  - agepod-agent-PMC4635334
  - agepod-agent-saarikangas2017-aam
  - agepod-agent-PMC11849620
  - agepod-agent-PMC6064742
- assessment_id: composition
  area: completeness
  topic: Observed components and minimal inventory
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: The variable client pool, small-HSP/Hsp70 cohorts, Hsp104, conditional
    Ydj1 enrichment and prion-state-dependent Sup35 cargo are supported as scoped.
    Hsp26 enrichment is limited, Ydj1 is not a universal coat, and Sup35 was recruited
    into pre-existing deposits without measurable potentiation of deposit formation
    by [PSI+] in the tested assay. The six rows form a supported subset; the source
    itself leaves the native client inventory unresolved, so omission of speculative
    constituents is not a completeness defect.
  evidence_ids:
  - agepod-agent-PMC4635334
  - agepod-agent-saarikangas2017-aam
  - agepod-agent-Q12329
  - agepod-agent-P15992
  - agepod-agent-P31539
  - agepod-agent-P10591
  - agepod-agent-P10592
  - agepod-agent-P25491
  - agepod-agent-P05453
- assessment_id: grounding
  area: grounding
  topic: Protein families versus individual accessions
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: 'The small-HSP, Hsp70 and Sup35/eRF3 families match their declared generic
    classes and example proteins. Complete native match sets do not supply an exact
    narrow Hsp104 or Ydj1-type class: the inspected ClpA/B and DnaJ-family names are
    broader. Retaining bounded label-only rows therefore does not automatically create
    a grounding finding. Protein example identities are correctly paired to S288C
    and do not imply every family member resides in the deposit.'
  evidence_ids:
  - agepod-agent-Q12329
  - agepod-agent-P15992
  - agepod-agent-P31539
  - agepod-agent-P10591
  - agepod-agent-P10592
  - agepod-agent-P25491
  - agepod-agent-P05453
  - agepod-agent-IPR031107
  - agepod-agent-IPR013126
  - agepod-agent-IPR003285
  - agepod-agent-IPR001270
  - agepod-agent-IPR050130
  - agepod-agent-ipr-matches-Q12329
  - agepod-agent-ipr-matches-P15992
  - agepod-agent-ipr-matches-P31539
  - agepod-agent-ipr-matches-P10591
  - agepod-agent-ipr-matches-P10592
  - agepod-agent-ipr-matches-P25491
  - agepod-agent-ipr-matches-P05453
- assessment_id: necessity-supported
  area: evidence
  topic: Assay-bounded formation and dispensability
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Hsp42-dependent normal deposit assembly, conditional small-HSP wording,
    and formation of Ssa1-marked deposits without Hsp104 support the record’s bounded
    assembly claims. Hsp26 deletion and Ssa1/Ssa2 single deletions must not be mistaken
    for a requirement of every family member or a double-mutant experiment. Sup35
    presence is prion-state-dependent cargo, not a universal assembly requirement.
  evidence_ids:
  - agepod-agent-PMC4635334
  - tracked-figure6
- assessment_id: necessity-unknown
  area: evidence
  topic: Unresolved cohort assembly requirements
  outcome: unknown
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Requirements for the heterogeneous client pool, entire Hsp70 cohort and
    Ydj1-type class remain unknown. Single-paralog perturbation and conditional localization
    do not establish necessity of the full class; Ydj1 deletion’s pleiotropy/fragmentation
    and C406S effects do not identify a required mature-deposit tether. The record
    retains these unknowns.
  evidence_ids:
  - agepod-agent-PMC4635334
  - agepod-agent-saarikangas2017-aam
- assessment_id: taxa
  area: scope
  topic: Species and experimental strains
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Species-level S.cerevisiae, the independently observed S288C background,
    and BY4741-derived2025 assays are valid distinct examples. Reviewed S288C protein
    identifiers identify reference sequences; they are not presented as evidence that
    every2017 assay used S288C or as lineage-wide prevalence.
  evidence_ids:
  - agepod-agent-PMC4635334
  - agepod-agent-saarikangas2017-aam
  - agepod-agent-PMC11849620
  - agepod-agent-tax-4932
  - agepod-agent-tax-559292
  - agepod-agent-tax-1247190
  - agepod-agent-Q12329
  - agepod-agent-P15992
  - agepod-agent-P31539
  - agepod-agent-P10591
  - agepod-agent-P10592
  - agepod-agent-P25491
  - agepod-agent-P05453
- assessment_id: graphs-assembly
  area: graph
  topic: Chaperone and lineage intervention graphs
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: The first two graphs encode experimentally perturbed formation/merger/lineage
    confinement rather than static parthood. Hsp42/Hsp104 opposition, separate Ssa1/Ssa2
    deletions, mating/prm3 perturbation, and barrier/Ydj1-C406S effects are supported.
    New daughter deposition is kept separate from mature-deposit passage, bud6 has
    an actin confound, and Ydj1 precursor capture remains an explicit model.
  evidence_ids:
  - agepod-agent-PMC4635334
  - agepod-agent-saarikangas2017-aam
  - tracked-figure6
- assessment_id: graphs-aging
  area: graph
  topic: TOR and clearance graphs
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: The aging-specific npr3/tco89 directions and young-versus-old rapamycin
    response are supported. Acute pro3-1 heat-stress translation/Hsf1 assays are not
    exported to the aging mechanism. The graph’s operational foci endpoint does not
    overclaim clearance by a particular biochemical route, and the cycloheximide-dose
    conflict is not silently normalized.
  evidence_ids:
  - agepod-agent-PMC11849620
- assessment_id: functions
  area: evidence
  topic: Collection and asymmetric inheritance functions
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Concentration into predominantly singular mother-retained deposits and
    confinement of new deposition are supported in the tested yeast conditions. The
    record avoids turning lifespan associations, early/midlife stress handling or
    reporter turnover into universal fitness benefits of the deposit.
  evidence_ids:
  - agepod-agent-PMC4635334
  - agepod-agent-saarikangas2017-aam
  - agepod-agent-PMC11849620
- assessment_id: provenance
  area: provenance
  topic: Citation, image and source placement
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: All four cited paper identities are verified. The2018 review supplies only
    nomenclature; primary mechanistic claims use2015/2017/2025 bodies. Tracked Figure6
    bytes, panel labels and native CC BY4.0 attribution are consistent. Historical
    curation access/search statements are not recertified as present-day exhaustive
    searches.
  evidence_ids:
  - agepod-agent-doi-10.7554_eLife.06197
  - agepod-agent-doi-10.1016_j.cub.2017.01.069
  - agepod-agent-doi-10.1016_j.jbc.2025.108172
  - agepod-agent-doi-10.3389_fnmol.2018.00249
  - agepod-agent-PMC6064742
  - agepod-agent-PMC4635334
  - agepod-agent-saarikangas2017-aam
  - agepod-agent-PMC11849620
  - tracked-figure6
  - agepod-figure6-license
findings: []
actions: []
limitations:
- 2015 primary body reading covered all Results, Discussion and Methods and associated
  captions, with tracked Figure6 pixels inspected; Introduction, original videos,
  raw data and the strain workbook were not independently audited.
- 2017 evidence is the openly deposited accepted manuscript, not publisher version-of-record
  markup. Main Results/Discussion, figure legends, supplemental procedures/strain
  table and Supplemental Figure5 pixels/caption were inspected; other microscopy pixels
  and original movies were not comprehensively reanalyzed.
- 2025 reading covered claim-bearing Results sec1.1–sec1.3, Figures1–5 captions and
  specified Methods; raw data, all microscopy pixels and the unrelated huntingtin
  experiment were not audited. Focus loss does not distinguish degradation/refolding;
  the stated cycloheximide-dose discrepancy remains unresolved.
- 2018 review evidence is limited to Figure1 caption nomenclature. No new exhaustive
  ontology absence search or re-verification of historical search-hit totals was performed;
  no neighboring scientific YAML informed this judgment.
- Family-wide assembly requirements and full client inventory remain unknown where
  stated. Reviewed reference-proteome IDs do not change experimental strain boundaries.
- Initial network-restricted native protein verification failed from DNS resolution;
  original failure logs were retained. Rerun with public-network access and all final
  native protein/causal, schema and strict checks passed.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
