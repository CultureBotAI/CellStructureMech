# P pilus structure, assembly and protein-example provenance review

- Review: 20261020T032926Z-p-pilus-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-19T23:39:33.817714Z
- Finished UTC: 2026-10-20T03:29:26Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

P-pilus identity, six constituents, conditional species scope, two functions and all nine assembly edges are supported by inspected full texts. One minor current UniProt selection-provenance issue affects PapA/PapG example notes; the protein assignments themselves remain supported.

## Scope And Provenance

Complete maintained record, all present claim-bearing fields and every causal edge.

Selection: Sixth target in the second fixed path-sorted group of previously unreviewed records; one target only.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:p_pilus | data/structures/appendage/p_pilus.yaml | maintained | P pilus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Open schema validation | passed | True | cellstructuremech:p_pilus | Focused check exited 0 with no validation errors; 2026-10-19T23:39:34.553125+00:00 to 2026-10-19T23:39:35.337079+00:00. |
| Closed schema validation | passed | True | cellstructuremech:p_pilus | Focused check exited 0 with no validation errors; 2026-10-19T23:39:35.337430+00:00 to 2026-10-19T23:39:36.645254+00:00. |
| All-field source and identifier inspection | passed | True | cellstructuremech:p_pilus | All five cited papers were read through public full-text routes. All eight UniProt accessions, the GO parent, taxon, local identity and publication identities were checked. Each of nine graph edges was assessed. The provenance wording defect is recorded separately. |
| Verbatim snippet applicability | not_applicable | False | cellstructuremech:p_pilus | The complete record contains no snippet fields; no quotation was added. |
| Target resolver coverage including residuals | passed | True | cellstructuremech:p_pilus | Collected values resolve through shared report plus scoped PDB/local receipts; scientific claim support is separately assessed. |
| Full corpus QC | passed | True | cellstructuremech:p_pilus | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:p_pilus | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:p_pilus | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:p_pilus | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:p_pilus | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### P-pilus identity, synonyms and generic parent

identity: supported. Targets: cellstructuremech:p_pilus.

The record denotes a named chaperone-usher appendage, distinct from the broader pilus class, a single protein and the assembly machinery. The definition, exact pyelonephritis-associated/P-fimbria synonyms and related Pap-pilus synonym are supported in context. GO:0009289 is correctly used as broader parent.

### Six constituents and scoped copy-number model

representation: supported. Targets: cellstructuremech:p_pilus.

PapA forms the repeated right-handed rod; PapG caps the distal tip; PapF, PapE and PapK connect tip to rod; PapH terminates the basal chain. Approximate large PapA abundance is consistent with the cited roughly 10^3 scale, rather than a fixed stoichiometry. A single distal PapG is explicit; one basal PapH follows the terminal-subunit model, not a new quantitative copy-number measurement.

### Six protein examples and two machinery xrefs

grounding: concern. Targets: cellstructuremech:p_pilus.

All accession/name/status/taxon pairings are appropriate. PapGIII is a supported PapG-family representative; PapD and PapC map to the correct machinery. Current exact-gene/uniqueness explanations for PapA and PapG need correction as detailed in F1; this does not establish wrong protein membership.

### Conditional UPEC occurrence and species exemplar

scope: supported. Targets: cellstructuremech:p_pilus.

VARIABLE E. coli presence is consistent with the source’s pathogenic-lineage and regulated pap-operon scope. The canonical example is UPEC within the named species, not a claim that all E. coli express P pili. Species-level accessions do not identify the exact strain of every structural experiment.

### Assembly and receptor-mediated adhesion

evidence: supported. Targets: cellstructuremech:p_pilus.

Ordered PapD delivery/PapC assembly and PapG interaction with Gal-alpha(1-4)Gal-bearing globoseries glycolipids are supported. The record does not treat the chaperone as the polymerizing enzyme or universalize a numerical binding specificity across PapG variants.

### All nine assembly edges and ten nodes

graph: supported. Targets: cellstructuremech:p_pilus.

Edges 0–5 encode delivery, adhesin-first initiation and the PapG–PapF–PapE–PapK–PapA order supported in EcoSal. Edge 6 assigns rod construction to PapA with Cell structural evidence; edge 7 assigns termination/anchoring to PapH with Verger 2006; edge 8 assigns assembly/secretion to PapC with Hospenthal 2017. Component references resolve and the machinery/constituent distinction is preserved.

### Boundary decision and family-grounding TODO

completeness: supported. Targets: cellstructuremech:p_pilus.

The resolved PapD/PapC discussion makes a coherent appendage boundary: preassembly chaperone and membrane usher are graph machinery. Label-only family groundings and the open TODO disclose a remaining extension; no guessed domain CURIE is used. A whole-family grounding search was not represented as exhaustive.

### Scientific status and citation identities

provenance: supported. Targets: cellstructuremech:p_pilus.

PROPOSED status and agent curation remain explicit. Publication identities match the five sources; relevant historical boundary refinements remain visible. F1 addresses current protein-example wording, not an unsupported claim about what a historical query returned.

