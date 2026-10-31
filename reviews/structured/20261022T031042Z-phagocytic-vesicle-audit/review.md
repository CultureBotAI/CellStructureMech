# Source-backed review of phagocytic vesicle

- Review: 20261022T031042Z-phagocytic-vesicle-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:58:48Z
- Finished UTC: 2026-10-22T03:10:42Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact identity and biological topology/maturation are supported. One minor source-attribution qualification is needed; no molecular-grounding, taxon-identity or optional-inventory defect was observed.

## Scope And Provenance

One complete target. Four frozen neighboring records supply graph identity/boundary context only. Native authority entries, actual primary bodies, formation-necessity semantics and every source placement were inspected; no neighboring defect is silently transferred.

Selection: Batch37 fixed strict path order, index6; one maintained record only.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0045335 | data/structures/membrane_organelle/phagocytic_vesicle.yaml | maintained | phagocytic vesicle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0045335 | Focused validator passed. |
| Focused native strict | passed | True | GO:0045335 | Focused validator passed. |
| Native focused causal protein scope | passed | True | GO:0045335 | No GENE_OR_PROTEIN nodes or dangling protein component references are present. |
| Claim-level scientific review | passed | True | GO:0045335 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0045335 | 10 of 12 collected target identifiers returned OK. PMID:12388753: UNREACHABLE; Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity, DOI and declared PMC/null status. This separately resolves citation identity after bulk eutils414; article-body scope is stated independently.; PMID:16926386: UNREACHABLE; Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity, DOI and declared PMC/null status. This separately resolves citation identity after bulk eutils414; article-body scope is stated independently. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0045335 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0045335 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0045335 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0045335 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0045335 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact target identity and topology

identity: supported. Targets: GO:0045335.

GO0045335 exactly matches the complete definition and phagosome synonym. The cytoplasmic-vesicle parent is explicitly supported by SL0206. MembraneGO0030670 and lumenGO0097013 are typed part_of children of the whole term; all graph classes resolve to frozen local records and native authorities. Expanded claims in neighboring early/late records are not adopted.

### Label-only collective lipid material

grounding: supported. Targets: GO:0045335.

The single LIPID row denotes the lipid material of the bilayer, deliberately retaining REVIEWED_LABEL_ONLY and no GO grounding as a chemical identity. Whole membraneGO0030670 remains in has_part/graph or record identity, not substituted as lipid identity. The collective bilayer is constitutional to this membrane-bounded class; no exact molecular composition, stoichiometry or particular lipid requirement is asserted.

### Specific molecular formation requirements remain unresolved

grounding: unknown. Targets: GO:0045335.

The ontology and location authority establish a bilayer boundary, not formation-depletion tests for individual lipid species or transient proteins. Exact lipid species, ratios and their separate necessity remain unknown; this does not invalidate the collective boundary requirement.

### Species and experimental scope

scope: supported. Targets: GO:0045335.

The qualitative D.discoideum presence statement is supported by the phagocytic Ax2 studies and exact species identity. Latex beads are the biochemical model;2002 compares CatD traffic with ingested yeast. These are not a census of every strain or a universal timetable for other protists. The record does not import the neighboring Entamoeba/ciliate definitions.

### Intact phagosome proteomics example

provenance: supported. Targets: GO:0045335.

The canonical example accurately specifies purified latex-bead phagosomes, a maturation time course,2D electrophoresis and mass spectrometry. The experimental organism and source metadata match; no isolated-membrane-only assay is asserted in this example.

### Uptake and maturation are supported

evidence: supported. Targets: GO:0045335.

GO0006909/0045335 support enclosure of ingested particulate material; GO0090382 and the primary papers support progressive membrane traffic and luminal-composition changes. Biological maturation is accepted; the acidification-method attribution is the bounded provenance concern below.

### Eight NONMECHANISTIC topology and maturation edges

graph: supported. Targets: GO:0045335.

All eight edges describe part_of/bounds, phagocytosis forming the compartment, whole-vesicle maturation, early/late subclasses and early-to-phagolysosome maturation. Native definitions/typed relations and source-specific Dictyostelium dynamics support this qualitative scope. No specific Rab recruitment order, fixed cargo census or universal kinetic mechanism is asserted.

### Distinguish measured trafficking from the cited acidification model

evidence: concern. Targets: GO:0045335.

The2002 citation note says the study dissected stages with distinct luminal-acidification behavior. Its Methods/Results directly characterize protein/lipid content and trafficking, whereas Discussionsec20 integrates acidification from prior work and cites Maniak1999/2001. Qualify this source note so it does not imply a direct pH-phase measurement by Gotthardt2002. The general maturation and acidification biology remains supported.

### All maintained claims and intentional boundaries

completeness: supported. Targets: GO:0045335.

