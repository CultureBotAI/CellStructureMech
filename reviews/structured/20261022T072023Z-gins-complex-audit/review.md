# Source-grounded review of GINS complex

- Review: 20261022T072023Z-gins-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:59:38Z
- Finished UTC: 2026-10-22T07:20:23Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minor findings resolve all four GINS subunit families and preserve the conditional sld5-12 complex-recovery/PSF2-rescue result. Four-subunit identity, reference proteins, CMG boundary and DNA-replication function are supported.

## Scope And Provenance

Exactly one complete maintained target, with source-native and primary reading scopes declared individually.

Selection: One complete record in strict-path batch 56 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000811 | data/structures/other/gins_complex.yaml | maintained | GINS complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0000811 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000811 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0000811 | Focused check passed; scientific claims assessed separately. |
| Native focused verify | passed | True | GO:0000811 | Focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0000811 | No iModulon-specific claim is assessed; the relevant complex/assay evidence was inspected directly. |
| Claim-level scientific review | passed | True | GO:0000811 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0000811 | 10 of 11 collected target identifiers returned OK. PMID:12730134: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0000811 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000811 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000811 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000811 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0000811 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Four-protein GINS boundary

identity: supported. Targets: GO:0000811.

GO and tagged-protein purification identify Sld5, Psf1, Psf2 and Psf3 as the heterotetramer. The existing resolved boundary correctly keeps Cdc45 and MCM outside GINS; origin factors and the broader CMG are adjacent assemblies.

### Four resolved constituent families

grounding: concern. Targets: GO:0000811.

Each label-only class has an exact native whole-family entry, corroborated by its reviewed S288C protein and gene query. Shared domains and generic prose are not substituted for class identity or primary mechanism.

### Direct conditional complex-recovery result

grounding: concern. Targets: GO:0000811.

The cited primary body directly measures reduced recoverable GINS in sld5-12 at 23 C and rescue by high-copy PSF2. Generic constituent roles and graph membership omit this bounded physical-complex result. The authors could not test psf1-1 complex assembly with the attempted tag, so that mutant cannot be assigned the same demonstrated phenotype.

### Supported composition and DNA-replication function

graph: supported. Targets: GO:0000811.

All four contributes-to edges and the whole-complex replication edge are supported. Origin association, subsequent flanking-sequence association and genetic dependencies explain the function without promoting adjacent origin machinery to constituents or asserting that GINS alone catalyzes helicase activity.

### Yeast experimental and reference scope

scope: supported. Targets: GO:0000811.

The maintained species example is supported. Reviewed S288C accession identities are not proof that all experiment strains were S288C; full strain-table details remain in the unread supplement. COMMON means present in most members with losses as exceptions; this qualitative category is not a measured frequency statistic.

### Complete maintained target and bounded follow-up

completeness: supported. Targets: GO:0000811.

Every maintained field, evidence row, component/example, graph edge, discussion and history entry was read. Optional unpopulated slots are not defects. Scientific status/history remain unchanged.

### Universal individual-constituent formation requirements

grounding: unknown. Targets: GO:0000811.

The bounded physical-association and activity observations assessed above do not establish a universal individual-constituent necessity profile for formation of this structure. Unspecified requirements remain unknown; they are not presumed essential or treated as a new corrective finding.

## Findings

### F1: Resolve the four GINS family mappings

minor / open / confirmed; issue key: gins-four-exact-subunit-families.

The four components and the existing open task still leave exact family groundings unresolved. Native whole-family entries and reviewed reference-protein cross-references now resolve every named class.

### F2: Capture the conditional GINS recovery and rescue result

minor / open / confirmed; issue key: gins-sld5-mutant-complex-recovery.

The source reports less than one fifth of normal recoverable complex in sld5-12 cells at 23 C and substantial high-copy PSF2 rescue. Current roles and graph edges give only generic membership despite this directly assayed complex-level dependence.

## Recommended Actions And Acceptance Checks

### A1

Ground the four classes and resolve or narrow the existing family task while preserving the established GINS versus CMG boundary.