### Optional images, traits, datasets and measurements

completeness: not_applicable. Targets: cellstructuremech:p_pilus.

There are no image licences, physical-property measurements, cross-corpus trait links or expression-module assertions to verify. Their absence does not require invented content.

## Findings

### F1: PapA and PapG example notes overstate exact UniProt gene-selection provenance

minor / open / confirmed; issue key: p-pilus-protein-example-exact-gene-provenance.

The current PapA example calls P04127 the single reviewed papA entry at taxon 562, but the exact-gene query also returns P62607, whose primary name is F7-2 and synonym is papA. The current PapG example calls P42188 the single reviewed entry for gene papG; P42188 instead has primary gene papGIII and synonym prsG, and the exact papG query returns no hit at taxon 562. Both chosen accessions remain biologically appropriate representatives. Clarify the selection rules and distinguish a PapG-family representative from an exact-symbol match; do not rewrite historical query results without historical evidence.

## Recommended Actions And Acceptance Checks

### A1

Describe P04127 as a representative reviewed PapA entry, or explicitly justify a primary-name-only rule. Describe P42188 as the PapGIII member of the PapG adhesin family without claiming an exact papG synonym or unique exact-gene hit. Preserve correct accessions, labels and species pairing.

- Repeat and retain current exact-gene/exact-species UniProt queries including synonyms; compare revised statements with P04127, P62607 and P42188 gene fields.
- Verify PapGIII family/function attribution separately from exact gene spelling.
- After separately authorized curation, use the guarded writer and both history surfaces, then run focused just validate / just validate-strict and native generated-product/QC gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/p_pilus.yaml; Entire record: identity and three synonyms; six components/protein examples; one taxonomic row and example; two functions; ten nodes and all nine graph edges; two discussions and six curation events | supports | Read the complete maintained YAML, including exact UniProt-selection wording. No snippet, physical-property, image, trait-link, dataset or source-composition field is present. |
| ecosal-full | https://pmc.ncbi.nlm.nih.gov/articles/PMC5940347/; DOI:10.1128/ecosalplus.ESP-0007-2017 / PMC5940347; Architecture of Chaperone/Usher Pili; Chaperone-Usher Pilus Assembly; Donor Strand Exchange; The Pilus Usher; Ordered Assembly; P-pilus repertoire | supports | Inspected CU architecture, adhesion, chaperone, usher and ordered-assembly sections. They support the six structural subunits, PapD delivery/PapC assembly distinction, PapG receptor recognition, conditional UPEC occurrence and tip-to-rod ordering. PapG is the single distal adhesin; PapH terminates the linear assembly and anchors its base. |
| cell-full | https://pmc.ncbi.nlm.nih.gov/articles/PMC4715182/; DOI:10.1016/j.cell.2015.11.049 / PMC4715182; Introduction; General Architecture of the P Pilus Rod; Fig. 1; sample preparation | supports | Inspected Introduction, Results and preparation context. The study resolves the PapA helical rod by cryo-EM using rods polymerized in vitro from purified PapD:PapA. It describes roughly 1,000 PapA copies in the rod; it is not an intact-cell determination of every accessory subunit. |
| verger-full | https://pmc.ncbi.nlm.nih.gov/articles/PMC1868955/; DOI:10.1371/journal.ppat.0030073 / PMC1868955; Introduction; Results and Discussion; crystallographic context | supports | Inspected PapA structural and assembly text. The paper identifies the major rod protein, right-handed architecture and large repeated copy number, and resolves PapD-bound and donor-strand-exchanged PapA in a ternary structural context. |
| paph-full | https://pmc.ncbi.nlm.nih.gov/articles/PMC1794691/; DOI:10.1038/sj.embor.7400833 / PMC1794691; Incorporation and localization of PapH; PapH is unable to undergo DSE; PapD–PapH structure; Conclusions | supports | Inspected localization, in vitro exchange and structural experiments. PapH is incorporated at the pilus base and localized to the outer membrane; the blocked P5 pocket explains termination rather than repeated extension. These experiments support the terminal-subunit model and basal anchoring claim. |
| uniprot | https://rest.uniprot.org/uniprotkb/accessions?accessions=P04127,P42188,P08408,P08407,P62532,P07111,P15319,P07110&amp;format=json; Eight results: accession, entryType, proteinDescription, genes, organism, and PapGIII function/family annotations | supports | All eight accessions are reviewed E. coli species-node entries matching the stated proteins. P42188 has primary gene papGIII and synonym prsG, with an explicit PapG-family/P-pilus adhesin annotation; papG is not an exact current gene-name synonym. P15319 and P07110 identify PapD and PapC. The five other component accession/name/gene joins match. |
| unique | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApapA+OR+gene_exact%3ApapG+OR+gene_exact%3ApapF+OR+gene_exact%3ApapE+OR+gene_exact%3ApapK+OR+gene_exact%3ApapH%29+AND+organism_id%3A562+AND+reviewed%3Atrue&amp;format=json; Complete six-result response for the six declared component symbols with organism_id:562 AND reviewed:true | refutes | Current exact-gene, exact-species, reviewed query returns P04127 and P62607 for papA; P62607 has primary name F7-2 and synonym papA. PapE, PapF, PapK and PapH each have one exact species-node hit. This refutes the present PapA uniqueness sentence without invalidating P04127 as a representative. |
| papg-exact | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApapG+AND+organism_id%3A562+AND+reviewed%3Atrue&amp;format=json&amp;size=500; results=[] for the exact PapG query; compare P42188 genes in uniprot evidence | refutes | The complete current gene_exact:papG AND organism_id:562 AND reviewed:true response is empty. Together with P42188’s explicit papGIII/prsG fields, this refutes the exact-gene selection claim while retaining its PapG-family identity. |
| strain-examples | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApapF+OR+gene_exact%3ApapE+OR+gene_exact%3ApapK+OR+gene_exact%3ApapH%29+AND+taxonomy_id%3A562+AND+reviewed%3Atrue&amp;format=tsv&amp;fields=accession%2Cgene_names%2Corganism_id%2Corganism_name%2Creviewed&amp;size=500; Full TSV of reviewed descendant-taxon exact papE/papF/papK/papH symbol hits | supports | The broader descendant-taxon query returns additional symbol hits. Some papE/papF/papH synonyms belong to ATP-synthase proteins, so symbol matching alone cannot establish family membership. The record’s selected E. coli entries are the correct pilus proteins. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009289; results[0].id/name/isObsolete/aspect/definition | supports | GO:0009289 is the active broader pilus cellular-component term. Its scope supports is-a parentage while the P-pilus subtype retains its own local identity. |
| taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=562&amp;retmode=xml; TaxaSet/Taxon/TaxId, ScientificName and Rank | supports | NCBITaxon:562 is Escherichia coli at species rank; all six protein examples and both machinery accessions use that node. |
| go-search | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;rows=30&amp;q=P%20pilus; OLS4 GO query P pilus; returned identifiers and labels | supports | Inspected returned GO candidates for P pilus: the generic pilus and neighboring classes/processes do not provide an exact P-pilus identity in this bounded result set. |
| ecosal | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128%2Fecosalplus.ESP-0007-2017; Europe PMC resultList.result DOI/title/authorString/pubYear/PMCID | supports | The exact DOI resolves to the expected publication title, authors and year; the linked manuscript/full text was inspected separately. |
| hospenthal | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038%2Fnrmicro.2017.40; Europe PMC resultList.result DOI/title/authorString/pubYear/PMCID | supports | The exact DOI resolves to the expected publication title, authors and year; the linked manuscript/full text was inspected separately. |
| cell | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016%2Fj.cell.2015.11.049; Europe PMC resultList.result DOI/title/authorString/pubYear/PMCID | supports | The exact DOI resolves to the expected publication title, authors and year; the linked manuscript/full text was inspected separately. |
| verger | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1371%2Fjournal.ppat.0030073; Europe PMC resultList.result DOI/title/authorString/pubYear/PMCID | supports | The exact DOI resolves to the expected publication title, authors and year; the linked manuscript/full text was inspected separately. |
| paph | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038%2Fsj.embor.7400833; Europe PMC resultList.result DOI/title/authorString/pubYear/PMCID | supports | The exact DOI resolves to the expected publication title, authors and year; the linked manuscript/full text was inspected separately. |
| hospenthal-full | https://discovery.ucl.ac.uk/id/eprint/1557577/1/Hospenthal%20et%20al%20%28NRM%29_Accepted%20%28002%29.pdf; Accepted manuscript pp.4–5, CU pilus biogenesis; manuscript associated with DOI:10.1038/nrmicro.2017.40 by UCL repository item 1557577 | supports | Reused the retrieved accepted manuscript and read the CU section. It describes PapD-mediated folding/delivery to PapC, usher-mediated polymerization/secretion and P-pilus subunit order. UCL’s item page explicitly joins this accepted version to the cited DOI. |
| internal | repository working tree; Target; generic pilus parent; history/records/p_pilus/2026-09-11T020526Z-codex-844e1e.yaml and 2026-09-11T021605Z-codex-61269d.yaml | supports | The local target and its broader pilus parent resolve. Historical records document earlier PapD/PapC and PapK boundary corrections; the current distinctions are present. Historical GitHub issue dispositions are not independently re-adjudicated. |
| target-resolver-coverage | just check-curies-strict; data/structures/appendage/p_pilus.yaml; exact collect() scope; shared reports/curie_check.tsv | supports | The exact collection has 16 CURIE-shaped scalars: {'OK': 15, 'SKIPPED': 1}. Skipped PDB identifiers resolve in the attached exact deposition receipts; the minted local target resolves in the maintained record. HTTP URLs and prose are checked separately. Existence does not imply correct biological mapping. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Current UniProt queries establish present annotation wording, not the result of a query on the historical retrieval date. Historical curation events should remain append-only.
- The literature combines native-pathogen biology, recombinant complexes and in vitro rod preparations; no single exact-strain complex composition is inferred from the species-level example list.
- Approximate rod subunit abundance and the terminal-subunit model are not new direct copy-number measurements. Exact source-neutral constituent-family groundings remain an explicit open extension.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- This is a read-only scientific observation. No record, history event, generated page or native scientific status was changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T032926Z-p-pilus-review
kind: record
repository: CultureBotAI/CellStructureMech
title: P pilus structure, assembly and protein-example provenance review
started_at: '2026-10-19T23:39:33.817714Z'
finished_at: '2026-10-20T03:29:26Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Separate checkout and source inspection; prior agent authorship
    does not establish independent human review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: P-pilus identity, six constituents, conditional species scope, two functions
  and all nine assembly edges are supported by inspected full texts. One minor current
  UniProt selection-provenance issue affects PapA/PapG example notes; the protein
  assignments themselves remain supported.
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
  - path: data/structures/appendage/p_pilus.yaml
    sha256: 45d84a4b76ecf3610b1973f234eb46b639134ad39a61cd6e9432152277ac0b7e
    role: target
  - path: data/structures/appendage/pilus.yaml
    sha256: 9e7c9fc2628b1b72c3d2d289c485967d78b8be5b38b2e75300f46d6750316333
    role: context
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
  - path: history/records/p_pilus/2026-09-11T020526Z-codex-844e1e.yaml
    sha256: 1a59cb3a4d3484f253476dd3290b74077a9f6f0c38168b83974fde866aa873fd
    role: context
  - path: history/records/p_pilus/2026-09-11T021605Z-codex-61269d.yaml
    sha256: ddc5cbb960d620141b9cbf02d86ea86d11bfd241c93776d86825166ba3093373
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
- target_id: cellstructuremech:p_pilus
  path: data/structures/appendage/p_pilus.yaml
  label: P pilus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/p_pilus.yaml
    role: maintained scientific record
