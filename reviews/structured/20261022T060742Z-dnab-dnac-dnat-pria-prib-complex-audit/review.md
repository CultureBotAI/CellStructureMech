# Source-backed review of dnab dnac dnat pria prib complex

- Review: 20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:50:58Z
- Finished UTC: 2026-10-22T06:07:42Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major loader-versus-isolated-preprimosome source-stage conflict and one grouped minor exact DnaT/PriA/PriB family-grounding gap. Native ontology identity and supported protein identities are retained with explicit substrate/stage boundaries.

## Scope And Provenance

Exactly one complete maintained target plus frozen governing/schema/protein/graph guidance. No neighboring maintained record supplies scientific evidence. All current claims were assessed at the explicitly read authority/primary tiers.

Selection: Batch52 strict ordered selection, index 6; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990158 | data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml | maintained | DnaB-DnaC-DnaT-PriA-PriB complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990158 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990158 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:1990158 | Focused check passed; biological scope independently assessed. |
| Focused native verify | failed | False | GO:1990158 | Executed sandbox verification failed because network DNS was unavailable; optional historic attempt retained and superseded by successful network retry. |
| Focused native verify network retry | passed | True | GO:1990158 | Focused check passed; biological scope independently assessed. |
| Claim-level scientific review | passed | True | GO:1990158 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990158 | 11 of 13 collected target identifiers returned OK. PMID:8663104: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:8663105: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990158 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990158 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990158 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990158 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990158 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Native identity retained with experimental-stage conflict

identity: concern. Targets: GO:1990158.

The label, definition, synonym types, pre-primosome parent and claimed DnaB-DnaC component reproduce active GO1990158. This faithful mapping does not establish that the cited stable isolated PhiX174 preprimosome has that composition; the source-stage conflict requires explicit qualification, not silent identifier replacement.

### Correct named proteins and unresolved stage-specific complex

grounding: concern. Targets: GO:1990158.

DnaT/PriA/PriB identities and protein examples are supported; exact IPR020917/IPR005259/IPR023646 match them. PriB is distinct from the broader SSB/PriB family. The primary studies support DnaB delivery from DnaB-DnaC but do not establish DnaC as a stable constituent of the final isolated preprimosome. Associated PAS DNA remains label-only without a verified exact feature-class match.

### Short PAS versus intact phage DNA and repair hypothesis

scope: concern. Targets: GO:1990158.

NgI complete abstract specifies PriA/PriB/DnaT/DnaB on a short PAS substrate without final DnaC; NgII intact PhiX174 experiments retain PriC. The current canonical context and exclusion discussion need to preserve these substrate/assembly-stage differences. Fork-repair relevance is supported by GO and broader interpretation, while NgII alone hypothesizes delivery to repair intermediates.

### Formation necessity remains unknown

evidence: unknown. Targets: GO:1990158.

Every existing component essentiality is UNKNOWN. Source-supported participation, catalytic effects, viability and condition-specific complex recovery do not automatically establish universal structure-formation necessity. The present unknown labels are retained.

### Verified native protein identities and query scope

grounding: supported. Targets: GO:1990158.

All maintained accessions, genes, reviewed status and K12 taxon pairs agree with native responses; single-entry claims are checked against actual query results. Gene taxonomy and exact-organism queries remain distinguished. Optional extra protein examples are not required.

### Species scope and COMMON semantics

scope: supported. Targets: GO:1990158.

E.coli and K12 identities are exact. COMMON retains its schema meaning present in most members with exceptional losses; the cited E.coli experimental systems give qualitative support, not a measured species census. Phage substrate or recombinant conditions do not change the bacterial source taxon.

### Nonmechanistic graph with explicit limits

graph: concern. Targets: GO:1990158.

The graph is explicitly NONMECHANISTIC and uses typed protein/complex/DNA/process nodes. Its DnaB-DnaC membership and resulting preprimosome prose inherit the same source-stage issue; NONMECHANISTIC labeling does not resolve that scientific boundary. No separate graph-kind defect is asserted.

### Complete single-target assessment

completeness: supported. Targets: GO:1990158.

All maintained fields, citations, component states, protein annotations, graph edges, discussions and history were reviewed. Exact actionable mappings are separated from unestablished optional enrichment; historical access/curation notes are preserved. No source beyond the declared reading tier is certified.

## Findings

### F1: Separate the loader-containing model from isolated preprimosome composition

major / open / confirmed; issue key: dnab-dnac-dnat-pria-prib-source-stage-conflation.

Current GO1990158 names a DnaB-DnaC-containing complex, and the record turns that model into an unqualified constituent/has_part and graph claim while treating Ng experiments as its canonical source. NgI explicitly reports final PriA/PriB/DnaT/DnaB without DnaC. NgII pp15653–54 likewise rejects stable DnaC membership and retains PriC on intact PhiX174 DNA, unlike the short PAS substrate. Input proteins, transient loading and stable isolated composition are therefore conflated. Native authority and experimental observation must both remain visible.

### F2: Resolve verified existing component-class groundings

minor / open / confirmed; issue key: dnab-dnac-dnat-pria-prib-complex-exact-component-groundings.

