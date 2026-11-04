# Source-backed review of glycine cleavage complex

- Review: 20261022T072027Z-glycine-cleavage-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:59:46Z
- Finished UTC: 2026-10-22T07:20:27Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: four-component identity, exact P/H/T groundings, K12 examples and coarse reaction sequence are supported. The mixed L-family candidate, assembly necessity and detailed primary1993 assay attribution remain explicitly unresolved; no exact mapping is forced.

## Scope And Provenance

Exactly one complete target plus fourteen frozen target/guidance/schema inputs. Source-native identities and precise primary/abstract scopes were independently read; no neighboring record is an unstated premise.

Selection: Batch56 strict ordered selection index 6; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005960 | data/structures/other/glycine_cleavage_complex.yaml | maintained | glycine cleavage complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005960 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005960 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0005960 | Native check passed; source support was independently assessed. |
| Focused native verify | passed | True | GO:0005960 | Native check passed; source support was independently assessed. |
| Claim-level scientific review | passed | True | GO:0005960 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005960 | 14 of 16 collected target identifiers returned OK. PMID:3023185: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:8375392: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005960 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005960 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005960 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005960 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005960 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Supported four-class glycine-cleavage identity

identity: supported. Targets: GO:0005960.

The exact GO identity, synonym set and both parent classes match. The definition remains a coarse four-component reversible system and does not invent a fixed oligomer copy number.

### Correct four identities and P/H/T families

grounding: supported. Targets: GO:0005960.

The four identities and K12 examples are supported. P/H/T use exact native families. LpdA shared service in several complexes is a role distinction and would not by itself prevent enzyme-class grounding; however the checked IPR006258 candidate also includes distinct-activity relatives, so it is not promoted to an unconditionally exact replacement.

### L-family candidate remains unresolved

grounding: unknown. Targets: GO:0005960.

IPR006258 includes ferric-leghemoglobin reductase and NADH:ferredoxin oxidoreductase members whose dihydrolipoamide activity is only predicted. P0A9P0 membership does not remove that family-level breadth. Applying the same exact-class standard used for mixed GltD-like families, the review retains label-only status pending a narrowed candidate or explicit justified homolog-family boundary; no mandatory exact mapping is claimed.

### Correct reviewed accession and alias boundaries

grounding: supported. Targets: GO:0005960.

All four examples are reviewed K12 entries with matching exact gene queries. lpd and lpdA are names of the same entry, not two missing proteins. The primary1993 complete abstract supports purified P/H/T and operon sequencing, but its detailed strain/assay Methods were not accessible.

### Supported coarse reaction sequence at native authority tier

evidence: supported. Targets: GO:0005960.

GO/IPR and reviewed protein annotations support P decarboxylation, H carrier transfer, T folate chemistry and L reoxidation. The four graph edges preserve those actors and directions. Authority annotation support is not presented as independently read primary reaction assays.

### Detailed1993 functional-coupling attribution remains unverified

evidence: unknown. Targets: GO:0005960.

The complete Okamura abstract reports purification, N-terminal sequencing, operon sequence and overexpression. It does not expose the main-body assays behind the graph notes about functional coupling and individual reaction steps. Native UniProt does cite this paper for function, so abstract-only access does not establish that those notes are false; this remains an explicit limitation rather than an invented finding.

### UNKNOWN formation labels remain appropriate

evidence: unknown. Targets: GO:0005960.

Purification, overexpression, enzyme activity and the four-class description do not establish universal physical-assembly necessity for each component. The existing UNKNOWN labels preserve this distinction.

### Complete target with bounded source and optional-field limits

completeness: supported. Targets: GO:0005960.