- Map Sld5 to IPR008591, Psf1 to IPR005339, Psf2 to IPR007257 and Psf3 to IPR010492.
- Keep taxon-paired reference examples distinct from exact class identifiers.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

### A2

Add the specifically assayed sld5-12 complex-recovery result and PSF2 dosage rescue with strain, temperature and purification/readout context.

- Distinguish lower recoverable complex and subunit abundance from direct measurement of protein degradation.
- Do not infer complete absence, universal ESSENTIAL for all four proteins, or an equivalent psf1-1 assembly result.
- Separate the permissive-temperature complex assay from restrictive-temperature replication/viability assays.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/gins_complex.yaml; Entire maintained target, including all components, evidence, graph edges, discussions and history | context_only | The complete target was read. The maintained YAML owns any later scientific correction. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope | context_only | Formation necessity is distinct from activity, localization and viability. COMMON is the qualitative category present in most members with exceptional losses, not a measured prevalence census. |
| curation | docs/CURATION.md; Exact class identity and taxon-paired protein examples | context_only | Protein examples do not replace constituent-class grounding. Shared domains and broader paralog families do not resolve exact class tasks. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Scope and edge-level source support | context_only | Descriptive membership graphs need not assert a complete mechanism; a directly observed conditional physical dependency can be stated without making every constituent universally essential. |
| root56-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0005789,GO:0006260,GO:0032991,GO:0043529,GO:0070258,GO:0071816,GO:0071980,GO:0140534,GO:0160055; Native identities, status, complete definitions/comments/synonyms and focal typed relationships | supports | The ten inspected terms establish the focal GET, GINS and glideosome identities, their declared parent classes and the named process/localization targets. Only relevant typed relations were used. |
| root56-sources-GO0000811-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811/ancestors?relations=is_a; Complete native is_a ancestor response | supports | The complete is_a-only ancestry supports the declared parent class. It does not establish parthood or taxonomic frequency. |
| root56-sources-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | Native taxId 4932 identifies Saccharomyces cerevisiae; broad taxon, species and reference strain are kept distinct. |
| root56-sources-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | Native taxId 559292 identifies Saccharomyces cerevisiae S288C; broad taxon, species and reference strain are kept distinct. |
| root56-sources-pmid-12730134 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12730134+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 12730134: GINS, a novel multiprotein complex required for chromosomal DNA replication in budding yeast. Takayama Y, Kamimura Y, Okawa M, Muramatsu S, Sugino A, Araki H. (2003); DOI 10.1101/gad.1065903. Entire native abstract read; this evidence row does not claim the paper body. |
| root56-sources-doi-10.1101_gad.1065903 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1065903%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED 12730134: GINS, a novel multiprotein complex required for chromosomal DNA replication in budding yeast. Takayama Y, Kamimura Y, Okawa M, Muramatsu S, Sugino A, Araki H. (2003). Complete abstract read; body evidence is separately located. |
| root56-sources-protein-Q03406 | https://rest.uniprot.org/uniprotkb/Q03406.json; Identity/status/names, genes/aliases, organism and family cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | Q03406: The reviewed gene/taxon identity and native whole-family cross-references corroborate the named constituent class. |
| root56-sources-gene-SLD5 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASLD5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set and literal native query parameters | supports | The query restricted to the declared organism and gene/locus returns exactly Q03406; reviewed filtering is used only for reviewed examples. |
| root56-sources-protein-Q12488 | https://rest.uniprot.org/uniprotkb/Q12488.json; Identity/status/names, genes/aliases, organism and family cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | Q12488: The reviewed gene/taxon identity and native whole-family cross-references corroborate the named constituent class. |
| root56-sources-gene-PSF1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set and literal native query parameters | supports | The query restricted to the declared organism and gene/locus returns exactly Q12488; reviewed filtering is used only for reviewed examples. |
| root56-sources-protein-P40359 | https://rest.uniprot.org/uniprotkb/P40359.json; Identity/status/names, genes/aliases, organism and family cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | P40359: The reviewed gene/taxon identity and native whole-family cross-references corroborate the named constituent class. |
| root56-sources-gene-PSF2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set and literal native query parameters | supports | The query restricted to the declared organism and gene/locus returns exactly P40359; reviewed filtering is used only for reviewed examples. |
| root56-sources-protein-Q12146 | https://rest.uniprot.org/uniprotkb/Q12146.json; Identity/status/names, genes/aliases, organism and family cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | Q12146: The reviewed gene/taxon identity and native whole-family cross-references corroborate the named constituent class. |
| root56-sources-gene-PSF3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set and literal native query parameters | supports | The query restricted to the declared organism and gene/locus returns exactly Q12146; reviewed filtering is used only for reviewed examples. |
| root56-sources-ipr-IPR008591 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008591/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | Exact whole-family identity for Sld5; the corresponding reviewed yeast example independently carries this cross-reference. Generic old clamp/helicase prose is not treated as a direct catalytic experiment. |
| root56-sources-ipr-IPR005339 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005339/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | Exact whole-family identity for Psf1; the corresponding reviewed yeast example independently carries this cross-reference. Generic old clamp/helicase prose is not treated as a direct catalytic experiment. |
| root56-sources-ipr-IPR007257 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007257/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | Exact whole-family identity for Psf2; the corresponding reviewed yeast example independently carries this cross-reference. Generic old clamp/helicase prose is not treated as a direct catalytic experiment. |
| root56-sources-ipr-IPR010492 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010492/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | Exact whole-family identity for Psf3; the corresponding reviewed yeast example independently carries this cross-reference. Generic old clamp/helicase prose is not treated as a direct catalytic experiment. |
| root56-sources-PMC196052-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC196052/; Results sec2, sec4, sec5, sec6, sec7, sec8 and sec9 in full, including embedded Figures 1–7 captions; Methods sec15 and sec20 in full | supports | Takayama 2003 identifies the four-protein GINS assembly and replication roles. In sld5-12 cells at the permissive 23 C, recoverable complex is below one fifth of wild type and high-copy PSF2 substantially rescues it. Reduced subunit abundance and inferred degradation are distinguished from directly measured coassociation; replication defects at restrictive temperatures are separate readouts. |
| schema-result | just validate data/structures/other/gins_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/gins_complex.yaml |
| strict-result | just validate-strict data/structures/other/gins_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/gins_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/gins_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/gins_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/gins_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/gins_complex.yaml --causal-graphs; Complete focused native report | supports | data/structures/other/gins_complex.yaml  (GO:0000811)<br>  gins_chromosomal_dna_replication	sld5_subunit	COVERED	-&gt;sld5_subunit (UniProtKB:Q03406)<br>  gins_chromosomal_dna_replication	psf1_subunit	COVERED	-&gt;psf1_subunit (UniProtKB:Q12488)<br>  gins_chromosomal_dna_replication	psf2_subunit	COVERED	-&gt;psf2_subunit (UniProtKB:P40359)<br>  gins_chromosomal_dna_replication	psf3_subunit	COVERED	-&gt;psf3_subunit (UniProtKB:Q12146)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/gins_complex.yaml --verify; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/gins_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 11 collected target identifiers returned OK. PMID:12730134: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five same-base batch26 corpus gates and exact target resolver rows are integrated with every manifested input hash verified.
- No figure pixels, raw datasets, sequence alignments, atomic coordinates or supplementary files were reanalyzed. Primary body reading is limited to declared sections and embedded captions.
- Any absence finding is confined to the complete inspected target and its existing task; no claim is made that a related record or identifier is absent from the corpus or all databases.
- The supplemental strain table and raw microscopy/gel data were not inspected. Methods sec15 and sec20 were read; no claim is made to have read every ChIP protocol detail.
- InterPro description text includes historical clamp suggestions and generic helicase wording; these are not adopted as a modern mechanistic conclusion.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations and issue-bearing reviews alike.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T072023Z-gins-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of GINS complex
started_at: '2026-10-22T06:59:38Z'
finished_at: '2026-10-22T07:20:23Z'
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
summary: Two minor findings resolve all four GINS subunit families and preserve the
  conditional sld5-12 complex-recovery/PSF2-rescue result. Four-subunit identity,
  reference proteins, CMG boundary and DNA-replication function are supported.
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
  - path: data/structures/other/gins_complex.yaml
    sha256: 485835a6777e1752fc93d1e3149d8ff1416f7ee1d24755ad5e636e591e57c048
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
- target_id: GO:0000811
  path: data/structures/other/gins_complex.yaml
  label: GINS complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gins_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, with source-native and primary
    reading scopes declared individually.
  selection: One complete record in strict-path batch 56 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000811
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000811
  command: just validate data/structures/other/gins_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000811
  command: just validate-strict data/structures/other/gins_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/gins_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0000811
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gins_complex.yaml --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0000811
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gins_complex.yaml --verify
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0000811
  summary: No iModulon-specific claim is assessed; the relevant complex/assay evidence
    was inspected directly.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000811
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root56-sources-go
  - root56-sources-GO0000811-ancestors
  - root56-sources-tax-4932
  - root56-sources-tax-559292
  - root56-sources-pmid-12730134
  - root56-sources-doi-10.1101_gad.1065903
  - root56-sources-protein-Q03406
  - root56-sources-gene-SLD5
  - root56-sources-protein-Q12488
  - root56-sources-gene-PSF1
  - root56-sources-protein-P40359
  - root56-sources-gene-PSF2
  - root56-sources-protein-Q12146
  - root56-sources-gene-PSF3
  - root56-sources-ipr-IPR008591
  - root56-sources-ipr-IPR005339
  - root56-sources-ipr-IPR007257
  - root56-sources-ipr-IPR010492
  - root56-sources-PMC196052-html
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0000811
  summary: '10 of 11 collected target identifiers returned OK. PMID:12730134: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - root56-sources-pmid-12730134
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000811
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0000811
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0000811
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0000811
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0000811
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
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/gins_complex.yaml
  locator: Entire maintained target, including all components, evidence, graph edges,
    discussions and history
  accessed_at: '2026-10-22T07:05:04Z'
  support: context_only
  summary: The complete target was read. The maintained YAML owns any later scientific
    correction.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope
  accessed_at: '2026-10-22T07:05:04Z'
  support: context_only
  summary: Formation necessity is distinct from activity, localization and viability.
    COMMON is the qualitative category present in most members with exceptional losses,
    not a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and taxon-paired protein examples
  accessed_at: '2026-10-22T07:05:04Z'
  support: context_only
  summary: Protein examples do not replace constituent-class grounding. Shared domains
    and broader paralog families do not resolve exact class tasks.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope and edge-level source support
  accessed_at: '2026-10-22T07:05:04Z'
  support: context_only
  summary: Descriptive membership graphs need not assert a complete mechanism; a directly
    observed conditional physical dependency can be stated without making every constituent
    universally essential.