The full record, all graph nodes/edges, history and open/resolved discussions were assessed. No individual UniProt accession, mandatory gene cohort, maintained image, exact dimension or quantitative pH is asserted. Optional transient factors and variable cargo do not become compulsory components. Label-only material grounding and historical access notes are not treated as confirmed defects merely because future enrichment is possible.

## Findings

### F1: Distinguish measured trafficking from the cited acidification model

minor / open / confirmed; issue key: phagocytic-vesicle-experimental-attribution.

The2002 citation note says the study dissected stages with distinct luminal-acidification behavior. Its Methods/Results directly characterize protein/lipid content and trafficking, whereas Discussionsec20 integrates acidification from prior work and cites Maniak1999/2001. Qualify this source note so it does not imply a direct pH-phase measurement by Gotthardt2002. The general maturation and acidification biology remains supported.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, Describe Gotthardt2002 as a direct membrane/cargo-trafficking study that discusses acidification based on prior work; if direct pH kinetics are intended, attach an actually inspected direct measurement source.

- The source note/canonical example matches the exact primary assay and preparation.
- Correct ontology identity, topology and supported biological outcomes are retained.
- Native schema, strict, identifier, graph and history gates pass after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/phagocytic_vesicle.yaml; Entire maintained YAML, including history, all source notes, discussions, components and every graph node/edge | context_only | The entire exact target was read; historical curation notes and scientific status remain unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent/EssentialityEnum and graph node/scope contracts | context_only | A label-only lipid material is distinct from whole-membrane GO grounding. Formation necessity differs from localization or mature function. NONMECHANISTIC graphs can represent topology and process outcomes without identifying molecular machinery. |
| context-early_phagosome | data/structures/membrane_organelle/early_phagosome.yaml; Complete frozen local record, read for exact graph identity and boundary context | context_only | The named local structure resolves to its maintained identifier. Neighbor definitions and interpretations are not transferred as independent experimental support; this review judges only the target. |
| context-phagocytic_vesicle_lumen | data/structures/membrane_organelle/phagocytic_vesicle_lumen.yaml; Complete frozen local record, read for exact graph identity and boundary context | context_only | The named local structure resolves to its maintained identifier. Neighbor definitions and interpretations are not transferred as independent experimental support; this review judges only the target. |
| context-phagocytic_vesicle_membrane | data/structures/membrane_organelle/phagocytic_vesicle_membrane.yaml; Complete frozen local record, read for exact graph identity and boundary context | context_only | The named local structure resolves to its maintained identifier. Neighbor definitions and interpretations are not transferred as independent experimental support; this review judges only the target. |
| context-phagolysosome | data/structures/membrane_organelle/phagolysosome.yaml; Complete frozen local record, read for exact graph identity and boundary context | context_only | The named local structure resolves to its maintained identifier. Neighbor definitions and interpretations are not transferred as independent experimental support; this review judges only the target. |
| phagocytic-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032010,GO:0061474,GO:0106174,GO:0005767,GO:0045335,GO:0030670,GO:0097013,GO:0032009,GO:0006909,GO:0090382,GO:0031410,GO:0030659; All12 complete returned terms: id/name/definition/isObsolete/synonyms and typed children; relation direction retained. | supports | The twelve active native entries identify the whole vesicle, membrane, lumen, early and late subclasses, broader classes and phagocytosis/maturation processes. GO0045335 has membrane/lumen part_of children and early-phagosome/phagolysosome is_a children. The maturation definition ends in phagolysosome formation. No unreturned direct parent edge is inferred. |
| phagocytic-agent-go-additional | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0060205,GO:0090383; Complete two active terms and typed children. | supports | GO0090383 defines reduction of phagosome pH. GO0060205 defines the volume inside a cytoplasmic vesicle. This response does not itself supply a direct GO0097013-to-GO0060205 hierarchy edge. |
| phagocytic-agent-SL0206 | https://rest.uniprot.org/locations/SL-0206.json; Complete top-level identity/definition/synonyms/GO map and immediate isA, including nested parent GO cross-reference. | supports | SL0206 maps Phagosome directly to GO0045335, lists phagocytic vesicle synonymy and explicitly has isA cytoplasmic vesicle/GO0031410. It defines an uptake-derived compartment specific to phagocytic cells, without a quantitative species prevalence estimate. |
| phagocytic-agent-SL0205 | https://rest.uniprot.org/locations/SL-0205.json; Complete top-level identity/definition/synonyms/GO map and immediate isA/partOf, with nested parent GO cross-references. | supports | SL0205 maps phagosome membrane to GO0030670, lists both maintained synonyms, has isA cytoplasmic vesicle membrane/GO0030659, and partOf phagosome/GO0045335. Its nested membrane definition describes lipid bilayers without identifying an exact lipid species. |
| phagocytic-agent-SL0342 | https://rest.uniprot.org/locations/SL-0342.json; Complete top-level identity/definition/synonyms and immediate isA/partOf; nested parent GO maps distinguished from a top-level map. | supports | SL0342 identifies phagosome lumen and both maintained synonyms, explicitly isA cytoplasmic vesicle lumen/GO0060205 and partOf phagosome/GO0045335. There is no direct top-level GO map in this response; the matching lumen identity is supported by the definition and synonyms. |
| phagocytic-agent-tax44689 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689; Complete taxId/scientificName/rank/lineage and otherNames. | supports | ENA verifies Dictyostelium discoideum44689 at species rank in Amoebozoa. StrainAx2 and experimental uptake conditions are supplied by the papers, not by this taxonomy response. |
| phagocytic-agent-PMID-12388753 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12388753%20AND%20SRC%3AMED; Exact MED identity/title/authors/year/DOI/PMC129962 and complete primary abstract. | supports | Unique MED12388753 matches Gotthardt et al.2002, DOI10.1091/mbc.e02-04-0206, High-resolution dissection of phagosome maturation reveals distinct membrane trafficking phases. Its complete abstract reports purification, membrane-protein/hydrolase traffic and CatD microscopy, not a direct pH time-course assay. |
| phagocytic-agent-PMID-16926386 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A16926386%20AND%20SRC%3AMED; Exact MED identity/title/authors/year/DOI and complete primary abstract. | supports | Unique MED16926386 matches Gotthardt et al.2006, DOI10.1074/mcp.M600113-MCP200, Proteomics fingerprinting of phagosome maturation and evidence for the role of a Galpha during uptake. The complete abstract identifies time-resolved2D gels/mass spectrometry on Dictyostelium phagosomes and separately tested G-protein uptake phenotypes. |
| phagocytic-agent-gotthardt2002-numeric | https://pmc.ncbi.nlm.nih.gov/articles/129962/; Genuine PMC129962 HTML: complete Methodssec2–11, Resultssec13–19 and Discussionsec20, including embedded Fig1–7 captions. No pixel quantification or supplemental/raw-data analysis. | supports | In Ax2 cultures, latex-bead pulse/chase purification, immunoblots, lipid analysis and microscopy resolve selective delivery/retrieval of phagosomal components. Methodssec3–11 and Resultssec13–19 contain no direct luminal-pH assay. Discussionsec20 integrates these measurements with prior acidification work, explicitly citing Maniak1999/2001 for V-ATPase delivery and acidification. This supports the biological maturation account while requiring a distinction between measured trafficking and discussion-based acidification. |
| phagocytic-agent-gotthardt2006-unige-pdf | https://access.archive-ouverte.unige.ch/access/metadata/eae2ae90-5a91-4330-85a9-04fa245d5d63/download; Genuine university-hosted published PDF; complete main scientific text/Methods/Results/Discussion pp2228–2241 and all main figure captions read from derivative. TableI row pixels and other figure pixels not reread for B37; references/supplements/raw datasets not independently analyzed. | supports | The Ax2 study profiles intact purified phagosomes over six pulse/chase time points using2D gels and mass spectrometry. Methods p2229 and Resultspp2230–2231 distinguish a separate carbonate-stripped membrane-enriched preparation used for preparative protein identification; Figure1B pools later time points, whereas the dynamic whole-phagosome series is Figure2/Resultspp2235–2237. The preparation contains membrane-associated and soluble/cytosolic proteins. Main Figure4C is a maturation schematic, not a new direct pH assay; the authors discuss alternative pathways and timing heterogeneity. |
| schema-result | just validate data/structures/membrane_organelle/phagocytic_vesicle.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/phagocytic_vesicle.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/phagocytic_vesicle.yaml --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagocytic_vesicle-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/phagocytic_vesicle.yaml --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagocytic_vesicle-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagocytic_vesicle-strict.tsv |
| focused-causal | /private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/phagocytic_vesicle.yaml; Complete native read-only graph/protein-scope log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/phagocytic_vesicle.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 12 collected target identifiers returned OK. PMID:12388753: UNREACHABLE; Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity, DOI and declared PMC/null status. This separately resolves citation identity after bulk eutils414; article-body scope is stated independently.; PMID:16926386: UNREACHABLE; Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity, DOI and declared PMC/null status. This separately resolves citation identity after bulk eutils414; article-body scope is stated independently. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Both primary bodies are readable and independently inspected at the stated scope. No new image-pixel quantification, supplemental dataset audit, complete protein census or kinetic reanalysis was performed.
- The2002 acidification scenario and2006 main Figure4C are interpreted with their source tier; no direct pH trace is inferred from a schematic or discussion. Intact-phagosome protein profiling is distinguished from the separate membrane-enrichment preparation.
- Ax2 particle-uptake experiments support the stated model-system example; they do not supply a quantitative prevalence census, every-species maturation timetable or a universal cargo/protein inventory.
- Native SL hierarchy supports the stated broader class where the returned GO response does not show a matching direct edge. No GO relation is fabricated from a nested SL parent.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User explicitly requested a review for every unreviewed target; no issue was manufactured to satisfy the local output gate.
- iModulonDB is not applicable: no gene/regulator expression-module claim is asserted in this target.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T031042Z-phagocytic-vesicle-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of phagocytic vesicle
started_at: '2026-10-22T02:58:48Z'
finished_at: '2026-10-22T03:10:42Z'
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
summary: Exact identity and biological topology/maturation are supported. One minor
  source-attribution qualification is needed; no molecular-grounding, taxon-identity
  or optional-inventory defect was observed.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/early_phagosome.yaml
    sha256: 9b6c5d68e60dd7e28c33d369c72e84353e5415993837864471571dd2d4bb294e
    role: context
  - path: data/structures/membrane_organelle/phagocytic_vesicle.yaml
    sha256: 604f232e3d5457913d2118c27a4e372ba90def9cb369184ce11d3a8f021e335f
    role: target
  - path: data/structures/membrane_organelle/phagocytic_vesicle_lumen.yaml
    sha256: 6f0f574162ac901bb338539914a46653734c7864b4acb89060254f6f34077c19
    role: context
  - path: data/structures/membrane_organelle/phagocytic_vesicle_membrane.yaml
    sha256: 65c456f56f9491c367091e38bf497df4e7f3aa50b21b94d9bf4017ffec2c449f
    role: context
  - path: data/structures/membrane_organelle/phagolysosome.yaml
    sha256: 1aa7bcc22c4b8a9bb65c69fad0c276e2446d28534b72a8abf930ed0e64c70e1e
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
- target_id: GO:0045335
  path: data/structures/membrane_organelle/phagocytic_vesicle.yaml
  label: phagocytic vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagocytic_vesicle.yaml
    role: maintained scientific record
