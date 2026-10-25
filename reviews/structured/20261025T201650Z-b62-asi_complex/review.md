# Scientific review of Asi complex

- Review: 20261025T201650Z-b62-asi_complex
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-25T19:59:39Z
- Finished UTC: 2026-10-25T20:16:50.859311Z
- Reviewer: Codex /root/plaque_review_source (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Reviewed the full record at explicitly bounded literature/native-source scope. Found 1 major and 1 minor issues. Accurate identities and supported biology are preserved; unresolved formation, prevalence and access details are reported separately.

## Scope And Provenance

One complete maintained record, all fields, source identities, current authority scopes and mechanistic assertions; no maintained scientific edits.

Selection: Root-confirmed strict uncovered-target selection for fresh B62; one independent review bundle per target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1497f644d59655f087825054920ef1a99ddebce4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097658 | data/structures/membrane_organelle/asi_complex.yaml | maintained | Asi complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | GO:0097658 | Executed current-target check returned0. |
| Native strict | passed | True | GO:0097658 | Executed current-target check returned0. |
| Native causal-graphs | passed | True | GO:0097658 | Executed current-target check returned0. |
| Native verify | passed | True | GO:0097658 | Executed current-target check returned0. |
| Bounded full-record scientific review | passed | True | GO:0097658 | Every maintained field was inspected against the explicitly declared native and literature scopes; source-body access, inference and unresolved formation limits remain in the assessments. |
| Current-base native corpus history | passed | True | GO:0097658 | Native append-only history validation passed for2065 history files. |
| Current-base native corpus products | passed | True | GO:0097658 | Native corpus ID-label validator returned0; it does not prove class-level identity or support biological scope. |
| Current-base native corpus traits | passed | True | GO:0097658 | All10 trait links matched the freshly obtained TraitMech index. This target has no asserted trait links. |
| Current-base native corpus curies | passed | True | GO:0097658 | Native corpus resolver returned0:6105 identifiers,4997 OK,856 UNREACHABLE,252 SKIPPED. BFO authority control was not exercised because unreachable. Native exit0 is not universal resolution; target source-native checks and limitations are recorded separately. |
| Current-base native corpus qc | passed | True | GO:0097658 | Full current-base native QC passed; review-only additions are checked separately after saving. Scientific content was unchanged. |
| Native expression-dataset applicability check | passed | False | GO:0097658 | The native dataset-list command ran successfully. No dataset matches the exact named organisms, so downstream target-gene queries are not applicable. Listing absence is not biological absence; expression-module membership would not establish physical assembly. |

## Scientific And Domain Assessments

### Asi complex ontology and compartment

identity: supported. Targets: GO:0097658.

Native GO0097658 matches the maintained inner-nuclear-membrane nuclear ubiquitin-ligase identity, both parent classes and the INM part-of placement. Primary main text independently supports the specialized nuclear-envelope surveillance system.

### Whole-protein identities versus a shared domain fold

grounding: concern. Targets: GO:0097658.

IPR013083 is a homologous superfamily covering RING/FYVE/PHD-like small domains and related folds. It does not identify the complete Asi1 or Asi3 protein class. IPR063277 is an Asi2 family, and the three reviewed UniProt instances have the maintained genes and S288C taxon. P53983’s native recommended name itself says ASI1 despite the correct ASI3 gene; that naming quirk is not an accession mismatch.

### Taxon label and supported population

scope: concern. Targets: GO:0097658.

NCBITaxon4891 denotes the class Saccharomycetes, whereas the target labels it Saccharomycetaceae and repeats a family-level conservation statement. The code and stated taxonomic scope must be reconciled. COMMON means majority occurrence with exceptional losses, not simply characterized in yeast; neither the native taxon identity nor the read single-species experiments establish a census across either chosen rank.

### Substrate ubiquitylation and degradation mechanism

graph: supported. Targets: GO:0097658.

The graph has valid component references and a coherent direction from Asi membership through ubiquitylation to degradation. The read primary body supports E2 interactions, substrate-dependent turnover and a recognition interpretation for Asi2. This positive assessment does not certify the unavailable Foresti-specific co-purification, RING-mutant or Cdc48 extraction details; those remain separately limited. The duplicated wrong domain grounding is included in F1.

### Foresti-specific mechanistic details

evidence: unknown. Targets: GO:0097658.

The complete Foresti abstract and Khmelinskii body support the overall pathway, but the exact Foresti experiments invoked for Cdc48-dependent extraction, essential catalytic RING partners and co-purification were not readable at full-body scope. They are not rejected merely because access failed, and are not passed as experimentally verified by this review.

### Formation necessity and dispensability

evidence: unknown. Targets: GO:0097658.

The three DISPENSABLE labels refer to complex formation under the schema. Viable deletions, loss of degradation activity and substrate-specific effects do not automatically establish formation of the defined complex without each named subunit. The inspected experiments support membership and functional differentiation but leave universal individual assembly necessity unresolved; no opposite ESSENTIAL claim is inferred.

### Scope and experimental exemplars

completeness: supported. Targets: GO:0097658.

All maintained fields and three constituent rows were inspected. Native S288C entries are valid reference protein instances; the read primary work uses specified derivative backgrounds, so the reference-strain label is not taken to certify every assay in unmodified S288C. No additional optional inventory or unsearched exact Asi1/Asi3 family is asserted.

## Findings

### F1: Remove domain-superfamily identity from the Asi1 and Asi3 protein classes

major / open / confirmed; issue key: asi-domain-superfamily-grounding.

Both whole-protein component rows and their graph nodes use InterProIPR013083 as identity. The actual native entry is a RING/FYVE/PHD-like homologous superfamily of small domains, not a whole Asi1/Asi3 protein family. Presence of such a domain in these correct protein examples does not make it an exact molecular-class grounding.

### F2: Reconcile Saccharomycetes identifier with the family-level label

minor / open / confirmed; issue key: asi-taxon-rank-label.

The distribution row pairs NCBITaxon4891 with Saccharomycetaceae. Native taxonomy identifies4891 as Saccharomycetes, rank class. The adjoining family-level conservation statement compounds the rank ambiguity. This finding concerns the concrete identifier/label mismatch; it does not infer absence from any lineage.

## Recommended Actions And Acceptance Checks

### C1

Remove IPR013083 from the two whole-protein identities and graph counterparts. Use exact whole-protein family groundings only after verification, otherwise retain accurate labels with appropriately qualified grounding status/notes. Keep RING-domain information as functional/domain context.

- Neither Asi1 nor Asi3 whole-protein node is equated to the domain superfamily.
- Any replacement family is verified at the appropriate whole-protein scope and bridged independently to the correct native examples.
- ASI2IPR063277 and the three correct UniProt identities remain unchanged unless separately supported.

### C2

Choose the intended taxonomic rank and make its identifier, label and conservation wording agree; verify any replacement family identifier and its distribution support.

- NCBITaxon4891 is labeled Saccharomycetes if retained, or a separately verified family identifier accompanies Saccharomycetaceae.
- The presence note does not use an identifier mismatch as evidence of family-wide conservation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-go-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097658/ancestors?relations=is_a; Complete ancestor lists; request explicitly restricts relations=is_a. | supports | This is an is_a-only ancestry request. Returned closures: GO:0097658: GO:0098796, GO:1902494, GO:1990234, GO:0000152, GO:0140535, GO:0140513, GO:0000151, GO:0097658, GO:0032991, GO:0005575. This response does not attest other relation types. |
| source-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000152,GO:0000209,GO:0005637,GO:0006511,GO:0097658,GO:0098796; All returned terms: identifiers, definitions, synonyms, isObsolete and typed children relationships. | supports | Complete requested native GO responses read: GO:0005637 nuclear inner membrane; GO:0006511 ubiquitin-dependent protein catabolic process; GO:0098796 membrane protein complex; GO:0000152 nuclear ubiquitin ligase complex; GO:0097658 Asi complex; GO:0000209 protein polyubiquitination. Definitions, obsolescence, synonyms and typed relationships were checked separately from biological source claims. |
| source-ipr-IPR013083 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013083/; metadata.accession/name/type, complete descriptions and member signatures. | supports | Native InterPro IPR013083 is named {'name': 'Zinc finger, RING/FYVE/PHD-type', 'short': 'Znf_RING/FYVE/PHD'}, with entry type 'homologous_superfamily'. Its complete native description and signatures were inspected for the represented family/domain scope. This family-entry response does not by itself attest membership of a particular UniProt accession. |
| source-ipr-IPR063277 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063277/; metadata.accession/name/type, complete descriptions and member signatures. | supports | Native InterPro IPR063277 is named {'name': 'Amino acid sensor-independent protein 2', 'short': 'ASI2'}, with entry type 'family'. Its complete native description and signatures were inspected for the represented family/domain scope. This family-entry response does not by itself attest membership of a particular UniProt accession. |
| source-protein-P53895 | https://rest.uniprot.org/uniprotkb/P53895.json; Identity, entryType, proteinDescription, genes, organism, relevant comments and InterPro cross-references. | supports | Native P53895 is UniProtKB reviewed (Swiss-Prot); recommended protein name Protein ASI2; primary gene(s) ASI2; organism Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (NCBITaxon:559292). Its own InterPro cross-references are IPR063277. Relevant function, subunit, subcellular-location and similarity comments were read, retaining evidence levels and source context. This protein response supplies the member-to-family bridge; a separate family entry does not establish that bridge by itself. |
| source-protein-P53983 | https://rest.uniprot.org/uniprotkb/P53983.json; Identity, entryType, proteinDescription, genes, organism, relevant comments and InterPro cross-references. | supports | Native P53983 is UniProtKB reviewed (Swiss-Prot); recommended protein name Probable ERAD-associated E3 ubiquitin-protein ligase ASI1; primary gene(s) ASI3; organism Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (NCBITaxon:559292). Its own InterPro cross-references are IPR013083. Relevant function, subunit, subcellular-location and similarity comments were read, retaining evidence levels and source context. This protein response supplies the member-to-family bridge; a separate family entry does not establish that bridge by itself. |
| source-protein-P54074 | https://rest.uniprot.org/uniprotkb/P54074.json; Identity, entryType, proteinDescription, genes, organism, relevant comments and InterPro cross-references. | supports | Native P54074 is UniProtKB reviewed (Swiss-Prot); recommended protein name ERAD-associated E3 ubiquitin-protein ligase ASI1; primary gene(s) ASI1; organism Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (NCBITaxon:559292). Its own InterPro cross-references are IPR013083. Relevant function, subunit, subcellular-location and similarity comments were read, retaining evidence levels and source context. This protein response supplies the member-to-family bridge; a separate family entry does not establish that bridge by itself. |
| source-tax-4891 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4891; Complete taxonomy response: taxId, scientificName, rank and lineage. | supports | Native taxonomy identifies NCBITaxon:4891 as Saccharomycetes, rank class. The response verifies this identifier/name/rank and lineage only, not prevalence or an experimental organism assignment. |
| source-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxonomy response: taxId, scientificName, rank and lineage. | supports | Native taxonomy identifies NCBITaxon:559292 as Saccharomyces cerevisiae S288C, rank strain. The response verifies this identifier/name/rank and lineage only, not prevalence or an experimental organism assignment. |
| source-pmid-25236469 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25236469+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native Europe PMC MED identity, title/authors/year/DOI and complete abstract where supplied; not a full-body attestation. | supports | Foresti et al. 2014, DOI10.1126/science.1255638, is the primary Asi inner-nuclear-membrane quality-control study. Exact authors/title/DOI and complete native abstract were read. The abstract supports an Asi quality-control pathway; the detailed Cdc48, RING-mutant, co-purification and strain claims are not certified as read from this paper’s unavailable body. |
| source-pmid-25519137 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25519137+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native Europe PMC MED identity, title/authors/year/DOI and complete abstract where supplied; not a full-body attestation. | supports | Khmelinskii et al. 2014, DOI10.1038/nature14096, is the primary mislocalized-protein surveillance study. Exact identity and complete abstract match the separately read primary body. |
| source-khmelinskii2014-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC4493439/; Complete unsectioned scientific main text with Figures1–3 captions; Methods sections S2–S13. Primer tables, extended-data captions/pixels and supplementary tables not independently inspected. | supports | The primary main text supports Asi1/Asi3 inner-nuclear-membrane ligase roles, Ubc6/Ubc7 interactions, altered substrate stability and Asi2-dependent recognition of a subset of tested substrates. The authors present Asi2 recognition as an inference from differential substrate effects, not a directly resolved recognition structure. Methods specify BY4741/scEB115-derived experimental backgrounds, not an undifferentiated reference-strain assay. |
| source-foresti2014-publisher | https://doi.org/10.1126/science.1255638; Retained access response only; no scientific body was available through this route. | context_only | The Foresti publisher request returned HTTP403; no scientific body was read from this route. |
| source-foresti2014-ora | https://ora.ox.ac.uk/objects/uuid:d529010b-d3f9-48a8-826b-b5d7bb093296; Institutional record title/authors/publication and access-document links. | context_only | The Oxford institutional landing page supplies bibliographic metadata and a publisher DOI link, not a recovered full scientific body. It is retained for access provenance only. |
| record-target | data/structures/membrane_organelle/asi_complex.yaml; Entire frozen maintained YAML, including history, every component/example, taxonomy, evidence and graph. | context_only | The complete maintained target was read and compared claim by claim with the scoped sources; this snapshot records the assertions being reviewed rather than supplying independent biological confirmation. |
| record-schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent grounding/essentiality, ProteinExample, EssentialityEnum and PresenceEnum definitions; frozen schema input. | context_only | Grounding identifies a protein family/class rather than a generic domain. Essentiality concerns whether the structure forms without a component, independently of function or viability. COMMON means present in most members with losses exceptional; it is not redefined as cell-state occurrence. |
| check-schema | /private/tmp/cellstructure-batch62-20261025-siz_24tk/asi_complex-schema.log; Complete retained native command output. | supports | Executed native schema check returned0 for this exact target. This validates its bounded syntactic/identifier or coverage scope; it does not prove the biological claims. |
| check-strict | /private/tmp/cellstructure-batch62-20261025-siz_24tk/asi_complex-strict.log; Complete retained native command output. | supports | Executed native strict check returned0 for this exact target. This validates its bounded syntactic/identifier or coverage scope; it does not prove the biological claims. |
| check-causal-graphs | /private/tmp/cellstructure-batch62-20261025-siz_24tk/asi_complex/causal-graphs.log; Complete retained native command output. | supports | Executed native causal-graphs check returned0 for this exact target. This validates its bounded syntactic/identifier or coverage scope; it does not prove the biological claims. |
| check-verify | /private/tmp/cellstructure-batch62-20261025-siz_24tk/asi_complex/verify.log; Complete retained native command output. | supports | Executed native verify check returned0 for this exact target. This validates its bounded syntactic/identifier or coverage scope; it does not prove the biological claims. |
| final-global-history | just validate-history; Exact current-base history stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Native append-only history validation passed for2065 history files. |
| final-global-products | just validate-products; Exact current-base products stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Native corpus ID-label validator returned0; it does not prove class-level identity or support biological scope. |
| final-global-traits | just check-trait-links --check; Exact current-base traits stdout; retained receipt binds command, UTC, input manifest and exit code | supports | All10 trait links matched the freshly obtained TraitMech index. This target has no asserted trait links. |
| final-global-curies | just check-curies-strict; Exact current-base curies stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Native corpus resolver returned0:6105 identifiers,4997 OK,856 UNREACHABLE,252 SKIPPED. BFO authority control was not exercised because unreachable. Native exit0 is not universal resolution; target source-native checks and limitations are recorded separately. |
| final-global-qc | just qc; Exact current-base qc stdout; retained receipt binds command, UTC, input manifest and exit code | supports | Full current-base native QC passed; review-only additions are checked separately after saving. Scientific content was unchanged. |
| imodulondb-datasets | https://imodulondb.org/api/datasets; Complete native console datasets listing;28 rows; exact named-organism applicability checked | context_only | No exact named-organism dataset match: Saccharomyces cerevisiae S288C. No listed organism matches the target named species/reference strains. Listing absence is not biological negative evidence. |

## Limits And Additional Notes

- Foresti2014 publisher access returned403 and the institutional landing page was metadata only. Its complete native abstract was read, but detailed co-purification, RING-mutant, Cdc48 and strain-specific evidence is not certified as full-body read.
- Khmelinskii main text, Figures1–3 captions and MethodsS2–S13 were read; primer tables, extended-data/supplement tables and figure pixels were not inspected. Its Asi2-recognition interpretation is retained as inference from substrate effects.
- Taxonomic majority occurrence remains unresolved beyond characterized yeast systems; this review preserves the precise COMMON schema meaning and does not infer biological absence.
- Correct S288C protein references do not attest that every cited experiment used unmodified S288C. Individual formation DISPENSABLE claims remain unresolved rather than being inferred from viability or loss of quality-control function.
- Corpus identifier resolution includes856 unreachable and252 skipped identifiers despite native exit0; BFO authority control was not exercised. These residuals are not evidence of absence or scientific validity.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T201650Z-b62-asi_complex
kind: record
repository: CultureBotAI/CellStructureMech
title: Scientific review of Asi complex
started_at: '2026-10-25T19:59:39Z'
finished_at: '2026-10-25T20:16:50.859311Z'
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
  Found 1 major and 1 minor issues. Accurate identities and supported biology are
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
  - path: data/structures/membrane_organelle/asi_complex.yaml
    sha256: 56c8f96688172f37a0f84d9a6d0932133243ffe331a63247c48d9f51ad168c54
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
  - GO:0097658
targets:
- target_id: GO:0097658
  path: data/structures/membrane_organelle/asi_complex.yaml
  label: Asi complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/asi_complex.yaml
    role: maintained scientific record
checks:
- check_id: schema
  name: Native schema
  status: passed
  required: true
  summary: Executed current-target check returned0.
  target_ids:
  - GO:0097658
  command: just validate data/structures/membrane_organelle/asi_complex.yaml
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
  - GO:0097658
  command: just validate-strict data/structures/membrane_organelle/asi_complex.yaml
    --out /private/tmp/cellstructure-batch62-20261025-siz_24tk/asi_complex-strict.tsv
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
  - GO:0097658
  command: /private/tmp/cellstructure-batch62-20261025-siz_24tk/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/membrane_organelle/asi_complex.yaml
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
  - GO:0097658
  command: /private/tmp/cellstructure-batch62-20261025-siz_24tk/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/membrane_organelle/asi_complex.yaml
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
  - GO:0097658
  evidence_ids:
  - source-go-ancestors
  - source-go
  - source-ipr-IPR013083
  - source-ipr-IPR063277
  - source-protein-P53895
  - source-protein-P53983
  - source-protein-P54074
  - source-tax-4891
  - source-tax-559292
  - source-pmid-25236469
  - source-pmid-25519137
  - source-khmelinskii2014-legacy
  - source-foresti2014-publisher
  - source-foresti2014-ora
  - record-target
  - record-schema
- check_id: final-global-history
  name: Current-base native corpus history
  status: passed
  required: true
  target_ids:
  - GO:0097658
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
  - GO:0097658
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
  - GO:0097658
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
  - GO:0097658
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
  - GO:0097658
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
  - GO:0097658
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
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097658/ancestors?relations=is_a
  locator: Complete ancestor lists; request explicitly restricts relations=is_a.
  accessed_at: '2026-10-25T20:02:46.235593Z'
  support: supports
  summary: 'This is an is_a-only ancestry request. Returned closures: GO:0097658:
    GO:0098796, GO:1902494, GO:1990234, GO:0000152, GO:0140535, GO:0140513, GO:0000151,
    GO:0097658, GO:0032991, GO:0005575. This response does not attest other relation
    types.'
  snapshot_sha256: 46004fbbbc4b213b746159c90fae29d1fb4678ac8fb9391bda85b81c24d15bb4
- evidence_id: source-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000152,GO:0000209,GO:0005637,GO:0006511,GO:0097658,GO:0098796
  locator: 'All returned terms: identifiers, definitions, synonyms, isObsolete and
    typed children relationships.'
  accessed_at: '2026-10-25T20:02:46.234210Z'
  support: supports
  summary: 'Complete requested native GO responses read: GO:0005637 nuclear inner
    membrane; GO:0006511 ubiquitin-dependent protein catabolic process; GO:0098796
    membrane protein complex; GO:0000152 nuclear ubiquitin ligase complex; GO:0097658
    Asi complex; GO:0000209 protein polyubiquitination. Definitions, obsolescence,
    synonyms and typed relationships were checked separately from biological source
    claims.'
  snapshot_sha256: 2f2f39cb47f1285b8335fb5b80fcf409d988f2afa396244d3613baad9807d808
- evidence_id: source-ipr-IPR013083
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013083/
  locator: metadata.accession/name/type, complete descriptions and member signatures.
  accessed_at: '2026-10-25T20:02:46.886334Z'
  support: supports
  summary: 'Native InterPro IPR013083 is named {''name'': ''Zinc finger, RING/FYVE/PHD-type'',
    ''short'': ''Znf_RING/FYVE/PHD''}, with entry type ''homologous_superfamily''.
    Its complete native description and signatures were inspected for the represented
    family/domain scope. This family-entry response does not by itself attest membership
    of a particular UniProt accession.'
  snapshot_sha256: 5c867bf846de6051ed5f4b36e12e85f8122ea244ce99fcaca54e6fa9e7e8f2cc
