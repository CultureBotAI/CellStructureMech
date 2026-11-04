# Source-grounded review of Isw1b complex

- Review: 20261022T080128Z-isw1b-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:34:44Z
- Finished UTC: 2026-10-22T08:01:28Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No material issue observed. Exact subtype identity, component inventory, yeast reference examples and the explicitly nonmechanistic chromatin-remodeling graph are supported; exact whole-family mappings and universal formation necessity remain unresolved.

## Scope And Provenance

Exactly one complete target and two explicitly frozen neighboring context records; source reading scopes declared individually.

Selection: One complete record in strict-path batch58 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0036437 | data/structures/other/isw1b_complex.yaml | maintained | Isw1b complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0036437 | Focused validator passed. |
| Focused native strict | passed | True | GO:0036437 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0036437 | Focused native check passed; scientific claims assessed separately. |
| Native focused verify | passed | True | GO:0036437 | Focused native check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0036437 | No iModulon-specific claim is assessed. The direct biochemical and genetic source is read instead. |
| Claim-level scientific review | passed | True | GO:0036437 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0036437 | 9 of 11 collected target identifiers returned OK. PMID:12482963: UNREACHABLE; Native Europe PMC uniquely identifies MED12482963: Yeast Isw1p forms two separable complexes in vivo. (2003); DOI 10.1128/mcb.23.1.80-91.2003. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:14562095: UNREACHABLE; Native Europe PMC uniquely identifies MED14562095: Global analysis of protein localization in budding yeast. (2003); DOI 10.1038/nature02026. This resolves the identifier transport residual only; primary-source reading remains separately scoped. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0036437 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0036437 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0036437 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0036437 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0036437 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Generic and two specific Isw1 identities

identity: supported. Targets: GO:0036437.

All three GO identities and parent relations are valid. Vary resolves two separable assemblies and does not support one stable four-subunit complex under the tested conditions. The generic record need not be deleted or assigned a subtype identity.

### Bounded family search leaves existing exact-class tasks unresolved

grounding: supported. Targets: GO:0036437.

Inspected native matches are domains, a broader ATPase superfamily or an empty candidate-subfamily response. They do not supply verified exact whole classes for these constituents. Retaining label-only status is appropriate under this bounded search; no all-database absence is claimed.

### Conditional recovery and universal necessity remain distinct

evidence: unknown. Targets: GO:0036437.

The source reports reciprocal dependence of Ioc2 and Ioc4 for stable Isw1 association. The Isw1b record already states that result. Neither optional copy-number fields nor UNKNOWN essentiality require a finding: recovery, ATPase stimulation and growth effects remain distinct, and the source explicitly allows unstable or condition-specific associations.

### Experimental strain and biochemical assay context

scope: supported. Targets: GO:0036437.

All experimental YTT strains derive from W303 with repaired RAD5; S288C entries are sequence references. COMMON retains its majority-with-exceptions meaning, without a population census. In-vitro comparisons use defined nucleosome substrates and concentrations; stronger Isw1a spacing/sliding does not establish greater activity in every in-vivo context.

### Supported subtype-specific constituent inventory

grounding: supported. Targets: GO:0036437.

The named Isw1/Ioc2/Ioc4 trio matches both the exact GO definition and the directly purified source assembly. Other actors and histone substrates are not promoted to invariant complex subunits.

### Supported nonmechanistic membership and function

graph: supported. Targets: GO:0036437.

Each named constituent and the broad chromatin-remodeling outcome are supported. The graph explicitly declines to resolve substrate recognition or the sliding cycle; it does not require optional detail to be a faithful inventory. ATPase stimulation, DNA binding, nucleosome spacing/sliding and growth/transcription phenotypes remain distinct assays.

### Complete target and explicit neighboring context

completeness: supported. Targets: GO:0036437.