All maintained scientific fields, discussion/history, graph actors/edges and citations were read. Findings concern concrete source placement or a verified current family task, not empty optional slots. Native protein/family databases address these claims; expression-module inference is not used for physical membership.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/glycine_cleavage_complex.yaml; Entire current YAML, including components, examples, all evidence, graph, discussions and history | context_only | All target bytes were read. No neighboring maintained record is an unstated premise. |
| curation | docs/CURATION.md; Exact source-neutral component classes and reviewed-label-only contract | context_only | A family identifies the molecular class; its role in a particular complex need not be exclusive to that complex. A species protein example does not replace family grounding. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, PresenceEnum and causal graph fields | context_only | UNKNOWN does not assert assembly necessity. COMMON means present in most members with exceptional losses; VARIABLE is a distribution pattern, not a synonym for unmeasured prevalence. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Actor identity and edge-level evidence | context_only | A coarse physical assembly and catalysis account may be mechanistic without every intermediate. Association, catalytic activity and formation necessity remain distinct. |
| micro56-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Native taxId, scientificName, rank, lineage and equivalent name. | supports | ENA taxId83333 is Escherichia coli K-12, rank strain; UniProt strain-format labels refer to the same taxon. |
| micro56-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031026,GO:0009342,GO:0004355,GO:0140535,GO:1990204,GO:0005960,GO:1990234,GO:0004375; Exact glycine target/parent/function definitions, synonyms and relevant typed children only in the combined response. | supports | GO0005960 exactly identifies the four-component glycine-cleavage system and retained exact synonyms; GO1990204/1990234 identify oxidoreductase/transferase complexes. GO0004375 describes the specific P-protein reaction and lists the complex capable_of it. |
| micro56-GO0005960-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005960/ancestors?relations=is_a; Complete exact-target relations=is_a ancestors array. | supports | The is_a-only array contains both maintained parent classes. |
| micro56-pmid-8375392 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8375392+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED record: exact PMID, title, authors, year, DOI and available abstractText. | supports | PMID8375392: Cloning and nucleotide sequence of the gcv operon encoding the Escherichia coli glycine-cleavage system. Okamura-Ikeda K, Ohmura Y, Fujiwara K, Motokawa Y. (1993), DOI10.1111/j.1432-1033.1993.tb18172.x. The complete native abstract was read; no unlisted main-body claim is inferred. |
| micro56-pmid-3023185 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A3023185+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED record: exact PMID, title, authors, year, DOI and available abstractText. | supports | PMID3023185: Cloning and characterization of the glycine-cleavage enzyme system of Escherichia coli. Stauffer LT, Plamann MD, Stauffer GV. (1986), DOI10.1016/0378-1119(86)90185-x. The complete native abstract was read; no unlisted main-body claim is inferred. |
| micro56-protein-P33195 | https://rest.uniprot.org/uniprotkb/P33195.json; Native identity/status/name, genes, organism/taxonId; complete FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs. Location annotations, if present, do not independently establish complex membership. | supports | Reviewed K12 P33195 is GcvP; native FUNCTION describes PLP-dependent decarboxylation and transfer to H, with both rule and PMID8375392 evidence. SUBUNIT identifies four classes; IPR020581 is present. |
| micro56-gene-gcvP | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgcvP%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results identity set; exact gene_exact, organism_id:83333 and reviewed:true query in the retained URL. | supports | The exact reviewed organism83333 gene query returns one entry, P33195; the returned primary gene or declared synonym matches gcvP. |
| micro56-protein-P0A6T9 | https://rest.uniprot.org/uniprotkb/P0A6T9.json; Native identity/status/name, genes, organism/taxonId; complete FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs. Location annotations, if present, do not independently establish complex membership. | supports | Reviewed K12 P0A6T9 is GcvH; native FUNCTION supports P-to-T methylamine shuttling, with a covalent lipoyl cofactor and IPR017453 membership. |
| micro56-gene-gcvH | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgcvH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results identity set; exact gene_exact, organism_id:83333 and reviewed:true query in the retained URL. | supports | The exact reviewed organism83333 gene query returns one entry, P0A6T9; the returned primary gene or declared synonym matches gcvH. |
| micro56-protein-P27248 | https://rest.uniprot.org/uniprotkb/P27248.json; Native identity/status/name, genes, organism/taxonId; complete FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs. Location annotations, if present, do not independently establish complex membership. | supports | Reviewed K12 P27248 is GcvT; native reaction gives transfer to tetrahydrofolate with ammonia release, and IPR006223 identifies its family. |
| micro56-gene-gcvT | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgcvT%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results identity set; exact gene_exact, organism_id:83333 and reviewed:true query in the retained URL. | supports | The exact reviewed organism83333 gene query returns one entry, P27248; the returned primary gene or declared synonym matches gcvT. |
| micro56-protein-P0A9P0 | https://rest.uniprot.org/uniprotkb/P0A9P0.json; Native identity/status/name, genes, organism/taxonId; complete FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs. Location annotations, if present, do not independently establish complex membership. | supports | Reviewed K12 P0A9P0 is lpdA with synonym lpd. FUNCTION explicitly places it in glycine cleavage and alpha-ketoacid complexes; CATALYTIC ACTIVITY supports NAD-dependent reoxidation of a reduced lipoyl protein, and IPR006258 is a native family cross-reference. |
| micro56-gene-lpdA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlpdA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results identity set; exact gene_exact, organism_id:83333 and reviewed:true query in the retained URL. | supports | The exact reviewed organism83333 gene query returns one entry, P0A9P0; the returned primary gene or declared synonym matches lpdA. |
| micro56-gene-lpd | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Alpd%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete identity set and actual query URL. | supports | The exact reviewed organism83333 lpd query returns the same single P0A9P0 entry whose primary name is lpdA and synonym is lpd. No separate second L-protein accession is required. |
| micro56-ipr-IPR020581 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020581/; Complete native accession/type/name/description, member signatures and GO annotations. | supports | IPR020581 is the exact GcvP family and carries GO0004375; it distinguishes fused/homodimeric and split/heterotetrameric P forms rather than a universal copy count. |
| micro56-ipr-IPR017453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017453/; Complete native accession/type/name/description, member signatures and GO annotations. | supports | IPR017453 is a curated GcvH subgroup, explicitly excluding divergent related proteins not established as authentic H proteins; its description supports lipoyl shuttling. |
| micro56-ipr-IPR006223 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006223/; Complete native accession/type/name/description, member signatures and GO annotations. | supports | IPR006223 is the GcvT aminomethyltransferase family, with folate-dependent C1 transfer and ammonia release; it is not the broader GcvT/YgfZ/DmdA cohort. |
| micro56-ipr-IPR006258 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006258/; Complete native family name/type/description/member signature/hierarchy and GO annotation fields. | supports | IPR006258 is the dihydrolipoamide-dehydrogenase family, with TIGR01350 and GO0004148. Its description explicitly includes shared E3 and glycine-cleavage L service. It also acknowledges a few proteins with distinct known activities, so the mapping identifies the named enzyme family and does not certify glycine-cleavage membership for every homolog. |
| micro56-okamura1993-wiley-pdf | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1432-1033.1993.tb18172.x; Original native403 response. | context_only | The direct Wiley PDF route returned HTTP403 HTML; this response is not a readable primary body. |
| micro56-okamura1993-browser-access | https://www.researchgate.net/publication/14824697_Cloning_and_nucleotide_sequence_of_the_gcv_operon_encoding_the_Escherichia_coli_glycine-cleavage_system; Browser representation status:null: exact title/DOI/abstract lines0–45 and access notice54–61 only; timestamp is retention after retrieval. | context_only | The exact ResearchGate paper page exposes the abstract and an explicit no-full-text notice. Its online-upload date is not substituted for the native1993 publication date. Citation excerpts below the article are not read as this paper body. |
| micro56-okamura1993-browser-diagnostics | https://febs.onlinelibrary.wiley.com/doi/epdf/10.1111/j.1432-1033.1993.tb18172.x; Combined browser diagnostic representation, status:null; no positive main-body evidence. | context_only | The alternate Wiley browser route was inaccessible. A guessed ResearchGate numerical ID redirected to an unrelated interferon article and is excluded entirely from scientific support. |
| micro56-stauffer1986-doi | https://doi.org/10.1016/0378-1119(86)90185-X; Original request/error bytes. | context_only | The native Stauffer DOI request failed TLS certificate verification with status0; the complete MED abstract is the positive scope. |
| schema-result | just validate data/structures/other/glycine_cleavage_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/glycine_cleavage_complex.yaml |
| strict-result | just validate-strict data/structures/other/glycine_cleavage_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_cleavage_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/glycine_cleavage_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_cleavage_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_cleavage_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/glycine_cleavage_complex.yaml --causal-graphs; Complete focused read-only native report | supports | data/structures/other/glycine_cleavage_complex.yaml  (GO:0005960)<br>  glycine_cleavage_cycle	gcvp_p_protein	COVERED	-&gt;gcvp_p_protein (UniProtKB:P33195)<br>  glycine_cleavage_cycle	gcvh_h_protein	COVERED	-&gt;gcvh_h_protein (UniProtKB:P0A6T9)<br>  glycine_cleavage_cycle	gcvt_t_protein	COVERED	-&gt;gcvt_t_protein (UniProtKB:P27248)<br>  glycine_cleavage_cycle	lpd_l_protein	COVERED	-&gt;lpd_l_protein (UniProtKB:P0A9P0)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/glycine_cleavage_complex.yaml --verify; Complete focused read-only native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/glycine_cleavage_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 16 collected target identifiers returned OK. PMID:3023185: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:8375392: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Okamura1993 and Stauffer1986 are complete native abstract only. Wiley PDF403, alternate publisher access failure, exact ResearchGate no-full-text notice and a rejected wrong-ID redirect are retained. No paper main-body, figure, supplement or specific reconstitution assay is certified.
- Native UniProt/InterPro reaction descriptions support the coarse graph independently, while detailed1993 functional-coupling/source claims remain unverified rather than automatically rejected.
- IPR006258 represents the enzyme family, not exclusive glycine-cleavage membership for every homolog; its native description acknowledges multifunctional/distinct-activity members. Role evidence remains separate.
- Original source URL, actual retained UTC and SHA256 joins are preserved; browser representations have status:null and are not called native HTTP200 bodies.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requests one review for every unreviewed record, including qualified clean cases.
- This is a scientific review with disclosed source access limits, not a claim that every cited paper was fully readable.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T072027Z-glycine-cleavage-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of glycine cleavage complex
started_at: '2026-10-22T06:59:46Z'
finished_at: '2026-10-22T07:20:27Z'
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
summary: 'Qualified pass: four-component identity, exact P/H/T groundings, K12 examples
  and coarse reaction sequence are supported. The mixed L-family candidate, assembly
  necessity and detailed primary1993 assay attribution remain explicitly unresolved;
  no exact mapping is forced.'
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
  - path: data/structures/other/glycine_cleavage_complex.yaml
    sha256: ed9aa4b2b2c567992efd6dee30006ab8457d55ebdc3d264ba3c9f88a3e615200
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
- target_id: GO:0005960
  path: data/structures/other/glycine_cleavage_complex.yaml
  label: glycine cleavage complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glycine_cleavage_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target plus fourteen frozen target/guidance/schema
    inputs. Source-native identities and precise primary/abstract scopes were independently
    read; no neighboring record is an unstated premise.
  selection: Batch56 strict ordered selection index 6; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005960
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005960
  command: just validate data/structures/other/glycine_cleavage_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005960
  command: just validate-strict data/structures/other/glycine_cleavage_complex.yaml
    --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_cleavage_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005960
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glycine_cleavage_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native check passed; source support was independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0005960
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glycine_cleavage_complex.yaml
    --verify
  exit_code: 0
  summary: Native check passed; source support was independently assessed.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005960
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0005960-ancestors
  - micro56-pmid-8375392
  - micro56-pmid-3023185
  - micro56-protein-P33195
  - micro56-gene-gcvP
  - micro56-protein-P0A6T9
  - micro56-gene-gcvH
  - micro56-protein-P27248
  - micro56-gene-gcvT
  - micro56-protein-P0A9P0
  - micro56-gene-lpdA
  - micro56-gene-lpd
  - micro56-ipr-IPR020581
  - micro56-ipr-IPR017453
  - micro56-ipr-IPR006223
  - micro56-ipr-IPR006258
  - micro56-okamura1993-wiley-pdf
  - micro56-okamura1993-browser-access
  - micro56-okamura1993-browser-diagnostics
  - micro56-stauffer1986-doi
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005960
  summary: '14 of 16 collected target identifiers returned OK. PMID:3023185: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:8375392: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - micro56-pmid-3023185
  - micro56-pmid-8375392
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005960
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
  - GO:0005960
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
  - GO:0005960
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
  - GO:0005960
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
  - GO:0005960
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
  reference: data/structures/other/glycine_cleavage_complex.yaml
  locator: Entire current YAML, including components, examples, all evidence, graph,
    discussions and history
  accessed_at: '2026-10-22T07:09:05Z'
  support: context_only
  summary: All target bytes were read. No neighboring maintained record is an unstated
    premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact source-neutral component classes and reviewed-label-only contract
  accessed_at: '2026-10-22T07:09:05Z'
  support: context_only
  summary: A family identifies the molecular class; its role in a particular complex
    need not be exclusive to that complex. A species protein example does not replace
    family grounding.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, PresenceEnum and causal graph fields
  accessed_at: '2026-10-22T07:09:05Z'
  support: context_only
  summary: UNKNOWN does not assert assembly necessity. COMMON means present in most
    members with exceptional losses; VARIABLE is a distribution pattern, not a synonym
    for unmeasured prevalence.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Actor identity and edge-level evidence
  accessed_at: '2026-10-22T07:09:05Z'
  support: context_only
  summary: A coarse physical assembly and catalysis account may be mechanistic without
    every intermediate. Association, catalytic activity and formation necessity remain
    distinct.
