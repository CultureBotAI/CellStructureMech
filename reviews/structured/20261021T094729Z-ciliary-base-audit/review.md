# Ciliary base identity, composition boundary and graph review

- Review: 20261021T094729Z-ciliary-base-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:07:00Z
- Finished UTC: 2026-10-21T09:47:29Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact base identity, Y-link grounding and TZ primary evidence are supported. Two minor findings, one graph and one known-region completeness finding require curation.

## Scope And Provenance

Full exact record and inspected repository rubric; source-native ontology/taxon/protein identities and all claim-bearing citation scopes, with readable primary results distinguished from review summaries and access-limited sources.

Selection: Exact target 2 in the frozen batch15 path selection on expanded-main revision 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; no old-base resolver result is reused.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097546 | data/structures/appendage/ciliary_base.yaml | maintained | ciliary base |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0097546 | Focused validator passed. |
| Focused native strict | passed | True | GO:0097546 | Focused validator passed. |
| Native verify | passed | True | GO:0097546 | Read-only native diagnostic passed; it does not establish biological membership or mechanism. |
| Native causal-graphs | passed | True | GO:0097546 | Read-only native diagnostic passed; it does not establish biological membership or mechanism. |
| Claim-level scientific review | passed | True | GO:0097546 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Target resolver slice with native transport-failure cross-checks | passed | True | GO:0097546 | 12 of 12 exact target identifiers returned OK. No target residuals. The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| Full corpus QC | passed | True | GO:0097546 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097546 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097546 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097546 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0097546 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Ciliary base versus transition zone

identity: supported. Targets: GO:0097546.

Exact GO identity, SUBCELLULAR_REGION kind, cilium parthood and four synonyms are supported. The base includes the TZ but is broader than it. The appended IFT/diffusion narrative is literature-level explanation beyond the GO definition and is assessed through the cited gate review, not attributed wholly to GO.

### Known non-TZ regions omitted

completeness: concern. Targets: GO:0097546.

All three component rows and constituent graph nodes describe the TZ, while the exact base definition includes distal basal body and transition fibers. This is a bounded known-region completeness gap, not a demand to enumerate all proteins or fill arbitrary optional slots.

### Y-link and aggregates

grounding: supported. Targets: GO:0097546.

The exact GO Y-link complex is grounded correctly and the historical earlier label-only rationale is expressly superseded. Generic TZ segment and heterogeneous protein-network aggregates need not be assigned a whole-axoneme or single-family CURIE. Unknown assembly essentiality is honest.

### Two unreviewed examples

grounding: supported. Targets: GO:0097546.

The two native accession/status/label/ORF/taxon fields match and native verification passes. NCBI Gene provides the CHLRE-to-Cre cross-reference and Fauser2022 Fig4d explicitly labels the two loci CEP290 and NPHP4. The bounded exact-gene reviewed search returns no entries. These are identity-only examples, distinct from primary localization evidence. The role correctly preserves the literal UniProt ORF rather than claiming it is the native geneName token.

### TZ tethering and gating

evidence: supported. Targets: GO:0097546.

The primary CEP290 loss/rescue/localization study and later three-mutant comparisons support TZ microtubule–membrane organization and ciliary-composition control. Wedge loss, Y-link loss and ciliary proteomics are not interchangeable endpoints. No complete network, Y-link-specific mechanism or fixed assembly hierarchy is inferred.

### Chlamydomonas canonical example

scope: supported. Targets: GO:0097546.

The named species and isolated-TZ proteomics example are correct; mutant preparation and differential localization remain strain/condition-specific. Diener isolated TZs do not represent every physical constituent of the complete base.

### Static membership and gate output

graph: concern. Targets: GO:0097546.

The graph links TZ elements to the base, base to cilium and base to gating. It contains no perturbation or mechanistic intermediate connecting a specific constituent to gating, despite labeling the graph MECHANISTIC.

### Optional fields and provenance

completeness: supported. Targets: GO:0097546.

All current claims and four cited bibliography identities were reviewed. No image or quantitative property requires a separate asset audit. Historical curation/access wording is not falsified merely by current accessibility.

## Findings

### F1: Represent the graph as structural context or supply causal steps

minor / open / confirmed; issue key: ciliary-base-graph-static-mechanistic-scope.

The graph is a set of constituent/compartment parthood assertions plus a whole-base gating output. It does not explain how a named constituent, interaction or perturbation controls that output. Source-backed molecular mechanisms exist in the primary papers, but the current edge representation does not encode them.

### F2: Represent the defining basal-body and transition-fiber regions

minor / open / confirmed; issue key: ciliary-base-known-non-tz-composition-gap.

The entire component inventory and constituent graph cover only transition-zone structures, despite the exact base definition explicitly comprising distal basal body, transition fibers and TZ. The cited Diener preparation expressly excludes transition fibers from isolated TZs, and the gate review separates those structures. This materially narrows the represented composition of the broad base. It does not require an exhaustive protein inventory or replace the base identity with TZ.

## Recommended Actions And Acceptance Checks

### A1

Mark the present graph NONMECHANISTIC, remove it, or build a bounded mechanism with actual constituent-to-event-to-outcome edges supported by primary experiments.

