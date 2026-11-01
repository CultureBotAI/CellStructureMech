# Source-backed review of dna replication factor a complex

- Review: 20261022T055922Z-dna-replication-factor-a-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:37:20Z
- Finished UTC: 2026-10-22T05:59:22Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One grouped minor exact-family grounding gap for three RPA classes; identity, approximate composition, ssDNA-binding function, taxonomic restriction and descriptive graph are supported with formation necessity left unknown.

## Scope And Provenance

Exactly one complete maintained target and the frozen governing/schema/protein/graph guidance; no scientific conclusion depends on a neighboring maintained record. All scientific fields and source claims are assessed at the explicitly inspected tiers.

Selection: Batch51 fixed strict path order, index 4; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005662 | data/structures/other/dna_replication_factor_a_complex.yaml | maintained | DNA replication factor A complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005662 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005662 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0005662 | Focused check passed; biological scope assessed independently. |
| Focused native verify | passed | True | GO:0005662 | Focused check passed; biological scope assessed independently. |
| Claim-level scientific review | passed | True | GO:0005662 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005662 | 4 of 5 collected target identifiers returned OK. PMID:9242902: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005662 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005662 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005662 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005662 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005662 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Conserved heterotrimeric RPA identity

identity: supported. Targets: GO:0005662.

Exact GO identity, RPA/replication protein A synonyms, nuclear-complex hierarchy, approximate size classes and nonspecific ssDNA-binding function are supported. Approximate30kDa versus the RPA32 family name does not denote a different constituent; native yeast example masses also vary. No species accession is used as the generic class grounding.

### Three actionable exact subunit family mappings

grounding: concern. Targets: GO:0005662.

The existing classes are precisely represented by IPR004591/014646/013970, with independent reviewed-protein cross-references. The current REVIEWED_LABEL_ONLY state and OPEN grounding task can be resolved without adding gene symbols or protein examples. Historical wording that no term was curated in that pass is not declared false.

### Formation necessity remains appropriately unknown

grounding: unknown. Targets: GO:0005662.

All three component essentialities are UNKNOWN. Heterotrimeric identity, DNA-binding function and broad biological requirement do not independently establish an assay of formation without each constituent.

### Four-edge descriptive function graph

graph: supported. Targets: GO:0005662.

The three constituent-to-complex edges and complex-to-ssDNA-binding edge are supported at the GO/secondary synthesis tier. Explicit NONMECHANISTIC scope correctly avoids claiming interfaces or an assembly/repair mechanism.

### Taxon identity, majority semantics and experimental boundaries

scope: supported. Targets: GO:0005662.

Eukaryota identity and only-in restriction agree with the conserved RPA authority. COMMON retains its schema meaning present in most members with exceptional losses. The sources provide qualitative conservation/system support rather than a measured prevalence census; no artificial census requirement is imposed.

### Whole-target coverage with bounded unresolved enrichment

completeness: supported. Targets: GO:0005662.

The complete maintained target, each source claim, graph edge, component state, protein example, discussion and history was assessed. Exact actionable class mappings are distinguished from unresolved broader/domain candidates and optional enrichment. Existing historical access/curation notes are not judged false merely because this review recovered additional sources.

## Findings

### F1: Resolve verified exact subunit family grounding

minor / open / confirmed; issue key: dna-replication-factor-a-complex-exact-family-grounding.

The three existing RPA size-defined protein classes have exact source-neutral whole-protein families:70kDa IPR004591, approximately30/32kDa IPR014646 and14kDa IPR013970. Native family type/name/signatures plus independent reviewed RFA1/2/3 xrefs establish the matches. The narrower yeast Rfa3 subgroup is not substituted for the generic14kDa class. Historical statements about what was curated in an earlier pass are preserved as history, not declared fabricated.

## Recommended Actions And Acceptance Checks

### A1

Ground the verified classes to IPR004591/014646/013970 with source-backed family evidence and update the corresponding open task/status. Preserve unresolved classes and historical provenance; keep organism accessions as examples.

