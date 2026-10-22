# Contractile vacuole identity, component membership and evidence review

- Review: 20261022T005252Z-contractile-vacuole-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T11:11:05Z
- Finished UTC: 2026-10-22T00:52:52Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The vacuole identity, topology, osmotic function and six protein identities are coherent. One major finding concerns unsupported declared Dictyostelium aqpA/aqpB CV membership. Two minor findings concern the Chlamydomonas size/osmolarity note and central bladder synonym scope.

## Scope And Provenance

Entire target reviewed, including all components and six protein examples, three canonical taxa, every graph edge, source placement, identity/hierarchy, discussions and history.

Selection: User-authorized all-record pass; batch24 indices1–4 are four distinct maintained contractile-vacuole records, each reviewed in full.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000331 | data/structures/membrane_organelle/contractile_vacuole.yaml | maintained | contractile vacuole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0000331 | Native command returned zero. Coverage warnings are interpreted separately from accession verification. |
| Native protein causal-graphs | passed | True | GO:0000331 | Native command returned zero. Coverage warnings are interpreted separately from accession verification. |
| Focused native schema | passed | True | GO:0000331 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000331 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0000331 | 20 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0000331 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0000331 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000331 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000331 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000331 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0000331 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Taxonomic distribution and model scope

scope: supported. Targets: GO:0000331.

RARE is bounded by the note to patchy occurrence across Eukaryota; it is not interpreted as a quantitative prevalence estimate or universality within freshwater protists. Canonical examples establish particular models, not a conserved molecular inventory.

### Maintained input and neighboring boundaries

ownership: supported. Targets: GO:0000331.

This maintained YAML owns future scientific corrections. Source-native identities and captured neighbors keep CVC, central vacuole, spongiome, membrane, pore and lumen separate. History entries are provenance, not independent experimental evidence. No maintained input was edited.

### Vacuole identity and CVC boundary

identity: concern. Targets: GO:0000331.

GO:0000331, native GO vacuole ancestry, recorded CVC part_of and bounding membrane are coherent. The broader vacuole ancestry is verified in GO, not an invented parent_structures field. However, the central bladder synonym is labeled EXACT_SYNONYM while its named GO source classifies it as related; this is a localized synonym-scope mismatch, not a wrong structure identity. SL prose uses CV/CVC loosely, so GO and captured child boundaries control the record identity.

### Six protein identities and exact symbol/taxon queries

grounding: supported. Targets: GO:0000331.

All six existing primary accessions, reviewed states, labels, symbols and taxon pairs verify. Identity-only caveats are correct. They do not establish the separately claimed CV membership of aqpA/aqpB. MIP1 has direct Chlamydomonas localization support despite an unfilled symbol-search accession gap; no fabricated accession is required.

### Named Dictyostelium aquaporins versus supported CV channel class

evidence: concern. Targets: GO:0000331.

The generic aquaporin role is supported by ApAQP and MIP1, but aqpA/aqpB are named as genes/examples of that CV constituent without matching direct CV evidence. AqpB primary data establish unspecified vacuoles and only hypothesize a similar CV role; AqpA evidence concerns spores. Later Komsic Introduction language is stronger than the cited primary result and does not supply an independent experiment. This is an unsupported constituent assignment, not a false accession or proof of biological absence.

### Pump/channel-assisted filling and discharge

graph: supported. Targets: GO:0000331.

V-ATPase identity and CVC-system involvement are supported; spatial localization varies between reservoir and surrounding vesicles across models. The record edge description scopes the residence claim to CV-system membranes, and proposed gradient wording is retained. It should not be read as every protist bladder bearing identical pumps. NONMECHANISTIC scope and UNKNOWN component essentiality avoid untested assembly/systole mechanisms. Generic aquaporin edges remain valid at class level; named-gene inheritance is the finding.

### Canonical models and source-specific evidence

scope: concern. Targets: GO:0000331.

Dictyostelium, Chlamydomonas and Trypanosoma names/IDs match native taxonomy and the cited model studies. Their different CV organization and acidocalcisome traffic are not treated as interchangeable mechanisms. The Chlamydomonas note overstates the osmolarity response: Results distinguish CV size correlated with cell size from contraction interval correlated with external osmolarity.

## Findings

### F1: Dictyostelium aqpA and aqpB lack demonstrated CV membership in the cited evidence

major / open / confirmed; issue key: contractile-vacuole-aqpa-aqpb-membership-support.

The contractile_vacuole_aquaporins constituent declares aqpA and aqpB and supplies their verified Dictyostelium examples. The identity-only disclaimers correctly limit what accessions prove but leave that constituent assignment unsupported. AqpA sources concern late development and spore dormancy. The AqpB primary paper localizes GFP constructs to unspecified vacuoles and plasma membrane/protrusions, then proposes a CV-like role by analogy; it does not experimentally identify the vacuoles as contractile vacuoles. Water permeability was demonstrated for a loop-deletion mutant rather than the tested wild-type protein. Amoeba ApAQP and Chlamydomonas MIP1 evidence supports the broader component without proving these two assignments.

### F2: Chlamydomonas example conflates CV size regulation with osmolarity response

minor / open / confirmed; issue key: contractile-vacuole-chlamydomonas-size-osmolarity-note.

The canonical note says both CV size and pulse frequency respond to changing external osmolarity. Komsic-Buchmann2014 Results explicitly report that CV size did not correlate with medium osmotic strength: CV size correlated with cell size, while contraction interval depended on medium osmolarity. The two adaptations are distinguished in the paper. The broader function and measured-size/interval evidence remain supported.

### F3: Central bladder synonym scope exceeds the cited GO mapping

minor / open / confirmed; issue key: contractile-vacuole-central-bladder-synonym-scope.

The record labels central bladder EXACT_SYNONYM and names GO:0000331 as its source. Both captured current term and ancestry responses classify central bladder as a related synonym. The label is biologically pertinent, but the exactness qualifier is not supported by the cited authority.

## Recommended Actions And Acceptance Checks

### A1

Under separately authorized curation, remove aqpA/aqpB and their identity-only examples from the established CV-constituent gene/example list unless direct CV-localization evidence is supplied. Retain the supported generic aquaporin class and evidenced MIP1/ApAQP context. If useful, preserve AqpB as an explicitly tentative hypothesis in a source-backed discussion, with unspecified-vacuole localization and mutant-versus-wild-type functional scope. Record the reason so symbol seeding cannot silently restore the unsupported assignment.

- Every retained named aquaporin in the CV constituent has a taxon-paired source supporting CV membership, not only identity, developmental expression or generic vacuolar location.
- The von Bülow2012 data are not described as direct CV localization or as demonstrated wild-type AqpB water conductance.
- The aquaporin graph remains at supported class/taxon scope, and MIP1 is not assigned a guessed accession.
- Use the guarded writer and required curation/history events; run native schema/strict, UniProt verification, CURIE/product, history and generated-page checks plus qc after any curation.

### A2

Under separately authorized curation, revise the Chlamydomonas canonical note to distinguish CV size adaptation during cell growth from contraction-interval or pulse-frequency adaptation to external osmolarity. Preserve the valid model and source, and retain generic descriptions of measured size and interval only without implying both depend on medium osmolarity.

- The canonical note accurately states the distinct Results relationships: CV size versus cell size, contraction interval versus medium osmolarity.
- No direct lumen-osmolarity measurement or independent wild-type MIP1 water-channel assay is inferred from the modeling/localization study.
- Use the guarded writer and required curation/history events; run native schema/strict, history, render and qc gates after curation.

### A3

Under separately authorized curation, change central bladder to RELATED_SYNONYM to match the cited GO authority, or supply and explicitly cite independent support for exact equivalence at this record scope. Retain the main GO identity and label.

