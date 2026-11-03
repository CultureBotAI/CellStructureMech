# Glycosome membrane identity, composition and source-scope review

- Review: 20261022T014700Z-glycosome-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:27:51Z
- Finished UTC: 2026-10-22T01:47:00Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor finding corrects the PEX14 paper’s first-author attribution; membrane topology and import role are supported within explicit source limits.

## Scope And Provenance

Whole single maintained target; exact identity, parthood, components/formation necessity, taxa, protein/source mappings, functions and every graph edge, with explicit primary/abstract/review tiers.

Selection: Target 8 of batch twenty-nine in strict uncovered path order; native initial inspection/schema/strict passed before assessment at fresh f97b1abe base.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0046860 | data/structures/membrane_organelle/glycosome_membrane.yaml | maintained | glycosome membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0046860 | The native command passed; biological membership and optional coverage are assessed independently. |
| Native protein causal-graphs | passed | True | GO:0046860 | The native command passed; biological membership and optional coverage are assessed independently. |
| Preserved first focused attempt | failed | False | GO:0046860 | The first executed attempt failed on UniProt DNS/network access; same-target network-enabled retry passed. No identity mismatch was reported by the failed transport attempt. |
| Focused native schema | passed | True | GO:0046860 | Focused validator passed. |
| Focused native strict | passed | True | GO:0046860 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0046860 | No expression-module or regulatory transcriptomics claim is used; physical compartment, protein identity and primary perturbation evidence are the applicable sources. |
| Claim-level scientific review | passed | True | GO:0046860 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0046860 | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0046860 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0046860 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0046860 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0046860 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0046860 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact whole/region/membrane identity and relations

identity: supported. Targets: GO:0046860.

The exact GO identity and peroxisomal relationship are supported. Whole glycosome, lumen and bounding membrane are distinct; the lumen parent is an is_a ancestor, and its boundary is not a lumen constituent. SL synonyms and direct mappings support their stated scopes.

### Kinetoplastid class and reference-strain versus experimental context

scope: supported. Targets: GO:0046860.

ENA5653 is class Kinetoplastea with Kinetoplastida as a synonym; the legacy order wording is not a taxon mismatch. Native source synthesis supports glycosomes across examined kinetoplastids. T.brucei is the directly studied canonical species; reference-strain protein examples are not relabelled as experiments in TREU927. Glycolytic composition varies with species and life stage.

### Collective constituents and bounded inventory

grounding: supported. Targets: GO:0046860.

The label-only constituent denotes the collective lipid bilayer, not an identified single chemical species or mixture. Its identity is supported; an exact molecular lipid inventory is not established or forced. PEX14 is a grounded graph actor, not silently added to the lipid constituent.

### Formation necessity versus functional or survival requirement

grounding: unknown. Targets: GO:0046860.

The collective membrane is constitutive of the named bounded organelle/membrane. Individual lipid-removal requirements and individual enzyme/peroxin requirements for organelle formation are not established here. Protein-import defects, catalytic effects and cell death do not alone demonstrate loss of glycosome formation. UNKNOWN protein-cohort necessity remains appropriate; the lumen record makes no component-necessity claim.

### Existing exemplar identity and evidence placement

grounding: supported. Targets: GO:0046860.

Existing native accession/status/gene/taxon pairs and their cited localization PMIDs match. Species, subspecies and reference-strain names are distinguished. Protein identity evidence is not treated as direct localization by itself; gene-less and by-similarity annotations retain their limits.

### Matrix-import boundary and four qualified edges

graph: supported. Targets: GO:0046860.

The matrix/cytosol boundary and PEX14 membrane localization/import role are supported by the complete Moyersoen abstract, independently inspected Furuya sections and native protein metadata. Four NONMECHANISTIC edges represent topology and docking placement without pretending to model the full receptor cycle. The record does not equate the PEX14 actor with the entire lipid bilayer.

### Exact first-author attribution

provenance: concern. Targets: GO:0046860.

The repeatedly cited DOI identifies Moyersoen et al.2003; Choe is the second author. Biological import claims match its abstract, but the repeated Choe et al. attribution should be corrected without replacing the paper.

### Whole target and bounded source inspection

completeness: supported. Targets: GO:0046860.

All maintained fields, source placements, discussions and graph edges were read. No maintained image asset, quantitative physical-property field or verbatim snippet is asserted. Historical status and events are not edited or independently recertified. No complete protein/lipid inventory, missing optional representative or access failure alone is converted to a finding.

## Findings

### F1: Correct the PEX14 paper’s first-author attribution

minor / open / confirmed; issue key: glycosome_membrane-pex14-first-author-attribution.

DOI10.1046/j.1432-1033.2003.03582.x is Moyersoen et al.2003, with Choe second. Several source notes call it Choe et al.2003. The DOI/title and relevant import biology are correct; the first-author attribution is not.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, change the repeated author attribution to Moyersoen et al.2003 while retaining the verified DOI and supported claim scopes.