- Each added family denotes the existing whole-protein class rather than a domain, broader homolog group or species accession.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dna_replication_factor_a_complex.yaml; Entire maintained target, all component/protein evidence, graph nodes/edges, discussion and history | context_only | All current claims were read in full; no neighboring record judgment is imported. |
| curation | docs/CURATION.md; Components: class grounding, REVIEWED_LABEL_ONLY and formation necessity | context_only | An exact family grounds a protein class, whereas a species accession is an example. REVIEWED_LABEL_ONLY means no exact term exists after review. Essentiality concerns formation of the structure, not viability or catalytic function. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, PresenceEnum and graph scope | context_only | COMMON means present in most taxon members with exceptional losses; it is not merely an occurrence label. UNKNOWN preserves unestablished formation necessity. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Topology versus mechanism and edge-level evidence | context_only | Membership, compartment placement and generic process membership do not themselves encode an experimentally supported assembly mechanism. |
| micro51-go-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662,GO:0005663,GO:0031261,GO:0140513,GO:0032991,GO:0032993,GO:0005654,GO:0005657,GO:0003689,GO:0003697,GO:0006260,GO:0042555,GO:0000811; Thirteen-term response: exact target definition/xrefs/status/synonyms, relevant parent/compartment typed children and declared function/component terms. Unrelated child inventory is not treated as biological evidence. | supports | Active GO0005662 is the heterotrimeric eukaryotic RPA complex with approximately70/30/14kDa classes and nonspecific ssDNA binding. Exact synonyms and PMID9242902 definition xref agree; GO0140513 typed children confirm the nuclear protein-containing-complex parent, and GO0003697 identifies the declared function. |
| micro51-GO0005662-ancestors-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662/ancestors?relations=is_a; Exact target query with relations=is_a; complete ancestor IDs inspected. No part_of relation is inferred from this ancestry list. | supports | The is_a-only native ancestor response confirms the target’s nuclear protein-containing-complex hierarchy. |
| micro51-GO0005662-constraints-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662/constraints; Exact taxonConstraints array only; inherited annotation blacklist is not used for occurrence or composition. | supports | The exact constraint is only_in_taxon Eukaryota2759. Taxon restrictions do not establish a prevalence census. |
| micro51-tax2759-network | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete taxId/scientificName/rank/lineage/otherNames native response. | supports | ENA taxId2759 is Eukaryota, rank domain. |
| micro51-pmid-9242902-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9242902%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED record: full title/authors/year/PMID/DOI and complete abstractText. Main-body evidence, where actually read, is recorded separately. | supports | Wold1997, Replication protein A: a heterotrimeric, single-stranded DNA-binding protein required for eukaryotic DNA metabolism, DOI10.1146/annurev.biochem.66.1.61. Its complete review abstract supports the conserved heterotrimeric RPA context; it is not a directly inspected primary experiment. |
| micro51-ipr-IPR004591 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004591/; Complete native metadata name/type/accession/descriptions and member_databases. Background prose is not promoted to new mechanistic evidence. | supports | Native IPR004591 identifies the whole-protein RPA70/Rfa1 class. Family with full-protein TIGR00617 signature. This entry supplies family identity/type/signature evidence; individual protein membership is verified in separate UniProt responses. |
| micro51-ipr-IPR014646 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014646/; Complete native metadata name/type/accession/descriptions and member_databases. Background prose is not promoted to new mechanistic evidence. | supports | Native IPR014646 identifies the whole-protein RPA32/Rfa2 class. Family with PIRSF036949 signature; broader IPR040260 includes other classes and is not substituted. This entry supplies family identity/type/signature evidence; individual protein membership is verified in separate UniProt responses. |
| micro51-ipr-IPR013970 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013970/; Complete native metadata name/type/accession/descriptions and member_databases. Background prose is not promoted to new mechanistic evidence. | supports | Native IPR013970 identifies the whole-protein RPA14/Rfa3 class. Family with PF08661 signature; IPR016588 is a narrower Saccharomycetes subgroup, not the generic target class. This entry supplies family identity/type/signature evidence; individual protein membership is verified in separate UniProt responses. |
| micro51-gene-RFA1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Exact reviewed taxonomy_id559292/gene query; entire returned identity, names, gene/taxon, InterPro xrefs and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments. | supports | The bounded reviewed S288C exact-gene query returns P22336 for RFA1, with native InterPro xref IPR004591. Identity, FUNCTION/SUBUNIT and nuclear location comments were read; by-similarity qualifications remain intact. This independently corroborates the class mapping and does not require adding an optional instance to the record. |
| micro51-gene-RFA2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA2%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Exact reviewed taxonomy_id559292/gene query; entire returned identity, names, gene/taxon, InterPro xrefs and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments. | supports | The bounded reviewed S288C exact-gene query returns P26754 for RFA2, with native InterPro xref IPR014646. Identity, FUNCTION/SUBUNIT and nuclear location comments were read; by-similarity qualifications remain intact. This independently corroborates the class mapping and does not require adding an optional instance to the record. |
| micro51-gene-RFA3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA3%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Exact reviewed taxonomy_id559292/gene query; entire returned identity, names, gene/taxon, InterPro xrefs and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments. | supports | The bounded reviewed S288C exact-gene query returns P26755 for RFA3, with native InterPro xref IPR013970. Identity, FUNCTION/SUBUNIT and nuclear location comments were read; by-similarity qualifications remain intact. This independently corroborates the class mapping and does not require adding an optional instance to the record. |
| micro51-wold1997-publisher | https://doi.org/10.1146/annurev.biochem.66.1.61; Actual status403 plus captured response bytes. | context_only | The retained publisher request returned HTTP403 challenge content, not a review main body. |
| schema-result | just validate data/structures/other/dna_replication_factor_a_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dna_replication_factor_a_complex.yaml |
| strict-result | just validate-strict data/structures/other/dna_replication_factor_a_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_a_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dna_replication_factor_a_complex.yaml --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_a_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_a_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_a_complex.yaml --causal-graphs; Complete focused read-only native causal-graphs report | supports | data/structures/other/dna_replication_factor_a_complex.yaml  (GO:0005662)<br>  rpa_single_stranded_dna_binding	rpa_70_kda_subunit	NO_GENE_SYMBOLS	-&gt;rpa_70_kda_subunit (PROTEIN: RPA 70 kDa subunit)<br>  rpa_single_stranded_dna_binding	rpa_30_kda_subunit	NO_GENE_SYMBOLS	-&gt;rpa_30_kda_subunit (PROTEIN: RPA 30 kDa subunit)<br>  rpa_single_stranded_dna_binding	rpa_14_kda_subunit	NO_GENE_SYMBOLS	-&gt;rpa_14_kda_subunit (PROTEIN: RPA 14 kDa subunit)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_a_complex.yaml --verify; Complete focused read-only native verify report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dna_replication_factor_a_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 4 of 5 collected target identifiers returned OK. PMID:9242902: UNREACHABLE; Exact native EuropePMC MED identifier, title and DOI independently inspected after the bulk eutils414 transport failure. Identifier resolution does not certify all biological claims; declared primary-body and abstract reading limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Wold1997 was read only as complete native abstract and bibliographic metadata; the publisher route returned403 challenge content. No primary RPA reconstitution experiment, image pixels or supplement was inspected.
- The three RPA protein queries are mapping corroboration, not a mandatory example inventory or proof of every modern mechanism mentioned in their comments.
- Native initial DNS failures and successful network retries are retained separately. An HTTP200 redirect, download challenge or abstract landing page is never treated as full scientific text.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user requests one review for every unreviewed record, including qualified clean records.
- Native UniProt/ontology/family adapters directly address these eukaryotic complex claims. No matched iModulonDB organism/dataset is established or used; expression-module evidence would not prove physical assembly.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T055922Z-dna-replication-factor-a-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of dna replication factor a complex
started_at: '2026-10-22T05:37:20Z'
finished_at: '2026-10-22T05:59:22Z'
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
summary: One grouped minor exact-family grounding gap for three RPA classes; identity,
  approximate composition, ssDNA-binding function, taxonomic restriction and descriptive
  graph are supported with formation necessity left unknown.
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
  - path: data/structures/other/dna_replication_factor_a_complex.yaml
    sha256: a3cfb2654e3e82b6d841247eb4580f288e2bb1d082ff6d5a06ae5f363019f7a9
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
- target_id: GO:0005662
  path: data/structures/other/dna_replication_factor_a_complex.yaml
  label: DNA replication factor A complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_a_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target and the frozen governing/schema/protein/graph
    guidance; no scientific conclusion depends on a neighboring maintained record.
    All scientific fields and source claims are assessed at the explicitly inspected
    tiers.
  selection: Batch51 fixed strict path order, index 4; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005662
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005662
  command: just validate data/structures/other/dna_replication_factor_a_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005662
  command: just validate-strict data/structures/other/dna_replication_factor_a_complex.yaml
    --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_a_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005662
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_a_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; biological scope assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0005662
  command: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_a_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; biological scope assessed independently.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005662
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro51-go-network
  - micro51-GO0005662-ancestors-network
  - micro51-GO0005662-constraints-network
  - micro51-tax2759-network
  - micro51-pmid-9242902-network
  - micro51-ipr-IPR004591
  - micro51-ipr-IPR014646
  - micro51-ipr-IPR013970
  - micro51-gene-RFA1
  - micro51-gene-RFA2
  - micro51-gene-RFA3
  - micro51-wold1997-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005662
  summary: '4 of 5 collected target identifiers returned OK. PMID:9242902: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro51-pmid-9242902-network
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005662
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
  - GO:0005662
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
  - GO:0005662
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
  - GO:0005662
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
  - GO:0005662
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
  reference: data/structures/other/dna_replication_factor_a_complex.yaml
  locator: Entire maintained target, all component/protein evidence, graph nodes/edges,
    discussion and history
  accessed_at: '2026-10-22T05:50:39Z'
  support: context_only
  summary: All current claims were read in full; no neighboring record judgment is
    imported.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: class grounding, REVIEWED_LABEL_ONLY and formation necessity'
  accessed_at: '2026-10-22T05:50:39Z'
  support: context_only
  summary: An exact family grounds a protein class, whereas a species accession is
    an example. REVIEWED_LABEL_ONLY means no exact term exists after review. Essentiality
    concerns formation of the structure, not viability or catalytic function.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, PresenceEnum and graph scope
  accessed_at: '2026-10-22T05:50:39Z'
  support: context_only
  summary: COMMON means present in most taxon members with exceptional losses; it
    is not merely an occurrence label. UNKNOWN preserves unestablished formation necessity.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Topology versus mechanism and edge-level evidence
  accessed_at: '2026-10-22T05:50:39Z'
  support: context_only
  summary: Membership, compartment placement and generic process membership do not
    themselves encode an experimentally supported assembly mechanism.