scope:
  description: Complete maintained record, all present claim-bearing fields and every
    causal edge.
  selection: Sixth target in the second fixed path-sorted group of previously unreviewed
    records; one target only.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:p_pilus
  exclusions:
  - target: Generic pilus and other appendage records
    reason: Used only as identity/provenance context; they do not receive scientific
      review coverage here.
checks:
- check_id: schema
  name: Open schema validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:p_pilus
  command: just validate data/structures/appendage/p_pilus.yaml
  exit_code: 0
  summary: Focused check exited 0 with no validation errors; 2026-10-19T23:39:34.553125+00:00
    to 2026-10-19T23:39:35.337079+00:00.
- check_id: strict
  name: Closed schema validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:p_pilus
  command: just validate-strict data/structures/appendage/p_pilus.yaml --out /private/tmp/cellstructure-batch2-20261019-52rdp0/p-pilus-review/strict.tsv
  exit_code: 0
  summary: Focused check exited 0 with no validation errors; 2026-10-19T23:39:35.337430+00:00
    to 2026-10-19T23:39:36.645254+00:00.
- check_id: sources
  name: All-field source and identifier inspection
  status: passed
  required: true
  target_ids:
  - cellstructuremech:p_pilus
  summary: All five cited papers were read through public full-text routes. All eight
    UniProt accessions, the GO parent, taxon, local identity and publication identities
    were checked. Each of nine graph edges was assessed. The provenance wording defect
    is recorded separately.
  evidence_ids:
  - ecosal-full
  - hospenthal-full
  - cell-full
  - verger-full
  - paph-full
  - uniprot
  - unique
  - papg-exact
  - go
  - taxon
