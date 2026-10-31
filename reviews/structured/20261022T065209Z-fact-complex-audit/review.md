# Source-backed review of fact complex

- Review: 20261022T065209Z-fact-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:28:06Z
- Finished UTC: 2026-10-22T06:52:09Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One grouped minor: verified exact families can resolve the existing Spt16 and Pob3 grounding task. Core membership, Nhp6 boundary, protein identities and coarse chromatin/transcription functions are supported.

## Scope And Provenance

Exactly one complete maintained target plus frozen governing/schema/protein/graph guidance. Native identifiers and independently read primary/abstract evidence are separated. No neighboring maintained record is an unstated premise.

Selection: Batch55 strict ordered selection, index 4; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0035101 | data/structures/other/fact_complex.yaml | maintained | FACT complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0035101 | Focused validator passed. |
| Focused native strict | passed | True | GO:0035101 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0035101 | Focused native check passed; scientific scope independently assessed. |
| Focused native verify | passed | True | GO:0035101 | Focused native check passed; scientific scope independently assessed. |
| Claim-level scientific review | passed | True | GO:0035101 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0035101 | 10 of 14 collected target identifiers returned OK. PMID:10413469: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:11432837: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:12934006: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:14585989: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0035101 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0035101 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0035101 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0035101 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0035101 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Supported FACT identity and core boundary

identity: supported. Targets: GO:0035101.

The exact GO identity, synonym and parent match. The record explicitly resolves Nhp6 as a cooperating factor rather than a constitutive core row; Formosa and native SUBUNIT evidence support that boundary.

### Two established subunits with actionable exact families

grounding: concern. Targets: GO:0035101.

The Spt16-Pob3 core and taxon-paired examples are supported. The open family-grounding task can be narrowed by exact IPR040258 and IPR000969; the broader RTT106/SSRP1 family is unnecessary.

### Chromatin reorganization and transcription elongation

evidence: supported. Targets: GO:0035101.

Yeast Formosa/Mason evidence and human Belot reconstitution support the coarse FACT functions. Belot is human, while the yeast graph refers to the conserved role and its separately supported Nhp6 cooperation; it does not claim that Belot performed a yeast assay or that proposed histone reinsertion was directly observed.

### Verified accessions and location attribution

grounding: supported. Targets: GO:0035101.

Both maintained examples are correct reviewed S288C identities and single exact-organism query hits. The cited nucleus/chromosome annotations match native evidence blocks. A location citation is not treated as sufficient membership or formation evidence.

### Yeast example and separate human biochemical context

scope: supported. Targets: GO:0035101.

COMMON retains present-in-most-members meaning with exceptional losses. The yeast studies provide qualitative support, not a quantitative census. S288C reference entries do not replace the explicitly distinct assay strains or reconstitution materials; human FACT assays are not relabeled as yeast.

### Four descriptive composition/function edges

graph: supported. Targets: GO:0035101.

The two constituent relations and two broad functions match their typed actors. NONMECHANISTIC is appropriate; no full nucleosome-disassembly/reassembly mechanism is asserted by the graph.

### Existing UNKNOWN labels remain justified

evidence: unknown. Targets: GO:0035101.

Essential genes, catalytic/chaperone activity and chromatin location do not establish universal physical formation necessity. The human truncation experiment explicitly retains subunit complex formation while losing tested activities. The review does not reinterpret UNKNOWN as demonstrated indispensability.

### Whole target reviewed with explicit evidence limits

completeness: supported. Targets: GO:0035101.

All scientific fields, citations, discussions, graph edges and history were reviewed. Findings address exact actionable current tasks, not optional empty slots or historical wording made false merely by later source availability. Unmeasured formation and broader prevalence remain explicit uncertainties.

## Findings

### F1: Resolve the two verified FACT subunit families

minor / open / confirmed; issue key: fact-exact-subunit-family-groundings.

The two existing subunits are REVIEWED_LABEL_ONLY under an open exact-family task. Native IPR040258 identifies Spt16 and IPR000969 identifies SSRP1/POB3, corroborated by the respective native protein cross-references.

## Recommended Actions And Acceptance Checks

### A1

Add InterPro:IPR040258 and InterPro:IPR000969 to the existing Spt16 and Pob3 classes, with source-specific evidence, and update the current grounding state/task. Do not substitute the broader RTT106/SSRP1 family or add Nhp6 as an obligatory core row.