Every target field, citation, component, example, graph edge, discussion and history entry was read. The two sibling context records are frozen inputs, not extra reviewed targets. Optional unpopulated fields are not defects.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/isw1b_complex.yaml; Entire maintained YAML including history and discussions | context_only | The complete target was read; scientific correction remains owned by this maintained YAML. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, PresenceEnum, EssentialityEnum and causal graph scope | context_only | A named protein class is distinct from unrelated alternative constituents. COMMON means present in most members with exceptional losses; unknown formation necessity is not automatically a defect. |
| curation | docs/CURATION.md; Exact structure identity and constituent-class grounding | context_only | A generic complex class and its subtypes can coexist, but component identities and evidence must retain the subtype boundaries. Protein examples do not replace exact class grounding. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Membership versus directed mechanistic claims | context_only | Membership and a whole-complex functional outcome can support a descriptive graph without establishing a resolved causal mechanism. |
| neighbor-isw1_complex | data/structures/other/isw1_complex.yaml; Complete adjacent subtype/supertype record | context_only | The exact frozen neighboring record was read to check subtype boundaries; it is context rather than an additional reviewed target. |
| neighbor-isw1a_complex | data/structures/other/isw1a_complex.yaml; Complete adjacent subtype/supertype record | context_only | The exact frozen neighboring record was read to check subtype boundaries; it is context rather than an additional reviewed target. |
| root58-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006338,GO:0016587,GO:0031010,GO:0036436,GO:0036437; All five identities/status/complete definitions/synonyms and focal subtype typed relationships | supports | The exact generic Isw1, Isw1a, Isw1b, ISWI-type and chromatin-remodeling definitions are distinct. Generic Isw1 has both a and b as is_a children; the definition itself does not state promoter/coding-region specialization or cryptic-transcription suppression. |
| root58-sources-GO0036437-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036437/ancestors?relations=is_a; Complete exact-target is_a-only ancestry | supports | The full is_a ancestry confirms the declared generic or subtype parent, without implying parthood or population frequency. |
| root58-sources-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | Native taxonomy confirms Saccharomyces cerevisiae taxon4932 at species rank. |
| root58-sources-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | Native taxonomy confirms Saccharomyces cerevisiae S288C taxon559292 at strain rank. |
| root58-sources-pmid-12482963 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12482963+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/bibliography/DOI/PMCID and full abstractText | supports | MED12482963: Yeast Isw1p forms two separable complexes in vivo. Vary JC, Gangaraju VK, Qin J, Landel CC, Kooperberg C, Bartholomew B, Tsukiyama T. (2003); DOI10.1128/mcb.23.1.80-91.2003. Native complete abstract was read; no unlisted primary body is claimed. |
| root58-sources-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/bibliography/DOI/PMCID and full abstractText | supports | MED14562095: Global analysis of protein localization in budding yeast. Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK. (2003); DOI10.1038/nature02026. Native complete abstract was read; no unlisted primary body is claimed. |
| root58-sources-doi-10.1128_MCB.23.1.80-91.2003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FMCB.23.1.80-91.2003%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique full bibliographic identity and abstractText | supports | The unique DOI result is Vary2003 MED12482963, Yeast Isw1p forms two separable complexes in vivo, with PMC140669. Complete abstract read. |
| root58-sources-PMC140669-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC140669/; Genuine primary HTML: all Results sec13–sec20, all Discussion sec21, all Methods sec2–sec11 including Table1 and all embedded main Figures1–5 captions. Introduction, Table2 sequence-accession appendix, figure pixels and external/raw datasets not read. | supports | Vary2003 directly separates Isw1–Ioc3 from Isw1–Ioc2–Ioc4 by reciprocal recovery and TAP purification. Ioc2/Ioc4 are mutually dependent for stable association with Isw1. The complexes show comparable nucleosome-stimulated ATPase activity but different substrate-binding, spacing/sliding and genetic-expression effects under the reported conditions. Unstable interactions or other growth conditions remain possible. |
| access-PMC140669-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC140669/; Actual response status/content type and diagnostic body only | context_only | HTTP200 was a browser challenge, not article text. |
| access-PMC140669-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML; Actual response status/content type and diagnostic body only | context_only | The first request failed at local DNS before retrieval; no article text. |
| access-PMC140669-xml-network | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML; Actual response status/content type and diagnostic body only | context_only | The network XML route returned HTTP500 and an error body. |
| access-PMC140669-europepmc | https://europepmc.org/articles/PMC140669; Actual response status/content type and diagnostic body only | context_only | HTTP200 provided a JavaScript page shell rather than the article body. |
| access-vary2003-doi | https://doi.org/10.1128/MCB.23.1.80-91.2003; Actual response status/content type and diagnostic body only | context_only | The publisher DOI route returned HTTP403. |
| access-PMC140669-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC140669/unicode; Actual response status/content type and diagnostic body only | context_only | HTTP200 contained an explicit no-result response rather than article text. |
| access-panther-PTHR45623-SF49 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45623:SF49/; Actual response status/content type and diagnostic body only | context_only | The protein-linked candidate subfamily route returned HTTP204 and no body; it did not establish an exact Isw1-only family. |
| root58-sources-protein-P38144 | https://rest.uniprot.org/uniprotkb/P38144.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY and MISCELLANEOUS comments where present; all InterPro/PANTHER cross-references | supports | P38144 is the reviewed S288C ISW1 reference. Native subunit and localization annotations match the named constituent; the reference strain is not substituted for the W303-derived experimental strains. Nuclear-location source tags were checked directly, without claiming the Huh primary body. |
| root58-sources-gene-ISW1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AISW1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete identity result set and literal query parameters | supports | Exact reviewed ISW1 query in taxon559292 uniquely returns P38144. |
| root58-sources-protein-Q12072 | https://rest.uniprot.org/uniprotkb/Q12072.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY and MISCELLANEOUS comments where present; all InterPro/PANTHER cross-references | supports | Q12072 is the reviewed S288C IOC2 reference. Native subunit and localization annotations match the named constituent; the reference strain is not substituted for the W303-derived experimental strains. Nuclear-location source tags were checked directly, without claiming the Huh primary body. |
| root58-sources-gene-IOC2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIOC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete identity result set and literal query parameters | supports | Exact reviewed IOC2 query in taxon559292 uniquely returns Q12072. |
| root58-sources-protein-Q04213 | https://rest.uniprot.org/uniprotkb/Q04213.json; Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY and MISCELLANEOUS comments where present; all InterPro/PANTHER cross-references | supports | Q04213 is the reviewed S288C IOC4 reference. Native subunit and localization annotations match the named constituent; the reference strain is not substituted for the W303-derived experimental strains. Nuclear-location source tags were checked directly, without claiming the Huh primary body. |
| root58-sources-gene-IOC4 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIOC4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete identity result set and literal query parameters | supports | Exact reviewed IOC4 query in taxon559292 uniquely returns Q04213. |
| root58-sources-ipr-IPR044754 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044754/; Complete native type/name/description including quality flags, integrated signatures and hierarchy | supports | The Isw1/Isw2 N-terminal ATPase domain spans two ATPase paralogs and is a domain, not an exact whole Isw1 family. |
| root58-sources-ipr-IPR038718 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038718/; Complete native type/name/description including quality flags, integrated signatures and hierarchy | supports | SNF2-like N-terminal homologous superfamily is broader than Isw1. |
| root58-sources-ipr-IPR028942 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028942/; Complete native type/name/description including quality flags, integrated signatures and hierarchy | supports | WHIM1 is a domain, not a whole exact Ioc3 family. |
| root58-sources-ipr-IPR035503 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035503/; Complete native type/name/description including quality flags, integrated signatures and hierarchy | supports | IOC4-like PWWP is a domain, not a whole exact Ioc4 family. |
| root58-sources-ipr-IPR062429 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062429/; Complete native type/name/description including quality flags, integrated signatures and hierarchy | supports | IOC2 N-terminal entry is a domain. |
| root58-sources-ipr-IPR062587 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062587/; Complete native type/name/description including quality flags, integrated signatures and hierarchy | supports | IOC2 middle-region entry is a domain. |
| root58-sources-ipr-IPR063422 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063422/; Complete native type/name/description including quality flags, integrated signatures and hierarchy | supports | IOC2 C-terminal entry is a domain. |
| schema-result | just validate data/structures/other/isw1b_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/isw1b_complex.yaml |
| strict-result | just validate-strict data/structures/other/isw1b_complex.yaml --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/isw1b_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/isw1b_complex.yaml --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/isw1b_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/isw1b_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml --causal-graphs; Complete focused native report | supports | data/structures/other/isw1b_complex.yaml  (GO:0036437)<br>  yeast_isw1b_chromatin_remodeling	isw1_isw1b_atpase_subunit	COVERED	-&gt;isw1_isw1b_atpase_subunit (UniProtKB:P38144)<br>  yeast_isw1b_chromatin_remodeling	ioc2_isw1b_subunit	COVERED	-&gt;ioc2_isw1b_subunit (UniProtKB:Q12072)<br>  yeast_isw1b_chromatin_remodeling	ioc4_isw1b_subunit	COVERED	-&gt;ioc4_isw1b_subunit (UniProtKB:Q04213)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml --verify; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/isw1b_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 11 collected target identifiers returned OK. PMID:12482963: UNREACHABLE; Native Europe PMC uniquely identifies MED12482963: Yeast Isw1p forms two separable complexes in vivo. (2003); DOI 10.1128/mcb.23.1.80-91.2003. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:14562095: UNREACHABLE; Native Europe PMC uniquely identifies MED14562095: Global analysis of protein localization in budding yeast. (2003); DOI 10.1038/nature02026. This resolves the identifier transport residual only; primary-source reading remains separately scoped. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five same-base batch26 corpus gates and exact target resolver rows are integrated with every manifested input hash verified.
- Vary Methods/Results/Discussion and embedded main captions were read; no figure pixels, external expression arrays, raw measurements, sequence alignments or Table2 accession appendix were independently inspected.
- Huh2003 is verified at native full-abstract tier and matching UniProt annotation-provenance tier; its primary-body localization assays were not independently rechecked.
- Native family checking is bounded to the retained entries; unresolved exact-class grounding is not an exhaustive database absence claim.
- Reference S288C proteins are not the W303-derived assay strains. No universal formation profile, fixed stoichiometric measurement or population census is inferred from recovery and activity assays.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes both issue-bearing and qualified clean observations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T080128Z-isw1b-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of Isw1b complex
started_at: '2026-10-22T07:34:44Z'
finished_at: '2026-10-22T08:01:28Z'
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
summary: No material issue observed. Exact subtype identity, component inventory,
  yeast reference examples and the explicitly nonmechanistic chromatin-remodeling
  graph are supported; exact whole-family mappings and universal formation necessity
  remain unresolved.
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
  - path: data/structures/other/isw1_complex.yaml
    sha256: 5662405c6e9c5ce9d246c4ea52175ca1cce9eee337ac704e5cb405e66f0ce912
    role: context
  - path: data/structures/other/isw1a_complex.yaml
    sha256: 1f8db379fbf44a20126d11fe7418076ec4361066f6564871614361ad31273865
    role: context
  - path: data/structures/other/isw1b_complex.yaml
    sha256: da27a6000afe1a8e535d8586b2841416d6f10e07058b226e446d785541c37137
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
- target_id: GO:0036437
  path: data/structures/other/isw1b_complex.yaml
  label: Isw1b complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/isw1b_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target and two explicitly frozen neighboring context
    records; source reading scopes declared individually.
  selection: One complete record in strict-path batch58 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0036437
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: just validate data/structures/other/isw1b_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: just validate-strict data/structures/other/isw1b_complex.yaml --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/isw1b_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0036437
  summary: No iModulon-specific claim is assessed. The direct biochemical and genetic
    source is read instead.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0036437
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - neighbor-isw1_complex
  - neighbor-isw1a_complex
  - root58-sources-go
  - root58-sources-GO0036437-ancestors
  - root58-sources-tax-4932
  - root58-sources-tax-559292
  - root58-sources-pmid-12482963
  - root58-sources-pmid-14562095
  - root58-sources-doi-10.1128_MCB.23.1.80-91.2003
  - root58-sources-PMC140669-legacy
  - access-PMC140669-html
  - access-PMC140669-xml
  - access-PMC140669-xml-network
  - access-PMC140669-europepmc
  - access-vary2003-doi
  - access-PMC140669-bioc
  - access-panther-PTHR45623-SF49
  - root58-sources-protein-P38144
  - root58-sources-gene-ISW1
  - root58-sources-protein-Q12072
  - root58-sources-gene-IOC2
  - root58-sources-protein-Q04213
  - root58-sources-gene-IOC4
  - root58-sources-ipr-IPR044754
  - root58-sources-ipr-IPR038718
  - root58-sources-ipr-IPR028942
  - root58-sources-ipr-IPR035503
  - root58-sources-ipr-IPR062429
  - root58-sources-ipr-IPR062587
  - root58-sources-ipr-IPR063422
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0036437
  summary: '9 of 11 collected target identifiers returned OK. PMID:12482963: UNREACHABLE;
    Native Europe PMC uniquely identifies MED12482963: Yeast Isw1p forms two separable
    complexes in vivo. (2003); DOI 10.1128/mcb.23.1.80-91.2003. This resolves the
    identifier transport residual only; primary-source reading remains separately
    scoped.; PMID:14562095: UNREACHABLE; Native Europe PMC uniquely identifies MED14562095:
    Global analysis of protein localization in budding yeast. (2003); DOI 10.1038/nature02026.
    This resolves the identifier transport residual only; primary-source reading remains
    separately scoped. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root58-sources-pmid-12482963
  - root58-sources-pmid-14562095
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch58 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch58 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch58 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch58 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0036437
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
    and current batch58 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/isw1b_complex.yaml
  locator: Entire maintained YAML including history and discussions
  accessed_at: '2026-10-22T07:38:50Z'
  support: context_only
  summary: The complete target was read; scientific correction remains owned by this
    maintained YAML.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, PresenceEnum, EssentialityEnum and causal graph scope
  accessed_at: '2026-10-22T07:38:50Z'
  support: context_only
  summary: A named protein class is distinct from unrelated alternative constituents.
    COMMON means present in most members with exceptional losses; unknown formation
    necessity is not automatically a defect.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact structure identity and constituent-class grounding
  accessed_at: '2026-10-22T07:38:50Z'
  support: context_only
  summary: A generic complex class and its subtypes can coexist, but component identities
    and evidence must retain the subtype boundaries. Protein examples do not replace
    exact class grounding.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Membership versus directed mechanistic claims
  accessed_at: '2026-10-22T07:38:50Z'
  support: context_only
  summary: Membership and a whole-complex functional outcome can support a descriptive
    graph without establishing a resolved causal mechanism.
