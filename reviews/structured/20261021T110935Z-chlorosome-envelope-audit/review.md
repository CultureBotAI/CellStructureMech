# Chlorosome envelope composition, assembly necessity and source-context audit

- Review: 20261021T110935Z-chlorosome-envelope-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:51:39Z
- Finished UTC: 2026-10-21T11:09:35Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Identity, non-bilayer boundary, protein examples and bounded light-harvesting organization are supported. One major finding concerns the unqualified CsmA-baseplate formation-essentiality label.

## Scope And Provenance

Entire exact target and its frozen local baseplate identity dependency, with all components, examples, six graph edges and current discussion.

Selection: Batch22 index8; one entire maintained record at frozen main9c0446.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033105 | data/structures/membrane_organelle/chlorosome_envelope.yaml | maintained | chlorosome envelope |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native verify | passed | True | GO:0033105 | Native command passed0; coverage labels remain descriptive, not automatic scientific defects. |
| Focused native causal-graphs | passed | True | GO:0033105 | Native command passed0; coverage labels remain descriptive, not automatic scientific defects. |
| Focused native schema | passed | True | GO:0033105 | Focused validator passed. |
| Focused native strict | passed | True | GO:0033105 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0033105 | 22 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0033105 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0033105 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0033105 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0033105 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0033105 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0033105 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact whole structure and part boundary

identity: supported. Targets: GO:0033105.

The exact GO identity and envelope parthood, synonyms and UniProt location cross-reference are supported; the envelope is a glycolipid/protein surface, not a bilayer organelle membrane. OTHER is compatible with the represented non-bilayer structure. The baseplate component resolves to the frozen local complex.

### Membrane material, pigment organization and Csm membership

evidence: supported. Targets: GO:0033105.

The collective monolayer is a constitutional boundary. The glycolipid mixture differs from the whole envelope GO class, so its label-only material row is not automatically an omitted exact envelope mapping. The CsmA–BChl a array and heterogeneous accessory proteins are supported. Broader protein families and individual homolog matches must not replace the complete cohort with an inexact single identity.

### Unqualified baseplate assembly-essentiality

evidence: concern. Targets: GO:0033105.

The baseplate row asserts ESSENTIAL formation necessity across the target class. The cited sources establish membership, structure, excitation transfer and CsmA viability/segregation constraints in C. tepidum; they do not isolate formation of this target after baseplate loss. This is a bounded unsupported necessity assertion (F1), not evidence that the baseplate is dispensable. Nielsen2016 also explicitly assigns a structural-integrity function in its Introduction; the concern does not deny that role.

### Collective definitions, individual subunits and mutant boundaries

evidence: unknown. Targets: GO:0033105.

Accessory cohort UNKNOWN is appropriate: single deletions do not establish requirements of the whole cohort across taxa. Individual lipid requirements are not established. The envelope study does not demonstrate formation necessity of every embedded protein.

### Bacterial variability and exact experimental context

scope: supported. Targets: GO:0033105.

VARIABLE Bacteria does not assert broad bacterial occurrence. Primary examples are C. tepidum and C. aurantiacus; old Chlorobium naming is a native synonym. Nielsen uses bchK-mutant carotenosomes plus wild-type comparisons; primary AFM measurements mentioned in that work are from earlier studies. No altered carotenosome is silently described as an unmodified experimental sample.

### Ten taxon-paired examples and bounded missing mapping

evidence: supported. Targets: GO:0033105.

All ten supplied accessions, gene/locus identities, taxon and reviewed/unreviewed states match. Native verification passes. CsmK has published protein membership despite no result for the narrow exact-symbol query; its optional missing protein example is not a finding.

### Six directed function edges and source levels

graph: supported. Targets: GO:0033105.

The NONMECHANISTIC envelope graph accurately states parthood, glycolipid boundary, accessory surface localization, aggregate enclosure and baseplate positioning toward light harvesting. It does not claim an exhaustive contact network. Downstream FMO/B808–866 and reaction-center details vary by lineage; no universal single acceptor accession or exhaustive inventory is forced.

### Claim-specific sources and acknowledged inventory boundaries

completeness: supported. Targets: GO:0033105.

All citations identify the intended works. The2004 deletion study and2006 cross-linking abstract establish different experiments and do not include a CsmK knockout. The2013 review supplies the broader protein cohort. The existing grouped material/protein rows, local baseplate reference and open exact-grounding questions are meaningful; no automatic finding follows from omitted carotenoid/quinone rows or absent optional examples.

## Findings

### F1: Separate CsmA baseplate function and viability from formation necessity

major / open / confirmed; issue key: chlorosome_envelope-baseplate-assembly-necessity.

The CsmA-baseplate component is marked ESSENTIAL, which the schema defines in terms of whether the target structure forms without it. Nielsen2016 resolves a baseplate in bchK-mutant carotenosomes and compares wild-type/mutant structure; it does not remove the baseplate to test formation. Frigaard2004 reports failure of csmA transformants to segregate under its growth conditions and interprets possible essential light harvesting/viability, while the nine non-CsmA deletions retain chlorosomes. These results cannot by themselves assign an unqualified formation requirement to the baseplate across this bacterial structure class. Preserve the well-supported constituent and antenna roles, but qualify or withhold the assembly-necessity assertion unless a direct, appropriately scoped formation result is supplied. This finding does not say the baseplate is dispensable or treat vestigial pigment-free remnants as normal chlorosomes. Nielsen2016 explicitly assigns structural integrity as a baseplate function in its Introduction; retain this positive structural role while separating it from a tested universal requirement for formation.

## Recommended Actions And Acceptance Checks

### A1

Revise the CsmA-baseplate formation-necessity annotation or attach direct source evidence at the relevant taxon and experimental scope.

