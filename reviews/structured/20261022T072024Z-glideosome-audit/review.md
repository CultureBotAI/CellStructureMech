# Source-grounded review of glideosome

- Review: 20261022T072024Z-glideosome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:59:40Z
- Finished UTC: 2026-10-22T07:20:24Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor finding preserves the source-specific GAP50 tail-dependent association and staged assembly result. The scoped glideosome core, exact GAP45 identity, qualified protein examples and broad motor functions are supported.

## Scope And Provenance

Exactly one complete maintained target, with source-native and primary reading scopes declared individually.

Selection: One complete record in strict-path batch 56 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0160055 | data/structures/other/glideosome.yaml | maintained | glideosome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0160055 | Focused validator passed. |
| Focused native strict | passed | True | GO:0160055 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0160055 | Focused check passed; scientific claims assessed separately. |
| Native focused verify | passed | True | GO:0160055 | Focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0160055 | No iModulon-specific claim is assessed; the relevant complex/assay evidence was inspected directly. |
| Claim-level scientific review | passed | True | GO:0160055 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0160055 | 14 of 16 collected target identifiers returned OK. PMID:10749937: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; Pfam:PF29346: SKIPPED; Exact native PF29346 GAP45 identifier and integrated IPR063210 family identity independently read. The native type label is domain; class scope and reference-protein membership are separately assessed in the scientific review. The skipped bulk prefix is not itself native authority verification. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0160055 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0160055 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0160055 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0160055 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0160055 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### GO glideosome and historical four-class core

identity: supported. Targets: GO:0160055.

Exact GO identity and protein-complex parent agree. The primary Toxoplasma study supports the four named core classes and IMC localization. The existing light-chain cohort properly accommodates MLC1/MTIP-like homologs and should not be narrowed back to one species gene.

### Exact GAP45 and appropriately unresolved broader candidates

grounding: supported. Targets: GO:0160055.

The existing GAP45 mapping is supported by its integrated family and native reference accession. The other inspected candidate entries are shared domains or broader families, so no exact replacement is forced. Four examples retain their actual reviewed/unreviewed statuses; MyoA lacks a native gene field and MLC1 is indexed by an ORF name.

### Direct stage and tail-dependent association evidence

grounding: concern. Targets: GO:0160055.

The generic GAP50 anchor role is correct but omits directly measured staged assembly and failure of the tail-deletion construct to associate. The pulse/chase result and transient-expression coimmunoprecipitation are distinct from the later failure to recover stable transfectants, which is not itself a direct formation assay.

### Supported scoped associations and motor outcomes

graph: supported. Targets: GO:0160055.

All four membership/anchor edges and the IMC-localization edge are supported by Gaskins. GO and complete native abstracts of the two cited reviews support the broad gliding/invasion outcomes. NONMECHANISTIC scope appropriately excludes a full actin/adhesin mechanism and later accessory proteins.

### Apicomplexan scope and distinct assay/reference strains

scope: supported. Targets: GO:0160055.

The 2009 review abstract treats apicomplexan glideosomes and GO defines the broader class. The primary assay used RH(HXGPRT-negative) Toxoplasma, whereas the MLC1 reference accession is ME49. Quantitative labeled-protein ratios were only interpreted as consistent with a heterotetramer by the source, not definitive fixed stoichiometry.

### Complete maintained target and bounded follow-up

completeness: supported. Targets: GO:0160055.

Every maintained field, evidence row, component/example, graph edge, discussion and history entry was read. Optional unpopulated slots are not defects. Scientific status/history remain unchanged.

### Universal individual-constituent formation requirements

grounding: unknown. Targets: GO:0160055.

The bounded physical-association and activity observations assessed above do not establish a universal individual-constituent necessity profile for formation of this structure. Unspecified requirements remain unknown; they are not presumed essential or treated as a new corrective finding.

## Findings

### F1: Preserve the tested GAP50 association dependency

minor / open / confirmed; issue key: glideosome-gap50-tail-dependent-association.

The cited primary body separates the soluble MyoA/MLC1/GAP45 precursor from later GAP50 association and reports loss of motor coassociation for the GAP50 C-terminal-tail deletion construct. Current role and anchors/assembles-into edges omit this concrete conditional assembly evidence.

## Recommended Actions And Acceptance Checks

### A1

Add the source-specific staged association and GAP50-tail perturbation results with their assay context, keeping association, localization and viability as distinct outcomes.

