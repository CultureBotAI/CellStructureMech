# Source-grounded review of Hda-beta clamp complex

- Review: 20261022T074157Z-hda-beta-clamp-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:12:35Z
- Finished UTC: 2026-10-22T07:41:57Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor finding resolves the Hda family mapping. Exact complex boundaries, DnaN substructure, reference proteins and the nonmechanistic RIDA function are supported.

## Scope And Provenance

Exactly one complete maintained target, with source-native and primary reading scopes declared individually.

Selection: One complete record in strict-path batch 57 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990085 | data/structures/other/hda_beta_clamp_complex.yaml | maintained | Hda-beta clamp complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990085 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990085 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:1990085 | Focused check passed; scientific claims assessed separately. |
| Native focused verify | passed | True | GO:1990085 | Focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:1990085 | No iModulon-specific claim is assessed; the relevant complex/assay evidence was inspected directly. |
| Claim-level scientific review | passed | True | GO:1990085 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990085 | 10 of 13 collected target identifiers returned OK. PMID:12618445: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:15150238: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:23994470: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990085 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990085 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990085 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990085 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990085 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Hda-beta assembly with a clamp substructure

identity: supported. Targets: GO:1990085.

The exact GO identity, two synonyms and replication-inhibiting parent agree. DnaN is correctly represented as a beta-ring complex with has_part linkage. The resolved discussion correctly excludes DnaA from this two-component-class boundary and distinguishes the separate DnaA-Hda entity.

### Resolvable Hda whole-family class

grounding: concern. Targets: GO:1990085.

The Hda label-only task is now resolvable through native IPR017788 and its Enterobacteriaceae child. The DnaN complex already has an exact GO grounding; a protein-family mapping is not substituted for that substructure.

### Direct binding perturbation with a bounded folding caveat

grounding: supported. Targets: GO:1990085.

The record correctly captures direct Hda/beta binding. Kurz additionally reports severe binding reduction after QLSLPL motif substitutions and competition by motif peptides. The authors retain altered folding as an alternative despite solubility and amylose binding. These observations support a bounded binding-site result; the scoped inventory need not enumerate every tested perturbation, and the assays do not establish universal necessity or directly measure DnaA hydrolysis.

### Supported broad RIDA function with correct evidence tier

graph: supported. Targets: GO:1990085.

The two membership edges and whole-complex negative-regulation edge are supported at their declared nonmechanistic scope. The function note says Kurz connected binding to accelerated hydrolysis; this is compatible with the paper's proposed connection and is not treated as a claim of newly measured hydrolysis. The graph already explicitly says proposed importance.

### E. coli binding assay and K12 reference proteins

scope: supported. Targets: GO:1990085.

The assay uses recombinant E. coli proteins expressed in specified hosts; K12 protein examples are kept separate from BL21/TB1 expression backgrounds. The paper's limited2002 sequence survey is historical and not a current distribution census. COMMON retains its majority-with-exceptions meaning.

### Universal individual-constituent requirements remain unestablished

grounding: unknown. Targets: GO:1990085.

The bounded interaction, recruitment and activity results do not establish a universal per-constituent formation-necessity profile. UNKNOWN values are not automatically defects and are not converted to ESSENTIAL.

### Complete maintained target and bounded follow-up

completeness: supported. Targets: GO:1990085.

Every maintained field, evidence row, component/example, graph edge, discussion and history entry was read. Optional unpopulated slots are not defects. Scientific status/history remain unchanged.

## Findings

### F1: Resolve the Hda family mapping

minor / open / confirmed; issue key: hda-beta-resolve-hda-family.

The Hda component and existing open task defer the exact family although native IPR017788 is the verified Hda branch, distinct from DnaA, and matches the reviewed reference protein.

## Recommended Actions And Acceptance Checks

### A1

Ground Hda at the verified whole-family identity and resolve the existing task.

