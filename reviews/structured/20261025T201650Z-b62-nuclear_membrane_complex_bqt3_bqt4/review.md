# Scientific review of nuclear membrane complex Bqt3-Bqt4

- Review: 20261025T201650Z-b62-nuclear_membrane_complex_bqt3_bqt4
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-25T19:59:42Z
- Finished UTC: 2026-10-25T20:16:50.891598Z
- Reviewer: Codex /root/plaque_review_source (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Reviewed the full record at explicitly bounded literature/native-source scope. Found 0 major and 1 minor issues. Accurate identities and supported biology are preserved; unresolved formation, prevalence and access details are reported separately.

## Scope And Provenance

One complete maintained record, all fields, source identities, current authority scopes and mechanistic assertions; no maintained scientific edits.

Selection: Root-confirmed strict uncovered-target selection for fresh B62; one independent review bundle per target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1497f644d59655f087825054920ef1a99ddebce4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990862 | data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml | maintained | nuclear membrane complex Bqt3-Bqt4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | GO:1990862 | Executed current-target check returned0. |
| Native strict | passed | True | GO:1990862 | Executed current-target check returned0. |
| Native causal-graphs | passed | True | GO:1990862 | Executed current-target check returned0. |
| Native verify | passed | True | GO:1990862 | Executed current-target check returned0. |
| Bounded full-record scientific review | passed | True | GO:1990862 | Every maintained field was inspected against the explicitly declared native and literature scopes; source-body access, inference and unresolved formation limits remain in the assessments. |
| Current-base native corpus history | passed | True | GO:1990862 | Native append-only history validation passed for2065 history files. |
| Current-base native corpus products | passed | True | GO:1990862 | Native corpus ID-label validator returned0; it does not prove class-level identity or support biological scope. |
| Current-base native corpus traits | passed | True | GO:1990862 | All10 trait links matched the freshly obtained TraitMech index. This target has no asserted trait links. |
| Current-base native corpus curies | passed | True | GO:1990862 | Native corpus resolver returned0:6105 identifiers,4997 OK,856 UNREACHABLE,252 SKIPPED. BFO authority control was not exercised because unreachable. Native exit0 is not universal resolution; target source-native checks and limitations are recorded separately. |
| Current-base native corpus qc | passed | True | GO:1990862 | Full current-base native QC passed; review-only additions are checked separately after saving. Scientific content was unchanged. |
| Native expression-dataset applicability check | passed | False | GO:1990862 | The native dataset-list command ran successfully. No dataset matches the exact named organisms, so downstream target-gene queries are not applicable. Listing absence is not biological absence; expression-module membership would not establish physical assembly. |

## Scientific And Domain Assessments

### Complex identity, hierarchy and functional relation

identity: supported. Targets: GO:1990862.

GO1990862 matches the two-protein inner-nuclear-membrane telomere-anchor complex, both maintained parent classes and INM parthood. The exact GO0070197 response includes the complex in the capable_of_part_of relationship, independently distinguishing this functional link from an is_a relation.

### Bqt3/Bqt4 classes and native examples

grounding: supported. Targets: GO:1990862.

The native Bqt4IPR037548 entry is a whole-protein family and O60158 provides the independent member bridge. O74510 and O60158 are reviewed bqt3/bqt4 instances in S. pombe972h−. Bqt3 remains accurately labeled without forcing a generic membrane domain as identity. The paper reports predicted multipass topology; a unique experimentally resolved seven-helix topology is not independently certified.

### Anchoring versus meiotic connector recruitment

evidence: concern. Targets: GO:1990862.

Bqt4 directly supports telomere attachment through Rap1 and thereby enables efficient bouquet formation. The component role additionally says it recruits Bqt1/Bqt2, but the defining study observes normal Bqt2 telomeric localization without Bqt4. The supported anchoring prerequisite must be separated from this different recruitment step.

### Telomere-anchoring mechanism

graph: supported. Targets: GO:1990862.

The graph’s stabilization/association edges and positive anchoring consequence follow the tested Bqt3/Bqt4 pathway. The function description already distinguishes anchoring from Bqt1/Bqt2-mediated clustering and should be preserved; F1 corrects the inconsistent component-role clause. Bqt3-dependent Bqt4 loss is conditioned by membrane association and nitrogen starvation, not a claim that Bqt3 is required for every viable cell state.

### Individual formation dispensability

evidence: unknown. Targets: GO:1990862.

The record’s DISPENSABLE values mean formation of the defined structure without the named component. Mitotic viability or persistence of some Bqt4 without Bqt3 is not equivalent to proving formation of the complete two-protein assembly. Conversely, the conditional stability experiments do not establish a universal formation requirement under every condition. Preserve that unresolved distinction instead of inferring ESSENTIAL from bouquet function or treating lack of a particular isolation assay as proof.

### Genus distribution and strain context

scope: unknown. Targets: GO:1990862.

The taxonomy IDs correctly identify Schizosaccharomyces and S. pombe972h−. COMMON retains its majority-occurrence meaning; the defining S. pombe experiments and discussion of other possible homologs are not a measured genus-wide functional census. TableI includes multiple engineered h+, h− and h90 backgrounds, so the reference protein strain is not substituted for every experimental mating type or genotype.

### Full-record scope and biochemical boundaries

completeness: supported. Targets: GO:1990862.

All fields, both subunits, source identities, function and graph were read. The separate meiotic Bqt1/Bqt2 connector is functional context, not an omitted constituent of the named Bqt3/Bqt4 assembly. No optional family or mechanistic-detail addition is demanded without an exact source-backed need.

## Findings

### F1: Separate Bqt4 anchoring from Bqt1–Bqt2 recruitment

minor / open / confirmed; issue key: bqt4-anchor-not-bridge-recruiter.

The Bqt4 component role says it recruits the meiotic Bqt1–Bqt2 bridge. In the cited2009 primary study, Bqt2 still localizes normally to telomeres in bqt4Δ cells even though clustering is defective. The supported Bqt4 contribution is Rap1-mediated membrane anchoring that enables efficient encounter with the spindle-pole-body connector, not the asserted direct recruitment step.

## Recommended Actions And Acceptance Checks

### C1

Replace the direct Bqt1/Bqt2 recruitment clause with the supported membrane-anchoring prerequisite for bouquet formation. Preserve the source’s normal Bqt2 telomere recruitment in bqt4Δ and the distinct Bqt1/Bqt2 bridge mechanism.

- The Bqt4 role does not assert that Bqt4 is required to recruit the Bqt1/Bqt2 bridge to telomeres.
- Rap1-dependent anchoring and its contribution to meiotic clustering remain represented, consistent with the existing function and graph.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-go-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990862/ancestors?relations=is_a; Complete ancestor lists; request explicitly restricts relations=is_a. | supports | This is an is_a-only ancestry request. Returned closures: GO:1990862: GO:0098796, GO:1990862, GO:0140513, GO:0032991, GO:0005575. This response does not attest other relation types. |
| source-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005637,GO:0070197,GO:0098796,GO:0140513,GO:1990862; All returned terms: identifiers, definitions, synonyms, isObsolete and typed children relationships. | supports | Complete requested native GO responses read: GO:0005637 nuclear inner membrane; GO:0140513 nuclear protein-containing complex; GO:0098796 membrane protein complex; GO:0070197 meiotic attachment of telomere to nuclear envelope; GO:1990862 nuclear membrane complex Bqt3-Bqt4. Definitions, obsolescence, synonyms and typed relationships were checked separately from biological source claims. |
| source-ipr-IPR037548 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037548/; metadata.accession/name/type, complete descriptions and member signatures. | supports | Native InterPro IPR037548 is named {'name': 'Bouquet formation protein 4', 'short': 'Bqt4'}, with entry type 'family'. Its complete native description and signatures were inspected for the represented family/domain scope. This family-entry response does not by itself attest membership of a particular UniProt accession. |
| source-protein-O60158 | https://rest.uniprot.org/uniprotkb/O60158.json; Identity, entryType, proteinDescription, genes, organism, relevant comments and InterPro cross-references. | supports | Native O60158 is UniProtKB reviewed (Swiss-Prot); recommended protein name Bouquet formation protein 4; primary gene(s) bqt4; organism Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812). Its own InterPro cross-references are IPR037548, IPR036887, IPR018004, IPR003163. Relevant function, subunit, subcellular-location and similarity comments were read, retaining evidence levels and source context. This protein response supplies the member-to-family bridge; a separate family entry does not establish that bridge by itself. |
| source-protein-O74510 | https://rest.uniprot.org/uniprotkb/O74510.json; Identity, entryType, proteinDescription, genes, organism, relevant comments and InterPro cross-references. | supports | Native O74510 is UniProtKB reviewed (Swiss-Prot); recommended protein name Bouquet formation protein 3; primary gene(s) bqt3; organism Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812). Its own InterPro cross-references are not supplied. Relevant function, subunit, subcellular-location and similarity comments were read, retaining evidence levels and source context. This protein response supplies the member-to-family bridge; a separate family entry does not establish that bridge by itself. |
| source-tax-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Complete taxonomy response: taxId, scientificName, rank and lineage. | supports | Native taxonomy identifies NCBITaxon:284812 as Schizosaccharomyces pombe 972h-, rank strain. The response verifies this identifier/name/rank and lineage only, not prevalence or an experimental organism assignment. |
| source-tax-4895 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4895; Complete taxonomy response: taxId, scientificName, rank and lineage. | supports | Native taxonomy identifies NCBITaxon:4895 as Schizosaccharomyces, rank genus. The response verifies this identifier/name/rank and lineage only, not prevalence or an experimental organism assignment. |
| source-pmid-19948484 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19948484+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native Europe PMC MED identity, title/authors/year/DOI and complete abstract where supplied; not a full-body attestation. | supports | Chikashige et al. 2009, DOI10.1083/jcb.200902122, establishes Bqt3/Bqt4 telomere anchoring at the nuclear envelope. Exact bibliographic identity and complete native abstract match the read primary body. |
| source-pmid-16615890 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16615890+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native Europe PMC MED identity, title/authors/year/DOI and complete abstract where supplied; not a full-body attestation. | supports | Chikashige et al. 2006, DOI10.1016/j.cell.2006.01.048, identifies Bqt1/Bqt2 as the meiotic connector between telomere proteins and the spindle-pole-body machinery. Complete native abstract only; publisher body was not recovered. |
| source-chikashige2009-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC2779253/; Complete Introduction sec1, Results sec3–8, Discussion sec9–13, Methods sec15–24, and complete TableI strain entries. Figure pixels and supplementary material not inspected; Figure4 conclusions read in Results prose, not independently from pixels. | supports | The primary study supports Bqt3/Bqt4 inner-nuclear-membrane association, Bqt4–Rap1 binding and telomere anchoring, plus reduced Bqt4 stability in bqt3 deletion, particularly under nitrogen starvation. Results sec6 reports normal telomeric Bqt2 localization in bqt4 deletion despite impaired telomere clustering. Thus Bqt4-mediated membrane attachment facilitates bouquet formation without being required to recruit the Bqt1/Bqt2 bridge to telomeres. TableI lists engineered strains with h+, h− and h90 mating types; it does not itself identify every assay as unmodified972h−. |
| source-chikashige2006-publisher | https://doi.org/10.1016/j.cell.2006.01.048; Retained access response only; no scientific body was available through this route. | context_only | The2006 publisher request failed with TLS certificate verification failure. The retained native complete abstract remains the source tier for that paper. |
| record-target | data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml; Entire frozen maintained YAML, including history, every component/example, taxonomy, evidence and graph. | context_only | The complete maintained target was read and compared claim by claim with the scoped sources; this snapshot records the assertions being reviewed rather than supplying independent biological confirmation. |
| record-schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent grounding/essentiality, ProteinExample, EssentialityEnum and PresenceEnum definitions; frozen schema input. | context_only | Grounding identifies a protein family/class rather than a generic domain. Essentiality concerns whether the structure forms without a component, independently of function or viability. COMMON means present in most members with losses exceptional; it is not redefined as cell-state occurrence. |
| check-schema | /private/tmp/cellstructure-batch62-20261025-siz_24tk/nuclear_membrane_complex_bqt3_bqt4-schema.log; Complete retained native command output. | supports | Executed native schema check returned0 for this exact target. This validates its bounded syntactic/identifier or coverage scope; it does not prove the biological claims. |
| check-strict | /private/tmp/cellstructure-batch62-20261025-siz_24tk/nuclear_membrane_complex_bqt3_bqt4-strict.log; Complete retained native command output. | supports | Executed native strict check returned0 for this exact target. This validates its bounded syntactic/identifier or coverage scope; it does not prove the biological claims. |
| check-causal-graphs | /private/tmp/cellstructure-batch62-20261025-siz_24tk/nuclear_membrane_complex_bqt3_bqt4/causal-graphs.log; Complete retained native command output. | supports | Executed native causal-graphs check returned0 for this exact target. This validates its bounded syntactic/identifier or coverage scope; it does not prove the biological claims. |
| check-verify | /private/tmp/cellstructure-batch62-20261025-siz_24tk/nuclear_membrane_complex_bqt3_bqt4/verify.log; Complete retained native command output. | supports | Executed native verify check returned0 for this exact target. This validates its bounded syntactic/identifier or coverage scope; it does not prove the biological claims. |
| final-global-history | just validate-history; Exact current-base history stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Native append-only history validation passed for2065 history files. |
| final-global-products | just validate-products; Exact current-base products stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Native corpus ID-label validator returned0; it does not prove class-level identity or support biological scope. |
| final-global-traits | just check-trait-links --check; Exact current-base traits stdout; retained receipt binds command, UTC, input manifest and exit code | supports | All10 trait links matched the freshly obtained TraitMech index. This target has no asserted trait links. |
| final-global-curies | just check-curies-strict; Exact current-base curies stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Native corpus resolver returned0:6105 identifiers,4997 OK,856 UNREACHABLE,252 SKIPPED. BFO authority control was not exercised because unreachable. Native exit0 is not universal resolution; target source-native checks and limitations are recorded separately. |
| final-global-qc | just qc; Exact current-base qc stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Full current-base native QC passed; review-only additions are checked separately after saving. Scientific content was unchanged. |
| imodulondb-datasets | https://imodulondb.org/api/datasets; Complete native console datasets listing;28 rows; exact named-organism applicability checked | context_only | No exact named-organism dataset match: Schizosaccharomyces pombe 972h-. No listed organism matches the target named species/reference strains. Listing absence is not biological negative evidence. |

## Limits And Additional Notes

- Chikashige2009 complete main prose, Methods and TableI were read; no figure pixels or supplementary material were independently examined. The Figure4 distinction is grounded in the explicit Results text.
- Chikashige2006 was read only at complete native abstract scope after a retained TLS failure; its full mechanistic Methods and figure data were not read.
- The primary paper predicts six to eight Bqt3 transmembrane segments using different tools; the record’s seven-transmembrane wording is not treated here as a uniquely measured topology.
- Genus-wide COMMON occurrence, exact correspondence of all engineered TableI strains to the canonical reference972h− label, and universal individual formation dispensability remain unresolved. These limitations do not negate the native reference-protein identities or the demonstrated S. pombe anchoring mechanism.
- Corpus identifier resolution includes856 unreachable and252 skipped identifiers despite native exit0; BFO authority control was not exercised. These residuals are not evidence of absence or scientific validity.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T201650Z-b62-nuclear_membrane_complex_bqt3_bqt4
kind: record
repository: CultureBotAI/CellStructureMech
title: Scientific review of nuclear membrane complex Bqt3-Bqt4
started_at: '2026-10-25T19:59:42Z'
finished_at: '2026-10-25T20:16:50.891598Z'
reviewer:
  identity: Codex /root/plaque_review_source
  kind: agent
  independence: independent
  independence_basis: Read-only review of the complete maintained target and retained
    native/primary payloads; this reviewer did not author or alter the maintained
    scientific record.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: Source-backed curation findings; current-base global validation receipts
  attached.
scientific_review: true
summary: Reviewed the full record at explicitly bounded literature/native-source scope.
  Found 0 major and 1 minor issues. Accurate identities and supported biology are
  preserved; unresolved formation, prevalence and access details are reported separately.
source:
  git_revision: 1497f644d59655f087825054920ef1a99ddebce4
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
  - path: data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml
    sha256: 62befbbfef3edc12db8d92b1c164212d3e1bdeb8acb85e36a21c0dfd01835b95
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
scope:
  description: One complete maintained record, all fields, source identities, current
    authority scopes and mechanistic assertions; no maintained scientific edits.
  selection: Root-confirmed strict uncovered-target selection for fresh B62; one independent
    review bundle per target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990862
targets:
- target_id: GO:1990862
  path: data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml
  label: nuclear membrane complex Bqt3-Bqt4
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml
    role: maintained scientific record
checks:
- check_id: schema
  name: Native schema
  status: passed
  required: true
  summary: Executed current-target check returned0.
  target_ids:
  - GO:1990862
  command: just validate data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
- check_id: strict
  name: Native strict
  status: passed
  required: true
  summary: Executed current-target check returned0.
  target_ids:
  - GO:1990862
  command: just validate-strict data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml
    --out /private/tmp/cellstructure-batch62-20261025-siz_24tk/nuclear_membrane_complex_bqt3_bqt4-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  summary: Executed current-target check returned0.
  target_ids:
  - GO:1990862
  command: /private/tmp/cellstructure-batch62-20261025-siz_24tk/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml
    --causal-graphs
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-causal-graphs
- check_id: verify
  name: Native verify
  status: passed
  required: true
  summary: Executed current-target check returned0.
  target_ids:
  - GO:1990862
  command: /private/tmp/cellstructure-batch62-20261025-siz_24tk/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml
    --verify
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-verify
- check_id: scientific-review
  name: Bounded full-record scientific review
  status: passed
  required: true
  summary: Every maintained field was inspected against the explicitly declared native
    and literature scopes; source-body access, inference and unresolved formation
    limits remain in the assessments.
  target_ids:
  - GO:1990862
  evidence_ids:
  - source-go-ancestors
  - source-go
  - source-ipr-IPR037548
  - source-protein-O60158
  - source-protein-O74510
  - source-tax-284812
  - source-tax-4895
  - source-pmid-19948484
  - source-pmid-16615890
  - source-chikashige2009-legacy
  - source-chikashige2006-publisher
  - record-target
  - record-schema
- check_id: final-global-history
  name: Current-base native corpus history
  status: passed
  required: true
  target_ids:
  - GO:1990862
  command: just validate-history
  exit_code: 0
  evidence_ids:
  - final-global-history
  summary: Native append-only history validation passed for2065 history files.
  scope_note: Run against unchanged scientific inputs at 1497f644d59655f087825054920ef1a99ddebce4;
    complete baseline regular-file manifest SHA256 29137a831cea7ea233f8d3f7930a920c51f63760b1c23623e2e4c0bf7bfac77e.
- check_id: final-global-products
  name: Current-base native corpus products
  status: passed
  required: true
  target_ids:
  - GO:1990862
  command: just validate-products
  exit_code: 0
  evidence_ids:
  - final-global-products
  summary: Native corpus ID-label validator returned0; it does not prove class-level
    identity or support biological scope.
  scope_note: Run against unchanged scientific inputs at 1497f644d59655f087825054920ef1a99ddebce4;
    complete baseline regular-file manifest SHA256 29137a831cea7ea233f8d3f7930a920c51f63760b1c23623e2e4c0bf7bfac77e.
- check_id: final-global-traits
  name: Current-base native corpus traits
  status: passed
  required: true
  target_ids:
  - GO:1990862
  command: just check-trait-links --check
  exit_code: 0
  evidence_ids:
  - final-global-traits
  summary: All10 trait links matched the freshly obtained TraitMech index. This target
    has no asserted trait links.
  scope_note: Run against unchanged scientific inputs at 1497f644d59655f087825054920ef1a99ddebce4;
    complete baseline regular-file manifest SHA256 29137a831cea7ea233f8d3f7930a920c51f63760b1c23623e2e4c0bf7bfac77e.
- check_id: final-global-curies
  name: Current-base native corpus curies
  status: passed
  required: true
  target_ids:
  - GO:1990862
  command: just check-curies-strict
  exit_code: 0
  evidence_ids:
  - final-global-curies
  summary: Native corpus resolver returned0:6105 identifiers,4997 OK,856 UNREACHABLE,252
    SKIPPED. BFO authority control was not exercised because unreachable. Native exit0
    is not universal resolution; target source-native checks and limitations are recorded
    separately.
  scope_note: Run against unchanged scientific inputs at 1497f644d59655f087825054920ef1a99ddebce4;
    complete baseline regular-file manifest SHA256 29137a831cea7ea233f8d3f7930a920c51f63760b1c23623e2e4c0bf7bfac77e.
- check_id: final-global-qc
  name: Current-base native corpus qc
  status: passed
  required: true
  target_ids:
  - GO:1990862
  command: just qc
  exit_code: 0
  evidence_ids:
  - final-global-qc
  summary: Full current-base native QC passed; review-only additions are checked separately
    after saving. Scientific content was unchanged.
  scope_note: Run against unchanged scientific inputs at 1497f644d59655f087825054920ef1a99ddebce4;
    complete baseline regular-file manifest SHA256 29137a831cea7ea233f8d3f7930a920c51f63760b1c23623e2e4c0bf7bfac77e.
- check_id: imodulondb-applicability
  name: Native expression-dataset applicability check
  status: passed
  required: false
  target_ids:
  - GO:1990862
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  summary: The native dataset-list command ran successfully. No dataset matches the
    exact named organisms, so downstream target-gene queries are not applicable. Listing
    absence is not biological absence; expression-module membership would not establish
    physical assembly.
  evidence_ids:
  - imodulondb-datasets
evidence:
- evidence_id: source-go-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990862/ancestors?relations=is_a
  locator: Complete ancestor lists; request explicitly restricts relations=is_a.
  accessed_at: '2026-10-25T20:02:46.888856Z'
  support: supports
  summary: 'This is an is_a-only ancestry request. Returned closures: GO:1990862:
    GO:0098796, GO:1990862, GO:0140513, GO:0032991, GO:0005575. This response does
    not attest other relation types.'
  snapshot_sha256: 02f1369c629016ae93100262f41b5dfa0392a948eeec835936d0941d246c98c0
- evidence_id: source-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005637,GO:0070197,GO:0098796,GO:0140513,GO:1990862
  locator: 'All returned terms: identifiers, definitions, synonyms, isObsolete and
    typed children relationships.'
  accessed_at: '2026-10-25T20:02:46.888431Z'
  support: supports
  summary: 'Complete requested native GO responses read: GO:0005637 nuclear inner
    membrane; GO:0140513 nuclear protein-containing complex; GO:0098796 membrane protein
    complex; GO:0070197 meiotic attachment of telomere to nuclear envelope; GO:1990862
    nuclear membrane complex Bqt3-Bqt4. Definitions, obsolescence, synonyms and typed
    relationships were checked separately from biological source claims.'
  snapshot_sha256: d4fa42a3b466308663c804f7bbd71cf2a27a04e81ddf1ec90496bb920320d4bd
- evidence_id: source-ipr-IPR037548
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037548/
  locator: metadata.accession/name/type, complete descriptions and member signatures.
  accessed_at: '2026-10-25T20:02:47.507725Z'
  support: supports
  summary: 'Native InterPro IPR037548 is named {''name'': ''Bouquet formation protein
    4'', ''short'': ''Bqt4''}, with entry type ''family''. Its complete native description
    and signatures were inspected for the represented family/domain scope. This family-entry
    response does not by itself attest membership of a particular UniProt accession.'
  snapshot_sha256: ee897421ddf7c27acbd49c7407a818a130066a5b66b5da0f2a2ff213a0b4a95b