- evidence_id: neighbor-isw1_complex
  kind: record_content
  reference: data/structures/other/isw1_complex.yaml
  locator: Complete adjacent subtype/supertype record
  accessed_at: '2026-10-22T07:38:50Z'
  support: context_only
  summary: The exact frozen neighboring record was read to check subtype boundaries;
    it is context rather than an additional reviewed target.
- evidence_id: neighbor-isw1a_complex
  kind: record_content
  reference: data/structures/other/isw1a_complex.yaml
  locator: Complete adjacent subtype/supertype record
  accessed_at: '2026-10-22T07:38:50Z'
  support: context_only
  summary: The exact frozen neighboring record was read to check subtype boundaries;
    it is context rather than an additional reviewed target.
- evidence_id: root58-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006338,GO:0016587,GO:0031010,GO:0036436,GO:0036437
  locator: All five identities/status/complete definitions/synonyms and focal subtype
    typed relationships
  accessed_at: '2026-10-22T07:24:24.396129Z'
  support: supports
  summary: The exact generic Isw1, Isw1a, Isw1b, ISWI-type and chromatin-remodeling
    definitions are distinct. Generic Isw1 has both a and b as is_a children; the
    definition itself does not state promoter/coding-region specialization or cryptic-transcription
    suppression.
  snapshot_sha256: 2951cfdac67bb29244b8035f970f155885d77e41f0d93b05bf3907cd268843ce
