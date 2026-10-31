# MCC membrane-domain identity, component and scaffold evidence review

- Review: 20261021T101612Z-eisosome-membrane-domain-mcc-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:59:26Z
- Finished UTC: 2026-10-21T10:16:12Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

MCC identity, hierarchy, Sur7 membership, protein example and the membrane-scaffolding mechanism are supported. One minor citation-placement gap leaves the yeast furrow/filament wording attached only to a localization paper.

## Scope And Provenance

Complete one-record claim-level audit, with exact native identifiers and all maintained assertions assessed against the documented readable source extents.

Selection: Batch eighteen target3; complete exact selected maintained record at frozen main9c0446, reviewed individually.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0090512 | data/structures/envelope/eisosome_membrane_domain_mcc.yaml | maintained | eisosome membrane domain/MCC |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native UniProt example verification | passed | True | GO:0090512 | Focused native check passed; scientific attribution was assessed separately. |
| Focused native causal protein-node audit | passed | True | GO:0090512 | Focused native check passed; scientific attribution was assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0090512 | No transcriptomic or expression-module claim; structural identity, localization and membrane scaffolding require different evidence. |
| Focused native schema | passed | True | GO:0090512 | Focused validator passed. |
| Focused native strict | passed | True | GO:0090512 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0090512 | 10 identifiers OK; 4 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0090512 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0090512 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0090512 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0090512 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0090512 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0090512 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Membrane subdomain versus complete eisosome and adjacent filament

identity: supported. Targets: GO:0090512.

The definition, label, exact MCC synonyms, ENVELOPE/SUBCELLULAR_REGION identity and current GO is-a/parthood agree. The membrane domain is distinct from its external cytoplasmic scaffold. The native filament term uses an S.pombe example, while the primary scaffold experiment here is in S.cerevisiae; neither is silently substituted for the other.

### Sur7 as a demonstrated constituent and marker

evidence: supported. Targets: GO:0090512.

Walther directly measures Sur7 colocalization with Pil1 in W303-derived yeast, Young measures stable Sur7 cortical patches, and the Douglas abstract identifies Sur7 as an integral MCC protein. The role is a membership/localization claim. No component essentiality enum is present; localization, Pil1-deletion effects and sporulation phenotypes are not converted to proof that Sur7 is required for assembly.

### Verified gene, accession and strain boundary

grounding: supported. Targets: GO:0090512.

P54003 is the single reviewed SUR7 entry in tax559292, matching the record. Its role explicitly restricts it to protein identity, and all three copied UniProt localization references are present in the native annotation. The W303 strain background of Walther does not invalidate this separate S288C identity example. Navarre and Huh are verified as native citation/abstract records; their bodies were not independently reanalysed.

### Narrow protein boundary and broader family candidate

grounding: supported. Targets: GO:0090512.

The one inspected candidate IPR009571/PF06687 spans Sur7/Rim9/PalI and does not by itself identify the demonstrated Sur7 MCC constituent. The existing REVIEWED_LABEL_ONLY status and bounded family-resolution TODO remain defensible. This is not an exhaustive claim that no narrower family identifier exists.

### Qualitative fungal scope and exact placement of the yeast architecture source

scope: concern. Targets: GO:0090512.

The review abstract supports a varied fungal MCC/eisosome class, and direct W303 yeast data support the canonical S.cerevisiae model. COMMON is qualitative rather than a measured population frequency. The S.cerevisiae distribution note combines directly supported Sur7 localization with furrow/filament architecture, but cites only Walther; the latter architectural clause should instead cite the available Karotki results or Douglas review.

### Stable membrane compartmentation

evidence: supported. Targets: GO:0090512.

The function is supported by stable Sur7/Pil1 patches, review-level MCC compartment organization, and Karotki membrane-scaffolding experiments. It does not repeat Walther historical endocytosis-site interpretation as an established MCC function or infer universal fungal rates/dimensions.

### Localization plus experimentally supported scaffold mechanism

graph: supported. Targets: GO:0090512.

The Sur7 localizes-to edge is supported by direct colocalization. The filament scaffolds-MCC edge is supported by reconstitution, membrane tubulation, perturbations and in-cell immunolabeled lattice observations; ASSEMBLY/MECHANISTIC is appropriate for this bounded structural scaffold model. This does not assert exact contacts, obligatory temporal ordering, universal Pil1/Lsp1 pairing across Fungi, or Sur7 assembly necessity.

### Primary bodies, review abstract and historical access annotations

provenance: supported. Targets: GO:0090512.

Walther main/Methods, Karotki named JATS sections and Young named PMC passages were read as direct primary evidence. Douglas is review-abstract evidence only after two publisher403 responses; the historical PMID rerouting note remains historical. Exact native citations resolve all four PMID transport residuals independently. The issue is a local architecture-source placement gap, not inaccessible historical evidence or a changed DOI identity.

### Bounded component inventory and absent optional measurements

completeness: supported. Targets: GO:0090512.

The record explicitly limits its constituent to demonstrated Sur7 and retains a TODO for other residents. It has no image or quantitative measurement assertion requiring inspection. No empty optional slot, untested Sur7 assembly necessity or historical access annotation is promoted to a finding.

## Findings

### F1: Cite the source that resolves MCC furrow and filament architecture

minor / open / confirmed; issue key: mcc-yeast-furrow-architecture-source-placement.

