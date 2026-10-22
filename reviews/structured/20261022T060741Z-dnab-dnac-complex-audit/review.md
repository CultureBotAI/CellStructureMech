# Source-backed review of dnab dnac complex

- Review: 20261022T060741Z-dnab-dnac-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:50:55Z
- Finished UTC: 2026-10-22T06:07:41Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One grouped minor exact DnaB/DnaC family-grounding gap. Loader identity, hexameric DnaB, delivery function and deliberately unresolved DnaC occupancy are supported; formation necessity remains unknown.

## Scope And Provenance

Exactly one complete maintained target plus frozen governing/schema/protein/graph guidance. No neighboring maintained record supplies scientific evidence. All current claims were assessed at the explicitly read authority/primary tiers.

Selection: Batch52 strict ordered selection, index 5; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990100 | data/structures/other/dnab_dnac_complex.yaml | maintained | DnaB-DnaC complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990100 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990100 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:1990100 | Focused check passed; biological scope independently assessed. |
| Focused native verify | failed | False | GO:1990100 | Executed sandbox verification failed because network DNS was unavailable; optional historic attempt retained and superseded by successful network retry. |
| Focused native verify network retry | passed | True | GO:1990100 | Focused check passed; biological scope independently assessed. |
| Claim-level scientific review | passed | True | GO:1990100 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990100 | 8 of 9 collected target identifiers returned OK. PMID:20129058: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990100 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990100 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990100 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990100 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990100 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Loader complex and hierarchy

identity: supported. Targets: GO:1990100.

The DnaB-DnaC multiprotein complex, broad/narrow synonyms and direct protein-containing-complex parent are correct. Separate DNA-bound loading intermediates are experimental context, not a requirement to retype the isolated protein complex.

### Subunits and exact family distinction

grounding: concern. Targets: GO:1990100.

Hexameric DnaB and DnaC loading roles are supported. Exact IPR007692 and NCBIfamNF005931 resolve the two existing protein classes; broad IPR028350 and the IstB-like ATP-binding domain do not. Reference entries and exact query results agree.

### DnaC occupancy remains unresolved at class level

quantity: supported. Targets: GO:1990100.

Six DnaB copies are supported. Leaving DnaC count unset is appropriate: the paper infers3 per hexamer from its oriC complex but explicitly discusses6:6 and does not exclude other ratios. The narrow synonyms are not conflicting assertions of a single invariant count.

### Delivery versus helicase activation

evidence: supported. Targets: GO:1990100.

Source support for DnaC-mediated DnaB delivery and initiation is direct. Mutant complexes can physically load DnaB yet be inactive, and primase/ribonucleotide conditions control DnaC release. Activity failure is not equated with absence of formation.

### Formation necessity remains unknown

evidence: unknown. Targets: GO:1990100.

Every existing component essentiality is UNKNOWN. Source-supported participation, catalytic effects, viability and condition-specific complex recovery do not automatically establish universal structure-formation necessity. The present unknown labels are retained.

### Verified native protein identities and query scope

grounding: supported. Targets: GO:1990100.

All maintained accessions, genes, reviewed status and K12 taxon pairs agree with native responses; single-entry claims are checked against actual query results. Gene taxonomy and exact-organism queries remain distinguished. Optional extra protein examples are not required.

### Species scope and COMMON semantics

scope: supported. Targets: GO:1990100.

E.coli and K12 identities are exact. COMMON retains its schema meaning present in most members with exceptional losses; the cited E.coli experimental systems give qualitative support, not a measured species census. Phage substrate or recombinant conditions do not change the bacterial source taxon.

### Nonmechanistic graph with explicit limits

graph: supported. Targets: GO:1990100.

The graph is explicitly NONMECHANISTIC and uses typed protein/complex/DNA/process nodes. Its qualitative membership/scaffold/initiation relations are supported without imposing a detailed kinetic or loading mechanism.

### Complete single-target assessment

completeness: supported. Targets: GO:1990100.

All maintained fields, citations, component states, protein annotations, graph edges, discussions and history were reviewed. Exact actionable mappings are separated from unestablished optional enrichment; historical access/curation notes are preserved. No source beyond the declared reading tier is certified.

## Findings

### F1: Resolve verified existing component-class groundings

minor / open / confirmed; issue key: dnab-dnac-complex-exact-component-groundings.