- evidence_id: root56-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0005789,GO:0006260,GO:0032991,GO:0043529,GO:0070258,GO:0071816,GO:0071980,GO:0140534,GO:0160055
  locator: Native identities, status, complete definitions/comments/synonyms and focal
    typed relationships
  accessed_at: '2026-10-22T06:55:10.748737Z'
  support: supports
  summary: The ten inspected terms establish the focal GET, GINS and glideosome identities,
    their declared parent classes and the named process/localization targets. Only
    relevant typed relations were used.
  snapshot_sha256: 09032cf2d48c60b2af7c714e4cb8b3a9aa65fce438af07e97bf95c6c59853e3a
- evidence_id: root56-sources-GO0000811-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811/ancestors?relations=is_a
  locator: Complete native is_a ancestor response
  accessed_at: '2026-10-22T06:55:18.037335Z'
  support: supports
  summary: The complete is_a-only ancestry supports the declared parent class. It
    does not establish parthood or taxonomic frequency.
  snapshot_sha256: 91319d3aeadefff2b3bc10f23b9869ba3328cb04a76894e48e8745d0242912ac
- evidence_id: root56-sources-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:55:10.749010Z'
  support: supports
  summary: Native taxId 4932 identifies Saccharomyces cerevisiae; broad taxon, species
    and reference strain are kept distinct.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root56-sources-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:55:11.406635Z'
  support: supports
  summary: Native taxId 559292 identifies Saccharomyces cerevisiae S288C; broad taxon,
    species and reference strain are kept distinct.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root56-sources-pmid-12730134
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12730134+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T06:55:15.424352Z'
  support: supports
  summary: 'MED 12730134: GINS, a novel multiprotein complex required for chromosomal
    DNA replication in budding yeast. Takayama Y, Kamimura Y, Okawa M, Muramatsu S,
    Sugino A, Araki H. (2003); DOI 10.1101/gad.1065903. Entire native abstract read;
    this evidence row does not claim the paper body.'
  snapshot_sha256: e384d195dea6f83623f4873a66ab86cf53162534e8813c2f3ad1b00128f9608a