- Each adopted identifier denotes the exact whole-protein class rather than a species example, shared domain or broader mixed family.
- Preserve supported component labels, protein examples and UNKNOWN formation necessity.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/fact_complex.yaml; Complete current YAML, including all citations, component/example fields, graph edges, discussions and history | context_only | The entire target was read. No neighboring maintained record is an unstated premise. |
| curation | docs/CURATION.md; Source-neutral class grounding and label-only review contract | context_only | Verified exact families may resolve explicit current grounding tasks; a protein example is not a family identity. Physical complex formation differs from catalytic activity, viability and localization. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum and PresenceEnum | context_only | UNKNOWN does not assert formation necessity. COMMON means present in most taxon members, with exceptional losses; a model-organism experiment or only_in_taxon constraint is not a prevalence census. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope, actor identity and source-specific edge support | context_only | Descriptive membership/function graphs may remain NONMECHANISTIC. A coarse physical assembly and catalytic reaction can be mechanistic without specifying every intermediate. |
| micro55-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035101,GO:0008023,GO:0034728,GO:0006354,GO:1990202,GO:1990204,GO:0052873,GO:0005760,GO:0042575,GO:0098798,GO:0005759,GO:0006264; Exact FACT/parent/function entries, full definitions/synonyms and relevant typed child relations. Other response entries are not used. | supports | GO0035101 identifies FACT as a histone-chaperone complex, with the exact expanded-name synonym; GO0008023 is its transcription-elongation-factor-complex parent. GO0034728 and GO0006354 are the represented nucleosome-organization and DNA-templated transcription-elongation functions. |
| micro55-GO0035101-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035101/ancestors?relations=is_a; Complete relations=is_a ancestors array. | supports | The is_a-only array confirms transcription elongation factor complex and protein-containing-complex ancestry; the additional GO0140513 identifier is retained without an unchecked label. |
| micro55-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Native taxId, scientificName, rank and lineage fields. | supports | ENA taxId4932 is Saccharomyces cerevisiae, species. |
| micro55-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Native taxId, scientificName, rank and lineage fields. | supports | ENA taxId559292 is Saccharomyces cerevisiae S288C, strain; this is the reference accession background, not every experimental strain. |
| micro55-pmid-10413469 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10413469+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry, exact title/authors/year/DOI/PMID and complete abstractText. No unlisted main-body or individual figure inference. | supports | PMID10413469: Spt16 and Pob3 of Saccharomyces cerevisiae form an essential, abundant heterodimer that is nuclear, chromatin-associated, and copurifies with DNA polymerase alpha. Wittmeyer J, Joss L, Formosa T. (1999), DOI10.1021/bi982851d. Exact identity and complete native abstract were read; source-specific body scope is separately declared. |
| micro55-pmid-11432837 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11432837+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry, exact title/authors/year/DOI/PMID and complete abstractText. No unlisted main-body or individual figure inference. | supports | PMID11432837: Spt16-Pob3 and the HMG protein Nhp6 combine to form the nucleosome-binding factor SPN. Formosa T, Eriksson P, Wittmeyer J, Ginn J, Yu Y, Stillman DJ. (2001), DOI10.1093/emboj/20.13.3506. Exact identity and complete native abstract were read; source-specific body scope is separately declared. |
| micro55-pmid-12934006 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12934006+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry, exact title/authors/year/DOI/PMID and complete abstractText. No unlisted main-body or individual figure inference. | supports | PMID12934006: FACT facilitates transcription-dependent nucleosome alteration. Belotserkovskaya R, Oh S, Bondarenko VA, Orphanides G, Studitsky VM, Reinberg D. (2003), DOI10.1126/science.1085703. Exact identity and complete native abstract were read; source-specific body scope is separately declared. |
| micro55-pmid-14585989 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14585989+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry, exact title/authors/year/DOI/PMID and complete abstractText. No unlisted main-body or individual figure inference. | supports | PMID14585989: The FACT complex travels with elongating RNA polymerase II and is important for the fidelity of transcriptional initiation in vivo. Mason PB, Struhl K. (2003), DOI10.1128/mcb.23.22.8323-8333.2003. Exact identity and complete native abstract were read; source-specific body scope is separately declared. |
| micro55-formosa2001 | https://pmc.ncbi.nlm.nih.gov/articles/125512/; Genuine numeric-PMC125512 HTML: sec1 Introduction; sec6-10 Results; sec13/14 Discussion; sec16 strain/TableIII and sec19 nucleosome-binding Methods; embedded Fig4-6 captions. No pixels, supplements or unlisted sections. | supports | The yeast primary study supports a stable Spt16-Pob3 core with weak/context-dependent Nhp6 association and Nhp6-assisted nucleosome binding/reorganization. It does not establish a constitutive purified Spt16-Pob3-Nhp6 heterotrimer. Its strains include A364a, W303 and S288C derivatives; the reconstituted nucleosomes use sea-urchin 5S DNA and chicken histone octamers. |
| micro55-mason2003 | https://pmc.ncbi.nlm.nih.gov/articles/262413/; Genuine numeric-PMC262413 HTML: Methods sec2/3, Results sec6/7 and embedded Fig1/2 captions. No pixels or unlisted sections. | supports | W303.1A-based tagged-protein ChIP supports recruitment of Spt16/Pob3 to transcribed coding regions and association with Pol II. The paper distinguishes traversal with polymerase from dynamic exchange; the experiments do not alone resolve those alternatives. |
| micro55-belot-browser | https://www.researchgate.net/publication/10601441_FACT_Facilitates_Transcription-Dependent_Nucleosome_Alteration; URL-specific browser-extracted primary representation, status:null. Printed p1090: title/abstract, Introduction and initial human-reconstitution results through the start of the C-terminal analysis, plus Fig1 caption. Original combined representation and derivation receipt retained. | supports | The captured primary paper identifies FACT-mediated nucleosome alteration and explicitly introduces human recombinant FLAG-hSpt16/His-SSRP1. This is direct human biochemical context, not a yeast reconstitution. |
| micro55-belot-browser2 | https://www.researchgate.net/publication/10601441_FACT_Facilitates_Transcription-Dependent_Nucleosome_Alteration; Browser-extracted primary blocks at printed pp1090-1092: recombinant human protein experiments, C-terminal truncation, nucleosome destabilization, hexasome and histone-deposition passages, Fig1/2 and captured portion of Fig3 caption. Exact retained blocks define the scope; intervening uncaptured lines, final paper text, supplements and pixels were not read. | supports | Human FACT truncation experiments separate physical subunit complex formation from chromatin-binding/transcription activity: Spt16 lacking its acidic C-terminus still forms FACT with SSRP1 but loses the tested activities. Captured sections also support transcription-associated H2A-H2B displacement and histone deposition; reinsertion following transcription is proposed as a model, not directly certified here. |
| micro55-protein-P32558 | https://rest.uniprot.org/uniprotkb/P32558.json; Native entryType, primaryAccession, recommendedName, organism/taxonId, genes, complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION blocks and relevant family cross-references. Unlisted annotation citations are not independently certified as papers. | supports | Reviewed S288C P32558 is SPT16. SUBUNIT identifies the stable POB3 heterodimer and weak multiple-Nhp6 association; location cites PMID10413469 with ECO0000269 for nucleus/chromosome. Relevant InterPro membership includes IPR040258. |
| micro55-gene-SPT16 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASPT16%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results identity set; exact gene_exact, organism_id and reviewed:true query retained in URL. This is accession uniqueness, not evidence of complex membership. | supports | The exact reviewed gene query returns one entry, P32558, matching the maintained example and its stated organism. |
| micro55-protein-Q04636 | https://rest.uniprot.org/uniprotkb/Q04636.json; Native entryType, primaryAccession, recommendedName, organism/taxonId, genes, complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION blocks and relevant family cross-references. Unlisted annotation citations are not independently certified as papers. | supports | Reviewed S288C Q04636 is POB3. Its stable SPT16 heterodimer and weak Nhp6 association match the qualified core account. Nucleus PMID10413469 and chromosome PMID10413469/14585989 carry ECO0000269. IPR000969 is present among native family cross-references. |
| micro55-gene-POB3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOB3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results identity set; exact gene_exact, organism_id and reviewed:true query retained in URL. This is accession uniqueness, not evidence of complex membership. | supports | The exact reviewed gene query returns one entry, Q04636, matching the maintained example and its stated organism. |
| micro55-ipr-IPR040258 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040258/; Complete native metadata accession/type/name/description/member-database signature fields. | supports | IPR040258 is the FACT complex subunit Spt16 family, with PTHR13980 signature; this is a whole-protein family rather than a Spt16 domain. |
| micro55-ipr-IPR000969 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000969/; Complete native family identity, description and PRINTS signature metadata. | supports | IPR000969 is the structure-specific recognition protein SSRP1/POB3 family, with PRINTS PR00887. Its family description explicitly includes yeast POB3; the HMG difference between higher-eukaryotic SSRP1 and yeast POB3 does not make it a shared-domain-only entry. |
| micro55-ipr-IPR050454 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050454/; Native family name/type/description and signature fields; unchecked generated prose is not mechanistic evidence. | context_only | IPR050454 includes RTT106 as well as SSRP1; its broader coverage is not used as the exact POB3 replacement. |
| micro55-belot2003 | https://www.science.org/doi/10.1126/science.1085703; Original native request/403 response. | context_only | The direct Science route returned HTTP403 HTML, not the article body. Genuine primary reading is separately retained through browser-extracted blocks. |
| schema-result | just validate data/structures/other/fact_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/fact_complex.yaml |
| strict-result | just validate-strict data/structures/other/fact_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/fact_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/fact_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/fact_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/fact_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/fact_complex.yaml --causal-graphs; Complete focused native read-only report | supports | data/structures/other/fact_complex.yaml  (GO:0035101)<br>  yeast_fact_nucleosome_reorganization	spt16_fact_subunit	COVERED	-&gt;spt16_fact_subunit (UniProtKB:P32558)<br>  yeast_fact_nucleosome_reorganization	pob3_fact_subunit	COVERED	-&gt;pob3_fact_subunit (UniProtKB:Q04636)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/fact_complex.yaml --verify; Complete focused native read-only report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/fact_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 14 collected target identifiers returned OK. PMID:10413469: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:11432837: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:12934006: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:14585989: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Wittmeyer1999 is complete native abstract only. Formosa and Mason reading is limited to the declared sections/captions; no primary figure pixels or supplements were inspected.
- Belot2003 is a genuine browser-extracted primary representation at the exact retained blocks, not native HTTP200 or an unbroken full-paper read. Its direct biochemical system is human recombinant FACT. The blocked Science route remains a diagnostic.
- No universal per-subunit formation necessity or quantitative COMMON census is established. Yeast and human functions are kept separate from identical experimental implementation.
- Original source bytes, URLs, UTC timestamps and SHA256 receipts are retained. Browser-derived URL-specific blocks retain their original combined representation and do not assert native HTTP200.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user requests a review for every unreviewed record, including qualified clean records.
- Native ontology, taxonomic and protein/family databases directly address these claims; no expression-module membership is treated as proof of physical complex membership.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T065209Z-fact-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of fact complex
started_at: '2026-10-22T06:28:06Z'
finished_at: '2026-10-22T06:52:09Z'
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
summary: 'One grouped minor: verified exact families can resolve the existing Spt16
  and Pob3 grounding task. Core membership, Nhp6 boundary, protein identities and
  coarse chromatin/transcription functions are supported.'
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/other/fact_complex.yaml
    sha256: 28c014acbd668aedf2ce72673a18af6d53f64b73c4bed22ebc321068b823219a
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
- target_id: GO:0035101
  path: data/structures/other/fact_complex.yaml
  label: FACT complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/fact_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target plus frozen governing/schema/protein/graph
    guidance. Native identifiers and independently read primary/abstract evidence
    are separated. No neighboring maintained record is an unstated premise.
  selection: Batch55 strict ordered selection, index 4; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0035101
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0035101
  command: just validate data/structures/other/fact_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0035101
  command: just validate-strict data/structures/other/fact_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/fact_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0035101
  command: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/fact_complex.yaml --causal-graphs
  exit_code: 0
  summary: Focused native check passed; scientific scope independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0035101
  command: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/fact_complex.yaml --verify
  exit_code: 0
  summary: Focused native check passed; scientific scope independently assessed.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0035101
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro55-go
  - micro55-GO0035101-ancestors
  - micro55-tax4932
  - micro55-tax559292
  - micro55-pmid-10413469
  - micro55-pmid-11432837
  - micro55-pmid-12934006
  - micro55-pmid-14585989
  - micro55-formosa2001
  - micro55-mason2003
  - micro55-belot-browser
  - micro55-belot-browser2
  - micro55-protein-P32558
  - micro55-gene-SPT16
  - micro55-protein-Q04636
  - micro55-gene-POB3
  - micro55-ipr-IPR040258
  - micro55-ipr-IPR000969
  - micro55-ipr-IPR050454
  - micro55-belot2003
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0035101
  summary: '10 of 14 collected target identifiers returned OK. PMID:10413469: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:11432837: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:12934006: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:14585989: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - micro55-pmid-10413469
  - micro55-pmid-11432837
  - micro55-pmid-12934006
  - micro55-pmid-14585989
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0035101
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0035101
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0035101
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0035101
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0035101
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
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/fact_complex.yaml
  locator: Complete current YAML, including all citations, component/example fields,
    graph edges, discussions and history
  accessed_at: '2026-10-22T06:45:18Z'
  support: context_only
  summary: The entire target was read. No neighboring maintained record is an unstated
    premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Source-neutral class grounding and label-only review contract
  accessed_at: '2026-10-22T06:45:18Z'
  support: context_only
  summary: Verified exact families may resolve explicit current grounding tasks; a
    protein example is not a family identity. Physical complex formation differs from
    catalytic activity, viability and localization.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum and PresenceEnum
  accessed_at: '2026-10-22T06:45:18Z'
  support: context_only
  summary: UNKNOWN does not assert formation necessity. COMMON means present in most
    taxon members, with exceptional losses; a model-organism experiment or only_in_taxon
    constraint is not a prevalence census.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope, actor identity and source-specific edge support
  accessed_at: '2026-10-22T06:45:18Z'
  support: context_only
  summary: Descriptive membership/function graphs may remain NONMECHANISTIC. A coarse
    physical assembly and catalytic reaction can be mechanistic without specifying
    every intermediate.