- evidence_id: source-ipr-IPR063277
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063277/
  locator: metadata.accession/name/type, complete descriptions and member signatures.
  accessed_at: '2026-10-25T20:02:46.906536Z'
  support: supports
  summary: 'Native InterPro IPR063277 is named {''name'': ''Amino acid sensor-independent
    protein 2'', ''short'': ''ASI2''}, with entry type ''family''. Its complete native
    description and signatures were inspected for the represented family/domain scope.
    This family-entry response does not by itself attest membership of a particular
    UniProt accession.'
  snapshot_sha256: 972ba562ee39e2f5a7b152a8d88c9f154e11d90f552ceb5bffbd39851f5f12e5
- evidence_id: source-protein-P53895
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53895.json
  locator: Identity, entryType, proteinDescription, genes, organism, relevant comments
    and InterPro cross-references.
  accessed_at: '2026-10-25T20:02:48.081410Z'
  support: supports
  summary: Native P53895 is UniProtKB reviewed (Swiss-Prot); recommended protein name
    Protein ASI2; primary gene(s) ASI2; organism Saccharomyces cerevisiae (strain
    ATCC 204508 / S288c) (NCBITaxon:559292). Its own InterPro cross-references are
    IPR063277. Relevant function, subunit, subcellular-location and similarity comments
    were read, retaining evidence levels and source context. This protein response
    supplies the member-to-family bridge; a separate family entry does not establish
    that bridge by itself.
  snapshot_sha256: 8a490bb4d8b72b6af65dbd33475fbe63aa08817e159bd3afb187d88df6d6cf22