DnaT, PriA and PriB exactly map to InterProIPR020917, IPR005259 and IPR023646, respectively. DnaT natural proteobacterial scope is stated; the PriB/SSB parent and helicase domains are not substituted. Native family/ontology identities plus independently inspected protein cross-references establish the matches. The current reviewed-label-only/open-task representation leaves these actionable classes unresolved. Historical earlier-pass statements are not declared false merely because current verification is available.

## Recommended Actions And Acceptance Checks

### A1

Preserve GO1990158 and explicitly distinguish its loader-containing assembly model from the Ng isolated complexes. Qualify the stage/source of DnaC parthood and graph membership, identify which substrate/stage the canonical example demonstrates, and retain the PriC-dependent intact-DNA versus short-PAS distinction. Inspect an appropriate primary source before claiming direct observation of the exact DnaC-containing assembly.

- Stable composition is not inferred from proteins supplied to the reaction.
- The action preserves current identity and reports the authority/source conflict without silently replacing it.
- Native schema, strict and CURIE checks pass after separately authorized curation.

### A2

Add the verified exact class CURIEs with source-specific evidence, update the corresponding grounding states/open task, and preserve organism accessions as examples. Do not force a broader homolog/domain or unresolved PAS-DNA mapping.

- Every added CURIE denotes the existing class at the stated scope, not an individual species protein.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml; Entire current YAML, all scientific fields, protein annotations, graph and discussion/history | context_only | The complete target was read. No neighboring maintained record supplies an unstated scientific premise. |
| curation | docs/CURATION.md; Component class grounding and formation necessity | context_only | REVIEWED_LABEL_ONLY means no exact class can be asserted after review; protein examples are not family classes. Essentiality concerns structure formation, separately from catalytic activity or viability. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentGroundingStatusEnum; EssentialityEnum; PresenceEnum | context_only | NCBIfam is an allowed source-neutral family prefix. COMMON means present in most taxon members with exceptional losses; UNKNOWN preserves unestablished formation necessity. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope and edge evidence | context_only | A descriptive composition/function graph may remain NONMECHANISTIC; exact node types and source-supported experimental context must be preserved. |
| micro52-go-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990101,GO:1990100,GO:1990158,GO:1990102,GO:1990077,GO:1990099,GO:0032991,GO:0031297,GO:0006270,GO:1990157,GO:1990160; Eleven-term native response: exact target identity/definition/synonyms/xrefs plus relevant typed parent children and function/boundary terms. Unrelated generic complex children are not used as scientific evidence. | supports | Active GO1990158 exactly matches the maintained label/definition and two synonyms and cites PMID8663105. GO1990099 typed children confirm the pre-primosome is_a parent; GO1990100 identifies the claimed subcomplex. Its definition, rather than a retrieved has_part edge, names the constituents. GO0031297 defines fork restoration/restart. The ontology model does not itself resolve the conflict with the cited isolated-complex experiment. |
| micro52-GO1990158-ancestors-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990158/ancestors?relations=is_a; Complete ancestors array, relations=is_a; no part_of relation is inferred from this array. | supports | The exact is_a-only ancestor response confirms pre-primosome, primosome and protein-DNA/protein-containing-complex ancestry. |
| micro52-GO1990158-constraints-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990158/constraints; Exact taxonConstraints array; inherited NOT annotation blacklist not used for prevalence. | supports | The exact restriction is only_in_taxon Prokaryota, represented as the Bacteria2/Archaea2157 union. This is an ontology taxon bound, not experimental proof of occurrence in either entire domain. |
| micro52-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete taxId/scientificName/rank/lineage/otherNames native response. | supports | ENA taxId562 identifies Escherichia coli, rank species. |
| micro52-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete taxId/scientificName/rank/lineage/otherNames native response. | supports | ENA taxId83333 identifies Escherichia coli K-12, rank strain. Reference-entry taxon is not silently equated with every experimental derivative. |
| micro52-pmid-8663104-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663104%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry: exact PMID/title/authors/year/DOI and complete abstractText. Main-body extents, when inspected, are separate. | supports | PMID8663104: The ordered assembly of the phiX174-type primosome. I. Isolation and identification of intermediate protein-DNA complexes. Ng JY, Marians KJ. (1996), DOI10.1074/jbc.271.26.15642. Complete native abstract and bibliographic identity read. The abstract explicitly excludes DnaC from the final PAS preprimosome; native metadata records a1996 erratum, whose content was not inspected. |
| micro52-pmid-8663105-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663105%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry: exact PMID/title/authors/year/DOI and complete abstractText. Main-body extents, when inspected, are separate. | supports | PMID8663105: The ordered assembly of the phiX174-type primosome. II. Preservation of primosome composition from assembly through replication. Ng JY, Marians KJ. (1996), DOI10.1074/jbc.271.26.15649. Complete native abstract and bibliographic identity read. The abstract retains PriC and excludes DnaC from the isolated intact-PhiX174 complexes; fork re-establishment is presented as a hypothesis. |
| micro52-protein-P0A8J2 | https://rest.uniprot.org/uniprotkb/P0A8J2.json; Primary accession/status; gene and organism; complete relevant comments and InterPro/NCBIfam cross-references. | supports | Reviewed P0A8J2 is dnaT in E.coli K12 taxon83333. Native identity, names, gene/taxon, full FUNCTION/SUBUNIT/SIMILARITY and available location comments plus family xrefs were read. |
| micro52-gene-dnaT-exact83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaT%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual URL query uses organism_id:83333, gene_exact:dnaT, reviewed:true; complete returned identity set. | supports | The bounded reviewed exact-dnaT query returns the single P0A8J2 record. The query is restricted to exact organism83333. |
| micro52-protein-P17888 | https://rest.uniprot.org/uniprotkb/P17888.json; Primary accession/status; gene and organism; complete relevant comments and InterPro/NCBIfam cross-references. | supports | Reviewed P17888 is priA in E.coli K12 taxon83333. Native identity, names, gene/taxon, full FUNCTION/SUBUNIT/SIMILARITY and available location comments plus family xrefs were read. |
| micro52-gene-priA-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual URL query uses taxonomy_id:83333, gene_exact:priA, reviewed:true; complete returned identity set. | supports | The bounded reviewed exact-priA query returns the single P17888 record. This descendant-inclusive query also confirms the exact83333 returned taxon. |
| micro52-protein-P07013-network | https://rest.uniprot.org/uniprotkb/P07013.json; Primary accession/status; gene and organism; complete relevant comments and InterPro/NCBIfam cross-references. | supports | Reviewed P07013 is priB in E.coli K12 taxon83333. Native identity, names, gene/taxon, full FUNCTION/SUBUNIT/SIMILARITY and available location comments plus family xrefs were read. |
| micro52-gene-priB-network | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual URL query uses organism_id:83333, gene_exact:priB, reviewed:true; complete returned identity set. | supports | The bounded reviewed exact-priB query returns the single P07013 record. The query is restricted to exact organism83333. |
| micro52-ipr-IPR020917 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020917/; Full metadata identity/name/type/descriptions and integrated member signatures; generic background stoichiometry/mechanism is not promoted to target-specific evidence. | supports | Native InterPro:IPR020917 is a whole-protein family for the named DnaT class, verified by type/name and source signatures. The separate reviewed UniProt response corroborates membership. The family explicitly covers DnaT and similar proteobacterial proteins; this natural taxonomic range fits the named E.coli class without implying all-domain distribution. |
| micro52-ipr-IPR005259 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005259/; Full metadata identity/name/type/descriptions and integrated member signatures; generic background stoichiometry/mechanism is not promoted to target-specific evidence. | supports | Native InterPro:IPR005259 is a whole-protein family for the named PriA class, verified by type/name and source signatures. The separate reviewed UniProt response corroborates membership. |
| micro52-ipr-IPR023646 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023646/; Full metadata identity/name/type/descriptions and integrated member signatures; generic background stoichiometry/mechanism is not promoted to target-specific evidence. | supports | Native InterPro:IPR023646 is a whole-protein family for the named PriB class, verified by type/name and source signatures. The separate reviewed UniProt response corroborates membership. |
| micro52-ng1996ii-pdf | https://pdfs.semanticscholar.org/7cc3/a0885916eebe17fede5346ad9e4d97fab747.pdf; Genuine public primary PDF pp15649–15654: entire scientific main text/Methods/Results/Discussion, TableI and Figure1–9 captions; p15655 references not scientific support. No figure pixels. | partial | Ng/MariansII isolates intact-PhiX174 complexes containing PriA/PriB/PriC/DnaT/DnaB. DnaC traces are interpreted as residual/transient interaction, not stable membership. The paper explicitly distinguishes the shorter PAS substrate and presents fork-re-establishment implications as hypotheses. |
| schema-result | just validate data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml |
| strict-result | just validate-strict data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_prib_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_prib_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_prib_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml --causal-graphs; Complete focused native read-only report | supports | data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml  (GO:1990158)<br>  dnab_dnac_dnat_pria_prib_restart	dnat_restart_protein	COVERED	-&gt;dnat_restart_protein (UniProtKB:P0A8J2)<br>  dnab_dnac_dnat_pria_prib_restart	pria_restart_protein	COVERED	-&gt;pria_restart_protein (UniProtKB:P17888)<br>  dnab_dnac_dnat_pria_prib_restart	prib_restart_protein	COVERED	-&gt;prib_restart_protein (UniProtKB:P07013)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml --verify; Complete focused native read-only report | context_only | Traceback (most recent call last):<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 922, in &lt;module&gt;<br>    raise SystemExit(main())<br>                     ~~~~^^<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 876, in main<br>    return cmd_verify(records)<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 727, in cmd_verify<br>    issues = verify_records(records)<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 616, in verify_records<br>    entries = fetch_entries_by_accession(all_accs) if all_accs else {}<br>              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 169, in fetch_entries_by_accession<br>    for entry in json.loads(_get(url)).get("results", []):<br>                            ~~~~^^^^^<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 134, in _get<br>    raise RuntimeError(f"UniProt unreachable after {RETRIES} attempts: {last}")<br>RuntimeError: UniProt unreachable after 3 attempts: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt; |
| native-verify-network | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml --verify; Complete focused native read-only report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 13 collected target identifiers returned OK. PMID:8663104: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:8663105: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- NgII entire scientific body/Methods/TableI/captions was read, but no pixels or underlying Western reanalysis. NgI is used only at its complete native abstract tier here; its indexed1996 erratum content remains uninspected.
- The DnaC finding does not assert that no transient loading intermediate can exist. Native GO identity is preserved pending reconciliation with direct source stage/composition. No uninspected modern restart study is imported to settle that conflict.
- No exact source-neutral primosome-assembly-site DNA class was independently established. This unresolved optional mapping is not automatically a finding; the exact protein-family mappings are separately established.
- Initial sandbox fetch/verification DNS failures and successful public-network retries are retained separately. Exact source URL, original UTC and SHA are preserved for every reused pair.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user requests one review for every unreviewed record, including qualified clean records.
- Native ontology/UniProt/family adapters directly answer these component claims. No iModulonDB dataset is established or used; computational expression-module membership would not prove physical complex formation.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of dnab dnac dnat pria prib complex
started_at: '2026-10-22T05:50:58Z'
finished_at: '2026-10-22T06:07:42Z'
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
summary: One major loader-versus-isolated-preprimosome source-stage conflict and one
  grouped minor exact DnaT/PriA/PriB family-grounding gap. Native ontology identity
  and supported protein identities are retained with explicit substrate/stage boundaries.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    sha256: 587fd3510ffd8ae95259dff336a7f2e984b50d34417d746277a41081a5b4ddb5
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
- target_id: GO:1990158
  path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
  label: DnaB-DnaC-DnaT-PriA-PriB complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target plus frozen governing/schema/protein/graph
    guidance. No neighboring maintained record supplies scientific evidence. All current
    claims were assessed at the explicitly read authority/primary tiers.
  selection: Batch52 strict ordered selection, index 6; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990158
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990158
  command: just validate data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990158
  command: just validate-strict data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_prib_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990158
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; biological scope independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: failed
  required: false
  target_ids:
  - GO:1990158
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    --verify
  exit_code: 1
  summary: Executed sandbox verification failed because network DNS was unavailable;
    optional historic attempt retained and superseded by successful network retry.
  evidence_ids:
  - native-verify
