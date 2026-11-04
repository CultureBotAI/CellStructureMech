# Spongiome scientific review

- Review: 20261022T034907Z-spongiome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:33:47Z
- Finished UTC: 2026-10-22T03:49:07Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact spongiome identity, pump localization, four protein examples and bounded fluid-segregation model are supported. No confirmed defect was established within the declared source limits.

## Scope And Provenance

Exactly one entire target reviewed for identity, constituents, evidence, scope, graph joins and completeness.

Selection: Target 1 of batch41, next uncovered strict-path-order target at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0062160 | data/structures/membrane_organelle/spongiome.yaml | maintained | spongiome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0062160 | Focused validator passed. |
| Focused native strict | passed | True | GO:0062160 | Focused validator passed. |
| Focused protein or graph check | passed | True | GO:0062160 | Focused native check passed; biological scope separately reviewed. |
| Focused protein or graph check | passed | True | GO:0062160 | Focused native check passed; biological scope separately reviewed. |
| Expression-module applicability | not_applicable | False | GO:0062160 | No expression-module regulatory claim is maintained. |
| Claim-level scientific review | passed | True | GO:0062160 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0062160 | 11 of 12 collected target identifiers returned OK. PMID:8294479: UNREACHABLE; Exact native MED identity independently verifies PMID, title, DOI and PMC/null mapping after bulk eutils414 failure. Abstract and body scientific scopes remain separately bounded. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0062160 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0062160 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0062160 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0062160 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0062160 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Spongiome is distinct from the central bladder

identity: supported. Targets: GO:0062160.

Exact GO0062160 and parent-complex parthood match the maintained definition. Decorated spongiome remains a narrow synonym, preserving smooth/other regions.

### Localized V-ATPase complex with honest grounding limits

grounding: supported. Targets: GO:0062160.

Primary abstracts support V-ATPase on spongiome membranes. GO0033176 identifies the generic pump class, not the exact spongiome-localized subset; leaving this localized component label-only and its grounding TODO open is acceptable. No wider CVC inventory is forcibly assigned to this subnetwork.

### Transport function versus structural necessity

evidence: supported. Targets: GO:0062160.

UNKNOWN formation essentiality is appropriate: inhibitor-dependent loss of fluid output is not evidence of structural loss. Fok explicitly reports minimal spongiome integrity effect while output is inhibited.

### Four verified subunit examples

grounding: supported. Targets: GO:0062160.

All four reviewed accessions, genes, labels, taxon pairs and one-hit native queries agree. The target correctly says these are gene-identity examples, not independent proof of spongiome localization.

### Two tested model systems

scope: supported. Targets: GO:0062160.

Nolta supports D.discoideum fractionation; Gronlien supports P.multimicronucleatum radial-arm electrophysiology. Qualitative presence and examples remain within each attached source.

### Bounded localization and functional chain

graph: supported. Targets: GO:0062160.

Four directed edges preserve CVC parthood, pump localization and Paramecium electrogenic support. NONMECHANISTIC explicitly limits a complete water-entry route; no forced upgrade or comprehensive mechanism is claimed.

### Full maintained target reviewed

completeness: supported. Targets: GO:0062160.