- Use IPR017788 for the Hda class, retaining IPR022864 as narrower Enterobacteriaceae context.
- Keep the DnaN beta ring as the already grounded GO complex and preserve the DnaA boundary.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/hda_beta_clamp_complex.yaml; Entire maintained target, including all components, evidence, graph edges, discussions and history | context_only | The complete target was read. The maintained YAML owns any later scientific correction. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope | context_only | Formation necessity is distinct from activity, localization and viability. COMMON is the qualitative category present in most members with exceptional losses, not a measured prevalence census. |
| curation | docs/CURATION.md; Exact class identity and taxon-paired protein examples | context_only | Protein examples do not replace constituent-class grounding. Shared domains and broader paralog families do not resolve exact class tasks. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Scope and edge-level source support | context_only | Descriptive membership graphs need not assert a complete mechanism; a directly observed conditional physical dependency can be stated without making every constituent universally essential. |
| root57-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000118,GO:0000417,GO:0000785,GO:0004407,GO:0006334,GO:0032297,GO:0032991,GO:0044775,GO:0070823,GO:1990078,GO:1990083,GO:1990085; Native identities, status, complete definitions/comments/synonyms and focal typed relationships | supports | The twelve inspected terms establish the focal HDA1, Hda-beta and HIR identities, their parent classes and the named function/substructure targets. Only relevant typed relations were used. |
| root57-sources-GO1990085-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990085/ancestors?relations=is_a; Complete native is_a ancestor response | supports | The complete is_a-only ancestry supports the declared parent class. It does not establish parthood or taxonomic frequency. |
| root57-sources-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxonomy response | supports | Native taxId 562 identifies Escherichia coli; broad taxon, species and reference strain are kept distinct. |
| root57-sources-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxonomy response | supports | Native taxId 83333 identifies Escherichia coli K-12; broad taxon, species and reference strain are kept distinct. |
| root57-sources-pmid-12618445 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12618445+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 12618445: Identification of a novel membrane-associated gene product that suppresses toxicity of a TrfA peptide from plasmid RK2 and its relationship to the DnaA host initiation protein. Kim PD, Banack T, Lerman DM, Tracy JC, Camara JE, Crooke E, Oliver D, Firshein W. (2003); DOI 10.1128/jb.185.6.1817-1824.2003. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-pmid-15150238 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15150238+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 15150238: Interaction of the sliding clamp beta-subunit and Hda, a DnaA-related protein. Kurz M, Dalrymple B, Wijffels G, Kongsuwan K. (2004); DOI 10.1128/jb.186.11.3508-3515.2004. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-pmid-23994470 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23994470+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 23994470: A replicase clamp-binding dynamin-like protein promotes colocalization of nascent DNA strands and equipartitioning of chromosomes in E. coli. Ozaki S, Matsuda Y, Keyamura K, Kawakami H, Noguchi Y, Kasho K, Nagata K, Masuda T, Sakiyama Y, Katayama T. (2013); DOI 10.1016/j.celrep.2013.07.040. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-doi-10.1128_JB.186.11.3508-3515.2004 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.186.11.3508-3515.2004%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED 15150238: Interaction of the sliding clamp beta-subunit and Hda, a DnaA-related protein. Kurz M, Dalrymple B, Wijffels G, Kongsuwan K. (2004). Complete abstract read; body evidence is separately located. |
| root57-sources-protein-P69931 | https://rest.uniprot.org/uniprotkb/P69931.json; Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY and MISCELLANEOUS comments where present | supports | P69931 is the reviewed hda reference in taxon 83333. Native names/aliases, organism, family cross-references and annotations support the stated identity. Its localization evidence tags were checked directly; this does not imply primary-body inspection of every cited localization assay. |
| root57-sources-gene-hda | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahda%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and literal query parameters | supports | The exact gene and organism query, restricted to reviewed entries, returns exactly P69931. |
| root57-sources-protein-P0A988 | https://rest.uniprot.org/uniprotkb/P0A988.json; Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY and MISCELLANEOUS comments where present | supports | P0A988 is the reviewed dnaN reference in taxon 83333. Native names/aliases, organism, family cross-references and annotations support the stated identity. Its localization evidence tags were checked directly; this does not imply primary-body inspection of every cited localization assay. |
| root57-sources-gene-dnaN | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaN%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and literal query parameters | supports | The exact gene and organism query, restricted to reviewed entries, returns exactly P0A988. |
| root57-sources-ipr-IPR017788 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017788/; Native accession/name/type, complete description with curation flags, integrated signatures and hierarchy | supports | The whole Hda family is distinct from its DnaA sibling and integrates TIGR03420. |
| root57-sources-ipr-IPR022864 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022864/; Native accession/name/type, complete description with curation flags, integrated signatures and hierarchy | supports | The Enterobacteriaceae Hda child integrates HAMAP MF01158 and supports the narrower reference scope. |
| root57-sources-PMC415757-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC415757/; Results sec12–sec16 and Discussion sec17 in full including Figures1–3 captions and Tables1/2; Methods sec2, sec7, sec8 and sec9 in full | supports | Kurz2004 directly demonstrates purified Hda/beta binding, severe binding defects for two Hda hexapeptide-motif mutants and competition by motif-containing peptides. The Discussion proposes their relevance to RIDA and cites earlier hydrolysis work; these assays do not newly measure DnaA ATP hydrolysis. |
| schema-result | just validate data/structures/other/hda_beta_clamp_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/hda_beta_clamp_complex.yaml |
| strict-result | just validate-strict data/structures/other/hda_beta_clamp_complex.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda_beta_clamp_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/hda_beta_clamp_complex.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda_beta_clamp_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda_beta_clamp_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml --causal-graphs; Complete focused native report | supports | data/structures/other/hda_beta_clamp_complex.yaml  (GO:1990085)<br>  hda_beta_clamp_rida	hda_regulator	COVERED	-&gt;hda_regulator (UniProtKB:P69931)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml --verify; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/hda_beta_clamp_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 13 collected target identifiers returned OK. PMID:12618445: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:15150238: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:23994470: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five same-base batch26 corpus gates and exact target resolver rows are integrated with every manifested input hash verified.
- No figure pixels, atomic coordinates, raw assay datasets or sequence alignments were reanalyzed. Primary body reading is limited to the explicitly named sections and embedded captions.
- Any absence finding is confined to the complete inspected target and its existing task; bounded native family queries do not establish absence from all databases.
- Protein localization source notes match native annotation provenance. Except where explicitly described, the cited localization papers were read at abstract tier; their detailed assays were not independently rechecked.
- Protein-expression/purification Methods sec5/sec6 and the buffer subsection were not independently read; the actual binding and mutation protocols were read.
- The sequence survey and proposed RIDA handover mechanism in the2004 Discussion are historical, not a current comparative-genomics or mechanistic review.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations and issue-bearing reviews alike.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Materiality reassessment removed an optional association-detail omission finding; the source observation remains explicitly assessed and universal formation necessity remains unknown.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T074157Z-hda-beta-clamp-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of Hda-beta clamp complex
started_at: '2026-10-22T07:12:35Z'
finished_at: '2026-10-22T07:41:57Z'
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
summary: One minor finding resolves the Hda family mapping. Exact complex boundaries,
  DnaN substructure, reference proteins and the nonmechanistic RIDA function are supported.
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
  - path: data/structures/other/hda_beta_clamp_complex.yaml
    sha256: 17d71a8e1991caf8baa03ec95079930ae623433d2f04a1c063211c4b127f4bfb
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
- target_id: GO:1990085
  path: data/structures/other/hda_beta_clamp_complex.yaml
  label: Hda-beta clamp complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda_beta_clamp_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, with source-native and primary
    reading scopes declared individually.
  selection: One complete record in strict-path batch 57 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990085
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: just validate data/structures/other/hda_beta_clamp_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: just validate-strict data/structures/other/hda_beta_clamp_complex.yaml
    --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda_beta_clamp_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990085
  summary: No iModulon-specific claim is assessed; the relevant complex/assay evidence
    was inspected directly.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990085
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root57-sources-go
  - root57-sources-GO1990085-ancestors
  - root57-sources-tax-562
  - root57-sources-tax-83333
  - root57-sources-pmid-12618445
  - root57-sources-pmid-15150238
  - root57-sources-pmid-23994470
  - root57-sources-doi-10.1128_JB.186.11.3508-3515.2004
  - root57-sources-protein-P69931
  - root57-sources-gene-hda
  - root57-sources-protein-P0A988
  - root57-sources-gene-dnaN
  - root57-sources-ipr-IPR017788
  - root57-sources-ipr-IPR022864
  - root57-sources-PMC415757-html
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990085
  summary: '10 of 13 collected target identifiers returned OK. PMID:12618445: UNREACHABLE;
    Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport
    failure in the corpus resolver is not treated as identifier invalidity or as proof
    that its primary body was read.; PMID:15150238: UNREACHABLE; Unique native MED
    identity, exact PMID/title/DOI and bibliography inspected; transport failure in
    the corpus resolver is not treated as identifier invalidity or as proof that its
    primary body was read.; PMID:23994470: UNREACHABLE; Unique native MED identity,
    exact PMID/title/DOI and bibliography inspected; transport failure in the corpus
    resolver is not treated as identifier invalidity or as proof that its primary
    body was read. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root57-sources-pmid-12618445
  - root57-sources-pmid-15150238
  - root57-sources-doi-10.1128_JB.186.11.3508-3515.2004
  - root57-sources-pmid-23994470
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990085
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
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/hda_beta_clamp_complex.yaml
  locator: Entire maintained target, including all components, evidence, graph edges,
    discussions and history
  accessed_at: '2026-10-22T07:22:38Z'
  support: context_only
  summary: The complete target was read. The maintained YAML owns any later scientific
    correction.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope
  accessed_at: '2026-10-22T07:22:38Z'
  support: context_only
  summary: Formation necessity is distinct from activity, localization and viability.
    COMMON is the qualitative category present in most members with exceptional losses,
    not a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and taxon-paired protein examples
  accessed_at: '2026-10-22T07:22:38Z'
  support: context_only
  summary: Protein examples do not replace constituent-class grounding. Shared domains
    and broader paralog families do not resolve exact class tasks.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope and edge-level source support
  accessed_at: '2026-10-22T07:22:38Z'
  support: context_only
  summary: Descriptive membership graphs need not assert a complete mechanism; a directly
    observed conditional physical dependency can be stated without making every constituent
    universally essential.
