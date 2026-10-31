# Lysp100 associated nuclear domain scientific review

- Review: 20261022T080132Z-lysp100-associated-nuclear-domain-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:34:53Z
- Finished UTC: 2026-10-22T08:01:32Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

LAND identity, SP140 isoform distinctions and the qualified redistribution/reporter context are supported. Broader family candidates and prevalence/formation uncertainties are explicit; no concrete actionable defect was established.

## Scope And Provenance

Exactly one complete maintained target plus frozen guidance and protein-example skill. Actual source-reading extents appear per evidence row; no unlisted primary experiments or assets are certified.

Selection: Target 8 of batch58, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0016606 | data/structures/other/lysp100_associated_nuclear_domain.yaml | maintained | LYSP100-associated nuclear domain |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0016606 | Focused validator passed. |
| Focused native strict | passed | True | GO:0016606 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0016606 | Native focused check passed; biological claims assessed separately. |
| Native verify | passed | True | GO:0016606 | Native focused check passed; biological claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0016606 | No expression-module inference is used. |
| Claim-level scientific review | passed | True | GO:0016606 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0016606 | 8 of 11 collected target identifiers returned OK. PMID:25593309: UNREACHABLE; Native Europe PMC uniquely identifies MED25593309: Screen identifies bromodomain protein ZMYND8 in chromatin recognition of transcription-associated DNA damage that promotes homologous recombination. (2015); DOI 10.1101/gad.252189.114. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:8695863: UNREACHABLE; Native Europe PMC uniquely identifies MED8695863: LYSP100-associated nuclear domains (LANDs): description of a new class of subnuclear structures and their relationship to PML nuclear bodies. (1996); DOI 10.1182/blood.v88.4.1423.bloodjournal8841423. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:8910577: UNREACHABLE; Native Europe PMC uniquely identifies MED8910577: Identification and characterization of a leukocyte-specific component of the nuclear body. (1996); DOI 10.1074/jbc.271.46.29198. This resolves the identifier transport residual only; primary-source reading remains separately scoped. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0016606 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0016606 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0016606 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0016606 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0016606 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### LAND morphology and isoform boundary

identity: supported. Targets: GO:0016606.

Exact GO morphology/location and native Q13342 SP140 identity agree. Native isoforms distinguish LYSp100-B from A and other forms; Q99856 is a correct human ARID3A/Bright identity used as external regulatory context, not a required LAND constituent.

### No forced broader family mapping

grounding: supported. Targets: GO:0016606.

The inspected SP110/SP140/SP140L and PANTHER membership sets are broader than the retained LYSp100B class; the bromodomain is only a domain. The acknowledged isoform-specific label-only boundary is justified at this inspection scope.

### Qualified overexpression redistribution and reporter context

graph: supported. Targets: GO:0016606.

The explicitly NONMECHANISTIC graph and evidence preserve in-vitro association, redistribution and reporter coactivation rather than asserting endogenous universal assembly causality. The observed HeLa/J558 preparations do not establish every species-specific Bright construct equivalence.

### Taxonomic frequency versus cell-type observations

scope: unknown. Targets: GO:0016606.

Human native protein identity and characterized lymphoid-associated bodies are established. VARIABLE retains lineage/strain-level patchiness meaning; cell-type expression and transfection-dependent visibility do not by themselves measure that frequency. This remains an explicit uncertainty, not a redefinition of the enum or a claim of ubiquitous LANDs.

### Unresolved individual formation necessity

grounding: unknown. Targets: GO:0016606.

UNKNOWN is appropriate: enrichment and redistribution do not establish that LANDs cannot form without the isoform or regulator. The proposed model is not a universal omission assay.

### Whole maintained target and declared source coverage

completeness: supported. Targets: GO:0016606.