DnaB exactly maps to InterProIPR007692 and DnaC to the unintegrated but exact NCBIfamNF005931. Broad DnaC/IstBIPR028350 is not the proposed match. Native family/ontology identities plus independently inspected protein cross-references establish the matches. The current reviewed-label-only/open-task representation leaves these actionable classes unresolved. Historical earlier-pass statements are not declared false merely because current verification is available.

## Recommended Actions And Acceptance Checks

### A1

Add the verified exact class CURIEs with source-specific evidence, update the corresponding grounding states/open task, and preserve organism accessions as examples. Do not force a broader homolog/domain or unresolved PAS-DNA mapping.

- Every added CURIE denotes the existing class at the stated scope, not an individual species protein.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dnab_dnac_complex.yaml; Entire current YAML, all scientific fields, protein annotations, graph and discussion/history | context_only | The complete target was read. No neighboring maintained record supplies an unstated scientific premise. |
| curation | docs/CURATION.md; Component class grounding and formation necessity | context_only | REVIEWED_LABEL_ONLY means no exact class can be asserted after review; protein examples are not family classes. Essentiality concerns structure formation, separately from catalytic activity or viability. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentGroundingStatusEnum; EssentialityEnum; PresenceEnum | context_only | NCBIfam is an allowed source-neutral family prefix. COMMON means present in most taxon members with exceptional losses; UNKNOWN preserves unestablished formation necessity. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope and edge evidence | context_only | A descriptive composition/function graph may remain NONMECHANISTIC; exact node types and source-supported experimental context must be preserved. |
| micro52-go-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990101,GO:1990100,GO:1990158,GO:1990102,GO:1990077,GO:1990099,GO:0032991,GO:0031297,GO:0006270,GO:1990157,GO:1990160; Eleven-term native response: exact target identity/definition/synonyms/xrefs plus relevant typed parent children and function/boundary terms. Unrelated generic complex children are not used as scientific evidence. | supports | Active GO1990100 defines the DnaB hexamer plus DnaC loader, with both6:3 and6:6 narrow synonyms and broad helicase-loading synonym. GO0032991 typed children include the target is_a; GO1990077 supplies separate part_of context. GO0006270 is DNA replication initiation. |
| micro52-GO1990100-ancestors-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990100/ancestors?relations=is_a; Complete ancestors array, relations=is_a; no part_of relation is inferred from this array. | supports | The exact is_a-only ancestor response confirms protein-containing-complex ancestry; this response does not make the isolated loader a DNA-containing complex. |
| micro52-GO1990100-constraints-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990100/constraints; Exact taxonConstraints array; inherited NOT annotation blacklist not used for prevalence. | supports | The exact restriction is only_in_taxon Prokaryota, represented as the Bacteria2/Archaea2157 union. This is an ontology taxon bound, not experimental proof of occurrence in either entire domain. |
| micro52-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete taxId/scientificName/rank/lineage/otherNames native response. | supports | ENA taxId562 identifies Escherichia coli, rank species. |
| micro52-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete taxId/scientificName/rank/lineage/otherNames native response. | supports | ENA taxId83333 identifies Escherichia coli K-12, rank strain. Reference-entry taxon is not silently equated with every experimental derivative. |
| micro52-pmid-20129058 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20129058+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry: exact PMID/title/authors/year/DOI and complete abstractText. Main-body extents, when inspected, are separate. | supports | PMID20129058: Primase directs the release of DnaC from DnaB. Makowska-Grzyska M, Kaguni JM. (2010), DOI10.1016/j.molcel.2009.12.031. Complete native abstract and bibliographic identity read. |
| micro52-protein-P0ACB0 | https://rest.uniprot.org/uniprotkb/P0ACB0.json; Primary accession/status; gene and organism; complete relevant comments and InterPro/NCBIfam cross-references. | supports | Reviewed P0ACB0 is dnaB in E.coli K12 taxon83333. Native identity, names, gene/taxon, full FUNCTION/SUBUNIT/SIMILARITY and available location comments plus family xrefs were read. |
| micro52-gene-dnaB-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual URL query uses taxonomy_id:83333, gene_exact:dnaB, reviewed:true; complete returned identity set. | supports | The bounded reviewed exact-dnaB query returns the single P0ACB0 record. This descendant-inclusive query also confirms the exact83333 returned taxon. |
| micro52-protein-P0AEF0-network | https://rest.uniprot.org/uniprotkb/P0AEF0.json; Primary accession/status; gene and organism; complete relevant comments and InterPro/NCBIfam cross-references. | supports | Reviewed P0AEF0 is dnaC in E.coli K12 taxon83333. Native identity, names, gene/taxon, full FUNCTION/SUBUNIT/SIMILARITY and available location comments plus family xrefs were read. |
| micro52-gene-dnaC-network | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual URL query uses organism_id:83333, gene_exact:dnaC, reviewed:true; complete returned identity set. | supports | The bounded reviewed exact-dnaC query returns the single P0AEF0 record. The query is restricted to exact organism83333. |
| micro52-ipr-IPR007692 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007692/; Full metadata identity/name/type/descriptions and integrated member signatures; generic background stoichiometry/mechanism is not promoted to target-specific evidence. | supports | Native InterPro:IPR007692 is a whole-protein family for the named DnaB-type replicative helicase class, verified by type/name and source signatures. The separate reviewed UniProt response corroborates membership. |
| micro52-ncbifam-NF005931 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF005931/; Full metadata identity/name/type/descriptions and integrated member signatures; generic background stoichiometry/mechanism is not promoted to target-specific evidence. | supports | Native NCBIfam:NF005931 is a whole-protein family for the named DnaC helicase loader class, verified by type/name and source signatures. The separate reviewed UniProt response corroborates membership. This unintegrated NCBIfam member entry is exact; the broader integrated DnaC/IstB group is not substituted. |
| micro52-ipr-IPR028350 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028350/; Complete family name/type/description/PIRSF003073 integration and hierarchy. | supports | IPR028350 includes DnaC and IstB paralogs and is broader than the loader class; it is not proposed as the exact component grounding. |
| micro52-makowska2010-legacy | https://pmc.ncbi.nlm.nih.gov/articles/instance/2819048/; Genuine PMC2819048 HTML: S8–S10, S14–S16, S18/S20/S21 and Figure5–7 captions. Original retained body also read at S1 during B51; no supplement TableS1, raw pixels or new structural measurement. | supports | Makowska-Grzyska/Kaguni2010 directly isolates an oriC prepriming intermediate with DnaB/DnaC, distinguishes mutant delivery from subsequent activity and detects primase-plus-ribonucleotide-dependent DnaC loss. Three DnaC per hexamer is a condition-dependent interpretation; other ratios are explicitly not excluded. |
| schema-result | just validate data/structures/other/dnab_dnac_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dnab_dnac_complex.yaml |
| strict-result | just validate-strict data/structures/other/dnab_dnac_complex.yaml --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dnab_dnac_complex.yaml --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml --causal-graphs; Complete focused native read-only report | supports | data/structures/other/dnab_dnac_complex.yaml  (GO:1990100)<br>  dnab_dnac_helicase_loading	dnab_helicase	COVERED	-&gt;dnab_helicase (UniProtKB:P0ACB0)<br>  dnab_dnac_helicase_loading	dnac_helicase_loader	COVERED	-&gt;dnac_helicase_loader (UniProtKB:P0AEF0)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml --verify; Complete focused native read-only report | context_only | Traceback (most recent call last):<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 922, in &lt;module&gt;<br>    raise SystemExit(main())<br>                     ~~~~^^<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 876, in main<br>    return cmd_verify(records)<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 727, in cmd_verify<br>    issues = verify_records(records)<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 616, in verify_records<br>    entries = fetch_entries_by_accession(all_accs) if all_accs else {}<br>              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 169, in fetch_entries_by_accession<br>    for entry in json.loads(_get(url)).get("results", []):<br>                            ~~~~^^^^^<br>  File "/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py", line 134, in _get<br>    raise RuntimeError(f"UniProt unreachable after {RETRIES} attempts: {last}")<br>RuntimeError: UniProt unreachable after 3 attempts: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt; |
| native-verify-network | /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml --verify; Complete focused native read-only report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dnab_dnac_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 9 collected target identifiers returned OK. PMID:20129058: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Makowska body was read at S8–S10/S14–S16/S18/S20/S21 and Figure5–7 captions. Supplement TableS1 and figure pixels were not inspected; exact derivative strains are not invented from the K12 description.
- The review does not turn a3:6 occupancy interpretation into invariant class stoichiometry. Later structural references in native annotations were not independently read as primary bodies.
- Initial sandbox fetch/verification DNS failures and successful public-network retries are retained separately. Exact source URL, original UTC and SHA are preserved for every reused pair.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user requests one review for every unreviewed record, including qualified clean records.
- Native ontology/UniProt/family adapters directly answer these component claims. No iModulonDB dataset is established or used; computational expression-module membership would not prove physical complex formation.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T060741Z-dnab-dnac-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of dnab dnac complex
started_at: '2026-10-22T05:50:55Z'
finished_at: '2026-10-22T06:07:41Z'
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
summary: One grouped minor exact DnaB/DnaC family-grounding gap. Loader identity,
  hexameric DnaB, delivery function and deliberately unresolved DnaC occupancy are
  supported; formation necessity remains unknown.
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
  - path: data/structures/other/dnab_dnac_complex.yaml
    sha256: 049bf3ed905aec42853fdf025e35d4cb71ecd89a7b8b89328042c39491aaa180
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
- target_id: GO:1990100
  path: data/structures/other/dnab_dnac_complex.yaml
  label: DnaB-DnaC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target plus frozen governing/schema/protein/graph
    guidance. No neighboring maintained record supplies scientific evidence. All current
    claims were assessed at the explicitly read authority/primary tiers.
  selection: Batch52 strict ordered selection, index 5; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990100
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: just validate data/structures/other/dnab_dnac_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: just validate-strict data/structures/other/dnab_dnac_complex.yaml --out
    /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; biological scope independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: failed
  required: false
  target_ids:
  - GO:1990100
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml
    --verify
  exit_code: 1
  summary: Executed sandbox verification failed because network DNS was unavailable;
    optional historic attempt retained and superseded by successful network retry.
  evidence_ids:
  - native-verify