The S.cerevisiae distribution note describes Sur7-marked furrow-like MCC domains paired with filaments but cites only Walther2006. That primary body establishes Sur7/Pil1 localization and immobile patches; its EM images described in the body concern abnormal pil1-deletion invaginations rather than normal furrow-and-filament architecture. Karotki2011 Results sec11/Fig7 directly support the fuller architecture and are already cited elsewhere in the record. The biological assertion is supported, but its nearest source is incomplete.

## Recommended Actions And Acceptance Checks

### A1

Replace the distribution-row reference with Karotki2011 or Douglas2014 for its full furrow-and-filament wording, or narrow that note to the Sur7/eisosome localization established by Walther2006. Preserve the species scope and separate S288C identity-only protein example.

- The nearest citation must support every retained anatomical clause; verify Karotki Results sec11/Fig7 or the exact Douglas abstract.
- Retain W303 experimental context without treating it as an S288C-specific localization assay.
- Any later maintained edit requires separate authorization, the guarded curation writer, history and focused schema/strict validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/envelope/eisosome_membrane_domain_mcc.yaml; Entire YAML, including all evidence notes, history, distributions, component, function, graph and discussion | context_only | The target denotes the MCC membrane subdomain, with one demonstrated Sur7 constituent and an external filament scaffold. It does not claim a complete resident inventory or Sur7 assembly essentiality. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Mechanistic scope, external structural actors and edge-level evidence | context_only | A directed scaffolding mechanism can be supported by perturbation, reconstitution and structural results; protein localization alone is assessed separately. |
| review-policy | .claude/skills/review-yaml-record/SKILL.md; Evidence Rules and Workflow steps5–6 | context_only | Material assertions must be supported at their nearest source. A non-blocking citation placement gap is minor; no optional inventory or unknown necessity finding is imposed. |
| eisosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0090512,GO:0044853,GO:0032126,GO:0036286; All four results: id/name/definition/aspect/isObsolete; exact children.relation fields on GO0044853 and GO0032126 | supports | All four native terms are active cellular components. GO0090512 exactly matches the MCC definition; GO0044853 lists MCC as an is_a child, and GO0032126 lists MCC and GO0036286 as part_of children. The filament definition describes the S.pombe Pil1 example, while the whole-eisosome definition distinguishes membrane domain and cytoplasmic scaffolding lattice. |
| eisosome-agent-P54003 | https://rest.uniprot.org/uniprotkb/P54003.json; primaryAccession, entryType, proteinDescription, genes, organism, proteinExistence, SUBCELLULAR LOCATION evidence arrays, SIMILARITY and InterPro/Pfam cross-references | supports | Reviewed P54003 is Protein SUR7, gene SUR7/YML052W, in tax559292 S288c. The Cell membrane/multipass annotation contains experimental PubMed attributions11784867,12469340,14562095 as copied by the target, plus two others. The entry identifies this protein and annotation provenance; its historical endocytosis note is not adopted as a new mechanism. |
| eisosome-agent-query-sur7 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ASUR7&amp;format=json&amp;size=500; results array: exactly one primaryAccession P54003; query fields in reference URL | supports | The exact reviewed SUR7 query for organism559292 returns one result, P54003. This is an identity-selection result, not an MCC localization assay. |
| eisosome-agent-family-IPR009571 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009571/; metadata accession/type/name/member_databases, complete description paragraphs and hierarchy | supports | IPR009571 is the fungal SUR7/Rim9-like family and integrates PF06687 SUR7/PalI. Its own description includes Sur7, Rim9 and PalI; it is broader than a Sur7-only protein identity or a demonstrated MCC-membership class. |
| eisosome-agent-taxon-4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; taxId, scientificName, rank, lineage and otherNames | supports | Native taxonomy identifies Fungi at kingdom rank. This source establishes identity and lineage only, not the frequency or occurrence of MCC domains. |
| eisosome-agent-taxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank, lineage and otherNames | supports | Native taxonomy identifies Saccharomyces cerevisiae at species rank. This source establishes identity and lineage only, not the frequency or occurrence of MCC domains. |
| eisosome-agent-taxon-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId, scientificName, rank, lineage and otherNames | supports | Native taxonomy identifies Saccharomyces cerevisiae S288C at strain rank. This source establishes identity and lineage only, not the frequency or occurrence of MCC domains. |
| eisosome-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28EXT_ID%3A25002088+OR+EXT_ID%3A11784867+OR+EXT_ID%3A12469340+OR+EXT_ID%3A14562095+OR+DOI%3A10.1038%2Fnature04472+OR+DOI%3A10.1083%2Fjcb.201104040%29+AND+SRC%3AMED&amp;format=json&amp;resultType=core; resultList.result: six records keyed by id; title, authorString, doi, pubYear, publication types and abstractText | supports | Exact native records verify titles, authors and identifiers for Walther2006 PMID16496001 DOI10.1038/nature04472; Karotki2011 PMID22123866 DOI10.1083/jcb.201104040; Douglas/Konopka2014 PMID25002088; Young2002 PMID11784867; Navarre2002 PMID12469340; and Huh2003 PMID14562095. The latter three match the target UniProt annotation citations. |
| douglas-review-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28EXT_ID%3A25002088+OR+EXT_ID%3A11784867+OR+EXT_ID%3A12469340+OR+EXT_ID%3A14562095+OR+DOI%3A10.1038%2Fnature04472+OR+DOI%3A10.1083%2Fjcb.201104040%29+AND+SRC%3AMED&amp;format=json&amp;resultType=core; resultList.result[id=25002088].abstractText only; full review body not recovered | supports | The Douglas/Konopka review abstract defines MCC as stable punctate membrane furrows containing Sur7 and Nce102, distinguishes the peripheral Pil1/Lsp1 filament portion, and describes comparison across diverse fungi. It supports the qualitative domain distinction and fungal scope at review-abstract level. |
| eisosome-agent-go-definition-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22368779+AND+SRC%3AMED&amp;format=json&amp;resultType=core; resultList.result[id=22368779], complete citation and abstractText; source cited by native GO0090512 definition | supports | Native PMID22368779 metadata identifies the review Membrane Compartment Occupied by Can1 (MCC) and Eisosome Subdomains of the Fungal Plasma Membrane. Its abstract distinguishes integral MCC proteins from adjacent peripheral eisosome proteins and describes stable furrows. It also uses a narrower lipid-raft distinction; the target parent is assessed as the current GO relation, not as an independently tested raft-biophysics claim. |
| eisosome-agent-walther2006-publisher | https://www.nature.com/articles/nature04472; Full publisher article Main paragraphs7–32, Methods paragraphs33–36 and captions in //article//p (zero-based derived paragraph index); especially9,11,15–16,22,33; Figs1–2 captions. Main and Methods read; figure pixels and supplementary files not independently inspected. | supports | Direct primary body shows Sur7-GFP colocalization with Pil1-HA and immobile plasma-membrane patches. Pil1 deletion redistributes Sur7/Lsp1 and produces abnormal invaginations; the EM observation is of mutant defects, not resolved normal MCC furrows or a filament lattice. All yeast strains are W303-derived. The source supports the target localization and species example, with the architectural citation limit recorded separately. |
| eisosome-agent-karotki | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3257569/fullTextXML; JATS PMC3257569 abstract; Results sec3,sec5–9,sec11; Discussion sec12; Methods sec14–15,17,19–21,25; captions Figs1–8. Claim-bearing text and captions read; no figure-pixel reanalysis. | supports | Direct primary results show purified Pil1/Lsp1 self-assembly, membrane binding/tubulation, and membrane-bound coats. DEEM with immunolabeling identifies Pil1/Lsp1 lattice on the cytoplasmic face of membrane furrows. The paper supports a scaffold mechanism, while exact subunit contacts, mixed assemblies in cells and whether wedge insertion also contributes remain model-level questions. In-vitro closed tubes and in-cell half-cylinder furrows are explicitly distinguished. |
| eisosome-agent-young2002-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC133540/; Genuine PMC133540 article HTML: Abstract; Introduction; Materials and Methods strain construction; Results Sur7-family localization and patch characterization; Discussion first two paragraphs. Derived //section//p indices5–10,22–28,33,35,54–55 read; no image-pixel or complete supplemental audit. | supports | Direct primary results localize Sur7-GFP and Sur7-9myc to stable cortical patches in the stated YJC strains; the discussion interprets these as novel plasma-membrane domains. This supports the narrow membrane-localization attribution. The paper does not establish an S288C-specific replication of the later W303 experiments or MCC-furrow architecture. |
| douglas2014-publisher-access | https://www.annualreviews.org/content/journals/10.1146/annurev-micro-091313-103507; Actual response bytes and original fetch metadata | context_only | HTTP403 HTML challenge; no readable review body. Access limitation only; it is not negative scientific evidence. |
| douglas2014-pdf-access | https://www.annualreviews.org/doi/pdf/10.1146/annurev-micro-091313-103507; Actual response bytes and original fetch metadata | context_only | HTTP403 HTML; no readable PDF. Access limitation only; it is not negative scientific evidence. |
| young2002-jats-access | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC133540/fullTextXML; Actual response bytes and original fetch metadata | context_only | HTTP500 response; this Europe PMC route failed although separately hashed genuine PMC HTML succeeded. Access limitation only; it is not negative scientific evidence. |
| walther2006-pdf-access | https://cienciavida.org/wp-content/uploads/2012/08/SB_09_2006-Nature.pdf; Actual response bytes and original fetch metadata | context_only | HTTP404 response; this alternate PDF route failed although separately hashed genuine Nature HTML succeeded. Access limitation only; it is not negative scientific evidence. |
| native-verify | /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/eisosome_membrane_domain_mcc.yaml --verify; Captured focused native log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/eisosome_membrane_domain_mcc.yaml --causal-graphs; Captured focused native log | supports | data/structures/envelope/eisosome_membrane_domain_mcc.yaml  (GO:0090512)<br>  eisosome_filament_scaffolds_mcc	sur7_membrane_protein	COVERED	-&gt;sur7_membrane_protein (UniProtKB:P54003)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/envelope/eisosome_membrane_domain_mcc.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/envelope/eisosome_membrane_domain_mcc.yaml |
| strict-result | just validate-strict data/structures/envelope/eisosome_membrane_domain_mcc.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/eisosome_membrane_domain_mcc-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/envelope/eisosome_membrane_domain_mcc.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/eisosome_membrane_domain_mcc-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/eisosome_membrane_domain_mcc-strict.tsv |
| target-curies | just check-curies-strict; data/structures/envelope/eisosome_membrane_domain_mcc.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 10 of14 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:11784867: UNREACHABLE; resolved by evidence eisosome-agent-epmc; PMID:12469340: UNREACHABLE; resolved by evidence eisosome-agent-epmc; PMID:14562095: UNREACHABLE; resolved by evidence eisosome-agent-epmc; PMID:25002088: UNREACHABLE; resolved by evidence eisosome-agent-epmc. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Douglas/Konopka2014 full body was not recovered: native publisher and PDF routes returned403. Only its exact native abstract supports qualitative fungal/domain statements.
- Navarre2002 and Huh2003 are verified at native metadata/abstract and UniProt annotation-attribution level; their primary bodies were not independently inspected. Young2002 genuine PMC body was read at the named localization and methods passages.
- Karotki2011 text and captions support a structural scaffold model; image pixels and supplementary files were not reanalysed. Exact subunit contacts, mixed Pil1/Lsp1 assemblies and additional membrane-bending mechanisms remain unresolved in that source.
- Walther2006 experiments use W303-derived strains. The record protein example is an explicitly identity-only S288C accession, not a claim of an identical experiment in that strain.
- Current GO parentage is verified as ontology hierarchy; the review terminology distinguishing MCC from lipid rafts is not treated as an independent experimental validation of raft biophysical properties.
- No exhaustive fungal occurrence survey, complete MCC resident inventory or all-family search was performed; no assembly necessity claim is added for Sur7.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Reused Karotki and three taxonomy raw/meta snapshots retain original batch6 UTC timestamps and byte hashes; scientific sources were read again for this target.
- All graph identifiers are external ontology terms or the local Sur7 component_ref; no neighboring maintained record was used as scientific evidence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101612Z-eisosome-membrane-domain-mcc-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: MCC membrane-domain identity, component and scaffold evidence review
started_at: '2026-10-21T09:59:26Z'
finished_at: '2026-10-21T10:16:12Z'
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
summary: MCC identity, hierarchy, Sur7 membership, protein example and the membrane-scaffolding
  mechanism are supported. One minor citation-placement gap leaves the yeast furrow/filament
  wording attached only to a localization paper.
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
  - path: data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    sha256: cf0490c93ccba7b66f5f9fc3f6e108981620ba71eb7635fb3c7582dd7dfb1a1f
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
- target_id: GO:0090512
  path: data/structures/envelope/eisosome_membrane_domain_mcc.yaml
  label: eisosome membrane domain/MCC
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    role: maintained scientific record
scope:
  description: Complete one-record claim-level audit, with exact native identifiers
    and all maintained assertions assessed against the documented readable source
    extents.
  selection: Batch eighteen target3; complete exact selected maintained record at
    frozen main9c0446, reviewed individually.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0090512