- evidence_id: root56-sources-doi-10.1101_gad.1065903
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1065903%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T06:55:17.325470Z'
  support: supports
  summary: 'Unique DOI result MED 12730134: GINS, a novel multiprotein complex required
    for chromosomal DNA replication in budding yeast. Takayama Y, Kamimura Y, Okawa
    M, Muramatsu S, Sugino A, Araki H. (2003). Complete abstract read; body evidence
    is separately located.'
  snapshot_sha256: acc19cbb1f311b91e922ad0f5990dc4616650500d6c580d8754dd3bdd54cd305
- evidence_id: root56-sources-protein-Q03406
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03406.json
  locator: Identity/status/names, genes/aliases, organism and family cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:55:13.317689Z'
  support: supports
  summary: 'Q03406: The reviewed gene/taxon identity and native whole-family cross-references
    corroborate the named constituent class.'
  snapshot_sha256: 0f0ab1e1af41bb24cee36f864ebc31dd7545b0bb29a248a5cc47c3d3e1af1494
- evidence_id: root56-sources-gene-SLD5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASLD5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set and literal native query parameters
  accessed_at: '2026-10-22T06:55:18.453033Z'
  support: supports
  summary: The query restricted to the declared organism and gene/locus returns exactly
    Q03406; reviewed filtering is used only for reviewed examples.
  snapshot_sha256: 7368ce9776d8376e6b65508a94e4db0a020b1e79807eee71b6f045dddcbd3721