- check_id: native-verify-network
  name: Focused native verify network retry
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; biological scope independently assessed.
  evidence_ids:
  - native-verify-network
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990100
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-pmid-20129058
  - micro52-protein-P0ACB0
  - micro52-gene-dnaB-83333
  - micro52-protein-P0AEF0-network
  - micro52-gene-dnaC-network
  - micro52-ipr-IPR007692
  - micro52-ncbifam-NF005931
  - micro52-ipr-IPR028350
  - micro52-makowska2010-legacy
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990100
  summary: '8 of 9 collected target identifiers returned OK. PMID:20129058: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - micro52-pmid-20129058
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990100
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
    and current batch52 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dnab_dnac_complex.yaml
  locator: Entire current YAML, all scientific fields, protein annotations, graph
    and discussion/history
  accessed_at: '2026-10-22T06:02:26Z'
  support: context_only
  summary: The complete target was read. No neighboring maintained record supplies
    an unstated scientific premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component class grounding and formation necessity
  accessed_at: '2026-10-22T06:02:26Z'
  support: context_only
  summary: REVIEWED_LABEL_ONLY means no exact class can be asserted after review;
    protein examples are not family classes. Essentiality concerns structure formation,
    separately from catalytic activity or viability.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentGroundingStatusEnum; EssentialityEnum; PresenceEnum
  accessed_at: '2026-10-22T06:02:26Z'
  support: context_only
  summary: NCBIfam is an allowed source-neutral family prefix. COMMON means present
    in most taxon members with exceptional losses; UNKNOWN preserves unestablished
    formation necessity.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope and edge evidence
  accessed_at: '2026-10-22T06:02:26Z'
  support: context_only
  summary: A descriptive composition/function graph may remain NONMECHANISTIC; exact
    node types and source-supported experimental context must be preserved.