- evidence_id: micro51-go-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662,GO:0005663,GO:0031261,GO:0140513,GO:0032991,GO:0032993,GO:0005654,GO:0005657,GO:0003689,GO:0003697,GO:0006260,GO:0042555,GO:0000811
  locator: 'Thirteen-term response: exact target definition/xrefs/status/synonyms,
    relevant parent/compartment typed children and declared function/component terms.
    Unrelated child inventory is not treated as biological evidence.'
  accessed_at: '2026-10-22T05:41:53.028093Z'
  support: supports
  summary: Active GO0005662 is the heterotrimeric eukaryotic RPA complex with approximately70/30/14kDa
    classes and nonspecific ssDNA binding. Exact synonyms and PMID9242902 definition
    xref agree; GO0140513 typed children confirm the nuclear protein-containing-complex
    parent, and GO0003697 identifies the declared function.
  snapshot_sha256: aa2de8390a1ee6ed65c370de3a77e03161506b64eace1416883667eb013d002e
- evidence_id: micro51-GO0005662-ancestors-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662/ancestors?relations=is_a
  locator: Exact target query with relations=is_a; complete ancestor IDs inspected.
    No part_of relation is inferred from this ancestry list.
  accessed_at: '2026-10-22T05:41:50.543362Z'
  support: supports
  summary: The is_a-only native ancestor response confirms the target’s nuclear protein-containing-complex
    hierarchy.
  snapshot_sha256: 1d9a896b3c2c8a7add410c4c1fa031b8c6677686f0fe92676022479510431a61