- evidence_id: root56-sources-protein-Q12488
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12488.json
  locator: Identity/status/names, genes/aliases, organism and family cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:55:14.078490Z'
  support: supports
  summary: 'Q12488: The reviewed gene/taxon identity and native whole-family cross-references
    corroborate the named constituent class.'
  snapshot_sha256: d2bc83c4f49cb856f2fbf59ea40455ddc5180c1d30345c829f945ba34ea5cf42
- evidence_id: root56-sources-gene-PSF1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set and literal native query parameters
  accessed_at: '2026-10-22T06:55:18.612974Z'
  support: supports
  summary: The query restricted to the declared organism and gene/locus returns exactly
    Q12488; reviewed filtering is used only for reviewed examples.
  snapshot_sha256: e80a00344596c83719b3207a5bdf34a416aa42fef76201dfe48cd6f4943922cc
- evidence_id: root56-sources-protein-P40359
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40359.json
  locator: Identity/status/names, genes/aliases, organism and family cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:55:13.162846Z'
  support: supports
  summary: 'P40359: The reviewed gene/taxon identity and native whole-family cross-references
    corroborate the named constituent class.'
  snapshot_sha256: a0372e9adda4d46ee4b088e3bac6455b0dcfa50df134106ee25d61c0a2c82689
- evidence_id: root56-sources-gene-PSF2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set and literal native query parameters
  accessed_at: '2026-10-22T06:55:19.394910Z'
  support: supports
  summary: The query restricted to the declared organism and gene/locus returns exactly
    P40359; reviewed filtering is used only for reviewed examples.
  snapshot_sha256: f623cb2d7331785b5dc3c72117083190c48927b7e740098a750f9d4f52698512
