# Source-backed review of bacterial microcompartment

- Review: 20261022T041112Z-bacterial-microcompartment-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:46:56Z
- Finished UTC: 2026-10-22T04:11:12Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor correction resolves the generic BMC-P protein-family grounding; the class, coarse composition, distribution and source-qualified shell model are supported.

## Scope And Provenance

One complete target, with the other three BMC/carboxysome/shell/Eut records frozen as boundary context. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch42 fixed strict path order, index 6; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031469 | data/structures/microcompartment/bacterial_microcompartment.yaml | maintained | bacterial microcompartment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0031469 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031469 | Focused validator passed. |
| Focused native proteins | passed | True | GO:0031469 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | GO:0031469 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:0031469 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031469 | 8 of 8 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031469 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031469 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031469 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031469 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031469 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact class and subtype boundaries

identity: supported. Targets: GO:0031469.

The bacterial protein-shelled organelle identity, membraneless parent and catabolic metabolosome subset are supported. The local carboxysome and Eut siblings preserve their specialized chemistry.

### Supported H/T/P and cargo classes

grounding: concern. Targets: GO:0031469.

The four coarse component classes accurately cover shell building blocks and heterogeneous enzyme cargo. H/T/cargo label-only boundaries are justified by architecture and metabolic heterogeneity; P-family withholding instead uses an assembled-vertex requirement on a PROTEIN row.

### Formation labels remain condition dependent

grounding: unknown. Targets: GO:0031469.

H is a constitutional major facet class in characterized shells; T/P and native cargo requirements vary by BMC and recombinant construct. CONDITIONAL does not identify every particular deletion condition. No formation necessity of every individual T/P protein is inferred from intact-shell structure alone.

### Distribution and recombinant canonical example

scope: supported. Targets: GO:0031469.

Native taxon identities are correct. The canonical HO note accurately identifies the shell used for structural work, not a directly isolated native enzyme-loaded organelle. The protein set was recombinantly expressed; VARIABLE Bacteria is supported by the catalog rather than a universal prevalence claim.

### Encapsulation and selective-permeability evidence

evidence: supported. Targets: GO:0031469.

Segregation/retention and pore-based exchange are supported at the synthesis/model level. The Greber evidence note explicitly calls its permeability route modelled; no direct rate or physiological substrate specificity is asserted.

### Directed shell construction and metabolic coupling

graph: supported. Targets: GO:0031469.

Every H/T/P assembly and cargo/exchange edge is compatible with the source-supported model. A mechanistic coarse graph is appropriate; it does not force identical pore composition or a demonstrated native HO metabolic pathway. Generic protein actor nodes do not require invented strain-specific instances.

### Full record and bounded enrichments

completeness: supported. Targets: GO:0031469.

All current and historical fields were read. No images, verbatim snippets or protein examples occur in this target. Optional inventories and unavailable exact H/T architectural families do not become automatic findings. The verified generic BMC-P family is a concrete resolvable grounding gap.

## Findings

### F1: Ground the generic BMC-P protein cohort to its verified family

minor / open / confirmed; issue key: bacterial-microcompartment-bmc-p-family.

