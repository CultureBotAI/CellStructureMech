# AP-5 adaptor complex scientific review

- Review: 20261022T044318Z-ap-5-adaptor-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:25:19Z
- Finished UTC: 2026-10-22T04:43:18Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor finding: all four exact AP5 subunit families are verified but withheld under reviewed-label-only status. Correct identities, examples and cautious endosomal-sorting graph are supported.

## Scope And Provenance

Exactly one complete maintained AP-5 adaptor complex record; frozen native inputs, actual source identities and the specific primary/review/native sections declared in evidence. Full-field review does not imply full reading of every downloaded article or its supplements.

Selection: Batch45 strict path-ordered target 1; initial native inspection/schema/strict gates all passed at unchanged f97b before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0044599 | data/structures/other/ap_5_adaptor_complex.yaml | maintained | AP-5 adaptor complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0044599 | Focused validator passed. |
| Focused native strict | passed | True | GO:0044599 | Focused validator passed. |
| Native verify | passed | True | GO:0044599 | Native diagnostics passed; scientific claims and scope were assessed separately. |
| Native causal-graphs | passed | True | GO:0044599 | Native diagnostics passed; scientific claims and scope were assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0044599 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0044599 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0044599 | 8 of 10 collected target identifiers returned OK. PMID:20613862: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:22022230: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0044599 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0044599 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0044599 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0044599 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0044599 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact AP5 class, synonym and subtype boundary

identity: supported. Targets: GO:0044599.

The native identifier, four-subunit definition, AP-type is_a parent and exact synonym match. The record correctly avoids equating AP5 with a constitutive clathrin coat.

### Four exact subtype families are available

grounding: concern. Targets: GO:0044599.

All four native entries are family-level AP5-specific identities, not domains: ap5_beta5_subunit → InterPro:IPR038741, ap5_zeta_subunit → InterPro:IPR028222, ap5_mu5_subunit → InterPro:IPR039591, ap5_sigma5_subunit → InterPro:IPR029392. Each is cross-referenced by the matching maintained human protein. Their current REVIEWED_LABEL_ONLY status and deferred-CURIE rationale conflict with the exact-family contract; no biological membership or accession error is asserted.

### Four verified human examples and exact cited localizations

evidence: supported. Targets: GO:0044599.

All four maintained accession/gene/taxon/status pairs and present single-hit query claims are supported. The source gives independent AP5 membership beyond the identity-only example notes; O43299 cytoplasmic localization is supported by Slabicki rather than inferred from the word AP5. Cytoplasmic versus late-endosomal annotation and isoform conditions are kept distinct.

### Human HeLa model and occurrence

scope: supported. Targets: GO:0044599.

COMMON retains the schema majority-occurrence meaning. Characterization of the human complex supports the qualitative organism-level synthesis without a population census or evidence that every cell has the same tagged localization. HeLaM knockdown/expression conditions support the stated example; no broad universal eukaryotic occurrence is inferred.

### Cautious endosomal-sorting topology

graph: supported. Targets: GO:0044599.

Four constituent edges, endosomal association and the is implicated in sorting edge match the inspected source scope. The tagged-protein and knockdown observations are accurately separated. Perturbed CI-MPR/Vps26 distribution does not establish a direct cargo-binding motif or exclusive transport direction; the NONMECHANISTIC graph does not claim one.

### Supported constituent classes separated from formation necessity

evidence: unknown. Targets: GO:0044599.

The components all retain UNKNOWN essentiality. Observed membership, interaction, sorting or invasion phenotypes do not establish universal assembly necessity for each individual constituent of these classes. No necessity upgrade is made.

### Entire maintained record and evidence placement assessed

completeness: supported. Targets: GO:0044599.

All maintained identity, history, component, example, taxonomic, function, graph and discussion fields were inspected. Optional exhaustive accessory-protein, taxon or mechanism inventories are not required. No scientific status/history promotion or source-quotation insertion is proposed.

## Findings

### F1: Ground the four verified AP5 subunit families

minor / open / confirmed; issue key: ap5-four-verified-family-groundings-label-only.

The native family identities ap5_beta5_subunit → InterPro:IPR038741, ap5_zeta_subunit → InterPro:IPR028222, ap5_mu5_subunit → InterPro:IPR039591, ap5_sigma5_subunit → InterPro:IPR029392 exactly match the four maintained AP5-specific subunit classes and their human examples. All four rows instead retain REVIEWED_LABEL_ONLY with notes saying no exact CURIE was curated in the earlier pass. The schema and CURATION define that status as inability to assert an exact class, not unfinished identifier curation.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, assign ap5_beta5_subunit → InterPro:IPR038741, ap5_zeta_subunit → InterPro:IPR028222, ap5_mu5_subunit → InterPro:IPR039591, ap5_sigma5_subunit → InterPro:IPR029392, remove incompatible reviewed-label-only status/notes and close or update the exact-family TODO. Retain the four components, correct examples, UNKNOWN assembly necessity and qualified clathrin/sorting scope.