- State the 15-minute pulse versus 4-hour chase context for the staged association experiment and the transient-expression coimmunoprecipitation context for the tail construct.
- Name the reported construct without resolving the paper's discrepancy between its residue-range label and method residue count by guesswork.
- Do not infer universal necessity for every component, fixed heterotetramer stoichiometry, or enzymatic GAP50 activity.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/glideosome.yaml; Entire maintained target, including all components, evidence, graph edges, discussions and history | context_only | The complete target was read. The maintained YAML owns any later scientific correction. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope | context_only | Formation necessity is distinct from activity, localization and viability. COMMON is the qualitative category present in most members with exceptional losses, not a measured prevalence census. |
| curation | docs/CURATION.md; Exact class identity and taxon-paired protein examples | context_only | Protein examples do not replace constituent-class grounding. Shared domains and broader paralog families do not resolve exact class tasks. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Scope and edge-level source support | context_only | Descriptive membership graphs need not assert a complete mechanism; a directly observed conditional physical dependency can be stated without making every constituent universally essential. |
| root56-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0005789,GO:0006260,GO:0032991,GO:0043529,GO:0070258,GO:0071816,GO:0071980,GO:0140534,GO:0160055; Native identities, status, complete definitions/comments/synonyms and focal typed relationships | supports | The ten inspected terms establish the focal GET, GINS and glideosome identities, their declared parent classes and the named process/localization targets. Only relevant typed relations were used. |
| root56-sources-GO0160055-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160055/ancestors?relations=is_a; Complete native is_a ancestor response | supports | The complete is_a-only ancestry supports the declared parent class. It does not establish parthood or taxonomic frequency. |
| root56-sources-tax-5794 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794; Complete native taxonomy response | supports | Native taxId 5794 identifies Apicomplexa; broad taxon, species and reference strain are kept distinct. |
| root56-sources-tax-5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; Complete native taxonomy response | supports | Native taxId 5811 identifies Toxoplasma gondii; broad taxon, species and reference strain are kept distinct. |
| root56-sources-tax-508771 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/508771; Complete native taxonomy response | supports | Native taxId 508771 identifies Toxoplasma gondii ME49; broad taxon, species and reference strain are kept distinct. |
| root56-sources-pmid-10749937 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10749937+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 10749937: A dibasic motif in the tail of a class XIV apicomplexan myosin is an essential determinant of plasma membrane localization. Hettmann C, Herm A, Geiter A, Frank B, Schwarz E, Soldati T, Soldati D. (2000); DOI 10.1091/mbc.11.4.1385. Entire native abstract read; this evidence row does not claim the paper body. |
| root56-sources-doi-10.1016_j.mib.2009.06.008 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.mib.2009.06.008%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED 19577950: Mechanisms controlling glideosome function in apicomplexans. Daher W, Soldati-Favre D. (2009). Complete abstract read; body evidence is separately located. |
| root56-sources-doi-10.1046_j.1365-2958.2002.03056.x | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1046%2Fj.1365-2958.2002.03056.x%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED 12139608: 'The glideosome': a dynamic complex powering gliding motion and host cell invasion by Toxoplasma gondii. Opitz C, Soldati D. (2002). Complete abstract read; body evidence is separately located. |
| root56-sources-doi-10.1083_jcb.200311137 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200311137%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED 15123738: Identification of the membrane receptor of a class XIV myosin in Toxoplasma gondii. Gaskins E, Gilk S, DeVore N, Mann T, Ward G, Beckers C. (2004). Complete abstract read; body evidence is separately located. |
| root56-sources-protein-O00934 | https://rest.uniprot.org/uniprotkb/O00934.json; Identity/status/names, genes/aliases, organism and family cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | O00934: The reviewed Myosin-A entry has no native gene field; MyoA is a protein short name, not an exact-gene search hit. |
| root56-sources-gene-MyoA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMyoA%29+AND+%28organism_id%3A5811%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set and literal native query parameters | supports | The exact-gene MyoA query returns no result, consistent with the reviewed entry lacking a gene field. Accession identity is verified directly; this is not evidence that MyoA is absent. |
| root56-sources-protein-A0A125YYD4 | https://rest.uniprot.org/uniprotkb/A0A125YYD4.json; Identity/status/names, genes/aliases, organism and family cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | A0A125YYD4: The unreviewed MLC1 entry lists TGME49_257680 as an orfName, rather than a primary geneName. Its ME49 identity is separate from the primary RH assay background. |
| root56-sources-gene-TGME49_257680 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATGME49_257680%29+AND+%28organism_id%3A508771%29&amp;format=json&amp;size=500; Whole returned identity set and literal native query parameters | supports | The query restricted to the declared organism and gene/locus returns exactly A0A125YYD4; reviewed filtering is used only for reviewed examples. |
| root56-sources-protein-Q7Z289 | https://rest.uniprot.org/uniprotkb/Q7Z289.json; Identity/status/names, genes/aliases, organism and family cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | Q7Z289: The unreviewed GAP45 entry corroborates the gene/taxon identity and IPR063210/PF29346 cross-references. |
| root56-sources-gene-GAP45 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AGAP45%29+AND+%28organism_id%3A5811%29&amp;format=json&amp;size=500; Whole returned identity set and literal native query parameters | supports | The query restricted to the declared organism and gene/locus returns exactly Q7Z289; reviewed filtering is used only for reviewed examples. |
| root56-sources-protein-Q6PQ42 | https://rest.uniprot.org/uniprotkb/Q6PQ42.json; Identity/status/names, genes/aliases, organism and family cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | Q6PQ42: The unreviewed entry carries the native acid-phosphatase label and GAP50 gene identity; its cited Gaskins paper establishes glideosome membership. Automated enzyme naming is not evidence of catalytic activity. |
| root56-sources-gene-GAP50 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AGAP50%29+AND+%28organism_id%3A5811%29&amp;format=json&amp;size=500; Whole returned identity set and literal native query parameters | supports | The query restricted to the declared organism and gene/locus returns exactly Q6PQ42; reviewed filtering is used only for reviewed examples. |
| root56-sources-ipr-IPR063210 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063210/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | The native whole-family entry identifies GAP45 and integrates PF29346; its Plasmodium-specific recruitment prose is not substituted for the primary Toxoplasma experiments. |
| root56-sources-pfam-PF29346 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF29346/; Native accession/name/type, complete description and integrated InterPro identity | supports | PF29346 names GAP45 and integrates into the exact IPR063210 family, although its native API type is domain. This type label alone does not contradict the exact GAP45 signature or prove that the record has the wrong constituent identity. |
| root56-sources-ipr-IPR036044 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR036044/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | A MyoA/MyoB-associated domain is broader than the complete glideosome MyoA class. |
| root56-sources-ipr-IPR049007 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR049007/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | The MTIP-associated N-terminal EF-hand domain does not represent the entire source-neutral glideosome light-chain cohort. |
| root56-sources-ipr-IPR024927 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024927/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | The purple-acid-phosphatase family includes GAP50 but also other proteins; homologous class coverage is broader than the specific glideosome receptor task. |
| root56-sources-ipr-IPR051558 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051558/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | This broader purple-acid-phosphatase family has an unchecked generated description and is not an exact GAP50 mapping or independent proof of enzymatic activity. |
| root56-sources-PMC2172186-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC2172186/; Results sec4, sec5, sec6 and sec7 in full, including embedded Figures 3–7 captions; Methods sec10, sec13, sec14, sec15 and sec17 in full | supports | Gaskins 2004 identifies MyoA/MLC1/GAP45/GAP50 coassociation and GAP50 localization to the IMC. Pulse/chase experiments distinguish a soluble three-protein precursor from later GAP50-associated membrane complex; a GAP50 C-terminal-tail deletion construct fails to associate with the motor components in the stated transient-expression assay. |
| schema-result | just validate data/structures/other/glideosome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/glideosome.yaml |
| strict-result | just validate-strict data/structures/other/glideosome.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glideosome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/glideosome.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glideosome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glideosome-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/glideosome.yaml --causal-graphs; Complete focused native report | supports | data/structures/other/glideosome.yaml  (GO:0160055)<br>  gap50_anchored_glideosome_motor	myoa_class_xiv_myosin_heavy_chain	COVERED	-&gt;myoa_class_xiv_myosin_heavy_chain (UniProtKB:O00934)<br>  gap50_anchored_glideosome_motor	glideosome_myosin_light_chains	COVERED	-&gt;glideosome_myosin_light_chains (UniProtKB:A0A125YYD4)<br>  gap50_anchored_glideosome_motor	gap45_glideosome_associated_protein	COVERED	-&gt;gap45_glideosome_associated_protein (UniProtKB:Q7Z289)<br>  gap50_anchored_glideosome_motor	gap50_membrane_receptor	COVERED	-&gt;gap50_membrane_receptor (UniProtKB:Q6PQ42)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/glideosome.yaml --verify; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/glideosome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 16 collected target identifiers returned OK. PMID:10749937: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; Pfam:PF29346: SKIPPED; Exact native PF29346 GAP45 identifier and integrated IPR063210 family identity independently read. The native type label is domain; class scope and reference-protein membership are separately assessed in the scientific review. The skipped bulk prefix is not itself native authority verification. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five same-base batch26 corpus gates and exact target resolver rows are integrated with every manifested input hash verified.
- No figure pixels, raw datasets, sequence alignments, atomic coordinates or supplementary files were reanalyzed. Primary body reading is limited to declared sections and embedded captions.
- Any absence finding is confined to the complete inspected target and its existing task; no claim is made that a related record or identifier is absent from the corpus or all databases.
- Opitz 2002, Daher 2009 and Hettmann 2000 were read at complete native abstract tier only. Gaskins body scopes are exact; Figure 2 caption, figure pixels and supplements were not read.
- The record reports a historical core and explicitly defers later GAP40/GAPM/accessory reconciliation. This review does not claim exhaustive present-day motor composition or species-wide quantitative prevalence.
- The source labels its tail-deletion construct by a residue range but describes a different residue count in Methods; no count is silently harmonized. Broad or generated phosphatase annotations are not accepted as direct GAP50 activity evidence.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations and issue-bearing reviews alike.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T072024Z-glideosome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of glideosome
started_at: '2026-10-22T06:59:40Z'
finished_at: '2026-10-22T07:20:24Z'
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
summary: One minor finding preserves the source-specific GAP50 tail-dependent association
  and staged assembly result. The scoped glideosome core, exact GAP45 identity, qualified
  protein examples and broad motor functions are supported.
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
  - path: data/structures/other/glideosome.yaml
    sha256: 29dfb078103c9a34a2d39e6d57499f9f781e94be53b968edcc6172057530a4f3
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
- target_id: GO:0160055
  path: data/structures/other/glideosome.yaml
  label: glideosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glideosome.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, with source-native and primary
    reading scopes declared individually.
  selection: One complete record in strict-path batch 56 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0160055
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0160055
  command: just validate data/structures/other/glideosome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0160055
  command: just validate-strict data/structures/other/glideosome.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glideosome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0160055
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glideosome.yaml --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0160055
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glideosome.yaml --verify
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0160055
  summary: No iModulon-specific claim is assessed; the relevant complex/assay evidence
    was inspected directly.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0160055
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root56-sources-go
  - root56-sources-GO0160055-ancestors
  - root56-sources-tax-5794
  - root56-sources-tax-5811
  - root56-sources-tax-508771
  - root56-sources-pmid-10749937
  - root56-sources-doi-10.1016_j.mib.2009.06.008
  - root56-sources-doi-10.1046_j.1365-2958.2002.03056.x
  - root56-sources-doi-10.1083_jcb.200311137
  - root56-sources-protein-O00934
  - root56-sources-gene-MyoA
  - root56-sources-protein-A0A125YYD4
  - root56-sources-gene-TGME49_257680
  - root56-sources-protein-Q7Z289
  - root56-sources-gene-GAP45
  - root56-sources-protein-Q6PQ42
  - root56-sources-gene-GAP50
  - root56-sources-ipr-IPR063210
  - root56-sources-pfam-PF29346
  - root56-sources-ipr-IPR036044
  - root56-sources-ipr-IPR049007
  - root56-sources-ipr-IPR024927
  - root56-sources-ipr-IPR051558
  - root56-sources-PMC2172186-html
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0160055
  summary: '14 of 16 collected target identifiers returned OK. PMID:10749937: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; Pfam:PF29346: SKIPPED;
    Exact native PF29346 GAP45 identifier and integrated IPR063210 family identity
    independently read. The native type label is domain; class scope and reference-protein
    membership are separately assessed in the scientific review. The skipped bulk
    prefix is not itself native authority verification. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root56-sources-pmid-10749937
  - root56-sources-pfam-PF29346
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0160055
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0160055
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0160055
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0160055
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0160055
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
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/glideosome.yaml
  locator: Entire maintained target, including all components, evidence, graph edges,
    discussions and history
  accessed_at: '2026-10-22T07:05:16Z'
  support: context_only
  summary: The complete target was read. The maintained YAML owns any later scientific
    correction.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope
  accessed_at: '2026-10-22T07:05:16Z'
  support: context_only
  summary: Formation necessity is distinct from activity, localization and viability.
    COMMON is the qualitative category present in most members with exceptional losses,
    not a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and taxon-paired protein examples
  accessed_at: '2026-10-22T07:05:16Z'
  support: context_only
  summary: Protein examples do not replace constituent-class grounding. Shared domains
    and broader paralog families do not resolve exact class tasks.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope and edge-level source support
  accessed_at: '2026-10-22T07:05:16Z'
  support: context_only
  summary: Descriptive membership graphs need not assert a complete mechanism; a directly
    observed conditional physical dependency can be stated without making every constituent
    universally essential.