checks:
- check_id: native-verify
  name: Focused native UniProt example verification
  status: passed
  required: true
  target_ids:
  - GO:0090512
  command: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; scientific attribution was assessed separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal protein-node audit
  status: passed
  required: true
  target_ids:
  - GO:0090512
  command: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; scientific attribution was assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0090512
  summary: No transcriptomic or expression-module claim; structural identity, localization
    and membrane scaffolding require different evidence.
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0090512
  command: just validate data/structures/envelope/eisosome_membrane_domain_mcc.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0090512
  command: just validate-strict data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/eisosome_membrane_domain_mcc-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0090512
  summary: 10 identifiers OK; 4 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - eisosome-agent-epmc
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0090512
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - graph-policy
  - review-policy
  - eisosome-agent-go
  - eisosome-agent-P54003
  - eisosome-agent-query-sur7
  - eisosome-agent-family-IPR009571
  - eisosome-agent-taxon-4751
  - eisosome-agent-taxon-4932
  - eisosome-agent-taxon-559292
  - eisosome-agent-epmc
  - douglas-review-abstract
  - eisosome-agent-go-definition-meta
  - eisosome-agent-walther2006-publisher
  - eisosome-agent-karotki
  - eisosome-agent-young2002-legacy
  - douglas2014-publisher-access
  - douglas2014-pdf-access
  - young2002-jats-access
  - walther2006-pdf-access
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0090512
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
  - GO:0090512
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
  - GO:0090512
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
  - GO:0090512
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
  - GO:0090512
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
  reference: data/structures/envelope/eisosome_membrane_domain_mcc.yaml
  locator: Entire YAML, including all evidence notes, history, distributions, component,
    function, graph and discussion
  accessed_at: '2026-10-21T10:06:39Z'
  support: context_only
  summary: The target denotes the MCC membrane subdomain, with one demonstrated Sur7
    constituent and an external filament scaffold. It does not claim a complete resident
    inventory or Sur7 assembly essentiality.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Mechanistic scope, external structural actors and edge-level evidence
  accessed_at: '2026-10-21T10:06:39Z'
  support: context_only
  summary: A directed scaffolding mechanism can be supported by perturbation, reconstitution
    and structural results; protein localization alone is assessed separately.