- evidence_id: root56-sources-protein-Q12146
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12146.json
  locator: Identity/status/names, genes/aliases, organism and family cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:55:13.945614Z'
  support: supports
  summary: 'Q12146: The reviewed gene/taxon identity and native whole-family cross-references
    corroborate the named constituent class.'
  snapshot_sha256: 72fc7e1d00fc0c8dee9b0e065a7683decb0c78a9cba00cf8252da2fe27c3bf3c
- evidence_id: root56-sources-gene-PSF3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set and literal native query parameters
  accessed_at: '2026-10-22T06:55:19.565582Z'
  support: supports
  summary: The query restricted to the declared organism and gene/locus returns exactly
    Q12146; reviewed filtering is used only for reviewed examples.
  snapshot_sha256: d7cd7f8989fc603bab14abc9c2d052cb1bd46a9090022b39abba5a11cdaf1887
- evidence_id: root56-sources-ipr-IPR008591
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008591/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:55:53.838713Z'
  support: supports
  summary: Exact whole-family identity for Sld5; the corresponding reviewed yeast
    example independently carries this cross-reference. Generic old clamp/helicase
    prose is not treated as a direct catalytic experiment.
  snapshot_sha256: 85e8cd86a991862236bac423a4b78a8657b441ab90bfc81b4db9fe4962302caf
- evidence_id: root56-sources-ipr-IPR005339
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005339/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:55:54.359060Z'
  support: supports
  summary: Exact whole-family identity for Psf1; the corresponding reviewed yeast
    example independently carries this cross-reference. Generic old clamp/helicase
    prose is not treated as a direct catalytic experiment.
  snapshot_sha256: 121f89ec73f3f03cd822ae44de3d8f88b8d0c03e2d0cace8bdbec8dc8a758196
- evidence_id: root56-sources-ipr-IPR007257
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007257/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:55:54.433285Z'
  support: supports
  summary: Exact whole-family identity for Psf2; the corresponding reviewed yeast
    example independently carries this cross-reference. Generic old clamp/helicase
    prose is not treated as a direct catalytic experiment.
  snapshot_sha256: da6e464787aa773567fa1b673d8d7428ffc4637302a642144f0fd11d389636a4
- evidence_id: root56-sources-ipr-IPR010492
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010492/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:55:54.953413Z'
  support: supports
  summary: Exact whole-family identity for Psf3; the corresponding reviewed yeast
    example independently carries this cross-reference. Generic old clamp/helicase
    prose is not treated as a direct catalytic experiment.
  snapshot_sha256: fc7bab38aac1ebe05715d0a7a9ff819d2de8abb1c981d9f1813c8064229268eb
- evidence_id: root56-sources-PMC196052-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC196052/
  locator: Results sec2, sec4, sec5, sec6, sec7, sec8 and sec9 in full, including
    embedded Figures 1–7 captions; Methods sec15 and sec20 in full
  accessed_at: '2026-10-22T06:55:56.876660Z'
  support: supports
  summary: Takayama 2003 identifies the four-protein GINS assembly and replication
    roles. In sld5-12 cells at the permissive 23 C, recoverable complex is below one
    fifth of wild type and high-copy PSF2 substantially rescues it. Reduced subunit
    abundance and inferred degradation are distinguished from directly measured coassociation;
    replication defects at restrictive temperatures are separate readouts.
  snapshot_sha256: d4bf96a2f9f6259823d78b1c5464f44419ab0b56728f12593720d1e1e9d39b99
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/gins_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:39Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/gins_complex.yaml'
  snapshot_sha256: 862c3eec3a10e7dab376915f63c9c7e3a3471cbc3c0a7bd431274c971f3d56e2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/gins_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/gins_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:40Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/gins_complex.yaml\
    \ --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/gins_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/gins_complex-strict.tsv"
  snapshot_sha256: 36f4e736bccc5cf9599e2b2d16def62dc6d5f0d9ea427c31fbf462dbe1aa5b99
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gins_complex.yaml --causal-graphs
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:02:48.150689Z'
  support: supports
  summary: "data/structures/other/gins_complex.yaml  (GO:0000811)\n  gins_chromosomal_dna_replication\t\
    sld5_subunit\tCOVERED\t->sld5_subunit (UniProtKB:Q03406)\n  gins_chromosomal_dna_replication\t\
    psf1_subunit\tCOVERED\t->psf1_subunit (UniProtKB:Q12488)\n  gins_chromosomal_dna_replication\t\
    psf2_subunit\tCOVERED\t->psf2_subunit (UniProtKB:P40359)\n  gins_chromosomal_dna_replication\t\
    psf3_subunit\tCOVERED\t->psf3_subunit (UniProtKB:Q12146)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     4  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     4  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 729eaa9be0fbb914f7362e788776bed060b90b9012ffa9f79c6e80d5e96439bf
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gins_complex.yaml --verify
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:02:49.359723Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/gins_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 11 collected target identifiers returned OK. PMID:12730134: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
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
  topic: Four-protein GINS boundary
  outcome: supported
  target_ids:
  - GO:0000811
  summary: GO and tagged-protein purification identify Sld5, Psf1, Psf2 and Psf3 as
    the heterotetramer. The existing resolved boundary correctly keeps Cdc45 and MCM
    outside GINS; origin factors and the broader CMG are adjacent assemblies.
  evidence_ids:
  - record
  - root56-sources-go
  - root56-sources-GO0000811-ancestors
  - root56-sources-PMC196052-html
