# Spindle microtubule identity and source-scope review

- Review: 20261021T082245Z-spindle-microtubule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:09:15Z
- Finished UTC: 2026-10-21T08:22:45Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Identity, hierarchy, tubulin examples and bounded spindle architecture are supported. Citation tiers and presumptive attachment evidence remain explicit; no concrete curation defect was established.

## Scope And Provenance

Entire target; all native identifier, protein and taxon claims; relevant primary ultrastructural and annotation-source sections; cited live-imaging abstract and secondary SPB review.

Selection: Sixth unreviewed path in batch eleven, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005876 | data/structures/cytoskeleton/spindle_microtubule.yaml | maintained | spindle microtubule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005876 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005876 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0005876 | 15 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Native UniProt causal-graphs | passed | True | GO:0005876 | Native read-only target check passed. |
| Native UniProt verify | passed | True | GO:0005876 | Native read-only target check passed. |
| Expression-module applicability | not_applicable | False | GO:0005876 | Filament architecture and chromosome segregation do not assert an expression-module mechanism. |
| Claim-level scientific review | passed | True | GO:0005876 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0005876 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005876 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005876 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005876 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0005876 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Filament identity and ontology relations

identity: supported. Targets: GO:0005876.

The exact identity, FILAMENT kind, microtubule is-a parent and enclosing-spindle parthood match native GO. Spindle pole bodies and kinetochores remain adjacent independent structures.

### Alpha/beta lattice material and exact examples

grounding: supported. Targets: GO:0005876.

The combined alpha/beta component is appropriate filament material; gamma-tubulin nucleators, motors and attachment complexes are not silently included as lattice constituents. All three example identities are verified separately from membership evidence. ESSENTIAL describes collective polymer material, not individual TUB3 viability.

### Combined component grounding boundary

completeness: supported. Targets: GO:0005876.

No exact source-neutral family for this combined spindle alpha/beta constituent set is established by this review. A future split into alpha and beta families is optional enrichment; the current combined label is not equated to a broader family that also includes other tubulins.

### Native annotation citations versus structural membership

provenance: supported. Targets: GO:0005876.

TUB1 and TUB2 experimental citations match UniProt cytoskeleton annotations. The human-disease paper includes yeast experiments, so its title is not a taxon mismatch. Neither identity-only example roles nor the record promote its astral-microtubule assay into spindle membership proof.

### Species, strain and study design

scope: supported. Targets: GO:0005876.

Species-level budding-yeast scope is supported by the S288c and related diploid reconstructions. Reference-strain protein examples keep taxon559292 rather than replacing it with4932. COMMON is qualitative occurrence, not a prevalence measurement.

### Chromosome movement and architecture

evidence: supported. Targets: GO:0005876.

The abstract of Straight1997 directly supports the stated live imaging, GFP-Tub1 and chromosome movement claims. Winey1995 supports reconstruction, not live dynamics. Presumptive kinetochore classes are not direct visualization of every attachment.

### Four bounded nonmechanistic relationships

representation: supported. Targets: GO:0005876.

The polymerization, SPB anchoring, mitotic-spindle parthood and subset kinetochore-attachment edges agree with the source tiers. The graph is a mitotic exemplar within a broader mitotic/meiotic term, not a claim that all GO0005876 instances are mitotic or attach to kinetochores.

### Bounded MAP inventory and primary access

completeness: supported. Targets: GO:0005876.