Every maintained field, source note, graph and discussion was inspected at the declared extents. Optional inventory/contact enrichment and acknowledged unknowns alone do not create findings.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/lysp100_associated_nuclear_domain.yaml; Entire maintained record, all examples, evidence, graphs, properties, images, history and discussions | context_only | Every maintained field was read. Historical curation statements are context, not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component/ProteinExample, EssentialityEnum, PresenceEnum and graph-scope contracts | context_only | Formation necessity differs from function, viability and membership. COMMON means most members with losses the exception; VARIABLE means lineage- or strain-level patchiness, not cell-type-specific visibility. |
| curation | docs/CURATION.md; Component grounding and REVIEWED_LABEL_ONLY at159–160 | context_only | Exact full-family mappings differ from shared domains or broader paralog classes. Label-only is not merely uncurated in this pass. |
| complex58-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004176,GO:0005743,GO:0005745,GO:0008559,GO:0016604,GO:0016605,GO:0016606,GO:0031981,GO:0034982,GO:0043190,GO:0044874,GO:0098800,GO:0140306,GO:1905368,GO:1990195,GO:1990196; Complete target-relevant definitions/synonyms and typed relationships; unrelated combined entries not attributed to this target | supports | GO0016606 defines the LYSP100-associated globular electron-dense nuclear domain, distinct from annular PML bodies. GO0016604 and0031981 distinguish the nuclear-body parent and lumen location. |
| complex58-agent-go-0016606-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016606/ancestors?relations=is_a; Complete is_a-only ancestor response | supports | The is_a-only closure includes the maintained parent class or classes. It establishes classification, not parthood, experimental assembly necessity or prevalence. |
| complex58-agent-tax-9606 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9606; Complete ENA identity/names/lineage | supports | Taxon9606: Homo sapiens, rank species; exact native names and lineage inspected. |
| complex58-agent-protein-Q13342 | https://rest.uniprot.org/uniprotkb/Q13342.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): Q13342, Nuclear body protein SP140; primary genes SP140, synonyms LYSP100, taxon9606. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex58-agent-protein-Q99856 | https://rest.uniprot.org/uniprotkb/Q99856.json; Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity comments and family cross-references | supports | UniProtKB reviewed (Swiss-Prot): Q99856, AT-rich interactive domain-containing protein 3A; primary genes ARID3A, synonyms DRIL1, DRIL3, DRX, E2FBP1, taxon9606. Its own native comments and family cross-references were inspected with their original evidence qualifiers. |
| complex58-agent-query-SP140 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASP140%29+AND+%28taxonomy_id%3A9606%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete query results | supports | Exact native query returns 1 entry: Q13342. Every returned identity/gene/organism was read. |
| complex58-agent-pmid-25593309 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25593309+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and available abstract | supports | MED25593309: Screen identifies bromodomain protein ZMYND8 in chromatin recognition of transcription-associated DNA damage that promotes homologous recombination. Gong F, Chiu LY, Cox B, Aymard F, Clouaire T, Leung JW, Cammarata M, Perez M, Agarwal P, Brodbelt JS, Legube G, Miller KM. (2015), DOI10.1101/gad.252189.114. Exact metadata and complete available abstract read; this does not claim body access.  |
| complex58-agent-pmid-8695863 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8695863+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and available abstract | supports | MED8695863: LYSP100-associated nuclear domains (LANDs): description of a new class of subnuclear structures and their relationship to PML nuclear bodies. Dent AL, Yewdell J, Puvion-Dutilleul F, Koken MH, de The H, Staudt LM. (1996), DOI10.1182/blood.v88.4.1423.bloodjournal8841423. Exact metadata and complete available abstract read; this does not claim body access.  |
| complex58-agent-pmid-8910577 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8910577+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and available abstract | supports | MED8910577: Identification and characterization of a leukocyte-specific component of the nuclear body. Bloch DB, de la Monte SM, Guigaouri P, Filippov A, Bloch KD. (1996), DOI10.1074/jbc.271.46.29198. Exact metadata and complete available abstract read; this does not claim body access.  |
| complex58-agent-doi-10.1093_emboj_19.15.4123 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1093%2Femboj%2F19.15.4123%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identity and abstract | supports | Exact native DOI/MED identity: Regulation of matrix attachment region-dependent, lymphocyte-restricted transcription through differential localization within promyelocytic leukemia nuclear bodies. Zong RT, Das C, Tucker PW. (2000), PMID10921892. Complete available abstract read. |
| complex58-agent-PMC306587-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC306587/; Complete Introduction sec1; Results sec3/4/6/10/11; Discussion sec12; Methods sec14/15/17, with embedded captions read. No figure pixels. | supports | Zong/Das/Tucker2000 distinguishes Bright–Sp100 from weaker Bright–LYSp100B interactions, overexpression-associated LYSp100B redistribution and IgH-enhancer reporter activation. In-vitro binding is not converted into a demonstrated cellular LYSp100B–Bright co-immunoprecipitation. J558 and HeLa experiments and the proposed LAND-disruption model are distinct. |
| complex58-agent-ipr-IPR043563 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR043563/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | SP110/SP140/SP140L is a broader full-family class, not a specific LYSp100B isoform family. |
| complex58-agent-ipr-IPR030411 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030411/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | The SP140 bromodomain entry describes a domain rather than the complete retained isoform. |
| complex58-agent-panther-PTHR46386 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR46386/; Native name/type, description and curation flags/signatures; example membership is independently supplied by UniProt | supports | The native PANTHER entry is labeled SP140 family; its name alone does not establish exclusivity of the retained isoform. |
| complex58-agent-panther-SP140-members | https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/panther/PTHR46386/?page_size=100; Every returned accession/protein/gene identity in the complete reviewed-member query | supports | All12 reviewed returned identities include SP100,SP110,SP140L and AIRE alongside SP140, confirming that this candidate membership set is broader than LYSp100B. |
| schema-result | just validate data/structures/other/lysp100_associated_nuclear_domain.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/lysp100_associated_nuclear_domain.yaml |
| strict-result | just validate-strict data/structures/other/lysp100_associated_nuclear_domain.yaml --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/lysp100_associated_nuclear_domain-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/lysp100_associated_nuclear_domain.yaml --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/lysp100_associated_nuclear_domain-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/lysp100_associated_nuclear_domain-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/lysp100_associated_nuclear_domain.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/lysp100_associated_nuclear_domain.yaml  (GO:0016606)<br>  lysp100b_land_redistribution	lysp100b_sp140	COVERED	-&gt;lysp100b_sp140 (UniProtKB:Q13342)<br>  lysp100b_land_redistribution	bright_arid3a	UNANCHORED_WITH_UNIPROT	Bright/ARID3A (UniProtKB:Q99856)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/lysp100_associated_nuclear_domain.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/lysp100_associated_nuclear_domain.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 11 collected target identifiers returned OK. PMID:25593309: UNREACHABLE; Native Europe PMC uniquely identifies MED25593309: Screen identifies bromodomain protein ZMYND8 in chromatin recognition of transcription-associated DNA damage that promotes homologous recombination. (2015); DOI 10.1101/gad.252189.114. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:8695863: UNREACHABLE; Native Europe PMC uniquely identifies MED8695863: LYSP100-associated nuclear domains (LANDs): description of a new class of subnuclear structures and their relationship to PML nuclear bodies. (1996); DOI 10.1182/blood.v88.4.1423.bloodjournal8841423. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:8910577: UNREACHABLE; Native Europe PMC uniquely identifies MED8910577: Identification and characterization of a leukocyte-specific component of the nuclear body. (1996); DOI 10.1074/jbc.271.46.29198. This resolves the identifier transport residual only; primary-source reading remains separately scoped. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five completed same-base batch26 global gates are integrated with exact manifest/input/log hashes verified; no fresh full-site QC is claimed from this sparse checkout.
- Only the explicitly listed source sections/assets were inspected. No unlisted supplements, atomic coordinates or raw experimental data were analyzed.
- Dent1996 exact DOI publisher route returned403; only its complete native abstract and identity were read. An initial guessed publisher route also403 is diagnostic only. Bloch1996 and Gong2015 are abstract-tier; Gong is used only for nuclear annotation.
- Zong XML endpoint returned500; genuine legacy HTML supplied the stated body sections. The endogenous distribution, all isoforms and lineage-level prevalence were not exhaustively assayed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes both clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T080132Z-lysp100-associated-nuclear-domain-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Lysp100 associated nuclear domain scientific review
started_at: '2026-10-22T07:34:53Z'
finished_at: '2026-10-22T08:01:32Z'
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
summary: LAND identity, SP140 isoform distinctions and the qualified redistribution/reporter
  context are supported. Broader family candidates and prevalence/formation uncertainties
  are explicit; no concrete actionable defect was established.
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
  - path: data/structures/other/lysp100_associated_nuclear_domain.yaml
    sha256: 1ab946fc5be33e183cca56f752088cfc96ff3c898c908039b43ed4007e3b1493
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
- target_id: GO:0016606
  path: data/structures/other/lysp100_associated_nuclear_domain.yaml
  label: LYSP100-associated nuclear domain
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/lysp100_associated_nuclear_domain.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target plus frozen guidance and protein-example
    skill. Actual source-reading extents appear per evidence row; no unlisted primary
    experiments or assets are certified.
  selection: Target 8 of batch58, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0016606
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0016606
  command: just validate data/structures/other/lysp100_associated_nuclear_domain.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0016606
  command: just validate-strict data/structures/other/lysp100_associated_nuclear_domain.yaml
    --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/lysp100_associated_nuclear_domain-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0016606
  command: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/lysp100_associated_nuclear_domain.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; biological claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0016606
  command: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/lysp100_associated_nuclear_domain.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; biological claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0016606
  summary: No expression-module inference is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0016606
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex58-agent-go
  - complex58-agent-go-0016606-ancestors
  - complex58-agent-tax-9606
  - complex58-agent-protein-Q13342
  - complex58-agent-protein-Q99856
  - complex58-agent-query-SP140
  - complex58-agent-pmid-25593309
  - complex58-agent-pmid-8695863
  - complex58-agent-pmid-8910577
  - complex58-agent-doi-10.1093_emboj_19.15.4123
  - complex58-agent-PMC306587-legacy
  - complex58-agent-ipr-IPR043563
  - complex58-agent-ipr-IPR030411
  - complex58-agent-panther-PTHR46386
  - complex58-agent-panther-SP140-members
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0016606
  summary: '8 of 11 collected target identifiers returned OK. PMID:25593309: UNREACHABLE;
    Native Europe PMC uniquely identifies MED25593309: Screen identifies bromodomain
    protein ZMYND8 in chromatin recognition of transcription-associated DNA damage
    that promotes homologous recombination. (2015); DOI 10.1101/gad.252189.114. This
    resolves the identifier transport residual only; primary-source reading remains
    separately scoped.; PMID:8695863: UNREACHABLE; Native Europe PMC uniquely identifies
    MED8695863: LYSP100-associated nuclear domains (LANDs): description of a new class
    of subnuclear structures and their relationship to PML nuclear bodies. (1996);
    DOI 10.1182/blood.v88.4.1423.bloodjournal8841423. This resolves the identifier
    transport residual only; primary-source reading remains separately scoped.; PMID:8910577:
    UNREACHABLE; Native Europe PMC uniquely identifies MED8910577: Identification
    and characterization of a leukocyte-specific component of the nuclear body. (1996);
    DOI 10.1074/jbc.271.46.29198. This resolves the identifier transport residual
    only; primary-source reading remains separately scoped. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - complex58-agent-pmid-25593309
  - complex58-agent-pmid-8695863
  - complex58-agent-pmid-8910577
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0016606
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
  - GO:0016606
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
  - GO:0016606
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
  - GO:0016606
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
  - GO:0016606
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
  reference: data/structures/other/lysp100_associated_nuclear_domain.yaml
  locator: Entire maintained record, all examples, evidence, graphs, properties, images,
    history and discussions
  accessed_at: '2026-10-22T07:47:24Z'
  support: context_only
  summary: Every maintained field was read. Historical curation statements are context,
    not independent biological evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component/ProteinExample, EssentialityEnum, PresenceEnum and graph-scope
    contracts
  accessed_at: '2026-10-22T07:47:24Z'
  support: context_only
  summary: Formation necessity differs from function, viability and membership. COMMON
    means most members with losses the exception; VARIABLE means lineage- or strain-level
    patchiness, not cell-type-specific visibility.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding and REVIEWED_LABEL_ONLY at159–160
  accessed_at: '2026-10-22T07:47:24Z'
  support: context_only
  summary: Exact full-family mappings differ from shared domains or broader paralog
    classes. Label-only is not merely uncurated in this pass.
