# Meiotic nuclear-membrane tether identity, source scope and function review

- Review: 20261021T094816Z-meiotic-nuclear-membrane-microtubule-tethering-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:24:16Z
- Finished UTC: 2026-10-21T09:48:16Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The membrane-tether identity, core examples and associated Bqt connector are supported. Two major findings concern transferred HAA function and broad fungal motor/distribution claims; one minor finding concerns graph classification.

## Scope And Provenance

Whole single target, all native terms, four protein examples and graph assertions; scoped primary bodies and exact older citation abstracts.

Selection: Target 5 in batch sixteen, selected in strict sorted path order from uncovered records at the fresh captured main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0034993 | data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml | maintained | meiotic nuclear membrane microtubule tethering complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native verify | passed | True | GO:0034993 | Focused native check passed; annotation coverage is not independent experimental membership evidence. |
| Native causal-graphs | passed | True | GO:0034993 | Focused native check passed; annotation coverage is not independent experimental membership evidence. |
| Expression-module applicability | not_applicable | False | GO:0034993 | No expression-module or transcriptomic dataset inference is needed for these structural claims. |
| Focused native schema | passed | True | GO:0034993 | Focused validator passed. |
| Focused native strict | passed | True | GO:0034993 | Focused validator passed. |
| Claim-level scientific review | passed | True | GO:0034993 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Target resolver slice with native transport-failure cross-checks | passed | True | GO:0034993 | 17 of 17 exact target identifiers returned OK. No target residuals. The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| Full corpus QC | passed | True | GO:0034993 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0034993 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0034993 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0034993 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0034993 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Membrane tether versus array or organizing center

identity: supported. Targets: GO:0034993.

The intended exact GO complex, is-a parent, site parthood and native synonyms are correct. The membrane bridge, rMTOC, microtubule array and entire telomere bouquet are related but distinct physical entities.

### Core bridge and associated connector

evidence: supported. Targets: GO:0034993.

Sad1/Kms1 are supported membrane-bridge constituents at the represented S.pombe scope. Bqt1/Bqt2 correctly remain associated telomere-connection machinery rather than being silently made intrinsic permanent membrane constituents. The source descriptions preserve direct observation versus cited topology background.

### Assembly necessity remains unverified

scope: unknown. Targets: GO:0034993.

The ESSENTIAL Sad1/Kms1 labels concern whether the structure forms without each component. Reviewed localization, function and bridge schematics do not independently test that endpoint. Bqt1-AID loss tests conditional telomere attachment, not disappearance of the complete membrane complex.

### Four exact native examples

grounding: supported. Targets: GO:0034993.

All four accessions, native labels, gene tokens, reviewed statuses and reference-taxon pairs match. The2017 Bqt1 and2025Kms1 evidence notes accurately preserve their experimental scopes; neither reference stock nor partial mitotic recruitment is substituted for every meiotic experiment.

### SUN protein class versus domain

grounding: supported. Targets: GO:0034993.

IPR045119 is the supported whole-protein family and agrees with native Q09825. No whole Kms1 family or Bqt1/Bqt2 complex identity is guessed from a short motif or incidental domain annotation.

### HAA function is copied onto the membrane complex

evidence: concern. Targets: GO:0034993.

The function and graph claim that this complex provides the radial microtubule array, with GO0032117 described as its exact structure definition. That term and the Hrs1 experiments concern the HAA/rMTOC system. The tether can connect structures without being the array itself.

### Fungi-wide dynein coupling exceeds the evidence

scope: concern. Targets: GO:0034993.

The native Fungi taxon is valid, but COMMON distribution and a conserved dynein-coupling note are attributed to one S.pombe Bqt study. Related fungal SUN/KASH systems can connect to actin/Myo2; generic LINC conservation is not evidence that this microtubule-specific class and motor mechanism have that broad distribution.

### Model species and reference strain

scope: supported. Targets: GO:0034993.

S.pombe is a valid model and the four sequence entries use the correct reference strain. The canonical note is a model description, not a declaration that every studied mutant stock was972h-. Ectopic2025 and auxin2017 preparations remain distinct.

### Supported topology does not supply the missing causal path

graph: concern. Targets: GO:0034993.

The graph comprises core parthood, connector association, compartment parthood and the misassigned whole-array function. Correct the function separately and narrow MECHANISTIC to the represented level, or add a source-supported tether/force-transmission transition. Atomic detail is not required.

### Bounded corrections rather than optional additions

completeness: supported. Targets: GO:0034993.

No optional image, exact stoichiometry, more family identifiers or full molecular inventory is required. Current function, scope and graph assertions are actionable; inaccessible older bodies and assembly necessity remain explicit limits.

## Findings

### F1: Keep the membrane tether distinct from the horsetail-astral array

major / open / confirmed; issue key: meiotic-membrane-tether-horsetail-array-function-transfer.

The function description and corresponding graph process/edge state that the membrane complex provides the radial microtubule array. Their GO0032117 evidence is called the exact structure definition, but that term denotes the HAA rather than GO0034993. Funaya2012 directly distinguishes array/rMTOC organization from the envelope bridge. Correct the actor/function and evidence placement without discarding the supported role in connecting chromosomes, membranes and the cytoskeleton.