- The central bladder synonym qualifier agrees with its cited authority or a separately justified exact mapping.
- Use the guarded writer and required history events; run schema/strict, identifier-label, history, render and qc checks after curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/contractile_vacuole.yaml; Entire YAML, every current field including all evidence, discussions and history | context_only | Full maintained target read. No source/generated row replaces this YAML as owner. Other three assigned targets and pore neighbor read fully; spongiome identity, hierarchy, components and discussion fields read for boundary context, not audited as a seventh target. |
| neighbors | data/structures/membrane_organelle; The six native-captured contractile-vacuole/spongiome records | context_only | Ignored-inclusive rg -l --no-ignore --hidden search under data/structures for GO:0000331, GO:0031164, GO:0062159, GO:0062160 and the local contractile-vacuole-lumen ID found these six distinct paths. Exact target and all five neighbors are captured by native inspect. No whole-corpus uniqueness beyond this identity neighborhood is claimed. |
| contractile-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031164,GO:0005774,GO:0000331,GO:0062159,GO:0062160,GO:0043232,GO:0005775,GO:0031913,GO:0098797,GO:0005856; Exact ten-term response: names, definitions, synonyms and relevant children/relation edges | supports | Current nonobsolete GO identities distinguish the vacuole, its lipid bilayer, the CVC and spongiome, and the broader vacuolar lumen. GO explicitly gives CVC the intracellular membraneless-organelle parent and lists vacuole and spongiome as parts; membrane components remain lipid-bounded despite this assembly-level ontology classification. |
| contractile-agent-more2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016%2Fj.ejop.2024.126078; PMID38688044; exact DOI/title and full abstract only | supports | More et al.2024 metadata and complete abstract describe CVs as common osmoregulatory devices of freshwater/soil protists with variable architecture and machinery, and discuss presence and absence across eukaryotes. This supports patchy distribution, not a measured fraction of all Eukaryota. |
| contractile-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; taxId, scientificName, rank | supports | NCBI-derived ENA taxonomy confirms2759 Eukaryota, current rank domain. It verifies identity, not CV prevalence. |
| access-more2024-publisher | https://doi.org/10.1016/j.ejop.2024.126078; Original HTTP response; final URL https://linkinghub.elsevier.com/retrieve/pii/S0932473924000282 | context_only | HTTP 200. The DOI route returned a LinkingHub HTML redirect/locator, not review body text. The complete abstract above, not this response, supplies the assessed content. |
| native-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole.yaml --verify; Actual command output for this exact target | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole.yaml --causal-graphs; Actual command output for this exact target | supports | data/structures/membrane_organelle/contractile_vacuole.yaml  (GO:0000331)<br>  proton_gradient_water_filling_and_discharge	v_type_atpase	COVERED	-&gt;v_type_atpase (UniProtKB:P54647, UniProtKB:Q76NU1, UniProtKB:P54648, UniProtKB:Q54E04)<br>  proton_gradient_water_filling_and_discharge	aquaporins	PARTIAL_EXAMPLES	-&gt;contractile_vacuole_aquaporins (have: UniProtKB:Q9U8P7, UniProtKB:Q54WT8; missing: MIP1)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| initial-protein-network-failure | /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole.yaml --verify; Initial sandbox attempt, superseded by successful native retry | context_only | Exit1 arose from UniProt DNS resolution failure, not a protein mismatch. Original log is retained; fresh network-enabled native retry returned0. |
| contractile-agent-SL-0073 | https://rest.uniprot.org/locations/SL-0073.json; Definition, GO mapping, synonym and vacuole parent | supports | SL-0073 maps to GO:0000331 but its descriptive text uses CV and CVC more broadly. The record retains the sharper GO bladder/CVC boundary through its explicit part_of link. |
| contractile-agent-go-vacuole-parent | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005773; Definition and direct is_a child edge | supports | GO:0005773 is vacuole, with GO:0000331 explicitly listed as an is_a child. |
| contractile-agent-ancestors-0000331 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000331/ancestors?relations=is_a,part_of; Mixed is_a/part_of closure plus term metadata | supports | GO:0000331 ancestry includes vacuole and containing CVC; the current GO definition/synonyms support central bladder as related synonym. |
| contractile-agent-nishihara2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1042%2FBC20070091; Exact citation metadata and complete abstract; body unavailable through tested public routes | supports | Amoeba ApAQP has oocyte water-channel activity and CV/perivacuolar-vesicle localization. V-ATPase occurs on surrounding vesicles; gradient generation is proposed. This supports the class-level model without proving Dictyostelium aqpA/aqpB CV membership. |
| contractile-agent-clarke2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1242%2Fjcs.115.14.2893; Exact citation metadata and complete abstract; body unavailable through tested public routes | supports | Dictyostelium VatM-GFP was correctly targeted to CV and endolysosomal membranes and assembled into functional V-ATPase. Dynamic CVC membranes, not one permanently fixed bladder membrane, are the examined system. |
| contractile-agent-rohloff2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1074%2Fjbc.M410372200; Exact citation metadata and complete abstract; body unavailable through tested public routes | supports | Rohloff et al.2004 demonstrate Trypanosoma cruzi CV participation in regulatory volume decrease and acidocalcisome-to-CV aquaporin traffic. The abstract supports the canonical model note, not universal acidocalcisome fusion in every protist. |
| contractile-agent-allen2002-title | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=TITLE%3A%22Osmoregulation%20and%20contractile%20vacuoles%20of%20protozoa%22; PMID11952235; exact title and full abstract only | supports | Allen and Naitoh2002 exact title/DOI metadata and complete abstract describe filling/discharge, pump-rich tubular/vesicular compartments and a pump-poor reservoir. The initial unquoted DOI query returned zero; the exact-title response resolves the citation and does not imply missing literature. |
| contractile-agent-komsic2014-pmc-numeric | https://pmc.ncbi.nlm.nih.gov/articles/4248701/; Genuine PMC4248701 article HTML via numerical URL; abstract, Introduction, all Materials/Methods, Results and Discussion, Table1 and Fig1–9 captions read; supplementary movies and image pixels not inspected | supports | Komsic-Buchmann et al.2014 study Chlamydomonas CC-3395/UVM4 under altered osmolarity. They measure CV size and contraction intervals, calculate flux/permeability under stated geometric assumptions, localize MIP1 to CV membranes by immunogold and GFP, and discuss water flow into the lumen. MIP1 localization is directly supported; its water-channel activity and GFP construct functionality remain qualified. No overexpression effect establishes essentiality. The Introduction calls Dictyostelium aquaporin localization clear but cites von Bülow2012, whose primary results are less specific. |
| contractile-agent-docampo2013-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3818246.1/PMC3818246.1.xml; Genuine PMC3818246 JATS; introduction and section3 history, structure/composition, biogenesis and osmoregulation text read; no figure-pixel or cited-paper audit inferred | supports | Docampo et al.2013 review distinguishes bladder and spongiome, summarizes taxon-specific CV components and proposed pump-driven water accumulation, and describes osmoregulatory collection and discharge. Section3.4 distinguishes stable Paramecium pores from changing Dictyostelium CV contacts. Membrane, lumen and whole complex are not interchangeable; a lumen is not chemically pure water. |
| contractile-agent-bulow2012-pmc-numeric | https://pmc.ncbi.nlm.nih.gov/articles/3293572/; Genuine PMC3293572 article HTML via numerical URL; abstract, Introduction, Experimental Procedures, all Results and Discussion and Fig1–4 captions read, especially intracellular localization result and CV hypothesis paragraph; no image-pixel reanalysis | context_only | von Bülow et al.2012 report AqpB-GFP on intracellular vacuolar structures, plasma membrane and protrusions; they do not identify those vacuoles as CVs experimentally. The Discussion proposes analogous CV function by comparison with Amoeba and Trypanosoma. Wild-type AqpB was impermeable in the tested Xenopus assays; a loop-deletion mutant conducted water. AqpA is described as late-developmental/spore-associated, with channel function unshown. These findings do not establish either protein as a CV water-channel constituent. |
| contractile-agent-bulow2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A22262860%20AND%20SRC%3AMED; Exact metadata, complete abstract; primary full text assessed separately | supports | Exact PMID22262860/DOI/title and complete abstract confirm AqpB functional assays and unspecified vacuolar/plasma-membrane localization. This independently resolves the global resolver transport residual. |
| contractile-agent-aqpA2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A10876090%20AND%20SRC%3AMED; PMID10876090 exact metadata and complete abstract; no body read | supports | Mitra et al.2000 characterize aqpA developmental transcription and spore dormancy. The complete abstract does not report CV localization; this is bounded source insufficiency, not proof of absence from CVs. |
| contractile-agent-tax-44689 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689; Exact taxon fields and lineage | supports | NCBI-derived authority confirms 44689 Dictyostelium discoideum and eukaryotic lineage. |
| contractile-agent-tax-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Exact taxon fields and lineage | supports | NCBI-derived authority confirms 3055 Chlamydomonas reinhardtii and eukaryotic lineage. |
| contractile-agent-tax-5693 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5693; Exact taxon fields and lineage | supports | NCBI-derived authority confirms 5693 Trypanosoma cruzi and eukaryotic lineage. |
| contractile-agent-UniProtKB-P54647 | https://rest.uniprot.org/uniprotkb/P54647.json; Primary accession, entryType, proteinDescription, genes, organism, functional/location comments and relevant GO/family cross-references | supports | Native primary accession, reviewed status, exact protein label, vatA gene token and taxon44689 match the record. V-ATPase subunit identity/function and existing CV-system GO annotations were inspected; a complex function or localization is not equated with organelle assembly essentiality. |
| contractile-agent-query-vatA-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AvatA%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete result set and gene tokens | supports | Exact reviewed gene/taxon query returns one entry, P54647; entry gene tokens were separately checked for equality. This verifies symbol resolution only. |
| contractile-agent-UniProtKB-Q76NU1 | https://rest.uniprot.org/uniprotkb/Q76NU1.json; Primary accession, entryType, proteinDescription, genes, organism, functional/location comments and relevant GO/family cross-references | supports | Native primary accession, reviewed status, exact protein label, vatB gene token and taxon44689 match the record. V-ATPase subunit identity/function and existing CV-system GO annotations were inspected; a complex function or localization is not equated with organelle assembly essentiality. |
| contractile-agent-query-vatB-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AvatB%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete result set and gene tokens | supports | Exact reviewed gene/taxon query returns one entry, Q76NU1; entry gene tokens were separately checked for equality. This verifies symbol resolution only. |
| contractile-agent-UniProtKB-P54648 | https://rest.uniprot.org/uniprotkb/P54648.json; Primary accession, entryType, proteinDescription, genes, organism, functional/location comments and relevant GO/family cross-references | supports | Native primary accession, reviewed status, exact protein label, vatC gene token and taxon44689 match the record. V-ATPase subunit identity/function and existing CV-system GO annotations were inspected; a complex function or localization is not equated with organelle assembly essentiality. |
| contractile-agent-query-vatC-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AvatC%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete result set and gene tokens | supports | Exact reviewed gene/taxon query returns one entry, P54648; entry gene tokens were separately checked for equality. This verifies symbol resolution only. |
| contractile-agent-UniProtKB-Q54E04 | https://rest.uniprot.org/uniprotkb/Q54E04.json; Primary accession, entryType, proteinDescription, genes, organism, functional/location comments and relevant GO/family cross-references | supports | Native primary accession, reviewed status, exact protein label, vatM gene token and taxon44689 match the record. V-ATPase subunit identity/function and existing CV-system GO annotations were inspected; a complex function or localization is not equated with organelle assembly essentiality. |
| contractile-agent-query-vatM-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AvatM%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete result set and gene tokens | supports | Exact reviewed gene/taxon query returns one entry, Q54E04; entry gene tokens were separately checked for equality. This verifies symbol resolution only. |
| contractile-agent-UniProtKB-Q9U8P7 | https://rest.uniprot.org/uniprotkb/Q9U8P7.json; Primary accession, entryType, proteinDescription, genes, organism, functional/location comments and relevant GO/family cross-references | supports | Native primary accession, reviewed status, exact protein label, aqpA gene token and taxon44689 match the record. Functional/location comments concern spore survival and cell membrane by similarity, not experimental CV membership. |
| contractile-agent-query-aqpA-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AaqpA%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete result set and gene tokens | supports | Exact reviewed gene/taxon query returns one entry, Q9U8P7; entry gene tokens were separately checked for equality. This verifies symbol resolution only. |
| contractile-agent-UniProtKB-Q54WT8 | https://rest.uniprot.org/uniprotkb/Q54WT8.json; Primary accession, entryType, proteinDescription, genes, organism, functional/location comments and relevant GO/family cross-references | supports | Native primary accession, reviewed status, exact protein label, aqpB gene token and taxon44689 match the record. Experimental comments name cell membrane/cytoplasmic vesicle and unspecified vacuoles; channel activity is qualified. No CV-specific claim is inferred from these comments. |
| contractile-agent-query-aqpB-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AaqpB%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete result set and gene tokens | supports | Exact reviewed gene/taxon query returns one entry, Q54WT8; entry gene tokens were separately checked for equality. This verifies symbol resolution only. |
| contractile-agent-query-MIP1-3055-all | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AMIP1%29%20AND%20%28taxonomy_id%3A3055%29; Complete query/result, size100 | context_only | Exact gene_exact:MIP1 plus taxonomy3055 query, without reviewed restriction, returned zero results. This bounded symbol search does not establish that no MIP1 accession exists under a locus or synonym. The primary paper identifies Cre12.g549300.t1.2; no accession is guessed. |
| contractile-agent-aquaporin-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000425/; Family type, complete description and hierarchy | context_only | The Major intrinsic protein family includes water and solute channels and is broader than the record CV-localized subset. A shared broad family cannot demonstrate membership or substitute for CV evidence. |
| contractile-agent-go-vatpase | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016471; Exact current complex definition and parts | context_only | GO:0016471 identifies a vacuolar proton-transporting V-type ATPase complex, with V1/V0 parts. It is a credible general complex grounding, but this review does not treat a general vacuolar annotation as proof of the CV-system-specific subset or universal bladder localization. |
| access-nishihara2008-publisher | https://doi.org/10.1042/BC20070091; Original HTTP response; final URL https://onlinelibrary.wiley.com/doi/10.1042/BC20070091 | context_only | HTTP 403. Access-denial HTML, not primary paper body. |
| access-clarke2002-publisher | https://doi.org/10.1242/jcs.115.14.2893; Original HTTP response; final URL https://journals.biologists.com/jcs/article/115/14/2893/26764/Dynamics-of-the-vacuolar-H-ATPase-in-the | context_only | HTTP 403. Access-denial HTML, not primary paper body. |
| access-rohloff2004-publisher | https://doi.org/10.1074/jbc.M410372200; Original HTTP response; final URL https://linkinghub.elsevier.com/retrieve/pii/S0021925820676694 | context_only | HTTP 200. LinkingHub HTML locator/redirect, not paper body. |
| access-allen2002-publisher | https://doi.org/10.1016/S0074-7696(02)15015-7; Original HTTP response; final URL https://linkinghub.elsevier.com/retrieve/pii/S0074769602150157 | context_only | HTTP 200. LinkingHub HTML locator/redirect, not paper body. |
| access-rohloff2004-api | https://api.elsevier.com/content/article/pii/S0021925820676694?httpAccept=text/xml; Original HTTP response; final URL https://api.elsevier.com/content/article/pii/S0021925820676694?httpAccept=text/xml | context_only | HTTP 200. Elsevier API coredata metadata stub, not full article body. |
| schema-result | just validate data/structures/membrane_organelle/contractile_vacuole.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/contractile_vacuole.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/contractile_vacuole.yaml --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/contractile_vacuole.yaml --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch24-20261021-qayobm82/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/contractile_vacuole.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 20 of21 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:22262860: UNREACHABLE; resolved by evidence contractile-agent-bulow2012-meta. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- This is full coverage of one maintained record, not a full systematic review of all species or all CV-associated proteins. RARE is qualitative and model examples do not establish all-eukaryote molecular conservation.
- Several cited papers were readable only as complete indexed abstracts through the tested routes. HTTP200 redirects, API metadata stubs and reCAPTCHA pages were not treated as full text. Actual successful primary-body reads are separately located.
- No maintained snippet, image, numerical physical property or trait link is present in these four targets to validate. No new quotation, molecular inventory, scientific status or history event was introduced.
- Focused native checks and exact current-base resolver slices are reported here. Root owns batch-wide final gates and immutable saving; this author does not finalize or publish.
- The membership finding is confined to actually inspected primary and authority evidence, not a claim that the proteins are absent from CVs. More2024 full body was unavailable; Komsic2014 secondary wording was checked against the primary Bülow experiment.
- Initial native protein verification failed due sandbox DNS; the retained fresh retry passed0. The required final check is the successful retry.
- Clarke2002, Nishihara2008, Rohloff2004, Allen2002 and Mitra2000 were assessed at complete-abstract level; Komsic2014 and Bülow2012 body sections and Docampo2013 section3 were read as specified.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T005252Z-contractile-vacuole-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Contractile vacuole identity, component membership and evidence review
started_at: '2026-10-21T11:11:05Z'
finished_at: '2026-10-22T00:52:52Z'
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
summary: The vacuole identity, topology, osmotic function and six protein identities
  are coherent. One major finding concerns unsupported declared Dictyostelium aqpA/aqpB
  CV membership. Two minor findings concern the Chlamydomonas size/osmolarity note
  and central bladder synonym scope.
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
  - path: data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
    sha256: a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole.yaml
    sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
    role: target
  - path: data/structures/membrane_organelle/contractile_vacuole_complex.yaml
    sha256: 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    sha256: 9c85ec352245d16e963b9d86d4d1cf0b41d499b956b0b2d05611dca3a4341622
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    sha256: e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294
    role: context
  - path: data/structures/membrane_organelle/spongiome.yaml
    sha256: 4bdc11a86d247b6a45549a41c9aac3b25946b046f3b54d269fab634ca9d44019
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
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0000331
  path: data/structures/membrane_organelle/contractile_vacuole.yaml
  label: contractile vacuole
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
scope:
  description: Entire target reviewed, including all components and six protein examples,
    three canonical taxa, every graph edge, source placement, identity/hierarchy,
    discussions and history.
  selection: User-authorized all-record pass; batch24 indices1–4 are four distinct
    maintained contractile-vacuole records, each reviewed in full.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000331
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0000331
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole.yaml
    --verify
  exit_code: 0
  summary: Native command returned zero. Coverage warnings are interpreted separately
    from accession verification.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0000331
  command: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole.yaml
    --causal-graphs
  exit_code: 0
  summary: Native command returned zero. Coverage warnings are interpreted separately
    from accession verification.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000331
  command: just validate data/structures/membrane_organelle/contractile_vacuole.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000331
  command: just validate-strict data/structures/membrane_organelle/contractile_vacuole.yaml
    --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0000331
  summary: 20 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - contractile-agent-bulow2012-meta
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000331
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - neighbors
  - contractile-agent-go
  - contractile-agent-more2024-meta
  - contractile-agent-tax-2759
  - access-more2024-publisher
  - contractile-agent-SL-0073
  - contractile-agent-go-vacuole-parent
  - contractile-agent-ancestors-0000331
  - contractile-agent-nishihara2008-meta
  - contractile-agent-clarke2002-meta
  - contractile-agent-rohloff2004-meta
  - contractile-agent-allen2002-title
  - contractile-agent-komsic2014-pmc-numeric
  - contractile-agent-docampo2013-s3
  - contractile-agent-bulow2012-pmc-numeric
  - contractile-agent-bulow2012-meta
  - contractile-agent-aqpA2000-meta
  - contractile-agent-tax-44689
  - contractile-agent-tax-3055
  - contractile-agent-tax-5693
  - contractile-agent-UniProtKB-P54647
  - contractile-agent-query-vatA-44689
  - contractile-agent-UniProtKB-Q76NU1
  - contractile-agent-query-vatB-44689
  - contractile-agent-UniProtKB-P54648
  - contractile-agent-query-vatC-44689
  - contractile-agent-UniProtKB-Q54E04
  - contractile-agent-query-vatM-44689
  - contractile-agent-UniProtKB-Q9U8P7
  - contractile-agent-query-aqpA-44689
  - contractile-agent-UniProtKB-Q54WT8
  - contractile-agent-query-aqpB-44689
  - contractile-agent-query-MIP1-3055-all
  - contractile-agent-aquaporin-family
  - contractile-agent-go-vatpase
  - access-nishihara2008-publisher
  - access-clarke2002-publisher
  - access-rohloff2004-publisher
  - access-allen2002-publisher
  - access-rohloff2004-api
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000331
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
  - GO:0000331
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
  - GO:0000331
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
  - GO:0000331
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
  - GO:0000331
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
  reference: data/structures/membrane_organelle/contractile_vacuole.yaml
  locator: Entire YAML, every current field including all evidence, discussions and
    history
  accessed_at: '2026-10-21T11:23:07Z'
  support: context_only
  summary: Full maintained target read. No source/generated row replaces this YAML
    as owner. Other three assigned targets and pore neighbor read fully; spongiome
    identity, hierarchy, components and discussion fields read for boundary context,
    not audited as a seventh target.
