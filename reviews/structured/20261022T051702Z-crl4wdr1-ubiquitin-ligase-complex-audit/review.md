# Crl4wdr1 ubiquitin ligase complex scientific review

- Review: 20261022T051702Z-crl4wdr1-ubiquitin-ligase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:01:11Z
- Finished UTC: 2026-10-22T05:17:02Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The source-bounded CRL4WDR1 association, procyclic scope and intervention graph are supported. One major finding identifies an unrelated protein incorrectly used as the WDR1 example; complete catalytic and localization limits remain appropriate.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph and completeness.

Selection: Target 9 of batch48 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml | maintained | CRL4WDR1 ubiquitin ligase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Focused validator passed. |
| Focused native causal-graphs | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Focused native check passed; identity and biological support assessed independently. |
| Focused native verify | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Focused native check passed; identity and biological support assessed independently. |
| Expression-module applicability | not_applicable | False | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | No maintained expression-module assertion requires this resource. |
| Claim-level scientific review | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | 10 of 11 collected target identifiers returned OK. cellstructuremech:crl4wdr1_ubiquitin_ligase_complex: SKIPPED; Exact frozen target identity has exactly one maintained-record match in the ignored-inclusive local search. This verifies the repository-minted identity without asserting exhaustive external ontology absence. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Source-defined receptor-specific association

identity: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

The custom identity is narrower than Cul4-RING, CLRC and repair heterodimers. Broad parentage follows the source classification while complete catalytic composition remains unresolved. No RING subunit is falsely inserted into the observed association.

### Three bounded constituent classes

grounding: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Cullin4 and DDB1 loci agree with their unreviewed reference accessions. The proposed receptor is identified by its source locus; generic WD40, Cullin and RSE1/DDB1/CPSF1 entries do not resolve exact receptor or scaffold subclasses. Client/marker boundaries remain correct.

### Wrong WDR1 reference example

grounding: concern. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Q582R9 is the distinct Tb927.3.4660 protein, whereas the primary paper defines WDR1 as Tb927.10.15080. Resolution of a real accession does not validate the asserted WDR1 alias. The Cullin/DDB1 loci are ORF names in the current entries, not primary gene names, and the older no-examples TODO has become inconsistent with current rows.

### RNAi does not prove assembly essentiality

grounding: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Growth and organelle defects after receptor depletion do not measure formation of the full complex. UNKNOWN is appropriately retained for all three components.

### Procyclic experimental cells versus reference genome

scope: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

The canonical species entry correctly describes29-13 and Lister427 cultures. TREU927 reference annotations are not the cultured strain, and E.coli/yeast assay hosts are excluded. No unsupported broad presence assertion is added.

### Measured turnover and organelle phenotypes

evidence: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Chase and abundance experiments support turnover regulation. The anti-ubiquitin signal may represent TbPLK or coprecipitated proteins, and overexpression is a phenocopy rather than rescue/epistasis. The maintained function text preserves those distinctions.

### Intervention-to-readout graph

graph: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Every edge originates in WDR1 RNAi. Distinct24-hour chase/staining,24/48-hour abundance and48-hour attachment readouts remain separate. No direct catalytic or exclusive mediation chain is asserted.

### Repair reference identity while preserving catalytic limits

completeness: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

The wrong receptor example is actionable. The explicitly incomplete catalytic assembly, source-specific localization and naming boundary do not justify invented components or a broader mechanistic graph. The captured image is scoped to subunit localization/interaction, not the assembled particle.

## Findings

### F1: Remove or replace the unrelated WDR1 protein example

major / open / confirmed; issue key: crl4wdr1-wrong-receptor-example.

The WDR1 protein_examples row assigns Q582R9/Tb927.3.4660 to WDR1. Hu2017 sec004 explicitly defines WDR1 as Tb927.10.15080. The current native Q582R9 entry and exact-locus query identify the different locus and supply no WDR1 synonym. A zero-result query for the source locus cannot justify selecting another WD-repeat protein. The false correspondence can propagate incorrect receptor identity despite the native identifier validator passing.

## Recommended Actions And Acceptance Checks

### A1