- check_id: snippets
  name: Verbatim snippet applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:p_pilus
  summary: The complete record contains no snippet fields; no quotation was added.
- check_id: target-resolver-coverage
  name: Target resolver coverage including residuals
  status: passed
  required: true
  target_ids:
  - cellstructuremech:p_pilus
  summary: Collected values resolve through shared report plus scoped PDB/local receipts;
    scientific claim support is separately assessed.
  evidence_ids:
  - target-resolver-coverage
  - record
  - internal
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:p_pilus
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:p_pilus
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:p_pilus
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:p_pilus
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:p_pilus
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch2 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/p_pilus.yaml
  locator: 'Entire record: identity and three synonyms; six components/protein examples;
    one taxonomic row and example; two functions; ten nodes and all nine graph edges;
    two discussions and six curation events'
  accessed_at: '2026-10-19T23:39:33.817714Z'
  support: supports
  summary: Read the complete maintained YAML, including exact UniProt-selection wording.
    No snippet, physical-property, image, trait-link, dataset or source-composition
    field is present.
- evidence_id: ecosal-full
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5940347/
  locator: DOI:10.1128/ecosalplus.ESP-0007-2017 / PMC5940347; Architecture of Chaperone/Usher
    Pili; Chaperone-Usher Pilus Assembly; Donor Strand Exchange; The Pilus Usher;
    Ordered Assembly; P-pilus repertoire
  accessed_at: '2026-10-19T23:40:14.906959Z'
  support: supports
  summary: Inspected CU architecture, adhesion, chaperone, usher and ordered-assembly
    sections. They support the six structural subunits, PapD delivery/PapC assembly
    distinction, PapG receptor recognition, conditional UPEC occurrence and tip-to-rod
    ordering. PapG is the single distal adhesin; PapH terminates the linear assembly
    and anchors its base.
  snapshot_sha256: 4e43af7b8da404d7be8829fbe9b0e8447ae7137877db2d143972ec8c0ab23b35