- evidence_id: source-protein-O60158
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O60158.json
  locator: Identity, entryType, proteinDescription, genes, organism, relevant comments
    and InterPro cross-references.
  accessed_at: '2026-10-25T20:02:48.198709Z'
  support: supports
  summary: Native O60158 is UniProtKB reviewed (Swiss-Prot); recommended protein name
    Bouquet formation protein 4; primary gene(s) bqt4; organism Schizosaccharomyces
    pombe (strain 972 / ATCC 24843) (NCBITaxon:284812). Its own InterPro cross-references
    are IPR037548, IPR036887, IPR018004, IPR003163. Relevant function, subunit, subcellular-location
    and similarity comments were read, retaining evidence levels and source context.
    This protein response supplies the member-to-family bridge; a separate family
    entry does not establish that bridge by itself.
  snapshot_sha256: 05febefeae7996b8ac56e6dd68dd668ec43ba1ed7dc5654cf28d5561d6b55548
- evidence_id: source-protein-O74510
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O74510.json
  locator: Identity, entryType, proteinDescription, genes, organism, relevant comments
    and InterPro cross-references.
  accessed_at: '2026-10-25T20:02:48.710446Z'
  support: supports
  summary: Native O74510 is UniProtKB reviewed (Swiss-Prot); recommended protein name
    Bouquet formation protein 3; primary gene(s) bqt3; organism Schizosaccharomyces
    pombe (strain 972 / ATCC 24843) (NCBITaxon:284812). Its own InterPro cross-references
    are not supplied. Relevant function, subunit, subcellular-location and similarity
    comments were read, retaining evidence levels and source context. This protein
    response supplies the member-to-family bridge; a separate family entry does not
    establish that bridge by itself.
  snapshot_sha256: 3ada8ab00298188c144b494139a4dc70a7e28bb9d728cf14e95e9bb3dd2f6acd
