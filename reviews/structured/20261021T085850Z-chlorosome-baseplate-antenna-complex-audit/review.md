# Chlorosome baseplate identity, pigment-protein array and experimental preparation review

- Review: 20261021T085850Z-chlorosome-baseplate-antenna-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:41:22Z
- Finished UTC: 2026-10-21T08:58:50Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The CsmA/BChl a baseplate identity, constituent core and bounded excitation-transfer graph are supported. One minor correction should identify the mutant-derived organelle preparation in the canonical example.

## Scope And Provenance

Entire target; all graph edges/component/protein/example/discussion claims, native GO/ChEBI/taxa/UniProt/family candidates and source-specific primary preparation/structural evidence.

Selection: Fourth target in batch thirteen; strict repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:chlorosome_baseplate_antenna_complex | data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml | maintained | chlorosome baseplate antenna complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native UniProt verify | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | Read-only native check passed; generic downstream acceptor-chain node is not an exact protein accession claim. |
| Native UniProt causal-graphs | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | Read-only native check passed; generic downstream acceptor-chain node is not an exact protein accession claim. |
| Focused native schema | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | 14 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Defined pigment-protein array

identity: supported. Targets: cellstructuremech:chlorosome_baseplate_antenna_complex.

The whole complex has a local exact identity; the GO light-harvesting class is broader. The array and its envelope/chlorosome parthood are supported. No synonym is promoted to a whole-chlorosome or single-protein identity.

### CsmA and pigment roles

evidence: supported. Targets: cellstructuremech:chlorosome_baseplate_antenna_complex.

CsmA and bound BChl a are the defining constituent core. ESSENTIAL is read as required for the identity of this pigment-protein assembly, not a cell-viability or selective-mutant necessity result. Lipid/carotenoid context is not silently converted into a universal stoichiometric inventory.

### CsmA family boundary

grounding: supported. Targets: cellstructuremech:chlorosome_baseplate_antenna_complex.

Protein-example identity is verified; family candidates include CsmA/CsmE types and a broader superfamily. Retaining the exact-family TODO is defensible. The checked candidates do not justify claiming no family could ever be found.

### Canonical example wording

scope: concern. Targets: cellstructuremech:chlorosome_baseplate_antenna_complex.

The canonical note collapses the principal bchK-mutant carotenosome preparation into intact chlorosomes. Specify the mutant-derived organelles and integrative model, while retaining the wild-type comparison and species identity. This is a minor experimental-context correction.

### Species versus strain and inferred dimer

scope: supported. Targets: cellstructuremech:chlorosome_baseplate_antenna_complex.

Species identities and variable green-phototroph distribution are bounded. C.aurantiacus lattice/dimer wording is supported as an inference; TLS accession identity is not proof that every experimental preparation used that unmodified reference strain.

### Excitation flow

evidence: supported. Targets: cellstructuremech:chlorosome_baseplate_antenna_complex.

Light-harvesting function and outward energy routing are supported by structural interpretation and cited spectroscopy review. The record claims no quantum yield, timescale, necessary/sufficient perturbation or universal direct reaction-center contact.

### Five bounded edges

graph: supported. Targets: cellstructuremech:chlorosome_baseplate_antenna_complex.

CsmA assembly and BChl a binding follow the structural model; aggregate-to-baseplate transfer follows the review; downstream coupling and light-harvesting contribution retain lineage-specific intermediates as explicit omissions. NONMECHANISTIC is appropriate. The unanchored acceptor-chain node is an aggregate placeholder, not a single protein requiring a guessed accession.

### Evidence and historical model note

provenance: supported. Targets: cellstructuremech:chlorosome_baseplate_antenna_complex.

All cited identifiers are checked. Pedersen abstracts explicitly contain a structural model, supporting the maintained scientific note regardless of the publisher review label or historical event wording. No verbatim snippets, numerical properties or reusable image claims are asserted.

## Findings

### F1: Name the mutant-derived preparation in the canonical example

minor / open / confirmed; issue key: baseplate-canonical-mutant-preparation.

The canonical Chlorobaculum tepidum note says intact chlorosomes were used to resolve the in situ structure. Nielsen2016 Methods specify that these were isolated bchK-mutant carotenosomes lacking BChl c as the principal NMR/cryo-EM/optical-model preparation; wild-type chlorosomes provide a freeze-fracture comparison. Naming that preparation makes the experiment reproducible without implying an unmodified wild-type sample. The paper itself describes the organelles as intact and the structure as in situ; those terms need not be removed, and the target makes no explicit wild-type claim. The baseplate architecture and species identity remain supported.

## Recommended Actions And Acceptance Checks

### A1

Clarify the canonical note to say bchK-mutant carotenosomes and an integrative baseplate model, with wild-type chlorosome comparison where useful. Keep the original species/example and citation.