- evidence_id: review-policy
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules and Workflow steps5–6
  accessed_at: '2026-10-21T10:06:39Z'
  support: context_only
  summary: Material assertions must be supported at their nearest source. A non-blocking
    citation placement gap is minor; no optional inventory or unknown necessity finding
    is imposed.
- evidence_id: eisosome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0090512,GO:0044853,GO:0032126,GO:0036286
  locator: 'All four results: id/name/definition/aspect/isObsolete; exact children.relation
    fields on GO0044853 and GO0032126'
  accessed_at: '2026-10-21T10:00:34.698206Z'
  support: supports
  summary: All four native terms are active cellular components. GO0090512 exactly
    matches the MCC definition; GO0044853 lists MCC as an is_a child, and GO0032126
    lists MCC and GO0036286 as part_of children. The filament definition describes
    the S.pombe Pil1 example, while the whole-eisosome definition distinguishes membrane
    domain and cytoplasmic scaffolding lattice.
  snapshot_sha256: a09940bf93bbf39f2e4230b6a1525ed286fe477f72c6e42c669cb436cd3d8f57
- evidence_id: eisosome-agent-P54003
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P54003.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, proteinExistence,
    SUBCELLULAR LOCATION evidence arrays, SIMILARITY and InterPro/Pfam cross-references
  accessed_at: '2026-10-21T10:00:34.699416Z'
  support: supports
  summary: Reviewed P54003 is Protein SUR7, gene SUR7/YML052W, in tax559292 S288c.
    The Cell membrane/multipass annotation contains experimental PubMed attributions11784867,12469340,14562095
    as copied by the target, plus two others. The entry identifies this protein and
    annotation provenance; its historical endocytosis note is not adopted as a new
    mechanism.
  snapshot_sha256: 9f26f2c5a9984a2a9a67dd5fe8478290ec8522abbc75595d2829145fa791b25d