- evidence_id: root57-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000118,GO:0000417,GO:0000785,GO:0004407,GO:0006334,GO:0032297,GO:0032991,GO:0044775,GO:0070823,GO:1990078,GO:1990083,GO:1990085
  locator: Native identities, status, complete definitions/comments/synonyms and focal
    typed relationships
  accessed_at: '2026-10-22T07:09:06.769100Z'
  support: supports
  summary: The twelve inspected terms establish the focal HDA1, Hda-beta and HIR identities,
    their parent classes and the named function/substructure targets. Only relevant
    typed relations were used.
  snapshot_sha256: 21ed713180a84eeed2230337bf1f89ecd5489141f8030b26157ee5ec18456ad0
- evidence_id: root57-sources-GO1990085-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990085/ancestors?relations=is_a
  locator: Complete native is_a ancestor response
  accessed_at: '2026-10-22T07:09:19.147174Z'
  support: supports
  summary: The complete is_a-only ancestry supports the declared parent class. It
    does not establish parthood or taxonomic frequency.
  snapshot_sha256: 79a887d523798106a919ec5ea9ad2ff992d366801e9c263cdc093ba67c98d66a
- evidence_id: root57-sources-tax-562
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T07:09:07.418260Z'
  support: supports
  summary: Native taxId 562 identifies Escherichia coli; broad taxon, species and
    reference strain are kept distinct.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: root57-sources-tax-83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T07:09:08.039051Z'
  support: supports
  summary: Native taxId 83333 identifies Escherichia coli K-12; broad taxon, species
    and reference strain are kept distinct.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: root57-sources-pmid-12618445
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12618445+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:12.523978Z'
  support: supports
  summary: 'MED 12618445: Identification of a novel membrane-associated gene product
    that suppresses toxicity of a TrfA peptide from plasmid RK2 and its relationship
    to the DnaA host initiation protein. Kim PD, Banack T, Lerman DM, Tracy JC, Camara
    JE, Crooke E, Oliver D, Firshein W. (2003); DOI 10.1128/jb.185.6.1817-1824.2003.
    Entire native abstract read; this evidence row does not claim the paper body.'
  snapshot_sha256: 9a4cf8f2fc413e18680829d20076a9510e53ab4c4f3f8d5163e9f4ce829a0189