The explicit optional MAP/motor expansion remains open. No image, complete molecular inventory or quantitative dynamic mechanism is asserted. The source access limits do not invalidate the narrowly stated claims supported by the available abstract and separate full primary reconstruction.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| spindle-mt-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776,GO:0005816,GO:0005819,GO:0005874,GO:0005876,GO:0007059,GO:0072686; All seven active definitions; GO0005874 and GO0005819 child relations | supports | Native active GO terms confirm GO0005876, its direct microtubule parent and spindle parthood, mitotic-spindle specialization, and the separate spindle-pole-body/kinetochore structures and segregation process. |
| spindle-mt-prep-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName and rank | supports | Species4932 is Saccharomyces cerevisiae. |
| spindle-mt-prep-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId, scientificName and lineage | supports | Taxon559292 names Saccharomyces cerevisiae S288C, the reference-strain taxon paired with all three protein examples. |
| spindle-mt-prep-winey-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.129.6.1601; Single DOI result title/authors/DOI/PMID/PMCID | supports | Winey et al.1995 exact DOI resolves to PMID7790357/PMC2291174, on three-dimensional budding-yeast spindle ultrastructure. |
| spindle-mt-prep-winey-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2291174.1/PMC2291174.1.pdf; Printedpp1602-1605 Methods/reconstructions; p1609 noncore classification; pp1611-1614 interpretation limits, read by independent source-review agent | supports | Serial-section reconstructions distinguish core/interpolar and presumptive kinetochore microtubules in S288c and a related diploid. Kinetochores were not directly visualized; inferred polarity and limited-resolution continuous categories remain qualified. |
| spindle-mt-prep-straight-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1126/science.277.5325.574; Single DOI result bibliographic identity and complete abstract | supports | The exact1997 Science paper PMID9228009 describes GFP-Tub1 spindle imaging and Lac-repressor-labelled loci in living budding yeast, chromosome movement and biphasic spindle elongation. Access was limited to its full abstract. |
| spindle-mt-prep-P09733 | https://rest.uniprot.org/uniprotkb/P09733.json; Primary accession, entryType, recommended protein name, gene tokens, organism and SUBCELLULAR LOCATION comments | supports | P09733 is the primary reviewed Tubulin alpha-1 chain entry for TUB1 in taxon559292. The cytoplasmic-cytoskeleton annotation carries ECO0000269 and PMID11739794. |
| spindle-mt-prep-query-TUB1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete result count and returned entry identity | supports | The exact reviewed-symbol query returned one entry, P09733, whose own gene tokens match TUB1. |
| spindle-mt-prep-P02557 | https://rest.uniprot.org/uniprotkb/P02557.json; Primary accession, entryType, recommended protein name, gene tokens, organism and SUBCELLULAR LOCATION comments | supports | P02557 is the primary reviewed Tubulin beta chain entry for TUB2 in taxon559292. The cytoplasmic-cytoskeleton annotation carries ECO0000269 and PMID23001566. |
| spindle-mt-prep-query-TUB2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete result count and returned entry identity | supports | The exact reviewed-symbol query returned one entry, P02557, whose own gene tokens match TUB2. |
| spindle-mt-prep-P09734 | https://rest.uniprot.org/uniprotkb/P09734.json; Primary accession, entryType, recommended protein name, gene tokens, organism and SUBCELLULAR LOCATION comments | supports | P09734 is the primary reviewed Tubulin alpha-3 chain entry for TUB3 in taxon559292. The record correctly uses identity-only entry evidence; no experimental localisation citation is supplied in that field. |
| spindle-mt-prep-query-TUB3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete result count and returned entry identity | supports | The exact reviewed-symbol query returned one entry, P09734, whose own gene tokens match TUB3. |
| spindle-mt-prep-anders-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11739794%20AND%20SRC%3AMED; Exact PMID record title, DOI and authors | supports | PMID11739794 resolves to Anders et al.2001, on dominant-lethal alpha-tubulin mutants in yeast. |
| spindle-mt-prep-cederquist-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A23001566%20AND%20SRC%3AMED; Exact PMID bibliographic record | supports | PMID23001566 resolves to Cederquist et al.2012, on TUBB2B mutation and axon dysinnervation; the study also contains direct yeast Tub2 experiments. |
| spindle-mt-agent-anders2001 | https://pmc.ncbi.nlm.nih.gov/articles/PMC60769/?report=xml; PMC60769 sections5,8,11-13 and Fig4B description; independently read source-review agent | supports | Selected yeast experiments image induced GFP::Tub1-828 incorporation into nuclear spindle and cytoplasmic microtubules. This substantiates the annotation context, with mutant/overexpression limits. |
| spindle-mt-agent-cederquist2012 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3516133/?report=xml; PMC3516133 Results s2h/s2i; Methods s4g/s4i/s4j; independently read source-review agent | supports | Yeast Tub2E421K experiments examine G1 astral microtubule dynamics and Kip3/Kip2 localisation. They support the cytoskeleton annotation provenance, not a direct spindle-localisation assay. |
| jaspersen-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscriptpp5-10, browserlines187-427; serialized browser text, not a native HTTP-body receipt | supports | The2004 literature review distinguishes SPB plaques, with nuclear microtubules at the inner plaque and cytoplasmic microtubules at the outer plaque. This is a secondary review; original capture time and exact snapshot hash are retained. |
| jaspersen-nucleation-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscriptpp24-26, browserlines978-1073; serialized browser text, not a native HTTP-body receipt | supports | The literature review describes SPB-associated nucleation from alpha/beta dimers and nuclear spindle formation. Gamma-tubulin nucleation factors are distinct from the alpha/beta lattice material. This is a secondary review; original capture time and exact snapshot hash are retained. |
| record | data/structures/cytoskeleton/spindle_microtubule.yaml; Entire maintained YAML including3protein examples,4graph edges,history anddiscussions | context_only | The generic target covers mitotic or meiotic spindle microtubules; the nonmechanistic architecture graph is explicitly a budding-yeast mitotic example. Its attachment edge is restricted to a subset and its evidence notes say presumptive kinetochore microtubules. |
| schema-result | just validate data/structures/cytoskeleton/spindle_microtubule.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/spindle_microtubule.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/spindle_microtubule.yaml --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_microtubule-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/spindle_microtubule.yaml --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_microtubule-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_microtubule-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/spindle_microtubule.yaml; exact collect() scope; SHA256 identifies the entire original resolver TSV | supports | 15 of 17 collected target identifiers returned OK at the unchanged base. Residuals: PMID:11739794: UNREACHABLE; resolved by evidence spindle-mt-prep-anders-meta; PMID:23001566: UNREACHABLE; resolved by evidence spindle-mt-prep-cederquist-meta. Source-native identity checked separately. |
| native-causal-graphs | /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_microtubule.yaml --causal-graphs; Entire captured native output | supports | data/structures/cytoskeleton/spindle_microtubule.yaml  (GO:0005876)<br>  budding_yeast_spindle_microtubule_architecture	alpha_beta_tubulins	COVERED	-&gt;alpha_beta_tubulins (UniProtKB:P09733, UniProtKB:P02557, UniProtKB:P09734)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_microtubule.yaml --verify; Entire captured native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Straight1997 full text was not recovered: the publisher returned403, its institutional PDF link failed certificate hostname validation and browser retrieval returned502. Its complete abstract directly supports the claims used; detailed assays and figure pixels were not verified.
- Winey1995 used high-pressure freezing followed by substitution/resin serial-section microscopy, not live imaging or vitreous cryo-electron tomography. Kinetochores were not directly visualized and assignments remain presumptive.
- Jaspersen2004 is secondary synthesis retrieved as browser text. Original timestamps and hashes are retained; an inherited200 field is not treated as proof of native HTTP access.
- Anders2001 and Cederquist2012 selected yeast Results/Methods were read by the independent source-review agent. Complete studies, supplements, raw data and primary image pixels were not independently reanalysed.
- No exhaustive family inventory or MAP/motor census was performed. The combined alpha/beta component and optional expansion TODO are retained.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The explicit user goal requires persistence of each target, including qualified passes; findings were not invented to justify saving.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082245Z-spindle-microtubule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Spindle microtubule identity and source-scope review
started_at: '2026-10-21T08:09:15Z'
finished_at: '2026-10-21T08:22:45Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Identity, hierarchy, tubulin examples and bounded spindle architecture are
  supported. Citation tiers and presumptive attachment evidence remain explicit; no
  concrete curation defect was established.
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
  - path: data/structures/cytoskeleton/spindle_microtubule.yaml
    sha256: bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9
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
- target_id: GO:0005876
  path: data/structures/cytoskeleton/spindle_microtubule.yaml
  label: spindle microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_microtubule.yaml
    role: maintained scientific record