- evidence_id: root58-sources-GO0036437-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036437/ancestors?relations=is_a
  locator: Complete exact-target is_a-only ancestry
  accessed_at: '2026-10-22T07:24:28.318252Z'
  support: supports
  summary: The full is_a ancestry confirms the declared generic or subtype parent,
    without implying parthood or population frequency.
  snapshot_sha256: e4da0c42c3c80f09c12136df991e0b4f73e6e91e5e07d2f9de9f8a9c1aad7c42
- evidence_id: root58-sources-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T07:24:24.396444Z'
  support: supports
  summary: Native taxonomy confirms Saccharomyces cerevisiae taxon4932 at species
    rank.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: root58-sources-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T07:24:25.012692Z'
  support: supports
  summary: Native taxonomy confirms Saccharomyces cerevisiae S288C taxon559292 at
    strain rank.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root58-sources-pmid-12482963
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12482963+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/bibliography/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:24:26.636221Z'
  support: supports
  summary: 'MED12482963: Yeast Isw1p forms two separable complexes in vivo. Vary JC,
    Gangaraju VK, Qin J, Landel CC, Kooperberg C, Bartholomew B, Tsukiyama T. (2003);
    DOI10.1128/mcb.23.1.80-91.2003. Native complete abstract was read; no unlisted
    primary body is claimed.'
  snapshot_sha256: 58b6f17bd9124bed0e4a98f6e77ad36e24272cd95bb76621ac6e83bbef579c0e