- evidence_id: root56-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0005789,GO:0006260,GO:0032991,GO:0043529,GO:0070258,GO:0071816,GO:0071980,GO:0140534,GO:0160055
  locator: Native identities, status, complete definitions/comments/synonyms and focal
    typed relationships
  accessed_at: '2026-10-22T06:55:10.748737Z'
  support: supports
  summary: The ten inspected terms establish the focal GET, GINS and glideosome identities,
    their declared parent classes and the named process/localization targets. Only
    relevant typed relations were used.
  snapshot_sha256: 09032cf2d48c60b2af7c714e4cb8b3a9aa65fce438af07e97bf95c6c59853e3a
- evidence_id: root56-sources-GO0160055-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160055/ancestors?relations=is_a
  locator: Complete native is_a ancestor response
  accessed_at: '2026-10-22T06:55:20.388370Z'
  support: supports
  summary: The complete is_a-only ancestry supports the declared parent class. It
    does not establish parthood or taxonomic frequency.
  snapshot_sha256: 06a3ebc40a4c4a740daeb1bcbae9c20261e55019c5890b332a1af235f089d852
- evidence_id: root56-sources-tax-5794
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:55:11.950375Z'
  support: supports
  summary: Native taxId 5794 identifies Apicomplexa; broad taxon, species and reference
    strain are kept distinct.
  snapshot_sha256: 617b42c27ae95a801b69abf63e1a545eff8565fd0af2f4a81be359d3fb6b3cbf