- Separate localization/parthood from effects on tethering and protein composition.
- Preserve organism, mutant, rescue and preparation boundaries on causal edges.
- After separately authorized curation, use the guarded writer and native history/status rules; run focused schema/strict, identifier and evidence checks.

### A2

Add source-backed structural representation of the distal basal-body and transition-fiber regions, or explicitly delimit the present component view as partial and identify the known missing regions for follow-up. Label-only rows can be used where exact scoped identifiers are unresolved.

- Preserve the complete GO0097546 boundary while keeping TZ-only experimental preparations scoped.
- Do not ground a distal segment to the complete basal body without a segment qualification or infer that isolated TZ proteomics samples transition fibers.
- After separately authorized curation, use the guarded writer and native history/status rules; run focused schema/strict, identifier and evidence checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/ciliary_base.yaml; Entire maintained YAML, all components/examples/evidence, definition, hierarchy, functions, every graph node/edge, and creation history. | context_only | The complete exact target was read after native inspect. No neighboring maintained record is relied on; external GO authority supplies graph identities. The target remains PROPOSED and contains no image, measured property, dataset or verbatim quotation assertion. |
| rubric | docs/CURATION.md; Evidence placement; component essentiality; source.inputs also freezes the full review checklist and protein/graph guidance. | context_only | Evidence is claim-specific and retains taxon, preparation and source tier. Essentiality concerns assembly necessity; canonical presence or catalytic activity does not independently prove it. Optional empty fields and generic protein classes do not automatically require findings. |
| graph-contract | src/cellstructuremech/schema/cellstructuremech.yaml; CellStructureRecord.causal_graphs; GraphKindEnum.ASSEMBLY/FUNCTION; CausalGraphScopeEnum; curate-causal-graphs/SKILL.md. | context_only | The graph should explain how the structure is built or does its job. Static parthood or whole-structure function summaries alone do not explain a causal mechanism, even when schema-valid. |
| ciliary-base-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005929,GO:0035869,GO:0097537,GO:0097546,GO:0110165; All five result id/name/definition/synonyms/children fields; relation direction retained. | supports | Active GO0097546 exactly denotes a base comprising distal basal body, transition fibers and transition zone, with all four exact synonyms. GO0110165 lists base is_a; GO0005929 lists base part_of. GO0097537 is the exact assembled Y-shaped link, within the TZ; it is not an individual protein family. |
| ciliary-base-agent-tax-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; taxId/scientificName/rank/lineage. | supports | Taxon3055 is Chlamydomonas reinhardtii, matching both native entries and the study organism. |
| ciliary-base-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016/j.cub.2014.11.066%22%20OR%20DOI%3A%2210.1038/s41467-022-31751-0%22%20OR%20DOI%3A%2210.1083/jcb.201006105%22%20OR%20DOI%3A%2210.1101/cshperspect.a028134%22&amp;format=json&amp;resultType=core&amp;pageSize=100; All resultList.result identifiers/title/pubTypeList. | context_only | The four cited DOI/PMID/title identities match. Garcia-Gonzalo/Reiter2017 is a review despite also carrying a generic research-article metadata flag; Craige2010, Diener2015 and Wang2022 are primary studies. |
| ciliary-base-agent-craige2010-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2935561/fullTextXML; Results CEP290 localization; mutant microtubule–membrane defects; CEP290 immunogold localization; abnormal composition and Discussion; Figs2–4 captions. | supports | CEP290 knockout/rescue and antibody/immunogold localization in Chlamydomonas show TZ localization, abnormal Y/wedge links and membrane detachment in mutants, and altered flagellar protein composition. Most axonemal sections and basal bodies are normal. The study supports the target tethering role; it does not establish every Y-link protein or a universal gate architecture. |
| ciliary-base-agent-wang2022-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9271036/fullTextXML; Results Loss of TCTN1, ultrastructure, localization, mutant phenotype and composition sections; Discussion; Methods Strains and cell culture. Fig2/3 and5 descriptions. | supports | Chlamydomonas tctn1 loss disrupts wedge-shaped structures while Y-links and 9+2 axoneme are distinguishable. CEP290/TCTN1/NPHP4 show distinct TZ positions, independent localization and different ciliary proteomic phenotypes. Mutant culture/autolysin conditions affect visible ciliogenesis. The record accurately summarizes wedge defects, protein sorting and ectosome comparisons without claiming a complete protein network. |
| ciliary-base-agent-diener2015-pmc-retry | https://pmc.ncbi.nlm.nih.gov/articles/PMC4318714/?pdf=render; Summary; Results Isolation of transition zones, Ultrastructure of the isolated TZ and Proteomic analysis; Fig1B and Fig2 captions. | supports | Primary isolation/proteomics analyzes Chlamydomonas TZ vesicles left during predivision flagellar resorption. The isolated TZ lacks depolymerized outer doublets and some in-situ features; the accepted proteome is enriched, not a complete ciliary-base inventory. Fig1B expressly distinguishes transition fibers, which are not part of the TZ. The canonical example is accurate as isolated-TZ proteomics. |
| ciliary-base-agent-garcia2017-pmc-retry | https://pmc.ncbi.nlm.nih.gov/articles/PMC5287074/?pdf=render; Abstract; introductory gate anatomy; TRANSITION FIBERS section; Fig1 caption. | supports | The review distinguishes transition fibers linking distal basal body to membrane from Y-links linking proximal axoneme and membrane within the TZ. Both contribute to the broader ciliary gate. The transition-fiber discussion separates anchoring, passageways and molecular hierarchy; these are reviewed comparative mechanisms rather than new experiments by this article. |
| ciliary-base-agent-A0A2K3DWT6 | https://rest.uniprot.org/uniprotkb/A0A2K3DWT6.json; primaryAccession/entryType/proteinDescription/genes/organism/SUBCELLULAR LOCATION. | supports | Primary unreviewed entry A0A2K3DWT6 has native ORF CHLRE_03g167550v5, the exact recorded Cep290-domain protein label and taxon3055. Its location is automatic ARBA, not experimentally curated. The record uses it as identity-only support. |
| ciliary-base-agent-A0A2K3D4W1 | https://rest.uniprot.org/uniprotkb/A0A2K3D4W1.json; primaryAccession/entryType/proteinDescription/genes/organism/comments. | supports | Primary unreviewed entry A0A2K3D4W1 has native ORF CHLRE_12g531400v5, exact Nephrocystin-4 label and taxon3055; no location comment is imported as experimental evidence. |
| ciliary-base-agent-mapping-gene5728998 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&amp;id=5728998&amp;retmode=xml; Entrezgene_gene/Gene-ref: locus-tag, Phytozome Dbtag and formal-name. | supports | NCBI Gene5728998 links the exact CHLRE_03g167550v5 locus tag to Phytozome Cre03.g167550. The official name here is uncharacterized protein; the record does not gain a literal CEP290 symbol from this database alone. |
| ciliary-base-agent-mapping-gene5718574 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&amp;id=5718574&amp;retmode=xml; Entrezgene_gene/Gene-ref: locus-tag, Phytozome Dbtag and formal-name. | supports | NCBI Gene5718574 links the exact CHLRE_12g531400v5 locus tag to Phytozome Cre12.g531400. The official name here is uncharacterized protein; the published symbol bridge is a separate source. |
| ciliary-base-agent-mapping-fauser2022-pdf | https://www.nature.com/articles/s41588-022-01052-9.pdf; Printed p709, Fig4d first two rows and entire caption, PDF page5 visually inspected; DOI10.1038/s41588-022-01052-9. | supports | The primary Fauser2022 article explicitly labels Cre03.g167550 as CEP290 and Cre12.g531400 as NPHP4 in Fig4d. Together with the native locus cross-references this verifies both record gene mappings. This bounded use establishes a published locus/symbol bridge, not a new localization assay or a claim that UniProt literally contains these symbols. |
| ciliary-base-agent-reviewed-gene-search | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACEP290%20OR%20gene_exact%3ANPHP4%29%20AND%20organism_id%3A3055%20AND%20reviewed%3Atrue&amp;format=json&amp;size=100; results array; native HTTP200 JSON. | supports | The exact reviewed CEP290/NPHP4 query at taxon3055 returns an empty results array. This supports using the verified unreviewed examples within the bounded gene-symbol search; it is not a claim that no reviewed entry could exist under any other alias. |
| schema-result | just validate data/structures/appendage/ciliary_base.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/appendage/ciliary_base.yaml |
| strict-result | just validate-strict data/structures/appendage/ciliary_base.yaml --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/ciliary_base-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/appendage/ciliary_base.yaml --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/ciliary_base-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch15-20261021-ohdkgt21/ciliary_base-strict.tsv |
| verify-result | /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml --verify; Read-only native target diagnostic log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| causal-graphs-result | /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml --causal-graphs; Read-only native target diagnostic log | supports | data/structures/appendage/ciliary_base.yaml  (GO:0097546)<br>  ciliary_base_mechanism	transition_zone_protein_network	COVERED	-&gt;transition_zone_protein_network (UniProtKB:A0A2K3DWT6, UniProtKB:A0A2K3D4W1)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| target-curies-result | just check-curies-strict; data/structures/appendage/ciliary_base.yaml; exact native collect() target slice of original fresh-base TSV | supports | 12 of 12 exact target identifiers returned OK. No target residuals. The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Native accession identity is distinct from direct experimental membership. Exact published CEP290/NPHP4 locus mappings are now independently verified through NCBI Gene and Fauser2022 Fig4d. Only the latter PDF page and relevant context were inspected; no whole-Fauser-paper or supplementary screen-data review is claimed.
- Diener2015 initial JATS route returned500 and the native PMC retry supplied genuine body; Garcia2017 likewise had500 JATS but genuine PMC review text. First sandbox DNS failures and retry receipts remain preserved.
- Diener vesicles are residual isolated TZs with absent outer-doublet microtubules, not intact full bases. Garcia2017 remains a secondary review; its broad gate context is not a new primary localization assay.
- The earlier Y-link label-only statement is explicitly labeled historical and superseded by exactGO0097537; current access and the record creation timestamp do not alone establish false prior curation provenance.
- The exact target resolver slice is derived from the completed fresh-base run. Any PMID transport failures were checked against the separately cited native literature metadata; these identity checks do not establish full-body scientific support.
- No raw microscopy pixels, original movies, supplementary datasets or unpublished data were independently reanalyzed. Figure captions and relevant body/methods prose were read at the listed locators. The target has no image asset or quantitative measurement assertion. Fauser2022 Fig4d plotted gene/locus labels and caption were visually inspected in the publisher PDF; that figure-pixel inspection is explicitly included in the locus-identity check.
- All 14 frozen repository inputs retain their inspected hashes. No neighboring local structure record, expression-module source or iModulonDB claim is used; no optional-empty finding is made.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Unsaveable clean exceptions are not manufactured; each listed finding is supported independently of validator results. Root alone owns finalization, save and shared index updates.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094729Z-ciliary-base-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Ciliary base identity, composition boundary and graph review
started_at: '2026-10-21T09:07:00Z'
finished_at: '2026-10-21T09:47:29Z'
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
summary: The exact base identity, Y-link grounding and TZ primary evidence are supported.
  Two minor findings, one graph and one known-region completeness finding require
  curation.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/structures/appendage/ciliary_base.yaml
    sha256: fce7c8f9b88ff6aeca1d3fcde92b8e97fc59d5613749df0e92dc14561aeb4ddb
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
- target_id: GO:0097546
  path: data/structures/appendage/ciliary_base.yaml
  label: ciliary base
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_base.yaml
    role: maintained scientific record