- evidence_id: complex58-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004176,GO:0005743,GO:0005745,GO:0008559,GO:0016604,GO:0016605,GO:0016606,GO:0031981,GO:0034982,GO:0043190,GO:0044874,GO:0098800,GO:0140306,GO:1905368,GO:1990195,GO:1990196
  locator: Complete target-relevant definitions/synonyms and typed relationships;
    unrelated combined entries not attributed to this target
  accessed_at: '2026-10-22T07:36:57.609631Z'
  support: supports
  summary: GO0016606 defines the LYSP100-associated globular electron-dense nuclear
    domain, distinct from annular PML bodies. GO0016604 and0031981 distinguish the
    nuclear-body parent and lumen location.
  snapshot_sha256: 242f72bf78cb9fffe4670986a4651eb5296e5987f4f8f28a92533f2d5764045d
- evidence_id: complex58-agent-go-0016606-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016606/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response
  accessed_at: '2026-10-22T07:37:05.657740Z'
  support: supports
  summary: The is_a-only closure includes the maintained parent class or classes.
    It establishes classification, not parthood, experimental assembly necessity or
    prevalence.
  snapshot_sha256: 80795cf10b2383ea69c6793d595d053bf98643aa18b6acd1123bdc276bc84203
- evidence_id: complex58-agent-tax-9606
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9606
  locator: Complete ENA identity/names/lineage
  accessed_at: '2026-10-22T07:37:01.925978Z'
  support: supports
  summary: 'Taxon9606: Homo sapiens, rank species; exact native names and lineage
    inspected.'
  snapshot_sha256: 43da11bd5ae67c7de16256e9a9f3d3f90f4d70315de700d16c290352aa7b94ba