- evidence_id: root58-sources-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/bibliography/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:24:27.002243Z'
  support: supports
  summary: 'MED14562095: Global analysis of protein localization in budding yeast.
    Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea EK. (2003);
    DOI10.1038/nature02026. Native complete abstract was read; no unlisted primary
    body is claimed.'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: root58-sources-doi-10.1128_MCB.23.1.80-91.2003
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FMCB.23.1.80-91.2003%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique full bibliographic identity and abstractText
  accessed_at: '2026-10-22T07:24:27.258320Z'
  support: supports
  summary: The unique DOI result is Vary2003 MED12482963, Yeast Isw1p forms two separable
    complexes in vivo, with PMC140669. Complete abstract read.
  snapshot_sha256: 94962844c1a017ea709b27a7c144524c453a4db7d3de6ab46939550fe90c57b8
- evidence_id: root58-sources-PMC140669-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC140669/
  locator: 'Genuine primary HTML: all Results sec13–sec20, all Discussion sec21, all
    Methods sec2–sec11 including Table1 and all embedded main Figures1–5 captions.
    Introduction, Table2 sequence-accession appendix, figure pixels and external/raw
    datasets not read.'
  accessed_at: '2026-10-22T07:31:06.007816Z'
  support: supports
  summary: Vary2003 directly separates Isw1–Ioc3 from Isw1–Ioc2–Ioc4 by reciprocal
    recovery and TAP purification. Ioc2/Ioc4 are mutually dependent for stable association
    with Isw1. The complexes show comparable nucleosome-stimulated ATPase activity
    but different substrate-binding, spacing/sliding and genetic-expression effects
    under the reported conditions. Unstable interactions or other growth conditions
    remain possible.
  snapshot_sha256: 291bd152549f0127f25ad49bd67de196e85f1776f010ef99b8867a7660bb598c
- evidence_id: access-PMC140669-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC140669/
  locator: Actual response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:25:29.713982Z'
  support: context_only
  summary: HTTP200 was a browser challenge, not article text.
  snapshot_sha256: 3e1c2bfa98a2b59ecb5d8523bf933eea4f98364160ef0f5a7692e75aa9b91e9b
- evidence_id: access-PMC140669-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML
  locator: Actual response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:29:49.530643Z'
  support: context_only
  summary: The first request failed at local DNS before retrieval; no article text.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: access-PMC140669-xml-network
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML
  locator: Actual response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:30:16.724232Z'
  support: context_only
  summary: The network XML route returned HTTP500 and an error body.
  snapshot_sha256: cd338236e7d267bf72bd57f3bd5bb62c39adda0451ca46dea4890f637dcf7e96