The PROTEIN component deliberately withholds grounding because PF03319 does not denote an assembled lineage-neutral vertex. This record models the generic BMC-P proteins, for which IPR004992 supplies the verified family across carboxysomes and metabolosomes; assembly geometry belongs in the role/evidence.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, ground the generic BMC-P protein component to the verified family and retain explicit pentamer/vertex role qualifications. Do not export the same broad family as an exact carboxysome-only or EutN-only identity.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/microcompartment/bacterial_microcompartment.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | Protein-family identity is distinct from an assembled complex. ESSENTIAL concerns failure of structure formation, not loss of catalytic function or ambient-CO2 growth. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| neighbor-carboxysome | data/structures/microcompartment/carboxysome.yaml; Complete frozen BMC/carboxysome/shell/Eut boundary neighbor | context_only | Frozen neighboring record read for class, family and boundary context; its scientific verdict is not imported. |
| neighbor-carboxysome_shell | data/structures/microcompartment/carboxysome_shell.yaml; Complete frozen BMC/carboxysome/shell/Eut boundary neighbor | context_only | Frozen neighboring record read for class, family and boundary context; its scientific verdict is not imported. |
| neighbor-ethanolamine_degradation_polyhedral_organelle | data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml; Complete frozen BMC/carboxysome/shell/Eut boundary neighbor | context_only | Frozen neighboring record read for class, family and boundary context; its scientific verdict is not imported. |
| micro42-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015977,GO:0031469,GO:0031470,GO:0031471,GO:0043232,GO:0046336; Exact six requested native entries; GO0031469/GO0043232 names/definitions/typed children and obsolescence fields. | supports | GO0031469 is an active protein-coated metabolic organelle, an is_a child of GO0043232; carboxysome and Eut are explicit is_a children. Metabolosome is the catabolic subset in the review; the exact acronym synonym remains a source-backed local synonym. |
| micro42-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro42-tax502025 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/502025; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 502025 identifies Haliangium ochraceum DSM 14365 at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro42-doi2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/nrmicro.2018.10%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED29503457: Bacterial microcompartments. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/s41467-021-24126-4%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED34155212: A catalog of the diversity and ubiquity of bacterial microcompartments. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi7 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126/science.aan3289%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED28642439: Assembly principles and structure of a 6.5-MDa bacterial microcompartment shell. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-doi1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016/j.str.2019.01.017%22&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED30833088: The Plasticity of Molecular Interactions Governs Bacterial Microcompartment Shell Assembly. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro42-legacy-PMC6022854 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6022854/; Genuine full HTML; independently read Introduction P1–6, shell/assembly/functional-diversity P47–72 and their main captions; timeline P8–46. Secondary synthesis, not a newly performed experiment. | supports | The secondary review supports the H/T/P classes, metabolosome subset, heterogeneous core cargo and selective permeability. It distinguishes beta core-first assembly from alpha concomitant shell/core assembly and identifies PF03319/BMV as the generic BMC-P protein family. Essential diffusive closure is distinct from gross compartment formation. |
| micro42-legacy-PMC5873307 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5873307/; Genuine author manuscript HTML; entire main P1–14 and Fig1–4 captions. Supplementary Methods/data and figure pixels were not inspected. | supports | The primary study resolves recombinant H. ochraceum-derived 6.5-MDa shells: H hexamers, T pseudohexamers and P pentamers. Mixed T densities and modelled permeability/cargo capacity are explicitly distinguished from direct measurements of physiological flux or native enzyme cargo. |
| micro42-body-PMC6506404 | https://pmc.ncbi.nlm.nih.gov/articles/6506404/; Genuine primary HTML; Introduction P6–10, Results P11–23/P25–26, Discussion P27–31 and Methods P33–38; associated main captions through Fig8. P24 had a truncated extraction and is not relied upon. No supplementary-data or raw-pixel reanalysis. | supports | Cryo-EM resolves recombinant HO shell H/T/P interactions and structural populations. Open/intermediate T-pore states support a proposed airlock-like route; actual gating/solute flux and dynamic interconversion were not directly established. Generic structural statements in the record remain compatible with those qualifications. |
| micro42-legacy-PMC8217296 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8217296/; Genuine primary HTML; complete abstract/Introduction Par1–6, Results Par7–10 and Fig1–4 captions; no new genome-census computation. | supports | The primary genomic catalog identifies conserved shell folds with neighboring signature enzymes and auxiliary genes, and widespread but uneven BMC loci. It supports VARIABLE bacterial occurrence; genomic locus detection is not direct microscopy or expression evidence for each organism. |
| micro42-PF03319 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF03319/; metadata accession/type/name/integrated/complete description; current native response. | supports | PF03319 is the EutN/CcmL BMV domain, integrated in IPR004992; its older hexamer discussion is not used to override the directly inspected pentamer/assembled-shell literature. |
| micro42-IPR004992 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004992/; Complete family identity/type/description and specified members; not a claim that every isolated homolog is constitutively pentameric. | supports | IPR004992 is a protein family encompassing EutN, CcmL, CsoS4A/B, PduN and BMC homologs. This breadth fits the generic BMC-P protein cohort, unlike narrower carboxysome- or Eut-only cohorts. Its older oligomer discussion is superseded for this assessment by direct BMC-P studies. |
| micro42-PF00936 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00936/; metadata accession/type/name/integrated/description. | supports | The native BMC domain is shared among different BMC shell architectures. A domain that occurs once or in tandem does not alone identify the exact H or T architectural class. |
| schema-result | just validate data/structures/microcompartment/bacterial_microcompartment.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/microcompartment/bacterial_microcompartment.yaml |
| strict-result | just validate-strict data/structures/microcompartment/bacterial_microcompartment.yaml --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/bacterial_microcompartment-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/microcompartment/bacterial_microcompartment.yaml --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/bacterial_microcompartment-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch42-20261022-q4522lvm/bacterial_microcompartment-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/bacterial_microcompartment.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/bacterial_microcompartment.yaml; Complete read-only focused native graphs log | supports | data/structures/microcompartment/bacterial_microcompartment.yaml  (GO:0031469)<br>  protein_shell_encapsulation	bmc_h_facet_shell_proteins	NO_GENE_SYMBOLS	-&gt;bmc_h_facet_shell_proteins (PROTEIN: BMC-H facet shell proteins)<br>  protein_shell_encapsulation	bmc_t_gated_shell_proteins	NO_GENE_SYMBOLS	-&gt;bmc_t_gated_shell_proteins (PROTEIN: BMC-T gated shell proteins)<br>  protein_shell_encapsulation	bmc_p_vertex_shell_proteins	NO_GENE_SYMBOLS	-&gt;bmc_p_vertex_shell_proteins (PROTEIN: BMC-P vertex shell proteins)<br>  protein_shell_encapsulation	enzyme_cargo	NO_GENE_SYMBOLS	-&gt;encapsulated_lumen_enzyme_cargo (PROTEIN: encapsulated lumen enzyme cargo)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/microcompartment/bacterial_microcompartment.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 8 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- The Sutter2017/Greber2019 particles are recombinant HO-derived shells; physiological native cargo, flux rates and universal dynamic gating are not demonstrated. Source-body reading is limited to the exact paragraphs/captions listed, with no supplementary-data or raw-image reanalysis.
- The genomic catalog supports potential locus distributions rather than observed organelles in every genome. Conditional formation labels do not establish individual-protein necessity in every BMC.
- Native PF03319/IPR004992 descriptions retain older EutN hexamer statements; those are not used as current oligomeric proof. Exact H/T architecture cannot be inferred solely from a shared domain.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these protein-shell identity, assembly and compartmentalized-enzyme claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T041112Z-bacterial-microcompartment-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of bacterial microcompartment
started_at: '2026-10-22T03:46:56Z'
finished_at: '2026-10-22T04:11:12Z'
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
summary: One minor correction resolves the generic BMC-P protein-family grounding;
  the class, coarse composition, distribution and source-qualified shell model are
  supported.
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
  - path: data/structures/microcompartment/bacterial_microcompartment.yaml
    sha256: 744baee4509a2d6c59e951bf107ec3730a2576b7c084d239569913389b1a3321
    role: target
  - path: data/structures/microcompartment/carboxysome.yaml
    sha256: cdb55020f01fc187a13bdecb69c982a747dfb27fd2fa2e341c288a0cb56bdcd6
    role: context
  - path: data/structures/microcompartment/carboxysome_shell.yaml
    sha256: a732afb9239cc57b69ff7d4ca75700b4f2b3fb682837b1be799376d12acb7762
    role: context
  - path: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
    sha256: 67b4280a4ef1837e40fe65ac0ed67e263b95339d1b364a976ee1110c2440029f
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
- target_id: GO:0031469
  path: data/structures/microcompartment/bacterial_microcompartment.yaml
  label: bacterial microcompartment
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/bacterial_microcompartment.yaml
    role: maintained scientific record