- check_id: native-verify-network
  name: Focused native verify network retry
  status: passed
  required: true
  target_ids:
  - GO:1990158
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; biological scope independently assessed.
  evidence_ids:
  - native-verify-network
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990158
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-pmid-8663104-network
  - micro52-pmid-8663105-network
  - micro52-protein-P0A8J2
  - micro52-gene-dnaT-exact83333
  - micro52-protein-P17888
  - micro52-gene-priA-83333
  - micro52-protein-P07013-network
  - micro52-gene-priB-network
  - micro52-ipr-IPR020917
  - micro52-ipr-IPR005259
  - micro52-ipr-IPR023646
  - micro52-ng1996ii-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990158
  summary: '11 of 13 collected target identifiers returned OK. PMID:8663104: UNREACHABLE;
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
  - micro52-pmid-8663104-network
  - micro52-pmid-8663105-network
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990158
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
  - GO:1990158
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
  - GO:1990158
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
  - GO:1990158
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
  - GO:1990158
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
  reference: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
  locator: Entire current YAML, all scientific fields, protein annotations, graph
    and discussion/history
  accessed_at: '2026-10-22T06:02:35Z'
  support: context_only
  summary: The complete target was read. No neighboring maintained record supplies
    an unstated scientific premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component class grounding and formation necessity
  accessed_at: '2026-10-22T06:02:35Z'
  support: context_only
  summary: REVIEWED_LABEL_ONLY means no exact class can be asserted after review;
    protein examples are not family classes. Essentiality concerns structure formation,
    separately from catalytic activity or viability.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentGroundingStatusEnum; EssentialityEnum; PresenceEnum
  accessed_at: '2026-10-22T06:02:35Z'
  support: context_only
  summary: NCBIfam is an allowed source-neutral family prefix. COMMON means present
    in most taxon members with exceptional losses; UNKNOWN preserves unestablished
    formation necessity.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope and edge evidence
  accessed_at: '2026-10-22T06:02:35Z'
  support: context_only
  summary: A descriptive composition/function graph may remain NONMECHANISTIC; exact
    node types and source-supported experimental context must be preserved.