- evidence_id: source-tax-284812
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: 'Complete taxonomy response: taxId, scientificName, rank and lineage.'
  accessed_at: '2026-10-25T20:02:47.540920Z'
  support: supports
  summary: Native taxonomy identifies NCBITaxon:284812 as Schizosaccharomyces pombe
    972h-, rank strain. The response verifies this identifier/name/rank and lineage
    only, not prevalence or an experimental organism assignment.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: source-tax-4895
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4895
  locator: 'Complete taxonomy response: taxId, scientificName, rank and lineage.'
  accessed_at: '2026-10-25T20:02:48.122067Z'
  support: supports
  summary: Native taxonomy identifies NCBITaxon:4895 as Schizosaccharomyces, rank
    genus. The response verifies this identifier/name/rank and lineage only, not prevalence
    or an experimental organism assignment.
  snapshot_sha256: 74ffbdd6b529650cbab65abad4eab52744dda99f6ce7f967c741d07505e0f8aa
- evidence_id: source-pmid-19948484
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19948484+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native Europe PMC MED identity, title/authors/year/DOI and complete
    abstract where supplied; not a full-body attestation.
  accessed_at: '2026-10-25T20:02:49.332796Z'
  support: supports
  summary: Chikashige et al. 2009, DOI10.1083/jcb.200902122, establishes Bqt3/Bqt4
    telomere anchoring at the nuclear envelope. Exact bibliographic identity and complete
    native abstract match the read primary body.
  snapshot_sha256: a44fef326ba1d55ea83adb62ce51a8c4a11e9ac3a99dffb56d353ac9c9d5609e