- evidence_id: access-PMC140669-europepmc
  kind: primary_source
  reference: https://europepmc.org/articles/PMC140669
  locator: Actual response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:30:32.454249Z'
  support: context_only
  summary: HTTP200 provided a JavaScript page shell rather than the article body.
  snapshot_sha256: db7e4f3351ac6a45e2475e25054e247d557083db08daaa07104d0375e3744b6d
- evidence_id: access-vary2003-doi
  kind: primary_source
  reference: https://doi.org/10.1128/MCB.23.1.80-91.2003
  locator: Actual response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:30:32.454024Z'
  support: context_only
  summary: The publisher DOI route returned HTTP403.
  snapshot_sha256: 75b4ca6429c083e85d882dbf8074a4bc357d2b57e479643e830499e16da8ef8d
- evidence_id: access-PMC140669-bioc
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC140669/unicode
  locator: Actual response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:31:06.007594Z'
  support: context_only
  summary: HTTP200 contained an explicit no-result response rather than article text.
  snapshot_sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
- evidence_id: access-panther-PTHR45623-SF49
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45623:SF49/
  locator: Actual response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:25:29.884732Z'
  support: context_only
  summary: The protein-linked candidate subfamily route returned HTTP204 and no body;
    it did not establish an exact Isw1-only family.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: root58-sources-protein-P38144
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38144.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY and MISCELLANEOUS comments where present; all
    InterPro/PANTHER cross-references
  accessed_at: '2026-10-22T07:24:25.034640Z'
  support: supports
  summary: P38144 is the reviewed S288C ISW1 reference. Native subunit and localization
    annotations match the named constituent; the reference strain is not substituted
    for the W303-derived experimental strains. Nuclear-location source tags were checked
    directly, without claiming the Huh primary body.
  snapshot_sha256: bbf8ea6564b1a0aeb6b66ba4f0449ebf54b36b780e36dc504e4c88293889256e
- evidence_id: root58-sources-gene-ISW1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AISW1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete identity result set and literal query parameters
  accessed_at: '2026-10-22T07:24:28.613425Z'
  support: supports
  summary: Exact reviewed ISW1 query in taxon559292 uniquely returns P38144.
  snapshot_sha256: 775233aac5f6c5e13fc0a73ff73d13b9055f2c9fc8c8ccf000d4373501cb662f
- evidence_id: root58-sources-protein-Q12072
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12072.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY and MISCELLANEOUS comments where present; all
    InterPro/PANTHER cross-references
  accessed_at: '2026-10-22T07:24:26.344999Z'
  support: supports
  summary: Q12072 is the reviewed S288C IOC2 reference. Native subunit and localization
    annotations match the named constituent; the reference strain is not substituted
    for the W303-derived experimental strains. Nuclear-location source tags were checked
    directly, without claiming the Huh primary body.
  snapshot_sha256: 4035abf4ee6da474aae5a55ddcd7f7f0ed4d671a7f51aa4e597c8d74ac33f885
- evidence_id: root58-sources-gene-IOC2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIOC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete identity result set and literal query parameters
  accessed_at: '2026-10-22T07:24:29.619630Z'
  support: supports
  summary: Exact reviewed IOC2 query in taxon559292 uniquely returns Q12072.
  snapshot_sha256: 608a84c396b8605bceb1199ad71f40482f9f036bf6b9ac8056febf4dfca0f2c8
- evidence_id: root58-sources-protein-Q04213
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04213.json
  locator: Native identity/status/names/genes/organism; complete FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY and MISCELLANEOUS comments where present; all
    InterPro/PANTHER cross-references
  accessed_at: '2026-10-22T07:24:25.899373Z'
  support: supports
  summary: Q04213 is the reviewed S288C IOC4 reference. Native subunit and localization
    annotations match the named constituent; the reference strain is not substituted
    for the W303-derived experimental strains. Nuclear-location source tags were checked
    directly, without claiming the Huh primary body.
  snapshot_sha256: 05f67a4b4a1047320b071cf91045b4b153e9b88c4ae7e95a845ca6fed97441c4
- evidence_id: root58-sources-gene-IOC4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIOC4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete identity result set and literal query parameters
  accessed_at: '2026-10-22T07:24:29.762930Z'
  support: supports
  summary: Exact reviewed IOC4 query in taxon559292 uniquely returns Q04213.
  snapshot_sha256: 4656f8fb3cc23c0748c260dd404667148c4bbb98c891e8d265cb09dcfbaab074
- evidence_id: root58-sources-ipr-IPR044754
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044754/
  locator: Complete native type/name/description including quality flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:25:27.809165Z'
  support: supports
  summary: The Isw1/Isw2 N-terminal ATPase domain spans two ATPase paralogs and is
    a domain, not an exact whole Isw1 family.
  snapshot_sha256: 061068d91ce4e280dc97c8d9a97b780be29b8b80f8c5df5475c0f0511e87bf06