- evidence_id: micro52-go-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990101,GO:1990100,GO:1990158,GO:1990102,GO:1990077,GO:1990099,GO:0032991,GO:0031297,GO:0006270,GO:1990157,GO:1990160
  locator: 'Eleven-term native response: exact target identity/definition/synonyms/xrefs
    plus relevant typed parent children and function/boundary terms. Unrelated generic
    complex children are not used as scientific evidence.'
  accessed_at: '2026-10-22T05:57:40.727722Z'
  support: supports
  summary: Active GO1990158 exactly matches the maintained label/definition and two
    synonyms and cites PMID8663105. GO1990099 typed children confirm the pre-primosome
    is_a parent; GO1990100 identifies the claimed subcomplex. Its definition, rather
    than a retrieved has_part edge, names the constituents. GO0031297 defines fork
    restoration/restart. The ontology model does not itself resolve the conflict with
    the cited isolated-complex experiment.
  snapshot_sha256: 190f29d0d4323902a99ad67697d7ec619c52626b213b1e00b2a05055063448bb
- evidence_id: micro52-GO1990158-ancestors-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990158/ancestors?relations=is_a
  locator: Complete ancestors array, relations=is_a; no part_of relation is inferred
    from this array.
  accessed_at: '2026-10-22T05:57:41.317523Z'
  support: supports
  summary: The exact is_a-only ancestor response confirms pre-primosome, primosome
    and protein-DNA/protein-containing-complex ancestry.
  snapshot_sha256: be9d22aa2b9a391faf36fb1d3a526bdbd8a544d3ee424d19778acb5108b97416