- evidence_id: source-pmid-16615890
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16615890+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native Europe PMC MED identity, title/authors/year/DOI and complete
    abstract where supplied; not a full-body attestation.
  accessed_at: '2026-10-25T20:02:48.952232Z'
  support: supports
  summary: Chikashige et al. 2006, DOI10.1016/j.cell.2006.01.048, identifies Bqt1/Bqt2
    as the meiotic connector between telomere proteins and the spindle-pole-body machinery.
    Complete native abstract only; publisher body was not recovered.
  snapshot_sha256: c67c32fdf42495084eadd021a426946960bdb919fa6edcbb175f69b01a18910c
- evidence_id: source-chikashige2009-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2779253/
  locator: Complete Introduction sec1, Results sec3–8, Discussion sec9–13, Methods
    sec15–24, and complete TableI strain entries. Figure pixels and supplementary
    material not inspected; Figure4 conclusions read in Results prose, not independently
    from pixels.
  accessed_at: '2026-10-25T20:03:08.008469Z'
  support: supports
  summary: The primary study supports Bqt3/Bqt4 inner-nuclear-membrane association,
    Bqt4–Rap1 binding and telomere anchoring, plus reduced Bqt4 stability in bqt3
    deletion, particularly under nitrogen starvation. Results sec6 reports normal
    telomeric Bqt2 localization in bqt4 deletion despite impaired telomere clustering.
    Thus Bqt4-mediated membrane attachment facilitates bouquet formation without being
    required to recruit the Bqt1/Bqt2 bridge to telomeres. TableI lists engineered
    strains with h+, h− and h90 mating types; it does not itself identify every assay
    as unmodified972h−.
  snapshot_sha256: 404d71cb5420a46af7823760fa0bd7ba75d53f97b1ddf33768978c4b6bb7feaa
