# Scientific review of dna polymerase iii clamp loader complex

- Review: 20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:37:05Z
- Finished UTC: 2026-10-22T05:59:20Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The DnaX heptamer identity, five correct K12 proteins and coarse clamp-loading graph are supported. Two minor findings clarify tau/gamma alternatives and resolve three exact whole-protein families.

## Scope And Provenance

Exactly one complete maintained record, bounded native source fields and literature passages identified in each locator. No scientific input was changed.

Selection: Batch51 strict unreviewed path order, index 1; exactly one entire maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0043846 | data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml | maintained | DNA polymerase III, clamp loader complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0043846 | Focused validator passed. |
| Focused native strict | passed | True | GO:0043846 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0043846 | Focused read-only check passed; scientific claims separately assessed. |
| Native focused verify | passed | True | GO:0043846 | Focused read-only check passed; scientific claims separately assessed. |
| Expression-module applicability | not_applicable | False | GO:0043846 | No target expression-module or transcriptomic claim requires this resource. |
| Claim-level scientific review | passed | True | GO:0043846 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0043846 | 16 of 18 collected target identifiers returned OK. PMID:11525729: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:12940977: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0043846 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0043846 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0043846 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0043846 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0043846 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### DnaX heptamer versus crystallized pentamer

identity: concern. Targets: GO:0043846.

The named heptamer and holoenzyme parthood are sound. Jeruzalmi crystallized a minimal gamma3-delta-delta-prime pentamer, while McHenry describes the heptamer including chi/psi. The definition should express three DnaX copies with tau/gamma alternatives instead of implying both are invariant.

### Five correct protein classes; exact family resolution

grounding: concern. Targets: GO:0043846.

The five K12 examples and their GO annotations match current native records. HolA, HolC and HolD have exact available families; HolB and DnaX candidates inspected here are domains and are not safe whole-protein replacements. Family membership comes from the separately cited UniProt xrefs, not from the family metadata response.

### Species example and reference strain

scope: supported. Targets: GO:0043846.

The canonical note correctly says E.coli is the source species of the solved gamma structure; it does not claim a full heptamer was crystallized. Reference K12 example identities are verified independently. The actual sample uses truncated gamma1–373 and purified reconstitution; no unmodified K12 preparation is inferred.

### Nine descriptive edges and model limits

graph: supported. Targets: GO:0043846.

All five constituent nodes are supported at the appropriate complex scope. Delta binds beta, and the clamp loader loads beta onto primer-template DNA and supports replication. Jeruzalmi labels its transition mechanism speculative; the target remains NONMECHANISTIC and does not assert direct visualization of ATP-driven motion. Chi/psi membership comes from GO and the McHenry body, not the pentamer crystal.

### Defining composition is not a loss-of-assembly experiment

grounding: unknown. Targets: GO:0043846.

The full heptamer has five protein classes and three DnaX copies. Active minimal-pentamer reconstitution does not prove that chi/psi are dispensable for formation of the scoped heptamer, nor does clamp-loading activity prove every member is physically necessary. UNKNOWN formation essentiality remains appropriate; tau and gamma alternatives need explicit wording.

### Complete maintained target

completeness: supported. Targets: GO:0043846.

All fields, history, discussions and edge evidence were reviewed. Optional images, dimensions or prevalence inventories are not filled without evidence. Cited authority identities and source-scoped claims were checked separately.

## Findings

### F1: State the three DnaX copies and their alternatives

minor / open / confirmed; issue key: pol-iii-clamp-loader-dnax-mixture.

The definition unconditionally says the heptamer includes tau and gamma. Its cited McHenry2003 body p1158 instead specifies DnaX3-delta-delta-prime-chi-psi with any mixture of tau and gamma for clamp loading, and native DnaX annotations agree. The original GO sentence matches the record but compresses the source distinction.

### F2: Resolve the available HolA, HolC and HolD families

minor / open / confirmed; issue key: pol-iii-clamp-loader-exact-family.

These three components remain REVIEWED_LABEL_ONLY despite verified whole-protein families IPR005790, IPR007459 and IPR004615 and matching current UniProt-example xrefs. The reviewed HolB/DnaX candidates are domains and do not justify forcing a mapping.

## Recommended Actions And Acceptance Checks

### A1

Qualify the E.coli heptamer model as three DnaX products, tau and/or gamma, plus delta, delta-prime, chi and psi. Keep additional tau-dependent fork organization separate from minimum clamp loading.

- Do not universalize one tau:gamma ratio or require both products in every assembly.
- Do not replace the full heptamer identity with the crystallized pentamer.
- Preserve source scope and correct current protein examples; pass applicable native validators.

### A2

Map the three verified exact families and narrow the current unresolved TODO to genuinely unresolved classes. Preserve the five correct protein examples.