- evidence_id: micro52-GO1990158-constraints-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990158/constraints
  locator: Exact taxonConstraints array; inherited NOT annotation blacklist not used
    for prevalence.
  accessed_at: '2026-10-22T05:57:41.317740Z'
  support: supports
  summary: The exact restriction is only_in_taxon Prokaryota, represented as the Bacteria2/Archaea2157
    union. This is an ontology taxon bound, not experimental proof of occurrence in
    either entire domain.
  snapshot_sha256: 05a80c3c70f81d8862490d2b66d6aa79e60ab75ce80cab308ac66b39e9f69d68
- evidence_id: micro52-tax562
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete taxId/scientificName/rank/lineage/otherNames native response.
  accessed_at: '2026-10-22T05:42:45.974189Z'
  support: supports
  summary: ENA taxId562 identifies Escherichia coli, rank species.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: micro52-tax83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete taxId/scientificName/rank/lineage/otherNames native response.
  accessed_at: '2026-10-22T05:42:45.974327Z'
  support: supports
  summary: ENA taxId83333 identifies Escherichia coli K-12, rank strain. Reference-entry
    taxon is not silently equated with every experimental derivative.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro52-pmid-8663104-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663104%20AND%20SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED entry: exact PMID/title/authors/year/DOI and complete abstractText.
    Main-body extents, when inspected, are separate.'
  accessed_at: '2026-10-22T05:57:41.318908Z'
  support: supports
  summary: 'PMID8663104: The ordered assembly of the phiX174-type primosome. I. Isolation
    and identification of intermediate protein-DNA complexes. Ng JY, Marians KJ. (1996),
    DOI10.1074/jbc.271.26.15642. Complete native abstract and bibliographic identity
    read. The abstract explicitly excludes DnaC from the final PAS preprimosome; native
    metadata records a1996 erratum, whose content was not inspected.'
  snapshot_sha256: 7b0362fdb1a24c9a3153d8c54f7ecfc22179908ef4db25b635a0fb7d8f36dc7a
- evidence_id: micro52-pmid-8663105-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663105%20AND%20SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED entry: exact PMID/title/authors/year/DOI and complete abstractText.
    Main-body extents, when inspected, are separate.'
  accessed_at: '2026-10-22T05:57:41.375934Z'
  support: supports
  summary: 'PMID8663105: The ordered assembly of the phiX174-type primosome. II. Preservation
    of primosome composition from assembly through replication. Ng JY, Marians KJ.
    (1996), DOI10.1074/jbc.271.26.15649. Complete native abstract and bibliographic
    identity read. The abstract retains PriC and excludes DnaC from the isolated intact-PhiX174
    complexes; fork re-establishment is presented as a hypothesis.'
  snapshot_sha256: 2a9d16fbfcb9a3eee84a9e40f4bb00d30aec456c985997792b8f3d2c1e68e728
- evidence_id: micro52-protein-P0A8J2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A8J2.json
  locator: Primary accession/status; gene and organism; complete relevant comments
    and InterPro/NCBIfam cross-references.
  accessed_at: '2026-10-22T05:52:56.246138Z'
  support: supports
  summary: Reviewed P0A8J2 is dnaT in E.coli K12 taxon83333. Native identity, names,
    gene/taxon, full FUNCTION/SUBUNIT/SIMILARITY and available location comments plus
    family xrefs were read.
  snapshot_sha256: 0386cc1a24225bd2163f02bb9321fd59c773a862df700e6e11a442f2478a0eb8
- evidence_id: micro52-gene-dnaT-exact83333
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaT%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual URL query uses organism_id:83333, gene_exact:dnaT, reviewed:true;
    complete returned identity set.
  accessed_at: '2026-10-22T05:53:37.865414Z'
  support: supports
  summary: The bounded reviewed exact-dnaT query returns the single P0A8J2 record.
    The query is restricted to exact organism83333.
  snapshot_sha256: 098bbb792557c7cee62ac410f631525fb18878c8a368f6dc6a608934b785ac70
- evidence_id: micro52-protein-P17888
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P17888.json
  locator: Primary accession/status; gene and organism; complete relevant comments
    and InterPro/NCBIfam cross-references.
  accessed_at: '2026-10-22T05:52:56.395030Z'
  support: supports
  summary: Reviewed P17888 is priA in E.coli K12 taxon83333. Native identity, names,
    gene/taxon, full FUNCTION/SUBUNIT/SIMILARITY and available location comments plus
    family xrefs were read.
  snapshot_sha256: 17504956503542663f62e0d18d9f987a50081497aa0daea13b6b7d96496536aa
- evidence_id: micro52-gene-priA-83333
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual URL query uses taxonomy_id:83333, gene_exact:priA, reviewed:true;
    complete returned identity set.
  accessed_at: '2026-10-22T05:52:58.144220Z'
  support: supports
  summary: The bounded reviewed exact-priA query returns the single P17888 record.
    This descendant-inclusive query also confirms the exact83333 returned taxon.
  snapshot_sha256: c618bd342375bdeea25c1ad6bad58c8a2e1caa6e8251a59b765619b44080f160
