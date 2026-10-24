# Cellular bud-neck septin-collar evidence and family-grounding review

- Review: 20261020T073445Z-cellular-bud-neck-septin-collar-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-20T07:29:54Z
- Finished UTC: 2026-10-20T07:34:45Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact collar identity, boundaries, topology and five protein examples are supported. One minor finding concerns withholding a verified taxon-agnostic Septin family mapping on an overly localized criterion.

## Scope And Provenance

Entire maintained record, native GO/UniProt/InterPro/taxonomy, cited bibliographic identities and abstracts, and relevant full-text sections of the cited2005 author review.

Selection: Third remaining unreviewed path in batch5, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032174 | data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml | maintained | cellular bud neck septin collar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032174 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032174 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0032174 | 14 identifiers OK; 3 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0032174 | No expression-module mechanism is asserted. Native sequence annotations and the cited localization/scaffold sources address these claims. |
| Claim-level scientific review | passed | True | GO:0032174 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0032174 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032174 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032174 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032174 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0032174 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact collar structure

identity: supported. Targets: GO:0032174.

GO identity and definition match the localized hourglass structure, distinct from both initial ring and split rings.

### Subtype and containing region

grounding: supported. Targets: GO:0032174.

Native GO confirms septin-collar subtype and bud-neck parthood.

### Septin class and structural necessity

evidence: supported. Targets: GO:0032174.

The named septins form the collar; class-level ESSENTIAL concerns forming a septin structure, not essentiality of every paralog or cell viability. The record does not impose a five-subunit stoichiometry.

### Five reference examples and their localization citations

provenance: supported. Targets: GO:0032174.

All five native accession/gene/name/status/taxon pairs match. The example evidence notes accurately report UniProt localization provenance; Huh survey membership was checked at the native annotation level, not inferred from its broad abstract.

### Family identity versus localized role

grounding: concern. Targets: GO:0032174.

The label-only rationale applies a localized fungal cohort restriction to a taxon-agnostic component. Verified IPR016491 matches the named Septin family and all five examples; IPR030379 is only a domain. The family mapping and discussion should be updated.

### Budding-yeast canonical example

scope: supported. Targets: GO:0032174.

The primary abstract supports the species and reporter context. COMMON represents ordinary cell-cycle occurrence rather than quantified prevalence; S288C examples do not assert every experiment used that strain.

### Bud-neck scaffold beyond cytokinesis

evidence: supported. Targets: GO:0032174.

GO and the author review support scaffolding; the primary abstract supports Bni4/Kcc4 asymmetric organization. The function does not claim these associated proteins are collar constituents.

### Nonmechanistic ring-to-collar topology

graph: supported. Targets: GO:0032174.

Assembly into the collar, initial-ring rearrangement and bud-neck placement are supported at the declared coarse level. No full recruitment mechanism is inferred.

### Scope and maintained status

completeness: supported. Targets: GO:0032174.

PROPOSED and the state-boundary discussion are appropriate. The family-grounding TODO has an actionable verified resolution; accessory census and measurements are not required by the stated scope.

## Findings

### F1: Label-only rationale confuses family identity with collar-localized scope

minor / open / confirmed; issue key: cellular-bud-neck-septin-collar-family-grounding-scope.

The component is labeled septin proteins, but grounding_notes withholds a family because it seeks the complete localized fungal collar cohort. Native IPR016491 denotes the Septin family and is annotated on all five verified examples. Repository policy assigns taxon-agnostic family identity to components; localization belongs in role and evidence. Retaining REVIEWED_LABEL_ONLY on this rationale leaves a resolvable family mapping and a stale TODO.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, ground the septin protein class to verified IPR016491, reconcile the grounding status/notes and resolve the exact-family TODO. Preserve the localized role, reference examples and their evidence.