- Keep IPR004622/IPR012763 domain matches separate from whole-protein identity.
- Do not import a family description claiming delta proofreading activity.
- Preserve source scope and correct current protein examples; pass applicable native validators.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml; Entire maintained record, all evidence and graph edges, discussions and history | context_only | All target bytes were read. The current source-backed composition is distinguished from historical review notes and untested formation requirements. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, EssentialityEnum, NONMECHANISTIC graph contract | context_only | Taxon-specific accessions identify examples; they do not replace family grounding or experimental membership. Formation necessity differs from catalytic function and viability. |
| curation | docs/CURATION.md; Exact grounding, REVIEWED_LABEL_ONLY at159–160 and assembly essentiality | context_only | Label-only review status denotes a genuinely unresolved exact mapping. A domain or broader family must not replace an exact named protein class. |
| graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Membership versus assembly and coarse functional-edge scope | context_only | NONMECHANISTIC membership and catalogued activity are assessed without claiming that a static structure establishes a complete dynamic mechanism. |
| root51-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846,GO:0009360,GO:0044776,GO:0044775,GO:0043847,GO:0032991,GO:0042575,GO:0003887,GO:0006260,GO:0003689; All ten term identities/definitions/synonyms/comments; relevant typed child links. Unrelated GO0032991 descendants not audited. | supports | Exact active PolIII holoenzyme/core/clamp-loader identities, native synonyms and typed holoenzyme parthood links are present. The clamp-loader and core definitions match the named structures. The beta-clamp cross-class sentence is not used as a stoichiometric claim here. |
| root51-sources-pmid-11525729 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11525729+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact identifier/title/author/year/DOI and complete abstract | supports | Native MED11525729: Crystal structure of the processivity clamp loader gamma (gamma) complex of E. coli DNA polymerase III. by Jeruzalmi D, O'Donnell M, Kuriyan J. (2001), DOI 10.1016/s0092-8674(01)00463-9. Complete native abstract read; source-specific body access is stated separately. |
| root51-sources-pmid-12940977 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12940977+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact identifier/title/author/year/DOI and complete abstract | supports | Native MED12940977: Chromosomal replicases as asymmetric dimers: studies of subunit arrangement and functional consequences. by McHenry CS. (2003), DOI 10.1046/j.1365-2958.2003.03645.x. Complete native abstract read; source-specific body access is stated separately. |
| root51-sources-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxonomy response | supports | ENA identifies taxon562 as Escherichia coli. Species and reference-strain levels are kept separate. |
| root51-sources-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxonomy response | supports | ENA identifies taxon83333 as Escherichia coli K-12. Species and reference-strain levels are kept separate. |
| root51-sources-protein-P06710 | https://rest.uniprot.org/uniprotkb/P06710.json; Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY and DnaX ALTERNATIVE PRODUCTS; relevant InterPro/GO xrefs | supports | P06710 is the reviewed K12 dnaX entry with the declared protein identity. Native gene/locus tokens, function/subunit annotations, relevant GO annotation and family cross-references were inspected. Annotation-referenced experiments are not independently certified unless a separate primary-source row says so. |
| root51-sources-gene-dnaX | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaX%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set for gene_exact:dnaX AND taxonomy_id:83333 AND reviewed:true; size500 | supports | The complete reviewed exact-gene query returns one result, P06710, with the expected primary gene and taxon83333. |
| root51-sources-protein-P28630 | https://rest.uniprot.org/uniprotkb/P28630.json; Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY; relevant InterPro/GO xrefs | supports | P28630 is the reviewed K12 holA entry with the declared protein identity. Native gene/locus tokens, function/subunit annotations, relevant GO annotation and family cross-references were inspected. Annotation-referenced experiments are not independently certified unless a separate primary-source row says so. |
| root51-sources-gene-holA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set for gene_exact:holA AND taxonomy_id:83333 AND reviewed:true; size500 | supports | The complete reviewed exact-gene query returns one result, P28630, with the expected primary gene and taxon83333. |
| root51-sources-protein-P28631 | https://rest.uniprot.org/uniprotkb/P28631.json; Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY; relevant InterPro/GO xrefs | supports | P28631 is the reviewed K12 holB entry with the declared protein identity. Native gene/locus tokens, function/subunit annotations, relevant GO annotation and family cross-references were inspected. Annotation-referenced experiments are not independently certified unless a separate primary-source row says so. |
| root51-sources-gene-holB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set for gene_exact:holB AND taxonomy_id:83333 AND reviewed:true; size500 | supports | The complete reviewed exact-gene query returns one result, P28631, with the expected primary gene and taxon83333. |
| root51-sources-protein-P28905 | https://rest.uniprot.org/uniprotkb/P28905.json; Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY; relevant InterPro/GO xrefs | supports | P28905 is the reviewed K12 holC entry with the declared protein identity. Native gene/locus tokens, function/subunit annotations, relevant GO annotation and family cross-references were inspected. Annotation-referenced experiments are not independently certified unless a separate primary-source row says so. |
| root51-sources-gene-holC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set for gene_exact:holC AND taxonomy_id:83333 AND reviewed:true; size500 | supports | The complete reviewed exact-gene query returns one result, P28905, with the expected primary gene and taxon83333. |
| root51-sources-protein-P28632 | https://rest.uniprot.org/uniprotkb/P28632.json; Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY; relevant InterPro/GO xrefs | supports | P28632 is the reviewed K12 holD entry with the declared protein identity. Native gene/locus tokens, function/subunit annotations, relevant GO annotation and family cross-references were inspected. Annotation-referenced experiments are not independently certified unless a separate primary-source row says so. |
| root51-sources-gene-holD | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholD%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set for gene_exact:holD AND taxonomy_id:83333 AND reviewed:true; size500 | supports | The complete reviewed exact-gene query returns one result, P28632, with the expected primary gene and taxon83333. |
| root51-sources-jeruzalmi2001-pdf | https://odonnell.rockefeller.edu/assets/pdfs/119.pdf; Author-hosted primary Cell106:429–441 PDF: entire Introduction, Fig1 caption, Results opening/Structure Determination/General Description through p431 before ATP-binding-domain discussion; complete Experimental Procedures pp439–440. No figure pixels, coordinates or unreported activity data inspected. | supports | The nucleotide-free gamma3-delta-delta-prime structure contains three truncated gamma products and one each of delta and delta-prime. The preparation is active in clamp loading; the paper explicitly separates its observed structure from later speculative transition models. Chi/psi and tau are not crystallized constituents of this minimal pentamer. |
| root51-sources-mchenry2003-pdf | https://www.sbs.utexas.edu/psaxena/bio226r/articles/dna_replication_mchenry_2003.pdf; Complete pp1157–1158, including Fig1 caption and opening Special contributions of tau; later primary studies are cited context, not independently reread | supports | This secondary review distinguishes a three-part replicase organization and the E.coli DnaX3-delta-delta-prime-chi-psi heptamer. Its p1158 text explicitly permits any mixture of tau and gamma for clamp loading, while tau has additional polymerase/helicase contacts. The mixed tau/gamma model described in its abstract is not a universal requirement for every isolated clamp-loader preparation. |
| root51-sources-GO0043846-is-a | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846/ancestors?relations=is_a; Complete is-a-only ancestor response | supports | The native is-a ancestry includes protein-containing complex but currently routes through nuclear protein-containing complex. This upstream topology is recorded as a conflict with the bacterial primary evidence, not propagated as a required biological classification. |
| root51-sources-GO0043846-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846/constraints; Complete focal taxonConstraints array; unrelated inherited protein blacklists not used | context_only | Native GO currently reports only_in_taxon Eukaryota for this bacterial complex. The record has no such assertion; primary E.coli evidence and the source definition conflict with that upstream restriction. |
| root51-sources-GO0043846-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846/history; Complete history array | context_only | Complete native history records the2020 nuclear-parent change and a2024 bad-taxon-ID constraint entry. This provides provenance of an upstream discrepancy, not bacterial taxonomic evidence. |
| root51-sources-ipr-IPR005790 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005790/; Native name/type, complete description and flags, hierarchy and member signatures | supports | Exact HolA delta full-protein family; PTHR34388/TIGR01128 signatures. The LLM-authored proofreading sentence is not used as delta-specific activity evidence. |
| root51-sources-ipr-IPR007459 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007459/; Native name/type, complete description and flags, hierarchy and member signatures | supports | Exact HolC chi full-protein family with PF04364/PTHR38767; historical biochemical context is distinguished from sequence membership. |
| root51-sources-ipr-IPR004615 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004615/; Native name/type, complete description and flags, hierarchy and member signatures | supports | Exact HolD psi full-protein family with PF03603/PIRSF029225; subgroup IPR018382 is narrower and dated unknown-function text does not override direct biochemistry. |
| root51-sources-ipr-IPR004622 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004622/; Native name/type, complete description and flags, hierarchy and member signatures | supports | This is a delta-prime N-terminal domain, not an exact whole-protein family; its model can also score gamma/tau proteins. |
| root51-sources-ipr-IPR012763 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012763/; Native name/type, complete description and flags, hierarchy and member signatures | supports | This is the gamma/tau N-terminal domain and includes plant STICHEL relatives; it cannot be substituted as an exact whole-protein DnaX family. |
| schema-result | just validate data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml |
| strict-result | just validate-strict data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_clamp_loader_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_clamp_loader_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_clamp_loader_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml; Complete focused native report | supports | data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml  (GO:0043846)<br>  clamp_loader_beta_clamp_loading	dnax_tau_gamma_subunit	COVERED	-&gt;dnax_tau_gamma_subunit (UniProtKB:P06710)<br>  clamp_loader_beta_clamp_loading	delta_subunit	COVERED	-&gt;delta_subunit (UniProtKB:P28630)<br>  clamp_loader_beta_clamp_loading	delta_prime_subunit	COVERED	-&gt;delta_prime_subunit (UniProtKB:P28631)<br>  clamp_loader_beta_clamp_loading	chi_subunit	COVERED	-&gt;chi_subunit (UniProtKB:P28905)<br>  clamp_loader_beta_clamp_loading	psi_subunit	COVERED	-&gt;psi_subunit (UniProtKB:P28632)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     5  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     5  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| initial-verify-dns | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml; Preserved initial sandbox DNS failure log | context_only | The first native verification could not resolve UniProt DNS; a subsequent authorized network run passed with unchanged inputs. |
| target-curies | just check-curies-strict; data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 16 of 18 collected target identifiers returned OK. PMID:11525729: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force.; PMID:12940977: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, coordinates, sequence alignments or raw kinetic data were reanalyzed. Native annotations and a secondary review remain distinct from independently inspected primary methods.
- Native GO currently assigns this term nuclear-complex ancestry and an Eukaryota-only restriction, conflicting with the cited E.coli evidence. Neither assertion is present in the target. Keep its exact named identity and supported bacterial example; do not import the erroneous source restriction or infer occurrence in every bacterium.
- Initial focused UniProt verification failed solely on sandbox DNS. Its original traceback is retained; the subsequent network-enabled native check passed for unchanged input bytes.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes qualified clean reviews as well as issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Scientific review of dna polymerase iii clamp loader complex
started_at: '2026-10-22T05:37:05Z'
finished_at: '2026-10-22T05:59:20Z'
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
summary: The DnaX heptamer identity, five correct K12 proteins and coarse clamp-loading
  graph are supported. Two minor findings clarify tau/gamma alternatives and resolve
  three exact whole-protein families.
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
  - path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    sha256: d577d4fffb8f72d79620d78bfc245c04ed3481af7ab41b626ea4b7f21f0b166a
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
- target_id: GO:0043846
  path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  label: DNA polymerase III, clamp loader complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained record, bounded native source fields
    and literature passages identified in each locator. No scientific input was changed.
  selection: Batch51 strict unreviewed path order, index 1; exactly one entire maintained
    record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0043846
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: just validate data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: just validate-strict data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_clamp_loader_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  exit_code: 0
  summary: Focused read-only check passed; scientific claims separately assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  exit_code: 0
  summary: Focused read-only check passed; scientific claims separately assessed.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0043846
  summary: No target expression-module or transcriptomic claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0043846
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graph-rubric
  - root51-sources-go
  - root51-sources-pmid-11525729
  - root51-sources-pmid-12940977
  - root51-sources-tax562
  - root51-sources-tax83333
  - root51-sources-protein-P06710
  - root51-sources-gene-dnaX
  - root51-sources-protein-P28630
  - root51-sources-gene-holA
  - root51-sources-protein-P28631
  - root51-sources-gene-holB
  - root51-sources-protein-P28905
  - root51-sources-gene-holC
  - root51-sources-protein-P28632
  - root51-sources-gene-holD
  - root51-sources-jeruzalmi2001-pdf
  - root51-sources-mchenry2003-pdf
  - root51-sources-GO0043846-is-a
  - root51-sources-GO0043846-constraints
  - root51-sources-GO0043846-history
  - root51-sources-ipr-IPR005790
  - root51-sources-ipr-IPR007459
  - root51-sources-ipr-IPR004615
  - root51-sources-ipr-IPR004622
  - root51-sources-ipr-IPR012763
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0043846
  summary: '16 of 18 collected target identifiers returned OK. PMID:11525729: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force.; PMID:12940977: UNREACHABLE; Exact native EuropePMC MED identifier, title
    and DOI independently inspected after the bulk eutils414 transport failure. Identifier
    resolution does not certify all biological claims; declared primary-body and abstract
    reading limits remain in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root51-sources-pmid-11525729
  - root51-sources-pmid-12940977
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0043846
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
    and current batch51 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  locator: Entire maintained record, all evidence and graph edges, discussions and
    history
  accessed_at: '2026-10-22T05:42:48Z'
  support: context_only
  summary: All target bytes were read. The current source-backed composition is distinguished
    from historical review notes and untested formation requirements.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, EssentialityEnum, NONMECHANISTIC graph
    contract
  accessed_at: '2026-10-22T05:42:48Z'
  support: context_only
  summary: Taxon-specific accessions identify examples; they do not replace family
    grounding or experimental membership. Formation necessity differs from catalytic
    function and viability.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact grounding, REVIEWED_LABEL_ONLY at159–160 and assembly essentiality
  accessed_at: '2026-10-22T05:42:48Z'
  support: context_only
  summary: Label-only review status denotes a genuinely unresolved exact mapping.
    A domain or broader family must not replace an exact named protein class.