- evidence_id: micro52-protein-P07013-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P07013.json
  locator: Primary accession/status; gene and organism; complete relevant comments
    and InterPro/NCBIfam cross-references.
  accessed_at: '2026-10-22T05:57:41.925066Z'
  support: supports
  summary: Reviewed P07013 is priB in E.coli K12 taxon83333. Native identity, names,
    gene/taxon, full FUNCTION/SUBUNIT/SIMILARITY and available location comments plus
    family xrefs were read.
  snapshot_sha256: 4a41331cb82a1040808d6b83f0be752e25dbea2320b60a6651bc862b9bac484f
- evidence_id: micro52-gene-priB-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual URL query uses organism_id:83333, gene_exact:priB, reviewed:true;
    complete returned identity set.
  accessed_at: '2026-10-22T05:57:41.925324Z'
  support: supports
  summary: The bounded reviewed exact-priB query returns the single P07013 record.
    The query is restricted to exact organism83333.
  snapshot_sha256: 44c93321a9d747492d7001566d8c7bd806b825ed3153821ac0c51ff7d20c58df
- evidence_id: micro52-ipr-IPR020917
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020917/
  locator: Full metadata identity/name/type/descriptions and integrated member signatures;
    generic background stoichiometry/mechanism is not promoted to target-specific
    evidence.
  accessed_at: '2026-10-22T05:53:37.121052Z'
  support: supports
  summary: Native InterPro:IPR020917 is a whole-protein family for the named DnaT
    class, verified by type/name and source signatures. The separate reviewed UniProt
    response corroborates membership. The family explicitly covers DnaT and similar
    proteobacterial proteins; this natural taxonomic range fits the named E.coli class
    without implying all-domain distribution.
  snapshot_sha256: 6737844952628c1e6c0e30133e8134728c11a4bc28c213dedc4afd497ef082cd
- evidence_id: micro52-ipr-IPR005259
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005259/
  locator: Full metadata identity/name/type/descriptions and integrated member signatures;
    generic background stoichiometry/mechanism is not promoted to target-specific
    evidence.
  accessed_at: '2026-10-22T05:53:37.121803Z'
  support: supports
  summary: Native InterPro:IPR005259 is a whole-protein family for the named PriA
    class, verified by type/name and source signatures. The separate reviewed UniProt
    response corroborates membership.
  snapshot_sha256: fd26c216e78be07f400f25ecd11062366714b19eda510840dbb92be4fb1e9db2
- evidence_id: micro52-ipr-IPR023646
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023646/
  locator: Full metadata identity/name/type/descriptions and integrated member signatures;
    generic background stoichiometry/mechanism is not promoted to target-specific
    evidence.
  accessed_at: '2026-10-22T05:58:05.792685Z'
  support: supports
  summary: Native InterPro:IPR023646 is a whole-protein family for the named PriB
    class, verified by type/name and source signatures. The separate reviewed UniProt
    response corroborates membership.
  snapshot_sha256: 9dc0552a7f882fde8e6cadc6ce070085b2587a417f05e6ef9320c059cd8b4603
- evidence_id: micro52-ng1996ii-pdf
  kind: primary_source
  reference: https://pdfs.semanticscholar.org/7cc3/a0885916eebe17fede5346ad9e4d97fab747.pdf
  locator: 'Genuine public primary PDF pp15649–15654: entire scientific main text/Methods/Results/Discussion,
    TableI and Figure1–9 captions; p15655 references not scientific support. No figure
    pixels.'
  accessed_at: '2026-10-22T05:55:37.199474Z'
  support: partial
  summary: Ng/MariansII isolates intact-PhiX174 complexes containing PriA/PriB/PriC/DnaT/DnaB.
    DnaC traces are interpreted as residual/transient interaction, not stable membership.
    The paper explicitly distinguishes the shorter PAS substrate and presents fork-re-establishment
    implications as hypotheses.
  snapshot_sha256: 1789a6bf1cfb26aeeacf73f6ba45b732d43eb3576268435c1736b357e3be6755
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:50:59Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml'
  snapshot_sha256: a93910b6e682f45922317433b22b2ef47c982076526472049003061c8ad2e2e4
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_prib_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:51:00Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml\
    \ --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_prib_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_dnat_pria_prib_complex-strict.tsv"
  snapshot_sha256: 9bdbbb7c373a108e511a21b5f132fcb736e442002f714af34f32937bd510a9a9
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    --causal-graphs
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T05:58:38.469095Z'
  support: supports
  summary: "data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml  (GO:1990158)\n\
    \  dnab_dnac_dnat_pria_prib_restart\tdnat_restart_protein\tCOVERED\t->dnat_restart_protein\
    \ (UniProtKB:P0A8J2)\n  dnab_dnac_dnat_pria_prib_restart\tpria_restart_protein\t\
    COVERED\t->pria_restart_protein (UniProtKB:P17888)\n  dnab_dnac_dnat_pria_prib_restart\t\
    prib_restart_protein\tCOVERED\t->prib_restart_protein (UniProtKB:P07013)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     3  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     3  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: da3be8302e150b5f1f300995c5bc908eaf804b9ec237b319e4ed1e1937955d35
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    --verify
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T05:58:51.020476Z'
  support: context_only
  summary: "Traceback (most recent call last):\n  File \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 922, in <module>\n    raise SystemExit(main())\n                     ~~~~^^\n\
    \  File \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 876, in main\n    return cmd_verify(records)\n  File \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 727, in cmd_verify\n    issues = verify_records(records)\n  File \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 616, in verify_records\n    entries = fetch_entries_by_accession(all_accs)\
    \ if all_accs else {}\n              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^\n  File\
    \ \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 169, in fetch_entries_by_accession\n    for entry in json.loads(_get(url)).get(\"\
    results\", []):\n                            ~~~~^^^^^\n  File \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 134, in _get\n    raise RuntimeError(f\"UniProt unreachable after {RETRIES}\
    \ attempts: {last}\")\nRuntimeError: UniProt unreachable after 3 attempts: <urlopen\
    \ error [Errno 8] nodename nor servname provided, or not known>"
  snapshot_sha256: bae930f373e9d6c317ec328ae8fa7db473a6cdbdcab44b8a9ba4cd2d486e5aad