- assessment_id: composition
  area: grounding
  topic: Four resolved constituent families
  outcome: concern
  target_ids:
  - GO:0000811
  summary: Each label-only class has an exact native whole-family entry, corroborated
    by its reviewed S288C protein and gene query. Shared domains and generic prose
    are not substituted for class identity or primary mechanism.
  evidence_ids:
  - record
  - curation
  - root56-sources-ipr-IPR008591
  - root56-sources-ipr-IPR005339
  - root56-sources-ipr-IPR007257
  - root56-sources-ipr-IPR010492
  - root56-sources-protein-Q03406
  - root56-sources-protein-Q12488
  - root56-sources-protein-P40359
  - root56-sources-protein-Q12146
  - root56-sources-gene-SLD5
  - root56-sources-gene-PSF1
  - root56-sources-gene-PSF2
  - root56-sources-gene-PSF3
- assessment_id: formation
  area: grounding
  topic: Direct conditional complex-recovery result
  outcome: concern
  target_ids:
  - GO:0000811
  summary: The cited primary body directly measures reduced recoverable GINS in sld5-12
    at 23 C and rescue by high-copy PSF2. Generic constituent roles and graph membership
    omit this bounded physical-complex result. The authors could not test psf1-1 complex
    assembly with the attempted tag, so that mutant cannot be assigned the same demonstrated
    phenotype.
  evidence_ids:
  - record
  - schema
  - root56-sources-PMC196052-html
- assessment_id: graph
  area: graph
  topic: Supported composition and DNA-replication function
  outcome: supported
  target_ids:
  - GO:0000811
  summary: All four contributes-to edges and the whole-complex replication edge are
    supported. Origin association, subsequent flanking-sequence association and genetic
    dependencies explain the function without promoting adjacent origin machinery
    to constituents or asserting that GINS alone catalyzes helicase activity.
  evidence_ids:
  - record
  - graphs
  - root56-sources-go
  - root56-sources-PMC196052-html
- assessment_id: scope
  area: scope
  topic: Yeast experimental and reference scope
  outcome: supported
  target_ids:
  - GO:0000811
  summary: The maintained species example is supported. Reviewed S288C accession identities
    are not proof that all experiment strains were S288C; full strain-table details
    remain in the unread supplement. COMMON means present in most members with losses
    as exceptions; this qualitative category is not a measured frequency statistic.
  evidence_ids:
  - record
  - schema
  - root56-sources-PMC196052-html
  - root56-sources-tax-4932
  - root56-sources-tax-559292
  - root56-sources-protein-Q03406
  - root56-sources-protein-Q12488
  - root56-sources-protein-P40359
  - root56-sources-protein-Q12146
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target and bounded follow-up
  outcome: supported
  target_ids:
  - GO:0000811
  summary: Every maintained field, evidence row, component/example, graph edge, discussion
    and history entry was read. Optional unpopulated slots are not defects. Scientific
    status/history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root56-sources-go
  - root56-sources-doi-10.1101_gad.1065903