- evidence_id: source-chikashige2006-publisher
  kind: authority
  reference: https://doi.org/10.1016/j.cell.2006.01.048
  locator: Retained access response only; no scientific body was available through
    this route.
  accessed_at: '2026-10-25T20:03:08.009080Z'
  support: context_only
  summary: The2006 publisher request failed with TLS certificate verification failure.
    The retained native complete abstract remains the source tier for that paper.
  snapshot_sha256: a8014ecefc9b9c4cc3987abe484f64b8ee37dd3e6bc0182a0f12915e702dedb3
- evidence_id: record-target
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml
  locator: Entire frozen maintained YAML, including history, every component/example,
    taxonomy, evidence and graph.
  accessed_at: '2026-10-25T20:10:02.282024Z'
  support: context_only
  summary: The complete maintained target was read and compared claim by claim with
    the scoped sources; this snapshot records the assertions being reviewed rather
    than supplying independent biological confirmation.
  snapshot_sha256: 62befbbfef3edc12db8d92b1c164212d3e1bdeb8acb85e36a21c0dfd01835b95
- evidence_id: record-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent grounding/essentiality, ProteinExample, EssentialityEnum
    and PresenceEnum definitions; frozen schema input.
  accessed_at: '2026-10-25T20:10:02.282024Z'
  support: context_only
  summary: Grounding identifies a protein family/class rather than a generic domain.
    Essentiality concerns whether the structure forms without a component, independently
    of function or viability. COMMON means present in most members with losses exceptional;
    it is not redefined as cell-state occurrence.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: check-schema
  kind: validation
  reference: /private/tmp/cellstructure-batch62-20261025-siz_24tk/nuclear_membrane_complex_bqt3_bqt4-schema.log
  locator: Complete retained native command output.
  accessed_at: '2026-10-25T19:59:44Z'
  support: supports
  summary: Executed native schema check returned0 for this exact target. This validates
    its bounded syntactic/identifier or coverage scope; it does not prove the biological
    claims.
  snapshot_sha256: a7a4ecc8e0feae6cfefc55d64a84a67eec8fc223c8b91e03c0bc0955569ba3b8