- Match the preparation statement to Nielsen2016 Methods and distinguish the wild-type comparison.
- Do not describe the result as an atomic cryo-EM-only map or an experimentally demonstrated assembly pathway.
- Use the guarded record writer, append curation/repository history, regenerate pages, and pass native schema/strict/products/history/qc gates in separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml; Entire maintained YAML including history, all component/protein/graph/evidence/discussion fields | context_only | Complete maintained record read; PROPOSED status and historical curation preserved. |
| policy | docs/CURATION.md; Components and evidence rules; exact review profile/checklist/schema captured in native inspect | context_only | Exact identifiers are required when assigned, but label-only constituent rows may retain unresolved family grounding; source-specific preparation and inference must be preserved. |
| baseplate-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009765,GO:0030076,GO:0033105,GO:0046858; Full GO0030076/0046858/0033105/0009765 results: identities, definitions, status, synonyms and available children | supports | Four active native GO definitions distinguish light-harvesting complex, chlorosome, monolayer chlorosome envelope and light-harvesting function. The baseplate is a specialized protein-pigment array, not the entire chlorosome or generic CsmA protein. |
| baseplate-prep-chebi30033 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/30033/; chebi_accession,ascii_name,is_released,stars and chemical_data | supports | Released three-star CHEBI:30033 has ascii_name bacteriochlorophyll a and formula C55H74MgN4O6; it is the pigment class named in the target, not the bulk BChl c aggregate. |
| baseplate-prep-nielsen2016-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4992139.1/PMC4992139.1.xml; PMC4992139 native JATS: full Results, Discussion and Methods, especially Sample preparation/Growth of Chlorobaculum tepidum bchK mutant, Isolation of carotenosomes, Solid-State NMR, Cryo-EM and calculation of baseplate structure. Claim-bearing captions read in these sections; no figure pixels or supplementary dataset reanalysis. | supports | The primary work resolves a CsmA/BChl a baseplate model using bchK-mutant carotenosomes lacking bulk BChl c. Wild-type and mutant freeze-fracture patterns are compared. Isolated carotenosomes, freeze-dried isotope-labeled ssNMR, cryo-EM and optical constraints jointly support rows of CsmA dimers with bound pigment; this is an integrative structure, not an atomic cryo-EM-only or native-cell assembly experiment. |
| baseplate-prep-psencik2009-pmc-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC2795307/; PMC2795307 native HTML: Materials and Methods; Results/Cryo-EM; Discussion/Perpendicular striation; abstract and Figure2 caption. No figure pixels. | supports | C.aurantiacus J-10-fl chlorosomes were isolated after growth at50C; primary cryo-EM shows a regular lattice confined to one face. The CsmA dimer is inferred from spacing and apparent globule mass, supported by earlier cross-linking/NMR; it is not an atomic protein assignment in this experiment. |
| baseplate-prep-oostergetel2010-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2882566.1/PMC2882566.1.xml; PMC2882566 native JATS: Organization of the baseplate and complete Light-harvesting and spectroscopic properties sections, with Abstract. Secondary synthesis identified explicitly. | supports | The review describes the baseplate as a CsmA/BChl a array in the chlorosome boundary and summarizes excitation transfer from bulk pigments to baseplate and onward via lineage-dependent acceptors. CsmA arrangement and entropic explanations are models, not selective assembly interventions. |
| baseplate-prep-pedersen2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A20077007%20AND%20SRC%3AMED; Exact bibliographic identity and complete abstract; full body unavailable. | supports | PMID20077007 resolves to Pedersen et al.2010, DOI10.1007/s11120-009-9519-y. Its abstract reviews prior baseplate knowledge and proposes a combined NMR/spectral model; the maintained note saying modeled is supported. |
| baseplate-prep-orf2013-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s11120-013-9869-3; Exact bibliographic identity and complete abstract only. | supports | Orf and Blankenship2013 DOI10.1007/s11120-013-9869-3, PMID23761131, describes in its abstract a CsmA/BChl a paracrystalline baseplate facing the next energy acceptor in green photosynthetic bacteria. |
| baseplate-prep-nielsen2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/ncomms12454; Complete exact DOI bibliographic result identity fields | supports | Exact DOI/title/authors/year/PMID/PMC agree with the cited work and full-text counterpart. |
| baseplate-prep-psencik2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/JB.00690-09; Complete exact DOI bibliographic result identity fields | supports | Exact DOI/title/authors/year/PMID/PMC agree with the cited work and full-text counterpart. |
| baseplate-prep-oostergetel2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s11120-010-9533-0; Complete exact DOI bibliographic result identity fields | supports | Exact DOI/title/authors/year/PMID/PMC agree with the cited work and full-text counterpart. |
| baseplate-prep-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; taxId, scientificName, rank, lineage and otherNames | supports | Native taxId and scientificName match the declared Bacteria, Chlorobaculum tepidum, Chloroflexus aurantiacus or TLS strain; rank, lineage and synonyms keep strain and species distinct. |
| baseplate-prep-tax-1097 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1097; taxId, scientificName, rank, lineage and otherNames | supports | Native taxId and scientificName match the declared Bacteria, Chlorobaculum tepidum, Chloroflexus aurantiacus or TLS strain; rank, lineage and synonyms keep strain and species distinct. |
| baseplate-prep-tax-1108 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1108; taxId, scientificName, rank, lineage and otherNames | supports | Native taxId and scientificName match the declared Bacteria, Chlorobaculum tepidum, Chloroflexus aurantiacus or TLS strain; rank, lineage and synonyms keep strain and species distinct. |
| baseplate-prep-tax-194439 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/194439; taxId, scientificName, rank, lineage and otherNames | supports | Native taxId and scientificName match the declared Bacteria, Chlorobaculum tepidum, Chloroflexus aurantiacus or TLS strain; rank, lineage and synonyms keep strain and species distinct. |
| baseplate-prep-P0A314 | https://rest.uniprot.org/uniprotkb/P0A314.json; primaryAccession,entryType,proteinDescription,genes and organism | supports | P0A314 is reviewed CsmA/CT1942 in taxon194439; recommended name remains Bacteriochlorophyll c-binding protein and alternative name is Chlorosome protein A. This nomenclature is accession identity, while baseplate membership rests on the primary paper. |
| baseplate-prep-query-csmA | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AcsmA%29%20AND%20%28organism_id%3A194439%29%20AND%20%28reviewed%3Atrue%29; Complete one-result native query; no broad-species uniqueness inferred | supports | The exact reviewed csmA/taxon194439 query yields P0A314 alone. |
| baseplate-prep-matches-P0A314 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P0A314/; Complete native response, type/name/description/member databases/hierarchy or all match/search results | supports | Complete six-match response has no next page and supplies family and superfamily candidates. |
| baseplate-prep-IPR001470 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001470/; Complete native response, type/name/description/member databases/hierarchy or all match/search results | supports | Family integrates PIRSF002903 CsmA/CsmE types together with PF02043; its old BChl-c-binding description does not establish an exact CsmA-only family boundary. |
| baseplate-prep-IPR038387 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038387/; Complete native response, type/name/description/member databases/hierarchy or all match/search results | supports | Homologous superfamily is broader than a precise CsmA component identity. |
| baseplate-prep-PF02043 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF02043/; Complete native response, type/name/description/member databases/hierarchy or all match/search results | supports | Family is integrated into IPR001470 and does not independently resolve the CsmA/CsmE boundary. |
| baseplate-prep-family-search | https://www.ebi.ac.uk/interpro/api/entry/all/?search=CsmA; Complete native response, type/name/description/member databases/hierarchy or all match/search results | supports | Bounded CsmA search yields the CsmA/CsmE-types PIRSF entry; no exhaustive absence claim follows. |
| uniprot-verify | /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml --verify; Captured native read-only check log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| uniprot-causal-graphs | /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml --causal-graphs; Captured native read-only check log | supports | data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml  (cellstructuremech:chlorosome_baseplate_antenna_complex)<br>  baseplate_excitation_transfer	csma_apoprotein	COVERED	-&gt;csma_apoprotein (UniProtKB:P0A314)<br>  baseplate_excitation_transfer	reaction_center_acceptor_chain	UNANCHORED_NO_UNIPROT	membrane reaction-center acceptor chain<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     2  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml |
| strict-result | just validate-strict data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/chlorosome_baseplate_antenna_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/chlorosome_baseplate_antenna_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch13-20261021-vud60b4w/chlorosome_baseplate_antenna_complex-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 14 of16 collected target identifiers returned OK at the unchanged base. Residuals: PMID:20077007: UNREACHABLE; resolved by evidence baseplate-prep-pedersen2010-meta; cellstructuremech:chlorosome_baseplate_antenna_complex: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Pedersen2010 and Orf2013 full bodies were unavailable; their inspected native metadata/abstracts and publisher abstract pages support only the explicitly stated model/background scope. Nielsen2016 and Psencik2009 primary claim-bearing body sections were read.
- No figure pixels, supplementary data, coordinates, raw spectra or tomograms were reanalyzed. Integrative structure does not demonstrate a necessary/sufficient biogenesis pathway.
- The initial native UniProt verify request failed under sandbox DNS; its failure log is retained and the network-enabled read-only rerun passed.
- Family checking is bounded to the complete current P0A314 match response and named candidates/search; no exhaustive family absence or iModulon-based localization claim is made.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- No neighboring maintained-record dependency; all13 native input hashes checked.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T085850Z-chlorosome-baseplate-antenna-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Chlorosome baseplate identity, pigment-protein array and experimental preparation
  review