scope:
  description: Full exact record and inspected repository rubric; source-native ontology/taxon/protein
    identities and all claim-bearing citation scopes, with readable primary results
    distinguished from review summaries and access-limited sources.
  selection: Exact target 2 in the frozen batch15 path selection on expanded-main
    revision 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; no old-base resolver result
    is reused.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097546
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: just validate data/structures/appendage/ciliary_base.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: just validate-strict data/structures/appendage/ciliary_base.yaml --out
    /private/tmp/cellstructure-batch15-20261021-ohdkgt21/ciliary_base-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml
    --verify
  exit_code: 0
  summary: Read-only native diagnostic passed; it does not establish biological membership
    or mechanism.
  evidence_ids:
  - verify-result
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native diagnostic passed; it does not establish biological membership
    or mechanism.
  evidence_ids:
  - causal-graphs-result
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0097546
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - rubric
  - graph-contract
  - ciliary-base-agent-go
  - ciliary-base-agent-tax-3055
  - ciliary-base-agent-epmc
  - ciliary-base-agent-craige2010-jats
  - ciliary-base-agent-wang2022-jats
  - ciliary-base-agent-diener2015-pmc-retry
  - ciliary-base-agent-garcia2017-pmc-retry
  - ciliary-base-agent-A0A2K3DWT6
  - ciliary-base-agent-A0A2K3D4W1
  - ciliary-base-agent-mapping-gene5728998
  - ciliary-base-agent-mapping-gene5718574
  - ciliary-base-agent-mapping-fauser2022-pdf
  - ciliary-base-agent-reviewed-gene-search