- evidence_id: neighbors
  kind: record_content
  reference: data/structures/membrane_organelle
  locator: The six native-captured contractile-vacuole/spongiome records
  accessed_at: '2026-10-21T11:23:07Z'
  support: context_only
  summary: Ignored-inclusive rg -l --no-ignore --hidden search under data/structures
    for GO:0000331, GO:0031164, GO:0062159, GO:0062160 and the local contractile-vacuole-lumen
    ID found these six distinct paths. Exact target and all five neighbors are captured
    by native inspect. No whole-corpus uniqueness beyond this identity neighborhood
    is claimed.
- evidence_id: contractile-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031164,GO:0005774,GO:0000331,GO:0062159,GO:0062160,GO:0043232,GO:0005775,GO:0031913,GO:0098797,GO:0005856
  locator: 'Exact ten-term response: names, definitions, synonyms and relevant children/relation
    edges'
  accessed_at: '2026-10-21T11:12:36.483337Z'
  support: supports
  summary: Current nonobsolete GO identities distinguish the vacuole, its lipid bilayer,
    the CVC and spongiome, and the broader vacuolar lumen. GO explicitly gives CVC
    the intracellular membraneless-organelle parent and lists vacuole and spongiome
    as parts; membrane components remain lipid-bounded despite this assembly-level
    ontology classification.
  snapshot_sha256: 3001e9aa0de9d2828e1a1a727af2c84d192398885fe3080a1f75b13f34bad99a