scope:
  description: One complete target, with the other three BMC/carboxysome/shell/Eut
    records frozen as boundary context. Exact authority, all current component/function/graph/source
    placements, taxonomic scope, formation semantics, history and discussions were
    reviewed.
  selection: Batch42 fixed strict path order, index 6; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031469
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031469
  command: just validate data/structures/microcompartment/bacterial_microcompartment.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031469
  command: just validate-strict data/structures/microcompartment/bacterial_microcompartment.yaml
    --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/bacterial_microcompartment-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - GO:0031469
  command: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/bacterial_microcompartment.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-proteins
- check_id: native-graphs
  name: Focused native graphs
  status: passed
  required: true
  target_ids:
  - GO:0031469
  command: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/bacterial_microcompartment.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0031469
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - neighbor-carboxysome
  - neighbor-carboxysome_shell
  - neighbor-ethanolamine_degradation_polyhedral_organelle
  - micro42-go
  - micro42-tax2
  - micro42-tax502025
  - micro42-doi2
  - micro42-doi4
  - micro42-doi7
  - micro42-doi1
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC5873307
  - micro42-body-PMC6506404
  - micro42-legacy-PMC8217296
  - micro42-PF03319
  - micro42-IPR004992
  - micro42-PF00936
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031469
  summary: 8 of 8 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031469
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0031469
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0031469
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0031469
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0031469
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
    and current batch42 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/microcompartment/bacterial_microcompartment.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T03:54:47Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T03:54:47Z'
  support: context_only
  summary: Protein-family identity is distinct from an assembled complex. ESSENTIAL
    concerns failure of structure formation, not loss of catalytic function or ambient-CO2
    growth.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T03:54:47Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: neighbor-carboxysome
  kind: record_content
  reference: data/structures/microcompartment/carboxysome.yaml
  locator: Complete frozen BMC/carboxysome/shell/Eut boundary neighbor
  accessed_at: '2026-10-22T03:54:47Z'
  support: context_only
  summary: Frozen neighboring record read for class, family and boundary context;
    its scientific verdict is not imported.