- evidence_id: check-strict
  kind: validation
  reference: /private/tmp/cellstructure-batch62-20261025-siz_24tk/nuclear_membrane_complex_bqt3_bqt4-strict.log
  locator: Complete retained native command output.
  accessed_at: '2026-10-25T19:59:47Z'
  support: supports
  summary: Executed native strict check returned0 for this exact target. This validates
    its bounded syntactic/identifier or coverage scope; it does not prove the biological
    claims.
  snapshot_sha256: 79d3d0e384f277d32c725541424d0cd25c197e2b183c07b7985ba817449480ad
- evidence_id: check-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch62-20261025-siz_24tk/nuclear_membrane_complex_bqt3_bqt4/causal-graphs.log
  locator: Complete retained native command output.
  accessed_at: '2026-10-25T20:03:45.858658Z'
  support: supports
  summary: Executed native causal-graphs check returned0 for this exact target. This
    validates its bounded syntactic/identifier or coverage scope; it does not prove
    the biological claims.
  snapshot_sha256: 63af451d58c5487f4552435d43922fe2560bfda67ba28a73a7a4c0bfe5170ccb
- evidence_id: check-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch62-20261025-siz_24tk/nuclear_membrane_complex_bqt3_bqt4/verify.log
  locator: Complete retained native command output.
  accessed_at: '2026-10-25T20:03:48.011938Z'
  support: supports
  summary: Executed native verify check returned0 for this exact target. This validates
    its bounded syntactic/identifier or coverage scope; it does not prove the biological
    claims.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: final-global-history
  kind: validation
  reference: just validate-history
  locator: Exact current-base history stdout; retained receipt binds command, UTC,
    input manifest and exit code
  accessed_at: '2026-10-25T19:59:33.039839Z'
  support: supports
  summary: Native append-only history validation passed for2065 history files.
  snapshot_sha256: beb8780a7910df045dcae7003d8ede2f8b6d08b9a311c15982997c40796d02d8