All fields, history and grounding discussion were inspected. No concrete current defect is established within the declared source scope.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/spongiome.yaml; Entire maintained target including history, all components, graph edges, evidence and discussions | context_only | All current fields were read. Historical events are provenance rather than independent experimental support. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component, essentiality, graph and source contracts | context_only | Exact anatomy differs from constituent material; activity and localization alone do not establish individual formation necessity. |
| root41-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0062160,GO:0062159,GO:0043231,GO:0033176,GO:0005802,GO:0098791,GO:0005794,GO:0032588,GO:0005768; Complete nine id/name/definition/active/synonym fields and applicable typed children; generic organelle child list read as context, not an exhaustive ontology search. | supports | Nine active GO entries verify exact spongiome and TGN identities, their applicable anatomy, and the generic proton-transporting V-type ATPase complex. GO0062159 has0062160 part_of;0098791 has0005802 is_a;0005802 has0032588 part_of. |
| neighbor-bladder | data/structures/membrane_organelle/contractile_vacuole.yaml; Boundary-neighbor identity, components, graph and discussions; other fields provide context | context_only | The central bladder remains distinct from the surrounding spongiome subnetwork; this neighbor is not independent experimental support. |
| root41-sources-go-search-spongiome | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=spongiome&amp;limit=100; Complete returned one-hit search response | supports | Exact native GO name search returns one active spongiome term GO0062160. |
| root41-sources-tax44689 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689; Complete native taxonomy response | supports | Native ENA identifies Dictyostelium discoideum and its rank and lineage. |
| root41-sources-tax44030 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44030; Complete native taxonomy response | supports | Native ENA identifies Paramecium multimicronucleatum and its rank and lineage. |
| root41-sources-nolta1994-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8294479%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Native bibliographic identity and returned abstract; Fok explicitly truncated, others complete | supports | Unique MED8294479 identifies Nolta and Steck1994 DOI10.1016/S0021-9258(17)42157-0. The complete abstract describes purified bipartite bladder/spongiome fractions, catalytically active pump-rich spongiomes and pump-poor bladders; energy transduction for water handling remains an interpretation. |
| root41-sources-fok1995-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1242%2Fjcs.108.10.3163&amp;format=json&amp;resultType=core; Native bibliographic identity and returned abstract; Fok explicitly truncated, others complete | supports | Unique MED7593277 identifies Fok etal1995 DOI10.1242/jcs.108.10.3163. The returned abstract is explicitly truncated at250 words: immunogold and immunofluorescence localize V-ATPase-related antigenicity to decorated pegs; concanamycin inhibits fluid output with minimal observed structural effect. The unreturned abstract ending and main body were not read. |
| root41-sources-gronlien2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1242%2Fjeb.205.20.3261&amp;format=json&amp;resultType=core; Native bibliographic identity and returned abstract; Fok explicitly truncated, others complete | supports | Unique MED12235204 identifies Gronlien etal2002 DOI10.1242/jeb.205.20.3261. Complete abstract describes microelectrode measurements, osmolarity manipulations, V-ATPase labeling and inhibition linking the decorated radial arms to electrogenic fluid segregation; membrane potential is not directly proportional to fluid-segregation rate. |
| root41-sources-docampo2013-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2FB978-0-12-407695-2.00002-0&amp;format=json&amp;resultType=core; Native bibliographic identity and returned abstract; Fok explicitly truncated, others complete | supports | Unique MED23890380 identifies Docampo etal2013 DOI10.1016/B978-0-12-407695-2.00002-0 PMC3818246. Complete abstract frames acidocalcisome/CVC osmoregulation as a review. |
| root41-sources-docampo2013-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC3818246/?report=xml; Complete sections S10 Structure and composition including Table2 and figure2 caption, S11 Biogenesis, S12 Osmoregulation including figure3/4 captions; no image pixels or underlying primary experiments | supports | Genuine review body defines bipartite CVC architecture and spongiome, differentiates bladder and spongiome protein localization in Table2, surveys biogenesis and proposed filling mechanisms. It does not turn every CVC factor into a mandatory spongiome constituent. |
| root41-sources-nolta1994-publisher | https://doi.org/10.1016/s0021-9258(17)42157-0; Retained failure response only; not article text | context_only | Native status 0 failed to supply a readable article body. No full-text access is inferred. |
| root41-sources-nolta1994-jbc | https://www.jbc.org/article/S0021-9258(17)42157-0/fulltext; Retained failure response only; not article text | context_only | Native status 403 failed to supply a readable article body. No full-text access is inferred. |
| root41-sources-fok1995-publisher | https://doi.org/10.1242/jcs.108.10.3163; Retained failure response only; not article text | context_only | Native status 403 failed to supply a readable article body. No full-text access is inferred. |
| root41-sources-fok1995-pdf | https://journals.biologists.com/jcs/article-pdf/108/10/3163/1387839/3163.pdf; Retained failure response only; not article text | context_only | Native status 403 failed to supply a readable article body. No full-text access is inferred. |
| root41-sources-gronlien2002-publisher | https://doi.org/10.1242/jeb.205.20.3261; Retained failure response only; not article text | context_only | Native status 403 failed to supply a readable article body. No full-text access is inferred. |
| root41-sources-docampo2013-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3818246/fullTextXML; Retained failure response only; not article text | context_only | Native status 500 failed to supply a readable article body. No full-text access is inferred. |
| root41-sources-protein-P54647 | https://rest.uniprot.org/uniprotkb/P54647.json; Complete identity, names, status, gene, taxon and subcellular-location/function/subunit comments; sequence and full bibliographies not reanalyzed | supports | Reviewed P54647 has exact gene vatA, D.discoideum taxon44689 and the declared V-ATPase subunit identity. Native location/function comments are distinguished from primary spongiome membership evidence. |
| root41-sources-gene-vatA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AvatA%29+AND+%28organism_id%3A44689%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Returned result count and complete accession/status/gene/taxon/protein-name fields, not all sequence or bibliography payload | supports | The complete returned reviewed gene_exact vatA/taxon44689 query has exactly one result, matching P54647. |
| root41-sources-protein-Q76NU1 | https://rest.uniprot.org/uniprotkb/Q76NU1.json; Complete identity, names, status, gene, taxon and subcellular-location/function/subunit comments; sequence and full bibliographies not reanalyzed | supports | Reviewed Q76NU1 has exact gene vatB, D.discoideum taxon44689 and the declared V-ATPase subunit identity. Native location/function comments are distinguished from primary spongiome membership evidence. |
| root41-sources-gene-vatB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AvatB%29+AND+%28organism_id%3A44689%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Returned result count and complete accession/status/gene/taxon/protein-name fields, not all sequence or bibliography payload | supports | The complete returned reviewed gene_exact vatB/taxon44689 query has exactly one result, matching Q76NU1. |
| root41-sources-protein-P54648 | https://rest.uniprot.org/uniprotkb/P54648.json; Complete identity, names, status, gene, taxon and subcellular-location/function/subunit comments; sequence and full bibliographies not reanalyzed | supports | Reviewed P54648 has exact gene vatC, D.discoideum taxon44689 and the declared V-ATPase subunit identity. Native location/function comments are distinguished from primary spongiome membership evidence. |
| root41-sources-gene-vatC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AvatC%29+AND+%28organism_id%3A44689%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Returned result count and complete accession/status/gene/taxon/protein-name fields, not all sequence or bibliography payload | supports | The complete returned reviewed gene_exact vatC/taxon44689 query has exactly one result, matching P54648. |
| root41-sources-protein-Q54E04 | https://rest.uniprot.org/uniprotkb/Q54E04.json; Complete identity, names, status, gene, taxon and subcellular-location/function/subunit comments; sequence and full bibliographies not reanalyzed | supports | Reviewed Q54E04 has exact gene vatM, D.discoideum taxon44689 and the declared V-ATPase subunit identity. Native location/function comments are distinguished from primary spongiome membership evidence. |
| root41-sources-gene-vatM | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AvatM%29+AND+%28organism_id%3A44689%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Returned result count and complete accession/status/gene/taxon/protein-name fields, not all sequence or bibliography payload | supports | The complete returned reviewed gene_exact vatM/taxon44689 query has exactly one result, matching Q54E04. |
| schema-result | just validate data/structures/membrane_organelle/spongiome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/spongiome.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/spongiome.yaml --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/spongiome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/spongiome.yaml --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/spongiome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch41-20261022-ex_agh9z/spongiome-strict.tsv |
| native-spongiome-causal | /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/spongiome.yaml; Complete focused native report | supports | data/structures/membrane_organelle/spongiome.yaml  (GO:0062160)<br>  vatpase_supported_fluid_segregation	v_type_atpase	COVERED	-&gt;v_type_atpase (UniProtKB:P54647, UniProtKB:Q76NU1, UniProtKB:P54648, UniProtKB:Q54E04)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-spongiome-proteins-network-retry | /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/spongiome.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/spongiome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 12 collected target identifiers returned OK. PMID:8294479: UNREACHABLE; Exact native MED identity independently verifies PMID, title, DOI and PMC/null mapping after bulk eutils414 failure. Abstract and body scientific scopes remain separately bounded. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Presence is qualitative and taxon examples are bounded; no complete species census, measured occurrence frequency or exhaustive molecular inventory is inferred.
- Nolta1994 and Gronlien2002 are complete-native-abstract reads only. Fok1995 is the explicitly250-word-truncated native abstract; neither its missing ending nor full paper was inspected. Publisher/PDF403 and initial Nolta request error are preserved.
- Docampo2013 S10–S12 were read completely with table and captions; other sections, image pixels and cited underlying experiments were not independently reviewed. Generic V-ATPase identity does not resolve a uniquely spongiome-localized complex.
- Initial focused protein verification failed because sandbox DNS could not reach UniProt. The preserved network-enabled retry passed; fresh native accession/query evidence was independently inspected.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User requests all uncovered records, including honest zero-finding reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T034907Z-spongiome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Spongiome scientific review
started_at: '2026-10-22T03:33:47Z'
finished_at: '2026-10-22T03:49:07Z'
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
summary: Exact spongiome identity, pump localization, four protein examples and bounded
  fluid-segregation model are supported. No confirmed defect was established within
  the declared source limits.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole.yaml
    sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
    role: context
  - path: data/structures/membrane_organelle/spongiome.yaml
    sha256: 4bdc11a86d247b6a45549a41c9aac3b25946b046f3b54d269fab634ca9d44019
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
- target_id: GO:0062160
  path: data/structures/membrane_organelle/spongiome.yaml
  label: spongiome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/spongiome.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, constituents, evidence,
    scope, graph joins and completeness.
  selection: Target 1 of batch41, next uncovered strict-path-order target at fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0062160
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0062160
  command: just validate data/structures/membrane_organelle/spongiome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0062160
  command: just validate-strict data/structures/membrane_organelle/spongiome.yaml
    --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/spongiome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-spongiome-causal
  name: Focused protein or graph check
  status: passed
  required: true
  target_ids:
  - GO:0062160
  command: /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/spongiome.yaml
  exit_code: 0
  summary: Focused native check passed; biological scope separately reviewed.
  evidence_ids:
  - native-spongiome-causal