- Preserve supported structure, protein identities and source-specific experimental boundaries.
- Run focused schema, strict and relevant native graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/glycosome_membrane.yaml; Entire maintained YAML, every field, evidence note, discussion, history entry and graph edge | context_only | The exact single target was fully read; maintained scientific content is unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component identity/grounding, essentiality, graph and protein-example contracts | context_only | Constituent identity, functional importance and necessity for organelle formation are distinct. A collective bilayer is not an exact individual lipid species. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Evidence and scope of causal edges | context_only | Graph mechanism requires claim-level causal support; topology can be described without implying molecular assembly mechanism. |
| protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Native identity verification, evidence localization, reviewed status and gene-less-entry attribution | context_only | Existing accessions and their source annotations are verified. This review does not invoke an enrichment mutation or infer membership solely from an accession. Optional absent examples are not automatic findings. |
| glycosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020015,GO:0034468,GO:0046860,GO:0005777,GO:0043233,GO:0005778; All six exact identifiers, definitions, active flags and returned child relations | supports | All six native GO terms are active. GO0020015 matches glycosome; its broader peroxisome relationship is checked in the separate exact ancestry response; GO0046860 and GO0034468 are part_of glycosome. GO0046860 is an is_a child of peroxisomal membrane GO0005778. GO0043233 is the broader organelle-lumen class; direct versus ancestral lumen relation is checked separately. |
| glycosome-agent-whole-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020015/ancestors?relations=is_a; Exact GO0020015 identifier and complete is_a ancestor list | supports | GO0020015 has GO0005777 among its is_a ancestors. This verifies the record’s broader peroxisome parent without asserting a direct edge. |
| glycosome-agent-lumen-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034468/ancestors?relations=is_a; Exact lumen ID and complete is_a ancestor list | supports | GO0034468 has GO0043233 among its is_a ancestors. This establishes a broader class relationship, not an asserted direct edge. |
| glycosome-agent-SL0129 | https://rest.uniprot.org/locations/SL-0129.json; Exact ID/name/definition, synonym list, direct GO mapping and nested isA/partOf relations; protein counts not used | supports | Native glycosome maps directly to GO0020015 and is a specialized peroxisome; its definition explicitly refers to examined kinetoplastids and glucose/glycerol enzymes. |
| glycosome-agent-SL0332 | https://rest.uniprot.org/locations/SL-0332.json; Exact ID/name/definition, synonym list, direct GO mapping and nested isA/partOf relations; protein counts not used | supports | Native Glycosome matrix maps directly to GO0034468, lists glycosomal lumen/glycosomal matrix/glycosome lumen synonyms, is_a peroxisome matrix and part_of glycosome. |
| glycosome-agent-SL0128 | https://rest.uniprot.org/locations/SL-0128.json; Exact ID/name/definition, synonym list, direct GO mapping and nested isA/partOf relations; protein counts not used | supports | Native glycosome membrane maps directly to GO0046860, lists glycosomal membrane as synonym, is_a peroxisome membrane and part_of glycosome. Nested parent information is not mistaken for another target. |
| glycosome-agent-tax5653 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5653; Exact taxId, scientificName, rank, lineage and otherNames | supports | ENA identifies Kinetoplastea, class rank, with Kinetoplastida explicitly a synonym. Database taxonomy is not a claim that all experiments used this reference strain. |
| glycosome-agent-tax5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Exact taxId, scientificName, rank, lineage and otherNames | supports | ENA identifies Trypanosoma brucei, species rank. Database taxonomy is not a claim that all experiments used this reference strain. |
| glycosome-agent-tax185431 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/185431; Exact taxId, scientificName, rank, lineage and otherNames | supports | ENA identifies Trypanosoma brucei brucei TREU927, strain rank, with strain927/4 GUTat10.1 as synonym. Database taxonomy is not a claim that all experiments used this reference strain. |
| glycosome-agent-opperdoes1977-title | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=TITLE:%22Localization%20of%20nine%20glycolytic%20enzymes%22; Exact returned MED ID, DOI, authors, title, issue/year/pages and absence of abstractText | supports | The exact native MED record is PMID142663, Opperdoes and Borst1977, FEBS Letters80:360–364, DOI10.1016/0014-5793(77)80476-6. Its title identifies nine enzymes and the microbody-like glycosome; no abstract is present and no methods or full-body claim is made from this metadata. |
| glycosome-agent-haanstra2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.bbamcr.2015.09.015; Exact PMID26384872/DOI/authors/title and complete abstractText | supports | The complete review abstract identifies specialized kinetoplastid peroxisomes, sequestration of the majority of glycolytic enzymes, varying enzyme content across species/life-cycle stages and conserved but divergent peroxin biogenesis machinery. It is review-tier synthesis, not a newly inspected primary experiment. |
| glycosome-agent-haanstra2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0806664105; Exact bibliographic identity and complete primary abstractText | supports | Native PMID19008351/PMC2584722/DOI10.1073/pnas.0806664105 identifies Haanstra et al.2008. The complete abstract reports Glc6P accumulation after glucose addition and stronger glycerol/GK rescue evidence; detailed qualifications are read in the separately captured body. |
| glycosome-agent-haanstra2008-pmc | https://pmc.ncbi.nlm.nih.gov/articles/2584722/; Complete Results sec1 including sec2–4 and Fig2–5 captions, complete Discussion sec5 and Experimental Procedures sec6 including sec7–13. No figure pixels, separate supplement or raw measurements inspected. | supports | The genuine primary body measures Glc6P accumulation in procyclic29–13 PEX14-RNAi cells after glucose addition, but Results/Discussion explicitly say this does not stringently test the compartmentation model: PGI pathway truncation is an alternative, and PF449 did not show significant Glc6P accumulation. Glycerol/Gly3P mislocalization and GK-knockdown rescue supply the stronger mechanistic test. These are not membrane-deletion experiments or universal strain phenotypes. |
| glycosome-agent-moyersoen2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1046/j.1432-1033.2003.03582.x; Exact ID/title/DOI/ordered authorList and complete abstractText; full body unavailable | supports | Native PMID12709066/DOI10.1046/j.1432-1033.2003.03582.x lists Moyersoen first and Choe second. The complete primary abstract directly reports glycosomal PEX14, N-terminal binding to PEX5 and matrix-protein mislocalization after PEX14 RNAi in bloodstream and procyclic forms; survival requirement is not organelle-formation necessity. |
| glycosome-agent-furuya2002-pmc | https://pmc.ncbi.nlm.nih.gov/articles/137857/; Methods sec5, Results sec9/10/12 including Fig1–3 captions, complete Discussion sec14. Other sections, original pixels and supplements not independently inspected. | supports | The primary study directly supports PEX14 glycosomal-membrane localization by fractionation/carbonate extraction and punctate staining, and protein mislocalization/glucose-dependent toxicity after RNAi. The study distinguishes procyclic29–13 and bloodstream cells; predicted metabolic explanations are not measured mechanism or formation necessity. |
| glycosome-agent-Q38CL4 | https://rest.uniprot.org/uniprotkb/Q38CL4.json; Accession, reviewed status, exact protein/gene/organism and localization evidence codes/citations | supports | Native reviewed Q38CL4 is glycosomal membrane PEX14 at tax185431; gene PEX14/ORF Tb10.100.0130 and cited membrane-localization PMID12386344/12709066/22809509 ECO0000269 match the graph exemplar. Single-pass topology is separately predictive. |
| access-moyersoen2003-publisher | https://febs.onlinelibrary.wiley.com/doi/10.1046/j.1432-1033.2003.03582.x; Actual retained access response, not scientific full text | context_only | Native request returned HTTP403; the response was not used as an article body. Readable native abstract or independently captured body scopes are stated separately. |
| access-moyersoen2003-pdf | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1046/j.1432-1033.2003.03582.x; Actual retained access response, not scientific full text | context_only | Native request returned HTTP403; the response was not used as an article body. Readable native abstract or independently captured body scopes are stated separately. |
| access-haanstra2016-publisher | https://www.sciencedirect.com/science/article/pii/S0167488915003080; Actual retained access response, not scientific full text | context_only | Native request returned HTTP403; the response was not used as an article body. Readable native abstract or independently captured body scopes are stated separately. |
| native-verify | /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/glycosome_membrane.yaml; Entire retained focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/glycosome_membrane.yaml; Entire retained focused native output | supports | data/structures/membrane_organelle/glycosome_membrane.yaml  (GO:0046860)<br>  glycosome_membrane_import_boundary	pex14_import_docking	UNANCHORED_WITH_UNIPROT	PEX14 import docking machinery (UniProtKB:Q38CL4)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-verify-historic-network-attempt | /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/glycosome_membrane.yaml; Original sandbox DNS failure, preserved separately from network-enabled retry | context_only | Traceback (most recent call last):<br>  File "/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py", line 922, in &lt;module&gt;<br>    raise SystemExit(main())<br>                     ~~~~^^<br>  File "/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py", line 876, in main<br>    return cmd_verify(records)<br>  File "/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py", line 727, in cmd_verify<br>    issues = verify_records(records)<br>  File "/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py", line 616, in verify_records<br>    entries = fetch_entries_by_accession(all_accs) if all_accs else {}<br>              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^<br>  File "/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py", line 169, in fetch_entries_by_accession<br>    for entry in json.loads(_get(url)).get("results", []):<br>                            ~~~~^^^^^<br>  File "/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py", line 134, in _get<br>    raise RuntimeError(f"UniProt unreachable after {RETRIES} attempts: {last}")<br>RuntimeError: UniProt unreachable after 3 attempts: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt; |
| schema-result | just validate data/structures/membrane_organelle/glycosome_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/glycosome_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/glycosome_membrane.yaml --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/glycosome_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/glycosome_membrane.yaml --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/glycosome_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch29-20261022-_v0k34u7/glycosome_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/glycosome_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- The fresh target-resolver slice and all five corpus receipt/manifest checks are integrated in this completed review.
- Opperdoes1977 is bibliographic/title-level only: native metadata has no abstract and the publisher body request returned403. No nine-enzyme original fractionation table was inspected. Haanstra2016 is complete review abstract only.
- Haanstra2008 body scope is complete Results/Discussion/main Experimental Procedures and included Fig2–5 captions; no raw data, figure pixels or separate supplements were inspected. Procyclic29–13 and PF449 responses, and glycerol versus glucose mechanism tests, remain distinct.
- COMMON denotes supported occurrence in the stated taxon context, not a measured prevalence. Experimental strains and life-cycle stages are not equated with reference-strain protein exemplars.
- Moyersoen2003 is complete primary abstract only, with exact authors/DOI verified. Furuya2002 body inspection is limited to the explicitly listed Methods/Results/Discussion sections and captions; no figure pixels or raw-data reanalysis. Individual import-protein necessity for organelle formation remains unknown.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requires one review per uncovered target, including justified clean reviews; no finding is invented to satisfy the local issue-only gate.
- Only unsaved review/support artifacts are written outside the repository; no scientific record, history, index or Git/publication mutation.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T014700Z-glycosome-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Glycosome membrane identity, composition and source-scope review
started_at: '2026-10-22T01:27:51Z'
finished_at: '2026-10-22T01:47:00Z'
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
summary: One minor finding corrects the PEX14 paper’s first-author attribution; membrane
  topology and import role are supported within explicit source limits.
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
  - path: data/structures/membrane_organelle/glycosome.yaml
    sha256: e4e8d4917968433f370c60a2f571b3c3e1f11034b01373015911772e014d2b1e
    role: context
  - path: data/structures/membrane_organelle/glycosome_lumen.yaml
    sha256: 86388cc4813e19a29b617f1800e0499e8b280823c7f3240b75c45fa7d1b8b544
    role: context
  - path: data/structures/membrane_organelle/glycosome_membrane.yaml
    sha256: 3d72e1e3fa6653b4d605c490e50da8b348c78773fa0e08947088b4e7ab2f43e9
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
- target_id: GO:0046860
  path: data/structures/membrane_organelle/glycosome_membrane.yaml
  label: glycosome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome_membrane.yaml
    role: maintained scientific record