- evidence_id: neighbor-carboxysome_shell
  kind: record_content
  reference: data/structures/microcompartment/carboxysome_shell.yaml
  locator: Complete frozen BMC/carboxysome/shell/Eut boundary neighbor
  accessed_at: '2026-10-22T03:54:47Z'
  support: context_only
  summary: Frozen neighboring record read for class, family and boundary context;
    its scientific verdict is not imported.
- evidence_id: neighbor-ethanolamine_degradation_polyhedral_organelle
  kind: record_content
  reference: data/structures/microcompartment/ethanolamine_degradation_polyhedral_organelle.yaml
  locator: Complete frozen BMC/carboxysome/shell/Eut boundary neighbor
  accessed_at: '2026-10-22T03:54:47Z'
  support: context_only
  summary: Frozen neighboring record read for class, family and boundary context;
    its scientific verdict is not imported.
- evidence_id: micro42-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015977,GO:0031469,GO:0031470,GO:0031471,GO:0043232,GO:0046336
  locator: Exact six requested native entries; GO0031469/GO0043232 names/definitions/typed
    children and obsolescence fields.
  accessed_at: '2026-10-22T03:50:27.488533Z'
  support: supports
  summary: GO0031469 is an active protein-coated metabolic organelle, an is_a child
    of GO0043232; carboxysome and Eut are explicit is_a children. Metabolosome is
    the catabolic subset in the review; the exact acronym synonym remains a source-backed
    local synonym.
  snapshot_sha256: 7d520adef79917ad67a8d84c30d00d98c1bd17c20957615036f09416a50f15a1
- evidence_id: micro42-tax2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:49:53.043115Z'
  support: supports
  summary: ENA taxId 2 identifies Bacteria at rank domain; aliases and lineage match
    the record. Identity alone is not prevalence or experimental-condition evidence.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: micro42-tax502025
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/502025
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:49:53.047393Z'
  support: supports
  summary: ENA taxId 502025 identifies Haliangium ochraceum DSM 14365 at rank strain;
    aliases and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: d3d41a358362c58a080416c6810177956883830ebbb373013bde60cdc91aee98
- evidence_id: micro42-doi2
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/nrmicro.2018.10%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:44.622347Z'
  support: supports
  summary: 'Unique MED29503457: Bacterial microcompartments. Authors/year/DOI and
    the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 2a201c7ad09e400058b0e169914d5d0b828ef4af6d8ec642fcb41e1d373b42e6
- evidence_id: micro42-doi4
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/s41467-021-24126-4%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:44.657511Z'
  support: supports
  summary: 'Unique MED34155212: A catalog of the diversity and ubiquity of bacterial
    microcompartments. Authors/year/DOI and the complete native abstract were inspected.
    This row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 4ef9237d799acf8c34a54a2ad911d8c1355d6d6949d0cb18e0d8aa61cce9b9f7
- evidence_id: micro42-doi7
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126/science.aan3289%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:45.401318Z'
  support: supports
  summary: 'Unique MED28642439: Assembly principles and structure of a 6.5-MDa bacterial
    microcompartment shell. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 260aeae9ad4015902da46b0e4269c7b5cb3ca79ccfef5902bedd860ac9a4faf0