### F2: Bound the taxonomic and motor claim to demonstrated systems

major / open / confirmed; issue key: meiotic-membrane-tether-fungi-dynein-scope.

The Fungi COMMON annotation and conserved dynein-coupling note are sourced to Chikashige2006, whose primary abstract establishes an S.pombe Bqt1/Bqt2 bridge. That does not demonstrate the frequency or motor mechanism of a microtubule-tethering complex across fungi. Lee2020 examines a related budding-yeast LINC/Myo2/actin system, so generic SUN/KASH conservation cannot fill that gap. This is not a claim that no other fungus has a microtubule-linked tether.

### F3: Use an honest scope for the current membership/function graph

minor / open / confirmed; issue key: meiotic-membrane-tether-static-graph-scope.

Even after correcting the copied HAA function, the graph has only constituent/compartment relations and a whole-structure output. It does not encode a tethering or force-transmission causal transition, despite MECHANISTIC scope. Use NONMECHANISTIC or represent a directly sourced transition with the proper actor and preparation.

## Recommended Actions And Acceptance Checks

### A1

Describe the supported tethering contribution and cite evidence for that exact role; reserve HAA organization and array identity for the corresponding structures.

- Do not treat a neighboring structure term as the exact identity of this complex.
- Distinguish physical linkage from microtubule nucleation, array organization and motor force generation.
- Apply only through separately authorized scientific curation, guarded writing, append-only history, rendering and native validation.

### A2

Narrow distribution/mechanism to verified taxa or provide separately inspected evidence for the broader microtubule-specific class, preserving the distinction from actin-linked LINC systems.

- COMMON at a broad taxon requires evidence beyond one studied species.
- Do not transfer specific Sad1/Kms1/Bqt or dynein identities to all fungal SUN/KASH assemblies.
- Apply only through separately authorized scientific curation, guarded writing, append-only history, rendering and native validation.

### A3

Calibrate graph scope independently of the supported physical membership statements.