- evidence_id: source-protein-P53983
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53983.json
  locator: Identity, entryType, proteinDescription, genes, organism, relevant comments
    and InterPro cross-references.
  accessed_at: '2026-10-25T20:02:48.244946Z'
  support: supports
  summary: Native P53983 is UniProtKB reviewed (Swiss-Prot); recommended protein name
    Probable ERAD-associated E3 ubiquitin-protein ligase ASI1; primary gene(s) ASI3;
    organism Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (NCBITaxon:559292).
    Its own InterPro cross-references are IPR013083. Relevant function, subunit, subcellular-location
    and similarity comments were read, retaining evidence levels and source context.
    This protein response supplies the member-to-family bridge; a separate family
    entry does not establish that bridge by itself.
  snapshot_sha256: 3b7d19cb5aa64aeb42345fe0937d89bc3dccb11f0fd7f9b1584b4a4033117909
- evidence_id: source-protein-P54074
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P54074.json
  locator: Identity, entryType, proteinDescription, genes, organism, relevant comments
    and InterPro cross-references.
  accessed_at: '2026-10-25T20:02:48.703149Z'
  support: supports
  summary: Native P54074 is UniProtKB reviewed (Swiss-Prot); recommended protein name
    ERAD-associated E3 ubiquitin-protein ligase ASI1; primary gene(s) ASI1; organism
    Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (NCBITaxon:559292). Its
    own InterPro cross-references are IPR013083. Relevant function, subunit, subcellular-location
    and similarity comments were read, retaining evidence levels and source context.
    This protein response supplies the member-to-family bridge; a separate family
    entry does not establish that bridge by itself.
  snapshot_sha256: 6a63ba3c6767e296a95e35a844e493ce3fb9ea83250a410a961c07e2e171233e