- evidence_id: cell-full
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4715182/
  locator: DOI:10.1016/j.cell.2015.11.049 / PMC4715182; Introduction; General Architecture
    of the P Pilus Rod; Fig. 1; sample preparation
  accessed_at: '2026-10-19T23:40:14.907684Z'
  support: supports
  summary: Inspected Introduction, Results and preparation context. The study resolves
    the PapA helical rod by cryo-EM using rods polymerized in vitro from purified
    PapD:PapA. It describes roughly 1,000 PapA copies in the rod; it is not an intact-cell
    determination of every accessory subunit.
  snapshot_sha256: 0113c90072bbc6b4d589ac41bcf2abc8aaeaedbf90e0ef24c6d511e392543ab1
- evidence_id: verger-full
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1868955/
  locator: DOI:10.1371/journal.ppat.0030073 / PMC1868955; Introduction; Results and
    Discussion; crystallographic context
  accessed_at: '2026-10-19T23:40:14.907844Z'
  support: supports
  summary: Inspected PapA structural and assembly text. The paper identifies the major
    rod protein, right-handed architecture and large repeated copy number, and resolves
    PapD-bound and donor-strand-exchanged PapA in a ternary structural context.
  snapshot_sha256: f8fe085df1f8b30707b22ad7e34ef21cab06878f33910d50f82f5dda1f617408
- evidence_id: paph-full
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1794691/
  locator: DOI:10.1038/sj.embor.7400833 / PMC1794691; Incorporation and localization
    of PapH; PapH is unable to undergo DSE; PapD–PapH structure; Conclusions
  accessed_at: '2026-10-19T23:40:14.907944Z'
  support: supports
  summary: Inspected localization, in vitro exchange and structural experiments. PapH
    is incorporated at the pilus base and localized to the outer membrane; the blocked
    P5 pocket explains termination rather than repeated extension. These experiments
    support the terminal-subunit model and basal anchoring claim.
  snapshot_sha256: cc5e28eee9597b638cd4c68540fae37fa68fe70a6b374ff0149d36300c615374
- evidence_id: uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/accessions?accessions=P04127,P42188,P08408,P08407,P62532,P07111,P15319,P07110&format=json
  locator: 'Eight results: accession, entryType, proteinDescription, genes, organism,
    and PapGIII function/family annotations'
  accessed_at: '2026-10-19T23:39:35.388499Z'
  support: supports
  summary: All eight accessions are reviewed E. coli species-node entries matching
    the stated proteins. P42188 has primary gene papGIII and synonym prsG, with an
    explicit PapG-family/P-pilus adhesin annotation; papG is not an exact current
    gene-name synonym. P15319 and P07110 identify PapD and PapC. The five other component
    accession/name/gene joins match.
  snapshot_sha256: 6a32145fc6b06cf896f2232aa6bcb7147cc6e20136f37469a26f3f39e98e729b
- evidence_id: unique
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApapA+OR+gene_exact%3ApapG+OR+gene_exact%3ApapF+OR+gene_exact%3ApapE+OR+gene_exact%3ApapK+OR+gene_exact%3ApapH%29+AND+organism_id%3A562+AND+reviewed%3Atrue&format=json
  locator: Complete six-result response for the six declared component symbols with
    organism_id:562 AND reviewed:true
  accessed_at: '2026-10-19T23:39:35.389001Z'
  support: refutes
  summary: Current exact-gene, exact-species, reviewed query returns P04127 and P62607
    for papA; P62607 has primary name F7-2 and synonym papA. PapE, PapF, PapK and
    PapH each have one exact species-node hit. This refutes the present PapA uniqueness
    sentence without invalidating P04127 as a representative.
  snapshot_sha256: 6dd4e903e74ead8140b3cdc5434daef9648149da75b06cbd35b1fa7f057d81cb