- evidence_id: contractile-agent-more2024-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016%2Fj.ejop.2024.126078
  locator: PMID38688044; exact DOI/title and full abstract only
  accessed_at: '2026-10-21T11:12:38.019911Z'
  support: supports
  summary: More et al.2024 metadata and complete abstract describe CVs as common osmoregulatory
    devices of freshwater/soil protists with variable architecture and machinery,
    and discuss presence and absence across eukaryotes. This supports patchy distribution,
    not a measured fraction of all Eukaryota.
  snapshot_sha256: b6c0fbe9809f35dec2f0151eb3a8e6e212d4ce1fb60f1cd001785fdff3bf3e0b
- evidence_id: contractile-agent-tax-2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: taxId, scientificName, rank
  accessed_at: '2026-10-21T11:12:36.484828Z'
  support: supports
  summary: NCBI-derived ENA taxonomy confirms2759 Eukaryota, current rank domain.
    It verifies identity, not CV prevalence.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: access-more2024-publisher
  kind: search
  reference: https://doi.org/10.1016/j.ejop.2024.126078
  locator: Original HTTP response; final URL https://linkinghub.elsevier.com/retrieve/pii/S0932473924000282
  accessed_at: '2026-10-21T11:13:13.494252Z'
  support: context_only
  summary: HTTP 200. The DOI route returned a LinkingHub HTML redirect/locator, not
    review body text. The complete abstract above, not this response, supplies the
    assessed content.
  snapshot_sha256: 39c152a279323c8fddcea53c5aed455c7f3a0f3d51945c4e1b1c8f4f76ed25bb
  search_scope: One public source-access request to the exact recorded URL, following
    HTTP redirects; inspect response body for full text rather than infer access from
    HTTP status.
- evidence_id: native-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole.yaml
    --verify
  locator: Actual command output for this exact target
  accessed_at: '2026-10-21T11:15:48.315625Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole.yaml
    --causal-graphs
  locator: Actual command output for this exact target
  accessed_at: '2026-10-21T11:13:06.521175Z'
  support: supports
  summary: "data/structures/membrane_organelle/contractile_vacuole.yaml  (GO:0000331)\n\
    \  proton_gradient_water_filling_and_discharge\tv_type_atpase\tCOVERED\t->v_type_atpase\
    \ (UniProtKB:P54647, UniProtKB:Q76NU1, UniProtKB:P54648, UniProtKB:Q54E04)\n \
    \ proton_gradient_water_filling_and_discharge\taquaporins\tPARTIAL_EXAMPLES\t\
    ->contractile_vacuole_aquaporins (have: UniProtKB:Q9U8P7, UniProtKB:Q54WT8; missing:\
    \ MIP1)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED      \
    \             component_ref target holds protein_examples covering all declared\
    \ symbols\n     1  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: edb741baf42e62adafc4079a26b0e9b6b4fbd5454e2414f85c3d4c10da9fe979
- evidence_id: initial-protein-network-failure
  kind: validation
  reference: /private/tmp/cellstructure-batch24-20261021-qayobm82/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole.yaml
    --verify
  locator: Initial sandbox attempt, superseded by successful native retry
  accessed_at: '2026-10-21T11:13:05.974141Z'
  support: context_only
  summary: Exit1 arose from UniProt DNS resolution failure, not a protein mismatch.
    Original log is retained; fresh network-enabled native retry returned0.
  snapshot_sha256: fa71467c1d9b87ca4824caa9dd0b8d3c0ee3f45113ed85852b14f1167d6be76f