- evidence_id: final-global-products
  kind: validation
  reference: just validate-products
  locator: Exact current-base products stdout; retained receipt binds command, UTC,
    input manifest and exit code
  accessed_at: '2026-10-25T20:00:11.856400Z'
  support: supports
  summary: Native corpus ID-label validator returned0; it does not prove class-level
    identity or support biological scope.
  snapshot_sha256: 0158645d825815955f637f5ec44265e94950a33f646e419a0c8999be5aff8d2f
- evidence_id: final-global-traits
  kind: validation
  reference: just check-trait-links --check
  locator: Exact current-base traits stdout; retained receipt binds command, UTC,
    input manifest and exit code
  accessed_at: '2026-10-25T19:59:53.599030Z'
  support: supports
  summary: All10 trait links matched the freshly obtained TraitMech index. This target
    has no asserted trait links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: final-global-curies
  kind: validation
  reference: just check-curies-strict
  locator: Exact current-base curies stdout; retained receipt binds command, UTC,
    input manifest and exit code
  accessed_at: '2026-10-25T20:01:08.675608Z'
  support: supports
  summary: Native corpus resolver returned0:6105 identifiers,4997 OK,856 UNREACHABLE,252
    SKIPPED. BFO authority control was not exercised because unreachable. Native exit0
    is not universal resolution; target source-native checks and limitations are recorded
    separately.
  snapshot_sha256: 1429e55e1cb3667b4710ad56b2b9d90bd7104a24f4899edc6470f15152838e7d
- evidence_id: final-global-qc
  kind: validation
  reference: just qc
  locator: Exact current-base qc stdout; retained receipt binds command, UTC, input
    manifest and exit code
  accessed_at: '2026-10-25T20:06:17.301813Z'
  support: supports
  summary: Full current-base native QC passed; review-only additions are checked separately
    after saving. Scientific content was unchanged.
  snapshot_sha256: 3b50443af049a5f09641445e5c29c66e5f96c4f7a3bb046b344e96fa0d223d8b
- evidence_id: imodulondb-datasets
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete native console datasets listing;28 rows; exact named-organism
    applicability checked
  accessed_at: '2026-10-25T20:04:24.215410Z'
  support: context_only
  summary: 'No exact named-organism dataset match: Schizosaccharomyces pombe 972h-.
    No listed organism matches the target named species/reference strains. Listing
    absence is not biological negative evidence.'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  search_scope: All28 dataset rows returned by kg-microbe-sources imodulondb datasets;
    exact named-organism matching, not an exhaustive transcriptomics search.
assessments:
- assessment_id: A1
  area: identity
  topic: Complex identity, hierarchy and functional relation
  outcome: supported
  summary: GO1990862 matches the two-protein inner-nuclear-membrane telomere-anchor
    complex, both maintained parent classes and INM parthood. The exact GO0070197
    response includes the complex in the capable_of_part_of relationship, independently
    distinguishing this functional link from an is_a relation.
  target_ids:
  - GO:1990862
  evidence_ids:
  - source-go
  - source-go-ancestors
- assessment_id: A2
  area: grounding
  topic: Bqt3/Bqt4 classes and native examples
  outcome: supported
  summary: The native Bqt4IPR037548 entry is a whole-protein family and O60158 provides
    the independent member bridge. O74510 and O60158 are reviewed bqt3/bqt4 instances
    in S. pombe972h−. Bqt3 remains accurately labeled without forcing a generic membrane
    domain as identity. The paper reports predicted multipass topology; a unique experimentally
    resolved seven-helix topology is not independently certified.
  target_ids:
  - GO:1990862
  evidence_ids:
  - source-ipr-IPR037548
  - source-protein-O74510
  - source-protein-O60158
  - source-tax-284812
  - source-chikashige2009-legacy
- assessment_id: A3
  area: evidence
  topic: Anchoring versus meiotic connector recruitment
  outcome: concern
  summary: Bqt4 directly supports telomere attachment through Rap1 and thereby enables
    efficient bouquet formation. The component role additionally says it recruits
    Bqt1/Bqt2, but the defining study observes normal Bqt2 telomeric localization
    without Bqt4. The supported anchoring prerequisite must be separated from this
    different recruitment step.
  target_ids:
  - GO:1990862
  evidence_ids:
  - source-chikashige2009-legacy
  - source-pmid-16615890
  - record-target