- check_id: target-curies
  name: Target resolver slice with native transport-failure cross-checks
  status: passed
  required: true
  target_ids:
  - GO:0097546
  summary: 12 of 12 exact target identifiers returned OK. No target residuals. The
    shared command exit zero is not interpreted as successful network resolution for
    transport failures.
  evidence_ids:
  - target-curies-result
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/ciliary_base.yaml
  locator: Entire maintained YAML, all components/examples/evidence, definition, hierarchy,
    functions, every graph node/edge, and creation history.
  accessed_at: '2026-10-21T09:23:25Z'
  support: context_only
  summary: The complete exact target was read after native inspect. No neighboring
    maintained record is relied on; external GO authority supplies graph identities.
    The target remains PROPOSED and contains no image, measured property, dataset
    or verbatim quotation assertion.
- evidence_id: rubric
  kind: record_content
  reference: docs/CURATION.md
  locator: Evidence placement; component essentiality; source.inputs also freezes
    the full review checklist and protein/graph guidance.
  accessed_at: '2026-10-21T09:23:25Z'
  support: context_only
  summary: Evidence is claim-specific and retains taxon, preparation and source tier.
    Essentiality concerns assembly necessity; canonical presence or catalytic activity
    does not independently prove it. Optional empty fields and generic protein classes
    do not automatically require findings.
- evidence_id: graph-contract
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: CellStructureRecord.causal_graphs; GraphKindEnum.ASSEMBLY/FUNCTION; CausalGraphScopeEnum;
    curate-causal-graphs/SKILL.md.
  accessed_at: '2026-10-21T09:23:25Z'
  support: context_only
  summary: The graph should explain how the structure is built or does its job. Static
    parthood or whole-structure function summaries alone do not explain a causal mechanism,
    even when schema-valid.
- evidence_id: ciliary-base-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005929,GO:0035869,GO:0097537,GO:0097546,GO:0110165
  locator: All five result id/name/definition/synonyms/children fields; relation direction
    retained.
  accessed_at: '2026-10-21T09:08:34.191304Z'
  support: supports
  summary: Active GO0097546 exactly denotes a base comprising distal basal body, transition
    fibers and transition zone, with all four exact synonyms. GO0110165 lists base
    is_a; GO0005929 lists base part_of. GO0097537 is the exact assembled Y-shaped
    link, within the TZ; it is not an individual protein family.
  snapshot_sha256: 283f71f909733a88e9ea5b9aabfc209d8bef76c05dde9fac9e0a6c7bec1125e6