- evidence_id: micro56-tax83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Native taxId, scientificName, rank, lineage and equivalent name.
  accessed_at: '2026-10-22T06:56:30.426930Z'
  support: supports
  summary: ENA taxId83333 is Escherichia coli K-12, rank strain; UniProt strain-format
    labels refer to the same taxon.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro56-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031026,GO:0009342,GO:0004355,GO:0140535,GO:1990204,GO:0005960,GO:1990234,GO:0004375
  locator: Exact glycine target/parent/function definitions, synonyms and relevant
    typed children only in the combined response.
  accessed_at: '2026-10-22T06:56:29.752821Z'
  support: supports
  summary: GO0005960 exactly identifies the four-component glycine-cleavage system
    and retained exact synonyms; GO1990204/1990234 identify oxidoreductase/transferase
    complexes. GO0004375 describes the specific P-protein reaction and lists the complex
    capable_of it.
  snapshot_sha256: 82929c8bb8ff4aca3063e872086f8cb0653f40f64d99f9220af7f6f194f64762
- evidence_id: micro56-GO0005960-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005960/ancestors?relations=is_a
  locator: Complete exact-target relations=is_a ancestors array.
  accessed_at: '2026-10-22T06:56:29.753191Z'
  support: supports
  summary: The is_a-only array contains both maintained parent classes.
  snapshot_sha256: 65a86a3d733f3d71dbdd7817fa2a8be0cc6f8e396c6e6cbd6c3489c769991b0a