Remove Q582R9 from the WDR1 example unless independent exact-locus/sequence evidence establishes an identity merger; otherwise replace only with a verified source-locus accession. Preserve Q57XW2 and Q586I3 as reference-strain examples, accurately call their identifiers ORF names, and reconcile stale no-examples discussion text. Do not guess a replacement or change the supported source-defined complex.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml; Entire maintained record including history, components, evidence, graph and discussions | context_only | All maintained fields were read. Historical curation notes document earlier decisions rather than independently proving current assertions. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component grounding, formation essentiality, taxonomic presence and graph scope | context_only | Whole-protein families differ from domains and individual examples. Assembly necessity differs from viability or function. COMMON means present in most members, with losses the exception; a qualitative ordinary-machinery assertion need not imply a numerical census. |
| curation | docs/CURATION.md; Exact identities and claim-specific evidence | context_only | A verified component identity and its membership in a complex require distinct support. Reviewed label-only status is reserved for the absence of an exact term; historical deferred searches can be revisited without alleging historical fabrication. |
| root48-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228,GO:0000776,GO:0000817,GO:0003689,GO:0007062,GO:0017119,GO:0031390,GO:0031464,GO:0043494,GO:0048193,GO:0070912,GO:0080008,GO:0099023,GO:0140513; Complete maintained-term identity and definition fields and relevant typed links; not every descendant | supports | All14 requested GO identities, active status, definitions, synonyms, comments and relevant maintained typed relationships were inspected. The custom WDR1-specific assembly is distinct from the broader Cul4 parent. |
| root48-sources-doi-9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.ppat.1006146%22&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED28052114: CRL4WDR1 Controls Polo-like Kinase Protein Abundance to Promote Bilobe Duplication, Basal Body Segregation and Flagellum Attachment in Trypanosoma brucei. DOI 10.1371/journal.ppat.1006146. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root48-sources-doi-3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41598-025-32077-9%22&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED41413177: Evolution, composition and functions of cullin E3 ubiquitin ligases in trypanosomes. DOI 10.1038/s41598-025-32077-9. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root48-sources-protein-Q57XW2 | https://rest.uniprot.org/uniprotkb/Q57XW2.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native Q57XW2 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-Q586I3 | https://rest.uniprot.org/uniprotkb/Q586I3.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native Q586I3 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-Q582R9 | https://rest.uniprot.org/uniprotkb/Q582R9.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native Q582R9 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-tax185431 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/185431; Complete native taxonomy response | supports | Native taxon 185431 name, rank, lineage and synonym data inspected. Reference strains are distinguished from experimental strains. |
| root48-sources-tax5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Complete native taxonomy response | supports | Native taxon 5691 name, rank, lineage and synonym data inspected. Reference strains are distinguished from experimental strains. |
| root48-sources-ipr-IPR045093 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045093/; Complete accession/name/type/description, hierarchy, integrated signatures and curation flags | supports | IPR045093 is classified as family and named Cullin. Native metadata, full description and curation flags inspected. This row supports identity scope, not an independent primary biological experiment. |
| root48-sources-ipr-IPR050358 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050358/; Complete accession/name/type/description, hierarchy, integrated signatures and curation flags | supports | IPR050358 is classified as family and named RSE1/DDB1/CPSF1. Native metadata, full description and curation flags inspected. This row supports identity scope, not an independent primary biological experiment. |
| root48-sources-locus-Tb927.3.1290 | https://rest.uniprot.org/uniprotkb/search?query=Tb927.3.1290+AND+organism_id%3A185431&amp;format=json&amp;size=25; Complete query URL and every returned accession/name/ORF/taxon | supports | The exact locus/taxon query returns Q57XW2 with ORF Tb927.3.1290, matching the maintained Cullin reference. |
| root48-sources-locus-Tb927.6.5110 | https://rest.uniprot.org/uniprotkb/search?query=Tb927.6.5110+AND+organism_id%3A185431&amp;format=json&amp;size=25; Complete query URL and every returned accession/name/ORF/taxon | supports | The exact locus/taxon query returns Q586I3 with ORF Tb927.6.5110, matching the maintained DDB1 reference. |
| root48-sources-locus-Tb927.3.4660 | https://rest.uniprot.org/uniprotkb/search?query=Tb927.3.4660+AND+organism_id%3A185431&amp;format=json&amp;size=25; Complete query URL and every returned accession/name/ORF/taxon | supports | The exact locus/taxon query returns Q582R9 with ORF Tb927.3.4660; this is the accession currently misassigned to WDR1. |
| root48-sources-locus-Tb927.10.15080 | https://rest.uniprot.org/uniprotkb/search?query=Tb927.10.15080+AND+organism_id%3A185431&amp;format=json&amp;size=25; Complete query URL and every returned accession/name/ORF/taxon | supports | The exact source-locus/taxon query returns zero results. This bounded search does not establish biological absence or justify a substitute identity. |
| root48-sources-hu2017-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC5241021/?_escaped_fragment_=; Complete Results sec004-sec008, Discussion sec009, Methods sec011/sec013-sec017, embedded Figures2-8 captions; no root figure-pixel or supplementary-data reanalysis | supports | WDR1 is explicitly Tb927.10.15080. Endogenous co-isolation supports the named Cullin4-DDB1-WDR1 association; client TbPLK and markers are not invariant constituents. RNAi chase, unresolved anti-ubiquitin immunoprecipitate and organelle outputs are distinguished from direct purified catalysis. The model extends beyond the measured mediation. Procyclic29-13/Lister427 and recombinant/yeast assay hosts are separated. |
| root48-sources-cullins2025-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC12816148/?_escaped_fragment_=; Complete Table1, Results Sec5/Sec6, Discussion Sec10 and Methods Sec12; no full proteomic tables or raw data | supports | Table1 maps Tb927.3.1290 to TbCul-D with DDB1/Rbx1 and DCAFs. Discussion attributes older PLK results to Cul-E despite its distinct locus. The record correctly prioritizes exact locus identity and avoids importing all scaffold-isolation interactors into the WDR1-specific assembly. |
| root48-sources-go-name-CRL4WDR1 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=CRL4WDR1&amp;limit=25; Complete name query and result count/results | supports | Bounded current GO name search returns zero hits. This supports retaining the specific local identifier alongside the verified broader parent without claiming exhaustive ontology absence. |
| root48-sources-go-name-WDR1 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=WDR1&amp;limit=25; Complete name query and result count/results | supports | Bounded current GO name search returns zero hits. This supports retaining the specific local identifier alongside the verified broader parent without claiming exhaustive ontology absence. |
| schema-result | just validate data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml |
| strict-result | just validate-strict data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/crl4wdr1_ubiquitin_ligase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/crl4wdr1_ubiquitin_ligase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch48-20261022-ppyyf64c/crl4wdr1_ubiquitin_ligase_complex-strict.tsv |
| native-crl4wdr1_ubiquitin_ligase_complex-causal-graphs | /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml; Complete focused native report | supports | data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml  (cellstructuremech:crl4wdr1_ubiquitin_ligase_complex)<br>  wdr1_depletion_outputs	wdr1	COVERED	-&gt;wdr1 (UniProtKB:Q582R9)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-crl4wdr1_ubiquitin_ligase_complex-verify | /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 11 collected target identifiers returned OK. cellstructuremech:crl4wdr1_ubiquitin_ligase_complex: SKIPPED; Exact frozen target identity has exactly one maintained-record match in the ignored-inclusive local search. This verifies the repository-minted identity without asserting exhaustive external ontology absence. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Primary-body reading is limited to the sections explicitly named. No raw experimental data, supplementary datasets or sequence alignments were reanalyzed.
- The exact WDR1 source-locus UniProt query returned zero; no replacement accession or exhaustive biological absence is asserted. Root read figure captions only; independent image-pixel and licence checks are recorded by the peer reviewer.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes all uncovered reviews, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T051702Z-crl4wdr1-ubiquitin-ligase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Crl4wdr1 ubiquitin ligase complex scientific review
started_at: '2026-10-22T05:01:11Z'
finished_at: '2026-10-22T05:17:02Z'
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
summary: The source-bounded CRL4WDR1 association, procyclic scope and intervention
  graph are supported. One major finding identifies an unrelated protein incorrectly
  used as the WDR1 example; complete catalytic and localization limits remain appropriate.
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
  - path: data/images/other/crl4wdr1_ubiquitin_ligase_complex/pmc5241021_ppat_1006146_g002_04eab535.jpg
    sha256: 670801001c1d236247e8901451b48538d1b444bbeddde152500be4273d75cc62
    role: context
  - path: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    sha256: 15951ee1c5321044ae8654b108d88de8388e09c2d10706fc7134d5ba32280ac4
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
- target_id: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  path: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  label: CRL4WDR1 ubiquitin ligase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph and completeness.
  selection: Target 9 of batch48 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: just validate data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: just validate-strict data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/crl4wdr1_ubiquitin_ligase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-crl4wdr1_ubiquitin_ligase_complex-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  exit_code: 0
  summary: Focused native check passed; identity and biological support assessed independently.
  evidence_ids:
  - native-crl4wdr1_ubiquitin_ligase_complex-causal-graphs