- check_id: native-spongiome-proteins-network-retry
  name: Focused protein or graph check
  status: passed
  required: true
  target_ids:
  - GO:0062160
  command: /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/spongiome.yaml
  exit_code: 0
  summary: Focused native check passed; biological scope separately reviewed.
  evidence_ids:
  - native-spongiome-proteins-network-retry
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0062160
  summary: No expression-module regulatory claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0062160
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - root41-sources-go
  - neighbor-bladder
  - root41-sources-go-search-spongiome
  - root41-sources-tax44689
  - root41-sources-tax44030
  - root41-sources-nolta1994-meta
  - root41-sources-fok1995-meta
  - root41-sources-gronlien2002-meta
  - root41-sources-docampo2013-meta
  - root41-sources-docampo2013-legacy
  - root41-sources-nolta1994-publisher
  - root41-sources-nolta1994-jbc
  - root41-sources-fok1995-publisher
  - root41-sources-fok1995-pdf
  - root41-sources-gronlien2002-publisher
  - root41-sources-docampo2013-jats
  - root41-sources-protein-P54647
  - root41-sources-gene-vatA
  - root41-sources-protein-Q76NU1
  - root41-sources-gene-vatB
  - root41-sources-protein-P54648
  - root41-sources-gene-vatC
  - root41-sources-protein-Q54E04
  - root41-sources-gene-vatM
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0062160
  summary: '11 of 12 collected target identifiers returned OK. PMID:8294479: UNREACHABLE;
    Exact native MED identity independently verifies PMID, title, DOI and PMC/null
    mapping after bulk eutils414 failure. Abstract and body scientific scopes remain
    separately bounded. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root41-sources-nolta1994-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0062160
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch41 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0062160
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch41 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0062160
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch41 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0062160
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch41 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0062160
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
    and current batch41 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/spongiome.yaml
  locator: Entire maintained target including history, all components, graph edges,
    evidence and discussions
  accessed_at: '2026-10-22T03:45:19Z'
  support: context_only
  summary: All current fields were read. Historical events are provenance rather than
    independent experimental support.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component, essentiality, graph and source contracts
  accessed_at: '2026-10-22T03:45:19Z'
  support: context_only
  summary: Exact anatomy differs from constituent material; activity and localization
    alone do not establish individual formation necessity.