- Keep the supported baseplate constituent identity, structural-integrity role and light-harvesting role.
- Use UNKNOWN or an appropriately qualified necessity state unless inspected evidence tests target formation after the relevant component loss.
- Do not substitute failed mutant segregation, viability or excitation-transfer loss for an assembly endpoint; retain the modified-carotenosome versus normal-chlorosome boundary.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/chlorosome_envelope.yaml; Entire YAML, all ten protein examples, six graph edges, current discussion and complete history | context_only | The whole target was inspected separately. Chlorosome and envelope boundaries, source annotations, protein identity-only roles and scope qualifiers were retained. |
| baseplate-record | data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml; Entire frozen local record; identifier, label, definition and part_of used to resolve the local substructure reference | context_only | The exact local-minted identifier denotes the CsmA–BChl a baseplate complex and is part of both chlorosome and envelope. The sibling is used for local identity, not as independent proof of its unresolved scientific claims. |
| schema-necessity | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent.essentiality and EssentialityEnum | context_only | Essentiality concerns whether the structure forms without the component; it is not an alias for importance in light harvesting or cell viability. |
| policy | docs/CURATION.md; Composition, essentiality and evidence-scope guidance | context_only | Keep component membership, formation necessity and function distinct. Do not force exact family groundings for heterogeneous cohorts or infer absence from an empty optional field. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Directed function/assembly paths and experimental-context rubric | context_only | A mechanistic label requires a meaningful directed functional path; topology or cell viability alone is not a formation experiment. |
| protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Taxon-paired protein identity and evidence boundaries | context_only | Accession identity is separate from structure membership. Reviewed and unreviewed entries retain their native statuses. |
| chlorosome-envelope-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046858,GO:0043232,GO:0033105,GO:0015979; Complete requested identity, definitions, synonyms, comments and relevant child relations | supports | All four requested GO terms are active. GO0046858 is a child of intracellular membraneless organelle GO0043232, whose definition excludes a lipid bilayer, and lists GO0033105 part_of. The envelope definition specifies glycolipid monolayer with proteins; its comment explicitly excludes bilayer-envelope parentage. GO0015979 correctly names photosynthesis. |
| chlorosome-envelope-agent-SL-0060 | https://rest.uniprot.org/locations/SL-0060.json; id/name/definition/synonyms/geneOntologies/partOf; no statistics used | supports | SL0060 maps chlorosome envelope to GO0033105 and has synonym Chlorosomal envelope and partOf chlorosome. It describes an asymmetric galactolipid-containing surface in green sulfur bacteria; pigment-tail contribution to an inner leaflet is explicitly probable, not established universal bilayer architecture. |
| chlorosome-envelope-agent-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; taxId/scientificName/rank/lineage/otherNames | supports | Native taxonomy identifies Bacteria domain. Names in older papers are valid synonyms, not organism mismatches. |
| chlorosome-envelope-agent-tax-1097 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1097; taxId/scientificName/rank/lineage/otherNames | supports | Native taxonomy identifies Chlorobaculum tepidum species, including Chlorobium tepidum synonym. Names in older papers are valid synonyms, not organism mismatches. |
| chlorosome-envelope-agent-tax-1108 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1108; taxId/scientificName/rank/lineage/otherNames | supports | Native taxonomy identifies Chloroflexus aurantiacus species. Names in older papers are valid synonyms, not organism mismatches. |
| chlorosome-envelope-agent-tax-194439 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/194439; taxId/scientificName/rank/lineage/otherNames | supports | Native taxonomy identifies Chlorobaculum tepidum TLS strain, including Chlorobium tepidum TLS synonym. Names in older papers are valid synonyms, not organism mismatches. |
| chlorosome-envelope-agent-orf2013-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s11120-013-9869-3; resultList.result[0] citation/author/year and complete abstractText | supports | Exact native citation and complete abstract inspected: PMID23761131, DOI10.1007/s11120-013-9869-3, Chlorosome antenna complexes from green photosynthetic bacteria. This is secondary-review bibliographic/abstract scope. |
| chlorosome-envelope-agent-oostergetel2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s11120-010-9533-0; resultList.result[0] citation/author/year and complete abstractText | supports | Exact native citation and complete abstract inspected: PMID20130996, DOI10.1007/s11120-010-9533-0, The chlorosome: a prototype for efficient light harvesting in photosynthesis. This is secondary-review bibliographic/abstract scope. |
| chlorosome-envelope-agent-psencik2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/JB.00690-09; resultList.result[0] citation/author/year and complete abstractText | supports | Exact native citation and complete abstract inspected: PMID19717605, DOI10.1128/jb.00690-09, Structure of chlorosomes from the green filamentous bacterium Chloroflexus aurantiacus. This metadata/abstract receipt is distinct from any independently inspected full body. |
| chlorosome-envelope-agent-nielsen2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/ncomms12454; resultList.result[0] citation/author/year and complete abstractText | supports | Exact native citation and complete abstract inspected: PMID27534696, DOI10.1038/ncomms12454, In situ high-resolution structure of the baseplate antenna complex in Chlorobaculum tepidum. This metadata/abstract receipt is distinct from any independently inspected full body. |
| chlorosome-envelope-agent-frigaard2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.186.3.646-653.2004&amp;format=json&amp;resultType=core; resultList.result[0] citation/author/year and complete abstractText | supports | Exact native citation and complete abstract inspected: PMID14729689, DOI10.1128/jb.186.3.646-653.2004, Nine mutants of Chlorobium tepidum each unable to synthesize a different chlorosome protein still assemble functional chlorosomes. This metadata/abstract receipt is distinct from any independently inspected full body. |
| chlorosome-envelope-agent-li2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1021%2Fbi060776y&amp;format=json&amp;resultType=core; resultList.result[0] citation/author/year and complete abstractText | supports | Exact native citation and complete abstract inspected: PMID16866355, DOI10.1021/bi060776y, Molecular contacts for chlorosome envelope proteins revealed by cross-linking studies with chlorosomes from Chlorobium tepidum. This metadata/abstract receipt is distinct from any independently inspected full body. |
| chlorosome-envelope-agent-frigaard2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007/s11120-005-1331-8&amp;format=json&amp;resultType=core; resultList.result[0] citation/author/year and complete abstractText | supports | Exact native citation and complete abstract inspected: PMID16172929, DOI10.1007/s11120-005-1331-8, Isolation and characterization of carotenosomes from a bacteriochlorophyll c-less mutant of Chlorobium tepidum. This metadata/abstract receipt is distinct from any independently inspected full body. |
| chlorosome-envelope-agent-nielsen2016-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4992139.1/PMC4992139.1.xml; All unsectioned Introduction; complete Results and Discussion; Methods Sample preparation including bchK growth, isolation and ssNMR; embedded captions. No raw spectra, microscopy pixels, supplements or full computational-method reanalysis. | supports | The high-resolution baseplate model combines ssNMR, spectroscopy and lower-resolution cryo-EM from bchK-mutant carotenosomes lacking BChl c. Wild-type/mutant freeze-fracture comparisons support conserved baseplate architecture. The intact functional baseplate in this modified organelle does not itself test formation after CsmA/baseplate removal. AFM dimensions discussed are from earlier work, not a new AFM experiment here. The Introduction explicitly attributes a structural-integrity role to the baseplate; this positive structural function is acknowledged separately from an isolated experimental test of universal formation necessity. |
| chlorosome-envelope-agent-psencik2009-pmc-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC2795307/; Methods sec1–sec2; all Results sec3–sec8 including Table1/captions; Discussion sec10 overall dimensions, sec12 perpendicular striation and sec13 summary. Other Discussion subsections not claimed as fully audited; no figure pixels/raw-data reanalysis. | supports | The primary C. aurantiacus J-10-fl study combines pigment analysis, cryo-EM/tomography and X-ray scattering. It attributes parallel striation to lamellar pigment organization and a regular one-face lattice to the baseplate. A CsmA dimer building block is an inference from lattice size and prior work, not atomic identification in this study. Residual cellular membranes are explicitly recognized as contamination. |
| chlorosome-envelope-agent-oostergetel2010-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2882566.1/PMC2882566.1.xml; Sec1 Introduction; Sec2 Chlorosomes; Sec3 supramolecular organization; Sec5 baseplate; Sec7 spectroscopic properties in relation to function; embedded captions. Sec4/Sec8 and complete reference list not exhaustively audited. | supports | This review supports chlorosome occurrence in three bacterial groups, a non-bilayer envelope, pigment self-assembly and the pigment-to-baseplate-to-downstream-antenna/RC excitation route. It distinguishes FMO and B808–866 acceptors, species-dependent kinetics, and inferred structural models. It is secondary synthesis, not a new intervention experiment. |
| chlorosome-envelope-agent-frigaard2004-ncbi | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC321489/; Introduction; all Methods sec1–sec6, Results sec7–sec11 and Discussion sec12; Tables1/2 and all embedded captions. No microscopy pixels, blot pixels or raw-data reanalysis. Genuine legacy PMC HTML, unlike earlier challenge responses. | supports | Nine separate non-CsmA gene disruptions retain chlorosomes with broadly similar composition and function, with specific size/pigment/growth effects. csmA transformants remain merodiploid under tested growth conditions; the authors infer a possible essential role in light harvesting and discuss lethality/difficulty of deletion. This does not directly establish universal chlorosome or envelope formation necessity. Individual deletions do not test complete cohort removal. |
| chlorosome-envelope-agent-orf2013-browser-body | https://www.researchgate.net/publication/237199940_Chlorosome_Antenna_Complexes_from_Green_Photosynthetic_Bacteria; Author-uploaded review browser capture: Introduction and Chlorosome proteins and the CsmA baseplate pp322–323; preceding carotenoid/quinone context. Native publisher200 contains abstract/references only; this is not a complete review-body audit. | supports | The review explicitly lists up to eleven Chlorobi protein types including CsmK, distinct motif families and lineage-dependent membership. It discusses carotenosomes and differentiates CsmA viability importance from structural characterization. Browser-captured secondary text, not native HTTP200. |
| chlorosome-envelope-agent-P0A314 | https://rest.uniprot.org/uniprotkb/P0A314.json; primaryAccession/entryType/proteinDescription/genes/organism | supports | Native P0A314 is reviewed, gene csmA, in tax194439 Chlorobaculum tepidum TLS. Gene/locus, native protein name, organism and entry status match the identity-only example. The historical native name Bacteriochlorophyll c-binding protein is retained as the source label; it is not used to override the experimentally established BChl a baseplate role. |
| chlorosome-envelope-agent-Q46383 | https://rest.uniprot.org/uniprotkb/Q46383.json; primaryAccession/entryType/proteinDescription/genes/organism | supports | Native Q46383 is reviewed, gene csmB, in tax194439 Chlorobaculum tepidum TLS. Gene/locus, native protein name, organism and entry status match the identity-only example. Identity evidence is not treated as an independent membership experiment. |
| chlorosome-envelope-agent-Q46367 | https://rest.uniprot.org/uniprotkb/Q46367.json; primaryAccession/entryType/proteinDescription/genes/organism | supports | Native Q46367 is reviewed, gene csmC, in tax194439 Chlorobaculum tepidum TLS. Gene/locus, native protein name, organism and entry status match the identity-only example. Identity evidence is not treated as an independent membership experiment. |
| chlorosome-envelope-agent-Q46386 | https://rest.uniprot.org/uniprotkb/Q46386.json; primaryAccession/entryType/proteinDescription/genes/organism | supports | Native Q46386 is reviewed, gene csmE, in tax194439 Chlorobaculum tepidum TLS. Gene/locus, native protein name, organism and entry status match the identity-only example. Identity evidence is not treated as an independent membership experiment. |
| chlorosome-envelope-agent-O68986 | https://rest.uniprot.org/uniprotkb/O68986.json; primaryAccession/entryType/proteinDescription/genes/organism | supports | Native O68986 is reviewed, gene csmF, in tax194439 Chlorobaculum tepidum TLS. Gene/locus, native protein name, organism and entry status match the identity-only example. Identity evidence is not treated as an independent membership experiment. |
| chlorosome-envelope-agent-O68988 | https://rest.uniprot.org/uniprotkb/O68988.json; primaryAccession/entryType/proteinDescription/genes/organism | supports | Native O68988 is reviewed, gene csmI, in tax194439 Chlorobaculum tepidum TLS. Gene/locus, native protein name, organism and entry status match the identity-only example. Identity evidence is not treated as an independent membership experiment. |
| chlorosome-envelope-agent-O68983 | https://rest.uniprot.org/uniprotkb/O68983.json; primaryAccession/entryType/proteinDescription/genes/organism | supports | Native O68983 is reviewed, gene csmJ, in tax194439 Chlorobaculum tepidum TLS. Gene/locus, native protein name, organism and entry status match the identity-only example. Identity evidence is not treated as an independent membership experiment. |
| chlorosome-envelope-agent-H2VFJ4 | https://rest.uniprot.org/uniprotkb/H2VFJ4.json; primaryAccession/entryType/proteinDescription/genes/organism | supports | Native H2VFJ4 is unreviewed, gene csmD, in tax194439 Chlorobaculum tepidum TLS. Gene/locus, native protein name, organism and entry status match the identity-only example. Identity evidence is not treated as an independent membership experiment. |
| chlorosome-envelope-agent-H2VFJ1 | https://rest.uniprot.org/uniprotkb/H2VFJ1.json; primaryAccession/entryType/proteinDescription/genes/organism | supports | Native H2VFJ1 is unreviewed, gene csmH, in tax194439 Chlorobaculum tepidum TLS. Gene/locus, native protein name, organism and entry status match the identity-only example. Identity evidence is not treated as an independent membership experiment. |
| chlorosome-envelope-agent-Q8KEN5 | https://rest.uniprot.org/uniprotkb/Q8KEN5.json; primaryAccession/entryType/proteinDescription/genes/organism | supports | Native Q8KEN5 is unreviewed, gene csmX, in tax194439 Chlorobaculum tepidum TLS. Gene/locus, native protein name, organism and entry status match the identity-only example. Identity evidence is not treated as an independent membership experiment. |
| chlorosome-envelope-agent-reviewed-csm-query | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A194439+AND+%28gene_exact%3AcsmA+OR+gene_exact%3AcsmB+OR+gene_exact%3AcsmC+OR+gene_exact%3AcsmD+OR+gene_exact%3AcsmE+OR+gene_exact%3AcsmF+OR+gene_exact%3AcsmH+OR+gene_exact%3AcsmI+OR+gene_exact%3AcsmJ+OR+gene_exact%3AcsmK+OR+gene_exact%3AcsmX%29&amp;format=json&amp;size=500; Complete result accession/gene/status/taxon projection; X-Total-Results7 and no next-page link | supports | The complete exact reviewed tax194439 query for the eleven declared csm symbols returns seven reviewed entries matching A/B/C/E/F/I/J; the three separately verified unreviewed examples remain unreviewed. The query does not justify inventing a reviewed CsmK accession. |
| chlorosome-envelope-agent-csmK-query | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AcsmK&amp;format=json&amp;size=500; Exact query gene_exact:csmK; complete results and X-Total-Results0 | context_only | This bounded exact-symbol UniProt query returns zero entries. It does not refute the independently readable published CsmK protein membership or prove the protein/gene absent; no accession is fabricated. |
| chlorosome-envelope-agent-matches-P0A314 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P0A314/; Complete count/next and all result metadata accession/name/type; no downstream functional or localization inference | supports | The exact P0A314 match endpoint reports G3DSA:1.20.5.950 bacteriochlorophyll c-binding protein (homologous_superfamily); IPR001470 Bacteriochlorophyll c-binding protein (family); IPR038387 Bacteriochlorophyll c-binding superfamily (homologous_superfamily); PF02043 Bacteriochlorophyll C binding protein (family); PIRSF002903 Chlorosome protein, CsmA/CsmE types (family); PR00656 BCHLROPHYLLC (family). These per-protein assignments do not alone establish an exact family for the complete accessory cohort. |
| chlorosome-envelope-agent-matches-Q46383 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46383/?page_size=200; Complete count/next and all result metadata accession/name/type; no downstream functional or localization inference | supports | The exact Q46383 match endpoint reports IPR059980 CsmB chlorosome envelope protein (family). These per-protein assignments do not alone establish an exact family for the complete accessory cohort. |
| chlorosome-envelope-agent-matches-Q46367 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46367/?page_size=200; Complete count/next and all result metadata accession/name/type; no downstream functional or localization inference | supports | The exact Q46367 match endpoint reports IPR020995 Chlorosome envelope protein C (family). These per-protein assignments do not alone establish an exact family for the complete accessory cohort. |
| chlorosome-envelope-agent-matches-Q46386 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46386/?page_size=200; Complete count/next and all result metadata accession/name/type; no downstream functional or localization inference | supports | The exact Q46386 match endpoint reports IPR001470 Bacteriochlorophyll c-binding protein (family); IPR038387 Bacteriochlorophyll c-binding superfamily (homologous_superfamily). These per-protein assignments do not alone establish an exact family for the complete accessory cohort. |
| chlorosome-envelope-agent-matches-O68986 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68986/?page_size=200; Complete count/next and all result metadata accession/name/type; no downstream functional or localization inference | supports | The exact O68986 match endpoint reports IPR059980 CsmB chlorosome envelope protein (family). These per-protein assignments do not alone establish an exact family for the complete accessory cohort. |
| chlorosome-envelope-agent-matches-O68988 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68988/?page_size=200; Complete count/next and all result metadata accession/name/type; no downstream functional or localization inference | supports | The exact O68988 match endpoint reports IPR001041 2Fe-2S ferredoxin-type iron-sulfur binding domain (domain); IPR001055 Adrenodoxin-like (family); IPR012675 Beta-grasp domain superfamily (homologous_superfamily); IPR036010 2Fe-2S ferredoxin-like superfamily (homologous_superfamily). These per-protein assignments do not alone establish an exact family for the complete accessory cohort. |
| chlorosome-envelope-agent-matches-O68983 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68983/?page_size=200; Complete count/next and all result metadata accession/name/type; no downstream functional or localization inference | supports | The exact O68983 match endpoint reports IPR001041 2Fe-2S ferredoxin-type iron-sulfur binding domain (domain); IPR001055 Adrenodoxin-like (family); IPR012675 Beta-grasp domain superfamily (homologous_superfamily); IPR036010 2Fe-2S ferredoxin-like superfamily (homologous_superfamily). These per-protein assignments do not alone establish an exact family for the complete accessory cohort. |
| chlorosome-envelope-agent-matches-H2VFJ4 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/H2VFJ4/?page_size=200; Native endpoint HTTP204 with zero-byte body; no JSON result or family absence inferred | context_only | The exact H2VFJ4 match endpoint supplied no content. This limits the family check and is not evidence of biological absence. |
| chlorosome-envelope-agent-matches-H2VFJ1 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/H2VFJ1/?page_size=200; Complete count/next and all result metadata accession/name/type; no downstream functional or localization inference | supports | The exact H2VFJ1 match endpoint reports IPR017845 Chlorosome envelope protein H, CsmH (repeat); IPR040561 Large polyvalent protein associated domain 38 (domain). These per-protein assignments do not alone establish an exact family for the complete accessory cohort. |
| chlorosome-envelope-agent-matches-Q8KEN5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8KEN5/?page_size=200; Complete count/next and all result metadata accession/name/type; no downstream functional or localization inference | supports | The exact Q8KEN5 match endpoint reports IPR001041 2Fe-2S ferredoxin-type iron-sulfur binding domain (domain); IPR001055 Adrenodoxin-like (family); IPR012675 Beta-grasp domain superfamily (homologous_superfamily); IPR036010 2Fe-2S ferredoxin-like superfamily (homologous_superfamily). These per-protein assignments do not alone establish an exact family for the complete accessory cohort. |
| native-verify | /private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml --verify; Complete focused native output including coverage categories | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml --causal-graphs; Complete focused native output including coverage categories | supports | data/structures/membrane_organelle/chlorosome_envelope.yaml  (GO:0033105)<br>  chlorosome_envelope_light_harvesting_topology	csm_envelope_proteins	PARTIAL_EXAMPLES	-&gt;csm_envelope_proteins (have: UniProtKB:Q46383, UniProtKB:Q46367, UniProtKB:Q46386, UniProtKB:O68986, UniProtKB:O68988, UniProtKB:O68983, UniProtKB:H2VFJ4, UniProtKB:H2VFJ1, UniProtKB:Q8KEN5; missing: csmK)<br>  chlorosome_envelope_light_harvesting_topology	csma_baseplate	COVERED	-&gt;csma_baseplate (UniProtKB:P0A314)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/chlorosome_envelope.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/chlorosome_envelope.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/chlorosome_envelope.yaml --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/chlorosome_envelope-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/chlorosome_envelope.yaml --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/chlorosome_envelope-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch22-20261021-xfifxerh/chlorosome_envelope-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/chlorosome_envelope.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 22 of24 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:14729689: UNREACHABLE; resolved by evidence chlorosome-envelope-agent-frigaard2004-meta; cellstructuremech:chlorosome_baseplate_antenna_complex: SKIPPED; resolved by evidence baseplate-record. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Nielsen2016 is genuine full JATS read at the declared Introduction/Results/Discussion and sample-preparation Methods scope. Its high-resolution model uses bchK-mutant carotenosomes, with wild-type/mutant comparisons; AFM dimensions cited there derive from earlier work. No raw NMR, cryo-EM pixels, supplements or complete computational pipeline were independently reanalyzed.
- Psencik2009 genuine HTML Methods and Results plus the specified Discussion subsections were read. Lattice-based CsmA dimer assignment is an inference supported by prior work. No raw tomography, spectra or microscopy pixels were reanalyzed.
- Frigaard2004 genuine legacy PMC body was read through Introduction, Methods, Results, Discussion and table/figure captions. Earlier canonical HTML200 was a challenge, S3 returned404 and EPMC XML500; those failures remain in the packet and are not cited as bodies.
- Orf2013 native publisher/PDF routes returned abstract/reference HTML, not a readable PDF/main body. Actual author-uploaded Introduction/protein-baseplate passages were read through a browser capture with status:null. Oostergetel2010 was read as secondary synthesis at the stated sections; neither is recast as a new primary experiment.
- Li2006 was verified through exact native metadata and its complete primary abstract; publisher full text403. The abstract supports cross-linking and proposed contact models, but no full Methods audit is claimed. Frigaard2005 was read only at exact metadata/complete abstract scope for the vestigial-carotenosome boundary.
- The gene/family search is bounded to named examples, their match endpoints and the exact csmK symbol query. H2VFJ4 returned HTTP204 with no content. This does not prove family/protein absence; individual motifs or broader CsmA/E and ferredoxin families do not exactly denote the whole accessory set.
- Assembly necessity remains distinct from composition and light-harvesting function. The collective monolayer is constitutional; individual lipids and the complete accessory cohort have no universal necessity conclusion here. Modified or vestigial pigment-free organelles are not equated with unchanged normal chlorosomes.
- No images or structural datasets are maintained on either target. Figure captions in sources were read as text; no image licence, pixel measurements or raw experimental data audit is claimed.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110935Z-chlorosome-envelope-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Chlorosome envelope composition, assembly necessity and source-context audit
started_at: '2026-10-21T10:51:39Z'
finished_at: '2026-10-21T11:09:35Z'
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
summary: Identity, non-bilayer boundary, protein examples and bounded light-harvesting
  organization are supported. One major finding concerns the unqualified CsmA-baseplate
  formation-essentiality label.
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
  - path: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    sha256: 7ea00dedcd0998fc477737d6d2e8301e4e57a08e57378d19efe5e32a6ea8c92d
    role: context
  - path: data/structures/membrane_organelle/chlorosome_envelope.yaml
    sha256: 2514acd0c5f9bd7c73e1c1d77096301858323dbfe5fa35434b09c501b5fbf8ed
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
- target_id: GO:0033105
  path: data/structures/membrane_organelle/chlorosome_envelope.yaml
  label: chlorosome envelope
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chlorosome_envelope.yaml
    role: maintained scientific record