- evidence_id: micro42-doi1
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016/j.str.2019.01.017%22&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T03:49:44.593290Z'
  support: supports
  summary: 'Unique MED30833088: The Plasticity of Molecular Interactions Governs Bacterial
    Microcompartment Shell Assembly. Authors/year/DOI and the complete native abstract
    were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 28d57c9a92f0f05bc7e538f233c24ceee017215be6b14dfd9daae11c135e81b9
- evidence_id: micro42-legacy-PMC6022854
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6022854/
  locator: Genuine full HTML; independently read Introduction P1–6, shell/assembly/functional-diversity
    P47–72 and their main captions; timeline P8–46. Secondary synthesis, not a newly
    performed experiment.
  accessed_at: '2026-10-22T03:50:50.533150Z'
  support: supports
  summary: The secondary review supports the H/T/P classes, metabolosome subset, heterogeneous
    core cargo and selective permeability. It distinguishes beta core-first assembly
    from alpha concomitant shell/core assembly and identifies PF03319/BMV as the generic
    BMC-P protein family. Essential diffusive closure is distinct from gross compartment
    formation.
  snapshot_sha256: 4d4c6458a485c328fdf9f64c005c464dbcb2c9866cd8236374995ece391db05d
- evidence_id: micro42-legacy-PMC5873307
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5873307/
  locator: Genuine author manuscript HTML; entire main P1–14 and Fig1–4 captions.
    Supplementary Methods/data and figure pixels were not inspected.
  accessed_at: '2026-10-22T03:50:50.628734Z'
  support: supports
  summary: 'The primary study resolves recombinant H. ochraceum-derived 6.5-MDa shells:
    H hexamers, T pseudohexamers and P pentamers. Mixed T densities and modelled permeability/cargo
    capacity are explicitly distinguished from direct measurements of physiological
    flux or native enzyme cargo.'
  snapshot_sha256: 81af31db44d85694e3d5b9260a25e7f472cd254f3a6b116e90f7d4681f05df61
- evidence_id: micro42-body-PMC6506404
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/6506404/
  locator: Genuine primary HTML; Introduction P6–10, Results P11–23/P25–26, Discussion
    P27–31 and Methods P33–38; associated main captions through Fig8. P24 had a truncated
    extraction and is not relied upon. No supplementary-data or raw-pixel reanalysis.
  accessed_at: '2026-10-22T03:50:10.259719Z'
  support: supports
  summary: Cryo-EM resolves recombinant HO shell H/T/P interactions and structural
    populations. Open/intermediate T-pore states support a proposed airlock-like route;
    actual gating/solute flux and dynamic interconversion were not directly established.
    Generic structural statements in the record remain compatible with those qualifications.
  snapshot_sha256: dcf84491c39d208c097747c19344593f5261b97e1541213e6fa9d991edfd86f2
- evidence_id: micro42-legacy-PMC8217296
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8217296/
  locator: Genuine primary HTML; complete abstract/Introduction Par1–6, Results Par7–10
    and Fig1–4 captions; no new genome-census computation.
  accessed_at: '2026-10-22T03:50:50.267128Z'
  support: supports
  summary: The primary genomic catalog identifies conserved shell folds with neighboring
    signature enzymes and auxiliary genes, and widespread but uneven BMC loci. It
    supports VARIABLE bacterial occurrence; genomic locus detection is not direct
    microscopy or expression evidence for each organism.
  snapshot_sha256: 3e1fe21fcf3ef391a378e1db66831851b09ac1e77e9c0483891831304e36b8f9
- evidence_id: micro42-PF03319
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF03319/
  locator: metadata accession/type/name/integrated/complete description; current native
    response.
  accessed_at: '2026-10-22T03:50:11.940521Z'
  support: supports
  summary: PF03319 is the EutN/CcmL BMV domain, integrated in IPR004992; its older
    hexamer discussion is not used to override the directly inspected pentamer/assembled-shell
    literature.
  snapshot_sha256: ad23273fdf50fc94344313209a5b93f784650f2cc77658c99ccae660b546c569
- evidence_id: micro42-IPR004992
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004992/
  locator: Complete family identity/type/description and specified members; not a
    claim that every isolated homolog is constitutively pentameric.
  accessed_at: '2026-10-22T03:49:54.003619Z'
  support: supports
  summary: IPR004992 is a protein family encompassing EutN, CcmL, CsoS4A/B, PduN and
    BMC homologs. This breadth fits the generic BMC-P protein cohort, unlike narrower
    carboxysome- or Eut-only cohorts. Its older oligomer discussion is superseded
    for this assessment by direct BMC-P studies.
  snapshot_sha256: e74c5aa30d022cec998d439ed5406764b62db0f8572dbda2a505255421d76c88