- evidence_id: root41-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0062160,GO:0062159,GO:0043231,GO:0033176,GO:0005802,GO:0098791,GO:0005794,GO:0032588,GO:0005768
  locator: Complete nine id/name/definition/active/synonym fields and applicable typed
    children; generic organelle child list read as context, not an exhaustive ontology
    search.
  accessed_at: '2026-10-22T03:36:16.668427Z'
  support: supports
  summary: Nine active GO entries verify exact spongiome and TGN identities, their
    applicable anatomy, and the generic proton-transporting V-type ATPase complex.
    GO0062159 has0062160 part_of;0098791 has0005802 is_a;0005802 has0032588 part_of.
  snapshot_sha256: 2422d30d8ab6355062d2ee5b73f7d06600669b7af572330b7cc8d560570acca9
- evidence_id: neighbor-bladder
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole.yaml
  locator: Boundary-neighbor identity, components, graph and discussions; other fields
    provide context
  accessed_at: '2026-10-22T03:45:19Z'
  support: context_only
  summary: The central bladder remains distinct from the surrounding spongiome subnetwork;
    this neighbor is not independent experimental support.
- evidence_id: root41-sources-go-search-spongiome
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=spongiome&limit=100
  locator: Complete returned one-hit search response
  accessed_at: '2026-10-22T03:36:16.669009Z'
  support: supports
  summary: Exact native GO name search returns one active spongiome term GO0062160.
  snapshot_sha256: fdd0101e8051c9d93bf9177870a8a072e867eb59e2be27236789f18a6b41266d