- evidence_id: eisosome-agent-query-sur7
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ASUR7&format=json&size=500
  locator: 'results array: exactly one primaryAccession P54003; query fields in reference
    URL'
  accessed_at: '2026-10-21T10:00:34.699840Z'
  support: supports
  summary: The exact reviewed SUR7 query for organism559292 returns one result, P54003.
    This is an identity-selection result, not an MCC localization assay.
  snapshot_sha256: 4c29ffd344834d92aed34a0900a95b054e4b46ae7d25df3866413488437ae518
  search_scope: Native UniProtKB query reviewed:true AND organism_id:559292 AND gene_exact:SUR7,
    JSON size500; one result, no pagination needed. No unreviewed or alternate-species
    candidates were inferred.
- evidence_id: eisosome-agent-family-IPR009571
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009571/
  locator: metadata accession/type/name/member_databases, complete description paragraphs
    and hierarchy
  accessed_at: '2026-10-21T10:01:29.740199Z'
  support: supports
  summary: IPR009571 is the fungal SUR7/Rim9-like family and integrates PF06687 SUR7/PalI.
    Its own description includes Sur7, Rim9 and PalI; it is broader than a Sur7-only
    protein identity or a demonstrated MCC-membership class.
  snapshot_sha256: c74c73d3bc87f92f276f050b86fd528fb0fab53e131f1afa34bc2ad80c075262
- evidence_id: eisosome-agent-taxon-4751
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-21T06:58:39.228942Z'
  support: supports
  summary: Native taxonomy identifies Fungi at kingdom rank. This source establishes
    identity and lineage only, not the frequency or occurrence of MCC domains.
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: eisosome-agent-taxon-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-21T06:58:39.225484Z'
  support: supports
  summary: Native taxonomy identifies Saccharomyces cerevisiae at species rank. This
    source establishes identity and lineage only, not the frequency or occurrence
    of MCC domains.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: eisosome-agent-taxon-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-21T06:58:39.217412Z'
  support: supports
  summary: Native taxonomy identifies Saccharomyces cerevisiae S288C at strain rank.
    This source establishes identity and lineage only, not the frequency or occurrence
    of MCC domains.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: eisosome-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28EXT_ID%3A25002088+OR+EXT_ID%3A11784867+OR+EXT_ID%3A12469340+OR+EXT_ID%3A14562095+OR+DOI%3A10.1038%2Fnature04472+OR+DOI%3A10.1083%2Fjcb.201104040%29+AND+SRC%3AMED&format=json&resultType=core
  locator: 'resultList.result: six records keyed by id; title, authorString, doi,
    pubYear, publication types and abstractText'
  accessed_at: '2026-10-21T10:00:34.700220Z'
  support: supports
  summary: Exact native records verify titles, authors and identifiers for Walther2006
    PMID16496001 DOI10.1038/nature04472; Karotki2011 PMID22123866 DOI10.1083/jcb.201104040;
    Douglas/Konopka2014 PMID25002088; Young2002 PMID11784867; Navarre2002 PMID12469340;
    and Huh2003 PMID14562095. The latter three match the target UniProt annotation
    citations.
  snapshot_sha256: 70208706447c086c7912051ed417fe8633c7289706ea80cba34de82f289692d9
- evidence_id: douglas-review-abstract
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28EXT_ID%3A25002088+OR+EXT_ID%3A11784867+OR+EXT_ID%3A12469340+OR+EXT_ID%3A14562095+OR+DOI%3A10.1038%2Fnature04472+OR+DOI%3A10.1083%2Fjcb.201104040%29+AND+SRC%3AMED&format=json&resultType=core
  locator: resultList.result[id=25002088].abstractText only; full review body not
    recovered
  accessed_at: '2026-10-21T10:00:34.700220Z'
  support: supports
  summary: The Douglas/Konopka review abstract defines MCC as stable punctate membrane
    furrows containing Sur7 and Nce102, distinguishes the peripheral Pil1/Lsp1 filament
    portion, and describes comparison across diverse fungi. It supports the qualitative
    domain distinction and fungal scope at review-abstract level.
  snapshot_sha256: 70208706447c086c7912051ed417fe8633c7289706ea80cba34de82f289692d9
- evidence_id: eisosome-agent-go-definition-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22368779+AND+SRC%3AMED&format=json&resultType=core
  locator: resultList.result[id=22368779], complete citation and abstractText; source
    cited by native GO0090512 definition
  accessed_at: '2026-10-21T10:01:29.742138Z'
  support: supports
  summary: Native PMID22368779 metadata identifies the review Membrane Compartment
    Occupied by Can1 (MCC) and Eisosome Subdomains of the Fungal Plasma Membrane.
    Its abstract distinguishes integral MCC proteins from adjacent peripheral eisosome
    proteins and describes stable furrows. It also uses a narrower lipid-raft distinction;
    the target parent is assessed as the current GO relation, not as an independently
    tested raft-biophysics claim.
  snapshot_sha256: 2558b00320d1e0ee2a597768454315a7ace653349ca54b100a3676360bdbe9f6