- evidence_id: source-tax-4891
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4891
  locator: 'Complete taxonomy response: taxId, scientificName, rank and lineage.'
  accessed_at: '2026-10-25T20:02:47.491673Z'
  support: supports
  summary: Native taxonomy identifies NCBITaxon:4891 as Saccharomycetes, rank class.
    The response verifies this identifier/name/rank and lineage only, not prevalence
    or an experimental organism assignment.
  snapshot_sha256: 4e24d1f031e5fbdf7700c46cc8394d228571ddac2ae29215981dfc022d3f42ac
- evidence_id: source-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: 'Complete taxonomy response: taxId, scientificName, rank and lineage.'
  accessed_at: '2026-10-25T20:02:47.653012Z'
  support: supports
  summary: Native taxonomy identifies NCBITaxon:559292 as Saccharomyces cerevisiae
    S288C, rank strain. The response verifies this identifier/name/rank and lineage
    only, not prevalence or an experimental organism assignment.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: source-pmid-25236469
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25236469+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native Europe PMC MED identity, title/authors/year/DOI and complete
    abstract where supplied; not a full-body attestation.
  accessed_at: '2026-10-25T20:02:48.981801Z'
  support: supports
  summary: Foresti et al. 2014, DOI10.1126/science.1255638, is the primary Asi inner-nuclear-membrane
    quality-control study. Exact authors/title/DOI and complete native abstract were
    read. The abstract supports an Asi quality-control pathway; the detailed Cdc48,
    RING-mutant, co-purification and strain claims are not certified as read from
    this paper’s unavailable body.
  snapshot_sha256: 092201a93f7a4b00a58fc43d117484e0728e528118338ea98458ff115635f4e2