- evidence_id: micro55-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035101,GO:0008023,GO:0034728,GO:0006354,GO:1990202,GO:1990204,GO:0052873,GO:0005760,GO:0042575,GO:0098798,GO:0005759,GO:0006264
  locator: Exact FACT/parent/function entries, full definitions/synonyms and relevant
    typed child relations. Other response entries are not used.
  accessed_at: '2026-10-22T06:35:36.591500Z'
  support: supports
  summary: GO0035101 identifies FACT as a histone-chaperone complex, with the exact
    expanded-name synonym; GO0008023 is its transcription-elongation-factor-complex
    parent. GO0034728 and GO0006354 are the represented nucleosome-organization and
    DNA-templated transcription-elongation functions.
  snapshot_sha256: 4afb3b0b05daaeda1d6ce52f48b9cae548f1c81ce9b5c4b1e12c97a343bb1f7d
- evidence_id: micro55-GO0035101-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035101/ancestors?relations=is_a
  locator: Complete relations=is_a ancestors array.
  accessed_at: '2026-10-22T06:35:41.826168Z'
  support: supports
  summary: The is_a-only array confirms transcription elongation factor complex and
    protein-containing-complex ancestry; the additional GO0140513 identifier is retained
    without an unchecked label.
  snapshot_sha256: 603e938fd38ce4bb6c606abdacaf30e04a5c5f3c89b74dd376efed2a0e531cc0