- Retain valid Sad1/Kms1/Bqt relationships and correct function scope.
- A meaningful source-backed causal step suffices; no atomistic mechanism is required.
- Apply only through separately authorized scientific curation, guarded writing, append-only history, rendering and native validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml; Entire maintained YAML, every evidence and graph field | context_only | The entire resolved target was read; maintained scientific inputs remain unchanged. |
| policy | docs/CURATION.md; Identity, exact grounding, evidence and component rules, with frozen schema | context_only | Membership, assembly necessity, function and taxonomic scope are assessed separately. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Source-supported directed paths and graph scope | context_only | Parthood and whole-structure function summaries do not alone explain a causal transition. |
| tether-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030989,GO:0032117,GO:0034992,GO:0034993,GO:0106094; All five returned native term definitions, synonyms and relevant hierarchy relations | supports | GO0034993 exactly denotes a meiotic membrane-spanning microtubule tether, with verified parent, site parthood and native synonyms. GO0032117 instead denotes the distinct horsetail-astral microtubule array. |
| tether-prep-tax-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Exact returned identity, rank and aliases | supports | Native taxon284812 verifies its own identity and rank. |
| tether-prep-tax-4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; Exact returned identity, rank and aliases | supports | Native taxon4751 verifies its own identity and rank. |
| tether-prep-doi-j.cell.2006.01.048-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2006.01.048; Exact bibliographic identity and full primary abstract only | supports | Chikashige2006 primary abstract identifies Bqt1/Bqt2 together as the Rap1-Sad1 bridge in S.pombe, including ectopic mitotic assembly. This is not a pan-fungal dynein survey or a complete structural-deletion test of Sad1/Kms1. |
| tether-prep-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml; Introduction; Results2.1–2.3 and2.5; full Discussion; Methods4.1/4.3/4.5/4.6. No new supplement/pixel/movie audit | supports | Funaya2012 distinguishes the Hrs1-dependent rMTOC and radial microtubules from the SPB and nuclear-membrane bridge. Kms1 topology is cited Introduction context; direct Hrs1-Kms1/Alp4 interaction tests do not directly assay dynein recruitment. |
| tether-prep-moiseeva2017-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5674143.1/PMC5674143.1.xml; Introduction; CDK1/SPB and premature-bouquet-termination Results; Fig7caption; strain/construction/imaging/auxin Methods | supports | Bqt1-AID destruction during meiotic prophase releases telomeres from the SPB and can impair later spindle behavior. The experiment tests bouquet attachment/maintenance; it does not show destruction of every Sad1-Kms1 membrane complex. |
| tether-prep-jimenez2025-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/PMC11747273.1.xml; ResultsSections8–10 inclFigs6/7captions; MethodsSections14and17; no raw images or full supplementary audit | supports | In Rabl-deficient mitotic cells with ectopic Bqt1/Bqt2, Sad1/Kms1,Alp4 andMto1 are recruited near telomeres, but Dhc1 is not detected and a complete bouquet is not reconstituted. The maintained example correctly preserves this partial context. |
| linc-agent-csm2020-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC7181386.1/PMC7181386.1.xml; ResultsS5/S6; DiscussionS10; meiotic culture MethodsS14. No full-paper or Csm4-disposition audit | supports | Lee2020 examines a distinct budding-yeast Mps3/Mps2 system linked to Myo2 and actin. Its interaction/localization experiments and qualified model show why broad fungal LINC conservation does not by itself establish universal dynein-linked microtubule tethering. |
| tether-prep-IPR045119 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045119/; Complete family identity/type/description and member database | supports | The native whole-protein SUN1–5 family includes Sad1/UNC84-type inner-membrane proteins. The full family is distinguished from the SUN domain alone. |
| tether-prep-Q09825 | https://rest.uniprot.org/uniprotkb/Q09825.json; Identity, genes, taxon, status and family/location annotations | supports | Native Q09825 verifies the exact declared gene, name, reviewed status and reference strain284812; source-specific biological roles are evaluated independently. This UniProt entry carries the exact IPR045119 family cross-reference. |
| tether-prep-P87245 | https://rest.uniprot.org/uniprotkb/P87245.json; Identity, genes, taxon, status and family/location annotations | supports | Native P87245 verifies the exact declared gene, name, reviewed status and reference strain284812; source-specific biological roles are evaluated independently. |
| tether-prep-Q92358 | https://rest.uniprot.org/uniprotkb/Q92358.json; Identity, genes, taxon, status and family/location annotations | supports | Native Q92358 verifies the exact declared gene, name, reviewed status and reference strain284812; source-specific biological roles are evaluated independently. |
| tether-prep-Q9US52 | https://rest.uniprot.org/uniprotkb/Q9US52.json; Identity, genes, taxon, status and family/location annotations | supports | Native Q9US52 verifies the exact declared gene, name, reviewed status and reference strain284812; source-specific biological roles are evaluated independently. |
| tether-prep-doi-celldisc.2017.41-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/celldisc.2017.41; Bibliographic identity, abstract and access flags | supports | Exact cited title, authors and DOI/PMID verified; the returned abstract is kept separate from any independently read body. |
| tether-prep-doi-j.cub.2012.02.042-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2012.02.042; Bibliographic identity, abstract and access flags | supports | Exact cited title, authors and DOI/PMID verified; the returned abstract is kept separate from any independently read body. |
| tether-prep-doi-j.cub.2005.07.058-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2005.07.058; Bibliographic identity, abstract and access flags | supports | Exact cited title, authors and DOI/PMID verified; the returned abstract is kept separate from any independently read body. |
| tether-prep-doi-s41467-025-56049-9-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/s41467-025-56049-9; Bibliographic identity, abstract and access flags | supports | Exact cited title, authors and DOI/PMID verified; the returned abstract is kept separate from any independently read body. |
| native-verify | /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml --verify; Focused native command log and timestamped receipt | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml --causal-graphs; Focused native command log and timestamped receipt | supports | data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml  (GO:0034993)<br>  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism	sad1_sun_protein	COVERED	-&gt;sad1_sun_protein (UniProtKB:Q09825)<br>  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism	kms1_kash_protein	COVERED	-&gt;kms1_kash_protein (UniProtKB:P87245)<br>  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism	bqt1_bqt2_meiotic_connector	COVERED	-&gt;bqt1_bqt2_meiotic_connector (UniProtKB:Q92358, UniProtKB:Q9US52)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/meiotic_nuclear_membrane_microtubule_tethering_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/meiotic_nuclear_membrane_microtubule_tethering_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch16-20261021-fjx428vi/meiotic_nuclear_membrane_microtubule_tethering_complex-strict.tsv |
| target-curies-result | just check-curies-strict; data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml; exact native collect() target slice of original fresh-base TSV | supports | 17 of 17 exact target identifiers returned OK. No target residuals. The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Chikashige2006 full body was not recovered: publisher403, coredata-only API200, Citeseer404 and browser403. Only its native primary abstract supports the stated bridge claims. Tanaka2005 likewise remains abstract-scoped.
- Funaya2012 was read only at the recorded scientific sections and main Methods; copied supplement and figure assets were not newly analyzed. The Kms1 topology statement is cited background, not a direct dynein recruitment experiment.
- Moiseeva2017 Fig7 was read as caption and claim-bearing Results/Methods, without image-pixel or movie reanalysis. Jimenez2025 was read at Sections8–10 and14/17; its partial mitotic system does not demonstrate complete meiotic bouquet formation.
- Lee2020 is bounded contrasting evidence for an actin-linked budding-yeast system, not proof of universal absence of a microtubule-linked fungal tether. Its Csm4 structural-versus-regulatory alternatives were not resolved here.
- Sad1/Kms1 assembly necessity remains unknown; the existence or activity of a complex is not by itself a loss-of-component formation test. The review does not establish direct dynein recruitment by Kms1 from the inspected experiments alone.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the requested review is proposed for saving. The shared fresh-base resolver must be completed and its exact target slice verified before finalization.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094816Z-meiotic-nuclear-membrane-microtubule-tethering-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Meiotic nuclear-membrane tether identity, source scope and function review
started_at: '2026-10-21T09:24:16Z'
finished_at: '2026-10-21T09:48:16Z'
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
summary: The membrane-tether identity, core examples and associated Bqt connector
  are supported. Two major findings concern transferred HAA function and broad fungal
  motor/distribution claims; one minor finding concerns graph classification.
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
  - path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    sha256: 1edc92bdba11eec4c3da00ba06bd5cae3bd2593f5ba94be9d545c52a9da86049
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
- target_id: GO:0034993
  path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
  label: meiotic nuclear membrane microtubule tethering complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