- evidence_id: micro51-GO0005662-constraints-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662/constraints
  locator: Exact taxonConstraints array only; inherited annotation blacklist is not
    used for occurrence or composition.
  accessed_at: '2026-10-22T05:41:50.543794Z'
  support: supports
  summary: The exact constraint is only_in_taxon Eukaryota2759. Taxon restrictions
    do not establish a prevalence census.
  snapshot_sha256: 3e03b6425e2a7ecab10a7e02aa60db8121ced5b6d31ebc212d8f88725c2c4952
- evidence_id: micro51-tax2759-network
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete taxId/scientificName/rank/lineage/otherNames native response.
  accessed_at: '2026-10-22T05:41:56.211399Z'
  support: supports
  summary: ENA taxId2759 is Eukaryota, rank domain.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: micro51-pmid-9242902-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9242902%20AND%20SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED record: full title/authors/year/PMID/DOI and complete abstractText.
    Main-body evidence, where actually read, is recorded separately.'
  accessed_at: '2026-10-22T05:41:55.210800Z'
  support: supports
  summary: 'Wold1997, Replication protein A: a heterotrimeric, single-stranded DNA-binding
    protein required for eukaryotic DNA metabolism, DOI10.1146/annurev.biochem.66.1.61.
    Its complete review abstract supports the conserved heterotrimeric RPA context;
    it is not a directly inspected primary experiment.'
  snapshot_sha256: eb3fa664c6bd1dad77de7af95e759a74bbe7ca6aec547990bf91b56f80dd4353