- evidence_id: micro42-PF00936
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00936/
  locator: metadata accession/type/name/integrated/description.
  accessed_at: '2026-10-22T03:50:12.001189Z'
  support: supports
  summary: The native BMC domain is shared among different BMC shell architectures.
    A domain that occurs once or in tandem does not alone identify the exact H or
    T architectural class.
  snapshot_sha256: 88a3c70d733d57424d141f6922140d963d8b905db3c6195b6ff0966a5174aca5
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/microcompartment/bacterial_microcompartment.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:46:57Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/microcompartment/bacterial_microcompartment.yaml'
  snapshot_sha256: 398757ac814232ea4d09d3aee5f62b1ffa20b50a5bdd0bb6a9a87015fd712118
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/microcompartment/bacterial_microcompartment.yaml
    --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/bacterial_microcompartment-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:46:58Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/microcompartment/bacterial_microcompartment.yaml\
    \ --out /private/tmp/cellstructure-batch42-20261022-q4522lvm/bacterial_microcompartment-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch42-20261022-q4522lvm/bacterial_microcompartment-strict.tsv"
  snapshot_sha256: a424321f5955ff5d2d0e13e10eb4ffeb91dd46031f319afbd2a9ef750c794dda
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/microcompartment/bacterial_microcompartment.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T03:50:27.461337Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch42-20261022-q4522lvm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/microcompartment/bacterial_microcompartment.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T03:50:28.107337Z'
  support: supports
  summary: "data/structures/microcompartment/bacterial_microcompartment.yaml  (GO:0031469)\n\
    \  protein_shell_encapsulation\tbmc_h_facet_shell_proteins\tNO_GENE_SYMBOLS\t\
    ->bmc_h_facet_shell_proteins (PROTEIN: BMC-H facet shell proteins)\n  protein_shell_encapsulation\t\
    bmc_t_gated_shell_proteins\tNO_GENE_SYMBOLS\t->bmc_t_gated_shell_proteins (PROTEIN:\
    \ BMC-T gated shell proteins)\n  protein_shell_encapsulation\tbmc_p_vertex_shell_proteins\t\
    NO_GENE_SYMBOLS\t->bmc_p_vertex_shell_proteins (PROTEIN: BMC-P vertex shell proteins)\n\
    \  protein_shell_encapsulation\tenzyme_cargo\tNO_GENE_SYMBOLS\t->encapsulated_lumen_enzyme_cargo\
    \ (PROTEIN: encapsulated lumen enzyme cargo)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     4  NO_GENE_SYMBOLS           component_ref target declares\
    \ no gene_symbols and holds no protein_examples\n     0  COVERED             \
    \      component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     4  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 9dfa9e7fa8f3ea3f9a69302205945d5357a9b0288271a806e6b9b6641f9460fe
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/microcompartment/bacterial_microcompartment.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 8 of 8 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
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
  topic: Exact class and subtype boundaries
  outcome: supported
  target_ids:
  - GO:0031469
  summary: The bacterial protein-shelled organelle identity, membraneless parent and
    catabolic metabolosome subset are supported. The local carboxysome and Eut siblings
    preserve their specialized chemistry.
  evidence_ids:
  - record
  - micro42-go
  - micro42-legacy-PMC6022854
- assessment_id: composition
  area: grounding
  topic: Supported H/T/P and cargo classes
  outcome: concern
  target_ids:
  - GO:0031469
  summary: The four coarse component classes accurately cover shell building blocks
    and heterogeneous enzyme cargo. H/T/cargo label-only boundaries are justified
    by architecture and metabolic heterogeneity; P-family withholding instead uses
    an assembled-vertex requirement on a PROTEIN row.
  evidence_ids:
  - record
  - curation
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC5873307
  - micro42-body-PMC6506404
  - micro42-PF03319
  - micro42-IPR004992
  - micro42-PF00936