scope:
  description: Entire target; all native identifier, protein and taxon claims; relevant
    primary ultrastructural and annotation-source sections; cited live-imaging abstract
    and secondary SPB review.
  selection: Sixth unreviewed path in batch eleven, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005876
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: just validate data/structures/cytoskeleton/spindle_microtubule.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: just validate-strict data/structures/cytoskeleton/spindle_microtubule.yaml
    --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_microtubule-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0005876
  summary: 15 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - spindle-mt-prep-anders-meta
  - spindle-mt-prep-cederquist-meta
- check_id: native-causal-graphs
  name: Native UniProt causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_microtubule.yaml
    --causal-graphs
  exit_code: 0
  summary: Native read-only target check passed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_microtubule.yaml
    --verify
  exit_code: 0
  summary: Native read-only target check passed.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005876
  summary: Filament architecture and chromosome segregation do not assert an expression-module
    mechanism.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005876
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - spindle-mt-prep-go
  - spindle-mt-prep-tax-4932
  - spindle-mt-prep-tax-559292
  - spindle-mt-prep-winey-meta
  - spindle-mt-prep-winey-s3
  - spindle-mt-prep-straight-meta
  - spindle-mt-prep-P09733
  - spindle-mt-prep-query-TUB1
  - spindle-mt-prep-P02557
  - spindle-mt-prep-query-TUB2
  - spindle-mt-prep-P09734
  - spindle-mt-prep-query-TUB3
  - spindle-mt-prep-anders-meta
  - spindle-mt-prep-cederquist-meta
  - spindle-mt-agent-anders2001
  - spindle-mt-agent-cederquist2012
  - jaspersen-browser
  - jaspersen-nucleation-browser
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: spindle-mt-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776,GO:0005816,GO:0005819,GO:0005874,GO:0005876,GO:0007059,GO:0072686
  locator: All seven active definitions; GO0005874 and GO0005819 child relations
  accessed_at: '2026-10-21T08:13:09.735032Z'
  support: supports
  summary: Native active GO terms confirm GO0005876, its direct microtubule parent
    and spindle parthood, mitotic-spindle specialization, and the separate spindle-pole-body/kinetochore
    structures and segregation process.
  snapshot_sha256: 099e0c8241d476fc601a0c6627fdb424559378cc77635c64c57f949f695fa785