- Family label and accession agree with native InterPro and all five example cross-references.
- Grounding no longer requires the family term to encode collar localization or fungal restriction.
- Run native schema, strict, product-label, history and generated-page checks after curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| collar-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032174,GO:0032173,GO:0005935,GO:0000144,GO:0032177; Native term definitions and child relations | supports | All five GO terms are active. The target definition is exact; GO0032173 lists the target as is_a and GO0005935 lists it as part_of. Initial ring and split-ring definitions distinguish the surrounding cell-cycle states. |
| collar-proteins | https://rest.uniprot.org/uniprotkb/search?query=(gene_exact:CDC3%20OR%20gene_exact:CDC10%20OR%20gene_exact:CDC11%20OR%20gene_exact:CDC12%20OR%20gene_exact:SHS1)%20AND%20organism_id:559292%20AND%20reviewed:true&amp;format=json; Complete five-result native query; genes, names, organism, localization evidence and InterPro cross-references | supports | The exact-gene, reviewed S288C query returns five entries: P32457 CDC3, P25342 CDC10, P32458 CDC11, P32468 CDC12 and Q07657 SHS1. Names, status and taxon match. Native localization evidence links match every PMID/ECO statement in the examples. All five entries cross-reference IPR016491. |
| collar-IPR016491 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; Native family type, name and scope | supports | IPR016491 is the Septin family, spanning yeast and animals. Its native description explicitly includes the five named budding-yeast septins. This family grounds the taxon-agnostic component class; it need not be restricted to collar-localized proteins. |
| collar-IPR030379 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030379/; Native type and scope | supports | IPR030379 is the septin G domain rather than the whole protein family. It is not the proposed family mapping. |
| collar-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1091/mbc.E04-09-0764%20OR%20DOI:10.1016/j.tcb.2005.06.007%20OR%20EXT_ID:14562095%20OR%20EXT_ID:25971666%20OR%20EXT_ID:9790978&amp;format=json&amp;resultType=core; Five bibliographic records and inspected abstracts | supports | Exact records verify the two cited DOIs and three example PMIDs. Kozubowski2005 abstract directly states ring-to-collar rearrangement and Bni4/Kcc4 asymmetry. Mino1998 abstract describes Shs1 bud-neck localization; Finnigan2015 abstract describes Cdc11/Shs1-dependent recruitment. Huh2003 abstract establishes the survey but does not resolve individual proteins. |
| ring-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=4932,559292; Native species and strain taxonomy records | supports | NCBI identifies4932 as Saccharomyces cerevisiae and559292 as its S288C strain. |
| review-text | https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/; Versele and Thorner2005: abstract, Septin functions and Figure3 caption | supports | Inspected author review names the five mitotic septins, describes collar filaments and scaffold activity, and distinguishes collar formation from cytokinetic splitting. It is a review, not a new localization experiment. |
| record | data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml; Entire maintained YAML | context_only | Identity, parent/parthood, one septin class, five sequence examples, one scaffold function, three topology edges and two discussions were read. No quantitative measurements, images or trait links are asserted. |
| component-policy | docs/CURATION.md; Components: taxon-agnostic class and REVIEWED_LABEL_ONLY rules | context_only | Components are taxon-agnostic families or classes. REVIEWED_LABEL_ONLY means no exact term exists; role and example context carry localization and taxon scope. |
| identity-search | data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml; Identifier search across data/structures with --no-ignore --hidden | context_only | Only the target declares GO0032174. |
| schema-result | just validate data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml --out /private/tmp/cellstructure-batch5-20261020-aEelh1/cellular_bud_neck_septin_collar-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml --out /private/tmp/cellstructure-batch5-20261020-aEelh1/cellular_bud_neck_septin_collar-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch5-20261020-aEelh1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch5-20261020-aEelh1/cellular_bud_neck_septin_collar-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml; exact collect() scope | supports | 14 of17 collected target identifiers returned OK at the unchanged base. Residuals: PMID:14562095: UNREACHABLE; resolved by evidence collar-epmc; PMID:25971666: UNREACHABLE; resolved by evidence collar-epmc; PMID:9790978: UNREACHABLE; resolved by evidence collar-epmc. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Kozubowski2005 and Finnigan2015 full-text routes returned Europe PMC500, public archive404 and browser challenges. Their inspected abstracts support the coarse assertions assessed here; detailed imaging and recruitment experiments were not re-audited.
- Huh2003 and Mino1998 were inspected at abstract level; exact protein-specific ECO localization provenance was verified in native UniProt.
- The cited author review supports the coarse state and scaffold model, not an updated stoichiometric census.
- COMMON is not a prevalence measurement; reference-strain examples are not independent proof of localization.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T073445Z-cellular-bud-neck-septin-collar-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cellular bud-neck septin-collar evidence and family-grounding review
started_at: '2026-10-20T07:29:54Z'
finished_at: '2026-10-20T07:34:45Z'
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
summary: Exact collar identity, boundaries, topology and five protein examples are
  supported. One minor finding concerns withholding a verified taxon-agnostic Septin
  family mapping on an overly localized criterion.