scope:
  description: Whole single maintained target; exact identity, parthood, components/formation
    necessity, taxa, protein/source mappings, functions and every graph edge, with
    explicit primary/abstract/review tiers.
  selection: Target 8 of batch twenty-nine in strict uncovered path order; native
    initial inspection/schema/strict passed before assessment at fresh f97b1abe base.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0046860
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/glycosome_membrane.yaml
  exit_code: 0
  summary: The native command passed; biological membership and optional coverage
    are assessed independently.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/glycosome_membrane.yaml
  exit_code: 0
  summary: The native command passed; biological membership and optional coverage
    are assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify-historic-network-attempt
  name: Preserved first focused attempt
  status: failed
  required: false
  target_ids:
  - GO:0046860
  command: /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/glycosome_membrane.yaml
  exit_code: 1
  summary: The first executed attempt failed on UniProt DNS/network access; same-target
    network-enabled retry passed. No identity mismatch was reported by the failed
    transport attempt.
  evidence_ids:
  - native-verify-historic-network-attempt
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: just validate data/structures/membrane_organelle/glycosome_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: just validate-strict data/structures/membrane_organelle/glycosome_membrane.yaml
    --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/glycosome_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0046860
  summary: No expression-module or regulatory transcriptomics claim is used; physical
    compartment, protein identity and primary perturbation evidence are the applicable
    sources.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0046860
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - protein-policy
  - glycosome-agent-go
  - glycosome-agent-whole-ancestors
  - glycosome-agent-lumen-ancestors
  - glycosome-agent-SL0129
  - glycosome-agent-SL0332
  - glycosome-agent-SL0128
  - glycosome-agent-tax5653
  - glycosome-agent-tax5691
  - glycosome-agent-tax185431
  - glycosome-agent-opperdoes1977-title
  - glycosome-agent-haanstra2016-meta
  - glycosome-agent-haanstra2008-meta
  - glycosome-agent-haanstra2008-pmc
  - glycosome-agent-moyersoen2003-meta
  - glycosome-agent-furuya2002-pmc
  - glycosome-agent-Q38CL4
  - access-moyersoen2003-publisher
  - access-moyersoen2003-pdf
  - access-haanstra2016-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0046860
  summary: 10 of 10 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0046860
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
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/glycosome_membrane.yaml
  locator: Entire maintained YAML, every field, evidence note, discussion, history
    entry and graph edge
  accessed_at: '2026-10-22T01:42:31Z'
  support: context_only
  summary: The exact single target was fully read; maintained scientific content is
    unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component identity/grounding, essentiality, graph and protein-example contracts
  accessed_at: '2026-10-22T01:42:31Z'
  support: context_only
  summary: Constituent identity, functional importance and necessity for organelle
    formation are distinct. A collective bilayer is not an exact individual lipid
    species.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Evidence and scope of causal edges
  accessed_at: '2026-10-22T01:42:31Z'
  support: context_only
  summary: Graph mechanism requires claim-level causal support; topology can be described
    without implying molecular assembly mechanism.