- evidence_id: ciliary-base-agent-tax-3055
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: taxId/scientificName/rank/lineage.
  accessed_at: '2026-10-21T09:08:34.223045Z'
  support: supports
  summary: Taxon3055 is Chlamydomonas reinhardtii, matching both native entries and
    the study organism.
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: ciliary-base-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016/j.cub.2014.11.066%22%20OR%20DOI%3A%2210.1038/s41467-022-31751-0%22%20OR%20DOI%3A%2210.1083/jcb.201006105%22%20OR%20DOI%3A%2210.1101/cshperspect.a028134%22&format=json&resultType=core&pageSize=100
  locator: All resultList.result identifiers/title/pubTypeList.
  accessed_at: '2026-10-21T09:08:34.830960Z'
  support: context_only
  summary: The four cited DOI/PMID/title identities match. Garcia-Gonzalo/Reiter2017
    is a review despite also carrying a generic research-article metadata flag; Craige2010,
    Diener2015 and Wang2022 are primary studies.
  snapshot_sha256: 2a58b1e11c937befb0c74097fe6aaada744b2161bb75d072eaabb6cca13f89c1
- evidence_id: ciliary-base-agent-craige2010-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2935561/fullTextXML
  locator: Results CEP290 localization; mutant microtubule–membrane defects; CEP290
    immunogold localization; abnormal composition and Discussion; Figs2–4 captions.
  accessed_at: '2026-10-21T09:09:27.560455Z'
  support: supports
  summary: CEP290 knockout/rescue and antibody/immunogold localization in Chlamydomonas
    show TZ localization, abnormal Y/wedge links and membrane detachment in mutants,
    and altered flagellar protein composition. Most axonemal sections and basal bodies
    are normal. The study supports the target tethering role; it does not establish
    every Y-link protein or a universal gate architecture.
  snapshot_sha256: a83f54c0f615e5ac6f3fa935a59ace211da887d0d8c92cbebf04dddc25715f7c
- evidence_id: ciliary-base-agent-wang2022-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9271036/fullTextXML
  locator: Results Loss of TCTN1, ultrastructure, localization, mutant phenotype and
    composition sections; Discussion; Methods Strains and cell culture. Fig2/3 and5
    descriptions.
  accessed_at: '2026-10-21T09:09:26.141621Z'
  support: supports
  summary: Chlamydomonas tctn1 loss disrupts wedge-shaped structures while Y-links
    and 9+2 axoneme are distinguishable. CEP290/TCTN1/NPHP4 show distinct TZ positions,
    independent localization and different ciliary proteomic phenotypes. Mutant culture/autolysin
    conditions affect visible ciliogenesis. The record accurately summarizes wedge
    defects, protein sorting and ectosome comparisons without claiming a complete
    protein network.
  snapshot_sha256: 026e49670797cdcbf1f206ff808cd0c87bc56041593c9947ffa32be9ea8a39bd
- evidence_id: ciliary-base-agent-diener2015-pmc-retry
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4318714/?pdf=render
  locator: Summary; Results Isolation of transition zones, Ultrastructure of the isolated
    TZ and Proteomic analysis; Fig1B and Fig2 captions.
  accessed_at: '2026-10-21T09:13:21.057184Z'
  support: supports
  summary: Primary isolation/proteomics analyzes Chlamydomonas TZ vesicles left during
    predivision flagellar resorption. The isolated TZ lacks depolymerized outer doublets
    and some in-situ features; the accepted proteome is enriched, not a complete ciliary-base
    inventory. Fig1B expressly distinguishes transition fibers, which are not part
    of the TZ. The canonical example is accurate as isolated-TZ proteomics.
  snapshot_sha256: d72442134b9aed0be6b1684a8949c55003f7cb301a4e42d2e8b4c7e158dc6955
- evidence_id: ciliary-base-agent-garcia2017-pmc-retry
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5287074/?pdf=render
  locator: Abstract; introductory gate anatomy; TRANSITION FIBERS section; Fig1 caption.
  accessed_at: '2026-10-21T09:13:21.087790Z'
  support: supports
  summary: The review distinguishes transition fibers linking distal basal body to
    membrane from Y-links linking proximal axoneme and membrane within the TZ. Both
    contribute to the broader ciliary gate. The transition-fiber discussion separates
    anchoring, passageways and molecular hierarchy; these are reviewed comparative
    mechanisms rather than new experiments by this article.
  snapshot_sha256: 5c1b4023c88aafa1c2530ab52d4645df0326d1f49d5fd113138ad577680da427
- evidence_id: ciliary-base-agent-A0A2K3DWT6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A2K3DWT6.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism/SUBCELLULAR
    LOCATION.
  accessed_at: '2026-10-21T09:08:34.746854Z'
  support: supports
  summary: Primary unreviewed entry A0A2K3DWT6 has native ORF CHLRE_03g167550v5, the
    exact recorded Cep290-domain protein label and taxon3055. Its location is automatic
    ARBA, not experimentally curated. The record uses it as identity-only support.
  snapshot_sha256: 2e8f6214c08ae3f786a8184d814b6051335991d83e2d80d7c2a0081942e0fd49