- evidence_id: micro51-ipr-IPR004591
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004591/
  locator: Complete native metadata name/type/accession/descriptions and member_databases.
    Background prose is not promoted to new mechanistic evidence.
  accessed_at: '2026-10-22T05:44:01.249708Z'
  support: supports
  summary: Native IPR004591 identifies the whole-protein RPA70/Rfa1 class. Family
    with full-protein TIGR00617 signature. This entry supplies family identity/type/signature
    evidence; individual protein membership is verified in separate UniProt responses.
  snapshot_sha256: 76b40296040dc3366ab7f658ee76399d1bfa7318da5a079ac9e43c593a03fa4f
- evidence_id: micro51-ipr-IPR014646
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014646/
  locator: Complete native metadata name/type/accession/descriptions and member_databases.
    Background prose is not promoted to new mechanistic evidence.
  accessed_at: '2026-10-22T05:44:01.249876Z'
  support: supports
  summary: Native IPR014646 identifies the whole-protein RPA32/Rfa2 class. Family
    with PIRSF036949 signature; broader IPR040260 includes other classes and is not
    substituted. This entry supplies family identity/type/signature evidence; individual
    protein membership is verified in separate UniProt responses.
  snapshot_sha256: e9df1d9b162d769daf0d3d97fecbaabf3f3152db6cb8ee07c9a11369095f387f