- Each mapped accession resolves to its stated AP5-specific family and matches the intended subtype class.
- The four current human identities and constituent roles remain unchanged; no domain or accessory factor replaces a core class.
- Focused schema/strict, protein and graph checks pass after the authorized scientific edit.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/ap_5_adaptor_complex.yaml; Entire maintained target, including history, identity, components, taxa, examples, functions, graph and discussions | context_only | Complete target read. Historical curation actions are provenance rather than independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent grounding/essentiality, ProteinExample, graph and COMMON contracts | context_only | Exact class grounding differs from a protein instance or partial domain; UNKNOWN assembly necessity is not converted to a requirement from activity or constituent identity. COMMON means present in most members, with losses exceptional. |
| curation | docs/CURATION.md; Grounding and REVIEWED_LABEL_ONLY rules, lines150–162 | context_only | Reviewed label-only means no exact term can be asserted without overclaiming; it does not mean merely not curated during an earlier pass. |
| ap45-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044599,GO:0030119,GO:0098796,GO:0030117,GO:0020007,GO:0020010,GO:0020031,GO:0020008,GO:0020009; GO0044599 complete term and its exact typed child relation in GO0030119; no unrelated combined-query term is used to prove this identity | supports | GO0044599 is active, exactly names/defines AP5 beta5/zeta/mu5/sigma5, carries the maintained exact synonym and is an is_a child of GO0030119. It leaves clathrin association unresolved; the parent definition has a separate outdated subtype list assessed in the separate parent review. |
| ap45-agent-tax9606 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9606; Complete native taxonomy response | supports | ENA identifies 9606 as Homo sapiens, rank species. This verifies the taxon only, not organism frequency or experimental strain. |
| ap45-agent-hirst2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1371/journal.pbio.1001170%22; Complete unique native Europe PMC MED identity, authors/title/year, DOI/PMID/PMC when returned and abstract | supports | Hirst et al.2011, The fifth adaptor protein complex, DOI10.1371/journal.pbio.1001170, PMID22022230, PMC3191125; complete abstract supports AP5 endosomal sorting and HeLa localization with qualified phylogenetic scope. |
| ap45-agent-hirst2011-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3191125/fullTextXML; Genuine JATS: complete Introduction s1; Results s2a/s2b/s2c/s2d/s2f including Figure1–4,8/9 captions and Table1; entire Discussion s3 including Figure10 caption; Methods s4c/s4d/s4e. Phylogenetic Results s2e, other Methods, supplements and figure pixels not inspected. | supports | Biochemistry and pairwise interactions support beta5/zeta/mu5/sigma5 AP5. Tagged mu5 localization required reducing overexpression/background; sigma5-GFP localizes to LAMP1-positive compartments. Knockdown affects CI-MPR/Vps26 and endosomal morphology, but the precise route/cargo-selection mechanism remains inferred. The corrected beta5 is 878 residues and predicted94kDa, unlike the parent gloss110–130kDa; zeta is explicitly the other large chain. Clathrin association is not supported in the tested preparations. |
| ap45-agent-pmid-20613862 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A20613862%20AND%20SRC%3AMED; Complete unique native Europe PMC MED identity, authors/title/year, DOI/PMID/PMC when returned and abstract | supports | Slabicki et al.2010, A genome-scale DNA repair RNAi screen identifies SPG48 as a novel gene associated with hereditary spastic paraplegia, DOI10.1371/journal.pbio.1000408/PMID20613862/PMC2893954. The exact complete abstract verifies the identity of the localization reference. |
| ap45-agent-slabicki2010-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2893954/fullTextXML; Genuine JATS: complete Results s2f including Figure5/6 captions; Methods s4i/s4j/s4k. Other sections, supplemental files and pixels not inspected. | supports | The BAC-tagged KIAA0415/SPG48 protein is detected in cytoplasmic and nuclear fractions, with different isoform biases; interaction experiments identify its partners. This supports the narrow UniProt cytoplasmic-localization attribution. Its historical putative-helicase/DNA-repair interpretation is not promoted to an AP5 sorting mechanism. |
| ap45-agent-family-search-AP5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-5&amp;page_size=200; Complete candidate accession/name/type list and pagination | context_only | The bounded AP5 InterPro search returns nine entries with no next page: four exact subunit families and five domains. Candidate names/types guide, but do not replace, each separately read family entry. |
| ap45-agent-ipr-IPR038741 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038741/; Native accession/name/type, complete description, LLM flags, integrated signatures and hierarchy | supports | IPR038741 is type family, named AP-5 complex subunit beta-1. The complete description, member signatures and LLM flags were read to distinguish exact AP5 subtype families from broader adaptor classes and domains. |
| ap45-agent-protein-Q2VPB7 | https://rest.uniprot.org/uniprotkb/Q2VPB7.json; Exact native identity/name/status/genes/taxon, function/subunit/location comments and InterPro crossrefs | supports | Q2VPB7 is the reviewed Homo sapiens9606 AP5B1 AP5 subunit, with the maintained accession/name/gene/status and exact IPR038741 cross-reference. Native function/subunit/location comments were read. The Hirst-linked membership and any cytosolic/location annotation remain bounded to their cited experiments. |
| ap45-agent-gene-AP5B1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AAP5B1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29; All returned reviewed entry identities and primary/alias gene fields | context_only | The current exact reviewed AP5B1 query at organism9606 returns one entry, Q2VPB7; primary gene and aliases were checked. This confirms current uniqueness, not a reconstruction of the historical query. |
| ap45-agent-ipr-IPR028222 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028222/; Native accession/name/type, complete description, LLM flags, integrated signatures and hierarchy | supports | IPR028222 is type family, named AP-5 complex subunit zeta-1. The complete description, member signatures and LLM flags were read to distinguish exact AP5 subtype families from broader adaptor classes and domains. |
| ap45-agent-protein-O43299 | https://rest.uniprot.org/uniprotkb/O43299.json; Exact native identity/name/status/genes/taxon, function/subunit/location comments and InterPro crossrefs | supports | O43299 is the reviewed Homo sapiens9606 AP5Z1 AP5 subunit, with the maintained accession/name/gene/status and exact IPR028222 cross-reference. Native function/subunit/location comments were read. AP5Z1 has KIAA0415/SPG48 aliases and the Slabicki cytoplasmic/nuclear annotation. |
| ap45-agent-gene-AP5Z1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AAP5Z1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29; All returned reviewed entry identities and primary/alias gene fields | context_only | The current exact reviewed AP5Z1 query at organism9606 returns one entry, O43299; primary gene and aliases were checked. This confirms current uniqueness, not a reconstruction of the historical query. |
| ap45-agent-ipr-IPR039591 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039591/; Native accession/name/type, complete description, LLM flags, integrated signatures and hierarchy | supports | IPR039591 is type family, named AP-5 complex subunit mu-1. The complete description, member signatures and LLM flags were read to distinguish exact AP5 subtype families from broader adaptor classes and domains. |
| ap45-agent-protein-Q9H0R1 | https://rest.uniprot.org/uniprotkb/Q9H0R1.json; Exact native identity/name/status/genes/taxon, function/subunit/location comments and InterPro crossrefs | supports | Q9H0R1 is the reviewed Homo sapiens9606 AP5M1 AP5 subunit, with the maintained accession/name/gene/status and exact IPR039591 cross-reference. Native function/subunit/location comments were read. The Hirst-linked membership and any cytosolic/location annotation remain bounded to their cited experiments. |
| ap45-agent-gene-AP5M1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AAP5M1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29; All returned reviewed entry identities and primary/alias gene fields | context_only | The current exact reviewed AP5M1 query at organism9606 returns one entry, Q9H0R1; primary gene and aliases were checked. This confirms current uniqueness, not a reconstruction of the historical query. |
| ap45-agent-ipr-IPR029392 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029392/; Native accession/name/type, complete description, LLM flags, integrated signatures and hierarchy | supports | IPR029392 is type family, named AP-5 complex subunit sigma-1. The complete description, member signatures and LLM flags were read to distinguish exact AP5 subtype families from broader adaptor classes and domains. |
| ap45-agent-protein-Q9NUS5 | https://rest.uniprot.org/uniprotkb/Q9NUS5.json; Exact native identity/name/status/genes/taxon, function/subunit/location comments and InterPro crossrefs | supports | Q9NUS5 is the reviewed Homo sapiens9606 AP5S1 AP5 subunit, with the maintained accession/name/gene/status and exact IPR029392 cross-reference. Native function/subunit/location comments were read. The Hirst-linked membership and any cytosolic/location annotation remain bounded to their cited experiments. |
| ap45-agent-gene-AP5S1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AAP5S1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29; All returned reviewed entry identities and primary/alias gene fields | context_only | The current exact reviewed AP5S1 query at organism9606 returns one entry, Q9NUS5; primary gene and aliases were checked. This confirms current uniqueness, not a reconstruction of the historical query. |
| schema-result | just validate data/structures/other/ap_5_adaptor_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/ap_5_adaptor_complex.yaml |
| strict-result | just validate-strict data/structures/other/ap_5_adaptor_complex.yaml --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/ap_5_adaptor_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/ap_5_adaptor_complex.yaml --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/ap_5_adaptor_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch45-20261022-mptgrq24/ap_5_adaptor_complex-strict.tsv |
| ap5-verify | /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/ap_5_adaptor_complex.yaml; Complete retained read-only native log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| ap5-causal-graphs | /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ap_5_adaptor_complex.yaml; Complete retained read-only native log | supports | data/structures/other/ap_5_adaptor_complex.yaml  (GO:0044599)<br>  ap5_adaptor_complex_topology	ap5_beta5_subunit	COVERED	-&gt;ap5_beta5_subunit (UniProtKB:Q2VPB7)<br>  ap5_adaptor_complex_topology	ap5_zeta_subunit	COVERED	-&gt;ap5_zeta_subunit (UniProtKB:O43299)<br>  ap5_adaptor_complex_topology	ap5_mu5_subunit	COVERED	-&gt;ap5_mu5_subunit (UniProtKB:Q9H0R1)<br>  ap5_adaptor_complex_topology	ap5_sigma5_subunit	COVERED	-&gt;ap5_sigma5_subunit (UniProtKB:Q9NUS5)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/ap_5_adaptor_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 10 collected target identifiers returned OK. PMID:20613862: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:22022230: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- The five completed same-base batch26 corpus gates await guarded integration by the parent before finalization.
- No image pixels, supplemental files, new sequence alignments or quantitative prevalence census were inspected. The individually declared sections, not every downloaded article paragraph, define the literature-read scope.
- Hirst localization is not an unqualified observation of all native AP5 molecules: tagged mu5 required knockdown/damping of diffuse background and sigma5 imaging used extraction. The record already distinguishes complex identification from tagged localization.
- The family search is bounded to the recorded InterPro query and four separately verified entries. No claim that all possible annotations or accessory-protein inventories were surveyed is made. Slabicki historical DNA-repair/putative-helicase wording is context only.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes an honest bundle for each uncovered target, including clean reviews. Parent owns global-gate integration/finalization; no scientific edits, persistence or Git mutation performed.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T044318Z-ap-5-adaptor-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: AP-5 adaptor complex scientific review
started_at: '2026-10-22T04:25:19Z'
finished_at: '2026-10-22T04:43:18Z'
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
summary: 'One minor finding: all four exact AP5 subunit families are verified but
  withheld under reviewed-label-only status. Correct identities, examples and cautious
  endosomal-sorting graph are supported.'
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: data/structures/other/ap_5_adaptor_complex.yaml
    sha256: d951b48b8f9fe05db066c722dd2dad8277f04eb4af1ac36bf4a5c03932ac82dc
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
- target_id: GO:0044599
  path: data/structures/other/ap_5_adaptor_complex.yaml
  label: AP-5 adaptor complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_5_adaptor_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained AP-5 adaptor complex record; frozen
    native inputs, actual source identities and the specific primary/review/native
    sections declared in evidence. Full-field review does not imply full reading of
    every downloaded article or its supplements.
  selection: Batch45 strict path-ordered target 1; initial native inspection/schema/strict
    gates all passed at unchanged f97b before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0044599
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: just validate data/structures/other/ap_5_adaptor_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: just validate-strict data/structures/other/ap_5_adaptor_complex.yaml --out
    /private/tmp/cellstructure-batch45-20261022-mptgrq24/ap_5_adaptor_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/ap_5_adaptor_complex.yaml
  exit_code: 0
  summary: Native diagnostics passed; scientific claims and scope were assessed separately.
  evidence_ids:
  - ap5-verify
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ap_5_adaptor_complex.yaml
  exit_code: 0
  summary: Native diagnostics passed; scientific claims and scope were assessed separately.
  evidence_ids:
  - ap5-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0044599
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0044599
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - ap45-agent-go
  - ap45-agent-tax9606
  - ap45-agent-hirst2011-meta
  - ap45-agent-hirst2011-xml
  - ap45-agent-pmid-20613862
  - ap45-agent-slabicki2010-xml
  - ap45-agent-family-search-AP5
  - ap45-agent-ipr-IPR038741
  - ap45-agent-protein-Q2VPB7
  - ap45-agent-gene-AP5B1
  - ap45-agent-ipr-IPR028222
  - ap45-agent-protein-O43299
  - ap45-agent-gene-AP5Z1
  - ap45-agent-ipr-IPR039591
  - ap45-agent-protein-Q9H0R1
  - ap45-agent-gene-AP5M1
  - ap45-agent-ipr-IPR029392
  - ap45-agent-protein-Q9NUS5
  - ap45-agent-gene-AP5S1
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0044599
  summary: '8 of 10 collected target identifiers returned OK. PMID:20613862: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:22022230:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - ap45-agent-pmid-20613862
  - ap45-agent-hirst2011-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0044599
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
    and current batch45 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/ap_5_adaptor_complex.yaml
  locator: Entire maintained target, including history, identity, components, taxa,
    examples, functions, graph and discussions
  accessed_at: '2026-10-22T04:31:37Z'
  support: context_only
  summary: Complete target read. Historical curation actions are provenance rather
    than independent scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent grounding/essentiality, ProteinExample, graph and COMMON
    contracts
  accessed_at: '2026-10-22T04:31:37Z'
  support: context_only
  summary: Exact class grounding differs from a protein instance or partial domain;
    UNKNOWN assembly necessity is not converted to a requirement from activity or
    constituent identity. COMMON means present in most members, with losses exceptional.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Grounding and REVIEWED_LABEL_ONLY rules, lines150–162
  accessed_at: '2026-10-22T04:31:37Z'
  support: context_only
  summary: Reviewed label-only means no exact term can be asserted without overclaiming;
    it does not mean merely not curated during an earlier pass.