- evidence_id: root57-sources-pmid-15150238
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15150238+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:13.124184Z'
  support: supports
  summary: 'MED 15150238: Interaction of the sliding clamp beta-subunit and Hda, a
    DnaA-related protein. Kurz M, Dalrymple B, Wijffels G, Kongsuwan K. (2004); DOI
    10.1128/jb.186.11.3508-3515.2004. Entire native abstract read; this evidence row
    does not claim the paper body.'
  snapshot_sha256: c5c5c1b6a1f782d496a6450aae2b6dbcf2d2b8442b8d870660409043fc51051f
- evidence_id: root57-sources-pmid-23994470
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23994470+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:14.352340Z'
  support: supports
  summary: 'MED 23994470: A replicase clamp-binding dynamin-like protein promotes
    colocalization of nascent DNA strands and equipartitioning of chromosomes in E.
    coli. Ozaki S, Matsuda Y, Keyamura K, Kawakami H, Noguchi Y, Kasho K, Nagata K,
    Masuda T, Sakiyama Y, Katayama T. (2013); DOI 10.1016/j.celrep.2013.07.040. Entire
    native abstract read; this evidence row does not claim the paper body.'
  snapshot_sha256: feea24d737397f0b9b8b8ec9c72b20936759036d7cf3b303d81c264d7ab780a8