source:
  git_revision: 99692a3d5f16a7dcd6db7e3811344c299a977b81
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
  - path: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
    sha256: 2901b13c5e8db9e171b7c1f93caf816991d0e58ba9456339c5db7f7f3716ae0e
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
- target_id: GO:0032174
  path: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
  label: cellular bud neck septin collar
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
    role: maintained scientific record
scope:
  description: Entire maintained record, native GO/UniProt/InterPro/taxonomy, cited
    bibliographic identities and abstracts, and relevant full-text sections of the
    cited2005 author review.
  selection: Third remaining unreviewed path in batch5, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032174
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032174
  command: just validate data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032174
  command: just validate-strict data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
    --out /private/tmp/cellstructure-batch5-20261020-aEelh1/cellular_bud_neck_septin_collar-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0032174
  summary: 14 identifiers OK; 3 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - collar-epmc
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0032174
  summary: No expression-module mechanism is asserted. Native sequence annotations
    and the cited localization/scaffold sources address these claims.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0032174
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - collar-go
  - collar-proteins
  - collar-IPR016491
  - collar-IPR030379
  - collar-epmc
  - ring-taxon
  - review-text
  - record
  - component-policy
  - identity-search
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032174
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0032174
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0032174
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0032174
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0032174
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: collar-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032174,GO:0032173,GO:0005935,GO:0000144,GO:0032177
  locator: Native term definitions and child relations
  accessed_at: '2026-10-20T07:32:23.248191Z'
  support: supports
  summary: All five GO terms are active. The target definition is exact; GO0032173
    lists the target as is_a and GO0005935 lists it as part_of. Initial ring and split-ring
    definitions distinguish the surrounding cell-cycle states.
  snapshot_sha256: 0703341bf313a2e7a789ee307b3d07a36585c3ee16d69b6d1cdc484fdc86b896
- evidence_id: collar-proteins
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=(gene_exact:CDC3%20OR%20gene_exact:CDC10%20OR%20gene_exact:CDC11%20OR%20gene_exact:CDC12%20OR%20gene_exact:SHS1)%20AND%20organism_id:559292%20AND%20reviewed:true&format=json
  locator: Complete five-result native query; genes, names, organism, localization
    evidence and InterPro cross-references
  accessed_at: '2026-10-20T07:32:27.037283Z'
  support: supports
  summary: 'The exact-gene, reviewed S288C query returns five entries: P32457 CDC3,
    P25342 CDC10, P32458 CDC11, P32468 CDC12 and Q07657 SHS1. Names, status and taxon
    match. Native localization evidence links match every PMID/ECO statement in the
    examples. All five entries cross-reference IPR016491.'
  snapshot_sha256: a2792effab2d1d29b11914248246793a98fedeab1da079da62df7b5e92e9f3f9
- evidence_id: collar-IPR016491
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: Native family type, name and scope
  accessed_at: '2026-10-20T07:32:51.027110Z'
  support: supports
  summary: IPR016491 is the Septin family, spanning yeast and animals. Its native
    description explicitly includes the five named budding-yeast septins. This family
    grounds the taxon-agnostic component class; it need not be restricted to collar-localized
    proteins.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: collar-IPR030379
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030379/
  locator: Native type and scope
  accessed_at: '2026-10-20T07:32:51.800701Z'
  support: supports
  summary: IPR030379 is the septin G domain rather than the whole protein family.
    It is not the proposed family mapping.
  snapshot_sha256: d57a91e3120089ef54335d489bf45d729ec0d6ae6ee13771769eb1e539124fb1
- evidence_id: collar-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1091/mbc.E04-09-0764%20OR%20DOI:10.1016/j.tcb.2005.06.007%20OR%20EXT_ID:14562095%20OR%20EXT_ID:25971666%20OR%20EXT_ID:9790978&format=json&resultType=core
  locator: Five bibliographic records and inspected abstracts
  accessed_at: '2026-10-20T07:32:23.432420Z'
  support: supports
  summary: Exact records verify the two cited DOIs and three example PMIDs. Kozubowski2005
    abstract directly states ring-to-collar rearrangement and Bni4/Kcc4 asymmetry.
    Mino1998 abstract describes Shs1 bud-neck localization; Finnigan2015 abstract
    describes Cdc11/Shs1-dependent recruitment. Huh2003 abstract establishes the survey
    but does not resolve individual proteins.
  snapshot_sha256: 8f308f8deb9cf1326ab1410e941fce7985ebe790a74920d8960622672963eec5