- evidence_id: graph-rubric
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Membership versus assembly and coarse functional-edge scope
  accessed_at: '2026-10-22T05:42:48Z'
  support: context_only
  summary: NONMECHANISTIC membership and catalogued activity are assessed without
    claiming that a static structure establishes a complete dynamic mechanism.
- evidence_id: root51-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846,GO:0009360,GO:0044776,GO:0044775,GO:0043847,GO:0032991,GO:0042575,GO:0003887,GO:0006260,GO:0003689
  locator: All ten term identities/definitions/synonyms/comments; relevant typed child
    links. Unrelated GO0032991 descendants not audited.
  accessed_at: '2026-10-22T05:38:54.490511Z'
  support: supports
  summary: Exact active PolIII holoenzyme/core/clamp-loader identities, native synonyms
    and typed holoenzyme parthood links are present. The clamp-loader and core definitions
    match the named structures. The beta-clamp cross-class sentence is not used as
    a stoichiometric claim here.
  snapshot_sha256: ddeb6461ed42738f76028c9ac0011c145d7cf09bf15815fc3ca84b50701c9d14
- evidence_id: root51-sources-pmid-11525729
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11525729+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact identifier/title/author/year/DOI and complete abstract
  accessed_at: '2026-10-22T05:38:57.603327Z'
  support: supports
  summary: 'Native MED11525729: Crystal structure of the processivity clamp loader
    gamma (gamma) complex of E. coli DNA polymerase III. by Jeruzalmi D, O''Donnell
    M, Kuriyan J. (2001), DOI 10.1016/s0092-8674(01)00463-9. Complete native abstract
    read; source-specific body access is stated separately.'
  snapshot_sha256: f0f86157384eba1f04a1c0446f61ac3fa213cfc4ccff0f4dba8be20a8a4e94d4