- evidence_id: eisosome-agent-walther2006-publisher
  kind: primary_source
  reference: https://www.nature.com/articles/nature04472
  locator: Full publisher article Main paragraphs7–32, Methods paragraphs33–36 and
    captions in //article//p (zero-based derived paragraph index); especially9,11,15–16,22,33;
    Figs1–2 captions. Main and Methods read; figure pixels and supplementary files
    not independently inspected.
  accessed_at: '2026-10-21T10:00:34.700930Z'
  support: supports
  summary: Direct primary body shows Sur7-GFP colocalization with Pil1-HA and immobile
    plasma-membrane patches. Pil1 deletion redistributes Sur7/Lsp1 and produces abnormal
    invaginations; the EM observation is of mutant defects, not resolved normal MCC
    furrows or a filament lattice. All yeast strains are W303-derived. The source
    supports the target localization and species example, with the architectural citation
    limit recorded separately.
  snapshot_sha256: 145bf600ec6c6dfd955824ec5ffd58f42700bff6ae47b0f2120d69db6cd2993e
- evidence_id: eisosome-agent-karotki
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3257569/fullTextXML
  locator: JATS PMC3257569 abstract; Results sec3,sec5–9,sec11; Discussion sec12;
    Methods sec14–15,17,19–21,25; captions Figs1–8. Claim-bearing text and captions
    read; no figure-pixel reanalysis.
  accessed_at: '2026-10-21T06:56:07.011936Z'
  support: supports
  summary: Direct primary results show purified Pil1/Lsp1 self-assembly, membrane
    binding/tubulation, and membrane-bound coats. DEEM with immunolabeling identifies
    Pil1/Lsp1 lattice on the cytoplasmic face of membrane furrows. The paper supports
    a scaffold mechanism, while exact subunit contacts, mixed assemblies in cells
    and whether wedge insertion also contributes remain model-level questions. In-vitro
    closed tubes and in-cell half-cylinder furrows are explicitly distinguished.
  snapshot_sha256: 403bb366f2d751bb16d953995b5800338820e4ee1a7f0c79b0c7f1b2d5a67152
- evidence_id: eisosome-agent-young2002-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC133540/
  locator: 'Genuine PMC133540 article HTML: Abstract; Introduction; Materials and
    Methods strain construction; Results Sur7-family localization and patch characterization;
    Discussion first two paragraphs. Derived //section//p indices5–10,22–28,33,35,54–55
    read; no image-pixel or complete supplemental audit.'
  accessed_at: '2026-10-21T10:04:42.917101Z'
  support: supports
  summary: Direct primary results localize Sur7-GFP and Sur7-9myc to stable cortical
    patches in the stated YJC strains; the discussion interprets these as novel plasma-membrane
    domains. This supports the narrow membrane-localization attribution. The paper
    does not establish an S288C-specific replication of the later W303 experiments
    or MCC-furrow architecture.
  snapshot_sha256: c224462ee527505040a8d636f2ae9e15e172bf51f9c96de0d760a034fe8b8686
- evidence_id: douglas2014-publisher-access
  kind: authority
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev-micro-091313-103507
  locator: Actual response bytes and original fetch metadata
  accessed_at: '2026-10-21T10:00:34.701299Z'
  support: context_only
  summary: HTTP403 HTML challenge; no readable review body. Access limitation only;
    it is not negative scientific evidence.
  snapshot_sha256: b1f4711f6f03e0c79150315105c200a454323178003dcc32b35f9bb6d4e03e1d
- evidence_id: douglas2014-pdf-access
  kind: authority
  reference: https://www.annualreviews.org/doi/pdf/10.1146/annurev-micro-091313-103507
  locator: Actual response bytes and original fetch metadata
  accessed_at: '2026-10-21T10:01:29.741344Z'
  support: context_only
  summary: HTTP403 HTML; no readable PDF. Access limitation only; it is not negative
    scientific evidence.
  snapshot_sha256: e94aa7d0fa76107936007effb3e0160e6c98ae0c915e5d2fb9ec9140842720d5
- evidence_id: young2002-jats-access
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC133540/fullTextXML
  locator: Actual response bytes and original fetch metadata
  accessed_at: '2026-10-21T10:01:29.740590Z'
  support: context_only
  summary: HTTP500 response; this Europe PMC route failed although separately hashed
    genuine PMC HTML succeeded. Access limitation only; it is not negative scientific
    evidence.
  snapshot_sha256: 285ac7c0b27b3d7b4cb4bc45c3ac7b7756fffe0f24a3049a74be0c6cbf450b58