started_at: '2026-10-21T08:41:22Z'
finished_at: '2026-10-21T08:58:50Z'
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
summary: The CsmA/BChl a baseplate identity, constituent core and bounded excitation-transfer
  graph are supported. One minor correction should identify the mutant-derived organelle
  preparation in the canonical example.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    sha256: 7ea00dedcd0998fc477737d6d2e8301e4e57a08e57378d19efe5e32a6ea8c92d
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
- target_id: cellstructuremech:chlorosome_baseplate_antenna_complex
  path: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
  label: chlorosome baseplate antenna complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    role: maintained scientific record
scope:
  description: Entire target; all graph edges/component/protein/example/discussion
    claims, native GO/ChEBI/taxa/UniProt/family candidates and source-specific primary
    preparation/structural evidence.
  selection: Fourth target in batch thirteen; strict repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
checks:
- check_id: uniprot-verify
  name: Native UniProt verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  command: /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native check passed; generic downstream acceptor-chain node is
    not an exact protein accession claim.
  evidence_ids:
  - uniprot-verify
- check_id: uniprot-causal-graphs
  name: Native UniProt causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  command: /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native check passed; generic downstream acceptor-chain node is
    not an exact protein accession claim.
  evidence_ids:
  - uniprot-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  command: just validate data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  command: just validate-strict data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/chlorosome_baseplate_antenna_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  summary: 14 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - baseplate-prep-pedersen2010-meta
  - record
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - baseplate-prep-go
  - baseplate-prep-chebi30033
  - baseplate-prep-nielsen2016-jats
  - baseplate-prep-psencik2009-pmc-html
  - baseplate-prep-oostergetel2010-jats
  - baseplate-prep-pedersen2010-meta
  - baseplate-prep-orf2013-meta
  - baseplate-prep-nielsen2016-meta
  - baseplate-prep-psencik2009-meta
  - baseplate-prep-oostergetel2010-meta
  - baseplate-prep-tax-2
  - baseplate-prep-tax-1097
  - baseplate-prep-tax-1108
  - baseplate-prep-tax-194439
  - baseplate-prep-P0A314
  - baseplate-prep-query-csmA
  - baseplate-prep-matches-P0A314
  - baseplate-prep-IPR001470
  - baseplate-prep-IPR038387
  - baseplate-prep-PF02043
  - baseplate-prep-family-search
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
  locator: Entire maintained YAML including history, all component/protein/graph/evidence/discussion
    fields
  accessed_at: '2026-10-21T08:53:44Z'
  support: context_only
  summary: Complete maintained record read; PROPOSED status and historical curation
    preserved.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Components and evidence rules; exact review profile/checklist/schema captured
    in native inspect
  accessed_at: '2026-10-21T08:53:44Z'
  support: context_only
  summary: Exact identifiers are required when assigned, but label-only constituent
    rows may retain unresolved family grounding; source-specific preparation and inference
    must be preserved.