- evidence_id: root56-sources-tax-5811
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:55:12.029165Z'
  support: supports
  summary: Native taxId 5811 identifies Toxoplasma gondii; broad taxon, species and
    reference strain are kept distinct.
  snapshot_sha256: cbb209002c87051ce78d0a34bc169d2f6623f6bbfbb21edad170d43eb16d4032
- evidence_id: root56-sources-tax-508771
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/508771
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:55:11.346932Z'
  support: supports
  summary: Native taxId 508771 identifies Toxoplasma gondii ME49; broad taxon, species
    and reference strain are kept distinct.
  snapshot_sha256: d1622dee69e1fe2abfea4351893585852f4200cfff6eac3b42e5a014283cd0b0
- evidence_id: root56-sources-pmid-10749937
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10749937+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T06:55:15.344661Z'
  support: supports
  summary: 'MED 10749937: A dibasic motif in the tail of a class XIV apicomplexan
    myosin is an essential determinant of plasma membrane localization. Hettmann C,
    Herm A, Geiter A, Frank B, Schwarz E, Soldati T, Soldati D. (2000); DOI 10.1091/mbc.11.4.1385.
    Entire native abstract read; this evidence row does not claim the paper body.'
  snapshot_sha256: 1b7e0bc67a1a2dea304d30191da512043cc2ccbf702c7419153c87bfda11cecd