- evidence_id: root41-sources-tax44689
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T03:36:16.669199Z'
  support: supports
  summary: Native ENA identifies Dictyostelium discoideum and its rank and lineage.
  snapshot_sha256: 6f53a1ddbf831afbc0544e18351c92d099e28c4e8258ef29d0f841829af7c37f
- evidence_id: root41-sources-tax44030
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44030
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T03:36:16.669796Z'
  support: supports
  summary: Native ENA identifies Paramecium multimicronucleatum and its rank and lineage.
  snapshot_sha256: dd9089870a55469cb29100f05fd2b0a1a7b47e43a08b0dc6c2590a52d8fc67ab
- evidence_id: root41-sources-nolta1994-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8294479%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Native bibliographic identity and returned abstract; Fok explicitly truncated,
    others complete
  accessed_at: '2026-10-22T03:36:19.390833Z'
  support: supports
  summary: Unique MED8294479 identifies Nolta and Steck1994 DOI10.1016/S0021-9258(17)42157-0.
    The complete abstract describes purified bipartite bladder/spongiome fractions,
    catalytically active pump-rich spongiomes and pump-poor bladders; energy transduction
    for water handling remains an interpretation.
  snapshot_sha256: d29beee964bad19b97cb72a6acb0084f79ae625b8c3bd042920b60002bd868a9
- evidence_id: root41-sources-fok1995-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1242%2Fjcs.108.10.3163&format=json&resultType=core
  locator: Native bibliographic identity and returned abstract; Fok explicitly truncated,
    others complete
  accessed_at: '2026-10-22T03:36:18.695387Z'
  support: supports
  summary: 'Unique MED7593277 identifies Fok etal1995 DOI10.1242/jcs.108.10.3163.
    The returned abstract is explicitly truncated at250 words: immunogold and immunofluorescence
    localize V-ATPase-related antigenicity to decorated pegs; concanamycin inhibits
    fluid output with minimal observed structural effect. The unreturned abstract
    ending and main body were not read.'
  snapshot_sha256: 1324b4538e3fe0062b491b6ea41d51d05ededb46ae15ca83f27dacf9ceee9b8d
- evidence_id: root41-sources-gronlien2002-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1242%2Fjeb.205.20.3261&format=json&resultType=core
  locator: Native bibliographic identity and returned abstract; Fok explicitly truncated,
    others complete
  accessed_at: '2026-10-22T03:36:18.987628Z'
  support: supports
  summary: Unique MED12235204 identifies Gronlien etal2002 DOI10.1242/jeb.205.20.3261.
    Complete abstract describes microelectrode measurements, osmolarity manipulations,
    V-ATPase labeling and inhibition linking the decorated radial arms to electrogenic
    fluid segregation; membrane potential is not directly proportional to fluid-segregation
    rate.
  snapshot_sha256: ed91c2bbcf0e9848dc377c9dfce281d36a5e7b2a45713b068b748fafcb61638f
- evidence_id: root41-sources-docampo2013-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2FB978-0-12-407695-2.00002-0&format=json&resultType=core
  locator: Native bibliographic identity and returned abstract; Fok explicitly truncated,
    others complete
  accessed_at: '2026-10-22T03:36:19.108315Z'
  support: supports
  summary: Unique MED23890380 identifies Docampo etal2013 DOI10.1016/B978-0-12-407695-2.00002-0
    PMC3818246. Complete abstract frames acidocalcisome/CVC osmoregulation as a review.
  snapshot_sha256: 8f658c3e5697cdafd7e14166ab852e8ea643cd62e75486c773953e14aed46ca7
- evidence_id: root41-sources-docampo2013-legacy
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3818246/?report=xml
  locator: Complete sections S10 Structure and composition including Table2 and figure2
    caption, S11 Biogenesis, S12 Osmoregulation including figure3/4 captions; no image
    pixels or underlying primary experiments
  accessed_at: '2026-10-22T03:42:31.028339Z'
  support: supports
  summary: Genuine review body defines bipartite CVC architecture and spongiome, differentiates
    bladder and spongiome protein localization in Table2, surveys biogenesis and proposed
    filling mechanisms. It does not turn every CVC factor into a mandatory spongiome
    constituent.
  snapshot_sha256: e0224a331d19e573ed78c42acb1e447ac24ad86d3df5ecf19a42b42f49847983