scope:
  description: One complete target. Four frozen neighboring records supply graph identity/boundary
    context only. Native authority entries, actual primary bodies, formation-necessity
    semantics and every source placement were inspected; no neighboring defect is
    silently transferred.
  selection: Batch37 fixed strict path order, index6; one maintained record only.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0045335
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0045335
  command: just validate data/structures/membrane_organelle/phagocytic_vesicle.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0045335
  command: just validate-strict data/structures/membrane_organelle/phagocytic_vesicle.yaml
    --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagocytic_vesicle-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: focused-causal
  name: Native focused causal protein scope
  status: passed
  required: true
  target_ids:
  - GO:0045335
  command: /private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/phagocytic_vesicle.yaml
  exit_code: 0
  summary: No GENE_OR_PROTEIN nodes or dangling protein component references are present.
  evidence_ids:
  - focused-causal
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0045335
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - context-early_phagosome
  - context-phagocytic_vesicle_lumen
  - context-phagocytic_vesicle_membrane
  - context-phagolysosome
  - phagocytic-agent-go
  - phagocytic-agent-go-additional
  - phagocytic-agent-SL0206
  - phagocytic-agent-SL0205
  - phagocytic-agent-SL0342
  - phagocytic-agent-tax44689
  - phagocytic-agent-PMID-12388753
  - phagocytic-agent-PMID-16926386
  - phagocytic-agent-gotthardt2002-numeric
  - phagocytic-agent-gotthardt2006-unige-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0045335
  summary: '10 of 12 collected target identifiers returned OK. PMID:12388753: UNREACHABLE;
    Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity,
    DOI and declared PMC/null status. This separately resolves citation identity after
    bulk eutils414; article-body scope is stated independently.; PMID:16926386: UNREACHABLE;
    Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity,
    DOI and declared PMC/null status. This separately resolves citation identity after
    bulk eutils414; article-body scope is stated independently. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - phagocytic-agent-PMID-12388753
  - phagocytic-agent-PMID-16926386
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0045335
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0045335
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0045335
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0045335
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0045335
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
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/phagocytic_vesicle.yaml
  locator: Entire maintained YAML, including history, all source notes, discussions,
    components and every graph node/edge
  accessed_at: '2026-10-22T03:03:53Z'
  support: context_only
  summary: The entire exact target was read; historical curation notes and scientific
    status remain unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent/EssentialityEnum and graph node/scope contracts
  accessed_at: '2026-10-22T03:03:53Z'
  support: context_only
  summary: A label-only lipid material is distinct from whole-membrane GO grounding.
    Formation necessity differs from localization or mature function. NONMECHANISTIC
    graphs can represent topology and process outcomes without identifying molecular
    machinery.