- evidence_id: micro56-pmid-8375392
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8375392+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED record: exact PMID, title, authors, year, DOI and available
    abstractText.'
  accessed_at: '2026-10-22T06:56:34.086666Z'
  support: supports
  summary: 'PMID8375392: Cloning and nucleotide sequence of the gcv operon encoding
    the Escherichia coli glycine-cleavage system. Okamura-Ikeda K, Ohmura Y, Fujiwara
    K, Motokawa Y. (1993), DOI10.1111/j.1432-1033.1993.tb18172.x. The complete native
    abstract was read; no unlisted main-body claim is inferred.'
  snapshot_sha256: 08a1b31a6ff9fd6b6a4b18bf9b660158f17b7b98e3e7f9f1228fde2559566f01
- evidence_id: micro56-pmid-3023185
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A3023185+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED record: exact PMID, title, authors, year, DOI and available
    abstractText.'
  accessed_at: '2026-10-22T06:56:34.144935Z'
  support: supports
  summary: 'PMID3023185: Cloning and characterization of the glycine-cleavage enzyme
    system of Escherichia coli. Stauffer LT, Plamann MD, Stauffer GV. (1986), DOI10.1016/0378-1119(86)90185-x.
    The complete native abstract was read; no unlisted main-body claim is inferred.'
  snapshot_sha256: 961462607d741b8e393fc2545668324a1500a57a6256a0756a6e7cd75b033cf5