scope:
  description: Entire exact target and its frozen local baseplate identity dependency,
    with all components, examples, six graph edges and current discussion.
  selection: Batch22 index8; one entire maintained record at frozen main9c0446.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033105
checks:
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0033105
  command: /private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml
    --verify
  exit_code: 0
  summary: Native command passed0; coverage labels remain descriptive, not automatic
    scientific defects.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0033105
  command: /private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml
    --causal-graphs
  exit_code: 0
  summary: Native command passed0; coverage labels remain descriptive, not automatic
    scientific defects.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0033105
  command: just validate data/structures/membrane_organelle/chlorosome_envelope.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0033105
  command: just validate-strict data/structures/membrane_organelle/chlorosome_envelope.yaml
    --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/chlorosome_envelope-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0033105
  summary: 22 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - chlorosome-envelope-agent-frigaard2004-meta
  - baseplate-record
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0033105
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - baseplate-record
  - schema-necessity
  - policy
  - graph-policy
  - protein-policy
  - chlorosome-envelope-agent-go
  - chlorosome-envelope-agent-SL-0060
  - chlorosome-envelope-agent-tax-2
  - chlorosome-envelope-agent-tax-1097
  - chlorosome-envelope-agent-tax-1108
  - chlorosome-envelope-agent-tax-194439
  - chlorosome-envelope-agent-orf2013-meta
  - chlorosome-envelope-agent-oostergetel2010-meta
  - chlorosome-envelope-agent-psencik2009-meta
  - chlorosome-envelope-agent-nielsen2016-meta
  - chlorosome-envelope-agent-frigaard2004-meta
  - chlorosome-envelope-agent-li2006-meta
  - chlorosome-envelope-agent-frigaard2005-meta
  - chlorosome-envelope-agent-nielsen2016-jats
  - chlorosome-envelope-agent-psencik2009-pmc-html
  - chlorosome-envelope-agent-oostergetel2010-jats
  - chlorosome-envelope-agent-frigaard2004-ncbi
  - chlorosome-envelope-agent-orf2013-browser-body
  - chlorosome-envelope-agent-P0A314
  - chlorosome-envelope-agent-Q46383
  - chlorosome-envelope-agent-Q46367
  - chlorosome-envelope-agent-Q46386
  - chlorosome-envelope-agent-O68986
  - chlorosome-envelope-agent-O68988
  - chlorosome-envelope-agent-O68983
  - chlorosome-envelope-agent-H2VFJ4
  - chlorosome-envelope-agent-H2VFJ1
  - chlorosome-envelope-agent-Q8KEN5
  - chlorosome-envelope-agent-reviewed-csm-query
  - chlorosome-envelope-agent-csmK-query
  - chlorosome-envelope-agent-matches-P0A314
  - chlorosome-envelope-agent-matches-Q46383
  - chlorosome-envelope-agent-matches-Q46367
  - chlorosome-envelope-agent-matches-Q46386
  - chlorosome-envelope-agent-matches-O68986
  - chlorosome-envelope-agent-matches-O68988
  - chlorosome-envelope-agent-matches-O68983
  - chlorosome-envelope-agent-matches-H2VFJ4
  - chlorosome-envelope-agent-matches-H2VFJ1
  - chlorosome-envelope-agent-matches-Q8KEN5
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0033105
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
  - GO:0033105
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
  - GO:0033105
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
  - GO:0033105
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
  - GO:0033105
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
  reference: data/structures/membrane_organelle/chlorosome_envelope.yaml
  locator: Entire YAML, all ten protein examples, six graph edges, current discussion
    and complete history
  accessed_at: '2026-10-21T11:00:58Z'
  support: context_only
  summary: The whole target was inspected separately. Chlorosome and envelope boundaries,
    source annotations, protein identity-only roles and scope qualifiers were retained.