scope:
  description: Whole single target, all native terms, four protein examples and graph
    assertions; scoped primary bodies and exact older citation abstracts.
  selection: Target 5 in batch sixteen, selected in strict sorted path order from
    uncovered records at the fresh captured main revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0034993
checks:
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0034993
  command: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; annotation coverage is not independent experimental
    membership evidence.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0034993
  command: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; annotation coverage is not independent experimental
    membership evidence.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0034993
  summary: No expression-module or transcriptomic dataset inference is needed for
    these structural claims.
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0034993
  command: just validate data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0034993
  command: just validate-strict data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/meiotic_nuclear_membrane_microtubule_tethering_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0034993
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - tether-prep-go
  - tether-prep-tax-284812
  - tether-prep-tax-4751
  - tether-prep-doi-j.cell.2006.01.048-meta
  - tether-prep-paper
  - tether-prep-moiseeva2017-jats
  - tether-prep-jimenez2025-jats
  - linc-agent-csm2020-jats
  - tether-prep-IPR045119
  - tether-prep-Q09825
  - tether-prep-P87245
  - tether-prep-Q92358
  - tether-prep-Q9US52
  - tether-prep-doi-celldisc.2017.41-meta
  - tether-prep-doi-j.cub.2012.02.042-meta
  - tether-prep-doi-j.cub.2005.07.058-meta
  - tether-prep-doi-s41467-025-56049-9-meta
- check_id: target-curies
  name: Target resolver slice with native transport-failure cross-checks
  status: passed
  required: true
  target_ids:
  - GO:0034993
  summary: 17 of 17 exact target identifiers returned OK. No target residuals. The
    shared command exit zero is not interpreted as successful network resolution for
    transport failures.
  evidence_ids:
  - target-curies-result
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0034993
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
  - GO:0034993
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
  - GO:0034993
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
  - GO:0034993
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
  - GO:0034993
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
  reference: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
  locator: Entire maintained YAML, every evidence and graph field
  accessed_at: '2026-10-21T09:36:32Z'
  support: context_only
  summary: The entire resolved target was read; maintained scientific inputs remain
    unchanged.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Identity, exact grounding, evidence and component rules, with frozen schema
  accessed_at: '2026-10-21T09:36:32Z'
  support: context_only
  summary: Membership, assembly necessity, function and taxonomic scope are assessed
    separately.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Source-supported directed paths and graph scope
  accessed_at: '2026-10-21T09:36:32Z'
  support: context_only
  summary: Parthood and whole-structure function summaries do not alone explain a
    causal transition.
- evidence_id: tether-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030989,GO:0032117,GO:0034992,GO:0034993,GO:0106094
  locator: All five returned native term definitions, synonyms and relevant hierarchy
    relations
  accessed_at: '2026-10-21T09:25:46.766116Z'
  support: supports
  summary: GO0034993 exactly denotes a meiotic membrane-spanning microtubule tether,
    with verified parent, site parthood and native synonyms. GO0032117 instead denotes
    the distinct horsetail-astral microtubule array.
  snapshot_sha256: 1ca86216e19f89b64e2249ec78841fd33387808beb5715ef3db699bd86af381d
- evidence_id: tether-prep-tax-284812
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Exact returned identity, rank and aliases
  accessed_at: '2026-10-21T09:25:47.322140Z'
  support: supports
  summary: Native taxon284812 verifies its own identity and rank.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: tether-prep-tax-4751
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: Exact returned identity, rank and aliases
  accessed_at: '2026-10-21T09:25:47.390608Z'
  support: supports
  summary: Native taxon4751 verifies its own identity and rank.
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: tether-prep-doi-j.cell.2006.01.048-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2006.01.048
  locator: Exact bibliographic identity and full primary abstract only
  accessed_at: '2026-10-21T09:25:52.864043Z'
  support: supports
  summary: Chikashige2006 primary abstract identifies Bqt1/Bqt2 together as the Rap1-Sad1
    bridge in S.pombe, including ectopic mitotic assembly. This is not a pan-fungal
    dynein survey or a complete structural-deletion test of Sad1/Kms1.
  snapshot_sha256: fd5cac1bd8170b876a62b1c8047774632bb68ee6b345e9e7f6748cd5ef216a78
- evidence_id: tether-prep-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml
  locator: Introduction; Results2.1–2.3 and2.5; full Discussion; Methods4.1/4.3/4.5/4.6.
    No new supplement/pixel/movie audit
  accessed_at: '2026-10-21T07:08:03.849693Z'
  support: supports
  summary: Funaya2012 distinguishes the Hrs1-dependent rMTOC and radial microtubules
    from the SPB and nuclear-membrane bridge. Kms1 topology is cited Introduction
    context; direct Hrs1-Kms1/Alp4 interaction tests do not directly assay dynein
    recruitment.
  snapshot_sha256: 59f662c998abf622fbb9bccbabc3867cb5ffd3174943cc52cb6228b1e35cd93d