- evidence_id: source-pmid-25519137
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25519137+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native Europe PMC MED identity, title/authors/year/DOI and complete
    abstract where supplied; not a full-body attestation.
  accessed_at: '2026-10-25T20:02:49.442637Z'
  support: supports
  summary: Khmelinskii et al. 2014, DOI10.1038/nature14096, is the primary mislocalized-protein
    surveillance study. Exact identity and complete abstract match the separately
    read primary body.
  snapshot_sha256: 43ebd4563dd59531786a11ae9ea594aeafab631be1f5f91743d79c3def1af338
- evidence_id: source-khmelinskii2014-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4493439/
  locator: Complete unsectioned scientific main text with Figures1–3 captions; Methods
    sections S2–S13. Primer tables, extended-data captions/pixels and supplementary
    tables not independently inspected.
  accessed_at: '2026-10-25T20:03:08.216355Z'
  support: supports
  summary: The primary main text supports Asi1/Asi3 inner-nuclear-membrane ligase
    roles, Ubc6/Ubc7 interactions, altered substrate stability and Asi2-dependent
    recognition of a subset of tested substrates. The authors present Asi2 recognition
    as an inference from differential substrate effects, not a directly resolved recognition
    structure. Methods specify BY4741/scEB115-derived experimental backgrounds, not
    an undifferentiated reference-strain assay.
  snapshot_sha256: b152e8676a7f52cb982942d3976abcd17b843f64cfc8ad2bb0ead2d1861f402c