- evidence_id: baseplate-record
  kind: record_content
  reference: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
  locator: Entire frozen local record; identifier, label, definition and part_of used
    to resolve the local substructure reference
  accessed_at: '2026-10-21T11:00:58Z'
  support: context_only
  summary: The exact local-minted identifier denotes the CsmA–BChl a baseplate complex
    and is part of both chlorosome and envelope. The sibling is used for local identity,
    not as independent proof of its unresolved scientific claims.
- evidence_id: schema-necessity
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent.essentiality and EssentialityEnum
  accessed_at: '2026-10-21T11:00:58Z'
  support: context_only
  summary: Essentiality concerns whether the structure forms without the component;
    it is not an alias for importance in light harvesting or cell viability.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Composition, essentiality and evidence-scope guidance
  accessed_at: '2026-10-21T11:00:58Z'
  support: context_only
  summary: Keep component membership, formation necessity and function distinct. Do
    not force exact family groundings for heterogeneous cohorts or infer absence from
    an empty optional field.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Directed function/assembly paths and experimental-context rubric
  accessed_at: '2026-10-21T11:00:58Z'
  support: context_only
  summary: A mechanistic label requires a meaningful directed functional path; topology
    or cell viability alone is not a formation experiment.
- evidence_id: protein-policy
  kind: record_content
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Taxon-paired protein identity and evidence boundaries
  accessed_at: '2026-10-21T11:00:58Z'
  support: context_only
  summary: Accession identity is separate from structure membership. Reviewed and
    unreviewed entries retain their native statuses.
- evidence_id: chlorosome-envelope-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046858,GO:0043232,GO:0033105,GO:0015979
  locator: Complete requested identity, definitions, synonyms, comments and relevant
    child relations
  accessed_at: '2026-10-21T10:55:50.607662Z'
  support: supports
  summary: All four requested GO terms are active. GO0046858 is a child of intracellular
    membraneless organelle GO0043232, whose definition excludes a lipid bilayer, and
    lists GO0033105 part_of. The envelope definition specifies glycolipid monolayer
    with proteins; its comment explicitly excludes bilayer-envelope parentage. GO0015979
    correctly names photosynthesis.
  snapshot_sha256: 311aa9bdde571efbc2741945a2a4d73b13239ed30ec05c89398115367858b60a
- evidence_id: chlorosome-envelope-agent-SL-0060
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0060.json
  locator: id/name/definition/synonyms/geneOntologies/partOf; no statistics used
  accessed_at: '2026-10-21T10:55:50.607107Z'
  support: supports
  summary: SL0060 maps chlorosome envelope to GO0033105 and has synonym Chlorosomal
    envelope and partOf chlorosome. It describes an asymmetric galactolipid-containing
    surface in green sulfur bacteria; pigment-tail contribution to an inner leaflet
    is explicitly probable, not established universal bilayer architecture.
  snapshot_sha256: 711bbfca86410598680bf45a126c4c9690dd7c71739ef68ab738259c18dff0c4
- evidence_id: chlorosome-envelope-agent-tax-2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-21T08:39:14.454254Z'
  support: supports
  summary: Native taxonomy identifies Bacteria domain. Names in older papers are valid
    synonyms, not organism mismatches.
  snapshot_sha256: 7429617438ff0162ee4783c4c660f6127642e6ff686522e670c6ecf3a5b28816
- evidence_id: chlorosome-envelope-agent-tax-1097
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1097
  locator: taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-21T08:39:14.312179Z'
  support: supports
  summary: Native taxonomy identifies Chlorobaculum tepidum species, including Chlorobium
    tepidum synonym. Names in older papers are valid synonyms, not organism mismatches.
  snapshot_sha256: a8e843e290efea6a5a31d92ee3cdb32ee8bae331690d26d3c87955c375625c37
- evidence_id: chlorosome-envelope-agent-tax-1108
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1108
  locator: taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-21T08:39:14.399358Z'
  support: supports
  summary: Native taxonomy identifies Chloroflexus aurantiacus species. Names in older
    papers are valid synonyms, not organism mismatches.
  snapshot_sha256: 0deab46a2ef0f0db1b1d668e0a685004fe06f6d56ee255e35d67d47e3e481278