- evidence_id: papg-exact
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApapG+AND+organism_id%3A562+AND+reviewed%3Atrue&format=json&size=500
  locator: results=[] for the exact PapG query; compare P42188 genes in uniprot evidence
  accessed_at: '2026-10-19T23:40:15.264334Z'
  support: refutes
  summary: The complete current gene_exact:papG AND organism_id:562 AND reviewed:true
    response is empty. Together with P42188’s explicit papGIII/prsG fields, this refutes
    the exact-gene selection claim while retaining its PapG-family identity.
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
- evidence_id: strain-examples
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApapF+OR+gene_exact%3ApapE+OR+gene_exact%3ApapK+OR+gene_exact%3ApapH%29+AND+taxonomy_id%3A562+AND+reviewed%3Atrue&format=tsv&fields=accession%2Cgene_names%2Corganism_id%2Corganism_name%2Creviewed&size=500
  locator: Full TSV of reviewed descendant-taxon exact papE/papF/papK/papH symbol
    hits
  accessed_at: '2026-10-19T23:40:15.367776Z'
  support: supports
  summary: The broader descendant-taxon query returns additional symbol hits. Some
    papE/papF/papH synonyms belong to ATP-synthase proteins, so symbol matching alone
    cannot establish family membership. The record’s selected E. coli entries are
    the correct pilus proteins.
  snapshot_sha256: 030095112030ecc3291968f5f1c8fb95338d32846f758cb01738c605a3839148
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009289
  locator: results[0].id/name/isObsolete/aspect/definition
  accessed_at: '2026-10-19T23:39:35.388869Z'
  support: supports
  summary: GO:0009289 is the active broader pilus cellular-component term. Its scope
    supports is-a parentage while the P-pilus subtype retains its own local identity.
  snapshot_sha256: bc564119fe5e6d56127346948989278deecab0f5ad24cb75366edb2d3d6d63cb
- evidence_id: taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=562&retmode=xml
  locator: TaxaSet/Taxon/TaxId, ScientificName and Rank
  accessed_at: '2026-10-19T23:39:35.388923Z'
  support: supports
  summary: NCBITaxon:562 is Escherichia coli at species rank; all six protein examples
    and both machinery accessions use that node.
  snapshot_sha256: 1d5618066f7d7b5fbf62b33b00b8928382362d9b9e017076caeb654151d980f8
- evidence_id: go-search
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&rows=30&q=P%20pilus
  locator: OLS4 GO query P pilus; returned identifiers and labels
  accessed_at: '2026-10-19T23:39:35.869620Z'
  support: supports
  summary: 'Inspected returned GO candidates for P pilus: the generic pilus and neighboring
    classes/processes do not provide an exact P-pilus identity in this bounded result
    set.'
  snapshot_sha256: 0e18fd9198156b83f9a5735f99dfcd8041d69b0a94cc7d8979b2fee51545e1a8
  search_scope: Live OLS4 query q=P pilus restricted to GO, rows=30; all returned
    candidates inspected. This is a bounded candidate search, not a claim that every
    possible GO term was exhaustively excluded.
- evidence_id: ecosal
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128%2Fecosalplus.ESP-0007-2017
  locator: Europe PMC resultList.result DOI/title/authorString/pubYear/PMCID
  accessed_at: '2026-10-19T23:39:36.083170Z'
  support: supports
  summary: The exact DOI resolves to the expected publication title, authors and year;
    the linked manuscript/full text was inspected separately.
  snapshot_sha256: 65cf333ebb01abf3f8e6b87167e0cada586c3ea253f4caa7a46d9a73071f095d
- evidence_id: hospenthal
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038%2Fnrmicro.2017.40
  locator: Europe PMC resultList.result DOI/title/authorString/pubYear/PMCID
  accessed_at: '2026-10-19T23:39:36.453829Z'
  support: supports
  summary: The exact DOI resolves to the expected publication title, authors and year;
    the linked manuscript/full text was inspected separately.
  snapshot_sha256: ae438ad4c05173f607057a1638e751a9b0adf8b8b18233bcfc8d157539d4529a
- evidence_id: cell
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016%2Fj.cell.2015.11.049
  locator: Europe PMC resultList.result DOI/title/authorString/pubYear/PMCID
  accessed_at: '2026-10-19T23:39:36.483209Z'
  support: supports
  summary: The exact DOI resolves to the expected publication title, authors and year;
    the linked manuscript/full text was inspected separately.
  snapshot_sha256: 255467a8949027ec1d337f9c90b65650b3faa41c825141e074dbde8829548606
- evidence_id: verger
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1371%2Fjournal.ppat.0030073
  locator: Europe PMC resultList.result DOI/title/authorString/pubYear/PMCID
  accessed_at: '2026-10-19T23:39:36.899521Z'
  support: supports
  summary: The exact DOI resolves to the expected publication title, authors and year;
    the linked manuscript/full text was inspected separately.
  snapshot_sha256: 3ad78a9594db6c915037cb7906e2ef0676f963a04594dd92a7afc5ef34405c97
- evidence_id: paph
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038%2Fsj.embor.7400833
  locator: Europe PMC resultList.result DOI/title/authorString/pubYear/PMCID
  accessed_at: '2026-10-19T23:39:37.110197Z'
  support: supports
  summary: The exact DOI resolves to the expected publication title, authors and year;
    the linked manuscript/full text was inspected separately.
  snapshot_sha256: 11ace5b5e148832dddbb1e88eafc4790d2bab93c16b6093cb9e04d7b2f5e8faa