- assessment_id: necessity
  area: grounding
  topic: Formation labels remain condition dependent
  outcome: unknown
  target_ids:
  - GO:0031469
  summary: H is a constitutional major facet class in characterized shells; T/P and
    native cargo requirements vary by BMC and recombinant construct. CONDITIONAL does
    not identify every particular deletion condition. No formation necessity of every
    individual T/P protein is inferred from intact-shell structure alone.
  evidence_ids:
  - record
  - schema
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC5873307
  - micro42-body-PMC6506404
- assessment_id: scope
  area: scope
  topic: Distribution and recombinant canonical example
  outcome: supported
  target_ids:
  - GO:0031469
  summary: Native taxon identities are correct. The canonical HO note accurately identifies
    the shell used for structural work, not a directly isolated native enzyme-loaded
    organelle. The protein set was recombinantly expressed; VARIABLE Bacteria is supported
    by the catalog rather than a universal prevalence claim.
  evidence_ids:
  - record
  - micro42-legacy-PMC5873307
  - micro42-legacy-PMC8217296
  - micro42-tax2
  - micro42-tax502025
- assessment_id: functions
  area: evidence
  topic: Encapsulation and selective-permeability evidence
  outcome: supported
  target_ids:
  - GO:0031469
  summary: Segregation/retention and pore-based exchange are supported at the synthesis/model
    level. The Greber evidence note explicitly calls its permeability route modelled;
    no direct rate or physiological substrate specificity is asserted.
  evidence_ids:
  - record
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC5873307
  - micro42-body-PMC6506404
- assessment_id: graph
  area: graph
  topic: Directed shell construction and metabolic coupling
  outcome: supported
  target_ids:
  - GO:0031469
  summary: Every H/T/P assembly and cargo/exchange edge is compatible with the source-supported
    model. A mechanistic coarse graph is appropriate; it does not force identical
    pore composition or a demonstrated native HO metabolic pathway. Generic protein
    actor nodes do not require invented strain-specific instances.
  evidence_ids:
  - record
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC5873307
  - micro42-body-PMC6506404
  - micro42-legacy-PMC8217296
- assessment_id: coverage
  area: completeness
  topic: Full record and bounded enrichments
  outcome: supported
  target_ids:
  - GO:0031469
  summary: All current and historical fields were read. No images, verbatim snippets
    or protein examples occur in this target. Optional inventories and unavailable
    exact H/T architectural families do not become automatic findings. The verified
    generic BMC-P family is a concrete resolvable grounding gap.
  evidence_ids:
  - record
  - micro42-go
  - micro42-legacy-PMC6022854
  - micro42-PF03319
  - micro42-IPR004992
  - micro42-PF00936
findings:
- finding_id: F1
  issue_key: bacterial-microcompartment-bmc-p-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the generic BMC-P protein cohort to its verified family
  description: The PROTEIN component deliberately withholds grounding because PF03319
    does not denote an assembled lineage-neutral vertex. This record models the generic
    BMC-P proteins, for which IPR004992 supplies the verified family across carboxysomes
    and metabolosomes; assembly geometry belongs in the role/evidence.
  target_ids:
  - GO:0031469
  field_paths:
  - components[2].grounding_status
  - components[2].grounding_notes
  - components[2].grounding
  evidence_ids:
  - record
  - curation
  - micro42-PF03319
  - micro42-IPR004992
  - micro42-legacy-PMC6022854
  - micro42-legacy-PMC5873307
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/bacterial_microcompartment.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: The biological class and role are sound; the issue is a bounded,
    now-resolvable protein-family grounding gap rather than an incorrect assembled-complex
    identity.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0031469
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/bacterial_microcompartment.yaml
    role: maintained scientific record
  description: In separately authorized curation, ground the generic BMC-P protein
    component to the verified family and retain explicit pentamer/vertex role qualifications.
    Do not export the same broad family as an exact carboxysome-only or EutN-only
    identity.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
limitations:
- The Sutter2017/Greber2019 particles are recombinant HO-derived shells; physiological
  native cargo, flux rates and universal dynamic gating are not demonstrated. Source-body
  reading is limited to the exact paragraphs/captions listed, with no supplementary-data
  or raw-image reanalysis.
- The genomic catalog supports potential locus distributions rather than observed
  organelles in every genome. Conditional formation labels do not establish individual-protein
  necessity in every BMC.
- Native PF03319/IPR004992 descriptions retain older EutN hexamer statements; those
  are not used as current oligomeric proof. Exact H/T architecture cannot be inferred
  solely from a shared domain.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these protein-shell identity, assembly and compartmentalized-enzyme
  claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