- evidence_id: native-verify-network
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    --verify
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T05:59:22.078153Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 13 collected target identifiers returned OK. PMID:8663104: UNREACHABLE;
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
  topic: Native identity retained with experimental-stage conflict
  outcome: concern
  target_ids:
  - GO:1990158
  summary: The label, definition, synonym types, pre-primosome parent and claimed
    DnaB-DnaC component reproduce active GO1990158. This faithful mapping does not
    establish that the cited stable isolated PhiX174 preprimosome has that composition;
    the source-stage conflict requires explicit qualification, not silent identifier
    replacement.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-ng1996ii-pdf
  - micro52-pmid-8663104-network
  - micro52-pmid-8663105-network
- assessment_id: composition
  area: grounding
  topic: Correct named proteins and unresolved stage-specific complex
  outcome: concern
  target_ids:
  - GO:1990158
  summary: DnaT/PriA/PriB identities and protein examples are supported; exact IPR020917/IPR005259/IPR023646
    match them. PriB is distinct from the broader SSB/PriB family. The primary studies
    support DnaB delivery from DnaB-DnaC but do not establish DnaC as a stable constituent
    of the final isolated preprimosome. Associated PAS DNA remains label-only without
    a verified exact feature-class match.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-ipr-IPR020917
  - micro52-ipr-IPR005259
  - micro52-ipr-IPR023646
  - micro52-protein-P0A8J2
  - micro52-gene-dnaT-exact83333
  - micro52-protein-P17888
  - micro52-gene-priA-83333
  - micro52-protein-P07013-network
  - micro52-gene-priB-network
  - micro52-ng1996ii-pdf
  - micro52-pmid-8663104-network
  - micro52-pmid-8663105-network
- assessment_id: source-boundaries
  area: scope
  topic: Short PAS versus intact phage DNA and repair hypothesis
  outcome: concern
  target_ids:
  - GO:1990158
  summary: NgI complete abstract specifies PriA/PriB/DnaT/DnaB on a short PAS substrate
    without final DnaC; NgII intact PhiX174 experiments retain PriC. The current canonical
    context and exclusion discussion need to preserve these substrate/assembly-stage
    differences. Fork-repair relevance is supported by GO and broader interpretation,
    while NgII alone hypothesizes delivery to repair intermediates.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-ng1996ii-pdf
  - micro52-pmid-8663104-network
  - micro52-pmid-8663105-network
- assessment_id: formation
  area: evidence
  topic: Formation necessity remains unknown
  outcome: unknown
  target_ids:
  - GO:1990158
  summary: Every existing component essentiality is UNKNOWN. Source-supported participation,
    catalytic effects, viability and condition-specific complex recovery do not automatically
    establish universal structure-formation necessity. The present unknown labels
    are retained.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-ng1996ii-pdf
- assessment_id: protein-examples
  area: grounding
  topic: Verified native protein identities and query scope
  outcome: supported
  target_ids:
  - GO:1990158
  summary: All maintained accessions, genes, reviewed status and K12 taxon pairs agree
    with native responses; single-entry claims are checked against actual query results.
    Gene taxonomy and exact-organism queries remain distinguished. Optional extra
    protein examples are not required.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-protein-P0A8J2
  - micro52-gene-dnaT-exact83333
  - micro52-protein-P17888
  - micro52-gene-priA-83333
  - micro52-protein-P07013-network
  - micro52-gene-priB-network
- assessment_id: taxonomic-scope
  area: scope
  topic: Species scope and COMMON semantics
  outcome: supported
  target_ids:
  - GO:1990158
  summary: E.coli and K12 identities are exact. COMMON retains its schema meaning
    present in most members with exceptional losses; the cited E.coli experimental
    systems give qualitative support, not a measured species census. Phage substrate
    or recombinant conditions do not change the bacterial source taxon.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-ng1996ii-pdf
  - micro52-pmid-8663104-network
  - micro52-pmid-8663105-network
- assessment_id: graph
  area: graph
  topic: Nonmechanistic graph with explicit limits
  outcome: concern
  target_ids:
  - GO:1990158
  summary: The graph is explicitly NONMECHANISTIC and uses typed protein/complex/DNA/process
    nodes. Its DnaB-DnaC membership and resulting preprimosome prose inherit the same
    source-stage issue; NONMECHANISTIC labeling does not resolve that scientific boundary.
    No separate graph-kind defect is asserted.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-ng1996ii-pdf
  - graphs
  - micro52-pmid-8663104-network
  - micro52-pmid-8663105-network