- check_id: native-crl4wdr1_ubiquitin_ligase_complex-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  exit_code: 0
  summary: Focused native check passed; identity and biological support assessed independently.
  evidence_ids:
  - native-crl4wdr1_ubiquitin_ligase_complex-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: No maintained expression-module assertion requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root48-sources-go
  - root48-sources-doi-9
  - root48-sources-doi-3
  - root48-sources-protein-Q57XW2
  - root48-sources-protein-Q586I3
  - root48-sources-protein-Q582R9
  - root48-sources-tax185431
  - root48-sources-tax5691
  - root48-sources-ipr-IPR045093
  - root48-sources-ipr-IPR050358
  - root48-sources-locus-Tb927.3.1290
  - root48-sources-locus-Tb927.6.5110
  - root48-sources-locus-Tb927.3.4660
  - root48-sources-locus-Tb927.10.15080
  - root48-sources-hu2017-legacy
  - root48-sources-cullins2025-legacy
  - root48-sources-go-name-CRL4WDR1
  - root48-sources-go-name-WDR1
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: '10 of 11 collected target identifiers returned OK. cellstructuremech:crl4wdr1_ubiquitin_ligase_complex:
    SKIPPED; Exact frozen target identity has exactly one maintained-record match
    in the ignored-inclusive local search. This verifies the repository-minted identity
    without asserting exhaustive external ontology absence. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch48 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch48 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch48 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch48 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
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
    and current batch48 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  locator: Entire maintained record including history, components, evidence, graph
    and discussions
  accessed_at: '2026-10-22T05:13:38Z'
  support: context_only
  summary: All maintained fields were read. Historical curation notes document earlier
    decisions rather than independently proving current assertions.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component grounding, formation essentiality, taxonomic presence and graph
    scope
  accessed_at: '2026-10-22T05:13:38Z'
  support: context_only
  summary: Whole-protein families differ from domains and individual examples. Assembly
    necessity differs from viability or function. COMMON means present in most members,
    with losses the exception; a qualitative ordinary-machinery assertion need not
    imply a numerical census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identities and claim-specific evidence
  accessed_at: '2026-10-22T05:13:38Z'
  support: context_only
  summary: A verified component identity and its membership in a complex require distinct
    support. Reviewed label-only status is reserved for the absence of an exact term;
    historical deferred searches can be revisited without alleging historical fabrication.