- evidence_id: baseplate-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009765,GO:0030076,GO:0033105,GO:0046858
  locator: 'Full GO0030076/0046858/0033105/0009765 results: identities, definitions,
    status, synonyms and available children'
  accessed_at: '2026-10-21T08:39:14.328125Z'
  support: supports
  summary: Four active native GO definitions distinguish light-harvesting complex,
    chlorosome, monolayer chlorosome envelope and light-harvesting function. The baseplate
    is a specialized protein-pigment array, not the entire chlorosome or generic CsmA
    protein.
  snapshot_sha256: 4fd43249fb65f5ee2156ac8bfda3aedd6dcc7029236d06cda87c09c9b39eeb7d
- evidence_id: baseplate-prep-chebi30033
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/30033/
  locator: chebi_accession,ascii_name,is_released,stars and chemical_data
  accessed_at: '2026-10-21T08:39:19.554773Z'
  support: supports
  summary: Released three-star CHEBI:30033 has ascii_name bacteriochlorophyll a and
    formula C55H74MgN4O6; it is the pigment class named in the target, not the bulk
    BChl c aggregate.
  snapshot_sha256: bf5d6ba8661e567f53a1a37b895cf6657fa63952eb5407f63419ee75813ef416
- evidence_id: baseplate-prep-nielsen2016-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4992139.1/PMC4992139.1.xml
  locator: 'PMC4992139 native JATS: full Results, Discussion and Methods, especially
    Sample preparation/Growth of Chlorobaculum tepidum bchK mutant, Isolation of carotenosomes,
    Solid-State NMR, Cryo-EM and calculation of baseplate structure. Claim-bearing
    captions read in these sections; no figure pixels or supplementary dataset reanalysis.'
  accessed_at: '2026-10-21T08:40:21.651455Z'
  support: supports
  summary: The primary work resolves a CsmA/BChl a baseplate model using bchK-mutant
    carotenosomes lacking bulk BChl c. Wild-type and mutant freeze-fracture patterns
    are compared. Isolated carotenosomes, freeze-dried isotope-labeled ssNMR, cryo-EM
    and optical constraints jointly support rows of CsmA dimers with bound pigment;
    this is an integrative structure, not an atomic cryo-EM-only or native-cell assembly
    experiment.
  snapshot_sha256: 0c5f33758e0ffea1a267cca08a1bcbb0da36023045ba7fcdc9189dfe9f6b3922