- evidence_id: micro55-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Native taxId, scientificName, rank and lineage fields.
  accessed_at: '2026-10-22T06:35:40.360388Z'
  support: supports
  summary: ENA taxId4932 is Saccharomyces cerevisiae, species.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro55-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Native taxId, scientificName, rank and lineage fields.
  accessed_at: '2026-10-22T06:35:40.404100Z'
  support: supports
  summary: ENA taxId559292 is Saccharomyces cerevisiae S288C, strain; this is the
    reference accession background, not every experimental strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro55-pmid-10413469
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10413469+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry, exact title/authors/year/DOI/PMID and complete abstractText.
    No unlisted main-body or individual figure inference.
  accessed_at: '2026-10-22T06:35:36.592030Z'
  support: supports
  summary: 'PMID10413469: Spt16 and Pob3 of Saccharomyces cerevisiae form an essential,
    abundant heterodimer that is nuclear, chromatin-associated, and copurifies with
    DNA polymerase alpha. Wittmeyer J, Joss L, Formosa T. (1999), DOI10.1021/bi982851d.
    Exact identity and complete native abstract were read; source-specific body scope
    is separately declared.'
  snapshot_sha256: 1217a27f71938173243487aa48cb759a799d0190b85c9dbfa0b1bfbae78d9b3c