- evidence_id: ring-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=4932,559292
  locator: Native species and strain taxonomy records
  accessed_at: '2026-10-20T07:26:49.146723Z'
  support: supports
  summary: NCBI identifies4932 as Saccharomyces cerevisiae and559292 as its S288C
    strain.
  snapshot_sha256: a0110fd4b27dc6aa4f9c3ae5db622f12e6d58f6309580788781290225ca768bb
- evidence_id: review-text
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/
  locator: 'Versele and Thorner2005: abstract, Septin functions and Figure3 caption'
  accessed_at: '2026-10-20T07:34:44Z'
  support: supports
  summary: Inspected author review names the five mitotic septins, describes collar
    filaments and scaffold activity, and distinguishes collar formation from cytokinetic
    splitting. It is a review, not a new localization experiment.
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T07:34:44Z'
  support: context_only
  summary: Identity, parent/parthood, one septin class, five sequence examples, one
    scaffold function, three topology edges and two discussions were read. No quantitative
    measurements, images or trait links are asserted.
- evidence_id: component-policy
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: taxon-agnostic class and REVIEWED_LABEL_ONLY rules'
  accessed_at: '2026-10-20T07:34:44Z'
  support: context_only
  summary: Components are taxon-agnostic families or classes. REVIEWED_LABEL_ONLY
    means no exact term exists; role and example context carry localization and taxon
    scope.
- evidence_id: identity-search
  kind: record_content
  reference: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
  locator: Identifier search across data/structures with --no-ignore --hidden
  accessed_at: '2026-10-20T07:34:44Z'
  support: context_only
  summary: Only the target declares GO0032174.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-20T07:29:56Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml'
  snapshot_sha256: 9687594d20a5889626ec4a85a8afdcbb48b281115ea69ec6fde787aa427eb042
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
    --out /private/tmp/cellstructure-batch5-20261020-aEelh1/cellular_bud_neck_septin_collar-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-20T07:29:58Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml\
    \ --out /private/tmp/cellstructure-batch5-20261020-aEelh1/cellular_bud_neck_septin_collar-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch5-20261020-aEelh1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch5-20261020-aEelh1/cellular_bud_neck_septin_collar-strict.tsv"
  snapshot_sha256: 78c10399b6d5bbcc8edd10255ced3e478880b43e4f0cbe1f7aef503ff0fb2ff5
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml; exact
    collect() scope
  accessed_at: '2026-10-20T07:34:44Z'
  support: supports
  summary: '14 of17 collected target identifiers returned OK at the unchanged base.
    Residuals: PMID:14562095: UNREACHABLE; resolved by evidence collar-epmc; PMID:25971666:
    UNREACHABLE; resolved by evidence collar-epmc; PMID:9790978: UNREACHABLE; resolved
    by evidence collar-epmc. Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec
  accessed_at: '2026-10-19T07:38:12Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 7b6165ba8532d080a336f7a5a4c29b456fdf7182dd596410b700dfe60af61a06
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-19T07:29:37Z'
  support: supports
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: b98e3eecd58a81fa46033e6baca6977811a439f119b943fd5d9931964adb2680
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad
  accessed_at: '2026-10-19T07:32:39Z'
  support: supports
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-19T07:29:45Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4
  accessed_at: '2026-10-19T08:04:01Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  snapshot_sha256: 7cb413edccc92ee6ce79a32cd2b96a59bc4da37f2cb7b326eaca51a64f723cfb
assessments:
- assessment_id: identity
  area: identity
  topic: Exact collar structure
  outcome: supported
  target_ids:
  - GO:0032174
  summary: GO identity and definition match the localized hourglass structure, distinct
    from both initial ring and split rings.
  evidence_ids:
  - collar-go
  - record
  - review-text
- assessment_id: hierarchy
  area: grounding
  topic: Subtype and containing region
  outcome: supported
  target_ids:
  - GO:0032174
  summary: Native GO confirms septin-collar subtype and bud-neck parthood.
  evidence_ids:
  - collar-go
- assessment_id: composition
  area: evidence
  topic: Septin class and structural necessity
  outcome: supported
  target_ids:
  - GO:0032174
  summary: The named septins form the collar; class-level ESSENTIAL concerns forming
    a septin structure, not essentiality of every paralog or cell viability. The record
    does not impose a five-subunit stoichiometry.
  evidence_ids:
  - collar-go
  - review-text
  - record