- evidence_id: baseplate-prep-psencik2009-pmc-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2795307/
  locator: 'PMC2795307 native HTML: Materials and Methods; Results/Cryo-EM; Discussion/Perpendicular
    striation; abstract and Figure2 caption. No figure pixels.'
  accessed_at: '2026-10-21T08:42:01.318551Z'
  support: supports
  summary: C.aurantiacus J-10-fl chlorosomes were isolated after growth at50C; primary
    cryo-EM shows a regular lattice confined to one face. The CsmA dimer is inferred
    from spacing and apparent globule mass, supported by earlier cross-linking/NMR;
    it is not an atomic protein assignment in this experiment.
  snapshot_sha256: da5d24b9f3f0abb179bd1b1b996a5b8b8542d2c9e67d3d07149b6e4636d9108a
- evidence_id: baseplate-prep-oostergetel2010-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2882566.1/PMC2882566.1.xml
  locator: 'PMC2882566 native JATS: Organization of the baseplate and complete Light-harvesting
    and spectroscopic properties sections, with Abstract. Secondary synthesis identified
    explicitly.'
  accessed_at: '2026-10-21T08:40:21.570713Z'
  support: supports
  summary: The review describes the baseplate as a CsmA/BChl a array in the chlorosome
    boundary and summarizes excitation transfer from bulk pigments to baseplate and
    onward via lineage-dependent acceptors. CsmA arrangement and entropic explanations
    are models, not selective assembly interventions.
  snapshot_sha256: d555d33602f2946ad490d2d02be169d4f767093604c513edbf0d0753b347cea5
- evidence_id: baseplate-prep-pedersen2010-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A20077007%20AND%20SRC%3AMED
  locator: Exact bibliographic identity and complete abstract; full body unavailable.
  accessed_at: '2026-10-21T08:39:17.818841Z'
  support: supports
  summary: PMID20077007 resolves to Pedersen et al.2010, DOI10.1007/s11120-009-9519-y.
    Its abstract reviews prior baseplate knowledge and proposes a combined NMR/spectral
    model; the maintained note saying modeled is supported.
  snapshot_sha256: 5780b95d98ba52d20ce49b6e2b546c6b931f70ef4a9b3032a22fabfe4226792e
- evidence_id: baseplate-prep-orf2013-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s11120-013-9869-3
  locator: Exact bibliographic identity and complete abstract only.
  accessed_at: '2026-10-21T08:39:18.111581Z'
  support: supports
  summary: Orf and Blankenship2013 DOI10.1007/s11120-013-9869-3, PMID23761131, describes
    in its abstract a CsmA/BChl a paracrystalline baseplate facing the next energy
    acceptor in green photosynthetic bacteria.
  snapshot_sha256: fe8c53d3d2226385cd7e88b2bea020c3dc89afdcfb6fc8d6d5870e9090a56e42
- evidence_id: baseplate-prep-nielsen2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/ncomms12454
  locator: Complete exact DOI bibliographic result identity fields
  accessed_at: '2026-10-21T08:39:17.817415Z'
  support: supports
  summary: Exact DOI/title/authors/year/PMID/PMC agree with the cited work and full-text
    counterpart.
  snapshot_sha256: 0040f396e49964974cf13f9586dbe914d0d51af62d0735571df420a194d9b999
- evidence_id: baseplate-prep-psencik2009-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/JB.00690-09
  locator: Complete exact DOI bibliographic result identity fields
  accessed_at: '2026-10-21T08:39:17.997855Z'
  support: supports
  summary: Exact DOI/title/authors/year/PMID/PMC agree with the cited work and full-text
    counterpart.
  snapshot_sha256: 202f2a3417932350d1493429648939255e642aee21d9a0d48b922102f0faa232
- evidence_id: baseplate-prep-oostergetel2010-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s11120-010-9533-0
  locator: Complete exact DOI bibliographic result identity fields
  accessed_at: '2026-10-21T08:39:18.509220Z'
  support: supports
  summary: Exact DOI/title/authors/year/PMID/PMC agree with the cited work and full-text
    counterpart.
  snapshot_sha256: d21480df53f3ec2d31f92b75e5938899961494a54d211fab7ece2c5af71c5907