- evidence_id: ap45-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044599,GO:0030119,GO:0098796,GO:0030117,GO:0020007,GO:0020010,GO:0020031,GO:0020008,GO:0020009
  locator: GO0044599 complete term and its exact typed child relation in GO0030119;
    no unrelated combined-query term is used to prove this identity
  accessed_at: '2026-10-22T04:26:12.185695Z'
  support: supports
  summary: GO0044599 is active, exactly names/defines AP5 beta5/zeta/mu5/sigma5, carries
    the maintained exact synonym and is an is_a child of GO0030119. It leaves clathrin
    association unresolved; the parent definition has a separate outdated subtype
    list assessed in the separate parent review.
  snapshot_sha256: a713b4e9448e2e08e74e577c6dc7c355ca849d5fbbb7c1de1889f1efec199a1a
- evidence_id: ap45-agent-tax9606
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9606
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:26:12.185331Z'
  support: supports
  summary: ENA identifies 9606 as Homo sapiens, rank species. This verifies the taxon
    only, not organism frequency or experimental strain.
  snapshot_sha256: ae6861231eabbe5c76a3e6240a9109a3163b77f2061b644c22bbdd1b01b15840
- evidence_id: ap45-agent-hirst2011-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1371/journal.pbio.1001170%22
  locator: Complete unique native Europe PMC MED identity, authors/title/year, DOI/PMID/PMC
    when returned and abstract
  accessed_at: '2026-10-22T04:26:13.999299Z'
  support: supports
  summary: Hirst et al.2011, The fifth adaptor protein complex, DOI10.1371/journal.pbio.1001170,
    PMID22022230, PMC3191125; complete abstract supports AP5 endosomal sorting and
    HeLa localization with qualified phylogenetic scope.
  snapshot_sha256: 990735219b8c0742f1b5c024ac389e3b293c817e9654ad39cb8ed81047108e94