- evidence_id: context-early_phagosome
  kind: record_content
  reference: data/structures/membrane_organelle/early_phagosome.yaml
  locator: Complete frozen local record, read for exact graph identity and boundary
    context
  accessed_at: '2026-10-22T03:03:53Z'
  support: context_only
  summary: The named local structure resolves to its maintained identifier. Neighbor
    definitions and interpretations are not transferred as independent experimental
    support; this review judges only the target.
- evidence_id: context-phagocytic_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/phagocytic_vesicle_lumen.yaml
  locator: Complete frozen local record, read for exact graph identity and boundary
    context
  accessed_at: '2026-10-22T03:03:53Z'
  support: context_only
  summary: The named local structure resolves to its maintained identifier. Neighbor
    definitions and interpretations are not transferred as independent experimental
    support; this review judges only the target.
- evidence_id: context-phagocytic_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/phagocytic_vesicle_membrane.yaml
  locator: Complete frozen local record, read for exact graph identity and boundary
    context
  accessed_at: '2026-10-22T03:03:53Z'
  support: context_only
  summary: The named local structure resolves to its maintained identifier. Neighbor
    definitions and interpretations are not transferred as independent experimental
    support; this review judges only the target.
- evidence_id: context-phagolysosome
  kind: record_content
  reference: data/structures/membrane_organelle/phagolysosome.yaml
  locator: Complete frozen local record, read for exact graph identity and boundary
    context
  accessed_at: '2026-10-22T03:03:53Z'
  support: context_only
  summary: The named local structure resolves to its maintained identifier. Neighbor
    definitions and interpretations are not transferred as independent experimental
    support; this review judges only the target.