- evidence_id: spindle-mt-prep-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName and rank
  accessed_at: '2026-10-21T08:13:14.029080Z'
  support: supports
  summary: Species4932 is Saccharomyces cerevisiae.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: spindle-mt-prep-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId, scientificName and lineage
  accessed_at: '2026-10-21T08:13:14.285708Z'
  support: supports
  summary: Taxon559292 names Saccharomyces cerevisiae S288C, the reference-strain
    taxon paired with all three protein examples.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: spindle-mt-prep-winey-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.129.6.1601
  locator: Single DOI result title/authors/DOI/PMID/PMCID
  accessed_at: '2026-10-21T08:13:11.883148Z'
  support: supports
  summary: Winey et al.1995 exact DOI resolves to PMID7790357/PMC2291174, on three-dimensional
    budding-yeast spindle ultrastructure.
  snapshot_sha256: 5f72dc2bd259f645d3040a785ce2272074b4076ee1deee2820baa3ecc6a1b4bc
- evidence_id: spindle-mt-prep-winey-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2291174.1/PMC2291174.1.pdf
  locator: Printedpp1602-1605 Methods/reconstructions; p1609 noncore classification;
    pp1611-1614 interpretation limits, read by independent source-review agent
  accessed_at: '2026-10-21T08:13:17.273553Z'
  support: supports
  summary: Serial-section reconstructions distinguish core/interpolar and presumptive
    kinetochore microtubules in S288c and a related diploid. Kinetochores were not
    directly visualized; inferred polarity and limited-resolution continuous categories
    remain qualified.
  snapshot_sha256: b25472f54aa259fba263345f6665f398654801c4574c60673c242a2c1f96630c