- evidence_id: root48-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228,GO:0000776,GO:0000817,GO:0003689,GO:0007062,GO:0017119,GO:0031390,GO:0031464,GO:0043494,GO:0048193,GO:0070912,GO:0080008,GO:0099023,GO:0140513
  locator: Complete maintained-term identity and definition fields and relevant typed
    links; not every descendant
  accessed_at: '2026-10-22T05:04:22.473075Z'
  support: supports
  summary: All14 requested GO identities, active status, definitions, synonyms, comments
    and relevant maintained typed relationships were inspected. The custom WDR1-specific
    assembly is distinct from the broader Cul4 parent.
  snapshot_sha256: d286c944be8950cb0f8aaf019fb391dc88abed2d978bb77bf24beba14a2ea670
- evidence_id: root48-sources-doi-9
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.ppat.1006146%22&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:04:29.744570Z'
  support: supports
  summary: 'MED28052114: CRL4WDR1 Controls Polo-like Kinase Protein Abundance to Promote
    Bilobe Duplication, Basal Body Segregation and Flagellum Attachment in Trypanosoma
    brucei. DOI 10.1371/journal.ppat.1006146. Complete bibliographic identity and
    abstract inspected; full-body access is certified only in separate evidence rows.'
  snapshot_sha256: 6315391006d877c6a628567d08585d34fb06f79180ac9bf13511662f9fe8ca11