- evidence_id: micro55-pmid-11432837
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11432837+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry, exact title/authors/year/DOI/PMID and complete abstractText.
    No unlisted main-body or individual figure inference.
  accessed_at: '2026-10-22T06:35:37.328631Z'
  support: supports
  summary: 'PMID11432837: Spt16-Pob3 and the HMG protein Nhp6 combine to form the
    nucleosome-binding factor SPN. Formosa T, Eriksson P, Wittmeyer J, Ginn J, Yu
    Y, Stillman DJ. (2001), DOI10.1093/emboj/20.13.3506. Exact identity and complete
    native abstract were read; source-specific body scope is separately declared.'
  snapshot_sha256: a2beeab47a3182f017cef381ada3802e883a03ba33e0232764a67a03110cf6f6
- evidence_id: micro55-pmid-12934006
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12934006+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry, exact title/authors/year/DOI/PMID and complete abstractText.
    No unlisted main-body or individual figure inference.
  accessed_at: '2026-10-22T06:35:36.593725Z'
  support: supports
  summary: 'PMID12934006: FACT facilitates transcription-dependent nucleosome alteration.
    Belotserkovskaya R, Oh S, Bondarenko VA, Orphanides G, Studitsky VM, Reinberg
    D. (2003), DOI10.1126/science.1085703. Exact identity and complete native abstract
    were read; source-specific body scope is separately declared.'
  snapshot_sha256: f8280ff13fda927598758ab119c414a79af4924a397f6edb79774c1803e3ad6c
- evidence_id: micro55-pmid-14585989
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14585989+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry, exact title/authors/year/DOI/PMID and complete abstractText.
    No unlisted main-body or individual figure inference.
  accessed_at: '2026-10-22T06:35:36.593635Z'
  support: supports
  summary: 'PMID14585989: The FACT complex travels with elongating RNA polymerase
    II and is important for the fidelity of transcriptional initiation in vivo. Mason
    PB, Struhl K. (2003), DOI10.1128/mcb.23.22.8323-8333.2003. Exact identity and
    complete native abstract were read; source-specific body scope is separately declared.'
  snapshot_sha256: 4bb788da3d1eccb39a5f88ae44b8c5dda83f41957c08d0fd56d25f987c01dd0e
- evidence_id: micro55-formosa2001
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/125512/
  locator: 'Genuine numeric-PMC125512 HTML: sec1 Introduction; sec6-10 Results; sec13/14
    Discussion; sec16 strain/TableIII and sec19 nucleosome-binding Methods; embedded
    Fig4-6 captions. No pixels, supplements or unlisted sections.'
  accessed_at: '2026-10-22T06:36:58.848118Z'
  support: supports
  summary: The yeast primary study supports a stable Spt16-Pob3 core with weak/context-dependent
    Nhp6 association and Nhp6-assisted nucleosome binding/reorganization. It does
    not establish a constitutive purified Spt16-Pob3-Nhp6 heterotrimer. Its strains
    include A364a, W303 and S288C derivatives; the reconstituted nucleosomes use sea-urchin
    5S DNA and chicken histone octamers.
  snapshot_sha256: b2138654d474b6bfd687ca3af948c02652bb62c0e3ec72046f12a50a1f17dfe5
- evidence_id: micro55-mason2003
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/262413/
  locator: 'Genuine numeric-PMC262413 HTML: Methods sec2/3, Results sec6/7 and embedded
    Fig1/2 captions. No pixels or unlisted sections.'
  accessed_at: '2026-10-22T06:36:59.428446Z'
  support: supports
  summary: W303.1A-based tagged-protein ChIP supports recruitment of Spt16/Pob3 to
    transcribed coding regions and association with Pol II. The paper distinguishes
    traversal with polymerase from dynamic exchange; the experiments do not alone
    resolve those alternatives.
  snapshot_sha256: d6fbde3460090b63744f2a146fb623c200eb3e285a2f6433da0d104f4787d6a3
- evidence_id: micro55-belot-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/10601441_FACT_Facilitates_Transcription-Dependent_Nucleosome_Alteration
  locator: 'URL-specific browser-extracted primary representation, status:null. Printed
    p1090: title/abstract, Introduction and initial human-reconstitution results through
    the start of the C-terminal analysis, plus Fig1 caption. Original combined representation
    and derivation receipt retained.'
  accessed_at: '2026-10-22T06:41:06.942414Z'
  support: supports
  summary: The captured primary paper identifies FACT-mediated nucleosome alteration
    and explicitly introduces human recombinant FLAG-hSpt16/His-SSRP1. This is direct
    human biochemical context, not a yeast reconstitution.
  snapshot_sha256: 8576250893d93b4c0dbaeb9b4e5e7034928975a129400409e208178aa568396b