- evidence_id: spindle-mt-prep-straight-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1126/science.277.5325.574
  locator: Single DOI result bibliographic identity and complete abstract
  accessed_at: '2026-10-21T08:13:12.702917Z'
  support: supports
  summary: The exact1997 Science paper PMID9228009 describes GFP-Tub1 spindle imaging
    and Lac-repressor-labelled loci in living budding yeast, chromosome movement and
    biphasic spindle elongation. Access was limited to its full abstract.
  snapshot_sha256: 20359fd5724bbec28de1b344568d2351d105528a0fc812c89f3208fb516173d7
- evidence_id: spindle-mt-prep-P09733
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09733.json
  locator: Primary accession, entryType, recommended protein name, gene tokens, organism
    and SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-21T08:13:14.287097Z'
  support: supports
  summary: P09733 is the primary reviewed Tubulin alpha-1 chain entry for TUB1 in
    taxon559292. The cytoplasmic-cytoskeleton annotation carries ECO0000269 and PMID11739794.
  snapshot_sha256: aed535980dd8ac2307085497de3917488ff4f5da0252812d09d17d17c739b426
- evidence_id: spindle-mt-prep-query-TUB1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete result count and returned entry identity
  accessed_at: '2026-10-21T08:13:15.782860Z'
  support: supports
  summary: The exact reviewed-symbol query returned one entry, P09733, whose own gene
    tokens match TUB1.
  snapshot_sha256: ab3ef6eb4aba30b014094695c817ac553dcd2c55c6f8feda6c32fae65e55e16c
- evidence_id: spindle-mt-prep-P02557
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P02557.json
  locator: Primary accession, entryType, recommended protein name, gene tokens, organism
    and SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-21T08:13:15.263588Z'
  support: supports
  summary: P02557 is the primary reviewed Tubulin beta chain entry for TUB2 in taxon559292.
    The cytoplasmic-cytoskeleton annotation carries ECO0000269 and PMID23001566.
  snapshot_sha256: d22cba0cfbb4aaa448114cc4356c81a4f7116a79ee7359a05b69dfd659d6b646
- evidence_id: spindle-mt-prep-query-TUB2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete result count and returned entry identity
  accessed_at: '2026-10-21T08:13:15.615716Z'
  support: supports
  summary: The exact reviewed-symbol query returned one entry, P02557, whose own gene
    tokens match TUB2.
  snapshot_sha256: 4d1049116e3e865676ca2a31ed8f01bdd757d3cad4b28b84933b5903876ea148
- evidence_id: spindle-mt-prep-P09734
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09734.json
  locator: Primary accession, entryType, recommended protein name, gene tokens, organism
    and SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-21T08:13:15.263897Z'
  support: supports
  summary: P09734 is the primary reviewed Tubulin alpha-3 chain entry for TUB3 in
    taxon559292. The record correctly uses identity-only entry evidence; no experimental
    localisation citation is supplied in that field.
  snapshot_sha256: 0a6865ddaa8955d9ccdc57056008255b39a4ab55d5b75e640a37a0206c197b67
- evidence_id: spindle-mt-prep-query-TUB3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete result count and returned entry identity
  accessed_at: '2026-10-21T08:13:15.526353Z'
  support: supports
  summary: The exact reviewed-symbol query returned one entry, P09734, whose own gene
    tokens match TUB3.
  snapshot_sha256: 1e154b62a419986ae1256476fa07411bfb9f6cc39e678a36cd482cc505e8e62e