- evidence_id: root56-sources-doi-10.1016_j.mib.2009.06.008
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.mib.2009.06.008%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T06:55:16.418143Z'
  support: supports
  summary: 'Unique DOI result MED 19577950: Mechanisms controlling glideosome function
    in apicomplexans. Daher W, Soldati-Favre D. (2009). Complete abstract read; body
    evidence is separately located.'
  snapshot_sha256: 0d78f82f607fafc094adb311d088ce8cf2361f897831edc191e512a26e69657a
- evidence_id: root56-sources-doi-10.1046_j.1365-2958.2002.03056.x
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1046%2Fj.1365-2958.2002.03056.x%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T06:55:16.628439Z'
  support: supports
  summary: 'Unique DOI result MED 12139608: ''The glideosome'': a dynamic complex
    powering gliding motion and host cell invasion by Toxoplasma gondii. Opitz C,
    Soldati D. (2002). Complete abstract read; body evidence is separately located.'
  snapshot_sha256: b1d9459d7472844a4a043a2614d553914a147680c5d338805de1d9b6e4dee9ed
- evidence_id: root56-sources-doi-10.1083_jcb.200311137
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200311137%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T06:55:17.058396Z'
  support: supports
  summary: 'Unique DOI result MED 15123738: Identification of the membrane receptor
    of a class XIV myosin in Toxoplasma gondii. Gaskins E, Gilk S, DeVore N, Mann
    T, Ward G, Beckers C. (2004). Complete abstract read; body evidence is separately
    located.'
  snapshot_sha256: f3828316456ec0559005468530c935186b09de05687b9723f6389a94cd3748fc
- evidence_id: root56-sources-protein-O00934
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O00934.json
  locator: Identity/status/names, genes/aliases, organism and family cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:55:12.655205Z'
  support: supports
  summary: 'O00934: The reviewed Myosin-A entry has no native gene field; MyoA is
    a protein short name, not an exact-gene search hit.'
  snapshot_sha256: 95b32ca195be7bfcead066fae9485017d12f952c0b02c1416d61c510622d80a5
- evidence_id: root56-sources-gene-MyoA
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMyoA%29+AND+%28organism_id%3A5811%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set and literal native query parameters
  accessed_at: '2026-10-22T06:55:20.480223Z'
  support: supports
  summary: The exact-gene MyoA query returns no result, consistent with the reviewed
    entry lacking a gene field. Accession identity is verified directly; this is not
    evidence that MyoA is absent.
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
- evidence_id: root56-sources-protein-A0A125YYD4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A125YYD4.json
  locator: Identity/status/names, genes/aliases, organism and family cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:55:12.556137Z'
  support: supports
  summary: 'A0A125YYD4: The unreviewed MLC1 entry lists TGME49_257680 as an orfName,
    rather than a primary geneName. Its ME49 identity is separate from the primary
    RH assay background.'
  snapshot_sha256: ef575e15d4295fceea51f5e6846b495fe68fcbcd4e45efed2c6ba17e08fed277
- evidence_id: root56-sources-gene-TGME49_257680
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATGME49_257680%29+AND+%28organism_id%3A508771%29&format=json&size=500
  locator: Whole returned identity set and literal native query parameters
  accessed_at: '2026-10-22T06:55:20.966225Z'
  support: supports
  summary: The query restricted to the declared organism and gene/locus returns exactly
    A0A125YYD4; reviewed filtering is used only for reviewed examples.
  snapshot_sha256: af4ef8a24774f018ec2ac947a0075758f2029ebc7affb8e6b115797b5ce5cc07