- evidence_id: phagocytic-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032010,GO:0061474,GO:0106174,GO:0005767,GO:0045335,GO:0030670,GO:0097013,GO:0032009,GO:0006909,GO:0090382,GO:0031410,GO:0030659
  locator: 'All12 complete returned terms: id/name/definition/isObsolete/synonyms
    and typed children; relation direction retained.'
  accessed_at: '2026-10-22T02:59:56.802595Z'
  support: supports
  summary: The twelve active native entries identify the whole vesicle, membrane,
    lumen, early and late subclasses, broader classes and phagocytosis/maturation
    processes. GO0045335 has membrane/lumen part_of children and early-phagosome/phagolysosome
    is_a children. The maturation definition ends in phagolysosome formation. No unreturned
    direct parent edge is inferred.
  snapshot_sha256: 6740690b1300ee1c52cf7b22391d2d56e075a2dd3003a46c6436ca1193d350dc
- evidence_id: phagocytic-agent-go-additional
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0060205,GO:0090383
  locator: Complete two active terms and typed children.
  accessed_at: '2026-10-22T03:00:14.617506Z'
  support: supports
  summary: GO0090383 defines reduction of phagosome pH. GO0060205 defines the volume
    inside a cytoplasmic vesicle. This response does not itself supply a direct GO0097013-to-GO0060205
    hierarchy edge.
  snapshot_sha256: 86d382d3145234a0c0fcea4c69f4a4480451223af37d31e1156b2b74bfb7740c
- evidence_id: phagocytic-agent-SL0206
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0206.json
  locator: Complete top-level identity/definition/synonyms/GO map and immediate isA,
    including nested parent GO cross-reference.
  accessed_at: '2026-10-22T02:59:56.810501Z'
  support: supports
  summary: SL0206 maps Phagosome directly to GO0045335, lists phagocytic vesicle synonymy
    and explicitly has isA cytoplasmic vesicle/GO0031410. It defines an uptake-derived
    compartment specific to phagocytic cells, without a quantitative species prevalence
    estimate.
  snapshot_sha256: 2dad97fc89fd4ac3bb8dd8e488d84eaf3a59f68f79c8686828f9d7c2d6b7408e
- evidence_id: phagocytic-agent-SL0205
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0205.json
  locator: Complete top-level identity/definition/synonyms/GO map and immediate isA/partOf,
    with nested parent GO cross-references.
  accessed_at: '2026-10-22T02:59:56.809381Z'
  support: supports
  summary: SL0205 maps phagosome membrane to GO0030670, lists both maintained synonyms,
    has isA cytoplasmic vesicle membrane/GO0030659, and partOf phagosome/GO0045335.
    Its nested membrane definition describes lipid bilayers without identifying an
    exact lipid species.
  snapshot_sha256: 7dbc46aeba8b802034e48acf5e9b1b59bdb39a9047fb204de722d452ba8cc9e6
- evidence_id: phagocytic-agent-SL0342
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0342.json
  locator: Complete top-level identity/definition/synonyms and immediate isA/partOf;
    nested parent GO maps distinguished from a top-level map.
  accessed_at: '2026-10-22T02:59:56.810774Z'
  support: supports
  summary: SL0342 identifies phagosome lumen and both maintained synonyms, explicitly
    isA cytoplasmic vesicle lumen/GO0060205 and partOf phagosome/GO0045335. There
    is no direct top-level GO map in this response; the matching lumen identity is
    supported by the definition and synonyms.
  snapshot_sha256: b241eb5f4701f414d2e4911c8d661922bd28e3523f6082c25a73e56375a18dd8