- evidence_id: root51-sources-pmid-12940977
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12940977+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact identifier/title/author/year/DOI and complete abstract
  accessed_at: '2026-10-22T05:38:57.642911Z'
  support: supports
  summary: 'Native MED12940977: Chromosomal replicases as asymmetric dimers: studies
    of subunit arrangement and functional consequences. by McHenry CS. (2003), DOI
    10.1046/j.1365-2958.2003.03645.x. Complete native abstract read; source-specific
    body access is stated separately.'
  snapshot_sha256: 36240e40d9d9df47601894cd849ca371d0afc4af98ef85efcaa76c35e32a2be2
- evidence_id: root51-sources-tax562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:38:57.355358Z'
  support: supports
  summary: ENA identifies taxon562 as Escherichia coli. Species and reference-strain
    levels are kept separate.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: root51-sources-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:38:57.520022Z'
  support: supports
  summary: ENA identifies taxon83333 as Escherichia coli K-12. Species and reference-strain
    levels are kept separate.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: root51-sources-protein-P06710
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P06710.json
  locator: Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY
    and DnaX ALTERNATIVE PRODUCTS; relevant InterPro/GO xrefs
  accessed_at: '2026-10-22T05:38:54.490836Z'
  support: supports
  summary: P06710 is the reviewed K12 dnaX entry with the declared protein identity.
    Native gene/locus tokens, function/subunit annotations, relevant GO annotation
    and family cross-references were inspected. Annotation-referenced experiments
    are not independently certified unless a separate primary-source row says so.
  snapshot_sha256: 9dda9544a27ae2699f7d77382a528089a2ff9fff43ab2d5106c4b1817d3db291