- evidence_id: micro51-ipr-IPR013970
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013970/
  locator: Complete native metadata name/type/accession/descriptions and member_databases.
    Background prose is not promoted to new mechanistic evidence.
  accessed_at: '2026-10-22T05:44:01.249999Z'
  support: supports
  summary: Native IPR013970 identifies the whole-protein RPA14/Rfa3 class. Family
    with PF08661 signature; IPR016588 is a narrower Saccharomycetes subgroup, not
    the generic target class. This entry supplies family identity/type/signature evidence;
    individual protein membership is verified in separate UniProt responses.
  snapshot_sha256: 594508b691b6fc97c2ca6d1beb10fb5996aaa7c468f730873c4e4d02f7bbc7a2
- evidence_id: micro51-gene-RFA1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Exact reviewed taxonomy_id559292/gene query; entire returned identity,
    names, gene/taxon, InterPro xrefs and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments.
  accessed_at: '2026-10-22T05:43:08.188952Z'
  support: supports
  summary: The bounded reviewed S288C exact-gene query returns P22336 for RFA1, with
    native InterPro xref IPR004591. Identity, FUNCTION/SUBUNIT and nuclear location
    comments were read; by-similarity qualifications remain intact. This independently
    corroborates the class mapping and does not require adding an optional instance
    to the record.
  snapshot_sha256: 8c2fe65f740f70e9fd298baac32dd53a42217d897ee00182b104a29fa5b8519a
- evidence_id: micro51-gene-RFA2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA2%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Exact reviewed taxonomy_id559292/gene query; entire returned identity,
    names, gene/taxon, InterPro xrefs and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments.
  accessed_at: '2026-10-22T05:43:08.653626Z'
  support: supports
  summary: The bounded reviewed S288C exact-gene query returns P26754 for RFA2, with
    native InterPro xref IPR014646. Identity, FUNCTION/SUBUNIT and nuclear location
    comments were read; by-similarity qualifications remain intact. This independently
    corroborates the class mapping and does not require adding an optional instance
    to the record.
  snapshot_sha256: 4f1cb7721a54564cc98d6b67c540fdce864cee0eb6143552ccf7c1720572ea5f
- evidence_id: micro51-gene-RFA3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA3%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Exact reviewed taxonomy_id559292/gene query; entire returned identity,
    names, gene/taxon, InterPro xrefs and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments.
  accessed_at: '2026-10-22T05:43:08.827286Z'
  support: supports
  summary: The bounded reviewed S288C exact-gene query returns P26755 for RFA3, with
    native InterPro xref IPR013970. Identity, FUNCTION/SUBUNIT and nuclear location
    comments were read; by-similarity qualifications remain intact. This independently
    corroborates the class mapping and does not require adding an optional instance
    to the record.
  snapshot_sha256: 49c4cd5589604dc7e1bf6f22536bd4a4530a8aefae36bc90b625396d76de3d0a