- evidence_id: phagocytic-agent-tax44689
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689
  locator: Complete taxId/scientificName/rank/lineage and otherNames.
  accessed_at: '2026-10-22T02:59:56.811450Z'
  support: supports
  summary: ENA verifies Dictyostelium discoideum44689 at species rank in Amoebozoa.
    StrainAx2 and experimental uptake conditions are supplied by the papers, not by
    this taxonomy response.
  snapshot_sha256: 6f53a1ddbf831afbc0544e18351c92d099e28c4e8258ef29d0f841829af7c37f
- evidence_id: phagocytic-agent-PMID-12388753
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12388753%20AND%20SRC%3AMED
  locator: Exact MED identity/title/authors/year/DOI/PMC129962 and complete primary
    abstract.
  accessed_at: '2026-10-22T01:10:31.455988Z'
  support: supports
  summary: Unique MED12388753 matches Gotthardt et al.2002, DOI10.1091/mbc.e02-04-0206,
    High-resolution dissection of phagosome maturation reveals distinct membrane trafficking
    phases. Its complete abstract reports purification, membrane-protein/hydrolase
    traffic and CatD microscopy, not a direct pH time-course assay.
  snapshot_sha256: 7ba1845e0950b4eb8287d04190a939a374cb06b9baee8d880bbd3829a813c22c
- evidence_id: phagocytic-agent-PMID-16926386
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A16926386%20AND%20SRC%3AMED
  locator: Exact MED identity/title/authors/year/DOI and complete primary abstract.
  accessed_at: '2026-10-22T01:10:31.456120Z'
  support: supports
  summary: Unique MED16926386 matches Gotthardt et al.2006, DOI10.1074/mcp.M600113-MCP200,
    Proteomics fingerprinting of phagosome maturation and evidence for the role of
    a Galpha during uptake. The complete abstract identifies time-resolved2D gels/mass
    spectrometry on Dictyostelium phagosomes and separately tested G-protein uptake
    phenotypes.
  snapshot_sha256: 434f8f37aafcf032d8142418f47aef2693fd65ceeb4ebae2c5cd5d31e2a00ce6
- evidence_id: phagocytic-agent-gotthardt2002-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/129962/
  locator: 'Genuine PMC129962 HTML: complete Methodssec2–11, Resultssec13–19 and Discussionsec20,
    including embedded Fig1–7 captions. No pixel quantification or supplemental/raw-data
    analysis.'
  accessed_at: '2026-10-22T01:11:10.565148Z'
  support: supports
  summary: In Ax2 cultures, latex-bead pulse/chase purification, immunoblots, lipid
    analysis and microscopy resolve selective delivery/retrieval of phagosomal components.
    Methodssec3–11 and Resultssec13–19 contain no direct luminal-pH assay. Discussionsec20
    integrates these measurements with prior acidification work, explicitly citing
    Maniak1999/2001 for V-ATPase delivery and acidification. This supports the biological
    maturation account while requiring a distinction between measured trafficking
    and discussion-based acidification.
  snapshot_sha256: 5c333f3d4898a3eac26fb3d8571f723db3ae547e0996914b4696718002408777
- evidence_id: phagocytic-agent-gotthardt2006-unige-pdf
  kind: primary_source
  reference: https://access.archive-ouverte.unige.ch/access/metadata/eae2ae90-5a91-4330-85a9-04fa245d5d63/download
  locator: Genuine university-hosted published PDF; complete main scientific text/Methods/Results/Discussion
    pp2228–2241 and all main figure captions read from derivative. TableI row pixels
    and other figure pixels not reread for B37; references/supplements/raw datasets
    not independently analyzed.
  accessed_at: '2026-10-22T01:11:52.952323Z'
  support: supports
  summary: The Ax2 study profiles intact purified phagosomes over six pulse/chase
    time points using2D gels and mass spectrometry. Methods p2229 and Resultspp2230–2231
    distinguish a separate carbonate-stripped membrane-enriched preparation used for
    preparative protein identification; Figure1B pools later time points, whereas
    the dynamic whole-phagosome series is Figure2/Resultspp2235–2237. The preparation
    contains membrane-associated and soluble/cytosolic proteins. Main Figure4C is
    a maturation schematic, not a new direct pH assay; the authors discuss alternative
    pathways and timing heterogeneity.
  snapshot_sha256: 5e34df34378099b87d70b1920b422d2a575515ecd8ad372dcfb4e2a322ee88cd
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/phagocytic_vesicle.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:58:49Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/phagocytic_vesicle.yaml'
  snapshot_sha256: 338a76434dfe352a43762296818571abd24c218da2e26303717cd244a1d8b242
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/phagocytic_vesicle.yaml
    --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagocytic_vesicle-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:58:50Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/phagocytic_vesicle.yaml\
    \ --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagocytic_vesicle-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch37-20261022-offjkz5m/phagocytic_vesicle-strict.tsv"
  snapshot_sha256: 689c847f6caa28e2f8c5e45ce0e49a7284bda1ef99977fec1b5f488ae47a395f