- evidence_id: micro52-go-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990101,GO:1990100,GO:1990158,GO:1990102,GO:1990077,GO:1990099,GO:0032991,GO:0031297,GO:0006270,GO:1990157,GO:1990160
  locator: 'Eleven-term native response: exact target identity/definition/synonyms/xrefs
    plus relevant typed parent children and function/boundary terms. Unrelated generic
    complex children are not used as scientific evidence.'
  accessed_at: '2026-10-22T05:57:40.727722Z'
  support: supports
  summary: Active GO1990100 defines the DnaB hexamer plus DnaC loader, with both6:3
    and6:6 narrow synonyms and broad helicase-loading synonym. GO0032991 typed children
    include the target is_a; GO1990077 supplies separate part_of context. GO0006270
    is DNA replication initiation.
  snapshot_sha256: 190f29d0d4323902a99ad67697d7ec619c52626b213b1e00b2a05055063448bb
- evidence_id: micro52-GO1990100-ancestors-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990100/ancestors?relations=is_a
  locator: Complete ancestors array, relations=is_a; no part_of relation is inferred
    from this array.
  accessed_at: '2026-10-22T05:57:40.728326Z'
  support: supports
  summary: The exact is_a-only ancestor response confirms protein-containing-complex
    ancestry; this response does not make the isolated loader a DNA-containing complex.
  snapshot_sha256: 4fa6a40537e61ff0fb8751d5ff147043038497216cbfb44ea0493a4e552e8696