- evidence_id: root57-sources-doi-10.1128_JB.186.11.3508-3515.2004
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.186.11.3508-3515.2004%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T07:09:17.570017Z'
  support: supports
  summary: 'Unique DOI result MED 15150238: Interaction of the sliding clamp beta-subunit
    and Hda, a DnaA-related protein. Kurz M, Dalrymple B, Wijffels G, Kongsuwan K.
    (2004). Complete abstract read; body evidence is separately located.'
  snapshot_sha256: b16dd0d9e230228b9d94183ae6f768c973349f352ae22db65f12b2c3c44495f0
- evidence_id: root57-sources-protein-P69931
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P69931.json
  locator: Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY
    and MISCELLANEOUS comments where present
  accessed_at: '2026-10-22T07:09:10.318613Z'
  support: supports
  summary: P69931 is the reviewed hda reference in taxon 83333. Native names/aliases,
    organism, family cross-references and annotations support the stated identity.
    Its localization evidence tags were checked directly; this does not imply primary-body
    inspection of every cited localization assay.
  snapshot_sha256: 426a92b935654ddf255d7bb462d2bd0bce6ab02033aed38b8e324916751c0b1d
- evidence_id: root57-sources-gene-hda
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahda%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and literal query parameters
  accessed_at: '2026-10-22T07:09:19.726645Z'
  support: supports
  summary: The exact gene and organism query, restricted to reviewed entries, returns
    exactly P69931.
  snapshot_sha256: eb8af1bf9d21c98c3becc40e269fbb9fd003455df2925d8b91c12c8d659df4c1
- evidence_id: root57-sources-protein-P0A988
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A988.json
  locator: Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY
    and MISCELLANEOUS comments where present
  accessed_at: '2026-10-22T07:09:08.113575Z'
  support: supports
  summary: P0A988 is the reviewed dnaN reference in taxon 83333. Native names/aliases,
    organism, family cross-references and annotations support the stated identity.
    Its localization evidence tags were checked directly; this does not imply primary-body
    inspection of every cited localization assay.
  snapshot_sha256: 41e5cead43ae6b73cc4fedfee2b9e111259e12f217532aba8590e487ea82f65f
- evidence_id: root57-sources-gene-dnaN
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaN%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and literal query parameters
  accessed_at: '2026-10-22T07:09:19.932997Z'
  support: supports
  summary: The exact gene and organism query, restricted to reviewed entries, returns
    exactly P0A988.
  snapshot_sha256: 1887ae15fef4c0ae00bfb78438785bb21e2ed00e22c11ddbe95db13d89030426
- evidence_id: root57-sources-ipr-IPR017788
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017788/
  locator: Native accession/name/type, complete description with curation flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:12:52.655610Z'
  support: supports
  summary: The whole Hda family is distinct from its DnaA sibling and integrates TIGR03420.
  snapshot_sha256: 7e9d3b5937bd2091b11b482deda5c5328592a0121f84c369e97a6ba8390abb6c
- evidence_id: root57-sources-ipr-IPR022864
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022864/
  locator: Native accession/name/type, complete description with curation flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:12:53.372943Z'
  support: supports
  summary: The Enterobacteriaceae Hda child integrates HAMAP MF01158 and supports
    the narrower reference scope.
  snapshot_sha256: a3300bce98be51679d5018b6ad7ad5dc4ad5108f0c7c19c006f084c8f43425f0