- evidence_id: focused-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/phagocytic_vesicle.yaml
  locator: Complete native read-only graph/protein-scope log
  accessed_at: '2026-10-22T03:02:13.164482Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/phagocytic_vesicle.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 12 collected target identifiers returned OK. PMID:12388753: UNREACHABLE;
    Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity,
    DOI and declared PMC/null status. This separately resolves citation identity after
    bulk eutils414; article-body scope is stated independently.; PMID:16926386: UNREACHABLE;
    Unique native EuropePMC MED result matches exact PMID, Gotthardt article identity,
    DOI and declared PMC/null status. This separately resolves citation identity after
    bulk eutils414; article-body scope is stated independently. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
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
  topic: Exact target identity and topology
  outcome: supported
  target_ids:
  - GO:0045335
  summary: GO0045335 exactly matches the complete definition and phagosome synonym.
    The cytoplasmic-vesicle parent is explicitly supported by SL0206. MembraneGO0030670
    and lumenGO0097013 are typed part_of children of the whole term; all graph classes
    resolve to frozen local records and native authorities. Expanded claims in neighboring
    early/late records are not adopted.
  evidence_ids:
  - record
  - phagocytic-agent-go
  - phagocytic-agent-go-additional
  - phagocytic-agent-SL0206
  - phagocytic-agent-SL0205
  - phagocytic-agent-SL0342
- assessment_id: composition
  area: grounding
  topic: Label-only collective lipid material
  outcome: supported
  target_ids:
  - GO:0045335
  summary: The single LIPID row denotes the lipid material of the bilayer, deliberately
    retaining REVIEWED_LABEL_ONLY and no GO grounding as a chemical identity. Whole
    membraneGO0030670 remains in has_part/graph or record identity, not substituted
    as lipid identity. The collective bilayer is constitutional to this membrane-bounded
    class; no exact molecular composition, stoichiometry or particular lipid requirement
    is asserted.
  evidence_ids:
  - record
  - schema
  - phagocytic-agent-go
  - phagocytic-agent-SL0205
  - phagocytic-agent-SL0206
- assessment_id: necessity
  area: grounding
  topic: Specific molecular formation requirements remain unresolved
  outcome: unknown
  target_ids:
  - GO:0045335
  summary: The ontology and location authority establish a bilayer boundary, not formation-depletion
    tests for individual lipid species or transient proteins. Exact lipid species,
    ratios and their separate necessity remain unknown; this does not invalidate the
    collective boundary requirement.
  evidence_ids:
  - record
  - schema
  - phagocytic-agent-go
  - phagocytic-agent-SL0205
- assessment_id: taxon
  area: scope
  topic: Species and experimental scope
  outcome: supported
  target_ids:
  - GO:0045335
  summary: The qualitative D.discoideum presence statement is supported by the phagocytic
    Ax2 studies and exact species identity. Latex beads are the biochemical model;2002
    compares CatD traffic with ingested yeast. These are not a census of every strain
    or a universal timetable for other protists. The record does not import the neighboring
    Entamoeba/ciliate definitions.
  evidence_ids:
  - record
  - phagocytic-agent-tax44689
  - phagocytic-agent-PMID-12388753
  - phagocytic-agent-gotthardt2002-numeric
  - phagocytic-agent-PMID-16926386
  - phagocytic-agent-gotthardt2006-unige-pdf
- assessment_id: example
  area: provenance
  topic: Intact phagosome proteomics example
  outcome: supported
  target_ids:
  - GO:0045335
  summary: The canonical example accurately specifies purified latex-bead phagosomes,
    a maturation time course,2D electrophoresis and mass spectrometry. The experimental
    organism and source metadata match; no isolated-membrane-only assay is asserted
    in this example.
  evidence_ids:
  - record
  - phagocytic-agent-PMID-16926386
  - phagocytic-agent-gotthardt2006-unige-pdf
- assessment_id: functions
  area: evidence
  topic: Uptake and maturation are supported
  outcome: supported
  target_ids:
  - GO:0045335
  summary: GO0006909/0045335 support enclosure of ingested particulate material; GO0090382
    and the primary papers support progressive membrane traffic and luminal-composition
    changes. Biological maturation is accepted; the acidification-method attribution
    is the bounded provenance concern below.
  evidence_ids:
  - record
  - phagocytic-agent-go
  - phagocytic-agent-go-additional
  - phagocytic-agent-gotthardt2002-numeric
  - phagocytic-agent-gotthardt2006-unige-pdf