- evidence_id: micro56-protein-P33195
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33195.json
  locator: Native identity/status/name, genes, organism/taxonId; complete FUNCTION,
    CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs.
    Location annotations, if present, do not independently establish complex membership.
  accessed_at: '2026-10-22T06:56:31.123775Z'
  support: supports
  summary: Reviewed K12 P33195 is GcvP; native FUNCTION describes PLP-dependent decarboxylation
    and transfer to H, with both rule and PMID8375392 evidence. SUBUNIT identifies
    four classes; IPR020581 is present.
  snapshot_sha256: befd9ab4b63f7c8d1af3d170c5bb82b1a16b9b78c4c8d78b674dcb6f65568a8b
- evidence_id: micro56-gene-gcvP
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgcvP%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results identity set; exact gene_exact, organism_id:83333 and
    reviewed:true query in the retained URL.
  accessed_at: '2026-10-22T06:56:32.477671Z'
  support: supports
  summary: The exact reviewed organism83333 gene query returns one entry, P33195;
    the returned primary gene or declared synonym matches gcvP.
  snapshot_sha256: 9873f3a50237c400aaa167c4222841cbb075dc9ceaa2a586779a9bfd56b735ad
- evidence_id: micro56-protein-P0A6T9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A6T9.json
  locator: Native identity/status/name, genes, organism/taxonId; complete FUNCTION,
    CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs.
    Location annotations, if present, do not independently establish complex membership.
  accessed_at: '2026-10-22T06:56:31.127414Z'
  support: supports
  summary: Reviewed K12 P0A6T9 is GcvH; native FUNCTION supports P-to-T methylamine
    shuttling, with a covalent lipoyl cofactor and IPR017453 membership.
  snapshot_sha256: adc53f2cfb6d80e2859c80cd19ad9e836afaadb2dd721eea6ca5f961ab09c27c
- evidence_id: micro56-gene-gcvH
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgcvH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results identity set; exact gene_exact, organism_id:83333 and
    reviewed:true query in the retained URL.
  accessed_at: '2026-10-22T06:56:32.800938Z'
  support: supports
  summary: The exact reviewed organism83333 gene query returns one entry, P0A6T9;
    the returned primary gene or declared synonym matches gcvH.
  snapshot_sha256: 5815bd22cadedaab50419f8c58aa6c2b761c0086cebf5c141ea66bfcf038f46a
- evidence_id: micro56-protein-P27248
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27248.json
  locator: Native identity/status/name, genes, organism/taxonId; complete FUNCTION,
    CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs.
    Location annotations, if present, do not independently establish complex membership.
  accessed_at: '2026-10-22T06:56:31.744311Z'
  support: supports
  summary: Reviewed K12 P27248 is GcvT; native reaction gives transfer to tetrahydrofolate
    with ammonia release, and IPR006223 identifies its family.
  snapshot_sha256: 730a60a57c4cd0b932ff03831c61f0b40222e06b33cfe9af27019095e473591e
- evidence_id: micro56-gene-gcvT
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgcvT%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results identity set; exact gene_exact, organism_id:83333 and
    reviewed:true query in the retained URL.
  accessed_at: '2026-10-22T06:56:32.937441Z'
  support: supports
  summary: The exact reviewed organism83333 gene query returns one entry, P27248;
    the returned primary gene or declared synonym matches gcvT.
  snapshot_sha256: f54121b7e7226c4237b99edf651bb71a77a3d063ded66c2f6865aa1366f42c7a
- evidence_id: micro56-protein-P0A9P0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A9P0.json
  locator: Native identity/status/name, genes, organism/taxonId; complete FUNCTION,
    CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs.
    Location annotations, if present, do not independently establish complex membership.
  accessed_at: '2026-10-22T06:56:31.786197Z'
  support: supports
  summary: Reviewed K12 P0A9P0 is lpdA with synonym lpd. FUNCTION explicitly places
    it in glycine cleavage and alpha-ketoacid complexes; CATALYTIC ACTIVITY supports
    NAD-dependent reoxidation of a reduced lipoyl protein, and IPR006258 is a native
    family cross-reference.
  snapshot_sha256: 547783133c18e16bf7627ac4b99d4e545e7d7622138d9413fa07dbf9cfb54dbe
- evidence_id: micro56-gene-lpdA
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlpdA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results identity set; exact gene_exact, organism_id:83333 and
    reviewed:true query in the retained URL.
  accessed_at: '2026-10-22T06:56:32.965954Z'
  support: supports
  summary: The exact reviewed organism83333 gene query returns one entry, P0A9P0;
    the returned primary gene or declared synonym matches lpdA.
  snapshot_sha256: f8a496db85602280b8a958d7fcf1fc91f5a9237f2f191ede24b9d7f89c265880