- evidence_id: root57-sources-PMC415757-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC415757/
  locator: Results sec12–sec16 and Discussion sec17 in full including Figures1–3 captions
    and Tables1/2; Methods sec2, sec7, sec8 and sec9 in full
  accessed_at: '2026-10-22T07:12:55.510102Z'
  support: supports
  summary: Kurz2004 directly demonstrates purified Hda/beta binding, severe binding
    defects for two Hda hexapeptide-motif mutants and competition by motif-containing
    peptides. The Discussion proposes their relevance to RIDA and cites earlier hydrolysis
    work; these assays do not newly measure DnaA ATP hydrolysis.
  snapshot_sha256: 9560275c8d6d865e2380f2ac8f9a73158261a8b3e999161ec784c7ae80a763fc
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/hda_beta_clamp_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:12:36Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/hda_beta_clamp_complex.yaml'
  snapshot_sha256: 7e7fb9dc21ee30fb04e47b9c4dd953d962429bc767095255613a3d8736987954
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/hda_beta_clamp_complex.yaml
    --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda_beta_clamp_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:12:37Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/hda_beta_clamp_complex.yaml\
    \ --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda_beta_clamp_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hda_beta_clamp_complex-strict.tsv"
  snapshot_sha256: d1bd31aeb483cddaac6ff767802335b1eb1acb76a0bd49f5ca155255b65f4c83
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml
    --causal-graphs
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:17:31.647667Z'
  support: supports
  summary: "data/structures/other/hda_beta_clamp_complex.yaml  (GO:1990085)\n  hda_beta_clamp_rida\t\
    hda_regulator\tCOVERED\t->hda_regulator (UniProtKB:P69931)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     1  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     1  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: fdb72ccdbcb760c5581b5ce5a9ec2ee7fbba558b130b4cc5bf5b39f01c27460d
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml
    --verify
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:17:32.951860Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/hda_beta_clamp_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 13 collected target identifiers returned OK. PMID:12618445: UNREACHABLE;
    Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport
    failure in the corpus resolver is not treated as identifier invalidity or as proof
    that its primary body was read.; PMID:15150238: UNREACHABLE; Unique native MED
    identity, exact PMID/title/DOI and bibliography inspected; transport failure in
    the corpus resolver is not treated as identifier invalidity or as proof that its
    primary body was read.; PMID:23994470: UNREACHABLE; Unique native MED identity,
    exact PMID/title/DOI and bibliography inspected; transport failure in the corpus
    resolver is not treated as identifier invalidity or as proof that its primary
    body was read. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
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
  topic: Hda-beta assembly with a clamp substructure
  outcome: supported
  target_ids:
  - GO:1990085
  summary: The exact GO identity, two synonyms and replication-inhibiting parent agree.
    DnaN is correctly represented as a beta-ring complex with has_part linkage. The
    resolved discussion correctly excludes DnaA from this two-component-class boundary
    and distinguishes the separate DnaA-Hda entity.
  evidence_ids:
  - record
  - root57-sources-go
  - root57-sources-GO1990085-ancestors
  - root57-sources-PMC415757-html
- assessment_id: composition
  area: grounding
  topic: Resolvable Hda whole-family class
  outcome: concern
  target_ids:
  - GO:1990085
  summary: The Hda label-only task is now resolvable through native IPR017788 and
    its Enterobacteriaceae child. The DnaN complex already has an exact GO grounding;
    a protein-family mapping is not substituted for that substructure.
  evidence_ids:
  - record
  - curation
  - root57-sources-ipr-IPR017788
  - root57-sources-ipr-IPR022864
  - root57-sources-protein-P69931
  - root57-sources-protein-P0A988
  - root57-sources-gene-hda
  - root57-sources-gene-dnaN
- assessment_id: formation
  area: grounding
  topic: Direct binding perturbation with a bounded folding caveat
  outcome: supported
  target_ids:
  - GO:1990085
  summary: The record correctly captures direct Hda/beta binding. Kurz additionally
    reports severe binding reduction after QLSLPL motif substitutions and competition
    by motif peptides. The authors retain altered folding as an alternative despite
    solubility and amylose binding. These observations support a bounded binding-site
    result; the scoped inventory need not enumerate every tested perturbation, and
    the assays do not establish universal necessity or directly measure DnaA hydrolysis.
  evidence_ids:
  - record
  - schema
  - root57-sources-PMC415757-html