- evidence_id: spindle-mt-prep-anders-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11739794%20AND%20SRC%3AMED
  locator: Exact PMID record title, DOI and authors
  accessed_at: '2026-10-21T08:13:13.113631Z'
  support: supports
  summary: PMID11739794 resolves to Anders et al.2001, on dominant-lethal alpha-tubulin
    mutants in yeast.
  snapshot_sha256: 09d880b0260ec19f9866a41868cb276dd1a1e6ee374c042df5ab39b5d2ee4b57
- evidence_id: spindle-mt-prep-cederquist-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A23001566%20AND%20SRC%3AMED
  locator: Exact PMID bibliographic record
  accessed_at: '2026-10-21T08:13:13.115528Z'
  support: supports
  summary: PMID23001566 resolves to Cederquist et al.2012, on TUBB2B mutation and
    axon dysinnervation; the study also contains direct yeast Tub2 experiments.
  snapshot_sha256: 11012dca34504a5eb2b11d689f0a93e4ce4338b23cc03fb67b1d2289c64726c1
- evidence_id: spindle-mt-agent-anders2001
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC60769/?report=xml
  locator: PMC60769 sections5,8,11-13 and Fig4B description; independently read source-review
    agent
  accessed_at: '2026-10-21T08:15:23.190725Z'
  support: supports
  summary: Selected yeast experiments image induced GFP::Tub1-828 incorporation into
    nuclear spindle and cytoplasmic microtubules. This substantiates the annotation
    context, with mutant/overexpression limits.
  snapshot_sha256: 20dccb8e9e57b87de542f2afb0be089c0d1c8da360f51621eaf436979e88ea44
- evidence_id: spindle-mt-agent-cederquist2012
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3516133/?report=xml
  locator: PMC3516133 Results s2h/s2i; Methods s4g/s4i/s4j; independently read source-review
    agent
  accessed_at: '2026-10-21T08:15:23.191157Z'
  support: supports
  summary: Yeast Tub2E421K experiments examine G1 astral microtubule dynamics and
    Kip3/Kip2 localisation. They support the cytoskeleton annotation provenance, not
    a direct spindle-localisation assay.
  snapshot_sha256: 3646d6a8902cf9bf9bd2815b614daa8850cf52ce46ec7c452a01ec53d7a4e393
- evidence_id: jaspersen-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Author-manuscriptpp5-10, browserlines187-427; serialized browser text,
    not a native HTTP-body receipt
  accessed_at: '2026-10-21T07:24:18Z'
  support: supports
  summary: The2004 literature review distinguishes SPB plaques, with nuclear microtubules
    at the inner plaque and cytoplasmic microtubules at the outer plaque. This is
    a secondary review; original capture time and exact snapshot hash are retained.
  snapshot_sha256: 8aa2398ded5512b2450c936e832c11bc46d77ac317e4c01a2f7a6b9f1a4fce4e