- assessment_id: formation-necessity
  area: grounding
  topic: Universal individual-constituent formation requirements
  outcome: unknown
  target_ids:
  - GO:0000811
  summary: The bounded physical-association and activity observations assessed above
    do not establish a universal individual-constituent necessity profile for formation
    of this structure. Unspecified requirements remain unknown; they are not presumed
    essential or treated as a new corrective finding.
  evidence_ids:
  - record
  - schema
  - root56-sources-PMC196052-html
findings:
- finding_id: F1
  issue_key: gins-four-exact-subunit-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the four GINS family mappings
  description: The four components and the existing open task still leave exact family
    groundings unresolved. Native whole-family entries and reviewed reference-protein
    cross-references now resolve every named class.
  target_ids:
  - GO:0000811
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - components[2].grounding_status
  - components[3].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root56-sources-ipr-IPR008591
  - root56-sources-ipr-IPR005339
  - root56-sources-ipr-IPR007257
  - root56-sources-ipr-IPR010492
  - root56-sources-protein-Q03406
  - root56-sources-protein-Q12488
  - root56-sources-protein-P40359
  - root56-sources-protein-Q12146
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gins_complex.yaml
    role: maintained scientific record
  rule_id: Exact constituent-class grounding
  native_severity: minor
  normalization_reason: A bounded actionable class mapping under the existing explicit
    task; the complex identity and named protein examples remain supported.
- finding_id: F2
  issue_key: gins-sld5-mutant-complex-recovery
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Capture the conditional GINS recovery and rescue result
  description: The source reports less than one fifth of normal recoverable complex
    in sld5-12 cells at 23 C and substantial high-copy PSF2 rescue. Current roles
    and graph edges give only generic membership despite this directly assayed complex-level
    dependence.
  target_ids:
  - GO:0000811
  field_paths:
  - components[0].role
  - components[2].role
  - causal_graphs[0]
  evidence_ids:
  - record
  - schema
  - graphs
  - root56-sources-PMC196052-html
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gins_complex.yaml
    role: maintained scientific record
  rule_id: Resolvable conditional complex-integrity evidence
  native_severity: minor
  normalization_reason: A bounded missing physical-complex observation in an otherwise
    supported heterotetramer; no complete assembly mechanism is demanded.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0000811
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gins_complex.yaml
    role: maintained scientific record
  description: Ground the four classes and resolve or narrow the existing family task
    while preserving the established GINS versus CMG boundary.
  acceptance_checks:
  - Map Sld5 to IPR008591, Psf1 to IPR005339, Psf2 to IPR007257 and Psf3 to IPR010492.
  - Keep taxon-paired reference examples distinct from exact class identifiers.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0000811
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gins_complex.yaml
    role: maintained scientific record
  description: Add the specifically assayed sld5-12 complex-recovery result and PSF2
    dosage rescue with strain, temperature and purification/readout context.
  acceptance_checks:
  - Distinguish lower recoverable complex and subunit abundance from direct measurement
    of protein degradation.
  - Do not infer complete absence, universal ESSENTIAL for all four proteins, or an
    equivalent psf1-1 assembly result.
  - Separate the permissive-temperature complex assay from restrictive-temperature
    replication/viability assays.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
limitations:
- All five same-base batch26 corpus gates and exact target resolver rows are integrated
  with every manifested input hash verified.
- No figure pixels, raw datasets, sequence alignments, atomic coordinates or supplementary
  files were reanalyzed. Primary body reading is limited to declared sections and
  embedded captions.
- Any absence finding is confined to the complete inspected target and its existing
  task; no claim is made that a related record or identifier is absent from the corpus
  or all databases.
- The supplemental strain table and raw microscopy/gel data were not inspected. Methods
  sec15 and sec20 were read; no claim is made to have read every ChIP protocol detail.
- InterPro description text includes historical clamp suggestions and generic helicase
  wording; these are not adopted as a modern mechanistic conclusion.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations and issue-bearing reviews
  alike.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