- evidence_id: contractile-agent-SL-0073
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0073.json
  locator: Definition, GO mapping, synonym and vacuole parent
  accessed_at: '2026-10-21T11:12:36.484293Z'
  support: supports
  summary: SL-0073 maps to GO:0000331 but its descriptive text uses CV and CVC more
    broadly. The record retains the sharper GO bladder/CVC boundary through its explicit
    part_of link.
  snapshot_sha256: bf50970299f0daf4a713091ca09dc75c5bfa17bbd69397afeac2da5420d8920e
- evidence_id: contractile-agent-go-vacuole-parent
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005773
  locator: Definition and direct is_a child edge
  accessed_at: '2026-10-21T11:18:13.092957Z'
  support: supports
  summary: GO:0005773 is vacuole, with GO:0000331 explicitly listed as an is_a child.
  snapshot_sha256: 38c7ec1de8258690b42a7da3161b0b9b1b8c92130fd28255c8c861785c402ec1
- evidence_id: contractile-agent-ancestors-0000331
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000331/ancestors?relations=is_a,part_of
  locator: Mixed is_a/part_of closure plus term metadata
  accessed_at: '2026-10-21T11:12:36.483975Z'
  support: supports
  summary: GO:0000331 ancestry includes vacuole and containing CVC; the current GO
    definition/synonyms support central bladder as related synonym.
  snapshot_sha256: a8bc7dcb4eefe50c5b9efcc30d1234894cffffb457fa5b6be34527920b84bec6
- evidence_id: contractile-agent-nishihara2008-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1042%2FBC20070091
  locator: Exact citation metadata and complete abstract; body unavailable through
    tested public routes
  accessed_at: '2026-10-21T11:12:37.286430Z'
  support: supports
  summary: Amoeba ApAQP has oocyte water-channel activity and CV/perivacuolar-vesicle
    localization. V-ATPase occurs on surrounding vesicles; gradient generation is
    proposed. This supports the class-level model without proving Dictyostelium aqpA/aqpB
    CV membership.
  snapshot_sha256: a4f39e396aa2fb01aa8673089dd4d4d8ac4fe192cdde0804323ce7f379b95a58
- evidence_id: contractile-agent-clarke2002-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1242%2Fjcs.115.14.2893
  locator: Exact citation metadata and complete abstract; body unavailable through
    tested public routes
  accessed_at: '2026-10-21T11:12:37.286499Z'
  support: supports
  summary: Dictyostelium VatM-GFP was correctly targeted to CV and endolysosomal membranes
    and assembled into functional V-ATPase. Dynamic CVC membranes, not one permanently
    fixed bladder membrane, are the examined system.
  snapshot_sha256: 2a37a596e7f4e7c579dffee743c4f268011dc6eec63559b0f9ff9072e24c677e
- evidence_id: contractile-agent-rohloff2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1074%2Fjbc.M410372200
  locator: Exact citation metadata and complete abstract; body unavailable through
    tested public routes
  accessed_at: '2026-10-21T11:12:38.014755Z'
  support: supports
  summary: Rohloff et al.2004 demonstrate Trypanosoma cruzi CV participation in regulatory
    volume decrease and acidocalcisome-to-CV aquaporin traffic. The abstract supports
    the canonical model note, not universal acidocalcisome fusion in every protist.
  snapshot_sha256: a2d84b841737fa7e9a58a86e7276b2c22a522934808df2a750ec556219141861
- evidence_id: contractile-agent-allen2002-title
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=TITLE%3A%22Osmoregulation%20and%20contractile%20vacuoles%20of%20protozoa%22
  locator: PMID11952235; exact title and full abstract only
  accessed_at: '2026-10-21T11:13:14.354512Z'
  support: supports
  summary: Allen and Naitoh2002 exact title/DOI metadata and complete abstract describe
    filling/discharge, pump-rich tubular/vesicular compartments and a pump-poor reservoir.
    The initial unquoted DOI query returned zero; the exact-title response resolves
    the citation and does not imply missing literature.
  snapshot_sha256: 6134ebe0236e6aea28c6e683db8fdb2ae275a717eaaecf476bc3408d11cdd142
- evidence_id: contractile-agent-komsic2014-pmc-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4248701/
  locator: Genuine PMC4248701 article HTML via numerical URL; abstract, Introduction,
    all Materials/Methods, Results and Discussion, Table1 and Fig1–9 captions read;
    supplementary movies and image pixels not inspected
  accessed_at: '2026-10-21T11:16:09.163473Z'
  support: supports
  summary: Komsic-Buchmann et al.2014 study Chlamydomonas CC-3395/UVM4 under altered
    osmolarity. They measure CV size and contraction intervals, calculate flux/permeability
    under stated geometric assumptions, localize MIP1 to CV membranes by immunogold
    and GFP, and discuss water flow into the lumen. MIP1 localization is directly
    supported; its water-channel activity and GFP construct functionality remain qualified.
    No overexpression effect establishes essentiality. The Introduction calls Dictyostelium
    aquaporin localization clear but cites von Bülow2012, whose primary results are
    less specific.
  snapshot_sha256: d804d3e2266b0a877bd9a448e18d257bb6267ed8cd0d0c49075ca5e88397cc4d
- evidence_id: contractile-agent-docampo2013-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3818246.1/PMC3818246.1.xml
  locator: Genuine PMC3818246 JATS; introduction and section3 history, structure/composition,
    biogenesis and osmoregulation text read; no figure-pixel or cited-paper audit
    inferred
  accessed_at: '2026-10-21T11:13:14.669515Z'
  support: supports
  summary: Docampo et al.2013 review distinguishes bladder and spongiome, summarizes
    taxon-specific CV components and proposed pump-driven water accumulation, and
    describes osmoregulatory collection and discharge. Section3.4 distinguishes stable
    Paramecium pores from changing Dictyostelium CV contacts. Membrane, lumen and
    whole complex are not interchangeable; a lumen is not chemically pure water.
  snapshot_sha256: 86c6b8220f007a31f585e81365fafb50db47b5610b3cc968f244acdd164d3741
- evidence_id: contractile-agent-bulow2012-pmc-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/3293572/
  locator: Genuine PMC3293572 article HTML via numerical URL; abstract, Introduction,
    Experimental Procedures, all Results and Discussion and Fig1–4 captions read,
    especially intracellular localization result and CV hypothesis paragraph; no image-pixel
    reanalysis
  accessed_at: '2026-10-21T11:16:09.201817Z'
  support: context_only
  summary: von Bülow et al.2012 report AqpB-GFP on intracellular vacuolar structures,
    plasma membrane and protrusions; they do not identify those vacuoles as CVs experimentally.
    The Discussion proposes analogous CV function by comparison with Amoeba and Trypanosoma.
    Wild-type AqpB was impermeable in the tested Xenopus assays; a loop-deletion mutant
    conducted water. AqpA is described as late-developmental/spore-associated, with
    channel function unshown. These findings do not establish either protein as a
    CV water-channel constituent.
  snapshot_sha256: 5e78ca95d676e40bf4ae57556aa3337ab3283f6137104a3f5b57065c3080f51a
- evidence_id: contractile-agent-bulow2012-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A22262860%20AND%20SRC%3AMED
  locator: Exact metadata, complete abstract; primary full text assessed separately
  accessed_at: '2026-10-21T11:12:38.119380Z'
  support: supports
  summary: Exact PMID22262860/DOI/title and complete abstract confirm AqpB functional
    assays and unspecified vacuolar/plasma-membrane localization. This independently
    resolves the global resolver transport residual.
  snapshot_sha256: d87b9e23e5b81b4f1d9bef714b085981a453949470028d7472636805d39b8b1a
- evidence_id: contractile-agent-aqpA2000-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A10876090%20AND%20SRC%3AMED
  locator: PMID10876090 exact metadata and complete abstract; no body read
  accessed_at: '2026-10-21T11:16:09.491657Z'
  support: supports
  summary: Mitra et al.2000 characterize aqpA developmental transcription and spore
    dormancy. The complete abstract does not report CV localization; this is bounded
    source insufficiency, not proof of absence from CVs.
  snapshot_sha256: 0b3825356048d3f639e38b020da45023726fbae6a13c74b10665b7e903c7d2be
- evidence_id: contractile-agent-tax-44689
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689
  locator: Exact taxon fields and lineage
  accessed_at: '2026-10-21T11:12:37.270270Z'
  support: supports
  summary: NCBI-derived authority confirms 44689 Dictyostelium discoideum and eukaryotic
    lineage.
  snapshot_sha256: f7bfea542a721125d862d08a5f8dd0986c1c19034b45f1fb92adf8c8d045efca