- evidence_id: protein-policy
  kind: record_content
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Native identity verification, evidence localization, reviewed status and
    gene-less-entry attribution
  accessed_at: '2026-10-22T01:42:31Z'
  support: context_only
  summary: Existing accessions and their source annotations are verified. This review
    does not invoke an enrichment mutation or infer membership solely from an accession.
    Optional absent examples are not automatic findings.
- evidence_id: glycosome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020015,GO:0034468,GO:0046860,GO:0005777,GO:0043233,GO:0005778
  locator: All six exact identifiers, definitions, active flags and returned child
    relations
  accessed_at: '2026-10-22T01:33:40.446056Z'
  support: supports
  summary: All six native GO terms are active. GO0020015 matches glycosome; its broader
    peroxisome relationship is checked in the separate exact ancestry response; GO0046860
    and GO0034468 are part_of glycosome. GO0046860 is an is_a child of peroxisomal
    membrane GO0005778. GO0043233 is the broader organelle-lumen class; direct versus
    ancestral lumen relation is checked separately.
  snapshot_sha256: facc9847059d6bee3b8ef37cca9b5dc06236198089219562db140ac1c4770195
- evidence_id: glycosome-agent-whole-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020015/ancestors?relations=is_a
  locator: Exact GO0020015 identifier and complete is_a ancestor list
  accessed_at: '2026-10-22T01:41:49.515761Z'
  support: supports
  summary: GO0020015 has GO0005777 among its is_a ancestors. This verifies the record’s
    broader peroxisome parent without asserting a direct edge.
  snapshot_sha256: 9425be9946b6ce52ccd4145f55fd33bc8e7160b5cb93a3dd8aab3bce522645d3