- evidence_id: ap45-agent-hirst2011-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3191125/fullTextXML
  locator: 'Genuine JATS: complete Introduction s1; Results s2a/s2b/s2c/s2d/s2f including
    Figure1–4,8/9 captions and Table1; entire Discussion s3 including Figure10 caption;
    Methods s4c/s4d/s4e. Phylogenetic Results s2e, other Methods, supplements and
    figure pixels not inspected.'
  accessed_at: '2026-10-22T04:26:34.158746Z'
  support: supports
  summary: Biochemistry and pairwise interactions support beta5/zeta/mu5/sigma5 AP5.
    Tagged mu5 localization required reducing overexpression/background; sigma5-GFP
    localizes to LAMP1-positive compartments. Knockdown affects CI-MPR/Vps26 and endosomal
    morphology, but the precise route/cargo-selection mechanism remains inferred.
    The corrected beta5 is 878 residues and predicted94kDa, unlike the parent gloss110–130kDa;
    zeta is explicitly the other large chain. Clathrin association is not supported
    in the tested preparations.
  snapshot_sha256: 0768f8cbad56fcc2885542c578a4b656859fca5ba30ce216a85d16782e1f6571
- evidence_id: ap45-agent-pmid-20613862
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A20613862%20AND%20SRC%3AMED
  locator: Complete unique native Europe PMC MED identity, authors/title/year, DOI/PMID/PMC
    when returned and abstract
  accessed_at: '2026-10-22T04:26:14.725411Z'
  support: supports
  summary: Slabicki et al.2010, A genome-scale DNA repair RNAi screen identifies SPG48
    as a novel gene associated with hereditary spastic paraplegia, DOI10.1371/journal.pbio.1000408/PMID20613862/PMC2893954.
    The exact complete abstract verifies the identity of the localization reference.
  snapshot_sha256: de238ae86a8413d45faba4d0b536fbf61ec31c7c2ea628d05d3731de1b27c5be