- evidence_id: root41-sources-nolta1994-publisher
  kind: primary_source
  reference: https://doi.org/10.1016/s0021-9258(17)42157-0
  locator: Retained failure response only; not article text
  accessed_at: '2026-10-22T03:37:21.190860Z'
  support: context_only
  summary: Native status 0 failed to supply a readable article body. No full-text
    access is inferred.
  snapshot_sha256: a8014ecefc9b9c4cc3987abe484f64b8ee37dd3e6bc0182a0f12915e702dedb3
- evidence_id: root41-sources-nolta1994-jbc
  kind: primary_source
  reference: https://www.jbc.org/article/S0021-9258(17)42157-0/fulltext
  locator: Retained failure response only; not article text
  accessed_at: '2026-10-22T03:42:31.028010Z'
  support: context_only
  summary: Native status 403 failed to supply a readable article body. No full-text
    access is inferred.
  snapshot_sha256: b258ab57934c4c0a874918c8b52f9a6312c4bf0990600797e34d1b0f58dbcf0c
- evidence_id: root41-sources-fok1995-publisher
  kind: primary_source
  reference: https://doi.org/10.1242/jcs.108.10.3163
  locator: Retained failure response only; not article text
  accessed_at: '2026-10-22T03:37:20.879202Z'
  support: context_only
  summary: Native status 403 failed to supply a readable article body. No full-text
    access is inferred.
  snapshot_sha256: 36bfb07228b2a234098ee1fd0aa9acce66276e7b88cc1601db2fd76c4fed5ed4
- evidence_id: root41-sources-fok1995-pdf
  kind: primary_source
  reference: https://journals.biologists.com/jcs/article-pdf/108/10/3163/1387839/3163.pdf
  locator: Retained failure response only; not article text
  accessed_at: '2026-10-22T03:42:31.028382Z'
  support: context_only
  summary: Native status 403 failed to supply a readable article body. No full-text
    access is inferred.
  snapshot_sha256: 49d1a88436ae7fc43ce8ba5350e3717e7ba784a8ad37b319043e24a52ab571f6
- evidence_id: root41-sources-gronlien2002-publisher
  kind: primary_source
  reference: https://doi.org/10.1242/jeb.205.20.3261
  locator: Retained failure response only; not article text
  accessed_at: '2026-10-22T03:37:20.879317Z'
  support: context_only
  summary: Native status 403 failed to supply a readable article body. No full-text
    access is inferred.
  snapshot_sha256: 6ec20ea0e02b59d1992f4285abf9192402719c21950fff939a602f846af337cc
- evidence_id: root41-sources-docampo2013-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3818246/fullTextXML
  locator: Retained failure response only; not article text
  accessed_at: '2026-10-22T03:37:20.879272Z'
  support: context_only
  summary: Native status 500 failed to supply a readable article body. No full-text
    access is inferred.
  snapshot_sha256: ede844864bf69d7625976f0ea40c83ad819a09fb90682d5d3de98bf0040b2bfb
- evidence_id: root41-sources-protein-P54647
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P54647.json
  locator: Complete identity, names, status, gene, taxon and subcellular-location/function/subunit
    comments; sequence and full bibliographies not reanalyzed
  accessed_at: '2026-10-22T03:36:17.465961Z'
  support: supports
  summary: Reviewed P54647 has exact gene vatA, D.discoideum taxon44689 and the declared
    V-ATPase subunit identity. Native location/function comments are distinguished
    from primary spongiome membership evidence.
  snapshot_sha256: 5aa848d69318cee34c696cf4e2dbca39cd7e8080ebc456bc473ec2a0532013a0
- evidence_id: root41-sources-gene-vatA
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AvatA%29+AND+%28organism_id%3A44689%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Returned result count and complete accession/status/gene/taxon/protein-name
    fields, not all sequence or bibliography payload
  accessed_at: '2026-10-22T03:36:18.063897Z'
  support: supports
  summary: The complete returned reviewed gene_exact vatA/taxon44689 query has exactly
    one result, matching P54647.
  snapshot_sha256: 2c12da1e577bb5870984d56cf5bcd170fbdb89f3172708ffd84ae12b049181c9
- evidence_id: root41-sources-protein-Q76NU1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q76NU1.json
  locator: Complete identity, names, status, gene, taxon and subcellular-location/function/subunit
    comments; sequence and full bibliographies not reanalyzed
  accessed_at: '2026-10-22T03:36:17.466649Z'
  support: supports
  summary: Reviewed Q76NU1 has exact gene vatB, D.discoideum taxon44689 and the declared
    V-ATPase subunit identity. Native location/function comments are distinguished
    from primary spongiome membership evidence.
  snapshot_sha256: 484196af4048c2df60bf0e618e372458df7ba5a7778b2f32288f73a1f328bb6d