- evidence_id: source-foresti2014-publisher
  kind: authority
  reference: https://doi.org/10.1126/science.1255638
  locator: Retained access response only; no scientific body was available through
    this route.
  accessed_at: '2026-10-25T20:03:08.216857Z'
  support: context_only
  summary: The Foresti publisher request returned HTTP403; no scientific body was
    read from this route.
  snapshot_sha256: d5c8d43f87ba2b3022c67d35a3f83f540a0ac8869323d20d3adae57d94abc2f7
- evidence_id: source-foresti2014-ora
  kind: authority
  reference: https://ora.ox.ac.uk/objects/uuid:d529010b-d3f9-48a8-826b-b5d7bb093296
  locator: Institutional record title/authors/publication and access-document links.
  accessed_at: '2026-10-25T20:04:32.969511Z'
  support: context_only
  summary: The Oxford institutional landing page supplies bibliographic metadata and
    a publisher DOI link, not a recovered full scientific body. It is retained for
    access provenance only.
  snapshot_sha256: 3667c9723f12faae24d0724c986272000169be929f1805f33f606e1b05ef82fd
- evidence_id: record-target
  kind: record_content
  reference: data/structures/membrane_organelle/asi_complex.yaml
  locator: Entire frozen maintained YAML, including history, every component/example,
    taxonomy, evidence and graph.
  accessed_at: '2026-10-25T20:10:01.215621Z'
  support: context_only
  summary: The complete maintained target was read and compared claim by claim with
    the scoped sources; this snapshot records the assertions being reviewed rather
    than supplying independent biological confirmation.
  snapshot_sha256: 56c8f96688172f37a0f84d9a6d0932133243ffe331a63247c48d9f51ad168c54
- evidence_id: record-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent grounding/essentiality, ProteinExample, EssentialityEnum
    and PresenceEnum definitions; frozen schema input.
  accessed_at: '2026-10-25T20:10:01.215621Z'
  support: context_only
  summary: Grounding identifies a protein family/class rather than a generic domain.
    Essentiality concerns whether the structure forms without a component, independently
    of function or viability. COMMON means present in most members with losses exceptional;
    it is not redefined as cell-state occurrence.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: check-schema
  kind: validation
  reference: /private/tmp/cellstructure-batch62-20261025-siz_24tk/asi_complex-schema.log
  locator: Complete retained native command output.
  accessed_at: '2026-10-25T19:59:41Z'
  support: supports
  summary: Executed native schema check returned0 for this exact target. This validates
    its bounded syntactic/identifier or coverage scope; it does not prove the biological
    claims.
  snapshot_sha256: e9b38f64e0ab7fe0d0c8312e04491760af11ff8d1eb1b56ad4f807ee3f13ffb1