- evidence_id: jaspersen-nucleation-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Author-manuscriptpp24-26, browserlines978-1073; serialized browser text,
    not a native HTTP-body receipt
  accessed_at: '2026-10-21T07:43:49.372408Z'
  support: supports
  summary: The literature review describes SPB-associated nucleation from alpha/beta
    dimers and nuclear spindle formation. Gamma-tubulin nucleation factors are distinct
    from the alpha/beta lattice material. This is a secondary review; original capture
    time and exact snapshot hash are retained.
  snapshot_sha256: 5c038e01761413d522e0ea145ffefb28f289f6f2f5cc3b55c8deb377bf2aa0cf
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_microtubule.yaml
  locator: Entire maintained YAML including3protein examples,4graph edges,history
    anddiscussions
  accessed_at: '2026-10-21T08:20:07Z'
  support: context_only
  summary: The generic target covers mitotic or meiotic spindle microtubules; the
    nonmechanistic architecture graph is explicitly a budding-yeast mitotic example.
    Its attachment edge is restricted to a subset and its evidence notes say presumptive
    kinetochore microtubules.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/spindle_microtubule.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:09:18Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/spindle_microtubule.yaml'
  snapshot_sha256: 5c91fec2106059c0f825fafdb39bd2b5cea374bf9f525ddf4a877ca214753c0d
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/spindle_microtubule.yaml
    --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_microtubule-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:09:20Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/spindle_microtubule.yaml\
    \ --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_microtubule-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../spindle_microtubule-strict.tsv"
  snapshot_sha256: 27890b89161a2904d5aa5e250161e3444cbd18f95599b7e351f960c515cba499
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/spindle_microtubule.yaml; exact collect()
    scope; SHA256 identifies the entire original resolver TSV
  accessed_at: '2026-10-21T08:20:07Z'
  support: supports
  summary: '15 of 17 collected target identifiers returned OK at the unchanged base.
    Residuals: PMID:11739794: UNREACHABLE; resolved by evidence spindle-mt-prep-anders-meta;
    PMID:23001566: UNREACHABLE; resolved by evidence spindle-mt-prep-cederquist-meta.
    Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_microtubule.yaml
    --causal-graphs
  locator: Entire captured native output
  accessed_at: '2026-10-21T08:17:04.941898Z'
  support: supports
  summary: "data/structures/cytoskeleton/spindle_microtubule.yaml  (GO:0005876)\n\
    \  budding_yeast_spindle_microtubule_architecture\talpha_beta_tubulins\tCOVERED\t\
    ->alpha_beta_tubulins (UniProtKB:P09733, UniProtKB:P02557, UniProtKB:P09734)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     1\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 67350563edda29e1dbbc383c68be5a4cf106f132f9b0028d2dd7e01c5c2201bc
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_microtubule.yaml
    --verify
  locator: Entire captured native output
  accessed_at: '2026-10-21T08:17:08.615478Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
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
  topic: Filament identity and ontology relations
  outcome: supported
  target_ids:
  - GO:0005876
  summary: The exact identity, FILAMENT kind, microtubule is-a parent and enclosing-spindle
    parthood match native GO. Spindle pole bodies and kinetochores remain adjacent
    independent structures.
  evidence_ids:
  - spindle-mt-prep-go
  - record
- assessment_id: composition
  area: grounding
  topic: Alpha/beta lattice material and exact examples
  outcome: supported
  target_ids:
  - GO:0005876
  summary: The combined alpha/beta component is appropriate filament material; gamma-tubulin
    nucleators, motors and attachment complexes are not silently included as lattice
    constituents. All three example identities are verified separately from membership
    evidence. ESSENTIAL describes collective polymer material, not individual TUB3
    viability.
  evidence_ids:
  - spindle-mt-prep-P09733
  - spindle-mt-prep-query-TUB1
  - spindle-mt-prep-P02557
  - spindle-mt-prep-query-TUB2
  - spindle-mt-prep-P09734
  - spindle-mt-prep-query-TUB3
  - spindle-mt-prep-go
  - spindle-mt-prep-straight-meta
  - record
- assessment_id: family
  area: completeness
  topic: Combined component grounding boundary
  outcome: supported
  target_ids:
  - GO:0005876
  summary: No exact source-neutral family for this combined spindle alpha/beta constituent
    set is established by this review. A future split into alpha and beta families
    is optional enrichment; the current combined label is not equated to a broader
    family that also includes other tubulins.
  evidence_ids:
  - spindle-mt-prep-go
  - record