- evidence_id: walther2006-pdf-access
  kind: authority
  reference: https://cienciavida.org/wp-content/uploads/2012/08/SB_09_2006-Nature.pdf
  locator: Actual response bytes and original fetch metadata
  accessed_at: '2026-10-21T10:01:29.741800Z'
  support: context_only
  summary: HTTP404 response; this alternate PDF route failed although separately hashed
    genuine Nature HTML succeeded. Access limitation only; it is not negative scientific
    evidence.
  snapshot_sha256: 4a5bbe01fc7064454189f13cdcb3f66e6b4ae57d576d7f856163be6a65ea8d80
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    --verify
  locator: Captured focused native log
  accessed_at: '2026-10-21T10:01:40.389359Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    --causal-graphs
  locator: Captured focused native log
  accessed_at: '2026-10-21T10:01:41.067438Z'
  support: supports
  summary: "data/structures/envelope/eisosome_membrane_domain_mcc.yaml  (GO:0090512)\n\
    \  eisosome_filament_scaffolds_mcc\tsur7_membrane_protein\tCOVERED\t->sur7_membrane_protein\
    \ (UniProtKB:P54003)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED\
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
  snapshot_sha256: 4555ff404e119b494724458ee3afd7d2de0bc52b8408c177a14a789823dc00d8
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/envelope/eisosome_membrane_domain_mcc.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:29Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/envelope/eisosome_membrane_domain_mcc.yaml'
  snapshot_sha256: 0ea4f9e02f5cb2972d18ff351a4f37b01f92024b4a22b89311f382678edeb104
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/eisosome_membrane_domain_mcc-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:31Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/envelope/eisosome_membrane_domain_mcc.yaml\
    \ --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/eisosome_membrane_domain_mcc-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/eisosome_membrane_domain_mcc-strict.tsv"
  snapshot_sha256: fdc5b3ac0463a41c979e1baba22c95cbefcb90cf890330fb127e297fcac4fa44
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/envelope/eisosome_membrane_domain_mcc.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:06:39Z'
  support: supports
  summary: '10 of14 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:11784867: UNREACHABLE; resolved by evidence eisosome-agent-epmc;
    PMID:12469340: UNREACHABLE; resolved by evidence eisosome-agent-epmc; PMID:14562095:
    UNREACHABLE; resolved by evidence eisosome-agent-epmc; PMID:25002088: UNREACHABLE;
    resolved by evidence eisosome-agent-epmc. Source-native identity checked separately.'
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
  topic: Membrane subdomain versus complete eisosome and adjacent filament
  outcome: supported
  target_ids:
  - GO:0090512
  summary: The definition, label, exact MCC synonyms, ENVELOPE/SUBCELLULAR_REGION
    identity and current GO is-a/parthood agree. The membrane domain is distinct from
    its external cytoplasmic scaffold. The native filament term uses an S.pombe example,
    while the primary scaffold experiment here is in S.cerevisiae; neither is silently
    substituted for the other.
  evidence_ids:
  - eisosome-agent-go
  - douglas-review-abstract
  - eisosome-agent-karotki
  - record
- assessment_id: composition
  area: evidence
  topic: Sur7 as a demonstrated constituent and marker
  outcome: supported
  target_ids:
  - GO:0090512
  summary: Walther directly measures Sur7 colocalization with Pil1 in W303-derived
    yeast, Young measures stable Sur7 cortical patches, and the Douglas abstract identifies
    Sur7 as an integral MCC protein. The role is a membership/localization claim.
    No component essentiality enum is present; localization, Pil1-deletion effects
    and sporulation phenotypes are not converted to proof that Sur7 is required for
    assembly.
  evidence_ids:
  - eisosome-agent-walther2006-publisher
  - eisosome-agent-young2002-legacy
  - douglas-review-abstract
  - record
- assessment_id: protein-example
  area: grounding
  topic: Verified gene, accession and strain boundary
  outcome: supported
  target_ids:
  - GO:0090512
  summary: P54003 is the single reviewed SUR7 entry in tax559292, matching the record.
    Its role explicitly restricts it to protein identity, and all three copied UniProt
    localization references are present in the native annotation. The W303 strain
    background of Walther does not invalidate this separate S288C identity example.
    Navarre and Huh are verified as native citation/abstract records; their bodies
    were not independently reanalysed.
  evidence_ids:
  - eisosome-agent-P54003
  - eisosome-agent-query-sur7
  - eisosome-agent-epmc
  - eisosome-agent-walther2006-publisher
  - eisosome-agent-taxon-4751
  - eisosome-agent-taxon-4932
  - eisosome-agent-taxon-559292
  - record
- assessment_id: family
  area: grounding
  topic: Narrow protein boundary and broader family candidate
  outcome: supported
  target_ids:
  - GO:0090512
  summary: The one inspected candidate IPR009571/PF06687 spans Sur7/Rim9/PalI and
    does not by itself identify the demonstrated Sur7 MCC constituent. The existing
    REVIEWED_LABEL_ONLY status and bounded family-resolution TODO remain defensible.
    This is not an exhaustive claim that no narrower family identifier exists.
  evidence_ids:
  - eisosome-agent-family-IPR009571
  - eisosome-agent-P54003
  - record
- assessment_id: taxa
  area: scope
  topic: Qualitative fungal scope and exact placement of the yeast architecture source
  outcome: concern
  target_ids:
  - GO:0090512
  summary: The review abstract supports a varied fungal MCC/eisosome class, and direct
    W303 yeast data support the canonical S.cerevisiae model. COMMON is qualitative
    rather than a measured population frequency. The S.cerevisiae distribution note
    combines directly supported Sur7 localization with furrow/filament architecture,
    but cites only Walther; the latter architectural clause should instead cite the
    available Karotki results or Douglas review.
  evidence_ids:
  - eisosome-agent-taxon-4751
  - eisosome-agent-taxon-4932
  - eisosome-agent-taxon-559292
  - eisosome-agent-walther2006-publisher
  - eisosome-agent-karotki
  - douglas-review-abstract
  - record
- assessment_id: function
  area: evidence
  topic: Stable membrane compartmentation
  outcome: supported
  target_ids:
  - GO:0090512
  summary: The function is supported by stable Sur7/Pil1 patches, review-level MCC
    compartment organization, and Karotki membrane-scaffolding experiments. It does
    not repeat Walther historical endocytosis-site interpretation as an established
    MCC function or infer universal fungal rates/dimensions.
  evidence_ids:
  - eisosome-agent-walther2006-publisher
  - eisosome-agent-karotki
  - douglas-review-abstract
  - record