- evidence_id: micro56-gene-lpd
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Alpd%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete identity set and actual query URL.
  accessed_at: '2026-10-22T06:56:33.298963Z'
  support: supports
  summary: The exact reviewed organism83333 lpd query returns the same single P0A9P0
    entry whose primary name is lpdA and synonym is lpd. No separate second L-protein
    accession is required.
  snapshot_sha256: f8a496db85602280b8a958d7fcf1fc91f5a9237f2f191ede24b9d7f89c265880
- evidence_id: micro56-ipr-IPR020581
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020581/
  locator: Complete native accession/type/name/description, member signatures and
    GO annotations.
  accessed_at: '2026-10-22T06:56:34.702245Z'
  support: supports
  summary: IPR020581 is the exact GcvP family and carries GO0004375; it distinguishes
    fused/homodimeric and split/heterotetrameric P forms rather than a universal copy
    count.
  snapshot_sha256: 2cc3ed1760b3d327a01d88786a66a0bb8c3a4f271732f2fa3ed5b92014480262
- evidence_id: micro56-ipr-IPR017453
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017453/
  locator: Complete native accession/type/name/description, member signatures and
    GO annotations.
  accessed_at: '2026-10-22T06:56:34.758768Z'
  support: supports
  summary: IPR017453 is a curated GcvH subgroup, explicitly excluding divergent related
    proteins not established as authentic H proteins; its description supports lipoyl
    shuttling.
  snapshot_sha256: 661e887901d66e7213355c831e2d69d45e476fd292c1fcc622309014701f865b
- evidence_id: micro56-ipr-IPR006223
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006223/
  locator: Complete native accession/type/name/description, member signatures and
    GO annotations.
  accessed_at: '2026-10-22T06:56:34.777032Z'
  support: supports
  summary: IPR006223 is the GcvT aminomethyltransferase family, with folate-dependent
    C1 transfer and ammonia release; it is not the broader GcvT/YgfZ/DmdA cohort.
  snapshot_sha256: f1c54cc7046164bf76b60cd8911db5206cc010c02d435d7d6963ed3625dee4bd
- evidence_id: micro56-ipr-IPR006258
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006258/
  locator: Complete native family name/type/description/member signature/hierarchy
    and GO annotation fields.
  accessed_at: '2026-10-22T06:57:18.517884Z'
  support: supports
  summary: IPR006258 is the dihydrolipoamide-dehydrogenase family, with TIGR01350
    and GO0004148. Its description explicitly includes shared E3 and glycine-cleavage
    L service. It also acknowledges a few proteins with distinct known activities,
    so the mapping identifies the named enzyme family and does not certify glycine-cleavage
    membership for every homolog.
  snapshot_sha256: f2473042ddda69ae7ca28bfd72c8b520446de9ba1cf4b15ec17da40b71c5f30e
- evidence_id: micro56-okamura1993-wiley-pdf
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1432-1033.1993.tb18172.x
  locator: Original native403 response.
  accessed_at: '2026-10-22T06:57:19.253457Z'
  support: context_only
  summary: The direct Wiley PDF route returned HTTP403 HTML; this response is not
    a readable primary body.
  snapshot_sha256: 7b87ffd0e0a4d87b886d107aef543b00448150c159bfc5acc2a1b06710791e1e
- evidence_id: micro56-okamura1993-browser-access
  kind: database
  reference: https://www.researchgate.net/publication/14824697_Cloning_and_nucleotide_sequence_of_the_gcv_operon_encoding_the_Escherichia_coli_glycine-cleavage_system
  locator: 'Browser representation status:null: exact title/DOI/abstract lines0–45
    and access notice54–61 only; timestamp is retention after retrieval.'
  accessed_at: '2026-10-22T07:05:07.074433Z'
  support: context_only
  summary: The exact ResearchGate paper page exposes the abstract and an explicit
    no-full-text notice. Its online-upload date is not substituted for the native1993
    publication date. Citation excerpts below the article are not read as this paper
    body.
  snapshot_sha256: c64a23dd03e3b5d58c27bbbab0bf7113762a8d55219281f5c22d96aa8f6c2f65
- evidence_id: micro56-okamura1993-browser-diagnostics
  kind: authority
  reference: https://febs.onlinelibrary.wiley.com/doi/epdf/10.1111/j.1432-1033.1993.tb18172.x
  locator: Combined browser diagnostic representation, status:null; no positive main-body
    evidence.
  accessed_at: '2026-10-22T07:05:07.074781Z'
  support: context_only
  summary: The alternate Wiley browser route was inaccessible. A guessed ResearchGate
    numerical ID redirected to an unrelated interferon article and is excluded entirely
    from scientific support.
  snapshot_sha256: 23584a444ab39bc456daa8bc2ad15f5723766ca21fe4fc4ddd2ba6c9af44f95e