- assessment_id: protein-provenance
  area: provenance
  topic: Native annotation citations versus structural membership
  outcome: supported
  target_ids:
  - GO:0005876
  summary: TUB1 and TUB2 experimental citations match UniProt cytoskeleton annotations.
    The human-disease paper includes yeast experiments, so its title is not a taxon
    mismatch. Neither identity-only example roles nor the record promote its astral-microtubule
    assay into spindle membership proof.
  evidence_ids:
  - spindle-mt-prep-P09733
  - spindle-mt-prep-query-TUB1
  - spindle-mt-prep-P02557
  - spindle-mt-prep-query-TUB2
  - spindle-mt-prep-P09734
  - spindle-mt-prep-query-TUB3
  - spindle-mt-prep-anders-meta
  - spindle-mt-prep-cederquist-meta
  - spindle-mt-agent-anders2001
  - spindle-mt-agent-cederquist2012
  - record
- assessment_id: scope
  area: scope
  topic: Species, strain and study design
  outcome: supported
  target_ids:
  - GO:0005876
  summary: Species-level budding-yeast scope is supported by the S288c and related
    diploid reconstructions. Reference-strain protein examples keep taxon559292 rather
    than replacing it with4932. COMMON is qualitative occurrence, not a prevalence
    measurement.
  evidence_ids:
  - spindle-mt-prep-tax-4932
  - spindle-mt-prep-tax-559292
  - spindle-mt-prep-winey-s3
  - record
- assessment_id: function
  area: evidence
  topic: Chromosome movement and architecture
  outcome: supported
  target_ids:
  - GO:0005876
  summary: The abstract of Straight1997 directly supports the stated live imaging,
    GFP-Tub1 and chromosome movement claims. Winey1995 supports reconstruction, not
    live dynamics. Presumptive kinetochore classes are not direct visualization of
    every attachment.
  evidence_ids:
  - spindle-mt-prep-go
  - spindle-mt-prep-winey-s3
  - spindle-mt-prep-straight-meta
  - record
- assessment_id: graph
  area: representation
  topic: Four bounded nonmechanistic relationships
  outcome: supported
  target_ids:
  - GO:0005876
  summary: The polymerization, SPB anchoring, mitotic-spindle parthood and subset
    kinetochore-attachment edges agree with the source tiers. The graph is a mitotic
    exemplar within a broader mitotic/meiotic term, not a claim that all GO0005876
    instances are mitotic or attach to kinetochores.
  evidence_ids:
  - spindle-mt-prep-go
  - spindle-mt-prep-winey-s3
  - spindle-mt-prep-straight-meta
  - jaspersen-browser
  - jaspersen-nucleation-browser
  - record
- assessment_id: completeness
  area: completeness
  topic: Bounded MAP inventory and primary access
  outcome: supported
  target_ids:
  - GO:0005876
  summary: The explicit optional MAP/motor expansion remains open. No image, complete
    molecular inventory or quantitative dynamic mechanism is asserted. The source
    access limits do not invalidate the narrowly stated claims supported by the available
    abstract and separate full primary reconstruction.
  evidence_ids:
  - spindle-mt-prep-winey-s3
  - spindle-mt-prep-straight-meta
  - record
findings: []
actions: []
limitations:
- 'Straight1997 full text was not recovered: the publisher returned403, its institutional
  PDF link failed certificate hostname validation and browser retrieval returned502.
  Its complete abstract directly supports the claims used; detailed assays and figure
  pixels were not verified.'
- Winey1995 used high-pressure freezing followed by substitution/resin serial-section
  microscopy, not live imaging or vitreous cryo-electron tomography. Kinetochores
  were not directly visualized and assignments remain presumptive.
- Jaspersen2004 is secondary synthesis retrieved as browser text. Original timestamps
  and hashes are retained; an inherited200 field is not treated as proof of native
  HTTP access.
- Anders2001 and Cederquist2012 selected yeast Results/Methods were read by the independent
  source-review agent. Complete studies, supplements, raw data and primary image pixels
  were not independently reanalysed.
- No exhaustive family inventory or MAP/motor census was performed. The combined alpha/beta
  component and optional expansion TODO are retained.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The explicit user goal requires persistence of each target, including qualified
  passes; findings were not invented to justify saving.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