- evidence_id: micro55-belot-browser2
  kind: primary_source
  reference: https://www.researchgate.net/publication/10601441_FACT_Facilitates_Transcription-Dependent_Nucleosome_Alteration
  locator: 'Browser-extracted primary blocks at printed pp1090-1092: recombinant human
    protein experiments, C-terminal truncation, nucleosome destabilization, hexasome
    and histone-deposition passages, Fig1/2 and captured portion of Fig3 caption.
    Exact retained blocks define the scope; intervening uncaptured lines, final paper
    text, supplements and pixels were not read.'
  accessed_at: '2026-10-22T06:41:06.943231Z'
  support: supports
  summary: 'Human FACT truncation experiments separate physical subunit complex formation
    from chromatin-binding/transcription activity: Spt16 lacking its acidic C-terminus
    still forms FACT with SSRP1 but loses the tested activities. Captured sections
    also support transcription-associated H2A-H2B displacement and histone deposition;
    reinsertion following transcription is proposed as a model, not directly certified
    here.'
  snapshot_sha256: 6e86108211937b86caebb3ee86b76bddf810239b474509a65d70025e67f8c372
- evidence_id: micro55-protein-P32558
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32558.json
  locator: Native entryType, primaryAccession, recommendedName, organism/taxonId,
    genes, complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION blocks and relevant family
    cross-references. Unlisted annotation citations are not independently certified
    as papers.
  accessed_at: '2026-10-22T06:35:38.007768Z'
  support: supports
  summary: Reviewed S288C P32558 is SPT16. SUBUNIT identifies the stable POB3 heterodimer
    and weak multiple-Nhp6 association; location cites PMID10413469 with ECO0000269
    for nucleus/chromosome. Relevant InterPro membership includes IPR040258.
  snapshot_sha256: 6be6279235f17c1133cf413181adc45f03b40bf54098fcdb890668ee37ff77f9
- evidence_id: micro55-gene-SPT16
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASPT16%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results identity set; exact gene_exact, organism_id and reviewed:true
    query retained in URL. This is accession uniqueness, not evidence of complex membership.
  accessed_at: '2026-10-22T06:35:39.328404Z'
  support: supports
  summary: The exact reviewed gene query returns one entry, P32558, matching the maintained
    example and its stated organism.
  snapshot_sha256: 0b55541eacab9ac6e6c83e868168a9eb19ffb7b552ac12709b53a0ba79a0c13b
- evidence_id: micro55-protein-Q04636
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04636.json
  locator: Native entryType, primaryAccession, recommendedName, organism/taxonId,
    genes, complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION blocks and relevant family
    cross-references. Unlisted annotation citations are not independently certified
    as papers.
  accessed_at: '2026-10-22T06:35:38.564327Z'
  support: supports
  summary: Reviewed S288C Q04636 is POB3. Its stable SPT16 heterodimer and weak Nhp6
    association match the qualified core account. Nucleus PMID10413469 and chromosome
    PMID10413469/14585989 carry ECO0000269. IPR000969 is present among native family
    cross-references.
  snapshot_sha256: bf60940520544903bb37811c5f85994536055e02f61a0d273cc7c0032df4c083
- evidence_id: micro55-gene-POB3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOB3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results identity set; exact gene_exact, organism_id and reviewed:true
    query retained in URL. This is accession uniqueness, not evidence of complex membership.
  accessed_at: '2026-10-22T06:35:39.386126Z'
  support: supports
  summary: The exact reviewed gene query returns one entry, Q04636, matching the maintained
    example and its stated organism.
  snapshot_sha256: 2aa3b82e77034e93b459d06d94f789c29b711dfea49de3409ee0f70ba6f0db89
- evidence_id: micro55-ipr-IPR040258
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040258/
  locator: Complete native metadata accession/type/name/description/member-database
    signature fields.
  accessed_at: '2026-10-22T06:36:18.441743Z'
  support: supports
  summary: IPR040258 is the FACT complex subunit Spt16 family, with PTHR13980 signature;
    this is a whole-protein family rather than a Spt16 domain.
  snapshot_sha256: 7dc6199ad8368691287b783fdc043236ad42eb24a80acba50d6931312c15e9fe
- evidence_id: micro55-ipr-IPR000969
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000969/
  locator: Complete native family identity, description and PRINTS signature metadata.
  accessed_at: '2026-10-22T06:36:56.347576Z'
  support: supports
  summary: IPR000969 is the structure-specific recognition protein SSRP1/POB3 family,
    with PRINTS PR00887. Its family description explicitly includes yeast POB3; the
    HMG difference between higher-eukaryotic SSRP1 and yeast POB3 does not make it
    a shared-domain-only entry.
  snapshot_sha256: 19451ae953fb0532e9b74127d4206ae49e564fe95bf2a8e63f319403b1832535
- evidence_id: micro55-ipr-IPR050454
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050454/
  locator: Native family name/type/description and signature fields; unchecked generated
    prose is not mechanistic evidence.
  accessed_at: '2026-10-22T06:36:18.441900Z'
  support: context_only
  summary: IPR050454 includes RTT106 as well as SSRP1; its broader coverage is not
    used as the exact POB3 replacement.
  snapshot_sha256: f114d77c71dfe613c240c4c7cf8f2e16ca87d6cdf2b48f2505fbdc4d170a5bb7