- evidence_id: ap45-agent-slabicki2010-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2893954/fullTextXML
  locator: 'Genuine JATS: complete Results s2f including Figure5/6 captions; Methods
    s4i/s4j/s4k. Other sections, supplemental files and pixels not inspected.'
  accessed_at: '2026-10-22T04:26:34.942455Z'
  support: supports
  summary: The BAC-tagged KIAA0415/SPG48 protein is detected in cytoplasmic and nuclear
    fractions, with different isoform biases; interaction experiments identify its
    partners. This supports the narrow UniProt cytoplasmic-localization attribution.
    Its historical putative-helicase/DNA-repair interpretation is not promoted to
    an AP5 sorting mechanism.
  snapshot_sha256: fe7ac53d14ba2ca6fc0b911e4bb714161b8e1abec29b00277fcc8073e8cc5c32
- evidence_id: ap45-agent-family-search-AP5
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-5&page_size=200
  locator: Complete candidate accession/name/type list and pagination
  accessed_at: '2026-10-22T04:26:15.057119Z'
  support: context_only
  summary: 'The bounded AP5 InterPro search returns nine entries with no next page:
    four exact subunit families and five domains. Candidate names/types guide, but
    do not replace, each separately read family entry.'
  snapshot_sha256: 22f406bd1fcb40745c7db59270746fae6de5c3ed49599fbc7ff3d2635b3896ab
  search_scope: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-5&page_size=200
- evidence_id: ap45-agent-ipr-IPR038741
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038741/
  locator: Native accession/name/type, complete description, LLM flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T04:26:34.158690Z'
  support: supports
  summary: IPR038741 is type family, named AP-5 complex subunit beta-1. The complete
    description, member signatures and LLM flags were read to distinguish exact AP5
    subtype families from broader adaptor classes and domains.
  snapshot_sha256: 9dcc8b54579b5d9162aded260904a30a25bc944333b8958eabb7014cfdd79869
- evidence_id: ap45-agent-protein-Q2VPB7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q2VPB7.json
  locator: Exact native identity/name/status/genes/taxon, function/subunit/location
    comments and InterPro crossrefs
  accessed_at: '2026-10-22T04:26:13.036674Z'
  support: supports
  summary: Q2VPB7 is the reviewed Homo sapiens9606 AP5B1 AP5 subunit, with the maintained
    accession/name/gene/status and exact IPR038741 cross-reference. Native function/subunit/location
    comments were read. The Hirst-linked membership and any cytosolic/location annotation
    remain bounded to their cited experiments.
  snapshot_sha256: 05e9ffb34a92f4558d354dc78b6e8dea7417623b9c890fc8dfd06db95aacd1aa
- evidence_id: ap45-agent-gene-AP5B1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5B1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned reviewed entry identities and primary/alias gene fields
  accessed_at: '2026-10-22T04:26:13.061105Z'
  support: context_only
  summary: The current exact reviewed AP5B1 query at organism9606 returns one entry,
    Q2VPB7; primary gene and aliases were checked. This confirms current uniqueness,
    not a reconstruction of the historical query.
  snapshot_sha256: 35ba81ef29bbebeb0ba091ca930351c9d1b6aca5c19eb646768f8be5de214139
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5B1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: ap45-agent-ipr-IPR028222
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028222/
  locator: Native accession/name/type, complete description, LLM flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T04:26:34.158012Z'
  support: supports
  summary: IPR028222 is type family, named AP-5 complex subunit zeta-1. The complete
    description, member signatures and LLM flags were read to distinguish exact AP5
    subtype families from broader adaptor classes and domains.
  snapshot_sha256: 58606c459d23c3d8d20143f67c466f88cdb3e326282c429ace58956157d96681