- evidence_id: glycosome-agent-lumen-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034468/ancestors?relations=is_a
  locator: Exact lumen ID and complete is_a ancestor list
  accessed_at: '2026-10-22T01:33:40.454690Z'
  support: supports
  summary: GO0034468 has GO0043233 among its is_a ancestors. This establishes a broader
    class relationship, not an asserted direct edge.
  snapshot_sha256: d00024e9ab50105b15553a2ffb64a3bcae2a9c8abde352c5dd510f161e3f7e4d
- evidence_id: glycosome-agent-SL0129
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0129.json
  locator: Exact ID/name/definition, synonym list, direct GO mapping and nested isA/partOf
    relations; protein counts not used
  accessed_at: '2026-10-22T01:33:42.332830Z'
  support: supports
  summary: Native glycosome maps directly to GO0020015 and is a specialized peroxisome;
    its definition explicitly refers to examined kinetoplastids and glucose/glycerol
    enzymes.
  snapshot_sha256: 3ccdcd832fab1e23ae58f1c83d96fad980b02693753c9ad5b6d485bbcb86b509
- evidence_id: glycosome-agent-SL0332
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0332.json
  locator: Exact ID/name/definition, synonym list, direct GO mapping and nested isA/partOf
    relations; protein counts not used
  accessed_at: '2026-10-22T01:33:41.820487Z'
  support: supports
  summary: Native Glycosome matrix maps directly to GO0034468, lists glycosomal lumen/glycosomal
    matrix/glycosome lumen synonyms, is_a peroxisome matrix and part_of glycosome.
  snapshot_sha256: e285497fc15ef710692ee1c0724633d21532888659475d2a1e4fcaf2d1146a56
- evidence_id: glycosome-agent-SL0128
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0128.json
  locator: Exact ID/name/definition, synonym list, direct GO mapping and nested isA/partOf
    relations; protein counts not used
  accessed_at: '2026-10-22T01:33:42.288631Z'
  support: supports
  summary: Native glycosome membrane maps directly to GO0046860, lists glycosomal
    membrane as synonym, is_a peroxisome membrane and part_of glycosome. Nested parent
    information is not mistaken for another target.
  snapshot_sha256: b38283b04408b2c4ca030d1cd42c83316ef00566eb140f2fb5a758a82893987a
- evidence_id: glycosome-agent-tax5653
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5653
  locator: Exact taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-22T01:33:40.563693Z'
  support: supports
  summary: ENA identifies Kinetoplastea, class rank, with Kinetoplastida explicitly
    a synonym. Database taxonomy is not a claim that all experiments used this reference
    strain.
  snapshot_sha256: 6e467f5ff25d9bd8189b9c916942db46996eee6ad67fa41afd146096c2fb0556
- evidence_id: glycosome-agent-tax5691
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Exact taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-22T01:33:41.225782Z'
  support: supports
  summary: ENA identifies Trypanosoma brucei, species rank. Database taxonomy is not
    a claim that all experiments used this reference strain.
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: glycosome-agent-tax185431
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/185431
  locator: Exact taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-22T01:33:41.145219Z'
  support: supports
  summary: ENA identifies Trypanosoma brucei brucei TREU927, strain rank, with strain927/4
    GUTat10.1 as synonym. Database taxonomy is not a claim that all experiments used
    this reference strain.
  snapshot_sha256: 37f4acd608d79bb144d706335e37a83a0f97a94595aca5175855c8c390ec652d
- evidence_id: glycosome-agent-opperdoes1977-title
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=TITLE:%22Localization%20of%20nine%20glycolytic%20enzymes%22
  locator: Exact returned MED ID, DOI, authors, title, issue/year/pages and absence
    of abstractText
  accessed_at: '2026-10-22T01:34:23.268726Z'
  support: supports
  summary: The exact native MED record is PMID142663, Opperdoes and Borst1977, FEBS
    Letters80:360–364, DOI10.1016/0014-5793(77)80476-6. Its title identifies nine
    enzymes and the microbody-like glycosome; no abstract is present and no methods
    or full-body claim is made from this metadata.
  snapshot_sha256: c9d36dfb3d23668b2a5d9df081c897ac090a0210bd3a0cf81dc22b71b1c4f5e6
- evidence_id: glycosome-agent-haanstra2016-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.bbamcr.2015.09.015
  locator: Exact PMID26384872/DOI/authors/title and complete abstractText
  accessed_at: '2026-10-22T01:33:42.945022Z'
  support: supports
  summary: The complete review abstract identifies specialized kinetoplastid peroxisomes,
    sequestration of the majority of glycolytic enzymes, varying enzyme content across
    species/life-cycle stages and conserved but divergent peroxin biogenesis machinery.
    It is review-tier synthesis, not a newly inspected primary experiment.
  snapshot_sha256: a0a62b80bfc07aaec977a621651c88879a8015ba2c6e20dd5939512e56e10b4a