- evidence_id: micro55-belot2003
  kind: authority
  reference: https://www.science.org/doi/10.1126/science.1085703
  locator: Original native request/403 response.
  accessed_at: '2026-10-22T06:37:00.475582Z'
  support: context_only
  summary: The direct Science route returned HTTP403 HTML, not the article body. Genuine
    primary reading is separately retained through browser-extracted blocks.
  snapshot_sha256: 33150b9a2eef5c3835c0f442cdf25762edb935325aec5cc32072bafc73acf016
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/fact_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:28:08Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/fact_complex.yaml'
  snapshot_sha256: 064baaf33c76d8b252b1a750938d1bbd8aac31d7150f278c1864bf32471eedb0
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/fact_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/fact_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:28:10Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/fact_complex.yaml\
    \ --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/fact_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/fact_complex-strict.tsv"
  snapshot_sha256: e2d558298a2318ae3b264198a7f894ea31befbb5c6fb1dd252588d633edb8711
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/fact_complex.yaml --causal-graphs
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T06:41:47.846561Z'
  support: supports
  summary: "data/structures/other/fact_complex.yaml  (GO:0035101)\n  yeast_fact_nucleosome_reorganization\t\
    spt16_fact_subunit\tCOVERED\t->spt16_fact_subunit (UniProtKB:P32558)\n  yeast_fact_nucleosome_reorganization\t\
    pob3_fact_subunit\tCOVERED\t->pob3_fact_subunit (UniProtKB:Q04636)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 564343089c790c3976a2096f605a72df5ebe0ad67af0969f3f6d41a88005eb8a
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/fact_complex.yaml --verify
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T06:41:49.310904Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/fact_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 14 collected target identifiers returned OK. PMID:10413469: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:11432837: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:12934006: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:14585989: UNREACHABLE;
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
  topic: Supported FACT identity and core boundary
  outcome: supported
  target_ids:
  - GO:0035101
  summary: The exact GO identity, synonym and parent match. The record explicitly
    resolves Nhp6 as a cooperating factor rather than a constitutive core row; Formosa
    and native SUBUNIT evidence support that boundary.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro55-go
  - micro55-GO0035101-ancestors
  - micro55-tax4932
  - micro55-tax559292
  - micro55-formosa2001
  - micro55-protein-P32558
  - micro55-gene-SPT16
  - micro55-protein-Q04636
  - micro55-gene-POB3
- assessment_id: composition
  area: grounding
  topic: Two established subunits with actionable exact families
  outcome: concern
  target_ids:
  - GO:0035101
  summary: The Spt16-Pob3 core and taxon-paired examples are supported. The open family-grounding
    task can be narrowed by exact IPR040258 and IPR000969; the broader RTT106/SSRP1
    family is unnecessary.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro55-go
  - micro55-GO0035101-ancestors
  - micro55-tax4932
  - micro55-tax559292
  - micro55-protein-P32558
  - micro55-gene-SPT16
  - micro55-protein-Q04636
  - micro55-gene-POB3
  - micro55-formosa2001
  - micro55-ipr-IPR040258
  - micro55-ipr-IPR000969
  - micro55-ipr-IPR050454
- assessment_id: function
  area: evidence
  topic: Chromatin reorganization and transcription elongation
  outcome: supported
  target_ids:
  - GO:0035101
  summary: Yeast Formosa/Mason evidence and human Belot reconstitution support the
    coarse FACT functions. Belot is human, while the yeast graph refers to the conserved
    role and its separately supported Nhp6 cooperation; it does not claim that Belot
    performed a yeast assay or that proposed histone reinsertion was directly observed.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro55-go
  - micro55-GO0035101-ancestors
  - micro55-tax4932
  - micro55-tax559292
  - micro55-pmid-10413469
  - micro55-pmid-11432837
  - micro55-pmid-12934006
  - micro55-pmid-14585989
  - micro55-formosa2001
  - micro55-mason2003
  - micro55-belot-browser
  - micro55-belot-browser2
- assessment_id: examples
  area: grounding
  topic: Verified accessions and location attribution
  outcome: supported
  target_ids:
  - GO:0035101
  summary: Both maintained examples are correct reviewed S288C identities and single
    exact-organism query hits. The cited nucleus/chromosome annotations match native
    evidence blocks. A location citation is not treated as sufficient membership or
    formation evidence.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro55-go
  - micro55-GO0035101-ancestors
  - micro55-tax4932
  - micro55-tax559292
  - micro55-protein-P32558
  - micro55-gene-SPT16
  - micro55-protein-Q04636
  - micro55-gene-POB3
  - micro55-pmid-10413469
  - micro55-pmid-11432837
  - micro55-pmid-12934006
  - micro55-pmid-14585989