- evidence_id: baseplate-prep-tax-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-21T08:39:14.454254Z'
  support: supports
  summary: Native taxId and scientificName match the declared Bacteria, Chlorobaculum
    tepidum, Chloroflexus aurantiacus or TLS strain; rank, lineage and synonyms keep
    strain and species distinct.
  snapshot_sha256: 7429617438ff0162ee4783c4c660f6127642e6ff686522e670c6ecf3a5b28816
- evidence_id: baseplate-prep-tax-1097
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1097
  locator: taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-21T08:39:14.312179Z'
  support: supports
  summary: Native taxId and scientificName match the declared Bacteria, Chlorobaculum
    tepidum, Chloroflexus aurantiacus or TLS strain; rank, lineage and synonyms keep
    strain and species distinct.
  snapshot_sha256: a8e843e290efea6a5a31d92ee3cdb32ee8bae331690d26d3c87955c375625c37
- evidence_id: baseplate-prep-tax-1108
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1108
  locator: taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-21T08:39:14.399358Z'
  support: supports
  summary: Native taxId and scientificName match the declared Bacteria, Chlorobaculum
    tepidum, Chloroflexus aurantiacus or TLS strain; rank, lineage and synonyms keep
    strain and species distinct.
  snapshot_sha256: 0deab46a2ef0f0db1b1d668e0a685004fe06f6d56ee255e35d67d47e3e481278
- evidence_id: baseplate-prep-tax-194439
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/194439
  locator: taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-21T08:39:14.378082Z'
  support: supports
  summary: Native taxId and scientificName match the declared Bacteria, Chlorobaculum
    tepidum, Chloroflexus aurantiacus or TLS strain; rank, lineage and synonyms keep
    strain and species distinct.
  snapshot_sha256: db206b8370769142a525002170c3e080b17cdb2493db598567586f1d4cae4eae
- evidence_id: baseplate-prep-P0A314
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A314.json
  locator: primaryAccession,entryType,proteinDescription,genes and organism
  accessed_at: '2026-10-21T08:39:14.950184Z'
  support: supports
  summary: P0A314 is reviewed CsmA/CT1942 in taxon194439; recommended name remains
    Bacteriochlorophyll c-binding protein and alternative name is Chlorosome protein
    A. This nomenclature is accession identity, while baseplate membership rests on
    the primary paper.
  snapshot_sha256: 39dadbdc04fa6b4350a737e9894067b526bb041096c6a646b145818be2e1fdfa
- evidence_id: baseplate-prep-query-csmA
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AcsmA%29%20AND%20%28organism_id%3A194439%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete one-result native query; no broad-species uniqueness inferred
  accessed_at: '2026-10-21T08:39:15.123206Z'
  support: supports
  summary: The exact reviewed csmA/taxon194439 query yields P0A314 alone.
  snapshot_sha256: 1da994559466dcbde681f76bcb44c9d8657f7d417e713a0a35eb8f977fea2fe5
- evidence_id: baseplate-prep-matches-P0A314
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P0A314/
  locator: Complete native response, type/name/description/member databases/hierarchy
    or all match/search results
  accessed_at: '2026-10-21T08:39:20.923741Z'
  support: supports
  summary: Complete six-match response has no next page and supplies family and superfamily
    candidates.
  snapshot_sha256: 54f4d65be0a9e9b2b9f0f132f009cff6bd1b7b844d423447f3e122b67fccd4e9
- evidence_id: baseplate-prep-IPR001470
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001470/
  locator: Complete native response, type/name/description/member databases/hierarchy
    or all match/search results
  accessed_at: '2026-10-21T08:40:22.380658Z'
  support: supports
  summary: Family integrates PIRSF002903 CsmA/CsmE types together with PF02043; its
    old BChl-c-binding description does not establish an exact CsmA-only family boundary.
  snapshot_sha256: b7ecd7ee239d1d15fa957b33f47c5bb199110209ede25c570b6be41495254ca5
- evidence_id: baseplate-prep-IPR038387
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038387/
  locator: Complete native response, type/name/description/member databases/hierarchy
    or all match/search results
  accessed_at: '2026-10-21T08:40:22.427160Z'
  support: supports
  summary: Homologous superfamily is broader than a precise CsmA component identity.
  snapshot_sha256: 90237667525b4f5d3b866682446f639afa8cb06ae267cdaf2d5dd7d4becbb904
- evidence_id: baseplate-prep-PF02043
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF02043/
  locator: Complete native response, type/name/description/member databases/hierarchy
    or all match/search results
  accessed_at: '2026-10-21T08:40:22.413975Z'
  support: supports
  summary: Family is integrated into IPR001470 and does not independently resolve
    the CsmA/CsmE boundary.
  snapshot_sha256: d9e9b8b57fada37ee6b5d467b8b9d94a15302afa1e84c2edaf9620ca76c9d885