- evidence_id: root48-sources-doi-3
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41598-025-32077-9%22&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:04:28.961898Z'
  support: supports
  summary: 'MED41413177: Evolution, composition and functions of cullin E3 ubiquitin
    ligases in trypanosomes. DOI 10.1038/s41598-025-32077-9. Complete bibliographic
    identity and abstract inspected; full-body access is certified only in separate
    evidence rows.'
  snapshot_sha256: 299cdbc60e0412c42be121a6e7125d3f6cf20d3ac8b64fe52745cdd50dbbebe8
- evidence_id: root48-sources-protein-Q57XW2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q57XW2.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:27.444477Z'
  support: supports
  summary: Native Q57XW2 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: 78db9b34f405b2f858702f27f90bfde6d3566d76ff0b64c30f67e683f1d5986d
- evidence_id: root48-sources-protein-Q586I3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q586I3.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:28.232018Z'
  support: supports
  summary: Native Q586I3 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: a81a6676d30c9b48c4928f035c773afe6ec0796da3bf3200874db9ff2218fd3c
- evidence_id: root48-sources-protein-Q582R9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q582R9.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:27.557371Z'
  support: supports
  summary: Native Q582R9 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: ec71b42e2b1085758d23efa606c6d89e6fcd869b073b1e63fb8023d09d67a6ff
- evidence_id: root48-sources-tax185431
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/185431
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:04:22.473466Z'
  support: supports
  summary: Native taxon 185431 name, rank, lineage and synonym data inspected. Reference
    strains are distinguished from experimental strains.
  snapshot_sha256: 37f4acd608d79bb144d706335e37a83a0f97a94595aca5175855c8c390ec652d
- evidence_id: root48-sources-tax5691
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:04:22.475003Z'
  support: supports
  summary: Native taxon 5691 name, rank, lineage and synonym data inspected. Reference
    strains are distinguished from experimental strains.
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: root48-sources-ipr-IPR045093
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045093/
  locator: Complete accession/name/type/description, hierarchy, integrated signatures
    and curation flags
  accessed_at: '2026-10-22T05:04:28.263384Z'
  support: supports
  summary: IPR045093 is classified as family and named Cullin. Native metadata, full
    description and curation flags inspected. This row supports identity scope, not
    an independent primary biological experiment.
  snapshot_sha256: 3c1fabca973d9704f4e57ccb886f8ae6284079c9178bdf627cccc8bb35bac5aa
- evidence_id: root48-sources-ipr-IPR050358
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050358/
  locator: Complete accession/name/type/description, hierarchy, integrated signatures
    and curation flags
  accessed_at: '2026-10-22T05:04:28.354309Z'
  support: supports
  summary: IPR050358 is classified as family and named RSE1/DDB1/CPSF1. Native metadata,
    full description and curation flags inspected. This row supports identity scope,
    not an independent primary biological experiment.
  snapshot_sha256: 36bb37346da7eabcb9f53419d1b173337dea419712be8c8a3828a6feb7100c3e
- evidence_id: root48-sources-locus-Tb927.3.1290
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=Tb927.3.1290+AND+organism_id%3A185431&format=json&size=25
  locator: Complete query URL and every returned accession/name/ORF/taxon
  accessed_at: '2026-10-22T05:06:22.577962Z'
  support: supports
  summary: The exact locus/taxon query returns Q57XW2 with ORF Tb927.3.1290, matching
    the maintained Cullin reference.
  snapshot_sha256: 1a2410deca1e1ec80f0aa0a74d5063eb4668cc57b68b3e5081e5fb570ea11064