- assessment_id: graph
  area: graph
  topic: Eight NONMECHANISTIC topology and maturation edges
  outcome: supported
  target_ids:
  - GO:0045335
  summary: All eight edges describe part_of/bounds, phagocytosis forming the compartment,
    whole-vesicle maturation, early/late subclasses and early-to-phagolysosome maturation.
    Native definitions/typed relations and source-specific Dictyostelium dynamics
    support this qualitative scope. No specific Rab recruitment order, fixed cargo
    census or universal kinetic mechanism is asserted.
  evidence_ids:
  - record
  - schema
  - phagocytic-agent-go
  - phagocytic-agent-SL0205
  - phagocytic-agent-SL0342
  - phagocytic-agent-gotthardt2002-numeric
  - phagocytic-agent-gotthardt2006-unige-pdf
- assessment_id: source-precision
  area: evidence
  topic: Distinguish measured trafficking from the cited acidification model
  outcome: concern
  target_ids:
  - GO:0045335
  summary: The2002 citation note says the study dissected stages with distinct luminal-acidification
    behavior. Its Methods/Results directly characterize protein/lipid content and
    trafficking, whereas Discussionsec20 integrates acidification from prior work
    and cites Maniak1999/2001. Qualify this source note so it does not imply a direct
    pH-phase measurement by Gotthardt2002. The general maturation and acidification
    biology remains supported.
  evidence_ids:
  - record
  - phagocytic-agent-gotthardt2002-numeric
  - phagocytic-agent-PMID-12388753
  - phagocytic-agent-go-additional
- assessment_id: coverage
  area: completeness
  topic: All maintained claims and intentional boundaries
  outcome: supported
  target_ids:
  - GO:0045335
  summary: The full record, all graph nodes/edges, history and open/resolved discussions
    were assessed. No individual UniProt accession, mandatory gene cohort, maintained
    image, exact dimension or quantitative pH is asserted. Optional transient factors
    and variable cargo do not become compulsory components. Label-only material grounding
    and historical access notes are not treated as confirmed defects merely because
    future enrichment is possible.
  evidence_ids:
  - record
  - schema
  - phagocytic-agent-go
  - phagocytic-agent-gotthardt2002-numeric
  - phagocytic-agent-gotthardt2006-unige-pdf
findings:
- finding_id: F1
  issue_key: phagocytic-vesicle-experimental-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish measured trafficking from the cited acidification model
  description: The2002 citation note says the study dissected stages with distinct
    luminal-acidification behavior. Its Methods/Results directly characterize protein/lipid
    content and trafficking, whereas Discussionsec20 integrates acidification from
    prior work and cites Maniak1999/2001. Qualify this source note so it does not
    imply a direct pH-phase measurement by Gotthardt2002. The general maturation and
    acidification biology remains supported.
  target_ids:
  - GO:0045335
  field_paths:
  - functions[1].evidence[1].notes
  evidence_ids:
  - record
  - phagocytic-agent-gotthardt2002-numeric
  - phagocytic-agent-PMID-12388753
  - phagocytic-agent-go-additional
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagocytic_vesicle.yaml
    role: maintained scientific record
  rule_id: Exact source scope and experimental attribution
  native_severity: minor
  normalization_reason: The structure identity and biological maturation/remodeling
    outcome remain supported. The defect is a bounded, nonblocking description of
    what the named experiment directly measured or isolated, rather than a false biological
    mechanism or cross-taxon generalization.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0045335
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagocytic_vesicle.yaml
    role: maintained scientific record
  description: In separately authorized curation, Describe Gotthardt2002 as a direct
    membrane/cargo-trafficking study that discusses acidification based on prior work;
    if direct pH kinetics are intended, attach an actually inspected direct measurement
    source.
  acceptance_checks:
  - The source note/canonical example matches the exact primary assay and preparation.
  - Correct ontology identity, topology and supported biological outcomes are retained.
  - Native schema, strict, identifier, graph and history gates pass after authorized
    curation.
limitations:
- Both primary bodies are readable and independently inspected at the stated scope.
  No new image-pixel quantification, supplemental dataset audit, complete protein
  census or kinetic reanalysis was performed.
- The2002 acidification scenario and2006 main Figure4C are interpreted with their
  source tier; no direct pH trace is inferred from a schematic or discussion. Intact-phagosome
  protein profiling is distinguished from the separate membrane-enrichment preparation.
- Ax2 particle-uptake experiments support the stated model-system example; they do
  not supply a quantitative prevalence census, every-species maturation timetable
  or a universal cargo/protein inventory.
- Native SL hierarchy supports the stated broader class where the returned GO response
  does not show a matching direct edge. No GO relation is fabricated from a nested
  SL parent.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User explicitly requested a review for every unreviewed target; no issue was manufactured
  to satisfy the local output gate.
- 'iModulonDB is not applicable: no gene/regulator expression-module claim is asserted
  in this target.'
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