- evidence_id: ciliary-base-agent-A0A2K3D4W1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A2K3D4W1.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism/comments.
  accessed_at: '2026-10-21T09:08:34.717710Z'
  support: supports
  summary: Primary unreviewed entry A0A2K3D4W1 has native ORF CHLRE_12g531400v5, exact
    Nephrocystin-4 label and taxon3055; no location comment is imported as experimental
    evidence.
  snapshot_sha256: 16666df8d22774e12fe41876dd64b8922335b09df8275a3adaf57c1601b4ace7
- evidence_id: ciliary-base-agent-mapping-gene5728998
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&id=5728998&retmode=xml
  locator: 'Entrezgene_gene/Gene-ref: locus-tag, Phytozome Dbtag and formal-name.'
  accessed_at: '2026-10-21T09:17:38.548696Z'
  support: supports
  summary: NCBI Gene5728998 links the exact CHLRE_03g167550v5 locus tag to Phytozome
    Cre03.g167550. The official name here is uncharacterized protein; the record does
    not gain a literal CEP290 symbol from this database alone.
  snapshot_sha256: 1c06ae2af4dcfaa1597ee1154b9c15e543b0180c4b2e239d20b1142f3a2ccf2d
- evidence_id: ciliary-base-agent-mapping-gene5718574
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&id=5718574&retmode=xml
  locator: 'Entrezgene_gene/Gene-ref: locus-tag, Phytozome Dbtag and formal-name.'
  accessed_at: '2026-10-21T09:17:38.550698Z'
  support: supports
  summary: NCBI Gene5718574 links the exact CHLRE_12g531400v5 locus tag to Phytozome
    Cre12.g531400. The official name here is uncharacterized protein; the published
    symbol bridge is a separate source.
  snapshot_sha256: a56838b49bdc08ba5f4c60d5269976165461534e61d7e16e5ba5e2afc5824cd8
- evidence_id: ciliary-base-agent-mapping-fauser2022-pdf
  kind: primary_source
  reference: https://www.nature.com/articles/s41588-022-01052-9.pdf
  locator: Printed p709, Fig4d first two rows and entire caption, PDF page5 visually
    inspected; DOI10.1038/s41588-022-01052-9.
  accessed_at: '2026-10-21T09:18:03.906700Z'
  support: supports
  summary: The primary Fauser2022 article explicitly labels Cre03.g167550 as CEP290
    and Cre12.g531400 as NPHP4 in Fig4d. Together with the native locus cross-references
    this verifies both record gene mappings. This bounded use establishes a published
    locus/symbol bridge, not a new localization assay or a claim that UniProt literally
    contains these symbols.
  snapshot_sha256: fc5fa7785f0d6d090731947488ad8c54ef8e439d1fa51ec4c3067b7a7b451594
- evidence_id: ciliary-base-agent-reviewed-gene-search
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACEP290%20OR%20gene_exact%3ANPHP4%29%20AND%20organism_id%3A3055%20AND%20reviewed%3Atrue&format=json&size=100
  locator: results array; native HTTP200 JSON.
  accessed_at: '2026-10-21T09:21:49.524765Z'
  support: supports
  summary: The exact reviewed CEP290/NPHP4 query at taxon3055 returns an empty results
    array. This supports using the verified unreviewed examples within the bounded
    gene-symbol search; it is not a claim that no reviewed entry could exist under
    any other alias.
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: Remote UniProt query exactly (gene_exact:CEP290 OR gene_exact:NPHP4)
    AND organism_id:3055 AND reviewed:true, JSON size100; zero returned entries. Other
    aliases/species were not searched. Ignored local files are not applicable to this
    remote query; no local absence claim.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/appendage/ciliary_base.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:07:06Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/ciliary_base.yaml'
  snapshot_sha256: 1d1ec31a0422b5d2ad596eca76ea48621ec0e4a411b264f83f83438136cc995d
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/appendage/ciliary_base.yaml --out
    /private/tmp/cellstructure-batch15-20261021-ohdkgt21/ciliary_base-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:07:10Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/appendage/ciliary_base.yaml\
    \ --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/ciliary_base-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch15-20261021-ohdkgt21/ciliary_base-strict.tsv"
  snapshot_sha256: 52b6ab6389f4780504aa471843f3f5c00f59477ec001c944965da3b880237cf7
- evidence_id: verify-result
  kind: validation
  reference: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml
    --verify
  locator: Read-only native target diagnostic log
  accessed_at: '2026-10-21T09:14:39Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: causal-graphs-result
  kind: validation
  reference: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml
    --causal-graphs
  locator: Read-only native target diagnostic log
  accessed_at: '2026-10-21T09:14:39Z'
  support: supports
  summary: "data/structures/appendage/ciliary_base.yaml  (GO:0097546)\n  ciliary_base_mechanism\t\
    transition_zone_protein_network\tCOVERED\t->transition_zone_protein_network (UniProtKB:A0A2K3DWT6,\
    \ UniProtKB:A0A2K3D4W1)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1\
    \  COVERED                   component_ref target holds protein_examples covering\
    \ all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref target\
    \ holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref\
    \ on the node\n     1  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 325ed6b53bc03abedd11adb2cf82cbf4272024d558150b70a030008c54cb7ddf