- evidence_id: micro56-stauffer1986-doi
  kind: authority
  reference: https://doi.org/10.1016/0378-1119(86)90185-X
  locator: Original request/error bytes.
  accessed_at: '2026-10-22T06:57:19.626421Z'
  support: context_only
  summary: The native Stauffer DOI request failed TLS certificate verification with
    status0; the complete MED abstract is the positive scope.
  snapshot_sha256: a8014ecefc9b9c4cc3987abe484f64b8ee37dd3e6bc0182a0f12915e702dedb3
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/glycine_cleavage_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:47Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/glycine_cleavage_complex.yaml'
  snapshot_sha256: 6f9b2792a0f538d0f0d9a797cc6f162da0803e8d1cab1b30375cf189f21a8c75
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/glycine_cleavage_complex.yaml
    --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_cleavage_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:48Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/glycine_cleavage_complex.yaml\
    \ --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_cleavage_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glycine_cleavage_complex-strict.tsv"
  snapshot_sha256: 6d1383407373b81780ad297a0e3f8647d1fa9f1a26bf7393cd006300da5dbeca
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glycine_cleavage_complex.yaml
    --causal-graphs
  locator: Complete focused read-only native report
  accessed_at: '2026-10-22T07:03:55.813386Z'
  support: supports
  summary: "data/structures/other/glycine_cleavage_complex.yaml  (GO:0005960)\n  glycine_cleavage_cycle\t\
    gcvp_p_protein\tCOVERED\t->gcvp_p_protein (UniProtKB:P33195)\n  glycine_cleavage_cycle\t\
    gcvh_h_protein\tCOVERED\t->gcvh_h_protein (UniProtKB:P0A6T9)\n  glycine_cleavage_cycle\t\
    gcvt_t_protein\tCOVERED\t->gcvt_t_protein (UniProtKB:P27248)\n  glycine_cleavage_cycle\t\
    lpd_l_protein\tCOVERED\t->lpd_l_protein (UniProtKB:P0A9P0)\n\ncausal_graphs GENE_OR_PROTEIN\
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
  snapshot_sha256: e9642745fe1b94010782cb896880aad8423c9d31f3c78f6236fb4f55999c2a3a
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glycine_cleavage_complex.yaml
    --verify
  locator: Complete focused read-only native report
  accessed_at: '2026-10-22T07:03:56.949829Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/glycine_cleavage_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '14 of 16 collected target identifiers returned OK. PMID:3023185: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:8375392: UNREACHABLE;
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
  topic: Supported four-class glycine-cleavage identity
  outcome: supported
  target_ids:
  - GO:0005960
  summary: The exact GO identity, synonym set and both parent classes match. The definition
    remains a coarse four-component reversible system and does not invent a fixed
    oligomer copy number.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0005960-ancestors
  - micro56-ipr-IPR020581
  - micro56-ipr-IPR017453
  - micro56-ipr-IPR006223
  - micro56-pmid-8375392
  - micro56-pmid-3023185
- assessment_id: composition
  area: grounding
  topic: Correct four identities and P/H/T families
  outcome: supported
  target_ids:
  - GO:0005960
  summary: The four identities and K12 examples are supported. P/H/T use exact native
    families. LpdA shared service in several complexes is a role distinction and would
    not by itself prevent enzyme-class grounding; however the checked IPR006258 candidate
    also includes distinct-activity relatives, so it is not promoted to an unconditionally
    exact replacement.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0005960-ancestors
  - micro56-protein-P33195
  - micro56-gene-gcvP
  - micro56-protein-P0A6T9
  - micro56-gene-gcvH
  - micro56-protein-P27248
  - micro56-gene-gcvT
  - micro56-protein-P0A9P0
  - micro56-gene-lpdA
  - micro56-ipr-IPR020581
  - micro56-ipr-IPR017453
  - micro56-ipr-IPR006223
  - micro56-ipr-IPR006258
  - micro56-gene-lpd
  - micro56-pmid-8375392
  - micro56-pmid-3023185
- assessment_id: family-boundary
  area: grounding
  topic: L-family candidate remains unresolved
  outcome: unknown
  target_ids:
  - GO:0005960
  summary: IPR006258 includes ferric-leghemoglobin reductase and NADH:ferredoxin oxidoreductase
    members whose dihydrolipoamide activity is only predicted. P0A9P0 membership does
    not remove that family-level breadth. Applying the same exact-class standard used
    for mixed GltD-like families, the review retains label-only status pending a narrowed
    candidate or explicit justified homolog-family boundary; no mandatory exact mapping
    is claimed.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0005960-ancestors
  - micro56-ipr-IPR006258
  - micro56-protein-P33195
  - micro56-gene-gcvP
  - micro56-protein-P0A6T9
  - micro56-gene-gcvH
  - micro56-protein-P27248
  - micro56-gene-gcvT
  - micro56-protein-P0A9P0
  - micro56-gene-lpdA
- assessment_id: examples
  area: grounding
  topic: Correct reviewed accession and alias boundaries
  outcome: supported
  target_ids:
  - GO:0005960
  summary: All four examples are reviewed K12 entries with matching exact gene queries.
    lpd and lpdA are names of the same entry, not two missing proteins. The primary1993
    complete abstract supports purified P/H/T and operon sequencing, but its detailed
    strain/assay Methods were not accessible.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0005960-ancestors
  - micro56-protein-P33195
  - micro56-gene-gcvP
  - micro56-protein-P0A6T9
  - micro56-gene-gcvH
  - micro56-protein-P27248
  - micro56-gene-gcvT
  - micro56-protein-P0A9P0
  - micro56-gene-lpdA
  - micro56-ipr-IPR020581
  - micro56-ipr-IPR017453
  - micro56-ipr-IPR006223
  - micro56-ipr-IPR006258
  - micro56-gene-lpd
  - micro56-pmid-8375392
  - micro56-pmid-3023185