- evidence_id: root51-sources-gene-dnaX
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaX%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set for gene_exact:dnaX AND taxonomy_id:83333
    AND reviewed:true; size500
  accessed_at: '2026-10-22T05:38:54.491048Z'
  support: supports
  summary: The complete reviewed exact-gene query returns one result, P06710, with
    the expected primary gene and taxon83333.
  snapshot_sha256: 4e78670a6d5108938c60e146feb18662a8b7a5a943ceb4726382ad7b35f257a8
- evidence_id: root51-sources-protein-P28630
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P28630.json
  locator: Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY;
    relevant InterPro/GO xrefs
  accessed_at: '2026-10-22T05:38:54.492443Z'
  support: supports
  summary: P28630 is the reviewed K12 holA entry with the declared protein identity.
    Native gene/locus tokens, function/subunit annotations, relevant GO annotation
    and family cross-references were inspected. Annotation-referenced experiments
    are not independently certified unless a separate primary-source row says so.
  snapshot_sha256: 5e2a1e19871db4c2fed6d09113fd509529216b53773a162e7f1d6e6961f60934
- evidence_id: root51-sources-gene-holA
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set for gene_exact:holA AND taxonomy_id:83333
    AND reviewed:true; size500
  accessed_at: '2026-10-22T05:38:54.491203Z'
  support: supports
  summary: The complete reviewed exact-gene query returns one result, P28630, with
    the expected primary gene and taxon83333.
  snapshot_sha256: 6461857914d6912e6053148a39a941b5d47155f2970fade624132a2a0b742874
- evidence_id: root51-sources-protein-P28631
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P28631.json
  locator: Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY;
    relevant InterPro/GO xrefs
  accessed_at: '2026-10-22T05:38:55.263732Z'
  support: supports
  summary: P28631 is the reviewed K12 holB entry with the declared protein identity.
    Native gene/locus tokens, function/subunit annotations, relevant GO annotation
    and family cross-references were inspected. Annotation-referenced experiments
    are not independently certified unless a separate primary-source row says so.
  snapshot_sha256: ec3b56d7d2bc891f94eaa40f752d2ce89ad6777698e8d4b729626fed970de38a
- evidence_id: root51-sources-gene-holB
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set for gene_exact:holB AND taxonomy_id:83333
    AND reviewed:true; size500
  accessed_at: '2026-10-22T05:38:55.456789Z'
  support: supports
  summary: The complete reviewed exact-gene query returns one result, P28631, with
    the expected primary gene and taxon83333.
  snapshot_sha256: 7963053af8c79623841085f31a8a582d8d2a320210556aa12f612e166d8af7b3
- evidence_id: root51-sources-protein-P28905
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P28905.json
  locator: Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY;
    relevant InterPro/GO xrefs
  accessed_at: '2026-10-22T05:38:55.558379Z'
  support: supports
  summary: P28905 is the reviewed K12 holC entry with the declared protein identity.
    Native gene/locus tokens, function/subunit annotations, relevant GO annotation
    and family cross-references were inspected. Annotation-referenced experiments
    are not independently certified unless a separate primary-source row says so.
  snapshot_sha256: 7b36f4f87de6692ef228e17ced56294a628188d88a248f1debd62a912eef5f57
- evidence_id: root51-sources-gene-holC
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set for gene_exact:holC AND taxonomy_id:83333
    AND reviewed:true; size500
  accessed_at: '2026-10-22T05:38:55.621557Z'
  support: supports
  summary: The complete reviewed exact-gene query returns one result, P28905, with
    the expected primary gene and taxon83333.
  snapshot_sha256: 9ffe9c8d9221032fc7915464e2c8e9e9ab26683e7b264268b35ffe517dc856f0
- evidence_id: root51-sources-protein-P28632
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P28632.json
  locator: Accession, status, recommended protein name, all genes and organism; FUNCTION/SUBUNIT/SIMILARITY;
    relevant InterPro/GO xrefs
  accessed_at: '2026-10-22T05:38:55.732083Z'
  support: supports
  summary: P28632 is the reviewed K12 holD entry with the declared protein identity.
    Native gene/locus tokens, function/subunit annotations, relevant GO annotation
    and family cross-references were inspected. Annotation-referenced experiments
    are not independently certified unless a separate primary-source row says so.
  snapshot_sha256: 5b0d2927c696ac3aee8304d1e0bca6ff313e6655c90a21fa618a247a7e1dc7b2
- evidence_id: root51-sources-gene-holD
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholD%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set for gene_exact:holD AND taxonomy_id:83333
    AND reviewed:true; size500
  accessed_at: '2026-10-22T05:38:56.058495Z'
  support: supports
  summary: The complete reviewed exact-gene query returns one result, P28632, with
    the expected primary gene and taxon83333.
  snapshot_sha256: 7a9744a2b70bad7c77358c27cbde2c7602185f088d552801264210ebf52453c5