- evidence_id: root48-sources-locus-Tb927.6.5110
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=Tb927.6.5110+AND+organism_id%3A185431&format=json&size=25
  locator: Complete query URL and every returned accession/name/ORF/taxon
  accessed_at: '2026-10-22T05:06:22.601392Z'
  support: supports
  summary: The exact locus/taxon query returns Q586I3 with ORF Tb927.6.5110, matching
    the maintained DDB1 reference.
  snapshot_sha256: 09ed2918b0fa6005a4d455930fe01739b3a31ea0cc11c85bfdd6177475fbcc0e
- evidence_id: root48-sources-locus-Tb927.3.4660
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=Tb927.3.4660+AND+organism_id%3A185431&format=json&size=25
  locator: Complete query URL and every returned accession/name/ORF/taxon
  accessed_at: '2026-10-22T05:06:22.553092Z'
  support: supports
  summary: The exact locus/taxon query returns Q582R9 with ORF Tb927.3.4660; this
    is the accession currently misassigned to WDR1.
  snapshot_sha256: c9ce65743ceceebc4b423fc982ee1b1b05f1fce382991e935b2d5e5219940d8e
- evidence_id: root48-sources-locus-Tb927.10.15080
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=Tb927.10.15080+AND+organism_id%3A185431&format=json&size=25
  locator: Complete query URL and every returned accession/name/ORF/taxon
  accessed_at: '2026-10-22T05:06:21.834418Z'
  support: supports
  summary: The exact source-locus/taxon query returns zero results. This bounded search
    does not establish biological absence or justify a substitute identity.
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
- evidence_id: root48-sources-hu2017-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5241021/?_escaped_fragment_=
  locator: Complete Results sec004-sec008, Discussion sec009, Methods sec011/sec013-sec017,
    embedded Figures2-8 captions; no root figure-pixel or supplementary-data reanalysis
  accessed_at: '2026-10-22T05:06:26.252895Z'
  support: supports
  summary: WDR1 is explicitly Tb927.10.15080. Endogenous co-isolation supports the
    named Cullin4-DDB1-WDR1 association; client TbPLK and markers are not invariant
    constituents. RNAi chase, unresolved anti-ubiquitin immunoprecipitate and organelle
    outputs are distinguished from direct purified catalysis. The model extends beyond
    the measured mediation. Procyclic29-13/Lister427 and recombinant/yeast assay hosts
    are separated.
  snapshot_sha256: 9fa8977198676a6de79e1076f47b9b4cc559f2f9d56a92e1cd48eba26c371a98
- evidence_id: root48-sources-cullins2025-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC12816148/?_escaped_fragment_=
  locator: Complete Table1, Results Sec5/Sec6, Discussion Sec10 and Methods Sec12;
    no full proteomic tables or raw data
  accessed_at: '2026-10-22T05:06:26.391432Z'
  support: supports
  summary: Table1 maps Tb927.3.1290 to TbCul-D with DDB1/Rbx1 and DCAFs. Discussion
    attributes older PLK results to Cul-E despite its distinct locus. The record correctly
    prioritizes exact locus identity and avoids importing all scaffold-isolation interactors
    into the WDR1-specific assembly.
  snapshot_sha256: a9128c1eeb9cc873a09188b50029ef58a7f99e0d7c83b77281bfe4bb9dfc05a9
- evidence_id: root48-sources-go-name-CRL4WDR1
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=CRL4WDR1&limit=25
  locator: Complete name query and result count/results
  accessed_at: '2026-10-22T05:07:11.579720Z'
  support: supports
  summary: Bounded current GO name search returns zero hits. This supports retaining
    the specific local identifier alongside the verified broader parent without claiming
    exhaustive ontology absence.
  snapshot_sha256: 4f0027cdf6df79bb6d4e90297666e971eb23ca7cfa19fc11fb9c9931fd5f1004