- evidence_id: root56-sources-protein-Q7Z289
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q7Z289.json
  locator: Identity/status/names, genes/aliases, organism and family cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:55:14.828096Z'
  support: supports
  summary: 'Q7Z289: The unreviewed GAP45 entry corroborates the gene/taxon identity
    and IPR063210/PF29346 cross-references.'
  snapshot_sha256: 4ecc18c62e24146999ce3544759e6cdd12481856d6149d395c4ce5b88565e1b8
- evidence_id: root56-sources-gene-GAP45
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AGAP45%29+AND+%28organism_id%3A5811%29&format=json&size=500
  locator: Whole returned identity set and literal native query parameters
  accessed_at: '2026-10-22T06:55:21.072535Z'
  support: supports
  summary: The query restricted to the declared organism and gene/locus returns exactly
    Q7Z289; reviewed filtering is used only for reviewed examples.
  snapshot_sha256: 0260f9db8392f40121bdfa1fc98dc046394c3c402d068cb41d1d7f320b7d379a
- evidence_id: root56-sources-protein-Q6PQ42
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q6PQ42.json
  locator: Identity/status/names, genes/aliases, organism and family cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:55:14.744549Z'
  support: supports
  summary: 'Q6PQ42: The unreviewed entry carries the native acid-phosphatase label
    and GAP50 gene identity; its cited Gaskins paper establishes glideosome membership.
    Automated enzyme naming is not evidence of catalytic activity.'
  snapshot_sha256: 5bd76e84d8428d00aeab6b3c07ed5cba76b707793f77d7869bfad19b3978a014
- evidence_id: root56-sources-gene-GAP50
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AGAP50%29+AND+%28organism_id%3A5811%29&format=json&size=500
  locator: Whole returned identity set and literal native query parameters
  accessed_at: '2026-10-22T06:55:21.705399Z'
  support: supports
  summary: The query restricted to the declared organism and gene/locus returns exactly
    Q6PQ42; reviewed filtering is used only for reviewed examples.
  snapshot_sha256: dcfedb9f03aacfda58f9ab1e0685ca9def26cc187b138dfb4cac03ce675509df
- evidence_id: root56-sources-ipr-IPR063210
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063210/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:55:23.547153Z'
  support: supports
  summary: The native whole-family entry identifies GAP45 and integrates PF29346;
    its Plasmodium-specific recruitment prose is not substituted for the primary Toxoplasma
    experiments.
  snapshot_sha256: be5d58575a5ce672abe297768cf55748f53a1e16712a517b2b55eec308f90333
- evidence_id: root56-sources-pfam-PF29346
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF29346/
  locator: Native accession/name/type, complete description and integrated InterPro
    identity
  accessed_at: '2026-10-22T06:55:23.356867Z'
  support: supports
  summary: PF29346 names GAP45 and integrates into the exact IPR063210 family, although
    its native API type is domain. This type label alone does not contradict the exact
    GAP45 signature or prove that the record has the wrong constituent identity.
  snapshot_sha256: 02493d5945c01de08c2c5665710f25fb8cb29c3642086c2b92ae1d42b415e70a
- evidence_id: root56-sources-ipr-IPR036044
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR036044/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:55:55.031471Z'
  support: supports
  summary: A MyoA/MyoB-associated domain is broader than the complete glideosome MyoA
    class.
  snapshot_sha256: 4a330d6c5968fda6c129b5e68d6462efe150b5a8afad9b94181b661593d4f948
- evidence_id: root56-sources-ipr-IPR049007
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR049007/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:55:55.552948Z'
  support: supports
  summary: The MTIP-associated N-terminal EF-hand domain does not represent the entire
    source-neutral glideosome light-chain cohort.
  snapshot_sha256: b9b801cd6179d0f2c25f465d47ceff5adf8de46ab35c02a9c6d064fd4e7a015c
- evidence_id: root56-sources-ipr-IPR024927
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024927/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:55:55.625782Z'
  support: supports
  summary: The purple-acid-phosphatase family includes GAP50 but also other proteins;
    homologous class coverage is broader than the specific glideosome receptor task.
  snapshot_sha256: 2177b4170074caa8fe3d17dd49736fd669efe24d985792471fa8f204821c3fb9
- evidence_id: root56-sources-ipr-IPR051558
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051558/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:55:56.202130Z'
  support: supports
  summary: This broader purple-acid-phosphatase family has an unchecked generated
    description and is not an exact GAP50 mapping or independent proof of enzymatic
    activity.
  snapshot_sha256: 4b3b3221eb3906c1fd73f59b9154fead54ecd4ceb74eee41e733c735b2db01b8