- assessment_id: A4
  area: graph
  topic: Telomere-anchoring mechanism
  outcome: supported
  summary: The graph’s stabilization/association edges and positive anchoring consequence
    follow the tested Bqt3/Bqt4 pathway. The function description already distinguishes
    anchoring from Bqt1/Bqt2-mediated clustering and should be preserved; F1 corrects
    the inconsistent component-role clause. Bqt3-dependent Bqt4 loss is conditioned
    by membrane association and nitrogen starvation, not a claim that Bqt3 is required
    for every viable cell state.
  target_ids:
  - GO:1990862
  evidence_ids:
  - source-chikashige2009-legacy
  - source-go
- assessment_id: A5
  area: evidence
  topic: Individual formation dispensability
  outcome: unknown
  summary: The record’s DISPENSABLE values mean formation of the defined structure
    without the named component. Mitotic viability or persistence of some Bqt4 without
    Bqt3 is not equivalent to proving formation of the complete two-protein assembly.
    Conversely, the conditional stability experiments do not establish a universal
    formation requirement under every condition. Preserve that unresolved distinction
    instead of inferring ESSENTIAL from bouquet function or treating lack of a particular
    isolation assay as proof.
  target_ids:
  - GO:1990862
  evidence_ids:
  - record-schema
  - source-chikashige2009-legacy
- assessment_id: A6
  area: scope
  topic: Genus distribution and strain context
  outcome: unknown
  summary: The taxonomy IDs correctly identify Schizosaccharomyces and S. pombe972h−.
    COMMON retains its majority-occurrence meaning; the defining S. pombe experiments
    and discussion of other possible homologs are not a measured genus-wide functional
    census. TableI includes multiple engineered h+, h− and h90 backgrounds, so the
    reference protein strain is not substituted for every experimental mating type
    or genotype.
  target_ids:
  - GO:1990862
  evidence_ids:
  - source-tax-4895
  - source-tax-284812
  - source-chikashige2009-legacy
  - record-schema
- assessment_id: A7
  area: completeness
  topic: Full-record scope and biochemical boundaries
  outcome: supported
  summary: All fields, both subunits, source identities, function and graph were read.
    The separate meiotic Bqt1/Bqt2 connector is functional context, not an omitted
    constituent of the named Bqt3/Bqt4 assembly. No optional family or mechanistic-detail
    addition is demanded without an exact source-backed need.
  target_ids:
  - GO:1990862
  evidence_ids:
  - record-target
  - source-chikashige2009-legacy
  - source-pmid-16615890
findings:
- finding_id: F1
  issue_key: bqt4-anchor-not-bridge-recruiter
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Separate Bqt4 anchoring from Bqt1–Bqt2 recruitment
  description: The Bqt4 component role says it recruits the meiotic Bqt1–Bqt2 bridge.
    In the cited2009 primary study, Bqt2 still localizes normally to telomeres in
    bqt4Δ cells even though clustering is defective. The supported Bqt4 contribution
    is Rap1-mediated membrane anchoring that enables efficient encounter with the
    spindle-pole-body connector, not the asserted direct recruitment step.
  target_ids:
  - GO:1990862
  field_paths:
  - components[1].role
  evidence_ids:
  - record-target
  - source-chikashige2009-legacy
  - source-pmid-16615890
  normalization_reason: Minor because the correct complex identity, anchoring function
    and graph remain intact; the defect is one mechanistic role clause conflating
    two separable steps.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml
    role: maintained scientific record
actions:
- action_id: C1
  description: Replace the direct Bqt1/Bqt2 recruitment clause with the supported
    membrane-anchoring prerequisite for bouquet formation. Preserve the source’s normal
    Bqt2 telomere recruitment in bqt4Δ and the distinct Bqt1/Bqt2 bridge mechanism.
  finding_ids:
  - F1
  target_ids:
  - GO:1990862
  acceptance_checks:
  - The Bqt4 role does not assert that Bqt4 is required to recruit the Bqt1/Bqt2 bridge
    to telomeres.
  - Rap1-dependent anchoring and its contribution to meiotic clustering remain represented,
    consistent with the existing function and graph.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_membrane_complex_bqt3_bqt4.yaml
    role: maintained scientific record
limitations:
- Chikashige2009 complete main prose, Methods and TableI were read; no figure pixels
  or supplementary material were independently examined. The Figure4 distinction is
  grounded in the explicit Results text.
- Chikashige2006 was read only at complete native abstract scope after a retained
  TLS failure; its full mechanistic Methods and figure data were not read.
- The primary paper predicts six to eight Bqt3 transmembrane segments using different
  tools; the record’s seven-transmembrane wording is not treated here as a uniquely
  measured topology.
- Genus-wide COMMON occurrence, exact correspondence of all engineered TableI strains
  to the canonical reference972h− label, and universal individual formation dispensability
  remain unresolved. These limitations do not negate the native reference-protein
  identities or the demonstrated S. pombe anchoring mechanism.
- Corpus identifier resolution includes856 unreachable and252 skipped identifiers
  despite native exit0; BFO authority control was not exercised. These residuals are
  not evidence of absence or scientific validity.
notes: []
```