- evidence_id: check-strict
  kind: validation
  reference: /private/tmp/cellstructure-batch62-20261025-siz_24tk/asi_complex-strict.log
  locator: Complete retained native command output.
  accessed_at: '2026-10-25T19:59:42Z'
  support: supports
  summary: Executed native strict check returned0 for this exact target. This validates
    its bounded syntactic/identifier or coverage scope; it does not prove the biological
    claims.
  snapshot_sha256: f8b240991b714df1f17d8377303b1969c54f2d9d41f23a02fea56e3f19e956b7
- evidence_id: check-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch62-20261025-siz_24tk/asi_complex/causal-graphs.log
  locator: Complete retained native command output.
  accessed_at: '2026-10-25T20:03:42.247607Z'
  support: supports
  summary: Executed native causal-graphs check returned0 for this exact target. This
    validates its bounded syntactic/identifier or coverage scope; it does not prove
    the biological claims.
  snapshot_sha256: 5a59d306198790e5045e71564d6a57c504bc7d559d11e01242b72a719709c1ec
- evidence_id: check-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch62-20261025-siz_24tk/asi_complex/verify.log
  locator: Complete retained native command output.
  accessed_at: '2026-10-25T20:03:43.678706Z'
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
  summary: 'No exact named-organism dataset match: Saccharomyces cerevisiae S288C.
    No listed organism matches the target named species/reference strains. Listing
    absence is not biological negative evidence.'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  search_scope: All28 dataset rows returned by kg-microbe-sources imodulondb datasets;
    exact named-organism matching, not an exhaustive transcriptomics search.
assessments:
- assessment_id: A1
  area: identity
  topic: Asi complex ontology and compartment
  outcome: supported
  summary: Native GO0097658 matches the maintained inner-nuclear-membrane nuclear
    ubiquitin-ligase identity, both parent classes and the INM part-of placement.
    Primary main text independently supports the specialized nuclear-envelope surveillance
    system.
  target_ids:
  - GO:0097658
  evidence_ids:
  - source-go
  - source-go-ancestors
  - source-khmelinskii2014-legacy
  - source-pmid-25236469
- assessment_id: A2
  area: grounding
  topic: Whole-protein identities versus a shared domain fold
  outcome: concern
  summary: IPR013083 is a homologous superfamily covering RING/FYVE/PHD-like small
    domains and related folds. It does not identify the complete Asi1 or Asi3 protein
    class. IPR063277 is an Asi2 family, and the three reviewed UniProt instances have
    the maintained genes and S288C taxon. P53983’s native recommended name itself
    says ASI1 despite the correct ASI3 gene; that naming quirk is not an accession
    mismatch.
  target_ids:
  - GO:0097658
  evidence_ids:
  - source-ipr-IPR013083
  - source-ipr-IPR063277
  - source-protein-P54074
  - source-protein-P53983
  - source-protein-P53895
  - record-schema
- assessment_id: A3
  area: scope
  topic: Taxon label and supported population
  outcome: concern
  summary: NCBITaxon4891 denotes the class Saccharomycetes, whereas the target labels
    it Saccharomycetaceae and repeats a family-level conservation statement. The code
    and stated taxonomic scope must be reconciled. COMMON means majority occurrence
    with exceptional losses, not simply characterized in yeast; neither the native
    taxon identity nor the read single-species experiments establish a census across
    either chosen rank.
  target_ids:
  - GO:0097658
  evidence_ids:
  - source-tax-4891
  - source-tax-559292
  - source-pmid-25236469
  - source-khmelinskii2014-legacy
  - record-schema
- assessment_id: A4
  area: graph
  topic: Substrate ubiquitylation and degradation mechanism
  outcome: supported
  summary: The graph has valid component references and a coherent direction from
    Asi membership through ubiquitylation to degradation. The read primary body supports
    E2 interactions, substrate-dependent turnover and a recognition interpretation
    for Asi2. This positive assessment does not certify the unavailable Foresti-specific
    co-purification, RING-mutant or Cdc48 extraction details; those remain separately
    limited. The duplicated wrong domain grounding is included in F1.
  target_ids:
  - GO:0097658
  evidence_ids:
  - source-khmelinskii2014-legacy
  - source-pmid-25236469
  - source-go
- assessment_id: A5
  area: evidence
  topic: Foresti-specific mechanistic details
  outcome: unknown
  summary: The complete Foresti abstract and Khmelinskii body support the overall
    pathway, but the exact Foresti experiments invoked for Cdc48-dependent extraction,
    essential catalytic RING partners and co-purification were not readable at full-body
    scope. They are not rejected merely because access failed, and are not passed
    as experimentally verified by this review.
  target_ids:
  - GO:0097658
  evidence_ids:
  - source-pmid-25236469
  - source-foresti2014-publisher
  - source-foresti2014-ora
  - source-khmelinskii2014-legacy