- evidence_id: glycosome-agent-haanstra2008-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0806664105
  locator: Exact bibliographic identity and complete primary abstractText
  accessed_at: '2026-10-22T01:33:42.586669Z'
  support: supports
  summary: Native PMID19008351/PMC2584722/DOI10.1073/pnas.0806664105 identifies Haanstra
    et al.2008. The complete abstract reports Glc6P accumulation after glucose addition
    and stronger glycerol/GK rescue evidence; detailed qualifications are read in
    the separately captured body.
  snapshot_sha256: f8d1a43be70c2a8f07b58c3a866f619c60cbfaab73a09f23cd462b3b458d0a54
- evidence_id: glycosome-agent-haanstra2008-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/2584722/
  locator: Complete Results sec1 including sec2–4 and Fig2–5 captions, complete Discussion
    sec5 and Experimental Procedures sec6 including sec7–13. No figure pixels, separate
    supplement or raw measurements inspected.
  accessed_at: '2026-10-22T01:34:23.141484Z'
  support: supports
  summary: 'The genuine primary body measures Glc6P accumulation in procyclic29–13
    PEX14-RNAi cells after glucose addition, but Results/Discussion explicitly say
    this does not stringently test the compartmentation model: PGI pathway truncation
    is an alternative, and PF449 did not show significant Glc6P accumulation. Glycerol/Gly3P
    mislocalization and GK-knockdown rescue supply the stronger mechanistic test.
    These are not membrane-deletion experiments or universal strain phenotypes.'
  snapshot_sha256: 3f10cabad24860b9d2987dfbf1f4eb229b76376a7efe67eecd6cf5090302df31
- evidence_id: glycosome-agent-moyersoen2003-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1046/j.1432-1033.2003.03582.x
  locator: Exact ID/title/DOI/ordered authorList and complete abstractText; full body
    unavailable
  accessed_at: '2026-10-22T01:33:42.446467Z'
  support: supports
  summary: Native PMID12709066/DOI10.1046/j.1432-1033.2003.03582.x lists Moyersoen
    first and Choe second. The complete primary abstract directly reports glycosomal
    PEX14, N-terminal binding to PEX5 and matrix-protein mislocalization after PEX14
    RNAi in bloodstream and procyclic forms; survival requirement is not organelle-formation
    necessity.
  snapshot_sha256: c239969526968117d4ce7f3b2137505805fb0c01127c046f44783b76be637274
- evidence_id: glycosome-agent-furuya2002-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/137857/
  locator: Methods sec5, Results sec9/10/12 including Fig1–3 captions, complete Discussion
    sec14. Other sections, original pixels and supplements not independently inspected.
  accessed_at: '2026-10-22T01:34:23.184427Z'
  support: supports
  summary: The primary study directly supports PEX14 glycosomal-membrane localization
    by fractionation/carbonate extraction and punctate staining, and protein mislocalization/glucose-dependent
    toxicity after RNAi. The study distinguishes procyclic29–13 and bloodstream cells;
    predicted metabolic explanations are not measured mechanism or formation necessity.
  snapshot_sha256: abe87b22e6a15e52ed793316b022e94c17f403a465c3d0ced8d81a1778964a3c
- evidence_id: glycosome-agent-Q38CL4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q38CL4.json
  locator: Accession, reviewed status, exact protein/gene/organism and localization
    evidence codes/citations
  accessed_at: '2026-10-22T01:33:42.485964Z'
  support: supports
  summary: Native reviewed Q38CL4 is glycosomal membrane PEX14 at tax185431; gene
    PEX14/ORF Tb10.100.0130 and cited membrane-localization PMID12386344/12709066/22809509
    ECO0000269 match the graph exemplar. Single-pass topology is separately predictive.
  snapshot_sha256: 8f717db05261f969fe531e7bd7a625eb994d4310b16be58bb9bbee0901f3ca25
- evidence_id: access-moyersoen2003-publisher
  kind: authority
  reference: https://febs.onlinelibrary.wiley.com/doi/10.1046/j.1432-1033.2003.03582.x
  locator: Actual retained access response, not scientific full text
  accessed_at: '2026-10-22T01:34:23.039364Z'
  support: context_only
  summary: Native request returned HTTP403; the response was not used as an article
    body. Readable native abstract or independently captured body scopes are stated
    separately.
  snapshot_sha256: bf3959a84ebadb57c92154781123a51ebd2abe325d3af06feecb81dbcff345a0
- evidence_id: access-moyersoen2003-pdf
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1046/j.1432-1033.2003.03582.x
  locator: Actual retained access response, not scientific full text
  accessed_at: '2026-10-22T01:34:23.214466Z'
  support: context_only
  summary: Native request returned HTTP403; the response was not used as an article
    body. Readable native abstract or independently captured body scopes are stated
    separately.
  snapshot_sha256: 6de74dc81e7158135b5ef8667a7ec748ce341936ffb14c18c8b547e997d42053
- evidence_id: access-haanstra2016-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0167488915003080
  locator: Actual retained access response, not scientific full text
  accessed_at: '2026-10-22T01:34:23.163711Z'
  support: context_only
  summary: Native request returned HTTP403; the response was not used as an article
    body. Readable native abstract or independently captured body scopes are stated
    separately.
  snapshot_sha256: 37c89f9423322b10055bcd01341ab2478adc3fde16d3578fa6983d89fdfef1d8
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/glycosome_membrane.yaml
  locator: Entire retained focused native output
  accessed_at: '2026-10-22T01:36:54.862450Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/glycosome_membrane.yaml
  locator: Entire retained focused native output
  accessed_at: '2026-10-22T01:37:25.599122Z'
  support: supports
  summary: "data/structures/membrane_organelle/glycosome_membrane.yaml  (GO:0046860)\n\
    \  glycosome_membrane_import_boundary\tpex14_import_docking\tUNANCHORED_WITH_UNIPROT\t\
    PEX14 import docking machinery (UniProtKB:Q38CL4)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node\
    \ carries a UniProtKB grounding or xref\n     0  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or\
    \ xref on the node\n     1  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: cbf88751e3948f178a24de69d80ce75d5a372684cece9df69fb6a9f43f5e9609