- evidence_id: complex58-agent-protein-Q13342
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q13342.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:36:59.889628Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): Q13342, Nuclear body protein SP140; primary
    genes SP140, synonyms LYSP100, taxon9606. Its own native comments and family cross-references
    were inspected with their original evidence qualifiers.'
  snapshot_sha256: 1ca48edbb0de5521968ad68e86b4df106c225d9d44713e7a6e8822fb9b48b11d
- evidence_id: complex58-agent-protein-Q99856
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q99856.json
  locator: Accession/status/name/all gene tokens/organism, relevant function/subunit/localization/similarity
    comments and family cross-references
  accessed_at: '2026-10-22T07:36:59.963631Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot): Q99856, AT-rich interactive domain-containing
    protein 3A; primary genes ARID3A, synonyms DRIL1, DRIL3, DRX, E2FBP1, taxon9606.
    Its own native comments and family cross-references were inspected with their
    original evidence qualifiers.'
  snapshot_sha256: fb86b98d83c2577e4851fe5033d8fc521fbf9d332623f823507e25bce306c332
- evidence_id: complex58-agent-query-SP140
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASP140%29+AND+%28taxonomy_id%3A9606%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete query results
  accessed_at: '2026-10-22T07:37:10.493793Z'
  support: supports
  summary: 'Exact native query returns 1 entry: Q13342. Every returned identity/gene/organism
    was read.'
  snapshot_sha256: 9a7e8c825872a5904efa07a2ba86f90816167d8403ae5eb68b0423259f58744d
  search_scope: Exact retained UniProt request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASP140%29+AND+%28taxonomy_id%3A9606%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    all returned identities inspected.