- evidence_id: contractile-agent-tax-3055
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Exact taxon fields and lineage
  accessed_at: '2026-10-21T11:12:37.270798Z'
  support: supports
  summary: NCBI-derived authority confirms 3055 Chlamydomonas reinhardtii and eukaryotic
    lineage.
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: contractile-agent-tax-5693
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5693
  locator: Exact taxon fields and lineage
  accessed_at: '2026-10-21T11:12:37.272356Z'
  support: supports
  summary: NCBI-derived authority confirms 5693 Trypanosoma cruzi and eukaryotic lineage.
  snapshot_sha256: d85474c78d866ba5b5b5b7f67fdec1433f8ca89addf1c52013fa2308d5919294
- evidence_id: contractile-agent-UniProtKB-P54647
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P54647.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, functional/location
    comments and relevant GO/family cross-references
  accessed_at: '2026-10-21T11:12:38.179604Z'
  support: supports
  summary: Native primary accession, reviewed status, exact protein label, vatA gene
    token and taxon44689 match the record. V-ATPase subunit identity/function and
    existing CV-system GO annotations were inspected; a complex function or localization
    is not equated with organelle assembly essentiality.
  snapshot_sha256: 5aa848d69318cee34c696cf4e2dbca39cd7e8080ebc456bc473ec2a0532013a0
- evidence_id: contractile-agent-query-vatA-44689
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AvatA%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete result set and gene tokens
  accessed_at: '2026-10-21T11:12:38.806469Z'
  support: supports
  summary: Exact reviewed gene/taxon query returns one entry, P54647; entry gene tokens
    were separately checked for equality. This verifies symbol resolution only.
  snapshot_sha256: 2c12da1e577bb5870984d56cf5bcd170fbdb89f3172708ffd84ae12b049181c9
- evidence_id: contractile-agent-UniProtKB-Q76NU1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q76NU1.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, functional/location
    comments and relevant GO/family cross-references
  accessed_at: '2026-10-21T11:12:38.750072Z'
  support: supports
  summary: Native primary accession, reviewed status, exact protein label, vatB gene
    token and taxon44689 match the record. V-ATPase subunit identity/function and
    existing CV-system GO annotations were inspected; a complex function or localization
    is not equated with organelle assembly essentiality.
  snapshot_sha256: 484196af4048c2df60bf0e618e372458df7ba5a7778b2f32288f73a1f328bb6d
- evidence_id: contractile-agent-query-vatB-44689
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AvatB%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete result set and gene tokens
  accessed_at: '2026-10-21T11:12:38.868030Z'
  support: supports
  summary: Exact reviewed gene/taxon query returns one entry, Q76NU1; entry gene tokens
    were separately checked for equality. This verifies symbol resolution only.
  snapshot_sha256: f9527eae42063733d601f599bd144adebe9c130843078b50f9d8de535d4ff25d
- evidence_id: contractile-agent-UniProtKB-P54648
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P54648.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, functional/location
    comments and relevant GO/family cross-references
  accessed_at: '2026-10-21T11:12:38.760952Z'
  support: supports
  summary: Native primary accession, reviewed status, exact protein label, vatC gene
    token and taxon44689 match the record. V-ATPase subunit identity/function and
    existing CV-system GO annotations were inspected; a complex function or localization
    is not equated with organelle assembly essentiality.
  snapshot_sha256: db4310ad9862f746a114c8af73f1363a6d432cf1329c0464fd20f4efb395feb9
- evidence_id: contractile-agent-query-vatC-44689
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AvatC%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete result set and gene tokens
  accessed_at: '2026-10-21T11:12:38.904687Z'
  support: supports
  summary: Exact reviewed gene/taxon query returns one entry, P54648; entry gene tokens
    were separately checked for equality. This verifies symbol resolution only.
  snapshot_sha256: 8a15ae741468663769fb0eeb265a150c3f9360f41949cf2b46a9db2e19537553
- evidence_id: contractile-agent-UniProtKB-Q54E04
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q54E04.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, functional/location
    comments and relevant GO/family cross-references
  accessed_at: '2026-10-21T11:12:38.762236Z'
  support: supports
  summary: Native primary accession, reviewed status, exact protein label, vatM gene
    token and taxon44689 match the record. V-ATPase subunit identity/function and
    existing CV-system GO annotations were inspected; a complex function or localization
    is not equated with organelle assembly essentiality.
  snapshot_sha256: 169ff6e42d6dcdd8abffa5ff7466a09eeabda4b1cf8b39bd2bc757a0a118fa8d
- evidence_id: contractile-agent-query-vatM-44689
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AvatM%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete result set and gene tokens
  accessed_at: '2026-10-21T11:12:39.365020Z'
  support: supports
  summary: Exact reviewed gene/taxon query returns one entry, Q54E04; entry gene tokens
    were separately checked for equality. This verifies symbol resolution only.
  snapshot_sha256: 7c969239729bc25a8916bb4db884580dd8f251d720b83222b316582d55b961a9
- evidence_id: contractile-agent-UniProtKB-Q9U8P7
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9U8P7.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, functional/location
    comments and relevant GO/family cross-references
  accessed_at: '2026-10-21T11:12:38.766342Z'
  support: supports
  summary: Native primary accession, reviewed status, exact protein label, aqpA gene
    token and taxon44689 match the record. Functional/location comments concern spore
    survival and cell membrane by similarity, not experimental CV membership.
  snapshot_sha256: 2409bd820504db30b75d137e0e271f109c7d362aff873366d06e2e25e7d487b8
- evidence_id: contractile-agent-query-aqpA-44689
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AaqpA%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete result set and gene tokens
  accessed_at: '2026-10-21T11:12:39.423376Z'
  support: supports
  summary: Exact reviewed gene/taxon query returns one entry, Q9U8P7; entry gene tokens
    were separately checked for equality. This verifies symbol resolution only.
  snapshot_sha256: e80456d7a26107ef43ce58350268cbdcd94f51d261dac3639e4f2f1849add8db
- evidence_id: contractile-agent-UniProtKB-Q54WT8
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q54WT8.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, functional/location
    comments and relevant GO/family cross-references
  accessed_at: '2026-10-21T11:12:38.774390Z'
  support: supports
  summary: Native primary accession, reviewed status, exact protein label, aqpB gene
    token and taxon44689 match the record. Experimental comments name cell membrane/cytoplasmic
    vesicle and unspecified vacuoles; channel activity is qualified. No CV-specific
    claim is inferred from these comments.
  snapshot_sha256: 3e0bd4d141af3060c05bf394af2cd4466eb7d8a6bec6eac097862726c0a48716
- evidence_id: contractile-agent-query-aqpB-44689
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AaqpB%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete result set and gene tokens
  accessed_at: '2026-10-21T11:12:39.476252Z'
  support: supports
  summary: Exact reviewed gene/taxon query returns one entry, Q54WT8; entry gene tokens
    were separately checked for equality. This verifies symbol resolution only.
  snapshot_sha256: 3a083c57f44816802e99be4216651711f86c02866b0f782a4a80fa2702e549bd
- evidence_id: contractile-agent-query-MIP1-3055-all
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AMIP1%29%20AND%20%28taxonomy_id%3A3055%29
  locator: Complete query/result, size100
  accessed_at: '2026-10-21T11:18:13.093529Z'
  support: context_only
  summary: Exact gene_exact:MIP1 plus taxonomy3055 query, without reviewed restriction,
    returned zero results. This bounded symbol search does not establish that no MIP1
    accession exists under a locus or synonym. The primary paper identifies Cre12.g549300.t1.2;
    no accession is guessed.
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
- evidence_id: contractile-agent-aquaporin-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000425/
  locator: Family type, complete description and hierarchy
  accessed_at: '2026-10-21T11:16:09.620305Z'
  support: context_only
  summary: The Major intrinsic protein family includes water and solute channels and
    is broader than the record CV-localized subset. A shared broad family cannot demonstrate
    membership or substitute for CV evidence.
  snapshot_sha256: ac574678948d33658edc435fb00f2d7419ea7dc2139f55433760ca9a82beb6bc
- evidence_id: contractile-agent-go-vatpase
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016471
  locator: Exact current complex definition and parts
  accessed_at: '2026-10-21T11:16:09.562199Z'
  support: context_only
  summary: GO:0016471 identifies a vacuolar proton-transporting V-type ATPase complex,
    with V1/V0 parts. It is a credible general complex grounding, but this review
    does not treat a general vacuolar annotation as proof of the CV-system-specific
    subset or universal bladder localization.
  snapshot_sha256: 43c760bfd14f3b2e02fca6b1cebe4547576402f89282fb18da04bc8e2c5d2f36