- evidence_id: root51-sources-jeruzalmi2001-pdf
  kind: primary_source
  reference: https://odonnell.rockefeller.edu/assets/pdfs/119.pdf
  locator: 'Author-hosted primary Cell106:429–441 PDF: entire Introduction, Fig1 caption,
    Results opening/Structure Determination/General Description through p431 before
    ATP-binding-domain discussion; complete Experimental Procedures pp439–440. No
    figure pixels, coordinates or unreported activity data inspected.'
  accessed_at: '2026-10-22T05:39:47.293749Z'
  support: supports
  summary: The nucleotide-free gamma3-delta-delta-prime structure contains three truncated
    gamma products and one each of delta and delta-prime. The preparation is active
    in clamp loading; the paper explicitly separates its observed structure from later
    speculative transition models. Chi/psi and tau are not crystallized constituents
    of this minimal pentamer.
  snapshot_sha256: b024aaa1d316c18a39e7f86ec5730dcd7078d94567157ca5df00d40eb7cf7211
- evidence_id: root51-sources-mchenry2003-pdf
  kind: authority
  reference: https://www.sbs.utexas.edu/psaxena/bio226r/articles/dna_replication_mchenry_2003.pdf
  locator: Complete pp1157–1158, including Fig1 caption and opening Special contributions
    of tau; later primary studies are cited context, not independently reread
  accessed_at: '2026-10-22T05:39:47.294305Z'
  support: supports
  summary: This secondary review distinguishes a three-part replicase organization
    and the E.coli DnaX3-delta-delta-prime-chi-psi heptamer. Its p1158 text explicitly
    permits any mixture of tau and gamma for clamp loading, while tau has additional
    polymerase/helicase contacts. The mixed tau/gamma model described in its abstract
    is not a universal requirement for every isolated clamp-loader preparation.
  snapshot_sha256: 943b7e0a6435e55da1766d5c567ff47410ece005e4ff3d137f150f30b2cb40d8
- evidence_id: root51-sources-GO0043846-is-a
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846/ancestors?relations=is_a
  locator: Complete is-a-only ancestor response
  accessed_at: '2026-10-22T05:40:51.733114Z'
  support: supports
  summary: The native is-a ancestry includes protein-containing complex but currently
    routes through nuclear protein-containing complex. This upstream topology is recorded
    as a conflict with the bacterial primary evidence, not propagated as a required
    biological classification.
  snapshot_sha256: 1128025335da2d8d3aa0304ebfbdd748618e7038b4623a85e7354099f7155a2b
- evidence_id: root51-sources-GO0043846-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846/constraints
  locator: Complete focal taxonConstraints array; unrelated inherited protein blacklists
    not used
  accessed_at: '2026-10-22T05:38:58.463680Z'
  support: context_only
  summary: Native GO currently reports only_in_taxon Eukaryota for this bacterial
    complex. The record has no such assertion; primary E.coli evidence and the source
    definition conflict with that upstream restriction.
  snapshot_sha256: f205df2be188d25bee5993a261d00b35ef2445e8a8567653f6e6bf733a906124
- evidence_id: root51-sources-GO0043846-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846/history
  locator: Complete history array
  accessed_at: '2026-10-22T05:38:58.411123Z'
  support: context_only
  summary: Complete native history records the2020 nuclear-parent change and a2024
    bad-taxon-ID constraint entry. This provides provenance of an upstream discrepancy,
    not bacterial taxonomic evidence.
  snapshot_sha256: db9f1d5548df0e96ee770d1bdd94bc2ffeb62eb78cf3bb48632e295acb876451
- evidence_id: root51-sources-ipr-IPR005790
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005790/
  locator: Native name/type, complete description and flags, hierarchy and member
    signatures
  accessed_at: '2026-10-22T05:39:47.488665Z'
  support: supports
  summary: Exact HolA delta full-protein family; PTHR34388/TIGR01128 signatures. The
    LLM-authored proofreading sentence is not used as delta-specific activity evidence.
  snapshot_sha256: 32531e23cefcda3d6c8294919dc4689ba859fbed120049da273ec2a452b1594f
- evidence_id: root51-sources-ipr-IPR007459
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007459/
  locator: Native name/type, complete description and flags, hierarchy and member
    signatures
  accessed_at: '2026-10-22T05:39:47.738952Z'
  support: supports
  summary: Exact HolC chi full-protein family with PF04364/PTHR38767; historical biochemical
    context is distinguished from sequence membership.
  snapshot_sha256: 5f9af2b066940512eac57ef0e983bf79616c8e00846a7fdaf4ac3eeacc116d12
- evidence_id: root51-sources-ipr-IPR004615
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004615/
  locator: Native name/type, complete description and flags, hierarchy and member
    signatures
  accessed_at: '2026-10-22T05:39:48.002942Z'
  support: supports
  summary: Exact HolD psi full-protein family with PF03603/PIRSF029225; subgroup IPR018382
    is narrower and dated unknown-function text does not override direct biochemistry.
  snapshot_sha256: 2c70542817958052c37c630066b6135d817759e1421ab5d91b21e0af5118a654