- assessment_id: graph
  area: graph
  topic: Supported broad RIDA function with correct evidence tier
  outcome: supported
  target_ids:
  - GO:1990085
  summary: The two membership edges and whole-complex negative-regulation edge are
    supported at their declared nonmechanistic scope. The function note says Kurz
    connected binding to accelerated hydrolysis; this is compatible with the paper's
    proposed connection and is not treated as a claim of newly measured hydrolysis.
    The graph already explicitly says proposed importance.
  evidence_ids:
  - record
  - graphs
  - root57-sources-go
  - root57-sources-PMC415757-html
  - root57-sources-protein-P69931
  - root57-sources-protein-P0A988
- assessment_id: scope
  area: scope
  topic: E. coli binding assay and K12 reference proteins
  outcome: supported
  target_ids:
  - GO:1990085
  summary: The assay uses recombinant E. coli proteins expressed in specified hosts;
    K12 protein examples are kept separate from BL21/TB1 expression backgrounds. The
    paper's limited2002 sequence survey is historical and not a current distribution
    census. COMMON retains its majority-with-exceptions meaning.
  evidence_ids:
  - record
  - schema
  - root57-sources-PMC415757-html
  - root57-sources-tax-562
  - root57-sources-tax-83333
  - root57-sources-protein-P69931
  - root57-sources-protein-P0A988
- assessment_id: formation-necessity
  area: grounding
  topic: Universal individual-constituent requirements remain unestablished
  outcome: unknown
  target_ids:
  - GO:1990085
  summary: The bounded interaction, recruitment and activity results do not establish
    a universal per-constituent formation-necessity profile. UNKNOWN values are not
    automatically defects and are not converted to ESSENTIAL.
  evidence_ids:
  - record
  - schema
  - root57-sources-PMC415757-html
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target and bounded follow-up
  outcome: supported
  target_ids:
  - GO:1990085
  summary: Every maintained field, evidence row, component/example, graph edge, discussion
    and history entry was read. Optional unpopulated slots are not defects. Scientific
    status/history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root57-sources-go
  - root57-sources-doi-10.1128_JB.186.11.3508-3515.2004
findings:
- finding_id: F1
  issue_key: hda-beta-resolve-hda-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the Hda family mapping
  description: The Hda component and existing open task defer the exact family although
    native IPR017788 is the verified Hda branch, distinct from DnaA, and matches the
    reviewed reference protein.
  target_ids:
  - GO:1990085
  field_paths:
  - components[0].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root57-sources-ipr-IPR017788
  - root57-sources-ipr-IPR022864
  - root57-sources-protein-P69931
  - root57-sources-protein-P0A988
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda_beta_clamp_complex.yaml
    role: maintained scientific record
  rule_id: Exact constituent-class grounding
  native_severity: minor
  normalization_reason: A bounded actionable class mapping under the existing explicit
    task; the complex identity and named protein examples remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990085
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda_beta_clamp_complex.yaml
    role: maintained scientific record
  description: Ground Hda at the verified whole-family identity and resolve the existing
    task.
  acceptance_checks:
  - Use IPR017788 for the Hda class, retaining IPR022864 as narrower Enterobacteriaceae
    context.
  - Keep the DnaN beta ring as the already grounded GO complex and preserve the DnaA
    boundary.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
limitations:
- All five same-base batch26 corpus gates and exact target resolver rows are integrated
  with every manifested input hash verified.
- No figure pixels, atomic coordinates, raw assay datasets or sequence alignments
  were reanalyzed. Primary body reading is limited to the explicitly named sections
  and embedded captions.
- Any absence finding is confined to the complete inspected target and its existing
  task; bounded native family queries do not establish absence from all databases.
- Protein localization source notes match native annotation provenance. Except where
  explicitly described, the cited localization papers were read at abstract tier;
  their detailed assays were not independently rechecked.
- Protein-expression/purification Methods sec5/sec6 and the buffer subsection were
  not independently read; the actual binding and mutation protocols were read.
- The sequence survey and proposed RIDA handover mechanism in the2004 Discussion are
  historical, not a current comparative-genomics or mechanistic review.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations and issue-bearing reviews
  alike.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Materiality reassessment removed an optional association-detail omission finding;
  the source observation remains explicitly assessed and universal formation necessity
  remains unknown.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