- evidence_id: root56-sources-PMC2172186-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2172186/
  locator: Results sec4, sec5, sec6 and sec7 in full, including embedded Figures 3–7
    captions; Methods sec10, sec13, sec14, sec15 and sec17 in full
  accessed_at: '2026-10-22T06:55:56.523571Z'
  support: supports
  summary: Gaskins 2004 identifies MyoA/MLC1/GAP45/GAP50 coassociation and GAP50 localization
    to the IMC. Pulse/chase experiments distinguish a soluble three-protein precursor
    from later GAP50-associated membrane complex; a GAP50 C-terminal-tail deletion
    construct fails to associate with the motor components in the stated transient-expression
    assay.
  snapshot_sha256: c46163bf86b66ed9be9db7324fee08e5a568bb2d4831fa704c45652b3642d12f
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/glideosome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:41Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/glideosome.yaml'
  snapshot_sha256: 0e56194be4f051721c5e4065e4e14ef2fb1b8ad6c1a402160b375fb199abc672
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/glideosome.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glideosome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:42Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/glideosome.yaml\
    \ --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glideosome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glideosome-strict.tsv"
  snapshot_sha256: 151bd508b8c775218a5be70452625be7c56453d5cdfff7cfd32ed62ad427ebbc
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glideosome.yaml --causal-graphs
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:02:50.417693Z'
  support: supports
  summary: "data/structures/other/glideosome.yaml  (GO:0160055)\n  gap50_anchored_glideosome_motor\t\
    myoa_class_xiv_myosin_heavy_chain\tCOVERED\t->myoa_class_xiv_myosin_heavy_chain\
    \ (UniProtKB:O00934)\n  gap50_anchored_glideosome_motor\tglideosome_myosin_light_chains\t\
    COVERED\t->glideosome_myosin_light_chains (UniProtKB:A0A125YYD4)\n  gap50_anchored_glideosome_motor\t\
    gap45_glideosome_associated_protein\tCOVERED\t->gap45_glideosome_associated_protein\
    \ (UniProtKB:Q7Z289)\n  gap50_anchored_glideosome_motor\tgap50_membrane_receptor\t\
    COVERED\t->gap50_membrane_receptor (UniProtKB:Q6PQ42)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     4  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     4  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 24917dd901888a745e39827156e91c29747c1604f7f9fdee3ef6657bd76598cb
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glideosome.yaml --verify
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:02:51.723031Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/glideosome.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '14 of 16 collected target identifiers returned OK. PMID:10749937: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; Pfam:PF29346: SKIPPED;
    Exact native PF29346 GAP45 identifier and integrated IPR063210 family identity
    independently read. The native type label is domain; class scope and reference-protein
    membership are separately assessed in the scientific review. The skipped bulk
    prefix is not itself native authority verification. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
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
  topic: GO glideosome and historical four-class core
  outcome: supported
  target_ids:
  - GO:0160055
  summary: Exact GO identity and protein-complex parent agree. The primary Toxoplasma
    study supports the four named core classes and IMC localization. The existing
    light-chain cohort properly accommodates MLC1/MTIP-like homologs and should not
    be narrowed back to one species gene.
  evidence_ids:
  - record
  - root56-sources-go
  - root56-sources-GO0160055-ancestors
  - root56-sources-PMC2172186-html
- assessment_id: composition
  area: grounding
  topic: Exact GAP45 and appropriately unresolved broader candidates
  outcome: supported
  target_ids:
  - GO:0160055
  summary: The existing GAP45 mapping is supported by its integrated family and native
    reference accession. The other inspected candidate entries are shared domains
    or broader families, so no exact replacement is forced. Four examples retain their
    actual reviewed/unreviewed statuses; MyoA lacks a native gene field and MLC1 is
    indexed by an ORF name.
  evidence_ids:
  - record
  - curation
  - root56-sources-ipr-IPR063210
  - root56-sources-pfam-PF29346
  - root56-sources-ipr-IPR036044
  - root56-sources-ipr-IPR049007
  - root56-sources-ipr-IPR024927
  - root56-sources-ipr-IPR051558
  - root56-sources-protein-O00934
  - root56-sources-protein-A0A125YYD4
  - root56-sources-protein-Q7Z289
  - root56-sources-protein-Q6PQ42
  - root56-sources-gene-MyoA
  - root56-sources-gene-TGME49_257680
  - root56-sources-gene-GAP45
  - root56-sources-gene-GAP50
- assessment_id: formation
  area: grounding
  topic: Direct stage and tail-dependent association evidence
  outcome: concern
  target_ids:
  - GO:0160055
  summary: The generic GAP50 anchor role is correct but omits directly measured staged
    assembly and failure of the tail-deletion construct to associate. The pulse/chase
    result and transient-expression coimmunoprecipitation are distinct from the later
    failure to recover stable transfectants, which is not itself a direct formation
    assay.
  evidence_ids:
  - record
  - schema
  - root56-sources-PMC2172186-html