- evidence_id: native-verify-historic-network-attempt
  kind: validation
  reference: /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/glycosome_membrane.yaml
  locator: Original sandbox DNS failure, preserved separately from network-enabled
    retry
  accessed_at: '2026-10-22T01:36:09.055463Z'
  support: context_only
  summary: "Traceback (most recent call last):\n  File \"/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py\"\
    , line 922, in <module>\n    raise SystemExit(main())\n                     ~~~~^^\n\
    \  File \"/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py\"\
    , line 876, in main\n    return cmd_verify(records)\n  File \"/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py\"\
    , line 727, in cmd_verify\n    issues = verify_records(records)\n  File \"/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py\"\
    , line 616, in verify_records\n    entries = fetch_entries_by_accession(all_accs)\
    \ if all_accs else {}\n              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^\n  File\
    \ \"/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py\"\
    , line 169, in fetch_entries_by_accession\n    for entry in json.loads(_get(url)).get(\"\
    results\", []):\n                            ~~~~^^^^^\n  File \"/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/scripts/uniprot_genes.py\"\
    , line 134, in _get\n    raise RuntimeError(f\"UniProt unreachable after {RETRIES}\
    \ attempts: {last}\")\nRuntimeError: UniProt unreachable after 3 attempts: <urlopen\
    \ error [Errno 8] nodename nor servname provided, or not known>"
  snapshot_sha256: 40fb3bf80808292deee264b66e98286246d50ca97b3b8432aeb4321c96a83e0f
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/glycosome_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:27:52Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/glycosome_membrane.yaml'
  snapshot_sha256: 823192476dcec9d1e842a1041a44df0b6cd0bdba141bfc2bbc3c20902b5667b4
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/glycosome_membrane.yaml
    --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/glycosome_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:27:54Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/glycosome_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/glycosome_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch29-20261022-_v0k34u7/glycosome_membrane-strict.tsv"
  snapshot_sha256: 0d4d7af79003205767e6ebdeae9345948f7d288fd5c82237a72513bf615d8398
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/glycosome_membrane.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 10 of 10 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
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
  topic: Exact whole/region/membrane identity and relations
  outcome: supported
  target_ids:
  - GO:0046860
  summary: The exact GO identity and peroxisomal relationship are supported. Whole
    glycosome, lumen and bounding membrane are distinct; the lumen parent is an is_a
    ancestor, and its boundary is not a lumen constituent. SL synonyms and direct
    mappings support their stated scopes.
  evidence_ids:
  - record
  - glycosome-agent-go
  - glycosome-agent-whole-ancestors
  - glycosome-agent-lumen-ancestors
  - glycosome-agent-SL0129
  - glycosome-agent-SL0332
  - glycosome-agent-SL0128
- assessment_id: scope
  area: scope
  topic: Kinetoplastid class and reference-strain versus experimental context
  outcome: supported
  target_ids:
  - GO:0046860
  summary: ENA5653 is class Kinetoplastea with Kinetoplastida as a synonym; the legacy
    order wording is not a taxon mismatch. Native source synthesis supports glycosomes
    across examined kinetoplastids. T.brucei is the directly studied canonical species;
    reference-strain protein examples are not relabelled as experiments in TREU927.
    Glycolytic composition varies with species and life stage.
  evidence_ids:
  - record
  - glycosome-agent-tax5653
  - glycosome-agent-tax5691
  - glycosome-agent-tax185431
  - glycosome-agent-haanstra2016-meta
  - glycosome-agent-haanstra2008-meta
  - glycosome-agent-haanstra2008-pmc
- assessment_id: composition
  area: grounding
  topic: Collective constituents and bounded inventory
  outcome: supported
  target_ids:
  - GO:0046860
  summary: The label-only constituent denotes the collective lipid bilayer, not an
    identified single chemical species or mixture. Its identity is supported; an exact
    molecular lipid inventory is not established or forced. PEX14 is a grounded graph
    actor, not silently added to the lipid constituent.
  evidence_ids:
  - record
  - policy
  - glycosome-agent-go
  - glycosome-agent-haanstra2016-meta
  - glycosome-agent-moyersoen2003-meta
  - glycosome-agent-furuya2002-pmc
  - glycosome-agent-Q38CL4
- assessment_id: necessity
  area: grounding
  topic: Formation necessity versus functional or survival requirement
  outcome: unknown
  target_ids:
  - GO:0046860
  summary: The collective membrane is constitutive of the named bounded organelle/membrane.
    Individual lipid-removal requirements and individual enzyme/peroxin requirements
    for organelle formation are not established here. Protein-import defects, catalytic
    effects and cell death do not alone demonstrate loss of glycosome formation. UNKNOWN
    protein-cohort necessity remains appropriate; the lumen record makes no component-necessity
    claim.
  evidence_ids:
  - record
  - policy
  - glycosome-agent-haanstra2016-meta
  - glycosome-agent-haanstra2008-pmc
  - glycosome-agent-moyersoen2003-meta
  - glycosome-agent-furuya2002-pmc