- evidence_id: chlorosome-envelope-agent-tax-194439
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/194439
  locator: taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-21T08:39:14.378082Z'
  support: supports
  summary: Native taxonomy identifies Chlorobaculum tepidum TLS strain, including
    Chlorobium tepidum TLS synonym. Names in older papers are valid synonyms, not
    organism mismatches.
  snapshot_sha256: db206b8370769142a525002170c3e080b17cdb2493db598567586f1d4cae4eae
- evidence_id: chlorosome-envelope-agent-orf2013-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s11120-013-9869-3
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T08:39:18.111581Z'
  support: supports
  summary: 'Exact native citation and complete abstract inspected: PMID23761131, DOI10.1007/s11120-013-9869-3,
    Chlorosome antenna complexes from green photosynthetic bacteria. This is secondary-review
    bibliographic/abstract scope.'
  snapshot_sha256: fe8c53d3d2226385cd7e88b2bea020c3dc89afdcfb6fc8d6d5870e9090a56e42
- evidence_id: chlorosome-envelope-agent-oostergetel2010-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s11120-010-9533-0
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T08:39:18.509220Z'
  support: supports
  summary: 'Exact native citation and complete abstract inspected: PMID20130996, DOI10.1007/s11120-010-9533-0,
    The chlorosome: a prototype for efficient light harvesting in photosynthesis.
    This is secondary-review bibliographic/abstract scope.'
  snapshot_sha256: d21480df53f3ec2d31f92b75e5938899961494a54d211fab7ece2c5af71c5907
- evidence_id: chlorosome-envelope-agent-psencik2009-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/JB.00690-09
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T08:39:17.997855Z'
  support: supports
  summary: 'Exact native citation and complete abstract inspected: PMID19717605, DOI10.1128/jb.00690-09,
    Structure of chlorosomes from the green filamentous bacterium Chloroflexus aurantiacus.
    This metadata/abstract receipt is distinct from any independently inspected full
    body.'
  snapshot_sha256: 202f2a3417932350d1493429648939255e642aee21d9a0d48b922102f0faa232
- evidence_id: chlorosome-envelope-agent-nielsen2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/ncomms12454
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T08:39:17.817415Z'
  support: supports
  summary: 'Exact native citation and complete abstract inspected: PMID27534696, DOI10.1038/ncomms12454,
    In situ high-resolution structure of the baseplate antenna complex in Chlorobaculum
    tepidum. This metadata/abstract receipt is distinct from any independently inspected
    full body.'
  snapshot_sha256: 0040f396e49964974cf13f9586dbe914d0d51af62d0735571df420a194d9b999
- evidence_id: chlorosome-envelope-agent-frigaard2004-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.186.3.646-653.2004&format=json&resultType=core
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T10:55:50.607597Z'
  support: supports
  summary: 'Exact native citation and complete abstract inspected: PMID14729689, DOI10.1128/jb.186.3.646-653.2004,
    Nine mutants of Chlorobium tepidum each unable to synthesize a different chlorosome
    protein still assemble functional chlorosomes. This metadata/abstract receipt
    is distinct from any independently inspected full body.'
  snapshot_sha256: 0142e808cc75ce236988195538136544013370342847498629c027f1e0dbc95a
- evidence_id: chlorosome-envelope-agent-li2006-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1021%2Fbi060776y&format=json&resultType=core
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T10:55:50.607808Z'
  support: supports
  summary: 'Exact native citation and complete abstract inspected: PMID16866355, DOI10.1021/bi060776y,
    Molecular contacts for chlorosome envelope proteins revealed by cross-linking
    studies with chlorosomes from Chlorobium tepidum. This metadata/abstract receipt
    is distinct from any independently inspected full body.'
  snapshot_sha256: 8073e85e672f077f1066a0641b6e01aaedde7170613240a3f52cd21de999c5d1
- evidence_id: chlorosome-envelope-agent-frigaard2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007/s11120-005-1331-8&format=json&resultType=core
  locator: resultList.result[0] citation/author/year and complete abstractText
  accessed_at: '2026-10-21T10:56:24.344770Z'
  support: supports
  summary: 'Exact native citation and complete abstract inspected: PMID16172929, DOI10.1007/s11120-005-1331-8,
    Isolation and characterization of carotenosomes from a bacteriochlorophyll c-less
    mutant of Chlorobium tepidum. This metadata/abstract receipt is distinct from
    any independently inspected full body.'
  snapshot_sha256: 14019ad8c85d29904ada495e915df35ea313ed78d856b001a197db0ebb11d420
- evidence_id: chlorosome-envelope-agent-nielsen2016-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4992139.1/PMC4992139.1.xml
  locator: All unsectioned Introduction; complete Results and Discussion; Methods
    Sample preparation including bchK growth, isolation and ssNMR; embedded captions.
    No raw spectra, microscopy pixels, supplements or full computational-method reanalysis.
  accessed_at: '2026-10-21T08:40:21.651455Z'
  support: supports
  summary: The high-resolution baseplate model combines ssNMR, spectroscopy and lower-resolution
    cryo-EM from bchK-mutant carotenosomes lacking BChl c. Wild-type/mutant freeze-fracture
    comparisons support conserved baseplate architecture. The intact functional baseplate
    in this modified organelle does not itself test formation after CsmA/baseplate
    removal. AFM dimensions discussed are from earlier work, not a new AFM experiment
    here. The Introduction explicitly attributes a structural-integrity role to the
    baseplate; this positive structural function is acknowledged separately from an
    isolated experimental test of universal formation necessity.
  snapshot_sha256: 0c5f33758e0ffea1a267cca08a1bcbb0da36023045ba7fcdc9189dfe9f6b3922
- evidence_id: chlorosome-envelope-agent-psencik2009-pmc-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2795307/
  locator: Methods sec1–sec2; all Results sec3–sec8 including Table1/captions; Discussion
    sec10 overall dimensions, sec12 perpendicular striation and sec13 summary. Other
    Discussion subsections not claimed as fully audited; no figure pixels/raw-data
    reanalysis.
  accessed_at: '2026-10-21T08:42:01.318551Z'
  support: supports
  summary: The primary C. aurantiacus J-10-fl study combines pigment analysis, cryo-EM/tomography
    and X-ray scattering. It attributes parallel striation to lamellar pigment organization
    and a regular one-face lattice to the baseplate. A CsmA dimer building block is
    an inference from lattice size and prior work, not atomic identification in this
    study. Residual cellular membranes are explicitly recognized as contamination.
  snapshot_sha256: da5d24b9f3f0abb179bd1b1b996a5b8b8542d2c9e67d3d07149b6e4636d9108a
- evidence_id: chlorosome-envelope-agent-oostergetel2010-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2882566.1/PMC2882566.1.xml
  locator: Sec1 Introduction; Sec2 Chlorosomes; Sec3 supramolecular organization;
    Sec5 baseplate; Sec7 spectroscopic properties in relation to function; embedded
    captions. Sec4/Sec8 and complete reference list not exhaustively audited.
  accessed_at: '2026-10-21T08:40:21.570713Z'
  support: supports
  summary: This review supports chlorosome occurrence in three bacterial groups, a
    non-bilayer envelope, pigment self-assembly and the pigment-to-baseplate-to-downstream-antenna/RC
    excitation route. It distinguishes FMO and B808–866 acceptors, species-dependent
    kinetics, and inferred structural models. It is secondary synthesis, not a new
    intervention experiment.
  snapshot_sha256: d555d33602f2946ad490d2d02be169d4f767093604c513edbf0d0753b347cea5
- evidence_id: chlorosome-envelope-agent-frigaard2004-ncbi
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC321489/
  locator: Introduction; all Methods sec1–sec6, Results sec7–sec11 and Discussion
    sec12; Tables1/2 and all embedded captions. No microscopy pixels, blot pixels
    or raw-data reanalysis. Genuine legacy PMC HTML, unlike earlier challenge responses.
  accessed_at: '2026-10-21T10:57:24.480300Z'
  support: supports
  summary: Nine separate non-CsmA gene disruptions retain chlorosomes with broadly
    similar composition and function, with specific size/pigment/growth effects. csmA
    transformants remain merodiploid under tested growth conditions; the authors infer
    a possible essential role in light harvesting and discuss lethality/difficulty
    of deletion. This does not directly establish universal chlorosome or envelope
    formation necessity. Individual deletions do not test complete cohort removal.
  snapshot_sha256: 9d7d1774a7e7aed6ff2816355f77df689adafd42ccc7218d6a9ae5d77df37bf6
- evidence_id: chlorosome-envelope-agent-orf2013-browser-body
  kind: authority
  reference: https://www.researchgate.net/publication/237199940_Chlorosome_Antenna_Complexes_from_Green_Photosynthetic_Bacteria
  locator: 'Author-uploaded review browser capture: Introduction and Chlorosome proteins
    and the CsmA baseplate pp322–323; preceding carotenoid/quinone context. Native
    publisher200 contains abstract/references only; this is not a complete review-body
    audit.'
  accessed_at: '2026-10-21T10:56:53.117693Z'
  support: supports
  summary: The review explicitly lists up to eleven Chlorobi protein types including
    CsmK, distinct motif families and lineage-dependent membership. It discusses carotenosomes
    and differentiates CsmA viability importance from structural characterization.
    Browser-captured secondary text, not native HTTP200.
  snapshot_sha256: 78a1e6d9b830045eb15da5f32f882639abc005c22a030e95e425c802768e3dd7