- evidence_id: access-nishihara2008-publisher
  kind: search
  reference: https://doi.org/10.1042/BC20070091
  locator: Original HTTP response; final URL https://onlinelibrary.wiley.com/doi/10.1042/BC20070091
  accessed_at: '2026-10-21T11:13:13.492709Z'
  support: context_only
  summary: HTTP 403. Access-denial HTML, not primary paper body.
  snapshot_sha256: 0c208ca2c358faa6dd7a5b8e0341696eb41dbfdc7837e5180844a34ec2037604
  search_scope: One public source-access request to the exact recorded URL, following
    HTTP redirects; inspect response body for full text rather than infer access from
    HTTP status.
- evidence_id: access-clarke2002-publisher
  kind: search
  reference: https://doi.org/10.1242/jcs.115.14.2893
  locator: Original HTTP response; final URL https://journals.biologists.com/jcs/article/115/14/2893/26764/Dynamics-of-the-vacuolar-H-ATPase-in-the
  accessed_at: '2026-10-21T11:13:13.492383Z'
  support: context_only
  summary: HTTP 403. Access-denial HTML, not primary paper body.
  snapshot_sha256: 60da0940cc93dc58e39fece862d94667532ec7c5121bbb4d75cd99a385ff2c7c
  search_scope: One public source-access request to the exact recorded URL, following
    HTTP redirects; inspect response body for full text rather than infer access from
    HTTP status.
- evidence_id: access-rohloff2004-publisher
  kind: search
  reference: https://doi.org/10.1074/jbc.M410372200
  locator: Original HTTP response; final URL https://linkinghub.elsevier.com/retrieve/pii/S0021925820676694
  accessed_at: '2026-10-21T11:13:13.493199Z'
  support: context_only
  summary: HTTP 200. LinkingHub HTML locator/redirect, not paper body.
  snapshot_sha256: e48eb42bbe1b86ace0b0c936c42882e49fdb8e14344e935c42e68a1955116c71
  search_scope: One public source-access request to the exact recorded URL, following
    HTTP redirects; inspect response body for full text rather than infer access from
    HTTP status.
- evidence_id: access-allen2002-publisher
  kind: search
  reference: https://doi.org/10.1016/S0074-7696(02)15015-7
  locator: Original HTTP response; final URL https://linkinghub.elsevier.com/retrieve/pii/S0074769602150157
  accessed_at: '2026-10-21T11:13:13.493488Z'
  support: context_only
  summary: HTTP 200. LinkingHub HTML locator/redirect, not paper body.
  snapshot_sha256: ecc1d4f218b8c031ef1815831f798766028a220881b3654576ab30109c15bfbc
  search_scope: One public source-access request to the exact recorded URL, following
    HTTP redirects; inspect response body for full text rather than infer access from
    HTTP status.
- evidence_id: access-rohloff2004-api
  kind: search
  reference: https://api.elsevier.com/content/article/pii/S0021925820676694?httpAccept=text/xml
  locator: Original HTTP response; final URL https://api.elsevier.com/content/article/pii/S0021925820676694?httpAccept=text/xml
  accessed_at: '2026-10-21T11:16:09.283338Z'
  support: context_only
  summary: HTTP 200. Elsevier API coredata metadata stub, not full article body.
  snapshot_sha256: 0c4e546b9a748f229985d6408c4d127125d8301365d60c2f791f26619204746f
  search_scope: One public source-access request to the exact recorded URL, following
    HTTP redirects; inspect response body for full text rather than infer access from
    HTTP status.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/contractile_vacuole.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:11:06Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/contractile_vacuole.yaml'
  snapshot_sha256: c54989305aa9759b27a3bd822ee1fc133ec4f2314ecd16426f441ce5b5fba423
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/contractile_vacuole.yaml
    --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:11:08Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/contractile_vacuole.yaml\
    \ --out /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch24-20261021-qayobm82/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch24-20261021-qayobm82/contractile_vacuole-strict.tsv"
  snapshot_sha256: c620ad593d744c9084aad066d73a5098befbe6380eeeef7c5b4d9cc07ea253b2
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/contractile_vacuole.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T11:23:07Z'
  support: supports
  summary: '20 of21 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:22262860: UNREACHABLE; resolved by evidence contractile-agent-bulow2012-meta.
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
- assessment_id: scope
  area: scope
  topic: Taxonomic distribution and model scope
  outcome: supported
  target_ids:
  - GO:0000331
  summary: RARE is bounded by the note to patchy occurrence across Eukaryota; it is
    not interpreted as a quantitative prevalence estimate or universality within freshwater
    protists. Canonical examples establish particular models, not a conserved molecular
    inventory.
  evidence_ids:
  - contractile-agent-tax-2759
  - contractile-agent-more2024-meta
- assessment_id: ownership
  area: ownership
  topic: Maintained input and neighboring boundaries
  outcome: supported
  target_ids:
  - GO:0000331
  summary: This maintained YAML owns future scientific corrections. Source-native
    identities and captured neighbors keep CVC, central vacuole, spongiome, membrane,
    pore and lumen separate. History entries are provenance, not independent experimental
    evidence. No maintained input was edited.
  evidence_ids:
  - record
  - neighbors
  - contractile-agent-go
- assessment_id: identity
  area: identity
  topic: Vacuole identity and CVC boundary
  outcome: concern
  target_ids:
  - GO:0000331
  summary: GO:0000331, native GO vacuole ancestry, recorded CVC part_of and bounding
    membrane are coherent. The broader vacuole ancestry is verified in GO, not an
    invented parent_structures field. However, the central bladder synonym is labeled
    EXACT_SYNONYM while its named GO source classifies it as related; this is a localized
    synonym-scope mismatch, not a wrong structure identity. SL prose uses CV/CVC loosely,
    so GO and captured child boundaries control the record identity.
  evidence_ids:
  - contractile-agent-go
  - contractile-agent-SL-0073
  - contractile-agent-go-vacuole-parent
  - contractile-agent-ancestors-0000331
  - neighbors
  - record
- assessment_id: protein-identities
  area: grounding
  topic: Six protein identities and exact symbol/taxon queries
  outcome: supported
  target_ids:
  - GO:0000331
  summary: All six existing primary accessions, reviewed states, labels, symbols and
    taxon pairs verify. Identity-only caveats are correct. They do not establish the
    separately claimed CV membership of aqpA/aqpB. MIP1 has direct Chlamydomonas localization
    support despite an unfilled symbol-search accession gap; no fabricated accession
    is required.
  evidence_ids:
  - contractile-agent-UniProtKB-P54647
  - contractile-agent-UniProtKB-Q76NU1
  - contractile-agent-UniProtKB-P54648
  - contractile-agent-UniProtKB-Q54E04
  - contractile-agent-UniProtKB-Q9U8P7
  - contractile-agent-UniProtKB-Q54WT8
  - contractile-agent-query-vatA-44689
  - contractile-agent-query-vatB-44689
  - contractile-agent-query-vatC-44689
  - contractile-agent-query-vatM-44689
  - contractile-agent-query-aqpA-44689
  - contractile-agent-query-aqpB-44689
  - contractile-agent-query-MIP1-3055-all
  - contractile-agent-komsic2014-pmc-numeric
  - native-verify
- assessment_id: membership
  area: evidence
  topic: Named Dictyostelium aquaporins versus supported CV channel class
  outcome: concern
  target_ids:
  - GO:0000331
  summary: The generic aquaporin role is supported by ApAQP and MIP1, but aqpA/aqpB
    are named as genes/examples of that CV constituent without matching direct CV
    evidence. AqpB primary data establish unspecified vacuoles and only hypothesize
    a similar CV role; AqpA evidence concerns spores. Later Komsic Introduction language
    is stronger than the cited primary result and does not supply an independent experiment.
    This is an unsupported constituent assignment, not a false accession or proof
    of biological absence.
  evidence_ids:
  - contractile-agent-bulow2012-pmc-numeric
  - contractile-agent-aqpA2000-meta
  - contractile-agent-komsic2014-pmc-numeric
  - contractile-agent-nishihara2008-meta
  - contractile-agent-UniProtKB-Q9U8P7
  - contractile-agent-UniProtKB-Q54WT8
  - record