- evidence_id: ap45-agent-protein-O43299
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O43299.json
  locator: Exact native identity/name/status/genes/taxon, function/subunit/location
    comments and InterPro crossrefs
  accessed_at: '2026-10-22T04:26:13.043030Z'
  support: supports
  summary: O43299 is the reviewed Homo sapiens9606 AP5Z1 AP5 subunit, with the maintained
    accession/name/gene/status and exact IPR028222 cross-reference. Native function/subunit/location
    comments were read. AP5Z1 has KIAA0415/SPG48 aliases and the Slabicki cytoplasmic/nuclear
    annotation.
  snapshot_sha256: bd057a0050e1996d438e5d681e2fa6e4880291b6d1cbb3131a526814cdfc75e6
- evidence_id: ap45-agent-gene-AP5Z1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5Z1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned reviewed entry identities and primary/alias gene fields
  accessed_at: '2026-10-22T04:26:13.814452Z'
  support: context_only
  summary: The current exact reviewed AP5Z1 query at organism9606 returns one entry,
    O43299; primary gene and aliases were checked. This confirms current uniqueness,
    not a reconstruction of the historical query.
  snapshot_sha256: 0496b6b2fbc12203d00ad86cbd6af7cf0d05e5b2a7cd3b490c0e398df9a07234
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5Z1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: ap45-agent-ipr-IPR039591
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039591/
  locator: Native accession/name/type, complete description, LLM flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T04:26:34.158477Z'
  support: supports
  summary: IPR039591 is type family, named AP-5 complex subunit mu-1. The complete
    description, member signatures and LLM flags were read to distinguish exact AP5
    subtype families from broader adaptor classes and domains.
  snapshot_sha256: bc6b499374cb70c152fcb68597afe765a3bd0925d9508583ab1fb85cbcf5071f
- evidence_id: ap45-agent-protein-Q9H0R1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9H0R1.json
  locator: Exact native identity/name/status/genes/taxon, function/subunit/location
    comments and InterPro crossrefs
  accessed_at: '2026-10-22T04:26:13.044903Z'
  support: supports
  summary: Q9H0R1 is the reviewed Homo sapiens9606 AP5M1 AP5 subunit, with the maintained
    accession/name/gene/status and exact IPR039591 cross-reference. Native function/subunit/location
    comments were read. The Hirst-linked membership and any cytosolic/location annotation
    remain bounded to their cited experiments.
  snapshot_sha256: d600d7c33bdcca4c1527efcd998c894208cc86d259ce0b64158985fb8843000a
- evidence_id: ap45-agent-gene-AP5M1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5M1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned reviewed entry identities and primary/alias gene fields
  accessed_at: '2026-10-22T04:26:13.848606Z'
  support: context_only
  summary: The current exact reviewed AP5M1 query at organism9606 returns one entry,
    Q9H0R1; primary gene and aliases were checked. This confirms current uniqueness,
    not a reconstruction of the historical query.
  snapshot_sha256: 2dfaea9dbf6ef344272f604d7f62de6a27e145c91fe01a5a8f5433f63f474c78
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5M1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: ap45-agent-ipr-IPR029392
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029392/
  locator: Native accession/name/type, complete description, LLM flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T04:26:34.158591Z'
  support: supports
  summary: IPR029392 is type family, named AP-5 complex subunit sigma-1. The complete
    description, member signatures and LLM flags were read to distinguish exact AP5
    subtype families from broader adaptor classes and domains.
  snapshot_sha256: 761eb11d006f3b3da7b2d822e6f90cfcd6ce3a6b5ee11dd15b848a7b68fe7649
- evidence_id: ap45-agent-protein-Q9NUS5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9NUS5.json
  locator: Exact native identity/name/status/genes/taxon, function/subunit/location
    comments and InterPro crossrefs
  accessed_at: '2026-10-22T04:26:13.047261Z'
  support: supports
  summary: Q9NUS5 is the reviewed Homo sapiens9606 AP5S1 AP5 subunit, with the maintained
    accession/name/gene/status and exact IPR029392 cross-reference. Native function/subunit/location
    comments were read. The Hirst-linked membership and any cytosolic/location annotation
    remain bounded to their cited experiments.
  snapshot_sha256: 66fd01cea60ce9fbd64f05f7870b05a0e4c1dadcf6110e97bf7174c332d1b5d3
- evidence_id: ap45-agent-gene-AP5S1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5S1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned reviewed entry identities and primary/alias gene fields
  accessed_at: '2026-10-22T04:26:13.859468Z'
  support: context_only
  summary: The current exact reviewed AP5S1 query at organism9606 returns one entry,
    Q9NUS5; primary gene and aliases were checked. This confirms current uniqueness,
    not a reconstruction of the historical query.
  snapshot_sha256: cff0f5c7bcdcdab9ec7b2441c9b85f18cc968db1dc05ebbe3e6b1fd6f26e555e
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5S1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/ap_5_adaptor_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:25:21Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/ap_5_adaptor_complex.yaml'
  snapshot_sha256: b8c3580e097522bbf7e04c6a76f5e1290cd730c1598da0a07fd9d65a7ee2a246
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/ap_5_adaptor_complex.yaml
    --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/ap_5_adaptor_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:25:22Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/ap_5_adaptor_complex.yaml\
    \ --out /private/tmp/cellstructure-batch45-20261022-mptgrq24/ap_5_adaptor_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch45-20261022-mptgrq24/ap_5_adaptor_complex-strict.tsv"
  snapshot_sha256: b3fac57ef9a3f0c427739c62a5b14269abf4556bf973fc66958a5a005dde9d17