- evidence_id: micro51-wold1997-publisher
  kind: database
  reference: https://doi.org/10.1146/annurev.biochem.66.1.61
  locator: Actual status403 plus captured response bytes.
  accessed_at: '2026-10-22T05:42:48.434702Z'
  support: context_only
  summary: The retained publisher request returned HTTP403 challenge content, not
    a review main body.
  snapshot_sha256: 4b1b1d39c74c3569e6ff00ffd6acd584d2cfd08cd32629ce3d45b6f10af463d9
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dna_replication_factor_a_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:22Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dna_replication_factor_a_complex.yaml'
  snapshot_sha256: 4536651c206aaab2829ca071cd467abb0afa56bf696843bfcaab0d3cd81315b7
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dna_replication_factor_a_complex.yaml
    --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_a_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:37:24Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dna_replication_factor_a_complex.yaml\
    \ --out /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_a_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch51-20261022-jny4s18h/dna_replication_factor_a_complex-strict.tsv"
  snapshot_sha256: ecb8f680cd640be396243c5e1027a44338da27ba35ebdd9688cfc5b7554f5948
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_a_complex.yaml
    --causal-graphs
  locator: Complete focused read-only native causal-graphs report
  accessed_at: '2026-10-22T05:43:01.798277Z'
  support: supports
  summary: "data/structures/other/dna_replication_factor_a_complex.yaml  (GO:0005662)\n\
    \  rpa_single_stranded_dna_binding\trpa_70_kda_subunit\tNO_GENE_SYMBOLS\t->rpa_70_kda_subunit\
    \ (PROTEIN: RPA 70 kDa subunit)\n  rpa_single_stranded_dna_binding\trpa_30_kda_subunit\t\
    NO_GENE_SYMBOLS\t->rpa_30_kda_subunit (PROTEIN: RPA 30 kDa subunit)\n  rpa_single_stranded_dna_binding\t\
    rpa_14_kda_subunit\tNO_GENE_SYMBOLS\t->rpa_14_kda_subunit (PROTEIN: RPA 14 kDa\
    \ subunit)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: fbd1529fce32834b71ee0b84e66e7977798e995a51cc7abcd9f4a3338bc57335
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch51-20261022-jny4s18h/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_a_complex.yaml
    --verify
  locator: Complete focused read-only native verify report
  accessed_at: '2026-10-22T05:43:02.825207Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dna_replication_factor_a_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '4 of 5 collected target identifiers returned OK. PMID:9242902: UNREACHABLE;
    Exact native EuropePMC MED identifier, title and DOI independently inspected after
    the bulk eutils414 transport failure. Identifier resolution does not certify all
    biological claims; declared primary-body and abstract reading limits remain in
    force. Native source checks are separately scoped; skipped or unreachable identifiers
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
  topic: Conserved heterotrimeric RPA identity
  outcome: supported
  target_ids:
  - GO:0005662
  summary: Exact GO identity, RPA/replication protein A synonyms, nuclear-complex
    hierarchy, approximate size classes and nonspecific ssDNA-binding function are
    supported. Approximate30kDa versus the RPA32 family name does not denote a different
    constituent; native yeast example masses also vary. No species accession is used
    as the generic class grounding.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005662-ancestors-network
  - micro51-GO0005662-constraints-network
  - micro51-tax2759-network
  - micro51-pmid-9242902-network
  - micro51-ipr-IPR004591
  - micro51-ipr-IPR014646
  - micro51-ipr-IPR013970
  - micro51-gene-RFA1
  - micro51-gene-RFA2
  - micro51-gene-RFA3
- assessment_id: grounding
  area: grounding
  topic: Three actionable exact subunit family mappings
  outcome: concern
  target_ids:
  - GO:0005662
  summary: The existing classes are precisely represented by IPR004591/014646/013970,
    with independent reviewed-protein cross-references. The current REVIEWED_LABEL_ONLY
    state and OPEN grounding task can be resolved without adding gene symbols or protein
    examples. Historical wording that no term was curated in that pass is not declared
    false.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005662-ancestors-network
  - micro51-GO0005662-constraints-network
  - micro51-tax2759-network
  - micro51-ipr-IPR004591
  - micro51-ipr-IPR014646
  - micro51-ipr-IPR013970
  - micro51-gene-RFA1
  - micro51-gene-RFA2
  - micro51-gene-RFA3
- assessment_id: formation
  area: grounding
  topic: Formation necessity remains appropriately unknown
  outcome: unknown
  target_ids:
  - GO:0005662
  summary: All three component essentialities are UNKNOWN. Heterotrimeric identity,
    DNA-binding function and broad biological requirement do not independently establish
    an assay of formation without each constituent.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005662-ancestors-network
  - micro51-GO0005662-constraints-network
  - micro51-tax2759-network
  - micro51-pmid-9242902-network
- assessment_id: topology
  area: graph
  topic: Four-edge descriptive function graph
  outcome: supported
  target_ids:
  - GO:0005662
  summary: The three constituent-to-complex edges and complex-to-ssDNA-binding edge
    are supported at the GO/secondary synthesis tier. Explicit NONMECHANISTIC scope
    correctly avoids claiming interfaces or an assembly/repair mechanism.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005662-ancestors-network
  - micro51-GO0005662-constraints-network
  - micro51-tax2759-network
  - micro51-pmid-9242902-network
  - graphs