- assessment_id: A6
  area: evidence
  topic: Formation necessity and dispensability
  outcome: unknown
  summary: The three DISPENSABLE labels refer to complex formation under the schema.
    Viable deletions, loss of degradation activity and substrate-specific effects
    do not automatically establish formation of the defined complex without each named
    subunit. The inspected experiments support membership and functional differentiation
    but leave universal individual assembly necessity unresolved; no opposite ESSENTIAL
    claim is inferred.
  target_ids:
  - GO:0097658
  evidence_ids:
  - record-schema
  - source-khmelinskii2014-legacy
  - source-pmid-25236469
- assessment_id: A7
  area: completeness
  topic: Scope and experimental exemplars
  outcome: supported
  summary: All maintained fields and three constituent rows were inspected. Native
    S288C entries are valid reference protein instances; the read primary work uses
    specified derivative backgrounds, so the reference-strain label is not taken to
    certify every assay in unmodified S288C. No additional optional inventory or unsearched
    exact Asi1/Asi3 family is asserted.
  target_ids:
  - GO:0097658
  evidence_ids:
  - record-target
  - source-tax-559292
  - source-protein-P54074
  - source-protein-P53983
  - source-protein-P53895
  - source-khmelinskii2014-legacy
findings:
- finding_id: F1
  issue_key: asi-domain-superfamily-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Remove domain-superfamily identity from the Asi1 and Asi3 protein classes
  description: Both whole-protein component rows and their graph nodes use InterProIPR013083
    as identity. The actual native entry is a RING/FYVE/PHD-like homologous superfamily
    of small domains, not a whole Asi1/Asi3 protein family. Presence of such a domain
    in these correct protein examples does not make it an exact molecular-class grounding.
  target_ids:
  - GO:0097658
  field_paths:
  - components[0].grounding
  - components[1].grounding
  - causal_graphs[0].nodes[0].grounding
  - causal_graphs[0].nodes[1].grounding
  evidence_ids:
  - record-target
  - record-schema
  - source-ipr-IPR013083
  - source-protein-P54074
  - source-protein-P53983
  normalization_reason: Major because a broad domain-level fold is asserted as the
    identity of two complete molecular building blocks, contrary to the grounding
    contract.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/asi_complex.yaml
    role: maintained scientific record
- finding_id: F2
  issue_key: asi-taxon-rank-label
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Reconcile Saccharomycetes identifier with the family-level label
  description: The distribution row pairs NCBITaxon4891 with Saccharomycetaceae. Native
    taxonomy identifies4891 as Saccharomycetes, rank class. The adjoining family-level
    conservation statement compounds the rank ambiguity. This finding concerns the
    concrete identifier/label mismatch; it does not infer absence from any lineage.
  target_ids:
  - GO:0097658
  field_paths:
  - taxonomic_distribution[0]
  evidence_ids:
  - record-target
  - source-tax-4891
  normalization_reason: Minor because the complex identity and experimentally supported
    yeast example remain intact; a bounded taxonomy-label and scope correction resolves
    the inconsistency.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/asi_complex.yaml
    role: maintained scientific record
actions:
- action_id: C1
  description: Remove IPR013083 from the two whole-protein identities and graph counterparts.
    Use exact whole-protein family groundings only after verification, otherwise retain
    accurate labels with appropriately qualified grounding status/notes. Keep RING-domain
    information as functional/domain context.
  finding_ids:
  - F1
  target_ids:
  - GO:0097658
  acceptance_checks:
  - Neither Asi1 nor Asi3 whole-protein node is equated to the domain superfamily.
  - Any replacement family is verified at the appropriate whole-protein scope and
    bridged independently to the correct native examples.
  - ASI2IPR063277 and the three correct UniProt identities remain unchanged unless
    separately supported.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/asi_complex.yaml
    role: maintained scientific record
- action_id: C2
  description: Choose the intended taxonomic rank and make its identifier, label and
    conservation wording agree; verify any replacement family identifier and its distribution
    support.
  finding_ids:
  - F2
  target_ids:
  - GO:0097658
  acceptance_checks:
  - NCBITaxon4891 is labeled Saccharomycetes if retained, or a separately verified
    family identifier accompanies Saccharomycetaceae.
  - The presence note does not use an identifier mismatch as evidence of family-wide
    conservation.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/asi_complex.yaml
    role: maintained scientific record
limitations:
- Foresti2014 publisher access returned403 and the institutional landing page was
  metadata only. Its complete native abstract was read, but detailed co-purification,
  RING-mutant, Cdc48 and strain-specific evidence is not certified as full-body read.
- Khmelinskii main text, Figures1–3 captions and MethodsS2–S13 were read; primer tables,
  extended-data/supplement tables and figure pixels were not inspected. Its Asi2-recognition
  interpretation is retained as inference from substrate effects.
- Taxonomic majority occurrence remains unresolved beyond characterized yeast systems;
  this review preserves the precise COMMON schema meaning and does not infer biological
  absence.
- Correct S288C protein references do not attest that every cited experiment used
  unmodified S288C. Individual formation DISPENSABLE claims remain unresolved rather
  than being inferred from viability or loss of quality-control function.
- Corpus identifier resolution includes856 unreachable and252 skipped identifiers
  despite native exit0; BFO authority control was not exercised. These residuals are
  not evidence of absence or scientific validity.
notes: []
```