- assessment_id: examples
  area: provenance
  topic: Five reference examples and their localization citations
  outcome: supported
  target_ids:
  - GO:0032174
  summary: All five native accession/gene/name/status/taxon pairs match. The example
    evidence notes accurately report UniProt localization provenance; Huh survey membership
    was checked at the native annotation level, not inferred from its broad abstract.
  evidence_ids:
  - collar-proteins
  - collar-epmc
  - ring-taxon
  - record
- assessment_id: mapping
  area: grounding
  topic: Family identity versus localized role
  outcome: concern
  target_ids:
  - GO:0032174
  summary: The label-only rationale applies a localized fungal cohort restriction
    to a taxon-agnostic component. Verified IPR016491 matches the named Septin family
    and all five examples; IPR030379 is only a domain. The family mapping and discussion
    should be updated.
  evidence_ids:
  - collar-IPR016491
  - collar-IPR030379
  - collar-proteins
  - component-policy
  - record
- assessment_id: taxa
  area: scope
  topic: Budding-yeast canonical example
  outcome: supported
  target_ids:
  - GO:0032174
  summary: The primary abstract supports the species and reporter context. COMMON
    represents ordinary cell-cycle occurrence rather than quantified prevalence; S288C
    examples do not assert every experiment used that strain.
  evidence_ids:
  - collar-epmc
  - ring-taxon
  - record
- assessment_id: function
  area: evidence
  topic: Bud-neck scaffold beyond cytokinesis
  outcome: supported
  target_ids:
  - GO:0032174
  summary: GO and the author review support scaffolding; the primary abstract supports
    Bni4/Kcc4 asymmetric organization. The function does not claim these associated
    proteins are collar constituents.
  evidence_ids:
  - collar-go
  - collar-epmc
  - review-text
  - record
- assessment_id: graph
  area: graph
  topic: Nonmechanistic ring-to-collar topology
  outcome: supported
  target_ids:
  - GO:0032174
  summary: Assembly into the collar, initial-ring rearrangement and bud-neck placement
    are supported at the declared coarse level. No full recruitment mechanism is inferred.
  evidence_ids:
  - collar-go
  - collar-epmc
  - review-text
  - record
- assessment_id: completeness
  area: completeness
  topic: Scope and maintained status
  outcome: supported
  target_ids:
  - GO:0032174
  summary: PROPOSED and the state-boundary discussion are appropriate. The family-grounding
    TODO has an actionable verified resolution; accessory census and measurements
    are not required by the stated scope.
  evidence_ids:
  - record
  - collar-go
  - collar-IPR016491
findings:
- finding_id: F1
  issue_key: cellular-bud-neck-septin-collar-family-grounding-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Label-only rationale confuses family identity with collar-localized scope
  description: The component is labeled septin proteins, but grounding_notes withholds
    a family because it seeks the complete localized fungal collar cohort. Native
    IPR016491 denotes the Septin family and is annotated on all five verified examples.
    Repository policy assigns taxon-agnostic family identity to components; localization
    belongs in role and evidence. Retaining REVIEWED_LABEL_ONLY on this rationale
    leaves a resolvable family mapping and a stale TODO.
  target_ids:
  - GO:0032174
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions[discussion_id=resolve_bud_neck_collar_septin_groundings]
  evidence_ids:
  - collar-IPR016491
  - collar-proteins
  - component-policy
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: The biological structure and membership are supported; this
    is a bounded missing family mapping and rationale defect, not an incorrect assigned
    CURIE.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032174
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
    role: maintained scientific record
  description: In separately authorized curation, ground the septin protein class
    to verified IPR016491, reconcile the grounding status/notes and resolve the exact-family
    TODO. Preserve the localized role, reference examples and their evidence.
  acceptance_checks:
  - Family label and accession agree with native InterPro and all five example cross-references.
  - Grounding no longer requires the family term to encode collar localization or
    fungal restriction.
  - Run native schema, strict, product-label, history and generated-page checks after
    curation.
  generator: Maintained YAML; just render derives pages.
limitations:
- Kozubowski2005 and Finnigan2015 full-text routes returned Europe PMC500, public
  archive404 and browser challenges. Their inspected abstracts support the coarse
  assertions assessed here; detailed imaging and recruitment experiments were not
  re-audited.
- Huh2003 and Mino1998 were inspected at abstract level; exact protein-specific ECO
  localization provenance was verified in native UniProt.
- The cited author review supports the coarse state and scaffold model, not an updated
  stoichiometric census.
- COMMON is not a prevalence measurement; reference-strain examples are not independent
  proof of localization.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