- assessment_id: taxonomic-scope
  area: scope
  topic: Taxon identity, majority semantics and experimental boundaries
  outcome: supported
  target_ids:
  - GO:0005662
  summary: Eukaryota identity and only-in restriction agree with the conserved RPA
    authority. COMMON retains its schema meaning present in most members with exceptional
    losses. The sources provide qualitative conservation/system support rather than
    a measured prevalence census; no artificial census requirement is imposed.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005662-ancestors-network
  - micro51-GO0005662-constraints-network
  - micro51-tax2759-network
  - micro51-pmid-9242902-network
- assessment_id: coverage
  area: completeness
  topic: Whole-target coverage with bounded unresolved enrichment
  outcome: supported
  target_ids:
  - GO:0005662
  summary: The complete maintained target, each source claim, graph edge, component
    state, protein example, discussion and history was assessed. Exact actionable
    class mappings are distinguished from unresolved broader/domain candidates and
    optional enrichment. Existing historical access/curation notes are not judged
    false merely because this review recovered additional sources.
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005662-ancestors-network
  - micro51-GO0005662-constraints-network
  - micro51-tax2759-network
  - micro51-pmid-9242902-network
  - micro51-ipr-IPR004591
  - micro51-ipr-IPR014646
  - micro51-ipr-IPR013970
  - micro51-gene-RFA1
  - micro51-gene-RFA2
  - micro51-gene-RFA3
findings:
- finding_id: F1
  issue_key: dna-replication-factor-a-complex-exact-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve verified exact subunit family grounding
  description: The three existing RPA size-defined protein classes have exact source-neutral
    whole-protein families:70kDa IPR004591, approximately30/32kDa IPR014646 and14kDa
    IPR013970. Native family type/name/signatures plus independent reviewed RFA1/2/3
    xrefs establish the matches. The narrower yeast Rfa3 subgroup is not substituted
    for the generic14kDa class. Historical statements about what was curated in an
    earlier pass are preserved as history, not declared fabricated.
  target_ids:
  - GO:0005662
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - components[2].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - schema
  - micro51-go-network
  - micro51-GO0005662-ancestors-network
  - micro51-GO0005662-constraints-network
  - micro51-tax2759-network
  - micro51-ipr-IPR004591
  - micro51-ipr-IPR014646
  - micro51-ipr-IPR013970
  - micro51-gene-RFA1
  - micro51-gene-RFA2
  - micro51-gene-RFA3
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_a_complex.yaml
    role: maintained scientific record
  rule_id: Claim-level evidence, exact class grounding and local formation/graph contracts
  native_severity: minor
  normalization_reason: The biological class, composition and protein identities remain
    correct. This is a bounded actionable class-grounding gap under the explicit REVIEWED_LABEL_ONLY
    contract, not a missing optional example inventory.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005662
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_a_complex.yaml
    role: maintained scientific record
  description: Ground the verified classes to IPR004591/014646/013970 with source-backed
    family evidence and update the corresponding open task/status. Preserve unresolved
    classes and historical provenance; keep organism accessions as examples.
  acceptance_checks:
  - Each added family denotes the existing whole-protein class rather than a domain,
    broader homolog group or species accession.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- Wold1997 was read only as complete native abstract and bibliographic metadata; the
  publisher route returned403 challenge content. No primary RPA reconstitution experiment,
  image pixels or supplement was inspected.
- The three RPA protein queries are mapping corroboration, not a mandatory example
  inventory or proof of every modern mechanism mentioned in their comments.
- Native initial DNS failures and successful network retries are retained separately.
  An HTTP200 redirect, download challenge or abstract landing page is never treated
  as full scientific text.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user requests one review for every unreviewed record, including qualified clean
  records.
- Native UniProt/ontology/family adapters directly address these eukaryotic complex
  claims. No matched iModulonDB organism/dataset is established or used; expression-module
  evidence would not prove physical assembly.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