- evidence_id: tether-prep-moiseeva2017-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5674143.1/PMC5674143.1.xml
  locator: Introduction; CDK1/SPB and premature-bouquet-termination Results; Fig7caption;
    strain/construction/imaging/auxin Methods
  accessed_at: '2026-10-21T09:27:43.695545Z'
  support: supports
  summary: Bqt1-AID destruction during meiotic prophase releases telomeres from the
    SPB and can impair later spindle behavior. The experiment tests bouquet attachment/maintenance;
    it does not show destruction of every Sad1-Kms1 membrane complex.
  snapshot_sha256: e5b2fc8c46775b2f6a9e0b176bb16d6f2bae801e78e90b191369414ca23f84a3
- evidence_id: tether-prep-jimenez2025-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/PMC11747273.1.xml
  locator: ResultsSections8–10 inclFigs6/7captions; MethodsSections14and17; no raw
    images or full supplementary audit
  accessed_at: '2026-10-21T08:24:58.921258Z'
  support: supports
  summary: In Rabl-deficient mitotic cells with ectopic Bqt1/Bqt2, Sad1/Kms1,Alp4
    andMto1 are recruited near telomeres, but Dhc1 is not detected and a complete
    bouquet is not reconstituted. The maintained example correctly preserves this
    partial context.
  snapshot_sha256: 1e0470a799e49976e35584be8e8449af77c2e85fd1e11576a460227cd526e4ed
- evidence_id: linc-agent-csm2020-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7181386.1/PMC7181386.1.xml
  locator: ResultsS5/S6; DiscussionS10; meiotic culture MethodsS14. No full-paper
    or Csm4-disposition audit
  accessed_at: '2026-10-21T09:25:46.270923Z'
  support: supports
  summary: Lee2020 examines a distinct budding-yeast Mps3/Mps2 system linked to Myo2
    and actin. Its interaction/localization experiments and qualified model show why
    broad fungal LINC conservation does not by itself establish universal dynein-linked
    microtubule tethering.
  snapshot_sha256: fc2ee1f306bcb93fb50bd1335c1a60bdd901b50f1ece7f7b1f8c63371a362c9a
- evidence_id: tether-prep-IPR045119
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045119/
  locator: Complete family identity/type/description and member database
  accessed_at: '2026-10-21T09:25:49.694779Z'
  support: supports
  summary: The native whole-protein SUN1–5 family includes Sad1/UNC84-type inner-membrane
    proteins. The full family is distinguished from the SUN domain alone.
  snapshot_sha256: ebf2e470f10e591fe8475c39ac5142261438a51a9bba2571c0282d80a75d359e
- evidence_id: tether-prep-Q09825
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q09825.json
  locator: Identity, genes, taxon, status and family/location annotations
  accessed_at: '2026-10-21T09:25:47.372425Z'
  support: supports
  summary: Native Q09825 verifies the exact declared gene, name, reviewed status and
    reference strain284812; source-specific biological roles are evaluated independently.
    This UniProt entry carries the exact IPR045119 family cross-reference.
  snapshot_sha256: af97b71167c7297318086add00ac1143a9ab78a2f714035f76ff4c31bf77993d
- evidence_id: tether-prep-P87245
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P87245.json
  locator: Identity, genes, taxon, status and family/location annotations
  accessed_at: '2026-10-21T09:25:47.356590Z'
  support: supports
  summary: Native P87245 verifies the exact declared gene, name, reviewed status and
    reference strain284812; source-specific biological roles are evaluated independently.
  snapshot_sha256: 84aa928d02abba093e6be0c791d5d9f775268e8701d7955ab7f7d7cbb36eb234
- evidence_id: tether-prep-Q92358
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q92358.json
  locator: Identity, genes, taxon, status and family/location annotations
  accessed_at: '2026-10-21T09:25:47.407587Z'
  support: supports
  summary: Native Q92358 verifies the exact declared gene, name, reviewed status and
    reference strain284812; source-specific biological roles are evaluated independently.
  snapshot_sha256: f4cfccab706bbf9515cd342b8bf6a7409bdb96c9a45f0e6ac5320e967827dd42
- evidence_id: tether-prep-Q9US52
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9US52.json
  locator: Identity, genes, taxon, status and family/location annotations
  accessed_at: '2026-10-21T09:25:48.035040Z'
  support: supports
  summary: Native Q9US52 verifies the exact declared gene, name, reviewed status and
    reference strain284812; source-specific biological roles are evaluated independently.
  snapshot_sha256: 51cfcf49971d8963b57f32b278b49e710b600813b392a15565ffb4b80b2b09e9