- evidence_id: micro52-GO1990100-constraints-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990100/constraints
  locator: Exact taxonConstraints array; inherited NOT annotation blacklist not used
    for prevalence.
  accessed_at: '2026-10-22T05:57:40.728458Z'
  support: supports
  summary: The exact restriction is only_in_taxon Prokaryota, represented as the Bacteria2/Archaea2157
    union. This is an ontology taxon bound, not experimental proof of occurrence in
    either entire domain.
  snapshot_sha256: 1ed36968402927e59bf9175919bb91b6393bd0db507b2ba40f32be3f4b645b97
- evidence_id: micro52-tax562
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete taxId/scientificName/rank/lineage/otherNames native response.
  accessed_at: '2026-10-22T05:42:45.974189Z'
  support: supports
  summary: ENA taxId562 identifies Escherichia coli, rank species.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: micro52-tax83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete taxId/scientificName/rank/lineage/otherNames native response.
  accessed_at: '2026-10-22T05:42:45.974327Z'
  support: supports
  summary: ENA taxId83333 identifies Escherichia coli K-12, rank strain. Reference-entry
    taxon is not silently equated with every experimental derivative.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro52-pmid-20129058
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20129058+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED entry: exact PMID/title/authors/year/DOI and complete abstractText.
    Main-body extents, when inspected, are separate.'
  accessed_at: '2026-10-22T05:42:48.788792Z'
  support: supports
  summary: 'PMID20129058: Primase directs the release of DnaC from DnaB. Makowska-Grzyska
    M, Kaguni JM. (2010), DOI10.1016/j.molcel.2009.12.031. Complete native abstract
    and bibliographic identity read.'
  snapshot_sha256: 18745cf1f2d5ecef959d74f070a2db408991ae1dfabc6c0f90412dae32f3d9c9
- evidence_id: micro52-protein-P0ACB0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ACB0.json
  locator: Primary accession/status; gene and organism; complete relevant comments
    and InterPro/NCBIfam cross-references.
  accessed_at: '2026-10-22T05:52:56.394463Z'
  support: supports
  summary: Reviewed P0ACB0 is dnaB in E.coli K12 taxon83333. Native identity, names,
    gene/taxon, full FUNCTION/SUBUNIT/SIMILARITY and available location comments plus
    family xrefs were read.
  snapshot_sha256: edebd0e1411d58b0f8593f28aec4b2a227356105e8ab65e8095652ff58c1c3ea
- evidence_id: micro52-gene-dnaB-83333
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual URL query uses taxonomy_id:83333, gene_exact:dnaB, reviewed:true;
    complete returned identity set.
  accessed_at: '2026-10-22T05:52:58.420322Z'
  support: supports
  summary: The bounded reviewed exact-dnaB query returns the single P0ACB0 record.
    This descendant-inclusive query also confirms the exact83333 returned taxon.
  snapshot_sha256: a82408ab2f13701ec5f77df653333e6715273c2cc3fcfad9fe06ad2a5cccb089
- evidence_id: micro52-protein-P0AEF0-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AEF0.json
  locator: Primary accession/status; gene and organism; complete relevant comments
    and InterPro/NCBIfam cross-references.
  accessed_at: '2026-10-22T05:57:41.897162Z'
  support: supports
  summary: Reviewed P0AEF0 is dnaC in E.coli K12 taxon83333. Native identity, names,
    gene/taxon, full FUNCTION/SUBUNIT/SIMILARITY and available location comments plus
    family xrefs were read.
  snapshot_sha256: 826b0c0f0c64c52ba43ae5cf0a1292b8080a58ce673cace11d83bd30075609a4