- evidence_id: root51-sources-ipr-IPR004622
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004622/
  locator: Native name/type, complete description and flags, hierarchy and member
    signatures
  accessed_at: '2026-10-22T05:39:47.488759Z'
  support: supports
  summary: This is a delta-prime N-terminal domain, not an exact whole-protein family;
    its model can also score gamma/tau proteins.
  snapshot_sha256: 1b80554d4eaa9095866a4e2ffd3b7c94281dbf076d6f123ff5346318a04a9188
- evidence_id: root51-sources-ipr-IPR012763
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012763/
  locator: Native name/type, complete description and flags, hierarchy and member
    signatures
  accessed_at: '2026-10-22T05:39:48.677205Z'
  support: supports
  summary: This is the gamma/tau N-terminal domain and includes plant STICHEL relatives;
    it cannot be substituted as an exact whole-protein DnaX family.
  snapshot_sha256: 6c8943d9fc9b647cbd674de5cdb97eb79ca5180af0898055995e986bd4cdca6b
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:08Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml'
  snapshot_sha256: 24fa6300d30a8965b07fff6b10d7da8e4eb5565a9696e3512b6e80fbe7e6d7e9
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_clamp_loader_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:10Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml\
    \ --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_clamp_loader_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_polymerase_iii_clamp_loader_complex-strict.tsv"
  snapshot_sha256: f1dcc9a1c64cb14e8e633ea4be16c47066c92cfd5736266e8b9f106871c42000
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:38:45.810102Z'
  support: supports
  summary: "data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml  (GO:0043846)\n\
    \  clamp_loader_beta_clamp_loading\tdnax_tau_gamma_subunit\tCOVERED\t->dnax_tau_gamma_subunit\
    \ (UniProtKB:P06710)\n  clamp_loader_beta_clamp_loading\tdelta_subunit\tCOVERED\t\
    ->delta_subunit (UniProtKB:P28630)\n  clamp_loader_beta_clamp_loading\tdelta_prime_subunit\t\
    COVERED\t->delta_prime_subunit (UniProtKB:P28631)\n  clamp_loader_beta_clamp_loading\t\
    chi_subunit\tCOVERED\t->chi_subunit (UniProtKB:P28905)\n  clamp_loader_beta_clamp_loading\t\
    psi_subunit\tCOVERED\t->psi_subunit (UniProtKB:P28632)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     5  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     5  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: aca3b51abc154a55cd6b3d81b01fc8a21768e3ec3940102586a9945621646d06
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:39:31.344651Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: initial-verify-dns
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  locator: Preserved initial sandbox DNS failure log
  accessed_at: '2026-10-22T05:38:58.268799Z'
  support: context_only
  summary: The first native verification could not resolve UniProt DNS; a subsequent
    authorized network run passed with unchanged inputs.
  snapshot_sha256: 638316eb6d04c49acacf1717010fa10a01d9d9954e01afa43caa919455bb88b3
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '16 of 18 collected target identifiers returned OK. PMID:11525729: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force.; PMID:12940977: UNREACHABLE; Exact native EuropePMC MED identifier, title
    and DOI independently inspected after the bulk eutils414 transport failure. Identifier
    resolution does not certify all biological claims; declared primary-body and abstract
    reading limits remain in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
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
  topic: DnaX heptamer versus crystallized pentamer
  outcome: concern
  target_ids:
  - GO:0043846
  summary: The named heptamer and holoenzyme parthood are sound. Jeruzalmi crystallized
    a minimal gamma3-delta-delta-prime pentamer, while McHenry describes the heptamer
    including chi/psi. The definition should express three DnaX copies with tau/gamma
    alternatives instead of implying both are invariant.
  evidence_ids:
  - record
  - root51-sources-go
  - root51-sources-jeruzalmi2001-pdf
  - root51-sources-mchenry2003-pdf
  - root51-sources-GO0043846-is-a
- assessment_id: composition
  area: grounding
  topic: Five correct protein classes; exact family resolution
  outcome: concern
  target_ids:
  - GO:0043846
  summary: The five K12 examples and their GO annotations match current native records.
    HolA, HolC and HolD have exact available families; HolB and DnaX candidates inspected
    here are domains and are not safe whole-protein replacements. Family membership
    comes from the separately cited UniProt xrefs, not from the family metadata response.
  evidence_ids:
  - record
  - curation
  - root51-sources-protein-P06710
  - root51-sources-protein-P28630
  - root51-sources-protein-P28631
  - root51-sources-protein-P28905
  - root51-sources-protein-P28632
  - root51-sources-gene-dnaX
  - root51-sources-gene-holA
  - root51-sources-gene-holB
  - root51-sources-gene-holC
  - root51-sources-gene-holD
  - root51-sources-ipr-IPR005790
  - root51-sources-ipr-IPR007459
  - root51-sources-ipr-IPR004615
  - root51-sources-ipr-IPR004622
  - root51-sources-ipr-IPR012763
- assessment_id: scope
  area: scope
  topic: Species example and reference strain
  outcome: supported
  target_ids:
  - GO:0043846
  summary: The canonical note correctly says E.coli is the source species of the solved
    gamma structure; it does not claim a full heptamer was crystallized. Reference
    K12 example identities are verified independently. The actual sample uses truncated
    gamma1–373 and purified reconstitution; no unmodified K12 preparation is inferred.
  evidence_ids:
  - record
  - root51-sources-jeruzalmi2001-pdf
  - root51-sources-tax562
  - root51-sources-tax83333
  - root51-sources-protein-P06710
  - root51-sources-protein-P28630
  - root51-sources-protein-P28631
  - root51-sources-protein-P28905
  - root51-sources-protein-P28632