- assessment_id: pumps-function
  area: graph
  topic: Pump/channel-assisted filling and discharge
  outcome: supported
  target_ids:
  - GO:0000331
  summary: V-ATPase identity and CVC-system involvement are supported; spatial localization
    varies between reservoir and surrounding vesicles across models. The record edge
    description scopes the residence claim to CV-system membranes, and proposed gradient
    wording is retained. It should not be read as every protist bladder bearing identical
    pumps. NONMECHANISTIC scope and UNKNOWN component essentiality avoid untested
    assembly/systole mechanisms. Generic aquaporin edges remain valid at class level;
    named-gene inheritance is the finding.
  evidence_ids:
  - contractile-agent-clarke2002-meta
  - contractile-agent-nishihara2008-meta
  - contractile-agent-allen2002-title
  - contractile-agent-docampo2013-s3
  - contractile-agent-komsic2014-pmc-numeric
  - contractile-agent-go-vatpase
  - contractile-agent-aquaporin-family
  - record
- assessment_id: examples
  area: scope
  topic: Canonical models and source-specific evidence
  outcome: concern
  target_ids:
  - GO:0000331
  summary: 'Dictyostelium, Chlamydomonas and Trypanosoma names/IDs match native taxonomy
    and the cited model studies. Their different CV organization and acidocalcisome
    traffic are not treated as interchangeable mechanisms. The Chlamydomonas note
    overstates the osmolarity response: Results distinguish CV size correlated with
    cell size from contraction interval correlated with external osmolarity.'
  evidence_ids:
  - contractile-agent-tax-44689
  - contractile-agent-tax-3055
  - contractile-agent-tax-5693
  - contractile-agent-clarke2002-meta
  - contractile-agent-komsic2014-pmc-numeric
  - contractile-agent-rohloff2004-meta
findings:
- finding_id: F1
  issue_key: contractile-vacuole-aqpa-aqpb-membership-support
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Dictyostelium aqpA and aqpB lack demonstrated CV membership in the cited
    evidence
  description: The contractile_vacuole_aquaporins constituent declares aqpA and aqpB
    and supplies their verified Dictyostelium examples. The identity-only disclaimers
    correctly limit what accessions prove but leave that constituent assignment unsupported.
    AqpA sources concern late development and spore dormancy. The AqpB primary paper
    localizes GFP constructs to unspecified vacuoles and plasma membrane/protrusions,
    then proposes a CV-like role by analogy; it does not experimentally identify the
    vacuoles as contractile vacuoles. Water permeability was demonstrated for a loop-deletion
    mutant rather than the tested wild-type protein. Amoeba ApAQP and Chlamydomonas
    MIP1 evidence supports the broader component without proving these two assignments.
  target_ids:
  - GO:0000331
  field_paths:
  - components[component_id=contractile_vacuole_aquaporins].gene_symbols
  - components[component_id=contractile_vacuole_aquaporins].protein_examples
  - causal_graphs[graph_id=proton_gradient_water_filling_and_discharge].nodes[node_id=aquaporins]
  evidence_ids:
  - contractile-agent-bulow2012-pmc-numeric
  - contractile-agent-aqpA2000-meta
  - contractile-agent-komsic2014-pmc-numeric
  - contractile-agent-nishihara2008-meta
  - contractile-agent-UniProtKB-Q9U8P7
  - contractile-agent-UniProtKB-Q54WT8
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; review-checklist:Component evidence and protein
    examples
  native_severity: major
  normalization_reason: The affected fields assert constituent membership and transfer
    a channel role to named proteins; accession verification alone cannot repair the
    missing structure-specific support.
- finding_id: F2
  issue_key: contractile-vacuole-chlamydomonas-size-osmolarity-note
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Chlamydomonas example conflates CV size regulation with osmolarity response
  description: 'The canonical note says both CV size and pulse frequency respond to
    changing external osmolarity. Komsic-Buchmann2014 Results explicitly report that
    CV size did not correlate with medium osmotic strength: CV size correlated with
    cell size, while contraction interval depended on medium osmolarity. The two adaptations
    are distinguished in the paper. The broader function and measured-size/interval
    evidence remain supported.'
  target_ids:
  - GO:0000331
  field_paths:
  - canonical_examples[taxon_id=NCBITaxon:3055].note
  evidence_ids:
  - contractile-agent-komsic2014-pmc-numeric
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  rule_id: review-checklist:Canonical examples; literature-evidence:claim-specific
    support
  native_severity: minor
  normalization_reason: A localized overstatement of one experimental variable in
    the canonical-example note; record identity, osmoregulatory function and the model
    choice remain valid.
- finding_id: F3
  issue_key: contractile-vacuole-central-bladder-synonym-scope
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Central bladder synonym scope exceeds the cited GO mapping
  description: The record labels central bladder EXACT_SYNONYM and names GO:0000331
    as its source. Both captured current term and ancestry responses classify central
    bladder as a related synonym. The label is biologically pertinent, but the exactness
    qualifier is not supported by the cited authority.
  target_ids:
  - GO:0000331
  field_paths:
  - synonyms[synonym_text=central bladder].synonym_type
  evidence_ids:
  - contractile-agent-go
  - contractile-agent-ancestors-0000331
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Identifier and synonym provenance; review-checklist:Identity
  native_severity: minor
  normalization_reason: Localized source-to-synonym-scope mismatch; canonical GO identity
    and general bladder/CVC boundaries remain valid.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0000331
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  description: Under separately authorized curation, remove aqpA/aqpB and their identity-only
    examples from the established CV-constituent gene/example list unless direct CV-localization
    evidence is supplied. Retain the supported generic aquaporin class and evidenced
    MIP1/ApAQP context. If useful, preserve AqpB as an explicitly tentative hypothesis
    in a source-backed discussion, with unspecified-vacuole localization and mutant-versus-wild-type
    functional scope. Record the reason so symbol seeding cannot silently restore
    the unsupported assignment.
  acceptance_checks:
  - Every retained named aquaporin in the CV constituent has a taxon-paired source
    supporting CV membership, not only identity, developmental expression or generic
    vacuolar location.
  - The von Bülow2012 data are not described as direct CV localization or as demonstrated
    wild-type AqpB water conductance.
  - The aquaporin graph remains at supported class/taxon scope, and MIP1 is not assigned
    a guessed accession.
  - Use the guarded writer and required curation/history events; run native schema/strict,
    UniProt verification, CURIE/product, history and generated-page checks plus qc
    after any curation.
  generator: Maintained scientific YAML; just render derives pages.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0000331
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  description: Under separately authorized curation, revise the Chlamydomonas canonical
    note to distinguish CV size adaptation during cell growth from contraction-interval
    or pulse-frequency adaptation to external osmolarity. Preserve the valid model
    and source, and retain generic descriptions of measured size and interval only
    without implying both depend on medium osmolarity.
  acceptance_checks:
  - 'The canonical note accurately states the distinct Results relationships: CV size
    versus cell size, contraction interval versus medium osmolarity.'
  - No direct lumen-osmolarity measurement or independent wild-type MIP1 water-channel
    assay is inferred from the modeling/localization study.
  - Use the guarded writer and required curation/history events; run native schema/strict,
    history, render and qc gates after curation.
  generator: Maintained scientific YAML; just render derives pages.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0000331
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  description: Under separately authorized curation, change central bladder to RELATED_SYNONYM
    to match the cited GO authority, or supply and explicitly cite independent support
    for exact equivalence at this record scope. Retain the main GO identity and label.
  acceptance_checks:
  - The central bladder synonym qualifier agrees with its cited authority or a separately
    justified exact mapping.
  - Use the guarded writer and required history events; run schema/strict, identifier-label,
    history, render and qc checks after curation.
  generator: Maintained scientific YAML; just render derives pages.
limitations:
- This is full coverage of one maintained record, not a full systematic review of
  all species or all CV-associated proteins. RARE is qualitative and model examples
  do not establish all-eukaryote molecular conservation.
- Several cited papers were readable only as complete indexed abstracts through the
  tested routes. HTTP200 redirects, API metadata stubs and reCAPTCHA pages were not
  treated as full text. Actual successful primary-body reads are separately located.
- No maintained snippet, image, numerical physical property or trait link is present
  in these four targets to validate. No new quotation, molecular inventory, scientific
  status or history event was introduced.
- Focused native checks and exact current-base resolver slices are reported here.
  Root owns batch-wide final gates and immutable saving; this author does not finalize
  or publish.
- The membership finding is confined to actually inspected primary and authority evidence,
  not a claim that the proteins are absent from CVs. More2024 full body was unavailable;
  Komsic2014 secondary wording was checked against the primary Bülow experiment.
- Initial native protein verification failed due sandbox DNS; the retained fresh retry
  passed0. The required final check is the successful retry.
- Clarke2002, Nishihara2008, Rohloff2004, Allen2002 and Mitra2000 were assessed at
  complete-abstract level; Komsic2014 and Bülow2012 body sections and Docampo2013
  section3 were read as specified.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