- evidence_id: root41-sources-gene-vatB
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AvatB%29+AND+%28organism_id%3A44689%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Returned result count and complete accession/status/gene/taxon/protein-name
    fields, not all sequence or bibliography payload
  accessed_at: '2026-10-22T03:36:18.162663Z'
  support: supports
  summary: The complete returned reviewed gene_exact vatB/taxon44689 query has exactly
    one result, matching Q76NU1.
  snapshot_sha256: f9527eae42063733d601f599bd144adebe9c130843078b50f9d8de535d4ff25d
- evidence_id: root41-sources-protein-P54648
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P54648.json
  locator: Complete identity, names, status, gene, taxon and subcellular-location/function/subunit
    comments; sequence and full bibliographies not reanalyzed
  accessed_at: '2026-10-22T03:36:18.057405Z'
  support: supports
  summary: Reviewed P54648 has exact gene vatC, D.discoideum taxon44689 and the declared
    V-ATPase subunit identity. Native location/function comments are distinguished
    from primary spongiome membership evidence.
  snapshot_sha256: db4310ad9862f746a114c8af73f1363a6d432cf1329c0464fd20f4efb395feb9
- evidence_id: root41-sources-gene-vatC
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AvatC%29+AND+%28organism_id%3A44689%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Returned result count and complete accession/status/gene/taxon/protein-name
    fields, not all sequence or bibliography payload
  accessed_at: '2026-10-22T03:36:18.653996Z'
  support: supports
  summary: The complete returned reviewed gene_exact vatC/taxon44689 query has exactly
    one result, matching P54648.
  snapshot_sha256: 8a15ae741468663769fb0eeb265a150c3f9360f41949cf2b46a9db2e19537553
- evidence_id: root41-sources-protein-Q54E04
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q54E04.json
  locator: Complete identity, names, status, gene, taxon and subcellular-location/function/subunit
    comments; sequence and full bibliographies not reanalyzed
  accessed_at: '2026-10-22T03:36:18.058013Z'
  support: supports
  summary: Reviewed Q54E04 has exact gene vatM, D.discoideum taxon44689 and the declared
    V-ATPase subunit identity. Native location/function comments are distinguished
    from primary spongiome membership evidence.
  snapshot_sha256: 169ff6e42d6dcdd8abffa5ff7466a09eeabda4b1cf8b39bd2bc757a0a118fa8d
- evidence_id: root41-sources-gene-vatM
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AvatM%29+AND+%28organism_id%3A44689%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Returned result count and complete accession/status/gene/taxon/protein-name
    fields, not all sequence or bibliography payload
  accessed_at: '2026-10-22T03:36:18.671156Z'
  support: supports
  summary: The complete returned reviewed gene_exact vatM/taxon44689 query has exactly
    one result, matching Q54E04.
  snapshot_sha256: 7c969239729bc25a8916bb4db884580dd8f251d720b83222b316582d55b961a9
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/spongiome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:33:48Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/spongiome.yaml'
  snapshot_sha256: 531e0617872fce75462b45572d34cd351a65fe7218a15b9495b8ac6a4c5fe14b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/spongiome.yaml
    --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/spongiome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:33:49Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/spongiome.yaml\
    \ --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/spongiome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch41-20261022-ex_agh9z/spongiome-strict.tsv"
  snapshot_sha256: d331563dcbfe6b61f8b09877f8efe9c3518474da3f5d8c88e7333dd7256d8d14
- evidence_id: native-spongiome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/spongiome.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T03:42:19.830701Z'
  support: supports
  summary: "data/structures/membrane_organelle/spongiome.yaml  (GO:0062160)\n  vatpase_supported_fluid_segregation\t\
    v_type_atpase\tCOVERED\t->v_type_atpase (UniProtKB:P54647, UniProtKB:Q76NU1, UniProtKB:P54648,\
    \ UniProtKB:Q54E04)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     1\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 4d41d47db587f66f6559b075ec4fa3a8035b83dcbe834c912167c7b48880de1d
- evidence_id: native-spongiome-proteins-network-retry
  kind: validation
  reference: /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/spongiome.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T03:43:37.593525Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/spongiome.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 12 collected target identifiers returned OK. PMID:8294479: UNREACHABLE;
    Exact native MED identity independently verifies PMID, title, DOI and PMC/null
    mapping after bulk eutils414 failure. Abstract and body scientific scopes remain
    separately bounded. Native source checks are separately scoped; skipped or unreachable
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
  topic: Spongiome is distinct from the central bladder
  outcome: supported
  target_ids:
  - GO:0062160
  summary: Exact GO0062160 and parent-complex parthood match the maintained definition.
    Decorated spongiome remains a narrow synonym, preserving smooth/other regions.
  evidence_ids:
  - record
  - root41-sources-go
  - root41-sources-go-search-spongiome
  - root41-sources-fok1995-meta
  - root41-sources-docampo2013-legacy