- assessment_id: graph
  area: graph
  topic: Nine descriptive edges and model limits
  outcome: supported
  target_ids:
  - GO:0043846
  summary: All five constituent nodes are supported at the appropriate complex scope.
    Delta binds beta, and the clamp loader loads beta onto primer-template DNA and
    supports replication. Jeruzalmi labels its transition mechanism speculative; the
    target remains NONMECHANISTIC and does not assert direct visualization of ATP-driven
    motion. Chi/psi membership comes from GO and the McHenry body, not the pentamer
    crystal.
  evidence_ids:
  - record
  - graph-rubric
  - root51-sources-go
  - root51-sources-jeruzalmi2001-pdf
  - root51-sources-mchenry2003-pdf
- assessment_id: formation
  area: grounding
  topic: Defining composition is not a loss-of-assembly experiment
  outcome: unknown
  target_ids:
  - GO:0043846
  summary: The full heptamer has five protein classes and three DnaX copies. Active
    minimal-pentamer reconstitution does not prove that chi/psi are dispensable for
    formation of the scoped heptamer, nor does clamp-loading activity prove every
    member is physically necessary. UNKNOWN formation essentiality remains appropriate;
    tau and gamma alternatives need explicit wording.
  evidence_ids:
  - record
  - schema
  - root51-sources-jeruzalmi2001-pdf
  - root51-sources-mchenry2003-pdf
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target
  outcome: supported
  target_ids:
  - GO:0043846
  summary: All fields, history, discussions and edge evidence were reviewed. Optional
    images, dimensions or prevalence inventories are not filled without evidence.
    Cited authority identities and source-scoped claims were checked separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root51-sources-go
findings:
- finding_id: F1
  issue_key: pol-iii-clamp-loader-dnax-mixture
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: State the three DnaX copies and their alternatives
  description: The definition unconditionally says the heptamer includes tau and gamma.
    Its cited McHenry2003 body p1158 instead specifies DnaX3-delta-delta-prime-chi-psi
    with any mixture of tau and gamma for clamp loading, and native DnaX annotations
    agree. The original GO sentence matches the record but compresses the source distinction.
  target_ids:
  - GO:0043846
  field_paths:
  - definition
  - components#dnax_tau_gamma_subunit.role
  evidence_ids:
  - record
  - root51-sources-go
  - root51-sources-mchenry2003-pdf
  - root51-sources-protein-P06710
  - root51-sources-protein-P28630
  - root51-sources-protein-P28631
  - root51-sources-protein-P28905
  - root51-sources-protein-P28632
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-scoped composition
  native_severity: minor
  normalization_reason: Correct structure identity, supported protein examples and
    core functional model remain intact; the defect is a bounded mapping or composition-wording
    gap.
- finding_id: F2
  issue_key: pol-iii-clamp-loader-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the available HolA, HolC and HolD families
  description: These three components remain REVIEWED_LABEL_ONLY despite verified
    whole-protein families IPR005790, IPR007459 and IPR004615 and matching current
    UniProt-example xrefs. The reviewed HolB/DnaX candidates are domains and do not
    justify forcing a mapping.
  target_ids:
  - GO:0043846
  field_paths:
  - components#delta_subunit.grounding_status
  - components#chi_subunit.grounding_status
  - components#psi_subunit.grounding_status
  - discussions#resolve_pol_iii_clamp_loader_groundings
  evidence_ids:
  - record
  - curation
  - root51-sources-ipr-IPR005790
  - root51-sources-ipr-IPR007459
  - root51-sources-ipr-IPR004615
  - root51-sources-ipr-IPR004622
  - root51-sources-ipr-IPR012763
  - root51-sources-protein-P06710
  - root51-sources-protein-P28630
  - root51-sources-protein-P28631
  - root51-sources-protein-P28905
  - root51-sources-protein-P28632
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-scoped composition
  native_severity: minor
  normalization_reason: Correct structure identity, supported protein examples and
    core functional model remain intact; the defect is a bounded mapping or composition-wording
    gap.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0043846
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    role: maintained scientific record
  description: Qualify the E.coli heptamer model as three DnaX products, tau and/or
    gamma, plus delta, delta-prime, chi and psi. Keep additional tau-dependent fork
    organization separate from minimum clamp loading.
  acceptance_checks:
  - Do not universalize one tau:gamma ratio or require both products in every assembly.
  - Do not replace the full heptamer identity with the crystallized pentamer.
  - Preserve source scope and correct current protein examples; pass applicable native
    validators.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0043846
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    role: maintained scientific record
  description: Map the three verified exact families and narrow the current unresolved
    TODO to genuinely unresolved classes. Preserve the five correct protein examples.
  acceptance_checks:
  - Keep IPR004622/IPR012763 domain matches separate from whole-protein identity.
  - Do not import a family description claiming delta proofreading activity.
  - Preserve source scope and correct current protein examples; pass applicable native
    validators.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, coordinates, sequence alignments or raw kinetic data were reanalyzed.
  Native annotations and a secondary review remain distinct from independently inspected
  primary methods.
- Native GO currently assigns this term nuclear-complex ancestry and an Eukaryota-only
  restriction, conflicting with the cited E.coli evidence. Neither assertion is present
  in the target. Keep its exact named identity and supported bacterial example; do
  not import the erroneous source restriction or infer occurrence in every bacterium.
- Initial focused UniProt verification failed solely on sandbox DNS. Its original
  traceback is retained; the subsequent network-enabled native check passed for unchanged
  input bytes.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes qualified clean reviews as well as issue-bearing
  reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