- evidence_id: root48-sources-go-name-WDR1
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=WDR1&limit=25
  locator: Complete name query and result count/results
  accessed_at: '2026-10-22T05:07:12.309570Z'
  support: supports
  summary: Bounded current GO name search returns zero hits. This supports retaining
    the specific local identifier alongside the verified broader parent without claiming
    exhaustive ontology absence.
  snapshot_sha256: 4f0027cdf6df79bb6d4e90297666e971eb23ca7cfa19fc11fb9c9931fd5f1004
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:01:12Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml'
  snapshot_sha256: 9d620acb7b8bf759ba2a0039a0c8bddb6e452756143411566fe72133a766ef93
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/crl4wdr1_ubiquitin_ligase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:01:13Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/crl4wdr1_ubiquitin_ligase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch48-20261022-ppyyf64c/crl4wdr1_ubiquitin_ligase_complex-strict.tsv"
  snapshot_sha256: 13cd98b176f3e0e6d956fe29e8af98d768c4ed6583fcf2f6e6273fe22c477199
- evidence_id: native-crl4wdr1_ubiquitin_ligase_complex-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:06:16.779429Z'
  support: supports
  summary: "data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml  (cellstructuremech:crl4wdr1_ubiquitin_ligase_complex)\n\
    \  wdr1_depletion_outputs\twdr1\tCOVERED\t->wdr1 (UniProtKB:Q582R9)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     1  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     1  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: fdf9c3bef748b6f4560e6e8ce8dde3a92ebb0e08a8417f04075ecc5a770c3b18
- evidence_id: native-crl4wdr1_ubiquitin_ligase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:06:18.039967Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 11 collected target identifiers returned OK. cellstructuremech:crl4wdr1_ubiquitin_ligase_complex:
    SKIPPED; Exact frozen target identity has exactly one maintained-record match
    in the ignored-inclusive local search. This verifies the repository-minted identity
    without asserting exhaustive external ontology absence. Native source checks are
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
  topic: Source-defined receptor-specific association
  outcome: supported
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: The custom identity is narrower than Cul4-RING, CLRC and repair heterodimers.
    Broad parentage follows the source classification while complete catalytic composition
    remains unresolved. No RING subunit is falsely inserted into the observed association.
  evidence_ids:
  - record
  - root48-sources-go
  - root48-sources-hu2017-legacy
  - root48-sources-cullins2025-legacy
  - root48-sources-go-name-CRL4WDR1
  - root48-sources-go-name-WDR1
- assessment_id: composition
  area: grounding
  topic: Three bounded constituent classes
  outcome: supported
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: Cullin4 and DDB1 loci agree with their unreviewed reference accessions.
    The proposed receptor is identified by its source locus; generic WD40, Cullin
    and RSE1/DDB1/CPSF1 entries do not resolve exact receptor or scaffold subclasses.
    Client/marker boundaries remain correct.
  evidence_ids:
  - record
  - root48-sources-hu2017-legacy
  - root48-sources-cullins2025-legacy
  - root48-sources-protein-Q57XW2
  - root48-sources-protein-Q586I3
  - root48-sources-protein-Q582R9
  - root48-sources-ipr-IPR045093
  - root48-sources-ipr-IPR050358
- assessment_id: examples
  area: grounding
  topic: Wrong WDR1 reference example
  outcome: concern
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: Q582R9 is the distinct Tb927.3.4660 protein, whereas the primary paper
    defines WDR1 as Tb927.10.15080. Resolution of a real accession does not validate
    the asserted WDR1 alias. The Cullin/DDB1 loci are ORF names in the current entries,
    not primary gene names, and the older no-examples TODO has become inconsistent
    with current rows.
  evidence_ids:
  - record
  - root48-sources-hu2017-legacy
  - root48-sources-protein-Q57XW2
  - root48-sources-protein-Q586I3
  - root48-sources-protein-Q582R9
  - root48-sources-locus-Tb927.3.1290
  - root48-sources-locus-Tb927.6.5110
  - root48-sources-locus-Tb927.3.4660
  - root48-sources-locus-Tb927.10.15080
- assessment_id: necessity
  area: grounding
  topic: RNAi does not prove assembly essentiality
  outcome: supported
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: Growth and organelle defects after receptor depletion do not measure formation
    of the full complex. UNKNOWN is appropriately retained for all three components.
  evidence_ids:
  - record
  - schema
  - root48-sources-hu2017-legacy