- evidence_id: target-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/ciliary_base.yaml; exact native collect() target
    slice of original fresh-base TSV
  accessed_at: '2026-10-21T09:47:05.884607Z'
  support: supports
  summary: 12 of 12 exact target identifiers returned OK. No target residuals. The
    shared command exit zero is not interpreted as successful network resolution for
    transport failures.
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: identity
  area: identity
  topic: Ciliary base versus transition zone
  outcome: supported
  target_ids:
  - GO:0097546
  summary: Exact GO identity, SUBCELLULAR_REGION kind, cilium parthood and four synonyms
    are supported. The base includes the TZ but is broader than it. The appended IFT/diffusion
    narrative is literature-level explanation beyond the GO definition and is assessed
    through the cited gate review, not attributed wholly to GO.
  evidence_ids:
  - ciliary-base-agent-go
  - ciliary-base-agent-garcia2017-pmc-retry
  - record
- assessment_id: composition
  area: completeness
  topic: Known non-TZ regions omitted
  outcome: concern
  target_ids:
  - GO:0097546
  summary: All three component rows and constituent graph nodes describe the TZ, while
    the exact base definition includes distal basal body and transition fibers. This
    is a bounded known-region completeness gap, not a demand to enumerate all proteins
    or fill arbitrary optional slots.
  evidence_ids:
  - ciliary-base-agent-go
  - ciliary-base-agent-diener2015-pmc-retry
  - ciliary-base-agent-garcia2017-pmc-retry
  - record
- assessment_id: grounding
  area: grounding
  topic: Y-link and aggregates
  outcome: supported
  target_ids:
  - GO:0097546
  summary: The exact GO Y-link complex is grounded correctly and the historical earlier
    label-only rationale is expressly superseded. Generic TZ segment and heterogeneous
    protein-network aggregates need not be assigned a whole-axoneme or single-family
    CURIE. Unknown assembly essentiality is honest.
  evidence_ids:
  - ciliary-base-agent-go
  - ciliary-base-agent-craige2010-jats
  - ciliary-base-agent-wang2022-jats
  - record
- assessment_id: protein
  area: grounding
  topic: Two unreviewed examples
  outcome: supported
  target_ids:
  - GO:0097546
  summary: The two native accession/status/label/ORF/taxon fields match and native
    verification passes. NCBI Gene provides the CHLRE-to-Cre cross-reference and Fauser2022
    Fig4d explicitly labels the two loci CEP290 and NPHP4. The bounded exact-gene
    reviewed search returns no entries. These are identity-only examples, distinct
    from primary localization evidence. The role correctly preserves the literal UniProt
    ORF rather than claiming it is the native geneName token.
  evidence_ids:
  - ciliary-base-agent-A0A2K3DWT6
  - ciliary-base-agent-A0A2K3D4W1
  - ciliary-base-agent-tax-3055
  - ciliary-base-agent-mapping-gene5728998
  - ciliary-base-agent-mapping-gene5718574
  - ciliary-base-agent-mapping-fauser2022-pdf
  - ciliary-base-agent-reviewed-gene-search
  - ciliary-base-agent-craige2010-jats
  - ciliary-base-agent-wang2022-jats
- assessment_id: mechanism-evidence
  area: evidence
  topic: TZ tethering and gating
  outcome: supported
  target_ids:
  - GO:0097546
  summary: The primary CEP290 loss/rescue/localization study and later three-mutant
    comparisons support TZ microtubule–membrane organization and ciliary-composition
    control. Wedge loss, Y-link loss and ciliary proteomics are not interchangeable
    endpoints. No complete network, Y-link-specific mechanism or fixed assembly hierarchy
    is inferred.
  evidence_ids:
  - ciliary-base-agent-craige2010-jats
  - ciliary-base-agent-wang2022-jats
  - ciliary-base-agent-garcia2017-pmc-retry
- assessment_id: taxa
  area: scope
  topic: Chlamydomonas canonical example
  outcome: supported
  target_ids:
  - GO:0097546
  summary: The named species and isolated-TZ proteomics example are correct; mutant
    preparation and differential localization remain strain/condition-specific. Diener
    isolated TZs do not represent every physical constituent of the complete base.
  evidence_ids:
  - ciliary-base-agent-tax-3055
  - ciliary-base-agent-diener2015-pmc-retry
  - ciliary-base-agent-wang2022-jats
- assessment_id: graph
  area: graph
  topic: Static membership and gate output
  outcome: concern
  target_ids:
  - GO:0097546
  summary: The graph links TZ elements to the base, base to cilium and base to gating.
    It contains no perturbation or mechanistic intermediate connecting a specific
    constituent to gating, despite labeling the graph MECHANISTIC.
  evidence_ids:
  - ciliary-base-agent-go
  - ciliary-base-agent-craige2010-jats
  - ciliary-base-agent-wang2022-jats
  - record
  - graph-contract
- assessment_id: coverage
  area: completeness
  topic: Optional fields and provenance
  outcome: supported
  target_ids:
  - GO:0097546
  summary: All current claims and four cited bibliography identities were reviewed.
    No image or quantitative property requires a separate asset audit. Historical
    curation/access wording is not falsified merely by current accessibility.
  evidence_ids:
  - ciliary-base-agent-epmc
  - record
  - ciliary-base-agent-go