- evidence_id: complex58-agent-pmid-25593309
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25593309+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and available abstract
  accessed_at: '2026-10-22T07:37:03.117885Z'
  support: supports
  summary: 'MED25593309: Screen identifies bromodomain protein ZMYND8 in chromatin
    recognition of transcription-associated DNA damage that promotes homologous recombination.
    Gong F, Chiu LY, Cox B, Aymard F, Clouaire T, Leung JW, Cammarata M, Perez M,
    Agarwal P, Brodbelt JS, Legube G, Miller KM. (2015), DOI10.1101/gad.252189.114.
    Exact metadata and complete available abstract read; this does not claim body
    access. '
  snapshot_sha256: 0e4b5737ad0505629623425b9b7a81f077abb9c5fe02f6571367db6f91161d3a
- evidence_id: complex58-agent-pmid-8695863
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8695863+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and available abstract
  accessed_at: '2026-10-22T07:37:03.749634Z'
  support: supports
  summary: 'MED8695863: LYSP100-associated nuclear domains (LANDs): description of
    a new class of subnuclear structures and their relationship to PML nuclear bodies.
    Dent AL, Yewdell J, Puvion-Dutilleul F, Koken MH, de The H, Staudt LM. (1996),
    DOI10.1182/blood.v88.4.1423.bloodjournal8841423. Exact metadata and complete available
    abstract read; this does not claim body access. '
  snapshot_sha256: 1a71dcfd0631d9187fde1c68dab6a31ca43686e996c9d33624e2ec002bc6dabb