- evidence_id: hospenthal-full
  kind: primary_source
  reference: https://discovery.ucl.ac.uk/id/eprint/1557577/1/Hospenthal%20et%20al%20%28NRM%29_Accepted%20%28002%29.pdf
  locator: Accepted manuscript pp.4–5, CU pilus biogenesis; manuscript associated
    with DOI:10.1038/nrmicro.2017.40 by UCL repository item 1557577
  accessed_at: '2026-10-19T23:36:40.842022Z'
  support: supports
  summary: Reused the retrieved accepted manuscript and read the CU section. It describes
    PapD-mediated folding/delivery to PapC, usher-mediated polymerization/secretion
    and P-pilus subunit order. UCL’s item page explicitly joins this accepted version
    to the cited DOI.
  snapshot_sha256: 0faaaef028c551eb3984b65bc01d747b7760d166ad8f4170f1f0e8bef80d0fc8
- evidence_id: internal
  kind: search
  reference: repository working tree
  locator: Target; generic pilus parent; history/records/p_pilus/2026-09-11T020526Z-codex-844e1e.yaml
    and 2026-09-11T021605Z-codex-61269d.yaml
  accessed_at: '2026-10-19T23:42:32Z'
  support: supports
  summary: The local target and its broader pilus parent resolve. Historical records
    document earlier PapD/PapC and PapK boundary corrections; the current distinctions
    are present. Historical GitHub issue dispositions are not independently re-adjudicated.
  search_scope: rg --no-ignore --hidden for identifier, label and slug through data/structures,
    all history, reviews/structured and conf; ignored files included. Only target
    and parent identity/provenance context were assessed.
- evidence_id: target-resolver-coverage
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/p_pilus.yaml; exact collect() scope; shared reports/curie_check.tsv
  accessed_at: '2026-10-19T23:41:41.324461Z'
  support: supports
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
  summary: 'The exact collection has 16 CURIE-shaped scalars: {''OK'': 15, ''SKIPPED'':
    1}. Skipped PDB identifiers resolve in the attached exact deposition receipts;
    the minted local target resolves in the maintained record. HTTP URLs and prose
    are checked separately. Existence does not imply correct biological mapping.'
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
  topic: P-pilus identity, synonyms and generic parent
  outcome: supported
  summary: The record denotes a named chaperone-usher appendage, distinct from the
    broader pilus class, a single protein and the assembly machinery. The definition,
    exact pyelonephritis-associated/P-fimbria synonyms and related Pap-pilus synonym
    are supported in context. GO:0009289 is correctly used as broader parent.
  target_ids:
  - cellstructuremech:p_pilus
  evidence_ids:
  - record
  - ecosal-full
  - go
  - go-search
- assessment_id: composition
  area: representation
  topic: Six constituents and scoped copy-number model
  outcome: supported
  summary: PapA forms the repeated right-handed rod; PapG caps the distal tip; PapF,
    PapE and PapK connect tip to rod; PapH terminates the basal chain. Approximate
    large PapA abundance is consistent with the cited roughly 10^3 scale, rather than
    a fixed stoichiometry. A single distal PapG is explicit; one basal PapH follows
    the terminal-subunit model, not a new quantitative copy-number measurement.
  target_ids:
  - cellstructuremech:p_pilus
  evidence_ids:
  - ecosal-full
  - cell-full
  - verger-full
  - paph-full
- assessment_id: examples
  area: grounding
  topic: Six protein examples and two machinery xrefs
  outcome: concern
  summary: All accession/name/status/taxon pairings are appropriate. PapGIII is a
    supported PapG-family representative; PapD and PapC map to the correct machinery.
    Current exact-gene/uniqueness explanations for PapA and PapG need correction as
    detailed in F1; this does not establish wrong protein membership.
  target_ids:
  - cellstructuremech:p_pilus
  evidence_ids:
  - uniprot
  - unique
  - papg-exact
  - strain-examples
- assessment_id: taxon
  area: scope
  topic: Conditional UPEC occurrence and species exemplar
  outcome: supported
  summary: VARIABLE E. coli presence is consistent with the source’s pathogenic-lineage
    and regulated pap-operon scope. The canonical example is UPEC within the named
    species, not a claim that all E. coli express P pili. Species-level accessions
    do not identify the exact strain of every structural experiment.
  target_ids:
  - cellstructuremech:p_pilus
  evidence_ids:
  - ecosal-full
  - taxon
  - hospenthal-full
- assessment_id: functions
  area: evidence
  topic: Assembly and receptor-mediated adhesion
  outcome: supported
  summary: Ordered PapD delivery/PapC assembly and PapG interaction with Gal-alpha(1-4)Gal-bearing
    globoseries glycolipids are supported. The record does not treat the chaperone
    as the polymerizing enzyme or universalize a numerical binding specificity across
    PapG variants.
  target_ids:
  - cellstructuremech:p_pilus
  evidence_ids:
  - ecosal-full
  - hospenthal-full
  - uniprot