- evidence_id: chlorosome-envelope-agent-P0A314
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A314.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism
  accessed_at: '2026-10-21T08:39:14.950184Z'
  support: supports
  summary: Native P0A314 is reviewed, gene csmA, in tax194439 Chlorobaculum tepidum
    TLS. Gene/locus, native protein name, organism and entry status match the identity-only
    example. The historical native name Bacteriochlorophyll c-binding protein is retained
    as the source label; it is not used to override the experimentally established
    BChl a baseplate role.
  snapshot_sha256: 39dadbdc04fa6b4350a737e9894067b526bb041096c6a646b145818be2e1fdfa
- evidence_id: chlorosome-envelope-agent-Q46383
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q46383.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism
  accessed_at: '2026-10-21T10:55:50.607935Z'
  support: supports
  summary: Native Q46383 is reviewed, gene csmB, in tax194439 Chlorobaculum tepidum
    TLS. Gene/locus, native protein name, organism and entry status match the identity-only
    example. Identity evidence is not treated as an independent membership experiment.
  snapshot_sha256: f301bfe1e0c4af824862782ee615256c4dde780828a84695ae74d21562ef0beb
- evidence_id: chlorosome-envelope-agent-Q46367
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q46367.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism
  accessed_at: '2026-10-21T10:55:50.608571Z'
  support: supports
  summary: Native Q46367 is reviewed, gene csmC, in tax194439 Chlorobaculum tepidum
    TLS. Gene/locus, native protein name, organism and entry status match the identity-only
    example. Identity evidence is not treated as an independent membership experiment.
  snapshot_sha256: 9f4fbc7b5b866d63bdd2fb45e49c2bc7890ec20343b17bb54c8e1de9cb76487b
- evidence_id: chlorosome-envelope-agent-Q46386
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q46386.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism
  accessed_at: '2026-10-21T10:55:51.264499Z'
  support: supports
  summary: Native Q46386 is reviewed, gene csmE, in tax194439 Chlorobaculum tepidum
    TLS. Gene/locus, native protein name, organism and entry status match the identity-only
    example. Identity evidence is not treated as an independent membership experiment.
  snapshot_sha256: 1bea7e1eeac590899a198949667c66f0871547966682307075b405c8affa2c98
- evidence_id: chlorosome-envelope-agent-O68986
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O68986.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism
  accessed_at: '2026-10-21T10:55:51.286630Z'
  support: supports
  summary: Native O68986 is reviewed, gene csmF, in tax194439 Chlorobaculum tepidum
    TLS. Gene/locus, native protein name, organism and entry status match the identity-only
    example. Identity evidence is not treated as an independent membership experiment.
  snapshot_sha256: 9281ae269128d5b54105a8605d129c917357da1399d7183edad995f522620a19
- evidence_id: chlorosome-envelope-agent-O68988
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O68988.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism
  accessed_at: '2026-10-21T10:55:51.572925Z'
  support: supports
  summary: Native O68988 is reviewed, gene csmI, in tax194439 Chlorobaculum tepidum
    TLS. Gene/locus, native protein name, organism and entry status match the identity-only
    example. Identity evidence is not treated as an independent membership experiment.
  snapshot_sha256: 32f580bff31de222d3691dcbb480e4e92c4ae62a84ca939b61630f8c2bc3786c
- evidence_id: chlorosome-envelope-agent-O68983
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O68983.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism
  accessed_at: '2026-10-21T10:55:51.915493Z'
  support: supports
  summary: Native O68983 is reviewed, gene csmJ, in tax194439 Chlorobaculum tepidum
    TLS. Gene/locus, native protein name, organism and entry status match the identity-only
    example. Identity evidence is not treated as an independent membership experiment.
  snapshot_sha256: f5fd85c67d811dba67f0cb2ff35680d9098f8b9fe0739f5723b646ed0f62c854
- evidence_id: chlorosome-envelope-agent-H2VFJ4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/H2VFJ4.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism
  accessed_at: '2026-10-21T10:55:52.203529Z'
  support: supports
  summary: Native H2VFJ4 is unreviewed, gene csmD, in tax194439 Chlorobaculum tepidum
    TLS. Gene/locus, native protein name, organism and entry status match the identity-only
    example. Identity evidence is not treated as an independent membership experiment.
  snapshot_sha256: 5c8e2854660c20e5a67f71093f44c2360ff76f83284f409937c1bfd8fa563e40
- evidence_id: chlorosome-envelope-agent-H2VFJ1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/H2VFJ1.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism
  accessed_at: '2026-10-21T10:55:52.810913Z'
  support: supports
  summary: Native H2VFJ1 is unreviewed, gene csmH, in tax194439 Chlorobaculum tepidum
    TLS. Gene/locus, native protein name, organism and entry status match the identity-only
    example. Identity evidence is not treated as an independent membership experiment.
  snapshot_sha256: f46eb2eea722743b474a6c6bb403702119f888e7a7081f82f49c3bc2d68271bc
- evidence_id: chlorosome-envelope-agent-Q8KEN5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8KEN5.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism
  accessed_at: '2026-10-21T10:55:53.711632Z'
  support: supports
  summary: Native Q8KEN5 is unreviewed, gene csmX, in tax194439 Chlorobaculum tepidum
    TLS. Gene/locus, native protein name, organism and entry status match the identity-only
    example. Identity evidence is not treated as an independent membership experiment.
  snapshot_sha256: 3312354f0f178ad589517039088723dc7aae08f91af1ebdac65fa552cb5188ee
- evidence_id: chlorosome-envelope-agent-reviewed-csm-query
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A194439+AND+%28gene_exact%3AcsmA+OR+gene_exact%3AcsmB+OR+gene_exact%3AcsmC+OR+gene_exact%3AcsmD+OR+gene_exact%3AcsmE+OR+gene_exact%3AcsmF+OR+gene_exact%3AcsmH+OR+gene_exact%3AcsmI+OR+gene_exact%3AcsmJ+OR+gene_exact%3AcsmK+OR+gene_exact%3AcsmX%29&format=json&size=500
  locator: Complete result accession/gene/status/taxon projection; X-Total-Results7
    and no next-page link
  accessed_at: '2026-10-21T10:55:54.101517Z'
  support: supports
  summary: The complete exact reviewed tax194439 query for the eleven declared csm
    symbols returns seven reviewed entries matching A/B/C/E/F/I/J; the three separately
    verified unreviewed examples remain unreviewed. The query does not justify inventing
    a reviewed CsmK accession.
  snapshot_sha256: 904b7429522795458886148bf17eed86c2b57d128f86e58f8286f778627757f8
- evidence_id: chlorosome-envelope-agent-csmK-query
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AcsmK&format=json&size=500
  locator: Exact query gene_exact:csmK; complete results and X-Total-Results0
  accessed_at: '2026-10-21T10:55:54.274940Z'
  support: context_only
  summary: This bounded exact-symbol UniProt query returns zero entries. It does not
    refute the independently readable published CsmK protein membership or prove the
    protein/gene absent; no accession is fabricated.
  snapshot_sha256: a0273f3ee015db2d93e8b7003c9e14e76d24ea7b4fc43150f7816cd47fe11e4a
  search_scope: Remote public UniProtKB query gene_exact:csmK, all taxa/review statuses,
    size500; response total0/no pagination. Only this exact symbol was searched, not
    every synonym or proteome. Ignored files are not applicable to this remote query;
    no local absence claim is made.
- evidence_id: chlorosome-envelope-agent-matches-P0A314
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P0A314/
  locator: Complete count/next and all result metadata accession/name/type; no downstream
    functional or localization inference
  accessed_at: '2026-10-21T08:39:20.923741Z'
  support: supports
  summary: The exact P0A314 match endpoint reports G3DSA:1.20.5.950 bacteriochlorophyll
    c-binding protein (homologous_superfamily); IPR001470 Bacteriochlorophyll c-binding
    protein (family); IPR038387 Bacteriochlorophyll c-binding superfamily (homologous_superfamily);
    PF02043 Bacteriochlorophyll C binding protein (family); PIRSF002903 Chlorosome
    protein, CsmA/CsmE types (family); PR00656 BCHLROPHYLLC (family). These per-protein
    assignments do not alone establish an exact family for the complete accessory
    cohort.
  snapshot_sha256: 54f4d65be0a9e9b2b9f0f132f009cff6bd1b7b844d423447f3e122b67fccd4e9
- evidence_id: chlorosome-envelope-agent-matches-Q46383
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46383/?page_size=200
  locator: Complete count/next and all result metadata accession/name/type; no downstream
    functional or localization inference
  accessed_at: '2026-10-21T10:55:50.608045Z'
  support: supports
  summary: The exact Q46383 match endpoint reports IPR059980 CsmB chlorosome envelope
    protein (family). These per-protein assignments do not alone establish an exact
    family for the complete accessory cohort.
  snapshot_sha256: 9d90c767f264a69a21098c3c83d3b39b5a1fe04146c9f05ab9d27d7a6f76b717
- evidence_id: chlorosome-envelope-agent-matches-Q46367
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46367/?page_size=200
  locator: Complete count/next and all result metadata accession/name/type; no downstream
    functional or localization inference
  accessed_at: '2026-10-21T10:55:50.609189Z'
  support: supports
  summary: The exact Q46367 match endpoint reports IPR020995 Chlorosome envelope protein
    C (family). These per-protein assignments do not alone establish an exact family
    for the complete accessory cohort.
  snapshot_sha256: 13d35de84da180af3b491e5c7352138a475483eac3b3b83930119900eff1bb58