- assessment_id: graph
  area: graph
  topic: Localization plus experimentally supported scaffold mechanism
  outcome: supported
  target_ids:
  - GO:0090512
  summary: The Sur7 localizes-to edge is supported by direct colocalization. The filament
    scaffolds-MCC edge is supported by reconstitution, membrane tubulation, perturbations
    and in-cell immunolabeled lattice observations; ASSEMBLY/MECHANISTIC is appropriate
    for this bounded structural scaffold model. This does not assert exact contacts,
    obligatory temporal ordering, universal Pil1/Lsp1 pairing across Fungi, or Sur7
    assembly necessity.
  evidence_ids:
  - eisosome-agent-walther2006-publisher
  - eisosome-agent-karotki
  - graph-policy
  - record
- assessment_id: provenance
  area: provenance
  topic: Primary bodies, review abstract and historical access annotations
  outcome: supported
  target_ids:
  - GO:0090512
  summary: Walther main/Methods, Karotki named JATS sections and Young named PMC passages
    were read as direct primary evidence. Douglas is review-abstract evidence only
    after two publisher403 responses; the historical PMID rerouting note remains historical.
    Exact native citations resolve all four PMID transport residuals independently.
    The issue is a local architecture-source placement gap, not inaccessible historical
    evidence or a changed DOI identity.
  evidence_ids:
  - eisosome-agent-epmc
  - eisosome-agent-walther2006-publisher
  - eisosome-agent-karotki
  - eisosome-agent-young2002-legacy
  - douglas-review-abstract
  - douglas2014-publisher-access
  - douglas2014-pdf-access
  - record
- assessment_id: completeness
  area: completeness
  topic: Bounded component inventory and absent optional measurements
  outcome: supported
  target_ids:
  - GO:0090512
  summary: The record explicitly limits its constituent to demonstrated Sur7 and retains
    a TODO for other residents. It has no image or quantitative measurement assertion
    requiring inspection. No empty optional slot, untested Sur7 assembly necessity
    or historical access annotation is promoted to a finding.
  evidence_ids:
  - eisosome-agent-go
  - douglas-review-abstract
  - record
  - review-policy
findings:
- finding_id: F1
  issue_key: mcc-yeast-furrow-architecture-source-placement
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Cite the source that resolves MCC furrow and filament architecture
  description: The S.cerevisiae distribution note describes Sur7-marked furrow-like
    MCC domains paired with filaments but cites only Walther2006. That primary body
    establishes Sur7/Pil1 localization and immobile patches; its EM images described
    in the body concern abnormal pil1-deletion invaginations rather than normal furrow-and-filament
    architecture. Karotki2011 Results sec11/Fig7 directly support the fuller architecture
    and are already cited elsewhere in the record. The biological assertion is supported,
    but its nearest source is incomplete.
  target_ids:
  - GO:0090512
  field_paths:
  - taxonomic_distribution[taxon_id=NCBITaxon:4932].note
  - taxonomic_distribution[taxon_id=NCBITaxon:4932].reference
  evidence_ids:
  - eisosome-agent-walther2006-publisher
  - eisosome-agent-karotki
  - douglas-review-abstract
  - record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:Evidence Rules; nearest-claim
    support
  native_severity: minor
  normalization_reason: A non-blocking citation placement gap in an otherwise supported
    species/architecture assertion; it neither changes structure identity nor contradicts
    the biology.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    role: maintained scientific record
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0090512
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    role: maintained scientific record
  description: Replace the distribution-row reference with Karotki2011 or Douglas2014
    for its full furrow-and-filament wording, or narrow that note to the Sur7/eisosome
    localization established by Walther2006. Preserve the species scope and separate
    S288C identity-only protein example.
  acceptance_checks:
  - The nearest citation must support every retained anatomical clause; verify Karotki
    Results sec11/Fig7 or the exact Douglas abstract.
  - Retain W303 experimental context without treating it as an S288C-specific localization
    assay.
  - Any later maintained edit requires separate authorization, the guarded curation
    writer, history and focused schema/strict validation.
limitations:
- 'Douglas/Konopka2014 full body was not recovered: native publisher and PDF routes
  returned403. Only its exact native abstract supports qualitative fungal/domain statements.'
- Navarre2002 and Huh2003 are verified at native metadata/abstract and UniProt annotation-attribution
  level; their primary bodies were not independently inspected. Young2002 genuine
  PMC body was read at the named localization and methods passages.
- Karotki2011 text and captions support a structural scaffold model; image pixels
  and supplementary files were not reanalysed. Exact subunit contacts, mixed Pil1/Lsp1
  assemblies and additional membrane-bending mechanisms remain unresolved in that
  source.
- Walther2006 experiments use W303-derived strains. The record protein example is
  an explicitly identity-only S288C accession, not a claim of an identical experiment
  in that strain.
- Current GO parentage is verified as ontology hierarchy; the review terminology distinguishing
  MCC from lipid rafts is not treated as an independent experimental validation of
  raft biophysical properties.
- No exhaustive fungal occurrence survey, complete MCC resident inventory or all-family
  search was performed; no assembly necessity claim is added for Sur7.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Reused Karotki and three taxonomy raw/meta snapshots retain original batch6 UTC
  timestamps and byte hashes; scientific sources were read again for this target.
- All graph identifiers are external ontology terms or the local Sur7 component_ref;
  no neighboring maintained record was used as scientific evidence.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