- assessment_id: graph
  area: graph
  topic: All nine assembly edges and ten nodes
  outcome: supported
  summary: Edges 0–5 encode delivery, adhesin-first initiation and the PapG–PapF–PapE–PapK–PapA
    order supported in EcoSal. Edge 6 assigns rod construction to PapA with Cell structural
    evidence; edge 7 assigns termination/anchoring to PapH with Verger 2006; edge
    8 assigns assembly/secretion to PapC with Hospenthal 2017. Component references
    resolve and the machinery/constituent distinction is preserved.
  target_ids:
  - cellstructuremech:p_pilus
  evidence_ids:
  - record
  - ecosal-full
  - cell-full
  - paph-full
  - hospenthal-full
- assessment_id: discussions
  area: completeness
  topic: Boundary decision and family-grounding TODO
  outcome: supported
  summary: 'The resolved PapD/PapC discussion makes a coherent appendage boundary:
    preassembly chaperone and membrane usher are graph machinery. Label-only family
    groundings and the open TODO disclose a remaining extension; no guessed domain
    CURIE is used. A whole-family grounding search was not represented as exhaustive.'
  target_ids:
  - cellstructuremech:p_pilus
  evidence_ids:
  - record
  - ecosal-full
  - uniprot
  - internal
- assessment_id: provenance
  area: provenance
  topic: Scientific status and citation identities
  outcome: supported
  summary: PROPOSED status and agent curation remain explicit. Publication identities
    match the five sources; relevant historical boundary refinements remain visible.
    F1 addresses current protein-example wording, not an unsupported claim about what
    a historical query returned.
  target_ids:
  - cellstructuremech:p_pilus
  evidence_ids:
  - record
  - internal
  - ecosal
  - hospenthal
  - cell
  - verger
  - paph
- assessment_id: optional
  area: completeness
  topic: Optional images, traits, datasets and measurements
  outcome: not_applicable
  summary: There are no image licences, physical-property measurements, cross-corpus
    trait links or expression-module assertions to verify. Their absence does not
    require invented content.
  target_ids:
  - cellstructuremech:p_pilus
  evidence_ids:
  - record
findings:
- finding_id: F1
  issue_key: p-pilus-protein-example-exact-gene-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: PapA and PapG example notes overstate exact UniProt gene-selection provenance
  description: The current PapA example calls P04127 the single reviewed papA entry
    at taxon 562, but the exact-gene query also returns P62607, whose primary name
    is F7-2 and synonym is papA. The current PapG example calls P42188 the single
    reviewed entry for gene papG; P42188 instead has primary gene papGIII and synonym
    prsG, and the exact papG query returns no hit at taxon 562. Both chosen accessions
    remain biologically appropriate representatives. Clarify the selection rules and
    distinguish a PapG-family representative from an exact-symbol match; do not rewrite
    historical query results without historical evidence.
  target_ids:
  - cellstructuremech:p_pilus
  field_paths:
  - components[component_id=papa_major_rod_subunit].protein_examples[uniprot_id=UniProtKB:P04127].evidence[0].notes
  - components[component_id=papg_tip_adhesin].protein_examples[uniprot_id=UniProtKB:P42188].role
  - components[component_id=papg_tip_adhesin].protein_examples[uniprot_id=UniProtKB:P42188].evidence[0].notes
  evidence_ids:
  - record
  - uniprot
  - unique
  - papg-exact
  rule_id: review-checklist:Components and Status/audit; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: Bounded current metadata-provenance wording; accession identity,
    species pairing and structural membership are retained.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/p_pilus.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Describe P04127 as a representative reviewed PapA entry, or explicitly
    justify a primary-name-only rule. Describe P42188 as the PapGIII member of the
    PapG adhesin family without claiming an exact papG synonym or unique exact-gene
    hit. Preserve correct accessions, labels and species pairing.
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:p_pilus
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/p_pilus.yaml
    role: maintained scientific record
  acceptance_checks:
  - Repeat and retain current exact-gene/exact-species UniProt queries including synonyms;
    compare revised statements with P04127, P62607 and P42188 gene fields.
  - Verify PapGIII family/function attribution separately from exact gene spelling.
  - After separately authorized curation, use the guarded writer and both history
    surfaces, then run focused just validate / just validate-strict and native generated-product/QC
    gates.
limitations:
- Current UniProt queries establish present annotation wording, not the result of
  a query on the historical retrieval date. Historical curation events should remain
  append-only.
- The literature combines native-pathogen biology, recombinant complexes and in vitro
  rod preparations; no single exact-strain complex composition is inferred from the
  species-level example list.
- Approximate rod subunit abundance and the terminal-subunit model are not new direct
  copy-number measurements. Exact source-neutral constituent-family groundings remain
  an explicit open extension.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- This is a read-only scientific observation. No record, history event, generated
  page or native scientific status was changed.
```