- assessment_id: scope
  area: scope
  topic: Procyclic experimental cells versus reference genome
  outcome: supported
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: The canonical species entry correctly describes29-13 and Lister427 cultures.
    TREU927 reference annotations are not the cultured strain, and E.coli/yeast assay
    hosts are excluded. No unsupported broad presence assertion is added.
  evidence_ids:
  - record
  - root48-sources-hu2017-legacy
  - root48-sources-cullins2025-legacy
  - root48-sources-tax185431
  - root48-sources-tax5691
- assessment_id: functions
  area: evidence
  topic: Measured turnover and organelle phenotypes
  outcome: supported
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: Chase and abundance experiments support turnover regulation. The anti-ubiquitin
    signal may represent TbPLK or coprecipitated proteins, and overexpression is a
    phenocopy rather than rescue/epistasis. The maintained function text preserves
    those distinctions.
  evidence_ids:
  - record
  - root48-sources-hu2017-legacy
- assessment_id: graph
  area: graph
  topic: Intervention-to-readout graph
  outcome: supported
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: Every edge originates in WDR1 RNAi. Distinct24-hour chase/staining,24/48-hour
    abundance and48-hour attachment readouts remain separate. No direct catalytic
    or exclusive mediation chain is asserted.
  evidence_ids:
  - record
  - root48-sources-hu2017-legacy
- assessment_id: coverage
  area: completeness
  topic: Repair reference identity while preserving catalytic limits
  outcome: supported
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  summary: The wrong receptor example is actionable. The explicitly incomplete catalytic
    assembly, source-specific localization and naming boundary do not justify invented
    components or a broader mechanistic graph. The captured image is scoped to subunit
    localization/interaction, not the assembled particle.
  evidence_ids:
  - record
  - root48-sources-hu2017-legacy
  - root48-sources-cullins2025-legacy
  - root48-sources-protein-Q57XW2
  - root48-sources-protein-Q586I3
  - root48-sources-protein-Q582R9
findings:
- finding_id: F1
  issue_key: crl4wdr1-wrong-receptor-example
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Remove or replace the unrelated WDR1 protein example
  description: The WDR1 protein_examples row assigns Q582R9/Tb927.3.4660 to WDR1.
    Hu2017 sec004 explicitly defines WDR1 as Tb927.10.15080. The current native Q582R9
    entry and exact-locus query identify the different locus and supply no WDR1 synonym.
    A zero-result query for the source locus cannot justify selecting another WD-repeat
    protein. The false correspondence can propagate incorrect receptor identity despite
    the native identifier validator passing.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  field_paths:
  - components#wdr1.protein_examples
  - discussions#component_families_and_examples
  evidence_ids:
  - record
  - root48-sources-hu2017-legacy
  - root48-sources-protein-Q57XW2
  - root48-sources-protein-Q586I3
  - root48-sources-protein-Q582R9
  - root48-sources-locus-Tb927.3.1290
  - root48-sources-locus-Tb927.6.5110
  - root48-sources-locus-Tb927.3.4660
  - root48-sources-locus-Tb927.10.15080
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: major
  normalization_reason: A wrong protein example identifies a different locus and can
    propagate incorrect biological identity.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    role: maintained scientific record
  description: Remove Q582R9 from the WDR1 example unless independent exact-locus/sequence
    evidence establishes an identity merger; otherwise replace only with a verified
    source-locus accession. Preserve Q57XW2 and Q586I3 as reference-strain examples,
    accurately call their identifiers ORF names, and reconcile stale no-examples discussion
    text. Do not guess a replacement or change the supported source-defined complex.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Primary-body reading is limited to the sections explicitly named. No raw experimental
  data, supplementary datasets or sequence alignments were reanalyzed.
- The exact WDR1 source-locus UniProt query returned zero; no replacement accession
  or exhaustive biological absence is asserted. Root read figure captions only; independent
  image-pixel and licence checks are recorded by the peer reviewer.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorizes all uncovered reviews, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