findings:
- finding_id: F1
  issue_key: ciliary-base-graph-static-mechanistic-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Represent the graph as structural context or supply causal steps
  description: The graph is a set of constituent/compartment parthood assertions plus
    a whole-base gating output. It does not explain how a named constituent, interaction
    or perturbation controls that output. Source-backed molecular mechanisms exist
    in the primary papers, but the current edge representation does not encode them.
  target_ids:
  - GO:0097546
  field_paths:
  - causal_graphs[graph_id=ciliary_base_mechanism].scope_status
  - causal_graphs[graph_id=ciliary_base_mechanism].edges
  evidence_ids:
  - record
  - graph-contract
  - ciliary-base-agent-craige2010-jats
  - ciliary-base-agent-wang2022-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_base.yaml
    role: maintained scientific record
  rule_id: review-checklist:Identity, Components, Evidence and Causal graph; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: The exact structure and most underlying membership/location
    claims remain supported. The bounded defect is an overbroad scope qualifier or
    mechanistic representation, rather than a demonstrated false experimental mechanism
    or wrong identity; calibrated as minor.
- finding_id: F2
  issue_key: ciliary-base-known-non-tz-composition-gap
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Represent the defining basal-body and transition-fiber regions
  description: The entire component inventory and constituent graph cover only transition-zone
    structures, despite the exact base definition explicitly comprising distal basal
    body, transition fibers and TZ. The cited Diener preparation expressly excludes
    transition fibers from isolated TZs, and the gate review separates those structures.
    This materially narrows the represented composition of the broad base. It does
    not require an exhaustive protein inventory or replace the base identity with
    TZ.
  target_ids:
  - GO:0097546
  field_paths:
  - components
  - causal_graphs[graph_id=ciliary_base_mechanism].nodes
  evidence_ids:
  - ciliary-base-agent-go
  - ciliary-base-agent-diener2015-pmc-retry
  - ciliary-base-agent-garcia2017-pmc-retry
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_base.yaml
    role: maintained scientific record
  rule_id: review-checklist:Identity, Components, Evidence and Causal graph; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: The record retains its exact biological identity; this bounded
    wording, grounding or completeness defect does not invalidate the supported core.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0097546
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_base.yaml
    role: maintained scientific record
  description: Mark the present graph NONMECHANISTIC, remove it, or build a bounded
    mechanism with actual constituent-to-event-to-outcome edges supported by primary
    experiments.
  acceptance_checks:
  - Separate localization/parthood from effects on tethering and protein composition.
  - Preserve organism, mutant, rescue and preparation boundaries on causal edges.
  - After separately authorized curation, use the guarded writer and native history/status
    rules; run focused schema/strict, identifier and evidence checks.
  generator: Maintained structure YAML; derived products only after authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0097546
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_base.yaml
    role: maintained scientific record
  description: Add source-backed structural representation of the distal basal-body
    and transition-fiber regions, or explicitly delimit the present component view
    as partial and identify the known missing regions for follow-up. Label-only rows
    can be used where exact scoped identifiers are unresolved.
  acceptance_checks:
  - Preserve the complete GO0097546 boundary while keeping TZ-only experimental preparations
    scoped.
  - Do not ground a distal segment to the complete basal body without a segment qualification
    or infer that isolated TZ proteomics samples transition fibers.
  - After separately authorized curation, use the guarded writer and native history/status
    rules; run focused schema/strict, identifier and evidence checks.
  generator: Maintained structure YAML; derived products only after authorized curation.
limitations:
- Native accession identity is distinct from direct experimental membership. Exact
  published CEP290/NPHP4 locus mappings are now independently verified through NCBI
  Gene and Fauser2022 Fig4d. Only the latter PDF page and relevant context were inspected;
  no whole-Fauser-paper or supplementary screen-data review is claimed.
- Diener2015 initial JATS route returned500 and the native PMC retry supplied genuine
  body; Garcia2017 likewise had500 JATS but genuine PMC review text. First sandbox
  DNS failures and retry receipts remain preserved.
- Diener vesicles are residual isolated TZs with absent outer-doublet microtubules,
  not intact full bases. Garcia2017 remains a secondary review; its broad gate context
  is not a new primary localization assay.
- The earlier Y-link label-only statement is explicitly labeled historical and superseded
  by exactGO0097537; current access and the record creation timestamp do not alone
  establish false prior curation provenance.
- The exact target resolver slice is derived from the completed fresh-base run. Any
  PMID transport failures were checked against the separately cited native literature
  metadata; these identity checks do not establish full-body scientific support.
- No raw microscopy pixels, original movies, supplementary datasets or unpublished
  data were independently reanalyzed. Figure captions and relevant body/methods prose
  were read at the listed locators. The target has no image asset or quantitative
  measurement assertion. Fauser2022 Fig4d plotted gene/locus labels and caption were
  visually inspected in the publisher PDF; that figure-pixel inspection is explicitly
  included in the locus-identity check.
- All 14 frozen repository inputs retain their inspected hashes. No neighboring local
  structure record, expression-module source or iModulonDB claim is used; no optional-empty
  finding is made.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Unsaveable clean exceptions are not manufactured; each listed finding is supported
  independently of validator results. Root alone owns finalization, save and shared
  index updates.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