- evidence_id: micro52-gene-dnaC-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual URL query uses organism_id:83333, gene_exact:dnaC, reviewed:true;
    complete returned identity set.
  accessed_at: '2026-10-22T05:57:41.918085Z'
  support: supports
  summary: The bounded reviewed exact-dnaC query returns the single P0AEF0 record.
    The query is restricted to exact organism83333.
  snapshot_sha256: fc27864cb545ea3c9b7a3c83dc91170c0e5705fa1cbbde16caf3aed18c97205b
- evidence_id: micro52-ipr-IPR007692
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007692/
  locator: Full metadata identity/name/type/descriptions and integrated member signatures;
    generic background stoichiometry/mechanism is not promoted to target-specific
    evidence.
  accessed_at: '2026-10-22T05:53:37.121780Z'
  support: supports
  summary: Native InterPro:IPR007692 is a whole-protein family for the named DnaB-type
    replicative helicase class, verified by type/name and source signatures. The separate
    reviewed UniProt response corroborates membership.
  snapshot_sha256: 88b9a5d41c0b3d6be01e7510bcdc6f5b03d5f0de15075277d153421c33818e10
- evidence_id: micro52-ncbifam-NF005931
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF005931/
  locator: Full metadata identity/name/type/descriptions and integrated member signatures;
    generic background stoichiometry/mechanism is not promoted to target-specific
    evidence.
  accessed_at: '2026-10-22T05:59:07.131359Z'
  support: supports
  summary: Native NCBIfam:NF005931 is a whole-protein family for the named DnaC helicase
    loader class, verified by type/name and source signatures. The separate reviewed
    UniProt response corroborates membership. This unintegrated NCBIfam member entry
    is exact; the broader integrated DnaC/IstB group is not substituted.
  snapshot_sha256: 63575711031577fefad416d402b34107e8ddf4c110d6d81236f592c32d5a2d0c
- evidence_id: micro52-ipr-IPR028350
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028350/
  locator: Complete family name/type/description/PIRSF003073 integration and hierarchy.
  accessed_at: '2026-10-22T05:58:05.793023Z'
  support: supports
  summary: IPR028350 includes DnaC and IstB paralogs and is broader than the loader
    class; it is not proposed as the exact component grounding.
  snapshot_sha256: 3be29cf2303dad6fad08a9b29568378f2b24bf038d4478219dc538b1cc52721d
- evidence_id: micro52-makowska2010-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/instance/2819048/
  locator: 'Genuine PMC2819048 HTML: S8–S10, S14–S16, S18/S20/S21 and Figure5–7 captions.
    Original retained body also read at S1 during B51; no supplement TableS1, raw
    pixels or new structural measurement.'
  accessed_at: '2026-10-22T05:43:16.588547Z'
  support: supports
  summary: Makowska-Grzyska/Kaguni2010 directly isolates an oriC prepriming intermediate
    with DnaB/DnaC, distinguishes mutant delivery from subsequent activity and detects
    primase-plus-ribonucleotide-dependent DnaC loss. Three DnaC per hexamer is a condition-dependent
    interpretation; other ratios are explicitly not excluded.
  snapshot_sha256: 1f0bb42eee117378fcdfa5208abde24c8f46935f32d1957ff781e22c3991e586
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dnab_dnac_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:50:56Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dnab_dnac_complex.yaml'
  snapshot_sha256: edf3dd6e6cb6b73df430bad7bd952554ba826c04b67bb049a2826be41cf3b2cf
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dnab_dnac_complex.yaml --out
    /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:50:58Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dnab_dnac_complex.yaml\
    \ --out /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch52-20261022-mvuvygy1/dnab_dnac_complex-strict.tsv"
  snapshot_sha256: 0442c7d157d125dc6e38762f6557a373fa8b619d7a75d0002b93ed4b0a93025b
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml
    --causal-graphs
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T05:58:24.860971Z'
  support: supports
  summary: "data/structures/other/dnab_dnac_complex.yaml  (GO:1990100)\n  dnab_dnac_helicase_loading\t\
    dnab_helicase\tCOVERED\t->dnab_helicase (UniProtKB:P0ACB0)\n  dnab_dnac_helicase_loading\t\
    dnac_helicase_loader\tCOVERED\t->dnac_helicase_loader (UniProtKB:P0AEF0)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 1a5fd2b44858b3af069fb75cc2842754b9f929dcbcc7335cc4034fd26fcf138e
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml
    --verify
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T05:58:37.365711Z'
  support: context_only
  summary: "Traceback (most recent call last):\n  File \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 922, in <module>\n    raise SystemExit(main())\n                     ~~~~^^\n\
    \  File \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 876, in main\n    return cmd_verify(records)\n  File \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 727, in cmd_verify\n    issues = verify_records(records)\n  File \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 616, in verify_records\n    entries = fetch_entries_by_accession(all_accs)\
    \ if all_accs else {}\n              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^\n  File\
    \ \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 169, in fetch_entries_by_accession\n    for entry in json.loads(_get(url)).get(\"\
    results\", []):\n                            ~~~~^^^^^\n  File \"/private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/scripts/uniprot_genes.py\"\
    , line 134, in _get\n    raise RuntimeError(f\"UniProt unreachable after {RETRIES}\
    \ attempts: {last}\")\nRuntimeError: UniProt unreachable after 3 attempts: <urlopen\
    \ error [Errno 8] nodename nor servname provided, or not known>"
  snapshot_sha256: bae930f373e9d6c317ec328ae8fa7db473a6cdbdcab44b8a9ba4cd2d486e5aad