- assessment_id: composition
  area: grounding
  topic: Localized V-ATPase complex with honest grounding limits
  outcome: supported
  target_ids:
  - GO:0062160
  summary: Primary abstracts support V-ATPase on spongiome membranes. GO0033176 identifies
    the generic pump class, not the exact spongiome-localized subset; leaving this
    localized component label-only and its grounding TODO open is acceptable. No wider
    CVC inventory is forcibly assigned to this subnetwork.
  evidence_ids:
  - record
  - schema
  - root41-sources-go
  - root41-sources-docampo2013-legacy
  - root41-sources-nolta1994-meta
  - root41-sources-fok1995-meta
  - root41-sources-gronlien2002-meta
  - root41-sources-docampo2013-meta
- assessment_id: formation
  area: evidence
  topic: Transport function versus structural necessity
  outcome: supported
  target_ids:
  - GO:0062160
  summary: 'UNKNOWN formation essentiality is appropriate: inhibitor-dependent loss
    of fluid output is not evidence of structural loss. Fok explicitly reports minimal
    spongiome integrity effect while output is inhibited.'
  evidence_ids:
  - record
  - schema
  - root41-sources-fok1995-meta
  - root41-sources-gronlien2002-meta
- assessment_id: proteins
  area: grounding
  topic: Four verified subunit examples
  outcome: supported
  target_ids:
  - GO:0062160
  summary: All four reviewed accessions, genes, labels, taxon pairs and one-hit native
    queries agree. The target correctly says these are gene-identity examples, not
    independent proof of spongiome localization.
  evidence_ids:
  - record
  - root41-sources-protein-P54647
  - root41-sources-gene-vatA
  - root41-sources-protein-Q76NU1
  - root41-sources-gene-vatB
  - root41-sources-protein-P54648
  - root41-sources-gene-vatC
  - root41-sources-protein-Q54E04
  - root41-sources-gene-vatM
- assessment_id: taxonomy
  area: scope
  topic: Two tested model systems
  outcome: supported
  target_ids:
  - GO:0062160
  summary: Nolta supports D.discoideum fractionation; Gronlien supports P.multimicronucleatum
    radial-arm electrophysiology. Qualitative presence and examples remain within
    each attached source.
  evidence_ids:
  - record
  - root41-sources-tax44689
  - root41-sources-tax44030
  - root41-sources-nolta1994-meta
  - root41-sources-gronlien2002-meta
- assessment_id: graph
  area: graph
  topic: Bounded localization and functional chain
  outcome: supported
  target_ids:
  - GO:0062160
  summary: Four directed edges preserve CVC parthood, pump localization and Paramecium
    electrogenic support. NONMECHANISTIC explicitly limits a complete water-entry
    route; no forced upgrade or comprehensive mechanism is claimed.
  evidence_ids:
  - record
  - root41-sources-go
  - root41-sources-nolta1994-meta
  - root41-sources-fok1995-meta
  - root41-sources-gronlien2002-meta
  - root41-sources-docampo2013-meta
  - root41-sources-docampo2013-legacy
- assessment_id: coverage
  area: completeness
  topic: Full maintained target reviewed
  outcome: supported
  target_ids:
  - GO:0062160
  summary: All fields, history and grounding discussion were inspected. No concrete
    current defect is established within the declared source scope.
  evidence_ids:
  - record
  - schema
  - root41-sources-go
  - root41-sources-docampo2013-legacy
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Presence is qualitative and taxon examples are bounded; no complete species census,
  measured occurrence frequency or exhaustive molecular inventory is inferred.
- Nolta1994 and Gronlien2002 are complete-native-abstract reads only. Fok1995 is the
  explicitly250-word-truncated native abstract; neither its missing ending nor full
  paper was inspected. Publisher/PDF403 and initial Nolta request error are preserved.
- Docampo2013 S10–S12 were read completely with table and captions; other sections,
  image pixels and cited underlying experiments were not independently reviewed. Generic
  V-ATPase identity does not resolve a uniquely spongiome-localized complex.
- Initial focused protein verification failed because sandbox DNS could not reach
  UniProt. The preserved network-enabled retry passed; fresh native accession/query
  evidence was independently inspected.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User requests all uncovered records, including honest zero-finding reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