- evidence_id: baseplate-prep-family-search
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/?search=CsmA
  locator: Complete native response, type/name/description/member databases/hierarchy
    or all match/search results
  accessed_at: '2026-10-21T08:40:26.303386Z'
  support: supports
  summary: Bounded CsmA search yields the CsmA/CsmE-types PIRSF entry; no exhaustive
    absence claim follows.
  snapshot_sha256: cd4dbab658813d61d165a3c2c73269fa7a41c47af2e49d1866696d8a5f1682f7
- evidence_id: uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    --verify
  locator: Captured native read-only check log
  accessed_at: '2026-10-21T08:48:42.588746Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: uniprot-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    --causal-graphs
  locator: Captured native read-only check log
  accessed_at: '2026-10-21T08:48:12.287970Z'
  support: supports
  summary: "data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml\
    \  (cellstructuremech:chlorosome_baseplate_antenna_complex)\n  baseplate_excitation_transfer\t\
    csma_apoprotein\tCOVERED\t->csma_apoprotein (UniProtKB:P0A314)\n  baseplate_excitation_transfer\t\
    reaction_center_acceptor_chain\tUNANCHORED_NO_UNIPROT\tmembrane reaction-center\
    \ acceptor chain\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     1  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB\
    \ grounding or xref on the node\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     2 \
    \ total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 9f6c213cca24fffa1b071461a1e606371dc4c0a90888e54babe8f67b85ca3e69
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:41:26Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml'
  snapshot_sha256: 781160c98258041a10c80c01807845cb7ca4b7e6fe22d892c6abaf2b5ac3e2c3
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/chlorosome_baseplate_antenna_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:41:29Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml\
    \ --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/chlorosome_baseplate_antenna_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch13-20261021-vud60b4w/chlorosome_baseplate_antenna_complex-strict.tsv"
  snapshot_sha256: 990e0f7b54cdaf87aeb5cc275eacbf7f4dc853a18ae00b79715e376fe929af7e
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml;
    exact collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T08:53:44Z'
  support: supports
  summary: '14 of16 collected target identifiers returned OK at the unchanged base.
    Residuals: PMID:20077007: UNREACHABLE; resolved by evidence baseplate-prep-pedersen2010-meta;
    cellstructuremech:chlorosome_baseplate_antenna_complex: SKIPPED; resolved by evidence
    record. Source-native identity checked separately.'
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
  topic: Defined pigment-protein array
  outcome: supported
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  summary: The whole complex has a local exact identity; the GO light-harvesting class
    is broader. The array and its envelope/chlorosome parthood are supported. No synonym
    is promoted to a whole-chlorosome or single-protein identity.
  evidence_ids:
  - baseplate-prep-go
  - baseplate-prep-nielsen2016-jats
  - baseplate-prep-psencik2009-pmc-html
  - baseplate-prep-oostergetel2010-jats
  - record
- assessment_id: composition
  area: evidence
  topic: CsmA and pigment roles
  outcome: supported
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  summary: CsmA and bound BChl a are the defining constituent core. ESSENTIAL is read
    as required for the identity of this pigment-protein assembly, not a cell-viability
    or selective-mutant necessity result. Lipid/carotenoid context is not silently
    converted into a universal stoichiometric inventory.
  evidence_ids:
  - baseplate-prep-nielsen2016-jats
  - baseplate-prep-chebi30033
  - record
- assessment_id: family
  area: grounding
  topic: CsmA family boundary
  outcome: supported
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  summary: Protein-example identity is verified; family candidates include CsmA/CsmE
    types and a broader superfamily. Retaining the exact-family TODO is defensible.
    The checked candidates do not justify claiming no family could ever be found.
  evidence_ids:
  - baseplate-prep-P0A314
  - baseplate-prep-query-csmA
  - baseplate-prep-matches-P0A314
  - baseplate-prep-IPR001470
  - baseplate-prep-IPR038387
  - baseplate-prep-PF02043
  - baseplate-prep-family-search
  - record
- assessment_id: preparation
  area: scope
  topic: Canonical example wording
  outcome: concern
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  summary: The canonical note collapses the principal bchK-mutant carotenosome preparation
    into intact chlorosomes. Specify the mutant-derived organelles and integrative
    model, while retaining the wild-type comparison and species identity. This is
    a minor experimental-context correction.
  evidence_ids:
  - baseplate-prep-nielsen2016-jats
  - record