- evidence_id: tether-prep-doi-celldisc.2017.41-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/celldisc.2017.41
  locator: Bibliographic identity, abstract and access flags
  accessed_at: '2026-10-21T09:25:49.062762Z'
  support: supports
  summary: Exact cited title, authors and DOI/PMID verified; the returned abstract
    is kept separate from any independently read body.
  snapshot_sha256: 7fa2f4851a8c430ea5d36bebfc02128e84cb4924adb9619c1a567b838b560b4e
- evidence_id: tether-prep-doi-j.cub.2012.02.042-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2012.02.042
  locator: Bibliographic identity, abstract and access flags
  accessed_at: '2026-10-21T09:25:49.253118Z'
  support: supports
  summary: Exact cited title, authors and DOI/PMID verified; the returned abstract
    is kept separate from any independently read body.
  snapshot_sha256: 829ab7ca0ecd9b0754bb91275c65d289b02940e0336937b39ae31e5c1abbf8e3
- evidence_id: tether-prep-doi-j.cub.2005.07.058-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2005.07.058
  locator: Bibliographic identity, abstract and access flags
  accessed_at: '2026-10-21T09:25:55.625489Z'
  support: supports
  summary: Exact cited title, authors and DOI/PMID verified; the returned abstract
    is kept separate from any independently read body.
  snapshot_sha256: b774d7d9ae22e94d9758b59c0f24de4bda443578035c5a69ac6db64622120e93
- evidence_id: tether-prep-doi-s41467-025-56049-9-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/s41467-025-56049-9
  locator: Bibliographic identity, abstract and access flags
  accessed_at: '2026-10-21T09:25:49.895418Z'
  support: supports
  summary: Exact cited title, authors and DOI/PMID verified; the returned abstract
    is kept separate from any independently read body.
  snapshot_sha256: 325789797eecd5b9eeed48935df51e17787ef0c6e6f55cbec5ce4ffebe708d6f
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    --verify
  locator: Focused native command log and timestamped receipt
  accessed_at: '2026-10-21T09:29:54.522617Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    --causal-graphs
  locator: Focused native command log and timestamped receipt
  accessed_at: '2026-10-21T09:29:55.214286Z'
  support: supports
  summary: "data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml\
    \  (GO:0034993)\n  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism\t\
    sad1_sun_protein\tCOVERED\t->sad1_sun_protein (UniProtKB:Q09825)\n  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism\t\
    kms1_kash_protein\tCOVERED\t->kms1_kash_protein (UniProtKB:P87245)\n  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism\t\
    bqt1_bqt2_meiotic_connector\tCOVERED\t->bqt1_bqt2_meiotic_connector (UniProtKB:Q92358,\
    \ UniProtKB:Q9US52)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: addf76366f950d0c7e95a3a7a7ceeb1985f206c317d1360884964f7376c472f9
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:24:18Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml'
  snapshot_sha256: bd3f07c5866426114d6d6f6f253d94fe8898ce1d27cdb7f03780ab9b8621b092
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/meiotic_nuclear_membrane_microtubule_tethering_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:24:19Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml\
    \ --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/meiotic_nuclear_membrane_microtubule_tethering_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch16-20261021-fjx428vi/meiotic_nuclear_membrane_microtubule_tethering_complex-strict.tsv"
  snapshot_sha256: bcc37ea5552eeab6f7101401fcf91bd1f0d51948077cfbc3825978e6066da47d
- evidence_id: target-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml;
    exact native collect() target slice of original fresh-base TSV
  accessed_at: '2026-10-21T09:48:00.228267Z'
  support: supports
  summary: 17 of 17 exact target identifiers returned OK. No target residuals. The
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
  topic: Membrane tether versus array or organizing center
  outcome: supported
  target_ids:
  - GO:0034993
  summary: The intended exact GO complex, is-a parent, site parthood and native synonyms
    are correct. The membrane bridge, rMTOC, microtubule array and entire telomere
    bouquet are related but distinct physical entities.
  evidence_ids:
  - tether-prep-go
  - tether-prep-paper
  - tether-prep-doi-j.cell.2006.01.048-meta
  - record
- assessment_id: composition
  area: evidence
  topic: Core bridge and associated connector
  outcome: supported
  target_ids:
  - GO:0034993
  summary: Sad1/Kms1 are supported membrane-bridge constituents at the represented
    S.pombe scope. Bqt1/Bqt2 correctly remain associated telomere-connection machinery
    rather than being silently made intrinsic permanent membrane constituents. The
    source descriptions preserve direct observation versus cited topology background.
  evidence_ids:
  - tether-prep-doi-j.cell.2006.01.048-meta
  - tether-prep-paper
  - tether-prep-moiseeva2017-jats
  - tether-prep-jimenez2025-jats
  - tether-prep-IPR045119
  - tether-prep-Q09825
  - tether-prep-P87245
  - tether-prep-Q92358
  - tether-prep-Q9US52
  - record
- assessment_id: necessity
  area: scope
  topic: Assembly necessity remains unverified
  outcome: unknown
  target_ids:
  - GO:0034993
  summary: The ESSENTIAL Sad1/Kms1 labels concern whether the structure forms without
    each component. Reviewed localization, function and bridge schematics do not independently
    test that endpoint. Bqt1-AID loss tests conditional telomere attachment, not disappearance
    of the complete membrane complex.
  evidence_ids:
  - tether-prep-go
  - tether-prep-doi-j.cell.2006.01.048-meta
  - tether-prep-paper
  - tether-prep-moiseeva2017-jats
  - record
  - policy