- assessment_id: graph
  area: graph
  topic: Supported scoped associations and motor outcomes
  outcome: supported
  target_ids:
  - GO:0160055
  summary: All four membership/anchor edges and the IMC-localization edge are supported
    by Gaskins. GO and complete native abstracts of the two cited reviews support
    the broad gliding/invasion outcomes. NONMECHANISTIC scope appropriately excludes
    a full actin/adhesin mechanism and later accessory proteins.
  evidence_ids:
  - record
  - graphs
  - root56-sources-go
  - root56-sources-PMC2172186-html
  - root56-sources-doi-10.1016_j.mib.2009.06.008
  - root56-sources-doi-10.1046_j.1365-2958.2002.03056.x
  - root56-sources-doi-10.1083_jcb.200311137
- assessment_id: scope
  area: scope
  topic: Apicomplexan scope and distinct assay/reference strains
  outcome: supported
  target_ids:
  - GO:0160055
  summary: The 2009 review abstract treats apicomplexan glideosomes and GO defines
    the broader class. The primary assay used RH(HXGPRT-negative) Toxoplasma, whereas
    the MLC1 reference accession is ME49. Quantitative labeled-protein ratios were
    only interpreted as consistent with a heterotetramer by the source, not definitive
    fixed stoichiometry.
  evidence_ids:
  - record
  - schema
  - root56-sources-go
  - root56-sources-PMC2172186-html
  - root56-sources-doi-10.1016_j.mib.2009.06.008
  - root56-sources-tax-5794
  - root56-sources-tax-5811
  - root56-sources-tax-508771
  - root56-sources-protein-O00934
  - root56-sources-protein-A0A125YYD4
  - root56-sources-protein-Q7Z289
  - root56-sources-protein-Q6PQ42
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target and bounded follow-up
  outcome: supported
  target_ids:
  - GO:0160055
  summary: Every maintained field, evidence row, component/example, graph edge, discussion
    and history entry was read. Optional unpopulated slots are not defects. Scientific
    status/history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root56-sources-go
  - root56-sources-doi-10.1016_j.mib.2009.06.008
  - root56-sources-doi-10.1046_j.1365-2958.2002.03056.x
  - root56-sources-doi-10.1083_jcb.200311137
- assessment_id: formation-necessity
  area: grounding
  topic: Universal individual-constituent formation requirements
  outcome: unknown
  target_ids:
  - GO:0160055
  summary: The bounded physical-association and activity observations assessed above
    do not establish a universal individual-constituent necessity profile for formation
    of this structure. Unspecified requirements remain unknown; they are not presumed
    essential or treated as a new corrective finding.
  evidence_ids:
  - record
  - schema
  - root56-sources-PMC2172186-html
findings:
- finding_id: F1
  issue_key: glideosome-gap50-tail-dependent-association
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve the tested GAP50 association dependency
  description: The cited primary body separates the soluble MyoA/MLC1/GAP45 precursor
    from later GAP50 association and reports loss of motor coassociation for the GAP50
    C-terminal-tail deletion construct. Current role and anchors/assembles-into edges
    omit this concrete conditional assembly evidence.
  target_ids:
  - GO:0160055
  field_paths:
  - components[3].role
  - causal_graphs[0]
  evidence_ids:
  - record
  - schema
  - graphs
  - root56-sources-PMC2172186-html
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glideosome.yaml
    role: maintained scientific record
  rule_id: Resolvable conditional motor-assembly evidence
  native_severity: minor
  normalization_reason: A bounded omission of direct physical-association evidence;
    the existing anchor function and scoped core identity remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0160055
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glideosome.yaml
    role: maintained scientific record
  description: Add the source-specific staged association and GAP50-tail perturbation
    results with their assay context, keeping association, localization and viability
    as distinct outcomes.
  acceptance_checks:
  - State the 15-minute pulse versus 4-hour chase context for the staged association
    experiment and the transient-expression coimmunoprecipitation context for the
    tail construct.
  - Name the reported construct without resolving the paper's discrepancy between
    its residue-range label and method residue count by guesswork.
  - Do not infer universal necessity for every component, fixed heterotetramer stoichiometry,
    or enzymatic GAP50 activity.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
limitations:
- All five same-base batch26 corpus gates and exact target resolver rows are integrated
  with every manifested input hash verified.
- No figure pixels, raw datasets, sequence alignments, atomic coordinates or supplementary
  files were reanalyzed. Primary body reading is limited to declared sections and
  embedded captions.
- Any absence finding is confined to the complete inspected target and its existing
  task; no claim is made that a related record or identifier is absent from the corpus
  or all databases.
- Opitz 2002, Daher 2009 and Hettmann 2000 were read at complete native abstract tier
  only. Gaskins body scopes are exact; Figure 2 caption, figure pixels and supplements
  were not read.
- The record reports a historical core and explicitly defers later GAP40/GAPM/accessory
  reconciliation. This review does not claim exhaustive present-day motor composition
  or species-wide quantitative prevalence.
- The source labels its tail-deletion construct by a residue range but describes a
  different residue count in Methods; no count is silently harmonized. Broad or generated
  phosphatase annotations are not accepted as direct GAP50 activity evidence.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations and issue-bearing reviews
  alike.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