- evidence_id: root58-sources-ipr-IPR038718
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038718/
  locator: Complete native type/name/description including quality flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:25:29.648892Z'
  support: supports
  summary: SNF2-like N-terminal homologous superfamily is broader than Isw1.
  snapshot_sha256: 4ea00d2c09f5089e771ef955d3066039ffbdca88d870d85de0109600aa99e155
- evidence_id: root58-sources-ipr-IPR028942
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028942/
  locator: Complete native type/name/description including quality flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:25:27.809536Z'
  support: supports
  summary: WHIM1 is a domain, not a whole exact Ioc3 family.
  snapshot_sha256: 91d266cd2f819b65c0636857bebd436de01d5f733d51a68a873c3c8b8bb07776
- evidence_id: root58-sources-ipr-IPR035503
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035503/
  locator: Complete native type/name/description including quality flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:25:28.433639Z'
  support: supports
  summary: IOC4-like PWWP is a domain, not a whole exact Ioc4 family.
  snapshot_sha256: 2be8ebb80d6bf3d9e6dfe5093f4324782c533a9bec6c5abe0e44cf0a8a9d7d45
- evidence_id: root58-sources-ipr-IPR062429
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062429/
  locator: Complete native type/name/description including quality flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:25:29.058980Z'
  support: supports
  summary: IOC2 N-terminal entry is a domain.
  snapshot_sha256: 131a1fdb8dfebcd5880e3ed5368994aa658dd9b68d55d27fd89c9f2356c1ca22
- evidence_id: root58-sources-ipr-IPR062587
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062587/
  locator: Complete native type/name/description including quality flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:25:29.048704Z'
  support: supports
  summary: IOC2 middle-region entry is a domain.
  snapshot_sha256: 41efdf3fd1268876253e8db2213e55abd8dc6495513a3be0d695760d7b9da214
- evidence_id: root58-sources-ipr-IPR063422
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063422/
  locator: Complete native type/name/description including quality flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:25:28.451814Z'
  support: supports
  summary: IOC2 C-terminal entry is a domain.
  snapshot_sha256: f653a487609cb242e843fd92c5219bf5ffedd7820a8504913421f7e5f1393787
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/isw1b_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:34:45Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/isw1b_complex.yaml'
  snapshot_sha256: 6ea2ef50cf1fb6d16edf33ffcabf74bf961ad0fa3860be958065d0a384276fad
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/isw1b_complex.yaml --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/isw1b_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:34:46Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/isw1b_complex.yaml\
    \ --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/isw1b_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/isw1b_complex-strict.tsv"
  snapshot_sha256: b3199bb41efc5a2d16fb205c3a7ac9168a021f150243b2cfa0e21ceec636e3d6
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml
    --causal-graphs
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:36:14.179670Z'
  support: supports
  summary: "data/structures/other/isw1b_complex.yaml  (GO:0036437)\n  yeast_isw1b_chromatin_remodeling\t\
    isw1_isw1b_atpase_subunit\tCOVERED\t->isw1_isw1b_atpase_subunit (UniProtKB:P38144)\n\
    \  yeast_isw1b_chromatin_remodeling\tioc2_isw1b_subunit\tCOVERED\t->ioc2_isw1b_subunit\
    \ (UniProtKB:Q12072)\n  yeast_isw1b_chromatin_remodeling\tioc4_isw1b_subunit\t\
    COVERED\t->ioc4_isw1b_subunit (UniProtKB:Q04213)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     3  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     3  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 0c0bce6fe667636f6e9cc1ecdfdf7e8f0a431f04d7dfc7da15f0cda90ac6517d
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml
    --verify
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:36:15.285211Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/isw1b_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '9 of 11 collected target identifiers returned OK. PMID:12482963: UNREACHABLE;
    Native Europe PMC uniquely identifies MED12482963: Yeast Isw1p forms two separable
    complexes in vivo. (2003); DOI 10.1128/mcb.23.1.80-91.2003. This resolves the
    identifier transport residual only; primary-source reading remains separately
    scoped.; PMID:14562095: UNREACHABLE; Native Europe PMC uniquely identifies MED14562095:
    Global analysis of protein localization in budding yeast. (2003); DOI 10.1038/nature02026.
    This resolves the identifier transport residual only; primary-source reading remains
    separately scoped. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
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
  topic: Generic and two specific Isw1 identities
  outcome: supported
  target_ids:
  - GO:0036437
  summary: All three GO identities and parent relations are valid. Vary resolves two
    separable assemblies and does not support one stable four-subunit complex under
    the tested conditions. The generic record need not be deleted or assigned a subtype
    identity.
  evidence_ids:
  - record
  - curation
  - root58-sources-go
  - root58-sources-GO0036437-ancestors
  - root58-sources-PMC140669-legacy