- assessment_id: coverage
  area: completeness
  topic: Complete single-target assessment
  outcome: supported
  target_ids:
  - GO:1990158
  summary: All maintained fields, citations, component states, protein annotations,
    graph edges, discussions and history were reviewed. Exact actionable mappings
    are separated from unestablished optional enrichment; historical access/curation
    notes are preserved. No source beyond the declared reading tier is certified.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-protein-P0A8J2
  - micro52-gene-dnaT-exact83333
  - micro52-protein-P17888
  - micro52-gene-priA-83333
  - micro52-protein-P07013-network
  - micro52-gene-priB-network
  - micro52-ipr-IPR020917
  - micro52-ipr-IPR005259
  - micro52-ipr-IPR023646
  - micro52-ng1996ii-pdf
findings:
- finding_id: F1
  issue_key: dnab-dnac-dnat-pria-prib-source-stage-conflation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate the loader-containing model from isolated preprimosome composition
  description: Current GO1990158 names a DnaB-DnaC-containing complex, and the record
    turns that model into an unqualified constituent/has_part and graph claim while
    treating Ng experiments as its canonical source. NgI explicitly reports final
    PriA/PriB/DnaT/DnaB without DnaC. NgII pp15653–54 likewise rejects stable DnaC
    membership and retains PriC on intact PhiX174 DNA, unlike the short PAS substrate.
    Input proteins, transient loading and stable isolated composition are therefore
    conflated. Native authority and experimental observation must both remain visible.
  target_ids:
  - GO:1990158
  field_paths:
  - definition
  - has_part
  - components[0]
  - canonical_examples[0]
  - causal_graphs[0].description
  - causal_graphs[0].edges[0]
  - discussions[1]
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-ng1996ii-pdf
  - micro52-pmid-8663104-network
  - micro52-pmid-8663105-network
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and claim-level primary-source scope
  native_severity: major
  normalization_reason: This is a material composition/assembly-stage conflict in
    the cited experimental support, even though the current ontology text is copied
    accurately. It does not establish that transient DnaC-containing intermediates
    are impossible or authorize renaming the record.
- finding_id: F2
  issue_key: dnab-dnac-dnat-pria-prib-complex-exact-component-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve verified existing component-class groundings
  description: DnaT, PriA and PriB exactly map to InterProIPR020917, IPR005259 and
    IPR023646, respectively. DnaT natural proteobacterial scope is stated; the PriB/SSB
    parent and helicase domains are not substituted. Native family/ontology identities
    plus independently inspected protein cross-references establish the matches. The
    current reviewed-label-only/open-task representation leaves these actionable classes
    unresolved. Historical earlier-pass statements are not declared false merely because
    current verification is available.
  target_ids:
  - GO:1990158
  field_paths:
  - components[1].grounding_status
  - components[2].grounding_status
  - components[3].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990158-ancestors-network
  - micro52-GO1990158-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-ipr-IPR020917
  - micro52-ipr-IPR005259
  - micro52-ipr-IPR023646
  - micro52-protein-P0A8J2
  - micro52-gene-dnaT-exact83333
  - micro52-protein-P17888
  - micro52-gene-priA-83333
  - micro52-protein-P07013-network
  - micro52-gene-priB-network
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and claim-level primary-source scope
  native_severity: minor
  normalization_reason: The correct named classes and example identities are retained.
    This is a bounded exact-grounding gap under the explicit local contract, not missing
    optional inventory.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990158
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    role: maintained scientific record
  description: Preserve GO1990158 and explicitly distinguish its loader-containing
    assembly model from the Ng isolated complexes. Qualify the stage/source of DnaC
    parthood and graph membership, identify which substrate/stage the canonical example
    demonstrates, and retain the PriC-dependent intact-DNA versus short-PAS distinction.
    Inspect an appropriate primary source before claiming direct observation of the
    exact DnaC-containing assembly.
  acceptance_checks:
  - Stable composition is not inferred from proteins supplied to the reaction.
  - The action preserves current identity and reports the authority/source conflict
    without silently replacing it.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:1990158
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    role: maintained scientific record
  description: Add the verified exact class CURIEs with source-specific evidence,
    update the corresponding grounding states/open task, and preserve organism accessions
    as examples. Do not force a broader homolog/domain or unresolved PAS-DNA mapping.
  acceptance_checks:
  - Every added CURIE denotes the existing class at the stated scope, not an individual
    species protein.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- NgII entire scientific body/Methods/TableI/captions was read, but no pixels or underlying
  Western reanalysis. NgI is used only at its complete native abstract tier here;
  its indexed1996 erratum content remains uninspected.
- The DnaC finding does not assert that no transient loading intermediate can exist.
  Native GO identity is preserved pending reconciliation with direct source stage/composition.
  No uninspected modern restart study is imported to settle that conflict.
- No exact source-neutral primosome-assembly-site DNA class was independently established.
  This unresolved optional mapping is not automatically a finding; the exact protein-family
  mappings are separately established.
- Initial sandbox fetch/verification DNS failures and successful public-network retries
  are retained separately. Exact source URL, original UTC and SHA are preserved for
  every reused pair.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user requests one review for every unreviewed record, including qualified clean
  records.
- Native ontology/UniProt/family adapters directly answer these component claims.
  No iModulonDB dataset is established or used; computational expression-module membership
  would not prove physical complex formation.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