- assessment_id: scope
  area: scope
  topic: Yeast example and separate human biochemical context
  outcome: supported
  target_ids:
  - GO:0035101
  summary: COMMON retains present-in-most-members meaning with exceptional losses.
    The yeast studies provide qualitative support, not a quantitative census. S288C
    reference entries do not replace the explicitly distinct assay strains or reconstitution
    materials; human FACT assays are not relabeled as yeast.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro55-go
  - micro55-GO0035101-ancestors
  - micro55-tax4932
  - micro55-tax559292
  - micro55-formosa2001
  - micro55-mason2003
  - micro55-belot-browser
  - micro55-protein-P32558
  - micro55-gene-SPT16
  - micro55-protein-Q04636
  - micro55-gene-POB3
- assessment_id: graph
  area: graph
  topic: Four descriptive composition/function edges
  outcome: supported
  target_ids:
  - GO:0035101
  summary: The two constituent relations and two broad functions match their typed
    actors. NONMECHANISTIC is appropriate; no full nucleosome-disassembly/reassembly
    mechanism is asserted by the graph.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro55-go
  - micro55-GO0035101-ancestors
  - micro55-tax4932
  - micro55-tax559292
  - micro55-formosa2001
  - micro55-belot-browser
  - micro55-belot-browser2
  - micro55-pmid-10413469
  - micro55-pmid-11432837
  - micro55-pmid-12934006
  - micro55-pmid-14585989
- assessment_id: formation
  area: evidence
  topic: Existing UNKNOWN labels remain justified
  outcome: unknown
  target_ids:
  - GO:0035101
  summary: Essential genes, catalytic/chaperone activity and chromatin location do
    not establish universal physical formation necessity. The human truncation experiment
    explicitly retains subunit complex formation while losing tested activities. The
    review does not reinterpret UNKNOWN as demonstrated indispensability.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro55-go
  - micro55-GO0035101-ancestors
  - micro55-tax4932
  - micro55-tax559292
  - micro55-formosa2001
  - micro55-belot-browser2
- assessment_id: coverage
  area: completeness
  topic: Whole target reviewed with explicit evidence limits
  outcome: supported
  target_ids:
  - GO:0035101
  summary: All scientific fields, citations, discussions, graph edges and history
    were reviewed. Findings address exact actionable current tasks, not optional empty
    slots or historical wording made false merely by later source availability. Unmeasured
    formation and broader prevalence remain explicit uncertainties.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro55-go
  - micro55-GO0035101-ancestors
  - micro55-tax4932
  - micro55-tax559292
  - micro55-formosa2001
  - micro55-mason2003
  - micro55-belot-browser
  - micro55-belot-browser2
  - micro55-protein-P32558
  - micro55-gene-SPT16
  - micro55-protein-Q04636
  - micro55-gene-POB3
  - micro55-ipr-IPR040258
  - micro55-ipr-IPR000969
  - micro55-pmid-10413469
  - micro55-pmid-11432837
  - micro55-pmid-12934006
  - micro55-pmid-14585989
findings:
- finding_id: F1
  issue_key: fact-exact-subunit-family-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the two verified FACT subunit families
  description: The two existing subunits are REVIEWED_LABEL_ONLY under an open exact-family
    task. Native IPR040258 identifies Spt16 and IPR000969 identifies SSRP1/POB3, corroborated
    by the respective native protein cross-references.
  target_ids:
  - GO:0035101
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - components[1].grounding_status
  - components[1].grounding_notes
  - discussions[1]
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro55-go
  - micro55-GO0035101-ancestors
  - micro55-tax4932
  - micro55-tax559292
  - micro55-protein-P32558
  - micro55-gene-SPT16
  - micro55-protein-Q04636
  - micro55-gene-POB3
  - micro55-ipr-IPR040258
  - micro55-ipr-IPR000969
  - micro55-ipr-IPR050454
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/fact_complex.yaml
    role: maintained scientific record
  rule_id: Exact component-class grounding under the explicit current task
  native_severity: minor
  normalization_reason: This is a bounded actionable grounding gap in an otherwise
    supported two-subunit core. It does not invalidate the correct labels, examples,
    Nhp6 boundary or coarse functions.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0035101
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/fact_complex.yaml
    role: maintained scientific record
  description: Add InterPro:IPR040258 and InterPro:IPR000969 to the existing Spt16
    and Pob3 classes, with source-specific evidence, and update the current grounding
    state/task. Do not substitute the broader RTT106/SSRP1 family or add Nhp6 as an
    obligatory core row.
  acceptance_checks:
  - Each adopted identifier denotes the exact whole-protein class rather than a species
    example, shared domain or broader mixed family.
  - Preserve supported component labels, protein examples and UNKNOWN formation necessity.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- Wittmeyer1999 is complete native abstract only. Formosa and Mason reading is limited
  to the declared sections/captions; no primary figure pixels or supplements were
  inspected.
- Belot2003 is a genuine browser-extracted primary representation at the exact retained
  blocks, not native HTTP200 or an unbroken full-paper read. Its direct biochemical
  system is human recombinant FACT. The blocked Science route remains a diagnostic.
- No universal per-subunit formation necessity or quantitative COMMON census is established.
  Yeast and human functions are kept separate from identical experimental implementation.
- Original source bytes, URLs, UTC timestamps and SHA256 receipts are retained. Browser-derived
  URL-specific blocks retain their original combined representation and do not assert
  native HTTP200.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user requests a review for every unreviewed record, including qualified clean
  records.
- Native ontology, taxonomic and protein/family databases directly address these claims;
  no expression-module membership is treated as proof of physical complex membership.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