- evidence_id: native-verify-network
  kind: validation
  reference: /private/tmp/cellstructure-batch52-20261022-mvuvygy1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml
    --verify
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T05:59:20.715152Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dnab_dnac_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 9 collected target identifiers returned OK. PMID:20129058: UNREACHABLE;
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
  topic: Loader complex and hierarchy
  outcome: supported
  target_ids:
  - GO:1990100
  summary: The DnaB-DnaC multiprotein complex, broad/narrow synonyms and direct protein-containing-complex
    parent are correct. Separate DNA-bound loading intermediates are experimental
    context, not a requirement to retype the isolated protein complex.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-makowska2010-legacy
- assessment_id: composition
  area: grounding
  topic: Subunits and exact family distinction
  outcome: concern
  target_ids:
  - GO:1990100
  summary: Hexameric DnaB and DnaC loading roles are supported. Exact IPR007692 and
    NCBIfamNF005931 resolve the two existing protein classes; broad IPR028350 and
    the IstB-like ATP-binding domain do not. Reference entries and exact query results
    agree.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-ipr-IPR007692
  - micro52-ncbifam-NF005931
  - micro52-protein-P0ACB0
  - micro52-gene-dnaB-83333
  - micro52-protein-P0AEF0-network
  - micro52-gene-dnaC-network
  - micro52-makowska2010-legacy
  - micro52-ipr-IPR028350
- assessment_id: stoichiometry
  area: quantity
  topic: DnaC occupancy remains unresolved at class level
  outcome: supported
  target_ids:
  - GO:1990100
  summary: 'Six DnaB copies are supported. Leaving DnaC count unset is appropriate:
    the paper infers3 per hexamer from its oriC complex but explicitly discusses6:6
    and does not exclude other ratios. The narrow synonyms are not conflicting assertions
    of a single invariant count.'
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-makowska2010-legacy
- assessment_id: function
  area: evidence
  topic: Delivery versus helicase activation
  outcome: supported
  target_ids:
  - GO:1990100
  summary: Source support for DnaC-mediated DnaB delivery and initiation is direct.
    Mutant complexes can physically load DnaB yet be inactive, and primase/ribonucleotide
    conditions control DnaC release. Activity failure is not equated with absence
    of formation.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-makowska2010-legacy
- assessment_id: formation
  area: evidence
  topic: Formation necessity remains unknown
  outcome: unknown
  target_ids:
  - GO:1990100
  summary: Every existing component essentiality is UNKNOWN. Source-supported participation,
    catalytic effects, viability and condition-specific complex recovery do not automatically
    establish universal structure-formation necessity. The present unknown labels
    are retained.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-makowska2010-legacy