- assessment_id: proteins
  area: grounding
  topic: Four exact native examples
  outcome: supported
  target_ids:
  - GO:0034993
  summary: All four accessions, native labels, gene tokens, reviewed statuses and
    reference-taxon pairs match. The2017 Bqt1 and2025Kms1 evidence notes accurately
    preserve their experimental scopes; neither reference stock nor partial mitotic
    recruitment is substituted for every meiotic experiment.
  evidence_ids:
  - tether-prep-Q09825
  - tether-prep-P87245
  - tether-prep-Q92358
  - tether-prep-Q9US52
  - tether-prep-tax-284812
  - tether-prep-tax-4751
  - tether-prep-moiseeva2017-jats
  - tether-prep-jimenez2025-jats
  - tether-prep-doi-j.cell.2006.01.048-meta
  - record
- assessment_id: family
  area: grounding
  topic: SUN protein class versus domain
  outcome: supported
  target_ids:
  - GO:0034993
  summary: IPR045119 is the supported whole-protein family and agrees with native
    Q09825. No whole Kms1 family or Bqt1/Bqt2 complex identity is guessed from a short
    motif or incidental domain annotation.
  evidence_ids:
  - tether-prep-IPR045119
  - tether-prep-Q09825
  - tether-prep-P87245
  - tether-prep-Q92358
  - tether-prep-Q9US52
  - record
- assessment_id: function
  area: evidence
  topic: HAA function is copied onto the membrane complex
  outcome: concern
  target_ids:
  - GO:0034993
  summary: The function and graph claim that this complex provides the radial microtubule
    array, with GO0032117 described as its exact structure definition. That term and
    the Hrs1 experiments concern the HAA/rMTOC system. The tether can connect structures
    without being the array itself.
  evidence_ids:
  - tether-prep-go
  - tether-prep-paper
  - tether-prep-doi-j.cub.2005.07.058-meta
  - tether-prep-doi-j.cell.2006.01.048-meta
  - record
- assessment_id: taxonomy
  area: scope
  topic: Fungi-wide dynein coupling exceeds the evidence
  outcome: concern
  target_ids:
  - GO:0034993
  summary: The native Fungi taxon is valid, but COMMON distribution and a conserved
    dynein-coupling note are attributed to one S.pombe Bqt study. Related fungal SUN/KASH
    systems can connect to actin/Myo2; generic LINC conservation is not evidence that
    this microtubule-specific class and motor mechanism have that broad distribution.
  evidence_ids:
  - tether-prep-doi-j.cell.2006.01.048-meta
  - linc-agent-csm2020-jats
  - tether-prep-go
  - tether-prep-tax-284812
  - tether-prep-tax-4751
  - record
- assessment_id: canonical
  area: scope
  topic: Model species and reference strain
  outcome: supported
  target_ids:
  - GO:0034993
  summary: S.pombe is a valid model and the four sequence entries use the correct
    reference strain. The canonical note is a model description, not a declaration
    that every studied mutant stock was972h-. Ectopic2025 and auxin2017 preparations
    remain distinct.
  evidence_ids:
  - tether-prep-doi-j.cell.2006.01.048-meta
  - tether-prep-moiseeva2017-jats
  - tether-prep-jimenez2025-jats
  - tether-prep-tax-284812
  - tether-prep-tax-4751
  - record
- assessment_id: graph
  area: graph
  topic: Supported topology does not supply the missing causal path
  outcome: concern
  target_ids:
  - GO:0034993
  summary: The graph comprises core parthood, connector association, compartment parthood
    and the misassigned whole-array function. Correct the function separately and
    narrow MECHANISTIC to the represented level, or add a source-supported tether/force-transmission
    transition. Atomic detail is not required.
  evidence_ids:
  - tether-prep-go
  - tether-prep-paper
  - tether-prep-doi-j.cell.2006.01.048-meta
  - record
  - graph-policy
- assessment_id: completeness
  area: completeness
  topic: Bounded corrections rather than optional additions
  outcome: supported
  target_ids:
  - GO:0034993
  summary: No optional image, exact stoichiometry, more family identifiers or full
    molecular inventory is required. Current function, scope and graph assertions
    are actionable; inaccessible older bodies and assembly necessity remain explicit
    limits.
  evidence_ids:
  - tether-prep-go
  - tether-prep-doi-j.cell.2006.01.048-meta
  - tether-prep-paper
  - record
  - policy