- assessment_id: family-grounding
  area: grounding
  topic: Bounded family search leaves existing exact-class tasks unresolved
  outcome: supported
  target_ids:
  - GO:0036437
  summary: Inspected native matches are domains, a broader ATPase superfamily or an
    empty candidate-subfamily response. They do not supply verified exact whole classes
    for these constituents. Retaining label-only status is appropriate under this
    bounded search; no all-database absence is claimed.
  evidence_ids:
  - record
  - curation
  - root58-sources-ipr-IPR044754
  - root58-sources-ipr-IPR038718
  - root58-sources-ipr-IPR028942
  - root58-sources-ipr-IPR035503
  - root58-sources-ipr-IPR062429
  - root58-sources-ipr-IPR062587
  - root58-sources-ipr-IPR063422
  - root58-sources-protein-P38144
  - root58-sources-protein-Q12072
  - root58-sources-protein-Q04213
  - root58-sources-gene-ISW1
  - root58-sources-gene-IOC2
  - root58-sources-gene-IOC4
- assessment_id: formation
  area: evidence
  topic: Conditional recovery and universal necessity remain distinct
  outcome: unknown
  target_ids:
  - GO:0036437
  summary: 'The source reports reciprocal dependence of Ioc2 and Ioc4 for stable Isw1
    association. The Isw1b record already states that result. Neither optional copy-number
    fields nor UNKNOWN essentiality require a finding: recovery, ATPase stimulation
    and growth effects remain distinct, and the source explicitly allows unstable
    or condition-specific associations.'
  evidence_ids:
  - record
  - schema
  - root58-sources-PMC140669-legacy
- assessment_id: scope
  area: scope
  topic: Experimental strain and biochemical assay context
  outcome: supported
  target_ids:
  - GO:0036437
  summary: All experimental YTT strains derive from W303 with repaired RAD5; S288C
    entries are sequence references. COMMON retains its majority-with-exceptions meaning,
    without a population census. In-vitro comparisons use defined nucleosome substrates
    and concentrations; stronger Isw1a spacing/sliding does not establish greater
    activity in every in-vivo context.
  evidence_ids:
  - record
  - schema
  - root58-sources-PMC140669-legacy
  - root58-sources-tax-4932
  - root58-sources-tax-559292
  - root58-sources-protein-P38144
  - root58-sources-protein-Q12072
  - root58-sources-protein-Q04213
- assessment_id: composition
  area: grounding
  topic: Supported subtype-specific constituent inventory
  outcome: supported
  target_ids:
  - GO:0036437
  summary: The named Isw1/Ioc2/Ioc4 trio matches both the exact GO definition and
    the directly purified source assembly. Other actors and histone substrates are
    not promoted to invariant complex subunits.
  evidence_ids:
  - record
  - curation
  - root58-sources-go
  - root58-sources-PMC140669-legacy
  - root58-sources-protein-P38144
  - root58-sources-protein-Q12072
  - root58-sources-protein-Q04213
  - root58-sources-gene-ISW1
  - root58-sources-gene-IOC2
  - root58-sources-gene-IOC4
- assessment_id: graph
  area: graph
  topic: Supported nonmechanistic membership and function
  outcome: supported
  target_ids:
  - GO:0036437
  summary: Each named constituent and the broad chromatin-remodeling outcome are supported.
    The graph explicitly declines to resolve substrate recognition or the sliding
    cycle; it does not require optional detail to be a faithful inventory. ATPase
    stimulation, DNA binding, nucleosome spacing/sliding and growth/transcription
    phenotypes remain distinct assays.
  evidence_ids:
  - record
  - graphs
  - root58-sources-go
  - root58-sources-PMC140669-legacy
- assessment_id: coverage
  area: completeness
  topic: Complete target and explicit neighboring context
  outcome: supported
  target_ids:
  - GO:0036437
  summary: Every target field, citation, component, example, graph edge, discussion
    and history entry was read. The two sibling context records are frozen inputs,
    not extra reviewed targets. Optional unpopulated fields are not defects.
  evidence_ids:
  - record
  - schema
  - curation
  - root58-sources-go
  - root58-sources-doi-10.1128_MCB.23.1.80-91.2003
findings: []
actions: []
limitations:
- All five same-base batch26 corpus gates and exact target resolver rows are integrated
  with every manifested input hash verified.
- Vary Methods/Results/Discussion and embedded main captions were read; no figure
  pixels, external expression arrays, raw measurements, sequence alignments or Table2
  accession appendix were independently inspected.
- Huh2003 is verified at native full-abstract tier and matching UniProt annotation-provenance
  tier; its primary-body localization assays were not independently rechecked.
- Native family checking is bounded to the retained entries; unresolved exact-class
  grounding is not an exhaustive database absence claim.
- Reference S288C proteins are not the W303-derived assay strains. No universal formation
  profile, fixed stoichiometric measurement or population census is inferred from
  recovery and activity assays.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes both issue-bearing and qualified clean observations.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