- evidence_id: chlorosome-envelope-agent-matches-Q46386
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46386/?page_size=200
  locator: Complete count/next and all result metadata accession/name/type; no downstream
    functional or localization inference
  accessed_at: '2026-10-21T10:55:51.269520Z'
  support: supports
  summary: The exact Q46386 match endpoint reports IPR001470 Bacteriochlorophyll c-binding
    protein (family); IPR038387 Bacteriochlorophyll c-binding superfamily (homologous_superfamily).
    These per-protein assignments do not alone establish an exact family for the complete
    accessory cohort.
  snapshot_sha256: 1196fdb735bad1a728a046dac7eb015b2dcd257ee11380e2ac38aa9823f96f5b
- evidence_id: chlorosome-envelope-agent-matches-O68986
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68986/?page_size=200
  locator: Complete count/next and all result metadata accession/name/type; no downstream
    functional or localization inference
  accessed_at: '2026-10-21T10:55:51.532976Z'
  support: supports
  summary: The exact O68986 match endpoint reports IPR059980 CsmB chlorosome envelope
    protein (family). These per-protein assignments do not alone establish an exact
    family for the complete accessory cohort.
  snapshot_sha256: f24e8d2e2362d57ce5607609a36cf37336a6b33537ee17404e33feba355fca4a
- evidence_id: chlorosome-envelope-agent-matches-O68988
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68988/?page_size=200
  locator: Complete count/next and all result metadata accession/name/type; no downstream
    functional or localization inference
  accessed_at: '2026-10-21T10:55:51.574997Z'
  support: supports
  summary: The exact O68988 match endpoint reports IPR001041 2Fe-2S ferredoxin-type
    iron-sulfur binding domain (domain); IPR001055 Adrenodoxin-like (family); IPR012675
    Beta-grasp domain superfamily (homologous_superfamily); IPR036010 2Fe-2S ferredoxin-like
    superfamily (homologous_superfamily). These per-protein assignments do not alone
    establish an exact family for the complete accessory cohort.
  snapshot_sha256: 4dc2781a1d1b61828609e12fdafb777740a4a7429809b0c70cd6c5da69c6f0fd
- evidence_id: chlorosome-envelope-agent-matches-O68983
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68983/?page_size=200
  locator: Complete count/next and all result metadata accession/name/type; no downstream
    functional or localization inference
  accessed_at: '2026-10-21T10:55:52.133431Z'
  support: supports
  summary: The exact O68983 match endpoint reports IPR001041 2Fe-2S ferredoxin-type
    iron-sulfur binding domain (domain); IPR001055 Adrenodoxin-like (family); IPR012675
    Beta-grasp domain superfamily (homologous_superfamily); IPR036010 2Fe-2S ferredoxin-like
    superfamily (homologous_superfamily). These per-protein assignments do not alone
    establish an exact family for the complete accessory cohort.
  snapshot_sha256: c4e6d56c3e1f6740223bcf6d8703d55bfbb4ca56b9f26a162f89adce3ff257b9
- evidence_id: chlorosome-envelope-agent-matches-H2VFJ4
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/H2VFJ4/?page_size=200
  locator: Native endpoint HTTP204 with zero-byte body; no JSON result or family absence
    inferred
  accessed_at: '2026-10-21T10:55:52.615911Z'
  support: context_only
  summary: The exact H2VFJ4 match endpoint supplied no content. This limits the family
    check and is not evidence of biological absence.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: chlorosome-envelope-agent-matches-H2VFJ1
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/H2VFJ1/?page_size=200
  locator: Complete count/next and all result metadata accession/name/type; no downstream
    functional or localization inference
  accessed_at: '2026-10-21T10:55:53.420952Z'
  support: supports
  summary: The exact H2VFJ1 match endpoint reports IPR017845 Chlorosome envelope protein
    H, CsmH (repeat); IPR040561 Large polyvalent protein associated domain 38 (domain).
    These per-protein assignments do not alone establish an exact family for the complete
    accessory cohort.
  snapshot_sha256: a6962831d38490b34c5d8bbb2a94f8e6c982c06b32c42a32a8e5858c45a6490d
- evidence_id: chlorosome-envelope-agent-matches-Q8KEN5
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8KEN5/?page_size=200
  locator: Complete count/next and all result metadata accession/name/type; no downstream
    functional or localization inference
  accessed_at: '2026-10-21T10:55:53.856537Z'
  support: supports
  summary: The exact Q8KEN5 match endpoint reports IPR001041 2Fe-2S ferredoxin-type
    iron-sulfur binding domain (domain); IPR001055 Adrenodoxin-like (family); IPR012675
    Beta-grasp domain superfamily (homologous_superfamily); IPR036010 2Fe-2S ferredoxin-like
    superfamily (homologous_superfamily). These per-protein assignments do not alone
    establish an exact family for the complete accessory cohort.
  snapshot_sha256: 903f92ae5457178d5dfb5387f4ff43b43dad57039a21b3b3f533cc4b0322333f
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml
    --verify
  locator: Complete focused native output including coverage categories
  accessed_at: '2026-10-21T10:57:25.283825Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml
    --causal-graphs
  locator: Complete focused native output including coverage categories
  accessed_at: '2026-10-21T10:57:25.799569Z'
  support: supports
  summary: "data/structures/membrane_organelle/chlorosome_envelope.yaml  (GO:0033105)\n\
    \  chlorosome_envelope_light_harvesting_topology\tcsm_envelope_proteins\tPARTIAL_EXAMPLES\t\
    ->csm_envelope_proteins (have: UniProtKB:Q46383, UniProtKB:Q46367, UniProtKB:Q46386,\
    \ UniProtKB:O68986, UniProtKB:O68988, UniProtKB:O68983, UniProtKB:H2VFJ4, UniProtKB:H2VFJ1,\
    \ UniProtKB:Q8KEN5; missing: csmK)\n  chlorosome_envelope_light_harvesting_topology\t\
    csma_baseplate\tCOVERED\t->csma_baseplate (UniProtKB:P0A314)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     1  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     1  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 573aab487e38acb58906341128af91f8f8d628fd2e62c300e45963b550a255ca
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/chlorosome_envelope.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:51:40Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/chlorosome_envelope.yaml'
  snapshot_sha256: fdee712ffc03f6528b258fabfd2799e4d35c5d4bb444c803e5418cde3644b7af
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/chlorosome_envelope.yaml
    --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/chlorosome_envelope-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:51:42Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/chlorosome_envelope.yaml\
    \ --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/chlorosome_envelope-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch22-20261021-xfifxerh/chlorosome_envelope-strict.tsv"
  snapshot_sha256: 6f77ec51748063491286d0343e0709ac5b81ac2c1491f75735ced41f914a1f30
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/chlorosome_envelope.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T11:00:58Z'
  support: supports
  summary: '22 of24 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:14729689: UNREACHABLE; resolved by evidence chlorosome-envelope-agent-frigaard2004-meta;
    cellstructuremech:chlorosome_baseplate_antenna_complex: SKIPPED; resolved by evidence
    baseplate-record. Source-native identity checked separately.'
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
  topic: Exact whole structure and part boundary
  outcome: supported
  target_ids:
  - GO:0033105
  summary: The exact GO identity and envelope parthood, synonyms and UniProt location
    cross-reference are supported; the envelope is a glycolipid/protein surface, not
    a bilayer organelle membrane. OTHER is compatible with the represented non-bilayer
    structure. The baseplate component resolves to the frozen local complex.
  evidence_ids:
  - record
  - baseplate-record
  - chlorosome-envelope-agent-go
  - chlorosome-envelope-agent-SL-0060
- assessment_id: composition
  area: evidence
  topic: Membrane material, pigment organization and Csm membership
  outcome: supported
  target_ids:
  - GO:0033105
  summary: The collective monolayer is a constitutional boundary. The glycolipid mixture
    differs from the whole envelope GO class, so its label-only material row is not
    automatically an omitted exact envelope mapping. The CsmA–BChl a array and heterogeneous
    accessory proteins are supported. Broader protein families and individual homolog
    matches must not replace the complete cohort with an inexact single identity.
  evidence_ids:
  - record
  - chlorosome-envelope-agent-go
  - chlorosome-envelope-agent-SL-0060
  - chlorosome-envelope-agent-nielsen2016-jats
  - chlorosome-envelope-agent-psencik2009-pmc-html
  - chlorosome-envelope-agent-frigaard2004-ncbi
  - chlorosome-envelope-agent-orf2013-browser-body
  - chlorosome-envelope-agent-matches-P0A314
  - chlorosome-envelope-agent-matches-Q46383
  - chlorosome-envelope-agent-matches-Q46367
  - chlorosome-envelope-agent-matches-Q46386
  - chlorosome-envelope-agent-matches-O68986
  - chlorosome-envelope-agent-matches-O68988
  - chlorosome-envelope-agent-matches-O68983
  - chlorosome-envelope-agent-matches-H2VFJ4
  - chlorosome-envelope-agent-matches-H2VFJ1
  - chlorosome-envelope-agent-matches-Q8KEN5
- assessment_id: baseplate-necessity
  area: evidence
  topic: Unqualified baseplate assembly-essentiality
  outcome: concern
  target_ids:
  - GO:0033105
  summary: The baseplate row asserts ESSENTIAL formation necessity across the target
    class. The cited sources establish membership, structure, excitation transfer
    and CsmA viability/segregation constraints in C. tepidum; they do not isolate
    formation of this target after baseplate loss. This is a bounded unsupported necessity
    assertion (F1), not evidence that the baseplate is dispensable. Nielsen2016 also
    explicitly assigns a structural-integrity function in its Introduction; the concern
    does not deny that role.
  evidence_ids:
  - record
  - schema-necessity
  - policy
  - chlorosome-envelope-agent-nielsen2016-jats
  - chlorosome-envelope-agent-frigaard2004-ncbi