- evidence_id: ap5-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/ap_5_adaptor_complex.yaml
  locator: Complete retained read-only native log
  accessed_at: '2026-10-22T04:26:47.516825Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: ap5-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch45-20261022-mptgrq24/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ap_5_adaptor_complex.yaml
  locator: Complete retained read-only native log
  accessed_at: '2026-10-22T04:26:47.932265Z'
  support: supports
  summary: "data/structures/other/ap_5_adaptor_complex.yaml  (GO:0044599)\n  ap5_adaptor_complex_topology\t\
    ap5_beta5_subunit\tCOVERED\t->ap5_beta5_subunit (UniProtKB:Q2VPB7)\n  ap5_adaptor_complex_topology\t\
    ap5_zeta_subunit\tCOVERED\t->ap5_zeta_subunit (UniProtKB:O43299)\n  ap5_adaptor_complex_topology\t\
    ap5_mu5_subunit\tCOVERED\t->ap5_mu5_subunit (UniProtKB:Q9H0R1)\n  ap5_adaptor_complex_topology\t\
    ap5_sigma5_subunit\tCOVERED\t->ap5_sigma5_subunit (UniProtKB:Q9NUS5)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     4  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     4  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 0ab5a9e877601b5e064d133c6e06c2d902f314b9c485fcf3447af02d79ff9db8
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/ap_5_adaptor_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 10 collected target identifiers returned OK. PMID:20613862: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:22022230:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
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
  topic: Exact AP5 class, synonym and subtype boundary
  outcome: supported
  target_ids:
  - GO:0044599
  summary: The native identifier, four-subunit definition, AP-type is_a parent and
    exact synonym match. The record correctly avoids equating AP5 with a constitutive
    clathrin coat.
  evidence_ids:
  - record
  - ap45-agent-go
  - ap45-agent-hirst2011-meta
  - ap45-agent-hirst2011-xml
  - ap45-agent-pmid-20613862
  - ap45-agent-slabicki2010-xml
- assessment_id: grounding
  area: grounding
  topic: Four exact subtype families are available
  outcome: concern
  target_ids:
  - GO:0044599
  summary: 'All four native entries are family-level AP5-specific identities, not
    domains: ap5_beta5_subunit → InterPro:IPR038741, ap5_zeta_subunit → InterPro:IPR028222,
    ap5_mu5_subunit → InterPro:IPR039591, ap5_sigma5_subunit → InterPro:IPR029392.
    Each is cross-referenced by the matching maintained human protein. Their current
    REVIEWED_LABEL_ONLY status and deferred-CURIE rationale conflict with the exact-family
    contract; no biological membership or accession error is asserted.'
  evidence_ids:
  - record
  - schema
  - curation
  - ap45-agent-family-search-AP5
  - ap45-agent-ipr-IPR038741
  - ap45-agent-ipr-IPR028222
  - ap45-agent-ipr-IPR039591
  - ap45-agent-ipr-IPR029392
  - ap45-agent-protein-Q2VPB7
  - ap45-agent-protein-O43299
  - ap45-agent-protein-Q9H0R1
  - ap45-agent-protein-Q9NUS5
- assessment_id: examples
  area: evidence
  topic: Four verified human examples and exact cited localizations
  outcome: supported
  target_ids:
  - GO:0044599
  summary: All four maintained accession/gene/taxon/status pairs and present single-hit
    query claims are supported. The source gives independent AP5 membership beyond
    the identity-only example notes; O43299 cytoplasmic localization is supported
    by Slabicki rather than inferred from the word AP5. Cytoplasmic versus late-endosomal
    annotation and isoform conditions are kept distinct.
  evidence_ids:
  - record
  - ap45-agent-tax9606
  - ap45-agent-hirst2011-meta
  - ap45-agent-hirst2011-xml
  - ap45-agent-pmid-20613862
  - ap45-agent-slabicki2010-xml
  - ap45-agent-protein-Q2VPB7
  - ap45-agent-protein-O43299
  - ap45-agent-protein-Q9H0R1
  - ap45-agent-protein-Q9NUS5
  - ap45-agent-gene-AP5B1
  - ap45-agent-gene-AP5Z1
  - ap45-agent-gene-AP5M1
  - ap45-agent-gene-AP5S1
- assessment_id: scope
  area: scope
  topic: Human HeLa model and occurrence
  outcome: supported
  target_ids:
  - GO:0044599
  summary: COMMON retains the schema majority-occurrence meaning. Characterization
    of the human complex supports the qualitative organism-level synthesis without
    a population census or evidence that every cell has the same tagged localization.
    HeLaM knockdown/expression conditions support the stated example; no broad universal
    eukaryotic occurrence is inferred.
  evidence_ids:
  - record
  - schema
  - ap45-agent-go
  - ap45-agent-tax9606
  - ap45-agent-hirst2011-meta
  - ap45-agent-hirst2011-xml
  - ap45-agent-pmid-20613862
  - ap45-agent-slabicki2010-xml