- assessment_id: protein-examples
  area: grounding
  topic: Verified native protein identities and query scope
  outcome: supported
  target_ids:
  - GO:1990100
  summary: All maintained accessions, genes, reviewed status and K12 taxon pairs agree
    with native responses; single-entry claims are checked against actual query results.
    Gene taxonomy and exact-organism queries remain distinguished. Optional extra
    protein examples are not required.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-protein-P0ACB0
  - micro52-gene-dnaB-83333
  - micro52-protein-P0AEF0-network
  - micro52-gene-dnaC-network
- assessment_id: taxonomic-scope
  area: scope
  topic: Species scope and COMMON semantics
  outcome: supported
  target_ids:
  - GO:1990100
  summary: E.coli and K12 identities are exact. COMMON retains its schema meaning
    present in most members with exceptional losses; the cited E.coli experimental
    systems give qualitative support, not a measured species census. Phage substrate
    or recombinant conditions do not change the bacterial source taxon.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-makowska2010-legacy
  - micro52-pmid-20129058
- assessment_id: graph
  area: graph
  topic: Nonmechanistic graph with explicit limits
  outcome: supported
  target_ids:
  - GO:1990100
  summary: The graph is explicitly NONMECHANISTIC and uses typed protein/complex/DNA/process
    nodes. Its qualitative membership/scaffold/initiation relations are supported
    without imposing a detailed kinetic or loading mechanism.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-makowska2010-legacy
  - graphs
  - micro52-pmid-20129058
- assessment_id: coverage
  area: completeness
  topic: Complete single-target assessment
  outcome: supported
  target_ids:
  - GO:1990100
  summary: All maintained fields, citations, component states, protein annotations,
    graph edges, discussions and history were reviewed. Exact actionable mappings
    are separated from unestablished optional enrichment; historical access/curation
    notes are preserved. No source beyond the declared reading tier is certified.
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-protein-P0ACB0
  - micro52-gene-dnaB-83333
  - micro52-protein-P0AEF0-network
  - micro52-gene-dnaC-network
  - micro52-ipr-IPR007692
  - micro52-ncbifam-NF005931
  - micro52-makowska2010-legacy
findings:
- finding_id: F1
  issue_key: dnab-dnac-complex-exact-component-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve verified existing component-class groundings
  description: DnaB exactly maps to InterProIPR007692 and DnaC to the unintegrated
    but exact NCBIfamNF005931. Broad DnaC/IstBIPR028350 is not the proposed match.
    Native family/ontology identities plus independently inspected protein cross-references
    establish the matches. The current reviewed-label-only/open-task representation
    leaves these actionable classes unresolved. Historical earlier-pass statements
    are not declared false merely because current verification is available.
  target_ids:
  - GO:1990100
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - schema
  - micro52-go-network
  - micro52-GO1990100-ancestors-network
  - micro52-GO1990100-constraints-network
  - micro52-tax562
  - micro52-tax83333
  - micro52-ipr-IPR007692
  - micro52-ncbifam-NF005931
  - micro52-protein-P0ACB0
  - micro52-gene-dnaB-83333
  - micro52-protein-P0AEF0-network
  - micro52-gene-dnaC-network
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and claim-level primary-source scope
  native_severity: minor
  normalization_reason: The correct named classes and example identities are retained.
    This is a bounded exact-grounding gap under the explicit local contract, not missing
    optional inventory.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:1990100
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_complex.yaml
    role: maintained scientific record
  description: Add the verified exact class CURIEs with source-specific evidence,
    update the corresponding grounding states/open task, and preserve organism accessions
    as examples. Do not force a broader homolog/domain or unresolved PAS-DNA mapping.
  acceptance_checks:
  - Every added CURIE denotes the existing class at the stated scope, not an individual
    species protein.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- Makowska body was read at S8–S10/S14–S16/S18/S20/S21 and Figure5–7 captions. Supplement
  TableS1 and figure pixels were not inspected; exact derivative strains are not invented
  from the K12 description.
- The review does not turn a3:6 occupancy interpretation into invariant class stoichiometry.
  Later structural references in native annotations were not independently read as
  primary bodies.
- Initial sandbox fetch/verification DNS failures and successful public-network retries
  are retained separately. Exact source URL, original UTC and SHA are preserved for
  every reused pair.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user requests one review for every unreviewed record, including qualified clean
  records.
- Native ontology/UniProt/family adapters directly answer these component claims.
  No iModulonDB dataset is established or used; computational expression-module membership
  would not prove physical complex formation.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