- evidence_id: complex58-agent-pmid-8910577
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8910577+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and available abstract
  accessed_at: '2026-10-22T07:37:03.799549Z'
  support: supports
  summary: 'MED8910577: Identification and characterization of a leukocyte-specific
    component of the nuclear body. Bloch DB, de la Monte SM, Guigaouri P, Filippov
    A, Bloch KD. (1996), DOI10.1074/jbc.271.46.29198. Exact metadata and complete
    available abstract read; this does not claim body access. '
  snapshot_sha256: 5b37e5078e4616a6e820b1eae750630d532a9018989d44b772ac308ee2058038
- evidence_id: complex58-agent-doi-10.1093_emboj_19.15.4123
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1093%2Femboj%2F19.15.4123%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identity and abstract
  accessed_at: '2026-10-22T07:37:05.588800Z'
  support: supports
  summary: 'Exact native DOI/MED identity: Regulation of matrix attachment region-dependent,
    lymphocyte-restricted transcription through differential localization within promyelocytic
    leukemia nuclear bodies. Zong RT, Das C, Tucker PW. (2000), PMID10921892. Complete
    available abstract read.'
  snapshot_sha256: 4bab70b8bea74fc35bfb51cfb5f8442711d7b8f86183e7697e84a6953f746ed5
- evidence_id: complex58-agent-PMC306587-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC306587/
  locator: Complete Introduction sec1; Results sec3/4/6/10/11; Discussion sec12; Methods
    sec14/15/17, with embedded captions read. No figure pixels.
  accessed_at: '2026-10-22T07:37:42.000052Z'
  support: supports
  summary: Zong/Das/Tucker2000 distinguishes Bright–Sp100 from weaker Bright–LYSp100B
    interactions, overexpression-associated LYSp100B redistribution and IgH-enhancer
    reporter activation. In-vitro binding is not converted into a demonstrated cellular
    LYSp100B–Bright co-immunoprecipitation. J558 and HeLa experiments and the proposed
    LAND-disruption model are distinct.
  snapshot_sha256: 9162060a127416c04f43c7d6a78dc790c983eb00a6abd9ce26ad4ac641d3660b
- evidence_id: complex58-agent-ipr-IPR043563
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR043563/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:37:43.918520Z'
  support: supports
  summary: SP110/SP140/SP140L is a broader full-family class, not a specific LYSp100B
    isoform family.
  snapshot_sha256: e2ba723108e50754180ad0e7cc9b915e06a30f2de13241eb7a84c978eee961ed