findings:
- finding_id: F1
  issue_key: meiotic-membrane-tether-horsetail-array-function-transfer
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Keep the membrane tether distinct from the horsetail-astral array
  description: The function description and corresponding graph process/edge state
    that the membrane complex provides the radial microtubule array. Their GO0032117
    evidence is called the exact structure definition, but that term denotes the HAA
    rather than GO0034993. Funaya2012 directly distinguishes array/rMTOC organization
    from the envelope bridge. Correct the actor/function and evidence placement without
    discarding the supported role in connecting chromosomes, membranes and the cytoskeleton.
  target_ids:
  - GO:0034993
  field_paths:
  - functions[function_id=horsetail_movement]
  - evidence[reference=GO:0032117]
  - causal_graphs[graph_id=meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism].nodes[node_id=horsetail_movement]
  - causal_graphs[graph_id=meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism].edges[object=horsetail_movement]
  evidence_ids:
  - tether-prep-go
  - tether-prep-paper
  - tether-prep-doi-j.cell.2006.01.048-meta
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: major
  normalization_reason: The represented structure is assigned a materially different
    structure function or an unsupported broad taxonomic mechanism.
- finding_id: F2
  issue_key: meiotic-membrane-tether-fungi-dynein-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Bound the taxonomic and motor claim to demonstrated systems
  description: The Fungi COMMON annotation and conserved dynein-coupling note are
    sourced to Chikashige2006, whose primary abstract establishes an S.pombe Bqt1/Bqt2
    bridge. That does not demonstrate the frequency or motor mechanism of a microtubule-tethering
    complex across fungi. Lee2020 examines a related budding-yeast LINC/Myo2/actin
    system, so generic SUN/KASH conservation cannot fill that gap. This is not a claim
    that no other fungus has a microtubule-linked tether.
  target_ids:
  - GO:0034993
  field_paths:
  - taxonomic_distribution[taxon_id=NCBITaxon:4751]
  - definition
  evidence_ids:
  - tether-prep-doi-j.cell.2006.01.048-meta
  - linc-agent-csm2020-jats
  - tether-prep-go
  - tether-prep-tax-284812
  - tether-prep-tax-4751
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: major
  normalization_reason: The represented structure is assigned a materially different
    structure function or an unsupported broad taxonomic mechanism.
- finding_id: F3
  issue_key: meiotic-membrane-tether-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Use an honest scope for the current membership/function graph
  description: Even after correcting the copied HAA function, the graph has only constituent/compartment
    relations and a whole-structure output. It does not encode a tethering or force-transmission
    causal transition, despite MECHANISTIC scope. Use NONMECHANISTIC or represent
    a directly sourced transition with the proper actor and preparation.
  target_ids:
  - GO:0034993
  field_paths:
  - causal_graphs[graph_id=meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism].scope_status
  evidence_ids:
  - tether-prep-doi-j.cell.2006.01.048-meta
  - tether-prep-paper
  - tether-prep-moiseeva2017-jats
  - record
  - graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: minor
  normalization_reason: The supported identity and basic biology remain intact; this
    is a bounded source-attribution or graph-representation defect.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0034993
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  description: Describe the supported tethering contribution and cite evidence for
    that exact role; reserve HAA organization and array identity for the corresponding
    structures.
  acceptance_checks:
  - Do not treat a neighboring structure term as the exact identity of this complex.
  - Distinguish physical linkage from microtubule nucleation, array organization and
    motor force generation.
  - Apply only through separately authorized scientific curation, guarded writing,
    append-only history, rendering and native validation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0034993
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  description: Narrow distribution/mechanism to verified taxa or provide separately
    inspected evidence for the broader microtubule-specific class, preserving the
    distinction from actin-linked LINC systems.
  acceptance_checks:
  - COMMON at a broad taxon requires evidence beyond one studied species.
  - Do not transfer specific Sad1/Kms1/Bqt or dynein identities to all fungal SUN/KASH
    assemblies.
  - Apply only through separately authorized scientific curation, guarded writing,
    append-only history, rendering and native validation.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0034993
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  description: Calibrate graph scope independently of the supported physical membership
    statements.
  acceptance_checks:
  - Retain valid Sad1/Kms1/Bqt relationships and correct function scope.
  - A meaningful source-backed causal step suffices; no atomistic mechanism is required.
  - Apply only through separately authorized scientific curation, guarded writing,
    append-only history, rendering and native validation.
limitations:
- 'Chikashige2006 full body was not recovered: publisher403, coredata-only API200,
  Citeseer404 and browser403. Only its native primary abstract supports the stated
  bridge claims. Tanaka2005 likewise remains abstract-scoped.'
- Funaya2012 was read only at the recorded scientific sections and main Methods; copied
  supplement and figure assets were not newly analyzed. The Kms1 topology statement
  is cited background, not a direct dynein recruitment experiment.
- Moiseeva2017 Fig7 was read as caption and claim-bearing Results/Methods, without
  image-pixel or movie reanalysis. Jimenez2025 was read at Sections8–10 and14/17;
  its partial mitotic system does not demonstrate complete meiotic bouquet formation.
- Lee2020 is bounded contrasting evidence for an actin-linked budding-yeast system,
  not proof of universal absence of a microtubule-linked fungal tether. Its Csm4 structural-versus-regulatory
  alternatives were not resolved here.
- Sad1/Kms1 assembly necessity remains unknown; the existence or activity of a complex
  is not by itself a loss-of-component formation test. The review does not establish
  direct dynein recruitment by Kms1 from the inspected experiments alone.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the requested review is proposed for saving. The shared fresh-base resolver
  must be completed and its exact target slice verified before finalization.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