- assessment_id: function
  area: evidence
  topic: Supported coarse reaction sequence at native authority tier
  outcome: supported
  target_ids:
  - GO:0005960
  summary: GO/IPR and reviewed protein annotations support P decarboxylation, H carrier
    transfer, T folate chemistry and L reoxidation. The four graph edges preserve
    those actors and directions. Authority annotation support is not presented as
    independently read primary reaction assays.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0005960-ancestors
  - micro56-protein-P33195
  - micro56-gene-gcvP
  - micro56-protein-P0A6T9
  - micro56-gene-gcvH
  - micro56-protein-P27248
  - micro56-gene-gcvT
  - micro56-protein-P0A9P0
  - micro56-gene-lpdA
  - micro56-ipr-IPR020581
  - micro56-ipr-IPR017453
  - micro56-ipr-IPR006223
  - micro56-ipr-IPR006258
  - micro56-gene-lpd
  - micro56-pmid-8375392
  - micro56-pmid-3023185
- assessment_id: primary-scope
  area: evidence
  topic: Detailed1993 functional-coupling attribution remains unverified
  outcome: unknown
  target_ids:
  - GO:0005960
  summary: The complete Okamura abstract reports purification, N-terminal sequencing,
    operon sequence and overexpression. It does not expose the main-body assays behind
    the graph notes about functional coupling and individual reaction steps. Native
    UniProt does cite this paper for function, so abstract-only access does not establish
    that those notes are false; this remains an explicit limitation rather than an
    invented finding.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0005960-ancestors
  - micro56-pmid-8375392
  - micro56-pmid-3023185
  - micro56-protein-P33195
  - micro56-gene-gcvP
  - micro56-protein-P0A6T9
  - micro56-gene-gcvH
  - micro56-protein-P27248
  - micro56-gene-gcvT
  - micro56-protein-P0A9P0
  - micro56-gene-lpdA
- assessment_id: formation
  area: evidence
  topic: UNKNOWN formation labels remain appropriate
  outcome: unknown
  target_ids:
  - GO:0005960
  summary: Purification, overexpression, enzyme activity and the four-class description
    do not establish universal physical-assembly necessity for each component. The
    existing UNKNOWN labels preserve this distinction.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0005960-ancestors
  - micro56-protein-P33195
  - micro56-gene-gcvP
  - micro56-protein-P0A6T9
  - micro56-gene-gcvH
  - micro56-protein-P27248
  - micro56-gene-gcvT
  - micro56-protein-P0A9P0
  - micro56-gene-lpdA
  - micro56-ipr-IPR020581
  - micro56-ipr-IPR017453
  - micro56-ipr-IPR006223
  - micro56-ipr-IPR006258
  - micro56-gene-lpd
  - micro56-pmid-8375392
  - micro56-pmid-3023185
- assessment_id: coverage
  area: completeness
  topic: Complete target with bounded source and optional-field limits
  outcome: supported
  target_ids:
  - GO:0005960
  summary: All maintained scientific fields, discussion/history, graph actors/edges
    and citations were read. Findings concern concrete source placement or a verified
    current family task, not empty optional slots. Native protein/family databases
    address these claims; expression-module inference is not used for physical membership.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0005960-ancestors
  - micro56-protein-P33195
  - micro56-gene-gcvP
  - micro56-protein-P0A6T9
  - micro56-gene-gcvH
  - micro56-protein-P27248
  - micro56-gene-gcvT
  - micro56-protein-P0A9P0
  - micro56-gene-lpdA
  - micro56-ipr-IPR020581
  - micro56-ipr-IPR017453
  - micro56-ipr-IPR006223
  - micro56-ipr-IPR006258
  - micro56-gene-lpd
  - micro56-pmid-8375392
  - micro56-pmid-3023185
findings: []
actions: []
limitations:
- Okamura1993 and Stauffer1986 are complete native abstract only. Wiley PDF403, alternate
  publisher access failure, exact ResearchGate no-full-text notice and a rejected
  wrong-ID redirect are retained. No paper main-body, figure, supplement or specific
  reconstitution assay is certified.
- Native UniProt/InterPro reaction descriptions support the coarse graph independently,
  while detailed1993 functional-coupling/source claims remain unverified rather than
  automatically rejected.
- IPR006258 represents the enzyme family, not exclusive glycine-cleavage membership
  for every homolog; its native description acknowledges multifunctional/distinct-activity
  members. Role evidence remains separate.
- Original source URL, actual retained UTC and SHA256 joins are preserved; browser
  representations have status:null and are not called native HTTP200 bodies.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requests one review for every unreviewed record, including qualified
  clean cases.
- This is a scientific review with disclosed source access limits, not a claim that
  every cited paper was fully readable.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