- assessment_id: remaining-necessity
  area: evidence
  topic: Collective definitions, individual subunits and mutant boundaries
  outcome: unknown
  target_ids:
  - GO:0033105
  summary: 'Accessory cohort UNKNOWN is appropriate: single deletions do not establish
    requirements of the whole cohort across taxa. Individual lipid requirements are
    not established. The envelope study does not demonstrate formation necessity of
    every embedded protein.'
  evidence_ids:
  - record
  - schema-necessity
  - chlorosome-envelope-agent-nielsen2016-jats
  - chlorosome-envelope-agent-frigaard2004-ncbi
  - chlorosome-envelope-agent-frigaard2005-meta
- assessment_id: taxa
  area: scope
  topic: Bacterial variability and exact experimental context
  outcome: supported
  target_ids:
  - GO:0033105
  summary: VARIABLE Bacteria does not assert broad bacterial occurrence. Primary examples
    are C. tepidum and C. aurantiacus; old Chlorobium naming is a native synonym.
    Nielsen uses bchK-mutant carotenosomes plus wild-type comparisons; primary AFM
    measurements mentioned in that work are from earlier studies. No altered carotenosome
    is silently described as an unmodified experimental sample.
  evidence_ids:
  - record
  - chlorosome-envelope-agent-nielsen2016-jats
  - chlorosome-envelope-agent-psencik2009-pmc-html
  - chlorosome-envelope-agent-frigaard2004-ncbi
  - chlorosome-envelope-agent-oostergetel2010-jats
  - chlorosome-envelope-agent-tax-2
  - chlorosome-envelope-agent-tax-1097
  - chlorosome-envelope-agent-tax-1108
  - chlorosome-envelope-agent-tax-194439
- assessment_id: proteins
  area: evidence
  topic: Ten taxon-paired examples and bounded missing mapping
  outcome: supported
  target_ids:
  - GO:0033105
  summary: All ten supplied accessions, gene/locus identities, taxon and reviewed/unreviewed
    states match. Native verification passes. CsmK has published protein membership
    despite no result for the narrow exact-symbol query; its optional missing protein
    example is not a finding.
  evidence_ids:
  - record
  - protein-policy
  - chlorosome-envelope-agent-reviewed-csm-query
  - chlorosome-envelope-agent-csmK-query
  - chlorosome-envelope-agent-orf2013-browser-body
  - chlorosome-envelope-agent-P0A314
  - chlorosome-envelope-agent-Q46383
  - chlorosome-envelope-agent-Q46367
  - chlorosome-envelope-agent-Q46386
  - chlorosome-envelope-agent-O68986
  - chlorosome-envelope-agent-O68988
  - chlorosome-envelope-agent-O68983
  - chlorosome-envelope-agent-H2VFJ4
  - chlorosome-envelope-agent-H2VFJ1
  - chlorosome-envelope-agent-Q8KEN5
- assessment_id: graph
  area: graph
  topic: Six directed function edges and source levels
  outcome: supported
  target_ids:
  - GO:0033105
  summary: The NONMECHANISTIC envelope graph accurately states parthood, glycolipid
    boundary, accessory surface localization, aggregate enclosure and baseplate positioning
    toward light harvesting. It does not claim an exhaustive contact network. Downstream
    FMO/B808–866 and reaction-center details vary by lineage; no universal single
    acceptor accession or exhaustive inventory is forced.
  evidence_ids:
  - record
  - graph-policy
  - chlorosome-envelope-agent-go
  - chlorosome-envelope-agent-SL-0060
  - chlorosome-envelope-agent-nielsen2016-jats
  - chlorosome-envelope-agent-psencik2009-pmc-html
  - chlorosome-envelope-agent-oostergetel2010-jats
  - chlorosome-envelope-agent-frigaard2004-ncbi
- assessment_id: evidence-completeness
  area: completeness
  topic: Claim-specific sources and acknowledged inventory boundaries
  outcome: supported
  target_ids:
  - GO:0033105
  summary: All citations identify the intended works. The2004 deletion study and2006
    cross-linking abstract establish different experiments and do not include a CsmK
    knockout. The2013 review supplies the broader protein cohort. The existing grouped
    material/protein rows, local baseplate reference and open exact-grounding questions
    are meaningful; no automatic finding follows from omitted carotenoid/quinone rows
    or absent optional examples.
  evidence_ids:
  - record
  - chlorosome-envelope-agent-orf2013-browser-body
  - chlorosome-envelope-agent-frigaard2004-ncbi
  - chlorosome-envelope-agent-orf2013-meta
  - chlorosome-envelope-agent-oostergetel2010-meta
  - chlorosome-envelope-agent-psencik2009-meta
  - chlorosome-envelope-agent-nielsen2016-meta
  - chlorosome-envelope-agent-frigaard2004-meta
  - chlorosome-envelope-agent-li2006-meta
  - chlorosome-envelope-agent-frigaard2005-meta
findings:
- finding_id: F1
  issue_key: chlorosome_envelope-baseplate-assembly-necessity
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate CsmA baseplate function and viability from formation necessity
  description: The CsmA-baseplate component is marked ESSENTIAL, which the schema
    defines in terms of whether the target structure forms without it. Nielsen2016
    resolves a baseplate in bchK-mutant carotenosomes and compares wild-type/mutant
    structure; it does not remove the baseplate to test formation. Frigaard2004 reports
    failure of csmA transformants to segregate under its growth conditions and interprets
    possible essential light harvesting/viability, while the nine non-CsmA deletions
    retain chlorosomes. These results cannot by themselves assign an unqualified formation
    requirement to the baseplate across this bacterial structure class. Preserve the
    well-supported constituent and antenna roles, but qualify or withhold the assembly-necessity
    assertion unless a direct, appropriately scoped formation result is supplied.
    This finding does not say the baseplate is dispensable or treat vestigial pigment-free
    remnants as normal chlorosomes. Nielsen2016 explicitly assigns structural integrity
    as a baseplate function in its Introduction; retain this positive structural role
    while separating it from a tested universal requirement for formation.
  target_ids:
  - GO:0033105
  field_paths:
  - components[1].essentiality
  evidence_ids:
  - record
  - schema-necessity
  - policy
  - chlorosome-envelope-agent-nielsen2016-jats
  - chlorosome-envelope-agent-frigaard2004-ncbi
  normalization_reason: 'Major unsupported scientific essentiality claim: a positive
    structure-formation requirement is represented using evidence of structure, antenna
    function and cell viability with different experimental endpoints.'
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chlorosome_envelope.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Revise the CsmA-baseplate formation-necessity annotation or attach
    direct source evidence at the relevant taxon and experimental scope.
  finding_ids:
  - F1
  target_ids:
  - GO:0033105
  acceptance_checks:
  - Keep the supported baseplate constituent identity, structural-integrity role and
    light-harvesting role.
  - Use UNKNOWN or an appropriately qualified necessity state unless inspected evidence
    tests target formation after the relevant component loss.
  - Do not substitute failed mutant segregation, viability or excitation-transfer
    loss for an assembly endpoint; retain the modified-carotenosome versus normal-chlorosome
    boundary.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chlorosome_envelope.yaml
    role: maintained scientific record
limitations:
- Nielsen2016 is genuine full JATS read at the declared Introduction/Results/Discussion
  and sample-preparation Methods scope. Its high-resolution model uses bchK-mutant
  carotenosomes, with wild-type/mutant comparisons; AFM dimensions cited there derive
  from earlier work. No raw NMR, cryo-EM pixels, supplements or complete computational
  pipeline were independently reanalyzed.
- Psencik2009 genuine HTML Methods and Results plus the specified Discussion subsections
  were read. Lattice-based CsmA dimer assignment is an inference supported by prior
  work. No raw tomography, spectra or microscopy pixels were reanalyzed.
- Frigaard2004 genuine legacy PMC body was read through Introduction, Methods, Results,
  Discussion and table/figure captions. Earlier canonical HTML200 was a challenge,
  S3 returned404 and EPMC XML500; those failures remain in the packet and are not
  cited as bodies.
- Orf2013 native publisher/PDF routes returned abstract/reference HTML, not a readable
  PDF/main body. Actual author-uploaded Introduction/protein-baseplate passages were
  read through a browser capture with status:null. Oostergetel2010 was read as secondary
  synthesis at the stated sections; neither is recast as a new primary experiment.
- Li2006 was verified through exact native metadata and its complete primary abstract;
  publisher full text403. The abstract supports cross-linking and proposed contact
  models, but no full Methods audit is claimed. Frigaard2005 was read only at exact
  metadata/complete abstract scope for the vestigial-carotenosome boundary.
- The gene/family search is bounded to named examples, their match endpoints and the
  exact csmK symbol query. H2VFJ4 returned HTTP204 with no content. This does not
  prove family/protein absence; individual motifs or broader CsmA/E and ferredoxin
  families do not exactly denote the whole accessory set.
- Assembly necessity remains distinct from composition and light-harvesting function.
  The collective monolayer is constitutional; individual lipids and the complete accessory
  cohort have no universal necessity conclusion here. Modified or vestigial pigment-free
  organelles are not equated with unchanged normal chlorosomes.
- No images or structural datasets are maintained on either target. Figure captions
  in sources were read as text; no image licence, pixel measurements or raw experimental
  data audit is claimed.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