- assessment_id: protein-identity
  area: grounding
  topic: Existing exemplar identity and evidence placement
  outcome: supported
  target_ids:
  - GO:0046860
  summary: Existing native accession/status/gene/taxon pairs and their cited localization
    PMIDs match. Species, subspecies and reference-strain names are distinguished.
    Protein identity evidence is not treated as direct localization by itself; gene-less
    and by-similarity annotations retain their limits.
  evidence_ids:
  - record
  - protein-policy
  - glycosome-agent-tax5653
  - glycosome-agent-tax5691
  - glycosome-agent-tax185431
  - glycosome-agent-Q38CL4
  - glycosome-agent-moyersoen2003-meta
  - glycosome-agent-furuya2002-pmc
- assessment_id: function-graph
  area: graph
  topic: Matrix-import boundary and four qualified edges
  outcome: supported
  target_ids:
  - GO:0046860
  summary: The matrix/cytosol boundary and PEX14 membrane localization/import role
    are supported by the complete Moyersoen abstract, independently inspected Furuya
    sections and native protein metadata. Four NONMECHANISTIC edges represent topology
    and docking placement without pretending to model the full receptor cycle. The
    record does not equate the PEX14 actor with the entire lipid bilayer.
  evidence_ids:
  - record
  - graph-policy
  - glycosome-agent-go
  - glycosome-agent-SL0129
  - glycosome-agent-SL0332
  - glycosome-agent-SL0128
  - glycosome-agent-moyersoen2003-meta
  - glycosome-agent-furuya2002-pmc
  - glycosome-agent-Q38CL4
  - glycosome-agent-haanstra2016-meta
- assessment_id: attribution
  area: provenance
  topic: Exact first-author attribution
  outcome: concern
  target_ids:
  - GO:0046860
  summary: The repeatedly cited DOI identifies Moyersoen et al.2003; Choe is the second
    author. Biological import claims match its abstract, but the repeated Choe et
    al. attribution should be corrected without replacing the paper.
  evidence_ids:
  - record
  - glycosome-agent-moyersoen2003-meta
- assessment_id: coverage
  area: completeness
  topic: Whole target and bounded source inspection
  outcome: supported
  target_ids:
  - GO:0046860
  summary: All maintained fields, source placements, discussions and graph edges were
    read. No maintained image asset, quantitative physical-property field or verbatim
    snippet is asserted. Historical status and events are not edited or independently
    recertified. No complete protein/lipid inventory, missing optional representative
    or access failure alone is converted to a finding.
  evidence_ids:
  - record
  - policy
  - glycosome-agent-go
  - glycosome-agent-opperdoes1977-title
  - glycosome-agent-haanstra2016-meta
  - glycosome-agent-haanstra2008-pmc
findings:
- finding_id: F1
  issue_key: glycosome_membrane-pex14-first-author-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the PEX14 paper’s first-author attribution
  description: DOI10.1046/j.1432-1033.2003.03582.x is Moyersoen et al.2003, with Choe
    second. Several source notes call it Choe et al.2003. The DOI/title and relevant
    import biology are correct; the first-author attribution is not.
  target_ids:
  - GO:0046860
  field_paths:
  - functions#glycosomal_matrix_import_boundary.evidence
  - evidence
  - causal_graphs#glycosome_membrane_import_boundary.edges
  evidence_ids:
  - record
  - glycosome-agent-moyersoen2003-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level support and severity
    rubric
  native_severity: minor
  normalization_reason: Minor bibliographic provenance defect; source identity and
    the supported PEX14 mechanism are not invalidated.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0046860
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome_membrane.yaml
    role: maintained scientific record
  description: In separately authorized curation, change the repeated author attribution
    to Moyersoen et al.2003 while retaining the verified DOI and supported claim scopes.
  acceptance_checks:
  - Preserve supported structure, protein identities and source-specific experimental
    boundaries.
  - Run focused schema, strict and relevant native graph checks after separately authorized
    curation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- The fresh target-resolver slice and all five corpus receipt/manifest checks are
  integrated in this completed review.
- 'Opperdoes1977 is bibliographic/title-level only: native metadata has no abstract
  and the publisher body request returned403. No nine-enzyme original fractionation
  table was inspected. Haanstra2016 is complete review abstract only.'
- Haanstra2008 body scope is complete Results/Discussion/main Experimental Procedures
  and included Fig2–5 captions; no raw data, figure pixels or separate supplements
  were inspected. Procyclic29–13 and PF449 responses, and glycerol versus glucose
  mechanism tests, remain distinct.
- COMMON denotes supported occurrence in the stated taxon context, not a measured
  prevalence. Experimental strains and life-cycle stages are not equated with reference-strain
  protein exemplars.
- Moyersoen2003 is complete primary abstract only, with exact authors/DOI verified.
  Furuya2002 body inspection is limited to the explicitly listed Methods/Results/Discussion
  sections and captions; no figure pixels or raw-data reanalysis. Individual import-protein
  necessity for organelle formation remains unknown.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requires one review per uncovered target, including justified
  clean reviews; no finding is invented to satisfy the local issue-only gate.
- Only unsaved review/support artifacts are written outside the repository; no scientific
  record, history, index or Git/publication mutation.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