- evidence_id: complex58-agent-ipr-IPR030411
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030411/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:37:44.050915Z'
  support: supports
  summary: The SP140 bromodomain entry describes a domain rather than the complete
    retained isoform.
  snapshot_sha256: 5b4f5ae80ac063073f2f63fee038bd5c751914cd2d5f04ad91faa8c72cf95009
- evidence_id: complex58-agent-panther-PTHR46386
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR46386/
  locator: Native name/type, description and curation flags/signatures; example membership
    is independently supplied by UniProt
  accessed_at: '2026-10-22T07:37:45.362973Z'
  support: supports
  summary: The native PANTHER entry is labeled SP140 family; its name alone does not
    establish exclusivity of the retained isoform.
  snapshot_sha256: b912bcf6a56f167b7309dbd31586c9a0a3c777ae24a869216f3a4d494254b860
- evidence_id: complex58-agent-panther-SP140-members
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/panther/PTHR46386/?page_size=100
  locator: Every returned accession/protein/gene identity in the complete reviewed-member
    query
  accessed_at: '2026-10-22T07:38:24.995111Z'
  support: supports
  summary: All12 reviewed returned identities include SP100,SP110,SP140L and AIRE
    alongside SP140, confirming that this candidate membership set is broader than
    LYSp100B.
  snapshot_sha256: 0ebef401307b7308b52d811757435cc52ac8b3b8ee96f4af5158dacbbc83f499
  search_scope: Exact retained reviewed UniProt PANTHER-family query; all12 returned
    identities inspected.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/lysp100_associated_nuclear_domain.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:34:55Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/lysp100_associated_nuclear_domain.yaml'
  snapshot_sha256: d342b50937fae4fb4c74fea48bf6b90415d34e9865728e12ac37853203ce9a40
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/lysp100_associated_nuclear_domain.yaml
    --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/lysp100_associated_nuclear_domain-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:34:56Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/lysp100_associated_nuclear_domain.yaml\
    \ --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/lysp100_associated_nuclear_domain-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/lysp100_associated_nuclear_domain-strict.tsv"
  snapshot_sha256: 744a61580500c190f61ee2596584f1fa4fc6a907eb1c79bb95fe16f4701e8590
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/lysp100_associated_nuclear_domain.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T07:37:28.291156Z'
  support: supports
  summary: "data/structures/other/lysp100_associated_nuclear_domain.yaml  (GO:0016606)\n\
    \  lysp100b_land_redistribution\tlysp100b_sp140\tCOVERED\t->lysp100b_sp140 (UniProtKB:Q13342)\n\
    \  lysp100b_land_redistribution\tbright_arid3a\tUNANCHORED_WITH_UNIPROT\tBright/ARID3A\
    \ (UniProtKB:Q99856)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries\
    \ a UniProtKB grounding or xref\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 03c648141dc26b94acdd7b083c185da463446f71a47c54aa27026991ce67e399
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/lysp100_associated_nuclear_domain.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T07:37:29.585348Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/lysp100_associated_nuclear_domain.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 11 collected target identifiers returned OK. PMID:25593309: UNREACHABLE;
    Native Europe PMC uniquely identifies MED25593309: Screen identifies bromodomain
    protein ZMYND8 in chromatin recognition of transcription-associated DNA damage
    that promotes homologous recombination. (2015); DOI 10.1101/gad.252189.114. This
    resolves the identifier transport residual only; primary-source reading remains
    separately scoped.; PMID:8695863: UNREACHABLE; Native Europe PMC uniquely identifies
    MED8695863: LYSP100-associated nuclear domains (LANDs): description of a new class
    of subnuclear structures and their relationship to PML nuclear bodies. (1996);
    DOI 10.1182/blood.v88.4.1423.bloodjournal8841423. This resolves the identifier
    transport residual only; primary-source reading remains separately scoped.; PMID:8910577:
    UNREACHABLE; Native Europe PMC uniquely identifies MED8910577: Identification
    and characterization of a leukocyte-specific component of the nuclear body. (1996);
    DOI 10.1074/jbc.271.46.29198. This resolves the identifier transport residual
    only; primary-source reading remains separately scoped. Native source checks are
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
  topic: LAND morphology and isoform boundary
  outcome: supported
  target_ids:
  - GO:0016606
  summary: Exact GO morphology/location and native Q13342 SP140 identity agree. Native
    isoforms distinguish LYSp100-B from A and other forms; Q99856 is a correct human
    ARID3A/Bright identity used as external regulatory context, not a required LAND
    constituent.
  evidence_ids:
  - record
  - complex58-agent-go
  - complex58-agent-go-0016606-ancestors
  - complex58-agent-PMC306587-legacy
  - complex58-agent-protein-Q13342
  - complex58-agent-protein-Q99856
  - complex58-agent-query-SP140
  - complex58-agent-tax-9606