- assessment_id: examples
  area: scope
  topic: Species versus strain and inferred dimer
  outcome: supported
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  summary: Species identities and variable green-phototroph distribution are bounded.
    C.aurantiacus lattice/dimer wording is supported as an inference; TLS accession
    identity is not proof that every experimental preparation used that unmodified
    reference strain.
  evidence_ids:
  - baseplate-prep-tax-2
  - baseplate-prep-tax-1097
  - baseplate-prep-tax-1108
  - baseplate-prep-tax-194439
  - baseplate-prep-nielsen2016-jats
  - baseplate-prep-psencik2009-pmc-html
  - baseplate-prep-orf2013-meta
  - baseplate-prep-P0A314
  - record
- assessment_id: function
  area: evidence
  topic: Excitation flow
  outcome: supported
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  summary: Light-harvesting function and outward energy routing are supported by structural
    interpretation and cited spectroscopy review. The record claims no quantum yield,
    timescale, necessary/sufficient perturbation or universal direct reaction-center
    contact.
  evidence_ids:
  - baseplate-prep-nielsen2016-jats
  - baseplate-prep-oostergetel2010-jats
  - baseplate-prep-orf2013-meta
  - baseplate-prep-go
  - record
- assessment_id: graph
  area: graph
  topic: Five bounded edges
  outcome: supported
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  summary: CsmA assembly and BChl a binding follow the structural model; aggregate-to-baseplate
    transfer follows the review; downstream coupling and light-harvesting contribution
    retain lineage-specific intermediates as explicit omissions. NONMECHANISTIC is
    appropriate. The unanchored acceptor-chain node is an aggregate placeholder, not
    a single protein requiring a guessed accession.
  evidence_ids:
  - baseplate-prep-nielsen2016-jats
  - baseplate-prep-oostergetel2010-jats
  - baseplate-prep-orf2013-meta
  - baseplate-prep-chebi30033
  - record
- assessment_id: provenance
  area: provenance
  topic: Evidence and historical model note
  outcome: supported
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  summary: All cited identifiers are checked. Pedersen abstracts explicitly contain
    a structural model, supporting the maintained scientific note regardless of the
    publisher review label or historical event wording. No verbatim snippets, numerical
    properties or reusable image claims are asserted.
  evidence_ids:
  - baseplate-prep-pedersen2010-meta
  - baseplate-prep-nielsen2016-jats
  - baseplate-prep-psencik2009-pmc-html
  - baseplate-prep-oostergetel2010-jats
  - baseplate-prep-orf2013-meta
  - record
findings:
- finding_id: F1
  issue_key: baseplate-canonical-mutant-preparation
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Name the mutant-derived preparation in the canonical example
  description: The canonical Chlorobaculum tepidum note says intact chlorosomes were
    used to resolve the in situ structure. Nielsen2016 Methods specify that these
    were isolated bchK-mutant carotenosomes lacking BChl c as the principal NMR/cryo-EM/optical-model
    preparation; wild-type chlorosomes provide a freeze-fracture comparison. Naming
    that preparation makes the experiment reproducible without implying an unmodified
    wild-type sample. The paper itself describes the organelles as intact and the
    structure as in situ; those terms need not be removed, and the target makes no
    explicit wild-type claim. The baseplate architecture and species identity remain
    supported.
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  field_paths:
  - canonical_examples[taxon_id=NCBITaxon:1097].note
  evidence_ids:
  - baseplate-prep-nielsen2016-jats
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: Non-blocking preparation precision; neither exact structure
    identity nor the supported architecture is invalidated.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    role: maintained scientific record
  description: Clarify the canonical note to say bchK-mutant carotenosomes and an
    integrative baseplate model, with wild-type chlorosome comparison where useful.
    Keep the original species/example and citation.
  acceptance_checks:
  - Match the preparation statement to Nielsen2016 Methods and distinguish the wild-type
    comparison.
  - Do not describe the result as an atomic cryo-EM-only map or an experimentally
    demonstrated assembly pathway.
  - Use the guarded record writer, append curation/repository history, regenerate
    pages, and pass native schema/strict/products/history/qc gates in separately authorized
    curation.
  generator: Maintained structure YAML; generated pages derive from it.
limitations:
- Pedersen2010 and Orf2013 full bodies were unavailable; their inspected native metadata/abstracts
  and publisher abstract pages support only the explicitly stated model/background
  scope. Nielsen2016 and Psencik2009 primary claim-bearing body sections were read.
- No figure pixels, supplementary data, coordinates, raw spectra or tomograms were
  reanalyzed. Integrative structure does not demonstrate a necessary/sufficient biogenesis
  pathway.
- The initial native UniProt verify request failed under sandbox DNS; its failure
  log is retained and the network-enabled read-only rerun passed.
- Family checking is bounded to the complete current P0A314 match response and named
  candidates/search; no exhaustive family absence or iModulon-based localization claim
  is made.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- No neighboring maintained-record dependency; all13 native input hashes checked.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