- assessment_id: graph
  area: graph
  topic: Cautious endosomal-sorting topology
  outcome: supported
  target_ids:
  - GO:0044599
  summary: Four constituent edges, endosomal association and the is implicated in
    sorting edge match the inspected source scope. The tagged-protein and knockdown
    observations are accurately separated. Perturbed CI-MPR/Vps26 distribution does
    not establish a direct cargo-binding motif or exclusive transport direction; the
    NONMECHANISTIC graph does not claim one.
  evidence_ids:
  - record
  - ap45-agent-go
  - ap45-agent-hirst2011-meta
  - ap45-agent-hirst2011-xml
  - ap45-agent-pmid-20613862
  - ap45-agent-slabicki2010-xml
- assessment_id: formation
  area: evidence
  topic: Supported constituent classes separated from formation necessity
  outcome: unknown
  target_ids:
  - GO:0044599
  summary: The components all retain UNKNOWN essentiality. Observed membership, interaction,
    sorting or invasion phenotypes do not establish universal assembly necessity for
    each individual constituent of these classes. No necessity upgrade is made.
  evidence_ids:
  - record
  - schema
  - ap45-agent-go
  - ap45-agent-hirst2011-meta
  - ap45-agent-hirst2011-xml
  - ap45-agent-pmid-20613862
  - ap45-agent-slabicki2010-xml
- assessment_id: coverage
  area: completeness
  topic: Entire maintained record and evidence placement assessed
  outcome: supported
  target_ids:
  - GO:0044599
  summary: All maintained identity, history, component, example, taxonomic, function,
    graph and discussion fields were inspected. Optional exhaustive accessory-protein,
    taxon or mechanism inventories are not required. No scientific status/history
    promotion or source-quotation insertion is proposed.
  evidence_ids:
  - record
  - ap45-agent-go
  - ap45-agent-hirst2011-meta
  - ap45-agent-hirst2011-xml
  - ap45-agent-pmid-20613862
  - ap45-agent-slabicki2010-xml
findings:
- finding_id: F1
  issue_key: ap5-four-verified-family-groundings-label-only
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the four verified AP5 subunit families
  description: The native family identities ap5_beta5_subunit → InterPro:IPR038741,
    ap5_zeta_subunit → InterPro:IPR028222, ap5_mu5_subunit → InterPro:IPR039591, ap5_sigma5_subunit
    → InterPro:IPR029392 exactly match the four maintained AP5-specific subunit classes
    and their human examples. All four rows instead retain REVIEWED_LABEL_ONLY with
    notes saying no exact CURIE was curated in the earlier pass. The schema and CURATION
    define that status as inability to assert an exact class, not unfinished identifier
    curation.
  target_ids:
  - GO:0044599
  field_paths:
  - components#ap5_beta5_subunit.grounding_status
  - components#ap5_zeta_subunit.grounding_status
  - components#ap5_mu5_subunit.grounding_status
  - components#ap5_sigma5_subunit.grounding_status
  - components#ap5_beta5_subunit.grounding_notes
  - components#ap5_zeta_subunit.grounding_notes
  - components#ap5_mu5_subunit.grounding_notes
  - components#ap5_sigma5_subunit.grounding_notes
  - discussions#resolve_ap5_subunit_groundings
  evidence_ids:
  - record
  - schema
  - curation
  - ap45-agent-family-search-AP5
  - ap45-agent-ipr-IPR038741
  - ap45-agent-ipr-IPR028222
  - ap45-agent-ipr-IPR039591
  - ap45-agent-ipr-IPR029392
  - ap45-agent-protein-Q2VPB7
  - ap45-agent-protein-O43299
  - ap45-agent-protein-Q9H0R1
  - ap45-agent-protein-Q9NUS5
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_5_adaptor_complex.yaml
    role: maintained scientific record
  rule_id: Exact family grounding and reviewed-label-only contract
  native_severity: minor
  normalization_reason: Correct complex, subunit biology and protein examples remain
    intact. Four omitted exact family mappings are a bounded curation gap, not a wrong
    structure or an invitation to substitute partial domains.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0044599
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_5_adaptor_complex.yaml
    role: maintained scientific record
  description: In separately authorized curation, assign ap5_beta5_subunit → InterPro:IPR038741,
    ap5_zeta_subunit → InterPro:IPR028222, ap5_mu5_subunit → InterPro:IPR039591, ap5_sigma5_subunit
    → InterPro:IPR029392, remove incompatible reviewed-label-only status/notes and
    close or update the exact-family TODO. Retain the four components, correct examples,
    UNKNOWN assembly necessity and qualified clathrin/sorting scope.
  acceptance_checks:
  - Each mapped accession resolves to its stated AP5-specific family and matches the
    intended subtype class.
  - The four current human identities and constituent roles remain unchanged; no domain
    or accessory factor replaces a core class.
  - Focused schema/strict, protein and graph checks pass after the authorized scientific
    edit.
limitations:
- The five completed same-base batch26 corpus gates await guarded integration by the
  parent before finalization.
- No image pixels, supplemental files, new sequence alignments or quantitative prevalence
  census were inspected. The individually declared sections, not every downloaded
  article paragraph, define the literature-read scope.
- 'Hirst localization is not an unqualified observation of all native AP5 molecules:
  tagged mu5 required knockdown/damping of diffuse background and sigma5 imaging used
  extraction. The record already distinguishes complex identification from tagged
  localization.'
- The family search is bounded to the recorded InterPro query and four separately
  verified entries. No claim that all possible annotations or accessory-protein inventories
  were surveyed is made. Slabicki historical DNA-repair/putative-helicase wording
  is context only.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes an honest bundle for each uncovered target, including
  clean reviews. Parent owns global-gate integration/finalization; no scientific edits,
  persistence or Git mutation performed.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