- assessment_id: grounding
  area: grounding
  topic: No forced broader family mapping
  outcome: supported
  target_ids:
  - GO:0016606
  summary: The inspected SP110/SP140/SP140L and PANTHER membership sets are broader
    than the retained LYSp100B class; the bromodomain is only a domain. The acknowledged
    isoform-specific label-only boundary is justified at this inspection scope.
  evidence_ids:
  - record
  - curation
  - complex58-agent-ipr-IPR043563
  - complex58-agent-ipr-IPR030411
  - complex58-agent-panther-PTHR46386
  - complex58-agent-panther-SP140-members
- assessment_id: graph
  area: graph
  topic: Qualified overexpression redistribution and reporter context
  outcome: supported
  target_ids:
  - GO:0016606
  summary: The explicitly NONMECHANISTIC graph and evidence preserve in-vitro association,
    redistribution and reporter coactivation rather than asserting endogenous universal
    assembly causality. The observed HeLa/J558 preparations do not establish every
    species-specific Bright construct equivalence.
  evidence_ids:
  - record
  - complex58-agent-PMC306587-legacy
  - complex58-agent-protein-Q13342
  - complex58-agent-protein-Q99856
- assessment_id: scope
  area: scope
  topic: Taxonomic frequency versus cell-type observations
  outcome: unknown
  target_ids:
  - GO:0016606
  summary: Human native protein identity and characterized lymphoid-associated bodies
    are established. VARIABLE retains lineage/strain-level patchiness meaning; cell-type
    expression and transfection-dependent visibility do not by themselves measure
    that frequency. This remains an explicit uncertainty, not a redefinition of the
    enum or a claim of ubiquitous LANDs.
  evidence_ids:
  - record
  - schema
  - complex58-agent-PMC306587-legacy
  - complex58-agent-tax-9606
- assessment_id: formation
  area: grounding
  topic: Unresolved individual formation necessity
  outcome: unknown
  target_ids:
  - GO:0016606
  summary: 'UNKNOWN is appropriate: enrichment and redistribution do not establish
    that LANDs cannot form without the isoform or regulator. The proposed model is
    not a universal omission assay.'
  evidence_ids:
  - record
  - schema
  - complex58-agent-PMC306587-legacy
- assessment_id: coverage
  area: completeness
  topic: Whole maintained target and declared source coverage
  outcome: supported
  target_ids:
  - GO:0016606
  summary: Every maintained field, source note, graph and discussion was inspected
    at the declared extents. Optional inventory/contact enrichment and acknowledged
    unknowns alone do not create findings.
  evidence_ids:
  - record
  - schema
  - curation
  - complex58-agent-go
findings: []
actions: []
limitations:
- All five completed same-base batch26 global gates are integrated with exact manifest/input/log
  hashes verified; no fresh full-site QC is claimed from this sparse checkout.
- Only the explicitly listed source sections/assets were inspected. No unlisted supplements,
  atomic coordinates or raw experimental data were analyzed.
- Dent1996 exact DOI publisher route returned403; only its complete native abstract
  and identity were read. An initial guessed publisher route also403 is diagnostic
  only. Bloch1996 and Gong2015 are abstract-tier; Gong is used only for nuclear annotation.
- Zong XML endpoint returned500; genuine legacy HTML supplied the stated body sections.
  The endogenous distribution, all isoforms and lineage-level prevalence were not
  exhaustively assayed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes both clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
